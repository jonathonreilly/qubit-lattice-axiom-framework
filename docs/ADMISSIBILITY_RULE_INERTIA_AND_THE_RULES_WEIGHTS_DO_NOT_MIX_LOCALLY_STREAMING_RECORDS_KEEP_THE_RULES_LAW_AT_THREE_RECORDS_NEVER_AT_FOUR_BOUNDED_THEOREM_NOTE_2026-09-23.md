---
claim_id: admissibility_rule_inertia_and_the_rules_weights_do_not_mix_locally_streaming_records_keep_the_rules_law_at_three_records_never_at_four_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN block 50's supplied clauses: six-axis records whose content is a direction of travel, streaming (enter an empty target, exchange contents with an occupied one), the rule's pair weights pi(C) = product of c omega(a, b) at (3,1,2) with c = 1 and the neutral scale c0 = 1/2; rates that depend only on the sites within distance one of an event's two sites (radius one), up to the event's symmetries. Exact (a probes worker's result, verified here in exact arithmetic): block 50 reproduced; with every move at the local clock or at rate one no exchange rates balance the three-record sector, and no rule balances record by record; radius-one rules exist for three records (exact rules on 3^3 and 4^3); none exists for four records on 3^3, nor on Z^3 (compact clusters whose equations agree on 6^3 and 9^3), with or without head-on pairs re-drawing on their momentum class. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_inertia_and_the_rules_weights_do_not_mix_locally_2026_09_23.py
---

# Inertia and the rule's weights do not mix locally: streaming records keep the rule's law at three records, never at four

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; a probes worker's result, verified here; referee of another model family pending; nothing adopted or registered; unaudited)

This note works within block 50's supplied clauses (records whose content is a direction of travel, streaming with exchange, the six-axis rule's pair weights) and reports, from a probes worker's exact certificates verified here, whether local rates can keep the rule's law stationary; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 96 (#8866) found that inertia, like waves, needs something that time reversal flips. Records carrying a direction of travel are the natural candidate (block 44). Block 50 (#8562) asked whether such records can move while keeping the Admissibility rule's pair weights as their long-run law:
- a global clock can do it, but it is not local;
- the local clock `1/π_x` fails at three records;
- whether any local rule works was left open.

A probes worker answered it (task `J:derive:local-clock-for-inertia-with-weights:a1`, worker `w-macbookpro90c72-j5257`, Claude Opus 5.5). This note restates the result and verifies it in exact arithmetic.

- **T1: the natural clocks fail.** With every move at the local clock `1/π_x`, or at rate one, no choice of exchange rates balances the three-record sector (at `c = 1` and at the neutral scale `c₀ = 1/2`). No rule balances each record against its own predecessor.
- **T2: three records can be balanced locally.** Rates that depend only on the sites within distance one of an event exist that keep the rule's law stationary for three records. There are exact rational rules on `3³` (274 rate classes) and `4³` (353), and the worker also found one on `5³`. They are irregular vertices of a polytope of solutions; no closed form was found.
- **T3: four records cannot.** No such rule balances the four-record sector: on `3³`, and on `Z³` through compact four-record clusters whose balance equations are the same on the `6³` and `9³` tori. This holds with or without head-on pairs re-drawing on their momentum class. Exact certificates of infeasibility, using four-record rows only, settle it.

So in the moving-records column, records that carry momentum cannot also keep the rule's weights with local rates, beyond three records. A gas with inertia either gives up the rule's weights in its long-run law (block 44's structureless law) or needs non-local rates (block 50's global clock). With block 96, this points inertia towards possibility (the walk, block 54) or towards contents that change.

In plain terms: if records remembered their direction of travel, their motion could not respect the rule that says which neighbours they prefer, at least not with rules that only look next door, once four records are involved.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`): Admissibility (one covariant nearest-neighbour rule) and Record. Motion and rates are open gates. Nothing is adopted.
- **Block 50's objects** (#8562, from block 44, #8550).
  - Six-axis contents `±x, ±y, ±z`.
  - The rule's law with vacancies `π(C) = Π` over adjacent occupied pairs of `c ω(a, b)`, with `ω = p, q, r = 3, 1, 2` for equal, opposite and orthogonal contents, at `c = 1` and `c₀ = 6/(p + q + 4r) = 1/2`.
  - Streaming: the record at `x` with content `s` targets `x + e_s`, enters it if empty, and exchanges contents with it if occupied.
- **The locality class** (supplied). A rate is any nonnegative function of the contents and occupancies of the sites within distance one of `x` or of its target (12 sites; 11 on `3³`), taken up to the 8 lattice symmetries that fix the event. The enlarged family adds a head-on pair (the target holds `−s`) re-drawing on its momentum class to `(a, −a)`, `a` transverse, at its own local rates.
- **The problem.** For every configuration `C`, the flow of `π` out must equal the flow in, `Σ π(C) r = Σ π(C'') r`, with moves at rates at least one and exchanges at least zero.
- **Provenance.** The result and its certificates are the probes worker's, proposed by a linear-programming solver and verified in exact rational arithmetic. Its companion attempt a2 (`w-jonathonsmac4f50-j42a0`, Claude Opus 5) agrees on `3³`. The supervisor re-ran the verification and ported it into this note's runner. All three are the same model family; a referee of another family has not yet run.

## Theorem T1 — the natural clocks fail

*Statement.* On `3³` at `(3,1,2)`:
1. Block 50 is reproduced. There are 70,200 three-record configurations with a record at the origin. Each has three events out and three in, so the global clock balances. The local clock `1/π_x` fails at 3,168 of them, with largest defect 3.
2. With every move at the local clock, or at rate one, no exchange rates balance the three-record sector, at `c = 1` and at `c₀`. Each case has a certificate: a combination of balance equations that no admissible exchange rates can meet.
3. No rule balances each record's event against its own predecessor.

*Proof.* The balance equations are linear in the rates. A nonnegative combination `y` of equations with `Mᵀy ≥ 0` over the free rate classes and `b·y < 0` for the fixed ones excludes every choice (family B, exact). ∎

## Theorem T2 — three records can be balanced locally

*Statement.* Exact rational radius-one rules exist, with moves at least one and exchanges at least zero, that balance every three-record configuration:
- on `3³`: 274 rate classes, 70,200 configurations;
- on `4³`: 353 rate classes, 421,848 configurations.

Both hold at `c = 1` and at `c₀`.

*Proof.* Every configuration's balance, evaluated exactly with the stated rates (family C). ∎

## Theorem T3 — four records cannot

*Statement.* There is no radius-one rule balancing the four-record sector:
- on `3³`, for streaming alone and with head-on re-draws, at `c = 1` and `c₀`;
- on `Z³`: the balance equations of compact four-record clusters (a record at the origin, the others in `[0, 2]³`) are identical on the `6³` and `9³` tori, so they are equations of the problem on `Z³`, and a certificate on this subset excludes every rate function.

Every event conserves the number of records and the total content vector, so number and momentum are kept whatever the rates.

*Proof.* Certificates `y ≥ 0` on four-record rows only, with `Aᵀy ≥ 0` on every rate class and `y·(Aℓ) > 0` for `ℓ = 1` on moves (families D, E, exact; rows recomputed on both tori). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 50 (#8562): 'OPEN: does any local rule keep pi stationary at all densities?'; block 96 (#8866): inertia needs a variable time reversal flips"
source_of_blocker_text: block 50; block 96; probes derivation J:derive:local-clock-for-inertia-with-weights
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "radius-one rules exist at three records and fail at four; next: a larger locality class at four records (radius two), the three-record sector on Z^3, and inertia carried by possibility (the walk) against inertia carried by records"
conditional_surface_status: "T1-T3 exact as stated on the stated tori and on Z^3 through compact clusters; the locality class and block 50's clauses supplied; certificates proposed by a solver and verified exactly"
hypothetical_axiom_status: "block 50's clauses (content as direction, streaming, the rule's weights as the target law) and the locality class are hypotheses; nothing adopted"
admitted_observation_status: "none; known physics is not used"
audit_required_before_effective_retained: true
```

## Prior art and what is new

Block 44 (#8550) gave the streaming clause, with a structureless equilibrium. Block 50 (#8562) gave the global clock (exact, not local), the local clock's failure at three records, and the open question answered here. Blocks 39 and 40 gave the rule's law with vacancies and the neutral scale. The certificate method is the standard alternative for linear feasibility (Farkas's lemma); the proposals came from the HiGHS solver.

New here, from the probes worker and verified by the supervisor:
- exact local rules at three records;
- the natural clocks' failure as certificates;
- the four-record obstruction on `3³` and on `Z³`, with and without momentum-class re-draws.

## Exact target and obligation graph

Target: block 50's open question. The obligations are:
- (O1) the natural local clocks;
- (O2) three records;
- (O3) four records, on `Z³`.

T1–T3 discharge them at radius one.

## No-Go Discipline Gate

The note's negative sentences:
- no radius-one rule balances four streaming records under the rule's weights;
- the local clock and unit moves fail at three;
- no rule balances record by record.

### N1 — Routes by which the sentences could fail or mislead
1. *A larger locality class* (radius two). Not tried; it might dissolve the four-record obstruction.
2. *Other target laws.* A structureless law (block 44) is kept by streaming with re-draws. The obstruction is to keeping the rule's weights.
3. *Non-local rates* (block 50's global clock) keep any law.
4. *Other menus or weights.* Only the six-axis rule at `(3,1,2)`, `c = 1` and `c₀`, is treated.
5. *Inertia elsewhere.* Possibility's walk carries inertia (block 54) and is not a record gas.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
Block 50's clauses and the locality class are supplied and named. The solver proposes; exact arithmetic verifies.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | Admissibility; motion and rates open | yes |
| block 50 (#8562) | objects, local clock, open question | yes |
| block 44 (#8550) | streaming clause | yes |
| blocks 39, 40 | law with vacancies; neutral scale | yes (placed) |
| block 96 (#8866) | inertia needs a coupling time reversal flips | no (placement) |
| probes worker `w-macbookpro90c72-j5257` | the result and its certificates | yes (verified here) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "streaming records keep the rule's law with radius-one rates at three records, never at four" | executed: every three-record configuration of 3³, 4³ against exact rules; every certificate row | executed: block 50's defects at all 70,200 configurations | not applicable | executed: clusters compared on 6³ and 9³ | T1–T2 on the stated tori; T3 on 3³ and Z³ |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- Hostile reviewer: "Radius one is arbitrary." Reply: it is the class block 50 asked about, and the note names radius two as open.
- Second objection: "A solver found the certificates." Reply: a solver proposed them. Every one is verified in exact arithmetic by the runner, and a certificate for a subset of equations excludes all rates.

### N8 — Cross-cycle echo
Block 50 left the question open, and block 96 said inertia needs a reversal-odd variable. This note shows the obvious record-level carrier cannot keep the rule's weights locally.

## Falsifiers

- A radius-one rule balancing every four-record configuration of `3³` under the rule's weights.
- A certificate row whose balance equation differs between the `6³` and `9³` tori.

## Boundaries and non-claims

- The note holds at radius one, for the six-axis rule at `(3,1,2)` at the two scales stated.
- The three-record sector on `Z³` is open.
- No gravitational claim is made, and known physics is not used.

## Imports
- `minimal_axioms`. Blocks 39, 40, 44, 50, 54, 96 (PRs): restated or placed.
- Named standard imports at definition level:
  - linear feasibility and its certificates (Farkas's lemma);
  - the HiGHS linear-programming solver, as a proposer only;
  - exact rational arithmetic.

## Review record
- **Who and when.** Supervisor-run block, the forty-eighth since the source-link direction opened, built from a probes worker's result at the owner's prompt ("are you writing blocks from the opus probe work?", 2026-09-23).
- **Provenance.** Worker `w-macbookpro90c72-j5257` (Claude Opus 5.5) and a2 (`w-jonathonsmac4f50-j42a0`, Claude Opus 5) are the same family as the supervisor. The supervisor re-ran the exact verification (all checks pass, 155 s) and ported it. No referee of another family has yet run.
- **Independence.** Mutation census: six mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_inertia_and_the_rules_weights_do_not_mix_locally_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
