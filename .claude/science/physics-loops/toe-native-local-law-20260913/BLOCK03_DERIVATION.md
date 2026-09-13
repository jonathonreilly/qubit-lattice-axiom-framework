# Protected native paths for a theorem-matched interacting Weyl model

Working block03 derivation, 2026-09-13. This uses an explicitly supplied
interacting model and a named external mathematical theorem. It does not
derive a Hamiltonian, Born rule, physical clock, gauge photon or gravity.
The finite native bridge has author checks against separate ordinary CAR
matrices. Independent review remains pending.

## 1. Exact external input and hypothesis match

Primary source: Giuliani, Mastropietro and Porta,
[Anomaly non-renormalization in interacting Weyl semimetals, v3](https://arxiv.org/pdf/1907.00682v3),
sections2.2–2.3, Eq.(2.27), Theorem2.1. Their theorem supplies an analytic
small-coupling counterterm and renormalized Weyl two-point function for its
specified two-band, two-node, symmetric finite-range class. The limit takes
volume first, then inverse temperature. We use only this correlation result,
not their anomaly coefficient. The coupling threshold is existential, not
a claimed numerical interval. The counterterm is indispensable.

Choose two orbitals per model cell n in Z³, with

    h0(k)=sin(k1) sigma1+sin(k2) sigma2
          +(2+zeta-cos(k1)-cos(k2)-cos(k3)) sigma3,
    zeta in [1/2,1).

This is the source's explicit example with t1=t2=1. The interacting model is

    H_W=sum c* h0 c
        +lambda sum_n (n_n0-1/2)(n_n1-1/2)
        -nu(lambda) sum_n(n_n0-n_n1).                  (3.1)

Its interaction has w01=w10=(1/2)delta_n0 and all other entries zero.
It is real, even, finite-range, translation invariant and invariant under
all spatial reflections and orbital exchange. Thus no unverified extension
to the four-node matching symbol is used.

The preceding source attribution is the external theorem import. The
following checks and native embedding are derived here.

For h0=a sigma1+b sigma2+c sigma3:
a is odd in k1 and even in the others; b is odd in k2 and even in the
others; c is even in all three. Therefore
h0(k)=sigma3 h0(-k) sigma3,
h0(k)=h0(k1,k2,-k3), and
h0(k)=-sigma1 h0(-k1,k2,k3) sigma1.
Time reversal by simple complex conjugation fails when sin(k1) is nonzero.

The eigenvalues are +/-sqrt(a²+b²+c²). A zero requires sin(k1)=sin(k2)=0.
If either coordinate is pi modulo2pi, c>=1+zeta>0. Otherwise the only
zeros are(0,0,+/-p), p=arccos(zeta). Their velocities are
v1=v2=1 and v3=sin(p)=sqrt(1-zeta²), with quadratic coefficient b0=zeta.
In particular b0>=1/2; the tempting choice zeta=0 would NOT obey the
nonzero quadratic-coefficient hypothesis as stated in this theorem.

For 0<p<=pi/3, p/sin(p) is uniformly bounded, so the separation2p and
v3 satisfy the uniform comparability condition with c0=3.
The node separation tends to zero as zeta tends to1. Taylor's theorem
bounds the sine remainder by |k_j|³/6 and the cosine remainder at a node
by |delta_k3|³/6. The transverse cosine terms are bounded by
(k1²+k2²)/2. These give the source's local remainder bounds uniformly.
Away from both node neighborhoods, compactness in the CLOSED parameter
interval [1/2,1] gives a positive determinant lower bound; at zeta=1
the only additional limiting zero is the merged node at the origin,
already excluded from that region. The untilted scalar term d is zero.
The complementary-region quadratic remainder is also controlled:
outside distance2p from the nodes, |k|>p and
1-zeta=1-cos(p)<=p²/2<=|k|²/2.

For any fixed zeta, such as1/2, the source theorem now supplies lambda0>0,
an analytic nu with nu(0)=0, and the interacting zero-temperature
two-point function with the Weyl singularity of Eq.(2.27) for
|lambda|<=lambda0. Z=1+O(lambda), v_j=v_j0(1+O(lambda)); its relative
remainder is O(|k-p_node|^theta), every fixed0<theta<1.
The selected strengths and analytic counterterm are model data. No
numerical value of nu or lambda0, isotropic dressed speed, interacting
star coefficient or emergent dynamical gauge field has been computed.

## 2. Place both orbitals on the actual virtual lattice

Let model orbital r=0,1 at cell n be virtual vertex

    v(n,r)=(2n1+r,n2,n3).

This is a bijection onto Z³. Retain the block02 candidate matching:
a y bond is a candidate exactly when its tail x+y is odd. All x,z bonds
and the alternating y bonds are protected. A candidate's +x plaquette
detour is entirely protected. The physical native edge factors remain
at midpoints2v+e_a; this orbital map does not put two qubits at one site.

Every nonzero offsite matrix element of h0 connects orbitals in neighboring
MODEL cells. The required virtual displacements are:
- same orbital, x-cell neighbor: +/-2e_x;
- same orbital, y or z neighbor: +/-e_y or +/-e_z;
- different orbitals, x-cell neighbor: +/-e_x or +/-3e_x;
- different orbitals, y-cell neighbor: +/-e_x+/-e_y.

All admit a simple protected path of length at most3.
An x path is straight. A same-orbital y hop is either protected or uses
its three-edge x detour. For an offdiagonal xy hop, perform x first or
last so that the y edge's tail x+y is even; the two possible x coordinates
have opposite parity. A z path is already protected.
The model has no offdiagonal z-cell hopping.

No hopping along a candidate is required. Diagonal terms and the
counterterm are functions of the two endpoint number operators; the
interaction is the adjacent-orbital density product.
An open model-cell box maps to a virtual rectangular box of x-width at
least two. At its maximum x boundary, use the -x detour for a candidate
y hop; otherwise use +x. Both choices flip the required parity. All
routed paths then stay inside the virtual box, without extra bulk
fermions. Boundary hops exiting the model box are omitted. Periodic
wrap bonds are not asserted to be uniformly short in physical Z³.

## 3. Native protected path identities

For a simple protected path p=(v0,...,v_l), l>=1, define

    A_p=i^(l-1) A_(v0,v1)...A_(v_(l-1),v_l).

In the native even-CAR code, A_vw=-i gamma_(2v) gamma_(2w).
Internal Majoranas cancel in order, so A_p=-i gamma_(2v0)gamma_(2v_l).
The factor i^(l-1) is necessary; dropping it gives the wrong phase.
The full native product is Hermitian because its reversed product gains
(-1)^(l-1), compensating complex conjugation of that factor.
It is an involution on the code, and in fact on the ambient Pauli carrier.

For endpoints v,w put

    T_p=(i/2) A_p(B_v-B_w),
    J_p=-(1/2) A_p(I-B_v B_w).

They implement c_v* c_w+c_w* c_v and
i(c_v* c_w-c_w* c_v), respectively.
An oriented coefficient h_vw=alpha+i beta is therefore alpha T_p+beta J_p.
All site-order/orientation signs must be retained in the checker.

Number terms use n_v=(I-B_v)/2. The interaction in(3.1) becomes
lambda B_v(n,0) B_v(n,1)/4, and its counterterm becomes
-nu(B_v(n,1)-B_v(n,0))/2. There is no additive energy reset between
Record histories.

Each path of length at most3 uses only the native stars of at most4
vertices. On the cubic graph their union has at most
6(l+1)-l=5l+6<=21 edge factors. All lie within physical Manhattan distance
at most7 of the starting physical vertex2v. Endpoint B factors add no
sites outside this union. This is bounded physical support, not a supplied
synthesis into two-site gates or an admissibility derivation from H.

Every A_p has X support only on protected edges. Hence T_p,J_p,B_v,
the density interaction and the complete native H_W commute with every
candidate Z and every native cycle. The changing CAR dictionary after
Record deletion intertwines the same full interacting Hamiltonian.

## 4. Global content kernel and continuing formation

For the complete finite multiset eta of neighboring M2 contents define

    F(eta)=average_(a in eta)[(3/4)delta_a+(1/4)delta_(I-a)],
    F(empty)=delta_0.

It is a normalized nonnegative Borel kernel on ALL conditions. It is
covariant under lattice translations/proper rotations and algebraic
similarity/conjugation. Its values vary with eta. Restrict its realization
to supplied digital projectors P and I-P. With n>0 neighbors and sign
sum b, its plus probability is1/2+b/(4n), always in[1/4,3/4].

Use the program graph of physical sites with at least two odd coordinates.
It is the subdivided cubic graph, disjoint from all native edge factors.
Start from TWO adjacent equal digital program Records, for example
(1,1,1) and(2,1,1), both P. They support each other under the same global
F. One isolated noncentral seed would need separate empty-condition
support; it is not used here. All other program targets are supplied in
the ready state |+x>. Candidate fuel, if used, lies at its all-even tail
and is unshared.

A program target is enabled by a formed program neighbor. Apply its
supplied ready-state rotation exp(+i theta sigma_y/2),
theta=arcsin(b/(2n)), using all actual neighboring digital Records,
then measure its Z basis. It implements F.
A native candidate is enabled once all FOUR transverse program neighbors
have formed. Its endpoint/fuel neighbors remain unrecorded, so n=4.
Its cycle pulse is U_e=cos(theta/2)I+sin(theta/2)Z_e S_e with
theta=arcsin(b/8), followed by Q_e,z=(I+zZ_e)/2.

On the incoming cycle code each native effect is
p_z P_code, p_z=(1+z sin(theta))/2, and each nonzero branch is
sqrt(p_z) times the fair native nonbridge isometry. All later events
preserve every unused candidate cycle. Program targets are disjoint
from matter; any native controls are older fixed Z Records.
Thus induction, including arbitrary interleaved H_W dwell, proves the
same local F and preserves the COMPLETE protected matter/reference
functional on every supported history. Quartic interactions are included;
no event-count error or free-state assumption enters this induction.

Every new program Record has an older program neighbor; the two seeds
have each other. Every old digital Record therefore keeps at least one
digital neighbor forever, and F gives both projectors positive mass.
A native Record retains its four program neighbors. Hence all old
Records remain supported as well as unchanged. Readiness, code, basis,
roles, occurrence controls and probabilities remain supplied model inputs.
The candidate's four-neighbor prerequisite implies that a program BIRTH
never has an older native candidate Record as a neighbor. Once formed,
its condition can acquire those native neighbors; the same full-multiset
kernel must still support its locked content. This is checked explicitly.

Independent rate-gamma clocks on newly enabled program sites and native
candidates give a concrete supplied occurrence law. Enabled sites are at
most a fixed multiple of the current Record count (12 suffices), so the
linear pure-birth comparison prevents finite-time explosion. Every fixed
program site is reached along a finite path from a seed by a finite sum
of exponential waiting times, almost surely. Every candidate is then
enabled and forms. This is a classical infinite Record law with finite
native window realizations; it does not assume an infinite physical code.

## 5. Parity and the thermodynamic interface: keep both limits honest

The source theorem is on grand-canonical fermionic tori. Native cycle codes
are even-parity and physical finite Z³ windows are open. Neither difference
may be ignored.

For any finite bulk density rho commuting with parity, append one idle
boundary fermion and use
rho_ext=rho_+ tensor |0><0|+rho_- tensor |1><1|.
Its total parity is even and bulk marginal is exactly rho. A protected
idle graph edge keeps the native dictionary connected without adding
a hopping term. This also gives an exact full-Fock Gibbs representation
inside the extended even sector when the bulk Hamiltonian is fixed;
there is one spectator parity state for each bulk state.

A finite physical torus embedding is NOT claimed to have bounded wrap
paths. Instead use finite marginals of the infinite interacting state
provided by the external theorem, with open finite Hamiltonians. For
fixed local observables and bounded real times, the companion
BLOCK03_BOUNDARY_DERIVATION derives the missing-boundary estimate
2 exp(24e|t|-d). Its Poisson smearing gives a fixed-Euclidean-time error
2 exp(24eT-d)+2tau/(pi T). Exact finite checks challenge its actual bond
norms, boundary distance, nonlinear onsite field evolution, parity map,
Poisson residue and growing-program support. These checks do not replace
the analytical infinite-volume argument or external review.

The two-point function is even as a whole, though each charged field is
odd. Its operator/measurement dictionary needs care. An idle ancilla
Majorana g_a gives even CAR representatives b_v=c_v g_a and
b_v*=g_a c_v*: b_v(t)b_w*=c_v(t)c_w*. These have nonlocal shared-ancilla
support; they are not a local charged Record-readout instrument.
At equal times any neutral two-field product has a direct protected-path
representation. The external Euclidean propagator, real-time finite-window
approximation and physical readout must not be conflated.

## 6. Author checks and remaining scope

check_block03.py reconstructs the complete Laurent symbol, routes all its
nonzero terms on a coordinate stencil, and compares native Pauli matrices
with ordinary CAR matrices on the entire finite even code. It checks the
real/imaginary signs, genuinely quartic interaction, counterterm and every
matrix element of the scalar event's interacting intertwiner. It also
computes each cell bond's many-body norm from its finite Fock spectrum.
check_block03_boundary.py checks the exact parity marginal, dressed CAR
fields and neutral correlators, literal two-seed formation and old Record
support, a bent three-cell interacting boundary fixture, graph-chain
counts, the Poisson contour residue and exponential-clock transform.

Two incorrect fixture expectations are preserved in recovery/block03_boundary:
program births cannot have older adjacent candidate Records, and straight
Wilson hopping has W1²=0, so its first distance-two boundary term vanishes.
The corrected bent path has a nonzero distance-two effect. Neither failure
was removed by weakening the stated propagation or support theorem.
The paired JSON files record executed checks and exact runner source hashes.
Neither author checking nor the external RG import is independent review.

The proposed contribution is a bounded native
implementation that can keep forming supported local Records while carrying
an actually interacting theorem-matched Weyl model. The external RG
theorem is an import; this is not a new proof of it, selection from the
framework axioms, or a dynamical gauge/gravity completion.
