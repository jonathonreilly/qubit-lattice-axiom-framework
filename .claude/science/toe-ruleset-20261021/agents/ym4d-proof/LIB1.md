# PRE-STATED — LIB-1

This first section fixes the choice and statements before the proof and any
new finite check. Source reading and exploratory reasoning have already
occurred. It contains no result or test verdict. Its original byte prefix
and filesystem stat are recorded in `LIB1_LOG.md`.

## Target choice

Choose **R10: boundary-polymer resummation under enlargement of the inactive
region**, including its counting prerequisite and its original-source norm
interface. The method is Jonathan Dimock's exposition of Tadeusz Balaban's
renormalization-group program: Part III, Appendix B, Lemma 19, equations
(238)–(245), and Part II, Appendix E, Lemmas E.1–E.3, pages 88–91. Rebuild
the argument on our four-dimensional block lattice; no literature theorem
will be a premise. The block graph and full support norm below are those of
`SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md` (H23)–(H24), not an abelian field
substitute. The hole geometry is a newly specified library interface.

| Candidates considered | Choice reason |
|---|---|
| R1, normalized kernel composition | Already supplied by SOFTHARD P1 and the Decision-4 normalization identity; does not meet the nonduplication condition. |
| R2, finite Gaussian elimination | LINEAR_PACKAGE/STEP55 and SOFTHARD P4 already supply the finite algebra. Matching a new nonlinear gauge space is a different task. |
| R3, coarse-energy comparison | Complete scalar proof strategy, but existing all-chain coercivity/linear estimates overlap the elementary part; a useful new SU(N) punctured-domain instance needs additional transport estimates. |
| R4, product-measure connected expansion | RECOVERY_CLUSTER_ASTRA §4 already supplies the corrected rooted-norm/tree proof; the current source/history note supplies an actual completion-good gas. Repeating it would duplicate work. |
| R5–R7, gauge identity/gap/regular representative | Primarily hard-route replacement work; the open expositions leave additional gauge, propagator or projection inputs. Decision 4 remains soft. |
| R8–R9, full histories and prices | Actual source/history return already addresses selected sectors. The remaining sea/failure estimate is larger than the complete elementary proof strategy inspected here. |
| **R10, selected** | Serves both routes and HANDOFF step 2's holes/reference bookkeeping and step 4's source locality. SF's collar/HULL regroupings and (H26)–(H27)'s fixed-boundary cancellation do not state the nested inactive-region operation or its norm conversion. The complete scalar strategy, including its counting input, is available in the open PDFs. |

Nonduplication search: `rg -n`/`rg -l` for `resumm`, `inactive region`,
`boundary.polymer`, `punctured.distance`, `regroup`, `hull`, and enlargement
of holes/regions across this folder's Markdown. Relevant statements checked:
`SF.md:423–438,758–779,1242–1289`, `RECOVERY_CLUSTER_ASTRA.md:92–111,231–305`,
`SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md:545–649`, `STEP55.md:579–585`, and the
R10 entries of SOFTHARD and its review. This is a bounded novelty check,
not a certificate of absence throughout every repository branch.

Candidate HEAD: `4f04b662f4d72d7ef269f6d9693ae9ff6424acf9`.
Fetched `origin/main`: `ca2bc7ddf64790da96cd43d42017d000fbfe4808`.
The working notes are candidate sources; neither planning nor local review
labels confer main/audit status. Decision 4 stays in force.

## Statements to establish

**Actual model and domain.** At a fixed level use the finite four-dimensional
periodic block lattice Γ (or a connected rectangular block box), with an
edge between distinct face-neighbour blocks; the degree is at most 8.
One block contains L⁴ level sites, L≥3 odd. The supplied gauge group is
SU(N), N≥2, with normalized Haar measure and u=1/g²>0. Decision 4 is

    s(U)=1−N⁻¹ Re tr U,
    M̄_c(U)=(4! L⁴)⁻¹ Σ_σ Σ_{y∈B(X)} T_y^σ(U),
    K(V,U)=Π_c exp{−κu[1−N⁻¹ Re tr(V_c⁻¹M̄_c(U))]}/𝒩(M̄_c(U)),
    𝒩(M)=∫_{SU(N)} exp{−κu[1−N⁻¹ Re tr(W⁻¹M)]} dW,
    w_ε(U;V)=exp{−u Σ_p(1+ε_p)s(U_p)} K(V,U),   κ>0.

Original coefficient sources vary in precisely the producer's
`D_(rho,lambda)(u)={epsilon: |epsilon_p|<=rho+lambda/u}`. Real U,V and fixed
source-independent history selectors remain arguments. The kernel is fixed
when ε varies. Each source/field is assigned to all blocks its factor reads;
an activity labelled X must read only original data in X. Bounds use
`sup_(real U,V; D_(rho,lambda)(u))`, or the same supremum restricted to a
specified fixed real-data domain. No holomorphy in a hard-selected coarse
field is asserted. Functions are holomorphic in the source variables on a
neighbourhood of the source polydisc (or uniformly on its compact interior
polydiscs).

Let Λ⊆Ω⊆Γ be fixed source-independent active sets. Let P_Ω consist of
nonempty connected X with X∩Ω≠∅, such that for every connected component H
of Γ\Ω, either H⊆X or H∩X=∅. Connectedness always uses Γ's face graph.
For nonempty S⊆Γ define t(S) as the minimum number of edges in a tree in
Γ containing S, allowing auxiliary vertices anywhere in Γ. Set

    d_Ω(X)=t(X∩Ω),
    R_Λ(X)=X ∪ ⋃{H: H is a component of Γ\Λ, dist_Γ(H,X)≤1}.

These lengths are in block units. In particular d_Ω is **not** the metric
obtained by contracting holes to points, and is not SF's continuum touching
tree length; no equality to either convention is assumed.

For X∈P_Ω meeting Λ let B_X be a complex, original-data-local activity.
For Y∈P_Λ define

    B'_Y=Σ_{X∈P_Ω: X∩Λ≠∅, R_Λ(X)=Y} B_X.

**LIB1, part A (exact resummation and geometry).** R_Λ(X)∈P_Λ,
X⊆R_Λ(X), R_Λ(X)∩Λ=X∩Λ, and d_Λ(R_Λ(X))≤d_Ω(X).
The sum of B'_Y equals the sum of B_X over X meeting Λ, pointwise in all
data. B'_Y is local in original data in Y and holomorphic on the same
source domain. Activities not meeting Λ remain explicitly in a separate
inactive term. No action, determinant, indicator, normalization, or
source-only term may be discarded by this identity.

**LIB1, part B (explicit entropy and decay).** Put

    a>log(32768),    C(a)=512/(1−32768 exp(−a)).

Uniformly in the lattice, Ω and v∈Ω,
`Σ_{X∈P_Ω: v∈X} exp(−a d_Ω(X))≤C(a)`.
If κ_B>a and `||B_X||∞≤B₀ exp(−κ_B d_Ω(X))`, then

    ||B'_Y||∞≤C(a) B₀ exp{−(κ_B−a)d_Λ(Y)}.

Here κ_B is a decay rate, distinct from the kernel stiffness κ. An explicit
choice is a=16 log 2, C(a)=1024. The empty active set gives an empty sum.

**LIB1, part C (the source norm interface).** The existing full norm is

    ||B||_μ=sup_{v∈Γ} Σ_{X∋v} exp(μ|X|)||B_X||∞,   μ≥0.

Define the explicitly different active norm

    ||B||_{μ;Ω,act}=sup_{v∈Ω} Σ_{X∋v} exp(μ|X∩Ω|)||B_X||∞,

with value zero when Ω is empty. The proposed inequalities are

    ||B'||_{μ;Λ,act}≤||B||_{μ;Ω,act}≤||B||_μ.

If every component of Γ\Λ has at most M≥1 blocks, the additional full-norm
statement is

    ||B'||_μ≤9M ||B||_{(1+8M)μ}.

For Λ=Γ there is no enlargement and the full-norm constant is 1. The
bounded-hole assumption is explicit and is not supplied for arbitrary
Yang–Mills histories. Keep source differences B_X(ε)−B_X(0), their factor
of two in a supremum estimate, and Cauchy bounds on inner polydiscs.

**Consumer specialization to check.** Starting with Ω=Γ and the exact
(H23) activities `B_X=V_X^F`, (H24) should give active norm at most d_q;
the source difference should give at most 2d_q. Full norm after saturation
uses the additional bounded-hole/stronger-rate hypothesis above. This
narrows HANDOFF steps 2 and 4, and the assembly review's items 11 and 13;
it does not assert the missing normalized sea estimate, failed-return
prices, higher-level induction, or the full RG step.

**Scope test.** For Λ={v} on a four-dimensional torus with connected
complement, use only B_{ {v} }=b ε_v/r on |ε_v|≤r, r>0. Compute the full
input and output norms and retain the filled inactive component. This is
a test of norm bookkeeping, not a no-go claim about alternative returns.

**Success witness.** A full finite-graph proof including the entropy bound,
an exact source/kernel dictionary, literal consumer quotes, and an honest
residue. Optional small finite checks must be pre-stated separately and
respect the brief's load, memory, niceness and single-thread requirements.

<!-- END PRE-STATED LIB1: immutable original prefix -->

# Result — boundary resummation on the actual block lattice

**PROVEN:** LIB1 parts A–C, with the hypotheses and the two different norms
stated above. This is a finite-volume mathematical implication with explicit
constants uniform over the specified graph/region family. The bounded-hole
clause is conditional on its stated geometric bound and stronger input rate.
It does not assert that actual arbitrary histories satisfy those hypotheses.
The exact H24 specialization below has the producer's original source
domain and field supremum, without changing the Decision-4 kernel.

**OPEN:** the normalized sea/failure estimate needed to turn these local
identities into HANDOFF's history-uniform RG step and N1/N2. This author
proof has not received independent review and supplies no retained/audit
status. The unchanged PRE-STATED prefix ends at the marker above.

## 1. Structures, norms and scope of the application

At level k the blocks of RLARGE §0 form Γ; rescaling their centres to unit
spacing gives the graph used here. The graph in this lemma is the ordinary
face-neighbour graph of the **supports X** in H23. The separate G₂ graph,
with degree bounded by 624, groups bad cores Y in the history producer.
Its collars A(Y) are face-connected. Those cores are not silently substituted
for the supports X. Similarly, SF's *-connected cubes and continuum touching
trees use a different convention. They require an explicit conversion before
using a result stated for them; LIB1 does not identify their distances.

The degree bound 8 follows from at most one neighbour in each signed
coordinate direction. Removing periodic duplicates or boundary edges can
only lower it. The proof below works on every finite connected simple graph
of degree at most 8, so in particular on every specified 4D torus and box.
It includes a one-vertex graph. Empty Γ gives empty activity families and
zero norms. All lengths count **block** edges, not fine edges or physical
distance; no factor L or ultraviolet spacing is suppressed in a conversion.

The algebraic physical inputs are only the supplied model in PRE-STATED:
finite L,N,u,κ, the normalized kernel, and the original Wilson coefficient
sources. Its proof neither differentiates a hard constraint nor changes the
group. For real fine fields 𝒩(M)>0 since its integrand is strictly positive;
the normalized expression is therefore well defined. This elementary fact
is not a bound for a returned denominator with complex sources.

**Local-data convention.** A block support includes every fine plaquette
coefficient and every fine/coarse link read by the activity. Boundary
objects can be assigned to more than one adjacent block; a purported local
activity must still carry their complete reading support, including any
collar. This is precisely H23's requirement that every original coefficient
and every actual sea/coarse field read occurs in X. The norm is the H24
supremum over those real fields and the original source polydisc, not a
norm of newly substituted, potentially nonlocal background coordinates.

For mathematical clarity, Ω,Λ and any fixed failure list F are fixed
**combinatorial parameters** when a function of U,V,ε is considered.
Uniform bounds may range over those parameters. Choosing a mask by a
data-dependent global rule and then varying the data through that rule is
a further composition; LIB1 supplies no locality for that composition.
Likewise, source-dependent cutoffs are outside its analytic statement.
Hard functions of the real data already present in B_X are allowed if
they read only X; holomorphy is claimed only in ε.

Suprema below are componentwise suprema on that common domain. For Banach
space valued coefficients the same proof uses the Banach norm and triangle
inequality. On a closed source polydisc, assume holomorphy on a neighbourhood;
alternatively carry every bound on compact interior polydiscs. All sums
over supports are finite at fixed Γ. If an input coefficient is itself an
infinite convergent series, its displayed sup-norm bound is a premise;
LIB1 does not prove that input convergence by renaming its summands.

## 2. Exact resummation and geometry — proof of part A

For a vertex set A write H(A) for the connected components of Γ\A.
Distinct components have no edge between them. Let X∈P_Ω with X∩Λ≠∅,
and put Y=R_Λ(X).

First, every component of H(Λ) added to X either intersects X or has an
edge to X. It is connected, so its union with X is connected. Adding all
such components preserves connectedness. Nothing added lies in Λ, whence

    X⊆Y,                 Y∩Λ=X∩Λ≠∅.                      (L1)

If a component H of H(Λ) meets Y, it either met X, in which case the rule
adds all H, or it meets an added component. In the second case the two
components coincide. Thus H⊆Y. This proves Y∈P_Λ. There is no cascade
through distinct inactive components: an edge between them would make
them a single component. Equivalently, repeatedly adding inactive vertices
adjacent to the current set gives the same Y.

For nonempty S⊆T⊆Γ, every tree containing T contains S; minimizing over
trees gives t(S)≤t(T). In (L1) take S=X∩Λ and T=X∩Ω. Therefore

    d_Λ(Y)=t(X∩Λ)≤t(X∩Ω)=d_Ω(X).                         (L2)

This proof uses ambient trees with their actual edge lengths. It would
not justify assigning zero cost to traversal of a large inactive component.
Nor does it require X∩Ω or X∩Λ to be connected; the tree can join separated
active vertices through Γ.

The function X↦R_Λ(X) is single-valued. Its nonempty fibres partition the
finite family {X∈P_Ω:X∩Λ≠∅}. Hence for all data

    Σ_{X∈P_Ω, X∩Λ≠∅} B_X = Σ_{Y∈P_Λ} B'_Y.             (L3)

Each X in the fibre is a subset of Y. Two data configurations agreeing
on Y therefore agree on every argument of every B_X in this sum, so give
the same B'_Y. This proves locality in **all** original variables. Finite
sums of holomorphic functions are holomorphic on their common domain;
no source radius is lost.

For the entire original sum define explicitly

    B_inactive=Σ_{X∈P_Ω, X∩Λ=∅} B_X.
    Σ_{X∈P_Ω} B_X = B_inactive + Σ_{Y∈P_Λ} B'_Y.         (L4)

This inactive term generally depends on inactive-field and source data.
It is not a numerical constant that can be removed. For any original
prefactor P and any measure for which the expressions are integrable,

    ∫ P exp(Σ_X B_X) dν
      = ∫ P exp(B_inactive) exp(Σ_Y B'_Y) dν.             (L5)

No product structure, positivity, cancellation or zero-free property of
the last integral is inferred. If P contains a determinant, a normalized
kernel factor, an indicator or a source-only term, that same P is present
on both sides. If Λ is empty, B'_Y is an empty family and (L4) retains the
whole expression as B_inactive. If Λ=Γ, necessarily Ω=Γ and R_Λ is the
identity. These cover the endpoint cases. ∎

## 3. A self-contained punctured-polymer count

Fix v∈Ω. For X∈P_Ω containing v write S=X∩Ω and n=t(S), an integer
at least zero. There exists a tree with n edges containing S: a connected
finite graph contains a finite connecting subgraph, a cycle edge can be
removed without disconnecting it, and a minimum among the finitely many
trees exists. Such a tree has n+1 vertices, so

    |S|≤n+1.                                             (L6)

Here and below a tree is the usual connected acyclic subgraph. Its
edge/vertex relation follows by deleting a leaf and induction, starting
with the single vertex. Thus no enumeration theorem is being imported.

For fixed S choose, by any fixed total order on labelled subgraphs, one
minimizing tree. Root it at v and order each vertex's children by a fixed
order of vertices of Γ. Traverse each child subtree and return before
visiting the next child. Every edge is traversed exactly twice, so this
depth-first walk has length 2n. Every step has at most 8 choices. There
are at most 8^(2n) such walks from v. The walk recovers its visited tree
and vertex set; recording which of the at most n+1 vertices belong to S
recovers S. At most 2^(n+1) markings suffice. Consequently

    #{S⊆Γ: v∈S, t(S)=n}≤8^(2n) 2^(n+1).                (L7)

This bound deliberately also counts walks/markings that do not encode a
minimizing tree, and sets S that are not subsets of Ω. Such extra terms
increase a nonnegative bound. For n=0 the traversal is the empty walk
and S={v}, covered by the right side 2.

Now hold S fixed. Every possible X with X∩Ω=S has the form

    X=S ∪ ⋃_{H∈J} H,             J⊆H(Ω).                (L8)

Each included H must have an edge to S. Indeed X is connected and meets
S. A path in X from a point of H to a point of S leaves H along an edge.
The next vertex cannot lie in another component of Γ\Ω, so lies in Ω
and hence in S. There are at most 8|S| components with an edge to S:
choose one edge from S to each such component; these edges are distinct.
The number of choices of J is thus at most 2^(8|S|). Some choices may
leave X disconnected; retaining them only enlarges the count. By (L6)

    #{X∈P_Ω: v∈X, d_Ω(X)=n}
       ≤8^(2n) 2^(n+1) 2^(8(n+1))
       =512 · 32768^n.                                  (L9)

For a>log32768, summing the geometric series gives exactly

    Σ_{X∈P_Ω, v∈X} exp(−a d_Ω(X))
       ≤512 Σ_{n≥0}(32768 exp(−a))^n
       =512/(1−32768 exp(−a))=C(a).                      (L10)

The geometric-series equality follows by multiplying its Nth partial
sum by 1−q and taking the limit q^(N+1)→0 for 0≤q<1. There is no
dependence on |Γ|, the number or sizes of holes, scale, N, u or κ. The
choice a=16 log2 gives 32768 exp(−a)=1/2 and C(a)=1024. These generous
constants were derived, not fitted to a numerical sample. ∎

## 4. Quantitative decay after regrouping — proof of part B

For a given Y with nonempty fibre, choose one vertex v(Y)∈Y∩Λ. By (L1),
**every** X in this fibre contains that same v(Y). This is a choice for
the estimate only, not a coordinate used to define the activity.
Using (L2), κ_B>a, and the input bound,

    ||B'_Y||∞
      ≤B₀ Σ_{X:R_Λ(X)=Y} exp(−κ_B d_Ω(X))
      ≤B₀ exp{−(κ_B−a)d_Λ(Y)}
              Σ_{X∈P_Ω, v(Y)∈X} exp(−a d_Ω(X))
      ≤C(a) B₀ exp{−(κ_B−a)d_Λ(Y)}.                     (L11)

An empty fibre gives zero and satisfies the same inequality. One shared
active root avoids a factor |Y∩Λ| and its additional unit of decay loss
in the broad union estimate printed in Dimock III (244)–(245). This is a
proof for the present graph metric, not an assertion that his continuum
constants can be replaced by these numerical values.

No smallness of B₀ is needed for this **linear** resummation. A cluster
expansion that subsequently consumes these coefficients would have its
own smallness, compatibility and measure hypotheses. This lemma does not
supply those by calling C(a)B₀ small. ∎

## 5. The actual source norm — proof of part C

### 5.1 Active-root contraction

Take μ≥0 and v∈Λ. Triangle inequality and (L1) imply

    Σ_{Y∋v} exp(μ|Y∩Λ|)||B'_Y||∞
      ≤Σ_{X∈P_Ω, v∈X} exp(μ|X∩Λ|)||B_X||∞
      ≤Σ_{X∈P_Ω, v∈X} exp(μ|X∩Ω|)||B_X||∞.             (L12)

Taking the supremum over v∈Λ, and then using Λ⊆Ω and |X∩Ω|≤|X|,
proves both asserted inequalities. The nonnegative sign of μ is essential
for the weight comparisons. The proof sums input supports before spending
any counting factor; entropy already paid in a rooted norm is not charged
again. Empty Λ has zero active norm by definition.

The roots in (L12) are retained active vertices, and its weight counts
only active vertices. This is not the H24 full norm with the letter X
replaced by Y. That distinction is part of the theorem's statement.

### 5.2 Full norm with a stated bound on hole size

Suppose every H∈H(Λ) has |H|≤M, M≥1. For X meeting Λ, every H that
enlarges X in R_Λ(X) has an edge to a vertex in X. If it is disjoint
from X this is the definition of addition. If it meets X, connectedness
of X and X∩Λ≠∅ give a path within X from H to Λ; its first exit from H
is such an edge. Distinct components use distinct incident edges.
There are at most 8|X| such components. Therefore, putting c_M=1+8M,

    |R_Λ(X)|≤|X|+8M|X|=c_M|X|.                          (L13)

If v∈Λ, its rooted full output sum is at most the input full sum at
rate c_M μ, since v∈R_Λ(X) iff v∈X and
exp(μ|R_Λ(X)|)≤exp(c_M μ|X|).

If v∉Λ, let H_v be its unique inactive component and let N[H_v] be H_v
together with all its graph neighbours. Whenever v∈R_Λ(X), H_v meets
or is adjacent to X, hence X∩N[H_v]≠∅. Also

    |N[H_v]|≤(1+8)|H_v|≤9M.

It follows, without any independence assumption on the activities, that

    Σ_{Y∋v} exp(μ|Y|)||B'_Y||∞
      ≤Σ_{x∈N[H_v]} Σ_{X∋x} exp(c_M μ|X|)||B_X||∞
      ≤9M ||B||_{c_M μ}.                                 (L14)

The active-root bound has constant 1≤9M, so taking all roots proves the
full-norm assertion. If there are no holes, the transformation is the
identity. If Λ=∅ its output is zero; if Γ is nonempty the component-size
hypothesis merely says |Γ|≤M in that endpoint case.

This bound concerns the part meeting Λ. For the **entire** expression
(L4), retain inactive activities with their original supports. Their
full norm is at most ||B||_μ≤||B||_{c_M μ}. Keeping both labelled families
therefore costs at most (1+9M)||B||_{c_M μ}; none of them is dropped.

### 5.3 Source differences and derivatives

The map B↦B' is linear and depends only on fixed graph/mask data. Thus

    (B(ε)−B(0))'=B'(ε)−B'(0),
    ∂_ε^α B'_Y=Σ_{X:R_Λ(X)=Y} ∂_ε^α B_X.               (L15)

The first family vanishes at zero source, and its input supremum and
rooted norm cost at most twice the original ones. Its argument support
does not shrink when the source is set to zero and then subtracted.

For completeness, let r>r'≥0 be radii of common concentric source
polydiscs and α any finite multi-index. For each derivative coordinate,
integrate on a circle of radius δ<r−r' about the evaluation point.
Repeated one-variable Cauchy integral formulas give a factor α!δ^(−|α|)
times the outer supremum. Letting δ↑r−r' gives

    ||∂^α B'_Y||_{r'}≤α! (r−r')^(−|α|)||B'_Y||_r.       (L16)

The same estimate holds after each of the rooted sums in (L12)–(L14).
A derivative involving a source outside Y vanishes, because the function
is independent of that coordinate. Thus this is an all-order consequence
of the proved holomorphic local function, not an inference from a finite
set of derivative tests. When r=0, (L3)–(L14) remain value statements;
no positive derivative radius is inferred. ∎

## 6. Exact specialization to the current soft-kernel producer

**PROVEN as an implication from the displayed H24 hypothesis.** Fix the
real sea sample/coarse field variables and a failure collection F in
`SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md`. The following is a mathematical
application of its *stated bound*, not an independent re-proof of H18–H25
or a new review verdict on that candidate.

The producer's hypothesis, word for word at H24, is

```text
sup_x sum_(X contains x) exp(mu|X|)
     sup_(real U,V; D_(rho,lambda)(u)) |V_X^F| <= d_q.
```

Its source domain, word for word at H20c, is

```text
D_(rho,lambda)(u)={epsilon: |epsilon_p|<=rho+lambda/u},
```

Its support contract is: “Every original coefficient and every actual
sea/coarse field read occurs in X, before and after summing histories at
FIXED F.” Its source convention is: “only the bare Wilson coefficient
changes, and the prescribed RG kernel K remains fixed.” These are the
hypotheses used here, without replacing the source by a single common
coupling or the real-field supremum by a small-background supremum.

Take Ω=Γ and B_X=V_X^F. Since X is face-connected, X∈P_Γ automatically.
For any fixed Λ⊆Γ, define

    V'^F_Y=Σ_{X:R_Λ(X)=Y, X∩Λ≠∅} V_X^F,
    V^F_inactive=Σ_{X:X∩Λ=∅} V_X^F.                       (L17)

Then (L3)–(L5) hold with the **same** K, ε, U,V and fixed F, and

    sup_{v∈Λ} Σ_{Y∋v} exp(μ|Y∩Λ|)
           sup_{real U,V; D_(ρ,λ)(u)} |V'^F_Y| ≤ d_q.     (L18)

The corresponding bound for V'^F_Y(ε)−V'^F_Y(0) is 2d_q. This statement
is uniform over arbitrary fixed holes whenever the H24 input is uniform.
It preserves the complete source dependence in Y; it counts only active
blocks in the displayed weight. No uniformity in RG depth follows unless
H24 itself is supplied at every level for the actual level-dependent action.

There is also a direct input for the graph-tree version. A connected X has
a spanning tree with |X|−1 edges (remove cycle edges from a connected
subgraph until none remain). No tree containing all |X| distinct vertices
has fewer than |X|−1 edges. Thus t(X)=|X|−1, and H24 implies termwise

    ||V_X^F||∞≤d_q exp(−μ|X|)
               ≤d_q exp(−μ d_Γ(X)).                     (L19)

If the chosen producer rate satisfies μ>a, (L11) gives the output decay
rate μ−a and prefactor C(a)d_q. This is a conditional choice of rate: the
producer's H21/H21a smallness threshold changes when μ changes. Neither a
large μ nor its coupling threshold is assumed free of cost.

For a **full H24-shaped output**, set ν=(1+8M)μ and assume H24 at ν with
bound d_q(ν). The dependence is explicit in the producer:

    r_q(ν)=q exp((ν+1)·81),
    d_q(ν)=81 r_q(ν)/(1−624² r_q(ν)),
    624² r_q(ν)<1,                 d_q(ν)≤1/4.           (L20)

If every inactive component has size at most M, (L14) gives

    sup_{v∈Γ} Σ_{Y∋v} exp(μ|Y|)
           sup_{real U,V; D_(ρ,λ)(u)} |V'^F_Y|
               ≤9M d_q(ν).                              (L21)

Its source difference costs 18M d_q(ν). If a subsequent consumer needs
the right side ≤1/4 or another budget, that is a further explicit
inequality to check. In particular (L20)'s 1/4 by itself does not imply
9M d_q(ν)≤1/4. The same source radius can be used; the required u threshold
may increase. No uniform M is supplied for unrestricted actual histories.

For the already constructed gas, H25's exact identity becomes

    G_ret,F^ε=exp(V^F_inactive(ε)+Σ_Y V'^F_Y(ε)).          (L22)

If H25 holds, this equality preserves its chosen exponential/logarithm
representation; it makes no new logarithm branch choice. In particular it
retains the interior reference and original sea/coarse variables. A
subsequent expectation under ν_cut^0, or summation with failure weights,
is a new operation. Neither its locality nor its zero-free domain follows
from reindexing (L22).

## 7. A norm-bookkeeping witness on our lattice

**PROVEN — exact scope example.** Let Γ=(Z/TZ)⁴ with T≥3, choose a
block v, and put Λ={v}, Ω=Γ. The graph Γ\{v} is connected. To see this
without invoking a topological assertion, put v=0. From any x≠0 choose
a coordinate i with x_i≠0. Keep that coordinate fixed while setting some
other coordinate j to 1. Keep j=1 while setting every other coordinate
to 1. Throughout this path at least one coordinate is nonzero, and the
path ends at (1,1,1,1). Reversing paths connects any two vertices of the
complement.

Choose an actual fine plaquette p entirely inside block v (L≥3 supplies
one), radius r>0 and b>0. Set B_{ {v} }=b ε_p/r and all other activities
to zero. This is a permitted original-source local test activity; it is
**not asserted to be an actual V_X^F**. On the source polydisc of radius r,
its supremum is b. The one inactive component H=Γ\{v} is adjacent to v,
so R_Λ({v})=Γ. For μ>0 the exact norms are

    ||B||_μ=b exp(μ),
    ||B'||_{μ;Λ,act}=b exp(μ),
    ||B'||_μ=b exp(μ|Γ|).                                (L23)

Thus the full/initial ratio is exp(μ(|Γ|−1)), while the active norm is
unchanged. This identifies the price of this particular support-saturation
map. It does not refute a hole-aware representation, a different support
label, additional suppression from actual history weights, or the actual
Yang–Mills return. At μ=0 this example has ratio 1 and asserts nothing
stronger. Keeping the original source support as an additional label is
also an available bookkeeping choice, but is not a proof that a consumer
requiring the single full support Y has the H24 bound.

## 8. Consumers and exact discharge boundary

The quotations below are literal fragments of the named local sources
(line wrapping normalized in the receipt). A discharged library interface
and a discharged full consumer are different claims.

| Consumer and exact quote | What LIB1 discharges or narrows | Remaining status |
|---|---|---|
| `SOFTHARD.md:349`, R10: “Enlarging the inactive region regroups boundary activities while preserving their sum and controlling a decay loss.” | **PROVEN:** that finite-graph operation, including its own counting prerequisite, original-source locality, and explicit native norm interface. | **OPEN:** an application using another distance must supply its conversion; the gauge R-operation is not constructed here. |
| `HANDOFF.md:420–421`, step 2: “Include holes, reference comparison and failed-return bookkeeping before claiming the history-uniform large-field step.” | **PROVEN:** the exact nested-hole sum and retained inactive term, with uniform active-root/tree bounds. This narrows the hole/reference bookkeeping subproblem. | **OPEN:** actual reference/sea integration, failure prices and the full returned denominator. |
| `HANDOFF.md:426–428`, step 4: “Construct N1's complete normalised, strictly source-local density representation, uniformly over all coarse fields, and N2.” | **PROVEN:** preservation of original-source locality and the same source domain under this fixed-mask reindexing; (L18) uses the literal H24 field supremum. | **OPEN:** the complete normalized density after sea integration, all histories/levels, and N2. |
| `CODEX_REVIEW_ASSEMBLY.md:229`, item 11: “Close the coupled flow/large-field construction.” | **PROVEN:** one reusable algebraic ingredient for its normalized reconstruction term; no flow estimate is consumed or produced by LIB1. | **OPEN:** the coupled induction and all its quantitative inputs. |
| `CODEX_REVIEW_ASSEMBLY.md:231`, item 13: “Match the coefficient norm and the actual source radii.” | **PROVEN:** (L18) and (L21) spell out the two output norms, radius preservation, stronger input rate, hole size and smallness cost. They prevent treating the active norm as the full consumer norm. | **OPEN:** a full-norm estimate at unrestricted hole size, or a separately proved compatible hole-aware consumer. |
| `STEP55.md:583`: “boundary polymers READ cone variables, so COL's exact integration must be redone with those polymers expanded” | **PROVEN:** the regrouped activities keep those arguments; none is removed in (L4)–(L5). | **OPEN:** the named integration argument. Local reindexing alone does not perform it. |

The approach registry's “Source-local resolvent and return” row has the
same boundary: original-source incidences and the full-factor return
remain the target. The branch's fixed-sector/hard-history candidates are
useful predecessors, not assumptions that every required source/sea
estimate has been established. Decision 4 remains the finite soft kernel.

**ARGUED — route value.** This lemma is common to both blocking choices
because it reindexes already supplied coefficient functions on blocks;
it does not use Gaussian softness, an abelian gauge field, or a hard
constraint. A hard-route application must supply its own actual activities,
source domain and bounds, including its constraint and gauge factors. The
identity does not justify taking κ→∞ in any current soft estimate.

## 9. Literature credit and rebuild accounting

Credit for the resummation method belongs to **Jonathan Dimock**, in his
exposition of **Tadeusz Balaban**'s program:

- [The Renormalization Group According to Balaban — III. Convergence](https://arxiv.org/abs/1304.0705),
  arXiv:1304.0705v1, Appendix B, Lemma 19, page 35, (238)–(245).
- [The Renormalization Group According to Balaban — II. Large fields](https://arxiv.org/abs/1212.5562),
  arXiv:1212.5562v2, Appendix E, pages 88–91, especially Lemma E.3,
  (627)–(632). The paper also credits Gawędzki and Kupiainen for related
  disconnected-polymer sums on page 89; their original papers are not
  invoked here.

The open PDFs were actually read at these arguments. Page 35 of III and
page 90 of II were rendered and visually inspected to check subscripts,
sets and summation domains. Their local source files and hashes are in
`checks/lib1_source_manifest.json`; the renders are
`checks/lib1_dimock_III_p35.png` and `checks/lib1_dimock_II_p90.png`.
The supplied read-only Dimock QED multiscale PDF was also opened for the
candidate comparison; its abelian d=3 scope is not used as a 4D estimate.

The inspected scalar source supplies the **strategy**, not a premise:
group by enlarged support, compare the active trees, and pay the number
of old supports. Section 3 replaces the cited counting chain by an explicit
finite graph walk encoding. Sections 2 and 4 prove the new set operation
and all constants; section 5 proves the source-norm interface. In the new
calculation every sum remains over the old family P_Ω until its fibre
has been formed. No printed shorthand in the source is used to exchange
P_Ω with P_Λ. The elementary tree and geometric-series facts used in the
estimate were proved above. There is no memory-only `[m]` mathematical
dependency and no imported Balaban/Dimock estimate in the proof.

Nonduplication is deliberately scoped. SF's CE⁺/HULL and CE-col/CE-exp-col
fill bounded collars or source connectors. RECOVERY_CLUSTER constructs a
connected logarithm in a full rooted norm. H26–H27 cancel common cluster
coefficients across a **fixed** exclusion/boundary. They are related
tools, but do not state this arbitrary nested inactive-component saturation
with its explicit full-versus-active norm comparison. The saved folder
search and the relevant source reads support this selection. They do not
certify that no other uninspected branch contains a similar theorem.

## 10. Author checks and limitations of those checks

The mathematical proof is §§2–5; the finite program is a regression check.
The pre-stated criteria are `checks/lib1_criteria.md`. The program
`checks/lib1_check.py` uses exact integers and rational numbers only.
It compares component filling with iterative inactive-vertex growth and
computes tree lengths by minimizing over all connected vertex supersets,
which is different from the proof's walk-count majorant.

The recorded run completed with:

- all 729 nested pairs Λ⊆Ω on each of the path6, cycle6 and 2×3 box;
- 36,873 support instances checking closure, active-set equality, tree
  monotonicity and original-source retention; 2,187 exact polynomial
  identities including the inactive remainder;
- 576 rooted-count and 8,972 decay comparisons, plus the active and
  bounded-hole full-norm inequalities;
- 6,288 support instances on the 2×2×2×2 block torus, across 137 active
  sets; periodic duplicate neighbours correctly reduce its degree to 4;

[R-fix 2026-10-29 B1] The original v1 coverage statement is retained
verbatim below. Its interpretation as evidence that the full-output norm
implementation rejects active-for-full substitution is withdrawn: the v1
control compared separate powers of two, without testing that computation.

> - four explicit wrong outputs distinguished: dropping the inactive term,
>   deleting an inactive source, ignoring adjacent inactive components,
>   and identifying the active and full norms.

Maximum recorded RSS was 22,167,552 bytes. Across 15 resource samples,
system-wide free memory was at least 60% and the largest load average was
2.36767578125. The run used nice 10 and all five thread variables set to
1; it completed in 0.457925125 seconds with empty stderr. The runner checks
its own 2 GB RSS, 50% free-memory and load<20 gates before enumeration,
periodically, and at completion. It creates no worker pools.

Receipts: `checks/lib1_check_result.json`, `checks/lib1_check_stdout.txt`
and `checks/lib1_check_stderr.txt`. These counts establish only the
enumerated predicates. They supply neither an independent review nor
experimental evidence for a cutoff limit or a physical gap.

### [R-fix 2026-10-29 B1] Computation-linked full-norm control

**B1 author repair: implemented and checked.** The updated acceptance
criteria, `checks/lib1_criteria_v2.md`, were written before
`checks/lib1_check_v2.py`. The frozen v1 criteria, scripts and outputs are
unchanged. The v2 bounded-hole inequality and both new exact witnesses call
the same `full_output_norm` function. Expected values are derived directly
from the explicit supports, before the new implementation and run:

- On the four-cycle with Λ={0} and one unit input at {0}, saturation gives
  all four vertices. The input full norm is 2¹=2, every full output root
  sum is 2⁴=16, and the active output norm is 2¹=2. The computed values
  were **2, 16, 2**, respectively.
- On the path 0–1–2 with Λ={0,2}, unit inputs at {0} and {2} saturate to
  {0,1} and {1,2}. The full rooted sums are (4,8,4), with the unique maximum
  at inactive vertex 1. The computed input full, output full and output
  active norms were **2, 8, 2**. Restricting the full-norm roots to Λ would
  incorrectly give 4.

One sequential invocation ran the baseline once and each of two actual
in-memory source mutants once. Each mutant changed only the shared
function's return expression; the inequalities, witnesses, asserted
constants and resource guards were unchanged. Each trial completed all
2,184 bounded-hole comparisons before reaching the witnesses.

| Trial | Observed outcome | Separate receipt under `checks/` |
|---|---|---|
| Corrected baseline | All finite predicates and both exact norm witnesses passed. | `lib1_check_v2_baseline_result.json` |
| Active norm substituted for full norm | `AssertionError: four_cycle_full_output_norm_exact`; computed 2, expected 16. | `lib1_check_v2_active_for_full_result.json` |
| Full weights with inactive roots omitted | `AssertionError: overlap_full_output_norm_exact`; computed 4, expected 8. | `lib1_check_v2_inactive_roots_result.json` |

These are actual rejection outcomes for those two substitutions. The
three inherited static wrong-output contrasts are labelled as such in v2;
they are not claimed as additional implementation-mutation executions in
this repair. The baseline retains the original finite enumeration counts.
The exact mutation lines and distinct compiled-source hashes are in the
receipts; the combined receipt is `checks/lib1_check_v2_result.json`, with
matching `checks/lib1_check_v2_stdout.txt` and empty
`checks/lib1_check_v2_stderr.txt`.

Across 51 resource observations, maximum RSS was 26,656,768 bytes, minimum
system-wide free memory was 60%, and the maximum load average was
2.30078125. The invocation used `nice -n 10` (observed niceness 20), Python
`-B`, all five thread variables set to 1, and no pools. The suite took
1.3022756249993108 seconds and exited 0. Resource guards also ran after
each expected assertion failure. No sandbox/resource step was blocked.

**OPEN (review disposition):** the original reviewer has not confirmed
this B1 repair; the author does not replace the recorded HOLD or claim
LAND. No B1 implementation obligation remains unperformed in this author
pass. These are same-author finite regression checks, not an independent
review. The immutable PRE-STATED prefix, theorem, hypotheses and analytic
residues in §12 are unchanged.

## 11. No-Go Discipline Gate — scope only, no exhausted-route claim

The repository's no-go-discipline skill was consulted because a norm
limitation appears inside a positive lemma. Its landing/ledger workflow
does not apply to this author-only brief; the user expressly forbids those
writes and commits. **OPEN** is the state of any would-be negative-claim
packet: no packet success or route-exhaustion verdict is asserted.

- **N1, alternatives.** The actual operation was tested, including the
  singleton example. A bounded-hole, stronger-input-norm route is proved
  in §5.2. Keeping original supports as extra labels, changing the downstream
  hole-aware algebra, and obtaining suppression from actual failure/sea
  weights are unclosed alternatives, not routes ruled out by this example.
  This task does not supply five exhausted families; no such count is claimed.
- **N2, dependence.** No independence or number of physical barriers is
  asserted. A new sea/failure construction could supply several missing
  estimates together. Implications between that construction, a new norm
  convention and a uniform geometric price have not been determined here.
- **N3, hidden premises.** Fixed masks, complete original reading supports,
  μ≥0, exact source domain, the supplied activity bound, κ_B>a, and M for
  (L21) are explicit. The word “background” labels neither a new primitive
  nor an assumed uniform estimate. The source supremum is not replaced.
- **N4, residual match.** The example addresses only full-support norm
  growth under R_Λ. The quoted COL and sea residuals concern integration;
  they are not offered as evidence that all alternative integrations fail.
- **N5, resolution.** (L23) is a single-activity example on a family of finite
  4D block tori. The finite program also checks graph/support identities.
  No per-mode, continuum, gauge-theory or physical-spectrum failure follows.
- **N6, partial closure.** Original-support labels or a compatible active
  norm can change the bookkeeping question without adding an axiom. The
  bounded-hole full-norm implication is already a positive partial route.
- **N7, strongest counter-route.** A successful construction can retain the
  old fine-source labels while using enlarged sets solely for geometric
  organization, then estimate the inactive-region expectation before
  imposing the final full norm. H23's original-source locality and the
  corrected CX-R norm provide starting data. Its missing step is the
  actual sea/failure estimate; (L23) says nothing against that mechanism.
- **N8, related work.** SF's collar/HULL bounds and the later CE-col
  reformulation show that regrouping conventions change apparent costs.
  H26–H27 retain a boundary factor without claiming its sea integration.
  These were checked as related mechanisms, not counted as repeated
  evidence of a global obstruction.

## 12. Open residue and next concrete use

**OPEN:** supply actual boundary activities, or a source-local description
of the inactive expectation, on the full history family. For those inputs,
use (L3)–(L4) to move the active region without losing source arguments or
inactive factors. If the next consumer requires a full H24 norm, establish
its budget through (L21) with uniform M and stronger input rate, or prove
a different compatible representation/estimate. Neither is assumed for
arbitrary holes. Reference comparison, failed-return suppression,
normalization after the sea expectation, higher-level actions and
induction remain the named analytic work. HANDOFF steps 1, 3 and 5 are
not discharged; existence and the physical mass gap remain open.

The delivered library unit is the single R10 resummation lemma and its
necessary counting/norm clauses. It introduces no physical axiom, changes
no owner decision, and edits no consumer, audit file or ledger.
