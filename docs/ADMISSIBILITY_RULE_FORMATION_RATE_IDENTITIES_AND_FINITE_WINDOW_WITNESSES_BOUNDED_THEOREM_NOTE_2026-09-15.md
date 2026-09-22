---
claim_id: admissibility_rule_formation_rate_identities_and_finite_window_witnesses_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Positive-total-rate memoryless clocks give causal scheduling weights; value-blind clocks give order mixtures. Exact finite witnesses at (3,1,2), seeded growth equality on connected trees, plaquette coefficient identities and a finite rank-five witness are retained. Universal rate-law and convex-mixture exclusions are deferred."
upstream_dependencies:
  - minimal_axioms
  - admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py
---

# Formation-rate identities and finite-window witnesses

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Independent memoryless clocks with positive total rate at every reachable nonfinal state define a finite formation process. Value-blind rates give a mixture over sequential order laws; value-dependent rates give causal scheduling weights that depend on the pattern. These weights are not posterior probabilities of orders conditional on the completed pattern.

The exact rectangle, cube and plaquette witnesses below distinguish the declared clocks at `(3,1,2)`. Seeded growth on a connected tree agrees with the static law. The plaquette algebra gives exact coefficient and difference identities. The original universal exclusions of clock laws and convex mixtures remain deferred pending complete negative certification. No plaquette conclusion is extended to larger windows.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain the named identities and finite witnesses; broad negative certification remains deferred."
conditional_surface_status: "Conditional on the declared six-axis menu, positive product rule and records-only reading."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
The original complete arguments and execution histories are preserved in
[the recovery manifest](work_history/review_loop/pr8150/original-manifest.json).
This source repair does not claim a completed independent audit.

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable." — and from its
reading note (2): the distribution "does not supply the formation site,
probability, or rate."

**Readings carried, named, nothing new adopted.** The records-only reading
and the formation law of block 01
([`ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)):
along an order `σ` the site `x_k` draws from the rule with its recorded
neighbours `A_k` only, `μ_σ(v) = Π_k r(v_{x_k} | v_{A_k})`, with
`r(a | ∅) = 1/M` and `r(a | A) = Π_{y∈A} K(v_y, a)/K_{|A|}(v_A)`,
`K(b, a) = φ(a, b)/Z_1`, `K_k(v_A) = Σ_s Π_{y∈A} K(v_y, s)` (`K_1 ≡ 1`). The
static law `Π_edges φ(v_e)/Z`. The six-axis menu, positivity, the product rule
with weights `(p, q, r)`, `Z_1 = p + q + 4r`. The multiset key of the census
note ([`ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md`](ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md),
Lemma L): `μ_σ` depends on `σ` only through the multiset of recorded sets of
size at least two.

**The clock model (the supplied object of this block).** Every unrecorded
site `x` carries an exponential clock of rate `λ(x, S, v_S) ≥ 0`, a function
of the site, the recorded set `S` and the recorded values, invariant under the
simultaneous action of lattice translations and proper cubic rotations on
`(x, S, v_S)` (the menu carries the rotation action on axes). Clocks are
independent given the state and memoryless. When `x`'s clock rings first, `x`
records a value from the rule given `v_{N(x)∩S}`; then all clocks restart. The
window `Λ` is the set of sites that can form; the process stops when `Λ` is
recorded. Require positive total rate at every reachable nonfinal state; a zero-rate clock never rings. *Value-blind* laws depend on `(x, S)` only. Executed laws: uniform
`λ ≡ 1`; seeded `λ = 1` if `N(x) ∩ S ≠ ∅` or `S = ∅`, else `0`; attracting
`λ = 1 + |N(x) ∩ S|`; parallel growth
`λ = 1 + [∃ y ∈ N(x) ∩ S : v_y = the axis from y to x]`.

**Windows.** The `2×3` rectangle; the open `2×2×2` cube; the plaquette
(sites `1 = (0,0)`, `2 = (1,0)`, `3 = (1,1)`, `4 = (0,1)` in the plane `z = 0`);
the path of three sites; the star (a site and four of its neighbours).

**Plaquette types.** For a corner `s` let `δ_s` point from `s` to the opposite
corner (`δ_1 = (1,1,0)`, `δ_2 = (−1,1,0)`, `δ_3 = (−1,−1,0)`, `δ_4 = (1,−1,0)`).
A value `v_s` is of type *toward* if `v_s · δ_s > 0`, *away* if `< 0`,
*perpendicular* if `v_s = ±z`. Write `d_same = 1/K_2(a,a)`,
`d_anti = 1/K_2(a,−a)`, `d_orth = 1/K_2(a,b)` for `b ⊥ a`; at `(3,1,2)`:
`72/13`, `72/11`, `6`.

## Prior art and what is new

The linked census supplies the multiset key and the quoted rectangle value; the linked finite-window classification supplies the sufficient one-recorded-neighbour factorization. Competing independent exponential clocks are the usual continuous-time Markov jump construction (Gillespie); seeded cluster growth has the Eden support rule. These names identify mathematical context, not empirical or axiomatic authority. The retained new content is the explicit clock witnesses, seeded-tree construction and plaquette coefficient identities.

## Exact target and obligation graph

Positive-total-rate memoryless clocks give causal scheduling weights; value-blind clocks give order mixtures. Exact finite witnesses at (3,1,2), seeded growth equality on connected trees, plaquette coefficient identities and a finite rank-five witness are retained. Universal rate-law and convex-mixture exclusions are deferred.

Universal negative conclusions from the original version remain deferred; they are not consequences promoted by this landing surface.

## Theorem R1 — clocks give orders, orders give mixtures

**Statement.** In the state `(S, v_S)` with unrecorded rates `λ_y`,
`Λ = Σ_y λ_y > 0`, the next site to form is `x` with probability `λ_x/Λ`,
independent of the waiting time, and the finished law is that of the
discrete chain with these jump probabilities. For a value-blind law the jump
probabilities do not depend on the values, the order `σ` has a law `P_R(σ)`
independent of the values, and the finished law is `μ_R = Σ_σ P_R(σ) μ_σ`,
which depends on `R` only through the induced law of the recorded-set
multiset. For a value-dependent law the finished law is
`μ_R(v) = Σ_σ W_R(σ; v) μ_σ(v)`, where `W_R(σ; v)` is the product of the causal site-choice probabilities, each using only previously recorded values. The joint order-pattern mass is `W_R(σ;v) μ_σ(v)`; when `μ_R(v)>0`, the posterior order probability is this joint mass divided by `μ_R(v)`, not `W_R(σ;v)` itself.

*Proof.* With independent exponential times `T_y` of rates `λ_y`,
`P(T_x < T_y ∀ y ≠ x) = ∫_0^∞ λ_x e^{−λ_x t} Π_{y≠x} e^{−λ_y t} dt = λ_x/Λ`,
and the minimum's law is exponential with rate `Λ` independent of which clock
rang; memorylessness makes the state sequence Markov with these jump
probabilities, and the finished pattern depends only on the state sequence.
Value-blind: the jump probabilities are functions of `(S)` only, so the order
law factorizes out of the value draws; the last claim is Lemma L. ∎ Executed:
the jump probabilities for rates `(1, 2, 3)` by the exact integral (B1); the
mixtures on `2×3` computed by multiset classes against the full enumeration of
`720` orders on 30 sampled rectangle patterns (B2); the plaquette comparison enumerates all 1296 patterns.

## Theorem R2 — the witness

**Statement.** At `(3,1,2)` on `2×3` (28 classes, as in the census note) the
uniform, seeded and attracting laws give pairwise different finished laws;
their distances to the static law are `372254646387017/12790481418000000` (`0.0291…`) (uniform; equal to the
census note's Theorem 3 value), `5951761987229/292725576000000` (`0.0203…`) (seeded; it charges 6 of the 28
classes) and `32318135184155791/1253467178964000000` (`0.0258…`) (attracting); the pairwise distances are
`1415480709077/147346345935360` (uniform–seeded, `0.0096…`), `842029569149/229205427010560` (uniform–attracting, `0.0037…`), `12238463804737/2062848843095040` (seeded–attracting, `0.0059…`). On the open cube (542 classes) the all-`+x` pattern has
probability `338229/7997080000` (uniform), `84807/1799782400` (seeded), `3244436397/73116160000000` (attracting) under the three laws, against `59049/775835648` for the
static law. On the plaquette the four laws give distances `262271/15806232` (uniform, `0.0166…`), `30457/2431728` (seeded, `0.0125…`), `591377/39515580` (attracting, `0.0150…`), `2239744469/137703893184` (parallel growth, `0.0163…`) to the
static law and are pairwise different.

*Proof.* Enumeration; the class structure is Lemma L. ∎ (C1–C4.)

## Theorem R3 — on trees the seeded law is the static law

**Statement.** Let `Λ` be a tree (a connected window without cycles). Under
the seeded law the recorded set is connected at every step, so every record
after the first has exactly one recorded neighbour, and `μ_seeded` equals the
static law of `Λ` exactly, whatever the first site. The uniform law differs
from it on the path and on the star.

*Proof.* If the recorded cluster is connected and `x` has two recorded
neighbours, the two paths from `x` through them into the cluster close a
cycle; so on a tree every new site has exactly one recorded neighbour, the
seeded law keeps the cluster connected by construction, and block 01's Theorem
B applies to every order it charges. ∎ The uniform-law differences on the two finite trees follow from the exact enumerations below, not merely from charging an order with two recorded neighbours. Executed: the
path and the four-leaf star, seeded equal to static, uniform at distance
`1/216` on the path and `56059/3369600` on the star (D1–D2).

## Theorem R4 — plaquette coefficient identities

**Retained identity.** On equal-diagonal-type plaquette patterns, the finished-law ratio is the explicit expression below in `G(p,d)`. Its pairwise differences factor through the exact positive normalizer gaps. The universal no-clock-law conclusion from the original argument is deferred, not promoted as a new positive classification.

*Derivation of the coefficient identities.* Write `Π K = Π_edges K(v_e)`. Every order of the plaquette is of one of
two kinds: a *path* order (start `s`, then an adjacent corner, then the next
along the cycle, then the last corner, which records both its neighbours, the
ends of one diagonal) with `μ_σ = (1/6) Π K · d`, `d = 1/K_2` of that diagonal;
or a *diagonal-first* order (start `s`, then the opposite corner with no
recorded neighbour, then the remaining two, each recording both) with
`μ_σ = (1/36) Π K · d_s²`, `d_s` for the diagonal through `s`. (Each edge factor
`K` appears once, when its later endpoint forms; `K_1 ≡ 1`.) The static law is
`Π K · Z_1⁴/Z`, a constant multiple of `Π K`.

Now the clock. At `S = ∅` the four rates are equal (the 90° rotation about
the plaquette's axis is a proper rotation carrying each corner to the next
and fixing the configuration), so the first site is uniform and its value is
uniform. At `S = {s}` the probability `p_s` that the opposite corner forms
next is `λ_diag/(λ_diag + λ_a + λ_b)`, a function of `(s, v_s)` alone; the
180° rotation about the axis `δ_s` (a proper rotation; it swaps the two
adjacent candidates and fixes the diagonal one, and acts on values by
swapping the two in-plane axes along `δ_s` and reversing `z`) shows that `p_s`
depends only on the type of `v_s`: `p_in`, `p_out`, `p_perp`. Whatever happens
later, a diagonal-first history from `s` ends with weight `(1/36) Π K d_s²`,
and a path history from `s` ends with weight `(1/6) Π K d` for the diagonal it
closes. Hence for any pattern whose two diagonals have the same pair type,
`d_1 = d_2 = d`, the finished law is
`μ(v) = Π K · (1/4) Σ_s [(1 − p_{type(s)}) d/6 + p_{type(s)} d²/36] = Π K · (1/4) Σ_s G(p_{type(s)}, d)`,
where `G(p, d) = (1 − p) d/6 + p d²/36` is strictly increasing in `d > 0` for
every `p ∈ [0, 1]`, and the path-class decisions (which may depend on values)
drop out because both diagonals carry the same `d`.

Take `P_1 = (+x, −x, +x, −x)`: diagonals `(+x,+x)` and `(−x,−x)`, `d = d_same`;
types toward, toward, away, away. Take `P_3 = (+x, +x, −x, −x)`: diagonals
`(+x,−x)` twice, `d = d_anti`; types toward, away, toward, away — the same
multiset. So `μ(P_3)/ΠK(P_3) − μ(P_1)/ΠK(P_1) = (1/2) Σ_{τ ∈ {in, out}} [G(p_τ, d_anti) − G(p_τ, d_same)]`,
which is strictly positive when `d_anti > d_same`, i.e. `K_2(a,−a) < K_2(a,a)`,
i.e. `(p − q)² > 0`. If `p = q`, take `P_4 = (+x, −x, +y, +y)`: diagonals
`(+x,+y)` and `(−x,+y)`, `d = d_orth`; types toward, toward, away, away — the
multiset of `P_1`; and `d_orth ≠ d_same` iff `(p − r)² + (q − r)² > 0`. These formulas retain the exact positive normalizer gaps in the displayed difference identity. ∎

Executed: the general identity with `p_in`, `p_out` as symbols and the three
`d`'s as rational functions of `(p, q, r)` (E1); the four explicit laws'
ratios at `P_1, P_3, P_4` (uniform: `152/169, 136/121, 1`) and their distances
to the static law (E2); the type assignment of `P_1, P_3, P_4` and the three
values of `d` (E3).

## Identities R5 and finite rank witness R6

**Mixture coefficient identity.** For `c_σ≥0`, `Σc_σ=1`, an order mixture on an equal-diagonal-type pattern has ratio `(c_path/6)d+(c_diag/36)d²` to `ΠK`. This follows by grouping the path and diagonal-first products derived above. Its difference between `d'>d>0` is `(d'-d)[c_path/6+c_diag(d'+d)/36]`. The universal convex-mixture exclusion remains deferred.

**Finite rank witness.** At `(3,1,2)`, the matrix of the four plaquette class laws and the declared parallel-growth law on all 1296 patterns has rank five (E5). This is an exact finite linear-algebra witness; it is not a classification of all value-dependent clocks.

## The clause candidates (recorded, not adopted)

Uniform, seeded, attracting and parallel-growth rates are supplied examples. The listed finite statistics describe their differences; the seeded construction agrees with the static law on connected trees. No example is selected as physical. A realized-state reference does not supply a rate law, averaging measure or statistical prediction.

## No-Go Discipline Gate

### N1 — Deferred negative certification
The original route table mixes changes of scope and non-attempts with actual arguments; it does not establish five independent exact-target attack families. Broad negative certification is withheld. The original full proofs remain byte-exact in the recovery manifest, and the original branches remain recovery handles.

### N2 — Supplied model conditions
The finite menu, positive product rule, records-only reading and any stated clock or joint-law convention are supplied mathematical conditions. The original wall-independence assertion does not complete the negative gate.

### N3 — Hidden conditions
The displayed domains govern: fixed exterior records cannot be varied inside a proof about one fixed environment. Value-blind mixing and causal value-dependent scheduling are distinct constructions.

### N4 — Actual mathematical imports
The linked finite-window classification supplies the product law and its at-most-one-recorded-neighbour sufficient condition. The linked census supplies the recorded-set multiset reduction and the quoted rectangle value. These are conditional mathematical inputs; no broader parent conclusions are imported.

### N5 — Executed resolution
The primary runner states its exact finite domains in five resolution lines. Written identities beyond those domains are checked as arguments, not executed on the infinite lattice. Historical controls have their original domains and are not relabelled as current primary execution.

### N6 — Primitive boundary
No primitive selects a rate, unit, measure over orders or boundary condition. The supplied mathematical constructions do not adopt a framework clause.

### N7 — Remaining objection
Positive identities and finite witnesses do not themselves discharge the deferred universal negative certification. Arbitrary fixed-environment necessity additionally has an unresolved proof gap.

### N8 — Recovery
The original complete proofs, including deferred arguments, are recoverable from the manifest; this narrowing does not declare their mathematical negations.

## Falsifiers

A failure of the exponential jump integral, causal scheduling product, sampled class/product agreement, quoted exact finite distances, seeded-tree factorization, plaquette coefficient identities or rank-five witness would falsify the corresponding retained result. No larger-window exclusion is included.

## Boundaries and non-claims

This note proves clock and plaquette identities, the seeded-tree construction and finite witnesses; universal clock-law and convex-mixture exclusions are deferred; no order, rate, rule or coupling is selected as physical, and no clause is adopted.

No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The menu, weights and clock conventions are declared mathematical inputs, not empirical or axiom-selected values.

## Imports

The linked axiom memo supplies only its quoted sentences. The linked finite-window classification and census supply the mathematical inputs identified above. The exponential race integral is proved here; Gillespie and Eden identify context only. All rates, triples and windows are declared model inputs.

## Review record

The original author controls, checker notes, proofs and outputs are preserved byte-exact in the recovery manifest. Their historical claims are not current review authority. This corrected draft awaits the original independent reviewer's affected-source confirmation and bounded final capture; no old output is restamped.

## Verification

```bash
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py --exact
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_static_law_2026_09_15.py --mutation static_reached_on_plaquette_claimed
```

Families: A authority and inputs; B the jump probabilities and the class mixtures; C the witness on `2×3`, the cube and the plaquette; D the trees; E the plaquette identities (general identity, explicit laws, types, the class ratios, the rank); F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=22 FAIL=0`.
