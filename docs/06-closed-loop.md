# Closed-Loop Learning

The realistic near-term product. Not upload. The AI reads how the brain is
responding and picks the next stimulus, the moment, and the difficulty. The
brain still does the encoding.

Written 2026-09-19. Extends Track 3 (`04-track3-ai.md`) and turns the stack
(`05-the-stack.md`) from open-loop into closed-loop.

## Why upload fails and this does not

There is no channel into the brain wider than the senses (see
`02-track1-bci.md`, 2026-09 update). Closed-loop learning accepts that and
moves the intelligence to the other side of the channel:

```
present → measure → infer state → adapt → present → ...
```

The loop runs per item, per minute. The AI adapts on every cycle instead of at
the end of a chapter. The only new channel is the *state readout*, and that can
be as cheap as response latency or as rich as EEG.

## The knobs with evidence

| Knob | Evidence | Effect |
|---|---|---|
| Difficulty | Wilson et al., Nature Comms 2019 | Learning rate peaks at ~85% success (15.87% error) |
| Timing | Spaced retrieval; FSRS-6 trained on ~700M reviews | Large, replicated. Already in the stack |
| Attention | MIT Media Lab NeuroChat; NeuroPilot (arXiv 2025); haptic lapse BCI (Springer 2026) | EEG-detected lapses → pacing / content change → higher engagement |
| Consolidation | Closed-loop TMR at home, 2025 | +8.6% on cued vocabulary, headband, sham-controlled |
| Neuromodulation | 40 Hz tACS post-learning, Mar 2026 | Better retention, lab only |
| Neurofeedback | J Neural Eng, Jul 2026 | 57 adults, sham-controlled; per-user fine-tuned nets beat sham on every reasoning variant |

The 85% rule is the one that changes behaviour. Everything else is a
multiplier on a loop that is already holding the right difficulty.

## Build ladder

Each level adds a sensor and a signal. Most of the gain arrives at level 0.

### Level 0 — no sensors

- LLM generates items from `skills/<skill>.md`, three difficulty tiers per
  heuristic.
- FSRS-6 decides *when* each item returns.
- Difficulty controller decides *how hard* the next item is, targeting 15%
  error over a rolling window of ~20 items.
- Signals: accuracy, response latency, hesitation (edits / backspaces),
  self-rated confidence.
- Weekend build. Captures the timing and difficulty knobs.

### Level 1 — webcam + keyboard

- Pupil dilation → cognitive load.
- Blink rate, gaze drift → attention lapse.
- Keystroke rhythm → fatigue.
- Policy responds: shorter items, modality switch, forced break.
- No new hardware for the learner.

### Level 2 — consumer EEG (~$250–1000)

- Muse, BrainAccess, OpenBCI. Theta / alpha band power.
- 10-min calibration per user, train a small classifier: the
  task-pretrained, subject-finetuned idea from the Jul 2026 study.
- Gates content delivery on engagement; runs the neurofeedback game.
- Sleep headband adds closed-loop TMR for the day's hardest items.

### Level 3 — lab

- Post-learning tACS, fMRI DecNef. Real effects. Not a product.

## Architecture

```
signals ──► STATE ESTIMATOR ──► { mastery[item], load, attention }
                                            │
                                            ▼
                         POLICY (contextual bandit)
                         action ∈ { difficulty, modality, pause, review }
                                            │
                                            ▼
                         LLM renders the action as content
                                            │
                                            ▼
                         learner responds ──► outcome logged ──► signals

SCHEDULER (FSRS-6)   owns long-term timing, feeds "review" candidates
NIGHTLY JOB          picks the TMR cue list from today's lowest-mastery items
```

Every action logs its outcome so the policy learns which interventions work
for *this* learner.

### Open decision — the bandit reward

The reward defines what "works" means. Decide before building level 0.

| Reward | Optimises for | Risk |
|---|---|---|
| Next-day recall | Consolidation | Slow feedback, one sample per item per day |
| Session length / engagement | Time on task | Goodharts into entertainment |
| Retention at 1 week | What we actually want | Very slow; needs a proxy during training |

Likely answer: proxy on within-session error rate near 15% plus latency
trend, and validate the proxy against 1-week retention monthly.

## Honest limits

- Consumer EEG is noisy. Per-user calibration is mandatory, not optional.
- Proven gains are 5–30%, not the 10× that neuro-marketing implies.
- The loop depends on the learner doing retrieval practice. The design problem
  is keeping them *in* the loop, not the sensors.
- "Effortless learning" claims (e.g. the 2025 Hutson AI-neurofeedback + BCI
  paper) are conceptual, with no controlled data. Skip.

## What changes in the stack

- Step 3: cards carry a difficulty tag; the generator emits three tiers per
  heuristic so the controller has something to choose from.
- Step 4: hold 85% success. Above 92% for a session means the items are too
  easy; raise the tier.
- Step 5: sleep headband + TMR moves ahead of tDCS.
- Step 6: the output test doubles as the 1-week retention probe that
  validates the reward proxy.
