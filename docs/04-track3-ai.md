# Track 3 — AI-Driven Cognitive Acceleration

The only track that scales today. Frontier LLMs as the teacher, your wetware as
the student, structured artifacts as the bridge.

## Why this works now

Frontier models (Claude, GPT) have ingested most of the procedural knowledge
that previously lived only in expert practitioners' heads. The compression
problem flips: instead of finding the right human mentor and apprenticing,
you query a model that already has the distillation.

The bottleneck is no longer access to expertise. It is **extraction format**
and **rehearsal schedule**.

## The four research moves to know

### 1. Hugging Face Upskill (Jan 2026)

- Extracts reasoning frameworks from frontier models (literally Claude traces).
- Encodes them as executable cognitive modules for smaller models.
- Architectural shift: from weight-based knowledge transfer (fine-tuning) to
  procedural knowledge artifacts.
- The flagship demo: teaching open models to write CUDA kernels using Claude
  traces.

**Why it matters for humans:** the same technique — extract expert reasoning
trace → structured procedural artifact — works to bootstrap human learning if
you treat the artifact as a curriculum rather than a model weight update.

### 2. LECTOR (LLM-Enhanced Concept-based Test-Oriented Repetition)

- Uses LLM semantic analysis to schedule review timing.
- 90.2% retention vs 88.4% best baseline.
- Available as research code. Not yet drop-in for Anki.

### 3. FSRS-6

- Free Spaced Repetition Scheduler v6.
- Trained on ~700M reviews from ~20K Anki users.
- Best public scheduler. Drop-in for Anki via add-on.
- This is what `pipeline/generate_cards.py` targets.

### 4. Khanmigo / DeepTutor / TutorBot

- Socratic LLM tutors.
- Khanmigo: $4-9/mo. Trial data: 54% test-score lift, 30% better outcomes,
  10× engagement.
- Useful for self-paced curriculum where you want a tutor pushing back, not
  just a search engine.

## The extraction format that works

Empirically, asking an LLM "teach me X" gets you a Wikipedia summary. The right
prompt extracts the *non-obvious* layer:

1. **Prerequisite map** — what you must know before X
2. **Minimal worked example** — smallest non-trivial case
3. **Failure modes** — top 5 ways this breaks in production
4. **Heuristics** — 20 things experts notice that beginners miss
5. **Hard problems** — 5 worked solutions with reasoning shown
6. **Smell tests** — quick checks that something is wrong

This is the procedural artifact. It is what `extract_skill_prompt.md` produces.

## Why distillation-style works for humans

Same principle as model distillation: the teacher's outputs (reasoning traces,
labeled examples) are higher signal than the teacher's raw training corpus. A
human reading 50 carefully chosen worked examples learns faster than reading
500 unfiltered ones.

The limit is not what the model knows. It is your willingness to drill.


## 2026-09 update — the fifth research move

### 5. The 85% rule (Wilson et al., Nature Comms 2019)

- For any gradient-like learner, including biologically plausible networks,
  learning rate peaks when training accuracy is ~85% (error 15.87%).
- Tutors and Anki decks drift to ~95% because it feels good. That is the
  wrong side of the curve.
- Holding 85% needs continuous measurement and a controller. That turns
  Track 3 from open-loop into closed-loop. See `06-closed-loop.md`.
