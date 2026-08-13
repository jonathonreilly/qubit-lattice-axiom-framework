---
claim_id: m2_tensor_sum_class_has_no_unital_m3_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The smallest class C of finite-dimensional unital C*-algebras containing M_2(C) and closed under finite tensor product and finite direct sum consists exactly of finite direct sums of matrix algebras of power-of-two size. Unital M_3(C) does not embed into any object of C, because a unital *-hom from the simple algebra M_3 factors through a unital *-hom into one summand M_{2^k}, which exists if and only if 3 divides 2^k. The result is a hypothetical C2-strong composite-class test. It does not adopt that class as a Qubit rewrite, does not declare a larger carrier, and does not identify M_3 with QCD."
upstream_dependencies:
  - minimal_axioms
runner: scripts/m2_tensor_sum_class_has_no_unital_m3_hypothetical_2026_08_13.py
---

# The `M_2` Tensor/Sum Class Has No Unital `M_3`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact finite-dimensional unital `C*`-algebra arithmetic for the
class generated from one-site `M_2(C)` by finite tensor product and finite
direct sum.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/m2_tensor_sum_class_has_no_unital_m3_hypothetical_2026_08_13.py`](../scripts/m2_tensor_sum_class_has_no_unital_m3_hypothetical_2026_08_13.py)

## Result Up Front

Current Qubit names one local possibility algebra: `M_2(C)`. A leftover C2
reading says that a physical object may still be a finite composite built from
that local algebra by tensor and direct sum. Let `C` be exactly that generated
class. Every object of `C` is `*-isomorphic` to a finite direct sum of matrix
algebras whose sizes are powers of two. Unital `M_3` does not sit in any such
object.

Color, read here as a unital copy of `M_3`, is therefore not an expected
construction on this class. The remaining C2 escape is a *declared* larger
carrier — a different type — not a Lattice+Qubit composite in `C`. That
declaration is displayed and not adopted. QCD is not imported. No axiom is
edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The class form and the unital-division obstruction are proved on declared finite-dimensional C*-algebras generated from M_2 by finite tensor and finite direct sum. Adoption of that composite class as a Qubit rewrite, and any declared larger carrier, remain open and are not taken."
trace_class: negative_route_pruning
target_claim_id: c2_m2_tensor_sum_class_hosts_unital_m3
target_blocker_text: "maybe some mix of tensor and direct sum of M_2 hosts unital M_3"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the generated tensor/sum class C; a declared larger carrier remains a different type and is not adopted"
hypothetical_axiom_status: "C2-strong: composites are the class generated from M_2 by finite tensor and finite direct sum; not adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Independent audit remains required before any effective status may change. No
canonical axiom edit.

## Exact Objects

The current Qubit sentence, quoted from
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), is:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Write `A2 = M_2(C)` and `A3 = M_3(C)`. Complex dimensions are
`dim_C(A2) = 2^2 = 4` and `dim_C(A3) = 3^2 = 9`.

Let `C` be the smallest class of finite-dimensional unital `C*`-algebras such
that `M_2(C) ∈ C` and `C` is closed under finite tensor product and finite
direct sum.

Tensor of matrix algebras multiplies sizes:
`M_a ⊗ M_b ≅ M_{ab}`. Direct sum concatenates summands:
`M_a ⊕ M_b` is the indicated two-summand algebra. Starting from `M_2` and
closing under those operations, every object of `C` is `*-isomorphic` to

```text
M_{2^{k_1}} ⊕ ⋯ ⊕ M_{2^{k_r}}
```

for some `r ≥ 1` and integers `k_i ≥ 1`. No odd prime appears as a matrix
size.

A unital `C`-linear `*-homomorphism` `M_k → M_m` exists if and only if `k`
divides `m`: the standard module `C^m` becomes a unital left `M_k`-module, so
it is a multiple of `C^k`.

`A3` is simple: its only closed two-sided ideals are `0` and itself. A unital
`*-hom` `φ : M_3 → ⊕_i M_{2^{k_i}}` therefore cannot have nontrivial kernel.
Composing with a coordinate projection `π_i` yields a `*-hom`
`π_i ∘ φ : M_3 → M_{2^{k_i}}`. Unitality of `φ` sends the unit to the unit
`(1,…,1)` of the sum, so some (in fact each) component is a unital `*-hom`
`M_3 → M_{2^{k}}`. That map exists if and only if `3 | 2^{k}`, which is false
for every integer `k ≥ 1`.

The displayed C2-strong sentence `S'` (not adopted) is: local algebra is
`M_2`; a physical object may be any member of the generated class `C`.

The remaining displayed leftover `S''` (not adopted) is: there is also a
declared one-object algebra `M_3(C)` of a different type, not required to lie
in `C`.

## Theorem 1 — four witnesses in `C`

The following four objects lie in `C` and have only power-of-two matrix
summand sizes.

| Witness | Construction | Summand sizes | `dim_C` |
|---|---|---|---|
| `M_2` | generator | `2` | `4` |
| `M_2 ⊗ M_2 ≅ M_4` | finite tensor | `4` | `16` |
| `M_2 ⊕ M_2` | finite direct sum | `2, 2` | `8` |
| `M_4 ⊕ M_2` | tensor then sum | `4, 2` | `20` |

The concatenated summand-size list is `{2, 4, 2, 4, 2}`. Each entry is a
positive power of two.

## Theorem 2 — no unital `M_3` into the four witnesses

`3` divides none of `{2, 4, 2, 4, 2}`. Therefore there is no unital `*-hom`
`M_3 → M_2`, none `M_3 → M_4`, and, by the simplicity factoring of the
previous section, none into `M_2 ⊕ M_2` or `M_4 ⊕ M_2`.

Separately, `M_2 ⊕ M_2` is not `*-isomorphic` to `M_3`: the complex dimensions
are `8` and `9`.

## Theorem 3 — the obstruction is the whole class

The same division obstruction holds for every object of `C`. Any
`X ∈ C` is `*-isomorphic` to `⊕_i M_{2^{k_i}}` with each `k_i ≥ 1`. A unital
`*-hom` `M_3 → X` would yield a unital `*-hom` `M_3 → M_{2^{k}}` for some `k`,
hence `3 | 2^{k}`. No such `k` exists.

Unital `M_3` is not an expected construction on this class. The leftover C2
escape after tensor and sum is therefore a declared larger carrier (`S''`),
not a Lattice+Qubit composite in `C`. `S'` and `S''` are displayed only.
Neither is adopted. Neither is a Qubit rewrite. `A3` is not identified with
QCD.

## No-Go Discipline

### N1 — materially distinct routes

| Route | Status here |
|---|---|
| one-site unital `M_3 → M_2` | closed: `3 ∤ 2` |
| finite tensor of `M_2` | closed: sizes `2^n`, and `3 ∤ 2^n` |
| finite direct sum of `M_2` | closed: simplicity factors through a summand |
| mixed finite tensor and finite direct sum (the class `C`) | closed by Theorems 1–3 |
| declared larger carrier `S''` | a different type; displayed; not adopted |

### N2 — wall independence and collapse

The tensor obstruction (`3 ∤ 2^k`) and the sum obstruction (simplicity plus
unital factoring) are independent elementary facts. Their join is not a new
mechanism: it is the inductive closure of those two operations. Collapsing
them into a slogan “composites can be anything” would hide that `C` is a
specific class.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `C` | explicit generated class; not present in the current axioms |
| `S'` | displayed C2-strong reading; not adopted |
| `S''` | displayed leftover declaration of a larger carrier; not adopted |
| unital `*-hom` | the only embedding type tested |
| non-unital maps, corners, essential ideals | not claimed to be absent; not the C2 composite reading under test |
| QCD, `SU(3)`, running couplings | not used |
| observations or fitted constants | none |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | one-site possibility domain `M_2(C)` | exact current Qubit wording only; no composite class is borrowed from the memo |

No unmerged parent is cited. The class form and the division facts are proved
here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | four explicit witnesses and the concatenated size list `{2,4,2,4,2}` | no classification of every C*-algebra |
| per site | local algebra remains `M_2` | no multi-site dynamics |
| per mode | every finite tensor/sum word in `C` | no claim about objects outside `C` |
| per block | unital `M_3` into `C` | no QCD identification |
| lattice-wide | not executed | no lattice-wide color construction |

### N6 — live partial-closure paths

1. A later construction could place unital `M_3` in an object *not* in `C`.
2. A declared larger carrier (`S''`) could be proposed as an extra object.
   That is a different type, not a theorem of Lattice+Qubit+`S'`.
3. A non-unital or corner embedding is a different mathematical question and
   is not the unital composite reading tested here.

None of those paths is taken here. An owner-approved extra object would still
be an extra object.

### N7 — hostile steelman

> Perhaps no single tensor power and no single direct sum of `M_2` hosts
> unital `M_3`, but some mixed word in tensor and direct sum does. The
> generated class might be larger than the obvious power-of-two sums, or
> simplicity might fail to force a unital map into one summand.

The class form answers the first half: every mixed word reduces to
`⊕_i M_{2^{k_i}}`. Simplicity plus unitality answers the second half. The
steelman is the claim under test, and it fails on `C`.

### N8 — cross-cycle echo

Earlier C2 readings that treat “full” as local-only, and that allow
composites, still have to name the composite *type*. Tensor alone and sum
alone are two types. Their generated mix is a third named type, and it is
still power-of-two matrix sums. Cross-cycle movement does not turn `S''` into
a theorem.

**Gate disposition:** PASS for (i) the four witnesses lie in `C` with only
power-of-two summand sizes, (ii) `3` divides none of those sizes, and
(iii) the same obstruction holds for every object of `C`. FAIL / DO NOT SHIP
for “an axiom update is necessary,” “QCD is derived,” “every larger algebra is
impossible,” or “the leftover declaration `S''` is adopted.”

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Qubit sentence | local algebra `M_2(C)` | supplied; no edit |
| generated class `C` | hypothetical C2-strong composite type | displayed; not adopted |
| unital division criterion | Theorem 2 and Theorem 3 | definition-level matrix algebra |
| simplicity of `M_3` | factoring through a summand | standard `C*`-algebra fact used here |
| declared larger carrier `S''` | leftover type after `C` | displayed; not adopted |
| QCD / color gauge physics | none | not imported |
| Qubit rewrite | none | not adopted |

## Review Record

Parents on `origin/main` are the axiom memo only. Independent audit remains
required. No `review-loop` was invoked in producing or self-reviewing this
artifact.
