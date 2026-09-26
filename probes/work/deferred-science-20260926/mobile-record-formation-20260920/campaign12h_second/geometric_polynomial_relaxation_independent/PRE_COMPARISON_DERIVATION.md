# Independent reconstruction before author-checker access

2026-09-21. This reconstructs the supplied candidate at SHA-256
`f9d12f1fccc3ea54d3b640deaccdcbb04749db1d6ac5b7b2708193a4a0dd89bb`.
The complete candidate note was read; the author runner was only hashed and
its body and results were not opened. The existing independently checked
general-graph slide construction is an explicit dependency. This is a
scientific proof check, with imported theorems identified below, not an audit.

## 1. Trace identity and its rate convention

Let G be finite, connected and simple, with 2K vertices and a perfect matching,
K>=2. Write Omega for matchings of size K-1 and P for perfect matchings;
n=|Omega|, Z=|P|, R=n/Z. Geometric slides have rate kappa per legal replacement.
The earlier constructive proof gives irreducibility on Omega even when G is
irregular, bridged or nonbipartite. It does not give marked-state irreducibility.

For incidence A(M,F)=1_{M subset F}, each row has sum h(M) in {0,1}, while
each column has sum K. In units kappa=1, the positive auxiliary Broder
Laplacian, ordered near/full, is

    [ L_slide+H    -A ]
    [   -A^T      K I].

Eliminating full states gives L_trace=L_slide+H-AA^T/K. A visit to F followed
by a deletion chooses each of its K edges uniformly. Thus its extra rate
from F-e to F-f is kappa/K for e!=f; a return to F-e is not a trace jump.
Keeping that self-return as killing would leave row sum kappa*h/K and is
incorrect. The independent matrix check deliberately constructs this wrong
alternative and detects its nonzero row sums.

For f on Omega, the harmonic extension is fbar(F)=K^-1 sum_{e in F}f(F-e).
With mu uniform on Omega union P, its energy is [n/(n+Z)] E_trace(f).
Conditional variance gives Var_mu(fbar)>= [n/(n+Z)] Var_pi(f). Applying the
Broder Poincare inequality and cancelling this same factor gives
gap(trace)>=gap(Broder). No extra n/(n+Z) or its inverse belongs in the bound.

## 2. Replacement paths and congestion

Fix F and contract its K edges. Connectivity of G makes the quotient
connected. Choose a simple quotient path for each ordered pair (e,f), with
one physical bridge per quotient edge. If e={a,a'} is missing and
f={b,b'} is occupied, bridge {a,b} gives the legal marked slides
(vacancy a, b, b') and then (vacancy a', a, b). Their projected sequence is

    F-e -> F-{e,f}+{a,b} -> F-f.

Both records move across physical graph edges with their immutable labels.
This is an actual slide route, not deletion of an old record and a fresh birth.
Concatenation along the quotient path uses at most D=2(K-1) slides. Parent
states are distinct; each intermediate state determines the two removed
F-edges and the inserted non-F bridge. Thus no micro-edge is repeated.

Every micro-edge on such a route has a parent endpoint F-e. Completing that
endpoint's two holes determines F uniquely because the graph is simple.
Either endpoint can be such a parent, so a micro-edge has at most two
reference F's. This is a real factor: on C4 the slide {01}->{03} is used by
routes associated with both {01,23} and {03,12}. The exact checks include it.
For each F at most K(K-1)<=K^2 ordered routes exist, so a micro-edge belongs
to at most 2K^2 routes.

Under uniform pi,
E_slide=(kappa/n) sum_unoriented_microedges |Delta f|^2 and
E_add=kappa/(2Kn) sum_F sum_{e,f in F}|f(F-e)-f(F-f)|^2.
Path Cauchy-Schwarz therefore gives E_add<=DK E_slide and

    E_trace <= [1+2K(K-1)] E_slide = C_K E_slide.

This also works for complex observables by the absolute-square inequality.
Fixed symmetric conservative additions leave pi invariant and add a
nonnegative Dirichlet form; they can be incorporated after the comparison.
This presumes a well-defined geometric Markov generator with the stated
constant baseline slide rates, not arbitrary dependence on hidden marks.

## 3. External conductance input, with normalization checked

The byte-pinned Jerrum--Sinclair 1989 paper, Theorem 3.6 (printed p.1161,
PDF page13), states the conductance lower bound 1/(16mR^2) for the indicated
matching chain on any graph with a perfect matching. Section3 initially
introduces bipartite graphs, but the theorem explicitly has general-graph
scope. Its transition specification on printed pp.1156-1157 selects a graph
edge uniformly, then adds a probability-one-half hold. Each distinct slide,
completion or deletion has probability 1/(2m). Hence
P_discrete=I+B/(2m*kappa), where B is the continuous-time generator here.
The exact finite checks assemble edge proposals separately and recover this
identity, including all holding probabilities.

Theorem2.2 (printed p.1153/PDF5), with conductance defined in Eq.(2), gives
decay factor 1-Phi^2/2 for a reversible chain with diagonal at least one-half.
Applying that decay to an eigenvector gives gap(discrete)>=Phi^2/2. Thus

    gap(Broder) >= kappa/(256mR^4),
    gap(slides) >= kappa/(256mR^4 C_K).

The primary PDF formula and theorem scope were visually checked on PDF13;
Theorem2.2 was also visually checked on PDF5. Pages4,5,8,9,13 were extracted
and read. The extraction warned about rotated text, so it was not used alone
to settle the factor16 formula. The web-tool retrieval failed due to source
length; the supplied local PDF's matching SHA supplies the source identity.
The external theorem's whole proof is not independently verified here.
Source: https://people.eecs.berkeley.edu/~sinclair/perm.pdf.

## 4. Green operator and uniform killing bounds

For any finite irreducible symmetric S on Omega, L=-S, gap g and uniform pi,
the initial row density relative to pi has centered L2 norm sqrt(n-1).
Spectral contraction and Cauchy-Schwarz imply

    sum_y |P_t(x,y)-1/n| <= min(2,sqrt(n-1)e^(-gt)).

Integrate against bounded f and split at log(n)/(2g). The first part is at
most log(n)/g and the remaining tail at most 1/g. Therefore for
A0=integral(P_t-Pi)dt=L^-1 on centered functions,

    ||A0 f||infty <= T_G ||f||infty,  T_G=(1+log n)/g.

This holds even for noncentered f since A0 annihilates constants. K>=2
ensures n>=K>=2; the singleton case needs a direct clock calculation.

Each adjacent-hole state has total birth hazard beta. Let p=pi(h)=KZ/n>0.
For a full-geometry event D define a_D=h 1_{completion in D}. The identity
pi(a_D)=p U(D) follows from exactly K parents per perfect matching.
The killed resolvent solves (L+beta H)u=beta a_D. With c=pi(u),v=u-c,

    v=beta A0(a_D-hu),  ||v||infty<=beta T_G,
    c-U(D)=-pi(hv)/p.

The first bound uses 0<=u<=1 and a_D in {0,h}, so |a_D-hu|<=1 rather than2.
The second gives |c-U(D)|<=||v|| since pi(h)=p. In particular there is no
inverse-p penalty. Supremizing over D yields TV(exit,U)<=min(1,2beta T_G)
from every initial state, hence every entrance law, including beta-dependent
ones. Earlier almost-sure finite filling permits applying this only upon
entry to Omega when growth starts at a lower count. It makes no claim about
the time taken by those earlier levels.

For lambda>=0, (L+beta H+lambda beta p I)u_lambda=beta a_D and 0<=u_lambda<=1.
Its centered part has norm at most beta T_G(1+lambda p); the averaged equation
is p(1+lambda)c+pi(hv)=pU(D). Consequently

    |u_lambda-U(D)/(1+lambda)|
      <= beta T_G(1+lambda p)(1+1/(1+lambda)).

This proves the stated uniform-event Laplace estimate for each fixed lambda.
It does not by itself claim total variation of the entire continuous-clock
joint law, or uniformity over lambda tending to infinity.

For z=beta p E[tau], (L+beta H)z=beta p and pi(hz)=p. The centered equation is
v=-beta A0(hz), because A0 kills the constant p. Thus
||v||<=beta T_G||z|| and |pi(z)-1|<=||v||. If e=||z-1|| and a=beta T_G,
e<=2a(1+e); for 2a<1 this gives e<=2a/(1-2a). Finiteness of the mean comes
first from finite irreducibility and a nonempty killing set. Moment convergence
is proved separately, not inferred from Laplace convergence.

## 5. Torus substitution and scope

For a fixed integer d>2, even cubic side N>=4, V=N^d=2K and m=2dK. The exact
counting identity R=K chi_N, together with the previously checked Taggi v3
Eq.(2.5), gives R<=K^2/(2d). Using C_K<=2K^2 gives

    g >= kappa d^3/(64 K^11),
    T_G <= 64 K^11(1+2dK log2)/(kappa d^3),

where log n<=m log2 uses only the edge-subset count. Thus
(beta_N/kappa)K^12 ->0 is sufficient for the preceding exit, fixed-lambda
clock and scaled-mean limits, uniformly over initial geometry. The identities
and constants survive fixed symmetric conservative additions. The relevant
parameters are geometric rates; no marked-state ergodicity is inferred.

The prior Taggi statement/hypothesis check is reused at its exact PDF hash:
unweighted all-sector perfect matchings on an even periodic cubic torus,
d>2, opposite-sublattice monomer numerator, and positive-time return constant
r_d. It gives (1-r_d/2)/(4d) <= liminf chi_N/V <= limsup chi_N/V <=1/(4d).
Since beta E[tau]/V=(chi_N/V)(beta p E[tau]), the same two bounds follow
along the sufficient schedule. No coefficient limit or total empty-start
upper clock bound is supplied. Source: https://arxiv.org/html/1909.06558v3.

Dropping connectivity invalidates the physical slide comparison (the earlier
edge-plus-square counterexample is retained in the dependency evidence).
Dropping a perfect matching can eliminate killing entirely. A marked process
need not be irreducible even when its geometry is. At fixed beta the finite
exit law generally is not uniform: on C4 with kappa=1 it has worst-state TV
beta/[2(beta+4)], equal to1/10 at beta=1, even though the constant-hazard clock
is exactly exponential. The optional symmetric moves do not justify asymmetric
or state-reweighted dynamics. R may be exponentially large on general graphs;
the proved comparison alone is not a polynomial theorem for that class.

## 6. Independent executable controls and preserved failure

The separately assembled eleven graphs include paths4/6, cycles4/6, diamond,
complete4/6, two triangles joined by a bridge, two squares joined by a bridge,
K3,3 and the cube. Their near/full sizes range from3/1 to45/15. Exact controls
check the Schur matrix, edge-proposal normalization, row sums, harmonic energy,
conditional variance, centered inverse, all ordered reference routes and
immutable slide legality. Exact conductance minimization is performed when
the auxiliary state count is at most12. Spectral gaps and form-PSD checks
are numerical corroboration of the analytic proof.

Eight smaller fixtures additionally use exact rational killed resolvents at
beta=1/10000,1/300,1/10,1, checking all entrance states and all full-geometry
events for lambda=1/2,2. Exact errors are compared numerically to the proved
logarithmic bounds; conditional mean estimates are tested only when2beta T_G<1.
Constant-hazard controls check the exact exponential-clock equation.

ATTEMPT_01 preserves a checker failure: an algebraically zero symbolic residual
was compared before simplification, so SymPy structural equality failed. The
only repair simplified that residual; the original checker bytes and complete
stdout/stderr/receipt remain. No scientific target or primary source changed.
The successful run has empty stderr. This evidence predates access to author
checker bodies or results. No production trajectories were accessed.
