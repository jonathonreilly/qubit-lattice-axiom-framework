---
claim_id: two_site_factor_swap_uniquely_names_rank3_corner_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On H=C^2⊗C^2 the factor-swap F is the unique linear map sending |i⟩⊗|j⟩ to |j⟩⊗|i⟩. It is a Hermitian involution with Tr(F)=2 and Ad_F(X⊗I)=I⊗X. The Hermitian involutions implementing that factor swap on the displayed generators are exactly ±F. The unique rank-3 spectral projection of F is p_+=(I+F)/2. This leftover is not adopted as color, SU(3), or QCD, and does not rewrite Qubit."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_site_factor_swap_uniquely_names_rank3_corner_2026_08_13.py
---

# Two-Site Factor-Swap Uniquely Names A Rank-3 Corner

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact Fraction identities for the two-site factor-swap on
`H = C^2 ⊗ C^2` and the rank-3 spectral projection of `F`.
No QCD. No Qubit rewrite. `F` is displayed, not axiom content.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_site_factor_swap_uniquely_names_rank3_corner_2026_08_13.py`](../scripts/two_site_factor_swap_uniquely_names_rank3_corner_2026_08_13.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `H = C^2 ⊗ C^2` with product basis `|00>, |01>, |10>, |11>`.
The factor-swap is the unique linear map `F : H → H` with
`F(|i⟩ ⊗ |j⟩) = |j⟩ ⊗ |i⟩` on that basis. In the product basis

```text
F = ((1,0,0,0), (0,0,1,0), (0,1,0,0), (0,0,0,1)).
```

`F` is Hermitian, `F^2 = I_4`, and `Tr(F) = 2`. Conjugation implements
the algebra automorphism that exchanges tensor factors:
`Ad_F(X ⊗ I_2) = I_2 ⊗ X` and `Ad_F(I_2 ⊗ X) = X ⊗ I_2`.

Any Hermitian involution that implements that swap on the generators
`{E_00, E_01}` is exactly `F` or `−F`. The unique rank-3 spectral
projection of `F` is `p_+ = (I_4 + F)/2`. The complementary
`p_- = (I_4 − F)/2` has rank 1. The corner unit is `p_+`, not `I_4`.

Qubit still names one-site `M_2(C)`. This leftover is not color, not
`SU(3)`, and not QCD.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Fraction identities uniquely name the two-site factor-swap and its rank-3 spectral projection. Color, SU(3), and QCD remain unadopted."
trace_class: negative_route_pruning
target_claim_id: two_site_factor_swap_uniquely_names_rank3_corner
target_blocker_text: "what uniquely names the rank-3 corner projector in the two-site tensor"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed factor-swap on T_2 ≅ M_4; other involutions and multi-site hosts remain unclaimed"
hypothetical_axiom_status: "factor-swap leftover: unique F names p=(I+F)/2; not adopted as color"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

All entries are exact `Fraction` values. No float is used.

The live Qubit sentence, quoted and not rewritten:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Write `T_2 = B(H) ≅ M_2(C) ⊗ M_2(C) ≅ M_4(C)`.
Matrix units of `M_2(C)` are `E_ij = |i⟩⟨j|`. Kronecker products are
the standard product-basis embeddings. `Ad_F(Z) := F Z F` because
`F^{-1} = F^* = F`.

`p_+ = (I_4 + F)/2` and `p_- = (I_4 − F)/2` are the spectral
projections of the Hermitian involution `F`.

## Theorem 1 — `F` is a Hermitian involution of trace 2

Direct matrix arithmetic: `F^* = F`, `F^2 = I_4`, `Tr(F) = 2`.

## Theorem 2 — `Ad_F` exchanges tensor factors

For `X ∈ {E_00, E_01, σ_x, σ_z}`,

```text
F (X ⊗ I_2) F = I_2 ⊗ X,    F (I_2 ⊗ X) F = X ⊗ I_2.
```

The identities extend by linearity to all of `M_2(C)`.

## Theorem 3 — uniqueness of the linear swap

If `G : H → H` is linear and `G(|i⟩ ⊗ |j⟩) = |j⟩ ⊗ |i⟩` on the four
basis vectors, then `G = F`. The four images fix the matrix.

## Theorem 4 — Hermitian involutions implementing the swap

Let `U` be a real-symmetric `4 × 4` matrix of exact Fractions with
`U^2 = I_4` and

```text
U (E_00 ⊗ I_2) = (I_2 ⊗ E_00) U,
U (E_01 ⊗ I_2) = (I_2 ⊗ E_01) U.
```

The companion runner row-reduces the linear intertwining system on
the 10-dimensional space of real-symmetric `4 × 4` matrices and then
imposes `U^2 = I_4`. The only solutions are `U = F` and `U = −F`.

Both work: `(−F)(X ⊗ I)(−F) = F(X ⊗ I)F`. They are distinct:
`F ≠ −F`.

## Theorem 5 — unique rank-3 spectral projection

`p_+ = (I_4 + F)/2` is an orthogonal projection of rank 3.
`p_- = (I_4 − F)/2` is an orthogonal projection of rank 1.
So the unique rank-3 spectral projection of `F` is `p_+`.
It is not `I_4`. The corner `p_+ T_2 p_+` is unital with unit `p_+`.

## Theorem 6 — no color, no Qubit rewrite

This note does not install `SU(3)`, name QCD, select color, or rewrite
Qubit. `F` is a displayed two-site map, not axiom content. No fifth
axiom is named.

## Mutations

Three hostile predicates must fail.

1. “`F == −F`.” False: `Tr(F) = 2 ≠ −2`.
2. “`rank(p_+) == 1`.” False: rank is 3.
3. “`p_+ == I_4`.” False: `p_+ ≠ I_4`.

## What This Does Not Claim

- No Qubit rewrite. The live one-site algebra remains `M_2(C)`.
- No color axiom, no `SU(3)`, and no QCD identification.
- No claim that Record locks `p_+` or that Admissibility selects `F`.
- No claim about other involutions that do not implement the factor swap.
- No unital `M_3` factor of `T_2` (the inclusion of the corner is not unital).
- Independent class-`C` leftovers are not used as parents.

## No-Go Discipline Gate

The negative claim is only: among Hermitian involutions implementing
the displayed factor swap, `±F` are the solutions, and `F` names a
unique rank-3 corner unit. The gate does not certify that color is
derived or impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| Linear swap on basis | four images | Theorem 3: `G = F` | **ATTEMPTED** |
| Algebra automorphism | `Ad_F` on `E_00`, `E_01` | Theorem 2 | **ATTEMPTED** |
| Other Hermitian involutions | real-symmetric `U^2=I` + intertwining | Theorem 4: only `±F` | **ATTEMPTED** |
| Rank-3 from `−F` | `p` of `−F` | that projector is `p_-`, rank 1 | **ATTEMPTED** |
| `p_+ = I_4` | unital factor | mutation fails | **ATTEMPTED** |
| Adopt `F` as axiom | rewrite Qubit / Lattice | refused | **CLOSED HERE** |
| Install QCD / `SU(3)` | treat `p_+` as color | refused | **CLOSED HERE** |
| Other hosts / more sites | different involutions | not claimed | **LIVE / OUT OF SCOPE** |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| linear uniqueness / Hermitian uniqueness | no: a basis map does not classify involutions | no: `±F` uses the linear `F` | independent |
| rank-3 / unital factor | no: rank does not force `p_+=I` | no | type separation |
| leftover / QCD | no | no | leftover remains hypothetical |

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| product basis of `C^2 ⊗ C^2` | displayed |
| real-symmetric restriction in Theorem 4 | explicit finite search domain; complex-Hermitian leftover named out of scope |
| color / QCD / `SU(3)` | comparison language only |
| float | none |

### N4 — hostile counter-reading

A reader might say: “uniqueness of `F` selects color.” Uniqueness of
the two-site swap names a projector. It does not name a QCD factor,
a gauge group, or a record label.

### N5 — exhaustion claim refused

Only the displayed factor-swap on `T_2` is classified. Other
involutions and other hosts are not exhausted.

### N6 — axiom-edit refusal

No axiom sentence is edited.

### N7 — adoption refusal

`hypothetical_axiom_status` records the leftover and marks it
**not adopted as color**.

### N8 — FAIL / DO NOT SHIP

Do not ship any of the following as consequences of this note:

- "an axiom update is necessary"
- “the factor-swap is now QCD”
- “`p_+` is a unital `M_3` factor of `T_2`”
- “Qubit is `M_3`”
- “`F` is axiom content”

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Those sentences name a local algebra and a lock rule. They do not name
a two-site swap, a corner projector, `SU(3)`, or QCD.

## Runner Contract

The companion runner checks Theorems 1–5 on exact Fractions, rejects
the three mutation predicates, quotes the live axiom sentences, and
records the non-claims. Declared audit inputs are this note and the
axiom memo only.
