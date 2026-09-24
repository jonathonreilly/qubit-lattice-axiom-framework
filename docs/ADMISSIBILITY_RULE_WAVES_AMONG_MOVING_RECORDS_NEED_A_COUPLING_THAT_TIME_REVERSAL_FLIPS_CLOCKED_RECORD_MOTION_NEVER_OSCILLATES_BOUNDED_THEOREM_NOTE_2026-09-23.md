---
claim_id: admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_clocked_record_motion_never_oscillates_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Finite continuous-time detailed-balance spectra; exact persistent-walk and linear-mode algebra; cubic symmetry tensors without a universal hydrodynamic claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
  - admissibility_rule_three_readings_of_records_form_against_known_physics_the_spacetime_reading_is_two_dimensional_skewed_and_irreversible_bounded_theorem_note_2026-09-23
  - admissibility_rule_records_with_inertia_content_as_direction_of_travel_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_or_emission_bounded_theorem_note_2026-09-20
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_2026_09_23.py
---

# Reversible continuous-time spectra and supplied wave matrices

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
Use a finite continuous-time generator Q with positive stationary pi and detailed balance. The corrected torus clocks of PR8860 are one conditional example. Separate discrete-time direction-memory matrices and linear field equations below are supplied models, not microscopic derivations.

## Theorem T1 — stationary autocorrelations
D^(1/2) Q D^(-1/2), D=diag pi, is real symmetric with nonpositive eigenvalues. For centered real f, <f,exp(tQ)f>_pi=sum c_j exp(lambda_j t), c_j>=0 and lambda_j<=0. Thus this stationary autocorrelation is completely monotone; a reducible chain may retain a constant term. This does not classify sample paths or all cross-correlations. Nonreal generator eigenvalues require failure of this detailed balance, but nonreversibility alone does not guarantee them.
The ring-six fixture verifies balance for two and three records and three timings, up to a common positive rate normalization. A biased single walker has imaginary rate part sqrt(3)/2 at the specified mode.

## Theorem T2 — direction-memory matrices
On a line, retain direction with probability p and reverse otherwise, 0<=p<=1. The characteristic equation is mu²-2p cos(k)mu+2p-1=0. For 0<p<1 the density branch near zero is 1-p k²/[2(1-p)]+O(k⁴). Nonreal multipliers occur precisely when p>1/2 and |sin k|>(1-p)/p; their modulus is sqrt(2p-1). Real negative multipliers can still alternate sign. The endpoints p=0 and p=1 are exceptional, with period-two behavior and free streams respectively.
For six directions with diagonal p and off-diagonal (1-p)/5, inversion Pi gives conjugate M(k)=Pi M(k)Pi. At p=9/10, k=0 the eigenvalues are 1 and22/25 (five times). At (pi/2,0,0) the polynomial has four real and two nonreal roots and exactly one root in(9/10,1). This fixture alone does not identify a branch globally.

## Theorem T3 — conditional algebra and symmetry
The supplied sound equations rho'=-i k.g, g'=-i c²k rho have polynomial mu²(mu²+c²|k|²). The supplied curl pair X'=a i k cross Y, Y'=-b i k cross X has polynomial mu²(mu²+ab|k|²)², with a,b>0. The supplied two-component symbol beta sum sigma_j sin k_j squares to beta² sum sin² k_j I. These identities do not prove that all waves require exactly two conserved quantities or derive any record-gas closure.

The average of the24 proper cubic rotations is zero; their tensor-square average projects onto the scalar rank-two tensor. Thus an analytic scalar symbol invariant under these rotations has no linear k term and has an isotropic quadratic term. Symmetry does not fix that term's magnitude, sign or existence as a hydrodynamic limit. A zero generator is covariant and has no positive diffusion coefficient.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Continuous-time stationary autocorrelations, discrete multipliers and supplied amplitude equations are distinct. Cubic symmetry does not prove diffusion for every rule or forbid arbitrary waves.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The operators, domains, boundary conditions and state assumptions stated above are explicit mathematical hypotheses. They do not add a framework axiom or primitive.

### N4 — Dependencies
The dependencies below identify the actual supplied inputs; earlier stronger conclusions are not imported.

### N5 — Resolution
The canonical runner checks the finite examples and identities stated above using exact arithmetic. General conclusions require the displayed arguments, not extrapolation from samples. Historical simulations are deferred.

### N6 — Primitive boundary
No new primitive, species selection, filling rule or physical interpretation is adopted.

### N7 — Strongest objection
Continuous-time stationary autocorrelations, discrete multipliers and supplied amplitude equations are distinct. Cubic symmetry does not prove diffusion for every rule or forbid arbitrary waves.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8860; no premise adoption or retained grade is inferred.
- [admissibility_rule_three_readings_of_records_form_against_known_physics_the_spacetime_reading_is_two_dimensional_skewed_and_irreversible_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_THREE_READINGS_OF_RECORDS_FORM_AGAINST_KNOWN_PHYSICS_THE_SPACETIME_READING_IS_TWO_DIMENSIONAL_SKEWED_AND_IRREVERSIBLE_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8840; no premise adoption or retained grade is inferred.
- [admissibility_rule_records_with_inertia_content_as_direction_of_travel_conserved_momentum_structureless_equilibrium_sound_speed_forces_need_capture_or_emission_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md): supplied mathematical construction from PR #8550; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8866 head `111143f765d15adac61fa33554fbf8749136754b`, branch `physics-loop/admissibility-induced-law-block96-waves-among-moving-records-need-a-coupling-time-reversal-flips-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
