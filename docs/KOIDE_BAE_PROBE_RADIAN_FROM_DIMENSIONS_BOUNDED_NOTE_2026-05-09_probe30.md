# Probe 30: supplied dimensional kernel and finite angle fixtures

**Date:** 2026-05-10 (scope corrected 2026-10-25)
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane; this source does not assign an audit outcome.
**Primary runner:** [`scripts/cl3_koide_bae_probe_radian_from_dimensions_2026_05_09_probe30.py`](../scripts/cl3_koide_bae_probe_radian_from_dimensions_2026_05_09_probe30.py)
**Cached output:** [`logs/runner-cache/cl3_koide_bae_probe_radian_from_dimensions_2026_05_09_probe30.txt`](../logs/runner-cache/cl3_koide_bae_probe_radian_from_dimensions_2026_05_09_probe30.txt)

## Supplied premises and exact statement

Take seven nonzero variables `(a_s,a_tau,v,M,hbar,P,g)` with dimensions
`L,T,L/T,M,ML²/T,1,1`. The names are labels, not a physical identification
of a lattice, ultraviolet mass, velocity, gauge coupling or measured plaquette.
For integer powers let the exponent vector be `(p,q,r,s,t,u,w)`.
For arbitrary real powers instead require all seven variables positive.
The dimensional exponent matrix, in rows L,T,M, is

```
D = [[1,0, 1,0, 2,0,0],
     [0,1,-1,0,-1,0,0],
     [0,0, 0,1, 1,0,0]].
```

A monomial is dimensionless precisely when
`p+r+2t=0`, `q-r-t=0`, `s+t=0`. Thus
`p=-r-2t`, `q=r+t`, `s=-t`. The columns for `a_s,a_tau,M`
form the identity, so rank is three and nullity four. Define

```
x1 = v*a_tau/a_s
x2 = M*a_s*v/hbar
```

Every dimensionless monomial has exactly the form
`x1^(r+t) * x2^(-t) * P^u * g^w`. Substitution gives the seven
exponents above, proving both directions. The four independent exponent
vectors are `(-1,1,1,0,0,0,0)`, `(1,0,1,1,-1,0,0)`, and the P,g unit
vectors. This is a statement about monomials in the supplied variables,
not an exhaustive inventory of physical observables or arbitrary functions.
Finite sums and quotients of such dimensionless monomials remain
dimensionless wherever denominators are nonzero; no converse about arbitrary
physical expressions is asserted.

## What dimensions do and do not fix

Four generators do not mean four possible numerical values. Setting `x1=1`
requires `v*a_tau=a_s`; a coherent change of measurement units leaves x1
unchanged. x2 is free: take positive numerical representatives
`a_s=a_tau=v=hbar=1`, `M=2pi`. Then x2=2pi. Dimensional analysis therefore
cannot exclude this value or select an angular phase.

The former expressions `M*a_tau/hbar`, `M*a_s/hbar`, `a_s/a_tau` have
respectively dimensions `T²/L²`, `T/L`, `L/T`; they are not alternative
dimensionless generators. Also the principal logarithm of 1 is zero,
not `2pi*i`. No algebraic independence of e and pi, arithmetic nature
of an underlying Monte Carlo quantity, or field exclusion is used here.

## Finite diagnostics, not parameter selection

The primary retains the supplied decimal P=.5934, g=1 and x1=1 fixtures,
the scan of p,r=1,...,100 against 2pi at absolute tolerance 1e-6, and the
original comparisons with `math.e`, cubic roots of unity and four momenta.
These are finite checks with their original thresholds, not transcendence
proofs. The rounded comparison vector is `(0.97540,-0.67857,-0.29683)`;
it is supplied comparator data, not a mass prediction.

Exactly ten alpha fixtures are used: `1,2pi,4pi,pi,2pi/3,2pi/9,x1=1,g=1,
P=.5934,e`. The cosine comparison uses phi=2/9 and relative tolerance
1e-3, with the original denominator floor 1e-9. Statements about passing
fixtures refer only to this list. In particular, for every integer k,
`alpha=1+9pi*k` yields the same three cosines because the argument shifts
by `2pi*k`. Nonzero sufficiently small changes of alpha also pass a
positive tolerance by continuity wherever the baseline passes strictly.
Neither a finite list nor tolerance agreement proves uniqueness.

## Withdrawn historical argument and evidence boundary

The old full-source version is retained in the bounded repair recovery.
Its dimensional inventory exclusion, e/pi inference, literal-log error,
physical provenance assertions, universal exhaustion, five-route no-go
and admission-count conclusions are withdrawn. Assignments and literal
True assertions survive only as `HISTORICAL_UNSCORED` output, never PASS.
All meaningful old finite predicates retain their expressions and thresholds;
the external predicate map records every old assertion and its disposition.
The runner adds exact integer kernel controls and finite counterexample
controls; the proof above supplies the general kernel and periodicity claims.
No other note is a proof premise. The old cache is historical until a separately
authorized source-bound execution. Physical phase selection remains open;
this note neither proves impossibility nor reduces a campaign ledger.
