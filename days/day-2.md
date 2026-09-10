# Day 2 — Make the process repeatable and reviewable

Guided participant guide. Continue the fictional payment reconciliation from
[Day 1](day-1.md). Work from the repository root with local fixture files. The
team's existing GitLab, Jira, and Confluence workflow is the destination model;
remote actions remain outside this exercise.

## Outcome and concepts

By 16:00, the cohort has made its context reusable, performed independent
review, distinguished tests from evaluations, and rehearsed a conceptual
release gate and handoff. Hooks, CI/CD, and deployment are overview topics.

The facilitator introduces `CLAUDE.md` as durable repository context, a skill
as a repeatable procedure, and a handoff as a fresh receiver's starting point.
An independent review is produced without reading another review. A test asks
whether a known contract passes; an evaluation asks whether a workflow is
useful and safe across a defined sample. Neither alone proves production
readiness. GitLab stores branch/MR evidence, Jira tracks fictional FIN tasks,
and Confluence stores shared procedure and recap.

Use the Day 1 MOB protocol: groups of three to five, one shared task and one
screen, facilitator/timekeeper, driver and navigator rotating every 5–7
minutes, agent operator separate from human decision makers, and a respectful
“pause” rule. Every exercise below includes a human gate and observable check.

Plain-language glossary: `CLAUDE.md` is repository context read before work; a
skill is a reusable procedure; a handoff gives a fresh receiver the current
state and proof. A merge request (MR) carries reviewed file changes, while a
resolved financial case still needs source confirmation. Jira tracks work and
Confluence shares procedures and recaps. A test checks a known contract; an
evaluation checks usefulness across a defined sample.

## Schedule — 10:00–16:00 (360 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Opening, Day 1 handoff readback |
| 10:15–10:40 | 25 | Concept recap/demo: context, skills, handoffs, review |
| 10:40–11:20 | 40 | Exercise 1: make context reusable |
| 11:20–11:30 | 10 | Break |
| 11:30–12:10 | 40 | Exercise 2: independent review and tests versus evals |
| 12:10–12:30 | 20 | Trainer demo and coaching: evidence and release controls |
| 12:30–13:15 | 45 | Lunch |
| 13:15–14:00 | 45 | Exercise 3: peer handoff through team tools |
| 14:00–14:10 | 10 | Break |
| 14:10–15:00 | 50 | Exercise 4: conceptual release gate and rollback |
| 15:00–15:10 | 10 | Break |
| 15:10–15:40 | 30 | Exercise 5: recap, metric, and teach-back |
| 15:40–16:00 | 20 | Individual check-in and MOB reflection |

Total: **360 minutes**.

Opening Kahoot/wordcloud prompt: “Which claim from Day 1 can you reproduce,
and what is still OPEN?” Ask each group to name one missing source or human
decision and one blocker, without proposing a production solution.

## Exercise 1 — Reusable context (40 minutes)

Trainer explains what belongs in repository context versus a one-off prompt,
then demos a minimal `CLAUDE.md` and skill outline. MOB: rotate
driver/navigator twice; remove secrets, client claims, and stale answers.
Observable check: a new operator can find cutoff, scope, commands, and evidence
rule in under two minutes.

```text
Read the accepted Day 1 intent, spec, plan, and handoff. Draft a minimal local
CLAUDE.md section and lab-notes/payment-reconciliation-skill.md for this
fictional fixture. State context, inputs, cutoff, duplicate rule, exact
scenario-directory validation command, evidence minimum, and human gates.
Keep team URLs OPEN, add no secrets or production policy, and do not edit CSVs.
Explain why each item belongs in context or in the procedure.
```

Output: context and skill drafts. Human gate: facilitator approves each
instruction as current, scoped, and reproducible before reuse.

## Exercise 2 — Independent review and tests versus evaluations (40 minutes)

Trainer explains the difference with one arithmetic test and one usefulness
evaluation, then demos two clean read-only review contexts. MOB: split into
arithmetic and scope reviewers, rotate driver/navigator within each, and submit
findings separately. Observable check: both reviews cite source IDs and neither
relies on the other review.

```text
Review the Day 1 evidence independently in read-only mode. Review A checks
identifiers, fee/net arithmetic, duplicate quarantine, and batch totals. Review
B checks cutoff semantics, exactly five case IDs, fixture-only scope, and
reproducibility. Do not read another review before writing yours. Return PASS
or BLOCKED with source IDs and exact steps. Explain which checks are contract
tests and which are workflow evaluations.
```

Output: `lab-notes/review-arithmetic.md` and `lab-notes/review-scope.md`.
Human gate: a named reviewer compares them and records disagreements without
silently rewriting evidence.

## Exercise 3 — Peer handoff in team tools (45 minutes)

Trainer explains the GitLab → Jira → Confluence relationship and demos a local
MR body, Jira field set, and Confluence outline with `OPEN` links. MOB: rotate
driver/navigator twice; simulate a receiver opening each artifact. Observable
check: the receiver traces one case from source row to finding and owner.

```text
Prepare local drafts only from the Day 1 evidence and independent reviews:
(1) a GitLab MR title/body with branch, revision, output, source IDs, and
reviewer slots; (2) Jira fields for FIN-001 and relevant FIN-002–FIN-006; and
(3) Confluence Intent, Spec, Runbook, Recap, Knowledge, and Handoff headings.
Use OPEN for unknown keys, URLs, approvals, and statuses. Do not call remote
services or claim publication.
```

Output: `lab-notes/team-handoff-day-2.md` containing three local drafts. Human
gate: evidence owner checks every link, status, and owner against local files.

## Exercise 4 — Conceptual release control (50 minutes)

Trainer explains approval gates, hooks, CI/CD, and rollback as concepts, then
demos a gate decision table. MOB: rotate driver/navigator every 5–7 minutes;
test the gate against a deliberate missing-source-ID case. Observable check:
participants can explain why a local rehearsal is not deployment evidence.

```text
Design a conceptual gate for this local package. Require unchanged CSVs,
passing identifier/arithmetic checks, visible duplicate quarantine, exactly
five documented cases, two independent reviews, and named human acceptance.
Include a BLOCKED example, exact missing evidence, and rollback: discard the
local package and restore the prior worksheet. Label hooks, CI/CD, deployment,
and enforcement as conceptual; do not deploy or publish.
```

Output: `lab-notes/release-gate-day-2.md` and local handoff package. Human gate:
release owner accepts or blocks the rehearsal with reasons and revision.

## Exercise 5 — Metrics, recap, and teach-back (30 minutes)

Trainer explains leading versus lagging metrics and demos one tied to the
evidence log. MOB: rotate driver/navigator once; check that counts come from
observed rows, not invented thresholds. Observable check: a colleague retells
intent → spec → plan → evidence → review → handoff and names the next gate.

```text
Using only observed local evidence, draft lab-notes/day-2-recap.md and a
follow-up intent. Define one leading metric, give its count only if supported,
list five case IDs, reviewer decision, open actions, next human gate, and a
two-minute teach-back. Do not claim production monitoring, recovery, or
publication.
```

Output: recap, follow-up intent, and teach-back notes. Human gate: facilitator
accepts the recap or records OPEN items for Day 3.

## Check-in and reflection

Individually answer: “Which instruction made the work repeatable, and which
decision still requires a human?” Name one test, one evaluation, and one
release control that remains conceptual. Carry the open case and evidence chain
into Day 3. Closing check-in prompt: “Which finding can your colleague
reproduce, and what remains uncertain?”

## Day 2 source map

Canonical URLs retained from the existing guide. Text was checked; no video or
audio is claimed as watched.

| Lesson | Use |
|---|---|
| [CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) | Exercise 1 |
| [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) | Exercise 1 |
| [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) | Exercise 2 overview |
| [Feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) | Exercise 2 |
| [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci) | Exercise 2 |
| [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop) | Exercise 2/3 |
| [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates) | Exercise 4 conceptual |
| [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment) | Exercise 4 conceptual |
| [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics) | Exercise 5 |
| [Closing thoughts and resources](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources) | Close |

Further reading remains the [course overview](https://academy.claude.com/courses/ai-native-sdlc-playbook).

## Facilitator notes (Nederlands)

Laat eerst het Day 1-handoff opnieuw bewijzen. Houd `CLAUDE.md`, skills en
handoffs klein en praktisch; leg uit dat een MR-documentatie kan dragen zonder
dat een financieel geval opgelost is. Laat onafhankelijke reviews echt apart
ontstaan. Benoem dat tests en evaluaties verschillende vragen beantwoorden en
dat hooks, CI/CD en deployment vandaag conceptueel blijven. Gebruik “pauze” om
claims terug te brengen naar bron, commando en menselijke beslissing.
