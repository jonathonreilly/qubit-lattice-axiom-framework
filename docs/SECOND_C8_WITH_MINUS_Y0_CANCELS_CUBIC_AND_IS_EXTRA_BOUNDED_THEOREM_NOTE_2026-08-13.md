---
claim_id: second_c8_with_minus_y0_cancels_cubic_and_is_extra_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On a displayed C^8 the operator Y_0 = Pi_+ - 3 Pi_- has exact cubic trace 6 - 54 = -48. On the extra direct sum H = C^8 ⊕ C^8 the complementary block -Y_0 cancels that cubic, Tr(Y_⊕^3) = 0, while the first block keeps the parent (6,2) eigenvalue ratio 1 : (-3). The resulting 16-dimensional object is strictly larger than one-site Qubit M_2(C) and larger than one C^8. The displayed pair is not adopted as an axiom, not named as two generations, and is not identified with U(1)_Y or PDG hypercharge. Physical-hypercharge closure is not claimed."
upstream_dependencies:
  - minimal_axioms
  - lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02
runner: scripts/second_c8_with_minus_y0_cancels_cubic_and_is_extra_2026_08_13.py
---

# A Second C^8 With −Y_0 Cancels the Two-Block Cubic and Is Extra

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact integer traces of one displayed pair of 8-by-8 diagonal
operators and their 16-by-16 direct sum. No observational input.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/second_c8_with_minus_y0_cancels_cubic_and_is_extra_2026_08_13.py`](../scripts/second_c8_with_minus_y0_cancels_cubic_and_is_extra_2026_08_13.py)

Parents used as source text only:

- [`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
  supplies the structural multiplicity pair `(6, 2)` and the traceless
  eigenvalue ratio `1 : (−3)`. That parent does not identify the ratio with
  Standard Model hypercharge.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  Qubit sentence that the full one-site possibility domain has algebraic
  presentation `M_2(C)`. Neither a second `C^8` nor `Y_⊕` is named there.

The cubic integer `6 − 54 = −48` is reconstructed here from the displayed
diagonal. It is not imported from any other row.

## Result Up Front

Let `Pi_+ = diag(I_6, 0_2)` and `Pi_- = diag(0_6, I_2)` act on `C^8`, and set

```text
Y_0 = Pi_+ − 3 Pi_- = diag(1,1,1,1,1,1,−3,−3).
```

The first block therefore keeps the parent ratio `1 : (−3)` on the
multiplicities `(6, 2)`. The exact cubic is

```text
Tr(Y_0^3) = 6 · (1)^3 + 2 · (−3)^3 = 6 − 54 = −48 ≠ 0.
```

On the extra space `H = C^8 ⊕ C^8` define the complementary block `−Y_0` and

```text
Y_⊕ = Y_0 ⊕ (−Y_0).
```

Then

```text
Tr(Y_⊕^3) = Tr(Y_0^3) + Tr((−Y_0)^3) = −48 + 48 = 0.
```

The complementary 8-carrier with opposite `Y` is the smallest extra object
that keeps the `(6, 2)` ratio on the first block and meets the extra matching
condition `Tr(Y^3) = 0`: the opposite spectrum of `Y_0` is six copies of
`−1` and two copies of `+3`, which occupies eight eigenvalues and cannot sit
in a strictly smaller complementary carrier. The displayed `Y_⊕` is an extra
algebraic object. It is not adopted as an axiom and is not named as two
generations.

`dim H = 16` is strictly larger than `dim C^2 = 2` (the one-site Hilbert
space whose endomorphism algebra is the Qubit domain `M_2(C)`) and strictly
larger than `8`. A predicate that one-site `M_2(C)` already contains `Y_⊕`
is therefore false.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer traces on a displayed pair of carriers. The pair is extra relative to Qubit and is not adopted. No physical-hypercharge identification and no generation axiom."
trace_class: negative_route_pruning
target_claim_id: complementary_c8_cancels_cubic
target_blocker_text: "the (6,2) cubic Tr(Y_0^3)=-48 is not cancelled on one C^8"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
conditional_surface_status: "exact for the displayed pair and the cubic identities; P-HY identification remains open"
hypothetical_axiom_status: "no edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

On `C^8` the complementary projectors are

```text
Pi_+ = diag(I_6, 0_2),     Pi_- = diag(0_6, I_2),
Pi_+^2 = Pi_+,             Pi_-^2 = Pi_-,
Pi_+ Pi_- = 0,             Pi_+ + Pi_- = I_8,
rank(Pi_+) = 6,            rank(Pi_-) = 2.
```

The displayed abelian operator is

```text
Y_0 = Pi_+ − 3 Pi_-.
```

Its spectrum is `1` with multiplicity `6` and `−3` with multiplicity `2`.
Tracelessness `6 · 1 + 2 · (−3) = 0` is the parent ratio identity with
scale `α = 1`. The cubic is recomputed only from this diagonal:

```text
Tr(Y_0^3) = 6 − 54 = −48.
```

A predicate `Tr(Y_0^3) = 0` is therefore false.

On `H = C^8 ⊕ C^8` the complementary block is `−Y_0` and

```text
Y_⊕ = Y_0 ⊕ (−Y_0)
    = diag(1,1,1,1,1,1,−3,−3,−1,−1,−1,−1,−1,−1,+3,+3).
```

The first eight eigenvalues are exactly those of `Y_0`, so the first block
keeps the `(6, 2)` ratio. The last eight are the opposite spectrum, so the
extra matching cubic vanishes:

```text
Tr(Y_⊕^3) = (−48) + 48 = 0.
```

Identity gates in the runner call `cubic_Y0()` and `cubic_Yplus()`; those
functions compute the traces from the constructed matrices. They do not
return a stored target constant.

## Theorems

**Theorem 1.** `Tr(Y_0^3) = −48 ≠ 0`. Recomputed from
`6 · (1)^3 + 2 · (−3)^3 = 6 − 54`.

**Theorem 2.** `Tr(Y_⊕^3) = 0`. The complementary block cancels the cubic.

**Theorem 3.** `dim H = 16 > 2 = dim C^2` (one-site Qubit) and `16 > 8`.
The Qubit axiom states that the full one-site possibility domain has
algebraic presentation `M_2(C)`. Neither a second `C^8` nor `Y_⊕` is named
in that axiom memo.

**Theorem 4.** The smallest extra object that keeps the `(6, 2)` ratio on
the first block and satisfies the extra matching `Tr(Y^3) = 0` is a
complementary 8-carrier with opposite `Y`. The note displays `Y_⊕`. It does
not adopt that operator as an axiom and does not call the pair two
generations.

**Theorem 5.** Do not identify `Y_⊕` with Standard Model hypercharge. Do not
import PDG values. Do not claim that physical hypercharge (P-HY) is closed.

## What this note does not close

- Identification of `Y_0` or `Y_⊕` with `U(1)_Y` or with any PDG
  hypercharge assignment.
- Adoption of a generation axiom, a two-generation reading of `H`, or any
  extra axiom.
- Closure of physical hypercharge (P-HY).
- Anomaly cancellation for any Standard Model fermion census.
- A claim that one-site `M_2(C)` already contains `Y_⊕`.

## Audit-lane disposition (proposed)

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  exact integer reconstruction Tr(Y_0^3) = 6 - 54 = -48 on one C^8;
  complementary -Y_0 on a second C^8 cancels the cubic; the 16-dimensional
  pair is extra relative to one-site M_2(C); no U(1)_Y, PDG, generation
  axiom, or P-HY closure.
audit_status_authority: independent audit lane only
audit_required_before_effective_retained: true
```
