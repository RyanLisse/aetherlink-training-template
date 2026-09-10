# Daily guides

These guides are a public-safe adaptation of the AI-Native SDLC playbook for a two-day AetherLink training lab. They are not official course material. The course pages and lesson text were publicly read for mapping; videos and audio were not watched or listened to.

## Participant setup

1. On GitHub, choose **Use this template** for RyanLisse/aetherlink-training-template and create your own repository.
2. Clone the created repository:

       git clone <url-of-your-created-repository>

3. Change into the actual cloned repository, then verify Python and create notes:

       cd <actual-cloned-repository>
       python3 --version
       mkdir -p lab-notes

4. Open the repository root as the agent context. Read intent.md, progress.md, the applicable day guide, and training-lab/README.md.
5. Keep the shared training intent at root. Day exercise artifacts belong in lab-notes/intent.md, lab-notes/spec.md, and lab-notes/plan.md.

All commands in the guides run from the repository root. Use local Git checkpoints after the named human gate; do not push as part of the exercise. A local release rehearsal is not deployment evidence.

## Guides

- [Day 1 — From intent to a tested first change](day-1.md)
- [Day 2 — Institutionalise, review, and close the loop](day-2.md)

## Shared scenario

Use [Northstar Demo Support Desk](../scenarios/status-desk/README.md) for the mock requests, role cards and ticket sequence. Follow its day-to-ticket mapping alongside these timeboxes; it adds context to the exercises rather than a third training day.

## Source map

The guides map all 14 lessons: Introduction; Capture as intent.md; Requirements and design; Plan mode; CLAUDE.md; Skills as institutional knowledge; Parallel sessions and subagents; Feedback loop; Continuous evals in CI; AI in the PR review loop; Hooks as approval gates; CI/CD integration and deployment; Closing the loop on metrics; and Closing thoughts and resources. The first four are practiced directly; later deployment, eval, and hook material is marked as applied or advanced overview where the lab does not implement it. See each guide for canonical links.
