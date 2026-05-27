# Topological-Instanton Import Repair Handoff

Target row: `topological_instanton_textbook_infrastructure_import_note_2026-05-17`

PR purpose: replace the former named Yang-Mills topology import umbrella with
a bounded framework-local certificate for the finite pieces used downstream.

What changed:

- Added `scripts/topological_instanton_framework_certificate.py`.
- Rewrote the note so global Atiyah-Singer, Luescher flow, and smooth
  existence theorems are parallel context, not hidden retained imports.
- Locally certified 4D Hodge/Bogomolny algebra, BPST `8*pi^2`
  normalization, and twisted `T^4` `Q=k/N` arithmetic.
- Generated cache and audit pipeline outputs so the row is `unaudited`,
  `ready=true`, with a registered runner.

Verification:

```text
python3 scripts/topological_instanton_framework_certificate.py
python3 scripts/precompute_audit_runners.py --runners scripts/topological_instanton_framework_certificate.py --force --allow-non-main --push-mode none
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
```

Observed runner result:

```text
PASS=3 FAIL=0
```

Reviewer boundary: this PR does not claim retained status. It queues the
bounded algebra/arithmetic packet for independent audit.
