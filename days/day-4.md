# Day 4 — Agents in the AI-native SDLC, and your first hook

Fourth session for **Wave 2 crew 1**. Two concepts today:

1. **Agents in the AI-native SDLC.** The line becomes a loop; build runs at
   agent speed while requirements, review and release stay human. You choose
   **one agent** from the lab menu and build it where it sits in that loop.
2. **Hooks: see the loop, then set a rule on it.** A trace hook shows what the
   agent did; your own `PreToolUse` hook decides what it may not do.

| Option | Agent | SDLC stage it serves | Closest real task |
|---|---|---|---|
| A | `ticket-triage` — six FIN tickets → Jira-shaped triage lines | Plan | grooming the queue before stand-up |
| B | `runbook-writer` — one reviewed run log → Confluence-shaped runbook | Maintain | turning a done ticket into a procedure |
| C | `repo-reviewer` — this repository → findings with file evidence | Deploy (review) | reviewing a merge request for consistency |
| Stretch | `retro-writer` — fictional Jira sprint export → retro draft | Maintain | only after A, B, or C passed the checker |

Lab: [agent menu](https://github.com/RyanLisse/aetherlink-agent-lab/blob/main/scenarios/agent-menu/README.md) ·
[first hook](https://github.com/RyanLisse/aetherlink-agent-lab/blob/main/scenarios/agent-menu/first-hook/README.md) ·
[observability](https://github.com/RyanLisse/aetherlink-agent-lab/blob/main/scenarios/agent-menu/observability.md).

## Session outcome and boundary

By 16:00 every participant has: one chosen agent installed and run twice on
their own laptop, a trace summary answering *what did it ask, read, delegate,
write*, a working `PreToolUse` hook they edited themselves, a checker result,
a completed run log, and one accepted output saved under `participant-output/`.

Fictional local inputs; agents use `Read`, `Glob`, `Grep` and preview in
chat; the only permitted agent write is the hook test under
`participant-output/`. No Jira, GitLab, Confluence, PSP or bank record; no
SDK deployment or hosting. Missing model or login is `OPEN`.

## Concept 1 — agents in the AI-native SDLC (10:15–10:35)

Sources: *The AI-native SDLC playbook* (claude.com blog and Claude Academy
course). Use the interactive SDLC slide (line vs loop, Before/After agents,
click a stage).

1. **The line versus the loop.** Traditional: Plan → Design → Build → Test →
   Deploy → Maintain; one loop back is a new release cycle. AI-native: the
   same six stages as a loop that turns in hours, with humans *above* the
   loop instigating, directing and governing.
2. **What actually speeds up.** Build runs at agent speed. Requirements
   (Plan/Design), review (Test) and release (Deploy) stay human — that is
   where the reclaimed cycle time goes.
3. **Start anywhere, adopt in order.** From the playbook's adoption map:
   capture intent, `CLAUDE.md`, skills, a feedback loop, hooks and plan mode
   have no prerequisites; subagents and evals build on them; PR review, CI/CD
   and closing the loop come last. This course walked that map: intent (Day 1),
   contract (Day 2), subagent (Day 3), hooks (today), evaluator (Day 5).
4. **Choose your agent by stage.** Point at the table above; each option is
   a bounded agent at one stage. Pick the work you want faster next week.

## Concept 2 — hooks: see the loop, then set a rule (13:00–13:20)

Source: Claude Code docs, *Automate actions with hooks* and the hooks
reference. Hooks are shell commands Claude Code runs at fixed points of the
agentic loop; they are **deterministic** — the rule runs whatever the model
decides.

1. **See.** The starter's trace hook listens on `UserPromptSubmit`,
   `PostToolUse`, `SubagentStop`, `Stop` and writes one line per event to
   `trace/<session>.jsonl`. Read one participant's trace aloud in the
   four-question order; show `/hooks`.
2. **Set a rule.** A `PreToolUse` hook on `Write|Edit` can block a write
   before it happens: exit code 2, message on stderr goes back to Claude as
   feedback. Demo the lab's `protect_output.py`: root write blocked, write
   under `participant-output/` allowed, trace shows one `Write`.
3. **What hooks cannot do.** They do not make the model understand the rule;
   they hold the boundary. `PostToolUse` cannot undo. Put the rule in
   `intent.md`/`CLAUDE.md` too, so agent and hook agree.
4. **Reference only:** Anthropic's `claude-agent-sdk-demos/hello-world`
   registers the same kind of `PreToolUse` block in TypeScript via the Agent
   SDK. Needs an API key — not part of the exercise.

## Facilitator preflight

1. Pull the lab; read `scenarios/agent-menu/README.md`, `first-hook/README.md`,
   `observability.md`; open each option README once.
2. On the trainer laptop: install the starter, run Option A's first prompt,
   confirm `trace/<session>.jsonl` and `trace_summary.py` output. Then add the
   `PreToolUse` hook per the first-hook README and run its test prompt; confirm
   block + allow. Record Claude Code version and model shown.
3. Ask who is on Windows; have the PowerShell and `python` variants from the
   first-hook README ready. Test one PowerShell command in a PowerShell window
   if a Windows laptop is available.
4. Board: the menu table, the four trace questions, the five hook events used.
5. Kahoot opener: "Which of these does a trace prove? (a) the answer is
   correct (b) which files were read (c) the model understood the ticket";
   wordcloud "Which step blocks you today?".

## Schedule — 10:00–16:00 (360 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Welcome back: Kahoot + wordcloud, Day 3 recap, today's two concepts |
| 10:15–10:35 | 20 | Concept 1: agents in the AI-native SDLC (interactive slide) |
| 10:35–10:50 | 15 | Menu choice and starter install |
| 10:50–11:15 | 25 | **Individual** Card 1: first run of the chosen agent, trace, checker |
| 11:15–11:25 | 10 | Break |
| 11:25–11:45 | 20 | Groups of 3–4, Card 2: trace versus citations |
| 11:45–12:00 | 15 | Human gate: baseline frozen |
| 12:00–13:00 | 60 | Lunch |
| 13:00–13:20 | 20 | Concept 2 + demo: hooks — see the loop, set a rule |
| 13:20–13:45 | 25 | **Individual** Card 3: build your first hook |
| 13:45–13:55 | 10 | Break |
| 13:55–14:10 | 15 | Groups of 3–4, Card 4: compare rules |
| 14:10–14:35 | 25 | **Individual** Card 5: second agent run with your hook active |
| 14:35–14:50 | 15 | Break |
| 14:50–15:25 | 35 | **Individual** Card 6: run log and handoff draft |
| 15:25–15:40 | 15 | Recap: the two concepts, one sentence each |
| 15:40–16:00 | 20 | Check-out, MOB reflection, Kahoot/wordcloud delta |

Total: **360 minutes**. Four individual blocks (25, 25, 25, 35) before or
between short group blocks.

## Literal task cards

### Card 1 — first run (individual, 10:50–11:15, 25 min)

- **Goal:** a complete preview from your chosen agent plus its trace summary and checker line.
- **Input:** your option README (contract + exact first prompt); the files it names.
- **Steps:** `cp -Rn scenarios/agent-menu/starter/.claude .claude` and start Claude Code in the checkout root; fill the `templates/run-log.md` header; type the option's first prompt unchanged; `python3 scenarios/agent-menu/tools/trace_summary.py` → four answers into the run log; save the accepted preview to `participant-output/<option>.md`; `python3 scenarios/agent-menu/tools/check_menu_output.py --agent <name> --output participant-output/<option>.md`.
- **Result:** preview, trace summary, checker line, run log with PASS/FAIL/OPEN.
- **Time limit:** 25 min.

### Card 2 — trace versus citations (groups of 3–4, 11:25–11:45, 20 min)

- **Goal:** one source cited but never read, or read but never cited.
- **Steps:** compare "Sources read" with the output's `Source:`/`[source: …]` lines; check one number by hand; agree one correction as a single added prompt sentence, or an `OPEN`.
- **Result:** one agreed correction per group on the board.

### Card 3 — your first hook (individual, 13:20–13:45, 25 min)

Follow the lab's `first-hook/README.md` card exactly: copy the script for your
OS into `.claude/hooks/`, add `PreToolUse` as a sibling event in
`.claude/settings.json`, restart Claude Code, verify with `/hooks`, run the
test prompt (root write blocked, `participant-output/` write allowed), read the
trace, then make the rule yours (folder, second pattern, or message).

- **Result:** `/hooks` shows your hook; one blocked and one allowed attempt in the run log; your edited rule.
- **Time limit:** 25 min. Not working = exact error as `OPEN`; never disable the trace hook to fix it.

### Card 4 — compare rules (groups of 3–4, 13:55–14:10, 15 min)

- **Goal:** one sentence per group: the first rule you would want on a real repository, and the event it needs (`PreToolUse` prevent, `PostToolUse` react, `Stop` summarise).

### Card 5 — second run with the hook active (individual, 14:10–14:35, 25 min)

- **Goal:** the Card 2 correction applied; the contract still passes; your hook stayed silent because the agent previewed only.
- **Steps:** same first prompt plus the agreed sentence; new trace; checker; one sentence in the run log on what the agent read differently and whether the hook fired.
- **Result:** two traces, two checker lines, hook observation.

### Card 6 — run log and handoff draft (individual, 14:50–15:25, 35 min)

- **Goal:** a run log a fresh reader can follow, the accepted output saved, the handoff started.
- **Steps:** complete every field of `templates/run-log.md` (Day 5 section empty); start `templates/handoff.md` with option, prompts, settings, checker line, trace file, hook rule, `OPEN` items; save as `lab-notes/day-4-run-log.md`.

## Recap and close — 15:25–16:00

Recap slide: "In the AI-native loop my agent sits at…" and "A hook is…", one
sentence each from the room. Then individual check-out (**Made**, **Learned**,
**Can do**), MOB reflection on the opening blocker and one correction that
worked, Kahoot and wordcloud repeated with the delta. Complete the
[daily recap](../templates/daily-recap.md), link it from `recaps/README.md`,
update `progress.md` with observed results only.

## Phase lens

`Plan`, `Design`, `Build`, bounded local `Test`, and a local `Deploy` gate
(the hook) are in scope. `Maintain` and any hosting, schedule or
business-system write are `NOT IN SCOPE`.
