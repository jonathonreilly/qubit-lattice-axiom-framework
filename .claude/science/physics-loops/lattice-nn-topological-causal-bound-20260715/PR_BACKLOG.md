# PR Backlog

No PR was opened. The invoked review-loop prohibits PR creation while audit
compatibility is blocked, and changing an already-retained source note requires
independent re-audit of its note and runner hashes. After that audit ratifies
the changed hashes, the recovery commands are:

```bash
git push -u origin claude/science-fix/lattice_nn_light_cone_note-3992628f
gh pr create --base main --head claude/science-fix/lattice_nn_light_cone_note-3992628f
```
