# Handoff

This branch adds a bounded support bridge for the DM Schur ADM-3 blocker.

## Claim Movement

The graph-shift selector curvature `m_perp=32` now has an explicit Dirac-side
selected-axis commutator curvature carrier:

```text
8 * tau_D([Gamma_1,M]^dag [Gamma_1,M])
```

has Hessian `diag(0,64,64)` at `e1`.

## Boundaries

- The pure even-trace no-go remains valid.
- The selected weak axis is load-bearing.
- The graph trace factor `8` is load-bearing.
- Full graph potential equality is not claimed.
- ADM-1 readout, ADM-2 coupling, and full physical Schur retention remain open.

## Verification

Run:

```bash
python3 scripts/frontier_dm_neutrino_vsel_selected_axis_commutator_transport_2026_06_16.py
python3 -m py_compile scripts/frontier_dm_neutrino_vsel_selected_axis_commutator_transport_2026_06_16.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_dm_neutrino_vsel_selected_axis_commutator_transport_2026_06_16.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_dm_neutrino_vsel_selected_axis_commutator_transport_2026_06_16.py
git diff --check
```

## Next Action

Reviewer should decide whether this support bridge is enough to make the ADM-3
curvature packet re-auditable as bounded support, while keeping ADM-1/ADM-2 and
physical functional interpretation open.
