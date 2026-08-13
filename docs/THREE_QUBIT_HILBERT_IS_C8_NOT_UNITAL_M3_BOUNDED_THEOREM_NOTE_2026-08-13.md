---
claim_id: three_qubit_hilbert_is_c8_not_unital_m3_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Lattice plus Qubit supply a three-site Hilbert space H_3 = (C^2)^{⊗3} ≅ C^8 of complex dimension 8, with B(H_3) ≅ M_8(C) of dimension 64. That object is a native site tensor. Unital M_3(C) is a different type: dim M_3 = 9 ≠ 8 = dim H_3 and 9 ≠ 64 = dim M_8, and a unital copy of M_3 does not sit in M_8 because 3 does not divide 8. The note does not identify C^8 with Standard Model generations, does not identify M_3 with QCD, and does not adopt a generation axiom."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_qubit_hilbert_is_c8_not_unital_m3_2026_08_13.py
---

# Three-Qubit Hilbert Space Is `C^8`, Not Unital `M_3`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact dimension and type split between a three-site Lattice+Qubit
Hilbert tensor and the unital matrix algebra `M_3(C)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_qubit_hilbert_is_c8_not_unital_m3_2026_08_13.py`](../scripts/three_qubit_hilbert_is_c8_not_unital_m3_2026_08_13.py)

Parents on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The Qubit axiom presents one site as `M_2(C)`. The defining module of that
presentation is `C^2`, of complex dimension `2`. Lattice supplies distinct
sites. The three-site tensor Hilbert space therefore exists as a native
construction:

`H_3 = (C^2)^{⊗3} ≅ C^8`, `dim_C H_3 = 2^3 = 8`.

Bounded operators on that space are `B(H_3) ≅ M_8(C)`, of complex dimension
`64`.

Unital `M_3(C)` is not that Hilbert space and is not its operator algebra:
`dim M_3 = 9 ≠ 8` and `9 ≠ 64`. A unital copy of `M_3` still does not sit
inside `M_8`, because `3` does not divide `8`. Those are different types:
one is a Lattice+Qubit tensor of sites; the other is not.

This note does not identify `C^8` with Standard Model generations and does
not identify `M_3` with QCD.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The three-site Hilbert dimension, the mismatch with dim M_3 and dim M_8, and the one-line 3-does-not-divide-8 non-embedding are exact integer facts on declared Lattice+Qubit objects. Identifying C^8 with generations, identifying M_3 with a gauge algebra, and adopting a generation axiom remain out of scope."
trace_class: type_split
artifact_role: theorem
conditional_surface_status: "exact for dimensions and the displayed type split; no Standard Model or QCD identification is claimed"
hypothetical_axiom_status: "no axiom edit, adoption, minimality, or necessity claim"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `C` for the complex numbers. The Qubit axiom gives each Lattice site
the one-site possibility algebra `M_2(C)`. The defining Hilbert module of
`M_2(C)` is `C^2`, with

`dim_C C^2 = 2`.

For any three sites, the Lattice+Qubit tensor of those one-site modules is

`H_3 := (C^2) ⊗ (C^2) ⊗ (C^2) ≅ C^8`.

The bounded operators on that finite-dimensional Hilbert space are

`B(H_3) ≅ M_8(C)`, `dim_C M_8(C) = 8 · 8 = 64`.

Separately, `M_3(C)` denotes the unital complex matrix algebra of `3 × 3`
matrices, with

`dim_C M_3(C) = 3 · 3 = 9`.

No further primitive is introduced. In particular this note does not add a
generation axiom and does not import an observational generation count.

## Theorems

### Theorem 1

`dim_C H_3 = 8`.

**Proof.** Each factor has dimension `2`. Dimension of a tensor product is
the product of the dimensions, so

`dim_C H_3 = 2 · 2 · 2 = 2^3`.

The integer identity is `2**3 == 8`. Hence `H_3 ≅ C^8`. ∎

### Theorem 2

`dim_C M_3 = 9 ≠ 8 = dim_C H_3`. Consequently `M_3` is not `B(H)` for
`H = H_3`. Also `9 ≠ 64 = dim_C M_8`.

**Proof.** A basis of `M_3(C)` is the nine matrix units `E_{ij}` with
`i, j ∈ {1,2,3}`, so the dimension is `3 · 3 = 9`. Theorem 1 gives
`dim H_3 = 8`. These integers are unequal, so the Hilbert space `H_3` is
not the defining module of `M_3`, and `M_3` is not the full operator
algebra of `H_3`. The operator algebra of `H_3` is `M_8(C)`, whose
dimension is `8 · 8 = 64`, and `9 ≠ 64`. ∎

### Theorem 3

A three-site Hilbert space is a Lattice+Qubit tensor of sites. That
construction exists and has dimension `8`. Unital `M_3` still does not sit
in `M_8` (`3 ∤ 8`). So a generations-as-Hilbert reading and a
color-as-unital-algebra reading are different types: one is a native tensor
of sites, the other is not.

**Proof.** Lattice supplies distinct sites; Qubit supplies a `C^2` module at
each site. The three-fold tensor of Theorem 1 is therefore a construction
already named by those two axioms; its dimension is `8`. A unital
homomorphism `M_3(C) → M_8(C)` would realize the defining `3`-dimensional
module of `M_3` as a direct summand of `C^8`, which requires `3 | 8`. But
`8 = 2^3` and `3` is odd, so `3 ∤ 8`. The Hilbert tensor therefore exists
as a site tensor while unital `M_3` does not sit in the operator algebra of
that tensor. Those are different mathematical types. ∎

The line `3 ∤ 8` is the whole unital-embedding content used here. This note
is not a restatement of a general unital-`M_3`-in-`M_{2^n}` classification.

### Theorem 4

Do not identify `C^8` with Standard Model generations. Do not identify
`M_3` with QCD. The displayed fact is the type split.

**Proof of the split; refusal of the identifications.** Theorems 1–3 compare
dimensions and types of declared Lattice+Qubit objects with the separate
algebra `M_3(C)`. Nothing in the axiom memo names three generations, a
generation axiom, QCD, or a color gauge algebra. An identification of
`H_3 ≅ C^8` with Standard Model generations, or of `M_3` with QCD, would
be an extra reading, not a consequence of the integers above. The note
therefore stops at the type split and does not adopt those readings. ∎

## Type Split

| Object | Type | Native from Lattice+Qubit? | `dim_C` |
|---|---|---|---|
| one-site module | `C^2` | yes (Qubit `M_2(C)` defining module) | `2` |
| three-site Hilbert `H_3` | `(C^2)^{⊗3} ≅ C^8` | yes (tensor of sites) | `8` |
| bounded operators on `H_3` | `B(H_3) ≅ M_8(C)` | yes (endomorphisms of that tensor) | `64` |
| unital `M_3(C)` | matrix algebra | no | `9` |

The first three rows are one type family: Hilbert modules and their
endomorphisms built by tensoring sites. The last row is an algebra of a
different size that does not embed unitaly into `M_8`. Displaying the split
is the claim. Equating the first family with Standard Model generations, or
the last row with QCD, is outside the claim.

## What This Note Does Not Do

- It does not edit an axiom and does not adopt a generation axiom.
- It does not identify `C^8` with Standard Model generations.
- It does not identify `M_3` with QCD and does not use PDG data.
- It does not reopen a closed color-algebra classification. The one-line
  fact `3 ∤ 8` is used only to keep the unital-algebra type distinct from
  the Hilbert tensor.
- It does not claim that no other three-dimensional structure can ever be
  defined on some other carrier. It claims that the native three-site
  Hilbert space is `C^8`, not unital `M_3`.

## Runner

[`scripts/three_qubit_hilbert_is_c8_not_unital_m3_2026_08_13.py`](../scripts/three_qubit_hilbert_is_c8_not_unital_m3_2026_08_13.py)
rebuilds the tensor basis by pairing, counts matrix units, checks the
integer identities `2**3 == 8`, `3·3 == 9`, `8·8 == 64`, checks that the
false predicates `2**3 == 9` and `3 | 8` fail, and checks that this note
and the axiom memo carry the type-split wording rather than a generation
or QCD identification.
