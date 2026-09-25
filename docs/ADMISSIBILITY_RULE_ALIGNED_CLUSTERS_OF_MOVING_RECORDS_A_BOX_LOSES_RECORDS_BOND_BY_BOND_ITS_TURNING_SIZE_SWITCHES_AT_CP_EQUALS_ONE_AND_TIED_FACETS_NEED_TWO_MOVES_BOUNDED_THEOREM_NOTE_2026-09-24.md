---
claim_id: admissibility_rule_aligned_clusters_of_moving_records_a_box_loses_records_bond_by_bond_its_turning_size_switches_at_cp_equals_one_and_tied_facets_need_two_moves_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied positive weights p,q,r,c and formation parameter z>=0, rate-one symmetric bond proposals,
  isolated aligned ideal clusters. Exact box instantaneous departure and touching-site formation counts for integer
  L>=2; continuous-size rate-balance crossings only in the stated interval between z2 and zc, not dynamical stability
  or survival. Half-space one-hop isolation criterion, explicit two-hop paths for (111)/(110), and general projection
  boundary count for axis-convex finite clusters. Octahedron/dodecahedron isolated-departure counts executed only
  at R=1..8. No closed shape evolution, total-process detailed balance or lifetime law.
upstream_dependencies:
- admissibility_rule_binding_scale_pinned_at_the_neutral_value_pair_weight_is_the_rules_likelihood_ratio_no_binding_without_a_cycle_all_binding_is_agreement_around_loops_bounded_theorem_note_2026-09-20
- admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20
runner: scripts/admissibility_rule_aligned_clusters_of_moving_records_a_box_loses_records_bond_by_bond_and_its_turning_size_switches_at_cp_one_2026_09_24.py
---

# Aligned-cluster instantaneous rates, size-domain corrections and facet escape paths

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 39 and 40 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 39 and 40 as landed on main (records that move: the motion clause counted bond by bond, the formation rate, and the neutral scale); it reports how an aligned cluster of moving records loses and gains records at its surface; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

For the supplied rate-one bond motion, the ideal L-box has the displayed exact instantaneous departure count. Its touching-site formation count includes every possible new content, so it does not preserve an aligned box. Neither count gives a closed shape evolution or a survival theorem.

The sign of the finite-size correction changes at x=cp=1. A balance crossing in the physical domain L>=2 also requires z to lie strictly between z2=1/[c A1(1+x^3)] and zc=1/[c A1(1+x^5)]. Outside that interval the instantaneous balance has one sign for all L>=2. Calling such a crossing dynamically stable or a nucleation threshold would require additional evolution assumptions.

The half-space calculation identifies which records can become isolated in one hop. Tied infinite facets have no such hop, but explicit two-hop escape paths exist on (111) and (110). Finite edges and tips are different geometries. A path's static weight ratio is not an escape rate.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "A site never carries more than one record; records are permanent." A record can move only to an empty site. Records that move are the owner's reading, and that reading is supplied.
  - "Records form." Block 39 T4's formation rate is supplied.
  - "Admissibility is not a dynamics axiom." The motion, the rate convention and the formation rate are supplied clauses. Nothing is adopted.
- **Motion** (block 39 as landed). A bond with exactly one occupied end is visited, with bonds at any symmetric rates. The record at `s` moves to the empty end `t` with probability `w_t/(w_s + w_t)`, where `w` is the product of the weights of the record's other bonds at that position.
  - Aligned records weigh `cp` per bond, and a bond with an empty end weighs `1`.
- **Formation** (block 39 T4 as landed). Rate `zZ_x`, with `Z_x = c^jA_j` next to `j` aligned records and `A_j = p^j + q^j + 4r^j`.
- **Rate convention.** Positive p,q,r,c and z>=0 are supplied. Every bond is visited at rate1. A configuration-independent covariant proposal rate is constant; symmetric configuration-dependent rates can also satisfy detailed balance. Changing the common motion rate rescales the balance thresholds relative to a fixed formation rate.
- **Accounting.** The ideal shape's instantaneous rates, with every other record fixed during a tested escape path. Formation generally introduces unaligned content and irreversible formation is not in detailed balance with the static law; only the hopping part has that property.
  - `E` counts moves to an isolated site; the departed record has left the cluster.
  - `G` sums formation over the empty sites touching the cluster.
  - This is a balance of rates, not a growth law (T4).
- **The neutral scale** (block 40 as landed): `c₀ = 6/(p + q + 4r)`, so that `c₀A₁ = 6`.
- **Comparators, named only:** nucleation and the nucleus of the classical theory (Becker and Döring); equilibrium crystal shapes (Wulff); the kinetic Ising model with exchange dynamics (Kawasaki).

## Theorem T1 — a box loses records bond by bond

*Statement.* For the aligned `L`-box, `L ≥ 2`:
- (a) Every one of its `6L²` occupied–empty bonds leads to an isolated site.
- (b) The departure rate is `E(L) = 24/(1+x³) + 24(L−2)/(1+x⁴) + 6(L−2)²/(1+x⁵) = 6L²/(1+x⁵) + βL + γ`, where
  - `β = 24x⁴(x−1)/((1+x⁴)(1+x⁵))`;
  - `γ = 24x³(x−1)³(x+1)(x²+1)/((1+x³)(1+x⁴)(1+x⁵))`;
  - `E = 3L²` at `x = 1`.
- (c) The bond-by-bond count is in detailed balance with the static law at a corner: forward over backward is `x^{−3}`. One attempt per record, split over its empty bonds, gives `2x^{−3}`.

*Proof.*
- (a) If `t = s + e` is empty, `e` points out through a face containing `s`. Every other neighbour of `t` lies one step beyond the box along `e`.
- (b) A corner record has three departure bonds with `k = 3`. An edge record has two with `k = 4`, and a face record one with `k = 5`. Each departs with `1/(1 + x^k)`. The split is algebra.
- (c) Moving a corner record out loses three aligned bonds. By bond, the rates are `1/(1+x³)` out and `x³/(1+x³)` back. By record, they are `(1/3)/(1+x³)` out and `(1/6)x³/(1+x³)` back, because the isolated record has six empty bonds.

∎

*Checked (B1).* The census of every occupied–empty bond for `L = 2..7`; the split, symbolically in `x`; both balance ratios.

## Theorem T2 — the turning size switches at cp = 1

*Statement.* Let `G = 6zcA₁L²`: every touching empty site has one aligned neighbour. Let `z_c = 1/(cA₁(1+x⁵))`.

Define z2=1/[c A1(1+x^3)], the balance value at L=2. For the continuous interpolation L>=2:

- If x<1, z2<zc. For z<=z2 the balance G-E is nonpositive at every size (strict for L>2); for z2<z<zc there is exactly one zero above2, positive below and negative above; for z>=zc it is positive everywhere.
- If x>1, zc<z2. For z<=zc the balance is negative everywhere; for zc<z<z2 there is exactly one zero above2, negative below and positive above; for z>=z2 it is nonnegative everywhere (strict for L>2).
- At z=z2 the only zero is at L=2. Integer sizes need not include the continuous zero.

These signs describe an instantaneous diagnostic, not attraction or repulsion under a proved dynamical size law.

At `x = 1` the sign of `z − z_c` decides at every size. At the neutral scale, `x > 1` iff `5p > q + 4r`. At `(3,1,2)`, with `c = c₀ = 1/2` and `x = 3/2`:
- `z_c = 16/825`;
- the instantaneous balance is negative at every size `L = 2..200` at `(9/10)z_c` and at `z_c`;
- at `(11/10)z_c` the instantaneous balance changes from negative to positive between17 and18.

The alternative per-record instantaneous balance would be positive up to `L = 10` at `(9/10)z_c`.

*Proof.* `G − E = 6L²(z/z_c − 1)/(1+x⁵) − βL − γ`, and `β` and `γ` carry the sign of `x − 1` (T1). Divide E by L^2: E/L^2=6/(1+x^5)+beta/L+gamma/L^2. Its derivative is -beta/L^2-2gamma/L^3, of sign opposite x-1 for x!=1. Its endpoint values are 6/(1+x^3) at L=2 and6/(1+x^5) at infinity. Comparing with6zcA1 proves every case above. ∎

*Checked (C1).* `z_c`, and the signs of `G − E` for `L = 2..200` at three formation rates, exactly. Also the per-record contrast.

## Theorem T3 — which surface records can leave in one move

*Statement.* Take the facet `{n·v ≤ 0}` with primitive normal `n`, and let `h ≥ k` be its two largest `|n_i|`. The surface records form the layers `m = −n·v = 0, …, h − 1`.
- (a) A record in layer `m` has `3 + #{i: |n_i| ≤ m}` recorded neighbours.
- (b) It can reach an isolated site in one move iff `m < h − k`, and then only along the largest normal component. So no record of a tied facet (`h = k`: `(110)`, `(111)`, `(221)`, `(331)`, …) can leave in one move.
- (c) In the executed finite census R=1..8, the octahedron `|x| + |y| + |z| ≤ R` loses records in one move only at its six tips. The rhombic dodecahedron, defined by max(|x|+|y|,|y|+|z|,|x|+|z|)<=R, has in that census `6 + 12R` one-move departure bonds for even `R`, and `6 + 12(R − 1)` for odd `R`.

*Proof.*
- (a) For each axis, `v ± e_i` are both in the facet iff `|n_i| ≤ m`, and otherwise exactly one is.
- (b) The destination `t = v + σe_i` is isolated iff `|n_i| − |n_j| > m` for every `j ≠ i`.

∎

*Checked (D1).*
- On `19` normals with signed components up to `4`, every surface record in a window: its neighbours and its one-move destinations.
- The octahedron and the dodecahedron for `R = 1..8`.

## Theorem T4 — one move is not enough

*Statement.*
- (a) A top-layer record has `k_s = 3, 4, 5` recorded neighbours on `(111)`, `(110)` and `(100)`.
  - On `(111)` it reaches an isolated site in two moves. The first is a hop of probability `1/(1+x)` to a site with two recorded neighbours. On `(110)` that hop has probability `1/(1+x³)`.
  - Any displacement to an isolated site multiplies the static weight by `x^{−k_s}`.
  - So a balance of one-move losses against growth, facet by facet, is no growth law for tied facets.
- (b) For a cluster whose axis-parallel lines meet it in intervals, one move reaches exactly `2(|π_xC| + |π_yC| + |π_zC|)` arrangements. That is `6L²` for the box, and `12R² + 12R + 6` for both the octahedron and the rhombic dodecahedron.

*Proof.*
- (a) Hold every other record fixed. From the origin on either (111) or (110), the path 0 -> e1 -> 2e1 ends isolated after removing the original occupied origin. The first intermediate site has respectively2 or1 remaining occupied neighbors, and the second hop has positive probability for x>0. This proves path existence, not a waiting-time law. The hop probability is `w_t/(w_s + w_t) = 1/(1 + x^{k_s − k_t})`. A record that ends isolated has lost its `k_s` aligned bonds.
- (b) Each axis-parallel line through the cluster meets it in one interval and has exactly two occupied-empty bonds. Distinct such bonds give distinct single-hop configurations. Both polyhedra project onto the integer diamond |a|+|b|<=R, containing1+2R(R+1) points: slice at a and sum2(R-|a|)+1. This proves the displayed all-R projection count separately from the finite isolated-departure census.

∎

*Checked (E1).*
- The neighbour counts and the first hops at the three facets.
- A two-move escape on `(111)`.
- The projection counts for the box (`L = 2..5`) and both polyhedra (`R = 1..5`).

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 39 as landed: where records clump and jam is recorded only as historical observations, not proved"
source_of_blocker_text: block 39 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a growth law per facet from two-move paths; the equilibrium shape of an aligned cluster; clusters with mixed contents"
conditional_surface_status: "T1-T2 for the box at every L by the census; T3 for every facet by the layer rule; T4 as stated; the motion, the rate convention, the scale and the formation rate supplied"
hypothetical_axiom_status: "records that move and form at block 39's rates are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 39: the motion clause, the formation rate, and the historical observations of clumping and jamming.
  - Block 40: the neutral scale.
- **The probes attempts.**
  - `moving-jammed-clusters` a2 (Claude Opus 5.5, issue #8680) found T1–T4 and corrected a1's count. A Grok referee confirmed it: "the partial result survives" (`probes/work/derive/moving-jammed-clusters/referee_w-macbookpro90c72-jb732/REPORT.md` on `ai/probes`; no confirm issue was opened).
  - Attempt a1 (Claude Opus 5, issue #8532, Grok-confirmed #9117) counted one attempt per record and put the switch at the root of `x⁵ = 2x⁴ + 1`. Its referee confirmed the arithmetic under that count. T1(c) shows that the count is not the one in detailed balance with the static law, so it is not used.
  - Attempt a3 (#8992) is unrefereed and not used.
- **In the literature.**
  - Classical nucleation, with the nucleus of Becker and Döring.
  - Wulff shapes.
  - Exchange dynamics (Kawasaki) and heat-bath acceptance (Glauber).

  All reference only.
- **New here:**
  - an independent exact runner;
  - the two counts compared and placed against block 39's own clause.

## Exact target and obligation graph

Target: how an aligned cluster of moving records loses and gains records. The obligations are:
- (O1) the box's departures (T1);
- (O2) its turning size (T2);
- (O3) facets (T3);
- (O4) the limit of one-move accounting (T4).

T1–T4 discharge them. Open: a growth law from two-move paths.

## No-Go Discipline Gate

The note's negative sentence: a balance of one-move losses against growth is no growth law for tied facets.

### N1 — Routes by which the sentence could fail or mislead
1. *Other rate conventions.* Block 39 allows any symmetric bond rates. A rate depending on more than the bond changes `E`. T1(c) tests two particular proposal conventions; other symmetric configuration-dependent proposals are not excluded.
2. *Mixed contents.* Only aligned clusters are treated.
3. *Beyond the ideal shape.* The accounting is instantaneous. A real cluster roughens, and that is what T4 says a growth law must follow.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied motion, rate convention, scale and formation rate.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; records form; no dynamics in the axioms | yes |
| blocks 39, 40 (landed) | the motion, the formation rate; the neutral scale | yes (restated) |
| probes (#8680; Grok referee report on `ai/probes`) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "a box loses records bond by bond; the switch is at `cp = 1`; tied facets need two moves" | executed: every occupied–empty bond of the box for `L = 2..7` | executed: the surface layers of 19 normals | executed: the split in `x`; both balance ratios | executed: `G − E` at `(3,1,2)` for `L = 2..200`; the polyhedra and the projection counts | the box at every `L`; every facet by the layer rule; the motion and rates supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "a1's count is also a valid dynamics."
  - *Reply:* It is a dynamics, but it is not in detailed balance with the static law that block 39 T1 pairs with its motion.
  - Block 39's clause says bonds are visited, and the bond-by-bond count is what follows from that.

### N8 — Cross-cycle echo
- Block 39 recorded clumping only as observation.
- Block 111 found that groups need a binding clause.
- This note finds a sign change of the ideal-box finite-size correction; actual persistence remains open.

## Falsifiers

- An occupied–empty bond of the box whose destination is not isolated.
- A size `L ≤ 200` at which the box grows at `z_c`, at `(3,1,2)`.
- A record of a tied facet that reaches an isolated site in one move.

## Boundaries and non-claims

- The motion, the rate convention, the scale and the formation rate are supplied.
- Mixed contents, roughening and a growth law are not claimed.
- No gravitational claim is made.

## Imports

- [Supplied source, block 39](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 40](ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 39 and 40, restated.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the sign analysis of a quadratic;
  - exact rational and symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-fifth since the source-link direction opened; 2026-09-24. It belongs to the moving-records thread of blocks 39–40.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#8680). A Grok referee confirmed them, in a report on `ai/probes`.
  - The supervisor re-checked them with its own runner.
- **Before writing.**
  - Main was re-fetched, and blocks 39 and 40 were read as landed.
  - The own-prior-art check found attempts a1 and a3 of the same problem. a1's count is shown not to be in balance, and a3 is not used.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_aligned_clusters_of_moving_records_a_box_loses_records_bond_by_bond_and_its_turning_size_switches_at_cp_one_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
