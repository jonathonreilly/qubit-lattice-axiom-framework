# Handoff

## What Changed

- Corrected the Section 2 truncation threshold from about `1.8` to about
  `1.91` using the runner's binary 4 GiB budget.
- Standardized binary memory labels from `GB` to `GiB` in the source note,
  runner, and cache.
- Added an explicit status firewall: this remains bounded-support and does not
  set audit status.

## Why It Matters

The previous note mixed decimal and binary unit conventions while the runner
used `1024^3`. That made the truncation-threshold argument look internally
inconsistent. The repaired version preserves the obstruction:

```text
(4 * 1024^3 / 16)^(1/30) ~= 1.91
```

Integer bond dimension is still at most `1`, and bond dimension `2` still
requires `16 GiB`.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_su3_wigner_l3_treewidth_2026_05_04.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_su3_wigner_l3_treewidth_2026_05_04.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_su3_wigner_l3_treewidth_2026_05_04.py`
- `python3 -m py_compile scripts/frontier_su3_wigner_l3_treewidth_2026_05_04.py`
- `git diff --check`

## Remaining Blockers

- No lower-bound certificate for true treewidth.
- No all-path optimizer search.
- No exact gauge-scalar bridge computation.

## Next Action

Open this as a review PR, then continue to the next conditional repair target.
