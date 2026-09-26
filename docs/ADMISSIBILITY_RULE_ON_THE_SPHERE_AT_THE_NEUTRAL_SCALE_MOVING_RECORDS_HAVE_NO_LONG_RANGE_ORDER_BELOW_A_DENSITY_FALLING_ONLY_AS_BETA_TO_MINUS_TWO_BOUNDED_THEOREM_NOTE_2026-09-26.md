---
claim_id: admissibility_rule_on_the_sphere_at_the_neutral_scale_moving_records_have_no_long_range_order_below_a_density_falling_only_as_beta_to_minus_two_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 126's law with vacancies as landed, on the sphere menu (uniform probability measure) at the neutral scale c0 = beta/sinh beta, on every even cubic torus: (T1) the occupied set is a gas of clusters (connected sets with no bond between different clusters) with weights w(A) = z^|A| I(A), I(A) the contents' integral of prod_(bonds in A) c0 e^(beta s.s'); a spanning tree integrates to exactly 1, and each of the at most 2|A| + 1 other bonds costs at most c0 e^beta = 2 beta/(1 - e^(-2 beta)), so w(A) <= c0 e^beta zeta^|A| with zeta = z (c0 e^beta)^2; (T2) the probability that A is the origin's cluster is at most w(A), and at most 36^(n-1) connected sets of n sites contain the origin, so for 36 zeta < 1, sum_x |<sigma_0.sigma_x>| <= c0 e^beta zeta/(1 - 36 zeta)^2: no long-range order and a bounded structure factor for z < z1(beta) = (1 - e^(-2 beta))^2/(144 beta^2); (T3) z1 -> 1/36 as beta -> 0 and z1 ~ 1/(144 beta^2), so against block 168's 1/(4 F_6(beta)) ~ 3/(64 beta^5) the ratio is ~ (4/27) beta^3 and the region falls only as beta^-2. The supervisor's own derivation (Claude Opus 5.5), unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_with_vacancies_the_infrared_stiffness_is_set_by_the_binding_scale_long_range_order_above_the_neutral_scale_and_no_full_bound_at_it_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_on_the_sphere_at_the_neutral_scale_moving_records_have_no_long_range_order_below_a_density_falling_as_beta_to_minus_two_2026_09_26.py
---

# On the sphere at the neutral scale, moving records have no long-range order below a density that falls only as β⁻²

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 126's law with vacancies on the sphere menu at its neutral scale; the supervisor's own derivation, not refereed by another model family; nothing adopted or registered; unaudited)

This note works within block 126 as landed on main (the law with vacancies, its sphere menu and its neutral scale) and places block 168 (a pushed branch); it reports a density below which moving records on the sphere at the neutral scale have no long-range order; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 168 (pushed) found no long-range order on the sphere at the neutral scale for `z < 1/(4F₆(β))`. That region falls as `β⁻⁵`, because it bounds every site by its worst neighbourhood: six aligned neighbours, whose weight grows like `β⁵`. This note counts whole clusters instead.

- **T1: clusters are cheap.** The occupied set is a gas of clusters: connected sets with no bond between different clusters.
  - At the neutral scale, the bonds of a spanning tree integrate to exactly 1.
  - Each other bond costs at most `c₀e^β = 2β/(1 − e^{−2β})`, which grows only like `2β`.
  - A cluster of `n` sites has at most `2n + 1` such bonds, so its weight is at most `c₀e^β ζⁿ`, with `ζ = z(c₀e^β)²`.
- **T2: no long-range order below `z₁(β) = (1 − e^{−2β})²/(144β²)`.**
  - The chance that a given set is the origin's cluster is at most its weight.
  - At most `36^{n−1}` connected sets of `n` sites contain the origin.
  - So `Σ_x |⟨σ₀·σ_x⟩| ≤ c₀e^β ζ/(1 − 36ζ)²` on every even torus when `36ζ < 1`.
- **T3: the gain.** `z₁ → 1/36` as `β → 0`, and `z₁ ∼ 1/(144β²)`. Against block 168's region the ratio grows like `(4/27)β³`.
  - So the sphere's low-density region falls only as `β⁻²`.
  - Together with block 168, there is no long-range order for `z < max(1/(4F₆(β)), z₁(β))`.

In plain terms: a single site can have an unusually heavy neighbourhood, but a whole island of records gains only a little weight per bond once the average over orientations is taken. So islands stay rare, and cannot line up across the lattice, at densities much higher than the site-by-site bound allowed when the binding is strong.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The law with vacancies, its weights and the menu are supplied clauses. Nothing is adopted.
- **Block 126 (landed on main).** Quoted by the runner (A3).
  - Each site of an even torus is empty with weight 1, or holds a content `s ∈ S²` with weight `z` times the uniform measure, taken as the probability measure.
  - The kernel is `1` with an empty end and `c e^{βs·s′}` between contents, and the neutral scale is `c₀ = β/sinh β`.
  - The diagnostic is `σ_x = n_x s_x` and `M_N² = N⁻¹Σ_x⟨σ₀·σ_x⟩`.
- **Block 168** (pushed branch, not landed): the region `1/(4F₆(β))` and the cluster decoupling, restated in T2. Placement.

## Domain qualifications

- `β > 0`, `z ≥ 0`, at the neutral scale exactly, on the sphere menu with the probability measure. The torus is even and cubic.
- Low density only. The window between low and high density, and the sphere at high density, are not covered.
- On the two-valued menu this method gives `z < 1/288`, which is weaker than block 168's `1/256`. The gain is specific to the sphere, where the worst single-site weight grows with `β`.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — clusters are cheap

*Statement.*
- The law of the occupied set `O` is `∝ Π_{clusters A of O} w(A)`, where `w(A) = z^{|A|} I(A)` and `I(A) = ∫ Π_{bonds in A} c₀e^{βs·s′} Π_{x∈A} dμ(s_x)`. Different clusters are neither overlapping nor joined by a bond.
- `I(A) ≤ (c₀e^β)^{|E(A)| − |A| + 1} ≤ (c₀e^β)^{2|A|+1}`, so `w(A) ≤ c₀e^β ζ^{|A|}` with `ζ = z(c₀e^β)²`.

*Proof.*
- Bonds with an empty end weigh 1, so the contents' integral factorizes over the clusters of `O`.
- Choose a spanning tree of `A`. Bound each other bond by its largest value, `c₀e^β = 2β/(1 − e^{−2β})` (B1).
- Integrate the tree from its leaves. Each leaf gives `c₀⟨e^{βs·s′}⟩ = c₀ sinh β/β = 1` (B1), so the tree integrates to exactly 1.
- Each site has 6 neighbours, so `|E(A)| ≤ 3|A|`, and at most `2|A| + 1` bonds lie off the tree (B2, checked on every connected set through 6 sites). ∎

## Theorem T2 — no long-range order below `z₁(β)`

*Statement.* For `36ζ < 1`, on every even torus, `Σ_x |⟨σ₀·σ_x⟩| ≤ c₀e^β ζ/(1 − 36ζ)²`. So there is no long-range order, and `⟨|σ̂(k)|²⟩` is bounded uniformly in `k` and `L`, for `z < z₁(β) = 1/(36(c₀e^β)²) = (1 − e^{−2β})²/(144β²)`.

*Proof.*
1. **One cluster's chance.** The configurations in which `A` is a cluster are `A` together with any configuration of clusters away from `A` and its neighbours. All weights are positive. So `P(A is a cluster) = w(A) Z′/Z ≤ w(A)`, where `Z′` is the partition function away from `A` and its neighbours. This is checked by full enumeration on a ring of six (C2).
2. **Clusters decouple.** A common rotation of one cluster's contents keeps every bond weight (block 168 T2). So `|⟨σ₀·σ_x⟩| ≤ P(0 ↔ x)`.
3. **Counting.**
   - A connected set of `n` sites containing the origin is determined by the closed walk of `2(n − 1)` steps around one of its spanning trees. So there are at most `36^{n−1}` of them; the exact counts for `n ≤ 6` are 1, 6, 45, 344, 2670 and 20886 (C1).
   - A connected set on the torus lifts to one on `ℤ³`, so the count holds on every torus.
4. **The sum.**
   - `Σ_x P(0 ↔ x) ≤ Σ_{A∋0} |A| w(A) ≤ c₀e^β Σ_n n 36^{n−1} ζⁿ`.
   - `Σ_n n 36^{n−1} ζⁿ = ζ/(1 − 36ζ)²` (C1). ∎

## Theorem T3 — the gain

*Statement.* `z₁(β) → 1/36` as `β → 0`, `β²z₁(β) → 1/144` as `β → ∞`, and `4F₆(β) z₁(β)/β³ → 4/27`.

*Proof.* By exact limits (D1). ∎

So at large `β` the cluster bound's region exceeds block 168's by a factor of order `β³`. At small `β`, block 168's `1/4` is larger than `1/36`.

## What this settles and what it does not

- **Settled.** On the sphere at the neutral scale, the low-density region falls only as `β⁻²`, not `β⁻⁵`.
- **For block 168** (pushed). Its region stands. This note adds a larger region at large `β`.
- **Not settled.**
  - The window between low and high density.
  - The sphere at high density.
  - Sharper counts. Using the true growth rate of lattice animals, about 8.35 in place of 36, would enlarge the region by a constant factor but not change `β⁻²`.
  - Whether `β⁻²` is the true behaviour.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 168 (pushed): the sphere's low-density region falls as beta^-5 because the worst neighbourhood bound is attained; probes task the-neutral-law-window-by-conditional-neutrality"
source_of_blocker_text: block 168 and probes refill ac
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; the window between low and high density; the sphere at high density"
conditional_surface_status: "exact at the neutral scale of block 126's law on the sphere, low density"
hypothetical_axiom_status: "the law with vacancies, its weights and the menu are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 126 (landed): the law and the neutral scale.
  - Block 168 (pushed; a harvest of #9304 with #9329): the region `1/(4F₆(β))` and the cluster decoupling.
- **Probes.** Refill ac posed the task `the-neutral-law-window-by-conditional-neutrality`, asking for a region falling more slowly than `β⁻⁵`. This note answers that at low density. The task stays open for a referee and for the window.
- **In the literature.** Treating occupied clusters as a hard-core gas of connected sets, and bounding a cluster's probability by its activity, is a standard polymer-gas argument. Counting lattice animals by spanning-tree walks is standard. Both are used at definition level.
- **New here.** The observation that at the neutral scale a spanning tree integrates to exactly 1, so a cluster pays only for its extra bonds, and the resulting `β⁻²` region.
- **Provenance.** The supervisor's own derivation, the same family as block 168's finder. No other-family check yet.

## Exact target and obligation graph

Target: the sphere's low-density region at the neutral scale. The obligations are:
- (O1) the premises (A3);
- (O2) the cluster weights (B1–B2);
- (O3) the cluster gas and the counting (C1–C2);
- (O4) the region and its comparison (D1).

## No-Go Discipline Gate

The note's negative sentence: no long-range order on the sphere at the neutral scale for `z < z₁(β)`.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *Clusters with many loops cost more than trees.* Every extra bond is bounded by `c₀e^β`, and there are at most `2n + 1` of them (B2). ATTEMPTED.
2. *A cluster's probability exceeds its weight.* Positivity of all weights forbids it (C2 checks a case exactly). ATTEMPTED.
3. *Torus wrapping creates more connected sets.* They lift to `ℤ³` (step 3). ATTEMPTED.

Scope left open: the window; the sphere at high density.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The probability normalization of the sphere's measure is declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 126 (landed) | the law, the sphere menu, the neutral scale | yes (quoted, A3) |
| block 168 (pushed) | the cluster decoupling; the region compared | yes (decoupling, restated); placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "no long-range order below `z₁(β) ∼ 1/(144β²)`" | executed: the leaf integral; the largest bond weight | executed: bonds off a spanning tree, all sets through 6 sites | executed: animal counts through 6 sites; the series | executed: the cluster-gas inequality on a ring of six; the limits | not executed: the window; high density |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 168's worst case is attained, so no better region exists."
  - *Reply:* The worst case is attained for a single site's conditional weight.
  - A whole cluster's weight averages its bonds over orientations, and a tree averages to exactly 1. The single-site bound is not the limit of every method.
- *Objection:* "`36` is crude."
  - *Reply:* Yes. It changes the constant, not the power of `β`.

### N8 — Cross-cycle echo
- Block 168: `β⁻⁵` from the worst neighbourhood.
- This note: `β⁻²` from clusters.

## Falsifiers

- A connected set `A` on the sphere at the neutral scale with `I(A) > (c₀e^β)^{|E(A)| − |A| + 1}`.
- An even torus and `z < z₁(β)` with `Σ_x|⟨σ₀·σ_x⟩|` above the stated bound.

## Boundaries and non-claims

- The sphere menu at the neutral scale, at low density.
- The law, the weights and the menu are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 126 (landed), restated and quoted. Block 168 (pushed), placed.
- Named standard imports, at definition level:
  - the polymer-gas inequality `P(A is a cluster) ≤ w(A)` for positive weights;
  - counting connected sets by spanning-tree walks;
  - the geometric series;
  - exact symbolic and rational arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-26, near the end of the owner's 12-hour campaign.
- **Provenance.** The supervisor's own derivation, after harvesting block 168. It is unrefereed, and a referee should come from another family.
- **Before writing.** Origin was re-fetched. Block 126 was read as landed. The own prior-art check covered memory, the probes tasks and block 168. It found no cluster-level bound at the neutral scale.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_on_the_sphere_at_the_neutral_scale_moving_records_have_no_long_range_order_below_a_density_falling_as_beta_to_minus_two_2026_09_26.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
