# Finite Translation-Character Profiles and Projectors Theorem

**Date:** 2026-06-15
**Type:** positive_theorem
**Status:** source-note proposal awaiting independent audit; audit and effective
status are pipeline-owned.
**Primary runner:**
[`scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py`](../scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py)
**Cache:**
[`logs/runner-cache/flavor_carrier_momentum_type_from_translation_2026_06_15.txt`](../logs/runner-cache/flavor_carrier_momentum_type_from_translation_2026_06_15.txt)

The historical filename and claim ID remain unchanged for citation-graph
stability. They are not the reader-facing statement of the theorem.

## Purpose

This note records an exact finite construction on the supplied periodic
`2 x 2 x 2` cell. Its content is the translation-character basis, the uniform
position profiles of those characters, and the associated rank-one spectral
projectors. Every statement below is a positive equality or construction.

## Theorem

Let the sites be `n in {0,1}^3`, in lexicographic order, and let

```text
T_mu |n> = |n + e_mu mod 2>,                 mu in {x,y,z}.
```

For `k in Z_2^3`, define

```text
psi_k(n) = (-1)^(k.n) / sqrt(8),
P_k = |psi_k><psi_k|.
```

Then:

1. `T_x`, `T_y`, and `T_z` are commuting unitary permutation matrices.
2. The eight vectors `psi_k` form an orthonormal simultaneous eigenbasis,
   with `T_mu psi_k = (-1)^(k_mu) psi_k`.
3. The supplied subset
   `K_1 = {(1,0,0), (0,1,0), (0,0,1)}` contains three distinct joint
   characters. The `C_3[111]` coordinate cycle acts transitively on `K_1` and
   carries each `psi_k` to the correspondingly cycled character vector.
4. Every character has the exact position probability profile

   ```text
   (|psi_k(n)|^2)_n = (1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8).
   ```

5. For an arbitrary diagonal position operator
   `O = diag(w_000, w_001, ..., w_111)`, with symbolic weights,

   ```text
   <psi_k, O psi_k> = (1/8) sum_n w_n
   ```

   for every `k`, including each member of `K_1`.
6. The eight projectors are orthogonal idempotents resolving the identity:

   ```text
   P_k P_q = delta_(kq) P_k,       sum_k P_k = I_8.
   ```

   Their full expectation matrix is exactly

   ```text
   <psi_k, P_q psi_k> = delta_(kq).
   ```

   The `K_1 x K_1` submatrix is therefore exactly `I_3`.

## Exact construction

The runner builds the site permutations and character vectors with exact
SymPy arithmetic. Orthonormality follows from the finite character sum

```text
(1/8) sum_n (-1)^((k+q).n) = delta_(kq).
```

The uniform profile gives the symbolic diagonal expectation directly:

```text
sum_n w_n |psi_k(n)|^2 = (1/8) sum_n w_n.
```

Finally, the projector product and expectation formulas follow from
`<psi_k,psi_q> = delta_(kq)`. The runner evaluates all of these identities as
exact matrix or symbolic equalities and prints the full `8 x 8` Kronecker
matrix together with its supplied `3 x 3` submatrix.

## Authority limit

This theorem's authority ends at the displayed finite-cell constructions and
equalities. The subset `K_1` is supplied as an abstract three-character locus;
the theorem assigns it no physical selection or species meaning. Physical
generation-locus identification, staggered/Kawamoto-Smit chirality, Koide
basepoint or readout selection, and any actual flavor identification belong to
separate authority surfaces. The formulas here assign no physical carrier,
observable, or readout role to either basis.

The proof adds no axiom, approved primitive, selector, convention, imported
value, or physical identification. Its only inputs are the displayed finite
definitions and exact finite-dimensional linear algebra.

## Verification and mutation controls

Run the exact certificate:

```bash
python3 scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py
```

Expected:

```text
TOTAL: PASS=10 FAIL=0
```

The same runner exposes reviewer-reproducible mutations for translation-step
binding, character phase, normalization, site ordering, the `C_3` map,
symbolic weight dependence, and projector-label binding:

```bash
python3 scripts/flavor_carrier_momentum_type_from_translation_2026_06_15.py \
  --mutation <translation_direction|character_phase|normalization|site_ordering|c3_map|weight_dependence|projector_label>
```

Each mutation exits nonzero by breaking the exact family it targets.
