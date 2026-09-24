---
claim_id: admissibility_rule_formation_on_the_sites_clock_spreads_records_apart_by_the_inverse_of_motions_pair_excess_clumping_needs_records_that_move_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the owner's moving-records reading, block 53's clock field slaved to the records, the motion of blocks 95 and 97 (hops timed by the occupied site) and a supplied formation clause timed the same way (an empty site forms a record at the rate of its own clock). Exact: with one record present the second forms at offset d in proportion to exp(U(d)) and is found there by motion in proportion to exp(-U(d)), U block 95's pair energy; every order of forming a set carries the same unnormalized weight exp(sum over pairs U), the per-step normalizations depending on the occupied set at first order only through its own pair sum; so for records that slow clocks, formation spreads records apart and motion gathers them. Executed: 96 records formed one at a time on 16^3 make fewer contacts as the coupling grows. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_formation_on_the_sites_clock_spreads_records_apart_clumping_needs_records_that_move_2026_09_23.py
---

# Formation on the site's clock spreads records apart by the inverse of motion's pair excess: clumping needs records that move

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; nothing adopted or registered; unaudited)

This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) with block 53's clock field, the motion of blocks 95 and 97 and formation timed by the site's clock; it reports how formation and motion place records in one field; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The owner's picture has two things happening to records. They form at empty sites, and they move. Blocks 95 and 97 (#8860, #8872) showed that records moving on the clock of the site they occupy, in a clock field they slow, are found together with pair weight `e^(−U)`, where `U(d) = 6 log κ G(d) < 0` near a record. The same locality principle, that a site's own processes run on that site's clock, times formation too: an empty site forms a record at the rate of its own clock. This note asks where formation puts records.

- **T1: the inverse law.** With one record present, a second record forms at offset `d` in proportion to `w(d) = e^(U(d))`. Motion finds it there in proportion to `e^(−U(d))`. The two laws are exact inverses.
- **T2: every order weighs the same.** Forming a set one record at a time, each at the rate of its site's clock in the field of those already present, gives the same unnormalized weight `e^(Σ_pairs U)` for every order of formation. The normalizations at each step depend on the occupied set, at first order, only through the set's own pair sum. So at low density the formed set carries weight `e^(+Σ U)`, the inverse of motion's `e^(−Σ U)`.
- **T3: formation spreads, motion gathers.** For records that slow clocks (block 55's books, block 97), a record forms less often next to another than far away, and motion finds it there more often. Control: 96 records formed one at a time on `16³` make `6.07, 5.63, 4.57, 3.65` contacts at couplings `0, 1/2, 1, 2` (uniform placement: `6.68`). In block 95's control, the same 96 records moving at coupling 1 put 95 per cent of themselves in one cluster.

So in the owner's picture, long-range clumping comes from records that move. In a reading where records form once and never move, the same clock field would place them apart. Formation fills the voids, where clocks are fast, and motion gathers what has formed.

In plain terms: records slow the clocks near them. A record that can move sits longer where clocks are slow, so moving records gather. A new record forms more readily where clocks are fast, so it forms away from the others. The same field pushes the two halves of the picture in opposite directions. The clumping we would call gravity-like needs the records to move.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`): Record ("Records form"), no time metric; the formation rate is an open gate ("does not supply the formation site, probability, or rate"). Nothing is adopted.
- **Block 53's clock field** (#8568). `log w_z = 6 log κ Σ_{r∈C} G(z − r)`, slaved to the records present.
- **Motion** (blocks 95, 97; #8860, #8872). A record hops on the clock of the site it occupies. The pair law is `e^(−Σ U)`, with `U = 6 log κ G`.
- **Formation clause** (supplied). An empty site `x` forms a record at rate `z w_x`. Formation is a process of the site `x`, and the locality principle of block 97 (a site's own processes are field-free per own tick) gives the exponent one. Block 54's local-time clause says the same for a one-site process. The content of the new record (the rule's odds) does not enter here.
- **Block 55's books** give `log κ < 0`.

## Theorem T1 — the inverse law

*Statement.* With one record at `0`, a record formed at an empty site at the rate of that site's clock lands at `d` with probability `w(d)/Σ_{y≠0} w(y)`, with `w(d) = e^(U(d))`. Block 95's motion finds the second record at `d` in proportion to `e^(−U(d))`. The product of the two unnormalized laws is one.

*Proof.* Definitions. Checked exactly at all offsets of a ring of six (base-4 clocks) and of `4³` (symbolic `log κ`) (family B). ∎

## Theorem T2 — every order weighs the same

*Statement.* For a set `C = {x₁, …, x_n}` formed in the order `x_{σ(1)}, …, x_{σ(n)}`, the product of the rates `Π_k w_{x_{σ(k)}}(C_{k−1})` is `e^(Σ_{pairs} U)` for every order `σ`. Here `C_{k−1}` is the set present before the `k`-th formation. The per-step normalization `Σ_{y∉C} w_y(C)` equals `N − |C| − 6 log κ Σ_{y, r ∈ C} G(y − r) + O(log² κ)`.

*Proof.* Each pair is counted once, when its later member forms. The zero-mean kernel sums to zero over all sites. Checked exactly on `4³`: every order of two sets of three records and one set of four (36 orders), and the first-order normalization for three records (families C, D). ∎

## Theorem T3 — formation spreads, motion gathers

*Statement.* For `log κ < 0`, `log w(1,0,0) − log w(2,2,2) = 6 log κ (G(1,0,0) − G(2,2,2)) < 0` on `4³`. A record forms next to another at a lower rate than at the far corner, and block 95's motion finds it there at a higher rate by the same factor.

*Proof.* The exact values of `G` (family E). ∎

## Executed control

Script `specs/supervisor_control_block99_formation.py`, output in `.out.txt`; floating point and sampling, evidence and not proof. 96 records were formed one at a time on `16³`, 60 sets per coupling:

| Coupling | Contacts (formed) | Low-density prediction |
|---|---|---|
| `0` | `6.07 ± 0.34` | — |
| `1/2` | `5.63 ± 0.29` | `5.38` |
| `1` | `4.57 ± 0.28` | `4.34` |
| `2` | `3.65 ± 0.26` | `2.82` |

Uniform placement gives `6.68`. The low-density prediction is the uniform count times `e^(U(1))`; at coupling 2 the first-order picture is past its range. Block 95's control W3 gives the other half: moving at coupling 1, the records condense.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 94's scorecard: reading (iii)'s arrow depends on a formation-rate clause; the fourth reading (records fixed, possibility moving) named by two lenses; blocks 95-98 left formation out"
source_of_blocker_text: block 94 (#8840); blocks 95-98
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "formation and motion placed in one field; the fourth reading has no long-range clumping of records under the clock field; next: the delayed field and formation-with-motion dynamics (probes refill c), the jam"
conditional_surface_status: "T1-T3 exact as stated; the normalization statement at first order; the control executed"
hypothetical_axiom_status: "the owner's reading, block 53's clock field, the motion of blocks 95/97 and the formation clause are hypotheses; nothing adopted"
admitted_observation_status: "none; known physics is not used"
audit_required_before_effective_retained: true
```

## Prior art and what is new

Block 39 (#8530) gave formation at rate `z Z_x` as the creation half of a reversible birth–death pair for the static law, which records that are never removed cannot use. Block 41 (#8547) found that formation next to agreeing records is enhanced by the rule's odds, a contact effect. Block 95's control condensed moving records. Sequential placement with weights set by what is already present is a standard sampling construction.

New here:
- the inverse law between formation and motion on one clock field;
- the order-independence of the formation weight;
- the consequence that long-range clumping in the owner's picture needs motion, and that the fourth reading's fixed records would be spread apart by the same field.

## Exact target and obligation graph

Target: where formation on the site's clock puts records, against motion. The obligations are:
- (O1) two records;
- (O2) any number, including the order of formation;
- (O3) the sign.

T1–T3 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- formation on the site's clock does not gather records;
- in a reading where records never move, the clock field gives no long-range clumping.

### N1 — Routes by which the sentences could fail or mislead
1. *Formation odds that favour neighbours of records* (block 41's contact enhancement). These give short-range clustering, not the `1/r` field's long range.
2. *Formation timed otherwise.* A rate `z w_x^b` with `b < 0` would gather records, but a site could then read the field from its own formation rate; the locality principle excludes it.
3. *High density.* The normalizations' pair-sum term matters there (the control's coupling-2 row).
4. *Records that are removed.* A birth–death pair (block 39 T4) would change the law; the axioms' records are permanent.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The formation clause is supplied and named. Contents are ignored.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | Record; formation rate an open gate | yes |
| block 53 (#8568) | the clock field | yes |
| blocks 95, 97 (#8860, #8872) | motion's pair law; the locality principle | yes |
| block 55 (#8571) | `log κ < 0` | yes |
| blocks 39, 41 | formation as a birth–death half; contact enhancement | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "formation on the site's clock places records by exp(+U), motion by exp(−U): formation spreads, motion gathers" | executed: both laws at every offset of the ring and 4³ | executed: first-order normalization over all empty sites of 4³ | executed: kernel from its modes; control on 16³ | executed: every order of three sets | T1–T2 on every torus; T3 wherever block 95's T4 holds |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- Hostile reviewer: "Formation might not be timed by the site's clock." Reply: it is supplied. The note names the alternative (`b < 0`), which lets a site read the field from its own formation, and the locality principle excludes it.
- Second objection: "Records gather anyway through the rule's odds." Reply: only at contact (block 41). The long range is the clock field's, and there formation spreads.

### N8 — Cross-cycle echo
Block 94 named the fourth reading. Block 95 showed that motion gathers records. This note shows that formation alone spreads them in the same field, so the owner's "records move" is what gives long-range clumping.

## Falsifiers

- An order of formation whose unnormalized weight differs from `e^(Σ_pairs U)`.
- For `log κ < 0`, a second record forming at contact at a higher rate than far away, under the site-clock formation clause.

## Boundaries and non-claims

- The note is conditional on the formation clause and blocks 53, 95, 97 and 55.
- Contents are ignored.
- The jam and the dynamics of formation with motion are not treated; they are among the probes' derivation and computation units.
- No gravitational claim is made, and known physics is not used.

## Imports
- `minimal_axioms`. Blocks 39, 41, 53, 55, 95, 97 (PRs): restated or placed.
- Named standard imports at definition level: sequential weighted sampling; first-order expansion of the exponential; floating-point sampling for the control.

## Review record
- **Who and when.** Supervisor-run block, the forty-seventh since the source-link direction opened and the tenth run on Claude Opus 5.5.
- **What prompted it.** The question of what formation does in block 95's clock field, and whether the fourth reading has clumping.
- **Independence.** No independent review has taken place. Mutation census: six mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_formation_on_the_sites_clock_spreads_records_apart_clumping_needs_records_that_move_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
