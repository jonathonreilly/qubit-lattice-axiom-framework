# Fermion-Parity Grading on an Ordered Finite Occupation Space

**Date:** 2026-05-02
**Type:** positive_theorem
**Claim scope:** exact finite-dimensional theorem on a supplied ordered
`N`-mode occupation space, for `N >= 1`. The theorem constructs a concrete
CAR representation by Jordan-Wigner strings, proves its balanced `Z_2`
grading, and separates parity conservation from the strictly stronger
number-conservation condition when `N >= 2`.
**Runner:** `scripts/fermion_parity_z2_grading_check.py`
**Log:** `logs/runner-cache/fermion_parity_z2_grading_check.txt`

## Cited authorities (one hop)

None. The inputs below are definitions and elementary finite-dimensional
linear algebra. In particular, no framework theorem is used to select the
ordered occupation carrier or a dynamics on it.

## Definitions and hypotheses

Fix an integer `N >= 1` and the ordered Hilbert space

```text
H_N := (C^2)^(tensor N).
```

On one factor use the orthonormal basis

```text
|0> = (1,0)^T,   |1> = (0,1)^T,
```

and define

```text
b = |0><1|,       b^dagger = |1><0|,
n = b^dagger b = |1><1|,   Z = I - 2n = diag(1,-1).
```

The ordered occupation basis is

```text
|nu> := |nu_1> tensor ... tensor |nu_N>,   nu_x in {0,1}.
```

For modes `x = 1,...,N`, define the Jordan-Wigner operators

```text
a_x := Z^(tensor(x-1)) tensor b tensor I^(tensor(N-x)),
a_x^dagger := Z^(tensor(x-1)) tensor b^dagger tensor I^(tensor(N-x)).   (1)
```

Empty tensor products in (1) are omitted. The order of the factors is part of
the hypothesis. It is not selected by this theorem.

The one-mode relations `{b,b}=0`, `{b,b^dagger}=I`, and `Zb=-bZ`, together
with the strings in (1), give the canonical anticommutation relations (CAR):

```text
{a_x,a_y}=0,   {a_x^dagger,a_y^dagger}=0,
{a_x,a_y^dagger}=delta_xy I.                                      (2)
```

Moreover,

```text
n_x := a_x^dagger a_x
     = I^(tensor(x-1)) tensor n tensor I^(tensor(N-x)),
Q := sum_(x=1)^N n_x.                                               (3)
```

Thus `n_x |nu> = nu_x |nu>` and
`Q |nu> = |nu| |nu>`, where `|nu| := sum_x nu_x`.

Define the occupation-parity operator by spectral functional calculus:

```text
F := exp(i pi Q).                                                    (4)
```

Finally, for the dynamics statement only, let `H_dyn` be an arbitrary
self-adjoint operator on `H_N` and let `U(t) := exp(-it H_dyn)`.

## Theorem

Under the definitions above:

1. `F` is Hermitian and unitary, and `F^2 = I`.
2. Its exact product form is

   ```text
   F = Z tensor ... tensor Z.                                      (5)
   ```

3. Both eigenvalues occur. With

   ```text
   H_even := ker(F-I),   H_odd := ker(F+I),
   ```

   one has

   ```text
   H_N = H_even direct_sum H_odd,
   dim(H_even) = dim(H_odd) = 2^(N-1).                              (6)
   ```

4. Every ladder operator is odd:

   ```text
   F a_x F = -a_x,   F a_x^dagger F = -a_x^dagger.                 (7)
   ```

   More generally, a product of `k` ladder operators is multiplied by
   `(-1)^k` under conjugation by `F`. Consequently every sum of even
   monomials commutes with `F`. This is a sufficient structural test for
   parity evenness; it is not asserted here to be a number-conservation
   condition.

5. Parity is conserved for all real `t` exactly when

   ```text
   U(t)^dagger F U(t) = F for every t
       iff [H_dyn,F] = 0.                                          (8)
   ```

6. Number conservation is sufficient for parity conservation:

   ```text
   [H_dyn,Q] = 0  implies  [H_dyn,F] = 0.                           (9)
   ```

   The converse is false for every `N >= 2`. For `N=1`, however,
   `F=I-2Q`, so the two commutation conditions are equivalent.

7. The two commutants have different block structures. If
   `H_q := ker(Q-qI)`, then

   ```text
   {Q}' = direct_sum_(q=0)^N End(H_q),
   {F}' = End(H_even) direct_sum End(H_odd).                        (10)
   ```

   Hence `{Q}'` is a subalgebra of `{F}'`. It is a strict subalgebra for
   `N >= 2`, while the two are equal for `N=1`.

## Proof

### CAR and occupation operators

For `x=y`, the one-factor relations give (2). For `x<y`, the `Z` string in
`a_y` crosses the single `b` or `b^dagger` in `a_x` once. That crossing gives
one minus sign; all other tensor factors commute. This proves the cross-mode
relations in (2). Squaring the strings in `a_x^dagger a_x` gives (3), so the
occupation-basis action of every `n_x` and of `Q` follows exactly.

### Spectral and product forms of parity

Let `P_q` be the spectral projector of `Q` for eigenvalue `q`. Since
`q` is an integer,

```text
F = sum_(q=0)^N exp(i pi q) P_q
  = sum_(q=0)^N (-1)^q P_q.                                       (11)
```

Equation (11) makes `F` Hermitian, unitary, and involutive. On a basis vector,

```text
F|nu> = (-1)^|nu| |nu>
       = product_x (-1)^nu_x |nu>
       = (Z tensor ... tensor Z)|nu>,
```

which proves (5). The vacuum has parity `+1`, while a one-occupation state has
parity `-1`, so both eigenvalues occur for every `N>=1`.

Flipping the first bit is a bijection between even- and odd-weight binary
strings. Each class therefore has `2^(N-1)` elements, proving (6).

### Odd and even monomials

The factor `Z` at mode `x` anticommutes with the `b` or `b^dagger` there;
all other factors in (5) commute through the Jordan-Wigner string. Therefore
(7) holds. Conjugation is multiplicative, so a product of `k` ladder
operators acquires exactly `k` minus signs. In particular all bilinears,
including `a_x^dagger a_y` and every `n_x`, commute with `F`.

### Exact dynamics boundary

If `[H_dyn,F]=0`, every power of `H_dyn` commutes with `F`, hence so does
`U(t)`, and (8) follows. Conversely, if parity is conserved for every `t`,
differentiating at `t=0` gives

```text
0 = d/dt [U(t)^dagger F U(t)]_(t=0) = i[H_dyn,F].                  (12)
```

This proves the equivalence in (8). If `[H_dyn,Q]=0`, then `H_dyn` commutes
with every spectral projector `P_q` and therefore with the function of `Q` in
(11). This proves the one-way implication (9).

For the converse, first take `N=2` and define

```text
H_pair := |00><11| + |11><00|
        = a_1^dagger a_2^dagger + a_2 a_1.                         (13)
```

The order in the annihilation term in (13) is fixed by the convention (1);
with that order both displayed matrix elements have coefficient `+1`.
For larger `N`, tensor (13) with the identity on the remaining modes.
The operator is self-adjoint and contains two ladder operators in each term,
so `[H_pair,F]=0`. Directly,

```text
[Q,H_pair]
  = 2 a_1^dagger a_2^dagger - 2 a_2 a_1 != 0.                     (14)
```

Thus parity conservation does not imply number conservation when `N>=2`.
For `N=1`, (4) reduces to `F=I-2Q`, proving the stated exception.

Finally, an operator commutes with a diagonalizable operator exactly when it
has no matrix elements between distinct eigenspaces. Applying this once to
the `N+1` eigenspaces of `Q` and once to the two eigenspaces of `F` proves
(10). The inclusion follows because each `H_q` lies wholly in one parity
sector. Equation (13) witnesses strictness for `N>=2`. Equivalently, the
complex dimensions are

```text
dim {Q}' = sum_q binomial(N,q)^2 = binomial(2N,N),
dim {F}' = 2^(2N-1),
```

with equality only at `N=1`. This completes the proof. ∎

## What the theorem does not select

This theorem is conditional on the supplied ordered occupation space and its
Jordan-Wigner realization. It does not derive or select:

- a physical fermion carrier, fermion statistics, a spin-statistics bridge,
  graded locality, or a parity superselection rule;
- a physical interpretation of `Q` as particle number or a law conserving it;
- a Hamiltonian, transfer operator, time variable, or framework dynamics;
- spatial locality for the order-dependent Jordan-Wigner generators;
- a continuum or quantum-field-theory limit; or
- an identification of these formal modes with lattice sites, records,
  particles, tastes, generations, or observables.

A consumer that needs any such interpretation must cite a separate bridge.
The theorem supplies only the exact finite-dimensional CAR representation,
grading, commutant distinction, and conditional dynamics criterion stated
above.

```yaml
claim_type_author_hint: positive_theorem
claim_scope: "On a supplied ordered N-mode occupation space (C^2)^(tensor N), N>=1, the Jordan-Wigner operators realize CAR; Q=sum_x a_x^dagger a_x and F=exp(i*pi*Q)=tensor_x Z give a balanced Z_2 grading; parity is conserved for all t under a supplied self-adjoint H_dyn iff [H_dyn,F]=0; [H_dyn,Q]=0 implies [H_dyn,F]=0 but the converse fails for N>=2 by the exact pair Hamiltonian |00><11|+|11><00|; the theorem selects no physical carrier, statistics rule, superselection rule, locality law, or dynamics."
upstream_dependencies: []
mathematical_definitional_inputs:
  - finite-dimensional spectral functional calculus
  - ordered tensor-product occupation basis
  - Jordan-Wigner construction
```
