# Handoff

## What Changed

The row no longer claims an all-`L` OBC Widom asymptotic theorem, no longer
imports the `L <= 96` probe as binding evidence, and no longer presents the
small finite-L value near `1/4` as a BH coefficient derivation.

## Verification

- `python3 scripts/frontier_bh_entropy_derived.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/BH_ENTROPY_DERIVED_NOTE.md .claude/science/physics-loops/bh-entropy-finite-packet-rescope/*.md`
- `git diff --check`
