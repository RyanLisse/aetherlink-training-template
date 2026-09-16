# Day 5 — Agent-native SDLC: n8n to Claude Code support triage

17 September workshop · Squad 1 Claude Code route (day5 deck) · 10:00–16:00.
The attached n8n workflow is the source flow. The participant implementation
lives in the [support-triage guide](https://github.com/RyanLisse/aetherlink-agent-lab/tree/main/scenarios/support-triage/README.md).

## Outcome

Each participant carries fictional `WL-1026` from the observed n8n baseline into
a read-only Claude Code run. The run produces strict JSON with `priority`
(`low`, `medium`, `high`), maps it to a draft `auto_reply`, `investigate`, or
`escalate`, preserves `ticket_id` and `risk_note`, and stops at a human gate. A
colleague can reproduce the local draft from the handoff.

No real customer record, send, refund, escalation, credential, or business-system
write is in scope.

## Source case and contract

The fictional input from the attached n8n export is:

```json
{
  "ticket_id": "WL-1026",
  "customer": "Maarten",
  "message": "I was charged twice. I need this fixed today or I will file a complaint."
}
```

The main coordinator always calls both specialist tools: **Customer Reply Agent**
for a customer-friendly draft and **Risk Agent** for `risk_note`. The attached
source coordinator output does not itself guarantee `ticket_id` or `risk_note`;
Claude Code must preserve those fields explicitly and the checker must catch a
missing field. The `Switch` maps `low → auto_reply`, `medium → investigate`,
and `high → escalate`; these remain drafts for a person to review.

The export uses static n8n memory keys. They are not isolated between tickets
or runs. Record the observed keys, treat cross-run context as `OPEN`, and do not
call a result reproducible until the run is repeated with an isolated key or no
memory. This is a training risk, not a production recommendation.

## Agent-native SDLC route

Agent-native here means applying the existing AI-native SDLC: an agent helps
produce each phase's artifact; people review evidence and decide what happens
next.

| Phase | Artifact | Literal prompt / action | Human evidence gate |
|---|---|---|---|
| **Plan** | `lab-notes/day-5-intent.md` with outcome, case, JSON contract, roles, stop rule | “Read the support-triage guide and WL-1026. State the observable result, required fields, no-send boundary, owners and OPEN questions. Do not run a business action.” | Facilitator accepts outcome, required fields and stop rule before setup. |
| **Design** | `lab-notes/day-5-design.md` with node → contract map and memory risk | “Map Ticket Input, coordinator, both specialists, Code parser, Switch and draft actions to the contract. Mark static memory keys as not isolated. Keep the main coordinator in the session.” | Reviewer checks every specialist call and route against the attached export. |
| **Build** | First Claude Code JSON preview and run record | “Use the participant guide. Confirm exactly two required specialists — Customer Reply Agent and Risk Agent — before the first run. Run the main coordinator on WL-1026 in read-only mode and show evidence that both were called.” | Human previews before saving; missing evidence stays `OPEN`. |
| **Test** | Normalized JSON, checker output, before/after trace and boundary notes | “Validate strict JSON: priority is low/medium/high; action is mapped; ticket_id is WL-1026; risk_note is non-empty and preserved. Confirm no send or refund occurred.” | Reviewer quotes the checker line and decides `PASS`, `FAIL`, or `OPEN`. |
| **Deploy** | `lab-notes/handoff-day-5.md` and local colleague reproduction | “Write the guide URL, exact prompt, model/mode, files read, traces, checker line, memory setting, gate decision, OPEN items and one local reproduction command. Draft only.” | Colleague reproduces locally; no remote or business-system write. |
| **Maintain** | Run-log feedback and one intent follow-up | “Record what the trace or validator taught us, what remains OPEN and one change to the next intent or prompt. Do not turn one run into a platform claim.” | Facilitator accepts the lesson or records `NONE — no validated learning yet`. |

## Concept slides

The opening recaps yesterday's concepts, then applies the agent-native SDLC and subagents to today's route. Site slide numbers are in brackets.

- **Agentic loop** · recap in one slide [3]
- **Human gate** · recap in one slide [4]
- **One contract, two platforms** · recap in one slide [5]
- **AI-native SDLC** · definition [6] → existing loop image [7] → six-phase application [8]
- **Plan + Design** · intent and source-to-target map [9–10]
- **Subagents** · definition [11] → visual [12] → usage [13]

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **Agentic loop** · recap in one slide [3]
- **Human gate** · recap in one slide [4]
- **One contract, two platforms** · recap in one slide [5]
<!-- concepts:end -->

## Schedule

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Welcome, route, recap, Kahoot, blocker wordcloud and Plan outcome |
| 10:15–10:35 | 20 | Theory: six phases, source translation, human control and memory risk |
| 10:35–10:55 | 20 | Demo: attached n8n flow, exactly two specialists, then first visible result |
| 10:55–11:20 | 25 | Individual Card 1: Claude Code setup and Design map |
| 11:20–11:35 | 15 | Break |
| 11:35–12:00 | 25 | Individual Card 2: first Claude run and strict JSON checker |
| 12:00–13:00 | 60 | Lunch |
| 13:00 | — | After-lunch route |
| 13:00–13:25 | 25 | Group review: n8n baseline against the translated contract |
| 13:25–13:35 | 10 | Demo: strict JSON failure and Test boundary |
| 13:35–14:00 | 25 | Individual Card 3: trace, semantic review and one improvement |
| 14:00–14:15 | 15 | Break |
| 14:15–14:35 | 20 | Human gate: accept, return or leave `OPEN` |
| 14:35–15:15 | 40 | Deploy: local colleague handoff and reproduction |
| 15:15–15:40 | 25 | Optional E2E draft, only after the core gate |
| 15:40–16:00 | 20 | Maintain: Made / Learned / Can do, run-log feedback and recap |

## Trainer preflight · before 10:00

1. Read the [participant support-triage README](https://github.com/RyanLisse/aetherlink-agent-lab/tree/main/scenarios/support-triage/README.md) in the same environment and access level learners will use. If unavailable, record the exact URL/error as `OPEN` and use the attached export only as a walkthrough source.
2. Confirm the attached export is the source case: `WL-1026`, `Maarten`, charged twice, model `gpt-5-mini`, and the two specialist tools. Remove credential IDs and metadata from recordings.
3. Confirm the coordinator is the main Claude Code session and exactly two custom specialists — Customer Reply Agent and Risk Agent — are required before the first run. Nested agents are optional and version-dependent; do not make them a dependency.
4. Prepare a weak JSON example with an invalid priority or missing `risk_note` for Test. Keep it fictional and local.
5. Confirm that no real send, refund, escalation, customer record, credential or remote write is possible. Record unavailable model, n8n login or Claude access as `OPEN`.
6. Keep the attached flow visible and the [day5 presentation](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=1&day=5#1) open. The external support calendar may use a different historical day label; this workbook is the 17 September Squad 1 day5 route.

## Cards and literal prompts

**Card 1 — Plan + Design (10:55–11:20).** In the participant lab, follow the
support-triage README. Create the main coordinator and exactly two required
specialists — Customer Reply Agent and Risk Agent — before the first run. Use WL-1026 exactly. Record model, mode, files, tools and any
`OPEN` access issue. Map the attached n8n nodes to the translated JSON contract;
call out that the source does not guarantee `ticket_id` or `risk_note`.

**Card 2 — Build + first visible result (11:35–12:00).** Confirm the two
required specialists are configured, then invoke the main coordinator with
WL-1026. Preview the first JSON result before saving. Confirm both Customer
Reply Agent and Risk Agent were called. Normalize and validate
the three priority values, action mapping, `ticket_id`, non-empty `risk_note`,
and the no-send/no-refund boundary. Record the exact checker line.

**Card 3 — Test (13:25–14:00).** Compare the Claude Code output with the n8n
baseline. Improve one instruction only. Save before and after JSON, prompt,
trace names, model, memory setting, checker result and every `OPEN` item.

**Card 4 — Deploy (14:35–15:15).** Complete `templates/handoff.md` with the
guide URL, input, exact prompts, setup, commands, files read, traces, checker,
gate decision, boundaries and local reproduction steps. A colleague follows
the text for ten minutes and reports `reproduced`, `partially reproduced`, or
`blocked` with the reason.

**Optional Card 5 — E2E (15:15–15:40).** Only after the core gate, choose one
fictional support issue, write its intent and acceptance checks, run the same
read-only contract, and stop at the human gate. Skip it when the core handoff
is incomplete.

Close with Made / Learned / Can do. Feed only observed run-log learning back to
intent; leave model behavior, business policy and unavailable access `OPEN`.
