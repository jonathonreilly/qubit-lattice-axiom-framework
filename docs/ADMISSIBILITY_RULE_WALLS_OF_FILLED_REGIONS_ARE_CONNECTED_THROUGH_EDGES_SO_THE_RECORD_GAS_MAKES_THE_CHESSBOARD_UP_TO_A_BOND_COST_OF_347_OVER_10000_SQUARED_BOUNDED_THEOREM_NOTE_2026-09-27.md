---
claim_id: admissibility_rule_walls_of_filled_regions_are_connected_through_edges_so_the_record_gas_makes_the_chessboard_up_to_a_bond_cost_of_347_over_10000_squared_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 117 as landed (the supplied six-content grand-canonical record gas with chessboard frames; its wall-removing map with weight ratio at most x^|dV|, x = g^(1/2) Lambda (Lambda/m)^(5/6) max(H, 1/H)^(1/6); the ray anchor giving at most |dV|/4 starting plaquettes; P(sigma_x = -1) <= sum_V x^|dV|): (T1) for every finite nonempty face-connected V in Z^3 whose complement is face-connected, the wall (the plaquettes between V and its complement) is connected through shared edges, with 12 edge-neighbours per plaquette; a cavity or a vertex-only touch splits it; (T2) so the regions around a site with |dV| = k number at most (k/4) r_k, r_k = (12/(k - 1)) C(11k, k - 2), the coefficients of U + U^2 with U = x(1 + U)^11, whose radius is 10^10/11^11; (T3) at x0 = 347/10000 the sum over regions around a site of x0^|dV| is at most 11/100 (the small regions counted exactly, U bounded by the supersolution 43/500), so for x <= 347/10000 the A-framed state has <sigma_x> >= 39/50 and the B-framed state <= -39/50; at zeta = g^-3, H = 1, this holds for g <= (347/10000)^2 = 120409/10^8 without contents, and every threshold of block 117 grows by the factor (347/120)^2 = 120409/14400. A harvest of probe #9212 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9338, Grok); the supervisor's certificate tightens the attempt's 0.143 to 11/100. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_the_record_gas_does_make_the_chessboard_when_a_recorded_bond_costs_a_factor_below_nine_over_62500_and_the_two_framed_states_differ_at_every_site_bounded_theorem_note_2026-09-24
runner: scripts/admissibility_rule_walls_of_filled_regions_are_connected_through_edges_so_the_record_gas_makes_the_chessboard_up_to_a_larger_bond_cost_2026_09_27.py
---

# Walls of filled regions are connected through edges, so the record gas makes the chessboard up to a bond cost of (347/10000)²

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 117 as landed; a harvest of probe #9212, confirmed by an other-family referee in #9338, with a tightened certificate; nothing adopted or registered; unaudited)

This note works within block 117 as landed on main (the record gas, its chessboard frame and its wall-removing map) and replaces its wall-connectivity step by a stronger one; it reports how far block 117's chessboard bound extends; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 117 (landed) showed that the record gas makes block 79's chessboard when a recorded bond is expensive: `g ≤ 9/62500` without contents. Its wall count connects each wall through shared vertices, where each plaquette has 32 neighbours. This note, a harvest of a probe result another model family has confirmed, connects walls through shared edges, where each plaquette has only 12 neighbours.

- **T1: walls are connected through edges.** Take a finite region of the cubic lattice that is face-connected and whose outside is face-connected. Its wall is connected through shared edges. A cavity, or two cubes touching only at a corner, would split it.
- **T2: fewer trees.** So the walls of area `k` around a site number at most `(k/4) r_k`, with `r_k = (12/(k − 1)) C(11k, k − 2)`. This count has radius `10¹⁰/11¹¹ ≈ 0.035`, where block 117's had `30³⁰/31³¹ ≈ 0.012`.
- **T3: a larger region.** At `x₀ = 347/10000` the defect sum is at most `11/100`. So:
  - for `x ≤ 347/10000` the two framed states have `⟨σ_x⟩ ≥ 39/50` and `≤ −39/50`;
  - without contents the chessboard holds for `g ≤ (347/10000)² ≈ 1.2·10⁻³`, which is `(347/120)² ≈ 8.36` times block 117's bound;
  - every content case's threshold grows by the same factor.

In plain terms: to show the records settle into the chessboard, one counts the ways a patch of the wrong pattern can sit around a site. Each patch is outlined by a wall. Walls turn out to hang together through their edges, not just their corners, so there are far fewer ways to draw one. That lets the argument work when recorded bonds are about eight times cheaper than before.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-27.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The gas, its weights and its frame are supplied clauses. Nothing is adopted.
- **Block 117 (landed on main).** Quoted by the runner (A3).
  - T3: the wall-removing map, with weight ratio at most `x^{|∂V|}`, where `x = g^{1/2}Λ(Λ/m)^{5/6} max(H, 1/H)^{1/6}`.
  - T4(b): the wall meets the `e₁` ray from `x` within `|∂V|/4` sites, and its tree count is `r_k = (32/(k − 1)) C(31k, k − 2)`.
  - T4(c): the certificate `0.0897` at `x₀ = 3/250`.
  - T5: `P(σ_x = −1) ≤ Σ_V x^{|∂V|}`, and `x ≤ x₀` means `g³Λ⁶(Λ/m)⁵ ≤ x₀⁶` at `ζ = g⁻³`, `H = 1`.
  - Block 117 proves vertex-connectivity of walls by a colouring argument. This note replaces that step by edge-connectivity.
- **Names.** The count of breadth-first port trees uses series inversion, as in block 117. The parity construction of a region from its wall is the lattice form of the separation of space by a closed surface.

## Domain qualifications

- The regions `V` are filled: finite, nonempty and face-connected, with a face-connected complement. These are the regions block 117's map uses.
- The thresholds are those of block 117's grand-canonical gas at `ζ = g⁻³`. The half-filling window with contents is not re-run.
- These are conditional statements within supplied clauses, not a physical identification.

## Theorem T1 — walls are connected through edges

*Statement.*
- Let `V ⊂ ℤ³` be finite, nonempty and face-connected, with a face-connected complement. Then its wall, the plaquettes between `V` and its complement, is connected through shared edges.
- Each plaquette shares an edge with 12 others.
- A cavity (a `3 × 3 × 3` block minus its centre) splits the wall into two edge-components, and so does a touch at a corner only. A touch along an edge only does not split it.

*Proof.*
1. Suppose the wall splits into nonempty parts `S_A` and `S_B`, with no plaquette of one sharing an edge with the other.
2. All wall plaquettes at a lattice edge share that edge, so they lie in the same part. Each edge lies on 0, 2 or 4 wall plaquettes. So each part meets every edge an even number of times: it is a cycle modulo 2.
3. Every finite cycle modulo 2 of plaquettes is the wall of exactly one finite cube set. That set is the cells whose `+e₁` ray crosses the cycle an odd number of times. So `S_A = ∂U_A` and `S_B = ∂U_B`, and `V = U_A Δ U_B`.
4. No plaquette lies in both walls. So two face-adjacent cubes never differ in both memberships.
5. Two face-adjacent cubes of `V` therefore have the same type, `U_A` without `U_B` or the reverse. By the face-connectedness of `V`, all of `V` has one type, say `V ⊆ U_A ∖ U_B`. Hence `U_B ⊆ U_A`.
6. The complement is `U_B` together with the outside of `U_A`, and a cube of one differs from a cube of the other in both memberships. By the face-connectedness of the complement, one of them is empty. The outside of the finite set `U_A` is not, so `U_B` is empty, and `S_B = ∂U_B` is empty. This is a contradiction.

- The runner checks every fixed polycube of 1 to 7 cells (27622 shapes) and the three examples (B1).
- It checks the parity construction on 60 random cube sets (B2). ∎

## Theorem T2 — fewer trees

*Statement.*
- The regions `V` around a site with `|∂V| = k` number at most `(k/4) r_k`, with `r_k = (12/(k − 1)) C(11k, k − 2)` for `k ≥ 2` and `r_1 = 1`.
- These are the coefficients of `U + U²` with `U = x(1 + U)^{11}`. The radius is `10¹⁰/11¹¹`.

*Proof.*
- A region is determined by its wall (T1, step 3).
- The wall meets the `e₁` ray within `|∂V|/4` plaquettes (block 117 T4(b)). By T1 it is connected through shared edges.
- A breadth-first spanning tree with a fixed ordering of the 12 ports has at most 12 children at the root and 11 at the other vertices. So rooted walls of area `k` inject into port trees, counted by `x(1 + U)^{12} = U + U²` with `U = x(1 + U)^{11}`.
- The coefficients follow by series inversion (C1, checked to `k = 15`). `u/(1 + u)^{11}` is largest at `u = 1/10`, where it is `10¹⁰/11¹¹`. ∎

## Theorem T3 — a larger region

*Statement.*
- At `x₀ = 347/10000`, `Σ_{V∋x} x₀^{|∂V|} ≤ 11/100`; it is about 0.1098.
- For `x ≤ 347/10000`, every site of every framed box has `P(σ_x = −1) ≤ 11/100`. So the A-framed state has `⟨σ_x⟩ ≥ 39/50`, the B-framed state has `⟨σ_x⟩ ≤ −39/50`, and any limits of the two differ.
- At `ζ = g⁻³` with `H = 1`, this holds without contents for `g ≤ (347/10000)² = 120409/10⁸`. That is `(347/120)² = 120409/14400 ≈ 8.36` times block 117's `9/62500`.
- At fixed contents every threshold of block 117 grows by the same factor, since `x` scales as `g^{1/2}`.

*Proof.*
- **Small regions.** The regions around a site with `|∂V| ≤ 22` are counted exactly: `{6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538}`. Seven cells already need `|∂V| ≥ 24` (D1).
- **The tail.** `U₊ = 43/500` satisfies `x₀(1 + U₊)^{11} ≤ U₊ < 1/10`, so `U(x₀) ≤ U₊`. Also `x R′(x) = U(1 + U)(1 + 2U)/(1 − 10U)` increases with `U`. So the regions with `|∂V| ≥ 24` contribute at most `¼[U₊(1 + U₊)(1 + 2U₊)/(1 − 10U₊) − Σ_{k≤23} k r_k x₀^k]`.
- **The total** is at most `11/100` in exact rationals (D1).
- **The rest** is block 117 T3 and T5 unchanged: the map is injective, and `P(σ_x = −1) ≤ Σ_V x^{|∂V|}`. ∎

The attempt printed `0.143` at the same `x₀`. The exact supersolution here gives `11/100`. At block 117's own `x₀ = 3/250`, the edge count gives at most `4/10000` in place of block 117's `0.0897`, with the supersolution `3/200` (D1). So there `⟨σ_x⟩ ≥ 999/1000`. Any certificate of this form stops at `x₀ < 10¹⁰/11¹¹`, that is, `g < (10¹⁰/11¹¹)² ≈ 1.23·10⁻³` without contents.

## What this settles and what it does not

- **Settled.** Within block 117's gas, the chessboard holds for recorded-bond costs up to `(347/10000)²` without contents, about 8.4 times block 117's range, with every content case scaled alike.
- **For landed block 117.** Its bounds stand. This note enlarges them and replaces its vertex count by an edge count.
- **Not settled.**
  - The half-filling window with contents.
  - Canonical ensembles.
  - The walker's gap on the gas's arrangements.
  - Costs above `(10¹⁰/11¹¹)²`, which this method cannot reach.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 117 as landed: the chessboard for g <= 9/62500; its open item, edge-connected walls (g ~ 1.2e-3)"
source_of_blocker_text: block 117's open items; probes task J:derive:edge-connected-walls-of-simply-connected-regions
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the half-filling window with contents; the walker's gap on the gas's arrangements"
conditional_surface_status: "exact within block 117's grand-canonical gas and frames"
hypothetical_axiom_status: "the gas, its weights, its contents and its frame are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.** Block 117 (landed): the map, the ray anchor, the 32-port count, and the certificate at `3/250`. Its open items included edge-connected walls.
- **Probes.**
  - #9212, worker `w-macbookpro9927a-j904f`, Claude Opus 5.5, the supervisor's own model family, proved T1 and redid block 117's certificate with 12 ports: `0.143` at `x₀ = 347/10000`.
  - #9338, worker `w-macbookpro90c72-je1df`, `grok-4.6`, another model family, refereed #9212 with its own checker: "HIT: confirmed - the wall of a finite face-connected set in `Z³` with face-connected complement is edge-connected, and the 12-neighbour certificate gives `g* = (347/10000)²` without contents."
- **In the literature.** Connectivity of the boundary of a simply connected lattice region is a classical ingredient of contour (Peierls) arguments. Counting connected sets by spanning trees is standard. Both enter here at definition level, with T1 proved in full.
- **New here.**
  - The harvest.
  - The exact supersolution certificate `11/100`, tightening the attempt's `0.143`.
  - The statement for every content case as the common factor `(347/120)²`.
- **Provenance.** Found by the supervisor's family and confirmed by another family. The tightened certificate is the supervisor's and is exact.

## Exact target and obligation graph

Target: how far block 117's chessboard bound extends. The obligations are:
- (O1) the premises (A3);
- (O2) edge-connected walls (B1–B2);
- (O3) the count (C1);
- (O4) the certificate and thresholds (D1).

## No-Go Discipline Gate

The note's negative sentence: no defect has probability above `11/100` at any site for `x ≤ 347/10000`.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A filled region with a disconnected wall.* T1 excludes it; the examples show that each hypothesis is needed. ATTEMPTED.
2. *More walls than the tree count allows.* The injection into port trees bounds them (T2). ATTEMPTED.
3. *The series leaves its disk.* `x₀ < 10¹⁰/11¹¹`, and the supersolution is exact. ATTEMPTED.

Scope left open:
- the half-filling window with contents;
- costs beyond this method's limit.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The filled-region hypotheses are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 117 (landed) | the map, the ray anchor, the injective sum, the threshold relation | yes (quoted, A3) |
| probe #9212 and referee #9338 | T1 and the 12-port count, with its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "walls are edge-connected; the chessboard for `g ≤ (347/10000)²`" | executed: 12 edge-neighbours; the walls of the examples | executed: regions with `|∂V| ≤ 22` counted | executed: the series to `k = 15`; the radius | executed: all polycubes to 7 cells; ray parity; the certificate | not executed: the half-filling window; canonical ensembles |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 117 already proved wall connectivity."
  - *Reply:* It proved connectivity through vertices, with 32 neighbours.
  - Edges give 12 neighbours. The count's radius rises from `0.012` to `0.035`, and the threshold rises about eightfold.
- *Objection:* "`39/50` is weaker than block 117's `0.82`."
  - *Reply:* It holds over a range about 8.4 times larger in `g`.
  - At block 117's own `x₀ = 3/250` the edge count gives a defect sum of at most `4/10000`, against block 117's `0.0897`.

### N8 — Cross-cycle echo
- Block 117: vertex-connected walls, `g ≤ 9/62500`.
- This note: edge-connected walls, `g ≤ (347/10000)²`.

## Falsifiers

- A finite face-connected region of `ℤ³` with face-connected complement whose wall is not connected through edges.
- A framed box and `x ≤ 347/10000` with `P(σ_x = −1) > 11/100` at some site.

## Boundaries and non-claims

- Block 117's gas, frames and map.
- The gas, its weights and its contents are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 117 (landed), restated and quoted.
- Named standard imports, at definition level:
  - series inversion for tree counts;
  - breadth-first spanning trees;
  - parity of ray crossings;
  - exact rational arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.**
  - Probe #9212 (Claude Opus 5.5) was refereed by #9338 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner and tightened the certificate with an exact supersolution.
- **Before writing.** Origin was re-fetched. Block 117 was read as landed, including its colouring argument for vertex-connectivity. The own prior-art check covered memory (block 117's open items list edge-connected walls), the held branches, open PRs and main.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_walls_of_filled_regions_are_connected_through_edges_so_the_record_gas_makes_the_chessboard_up_to_a_larger_bond_cost_2026_09_27.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
