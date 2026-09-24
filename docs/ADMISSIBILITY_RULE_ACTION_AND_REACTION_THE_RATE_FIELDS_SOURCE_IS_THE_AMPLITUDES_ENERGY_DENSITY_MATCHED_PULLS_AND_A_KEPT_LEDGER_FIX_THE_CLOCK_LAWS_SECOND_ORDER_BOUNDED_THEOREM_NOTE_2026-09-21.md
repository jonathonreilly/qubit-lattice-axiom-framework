---
claim_id: admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied canonical evolution i dotchi=H_w(t) chi, H_w=phi H phi, phi=exp(u/2), and a differentiable field energy F: the derivative of amplitude energy is its local energy density and a stated constrained variational equation is sufficient for ledger conservation. It is not necessary merely from conservation along one motion. Reciprocal point-force algebra is a separate supplied weak-field model. Homogeneous symmetric bond energies give a local source-free square-root averaging law through second order under zero-multiplier variations; this is distinct from a closed constrained lattice, whose multiplier is total ledger/N, not mean amplitude energy. No physical source or exact packet force is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_2026_09_21.py
---

# Clocked energy derivatives, sufficient ledger conservation, and conditional reciprocal forces

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (supplied mathematical models; unaudited)

This note works within supplied clauses for local tick rates and canonical amplitudes; it proves energy-derivative identities and a sufficient variational conservation law, with a separately supplied reciprocal point-force model; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The local energy derivative and the rate of change of the total ledger are exact identities for the chosen canonical dynamics. A variational field equation keeps that ledger; conservation alone does not uniquely force this equation. The periodic constraint and a source-free local equation with held exterior values have different multipliers and must not be interchanged. No universal packet-force result is imported from the companion amplitude note.

## Premises and declared objects

On a finite lattice let H be any fixed Hermitian matrix, phi_x=exp(u_x/2)>0, H_w=phi H phi, and let i dotchi=H_w(t)chi be the supplied canonical equation. Write E=chi^dagger H_w chi and e_x=Re[chi_x^dagger(H_w chi)_x], with the internal components summed. For several walkers sum these expressions. F[u] is a differentiable field energy and L=E+F the ledger.

When rates depend on time, this canonical equation is an extra choice: transforming a receiving-site equation i dotpsi=W H psi by chi=W^-1/2 psi also produces -(i/2)dotu chi. The present equation omits that term by hypothesis, not by a fixed-rate similarity argument.

For the periodic variational model impose sum_x u_x constant. Separately, the local source-free model fixes neighbours/exterior and uses unconstrained interior variations with multiplier zero. For the bond-energy analysis assume a sum of identical symmetric nearest-neighbour bond functions, homogeneous of degree one in the two endpoint rates; this ansatz is narrower than every possible local energy functional.

Named mathematical imports: differentiation of a quadratic form, Euler's identity for homogeneous functions, constrained stationarity, and Taylor expansion. The separate point-body model uses the even Green function of a periodic averaging operator and a supplied central-difference force.

## Theorem T1 — the energy derivative

At fixed chi, partial E/partial u_x=e_x and sum_x e_x=E. Each term of E is bilinear in phi. Differentiating an endpoint contributes one half of that term; pairing the two endpoints gives the real local expression, including the correct full derivative of an onsite term. Summing counts each term once. Along the supplied canonical evolution, chi's derivative contributes i< [H_w,H_w] >=0, so dotE=sum_x e_x dotu_x. This last identity is conditional on that evolution, not arbitrary motion of chi.

## Theorem T2 — a sufficient law and the exact defect for another source

With sum u fixed, if partial F/partial u_x=-(e_x-mu), where mu is independent of x, then dotL=mu sum_x dotu_x=0. For a different source s in the same equation, dotL=sum_x(e_x-s_x)dotu_x. These follow by adding dotF to T1.

This is a sufficient condition, not an unconditional necessity: any difference e-s orthogonal to the actual velocity dotu gives the same conservation along that motion. A universal necessity statement would need an independently proved set of accessible velocities and restrictions on the field law.

On the supplied reduced one-dimensional walk H=m sigma_1+sigma_3 D, a real envelope multiplying the positive sigma_1 spinor has e_x=m w_x |chi_x|^2 instantaneously; the hopping contribution has zero real part. This does not prove the envelope is a stationary body. At uniform rate, the stated ring plane wave with k=pi/2 and m=3/4 has energy5/4 per local amplitude norm, rather than3/4. The runner's three-dimensional identity test adds an arbitrary onsite sigma_1 term to a Hermitian generator; it is not a three-dimensional anticommuting mass construction.

## Theorem T3 — reciprocal point-force algebra

Supply point bodies with nonzero energies E_A,E_B, fields -g S_B G_0(x-x_B), and force -E_A times the central difference of the other body's field. Here g is the coupling of this separate point-force model; it is not implicitly the gamma normalization used in T4. On a translation-invariant periodic lattice, G_0 is even and its central difference is odd. Consequently the sum of the two forces is

`g (E_A S_B-E_B S_A) grad_c G_0(x_A-x_B)`.

If the central difference is nonzero at some separation, the pair's force sum vanishes at every separation exactly when S_A/E_A=S_B/E_B. At an individual separation with zero gradient, cancellation imposes no such ratio; on a side-two torus central differences vanish identically. Sources S_A=c E_A give pairwise cancellation for any number of bodies. Other choices can still cancel in particular geometries, so this is not an iff for the total force of every individual many-body configuration. The runner gives a nonzero count-source counterexample on a side-four torus. No field momentum or microscopic quantum force theorem is inferred.

## Theorem T4 — weight one, the multiplier, and local second order

For the specified symmetric bond ansatz, homogeneity gives bond energy sqrt(w_x w_y) f(u_x-u_y) with f even: scale the two rates to geometric mean one and use endpoint interchange. If E and F both have weight one under w->t w, sum_x partial L/partial u_x=L. Thus unconstrained full stationarity would require L=0. A positive ledger has no such stationary point. In the periodic problem constrained by fixed sum u, stationarity instead gives partial F/partial u_x+e_x=mu with mu=L/N.

In particular, mu is (E+F)/N, not E/N. The vector e-mu need not have zero sum. It is the full ledger gradient that is projected by the constraint. The simple mean-subtracted amplitude source is only a leading weak-field approximation when the field energy contributes at higher order.

For F=(2/gamma)sum_bonds(phi_x-phi_y)^2 with gamma>0, partial F/partial u_x=(2/gamma)phi_x sum_y(phi_x-phi_y). At w=wbar exp(delta u), its linear part is (6 wbar/gamma)(delta u_x-average(delta u_neighbours)). Hence the linearized constrained equation is L_avg(delta u)=-(gamma/(6 wbar))(e-mu) at that order.

Now switch to the distinct unconstrained local source-free problem, partial F/partial u_x=0. Uniform fields solve it when f(0)=0. An onsite term c w_x is also homogeneous and local, but spoils that normalized uniform-vacuum condition when c!=0; locality alone does not exclude it. Assume f is even and sufficiently smooth, f(0)=0 and f_2=f''(0)>0. Write d_y=u_x-u_y. Dividing the bond derivative by its positive common factor gives sum_y exp(-d_y/2)[f(d_y)/2+f'(d_y)]=0. To second order this is f_2 sum_y[d_y-d_y^2/4]+O(d^3)=0. It agrees through second order with averaging sqrt(w).

For the symmetric bump u_neighbours=(delta,-delta,0,0,0,0), implicit expansion gives u_x=delta^2/12+((4f_4-f_2)/(576f_2))delta^4+o(delta^4), with f_4 the fourth derivative of f at zero. Fourth order is not universal. For the selected squared-root-difference energy the local equation is exactly phi_x=average(phi_neighbours). This zero-multiplier local result is not the equation at an empty site of a constrained periodic solution with nonzero mu.

## No-Go Discipline Gate

### N1 — Alternative routes
Conservation with other reachable velocities, field energies depending on chi, a dynamical field carrying momentum, other bond ansatzes, zero stiffness, and different constraints are outside the necessity or second-order claims. None is excluded as a physical route.

### N2 — Wall independence
No repository no-go wall is used. The distinct periodic and held-exterior variational problems are explicit mathematical settings.

### N3 — Hidden assumptions
Canonical time-dependent chi dynamics is supplied. T3 is a point-force model, not the former exact packet-force claim. The local expansion needs smoothness, evenness and nonzero f_2.

### N4 — Dependencies
The axioms provide lattice context only. Companion rate and amplitude notes supply definitions with their corrected scopes. The weak-field packet is a comparison target and does not establish this model's source identification.

### N5 — Resolution
per_element: executed — finite clocked energy density and exact quadratic-form derivatives, with a separate algebraic ledger-defect control.
per_site: executed — instantaneous real-envelope identity on a ring and a moving ring eigenstate of energy5/4.
per_mode: executed — local zero-multiplier bump series for two homogeneous bond functions through fourth order.
per_block: executed — side-four reciprocal-force examples and the distinction between total-ledger multiplier and mean amplitude energy.
lattice_wide: analytic energy and conditional variational identities at the stated scopes; no unique physical source, global dynamics, or formation rule is established.

### N6 — Partial closure and primitives
No registered primitive supplies these dynamics, a conserved ledger or a coupling. None is added here.

### N7 — Strongest objection
Conservation is weaker than the full field equation, and the two multipliers were conflated in the original summaries. Both objections are accepted and corrected above. The local second-order identity remains useful without a uniqueness claim about the entire theory.

### N8 — Historical scope
The original coupled two-walker simulations and comparisons to static continuum theories remain historical author work. Their numerical tolerances are not general theorems and are not needed by the finite identities retained here.

## Original-source disposition

PR #8571 at `525c6500c56b178a241a2e17cbf18a46485e57f2` on `physics-loop/admissibility-induced-law-block55-action-and-reaction-the-rate-fields-source-is-the-amplitudes-energy-density-20260921` preserves the original note, auxiliary programs, numerical tables and campaign records. Historical simulations are deferred and not freshly executed in this canonical review. The T1–T4 mathematical arguments are retained with corrected hypotheses and normalization; the unique-source inference and universal packet acceleration corollary are withdrawn.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Rate covariance](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Clocked amplitudes](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Weak-field comparison target](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)

## Verification

Run `python3 scripts/admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_2026_09_21.py`. Review is not a formal audit verdict.
