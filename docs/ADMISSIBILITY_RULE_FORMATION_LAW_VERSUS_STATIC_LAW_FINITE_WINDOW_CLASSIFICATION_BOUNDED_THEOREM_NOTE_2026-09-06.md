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

## Theorem B — the formation law and the classification

Throughout: `W` a finite graph, (P) with symmetric isotropic positive `φ` of
orbit values `(p, q, r)` and constant `ψ`, `σ = (x_1, …, x_n)` an order,
`A_k = N(x_k) ∩ {x_1, …, x_{k−1}}`, and the records-only reading. Write
`Z_k(η) = Σ_s ψ(s) Π_{y∈A_k} φ(s, η_y)` for the local normalizer at `x_k`
given the recorded values `η` on `A_k`, and `Z_W = Σ_v Π_x ψ(v_x) Π_{xy∈E} φ(v_x, v_y)`.

**B1 (identity).** For every `v`,
`μ_σ(v) · Π_k Z_k(v_{A_k}) = μ(v) · Z_W`.
*Proof.* `μ_σ(v) = Π_k [ψ(v_{x_k}) Π_{y∈A_k} φ(v_{x_k}, v_y)] / Z_k(v_{A_k})`.
Every edge `xy` of `W` is charged exactly once, to whichever endpoint forms
later, and by symmetry of `φ` the charged factor equals `φ(v_x, v_y)`; every
site contributes its `ψ`. So the numerators multiply to `Z_W · μ(v)`. ∎
Executed for every order of path3, P4, star4, cycle4 at both triples (D1),
with `Σ_v μ_σ = 1` (D2) and the consistency line `Z_W = Σ_v μ_σ Π_k Z_k`
(D3; a runner line, not a theorem), and on the six declared cube orders for
the configuration family (D9). Hence `μ_σ = μ` iff `Π_k Z_k(v_{A_k})` is
constant in `v`.

**B2 (classification).** With `(p, q, r)` not all equal on the declared
menu: `μ_σ = μ` if and only if `|A_k| ≤ 1` for every `k`.

(⇐) The zero-neighbor normalizer is the constant `6ψ`; the one-neighbor
normalizer `Σ_s ψ φ(s, t) = ψ (p + q + 4r)` is independent of `t` because
the menu is transitive and `φ` isotropic (D7, symbolic for every `t`). So
every factor is constant and B1 gives `μ_σ = μ`.

(⇒, the single-site variation lemma.) Suppose `|A_m| ≥ 2` for some `m`.
Pick `y ∈ A_m` and fix every site other than `y` at a reference value `R`.
Then every factor `Z_k` with `y ∉ A_k` is a constant (its arguments are all
`R`); every factor with `y ∈ A_k` and `|A_k| = 1` is the constant
`ψ(p + q + 4r)`; and every factor with `y ∈ A_k` and `|A_k| = j + 1 ≥ 2`
equals `ψ f_j(orbit(v_y, R))`, where
```text
f_j(par)  = p^{j+1} + q^{j+1} + 4 r^{j+1},
f_j(anti) = p q^j + q p^j + 4 r^{j+1},
f_j(orth) = (p + q) r^j + r (p^j + q^j) + 2 r^{j+1}.
```
These come from counting the six `s` by their orbit relative to the pair
`(v_y, R)`: for `v_y = R` the six `s` split as one parallel to both, one
antiparallel to both, four orthogonal to both; for `v_y = −R` as
(parallel, antiparallel), (antiparallel, parallel) and four (orth, orth);
for `v_y ⊥ R` as (par, orth), (anti, orth), (orth, par), (orth, anti) and
two (orth, orth). Then
```text
f_j(par) − f_j(anti)  = (p − q)(p^j − q^j)                          ≥ 0, = 0 iff p = q;
f_j(anti) − f_j(orth) = (p − r)(q^j − r^j) + (q − r)(p^j − r^j);
at p = q:  f_j(anti) − f_j(orth) = 2 (p − r)(p^j − r^j)             ≥ 0, = 0 iff p = r.
```
(The first identity is elementary for every `j`; the second is the
subtraction of the displayed formulas; both are executed symbolically for
`j = 1, …, 5`, D6.) The multiset of varying factors is nonempty (it contains
`k = m`) and every factor is positive, so their product takes the same value
on the three orbits iff each factor does, iff `p = q = r`. As `v_y` runs over
the menu it meets all three orbits relative to `R`, so under the hypothesis
`Π_k Z_k` is not constant and by B1 `μ_σ ≠ μ`. ∎
Executed: on the six declared cube orders, with all sites but `y` at
`P(e_x)` (`y` the first recorded neighbor of the first site with
`|A_m| ≥ 2`), `Π_k Z_k` takes exactly three values as `v_y` runs over the
menu, equal to `const × Π_j f_j` for the recomputed multiset of `j`'s (D9);
for the identity order at `(3, 1, 2)`: `m = 3`, `y = 1`, `j`-multiset
`{1, 1}`, values `(10933678080, 7828254720, 9316270080)` on (par, anti, orth).

**B3 (corollaries).** An order with `|A_k| ≤ 1` for all `k` exists iff `W`
is a forest: each edge is charged to its later endpoint, so `|A_k| ≤ 1` for
all `k` means every site receives at most one charged edge, i.e. `|E| ≤`
the number of non-first sites in each component, which forces a forest; and
on a forest the root-outward sweeps of each component are exactly such
orders. On every window containing a cycle — every plaquette of `Z^3` — no
order gives `μ_σ = μ`. Executed: path3 exactly the orders
`(0,1,2), (1,0,2), (1,2,0), (2,1,0)` (4 of 6); P4 8 of 24; star4 exactly the
12 orders with the center first or second; cycle4 0 of 24 (D4, all laws
computed); cube8: every one of the 40,320 orders has some `|A_k| ≥ 2`, and
the distribution of `max_k |A_k|` is `{3: 40320}` — the last site to form
always sees all three of its neighbors recorded (D8).

**B4 (the constant rule).** At `p = q = r` the rule's output is uniform under
every condition and `μ_σ = μ` for every order (executed at `(2, 2, 2)` for
every one- and two-neighbor condition and every order of path3 and cycle4,
D10). Under the extensional reading of "determined by, and varies with, the
nearest-neighbor conditions" — a named reading — the constant rule is
excluded. That reading is about the full one-site domain `M_2(C)` and does
not imply variation on a finite menu: the isotropic pair weight
`φ(s, t) = f(2 Tr(PP') − 1)` with `f(x) = 1 + x²(1 − x²)` gives
`f(1) = f(−1) = f(0) = 1`, so `(p, q, r) = (1, 1, 1)` on the six-axis menu
and `μ_σ = μ` for every order on every window, while `f(1/2) = 19/16` and
`f(x) = 5/4` at `x² = 1/2` (D11, exact rationals). The reading this note
uses is therefore "the variation clause restricted to the declared menu",
named as such; B2's hypothesis "not all equal on the declared menu" is that
clause and nothing bridges from the axiom's clause to the menu without it.

**B5 (order dependence, stated exactly).** `μ_σ` depends on `σ`, and distinct
orders need not give distinct laws. The census of distinct formation laws
over all orders, identical at `(3, 1, 2)` and `(5, 2, 4)` (D5): path3 6
orders → 2 laws (class sizes 4, 2; the class of size 4 is `μ`); P4 24 → 3
(8, 8, 8; one class is `μ`); star4 24 → 5 (12, 6, 2, 2, 2; the class of size
12 is `μ`); cycle4 24 → 4 (8, 8, 4, 4; none is `μ`). No invariant of the
classes is claimed.

## The six readings and routes by which the two laws could still coincide

Each row answers, for the corollary "on every window containing a plaquette,
for every order, the formation law differs from the static law", one way the
conclusion could be escaped; all are executed.

1. **The constant rule** coincides for every order (D10) and is excluded by
   the named reading of the variation clause restricted to the menu; the
   `(3, 1, 2)` rule varies between the conditions `P(e_x)` and `P(e_y)`
   while the constant rule does not (E1).
2. **A non-constant site weight.** An explicit `ψ = (2, 1, 1, 1, 1, 1)`
   fails the covariance equations (E2); without assuming covariance, "the
   two-neighbor normalizer `Z_2(b, c) = Σ_s ψ(s) φ(s, b) φ(s, c)` is
   constant" is a homogeneous linear system in the six values `ψ(s)` of rank
   6 at both declared triples, so no signed site weight makes it constant
   (E2).
3. **A direction-blind absence factor `φ_abs(s)`.** Covariance forces it
   constant (solution space one-dimensional, E3), so inside that subfamily
   R-only is without loss of generality.
4. **A direction-dependent covariant absence factor `(a, b, c)`** — orbit
   of (forming value `s`, absent direction `d`): parallel same sign `a`,
   opposite sign `b`, orthogonal `c`. On path3 with order `(0, 2, 1)`, the
   equations `μ_σ(v) = μ(v)` on the declared configuration set (all 36
   configurations with the first two formed sites free and the rest at
   `P(e_x)`, plus the six single-site variations) reduce, after the
   homogeneity normalization `r = c = 1`, to 8 polynomial equations whose
   lex Gröbner basis contains `(a − 1)u`, `(b − 1)u`, `(p − q)²u`,
   `(q − 1)³u` with `u = (p + q + 4)² > 0`; the solution set in the positive
   domain is `a = b = c`, `p = q = r`, verified on every configuration
   (E4a). On cycle4 with order `(0, 1, 2, 3)`, the raw system's `sympy.solve`
   did not finish inside the block's time cap (a could-not, recorded in the
   pack), and the runner instead executes an exact two-step route: the
   static law's site marginal is uniform (symbolic; `μ` is invariant under a
   simultaneous rotation of all values, and the menu is transitive), while
   the formation law's marginal at the first-formed site is
   `r(· | ∅) ∝ (ac, bc, ac, bc, c², c²)`, uniform iff `a = b = c`; a constant
   absence factor cancels between numerator and normalizer, so the system
   reduces to the R-only one, whose declared-set equations give `p = q = r`;
   the found solution is verified on every configuration (E4b). Any
   factorized absence weight on path3 `(0, 2, 1)` would need the middle
   site's normalizer to factor as `χ(v_0) χ(v_2)`, i.e. the `6 × 6` matrix
   `Z_2(b, c) = (Φ²)(b, c)` to have rank 1. Its rank is 4 at `(3, 1, 2)` and
   6 at `(5, 2, 4)`: `det Φ = (p + q + 4r)(p + q − 2r)²(p − q)³`, and
   `3 + 1 − 2·2 = 0` (the block contract's expectation "rank 6 at both
   triples" was wrong at `(3, 1, 2)`; the route needs only rank ≠ 1). The
   two `2 × 2` minors `(p − q)²(p² + 2pq + q² + 8r²)` and
   `((p − r)² + (q − r)²)(p² + 2pr + q² + 2qr + 6r²)` hold symbolically, so
   the rank is at least 2 whenever `(p, q, r)` are not all equal (E4c). The
   same rank fact says the normalizer history couples sites at graph
   distance two non-multiplicatively: the formation law is not a
   nearest-neighbor field of the static kind.
5. **The uniform mixture of `μ_σ` over all 24 orders of cycle4** differs
   from `μ`: `max_v |avg_σ μ_σ(v) − μ(v)| = 899/2341664` at `(3, 1, 2)` and
   `3478458125/23066700436908` at `(5, 2, 4)`; the panel's pre-run value
   `1585133/10007780364` at `(2, 3, 5)` is reproduced (E5).
6. **The marginal reading** makes `μ_σ = μ` for every order by the chain
   rule when the conditional at the forming site is the static law's
   conditional given all existing records (executed on cycle4 for all 24
   orders, E6b); given only the recorded neighbors it does so for 0 of 24
   orders, because a partial set of records does not screen off the rest.
   And it is not one fixed nearest-neighbor rule: the one-neighbor
   conditional it assigns on path3 equals the rule's for every `v_1`, while
   on cycle4 at `(3, 1, 2)` and `v_1 = P(e_x)` it is
   `(219/866, 71/866, 72/433 ×4)` against the rule's `(1/4, 1/12, 1/6 ×4)`
   (E6a) — the same recorded condition receives different odds on different
   windows.

## Named objects (remarks; no computation beyond the above)

- The static action `S_W^ω = −Σ_x log ψ(v_x) − Σ_{xy} log φ(v_x, v_y)
  − Σ log φ(v_x, ω_y)`, unique up to the gauge `φ → φ h(s) h(t)`,
  `ψ → ψ h^{−deg}` and an additive constant; on the transitive menu the
  gauge class is canonical up to a constant.
- The formation action `S_W + Σ_k log Z_k(v_{A_k})`: the static action plus
  the order-dependent normalizer history.
- The family `{μ_W^ω}` over finite windows and exterior assignments is a
  specification: the rule induces a static ACTION (a gauge class) rather than
  a single law. Whether the infinite lattice carries one static law or
  several is the phase question; existence or uniqueness of an
  infinite-volume law is not claimed here and is the next block's target.
- Gaussian analogy, three sentences with hypotheses: for a real symmetric
  positive-definite quadratic pair form the static law is Gaussian with that
  precision. Pinning records fixes a sub-block of the precision, and the
  read-slice block of its inverse is the read-slice marginal covariance under
  the pinned law — a static, conditional-then-marginal object, not a
  formation-order conditional. The parked bridge text's weights are the
  normalized diagonal of such a block on a different carrier, so this is a
  cross-carrier analogy, and the 2026-08-26 gate measurement is a float
  measurement on one fixture, cited by path, on which this note has no
  bearing.
- This note does not fire wake condition 1 of
  `docs/repo/DEFERRED_DECISIONS.md` entry 1 (the committed-action
  identification); nothing here identifies the infinite-lattice object.
