# PR Backlog

No pull request was opened from this isolated science-fix worktree. Integration
is owned by the autonomous science-fix/review path after local review; the
cycle is not presented as a new physics derivation. This managed worktree also
cannot create a Git index lock under the external `.git/worktrees` directory,
so it cannot create the integration commit itself.

Once the integration worker has a writable Git index, the recovery sequence is:

```bash
git add docs/LH_TRACELESS_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-10.md
git add scripts/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.py
git add logs/runner-cache/audit_companion_lh_traceless_eigenvalue_ratio_exact_2026_05_10.txt
git add .claude/science/physics-loops/lh-traceless-eigenvalue-ratio-stdout-repair-20260729/
git commit -m "science-fix: bind LH traceless ratio runner evidence"
```
