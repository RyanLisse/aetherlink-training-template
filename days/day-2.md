# Day 2 — Institutionalise, review, and close the loop

Participant guide (English) with facilitator notes (Nederlands). This day starts from the Day 1 handoff. Work only with fictional local fixtures. The status service remains Python 3 standard library: `lookup_status(reference, records)` returns only `reference` and `status`, or `None`; `filter_status(status, records)` returns matching records with only those two fields. Valid statuses are `pending`, `settled`, and `failed`; an unknown filter status raises `ValueError`. There are no payments, network calls, credentials, persistence, or real data.

## Setup, outcomes, and evidence boundary

Use the template workflow before the session: use the GitHub template, clone the created repository, `cd` into the actual cloned repository, run `python3 --version`, and create the notes directory:

```sh
cd <actual-cloned-repository>
python3 --version
mkdir -p lab-notes
```

The agent context is the repository root plus `intent.md`, `progress.md`, the Day 1 handoff, and this guide. See [days/README.md](README.md) for the complete setup sequence.

By 16:00 you will have reproduced Day 1 evidence, added and tested `filter_status`, drafted institutional knowledge, completed independent read-only review tasks, distinguished tests from evals, and rehearsed a local-only release and incident loop. Release and incident notes are training artifacts. Update the root `progress.md` only with observed training completion, exact commands, links, and open tasks; never write fictional production outcomes there.

## Schedule — 09:00–16:00 (420 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 09:00–09:15 | 15 | Opening quiz, wordcloud, Day 1 retrieval |
| 09:15–10:15 | 60 | Exercise 1: reproduce and extend the status service |
| 10:15–10:25 | 10 | Break |
| 10:25–11:25 | 60 | Exercise 2: institutional knowledge in `CLAUDE.md` and skills |
| 11:25–11:35 | 10 | Break |
| 11:35–12:00 | 25 | Advanced source map: evals, review, hooks, deployment, metrics |
| 12:00–13:00 | 60 | Lunch |
| 13:00–14:10 | 70 | Exercise 3: independent parallel review and tests versus evals |
| 14:10–14:20 | 10 | Break |
| 14:20–15:20 | 60 | Exercise 4: conceptual hooks and LOCAL-only release rehearsal |
| 15:20–15:30 | 10 | Break |
| 15:30–15:50 | 20 | Exercise 5: metric fixture, incident intent, and teachback |
| 15:50–16:00 | 10 | Individual check-in, mob reflection, transfer task |

Total: **420 minutes**, including 60-minute lunch and four 10-minute breaks.

## Exercise 1 — Reproduce Day 1 and add filtering (60 minutes)

**Timebox and roles:** 10 minutes handoff read; 15 minutes Day 1 reproduction; 20 minutes implementation; 10 minutes tests; 5 minutes evidence check. Rotate retriever, implementer, test runner, and evidence keeper.

**Copy-ready prompt**

```text
Read lab-notes/handoff-day-1.md, lab-notes/intent.md, lab-notes/spec.md, and lab-notes/plan.md. Reproduce the Day 1 proof from the repository root: python3 -m unittest discover -s training-lab/tests/day1 -v and python3 training-lab/status.py TX-100. Then implement only the accepted Day 2 addition filter_status(status, records) in training-lab/status.py. It returns a list of new dicts containing only reference and status for matching records. Valid statuses are pending, settled, failed. An unknown status raises ValueError. Use fixture records only and no payments, network, credentials, persistence, or real data. Run python3 -m unittest discover -s training-lab/tests/day2 -v. Explain failures before edits.
```

**Numbered participant actions**

1. Read the Day 1 handoff and verify its claims by running both exact Day 1 commands.
2. Record observed output in `lab-notes/reproduction-day-2.md`; do not copy an unverified “pass.”
3. Inspect the Day 2 starter/tests supplied by the lab lane and preserve unrelated edits.
4. Implement `filter_status(status, records)` with the exact valid-status and `ValueError` contract.
5. Run `python3 -m unittest discover -s training-lab/tests/day2 -v` from the repository root.
6. Check known filters, empty matches, unknown status, and output field allow-list.
7. After human review, create a local checkpoint: `git add training-lab/status.py training-lab/tests/day2 lab-notes/reproduction-day-2.md && git commit -m "training: implement day 2 filter"` (do not push).

**Expected artifacts and sample outputs**

`lab-notes/reproduction-day-2.md` records the two Day 1 commands and their actual result. A passing Day 2 run ends with `OK`. Equivalent examples:

```python
filter_status("pending", records) == [{"reference": "TX-100", "status": "pending"}]
filter_status("settled", records) == [{"reference": "TX-101", "status": "settled"}]
filter_status("failed", records) == [{"reference": "TX-102", "status": "failed"}]
filter_status("unknown", records)  # raises ValueError
```

**Acceptance checklist:** Day 1 commands were actually rerun; Day 2 unittest command passes; all three valid statuses work; no-match is an empty list; unknown status raises `ValueError`; each output dict has exactly `reference` and `status`; no external effects.

**Stuck/fallback:** if Day 1 reproduction fails, quote the assertion and mechanism in the reproduction note before touching Day 2. If starter/tests are missing, report the exact missing path and use the examples as a manual check. Never turn a missing test into a claimed pass.

## Exercise 2 — Make knowledge operational (60 minutes)

**Timebox and roles:** 15 minutes extract conventions; 20 minutes draft; 15 minutes trigger review; 5 minutes policy-owner decision; 5 minutes scribe. Rotate maintainer, new joiner, policy owner, and scribe.

**Copy-ready prompt**

```text
Read the status service artifacts and the course principles. Draft a short repository-root CLAUDE.md for a new joiner: commands, Python 3 standard-library convention, fixture-only safety, output allow-list, and common mistakes. Draft a skill at .claude/skills/status-contract/SKILL.md that triggers when changing or reviewing the status functions and requires the three valid statuses, ValueError for an unknown filter, None for an unknown lookup, and tests before claims. Keep both files concise. Explain that a skill is advisory until a deterministic check or human review enforces it. Do not add network, credentials, or real data.
```

**Numbered participant actions**

1. List the repeatable facts a new joiner needs after seeing Day 1’s mistakes.
2. Write `CLAUDE.md` with commands and “things the agent gets wrong,” keeping it under one page.
3. Write `.claude/skills/status-contract/SKILL.md` with valid frontmatter and a clear trigger.
4. Have a new joiner try three phrasings of a status change and predict whether the skill should trigger.
5. Mark the skill’s limits: it guides behavior; it does not prove enforcement.
6. Record the policy owner and review decision. Do not claim a trigger test ran unless it did.
7. After human review, create a local checkpoint: `git add CLAUDE.md .claude/skills/status-contract/SKILL.md && git commit -m "training: document status contract"` (do not push).

**Expected artifacts and sample output**

`CLAUDE.md` includes:

```markdown
## Commands
python3 -m unittest discover -s training-lab/tests/day1 -v
python3 -m unittest discover -s training-lab/tests/day2 -v
python3 training-lab/status.py TX-100
## Conventions
Python 3 stdlib; fixture records only; return only reference/status.
## Things the agent gets wrong
Unknown lookup is None; unknown filter status is ValueError; never add network or real data.
```

`SKILL.md` has `name: status-contract` and a description beginning “Use whenever changing or reviewing status lookup or filtering.”

**Acceptance checklist:** commands are copyable; safety and output rules are explicit; skill trigger is specific; enforcement limitation is stated; policy owner decision is recorded; no fictional trigger result.

**Stuck/fallback:** use the sample blocks and mark the trigger check “not run.” If `.claude/skills` is unavailable, keep the skill text in `lab-notes/status-contract.SKILL.md` and note the path issue. Do not turn a prompt into a hard policy claim.

## Exercise 3 — Review independently; separate tests from evals (70 minutes)

**Timebox and roles:** 15 minutes split tasks; 20 minutes independent read-only review; 15 minutes test/eval classification; 10 minutes findings review; 10 minutes record. Rotate review lead, security reviewer, eval owner, and decision maker. Review tasks run in parallel only when they are read-only and touch separate scopes; no concurrent edits.

**Copy-ready prompt**

```text
You are one of two independent reviewers. Read the current diff and artifacts without editing. Review A checks functional behavior and output allow-list. Review B checks safety, scope, and whether evidence supports the claim. Each writes a separate read-only finding in lab-notes/review-a.md or lab-notes/review-b.md. Then classify each check: a test is a deterministic case for this change; an eval is a curated regression task suite (20–50 real or representative tasks) used over time, especially after CLAUDE.md, skills, or hooks changes. Do not call the current unit tests “continuous evals.”
```

**Numbered participant actions**

1. Assign Review A and Review B separate read-only scopes and separate files.
2. Review without changing code, tests, or shared artifacts.
3. Record each finding with file, evidence, severity, and a suggested owner.
4. Label the Day 2 unittest cases as deterministic tests, not an eval suite.
5. Draft `lab-notes/eval-seed.md` with three representative future tasks and expected outcomes; label it a seed, not a completed 20–50-task eval.
6. A decision maker accepts, rejects, or requests follow-up based on findings and evidence.
7. After the decision, create a local checkpoint: `git add lab-notes/review-a.md lab-notes/review-b.md lab-notes/eval-seed.md && git commit -m "training: record independent review"` (do not push).

**Expected artifacts and sample output**

```markdown
# Review A
Finding: PASS — valid statuses and unknown ValueError are covered by Day 2 tests.
# Review B
Finding: CHECK — skill is advisory; no deterministic hook evidence supplied.
# Eval seed
1. Add a fixture field; output must remain reference/status.
2. Ask for an invalid filter; expected ValueError.
3. Remove a test; CI/eval policy should detect the gap.
```

**Acceptance checklist:** reviews are independent and read-only; findings cite evidence; no concurrent edits occurred; tests versus evals are explicitly distinguished; eval seed is not misrepresented as complete; human decision is recorded.

**Stuck/fallback:** if reviewers disagree, preserve both findings and escalate to the decision maker. If time prevents the seed, write three cases with a “future eval work” label. A test command passing does not establish a continuous-eval claim.

## Exercise 4 — Hooks conceptually; rehearse a LOCAL-only release (60 minutes)

**Timebox and roles:** 15 minutes hook design; 15 minutes gate mapping; 20 minutes local release rehearsal; 5 minutes incident note; 5 minutes rollback/readback. Rotate release manager, hook designer, verifier, and incident scribe.

**Copy-ready prompt**

```text
Design a conceptual pre-merge hook for this local lab: block a change if the Day 2 unittest command fails, if an output dict exposes fields beyond reference/status, or if a valid-status list omits pending, settled, or failed. State clearly that this exercise describes a gate; it does not prove a hook is installed or enforced. Rehearse a LOCAL ONLY release with `python3 training-lab/release_rehearsal.py --output lab-output/day-2.zip`, then record the tested artifact, commands, reviewer, and rollback (restore the prior local file). Write lab-notes/release-day-2.md and, if a check fails, lab-notes/incident-day-2.md. Do not deploy, publish, call a service, or write fictional production outcomes to root progress.md.
```

**Numbered participant actions**

1. Draw the conceptual gate: tests → allow-list check → named human release manager.
2. List what the hook would block and what remains a human decision.
3. Run the Day 2 tests, the CLI check, and `python3 training-lab/release_rehearsal.py --output lab-output/day-2.zip` locally; capture actual output.
4. Write `lab-notes/release-day-2.md` with artifact identifier (path/commit if known), commands, reviewer, timestamp, and local-only scope.
5. Simulate one failed gate on paper or with a temporary read-only thought experiment; do not damage the working tree.
6. If any real check fails, write an incident note with symptom, evidence, containment, next action, and rollback; do not modify `progress.md`.
7. After human review, create a local checkpoint: `git add lab-notes/release-day-2.md lab-notes/incident-day-2.md && git commit -m "training: record local release rehearsal"` (omit the incident path when no incident note exists; do not push).

**Expected artifacts and sample outputs**

```markdown
# Local release rehearsal
Scope: local training lab only; no deploy or publish.
Proof: python3 -m unittest discover -s training-lab/tests/day2 -v; python3 training-lab/status.py TX-100
Gate: conceptual only; installation/enforcement not evidenced.
Release manager: <name>. Rollback: restore prior local status.py.
```

```markdown
# Incident note (only if observed)
Symptom: <exact failing assertion/output>.
Containment: no release; working tree preserved.
Next action: <owner and bounded fix>. Rollback: restore prior local file.
```

**Acceptance checklist:** conceptual versus enforced hook is explicit; tests, CLI, and release command evidence are captured; `lab-output/day-2.zip` is local only; reviewer and rollback are named; incident note is evidence-based if needed; root progress contains only observed training state and open tasks.

**Stuck/fallback:** if a hook runner is absent, stop at the design and label enforcement “not installed.” If a command fails, do not release; preserve output and write the incident note. Never use a production or network endpoint for this exercise.

## Exercise 5 — Turn a fixture metric into new intent and teach back (20 minutes)

**Timebox and roles:** 5 minutes metric selection; 5 minutes intent draft; 5 minutes teachback; 5 minutes peer challenge. Rotate metric owner, originator, teacher, and skeptic.

**Copy-ready prompt**

```text
Run python3 training-lab/check_metrics.py. Use its observed synthetic 8% window, fixed 5% threshold, and breach=true as an exercise prompt. Draft lab-notes/intent-from-metric.md and update lab-notes/incident-day-2.md with the exact output, naming the desired outcome, affected users/systems, constraints, open question, and next human gate. Do not claim production monitoring or a 3-sigma result. Prepare a two-minute teachback of the artifact chain and test/eval distinction.
```

**Numbered participant actions**

1. Run `python3 training-lab/check_metrics.py` and record the observed synthetic result: 8% window versus a fixed 5% threshold, `"breach": true`.
2. Treat that breach as an exercise prompt, not production monitoring: update `lab-notes/incident-day-2.md` with the exact output and write `lab-notes/intent-from-metric.md` for the follow-up.
3. Mark the metric as a synthetic fixture and state the next human gate and evidence needed.
4. Teach back: intent → spec → plan → code/tests → review/release → metric/incident.
5. Let the skeptic ask what is observed, what is inferred, and what remains open.
6. Correct overclaims before saving the final note.
7. Use the templates at close: copy `templates/daily-recap.md` to `recaps/<YYYY-MM-DD>-day-2.md`, complete it with observed commands and open actions, and link it from `recaps/README.md`. Update root `progress.md` with only verified training state. Use `templates/knowledge-note.md` for one validated lesson as `knowledge/<YYYY-MM-DD>-day-2.md` and link it from `knowledge/README.md`, or record `NONE — no reusable learning yet`.
8. After human review, create a local checkpoint: `git add lab-notes/incident-day-2.md lab-notes/intent-from-metric.md recaps/<YYYY-MM-DD>-day-2.md recaps/README.md progress.md && git commit -m "training: close day 2 loop"` (also stage the concrete knowledge note and index if validated; do not push).

**Expected artifact and sample output**

```markdown
# Intent: respond to a synthetic metric breach (fixture exercise)
Problem: the intake artifact can omit a measurable success statement.
Proposed outcome: every accepted intent has one observable success sentence.
Metric: synthetic error-rate fixture, 8% window > fixed 5% threshold; simulation only.
Constraint: this is local training evidence, not production telemetry or a 3-sigma claim.
Next gate: product owner accepts or rejects the intent.
```

**Acceptance checklist:** exact metric command was run; 8% versus 5% and `breach: true` are recorded as synthetic fixture evidence; no production or 3-sigma claim; incident and new intent are linked; artifact chain and human gate are explained; teachback distinguishes tests from evals; constraints remain public-safe.

**Stuck/fallback:** if the metric command cannot run, record the missing command as `OPEN` and do not claim a breach. If the command runs but notes cannot be saved, preserve the exact output in the editor and tell the facilitator. A clear evidence gap is the correct output.

## Opening and closing participation

Opening Kahoot (concrete answers):

1. Is a skill a hard policy guarantee? **No; a hook or review check is the deterministic enforcement layer.** Distractors: “always,” “only if named,” “a database.”
2. Can two sessions edit the same files safely at once? **No; parallelize independent read-only work or use separate worktrees, and sequence shared edits.** Distractors: “yes automatically,” “only on Fridays,” “CI solves it.”
3. Who owns the release judgment? **A named human release manager or code owner.** Distractors: “the model alone,” “the fixture,” “the CLI.”

Wordcloud prompt: “What evidence would make you trust an AI-assisted change?”

Individual check-in: “Which artifact or gate will you use next week, and what exact command, review, or timestamp will prove it?” Mob reflection: identify a bottleneck, write five intent lines, name the missing artifact and human gate, choose leading and lagging metrics, and agree on tomorrow’s proof. Roles: originator, skeptic, policy owner, scribe.

Independent transfer task: use 4 minutes to write a four-line intent for a fictional non-payment work item; name the next spec and plan artifacts, one deterministic test, and one future eval case. Use the remaining 6 minutes for the individual check-in, mob reflection, and recap/close. Keep it local and do not claim implementation.

## Course lesson source map

All 14 public lesson pages are covered across the two days. Lessons 1–4 are practiced directly; lessons 5–14 are practiced or discussed as marked, with advanced deployment/eval topics presented as overviews where no implementation exists.

1. [Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction) — loop recap.
2. [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent) — Exercise 5 transfer.
3. [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design) — artifact chain.
4. [Plan mode](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode) — plan gate recap.
5. [CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) — Exercise 2.
6. [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) — Exercise 2.
7. [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) — Exercise 3.
8. [Feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) — Exercise 1 evidence.
9. [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci) — Exercise 3 overview.
10. [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) — Exercise 3.
11. [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates) — Exercise 4 conceptual.
12. [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) — Exercise 4 local rehearsal.
13. [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) — Exercise 5.
14. [Closing thoughts and resources](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources) — close.

Further reading: [course overview](https://academy.claude.com/courses/ai-native-sdlc-playbook), plus local `work/playbook.txt` and `work/sdlc-course/findings.md`. Video/audio were not watched or listened to for this guide.

## Facilitator notes (Nederlands)

Begin met het Day 1 handoff-document en laat deelnemers de claims opnieuw bewijzen. De lab lane levert starter, tests en traineroplossing; voeg geen eigen productievoorbeeld toe. Bij Exercise 1 is vooral het verschil tussen `None` en `ValueError` belangrijk, naast de allow-list van twee velden.

Bij Exercise 2 laat je deelnemers institutionele kennis klein houden: `CLAUDE.md` voor context, skill voor herhaalbare werkwijze. Benadruk dat een skill adviserend is. Bij Exercise 3 geef je parallelle reviewers aparte read-only scopes en aparte bestanden; geen gelijktijdige edits. Laat ze hardop zeggen waarom een unittest-suite geen continue eval-suite is.

Bij Exercise 4 is de hook conceptueel. Een lokale release rehearsal is geen deploymentbewijs. Laat de release manager en rollback expliciet opschrijven. Bij Exercise 5 run je de synthetische metric-check: 8% tegenover een vaste 5%-drempel geeft `breach: true`; schrijf dit als fixture-evidence terug naar incident en intent, zonder productieclaim of 3-sigma-claim. Werk `progress.md` bij met echte trainingscommando’s en open taken, maar nooit met fictieve productie-uitkomsten. Gebruik de recap- en knowledge-templates aan het einde.

Bij Exercise 5 mogen deelnemers geen cijfers verzinnen buiten de vaste synthetic fixture: 8% window tegenover 5% threshold. Sluit af met een korte individuele transfer en een mob-reflectie. Houd het gesprek over menselijke gates, bewijs en terugschrijven naar intent.
