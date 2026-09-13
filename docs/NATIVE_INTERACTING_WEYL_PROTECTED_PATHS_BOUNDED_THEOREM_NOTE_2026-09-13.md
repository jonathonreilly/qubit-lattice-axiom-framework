---
claim_id: native_interacting_weyl_protected_paths_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "Given ordinary quantum composition, the supplied native even-CAR code, the specified small-coupling Wilson density-interaction model with its theorem-selected counterterm and state, and the stated controls, two supported seed Records and Born readout, protected native paths of at most three edges implement the interacting model while a single nearest-neighbor content kernel supports continuing nonexplosive Record formation. Finite open native regions approximate fixed local real-time and Euclidean two-point correlations with the stated errors. This is a conditional common-carrier construction; Hamiltonian, state, control and clock selection are additional questions."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_interacting_weyl_2026_09_13.py
---

# Interacting Weyl matter on protected native paths with continuing local Records

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Target and dependency structure

Given the conditions stated below, a finite native edge-qubit implementation
of a specified interacting Weyl model preserves its complete protected matter
functional through growing local Records and approximates its infinite-state
fixed-time correlations with controlled boundary and truncation errors.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Positive native construction and analytical finite-window bounds under explicitly supplied model and instrument premises."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "A common native carrier sustaining continuing supported local Records and controlled interacting Weyl correlations."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Check the physical selection and informative-control obligations exposed by this compatible carrier."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The proof depends on the following objects; none is an inferred empirical
property of the physical world.

| Premise or lemma | Provenance and use | Treatment |
|---|---|---|
| Physical cubic lattice and one-site M2 domain | Current framework axiom memo | Placement/domain only |
| Ordinary tensor quantum composition, Pauli basis, native code | Supplied finite model; algebra in the linked native source | Conditional physical realization |
| Chosen Wilson Hamiltonian, density interaction and counterterm | Specified here; external theorem below | Model parameters and theorem import |
| Protected length-three routes and operator signs | Derived here; Pauli versus CAR check | Author proposal |
| Ready states, selected interacting-state marginals, two seed Records | Specified preparation | Supplied state |
| One global content kernel and its support | Defined and proved here | Conditional local law |
| Rotations, cycle pulses, readout, occurrence clocks and record history | Explicit instrument/control model | Supplied implementation |
| Infinite correlation behavior | Named primary RG theorem with matched hypotheses | Imported mathematical result |
| Finite-region and Poisson approximation | Derived below using even-CAR commutator recursion | Author proof; finite challenges |

The [current framework memo](MINIMAL_AXIOMS_2026-06-29.md) separates
admissibility from Hamiltonian and occurrence selection. This note constructs
one compatible instrument family under its supplied quantum representation;
it does not treat record-free quantum amplitudes as an added framework axiom.
Its quantum states are conditional representations used to calculate the
stated event instruments and correlators.

## Native algebra used in the proof

The required finite dictionary is given by Theorems 1–2 of the
[native edge/CAR source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md).
That source is on the pinned main revision
`b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf`; its conditional theorem is used
with its hypotheses, without assigning an audit grade.
For a connected finite nearest-neighbor virtual graph, put one physical
qubit at each edge midpoint 2v+e_a and fix an oriented neighbor order. Set

    B_v=product_(e incident v) Z_e,
    A_vw=epsilon_vw X_vw product_(u<_v w) Z_vu
                              product_(u<_w v) Z_wu.

The A operators anticommute exactly for distinct edges sharing one vertex,
and with B at their two endpoints. For a cycle C of length l,
S_C=i^l product_ordered A_e is a central Hermitian involution.
The all-positive cycle code represents the even CAR algebra faithfully:
B_v=1-2c_v* c_v and A_vw=-i gamma_(2v)gamma_(2w).
After nonbridge Z_e readout, only surviving cycle checks remain. The map
sqrt(2)Q_e,z from the incoming code is an isometry onto the corresponding
new code and intertwines the complete surviving CAR algebra. Indeed an
incoming cycle anticommutes with Z_e, so P_code Z_e P_code=0; the
surviving algebra commutes with Z_e and both codes have equal dimension.
Every candidate below has a protected detour, hence remains a nonbridge
after any previous candidate deletions. The supplied graph code and
instrument, rather than an occupation-site deletion rule, are the ones used.

## External theorem and hypothesis match

Primary source: Giuliani, Mastropietro and Porta,
[Anomaly non-renormalization in interacting Weyl semimetals, v3](https://arxiv.org/pdf/1907.00682v3),
sections 2.2–2.3, Eq.(2.27), Theorem 2.1. Their theorem supplies an analytic
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
all spatial reflections and orbital exchange.

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
If either coordinate is pi modulo 2pi, c>=1+zeta>0. Otherwise the only
zeros are (0,0,+/-p), p=arccos(zeta). Their velocities are
v1=v2=1 and v3=sin(p)=sqrt(1-zeta²), with quadratic coefficient b0=zeta.
In particular b0>=1/2; the tempting choice zeta=0 would NOT obey the
nonzero quadratic-coefficient hypothesis as stated in this theorem.

For 0<p<=pi/3, p/sin(p) is uniformly bounded, so the separation 2p and
v3 satisfy the uniform comparability condition with c0=3.
The node separation tends to zero as zeta tends to 1. Taylor's theorem
bounds the sine remainder by |k_j|³/6 and the cosine remainder at a node
by |delta_k3|³/6. The transverse cosine terms are bounded by
(k1²+k2²)/2. These give the source's local remainder bounds uniformly.
Away from both node neighborhoods, compactness in the CLOSED parameter
interval [1/2,1] gives a positive determinant lower bound; at zeta=1
the only additional limiting zero is the merged node at the origin,
already excluded from that region. The untilted scalar term d is zero.
The complementary-region quadratic remainder is also controlled:
outside distance 2p from the nodes, |k|>p and
1-zeta=1-cos(p)<=p²/2<=|k|²/2.

For any fixed zeta, such as 1/2, the source theorem now supplies lambda0>0,
an analytic nu with nu(0)=0, and the interacting zero-temperature
two-point function with the Weyl singularity of Eq.(2.27) for
|lambda|<=lambda0. Z=1+O(lambda), v_j=v_j0(1+O(lambda)); its relative
remainder is O(|k-p_node|^theta), every fixed 0<theta<1.
The selected strengths and analytic counterterm are model data. No
numerical value of nu or lambda0, isotropic dressed speed, interacting
star coefficient or emergent dynamical gauge field has been computed.

## Place both orbitals on the virtual lattice

Let model orbital r=0,1 at cell n be virtual vertex

    v(n,r)=(2n1+r,n2,n3).

This is a bijection onto Z³. Use the candidate matching defined here:
a y bond is a candidate exactly when its tail x+y is odd. All x,z bonds
and the alternating y bonds are protected. A candidate's +x plaquette
detour is entirely protected. The physical native edge factors remain
at midpoints 2v+e_a; this orbital map does not put two qubits at one site.

Every nonzero offsite matrix element of h0 connects orbitals in neighboring
MODEL cells. The required virtual displacements are:

- same orbital, x-cell neighbor: +/-2e_x;
- same orbital, y or z neighbor: +/-e_y or +/-e_z;
- different orbitals, x-cell neighbor: +/-e_x or +/-3e_x;
- different orbitals, y-cell neighbor: +/-e_x+/-e_y.

All admit a simple protected path of length at most 3.
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

## Native protected path identities

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

Each path of length at most 3 uses only the native stars of at most 4
vertices. On the cubic graph their union has at most
6(l+1)-l=5l+6<=21 edge factors. All lie within physical Manhattan distance
at most 7 of the starting physical vertex 2v. Endpoint B factors add no
sites outside this union. This is bounded physical support, not a supplied
synthesis into two-site gates or an admissibility derivation from H.

Every A_p has X support only on protected edges. Hence T_p,J_p,B_v,
the density interaction and the complete native H_W commute with every
candidate Z and every native cycle. The changing CAR dictionary after
Record deletion intertwines the same full interacting Hamiltonian.

## Global content kernel and continuing formation

For the complete finite multiset eta of neighboring M2 contents define

    F(eta)=average_(a in eta)[(3/4)delta_a+(1/4)delta_(I-a)],
    F(empty)=delta_0.

It is a normalized nonnegative Borel kernel on ALL conditions. It is
covariant under lattice translations/proper rotations and algebraic
similarity/conjugation. Its values vary with eta. Restrict its realization
to supplied digital projectors P and I-P. With n>0 neighbors and sign
sum b, its plus probability is 1/2+b/(4n), always in [1/4,3/4].

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

## Parity and the thermodynamic interface

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
finite-window argument below derives the missing-boundary estimate
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

## Author checks and scope

The primary runner's model calculation reconstructs the complete Laurent symbol, routes all its
nonzero terms on a coordinate stencil, and compares native Pauli matrices
with ordinary CAR matrices on the entire finite even code. It checks the
real/imaginary signs, genuinely quartic interaction, counterterm and every
matrix element of the scalar event's interacting intertwiner. It also
computes each cell bond's many-body norm from its finite Fock spectrum.
Its boundary calculation checks the exact parity marginal, dressed CAR
fields and neutral correlators, literal two-seed formation and old Record
support, a bent three-cell interacting boundary fixture, graph-chain
counts, the Poisson contour residue and exponential-clock transform.

Two incorrect fixture expectations are preserved in the committed failure-recovery packet:
program births cannot have older adjacent candidate Records, and straight
Wilson hopping has W1²=0, so its first distance-two boundary term vanishes.
The corrected bent path has a nonzero distance-two effect. Neither failure
was removed by weakening the stated propagation or support theorem.
The emitted receipt records executed checks and the runner source hash.
Neither author checking nor the external RG import is independent review.

The proposed contribution is a bounded native
implementation that can keep forming supported local Records while carrying
an actually interacting theorem-matched Weyl model. The external RG
theorem is an import; this is not a new proof of it, selection from the
framework axioms, or a dynamical gauge/gravity completion.

## Cell interaction norms

For the selected t1=t2=1 Wilson symbol, the oriented neighboring-cell
coefficient matrices, using h(k)=sum_delta h_delta exp(-ik.delta), are

    W1=(-sigma3+i sigma1)/2,
    W2=(-sigma3+i sigma2)/2,
    W3=-sigma3/2.

Each has trace norm 1. The first two have singular values 1,0; the third
has 1/2,1/2. The bond Fock operator
c_n* W_a c_(n+e_a)+h.c. therefore has norm 1: diagonalizing its one-particle
block gives paired singular values, and its largest many-body energy is
their positive sum. This is a norm of the actual bond, not a coefficient
count proxy.

All interaction and counterterm terms are onsite in MODEL-cell space,
whose local Fock dimension is four. Passing to their product onsite
interaction picture leaves every cell-bond term even, on the same two
cells, and norm 1. Consequently the following propagation estimate has
no hidden volume factor or onsite-interaction norm in its velocity.
The onsite Hamiltonian is bounded per cell, so that interaction picture
exists on every local observable, uniformly in the finite volume.

## A coarse boundary estimate

Let Lambda be an open model-cell box, x in Lambda, and
d=dist_Z3(x,Lambda_complement). Let tau^Lambda_t and tau_t be finite and
infinite dynamics for (3.1). For any unit-norm operator A supported in
cell x, including an odd field, the bound is

    ||tau^Lambda_t(A)-tau_t(A)||
       <=2 sum_(n>=d) (24|t|)^n/n!
       <=2 exp(24e|t|-d).                              (B.1)

A proof must retain the support-chain resummation; a naive unrestricted
nested-commutator count would introduce spurious factorials.

The time-dependent even-CAR commutator recursion is the one in
[Nachtergaele, Sims and Young, v3](https://arxiv.org/pdf/1705.08553v3),
Lemma3.3 and Eqs.(3.28)–(3.31), whose statement and proof were read.
Here there are two fermion labels per cell, norm-continuous even finite-range
terms, and the comparison boundary operator is even. Its disjoint commutator
therefore vanishes even when A is odd. The specialized bond counting below
derives our constants; no numerical velocity is imported from that paper.

In the onsite interaction picture, the standard commutator differential
inequality iterates over chains of bonds with consecutive intersections.
Its n-fold time-ordered integral is |t|^n/n!, and each commutator costs
a factor 2 times the bond norm. An initial cell meets 6 bonds; a bond meets
at most 11 bonds, including itself. In the Duhamel difference of the two
dynamics the final bond crosses the boundary. Every such chain has at
least d bonds. Summing boundary bonds inside the chain count, rather
than multiplying by the boundary area afterwards, gives at most
6*11^(n-1) chains, each contributing at most(2|t|)^n/n! after the
Duhamel integration. Their bound is no larger than the deliberately looser
2*12^n count used in(B.1). The same argument works for an odd A because
the Hamiltonian terms are even and commute with disjoint odd observables.
The time-dependent interaction-picture terms have the same norms.
For the last inequality, use1_(n>=d)<=exp(n-d) in the exponential series.

For a finite observable support X, replace the right side by |X| times
it and let d be the minimum boundary distance. This is only a finite-time
comparison, not a norm bound uniform as time tends to infinity.

## State restriction and neutral correlators

Let omega be the infinite interacting state supplied by the primary theorem.
Take its exact finite marginal rho_Lambda, and extend its parity by the
one idle boundary fermion. The native even-sector state has exactly that
bulk marginal. For y also in Lambda, the finite real-time neutral function

    f_Lambda(t)=Tr rho_Lambda tau^Lambda_t(c_x) c_y*

is represented by an even native observable. Its infinite counterpart is
f(t)=omega(tau_t(c_x)c_y*), and(B.1) implies
|f_Lambda(t)-f(t)|<=2 exp(24e|t|-d).
The rho_Lambda used here is a marginal of omega, not claimed to be the
Gibbs state of the open Hamiltonian. Preparation remains supplied.
Using the dressed fields c_x g_ancilla makes the full finite CAR matrix
representation explicit, but does not create a local charged readout.

## Recovering a fixed Euclidean correlator

The infinite ground-state GNS generator is nonnegative. Therefore the
positive-time Euclidean two-point function can be recovered by the Poisson
smearing of its real-time function:

    G(tau)=integral_R P_tau(t) f(t) dt,
    P_tau(t)=tau/[pi(t²+tau²)], tau>0.

Indeed Fourier transformation of P_tau gives exp(-tau|omega|), which
equals exp(-tau omega) on the nonnegative ground-state spectral support.
The spectral theorem justifies the identity also for the complex
cross-spectral measure of distinct fields. The norm bound |f(t)|<=1
is sufficient for the tail estimate.

The ground-state input can be obtained without assuming a unique full
infinite state. Finite Gibbs states have weak-* accumulation points on the
quasi-local CAR algebra. The boundary bound supplies the limiting local
dynamics. For any local B, define its positive spectral measure by
omega_beta(tau_t(B*) B)=integral exp(-itE) dmu_(B,beta)(E).
It has total mass at most ||B||². The finite-volume trace identity exchanges
the two matrix elements and gives
mu_(B,beta)((-infinity,-a])<=exp(-beta*a)||B||² for every a>0,
using the reversed B* measure on the positive side. This estimate is
uniform in volume. A uniform second-moment bound follows from the finite
local norm of [H,B], ensuring tightness of these measures. After the
volume limit followed by beta to infinity,
every weak spectral limit has support in [0,infinity). Thus the cyclic
GNS generator is nonnegative. The local weak-* subsequence may be chosen
first; the unique two-point limit provided by the imported theorem fixes
the correlations used here, even if other observables have several
accumulation limits. No full-state uniqueness is inferred from a two-point
theorem. The finite Gibbs states conserve number, so their finite
marginals and limits commute with parity as required above.

For fixed tau>0 the finite-temperature Euclidean autocorrelation is the
same spectral integral with exp(-tau E). Its negative-energy tail below
-a is bounded by exp(-(beta-tau)*a)||B||² for beta>tau, by the same trace
identity. The interval [-a,0] is controlled by continuity, then a tends
to zero. The nonnegative-energy multiplier is bounded. This identifies
the imported fixed-time Euclidean limit with the ground-state spectral
integral used here; complex cross-correlations follow by polarization.

For clarity the Poisson Fourier identity follows directly by a contour
integral: for energy E>0, integrate exp(-itE) tau/[pi(t²+tau²)] in the
lower half-plane. Its pole at -i tau and clockwise orientation give
exp(-tau E). E<0 uses the upper half-plane; E=0 is normalization. The
spectral theorem then applies this scalar identity to the nonnegative
generator. This is not an assumed Wick rotation of the open marginal.

Define the FINITE observable
G_(Lambda,T)(tau)=integral_(-T)^T P_tau(t) f_Lambda(t) dt.
It is not the open marginal's own imaginary-time Gibbs correlator.
The explicit comparison is

    |G_(Lambda,T)(tau)-G(tau)|
       <=2 exp(24eT-d)+2tau/(pi T).                    (B.2)

The second term bounds the omitted Cauchy-kernel tail. For 0<epsilon<1,
choose T>=4tau/(pi epsilon) and d>=24eT+log(4/epsilon); then the error
is at most epsilon. Negative Euclidean times use the reversed occupied
correlator and its fermionic sign. Equal time is already a marginal identity.

This transfers FIXED-time correlators of the theorem-matched interacting
model to finite native protected observables. The continuum infrared
asymptotic is taken only after this finite-window approximation converges.
It gives no uniform finite-resource limit all the way to zero energy.

## Containing the growing Record process

For the two-seed program process, each program vertex has degree at most 6.
A simple length-n path from a seed with no other seed in its interior
has a sum of n independent exponential waiting times. For a union bound on unusually fast arrival,
an actual arrival by T implies SOME simple path whose sum is at most T.
Markov's inequality for exp(-11gamma sum E) gives

    Pr(sum_(j=1)^n E_j<=T)<=exp(11gamma T) 12^-n.

From two seeds there are at most 2*6^n candidate paths. Thus the probability
of reaching program graph distance at least D by T is at most

    2^(2-D) exp(11gamma T).                             (B.3)

All newly formed native sites are adjacent to already formed program sites.
A program window with D>=(11gamma T+log(4/epsilon))/log2, with a fixed
one-site native margin, therefore couples to the infinite Record process
up to time T except on an event of probability at most epsilon.
This is a stated probability error, not a pathwise bound for all clocks.

Combining the model-cell matter margin with its physical embedding and this
program margin gives finite site resources of order
(R+T+gamma T+log(1/epsilon))³, with T itself scaling as tau/epsilon in(B.2).
The native paths have length at most 3 and fixed star support, and there
is one parity spectator. Optional collision storage/control is additional.
The one-site margin above contains Record LOCATIONS. Finite physical
operators also require a fixed outer margin for their cycle/star support;
seven additional physical lattice steps suffice with the chosen routes.
Boundary candidates whose protected plaquette is incomplete are not enabled.
The coupling region is chosen inside this margin, so that this convention
does not affect the comparison on the stated no-escape event.
No rate, clock, infinite state or preparation procedure is derived.

The author checked the support-chain coefficient and Fourier/path conventions
against the written derivation and the finite runner. This is a proposed
analytical result with independent review pending.


## Reproduction and review record

The [primary runner](../scripts/native_interacting_weyl_2026_09_13.py) contains
both finite checking implementations, so no external helper registration is
required. Its [machine cache](../logs/runner-cache/native_interacting_weyl_2026_09_13.txt)
is produced by the repository cache envelope; its detailed
[receipt](../outputs/native_interacting_weyl_2026_09_13.json) includes the
actual growth prefix. It reads no ancestral scientific data at runtime;
its self-hash is a package-local integrity read, and the envelope binds the
listed source-note inputs. The analytical argument supplies the infinite
quantifiers; the finite runner is a falsification check, not their proof.
The [author review and recovery record](../.claude/science/physics-loops/native-interacting-weyl-20260913/REVIEW_HISTORY.md)
records source identity, failed fixture expectations and mutation evidence.

The strongest downstream obligation is to derive or explicitly select the
Hamiltonian, state and controls in the framework, including an informative
local readout when that is the intended physical interpretation. This note
asserts no impossibility for those obligations and no necessity of an axiom
update. It imports the existing small-coupling RG theorem and supplies a
common native implementation; it establishes neither a new RG theorem nor
a full TOE, dynamical photon or gravity theory. Independent review and the
later independent audit remain pending.
