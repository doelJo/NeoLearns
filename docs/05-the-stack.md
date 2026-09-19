# The Stack

The operational pipeline. Read this one. Skip the others if you're in a hurry.

## Six steps

```
[1] DEFINE THE SKILL
    Pick one domain, narrow.
    Bad:  "AI"
    Good: "build production agent harnesses in TypeScript"
    Concrete: there must be a thing future-you can ship as proof.

[2] EXTRACT EXPERT TRACE
    Use pipeline/extract_skill_prompt.md against a frontier model.
    Output: skills/<skill-name>.md
    The artifact contains: prereq map, minimal example, failure modes,
    20 heuristics, 5 worked hard problems, smell tests.

[3] CONVERT TO ACTIVE RECALL
    Run pipeline/generate_cards.py.
    Cards must be:
      - Cloze deletions of heuristics
      - "What goes wrong if X" problem prompts
      - Worked-example reproductions
    Cards must NOT be:
      - Definitions
      - "What is X" prompts
      - Multiple-choice
    Push to Anki via AnkiConnect. FSRS-6 schedules review.

[4] DELIBERATE PRACTICE WITH FEEDBACK
    25-50 min focused sessions.
    You write code or solve problems → frontier model reviews → you fix.
    The skill compiles into wetware here, not in step 3.
    Anki keeps the scaffolding from rotting.

[5] OPTIONAL NEUROMOD STACK
    - tDCS (~$300, NeuroMyst or LIFTiD): anodal over left DLPFC, 20 min
      during practice. Multiplier ~1.2-1.4×.
    - HRV biofeedback (HeartMath / Elite HRV): 5 min before session.
    - Sleep: 7-9 hours, prioritize REM. Non-negotiable.

[6] OUTPUT TEST
    Teach it back. Public post, project ship, or live explanation to a
    hostile reviewer.
    If you cannot defend it under questioning, you do not have it.
    Loop back to step 4 on the gaps surfaced.
```

## Cadence

| Phase | Duration | Daily commitment |
|---|---|---|
| Bootstrap (step 1-3) | 1-2 days | Heavy — 4-6 hr |
| Compile (step 4) | 6-12 weeks | 1-2 hr deliberate practice + 15 min Anki |
| Output test (step 6) | 1-2 weeks | Ship the thing |

For most skill domains: **6-18 months from zero to functional expert**, vs the
~5-year apprenticeship that was the previous floor. The compression comes from
step 2 (extraction) and step 3 (scheduling), not from working harder.

## Failure modes

1. **Skipping step 2.** Asking "teach me X" gets a textbook. You need the
   procedural layer.
2. **Definition cards.** Anki full of "What is X?" cards is busywork. Cards
   must test recall of *non-obvious decisions*, not vocabulary.
3. **No deliberate practice.** Anki without step 4 produces trivia knowledge,
   not skill. The cards exist to keep the scaffolding from rotting.
4. **Skipping output test.** Without shipping, you cannot tell signal from
   illusion of competence.
5. **Buying tDCS first.** Buy tDCS last, after the rest of the loop is
   running. It is a multiplier on a working pipeline, not a fix for a broken
   one.

## Hardware budget

| Tier | Cost | What you get |
|---|---|---|
| **Minimum** | $0 | Anki (free) + frontier model API access ($20-50/mo) |
| **Recommended** | ~$400 | + tDCS device + HRV chest strap |
| **Maxed** | ~$2000 | + Muse / NeuroSky EEG + private fMRI access (if available) |

Minimum tier captures ~80% of the gain.


## Closing the loop (added 2026-09-19)

The six steps above are open-loop: extraction and scheduling are fixed at
step 3, and step 4 runs on feel. `06-closed-loop.md` adds the control system:

- Step 3: three difficulty tiers per heuristic.
- Step 4 target: 85% success / 15% error per session. Above 92% → harder tier.
- Step 5 order: sleep headband + closed-loop TMR first, tDCS last.
- Signals at $0: accuracy, latency, hesitation, self-rated confidence.

Hardware tiers still hold. Level 0 of the loop is the Minimum tier.
