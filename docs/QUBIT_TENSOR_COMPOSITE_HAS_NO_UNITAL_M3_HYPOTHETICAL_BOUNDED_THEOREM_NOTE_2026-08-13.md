---
claim_id: qubit_tensor_composite_has_no_unital_m3_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the hypothetical C2-strong leftover that the one-site algebra is M_2(C) while a physical object may be a finite tensor of sites, a unital C-linear *-homomorphism M_3(C) -> M_{2^n}(C) never exists, because 3 never divides 2^n. Color is not an expected construction of that composite type. The leftover is not adopted. No fifth axiom is named. A3 is not identified with QCD."
upstream_dependencies:
  - minimal_axioms
runner: scripts/qubit_tensor_composite_has_no_unital_m3_hypothetical_2026_08_13.py
---

# Qubit Tensor Composite Has No Unital M_3

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact unital-divisibility obstruction for `M_3(C)` inside a finite
tensor of one-site `M_2(C)` algebras. Dimensions are reconstructed here.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/qubit_tensor_composite_has_no_unital_m3_hypothetical_2026_08_13.py`](../scripts/qubit_tensor_composite_has_no_unital_m3_hypothetical_2026_08_13.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

The live Qubit wording supplies one-site algebra `M_2(C)`. A leftover
C2-strong reading says “full means local only; composites allowed,” so a
physical object may be a finite tensor of sites. That reading is **not
adopted**. Even if it were granted for the sake of the leftover, it does
**not** by itself make color an expected construction when “composite”
means a finite tensor of sites.

Let `A2 = M_2(C)` and `A3 = M_3(C)`. Reconstruct the dimensions from the
matrix size: `dim_C(A2) = 2^2 = 4` and `dim_C(A3) = 3^2 = 9`. The n-site
tensor composite is

`T_n = A2^{⊗ n} ≅ M_{2^n}(C)`,

so the matrix size is `d_n = 2^n` and `dim_C(T_n) = (2^n)^2 = 4^n`.

A unital C-linear *-homomorphism `φ : M_k(C) → M_m(C)` exists if and only
if `k` divides `m`. Reason: `M_m` becomes a unital left `M_k`-module of
C-dimension `m^2 / k`, equivalently the standard module `C^m` is a
multiple of `C^k`, so `k | m`.

For every `n ≥ 1`, `d_n = 2^n` is a power of two, hence `3 ∤ 2^n`. There
is therefore no unital *-homomorphism `A3 → T_n`. Unital `M_3` never sits
inside a finite tensor of one-site `M_2`. On that composite type, `A3`
remains extra.

This note does not rewrite the Qubit axiom. It does not adopt a fifth
axiom named color. It does not identify `A3` with QCD.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer reconstruction of dim A2, dim A3, and d_n=2^n, plus the divisibility obstruction 3 never divides 2^n, are proved on declared finite matrix algebras. Adoption of the C2-strong composite leftover, a color axiom, and any QCD identification remain open and are refused here."
trace_class: negative_route_pruning
target_claim_id: c2_strong_tensor_composite_unital_m3
target_blocker_text: "does a C2-strong finite-tensor composite of M_2 sites make unital M_3, or color, an expected construction"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for unital *-homs A3 -> T_n on finite n; other composite types remain unclaimed"
hypothetical_axiom_status: "C2-strong tensor composite: local algebra M_2; physical object may be a finite tensor of sites; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Reconstruct the finite matrix dimensions from first principles. Write
`M_k(C)` for k-by-k complex matrices. Then `dim_C(M_k(C)) = k^2`.

- `A2 = M_2(C)`, so `dim_C(A2) = 4`.
- `A3 = M_3(C)`, so `dim_C(A3) = 9`.
- For `n ≥ 1`, `T_n = A2^{⊗ n} ≅ M_{2^n}(C)`.
- Matrix size `d_n = 2^n`. Explicit values used below:
  `n=1,2,3,4` give `d_n = 2,4,8,16`.
- `dim_C(T_n) = d_n^2 = 4^n`.

A unital C-linear *-homomorphism of finite type-I factors
`φ : M_k(C) → M_m(C)` exists if and only if `k | m`. The image of the
standard representation `C^k` must occupy a subspace of `C^m` of
dimension a multiple of `k`, equivalently `M_m` is a unital left
`M_k`-module of C-dimension `m^2 / k`.

Positive control, not a color construction: `2 | 2^n` for every `n ≥ 1`,
so a unital *-hom `A2 → T_n` exists (the standard inclusion
`X ↦ X ⊗ I_{2^{n-1}}`). The obstruction below is special to `k = 3`.

## Theorem 1 — identity dimensions

`dim_C(A2) = 4`, `dim_C(A3) = 9`, and `d_n = 2^n` for
`n = 1,2,3,4` (`2,4,8,16`). These are identities of finite matrix
algebras, reconstructed here from `dim_C(M_k) = k^2` and
`M_2^{⊗ n} ≅ M_{2^n}`. They are not imported from a QCD package and
they do not rewrite the live Qubit sentence.

The companion runner implements `dim_m2()`, `dim_m3()`, and
`matrix_size(n)` as exact integers.

## Theorem 2 — finite check, n = 1,2,3,4

For each `n ∈ {1,2,3,4}`, the integer remainder `2^n mod 3` is nonzero:

| n | d_n = 2^n | 2^n mod 3 |
|---|----------:|----------:|
| 1 | 2 | 2 |
| 2 | 4 | 1 |
| 3 | 8 | 2 |
| 4 | 16 | 1 |

Therefore `3` does not divide `2^n`, so there is no unital *-homomorphism
`A3 → T_n` for these n. The check is exact integer `%`, not a float
tolerance.

## Theorem 3 — every finite n

For every `n ≥ 1`, `2^n` is a power of two. The only prime dividing
`2^n` is `2`. In particular `3 ∤ 2^n`. Hence unital `M_3` never sits
inside a finite tensor of one-site `M_2`.

The companion runner implements `three_never_divides_power_of_two(N)`
and evaluates it at `N = 8` (the range `n = 1..8`). The same remainder
argument covers every larger finite `N`.

## Theorem 4 — C2-strong leftover does not expect color

The leftover C2 reading “full means local only; composites allowed”
does **not** by itself make color an expected construction, if
“composite” means a finite tensor of sites. Theorems 1–3 show that
`A3` has no unital image in any such `T_n`. On that composite type,
A3 remains extra.

This is a type obstruction, not a fifth extra, not a C6/C7 clone, and
not a C1 clone. Displaying the leftover does not adopt it. The live
axiom memo still states only that the full **one-site** possibility
domain has algebraic presentation `M_2(C)`.

Do not adopt a fifth axiom named color. Do not identify `A3` with QCD.

## Mutations

Two hostile predicates must fail.

1. “`3` divides `2^n` for some `n` in `1..8`.” False: every remainder
   `2^n mod 3` on that range is `1` or `2`.
2. “`dim_C(A3) = 4`.” False: reconstructing `3^2` gives `9`, not the
   one-site qubit dimension `4`.

## What This Does Not Claim

- No Qubit rewrite. The live one-site sentence is unchanged.
- No adopted C2-strong axiom. Finite tensors of sites remain a
  hypothetical leftover, not a fifth or restated primitive.
- No color axiom. Naming `A3` as a comparison algebra does not install
  SU(3), a color charge, or a fifth axiom.
- No QCD import and no identification of `A3` with QCD.
- No claim about non-unital embeddings, infinite products, inductive
  limits, or other composite types. The corner pad into a larger matrix
  algebra is a different leftover and is not used here.
- No claim that every unital *-hom between finite matrix algebras has
  been classified beyond the standard divisibility criterion used above.

## No-Go Discipline Gate

The negative claim is only: there is no unital *-hom `A3 → T_n` for
finite n, so the C2-strong finite-tensor leftover does not make unital
`M_3` (or color) expected. The gate does not certify that every
composite construction is impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Unital *-hom into T_n | require 3 | 2^n | Theorems 2–3: 3 never divides 2^n | **ATTEMPTED** |
| Dimension coincidence | set dim A3 = dim A2 | mutation: 9 ≠ 4 | **ATTEMPTED** |
| Finite n = 1..4 table | integer remainder | Theorem 2 table, all nonzero | **ATTEMPTED** |
| C2-strong leftover as expectation | “composites allowed” implies color | Theorem 4: leftover does not make color expected | **ATTEMPTED** |
| Adopt a color axiom | name a fifth primitive | refused; leftover not adopted | **CLOSED HERE** |
| Identify A3 with QCD | treat A3 as QCD | refused; no QCD content | **CLOSED HERE** |
| Rewrite Qubit to M_3 | change the one-site algebra | refused; live memo unchanged | **CLOSED HERE** |
| Other composite types | non-unital pad, infinite product | not claimed | **LIVE / OUT OF SCOPE** |

The broad statement “the axioms cannot derive color by any route” is
not shipped.

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| dim A3 = 9 / 3 ∤ 2^n | no: a dimension does not decide divisibility of matrix size | no: non-divisibility does not compute 3^2 | independent identities |
| finite table n=1..4 / all n ≥ 1 | the table is the finite special case | the prime argument covers the table | special case / general case |
| unital obstruction / non-unital pad | no: Theorems 2–3 are unital | no: a non-unital corner is a different type | independent leftover |
| leftover display / axiom adoption | no: Theorem 4 refuses adoption | no: the live memo does not name T_n | leftover remains hypothetical |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `A2`, `A3`, `T_n`, `d_n` | reconstructed finite matrix objects |
| unital C-linear *-hom | standard finite-factor criterion `k | m` |
| C2-strong leftover | explicit hypothetical reading; not adopted |
| color / QCD | comparison language only; not identified |
| observations or fitted constants | none |
| float approximations | none; integer remainder only |

### N4 — hostile counter-reading

A reader might say: “composites are allowed, `T_2 ≅ M_4` is larger than
`M_3`, so color sits inside two qubits.” Matrix-size comparison is not
unital inclusion. `3 ∤ 4`, so there is still no unital *-hom
`M_3 → M_4`. The extra dimension `16 - 9 = 7` does not create a unital
copy of `A3`.

### N5 — exhaustion claim refused

Only the unital finite-tensor route is closed. Other composite types
are not exhausted.

### N6 — axiom-edit refusal

No axiom sentence is edited. The Qubit one-site `M_2(C)` wording remains
the live parent.

### N7 — adoption refusal

`hypothetical_axiom_status` records the leftover and marks it
**not adopted**. No fifth axiom named color is proposed.

### N8 — FAIL / DO NOT SHIP

Do not ship any of the following as consequences of this note:

- “an axiom update is necessary”
- “color is derived from finite qubit tensors”
- “`A3` is QCD”
- “the C2-strong leftover is now axiom content”

## Live Parent Quote

The only parent on the current public axiom memo is the Qubit
one-site sentence, quoted for non-mutation:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

That sentence names a local algebra. It does not name `M_3`, a finite
tensor composite as axiom content, a color primitive, or QCD.
