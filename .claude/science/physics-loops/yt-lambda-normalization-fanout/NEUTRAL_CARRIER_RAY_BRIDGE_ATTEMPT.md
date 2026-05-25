# Neutral Carrier-Ray Bridge Attempt

## Result

Status: `exact-support`.

The signed-record source carrier is now bridged to the neutral one-Higgs ray:

```text
epsilon = sigma_z = I - 2 P_-
exp(h epsilon) = exp(h) exp(-2h P_-)
P_- H_0 = H_0
Q H_0 = 0
```

So the source used in the Y_T support packet is affinely equivalent to the
occupation source for the lower component of the retained EW Higgs doublet.
The unknown affine scale is already harmless for the same-source top/W ratio.

## What It Retires

- The carrier-ray part of "why this source could be the neutral Higgs radial
  source" is no longer the main blocker.
- The source-coordinate normalization/slope remains non-load-bearing for the
  top/W response ratio.

## What It Does Not Retire

- Full same-surface EW transfer response.
- Strict same-source top/W response rows.
- Retained one-Higgs/top carrier authority.
- Retained hypercharge authority.
- Physical-scale `g_2(v)` authority.

## Artifacts

- `docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`
- `scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py`
- `outputs/yt_qubit_neutral_higgs_carrier_ray_bridge_2026-05-25.json`

## Verification

```text
python3 scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py
python3 scripts/frontier_yt_source_coordinate_invariant_top_w_ratio_gate.py
python3 scripts/frontier_yt_ew_higgs_source_intertwiner_gate.py
python3 scripts/frontier_yt_same_source_ew_higgs_authority_gate.py
```

All four gates pass after the status narrowing.
