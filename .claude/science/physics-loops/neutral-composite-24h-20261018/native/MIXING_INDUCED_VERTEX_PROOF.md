# Native vacuum mixing induces a local heavy/neutral vertex

Status: conditional-support. Fixed finite volume and fixed even height L>=10 unless stated otherwise. Every numerical example is exposed model development; no observation is used as a fit or a test. This block uses the same one-qubit Hamiltonian and no new physical interaction.

## 1. Premises and physical channel identification

Use the canonical reduction, positive vacuum plane characters, and coefficients of `TEN_LAYER_NEUTRAL_BOUND_PROOF.md`. Let Delta=L/16, gamma=binom(2L-2,L-1)/8^(L-1), and c=(gamma/Delta)lambda^(L-4). A local pair of flipped adjacent columns has four plaquette fluxes. Its leading heavy hopping operator is T_e; on a flat background it is T_0. Horizontal hopping is -1, vertical hopping is -s_i s_j. For a horizontal pair, V_e=T_e-T_0 has +2 on each of the four vertical bonds leaving the pair, and their adjoints. These entries are inherited from the microscopic signs.

The heavy particle cannot move through every row while keeping the background in the same all-positive character. Fix the physical heavy sector produced by a singleton in reference row y0. At position i, identify its background orbit by W_i=Z_(x_anchor,y_i)Z_(x_anchor,y0). This flips precisely the two needed logical row characters; it leaves column characters and parity unchanged. In a flat configuration s_xy=a_x b_y, the vertical hopping factor b_y b_(y+1) cancels W_j W_i. Thus T_0 is ordinary sign-free hopping in this matched basis. For an edge flip supported away from the anchor column, E_e commutes with every W_i and T_e is the stated flux operator. Features crossing the anchor require the transformed strings. We assert a specified local vertex, not a global momentum-space sum of identical vertices.

## 2. Leading coefficient from the existing vacuum rotation

The vacuum perturbation theory gives

    |g> = |0> + c sum_e |e> + higher orders,
    |b_e> = |e> - c |0> + higher orders.

This is the first term of a normalized analytic channel transformation at fixed volume. For the heavy operator blocks,

    <b_e|H|g> = H_e0 + c(H_ee-H_00) + higher orders.

The diagonal heavy difference starts at J lambda V_e. Heavy corrections begin at J lambda^2; independent background-changing heavy paths require at least L-1 microscopic flips. Consequently

    <b_e|H|g> = J(gamma/Delta)lambda^(L-3) V_e
               + O_(R,L)(J lambda^(L-2)).

The common background contribution -J gamma lambda^L cancels c J Delta lambda^4. This statement does not exhaust the order-L heavy block: winding paths touching the occupied column can have extra local terms at that order. They are later than the displayed leading coefficient. The complementary assisted hop at order L-1 is also later. The leading coefficient is therefore fixed by existing vacuum fluctuations and signed hopping; it is not a separately supplied scalar coupling.

This is a vacuum-channel rotation, NOT a heavy-channel adiabatic elimination: J lambda is much larger than J lambda^4. Dividing the full heavy transition by the small neutral gap would not give a controlled Schrieffer-Wolff transformation. The local coefficient is basis-dependent until the preparation, readout and effective frame are specified together.

## 3. Exact finite-time consistency

Set U_a(tau)=exp(-i tau T_a), with physical time hbar tau/(J lambda). Duhamel's identity gives exactly

    -i c integral_0^tau U_e(tau-s)V_e U_0(s) ds
      = c[U_e(tau)-U_0(tau)].

Thus the vertex reproduces the already checked matched-return response in `BOUND_MODE_ENVIRONMENT_PROOF.md`. A diagonal return first sees a plaquette at four hops. It need not respond at first order in tau even though the Hamiltonian vertex is nonzero. The native finite-volume transfer uses matched microscopic embeddings and the flat-orbit cancellation in that proof; a bare pulse is not covered.

## 4. Exact two-channel diagnostic, with an explicit limit on its scope

For a single specified pair channel, write the scaled diagnostic model

    H_bare = diag(L_0,L_0+V) + [[0,-h],[-h,d]] tensor I,

where L_0=T_0+4, d>0 and h>0. Here d=Delta lambda^3 and h=gamma lambda^(L-1) reproduce the leading native ratio h/d=c. The model omits all other pair channels, recoil, higher native terms and anchor-crossing strings; it is a coefficient diagnostic, not a new microscopic Hamiltonian or a proof of native scattering.

Diagonalizing only the constant background matrix, tan(2theta)=2h/d, gives background thresholds E_- and E_+, diagonal local potentials sin^2(theta)V and cos^2(theta)V, and the exact off-diagonal potential sin(theta)cos(theta)V. Their values are linked: no independent off-diagonal coupling may be inserted. The small-c vertex above follows immediately. At h=0 the channels decouple. The finite-matrix runner checks this identity and the propagator integral independently of the native combinatorics.

## 5. Energy-conserving coefficient scattering

Here use d for the separation of the diagonalized thresholds (the bare separation differs by a factor sqrt(1+4c^2)). Subtract the lower threshold. To first order in c the channels are L_0 and L_0+V+d, with transition cV. For incoming kinetic energy E and outgoing kinetic energy E_f=E-d>0, define G_f^+=(L_0-E_f-i0)^(-1). The distorted outgoing bra gives the finite-rank form factor

    M/c = phi_(k')^dag (I+V G_f^+)^(-1) V phi_k
        = phi_(k')^dag V(I+G_f^+ V)^(-1) phi_k.

Both waves obey their respective kinetic shells. The six-site set and V are those of `BOUND_MODE_ENVIRONMENT_PROOF.md`. This expression conserves total energy in the stated pinned coefficient model. It is not a full microscopic scattering theorem or a rate.

At low outgoing energy the six-site free resolvent is

    G_f^+ = g_f 11^T - A + o(1),
    g_f = log(32/E_f)/(4pi) + i/4 + o(1).

The potential kernel A and its declared standard-mathematics source are recorded in the preceding environment proof. Let C=I-AV, p=1/pi and

    beta = 1^T V C^(-1)1 = -4(8p-3)/(8p^2-1),
    g_c = -1/beta = (pi^2-8)/(12pi^2-32pi).

The rank-one inverse identity gives exactly, for the constant-vector leading kernel,

    1^T V(C+g_f 11^T V)^(-1)1 = 1/(g_f-g_c).

For E,E_f tending to zero with d/E in a compact subinterval of (0,1), the restricted incident waves tend to 1. The six-site inverse stays bounded; their O(sqrt(E)) corrections and the potential-kernel O(E_f log(1/E_f)) corrections are smaller than 1/log(1/E_f). Therefore the first-order coefficient satisfies

    log(1/E_f) M/c -> 4pi.

The unscaled amplitude still vanishes. This is the full local V form factor, not the endpoint source u0+u1; replacing one by the other would give the wrong coefficient. The limit is taken after extracting first order in c. It does not assert a uniform all-orders simultaneous native lambda limit.

The relation <psi_e^-|V|phi_k>=(E_f-E)<psi_e^-|phi_k> does not set the answer to zero. The two states diagonalize different channel Hamiltonians, and their generalized overlap contains an energy denominator. Wavepacket regularization preserves the finite transition; dropping the singular off-shell overlap before taking d to zero is invalid.

The runner uses the exact rotated local potential W=[[sin²theta,sin theta cos theta],[sin theta cos theta,cos²theta]] tensor V, the two free channel resolvents and T=W(I+G W)^(-1). At fixed E=.1, threshold separation .03, its transition approaches the first-order expression with O(c²) relative error. Separately, the six-site threshold expression agrees with its leading kernel to relative error 3.34e-7 at E_f=1e-7. These are controls of the declared coefficient model, not observational data or full-native error estimates.

## 6. What is still required

This establishes a local matched vertex and its finite-time consequence. It does not yet identify a global q=0 pole charge, a relaxed heavy eigenstate, a complete energy-conserving emission rate, a universal equivalence-principle coupling, a three-dimensional cosmological field, or a selected value of L, J or lambda. Translational projection must include the physical-plane gauge. Fixed-volume coefficient control alone is not a uniform on-shell theorem.
