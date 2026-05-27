# Handoff

## Summary

This branch repairs two imported-math cases by making the binding mathematics
framework-local and auditable:

- KMS/Brydges majorant: proves the finite scale-mesh comparison lemma directly
  and keeps KMS as a parallel background reference.
- Born/Gleason-Busch: routes finite ideal-record Born through retained-grade
  framework Gleason, Busch, pre-record tracial, Kraus/Choi, Naimark/Luders, and
  sequential-product rows, with a new finite algebra runner.

## Files Changed

- `docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`
- `scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
- `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
- `scripts/born_rule_framework_bridge_check.py`
- Audit pipeline outputs under `docs/audit/`
- Loop pack under `.claude/science/physics-loops/imported-math-framework-repairs-20260527/`

## Verification

- `python3 scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
  - `TOTAL: PASS=20, FAIL=0`
- `python3 scripts/born_rule_framework_bridge_check.py`
  - `TOTAL: PASS=25, FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`
  - clean
- `python3 scripts/vocab_lint.py --report-only docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete

## Audit Queue Effects

- KMS row reset to `unaudited`, `claim_type=bounded_theorem`, ready in queue.
- Born row reset to `unaudited`, `claim_type=bounded_theorem`, ready in queue.
- Dispatch queue includes a live targeted Born review entry for the
  `lsp_projective_born_chain` lane.

## Residuals

- KMS substrate identification and physical bridge remain open.
- Born durable/native record formation remains open.
- Born arbitrary unsharp instrument uniqueness remains open.
- Bernoulli/CKM rows were not changed here because their current blocker is
  upstream audit readiness, not raw imported textbook math.
- Lawson-Michelsohn/Clifford chirality was not changed here because the
  inspected row was already retained/audited-clean.

## PR

PR URL: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2085
