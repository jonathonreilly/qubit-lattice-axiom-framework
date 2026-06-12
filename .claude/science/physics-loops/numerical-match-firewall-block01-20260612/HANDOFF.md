# Numerical-Match Firewall Block 01

Branch: `physics-loop/numerical-match-firewall-block01-20260612`
Base: `origin/main` at `31b5d454`

## Purpose

Source-side repair for five uncovered `audited_numerical_match` rows:

- `quark_cp_carrier_completion_note_2026-04-18`
- `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`
- `ckm_down_type_scale_convention_support_note_2026-04-22`
- `quark_e_channel_endpoint_quotient_law_note_2026-04-19`
- `quark_endpoint_ratio_chain_law_note_2026-04-19`

## Changes

- Added current-surface certificates to all five source notes.
- Repaired CKM down-type wording from "Retained inputs" to "Inputs and comparators declared on main" so PDG/FLAG/QCD inputs are not framed as retained framework authorities.
- Left the useful numerical science intact: tuned quark CP completion, DM transport interval witness, CKM threshold-local support, and the quark endpoint rational-match candidates.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_cp_carrier_completion.py
# TOTAL: PASS=11, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
# PASS=12 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_ckm_down_type_scale_convention_support.py
# PASSED: 17/17

PYTHONPATH=scripts python3 scripts/frontier_quark_e_channel_endpoint_quotient_law.py
# PASS=22 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_endpoint_ratio_chain_law.py
# PASS=21 FAIL=0
```

Remaining blockers:

- derive `xi_u`, `xi_d`, the determinant-neutral carrier slot, and quark comparator readouts;
- derive the off-seed DM source selector independently of `ETA_OBS`;
- derive the CKM `5/6` bridge and threshold-local comparator;
- derive endpoint_readout(), the E-center endpoint primitive, and the endpoint ratio chain from retained tensor machinery.
