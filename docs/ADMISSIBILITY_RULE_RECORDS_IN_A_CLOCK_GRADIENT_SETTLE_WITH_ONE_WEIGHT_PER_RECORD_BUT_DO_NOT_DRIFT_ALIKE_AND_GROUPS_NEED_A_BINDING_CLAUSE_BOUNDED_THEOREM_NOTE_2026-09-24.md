---
claim_id: admissibility_rule_records_in_a_clock_gradient_settle_with_one_weight_per_record_but_do_not_drift_alike_and_groups_need_a_binding_clause_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional positive pair-weight transit in a supplied fixed linear clock field. Local detailed balance
  gives a reversible weight, not a probability equilibrium on the infinite lattice. Finite irreducible translation-covariant
  tether models have a centre-clock linear response with explicit diffusion constants. A separate bounded-kernel
  pair model has no stationary separation probability. No universal fall, binding mechanism or physical-time asymptotic
  is established.
upstream_dependencies:
- admissibility_rule_binding_scale_pinned_at_the_neutral_value_pair_weight_is_the_rules_likelihood_ratio_no_binding_without_a_cycle_all_binding_is_agreement_around_loops_bounded_theorem_note_2026-09-20
- admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
- admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20
runner: scripts/admissibility_rule_records_in_a_clock_gradient_settle_with_one_weight_per_record_but_do_not_drift_alike_2026_09_24.py
---

# Reversible clock-gradient weights and conditional drift of tethered records

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 95's clocked transit as landed, a held uniform gradient and, for groups, a supplied binding clause; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note studies supplied pair-weight transit in a held clock gradient: local reversible weights, centre-clock drift of tethered groups and a conditional absence of stationary separation; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Under the owner's reading, records move, one per site at a time. Block 95, as landed, times a record's moves by the clocks at its site and at its target, with a timing number `a`. This note asks whether records in a clock gradient fall alike. The comparator, used only as a comparator, is known physics, where every body falls alike.

- **T1: one record.** A record's mean velocity, on its own clock, is `b + ((1 − a)/6) M g` at first order in the gradient `g`. The matrix `M` and the contact bias `b` depend on its neighbours only through the pair weights and exclusion. An isolated record, of any content, has `b = 0` and `M = I`. At `a = 1` there is no gradient term at any order: the direction of a record's hop never depends on the field.
- **T2: reversible weight.** In the held gradient, block 95's law is `π(C) ∝ W(C) exp((1 − 2a) n g·X)`, with `X` the centre of the `n` records. That is one factor `(2a − 1) g` per record, whatever the contents or the shape. The clock exponent is independent of content; the full weight W still depends on content and shape. It is not summable over translations on Z³.
- **T3: how a group moves.** A group of `n` records held in a finite set of shapes by a binding clause drifts, on its centre's clock, at

  `V = −((2a − 1)n − 1) D₀ g + O(g²)`,

  where `D₀` is the group's field-free diffusion constant.
- **T4: the drift is not universal.**
  - At `a = 1` a lone record does not drift at all.
  - A bound pair drifts towards slower clocks at `D_pair g`.
  - `D_pair` depends on the pair's contents: `2/105`, `2/135` and `1/54` for equal, opposite and orthogonal contents, against `D₀ = 1/12` for a lone record.
  - How fast a group falls depends on its size and on how freely it moves inside itself.
- **T5: a conditional nonbinding model.** The supplied bounded-kernel pair model has no stationary separation probability on `Z³`: the separation's reversible measure never falls below a positive constant. So T3 needs a binding clause, which is not derived here.
- **T6: not a contact force.** At `a = 1`, two records in contact along the gradient are pushed towards faster clocks, at `(e^g − 1)/24` in label time with w(0)=1, because the faster record is pushed off more often. The same pair, tethered, drifts towards slower clocks. The finite internal law and centre-clock rates determine the tethered drift.

The clock factor has the same exponent per record, but it does not determine a normalized infinite-lattice equilibrium or universal settling. On a finite closed connected configuration class it can be normalized. The centre-clock drift of a supplied bound group depends on its size and internal mobility. The tether is an added model constraint, not derived binding.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full): "Each site has a domain of local possibilities."; "Admissibility is not a dynamics axiom."; it does not "define a time metric". The clocks, the transit and the binding are supplied clauses. Nothing is adopted.
- **Block 95** (#8860, landed on main).
  - A move takes a record at `x` to an empty neighbour `y` at rate `exp[a u_x + (1 − a) u_y] h/6`, where `h = W(C′)/(W(C) + W(C′))`. Proposals are symmetric and the record count is fixed.
  - T1 as landed: in a configuration-independent field, `π(C) ∝ W(C) Π_z w_z^{1−2a}`.
- **Pair weights.** `W(C)` is block 39's product of pair weights over occupied bonds (#8530, landed). The examples use block 40's neutral-scale values at `(p, q, r) = (3, 1, 2)`: `3/2`, `1/2` and `1` for equal, opposite and orthogonal contents.
- **The field.** A held uniform gradient `u = log w = g·x` on `Z³`. It is a declared field, not produced by the records here. T2 asserts local detailed balance only: translation makes its weight nonsummable, including zero gradient. Normalization and long-time settling require a finite closed communicating class. A nonzero linear gradient is not periodic. No nonexplosion assertion is made for the unbounded label-time rates.
- **Groups.** `n` records whose relative configuration `σ` stays in a finite set `S`, with positive translation-covariant weights and an irreducible internal transition graph. A move that would leave `S` is forbidden, and so is its reverse. This is a supplied binding clause, not proposed as physics. The examples use a tether: two records whose offset stays among the 6 nearest and 12 face-diagonal offsets. The centre is `X`, and the centre's clock is `dτ = w(X) dt`.
- **Names.** The principal eigenvalue of a finite irreducible generator is Perron's and Frobenius's; the isotropy step is Schur's lemma; the positive-recurrence criterion and uniqueness of an invariant measure up to scale for an irreducible recurrent chain are standard imports. The cycle criterion alone would not prove positive recurrence.

## Theorem T1 — one record in a gradient

*Statement.*
- The mean velocity of record `i` on its own clock is `b_i + ((1 − a)/6) M_i g + O(g²)`, with `M_i = Σ_{e free} h_e e eᵀ` and `b_i = (1/6) Σ_{e free} h_e e`.
- An isolated record, of any content, has `h = 1/2` on all six moves, so `b = 0` and `M = I`.
- With one neighbour at `ê` of pair weight `ω`, each of its five free moves breaks that bond: `h = 1/(1 + ω)`, `M = h(2I − êêᵀ)` and `b = −(h/6) ê`.
- At `a = 1` the velocity is `b` exactly: the gradient enters no hop's direction.

*Proof.* The rate of hop `e` is `w_x e^{(1−a) g·e} h_e/6`. Expand the exponential. At `a = 1` it is 1. The runner checks this symbolically in `g` and `a`, for the isolated record and for all three contents (family B). ∎

## Theorem T2 — a local reversible weight

*Statement.* In the held gradient, block 95's T1 becomes `π(C) ∝ W(C) exp((1 − 2a) n g·X)`: one factor per record, whatever the contents or the shape.

*Proof.* This is a positive sigma-finite reversible weight. Its sum over translations diverges: the exponential grows in one direction when its translation exponent is nonzero, and is constant otherwise. On a finite closed irreducible class it instead normalizes to the unique stationary probability. `Π_z w_z^{1−2a} = exp((1 − 2a) g·Σ_z z)`, and `W` is invariant under translation. The runner checks detailed balance for every move of two records in four configurations, symbolic in `g`, `a` and the contact weight (C1). ∎

## Theorem T3 — how a bound group drifts

*Statement.*
- Divide every rate by the centre's clock `w(X)`. The chain of `(X, σ)` is then in detailed balance with `W(σ) exp(−c g·X)`, where `c = (2a − 1)n − 1`.
- For the finite irreducible binding class above, covariant under cubic rotations, the group's long-time mean velocity on its centre's clock is `V = −c D₀ g + O(g²)`. Here `D₀` is the field-free diffusion constant of its centre. For `c = 0` the velocity is exactly zero.

*Proof.*
- A hop of record `i` by `e` runs at `q₀ e^{g·(r_i + (1−a)e)}` on the centre's clock, where `r_i` is the record's offset from the centre, and it moves the centre by `e/n`.
- The heat-bath factor balances `W`. The exponents balance exactly when `−c/n + (1 − 1/n) − 2(1 − a) = 0`. The runner checks every move of a lone record and of a tethered pair, symbolically in `g`, `a` and the contact weight (C2).
- So the tilted generator has principal eigenvalue `Λ(g, k)` with two zeros: `Λ(g, 0) = 0` (the stationary law) and `Λ(g, cg) = 0` (the positive eigenvector `W`).
- `Λ` is analytic near the origin, being a simple eigenvalue. So `Λ(g, k) = k·V(g) + k·D(g)k + …`, and `V(0) = 0`.
- For c nonzero, expanding the second zero gives `sym(dV/dg) = −c D₀`. Cubic covariance makes both scalars. For c=0 the two zeros coincide and that expansion supplies no inference. Instead, detailed balance pairs every directed internal transition and its reverse with opposite centre increments under W/Z, giving exactly zero mean velocity. The finite internal chain has bounded rates on the centre clock, so its stationary additive drift is well defined. ∎

## Theorem T4 — the drift is not universal

*Statement.* At first order, exactly:
- **A lone record:** `D₀ = 1/12`. Its velocity is `0` at `a = 1`, `g/24` at `a = 3/4` and `g/6` at `a = 0`.
- **Tethered pairs** with contact weights `3/2`, `1/2` and `1`: `D_pair = 2/105`, `2/135` and `1/54`.
  - At `a = 1` they drift towards slower clocks at `D_pair g`.
  - At `a = 3/4`, where `c = 0`, they do not drift.
  - At `a = 0` they drift towards faster clocks at `3 D_pair g`.
- So the drift per unit gradient differs between a lone record and a pair, and between pairs of different contents.

*Proof.* Exact linear algebra on the chains of T3. The runner solves the first-order stationary law and the field-free corrector equation `−L₀ψ = b·k` for `D₀`, at `a = 1, 3/4, 0` and for the gradient along `(1,0,0)` and `(1,2,3)`. It finds `V₁ = −c D₀ g` in every case, with `D₀` isotropic and the internal law `W/Z` (D1). ∎

## Theorem T5 — conditional absence of stationary separation

Supply on Z³ an even translation-invariant kernel G with finite constant diagonal and 0 <= G(d) <= G(0), finite real lambda and a, and positive contact weight omega; W(d)=omega at nearest-neighbour separation and one elsewhere. These are extra mathematical hypotheses: current block 95 establishes a finite neutralized-torus model, not this infinite-lattice extension. Recompute each clock after a move by u_z=6lambda sum_r G(z-r).

For the two-record relative chain on Z³ minus {0}, forward/reverse ratios give reversible weight m(d)=W(d) exp[6lambda(1-2a)G(d)]. Evenness and the constant diagonal cancel self terms exactly as in the finite parent proof. This weight is bounded below by min(1,omega) exp[-6|lambda(1-2a)|G(0)]>0, hence nonsummable. The relative graph is connected and all allowed rates are bounded above and below by positive constants, so the chain is irreducible and nonexplosive. If it had a stationary probability it would be positive recurrent; uniqueness of its invariant measure up to scale would force m to be summable, a contradiction. This excludes stationary separation probability only in this supplied bounded-kernel model, not every binding mechanism. The argument is analytic; the runner does not execute an infinite-volume recurrence test.

## Theorem T6 — the push at contact is the opposite of the fall

*Statement.* At `a = 1`, with exclusion only (`h = 1/2`), two records in contact along the gradient have centre velocity `(e^g − 1)/24` in label time with their sites at 0 and e1 and w(0)=1, towards faster clocks. Dividing by w(X)=exp(g/2) gives centre-clock velocity sinh(g/2)/12; its sign agrees. The same pair, tethered, drifts at `−D_pair g`, towards slower clocks.

*Proof.* Each record's five free moves run at its own clock over 12. The two contact biases are opposite, and they are weighted by different clocks. The runner checks this exactly and compares it with T4 (E1). ∎

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "the third column's fall under the owner's reading: do moving records fall alike? block 95 as landed gives the fixed-field law and clock-only motion, not the drift of groups"
source_of_blocker_text: the owner's reading (records move); block 95 as landed; the probes problem do-records-fall-with-a-universal-weight
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a binding clause in the moving-records column, and the law D0(n) for the groups it binds; a field that responds to the drifting group (block 57's delay)"
conditional_surface_status: "T1, T2, T4 and T6 exact; T3 exact with the named imports; T5 by the recurrence criterion"
hypothetical_axiom_status: "the transit, its timing a, the pair weights, the held gradient, bounded kernel in T5 and binding clause are hypotheses; nothing adopted"
admitted_observation_status: "known physics (bodies fall alike) is a comparator only"
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 95 (landed) gave the fixed-field law. Its T3 gave clock-only motion at `a = 1`: with `W = 1` a record's hops run at `w_x/12` and point uniformly among empty neighbours.
  - Block 97 (landed) studied the timing `a`.
  - Block 99 (landed) studied sequential formation weights beside block 95's motion.
  - Block 40 (landed) gave the neutral-scale weights, and block 39 (landed) the pair-weight transit.
- **The probes attempt.** `do-records-fall-with-a-universal-weight` a1 (worker `w-macbookpro9927a-j4d29`, Claude Opus 5.5) derived T1–T6. A Grok referee (`referee_w-macbookpro90c72-j17d3`) confirmed the partial result: the drift is not universal across a lone record and a bound pair, while the equilibrium weight is one factor `(2a − 1)` per record. The referee noted that the tether is a finite witness, not a property of block 95's free pairs. The present T5 separately states the extra infinite-lattice bounded-kernel hypotheses.
- **In the literature.** The drift–diffusion relation `V = −c D₀ g` is the lattice form of the relation of Einstein and Smoluchowski between mobility and diffusion. The comparator's universality of free fall is Galileo's and Eötvös's. Perron's and Frobenius's theorem, Schur's lemma and the irreducible-chain positive-recurrence criterion are standard.
- **New here:**
  - an independent runner, with its own code, for T1–T4 and T6;
  - the statements placed against block 95 as landed;
  - the reading for the third column: the reversible clock exponent is content-independent, but group drift is not universal, and binding is not supplied.

## Exact target and obligation graph

Target: do moving records fall alike? The obligations are:
- (O1) one record;
- (O2) the local reversible weight, with finite-volume normalization only;
- (O3) groups;
- (O4) whether groups exist without a clause.

T1–T6 address these conditional model questions; deriving binding, physical-time asymptotics and universal falling remains open.

## No-Go Discipline Gate

The note's negative sentences:
- the drift is not universal;
- the supplied bounded-kernel pair model has no stationary separation probability on `Z³`.

### N1 — Routes by which the sentences could fail or mislead
1. *Physical time.* The drift statements are on the centre's clock. The conversion to label time multiplies by `w(X)` at first order. That conversion is a sketch here and not claimed.
2. *The binding clause.* T3 and T4 hold for a group held by a supplied clause. Another binding could change `D₀`, but not the non-universality at `a = 1`: a lone record does not drift, and a bound group with `n ≥ 2` and `D₀ > 0` does.
3. *Fields that respond.* The gradient is held. A field that responds to the group, as with block 57's delay, is not treated.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The imports are named at definition level under Imports: the principal eigenvalue of a finite irreducible generator, analytic perturbation of a simple eigenvalue, the isotropy lemma for the cubic group, and the recurrence criterion.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | a site's possibilities; no dynamics or time metric in the axioms | yes |
| block 95 (#8860, landed) | the transit, its timing and the fixed-field law | yes |
| blocks 39, 40 (landed) | the pair weights and their neutral values | yes |
| probes `do-records-fall-with-a-universal-weight` a1 (Grok-refereed) | T1–T6 first derived | historical provenance only |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "reversible clock weights and conditional group drift" | executed: one record's first-order velocity, isolated and with one neighbour of each content (symbolic in `g` and `a`); no gradient term at `a = 1` | executed: detailed balance of block 95's law in a linear field for two records, and of the centre-clock chain's tilted measure, move by move (symbolic) | executed: the exact first-order drift and diffusion constant of a lone record and of tethered pairs of three contents, at `a = 1, 3/4, 0` and two gradient directions | executed: the push at contact against the long-time drift of the same pair | T1–T4 and T6 on `Z³` in a held uniform gradient for block 95's transit; T3–T4 for a group held by a supplied binding clause; T5 on `Z³` only under the extra bounded-kernel hypotheses; the transit, `a`, the pair weights and the binding supplied |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The equilibrium weight is universal, so records do fall alike." *Reply:* The clock exponent alone is content-independent; on Z³ there is no normalized settling law. Along the way, the drift per unit gradient is set by `((2a − 1)n − 1)D₀`. That is zero for a lone record at `a = 1` and positive for a bound pair, and it differs between contents.
- *Objection:* "A tether is artificial." *Reply:* Yes, and T5 says so. The supplied bounded-kernel model has no stationary separation probability, so a group needs a clause. The tether is a finite witness; other binding laws require the hypotheses of T3.

### N8 — Cross-cycle echo
- Block 95 gave the transit and the fixed-field law. Block 99 studied formation weights beside it.
- This note answers whether records fall alike: a content-independent clock exponent does not establish universal settling or universal drift.

## Falsifiers

- A lone record at `a = 1` with a nonzero drift in a held gradient.
- A group held by a cubic-symmetric binding whose first-order drift is not `−((2a − 1)n − 1)D₀ g`.
- A stationary separation probability satisfying all hypotheses of T5.

## Boundaries and non-claims

- The transit, its timing, the pair weights, the held gradient and any binding are supplied.
- Physical-time drift is not claimed.
- No binding clause is proposed, and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 39, 40, 95, 97 and 99, restated or placed.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the Perron–Frobenius theorem;
  - analytic perturbation of a simple eigenvalue;
  - Schur's lemma;
  - the irreducible-chain positive-recurrence criterion;
  - exact symbolic arithmetic.

## Review record — historical author provenance

- **Who and when.** Supervisor-run block, the fifty-ninth since the source-link direction opened; 2026-09-24.
- **Provenance.** The probes attempt `do-records-fall-with-a-universal-weight` a1 (Claude Opus 5.5) derived the results. A Grok referee confirmed them. The supervisor re-checked them with its own runner.
- **Before writing.** Main was re-fetched, and block 95 was read as landed (1cb2a082bf).
- **Prior art.** Own blocks and the probes' attempts were searched for "drift", "universal weight", "tether" and "bound pair". There was one attempt on this problem, and no block.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_records_in_a_clock_gradient_settle_with_one_weight_per_record_but_do_not_drift_alike_2026_09_24.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.

## Current dependencies and scope corrections

The original author/probe reports above are history, not current review authority. The filename remains a historical identifier. No infinite-volume settling claim is retained; T5 adds a bounded-kernel hypothesis explicitly, and c=0 uses flux cancellation rather than coincident tilted roots.

- [ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20](ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md)
