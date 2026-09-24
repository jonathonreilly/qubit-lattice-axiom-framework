---
claim_id: admissibility_rule_record_layer_fields_arrive_by_diffusion_establishment_time_grows_as_the_square_of_the_range_transit_halo_and_massless_odds_field_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "Conditional discrete walk model W=I+h Delta with 0<h<=1/6. The displayed low-frequency torus mode obeys a quadratic-in-size relaxation lower bound, but an even torus at h=1/6 also has an undamped alternating mode. Independent-walk kernels have exact mean-square reach 6hs and the stated second-moment tail bound. The odds-map derivative is algebraically 6lambda1 times a simple walk; a killed-walk interpretation needs 0<=6lambda1<=1. Sequential removal with 0<hm\u00b2<1 gives effective squared static mass m\u00b2/(1-hm\u00b2), and a mode lower bound under hE<=1, not a general relaxation or exact range theorem. Continuous-time exclusion has a differential mean equation, not exact discrete Euler sampling. The units corollary assumes tick=a/c separately and concerns a specified emitted-mass tail criterion, not physical force establishment."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_record_layer_fields_arrive_by_diffusion_establishment_time_square_of_the_range_2026_09_20.py
---

# Walk-kernel tail bounds and low-frequency relaxation bounds for supplied record-layer updates

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** bounded-support (exact; about fields defined under supplied readings; nothing adopted or registered; unaudited)

This note analyzes supplied walk updates associated with the record-layer fields of blocks 39 to 42; its tail and mode bounds do not prove general settling, and it adopts nothing.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Conditional discrete walk model W=I+h Delta with 0<h<=1/6. The displayed low-frequency torus mode obeys a quadratic-in-size relaxation lower bound, but an even torus at h=1/6 also has an undamped alternating mode. Independent-walk kernels have exact mean-square reach 6hs and the stated second-moment tail bound. The odds-map derivative is algebraically 6lambda1 times a simple walk; a killed-walk interpretation needs 0<=6lambda1<=1. Sequential removal with 0<hm²<1 gives effective squared static mass m²/(1-hm²), and a mode lower bound under hE<=1, not a general relaxation or exact range theorem. Continuous-time exclusion has a differential mean equation, not exact discrete Euler sampling. The units corollary assumes tick=a/c separately and concerns a specified emitted-mass tail criterion, not physical force establishment.

Original empirical-number comparisons are preserved on the frozen PR branch; no physical value or time scale is needed for these identities.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "owner, 2026-09-20: 'keep going until we have something solid or need to probe a different direction'; the gravity lane's open item on main: a local conservation/attachment law, including cadence, consumed by the same carrier"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the record layer's fields are shown to settle by diffusion, a fourth and carrier-level reason (after content charge, mass term, non-additive sources) that they cannot be the long-range field; next a reading pass over what the repository has for propagation in the amplitude layer, and the lead that content is a direction of travel (records with inertia); no source link is proposed before that"
conditional_surface_status: "T1-T4 exact; the corollary is conditional on the tick being one lattice unit at the limiting speed; the numbers in the Result are comparators"
hypothetical_axiom_status: "the readings of blocks 39 to 42 under which the two fields are defined; hypotheses only"
admitted_observation_status: "comparators only: the Earth-Sun distance, the age of the universe and the speed of light are used once, to illustrate the corollary's inequality; no theorem depends on them"
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." (the transit field has no removal term, hence no mass term) and through the sentence on the probability distribution quoted in block 42. Block 01 (on `main`, proposed and unaudited) supplies the rule. Blocks 41 and 42 (open PRs #8547, #8548) supply the two fields; both are restated here and their runners' relevant parts are repeated in this note's runner. The registered `scale_reference_primitive` (a conversion of units; it asserts no value of the lattice unit) and `kinetic_isotropy_primitive` (the tick grained on the same footing as the edge) are the only registered primitives the corollary touches.

- **Walk operator.** `W = 1 + hΔ_lat`, `0 < 6h ≤ 1`: a walker hops to each neighbour with probability `h` and stays with probability `1 − 6h`. `E(k) = 6 − 2Σcos k_i`.
- **Transit field** (block 41, T5): continuous-time symmetric transit gives du/dt=kappa Delta u+j(t). The supplied discrete linear update u_(t+1)=W u_t+j is a separate walk model (or an explicit time discretization), not its exact finite-time sampling; continuous-time sampling uses exp(kappa Delta t).
- **Odds field** (block 42, T2): the departure of the odds of unformed sites from the uniform ones, linearized, obeys `δ_x ← Σ_{y∼x} K₁ δ_y`; its vector part is multiplied by `λ₁` per neighbour.
- **Mass term.** Removal with probability `hm²` per tick before the step: `u_{t+1} = (1 − hm²) W u_t + j`; effective squared mass mu²=m²/(1-hm²), for 0<hm²<1; its small-wavevector length parameter is sqrt(1-hm²)/m.

A reach growing as the square root of the time is the law of the walk of Brown and of the diffusion of Fick; the second-moment tail bound is that of Markov and Chebyshev; `(1 − x)ⁿ ≥ 1 − nx` is the inequality of Bernoulli. The lattice unit is often taken to be the length of Planck; the registered primitive does not say so and this note does not either. None is used as authority.

## Prior art and what is new

That a walk reaches the square root of the time is classical. What is new is its place in the campaign: the identification of one walk operator behind both record-layer fields (T3 ties block 42's odds map to it by exact differentiation), the half-life bound in exact rational form, the statement that a mass term cannot buy speed without giving up range, and the units corollary stated with the lattice unit left free, as the registered primitive requires.

## Exact target and obligation graph

Target: how long the record layer's fields take to be set up over a distance. Obligations: (O1) the modes of a torus; (O2) the kernel on the infinite lattice; (O3) that the odds field is driven by the same operator; (O4) the effect of a mass term. T1–T4 discharge them.

## Theorem T1 — a lower bound for a nonzero low-frequency mode

`Δ_lat` multiplies the wave `cos(k·x)` by `−E(k)`, so `W` multiplies it by `1 − hE(k)`, and after `n` ticks the distance of that mode from its static value is `(1 − hE(k))ⁿ` times what it was. For `0 ≤ x ≤ 1`, `(1 − x)ⁿ ≥ 1 − nx`, which is at least `1/2` while `n ≤ 1/(2x)`. The slowest mode has `E_min = 2(1 − cos(2π/L)) ≤ (2π/L)²`. For L>=2, hE_min<=1. Hence for every `n ≤ 1/(2hE_min)`, and in particular for every `n ≤ L²/(8π²h)`, at least half of the slowest mode's deviation remains. ∎

On an even torus at h=1/6 the alternating mode has eigenvalue -1 and never relaxes. A static forced field also requires a compatible zero mode. T1 is a lower bound for the displayed nonzero mode, not a guarantee that every initial field settles.

## Theorem T2 — on the infinite lattice the reach is the square root of the time

Let `p_s` be the `s`-tick kernel of the walk. (a) `Σ_x p_s(x) = 1`, and `p_s(x) = 0` when `x` is more than `s` steps away, since a tick moves a walker by at most one step. (b) The steps are independent with mean zero and mean-square length `6h`, so `Σ_x |x|² p_s(x) = 6hs` exactly. (c) Therefore `Σ_{|x| ≥ R} p_s(x) ≤ 6hs/R²`. (d) With a source switched on at tick `0`, `u_t = Σ_{s<t} W^s j`, the sum of the kernels; of everything a point source has emitted up to tick `t`, the share beyond `R` is at most `6ht/R²`. For a share `f` to lie beyond `R`, at least `fR²/(6h) ≥ fR²` ticks must pass. ∎

## Theorem T3 — the odds field is driven by the same walk

Differentiating block 42's map `Φ(π)_x(s) ∝ Π_{y∼x} Σ_b ω(s,b)π_y(b)` at the uniform field, a departure `e_z(b)/2` of one neighbour's odds (a unit lean along `z`) changes the odds at `x` by `λ₁ e_z(s)/2` and induces no lean along the other axes. One linearized iteration is therefore `v_x ← λ₁ Σ_{y∼x} v_y = 6λ₁ · (1/6)Σ_{y∼x} v_y`: a step of the simple walk (`h = 1/6`) weighted by `6λ₁`, which is a removal with probability 1-6lambda1 only when 0<=6lambda1<=1 and nothing at all on the surface `5p = 7q + 4r`. The exact derivative gives the lean `1/6` at `(3,1,2)` and `3/23` at `(5,2,4)`. ∎

## Theorem T4 — a mass term buys speed only by giving up range

With the mass term the factor of the mode `k` per tick is `(1 − hm²)(1 − hE(k)) = 1 − x` with `x ≤ h(m² + E(k))`. For modes satisfying E(k)<=m² and hE(k)<=1, this is at most `2hm²`, and by the inequality of T1 at least half of their deviation remains for every `n ≤ 1/(4hm²)`. The static denominator is h[m²+(1-hm²)E], so its small-wavevector length parameter is ell=sqrt(1-hm²)/m, not exactly 1/m. The proved lower bound is 1/(4hm²)=(ell²+h)/(4h). This is a lower bound for the specified modes, not a general matching upper bound or exact lattice decay length. ∎

## Corollary — units, with a separately supplied tick conversion

Let a tick be the time `a/c` in which the limiting speed `c` covers one lattice unit `a`. A distance `R` is `R/a` steps and a time `T` is `cT/a` ticks. By T2(d) with `f = 1/2` and `6h ≤ 1`, half of what a source has emitted can lie beyond `R` within `T` only if `cT/a ≥ (R/a)²/2`, that is `a ≥ R²/(2cT)`. The equality tick=a/c is an extra model assumption, not a primitive-derived dynamical law. The framework does not fix `a`; the inequality says how coarse the lattice would have to be for a walk to have carried a field that far.

## No-Go Discipline Gate

The note's negative sentence is that the record-layer fields of blocks 41 and 42 cannot be set up over a distance `R` in fewer than of the order of `R²` ticks.

### N1 — Routes by which the sentence could fail
1. *A carrier that is not a walk* — a field propagated by the amplitude layer's dynamics, or by records that remember their direction of travel, is outside the two fields treated here. Nothing is claimed about it.
2. *The law already in place* — a static law that is long-range from the start needs no setting up; but bodies move, and the field of a body that has moved has to be set up again, by the same operator.
3. *Non-reversible transit* — a transit with a drift carries a field at the drift speed along the drift, not in all directions; an isotropic field still spreads as the square root of the time.
4. *The nonlinear map* — T3 is about the linearization; the executed iteration counts of block 42's control (successive ratios close to those of the squares of the sides, on the massless surface) show the same law in the full map, and are not claimed.
5. *A coarse lattice* — the corollary is an inequality on `a`, not a value.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the readings of blocks 39 to 42, declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | permanence of records (no removal term); the sentence behind the odds reading | yes (premise) |
| block 01 (`main`) | the rule | yes (premise, proposed) |
| blocks 41, 42 (open PRs #8547, #8548) | the two fields | yes (restated; the runner repeats the relevant exact computations) |
| `scale_reference_primitive`, `kinetic_isotropy_primitive` | the corollary's units | registered primitives; the first asserts no value of `a` |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "both record-layer fields are driven by one walk operator and settle in a number of ticks of the order of the square of the distance" | executed: the lean induced by a unit lean at a neighbour, exact differentiation, two triples | executed: waves under one tick at sample sites; the response to a switched-on source against the sum of the kernels at every site reached in 12 ticks | executed: `1 − hE(k)` for four wavevectors, two sides, two hop probabilities; the slowest mode's half-life bound | executed: exact path counts for 0 to 12 ticks (weight, light cone, mean-square reach, tail shares) | T1 on every torus; T2 on the infinite lattice for every number of ticks; T3 for every positive triple; T4 for 0<hm²<1 and modes with hE<=1 |

### N6 — Partial-closure paths and primitive scan
The registered primitives give no carrier with a speed for a record-layer field. Supplying one (a clause under which records keep their direction of travel, or a field carried by the amplitude layer) is not attempted here.

### N7 — Steelman
Hostile reviewer: "Equilibrium laws are not set up by anything; the correlations are simply there." Reply: for a law that holds from the start, yes, and N1 route 2 says so. But the use these fields were examined for is a field between bodies that move, and the field of a body that has moved is set up by the dynamics; for the two fields at hand that dynamics is the walk. The note claims nothing about other carriers.

### N8 — Cross-cycle echo
Blocks 13, 26, 34 and 35 found heat kernels in level time for the formation reading's two-point functions; block 41's halo and block 42's iteration counts are the same law in the moving-records reading.

## Falsifiers

- A torus and a mode whose deviation falls below half in fewer than `1/(2hE(k))` ticks.
- A number of ticks `s` and a distance `R` with more than the share `6hs/R²` of the kernel beyond `R`.
- A positive triple at which one linearized iteration of block 42's odds map is not `6λ₁` times a step of the simple walk.

## Boundaries and non-claims

Nothing is said about the amplitude layer, about records with a memory of their direction of travel, or about any carrier whose dynamics is not the reversible walk above. No value of the lattice unit is asserted. The numbers in the Result are comparators. No gravitational statement is made; the results constrain the supplied linear updates.

## Imports
- `minimal_axioms`: the sentences quoted under Premises. Block 01 (on `main`): the rule; proposed, unaudited. Blocks 41, 42 (PRs #8547, #8548, open): restated. Blocks 13, 26, 34, 35 as evidence addresses.
- Named standard imports at definition level: independence of the steps of a walk; the second-moment tail bound; `(1 − x)ⁿ ≥ 1 − nx`; `1 − cos θ ≤ θ²/2`; a rational lower bound for `π²`.
- Reference only: Brown and Fick for the law of diffusion; Markov and Chebyshev for the tail bound; Bernoulli for the inequality; Planck for the customary lattice unit, which the registered primitive does not assert.

## Review record — original author provenance
Supervisor-run block (owner 2026-09-20: "keep going until we have something solid or need to probe a different direction"). Lens: while reading the gravity lane's notes on `main` in full for the source link, the supervisor noticed that block 42's control had already measured iteration counts in the ratio of the squares of the sides, and that block 41's halo is a heat kernel: whatever else is repaired, both fields arrive by a walk. Refuting pass (`specs/supervisor_control_block43_refuter.py`, machinery disjoint from the runner's): W1 all `6^s` paths of the simple walk, `s ≤ 7`; W2 the lazy walk by enumeration of weighted paths; W3 the slowest mode of the `6³` torus stepped on all 216 sites (half-lives 4 and 8 ticks against the bounds 3 and 6); W4 the half-life with a mass term. All pass. Mutation census: 8 mutations, each failing in its own family only. The theorem text was re-read against the runner before the gates. Author checks only; no independent review has taken place.

## Current review boundaries and dependencies

The historical simulations and auxiliary refuters remain author reports on original branch head `a6af3f2d571cc23aed9674ab44f999fc55de94a5`; their tables are preserved but are not freshly verified by the canonical runner. No physical propagation, force law, or hydrodynamic limit follows from these finite identities.

- [Companion model](ADMISSIBILITY_RULE_WHAT_A_SOURCE_IS_WHEN_RECORDS_MOVE_ONE_MASS_PER_RECORD_NO_ACTION_ACROSS_EMPTY_SPACE_SCREENED_DENSITY_POTENTIAL_SIGNED_TILT_CHANNEL_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Companion model](ADMISSIBILITY_RULE_INTERACTION_THROUGH_THE_ODDS_OF_UNFORMED_SITES_FIELD_EQUATION_MASSLESS_SURFACE_CONTENT_CHARGE_NO_FIRST_ORDER_MASS_CHANNEL_AT_NEUTRAL_SCALE_BOUNDED_THEOREM_NOTE_2026-09-20.md)
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Finite-window rule](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)

## Verification

```bash
python3 scripts/admissibility_rule_record_layer_fields_arrive_by_diffusion_establishment_time_square_of_the_range_2026_09_20.py
python3 scripts/admissibility_rule_record_layer_fields_arrive_by_diffusion_establishment_time_square_of_the_range_2026_09_20.py --list-mutations
python3 .claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block43_refuter.py
```
