# Independent PRE: a conditional electric completion

Prepared 2026-09-24 by the assigned independent checker. This is a source-bound
reconstruction before author comparison, not a formal audit or premise adoption.
The candidate was supplied in the dispatch. No electric-completion author files,
checkpoint, high-flux author/checker files, external calculations, or existing
model/builders were inspected. The six mathematical input notes are identified
by full SHA256 in SOURCE_MANIFEST.json and EXACT_RESULTS.json. No network or git
mutation was used. Only this assigned output directory was written.

## Result and scope

For every fixed finite simple bipartite graph with the supplied hard-core
charge/normalized integer-spin algebra and physical Gauss sector, the proposed
family satisfies the bounded compensation theorem. Its common rotor density
dynamics exists and has

    h_lambda = K D_lambda + delta Q,
    D_lambda = (1-lambda) D + lambda E2,
    Q = -2 sum_{unordered a,c: distance(a,c)=2} S_ac^* S_ac,
    S_ac = F_c F_a P,
    L_lambda rho = -i[h_lambda,rho] + kappa sum_j D[B_j]rho,
    B_(a,b,sigma) = P j_(a,b,sigma) F_a P.                 (1)

Here 0 <= lambda <= 1 is fixed, delta,K,kappa > 0, and
delta/epsilon(S)^2 = K S(S+1). D is the local-compensation electric diagonal
on the entire P space, not just its initial number sector. The jumps, charge
conventions and instrument choice are those of the supplied sources.

All lambda have the same limiting original pre-first field dynamics up to a
scalar and the same specified first-formation instruments. They have different
later dynamics: on an existing all-occupied sector, h_lambda = K lambda E2,
all effective jumps vanish, and field coherences can evolve. On the specified
cube two-mark history, an accessible terminal interference has limiting value
cos(2 K lambda n u). Thus n != 0 distinguishes lambda=0 from suitable lambda>0
even though the common pre-first field/instrument data agree. These conclusions
are conditional on the changed Hamiltonian. No autonomous reservoir, native
selection of lambda, empirical identification or growing-volume limit follows.

## 1. Source and premise contract

The pinned candidate worktree HEAD is
723dacc0eee0ed9897f5c9445be72cdfbc71389d. The supplied main snapshot is
61fa847f032d25c90bca2c1273b7edb5713fe160 and instruction snapshot is planning
eb1f1ca8338848cf2046582e13aef372d8540937. During this check the local origin/main
ref was 5efa36e7c357ae2a62ee586a5407f90982f6ded9. A read-only git diff of
AGENTS.md, SCIENCE_WORKFLOW.md, SKILL_FRESHNESS_CHECK.md, the
physics-claim-reviewer skill, and its proof-search-governance reference between
the supplied main snapshot and that local ref was empty. Remote freshness was
not checked because the dispatch forbids network actions. The installed reviewer
skill and the pinned-main reviewer skill had identical bytes. Planning AGENTS.md
was read directly from the supplied commit. The workflow's selective-check
cadence applies; no audit, landing review, or unrelated frontier search started.

Accepted supplied hypotheses are: tensor-product hard-core sites q=0,+1,-1;
integer-spin links E=-S,...,S and U=S_+/sqrt(S(S+1)); a fixed finite simple
bipartite graph and edge orientation; div E=q-1_A; the hopping T, penalty W,
resolved or coherent birth instruments j, positive couplings, deterministic
P initialization, and the new compensation law. None is derived here from
more minimal physics. The canonical fourth-order formula is reconstructed
below from the supplied general target and its accompanying wording correction.
The frozen phrase “all displayed operators are self-adjoint” must be read only
as self-adjointness of H2 and H4; B_j need not be self-adjoint.

Use s_ab=+1 when the oriented edge runs from A site a to B site b, and -1
otherwise. A hop of q_a from a to b shifts E_e by -s_ab q_a. A resolved birth
with charge sigma at a shifts E_e by s_ab sigma. Both preserve the Gauss law.
Let n=q^2, C=S(S+1), W=sum_A(1-n_a), P=1_(W=0), and

    D_ext = sum_{a~b} n_a(1-n_b) E_e(E_e-s_ab q_a),
    R_S = (E2-D_ext)/C,
    C_S^lambda = C_S + lambda R_S.                         (2)

The source compensation is

    C_S = sum_a [F_a^*F_a - D_(a,S) + D_(a,infinity)] Q_a,
    Q_a = product_{c != a, distance(c,a)=2} n_c.

F_a is the unsigned legal outward-hop sum. The notation C_S denotes an
operator and C denotes the scalar S(S+1). All statements below retain this
distinction.

## 2. Why the general target applies

R_S is real diagonal and preserves all occupations, N, W and Gauss. On a spin
link, 0 <= E^2 <= S^2 and 0 <= E(E +/- 1) <= C. The latter uses integer E;
the nonnegative product would not hold for arbitrary real E between 0 and 1.
Consequently ||E2/C|| <= m and ||D_ext/C|| <= m, with m=|E|, so
||R_S|| <= 2m. This loose bound is uniform in S and sufficient. C_S^lambda is
bounded, self-adjoint and W preserving with a fixed-graph uniform bound. It is
not necessary to assert that this entire operator is positive. The added term
is a sum of single-edge diagonal interactions and changes no T, W or j.

On P, n_a=1 and D_ext=D. The source identity P C_S P=M_S+D/C, where
A_S=Pi_1 T_S P and M_S=A_S^*A_S, follows directly because different vacant-A
outward-hop ranges are orthogonal. Therefore the second coefficient is exactly

    H2_S^lambda = P C_S^lambda P - M_S
                 = [(1-lambda)D + lambda E2]/C,
    delta epsilon^-2 H2_S^lambda = K D_lambda.            (3)

This holds on the complete physical spin P space, including sectors reached
after formation. There is no post-event projection onto a special field state.

For completeness, the canonical fourth coefficient with any supplied C_S^lambda
is obtained from the low spectral graph X:P->P^perp of
W+epsilon T+epsilon^2 C_S^lambda. Put C0=P C_S^lambda P and
C1=Pi_1 C_S^lambda Pi_1. Its invariance equation gives

    X1=-A, X2=Z/2,
    A^*X3=M^2-M C0+A^*C1 A-Z^*Z/2,
    Z=Pi_2 T Pi_1 A.

Conjugation from graph coordinates by (I+X^*X)^(1/2) contributes
[M,C0]/2 at order epsilon^4. Hence

    H4_S^lambda=M^2-{M,C0}/2+A^*C1 A-Z^*Z/2.             (4)

This is Hermitian; the unnormalized graph-coordinate coefficient generally is
not. The added diagonal's exact finite-spin correction to the old H4_S is
lambda[-{M,R0}/2+A^*R1 A], with Rr=Pi_r R_S Pi_r. It need not vanish at a
fixed spin. Embed R_S by zero outside its physical spin box. On every finite
electric-support vector R_S tends to zero; uniform boundedness then gives strong
convergence to zero on the full rotor space.
The same holds for adjoints. The normalized spin shifts converge strongly to
the unit rotor shifts, so all fixed bounded products in (4) converge strongly.
Thus all lambda have the same limiting H4, and the effective B_j are unchanged.

The source uniform-density estimate is applicable without a new unbounded
microscopic theorem: for each S all operators in its bracket are uniformly
bounded. Its spectral clusters remain separated for small epsilon, and the
positive-overlap block rotation is I+O(epsilon), uniformly in S. W parity makes
the rotated Hamiltonian blocks even in epsilon. The P block remainder after
(3)-(4) is O(epsilon^2) in the physical Hamiltonian. The transformed jump
satisfies j_tilde P=epsilon B_j+O(epsilon^2).

The off-block dissipative loss residual is O(epsilon^-1), not zero. Inverting
-i delta[W,.] on (I-P)P and P(I-P) matrix blocks and multiplying this residual by -epsilon^4 makes
an O(epsilon^3) embedding correction. Its remaining residual is O(epsilon):
the corrected diagonal discrepancy is O(epsilon), while the remaining full
generator and the target have norms O(epsilon^-2). Duhamel and CPTP contraction
give the stated O(epsilon) trace-norm density error on a fixed finite interval,
uniformly over spin and P densities. This argument also applies to a finite
record of the two designated marks or fixed time windows. It is not a theorem
of total-variation convergence of arbitrary continuously conditioned histories.

## 3. Deriving the local fourth-order term

At rotor order C_infinity=sum_a F_a^*F_a Q_a and C0=M. On a one-vacancy state
with empty A site a, the c term survives precisely when c is distinct from a
and their stars share no B site. Different vacancy locations are orthogonal.
Thus A^*C1 A is the sum over ordered disjoint-star pairs of
P F_a^*F_c^*F_c F_a P. Two outward hops commute: if they target the same B
site both orders vanish, and otherwise their site operations commute and any
shared A-site issue is absent because the centers are distinct. The two orders
give Z=2 sum_{a<c} S_ac into mutually orthogonal two-vacancy ranges. Hence
Z^*Z/2=2 sum_{a<c} S_ac^*S_ac. The distant-pair contributions cancel exactly,
leaving Q in (1). This is a proof for every P charge word and electric field.

Each term is supported on two overlapping A stars and is bounded in norm by
2 z_a^2 z_c^2. The number of partner stars at a is at most z(z-1) on degree-z
graphs. Jumps have A-star support with norm <=z_a-1 for each resolved channel;
coherent channels are their specified bounded sums. The electric D_lambda is
a sum of commuting edge-local multiplication operators. These facts give
finite-range interaction structure and per-term bounded estimates; the total
bounded interaction norm and the microscopic error constants depend on volume.

The standalone exact control implements hopping and birth directly from integer
charge words and incidence, without importing any supplied builder. It evaluates
the entire canonical polynomial (4) at rotor order before comparing it with
the local pair expression. Its mixed graph has A={0,2,4} and edges
01,03,12,23,25,45,46. It contains both a four-cycle and disjoint A stars, so
the C1 cancellation is actually exercised. All 52 admissible total-charge-three
P matter words were tested at three independent cycle fluxes (-2,0,3), giving
156 exact rational cases. The diagonal D bounds were also tested. Dropping
Z^*Z/2 changed 93 cases; omitting the occupancy gate changed 93 cases and
made the full rotor fourth coefficient zero. Distant-pair cancellation was
nontrivial in 63 cases. These finite checks corroborate, but do not replace,
the preceding all-state operator proof.

## 4. Domain and common density limit

On the rotor physical P space, D is nonnegative because each included term is
E(E +/- 1) on integers. D_lambda is a real nonnegative diagonal multiplication
operator. Its maximal multiplication domain is

    {psi: sum_(q,E) D_lambda(q,E)^2 |psi(q,E)|^2 < infinity}.

Finite-support physical vectors are a core, as follows by coordinate truncation
of both psi and D_lambda psi. h_lambda is self-adjoint on that domain by the
bounded perturbation delta Q. The unitary trace-class group generated by it
plus the finite collection of bounded dissipators yields a strongly continuous
trace-preserving completely positive semigroup. An arbitrary trace-class initial
density can be evolved; an energy expectation or a derivative of the density
requires the relevant separate domain assumptions.

To compare spin targets, embed their physical electric boxes in the common
rotor space. Extend H4_S^lambda and B_(j,S) by zero off the box, and take the
same K D_lambda on the whole rotor space. The box reduces this extended target,
and restriction gives exactly (3)-(4) and its jumps. Strong convergence, with
uniform boundedness, of all bounded factors gives trace-norm convergence of
their left/right multiplication and recycling maps on every trace-class input.
This follows first for rank-one operators and then by finite-rank approximation.

In the common interaction picture of K D_lambda, the remaining time-dependent
generators are uniformly bounded on trace class. Their Dyson series have a
common exponential majorant on [0,T]. Strong convergence on fixed inputs,
continuity of the free orbit, and finite-net approximation of compact orbits
give convergence of the integral terms uniformly on [0,T]. The dominated
Dyson series therefore gives

    sup_(0<=t<=T) ||rho_target,S(t)-exp(t L_lambda)rho_0||_1 -> 0.    (5)

Trace-norm convergent physical initial approximants are allowed by contraction.
The O(epsilon(S)) microscopic estimate from section 2 transfers (5) to the
bare microscopic densities of the changed law. The common density is supported
on P, but the comparison includes the microscopic population outside P and
does not discard any reachable formation branch. Finite event/count registers
inherit the statement. S tends to infinity with fixed graph, lambda, couplings
and time horizon. This is a strong trace-class limit, not operator-norm uniform
convergence over high-field states, a joint growing-volume theorem, or a result
uniform over S-dependent times or lambda(S).

The bounded-compensation microscopic theorem is used on the finite-spin
family. Replacing its links by uncut unit rotors at a fixed finite C while
retaining (E2-D_ext)/C would give an unbounded compensation and would require
a different microscopic theorem. That replacement is not part of this proof.

At lambda>0 there are useful stronger domain and spectral statements. Since
|E|<=E^2 for integer E,

    0 <= D <= 2 E2,
    lambda E2 <= D_lambda <= (2-lambda) E2.               (6)

Thus D(D_lambda)=D(E2) for each fixed lambda>0. At fixed finite graph and fixed
finite matter alphabet, every E2 sublevel has finitely many physical basis
vectors. D_lambda has compact resolvent, and bounded perturbation preserves
that property. h_lambda is bounded below and has discrete eigenvalues of finite
multiplicity, with no finite accumulation in an infinite-dimensional sector.
For finite-dimensional physical sectors the statement is immediate. These are
Hamiltonian spectral conclusions; they establish no dissipative spectral gap,
mixing rate, dispersion relation, infinite-volume gap, or unique stationary
density. At lambda=0 compactness is not assured: the terminal cyclic cube sector
has h_0=0 on an infinite-dimensional field space.

## 5. Initial sector and what it can select

On all-A-plus, B-empty fields, D=E2-sum_a div E_a=E2, since Gauss gives
div E=0. Consequently every lambda has exactly the same second-order electric
diagonal there. At rotor fourth order, put r_ac=|N(a) intersect N(c)|. Two-hop
path counting gives diagonal z_a z_c-r_ac for each overlapping A pair; distinct
assignments of two common B neighbors give one oriented four-cycle and its
reverse. Thus

    Q_initial=c_comp I-2 sum_(simple unoriented four-cycles p)(W_p+W_p^*),
    c_comp=-2 sum_(a<c,r_ac>0)(z_a z_c-r_ac).              (7)

The original uncompensated H4 has the same loop term and scalar
c_original=sum_a z_a^2+sum_b z_b(z_b-1). This follows from M=m I and the
same two-hop count over all A pairs. On the cube c_comp=-84 and c_original=60.
The large original second-order scalar -m delta epsilon^-2 is also irrelevant
within this pre-first sector. Therefore the limiting common pre-first field
Hamiltonian, for all the stated graphs and all divergence-free initial field
densities, agrees with the original one up to a scalar:

    K E2 - 2 delta sum_p(W_p+W_p^*).                      (8)

The total first loss is 2 kappa sum_a z_a(z_a-1) times the identity; the resolved
or coherent B_j instruments are unchanged. Thus the corresponding first-event
waiting law, marks, and output instruments agree. This does not assert equality
of finite-S microscopic laws or fourth-order spin corrections, and it does not
extend the original Hamiltonian to later sectors by fiat. Sector-dependent
scalars would require care for coherences between different number sectors;
the present agreement is within the single initial sector and its first-event
instrument.

Since the family matches these common pre-first data but has the observable
difference below, those data do not select lambda. This is explicit
underdetermination within the supplied family, not an impossibility theorem for
other physical selection principles. A post-formation experiment, an additional
dynamical premise, or more microscopic finite-resource information could impose
further conditions. lambda=1 is a supplied occupancy-independent E2 extension,
not a value derived by the pre-first calculation.

## 6. Actual two-mark cube output

List the smaller-to-larger cube edges as

    (01,02,04,13,15,23,26,37,45,46,57,67).

The input phi_n has q=1_A and fields

    E=(n,-n,0,n,0,-n,0,0,0,0,0,0), n in Z.

For resolved mark (01,+ at 0), the old charge must hop from 0 to 2 or 4;
the birth then puts + at 0 and - at 1. For mark (67,+ at 6), the old charge
must hop to whichever of 2 or 4 is still vacant, and the birth puts + at 6
and - at 7. Both alternatives have the same final charge word

    q_final=(1,-1,1,1,1,1,1,-1).

There are exactly two rotor outputs, each with amplitude +1:

    alpha_n: first hop 0->2, second hop 6->4,
    E_alpha=(n+1,-n-1,0,n,0,-n,0,0,0,1,0,1),

    beta_n: first hop 0->4, second hop 6->2,
    E_beta=(n+1,-n,-1,n,0,-n,1,0,0,0,0,1).

The signs are fixed by B=-PjTP=PjF, and no record label distinguishing the two
old-hop routes is supplied. Consequently the resolved birth marks alone leave
their coherent sum intact. Both outputs obey Gauss. They are distinct and
orthogonal electric basis vectors, even at n=0. Their difference is the
circulation (-1,+1,-1,+1) on (02,04,26,46). Direct summation gives

    E2(alpha_n)=4n^2+4n+4,
    E2(beta_n) =4n^2+2n+4,
    B_(67,+) B_(01,+) phi_n=alpha_n+beta_n,
    ||B_(67,+) B_(01,+) phi_n||^2=2.                    (9)

On either all-occupied output no hop is legal, so A=Z=0, every effective B=0,
D=0 and Q=0. Hence the common terminal Hamiltonian is K lambda E2. In fact
the restriction of the modified finite-spin microscopic Hamiltonian to an
all-occupied sector is also exactly K lambda E2 under the stated scaling:
W,T,j,C_S,D_ext all vanish there. At lambda=0 the full terminal density freezes;
at lambda>0 occupations and electric populations are constant while field
coherences can acquire relative phases. All-occupied sectors need not exist
on every graph or be reached from every state; the cube construction proves
the needed particular accessibility. Componentwise total charge and hard-core
parity must be compatible on other graphs.

If all fields in (9) lie inside the spin box, put

    r=1-n(n+1)/[S(S+1)].

The four primitive spin factors give amplitudes r for alpha and sqrt(r) for
beta: the alpha route has both the initial 02 downward shift and 01 upward
shift with squared weight r, whereas the beta route has only the latter.
Both second marks have unit weight on their two initially zero links. Thus
the exact finite-spin ideal composition norm squared is r^2+r and its branch
norms squared are r^2 and r. This is zero when the relevant outward boundary
blocks the common birth, and tends to 2 for fixed n as S tends to infinity.
The direct control verified these weights for n=-3,-1,0,1,2,4 at admissible
spins; this also checks the orientation sign with negative n.

## 7. Interference and positive-probability histories

Let V be the physical unit-rotor loop shift with increments -1,+1,-1,+1 on
(02,04,26,46). It maps beta_n to alpha_n and preserves the final Gauss sector.
For the normalized ideal terminal vector psi_n=(alpha_n+beta_n)/sqrt(2),

    <V+V^*>_(exp(-i K lambda E2 u) psi_n)
       = cos(2 K lambda n u).                           (10)

V+V^* is a bounded local field observable, so this is not a formal comparison
of unbounded energy expectations. Its operator norm is at most 2. The n=0
input has equal terminal energies and cannot distinguish lambda using (10).
For n=1, for example, the energy pair is (12,10); lambda=0 stays at 1 and
lambda>0 oscillates with angular frequency 2K lambda. The exact spin-normalized
two-branch state has coherence visibility 2 sqrt(r)/(1+r) for the rank-two
flip, and the product of normalized spin link shifts corresponding to V has
visibility 2r/(1+r). Both approach the rotor result. Equation (10) itself is
a common rotor statement.

An ideal B2 B1 composition is not the exact conditional state of a finite-time
trajectory. With rho_n=|phi_n><phi_n|, define J_j(rho)=B_j rho B_j^*, and let
S_m(t) be the no-event completely positive evolution in the N=m sector. The
unnormalized final density for the specified ordered marks, both in (0,t), is

    R(t)=kappa^2 integral_(0<t1<t2<t)
         S_8(t-t2) J_2 S_6(t2-t1) J_1 S_4(t1)(rho_n) dt1 dt2.      (11)

There can be no third formation after the second because all eight sites are
occupied. The no-event evolutions include the full sector Hamiltonians and
losses; they cannot be replaced by the identity for an exact finite t. For
finite time-window conditioning, (11) is generally a mixture of different
conditional vectors. Even a trajectory conditioned on exact jump times has
nontrivial propagation between the jumps. Thus no claim of exact equality
with psi_n at positive t is justified by the composition alone.

However, all S_m are strongly continuous on trace class, and J_1,J_2 are
bounded. Their integrand tends uniformly over the shrinking time simplex to
J_2 J_1(rho_n). The simplex has area t^2/2, so

    R(t)=(kappa^2 t^2/2)|alpha_n+beta_n><alpha_n+beta_n|+o(t^2),
    Pr(specified ordered marks in (0,t))=kappa^2 t^2+o(t^2),
    R(t)/tr R(t) -> |psi_n><psi_n| in trace norm.         (12)

The probability is strictly positive for every sufficiently small positive t.
After conditioning on that finite window and waiting a further fixed time u,
the terminal sector evolves exactly under K lambda E2. Unitary evolution
preserves the trace-norm error, and the expectation error in (10) is bounded
by twice that error. Hence the distinguishable interference is accessible
to arbitrary accuracy by positive-probability small-time marked histories.
For example n=1 and u=pi/(2K) give limiting expectations +1 at lambda=0
and -1 at lambda=1. Their difference persists for sufficiently small but
strictly positive conditioning windows; exact zero-time jumps are unnecessary.
For a fixed spin with r>0 the corresponding leading target probability is
kappa^2(r^2+r)t^2/2. No derivative of an unbounded Hamiltonian is used.

The common density/register limit transfers probabilities and bounded terminal
observables for each fixed positive window t from the microscopic law. Since
the limiting window probability is positive, the corresponding normalized
conditional outputs converge as well. This is a sequential argument: first
S->infinity at fixed window, then the window may shrink. The O(epsilon) absolute
bound does not itself control a joint limit with t(S)^2 comparable to or smaller
than epsilon. Exact jump-time conditioning is a null-event/disintegration
question and is not established by the finite-register theorem.

## 8. Remaining boundaries and PRE disposition

The added diagonal is local, bounded at finite spin in the compensation bracket,
and supplies a coercive rotor electric term for lambda>0. It therefore repairs
the specific terminal field freeze within a family that leaves the common
pre-first sector unchanged. It also changes intermediate post-formation field
dynamics. This is a conditional construction, not a selection argument.

The finite-volume common dynamics and finite-volume compact-resolvent statement
are established under the supplied hypotheses. No volume-uniform microscopic
bound, infinite-volume gauge-state construction, norm-continuous dynamics on all
rotor observables, unique equilibrium, autonomous formation fuel, permanent
record content beyond q, or empirical coupling selection was supplied or proved.
The existing external birth channel remains a supplied open-system instrument.
Locality of the terms alone does not discharge these independent obligations.

The finite exact controls passed on their first execution with no assertion
failure. Their full stdout, empty stderr, JSON data and standalone runner are
saved with an execution receipt. They test 156 finite operator cases and six
cube inputs; they are not exhaustive enumeration of the infinite rotor space.
The analytic argument supplies that scope. PRE_SEAL.json binds this report and
the complete evidence before any root/author comparison. Stop here: no source
comparison or publication authorization is represented by this PRE packet.
