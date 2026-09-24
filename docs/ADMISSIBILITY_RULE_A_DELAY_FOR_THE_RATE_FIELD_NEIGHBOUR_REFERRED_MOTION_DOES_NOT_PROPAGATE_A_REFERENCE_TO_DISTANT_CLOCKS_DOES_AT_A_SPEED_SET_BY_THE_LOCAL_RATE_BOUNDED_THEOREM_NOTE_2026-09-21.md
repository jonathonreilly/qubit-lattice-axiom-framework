---
claim_id: admissibility_rule_a_delay_for_the_rate_field_neighbour_referred_motion_does_not_propagate_a_reference_to_distant_clocks_does_at_a_speed_set_by_the_local_rate_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Within supplied differentiable rate actions with exact time-reparameterization invariance: symmetric quadratic kinetic matrices annihilate the uniform velocity and have scaling degree minus one. On a separately specified reduced zero-mean weak-field model, nearest-neighbour covariance makes kinetic and potential operators proportional, with flat oscillator dispersion; positive regular finite-range kinetic symbols do not yield an acoustic branch against the fixed nondegenerate averaging potential. A reference-clock or master-parameter model instead has the continuous-time lattice-wave dispersion with long-wavelength speed c*wbar, not a strict signal cone. A leapfrog numerical cone is a separate discrete-time property. The uniform master-mode solution has an initial-rate factor absent from the original claim. No complete invariant positive-energy closed theory or physical delay rule is established."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_delay_for_the_rate_field_neighbour_referred_motion_does_not_propagate_a_reference_to_distant_clocks_does_2026_09_21.py
---

# Rate-action covariance, reduced oscillator dispersion, and the distinction between lattice waves and numerical cones

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (supplied mathematical models; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger; it reports which motions of the rate field survive an arbitrary change of the time parameter and whether they carry a delay; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Exact covariance restricts the kinetic form of rates. A particular reduced nearest-neighbour model has a flat frequency band and an instantaneous spatial inverse in its forced response. This is not a general ban on propagation by every finite-range model. Reference-clock and master-parameter models give a lattice-wave dispersion; its long-wavelength speed is distinct from the exact cone of a chosen numerical recursion. The original uniform-mode formula is corrected for a general initial rate.

## Premises and declared objects

Let w_x=exp(u_x)>0 and v_x=dotu_x. Under t'=f(t), f'>0, set w'=w/f' and v'=(v-f''/f')/f'. Supply a differentiable Lagrangian depending only on rates and their first derivatives, and require exact invariance of L dt, not merely equality up to a total derivative. A canonical amplitude chi is unchanged by this relabeling and obeys the separately supplied equation i dotchi=H_w chi, with H_w homogeneous of degree one in rates.

For quadratic rate kinetics take K=one-half v^T M(w)v with symmetric M, and a potential ledger F+E of weight one. For weak-field calculations set w=wbar exp(u), wbar>0. Let Lambda=-Delta_lat be the nearest-neighbour difference operator with symbol E(k)=sum_j(2-2cos k_j). Couplings gamma,kappa,c are positive. Distinguish a projected periodic zero-mean model from fixed-rate walls and from a master parameter. These are different supplied variational settings.

Named mathematical imports: Lagrange equations, symbols of finite-range difference operators, positive grounded graph inverses, and the leapfrog recursion with its Courant stability condition. None is a framework premise or empirical input.

## Theorem T1 — exact kinetic covariance

At an instant f' and f'' can vary independently. Setting f'=1 shifts every v_x by the same number, so exact invariance requires dependence on velocity differences only. Constant rescaling additionally requires L(a w,a v)=a L(w,v), a>0. Conversely these two properties give the transformation law for arbitrary instantaneous f',f''.

For the symmetric quadratic form this means M(w)1=0, M(a w)=a^-1 M(w), and a potential of degree one. Expanding K(v+b1)-K(v) proves the kernel condition. The onsite form diag(1/w) fails it, although it satisfies constant-rescaling covariance. The bond-difference form with weights1/sqrt(w_x w_y), the reference-site difference form, and the weighted-mean-referred form satisfy it. The last matrix is D-D11^T D/(1^T D1), D=diag(1/w); it is generally not local.

There is a variational constraint as well as a covariance identity. If every rate, including the common mode, is varied in a closed invariant action, sum_x partial K/partial v_x=0 and sum_x partial(K-F-E)/partial u_x=-(K+F+E). Summing the field equations therefore requires the total ledger to vanish. A nontrivial positive ledger cannot satisfy this unconstrained closed system. The reduced fixed-mean model below removes that variation by an explicit constraint; it must not be described as a complete unconstrained invariant theory.

## Theorem T2 — the specified reduced neighbour model

At a uniform background, a constant-coefficient symmetric nearest-neighbour covariant matrix with M1=0 is a multiple of Lambda: the six neighbour coefficients agree and the row sum fixes the onsite coefficient. For K=(kappa/(2wbar))dotu^T Lambda dotu and V=(wbar/(2gamma))u^T Lambda u, the reduced zero-mean equation is

`Lambda[(kappa/wbar)ddotu+(wbar/gamma)u]=-P_0 s`.

On that subspace each unforced mode has omega_0=wbar/sqrt(gamma*kappa). With zero initial data the forced solution is -(gamma/wbar)Lambda^+P_0 applied to the convolution of s with omega_0 sin(omega_0 t). A fixed source switched on at zero gives (1-cos(omega_0 t))u_static. The nonlocal response is the prescribed inverse Lambda^+, and the free reduced oscillators have no spatial dispersion. Nonzero initial data add their own homogeneous oscillations.

For a regular symmetric finite-range kinetic symbol M(k) vanishing at zero, M(k)=O(|k|^2). If it is positive for punctured small k and the fixed potential symbol is nondegenerate positive order |k|^2, V/M cannot tend to zero. It may approach a nonzero value or diverge; singular directions require separate treatment. This excludes an acoustic branch in that class, not every propagating wave packet: a nonconstant gapped dispersion can transport a packet. It also does not cover a different potential, nonlocal or singular kinetic symbols, higher time derivatives, or other fields.

For positive bond-difference weights with fixed walls, the instantaneous grounded kinetic inverse is entrywise positive by the connected graph maximum principle. This algebraic inverse statement alone is not a full nonlinear well-posedness or signaling theorem.

## Theorem T3 — reference clocks and lattice-wave dispersion

With a wall reference, K_ref=(1/(2gamma*c^2))sum_x[dot(u_x-u_ref)]^2/w_x is invariant when the reference transforms too. In the gauge of held wall clocks dotu_ref=0, put psi=w^-1/2. Then K_ref=(2/(gamma*c^2))sum dotpsi^2 and the field equation is

`ddotpsi_x=gamma*c^2/(2psi_x) * (partial F/partial u_x+e_x)`.

Together with the supplied canonical chi dynamics it conserves E+F+K_ref when boundary work vanishes. Linearizing the selected quadratic field energy gives ddotu=c^2*wbar^2 Delta_lat u-gamma*c^2*wbar e on the grounded interior. A mean-referred periodic model instead projects the source and has a different common-mode constraint. One must not insert mean subtraction into the wall equation without specifying that additional model change.

The uniform-background dispersion is omega^2=c^2*wbar^2 E(k), with long-wavelength speed c*wbar. A continuous-time lattice wave generally has arbitrarily small tails at arbitrarily distant sites for nonzero time; it has no exact finite support cone. A slowly varying source approaches a quasistatic response only in a specified frequency regime away from resonances and with appropriate initial/transient treatment; a speed comparison alone is insufficient.

For the separate leapfrog update, compactly supported forcing expands its numerical support by at most one bond per step. That cone speed is1/h sites per time, where h is the chosen step. At c*wbar*h=1/2 it is2*c*wbar, not c*wbar. In d dimensions stability requires d*(c*wbar*h)^2<=1. The exact numerical zeros therefore do not prove a physical propagation boundary. Reported half-rise times are empirical features of specified simulations.

## Theorem T4 — a uniform master-parameter model

The onsite kinetic form can instead be supplied in a fixed master parameter. Suppose a spatially uniform sector is preserved, its static energy at unit rate is a constant S, the number of sites is N, and its rate is w=psi^-2. Then ddotpsi=a/psi^3, a=gamma*c^2*S/(2N). From rest with psi(0)=psi_0>0 the solution is

`psi(t)^2=psi_0^2+(a/psi_0^2)t^2`.

Differentiation proves the formula. The originally stated psi_0^2+a*t^2 is correct only at psi_0=1. For a>0 this solution slows the common rate; nonuniform energy density need not preserve the uniform ansatz, and a negative S would change the conclusion. The absence of common kinetic momentum in T1 does not by itself produce a consistent positive closed unconstrained dynamics, as its constraint above shows.

## Theorem T5 — a separate field unchanged by relabeling

Let q be unchanged by t->f(t), and supply L_q=one-half sum dotq_x^2/w_x -(c_q^2/2)sum_bonds sqrt(w_x w_y)(q_x-q_y)^2. Since dotq'=dotq/f', both action terms are invariant with only nearest-neighbour spatial couplings. At constant uniform rate the equation is ddotq=c_q^2*wbar^2 Delta_lat q, with the same dispersion/tail qualification as T3. For varying w the equation has additional terms, including dotw/w in the kinetic derivative; no constant-rate equation is asserted there. This establishes an allowed mathematical model, not a unique physical carrier.

## No-Go Discipline Gate

### N1 — Alternatives
Nonlocal references, a fixed master parameter, other fields, different potential symbols and higher-time-derivative actions lie outside individual subclaims. Lack of an acoustic branch does not rule out all propagation.

### N2 — Wall independence
No repository no-go wall is assumed. Grounded and periodic constraints are explicit mathematical boundary data.

### N3 — Hidden assumptions
The covariance statement is exact action-density invariance. The positive reduced model fixes the common-rate variation. The master uniform solution needs a preserved uniform source sector and fixed S. A discrete integration cone is not a continuous-time lattice cone.

### N4 — Dependencies
Companion notes supply the selected rate energy and canonical chi equation. Their corrected scopes are used. The axioms do not choose a time parameter, these fields, or their equations.

### N5 — Resolution
per_element: executed — rational transformation of four kinetic forms, bond energy and an invariant non-rate field; matrix row sums.
per_site: executed — finite reduced inverse response and the separate leapfrog numerical support cone with start-from-rest forcing.
per_mode: executed — rational symbol samples for flat, gapped and lattice-wave dispersions; numerical stability bound.
per_block: executed — nearest-neighbour coefficient constraints, uniform kinetic identities and the corrected arbitrary-initial-rate solution.
lattice_wide: stated covariance and dispersion proofs only; nonlinear well-posedness, a strict physical front and a complete invariant positive closed theory remain unproved.

### N6 — Partial closure and primitives
No primitive fixes c or supplies the model. None is newly registered.

### N7 — Strongest objection
The original text equated the numerical cone with wave speed and suppressed the initial-rate factor in T4. Both are corrected. Its no-wave reading is restricted to the exact flat-band reduced model and the separately stated acoustic-branch obstruction.

### N8 — Historical scope
The original coupled walker simulations and half-rise measurements remain author reports. They do not prove exact causal support or global nonlinear dynamics.

## Original-source disposition

PR #8578 at `621c0c56378574c17622f21ebd69e9294639909b` on `physics-loop/admissibility-induced-law-block57-a-delay-for-the-rate-field-nearest-neighbour-kinetic-terms-do-not-propagate-20260921` preserves all original simulations, outputs and campaign history. These are deferred, not fresh canonical evidence. Useful T1–T5 identities remain with the distinctions and corrected formula above. No global physical no-delay theorem is asserted.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Canonical amplitude scope](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Ledger identities](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Grounded quadratic field](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Verification

Run `python3 scripts/admissibility_rule_a_delay_for_the_rate_field_neighbour_referred_motion_does_not_propagate_a_reference_to_distant_clocks_does_2026_09_21.py`. Review is not an audit verdict.
