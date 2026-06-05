# Beta=6 SU(3) Plaquette: d_11 Coefficient and Continuation-Spread Evidence

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. This note writes no audit verdict and supplies no
direct effective-status change.
**Primary runner:** [`frontier_beta6_d11_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d11_coefficient_2026_06_04.py)

## Scope

Two results: (i) the **exact** order-`beta^11` coefficient `d_11` of the connected
plaquette series `Delta(beta) = <P> - P_1plaq = sum_{n>=5} d_n beta^n`; and (ii)
a seven-coefficient Padé continuation-spread diagnostic for `<P>(6)`. This is a
frontier-discovery increment, NOT a closure of `<P>(6)` and NOT a proof of a
physical-value bound.

## The exact coefficient

```text
d_11 = -13/3967185807360 = -3.27688e-12         (NEGATIVE; d_11/d_10 = 52/31449 ~ 0.00165)
```

`|d_11|` is ~600x smaller than `|d_10|` -- a **near-cancellation** between the cube
and two-cube sectors:

```text
cube(11)            = -221/1322395269120  = -663/3967185807360   (-1.671e-10)
weight-10 class(11) =    5/44079842304    = +450/3967185807360   (+1.134e-10)
weight-11 class(11) =    5/99179645184    = +200/3967185807360   (+0.504e-10)
weight-12 class(11) =    0  (EXACT)        <- leading order of weight-12 vanishes
-------------------------------------------------------------------
d_11                = -13/3967185807360   (the small residue of -663 + 450 + 200)
```

`cube(11)` and `weight-10(11)` are reproduced from the reproven closed forms
`72 K''(K')^5` and `1080 K''(K')^9` (independent J-recurrence). Regression `d_5..d_10`
exact.

**weight-12 opens (leading order 11) but vanishes.** The weight-12 class = **two
disjoint elementary cubes** (0 shared faces), 240 distinct supports in **8
p0-fixing orbits** `{16,16,16,32,32,32,32,64}`. Its leading-order-11 cumulant is
**0 on all 8 orbits** (28 Fraction-engine confirmations); weight-12 first
contributes at order 12. The GF(3) 2-cycle weight spectrum through `p0` is exactly
`{6, 10, 11, 12}` -- the complete class list; the epsilon/det (baryon) sector is
built into every Haar link projector, not a separate class.

## Seven-coefficient continuation spread (diagnostic, not a bound)

The d-log-Padé approximants continue to place the nearest candidate singularity of
`Delta` in an off-real-axis complex-conjugate pair (estimated
`R ~ 5.35-5.39 < 6`; `[3/2]` gives `2.734 - 4.601 i`). This is radius evidence,
not a proof of the true radius or of divergence at `beta=6`. Padé continuation of
the normalized series `B(beta) = Delta/(d_5 beta^5)` evaluated at `beta = 6` (now
with 7 coefficients) gives `<P>(6) = 0.42253173965 + d_5 6^5 B(6)`:

```text
[2/3] -> 0.5899     [3/3] -> 0.5379     [2/4] -> 0.5140
[4/2] -> 0.5283     [3/2] -> 0.5191
```

**The estimates do NOT converge.** With six coefficients the single `[2/3]`
approximant gave `0.590` (near the lattice `0.5934`), but adding `d_11` the new
higher-order approximants cluster at `0.51-0.54`, so `[2/3]=0.590` is not a stable
trend. The honest continuation diagnostic is the approximant spread:

```text
Padé continuation spread:  ~0.51 to ~0.59    (7 coefficients)
```

This spread is compared after the fact with the Monte-Carlo comparator `0.5934`
and with the certified backbone value `0.5155` for the named convergent sectors
(separate note; not a full plaquette lower bound absent a remainder-sign proof),
but **the continuation does not pin or bound `<P>(6)`** at this coefficient depth.

## Path status (honest)

The exact strong-coupling series is now known through `d_11` (seven coefficients).
The approximant evidence continues to support a complex-pair radius below 6, but
this note does **not** prove divergence at `beta = 6`. The seven-coefficient
continuation spread is ambiguous and does not converge to a stable value. The next
coefficient `d_12` would add a useful diagnostic, but it requires the weight-12
class at order 12, whose worst link is the incidence-5 `(5,5)` projector -- the
documented `~10^7`-nnz OOM wall (treewidth-29). **So the feasible-coefficient
continuation route is at its current computational limit.** A separate route to a
controlled `<P>(6)` value would need a controlled tensor-network evaluation
(character-truncated TRG with bounded bond dimension and monitored error),
independent of the finite coefficient series.

## Boundary

- The **exact `d_11`** and `weight-12(11) = 0` are theorems (regression-validated;
  `cube(11)`, `weight-10(11)` from closed forms; `weight-11(11)` from the prior
  weight-11 enumeration; weight-12 leading = 0 by 28 Fraction-engine checks).
- The **continuation spread** `[0.51, 0.59]` is a numerical diagnostic from 7
  coefficients; it does NOT bound the physical value, prove convergence or
  divergence, establish a converged value, or close `<P>(6)`.
- Repins nothing (`u_0`, `alpha_s` untouched).

## Forbidden-import

Clean: every coefficient is reproven from the SU(3) Haar single-link integral and
the `J` recurrence. `0.5934` is an after-the-fact comparator. The Pade /
differential-approximant continuation methodology is cited as method only.

## Key files

- [`scripts/frontier_beta6_d11_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d11_coefficient_2026_06_04.py) (this note's runner)
- [`BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md) (the `d_10` coefficient and radius evidence)
- [`BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md) (the certified 0.5155 backbone support surface)
