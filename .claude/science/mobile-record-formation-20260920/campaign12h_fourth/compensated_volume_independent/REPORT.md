# Compensated rotor target: independent local-volume reconstruction

2026-09-23. This report was completed before opening the new author volume
packet. It concerns the already checked effective rotor target, not a
volume-uniform limit of its microscopic spin/epsilon model.

**Result.** The finite induced-graph target evolutions have a limit in operator
norm on each bounded local observable, uniformly on compact time intervals.
In fact the estimate is uniform over the unit ball of each fixed local
algebra, including finite ancillary matrix amplifications. The limit is a
unital completely positive semigroup on the quasi-local algebra. Locally
normal initial states remain locally normal and have continuous expectations.
There is generally no norm continuity in time on the full bounded local rotor
algebra, nor a normal density evolution in every preselected global Hilbert
representation. Those stronger assertions are false even for the permitted
purely electric case.

The proof below handles the missing norm-continuity hypothesis by first
capping the commuting electric terms. It does not apply a bounded-generator
norm-continuity theorem directly to the uncapped interaction picture.

## 1. Dependencies, target, and algebra

The fixed local-pair identity and jump support are reused from the previously
fully checked `LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS.md`, SHA256
`5539bbe3171ba21933aa42c4cc191b787029e5f5c9220dc8c3ee255e4906f582`.
The common-field construction is SHA256
`42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4`.
My preceding independent REPORT, COMPARISON, and FINAL seal are also bound in
SOURCE_BINDINGS.json. Their fixed-graph conclusions are reused within scope;
the volume proof here is new independent work. No file in
`compensated_volume_author`, new root frontier, checkpoint, planning, registry,
Git or publication surface was opened.

Use the decorated lattice consisting of the sites of Z^d and its link
factors. Give the decoration the incidence-graph distance. The site Hilbert
space is C^2 at A (charges +/-1, already occupied) and C^3 at B (0,+1,-1).
A link has Hilbert space l^2(Z). For a finite set X of factors, use the full
algebra B(H_X), with normal embeddings A -> A tensor I. The norm closure of
their union is the quasi-local C*-algebra A. This convention includes every
bounded observable on a finite collection of infinite-dimensional rotors.
No infinite product projection P is required: all-A occupancy is built into
the local effective Hilbert spaces. The already checked compressed local
operators define the interactions on these spaces.

For an edge joining a in A to b in B, let s_ab be +1 when the stored
orientation is a to b and -1 otherwise. Set

    D_e=(1-n_b)(E_e^2-s_ab q_a E_e),
    V_ac=-2 delta (F_c F_a P)^* (F_c F_a P),
    L_(e,sigma)=sqrt(kappa) B_(e,sigma),
    B_(e,sigma)=P j_(e,sigma) F_a P.                    (1)

The unordered pair a,c appears only if it shares a B neighbor. The notation
P in (1) is the finite local compression just described. All D_e commute.
Each is a nonnegative diagonal self-adjoint operator, since E is integer and
q_a=+/-1. For a finite induced graph Lambda,

    H_Lambda=K sum_(e internal to Lambda) D_e
                         + sum_(a,c in Lambda) V_ac^Lambda.   (2)

The stars in V^Lambda and B^Lambda use that induced graph, not fictitious
neighbors outside it. K>0 is fixed and finite; delta,kappa>=0. On the regular
lattice put z=2d. The useful uniform estimates are

    ||F_a||<=z,  ||V_ac||<=2 delta z^4,
    ||B_(e,sigma)||<=z-1.                              (3)

The coherent convention here is one edge channel
sqrt(kappa)(B_(e,+)+B_(e,-)); there is no additional 1/sqrt(2).
The resolved convention has two separate channels, each with sqrt(kappa).
A conservative coherent norm bound is 2 sqrt(kappa)(z-1). Coherently summing
different edges is a different model and is not covered by the diagnostic
below, although any explicitly local bounded alternative can be handled by
the same volume proof.

Each Hamiltonian or jump term has uniformly finite support and only finitely
many such supports meet a given factor. The spatial range and these counts
depend on d, not volume or electric amplitude. Their commutator/dissipator
maps are normal and completely bounded, with

    ||i[V, .]||_cb <= 2||V||,
    ||L^*(.)L - {L^*L, .}/2||_cb <= 2||L||^2.          (4)

These estimates remain valid when tensoring with an arbitrary spectator
Hilbert space: each summand is a finite elementary operator. Thus an
infinite local rotor dimension does not introduce a hidden dimension factor.

## 2. Finite-volume evolution and the commuting electric picture

For each finite Lambda, the electric sum in (2) is a real diagonal
multiplication operator. Its natural square-summability domain is
self-adjoint, with finite electric-support vectors as a core. The bounded
perturbation sum V leaves a self-adjoint Hamiltonian on that domain. The
finite list of bounded jumps gives a normal CPTP evolution on trace class;
no electric moment is required for existence for a density operator.
For a general density the generator equation is understood mildly, rather
than as an everywhere-defined unbounded commutator.

One direct construction, useful below, is to remove the electric unitary.
For a bounded local operator A_X, commuting diagonals imply the exact identity

    alpha_t^D(A_X)
      = exp(i K t sum_(e:supp D_e intersects X) D_e)
             A_X
        exp(-i K t sum_(e:supp D_e intersects X) D_e).  (5)

No iteration of the support neighborhood is needed: electric terms disjoint
from the original X commute both with A_X and with every retained D_e.
Let X^+ denote the union of the supports in (5) and X. Its enlargement is at
most two incidence-graph steps. Equation (5) gives a consistent isometric
automorphism alpha_t^D of A for each t, with the group law. It need not be
norm continuous as a function of t.

In the electric interaction picture, replace every V and L by alpha_t^D(V)
and alpha_t^D(L). Their supports are fixed enlarged finite sets X^+ and their
norms are unchanged. The original two-star Hamiltonian supports have
incidence diameter at most 8; hence diameter 12 is a safe common bound after
enlargement. Every finite-volume interaction-picture generator has a uniform
bound as a map on trace class, though it grows with that finite volume.

Its coefficients and their adjoints are strongly continuous in time.
For example, on a rank-one trace-class operator, strong continuity of a
bounded coefficient becomes trace-norm continuity of left multiplication;
right multiplication uses strong continuity of its adjoint. Finite-rank
approximation then gives strong continuity of the generator on trace class.
The uniformly bounded nonautonomous Dyson series therefore converges there
and defines the unique interaction-picture propagator. Piecewise constant
coefficient approximations converge strongly on trace class: the relevant
solution orbits on a compact time interval are compact, so strong continuity
and the common bounds give uniform approximation on those orbits. Every
piecewise constant propagator is CPTP. Passing on trace class, and at each
finite matrix amplification, proves CPTP for the limit. The dual maps are
normal UCP contractions. Combining with the electric unitary constructs (2).

This construction needs neither a norm Bochner integral of the coefficients
on B(H_Lambda) nor norm continuity of the uncapped coefficients.

## 3. Locality estimate with a justified cutoff removal

Here is the step that cannot be supplied merely by quoting a norm-continuous
Lindblad theorem. Introduce a second approximation, used only in the proof:

    D_e^(M)=min(D_e,M).                                (6)

These bounded local operators still commute and preserve every support and
Gauss symmetry. For every fixed finite volume, its interaction-picture
coefficients are now norm continuous in t. All bounds (3)-(4), their support
sizes, and the overlap count are independent of M and K.

Index the enlarged local generator terms by their full-lattice support
containers Z, counting distinct channels separately. Terms truncated by a
boundary are assigned the same containers as their bulk counterparts. Let
a=12 be a safe diameter bound, let zeta>=1 bound the number of containers
intersecting any one container, and let

    g=max(4 delta z^4, 8 kappa (z-1)^2).               (7)

The second entry safely covers either instrument convention. The geometrical
zeta is finite on Z^d, with a uniformly bounded number of containers per
anchor. If delta=kappa=0, no bounded terms are present and the eventual
spatial comparison is exact once the electric neighborhood is included.

For completeness, the bounded-generator propagation estimate follows by
separating terms disjoint from a test support X. Those disjoint terms generate
a UCP contraction and commute with a local elementary test map Q_X satisfying
Q_X(I)=0. Variation of constants and division by ||Q_X||_cb give the Volterra
inequality

    C_X(s) <= ||A_Y|| 1_(X intersects Y)
                + sum_(Z intersects X) g int_s^t C_Z(u) du,   (8)

where C_X bounds ||Q_X V(s,t)A_Y||/||Q_X||_cb. One can take a supremum over
normal completely bounded local maps, or simply the elementary maps needed
at each subsequent step. All norms include spectator amplifications.
The n-th iteration of (8) is a sum over n successive overlapping containers,
with time-simplex volume (t-s)^n/n!. If X is one of the uniformly bounded
test containers, there are at most zeta^n paths. None reaches Y in fewer
than ceil(dist(X,Y)/a) steps. The bounded finite-volume residual in this
iteration tends to zero by the factorial. Thus

    ||Q_X V(s,t) A_Y||
      <= ||Q_X||_cb ||A_Y||
         sum_(n>=ceil(dist(X,Y)/a)) [zeta g(t-s)]^n/n!
      <= ||Q_X||_cb ||A_Y||
                    exp(e zeta g(t-s)-dist(X,Y)/a).    (9)

If a test container is the union of a fixed number of the standard ones,
a harmless geometrical prefactor suffices. The last inequality follows by
inserting exp(n-D)>=1 in the exponential tail starting at D. This proof
uses contractivity, support overlap, and cb bounds, not a finite local
Hilbert-space dimension.

For two finite graphs that agree on a large neighborhood of Y, the Duhamel
identity for their interaction-picture propagators inserts differences of
local terms. Such a difference annihilates I, has cb norm at most 2g, and
is confined to a boundary container. Apply (9) and sum those containers.
On the decorated Z^d lattice, the number at distance in [r,r+1) from Y is
bounded by c_d |Y| (1+r)^d. In particular, if every differing container has
distance at least R from Y, a sufficient bound is

    ||(V_Omega(0,t)-V_Lambda(0,t)) A_Y||
      <= c_d |Y| ||A_Y|| g T exp(e zeta g T)
                           sum_(r>=floor R) (1+r)^d exp(-r/a),   (10)

uniformly for 0<=t<=T. Constants absorb the finite container multiplicity and
the factor 2. The displayed summable tail is preferable to optimizing its
inessential polynomial prefactor. It tends to zero as R tends to infinity.
The same proof works after any finite ancillary matrix amplification.

Now remove M **at each fixed finite volume**. In a charge/electric basis,
exp(-i K t sum D_e^(M)) converges strongly, uniformly on compact t intervals,
to the uncapped electric unitary. It is eventually exactly equal on every
fixed finite set of basis vectors. Density and uniform unitary bounds prove
the assertion for all vectors. The bounded interaction-picture coefficients
and their adjoints consequently converge strongly; multiplication on trace
class and the bounded Dyson series give strong trace-class convergence of
their propagators, uniformly on compact intervals. Their adjoint actions on
every bounded A converge ultraweakly. Bounds (9)-(10) pass by lower
semicontinuity of operator norm; the amplified versions pass as well.
No limit in operator norm with respect to M is claimed or needed.

For the full Heisenberg evolution, use

    tau_Lambda(t)A = V_Lambda(0,t) alpha_(t,Lambda)^D(A).       (11)

Once Lambda includes Y^+, the electric factor on A_Y is exactly the same
for both volumes, at every t and every cutoff. It is supported on Y^+ and
has norm ||A_Y||. Apply (10) with Y^+ and that time-dependent input; the
estimate is uniform over its entire unit ball, so its lack of norm time
continuity causes no problem. The differing induced-star terms are confined
to a fixed boundary strip. Their range, cb norms, and count per anchor obey
the same bounds. This proves

    sup_(0<=t<=T) ||tau_Lambda(t)|_(A_Y)-tau_Omega(t)|_(A_Y)||_cb -> 0   (12)

as the distance from Y to both boundaries tends to infinity. Here the cb
norm refers to restriction to that fixed local algebra, with the common
larger algebra as codomain. Equation (12), or (10) with the enlarged support,
is the required volume-uniform conclusion for the **target**.

The literature check was limited and explicit. The bounded propagation
method is established machinery; [Barthel--Kliesch v2](https://arxiv.org/html/1111.4210v2)
Sections II--III, V and Appendix B were read for its support-path and
contractivity formulation. [Nachtergaele--Vershynina--Zagrebnov v2](https://arxiv.org/html/1103.1122v2)
Section 2, Assumption 1 and Theorems 1--3 were read for the cb setup and
the explicitly required norm continuity of finite-volume generators.
That hypothesis is met after (6), not assumed for the uncapped picture.
Equations (5)-(12) supply the additional cutoff and normality argument here.
This is not a claim to have independently proved or fully reviewed every
result in either paper. Versioned retrieval identities and exact read scope
are recorded separately; no full third-party text is redistributed.

## 4. Infinite-volume maps, states, constraints, and boundary conditions

For each bounded local A, (12) defines tau(t)A in A, uniformly on compact
times. Contractivity extends tau(t) and the convergence to every quasi-local
A. The limit is unital and completely positive, since these properties hold
in every finite matrix amplification. The autonomous finite-volume semigroup
law passes to the limit: first approximate the fixed quasi-local tau(s)A by
a local observable, and use contractivity. Thus tau(t+s)=tau(t)tau(s).

There is a precise local normality statement. In any representation normal
on all finite factor algebras, tau_Lambda(t)|_(A_Y) is normal. Estimate (12)
is uniform over the local unit ball. Its norm limit is therefore still a
normal map from B(H_Y) into that representation's von Neumann closure:
compose with a normal functional, and use norm closedness of the local
predual. In particular, if omega is a state normal on every B(H_X), then
omega_t=omega composed with tau(t) is locally normal. Finite-volume
expectations are continuous in t against local normal functionals; their
compact-time uniform approximation proves continuity for omega_t(A), first
for local A and then for quasi-local A. Equivalently, one may obtain
point-strong-star continuity in a locally normal representation from the
finite-volume maps and the same uniform approximation. No uniform electric
moment or decay of initial spatial correlations is required for these
qualitative statements.

At a fixed t a CP map also has its standard normal bidual extension. This
does not establish a normal channel or density in an arbitrary chosen
infinite-system Hilbert representation. The latter can be false, as below.

The finite-volume Hamiltonian and jumps commute with every local Gauss
unitary and with its physical spectral projection

    P_x^G=1_(div E_x-q_x+1_A(x)=0).                    (13)

The conservation can be checked on each legal shift in (1). A move inside a
finite graph also preserves the full lattice constraint when exterior
variables are left untouched. Hence tau_Lambda(t)(P_x^G)=P_x^G and the
identity passes to tau(t). A locally normal physical initial state, defined
by omega(P_x^G)=1 for every x, remains physical. Gauge-invariant observables
remain gauge invariant. This uses local spectral projections, not an
undefined projection onto all infinitely many constraints at once.

The result applies to induced-graph exhaustions: every fixed finite
neighborhood is eventually inside the graph. Boxes are a simple choice.
There is no assumption that boundary/volume ratios tend to zero for the
local dynamics statement. It also applies to uniformly finite-range,
uniformly cb-bounded boundary perturbations whose supports recede to infinity,
and to compatible periodic boxes with every period tending to infinity,
provided the local bipartition and orientation are identified consistently.
Electric boundary prescriptions require the same commuting, bounded-range
structure and eventual exact agreement on each interior neighborhood; their
effects on the bounded interaction picture must obey the above uniform
support and norm bounds. Arbitrarily growing noncommuting boundary
interactions, boundary terms reaching into the bulk, or a nonreceding
boundary are not covered.

The dynamics is constructed on the common kinematic algebra before choosing
physical states. Finite induced-graph Gauss subspaces with zero exterior
flux are not naturally nested and need not be the marginals of an arbitrary
infinite physical state. Boundary independence of the maps does not imply
that arbitrary boundary-selected state sequences have the same limit.
For finite initial states converging on every fixed local algebra, the
corresponding expectations converge at each fixed time to the evolved limit
state. Local trace-norm convergence of their marginals suffices for compact-
time uniform expectation convergence. Mere weak convergence is not promoted
to that stronger uniform-in-time claim, nor does it ensure local normality
of the initial limiting state.

## 5. Two explicit failed stronger claims

**Norm time continuity is false.** Take the allowed delta=kappa=0 and any
elementary plaquette p, with all A plus and all B empty. In the physical
subspace of divergence-free circulations supported on p, let |m> have
integer circulation m. The electric energy is 4 K m^2: the linear electric
term sums to zero by Gauss. The bounded gauge-invariant Wilson shift satisfies
W_p|m>=|m+1>. Consequently

    ||alpha_t^D(W_p)-W_p||
      >= |exp(i K t(8m+4))-1|.                        (14)

At t_m=pi/[K(8m+4)], the right side is 2, which is also the general upper
bound. Since t_m tends to zero, the full local bounded algebra does not carry
a norm-C0 semigroup. This counterexample uses a physical bounded observable,
not just a gauge-violating operator or a distributional field eigenstate.
Each |m> is a normalizable finite-region vector. For any one fixed local
normal state, strong-unitary/trace-class continuity still holds.

**Global normality in a chosen folium is not automatic.** Select infinitely
many separated plaquettes and prepare on each the physical vector
(|0>+|1>)/sqrt(2), with all other fields zero and the same fixed matter.
This is a locally normal physical product over the separated blocks. Again
take delta=kappa=0. At t=pi/(8K), each block becomes
(|0>-i|1>)/sqrt(2), whose squared overlap with the initial block is 1/2.
The infinite evolved product state is not normal in the initial incomplete
tensor-product representation. To see more than just a vanishing overlap,
let Q_(n,infinity) be the projection onto the initial vector on every block
from n onward. In that representation Q_(n,infinity) increases strongly to
I as n tends to infinity, because finite modifications are dense. A putative
normal evolved state would give Q_(n,infinity) expectation zero for every n,
by taking the decreasing limit of finite tail products with expectations
2^(-M). Normality and Q_(n,infinity) -> I contradict this. The evolved state
nevertheless remains normal on every finite local algebra, as proved above.

These are scope countercontrols, not counterexamples to (12). No singular
local states are assumed to have continuous expectations, and no global
trace-class density on a preferred infinite tensor product is asserted.

## 6. Initial local formation diagnostic

Let omega_0 be all A plus, all B empty, and zero electric field on every
link. This is a locally normal Gauss-legal product state. Fix e=(a,b), with
degree z at a. In B_(e,sigma) the old plus at a first moves to a distinct
neighbor c!=b. Birth then sets q_a=sigma, q_b=-sigma; the old record at c
remains plus. There are z-1 such legal paths. Their final charge/field words
are orthogonal. Thus

    omega_0(B_(e,sigma)^* B_(e,sigma))=z-1,
    initial resolved rate for (e,sigma)=kappa(z-1),
    initial total edge rate=2 kappa(z-1).              (15)

The two charge orientations have orthogonal final A-charge ranges. In fact
B_(e,+)^*B_(e,-)=0 on the entire effective space. The coherent edge channel
therefore has the same loss operator as the two resolved channels together.
For the actual initial state, its normalized output is a pure superposition
of the two orthogonal normalized resolved outputs. Discarding the resolved
charge mark instead gives their equal mixture. Their purities are 1 and
1/2 and their trace distance is 1/2. Equality of instantaneous loss does not
make the instruments or their later histories identical.

For one B site b, each neighboring a contributes in two ways: b is the
new pair endpoint, or b receives the old plus. Each alternative has
2(z-1) orthogonal marked paths. Hence, with the channel normalization above,

    (d/dt) omega_t(n_a)|_0=0                    (a in A),
    (d/dt) omega_t(n_b)|_0=4 kappa z(z-1)       (b in B).       (16)

The Hamiltonian contributes zero at the initial instant. More generally it
preserves total record number; the electric term commutes with every n_x.
For (16), it is enough that the initial vector is an n_b eigenvector of
eigenvalue zero. The finite local birth calculation is unaffected by a
boundary outside its radius-two site neighborhood. To justify the derivative
after the volume limit, put A_b=L(n_b). Since n_b commutes with the electric
part, A_b is a bounded local operator independent of a sufficiently distant
boundary. The finite-volume weak identity is
omega(tau_Lambda(t)n_b)-omega(n_b)=int_0^t omega(tau_Lambda(s)A_b) ds.
The volume estimate passes this scalar integral to the limit. Local normality
and continuity then give its derivative at zero. This is an initial
derivative, not a product-law closure for positive time.

The model and omega_0 are invariant under translations preserving the
bipartition. Consequently their spatial mean record density obeys

    rho(0)=1/2,
    rho'(0)=2 kappa z(z-1),
    initial event intensity per lattice vertex=kappa z(z-1). (17)

The mean here is the expected per-vertex occupation, not an almost-sure
concentration assertion. Each event creates two records, which checks the
factor in (17). For d=2,
3,4, the B-site derivatives divided by kappa are respectively 48,120,224;
the mean-density derivatives are 24,60,112. These formulas vanish at
kappa=0 and hold for either of the stated instruments. A normalized coherent
sum divided by sqrt(2) would halve the rate and is not the stipulated jump.
For kappa>0 the sum of the initial rates over all of Z^d is infinite; (15)--(17)
are local intensities, not a finite global first-event clock or a claim to
have constructed a global jump unravelling.

## 7. Independent controls and limits

`exact_control.py` is a new standalone implementation with no author or older
model-builder imports. It constructs complete radius-two site balls around
a B site in d=2,3,4, orients every edge A to B, and assembles effective births
as an actual old-record hop followed by pair creation. It checks every
resulting integer Gauss equation, immutable old charge, hard capacity,
record increase by two, total charge, mark norm, coherent/resolved rate and
central occupation derivative. The three balls have respectively 13,25,41
vertices and 16,36,64 edges. All neighboring A stars are complete, so the
central diagnostic is exactly the infinite-lattice local one. Boundary B
degrees need not be regular. The same control records the exact rational
times in (14) and finite products used in the representation countercontrol.
Floating time columns are illustrations; the phase identity and rate checks
use integer or Fraction arithmetic.

`support_control.py` independently enumerates every relative A pair sharing
a B neighbor in d=2,3,4. With exact incidence distances it checks the
two-star diameters before and after one electric enlargement, and the
corresponding jump-star diameters. The maxima are 8 to 12 and 4 to 8,
respectively. It does not replace the commuting-operator cancellation in
(5) by repeated graph expansion. Both scientific controls ran successfully
on their first execution.

No failed scientific assertion or
abandoned computation was overwritten. The rejected proof routes are the
uncapped norm-continuity import and the global-folium inference in Section 5.
One combined tool read was truncated; the missing external theorem/proof
sections were reread separately before this report. Complete subprocess
stdout, stderr, command argv, source hashes, times and return codes are
preserved. One report-edit patch failed to match its expected line wrapping;
it made no file change and was retried against the displayed exact lines.
That tooling failure is recorded in ATTEMPTS.json. The literature retrieval
script records the versioned HTML hashes
without redistributing third-party full text. These finite controls test
normalizations and the topology counterexamples; they are not a simulation
of the infinite process or substitutes for Sections 2--4.

The conclusion is a local infinite-volume dynamics for this stipulated
compensated rotor target, at fixed K,delta,kappa and compact ordinary times.
It does not control microscopic epsilon/spin errors uniformly in volume,
construct an autonomous birth reservoir, prove a thermodynamic phase, select
a vacuum, establish long-time relaxation or a photon theory, or identify the
resources with native record axioms. Those questions remain outside this
bounded reconstruction. The new root candidate remains unread until after
the PRE seal and explicit comparison authorization.
