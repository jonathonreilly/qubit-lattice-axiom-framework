# Mermin-Wagner / Bogoliubov Import Repair Handoff

Target row: `mermin_wagner_bogoliubov_textbook_import_note_2026-05-18`

PR purpose: replace the former named textbook-import wrapper with a bounded
framework-local certificate for the finite Bogoliubov inequality and the
`Z^d` infrared divergence mechanism used downstream.

What changed:

- Added `scripts/mermin_wagner_bogoliubov_framework_certificate.py`.
- Rewrote the note so Mermin-Wagner/Hohenberg/Coleman are parallel literature
  citations, not uninspected retained imports.
- Kept Coleman's zero-temperature relativistic theorem out of the retained
  target scope; it needs a separate authority if downstream claims require it.
- Generated cache and audit pipeline outputs so the row is `unaudited`,
  `ready=true`, with a registered runner.

Verification:

```text
python3 scripts/mermin_wagner_bogoliubov_framework_certificate.py
python3 scripts/precompute_audit_runners.py --runners scripts/mermin_wagner_bogoliubov_framework_certificate.py --force --allow-non-main --push-mode none
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

Observed runner result:

```text
PASS=5 FAIL=0
```

Reviewer boundary: this PR does not claim retained status. It queues the
bounded finite-lattice mechanism for independent audit.
