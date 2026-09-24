# A finite autonomous clock for the original reduced dynamics

Personal root derivation, 2026-09-24. Provisional conditional construction;
independent reconstruction pending. This extends the separately sealed finite
energy supply construction. It retains the original microscopic H and L_j.
The conclusion is uniform approximation of its one-time reduced channels over
a fixed finite interval. It is not an exact continuous-time marked instrument,
a process-tensor result, or a native microscopic selection principle.

## 1. Question and supplied resources

The preceding construction uses a positive finite battery to realize a finite
sequence of marked collision gates, but schedules those gates externally.
Here a finite prepared clock and a time-independent Hamiltonian implement the
sequence approximately in physical time. All spectral couplings, program,
phase references, blank flags and clock preparation remain supplied. Their
energies, dimensions and large coupling scale are explicit rather than free.

Let the system be finite dimensional, H>=0, with h=||H||, and set

    A(rho)=-i[H,rho],
    D(rho)=sum_j L_j rho L_j* - {Gamma,rho}/2,
    Gamma=sum_j L_j* L_j,       g=||Gamma||,
    Phi(t)=exp(t(A+D)).

We use the diamond norm, or equivalently the reference-uniform channel trace
norm, with maximal distance two. Fix T>0, n>=1, tau=T/n and tau g<=1/2.
The original marks give Kraus operators

    K_0=sqrt(I-tau Gamma),       K_j=sqrt(tau)L_j,
    followed by exp(-iH tau).

Their channel Phi_tau has a unitary completion U on system and a fresh blank
zero-energy flag. All n flags are included from the start. Later gates do not
act on earlier flags. The preceding root bound is

    ||Phi_tau^k-Phi(k tau)||_diamond <= k tau^2 c,
    c=7g^2+4hg,                    0<=k<=n.                 (1)

This conservative constant is sufficient. The independent predecessor gives
a sharper constant, separately attributed, but it is not needed here.

Let E_a be the distinct positive gaps above the minimum eigenvalue of H,
a=1,...,r. The preceding finite battery has r ladders of length L+2, positive
Hamiltonian H_R=sum_a E_a N_a, and product sine state beta on levels1,...,L.
It lifts every completed gate to V(U), an exactly unitary operator commuting
with H+H_R. Zero-energy flags do not change these spectral gaps. On complete
charge sectors, products obey V(U_k)...V(U_1)=V(U_k...U_1); the identity rule
on incomplete sectors is common to every lift. No reservoir reset is made.
For every prefix, including arbitrary external references and all its flags,

    channel error <= eta_L=min(2,8 sin(pi/[2(L+1)])).        (2)

Its mean initial energy is (L+1)sum_a E_a/2. The buffer, same-battery product
identity, all-input estimate, and finite noncommensurate-spectrum theorem are
premises from FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS.md. They are
not inferred from an informal infinite-ladder shift or catalytic claim.

## 2. The interaction-picture program is essential

The physical autonomous Hamiltonian will include H+H_R as an additive term.
Using the Schrödinger-picture gates directly would therefore add the free H
evolution a second time. Program instead the conserving unitary gates

    W_k = exp(+iH k tau) V(U_k) exp(-iH (k-1)tau),
    G_k = W_k ... W_1 = exp(+iH k tau) V(U_k ... U_1),
    G_0 = I.                                                  (3)

All exponentials act on the system, and every W_k and G_k commutes with
H+H_R. Telescoping is an exact full-space identity. It does not require the
W_k themselves to equal the chosen lift's identity boundary rule outside
accessible complete sectors.

Define the exact interaction-picture channel

    Psi_I(t)=exp(-t A) Phi(t).

Its derivative is D_I(t)Psi_I(t), where
D_I(t)=exp(-t A) D exp(t A). As ||D||_diamond<=2g and Psi_I is a channel,

    ||Psi_I(t)-Psi_I(s)||_diamond <= 2g |t-s|.                 (4)

The large h does not enter this time-mismatch estimate. It still enters (1).
This distinction is needed for the resource scaling below.

## 3. Positive finite history Hamiltonian

The clock has integer positions x from -w-R through n+R, with w>=2. Its
dimension is M=n+w+2R+1. Put k(x)=min(n,max(0,x)), and define

    Gcal=sum_x |x><x| tensor G_{k(x)},
    T_M=sum_{x=x_min}^{x_max-1}|x+1><x|,
    K_M=2J I-J(T_M+T_M*),
    e_0=2J[1-cos(pi/(M+1))],
    H_hist=Gcal [(K_M-e_0 I) tensor I] Gcal*,
    H_aut=H+H_R+H_hist.                                       (5)

The finite path eigenvalues give K_M-e_0 I>=0. Thus H_hist and H_aut are
nonnegative. H_aut is a finite, time-independent Hamiltonian. Since every
G_k conserves the free energy,

    [H_hist,H+H_R]=0.                                         (6)

The nearest-clock hopping block is -J G_{k(x+1)}G_{k(x)}*.
These blocks generally act on the entire system, battery and a program flag;
nearest-neighbor clock hopping is not a spatial-locality theorem for matter.

Choose the normalized initial clock packet

    chi(x)=i^x sqrt(2/(w+1)) sin(pi(x+w+1)/(w+1)),
            x=-w,...,-1,
    chi(x)=0 otherwise,
    theta=pi/(w+1),        2J cos(theta)=1/tau.                (7)

It is supported entirely in G_{k(x)}=I. The initial joint preparation is the
product chi tensor beta tensor arbitrary system/reference state tensor blank
flags. No state-dependent pre-entangling clock transformation is hidden.
Equations (5)-(6) imply that, after tracing the clock, the evolution is exactly
the mixture of prefix G_{k(x)} channels weighted by the freely propagated
finite-clock position distribution p_t(x), followed by system free evolution
exp(t A). Free reservoir evolution at the end disappears under partial trace.
For arbitrary input, correlations with the one shared battery remain intact.

The initial expectation of H_hist is 2J-e_0=2J cos(pi/(M+1)). Indeed the
phase i^x makes the real nearest-neighbor clock overlap zero and Gcal is the
identity on the initial support. This is the energy above the actual ground
of H_hist; it is not an arbitrarily chosen positive constant offset. The
total initial energy is

    E_system(0) + (L+1)sum_a E_a/2 + 2J cos(pi/(M+1)).        (8)

The clock/program term is an interaction Hamiltonian as well as a clock term.
Equation (8) does not pretend that all of its energy is a separately free
clock observable. H_hist and H+H_R are separately conserved. In particular,
the battery energy change exactly balances system energy change. Clock and
battery states may change and correlate; no catalyst-return claim is made.

## 4. Clock position bound in physical time

For analysis only, first evolve the finite-support packet on the infinite
integer chain with K=2JI-J(T+T*). Let X be position and

    V=iJ(T-T*).

Then i[K,X]=V, [K,V]=0, and X(t)=X+tV on this packet's finite-moment domain.
The sine recurrence and its two zero-extension endpoints give exactly

    <X>=-(w+1)/2,
    <V>=2J cos(theta)=1/tau,
    Var(V)=4J^2 sin^2(theta)/(w+1),
    sd(X)<=(w-1)/2.                                         (9)

For clarity the endpoint identity is
sum_j a_j a_{j+2}=cos(2theta)+2 sin^2(theta)/(w+1), with a_j the normalized
real sine amplitudes extended by zero. Dropping its boundary correction
would incorrectly give zero velocity variance.

The Hilbert-space triangle inequality gives
sd(X+tV)<=sd(X)+t sd(V); it assumes no position/velocity independence.
Adding the fixed initial mean lag and using Cauchy-Schwarz yields

    tau E |X(t)-t/tau|
      <= tau w + t tan(theta)/sqrt(w+1).

Because projection onto [0,n] cannot increase distance from t/tau in that
interval, the clipped position obeys uniformly 0<=t<=T,

    E |tau k(X(t))-t|
      <= tau w + T tan(theta)/sqrt(w+1).                    (10)

This is a physical-time bound. A perfect-transfer clock's nonlinear
sin^2(pi t/(2T)) mean would not establish (10); that route was rejected.

To return to the finite path, embed its Hilbert space in the integer line.
The finite and infinite adjacency powers on chi agree below order R, because
both boundaries are at least R steps from its support. After removing their
irrelevant scalar phases, the two Taylor series give the vector error

    <= 2 sum_{m>=R} a^m/m! <= 2 exp(a) a^R/R!,
    a=2JT.                                                  (11)

The associated trace/channel error is at most

    b_R=min(2,4 exp(a) a^R/R!).                              (12)

Conjugating by the same controlled prefix operators and including a reference
does not increase that bound. If R>=8a, R!>=(R/e)^R implies
4 exp(a) a^R/R!<=4 exp(-7a). This deliberately loose tail estimate suffices.
M is still O(n+w) when R is chosen this way, since a=n/cos(theta) and
cos(theta)>=1/2 for w>=2. Infinite position is an analysis aid; the implemented
clock and Hamiltonian in (5) are finite throughout.

## 5. Uniform finite-horizon theorem

Let Omega_aut(t) be the system channel from (5), with battery, clock and all
flags traced out and their specified initial preparations. Equations
(1)-(4), the exact mixture identity, and (10)-(12) prove

    sup_{0<=t<=T} ||Omega_aut(t)-Phi(t)||_diamond
      <= min(2, zeta),

    zeta = eta_L + T tau c
         + 2g[tau w + T tan(theta)/sqrt(w+1)] + b_R.         (13)

To see this without assuming a classical Markov clock, use the infinite
packet only in the comparison channel. Replace each actual lifted prefix by
its ideal collision prefix at cost eta_L, uniform in that prefix and the
reference. Replace the latter by Psi_I(k tau) at cost at most T tau c.
Apply (4) and the position distribution to replace that mixture by Psi_I(t).
Finally restore finite-clock propagation using (12), and apply exp(t A).
Only convexity, contractions and the stated isometry estimates are used.

At a specified t the reservoir preparation and Hamiltonian are the same as
at every other t. The supremum in (13) is therefore a common realization on
the whole interval, not a different channel-specific dilation for each time.
It does not imply closeness of joint multi-time statistics under interventions.
The discrete gate program uses exactly the original marks; the theorem does
not identify clock positions with exact continuous stochastic event times.

For the bounded microscopic observable H,

    |E_aut(t)-E_GKLS(t)| <= h min(2,zeta).                    (14)

An energy conclusion needs this error multiplied by h. Density convergence
alone is insufficient when the microscopic H changes along a limit.

## 6. Application to the supplied star and electric family

Use the complete sixteen-state physical star, original resolved or coherent
L_j=sqrt(kappa)/epsilon j, and supplied electric family
H_lambda=H_0+K lambda E2. Put C=S(S+1) and epsilon^2 C=delta/K with fixed
positive delta,K,kappa. The independently checked microscopic result gives
h_lambda=O(C^2), g=O(C), and at most fifteen distinct positive gaps, uniformly
0<=lambda<=1. The spectral program and reservoir can depend on lambda; no
common fixed physical bath is being selected.

Sufficient choices, with fixed positive prefactors, are

    L=ceil(constant C^2),    w=max(2,ceil(constant C^2)),
    n=ceil(constant C^5),    tau=T/n,
    R=ceil(8n/cos(pi/(w+1))).                               (15)

Then every nonexponential term in (13) is O(C^-2): tau c=O(C^-2),
g tau w=O(C^-2), and g tan(theta)/sqrt(w+1)=O(C^-2). The boundary term is
exponentially small in C^5. Equations (13)-(14) therefore give a uniform
O(C^-2) channel error, an O(1) absolute energy error, and O(C^-1) error in
the energy divided by C. Combining this with the separately attributed
uniform microscopic Duhamel estimate, for the same supplied dressed input,

    E_aut(t)/C -> (3K/2)[1-exp(-12kappa t)]                  (16)

uniformly on each fixed [0,T], including choices lambda=lambda_S in [0,1].
It is a one-birth star. Nothing here changes its capacity or the six-site
cycle's inability to form a second pair.

The sufficient initial battery energy is O(C^4), its dimension is bounded
by (L+2)^15, clock dimension is O(C^5), and clock/program energy above its
ground is O(C^5). The hopping strength J is O(C^5). There are n=O(C^5)
fresh program flags, each of dimension seven or four for the resolved or
coherent instrument; their combined Hilbert-space dimension is exponential
in n. Pure blank memory and coherent preparations are resources even when
assigned zero free energy. None of these sufficient bounds is an optimum.

## 7. Status and physical limits

This is an engineered positive finite-Hamiltonian construction for a stated
finite interval, with growing resources. It shows what the supplied original
reduced generator can be approximated by when such preparations and couplings
are allowed. It does not derive them from the lattice axioms or from a thermal
reservoir. It therefore does not select lambda, the compensation, a time arrow
or a physical vacuum. It does not replace the matter degrees of freedom by a
field-only postbirth limit.

No exact unbinned event-time law, arbitrary-intervention process tensor,
uniform infinite-time approximation, spatial locality, bounded-strength or
finite-density thermodynamic limit, replenishment, optimality, or TOE claim
is made. Finite recurrence is compatible with this finite-horizon statement.
The source and controls must be sealed and independently compared before
describing this extension as independently checked.
