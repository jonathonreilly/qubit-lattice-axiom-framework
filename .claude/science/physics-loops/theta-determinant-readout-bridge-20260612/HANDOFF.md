# Handoff

## Summary

This block adds a narrow source-side determinant-readout bridge for the
`theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10`
audit row.

The bridge proves that, once the mass-side strong-CP readout is supplied as a
determinant-channel record readout with independent-block determinant
multiplication and K/CPT orbit registration, the only continuous
block-multiplicative determinant phase character surviving K/CPT is `k = 0`.
It also records the hostile guard: K-even nonmultiplicative phase probes such
as `cos(arg det M)` do not satisfy the determinant-channel block law.

## Main Artifacts

- `docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`
- `scripts/frontier_strong_cp_determinant_readout_bridge_2026_06_12.py`
- `logs/runner-cache/frontier_strong_cp_determinant_readout_bridge_2026_06_12.txt`
- `docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
- `scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py`
- `logs/runner-cache/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.txt`
- `.claude/science/physics-loops/theta-determinant-readout-bridge-20260612/TRACE_GATE.md`
- `.claude/science/physics-loops/theta-determinant-readout-bridge-20260612/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_strong_cp_determinant_readout_bridge_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_strong_cp_determinant_readout_bridge_2026_06_12.py,scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py --force --concurrency 1 --push-mode none --allow-non-main
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_strong_cp_determinant_readout_bridge_2026_06_12.py,scripts/frontier_theta_p2_k_cpt_determinant_character_phase_erasure_2026_06_10.py --check-only --push-mode none --allow-non-main
git diff --check
git diff -- docs/audit/data
```

Expected key results:

- Strong-CP determinant-readout bridge runner: `TOTAL: PASS=19 FAIL=0`.
- Theta P2/K-CPT parent runner: `SUMMARY: PASS=14 FAIL=0`.
- Runner-cache check-only reports both caches fresh.
- No `docs/audit/data` changes.

## Remaining Boundaries

- The bridge is mass-determinant-channel only.
- It does not set `theta_gauge = 0`.
- It does not derive the real-positive Wilson action surface.
- It does not eliminate multi-plaquette or large-winding gauge data.
- It does not prove that arbitrary action-level observables factor through
  the mass determinant.
- Independent review and audit own any effective status movement.

## Next Action

Send this PR through review and re-audit. Do not land audit results from this
branch.
