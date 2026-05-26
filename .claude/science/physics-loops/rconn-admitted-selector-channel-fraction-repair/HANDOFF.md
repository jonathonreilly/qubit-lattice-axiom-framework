# Handoff

## What changed

This block repairs `rconn_derived_note` by reducing it to exact finite
channel-fraction algebra:

- `dim(M_3(C)) = 9`
- `dim(C I_3) = 1`
- `dim(sl_3(C)) = 8`
- `F_adj = 8/9`
- `P(kappa_EW) = 8/9 + kappa_EW/9`

`R_conn = 8/9` is stated only under the explicit connected-trace selector
premise `(M0)`.

## Files

- `docs/RCONN_DERIVED_NOTE.md`
- `scripts/frontier_rconn_admitted_selector_channel_fraction_repair.py`
- `outputs/rconn_admitted_selector_channel_fraction_repair_2026-05-25.txt`

## Verification

- `bash docs/audit/scripts/run_pipeline.sh`
- `PYTHONPATH=scripts python3 scripts/frontier_rconn_admitted_selector_channel_fraction_repair.py`
- `python3 -m py_compile scripts/frontier_rconn_admitted_selector_channel_fraction_repair.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/RCONN_DERIVED_NOTE.md .claude/science/physics-loops/rconn-admitted-selector-channel-fraction-repair/*.md`
- `git diff --check`

## Remaining blocker

The branch does not derive the connected-trace selector. If audit accepts the
rescope, the row should be judged only as narrowed conditional-support.
