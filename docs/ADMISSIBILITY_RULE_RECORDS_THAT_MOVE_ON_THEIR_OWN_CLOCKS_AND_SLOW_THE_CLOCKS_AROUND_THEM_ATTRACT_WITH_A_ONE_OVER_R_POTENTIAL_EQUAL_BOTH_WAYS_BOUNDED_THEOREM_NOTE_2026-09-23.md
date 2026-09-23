---
claim_id: admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "WITHIN the owner's moving-records reading (records move between neighbouring sites, one per site at a time), block 53's supplied clock clause (a positive tick rate at every site, set by the neighbours' rates by one covariant rule, only ratios meaningful; a record sets its site's rate to kappa times its neighbours' mean) and a supplied timing clause (a hop x -> y runs at w_x^a w_y^(1 - a) times the motion rule's factor). Exact: in a fixed rate field the stationary law is W(C) prod w^(1 - 2a); when the rate field follows the records, the chain is in detailed balance with W(C) exp(6 log(kappa)(1 - 2a) sum over pairs of G(r - s)), G the zero-mean inverse of the lattice Laplacian, each pair once; for a = 1 a record's jumps are unbiased and the field acts only on waiting times; G is even and decreases along axes and diagonals on the checked tori, so the pair term is attractive iff (2a - 1) log(kappa) < 0 and exactly reciprocal. Executed: the far field 1/(4 pi r); simulations of the clocked gas (two records, three timings; 96 records condensing into one cluster). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_one_over_r_equal_both_ways_2026_09_23.py
---

# Records that move on their own clocks and slow the clocks around them attract with a 1/r potential, equal both ways

**Date:** 2026-09-23
**Type:** bounded_theorem
**Status:** bounded-support (exact within supplied clauses; nothing adopted or registered; unaudited)

This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) with block 53's supplied clock clause; it reports what records that move on their own clocks and slow the clocks around them do to one another; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The owner, on 2026-09-23, after block 94's scorecard: "I think we are in the third column of your chart, and we need to figure out the not from records alone bits (make sure to check latest PRs and repo though)". The third column is the moving-records reading. Its two cells that records alone do not fill are a reciprocal `1/r` pull and waves. Block 94 credited the pull to the amplitude layer's clock field and scored the record layer as failing. The repository offers other routes, but none of them gives a universal reciprocal pull:
- block 49 (#8559): the capture pull is tied to growth and not reciprocal;
- blocks 41–43 (#8547–#8549): the record layer's equilibrium has no long-range channel for mass, its odds field is charged by content, and its fields arrive by diffusion;
- the ice-rule constructions (main's exact cubic-ice note of 2026-09-03; #8698): Coulomb-phase correlations whose sources are the ice rule's charges, which are signed and not universal;
- #8600 and #8650: waves of content or of link rotors, not a pull.

This note shows that the clock field acts on the records themselves once one timing clause is supplied. The result is exact.

- **T1: which end of a hop keeps its time.** Take a hop `x → y` that runs at `w_x^a w_y^(1−a)`. In a fixed rate field the stationary law is `W(C) Π_{z∈C} w_z^(1−2a)`.
  - Timed by the site it leaves (`a = 1`), a record lingers where clocks are slow. For one record this is block 53's T5.
  - Timed by the bond (`a = 1/2`), nothing happens.
  - Timed by the site it enters (`a = 0`), a record lingers where clocks are fast.
- **T2: the field follows the records.** Every record slows its own site's clock by the ratio `κ` (block 53's law). The whole gas is then in detailed balance with `π(C) ∝ W(C) exp(6 log κ (1 − 2a) Σ_{pairs} G(r − s))`, where `G` is the zero-mean inverse of the lattice Laplacian. The law holds for any number of records, and each pair enters once.
- **T3: the field changes how long a record waits, not where it goes.** Timed by the site it leaves, a record's hops go to every empty neighbour with equal odds, so its expected displacement is zero away from contact. Two records always tick at the same rate. The attraction lives in waiting times: records linger near records because clocks are slow there. This corrects a sentence of block 53, which said the record's mean velocity follows the gradient.
- **T4: one over `r`, equal both ways.** `G` is even, and it decreases along the axes and diagonals of the checked tori. Its far field is `1/(4πr)` (control). So the pair potential `U(r) = 6(2a − 1) log κ · G(r)` is attractive exactly when `(2a − 1) log κ < 0`. It is exactly reciprocal and additive over pairs. For `a = 1` and records that slow clocks, `U(r) ≈ −(3|log κ|/2π)/r` at long range.

The sign of the pull is set by the product `(2a − 1) log κ`, and no clause fixes either factor. Records that move on their own site's clock and slow the clocks around them attract. Records timed by the site they enter repel. A bond clock gives nothing.

In plain terms: suppose a record's clock runs slow near other records, and a record moves when its own clock ticks. Then records spend longer near one another and are found together more often. They are found together exactly as often as a `1/r` attraction would make them, and the preference is exactly mutual. Nothing pushes them: each step goes any way with equal odds. A record simply waits longer where time runs slow, and time runs slow near records. Many such records pull themselves into one clump once the coupling passes a value set by their number and the size of the space. Inside the clump the clocks run so slow that its records hardly move. What still does not come from records alone:
- the clock clause itself (block 53);
- which end of a hop keeps its time;
- inertia, since nothing here orbits, and the amplitude layer is where things fall (block 54);
- the delay of the field, which here follows the records at once;
- waves.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through its exact sentences:
- Lattice (`Z³`, nearest-neighbour adjacency, translations and proper cubic rotations).
- Admissibility (one covariant nearest-neighbour rule). The rule does not "define a time metric" and does not supply the formation "rate".
- Record ("A site never carries more than one record; records are permanent.").
- The open gates on update laws, rates and persistence dynamics.

Nothing is adopted here.

- **P1: the owner's reading** (2026-09-20, restated 2026-09-23; quoted as the owner's, not as axiom text). Records move between neighbouring sites, a site holds one record at a time, and "possibility shifts at the site as the neighborhood changes". `C` is the set of occupied sites with their contents. `W(C) > 0` is the motion rule's weight: block 39's (#8530) product of the rule's pair weights over occupied bonds, or `W ≡ 1` for records with exclusion only. A move `C → C'` takes a record at `x` to an empty neighbour `y`, with heat-bath factor `h = W(C')/(W(C) + W(C'))`.
- **P2: block 53's clock clause** (#8568, supplied). Every site has a tick rate `w_x > 0`, set by the neighbours' rates through one covariant rule, and only ratios of rates mean anything. A record sets its site's rate to `κ` times its neighbours' mean. This note uses the geometric-mean member of the class, for which block 53's T2 gives the exact law `log w_x = (1/6) Σ_e log w_{x+e} + (log κ) n_x`. On an `L³` torus with `N = L³` sites, block 53's T3 gives `log w_z = 6 log κ Σ_{r∈C} G(z − r)`, where `G` solves `6G(d) − Σ_e G(d + e) = [d = 0] − 1/N` with `Σ_d G(d) = 0`. The zero mode, the unit of rate, is set by the mean of `log w`. This `G` is the zero-mean lattice function of Green.
- **P3: the timing clause** (supplied; the new clause of this note). A move `x → y` runs at the rate `w_x^a w_y^(1−a) · h / 6`, with all rates read in the configuration before the move and `a` a fixed real number.
  - `a = 1`: the hop is an event of the site the record leaves, so the record "moves on its own clock".
  - `a = 0`: the hop is an event of the site it enters.
  - `a = 1/2`: the hop is an event of the bond, at the geometric mean.
- **P4: the field follows the records at once.** P2's static law holds in every configuration. How a change of the sources reaches the rates (a delay; block 57, #8578) is not modelled.
- **Mass.** The mass is the record count (block 41, #8547). It is held fixed: formation is not included.

## Theorem T1 — which end of a hop keeps its time

*Statement.* In a rate field `w` that does not depend on the configuration, the chain of P1 and P3 is in detailed balance with `π(C) = W(C) Π_{z∈C} w_z^(1−2a)`.
- For `a = 1`, each record carries the factor `1/w`: records are found where clocks are slow.
- For `a = 1/2`, and for any rate symmetric in the two ends, no factor appears.
- For `a = 0`, each record carries the factor `w`.

*Proof.* Let `D = C ∖ {x} = C' ∖ {y}`. Then `π(C) · rate(C → C') = Π_{z∈D} w_z^(1−2a) · w_x^(1−2a) w_x^a w_y^(1−a) · W(C) W(C') / (6(W(C) + W(C')))`. This equals `Π_{z∈D} w_z^(1−2a) · (w_x w_y)^(1−a) · W(C) W(C') / (6(W(C) + W(C')))`, which is symmetric under `(C, x) ↔ (C', y)`. ∎

The runner checks this on a ring of five with two records, contents `±1` and pair weights `p, q`, with all five rates and the exponent `a` symbolic. It checks 40 configurations and 120 moves in log form, and the three named timings in product form (family B). The single-record cases `a = 1` and a symmetric bond rate are block 53's T5.

## Theorem T2 — when the field follows the records, the law is a pair law

*Statement.* Under P1–P4 on a finite torus, the chain is in detailed balance with

`π(C) ∝ W(C) exp(6 log κ (1 − 2a) Σ_{{r, s} ⊂ C} G(r − s))`,

the sum running over unordered pairs of occupied sites. This holds for any number of records.

*Proof.* Write `λ = log κ`. For the move `x → y`, with `D` as above, set `A = Σ_{r∈D} G(x − r)`, `B = Σ_{r∈D} G(y − r)` and `g = G(x − y) = G(y − x)` (`G` is even, T4). Every rate includes the field of every record, the moving one included. So
- `log w_x(C) = 6λ(G(0) + A)` and `log w_y(C) = 6λ(g + B)`;
- `log w_y(C') = 6λ(G(0) + B)` and `log w_x(C') = 6λ(g + A)`.

The ratio of the two rates is then `log rate(C → C') − log rate(C' → C) = log(W(C')/W(C)) + 6λ(2a − 1)(A − B)`: the terms `G(0)` and `g` cancel. The pair sum changes by `B − A`. So `log π(C') − log π(C) = log(W(C')/W(C)) + 6λ(1 − 2a)(B − A)`, which is the same number. ∎

Each pair enters once. Evaluating T1's fixed-field factor in the slaved field would instead give `Π_z w_z(C)^(1−2a) = exp(6λ(1 − 2a)(|C| G(0) + 2 Σ_{pairs} G))`, which counts each pair twice; that is not the stationary law (the runner's mutation "pair counted twice" fails). The runner checks the identity in `λ` and `a`:
- on a ring of six (one-dimensional law, factor 2 in place of 6), at every configuration of two and three records and every move;
- on `4³`, at 80 moves of six configurations with two and three records, after checking `G`'s defining identity at all 64 sites (family C).

## Theorem T3 — the field changes how long a record waits, not where it goes

*Statement.* Let `a = 1`.
1. The record at `x` hops to each empty neighbour at the same rate `w_x/6`. Its expected displacement per unit time is `(w_x/6) Σ_{e: x+e empty} e`. This is zero when its six neighbours are empty, and it points away from occupied neighbours otherwise, whatever the rate field. In a fixed field on the infinite lattice, with rates bounded above and below and no other record in the way, a lone record's position is a martingale: its expected position never moves. Its sequence of places is that of the plain walk, and the field changes only the waiting times, by `1/w_x` at `x`.
2. Two records always tick at the same rate, `log w = 6λ(G(0) + G(d))` at both, where `d` is their separation. The separation is the plain exclusion walk slowed by the factor `w(d)`, and it is found in proportion to `1/w(d) ∝ exp(−6λ G(d))` (T2 with two records).
3. For `a < 1` the hops are biased: the expected displacement is `(1/6) Σ_{e: x+e empty} e · w_x^a w_{x+e}^(1−a)`, towards faster clocks. With `κ < 1` that is away from other records.

*Proof.*
- Part 1 holds because the rate `w_x/6` does not depend on `e`. The martingale statement is the zero-drift case of the standard formula for chains with bounded jumps and rates.
- Part 2 holds because `G` is even.
- Part 3 is the same sum with rates that depend on `e`.

Family D checks these on `6³` with the slaved field:
- zero displacement with four placements of a second record;
- the contact bias `−w_x/6` along the occupied direction;
- the sign of the `a = 0` bias at `λ = −1/2`;
- equal clocks at all 215 separations. ∎

*Correction to block 53.* Block 53's T5 remark "It is a drift: the record's mean velocity, not its acceleration, follows the gradient, as in block 48" is wrong for its own timing. The record's mean velocity is zero away from contact. What follows the gradient is the flux of its probability, `J_{x→y} = (m_x w_x − m_y w_y)/6`. The record lingers where clocks are slow; it is not carried there, as block 48's bodies are carried by a wind. A corrigendum is pushed on #8568.

So the attraction of T2 is a residence effect. Clocks are slow near records, a record waits longer where clocks are slow, and records are therefore found together. Counted in its own site's ticks, a record's walk is the plain walk. The lingering is seen against the unit of rate, which is the mean clock of P2. The stationary law is reached by spreading, not by motion of records towards one another. A single record in the held field of a finite cluster on the infinite lattice is not bound, because its walk stays transient. On a finite torus the pair law of T2 holds exactly, and with many records it condenses (control W3).

## Theorem T4 — one over `r`, equal both ways

*Statement.*
1. `G(d) = G(−d)` for every offset. So the pair term of T2 is one number seen from either record. The weight of cluster `A` in `B`'s field equals that of `B` in `A`'s, the central-difference pull of `A` on `B` is exactly minus that of `B` on `A` along each axis, and the law is a product over pairs (block 53's T4: superposition).
2. On the `4³` and `6³` tori, `G` decreases strictly along the axes and the body diagonals; on `4³`, `G(1,0,0) = 257/7680` and `G(2,0,0) = 29/7680`.

With `U(r) = 6(2a − 1) log κ · G(r)`, so that `π ∝ W(C) exp(−Σ_{pairs} U)`, the pair term is lower at shorter distance exactly when `(2a − 1) log κ < 0`: records attract. At long range `G(r) → 1/(4π|r|)` (control W1), so `U(r) ≈ (3(2a − 1) log κ/2π)/r`.

*Proof.* Evenness holds because the defining identity is invariant under `d → −d` and the solution is unique. Monotonicity is exact arithmetic on the two tori (family E, which also checks the reciprocity identities for a three-record and a two-record cluster). ∎

Every record is one unit of source (it slows its site's clock by `κ`) and one unit of response (it moves on its site's clock). So the pairing that block 55 (#8571) had to impose on amplitudes, source proportional to response, holds for records by construction. That is why the pull is equal both ways and does not depend on which record is called the source.

## Executed control

Script `specs/supervisor_control_block95_clocked_records.py`, output in `.out.txt`; floating point and simulation, evidence and not proof.

- **W1: the far field.** On `64³`, with the torus background `r²/(6N)` removed, the slope of `G` against `1/r` between successive points is:

  | Direction | Points `r` | Slopes |
  |---|---|---|
  | Axis | 4 to 16 | `0.0831, 0.0810, 0.0802, 0.0794` |
  | Body diagonal | 3.5 to 13.9 | `0.0772, 0.0784, 0.0790, 0.0795` |

  The expected value is `1/(4π) = 0.07958`.
- **W2: two records on `10³` with `log κ = −1`.** The simulated law of the separation matches T2 for all three timings, with total variation `0.003` over 999 separations after 36 million recorded steps. The three exact laws differ from one another by `0.013` to `0.027`, so each run picks out its own timing's law. The probability of contact is:

  | Timing | Contact (simulated) | Contact (exact) |
  |---|---|---|
  | Site it leaves | `0.0087` | `0.0088` |
  | Bond | `0.0060` | `0.0060` |
  | Site it enters | `0.0041` | `0.0041` |

  A uniform law would give `0.0060`. For `a = 1`, the mean displacement of a record is `0.0000` at every separation checked beyond contact and `−0.0286 = −w/6` at contact (T3).
- **W3: 96 records on `16³` (density `3/128`) with `a = 1` and `log κ = −g`.** 20 million events from a random start, two seeds (both values shown). The mean-field column is the comparator `(1 − ρ)/(1 − 6gρ(1 − ρ)/E(k_min))` for the spread gas.

  | `g` | Records touching another | Largest cluster's share | `S(k_min)` | Mean-field `S` |
  |---|---|---|---|---|
  | 0 | 0.131 / 0.131 | 0.027 / 0.027 | 0.99 / 0.99 | 0.98 |
  | 0.5 | 0.163 / 0.163 | 0.030 / 0.030 | 1.73 / 1.74 | 1.78 |
  | 0.8 | 0.859 / 0.859 | 0.840 / 0.840 | 62.2 / 62.2 | 3.51 |
  | 1.0 | 0.950 / 0.950 | 0.946 / 0.946 | 70.1 / 70.2 | 9.97 |
  | 1.5 | 0.993 / 0.993 | 0.993 / 0.992 | 73.3 / 73.3 | none |
  | 3.0 | 1.000 / 1.000 | 1.000 / 1.000 | 74.3 / 74.3 | none |

  At `g = 0.5` the gas stays spread and matches the comparator. From `g = 0.8` it condenses into one cluster that coexists with a vapour of free records. This is below the spread gas's mean-field stability limit, `g = E(k_min)/(6ρ(1 − ρ)) = 1.109`, and near an energy–entropy count that puts the collapse into a single ball of 96 records at `g ≈ 0.887`.
- **W4: the condensed state along the runs at `g = 0.8`.** The gas stays spread at first. Then a cluster nucleates: within the first two million events for one seed, and between two and four million for the other. After that, a vapour of 9–22 free records coexists with the cluster. The slowest clocks, at the cluster's centre, run at between `e^(−10.6)` and `e^(−11.8)` of the mean clock, so the cluster's inner records hardly ever move.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the owner's request of 2026-09-23 ('I think we are in the third column of your chart, and we need to figure out the not from records alone bits'); block 94's scorecard cell 'static potential proportional to 1/r, reciprocal' for reading (iii)"
source_of_blocker_text: owner, 2026-09-23; block 94 (#8840); decision record #8572
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the waves cell of the moving-records column (records that carry a direction; the walk; link memory); the delayed clock law (P4 relaxed: does detailed balance survive a field that follows the records late?); a formation clause with the clock (does formation timed by the site's clock keep the pair law?)"
conditional_surface_status: "T1-T4 exact as stated within P1-P4; W1-W4 executed"
hypothetical_axiom_status: "the owner's moving-records reading, block 53's clock clause, the timing clause and the instant field are hypotheses; nothing adopted"
admitted_observation_status: "none; known physics is not used"
audit_required_before_effective_retained: true
```

## Prior art and what is new

Block 53's T5 (#8568) found that one test record, timed by its own site's clock in a held field, has the law `1/w`, and that timing by the mean of two rates gives the uniform law. Block 53's T4 gave the additivity and the symmetric pair term of the field. Block 54 (#8570) found that an amplitude whose phase is timed by the clock falls towards slow clocks, with force equal to energy times the gradient. Block 55 (#8571) found that action equals reaction for amplitudes only if the source is proportional to the energy. Block 39 (#8530) gave the pair-weight motion and its equilibrium, and block 41 (#8547) the mass as record count. Blocks 44–52 gave the capture picture's pull, which block 49 tied to growth. Block 94 (#8840) set out the scorecard whose cell this note revises.

From the literature, named at definition level:
- A chain whose rates out of a state are all multiplied by a positive factor keeps its jump chain, and its stationary law is divided by the factor. This is the time change of a Markov chain; T1 with one record is an instance.
- Diffusion with a position-dependent rate relaxes to a law weighted by the inverse rate, with no mean velocity. This is the difference between the forms of Itô and of the "isothermal" or Smoluchowski equation, discussed by van Kampen ("Itô versus Stratonovich", 1981).
- A lattice gas with a pair potential `∝ −1/r` is the lattice form of the self-gravitating gas, reviewed by Padmanabhan (Physics Reports 188, 1990). Its uniform state is unstable to clumping above a size set by the coupling and the density: the instability of Jeans, used here only as the mean-field comparator of W3.

New here:
- the exponent family `w^(1−2a)` with its sign rule, where the entering end repels;
- the pair law of T2 for a gas whose records are both sources and movers, each pair once;
- the statement that the clock field acts on waiting times only (T3), with the correction to block 53;
- the reading that the moving-records column's reciprocal `1/r` cell is filled by records plus the clock clause plus the timing clause.

## Exact target and obligation graph

Target: what must be supplied, besides records, for a reciprocal `1/r` pull in the moving-records reading, and what it gives exactly. The obligations are:
- (O1) the stationary law in a held field for every timing;
- (O2) the stationary law when the field follows the records;
- (O3) what the field does to a record's motion;
- (O4) the sign, range and reciprocity of the pair term.

T1–T4 discharge them.

## No-Go Discipline Gate

The note's negative sentences:
- a bond clock gives no pull;
- timed by the site it leaves, a record's hops are unbiased and its mean velocity is zero away from contact;
- the fixed-field factor evaluated in the slaved field is not the stationary law;
- nothing here is an acceleration.

### N1 — Routes by which the sentences could fail or mislead
1. *A field that follows the records late.* P4 fails if the log rates relax by diffusion (block 43) or with a delay (block 57); detailed balance with T2's law is then not established. Open, and next.
2. *Other timing laws.* In a held field only the ratio `rate(x → y)/rate(y → x)` enters the stationary law; `w_x^a w_y^(1−a)` covers the power ratios, and any ratio `(w_x/w_y)^(2a−1)` gives the same law.
3. *A contact dependence of `κ`* (on content or on occupied neighbours; block 53's remark). This changes contact terms and not the long range.
4. *A master clock* (block 53's N1, route 1). A mass term would screen the field.
5. *A configuration-dependent unit of rate.* Multiplying all rates by `c(C)` divides the law by `c(C)` (block 50's T1). P2's unit is the mean of `log w`, which is the same in every configuration.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
P2–P4 are supplied and named. The zero mode is fixed by P2. The record count is fixed (no formation). The heat-bath factor is block 39's; any motion rule in detailed balance with `W` gives the same results.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the Lattice, Admissibility and Record sentences; the open gates | yes |
| block 53 (#8568) | the clock clause P2, its exact geometric-mean member, the zero mode; T5 as prior art; corrected in T3 | yes |
| block 39 (#8530) | the motion rule and `W` | yes (placed) |
| block 41 (#8547) | mass = record count | yes (placed) |
| blocks 49, 54, 55 (#8559, #8570, #8571) | the capture pull, the amplitude's fall, the source–response pairing | no (comparison) |
| block 94 (#8840) | the scorecard cell revised | no (placement) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "stationary law `W Π w^(1−2a)` in a held field; pair law `W exp(6 log κ (1 − 2a) Σ_pairs G)` when the field follows the records; unbiased jumps for `a = 1`; attraction iff `(2a − 1) log κ < 0`, reciprocal" | executed: detailed balance at every configuration and move on rings of five and six, symbolic | executed: `G`'s identity at all 64 sites of `4³`; the slaved balance at 80 moves; the displacement on `6³` | executed: `G` from its nonzero modes on `4³` and `6³`; control far field | executed: monotone decrease; reciprocity for two clusters | T1–T2 on every finite graph with an even kernel (proofs above); T3–T4 as stated |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration. `κ` and `a` are left free.

### N7 — Steelman
- Hostile reviewer: "This is block 53's T5 again." Reply: T5 is one test record in a held field. T2 is the gas whose records both make and feel the field, which could have failed (a held field would count each pair twice). T1's exponent family, the entering end and T3 are new.
- Second objection: "A pull with zero mean velocity is not a pull." Reply: the stationary law is exactly that of a `1/r` attractive pair potential. The note states that the effect lives in waiting times and corrects block 53's sentence.
- Third objection: "The sign is put in by hand." Reply: yes, through `(2a − 1) log κ`, and the note says so.

### N8 — Cross-cycle echo
Block 42 found its odds field massless only on a tuned surface, and block 49 that a long range needs a field protected by a conservation law or a symmetry. Block 53 supplied such a field, since no master clock means no mass term. Block 49 closed the capture pull. This note returns the record layer to the scorecard's pull cell through the same clock field that blocks 53–55 used for amplitudes.

## Falsifiers

- A move of the slaved-field chain that violates detailed balance with T2's law, on any torus, for any `a`.
- A record timed by the site it leaves, with six empty neighbours, whose expected displacement is nonzero.
- A torus of side at least 4 on which `G` fails to decrease from `(1,0,0)` to `(2,0,0)`.

## Boundaries and non-claims

- The note is conditional on P2–P4, which are supplied. The sign needs `(2a − 1) log κ < 0`, which no clause fixes.
- There is no inertia (nothing orbits) and no delay (the field acts at once).
- Formation is not included: the record count is fixed.
- The law is measured against P2's unit of rate.
- W3's clumping is an executed observation, and its threshold is compared with a mean-field value only.
- No gravitational claim is made, and known physics is not used.

## Imports
- `minimal_axioms`. Blocks 39, 41, 43, 48–50, 53–55, 57, 94 (PRs): restated or placed.
- Named standard imports at definition level:
  - detailed balance;
  - the time change of a chain;
  - the zero-drift martingale formula for chains with bounded jumps and rates, and transience of the three-dimensional walk;
  - the zero-mean lattice function of Green and its far field (executed);
  - the Itô and Smoluchowski forms of diffusion with a position-dependent rate (van Kampen);
  - the self-gravitating lattice gas and the instability of Jeans (Padmanabhan's review), as comparators only;
  - floating-point FFT and continuous-time simulation for the control.

## Review record
- **Who and when.** Supervisor-run block, the forty-third since the source-link direction opened and the sixth run on Claude Opus 5.5. Asked by the owner on 2026-09-23.
- **Repository survey before the block.**
  - The open PRs since 2026-09-20, including #8545, #8600, #8650 and #8698.
  - The notes on main that touch `1/r` and waves (the cubic-ice note of 2026-09-03).
  - Main's integration commits, which now carry the reviewed source units up to #8177.
- **Own-prior-art check.** It found block 53's T5. That led to T1's generalisation and to the correction in T3.
- **Supervisor checks.**
  - The runner's families by hand.
  - T2's cancellation, redone symbolically for general `a`.
  - The control's two-record law against T2 for all three timings.
- **Independence.** No independent review has taken place. Mutation census: nine mutations, each failing in its own family.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_one_over_r_equal_both_ways_2026_09_23.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
