# Example prompts by workflow

These prompts are reusable starting points. Replace every bracketed field, ask for evidence, and mark unanswered parts `OPEN`. They contain no results.

## Plan

> State the observable outcome for `[session]`, what is in and out of scope, the roles, the stop rule, and the exact check that will prove completion. Put the result in a session plan.

## Design

> Propose the smallest design for `[outcome]`. List assumptions, alternatives, risks, and the evidence needed to choose. Do not claim a decision until the reviewer accepts the ADR.

## Build

> Implement only `[bounded change]` in `[exact workspace or revision]`. Show the diff or artifact path and call out assumptions. Stop when the scope or ownership becomes unclear.

## Test

> Run `[exact command or procedure]` with at most the stated resource limit. Report the exact result. If it fails, name the assertion and mechanism before suggesting a fix or retry.

## Deploy

> For `[target environment]`, state the revision, precondition, rollback, and deployment check. Execute only within the approved boundary and link the resulting evidence.

## Maintain

> State what must be monitored for `[artifact or service]`, who owns it, the review date, and the escalation trigger. If ownership changes, create a handoff with fresh verification steps.

## Demo and reflection

> Demonstrate `[scenario]` from `[starting state]`. Record what was observed, the evidence link, known limitations, and one keep/change/try reflection. Do not infer behavior that was not observed.

## Recap and knowledge extraction

> Complete the daily recap from observed evidence. Separate validated facts from hypotheses, then, if learning was validated, draft one reusable knowledge note with a reuse owner and review date. Link the note back to the recap; otherwise record `NONE`.

## Teach-back and review

> Run a five-minute teach-back for `[named audience]` in `[channel or document link]`. Have another participant try the procedure from the note. Ask `[reviewer]` to promote it to `REVIEWED` only when the attempt and evidence support it, or record why it remains `DRAFT`.

## Handoff

> Prepare a handoff for `[receiver]`: state the current revision and status, list open work and owners, then give fresh verification commands and expected signals. Tell the receiver what context they cannot see and where to record the result.
