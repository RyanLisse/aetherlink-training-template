# AetherLink training glossary

Use this page whenever a new term appears. In the Site, open **Glossary** in
the top bar; it is available from every slide.

| Term | Definition |
|---|---|
| Model | Predicts and generates language; by itself it is not an agent. |
| Chat | A model with a conversation and context, waiting for your next message. |
| Agent | A model in a loop with a goal, tools, feedback and a boundary. |
| Agentic loop | Gather context → take action → verify results → repeat or stop at a human gate. |
| Tool | A capability exposed by the harness, such as reading, calculating or checking. |
| Harness | The system around a model that supplies context, tools, permissions and feedback. |
| Human gate | A deliberate pause where a person accepts, revises, parks or redirects the work. |
| Trace | A record of observed lifecycle and successful tool events; it does not prove correctness. |
| Hook | A deterministic rule at a lifecycle point, such as blocking a Write before it happens. |
| Evaluator | A separate reviewer that checks output against a written contract and returns PASS or REVISE. |
| OPEN | Evidence, access or a decision is unavailable or has not been run yet. |
| intent.md | The human starting brief written before design or build: what we want, why it matters, within which boundaries. Unknowns are marked OPEN, not guessed. |
| Evidence rule | A claim counts only with a source (row id or file at the cutoff), a reproduced check (command, calculation or sheet) and a reviewer who reran it. Anything less is a hypothesis. |
| MOB programming | One task, one screen, one human driver. The navigator directs, the skeptic asks for source ids, the scribe records decisions. Rotate every 5–7 minutes; anyone may say "pause". |
| Contract | The shared functional instruction (shared-prompt.md plus the ticket input): what the agent must produce and must not do, identical on every platform. |
| Adapter | The platform-specific way a contract is wired in: system message, model, mode, access and tools in n8n or Claude Code. Recorded per platform, never part of the contract. |
| Subagent | An agent another agent delegates to, with its own context and a narrower task. |
| Checkpoint | The observable condition on a slide that must be true before the group moves on. Marked passed by a human, never assumed. |
