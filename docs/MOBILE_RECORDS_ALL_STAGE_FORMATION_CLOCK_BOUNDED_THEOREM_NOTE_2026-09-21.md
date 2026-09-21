---
claim_id: mobile_records_all_stage_formation_clock_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied classical paired-birth and immutable-record slide process on a finite connected simple graph admitting a perfect matching, every nonfull geometric matching layer is connected. At fixed graph in the slow-birth limit, all interbirth clocks become independent exponentials with matching-count rates, and successive postbirth geometries become independent uniform matchings. An injective alternating-path bound controls the total mean formation coefficient; an auxiliary-chain comparison isolates the remaining quantitative all-stage mixing obligation. No simultaneous volume/rate schedule, fixed-rate thermodynamic clock, marked-state ergodicity, quantum mechanism or physical TOE is established."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_geometric_formation_selection_and_clock_bounded_theorem_note_2026-09-21
runner: scripts/mobile_records_all_stage_formation_clock_2026_09_21.py
---

# The entire formation clock for mobile permanent records

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

This extends the [geometric formation and final-pair theorem](MOBILE_RECORDS_GEOMETRIC_FORMATION_SELECTION_AND_CLOCK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
from the last pair of vacancies to every stage of formation. Under the same
specified record rules, vacancies can be transported through any nonfull
matching layer without destroying an existing record. This permits an
empty-start formation-clock formula in a fixed-graph slow-birth limit.

The model is not a derivation from the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
Paired births, exact classical recognition of antipodal contents, geometric
partnership, the local transport rule, and the rates are supplied premises.
The parent theorem remains an explicit provisional dependency; this extension
does not confer retained status on either claim.

For a graph on 2K vertices, let a_j count its j-edge matchings. As the birth
rate beta tends to zero with the finite graph and slide rate fixed, the
scaled interbirth times converge jointly to independent exponentials with
rates (j+1)a_(j+1)/a_j. The total mean coefficient is

    C(G) = lim_(beta->0) beta E_empty T
         = sum_(j=0)^(K-1) a_j/[(j+1)a_(j+1)].

Writing R=a_(K-1)/a_K gives R/K <= C(G) <= 2 R H_K/(K+1).
With the explicitly named monomer input already checked in the parent note,
the cubic-torus coefficient is bounded between order volume and order
volume times log volume. The slow-birth limit is taken first at each graph;
this is not a bound at a fixed positive birth rate.

A separate-context check reconstructed the connectivity proof, alternating-
path injection, killed-chain composition and comparison normalization before
opening the author controls. It found no unresolved mathematical correction.
The following complete original argument is preserved with only its title
removed and headings shifted. Its historical pending-review wording records
its original state; the source-bound review packet records completed coverage.

## Complete conditional argument

2026-09-21. Root candidate conditional theorem and proof, awaiting independent
reconstruction. This continues the supplied classical-key geometric process.
It adds no primitive, rate-selection principle, deletion channel, quantum
operation or physical field identification. Every statement below is finite
graph unless a limiting order is written explicitly.

### State space and claims

Let G be a connected simple graph on V=2K vertices, K>=2, with at least one
perfect matching. Write E for its edges, m=|E|, Omega_j for its j-edge
matchings, a_j=|Omega_j|, a_0=1, Z=a_K, and R=a_(K-1)/a_K.
Each legal geometric slide {b,c}->{a,b}, with a vacant and a,b,c distinct,
has continuous-time rate kappa>0. The two immutable record contents move
b->a and c->b. This is the same local move as in the earlier formation note.

Every edge with two vacant endpoints receives a paired birth at rate beta>0.
Birth content can use the earlier neighbor-dependent distribution: only its
integrated geometric rate beta is used here. For now no other moves are
included. Adding symmetric same-cardinality moves preserves the connectivity
and stationary-law arguments, with the corresponding generator substituted.

The proposed conclusions are:

1. At each j<K, the geometric slide chain on Omega_j is irreducible (j=0 is a
   singleton). No marked-state ergodicity is claimed.
2. Let tau_j be the time between entry to Omega_j and the next birth, starting
   empty and stopping at the first completed matching. At fixed G and kappa,
   as beta decreases to zero, the vector (beta*tau_0,...,beta*tau_(K-1))
   converges to independent exponential variables with respective rates

       p_j = (j+1) a_(j+1)/a_j.                                    (1)

   The completed geometry is uniform and independent of the limiting clock
   vector. The successive geometries immediately after births also have
   independent uniform limits on their respective cardinalities. Their
   joint limiting independence does not mean finite-beta trajectories lack
   record identities or memory.
3. Writing T_total=sum_j tau_j and H_K=sum_(k=1)^K 1/k,

       lim_(beta->0) beta E_empty T_total
         = C(G) := sum_(j=0)^(K-1) a_j/[(j+1)a_(j+1)],              (2)

       R/K <= C(G) <= 2 R H_K/(K+1).                               (3)

   The whole-clock Laplace transform is

       lim E exp(-s beta T_total) = product_j p_j/(p_j+s), s>=0.    (4)

These are ordered fixed-graph slow-formation limits. This note does not claim
a polynomial schedule beta(V) sufficient for all stages, an upper bound at
fixed positive beta, or a theorem on infinite-volume formation dynamics.
A comparison lemma below isolates one route to that additional question.

### Empty-corridor parent transport

First take any matching T of size k>=2, not necessarily perfect or maximum.
For e,f in T, the two parents T-e and T-f can be connected by at most V-2
legal slides. The construction never creates or deletes a record.

Contract every edge of T to one quotient vertex and retain every vertex not
covered by T as a singleton quotient vertex. This quotient of a connected
graph is connected. Choose a simple path from the node e to the node f.
Between consecutive matched nodes on that path there is a corridor containing
s>=0 singleton nodes. Those singleton sites are vacant in every parent of T.

Name the first matched edge aa', the second bb', and the connecting original
path a,z_1,...,z_s,b. Start with aa' absent and bb' occupied. Move the bb'
record pair backward along this empty corridor: the legal slides are

    (z_s,b,b'), (z_(s-1),z_s,b), ... , (a,z_1,z_2), (a',a,z_1),

with the evident shorter forms when s=0 or 1. A slide (u,v,w) replaces the
occupied edge vw by uv and moves its two immutable contents v->u and w->v.
After s+2 slides, aa' is occupied, bb' is absent and every intervening
singleton site is vacant again. All other pairs retain their original edges.

Concatenate these segments. If the quotient path visits r matched nodes and
s_total singleton nodes, its length is 2(r-1)+s_total. Since r<=k and
s_total<=V-2k, the length is at most V-2. Each intermediate matching is either
T-e' or T-e'-f'+g, where g is the currently moving edge. Each segment traverses
distinct corridor edges; successive segments have distinct pairs of missing
reference edges. Thus no physical transition is repeated on a route.
The exact reverse route restores the actual immutable contents, not just
the unmarked matching. For k=1 the parent space is the singleton empty state.

### All nonfull cardinalities are connected

Fix a perfect matching P and a matching M of size j<K. In M symmetric-
difference P, components are alternating cycles and paths that begin and end
with P edges. There are exactly K-j such paths; a length-one path is allowed.
The absence of any other path type uses the fact that P covers every vertex.

On a path v_0,...,v_(2r+1), the M edges are v_1v_2,...,v_(2r-1)v_(2r),
and both endpoints are vacant. The r slides

    (v_0,v_1,v_2), (v_2,v_3,v_4), ...,
    (v_(2r-2),v_(2r-1),v_(2r))

replace these by P edges and leave just the last P edge vacant. After doing
this on all paths, every non-P edge of M lies on one of the alternating
cycles, and at least one P edge h is absent with both endpoints vacant.

Choose a remaining alternating cycle and one of its M edges e. The matching
T=M+h has size j+1. The parent-transport lemma takes T-h=M to T-e. This
fills h, vacates e and changes no other final edge of M. Its intermediate
slides may leave the cycle and return; only the final state is used next.

Write the cycle in the order x_0,...,x_(2r-1), with e=x_(2r-1)x_0 absent,
the other M edges x_1x_2,...,x_(2r-3)x_(2r-2), and P edges x_0x_1,
x_2x_3,...,x_(2r-2)x_(2r-1). The r-1 successive slides from x_0 move the
occupied pairs onto the first r-1 P edges. Only the last P edge is now
vacant. The cycle is aligned with P; that vacant P edge supplies h for the
next cycle. Repeating leaves a j-edge subset of P.

Any two j-edge subsets of P are connected too. Add a desired but absent P
edge h virtually to the first subset, then transport the missing edge from
h to an unwanted occupied P edge e. The endpoint has exchanged e for h.
Iterate until reaching the second subset, and reverse the corresponding
path from any target matching. This proves irreducibility using only slides.
The virtual T is a proof reference, not an extra physical birth.

Perfect-matchings-only dynamics need not be connected: the slide process has
no vacancies at j=K. Nothing in this proof asserts otherwise.

### The next-birth law at an arbitrary cardinality

For 1<=j<K, let S_j be the symmetric slide generator, pi_j uniform on Omega_j,
and A_j(M,T)=1 when T is obtained from M by adding one vacant edge.
Let h_j=A_j 1 be the number of vacant edges, H_j=diag(h_j).
Then 0<=h_j<=m. Every T in Omega_(j+1) has exactly j+1 birth parents, so

    pi_j A_j(T)=(j+1)/a_j,    pi_j h_j=p_j,

and the stationary birth flux normalized by p_j is exactly uniform on
Omega_(j+1). Irreducibility and p_j>0 make eventual birth almost sure.

For clarity, a uniform error control can be proved without assuming constant
hazard. Set Pi_j f=pi_j f and

    G_j = integral_0^infinity (exp(t S_j)-Pi_j) dt.

Choose B_j >= ||G_j||_(infinity->infinity). For example the symmetric gap
g_j>0 gives B_j=(1+log a_j)/g_j by the elementary spectral/TV bound used in
the earlier polynomial note. This is a finite constant here, not a claimed
polynomial bound in V.

For any event D of next geometries, let a_D=A_j 1_D and
u(M)=P_M(next geometry in D). The killed equation is

    (-S_j+beta H_j)u=beta a_D.

Write u=c+v with pi_j v=0. Since 0<=u<=1, 0<=a_D<=h_j<=m,

    v=beta G_j(a_D-h_j u),    ||v||_infinity<=beta m B_j.

The constant equation gives
c=U_(j+1)(D)-pi_j(h_j v)/p_j. Consequently

    sup_M ||Law_M(next geometry)-U_(j+1)||_TV
       <= min(1, 2 beta m B_j).                                   (5)

The factor p_j cancels because pi_j h_j=p_j. A small mean hazard does not
by itself introduce a 1/p_j penalty into this bound.

For lambda>=0 replace u by
E_M[exp(-lambda beta p_j tau_j) 1_D(next geometry)].
Its equation replaces H_j by H_j+lambda p_j I. Since again 0<=u<=1,
the same decomposition yields

    sup_M |u(M)-U_(j+1)(D)/(1+lambda)|
      <= beta B_j (m+lambda p_j)(1+1/(1+lambda)).                   (6)

For the mean set w=beta p_j E_M tau_j. Its constant equation is pi_j(h_j w)=p_j.
The centered equation is v=-beta G_j(h_j w), because G_j annihilates constants.
Thus ||w-1||<=2 beta m B_j ||w|| and, if delta_j=beta m B_j<1/2,

    sup_M |beta p_j E_M tau_j - 1|
       <= 2 delta_j/(1-2 delta_j).                                (7)

At j=0 the waiting time is exactly Exp(beta m), independent of a uniformly
selected graph edge, and p_0=m. No inverse gap is needed for this singleton.

### Composition of the stage kernels

At a fixed finite graph there are only K stages. Bounds (5)-(7) are uniform
over every entrance matching. Apply the strong Markov property at each birth:
(6), first for events and then by finite linear combination on each finite
exit state space, makes each normalized waiting time and next geometry
independent of the preceding stage in the limit. Iterating the kernels gives
the product transform in (4) and the joint conclusion stated above. Laplace
transform convergence on nonnegative waiting times identifies the probability
law. Formula (7) also converges uniformly at every stage. Summing its conditional
means proves (2), rather than inferring convergence of means from weak
convergence alone. Starting at a specified later cardinality simply omits
the earlier factors and summands.

This composition holds for geometric observables. Birth contents retain
their neighbor dependence, and permanent marked records can keep historical
correlations. Those hidden marked correlations do not alter the supplied
autonomous geometric rates used in this proof.

### An injective counting bound for the entire clock

For M in Omega_j and P a perfect matching, their symmetric difference has
exactly K-j augmenting path components for M. Mark one such component Q
and flip Q in both matchings. The images

    U = M symmetric_difference Q in Omega_(j+1),
    W = P symmetric_difference Q in Omega_(K-1)

uniquely recover the preimage. The two vertices unmatched by W are precisely
the endpoints of Q. In U symmetric_difference W they determine the unique
component connecting them; its edges are Q. Flipping Q again recovers M and
P. Thus the map from triples (M,P,Q) to pairs (U,W) is injective, giving

    (K-j) a_j Z <= a_(j+1) a_(K-1).

It follows that 1/p_j <= R/[(j+1)(K-j)]. Summing and using

    sum_(k=1)^K 1/[k(K+1-k)] = 2 H_K/(K+1)

proves the upper half of (3); its lower half retains the final-stage term
1/p_(K-1)=R/K. No mixing theorem is used in this counting inequality.

On an even side-length N>=4 nearest-neighbor torus in dimension d>2, let
V=N^d=2K. If the already identified Taggi v3 monomer theorem and normalization
R=K chi are imported, its bound R<=K^2/(2d) yields

    C(G)/V <= K H_K/[2d(K+1)] <= H_K/(2d).                         (8)

The same named theorem's lower bound on chi/V gives

    liminf_(N->infinity) C(G_N)/V >= (1-r_d/2)/(4d)>0.             (9)

Here r_d is the expected number of strictly positive-time returns of simple
random walk on Z^d, with the convention checked in the earlier clock note.
The limit beta->0 defining C(G_N) is taken first for each graph. Equations
(8)-(9) place that coefficient between order V and order V log V. They do
not prove a limiting coefficient or transfer this bound to a fixed beta.

### A conditional comparison route to quantitative all-stage relaxation

This additional lemma is separate from the fixed-graph clock conclusions.
For j>=1 set k=j+1. On Omega_j union Omega_k define an auxiliary symmetric
chain B at rate kappa per legal single-edge addition/deletion between levels
and per valid single-edge exchange within either level. An exchange can
replace disjoint edges and need not be physically local. All such events are
only a comparison device; they are not added to the record process.

For a function g on Omega_j, extend it to an upper matching T by the average
of g(T-e) over its k parents. Write

    U = sum_(T in Omega_k) sum_(unordered e,f in T)
            [g(T-e)-g(T-f)]^2,

and let D_slide be the unnormalized sum of squared differences over undirected
physical slide edges in Omega_j. The lower-level exchange energy is exactly
D_slide+U: overlapping replacements are slides; disjoint replacements have
the unique union T. The add/delete energy is U/k by the variance identity.
Two adjacent upper states have a common parent C. Applying
(x-y)^2<=2(x-z)^2+2(y-z)^2 with z=g(C), and observing that a fixed (T,C) has
at most m upper neighbors with that common parent, bounds upper exchange
energy by 2m U/k. Hence the auxiliary unnormalized energy is at most

    kappa [D_slide + (1+(1+2m)/k) U].                              (10)

Route each unordered parent pair using one chosen orientation of the
empty-corridor construction. Its length is at most V-2. A physical edge
M<->M' identifies its moving edge at either endpoint as M minus M'.
Each possible reference T is either M+e or (M-g)+e+f, using graph edges e,f;
including the other orientation gives at most 2(m+m^2) candidate references.
Each reference has at most k(k-1)/2 unordered parent pairs. The no-repeat
property of the routes therefore gives

    U <= (V-2)(m+m^2)k(k-1) D_slide.

Let

    C_(V,m,k)=1+(V-2)(m+m^2)(k-1)(k+1+2m).

Equations (10) and the variance decomposition under uniform measure on the
two-level space imply

    gap(S_j) >= gap(B)/C_(V,m,k).                                 (11)

Indeed the lower-level mass a_j/(a_j+a_k) appears in both the energy
normalization and the lower bound for the variance of the extension, and
cancels. There is no hidden reciprocal mass factor. The chain B is connected
because its lower slide subgraph is connected and every upper state has k
parents. Thus (11) is nonvacuous at any fixed graph.

No uniform polynomial lower bound on gap(B) is proved or imported here.
Dagum-Luby 1992 is a relevant lead, but the retrieved text loses key displayed
formulas and is insufficient to authenticate a quantitative theorem. The
2024 fixed-distance-from-maximum down-up result does not cover this question
by substituting a distance that decreases as 1/K. Neither source is used in
(1)-(11). A verified auxiliary bound would combine with (11), (5)-(7) and
the sum over stage errors to give an explicit simultaneous schedule.

### Evidence status and remaining physical question

The preliminary parent-transport checker tested 842 connected graphs and
115062 ordered parent pairs, replaying immutable marked contents forward and
backward. That finite screen is not an all-graph proof. The complete
all-stage checker will bind this note, reconstruct graph connectivity and
the counting injection, check killed-chain stage composition, and test the
Dirichlet comparison. Independent reconstruction remains pending.

This is a result about a supplied formation process with exact geometric
constraints. It gives no dipolar-correlation theorem, propagating transverse
sector, local quantum implementation, Maxwell identification, Lorentz
symmetry, gravity, or empirical prediction. Those remain separate research
obligations.

## Verification and remaining questions

[The evidence packet](../.claude/science/mobile-record-all-stage-formation-20260921/README.md) contains the unchanged primary argument,
both author source files, the complete four-group control results and one
portable selective-review capsule. The runner executes the complete all-stage
checker, which imports and exercises the corridor construction. It does not
repeat the separate preliminary 842-graph corridor screen. The controls include
marked-record route replay, exhaustive small-graph counting injections, exact
killed-chain calculations and finite matrix comparisons. Finite controls do
not replace the all-graph proofs.

The auxiliary-chain comparison supplies no uniform polynomial spectral-gap
bound. Neither the incompletely retrieved Dagum-Luby formulas nor a fixed-
distance-from-maximum mixing theorem is imported. Quantitative all-stage
preparation, infinite-volume dynamics, the quantum bridge and a physical
identification of fields remain open. This proposed theorem does not imply
Lorentz symmetry, gravity, a TOE or an empirical prediction.

This is a draft research milestone with selective independent checks. Formal
retained status remains on the repository's independent audit path.
