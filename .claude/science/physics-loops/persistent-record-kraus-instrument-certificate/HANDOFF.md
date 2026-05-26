# Handoff

## Block

`persistent_record_as_kraus_operator_note_2026-05-20`

## Branch

`physics-loop/persistent-record-kraus-instrument-certificate-20260526`

## PR

https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/1948

## Claim movement

The previous audit objection was that the row named a record-conditional map as `K_r` without proving a normalized linear measurement instrument. This block adds a deterministic finite certificate for that exact algebraic bridge and updates the note to state the finite premise explicitly.

After running the audit pipeline locally, the row is ready for independent re-audit:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `runner_path`: `scripts/persistent_record_kraus_instrument_certificate.py`
- `open_dependency_paths`: `[]`

## Remaining blockers

- Independent audit must decide whether the finite-instrument bridge is sufficient for the row's bounded scope.
- The branch does not prove asymptotic persistent-record formation.
- The branch does not repair or promote the downstream Born-rule row.

## Verification

Run:

```bash
python3 scripts/persistent_record_kraus_instrument_certificate.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/vocab_lint.py --report-only docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md scripts/persistent_record_kraus_instrument_certificate.py .claude/science/physics-loops/persistent-record-kraus-instrument-certificate/*.md
python3 scripts/render_controlled_vocabulary.py --check
python3 -m py_compile scripts/persistent_record_kraus_instrument_certificate.py
python3 scripts/precompute_audit_runners.py --runners scripts/persistent_record_kraus_instrument_certificate.py --allow-non-main --check-only
git diff --check
```

## Next exact action

After this PR is opened and mergeability is clean, continue the campaign with the highest-impact independent audited-conditional row not already covered by an open PR.
