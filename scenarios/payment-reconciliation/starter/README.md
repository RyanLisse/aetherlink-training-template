# Claude Code starter (Day 4)

Copy this folder's `.claude` directory into a learner copy of the repository
root, then run Claude Code from that root:

```sh
cp -R scenarios/payment-reconciliation/starter/.claude .claude
claude
```

Ask: `Use the reconciliation-reviewer subagent to reconcile the fictional
batches.` The subagent reads `contract.md` and the three CSVs, returns the
findings table, and quotes the fixture check.

`settings.json` registers a **Stop hook**: every time the agent wants to
finish, `check_fixture.py` runs. A non-zero exit (`FAIL …`) blocks the stop
and the failure line is fed back to the agent. That is the Day 4 guardrail:
no "reconciled" claim before the check passes.

For the subagents exercise, ask for one reviewer per batch and merge the six
rows yourself. For the guardrail exercise, add the line "Never approve a
batch that contains a duplicate settlement row" to the agent file, rerun, and
keep both outputs.

Status: `OPEN — not yet run against a live Claude Code session`. Record model,
mode and tool calls on the evidence card after the first real run.
