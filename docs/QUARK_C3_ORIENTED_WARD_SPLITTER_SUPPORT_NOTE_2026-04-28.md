# Quark `C3`-Oriented Ward Splitter Support Note

**Date:** 2026-04-28
**Type:** bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)
**Load-bearing carrier input:** the retained finite-dimensional
`H_hw=1 = C^3` operator surface and induced `C3[111]` cycle from
[`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md).
**Non-load-bearing physical-provenance boundary:** the broader
staggered-Dirac physical-realization program remains outside this local
matrix theorem. This note does not use that open physical-carrier provenance
as a proof input for the `C3` Ward normal form. In particular,
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` is named here only as a
plain-text non-load-bearing provenance pointer, not as a markdown one-hop
authority for this theorem.

**Status authority:** independent audit lane only. This source note does not
set status; the audit pipeline recomputes downstream status from source on
`origin/main`.

**Status:** exact support/boundary theorem for Lane 3 target 3C. This
block-06 artifact identifies the smallest local source/readout primitive that
can split the `S_3` doublet found in
`QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md`.
It does not claim retained `m_u`, `m_d`, `m_s`, `m_c`, or `m_b`.

**Primary runner:**
`scripts/frontier_quark_c3_oriented_ward_splitter_support.py`

## 1. Question

Block 05 proved that an `S_3`-equivariant Hermitian Ward operator on the
retained `hw=1` generation triplet has one singlet eigenvalue and one
doubly-degenerate `E` eigenvalue. Target 3C therefore needs a named
source/readout/symmetry-breaking primitive.

This note tests the nearest such primitive already suggested by the retained
generation observable surface:

```text
the induced oriented cycle C3[111] : X1 -> X2 -> X3 -> X1.
```

The question is not whether this closes quark masses. It asks the exact local
representation question:

```text
What is the complete Hermitian Ward normal form if the Ward operator is
C3[111]-equivariant but not required to be reflection-equivariant?
```

## 2. Minimal Premise Set

Allowed premises:

1. the retained `hw=1` generation triplet `V = span(X1,X2,X3)`;
2. the exact induced `C3[111]` cycle from the retained three-generation
   observable theorem;
3. ordinary Hermitian Ward endomorphisms on `V`;
4. standard finite cyclic representation theory and spectral algebra.

Forbidden proof inputs:

1. observed quark masses;
2. fitted Yukawa entries;
3. CKM mixing data treated as mass-eigenvalue input;
4. nearest-rational selection from endpoint or comparator data;
5. treating the new orientation coefficient as derived without a source law.

## 3. Exact `C3`-Equivariant Hermitian Normal Form

Let `C` be the retained cycle on the ordered basis `(X1,X2,X3)`:

```text
C X1 = X2,   C X2 = X3,   C X3 = X1,   C^3 = I.
```

Every complex endomorphism commuting with `C` is a polynomial in `C`:

```text
u I + v C + w C^2.
```

Hermiticity imposes `u in R` and `w = conjugate(v)`. Equivalently every
`C3`-equivariant Hermitian Ward operator has the three-real-parameter form

```text
W(a,b,c) = a I + b (C + C^2) + c (C - C^2)/(i sqrt(3)),
```

with `a,b,c in R`.

The last term is the oriented splitter:

```text
K_C3 = (C - C^2)/(i sqrt(3)).
```

It changes sign under any reflection that conjugates `C` to `C^2`. Therefore
`c` is precisely the reflection-breaking / orientation coefficient.

## 4. Spectrum

In the Fourier basis diagonalizing `C`, the eigenvalues are

```text
lambda_0 = a + 2 b,
lambda_+ = a - b + c,
lambda_- = a - b - c.
```

Consequences:

1. if `c = 0`, the `E` doublet degeneracy remains:

   ```text
   lambda_+ = lambda_- = a - b;
   ```

2. if `c != 0` and `c != +/- 3b`, the three eigenvalues are distinct;
3. the split is in the cyclic Fourier basis, not in the original generation
   projector basis `(X1,X2,X3)`.

Thus an oriented `C3` primitive is sufficient to remove the representation
degeneracy found in block 05. It is not sufficient to derive quark Yukawa
ratios, because the real Ward coefficients `a,b,c` remain free.

## 5. Diagonal Generation Readout Boundary

The retained translation-character projectors separate `X1`, `X2`, and `X3`.
If a Ward readout is required to be diagonal in that generation basis and
`C3`-equivariant, then cyclic covariance forces

```text
diag(x,y,z) = diag(x,x,x).
```

So the `C3` splitter and a generation-basis diagonal readout are different
choices. The oriented `C3` primitive gives exact Fourier-mode strata. A future
3C closure still needs a source/readout theorem explaining why those strata,
or a derived transform of them, are the physical quark Yukawa Ward channels.

## 6. Theorem

**Theorem (`C3`-oriented Ward splitter support/boundary).** On the retained
`hw=1` generation triplet, the Hermitian Ward endomorphisms that commute with
the retained induced `C3[111]` cycle are exactly

```text
W(a,b,c) = a I + b (C + C^2) + c (C - C^2)/(i sqrt(3)),
```

with `a,b,c in R`. The coefficient `c` is odd under the retained reflections
that exchange the two cycle orientations. Nonzero generic `c` splits the
`S_3` doublet into two cyclic Fourier channels, while `c = 0` collapses back
to the unbroken-`S_3` two-value spectrum. If a readout is also diagonal in the
translation-character generation basis, `C3` equivariance forces it to be
scalar. Therefore oriented `C3` is an exact local splitter primitive for the
3C residual, but not a retained non-top quark mass derivation.

## 7. What This Adds

This block gives the next theorem target a sharper form:

```text
derive a physical source law for the orientation coefficient c and the
remaining Ward coefficients b/a, or derive a readout theorem that maps the
cyclic Fourier strata to quark Yukawa channels.
```

Without that source/readout theorem, the oriented `C3` normal form is exact support only.

## 8. What Remains Open

Lane 3 remains open. This note does not derive:

1. numerical `y_u/y_t`, `y_c/y_t`, `y_d/y_t`, `y_s/y_t`, or `y_b/y_t`;
2. an absolute non-top quark mass scale;
3. the down-type `5/6` non-perturbative exponent and scale-selection theorem;
4. an up-type amplitude scalar law.

## 9. Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_c3_oriented_ward_splitter_support.py
```

Expected result:

```text
TOTAL: PASS=58, FAIL=0
VERDICT: oriented C3 supplies an exact local splitter primitive, but leaves
the Lane 3 quark-mass Ward source/readout law open.
```


## Dependency rewire (2026-06-18)

The local theorem in this note needs only a supplied three-dimensional
operator surface and a supplied oriented order-three cycle. That surface is
now supplied by the retained finite-dimensional matrix theorem in
[`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md):

1. `V = H_hw=1 = span(X1,X2,X3) = C^3`;
2. three rank-one translation-character projectors that distinguish
   `X1`, `X2`, and `X3`;
3. the induced oriented `C3[111]` cycle
   `X1 -> X2 -> X3 -> X1`;
4. the statement that these projectors and the cycle generate the full
   finite matrix algebra `M_3(C)`.

This support note then proves a different finite-dimensional fact on that
surface: the Hermitian commutant of the oriented cycle is the
three-real-parameter family

```text
W(a,b,c) = a I + b (C + C^2) + c (C - C^2)/(i sqrt(3)).
```

The physical origin of the retained `C^3` surface, species semantics,
fermion fields, staggered action, Grassmann/CAR realization, charged-lepton
sector content, neutrino sector content, quark/hadron content, and the
Koide/PMNS/CKM observable surfaces are not part of this note's proof. A
future theorem that uses those physical meanings must cite its own retained
physical-carrier or source/readout bridge.

For a source-side audit-unlock split that isolates this algebraic core from
physical-carrier provenance, see
[`QUARK_C3_ORIENTED_WARD_SPLITTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`](QUARK_C3_ORIENTED_WARD_SPLITTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md).

## Dependency repair (2026-06-20)

This source-side repair removes the unaudited
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` as a load-bearing one-hop
authority and cites only the retained finite-dimensional `C3` operator surface.

The actual derivation in Sections 3-6 needs exactly two supplied objects: a
three-dimensional complex operator surface `V = C^3` and an oriented order-three
cycle `C` with `C^3 = I`. Both are supplied by the **retained** finite-dimensional
matrix theorem
[`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
(its load-bearing surface is, per its own narrowing, purely algebraic on
`H_hw=1 = C^3` and retained-grade). No fermion-field, staggered-action,
Grassmann/CAR, or physical-carrier content enters the commutant computation
`W(a,b,c) = a I + b(C + C^2) + c(C - C^2)/(i sqrt(3))`, the Fourier spectrum, or
the diagonal-readout boundary.

Concretely:

1. the load-bearing carrier authority is re-cited as the retained
   `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md` (one-hop markdown link);
2. `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` is demoted to a
   plain-text non-load-bearing provenance pointer (no markdown link) and is no
   longer listed among the machine-visible dependency links for this row;
3. the primary runner reads only the retained carrier/support surfaces
   (`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`,
   `QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md`,
   `S3_TASTE_CUBE_DECOMPOSITION_NOTE.md`,
   `Z2_HW1_MASS_MATRIX_PARAMETRIZATION_NOTE.md`) and never reads the staggered
   gate; a runner check now positively asserts that the staggered gate is not a
   markdown one-hop authority of this note.

This is a citation-graph repair only. It does not change any derived value, does
not broaden the claim scope, and does not set status.

**Status authority:** independent audit lane only.

## Machine-Visible Dependency Links

This graph-bookkeeping section records explicit dependency links for the audit
citation graph. It does not promote this note or change the claim scope.

- [three_generation_observable_theorem_note](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
- [quark_generation_equivariant_ward_degeneracy_no_go_note_2026-04-28](QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md)
- [s3_taste_cube_decomposition_note](S3_TASTE_CUBE_DECOMPOSITION_NOTE.md)
