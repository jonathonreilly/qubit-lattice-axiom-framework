# An original microscopic local quantum/marked limit in a volume-spin window

**Type:** bounded theorem candidate. **Status:** conditional-support, author
composition of supplied mathematical laws and explicitly provisional inputs.
No formal review, audit or framework adoption is supplied here.

## 1. Result and exact dependency boundary

Fix positive K, delta and kappa, one of the two original instruments below,
and the bare preparation Omega. Let L be even, L>=64, n=L^3/2 and S a positive
integer. Set

    epsilon^2 S(S+1)=delta/K.                                      (1)

For every sequence with

    L -> infinity, S -> infinity, epsilon n^3 -> 0,                (2)

the actual compensated microscopic process has a unique local joint limit:
on each fixed finite output cell set X, jointly with the complete original
labels and continuous timestamps at each fixed finite set F of A centers,
its subnormalized quantum output densities converge in integrated trace norm,
uniformly for final time 0<=t<=T for every fixed T<infinity. This limit is the
Omega process of the exact rotor law in provisional PR9399, head
5bec44a4a08d7e7727e8d23d94c884fc32332b05. It is not a new choice of that law.
The microscopic approximation is in original physical coordinates, from bare
Omega, without an observed vacancy grade or discarded coherent cross term.

The window is equivalently n=o(S^(1/3)), or L=o(S^(1/9)), with L still tending
to infinity. It is a sufficient window, not a sharpness claim. The error below
has two separately controlled contributions: the checked full finite-volume
microscopic error, and an explicit local thermodynamic error. In particular,
this is not an estimate uniform over arbitrary growing microscopic volumes.

Two new joins are proved here rather than assumed: (i) the source's
operator-valued timestamp-kernel bounds give integrated local trace norm,
not only convergence for each fixed history event; (ii) a constructive
finite-horizon localization recursion makes this bound compatible with (2).
The triangle inequality then gives the result.

Load-bearing inputs, each kept at its own scope:

* G: campaign original-record-growing-volume-route/WORKING_PROOF.md,
  SHA63394b20...; root focused check independent-original-growing-volume-check/
  REPORT.md, SHA8d9d9809.... G proves the quantitative microscopic/spin/rotor
  finite-volume full-output comparisons restated in section3.
* R: the complete PR9399 canonical note
  ORIGINAL_RECORD_THERMODYNAMIC_DYNAMICS_AND_ENERGY_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-30.md,
  SHAaf19d44a.... R supplies the exact rotor finite maps, connected locality,
  original instruments and their thermodynamic construction. Its full source
  review and precursor focused check were read. The PR remains OPEN and
  provisional. No review grade is inherited by this new composition.
* The actual landed compensation, canonical coefficient and local-pair sources
  supply the literal operators. Their complete relevant proofs were read at
  current main fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7. Exact full identities
  appear in SOURCE_BINDINGS.json. Earlier finite-rate formation is used for
  the carrier and elementary hop/birth definitions, not its different scaling.

R's energy and early-power results are not premises or conclusions of this
composition. Its original first-birth source was nevertheless read to verify
that this transitive branch is confined to R's separate energy claims.
The PR9412 local-output proposal is comparison prior: its arbitrary-volume
subsequential result is not an input to this proof and is not superseded in
that larger volume domain.

## 2. Literal laws, carrier and observation maps

The lattice is Z^3 with A the even sublattice and B its complement, or its
even periodic cubic quotient. Orient every edge a->b, a in A. Each microscopic
vertex has the supplied qutrit basis 0,+,- with q=diag(0,1,-1), n_x=q_x^2.
An edge has integer spin S, E=S_z, U=S_+/sqrt(S(S+1)); U and U* are partial
shifts with their true boundary zeros. The physical constraint is

    div E_x=q_x-1_A(x).

F_a is the unsigned sum of hops moving the existing charge q_a to an empty
neighbor b, emptying a and shifting E_ab by -q_a. Its adjoint reverses it.
The original j_(ab,sigma) fills two empty endpoints with sigma,-sigma and
shifts E_ab by sigma. Choose exactly one instrument:

    resolved: j_(ab,+), j_(ab,-) separately;
    coherent: j_(ab,+)+j_(ab,-), one unnormalized label per edge.

The coherent label is never refined by a hidden sign. All Hamiltonian terms
preserve total occupation, all original jumps add two, and all preserve Gauss.
With W=sum_A(1-n_a), P=1_(W=0), the actual supplied compensation is

    Q_a=product_(c in A, c!=a, dist(c,a)<=2) n_c,
    C_S=sum_a [F_a*F_a-D_(a,S)+D_(a,infinity)]Q_a,
    D_(a,S)=diag(F_a*F_a),
    D_(a,infinity)=n_a sum_(b~a)(1-n_b).

The microscopic Hamiltonian and jumps are exactly

    H_(epsilon,S)=delta epsilon^-4(W+epsilon T+epsilon^2 C_S),
    T=-sum_a(F_a+F_a*),
    L_(epsilon,mu)=sqrt(kappa) epsilon^-1 j_mu.                    (3)

This is the compensated model. The compensation is an additional supplied
interaction, not the unchanged uncompensated law or a native M2 derivation.
Here 'original' describes the specified microscopic instruments, states and
coordinates of (3). It does not erase that model hypothesis.

Omega has every A plus, every B empty and every E zero. It is physical and
has consistent product marginals on rooted finite regions. No dressed state
is prepared. Time t in (3), G and R is the same supplied continuous parameter;
there is no time rescaling in this composition and no physical calibration.
The divergent microscopic coefficients and the finite coefficients K,delta,
kappa have already been related by (1), not fitted to a record rate.

The canonical positive-overlap effective coefficients are, with
Pi_r=1_(W=r), A1=Pi_1 T P, M=A1* A1,
Z=Pi_2 T Pi_1 A1, C_r=Pi_r C_S Pi_r,

    H2_S=C_0-M=D/[S(S+1)],
    H4_S=M^2-(M C_0+C_0 M)/2+A1* C_1 A1-Z*Z/2,
    B_(mu,S)=-P j_mu Pi_1 T P=P j_mu F_a P.                       (4)

Thus delta epsilon^-2 H2_S=KD exactly. At rotor order C_0=M, and the
occupancy gate cancels every disjoint-star pair in A1*C_1 A1-Z*Z/2:

    H4_infinity=-2 sum_(unordered a,c, dist(a,c)=2) S_ac* S_ac,
    S_ac=F_c F_a P,
    D=sum_(a->b)(1-n_b)E_ab(E_ab-q_a),
    h=KD+delta H4_infinity,
    L_mu=sqrt(kappa) B_(mu,infinity).                             (5)

These are exactly R's coefficients, with the same unordered-pair factor -2,
occupied-B electric mask and original coherent sum. In (5) P denotes the
all-A-occupied input/output carrier; the complete local words do not insert
a nonlocal dynamical projector between their primitive operations.

For local comparison group each rotor with its B endpoint. A target A cell
is C^2 spanned by +,-; a B cell is C^3 tensor its six incoming ell2(Z) factors.
The microscopic cell has C^3 also at A and finite-spin incoming factors at B.
Embed spin E=-S,...,S by its actual integer basis into ell2(Z), and target
C^2 at A by its isometry into the occupied subspace of C^3. On a fixed X this
gives a common ambient separable Hilbert space Htilde_X, with full algebra
B(Htilde_X). There is no identification of that algebra with the norm closure
of simple one-cell tensors. The target local states are supported on the
occupied-A subspace. All observation maps are ordinary partial traces,
these local isometries, and forgetting original labels outside F. They are
trace-norm contractions. No projection followed by renormalization is used.

All links of a Gauss star are contained in a finite enlarged cell set. The
finite laws preserve its bounded Gauss spectral projection. Eventual rooted
embeddings of that set allow its expectation-one identity to pass to the
local limit. No global infinite Gauss projector is needed.

## 3. The finite-volume input and its exact use

G proves constants c0>0 and A_T,B_T<infinity, independent of n,S and of the
classical register size, such that whenever epsilon n^2<=c0,

    d_full(micro_(L,S),target_(L,S))
                    <=A_T(epsilon n^3+epsilon^2 n^6),
    d_full(target_(L,S),rotor_L)
                    <=B_T n^6/[S(S+1)].                         (6)

The first bound is for physical output coordinates and any P-supported input;
the second is used here only from Omega. The distances include joint full
quantum output and the complete original finite-volume timestamp instrument,
uniformly in t<=T. G obtains the latter by dimension-independent finite-register
bounds and increasing time partitions, retaining original label order and
multiple events in each bin. It does not infer full path variation solely
from a finite collection of CDFs. The finite capacity is floor(n/2) births
from Omega, because each birth adds two and there are 2n hard-core vertices.

Applying the observation contractions above to (6) gives, for every fixed X,F,

    d_(X,F,t)(micro_(L,S),rotor_L) <= E_T(L,S),
    E_T=A_T epsilon n^3+(A_T+B_T K/delta)epsilon^2 n^6.            (7)

The substitution uses 1/[S(S+1)]=(K/delta)epsilon^2. This is a same-volume
comparison; no thermodynamic limit has yet been taken. Condition (2) implies
epsilon n^2<=c0 eventually and E_T->0. No uniform estimate for arbitrary
microscopic initial states or an input-channel norm is obtained from the
Omega-specific second bound. R already constructs the full finite-volume
rotor maps; its auxiliary field boxes are removed at fixed finite volume
before the thermodynamic passage. This composition introduces no extra
field cutoff or unproved interchange with S or L.

For precision, let Xi_(F,t) be the disjoint union of the empty history and all
finite ordered original-label lists with 0<t1<...<tm<t. Use counting measure
on labels and Lebesgue measure on each time simplex, plus the empty-history
atom, denoted mu_(F,t). For either finite process let sigma_(X,F,t)(xi) be
its positive subnormalized local quantum density with respect to this measure.
Then the distance used here is

    d_(X,F,t)(sigma,tau)=integral ||sigma(xi)-tau(xi)||_1 dmu.     (8)

There is no factor 1/2 in this convention. The total trace integral is one.
It controls classical total variation and every bounded, history-dependent
local quantum test. It is unaffected by replacing mu with any equivalent
positive domination measure. At t=0 only the empty atom remains.

## 4. The thermodynamic locality input, with its constants

R constructs the exact rotor finite dynamics first on trace class in the
interaction picture of KD. Its bounded coefficients are strongly continuous
there. Dual integrals are strong/ultraweak; no B(H) norm-Bochner continuity is
assumed. The diagonal electric terms strongly commute, so conjugation of a
local bounded operator has precisely a one-step support halo and unchanged
norm. The full generator, including losses, annihilates a disjoint observable.

The complete-word bounds on the cubic lattice are

    ||A_a||<=2592 delta,
    ||Gamma_a||<=80 kappa,
    sum_(mu at a)||L_mu||^2<=108 kappa,
    lambda=5184 delta+160 kappa,
    a=16641 lambda,  tau=1/(2a).                                (9)

Here A_a is half the sum of the 18 magnetic pairs touching a. The electric
interaction-picture center generator has support in graph ball B_4(a),
with 129 cells; at most 129 center labels can touch one cell. For an initial
anchor of x cells, a nonzero length-l connected string is counted by
16641^l(q)_l, with q=max(1,ceil(x/129)). Consequently define

    R_(q,m)(z)=sum_(l=m+1)^infinity binom(l+q-1,l) z^l.           (10)

For monitored centers F only the removed monitored gains fail to annihilate
I. Their persistent anchor is inside union_(a in F) B_2(a). If the output is
supported on X, a valid initial anchor is

    Y=X^+ union union_(a in F) B_2(a),
    |Y|<=7|X|+25|F|.                                           (11)

Monitored centers' magnetic terms are ordinary unital background terms;
they are not incorrectly confined to B_2. Their larger B_4 supports are
already included in the connected-string count.

For a fixed specified history xi=(mu1,t1,...,muv,tv), let K_xi^Lambda(O) be
the exact finite-volume Heisenberg density kernel, retaining all unobserved
exterior gains and every loss. If two finite approximants agree through the
first m background insertions around Y, R's direct expansion gives

    ||K_xi^Lambda(O)-K_xi^Lambda'(O)||
       <=2 ||O|| w(xi) R_(q,m)(a h),
    w(xi)=product_i ||L_mui||^2,  0<=h<=tau.                    (12)

The sum over distributing l background insertions among v+1 waiting segments
is h^l/l!, irrespective of the number and times of the specified jumps.
Those jumps do not enlarge Y. Thus (12) is uniform over histories and over
the entire unit ball of the finite regional algebra. Canonical open and
periodic approximants obey the same constants. The torus comparison uses a
rooted interior lift: a seam cannot enter a prefix before its support reaches
that seam. It does not treat the seam as a short ambient-coordinate edge.

The scalar measure w dmu has total mass

    exp(r'_F h),  r'_F=sum_(mu at F)||L_mu||^2<=108 kappa |F|.    (13)

This is only a dominating measure; it is not a replacement Poisson instrument.

## 5. From density kernels to the actual joint output norm

This step is stronger than eventwise weak convergence, and is explicit.
Embed two finite approximants in a common finite ambient region, use the same
normal input there (in particular the product Omega), and normally amplify
local maps by the spectator identity. For each history xi, the difference
of local output densities is Hermitian trace class. Taking the supremum of
its pairing against self-adjoint O in the whole unit ball of B(H_X), (12)
gives

    ||sigma_Lambda(xi)-sigma_Lambda'(xi)||_1
                         <=2 w(xi) R_(q,m)(a h).                (14)

Taking that supremum is legitimate because (12) is uniform over O; it is
not convergence of a chosen countable list of matrix elements. The finite
predual construction gives strongly measurable trace-class density kernels.
Hence integrating (14), then using (13), yields

    d_(X,F,h)(Lambda,Lambda')
                         <=2 exp(r'_F h) R_(q,m)(a h).          (15)

The same norm estimate holds for a finite classical register of past history:
apply it blockwise and sum input trace norms. Equivalently, test the current
history against any finite measurable partition with an arbitrary bounded
local operator on each partition cell. The integral of (12) is independent
of the partition cardinality. Such tests norm the L1 trace-class output:
separability of H_X permits a countable norming family of finite-rank rational
self-adjoint contractions and measurable near-maximizing choices. One may
also use increasing finite partitions and trace-class conditional averages.
There is no need to assume a norm-measurable B(H_X)-valued sign function.

This uniformity permits slice composition with history-dependent future
observables. A complete joint record/quantum channel is trace preserving;
its adjoint on classical block observables is unital CP and has norm one.
Signed output differences therefore contract. Only the intermediate
no-monitored-jump pieces are trace decreasing, with all monitored losses kept.
No quantum intervention or modified instrument is inserted.

## 6. A constructive all-time local error

Here is one conservative computable resource bound; it is not claimed sharp.
Choose an integer r0>=1 with X union F inside the coordinate cube
C_r0=[-r0,r0]^3. Let f=|F| and fix T. Put

    M=max(1,ceil(2aT)).                                         (16)

For t<=T use M equal slices of length h=t/M<=tau. Given an integer k>=0,
recursively define, for j=1,...,M,

    q_j=max(1,ceil([7(2r_(j-1)+1)^3+25f]/129)),
    m_j=4q_j+k,
    r_j=r_(j-1)+8m_j+4.                                       (17)

At backward step j the future quantum output is supported in C_(r_(j-1));
future record entries are passive classical indices. Its anchor (11) lies
in C_(r_(j-1)+2), and every background insertion expands the coordinate
radius by at most eight. The open finite map on C_rj thus reproduces every
prefix through order m_j, including its full electric halo and complete words.
The extra four in (17) is conservative support slack. All monitored jumps
at F are retained. No primitive hop is individually clipped inside a word.

For 0<=z<=1/2, comparison with the full generating series at 3/4 gives

    R_(q,m)(z) <=(2/3)^(m+1) 4^q.

With m=4q+k the extra factor is [4(2/3)^4]^q=(64/81)^q<=1, so

    R_(q,4q+k)(z) <=(2/3)^(k+1).                              (18)

Compare a sufficiently large periodic torus evolution over M slices with
the nested sequence of open finite maps on C_r1,...,C_rM, working backwards
from the final observable. Each replacement costs at most
2 exp(r'_F T/M)(2/3)^(k+1) by (15). All earlier exact joint channels contract,
and every later localized observable has norm at most one and the support
used in (17). Telescoping gives M times this cost. This argument can first
be made with finite history partitions; the estimate is independent of the
partitions, which can then be refined in the predual L1 norm.

If L>=2r_M(k)+16, the nested maps have the same rooted realization in the
torus and on the lattice. Two such tori are consequently within

    B_(T,X,F)(k)=4M exp(108 kappa f T/M)(2/3)^(k+1)               (19)

in (8), uniformly for t<=T. The factor four allows comparison of both exact
processes with the same nested approximation; no cancellation is needed.
The initial marginal of Omega on C_rM is identical for both approximants.
Taking the second torus to infinity gives the same bound between one torus
and the local limiting output. The universal alternative bound is two.
For the uniform-in-t statement all history densities can be placed in the
single space L1(Xi_(F,T);trace class), extended by zero on histories having
an event after t; its restriction agrees exactly with (8).

For every fixed k all radii in (17) are finite. Thus as L->infinity one can
take k->infinity while L>=2r_M(k)+16. This proves uniform-in-t L1 Cauchy
convergence in the complete Banach space of trace-class history densities.
The limit is positive, has total trace one, and defines locally normal event
states. Its pairing with each bounded local O on every Borel event equals
R's already unique instrument limit. Therefore it is exactly that process,
not a second construction with an unidentified holding term.

For an explicit modulus for every L, put

    k_L=max{k>=0: 2r_M(k)+16<=L},
    b_(T,X,F)(L)=min(2,B_(T,X,F)(k_L)),                         (20)

using b=2 if this set is empty. Then b(L)->0. Formulae (9),(16)-(20) are
an actual finite algorithm using only the source locality constants and
observation data. They may give astronomically pessimistic radii; no useful
numerical resource size or finite experiment is promised.

There is also a purely asymptotic rate interpretation. Let R_j=r_j+1,
R_0=r0+1. From (17),

    R_j<=15 R_(j-1)^3+(44+7f)(k+1).

Set A_1=15R_0^3+44+7f and A_j=15A_(j-1)^3+44+7f for j>=2. Induction gives

    r_M(k)+1<=A_M(k+1)^[3^(M-1)].                              (21)

Consequently b(L)<=C exp(-c L^[1/3^(M-1)]) for sufficiently large L, with
positive finite constants determined by (9),(16),(21). This rate is an
optional consequence of the explicit recursion, not a Lieb-Robinson bound
imported for an unbounded generator. Only b(L)->0 is needed below.

## 7. Combined error and unique simultaneous limit

The triangle inequality between microscopic, same-volume rotor, and infinite
rotor local joint outputs gives the promised quantitative statement:

    sup_(0<=t<=T) d_(X,F,t)(micro_(L,S),infinite rotor)
                <=E_T(L,S)+b_(T,X,F)(L),                       (22)

provided epsilon n^2<=c0, with E_T from (7). If a particular k satisfies the
explicit buffer condition, replace b by min(2,B(k)). This bound retains all
original timestamp labels and the final local quantum coherences.

Along (2), E_T->0 and b(L)->0 independently. There is no order swap of two
uncontrolled limits and no subsequence-dependent choice of a quantum law.
Every such simultaneous sequence has the same limit. For example, for large
integer S choose the even side

    L(S)=2 floor(S^(1/12)/2).

Once L>=64, n is of order S^(1/4), E_T=O_T(S^-1/4), and the thermodynamic
term tends to zero by (20) (indeed faster than any power asymptotically using
(21), with extremely poor T-dependent constants). Thus the total local
joint error is O_(T,X,F)(S^-1/4) asymptotically. The statement is a window
existence and convergence result; it is not a practical spin-size estimate.

The same sequence works for every fixed finite X,F,T. Countably exhausting
regions and integer time horizons yields the compatible family, without a
second sequence selection: each fixed observation already converges uniquely.
Fixed-time consistency under output partial traces and forgetting monitored
centers passes through (22). Classical histories also have the usual time
restriction consistency. Quantum output at T with later marks forgotten is
not identified with the earlier quantum state at t<T: it has undergone the
unconditioned future evolution. The correct temporal relation is R's CP
instrument concatenation. No arbitrary inserted quantum measurements have
been included in (22).

R's local count estimate, inherited by the identified limit, is (v>=1)

    Pr[N_F(T)>=v]<=(80 kappa f T)^v/v!,
    E N_F(T)<=80 kappa f T.                                    (23)

This supplies a locally finite original marked configuration on the countable
lattice, with locally normal quantum states for finite-region events. It does
not supply a global first jump or finite total event number. Gauss constraints,
even-sublattice covariance and occupied-A support have the precise local meaning
explained above and in R. For a fixed positive-probability history event, local
conditional densities also converge after division by its convergent nonzero
probability. There is no bound uniform over rare conditioning events.

## 8. What has and has not been identified

The unique limit in (22) is unique as the simultaneous local output limit of
the declared microscopic family from Omega. It is not a claim that every
abstract weak solution on an unrestricted unbounded-generator domain is unique.
R identifies its dynamics on electric-time-smoothed bounded local tests, for
which the electric commutator is a bounded local operator; its full quantum
Hamiltonian, gains and losses are (5). Thus no fast vacancy-supported term
remains unidentified in this window. This does not close that term for arbitrary
volume-spin sequences in the stronger volume-uniform problem of PR9412.

The conclusion is about probabilities and bounded local quantum outputs.
Trace norm alone does not transfer the microscopic energy (whose coefficients
diverge), quadratic field expectations, or unbounded record-count moments.
In particular (23) is a statement about the identified limit. The present
proof does not infer convergence of microscopic E N_F merely from path total
variation: rare microscopic histories can have volume-dependent counts.
Additional already-proved moment estimates could be combined only with their
own hypotheses and source identities. None is silently imported here.

The target has the finite local-energy balance established separately in R,
but no limit of microscopic energy density, physical heat/work, supplier
ledger or energy calibration is asserted. No global trace-class state, quantum
disintegration conditional on the entire infinite record, point-norm C0
semigroup, equilibrium/phase, or physical clock selection follows.

The compensated model's qutrit and link carrier, tensor product, Born/GKSL law,
staggered background/Gauss condition, Omega preparation, positive couplings,
continuous time, original instruments and scaling are supplied hypotheses.
Current minimal axioms and registered scale-reference, kinetic-isotropy and
realized-state primitives were checked against their actual source. They do
not select those hypotheses. In particular no permanent site-record or native
M2 realization is inferred by naming a birth a record. These are physical
bridge obligations, not asserted contradictions with the axioms.

## 9. Evidence, independence and remaining gate

This is an analytic author composition. No new numerical experiment, author
runner rerun, formal reviewer, audit, commit, push or PR was performed. Complete
source and check reads and exact blob/hash comparisons are recorded separately.
The agent has prior authorship/checking involvement in campaign precursors;
this result is not represented as independent validation of G or R. Their
existing receipts support reuse only at the frozen scopes read here.

The new load-bearing argument for focused independent checking is sections5-7:
whole-unit-ball kernel duality, finite-classical-register slice contraction,
actual support recursion, and the simultaneous-window triangle inequality.
No target-equivalent missing lemma remains in this proposed conditional
composition. It is frozen for root independent reconstruction before downstream
use; until that check it remains an author theorem candidate.
