# NeoLearns

Real-world AI → human knowledge transfer. The closest thing to a Matrix download
that actually works in 2026.

## What this is

A working pipeline for compressing expert knowledge from frontier LLMs (Claude,
GPT, etc.) into your wetware as fast as physics and neurochemistry allow.

Not theory. A stack you run.

## The pipeline (one paragraph)

Pick a skill → have an LLM dump the procedural artifact (heuristics, failure
modes, worked problems) → convert to FSRS-6 spaced-repetition cards → drill
during deliberate practice with immediate feedback → optionally pair with tDCS
or HRV biofeedback → output test by teaching it back.

## Layout

```
NeoLearns/
├── README.md                this file
├── docs/                    research: what exists, what works, what doesn't
│   ├── 01-landscape.md      the three tracks
│   ├── 02-track1-bci.md     invasive BCI (Neuralink etc) — read-only, no upload
│   ├── 03-track2-neuromod.md non-invasive neuromod (TNT, tFUS, tDCS, DecNef)
│   ├── 04-track3-ai.md      AI-driven cognitive acceleration — where you live
│   ├── 05-the-stack.md      the actual real-world Matrix stack you run
│   ├── 06-closed-loop.md    AI-personalised closed-loop learning — the near-term product
│   └── sources.md           citations
├── pipeline/
│   ├── extract_skill_prompt.md   the prompt template for step 2
│   └── generate_cards.py         LLM trace → Anki via FSRS-6 + AnkiConnect
└── skills/                  one file per skill — extracted procedural artifacts
    └── _template.md         skeleton for new skill dumps
```

## Start here

1. Read `docs/05-the-stack.md` — the only doc that matters operationally.
   Then `docs/06-closed-loop.md` — how the stack becomes closed-loop (2026-09).
2. Pick a target skill.
3. Use `pipeline/extract_skill_prompt.md` against your favorite frontier model.
4. Save output as `skills/<skill-name>.md`.
5. Run `pipeline/generate_cards.py` to push cards to Anki.
6. Drill daily. Review weekly. Ship monthly.

## Status

Bootstrapped 2026-05-08. Pre-alpha. The pipeline script is a stub —
`generate_cards.py` works against AnkiConnect but the LLM-driven card generation
needs your API key wired in.

Enriched 2026-09-19: write-side BCI data (02), AI-personalised neuromod and
closed-loop TMR (03), the 85% rule (04), new `06-closed-loop.md`, sources.
