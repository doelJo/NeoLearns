# Track 1 — Invasive BCI

Implanted electrodes in or on cortex. Read-mostly. The "Matrix download" is not
on the roadmap.

## Active programs (2026)

| Project | Status | What it does |
|---|---|---|
| **Neuralink** | Gen-2 FDA-approved 2026; sub-100 MPa flexible polymer threads (polyimide + carbon nanotubes) eliminated micromotion-induced scarring | Reads motor intent for paralyzed patients; restores cursor and speech |
| **Synchron** | Stentrode — threaded through jugular vein, no craniotomy | Lower bandwidth, lower risk; intent decoding only |
| **Precision Neuroscience** | First 510(k) clearance among new commercial BCI; 30-day implants; 38 humans implanted | Surface array, highest electrode density, read-only |
| **Paradromics** | High-bandwidth array, IDE-stage trials | Aiming at full speech decode |
| **Blackrock Neurotech** | Utah array — research workhorse for two decades | Reference platform for cortical recording |

## Why "writing knowledge in" is not coming soon

- Reading: pick up signals from neurons. Hard but tractable.
- Writing: stimulate neurons to encode a *specific concept*. Requires knowing
  the neural code of that concept in *your* brain. We don't have that code for
  anything more complex than basic visual stimuli or motor twitches.
- Even with perfect electrodes, the encoding problem dominates.

## What invasive BCI is actually for

Restoring lost function (paralysis, locked-in syndrome, blindness). It is a
medical device category, not a learning enhancement category.

## Implication for NeoLearns

Ignore. Revisit in 2030+ if encoding-side breakthroughs happen.


## 2026-09 update — the write side

Searched 2026-09-19. The question that matters for NeoLearns is whether anyone
can *write* into cortex, not read from it. Status:

| Result | Where | What it shows | Ceiling |
|---|---|---|---|
| Pitt + UChicago touch implants | Science Translational Medicine, Jul 2026 | 5 spinal-cord-injury participants, 27 combined implant-years, 168M stimulation pulses, no serious adverse events. Persistent sensations ~1 per 23,000 trials, under 10 s, never painful. Touch stayed mapped to the hand. ~64% of electrodes still working on average; 60% after ~10 years in the longest participant | Sensations are tingle / vibration. Cannot tell silk from satin |
| Neuralink Blindsight | No human implant confirmed as of 2026-09 | Camera on glasses → 1000+ thread array in visual cortex. Monkeys oriented to stimuli in ~2/3 of trials. First humans "expected 2026", possibly Cleveland Clinic Abu Dhabi | Expected output: a grid of bright/dark dots ("Atari graphics") the brain learns to read over months |
| Wireless transcranial optogenetics | Nature Neuroscience, Dec 2025 | Implanted micro-LED array in mice writes spatiotemporal patterns across motor, somatosensory and visual cortex. Mice learn to discriminate the artificial percepts | Needs opsin-expressing neurons plus days of reward training per pattern. No human path |
| Holographic V1 stimulation | Nature Neuroscience | Stimulating the right ensemble in the dark reproduces the network activity of a visual illusion (pattern completion) | Single-cell write, mouse only |
| Hippocampal memory prosthesis (Hampson / Song, Wake Forest / USC) | J Neural Eng 2018; Frontiers Comp Neurosci, Feb 2024 | Read the firing pattern that predicts successful encoding, play it back. 11–54% recall improvement over baseline (mean ~35%). The 2024 paper used a fixed stimulation pattern tied to specific content | Boosts encoding of something you are already learning. Does not supply the content. Epilepsy patients with existing depth electrodes only |

### The bottleneck, stated precisely

Bandwidth and coding, not electrodes.

- Write bandwidth today: a few hundred crude percepts (touch, dot-grid vision).
- Nobody can encode a *concept* as a stimulation pattern. The closest thing is
  a memory prosthesis replaying the brain's own successful pattern back at it.
- Even mice need days of reward training to interpret a simple artificial
  pattern. The brain has to learn the code; the implant cannot install it.
- Every result above flows the other way: the AI learns the brain. CMU's 2026
  joint-learning loop (human and decoder adapt to one shared objective) is the
  state of the art, and it is the decoder doing most of the adapting.

### Revised implication for NeoLearns

Still ignore for knowledge transfer. Two things to watch:

1. Memory-prosthesis effect sizes. If a non-invasive proxy for "replay the
   successful encoding pattern" appears, it belongs in Track 2.
2. Blindsight first-human data. It will set the public expectation for what
   "writing to the brain" looks like: low-res percepts, months of adaptation.
