# Handoff

This PR source-covers four audited-clean `open_gate` flavor rows:

- `flavor_native_action_predicts_q1_2026-06-02`
- `flavor_record_readout_form_not_weight_2026-06-02`
- `flavor_hw_clifford_does_not_constrain_r_2026-06-02`
- `flavor_zdet_fermionic_statistics_admission_2026-06-04`

The move is not to solve the Koide value. It is to make the current source
state explicit: action scans, Record additivity, HW/Fourier symmetry, and
determinant statistics are route-local boundaries around the same
occupancy/slot-degree atom. The shared helper checks the downstream bounded
occupancy theorem, the Record non-supply clause, the exact sector/orbit weights,
and the orientation back to `r = 1` versus `r = 1/2`.

Runner results:

- `flavor_native_action_predicts_q1_2026_06_02.py`: `PASS=10 FAIL=0`
- `flavor_record_readout_form_not_weight_2026_06_02.py`: `PASS=10 FAIL=0`
- `flavor_hw_clifford_does_not_constrain_r_2026_06_02.py`: `PASS=11 FAIL=0`
- `flavor_zdet_fermionic_statistics_admission_2026_06_04.py`: `PASS=16 FAIL=0`

Verification:

```bash
python3 scripts/precompute_audit_runners.py --allow-non-main --push-mode=none --force --concurrency=4 --runners scripts/flavor_native_action_predicts_q1_2026_06_02.py,scripts/flavor_record_readout_form_not_weight_2026_06_02.py,scripts/flavor_hw_clifford_does_not_constrain_r_2026_06_02.py,scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py
python3 scripts/precompute_audit_runners.py --allow-non-main --check-only --push-mode=none --runners scripts/flavor_native_action_predicts_q1_2026_06_02.py,scripts/flavor_record_readout_form_not_weight_2026_06_02.py,scripts/flavor_hw_clifford_does_not_constrain_r_2026_06_02.py,scripts/flavor_zdet_fermionic_statistics_admission_2026_06_04.py
git diff --check
git diff --name-only -- docs/audit docs/repo/FRONT_DOOR_STATUS.md
```

No audit ledger, active queue, front-door status, or publication matrix is
edited.
