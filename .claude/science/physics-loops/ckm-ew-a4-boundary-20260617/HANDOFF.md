# Handoff

Branch: `physics-loop/ckm-ew-a4-boundary-20260617`

Target: `ckm_ew_lattice_a4_bridge_retained_identity_note_2026-04-25`

What changed:

- The note now describes a bounded-support dependency-gated bridge, not retained closure.
- The runner preserves the exact `4/9` arithmetic checks and reports dependency-status gaps as `[BOUNDARY]`.
- The cache is refreshed and scanner-clean.

Checks run:

- `python3 -m py_compile scripts/frontier_ckm_ew_lattice_a4_bridge.py`
- `PYTHONPATH=scripts python3 scripts/frontier_ckm_ew_lattice_a4_bridge.py`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py --refresh scripts/frontier_ckm_ew_lattice_a4_bridge.py --timeout-sec 120`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/frontier_ckm_ew_lattice_a4_bridge.py`
- `rg -n 'FAIL=|\[FAIL\]|FAILED:' logs/runner-cache/frontier_ckm_ew_lattice_a4_bridge.txt`
- `git diff --check`

Remaining blocker:

Independent audit of the dependencies is still required before any retained closure can propagate.
