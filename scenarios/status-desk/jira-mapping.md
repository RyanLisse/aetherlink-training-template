# [TRAINING] fictional Jira mapping notes

This pack is not an import file and does not create or publish Jira issues.
The destination project, issue type IDs, workflow, field names, and account
permissions are unknown. A human must select and verify those values before
any manual entry or later import is considered.

## Suggested human mapping

| Scenario field | Jira field to choose and verify | Rule |
| --- | --- | --- |
| `id` | External ID, label, or description | Preserve `SCN-001` through `SCN-007` as the stable training reference. |
| `title` | Summary | Keep the `[TRAINING]` and `fictional` labels. |
| `issue_type` | Project-specific issue type | Map `Epic`, `Story`, `Bug`, or `Task` only after reading the project's available types. |
| `day` | Label, component, or custom field | Do not assume a field exists; retain the full Day/Exercise text in the description if needed. |
| `priority` | Project-specific priority | Verify allowed values before mapping `P0`–`P3`. |
| `depends_on` | Issue links | Resolve links only after the destination keys exist; preserve order and do not invent keys. |
| `body` | Description | Copy the Markdown narrative, commands, expected result, unchecked acceptance, evidence, and human role. |
| no assignee | Assignee | Leave unassigned until a human chooses an owner. |

Before any Jira action, the human project owner should record the project key,
chosen issue types, destination custom fields, link strategy, and reviewer.
They should then compare each created issue against the local Markdown source.
This document does not provide those values and does not claim that any Jira
issue has been created, imported, or linked.
