# Day 4 — Build the first agent in n8n

Squad 1 · 10:00–16:00. We use the frozen Day 3 plan and the existing payment-reconciliation contract for `TICKET-OPS-101`.

## Outcome
Each participant imports and runs the n8n `ticket-coach` once, records model/tools/settings, checks the output against the contract, and writes a reproducible handoff. No Jira, GitLab, Confluence or payment-system writes.

## Cadence
Theory (agent loop and n8n harness) → facilitator demo → individual build → group review → human gate → individual improvement → MOB transfer.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **Harness** · What is a harness? [4] → Harness · see the layers [5] → Harness · how we use it [7]
- **Agentic loop** · What is an agent? [8] → The agentic loop · see the loop [9] → The agentic loop · how we use it [11]
- **One contract, two platforms** · What is "one contract, two platforms"? [12] → One contract · see the split [13] → One contract · how we use it [14]
- **Human gate** · What is a human gate? [20] → Human gate · see the decision [21] → Human gate · how we use it [22]
<!-- concepts:end -->

## Schedule
| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Recap, Kahoot and blocker wordcloud |
| 10:15–10:40 | 25 | Theory: agent loop, tools, guardrails and n8n |
| 10:40–11:00 | 20 | Demo: import workflow and inspect Calculator tool |
| 11:00–11:20 | 20 | Individual Card 1: setup |
| 11:20–11:35 | 15 | Break |
| 11:35–12:00 | 25 | Individual Card 2: first run and evidence |
| 12:00–13:00 | 60 | Lunch |
| 13:00–13:25 | 25 | Group review against ticket contract |
| 13:25–14:00 | 35 | Individual Card 3: improve prompt/output |
| 14:00–14:15 | 15 | Break |
| 14:15–14:35 | 20 | Human gate: PASS / FAIL / OPEN |
| 14:35–15:20 | 45 | Individual Card 4: handoff and rerun |
| 15:20–15:40 | 20 | MOB transfer: what would we automate next? |
| 15:40–16:00 | 20 | Recap and check-in |

## Card 1–2
Import `n8n/workflows/ticket-coach.json`, select the preflighted model credential, confirm Calculator is connected, and run once with the exact shared prompt. Save output and settings in `lab-notes/day-4-run.md`. If login or execution is unavailable, record the exact error as `OPEN`.

## Card 3–4
Check ticket identity, protected Current/Desired sections, source citations, ≥2 positive and ≥2 negative scenarios, assumptions, and `OPEN` labels. Improve only one instruction, rerun, compare traces/output, then complete `templates/handoff.md`.

Close with the daily recap and evidence only. Tomorrow rebuilds this functional contract in Claude Code.
