---
claim_id: admissibility_rule_frame_attached_four_point_menu_covariant_weights_gibbs_linear_family_and_sequential_support_obstruction_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Under the unsoldered reading of possibility covariance, the two-neighbour finite support S={q, q', -q, -q'} for non-collinear unit records q, q' is Aut-covariant as a set (the four points are distinct iff |q·q'|<1). Aut-covariant probabilities on S are the two-function family with copy mass α(t) on {q, q'} and flip mass γ(t) on {-q, -q'}, t=q·q', 2α+2γ=1, because the 180-degree rotation about the bisector swaps the two neighbours and preserves S. Pair-Gibbs weights exp(β s·(q+q')) lie in that family; at t=0 with e^{2β}=2 the copy mass is 1/3 and the flip mass is 1/6. The linear family (1+λ s·(q+q'))/4 is the same family. The two-outcome Born overlap (1+s·q)/2 on the four-point set takes values 1, 1/2, 0, 1/2, sums to 2, and is not a four-point law; it also ignores q' as a recorded neighbour. Sequential formation cannot be order-blind on a three-site path: the middle's support has two points in the chain (the antipodal pair of the unique recorded neighbour) and four in ends-first (the four-point set of two non-collinear ends). No menu, rule, order, or reading is selected."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.py
---

# Frame-attached four-point menus: the covariant copy/flip family, pair-Gibbs as its one-parameter subfamily, Born is not a four-point law, and sequential formation fails at the support

**Date:** 2026-09-16
**Type:** bounded_theorem
**Scope:** unsoldered Aut-covariant finite two-neighbour supports of the form `{q, q', -q, -q'}` on the pure-state sphere, their covariant probabilities, and sequential products on a three-site path.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.py`](../scripts/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.txt`](../logs/runner-cache/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.txt)

## Result up front

The landed possibility-covariance note on `main` leaves two readings of the
Qubit automorphism group. Under the unsoldered reading, a finite one-neighbour
support is the antipodal pair of the recorded neighbour (any other point
sweeps a circle). The smallest two-neighbour finite support that includes both
neighbours' axes is the four-point set

```text
S(q, q') = {q, q', -q, -q'},
```

four distinct points whenever `q` and `q'` are non-collinear. That set is
Aut-covariant: rotating both neighbours rotates the four points with them.

Aut-covariant probabilities on `S` are not free four-vectors. The 180-degree
rotation about the bisector of `q` and `q'` swaps the two neighbours and
preserves `S`, so the copy masses on `q` and `q'` are equal, and the flip
masses on `-q` and `-q'` are equal. What remains is a **copy mass** `α(t)` and
a **flip mass** `γ(t)` with `t = q·q'` and `2α + 2γ = 1`.

Pair-Gibbs `exp(β s·(q+q'))` restricted to `S` is that family with one
parameter. At orthogonal neighbours (`t = 0`) with `e^{2β}=2` the copy mass is
`1/3` and the flip mass is `1/6`. The linear family `(1 + λ s·(q+q'))/4` is
the same two-function family; `λ = 0` is uniform, `λ = ±1` at `t = 0` are
deterministic copy and deterministic flip.

The two-outcome Born overlap `(1 + s·q)/2` is **not a four-point law**. On
`S` at the orthogonal reference pair it takes the four values `1, 1/2, 0, 1/2`
and **sums to 2**. It is a two-point law on `{q, -q}`, where it is
deterministic copying, and it ignores `q'` as a recorded neighbour. A
nontrivial Born statistic on a generated finite alphabet therefore cannot be
the two-outcome overlap evaluated on this four-point menu.

Sequential formation cannot hide the order even at the level of supports.
On a three-site path, the chain order gives the middle one recorded neighbour,
hence a two-point antipodal support. Ends-first gives the middle two
non-collinear recorded neighbours (Haar-empty ends are non-collinear almost
surely), hence the four-point support. The middle's support has **two points
in the chain and four in ends-first**. The sequential products cannot agree.

The physical formation order is not selected. The note selects neither a
menu, a rule, nor a reading. Open PR #8152 classifies generated supports and
records Born-on-antipodal as deterministic; it is a sibling, not a landed
premise. The four-point set, the weight family, the Gibbs and linear
identifications, the Born sum, and the support obstruction are proved here.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Aut-covariant four-point weights, Gibbs/linear identification, Born sum, and path3 support cardinalities are exact. No menu, rule, or reading is selected."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the Born form on unsoldered frame-attached supports, and whether sequential formation can be order-blind on generated finite alphabets"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "three-or-more recorded neighbours in special position; mixed-state domains"
conditional_surface_status: "exact on the four-point menu and on one three-site path; no infinite-volume statement; no physical-law selection"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared objects

Scientific dependencies: the current four-axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the landed possibility-covariance note
[`POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md).
Sentences used, verbatim:

- Qubit: "No possibility is privileged. Possibilities are distinguished by
  the supplied algebraic structure alone."
- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and
  "For each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form."

The unsoldered reading is the landed note's: internal `SO(3)` acts on
possibility values independently of the 24 proper cubic rotations of the
lattice. This note does not adopt that reading as physical; it computes
inside it.

Declared scaffolding: unit vectors in `S^2`; the four-point set `S(q, q')`;
pair-Gibbs as a named one-parameter subfamily, not as an imported
Hamiltonian of the framework; sequential products on a three-site path
with the records-only reading.

## Exact target

Classify Aut-covariant probabilities on `S(q, q')`, identify pair-Gibbs and
the linear family inside that classification, show that the two-outcome Born
overlap is not a four-point law, and show that sequential formation on a
three-site path fails already at the support.

## Prior art and what is new

The landed possibility-covariance note supplies the two readings and the
uniform empty-neighbourhood law under unsoldered Aut. The open menus note
(PR #8152) classifies one-neighbour finite supports as antipodal, two-neighbour
supports as frame-attached, and records that Born on the antipodal pair is
deterministic; it lists "the Born form on frame-attached supports" as open
and is not a premise of the proofs below.

New here: the two-function copy/flip family on the four-point menu; the
exact Gibbs masses `1/3` and `1/6` at `t = 0`, `e^{2β}=2`; the identification
of the linear family; the Born four-tuple summing to 2; the path3 support
cardinalities 2 versus 4.

## Proof-obligation graph

| obligation | disposition |
|---|---|
| `S(q, q')` is Aut-covariant and four-distinct iff non-collinear | proved; executed at the orthogonal reference pair |
| Aut plus the bisector 180-degree swap forces copy=copy, flip=flip | proved; executed |
| pair-Gibbs lies in the two-function family | exact masses at `t = 0` |
| Born four-tuple sums to 2 | executed |
| chain support 2, ends-first support 4 | executed on `q = e_z`, `q' = e_x` |
| collinear control collapses to 2 | executed |
| select a physical menu or reading | not claimed |

## Theorem 1 — the four-point set is Aut-covariant

Let `q, q'` be unit vectors. The set `S(q, q') = {q, q', -q, -q'}` satisfies
`S(g q, g q') = g S(q, q')` for every `g ∈ SO(3)`. The four points are
distinct iff `|q · q'| < 1`. Executed: `q = (0,0,1)`, `q' = (1,0,0)` have
inner product 0 and four distinct points.

## Theorem 2 — covariant weights are copy mass and flip mass

An Aut-covariant probability on `S` is determined by its value at one pair
per inner product `t`. The 180-degree rotation about the bisector of `q` and
`q'` (for the orthogonal reference: `(x,y,z) ↦ (z, -y, x)`) swaps `q` with
`q'` and preserves `S`. Hence the mass at `q` equals the mass at `q'` (the
**copy mass** `α(t)`), and the mass at `-q` equals the mass at `-q'` (the
**flip mass** `γ(t)`), with `2α + 2γ = 1` and `α, γ ≥ 0`. The 180-degree
rotation about `q` sends `q'` to `-q'` at `t = 0` and preserves `S`; it
relates the law at `(q, q')` to the law at `(q, -q')` and does not force
`α(0) = γ(0)`.

## Theorem 3 — pair-Gibbs is the one-parameter subfamily

The pair-Gibbs assignment `p(s) ∝ exp(β s · (q + q'))` on `S` gives equal
mass to `q` and `q'`, equal mass to `-q` and `-q'`, and

```text
α(t) / γ(t) = exp(2β (1 + t)).
```

It lies in the two-function family. At `t = 0` with `e^{2β}=2` one has
`α = 1/3`, `γ = 1/6`. At `β = 0` one has `α = γ = 1/4`. The linear assignment
`p(s) ∝ 1 + λ s · (q + q')` is `α = (1 + λ(1+t))/4`, the same family; at
`t = 0` it interpolates uniform (`λ = 0`), deterministic copy (`λ = 1`), and
deterministic flip (`λ = -1`). Pair-Gibbs is a named comparison, not a
framework Hamiltonian.

## Theorem 4 — Born is not a four-point law

The two-outcome overlap `(1 + s · q)/2` on `{q, -q}` equals `1` and `0`. On
the four-point set at the orthogonal reference it takes the values `1` at
`q`, `1/2` at `±q'`, and `0` at `-q`, and **sums to 2**. It is therefore not
a probability on `S`. It also does not depend on `q'` as a recorded
neighbour, so it fails Admissibility's variation sentence at two recorded
neighbours. A nontrivial Born statistic on this generated alphabet is not
that overlap.

## Theorem 5 — sequential formation fails at the support

On a three-site path, the records-only one-neighbour finite support is the
antipodal pair of the unique recorded neighbour (any extra point would sweep
a circle under Aut about that neighbour). In the chain order the middle sees
one neighbour, so its support has two points. In the ends-first order both
ends form empty and are independent Aut-invariant draws; they are
non-collinear almost surely, and the middle's support is the four-point set.
Executed: `L = e_z`, `R = e_x` gives chain support size 2 and ends-first
support size 4. When the ends are collinear the four-point set collapses to
the antipodal pair (control). Haar-empty ends realise the non-collinear case
almost surely. The sequential products cannot agree as measures: they are
not even supported on the same sets.

## Boundary and falsifiers

Falsified if the bisector 180-degree map fails to swap the reference pair, if
pair-Gibbs at `e^{2β}=2`, `t = 0` is not `1/3` and `1/6`, if the Born
four-tuple does not sum to 2, or if the chain and ends-first supports of the
executed path have equal cardinality.

The theorem does not classify mixed-state supports, does not treat three or
more recorded neighbours, does not select the unsoldered reading, and does
not adopt pair-Gibbs as the physical rule. Open PR #8152 remains the support
classification; this note does not rest on it.

## Separating clauses, not adopted

1. Adopt the soldered reading and a site-independent finite menu (the six-axis
   thermodynamics of the induced-law series).
2. Keep unsoldered finite supports and accept that sequential formation is
   order-dependent already at the support.
3. Drop finite supports and use the continuum sphere static law.

None is adopted here.

## Honest-auditor read

The load-bearing step is Theorem 5: the two orders put the middle on
different finite sets. Theorems 2–4 are a classification of weights on the
four-point set the ends-first order actually uses. The Born sentence is a
negative about one named formula, not a derivation of a replacement. Pair-Gibbs
is a comparison inside the covariant family, not a TOE Hamiltonian.

## No-Go Discipline Gate

Negative sentences: Born is not a four-point law; sequential products on a
three-site path cannot agree at the support.

### N1 — Routes that would restore a four-point Born or order-blind sequential formation

| route | attempt | disposition |
|---|---|---|
| 1 renormalise Born's four values to sum to 1 | divide by 2, getting `1/2, 1/4, 0, 1/4` | that assignment ignores `q'` and puts zero on `-q` independently of `q'`; it is not the two-function family unless `γ` is allowed to vanish only at one of the two flips, which Aut about the bisector forbids |
| 2 use Born about `(q+q')/|q+q'|` | linear family at a particular `λ` | that is Theorem 3's linear family, not the two-outcome overlap; recorded as such |
| 3 force the ends to be collinear | then both orders have two-point support | Haar-empty ends are non-collinear a.s.; the collinear case is the executed control, not the generic one |
| 4 drop finite supports | continuum zonal kernels | outside this note; sequential zonal variation is a different object |

### N2 — Wall-independence

Walls: unsoldered Aut; finite supports; records-only sequential products.
Independent.

### N3 — Hidden-wall scan

No "the framework provides a four-point Born" or "naturally Gibbs" in the
theorems. Pair-Gibbs is named as a comparison.

### N4 — Per-citation

| surface | residual | match |
|---|---|---|
| possibility-covariance note on `main` | the unsoldered reading; uniform empty law | used as the reading, not as a weight theorem |
| PR #8152 (open, not a premise) | generated supports; Born-on-antipodal | sibling; antipodal one-neighbour support re-stated, not cited as authority |

### N5 — Resolution

The four-point distinctness, the Gibbs masses, the Born sum, and the two
support cardinalities are executed on an explicit orthogonal pair.

### N6 — Primitives

No menu is supplied by a registered primitive.

### N7 — Steelman

Hostile: "Four points on a sphere is an exercise, and 2 versus 4 is obvious."
Reply: the content is what it fixes — the only Aut-covariant finite
two-neighbour alphabet that carries both neighbours' axes has a two-function
weight family, the named Born overlap is not in it, and sequential formation
cannot be order-blind on that alphabet. Conceded: small finite geometry;
the TOE movement is the obstruction, not a new census.

### N8 — Cross-cycle

Does not retire a previous wall. Complements the open menus note's leftover
row without depending on it.

## Verification

```bash
python3 scripts/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.py
```
