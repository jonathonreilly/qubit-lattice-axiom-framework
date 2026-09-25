---
claim_id: admissibility_rule_the_record_gas_does_make_the_chessboard_when_a_recorded_bond_costs_a_factor_below_nine_over_62500_and_the_two_framed_states_differ_at_every_site_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "WITHIN block 81's record gas as landed on main (records on Z^3, one per site, six-axis contents with pair weights p, q, r, bond scale g and activity zeta = 6z; the law zeta^N g^B Q with Q = E_uniform prod_bonds M, M = 6 omega/(p + q + 4r)), all supplied. Exact: (T1) on a box framed by the A-chessboard, at zeta = g^-3 H the law is H^N g^(#unlike/2) Q up to a constant; without contents it is complement-symmetric at zeta = g^-3 and even tori are exactly half filled. (T2) contents act on cycles and merges only: Q = 1 on forests, Q <= Lambda^(cycle rank), and identifying two records multiplies Q by 1 across components and by at least (m/Lambda)^deg within one; on p + q = 2r contents only add weight. (T3) translating a cluster of out-of-step sites, with its holes, by one step drops the unlike bonds by exactly the wall size |dV|, and with the direction chosen from V alone lowers the weight by at least x^|dV|, x = g^(1/2) Lambda (Lambda/m)^(5/6) max(H, 1/H)^(1/6). (T4) the regions V around a site are counted exactly to |dV| = 22 and beyond by a tree bound on vertex-connected walls (wall connectedness imported); at x0 = 3/250 the sum over V of x0^|dV| is at most 0.0897. (T5) for x <= 3/250 the A-framed state has <sigma_x> >= 0.82 and the B-framed <= -0.82 at every site of every box, so any limits of the two differ: at zeta = g^-3 this holds for g <= 9/62500 without contents, g <= 10^-5 at (3,1,2), 1.8 10^-5 at (5,2,4), 1.9 10^-7 at (12,1,2) and 9.7 10^-5 at (9,8,8). Harvest block from two Grok-refereed probes attempts, re-checked by an independent runner. Block 79's coupling of the walk to the chessboard remains supplied; whether the walk's gap survives the gas's defects is not treated. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_record_gas_does_make_the_chessboard_when_a_recorded_bond_is_expensive_a_wall_counting_bound_2026_09_24.py
---

# The record gas does make the chessboard when a recorded bond is expensive: at ζ = g⁻³ its two framed states differ at every site for g ≤ 9/62500 without contents, and for g ≤ 10⁻⁵ at (3,1,2)

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 81's record gas as landed, with one named topological import; harvest block from two Grok-refereed probes attempts; nothing adopted or registered; unaudited)

This note works within block 81's record gas, as landed on main; it reports that the gas makes the chessboard of block 79 when a recorded bond is expensive, with explicit bond scales, and what contents do to that; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 79, as landed, found that a chessboard of records gives the walk a rest mass through a supplied site coupling. It states: "No formation or ordering of that configuration is derived." Block 81, as landed, keeps only finite statements about the record gas: "Finite symmetry is not absence of order." This note asks whether the gas makes the chessboard.

- **T1: the gas as a count of unlike bonds.** Call a bond *unlike* when its two ends have the same occupancy, so the chessboard has none.
  - At activity `ζ = g⁻³H` the law is `H^N g^{#unlike/2} Q`, up to a constant, on a box framed by the chessboard.
  - Without contents the gas is exactly half filled at `ζ = g⁻³`.
- **T2: contents act on cycles and merges only.** The content factor `Q` is 1 on forests and at most `Λ` per independent cycle. Identifying two records costs at most `(Λ/m)` per bond.
- **T3: a map that removes a wall.**
  - Take the cluster of out-of-step sites at a site, with its holes filled (`V`), and translate it by one step.
  - This removes exactly its wall: the unlike bonds drop by `|∂V|`.
  - With the direction chosen from `V` alone, the weight drops by at least `x^{|∂V|}`, where `x = g^{1/2} Λ (Λ/m)^{5/6} max(H, 1/H)^{1/6}`.
- **T4: counting walls.** The regions `V` around a site are counted exactly up to `|∂V| = 22`, and beyond that by a tree bound. At `x₀ = 3/250` the sum of `x₀^{|∂V|}` over all of them is at most `0.0897`.
- **T5: two chessboard states.**
  - For `x ≤ 3/250`, the box framed by the A-chessboard has staggered order `⟨σ_x⟩ ≥ 0.82` at every site. The box framed by the B-chessboard has `⟨σ_x⟩ ≤ −0.82`.
  - At `ζ = g⁻³` this holds for `g ≤ 9/62500` without contents and for `g ≤ 10⁻⁵` at `(3,1,2)`.

In plain terms, if putting two records next to each other is made very expensive, the records settle into the chessboard: every other site filled, like the black squares of a board. The price must be steep, a factor below about 1/7000 per neighbouring pair, and steeper still, about 1/100000, once the records carry the six-axis contents. The proof is the standard one: any patch that is out of step with the chessboard has a boundary, and every unit of that boundary costs a factor the patch cannot pay back. So the gas can supply the background that block 79 needs for a rest mass. What it does not supply is the price itself, which is put in by hand, and the coupling by which a chessboard reaches the walk. It is also not shown that the walk's gap survives the gas's own defects.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." This is the gas's exclusion.
  - "Each site has a domain of local possibilities." Here that means six-axis contents.
  - "Admissibility is not a dynamics axiom." The gas and its weights are supplied clauses. Nothing is adopted.
- **The gas** (block 81 as landed).
  - Records sit on `ℤ³`, one per site. Each carries a content `s` among the six unit axis vectors.
  - Pair weights are `p, q, r` for equal, opposite and orthogonal contents, giving `M(s, s') = 6ω(s, s')/(p + q + 4r)`.
  - `Q(G) = E_uniform[Π_{bonds of G} M(s_x, s_y)]` over independent uniform contents, `G` being the graph of recorded bonds (both ends recorded). `Λ = max M` and `m = min M`.
  - At bond scale `g` and activity `ζ = 6z`, an arrangement with `N` records and `B` recorded bonds weighs `ζ^N g^B Q`.
  - With `p = q = r`, `M ≡ 1` and there are no contents.
- **The chessboards.** `A` is the even sublattice, `x₁ + x₂ + x₃` even. The A-chessboard occupies `A` and leaves `B` empty.
  - `σ_x = +1` when site `x` agrees with the A-chessboard, and `−1` otherwise.
  - A bond is *unlike* when `σ` differs across it. Equivalently, its ends have the same occupancy.
- **Framed boxes.** A finite box is surrounded by the A-chessboard, held fixed, with the frame records' contents summed.
- **The map.** `C` is the cluster of `σ = −1` sites (connected through faces) at a site `x`. `V` is `C` together with the finite components of its complement, and `∂V` is the set of bonds leaving `V`. The front is `(V + d) ∖ V`, and the back is `V ∖ (V + d)`.

## Theorem T1 — the gas as a count of unlike bonds

*Statement.*
- (a) On a framed box, `B − 3N = (#unlike − #bonds)/2 + const`, the sums running over the bonds that meet the box. So at `ζ = g⁻³H` the law is `∝ H^N g^{#unlike/2} Q`.
- (b) On an even torus without contents, `n → 1 − n` sends `B` to `3V − 6N + B`. So `ζ^N g^B` is complement-symmetric exactly at `ζ = g⁻³`, and the gas is exactly half filled there.

*Proof.*
- (a) Over the bonds meeting the box, `n_x n_y − (n_x + n_y)/2` is `−1/2` on bonds with exactly one end occupied and `0` otherwise. Summing gives `B − 3N − (frame terms) = −(#bonds − #unlike)/2`.
- (b) On a 6-regular graph, `Σ_b (n_x + n_y) = 6N`, so the bonds with both ends empty number `3V − 6N + B`. ∎

*Checked (B1, B2).* (a) takes one value over 60 sampled arrangements of the framed `4³` box. (b) holds on 60 arrangements of the `4³` torus.

## Theorem T2 — what contents do

*Statement.*
- (a) `Q = 1` on forests. `Q ≤ Λ^{c(G)}`, where `c(G)` is the cycle rank. Adding a bond between two components multiplies `Q` by exactly 1.
- (b) On the line `p + q = 2r`, contents only add weight: `Q ≥ 1`, and adding a bond never lowers `Q`.
- (c) Identifying two non-adjacent records `u, v` multiplies `Q` by `6P(s_u = s_v)`. This is exactly 1 across components, and at least `(m/Λ)^{deg v}` within one.

*Proof.*
- (a) Adding a bond multiplies `Q` by the current expectation of `M(s_x, s_y)`, which lies in `[m, Λ]`. Across components the two contents are independent and uniform, and the rows of `M` sum to 6, so the factor is 1. Leaves average to 1.
- (b) On `p + q = 2r`, `M = 1 + 3λ₁ s·s'`. Expanding `Π(1 + 3λ₁ s_x·s_y)` gives products of single-site monomial means, and each of these is 0, 1 or 1/3.
  - For `λ₁ ≥ 0` every term is non-negative.
  - For `λ₁ < 0`, flip `s` on one sublattice.
- (c) The conditional law of `s_v` given its neighbours is `∝ Π_w M(·, s_w)`, so every value has conditional probability at least `m^{deg}/(6Λ^{deg})`. ∎

*Checked (C1, C2).*
- (a): every set of at most 6 sites of the `2×2×2` cube, at `(3,1,2)` and `(12,1,2)`, together with `M = J + 6λ₁P₁ + 6λ₂P₂` at five triples.
- (b): every bond set on at most 5 cube sites, at `(3,1,2)` and `(1,3,2)`.
- (c): every non-adjacent pair, at most 6 sites.

## Theorem T3 — a map that removes a wall

*Statement.* On a framed box, let `σ_x = −1`, and translate `V` by a unit vector `d`. Set `n'(y) = n(y − d)` on `V + d`, put the A-chessboard on the back layer, and leave `n` elsewhere. Then:
- (a) every bond of `∂V` is unlike, and the unlike bonds drop by exactly `|∂V|`;
- (b) `N' − N = #(back ∩ A) − #(front ∩ A)`, at most the number of runs of `V` along `d` in absolute value;
- (c) `σ(y) = −σ'(y + d)` on `V`, so the map is injective once `(V, d)` is fixed. The frame is untouched;
- (d) `Q(n)/Q(n') ≤ Λ^{|D|+|F|}(Λ/m)^{5|F|}`. Here `F` is the set of occupied wall bonds along `d`, which are contracted, and `D` is the set of the other occupied wall bonds, which are deleted;
- (e) the fronts of the six directions have sizes `f_d(V)` summing to `|∂V|`, and so do the runs. Choose `d` from `V` alone so that it minimises `|N' − N| log max(H, 1/H) + 5 f_d log(Λ/m)`. Then `w(n)/w(n') ≤ x^{|∂V|}`, with
  `x = g^{1/2} Λ (Λ/m)^{5/6} max(H, 1/H)^{1/6}`.

*Proof.*
- (a)–(c) A shift by an odd vector exchanges the sublattices, so `σ' = −σ(· − d)` on `V + d`.
  - Every site of `V + d` next to the back layer or to the outside has its preimage in `C`, next to `∂V`, so it gets `σ' = +1`. The back layer is `+1`.
  - So the unlike bonds of `n'` are those of `n` without `∂V`.
  - A front site in the frame is the image of a site of `C`, so it keeps the chessboard's occupancy.
- (d) Delete `D`, then identify the pairs of `F`, using T2(a) and T2(c). The moved record has at most 5 other bonds.
- (e) `g` enters as `g^{|∂V|/2}` by (a). `|D| + |F| ≤ |∂V|`, and `Λ ≥ 1`. Average over the six directions.
  - The direction depends on `V` only, so the map stays injective on each class.
  - The occupied front bonds number at most `f_d(V)`. ∎

*Checked (D1, D2).*
- (a)–(c) and the two sums hold on 720 maps: 120 near-chessboard arrangements of the framed `4³` box, in six directions each.
- (d) and the bound with `d` chosen from `V` hold on 864 maps at `(3,1,2)` and on 864 at `(12,1,2)`. On 84 of each set `Q` changes.

*Repair to the attempt.* The attempt chose `d` separately for each arrangement. For the sum below the map must be injective, so `d` is chosen here from `V` alone. The bound is unchanged, because the occupied front bonds number at most `f_d(V)`.

## Theorem T4 — counting walls

*Statement.*
- (a) **Small regions.** Fixed polycubes of 1 to 7 cells number 1, 3, 15, 86, 534, 3481 and 23502. The regions `V` around a site with `|∂V| ≤ 22` number `{6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538}`, and seven cells already need `|∂V| ≥ 24`.
- (b) **Large regions.** A region is determined by its wall.
  - The wall meets the `e₁` ray from `x` within `|∂V|/4` sites, since each ray site in `V` accounts for four wall bonds across the two other axes.
  - The wall is connected through shared vertices (imported below). A plaquette meets 32 others at a vertex.
  - So the regions with `|∂V| = k` number at most `(k/4) r_k`, where `r_k = (32/(k − 1)) C(31k, k − 2)` counts trees rooted at a given plaquette.
- (c) **The sum.** At `x₀ = 3/250`, which is below `30³⁰/31³¹`, `Σ_{V∋x} x₀^{|∂V|} ≤ 0.0897`.

*Proof.*
- (a) Enumeration.
- (b) `r_k` is the `k`-th coefficient of `U + U²`, where `U = x(1 + U)³¹` (inversion of the series). A breadth-first tree has a root with at most 32 children and other vertices with at most 31.
- (c) `x₀(1 + U₊)³¹ ≤ U₊` at `U₊ = 31/1000`, so `U(x₀) ≤ U₊`.
  - The tail is at most `(x₀/4)R'(x₀)`, with `R = U + U²` and `R' = (1 + U)³¹(1 + 2U)/(1 − 31x(1 + U)³⁰)`, minus the first 23 terms.
  - The exact small counts are added back. ∎

*Checked (E1, E2).*
- The counts, by enumeration.
- The connectedness of every wall of at most six cells, through vertices and through edges.
- The ray bound.
- The plaquette degrees, 32 and 12.
- The series identity to `k = 13`.
- The certificate in exact rationals: the sum is `0.08962…`.

## Theorem T5 — two chessboard states

*Statement.*
- For `x ≤ 3/250`, every site of every framed box has `P(σ_x = −1) ≤ 0.0897`.
  - So the A-framed state has `⟨σ_x⟩ ≥ 0.82`.
  - The B-framed state, which is the translate of an A-framed one, has `⟨σ_x⟩ ≤ −0.82`.
- Any limits of the two therefore differ.
- At `ζ = g⁻³` (`H = 1`), `x ≤ 3/250` means `g³Λ⁶(Λ/m)⁵ ≤ (3/250)⁶`. That holds for:
  - `g ≤ 9/62500` without contents;
  - `g ≤ 10⁻⁵` at `(3,1,2)`;
  - `g ≤ 1.8·10⁻⁵` at `(5,2,4)`;
  - `g ≤ 1.9·10⁻⁷` at `(12,1,2)`;
  - `g ≤ 9.7·10⁻⁵` at `(9,8,8)`.

*Proof.* `P(σ_x = −1) ≤ Σ_V Σ_{n: V(n) = V} w(n)/Z ≤ Σ_V x^{|∂V|}`, by T3(e) and injectivity. Then use T4(c). ∎

*Checked (E2, E3).* `1 − 2(0.08962…) ≥ 0.82`, and the five inequalities hold in exact rationals.

The ensemble here is grand canonical. Without contents `ζ = g⁻³` is exactly half filling (T1(b)). With contents, attempt a2 also places each box's half-filling activity inside a window where the bound holds (`1.5·10⁻⁷` at `(3,1,2)`, and `5·10⁻⁶` without contents). That step is refereed but not re-run here.

## What this gives block 79

- **Supplied now.** Block 79 needs a chessboard of records and a site coupling `c n`. Under that coupling the walk's staggered term has gap `|c|/2` relative to the offset. Block 79 derived no ordering. T5 supplies one: block 81's gas makes the chessboard when a recorded bond costs a factor below `9/62500`, or about `10⁻⁵` with contents.
- **Still supplied or open.**
  - the bond scale `g`, which must be very small;
  - the coupling `c n` and its clocking, which block 79 as landed separates into two distinct choices;
  - whether the walk's gap survives the gas's defects, of density up to `0.0897` per site. This is not treated.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 79 as landed: 'No formation or ordering of that configuration is derived.'; block 81 as landed: 'Finite symmetry is not absence of order.'"
source_of_blocker_text: blocks 79 and 81 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the walk's gap on the gas's typical arrangement (defects of density at most 0.0897); edge-connected walls (g near 1.2 10^-3); closed-wall counts; the canonical ensemble; the scan window 0.30-0.50"
conditional_surface_status: "T1-T5 exact for block 81's supplied gas; T4(b) and T5 rest on the imported connectedness of walls; half filling with contents is the attempt's refereed step, not re-run"
hypothetical_axiom_status: "the gas, its bond scale, activity and contents are hypotheses; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 39 gave the static law with vacancies.
  - Block 81 gave the gas, its bond identity and finite statements.
  - Block 79 gave the chessboard's rest mass under a supplied coupling.
  - Block 102 gave reflection positivity through planes of sites, which is not used here.
- **The probes attempts**, both written by Claude Opus 5.5 and refereed by a Grok model, confirmed (#9014, #9042).
  - `the-record-gas-chessboard-threshold` a1 (issue #8834) proved order through reflection positivity and chessboard estimates, with `g* ≈ 10⁻⁹`. It also found T2(a)–(b).
  - a2 (issue #9034) proved it by translation, with `g* = 9/62500`. It also found T1, T3 and T4, and the half-filling window.
- **In the literature.**
  - The argument is Peierls's contour argument.
  - The translation map is Dobrushin's argument for the hard-core lattice gas with nearest-neighbour exclusion, which orders into a chessboard at high activity.
  - Wall connectedness uses the Mayer–Vietoris sequence.
  - The tree count uses Lagrange inversion, as in the counts of Klarner.
- **New here:**
  - an independent exact runner, with its own polycube enumeration, translation checks and certificate;
  - the repair that fixes the direction from `V` alone;
  - the statement placed against blocks 79 and 81 as landed.

## Exact target and obligation graph

Target: whether block 81's gas makes block 79's chessboard. The obligations are:
- (O1) the law in unlike bonds;
- (O2) the contents;
- (O3) a map that removes a wall;
- (O4) the wall count;
- (O5) the two states.

T1–T5 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- without contents the bound says nothing above `g = 9/62500`, and the scan window near `0.3–0.5` is out of reach of this count;
- contents can only raise the bound, never lower it.

### N1 — Routes by which the sentences could fail or mislead
1. *Edge-connected walls.* If every wall is connected through shared edges (true for every wall of at most six cells), the same certificate gives about `g ≤ 1.2·10⁻³` (a2). Not proved.
2. *Closed walls.* The true growth rate of walls is far below 82.9 per plaquette. Counting closed walls would raise `g*`.
3. *The merge cost.* `(Λ/m)⁵` per front merge is a worst case, and it dominates at `(12,1,2)`.
4. *The canonical ensemble.* Not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The connectedness of walls rests on the imported topological sequence (see Imports).
- The ensemble is grand canonical.
- The frame is the A-chessboard.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; a site's possibilities; no dynamics in the axioms | yes |
| block 81 (landed) | the gas, its weights and bond identity | yes (restated) |
| block 79 (landed) | what a chessboard gives the walk | placement |
| probes (#8834, #9034; Grok-refereed #9014, #9042) | T1–T5 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the record gas makes the chessboard for `g ≤ 9/62500` (`10⁻⁵` at (3,1,2)) at `ζ = g⁻³`; contents act only on the wall" | executed: `M`'s decomposition at five triples; `Q` on every cube subgraph of at most 6 sites | executed: the unlike-bond identity on 60 framed arrangements; complement symmetry on 60 torus arrangements | executed: the translation map on 720 maps, and the content bound on 1728 | executed: fixed polycubes to 7 cells, wall counts, connectedness and ray; the certificate in exact rationals | every framed box and every even torus; T4(b)–T5 with the imported wall connectedness; the gas is supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A factor below `10⁻⁴` per bond is not physics." *Reply:* It is a bound from a crude count. The finite-box control of block 81 saw a near-perfect chessboard at `g = 1/4`. The theorem places the order in the gas; the scale is supplied either way.
- *Objection:* "Order in the gas is not a rest mass." *Reply:* Agreed. The coupling to the walk and the gap's survival with defects are listed as open.

### N8 — Cross-cycle echo
- Block 79 needed a chessboard.
- Block 81's finite statements left the question open ("Finite symmetry is not absence of order").
- This note answers it for expensive bonds.

## Falsifiers

- A framed arrangement where translating `V` does not drop the unlike bonds by `|∂V|`.
- A region `V` of at most six cells whose wall is not connected.
- A wall count around a site different from T4(a).
- An exact evaluation of the certificate above `0.0897`.

## Boundaries and non-claims

- The gas, its bond scale, activity and contents are supplied.
- The wall connectedness for large walls is imported.
- Half filling with contents is not re-run.
- The walk's gap on the gas's arrangements is not treated.
- No gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 39, 79, 81 and 102, restated or placed.
- The probes attempts, refereed by another model family.
- Named standard imports, at definition level:
  - the Mayer–Vietoris sequence, for the connectedness of a wall whose two sides are connected;
  - Lagrange inversion;
  - exact rational arithmetic.
- Reference only: Peierls; Dobrushin; Klarner.

## Review record

- **Who and when.** Supervisor-run block, the sixty-fifth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - Two probes attempts by Claude Opus 5.5 derived the results (#8834, #9034). Grok referees confirmed them (#9014, #9042).
  - The supervisor re-checked them with its own runner, and repaired the choice of direction.
- **Before writing.** Main was re-fetched. Blocks 79 and 81 were read as landed.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_record_gas_does_make_the_chessboard_when_a_recorded_bond_is_expensive_a_wall_counting_bound_2026_09_24.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.
