# Squad 2 Day 4 · First agent in Claude Code

Mode: COACHED · 10:00–16:00

Rebuild the Day 3 review agent in Claude Code using the same functional contract. Record the read-only adapter, model, mode, access, and trace.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **One contract, two platforms** · What is "one contract, two platforms"? [3] → One contract · see the split [4] → One contract · how we use it [5]
- **Hooks** · What is a hook? [6] → Hooks · see the guardrail [7] → Hooks · how we use it [8]
- **Subagents** · What are parallel sessions and subagents? [9] → Subagents · see the streams [10] → Subagents · how we use it [11]
<!-- concepts:end -->

<!-- example:start -->
## Worked example · daily payment reconciliation

One example runs from Day 1 to Day 5; see [worked-example.md](worked-example.md). Today's step, with the site slide number in brackets:

- **The example · same contract in Claude Code** [12] · Same files, same contract, different platform. Today the check runs before the claim.
  - Expected: One Claude Code run with trace, table and hook result, plus the per-batch rerun.
  - Checkpoint: Same six classifications as n8n, or the difference is explained.
- **The example · before and after** [17] · Day 2 by hand next to Day 4 with an agent and a gate. Fill it with the squad's own numbers.
  - Expected: Both columns filled in with the squad's own numbers.
  - Checkpoint: Nobody claims speed without naming a trap the gate caught.
<!-- example:end -->

## Schedule

| Time | Minutes | Block | Result |
|---|---|---|
| 10:00–10:15 | 15 | Recap + theory | Agent loop and platform |
| 10:15–10:35 | 20 | Instruction + demo | Subagent, `CLAUDE.md`, Read/Glob/Grep |
| 10:35–11:00 | 25 | Individual | Run the starter agent |
| 11:00–11:20 | 20 | Review | Read trace and checker |
| 11:20–11:35 | 15 | Break | — |
| 11:35–12:00 | 25 | Group practice | Improve one instruction |
| 12:00–13:00 | 60 | Lunch | — |
| 13:00–13:15 | 15 | Theory | Hooks and human gate |
| 13:15–14:00 | 45 | Individual + group | Add one guardrail, rerun, fill the before-and-after slide |
| 14:00–14:15 | 15 | Break | — |
| 14:15–15:05 | 50 | Transfer | Fresh reader reproduces run |
| 15:05–15:40 | 35 | Handoff | Trace, checker, prompt, OPEN items |
| 15:40–16:00 | 20 | Close | Check-in, Kahoot, wordcloud, MOB reflection |

**Prompt.** Copy `scenarios/payment-reconciliation/starter/.claude` into your project and run the `reconciliation-reviewer` subagent on the same three CSVs under the same contract. The Stop hook runs `check_fixture.py` before the agent may finish. Record observed tool calls, the findings table, the hook output, and `OPEN` items. Then rerun with one reviewer per batch. Do not create remote records.

**Checkpoint.** A fresh reader can explain what the agent read, produced, and what remains unproven; the hook ran before any "reconciled" claim; the before-and-after slide is filled with the squad's own numbers.

