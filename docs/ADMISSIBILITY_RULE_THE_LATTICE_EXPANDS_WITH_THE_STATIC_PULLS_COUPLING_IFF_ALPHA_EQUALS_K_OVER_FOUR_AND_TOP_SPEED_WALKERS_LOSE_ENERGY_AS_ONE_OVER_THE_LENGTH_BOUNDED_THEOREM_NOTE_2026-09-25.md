---
claim_id: admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied homogeneous scalar action c_k ell^3 lambdadot\xB2/w-w m(lambda), with positive alpha,K, beta=-alpha\
  \ and c_k=-24alpha. Its constraint and length equation give the stated density/pressure relations and normalized\
  \ expansion/contraction branches. Matching its coefficient to the separately supplied static inverse-distance coupling\
  \ holds iff alpha=K/4 for nonzero density. Uniform massless hopping H(k)/ell gives exact comoving energy scaling\
  \ and scalar dilation pressure. This does not establish nonlinear zero-mode solvability of the full lattice source-field\
  \ equations or force every closed lattice to expand."
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_blindness_to_coin_rotations_that_vary_in_time_leaves_exactly_block_62s_two_kinetic_numbers_and_no_ratio_makes_a_transverse_relabelling_in_time_a_symmetry_bounded_theorem_note_2026-09-24
- admissibility_rule_block_60s_declared_numbers_unit_free_speeds_force_s_equals_p_plus_two_positive_content_forces_the_kinetic_sign_bounded_theorem_note_2026-09-24
- admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
- admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
- minimal_axioms
runner: scripts/admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_2026_09_25.py
---

# Conditional homogeneous motion and massless hopping under uniform dilation

**Type:** bounded_theorem
**Status:** supplied homogeneous model and exact identities; unaudited.

## Model and boundary

Supply `L=c_k exp(3lambda) lambdadot²/w-w m(lambda)` per site, ell=exp(lambda)>0, and fix w=1 after varying it. Assume alpha,K>0, beta=-alpha and c_k=12alpha+36beta=-24alpha. The coefficient follows by inserting the infinitesimal dilation `hdot=2 lambdadot I` in the specified quadratic kinetic form. Extending that quadratic form to the finite homogeneous action with volume exponent 3 is a supplied ansatz, not a derived nonlinear completion.

For the linearized periodic constraint `K R1=e`, summing spatial derivatives gives mean(e)=0. That excludes nonzero nonnegative content in this static linearized setting. The selected bilinear static model has a related restriction. Neither proves that every closed lattice with content must expand, nor that the homogeneous ansatz solves the full nonuniform, shear and momentum constraints. The previously open full zero-mode compatibility remains open.

## Theorem T1 — the scalar constraint

Rate variation yields `m=-c_k ell³ lambdadot²`; hence `lambdadot²=rho/(24alpha)`, rho=m/ell³. The length equation is `c_k ell³(2 lambdaddot+3 lambdadot²)+m'=0`. Differentiating the rate constraint equals minus lambdadot times this equation. For a smooth strictly positive m(lambda), this provides local expanding and contracting solutions on intervals of positive ell. Arbitrary signed or nonsmooth content is not covered by the existence statement.

## Theorem T2 — coefficient matching

The separately supplied nonzero-mode static law `u=-e/(4Kp²)`, with its infinite-space inverse-Laplacian kernel, defines `G=1/(16pi K)`. This is a coefficient comparison, not an inverse of the zero mode on a closed torus. For rho>0, `rho/(24alpha)=(8pi G/3)rho` iff alpha=K/4. At zero density that comparison cannot select alpha.

Define scalar dilation pressure by `m'=-3p ell³`. Combining the length equation and constraint gives `ell_ddot/ell=-(rho+3p)/(48alpha)`, or `-(4pi G/3)(rho+3p)` at the matching coefficient. It is a conditional identity. Equating the two coefficients is an additional matching demand, not an axiom-based selection mechanism.

## Theorem T3 — fixed comoving massless modes

Under the supplied uniform hopping rule the massless symbol is `H(k)/ell(t)`, with eigenvalues `±sqrt(sum_a sin² k_a)/ell(t)`. These Hamiltonians commute at different times. A fixed comoving momentum eigenstate thus retains its band populations and its energy scales by 1/ell. The physical reciprocal scale changes as k/ell; k itself is the lattice/comoving label. Finite lattice massless modes need not travel at the maximal group speed.

For positive massless-band energy per site `m=epsilon/ell`, scalar dilation pressure is rho/3. This scalar is one third of the stress trace, not a proof of isotropic stress for an arbitrary directional occupation. For epsilon>0 and ell(0)=1 the expanding branch is `ell=(1+t/t1)^(1/2)`, `t1=sqrt(6alpha/epsilon)`. For rest content m0>0 it is `ell=(1+t/t0)^(2/3)`, `t0=(4/3)sqrt(6alpha/m0)`. Contracting branches follow by reversing t, on intervals where the bracket stays positive. The zero-length endpoint is excluded. For m=m0+epsilon/ell only the massless part contributes to this scalar pressure.

The identities follow by substituting the two displayed ell functions into the constraint and length equation, and differentiating m with respect to lambda. Massive time-dependent band evolution and anisotropic stress backreaction are separate open problems; no exact massive adiabatic-following claim is made here.

## No-Go Discipline Gate

- **N1:** restricted smooth homogeneous scalar action, positive parameters/content and positive-length intervals.
- **N2:** no repository no-go wall is a premise.
- **N3:** nonlinear homogeneous completion, volume law, hopping and source law are supplied.
- **N4:** actual corrected parent scopes apply; coefficient matching is conditional.
- **N5:** runner checks algebra, scalar constraint preservation and both power-law forms, not the full lattice evolution.
- **N6:** shear, nonuniform modes, all source constraints and consistency of a nonlinear completion remain open.
- **N7:** other nonlinear terms sharing the same quadratic action can change finite homogeneous evolution.
- **N8:** this is a partial scalar calculation, not closure of the deferred full zero-mode task.

## Verification and recovery

Original source and campaign are retained at PR #9237 head 600adb94e5c416c79467b5c2f5f806619c2c92b7. The primary runner checks the displayed supplied-model identities. No audit verdict or physical cosmology identification is applied.

This note studies only the supplied homogeneous scalar action and uniform hopping rule; full nonlinear source-field compatibility remains open; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Inputs

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [ADMISSIBILITY_RULE_BLOCK_60S_DECLARED_NUMBERS_UNIT_FREE_SPEEDS_FORCE_S_EQUALS_P_PLUS_TWO_POSITIVE_CONTENT_FORCES_THE_KINETIC_SIGN_BOUNDED_THEOREM_NOTE_2026-09-24](ADMISSIBILITY_RULE_BLOCK_60S_DECLARED_NUMBERS_UNIT_FREE_SPEEDS_FORCE_S_EQUALS_P_PLUS_TWO_POSITIVE_CONTENT_FORCES_THE_KINETIC_SIGN_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25](ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [ADMISSIBILITY_RULE_BLINDNESS_TO_COIN_ROTATIONS_THAT_VARY_IN_TIME_LEAVES_EXACTLY_BLOCK_62S_TWO_KINETIC_NUMBERS_AND_NO_RATIO_MAKES_A_TRANSVERSE_RELABELLING_IN_TIME_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-24](ADMISSIBILITY_RULE_BLINDNESS_TO_COIN_ROTATIONS_THAT_VARY_IN_TIME_LEAVES_EXACTLY_BLOCK_62S_TWO_KINETIC_NUMBERS_AND_NO_RATIO_MAKES_A_TRANSVERSE_RELABELLING_IN_TIME_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23](ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md)
