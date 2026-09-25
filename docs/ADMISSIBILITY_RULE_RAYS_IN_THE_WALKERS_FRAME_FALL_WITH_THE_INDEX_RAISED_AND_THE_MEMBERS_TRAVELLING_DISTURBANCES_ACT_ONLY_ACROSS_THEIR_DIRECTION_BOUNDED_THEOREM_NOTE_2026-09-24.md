---
claim_id: admissibility_rule_rays_in_the_walkers_frame_fall_with_the_index_raised_and_the_members_travelling_disturbances_act_only_across_their_direction_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Declared positive-branch local ray dispersion with positive rates, positive-definite inverse metric
  and m>0 for the rest-state derivative. Exact symbol derivatives and conditional same-point axial transverse-acceleration
  ratios; no integrated deflection or packet theorem. First-order massless ray vector field for a supplied axis-three
  transverse trace-free wave at w=1, including bounded momentum turn and sideways displacement for nonzero frequency;
  the accumulated longitudinal displacement need not be bounded. Uniform two-state mass anticommutation is controlled
  by the global span of actual bond coin vectors, not pointwise rank of an arbitrary varying frame. Constant staggered
  mass squares on purely opposite-parity hops on a bipartite lattice. No uniqueness of a rest term or physical wave
  identification.
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
- admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_rays_in_the_walkers_frame_fall_with_the_index_raised_and_the_members_travelling_disturbances_act_only_across_their_direction_2026_09_24.py
---

# Supplied frame rays: local accelerations and first-order response to a transverse wave

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 59, 60, 62 and 77 as landed, in the declared ray limit; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 59, 60, 62 and 77 as landed on main (rays and rates, the curvature member's field, the coin's frame and its disturbances, and the staggered sign), with the ray limit declared; it reports how rays move in a frame, what the member's travelling disturbances do to them, and which rest energy a frame admits; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The supplied local ray dispersion gives the inverse-metric rest-state acceleration. Reading the selected scalar fields as an isotropic frame gives the stated local transverse-acceleration ratios. These compare an axial massless ray and a massive rest state at the same point and local bond speed, with parallel gradients and a nonzero comparison denominator. They are not integrated bending angles.

For the specified wave, an initially axis-one ray has a direct sideways drift and a momentum turn. The displayed v3=0 is the vector field evaluated at exactly axial momentum; the induced k3 changes v3 at first order during evolution. Its displacement can contain a secular term. A ray initially along axis3 has no first-order forcing from this transverse trace-free perturbation.

A uniform mass anticommutes only when its coin vector is orthogonal to every actual bond coin vector. For a constant frame this means rank at most2; for varying frames the global bond span matters. A staggered mass is one separately supplied construction for bipartite hopping, not a unique possible rest term.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "No possibility is privileged." No coin axis carries a preferred rest energy.
  - "No site is privileged." The staggered sign breaks one-site translation, as block 77 as landed notes.
  - "Admissibility is not a dynamics axiom." The frame, the rates and the ray limit are supplied. Nothing is adopted.
- **The symbol** (blocks 59 and 62 as landed). The massive ray dispersion is separately supplied; a uniform two-state on-site mass need not realize it in a rank-three frame. For uniform fields, `E² = a²m² + w²g^{ij} sin k_i sin k_j` with `g^{ij} = Σ_aE_a^iE_a^j`. Here `a` times the rest energy and `w` times the hops.
- **The ray limit, declared.** A slowly varying packet follows `ẋ = ∂E/∂k` and `k̇ = −∂E/∂x` for the local symbol. Corrections of the next order in gradients are not included. The landed blocks 59 and 60 read their ray statements as local same-point comparisons, and so does this note.
- **The member's disturbances** (block 62 T4 as landed). Transverse traceless `h`, with `p_ih_ij = 0` and `h_ii = 0`, and `g^{ij} = δ − h` at first order.
- **Block 60's fields** (as landed). Weak field `ℓ = w̄/w`; strong field `ℓ = χ²` and `w = N/χ`, with far fields `χ ≈ 1 + Qg` and `N ≈ 1 − Pg`.
- **The staggered sign** (block 77 as landed): `ε = (−1)^{x₁+x₂+x₃}`, supplied.
- **Comparators, named only:** the ray equations as Hamilton's equations; the anomalous (Berry) velocity at the next order; the transverse action of the comparator's waves on light; the Shapiro-type delay.

## Theorem T1 — the fall with the index raised

*Statement.* Take the positive branch, a,w,m>0 and positive-definite g inverse. For `E` as above, with `a`, `w` and the six `g^{ij}` general functions of position:
- `v_i = ∂E/∂k_i = w²g^{ij} sin k_j cos k_i/E` exactly;
- a slow body at `k = 0` accelerates as `dv_i/dt = −(w²/a)g^{il}∂_l a`.

*Proof.* Differentiate. At `k = 0`, `∂v_i/∂k_l = w²g^{il}/(am)` and `k̇_l = −m∂_l a`, while `ẋ = 0`. ∎

*Checked (B1).* Symbolically, with general functions.

## Theorem T2 — block 60's field read as a frame

*Statement.*
- (a) Block 60's weak field is the frame `(1/ℓ)·1` with `ℓ = w̄/w`. With the rest energy timed by `a = w`, the light speed is `c = w/ℓ = w²/w̄`, so `d log c/d log a = 2` exactly: the specified local axial-ray transverse acceleration divided by the massive rest-state acceleration is2, when both are evaluated at the same local c with parallel gradients and nonzero denominator. This is not a deflection-angle comparison.
- (b) In block 60's strong field, `log c = −(P + 3Q)g` and `log a = −(P + Q)g` at first order far away, so the same local far-field comparison has ratio(P+3Q)/(P+Q), provided P+Q!=0 and the leading comparison gradient is nonzero.

*Proof.* Substitute. ∎

*Checked (C1).* Both, symbolically.

## Theorem T3 — first-order response of initially axial rays

*Statement.* Set w=1,m=0, Omega>0 and work to first order at fixed elapsed time. Take `h = (A₊(e₁e₁ − e₂e₂) + A_×(e₁e₂ + e₂e₁)) cos(qx₃ − Ωt)`, a transverse traceless disturbance travelling along axis 3. At first order in `h`:
- (a) Evaluating the instantaneous ray vector field at exactly k=(pi/3,0,0) gives:
  - `v₁ = cos k (1 − h₁₁/2)`, a delay;
  - `v₂ = −h₁₂`, a sideways drift;
  - `v₃ = 0`;
  - `k̇₂ = 0`;
  - `k̇₃ = (sin k/2) ∂₃h₁₁`, a turn towards the gradient of `h₁₁`;
- (b) along the unperturbed ray at `x₃ = z₀` the drift integrates to `−A_×(sin qz₀ − sin(qz₀ − ΩT))/Ω`, bounded by `2|A_×|/Ω`; the delay and the turn are bounded oscillations in the same way;
- (c) a ray along axis 3, the disturbance's direction, feels nothing at first order.

*Proof.* Expand `E = √(g^{ij} sin k_i sin k_j)` to first order in `h`.
- At `k ∥ e_j` only the row `g^{j·}` meets `sin k_j`.
- For a disturbance along axis 3, `h_{i3} = 0`, so a ray along axis 3 sees no first-order change.

∎

*Checked (D1).* The six ray quantities along axis 1, the six along axis 3, and the drift integral, symbolically.

## Theorem T4 — which rest energy a frame admits

*Statement.*
- (a) For a nonzero uniform Hermitian mass, `M = m₀ + m·σ` anticommutes with all three `σ_a` only if `M = 0`. Since `{σ₁, E·σ} = 2E₁`, a uniform mass m sigma_c anticommutes iff every actual bond coin vector is perpendicular to axis c. For a constant nonaliasing frame this requires rank at most2 and is sufficient for some mass direction. For a varying symmetrized frame the vectors are the bond averages (E^j(x)+E^j(y))/2; their global span must have rank at most2. Pointwise rank is neither the correct sufficient condition nor, with cancellations, a necessary one.
- (b) For constant real m, no other on-site terms, and a bipartite lattice (even tori or the infinite lattice), the staggered sign anticommutes with every opposite-parity frame hop, and `(H + mε)² = H² + m²`.

*Proof.*
- (a) `{M, σ_b} = 2m₀σ_b + 2m_b`.
- (b) Every hop of `½Σ_j{E^j(x)·σ, S_j}` joins sites of opposite parity, whatever the frame field.

∎

*Checked (E1).*
- (a) symbolically.
- (b) exactly on the `4³` torus, with a varying integer frame field and the symmetrised bond hops: the anticommutator, the square, and hermiticity.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 62 as landed: rays in a frame and the action of its travelling disturbances on rays are not stated; blocks 59-60 as landed: ray statements are local same-point comparisons"
source_of_blocker_text: blocks 59, 60 and 62 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a packet control in floating point (labelled); the next-order (anomalous) velocity in a frame; second order in h for rays co-moving with the disturbance"
conditional_surface_status: "T1-T3 in the declared ray limit, T3 at first order in h; T4 exact on every even torus; frame, rates and disturbances supplied"
hypothetical_axiom_status: "the frame, rates, disturbances and ray limit are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 59: rays and the fall in isotropic lengths (T4), and lengths as pure numbers.
  - Block 60: the member's weak and strong fields.
  - Block 62: the frame (T1) and the transverse traceless disturbances (T4).
  - Block 77: the staggered sign and `(K + mε)² = K² + m²`.
- **The probes attempt.** `rays-in-a-frame` a2 (Claude Opus 5.5, issue #8815) found T1–T4. A Grok referee confirmed it (#8994).
- **In the literature.**
  - The ray equations as Hamilton's equations.
  - The anomalous (Berry) velocity.
  - The transverse action of the comparator's waves on light, and the Shapiro-type delay.

  All reference only.
- **New here:**
  - an independent exact runner;
  - T3's statement that the member's travelling disturbances act on rays only across their direction;
  - T4 placed against block 77.

## Exact target and obligation graph

Target: rays in a frame, and the action of the member's travelling disturbances on them. The obligations are:
- (O1) the fall (T1);
- (O2) block 60's field (T2);
- (O3) the disturbances (T3);
- (O4) the rest energy (T4).

T1–T4 discharge them. Open: packet controls and higher orders.

## No-Go Discipline Gate

The note's negative sentences:
- a ray along a travelling disturbance's direction feels nothing at first order;
- a nonzero uniform anticommuting mass is excluded when the actual bond coin vectors span three dimensions.

### N1 — Routes by which the sentence could fail or mislead
1. *Second order.* A ray co-moving with the disturbance at its speed could accumulate a second-order effect. That is not treated.
2. *The ray limit.* It is declared. Corrections of the next order in gradients are not included.
3. *Lattice placement.* Block 62 places `h` on sites and faces. At leading order in gradients this is its value at the ray.
4. *Other rest energies.* Non-anticommuting on-site terms, terms that are not on-site, and spatially varying terms are outside T4(a). The staggered term is one of them.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied frame, rates, disturbances and ray limit.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 59, 60, 62, 77 (landed) | rays; the fields; the frame and disturbances; the staggered sign | yes (restated) |
| probes (#8815; Grok-refereed #8994) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "local inverse-metric acceleration; conditional first-order axial-ray response; a supplied staggered mass anticommutes with bipartite hopping" | executed: velocity and fall with general functions | executed: block 60's fields as frames | executed: rays along and across a travelling disturbance; the drift | executed: the anticommutations; the `4³` frame field | ray limit declared; first order in `h`; T4 exact |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used, and nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A ray along the disturbance feeling nothing is just the transversality of `h`."
  - *Reply:* Yes, and that is the content: the member's disturbances carry no longitudinal part (block 62 T4). This is only the supplied symbol calculation. General ray directions and higher-order effects are not classified.

### N8 — Cross-cycle echo
- Blocks 59 and 60 compared bending and falling.
- Block 62 found the disturbances.
- This note finds how the disturbances act on rays.

## Falsifiers

- A frame in which the slow-body fall does not raise its index with `g^{il}`.
- A first-order effect on a ray along a transverse traceless disturbance's direction.
- A uniform on-site rest energy anticommuting with all three coin matrices.

## Boundaries and non-claims

- The frame, rates, disturbances and ray limit are supplied.
- No packet control is run.
- No gravitational claim is made.

## Imports

- [Supplied source, block 59](ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 60](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 62](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 77](ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 59, 60, 62 and 77, restated.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - Hamilton's equations for the ray limit;
  - first-order expansion;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-ninth since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#8815). A Grok referee confirmed them (#8994).
  - The supervisor re-checked them with its own runner.
- **Before writing.**
  - Main was re-fetched, and blocks 59, 60, 62 and 77 were read as landed.
  - The own-prior-art check found blocks 98 and 110 on rays in the member's static fields. The travelling disturbances were not treated there.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_rays_in_the_walkers_frame_fall_with_the_index_raised_and_the_members_travelling_disturbances_act_only_across_their_direction_2026_09_24.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
