# Conditional positive quartic coefficient-to-scale theorem

**Date:** 2026-06-16
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** conditional algebraic theorem
**Primary runner:** [finite checks](../scripts/frontier_hierarchy_d4_density_scale_readout_bridge_2026_06_16.py)

## Premises and proof

Supply `rho_*>0`, `A(L)>0`, `A_ref>0`, and positive coordinates obeying
`rho_* = A(L) v(L)^4 = A_ref v_ref^4`. These equations are a stipulated
quartic density law; neither the physical dimension nor a physical density is
derived here. Positive real fourth roots exist uniquely, so division gives

```text
v(L) / v(L_ref) = (A_ref / A(L))^(1/4).
```

For `0<x<y`, `y^4-x^4=(y-x)(y+x)(y^2+x^2)>0`; hence the positive root is unique.
Equal coefficients give ratio one; a larger coefficient gives a smaller
coordinate at fixed density. This fixed positive D=4 density-coefficient readout
is conditional algebra. It does not identify the electroweak VEV, identify a
physical endpoint, or fix an absolute scale when `rho_*` is unspecified.
No observed target value or audit status enters this proof.

## Supplied coefficient family

For integer `L>=1` and real `u0 != 0`, define, rather than physically derive,

```text
A_L = (1/(2 L u0^2)) sum_(n=0)^(L-1) 1/(3+sin^2((2n+1) pi/L)).
```

All terms are positive. At `L=2`, every squared sine is one, so
`A_2=1/(8u0^2)`. At `L=4`, each squared sine is `1/2`, so
`A_4=1/(7u0^2)` and `A_2/A_4=7/8`.

Define the angular average `A_avg=(1/(2u0^2))(1/(2pi)) integral_0^(2pi)
[1/(3+sin^2 t)] dt`. Quarter-period symmetry and `x=tan(t)` give
`integral_0^(pi/2) dt/(3+sin^2 t) = integral_0^infinity dx/(3+4x^2)
= pi/(4 sqrt(3))`. Thus `A_avg=1/(4 sqrt(3) u0^2)` and
`A_avg/A_2=2/sqrt(3)`. The continuous periodic integrand also makes the finite
midpoint Riemann sums converge to this average as `L` tends to infinity. This
mathematical average is not a continuum thermodynamic or physical lattice limit.
The runner retains the historical variable name `A_inf` for this formula.

If these numbers are supplied as the coefficients in the quartic law, the
coordinate ratios are `(7/8)^(1/4)` and `(sqrt(3)/2)^(1/4)`, respectively.
Neither the finite condensate statistic in the [parent](HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md) nor a
physical Higgs density has been identified with this coefficient family.

## Checks and open boundary

The runner preserves all thirteen numerical predicates and their tolerances.
They evaluate the supplied formulas at `u0=1`, check fixed-density arithmetic,
and compare placements. Its average-formula self-comparison is a consistency
check, not an independent numerical integration or a proof of a continuum law.
The analytic integral proof above is a separate argument requiring independent
review. Documentary checks bind this scope, not a promised PASS count.

The previous missing-ledger membership contract and literal-True status check
are withdrawn from current authority and retained in the recovery source. No
physical selector is ruled out: extra dynamics or a justified density readout
may supply information absent from these equations.

## Recovery and execution boundary

The complete preceding argument, runner and cache are preserved at Git commit
`6919e7f72cc95c3df7d6a4e9aa1f43ab6d449dff` and in the external original-source
inventory `repair-9849-dimensional-readers/original-identities.json`. Historical
ledger assertions are not current scientific premises; no ledger is substituted
or restamped. The old cache is historical until a bounded execution binds the
revised source and its actual inputs. This source checkpoint claims no fresh run
or independent audit verdict.
