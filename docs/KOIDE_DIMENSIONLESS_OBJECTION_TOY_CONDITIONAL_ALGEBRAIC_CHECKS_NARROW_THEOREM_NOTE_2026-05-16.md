# Two-Channel Rational Functions and Exact Projectors — Positive Theorem

**Date:** 2026-05-16 (self-contained formal repair: 2026-07-16)
**Type:** positive_theorem
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note states and
proves a theorem; it neither assigns nor predicts an audit verdict.
**Tier:** exact finite algebra over `Q`
**Dependencies:** none
**Primary runner:**
[`scripts/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.py`](../scripts/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.py)
**Cached log:**
[`logs/runner-cache/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.txt`](../logs/runner-cache/audit_companion_koide_dimensionless_objection_toy_conditional_algebraic_checks.txt)

## Claim

The theorem consists only of identities for explicitly defined rational
functions and `2 x 2` rational matrices. Every variable is universally
quantified on the domain written below. No carrier, scalar, section, or
selection rule is assumed from elsewhere.

Let

```text
D = {(s,z) in Q^2 : 1+s+z != 0 and 1+s-z != 0}.
```

For `(s,z) in D`, define

```text
y_+(s,z) = 1/(1+s+z),
y_-(s,z) = 1/(1+s-z),
R(s,z)   = (1/3) [1 + y_-(s,z)/y_+(s,z)].
```

For `w in Q`, define `zeta(w)=2w-1`. In `V=Q^2`, with standard basis
`e_1,e_2`, define

```text
I = [[1,0],[0,1]],
P = [[1,0],[0,0]],
J = [[1,0],[0,-1]] = 2P-I,
L = span_Q{e_1}.
```

Finally, for arbitrary `eta,s,c in Q`, define

```text
d_eta(s,c) = eta(1-s)+c.
```

Then the following four statements hold.

### T1 — exact rational reduction and complete `2/3` fiber

For every `(s,z) in D`,

```text
R(s,z)       = 2(1+s) / [3(1+s-z)],
R(s,z) - 2/3 = 2z / [3(1+s-z)],
R(s,z) = 2/3 iff z = 0.
```

In particular, the two exact points `(0,1/4)` and `(0,-1/4)` belong to
`D` and give

```text
R(0,1/4)  = 8/9,
R(0,-1/4) = 8/15.
```

Thus the displayed definition is constructively nonconstant on `D`, while its
entire `2/3` fiber is exactly `{(s,0): s in Q, s != -1}`.

### T2 — exact affine coordinate

The map `zeta: Q -> Q` is a bijection with inverse
`zeta^{-1}(t)=(t+1)/2`. Consequently,

```text
zeta(w)=0 iff w=1/2,
zeta(w_1)-zeta(w_2)=2(w_1-w_2).
```

### T3 — exact projector and endomorphism dimensions

The matrices defined above obey

```text
P^2=P,       J^2=I,       JP=PJ=P.
```

Moreover,

```text
image(P)=L,                 kernel(P)=span_Q{e_2},
rank(P)=1,                  dim_Q End_Q(L)=1,
dim_Q End_Q(V)=4.
```

### T4 — arbitrary-parameter affine family

For every fixed `eta,s in Q`, the map `c -> d_eta(s,c)` is a bijection
`Q -> Q`, with inverse at target `t` given by

```text
c = t-eta(1-s).
```

The following identities therefore hold for every `eta in Q`:

```text
d_eta(0,0)       = eta,
d_eta(1,0)       = 0,
d_eta(1/2,0)     = eta/2,
d_eta(0,eta/2)   = 3eta/2.
```

The substitution `eta=2/9` is one exact example and gives

```text
d_(2/9)(0,0)     = 2/9,
d_(2/9)(1,0)     = 0,
d_(2/9)(1/2,0)   = 1/9,
d_(2/9)(0,1/9)   = 1/3.
```

The bijection theorem is stronger than a finite list of examples: for every
fixed `eta` and `s`, every rational target occurs at exactly one rational
shift `c`.

## Proof

For T1, direct division gives

```text
y_-/y_+ = (1+s+z)/(1+s-z).
```

Both factors exist on `D`. Combining terms over the common denominator gives

```text
R(s,z)
 = (1/3)[1+(1+s+z)/(1+s-z)]
 = (1/3)[2(1+s)/(1+s-z)].
```

Subtracting `2/3` yields

```text
R(s,z)-2/3
 = [2(1+s)-2(1+s-z)]/[3(1+s-z)]
 = 2z/[3(1+s-z)].
```

The denominator is nonzero on `D`, so this difference vanishes exactly when
`z=0`. At `z=0`, membership in `D` is equivalent to `s != -1`, proving the
fiber statement. Substituting `z=1/4` and `z=-1/4` at `s=0` gives `8/9` and
`8/15`. This proves T1.

For T2, solving `t=2w-1` gives the unique solution `w=(t+1)/2` in `Q`.
The zero and difference identities follow immediately.

For T3, exact multiplication gives

```text
P^2 = [[1,0],[0,0]],
J^2 = [[1,0],[0,1]],
JP = PJ = [[1,0],[0,0]].
```

For `(a,b) in Q^2`, `P(a,b)=(a,0)`. Hence its image is `L`, its kernel is
`span_Q{e_2}`, and its rank is one. Every endomorphism of the line `L` is
fixed by one rational coefficient. Every endomorphism of `V` is fixed by the
four rational entries of its `2 x 2` matrix; the four matrix units form a
basis. This proves T3.

For T4, at fixed `eta,s`, the equation `t=eta(1-s)+c` has the unique rational
solution `c=t-eta(1-s)`. This proves bijectivity. The general identities and
the `eta=2/9` example follow by exact substitution.

## Boundary of the theorem

This result is self-contained algebra over `Q`. The symbols are definitions,
not admissions, and they consume no framework axiom or approved primitive.
The theorem assigns no physical meaning to the two coordinates, the matrices,
the rational functions, or `eta`. In particular, it supplies no particle-mass
relation, Koide observable, physical source grammar, endpoint interpretation,
APS invariant, or framework selector. The example `eta=2/9` has exactly the
same formal status as any other rational substitution.

The historical filename preserves repository identity only; it contributes no
premise and broadens none of T1–T4.

## Cited dependencies and imports

None. The proof uses only field arithmetic in `Q`, elementary `2 x 2` matrix
multiplication, and the standard definitions of image, kernel, rank, and
finite-dimensional endomorphism space. No observed value, literature
comparator, fitted coefficient, unit convention, or same-surface claim is
used.

## Validation

The companion runner verifies the theorem with exact `Fraction` arithmetic in
three independent modes:

1. normal mode checks all formulas, dimensions, bijections, named examples,
   and exhaustive finite rational grids;
2. `--independent` reconstructs the rational identities by cross
   multiplication, uses an independent matrix-rank implementation, and checks
   each finite grid without calling the primary closed-form oracle;
3. `--hostile` rejects integers, booleans, floats, subclasses, malformed
   matrices, and all denominator singularities while enforcing the note's
   scope and dependency boundary.

Selectable mutation fixtures alter actual formulas, domain logic, matrices,
or source prose. Every individual mutation and the aggregate mutation must
produce a nonzero exit, demonstrating that the checks fail closed.
