# GL-REVIEW-001 · Scheduled repository review

As a GitLab maintainer, I want a scheduled review note that identifies one
actionable issue in a local repository mirror, cites the exact evidence, and
states the next human action. The reviewer must not change files or merge code.

Acceptance checks:

- The note names the repository scope and review timestamp.
- Every finding cites a local path and line or command output.
- At least one positive check and one negative or missing-evidence check are
  recorded.
- Severity and merge decision remain human fields.
- Unrun GitLab, CI, or network checks are marked `OPEN`.
