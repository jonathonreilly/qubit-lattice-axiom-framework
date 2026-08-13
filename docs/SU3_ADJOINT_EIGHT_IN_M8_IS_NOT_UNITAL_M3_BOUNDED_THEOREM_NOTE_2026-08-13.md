---
claim_id: su3_adjoint_eight_in_m8_is_not_unital_m3_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The eight Gell-Mann matrices are an R-basis of su(3), dim_R = 8 ≠ 9 = dim_C M_3(C). Commutators close on the standard real structure constants. The adjoint representation ad(λ_a)_{bc} = 2 f_abc is an injective Lie homomorphism su(3) → M_8(R) ⊂ M_8(C) = End(C^8). That leftover does not install a unital *-hom M_3(C) → M_8(C), because 3 does not divide 8. Qubit names M_2(C), not su(3). The leftover is not adopted as QCD or as a unital M_3 summand, and Y_0 / hypercharge are not identified."
upstream_dependencies:
  - minimal_axioms
runner: scripts/su3_adjoint_eight_in_m8_is_not_unital_m3_2026_08_13.py
---

# su(3) Adjoint Eight In `M_8` Is Not Unital `M_3`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact type split between the real Lie algebra `su(3)` (adjoint-8
inside `End(C^8)`) and the unital `*`-algebra `M_3(C)`. No QCD. No Qubit
rewrite.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/su3_adjoint_eight_in_m8_is_not_unital_m3_2026_08_13.py`](../scripts/su3_adjoint_eight_in_m8_is_not_unital_m3_2026_08_13.py)

Parents on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Lattice plus Qubit supply a three-site Hilbert space

`H = (C^2)^{⊗3} ≅ C^8`, `B(H) ≅ M_8(C)`, `dim_C M_8(C) = 64`.

That Hilbert space is a native site tensor. Separately, the eight Gell-Mann
matrices `{λ_a}_{a=1..8}` are traceless Hermitian and `R`-linearly
independent, so `dim_R su(3) = 8`. The unit algebra `M_3(C)` has
`dim_C M_3(C) = 9`. The integers `8 ≠ 9`: the color Lie algebra is not the
unit algebra `M_3`.

Commutators close on the standard real structure constants:

`[λ_a, λ_b] = 2i ∑_c f_abc λ_c`.

The adjoint matrices `ad(λ_a)_{bc} = 2 f_abc` are eight linearly independent
real `8 × 8` matrices, so

`ad : su(3) → M_8(R) ⊂ M_8(C) = End(C^8)`

is an injective Lie homomorphism. Thus `su(3)` sits in `End(C^8)`.

That leftover is still not a unital `M_3` factor of the three-qubit algebra:
there is no unital `*`-homomorphism `M_3(C) → M_8(C)`, because `3 ∤ 8`.
Do not identify `C^8` with `M_3`. Do not identify `ad(su(3))` with a unital
`M_3` summand.

Qubit names `M_2(C)`, not `su(3)`. Lattice+Qubit supply `C^8` as a Hilbert
space. They do not name Gell-Mann matrices or QCD. This note does not adopt
a color axiom and does not identify `Y_0` or hypercharge.

This hole is independent of the three-site Hilbert-versus-unital-`M_3` type
split (`H ≅ C^8` is not unital `M_3`) and of the two-block `Y_0` carrier.
The present hole is type: color-as-Lie-8 versus color-as-`M_3`-9.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Gell-Mann independence, structure-constant closure, injective adjoint into M_8, and the 3-does-not-divide-8 unital obstruction are proved on declared finite matrix objects. Adoption of a color axiom, QCD identification, and a unital M_3 summand remain refused."
trace_class: type_split
target_claim_id: color_as_adjoint_8_is_not_unital_m3
target_blocker_text: "does su(3) sitting in End(C^8) install unital M_3 as a three-qubit color algebra"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for adjoint-8 versus unital M_3 on End(C^8); other color leftovers remain unclaimed"
hypothetical_axiom_status: "color-as-adjoint-8 leftover: su(3) closes in M_8; not adopted as QCD or as unital M_3"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `C` for the complex numbers. The Qubit axiom gives each Lattice site
the one-site possibility algebra `M_2(C)`. The defining module is `C^2`.
The three-site tensor is

`H := (C^2)^{⊗3} ≅ C^8`, `B(H) ≅ M_8(C)`, `dim_C M_8(C) = 8 · 8 = 64`.

Let `{λ_a}_{a=1..8}` be the standard Gell-Mann matrices (traceless Hermitian
`3 × 3`). They are `C`-linearly independent as well, but the Lie algebra they
span is the **real** span of `{i λ_a}` (equivalently the real span of the
`λ_a` inside the traceless Hermitian matrices). Thus `dim_R su(3) = 8`.

Separately, `M_3(C)` is the unital complex `*`-algebra of `3 × 3` matrices,
with matrix-unit basis of cardinality `9`, so `dim_C M_3(C) = 9`.

The standard totally antisymmetric real structure constants of `su(3)` are
determined by the independent values

`f_123 = 1`,
`f_147 = f_246 = f_257 = f_345 = 1/2`,
`f_156 = f_367 = -1/2`,
`f_458 = f_678 = √3 / 2`,

and the sign of the permutation on each triple. The Lie bracket in the
Gell-Mann basis is

`[λ_a, λ_b] = 2i ∑_{c=1}^8 f_abc λ_c`.

The adjoint representation used here is the real `8 × 8` family

`ad(λ_a)_{bc} = 2 f_{abc}`,

with `b, c` running through `{1,...,8}`. These matrices lie in
`M_8(R) ⊂ M_8(C) = End(C^8)`.

No axiom is edited. The Gell-Mann matrices and `ad` are displayed test
objects, not a proposed Qubit rewrite and not a registered primitive.

## Theorems

### Theorem 1 — eight, not nine

The eight Gell-Mann matrices are linearly independent over `R` and each has
trace `0`. The real span therefore has dimension `8`, not `9`.

**Proof.** Each `λ_a` is Hermitian by inspection and `Tr λ_a = 0` (the
diagonal matrices `λ_3` and `λ_8` are `diag(1,-1,0)` and
`(1/√3) diag(1,1,-2)`). The trace form is

`Tr(λ_a λ_b) = 2 δ_{ab}`.

If `∑_a r_a λ_a = 0` with real coefficients, pairing against `λ_b` gives
`2 r_b = 0`. Hence the eight matrices are `R`-independent, so
`dim_R su(3) = 8`. The unit algebra `M_3(C)` has dimension `9`. These are
different integers. ∎

### Theorem 2 — commutators close

`[λ_a, λ_b] = 2i ∑_c f_abc λ_c` with the standard real `f_abc`.

A generating set used by the companion runner:

- I-spin: `[λ_1, λ_2] = 2i λ_3`.
- V-spin: `[λ_4, λ_5] = 2i (½ λ_3 + (√3/2) λ_8)`.
- U-spin: `[λ_6, λ_7] = 2i (-½ λ_3 + (√3/2) λ_8)`.
- The identity `f_147 = 1/2`: `[λ_1, λ_4] = i λ_7`.

The V-spin and U-spin brackets mix `λ_3` with `λ_8`. They are **not** equal
to `2i λ_3`. The structure-constant formula is the claim; the I-spin copy
is the only one of those three su(2) triples whose third generator is
exactly `λ_3`.

**Proof.** Direct matrix multiplication on the four pairs, using only
integer/`Fraction` entries except the exact `√3` coefficients of `λ_8` and
of `f_458`, `f_678`. The same `f_abc` reproduce every pair through the
stated formula. ∎

### Theorem 3 — adjoint eight sits in `End(C^8)`

The matrices `ad(λ_a)_{bc} = 2 f_{abc}` are eight linearly independent real
`8 × 8` matrices. Therefore

`ad : su(3) → M_8(R) ⊂ M_8(C)`

is an injective Lie homomorphism, and `su(3)` sits in `End(C^8)`.

**Proof.** The entries `2 f_abc` are real. The Frobenius pairing

`∑_{b,c} ad(λ_a)_{bc} ad(λ_d)_{bc} = 4 ∑_{b,c} f_abc f_dbc = 12 δ_{ad}`

is nondegenerate, so the eight matrices are `R`-independent and `ad` has
trivial kernel. Internal consistency of the index convention
`ad(λ_a)_{bc} = 2 f_{abc}` is the homomorphism identity on the I-spin
generators,

`[ad(λ_1), ad(λ_2)] = -2 ad(λ_3)`.

The minus sign is the matrix-index counterpart of `f_{abc} = -f_{acb}`;
it is the real adjoint of `[λ_1, λ_2] = 2i λ_3` in this convention. ∎

### Theorem 4 — still no unital `M_3` in `M_8`

There is still no unital `*`-homomorphism `M_3(C) → M_8(C)`, because
`3 ∤ 8`. Adjoint-8 is not a unital `M_3` factor of the three-qubit algebra.

**Proof.** A unital `C`-linear `*`-hom `M_k(C) → M_m(C)` exists if and only
if `k` divides `m`: the standard module `C^m` must be a multiple of `C^k`.
Here `k = 3` and `m = 8 = 2^3`, so `3 ∤ 8`. An injective Lie embedding of
`su(3)` into `M_8` is a different type from a unital algebra embedding of
`M_3`. The extra complex dimension `9 - 8 = 1` is exactly the unit line
that `su(3)` does not contain. ∎

### Theorem 5 — Qubit does not name this leftover

Qubit names `M_2(C)`, not `su(3)`. Lattice+Qubit supply `C^8` as a Hilbert
space. They do not name Gell-Mann matrices or QCD. This note does not adopt
a color axiom and does not identify `Y_0` or hypercharge.

**Proof of the split; refusal of the identifications.** Theorems 1–4 compare
a displayed Lie algebra and its adjoint representation with the separate
unital algebra `M_3(C)` and with the native three-site Hilbert space. The
live axiom memo names one-site `M_2(C)` and does not name `su(3)`, Gell-Mann
matrices, QCD, `Y_0`, or hypercharge. Displaying the leftover does not adopt
it. ∎

## Type Split

| Object | Type | Native from Lattice+Qubit? | Dimension |
|---|---|---|---|
| one-site module | `C^2` | yes (Qubit defining module) | `dim_C = 2` |
| three-site Hilbert `H` | `(C^2)^{⊗3} ≅ C^8` | yes (tensor of sites) | `dim_C = 8` |
| bounded operators on `H` | `B(H) ≅ M_8(C)` | yes (endomorphisms) | `dim_C = 64` |
| `su(3)` | real Lie algebra | no; displayed leftover | `dim_R = 8` |
| `ad(su(3))` | eight matrices in `M_8(R)` | no; injective Lie image | `dim_R = 8` |
| unital `M_3(C)` | unital `*`-algebra | no | `dim_C = 9` |

The first three rows are the Lattice+Qubit Hilbert type. The next two rows
are a Lie-algebra leftover that happens to act on an 8-dimensional space.
The last row is a 9-dimensional unital algebra that does not embed unitaly
into `M_8`. Equating the leftover with QCD, or with a unital `M_3` summand,
is outside the claim.

## Mutations

Three hostile predicates must fail.

1. “`dim su(3) == 9`.” False: Theorem 1 reconstructs `dim_R su(3) = 8`.
2. “`3` divides `8`.” False: `8 = 2^3` and `3` is odd.
3. “The eight matrices `ad(λ_a)` are linearly dependent.” False: Theorem 3,
   the pairing is `12 δ_{ad}`.

## What This Note Does Not Do

- It does not edit an axiom and does not rewrite Qubit.
- It does not adopt a color axiom.
- It does not identify `C^8` with `M_3`.
- It does not identify `ad(su(3))` with a unital `M_3` summand.
- It does not identify the leftover with QCD, and it does not identify
  `Y_0` or hypercharge.
- It does not rest on, and does not reopen, the separate hole that the
  three-site Hilbert space `C^8` is not itself unital `M_3`, nor the
  two-block `Y_0` carrier hole.
- It does not claim that every other color construction is impossible.

## No-Go Discipline Gate

The negative claim is only: adjoint-8 sits in `End(C^8)` and is still not
unital `M_3`. The gate does not certify that color is underivable by every
route.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Gell-Mann span equals `M_3` | compare `dim_R su(3)` to `dim_C M_3` | Theorem 1: `8 ≠ 9` | **ATTEMPTED** |
| Commutator closure | check `[λ_a,λ_b]=2i ∑ f_abc λ_c` on a generating set | Theorem 2 | **ATTEMPTED** |
| Adjoint injection into `M_8` | `ad(λ_a)_{bc}=2 f_abc` independent | Theorem 3: injective Lie hom | **ATTEMPTED** |
| Unital `*`-hom `M_3 → M_8` | require `3 \| 8` | Theorem 4: `3 ∤ 8` | **ATTEMPTED** |
| Identify `ad(su(3))` with a unital `M_3` summand | equate Lie image with unit algebra | refused; different types | **CLOSED HERE** |
| Identify `C^8` with `M_3` | equate Hilbert space with unit algebra | refused | **CLOSED HERE** |
| Adopt a color axiom / name QCD | fifth primitive or QCD import | refused; leftover not adopted | **CLOSED HERE** |
| Identify `Y_0` or hypercharge | extra reading | refused | **CLOSED HERE** |
| Other color leftovers | non-unital pads, declared carriers | not claimed | **LIVE / OUT OF SCOPE** |

The broad statement “the axioms cannot derive color by any route” is not
shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| `dim su(3)=8` / `3 ∤ 8` | no: a Lie dimension does not decide unital divisibility | no: non-divisibility does not compute the Gell-Mann span | independent identities |
| adjoint injection / unital `M_3` obstruction | no: a Lie hom can exist when no unital `*`-hom exists | no: absence of a unital map does not produce `ad` | independent holes |
| leftover display / axiom adoption | no: Theorem 5 refuses adoption | no: the live memo does not name Gell-Mann matrices | leftover remains hypothetical |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `H`, `M_8`, `M_3`, `{λ_a}`, `f_abc`, `ad` | reconstructed finite matrix objects |
| unital `C`-linear `*`-hom | standard finite-factor criterion `k \| m` |
| color-as-adjoint-8 leftover | explicit hypothetical reading; not adopted |
| QCD / `Y_0` / hypercharge | comparison language only; not identified |
| observations or fitted constants | none |
| float approximations | none required; `√3` kept as an exact `Q(√3)` coefficient |

### N4 — hostile counter-reading

A reader might say: “`su(3)` injects into `M_8`, and `C^8` is the
three-qubit space, so color is already a three-qubit algebra.” An injective
Lie homomorphism is not a unital `*`-homomorphism of `M_3`. The missing
complex dimension is the unit. `3 ∤ 8` still forbids a unital copy of
`M_3` inside `B(H)`.

### N5 — exhaustion claim refused

Only the adjoint-8-versus-unital-`M_3` route is closed. Other color
constructions are not exhausted.

### N6 — axiom-edit refusal

No axiom sentence is edited. The Qubit one-site `M_2(C)` wording remains
the live parent.

### N7 — adoption refusal

`hypothetical_axiom_status` records the leftover and marks it **not
adopted** as QCD or as unital `M_3`. No fifth axiom named color is
proposed.

### N8 — FAIL / DO NOT SHIP

Do not ship any of the following as consequences of this note:

- “an axiom update is necessary”
- “color is derived from three qubits”
- “`ad(su(3))` is a unital `M_3` summand”
- “the leftover is now axiom content”
- “`Y_0` is hypercharge”

## Live Parent Quote

The only parent on the current public axiom memo is the Qubit one-site
sentence, quoted for non-mutation:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

That sentence names a local algebra. It does not name `su(3)`, Gell-Mann
matrices, a color primitive, QCD, `Y_0`, or hypercharge.

## Runner

[`scripts/su3_adjoint_eight_in_m8_is_not_unital_m3_2026_08_13.py`](../scripts/su3_adjoint_eight_in_m8_is_not_unital_m3_2026_08_13.py)
reconstructs the Gell-Mann matrices and the standard `f_abc` over
`Q(√3)`, checks Theorems 1–5, requires the three hostile predicates to
fail, and checks that this note and the axiom memo carry the leftover
wording rather than a QCD or unital-`M_3` identification.
