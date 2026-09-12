# Squad 2 Day 3 · First agent in n8n

Mode: COACHED · 10:00–16:00

Use the Day 2 plan and run one bounded read-only agent in n8n on the reconciliation example. The contract is `scenarios/payment-reconciliation/contract.md`; the workflow export and a ten-minute rebuild recipe are in `scenarios/payment-reconciliation/n8n/`. GitLab fields are mock and remain `OPEN`.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **Agentic loop** · What is an agent? [2] → The agentic loop · see the loop [3] → The agentic loop · how we use it [4]
<!-- concepts:end -->

<!-- example:start -->
## Worked example · daily payment reconciliation

One example runs from Day 1 to Day 5; see [worked-example.md](worked-example.md). Today's step, with the site slide number in brackets:

- **The example · first run in n8n** [5] · The Day 2 plan becomes the contract. The agent reads the same files and returns one row per batch.
  - Expected: One observed n8n run with settings, output and a disagreement list.
  - Checkpoint: The reviewer can name the trap the agent missed, or show it caught all three.
<!-- example:end -->

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
| 13:15–14:00 | 45 | Individual + group | Tighten one contract line and rerun |
| 14:00–14:15 | 15 | Break | — |
| 14:15–15:05 | 50 | Transfer | Fresh reader reproduces run |
| 15:05–15:40 | 35 | Handoff | Save workflow evidence |
| 15:40–16:00 | 20 | Close | Check-in, Kahoot, wordcloud, MOB reflection |

**Prompt.** Import `n8n/reconciliation-agent.json` or rebuild it from `n8n/README.md`. Run it once on the three CSVs. The output is one row per batch with nets, classification, row ids as evidence, next human action, and `OPEN` for anything not checked. Save the output and the model settings. Compare with your Day 2 worksheet and mark every disagreement. Make no writes.

**Checkpoint.** The run has observed input, settings, output, reviewer, and evidence gaps, and the reviewer can name which of the three traps the agent missed or show that it caught all three.

