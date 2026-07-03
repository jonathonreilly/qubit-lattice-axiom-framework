# Wilson Extremum Curvature Readout Boundary Certificate

**Date:** 2026-06-15
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py`](../scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py)

## Claim

This certificate isolates the framework-native part of the Wilson
extremum Higgs-sector bookkeeping from the two non-native readings that
must not be smuggled in as conclusions.

Given:

- the Wilson Hamming staircase normalization
  `W(hw) = 2 r hw` from
  [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md);
- the Wilson-shifted extremum `m* = -4r` and leading curvature
  `d2 V_taste^W/dm2|_{m*} = -4/u_0^2 + 12 r^2/u_0^4 + O(r^4)` from
  [`WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`](WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md);
- the parent diagnostic definition D1 in
  [`HIGGS_MASS_FROM_AXIOM_NOTE.md`](HIGGS_MASS_FROM_AXIOM_NOTE.md), where
  the mass-like quantity is explicitly the symmetric-point per-channel
  curvature scale `m_curv_tree`, not a Higgs pole;
- the uniform all-corners denominator `N_taste = 16`, read here only as
  the degenerate diagnostic count on the declared minimal-block surface,

the Wilson-shifted diagnostic curvature scale has the leading
source-side form

```text
(m_curv,W / v)^2
   = (1 / (4 u_0^2)) * (1 - 3 r^2/u_0^2) + O(r^4).             (1)
```

Equivalently,

```text
m_curv,W / m_curv,0
   = sqrt(1 - 3 r^2/u_0^2)
   = 1 - (3/2) r^2/u_0^2 - (9/8) r^4/u_0^4 + O(r^6).          (2)
```

This note proves only the normalized diagnostic readout (1)-(2). It
does not prove that the physical broken-phase Higgs pole is exhausted by
this diagnostic, does not derive the numerical Wilson coefficient `r`,
and does not derive a physical channel-selection principle for the
uniform all-corners readout.

## Boundary Split

**Closed native layer.** The native finite calculation fixes the
staircase normalization, the shifted extremum, the leading curvature
coefficient, the division by the declared 16-fold diagnostic count, and
the Taylor expansion of the resulting square-root readout. These are
finite combinatorics, scalar calculus on the registered Wilson
potential, and exact rational arithmetic.

**Declared diagnostic layer.** The denominator `N_taste = 16` is used as
the all-corners degenerate diagnostic count in D1. That is enough to
define `m_curv,W` as a per-channel curvature scale. It is not a
framework-native proof that the physical Higgs pole occupies a single
uniform all-corners channel.

**Open physical layer.** A physical Higgs-pole statement would still need
a retained bridge from the full broken-phase effective potential to this
diagnostic curvature surface, plus a retained or explicitly admitted
normalization for a nonzero Wilson coefficient. This certificate supplies
neither. The symbol `r` is normalized only by the upstream staircase law
`W(hw) = 2 r hw` and is otherwise carried symbolically.

## Proof Walk

The upstream extremum note gives the total leading curvature

```text
d2 V_taste^W/dm2|_{m*}
   = -4/u_0^2 + 12 r^2/u_0^4 + O(r^4).
```

Taking the curvature magnitude and dividing by the diagnostic count
`N_taste = 16` gives

```text
|d2 V_taste^W/dm2|/16
   = (4/u_0^2 - 12 r^2/u_0^4)/16 + O(r^4)
   = 1/(4 u_0^2) - 3 r^2/(4 u_0^4) + O(r^4)
   = (1/(4 u_0^2)) * (1 - 3 r^2/u_0^2) + O(r^4).
```

Applying the parent D1 diagnostic definition to this curvature magnitude
gives (1). The square-root expansion (2) follows from
`sqrt(1 - x) = 1 - x/2 - x^2/8 + O(x^3)` with
`x = 3 r^2/u_0^2`.

The same coefficient is checked against the all-orders closed form recorded in
`WILSON_M_H_TREE_AT_EXTREMUM_ALL_ORDERS_BOUNDED_NOTE_2026-05-08.md`
(context only, not a one-hop dependency here):

```text
(m_curv,W / v)^2
   = (1/64) * sum_{k=0}^4 binom(4,k)
       (u_0^2 - (k-2)^2 r^2) / ((k-2)^2 r^2 + u_0^2)^2.
```

Expanding the summand at `r = 0` gives
`1/u_0^2 - 3 (k-2)^2 r^2/u_0^4 + O(r^4)`. The centered binomial moment
`sum binom(4,k)(k-2)^2 = 16` then yields exactly the coefficient in
(1).

## Dependencies

- [`WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md`](WILSON_BZ_CORNER_HAMMING_STAIRCASE_BOUNDED_NOTE_2026-05-08.md)
  for the 16 corners, multiplicities `(1,4,6,4,1)`, and Wilson mass
  shift normalization `2 r hw`.
- [`WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`](WILSON_VTASTE_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md)
  for the shifted extremum and leading curvature coefficient.
- [`HIGGS_MASS_FROM_AXIOM_NOTE.md`](HIGGS_MASS_FROM_AXIOM_NOTE.md)
  for D1, the declared diagnostic curvature-scale definition.
- [`HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md`](HIGGS_CHANNEL_EFFECTIVE_NTASTE_BOUNDARY_BOUNDED_NOTE_2026-05-08.md)
  for the explicit boundary that the uniform `N_taste = 16` physical
  channel assignment is not derived by the staircase alone.

Context only, not a one-hop authority:
`WILSON_M_H_TREE_AT_EXTREMUM_ALL_ORDERS_BOUNDED_NOTE_2026-05-08.md`
records the closed-form all-orders expression used as an internal
consistency check by the runner. It is not a load-bearing dependency for
this certificate, avoiding a dependency cycle with that note.

## Boundaries

This certificate does not close:

- the physical Higgs-mass pole;
- the +12 percent Higgs gap chain;
- a derivation of a nonzero Wilson coefficient;
- a physical channel-selection principle for uniform all-corners
  `N_taste = 16`;
- the plaquette mean-field number `u_0`;
- the staggered-Dirac realization gate;
- any audit status change.

It only makes the Wilson extremum curvature-scale readout and its
remaining admission surface explicit enough for re-audit.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py
```

Expected:

```text
TOTAL: PASS=28 FAIL=0
VERDICT: Wilson extremum curvature readout boundary certified; native
leading coefficient and Taylor residuals verified, while the physical
Higgs-pole and Wilson-coefficient readings remain explicitly outside
scope.
```
