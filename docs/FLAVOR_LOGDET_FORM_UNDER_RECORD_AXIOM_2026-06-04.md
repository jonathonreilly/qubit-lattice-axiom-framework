# Flavor - conditional log-det form from Record-compatible additivity plus a separate det-character authority

**Date:** 2026-06-04
**Claim type:** bounded_theorem — conditional form theorem / roadmap. This is not an audit
verdict, not a value derivation, and not a downstream row promotion.
**Status authority:** independent audit lane only. This note sets no audit
status and assigns no grade.
**Runner:** [scripts/flavor_logdet_form_under_record_axiom_2026_06_04.py](../scripts/flavor_logdet_form_under_record_axiom_2026_06_04.py)
(SCORECARD 6/6).
**Depends:** [MINIMAL_AXIOMS_2026-06-04.md](MINIMAL_AXIOMS_2026-06-04.md)
for the Record additivity premise, and
[OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md](OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md)
for the separate determinant-character form-selection authority.

## Statement

This is a conditional form statement, not a new axiom and not a claim that the
Record axiom alone supplies log-det readout.

Assume all of the following external conditions have already been specified or
proved:

1. a proposed generator is a finite scalar record functional on a specified
   disjoint record-readout surface;
2. its block value is built from a multiplicative character of the local
   operator algebra;
3. the relevant character authority selects the determinant family, up to
   power and scale.

Then Record additivity over disjoint record collections requires the additive
image of that multiplicative determinant family:

```text
W = c log |det|
```

where `c` is an additive-baseline and normalization convention.

## What Record Contributes

The Record axiom contributes only the finite scalar additivity rule:

```text
I(R_1 sqcup R_2) = I(R_1) + I(R_2)
```

It does not identify an arbitrary operator expression as a record functional,
does not prove the determinant-character theorem, and does not supply the
source/action coupling `D + J`.

In this conditional setting, the additive rule rules out using the raw
multiplicative quantity `|det|^p` as the scalar record readout, because
`|det(A (+) B)|^p` multiplies across disjoint blocks. Its logarithmic image
adds:

```text
log |det(A (+) B)| = log |det A| + log |det B|.
```

This is the narrow sense in which the Record axiom supplies the additivity
premise for a log-det form. It is not a source of `retained_bounded` status.

## What Remains Outside This Note

- **Record-realization:** showing that the proposed domain is a specified
  finite record-readout surface.
- **Det-character selection:** the determinant family is supplied only by the
  separate det-character note, which still has its own audit status.
- **Source/action coupling:** `W = log |det(D+J)|` and
  `dW/dj_x = Re Tr[(D+J)^-1 P_x]` require a separate source/action bridge.
- **Koide value or Born weights:** Record excludes Born weights,
  `AC_phi_lambda`, and within-`C^3` weight selection.

Therefore this note does not move the 91 rows classified in
[RECORD_P1_DEPENDENCY_AUDIT_NOTE_2026-06-04.md](RECORD_P1_DEPENDENCY_AUDIT_NOTE_2026-06-04.md).
Rows that need log-det readout still need the non-axiom residuals named above.

## Verified Algebra

The runner checks the finite algebra used by this conditional statement:

- `det(AB)=det(A)det(B)` for sample invertible matrices, while `Tr` fails the
  same multiplicative-character test;
- powers of `det` multiply, illustrating the determinant-character family;
- `det(A (+) B)=det(A)det(B)` over disjoint blocks;
- `|det|^p` multiplies over disjoint blocks, while `log |det|` adds;
- the same logarithmic additivity holds over three blocks;
- for Hermitian `H`, `log |det H|` equals the sum of `log |lambda|` over its
  spectral modes.

These checks are sanity checks for the finite algebra. They do not prove the
separate representation-theoretic determinant-character theorem and do not
assign audit status.
