---
claim_id: admissibility_rule_where_moving_records_cannot_clump_a_sharp_one_site_bound_gives_uniqueness_below_a_ratio_spread_of_49_over_25_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the owner's moving-records reading and block 39's law with vacancies (each site empty or one record of content in the six axes; weight z^N times the product over bonds of W = c omega between records, 1 at an empty end), the equilibrium of records moving by the pair weights. Exact: the largest total-variation change of a law under a multiplier with values in [m, M] is tanh(log(M/m)/4), attained; hence (with the imported one-site uniqueness criterion) the law is unique at every fugacity when every neighbour change has ratio spread below 49/25 - content-less records for 25/49 < cw < 49/25, no certificate at (3,1,2), where the spread is 9; reflection through planes of sites is positive for every positive law (through bond planes only from the neutral scale up); an explicit, very conservative clumping region from the chessboard and contour estimates (imported). A probes worker's result, refereed by another model family. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_where_moving_records_cannot_clump_2026_09_23.py
---

# Where moving records cannot clump: a sharp one-site bound gives uniqueness below a ratio spread of 49/25; reflection through planes of sites is positive for every law

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; a probes worker's result, its key steps refereed by another model family; nothing adopted or registered; unaudited)

This note works within the owner's moving-records reading and block 39's law with vacancies (the equilibrium of records that move by the pair weights) and reports, from a probes worker's result refereed by another model family, where that law cannot clump and which reflections it admits; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 39 (#8530) found that records moving by the pair weights equilibrate to the static law on the occupied set, and executed where they clump and jam. In the owner's picture, records that gather can jam. A probes worker asked where this law provably cannot clump, and above what binding it provably does (task `J:derive:moving-clumping-bounds:a2`, worker `w-macbookpro90c72-j046a`, Claude Opus 5.5). A referee of another model family (`w-macbookpro90c72-j2014`, a Grok model) confirmed the sharp bound and the window, and corrected one number.

- **T1: the sharp one-site bound.** If a law `P ∝ f` is multiplied by `h` with values in `[m, M]`, it moves in total variation by at most `(√M − √m)/(√M + √m) = tanh(¼ log(M/m))`, and this is attained. The earlier attempt's bound `(M − m)/(M + m)` is weaker.
- **T2: no clumping below a ratio spread of 49/25.** A site's conditional law, over its seven states, changes under a change of one neighbour by the factor `W(a, b′)/W(a, b)`. With six neighbours and the one-site uniqueness criterion, the law is unique at every fugacity when every such factor has ratio spread `R < 49/25`.
  - Content-less records: `25/49 < cw < 49/25`. At the neutral scale `cw = 1` the sites are independent.
  - `(9, 8, 8)`: `25/392 < c < 49/225`.
  - `(3, 1, 2)`: a neighbour turned to its opposite content changes the odds by `(p/q)² = 9`, the referee's correction of the worker's 4. There is no certificate at any `c`.
- **T3: reflections.**
  - Through bond planes the law is reflection positive exactly when `c ≥ c₀`, `p ≥ q` and `p + q ≥ 2r` (block 39 T5).
  - Through planes of sites it is reflection positive for every positive law, because no bond crosses such a plane.
  - So the chessboard estimate is available at every `(c, p, q, r)`.
- **T4: a region where it clumps.** Take unit cubes, one per site, with face-sharing neighbours. The 254 non-uniform occupancy patterns fall into 16 classes, with at least 3/4 mixed bonds per site. With the tree bound for contents and the contour count, exact rational arithmetic certifies the contour condition at `c max(p, q, r) = 44⁸` (at `T/ω* = 2`), and at `cw = 38⁸` for content-less records. By the imported chessboard and coexistence arguments, the gas has two phases there. This is very conservative: for content-less records the known onset is `cw ≈ 2.43`.

In plain terms: when a record's neighbours can change its odds by less than a factor of about two, moving records spread out, whatever their density. At the campaign's usual weights `(3,1,2)` the odds swing by a factor of nine, so nothing rules out clumping, and block 39's simulations saw it. The rigorous clumping region is real but far from where clumping actually starts.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`): Admissibility and Record. Motion is an open gate. Nothing is adopted.
- **The owner's reading** (records move, one per site at a time) and **block 39's law with vacancies** (#8530).
  - Each site of `Z³` is empty or holds one record, of content `±e₁, ±e₂, ±e₃`.
  - The weight is `z^N Π_bonds W`, with `W(a, b) = c ω(a, b)` between records (`ω = p, q, r` for equal, opposite, orthogonal) and `W = 1` at an empty end.
  - Constants: `T = p + q + 4r`, `c₀ = 6/T`, `ω* = max(p, q, r)`, `t = T/ω*`.
  - This is the equilibrium of block 39's pair-weight motion at a fixed record count, taken here grand-canonically.
- **Clumping** means two translation-invariant states of different density at one fugacity.
- **Provenance.**
  - The worker (Claude Opus 5.5) and its earlier attempt a1 (`w-jonathonsmac4f50-j6200`, Claude Opus 5) are the same family as the supervisor.
  - The referee is a Grok model, another family. It confirmed T1 and T2's window and corrected the `(3,1,2)` spread; it did not recompute T4's constants.
  - The supervisor re-ran the worker's check (all steps ok) and ported it.

## Theorem T1 — the sharp one-site bound

*Statement.* For `P ∝ f` and `P′ ∝ fh` with `h ∈ [m, M]`, `sup_f TV(P, P′) = (√M − √m)/(√M + √m)`, attained by a two-point `f`.

*Proof.* `TV = E_P[(h − H)⁺]/H` with `H = E_P h`. Convexity bounds `E(h − H)⁺ ≤ (H − m)(M − H)/(M − m)`, attained on `{m, M}`. Maximising over `H` gives `H = √(Mm)` (family B: symbolic, 300 random rational instances, and the attained value `1/5` at `M/m = 9/4`). ∎

## Theorem T2 — no clumping below a ratio spread of 49/25

*Statement.* Let `R_max` be the largest ratio spread of `W(a, b′)/W(a, b)` over the seven states `a` and all neighbour changes `b → b′`. If `R_max < 49/25`, the law is unique at every fugacity. The windows are as stated in the result, checked exactly just inside and just outside each edge. At `(3, 1, 2)`, `R_max ≥ 9` for every `c` tried and the content-only spread is exactly 9.

*Proof.* By T1 each neighbour moves the conditional law by at most `tanh(¼ log R_max)`. The one-site uniqueness criterion needs the sum over six neighbours below one: `6 tanh(¼ log R) < 1` iff `R < (7/5)²`. The criterion itself is imported (family C). ∎

## Theorem T3 — reflections

*Statement.*
1. Through bond planes, the law is reflection positive iff the `7 × 7` bond matrix is positive semidefinite, iff its Schur complement `cΩ − J` is. That matrix has eigenvalues `cT − 6`, `c(p − q)` and `c(p + q − 2r)`.
2. Through planes of sites, the law is reflection positive for every positive `(c, p, q, r)`.

*Proof.* (1) Block 39 T5, recomputed symbolically. (2) No nearest-neighbour bond joins the two sides of a plane of sites. Share the plane's bonds and fugacities as square roots; the weight is `F θF` and `⟨F θF⟩ = Σ G² ≥ 0` (family D). ∎

## Theorem T4 — a region where it clumps

*Statement.* The 254 non-uniform occupancy patterns of a unit cube, repeated with period two, fall into 16 classes `(ρ, e, κ)`, with `e ≥ 3/4`. Each weighs at most `6^κ t^{ρ−κ} (cω*)^{−e/2}` per cube, and exact rational arithmetic gives `676 ε ≤ 1/4` at `T/ω* = 2`, `cω* = 44⁸`, and for content-less records at `cw = 38⁸`.

*Proof.* Enumeration and exact bounds (family E). Turning the contour condition into two phases uses the chessboard estimate and the coexistence argument, imported. ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 39 (#8530): where moving records clump and jam (executed only); the owner's jam remark"
source_of_blocker_text: block 39; probes derivation J:derive:moving-clumping-bounds (refereed by another family)
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "no-clumping window and a rigorous clumping region for block 39's law; next: close the gap between 49/25 and the conservative clumping region (sharper contour counts; bond-plane blocks in block 39 T5's region); the same questions with block 95's clock field added"
conditional_surface_status: "T1, T3 exact for every law; T2 through the imported uniqueness criterion, windows exact; T4 through the imported chessboard and coexistence arguments, certificate exact"
hypothetical_axiom_status: "the owner's reading and block 39's law with vacancies are hypotheses; nothing adopted"
admitted_observation_status: "the content-less lattice gas's known onset cw = exp(4 K_c) = 2.4269 is a literature comparator only"
audit_required_before_effective_retained: true
```

## Prior art and what is new

Block 39 (#8530) gave the law, the neutral scale, the bond-plane reflection region, and the executed clumping map (onset near `p = 10` at the neutral scale on the line `(p,1,2)`). The one-site uniqueness criterion is Dobrushin's. The chessboard estimate and the coexistence argument are those of Fröhlich, Israel, Lieb and Simon. Contour counting with depth-first codes is the Peierls argument. Content-less records are the lattice gas of bond activity `cw`, the Ising model with `K = ¼ log(cw)`, whose onset is known numerically; that onset is used here only as a comparator.

New here, from the probes worker and its referee:
- the sharp bound `tanh(¼ log R)` and the `49/25` windows;
- reflection positivity through planes of sites for every law;
- an explicit contour certificate;
- the referee's correction at `(3,1,2)`.

## Exact target and obligation graph

Target: where block 39's law cannot clump, and where it provably does. The obligations are:
- (O1) the one-site influence;
- (O2) the uniqueness windows;
- (O3) the reflections;
- (O4) a clumping region.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- no clumping when every neighbour change has ratio spread below 49/25;
- no uniqueness certificate at `(3,1,2)` by this route.

### N1 — Routes by which the sentences could fail or mislead
1. *Sharper uniqueness criteria.* Block-based versions could widen the window. Not tried.
2. *Sharper contour counts.* These would lower T4's region substantially; the known content-less onset is about `2.43`.
3. *The clock field of block 95.* Adding a long-range pair term changes the law. These windows are for block 39's contact weights alone.
4. *The formation law* (block 39's corrigendum, #8545). The growing population is not a sample of this law. The windows concern the equilibrium at fixed count.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The imported theorems are named. Block 39's law is supplied.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | Admissibility; Record | yes |
| block 39 (#8530) | the law with vacancies; T5 | yes |
| probes worker `w-macbookpro90c72-j046a` and referee `w-macbookpro90c72-j2014` | the result; the confirmation and correction | yes (verified here) |
| #8545 | the formation-event law | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "unique below a ratio spread of 49/25; site-plane reflection positivity for every law; an explicit clumping region" | executed: the one-site bound on 300 instances; all neighbour changes | executed: the 254 cube patterns | executed: the Schur complement's eigenvalues | executed: the contour certificate | T1, T3 for every law; T2, T4 through imported theorems |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- Hostile reviewer: "The clumping region is useless in practice." Reply: it is conservative by ten orders, and the note says so. Its content is that a rigorous two-phase region exists for every `(p, q, r)`, through site-plane reflections, including weights outside block 39's bond-plane region.
- Second objection: "(3,1,2) is left open." Reply: yes. By this route no certificate is possible there, because the spread is 9. Block 39's simulations are the evidence at those weights.

### N8 — Cross-cycle echo
Block 39 executed a clumping map; blocks 95–99 added the clock field. This note gives block 39's contact law rigorous bounds on both sides, from a worker's result refereed by another family.

## Falsifiers

- An `f` and `h ∈ [m, M]` with total variation above `tanh(¼ log(M/m))`.
- A neighbour change with ratio spread below 49/25 at a point the note excludes, or above it at a point it includes.
- A positive `(c, p, q, r)` whose law is not reflection positive through a plane of sites.

## Boundaries and non-claims

- T2 and T4 rest on imported theorems (the uniqueness criterion; the chessboard and coexistence arguments).
- T4 is very conservative.
- The windows are for block 39's contact law at fixed count, without the clock field.
- No gravitational claim is made. The known onset is a comparator only.

## Imports
- `minimal_axioms`. Blocks 39, 95 (PRs) and #8545: restated or placed.
- Named standard imports at definition level:
  - Dobrushin's uniqueness criterion;
  - the chessboard estimate and the coexistence argument (Fröhlich–Israel–Lieb–Simon);
  - Peierls contour counting with depth-first codes;
  - the Ising model's onset on the simple cubic lattice, as a comparator only;
  - exact rational arithmetic.

## Review record
- **Who and when.** Supervisor-run block, the fiftieth since the source-link direction opened, built from a probes worker's result with an other-family referee.
- **Provenance.** Worker `w-macbookpro90c72-j046a` (Claude Opus 5.5). Referee `w-macbookpro90c72-j2014` (a Grok model), which confirmed T1 and the window and corrected the `(3,1,2)` spread from 4 to 9. The supervisor re-ran the worker's check (all ok) and ported it with the correction.
- **Independence.** Mutation census: six mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_where_moving_records_cannot_clump_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
