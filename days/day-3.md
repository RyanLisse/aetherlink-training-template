# Day 3 — AI-native SDLC: from intent to evidence

Squad 1 · 10:00–16:00. Today follows the [AI-native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) and [Claude Academy course](https://academy.claude.com/courses/ai-native-sdlc-playbook). We do not build an agent today; we create the route that makes tomorrow's build safe and useful.

## Outcome
Each participant produces a small, reviewable change plan for the existing payment-reconciliation case (`TICKET-OPS-101`): intent, acceptance criteria, test evidence, human gates and a handoff. The existing ticket contract remains unchanged.

## Concept definition — AI-native SDLC

**AI-native SDLC = the familiar SDLC as a loop, with AI embedded at every stage and human control preserved.**

**Intent.md = what we want · why it matters · within which boundaries.**

Use the definition slide, show the loop image, then ask participants to place
their own ticket on one phase before they write the Day 3 plan.

## Theory → instruction → individual → review
Explain the six stages: **Plan → Design → Build → Test → Deploy → Maintain**. In the AI-native model the loop is shorter, while humans retain intent, review and release authority. Show how `intent.md`, `CLAUDE.md`, a ticket contract and `progress.md` connect the stages. Demonstrate one complete route on `TICKET-OPS-101`, then let each person do the same with a bounded prompt.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **AI-native SDLC** · What is an AI-native SDLC? [2] → AI-native SDLC · see the loop [3] → AI-native SDLC · how we use it [4]
<!-- concepts:end -->

## Schedule
| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:20 | 20 | Welcome, recap, Kahoot and blocker wordcloud |
| 10:20–10:50 | 30 | Theory: AI-native SDLC and agentic loop |
| 10:50–11:15 | 25 | Demo: intent → plan → acceptance gates on TICKET-OPS-101 |
| 11:15–11:30 | 15 | Break |
| 11:30–12:00 | 30 | Individual Card 1: write your route |
| 12:00–13:00 | 60 | Lunch |
| 13:00–13:25 | 25 | Group review: analyst → developer → tester handoff |
| 13:25–13:50 | 25 | Individual Card 2: revise with feedback |
| 13:50–14:00 | 10 | Human gate: freeze the plan |
| 14:00–14:15 | 15 | Break |
| 14:15–15:00 | 45 | Individual Card 3: evidence and test scenarios |
| 15:00–15:25 | 25 | MOB review in groups of 3–4 |
| 15:25–15:40 | 15 | Transfer: what changes tomorrow in n8n? |
| 15:40–16:00 | 20 | Recap, check-in, wordcloud delta and daily recap |

## Card 1 — make the route (individual, 30 min)
**Prompt:** “Read `intent.md`, `progress.md`, and `scenarios/ticket-agent/TICKET-OPS-101.md`. Create `lab-notes/day-3-plan.md` with: goal, current/desired state, Plan/Design/Build/Test/Deploy/Maintain activities, two positive and two negative Given/When/Then scenarios, exact evidence needed, human approval gates, and every unknown marked `OPEN`. Do not edit business records.”

**Done when:** a fresh reader can name the next action, the proof, and the stop condition in two minutes.

## Card 2 — handoff and revise
One person plays analyst, one developer, one tester. The analyst hands over the plan; the developer identifies one missing technical consequence; the tester checks one positive and one negative scenario. Revise only after the group has stated the evidence.

## Card 3 — evidence pack (individual, 45 min)
Add source citations, expected output shape, checker command, and a short `lab-notes/handoff-day-3.md`. Use `OPEN` for unavailable access or unrun tools. No n8n or Claude Code execution yet.

Close with Made / Learned / Can do, MOB reflection, and a link in `recaps/README.md`. Tomorrow uses this frozen plan to build the same contract in n8n.
