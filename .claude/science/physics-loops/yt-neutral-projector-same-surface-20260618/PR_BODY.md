# Summary

This PR is a source-side science repair for the audited-conditional `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25` row. It does not audit, retag, or edit any audit/status surface.

The current blocker asks for a same-surface carrier theorem identifying the qubit `P_-` source ray with the neutral EW Higgs doublet ray. This branch adds that theorem by using the retained EW charge operator:

```text
Q_H = T_3 + Y_H = diag(1,0)
P_neut = 1_0(Q_H) = I - Q_H = P_-
```

It then wires the theorem into the existing YT neutral-Higgs carrier bridge runner.

# Claim Status

- Actual current branch status: `exact-support`
- Trace class: `direct_blocker_closure`
- Reachability: closes the source-side same-surface carrier blocker only
- Independent audit required before any effective-status movement: yes
- Bare retained/proposed retained claim: no

# Artifacts

- New theorem note: `docs/YT_EW_NEUTRAL_PROJECTOR_SAME_SURFACE_CARRIER_THEOREM_NOTE_2026-06-18.md`
- New runner/output/cache: `scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py`, `outputs/yt_ew_neutral_projector_same_surface_carrier_2026-06-18.json`, `logs/runner-cache/frontier_yt_ew_neutral_projector_same_surface_carrier.txt`
- Updated target bridge note/runner/output/cache: `docs/YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md`, `scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py`, `outputs/yt_qubit_neutral_higgs_carrier_ray_bridge_2026-05-25.json`, `logs/runner-cache/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.txt`
- Loop pack: `.claude/science/physics-loops/yt-neutral-projector-same-surface-20260618/`

# Verification

```text
python3 scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py
python3 scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py
python3 -m py_compile scripts/frontier_yt_ew_neutral_projector_same_surface_carrier.py scripts/frontier_yt_qubit_neutral_higgs_carrier_ray_bridge.py
git diff --check
```

# Boundaries

This PR does not close full physical `Y_T`, derive the top coefficient, derive scalar LSZ/source-Higgs normalization, provide physical-scale `g_2(v)`, prove retained top carrier/hypercharge authority, or use observed masses/fitted selectors.

No files under `docs/audit/**`, publication effective-status surfaces, front-door status, lane registry, active review queue, or lane status board are changed.
