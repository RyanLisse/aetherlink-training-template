# Individual ticket-agent exercise

This is a **25-minute, local, fictional first exercise** for one learner on
their own laptop. The learner creates a small Claude Code subagent and
previews a draft. Two optional follow-up blocks then change one instruction
and transfer the same method to a second ticket. The result is a repeatable
way to see how a narrowly scoped instruction changes an output.

The scenario is payment operations and reconciliation. It contains no client
data, credentials, remote issue keys, or approved team answer. Do not connect
it to a production repository or write to a remote system.

## The four roles of the files

Read these in order. Keep each role distinct while working:

| File | Role |
| --- | --- |
| [`ticket-template.md`](ticket-template.md) | Output contract and exercise checklist; this is the intent that leads. |
| [`ticket-inputs.md`](ticket-inputs.md) | Two fictional payment tickets; choose one for the first run and one for transfer. |
| [`target-examples.md`](target-examples.md) | Two worked shapes for discussion; they are not an approved gold standard. |
| [`starter/.claude/agents/ticket-coach.md`](starter/.claude/agents/ticket-coach.md) | The agent under test, copied into the learner project. |

If the checklist, an input, and an example ever appear to disagree, stop and
write `OPEN — source conflict` in your notes. The exercise intent and
checklist lead; examples illustrate shape only. Do not silently reconcile a
contradiction.

Do not put `target-examples.md` into the agent prompt, copy it into the agent
directory, or treat it as a hidden oracle. The learner should discover the
effect of the one added instruction from the same input and settings.

## Before the 25-minute timer

Use a learner copy of this repository. From its root, run:

```sh
claude --version
mkdir -p .claude/agents
cp -n scenarios/ticket-agent/starter/.claude/agents/ticket-coach.md .claude/agents/ticket-coach.md
```

Use a clean learner copy. The `cp -n` guard avoids overwriting an existing
project agent; if it reports that the destination exists, stop and choose a
new learner copy or have a human review that existing file.

In the Claude Code session, do this preflight before discussing the ticket:

1. Type `/model` and record the selected model. Confirm the account and local
   permission/access mode in the session status view; use only the access you
   already have.
2. Set the terminal or app zoom so the four output headings are readable
   (110–125% is a useful starting point). Keep this zoom and the model/access
   settings unchanged for both runs.
3. Type `/skills` and note any previously available skills. Do not preload or
   invoke one for this exercise; the starter deliberately has no `skills`
   field. If a prior skill looks relevant, record its name and leave it unused
   so the comparison stays bounded.
4. Open [`ticket-template.md`](ticket-template.md) and choose `TICKET-OPS-101`
   for the first run. Keep `TICKET-OPS-102` for transfer.

The exercise is blocked until the learner can state the model, access mode,
zoom, selected input, and whether any prior skill was available. If account or
model access cannot be confirmed, record `OPEN — model/access not confirmed`
and continue only with a local read-only walkthrough or the supplied checker.
Do not claim that an agent was built or run when Claude Code is unavailable.
This is a preflight record, not proof that the account can access every team
tool.

## Run and preview — first 25 minutes

Start Claude Code from the learner copy root:

```sh
claude
```

Invoke the local project agent explicitly. The documented natural-language
form below is the primary invocation. If your Claude Code version exposes an
agent typeahead, type `@` and select `ticket-coach` from the agent choices. Send the same prompt for the first and second run, changing only the
one instruction in the agent file between them:

```text
Use the ticket-coach subagent. Read scenarios/ticket-agent/ticket-inputs.md and use the TICKET-OPS-101 input. Return a draft that follows scenarios/ticket-agent/ticket-template.md. Preview the complete draft in chat; do not write files or use remote tools.
```

Before any copy or write, a human previews the complete chat output. Check
that `Current situation` and `Desired situation` are present and that the
four added headings are visible. Save the first preview somewhere local only
if the human chooses to do so.

The first 25-minute block ends after the human previews the baseline draft,
checks the protected sections and four headings, and records the model,
access, input, and observed output. Do not count a supplied target example as
the learner's result.

## Change and rerun — optional 15-minute block

Add exactly this single sentence to the **body** of
`.claude/agents/ticket-coach.md` (do not change frontmatter, model, access,
zoom, input, or prompt):

```text
For every technical proposal or test assumption, cite the exact input section; if the input does not support it, label it OPEN.
```

That is the learner's source-evidence instruction. The starter omits it on
purpose. Wait a few seconds for the agent watcher to notice the edit, then
send the identical prompt again. If `ticket-coach` is missing from the
typeahead or the output still uses the old definition, exit Claude Code with
`Ctrl-D` (or close the session), run `claude` again from the learner copy
root, and repeat the same prompt. The official documentation says a restart
is required when the first `agents` directory was created after the session
started; edits to an already watched directory are normally picked up.

Preview the second draft before saving it. Compare the two previews with the
same model, access, zoom, input, and prompt. Record one concrete difference
and one thing that stayed the same. The new instruction makes source handling
more observable, but a visible output change is not guaranteed; record `OPEN
— no visible difference` if the two drafts look the same. Either result is an
observation from this run, not proof of semantic quality.

## Transfer — optional 15-minute block

Finally, run the transfer prompt with the same settings and use
`TICKET-OPS-102`:

```text
Use the ticket-coach subagent. Read scenarios/ticket-agent/ticket-inputs.md and use the TICKET-OPS-102 input. Return a draft that follows scenarios/ticket-agent/ticket-template.md. Preview the complete draft in chat; do not write files or use remote tools.
```

The transfer check is complete only when the learner can point to the two
protected sections, the four added headings, and at least one `OPEN` item in
the second preview. The human decides whether the draft is useful.

## Compact glossary

An **agent** is a named assistant definition with its own prompt, model, and
tool access. A **skill** is a reusable workflow or prompt that can be invoked
or preloaded; it is not the same configuration object as an agent. A **hook**
is an event-triggered command or guard around a lifecycle event. **Custom
intent/progress** are human-owned files that state the outcome, boundary,
owners, and evidence state; they guide work but do not become hidden agent
instructions.

## Checker: protected shape only

The standard-library checker confirms that the selected input's `Current
situation` and `Desired situation` sections are preserved and that the output
has the four required headings. It does **not** prove that a proposal is
technically correct, that Given/When/Then tests are meaningful, that an `OPEN`
question is sufficient, or that Claude Code actually ran.

From this directory, the following valid example should pass:

```sh
python3 check_ticket.py --input ticket-inputs.md --ticket TICKET-OPS-101 --output examples/valid-output.md
```

The invalid example should fail because it changes protected text and omits a
required heading:

```sh
python3 check_ticket.py --input ticket-inputs.md --ticket TICKET-OPS-101 --output examples/invalid-output.md
```

Use the checker after a human preview, not as an automatic approval gate.
The two worked target blocks can also be shape-checked independently:

```sh
python3 check_ticket.py --input ticket-inputs.md --ticket TICKET-OPS-101 --output target-examples.md
python3 check_ticket.py --input ticket-inputs.md --ticket TICKET-OPS-102 --output target-examples.md
```

## Team approval checklist — PENDING

- [ ] Training owner reviews the 25-minute task and stop rule.
- [ ] A team representative reviews the fictional template vocabulary.
- [ ] A trainer dry-runs the copy, access, and restart steps in the same
      environment learners will use.
- [ ] A human reviewer accepts the pack for the next session.

Until these boxes are checked, this pack is a draft training artifact.

Configuration reference checked for this pack: [Claude Code sub-agents
documentation](https://code.claude.com/docs/en/sub-agents.md). The starter's
`tools: Read, Glob, Grep` restriction provides read-only access for this
exercise; the human preview remains the gate before any local copy or write.
