# Staggered + Wilson Supplied-Surface Determinant Positivity

**Date:** 2026-05-05 (original); 2026-05-28 (reframed as supplied-surface
linear algebra; superseded meta dependency removed).
**Claim type:** positive_theorem
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/frontier_staggered_wilson_det_positivity_bridge_2026_05_05.py`

## Claim

Given the following finite matrix surface:

- a balanced `eps` decomposition with equal `+` and `-` subspaces;
- an anti-Hermitian staggered-hop block

```text
M_KS = [[ 0,  K ],
        [ -K^dag, 0 ]],
```

- a supplied Wilson/mass diagonal surface

```text
M_W + m I = alpha I,          alpha = m + r d,       m > 0,
```

the supplied Dirac matrix

```text
M = M_KS + M_W + m I = [[ alpha I, K ],
                        [ -K^dag, alpha I ]]
```

has

```text
det(M) = product_i (alpha^2 + sigma_i^2) > 0,
```

where `sigma_i` are the singular values of `K`.

This is a finite-dimensional linear-algebra theorem about the supplied
matrix surface. It does **not** claim that `M_W = r d I` is forced by the
framework, by the Wilson lattice action, or by any retained convention. That
identification is out of scope.

## 2026-05-28 Audit Repair

The previous source mixed the correct determinant algebra with an unsupported
claim that the supplied symmetric-canonical Wilson surface was a framework
convention inherited from parent notes. The repair is to keep only the
standalone supplied-surface theorem:

- no load-bearing dependency on `MINIMAL_AXIOMS_2026-04-11.md`;
- no load-bearing dependency on the reflection-positivity parent row;
- no claim that the standard Wilson nearest-neighbour Laplacian is covered;
- no claim that the supplied surface repairs any broader Wilson-sector
  reflection-positivity theorem.

Downstream rows that need this exact supplied surface may cite this theorem.
Downstream rows that need a framework derivation of the Wilson surface must
wait for a separate retained authority.

## Proof

Let `K = U Sigma V^dag` be a singular-value decomposition, where
`Sigma = diag(sigma_i)` and each `sigma_i >= 0`. Conjugating `M` by
`diag(U,V)` gives

```text
M ~ [[ alpha I, Sigma ],
     [ -Sigma,  alpha I ]].
```

The matrix is a direct sum over `i` of two-by-two blocks

```text
B_i = [[ alpha, sigma_i ],
       [ -sigma_i, alpha ]].
```

Each block has determinant

```text
det(B_i) = alpha^2 + sigma_i^2.
```

Since `m > 0` and `r d >= 0` on the supplied surface, `alpha = m + r d > 0`.
Therefore every factor is positive and

```text
det(M) = product_i det(B_i) = product_i (alpha^2 + sigma_i^2) > 0.
```

## Runner Companion

The companion runner constructs finite staggered-hop matrices on small seeded
`SU(3)` link backgrounds, then **supplies** the diagonal Wilson/mass surface
`M_W + m I = alpha I`. It checks:

- balanced `eps` subspaces;
- zero diagonal `eps` blocks and lower-left block `-K^dag`;
- direct determinant sign and log magnitude;
- agreement with the closed form `product_i(alpha^2 + sigma_i^2)`.

The runner is support for the supplied matrix theorem. It is not evidence that
the supplied Wilson surface is framework-forced.

## Imports and Non-Claims

Imported standard mathematics:

- singular-value decomposition over complex matrices;
- determinant invariance under unitary conjugation;
- determinant of a two-by-two block.

This note does not claim:

- a framework derivation of a Wilson term;
- determinant positivity for the standard Wilson nearest-neighbour
  Laplacian;
- reflection positivity for the parent row;
- closure of any Wilson-sector sign problem;
- any new axiom or retained convention.

Historical/navigational references only, not load-bearing dependencies:

- `MINIMAL_AXIOMS_2026-04-11.md`;
- `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`.
