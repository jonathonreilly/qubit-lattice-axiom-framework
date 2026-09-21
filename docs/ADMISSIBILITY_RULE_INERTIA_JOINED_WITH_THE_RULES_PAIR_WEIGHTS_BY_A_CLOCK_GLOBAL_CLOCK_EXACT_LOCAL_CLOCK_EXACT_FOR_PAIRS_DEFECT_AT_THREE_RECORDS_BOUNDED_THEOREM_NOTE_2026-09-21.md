---
claim_id: admissibility_rule_inertia_joined_with_the_rules_pair_weights_by_a_clock_global_clock_exact_local_clock_exact_for_pairs_defect_at_three_records_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied inertial clause of block 44 (PR #8550; six-axis menu: a record's content is its direction of travel; an empty target is entered, an occupied target exchanges contents) and the supplied law with vacancies of block 39 (PR #8530; pi(C) = product over adjacent occupied pairs of c omega(a, b), omega = p, q, r for equal, opposite, orthogonal contents); nothing adopted. (T1) GLOBAL clock: every record of a configuration has exactly one streaming event and exactly one predecessor through such an event, so the unit-clock dynamics has as many ways into a configuration as out of it (block 44); if every event of C runs at the rate 1/pi(C), then pi is stationary, for any positive weights, any density and any window, and number and momentum are conserved event by event: a change of time, not local. (T2) LOCAL clock: if the event of the record at x runs at the rate 1/pi_x(C), pi_x the product of the pair weights of site x, then out(C) - in(C) = sum over the records whose site behind is occupied of W_0 [A_b(u) - A_x(u)], u the content behind, A_b(u) and A_x(u) the weight of u among the other neighbours of the site behind and of the record's site, W_0 the weight of the pairs that touch neither; hence pi is stationary in the two-record sector and whenever no such pair of sites has a third record next to it, and is not stationary at three records: on the 3x3x3 torus at (p, q, r) = (3, 1, 2), c = 1, the balance fails at 3168 of the 70200 three-record configurations with a record at the origin (28512 of all 631800), the largest defect being 3 = (c r - 1) + (c p - 1). (T3) In the two-record sector the stationary law is the rule's pair law; at the neutral scale c_0 = 6/(p + q + 4r) the mean pair weight is one, and c_0 r = 1 exactly when p + q = 2r, which holds at (3, 1, 2). Without re-drawing the dynamics is not irreducible (two records on a common line with contents along it never leave it); uniqueness of the stationary law is not claimed. (T4) Re-drawing the two contents of a bond on their momentum class with probabilities proportional to pi satisfies detailed balance with respect to pi, conserves the pair's momentum and is local. NOT claimed: a local clock that is exact at all densities (open), any hydrodynamic statement for the weighted gas, the sphere menu, any gravitational statement, any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_inertia_joined_with_the_rules_pair_weights_by_a_clock_global_exact_local_exact_for_pairs_defect_at_three_records_2026_09_21.py
---

# Inertia joined with the rule's pair weights by a clock: a global clock is exact, a local clock is exact for pairs and fails at three records

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements on finite windows within two supplied clauses; one open question named; nothing adopted or registered; unaudited)

This note works within the supplied inertial clause of block 44 and the supplied law with vacancies of block 39; it reports which clocks let streaming keep that law stationary; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The campaign's decision record (PR #8555) lists as open that the inertial clause of block 44 does not use the rule's weights `(p, q, r)` at all: its equilibrium is structureless. Blocks 39 and 40 (PRs #8530, #8546) had the opposite: records that move by pair weights, with the rule's law as equilibrium, and no inertia. This note asks whether the two can be had together: records that travel along their contents, number and momentum conserved event by event, **and** the rule's law with vacancies as the stationary law.

1. **Yes, with a global clock.** In block 44's dynamics every record of a configuration has exactly one event and exactly one predecessor, so there are as many ways into a configuration as out of it. Let every event of `C` run at the rate `1/π(C)`. Then `π` is stationary, for any weights, any density, any periodic window of side at least three (T1). The configurations are visited in the same order as before; only the waiting times change. But the clock of a record then reads every pair weight of the configuration: it is not local.
2. **A local clock is exact for pairs and fails at three.** Let the event of the record at `x` run at the rate `1/π_x(C)`, the inverse of the product of its own pair weights: a record lingers where its content agrees with its neighbours' and hurries where it disagrees. Then the flow of `π` out of a configuration minus the flow into it is an explicit sum over the records that have another record directly behind them (T2). It vanishes for two records, and whenever no such pair has a third record next to it. It does not vanish at three records: at `(3, 1, 2)` the balance fails at 3168 of the 70200 three-record configurations with a record at the origin, by at most 3.
3. **What the law then says.** For two records the stationary law is the rule's pair law: neighbours with equal, opposite and orthogonal contents weigh `cp, cq, cr` against 1. At the neutral scale `c₀ = 6/(p + q + 4r)` of block 40 the mean pair weight is one; and `c₀r = 1` exactly when `p + q = 2r`, which holds at `(3, 1, 2)`: there, orthogonal neighbours are neutral (T3).
4. **Re-drawing with the weights.** A bond's two contents can be re-drawn on their momentum class with probabilities proportional to `π`: detailed balance, momentum conserved, local (T4).

So the rule's weights can ride with inertia exactly, at the price of a clock that is not local; with a local clock they can do so only while records meet in pairs. Whether some local clock is exact at all densities is open.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision record (PR #8555), fork 6: 'the inertial clause does not use the rule's weights (p, q, r) at all yet; a clause joining inertia with the rule is open'"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "a global clock joins inertia with the rule's law exactly; a local clock does so for pairs and fails at three records with an explicit defect; next: decide by a linear feasibility computation on the three-record sector whether any local rule (rates that read only the neighbourhoods of the two sites of an event) is exact; queued on ai/probes"
conditional_surface_status: "T1 exact for any finite window on which block 44's unit-clock dynamics keeps the uniform measure; T2's identity proved for any number of records and checked at two and three on the 3x3x3 torus; T3, T4 exact; the open question is named in N1"
hypothetical_axiom_status: "the inertial clause of block 44, the law with vacancies and the scale c of block 39, and the clocks of this note; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the six-axis menu and the weights `(p, q, r)`. Blocks 39, 40 and 44 (open PRs #8530, #8546, #8550) supply the law with vacancies and its scale `c`, the neutral scale `c₀ = 6/(p + q + 4r)`, and the inertial clause with its stationary uniform measure. They are restated; the runner re-derives what it uses.

- **Configuration, weight.** A set of occupied sites with one of six contents each; `π(C) = Π c·ω(a, b)` over adjacent occupied pairs, `ω = p, q, r` for equal, opposite and orthogonal contents. (The activity per record is a constant factor at fixed number and is dropped.)
- **Event of a record.** The record at `x` with content `s` has the target `x + e_s`. If the target is empty the record enters it; if it is occupied the two contents are exchanged. *Site behind:* `x − e_s`.
- **Predecessor.** The configuration from which the record now at `x` arrived by its own event: the same record one site back if the site behind is empty, the two contents exchanged back if it is occupied.
- **Unit clock, global clock, local clock.** Every event at the rate one; every event of `C` at the rate `1/π(C)`; the event of the record at `x` at the rate `1/π_x(C)`, `π_x` the product of the pair weights of site `x`.
- **`W₀`, `A_b(u)`, `A_x(u)`.** For a record at `x` whose site behind, `b`, holds the content `u`: `W₀` the weight of the pairs that touch neither `x` nor `b`; `A_b(u)` the product of `c·ω(u, ·)` over the occupied neighbours of `b` other than `x`; `A_x(u)` the same over the occupied neighbours of `x` other than `b`.

A change of the time scale of a jump process by a function of the state is a classical device for processes named after Markov; persistent motion that samples a law of the kind named after Gibbs is what lifted and event-chain samplers do (Diaconis and co-workers; Krauth and co-workers), and the rule by which a vetoed move passes on to the vetoing partner is the ancestor of the exchange of contents used here; conditions of pairwise balance for driven lattice gases go back to Schutz and co-workers. None is used as authority.

## Prior art and what is new

Time changes and lifted samplers are classical. What is new is their exact form in the campaign's clause: that block 44's event structure (one event and one predecessor per record) makes the global clock exact for any weights and density; the explicit defect of the natural local clock, which is supported on records that have another record directly behind them and a third record next to the pair; its vanishing for pairs; and the count and the largest defect at three records.

## Exact target and obligation graph

Target: records that travel along their contents, with number and momentum conserved event by event, and the rule's law with vacancies stationary. Obligations: (O1) a clock that does it; (O2) a local clock, and where it fails; (O3) what the stationary law says; (O4) re-drawing contents with the weights. T1–T4 discharge them; the open part of O2 is named in N1.

## Theorem T1 — the global clock

Take a periodic window of side at least three, so that the target of a record and the site behind it are distinct. In block 44's dynamics every record of a configuration has exactly one event. The predecessor map inverts it: if the site behind the record at `x` is empty, the configuration with the record one site back has the event that leads to `C`; if it is occupied, the configuration with the two contents exchanged back has the record at the site behind pointing at an occupied target, and its event leads to `C`. So every configuration with `n` records has `n` events out and `n` events in, and with unit clocks the uniform measure is stationary (block 44). Events move contents or exchange them, so the number of records and the sum of the contents' directions are conserved.

Let every event of `C` run at the rate `1/π(C)`, for any positive `π`. The flow of `π` out of `C` is `π(C)·n/π(C) = n`; the flow into `C` is the sum over its `n` predecessors `C″` of `π(C″)/π(C″) = 1`, that is `n`. So `π` is stationary. The same holds with block 44's scattering included, since its unit-clock kernel is symmetric. The configurations are visited in the same order as with unit clocks; only the waiting times change. ∎

The clock is not local: the rate of a record's event is the inverse of the product of all pair weights of the configuration.

## Theorem T2 — the local clock and its defect

Let the event of the record at `x` run at the rate `1/π_x(C)`. Its flow out of `C` is `π(C)/π_x(C)`, the weight of the pairs of `C` that do not touch `x`.

*A record whose site behind is empty.* Its predecessor has the same record one site back and everything else unchanged; the flow in is the weight of the pairs that do not touch the record, which is the same number. The two cancel.

*A record at `x` whose site behind, `b`, holds `u`.* Its predecessor has the record's content at `b` and `u` at `x`, and the active record is the one at `b`; the flow in is the weight of the predecessor's pairs that do not touch `b`, that is `W₀·A_x(u)`. The flow out is the weight of the pairs of `C` that do not touch `x`, that is `W₀·A_b(u)`.

Hence, for any number of records,

`out(C) − in(C) = Σ W₀ [A_b(u) − A_x(u)]`, summed over the records whose site behind is occupied. ∎

**Consequences.** (i) With two records there is no third: `A_b = A_x = 1` and `π` is stationary (checked at all 936 two-record configurations with a record at the origin, for the weights `(3, 1, 2)`, `(5, 2, 4)` and `(3, 1, 2)` at the neutral scale `1/2`). (ii) `π` is balanced at every configuration in which no record with an occupied site behind it has a third record next to either of the two sites. (iii) At three records the balance fails: on the `3×3×3` torus at `(3, 1, 2)`, `c = 1`, at 3168 of the 70200 configurations with a record at the origin, which is 28512 of all 631800 configurations. The largest defect is 3, at the records `(0,0,0)` with content `+y`, `(0,0,1)` with `+z`, `(0,1,0)` with `+y`: the second and the third each have the first directly behind them, and in each case the remaining record is next to the first; the two terms are `cr − 1` and `cp − 1`.

## Theorem T3 — what the stationary law says, and what it does not

In the two-record sector `π` is one on configurations whose records are not adjacent and `cp`, `cq`, `cr` on adjacent pairs of equal, opposite and orthogonal contents: the rule's pair law. With the local clock a record next to another waits `c·ω` times as long. At the neutral scale of block 40 the mean of `c₀ω(a, ·)` over the partner's six contents is `c₀(p + q + 4r)/6 = 1`: adjacent pairs are as frequent as without weights, and only the contents of neighbours are correlated. Moreover `c₀r = 6r/(p + q + 4r)` equals one exactly when `p + q = 2r`; this holds at `(3, 1, 2)`, where orthogonal neighbours are therefore neutral at the neutral scale and the defect of T2's witness reduces to `c₀p − 1 = 1/2`. ∎

Stationarity is not uniqueness. Without re-drawing, two records on a common line whose contents lie along that line never leave it, so the dynamics is not irreducible, on this window or any other. The refuting pass's simulation reaches the rule's ratios `3 : 1 : 2` on the configurations that a generic start can reach, and never visits the others.

## Theorem T4 — re-drawing contents with the weights

Let a bond whose two sites are occupied re-draw its two contents on their momentum class (the ordered pairs of contents with the same sum of directions: one pair for equal contents, two for orthogonal ones, six for opposite ones) with probabilities proportional to `π` of the resulting configuration. For two members `i, j` of a class, `π_i·P(i → j) = π_iπ_j/Σπ = π_j·P(j → i)`: detailed balance with respect to `π`. The pair's momentum is conserved by construction, and the probabilities read only the contents next to the two sites. With the unit re-draw of block 44 (uniform on the class) detailed balance fails as soon as the class has members of different weight. ∎

This is the re-drawing that goes with the local clock. Under the global clock block 44's uniform re-draw needs no change (T1).

## No-Go Discipline Gate

The note's negative sentences: the global clock is not local; the local clock `1/π_x` does not keep `π` stationary at three records; without re-drawing the dynamics is not irreducible.

### N1 — Routes by which the sentences could fail
1. *Another local rule* — rates of an event that read the neighbourhoods of both sites of the event, or an event other than the exchange of contents when the target is occupied. The balance conditions are linear in the rates, so on the three-record sector the question is a finite linear feasibility problem. It is not decided here. This is the note's open question.
2. *Weights that make the defect vanish* — `A_b(u) = A_x(u)` for all environments needs `cω ≡ 1`, the structureless case of block 44; at the neutral scale on the line `p + q = 2r` the orthogonal part vanishes and the equal and opposite parts do not.
3. *A dilute gas* — the defect is supported on meetings of three records; at small density the local clock is exact up to terms of that order. No bound is claimed.
4. *The sphere menu* — not treated; the event structure (one event and one predecessor per record) is specific to contents that are lattice directions.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T1 uses block 44's stationarity of the uniform measure, which the runner re-derives through the predecessor map on the window used. The three-record count is for one window and one weight triple; the identity is general.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; permanence | yes (premise) |
| block 01 (`main`) | the six-axis menu and the weights | yes (premise, proposed) |
| block 39 (open PR #8530) | the law with vacancies and its scale | yes (restated) |
| block 40 (open PR #8546) | the neutral scale | yes for T3 (restated) |
| block 44 (open PR #8550) | the inertial clause; the uniform stationary measure | yes (restated; re-derived on the window) |
| decision record (open PR #8555) | the open fork this note works | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "one event and one predecessor per record; the global clock keeps `π`; the local clock's defect is `Σ W₀[A_b(u) − A_x(u)]`; zero for pairs, 3168 of 70200 at three; `c₀r = 1` iff `p + q = 2r`; weighted re-drawing is in detailed balance" | executed: every event of the two-record sector and its inverse; the momentum classes of a bond | executed: the local-clock balance at all 936 two-record configurations for three weight sets; the defect identity at all 70200 three-record configurations | not applicable | executed: the global-clock balance in both sectors; the count, the largest defect and its configuration; the neutral scale for three triples; detailed balance next to a third record | T1 holds for any weights, density and window on which the unit-clock dynamics keeps the uniform measure; T2's identity is proved for any number of records; whether some local clock is exact at all densities is open |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no update law. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "The global clock is a trick: any law is stationary for some time change." Reply: yes, and that is the content of T1: because block 44's events form a bijection on configurations, inertia puts no constraint at all on the stationary law, so the structureless equilibrium of block 44 was a choice of clock and not a consequence of inertia. The constraint comes from locality, and T2 measures it. Second objection: "A defect at three records on a small torus may be an artefact of the window." Reply: the identity is local and holds on any window; the witness uses three mutually close records and no wrapping.

### N8 — Cross-cycle echo
Block 39 had the rule's law without inertia; block 44 had inertia without the rule's law; block 38 found that under a fixed predecessor structure every rate clause gives one law. Here the predecessor structure is a bijection, and the law is again free: it is fixed by the clocks, not by the streaming.

## Falsifiers

- A configuration of block 44's dynamics with a number of predecessors different from its number of records; a positive `π` that the global clock does not keep stationary.
- A configuration at which `out − in` under the local clock differs from `Σ W₀[A_b(u) − A_x(u)]`; a two-record configuration with a non-zero defect.
- A momentum class on which the weighted re-draw violates detailed balance.

## Boundaries and non-claims

One window (`3×3×3` torus) and one weight triple for the three-record count; the six-axis menu only. No local clock exact at all densities is exhibited or excluded. No statement is made about currents, pressure or sound in the weighted gas, about irreducibility with re-drawing, or about the uniqueness of the stationary law. The clocks are supplied clauses. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menu and the weights; proposed, unaudited. Blocks 39, 40, 44 and the decision record (PRs #8530, #8546, #8550, #8555, open): restated or placed.
- Named standard imports at definition level: stationarity of a measure under a jump process as the balance of flows (processes named after Markov); detailed balance.
- Reference only: changes of time; lifted and event-chain samplers (Diaconis and co-workers; Krauth and co-workers); pairwise balance (Schutz and co-workers).

## Review record
Supervisor-run block of the 12-hour campaign. Lens: the decision record's fork 6. The expectation going in was that streaming cannot keep a weighted law without breaking momentum conservation (a vetoed move must turn the record back); the observation that block 44's events form a bijection removed the veto altogether: a clock does it. An exact scratch check on two and three records confirmed the global clock and showed where the local clock fails before anything was written. Refuting pass (`specs/supervisor_control_block50_refuter.py`, machinery disjoint from the runner's): W1, W2 forward flux accounting over the full two- and three-record sectors (12636 and 631800 configurations); W3 symbolic weights; W4 a continuous-time simulation of two records with local clocks; W5 the neutral scale symbolically. It returned three findings, all folded: the runner's count 3168 is of configurations with a record at the origin, and the full sector has nine times as many (the supervisor had expected twenty-seven times); the simulation reached `2 : 2/3 : 2` instead of `3 : 1 : 2` until the closed classes of collinear pairs were recognised, which is now the last paragraph of T3; and a symbolic check failed on a floating-point zero produced by dividing two integers. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_inertia_joined_with_the_rules_pair_weights_by_a_clock_global_exact_local_exact_for_pairs_defect_at_three_records_2026_09_21.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
