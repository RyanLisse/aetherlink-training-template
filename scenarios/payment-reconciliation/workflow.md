# Team workflow — GitLab, Jira, and Confluence

The public GitHub repository distributes this fictional template. A cohort
that already works in GitLab, Jira, and Confluence uses an **approved TRAINING
GitLab repository**, an approved Jira project, and an approved Confluence space
for its training record; GitHub is not a required workflow. Project keys, URLs,
custom fields, and account names are deliberately unknown and must be filled
by the team. This scenario performs no remote operations.

Before the exercise, the facilitator records the approved training repository,
Jira project, Confluence space, and access owner. Never import these files into
a default production repository or space. If the approved spaces are not
available, use the local/offline fallback below.

## GitLab repository and merge request

1. Start from the approved TRAINING GitLab repository and its default branch.
   Import or copy this scenario as a reviewed starting commit, then create a
   branch such as `training/fin-003-duplicate-unresolved`.
2. Put the cohort evidence log and reviewed notes on that branch. Preserve the
   source CSVs and record the exact commit SHA in the handoff.
3. Open an MR titled `[FIN-003] Quarantine duplicate settlement — UNRESOLVED`.
   Link the team Jira task and Confluence evidence page after a human supplies
   their real URLs.
4. Use two independent reviewers: one checks identifiers/arithmetic and one
   checks scope, cutoff, duplicate treatment, and evidence. Neither reads the
   other's finding before submitting it.
5. MR evidence is actual validation output, cited CSV rows, and both findings.
   A green pipeline or MR approval does not replace source-row readback.
6. A reviewed evidence MR may merge while the financial case remains OPEN and
   `UNRESOLVED`; merging documentation is not approval of the payout. Real
   crosslinks improve the team record but do not block local training
   acceptance. If GitLab is unavailable, record branch, intended MR title,
   commit/working-tree revision, and missing evidence locally.

## Jira epic and task statuses

Copy the six local templates into the team's chosen Jira project only after a
human identifies its project key and issue-type fields. Keep the fictional IDs
as labels or external references if Jira requires a different key.

| Local | Jira role | Suggested status progression | Crosslinks |
| --- | --- | --- | --- |
| `FIN-001` | epic | Backlog → In progress → Done | GitLab overview MR; Confluence index |
| `FIN-002`–`FIN-006` | child tasks | Backlog → In progress → Blocked/Done | parent epic; GitLab MR; Confluence page |

`FIN-001`–`FIN-006` are local scenario IDs, not assumed Jira keys. For
`FIN-003`, create the corresponding task in the approved project, retain
`FIN-003` as a label/external reference, and capture the Jira-assigned key.
Use `Backlog`, `In Progress`, `Blocked`, and `Done` according to the team's
workflow: `In Progress` while reviewing and `Blocked` when source confirmation
is needed. For this fictional exercise, the financial case stays open while the duplicate
batch is `UNRESOLVED`. Map that state to the team's actual Jira workflow;
this exercise does not define a Worldline completion policy. If Jira
is unavailable, keep status and next owner in the local template and label the
future link `OPEN`.

## Confluence page outlines

Create pages in the team's agreed space; do not invent a space key or URL.
Each page links the exact GitLab commit/MR and Jira issue once they exist, plus
local source paths while working offline.

| Page | Minimum outline | Evidence links |
| --- | --- | --- |
| Intent | problem, outcome, roles, cutoff/timezone, constraints, open questions | GitLab branch/MR; Jira `FIN-001` |
| Spec | schemas, keys, fee rule, batch formula, duplicate/due-date policy, case IDs | CSV paths; validator output; Jira tasks |
| Runbook | load, validate, reconcile, quarantine, classify, hand over | exact command; GitLab SHA; `FIN-002`–`FIN-006` |
| Recap | observed checks, reviewer decisions, open actions, next gate | MR output; Jira statuses |
| Knowledge | validated facts, hypotheses, review date, reuse owner | reviewed MR; Runbook |
| Handoff | receiver, cutoff, source IDs, command, risks, rollback, OPEN items | commit/MR; Jira; all pages |

When Confluence is unavailable, keep these headings in the local dated
recap/handoff and write `Confluence page: OPEN`; do not claim publication.

## Copyable coordination prompt (drafts only)

```text
Read scenarios/payment-reconciliation/README.md, the three CSVs, and my evidence log. Prepare three local drafts without publishing or calling any remote service: (1) a GitLab MR title/body with branch name, commit placeholder, validation command/output, source-row IDs, and two independent reviewer slots; (2) Jira field values for local scenario ID FIN-003, including summary, suggested status, evidence IDs, dependency text, and a placeholder for the Jira-assigned key; and (3) a Confluence Recap page with cutoff/timezone, provisional unique net 24,010, raw net 43,610, bank credit 24,010, UNRESOLVED state, open confirmation action, and GitLab/Jira links marked OPEN. Do not invent project keys, URLs, policies, approvals, or recovery outcomes.
```

## Literal FIN-003 example — duplicate remains UNRESOLVED

1. From this scenario directory, run the README validation command and save
   actual output. Read PSP rows `SET-1003-A`/`SET-1003-B`, ledger row
   `TX-NS-1003`, and bank row `BANK-0909-01`.
2. Record ledger expected `19,600 + 4,410 = 24,010`; PSP raw
   `19,600 + 19,600 + 4,410 = 43,610`; provisional unique `24,010`; bank
   `24,010`. Keep both rows visible and mark batch `B-20260909-01`
   `UNRESOLVED`. Do not delete, count twice, approve, or claim recovery.
3. Create/update the Jira task in the approved project with label/external
   reference `FIN-003`, summary `Quarantine duplicate settlement`, status
   `In progress` (or `Blocked` if confirmation is requested), and the evidence
   IDs. Capture the Jira-assigned key. Add real GitLab MR and Confluence links
   when available; keep them `OPEN` until supplied.
4. Create branch `training/fin-003-duplicate-unresolved`, commit the evidence
   note, and open MR `[FIN-003] Quarantine duplicate settlement — UNRESOLVED`.
   Ask two fresh reviewers for separate arithmetic and scope findings. Attach
   command output and cite CSV row IDs.
5. Create the Confluence Spec or Recap page outline above with evidence table,
   cutoff, provisional/UNRESOLVED state, Jira reference, and MR reference. A
   human decides whether the source confirms one row.
6. Until that decision is evidenced, keep the Jira task open/blocked. The
   evidence MR may merge after independent review, but this does not approve
   the financial case. If a team system is unavailable, preserve all six steps
   in local `lab-notes` with `OPEN` links for later backfill.
