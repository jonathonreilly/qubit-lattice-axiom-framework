# Handoff

This PR repairs the science in the old `g_*` residual-retirement row.

The important change is R-FSB. The previous row used a retained hierarchy
`7/8` theorem to source the thermal `g_*` fermion weight. The repaired row
instead proves the actual Stefan-Boltzmann Fermi/Bose ratio directly in the
note and runner. R-U1Y remains rank-only and sourced to retained
`NATIVE_GAUGE_CLOSURE_NOTE.md` / `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`.

Expected review focus:

- Verify that the thermal-integral proof is sufficient for the `g_*` dof-count
  role under the stated thermal hypotheses.
- Confirm the GSTAR thermal bridge and hierarchy anchor are non-load-bearing
  context, not dependencies.
- Confirm no audit results were edited.

Verification:

```bash
python3 scripts/frontier_sm_gstar_residual_retirement_fsb_u1y_2026_05_29.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_sm_gstar_residual_retirement_fsb_u1y_2026_05_29.py
```
