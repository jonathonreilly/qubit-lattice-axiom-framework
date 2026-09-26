# Independent all-stage reconstruction before author controls

2026-09-21. The complete supplied note was read at SHA-256
`e7d47eb97d62fad65153d377bc19257ebcc2ff8aa1b0f0c5027a5424afe0eabd`.
No new author checker, results or logs have been opened. The following proof
check uses the supplied geometric model and unchanged independently checked
matching/finite-killing premises. No replacement construction, imported
Dagum--Luby bound, physical interpretation or audit status is supplied.

## Corridor and connectivity

Let T have k>=2 edges. Contract each T-edge and leave its unmatched vertices
as singleton nodes. A simple quotient path joins any two reference edges.
For a segment aa',z1,...,zs,bb', start with aa' missing. Shift the occupied
pair bb' successively backwards through the empty corridor, then across a
to a'. This takes s+2 legal slides, ends at T-bb', and leaves every singleton
site empty again. The s=0 case consists of (a,b,b') then(a',a,b); s=1 takes
three steps. No record is created: each slide transfers the two existing IDs
one physical edge each. Applying inverse triples in reverse order restores
every record ID, including its orientation.

If the simple quotient path visits r matched nodes and s singleton nodes,
the count is2(r-1)+s<=2(k-1)+(V-2k)=V-2. Parent states T-e are distinct.
Within a segment, an intermediate state is T-e-f+g where g is a non-T edge
along the corridor. Its missing reference pair and moving edge identify it.
Different segments have distinct pairs of missing reference edges. Thus the
route repeats no state or transition. The explicit path-ten control with
T={01,89} and six interior singleton nodes takes exactly8=V-2 slides.

For arbitrary M of size j<K and a perfect P, M xor P has even alternating
cycles and exactly K-j alternating paths with P edges at both ends. There
are no other path types: every vertex has a P partner, so an endpoint of a
nontrivial symmetric-difference component must be unmatched by M. Sliding
successively from one endpoint of each path installs P edges and leaves one
vacant P edge per path. Remaining non-P edges lie only on cycles.

Use a vacant P edge h as a reference vacancy. For an M edge e on a remaining
cycle, T=M+h is a legitimate matching of size j+1; the corridor route takes
T-h to T-e using only the actual j record pairs. A cycle with r M edges is
then aligned using r-1 slides, leaving one vacant P edge for the next cycle.
This eventually yields a j-edge subset of P. Two such subsets are joined
by virtually adding a desired missing edge and transporting the missing
reference edge to an unwanted occupied edge. Reversing the corresponding
construction from a target proves geometric irreducibility for every j<K.
The virtual matching is bookkeeping; it never inserts a physical record.

The empty level is a singleton. At j=K there are no slides and multiple full
matchings remain distinct. No statement about irreducibility of all marked
states or full-matchings-only motion follows. Connectivity of G and existence
of a perfect matching are genuinely used; disjoint edges give a disconnected
one-pair slide chain, and a star without a perfect matching has no terminal
paired birth after its first insertion.

## Arbitrary hazard and composition

Write A_j(M,T)=1_{M subset T}, h=A_j1 and p=pi h. Counting parents gives
A_j^T1=(j+1)1, p=(j+1)a_(j+1)/a_j and pi A_j=p U_(j+1). In particular p>0
although individual h values may vanish. The finite irreducible symmetric
slide chain has centered inverse G_j with finite infinity norm. The previous
spectral argument supplies B_j=(1+log a_j)/g_j if j>=1. This is a finite-graph
bound, not a quantitative all-volume mixing assertion.

For an exit event D, a_D=A_j1_D obeys0<=a_D<=h<=m. The killed equation is
(L+beta H)u=beta a_D. If u=c+v, pi v=0, then

    v=beta G_j(a_D-hu), ||v||infty<=beta m B_j,
    c-U(D)=-pi(hv)/p, |c-U(D)|<=||v||infty.

The cancellation uses pi h=p; no lower bound on h at individual states or
extra inverse-p factor is needed. It gives the claimed TV bound2beta m B_j.
For the joint transform with exponent lambda beta p tau, replace H by
H+lambda p I. The centered source is bounded by m+lambda p, and the constant
equation becomes p(1+lambda)c+pi(hv)=pU(D). Hence the error is at most
beta B_j(m+lambda p)(1+1/(1+lambda)), as stated.

For w=beta p E tau, the constant equation is pi(hw)=p, while the centered
part is v=-beta G_j(hw). With delta=beta m B_j,
||w-1||<=2delta||w||<=2delta(1+||w-1||). For2delta<1 this gives Eq.(7).
Finiteness of the mean comes first from finite irreducibility and the
nonempty killing set. Mean convergence is not inferred from weak convergence.

At j=0, h=m is constant and the first mark is a uniform edge independent
of its Exp(beta m) time. At fixed G there are finitely many later levels.
The event/transform bounds hold uniformly over every entrance state, so the
strong Markov property permits multiplying their finite kernels. For arbitrary
nonnegative stage parameters s_j, choose lambda_j=s_j/p_j. The limiting kernel
from any entrance is [p_j/(p_j+s_j)] times the uniform row on Omega_(j+1).
Products with any intervening geometry-event diagonal matrices converge to
the product of these factors and the corresponding uniform event masses.
This proves joint independence of all scaled stage times and the successive
post-birth geometries, including the terminal geometry. Multivariate Laplace
uniqueness on nonnegative coordinates identifies the clock law. Summing the
uniform conditional mean limits separately proves C(G)=sum_j1/p_j.

This uses autonomous geometric rates. Neighbor-dependent content marks can
retain correlations without changing that geometric kernel. It does not
assert independence of immutable marked histories at finite or limiting beta.

## Counting injection and the clock coefficient

For each pair (M,P), choose one of its K-j P-augmenting path components Q.
Flip Q in both matchings, producing U of size j+1 and W of size K-1. Their
symmetric difference is unchanged: U xor W=M xor P. The two holes of W are
exactly the endpoints of Q. Therefore they recover the unique component Q
in U xor W, and flipping it recovers M,P. Arbitrary codomain pairs need not
have those holes in one component, but injectivity only requires recovery
on the image. Thus

    (K-j)a_j Z <= a_(j+1)a_(K-1),
    1/p_j <= R/[(j+1)(K-j)].

Summing 1/[k(K+1-k)]=(1/k+1/(K+1-k))/(K+1) gives
R/K<=C(G)<=2R H_K/(K+1). This is elementary counting, independent of mixing
rates and valid on irregular and nonbipartite graphs under the stated premises.

The unchanged Taggi input is reused only for even cubic tori N>=4, fixed d>2,
unweighted all-sector matching counts and the previously checked positive-time
return convention. R<=K^2/(2d), V=2K, and C>=R/K give exactly Eqs.(8)-(9).
These concern lim_(beta->0) beta E T at each finite graph, followed by volume;
they imply an Omega(V)/O(V log V) interval for that coefficient. They do not
give a fixed-beta upper time bound, a coefficient limit or an all-stage
simultaneous beta(V) schedule. The external theorem's statement/hypothesis
verification is inherited by identity; its full proof was not newly checked.

## Two-level energy comparison

Take1<=j<K and k=j+1. The auxiliary chain includes every valid one-edge
replacement within each of Omega_j and Omega_k, as well as additions/deletions
between them, all at rate kappa. Disjoint replacements are comparison events,
not physical slides. If A is lower/upper incidence and H=diag(A1), the
unnormalized lower parent-clique energy is represented by U=kH-AA^T. Thus
the lower exchange Laplacian is exactly L_slide+U.

Extend f by bar f(T)=k^-1 sum_{e in T} f(T-e). The cross-level energy is
U(f)/k by the finite variance identity. Any adjacent upper pair T,T' has the
unique shared parent C=T intersection T'. Inserting f(C) and using the
two-term square bound gives upper energy at most
2 sum_(T,C) number_of_neighbors_through_C [bar f(T)-f(C)]^2.
For fixed (T,C), there are at most m such neighbors, so this is at most
2m U(f)/k. Consequently the total unnormalized energy is bounded by
kappa[D_slide+(1+(1+2m)/k)U], with the factors in Eq.(10) intact.

For any micro-edge M--M', its removed/moving edge g=M minus M' is identified
from that oriented transition. A reference matching used by a routed parent
pair is either T=M+e (parent case), or T=(M-g)+e+f (corridor-interior case).
Allowing both endpoint orientations gives at most2(m+m^2) references. Each
reference has at most k(k-1)/2 unordered parent pairs. No route repeats a
micro-edge and each has length at most V-2. Therefore

    U <= (V-2)(m+m^2)k(k-1) D_slide,
    C_(V,m,k)=1+(V-2)(m+m^2)(k-1)(k+1+2m).

The smaller two-reference bound from the near-perfect proof cannot be reused
at intermediate levels: the independent path-ten one-pair control encounters
nineteen references on one micro-edge. The new bound covers it. The extra
factor two here is conservative, so no optimization is needed to justify it.

Under the uniform auxiliary law, both the energy conversion and the variance
lower bound carry a_j/(a_j+a_k). They cancel, yielding gap(S_j)>=gap(B)/C.
The auxiliary chain is connected because its lower slide subgraph is connected
and every upper matching has k parents. No uniform polynomial lower bound on
its gap has been imported. In particular, neither Dagum--Luby nor a
fixed-distance-from-maximum theorem is used in this reconstruction.

## Exact finite controls and countercontrols

The independent program chooses ten fixed graphs: paths4,6,10; cycle4;
diamond; complete6; two triangles joined by a bridge; triangle with a tail;
two squares joined by a bridge; and the cube. It checks all nonfull
cardinalities, arbitrary-parent corridor paths with marked forward/inverse
replay, and the injection/recovery for every (M,P,Q) in these graphs.
All lower/add-delete/extension matrix identities are exact rational checks.
Spectral gaps and positive-semidefinite inequalities are numerical controls
supporting the analytic argument, not exact eigenvalue proofs.

For lower layers of at most12 states, direct rational killed resolvents check
the arbitrary-hazard bounds at two beta values, two nonzero Laplace parameters
and all next-geometry events via positive/negative row sums. The hazards are
not restricted to0/1; an intermediate path-ten level has range0..3. This
tests the m factor and the claim that zero instantaneous birth hazard need
not prevent eventual formation.

Separately, exact symbolic multistage resolvent products give:

- C4: beta E T_total=5/4, exactly, at every beta with kappa=1.
- Diamond: beta E T_total=(beta+29)/20, giving slow limit29/20.
- Path6: beta E T_total=(30beta^3+228beta^2+398beta+157)/
  [20(3beta^2+7beta+3)], giving slow limit157/60.

The same controls use distinct Laplace parameters at successive levels and
intervening post-birth geometry events; their limiting transforms factor with
the predicted uniform event masses. The diamond expression is a countercontrol
to silently treating the limiting C(G) as an exact fixed-beta formula.
Disconnected-edge and no-perfect-matching controls retain the hypothesis
boundaries. The independent run completed on its first execution with empty
stderr. No author-control body, results or log has yet been accessed.
