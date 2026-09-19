# Skill Extraction Prompt

Paste this into a frontier model (Claude, GPT-4o+, etc.) with `{SKILL}` filled
in. Save the model's output to `skills/<skill-name>.md`.

This is the only prompt you need for step 2 of the pipeline.

---

```
You are a senior practitioner of {SKILL}. I am a learner who wants to acquire
this skill in 6-18 months instead of 5 years. You will produce a procedural
knowledge artifact, not an explanation.

Output the following sections, in order, in markdown:

## 1. Prerequisite Map
List the things I must already know before {SKILL} makes sense. For each:
- Name
- Why it's a prerequisite (one sentence)
- A self-test question I should be able to answer without help

## 2. Minimal Worked Example
The smallest non-trivial example of {SKILL} in action. Include:
- The setup
- The work shown step by step
- The reasoning at each step (this is the part most teachers skip)
- What the finished output looks like

## 3. Failure Modes (top 5)
The five ways this most often breaks in real-world practice. For each:
- Symptom
- Root cause
- Fix
- How an expert would have seen it coming

## 4. Twenty Heuristics
Twenty things experts notice that beginners miss. Format each as:
- The heuristic in one sentence
- A concrete example where it applied
- The cost of ignoring it

These should be the non-obvious decision rules. Avoid generic advice
("write tests", "be careful with edge cases"). I want the things you'd tell
a junior on day 100, not day 1.

## 5. Five Hard Problems with Worked Solutions
Five problems that separate intermediate from expert. For each:
- The problem statement
- A wrong-but-tempting first approach (and why it fails)
- The correct approach
- The reasoning trace, narrated as you would think it through
- What this problem teaches that nothing else does

## 6. Smell Tests
Quick checks (under 30 seconds each) that something is wrong with my work.
At least 10. These are the "this doesn't smell right" instincts experts use.

## Style Constraints
- No platitudes. No "remember to be patient with yourself."
- No padding. Every sentence earns its place.
- Concrete > abstract. Show, don't define.
- Assume I will read this 50 times and turn it into Anki cards.
- Length: long enough to be useful, no longer.
```

---

## Tips

- Use a frontier model with extended thinking enabled. This is not the place
  to save tokens.
- If the output feels generic, push back: "section 4 is too abstract, give me
  decision rules a senior would whisper to a junior in code review."
- Iterate. The first dump is rarely the keeper. Refine sections 4 and 5
  especially.
- For skills with code: ask the model to include runnable examples.
- For skills with judgment calls: ask for "the call you would make and why,
  in cases where reasonable people disagree."
