# Handoff: Flavor detR Real-Character Narrow

## What Changed

This PR repairs the conditional audit blocker for
`docs/FLAVOR_DETR_DEFAULT_FULL_EXERCISE_NOTE_2026-05-30.md`.

The audit found that the finite algebra checks are good, but the
no-holomorphic-carrier sentence relied on a CPT corner-reflection sign
`J_b -> -J_b` that is not derived in the restricted packet and is not checked
by the runner.

This branch narrows that sentence to the independently checked real-character
algebra:

- `(Z_2)^3` corner amplitudes are real `+/-1`;
- the checked finite carrier is real `R[Z3]`;
- this does not supply a native complex-line carrier or automatic `det_C`
  read;
- the CPT reflection sign remains open/non-load-bearing.

## What It Does Not Do

- It does not edit `docs/audit/**`.
- It does not apply an audit verdict.
- It does not choose the physical generation reference state.
- It does not derive a CPT corner-reflection theorem or holomorphic/Kahler
  bridge.

## Verification

```bash
python3 scripts/flavor_detR_default_full_exercise_2026_05_30.py
# UPDATED SCORECARD PASS=6 FAIL=0

python3 -m py_compile scripts/flavor_detR_default_full_exercise_2026_05_30.py

python3 scripts/cached_runner_output.py --check-only scripts/flavor_detR_default_full_exercise_2026_05_30.py
# fresh logs/runner-cache/flavor_detR_default_full_exercise_2026_05_30.txt

git diff --check
git diff -- docs/audit
```

Independent audit decides whether this narrowed finite-locator row is now
clean.
