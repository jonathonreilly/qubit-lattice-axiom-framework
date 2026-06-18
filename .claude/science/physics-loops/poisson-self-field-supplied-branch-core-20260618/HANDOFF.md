# Handoff

This PR repairs `poisson_self_field_note` by splitting out the finite
supplied-branch core and correcting the stale Born value in the parent note.

The reviewer should check that the new note remains bounded to supplied inputs,
that the runner genuinely recomputes the branch metrics, and that no audit or
publication status files were touched.

Expected verification:

```bash
python3 scripts/poisson_self_field_supplied_branch_core_2026_06_18.py
python3 scripts/cached_runner_output.py --refresh scripts/poisson_self_field.py
python3 scripts/cached_runner_output.py --refresh scripts/poisson_self_field_supplied_branch_core_2026_06_18.py
git diff --check
```
