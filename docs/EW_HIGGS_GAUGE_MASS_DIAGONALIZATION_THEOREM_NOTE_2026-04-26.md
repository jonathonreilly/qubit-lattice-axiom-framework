# Defined C2 Quadratic-Form Diagonalization Theorem

**Date:** 2026-04-26; 2026-07-16 defined-algebra repair

**Type:** positive theorem
**Claim type:** positive_theorem

**Stable claim ID:**
`ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26`

**Historical-identifier notice:** the electroweak, Higgs, gauge, and mass words
in this file's stable path and claim ID are graph-continuity identifiers only.
They add no physical hypothesis or conclusion to the theorem below.

**Primary runner:**
`scripts/frontier_ew_higgs_gauge_mass_diagonalization.py`

## 1. Exact definitions

Let

```text
V = C^2
```

with its standard Hermitian inner product
`<x,y> = conjugate(x)^T y` and norm `||x||^2 = <x,x>`. Let
`v`, `g`, and `gY` be positive real scalars, and let
`W1`, `W2`, `W3`, and `B` range independently over `R`.

Define the displayed matrices and vector; they are data of this theorem:

```text
sigma1 = [[0,  1],       sigma2 = [[0, -i],
          [1,  0]],                [i,  0]],

sigma3 = [[1,  0],       I2 = [[1, 0],
          [0, -1]],             [0, 1]],

Ta = sigmaa / 2,         Y = I2 / 2,
h0 = (0, v/sqrt(2))^T.
```

Define the real-linear map `L : R^4 -> C^2` and its real quadratic form
`Q : R^4 -> R` by

```text
L(W1,W2,W3,B)
  = -i [g (W1 T1 + W2 T2 + W3 T3) + gY B Y] h0,

Q(W1,W2,W3,B) = ||L(W1,W2,W3,B)||^2.
```

No covariant derivative, field, action, or physical system is being defined
by this notation. `L` and `Q` are simply the displayed finite-dimensional
map and quadratic form.

For later compactness define

```text
G = sqrt(g^2 + gY^2),    c = g/G,    s = gY/G.
```

The positivity assumptions make `G`, `c`, and `s` unambiguous and nonzero.

## 2. Theorem

For the definitions above:

1. The matrix actions are

   ```text
   T1 h0 = ( v/(2 sqrt(2)), 0)^T,
   T2 h0 = (-i v/(2 sqrt(2)), 0)^T,
   T3 h0 = (0, -v/(2 sqrt(2)))^T,
   Y  h0 = (0,  v/(2 sqrt(2)))^T.
   ```

2. The map and quadratic form are

   ```text
   L = -i v/(2 sqrt(2))
       ( g(W1 - i W2), -g W3 + gY B )^T,

   Q = v^2/8 [g^2(W1^2 + W2^2) + (g W3 - gY B)^2].
   ```

3. Writing `x = (W1,W2,W3,B)^T`, the unique symmetric matrix `M` for
   which `Q = (1/2) x^T M x` is

   ```text
   M = v^2/4 [[g^2, 0,   0,      0],
              [0,   g^2, 0,      0],
              [0,   0,   g^2,   -g gY],
              [0,   0,  -g gY,   gY^2]].
   ```

   Thus the two-direction charged block is `(g^2 v^2/4) I2`. If

   ```text
   Wplus  = (W1 - i W2)/sqrt(2),
   Wminus = (W1 + i W2)/sqrt(2),
   ```

   then `Wplus Wminus = (W1^2+W2^2)/2` and the charged summand of
   `Q` is `(g^2 v^2/4) Wplus Wminus`.

4. The neutral block is

   ```text
   M0 = v^2/4 [[g^2,  -g gY],
               [-g gY, gY^2]].
   ```

   It has

   ```text
   det(M0) = 0,
   rank(M0) = 1,
   trace(M0) = v^2(g^2+gY^2)/4,
   characteristic polynomial = lambda
       [lambda - v^2(g^2+gY^2)/4].
   ```

   Its kernel is `span{(gY,g)^T}`. Its range and nonzero eigenspace are
   `span{(g,-gY)^T}`, with nonzero eigenvalue
   `v^2(g^2+gY^2)/4`.

5. The orthogonal change of coordinates

   ```text
   (Z)   [[c, -s], (W3)
   (A) =  [s,  c]] ( B)
   ```

   satisfies

   ```text
   R M0 R^T = diag(v^2(g^2+gY^2)/4, 0),
   Qneutral = v^2(g^2+gY^2) Z^2/8.
   ```

6. Inside `span_C{T3,Y}`, the full annihilator of `h0` is exactly

   ```text
   {alpha T3 + beta Y : (alpha T3 + beta Y)h0 = 0}
     = span_C{T3 + Y}.
   ```

   In particular, the defined endomorphism `T3+Y` kills `h0`.

7. The following are defined scalar readouts of this quadratic form:

   ```text
   MW2  := g^2 v^2/4,
   MZ2  := (g^2+gY^2) v^2/4,
   MA2  := 0,
   e    := g gY/G,
   rho  := MW2/(MZ2 c^2).
   ```

   They obey the exact identities

   ```text
   c^2+s^2 = 1,
   e = g s = gY c,
   1/e^2 = 1/g^2 + 1/gY^2,
   rho = 1.
   ```

The symbols `MW2`, `MZ2`, `MA2`, `e`, and `rho` are formal labels only.

## 3. Proof

Direct multiplication of each displayed matrix by `h0` gives item 1.
Substitution of those four vectors into the definition of `L` gives

```text
L = -i v/(2 sqrt(2))
    (g(W1-iW2), -gW3+gYB)^T.
```

Because all four coefficients are real, taking the standard Hermitian norm
gives item 2. The Hessian of the resulting quadratic polynomial, or
equivalently collecting its coefficients in `(1/2)x^T Mx`, gives the matrix
in item 3. The `Wplus Wminus` identity is direct multiplication.

For the neutral block, factor its scalar prefactor and observe

```text
[[g^2,  -g gY],       (g )
 [-g gY, gY^2]] =     (-gY) (g, -gY).
```

It is therefore a nonzero rank-one outer product. Its determinant, trace,
characteristic polynomial, kernel, range, and two eigenspaces follow
immediately, proving item 4. The two rows of `R` are the normalized nonzero
eigenvector and normalized kernel vector. Their orthonormality gives
`R R^T = I2`, and left/right multiplication gives the diagonal matrix and
the reconstructed neutral quadratic form in item 5.

For arbitrary complex `alpha` and `beta`, direct multiplication gives

```text
(alpha T3 + beta Y)h0
  = v/(2 sqrt(2)) (0, beta-alpha)^T.
```

Since `v>0`, this vanishes exactly when `alpha=beta`, proving item 6.
Finally, substituting the definitions of `G`, `c`, `s`, and the five scalar
labels proves every identity in item 7 by cancellation of positive nonzero
factors.

## 4. Exact formal scope

This theorem proves only identities among explicitly defined matrices,
vectors, a real-linear map, a real quadratic form, and scalar abbreviations.
It has no dependency on the framework's minimal axioms, primitive registry,
premise history, experimental values, physical carrier choices, or any
downstream claim status. No scalar potential or Hessian theorem is included;
a supplied polynomial potential is a separate problem and gives this claim
no additional authority.

The notation is intentionally compatible with older graph consumers, but
notation is not an identification. In particular, a downstream note may use
this result as finite-dimensional algebra only. Any physical interpretation
needs its own explicit premises and bridge theorem.

## 5. Non-identification firewall

Nothing here selects, derives, or identifies:

- an electroweak gauge group or any other gauge group;
- a physical Higgs carrier, its hypercharge, or any representation;
- a physical vacuum or vacuum expectation value;
- a covariant derivative, gauge field, connection, action, or dynamics;
- a particle mass, pole mass, gauge-boson mass, or mass-selection rule;
- a weak angle, electric charge, photon, `W`, or `Z` particle;
- custodial symmetry or custodial physics;
- a continuum theory, quantum field theory, or phenomenological model;
- a GUT normalization or any normalization selected by the framework;
- a physical observable, physical readout, or comparison with experiment.

The facts that `T3+Y` kills `h0`, that `M0` has a one-dimensional kernel,
and that the formal readouts satisfy `rho=1` are algebraic facts about the
definitions above. They are not claims of an unbroken physical generator,
a massless physical state, or a custodial relation.

## 6. Reproduction

Run exact symbolic verification with no floats, network, or external data:

```bash
python3 scripts/frontier_ew_higgs_gauge_mass_diagonalization.py
python3 scripts/frontier_ew_higgs_gauge_mass_diagonalization.py --mode independent
python3 scripts/frontier_ew_higgs_gauge_mass_diagonalization.py --mode hostile
python3 scripts/frontier_ew_higgs_gauge_mass_diagonalization.py --mode intentional-failure
```

The first three commands must exit `0`. Intentional-failure mode promotes
each installed mutation to a claimed identity and must exit `1`.
