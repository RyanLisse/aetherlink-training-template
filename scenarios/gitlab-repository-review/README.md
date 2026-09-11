# GitLab repository review scenario

This fictional scenario teaches a scheduled repository reviewer for a GitLab
team. Learners inspect a local mirror, identify one actionable finding, and
prepare a review note for a human maintainer. No GitLab API, merge request,
pipeline, credential, or production repository is contacted.

## Shared contract

The reviewer receives a repository path, review scope, and stop rule. It may
read the supplied files and run explicitly named local checks. It returns
findings with path, line, severity, evidence, and a suggested next action. It
must say `OPEN` when a check was not run or evidence is missing. A human owns
severity, merge approval, and publication.

## Ticket

Read [`GL-REVIEW-001`](tickets/GL-REVIEW-001.md) and the local fixture under
`data/`. Keep the repository mirror unchanged. The same functional contract
is used in n8n and Claude Code, while their adapters and observed settings are
recorded separately.

## GitLab mapping

Draft fields for a GitLab issue or merge request are allowed only as local
notes. Use `OPEN` for the project path, issue number, reviewer, and URL until
the team supplies and approves them. Never create a remote record from this
public training repository.
