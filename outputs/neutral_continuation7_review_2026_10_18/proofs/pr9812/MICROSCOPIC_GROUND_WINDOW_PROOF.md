<!-- Original PR9812 source SHA256 0fdf4d387748323f3f2ca914d2dd49af56e4912836c2bfd930a2928500242628. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# From native coefficients to actual ground-state finite-time response

Status: bounded-support. The Hamiltonian and diagnostic remain supplied. The result is a joint weak-coupling/growing-finite-volume statement, not a full microscopic outgoing pole or a cosmological-state theorem. Set Jz=1 in the proof; restoring it replaces t by Jz t and frequency by omega/Jz.

## A. Positive form bound for the actual fixed-order normal form

Fix m>=4. The exact local construction gives U_m H U_m†=B_m+R_m, B_m=2N+sum_(j=1)^m lambda^j D_j, and interaction norm of R_m at most C_m lambda^(m+1). Each D_j is a sum of Hermitian connected finite-support terms. Apply the commuting-N average separately to each term; their sum is unchanged since [D_j,N]=0. Average under the finitely many plane Pauli actions meeting its support. This leaves the coefficient unchanged and produces individually N-preserving, plane-invariant terms without unbounded support enlargement.

For each term t enlarge its support to a fixed column-convex box, including all incident vertical bonds and paths to one anchor slice. Let Q be the projector onto at least one broken vertical bond in that box. If the input has no such wall, any nonempty finite spin change creates a vertical wall and cannot remove one outside the box. N preservation forbids it. Whole-column flips are excluded by taking all periods larger than the fixed support. Thus t is diagonal on Q=0 with no matrix elements to Q=1.

Define f_t by that wall-free diagonal value, sampled on the column signs at the anchor slice. Then t-f_t=Q(t-f_t)Q and its quadratic form has absolute value at most 2||t|| Q. Summing translates bounds all these remainders by C_m lambda N. No extensive vacuum constant remains: subtract the all-up value termwise.

Plane flips act on the sampled signs by s_xy -> a_x b_y s_xy. Therefore f_t is invariant under row and column sign flips. On a proper transverse rectangle all elementary plaquettes P=+1 imply s_xy=a_x b_y, so f_t equals its all-up value. With B_p=(1-P_p)/2,

    |f_t-f_t(allup)| <= 2||t|| sum_(p in rectangle) B_p.

Group translated terms by their anchor slice. The wall-free functional is constant at orders below four. At order four its only sign-dependent return graph is an elementary square, with the already derived coefficient -P/128. Repeated-edge graphs are sign independent. Thus its exact excess per slice is sum B_p/64. Higher orders are bounded in absolute value by C_m lambda^5 sum B_p using the preceding local comparison. The anchor grouping prevents a spurious local-density/gauge mismatch when the sampled slice varies.

For sufficiently small positive lambda, at fixed m, this yields the volume-independent form inequality

    B_m-E_vac >= (2-C_m lambda)N + (lambda^4/128) sum_(x,y,z) B_xyz.   (1)

This is an inequality for B_m. The microscopic remainder is treated separately below, not discarded.

## B. Ground cluster in the growing finite boxes

Take even periodic cubes of side L=2 ceil(K_m lambda^-4/2), volume V=L^3=O(lambda^-12). K_m is a fixed sufficiently large constant for the locality comparisons below. With N=0 every column is constant in z, and a bad transverse plaquette occurs on all L slices. Equation (1) gives a positive constant gap above the span P0 of configurations

    N=0, P_p=+1, s_xy=a_x b_y.

There are 2^(2L-1) such product configurations. Each is an exact B_m eigenvector with energy E_vac: proper-support N-preserving terms cannot mix them, and exact plane flips equate their energies. The bound excludes every other ground state. Nonzero N costs at least a fixed wall energy; N=0 with a bad plaquette costs at least lambda^4 L/128, also bounded below. The gap is independent of the dimension of this degenerate ground subspace along the stated box family.

Choose m=40. The exact remainder has global operator norm at most C V lambda^41=O(lambda^29). Isolated-cluster perturbation gives a lowest microscopic band of the same rank whose projector, in the U_40 frame, differs from P0 by O(lambda^29). Small splittings inside that band are allowed. The exact true-ground projector may have smaller rank and is NOT asserted close in operator norm to all of P0. Every exact ground density nevertheless maps, by a near-identity intertwining unitary, to some density on P0 with trace-norm error O(lambda^29).

## C. Original diagnostic and elementary error accounting

Let C=V^-1/2 sum_j Z_j Z_(j+2ez), so ||C||<=sqrt(V). Transform it with the same U_40 and truncate its connected local Taylor coefficients through order40, obtaining C_40. The exact-source tail obeys

    ||U_40 C U_40†-C_40|| <= C sqrt(V) lambda^41.

This contributes O(V lambda^41)=O(lambda^29) to a connected correlation. Replacing an actual ground density by its P0 counterpart costs O(V lambda^29)=O(lambda^17). Finite-volume Duhamel, without an infinite-volume remainder norm, bounds the dynamics difference for |t|<=T=c lambda^-4 by

    C T ||R_40|| V <= C T V^2 lambda^41=O(lambda^13).               (2)

Center each source with its corresponding stationary mean; the differences of means are bounded by the same estimates. The actual state is any microscopic ground density, not a specially selected dressed all-up preparation.

## D. Independence from the ground superposition

Every local coefficient c_j of C_40 is plane-flip invariant, as are B_40 and its time evolution. Ordinary finite-range Lieb-Robinson locality gives a conditional-expectation localization c_j^R(t) to radius R=L/10 with exponentially small error for R-v_m T positive and proportional to L. Choose K_m sufficiently large for all geometrical versions of this separation. Constants may depend on m, so no universal numerical K is claimed.

Conditional expectation preserves plane invariance exactly. The union of the localized support and the fixed support of c_k cannot cover an entire vertical column. Consequently c_j^R(t)c_k has zero offdiagonal matrix elements between distinct P0 column configurations. Plane-flip transitivity equates its diagonal elements. Thus

    P0 c_j^R(t)c_k P0 = a_jk(t) P0

as an operator identity. This avoids an exponentially large ground-dimension factor. Summing j,k with normalization1/V costs only V times the localization error, which remains smaller than every power of lambda. Every density on P0 therefore has the same connected response as all-up to that accuracy on this time window.

## E. Frequency window and the complete four-wall response

Choose a fixed smooth function psi with compact support in (-1,1), and define

    S_T(omega)= integral dt/T psi(t/T) exp(i omega t) <C(t)C>_connected.

This is an explicit analysis window, not an added Hamiltonian term. Its Fourier transform decays faster than any inverse power; the window need not define a positive spectral weight.

In the even longitudinal-plane-parity sector N=2 is impossible: one partially flipped column changes plane parity between the inside and outside of its interval. A fixed-order finite-support source cannot reach another N=0 column pattern, and centering removes the vacuum component. Hence the first source sector is N=4 and the rest have N>=6. By (1), the latter lie above10 for sufficiently small lambda. For omega in [7,9], their window contribution is at most

    C_p V T^-p.

Take p=5 to obtain O(lambda^8). Integrating (2) with dt/T costs only the fixed L1 norm of psi, not another T. The actual ground-state window response thus equals the FULL finite-volume N=4 coefficient response plus O(lambda^8), uniformly over that frequency interval. The scale1/T is lambda^4, while the previously derived residue scale is lambda^6.

To compare that full finite-volume block with the infinite compact graph, use the local charge component

    c_(j,+4) = (2pi)^-1 integral dtheta exp(-4i theta)
                  exp(i theta N)c_j exp(-i theta N).

Because N is a sum of commuting vertical-bond projectors, this enlarges the finite support by only incident vertical neighbors. It raises N by four; on all-up it equals the N=4 projection of c_j. The N=4 response is therefore the local two-point function of c_(+4)† and c_(+4), rather than an insertion of a nonlocal spectral projector into a locality estimate.

In the all-up product state, connected correlations of disjoint localized operators vanish. Locality supplies summable tails in their relative separation. Split the zero-momentum correlation sum into separations well inside the cube and its tail. Local finite/infinite dynamics agree in the first part; the tail is exponentially small in L/c_geometry-v_m T, up to polynomial factors. With the chosen K_m, the resulting difference is superpolynomially small. This controls winding/background changes; initial compact support alone would not do so. In the infinite finite-excitation representation, N=4 and even plane parity are exactly the two-column common-interval graph used earlier.

Restoring units, for any actual microscopic ground density on these cubes,

    S_T^H(omega) = S_T^(complete compact N=4, B_40,C_40)(omega)
                   +O(lambda^8),
    T=c lambda^-4/Jz,  omega/Jz in [7,9].                           (3)

## F. What equation (3) does and does not establish

This is an actual microscopic finite-time response comparison, with error smaller than the candidate residue scale, and it removes the choice of a particular polarized reference within this ground-state problem. It keeps the whole coefficient response, including fast background and fine structure. It does not say that an outgoing pole becomes an isolated positive line, nor prove an outgoing pole of H. Ground-state restriction, supplied H, weak anisotropy regime, diagnostic and units remain explicit; no cosmological initial state, measured coupling or empirical fit is derived. Constants are fixed-order asymptotic constants, not a certified useful numerical threshold. The joint limit is lambda->0 with L proportional to lambda^-4; an arbitrary fixed-lambda thermodynamic ground-state theorem is not claimed.
