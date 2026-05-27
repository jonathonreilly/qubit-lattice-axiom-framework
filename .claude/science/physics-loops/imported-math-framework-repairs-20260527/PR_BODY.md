## Summary

This PR repairs two imported-math bounded rows so their binding surfaces are
framework-local and auditable rather than raw textbook/paper imports.

- KMS/Brydges majorant: proves the finite framework comparison lemma directly
  on a scale mesh and leaves KMS as parallel literature context.
- Born/Gleason-Busch: routes finite ideal-record Born through retained-grade
  framework rows and adds a runner for the finite algebraic bridge.

This does not retag either row as retained. Both rows are reset to unaudited
bounded-theorem queue entries for independent audit.

Loop PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2085

## Target Rows

- `kms_fermionic_brydges_majorant_external_narrow_theorem_note_2026-05-11`
- `born_rule_from_gleason_busch_derivation_note_2026-05-20`

## Key Files

- `docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`
- `scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
- `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
- `scripts/born_rule_framework_bridge_check.py`
- `.claude/science/physics-loops/imported-math-framework-repairs-20260527/HANDOFF.md`
- `.claude/science/physics-loops/imported-math-framework-repairs-20260527/TRACE_GATE.md`
- `.claude/science/physics-loops/imported-math-framework-repairs-20260527/CLAIM_STATUS_CERTIFICATE.md`

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

## Boundaries

- No new axioms.
- No author-side retained retag.
- KMS substrate identification and physical bridge remain open.
- Born durable/native persistent record formation remains open.
- Born arbitrary unsharp instrument uniqueness remains open.
- Independent audit owns effective status.
