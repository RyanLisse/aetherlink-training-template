# Guided ticket exercise — FIN-003 duplicate quarantine

This fictional local exercise moves one narrow financial operations ticket from
analyst to developer to tester while keeping its functional requirement stable.
It does not create a Jira issue, change a remote system, or prove runtime setup.

## Assignment card

| Field | Assignment |
|---|---|
| Goal | Keep the duplicate settlement visible and safe to review while the case remains UNRESOLVED pending human source confirmation. |
| Inputs | [FIN-003 ticket](tickets/FIN-003.md); [data/](data/) with internal-ledger.csv, psp-settlements.csv, and bank-credits.csv; cutoff 2026-09-10 12:00 Europe/Amsterdam. |
| Literal steps | Read FIN-003; locate TX-NS-1003, SET-1003-A/B, BANK-0909-01; write behavior; pass the same statement to the developer; add behavior tests; record source IDs, commands, decision, and open questions. |
| Output | lab-notes/day-2/FIN-003-ticket-packet.md containing analyst, developer, technical-addition, tester, and handoff sections. |
| Timebox | Guided first 90 minutes; analyst 40; developer 40; tester 40; review/handoff 60, with lunch fixed at 12:00–13:00 in [Day 2](../../days/day-2.md). |
| Exclusions | No Jira/GitLab/Confluence writes, credentials, network, production data, deployment, recovery claim, payout approval, or all-five-case reconciliation. Never delete either duplicate row or count it twice. |

Run this preflight from the repository root before the role pass:

```sh
python3 -c "from pathlib import Path; p=Path('scenarios/payment-reconciliation/data'); assert all((p/n).is_file() for n in ('internal-ledger.csv','psp-settlements.csv','bank-credits.csv')); print('local fixture inputs present')"
```

If it cannot run, use a manual CSV worksheet with the source IDs, amounts, and
status, and mark the packet OPEN — preflight not run. This fallback is a
drafting aid, not runtime validation.

## Source slice and requirement

Read the rows yourself and record them in the packet: ledger TX-NS-1003
(expected net 19,600, batch B-20260909-01); PSP SET-1003-A and SET-1003-B
(same transaction/reference, each net 19,600); and bank BANK-0909-01
(24,010). Preserve ledger batch expected 19,600 + 4,410 = 24,010, raw PSP
43,610, and provisional unique net 24,010.

Starting functional requirement:

> When two PSP settlement rows share a transaction and PSP reference in a
> batch, keep both source rows visible, quarantine the ambiguity, count one
> candidate per transaction for the provisional comparison, show the raw total
> separately, and keep the case UNRESOLVED until a human confirms the source.
> Do not approve a payout from this result.

The analyst, developer, and tester carry this contract unchanged in substance.
An altered status, visible-row rule, count, or human gate is an open policy
question, not an implementation detail. A bank match never makes the provisional
comparison payable.

## Worked example

The trainer shows this shape before the group writes; it is not learner evidence.

**Analyst.** “For B-20260909-01, retain SET-1003-A and SET-1003-B; identify
TX-NS-1003 and PSP-NS-1003; show raw 43,610 and provisional unique 24,010;
label UNRESOLVED pending human confirmation. Bank 24,010 is evidence, not
approval.”

**Developer.** “Group locally by transaction, PSP reference, and batch. Emit a
duplicate quarantine record with both settlement IDs, raw net, provisional
unique net, and status. Preserve the analyst behavior.”

Those keys and fields are technical additions, labelled as proposals after the
functional requirement. They do not narrow or replace the requirement.

**Tester.** The positive check expects both IDs visible, raw 43,610, provisional
unique 24,010, and UNRESOLVED. Negative checks fail hidden/deleted rows,
double-counting, or payout approval.

| Type | Given | When | Then | Result |
|---|---|---|---|---|
| Positive | Both duplicate PSP rows and matching ledger/bank rows | Apply the requirement | Both IDs visible; raw 43,610; provisional unique 24,010; UNRESOLVED | OPEN until learner runs it |
| Positive boundary | One non-duplicate settlement | Apply the requirement | Included once; no duplicate quarantine | OPEN until learner runs it |
| Negative | Both duplicate rows | A proposal deletes or hides SET-1003-B | Test fails because source evidence is invisible | Learner records FAIL if observed |
| Negative | Both duplicate rows | A proposal counts both as payable | Test fails; raw 43,610 must remain separate, provisional unique 24,010 is for comparison, and neither authorizes payout | Learner records FAIL if observed |

## Literal role prompts

### Analyst

```text
Act as the analyst for fictional local ticket FIN-003. Read the ticket and
only the relevant rows in the three CSV files. Identify the two settlement IDs,
transaction, PSP reference, bank row, batch, and cutoff. Write one
user-visible functional requirement, source-backed acceptance checks, both net
calculations, and open policy questions. Keep both PSP rows visible, preserve
UNRESOLVED, do not approve a payout, inspect other FIN tickets, or classify all
five cases. Return a local draft for the shared packet.
```

### Developer

```text
Act as the developer receiving the analyst's FIN-003 draft. Read the original
ticket, analyst requirement, and cited rows. Preserve both visible rows,
provisional unique 24010, raw 43610, UNRESOLVED, and human confirmation.
Write the smallest local implementation sketch. Put every field name, key,
ordering, logging, or storage/API idea under "Technical addition — proposal".
Do not turn a preference into behavior, call services, edit CSVs, create remote
tickets, or claim runtime tested.
```

### Tester

```text
Act as tester for the same FIN-003 ticket. Read the ticket, analyst requirement,
developer proposal, and cited rows. Write one positive and at least two
negative behavior tests using Given/When/Then. Expect both IDs visible, raw
43610, provisional unique 24010, and UNRESOLVED. Fail silent deletion, hidden
rows, double count, or payout approval. Keep facts, behavior, and technical
additions separate. Record only checks actually run or mark OPEN. Do not create
remote records or claim runtime, deployment, recovery, or production testing.
```

## Relay, individual variant, and review

The analyst hands the same packet to the developer, who appends rather than
rewrites it; the tester checks both earlier sections. Use groups of three or
four people. Rotate analyst, developer, tester, reviewer/scribe, driver, and
navigator at each pass; rotate driver/navigator every 5–7 minutes. With three
people, the facilitator/timekeeper also holds review notes.

Only the navigator gives the driver the next instruction. Other participants
share observations with the navigator; the driver repeats the instruction
before acting. Anyone can call a pause.

For the individual check, give each learner a variant name and expected result,
not a complete oracle answer:

| Variant | Input | Known expected correction |
|---|---|---|
| A | Both duplicate rows | Both visible; duplicate detected; UNRESOLVED |
| B | One non-duplicate row | Count once; no duplicate quarantine |
| C | Duplicate rows plus matching bank | Bank match is evidence; status stays UNRESOLVED |
| D | Draft says RESOLVED because bank matches | Correct to UNRESOLVED; request human confirmation |

The reviewer checks that technical additions are separate and every expected
value traces to a row. Accept only when each test is PASS, FAIL, or OPEN with
reason and command or worksheet evidence.

## Five-minute parking rule and close

The facilitator may clarify source, wording, or role boundaries for five
minutes. Park longer questions, new policy, and scope expansion under Open
questions / parked; return during review and never guess. Keep private learner
feedback out of the repository.

Close with one sentence per person: **Made** (packet change), **Learned**
(assumption caught), and **Can do** (next step reproducible independently).
Use OPEN for unknown links, decisions, and unrun checks. The packet remains a
local draft and FIN-003 remains UNRESOLVED until human source confirmation.
