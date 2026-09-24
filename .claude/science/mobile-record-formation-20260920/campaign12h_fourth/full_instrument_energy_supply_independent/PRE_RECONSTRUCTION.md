# Finite positive energy supply for a complete marked operation

Independent PRE reconstruction, 2026-09-24. This packet precedes exposure to
`full_instrument_energy_supply_author`, `coherent_energy_supply_author`, the
current campaign checkpoint, and the external autonomous-reservoir work.
It is a conditional mathematical construction and independent control, not an
audit verdict, physical selection, autonomous-reservoir derivation, or adoption
of an energy-accounting axiom. Source identities are in `SOURCE_MANIFEST.json`.

## 1. Question and result

For a finite-dimensional system with a prescribed finite marked quantum
instrument, a finite positive reservoir can approximate the complete operation
uniformly for every input, including inputs entangled with an arbitrary
reference. The construction uses a prepared coherent reservoir and zero-energy
ancillas/flags. Its unitary preserves the sum of the specified system and
reservoir free Hamiltonians exactly. Both ends of the reservoir spectrum are
finite, and no cyclic energy wrap is used.

An integer energy grid admits a single ladder. Commensurate gaps are **not
necessary**: a product of finitely many positive ladders gives a construction
for every finite spectrum, with a different dimension cost. The arbitrary
spectrum construction and its bound below were obtained before reading the
new target author packets.

For a sequence of operations on the **same bounded system**, all zero-energy
flags and hidden dilation ancillas can be included from the beginning. The
same reservoir is then reused with its actual correlations. A blockwise
composition identity bounds the complete discrete flag history without
assuming a reset, a product state after a step, or statistical independence.

For a bounded GKLS generator, an explicitly completely positive marked step
converges to its reduced channel with an explicit finite-time error. Combining
the two constructions also controls any fixed number of energy moments when
the accuracy is scaled with the microscopic Hamiltonian norm. This is a
scheduled finite-gate construction for each requested precision; it does not
construct a single autonomous continuous-time environment or identify the
exact event-time path instrument.

## 2. Premises and norms

Let S be finite dimensional. A finite marked instrument is described by
operators K_(a,b) with sum_(a,b) K_(a,b)^dagger K_(a,b)=I. The reported mark is
a and b is an unreported finite Kraus index. A trace-decreasing operation is
included by adding its complementary failure operation. Infinitely many
distinct classical outcomes are outside the finite-flag statement here.

Use a finite ancillary space F, initially in a specified pure state |0>, and
a unitary U on A=S tensor F whose isometry on this initial subspace is

    |psi>|0> -> sum_(a,b) K_(a,b)|psi>|a,b>.

Finite isometries admit a unitary completion by completing orthonormal bases.
All flags and ancillary degrees of freedom have Hamiltonian zero. Copying a
mark to another zero-energy pointer and tracing/dephasing it gives the desired
classical record; this final operation is contractive for the norms used here.
For a fully unitary description the extra pointers can simply be retained.

All channel errors below use the full diamond norm, with maximum 2 for the
difference of channels. State errors use the full trace norm, not one half of
it. Statements uniform over references follow from operator-norm bounds on
Stinespring isometries, not from the sampled entangled-state controls alone.
For isometries V and W with common output space,

    ||V(.)V^dagger - W(.)W^dagger||_diamond <= 2 ||V-W||.

This follows by expanding the difference into two terms, using norm-one
isometries, and the ideal property of trace norm, including after tensoring
an arbitrary identity. It also bounds the channels after partial trace or
classical flag readout.

Prepared coherence, finite pure zero-energy memories, and the choice/scheduling
of the gates are explicit supplied resources. The theorem does not prepare
these resources from an incoherent energy source.

## 3. One finite ladder for an integer grid

Assume H_A=omega sum_(m=0)^d m P_m, omega>0, where absent levels are allowed
and the projectors include the zero-energy flags. Set L>=1 and

    M=2d+L-1,
    H_R=omega sum_(n=0)^M n |n><n|,
    dim R=2d+L.

Prepare the normalized finite sine profile

    |eta>=sqrt(2/(L+1)) sum_(k=0)^(L-1)
           sin(pi(k+1)/(L+1)) |d+k>.

Its mean reservoir energy is omega[d+(L-1)/2]=omega M/2; its maximum energy
is omega M. H_R is nonnegative. If strictly positive definite H_R is desired,
add a fixed positive scalar times I; this does not affect any commutator,
channel, or energy change, and adds that scalar to the initial supply.

For every total integer energy q in [d,M], the q sector contains a full copy
of A under the isometry

    J_q |m,alpha> = |m,alpha>|q-m>.

The finite bounds follow from 0<=m<=d and d<=q<=M. Define V_R(U) on this
sector as J_q U J_q^dagger. Define it as the identity on every remaining
total-energy sector, q<d or q>M. This is a unitary on the entire finite tensor
product, including both incomplete boundaries, and

    [V_R(U), H_A+H_R]=0.                                  (3.1)

For every input on A and the stated reservoir preparation, the occupied q
sectors lie in [d,M]: n lies in [d,d+L-1] and q=n+m. Thus only the copied-U
blocks are used. This support statement also holds with an entangled
reference and coherent superpositions of system energies.

For the error proof only, embed the finite ladder in the bilateral integer
ladder and write Delta|n>=|n+1>. The physical reservoir remains the finite
one just defined. On the accessible subspace,

    V_R(U) = D (U tensor I) D^dagger,
    D = sum_m P_m tensor Delta^(-m).

The sine recurrence and its zero endpoints give

    <eta|Delta|eta>=cos(pi/(L+1)),
    c_L := ||Delta eta-eta|| = 2 sin(pi/[2(L+1)])
                              <= pi/(L+1).

By telescoping the unitary shifts, ||Delta^m eta-eta||<=|m| c_L. Let
J_eta:psi->psi tensor eta. Orthogonality of the P_m gives

    ||D^dagger J_eta-J_eta|| <= d c_L,
    ||D J_eta-J_eta|| <= d c_L.

Insert and subtract D(U tensor I)J_eta to obtain

    ||V_R(U)J_eta-J_eta U|| <= 2d c_L.                    (3.2)

Consequently the complete joint channel, including the reservoir compared
with the unchanged product eta and including any external reference, differs
from the ideal unitary channel by at most

    beta_grid = min(2,4d c_L) <= min(2,4pi d/(L+1)).       (3.3)

The same bound applies to the marked instrument after preparing and reading
F. It is independent of the degeneracy, dimension, and particular U. For
desired error beta>0, L+1>=4pi d/beta suffices. If d=0, U already preserves
the free Hamiltonian and no nontrivial reservoir is needed.

## 4. Arbitrary finite spectra: no commensurability premise

Let the distinct positive system energies above the minimum be e_1,...,e_r,
with spectral projectors P_1,...,P_r and ground projector P_0. A global scalar
shift of a finite Hamiltonian to minimum zero leaves both dynamics and all
energy changes unchanged. This is not a particle-number-dependent shift.
Extend each projector by identity on all zero-energy flags.

For each i use a finite ladder n_i=0,...,L+1. Define

    R = tensor_(i=1)^r R_i,         dim R=(L+2)^r,
    H_R=sum_i e_i N_i,
    Q_i=N_i+P_i.

The commuting Q_i are auxiliary vector charges. Their weighted sum is exactly
H_A+H_R. Label a ground system state by k_0=0 and an energy-e_i state by the
ith unit vector k_i. For every vector q in {1,...,L+1}^r, the sector Q=q is
a full copy of A: the reservoir vector is n=q-k_i. Copy U onto each of these
complete vector-charge sectors and use identity on every other sector. This
defines a finite unitary preserving **each** Q_i and therefore H_A+H_R.
Degeneracies or rational relations among the e_i create no obstruction; it
is permissible to preserve these finer charges inside a scalar-energy
degeneracy. Exact commensurability is nowhere assumed.

Prepare the product of sine profiles, each supported on n_i=1,...,L:

    eta = tensor_i [sqrt(2/(L+1)) sum_(n=1)^L
                         sin(pi n/(L+1)) |n>].

For any input system energy label, every occupied Q_i lies in [1,L+1]. On
this accessible subspace the bilateral proof lift is

    D=sum_(a=0)^r P_a tensor Delta^(-k_a).

Each k_a moves at most one coordinate by one unit. Hence orthogonality of
the system projectors gives

    ||D^dagger J_eta-J_eta|| <= c_L,
    ||D J_eta-J_eta|| <= c_L,
    ||V_R(U)J_eta-J_eta U|| <= 2c_L,
    beta_vector = min(2,4c_L) <= min(2,4pi/(L+1)).        (4.1)

There is no factor r in this bound. The resource cost does depend strongly
on r through dimension and energy:

    mean(H_R)=(L+1)/2 sum_i e_i,
    max(H_R)=(L+1) sum_i e_i.                            (4.2)

This is a finite construction for every fixed finite spectrum and precision,
even for irrational energy ratios. It is not asserted to optimize any
resource. The one-ladder construction can be much smaller when an integer
grid is available. Exact knowledge/control of the supplied spectral energies
is part of an exact conservation construction; robustness to implementation
errors in those energies is a different question.

## 5. Same reservoir, complete discrete flag history

Consider N prescribed marked operations on the same S, with fresh finite
zero-energy dilation spaces F_1,...,F_N initially prepared once. Enlarge
A=S tensor F_1 tensor ... tensor F_N before constructing the lift. Its
system energy span and distinct positive levels have not increased. Let U_k
be the kth unitary acting on S and its flag, and possibly controlled on
earlier recorded flags. The physical lifts all use the same finite reservoir,
same complete sectors, and same identity boundary completion.

On every complete block these are ordinary matrix copies. On every
incomplete block all are identities. Therefore the global exact identity is

    V_R(U_N) ... V_R(U_1) = V_R(U_N ... U_1).             (5.1)

Applying (3.2) or (4.1) once to the product U_N...U_1 proves the same beta
bound for the entire output S, all flags, the reservoir, and an arbitrary
reference. There is no sum of N reservoir errors. The actual intermediate
reservoir may be mixed and correlated with S and earlier flags. Although its
marginal support can reach a ladder boundary, the conserved total-energy or
vector-charge label stays in the complete sector. Reapplying a single-step
argument to a supposedly fresh reservoir marginal would be unjustified;
(5.1) avoids that assumption.

For classical histories, previous flags must be left intact by later gates
except as classical controls. Dephasing/copying those flags can then be
deferred to the end; controlled gates commute with that dephasing. This gives
the full joint distribution of finite discrete marks together with their
unnormalized conditional system outputs. If later gates coherently erase or
mix earlier outcomes, the theorem still approximates that coherent circuit,
but it is not the same prescribed classical-history instrument.

The history statement is uniform before conditioning. For a particular ideal
history of probability p>0, the normalized conditional-state error is at most
2 beta/p when the corresponding actual probability is nonzero. In particular
beta<p suffices for nonzero probability. There is no uniform normalized
rare-history bound as p tends to zero.

Finite memory is accounted for explicitly. A conservative total environment
dimension is dim(R) times product_k dim(F_k), enlarged by any readout pointers.
No ancilla is reset during the process. The zero-energy purity and memory
space are supplied even though they do not enter the free-energy sum. As N
grows without bound, this conservative construction has no fixed finite
memory limit. A sequence on N different energetic output systems also has
a larger joint energetic spectrum; the fixed-span bound cannot be quoted
while ignoring those systems' retained energies.

## 6. An explicitly CP marked approximation to bounded GKLS dynamics

Let the specified generator on finite S be

    L(rho)=-i[H,rho]+sum_j (L_j rho L_j^dagger
                           -{L_j^dagger L_j,rho}/2),
    Gamma=sum_j L_j^dagger L_j,
    h=||H||,       gamma=||Gamma||.

For step size tau with tau gamma<=1, define the marked Kraus operators

    K_0=exp(-i H tau) sqrt(I-tau Gamma),
    K_j=exp(-i H tau) sqrt(tau) L_j.                     (6.1)

Their completeness relation is exactly I, so this defines a CPTP marked
step Phi_tau. It retains the prescribed L_j at leading order, including
their coherent output amplitudes and mark labels. It is a discretization,
not an assertion that (6.1) equals an exact finite-bin trajectory instrument.

Here is a dimension-independent bound with explicit constants. Write
A=-i[H,.], D=L-A, and let Psi_tau be (6.1) before the Hamiltonian unitary.
Set B=I-sqrt(I-tau Gamma). Since tau Gamma=2B-B^2, direct expansion gives
the exact superoperator identity

    Psi_tau-(I+tau D) = D[B],
    D[B](rho)=B rho B-{B^2,rho}/2.                      (6.2)

For 0<=tau Gamma<=I, ||B||<=tau gamma, so the diamond norm of (6.2) is
at most 2 tau^2 gamma^2. The completely positive recycling map
rho->sum L_j rho L_j^dagger has diamond norm ||Gamma||, and each left/right
multiplication in the loss has its usual operator-norm bound. Thus
||D||_diamond<=2gamma. Using the integral Taylor remainder and the channel
contractivity of exp(sD),

    ||exp(tau D)-I-tau D||_diamond <= 2tau^2 gamma^2,
    ||Psi_tau-exp(tau D)||_diamond <= 4tau^2 gamma^2.

For completeness, differentiating
exp((tau-s)(A+D)) exp(sA) exp(sD), and expanding [exp(sA),D] as an integral
of exp(uA)[A,D]exp(vA), involves only nonnegative-time channels around the
commutator. Its norm is therefore bounded by tau^2||[A,D]||/2. Because
||A||_diamond<=2h and ||D||_diamond<=2gamma,

    ||exp(tau A)exp(tau D)-exp(tau L)||_diamond
              <= 4h gamma tau^2.

Combining the two estimates yields

    ||Phi_tau-exp(tau L)||_diamond
              <= 4gamma(h+gamma)tau^2.                 (6.3)

No assumption tau h<=1 is needed for this bound. CPTP telescoping for
T=N tau gives

    ||Phi_tau^N-exp(T L)||_diamond
              <= 4T tau gamma(h+gamma)
               = 4T^2 gamma(h+gamma)/N.                (6.4)

The same bound with T replaced by a smaller grid time holds at each prefix.
A last shorter step handles a fixed off-grid time; sum tau_k^2<=T max tau_k.
The case gamma=0 is exact unitary evolution and requires no dissipative-step
error estimate.

Complete the isometry of (6.1) to a finite unitary with zero-energy flags,
and apply the reservoir construction to the N dilations together. Keeping
the same reservoir gives error beta for their full **discrete** history.
After the flags and reservoir are discarded, (6.4) gives

    ||implemented reduced channel - exp(T L)||_diamond
          <= eta := beta+4T^2 gamma(h+gamma)/N.         (6.5)

The continuous-time statement proved here is for the reduced channel, with
all input/reference states included. Proving convergence to the exact
continuous-time event-time instrument requires a specified path space,
timing/readout convention and additional argument; no equality of that
instrument is inferred from (6.5). The exact finite discrete history bound
and the reduced continuous-time bound are separate statements.

## 7. Energy moments and explicit precision choices

For output states with trace-norm difference at most eta and bounded H,

    |difference of mean(H)| <= h eta,
    |difference of raw moment(H^p)| <= h^p eta,
    |difference of Var(H)| <= 3h^2 eta.                (7.1)

The variance estimate uses the second-moment bound and
|a^2-b^2|<=2h|a-b| for means of states. The bounds also apply to bounded
observables on a reference-extended output. They are not uniform under
h->infinity unless eta is tightened accordingly.

For desired channel accuracy eta_*>0 at fixed T, it suffices to choose

    N >= max(1, T gamma, 8T^2 gamma(h+gamma)/eta_*),
    beta <= eta_*/2,
    L+1 >= 8pi d/eta_*     [one integer ladder],
or  L+1 >= 8pi/eta_*       [r vector ladders].          (7.2)

Take integer ceilings as needed. For an absolute first-moment tolerance a,
require eta_*<=a/h; for an absolute pth raw-moment tolerance b, require
eta_*<=b/h^p. Formula (7.2) is a sufficient finite resource prescription,
not an optimal one. It explicitly includes full preparation, memory, and
external gate scheduling in addition to energy supply.

## 8. Application to the unchanged complete microscopic compensated star

The two released, already independently checked microscopic star notes are
used as premises. Their complete argument and final independent comparison
were read; their source bytes and all 50 artifacts in the prior final seal
were authenticated. The older builders are not imported. The control here
also independently reconstructs the complete star matrices directly from
the primitive charge/transport/creation rules.

On A={0}, B={1,2,3}, Gauss law fixes E_0b=-q_b and sum q=1. The sixteen
physical charge words comprise four one-record states and twelve three-record
states. Every allowed normalized spin step between fields 0 and +/-1 has
coefficient one for integer S>=1. With W the empty-A projector and F the
outward transport, the supplied lambda=0 compensated Hamiltonian is

    H=delta epsilon^-4 (W-epsilon F)^dagger(W-epsilon F).

The original resolved jumps are L_(b,sigma)=sqrt(kappa)/epsilon j_(b,sigma).
For the original coherent-edge alternative, keep the specified coherent sum
inside each jump. Neither instrument is replaced by a different energy
filter. The complete spectra and loss norms are

    spec(H) = {0 [mult 10], delta epsilon^-4 [mult 2],
               delta epsilon^-4(1+3epsilon^2) [mult 4]},
    ||sum_j L_j^dagger L_j||=4kappa/epsilon^2.

These are full-space norms, not restrictions to the dressed initial ray.
The at-most-one-birth fact is useful for the existing exact energy result,
but the CP approximation theorem does not rely on it.

For the explicitly chosen sequence

    C=S(S+1),   delta=K>0,   epsilon^2=1/C,

the spectrum is on the integer grid of spacing K, with

    d=C(C+3),   h=K C(C+3),   gamma=4kappa C.            (8.1)

Thus (7.2) constructs a genuinely finite reservoir/dilation for every S and
finite T. Alternatively, the two positive energies can be used in the
arbitrary-spectrum construction. For more general positive delta,epsilon,
the ratio of the two positive levels need not be rational; section 4 still
applies without approximating or replacing those energies.

For an explicit joint microscopic/resource limit, set eta_*=C^-6. With fixed
T,K,kappa choose the integer ceilings in (7.2). Then

    N=O(C^9),
    L=O(C^8) and dim R=O(C^8) for the integer ladder,
    mean(H_R)=O(K C^8),
    implemented channel error <= C^-6,
    absolute first-moment error = O(C^-4),
    absolute second-moment and variance errors = O(C^-2).

The one-step zero-energy flag space has dimension 7 for six resolved jumps
plus no-jump, or dimension 4 for the coherent-edge version. A conservative
unreset flag space is respectively 7^N or 4^N, plus any retained readout
pointers. These large but finite resources are counted rather than silently
assumed absent. The alternative two-ladder choice has L=O(C^6), battery
dimension O(C^12), and the same O(K C^8) upper bound on mean energy. Neither
resource scaling is claimed sharp.

For the exactly dressed zero-energy initial state, the checked prior result
gives

    mean(H)_GKLS(t)/C -> (3K/2)(1-exp(-12kappa t))

at every fixed t>0. Since the present construction controls the microscopic
energy expectation itself, it reproduces this mean with vanishing absolute
error under the displayed precision scaling. Exact free-energy conservation
and H_R>=0 then entail for the implemented state

    mean(H_R initial) >= mean(H implemented at t)
                      >= mean(H GKLS at t)-h eta.

This is compatible with the prior necessary O(C) supply lower bound. The
construction uses a much larger sufficient resource and does not establish
the optimal bill. It also does not transfer energy expectations merely from
the earlier slow-density convergence theorem.

## 9. Boundaries, rejected routes, and attribution

1. A finite cyclic shift is unitary but wraps the energy at its seam and does
   not implement an exact energy translation. The exact complete-block
   construction uses identity on incomplete sectors instead. The control
   detects the cyclic-shift translation-identity defect.
2. A fresh-reservoir or product-state assumption after each mark would ignore
   actual correlations. The control exhibits a mixed reservoir after the
   first gate; composition (5.1), not a reset assumption, proves the bound.
3. Supplying only an energy-diagonal reservoir is insufficient for arbitrary
   coherence-generating target operations under the stated symmetry. The
   theorem deliberately supplies a coherent sine preparation. It does not
   derive its preparation or select that resource physically.
4. The naive Euler map I+tau L is not generally CP. An amplitude-damping
   negative control has a negative Choi eigenvalue. The square-root Kraus
   step (6.1) avoids this defect.
5. A fixed trace-distance accuracy does not control a growing microscopic
   energy. The H-dependent estimates in (7.1) are necessary to state the
   claimed moment approximation. Rare normalized histories need their own
   probability denominator.
6. All gates conserve the specified **free** sum. This permits a scheduled
   implementation; it does not derive the energy cost or autonomy of the
   switching apparatus, clock, initial coherent preparation, or fresh pure
   memories. Each finite gate has a commuting Hermitian logarithm, but the
   existence of such separate generators does not produce one fixed local,
   autonomous, time-independent reservoir realizing the prescribed GKLS
   semigroup and exact marked path law. No such claim is made.

The translation-lift mechanism and its multiplicative property have a
standard antecedent in Johan Åberg, *Catalytic Coherence*, arXiv:1304.1060v3,
Appendix B, especially Lemma 2 and equations (B4)-(B6), and the discussion of
time control and lower boundaries in Appendices B/D. Primary source:
https://arxiv.org/abs/1304.1060. A versioned PDF is bound in this packet. The
fully finite two-boundary construction, the sine-profile constants, the
vector-charge finite-spectrum extension, and their use in (6.5)-(8.1) are
derived explicitly here; no error constant is imported from the paper.

## 10. Evidence and disposition before author comparison

`control.py` is a standalone reconstruction with portable adjacent source
lookup before an absolute fallback. It imports no existing model builder.
Its exact rational matrix controls prove, by exact equality in two small
models, unitarity, conserved charge labels and repeated-lift composition.
One uses levels {0,2}; the other uses vector labels for {0,1,sqrt(2)}.
These checks do not replace the general proofs above.

Numerical controls cover twelve integer-ladder cases, three incommensurate
two-ladder cases, a same-reservoir two-gate history with an entangled reference,
and nine complete sixteen-state star CP discretizations using its full
256-dimensional Liouvillian. The history test has reservoir purity
0.9735652323 after the first operation and nonzero system/flags-reservoir
correlation trace norm 0.2563647336. Its complete classical history error is
0.01833562981, below the uniform bound 0.5707134656. The exact block product
identity has zero matrix error in that test.

Every completed control assertion passes in `CONTROL_RESULTS_02.json`.
The first run failed at Python parsing because of one extra closing bracket;
its code snapshot, stderr and receipt are preserved. It produced no science
result. The completed run takes about 0.83 seconds on the recorded host. Full
outputs and explicit numerical thresholds are saved. The normalized Choi
tests are actual entangled-input checks, not numerical diamond-norm proofs.

PRE conclusion: a concrete positive answer exists under the stated finite
system, finite instrument, prepared-coherence, zero-energy-memory and external
control premises. Commensurate gaps are optional. The same finite reservoir
can be used for a finite sequence on the same energetic system without a
reset, and the explicit CP discretization reproduces the original microscopic
GKLS reduced channel and chosen energy moments at finite times. Autonomous
continuous-time realization, exact event-time instruments, optimized supply,
and physical selection remain separate obligations. Stop here before target
author comparison.
