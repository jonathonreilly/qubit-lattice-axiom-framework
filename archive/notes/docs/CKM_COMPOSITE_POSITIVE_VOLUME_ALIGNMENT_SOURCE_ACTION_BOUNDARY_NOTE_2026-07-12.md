# CKM Composite Positive-Volume Alignment Source-Action Boundary

**Date:** 2026-07-12

**Claim type:** bounded_theorem

**Actual current-surface status:** exact support/boundary theorem

**Trace class:** negative_route_pruning

**Reachability to target:** prunes

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:**
[`scripts/frontier_ckm_composite_positive_volume_alignment_source_action_boundary.py`](../scripts/frontier_ckm_composite_positive_volume_alignment_source_action_boundary.py)

## 1. Target and result

The parent
[`CKM_MASS_OPERATOR_PROJECTOR_OVERLAP_TYPING_THEOREM_NOTE_2026-07-12.md`](CKM_MASS_OPERATOR_PROJECTOR_OVERLAP_TYPING_THEOREM_NOTE_2026-07-12.md)
reduced the five-sixths bridge to

```text
t := Tr(P_c^u P_b^d) = (m_s/m_b)^(5/3).                 (1.1)
```

This note attacks the remaining source/action target from three independent
directions. It establishes:

1. even on the residual-`Z_2` Hermitian normal form (reproduced here in the
   runner's narrow commutant scope), fixed simple up/down spectra leave `t`
   free over the whole interval `[0,1]`;
2. Jacobi/NNI sparsity likewise constructs mass operators but does not select
   their relative eigenbasis;
3. there is an exact target-equivalent positive composite for which determinant
   neutrality, or equivalently removal of the positive volume mode, uniquely
   forces (1.1) after explicit rank and block-weight dictionaries are supplied.

The third result is a sharp conditional representation, not a current
framework derivation or a prediction. The authorities cited and tested here do
not select its tensor carrier, asymmetric lift, block-weight dictionary,
determinant-sector compression, or variational principle. The remaining
physical imports are therefore explicit rather than hidden.

## 2. Minimal allowed surface

The algebraic results use:

- a supplied physical left-handed generation space `H_g = C^3`;
- supplied positive simple-spectrum mass-squared operators `H_u,H_d`;
- their spectral projectors and the standard CKM semantics from the parent;
- an abstract six-state space `H_6=C^6` with a supplied rank-one projector
  `Q`, and `P=I_6-Q`;
- `R=m_s/m_b` with `0<R<1`.

The labels `u,c,t` and `d,s,b` are supplied ordered-spectrum labels inherited
from the parent. They are a naming/readout convention, not a derived result.

The residual-`Z_2` test reuses the exact five-parameter `Z_2` commutant normal
form set out in
[`Z2_HW1_MASS_MATRIX_PARAMETRIZATION_NOTE.md`](Z2_HW1_MASS_MATRIX_PARAMETRIZATION_NOTE.md)
(that note's own broader `S_3`-locus claim is not consumed here, and the
commutant structure used below is reconstructed and checked directly by the
paired runner).

Forbidden proof inputs are observed masses, CKM targets, fitted texture
coefficients, nearest-rational selection, an imported gauge-link
unimodularity condition, or an assertion that Record supplies a log-determinant
source action.

The current
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
explicitly leaves source/action and physical-observable identification outside
axiom content. The scale-reference, kinetic-isotropy, and realized-state
primitives supply no mass operator, flavor selector, mixing angle, or
source/action law.

## 3. Fixed-spectrum residual-`Z_2` orbit theorem

Work in the ordered basis `(X_3,X_1,X_2)` and let the residual `Z_2` exchange
the last two basis vectors. Define

```text
e_0 = X_3,
e_+ = (X_1+X_2)/sqrt(2),
e_- = (X_1-X_2)/sqrt(2).                                (3.1)
```

The sign line `span(e_-)` and the two-dimensional trivial block
`span(e_0,e_+)` are invariant. Fix any three distinct positive eigenvalues in
each sector. Put the charm eigenline at `e_0` and rotate only the down-sector
bottom eigenline inside the trivial block,

```text
v_b(theta) = cos(theta)e_0 + sin(theta)e_+,
v_s(theta) =-sin(theta)e_0 + cos(theta)e_+.              (3.2)
```

Both operators remain in the exact residual-`Z_2` commutant and both spectra
remain fixed, while

```text
Tr(P_c^u P_b^d(theta)) = cos(theta)^2.                   (3.3)
```

Thus the overlap spans `[0,1]`. In particular, the normal form admits an
orientation satisfying (1.1), but does not select it.

Because each `H_q` is positive, its unique positive square root
`H_q^(1/2)` gives an abstract positive factor on the same left carrier with
the same spectral projectors. It is not a physically typed Dirac mass operator:
that would additionally require a right-handed carrier, a right-to-left map,
and the corresponding right-unitary data. The construction therefore gives a
fixed-spectrum left-operator pair family, not a physical mass-pair derivation.

An exact endpoint counterpair makes the freedom concrete:

```text
H_d = [[9, 0,   0  ],
       [0, 5/2, 3/2],
       [0, 3/2, 5/2]],             spec(H_d)={1,4,9},

H_u^(0) = [[4, 0,    0   ],
           [0, 17/2, 15/2],
           [0, 15/2, 17/2]],       spec(H_u^(0))={1,4,16},

H_u^(1) = [[16,0,   0  ],
           [0, 5/2, 3/2],
           [0, 3/2, 5/2]],         spec(H_u^(1))={1,4,16}. (3.4)
```

For `H_u^(0)`, `P_c^u=P_b^d=|X_3><X_3|` and the overlap is one. For
`H_u^(1)`, the charm line is `span(e_+)`, orthogonal to the bottom line, and
the overlap is zero.

Full unbroken `S_3` does not repair this freedom: an `S_3`-invariant Hermitian
operator on `C^3` reduces to a scalar plus a multiple of the all-ones matrix and
therefore carries a repeated eigenvalue, the same abstract degeneracy recorded in
[`S3_MASS_MATRIX_NO_GO_NOTE.md`](S3_MASS_MATRIX_NO_GO_NOTE.md). Shared `C_3` circulants are simultaneously
Fourier diagonal and give only zero/one projector overlaps. Distinct residual
axes require an additional sector selector and yield either discrete
mass-independent overlaps or renewed continuous freedom.

## 4. Exact 18-dimensional determinant-balance construction

Let

```text
t = Tr(P_c^u P_b^d),
B = P_b^d.
```

On `H_6 tensor H_g`, define three mutually orthogonal projectors

```text
C = Q tensor I_3,             rank(C)=3,
D = P tensor B,               rank(D)=5,
E = I_18-C-D,                 rank(E)=10.               (4.1)
```

For `t>=0`, define the positive-semidefinite composite

```text
Z(t,R) = t C + R^(-1) D + E.                            (4.2)
```

Its spectrum and determinant are exact:

```text
spec Z = {t [x3], R^(-1) [x5], 1 [x10]},
det Z  = t^3 R^(-5).                                    (4.3)
```

Therefore

```text
det Z = 1
<=> t^3 = R^5
<=> Tr(P_c^u P_b^d) = R^(5/3).                          (4.4)
```

The construction places the three-generation multiplicity and
five-dimensional complement in one typed determinant equation. It is also an
exact representation of the target residual: the chosen ranks and scalar
block assignments already determine the powers in (4.4).

More generally, for positive block powers `alpha,beta`,

```text
Z_(alpha,beta)=t^alpha C+R^(-beta)D+E
```

has determinant `t^(3 alpha)R^(-5 beta)`, so determinant neutrality gives

```text
t=R^(5 beta/(3 alpha)).                                 (4.5)
```

Thus `alpha=beta=1`, the assignment of `t` itself to the rank-three block,
and the inverse-ratio assignment to the rank-five block are independent
selector content. No fitted numerical coefficient remains after those
dictionaries are supplied, but the dictionaries encode the desired exponent.

## 5. Conditional positive-volume action theorem

Restrict this section to `0<t<=1`, where `Z` is positive definite. At `t=0`,
the determinant identity remains valid but `log Z` and the affine-invariant
action are undefined; the action diverges as `t` approaches zero from above.

Let `SPD_1(18)` be the determinant-one positive cone. Use the unnormalized
trace affine-invariant metric
`g_A(U,V)=Tr(A^(-1) U A^(-1) V)`. The squared distance from `Z` to this cone
is

```text
Gamma_vol(Z)
  = dist_AI(Z,SPD_1(18))^2
  = (Tr log Z)^2/18
  = (3 log t - 5 log R)^2/18.                            (5.1)
```

For fixed `0<R<1`, this nonnegative action has the unique zero and unique
global minimum

```text
t_* = R^(5/3).                                           (5.2)
```

An equivalent scalar determinant action is

```text
z = det Z,
Gamma_det(z) = z-log(z)-1 >= 0,                          (5.3)
```

with equality only at `z=1`. Equations (5.1)-(5.3) contain no measured or
fitted coefficient.

For completeness, the distance formula follows directly. For any
`B in SPD_1(18)`, put `L=log(Z^(-1/2) B Z^(-1/2))`. Then

```text
Tr L = -log det Z,
||L||_F^2 >= (Tr L)^2/18                                (5.4)
```

by Cauchy-Schwarz. Equality holds at
`B_*=(det Z)^(-1/18) Z`, whose determinant is one. This proves (5.1) without
assuming the target minimum.

The theorem is conditional on the physical statement that the quark composite
uses (4.1)-(4.2), the unit block powers in (4.5), and suppression of its
positive volume mode. No authority cited or tested here supplies that complete
statement.

## 6. Why the conditional action is not yet derived

### 6.1 Rank-lift selector

For orthogonal blocks with general ranks `(a,b)`, determinant neutrality gives

```text
det(t C_a + R^(-1)D_b + E)=t^a R^(-b)=1
=> t=R^(b/a).                                            (6.1)
```

The desired exponent follows from `(a,b)=(3,5)` only after the unit block
powers in (4.5) are also supplied. Other equally covariant
unions of the atomic tensor projectors have different ranks and give
different exponents. Covariance alone does not select `Q tensor I_3` against
the other possible singlet lifts, or `P tensor P_b^d` against the other
fivefold/complement lifts.

### 6.2 Natural spectral actions do not couple the blocks

The full positive-matrix action

```text
Tr Z-log det Z-18
 = 3(t-log t-1)+5(R^(-1)+log R-1)                       (6.2)
```

is minimized at `t=1`, independently of `R`. More generally, for a
differentiable scalar function `f` fixed independently of `R`, the separable
trace-spectral action has the form

```text
Tr f(Z)=3f(t)+5f(R^(-1))+10f(1),                        (6.3)
```

so its stationarity equation `f'(t)=0` is independent of `R`. A bare
`log det Z` term has no interior stationary point. The needed physics is
specifically determinant-sector compression or an equivalent nonseparable
volume constraint.

The simplest mixed action on the mass pair also fails on its exact orbit
class. Under `H_u -> exp(epsilon K) H_u exp(-epsilon K)` with anti-Hermitian
`K`,

```text
delta Tr(H_u H_d)=Tr(K[H_u,H_d]).                        (6.4)
```

Stationarity for every `K` therefore requires `[H_u,H_d]=0`. For simple
spectra the operators share an eigenbasis, so their rank-one overlaps are
zero or one up to permutation. This prunes the linear mixed-trace action, not
general nonlinear paired actions.

Gauge-link `SU(3)` unimodularity cannot be imported here: it applies to
unitary three-color holonomies, whereas `Z` is a positive `18 x 18` composite
source operator. Treating those spaces as the same is a type error.

### 6.3 The mass pair remains only supplied

Even if (5.1) is granted, it consumes the already supplied projectors and
ratio. It does not derive absolute scales, the other quark eigenvalues,
remaining CKM entries or phases, or the full operators `M_u,M_d`. It is a
one-scalar alignment selector, not a quark source action in full.

## 7. NNI and inverse-spectral falsifiers

A real `3 x 3` Jacobi matrix has five coefficients. Its trace, quadratic
characteristic coefficient, and determinant give three independent spectral
constraints at generic points, leaving a two-real-dimensional isospectral
family. The runner also checks an explicit strict-Jacobi fixed-spectrum
counterfamily with continuously varying relative overlap.

On a two-family geometric-mean NNI block, and on the small-angle branch
`0<R<2^(-3/5)`,

```text
theta = (1/2) atan(2 c_23 sqrt(R)/(1-R)).                 (7.1)
```

For an aligned up sector with dimensionless block

```text
M(R,c_23)=[[R, c_23 sqrt(R)],
           [c_23 sqrt(R), 1]],                           (7.2)
```

forcing `sin(theta)^2=R^(5/3)` requires

```text
c_23(R)
 = (1-R) R^(1/3) sqrt(1-R^(5/3))/(1-2R^(5/3)).          (7.3)
```

Thus the desired exponent reappears as a new coefficient/source law. A
constant order-one `c_23` instead gives `theta` proportional to `R^(1/2)` as
`R` tends to zero, not `R^(5/6)`. Allowing both sectors adds more free
coefficients and relative phases rather than selecting (1.1).

The exact NNI and Schur identities elsewhere in the repository remain useful
construction tools, but they do not supply the missing selector and are not
consumed as dependencies here.

## 8. Exact boundary and remaining target

Established here:

1. fixed spectra plus the residual-`Z_2` normal form do not force alignment;
2. spectra plus Jacobi/NNI sparsity do not force alignment;
3. natural separable spectral actions do not force a mass-dependent interior
   overlap;
4. an exact target-equivalent rank-`(3,5)` positive-volume representation that
   would force the desired law if all carrier, block-weight, and action
   dictionaries were physically selected.

Still open:

1. framework derivation and physical typing of the full quark mass pair;
2. a theorem physically composing the six-state and generation carriers;
3. a source/action theorem selecting the asymmetric rank-`(3,5)` tensor lift;
4. a theorem selecting the unit `t` and inverse-`R` block-weight dictionary;
5. a theorem identifying positive-volume neutrality as the physical quark
   alignment principle;
6. all other mass, phase, running, and empirical-comparison gates.

This is an exact support/boundary theorem and route-pruning result. It is not a
derivation of the physical five-sixths law and does not permit retained-grade
proposal language.

## 9. Verification

Run:

```bash
python3 scripts/frontier_ckm_composite_positive_volume_alignment_source_action_boundary.py
```

The runner checks the exact residual-`Z_2` orbit, endpoint countermodels,
projector ranks, determinant factorization, both conditional actions, general
rank law, natural-action falsifiers, NNI coefficient identity, and source-note
claim firewalls with symbolic or rational algebra only.
