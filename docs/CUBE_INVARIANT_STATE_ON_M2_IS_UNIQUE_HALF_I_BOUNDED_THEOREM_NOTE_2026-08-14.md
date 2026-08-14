---
claim_id: cube_invariant_state_on_m2_is_unique_half_i_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On one-site M_2(C), the unique G-invariant state under the displayed faithful proper cubic action α is I_2/2. Uniqueness is conditional on the displayed faithful action. I_2/2 is the unique G-invariant candidate reference state and is not adopted as Born. No axiom text, kernel, menu, or formation rule is added."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_invariant_state_on_m2_is_unique_half_i_2026_08_14.py
---

# The Unique `G`-Invariant State on `M_2` Is `I_2/2`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact Bloch-vector uniqueness for one-site density matrices
under the displayed faithful proper cubic action. Uniqueness is
conditional on the displayed faithful action. `I_2/2` is exhibited as
the unique `G`-invariant candidate reference state and is not adopted
as Born.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_invariant_state_on_m2_is_unique_half_i_2026_08_14.py`](../scripts/cube_invariant_state_on_m2_is_unique_half_i_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Work in one-site `M_2(C)`. Density matrices have the Bloch form

```text
ρ(n) = (I_2 + n_x σ_x + n_y σ_y + n_z σ_z) / 2,
```

with rational Bloch coordinates satisfying `|n|^2 ≤ 1`. Let `G` be the
proper cubic rotation group (24 integer `3 × 3` matrices of determinant
`+1` that permute the coordinate axes up to signs). The displayed
faithful action is the standard module action

```text
Rx = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
α_R(σ_j) = Σ_i R_{ij} σ_i,
```

which implies `α_R(ρ(n)) = ρ(R n)`. A state `ρ(n)` is `G`-invariant
under `α` if and only if `R n = n` for every `R ∈ G`.

The unique solution is `n = 0`. Therefore `I_2/2` is the unique
`G`-invariant state. The same uniqueness holds for every conjugate
action `β_R = α_S ∘ α_R ∘ α_S^{-1}`: conjugating the action conjugates
the fixed-vector equation, and still only `0` is fixed by all of `G`.

This is uniqueness of the invariant state, conditional on the displayed
faithful action. The leftover is the nearest-neighbor-dependent kernel,
formation, and menu — not a second invariant state. `I_2/2` is the
unique `G`-invariant candidate reference state and is not adopted as
Born.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Q(i)/Fraction identities and integer 3x3 linear algebra show that the only Bloch vector fixed by the displayed faithful proper cubic action is 0, so I_2/2 is the unique G-invariant state. The statement is conditional on that displayed action and is not a Born adoption."
trace_class: frontier_discovery
target_claim_id: cube_invariant_state_on_m2_is_unique_half_i
target_blocker_text: "whether a faithful cube action still leaves a free choice of G-invariant one-site reference state"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded uniqueness claim; kernel form, menu, and formation remain separate"
conditional_surface_status: "exact uniqueness of the G-invariant state on one-site M_2(C) conditional on the displayed faithful action; no Born, kernel, menu, or formation claim"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the one-site `M_2(C)` possibility algebra, the nearest-neighbor
  Admissibility distribution clause, and the Record locking/readability
  sentences. As the registered `minimal_axioms` premise, it is not a
  bounded-status source.
- The group `G` and the action `α` are displayed mathematical data for
  this theorem. They are reconstructed locally from the integer cube
  rotations and the Pauli module; they are not imported as a named
  extra parent.
- No measured, fitted, observational, literature, scale, or other
  phenomenological value is used.

## Exact Objects

Entries live in the Gaussian field `Q(i)` with `i^2 = -1`. Pauli
matrices and Bloch coordinates use exact `Fraction` coefficients.
Cube rotations are integer `3 × 3` matrices.

```text
σ_x = ((0, 1), (1, 0))
σ_y = ((0, -i), (i, 0))
σ_z = ((1, 0), (0, -1))
Rx  = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
Rz  = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
```

`Rx` sends `(x, y, z)` to `(x, -z, y)`. `Rz` sends `(x, y, z)` to
`(-y, x, z)`. The live Qubit sentence, quoted and not rewritten:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

## Theorem 1 — the zero Bloch vector is invariant

`R 0 = 0` for every `R ∈ G`, so `n = 0` is invariant. The
corresponding state is

```text
ρ(0) = I_2 / 2.
```

## Theorem 2 — a nonzero Bloch vector is moved by some `R ∈ G`

Let `n = (n_x, n_y, n_z)` have rational coordinates, not all zero.

- If `n_y ≠ 0` or `n_z ≠ 0`, then `Rx n = (n_x, -n_z, n_y) ≠ n`.
- If `n = (c, 0, 0)` with `c ≠ 0`, then `Rz n = (0, c, 0) ≠ n`.

Hence no nonzero vector is fixed by all of `G`. Equivalently, the
common `+1` eigenspace of `G` on `Q^3` is `{0}`: stacking `R − I_3`
over `G` and row-reducing over `Q` yields three pivots.

Restricting to Bloch vectors with `|n|^2 ≤ 1` does not add a second
fixed point. The only invariant Bloch vector is `0`.

## Theorem 3 — unique invariant state, and the same after conjugation

A state is `G`-invariant under `α` if and only if its Bloch vector is
fixed by every `R ∈ G`. Theorems 1 and 2 therefore give a unique
`α`-invariant state: `I_2/2`.

The action is faithful: `α_R` is the identity on `M_2(C)` if and only
if `R = I_3`. The same uniqueness holds for every conjugate action
`β_R = α_S ∘ α_R ∘ α_S^{-1}`. On Bloch vectors this is the conjugate
group `{S R S^{-1}}`, whose common fixed space is `S` applied to the
fixed space of `G`, hence still `{0}`.

## Theorem 4 — live Admissibility and Record do not name `I_2/2`

Quoted Admissibility (distribution exists and is nearest-neighbor
determined; form and values are not specified):

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Quoted Record (locks one admissible possibility; only records readable):

> When present, a record locks exactly one admissible local possibility.

> Only records are readable.

Those sentences do not name `I_2/2`, a kernel, or Born weights. This
note displays `I_2/2` as the unique `G`-invariant candidate reference
state, conditional on the displayed faithful action `α`. It is not
adopted as Born. Record does not select it.

## Theorem 5 — a non-invariant control, not the load-bearing cut

The displayed alternative

```text
ρ(ê_z) = |0⟩⟨0| = (I_2 + σ_z) / 2
```

disagrees with `I_2/2`. It is not `G`-invariant: `Rx ê_z = (0, -1, 0)
≠ ê_z`, so `α_{Rx}(ρ(ê_z)) = ρ(ê_y with a sign) ≠ ρ(ê_z)`.

That disagreement is not the load-bearing cut. The load-bearing cut is
uniqueness of the invariant state. The alternative is a control that
invariance is discriminating: a perfectly legal one-site state fails
the invariance predicate that isolates `I_2/2`.

## Mutations

1. Predicate "`ρ(ê_z)` is `G`-invariant" fails: `Rx` moves `ê_z`.
2. Predicate "a nonzero `n` is fixed by all of `G`" fails: Theorem 2
   supplies an explicit witness in every nonzero case.
3. Predicate "`I_2/2 ≠ ρ(0)`" fails: both sides are the same matrix.
4. Predicate "live memo names `I/2` or Born as axiom content" fails:
   the four axiom statements do not name those objects.
5. Predicate "note adopts `I/2` as Born" fails: the note states that
   `I_2/2` is not adopted as Born.

## Honest-auditor / Boundary

The honest reading is narrow. Once a faithful cube action on the Pauli
module is supplied, there is not a leftover free choice of invariant
one-site state: the unique `G`-invariant state is `I_2/2`. That is a
linear-algebra fact about Bloch vectors, not a probability law.

The boundary is equally sharp. Uniqueness does not supply the
nearest-neighbor kernel, its numerical values, a finite menu, or a
formation rule. It does not rewrite Qubit. It does not promote `I_2/2`
into axiom text. Finite `G` is the input; a stronger `U(2)`-invariance
statement is a different hypothesis and is not used. Conjugate actions
do not create a second invariant state.

This note authors no audit verdict.

## What This Does Not Claim

- No Qubit rewrite.
- No Born adoption and no axiom edit.
- No derived kernel, menu, or formation rule.
- No claim that Record selects `I_2/2`.
- No `U(2)`-invariance theorem.
- No two-site, composite, or lattice-wide state uniqueness.

## Runner Contract

The companion runner reconstructs `G` and `α` locally over `Q(i)` and
integer `3 × 3` matrices, computes the common fixed space, constructs
`I_2/2` and the `ρ(ê_z)` control, checks the five mutation predicates,
and binds the declared audit inputs to this note and the axiom memo.
Identity gates call `invariant_bloch_vectors()`, `rho_half_i()`, and
`rho_z_is_not_invariant()`.
