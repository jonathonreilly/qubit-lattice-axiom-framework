---
claim_id: one_qubit_split_step_walk_relay_source_and_doublers_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Spectral and parity identities for a supplied two-component single-particle split-step walk on Z^3, and a conditional second-moment identity for an auxiliary classical sign distribution and supplied source weights. No framework realization, sequential measurement history or physical fermion identification."
runner: scripts/one_qubit_split_step_walk_relay_source_and_doublers_2026_10_21.py
---

# Two-component split-step walk: conditional source identity and spectral cones

Claim type: bounded_theorem.
Primary runner: `scripts/one_qubit_split_step_walk_relay_source_and_doublers_2026_10_21.py`.

The filename and claim identifier are historical handles. The supplied Hilbert space is l2(Z^3) tensor C^2, a two-component single-particle amplitude field. It is not a demonstrated many-site tensor-product qubit dynamics or a realization of framework admissibility and record processes. In each tick, the sigma_i=+1 and -1 components translate by +i and -i respectively, in fixed axis order x,y,z. Thus S_i(k)=exp(-i k_i sigma_i) and U(k)=S_z S_y S_x. The update and its physical interpretation are supplied, not derived from a candidate-law clause.

## Plane waves and auxiliary source

For a normalized nondegenerate differentiable eigenband Uu=exp(-i eps)u, differentiating the product and applying the eigenphase derivative identity gives d_i eps=<u_before_i|sigma_i|u_before_i>. The factors after substep i cancel in U's expectation, and S_i commutes with sigma_i, so expectations immediately before and after that substep agree. No unique-band derivative is asserted at degeneracies. Five nondegenerate positive-band momenta in the runner give agreement with finite-difference group velocities to 1e-8 or better.

Separately stipulate an auxiliary classical product distribution of three signs with probabilities q_i=(1+<sigma_i>)/2, evaluated on the unmeasured substep states. These signs are not the joint Born statistics of sequential noncommuting measurements: performing a measurement changes the subsequent state. Their independence is an additional supplied rule, not a derived relay or record trajectory.

For a direction D from this distribution, write mu=E[D] and M=E[DD^T]. For an independent redraw D', E[(D'-D)(D'-D)^T]=2(M-mu mu^T). With supplied burn tensor eps M, redraw coefficient r=2eps, and turn tensor -r E[(D'-D)(D'-D)^T]/4, their sum is exactly eps mu mu^T. This identity in fact holds for any normalized direction distribution with an independent redraw; coordinate independence is only the chosen way of matching mu to the substep means. The source weights are not consequences of U alone.

Interpreting r as a probability requires 0<=eps<=1/2. All five samples satisfy this restriction. At k=(1,0,0), the positive eigenphase is eps=1 and r=2, so this probability interpretation does not extend over the full Brillouin zone. Outside the probability domain the same expression is only an algebraic weighted identity. At the five sampled directions with |k| up to .2, eps/|k| is within 3 percent of one; this is a finite diagnostic, not a uniform dispersion bound.

## Exact spectral nodes

Writing c_i=cos(k_i), s_i=sin(k_i), Pauli multiplication gives U=a I-i b.sigma, with

    a = cx cy cz + sx sy sz
    b = (sx cy cz - cx sy sz,
         cx sy cz + sx cy sz,
         cx cy sz - sx sy cz).

The eigenvalues are exp(+-i eps), with cos(eps)=a. To solve U=I, use S_y S_x=S_z inverse. The x and y coefficients require sx cy=0 and cx sy=0. Their simultaneous solutions have x,y both integer multiples of pi, or both odd multiples of pi/2. The remaining coefficients fix z modulo 2pi. In the first case all three coordinates are 0 or pi and the sum is even in units of pi, giving four nodes. In the second case all coordinates are +-pi/2 and sx sy sz=+1, giving four nodes. Linearizing b gives determinant +1 at the integer-pi nodes and -1 at the half-pi nodes. Thus there are exactly eight zero-eigenphase cones, four of each determinant sign. Shifting any one coordinate by pi multiplies U by -1 and pairs them with pi-eigenphase nodes. The runner's 48^3 grid scan is a numerical check of this algebra, not its completeness proof.

These are single-particle spectral cones. Neither fermionic statistics nor physical massless fermions follow. No general statement about which mass perturbations must couple momenta is made; that question requires specified symmetries, degrees of freedom and allowed perturbations.

## Fixed-order and parity limits

The fixed order is not exactly cubic covariant: a proper rotation exchanging two axes and flipping the third changes the sign of the triple-sine term in the trace. Every full-tick displacement has three odd components, so x-y and y-z parities are invariant. The walk therefore preserves four parity sectors at tick boundaries. This is a decomposition of the supplied update, not an identification of physical species.

## Scope

The Hilbert space, update order, Born convention for individual substep expectations, auxiliary product law, independent redraw, source weights, dimensionless momentum/eigenphase conventions, five sample points, scan grid and numerical chirality evaluation are supplied. No empirical comparison, framework-qubit realization, physical matter content, outcome-selection dynamics or exact cubic covariance is established. Independent review and audit authority are separate from this conditional mathematical statement.
