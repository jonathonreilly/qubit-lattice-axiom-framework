# Yukawa SSB Matching-Gap Arithmetic Boundary Note

**Date:** 2026-04-18
**Repair dates:** 2026-05-06; normalization-chain closure 2026-07-11
**Type:** positive_theorem
**Scope class:** exact finite-dimensional algebraic identity
**Claim scope:** bounded `H_unit` normalization arithmetic. On the canonical
orthonormal diagonal-contractor basis, form the equal-weight diagonal direction

```text
S_D = sum_{alpha,a} E_{alpha,a},  D = N_iso * N_c.
```

The positive unit-norm representative `H_unit = c S_D` has
`c = 1 / sqrt(D)`, derived below rather than assumed. Each single component
overlap is therefore `1 / sqrt(N_iso * N_c)`. For the stated values
`(N_iso, N_c) = (2, 3)`, every component independently evaluates to
`1 / sqrt(6)`.

**Boundary:** this note does not close a retained matching theorem for the
physical Standard Model Yukawa trilinear. In particular, it does not identify
the Ward four-fermion matrix element with the `Qbar_L-H-u_R` trilinear
coefficient. That stronger matching statement would require a separate
tree-level operator-matching theorem deriving the HS/source normalization,
SSB VEV division, chirality projection, LSZ/external-state normalization, and
absence of extra factors from the retained action. Those steps are not derived
here.

**Status authority:** this source note does not set its own audit outcome.
Independent audit must decide the final audit status for the scoped
finite-dimensional theorem.
**Primary runner:** `scripts/frontier_yt_ssb_matching_gap.py`
**Log:** `logs/retained/yt_ssb_matching_gap_2026-04-18.log`

---

## 1. Repair Summary

The earlier version of this note overclaimed that the SSB matching gap was
closed by a Hubbard-Stratonovich / effective-action route and a direct
identical-operator route. The review objection correctly identified that this
equated two different readout structures by naming both of them `H_unit`.

The first repair kept only the local component arithmetic, but began after the
normalizing coefficient had already been inserted into the definition. This
repair closes that remaining local step. Starting from the unnormalized
equal-weight diagonal direction `S_D`, orthonormality gives
`||S_D||_HS^2 = D`; the positive unit-norm condition then forces
`H_unit = S_D / sqrt(D)`. Only after that derivation does the note evaluate
the component overlap:

```text
<alpha_0,a_0 | H_unit | alpha_0,a_0>
  = 1 / sqrt(N_iso * N_c).
```

At `(N_iso, N_c) = (2, 3)`, the result is `1 / sqrt(6)`. This is exact
finite-dimensional arithmetic. It is not a physical SSB matching theorem.

---

## 2. Definitions

Let

```text
D = N_iso * N_c
```

with `N_iso, N_c` positive integers. Let the pair Hilbert space have
orthonormal basis

```text
|alpha,a>,  1 <= alpha <= N_iso,  1 <= a <= N_c.
```

Let `E_{alpha,a}` be the diagonal Wick-contractor / matrix-unit operator that
acts as the identity on the basis pair `|alpha,a>` and as zero on all other
basis pairs:

```text
<beta,b | E_{alpha,a} | beta,b> =
  1, if (beta,b) = (alpha,a),
  0, otherwise.
```

Equip this diagonal-contractor space with its canonical Hilbert-Schmidt inner
product. The contractors are orthonormal:

```text
<E_{alpha,a}, E_{beta,b}>_HS
  := Tr(E_{alpha,a}^dagger E_{beta,b})
   = delta_{alpha,beta} delta_{a,b}.
```

Define the unnormalized equal-weight diagonal direction

```text
S_D := sum_{alpha=1..N_iso} sum_{a=1..N_c} E_{alpha,a} = I_D.
```

`H_unit` is defined as the positive unit-norm representative on this ray:

```text
H_unit := c S_D,  c > 0,  ||H_unit||_HS = 1.                       (D1)
```

The positivity clause fixes only the otherwise arbitrary overall sign/phase
of the one-dimensional ray. It is a mathematical representative convention,
not a physical Yukawa, source, VEV, or external-state normalization.

---

## 3. Theorem

The definition `(D1)` uniquely gives

```text
c = 1 / sqrt(N_iso * N_c),
H_unit = I_D / sqrt(D).                                             (T1)
```

Consequently, for any basis pair `|alpha_0,a_0>`,

```text
F(alpha_0,a_0)
  := <alpha_0,a_0 | H_unit | alpha_0,a_0>
   = 1 / sqrt(N_iso * N_c).                                        (T2)
```

For `(N_iso, N_c) = (2, 3)`,

```text
F(alpha_0,a_0) = 1 / sqrt(6).                                      (T3)
```

In particular, for any two independently selected basis components
`(alpha_0,a_0)` and `(beta_0,b_0)`, including distinct components,

```text
F(alpha_0,a_0) = F(beta_0,b_0) = 1 / sqrt(6).                       (T4)
```

This is equality of two separately evaluated components of the derived
equal-weight unit vector, not an identification of two physical operators.

---

## 4. Proof

First derive the coefficient. Orthonormality gives

```text
||S_D||_HS^2
  = <sum_{alpha,a} E_{alpha,a}, sum_{beta,b} E_{beta,b}>_HS
  = sum_{alpha,a,beta,b}
      delta_{alpha,beta} delta_{a,b}
  = D.
```

Using `H_unit = c S_D` and the unit-norm clause in `(D1)`,

```text
1 = ||H_unit||_HS^2 = c^2 ||S_D||_HS^2 = c^2 D.
```

Thus `|c| = 1 / sqrt(D)`. The specified positive representative has
`c = 1 / sqrt(D)`, which proves `(T1)`. No `1 / sqrt(D)` coefficient was used
as an input to this normalization step.

Now evaluate a component. From `(T1)`,

```text
<alpha_0,a_0 | H_unit | alpha_0,a_0>
  = <alpha_0,a_0 |
      c * sum_{alpha,a} E_{alpha,a}
    | alpha_0,a_0>
```

Linearity gives

```text
= c *
  sum_{alpha,a}
  <alpha_0,a_0 | E_{alpha,a} | alpha_0,a_0>.
```

All summands vanish except the one with `(alpha,a) = (alpha_0,a_0)`, and that
summand equals `1` by the canonical basis-pair normalization. Therefore

```text
<alpha_0,a_0 | H_unit | alpha_0,a_0>
  = c * 1
  = 1 / sqrt(D)
  = 1 / sqrt(N_iso * N_c).
```

Substituting `(N_iso, N_c) = (2, 3)` gives `D = 6` and hence
`1 / sqrt(6)`. Repeating the displayed contraction for any second component
selects its own single Kronecker-delta term and yields the same value; no
aliasing step is used.

No gauge coupling, source normalization, SSB VEV, LSZ residue, chirality
projector, or physical Yukawa readout map appears in this proof. The theorem
is exactly the component-overlap arithmetic of the stated operator.

---

## 5. What This Claims

- The Hilbert-Schmidt normalization identity `(T1)` for the equal-weight
  diagonal direction at any positive `N_iso, N_c`.
- The finite-dimensional component identity `(T2)`.
- The stated arithmetic instance `(N_iso, N_c) = (2, 3)` gives
  `1 / sqrt(6)`.
- Any two component overlaps, evaluated separately, give the same number.
- The scoped overlap expression contains no gauge-coupling parameter and no
  SSB/readout normalization symbol.

---

## 6. What This Does Not Claim

- Does not derive the physical Yukawa trilinear coefficient.
- Does not close the SSB matching gap.
- Does not prove a Hubbard-Stratonovich source-normalization theorem.
- Does not divide by or derive an EWSB VEV normalization.
- Does not perform a chirality projection from the scalar-singlet bilinear to
  the `Qbar_L-H-u_R` Standard Model monomial.
- Does not derive LSZ or external-state normalization factors.
- Does not prove that no additional finite, sign, color, chirality, source, or
  field-normalization factors enter the physical trilinear readout.
- Does not use observed masses, PDG values, fitted selectors, or admitted unit
  conventions.

The physical matching problem remains open until those ingredients are
derived by a separate retained action-level operator-matching theorem.

---

## 7. Relation To The Ward And Class 5 Notes

`YT_WARD_IDENTITY_DERIVATION_THEOREM.md` is context for the framework's
Ward-side use of `H_unit` and
contains the stronger free-two-point-residue and symmetry-uniqueness chain.
This note does not consume the Ward or physical-readout claims. It independently
derives only the equal-weight diagonal ray's Hilbert-Schmidt normalization and
component arithmetic from the definitions in Section 2.

`YT_CLASS_5_NON_QL_YUKAWA_VERTEX_NOTE_2026-04-18.md` discusses
non-`Q_L` Yukawa trilinear Clebsch-Gordan factors. This note does not certify
that the Class 5 trilinear coefficient is the same Green-function object as the
Ward four-fermion coefficient, and it uses no Class 5 statement as a premise.

---

## 8. Audit Repair Mapping

Review target quoted from the existing row:

```text
Shared H_unit normalization is asserted, not derived from a tree-level
operator-matching theorem.
```

Repair:

1. The theorem starts from `S_D = sum E_{alpha,a}`, not from an already
   normalized `H_unit`.
2. The Hilbert-Schmidt contraction derives `||S_D||^2 = D` and hence derives
   the positive unit coefficient `c = 1 / sqrt(D)`.
3. Each component is evaluated independently from the derived coefficient;
   there is no two-name alias equality.
4. The theorem statement continues to exclude the physical trilinear and all
   operator-matching content.
5. The missing physical steps remain explicit open boundaries rather than
   silently passed.

The intended re-audit scope is therefore:

```text
Given an orthonormal diagonal-contractor basis and its equal-weight sum S_D,
the positive unit-norm representative is H_unit = S_D / sqrt(N_iso*N_c);
therefore every diagonal component overlap at (N_iso,N_c)=(2,3) equals
1 / sqrt(6).
```

---

## 9. Validation

Primary runner: `scripts/frontier_yt_ssb_matching_gap.py`.

The repaired runner verifies:

1. positive integer dimensions and `D = N_iso * N_c`;
2. the unnormalized equal-weight vector has squared norm `D`;
3. solving the unit-norm equation gives the positive coefficient
   `1 / sqrt(D)` and normalized squared norm `1`;
4. the stated instance `D = 6`;
5. explicit matrix form `H_unit = I_6 / sqrt(6)`;
6. diagonal component overlaps are all `1 / sqrt(6)`;
7. off-diagonal overlaps are zero;
8. two distinct components are separately evaluated and agree;
9. a doubled coefficient fails the unit-norm equation, while the negative
   coefficient preserves norm but fails the positive-representative clause;
10. alternative dimensions `(3,4)` give `1 / sqrt(12)`;
11. the degenerate dimension `(1,1)` gives `1`;
12. the proof expression contains no `g_bare`, `y_t_phys`, `V_EWSB`,
   `Z_LSZ`, `P_chiral`, or HS source-normalization symbol;
13. the runner outcome explicitly says the SSB matching theorem remains open.

The runner is intentionally an arithmetic verifier, not a physical matching
verifier.

---

## 10. Cross-References

- `YT_WARD_IDENTITY_DERIVATION_THEOREM.md` - context-only parent Ward/H_unit
  note; not a premise of this self-contained arithmetic theorem.
- `YT_CLASS_5_NON_QL_YUKAWA_VERTEX_NOTE_2026-04-18.md` - separate
  trilinear Clebsch-Gordan discussion, not certified by this note.
- `UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md` - context-only sibling
  narrow arithmetic theorem with the same finite-dimensional overlap core.
