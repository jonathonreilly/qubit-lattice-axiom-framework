## Summary

This PR repairs `persistent_record_as_kraus_operator_note_2026-05-20` by adding a bounded finite-instrument certificate for the record-as-Kraus bridge.

The new runner constructs a finite normalized record-writing isometry, extracts record blocks `K_r`, and verifies:

- `W^* W = I`;
- `sum_r K_r^* K_r = I`;
- Choi positivity for the unconditional channel;
- sampled trace preservation and positivity;
- normalized positive selective states for nonzero record probabilities.

## Claim Boundary

Honest status: bounded support, not an audit verdict.

This branch does not:

- prove asymptotic persistent-record closure;
- promote or repair the downstream Born-rule row;
- introduce any new axiom;
- write an independent audit verdict.

After the local audit pipeline, the row is queued for independent re-audit:

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `runner_path`: `scripts/persistent_record_kraus_instrument_certificate.py`
- `open_dependency_paths`: `[]`

## Artifacts

- Source note: `docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`
- Runner: `scripts/persistent_record_kraus_instrument_certificate.py`
- Runner cache: `logs/runner-cache/persistent_record_kraus_instrument_certificate.txt`
- Loop handoff: `.claude/science/physics-loops/persistent-record-kraus-instrument-certificate/HANDOFF.md`
- Review history: `.claude/science/physics-loops/persistent-record-kraus-instrument-certificate/REVIEW_HISTORY.md`

## Verification

- `python3 scripts/persistent_record_kraus_instrument_certificate.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/vocab_lint.py --report-only docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md scripts/persistent_record_kraus_instrument_certificate.py .claude/science/physics-loops/persistent-record-kraus-instrument-certificate/*.md`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 -m py_compile scripts/persistent_record_kraus_instrument_certificate.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/persistent_record_kraus_instrument_certificate.py --allow-non-main --check-only`
- `git diff --check`

Known lint warning: this branch still sees the pre-existing lattice Green's Maradudin repair warning from the branch base; that row is handled by the separate lattice Green's certificate PR.
