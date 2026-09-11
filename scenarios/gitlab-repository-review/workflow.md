# Local GitLab review workflow

1. Read the supplied repository snapshot and review scope.
2. Run only named local checks and capture their exact output.
3. Record each finding with path, line, severity as a human field, and next action.
4. Mark GitLab, CI, network, or dependency checks `OPEN` when they were not run.
5. Prepare local draft fields for a GitLab issue or merge request. A human
   reviewer decides whether anything is published.

The workflow is a training simulation. It does not call GitLab or change a
repository.
