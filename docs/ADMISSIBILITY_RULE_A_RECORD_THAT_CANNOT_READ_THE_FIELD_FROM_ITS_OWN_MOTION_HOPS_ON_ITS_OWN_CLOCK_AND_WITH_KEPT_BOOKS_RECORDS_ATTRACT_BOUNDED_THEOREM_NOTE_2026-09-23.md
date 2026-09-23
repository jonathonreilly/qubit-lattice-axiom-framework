---
claim_id: admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the owner's moving-records reading, block 53's clock clause, a supplied principle that a record cannot read the field from its own motion, and block 55's kept books. Exact: among degree-one rate laws w_x^a w_y^(1 - a) a record's hop rate per tick of its own site, and the odds of the direction it takes, are free of the field only for a = 1 (the site it occupies times the hop); for amplitudes the three timings (site entered, bond, site left) are similar generators, one dynamics, while for records they are three stationary laws (1/w, 1, w per record); with a = 1 and block 55's log(kappa) = -(gamma/6) E/wbar, block 95's pair term is attractive. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_2026_09_23.py
---

# A record that cannot read the field from its own motion hops on its own clock, and with kept books records attract

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; nothing adopted or registered; unaudited)

This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) with block 53's clock clause, a supplied locality principle and block 55's kept books; it reports which end of a hop keeps its time when a record cannot read the field from its own motion, and the sign of the pull that follows; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 95 (#8860) found that records hopping in block 53's clock field attract or repel according to the product `(2a − 1) log κ`. Here a hop `x → y` runs at `w_x^a w_y^(1−a)`, and a record slows its site's clock by `κ`. No clause fixed either factor. This note fixes both with two principles: one of locality, which is new here, and block 55's kept books.

- **T1: a record that cannot see the field in its own motion hops on its own site's clock.**
  - Every rate `w_x^a w_y^(1−a)` has degree one: there is no master clock.
  - Counted in ticks of the site it occupies, a record hops `(w_y/w_x)^(1−a)` times per tick. It picks among its empty neighbours in proportion to `w_y^(1−a)`.
  - Both are free of the field only for `a = 1`. Timed by the bond, a record hops `√(w_y/w_x)` times per own tick; timed by the site it enters, `w_y/w_x` times, and it heads for fast clocks.
  - So the principle that a record cannot read the field from its own motion gives `a = 1`: a record's hop is a process of the site it occupies.
- **T2: why the question never arose for amplitudes.**
  - For an amplitude, timing by the site entered (`WH`), by the bond (`√W H √W`) or by the site left (`HW`) gives similar generators: one dynamics in three sets of variables. Block 54's walk falls towards slow clocks whichever is chosen.
  - For records, the three timings have different stationary laws, `1/w`, `1` and `w` per record: three different dynamics.
  - Timing is a matter of variables for amplitudes and a matter of physics for records. Block 54's clause, that the amplitude at a site advances in that site's own time, did not need to choose, and it does not choose here: read as the arrival of a record at a site, it would give `a = 0`. The principle of T1 is what decides.
- **T3: with kept books, records attract.** Block 55 found that if the books balance (action equals reaction), a body of energy `E` sources the clock field with `log κ = −(γ/6) E/w̄`, so records slow clocks. With `a = 1`, block 95's pair term is `U(r) = −(γE/w̄) G(r)`. It is lower at shorter distance: on `4³`, `U(1,0,0) − U(2,0,0) = −(γE/w̄)(228/7680)`. Records attract, as amplitudes fall.

In plain terms: if every record lives by the clock of the place it sits, it cannot tell from its own hopping where it is. That is the only choice under which a record's own motion carries no trace of the field. And if records slow the clocks around them, which is what balanced books require, then records attract. The same two rules make waves fall towards slow clocks (block 54). Matter and waves then both move towards slow clocks, by one field and one number.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`): Admissibility does not "define a time metric"; update laws and rates are open gates.
- **The owner's reading.** Records move, one per site at a time; quoted as the owner's.
- **Block 53's clock clause** (#8568). A tick rate `w_x > 0` at every site; only ratios mean anything (rate laws of degree one); records slow or speed their site's clock by `κ`.
- **Block 54's local-time clause** (#8570). "The amplitude at a site advances in that site's own time." It is used here only in T2, for comparison.
- **The principle of this note** (supplied). *A record cannot read the field from its own motion.* Counted in ticks of the site it occupies, its hop rate and the odds of its direction do not depend on the clocks. T1 shows this is the timing `a = 1`, in which a record's hop is a process of the site it occupies and runs on that site's clock.
- **Block 55's kept books** (#8571). The pair of clock field and bodies keeps a ledger. A body pulled in proportion to its energy `E` sources in the same proportion, `log κ = −(γ/6) E/w̄`, with `γ` the one pure number of the lane (positive, for a positive field energy).
- **Block 95's pair law** (#8860): `π ∝ W(C) exp(6 log κ (1 − 2a) Σ_pairs G(r − s))`.

Nothing is adopted.

## Theorem T1 — a record that cannot see the field in its own motion hops on its own site's clock

*Statement.* For the rate `w_x^a w_y^(1−a)`, which has degree one for every `a`:
- the hop rate per tick of the occupied site is `(w_y/w_x)^(1−a)`;
- the odds of a direction among empty neighbours are `w_y^(1−a)/Σ w^(1−a)`.

Both are independent of the clocks for all fields if and only if `a = 1`. More generally, a degree-one rate is `w_x φ(w_y/w_x)`, and its per-own-tick rate `φ(w_y/w_x)` is field-free if and only if `φ` is constant.

*Proof.* The derivative of `(w_y/w_x)^(1−a)` in `w_y` is `(1 − a)` times a positive factor. The odds are uniform if and only if the exponent `1 − a` vanishes. The general form follows from degree one with `t = 1/w_x`. Families B and E, symbolic. ∎

## Theorem T2 — timing is variables for amplitudes and physics for records

*Statement.*
1. For a hermitian nearest-neighbour `H` and a positive diagonal `W`, the three generators satisfy `W^(−1/2)(WH)W^(1/2) = W^(1/2) H W^(1/2) = W^(1/2)(HW)W^(−1/2)`.
2. For one record with rates `w_x^a w_y^(1−a)`, the stationary law is `w^(1−2a)`: `1/w`, `1` and `w` for `a = 1, 1/2, 0`.

*Proof.* Matrix algebra, and the detailed-balance law of block 95's T1. Checked on a ring of four with symbolic clocks and complex hopping (family C). ∎

## Theorem T3 — with kept books, records attract

*Statement.* With `a = 1` and `log κ = −(γ/6) E/w̄` (`γ, E, w̄ > 0`), block 95's pair term is `U(r) = −(γE/w̄) G(r)`. It is lower at shorter distance wherever `G` decreases, and it falls as `1/r`. On `4³`, `U(1,0,0) − U(2,0,0) = −(γE/w̄)(G(1,0,0) − G(2,0,0)) = −(γE/w̄)(228/7680) < 0`.

*Proof.* Substitution in block 95's T4; exact values of `G` on `4³` (family D). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 95 (#8860): 'the sign of the pull is set by (2a - 1) log(kappa), and no clause fixes either factor'"
source_of_blocker_text: block 95's result; the owner's request of 2026-09-23
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "sign fixed within the locality principle and the kept books; next candidates: one geometry (the clock field of a condensed clump bending a route's waves, deflection against the pair law); the delayed clock law; formation with the clock"
conditional_surface_status: "T1-T3 exact as stated; the locality principle and the kept books are supplied"
hypothetical_axiom_status: "the owner's reading, the clock clause, the locality principle and the kept books are hypotheses; nothing adopted"
admitted_observation_status: "none; known physics is not used"
audit_required_before_effective_retained: true
```

## Prior art and what is new

Block 53 (#8568) gave the clock clause and a test record's law `1/w`. Block 54 (#8570) gave the local-time clause for amplitudes and the similarity of `WH` and `√W H √W`. Block 55 (#8571) gave the kept books and `log κ = −(γ/6) E/w̄`. Block 95 (#8860) gave the timing family, the pair law and the sign rule.

In the physics comparator, the analogue of T1's principle is Einstein's requirement that no local experiment reveals a uniform field. It is named here as motivation only.

New here:
- the characterisation of `a = 1` as the unique field-free timing, for both the rate and the odds of direction;
- the contrast in T2: similar generators for amplitudes, different laws for records;
- the sign of the pull fixed by the two clauses together.

## Exact target and obligation graph

Target: which end of a hop keeps its time, and the sign of the pull, within principles already in the lane. The obligations are:
- (O1) the field-free timing;
- (O2) why amplitudes did not need it;
- (O3) the sign with the kept books.

T1–T3 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- no timing other than `a = 1` leaves a record's own motion free of the field;
- the three record timings are not one dynamics.

### N1 — Routes by which the sentences could fail or mislead
1. *Bonds with clocks of their own* (block 59's bond rates). If a hop were a process of the bond, the bond's rate `a = 1/2` would time it and there would be no pull (block 95's T1). The record would then hop `√(w_y/w_x)` times per own tick: it could read the field. T1's principle excludes this.
2. *The arrival reading of block 54's clause.* Read as the arrival of a record at a site, block 54's clause gives `a = 0`, repulsion and a record that heads for fast clocks. T1's principle excludes this too.
3. *Rate laws not of degree one.* These need a master clock (block 53).
4. *A negative field energy* (`γ < 0`). Block 55's T4 shows that like energies would then repel.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The principle that a record cannot read the field from its own motion is supplied and named. So are the kept books.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no time metric; open gates | yes |
| block 53 (#8568) | clock clause; degree one | yes |
| block 54 (#8570) | local-time clause for amplitudes (comparison in T2) | no (comparison) |
| block 55 (#8571) | kept books; `log κ` | yes |
| block 95 (#8860) | timing family; pair law; sign rule | yes |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "only a = 1 leaves a record's own motion field-free; timing is variables for amplitudes and physics for records; with kept books records attract" | executed: own-tick rate and direction odds, symbolic | executed: one record's laws for three timings | executed: similarity of the amplitude generators | executed: the pair term's sign on 4³ | T1 for every degree-one law; T2 on every finite graph; T3 wherever block 95's T4 holds |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- Hostile reviewer: "You chose the principle that gives attraction." Reply: the principle is that a record cannot read the field from its own motion. That is a statement about locality, not about the sign. T1 shows it has a unique solution, and N1 names the two readings that would give no pull or repulsion; both let a record read the field from its own hopping.
- Second objection: "Block 55's kept books were for amplitudes." Reply: block 55 already stated the records form, `log κ = −(γ/6) E/w̄`. A record that falls like an amplitude of energy `E` must source like one.

### N8 — Cross-cycle echo
Block 95 left the sign open. A locality principle (T1) and block 55's books close it.

## Falsifiers

- A degree-one rate law other than `c·w_x` whose per-own-tick rate is field-free.
- A timing `a ≠ 1` with field-free direction odds.
- `WH` and `√W H √W` not similar for some positive `W`.

## Boundaries and non-claims

- The note is conditional on the principle of T1, the kept books and block 95's clauses.
- It fixes the sign, not the size (`γ`, `E`).
- There is no inertia and no delay, as in block 95.
- No gravitational claim is made, and known physics is not used.

## Imports
- `minimal_axioms`. Blocks 53, 54, 55, 59, 95 (PRs): restated or placed.
- Named standard imports at definition level: homogeneous functions of degree one; similarity of matrices; detailed balance.
- Einstein's requirement that no local experiment reveals a uniform field, as motivation only.

## Review record
- **Who and when.** Supervisor-run block, the forty-fifth since the source-link direction opened and the eighth run on Claude Opus 5.5.
- **What prompted it.** Block 95's open sign.
- **A correction made while writing.** The first draft read block 54's clause as the principle. T2 shows that clause does not decide for records: read as the arrival of a record, it gives `a = 0`. The principle is now stated on its own, as the requirement that a record cannot read the field from its own motion.
- **Own-prior-art check.** Blocks 53–55, 59, 95. Block 54's similarity of generators was known there. The contrast with records is new.
- **Independence.** No independent review has taken place. Mutation census: six mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
