# Recovery of the one-step cluster implication

## Pre-check contract — 2026-10-29 10:48 UTC

Completed author proposal; no audit status. Frozen at 2026-10-29 11:13:54 UTC. Model provenance: the coordinator
reports an explicit tool dispatch of `gpt-6-astra`, reasoning effort `max`,
with `fork_turns=none`, to `/root/cluster_repair`. This worker does not have a
separate runtime identity attestation. Vendor family: OpenAI. Same-family
checks are not an independent referee.

Assigned snapshot: `46dc04b05c5842a03ae3af64caa77628f099128f`, supplied by the
coordinator, not independently verified by git (git is outside this task).
All paths below are relative to this existing `ym4d-proof` pack. Only this
file and `checks/recovery_cluster_*` may be written. No axiom, audit verdict,
commit, PR, publication, merge, or unattended run is part of this block.

This contract is written after the source reads and exploratory route
selection, but before executing any new check or writing the new proof.
Prior exposure: the late reviews' counterexamples and their conclusions are
known; reproducing those examples will not be called a new discovery.

**Exact target.** Produce a correctly quantified, constructive sufficient
one-step theorem for a finite region of a bounded-degree lattice, with
constants uniform over any family satisfying its explicit hypotheses. Its
logarithmic activities must be local in both the integrated variables and
the original external source/background coordinates. It must account for the
full main term, Gaussian determinant, cutoff normalization, linear term,
Jacobians, and history dependence needed by the *actual* denominator. Then
compare its hypotheses with the available Yang–Mills premises.

**Allowed inputs.** Product reference measure; genuinely local analytic bare
vertices; a separately stated connected-support expansion of the linear
fluctuation map/operator, if constructed or quantitatively bounded below;
elementary convergent-series and graph arguments. No positivity-to-locality
inference, no finite-order derivative-to-all-order locality inference, no
replacement of original coefficient fields by secretly global backgrounds,
and no identification of a single kernel normalizer with a return integral.

**Completion witness.** A proved implication with non-circular small input
conditions, explicit constants or computable majorants, a finite direct
check using a different calculation, and a source-to-hypothesis ledger.
An unproved Yang–Mills instantiation does not count as closure of the RG step
or N1. Finite checks do not prove cutoff/scale/volume uniformity.

**Pre-stated controls.**

1. A local small-interaction example: compute its exact finite partition
   polynomial by direct product-measure summation and independently by
   connected-support grouping. Their coefficients must agree; changing an
   interaction sign must be detected.
2. A remote-parameter example with identity covariance must retain the remote
   source in its support. Any claimed local representation that omits it
   fails the mixed-coefficient check. This reproduces R9/F7, rather than
   asserting a counterexample to the full Yang–Mills package.
3. At zero nonlinear interaction, a varying Gaussian determinant must still
   give a nonconstant full logarithm. Dropping that term is a failing control;
   it may not be repaired by assigning it to the nonlinear smallness budget.
4. A non-nearest-neighbor operator entry must carry its entire connector in
   the support accounting. Counting only its two endpoints is a failing
   control for the geometric bound.

**Routes.** (A) Explicit connected-support algebra, analytic composition,
and a product-measure cluster theorem: active constructive route. (B)
Telescoping truncations on metric balls: not used without a summable bound
in support size, since an exponential-in-radius tail in four dimensions
does not pay an exponential-in-ball-volume weight. (C) Existing countermodels
to the old implication: diagnostics only; no impossibility statement about
all alternative Yang–Mills constructions.

**Source reads completed.** `AGENTS.md`,
`docs/ai_methodology/SCIENCE_WORKFLOW.md`; all of `CODEX_REVIEW_STEP.md`;
STEP55 §5.1–5.4 and S8/S9; `CODEX_REVIEW_SRC2.md` F1/F2/F7;
`CODEX_REVIEW_B2.md` R7/R8; necessary BFT34 §2.1–2.3 and LINEAR_PACKAGE §5
statement/qualification. Methodology: physics-loop, its claim/discovery/
delivery references, proof-search governance, exercise and no-go discipline
were inspected. The assigned frozen worktree and bounded author task take
precedence over campaign, git-refresh, fanout, and landing procedures. No
claim about the framework's primitive registry is being made.

## Results

The proposed replacement is a **generic conditional theorem**, proved below.
Its Yang–Mills instantiation remains open. It constructs the interaction
localization and the determinant from smaller data; it does not assume a
local expansion of the final integrated density. Its matrix smallness
condition is sufficient, not necessary, and is stronger than the currently
verified Yang–Mills operator information.

### 1. Support must mean support in the original variables

Let G be any finite graph with vertex set Γ. A nonempty connected vertex set
S is an allowed support. At each vertex there are q fluctuation coordinates
W_x and finitely many external coordinates z_x. A function labeled S must
depend only on W_S and the **original** z_S. A holomorphic global spectator
parameter, such as one common coupling, is allowed; it is not counted as a
spatial coordinate. Substituting a background b(z) preserves a support label
only if the resulting original-z dependence is included in that label.

Use a fixed product probability measure μ = ⊗_x μ_x on W, with
|W_x|_∞ ≤ p. A fixed collar is allowed by taking some μ_x to be point masses.
All complex z vary in a product domain D; every supremum below is uniform on
D and on supp μ, and the relevant functions are holomorphic on an open
neighborhood of D (or the bounds hold on all compact subdomains). Fix
**β≥0** for the support norms and operator lemma below. Define

    ||U||_β := sup_v Σ_{S∋v} e^{β|S|} ||U_S||_∞.

This norm already sums support entropy; no counting constant or rate is
silently spent afterward. All constants in the results below are uniform
over a family of graphs/regions/holes **only when these input norms and the
stated local combinatorial parameters are uniform on that same family**.

### 2. Constructive operator lemma: every jump carries a connector

Let K(z)=I−E(z), with q×q matrix blocks indexed by Γ (or by the integrated
vertices), and suppose a supplied decomposition is available:

    E_xy(z) = Σ_{S connected, x,y∈S} E_xy;S(z_S).

The block norm is the induced infinity norm. Put

    r = max{ sup_x Σ_{y,S} e^{β|S|} ||E_xy;S||,
             sup_y Σ_{x,S} e^{β|S|} ||E_xy;S|| } < 1,
    b = sup_v Σ_{x,y,S∋v} e^{β|S|} ||E_xy;S|| < ∞.

No assumption about locality of the *inverse* occurs here. These are
entrywise conditions on the original operator and its original-z
dependence. For a nearest-neighbor matrix whose entries depend only on
their endpoints, one may use S={x,y}; then b≤2r. A long jump x→y needs a
connected S containing both endpoints, with its actual weight e^{β|S|}.
An arbitrary pair of endpoints cannot be charged as two adjacent boxes.

**Lemma O.** The series

    C=K^(−1/2)=I+Σ_{n≥1} c_n E^n,
    c_n=binom(2n,n)/4^n,

converges absolutely and gives a connected-support expansion. Its weighted
row and column sums are at most

    M = e^β + (1−r)^(−1/2) − 1.

The sum of all its matrix terms whose support contains any fixed vertex
is at most

    B_C = e^β + (b/2)(1−r)^(−3/2).

The analytic branch

    −(1/2) log det K = (1/2) Σ_{n≥1} Tr(E^n)/n

has connected-support activities D_S(z_S) satisfying

    ||D||_β ≤ q b/[2(1−r)].                         (O-det)

**Proof.** Expand each product E_x0x1⋯E_x(n−1)xn into its given support
atoms. Consecutive supports share the intermediate vertex; their union is
connected, contains the endpoints, and contains every parameter read.
The weight of the union is no larger than the product of the weights. Row
and column sums of n-step terms are therefore at most r^n. For a fixed
vertex v in a union, mark one step whose support contains v. Summing the
prefix by its column bound and the suffix by its row bound bounds the sum
by n b r^(n−1). This is an overcount, not an equality. The identity term is
supported at one vertex and costs e^β. Summing the binomial series and its
derivative gives M and B_C. Closed walks give Tr(E^n); their sum is a
subsum of the marked walks, and |tr A|≤q||A||. The factor n from marking
cancels 1/n, giving (O-det). Absolute convergence also proves holomorphy.
The logarithm is the branch connected to K=I along I−tE, |t|≤1. All those
matrices are invertible by the unweighted row bound <1, so no zero-free
conclusion was used to construct the logarithm. ∎

When K is complex symmetric and is real symmetric on real data, C is
symmetric and C^T K C=I; the real matrix is positive since ||E||<1. This
supplies the Gaussian change of variables in this sufficient regime.
Without the symmetry condition the support statements remain true, but
that change-of-variables interpretation is not asserted.

### 3. Analytic composition localizes the interaction, including sources

Set A=σ C W, where σ is a global holomorphic spectator and |σ|≤σ_*.
Lemma O supplies an expansion of each A_x into connected-support functions
containing x, with weighted row bound A_* and support-incidence bound B_*:

    A_* = σ_* p M,          B_* = σ_* p B_C.

Suppose the bare interaction is Σ_x V_x(A|_{B_x}; z|_{B_x}), where B_x is
connected, contains x, has at most s vertices, and each vertex belongs to
at most d_B of the sets B_x. Each V_x is holomorphic for all q|B_x|
individual fluctuation coordinates of modulus <a, and has supremum ≤H on
that polydisc and D. Assume A_*<a; write Q=q s. Then substitution constructs
an exact expansion

    V(σCW;z)=Σ_{S connected} U_S(W_S,z_S)

with the explicit sufficient bound

    ||U||_β ≤ h_loc
      := d_B e^{βs} H [ (1−A_*/a)^(−Q)
             + (Q B_*/a)(1−A_*/a)^(−Q−1) ].        (C)

Any already supplied connected-support interaction of norm h_inh may be
added, giving h=h_loc+h_inh. Such an inherited interaction must itself be
local in the original z; a label carried over from before a global
background substitution is insufficient.

**Proof.** Taylor-expand V_x in its individual A coordinates at zero.
Cauchy bounds give the absolute coefficient majorant

    F(t)=H(1−t/a)^(−Q).

Expand every A factor using Lemma O, and label the resulting term by B_x
union all the attached walk supports. Each walk starts in B_x, so this
union is connected, and includes every W and z read by the term. For a
fixed v in the union, either v∈B_x or v belongs to at least one attached
walk. The first possibility costs at most d_B e^{βs}F(A_*). Marking one
factor in the second costs at most d_B e^{βs} B_* F'(A_*): for any marked
starting vertex y there are at most d_B possible B_x containing y, and
the sum over all starting vertices of walk terms containing v is B_*.
This proves (C) and absolute convergence of the regrouping. ∎

For q>1 the Taylor expansion uses scalar coordinate multi-indices, with
at most Q=q s coordinates. In the marked-factor bound all terms with a
given starting block y are summed over their coordinate choices before
using the block infinity bound B_*. Their coefficient sum is a subsum of
F'; no additional uncounted q appears. Q and F' already pay those choices.

This is an all-order analytic construction. Low-order derivative locality
by itself is not being promoted to a support expansion; BFT34 §2.2 already
provides a counterexample to that separate promotion.

### 4. Product-measure cluster theorem with explicit rooted norms

**Theorem CX-R.** In §1's setting choose μ_0≥0 and β=μ_0+2. If the localized
interaction U constructed above, or any independently supplied interaction
with the same support meaning, satisfies

    h=||U||_β ≤ 1/4,

then

    Z_red(z)=∫ exp(−Σ_S U_S(W_S,z_S)) dμ(W)
            = exp(Σ_{Y connected} F_Y(z_Y)),
    sup_v Σ_{Y∋v} e^{μ_0|Y|} ||F_Y|| ≤ 2h.        (CX-R)

All F_Y are holomorphic. The representation, its convergence, and
zero-freeness hold throughout D, uniformly over the explicit input family.
If μ_0>0, the norm supplies exponential support-size decay. On a lattice
with unit adjacent steps this also pays the length of an actual spanning
tree of each support, including any filled long-jump connector. Empty Γ
gives Z_red=1 and the empty exponent. Disconnected Γ factorizes.

**Proof, first stage (local interactions to a hard-core gas).** Put
f_S=e^(−U_S)−1. Since ||U_S||≤h, |f_S|≤e^h|U_S|≤2|U_S|. Therefore

    q_* := sup_v Σ_{S∋v} e^{(μ_0+2)|S|} ||f_S|| ≤ 2h ≤ 1/2.

Expand ∏_S(1+f_S). A selected finite collection of supports splits uniquely
into components of its overlap graph. Different components use disjoint
W sets, so their integrals factor. If w(P) sums the integrals of all
nonempty connected collections with union P, this is exactly the gas
partition sum over mutually disjoint connected P.

Here is the quantitative bound without an entropy assertion. Set
v(S)=||f_S||e^{(μ_0+1)|S|}. A connected collection with a designated root
support is bounded by the sum over its spanning trees. Allowing repeated
supports can only enlarge this nonnegative sum. Its rooted tree generating
function is dominated by successive iterations of

    T(S)=v(S) exp(Σ_{S': S'∩S≠∅} T(S')).

Starting at zero, all iterations satisfy T(S)≤v(S)e^{|S|}, since the sum
in the exponent is bounded by |S|q_*≤|S|. (The exponential factorials
count unordered children; equivalently use labeled trees with the usual
1/(n−1)!.) A polymer P containing v has some root support containing v.
The union weight is at most the product of support weights, hence

    sup_v Σ_{P∋v} |w(P)|e^{(μ_0+1)|P|} ≤ q_*.    (G)

**Second stage (logarithm of the gas).** For polymers P_1,…,P_n let φ^T be
the sum of (−1)^(number of edges) over connected spanning subgraphs of
their overlap graph. For n=1 set φ^T=1. The elementary tree inequality is

    |φ^T| ≤ Σ_{trees τ} ∏_{ij∈τ} 1_{P_i∩P_j≠∅}.

One proof orders the edges of the overlap graph distinctly and groups
each connected subgraph by its unique Kruskal minimum spanning tree τ.
For a fixed τ the allowed extra edges are precisely those whose order is
larger than every edge on their τ path. The subgraphs form an interval
[τ,R(τ)]; their signed sum is (−1)^(n−1)(1−1)^(|R(τ)−τ|), of magnitude
at most one. These intervals partition the connected subgraphs.

Replace each |w(P)| by |w(P)|e^{μ_0|P|}. By (G), the same rooted-tree
iteration bounds its cluster sum with distinguished P by e^{|P|}.
Define F_Y by summing

    (1/n!) φ^T(P_1,…,P_n) ∏_i w(P_i)

over ordered tuples with union Y. The overlap condition makes Y connected.
To bound all Y containing v, mark a polymer containing v. The at most n
choices cancel the n in n!, and (G) bounds the resulting rooted sum by
q_*≤2h. This proves the displayed norm and absolute local uniform
convergence. All input parameter dependence lies in Y.

Finally replace U by tU. The same bounds hold for |t|≤1, with a strict
margin allowing a slightly larger disk. Near t=0 the exponential identity
follows by the finite formal connected-graph identity (or its absolutely
convergent Taylor series). Analytic continuation in t reaches t=1 on the
same domain. Thus Z_red=exp(ΣF_Y) is proved before zero-freeness is
concluded. Holomorphy in z follows from the uniform bounds. ∎

The two connected-graph stages do different jobs: the first uses independence
of disjoint W sets; the second takes the logarithm of the resulting
hard-core gas. This proof neither requires nor asserts pointwise
independence of globally transformed Gaussian fields.

**Adjustable rate/size variant.** The fixed extra weight 2 is convenient,
not necessary. For any a_c>0 the same proof works with β=μ_0+2a_c and
h≤min(1/4,a_c/2). Replace the intermediate weight μ_0+1 by μ_0+a_c and
the rooted-tree majorant e^{|S|} by e^{a_c|S|}. Then q_*≤a_c supplies both
tree iterations, and the output bound is still 2h. This makes the
sufficient regime meaningful even when a normalized operator is close to
the edge of its unweighted Neumann convergence domain.

For example, for any m^2>0 and any finite graph of maximum degree Δ>0,
take the scalar massive graph Laplacian K=m^2I+L_G and c=m^2+Δ. Write
K=c(I−E), with

    E_xx=(Δ−deg(x))/c,       E_xy=1/c for adjacent x,y.

Diagonal supports are {x}; edge supports are {x,y}. Both row and column
weighted norms obey r≤Δe^{2β}/c, and the incidence norm obeys b≤2Δe^{2β}/c.
Thus any 0<β<(1/2)log(1+m^2/Δ) gives r<1. Choose μ_0=β/2, a_c=β/4,
then a sufficiently small fluctuation scale and interaction satisfy (C)
and h≤min(1/4,β/8). The factor c contributes only the local constant
−(|Γ|/2)log c to −(1/2)logdetK and changes C by c^(−1/2).
The case Δ=0 is purely diagonal. This works for every positive fixed mass,
but its constants deteriorate as m→0; no massless or Yang–Mills conclusion
is asserted. The operator here has fixed coefficients; adding local
coefficient dependence requires checking the same support norm on its
complex domain rather than appealing to real positivity alone.

### 5. The full denominator and its actual normalization

Suppose an **independently established exact change-of-variables identity**
for the intended denominator is

    Den_Γ(z) = P_Γ(z) exp(−S_0(z)) det K(z)^(−1/2)
               × N_χ,Γ(z) × Z_red(z).             (ID)

All Jacobian, gauge-fixing and inherited terms must occur exactly once in
P, S_0, K, N_χ, or U. In particular a nonzero linear fluctuation term must
be included in U or shifted by a justified change of variables; subtracting
it in the definition of a remainder does not erase it from (ID). The
critical point must be for the exact action if it is used to erase that
term. The cutoff is the same fixed white-noise product cutoff as in μ.
Any altered contour, history indicator, or boundary conditioning is part of
the identity to be proved, not a convention implicit in CX-R.

In a gauge theory this includes the map from slice coordinates to the
vertex-labeled fluctuation coordinates. A product measure in a nonlocal
slice basis is not automatically the product measure with local coordinate
support required by §1. Its map and Jacobian must satisfy the same stated
support accounting. Complex Gaussian identities use transpose/bilinear
forms, not conjugate-transpose Hermitian forms at complex z.

Assume P and N_χ have specified nonvanishing holomorphic logarithms and
connected original-z-local decompositions with norms p_0 and c_0 at
weight μ_0, and S_0 has such a decomposition with norm s_0. For a fixed
product cutoff, log N_χ is simply a sum of one-site constants. Applying
CX-R and Lemma O gives

    log Den_Γ = log P_Γ − S_0 − (1/2)log det K
                  + log N_χ,Γ + Σ_Y F_Y,
    rooted norm ≤ p_0+s_0+c_0+q b/[2(1−r)]+2h.   (FULL)

Here the first three input norms need not be small. Their local expansions
can sometimes be constructed by §3's composition argument applied to the
actual background map; this has to be demonstrated in original source
coordinates. If they are not localized, (ID) still yields zero-freeness
when its scalar factors are nonzero, but it does **not** give the full
source-local conclusion (FULL).

For any two points z,z' in the same chosen logarithm domain,

    Δlog Den = Δlog P − ΔS_0 − (1/2)Δlog det K
                 + Δlog N_χ + ΔΣ_Y F_Y.           (VAR)

Only the last term has the bound 4h|Γ| obtained from CX-R. The determinant
term alone has the bound q b|Γ|/(1−r) by the two-point norm estimate;
the other separate bounds are 2p_0|Γ|, 2s_0|Γ|, and 2c_0|Γ|. A sharper
small-displacement estimate can be taken from the derivatives of those
actual factors. None is O(h) merely because it is nonzero. In particular,
h=0 does not remove the determinant or main term.

**Nonempty sufficient regime.** On any graph of maximum degree Δ, take
nearest-neighbor E_xy=ε a_xy(z_x,z_y), with ||a_xy||≤1, real symmetric on
real data, and εΔ e^{2β}<1. Then r≤εΔe^{2β}, b≤2r, independently of volume
and deletion of vertices. Choose σ_*p so A_*<a and then choose H so (C)
is ≤1/4. This is a concrete class satisfying the theorem; it is not a
renaming of its integrated conclusion. Nothing here identifies the
Yang–Mills operator with that class.

### 6. Concrete uniform example and exact-check preregistration

Take any finite path, cycle of length at least three, or induced subgraph
of such a graph. Thus holes and disconnected components are allowed and
the maximum degree is two. Let q=1, μ_0=1, β=3, ε=1/16384, and

    E_xy(z)=ε z_x z_y on edges, zero otherwise,  |z_x|≤1.

The atom on an edge has support {x,y}. It is symmetric (transpose, without
complex conjugation), and is real symmetric on real z. Let σ=1/112,
|W_x|≤1, a=1, B_x={x}, and

    V_x(A_x,z_x) = (1/1024) z_x A_x^3.

All component choices and norms in this example are explicit. The bound
e<3 follows from n!≥2^(n−1) for n≥1 with strict inequality for some n.
Consequently e^3<27 and e^6<729, and uniformly over this whole graph family

    r < 2ε·729 = 729/8192 < 1/8,
    b < 4ε·729 = 729/4096 < 1/4.

The two orientations of an edge account for the factor four in b; both
row and column bounds have at most two terms. The empty graph contributes
zero. As (1−r)^(−1/2)≤8/7 and (1−r)^(−3/2)≤(8/7)^2,

    M < 27+8/7−1 < 28,
    B_C < 27+(1/8)(8/7)^2 < 28,
    A_*, B_* < 1/4.

Here s=d_B=Q=1 and H=1/1024, so (C) gives

    h_loc < 27H[4/3+(1/4)(16/9)] = 48H = 3/64,
    ||F||_1 ≤ 2h_loc < 3/32,
    ||−(1/2)logdet K||_3 < 1/7.

These are universal inequalities proved by degree bounds, not inferred from
the finite check. They hold for a product of bounded spin measures or a
fixed product of truncated Gaussian measures. In the latter case the
actual Gaussian prefactor and cutoff probability must be included in (ID).
The real K is positive and the complex branch is the convergent series
from §2, uniformly on |z_x|≤1. No diagonalization by a unitary matrix is
used at complex z; the quadratic form is bilinear A^TKA.

**Exact-check protocol, fixed before running.**

* Verify the rational upper row/column/incidence majorants on paths of
  lengths 1 through 8 and every induced vertex subset. Record the maximum;
  the proof above, rather than this finite family, gives uniformity.
* On four product fair spins use four singleton source factors and four
  pair factors (the three nearest-neighbor edges plus 0–3). The long pair
  gets the connector {0,1,2,3}. Set every factor to 1+t a_i and use distinct
  rational positive coefficients 1/101,…,1/108. Compare the entire exact
  partition polynomial from enumeration of 16 spin configurations with
  a separately implemented overlap-component/hard-core-gas computation
  using spin parity. Compare logarithmic Taylor coefficients through t^6.
  The predicted coefficient of t^3 z_0 z_3 in both logarithms is the
  product of the two endpoint-field coefficients and the long-edge
  coefficient. Reversing the sign of only the long edge must change it.
* On the three-vertex path set z_0=(1+t)/2, z_1=1, z_2=1/2 and H=0.
  A permutation determinant of K(t) and a separate exact inverse/trace
  computation must give

      d/dt [−(1/2)logdet K(t)] at t=0
        = 1/(4·16384^2−2) = 1/1073741822 ≠ 0.

  The omitted-determinant control predicts zero and must fail.
* Audit explicit dependence labels: z_0 z_3 assigned only {0} must fail;
  assigning the same function the full connector must pass. A 0–3 matrix
  atom assigned only {0,3} must fail connectivity, whereas its full
  connector must pass. These are controlled demonstrations of the old
  hypothesis defect, not exhaustive semantic audits of arbitrary code.

The finite graph calculation is an algebraic check using a different
representation from the analytic proof; it does not check a Yang–Mills
measure, any infinite-volume limit, or the actual return operation.

### 7. Executed checks and their limits

Executed under Python 3 using only exact `Fraction` arithmetic:

    python3 checks/recovery_cluster_exact.py > checks/recovery_cluster_results.json

The command exited 0. All 15 named predicates passed. Results:

| Check | Exact result | What it decides |
|---|---|---|
| Direct 16-spin sum versus connected-subset/gas calculation | Entire partition polynomial agrees: 13 nonzero monomials | Finite factorization/combinatorics, with two different implementations |
| Direct log versus overlap-cluster log through t^6 | 19 nonzero monomials agree; every source is inside its connected support | Finite logarithm/locality check; only one- and two-polymer clusters enter this truncation |
| Long-edge source coefficient | t^3 z_0 z_3 coefficient = 1/1134432 | The coefficient is carried by the full connector |
| Sign-corruption control | Coefficient becomes −1/1134432 | The algebraic equality gate can detect a wrong interaction |
| 510 induced paths | Row and column maxima 729/8192; incidence maximum 729/4096 | The stated finite operator majorants, including empty/disconnected graphs |
| Gaussian with H=0 | Both determinant and inverse/trace paths give 1/1073741822 | The full logarithm varies while the nonlinear interaction vanishes |
| Omitted-determinant control | Its prediction 0 disagrees | R11's full-normalizer error is distinguished |
| Remote parameter and endpoint-only labels | Both invalid labels rejected; connector labels accepted | The explicit source and connectivity omissions are distinguished |

For the spin calculation, 176 of 255 nonempty factor subsets are overlap
connected; 14 have nonzero parity expectation, grouped into six gas
supports. Those counts are measured outputs, not success criteria. The
finite check is not a proof of the general rooted tree bounds, which are
proved in §4. There is no numerical spectral estimate or floating-point
fit. These are author-run checks with independent algebraic paths, not a
fresh independent referee and not a formal audit.

### 8. Does the available Yang–Mills material instantiate CX-R?

**No instantiation has been established in the inspected sources.** This
is a coverage and obligation statement, not a counterexample to the
Yang–Mills construction and not an assertion that another proof cannot
work. The generic theorem's exact sufficient conditions stay separate from
the following producer obligations.

| Required object/estimate | Inspected source and actual content | Remaining task |
|---|---|---|
| Correct one-step operator K | `PROOF.md`, N5-sf_i: Hessian of minimum-defined E_i^NA; `B2_55.md` J7 and `CODEX_REVIEW_B2.md` R8 distinguish E_k^cb | Prove the minimum-action/critical-value identification, or derive the actual one-step construction with the critical-value action. A notation change is insufficient. |
| Source-local connected-support expansion of C with row **and incidence** bounds | PROOF Theorem RW (RW1)/(RW2) supplies spatial kernel/walk bounds. RW(v) gives geometric locality only for finite-range K, and dependence on entries of K is not locality of those entries in original z. | Construct supports for the operator's original-coefficient dependence, including gauge/slice maps and long-jump connectors; control their weighted incidence. Lemma O is one sufficient construction, not a consequence of RW1/RW2. §3–4 can also use another construction of the same C bounds. |
| All-order localization after substituting b(z) | BFT34 §1.1–1.2 gives a conditional analytic critical map and weighted first derivative. Its §2.2 separates fixed-order derivative decay from all-order support norms. SRC2 E11 leaves strict relocalization inside its input. | Supply an all-order connected-support mechanism for the actual substituted original coefficient field. A low-order Hessian/kernel estimate does not fill this slot. |
| Uniform complex domain when compression boxes enlarge | STEP55 §5.3/S8 reuses the R_* chart; STEP review R10 identifies its changed quantifiers | Re-prove the needed bounds at the chosen R, e.g. with ε≤α_*/[10 p_L(4R+5)L], T≥4R+6 and the matching complex neighborhood, or supply new global-gap-based compression bounds. Treat excluded small tori separately. |
| Actual local nonlinear vertices with a small norm | STEP55 §5.1/5.3 identifies cubic bare terms and single-normalizer terms, but leaves constants, FP/Jacobian localization and inherited polymers partly unwritten/open | Prove a bound such as (C) for every term after the exact substitution, including the linear term unless exact stationarity removes it. Inherited activities require an induction preserving the same norm and source domain. |
| Main term and determinant in original coefficient variables | STEP55 S9 restores both scalar factors; R11 shows its old variation bound fails | Localize their full logarithms or prove the exact cancellations in the desired ratio. Their size and variation have separate budgets; O(h) is not automatic. Lemma O is sufficient for the determinant only for its actual operator hypotheses. |
| Holomorphy in locally varied source/coupling coordinates | Single-normalizer lemma is uniform for **real** t>0 and complex fields; it is not a uniform complex-coupling theorem (STEP review R6) | Check the complex parameter domain required for the specific coefficient source family, with branches and any zeros controlled on that domain. A global scalar spectator and a spatial source field are different inputs. |
| Exact identity (ID) for Den_Y of the actual return | STEP55 §5.4 assumes the denominator has the CX form; R11 leaves the identity unproved | Match the history, collar, indicators, contour, gauge Jacobian, linear term, reference normalization and product white-noise coordinates. This is necessary already at level zero for a full returned activity. Single-kernel zero-freeness cannot substitute. |
| N1 / multiscale density ratio | SRC2 §3.5 MB proves bookkeeping; F1/F2/F7 distinguish it from norm control and source locality | Supply induction/flow bounds, frozen-part independence from V, bounded top remainder at every V, and the necessary return/large-field estimates. CX-R is one-step support and does not prove these accumulated bounds. |

The operator and source-locality obligations are related; the list is not
a claim of pairwise independent barriers. In particular the same support
construction could discharge the C and determinant slots together. Exact
denominator identification may constrain that construction. No count of
independent walls is inferred.

**Theorem-strength check.** The condition r<1 in Lemma O, the explicit
bare-vertex data in §3 and their smallness imply CX-R by a new construction.
CX-R does not imply r<1 or the bare-vertex representation: they are stricter
sufficient structural conditions, not equivalent reformulations. The
massive graph example shows that the mechanism has a concrete nonempty
domain. Obtaining those inputs for the Yang–Mills producer is unfinished;
it is not being called near closure. A general corrected one-step theorem
could use resolvent/parametrix atoms rather than I−E, provided it proves
the same original-variable support/incidence bounds and handles logdet.

**What can be used now.** The author proof gives a conditional replacement
for the flawed abstract CX implication, with explicit local inputs,
constructive source localization, and the full normalizer formula. It
also gives a direct target for a future RW/parametrix proof: connected
support atoms with finite weighted incidence, before any cluster theorem
is applied. It does not establish the one-step Yang–Mills return, N1, an
off-chart extension, gauge invariance of each generated activity, a
thermodynamic limit, or a continuum limit.

### 9. Checkpoint and exact next work

Preserve the verified distinction between a conditional sufficient theorem
and its physical instantiation. The smallest next useful producer task is
to start from the **identified actual** one-step operator and construct a
background/source-local resolvent parametrix with connected supports and
both row/column and incidence majorants. Its atoms must be functions of the
original coefficient field, and must charge long jumps before regrouping.
At level zero the finite-range bare operator is a reasonable first test;
the exact slice map and full normalized return identity still need to be
matched. At higher levels resolve the consumer identity before importing
critical-branch Hessian estimates.

No generic no-go theorem is claimed. Three approach families were actually
examined: connected-support analytic composition (constructed), ball
truncation with exponential radius tails (insufficient for the chosen
support-size proof without extra estimates), and exact countermodels to
the old hypotheses (reproduced). There is no five-family negative-packet
PASS and no claim of route exhaustion. Countermodel residuals are matched
only to the literal old implication; they are not presented as matched
countermodels to the full Yang–Mills input package.

Additional bounded source reads after the initial declaration:
PROOF's full Theorem RW and N5-sf_i statement/qualification; SRC2 §3.5 and
E11; B2 J6/J7; BFT34 §1.1–1.2. A source-identity/check receipt is saved as
`checks/recovery_cluster_receipt.json`. The assigned baseline identifier
remains coordinator-supplied. No original scientific file was edited.

Coordinator check receipt: the coordinator reports an independent replay of
`checks/recovery_cluster_exact.py`, exit 0, empty stderr, and byte-for-byte
stdout agreement with `checks/recovery_cluster_results.json`. This is a
reproduction check, not independent mathematical review of the theorem.
