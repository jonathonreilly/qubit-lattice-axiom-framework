# Charge-directed axial coefficients: a separated-form bound

Separate analytical probe after the frozen mixed forest and residual module. Same actual rotor H2, physical Gauss fiber, W=1, protected union P=P_++P_-, L divisible by four and L>=12. This uses no independent edge weights and introduces no new dynamical law or monitored channel. The six maps below are auxiliary Laurent coefficients of the original coherent Hamiltonian, not physical event maps.

## 1. Exact maps and Gram matrix

For i=1,2,3 and s=+1,-1 define M_i^s on each protected input of polarity sigma and hole h by retaining only its ACTUAL axial H path with output hole

    a=h+2s sigma e_i.                                    (1)

There is exactly one common B on this path. The complete protected-column calculation gives its coefficient of modulus one, with the exact two-link Gauss shift and unchanged B pattern. The input A donor has charge sigma by its radius-two condition. Thus every column of each M_i^s has norm one.

Two distinct columns in the SAME map can coincide in their full physical output only if their input signs differ: with a fixed sign, (1) reconstructs h uniquely, and inverse charge/field transport reconstructs the entire input. For opposite signs the two holes are a-2s e_i and a+2s e_i. The complete mixed-row theorem gives exactly the two original predecessors and no additional column. Hence these collisions are precisely the mixed relation edges assigned to (i,s). Each complete mixed edge belongs to exactly one of the six maps.

It follows, as an identity on the FULL protected input space, that

    sum_(i,s) (M_i^s)* M_i^s = 6 I + A_eta,              (2)

where A_eta is the Hermitian adjacency matrix of the complete mixed relation forest, with its genuine unit edge phase t_x* t_y. Equation (2) includes singleton outputs, which supply their own diagonal contribution; no row has been omitted. The forest has maximum degree six.

Gauge the edge phases away along each tree. The adjacency norm is at most 2 sqrt(5). An elementary proof roots each tree and uses on every parent-child edge

    2 |f_p f_c| <= |f_p|^2/sqrt(5)+sqrt(5)|f_c|^2.

A nonroot vertex has at most five children, so its total coefficient is at most 2 sqrt(5). The root has at most six children and coefficient 6/sqrt(5)<=2 sqrt(5). Applying the same estimate to the negative form bounds both signs of the adjacency. Therefore

    sum_(i,s) ||M_i^s psi||^2
            >= (6-2 sqrt(5)) ||psi||^2.                  (3)

This is uniform in finite volume, the complete B pattern and all actual physical phases, but ONLY on the declared protected input support. It proves that all six coefficient maps cannot simultaneously annihilate a nonzero protected vector.

## 2. These are genuine flat-connection coefficients

Choose an edge-connection representation of the actual physical Gauss fiber, as in the frozen fixed-background proof. Add the physical flat connection phi dot delta to every oriented A-to-B edge, using its local displacement delta including seams. This has holonomies L phi_i and no plaquette flux. The change in a protected two-hop coefficient h->a is

    exp(i sigma phi dot (a-h)).                          (4)

For (1), equation (4) is exp(2 i s phi_i). Other nontrivial protected H columns have diagonal displacement +/-e_i+/-e_j, i!=j, hence frequencies +/-e_i+/-e_j; the same-hole return is the unchanged diagonal 6. They do not share the six axial frequencies. Thus, in this explicit connection gauge,

    H(A+phi) P = 6P
       + sum_(i,s) exp(2 i s phi_i) M_i^s(A)
       + sum_(diagonal frequencies nu) exp(i nu dot phi) C_nu(A).
                                                               (5)

The C_nu retain their complete actual two-path coefficients. Formula (5) is an exact finite Laurent decomposition, not permission to vary the six M coefficients independently while holding the remaining source fixed. Connection-gauge changes correspond to the usual charge-dependent matter-basis change; no phase-averaged physical preparation is being selected.

For a FIXED vector psi in this displayed trivialization and a FIXED complex number z, Parseval in phi gives the limited corollary

    integral_(T^3) ||(H(A+phi)-z)psi||^2 dphi/(2pi)^3
            >= (6-2 sqrt(5)) ||psi||^2.                  (6)

The constant Fourier term is (6-z)psi and all other frequencies contribute nonnegative squares. This is a fixed-vector coefficient identity, not a bound on phase-dependent eigenvectors or physical source densities.

## 3. Why this still does not solve the residual module

The actual spectral problem uses the COHERENT sum (5) at one physical phase. A candidate fiber eigenvector psi(phi) and its eigenvalue may both depend on phi. Equation (3) does not imply a lower bound for that coherent sum, nor does (6) permit holding psi fixed when the problem requires psi(phi).

The already frozen ALIGNED_FIBER_PROOF.md supplies an actual warning within this protected class: on L divisible by four (take L>=12) its full uniform-polarity plane wave lies in P and satisfies H(0)psi=0, while (3) remains strictly positive for that same nonzero psi. The diagonal and the coherently summed path coefficients cancel. This is not a counterexample to generic-phase exclusion, but it directly rules out replacing the true H by the separated positive form (2).

There is also a direct failure of a one-step observed-exit lower bound. Take L divisible by four, L>=16, hole h=0, all occupied A charges plus, one remote B vacancy v=(1,L/2,0), and NB=n-1. Put B plus on the graph-distance-three B ball around h and choose exactly (n-2)/2 B minuses outside that ball and v. The ball has44 B sites, so the capacity condition is satisfied at these sizes. Total charge is n, hence an integer Gauss flow exists. Every B within distance five of h is occupied. Each actual H output hole a is at distance at most two from h, has a plus B star and a full distance-three B neighborhood, with an all-plus A cone. Thus the COMPLETE H column, and all six M columns, land inside P. In particular (I-P)H|word> = 0 and (I-P)M_i^s|word> = 0 at every phase. This is a legal physical-background discriminator, not an actual Omega probability statement or an invariant orbit. Longer-time exit still requires the true coherent dynamics.

The coefficient bound therefore exposes a specific remaining cancellation issue rather than proving absorption. A valid continuation must control the physical phase-dependent transport ratios and the remaining rows in REDUCED_PROTECTED_MODULE.md. No nonzero residual minor, actual source-image faithfulness, full dark-module conclusion, rate, finite-spin transfer or continuously forced residence estimate has been obtained from this probe. No scientific computation was performed.
