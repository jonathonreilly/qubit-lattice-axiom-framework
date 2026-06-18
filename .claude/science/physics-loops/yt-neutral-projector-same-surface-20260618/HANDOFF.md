# Handoff

## Target

`yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`

Current audit blocker:

```text
missing_bridge_theorem: add or cite a retained same-surface carrier theorem identifying the qubit P_- source ray with the neutral EW Higgs doublet ray, then re-audit the bounded support claim.
```

## What This Branch Does

Adds `YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md`, proving that on the retained one-Higgs EW carrier:

```text
Q_H = T_3 + Y_H = diag(1,0)
P_neut = 1_0(Q_H) = I - Q_H = P_-
P_ch = Q_H = P_+
epsilon_H = 2 Q_H - I = I - 2 P_neut
exp(h epsilon_H) = exp(h) exp(-2h P_neut)
```

The existing YT carrier bridge now cites this theorem and its runner checks the same-surface charge-spectral projector markers.

## What This Branch Does Not Do

- Does not audit.
- Does not retag the ledger.
- Does not land to main.
- Does not edit audit/status surfaces.
- Does not claim retained or proposed retained status.
- Does not close full physical `Y_T`.

## Verification

Run:

```text
python3 scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py
python3 scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py
python3 -m py_compile scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py
git diff --check
```

Latest direct runner results before packaging:

- `frontier_yt_ew_neutral_projector_same_surface_carrier.py`: `PASS=69 FAIL=0`
- `frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py`: `PASS=66 FAIL=0`

## Next Action

Reviewer should inspect the source-side theorem and decide whether the repair is suitable for an independent audit re-run of the bounded support row.
