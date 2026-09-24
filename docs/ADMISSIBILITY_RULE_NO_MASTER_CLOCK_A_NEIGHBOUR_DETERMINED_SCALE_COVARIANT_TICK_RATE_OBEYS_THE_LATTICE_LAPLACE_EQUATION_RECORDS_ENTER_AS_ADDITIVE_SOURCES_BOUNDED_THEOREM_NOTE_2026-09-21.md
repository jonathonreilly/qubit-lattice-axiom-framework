---
claim_id: admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Within supplied positive local rates and a differentiable, cubic-covariant, degree-one neighbour rule normalized on uniform fields: the first-order equation in log rates is neighbour averaging. Exact source superposition is restricted to the independently selected log-linear equation with fixed source strengths. On a connected finite torus this equation is solvable only for zero-sum sources; subtracting a source mean is an additional background prescription. A single symmetric departure-timed walker has finite-volume stationary weights proportional to inverse rate and zero local expected displacement. No unique nonlinear law, population equilibrium, acceleration, or physical clock identification is derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_no_master_clock_neighbour_determined_scale_covariant_tick_rate_lattice_laplace_equation_additive_sources_2026_09_21.py
---

# Local rate covariance: linearization, conditional source superposition, and waiting-time weights

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (supplied mathematical model; unaudited)

This note works within a supplied clause for local tick rates; it reports what field equation, what zero mode and what kind of source the clause forces; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Covariance and degree-one homogeneity fix the derivative of a normalized neighbour rule at a uniform field. They do not fix its nonlinear completion or how records source it. Exact additivity below is a property of a selected linear equation. Slow departure clocks increase stationary residence weights on a finite graph; they do not create a local velocity directed towards slow clocks. This incorporates the author's 2026-09-23 correction.

## Premises and declared objects

Let w_x>0 and u_x=log(w_x) on the cubic lattice. The supplied rule w_x=F(w_neighbours) has six arguments, is differentiable at positive uniform fields, is invariant under the 24 proper cubic rotations, satisfies F(t v)=t F(v) for t>0, and F(1,...,1)=1. Thus F(c,...,c)=c. Global scaling covariance is an added hypothesis; silence about time in the axioms does not prove it.

The optional record law uses fixed strengths s_x=(log kappa)n_x in the selected equation L u=s, L=I-A with A the six-neighbour average. Neither fixed kappa nor the additive identification n_x follows from homogeneity alone. A finite torus is connected, with L>=3 for the displayed examples. On the infinite three-dimensional lattice use finitely supported sources and a field tending to zero at infinity. A single test walker jumps along each incident cubic bond at w_x/6; there is no exclusion, formation, or interaction in this test process.

Named mathematical imports: Euler's identity for differentiable homogeneous functions, the kernel of a connected graph Laplacian, Green functions with specified boundary conditions, and detailed balance for finite Markov chains. All uses are proved or defined below; these are not empirical inputs.

## Theorem T1 — covariant linear equations

Write c_0 u_x+sum_e c_e u_(x+e)=s_x. The 24 rotations act transitively on the six neighbours, so all c_e=c_1. Invariance under u->u+a requires c_0+6c_1=0. Hence the equation is c_0 L u=s. To obtain a nonzero operator require c_0!=0; the zero equation is also formally covariant. The runner independently builds the rotation constraints and finds a one-dimensional fixed space for the neighbour coefficients.

## Theorem T2 — linearization and nonlinear freedom

At the uniform point rotation symmetry makes all six derivatives of F equal. Differentiating F(t,...,t)=t makes their sum one, so each is 1/6. Since a first variation of log w at a uniform field is the relative first variation of w, the linearized equation is L(delta u)=0.

For the power mean of order p, two neighbouring inputs 1+d and 1-d with the other four equal to one give 1+(p-1)d^2/6+O(d^4). At d=1/10 the arithmetic, harmonic, contraharmonic, and pair-ratio means in the runner give changes 0, -1/298, 1/300, -1/1500 respectively. Thus the common first derivative does not force the second order. The geometric mean gives u_x=A u exactly, by the logarithm of a product. The product of six rates has degree six and is outside the class. On the side-four symbol sample its linearization has range [-5,7], while I-A is nonnegative with its only zero at uniform wave vector.

## Theorem T3 — solvability is not a background prescription

The quadratic form of I-A is a positive multiple of the sum of squared bond differences. On a connected finite torus its kernel is exactly the constants and its range consists exactly of zero-sum sources. It therefore has rank L^3-1. A nonzero-total source has no solution; it is not automatically projected by the equation. One may separately prescribe a compensating uniform background and solve L u=s-mean(s), with mean(u)=0. The runner checks rank26 on the side-three torus, both solvability cases, and the freedom to add a constant.

For finitely supported sources on the infinite three-dimensional lattice, the usual decaying inverse gives a solution. Its existence and boundary choice are part of this infinite-volume formulation; the finite runner does not establish its long-distance asymptotics.

## Theorem T4 — exact superposition in the selected log-linear model

An absolute pin w_x=U with U fixed fails covariance under w->t w. A relative clause w_x=kappa F(neighbours) is covariant, but its logarithm is generally nonlinear. Exact L u=(log kappa)n requires choosing the geometric mean (or stating this log-linear law directly), and treating kappa and the source counts as fixed inputs. A generic homogeneous rule gives this form only to first order near a uniform solution with small log kappa. Contact-dependent strengths can change the source map and invalidate superposition as a function of the record arrangement.

For the selected linear model with fixed sources and a fixed boundary/background prescription, linearity gives exact superposition and the symmetric inverse gives reciprocal pair potentials. On the side-four torus the runner uses a zero-mean background and log kappa=-3/10: three fixed sources add exactly; the single-source value at its source is -4551/12800. For a single negative source with the stated decaying or grounded boundary, the maximum principle gives a negative field, lowest at the source. This is a potential identity, not a dynamical force law or a rule for the statistical distribution of records.

## Theorem T5 — finite stationary weights without local drift

On a connected finite periodic lattice, pi_x=(1/w_x)/sum_y(1/w_y) satisfies pi_x w_x/6=pi_y w_y/6 across every bond. It is therefore the unique stationary law of this positive-rate finite process. But its local expected displacement per unit time is sum_e e w_x/6=0. The probability current across a bond is (p_x w_x-p_y w_y)/6; spatially varying residence times and evolving probability flux must not be confused with a drift of an individual walker. Symmetric bond-timed rates instead have uniform stationary weights.

On the infinite lattice, 1/w is only a reversible measure unless its sum is finite. In the decaying-source model w tends to a positive constant, so it is not a normalizable stationary probability. No limiting-distribution or equilibrium assertion for a growing population follows from this single-walker result.

## No-Go Discipline Gate

### N1 — Alternative routes
Non-differentiable rules, longer-range rules, different record source laws, and an absolute clock lie outside T2's hypotheses. A finite-range shift-invariant operator need not have a nonzero quadratic symbol: the square of the averaging operator is an explicit fourth-order counterexample. Consequently no universal long-range law follows from shift symmetry alone. These are scope boundaries, not exclusions of other physics.

### N2 — Wall independence
No repository no-go wall is used. The restrictions are the explicitly supplied mathematical hypotheses.

### N3 — Hidden assumptions
T4 needs the log-linear choice and fixed source strengths. Finite-volume source compensation is added, and T5 needs a finite connected state space for its probability statement. Rates are static inputs to T5.

### N4 — Dependencies
The minimal axioms supply the lattice and named symmetry context only. The finite-window rule is background for the rejected degree-six rate analogy. The companion record-source note motivates using n_x but does not derive this rate equation.

### N5 — Resolution
per_element: executed — 24 rotations and their fixed coefficient space; exact dual-number derivatives of four homogeneous rules.
per_site: executed — absolute versus relative pins; finite inverse-rate balance and zero conditional displacement.
per_mode: executed — finite symbol values for the averaging and degree-six product linearizations; no general asymptotic certificate.
per_block: executed — side-three solvability and side-four fixed-source superposition with reciprocal pair potentials.
lattice_wide: analytic proofs at the stated linear/differentiable scopes; nonlinear completion, record statistics and physical clock interpretation remain supplied or open.

### N6 — Partial closure and primitives
The registered primitives do not supply this clock rule or kappa. No new premise is proposed or registered.

### N7 — Strongest objection
Covariance alone does not produce the exact source equation. Agreed: T2 is first order, while T4 explicitly selects a log-linear completion. A stationary residence bias does not imply acceleration or local drift; T5 makes the distinction explicit.

### N8 — Historical scope
The original campaign linked these results to a supplied weak-field packet and compared capture models. Those comparisons do not establish a physical source, a force law, or a unique nonlinear completion.

## Falsifiers and boundaries
A normalized differentiable homogeneous covariant rule with a different first derivative would refute T2. A failure of zero-sum solvability or fixed-source superposition would refute T3 or T4 in their stated settings. Failure of detailed balance for the stated finite departure-timed process would refute T5. No measured finite-box fit or simulation tolerance is promoted to a general theorem.

## Original-source disposition

All original source is recoverable from PR #8568 at `c4e6a23f6c24c7f5de6d94bedbd749458452c604` on `physics-loop/admissibility-induced-law-block53-no-master-clock-forces-the-lattice-laplace-equation-20260921`. Historical refuter programs, finite-box fits, simulation output and campaign records are deferred and preserved there; they are not freshly executed evidence for this canonical review. The original T1–T5 arguments survive with the scope corrections above. The false drift wording and unconditional source-additivity inference are withdrawn.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Finite-window rule](ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md)
- [Record-source scope](ADMISSIBILITY_RULE_WHAT_A_SOURCE_IS_WHEN_RECORDS_MOVE_ONE_MASS_PER_RECORD_NO_ACTION_ACROSS_EMPTY_SPACE_SCREENED_DENSITY_POTENTIAL_SIGNED_TILT_CHANNEL_BOUNDED_THEOREM_NOTE_2026-09-20.md)

## Verification

Run `python3 scripts/admissibility_rule_no_master_clock_neighbour_determined_scale_covariant_tick_rate_lattice_laplace_equation_additive_sources_2026_09_21.py`. This canonical runner checks the finite identities stated above; review is not a formal audit verdict.
