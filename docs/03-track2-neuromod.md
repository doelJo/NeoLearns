# Track 2 — Non-invasive Neuromodulation

Stimulate the brain or peripheral nerves to enhance plasticity during learning.
Real, modest, deployable.

## DARPA TNT (Targeted Neuroplasticity Training)

- Peripheral nerve stim (vagus, trigeminal) triggers release of acetylcholine,
  dopamine, serotonin, norepinephrine during training.
- Eight teams, ~$50M.
- Target: 30% faster learning on language, marksmanship, cryptography, target
  discrimination, intel analysis.
- Status: program-level, not a consumer product. Translates into vagal nerve
  stim devices that are starting to appear consumer-side.

## tFUS — Transcranial Focused Ultrasound

- Acoustic energy through the skull, focused at millimeter precision.
- Spatial resolution 1-5 mm vs TMS 3-5 cm vs tDCS 5-7 cm.
- Can reach deep structures (amygdala, nucleus accumbens) non-invasively.
- 2026: Science Advances paper showed amygdala-specific modulation of threat
  acquisition and extinction. Nature Comms showed nucleus accumbens modulation
  of reward sensitivity.
- Status: research-only for cognitive enhancement. Clinical devices for
  treatment exist (essential tremor, depression).

## tDCS — Transcranial Direct Current Stimulation

- Mild electrical current (~1-2 mA) across scalp electrodes.
- Mechanism: shifts resting membrane potential, makes target neurons more or
  less likely to fire.
- The reproducible win is **concurrent stimulation with practice**, not passive
  use.

### Home devices (2026)

| Device | Price | Notes |
|---|---|---|
| **Flow** | $500-800 | First FDA-cleared (depression). Prescription. |
| **NeuroMyst** | ~$300-500 | Portable tDCS + tACS, research-grade |
| **TheBrainDriver v2.1** | ~$300 | Established consumer device |
| **LIFTiD** | ~$150 | Cheap, focus-oriented |
| **Caputron Activadose** | $200-400 | Research-grade, used in studies |

### Realistic effect size

10-20% gains on motor learning during the session. Less retention benefit if
not paired with repeated practice. Headaches and tingling under electrodes are
common; mild and transient.

## Decoded Neurofeedback (DecNef)

- fMRI decoder identifies the brain pattern associated with a target skill.
- Subject does an unrelated task; gets reward when their brain spontaneously
  produces the target pattern.
- Result: subjects acquire visual discriminations they cannot consciously
  describe. Closest published thing to "Matrix download."
- Limitation: needs a $2M MRI scanner. Currently demonstrated for low-level
  perceptual learning, not skills.

## HRV biofeedback

- Heart rate variability training (HeartMath, Elite HRV) to enter coherent
  autonomic state.
- Not learning per se — pre-conditioning to make learning sessions more
  productive (better focus, reduced anxiety).
- Useful as a 5-minute primer before deliberate practice.

## What to actually deploy at home

1. tDCS device (~$300) anodal over left DLPFC during deliberate practice.
2. HRV biofeedback (5 min) before sessions.
3. Sleep — non-negotiable. Slow-wave + REM is where consolidation happens.

That's it. Anything else is currently research-only or marketing.


## 2026-09 update — AI-personalised neuromod

Searched 2026-09-19. The shift since May: the decoder-personalised approach
that needed an fMRI scanner (DecNef) now has a sham-controlled EEG result.

### DecNef (fMRI) — still the reference

- Associative DecNef gave meaningless hiragana characters the perceptual
  meaning "dog" without participants knowing the goal (J Neurosci 2024).
- Co-adaptive DecNef (2026): the decoder updates in real time from its own
  predictions. Proof-of-concept that co-adaptation makes the target state
  easier to induce and the training more reliable.
- Jan 2026 meta-study of five DecNef experiments: large subject-to-subject
  variability in which networks reorganise. Personalisation is mandatory.

### AI-supervised EEG neurofeedback — the result that matters

- Journal of Neural Engineering 23(4), 15 Jul 2026.
- 57 healthy adults aged 41–64, sham-feedback control group.
- "Task-pretrained, subject-finetuned neurofeedback" (TPSF-NF): a deep net
  pretrained on the task, then fine-tuned to each participant's EEG.
  10–11 gamified delayed-match-to-sample sessions.
- Training group improved on all three variants of a transitive reasoning
  task (p < .01) and beat sham on every condition at posttest (p < .03).
  Lower alpha power, higher beta/gamma connectivity.
- Why it matters here: this is DecNef logic on EEG-class hardware. Per-user
  fine-tuning is the active ingredient, and it is software.

### Post-learning stimulation

- tACS, 40 Hz over posterior parietal cortex, 20 min immediately after
  learning: improved episodic memory retention (Mar 2026). Lab only, but
  NeuroMyst-class home devices can output tACS. Not yet a home protocol.

### Closed-loop targeted memory reactivation (sleep)

- Wearable EEG headband at home detects slow-wave sleep and replays the sound
  cue that was paired with a word during learning, phase-locked to the
  slow-oscillation up-state.
- +8.6% translation accuracy on cued vocabulary, no change on uncued (2025).
- Nature Comms 2025: same method on motor memory, with fMRI + EEG mechanism.
- 2026 registered RCT running on fear-extinction consolidation in social
  anxiety.
- First Track 2 method that is (a) closed-loop, (b) wearable, (c) sham-
  controlled with a positive result at home. Its evidence is cleaner than
  home tDCS. No off-the-shelf product does the cueing yet; you build it on a
  headband that exposes sleep staging.

### Revised "what to deploy at home"

1. Sleep headband with closed-loop TMR for the day's hardest items.
2. HRV biofeedback 5 min before sessions.
3. tDCS anodal left DLPFC during practice — last, as before.
4. Sleep 7–9 h, still non-negotiable. TMR only works inside it.

See `06-closed-loop.md` for how these become one loop.
