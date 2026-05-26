# Artifact Plan

## Created

- `scripts/persistent_record_kraus_instrument_certificate.py`
- `logs/runner-cache/persistent_record_kraus_instrument_certificate.txt`
- Updated `docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`
- Generated audit ledger and queue updates from `docs/audit/scripts/run_pipeline.sh`

## Final gates

- Run the certificate directly.
- Run the audit pipeline.
- Run strict audit lint.
- Run vocabulary checks.
- Run render-control check.
- Run Python compile check.
- Run runner-cache check-only.
- Run `git diff --check`.

## PR packaging

Open one review PR for this bounded-support block and record the PR URL in `HANDOFF.md` and `PR_BACKLOG.md`.
