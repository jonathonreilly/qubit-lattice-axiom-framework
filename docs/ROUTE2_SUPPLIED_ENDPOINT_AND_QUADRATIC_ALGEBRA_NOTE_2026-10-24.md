# Supplied endpoint and quadratic-form algebra

**Date:** 2026-10-24
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** positive conditional identities and finite examples; no physical selector
**Primary runner:** [exact rational checks](../scripts/route2_supplied_endpoint_and_quadratic_algebra_2026_10_24.py)

## Supplied definitions, not physical endpoints

Let `rho_T=-1`, `mu=-2`, `q_T=1+rho_T/6=5/6`, and, for real `rho_E`,
`q_E=1+rho_E/6`. Restrict `q_E!=0` when defining `c_TE=mu*q_T/q_E`.
The comparator values in this note are supplied comparison data, not derived
quark masses, observed inputs or physical endpoints. No archived no-go,
carrier theorem, Fisher metric or current-source absence claim is a premise.

Straight substitution and rearrangement give the equivalence

```text
rho_E=21/4 <=> q_E=15/8 <=> c_TE=-8/9 <=> q_E/q_T=9/4.
```

In particular `c_TE=-5/(3q_E)`, so the nonzero-denominator condition makes its
inverse step valid. `rho_E=6(q_E-1)` gives the other inverse step.

For a supplied matrix family `P(r)=((1,0,r,0),(0,-2,0,2))`, evaluate on the
four supplied columns `e1`, `e1+e3/6`, `e2`, `e2+e4/6` of `R^4`.
The two-component outputs are `(1,0)`, `(1+r/6,0)`, `(0,-2)`, `(0,-5/3)`.
Only the second output varies with `r`; its slope is `1/6`, hence is injective.
This is a direct finite linear-algebra statement about these definitions, not
an exhaustion theorem about other readouts or physical mechanisms.

## Conditional monomial characterization and a counterexample to extension

Supply `w_E=1/3`, `w_T=1/2` and one common positive monomial law
`q_X=C*w_X^p`, where `C>0` and `p` is real. If the ratio is `9/4`, then
`(2/3)^p=9/4=(2/3)^(-2)`. Since `log(2/3)<0`, the function
`p -> exp(p log(2/3))` is strictly decreasing and therefore injective.
Thus `p=-2` uniquely **within the monomial family**. Matching the supplied
`q_T=5/6` then gives `C=q_T*w_T^2=5/24`. The finite integer sweep `-8..8`
in the runner is a check, not the proof for all real exponents.

Do not extend this uniqueness to unrestricted nonlinear laws. For any real `t`,

```text
f_t(w)=5/(24*w^2)+t*(w-1/3)*(w-1/2),  w>0,
```

matches both supplied endpoints. For `t!=0`, its value at `w=1` differs from
the inverse-square value by `t/3`. If it were a positive monomial matching the
same two endpoints, the preceding characterization would force that difference
to vanish. The member `t=1` is positive for all `w>0`: outside `[1/3,1/2]`
the added term is nonnegative; inside, `5/(24w^2)>=5/6` and the added term is
at least `-1/144`, so their sum is positive. This is an explicit positive
nonmonomial alternative, not just a law with unconstrained negative values.
No claim that arbitrary `t` preserves global positivity is made.

## Symmetric positive quadratic forms

Supply `S=(1,-2)`, `C(q)=(q,-5/3)` and the real symmetric matrix
`G=((a,c),(c,b))`, with `a>0` and `ab-c^2>0`. Completing the square gives
`x^T G x=a*(x1+(c/a)*x2)^2+((ab-c^2)/a)*x2^2`, so it is SPD.
Direct expansion yields

```text
C(q)^T G C(q)-S^T G S
 = a*(q^2-1)+2*c*(2-5*q/3)-11*b/9.
```

At the supplied comparator `q=15/8`, equal norms are equivalent to
`161*a/64-9*c/4-11*b/9=0`. This is compatibility, not unique selection.
For `c=0`, `a,b>0`, the equation is `q^2=1+11*b/(9*a)`. Under the additional
restriction `q>0`, it has one root; it equals `15/8` exactly when
`b/a=1449/704`. If negative `q` is permitted, `-15/8` is also a root.

Even `q>0` does not ensure uniqueness for general off-diagonal SPD metrics.
Take `a=1`, `c=3/5`, `b=3357/3520`. Its determinant is `10449/17600>0`,
and the residual factors exactly as `(q-15/8)*(q-1/8)`.
Thus two distinct positive roots coexist in this supplied SPD example.
No physical metric or endpoint-selection principle is inferred.

## Bounded integer comparison

At the comparator, clearing denominators gives
`1449*a-1296*c-704*b=0`. For integer coefficients this implies `a=0 mod16`.
The finite box is `1<=a,b<=64`, `-64<=c<=64`, with `ab-c^2>0`.
It suffices to test `a=16,32,48,64`, every integer `b=1..64`, and the unique
candidate `c=(1449*a-704*b)/1296`, retaining only integer in-box candidates.
The runner preserves the bounded search conclusion via these 256 exact
candidate evaluations. It does not claim an unrestricted absence of metrics:
`(a,b,c)=(704,1449,0)` is an explicit SPD solution outside the box.
The finite computation requires its own confirmed capture, not inherited
success from an archived runner.

## Recovery and current authority boundary

Two old Route2 notes were already archived, while their live runners/cache
still required absent docs/ notes. Those orphan runner/cache contracts are
now retired losslessly. Their original negative arguments, source inventories,
expected scores and old outputs are preserved as text alongside exact copies
of both archived notes in `archive/source-history/route2-orphan-contract-retirement-2026-10-24/`; `manifest.json` binds all six files.
The original archived notes are unchanged. No new source promotes their
route-pruning conclusions or proves the cited framework surfaces false.

This new owner is self-contained conditional mathematics. Its only runtime
repository input is this note for a documentary scope check. All numerical
constants and finite matrices are supplied explicitly in the runner. It uses
exact rational arithmetic; the real-exponent characterization is the analytic
proof above. No status/census/ledger, physical selector, new primitive or
whole-repository claim is established. New source confirmation and its own
bounded capture remain pending; no historical cache is reused for it.
