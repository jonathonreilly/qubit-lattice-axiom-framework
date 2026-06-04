# Handoff

## What Changed

- Added runner helpers for oriented plaquettes, principal `(0,1)` flux quanta,
  non-`(0,1)` plaquette flatness, and Polyakov-loop closure.
- Extended V6 from three checks to seven checks for each tested size.
- Refreshed the runner cache from `PASS=50 FAIL=0` to `PASS=58 FAIL=0`.
- Updated the source note to say the local plaquette phases are not constant
  and to state the actual finite invariant.

## Why It Matters

The prior packet described the special U(1) background as flux/winding-like
without directly proving the invariant in the runner. The repaired runner now
checks:

```text
sum_{x0,x1} Arg P_01(x0,x1,x2,x3) / (2*pi) = 1
```

for every fixed `(x2,x3)`, flatness of all non-`(0,1)` plaquettes, and
periodic Polyakov-loop closure.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py`
- `python3 -m py_compile scripts/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py`
- `git diff --check`

## Remaining Blockers

- No nonzero staggered index is exhibited.
- No ABJ/Fujikawa/Wess-Zumino import is retired.
- No downstream anomaly-forces-time claim is promoted.

## Next Action

Open the review PR, then continue the science-fix campaign on the next
conditional runner-artifact target.
