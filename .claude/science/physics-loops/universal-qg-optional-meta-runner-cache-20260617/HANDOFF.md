# Universal QG Optional Meta Runner Cache Handoff

## Target

`UNIVERSAL_QG_OPTIONAL_TEXTBOOK_COMPARISON_NOTE.md` is a zero-authority
metadata row that already has a metadata invariant runner, but the source note
did not expose a plain runner-cache field. That makes it less discoverable for
audit replay tooling even though the row is intentionally not a physics
derivation.

## Change

- Adds a plain `Runner cache` header field to the source note.
- Makes the meta runner fail if the runner-cache field or the zero-authority
  audit-readiness boundary disappears.
- Refreshes the cached runner transcript.

## Honest Boundary

This PR does not add a universal-QG theorem, does not alter the row's
zero-authority role, and does not assert an audit outcome. It is source-side
metadata and cache wiring only.

## Verification

```bash
python3 scripts/universal_qg_optional_textbook_comparison_meta_check.py
python3 scripts/cached_runner_output.py --refresh scripts/universal_qg_optional_textbook_comparison_meta_check.py
python3 scripts/cached_runner_output.py --check-only scripts/universal_qg_optional_textbook_comparison_meta_check.py
python3 scripts/precompute_audit_runners.py --runners scripts/universal_qg_optional_textbook_comparison_meta_check.py --check-only
python3 -m py_compile scripts/universal_qg_optional_textbook_comparison_meta_check.py
git diff --check
git diff -- docs/audit docs/publication docs/repo/FRONT_DOOR_STATUS.md --stat
```
