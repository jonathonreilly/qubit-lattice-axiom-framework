# Handoff

## What changed

This branch rewrites
`docs/KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md` so the
theorem claim is only the unreduced `3 x 3` determinant obstruction:

```text
det(alpha P_+ + beta P_perp) = alpha beta^2
weights = (1, 2)
kappa = 1
```

The reduced two-slot `SO(2)` quotient calculation remains in the note and
runner only as non-load-bearing future-route context.

## Why it unlocks audit

The current audit row is conditional because the positive reduced-carrier
route consumes an unproved physical `SO(2)` quotient/cos-channel decoupling
bridge. This branch stops making that positive route part of the theorem
scope. The row can now be reviewed as a bounded unreduced obstruction/no-go.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_koide_mru_weight_class_obstruction_theorem.py`
  passed with `classified_pass=37 fail=0`.
- `PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_mru_weight_class_obstruction_theorem.py --force --allow-non-main --push-mode none`
  refreshed the paired cache successfully.
- `PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main`
  passed.
- Full queue cache check is still blocked on the unrelated kinetic-isotropy
  corrupt cache already handled by PR #4013.

## Remaining science

A separate positive MRU quotient route still needs a framework-native theorem
that the charged-lepton scalar lane factors through the `SO(2)` orbit radius,
or equivalently decouples `cos(3 arg b)`.
