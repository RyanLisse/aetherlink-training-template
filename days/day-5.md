# Day 5 — Build the agent in Claude Code and transfer it end to end

Squad 1 · 10:00–16:00. Rebuild the same `ticket-coach` contract from Day 4 in Claude Code. The own-team end-to-end issue is an optional extension after the core exercise and human gate.

## Outcome
Each participant has a read-only Claude Code agent, a checked output for `TICKET-OPS-101`, a trace, and a handoff another person can reproduce. If time remains, the team applies the route to one self-selected fictional issue.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **One contract, two platforms** · What is "one contract, two platforms"? [4] → One contract · see the split [5] → One contract · how we use it [6]
- **Hooks** · What is a hook? [7] → Hooks · see the guardrail [8] → Hooks · how we use it [9]
- **Holdout scenarios** · What are holdout scenarios? [16] → Holdout scenarios · see the seal [17] → Holdout scenarios · how we use it [18]
- **Subagents** · What are parallel sessions and subagents? [22] → Subagents · see the streams [23] → Subagents · how we use it [24]
- **Measure the loop** · What does 'it got better' mean? [26] → Measure the loop · see the constant [27] → Measure the loop · how we use it [28]
<!-- concepts:end -->

## Schedule
| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Recap, Kahoot and blocker wordcloud |
| 10:15–10:40 | 25 | Theory: Claude Code platform, CLAUDE.md, tools and trace |
| 10:40–11:00 | 20 | Demo: create subagent and run read-only ticket coach |
| 11:00–11:20 | 20 | Individual Card 1: setup |
| 11:20–11:35 | 15 | Break |
| 11:35–12:00 | 25 | Individual Card 2: first run and checker |
| 12:00–13:00 | 60 | Lunch |
| 13:00–13:25 | 25 | Group review: n8n vs Claude output as observations |
| 13:25–14:00 | 35 | Individual Card 3: trace and improve |
| 14:00–14:15 | 15 | Break |
| 14:15–14:35 | 20 | Human gate: accept core result |
| 14:35–15:15 | 40 | Individual Card 4: handoff and reproduction |
| 15:15–15:40 | 25 | Optional team E2E issue, only if core gate passed |
| 15:40–16:00 | 20 | Final recap, MOB reflection and check-in |

## Card 1–3
Create `.claude/agents/ticket-coach.md` from the starter, keep `Read`, `Glob`, and `Grep` read-only, invoke it with the shared prompt, save `participant-output/ticket-101-preview.md`, and run `python3 scenarios/ticket-agent/check_ticket.py ...`. Record model, mode, files read, trace, checker line and all `OPEN` items. Improve one instruction only after group review.

## Card 4 — handoff
Complete `templates/handoff.md` with exact prompt, setup, command, output path, checker result, trace, boundaries and reproduction steps. A neighbour must reproduce it in ten minutes.

## Optional Card 5 — own team issue
Choose one fictional reconciliation issue, write its intent and acceptance gates first, then run the same read-only agent. Stop at the human gate; do not create real Jira/GitLab/Confluence records.

Close with Made / Learned / Can do, what transfers next week, and the five-day evidence wall in `progress.md`.
