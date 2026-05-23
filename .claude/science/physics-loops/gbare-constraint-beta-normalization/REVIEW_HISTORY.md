# Review History

- 2026-05-23: Selected after latest audit batch because
  `g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` is now retained
  and the remaining blocker was a precise missing Wilson-matching edge.
- 2026-05-23: Source repair narrows `beta = 6` to explicit local Wilson input
  and wires the retained Wilson-matching note as a one-hop dependency.
- 2026-05-23: Initial attempt to edit the shared `frontier_g_bare_derivation.py`
  runner was rejected locally because it would change the retained
  rescaling row's runner hash. The repair now uses a constraint-specific
  runner and leaves the shared retained runner untouched.
- 2026-05-23: Verification passed:
  `python3 scripts/frontier_g_bare_constraint_surface_check.py`,
  `bash docs/audit/scripts/run_pipeline.sh`, `python3 docs/audit/scripts/audit_lint.py --strict`,
  `git diff --check`, and changed-artifact vocabulary lint.

Baseline note: full `docs/` vocabulary lint still reports pre-existing
violations outside this block; the changed note, runner, and loop pack are
clean.
