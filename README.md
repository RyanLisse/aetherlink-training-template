# AetherLink human-agent training template

This small repository helps a cohort run a repeatable human-agent learning loop. It is a reusable template: files with `TEMPLATE` in the title contain prompts and empty fields, while files under `examples/` are explicitly fictional worked examples. Do not copy an example as evidence for a live session.

## Guided training days · 09:00–16:00

Start with the [two-day programme](days/README.md). Each day includes a timed agenda, literal participant instructions, copy-ready prompts, expected outputs, checkpoints, and facilitator guidance.

| Day | Focus | Participant workbook | Interactive presentation |
| --- | --- | --- | --- |
| 1 | Intent → spec → plan → first working slice | [Day 1](days/day-1.md) | [Present day 1](https://aetherlink-training.ryanlisse.chatgpt.site/?day=1#1) |
| 2 | Feedback → review → release rehearsal → next intent | [Day 2](days/day-2.md) | [Present day 2](https://aetherlink-training.ryanlisse.chatgpt.site/?day=2#1) |

Presentation access is managed separately through ChatGPT sign-in. The workbooks and [fictional Python training lab](training-lab/README.md) are available in this public repository. Releases and monitoring in the lab are local rehearsals with synthetic data, not production operations.

Keep the root `intent.md` for the training outcome; exercise artifacts live in `lab-notes/`. Leave supplied tests intact and implement the exercise in your own template copy. The SDLC is a loop: return to an earlier phase whenever evidence changes the plan.

## Scenario and training tickets

Use the [Northstar Demo Support Desk scenario](scenarios/status-desk/README.md) to give the day exercises a shared story. It includes synthetic records, support requests, a monitoring fixture, role cards and a sequenced ticket backlog. Keep the original `training-lab/records.json` unchanged; the larger scenario dataset lives separately.

For payment operations teams, use the [daily payment reconciliation scenario](scenarios/payment-reconciliation/README.md). Compare a transaction ledger, PSP settlements, and bank credits; investigate exceptions and hand over an evidence-backed action list. This is a fictional training model, not a description of Worldline systems or policies.

## Quickstart

1. Read [intent.md](intent.md) and agree on the outcome, today's boundary, owners, and evidence checks.
2. Copy [templates/session-plan.md](templates/session-plan.md) into a dated working note. Assign a human facilitator, agent operator, reviewer, and evidence owner.
3. Choose the relevant Plan, Design, Build, Test, Deploy, and Maintain phases for the session. Record `NOT IN SCOPE` with a reason for every phase you do not select. Capture links, commands, screenshots, or recordings as they become available.
4. Complete [templates/daily-recap.md](templates/daily-recap.md), update [progress.md](progress.md), and add the recap to the relevant [recaps index](recaps/README.md). State what was verified, what remains open, and who owns each action.
5. If the session produced validated learning, extract one reusable lesson into [templates/knowledge-note.md](templates/knowledge-note.md); otherwise record `NONE — no reusable learning yet`. Separate validated source material from hypotheses.
6. If work changes hands, complete [templates/handoff.md](templates/handoff.md) with fresh verification instructions and a named receiver.

The worked example in [examples/fictional-session-recap.md](examples/fictional-session-recap.md) shows how a recap links to its reusable [knowledge note](examples/fictional-knowledge-note.md).

## Use this template on GitHub

Select **Use this template** on the repository page, create a new repository, and clone that copy. Keep `intent.md`, `progress.md`, and `AGENTS.md` at the root. Copy the files under `templates/` into dated records as needed, then remove or retain the fictional examples according to your team's documentation policy. Review all placeholders before treating the new repository as live training material.

## Daily workflow

| Phase | Human focus | Agent focus | Evidence to capture |
| --- | --- | --- | --- |
| Plan | Define outcome, boundary, roles, and stop rule | Turn the outcome into checks and a small plan | Session plan and acceptance checks |
| Design | Review proposed flow and risks | Make assumptions and interfaces explicit | Design note, decision, or diagram link |
| Build | Keep scope clear and review changes | Implement in the assigned workspace | Diff, command, or artifact link |
| Test | Interpret failures before retrying | Run targeted checks and report exact output | Test command, result, and failure mechanism |
| Deploy | Approve the intended environment and rollback | Follow the runbook and report deployment evidence | Deployment URL, revision, or log link |
| Maintain | Decide follow-up and ownership | Monitor, document, and surface changes | Health check, issue, or handoff link |

At the end of the day, use the recap to close the loop: learning, evidence, open risks, actions, and a candidate knowledge note when learning was validated. Select only the phases needed for that outcome; record a reason beside every `NOT IN SCOPE` phase.

## Knowledge sharing routine

Reserve five minutes for a teach-back or demo of the lesson. Name the audience and the channel or document link; do not send automatic messages from this template. Have another participant try the procedure from the note, then ask a reviewer to promote the draft to `REVIEWED` only when the attempt and evidence support it. Review notes on their stated date and mark stale guidance `RETIRED` when it no longer applies. If no learning was validated, record `NONE` and skip the promotion step.

## File index

| Path | Use |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Lean operating instructions for contributors and agents |
| [LICENSE](LICENSE) | Public MIT license for the original template content |
| [intent.md](intent.md) | Series outcome, today's boundaries, owners, and evidence contract |
| [progress.md](progress.md) | Current verified state, blockers, next actions, and evidence links |
| [templates/daily-recap.md](templates/daily-recap.md) | Daily session recap form |
| [templates/knowledge-note.md](templates/knowledge-note.md) | Reusable learning note form |
| [templates/decision-adr.md](templates/decision-adr.md) | Architecture or operating decision record |
| [templates/handoff.md](templates/handoff.md) | Evidence-bound handoff form |
| [templates/session-plan.md](templates/session-plan.md) | Session agenda, roles, phases, and checks |
| [recaps/README.md](recaps/README.md) | Recap index and naming convention |
| [knowledge/README.md](knowledge/README.md) | Knowledge index and validation convention |
| [decisions/README.md](decisions/README.md) | Decision index and status convention |
| [handoffs/README.md](handoffs/README.md) | Handoff index and freshness convention |
| [examples/fictional-session-recap.md](examples/fictional-session-recap.md) | Fictional worked recap |
| [examples/fictional-knowledge-note.md](examples/fictional-knowledge-note.md) | Fictional reusable learning linked from the recap |
| [docs/README.md](docs/README.md) | Documentation map |
| [docs/example-prompts.md](docs/example-prompts.md) | Example prompts for each workflow |

## Evidence rules

Use a direct link or exact command for every completed claim. Mark missing evidence as `OPEN` and name the owner. A green historical check, an agent's statement, or a health endpoint alone does not prove the current state. Never add credentials, private client data, or secrets to this repository.

For shared handoff installation guidance, use the [shared skills pack handoff installation docs](https://github.com/RyanLisse/claude-code-skills-pack/blob/main/skills/handoff/SKILL.md). Keep this training material vendor-neutral; the linked document is a shared installation reference, not a requirement to use a particular assistant.
