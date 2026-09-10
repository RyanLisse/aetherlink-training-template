# Day 1 — From intent to a tested first change

Participant guide (English) with facilitator notes (Nederlands). Bring a terminal, an editor, and a copy of the repository. All examples use fictional data in a local training lab. Do not use payment systems, network calls, credentials, or real customer data. Course sources were text-checked; no video or audio is assumed to have been watched.

## Setup and outcomes

Use the template workflow before the session: use the GitHub template, clone the created repository, `cd` into the actual cloned repository, run `python3 --version`, and create the notes directory:

```sh
cd <actual-cloned-repository>
python3 --version
mkdir -p lab-notes
```

The agent context is the repository root plus `intent.md`, `progress.md`, and this day guide. Keep commands below relative to that repository root. The full setup handoff is in [days/README.md](README.md).

By 16:00 you will have a reviewed `lab-notes/intent.md`, `lab-notes/spec.md`, and `lab-notes/plan.md`; a first implementation of `lookup_status(reference, records)`; test evidence; and a handoff note that another person can continue. The starter is `training-lab/status.py`, a Python 3 standard-library status service. Its fixture records are:

```python
[{"reference": "TX-100", "status": "pending"},
 {"reference": "TX-101", "status": "settled"},
 {"reference": "TX-102", "status": "failed"}]
```

The function returns only `reference` and `status`. `lookup_status("TX-100", records)` returns `{"reference": "TX-100", "status": "pending"}`; an unknown reference returns `None`. Valid statuses are `pending`, `settled`, and `failed`. The service has no payments, network, or real data.

## Schedule — 09:00–16:00 (420 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 09:00–09:15 | 15 | Opening quiz, wordcloud, working agreement |
| 09:15–10:15 | 60 | Exercise 1: capture `intent.md` |
| 10:15–10:25 | 10 | Break |
| 10:25–11:25 | 60 | Exercise 2: turn intent into `spec.md` |
| 11:25–11:35 | 10 | Break |
| 11:35–12:00 | 25 | Course map, source discussion, plan-mode demonstration |
| 12:00–13:00 | 60 | Lunch |
| 13:00–14:10 | 70 | Exercise 3: write and interrogate `plan.md` |
| 14:10–14:20 | 10 | Break |
| 14:20–15:20 | 60 | Exercise 4: implement and test `lookup_status` |
| 15:20–15:30 | 10 | Break |
| 15:30–15:50 | 20 | Exercise 5: feedback loop and handoff |
| 15:50–16:00 | 10 | Individual check-in, mob reflection, transfer task |

Total: **420 minutes**, including 60-minute lunch and four 10-minute breaks.

## Exercise 1 — Capture the intent (60 minutes)

**Timebox and roles:** 10 minutes solo originator; 15 minutes Claude/partner interview; 20 minutes pair correction; 10 minutes product-owner review; 5 minutes scribe commit-ready check. Rotate originator, interviewer, reviewer, and scribe.

**Copy-ready prompt**

```text
Act as an intent interviewer. We are designing a fictional local training exercise for a Python 3 standard-library status lookup. Ask one question at a time until you can state: the problem, desired observable outcome, affected users and systems, constraints, and open questions. Keep the exercise public-safe: fixture data only, no payments, network, credentials, or real personal data. Then draft lab-notes/intent.md with author, status, and a measurable success sentence. Do not write code or invent outcomes.
```

**Numbered participant actions**

1. Start from the user problem: “A support learner needs to find the status for a fictional reference without exposing unrelated fields.”
2. Answer the interview questions in plain language; explicitly say that records are local fixtures.
3. Ask for one observable success statement: lookup of `TX-100` yields only its reference and status.
4. Correct any invented payment, network, identity, or customer details.
5. Save the result as `lab-notes/intent.md` with `status: draft`, an author name, and open questions.
6. Read it as a product owner, resolve or carry forward open questions, and explicitly accept the intent before Exercise 2 (or mark it `needs revision`).
7. After that human acceptance, create a local Git checkpoint: `git add lab-notes/intent.md && git commit -m "training: accept day 1 intent"` (do not push).

**Expected artifact and sample output**

`lab-notes/intent.md` contains:

```markdown
# Intent: fictional status lookup
Author: <name>. Status: draft.
## Problem
Learners need a safe way to look up one fixture record by reference.
## Proposed outcome
Return only reference and status for a known reference; return None when unknown.
## Affected users and systems
Participants, facilitator, and local training-lab/status.py.
## Constraints
Python 3 standard library; fixture records only; no payment, network, credentials, or real data.
## Open questions
How should invalid status filters behave in Day 2?
## Success
`TX-100` returns `{"reference": "TX-100", "status": "pending"}` and no other fields.
```

**Acceptance checklist:** problem and outcome are distinct; affected users/system are named; constraints include fixture-only and no network; open question is visible; author/status are present; success is observable and limited to reference/status.

**Stuck/fallback:** if the interview stalls, use the sample text, then circle one sentence that needs human correction. If the file cannot be saved, keep the markdown in the editor and paste it into `lab-notes/intent.md` when access returns. The facilitator resolves scope questions; never add real data.

## Exercise 2 — Produce a requirements and design spec (60 minutes)

**Timebox and roles:** 10 minutes prompt setup; 20 minutes pair generation; 15 minutes policy/edge-case review; 10 minutes product-owner decision; 5 minutes scribe. Rotate designer, policy reviewer, product owner, and scribe.

**Copy-ready prompt**

```text
Read lab-notes/intent.md. Produce lab-notes/spec.md for the smallest local Python 3 standard-library change. Define the function signature lookup_status(reference, records), input and output shape, known and unknown behavior, fixture records TX-100 pending, TX-101 settled, TX-102 failed, and explicit non-goals: no payments, network, credentials, persistence, or real data. Include acceptance examples and flagged concerns. Do not implement code.
```

**Numbered participant actions**

1. Attach or open `lab-notes/intent.md` and run the prompt.
2. Verify the spec preserves every constraint and does not add fields beyond `reference` and `status`.
3. Add examples for all three known references and an unknown reference.
4. Flag ambiguous behavior instead of guessing; resolve it as a human reviewer.
5. Save `lab-notes/spec.md`; record the product-owner decision as `accepted for local training` or `needs revision`.
6. If accepted, link the intent path at the top of the spec.
7. After human acceptance, create a local checkpoint: `git add lab-notes/spec.md && git commit -m "training: accept status spec"` (do not push).

**Expected artifact and sample output**

```markdown
# Spec: fixture status lookup
Input: reference: str, records: list[dict].
Output: dict with exactly reference and status, or None.
Known: TX-100→pending, TX-101→settled, TX-102→failed.
Unknown reference: None.
Non-goals: payments, network, credentials, persistence, real data.
Acceptance: lookup_status("TX-100", records) == {"reference":"TX-100","status":"pending"}.
Concern: preserve output allow-list if fixture rows gain extra fields.
```

**Acceptance checklist:** signature is exact; output allow-list is explicit; all fixtures and unknown behavior are covered; non-goals are explicit; tests can be derived without network; a human decision is recorded.

**Stuck/fallback:** copy the sample spec and mark unresolved points as concerns. If Claude over-designs an API, delete everything outside the function and fixture contract. If intent and spec conflict, stop and ask the product owner in the exercise; do not silently rewrite intent.

## Exercise 3 — Plan before code (70 minutes)

**Timebox and roles:** 15 minutes plan-mode read; 20 minutes engineer interrogation; 15 minutes risk review; 10 minutes acceptance; 10 minutes scribe/revision. Rotate engineer, skeptic, test owner, and approver.

**Copy-ready prompt**

```text
Read lab-notes/intent.md and lab-notes/spec.md and inspect the repository in read-only plan mode. Write lab-notes/plan.md naming files that change, order of work, risks, and proof commands. Plan only the lookup_status change. Ask me what could break and which step is riskiest before proposing implementation. Do not edit code until the plan is accepted.
```

**Numbered participant actions**

1. Open a read-only plan session and provide both artifacts.
2. Require the plan to name `training-lab/status.py` and `training-lab/tests/day1/`.
3. Ask: “What could break?”, “What is riskiest?”, and “What will prove it works?”
4. Reject any plan that introduces dependencies, network access, or unrelated files.
5. Write `lab-notes/plan.md`, including deviation handling: update the plan if implementation changes.
6. Have the approver sign the plan in a note or commit message before implementation.
7. After human acceptance, create a local checkpoint: `git add lab-notes/plan.md && git commit -m "training: accept status plan"` (do not push).

**Expected artifact and sample output**

```markdown
# Plan: lookup_status
## Files that change
training-lab/status.py; training-lab/tests/day1/test_status_lookup.py.
## Order of work
1. Inspect starter and preserve CLI behavior.
2. Implement an exact reference match and allow-listed return.
3. Run the Day 1 unittest command and the TX-100 CLI check.
## Risks
Returning the whole fixture row; changing the starter CLI; treating unknown as an exception.
## Proof
python3 -m unittest discover -s training-lab/tests/day1 -v
python3 training-lab/status.py TX-100
```

**Acceptance checklist:** files/order/risks/proof named; plan is implementable by a stranger; exact commands included; scope is local and fixture-only; human approval recorded.

**Stuck/fallback:** if plan mode is unavailable, simulate it with a read-only editor and label the artifact “manual plan-mode exercise.” If repository paths differ, inspect and record the actual path without broadening scope. Never start implementation before a human accepts the plan.

## Exercise 4 — Implement and test the first change (60 minutes)

**Timebox and roles:** 10 minutes starter inspection; 25 minutes implementation; 15 minutes tests; 5 minutes CLI proof; 5 minutes peer readback. Rotate implementer, test runner, reviewer, and evidence keeper.

**Copy-ready prompt**

```text
Implement only the accepted lab-notes/plan.md for lookup_status(reference, records) in training-lab/status.py. Use Python 3 standard library and fixture-safe behavior. Return a new dict with only reference and status for a known reference; return None for an unknown reference. Do not add payments, network, persistence, credentials, or real data. Run exactly: python3 -m unittest discover -s training-lab/tests/day1 -v and python3 training-lab/status.py TX-100. Show the outputs and explain any failure before changing code.
```

**Numbered participant actions**

1. Inspect the starter and tests supplied by the lab lane; read, do not replace, unrelated work.
2. Apply the smallest implementation consistent with the accepted plan.
3. Run `python3 -m unittest discover -s training-lab/tests/day1 -v` from the repository root.
4. Run `python3 training-lab/status.py TX-100` from the repository root.
5. Check that displayed output contains only `TX-100` and `pending` (the exact CLI formatting may follow the starter).
6. Read the diff against the spec and record pass/fail evidence.
7. After review, create a local checkpoint for the observed work: `git add training-lab/status.py training-lab/tests/day1 lab-notes/feedback.md && git commit -m "training: implement day 1 lookup"` (do not push; omit `lab-notes/feedback.md` if no feedback note was needed).

**Expected artifact and sample output**

Tests should report `OK` with the Day 1 cases. The CLI should communicate the known fixture status, for example:

```text
TX-100: pending
```

The code path must produce a dict equivalent to `{"reference": "TX-100", "status": "pending"}` and `None` for an unknown reference.

**Acceptance checklist:** exact unittest command passes; CLI command runs; known lookup returns only two keys; unknown lookup returns `None`; no network/imported dependency/real data; diff matches plan.

**Stuck/fallback:** first explain the failing assertion and mechanism in `lab-notes/feedback.md`; then make one bounded correction. If tests or starter are missing, stop and report the missing path to the facilitator, using the spec examples as a manual check. Do not claim a pass without command output.

## Exercise 5 — Feedback loop and handoff (20 minutes)

**Timebox and roles:** 5 minutes feedback check; 5 minutes fresh-context review; 5 minutes handoff writing; 5 minutes peer readback. Rotate engineer, verifier, handoff writer, and recipient.

**Copy-ready prompt**

```text
Act as a fresh verifier. Read lab-notes/intent.md, lab-notes/spec.md, lab-notes/plan.md, the current diff, and the recorded test output. Check the lookup contract, fixture-only constraints, and evidence. Do not edit files. Return PASS or BLOCKED with the exact missing proof. Then draft a concise handoff for Day 2 without inventing outcomes.
```

**Numbered participant actions**

1. Run the tests before asking a peer to look at the diff.
2. Give the artifact chain and output to a fresh reviewer who did not write the code.
3. Record PASS only if the reviewer can reproduce the commands and sees the allow-list.
4. Write `lab-notes/handoff-day-1.md` with completed artifacts, exact commands, and open Day 2 work.
5. State that Day 2 will add `filter_status(status, records)` and invalid-status behavior; do not state it is complete.
6. After the handoff review, create a local checkpoint: `git add lab-notes/handoff-day-1.md && git commit -m "training: handoff day 1"` (do not push).

**Expected handoff sample**

```markdown
# Day 1 handoff
Ready: intent/spec/plan reviewed; lookup_status scoped to fixture records.
Proof run: python3 -m unittest discover -s training-lab/tests/day1 -v; python3 training-lab/status.py TX-100.
Next: reproduce evidence, add filter_status, review independently, and rehearse a local release.
Open: verify exact Day 2 invalid-status contract.
```

**Acceptance checklist:** verifier is fresh; PASS/BLOCKED is evidence-based; handoff names paths and commands; Day 2 work is clearly open; no fictional outcome is written.

**Stuck/fallback:** if time expires, write BLOCKED with the exact missing command/output and hand the artifact chain to the facilitator. A transparent blocked handoff is acceptable; invented completion is not.

## Opening and closing participation

Opening Kahoot (concrete answers):

1. Where does the bottleneck move when agents make code faster? **Plan, review/test, and deploy.** Distractors: “only typing,” “the compiler,” “nowhere.”
2. Is the AI-native SDLC a straight line? **No, it is a loop with humans at judgment gates.** Distractors: “always six isolated phases,” “only CI,” “only design.”
3. What is the safest first artifact for a vague idea? **A reviewed, version-controlled `intent.md`.** Distractors: “production code,” “a password,” “a marketing claim.”

Wordcloud prompt: “One word for the biggest human-speed bottleneck in your current delivery process.”

Individual check-in: “What will you transfer to your next work item, and what evidence will prove it?” Mob reflection: name the current bottleneck, write five lines of intent, identify the missing artifact and human gate, choose one leading and one lagging metric, and state tomorrow’s proof. Roles: originator, skeptic, policy owner, scribe.

Independent transfer task: before the next session, take a harmless fictional work item and draft an `intent.md` with one measurable success statement and one constraint. Use 3 minutes to draft, 4 minutes to share in the mob, and 3 minutes to write the evidence target. Do not use real customer or payment data.

Close the shared template loop with observed state only: copy `templates/daily-recap.md` to `recaps/<YYYY-MM-DD>-day-1.md`, complete the recap with exact commands and open actions, and link it from `recaps/README.md`. Update root `progress.md` with verified training state (never fictional production outcomes). Use `templates/knowledge-note.md` for one validated lesson as `knowledge/<YYYY-MM-DD>-day-1.md` and link it from `knowledge/README.md`, or record `NONE — no reusable learning yet` in the recap. After human review, checkpoint these records locally with `git add lab-notes/handoff-day-1.md recaps/<YYYY-MM-DD>-day-1.md recaps/README.md progress.md && git commit -m "training: close day 1"` (also stage the knowledge note and index if validated; do not push).

## Course lesson source map

The 14 source lessons are mapped across the two days; advanced topics are discussion overviews and are not claimed as implemented in this lab.

| # | Lesson | Day 1 use |
|---:|---|---|
| 1 | [Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction) | loop and bottleneck |
| 2 | [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent) | Exercise 1 |
| 3 | [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design) | Exercise 2 |
| 4 | [Plan mode](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode) | Exercise 3 |
| 5 | [CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) | preview |
| 6 | [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) | preview |
| 7 | [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) | preview |
| 8 | [Feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) | Exercise 5 |
| 9 | [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci) | preview |
| 10 | [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) | Exercise 5 |
| 11 | [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates) | preview |
| 12 | [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) | preview |
| 13 | [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) | preview |
| 14 | [Closing thoughts and resources](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources) | close |

Further reading: [course overview](https://academy.claude.com/courses/ai-native-sdlc-playbook), and the local source notes in `work/playbook.txt` and `work/sdlc-course/findings.md`.

## Facilitator notes (Nederlands)

Houd de oefening publiek veilig: fictieve fixtures, geen betalingen, netwerk, credentials of echte persoonsgegevens. Zeg expliciet dat de lab lane starter, tests en traineroplossing levert. Laat deelnemers claims onderbouwen met command output; video’s/audio zijn niet bekeken en worden niet als bekeken gepresenteerd.

Bij Exercise 1: stuur op probleem, uitkomst, betrokkenen, constraints en open vragen. Corrigeer scope creep meteen. Bij Exercise 2: laat de product owner beslissen; de agent schrijft, de mens accepteert. Bij Exercise 3: benadruk dat plan mode eerst leest en pas na acceptatie wijzigt. Bij Exercise 4: laat eerst de fout en het mechanisme hardop uitleggen. Bij Exercise 5: geef de frisse verifier geen voorkennis uit de schrijfsessie. Beloon een eerlijke BLOCKED-status.

De 25-minuten bronbespreking is een overzicht van de 14 lessen; alleen de concrete labonderdelen zijn geïmplementeerd. Gebruik de woordwolk om team-bottlenecks te verzamelen. Sluit af met individueel transfer-antwoord en een mob-reflectie die eindigt met één bewijsstuk voor morgen.
