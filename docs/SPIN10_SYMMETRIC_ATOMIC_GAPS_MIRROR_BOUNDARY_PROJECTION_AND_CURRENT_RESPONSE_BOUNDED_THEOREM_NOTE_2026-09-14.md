# Spin(10) atomic gaps and the actual remaining mirror spectrum

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author-proposed conditional mathematics; actual source status conditional-support.
Independent scientific review is pending. No interacting chiral phase or axiom
contradiction is established.

An explicit local Spin(10)-invariant atom has a unique symmetric ground state
and an exact gap, while breaking the larger flavor and number symmetries of
a simpler projector model. Freezing these atoms on a supplied Wilson slab
leaves a calculable boundary spectrum: removing a full layer preserves a
partner, and removing only the original mirror slots restores eight Weyl
nodes. Their actual charged-current response detects the additional modes.
Exact elementary/composite spectral functions and a fourth-order interaction
also show why an atomic propagator alone cannot supply the lattice response.

**Runner:** [self-contained primary](../scripts/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_2026_09_14.py).
**Receipt:** [canonical cache](../logs/runner-cache/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_2026_09_14.txt).
**Review:** [author record](../.claude/science/physics-loops/toe-charged-phase-20260914/deliveries/block6/REVIEW_HISTORY.md).

## Premises and precise scope

| Supplied data | Bounded result | Remaining obligation |
|---|---|---|
| CAR modes in two or four copies of the chiral 16, explicit local operators | Unique Spin(10) singlet and exact atomic gap | Native finite-cell encoding and selected interaction |
| Tuned finite-width Wilson slab and a specified frozen boundary subspace | Exact projected bands, node locations and handedness | A chiral finite-coupling many-body phase |
| Product atomic zero sector, finite-box hopping norm | Feshbach error bound with explicit volume dependence | Uniform thermodynamic/infrared control |
| Actual free projected current and zero-temperature half filling | Leading absorptive conductivity of all remaining cones | Interacting chiral current response and gauging |
| Bare atomic comparator and supplied bath coupling | Exact fourth-order density interaction | Its coefficient is not imported into the refined atom |

All matrices, CAR structure, representation, auxiliary width, hopping,
Hamiltonian, state, gauge probe and couplings are supplied model data. The
minimal axioms and three approved primitives do not select them. The model
uses finite local payload and finite-range interactions after grouping each
fixed-width cell; a one-qubit nearest-neighbor native compiler is not supplied.
No unmerged campaign result is a scientific premise. The general strong-
coupling doubling warning and symmetric mass-generation mechanism have prior
art; no priority claim is made for those principles.

Take Delta,lambda,epsilon>0 in the refined atom, q=32 or64, finite L>=2,
and D>0 in the separate quadratic dilation. The bare projector comparator
allows even q>=4, with q>4 for its fourth-order formula. The finite-box
strong-coupling statement takes U>2||V||. Optical limits take positive omega
to zero after the declared free spatial infinite-volume limit; no exchange
with the interacting finite-U limit is assumed.

## 1. An exact symmetric onsite gap

Take q even complex CAR modes, q>=4, with |F>=c_1^dag...c_q^dag|0>,
|s>=(|0>+|F>)/sqrt(2), P=|s><s| and Q=1-P. The onsite Hamiltonian
H_at=Delta Q has a unique even ground state and exact gap Delta>0. For any
onsite one-particle representation R(g) with det R(g)=1, both |0> and |F>
are invariant, hence P and H_at are invariant. Spin(10) chiral 16 with two
or four Weyl/orbital copies has this property (q=32 or 64). The state has
<c_a^dag c_b>=delta_ab/2 and <c_a c_b>=0. This is an exact finite-dimensional
interacting singlet, not a quadratic fermion mass.

The bare projector has extra symmetries, including SU(q) and number modulo q.
For the proposed mirror use these are not silently ignored. We can explicitly
remove the larger flavor symmetry and reduce uniform number rotations to the
Spin(10) central Z4 while retaining the exact statements below.

For k=0,...,4, define 32-dimensional Euclidean Clifford matrices
gamma_(2k+1)=I^tensor k tensor X tensor Z^tensor(4-k),
gamma_(2k+2)=I^tensor k tensor Y tensor Z^tensor(4-k).
Restrict to the +1 eigenspace of Z^tensor5, ordered by the underlying binary
basis; its dimension is 16. Set t_ab=(i/2) gamma_a gamma_b on the 16, a<b, so
sum_(a<b) t_ab^2=(45/4)I. The many-body generators are
T_ab=sum_(orbital,alpha,beta)c^dag_(orbital,alpha)(t_ab)_alpha,beta c_(orbital,beta).
Their Casimir C2=sum T_ab^2 is nonnegative and annihilates vacuum and filled
states. It equals 45/4 on the one-particle and one-hole sectors.

For two spin slots u_alpha,v_alpha, choose symmetric matrices
M_a=(C gamma_a)|_+ where C=Y tensor X tensor Y tensor X tensor Y in the explicit
five-qubit Clifford convention. Define B_a=sum M_a[alpha,beta] u_alpha v_beta
and Omega=sum_a B_a B_a. B_a transforms as the 10-vector; Omega is a Spin(10)
singlet changing fermion number by four. It is also a spin SU(2) singlet,
since B_a=epsilon_st c_s M_a c_t/2. Omega is nonzero: its ordered
u_alpha u_gamma v_beta v_delta coefficient is
-2 sum_a(M_a[alpha,beta]M_a[gamma,delta]-M_a[alpha,delta]M_a[gamma,beta]),
for alpha<gamma,beta<delta. The explicit matrices give 240 nonzero ordered coefficients, norm bound B=2560,
and a coefficient +8 at (alpha,gamma,beta,delta)=(0,1,14,15). The runner checks
the complete fourth exterior tensor against all 45 Spin(10) generators.
For q=64 use one of its two orbital spin pairs; all slots still enter C2.

Let Pi_mid be the number projector onto 2<=N<=q-2 and
O=Pi_mid(Omega+Omega^dag)Pi_mid. Let B be twice the sum of absolute values
of the ordered coefficients of Omega, which bounds ||O||. For lambda,epsilon>0,

H_at = Delta Q + lambda C2 + epsilon (B Pi_mid + O).

The last two terms are nonnegative, annihilate |s>, and also leave the
one-particle/hole subspaces invariant with the same Casimir value. The exact
many-body gap is still Delta: Q is one on its complement and the orthogonal
state (|0>-|F>)/sqrt(2) attains Delta. The single-fermion excitation energy is
Delta_f=Delta+45 lambda/4. No expansion in epsilon is used.

The finite operator norm is bounded by Delta+45 lambda q^2/16+2 epsilon B,
since each many-body T_ab has norm at most q/4.

This Hamiltonian is Spin(10) invariant. The generator identity
t_ab^T M_c+M_c t_ab=i(delta_ac M_b-delta_bc M_a) proves the vector
transformation and hence invariance of Omega. Nonzero coefficients of O really
survive Pi_mid: the +8 monomial on modes u_0,u_1,v_14,v_15 connects, for
example, a two-particle state on unused modes u_2,u_3 to a six-particle state.

The two-particle Casimir values can be derived without diagonalization.
The Clifford bilinears C gamma_[a1...ap] give the decomposition of 16 tensor16
into one-, three- and one chiral half of five-forms. Their dimensions are
10,120,126 and their transpose signs place the one/five-forms in Sym^2(16)
and the three-forms in its antisymmetric square. Clifford trace orthogonality
and the chiral five-form duality give completeness (10+120+126=256).
The rotation generators acting on a p-form have quadratic Casimir p(10-p),
as follows by summing the generators which replace one occupied index by an
unoccupied one. Thus the values are 9,21,25. The primary additionally checks
the exact annihilating polynomial and multiplicities in the explicit matrices.

C2 removes full SU(16) flavor symmetry:
on Sym^2(16), realized with the two orbital slots, the two irreducible Casimir
values are 9 and 25 (multiplicities 10 and 126), whereas Sym^2 of the SU(16)
fundamental is irreducible. A nonscalar C2 on it cannot commute with all SU(16).
The number-conserving part and charge-four part of the commutator cannot cancel.
Nonzero O connects some interior number sectors N and N+4, so its uniform
number rotations have exactly e^(4i theta)=1. This Z4 is already represented
by the Spin(10) center acting on the 16. We make no assertion classifying every
remaining discrete or spatial symmetry of the full slab.

## 2. Exact elementary and composite spectral functions

Use the retarded/analytic anticommutator convention with Im z>0 and ground
energy zero:
G_AB(z)=<s|A(z-H)^(-1)B^dag|s>+<s|B^dag(z+H)^(-1)A|s>.
For the above H_at, c_a^dag|s> and c_a|s> have squared norm 1/2 and energy
Delta_f. The elementary function is

G_cc,ab(z)=delta_ab z/(z^2-Delta_f^2).

It has a zero at z=0 despite a positive Hilbert space, Hermitian bounded
Hamiltonian and positive spectral weights. A propagator zero alone does not
establish a ghost or failure of unitarity of a specified interacting model.
This is an atomic example; no chiral continuum gauge theory is inferred.

Define b_a=[H_at,c_a]/Delta_f. Then b_a|s>=c_a|s> while
b_a^dag|s>=-c_a^dag|s>. In the interpolator vector (c_a,b_a), the exact function is

G(z)=(z I-Delta_f sigma_x)/(z^2-Delta_f^2),
G(z)^(-1)=z I+Delta_f sigma_x.

Its spectral residues are the positive rank-one projectors (I-/+sigma_x)/2.
The elementary zero is removed in this enlarged interpolator matrix. b is a
composite operator of the same Spin(10) transformation type as c. It is not
an extra independent CAR generator: this two-point identity does not make
the interacting lattice equivalent to a free theory with added orbitals.

For any two distinct modes the same refined ground state has
<n_a n_b>=1/2, while its normal two-point data and vanishing anomalous two-point
data would give 1/4 under Wick factorization. Thus non-Gaussianity is exact
also for the refined Spin(10) atom, independently of its middle-sector spectrum.

The recent interacting doubling criterion assumes a complete interpolating
set whose zero-frequency matrix has no zeros and the other smoothness/limit
conditions. This example neither disproves that conditional criterion nor
establishes such a set uniformly over the Brillouin zone after hopping.

## 3. An explicit tuned Wilson slab

Supply a finite auxiliary width L>=2, three-dimensional spatial momenta,
s_i(k)=sin k_i and b(k)=sum_i(1-cos k_i). Let B_L=b I_L-S_L, where
(S_L)_(j+1,j)=1, all other entries zero. With A/B orbital sectors and Pauli
spin, the one-particle Hamiltonian is

h_L(k) = [[ I_L tensor sigma.s, B_L tensor I_2 ],
          [ B_L^dag tensor I_2, -I_L tensor sigma.s ]].

This has nearest-neighbor spatial and auxiliary hoppings. It is a supplied
Wilson-slab representative, with the explicit tuning b(0)=0. Its square is
block diagonal with s^2+B_L B_L^dag and s^2+B_L^dag B_L. At k=0 the null modes
are A_1 and B_L, with opposite sigma.s signs. For a Brillouin corner with
r>=1 pi-components, b=2r and sigma_min(B_L)>=b-1>=1. Thus only the zero corner
has these Weyl zeros. Adding a constant offset to b generally restores the
finite-width residual gap det B_L=b^L; no robust exact zero for arbitrary
profiles is claimed. There is one 16-flavor copy in the Spin(10) model.

## 4. What the exact atomic projection leaves

Put the onsite H_at on each spatial site of a selected set of boundary slots.
P_tot is the product of their one-dimensional singlet projectors. For every
frozen fermion f, P_tot f P_tot=0; for two frozen modes at the same site,
P_tot f_a^dag f_b P_tot=delta_ab P_tot/2. Hopping between distinct frozen sites
and between frozen and retained modes has zero projection. Projecting the
quadratic slab Hamiltonian therefore deletes those one-particle rows/columns,
up to an explicit constant from onsite frozen bilinears (zero for the traceless
blocks here). This is an exact many-body projection identity.

Freeze a whole last layer (A_L and B_L, q=64 per spatial site). The projected
Hamiltonian is the same slab of width L-1. It still has the opposite-handed
boundary partner; at L-1=1 the two Weyl sectors occupy the same layer. A local
atomic gap on a complete layer does not remove the topological interface.

Freeze only B_L (q=32 per spatial site). The remaining off-diagonal matrix is
B_tilde with L rows and L-1 columns. It has full column rank for every real b:
the submatrix of rows 2,...,L has triangular determinant (-1)^(L-1). Its left
null vector is

v_j(b)=b^(j-1)/sqrt(S_L(b)), S_L(b)=sum_(j=0)^(L-1)b^(2j).

Consequently the exact invariant unpaired band is sigma.s(k) at every k.
The other singular values satisfy

lambda_n^2=1+b^2-2b cos(n pi/L), n=1,...,L-1,

so their energies are +/-sqrt(s^2+lambda_n^2), each twice. They remain separated
from zero by at least sin(pi/L) for fixed L. The unpaired band has eight Weyl
zeros at the spatial Brillouin corners, with chirality (-1)^r. Four signs are
positive and four negative; all have the same Spin(10) representation.
At b=0 the band is on A_1; for b=2r>=2 its weight is concentrated toward A_L.
The removed mirror has not yielded an isolated chiral species: the projection
restores momentum-space doublers. This statement holds for every finite L.
The real normalized orbital v has zero Berry connection, so its k-dependence
does not alter the displayed local Pauli winding signs.

## 5. Fixed-volume strong-coupling control

Write the full many-body H=U H0+V, where H0 is a sum of the dimensionless onsite
terms above with gap >=1 and product zero-sector P; V is the finite-box hopping
Hamiltonian. Set v=||V||. For U>2v, the low band lies in [-v,v], the remaining
spectrum starts at U-v, and for real |E|<=v the exact Feshbach operator on P is

F(E)=P V P-P V Q(Q H Q-E)^(-1)Q V P.

Its difference from PVP has norm at most v^2/(U-2v). This follows directly
from QHQ>=U-v and the Schur complement; the bound retains v's volume dependence.
For any low eigenvalue E, dist(E,spec(PVP))<=v^2/(U-2v). Thus the strong-coupling
endpoint at fixed volume is genuinely the deleted-slot problem above.

This is not a volume-uniform expansion or a proof about an intermediate
interacting phase. It does not license exchanging U->infinity, volume->infinity
or the infrared limit. An interaction phase that changes the remaining
boundary structure can evade this endpoint. Neither a finite atomic singlet
nor a classification-based existence claim supplies that quantitative path.

## 6. The first induced terms and the Gaussian-replacement boundary

Let a single frozen atom couple to retained CAR modes c by
V_mix=f^dag T c+c^dag T^dag f. All its ground-to-one-particle/hole transitions
have equal energy Delta_f and equal spectral weight 1/2. The second-order
Schrieffer-Wolff term is exactly

-P V_mix Q H_at^(-1) Q V_mix P
= -Tr(T^dag T)/(2 Delta_f) P.

The terms proportional to c^dag T^dag T c cancel between virtual atomic
particles and holes, by the CAR. At this order the induced term is a constant,
not a mirror mass. For several independent frozen atoms the constants add.
This formula concerns two boundary mixing vertices; retained kinetic insertions
or frozen-atom spatial hopping enter separate higher-order terms.

The second cumulant in the frequency-dependent boundary action has
Sigma^(2)(z)=T^dag T z/(z^2-Delta_f^2), so for |z|<Delta_f,
||Sigma^(2)(z)||<=||T||^2 |z|/(Delta_f^2-|z|^2).
It begins with -z T^dag T/Delta_f^2, a wavefunction correction. This is the
coefficient of the expansion in boundary hopping, not an exact resummation of
the entire interacting lattice or a claim that its higher cumulants vanish.

There is a direct counterexample to a Gaussian replacement. In the bare
projector atom (lambda=epsilon=0), a two-fermion state reached from |s> has
energy Delta, whereas a quadratic completion with one-fermion energy Delta
would have the corresponding two-particle threshold 2 Delta. The four-point
function therefore cannot follow by applying Wick's rule to the displayed
elementary propagator.

More quantitatively, take the bare q-mode atom with q>4 even, q retained bath
modes, and V=t sum_a(f_a^dag c_a+c_a^dag f_a), with zero bath Hamiltonian.
For the finite degenerate low space P, PV^2P=(q t^2/2)P. If n is retained
bath number,

PV^4P=t^4[3(n-q/2)^2+3q^2/4-q].

Proof: for the atomic vacuum, independent even hopping terms give
<V^4>=t^4[n+6 binom(n,2)]; for the filled atom replace n by q-n. Off-diagonal
vacuum/filled contributions need at least q hops and are absent at order four
because q>4. Averaging gives the formula.

The fourth-order effective Hamiltonian (in the standard Hermitian degenerate
expansion, with lower coefficients commuting here) is

H_eff^(4)=[2(PV^2P)^2-PV^4P]/Delta^3
=t^4[ q-q^2/4-3(n-q/2)^2 ]/Delta^3.

This supplies a nonzero attractive density interaction despite the simple
atomic two-point function. The q=6 full CAR calculation checks the entire
64-dimensional low-space identity through the 4096-dimensional atom/bath
space. The bare atom is an algebraic comparator with extra symmetries; this
coefficient is not imported unchanged into the refined Spin(10) atom. The
exact second-order cancellation above does apply to the refined atom.

## 7. An exact quadratic dilation retains the missing doublers

Another controlled comparison adds a free auxiliary two-spinor a to the
mirror B_L slots with onsite coupling D(a^dag B_L+B_L^dag a), D>0, and no
auxiliary spatial hopping. Its isolated B_L two-point function is exactly
z/(z^2-D^2), the atomic elementary expression. It is a separate quadratic
model, not a replacement theorem for the interacting atom.

At each spatial corner the enlarged off-diagonal matrix has rows
[B_L; D e_L^T] and full column rank. Its left null vector has physical A_j
components b^(j-1) and auxiliary component -b^L/D. Let
S_L=sum_(j=0)^(L-1)b^(2j). The projected velocity at a corner is

v_corner = S_L/(S_L+b^(2L)/D^2) > 0,

multiplying sigma_i cos k_i. Thus all eight corners remain Weyl zeros with
alternating chirality, at every finite D>0 and L>=2. At E=0 away from the
corners, the auxiliary equation forces B_L=0; the invertible deleted-slot
Hamiltonian of section 4 then forces every remaining component to vanish.
There are no other zeros. The small-D limit has very slow unwanted corner
modes, which can look absent in a restricted energy/momentum scan, but they
are gapless. The exact D=0 limit has a decoupled flat auxiliary sector and
is singular for this counting argument.

The same elementary atomic function is therefore compatible with very
different higher correlators and a free dilation whose additional modes are
explicit. Neither elementary zeros, composite mass terminology nor an onsite
gap establishes the desired chiral current response.

## 8. Actual charged-current discriminator in the projected models

Supply the zero-temperature half-filled ground state of the projected free
Hamiltonian, with negative-energy bands filled, and a background Spin(10)
Cartan generator t. Let Tr_16(t^2)=T (T=4 for t_ab normalized above), and g be
the supplied gauge coupling. Gauge the original spatial hopping with Peierls
links and differentiate that Hamiltonian to obtain the current. The onsite
singlet projectors are gauge invariant and field-independent, so the projected
current is the derivative of the deleted-slot Hamiltonian. No current is
inferred by differentiating an interacting propagator inverse.

For one isotropic Weyl cone h=v sigma.p and charge e, the absorptive diagonal
conductivity at positive small frequency is

Re sigma_ii(omega) = e^2 omega/(24 pi v) + o(omega).

This follows from the actual interband Kubo formula
(pi/omega) integral d^3p/(2pi)^3 e^2 v^2(1-p_i^2/|p|^2)
delta(omega-2v|p|): the angular integral is 8pi/3 and the radial integral
is omega^2/(8v^3). Chirality reverses no squared matrix element. Summing the
Cartan charges replaces e^2 with g^2 T. This is a free-band result in the
specified state and with the actual current; no interacting vertex assumption.

The deleted B_L model has eight unit-speed corners. Its small-frequency
conductivity slope is therefore eight times the single desired 16-Weyl-cone
slope g^2 T/(24pi). The whole-layer deletion has two opposite-handed
unit-speed cones and twice that slope. At fixed L the other bands have a
strict positive gap, so they do not change this leading absorptive term.
These statements take the atomic projection first, then the spatial infinite-
volume free model and finally omega->0. Finite-U interacting limits remain open.

For the quadratic dilation of section 7, the factor is instead

sum_corners 1/v_corner
=8+(1/D^2) sum_(r=1)^3 binom(3,r) (2r)^(2L)/S_L(2r).

For L->infinity at fixed D this approaches 8+89/D^2. Very slow unwanted cones
have enhanced, not suppressed, optical slope because their density of states
overcomes the squared velocity in the current. This limit is omega->0 first
at each finite D,L. It cannot be exchanged with D->0, where a flat auxiliary
sector appears. No direct physical prediction for the axioms is made.

## 9. Prior result and missing-hypothesis guard

The general warning that a strong-coupling endpoint can return doubling is
prior art, including Golterman-Shamir 2505.20436v3 section IV and appendix A.3.
The present result supplies an explicit Spin(10) atom, a Hilbert-space gap and
Schur bound, its remaining three-dimensional slab bands and actual current
response. It makes no priority claim for symmetric mass generation, atomic
propagator zeros or the general endpoint warning.

The onsite gap and its one-dimensional even projector are substantive
hypotheses. Mere uniform scaling of all interaction coefficients does not
justify deleting every participating fermion. For example,
H=U n_f n_d+t(f^dag c+c^dag f) has a degenerate local zero sector. In the
invariant sector n_d=0, the f/c hopping and eigenvalues +/-t persist for all U.
Thus P f P is nonzero even as U->infinity. Rescaling a CAR operator is not a
canonical transformation. This example blocks an extension of the present
projector theorem to arbitrary strong local interactions; it does not realize
a gapped mirror sector or refute a theorem with its hypotheses checked.

Sources are used with their actual qualifications: Wen's S9 proposal;
Wang-Wen's static-boundary/classification construction and its explicit
assumptions; Golterman-Shamir's complete-interpolator/smoothness condition and
endpoint discussion; and Zeng et al.'s warning about extracting current response
from an interacting two-point function alone. No full chiral-theory verdict is
imported from those discussions. The new obligation is a concrete finite-
coupling phase with a controlled chiral current spectrum, not simply an
onsite singlet or a list of anomaly coefficients.

## Negative-claim discipline and remaining constructions

### N1

The examined routes are a complete-layer singlet, a mirror-slot singlet,
a quadratic auxiliary completion with the same elementary atomic function,
a composite interpolating field, and the classification/S9 constructions
as literature comparisons. The first two have exact projected spectra;
the latter existence mechanisms are not evaluated as controlled interacting
phases. Intermediate interactions, non-product low spaces, spatially extended
interactions, different boundary couplings and additional fields remain live.

### N2

The onsite gap, the remaining lattice spectrum and the physical current
response are consecutive obligations. They are not three independent axiom
walls. The simple and refined atoms share their projection and are not
independent proofs against every mirror construction. The quadratic dilation
is a different model whose matching two-point function is explicitly limited.

### N3

The CAR carrier, Spin(10) representation, Wilson band, auxiliary coordinate,
tuning b(0)=0, frozen slot choice, product singlets, couplings, half-filled
state and physical gauge probe are supplied. The refined interaction removes
specific extra symmetries of the bare projector, but does not prove that no
other accidental symmetry remains. Finite local payload is not a native
one-qubit realization or an axiom-selected particle spectrum.

### N4

The current-main finite record-coordinate wall correction concerns a supplied
one-particle matrix, balanced low spaces and diagnostic limits. It supplies
no interacting mirror gap. The charged paired-fermion milestones also do not
supply one. The literature endpoint warning is matched here with an actual
Hilbert-space gap, projection, spectrum and current; no unrestricted
field-rescaling claim is used to remove CAR degrees of freedom.

### N5

The singlet, Casimir, projection, rectangular-kernel and Schur arguments carry
the stated generality. Small full Fock examples, exact exterior-tensor checks,
finite spectra and Kubo surface integrals are falsifiers. None proves a
finite-coupling thermodynamic phase or the completeness of a global
interpolator set. The volume dependence in ||V|| remains explicit.

### N6

The positive partial construction is an exact bounded Spin(10) atom without
the full SU(16) or extra uniform number symmetry. The analysis identifies
the required next construction: a finite-coupling chiral phase with its actual
conserved-current spectrum. A symmetric non-product boundary or a controlled
interacting deformation can evade the particular projection endpoint. No
additional axiom is introduced to close that open problem.

### N7

The strongest objection to a broad negative claim is valid: an intermediate
interaction phase need not equal the U->infinity endpoint. A propagator zero
alone does not violate positivity, and a symmetry-classification existence
argument is not refuted by failure of this particular atom/slab assembly.
A degenerate local zero space can retain participating fermions, as the exact
n_f n_d example demonstrates. Those alternatives prevent an all-lattice no-go.

### N8

This is a new chiral-matter obligation after the tensor and charged-gauge
blocks. It does not promote representation counts, anomaly bookkeeping or
an atomic PASS into a physical particle theory. General endpoint doubling,
atomic Green-function zeros and SMG are established research themes; the
repo contribution is the explicit model and its quantitative inference
boundaries. Independent scientific review and native construction remain open.

## Sources and review boundary

- [Wen, lattice Spin(10) chiral construction](https://arxiv.org/abs/1305.1045v4): supplied slab and proposed fluctuating-mass route.
- [Wang and Wen, nonperturbative Standard Models](https://arxiv.org/abs/1809.11171v3): classification and static/dynamical boundary qualifications.
- [Golterman and Shamir, SMG constraints](https://arxiv.org/abs/2505.20436v3): complete-interpolator conditions and the prior strong-coupling endpoint discussion.
- [Golterman and Shamir, proceedings](https://arxiv.org/abs/2603.15985v1): concise statement of the conditional interacting doubling test.
- [Zeng et al., optical response of SMG insulators](https://arxiv.org/abs/2405.05339v1): the need to obtain current response from the actual model.

No editable prompt, workflow, axiom or primitive file changes. No author audit
verdict, effective retained status or main merge is part of this proposal.

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "Construct a native chiral matter sector with a controlled mirror gap and the actual conserved-current spectrum."
source_of_blocker_text: "frontier_question"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Independently review the explicit Spin(10) atom, projected spectrum and current response; construct a controlled finite-coupling phase that passes the mirror-current test."
conditional_surface_status: "Supplied local model, exact atomic gap and endpoint/comparator mathematics; finite-coupling chiral phase and native carrier/law remain open."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact local singlet construction, quantified projection and complete free-band/current comparison; no all-interacting-lattice or axiom-forcing conclusion."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
