# Handoff

Branch: `physics-loop/fifth-family-complex-sampled-gates-20260609`

Target claim:
`fifth_family_complex_boundary_note`

What changed:

- `scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py` now computes the Born proxy on all
  six sampled rows instead of only `drift = 0.20`, `seed = 0`.
- The runner now separates Born and F~M gates, prints sampled-row gate counts,
  and asserts the corrected companion set.
- `docs/FIFTH_FAMILY_COMPLEX_BOUNDARY_NOTE.md` removes the old seed-singleton
  claim and records the drift-0.20 two-seed companion pair.
- `logs/runner-cache/FIFTH_FAMILY_COMPLEX_TARGETED.txt` was refreshed from the
  repaired runner.

Verification:

```text
python3 scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py
ASSERTIONS: PASS

python3 scripts/cached_runner_output.py scripts/FIFTH_FAMILY_COMPLEX_TARGETED.py
status: ok
```

Remaining boundary:

This branch does not claim a family-wide complex companion. The sampled outer
rows remain controls, and the retained scope is the drift-0.20 sampled pair.

Next action:

Open a PR for reviewer extraction and independent re-audit. Do not edit
`docs/audit/**`.
