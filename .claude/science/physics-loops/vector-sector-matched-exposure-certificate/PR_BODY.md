## Summary

This PR repairs `vector_sector_note` by adding a companion runner that explicitly logs the matched scalar exposure for the audited CCW/CW case and by narrowing the note to bounded support.

The new runner verifies:

- CCW `dz > 0`;
- CW `dz < 0`;
- `avg 1/r` scalar exposure matches exactly;
- the legacy vector runner is recorded as a helper.

## Claim Boundary

Honest status: bounded support, not an audit verdict.

This branch does not claim a retained vector-sector observable, a universal DC force, or a physical observable bridge from lock-in readout.

After the local audit pipeline:

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `runner_path`: `scripts/vector_sector_matched_scalar_exposure_certificate.py`
- `helper_runner_paths`: `['scripts/vector_sector_circular_orbit.py']`
- `open_dependency_paths`: `[]`

## Verification

- `python3 scripts/vector_sector_matched_scalar_exposure_certificate.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/vocab_lint.py --report-only docs/VECTOR_SECTOR_NOTE.md scripts/vector_sector_matched_scalar_exposure_certificate.py .claude/science/physics-loops/vector-sector-matched-exposure-certificate/*.md`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 -m py_compile scripts/vector_sector_matched_scalar_exposure_certificate.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/vector_sector_matched_scalar_exposure_certificate.py --allow-non-main --check-only`
- `git diff --check`
