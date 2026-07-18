# SU(3) Character Diagonal Convolution Equivalence Narrow Theorem

**Date:** 2026-05-10
**Type:** positive_theorem
**Claim scope:** the input surface is the finite `B_4` `SU(3)` character
basis, normalized Haar probability measure, an abstract real nonnegative
swap-symmetric sequence `rho_(p,q)` with `rho_(0,0) = 1`, and standard
compact-group representation algebra. The output surface is T1 Schur
orthogonality, T2 equality of normalized convolution and diagonal action on
`V_4`, T3 coefficient uniqueness, and T4 positivity, self-adjointness, and
swap symmetry.

The parent Wilson-environment program is a separate coefficient-source
problem. Once a physical coefficient sequence is supplied with its own
authority and matches this input signature, this theorem supplies the
algebraic convolution/diagonal equivalence on `V_4`.

**Runner:** [`scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py`](./../scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py)

## Statement

Fix `N = 4` and let `B_4 = {(p, q) : 0 <= p, q <= 4}` be the 25-element
finite set of dominant `SU(3)` weights in the packet. For each
`(p, q) in B_4` let `chi_(p,q)` denote the irreducible `SU(3)` character of
highest weight `(p, q)`, and let

```text
d_(p,q) = (p + 1) (q + 1) (p + q + 2) / 2                                  (1)
```

be the irrep dimension. Let `(rho_(p,q))_(p,q in B_4)` be an abstract real
sequence with

- `rho_(p,q) >= 0` (non-negativity),
- `rho_(p,q) = rho_(q,p)` (conjugation symmetry under irrep complex conjugation `(p,q) <-> (q,p)`),
- `rho_(0,0) = 1` (normalization).

Define on the finite character-basis truncation
`V_4 = span{chi_(p,q) : (p,q) in B_4}`:

- the **diagonal operator** `R: V_4 -> V_4`,
  ```text
  R chi_(p,q) = rho_(p,q) chi_(p,q);                                       (2)
  ```
- the **central class function**
  ```text
  Z(W) = sum_(p,q in B_4) d_(p,q) rho_(p,q) chi_(p,q)(W);                  (3)
  ```
- the **normalized convolution operator** `C_{Z/Z_(0,0)}: V_4 -> V_4`,
  ```text
  (C_{Z/Z_(0,0)} f)(V)
        =  integral_{SU(3)} (Z(V W^{-1}) / Z_(0,0)) f(W) dW,               (4)
  ```
  where `dW` is normalized Haar probability measure
  (`integral_{SU(3)} dW = 1`) and
  `Z_(0,0) = d_(0,0) rho_(0,0) = 1 * 1 = 1`, so on `V_4` this reduces to
  convolution by `Z` itself.

**Conclusion (T1) (Schur orthogonality on the finite truncation).** For all
`(p, q), (p', q') in B_4`,

```text
integral_{SU(3)} chi_(p,q)(W) conj(chi_(p',q')(W)) dW
   =  delta_{(p,q), (p',q')}.                                              (5)
```

Equivalently, since `chi_(p',q')(W^{-1}) = conj(chi_(p',q')(W))` on
`SU(3)` (the contragredient irrep of `(p', q')` is `(q', p')`), this is
the standard inverse-character orthogonality relation
`int chi_(p,q)(W) chi_(p',q')(W^{-1}) dW = delta_{(p,q),(p',q')}`.

**Conclusion (T2) (diagonal action of normalized convolution).** The
normalized convolution operator `C_{Z/Z_(0,0)}` acts on each character by

```text
C_{Z/Z_(0,0)} chi_(p,q)  =  rho_(p,q) chi_(p,q),                           (6)
```

i.e. `C_{Z/Z_(0,0)} = R` as endomorphisms of `V_4`.

**Conclusion (T3) (uniqueness of coefficient sequence).** Two abstract
coefficient sequences `(rho^(1)_(p,q))` and `(rho^(2)_(p,q))` over `B_4`
give the same diagonal operator `R` on `V_4` iff
`rho^(1)_(p,q) = rho^(2)_(p,q)` for every `(p, q) in B_4`. Equivalently,
`R` determines its character coefficients uniquely; the algebraic
bijection `R <-> Z/Z_(0,0) <-> (rho_(p,q))` over `B_4` is one-to-one.

**Conclusion (T4) (positivity and Hermitian/conjugation symmetry of `R`).**
Under the abstract hypotheses on `(rho_(p,q))`, the operator `R` on `V_4`
is:

- positive (each eigenvalue `rho_(p,q) >= 0`),
- self-adjoint (diagonal in the Schur-orthonormal character basis),
- conjugation-symmetric: it commutes with the involution
  `swap: chi_(p,q) -> chi_(q,p)` on `V_4`.

The condition `rho_(0,0) = 1` is used only to fix the trivial-channel
normalization `Z_(0,0) = 1` in `(T2)`. Conclusion `(T4)` uses the real,
nonnegative, swap-symmetric properties of the sequence.

## Proof

`(T1)` This is the Schur character orthogonality relation for
irreducible characters of a compact group applied to `SU(3)`. For any
irreducible unitary representations `pi_(p,q)` and `pi_(p',q')` of
`SU(3)`, the Peter-Weyl theorem gives the orthogonality

```text
integral_{SU(3)} pi_(p,q)(W)_(ij) conj(pi_(p',q')(W)_(kl)) dW
   =  delta_{(p,q),(p',q')} delta_{ik} delta_{jl} / d_(p,q).               (7)
```

Tracing over `i = j` and `k = l` and summing,

```text
int chi_(p,q)(W) conj(chi_(p',q')(W)) dW
   =  sum_{i, k} delta_{(p,q),(p',q')} delta_{ik} delta_{ik} / d_(p,q)
   =  (delta_{(p,q),(p',q')} / d_(p,q)) * d_(p,q)
   =  delta_{(p,q),(p',q')},
```

which is `(5)`. The identity
`chi_(p,q)(W^{-1}) = conj(chi_(p,q)(W)) = chi_(q,p)(W)` is the standard
identity for compact Lie groups (`W^{-1}` lies in the conjugacy class
inverse to that of `W`, and the contragredient irrep of `(p,q)` is
`(q,p)`); it lets us rewrite the integrand in inverse-element form when
needed for `(9)` below.

`(T2)` Write `lambda = (p,q)`, `mu = (p',q')`, and let
`D^lambda`, `D^mu` be unitary irreducible representation matrices.
By `(3)`, `(4)`, and linearity,

```text
(C_Z chi_mu)(V)
   = integral_{SU(3)} Z(V W^{-1}) chi_mu(W) dW
   = sum_(lambda in B_4) d_lambda rho_lambda
       integral chi_lambda(V W^{-1}) chi_mu(W) dW.                         (8)
```

The inverse and conjugation convention is:

```text
D^lambda(V W^{-1})
   = D^lambda(V) D^lambda(W)^{-1}
   = D^lambda(V) D^lambda(W)^dagger,

chi_lambda(V W^{-1})
   = sum_(a,b) D^lambda(V)_(a b) conj(D^lambda(W)_(a b)),

chi_mu(W) = sum_c D^mu(W)_(c c).                                          (9)
```

Here `W^{-1}` creates the conjugated matrix element in the first character,
while the target character `chi_mu(W)` appears in its direct form. Reordering
`(7)` gives the precise matrix-element pairing

```text
integral conj(D^lambda(W)_(a b)) D^mu(W)_(c d) dW
   = delta_(lambda,mu) delta_(a,c) delta_(b,d) / d_mu.                     (10)
```

Set `d = c`, insert `(9)`, and contract every index:

```text
I_(lambda,mu)(V)
  := integral chi_lambda(V W^{-1}) chi_mu(W) dW

   = sum_(a,b,c) D^lambda(V)_(a b)
       integral conj(D^lambda(W)_(a b)) D^mu(W)_(c c) dW

   = delta_(lambda,mu) / d_mu
       sum_(a,b,c) D^lambda(V)_(a b) delta_(a,c) delta_(b,c)

   = delta_(lambda,mu) / d_mu sum_c D^lambda(V)_(c c)

   = delta_(lambda,mu) chi_mu(V) / d_mu.                                  (11)
```

The last line uses `lambda = mu` only on the surviving Schur-delta branch.
Thus the trace and the factor `1/d_mu` are outputs of the matrix-index
contraction itself.
The indexed calculation is dimension-generic, but the durable claim in this
note is restricted to the fixed `B_4` packet.

The inverse/conjugation choices are essential. If `W^{-1}` is replaced by
`W`, the Haar substitution `U = W^{-1}` changes the target to
`chi_mu(U^{-1}) = chi_(mu^*)(U)`, where `mu^* = (q',p')`. Likewise,
replacing `chi_mu(W)` by its complex conjugate directly inserts
`chi_(mu^*)(W)`. Either mutation therefore produces the dual-irrep action
`rho_(mu^*) chi_(mu^*)(V)`, which generally differs from
`rho_mu chi_mu(V)`. The runner tests both mutations on the complex
fundamental character at a `V` for which
`chi_(1,0)(V) != chi_(0,1)(V)`.

Substituting `(11)` into the full finite sum `(8)` gives the dimension
cancellation explicitly:

```text
(C_Z chi_mu)(V)
   = sum_(lambda in B_4)
       d_lambda rho_lambda delta_(lambda,mu) chi_mu(V) / d_mu
   = d_mu rho_mu chi_mu(V) / d_mu
   = rho_mu chi_mu(V).                                                     (12)
```

Because `Z_(0,0) = 1`, this is also `C_{Z/Z_(0,0)} chi_mu`. It is exactly
`R chi_mu` evaluated at `V`. Hence
`C_{Z/Z_(0,0)} = R` on the finite truncation `V_4`.

`(T3)` Because `{chi_(p,q) : (p,q) in B_4}` is a linearly independent
basis of `V_4` (Schur orthogonality `(5)` makes them mutually
orthogonal, hence linearly independent), the action of `R` on this
basis determines its diagonal entries uniquely. So
`R^(1) = R^(2)` implies `rho^(1)_(p,q) = rho^(2)_(p,q)` for every
`(p, q) in B_4`. The converse is immediate from `(2)`.

`(T4)` This conclusion is logically separate from the convolution
contraction above. Each `rho_(p,q) >= 0` by hypothesis, so `R` has non-negative
eigenvalues. In the Schur-orthonormal character basis `{chi_(p,q)}`,
`R` is diagonal with real entries, hence self-adjoint.
Conjugation symmetry
`swap chi_(p,q) = chi_(q,p)` and `rho_(p,q) = rho_(q,p)` give
`R swap chi_(p,q) = R chi_(q,p) = rho_(q,p) chi_(q,p)
= rho_(p,q) chi_(q,p) = swap rho_(p,q) chi_(p,q) = swap R chi_(p,q)`,
so `R` commutes with `swap`. ∎

## Input and output surface

The complete theorem input is:

- the 25 characters indexed by `B_4` and their span `V_4`;
- normalized Haar probability measure on `SU(3)`;
- the abstract real sequence `(rho_(p,q))` with nonnegative entries,
  swap symmetry, and trivial-channel normalization `rho_(0,0) = 1`;
- standard compact-group representation algebra, including the exact
  `SU(3)` dimension formula and matrix-element Schur orthogonality.

From exactly that input, the theorem returns:

- `(T1)` Schur character orthogonality on `B_4`;
- `(T2)` `C_{Z/Z_(0,0)} = R` on `V_4`;
- `(T3)` uniqueness of the diagonal coefficient sequence;
- `(T4)` positivity, self-adjointness, and swap symmetry of `R`.

## Division of labor with the parent plaquette program

The parent Wilson-environment program owns the source problem for a physical
coefficient sequence, including its Wilson configuration-integral provenance,
normalization, and domain. This theorem owns the algebraic map from any
sequence matching the input signature above to the corresponding normalized
central convolution on `V_4`.

A physical application therefore has a two-authority type signature: the
coefficient-source result supplies `(rho_(p,q))`, and this theorem supplies
the convolution/diagonal equivalence after that typed input is present. The
bounded coefficient companion
`GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`
supplies only one finite stipulated-integral coefficient packet. It provides
no physical-surface, environment, or tensor-transfer identification; any such
application requires its own authority in addition to this abstract theorem.

## Cited dependencies

Repository-source dependency set: empty. The mathematical authority surface
is normalized Haar probability measure, unitary irreducible representations,
Peter-Weyl theory, and matrix-element Schur orthogonality for compact groups.
The interface with the parent Wilson program requires a coefficient sequence
carrying its own physical authority.

## Input-authority check

The complete load-bearing input roster is the finite `B_4` character packet,
normalized Haar measure, the abstract normalized nonnegative swap-symmetric
sequence, and standard compact-group representation algebra. Numerical data,
physical coefficient provenance, environment compression, and Wilson
configuration-integral construction retain their respective source
authorities in the parent program.

## Validation

Primary runner: [`scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py`](./../scripts/frontier_su3_character_diagonal_convolution_equivalence_narrow.py)
verifies, on the finite `N = 4` truncation (`B_4 = {(p,q): 0 <= p,q <= 4}`):

1. Schur orthogonality `(5)` to machine precision via Weyl integration
   on the SU(3) Cartan torus: `<chi_(p,q), chi_(p',q')>_Haar
   = delta_((p,q),(p',q'))` for all sampled pairs in `B_4`.
2. Exact matrix-element Conclusion `(T2)`: the runner expands
   `chi_lambda(V W^{-1}) chi_mu(W)` into the generic `(a,b,c)` matrix-index
   sum `(9)` and mechanically contracts `(10)`. It checks an inequivalent
   fundamental/antifundamental pair, every unequal pair in `B_4`, and every
   same-irrep pair in `B_4`, obtaining exactly
   `delta_(lambda,mu) Tr D^mu(V)/d_mu`. Before applying any `rho`, it
   verifies that multiplication by `d_lambda` gives the exact `25 x 25`
   identity, then checks the full finite sum on every target in `B_4`.
3. Conclusion `(T3)` uniqueness: two distinct coefficient sequences
   (one positive symmetric, one with one entry perturbed) give two
   distinct diagonal operators with at least one different eigenvalue.
4. Conclusion `(T4)` positivity/Hermiticity/swap-symmetry: under the
   abstract hypotheses, `R` is non-negative definite, self-adjoint
   in the Schur-orthonormal character basis, and commutes with the
   conjugation swap involution.
5. Concrete instance with an abstract rational positive symmetric
   sequence, for example `(rho_(1,0), rho_(1,1), rho_(2,0)) =
   (2/5, 1/7, 1/8)`,
   and confirmation that
   `C_{Z/Z_(0,0)} chi_(p,q) = rho_(p,q) chi_(p,q)` exactly on every
   basis character.
6. Concrete instance with `(rho_(p,q)) = (1, 0, 0, ..., 0)` (trivial
   sequence) and confirmation that `C_{Z/Z_(0,0)}` collapses to the
   trivial projection.
7. Independent numerical support: deterministic Ginibre-QR
   Haar-random `SU(3)` matrices and explicit trace formulas for the trivial,
   fundamental, antifundamental, adjoint, symmetric square, conjugate
   symmetric square, symmetric cube, and conjugate symmetric cube
   characters reproduce `C_Z chi_mu(V) = rho_mu chi_mu(V)` for three
   nontrivial `V` values and an abstract rational symmetric coefficient
   sequence. This Monte Carlo calculation supplies independent numerical
   support; the indexed Schur contraction supplies the exact proof.
8. Hostile controls that reject a missing `1/d_mu`, `W` in place of
   `W^{-1}`, conjugating the target character, and the lookup-only value
   `rho_mu` in place of the V-dependent value `rho_mu chi_mu(V)`.

Expected summary:

- `PASS=24 FAIL=0`
