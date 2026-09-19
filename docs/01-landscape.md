# The Landscape

There are three tracks for transferring AI knowledge into a human. Only one is
operational for a normal person in 2026.

## Track 1 — Invasive BCI

Read neural signals from cortex via implanted electrodes. Restores function for
paralyzed patients. Cannot write semantic content into a brain.

**Verdict:** sci-fi for knowledge transfer. Will not be a 2026 or 2030 product.
See `02-track1-bci.md`.

## Track 2 — Non-invasive neuromodulation

Stimulate the brain or peripheral nerves during learning to amplify
neuroplasticity. Real but modest gains (~30% on narrow tasks).

**Verdict:** real, deployable as tDCS at home, useful as a multiplier on
deliberate practice but not a replacement for it. See `03-track2-neuromod.md`.

## Track 3 — AI-driven cognitive acceleration

Use frontier LLMs to extract expert procedural knowledge, compress it into
spaced-repetition schedules, and pair with deliberate practice.

**Verdict:** the only track that scales today. Compresses 5-year apprenticeships
into 6-18 months for most knowledge domains. See `04-track3-ai.md`.

## How they combine

The real-world Matrix stack uses all three where they work:

```
Track 3 (AI extraction + scheduling)  ← the engine
   +
Track 2 (tDCS during practice)        ← optional 1.2-1.4× multiplier
   +
Track 1 (BCI)                          ← not yet, ignore
```

See `05-the-stack.md` for the operational pipeline.


## Update 2026-09-19

Two additions since May, both in the docs:

- **Write side of Track 1** now has hard human data (Pitt / UChicago touch,
  Jul 2026) and it confirms the verdict: percepts yes, concepts no. See
  `02-track1-bci.md`.
- **Track 3 becomes closed-loop.** The AI reads learner state (latency up to
  EEG) and adapts difficulty, timing and consolidation cues every cycle.
  Sham-controlled results now exist on EEG-class hardware. See
  `06-closed-loop.md`. This is the realistic near-term product, not upload.

Diagram becomes:

```
Track 3 (AI extraction + scheduling + closed-loop control)  ← the engine
   +
Track 2 (TMR in sleep, tDCS during practice)                ← multiplier
   +
Track 1 (BCI)                                                ← still ignore
```
