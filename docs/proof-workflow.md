# Bounded Proof workflow

This is a 20-minute exercise that fits inside the existing intent block. It
uses a squad-owned Proof document as a review surface for a draft and uses
synthetic data only. The facilitator creates that separate draft in the hosted
Proof browser, invites the squad, and configures scoped agent access when
available; they record its owner and revision. This page is an adoption guide;
it does not claim that Proof has been set up.

The [Proof agent documentation](https://www.proofeditor.ai/agent-docs) is the
authoritative hosted reference. The existing
[Proof welcome document](https://www.proofeditor.ai/d/v07vptke) is available to
the agent as read-only context. Do not edit that welcome document.

## Evidence chain

Keep the Proof draft (a local candidate for this exercise) and the approved
repository files distinguishable:

1. Draft the proposed outcome, boundary, and evidence checks against the
   synthetic exercise in the squad-owned Proof document. Keep unresolved
   decisions as `OPEN`.
2. Check the draft against the repository's [intent.md](../intent.md),
   [progress.md](../progress.md), and [CLAUDE.md](../CLAUDE.md). The root
   `CLAUDE.md` must keep explicit `@intent.md`, `@progress.md`, and `@AGENTS.md`
   references so an agent receives the same project context.
3. After a human accepts the draft and its Proof suggestions, manually apply the approved text to
   `intent.md` and `progress.md` in the approved training GitLab repository and
   open or update its merge request. Record the commit or MR revision in the
   recap. This is a deliberate manual handoff; there is no automatic Proof →
   GitLab synchronisation.

Proof's agent API can support the squad-owned document when the facilitator
provides scoped agent access. Its hosted routes are `GET
/api/agent/<slug>/v3/document` for reading and `POST
/api/agent/<slug>/v3/edit` for editing. A write requires an access token. Keep
tokens in the approved secret manager or process environment, never in this
repository, a prompt, a Proof document, a URL committed to the site, or a
training artifact. If scoped API access is unavailable, the agent returns
suggestions to the operator for manual entry in Proof and the API step is
`OPEN`; do not guess a token or claim an API write.

## The 20-minute intent exercise

| Time | Activity | Required output and gate |
| --- | --- | --- |
| 0–5m | Individual draft | Each person drafts one observable outcome, boundary, owner, and evidence check for the chosen synthetic scenario. Unknowns remain `OPEN`. |
| 5–10m | Squad combine | The squad compares drafts and produces one concise candidate draft. Keep source paths, assumptions, and the proposed `intent.md`/`progress.md` changes visible. |
| 10–15m | Agent suggestions | The agent reviews the Proof draft and returns bounded suggestions with exact quotes, reason, risk, and `OPEN` questions. With scoped access it may add suggestions/comments through `v3/edit`; otherwise the operator records them for manual entry. The welcome document remains read-only. |
| 15–20m | Human approval / export to GitLab MR | The human reviewer accepts, revises, or rejects each suggestion. The evidence owner manually copies the approved `intent.md` and `progress.md` into the approved training GitLab branch and prepares or updates the MR. If access is missing, record the intended branch/MR and `OPEN`; do not imply publication. |

The exercise is complete only when the reviewer and evidence owner are named,
the approved content is traceable to a revision, and every unverified claim is
still marked `OPEN`.

## Example review prompt

```text
Act as a bounded review assistant for this synthetic training exercise. Read
the candidate draft plus intent.md, progress.md, CLAUDE.md, and AGENTS.md.
Check that the outcome is observable, the boundary excludes live or private
systems, owners and evidence checks are explicit, and unknowns remain OPEN.
Return suggestions only; for each suggestion include the exact quoted text,
the reason, the risk if unchanged, and an OPEN question when evidence is
missing. You may read the Proof welcome document at
https://www.proofeditor.ai/d/v07vptke as context, but treat it as read-only.
Propose comments or suggestions for human approval; if scoped API access is
unavailable, return them to the operator instead of guessing a token. Do not
edit canonical files, contact GitLab/Jira/Confluence, or claim approval,
export, or publication. Use synthetic data only.
```

## Success checks

- [ ] The squad has one candidate draft with an observable outcome, boundary,
      named owner, and evidence check.
- [ ] A squad-owned Proof draft has a recorded owner, slug, and revision; the
      supplied welcome document remains read-only.
- [ ] The agent's suggestions quote text that exists in the candidate or the
      named repository files; unsupported details are `OPEN`.
- [ ] A human has recorded accept, revise, or reject for every suggestion.
- [ ] The approved `intent.md` and `progress.md` are present in the intended
      GitLab branch/MR, or the missing access and intended destination are
      recorded as `OPEN`.
- [ ] `CLAUDE.md` explicitly references `@intent.md`, `@progress.md`, and
      `@AGENTS.md`.
- [ ] The recap identifies the human owner, reviewer, evidence owner, source
      revision, GitLab branch/MR revision, and the next recheck.
- [ ] No access token, private client data, or live-system result appears in
      the repository, site, prompt, or recap.

## Recap template

Copy this into the relevant dated recap and replace each placeholder.

```markdown
## Proof exercise recap — TEMPLATE

- Date/time: `YYYY-MM-DD HH:MM TZ`
- Scenario/data: `synthetic scenario and input path`
- Owner: `human facilitator or reviewer`
- Agent operator: `name`
- Evidence owner: `name`
- Local draft revision: `file, commit, or timestamp`
- Proof draft: `squad-owned slug, owner, and revision`
- Proof welcome reference: `read-only; unchanged`
- Agent review: `suggestions accepted/revised/rejected; evidence link`
- Approved intent.md revision: `GitLab branch/MR/commit, or OPEN`
- Approved progress.md revision: `GitLab branch/MR/commit, or OPEN`
- CLAUDE.md refs checked: `yes/no; exact path`
- Human decision: `accepted / revise / rejected`
- Open items and owner: `item — owner — due date`
- Next recheck: `date and exact command or link`

### Evidence

- Source paths: `...`
- Exact commands or readbacks: `...`
- Reviewer reproduction path: `...`
```

The owner is accountable for the decision. The revision is the value a fresh
reader uses to retrieve the draft and approved files; a Proof revision is only
meaningful when a writable, authorised document already exists. Never turn a
missing revision into a claim that the GitLab MR was published.
