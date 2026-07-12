# PR Backlog

Review-loop disposition is pass, but review-loop policy forbids this review run
from creating or opening a pull request. The reviewed science branch is:

`claude/science-fix/poisson_self_field_supplied_branch_core_bounded_note_2026-06-1c41e761`

The branch is pushed. An authorized non-review integration step can open the
review PR with:

```bash
gh pr create --base main --head claude/science-fix/poisson_self_field_supplied_branch_core_bounded_note_2026-06-1c41e761 --title "[physics-loop] poisson-supplied-branch-packet — bounded-support" --body "Closes the named restricted-packet helper omission without changing the supplied-input physics boundary. See .claude/science/physics-loops/poisson-supplied-branch-packet-20260712/HANDOFF.md, TRACE_GATE.md, CLAIM_STATUS_CERTIFICATE.md, and REVIEW_HISTORY.md. Primary/helper caches are fresh; validation pipeline and strict lint pass; independent audit remains required and owns the verdict."
```
