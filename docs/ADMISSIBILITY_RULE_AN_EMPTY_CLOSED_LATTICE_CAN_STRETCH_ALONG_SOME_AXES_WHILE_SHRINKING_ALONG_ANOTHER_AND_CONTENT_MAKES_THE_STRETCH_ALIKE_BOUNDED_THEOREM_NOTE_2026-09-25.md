---
claim_id: admissibility_rule_an_empty_closed_lattice_can_stretch_along_some_axes_while_shrinking_along_another_and_content_makes_the_stretch_alike_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied nonlinear diagonal homogeneous action -8alpha exp(sum lambda) sum_(i<j) lambdadot_i lambdadot_j/w-w\
  \ m with alpha positive. Vacuum power laws satisfy sum p=sum p\xB2=1, while static solutions are also allowed.\
  \ The stated constant positive rest-content family obeys the constraint on its integration-constant cone and has\
  \ late expanding-branch rates t lambdadot_i tending to 2/3. Length ratios need not tend to one. This is not full\
  \ nonlinear lattice solvability, all-content isotropization or derivation of the finite action from its quadratic\
  \ coefficients."
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_bounded_theorem_note_2026-09-25
- admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_and_the_delays_speed_depends_on_direction_bounded_theorem_note_2026-09-21
- minimal_axioms
runner: scripts/admissibility_rule_an_empty_closed_lattice_can_stretch_along_some_axes_while_shrinking_along_another_and_content_makes_the_stretch_alike_2026_09_25.py
---

# Conditional diagonal homogeneous solutions and late expansion rates

**Type:** bounded_theorem
**Status:** supplied finite homogeneous action; unaudited.

## Premises and declared objects

Set ell_i=exp(lambda_i)>0, V=ell_1 ell_2 ell_3, alpha>0, and supply `L=-8alpha V sum_(i<j) lambdadot_i lambdadot_j/w-w m`. Vary w before setting w=1. The volume factor and nonlinear extension to arbitrary lambda are supplied. Quadratic kinetic coefficients in current parent notes do not fix this full action. No consistency with all off-diagonal, nonuniform, source or momentum constraints is established here.

## Theorem T1 — coefficient comparison

Inserting the infinitesimal diagonal rates `hdot=2 diag(lambdadot_i)` into `alpha tr(hdot²)+beta(tr hdot)²` yields `4(alpha+beta)sum lambdadot_i²+8beta sum_(i<j)lambdadot_i lambdadot_j`. Thus beta=-alpha gives the stated cross coefficient; equal rates give -24alpha lambdadot². This is an exact quadratic algebraic identity, not a finite-field completion theorem.

The supplied action gives `8alpha V sum_(i<j) lambdadot_i lambdadot_j=m`. For constant rest content m=m0, using this constraint in each length equation gives `d/dt[8alpha V(S-lambdadot_k)]=m0`, S=sum lambdadot_i.

## Theorem T2 — vacuum solutions

For m=0 and t>0, take ell_i=C_i t^(p_i) with positive constants C_i. If sum p_i=sum p_i²=1, the constraint and all three length equations vanish: V is proportional to t, the cross sum is zero, and V(S-lambdadot_k) is constant. An explicit rational family is `(-u,1+u,u(1+u))/(1+u+u²)`, u>0, with axis permutations. If all p_i were positive the cross sum could not vanish. Endpoints such as (1,0,0) are allowed. Constant positive lengths also solve the vacuum equations. Equal rates in a vacuum require the common rate to vanish; this excludes nontrivial isotropic motion within this model, not static geometry. No classification of all lattice evolutions is claimed.

## Theorem T3 — constant rest content

Let m0>0, real D_k, D=sum D_k and

`V=(3m0 t²/2+D t)/(16alpha)`, `S=Vdot/V`, `lambdadot_k=S-(m0 t+D_k)/(8alpha V)`.

Require `sum D_k²=2sum_(i<j)D_i D_j`. On any interval with V>0, the rates sum to S and obey all three length equations. Substitution gives constraint residual `-[sum D_k²-2sum_(i<j)D_i D_j]/[t(2D+3m0t)]`, hence zero. Integrating the rates gives positive ell_k; choose their initial product to be V so it remains V. The finite-volume zeros are excluded.

On the late expanding branch t>max(0,-2D/(3m0)), `t lambdadot_k -> 2/3`. Rate differences are `(D_j-D_i)/(8alpha V)=O(t^-2)`, whereas the common leading rate is 2/(3t). Thus `ell_k=C_k t^(2/3)(1+O(t^-1))` with positive constants C_k. Their ratios can approach unequal constants: expansion-rate anisotropy decays, not every geometric length difference. The other exterior positive-volume interval t<min(0,-2D/(3m0)) has t lambdadot_k -> 2/3 as t -> -infinity and ell_k=C_k |t|^(2/3)(1+O(|t|^-1)). Under simultaneous t -> -t and D_k -> -D_k the volume is unchanged and every rate changes sign; the equations select no time direction. Negative/signed content, direction-dependent stresses and other source laws are not covered. A prescribed constant rest energy does not represent all moving matter.

## No-Go Discipline Gate

- **N1:** supplied diagonal homogeneous action; positive alpha and lengths, with positive constant rest content in T3.
- **N2:** no repository no-go wall is a premise.
- **N3:** volume law and finite nonlinear kinetic extension are supplied.
- **N4:** quadratic parent classifications do not supply omitted nonlinear equations.
- **N5:** exact scalar substitutions and limits, not full source-field evolution.
- **N6:** off-diagonal, inhomogeneous and source compatibility remain open.
- **N7:** static vacuum, contracting branches, unequal limiting length ratios and anisotropic stresses prevent broader conclusions.
- **N8:** retain the explicit families; no universal matter-isotropization or physical geometry claim.

## Verification and recovery

Original source and campaign remain at PR #9241 head e594fcd0c24c00b0de7fe7355aa8f889268df57a. The independent control derives volume and anisotropy equations in different coordinates. No audit verdict is applied.

This note studies an explicitly supplied diagonal homogeneous action; the nonlinear lattice completion remains open; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Inputs

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_WITH_THE_STATIC_PULLS_COUPLING_IFF_ALPHA_EQUALS_K_OVER_FOUR_AND_TOP_SPEED_WALKERS_LOSE_ENERGY_AS_ONE_OVER_THE_LENGTH_BOUNDED_THEOREM_NOTE_2026-09-25](ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_WITH_THE_STATIC_PULLS_COUPLING_IFF_ALPHA_EQUALS_K_OVER_FOUR_AND_TOP_SPEED_WALKERS_LOSE_ENERGY_AS_ONE_OVER_THE_LENGTH_BOUNDED_THEOREM_NOTE_2026-09-25.md)
- [ADMISSIBILITY_RULE_THREE_LENGTHS_PER_SITE_A_BODY_AT_REST_STRETCHES_THEM_ALIKE_HOP_ENERGY_DRIVES_WHOLE_COLUMNS_AND_THE_DELAYS_SPEED_DEPENDS_ON_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-21](ADMISSIBILITY_RULE_THREE_LENGTHS_PER_SITE_A_BODY_AT_REST_STRETCHES_THEM_ALIKE_HOP_ENERGY_DRIVES_WHOLE_COLUMNS_AND_THE_DELAYS_SPEED_DEPENDS_ON_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-21.md)
