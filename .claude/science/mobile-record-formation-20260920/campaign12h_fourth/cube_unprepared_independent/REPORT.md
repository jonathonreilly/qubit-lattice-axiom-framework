# Original cube: local density limits with an unselected first output

Independent reconstruction, 2026-09-23, before candidate access.

**Conditional consequence.** Assume the supplied, provisionally checked
empty-point-spectrum result for the cube's six-record physical P sector.
For the original all-A-plus/B-vacant initialization with any fixed normalizable
physical field, the ordinary-time joint-spin limit on every fixed finite
electric window is exactly the surviving four-record field density. The
six- and eight-record densities both tend to zero on those windows, uniformly
on compact time intervals. The limiting local total trace is
exp(-48 kappa t), even though the complete density always has trace one.
Consequently at each fixed t>0 the original full density has no trace-norm
convergent subsequence in the specified common physical embedding.

This local escape does not say that either total six- or eight-record
probability vanishes. The first-event probability has the controlled limit
1-exp(-48 kappa t). The split of this probability between six and eight
records is not determined; explicit bounds and subsequential count-curve
compactness are proved below. Both stipulated creation instruments are covered.

The first sector is a real field problem on the cube. Its limiting Hamiltonian
is K sum_e E_e^2 minus twice delta times the sum of the six oriented face
shift pairs. In particular the zero-field state does not remain fixed, and
its finite-spin first clock is not exactly exponential. Direct countercontrols
also show why counting eight legal second-birth paths does not give an
8 kappa operator hazard bound: interference between inputs raises it. A
valid uniform upper bound is 16 kappa.

The six-record spectral premise is supplied by
`cube_point_spectrum_independent/REPORT.md`, SHA
20303cc9320deb32799bdc98befc986c856943ac632d0245ace929c8140a7d7d,
under PRE 8c29f173d14a983a0c6273560712c32685d48429d7482c5dcff152e426d05c0a.
Its candidate comparison was pending at dispatch. This packet does not
independently recheck that certificate and does not confer formal retained,
audit or no-go status on this consequence. Candidate and excluded sources
remain unopened. Exact read identities are in SOURCE_IDENTITIES.json.

## 1. Supplied model, embeddings and observable class

The graph is the eight-vertex cube, vertices 0 through 7 in binary, with
oriented edges in this fixed order:

    01,02,04,13,15,23,26,37,45,46,57,67.

A={0,3,5,6}; every edge is oriented from its smaller to its larger endpoint.
Matter has q=0,+1,-1, is hard-core, has total charge four, and obeys
outgoing-minus-incoming div E=q-1_A. Hopping charge c along an oriented
edge changes its field by -c, with a negative real hopping amplitude.
Birth on an empty oriented edge creates (sigma,-sigma) and changes its
field by sigma, with positive amplitude. Integer spin S has squared shift
weight 1-E(E+k)/[S(S+1)], with zero at a forbidden boundary shift. No extra
exchange sign or register is introduced.

Let C=S(S+1), eta=K C=delta/epsilon^2, with K,delta,kappa>0 fixed. Use the
parent's fixed-graph target H2_S=-A_S^dagger A_S,
H4_S=(A_S^dagger A_S)^2-Z_S^dagger Z_S/2 and effective jumps sqrt(kappa)B_S.
The target lies in P, where all A sites are occupied. Starting at four
records, the only reachable number sectors are N=4,6,8. They have respectively
1,36,28 P matter words. The N=8 sector is absorbing: T,H2,H4 and further
births vanish because every site is occupied. The density stays number-block
diagonal. A coherent edge channel is the stipulated unnormalized positive
sum of its two newborn charge orientations.

For each matter word, solve Gauss using tree
01,02,04,13,15,26,37 and chords 23,45,46,57,67. Every field is uniquely

    E=E0(q)+C_cycle m,       m in Z^5.

The new builder independently verifies the tree minor determinant -1 and
the integer divergence-free cycle matrix, with identity on chord rows.
This gives fixed common rotor spaces H_N and the complete physical spin
embeddings |E_e|<=S. No arbitrary electric cutoff is used in a theorem.

The initial normalized density rho0 lies in the N=4 field space with all
A plus and div E=0. A pure fixed normalizable field is included; finite
electric moments are not assumed. Physical spin initial densities rho0,S
must converge to rho0 in trace norm in the common embedding. Normalized
physical-box truncations of a fixed vector or density are admissible. The
theorem is not uniform over unrelated S-dependent field preparations.

For fixed integer R define Pi_R^(N) by max_e|E_e|<=R inside H_N. It is
finite rank and tends strongly to identity as R increases. A fixed-window
observable is any O=Pi_R O Pi_R, including field/matter coherences. Local
density convergence means trace-norm convergence after that compression.
It is not convergence of the infinite-rank number projection, an unbounded
field moment, or a window growing with S.

The empty point spectrum concerns only H2 on **H6=P H_(N=6,phys)**. It does
not concern the pre-first N4 sector, the absorbing N8 sector, or the zero
extension of the sandwiched operator to P-perp. In particular rotor H2 is
-12 I on H4 and zero on H8; those obvious point eigenvalues are not being
discarded.

## 2. The cube's first-sector field dynamics

Write s_e=+1 if the A endpoint is the edge tail and -1 otherwise. From an
all-A-plus configuration there is exactly one outward hop per edge, of field
shift k_e=-s_e. A two-hop return to P must undo that hop. Hence exactly,
including physical boundaries,

    H2,S|H4 = -12 I + C^-1 sum_e E_e^2.                 (1)

The linear term vanishes because sum_e s_e E_e=sum_(a in A)div E_a=0.
After removing the common -12 eta phase the second-order term is the
compression of the same diagonal Q=K sum_e E_e^2 for every S.

The fourth-order rotor coefficient must be checked on this degree-three
cube; the parent's longer-period degree-six cubic corollary cannot be
silently substituted. Here M=12 I. Two legal outward hops use two disjoint
edges. There are

    choose(12,2)-8 choose(3,2)=42

unordered choices, each with two time orders. Therefore the diagonal of
Z^dagger Z is 4*42=168. Two different matchings with the same intermediate
occupations differ exactly around a four-cycle. The cube has its six square
faces as the complete set of such cycles. Each oriented face cross term has
coefficient four in Z^dagger Z. Thus on the entire rotor field space,

    H4 = 60 I - 2 sum_(six faces p)(U_p+U_p^dagger).     (2)

At zero field the formula is also exact on that vector for every S>=1:
all contributing link steps use fields 0,+/-1 and have unit amplitude.
The twelve shifted face states are distinct normalizable fields.

For a fixed resolved first-birth edge/orientation there are two possible
old-record destinations, the other B neighbors of its A endpoint. Their
output matter patterns are orthogonal. Distinct initial fields remain
orthogonal for each path, and no other P matter word is present in N4.
Each path has squared weight at most one. It follows that its Gram is
diagonal, at most 2 I, and is exactly 2 I in the rotor limit. The coherent
edge Gram is the sum of the two resolved Grams: their newborn patterns are
orthogonal. Summing all channels gives

    0 <= R4,S=sum_j B4,(j,S)^dagger B4,(j,S) <= 48 I,
    R4,rotor=48 I.                                     (3)

In particular R4,S is diagonal in the physical field basis. B4,S and its
adjoint converge strongly to their rotor values. H4,S and R4,S converge
strongly as uniformly bounded operators. This follows on finite field support
from the finite path expressions and shift weights, then on the full Hilbert
space by density. On a fixed graph ||T_S||<=12 supplies a uniform bound for
all retained Hamiltonian polynomials; no field-moment estimate is needed
for this bounded part.

Let

    H_f = K sum_e E_e^2 - 2 delta sum_p(U_p+U_p^dagger),
    r1=48 kappa,     V_f(t)=exp(-it H_f).               (4)

The real diagonal Q is self-adjoint on D(sum E_e^2) with finite-support core;
the magnetic operator is bounded, so H_f has the same domain. Extend each
finite-spin first-sector problem to the whole field space using the common
Q and its bounded H4,S/loss perturbations. The physical spin box is reducing.
Interaction-picture Dyson series, dominated uniformly in S, and strong
convergence of those bounded perturbations give the centered no-event vector
limit exp(-r1 t/2)V_f(t), uniformly on compact times. The scalar 60 delta
has no effect on density. Finite-rank approximation and contraction extend
this to every allowed trace-class initial density:

    rho4,S(t) -> rho4(t)
       =exp(-r1 t) V_f(t)rho0 V_f(t)^dagger             (5)

in trace norm, uniformly on compact time intervals. This argument uses no
uniform electric moment of the initial sequence.

The positive first-event source into H6 is

    A_S(t)=kappa sum_j B4,(j,S) rho4,S(t) B4,(j,S)^dagger.

It converges in trace norm, uniformly on compact times, to

    A(t)=kappa sum_j B4,j rho4(t) B4,j^dagger,
    tr A(t)=r1 exp(-r1 t).                             (6)

Uniformity follows from a finite net of the trace-norm compact trajectory
rho4([0,T]) and the uniform jump bounds. A([0,T]) is consequently a compact
set of positive trace-class operators. This compact source curve, not an
exact finite-S scalar first clock, is the composition input used below.

The limiting first-event CDF is 1-exp(-r1 t). Individual resolved marks have
limiting density 2 kappa exp(-r1 t) and each coherent edge mark has density
4 kappa exp(-r1 t). Their quantum output densities still depend on V_f(t)
and the specified instrument. Those marked statements do not assert a
later unselected state limit.

## 3. A counterexample to an exact finite-spin cube clock

For v0 at zero field, (2) produces twelve face components. On a unit face
field direct evaluation of (3) gives

    R4,S(E_face)=48-32/C+8/C^2.                         (7)

There are two A vertices on that face. At each, the two nonzero incident
fields have s_e E_e equal to +1 and -1; the third incident field is zero.
In the local sum of one old hop and a distinct birth edge this reduces the
loss by 16/C-4/C^2 per such A. The other A vertices retain loss twelve.
This proves (7), including S=1.

If s_S(t) is the first no-event survival from v0 and psi_S(t) its unnormalized
no-event vector, then s'_S+r1 s_S=<psi_S,(r1 I-Gamma4,S)psi_S>.
The face probabilities begin as
4 delta^2 t^2 each. Since Gamma4,S is diagonal, (7) gives

    s_S(t)-exp(-48 kappa t)
       =16 delta^2 kappa(32/C-8/C^2)t^3+O_S(t^4).       (8)

The coefficient is positive for every S>=1. In particular at S=1 and
K=delta=kappa=1 the first three survival derivatives are

    -48, 2304, -109248,

whereas exp(-48t) has third derivative -110592. The difference in the cubic
coefficient is 224. The new path runner verifies this directly by three
applications of the exact finite-spin no-event generator; all nonzero
spin-one link weights are one. No small-time fit is used.

Equation (8) is a finite-S counterexample, not a contradiction of (5).
The coefficient tends to zero in the prescribed joint-spin limit. It also
shows why the ring's exact zero-field scalar clock cannot be copied here.

## 4. Uniform next-birth bound: interference matters

Every pair of vacant B vertices on the cube has two common A neighbors.
For each such A, either vacant B can receive the old record and the other
can receive the new pair. With two newborn orientations this gives eight
resolved paths from each N6 P basis state.

A fixed resolved channel has at most one path from a given input: the other
vacant B is its unique possible old-record destination. However a fixed
final N8 word/field and resolved channel can have **two** predecessors, one
for either other B neighbor of the birth A. Those predecessors may interfere.
Every B matrix entry has absolute value at most one, every input has at most
eight total channel paths, and each such path has at most two predecessors
when forming its Gram. Thus the absolute row and column sums of R6,S obey

    0 <= R6,S=sum_j B6,(j,S)^dagger B6,(j,S) <=16 I.     (9)

This is the Schur bound on the complete physical spin space, uniformly in
S. Boundary suppression only lowers path weights. The identical bound holds
for the common whole-box zero extension. The coherent/resolved Gram sums
again agree by newborn-pattern orthogonality on every fixed edge.

The runner checks all 36 P matter words by full physical local path sums.
Their rotor Gram diagonal is eight and absolute column sum sixteen. There
is an off-diagonal matrix element two between the two compact basis states
saved in CUBE_CONSEQUENCE_CONTROLS.json. Each diagonal is eight, so their
normalized positive superposition has exact rotor expectation ten. Its
finite-S expectation is already about 9.83333 at S=2. Thus the proposed
bound R6,S<=8 I would be false. The valid bound used below is (9).

Every six-record no-event propagator V6,S is a contraction. For a positive
input X, (9) gives the exact survival estimate

    tr[V6,S(t) X V6,S(t)^dagger]
       >=exp(-r2 t) tr X,       r2=16 kappa.            (10)

Each B6 path changes two distinct links by one unit, so every individual
electric component changes by at most one. For a fixed electric window,
B6,S^dagger Pi_R^(8) B6,S is supported inside Pi_(R+1)^(6). Its norm and the
summed Gram norm are bounded uniformly in S. Large-field probability cannot
make a single birth directly into a fixed window from outside that enlarged
window.

## 5. Empty point spectrum gives time-averaged local escape

Here the provisional spectral premise enters: H2 on H6 is bounded,
self-adjoint and has no normalizable point eigenvectors. No absolute
continuity theorem, gap, rate, or pointwise dispersive decay is assumed.

Let Phi_S(t)X=V6,S(t)X V6,S(t)^dagger. For every fixed positive trace-class
X and every fixed electric window,

    integral_0^T tr[Pi_R^(6) Phi_S(u)X] du ->0.         (11)

More generally finite-window densities tend to zero after any L^1 time
smearing. Trace-convergent physical inputs can replace X by contraction.

To prove this, extract weak-star L-infinity subsequences of the countably
many physical matrix entries of the positive, trace-bounded densities.
Positivity and bounds on every finite diagonal sum pass to the limit and
give a positive trace-class sigma(t) with tr sigma(t)<=tr X almost everywhere.
Testing the no-event equation against a finite-rank finite-field matrix K
and a smooth time test, then dividing by eta, gives

    integral a(t) tr([H2,S,K] Phi_S(t)X) dt ->0.        (12)

The integrated derivative, H4,S and loss terms are O(eta^-1). The uniform
fixed-graph bounds hold on the entire spin space. H2,S and its adjoint converge
strongly and are uniformly bounded; therefore [H2,S,K] converges in norm to
[H2,K]. The limiting sigma(t) commutes with H2 almost everywhere.

A positive trace-class operator is compact. Its nonzero eigenspaces are
finite-dimensional and, if it commutes with H2, are invariant under H2.
Diagonalizing the self-adjoint H2 on each such space gives point eigenvectors
of H2. The empty-point-spectrum premise therefore forces sigma(t)=0.
Uniqueness of every local subsequential limit proves (11); smooth tests extend
to L^1 by the common trace bound. Finite-dimensional compression turns matrix
entry convergence into trace-norm convergence of the smeared density.

This proof treats the exact finite-spin propagators. It does not replace
eta H2,S by eta H2 in operator norm or neglect electric corrections at large
fields. It does not give pointwise-in-time local decay after an arbitrary
externally fixed first-output restart. An instantaneous return spike is not
excluded by a time-averaged statement alone.

## 6. The actual first source upgrades the conclusion to fixed times

For the specified original initialization the exact triangular target identity
is

    rho6,S(t)=integral_0^t Phi_S(u) A_S(t-u) du.         (13)

Both the age u and the time-dependent field source must be kept. Replacing
A_S(t) by a fixed output times an exact exponential would be unjustified
at finite S on this cube.

There is a direct positive-source proof of the required uniform limit.
For any e>0, choose finitely many positive trace-class anchors A_1,...,A_m
within distance e of every point of the compact curve A([0,T]). Equation
(6) implies that, for all large S, every A_S(s) lies within 2e of an anchor.
For each t, assign anchors to the source values A_S(t-u). Contractivity and
positivity give, uniformly for 0<=t<=T,

    tr[Pi_R rho6,S(t)]
      <=2e T + sum_(j=1)^m integral_0^T
                                 tr[Pi_R Phi_S(u) A_j] du. (14)

The subsets of ages assigned to each anchor may depend on t and S; positivity
allows replacing each subset by the whole [0,T] in this upper bound. For the
fixed finite list of anchors, (11) makes the sum vanish. Letting e tend to
zero proves

    sup_(t<=T) ||Pi_R^(6) rho6,S(t) Pi_R^(6)||_1 ->0.  (15)

This argument needs no differentiability or field-moment bound for A(t).
Its trace-norm compactness is load-bearing. A merely bounded S-dependent
positive source would not suffice: in a unitary model an adversarial source
X_S(s)=U_S(t_*-s)^dagger X U_S(t_*-s), for fixed compact X>=0, yields
rho_S(t_*)=t_* X by (13). Such a rapidly varying source can refocus at t_*.
It is not the source of this cube initialization and fails the compact-source
convergence used in (6) and (14).

Because N8 is absorbing,

    rho8,S(t)=kappa sum_j integral_0^t
                       B6,(j,S)rho6,S(s)B6,(j,S)^dagger ds.

Equations (9), (15) and the fixed enlarged-window support imply

    sup_(t<=T) tr[Pi_R^(8)rho8,S(t)]
       <=16 kappa T sup_(s<=T)tr[Pi_(R+1)^(6)rho6,S(s)] ->0. (16)

Thus every finite-window six- and eight-record observable vanishes in the
ordinary-time joint limit of the **original** evolution. This is a composition
of the exact target sector equations with controlled first-field evolution;
it is not a normalized microscopic random-first-mark restart theorem.

## 7. Full local density, topology and deterministic microscopic transfer

Combining (5), (15) and (16), the full original target density converges,
uniformly on compact times on each fixed electric window, to

    rho_loc(t)=exp(-48 kappa t) V_f(t)rho0 V_f(t)^dagger

supported entirely in N4. Its trace is exp(-48 kappa t). Finite-window
operators determine all matrix entries; compact observables follow by norm
approximation. At any fixed t>0 a trace-norm convergent subsequence of the
normalized full densities would have to equal rho_loc(t). Trace continuity
would then give trace one, which contradicts its computed trace. This proves
the stated trace-norm subsequence obstruction in the fixed common embedding.

The limiting orders do not commute. With Pi_R the sum of the three number
windows, for every fixed t>0,

    lim_(R->infinity) lim_(S->infinity) tr[Pi_R rho_S(t)]
        =exp(-48 kappa t),
    lim_(S->infinity) lim_(R->infinity) tr[Pi_R rho_S(t)]=1. (17)

All mass that has left N4 escapes every fixed field window in this sense.
No location, scaling rate, semiclassical law or eventual fate of that escaped
mass is specified. In particular, vanishing local N8 density does not imply
vanishing total N8 probability. A simple logical counterexample is a sequence
of normalized absorbing N8 basis states with fields E0(q)+n C_cycle e_1,
embedded at S_n>=max|E|. Every fixed-window expectation eventually vanishes,
while P8 is exactly one. These states are not asserted to be the outputs of
the original initialization; they expose the invalid topology inference.

The parent's deterministic microscopic-to-target trace-density error is
O(epsilon), uniformly in S on this fixed graph and compact time intervals.
Here epsilon^2=delta/[K S(S+1)] tends to zero. Applied to the original bare
P-supported initial sequence, it transfers the full local limit, the first
count limits and the trace-norm subsequence obstruction to the microscopic
density. Extra W>0 microscopic components have trace-norm contribution
tending to zero. The initial state is number-block diagonal, so it also
satisfies the parent's qualification when using its N_B Hamiltonian form.
No conditioned trajectory estimate or new microscopic approximation is used.

## 8. What is and is not known about global counts

Let p_(N,S)=tr rho_(N,S), and define

    a(t)=exp(-48 kappa t),
    g(t)=(3/2)[exp(-16 kappa t)-exp(-48 kappa t)],
    h(t)=1-a(t)-g(t)
        =1-(3/2)exp(-16 kappa t)+(1/2)exp(-48 kappa t). (18)

The controlled statements, uniform on compact times where limits appear, are

    p4,S -> a,
    p6,S+p8,S ->1-a,
    sup_(t<=T)[g(t)-p6,S(t)]_+ ->0,
    0<=p6,S(t)<=1-a(t)        for every S,
    0<=p8,S(t)<=h(t)          for every S.              (19)

The finite-S p6 upper bound follows from p4,S>=a, which is exact by (3).
For the asymptotic p6 lower bound, apply (10) inside (13):

    p6,S(t)>=integral_0^t exp[-r2(t-s)]tr A_S(s) ds.

The uniformly converging first source trace gives g in the limit.

The p8 upper bound is also exact at finite S, despite the nonexponential
first clock. If F1,S=1-p4,S is the first-event CDF, (3) gives
F1,S(s)<=1-exp(-r1 s). The conditional second-event probability after any
physical first output is at most 1-exp[-r2(t-s)] by (10). Integration by
parts therefore bounds the exact target P8 by

    r2 integral_0^t exp[-r2(t-s)] F1,S(s) ds
      <=r2 integral_0^t exp[-r2(t-s)](1-exp(-r1 s)) ds
       =h(t).                                         (20)

The positive integral representation proves h>=0. The independent algebra
runner verifies (18)--(20). It does not replace the actual second clock by
an exponential of rate 16 kappa.

There are compact-time convergent subsequences of the number curves: their
derivatives have bounds |p4,S'|<=48 kappa, |p6,S'|<=64 kappa and
0<=p8,S'<=16 kappa. Every subsequential limit has p4=a,
p6+p8=1-a and, almost everywhere, 0<=p8'<=16 kappa p6. Neither uniqueness
of p6,p8 nor a nonzero asymptotic lower bound on p8 is proved here. The stated
constraints are necessary; they do not assert that every curve satisfying
them occurs in this model. First moments, second-event waiting laws and
large-time tails are not extracted from the vanishing local densities.

By the parent estimate, the limiting count statements and the upper/lower
bounds up to O(epsilon) also hold for the microscopic evolution. Exact
finite-S target inequalities are not labelled exact microscopic identities.

## 9. Evidence, failures and provisional scope

The new `cube_controls.py` imports no previous or author builder. It uses
the full twelve-component physical fields and local hopping/birth rules.
It verifies all six face shifts, the 42 grade-two outputs and Z norm squared 168,
the H2 electric identity on 243 physical chord-field samples, first-channel
norms and loss at S=1,2,4,8, the finite-clock Taylor counterexample, and all
36 six-record matter-word Gram path counts. Its compact interference and
terminal escape counterexamples are preserved with explicit states.

The operator inequalities and strong-limit arguments are proved above for
all physical fields; finite numerical samples do not establish them by
extrapolation. No complete five-dimensional finite-spin time propagation or
empirical convergence rate was computed. No such computation is needed for
the source-compactness/commutant proof. The exact spectrum certificate is
an explicit provisional dependency and was not rerun in this packet.

`count_bound_check.py` supplies a separate symbolic convolution check.
`source_check.py` verifies all five allowed source identities and the thirty
artifacts in the reused own packet. All three commands exited zero; complete
stdout/stderr, source and stream hashes, timings and execution receipts are
retained. No failed execution was removed. The scientifically invalid routes
are retained as counterexamples: an exact finite-spin first clock, an eight
unit next-hazard bound, a pointwise conclusion from time averaging alone,
and equating local terminal disappearance with a global count limit.

The exact negative topology result is provisional scientific content under
the stated spectral dependency. Its scoped N1--N8 stress test is recorded
separately, without a formal packet PASS, forbidden historical scan, Git
operation, audit or publication. The result does not imply inconsistency of
the supplied microscopic model, the absence of weaker/rescaled descriptions,
or a macroscopic field/TOE conclusion. PRE source comparison remains pending.

The coordinator received concise mathematical progress findings before this
PRE. No candidate freeze identity or candidate formula was supplied to this
checker, and no candidate source was read. This packet therefore claims an
independent pre-access reconstruction; it does not claim that the primary
author was blind to the progress findings received during this work.
