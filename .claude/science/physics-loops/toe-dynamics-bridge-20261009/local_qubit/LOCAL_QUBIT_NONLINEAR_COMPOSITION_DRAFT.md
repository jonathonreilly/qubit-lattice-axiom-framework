# Proposed local-qubit to nonlinear-fluid composition

Root derivation, 2026-10-11. Provisional until both source theorems and this
composition have source-bound checks. This is a corollary within the supplied
GKSL construction, not a physical law selection or a permanent-Record claim.

## Inputs and exact initialization

Use the particle theorem's smooth solution U on [0,L], constants C_path,C_prob,
and small-delta conditions. For 0<delta<=1 set

    m = the least odd integer >= max(3,2pi delta^-2),
    ell=2pi/m, w=m^-3, N=max(2,ceil(delta^-19)),
    b=delta^-1, c=delta^-2.

The particle preparation draws N independent cell/species labels with exact
probabilities p_xv=w M_v[1+delta (P_m U(0))_v(x)]. The cutoff zero mode and
mean-zero density assumption give sum p=1; small delta gives positivity.
Its occupation-count law is multinomial. Choose capacity K>=N. Every such
count vector is realizable by at most K occupied qubits in each compartment.
An arbitrary distribution over the associated within-fiber bit configurations
realizes this law. Any density matrix supported in total number N whose
count-diagonal law is this multinomial law is allowed; coherence is unrestricted
subject to positivity and that support. A diagonal mixed density matrix is an
explicit existence witness. No initial fast-fiber equilibration is required.

Let the local-qubit port theorem's fast generator use BFS spanning trees and
unit edge clock before multiplication by nu. With D=27m^3 and K_Sigma=sum kappa,
write

    B_K = 54K/(delta w ell) + K^2 K_Sigma/(delta^2 N w^2),
    C_cap = 3N^2/(2delta ell) + K_Sigma N^2/(16delta^2 w),
    Delta_K=C_cap/K.

Define

    K_req=max(N,2,ceil(2L C_cap/delta^2)),
    S=max(1152,ceil(sqrt(2(K_req+1)))), K=floor(S^2/2),
    n_*=min(N,floor(K/2)), D_N=min(D,N),
    c_KS=min(K(2K-3),K(8S+19)),
    tau=c_KS[1+log D_N+(n_*/2)log(eK/n_*)],
    nu=2 tau B_K(1+L B_K)/delta^2.

All logs are natural. These choices meet the geometry's exact integer
admissibility interval; K>=K_req. Rates are supplied real positive numbers.
Then the local-qubit path comparison gives

    TV(actual associated count path, target particle count path)
       <= tau B_K(1+L B_K)/nu + L C_cap/K <= delta^2.

The norm event in the particle theorem is measurable on these finite-state
cadlag count paths. Transfer that event by total variation. Its field
h_v(x)=n_xv/(Nw delta M_v)-1/delta has piecewise-constant reconstruction I_m h.
Consequently

    P( sup_(0<=t<=L) ||I_m h(t)-U(t)||_(L2_M) <= C_path delta )
       >= 1-min(1,(C_prob+1)delta^2).

Here probability refers to the associated classical population count law of
the supplied GKSL dynamics. The full path may be non-Markov after projection
to counts; the source theorem already handles that by fast-fiber coupling.

## Actual quantum readout meaning

Every microscopic jump is a partial permutation of computational basis states,
so diag(exp(t L_GKSL) rho)=exp(t Q)diag(rho) for every density matrix. Let P_n
be the orthogonal projector onto a count fiber. The selective count measurement
rho -> P_n rho P_n has diagonal equal to the indicator of that fiber times
diag(rho). Applying these two identities successively shows that, for any fixed
finite ordered set of count-measurement times in [0,L], the quantum joint
readout law equals that of the associated classical count process at those
times. The transferred bound therefore controls all these readouts together,
with the same failure bound independent of their number. This argument does
not assign an ontological quantum trajectory or identify occupation bits with
permanent Records. Arbitrary unmeasured quantum observables are outside it.

## Explicit polynomial resource ceiling

Let c_m=2pi+2 and c_ell=2pi/c_m. For delta<=1,

    m<c_m delta^-2, ell>c_ell delta^2,
    delta^-19<=N<=2delta^-19,
    C_cap<=C_cap0 delta^-46,
    C_cap0=6/c_ell+K_Sigma c_m^3/4.

The last inequality separately bounds the hopping delta^-41 and collision
delta^-46 terms. Choose constants (independent of delta)

    C_req=max(2,2L C_cap0+1),
    C_S=max(1152,sqrt(2(C_req+1))+1), C_K=C_S^2/2,
    D0=27c_m^3, c0=C_K(8C_S+19),
    B0=54C_K c_m^3/c_ell+K_Sigma C_K^2 c_m^6,
    T0=c0 max(2+log D0+log C_K,54),
    V0=2T0 B0(1+L B0).

Ceiling/floor inequalities imply S<=C_S delta^-24, K<=C_K delta^-48.
The number of physical qubit sites (including inert full qubits) is at most

    m^3 S^3 <= c_m^3 C_S^3 delta^-78.

The actual slow exit bound satisfies B_K<=B0 delta^-91: its hopping term is
O(delta^-57), and N>=delta^-19 supplies the collision upper bound. The BFS
comparison gives c_KS<=c0 delta^-72. Since D_N<=D<=D0 delta^-6, n_*<=N<=2delta^-19,
and 1<=n_*<=K, the displayed tau satisfies

    tau <= c0 delta^-91
              [2+log D0+log C_K+54 log(1/delta)]
        <= T0 delta^-91[1+log(1/delta)].

Thus the chosen fast edge rate has the explicit sufficient upper bound

    nu <= V0 delta^-275[1+log(1/delta)].

Active sites and fast marks are O(delta^-54). The individual hopping rate
is O(delta^-51); an individual collision rate is O(delta^-85), using
N>=delta^-19. These are conservative constructive resource ceilings, not
physical scaling laws or efficiency claims. Microscopic volume, preparation,
rate strengths and the supplied dissipative law all change with accuracy.
No fixed-strength or fixed-microscopic-volume fluid limit follows from them.
