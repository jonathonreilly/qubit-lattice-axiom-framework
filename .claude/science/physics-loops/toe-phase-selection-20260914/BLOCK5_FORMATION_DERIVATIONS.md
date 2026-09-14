# Formation histories, Gaussian fill, and a posterior escape

Personal derivations, 2026-09-14. Author-checked finite examples accompany
these arguments. No formal retained status, no axiom amendment and no claim
that a selected native history law has been derived.

## Fixed-order raw-record criterion

Let P=N(0,Q^-1), with Q a real positive definite precision on a finite graph.
Supply an order v1,...,vn. A candidate sampler writes each scalar once and
uses a conditional density q_k(x_vk | x_Parents_k), where Parents_k are
previous vertices adjacent to vk in the declared physical read graph.
Permit arbitrary site-dependent densities, not just linear Gaussian rules;
this is more permissive than a single covariant native rule. There is no
hidden message, shared latent seed or schedule variable in this candidate.

For prefix A={v1,...,vk} and future F its complement, Gaussian integration
gives the marginal precision

    K_A=Q_AA-Q_AF Q_FF^-1 Q_FA.

The exact next conditional has variance 1/(K_A)_vv and mean
-sum_(u in past)(K_A)_vu x_u/(K_A)_vv. Full support makes its dependence on
each scalar coefficient unambiguous almost everywhere. Thus an exact local
sampler for this order exists iff every coefficient to a past nonneighbor
is zero. The proof uses the chain factorization of the joint density; it
does not substitute the full-neighbor Gibbs conditional for the prefix law.

For ANY candidate local densities, the KL chain rule gives

    D(P || product_k q_k)
       = sum_k I_P(X_vk; X_Past\Parents | X_Parents)
         + sum_k E_Parents D(P(X_vk|Parents) || q_k(.|Parents)).

Therefore the minimum is the sum of conditional mutual informations and is
attained by the target's own local-parent conditionals. For Gaussians it is
one half the logarithm of the product of local conditional variance divided
by full-past conditional variance. This is an exact optimization over local
densities, not a fit to one Gaussian approximation. It is only for the
specified order and specified information available in each record.

## Attractive precision: why a cycle leaves missing information

Suppose Q has strictly negative entries at every interaction edge and zero
at nonedges. Every principal block is a positive definite M-matrix. To see
entrywise positivity of its inverse, choose s at least its spectral maximum
and write Q_FF=s(I-T). T is entrywise nonnegative, ||T||<1, and
Q_FF^-1=s^-1 sum T^j. Its entries are strictly positive precisely within
connected components, by paths in this nonnegative series.

The Schur formula consequently adds a negative coupling between two visible
vertices whenever a path between them has internal vertices in the future.
No later Schur elimination cancels a negative fill edge: every correction
has the same nonpositive sign. If the interaction graph has an induced
cycle of length at least four, take its latest-formed vertex, equivalently
the first of that cycle eliminated in reverse. Its two cycle neighbors
are original nonneighbors. Eliminating it creates a strict negative fill
between them; the edge persists until one endpoint is eliminated. The
conditional at that endpoint then depends on an original nonneighbor.
Additional vertices outside the cycle cannot cancel this contribution.

Thus no fixed order in the raw-record candidate realizes an attractive
Gaussian on a graph with an induced cycle. For a triangle-free interaction
graph, a shortest cycle is induced, so an exact order exists iff the graph
is a forest. A forest has a constructive root-first sampler: reverse
eliminate leaves, which creates no new adjacency. More generally the usual
perfect-elimination/chordal sparsity machinery supplies the no-fill order
criterion for an entire positive definite sparsity class. Tuned signed
matrices are outside the noncancellation argument.

An independent algebraic view writes the exact Gaussian chain as
Q=(I-A)^T D^-1(I-A). In the attractive case its regression coefficients
are nonnegative. On a triangle-free read graph, any two parents of one
child are nonneighbors and contribute a positive parent-parent precision
entry. There is no direct parent-parent edge term to cancel it, and other
children contribute the same sign. This again prevents such a candidate
from creating an attractive cycle with its declared local read set.

## Exact four-cycle, and a signed positive counterexample

For Q=3I-Adj(C4), order (0,1,2,3) gives
K_02=-1/3, K_22=8/3 at the third step. Hence

    X2 | X0,X1 ~ N((X0+3 X1)/8, 3/8).

X0 is a past nonneighbor of X2. The best local-parent conditional has
variance 8/21 instead, giving KL loss (1/2)log(64/63). The exact runner
enumerates all 24 orders: 16 have this minimum loss and eight have
(1/2)log(49/45). It independently constructs the generated covariance and
checks both its determinant ratio and the Gaussian KL trace term. Longer
five- and six-cycles are finite challenges, not an all-size proof.

Now flip the 0--3 edge sign:

    Q=[[3,-1,0,1],[-1,3,-1,0],[0,-1,3,-1],[1,0,-1,3]].

It is positive definite, eigenvalues 3+-sqrt(2), each twice. An exact local
sampler in order (0,2,1,3) is

    X0,X2 independently N(0,3/7),
    X1=(X0+X2)/3 + independent N(0,1/3),
    X3=(-X0+X2)/3 + independent N(0,1/3).

Both covariance and precision factorization reproduce Q exactly. The two
parents' fill terms from children cancel. Eight orders have zero KL loss;
the other sixteen have (1/2)log(64/63). This is a decisive counterexample
to a sign-blind no-go from the cycle geometry alone. The actual DK source
has signed/complex coefficients, so an attractive-field obstruction cannot
be applied to it without a source-specific reduction.

For a two-layer bipartite precision [[U,C*],[C,V]] with U,V diagonal, forming
the first layer independently and then the second using its neighbors is
possible precisely when U-C*V^-1C is diagonal and positive. The signed
four-cycle uses weighted orthogonal columns of C. This supplies a useful
positive mechanism to test in Dirac/Clifford source algebra, not an assumption
that all such sources satisfy it.

## A local permanent process with nonlocal static full conditionals

Supply four initial control records and root sites
(0,0,0),(2,0,0),(2,2,0),(0,2,0), with each control one step in +z from
its root. Edge-observation sites are the four midpoints of this square.
For fixed positive m,kappa, draw independent root values X~N(0,m^-2 I).
After an edge's two roots are present, write

    Y_e=(D X)_e+eta_e,    eta_e independently N(0,kappa^-1),

where D is the oriented cycle incidence. Each write reads only neighboring
records; each site writes once; prior controls and every written value are
permanent. A causal schedule is supplied. Any fair schedule respecting the
parent relation gives the same complete joint law, since independent noises
can be assigned to nodes in advance and the acyclic recursion fixes their
outputs. This is a downstream conditional protocol, not a selected formation
site/rate law or a construction of the initial program records.

The target values and finite role/frame metadata fit a particularly simple
closed-support one-real-payload M2 codec:

    M=(8r+i x)I+(R(1,2,3)).sigma.

The real and imaginary central traces recover r and x; the free proper-cubic
orbit recovers R. Each supported affine line is closed. Proper rotations
act by the usual Pauli star automorphism; co-rotate coordinates and frame.
This uses no nonlinear full-payload codec or independent authority from
PR8125. Only present records are read. Controls identify the root role;
two compatible root roles identify an edge-observation role. One finite
rule on these supplied local program conditions can implement the root,
copy and observation cases. Its probabilities, frame convention and program
are definitions, not selections from the four axioms.

The completed joint precision of (X,Y) is

    [[m^2 I+kappa D^T D, -kappa D^T],
     [-kappa D,                 kappa I]].

It contains root-root terms at physical distance two. Thus nearest-neighbor
formation kernels do NOT generally imply a nearest-neighbor static Gaussian
precision on the completed records. The root would never form again after
its child observations; applying a hypothetical full conditional there is
a different question from the actual formation probability.

The unconditional root covariance stays m^-2 I. Conditioning on Y=0 gives

    X | Y=0 ~ N(0,C),   C=(m^2 I+kappa D^T D)^-1.

For m=kappa=1 this is exactly the attractive four-cycle above. This does not
contradict its raw-field sampling obstruction: the target is now a POSTERIOR
after conditioning on extra later observations, not the unconditional law
of the formed roots. The runner separately constructs the joint covariance,
the conditioning Schur complement and the nonnearest precision entries.

An exact point Y=0 has zero probability in this continuous model. The
Gaussian conditional is the continuous version there, and positive windows
give a controlled operational approximation. Write A=kappa C D^T.
For any y, X|Y=y has mean Ay and covariance C. The KL divergence from
N(0,C) is (1/2) y^T A^T C^-1 A y. Since kappa D C D^T<=I, this is at
most kappa ||y||^2/2. Conditional on ||Y||_infinity<=epsilon, convexity of KL
and Pinsker give

    TV(P(X | window), N(0,C)) <= epsilon sqrt(kappa E)/2,

where E is the number of edge observations. The finite window has positive
probability; no lower bound uniform in E or epsilon is claimed. Its rarity
and the conditioning choice are physical costs, not automatic phase selection.

## Consequence for the next construction

The strict scalar-precision routing program is sufficient for a particular
Gaussian full-conditional specification. It is not forced by formation
locality alone. Conversely, the local Bayesian protocol above does not
automatically produce the desired Gaussian as an unconditional physical
state. These two distinctions should be carried into any claimed native
realization or axiom-update argument.

The next useful experiment is an actual Gaussian likelihood program for the
finite DK source, keeping its proper-prior and postselection costs explicit.
Its deterministic copy/sum wires need a CAUSAL physical embedding: sharing
two crossing payloads at one permanent site can couple their write stages
and introduce a site-level dependency cycle even when the scalar circuit is
acyclic. A vertex-disjoint wire construction would avoid that additional
assumption. No such construction or DK program is claimed complete yet.

## Literature coverage and limits

Read the Gaussian conditional-independence section 2.1 and chordal Schur
factorization section 3.2 of Dahl, Roychowdhury and Vandenberghe,
https://www.seas.ucla.edu/~vandenbe/publications/covsel1.pdf .
The mathematical claims above are derived explicitly, and the signed
cancellation is not excluded by a theorem about generic sparsity patterns.
Rose--Tarjan--Lueker (1976), DOI 10.1137/0205021, was checked at publisher
abstract level only. Lauritzen's Oxford lecture page was read, but the slides
returned HTTP403 on full retrieval; do not claim them read.

Any negative publication needs the full no-go discipline. Live alternatives
include correlated messages, joint writes, adaptive schedules, latent data,
postselection, approximation and differently factorized sources. The only
negative result currently supported is for the stated raw-record fixed-order
candidate, with the noncancellation assumptions explicit.
