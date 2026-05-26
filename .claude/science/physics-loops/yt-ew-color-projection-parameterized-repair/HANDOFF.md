# Handoff

## What Changed

This PR repairs `yt_ew_color_projection_theorem` by narrowing it to the exact
parameterized algebra:

```text
K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)
```

The note now treats `kappa_EW` as a formal parameter. It does not derive,
admit, or promote `kappa_EW = 0`; the `9/8` specialization and observed
coupling comparisons are diagnostic context only.

## Audit Queue Result

After `docs/audit/scripts/run_pipeline.sh`:

- `audit_status: unaudited`
- `effective_status: unaudited`
- `deps: []`
- audit queue position: 1
- ready: true
- critical row, 554 descendants

No audit verdict is applied by this PR.

## Verification

```bash
python3 -m py_compile scripts/frontier_yt_ew_color_projection_parameterized.py
docs/audit/scripts/run_pipeline.sh
set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_yt_ew_color_projection_parameterized.py | tee outputs/yt_ew_color_projection_parameterized_repair_2026-05-25.txt
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/YT_EW_COLOR_PROJECTION_THEOREM.md scripts/frontier_yt_ew_color_projection_parameterized.py .claude/science/physics-loops/yt-ew-color-projection-parameterized-repair
git diff --check
```

Results:

- runner: `PASS=34, FAIL=0`
- pipeline: completed; target row `unaudited`, queue position 1, `deps: []`
- strict audit lint: no errors; one pre-existing Maradudin warning remains

## Remaining Blocker

The physical EW readout still needs a retained-grade selector theorem or exact
disconnected-current coefficient computation fixing `kappa_EW`, especially the
`kappa_EW = 0` specialization. This PR does not attempt that theorem.
