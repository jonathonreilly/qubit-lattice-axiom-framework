# Gauge Wilson SU(3) All-Weight Positive-Coefficient Formal Bridge

**Date:** 2026-06-07 (post-audit source repair 2026-07-16)
**Claim type:** positive_theorem
**Claim scope:** two exact statements on the standard finite-dimensional
`SU(3)` representation and normalized-Haar surfaces:

1. For every `beta > 0` and every dominant weight `(p,q)`, the one-link
   Wilson class function
   `w_beta(U) = exp[(beta/6)(chi_(1,0)(U) + chi_(0,1)(U))]`
   has strictly positive character coefficient `c_(p,q)(beta)`, and the
   normalized convolution eigenvalue
   `a_(p,q)(beta) = c_(p,q)(beta)/(d_(p,q)c_(0,0)(beta))`
   is strictly positive.
2. Any all-weight scalar sequence `(z_(p,q))` gives a compatible family of
   finite central character polynomials whose ordinary Haar convolutions
   stabilize on every finite-character test vector to
   `chi_(p,q) -> z_(p,q) chi_(p,q)`.

The second statement is algebraic-dual/finite-test-vector only. It does not
assert an all-weight `L^2` class function, a continuous class function, a
measure, a positive distribution, or a bounded operator on a completed
Hilbert space.

**Primary runner:**
[`scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py`](../scripts/audit_companion_gauge_wilson_su3_all_weight_positive_coefficient_formal_bridge_2026_06_07.py)

**Status boundary:** audit status is pipeline-derived. This source repair does
not write or predict an audit verdict.

## 1. Notation

Let

```text
G = SU(3),
E = C^3 = V_(1,0),
E* = V_(0,1),
W = E direct_sum E*,
t = beta/6.
```

Here `E*` is the contragredient representation; for `SU(3)` it is the
antifundamental `3bar`. Let `dU` be normalized Haar probability measure.
For a dominant weight `(p,q)`, write

```text
lambda_(p,q) = p omega_1 + q omega_2,
d_(p,q) = (p+1)(q+1)(p+q+2)/2.
```

Define the tensor-power multiplicity

```text
m_(p,q)(n) = dim Hom_G(V_(p,q), W^(tensor n)).
```

Finite-dimensional complete reducibility makes this a non-negative integer,
and

```text
chi_W(U)^n
  = chi_(W^(tensor n))(U)
  = sum_(r,s) m_(r,s)(n) chi_(r,s)(U),                         (1)
```

where the sum is finite for each fixed `n`.

## 2. Explicit SU(3) Highest-Weight Occurrence

This section proves the contested occurrence directly.

Work with the complexified Lie algebra `sl_3(C)`. Let
`e_1,e_2,e_3` be the standard basis of `E`, with dual basis
`e^1,e^2,e^3`. Choose the standard upper-triangular positive-root
operators

```text
E_12, E_23, E_13.
```

For a traceless diagonal matrix
`H = diag(h_1,h_2,h_3)`, the fundamental weights in this convention satisfy

```text
omega_1(H) = h_1,
omega_2(H) = h_1 + h_2 = -h_3.
```

Therefore

```text
H e_1 = omega_1(H) e_1,
H e^3 = -h_3 e^3 = omega_2(H) e^3.                           (2)
```

The dual action is `(X phi)(v) = -phi(Xv)`. Direct calculation gives

```text
E_12 e_1 = E_23 e_1 = E_13 e_1 = 0,
E_12 e^3 = E_23 e^3 = E_13 e^3 = 0.                         (3)
```

For example, `E_23 E` has image in `span(e_2)`, which `e^3` annihilates,
and similarly for `E_12` and `E_13`.

For arbitrary `p,q >= 0`, consider the nonzero tensor

```text
v_(p,q)
  = e_1^(tensor p) tensor (e^3)^(tensor q)
  in E^(tensor p) tensor (E*)^(tensor q).                    (4)
```

The Lie-algebra action on a tensor product is the sum of the actions on its
factors. Equations `(2)` and `(3)` therefore imply

```text
weight(v_(p,q)) = p omega_1 + q omega_2,
E_12 v_(p,q) = E_23 v_(p,q) = E_13 v_(p,q) = 0.              (5)
```

Thus `v_(p,q)` is an explicit highest-weight vector of dominant weight
`(p,q)`. It is symmetric separately in its `E` and `E*` factors, so it also
lies in

```text
Sym^p(E) tensor Sym^q(E*).
```

To identify the occurring irreducible without assuming the Cartan-component
claim, decompose the finite-dimensional unitary `SU(3)` representation
`E^(tensor p) tensor (E*)^(tensor q)` into irreducibles. Project
`v_(p,q)` to those summands. Each projection has the same weight and is killed
by all positive-root operators. In an irreducible finite-dimensional
`SU(3)` module, the common kernel of the positive-root operators is its
one-dimensional highest-weight line. Hence every nonzero projection is in an
irrep whose highest weight is exactly `p omega_1 + q omega_2`. At least one
projection is nonzero because `v_(p,q)` is nonzero. By the classification of
finite-dimensional irreducibles by dominant highest weight, that summand is
`V_(p,q)`.

Finally,

```text
E^(tensor p) tensor (E*)^(tensor q)
```

is one direct-sum word inside
`(E direct_sum E*)^(tensor (p+q))`. Consequently

```text
m_(p,q)(p+q) >= 1                                            (6)
```

for every dominant weight `(p,q)`.

This proves only the occurrence needed here. It does not claim that all of
`Sym^p(E) tensor Sym^q(E*)` is irreducible.

### Elementary representation facts: proved versus used

The note proves explicitly:

- the weights of `e_1` and `e^3`;
- their annihilation by the three positive-root matrices;
- weight additivity and positive-root annihilation for the tensor
  `v_(p,q)`;
- the embedding of its tensor word into `W^(tensor (p+q))`.

The note uses these standard finite-dimensional facts:

- unitary representations of compact `SU(3)` are completely reducible;
- the coordinate projections of a `G`-invariant irreducible direct-sum
  decomposition are `G`-equivariant;
- finite-dimensional irreducible `SU(3)` representations are classified by
  dominant highest weight;
- in an irreducible, the common positive-root kernel is the highest-weight
  line;
- Schur's lemma identifies
  `dim Hom_G(V_(p,q),W^(tensor n))` with the multiplicity of `V_(p,q)`;
- characters multiply under tensor products and add under direct sums;
- the `SU(3)` Weyl dimension formula displayed above;
- for a unitary representation, `|chi(U)| <= dim(V)`;
- normalized-Haar matrix-element Schur orthogonality;
- the two explicit `SU(3)` Pieri rules used by the finite runner recurrence.

The first four used facts identify the explicitly constructed vector with an
occurring copy of `V_(p,q)`; they do not assume the occurrence itself.
The Pieri rules are not used to prove the all-weight theorem; they are the
standard exact recurrence input for the independent finite executable
certificate.

## 3. Legitimate Character-Coefficient Extraction

For every real `beta` and every `U in SU(3)`,

```text
|chi_W(U)| <= dim(W) = 6.
```

Hence the exponential series obeys the uniform absolute majorant

```text
sum_(n>=0) |t|^n |chi_W(U)|^n / n!
  <= sum_(n>=0) (6|t|)^n/n!
  = exp(|beta|).                                             (7)
```

The Weierstrass M-test gives uniform and absolute convergence on compact
`SU(3)`:

```text
w_beta(U)
  = exp[t chi_W(U)]
  = sum_(n>=0) t^n chi_W(U)^n/n!.                            (8)
```

Fix `(p,q)`. Since `|chi_(p,q)(U)| <= d_(p,q)`, the coefficient integrands
also have an absolutely summable majorant:

```text
sum_(n>=0) integral_G
  |t^n chi_W(U)^n conj(chi_(p,q)(U))/n!| dU
  <= d_(p,q) exp(|beta|).                                   (9)
```

It is therefore legitimate to integrate the series term by term. With the
standard character coefficient

```text
c_(p,q)(beta)
  = integral_G w_beta(U) conj(chi_(p,q)(U)) dU,
```

equations `(1)`, `(8)`, normalized-Haar character orthogonality, and `(9)`
give

```text
c_(p,q)(beta)
  = sum_(n>=0) (beta/6)^n m_(p,q)(n)/n!.                    (10)
```

For `beta >= 0`, Tonelli's theorem for non-negative series and the
representation-dimension identity

```text
sum_(p,q) m_(p,q)(n) d_(p,q) = dim(W^(tensor n)) = 6^n
```

also gives

```text
sum_(p,q) c_(p,q)(beta) d_(p,q) = exp(beta).                (10a)
```

Thus `sum_(p,q) c_(p,q)(beta) chi_(p,q)` is itself uniformly and
absolutely convergent, because
`|chi_(p,q)(U)| <= d_(p,q)`. This justifies using the actual Wilson
character series in the ordinary convolution calculation below, independently
of the formal arbitrary-sequence construction.

For `beta > 0`, every summand in `(10)` is non-negative, and `(6)` supplies
the strictly positive term

```text
(beta/6)^(p+q) m_(p,q)(p+q)/(p+q)! > 0.
```

Thus

```text
c_(p,q)(beta) > 0
```

for every dominant `(p,q)` when `beta > 0`. The trivial coefficient also
satisfies `c_(0,0)(beta) >= 1` because of the `n=0` term.

The boundary is separate:

```text
c_(0,0)(0) = 1,
c_(p,q)(0) = 0 for (p,q) != (0,0).                         (11)
```

No strict all-weight positivity is claimed at `beta=0`.

## 4. Derived Convolution Normalization

The diagonal rule is derived here from the finite Haar convolution, not taken
as its definition.

Let `F` be a finite set of dominant weights and let

```text
Z_F(W) = sum_(lambda in F) d_lambda z_lambda chi_lambda(W).
```

For irreducible unitary matrix representations `D^lambda,D^mu`, define

```text
I_(lambda,mu)(V)
  = integral_G chi_lambda(VW^(-1)) chi_mu(W) dW.
```

Expanding the two traces gives

```text
chi_lambda(VW^(-1))
  = sum_(a,b) D^lambda(V)_(a b)
      conj(D^lambda(W)_(a b)),

chi_mu(W) = sum_c D^mu(W)_(c c).
```

Matrix-element Schur orthogonality then contracts all indices:

```text
I_(lambda,mu)(V)
  = sum_(a,b,c) D^lambda(V)_(a b)
      delta_(lambda,mu) delta_(a,c) delta_(b,c)/d_mu
  = delta_(lambda,mu) chi_mu(V)/d_mu.                       (12)
```

Therefore ordinary convolution by the finite polynomial gives

```text
(C_(Z_F) chi_mu)(V)
  = sum_(lambda in F) d_lambda z_lambda I_(lambda,mu)(V)
  = z_mu chi_mu(V)                                          (13)
```

whenever `mu in F`. The factor `d_lambda` in `Z_F` cancels the
`1/d_mu` produced by the Schur contraction only on the surviving
`lambda=mu` branch.

Now let

```text
C_fin = direct_sum_lambda C chi_lambda.
```

Let `chi_lambda^vee` be its algebraic dual basis,
`chi_lambda^vee(chi_mu)=delta_(lambda,mu)`. The all-weight sequence defines
the algebraic-dual element

```text
Z_z = sum_lambda d_lambda z_lambda chi_lambda^vee in C_fin^*,
```

where the displayed sum is formal but its evaluation on every element of
`C_fin` is finite. The finite polynomial `Z_F` realizes the same coordinates
on tests supported in `F`.

For a finite test vector `f = sum_(mu in S) f_mu chi_mu`, every finite
`F` containing `S` gives, by the ordinary finite convolution just derived,

```text
C_(Z_F) f = sum_(mu in S) z_mu f_mu chi_mu.                  (14)
```

The right side is unchanged when `F` is enlarged. The formal all-weight
object `Z_z` is this compatible family of finite central polynomials, and its
action on `C_fin` is the stabilized value `(14)`. Thus the all-weight
coefficientwise action is an output of the finite Schur/Peter-Weyl
contraction, not a definition standing in for that contraction.

Applying `(12)` to the actual Wilson class function
`w_beta = sum_lambda c_lambda(beta) chi_lambda` gives

```text
C_(w_beta) chi_(p,q)
  = c_(p,q)(beta)/d_(p,q) chi_(p,q).
```

Dividing by the positive trivial-channel eigenvalue `c_(0,0)(beta)` yields

```text
a_(p,q)(beta)
  = c_(p,q)(beta)/(d_(p,q)c_(0,0)(beta)) > 0                (15)
```

for every `(p,q)` and every `beta > 0`.

The matrix-index calculation `(12)` is the dimension-generic contraction
used by the landed
`SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM` block; it is
inlined here because the present conclusion is all-weight on finite tests,
whereas that block's durable numerical packet is finite.

## 5. Exact Scope Boundary

The compatible family `(Z_F)` and stabilized action `(14)` require no
summability of `(z_lambda)`, because each test vector has finite support.
They do not provide:

- an `L^2` or continuous all-weight class function;
- a countably additive or positive measure;
- continuity of the formal functional in a completed topology;
- a bounded, compact, trace-class, or positive operator on a Hilbert-space
  completion.

Any such upgrade requires a separate decay or summability theorem.

## 6. Direct Consumers And Literal Pins

The current-main direct source consumers were inspected. At this repair
snapshot:

- the residual-environment all-weight convolution note consumes only the
  strict nonzero Wilson coefficient and the finite-test formal convolution
  dictionary;
- the native positive-class theta note consumes only the strict Wilson
  coefficient/eigenvalue positivity for `beta > 0`.

Both statements remain within the repaired scope. Because the
residual-environment note belongs to a separately changing source-sector
block, its downstream prose is not an executable premise of this source
theorem or its primary runner. No downstream source-sector identity,
environment coefficient, `beta=6` value, reflection-positivity upgrade, or
completed-operator statement is supplied here.

## 7. Forbidden Imports Check

- No observed value, fitted selector, explicit unit convention, or
  literature numerical comparator is used.
- No framework axiom or primitive is introduced.
- The proof uses only the displayed finite-dimensional `SU(3)` matrices,
  standard compact-group complete reducibility/highest-weight facts, and
  normalized-Haar Schur orthogonality.
- No finite-slab pure-gauge reflection-positivity theorem is imported; it is
  not needed for this one-link coefficient and finite-test convolution
  theorem.

## 8. Validation

The companion runner:

1. computes the exact multiplicities of
   `(3 direct_sum 3bar)^(tensor n)` recursively through tensor level `16`,
   retaining the full reachable support at every level;
2. certifies every weight in the declared box `B_8` by scanning for its first
   nonzero computed multiplicity rather than assigning a witness length;
3. checks exact dimension conservation
   `sum_(p,q) m_(p,q)(n)d_(p,q)=6^n` at every level and the local Pieri
   dimension identities;
4. independently reconstructs the tensor-power decompositions by exact
   Jacobi-Trudi character algebra through level `8` and by direct
   Gelfand-Tsetlin torus-character enumeration through level `6`;
5. checks the `beta=0` boundary and exact positive lower monomials at
   `beta=1`;
6. reproduces the matrix-index Schur contraction and dimension cancellation
   on a finite character packet before applying arbitrary rational
   coefficients;
7. checks stabilization under enlargement of the finite convolution packet;
8. rejects missing-Pieri-branch, fundamental/antifundamental-swap,
   hard-coded-unit-multiplicity, missing-`1/d`, missing-`d_lambda`, and
   coefficient-only convolution mutants, with the recurrence mutants also
   required to disagree with both independent character decompositions;
9. checks source-note scope markers while leaving the separately changing
   downstream consumer prose outside the executable certificate.

Its recurrence is the explicit pair

```text
V_(a,b) tensor 3
  = V_(a+1,b)
    direct_sum [a>0] V_(a-1,b+1)
    direct_sum [b>0] V_(a,b-1),

V_(a,b) tensor 3bar
  = V_(a,b+1)
    direct_sum [b>0] V_(a+1,b-1)
    direct_sum [a>0] V_(a-1,b).
```

Starting from `m_(0,0)(0)=1`, it applies both rules at every step and stores
the resulting integer multiplicity dictionary without a weight cutoff. The
declared `B_8` is only the set on which the first-occurrence certificate is
reported; it is not a truncation of the recurrence.

The cache records the exact final pass/fail count.
