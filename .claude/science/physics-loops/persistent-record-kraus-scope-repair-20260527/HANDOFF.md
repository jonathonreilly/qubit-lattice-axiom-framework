# Handoff

## What Moved

The persistent-record/Kraus row was narrowed to finite isometry-to-Kraus
instrument algebra. The physical bridge from persistent-record dynamics
to a normalized isometry remains open.

## Files

- `docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`
- `scripts/persistent_record_kraus_instrument_certificate.py`
- `.claude/science/physics-loops/persistent-record-kraus-scope-repair-20260527/`

## Verification

- `PYTHONPATH=scripts python3 scripts/persistent_record_kraus_instrument_certificate.py`
  - certificate pass; final label `FINITE_ISOMETRY_TO_KRAUS_INSTRUMENT_ALGEBRA=TRUE`
- `python3 scripts/vocab_lint.py --report-only ...`
  - clean
- `git diff --check`
  - clean
- `bash docs/audit/scripts/run_pipeline.sh`
  - complete; target row reset to `unaudited`, `claim_type=bounded_theorem`,
    with no deps or open dependency paths

## Remaining Blockers

The normalized record-writing isometry still needs a separate physical
bridge from persistent-record dynamics.

## Next Action

Draft PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2113

Proceed to the next ledger-order conditional row.
