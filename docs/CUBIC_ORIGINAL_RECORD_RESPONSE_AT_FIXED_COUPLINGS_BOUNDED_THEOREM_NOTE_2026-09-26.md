---
claim_id: cubic_original_record_response_at_fixed_couplings_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: For the supplied compensated cubic integer-rotor law, a local original-event occurrence contrast after its full actual first mark admits an explicit finite-window comparison to a complete one-pair hazard response, uniformly on sufficiently large finite even tori at fixed finite R and positive r. The construction retains all later birth sectors and supplies local preparation, electric averaging, capture and volume errors. Numerical response estimates have separately stated sampling and floating-arithmetic qualifications. No physical detector identity, calibration, infinite-volume first-event process or experimental success is asserted.
upstream_dependencies:
- cubic_one_pair_band_actual_first_birth_limit_and_electric_excitation_bounded_theorem_note_2026-09-26
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/cubic_original_record_local_response_2026_09_26.py
---

# Original local records after actual formation, at fixed couplings and large volume

Type: bounded_theorem
Status: proposed_retained

The supplied common law connects its actual first birth to a later original
record statistic with an error independent of total lattice volume. All
subsequent original births remain present. The leading response uses the
complete first state and the full magnetic translation component, with no
lowest-band filter. Unlike the parent's global comparison, this local
comparison permits the same finite R and positive r on arbitrarily large
finite tori. It is a finite-window statement, not a long-time transport theorem.

The explicit sufficient parameters remain extreme: u=.02, r=10^-33 and
R approximately3.14*10^93. A normalized response change of order one then
changes an occurrence probability by only order10^-35. This is conditional
model mathematics, not a practical experiment or evidence that the proposed
foundations describe nature. Physical preparation, record-to-detector mapping
and independent calibration remain to be supplied or derived. No observational
number is fitted here, and no new interaction, state selector or normalization
is added to obtain the response.

## Supplied law, state and observable

The actual parent sources are
[the compensated common law](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[the general-graph pair dynamics](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md),
and [the complete cubic first component](CUBIC_ONE_PAIR_BAND_ACTUAL_FIRST_BIRTH_LIMIT_AND_ELECTRIC_EXCITATION_BOUNDED_THEOREM_NOTE_2026-09-26.md).
They supply the hard-core charged matter, integer rotors, Gauss constraint,
compensation, Hamiltonian and resolved/coherent instruments. These structures
are not derived from the four native axioms by this note. The common-limit
model is the starting law; its microscopic-limit error is not estimated here.

Let L>=24 be even, N=L^3/2, A the even sites, B the odd sites, and orient each
edge from A to B. The physical P space has all A occupied, conserved charge N
and div E=q-1_A. Keep every allowed particle sector and every integer field.
In magnetic time u=delta*t, the full generator is

    L_R(rho)=-i[RD+H4,rho]+r sum_m D[B_m](rho),
    D=sum_(a->b,q_b=0) E_ab(E_ab-q_a),
    H4=-2 sum_{overlapping unordered a,c} S_ac^* S_ac,
    S_ac=F_c F_a P,
    D[B](rho)=B rho B^* - {B^*B,rho}/2,
    R=K_electric/delta, r=kappa/delta>0.

The B_m are exactly the parents' full original birth maps. The resolved
instrument has12N edge/sign labels; the coherent instrument has6N original
unnormalized sign sums. The frequency decomposition used for averaging below
is unobserved and does not redefine those labels.

Start at the supplied Omega: all A charges+1, B empty and E=0. Condition on the
original first resolved-minus mark on(0,e1). Its nominal normalized output has
all five destinations d adjacent to0 other than e1, each amplitude1/sqrt5:
A0 has charge-1, B_e1 and B_d have charge+1, with E_(0,e1)=E_(0,d)=-1.
The actual state is the same mark applied to the full prebirth evolved state.
The local preparation proof below holds for every finite first waiting time.
Matching sign/edge mixtures are possible but cannot replace this fixed
localized preparation without changing the stated statistic. A registered
first position may be translated along with the measurement; an unregistered
uniform mixture is not a localized preparation.

Let W be ALL A centers with |a|_infinity<=l, for an integer l>=7. Reset the
record window immediately AFTER the conditioning first event. Let p_f,W(u)
be the probability of any original mark centered in W during(0,u] under the
full subsequent law. Let p_v,W(u) use the SAME full law starting freshly at
Omega. W selects mark centers; all their outputs, including positive-D outputs
or charges outside W, remain intact. The statistic is

    S_L(u)=(p_f,W(u)-p_v,W(u))/(r*u)+1164/5.             (1)

The denominator r*u=kappa*t is a supplied rate times duration, not a fitted
scale, a survival probability or a measured-rate replacement. The baseline is
the same supplied Omega, not a fitted stationary state. A physical protocol
for both preparations is still absent.

Let H0 be the parent's complete one-pair D0 Hamiltonian and subtract its vacuum
scalar to obtain Hrel. Let G be the compression of the FULL original loss
minus60N I onto its closed first translation component. Define

    C(u)=(1/u) integral_0^u <phi_minus,e^(itHrel) G e^(-itHrel)phi_minus> dt
           +1164/5,                                   (2)

where the expectation is the normalized infinite-lattice Bloch integral.
Every first-vector component is retained. Equation(2) is a time average;
an endpoint response is a distinct quantity.

## Quantified conclusion and useful limits

The estimates below give, for fixed u>0, integer l>=7, positive r, integer
b>l+7 and even L>4(b+4),

 |S_L(u)-C(u)| <= 160*r*m*u*B_(l+2)(u)+r*m^2*u
    +[e_prep,b+2e_av,b+4E_b]/(r*u)+E_capture+E_volume(L),  (3)

with every constant defined constructively below and m=80|W|. Given a desired
positive error tolerance, choose l for capture, then r>0 for the two probe
terms, b for truncation and R for preparation/averaging. Finally take L large
for the volume error and geometric domain. The SAME l,r,b,R,u then work for
all sufficiently large even L. No N*r*u smallness is assumed. This does not
construct an infinite-volume first-event process; a homogeneous infinite
volume need not have a globally first event.

The rational runner exhibits l=2048,u=1/50,r=10^-33,b=434071 and

    R=31406174599109769984 * 10^74,
    even L>=1736302,

for which the right side of(3) is less than.014. This analytic error does not
include sampling or floating propagation error. At L=10^12, N*r*u=10, so the
comparison has not conditioned away all distant births. The huge R and tiny
record signal provide no laboratory feasibility claim. Smaller necessary
parameters are not ruled out by these sufficient inequalities.

## Full original hazard and exact first component

For a center a with o occupied neighboring B sites, full output orthogonality
gives the operator identity Gamma_a=2(5-o)F_a^*F_a for either original
instrument convention. After F_a there are o+1 occupied B neighbors; each
of the5-o eligible creation edges has two unit-norm signs. Summing their
creation losses gives2(5-o)I on that intermediate space. The coherent
edge loss has no cross term because opposite newborn A signs have orthogonal
ranges; its gain still retains the original coherent sign interference. On a one-pair coordinate word the compressed excess
has diagonal2(5-o)(6-o)-60, namely0,-20 or-36. Off-diagonal entries are
nonnegative counts of common full birth outputs. This computes B^*B before
compressing its input/output block. Inserting P0 between B^* and B would
incorrectly discard the known D2 outputs.

Only centers adjacent to an occupied B can contribute excess; an o=0 center
returns only the same input under the same-mark inverse and gives60I.
The complete11322-word component has118092 directed displacement entries for
G, zero missing targets and exact reverse-displacement Hermiticity. Its full
absolute row/column sum is at most684, its anchor step at most2, and uniform
Gershgorin bounds are[-684,212]. These are integer-stencil bounds for every
Bloch momentum, not estimates from a momentum grid. Its exact initial excess
is-1164/5 for the full first-minus vector; full plus and coherent first vectors
instead give-1044/5 and-1104/5.

For any selected subset of centers, each diagonal contribution is nonpositive
and each off-diagonal contribution is nonnegative. Partial G_W and complementary
G_out are therefore entrywise absolutely dominated by G and each has norm<=684.
This is not a positivity claim for the excess operator. Nonnegative off-diagonal
counts also prevent hidden off-component terms from cancelling between centers.

## Sharper uniform local operator bounds from original incidences

For F_a from occupied A to its vacancy, fix o occupied neighboring B sites.
Every source coordinate word has6-o outgoing destinations and every output
word has o+1 possible adjoint predecessors. Each nonzero matrix incidence
has modulus1, including the integer rotor shifts; restricting Gauss/charge
can only remove incidences. The rectangular Schur test therefore gives

    ||F_a on this block||² <= (6-o)(o+1) <=12.

Different o blocks have orthogonal domains/ranges; hence ||F_a||²<=12 on the
whole local domain (o=6 gives zero). This bound also holds in intermediate
spaces with another A hole, since that spectator does not change the degree
bound. The original pair term h_ac=-2 S_ac^* S_ac therefore has norm<=288,
and its commutator generator has norm<=576.

For a fixed resolved mark on edge(a,b), b must already be vacant. The outgoing
hop may use only the other five neighbors. On its o block the column/row
degrees are5-o and o+1. Creation j_sigma is an isometry on those eligible
intermediates. Thus ||B_(a,b,sigma)||²<=max_o(5-o)(o+1)=9. The coherent edge
loss is the sum of its orthogonal-sign losses, so its norm is<=18.

The previously independently checked exact center loss identity gives
Gamma_a=2(5-o)F_a^*F_a. Its squared-degree bounds for o=0,...,5 are
60,80,72,48,20,0; at o=6 the operator is zero. Hence ||Gamma_a||<=80 and
the full dissipator belonging to one A center has norm<=160r, in either
original instrument convention. These imply the optional sharper global
b=2592N, gamma=80N, ell=N(5184+160r). They improve bounds, not the law.
The earlier conservative constants remain valid unchanged.

## Why the averaged terms remain local despite the spectral notation

To make locality explicit, put each A charge in a two-dimensional site factor.
At each B site put its three-state matter and the six integer rotors on the
edges incident to that B. Each rotor occurs in exactly one such site factor.
Work first on this tensor space and then restrict to the invariant Gauss/
conserved-charge subspace. The composite original B and S^*S have local
extensions preserving all A occupations; no global projector is an added
interaction in this representation.

Each diagonal electric summand D_e depends only on its A and B endpoint
factors. All D_e commute. For an operator originally supported on a star at
center a, only electric terms touching that star can contribute to electric
conjugation; terms commuting with it stay commuting after every other D_e
conjugation. Consequently its averaged support lies in the lattice ball
S_a={x:|x-a|_1<=2}, containing25sites. A pair term at centers a,c has averaged
support in S_a union S_c, where|a-c|_1=2. No iterative support growth is caused
by this one electric conjugation. Uniform integration/averaging preserves
these supports and operator-norm bounds. This argument uses the original
local operators, not an assumption that individual global P_d are local.

The exact support inventory has85 even centers in the L1 radius4 ball and
1038 unordered distance2 A pairs with at least one endpoint in that set.
They bound terms meeting a star; a pair support has at most twice those counts.
These are overlap overcounts, not assertions that every commutator is nonzero.
The runner enumerates them without a finite-field cutoff.

## Periodic averaging of the complete instrument

## Periodic interaction picture and a norm error

For any finite sum with trace-generator norm bound ell, let U_s(rho)=exp(-isD)rho exp(isD). It is a trace-norm isometry of period pi.
In the electric interaction picture the bounded time-dependent generator is
A_R(u)=U_(-Ru) K U_(Ru), with period T=pi/R, norm at most ell, and

    Abar=(1/pi) integral_0^pi U_(-s) K U_s ds. Here K is the bounded interaction generator, not K_electric.

The integral is strong on trace class. Conjugation is strongly continuous
there even though norm continuity for the unbounded electric Hamiltonian is
not assumed. Each A_R(u) is a bounded GKLS generator, with its original jump
labels, and Abar generates a completely positive trace-preserving semigroup.
Its trace-class operator norm is at most ell.

Define C_R(u)=integral_0^u(A_R(s)-Abar)ds. Completed periods cancel exactly.
For the remaining fractional period of length v in[0,T], either that segment
or its complement gives norm at most2ell*min(v,T-v). Consequently

    ||C_R(u)||_(1->1) <= ell*T = pi*ell/R.

Write V_R(u,s) for the interaction-picture propagator. Duhamel and integration
by parts on each trace-class vector give

 V_R(u,0)-exp(u Abar)
 = C_R(u)exp(u Abar)
   +integral_0^u V_R(u,s)[A_R(s)C_R(s)-C_R(s)Abar]exp(s Abar) ds.

The propagators have trace-class norm1, including on non-Hermitian inputs
(by duality of completely positive unital maps). Therefore

 ||V_R(u,0)-exp(u Abar)||_(1->1)
 <= (pi*ell/R)(1+2ell*u).

For states, using trace distance ||rho-sigma||_1/2, this supplies

    epsilon_av=min(1, pi*ell*(1+2ell*u)/(2R)).

If rho0 commutes with D, so does exp(u Abar)rho0: group averaging makes Abar
covariant under U_s. Thus its electric rotation drops out on returning to the
Schrodinger picture. For such rho0 the FULL unconditioned postbirth law is
within epsilon_av of exp(u Abar)rho0. This includes every later birth, not a
comparison to a no-birth trajectory. No assumption2R>b is required for the
averaging identity, although useful bounds require a large R.

## What the averaged instrument actually is

Let P_d be the spectral projections of D. The averaged Hamiltonian is
Hbar=sum_d P_d H4 P_d, as a bounded strong operator integral. For each ORIGINAL
mark m, define B_(m,omega)=sum_(d-e=omega) P_d B_m P_e. Then the corresponding
averaged jump map is

    Jbar_m(rho)=r sum_omega B_(m,omega)rho B_(m,omega)^*.

This expression must be justified as the positive strong integral above;
it is not a finite sum assumed merely because the lattice is finite. On
positive trace-class inputs it converges in trace norm by the CP integral
and Fourier/Parseval identity. The anticommutator loss is the matching
sum_omega B_(m,omega)^*B_(m,omega), the electric-block diagonal average of
B_m^*B_m. Original coherent B_m remains the full sign sum before taking its
frequency components; coherence within a common omega is retained.

The frequency index is UNOBSERVED. It is an effective Kraus decomposition,
not another measured mark, physical selector, interaction or adopted axiom.
The same original edge/sign or coherent edge labels remain the records.
Starting from D0, a later mark can populate every d reached by P_d B_m P0,
including the known D2 outputs. Subsequent magnetic dynamics occurs in each
occupied electric sector and further original marks remain active. This
construction explicitly cannot be replaced by field-only D0 continuation.

## Local actual-first preparation

Let L be even with L>=24, as in the inherited unaliased cubic source,
N=L^3/2, and R=K_electric/delta>0. Before the first birth, all A sites
have charge+1, all B are empty, and Gauss gives D=sum_edges E^2. Group each
edge with its B endpoint, so D=sum_b D_b, D_b=sum_(a adjacent b) E_ab^2.
Every D_b is positive with integer spectrum. The prebirth H is RD+H4, with
H4=-618N I+V, ||V||<=24N and <Omega,V Omega>=0. These exact identities and
the bound are established in the linked cubic parent's preparation proof.

For the normalized prebirth no-jump state psi(t), Gamma=60N I, so its
normalized evolution is the unitary RD+H4 evolution of Omega. Energy
conservation, initially <RD+V>=0, implies

  R <D>_t=-<V>_t <=24N.

The state stays invariant under the even-sublattice translations of the torus,
which act transitively on the N B sites. Consequently <D_b>_t<=24/R for
EVERY B site, uniformly over all finite waiting times t. This does not require
the global state to stay close to Omega or the probability of any excitation
to be small. The domain justification is unchanged: D is self-adjoint,
V bounded, Omega in Dom D, and unitary evolution preserves Dom(RD+V)=Dom D.

For a finite set X of B cells (each B matter plus its six rotors), let P_X
project their rotors onto zero and let rho_X be the reduced prebirth state,
including any desired A charges, which are fixed. The commuting integer
operators give

  I-P_X <=sum_(b in X) D_b,
  1-<Omega_X,rho_X Omega_X> <= min(1,24|X|/R).

Trace distance to the pure local vacuum therefore obeys

  (1/2)||rho_X-|Omega_X><Omega_X|||_1
       <= sqrt(min(1,24|X|/R)).                         (P1)

This follows, for example, by purifying rho_X and projecting the purification
onto Omega_X: its overlap squared is the displayed fidelity; pure-state trace
distance followed by partial trace gives the inequality. Thus no unproved
factorization of the physical Gauss subspace is used. Partial traces occur in
the already checked ambient tensor representation.

Fix the original first edge(0,e1) and either resolved sign or coherent edge.
On the entire prebirth fixed-matter subspace, its normalized operator
V_m=B_m/sqrt(c_m), c_m=5 or10, is an isometry. This holds without using Gauss:
the five destinations have mutually orthogonal final matter words, and rotor
shifts are unitary; the two coherent signs also have orthogonal matter outputs.
V_m acts only on the original star C. No other A projector matters on this
input subspace. Thus its channel on a local region containing C is trace-
preserving on the relevant fixed-matter input domain.

For any finite tensor region Y, enlarge it to Y union C. Let X be its B cells.
Apply (P1), the local isometry and partial-trace contraction. The actual
normalized first-mark state's reduced density and the full nominal first
output of Omega then obey

  dist((rho_actual_first)_Y,(rho_nominal_first)_Y)
       <= sqrt(min(1,24|X|/R)).                        (P2)

The input local region must contain ALL six rotor cells needed by the star,
not just its displayed A center or selected endpoint. The nominal vector keeps
all5 or10 outputs. Conditioning causes no additional probability denominator:
B_m^*B_m=c_m I on every prebirth rotor input. First waiting-time mixtures retain
the same uniform bound. A uniform unregistered first position is not this
localized preparation and cannot be substituted for it.

For a local effect 0<=F_Y<=I the probability difference is at most(P2).
For a general Hermitian O_Y it is at most2||O_Y|| times(P2). A propagated effect
is generally quasilocal, so(P2) alone does not control it; a separate truncation
or influence bound is needed. Unlike the former global sqrt(6N/R), the bound
for a fixed Y has no total-volume factor. It changes a proof norm, not a state,
interaction, instrument, preparation rule or physical normalization.

## A bounded local-generator influence estimate

Here H^*=i[Hbar,.] is the averaged Hamiltonian generator,
D_a^* is the full averaged center dissipator before its rate factor r, and
L_r^*=H^*+r sum_a D_a^* is the full averaged law on ALL particle/electric
sectors. The nominal complete first density lies in the one-pair D0 component;
its Hbar evolution is the parent H0 evolution, equivalently Hrel after dropping
the scalar phase. This identification computes only the leading coefficient:
the L_r^* evolution used for comparison retains every subsequent original birth.

For a pair support S_a union S_c, all overlapping magnetic pair terms are
contained in the union of the two support lists enumerated above for S_a and S_c.
Each list has1038 terms. Thus a safe weighted interaction degree for the
Hamiltonian terms is

    J_H=2*1038*576=1195776,  v_H=e*J_H.

A birth support S_a meets at most1038 Hamiltonian terms, so the same upper
bound works when it is the initial support of an influence path. Multiple
Hamiltonian terms with the same support may be kept separately; this only
increases the bound. No birth terms enter v_H in the comparison below.

For a bounded local generator K_X with K_X(I)=0, restrict X to S_a or a
Hamiltonian pair support; more generally require its initial weighted overlap
sum to be at most J_H. Define C_X(t) as the supremum of
||K_X exp(t H^*)O_Y||/||K_X|| over generators on that fixed support. Split H^* into terms disjoint from X and
terms meeting X. K_X commutes with the former. Variation of constants using
the contractive evolution of that disjoint sum gives

 C_X(t) <= 1_(X meets Y)||O_Y||
           + sum_(Z meets X) ||H_Z^*|| integral_0^t C_Z(s) ds.

The same estimate applies successively to each local term. A path of n terms
cannot bridge distance d(X,Y) if6n<d(X,Y); its total weight is at most J_H^n.
Picard iteration and the exponential-series tail bound give

 ||K_X exp(t H^*)O_Y||
 <= ||K_X|| ||O_Y|| exp(v_H t-d(X,Y)/6).

The trivial contraction bound is ||K_X|| ||O_Y||. No prefactor-one bound
is asserted for an arbitrary large initial support X: its initial overlap
degree could grow with its size. The required D_a^* has X=S_a and meets the
stated degree condition. This reasoning uses only
bounded local maps, finite interaction degree and contractivity, not finite
local Hilbert-space dimension. It is the bounded-generator path proof of the
Lieb-Robinson estimate; compare Barthel–Kliesch, arXiv:1111.4210, Section V.
Its hypotheses are verified here for the averaged Hamiltonian, including the
local extension before restriction. No direct finite-qubit substitution occurs.

## Uniform sum over ALL distant birth centers

Suppose Y is inside the L-infinity ball of integer radius s about0. Then

 d(S_a,Y) >= max(0, |a|_infinity-s-2).

For u>=0 let q=ceil(s+2+6 v_H u) and z=exp(-1/6). Count all integer centers,
including odd centers as an overcount. In the periodic minimum-distance metric,
the number with |a|_infinity<=q is at most(2q+1)^3, and the shell at radius m
has at most24m²+2 sites, independently of total L. The influence sum obeys

 sum_a min(1, exp(v_H t-d(S_a,Y)/6)) <= B_s(u), 0<=t<=u,
 B_s(u)=(2q+1)^3
       +24*(q² z/(1-z)+2q z/(1-z)²+z(1+z)/(1-z)³)
       +2z/(1-z).

The tail follows by putting m=q+j and using
v_H u+(s+2-q)/6<=0. It is a bound on all original birth centers, not a rule
that deletes distant births. For fixed s,u it is independent of N.

Duhamel with the FULL L_r^* semigroup on the left and the H^* semigroup on
the right now gives, for any local O_Y,

 ||exp(t L_r^*)O_Y-exp(t H^*)O_Y||
 <=160 r ||O_Y|| t B_s(u), 0<=t<=u.

All later sectors appear in the left evolution and in each full dissipator.
Its contractivity, rather than a one-pair norm, controls that left factor.
The bound is useful for small fixed r; it imposes no N*r*u condition.

## Original region events and error before dividing

Let W be a finite set of A centers inside radius l. Count all ORIGINAL labels
born at those centers, in either one supplied instrument convention. Put
M_W=sum_(a in W) Gamma_bar_a. It is positive, local in Y inside radius s=l+2,
and m=80|W| bounds its full-space norm. In the averaged process its conditional
intensity is at most r*m. The exact mean count during(0,u] is

 E_r C_W(u)=r integral_0^u Tr[M_W exp(t L_r)rho]dt.

The previous operator bound yields

 |E_r C_W-r integral_0^u Tr[M_W exp(t H)rho]dt|
 <=80 r² m u² B_(l+2)(u).

If p_r,W is the probability of at least one such event, the bounded-intensity
counting process has factorial moment E[C_W(C_W-1)]<=(r*m*u)². Therefore

 0<=E C_W-p_r,W <=(r*m*u)²/2.

The count is not assumed Poisson; this bound follows by iterating the
conditional-intensity upper bound for two ordered event times. The original
finite-volume process has finitely many total births and bounded intensity.

Take the contrast between rho_f and Omega. Under the nominal Hamiltonian,
Omega is stationary as a density, and M_W has constant vacuum value60|W|.
Define the compressed one-pair excess G_W=P0(M_W-60|W|I)P0 on the first
component. It compresses B*B AFTER full outputs, never B*P0B. Thus

 |(p_f,W-p_vac,W)-r integral_0^u <G_W>_f,t dt|
 <=160 r² m u² B_(l+2)(u)+(r*m*u)².                   (W1)

## Capture and finite-volume comparison

The complete compressed excess G has full-stencil norm bound684. For each
center, its coordinate diagonal is2(5-o)(6-o)-60<=0, and all off-diagonal
coefficients are nonnegative. Thus restricting to a subset of centers only
decreases every absolute row/column sum. Each partial G_W and complementary
G_out has norm at most684 on the closed first component. This also follows
for nontranslation-invariant subsets because the exact diagonal/off-diagonal
incidence signs are coordinatewise. No cancellation across centers is needed.

If W contains every A center with |a|_infinity<=l, G_out annihilates any basis
word whose anchor has |tau|_infinity<=l-7: all occupied B sites are within the
analytic relative radius6, and only adjacent A centers can contribute excess.
Hermiticity gives G_out=P_far G_out P_far, so

 |<G-G_W>_t|<=684 ||P_far psi(t)||².

The exact original H stencil has maximum anchor jump2 in L-infinity. Scalar
shift2400 gives absolute row bound M_s=11728. Starting at anchor0, powers of
order j cannot reach anchor distance>2j. With n=floor((l-7)/2)+1,

 ||P_far psi(t)||<=T_n(M_s*t), T_n(x)<=exp(x)*x^n/n!.

This is a quantitative capture bound on the full wave packet, not a lowest-band
filter. At fixed l,u it is uniform in sufficiently large tori; the region must
be represented without wrapping. For comparison of the total G expectation
with the infinite Bloch integral, a safe series threshold is q_L=floor(L/8)-1.
At total H power j<q_L, all paths in <phi H^m G H^n phi>,m+n=j, remain
unaliased by the same local periodification argument; G adds one bounded-range
step. The summed coefficients at order j are bounded by684*(2M)^j/j!,M=14128.
For completeness, an input relative word has support radius at most6.
An active birth center is within7 of the anchor, and every full birth output
and same-mark inverse stays within radius8. For even L>=24 this local
neighborhood is unaliased, so the full original loss periodifies exactly.
The unique negative charge identifies the anchor; distinct internal words
remain distinct. The parent gives the analogous H periodification. A monomial
with j=m+n has at most j+1 anchor steps of size2; at j<q_L its intermediate
anchors stay strictly inside L/2 and cannot close through a nonzero winding.
Each volume contributes at most684*(2M)^j/j! at total order j. The orders
below q_L agree, and bounding both remaining tails proves the stated error.
The finite/infinite expectation difference is therefore at most

 E_vol=2*684*exp(2M*u)*(2M*u)^q_L/q_L!.

Here E_capture=684*T_n(11728u)^2. For l2048,L16384,u.02, independently
reconstructed exact rational upper bounds are1.66473687478e-215 for capture
and1.92515042277e-9 for volume. For larger L, the latter factorial expression
decreases once q_L+1>2Mu, which already holds at this base size. Thus the
runner's simpler certified bounds1e-200 and2e-9 also cover every L in the
explicit fixed-parameter example. The periodification proof uses complete
local original-B outputs/inverses and the fixed first-edge anchor, not a
field-only truncation or finite momentum-grid approximation.

## Local event bookkeeping and generators

Use the same physical/ambient tensor construction and the same interaction
frame for RD. Each bounded Hamiltonian pair generator has support S_a union
S_c, |a-c|_1=2, norm<=576 and diameter<=6. Each original center's full birth
dissipator has support S_a, norm<=160r. S_a is the L1 radius2 ball. These bounds
hold before and after the period-pi/R electric average on all sectors.

To register occurrence of any mark with center in W={even a:|a|inf<=l}, attach
a separate classical binary bookkeeping flag to EACH selected A center. For
each original mark at a, replace the jump by its two versions with flag maps
|1><0| and |1><1|. Nonselected marks leave flags alone. The sum of losses is
Gamma_a tensor I_flag. The physical marginal is the original process from
initial all-zero flags, and the final effect F=I-product_a |0><0|_a equals the
original event occurrence. The norm of each flagged center dissipator is still
<=160r: its CP gain has norm||Gamma_a||<=80 and its loss has norm<=80.
No common spatially nonlocal flag is introduced. The flags are classical
bookkeeping, not a new interaction or additional physical event.

The extended local terms, indexed Z, are bounded generators l_Z^R(t), periodic
with period pi/R. Let bar l_Z be their time average. Every selected partial sum
is a time-dependent GKLS generator (Hamiltonian terms plus complete center
birth dissipators) and has a unital CP contractive Heisenberg propagator.
Strong trace-class integration suffices; norm continuity in electric frequency
is not assumed. Electric factors cancel from the final flag effect.

## Uniform influence bound for time-dependent terms

A pair support meets at most2076 Hamiltonian pair terms and170 birth centers;
a star meets at most1038 and85. Thus the weighted degree bound is

  J=1195776+27200r, v=e J.

The corrected initial-degree condition holds for every star/pair term used
below. The same disjoint-generator variation-of-constants recursion works for
time-dependent generators. In backwards time, remove terms meeting initial X;
the disjoint propagator remains contractive and commutes with K_X. Picard path
weights are bounded by J^n. Therefore, for an initially local observable O_Y,
any restricted sum of the terms, and any star/pair-supported bounded map
K_X annihilating I with the corresponding local extension,

 ||K_X T_restricted^*(t,s) O_Y||
 <=||K_X||||O_Y|| min(1, exp(v(t-s)-d(X,Y)/6)).          (A1)

This is precisely the prior influence proof with uniform time-dependent norm
bounds and birth terms included in the weighted degree. It is not an estimate
for an arbitrary large initial K support. Initial Y may be the whole W.

## Finite-region truncation of the effect, not of the original law

Take nonnegative integer lattice cutoffs l,b with b>l+7.
Let Lambda_b be the tensor-site cube |x|inf<=b, and retain only whole
local terms whose supports are contained in it. Denote its propagator by T_b.
This is an approximation used in the proof. The original full process is
always T. For the norm-one flag effect F supported in W, Duhamel with the
full contraction on the left and T_b on the right bounds ||T^*F-T_b^*F|| by
the time integral of omitted l_Z acting on the backwards truncated effect.

Assign each unordered Hamiltonian pair to one endpoint a. At most18 pairs
are assigned to a center, and each support is within infinity radius4 of a.
A birth term is within radius2. If a term is omitted, its representative obeys
|a|inf>b-4, hence integer m=|a|inf>=b-3. Also d(Z,W)>=m-l-4.
Counting all integer centers, even the unused odd ones, shell size is at most
24m²+2 on every torus. Put c=10368+160r and z=exp(-1/6). For u>=0,

 E_b = u*c*exp(v*u-(b-l-7)/6)
       *[24*((b-3)^2/(1-z)+2*(b-3)*z/(1-z)^2
                    +z*(1+z)/(1-z)^3)+2/(1-z)]          (A2)

bounds the effect truncation error for both T_R and bar T. This sums all
omitted terms and does not remove their actual births. For a nonwrapping
comparison take even L>4(b+4), although the shell inequality itself is uniform
on periodic metrics. For fixed l,u,r, E_b tends to zero as b tends to infinity
(polynomial prefactor times decaying exponential), independently of N.

## Apply the checked periodic average on this finite approximation

Let n_A(b) be the number of A centers in Lambda_b, safely <=(2b+1)^3.
Every retained magnetic pair has both endpoints there; degree18 gives at most
9 n_A(b) unordered pairs. All retained centers contribute at most160r each.
Thus ell_b=n_A(b)*(5184+160r) bounds the entire truncated trace generator.
The already checked bounded periodic averaging theorem gives a probability
error for any initial state and norm-one effect of at most

  e_av,b=min(1, pi*ell_b*(1+2ell_b*u)/(2R)).              (A3)

No global D truncation is performed. The time-periodic bounded interaction-
frame maps themselves are retained/averaged. Their average is a valid GKLS
sum, with the same unobserved frequency resolution of full original marks.

The truncated backwards flag effect is a positive contraction supported in
Lambda_b. The original first star is contained there. The local preparation lemma above bounds its expectation difference between actual and
nominal full first outputs by

  e_prep,b=sqrt(min(1,24 n_B(b)/R)),                     (A4)

where n_B(b) counts B cells in Lambda_b, safely <=(2b+1)^3. Initial flags are
identical product zeros. Apply(A2) before and after(A3), and(A4) only in the
first experiment. For the actual-minus-vacuum contrast compared with the
full averaged nominal-minus-vacuum contrast, the error is at most

  e_prep,b+2e_av,b+4E_b.                                (A5)

The baseline starts at Omega with fresh flags; no preparation error is added.
The first experiment starts AFTER the registered original first mark, with
fresh flags and window(0,u]. All first waiting times are covered uniformly.

## Rational parameter certificate and sampling protocol

For the explicit example take z<6/7, e<3 and pi<22/7. Let T=256 and
b=l+7+ceil(18Ju)+6T. The exponent in E_b is at most-T, so exp(-T)<2^-256
bounds the tail using exact rational arithmetic. The even/odd cube counts are
n_A=((2b+1)^3+(-1)^b)/2 and n_B=((2b+1)^3-(-1)^b)/2.
With epsilon=r*u/400, choose integer R at least both24n_B/epsilon² and
(22/7)ell_b(1+2ell_bu)/(2epsilon). Then e_prep,b,e_av,b<=epsilon and
E_b<5.67e-62. The original weak/count terms total.00569865243435; bounding
preparation and both averaging terms by epsilon gives local transfer.0075
plus the tiny truncation term. Adding capture and volume gives(3)<.014.
These choices were based on error inequalities, not observational fitting.

The numerical protocol uses4096 new uniform momenta from seed261926322,
full first-minus vectors and u=.02. A second target uses the SAME momenta
and independent uniform times in[0,.02] from seed261926323. The endpoint and
time-average have fixed stops; the earlier128-sample production and16-sample
pilot are excluded. The full[-pi,pi)^3 cube pushes forward to normalized Haar
measure on the even-sublattice reciprocal torus, so no factor2 is inserted.

For each target, scaling the exact G range[-684,212] in Maurer–Pontil Theorem4
and taking a union bound over two signs and two targets gives joint95%
coverage conditional on iid exact integration samples, with radius

    sqrt(2*s²*log160/4096)+7*896*log160/(3*4095).

Here s² is unbiased sample variance. Pairing between targets does not invalidate
the union bound; their full sample covariance is retained. Seeded pseudorandom
points and floating evaluation are separate numerical assumptions. Norm errors
or selected alternative-propagator agreement do not certify all rounding errors.

The completed fixed-budget results are:

| Target | Mean change from initial excess | Joint-family empirical-Bernstein interval |
|---|---:|---:|
| Endpoint at u=.02 | -4.22773599689 | [-6.83883359965,-1.61663839413] |
| Uniform time average over[0,.02] | -3.74314936801 | [-6.39235515321,-1.09394358280] |

The sample variances are.161602291839 and1.363102969974. The paired sample
covariance is-.000927014493. All4096 points per target are included; neither
result changed the stop rule. Independent reconstruction of the final arrays,
range, Haar normalization and confidence constants agrees. Sixteen prescribed
alternative propagations (eight momenta, both targets) from independently rebuilt
H/G stencils differ by at most2.26e-11. Their exact-arithmetic Taylor truncation
bound and floating-operation-model bound are separate; these selected checks
are not a rounding certificate for all8192 primary evaluations.

Under the ideal-iid/exact-integrand sampling interpretation, adding the analytic
transfer error below.014 widens the time-average interval for S_L to
[-6.40636,-1.07994]. This numerical interpretation is therefore separated from
zero by much more than the stated analytic error. It is not an unconditional
interval-arithmetic proof of the sign: the implemented pseudorandom quadrature
and noninterval floating values retain their disclosed qualifications. It is
also not a physical observation. The endpoint is not used as the time average.

## Preserved failures and exact scope

The original influence lemma incorrectly allowed arbitrary large initial K
support with a unit prefactor. For many disjoint qubit bonds, a product-support
commutator violates that bound; restricting K to a star/pair or its actual
weighted initial degree repairs it. The local preparation first draft said
only even L: on the simple L4 torus its imported vacuum scalar/norm are
-510N/30N, so the inherited even L>=24 domain is required. A noninteger b also
invalidates the integer shell-start inference; b,l are lattice integers here.
These restrictions change no physical law.

A center ball with a missing origin can leave G_out diagonal-36 at anchor0,
so the capture proof needs the FULL ball. Changing the first edge to(0,e2)
without changing the plus/coherent anchor convention invalidates an anchor-zero
argument. Selecting centers does not select output positions: an allowed
center in a radius2 ball can have every output outside it. The parent's
later-birth witness has full norm3 split1 atD0 and2 atD2; projecting those
outputs early gives the wrong hazard. The window starts after the conditioning
mark, excluding that mark itself. All these counterexamples remain explicit.

## Evidence, source status and physical interpretation

The canonical runner rebuilds the whole relative H component and G from the
original primitives, checks exact rational parameter/capture/volume inequalities,
and runs both fixed4096 integrations. The terminal text-cache payload retains
all8192 hazard values losslessly as base64-encoded little-endian binary64,
with shape(4096,2), column order and a SHA256. The integration points are
reproduced from the fixed PCG64 seeds and uniform ranges; full design-array
hashes and the NumPy version bind that regeneration. Per-target maximum norm
errors and the full norm-error array hash are diagnostic. This compact payload
fits below the canonical cache's200000-character stdout cap; binary
intermediates exist only in a temporary directory.
Support counts and integer certificates test quantitative parts of the proof;
the analytic locality, normalization and physical distinctions above cannot
be established by counting passing assertions.

Independent reconstructions have separately checked the entire original H
stencil; every11322 G column and118092 entries by full-B outputs/inverses;
local operator/support bounds; periodic electric averaging; the original-count
comparison; local preparation; capture/periodification; and local flag/averaging
composition. Known scope failures were corrected and their counterexamples
preserved. The numerical reconstruction also agrees within the stated computation limits.
Independent source checks are research evidence, not audit retention. No audit
verdict or retained grade is supplied here.

The chain presently ends at a conditional model record statistic. Omega is a
supplied preparation, the rotor/matter representation and common law are
supplied constructions, and original labels have no established detector
identity. The Planck units reference supplies no R,r or physical clock; kinetic-
form isotropy supplies no particular dynamics; the realized-state primitive
selects no Omega. A model loss or mobile charge cannot simply be identified
with a permanent readable native Record. These are explicit physical tasks,
not extra assumptions adopted to turn this calculation into a fit. Mass,
photon and cosmological-number programs cannot inherit this response as an
empirical calibration or validated common-regime particle identification.

## Primary mathematical precedents

- [Barthel and Kliesch, arXiv:1111.4210v2](https://arxiv.org/pdf/1111.4210): bounded local-generator path recursion; the hypotheses and needed constants are reconstructed above on the actual ambient rotor tensor space.
- [Etienney, Robin and Rouchon, Quantum10,2031 (2026)](https://quantum-journal.org/papers/q-2026-03-16-2031/): contractive residual estimates motivate comparing a local backwards effect; no external-vacuum stationarity is imported.
- [Maurer and Pontil, arXiv:0907.3740, Theorem4](https://arxiv.org/pdf/0907.3740): the bounded iid sample-variance inequality used with the explicitly stated sampling hypotheses.
