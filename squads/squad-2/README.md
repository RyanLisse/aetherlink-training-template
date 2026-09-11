# Squad 2 — new five-day human-agent training track

Status: `FUTURE CURRICULUM — PREFLIGHT APPROVAL: OPEN`

This directory is a new five-day track for a later squad. It starts after squad
1 finishes the existing [Day 3](../../days/day-3.md),
[Day 4](../../days/day-4.md), and [Day 5](../../days/day-5.md) material. The
existing guides remain squad 1 source material; they are not learner results,
approval, or evidence that a team ran the sessions.

Squad 2 participants use the [aetherlink-agent-lab](https://github.com/RyanLisse/aetherlink-agent-lab)
root repository for the n8n-first and Claude Code rebuild exercises. Trainers
use the fictional Northstar GitLab repository-review scenario and the
[ticket-coach workbook](../../scenarios/ticket-agent/README.md), which remains
course reference material. The scenario is local, synthetic, and read-only. Do not add real payment data,
credentials, customer details, production claims, or remote tickets. The
team's real GitLab, Jira, and Confluence destinations, access, and ticket IDs
must be supplied and approved by the team before any workflow rehearsal is
treated as live. Until then, all team links and access fields are `OPEN`.

## Track outcome

By the end of this future track, each learner can produce a small
source-backed review result, constrain and inspect a ticket-coach
agent, pass one ticket through analyst/developer/tester roles, let peers run a
local handoff workflow, and independently repeat the result with only the
date scope changed. A human accepts every artifact; an agent suggestion is never
acceptance evidence.

## Five sessions

Each session is 10:00–16:00 (360 minutes) with a shared lunch window at
12:00–13:00 and day-specific agendas. Every learner
gets at least 25 minutes of individual attempt time, including the MOB days.
After the individual block, groups of 3–4 may work together with one navigator
directing the human driver; rotate the navigator and driver every 5–7 minutes.
Anyone may say `pause`. If a group is blocked or drifting for five minutes,
the facilitator points to the source or restates the task, then parks longer
questions as `OPEN`.

| Day | Mode | New focus | Visible learner artifact |
| --- | --- | --- | --- |
| 1 | Fully guided | One small result on each learner's own laptop | One source-backed GitLab review note |
| 2 | Fully guided | Same bounded agent in n8n then Claude Code; compare `GL-REVIEW-001` before a second scope | Two same-input previews and gated transfer |
| 3 | Coached | Analyst → developer → tester relay on the same GL-REVIEW-001 request | One role-preserving review packet |
| 4 | Peer-led | Runbook and shared-skill handoff in mock GitLab/Jira/Confluence workflow | Peer-runnable runbook and handoff drafts |
| 5 | Independent | Transfer with unchanged copied repository data and a changed review scope | Recalculated review note and acceptance record |

The independent variation uses the repository fixture copied into a separate
learner directory without edits. The learner changes only the review scope,
records a second finding or `OPEN`, and shows that the baseline mirror remains
unchanged. This is a synthetic exercise, not an operating policy.

## Fixed daily agenda

| Time | Minutes | Block | Required learner action |
| --- | ---: | --- | --- |
| 10:00–10:15 | 15 | Open | Kahoot + wordcloud, goal, boundary, roles, blocker capture |
| 10:15–10:35 | 20 | Demo | Trainer introduces only the concept used in the next task |
| 10:35–11:00 | 25 | Individual attempt | Every learner works alone on the literal task card |
| 11:00–11:20 | 20 | Review | Pair or facilitator readback; record `PASS`, `FAIL`, or `OPEN` |
| 11:20–11:35 | 15 | Break | — |
| 11:35–12:00 | 25 | Practice | Small group, one navigator after individual work |
| 12:00–13:00 | 60 | Lunch | — |
| 13:00–13:15 | 15 | Check | Human acceptance against sources and the task card |
| 13:15–14:00 | 45 | Practice | Apply the morning result to the day's second case |
| 14:00–14:15 | 15 | Break | — |
| 14:15–15:05 | 50 | Transfer | Reproduce, teach back, or hand to a fresh reader |
| 15:05–15:40 | 35 | Handoff | Store artifact, evidence, owner, next action, and `OPEN` items |
| 15:40–16:00 | 20 | Close | Rating, MOB recap, Kahoot/wordcloud delta, next practice need |

## Shared acceptance rules

- Cite the exact local path and source row or command for every result.
- Keep fictional data and expected examples separate from observed learner
  output. Use `OPEN` for an unrun check, missing access, or unresolved policy.
- Human acceptance records the reviewer and decision. The agent may read,
  draft, or run an explicitly bounded local check, but cannot approve scope,
  payout, ticket state, or publication.
- The team workflow is a mock GitLab/Jira/Confluence exercise until approved
  destinations and access are recorded. Do not create or send remote records
  from this public template.
- Close every day with one personal rating (`independent`, `with help`, or
  `needs practice`) and one agreed MOB learning. Keep private feedback out of
  this repository.

## Guides and presentations

| Day | Workbook | Public guide URL | Site presentation |
| --- | --- | --- | --- |
| 1 | [day 1](day-1.md) | [GitHub guide](https://github.com/RyanLisse/aetherlink-training-template/blob/main/squads/squad-2/day-1.md) | [Present day 1](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=2&day=1#1) |
| 2 | [day 2](day-2.md) | [GitHub guide](https://github.com/RyanLisse/aetherlink-training-template/blob/main/squads/squad-2/day-2.md) | [Present day 2](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=2&day=2#1) |
| 3 | [day 3](day-3.md) | [GitHub guide](https://github.com/RyanLisse/aetherlink-training-template/blob/main/squads/squad-2/day-3.md) | [Present day 3](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=2&day=3#1) |
| 4 | [day 4](day-4.md) | [GitHub guide](https://github.com/RyanLisse/aetherlink-training-template/blob/main/squads/squad-2/day-4.md) | [Present day 4](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=2&day=4#1) |
| 5 | [day 5](day-5.md) | [GitHub guide](https://github.com/RyanLisse/aetherlink-training-template/blob/main/squads/squad-2/day-5.md) | [Present day 5](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=2&day=5#1) |

The presentation data lives in [presentations.json](presentations.json). The
JSON is intentionally separate from the existing squad 1
[day-decks.json](../../presentations/day-decks.json); the old deck is
preserved as trainer material. Both decks point learners to the lab root and
keep workbook links for trainers.

## Preflight before a future run

`OPEN — team approval, approved TRAINING GitLab repository, Jira project,
Confluence space, learner access, facilitator, and evidence owner.` The
facilitator must fill these fields in a dated local session plan and confirm
that the ticket-agent guide is present before scheduling a live run. No date,
learner result, real ticket, access grant, or external publication is claimed
by this curriculum.
