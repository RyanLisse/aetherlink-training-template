# Squad 2 · one worked example we walk through together

Status: `ACCEPTED — 2026-09-12 · squad 2 is mixed: A is the primary thread, D is the reserve; slides, prompts, n8n export and Claude Code starter built`

## Why one example

Squad 2 today has four unconnected threads: a playbook summary on Day 1, an unnamed "local example issue" on Day 2, a two-line repository snapshot on Days 3 and 4, and the team's own issue on Day 5. Nothing carries over, so the value of the AI-native SDLC never becomes visible: each day shows one stage, never the loop.

One example that runs from Day 1 to Day 5 fixes that. The same intent becomes a plan, the plan becomes an agent run in n8n, the same contract runs again in Claude Code with a guardrail, and the team gates and hands over the result. Participants see the bottleneck move from doing the work to verifying it, on data they can rerun at home.

## What the example must satisfy

| Requirement | Meaning in practice |
| --- | --- |
| Independent of their systems | Fictional data, local files only. No GitLab, Jira, CI, credentials, or network. Draft fields with `OPEN` where a real system would be. |
| Shows the value | A measurable before (human does it by hand) and after (agent does it, human verifies). At least one trap the human gate must catch. Evidence a fresh reader can rerun. |
| One contract, two platforms | The same inputs, output shape, and stop rule run in n8n on Day 3 and in Claude Code on Day 4. |
| Already in the repository | Fixtures, tickets, answer key, and checker exist. We build slides and prompts, not new data. |
| Recognisable domain | Payments or support vocabulary the squad knows, without touching their real process. |

## Candidates

All four already live under `scenarios/`.

### A · Daily payment reconciliation (recommended primary)

Folder: `scenarios/payment-reconciliation/`. Fictional merchant, three CSVs (8 ledger rows, 7 PSP settlement rows, 4 bank credits), a fixed cutoff, one fee rule, five documented cases `EX-001` to `EX-005`, six ticket templates `FIN-001` to `FIN-006`, a trainer answer key, a learner guide, a fixture checker, and a worked GitLab, Jira and Confluence handoff for `FIN-003`.

Value it shows. A human classifies the six batches by hand on Day 2 and times it. On Day 3 the agent does it in minutes and shows what it read. The human gate then has to catch three built-in traps: the duplicate row `SET-1003-B` must be quarantined and the batch stays `UNRESOLVED`, `TX-NS-1008` is a timing item and not an error, and the fee mismatch on `TX-NS-1004` stays a mismatch even though the net reaches the bank. An agent that says "all reconciled" fails the gate. That is the bottleneck moving to verification, on one screen.

Platform fit. n8n reads the three CSVs and feeds an agent node with the contract; the output is a findings table with case, evidence anchors, and `OPEN`. Claude Code reads the same files with the same contract. The fixture check in the scenario README is the ready-made hook for Day 4: no "reconciled" claim before the check passes. One subagent per batch is the natural parallel split for the subagents concept.

Risks. Squad 1 uses this case too. That is fine for different people, but the facilitator must not reuse Squad 1 evidence. It is an operations case, not a code change, so a pure engineering squad may want candidate D for Day 5.

### B · Ticket refinement (`TICKET-OPS-101` and `102`)

Folder: `scenarios/ticket-agent/`. Two fictional payment tickets, a read-only `ticket-coach` subagent, a shape checker `check_ticket.py`, and two target examples. The learner runs the agent, changes one instruction, and compares drafts.

Value it shows. Before and after with one instruction changed; the checker is a working hook. Strong for the hooks and subagents concepts on Day 4.

Why not primary. It is one artifact, a ticket draft, not a lifecycle. There is no plan, no run that produces a result to verify, and no natural n8n version. Squad 1 also built its Day 1 and 2 skill on it. Keep it as the Day 4 guardrail exercise inside candidate A, where `TICKET-OPS-101` is the same fee mismatch as `EX-003`.

### C · Repository review (`GL-REVIEW-001`, the current Day 3 and 4 thread)

Folder: `scenarios/gitlab-repository-review/`. One ticket and a `repository.json` with two files and two lines.

Why not. There is nothing to find. A "finding" on a two-line fixture looks staged, and the run proves neither speed nor judgement. Making it real means writing a fictional repository mirror with planted issues, which is new work with no answer key. Retire it from Squad 2 unless someone builds that mirror.

### D · Status desk (`SCN-001` to `SCN-007`, reserve for engineering squads)

Folder: `scenarios/status-desk/` plus `training-lab/status.py`. A Python starter with a lookup and a status filter, a public-field allow-list with a redaction negative control, twelve records, five requests with a pass or fail runner, a release rehearsal, and a synthetic error-rate fixture that turns into the next intent.

Value it shows. The full loop on real code: intent, spec, plan, implement, test, independent review, local release, maintain. The runner `run_requests.py` is a ready-made check, and the metric fixture closes the loop back to Plan.

Why reserve. n8n cannot edit Python, so Day 3 would need a different shape: the same lookup contract as an n8n workflow answering the five requests, then Claude Code implementing it in code. That is a good "one contract, two platforms" story but a heavier build. Use it when the squad is developers and wants to see code change, or as the Day 5 stretch.

## Recommendation

Primary: A, payment reconciliation. Fold B into Day 4 as the guardrail exercise. Retire C. Keep D built as the reserve for an engineering-heavy squad or the Day 5 stretch.

Several examples prepared, one example run. Preparing more than two threads dilutes the point: the value only shows through continuity. Two ready threads, A for operations and D for engineering, cover both squad profiles without splitting the week.

## The thread day by day (candidate A)

| Day | Concepts on the deck | The example step | Evidence produced |
| --- | --- | --- | --- |
| 1 | Bottleneck, AI-native SDLC, intent.md | Write `intent.md` for `FIN-001`: outcome "evidence-backed action list for the 2026-09-10 cutoff", human gate "reviewer accepts per batch", stop rule "no approval on an `UNRESOLVED` batch", one `OPEN` "who confirms the duplicate". Map Plan and Design to today, Build to Days 3 and 4, Test to checker plus gate, Deploy to handoff, Maintain to `FIN-006`. | Reviewed `intent.md` |
| 2 | Evidence rule | Plan the batch review without an agent. Inputs: three CSVs, cutoff, fee rule. Expected: five cases. Two positive checks (fee rule on `TX-NS-1001`; batch `B-20260908-01` matches bank). Two negative checks (`TX-NS-1008` must not be called overdue; `SET-1003-B` must not be counted). Then classify the six batches by hand and record the time. | Plan card, hand worksheet, baseline time |
| 3 | Agentic loop | n8n: read files, agent node with the contract, findings table with case, anchors, `OPEN`. Compare with the Day 2 worksheet. Review: which trap did the agent miss? | n8n run with settings, findings, reviewer note |
| 4 | One contract, hooks, subagents | Same contract in Claude Code. Hook: run the fixture check before any "reconciled" claim. Subagents: one per batch, then merge. Guardrail exercise: add "never approve a batch with a duplicate", rerun, compare before and after. | Trace, before and after output, hook result |
| 5 | MOB, human gate | MOB runs `FIN-003` end to end with roles. Human gate accepts or rejects per FIN ticket. Handoff into the GitLab, Jira and Confluence draft fields from `workflow.md`, links `OPEN`. Then the same shape on the team's own sanitised issue. | Gate decisions, handoff drafts, own-issue brief |

The "value" slide at the end of Day 4 puts Day 2 and Day 4 side by side: minutes spent, traps caught, evidence a fresh reader can rerun. That slide is the demonstration the request asks for.

## What was built for A

1. Six example slides (one per day plus the before-and-after slide on Day 4), generated from the `examples` block in `presentations/concepts.json` by `apply_concepts.py`, with a `Worked example` block in each workbook.
2. All 37 generic squad 2 slides (theory, individual, review, practice, gate, transfer, route, break, close) patched from the register to name the example step.
3. `scenarios/payment-reconciliation/n8n/reconciliation-agent.json` plus a rebuild recipe and `bundle-rows.js`. Status `OPEN` until run on a live n8n.
4. `scenarios/payment-reconciliation/starter/.claude/` with the `reconciliation-reviewer` subagent and a Stop hook that runs `check_fixture.py`; the contract both platforms share is `contract.md`.
5. The before-and-after slide on Day 4, filled in live.
6. `GL-REVIEW-001` removed from the Squad 2 workbooks; the scenario folder stays for other uses.

## What is still open

- Live n8n and Claude Code runs have never been executed in this repository (see `progress.md`). The n8n export and the starter need one real run before the training day.
- Whether the facilitator wants the hand-classification baseline on Day 2 to be timed per person or as a group.
