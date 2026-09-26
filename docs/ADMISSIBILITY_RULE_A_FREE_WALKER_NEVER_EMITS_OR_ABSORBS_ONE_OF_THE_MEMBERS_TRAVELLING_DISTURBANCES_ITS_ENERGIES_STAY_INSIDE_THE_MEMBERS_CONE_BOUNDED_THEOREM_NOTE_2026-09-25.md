---
claim_id: admissibility_rule_a_free_walker_never_emits_or_absorbs_one_of_the_members_travelling_disturbances_its_energies_stay_inside_the_members_cone_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Same-band kinematic inequality for supplied E_mu(k)=sqrt(mu\xB2+sum sin\xB2 k) and omega(q)=sqrt(sum\
  \ 4sin\xB2(q/2)), for real mu and q nonzero modulo 2pi. Differences within either fixed-sign band are strictly\
  \ below omega. With separately supplied single-quantum energy omega and conserved lattice momentum this excludes\
  \ same-band one-quantum emission/absorption only. Interband transitions can be kinematically resonant. Selected\
  \ transverse tensor modes have this frequency at alpha=K/4; no full mode count at degenerate coefficients, universal\
  \ stability, finite-k speed ordering or coupling/quantization derivation follows."
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- minimal_axioms
runner: scripts/admissibility_rule_a_free_walker_never_emits_or_absorbs_one_of_the_members_travelling_disturbances_its_energies_stay_inside_the_members_cone_2026_09_25.py
---

# Strict same-band energy differences for two supplied lattice dispersions

**Type:** bounded_theorem
**Status:** exact conditional kinematics; unaudited.

## Premises and declared objects

Let `s_j(k)=sin k_j`, `p_j(q)=2sin(q_j/2)`, `E_mu(k)=sqrt(mu²+|s(k)|²)` with real mu, and `omega(q)=|p(q)|`. Momenta are real three-vectors modulo 2pi. Choose one fixed sign of the walker energy band; initial and final energies are both +E_mu or both -E_mu.

The current tensor parent supplies a staggered quadratic action. Its transverse trace-free subspace has `h p=0`, `tr h=0`, `R1=0`, `R2=-p² tr(h²)/4`. The restricted action is `alpha tr(hdot²)-Kp² tr(h²)/4`, yielding `omega²=Kp²/(4alpha)` for K,alpha>0. At alpha=K/4 it gives the frequency above. This proves the selected tensor solutions; the parent's full determinant degenerates at beta=-alpha and does not alone count every mode or resolve all constraints. The kinetic normalization is supplied.

To interpret frequency as the energy of one emitted/absorbed quantum, additionally supply that quantum excitation and its energy omega, with units fixed accordingly, as well as translation-invariant momentum-conserving coupling and on-shell free-particle kinematics. A classical wave's energy is not fixed by its frequency alone. Neither quantization nor a complete source transfer/coupling follows here.

## Theorem T1 — strict massless same-band bound

For all k and q not congruent to zero,

`||s(k)|-|s(k-q)|| < |p(q)|`.

Componentwise `s_j(k)-s_j(k-q)=2cos(k_j-q_j/2)sin(q_j/2)`. Thus the vector difference has norm at most |p|; the difference of norms is no larger. If the first inequality saturates, every nonzero p_j requires cos(k_j-q_j/2)=±1, so the two sine components there are nonzero and opposite. Hence neither vector is zero. Saturation of the reverse triangle inequality would require the two vectors to be nonnegative collinear, impossible on such a component. Since at least one p_j is nonzero, the combined inequality is strict. At q=0 equality holds and is excluded. The 32768 rational configurations in the runner illustrate the identity; the saturation argument proves its full domain.

## Theorem T2 — massive and fixed negative bands

For a,b>=0, `|sqrt(mu²+a²)-sqrt(mu²+b²)|<=|a-b|`: the map has derivative a/sqrt(mu²+a²) between zero and one for mu nonzero, with mu=0 immediate. Equivalently squaring follows from `(mu²+a²)(mu²+b²)-(mu²+ab)²=mu²(a-b)²>=0`. Combine with T1. The same absolute difference applies when both energies carry a minus sign. For the staggered mass, momentum transfer can include Q=(pi,pi,pi); E_mu(k-Q)=E_mu(k), so this transfer does not change the bound.

## Theorem T3 — bounded emission conclusion and interband counterroute

Under the separately supplied one-quantum and conservation assumptions, a same-band transition would need an energy difference of magnitude omega(q), which T1/T2 forbid for nonzero q. This is a kinematic result only. Interband transitions are outside it: for massless k=(pi/4,0,0), q=(pi/2,0,0), the energy drop from +E(k) to -E(k-q) is sqrt(2)=omega(q). For mu=1, k=0 and q=(pi,0,0), the interband drop is 2=omega(q). Occupation blocking and matrix elements may forbid particular transitions dynamically, but energy-momentum conservation alone does not. No all-scale stability claim follows, and multi-quantum or multi-particle channels remain separate.

Two-particle scattering is also outside the one-particle theorem. With continuous axial momenta, incoming walkers pi/2 and -pi/2 have total energy2. Outgoing walkers a and pi/3 plus a quantum q=-a-pi/3 conserve momentum. Their energy equals2 at the unique a in(0,pi/6) solving f(a)=sin a+sqrt(3)/2+2sin((a+pi/3)/2)-2=0: f(0)=sqrt(3)/2-1<0, f(pi/6)=sqrt(3)/2+sqrt(2)-3/2>0 and f'(a)=cos a+cos((a+pi/3)/2)>0 throughout. This is a kinematic witness under supplied additive free energies, not a nonzero scattering amplitude or rate; a finite grid need not contain the root. Claims in draft probes about actual amplitudes are not adopted here.

If the comparator quantum instead has frequency |sin q| on an axis, k=q=pi/2 gives a same-band energy difference of one equal to that frequency. This shows why the stipulated half-angle frequency matters.

## Theorem T4 — small positive axial momentum

As q tends to zero from above, `sin q-2sin(q/2)=-q³/8+O(q^5)`. This compares the displayed positive frequencies near a node. Finite-momentum phase or group-speed ordering does not follow: near axial k=pi, the positive massless walker band has one-sided group-speed magnitude approaching one, while the half-angle wave's group speed approaches zero. The word cone in the historical identifier is not a derived causal cone.

## Theorem T5 — continuous-momentum pair kinematics

For massless opposite bands define F(k,q)=|s(k)|+|s(k+q)|. The symmetric choice k=-q/2 gives F=2|s(q/2)|=omega(q) for every q. This uses continuous momenta; a finite torus need not contain the half-momentum. For nonzero q, F(0,q)=|s(q)|<omega(q). At k_j=pi/2-q_j/2, F=2|cos(q/2)|, whose squared excess over omega² is 4 sum_j cos q_j. Thus sum cos q_j>0 also supplies an explicit continuous path crossing of the target energy. This is a sufficient open region, not a necessary condition for resonance. With mass mu, pair energies are at least 2|mu|, so omega<2|mu| excludes this pair channel. At or above threshold no exclusion follows from that bound. Occupied initial and unoccupied final states, a nonzero coupling matrix element and the supplied quantum energy remain necessary for actual absorption; no rate is derived.

## No-Go Discipline Gate

- **N1:** one fixed-sign band, nonzero q, the displayed free dispersions and an explicitly supplied single-quantum channel.
- **N2:** no repository no-go wall is a premise.
- **N3:** mode, normalization, quantization/energy conversion and coupling are supplied.
- **N4:** current tensor-parent degeneracies and source-placement limits remain in force.
- **N5:** exact identities and finite controls; no interacting spectral or dynamical stability proof.
- **N6:** coupling matrix elements, band occupancy and full constrained evolution remain open.
- **N7:** interband resonances, additional particles/quanta and altered dispersions are counterroutes.
- **N8:** retain strict intraband kinematics; no universal emission or stability no-go.

## Verification and recovery

Original source and campaign remain at PR #9242 head 35f84904e550d36d280a0239ca774090c308b696. Fresh controls include the interband resonances and restricted tensor frequency. No audit verdict is applied.

This note proves only same-band kinematics for supplied dispersions and a supplied single-quantum channel; interband resonances remain possible; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Inputs

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25](ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
