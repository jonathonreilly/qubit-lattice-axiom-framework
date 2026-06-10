# 3D 1/L^2 Tail Statistics Note

**Date:** 2026-04-04 (2026-06-10: default runner adds a live
width-6/width-8 head-to-head no-barrier tail-fit packet)
**Status:** bounded - bounded or caveated result note
**Type:** bounded_theorem
**Claim scope:** the load-bearing content is the bounded finite
`h = 0.25` tail-statistics packet. The frozen-log half verifies the
`width = 8` barrier sanity table: Born `3.75e-15`, `k=0` gravity
`0.000000`, dTV `0.358`, ATTRACTIVE barrier read, no-barrier rows
at `z = 4..8`, and post-peak fit `b^(-0.70)`, `R² = 0.955`.
The default runner now also computes the width-6 and width-8
no-barrier tail fits in one packet: width 6 has three post-peak rows
and fit `b^(-0.52)`, `R² = 0.906`, while width 8 has five post-peak
rows and fit `b^(-0.70)`, `R² = 0.955`. This supports only the
finite same-harness improvement claim; it does not prove an
asymptotic `1/r^2` law or promote the branch.
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/lattice_3d_l2_tail_stats.py`](../scripts/lattice_3d_l2_tail_stats.py)
defaults to a frozen-log verifier plus live width-6/width-8
head-to-head no-barrier tail-fit computation (`SCORECARD PASS=32
FAIL=0`). The original slow width-8 recomputation remains available
with `--recompute`, but the default audit packet uses the fast
layer-by-layer kernel for the comparator and calibrates it against
the frozen width-8 centroids and `P_near` rows.

**Review repair perimeter (2026-05-03 generated-audit context):**
Generated-audit context identified this chain-closure blocker: "The note states the width-8
statistics and the width-6 comparison, but the restricted packet
contains no runner output and no cited width-6 comparator authority.
The improvement claim therefore depends on premises not closed by
the provided inputs." The repair target being addressed is:
"provide the runner output/log as audit evidence and cite the exact
width-6 comparator note/status, or include the reproducible fit
calculation in the note." The 2026-06-10 runner repair takes the
second route: the registered primary runner computes both widths in
one packet and prints PASS/FAIL checks for the finite comparison.
This source repair does not set audit status. The runner cache file
[`logs/runner-cache/lattice_3d_l2_tail_stats.txt`](../logs/runner-cache/lattice_3d_l2_tail_stats.txt)
(the canonical SHA-pinned cache path under
[`scripts/runner_cache.py`](../scripts/runner_cache.py)) now records
the audit-compatible frozen-log plus head-to-head verifier with
`status: ok` at the default 120 s ceiling. The completed frozen
reference log
[`logs/2026-04-04-lattice-3d-l2-tail-stats.txt`](../logs/2026-04-04-lattice-3d-l2-tail-stats.txt)
remains the completed stdout artifact whose width-8 load-bearing
values are parsed and independently re-fit by the verifier. The
width-6 comparator defaults are the
[`scripts/lattice_3d_inverse_square_kernel.py`](../scripts/lattice_3d_inverse_square_kernel.py)
module-top constants `PHYS_L = 12.0`, `PHYS_W = 6.0` against which
this note's `lattice_3d_l2_tail_stats.py --recompute` patches
`PHYS_W = 8.0` (see the `patched_branch` context manager in the
runner). The default head-to-head packet uses
[`scripts/lattice_3d_l2_fast.py`](../scripts/lattice_3d_l2_fast.py)
as the layer-by-layer no-barrier computation helper; the primary
runner imports it directly so audit metadata can include the helper
source by transitive-import resolution.

## Purpose

This note freezes a narrow follow-up on the exploratory 3D `1/L^2`
propagator fork. The question is not whether the branch closes; it is
whether widening the `h = 0.25` lattice improves the post-peak tail fit
without losing the same-family barrier sanity checks.

Artifact chain:

- [`scripts/lattice_3d_l2_tail_stats.py`](../scripts/lattice_3d_l2_tail_stats.py)
- [`scripts/lattice_3d_inverse_square_kernel.py`](../scripts/lattice_3d_inverse_square_kernel.py)
- [`scripts/lattice_3d_l2_fast.py`](../scripts/lattice_3d_l2_fast.py)
- [`logs/2026-04-04-lattice-3d-l2-tail-stats.txt`](../logs/2026-04-04-lattice-3d-l2-tail-stats.txt)
- [`logs/runner-cache/lattice_3d_l2_tail_stats.txt`](../logs/runner-cache/lattice_3d_l2_tail_stats.txt)

## Result

The wider `h = 0.25` probe at `width = 8` stayed review-clean on the same
barrier geometry:

- Born: `3.75e-15`
- `k=0`: `0.000000`
- `dTV`: `0.358`
- barrier read: `ATTRACTIVE`

The no-barrier rows remained attractive across the post-peak sample:

| `z` | centroid | `P_near` | bias | read |
|---|---:|---:|---:|---|
| 4 | `+0.049373` | `+0.004422` | `+0.795766` | attractive |
| 5 | `+0.046445` | `+0.003459` | `+0.765371` | attractive |
| 6 | `+0.040248` | `+0.001309` | `+0.719169` | attractive |
| 7 | `+0.035067` | `+0.000651` | `+0.668926` | attractive |
| 8 | `+0.030697` | `+0.000357` | `+0.627323` | attractive |

Tail fit on the post-peak segment:

- `peak@z = 4`
- `n_tail = 5`
- exponent `b^(-0.70)`
- `R^2 = 0.955`

## Comparison

The default runner now performs the width-6/width-8 comparison in one
packet:

| width | no-barrier rows | peak | `n_tail` | exponent | `R²` |
|---:|---|---:|---:|---:|---:|
| 6 | `z = 4,5,6` | 4 | 3 | `b^(-0.52)` | `0.906` |
| 8 | `z = 4,5,6,7,8` | 4 | 5 | `b^(-0.70)` | `0.955` |

On this finite same-harness packet, the wider lattice gives:

- more post-peak support points
- a steeper tail
- slightly better `R^2`

The right review-safe wording is still narrow:

- the wider lattice **improves the post-peak tail fit**
- it does **not** by itself prove an asymptotic `-2` law
- it remains a propagator-fork probe, not a branch theorem

## Cited authority chain (2026-06-10)

The generated-audit context cited at top flagged that the
restricted audit packet "contains no runner output and no cited
width-6 comparator authority." The cited-authority chain on this
row is:

| Cited authority | File / log | Role |
|---|---|---|
| Active runner | [`scripts/lattice_3d_l2_tail_stats.py`](../scripts/lattice_3d_l2_tail_stats.py) | default audit mode verifies the frozen width-8 log, parses the five no-barrier rows, recomputes the post-peak tail exponent/R² from the logged centroids, and then computes the width-6/width-8 no-barrier tail fits in one live packet; `--recompute` preserves the original heavy width-8 computation that patches `PHYS_W = 8.0` over the inverse-square kernel default `PHYS_W = 6.0` via the `patched_branch` context manager |
| Width-6 comparator defaults | [`scripts/lattice_3d_inverse_square_kernel.py`](../scripts/lattice_3d_inverse_square_kernel.py) | module-top constants `PHYS_L = 12.0`, `PHYS_W = 6.0`, `PHYS_CONNECTIVITY = 3.0`; provides the reference family and scalar readout helpers used here |
| Fast head-to-head helper | [`scripts/lattice_3d_l2_fast.py`](../scripts/lattice_3d_l2_fast.py) | layer-by-layer no-barrier `1/L^2` propagation used by the primary runner to compute the width-6 and width-8 tail fits inside the default audit packet; the primary runner calibrates the width-8 centroids and `P_near` values against the frozen log |
| Frozen runner output | [`logs/2026-04-04-lattice-3d-l2-tail-stats.txt`](../logs/2026-04-04-lattice-3d-l2-tail-stats.txt) | preserves the exact width-8 Born=3.75e-15, k0=+0.000000, dTV=0.358 barrier row, the five no-barrier centroid rows for `z=4..8`, and the `tail fit: peak@z=4 n_tail=5 exponent=b^(-0.70) R^2=0.955` line cited in the Result table |
| Audit-lane runner cache | [`logs/runner-cache/lattice_3d_l2_tail_stats.txt`](../logs/runner-cache/lattice_3d_l2_tail_stats.txt) (canonical path under `scripts/runner_cache.py`) | SHA-pinned cache for the current runner source; records `status: ok` for the default verifier, including the exact width-8 table checks and the live width-6/width-8 head-to-head (`SCORECARD PASS=32 FAIL=0`). |
| Cache contract | [`scripts/runner_cache.py`](../scripts/runner_cache.py) | declares the cache header format and `runner_sha256` pinning that lets the audit lane verify the cache is fresh against the current runner source |

The width-6 baseline is now computed directly in the primary packet:
same family, same action, same `h = 0.25`, and no barrier, with
`PHYS_W = 6.0` rather than the width-8 patch. Its live fit
`b^(-0.52)` is the source of the earlier rounded `b^(-0.53)`
summary wording.

## Upstream authority (width-6 comparator wrapper)

- [LATTICE_3D_INVERSE_SQUARE_KERNEL_HELPER_NOTE_2026-04-04.md](LATTICE_3D_INVERSE_SQUARE_KERNEL_HELPER_NOTE_2026-04-04.md) — bounded helper-module wrapper for `scripts/lattice_3d_inverse_square_kernel.py`, documenting the module-top width-6 comparator defaults (`PHYS_L = 12.0`, `PHYS_W = 6.0`, `PHYS_CONNECTIVITY = 3.0`, `MASS_Z_VALUES = [2.0..7.0]`) and the helper functions (`build_family`, `barrier_metrics`, `no_barrier_distance`, `fit_power`) that this note patches via the `patched_branch` context manager to obtain the width-8 row.

This rigorization edit only supplies the missing head-to-head compute
packet and registers the cited authority chain; it does not set audit
status, hand-author audit JSON, or claim a stronger asymptotic law
beyond the bounded post-peak improvement already in scope.
