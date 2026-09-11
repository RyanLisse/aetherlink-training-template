# Squad 2 Day 3 · First agent in n8n

Mode: COACHED · 10:00–16:00

Use the Day 2 plan and build one bounded read-only agent in n8n. The issue is a local repository review request. GitLab fields are mock and remain `OPEN`.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **Harness** · What is a harness? [2] → Harness · see the layers [3] → Harness · how we use it [4]
- **Agentic loop** · What is an agent? [5] → The agentic loop · see the loop [6] → The agentic loop · how we use it [7]
<!-- concepts:end -->

## Schedule

| Time | Minutes | Block | Result |
|---|---|---|
| 10:00–10:15 | 15 | Recap + theory | Agent, model, context, tools, human gate |
| 10:15–10:35 | 20 | Instruction + demo | n8n workflow and agent loop |
| 10:35–11:00 | 25 | Individual | Run the prepared workflow |
| 11:00–11:20 | 20 | Review | Inspect output against contract |
| 11:20–11:35 | 15 | Break | — |
| 11:35–12:00 | 25 | Group practice | Improve one boundary |
| 12:00–13:00 | 60 | Lunch | — |
| 13:00–13:15 | 15 | Theory | Tool permissions and evidence |
| 13:15–14:00 | 45 | Individual + group | Repeat on second local scope |
| 14:00–14:15 | 15 | Break | — |
| 14:15–15:05 | 50 | Transfer | Fresh reader reproduces run |
| 15:05–15:40 | 35 | Handoff | Save workflow evidence |
| 15:40–16:00 | 20 | Close | Check-in, Kahoot, wordcloud, MOB reflection |

**Prompt.** Use the prepared n8n workflow on the supplied local repository snapshot. Return findings with path, line, evidence, severity as a human field, and `OPEN` for unrun GitLab or CI checks. Make no writes.

**Checkpoint.** The run has observed input, settings, output, reviewer, and evidence gaps.

