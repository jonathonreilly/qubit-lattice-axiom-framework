# Alpha-Bare Green-Native Dependency Handoff

## Target

`alpha_bare_four_pi_from_z3_plancherel_bridge_bounded_note_2026-05-26`

## Repair Summary

The alpha-bare composition bridge no longer describes the `1/(4 pi r)`
Green coefficient as supplied by a Maradudin accepted-premise bridge. It now
consumes the framework-local `Z^3` graph-Laplacian Green theorem and its
normalization certificate.

This does not derive or change the I1 static-source readout, I2 alpha
convention, or I3 no-rescaling dependencies.

## Verification

```text
PYTHONPATH=scripts python3 scripts/alpha_bare_four_pi_from_z3_plancherel_bridge_2026_05_26.py
python3 scripts/cached_runner_output.py --check-only scripts/alpha_bare_four_pi_from_z3_plancherel_bridge_2026_05_26.py
python3 -m py_compile scripts/alpha_bare_four_pi_from_z3_plancherel_bridge_2026_05_26.py
git diff --check
git diff --name-only -- docs/audit
```

Latest runner result: `TOTAL: PASS=40 FAIL=0`.
