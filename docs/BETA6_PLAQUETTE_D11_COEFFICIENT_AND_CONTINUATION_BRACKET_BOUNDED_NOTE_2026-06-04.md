# Beta=6 SU(3) Plaquette: d_11 Coefficient and the Continuation Bracket

**Date:** 2026-06-04
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. The independent audit lane sets audit and
effective status.
**Primary runner:** [`frontier_beta6_d11_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d11_coefficient_2026_06_04.py)

## Scope

The **exact** order-`beta^11` coefficient `d_11` of the connected plaquette series
`Delta(beta) = <P> - P_1plaq = sum_{n>=5} d_n beta^n`, plus an honest assessment of
what the analytic continuation of the now-7-term exact series says about `<P>(6)`.
Frontier_discovery increment; NOT a closure.

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

## What the continuation says about <P>(6) (honest, ambiguous)

The dominant singularity of `Delta` is a complex-conjugate pair off the real axis
(radius `R ~ 5.35-5.39 < 6`; reconfirmed by `[3/2]` d-log-Pade `2.734 - 4.601 i`),
so `Delta(6)` is a regular real value reachable only by analytic continuation. Pade
continuation of the bracket `B(beta) = Delta/(d_5 beta^5)` evaluated at `beta = 6`
(now with 7 coefficients) gives `<P>(6) = 0.42253173965 + d_5 6^5 B(6)`:

```text
[2/3] -> 0.5899     [3/3] -> 0.5379     [2/4] -> 0.5140
[4/2] -> 0.5283     [3/2] -> 0.5191
```

**The estimates do NOT converge.** With six coefficients the single `[2/3]`
approximant gave `0.590` (near the lattice `0.5934`), but adding `d_11` the new
higher-order approximants cluster at `0.51-0.54`, so `[2/3]=0.590` is revealed as a
non-robust outlier, not a trend. The honest statement is a **bracket**:

```text
<P>(6) in [~0.51, ~0.59]    (Pade continuation, 7 coefficients)
```

consistent with the Monte-Carlo comparator `0.5934` (which sits at/just above the
upper edge) and with the certified rigorous lower bound `0.5155` (separate note),
but **the continuation does not pin `<P>(6)`** at this coefficient depth.

## Path status (honest)

The exact strong-coupling series is now known through `d_11` (seven coefficients).
The series **diverges** at `beta = 6` (complex pair, `R < 6`), and its analytic
continuation **brackets** `<P>(6)` in `[0.51, 0.59]` without converging. The next
coefficient `d_12` would tighten the bracket, but it requires the weight-12 class
at order 12, whose worst link is the incidence-5 `(5,5)` projector -- the
documented `~10^7`-nnz OOM wall (treewidth-29). **So the feasible-coefficient
continuation route is at its limit.** The remaining route to a converged `<P>(6)`
is a controlled tensor-network evaluation (character-truncated TRG with bounded
bond dimension and monitored error), independent of the coefficient series.

## Boundary

- The **exact `d_11`** and `weight-12(11) = 0` are theorems (regression-validated;
  `cube(11)`, `weight-10(11)` from closed forms; `weight-11(11)` from the prior
  weight-11 enumeration; weight-12 leading = 0 by 28 Fraction-engine checks).
- The **continuation bracket** `[0.51, 0.59]` is a numerical statement from 7
  coefficients; it does NOT establish a converged value and does NOT close `<P>(6)`.
- Repins nothing (`u_0`, `alpha_s` untouched).

## Forbidden-import

Clean: every coefficient reproven from the SU(3) Haar single-link integral + the
`J` recurrence. `0.5934` is an after-the-fact comparator. The Pade /
differential-approximant continuation methodology is cited as method only.

## Key files

- [`scripts/frontier_beta6_d11_coefficient_2026_06_04.py`](../scripts/frontier_beta6_d11_coefficient_2026_06_04.py) (this note's runner)
- [`BETA6_PLAQUETTE_D10_COEFFICIENT_AND_DIVERGENCE_VERDICT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_DIVERGENCE_VERDICT_BOUNDED_NOTE_2026-06-04.md) (the R<6 verdict)
- [`BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md) (the rigorous 0.5155 lower portion)
