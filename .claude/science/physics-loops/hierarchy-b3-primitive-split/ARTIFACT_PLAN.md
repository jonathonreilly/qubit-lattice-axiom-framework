# Artifact Plan

- Patch `docs/HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md` with the B3a/B3b split.
- Patch `scripts/frontier_hierarchy_formula_honest_status.py` so the runner checks:
  - the `kinetic_isotropy_primitive` registration;
  - the primitive's exact `c_t = c_s` / hypercubic-form scope;
  - the note's B3a/B3b split;
  - B4 remaining open.
- Refresh `logs/runner-cache/frontier_hierarchy_formula_honest_status.txt`.
- Run syntax, runner, cache, diff, and protected-output guards.
