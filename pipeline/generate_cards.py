"""
NeoLearns — skill artifact → Anki cards via AnkiConnect.

Usage:
    python generate_cards.py skills/<skill-name>.md --deck "NeoLearns::<skill>"

Reads a procedural artifact produced by extract_skill_prompt.md, asks a frontier
LLM to convert it into FSRS-6-friendly Anki cards (cloze deletions of
heuristics, problem-prompt cards, smell-test cards), and pushes them to a
running Anki desktop via the AnkiConnect add-on.

Prerequisites:
    1. Anki desktop running
    2. AnkiConnect add-on installed (code 2055492159)
    3. ANTHROPIC_API_KEY (or OPENAI_API_KEY) in environment
    4. pip install anthropic requests

The card generation prompt is biased toward retrieval practice, not recognition.
Definition cards are explicitly rejected.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

import requests

ANKI_CONNECT_URL = "http://127.0.0.1:8765"
ANKI_CONNECT_VERSION = 6

CARD_GENERATION_PROMPT = """\
You are converting a procedural knowledge artifact into Anki flashcards
optimized for FSRS-6 spaced repetition.

ARTIFACT:
---
{artifact}
---

Produce flashcards as a JSON array. Each card has fields:
  - "front": the prompt
  - "back": the answer
  - "tags": list of tags (use the artifact section names)
  - "type": one of "cloze", "problem", "smell-test", "heuristic-application"

RULES:
1. NO definition cards. "What is X?" is forbidden. Test recall of decisions,
   heuristics, failure modes, and worked solutions.
2. For each of the 20 heuristics, produce 1-2 application cards: a concrete
   scenario where the front asks "what should you do here and why" and the
   back gives the heuristic plus reasoning.
3. For each of the 5 hard problems, produce 2-3 cards: one for the wrong-
   tempting approach and why it fails, one for the right approach, one for
   the reasoning trace.
4. For each smell test, produce 1 card: front shows a snippet or scenario,
   back identifies what's off.
5. For failure modes, produce cards that test root-cause identification, not
   just symptom recognition.
6. Cards should be answerable in under 60 seconds.
7. Front side must be unambiguous — no "describe X" prompts.

Return ONLY the JSON array. No prose before or after.
"""


def call_anki_connect(action: str, **params: Any) -> Any:
    payload = {"action": action, "version": ANKI_CONNECT_VERSION, "params": params}
    response = requests.post(ANKI_CONNECT_URL, json=payload, timeout=10)
    response.raise_for_status()
    body = response.json()
    if body.get("error"):
        raise RuntimeError(f"AnkiConnect error: {body['error']}")
    return body.get("result")


def ensure_deck(deck_name: str) -> None:
    decks = call_anki_connect("deckNames")
    if deck_name not in decks:
        call_anki_connect("createDeck", deck=deck_name)


def generate_cards_with_llm(artifact_text: str) -> list[dict[str, Any]]:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY not set. Export it or wire in another provider."
        )

    try:
        import anthropic
    except ImportError:
        raise RuntimeError("pip install anthropic")

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=16000,
        messages=[
            {
                "role": "user",
                "content": CARD_GENERATION_PROMPT.format(artifact=artifact_text),
            }
        ],
    )
    text = message.content[0].text.strip()

    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
        if text.endswith("```"):
            text = text[:-3].strip()

    return json.loads(text)


def push_cards(deck_name: str, cards: list[dict[str, Any]]) -> int:
    notes = []
    for card in cards:
        if card.get("type") == "cloze":
            note = {
                "deckName": deck_name,
                "modelName": "Cloze",
                "fields": {"Text": card["front"], "Back Extra": card.get("back", "")},
                "tags": card.get("tags", []),
            }
        else:
            note = {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {"Front": card["front"], "Back": card["back"]},
                "tags": card.get("tags", []) + [f"type:{card.get('type', 'basic')}"],
            }
        notes.append(note)

    results = call_anki_connect("addNotes", notes=notes)
    return sum(1 for r in results if r is not None)


def main() -> int:
    parser = argparse.ArgumentParser(description="NeoLearns card generator")
    parser.add_argument("artifact", type=Path, help="Path to skills/<skill>.md")
    parser.add_argument(
        "--deck",
        required=True,
        help='Anki deck name, e.g. "NeoLearns::ts-agents"',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print generated cards as JSON; do not push to Anki",
    )
    args = parser.parse_args()

    if not args.artifact.exists():
        print(f"Artifact not found: {args.artifact}", file=sys.stderr)
        return 1

    artifact_text = args.artifact.read_text(encoding="utf-8")
    print(f"[1/3] Generating cards from {args.artifact}...")
    cards = generate_cards_with_llm(artifact_text)
    print(f"[1/3] {len(cards)} cards generated.")

    if args.dry_run:
        print(json.dumps(cards, indent=2))
        return 0

    print(f"[2/3] Ensuring deck '{args.deck}' exists...")
    ensure_deck(args.deck)

    print(f"[3/3] Pushing {len(cards)} cards to Anki...")
    pushed = push_cards(args.deck, cards)
    print(f"[3/3] {pushed}/{len(cards)} cards added (duplicates skipped).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
