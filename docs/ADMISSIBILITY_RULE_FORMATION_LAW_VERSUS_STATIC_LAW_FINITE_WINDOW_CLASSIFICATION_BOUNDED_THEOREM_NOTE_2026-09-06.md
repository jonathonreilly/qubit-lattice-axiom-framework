---
claim_id: admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis projector menu inside M_2(C) and the finite windows path3, P4, star4, cycle4 (one plaquette) and the open 2x2x2 cube, a covariant positive nearest-neighbor rule of product class (P) with orbit weights (p, q, r) defines two objects: the static law (the joint law whose full conditionals are the rule with every neighbor recorded; Theorem A, the landed binary compatibility theorem generalized to a finite menu and exterior records, cited) and the formation law (the chain of the rule's conditionals along a formation order, conditioning on records only; one of three named readings of a partially recorded neighborhood). Theorem B: for every finite graph, every (P) with (p, q, r) not all equal on the declared menu, and every order, the formation law equals the static law exactly when every site forms with at most one recorded neighbor; hence on every window containing a plaquette no order gives equality. The sum rule is not consistent on the three-site path. Exact arithmetic throughout; no infinite-volume statement; no selection of a rule, coupling, order or reading."
upstream_dependencies:
  - minimal_axioms
  - admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_rule_formation_law_versus_static_law_finite_window_classification_2026_09_06.py
---

# The formation law of a nearest-neighbor rule equals its static law exactly when every record forms with at most one recorded neighbor

**Date:** 2026-09-06
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_rule_formation_law_versus_static_law_finite_window_classification_2026_09_06.py`](../scripts/admissibility_rule_formation_law_versus_static_law_finite_window_classification_2026_09_06.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_rule_formation_law_versus_static_law_finite_window_classification_2026_09_06.txt`](../logs/runner-cache/admissibility_rule_formation_law_versus_static_law_finite_window_classification_2026_09_06.txt)

## Result up front

Take one fixed rule that gives the odds for the value a new record takes from
the values its neighbours already carry. The odds at a site depend on which
of its neighbours already carry records, so the pattern of records that grows
on a patch of lattice depends on the order in which the records formed. The
rule alone does not fix the pattern; whatever fixes the order is physics the
axioms leave open. The same rule also defines a single static pattern law, the
one whose every local conditional is the rule with all neighbours recorded.
Growing records one by one reproduces that static law only when no record
ever forms between two earlier ones, which never happens on a lattice with
plaquettes: around any square, the last corner to form sees two recorded
neighbours.

Exactly: for the six-projector menu, a covariant positive product rule with
orbit weights `(p, q, r)`, and any finite window, the formation law along an
order `σ` and the static law `μ` satisfy the identity
`μ_σ(v) · Π_k Z_k(v_{A_k}) = μ(v) · Z_W` (Theorem B, B1), where `Z_k` is the
rule's normalizer at the `k`-th formed site given its recorded neighbours
`A_k`. The two laws coincide if and only if `|A_k| ≤ 1` for every `k` (B2),
provided `(p, q, r)` are not all equal on the declared menu; such orders exist
exactly on forests (B3). Executed exactly: path3 4 of 6 orders coincide, P4 8
of 24, star4 12 of 24, cycle4 0 of 24; distinct formation laws 2, 3, 5, 4;
cube8 all 40,320 orders have a site with two or more recorded neighbours. The
static half (Theorem A) is the landed binary compatibility theorem generalized
to the finite menu with exterior records and cited; the sum rule fails it on
the three-site path with an exact Brook certificate (`R(1/4) = 27/25`). Six
readings and routes by which the two laws could still coincide are computed;
each either forces the constant rule or is not one fixed nearest-neighbour
rule.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "what the Admissibility rule induces on the infinite lattice — the framework-level action — is unidentified (owner sequencing rule 2026-08-26); the parked statistical-bridge decision wakes on 'the committed-action identification lands', which this note does not fire"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "consumers: the parked statistical-bridge decision material (docs/repo/DEFERRED_DECISIONS.md entry 1, read-only), the record-matter lane's formation-order supply, and the Born-form lane; next targets: the infinite-volume specification of the static laws (DLR existence and uniqueness on the six-projector menu) and the Gaussian instance of the static/formation distinction on the gravity lane's own fixture"
conditional_surface_status: "exact on the declared finite windows and menu; Theorem B's proof is for every finite graph; conditional on the records-only reading where stated, with the two alternative readings computed; no infinite-volume statement"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Theorem A is cited and generalized with the finite-menu Brook lemma re-proved; Theorem B (identity, classification with the single-site variation lemma, forest corollary, constant-rule boundary, order census) is proved for every finite graph and executed exactly on the declared windows; the six coincidence routes are exact finite computations; nothing infinite-volume, physical-selection or bridge-related is claimed."
```

## Premises and declared objects

The only scientific dependencies are the four axioms in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and, for the
static half, the landed binary note linked under Prior art. The axiom
sentences used, verbatim:

- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and "For
  each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form." — "records are permanent" — "Only records are
  readable." — "A site with no record cannot be read."
- Lattice: sites are the points of `Z^3` with nearest-neighbor adjacency,
  translations and proper cubic rotations; Qubit: the full one-site domain is
  `M_2(C)`.

**Menu `M`.** The six pure-state projectors `P(±e_a) = (I ± σ_a)/2`,
`a ∈ {x, y, z}`, in `M_2(C)` (runner B1). The 24 proper cubic rotations act on
`M` as signed axis permutations; the spinor conjugations by
`U_z = diag(e^{−iπ/4}, e^{iπ/4})` and `U_3 = (I − i(σ_x + σ_y + σ_z))/2`
induce exactly that action on two generators (B5, B6). Ordered pairs fall
into three orbits — parallel (6), antiparallel (6), orthogonal (24) —
labelled by `Tr(PP') ∈ {1, 0, 1/2}` (B2); the action on `M` is transitive
(B4). The pairing `⟨P, P'⟩ = 2 Tr(PP') − 1 ∈ {1, −1, 0}` is used by the sum
rule.

**Windows.** Finite graphs with nearest-neighbor edges: path3 (edges 0-1,
1-2), P4 (0-1, 1-2, 2-3), star4 (0-1, 0-2, 0-3), cycle4 (0-1, 1-2, 2-3, 3-0;
one plaquette of `Z^3`), cube8 (the twelve edges of `{0,1}^3`). Open
boundary by default; one declared exterior assignment on cycle4 (two exterior
records per site, `P(e_x)` and `P(−e_y)`) and on cube8 (the exterior neighbor
along axis `a` carries `P(e_a)`) for the boundary-conditioned static law.

**Rules.** A nearest-neighbor rule `r` assigns, to a site `x` and an
assignment `η` of menu values to a subset `A ⊆ N(x)` of its neighbors (the
recorded ones), a probability vector `r(· | η)` on `M`. Covariant: `r`
depends on `η` only through rotation-orbit data. Positive (a named premise;
the axioms allow zero-probability possibilities, admissibility being the
support): `r(s | η) > 0` for every `s` and every partial `η` (B10).

- (P) product rules `r(s | η) ∝ ψ(s) Π_{y∈A} φ(s, η_y)` with `φ` symmetric,
  isotropic, positive with orbit values `(p, q, r)` on `M`, and `ψ`
  covariant, hence constant on the transitive menu (B7: the covariance
  equations' solution space is one-dimensional). Declared triples `(3, 1, 2)`
  and `(5, 2, 4)`; the constant triple `(2, 2, 2)` as the boundary.
- (S) the sum rule `r(s | η) ∝ 1 + λ Σ_{y∈A} ⟨s, η_y⟩`, positive for
  `|λ| < 1/deg`; declared `λ = 1/4` on the path (degree 2) and `λ = −1/8`
  elsewhere (degree 6 on the `Z^3` shell needs `|λ| < 1/6`).

**Three readings of the rule at a partially recorded neighborhood.** None is
axiom content; the Admissibility sentence says "conditions", the Record
sentences say only records are readable and an unrecorded site cannot be
read. (i) R-only, the records-only extension: an unrecorded neighbor
contributes no factor and is not a condition. (ii) Absence-as-condition: an
unrecorded neighbor in lattice direction `d` contributes a covariant factor
`φ_abs(s, d)` with orbit values `(a, b, c)` by the orbit of (forming value,
absent direction). (iii) The marginal reading: the conditional at the
forming site given all existing records is the static law's own conditional
`μ(v_x | v_E)`, `E` the recorded sites. This note uses (i) as a named
premise and computes (ii) and (iii).

**The two definitions.** The STATIC law of a rule on `W` with exterior
records `ω` (empty for the open boundary) is a probability law `μ` on `M^W`
whose full conditionals equal the rule with all neighbors, interior and
exterior, recorded; the rule is *consistent* on `W` iff such `μ` exists. The
FORMATION law of a rule for a formation order `σ = (x_1, …, x_n)` under
R-only is `μ_σ(v) = Π_k r(v_{x_k} | v restricted to A_k)` with
`A_k = N(x_k) ∩ {x_1, …, x_{k−1}}`. The axioms supply no order; every
statement below quantifies over orders or names a declared order family. The
reading of "varies with" used for the constant-rule boundary is the
extensional one restricted to the declared menu, named as such (B4 below).

## Prior art and what is new

The landed note
[`ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md)
(unaudited; its own status field reads candidate-retained-grade) proves, at
its own scope, that "strictly positive binary full-conditionals on a finite
nonempty set of sites" admit a positive joint law "exactly when every
two-site configuration square satisfies" the square-curl equation, with the
joint law unique and recovered by path integration; it excludes "stochastic
update dynamics" and "Record formation" from its scope. Theorem A below is
that static half generalized to the six-value menu with exterior records; the
Brook ratio lemma is re-proved at the finite-menu scope. The archived packet
result `R136` (`archive/campaigns/opus-direct-20260827/POSITIVE_PATH.md`,
floating point, never refereed) read the Admissibility conditional as the
full conditional of one static joint law; it is a reference only, its
reading is the static one, and nothing is imported from it.

New here: the formation law as an object; the identity B1; the classification
B2 with its proof (the single-site variation lemma); the forest corollary B3
and the plaquette corollary; the exact order census B5; the six executed
coincidence routes, including the window dependence and non-locality of the
marginal reading; the menu-restriction witness for the variation clause. The
prior-art sweep is recorded in the block's `ROUTE_PORTFOLIO.md`.

## Exact target and obligation graph

**Target.** For every finite graph `W`, every (P) with `(p, q, r)` not all
equal on the declared menu, and every order `σ`, under R-only:
`μ_σ = μ` iff `|A_k| ≤ 1` for every `k`.

| obligation | disposition |
|---|---|
| the static law of (P) exists with the rule as full conditionals (direct cancellation) | proved here (Theorem A) |
| uniqueness of the static law given positive full conditionals on a finite menu (Brook ratio lemma) | re-proved here at scope; the binary case is the landed note |
| a positive rule's static law is positive on every configuration | proved here (one paragraph) |
| symmetry of the pair weight on `Z^3` windows (edge-flip element) | proved here for `Z^3` windows; a class-(P) hypothesis on the abstract graphs |
| the sum rule is not consistent on path3 (degree ≥ 2) and is consistent on one edge | executed (C6, C7, C8) |
| the formation identity B1 | proved here; executed on every order of four windows and six cube orders |
| the one-neighbor normalizer is constant (transitivity) | proved here; executed (D7) |
| the single-site variation lemma (B2 ⇒), every arity | proved here; `f_j` executed for `j = 1..5` (D6) and on the cube (D9) |
| forest corollary B3 and the plaquette corollary | proved here; executed (D4, D8) |
| the constant rule coincides for every order | proved here; executed (D10) |
| the six coincidence routes | executed (E1–E6b) |
| the general converse of Theorem A (only product rules are consistent on triangle-free graphs) | referenced only; not used and not re-proved |
| existence or uniqueness of an infinite-volume law for the specification | open; not this note |

The strongest missing lemmas are the general converse of Theorem A and the
infinite-volume specification; neither is used by the target.

## Theorem A — the static law of a product rule (cited and generalized)

**Statement.** For every finite graph `W`, every exterior assignment `ω` and
every (P), the law
`μ_W^ω(v) ∝ Π_x ψ(v_x) Π_{xy∈E(W)} φ(v_x, v_y) Π_{x∈W, y∈∂W} φ(v_x, ω_y)`
has full conditionals equal to the rule with all neighbors recorded, and it
is the unique law with those full conditionals.

**Direct cancellation.** Fix `x` and the values off `x`. In the ratio
`μ(v_x = s | rest) = μ(v[x→s]) / Σ_t μ(v[x→t])` every factor not containing
`x` cancels, leaving `ψ(s) Π_{y∈N(x)} φ(s, v_y) Π_{y∈∂W∩N(x)} φ(s, ω_y)`
normalized over `s`: the rule with every neighbor recorded. Executed
exhaustively on path3, P4, star4, cycle4 (C1), on cycle4 with the declared
exterior records (C2), and on cube8 for the declared configuration family
with and without exterior records (C3), at both triples.

**Positivity lemma.** A positive rule's static law is positive on every
configuration: the weight is a product of positive factors, so every `μ(v)`
is positive (C4). Equivalently, the single-site-change graph on `M^W` is
connected and every full-conditional ratio along its edges is positive, which
is what the next lemma needs.

**Brook's ratio lemma, finite menu (re-proved).** Let `μ` and `μ'` be two
positive laws on `M^W` with the same full conditionals. For any two
configurations `v, v'` choose a path `v = v^0, v^1, …, v^n = v'` changing one
site at a time. For each step, `μ(v^{i+1})/μ(v^i)` equals the ratio of the
shared full conditional at the changed site (both are the same conditional
evaluated at two values, given the same rest), so `μ(v')/μ(v)` is the
product of those ratios, and the same product gives `μ'(v')/μ'(v)`. Hence
`μ'/μ` is constant, and normalization makes it 1. Executed as an instance on
path3 at `(3, 1, 2)`: the homogeneous compatibility system
`μ(v) Z_x(v) − num_x(v) Σ_t μ(v[x→t]) = 0` (648 equations, 216 unknowns) has
exact rank 215 by fraction-free integer elimination and the static weight
vector spans its nullspace, all entries positive (C5).

**Symmetry of the pair weight on `Z^3` windows.** The element
`g = t_{e_1} ∘ R_{e_2,π}` (unit translation after the proper half-turn
`diag(−1, 1, −1)` about `e_2`, both in the axioms' group) sends `0 ↦ e_1` and
`e_1 ↦ 0`; covariance of the rule under `g` forces `φ(a, b) = φ(ρ b, ρ a)`
with `ρ` the induced menu permutation, and isotropy then gives
`φ(a, b) = φ(b, a)` (B9, executed on all 36 pairs). On the abstract graphs
path3, P4, star4, cycle4, uniformity and symmetry of `φ` are class-(P)
hypotheses, not consequences. Symmetry is what makes the formation identity
hold: with an asymmetric pair weight the sequential product orients every
edge later-after-earlier, and the identity `μ_σ Π Z_k = μ Z_W` against the
static law with edges oriented by site index fails for 5 of the 6 orders of
path3 (D12, one executed instance).

**The sum rule.** On a single edge the sum rule is consistent: the
compatibility system has nullity 1 with the explicit law
`μ(s, t) = (1 + λ⟨s, t⟩)/36` at both couplings (C7). On path3 it is not: the
compatibility system has full rank 216 at `λ ∈ {1/4, −1/8}` (C6). The
symbolic Brook cycle at sites 1–2 (`a = P(e_x) → a' = P(−e_x)` at the end
site, `b = P(e_x) → b' = P(−e_x)` at the middle site, `c = P(e_x)`) gives
`R(λ) = (−2λ³ + 3λ² − 1)/(2λ³ + 3λ² − 1)`, `R(1/4) = 27/25`, and
`R(λ) − 1 = −4λ³ / ((λ + 1)²(2λ − 1))`: the numerator carries the factor
`λ²` and has no other root, so none in `|λ| < 1/6` (C8). The same cycle for
(P) with symbolic `(p, q, r)` is exactly 1 (C9). The obstruction is
degree-dependent: it needs a site of degree at least two, and positivity of
the sum rule holds for `|λ| < 1/deg`.
