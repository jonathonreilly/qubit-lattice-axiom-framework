# Independent reconstruction before author-control access

2026-09-21. This is a selective review of the two frozen notes identified in
PRE_COMPARISON_SOURCES.json. Both were read completely before the new author
checker or result directory was accessed. Existing matching-connectivity,
two-level comparison, Broder normalization, color-preparation and wave
arguments are reused at their checked identities. The Jerrum--Sinclair and
Taggi statement/hypothesis reviews are inherited; no new whole-proof review
of those papers is claimed.

At this boundary I find no mathematical counterexample or missing hypothesis
in the intended statements. The deterministic-window comparison is on the
closed matching-geometry/pair-color state space defined in its Section 2.
It must not be read as total-variation mixing of every immutable identity or
continuous projector key. That stronger statement is neither used nor
established. The calculations below include the bad histories rather than
conditioning them away.

## 1. Padding, fibers and the imported comparison chain

Fix j in 1,...,K-1, k=j+1, h=K-k. Add h labeled dummy vertices per part,
joined to every original vertex of the opposite part, with no dummy-dummy
edge. The padded graph is connected, simple and bipartite, has m+2hK edges,
and admits a perfect matching by extending any original k-edge matching.

For an original matching, the four fiber factors are obtained independently
on the two sides. Write f0=(h!)^2.

* A perfect padded matching projects to rank k. The h unused original
  vertices per side are assigned bijectively to h opposite dummy vertices,
  giving f0.
* Two original holes give rank j. Per side choose the original hole from
  h+1 vertices and assign the remaining h: (h+1)^2 f0 in total.
* One original and one dummy hole give rank k. On the deficient side there
  are h choices for each hole and (h-1)! assignments; the other side gives
  h!. This is h f0 for each of the two orientations, hence 2h f0.
* Two dummy holes give rank k+1. Each side has h choices for its dummy hole
  and (h-1)! assignments, so the total is h^2((h-1)!)^2=f0. This class is
  absent at h=0, when k=K and a_(k+1)=0.

Consequently the near/perfect ratio is exactly the displayed R_hat. The
previously checked injection gives a_j/a_k<=R/(h+1); counting extensions
gives (k+1)a_(k+1)<=m a_k. Substitution yields R_hat<=U_j, with no regularity
or uniform-sampling hypothesis on the original graph.

The padded graph satisfies the already checked hypotheses for the ordinary
Broder chain. At rate kappa for each legal graph-edge proposal, its gap is
at least kappa/(256 m_hat R_hat^4). The factor 256 includes the published
lazy proposal convention as reconstructed in the prior review. These
dummy states, completions and deletions remain proof devices.

## 2. Function extension and normalized Dirichlet forms

Let B be the original rank-j/rank-k auxiliary state set. Its within-level
edges are all valid one-edge replacements, including disjoint replacements;
its cross edges are one-edge additions/deletions. Its invariant measure is
uniform. Define F to be g of the original projection on good padded states;
on a bad projection U of rank k+1 take the average of g(U-e) over e in U.

Every padded graph edge offers at most one nontrivial proposal at a state.
On a near-perfect state it can complete two holes or slide into one hole;
on a perfect state only a matched edge can be deleted. Thus degree<=m_hat.
Good-to-good projected transitions are either constant or one of B's edges.
A transition remaining in the two-dummy-hole class leaves U unchanged.
Every exit from that class projects to U-e. These facts follow directly
from the absence of dummy-dummy edges and the bipartite two-hole pattern.

The good fiber weights are f_j=(h+1)^2 f0 and f_k=(2h+1)f0. Their minimum
is f_min=(2h+1)f0 and maximum is f_max=(h+1)^2 f0, including h=0. Retaining
f_min copies of every B state inside the padded measure gives a mixture
component of mass w=f_min Z_B/Z_hat with law uniform on B. The law of total
variance therefore gives Var_hat(F)>=w Var_B(g), for real or complex g.
Equivalently this follows by minimizing the pointwise inequality over the
constant c. No factor depending on the potentially small mass w is lost.

Use D_hat=kappa/Z_hat times the sum over undirected padded transition edges,
and D_B=kappa/Z_B times the sum over undirected B edges. At most
f_max m_hat good transitions lie over any B edge. For a bad U and its parent
U-e, at most f0 m_hat edges connect the two fibers. The complete-graph
variance identity on its k+1 parents gives

    sum_e |g(U-e)-average|^2
       = (1/(k+1)) sum_(e<f) |g(U-e)-g(U-f)|^2.

Each parent pair uniquely determines U by its union, so it is not duplicated
over different bad projections. This yields

    D_hat(F) <= w m_hat [f_max/f_min+f0/((k+1)f_min)] D_B(g)
              <= w m_hat(h+2) D_B(g).

The small h=0 case merely discards an unnecessary positive upper bound.
Combining the energy and variance inequalities gives
gap(B)>=gap(Broder_hat)/[m_hat(h+2)]. This is a function-extension comparison,
not a claim that the projected Broder path is Markov. The independent finite
examples in fact show different projected rates inside common good fibers.

Composing the identity-matched empty-corridor comparison gap(S_j)>=gap(B)/C_j
gives Eq. (1). Its physical comparison paths are the previously checked
immutable slides. Bipartiteness is used by the padding construction; this
argument is not an extension to nonbipartite graphs.

## 3. Cubic constants and killing at every positive birth rate

For the even simple cubic torus N>=8, m=6K and K>=256. The inherited Taggi
bound is R<=K^2/6. Since 2<=k<=K and 0<=h<=K-2,

    m_hat<=4K^2,  h+2<=K,
    U_j<=(K^3/6)+4K<=K^3,
    C_j<=1+(2K)(42K^2)(K)(14K)<=2^11 K^5.

Multiplying 256*(4K^2)^2*K*(K^3)^4*(2^11K^5) gives exactly 2^23 K^22.
Thus the conservative gap in every nonempty nonfull layer is at least
kappa/(2^23 K^22). This polynomial statement depends on the controlled R;
there is no unconditional polynomial bound for arbitrary bipartite graphs.

For a finite symmetric layer let L=-S, pi uniform, conservative gap at least
g>0, birth hazard h in [0,m], p=pi(h)>0, and f=c+v with pi(v)=0. The norm
inequality in L2(h pi) gives

    p|c|^2 <= 2 pi(h|f|^2)+2m||v||^2.

Poincare then gives

    ||f||^2 <= [2/(beta p)+(1+2m/p)/g]
                   [<f,Lf>+beta pi(h|f|^2)].

The bracket's reciprocal bounds the bottom eigenvalue of L+beta H. This
proof allows complex f and hazard zeros. The positive sub-Markov survival
vector has L2 norm at most exp(-lambda t), because ||1||_(2,pi)=1. Point
evaluation costs sqrt(n), so its value is at most
min(1,sqrt(n)exp(-lambda t)). Integrating at its crossing time yields the
factor 1+(1/2)log n exactly. No nonstationary entrance-density estimate is
silently omitted: the sqrt(n) factor covers a point entrance and hence any
mixture. Singleton layers are treated separately as in the note.

At stage j the incidence identity gives p_j=(j+1)a_(j+1)/a_j. The inherited
injection and torus R bound imply p_j>=6/K. Also m/p_j<=K^2,
1+2m/p_j<=3K^2 and 1+(1/2)log a_j<=4K. Each nonempty stage therefore has
uniform mean at most 4K^2/(3beta)+12*2^23 K^25/kappa. The strong Markov
property permits summing this bound despite arbitrary entrance states.
There are K-1 such stages, and the empty stage has exact mean 1/(6beta K).
The displayed 2K^3/beta+2^27K^26/kappa bound follows. It does not assume
rare births or uniform entrance to any stage. Extra symmetric autonomous
conservative transitions preserve the uniform layer law and can only
increase the conservative gap.

## 4. Simultaneous selection schedule

The bound (1+log a_j)/g_j<=2^26K^23/kappa and beta_K=kappa*2^-32*K^-27
give delta_j=beta_K m B_j<=3/(32K^3). The earlier arbitrary-hazard exit
estimate is uniform over entrances, so successive conditional kernels may
be coupled to independent uniform-rank kernels. Their sequence total
variation is at most sum_j 2delta_j<=3/(16K^2); the first edge is already
exactly uniform.

For a fixed vector of bounded nonnegative clock parameters, the inherited
killed-transform event bound is at most 2delta_j(1+Lambda). Layer-cake
integration extends the event bound to any test in [0,1], and telescoping
sub-Markov kernels gives the displayed total transform error. No extra
factor of two for signed tests is required, because the remaining tests
in that telescoping argument are nonnegative and at most one. This is not
total-variation convergence of a growing-dimensional continuous clock law.

The mean error is bounded by

    2delta_j/(1-2delta_j) <= 3/(13K^3).

Its uniformity allows a weighted sum with weights 1/p_j, giving the same
relative bound for beta_K E T_fill/C(G). The earlier counting result gives
C(G)<=K H_K/3, hence the special-family time O(K^28 log K/kappa). This
volume-dependent beta_K is separate from the fixed-rate bound above.

## 5. Deterministic unconditioned observation window

This part composes the already checked closed geometry/color process; it
does not claim mixing of additional immutable identities or continuous
keys. In the supplied encoding, birth color counts are multinomial and
independent of the autonomous geometry history. Define E={F<=H_N} with
H_N=2A_N/eta. Markov's inequality gives P(E^c)<=eta/2. This event depends
only on the geometry; color-dependent selection would invalidate the
following count-mixture step.

The improved preparation gap is k0/[8N(3N-1)]. The note's s_N therefore
makes the uniform sector bound

    (1/2)14^(K/2) exp(-gap*s_N) <= eta/2.

Condition on the geometry history and the final count sector. On E there
is at least s_N post-completion time before the deterministic t_N; the
uniform contraction is valid for the possibly varying geometry intervals
and boundary permutations. Averaging over the still-multinomial counts
gives p^K, independently of that geometry history. Fixed counts alone would
not give p^K, and longer evolution does not repair that distinction.

For the reference geometry, retain the actual full matching on E and choose
any fixed full matching on E^c. Sample reference colors from p^K independently
of this reference geometry. Mixing the conditional estimates shows

    TV(actual projected law at t_N, reference law)<=P(E^c)+eta/2<=eta.

This is an inequality for the original unconditioned law. Histories that
complete only after H_N, including those complete by t_N, are charged fully
to the error; histories still partial at t_N are charged as well. The
construction does not postselect on completion or physically reset records.

Both projected laws can be coupled at t_N, then continued with the same
transition randomness on agreement. Agreement states are full, where no
birth or vacancy slide remains and the two generators coincide. Coupling
therefore persists for the future interval NT. The initial reference
geometry distribution may be biased or nonstationary; the quantitative
wave bound was proved uniformly over such distributions.

The partial-state convention xi_b=0 at a vacant black site bounds every
field by 2sqrt(K); the fixed-time propagator has bounded norm on [0,T].
The two residual squared observables differ in expectation by at most
C K eta. With eta=N^-4 this is O(N^-1), and the independently checked
reference bound contributes O(N^-1/6). This proves the displayed supremum
of expectations. Vanishing path-law total variation also transfers each
fixed finite mode/time Gaussian law. It does not prove a path-supremum or
infinite-dimensional limit.

The two-endpoint sqrt(2) convention and product-reference phase error are
inherited. Their bad-event contribution is handled by the same O(K eta)
bound. At fixed rates, H_N's leading upper-bound term is order N^82/kappa;
s_N is only order N^5/k0 plus a logarithmic term. This is a deliberately
loose observation schedule, not a measured filling law. Isotropy, nonzero
gamma and nonzero Q remain necessary for the particular four-wave scalar
speed statement; the general matrix estimate has its broader stated scope.

## 6. Controls, countercontrols and verification limits

independent_check.py imports no author code. Its first execution passed
with empty stderr; all output rows were read. The original graph fixtures
are path4, path6, cycle6, two squares connected by a bridge, and K4,4, with
all eleven nonempty nonfull ranks. They cover h=0,1,2, irregular degrees,
a bridge and dense graphs. Every padded full/near state and transition is
enumerated; the largest padded state set has 2400 states.

All four fiber classes, degree bounds and transition projections agree
exactly. In each bad fiber the direct enumeration additionally finds two
exits per removed original edge per augmented state, consistent with the
source's looser bound. Common good fibers with distinct projected outgoing
rates occur for all six h>0 examples. This is a countercontrol to replacing
the function extension by an unjustified Markov projection.

The checker constructs the full integer matrix of the extension, scaled by
k+1, and compresses every augmented edge form. The claimed energy upper
bound minus that compressed form is exactly a nonnegative-conductance
Laplacian, hence positive semidefinite for all real and complex test
functions on each fixture. Variance inequalities are checked with all
coordinate vectors and additional integer vectors; their general proof is
the mixture argument above. Gap comparisons are floating spectral
corroboration, not exact eigenvalue claims.

There are 24 exact rational killed-resolvent controls at beta=1/11,1,7 on
eight physical layers, including states of zero hazard. Eigenvalue and
logarithmic bounds are compared numerically. These controls use an
independent safe gap 1/n^2: a spanning-path comparison gives at least
2/(n-1)^2 for any connected unit-rate graph, so this weaker value suffices.
An exact two-state control with h=(0,H) gives mean waiting times
2/(beta H)+1/a and 2/(beta H), showing why a conservative gap cannot be
discarded at a zero-hazard entrance.

Exact rational arithmetic checks the cubic products and selection constants
at five sizes and several ranks. A separate nine-state law/coupling control
retains bad mass 1/10, obtains unconditioned TV 51/320 below 9/40, and
verifies contraction to 39/320 under a common future Markov kernel. A fixed
one-of-each two-color count sector remains at TV 1/2 from the two-site iid
law, demonstrating the necessity of the multinomial sector mixture. This
finite-law control tests the coupling argument, not a replacement record
model or a new physical process.

No independent failure occurred before this seal. No author checker,
author output, production trajectory, new quantum work or unrelated source
was accessed. No complete proof of an external literature theorem has been
repeated. There is no formal audit status or publication action.
