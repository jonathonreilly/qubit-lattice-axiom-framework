# Same-Family 3D Closure: Valley-Linear

**Date:** 2026-04-04 (live-source repair: 2026-05-27)
**Status:** bounded same-family finite-lattice closure packet, submitted for
re-audit after replacing the former print-only wrapper path with a live primary
runner.
**Claim type:** bounded_theorem

## Claim

On the ordered 3D dense lattice family with action `S = L(1-f)`, kernel
`1/L^2` with `h^2` measure, field `s/r`, slit geometry from the valley-linear
harness, and detector readout from the same harness, the primary runner
[`scripts/same_family_3d_closure.py`](../scripts/same_family_3d_closure.py)
now recomputes the load-bearing `h=0.25`, `W=10` finite-lattice closure rows:

- rows 1-7 at `L=12`;
- rows 8-9 at the same `h=0.25`, `W=10` slice for `L=8,10,12`;
- row 10 for the core `W=10` distance tail.

The widened `W=12` row-10 companion remains a dependency on the retained
bounded packet [`VALLEY_LINEAR_WIDE_TAIL_NOTE.md`](VALLEY_LINEAR_WIDE_TAIL_NOTE.md)
rather than a second live replay inside this primary runner.

## What Changed

The prior audit conditional blocker was not a failed science result. It was a
source-chain failure: the packet exposed a wrapper that printed frozen constants,
with rows 2, 6, 7 and the `L=8/L=10` same-slice rows not recomputed in the
executed path. The 2026-05-27 repair changes that executed path.

The repaired runner imports the same lattice/action implementation from
[`scripts/lattice_3d_valley_linear_card.py`](../scripts/lattice_3d_valley_linear_card.py),
declares a 30-minute audit timeout, and performs the actual finite-lattice
propagations for the core card, the same-`h` multi-`L` purity/gravity checks,
and the `W=10` distance-law fit. The runner exits nonzero if any of the bounded
certificate checks fail.

## Load-Bearing Dependencies

This note intentionally makes the dependency chain visible.

- [`VALLEY_LINEAR_ACTION_NOTE.md`](VALLEY_LINEAR_ACTION_NOTE.md) supplies the
  retained bounded action-family context for the fixed 3D ordered dense lattice
  comparison.
- [`VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md`](VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md)
  supplies the retained bounded bridge context for the `h/W` ladder and
  slice-dependent tail interpretation.
- [`VALLEY_LINEAR_WIDE_TAIL_NOTE.md`](VALLEY_LINEAR_WIDE_TAIL_NOTE.md) supplies
  the retained bounded `h=0.25`, `W=12` wide-tail companion used in row 10.
- [`scripts/lattice_3d_valley_linear_card.py`](../scripts/lattice_3d_valley_linear_card.py)
  is the helper source included in the audit packet for the lattice, action,
  field, slit, decoherence, and fit routines used by the primary runner.

## Recomputed Card

The current runner output reports:

| # | Property | Recomputed value | Slice |
|---|---:|---:|---|
| 1 | Born `|I3|/P` | `4.20e-15` | `h=0.25`, `W=10`, `L=12` |
| 2 | path distinguishability `d_TV` | `0.8341` | `h=0.25`, `W=10`, `L=12` |
| 3 | `k=0` gravity | `0.000000` | `h=0.25`, `W=10`, `L=12` |
| 4 | mass scaling `F~M alpha` | `1.00` | `h=0.25`, `W=10`, `L=12` |
| 5 | gravity sign at `z=3` | `+0.000224` TOWARD | `h=0.25`, `W=10`, `L=12` |
| 6 | decoherence | `49.9%` | `h=0.25`, `W=10`, `L=12` |
| 7 | detector mutual information | `0.6376` bits | `h=0.25`, `W=10`, `L=12` |
| 8 | purity stability | `49.97%`, `49.94%`, `49.94%` | `L=8,10,12` at same `h,W` |
| 9 | gravity growth | `+0.000157 -> +0.000199 -> +0.000224` | `L=8,10,12` at same `h,W` |
| 10 | distance tail | `b^(-0.93)`, `R^2=0.983`; `8/8` TOWARD | core `W=10` |

The retained `W=12` companion from
[`VALLEY_LINEAR_WIDE_TAIL_NOTE.md`](VALLEY_LINEAR_WIDE_TAIL_NOTE.md) reports
`b^(-1.07)`, `R^2=0.990` from `z>=4` and `b^(-1.17)`, `R^2=0.997` from
`z>=5`.

## Runner Boundary

The primary runner is still a bounded finite-lattice certificate, not a
continuum theorem. It proves that the stated computations close on this family
and these finite slices. It does not derive the valley-linear action, prove
universal Newtonian `1/b`, or claim stability under all future refinements.

The repair is therefore aimed at removing the specific audit blocker
`missing_dependency_edge` / `print-only wrapper`, not at expanding the physics
claim beyond the finite slices above.

## Re-Audit Target

The row should be re-audited as a bounded theorem packet with:

- primary runner:
  [`scripts/same_family_3d_closure.py`](../scripts/same_family_3d_closure.py);
- helper/source runner:
  [`scripts/lattice_3d_valley_linear_card.py`](../scripts/lattice_3d_valley_linear_card.py);
- retained dependencies:
  [`VALLEY_LINEAR_ACTION_NOTE.md`](VALLEY_LINEAR_ACTION_NOTE.md),
  [`VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md`](VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md),
  and [`VALLEY_LINEAR_WIDE_TAIL_NOTE.md`](VALLEY_LINEAR_WIDE_TAIL_NOTE.md).

The row should not be promoted by this edit alone. The independent audit owns
the verdict after checking that the repaired primary runner and the retained
dependencies close the stated finite-lattice chain.
