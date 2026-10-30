# JMBRB — per-step large-field renormalization and the missing renewal bound

**LF-JMBR on the actual all-cut reference remains OPEN.** Per-step
renormalization removes the old depth test **if a genuinely new price or
an irrelevant contraction is proved at each step**. Re-blocking a positive
old activity does not itself earn that price. Here the normalized soft
kernel supplies a new price for its gap events, including a conditional
geometric bad-plaquette branch. It does not supply the required estimate
for the branch with an inherited rough mean. SOFTHARD G2 supplies a finite
boundary debit, not a negative action or a renewal probability.

The exact transfer identities, gap bound, geometric dichotomy, conditional
per-step summation and conditional connected expansion below are PROVEN
at their stated scopes. The proposed actual induction is ARGUED; its
unmet clauses are OPEN. These words are author mathematical statuses,
not audit verdicts, a full Yang--Mills theorem or a no-go for this route.
The fresh review and execution record are in [JMBRB_LOG.md](JMBRB_LOG.md).

Credit: Tadeusz Balaban for the organization of small and large fields
and the recycling of large-field contributions; Jonathan Dimock for the
exposition, particularly [Large fields](https://arxiv.org/abs/1212.5562)
and [Convergence](https://arxiv.org/abs/1304.0705). Their stated models
are scalar theory in three dimensions. In Part II, section 3.3, Remark 3,
Dimock distinguishes Balaban's recycling operation from the construction
needed in that paper. This note rebuilds its mathematical statements;
neither those papers nor the description “Balaban's organization” supplies
the missing four-dimensional nonabelian induction. No memory-only [m]
item carries weight.

## 1. Target and conventions

Fix N>=2, odd L>=3 and a finite compatible four-dimensional periodic
lattice. Haar measures are probability measures. The supplied Wilson and
Decision-4 model, not a new physical axiom, is

    s(U)=1-Re tr(U)/N=||I-U||_HS^2/(2N),
    u_j=g_j^(-2),  t_j=kappa u_j,
    h_M(V)=Re tr(V^*M)/N,
    k_t(V;M)=exp(t h_M(V))/Z_t(M),
    Z_t(M)=int exp(t h_M(W)) dW,
    K_j(V,U)=product_c k_(t_j)(V_c;M_c(U)).                 (B1)

Here M_c is the arithmetic mean of Decision-4's paired contour
transporters; ||M_c||_op<=1. It is not the deterministic averaged-log
map. The constant exp(-t) in the other convention cancels from numerator
and denominator. The exact action at fixed V contains

    S_j(U)-t_j sum_c h_(M_c(U))(V_c)+sum_c log Z_(t_j)(M_c(U)). (B2)

The last term depends on U. All reference constructions must retain it.
At higher levels S_j is the actual effective action, not a fresh bare
Wilson action supplied by notation.

The consumer remains LFPRICE section 6, clauses 1--5, on RD3's

    R_h(V)=int rho_(j,h)(U) K_j(V,U) dU,
    Z_A(V)=int chi_A(U) b_j(U) K_j(V,U) dU,
    Q_h(V)=R_h(V)/Z_A(V).                                  (B3)

Any current selectors in a selected numerator remain inside its integral.
The fixed original-source/coarse domain is D_* of RD4, on the actual
history/chart class. Neither the real full-chain partition function nor
a convenient Gaussian normalizer may be substituted for Z_A. Original
source readers, inactive vertices and tails count in the full support
norm, with mu>=0,

    ||F||_mu=sup_x sum_(X contains x) exp(mu |X|) sup_(D_*) |F_X|. (B4)

The norm graph and source labels must be fixed by the consumer. Counting
only the latest coarse shadow does not prove (B4).

For comparison with freezing only, use the named, unproved-here bracket

    v+beta_- r log L-R <= u_(K-r) <= v+beta_+ r log L+R,
    0<beta_-<=beta_+,  v>0.                                (B5)

For a raw cut epsilon(u)=u^((delta-1)/2), 0<delta<1, a distinct owned
Wilson plaquette costs at least u^delta/(2N). If the cut is on the
rescaled curvature f/g, this is p(g)^2/(2N), not u p(g)^2/(2N).
It follows by expanding (I-U)^*(I-U) and using the largest singular
value <= the Hilbert--Schmidt norm. No unbounded curvature variable is
substituted for the compact group distance.

## 2. Exact re-blocking, and what it cannot reprice

### B-RB: sector transfer — PROVEN, finite real measure scope

Let f_h(U)>=0 be any integrable inherited density with all its history
indicators and earlier integrals included. At the next step choose any
finite measurable partition {I_a(U,V)} of the full real configuration
space. For example, insert each local chi+(1-chi), then specify the exact
bad set, its maximal components and all completion outcomes. Define

    f'_(h,a)(V)=int f_h(U) K_j(V,U) I_a(U,V) dU.            (B6)

Fubini and sum_a I_a=1 give

    sum_a f'_(h,a)=K_j f_h,
    sum_a int f'_(h,a)(V)dV=int f_h(U)dU.                  (B7)

This is an exact per-step reclassification without freezing the fields.
Zero-mass sectors stay zero. Components may merge; label a contains the
whole new partition rather than independently chosen overlapping pieces.
For a prescribed old h, its absence-of-other-failure predicates stay in
f_h. Summing h later and normalizing a fixed h are different operations.

An explicit reader assignment is available before any chart change.
Give each bare action/source factor its plaquette and original source
label, each kernel numerator and its Z_t its entire contour reader set,
and each predicate every variable it tests. When integrating variables
in a set Y, join all factors reading those variables and keep the union
of their other readers. Repeating this rule gives an exact, possibly
large, support for every output factor. This follows directly because
the integrand depends on no coordinates outside that union. Take connected
hulls when (B4) requires them. A history-dependent effective action can
also be opened back into its earlier variables before applying this rule.
Haar coordinates here have no new gauge Jacobian. A later gauge/chart
change requires its own exact identity and all its factors.

Thus (B6) proves the raw integration and support bookkeeping substep of
clause 1. It does not prove a small local reference matching Z_A off the
boundary: the above union may contain long readers or an extensive
avoidance condition. No density ratio across different hard supports was
used.

### B-MASS: transport preserves an old positive mass — PROVEN

Let mu be a probability on U, K a positive normalized kernel, and
nu(dV)=int mu(dU)K(U,dV). For a>=0 integrable, its relative transported
insertion is the Radon--Nikodym derivative

    a'(V)=d[(a mu)K]/dnu=E[a(U)|V].                        (B8)

The conditional expectation is defined nu-almost everywhere. Integration
gives

    int a' dnu=int a dmu,
    ||a'||_(L^1(nu))=||a||_(L^1(mu)),
    ||a'||_infinity<=||a||_infinity.                       (B9)

The last statement applies to bounded a. For signed a, the L1 statement
becomes <= by the triangle inequality. In particular, the universal
positive-mass estimate `||a'||_1<=exp(-q)||a||_1`, q>0, is false for
every nonzero positive a. The insertion a=epsilon is an exact fixed
point. A mandatory event E of mass p becomes 1_E/p when conditioned;
its L1 norm is one, not p.

For the actual (B6), an inherited history with mass A_h>0 has total
descendant mass A_h after every number of steps. Charging that same
unnormalized mass exp(-q) again at each step while retaining **all**
its descendants contradicts (B7). An effective-action rewriting may
extract a vacuum factor or move weight to returned sectors; that is not
the estimate contradicted here. The result rules out automatic repeated
pricing of unchanged mass, not renormalization with extraction.

Even subtracting just the mean need not give weak-coupling contraction.
For a diagnostic on one SU(2) link, take M(U)=U and the kernel (B1).
Haar is stationary, Z_t(U)=Z_t(I), and f(U)=tr(U)/2 is real and has
Haar mean zero (U -> -U reverses its sign). With

    lambda_t=int f(W) exp(t f(W))dW / int exp(t f(W))dW,

conjugation invariance and W -> W^(-1) imply E_t W=lambda_t I.
Substitution U=VW in the backward conditional integral yields
`E[f(U)|V]=lambda_t f(V)`. Moreover lambda_t ->1. Indeed, for any
eta>0, the numerator mass where f<=1-eta is at most exp(t(1-eta));
a positive Haar neighborhood where f>1-eta/2 lower-bounds the denominator
by m_eta exp(t(1-eta/2)). Its complementary probability tends to zero;
boundedness of f then proves the limit. Thus a normalized soft kernel
alone has no centered contraction uniformly below L^(-4) as t grows.
This is a kernel diagnostic, not the actual four-dimensional block map
or a counterexample to contraction after the full R-operation.

## 3. A genuinely new per-step price from the soft kernel

### B-GAP: uniform gap pricing — PROVEN, all fixed N

Set D=2N^2 and psi_M(V)=max_W h_M(W)-h_M(V)>=0. For 0<r<=1,
an operator-norm Haar ball of radius r has mass at least

    m_r >= (1+4N/r)^(-D).                                 (B10)

Proof: partition the real and imaginary matrix entries in [-1,1] into
intervals of length at most r/(2N). There are at most (1+4N/r)^D
cells. Two matrices in a cell have Hilbert--Schmidt distance at most
r/sqrt(2). A representative group element in each occupied cell gives
a cover by r-balls. Haar invariance makes their masses equal, so their
total mass is at least one. Compactness supplies a maximizer of h_M,
and trace duality gives |h_M(V)-h_M(W)|<=||V-W||_op.

For t>=1, the 1/t ball about a maximizer therefore gives

    int exp(-t psi_M)dV >= e^(-1)(1+4Nt)^(-D),
    1_(psi_M>=a) k_t(V;M) <= e(1+4Nt)^D exp(-t a),
    P_(k_t)(psi_M>=a) <= min{1,exp[-q_gap(t,a)]},
    q_gap(t,a)=t a-1-D log(1+4Nt).                         (B11)

The pointwise inequality is relative to Haar density, not to Z_A.
It holds even for short or singular means. No sharp SU(N) moment formula
is imported. Distinct output links have product conditional kernels, so
the probability bounds multiply conditional on the whole past.

Here is the exact multistep use, allowing dependence on earlier fields.
Let F>=0 be measurable before step j. At each subsequent step l choose
a past-measurable set of distinct output links and gap thresholds whose
conditional joint bound is at most e^(-q_l), uniformly over that past.
For a fixed finite list of such steps, integrating the latest output
first and iterating conditional expectation proves

    E[F product_l 1_(gap event at l)]
                 <= E[F] product_l exp(-q_l).             (B12)

The bounds may be chosen deterministic uniform lower bounds if thresholds
or link choices are adaptive. Earlier events are measurable when the
next conditional estimate is applied. This proves true repeated pricing
of **new gap events**, not repeated pricing of an old label. Future
conditioning cannot be silently inserted into F. For a fixed prescribed
future event the law is tilted by its conditional probability; that
extra factor needs its own estimate. Sources at original fields may ride
as |F| for an absolute bound, but their complete norm (B4) is not proved
by (B12).

At a shrinking gap a(u)=a_0 u^(delta-1), a_0>0, the price is
`kappa a_0 u^delta-O(log u)`, which tends to infinity for every delta>0.
It can beat a fixed per-step entropy for a singleton. This is the first
place the soft kernel genuinely supplies the proposed per-step price.

### B-GEOM: the geometric interface and its unsolved branch — PROVEN dichotomy

For clarity rebuild the needed part of RLARGE's one-step RS method.
For c=(X,X+e_mu), let S_c be the straight transporter between block
centers. The paired contour T_y^sigma follows the order-sigma axial
path gamma from the center to y, the length-L leg in direction mu,
and the reverse translated copy of gamma. Moving the leg past one
transverse edge of gamma sweeps L elementary plaquettes. An edge parallel
to mu cancels by backtracking. There are at most 3(L-1)/2 transverse
edges. Consequently, if every fine plaquette in the two endpoint blocks
and the intervening ribbons has distance <=eta from identity,

    ||T_y^sigma-S_c||_op<=A_L eta,
    ||M_c-S_c||_op<=A_L eta,  A_L=3L(L-1)/2.              (B13)

To justify the nonabelian bound, each successive plaquette attachment
multiplies the loop holonomy by a conjugate of that plaquette or its
inverse. Unitary conjugation preserves norm and
`||AB-I||<=||A-I||+||B-I||`. Telescoping proves (B13), without commuting
plaquettes. The L by L square between four block centers similarly gives
`||I-S_P||<=L^2 eta`. Telescoping its four links yields

    ||I-V_P||<=L^2 eta+sum_(c in boundary P)||V_c-S_c||.    (B14)

These constructions are local lifted lattice paths. On a compatible
torus use the same labeled paths before projection; repeated plaquettes
are counted with multiplicity. A history removing any of these readers
does not satisfy this hypothesis until the missing reader is restored.

For any S in SU(N) and ||M-S||<=d,

    psi_M(V)>=h_M(S)-h_M(V)
             >=||V-S||_op^2/(2N)-2d.                     (B15)

The second inequality compares the two h_M values to h_S; each error is
at most d, and `h_S(S)-h_S(V)=||V-S||_HS^2/(2N)`.
Given a coarse cut epsilon>0, put

    eta_1=min{epsilon/(2L^2),epsilon^2/(512 N A_L)},
    a_epsilon=epsilon^2/(256N).                           (B16)

If ||I-V_P||>=epsilon, either a fine plaquette in the four-block
ribbon/square neighborhood has size >=eta_1, or all are <eta_1 and
one of the four links has ||V_c-S_c||>=epsilon/8. In the second
case (B13)--(B15) give psi_(M_c)(V_c)>=a_epsilon. The first alternative
is called the rough-input branch; it has not become a new kernel event.

There is also an explicit block multiplicity bound. Conditional on an
input U satisfying the smooth-input premise for n distinct selected
coarse plaquettes, simultaneous badness assigns one of four witness links
to each plaquette. At most six distinct plaquettes in four dimensions
read any given link, counting oriented geometric labels once. Thus an
assignment uses at least n/6 distinct links. With
`p_gap=min{1,exp[-q_gap(t,a_epsilon)]}` and conditional independence,

    P(all n selected plaquettes bad | U)
        <=min{1,4^n p_gap^(n/6)}.                         (B17)

The 4^n assignments are a union bound, not assumed independence of
plaquettes. Bad blocks supplying distinct owned interior plaquettes may
use (B17) after summing their finite choices as well. That extra fixed
within-block choice factor belongs in entropy. With epsilon(u) as in
section 1, the available per-plaquette exponent on this branch is

    q_geo(u)=kappa u^delta/(1536N)
                    -[1+D log(1+4N kappa u)]/6-log 4,     (B18)

once q_gap is positive. This tends to infinity. It is a price under the
plain forward law on the stated smooth-input branch, not an evaluated
joint all-cut activity exponent.

The other branch is substantive. For small epsilon, eta_1 is proportional
to epsilon^2, so its **bare Wilson threshold bound alone** is of order
`u eta_1^2=u^(2delta-1)`. It does not diverge when delta<=1/2.
In particular it is weaker than the original cut u^delta, and a
plaquette between eta_1 and epsilon may pass that original cut. At higher
levels even the Wilson form needs a consistent effective-action input.
This calculation shows failure of this particular dichotomy to furnish
the same new price on both branches. It is not a lower bound on the
true rough-input contribution or an obstruction to a sharper map estimate.
An alternative nondegenerate polar-mean or nonlinear dilution theorem
could improve it, but is not assumed here.

For a mean-uniform gap theorem, the limitation is visible already at
M=0: the kernel is Haar and psi_M vanishes everywhere. Geometric roughness
then has no positive gap. This is a diagnostic on the allowed mean
domain, not a constructed occurrence of M=0 for every actual lattice
history. No such occurrence is needed for the exact mass identity (B9).

## 4. Precisely when the depth test becomes a per-step test

### B-RENEW: conditional singleton summation — PROVEN implication

Let a carried lineage receive a **new** factor exp(-q_l) at step l,
and let its one-step placement, boundary, reference and norm costs be
at most `B_l=L^4 C_l exp(b_l)`. All factors refer to the same absolute
integral and full readers; no old action term is charged twice. Suppose

    theta=sup_l B_l exp(-q_l)<1.                          (B19)

Then its summed continuation weights through any positive number of
steps are at most `sum_(r>=1) theta^r=theta/(1-theta)` times its initial
weight. Proof: after r steps multiply the r bounds, obtaining at most
theta^r, and sum the geometric series. A non-branching lineage estimate
is all that is asserted here. Branching, mergers and extra types require
their summed cost in C_l or the activity theorem below.

The volume factor has an exact origin for simple support contraction:
if output supports are pi(S), the rooted sum at a coarse vertex can be
charged to its at most L^4 fine preimages. Also |pi(S)|<=|S|. Thus

    b_Y=sum_(S:pi(S)=Y) a_S,    ||b||_mu<=L^4 ||a||_mu    (B20)

for this support relabeling, provided the function suprema do not grow
and the support labels and norm rates obey these premises. A halo,
long reader, or original source label retained after contraction may
invalidate the premise; its extra cost must be proved and included.
Equation (B20) never deletes a source reader in (B4).

For fixed C_l<=C and costs with

    q(u)-b(u) >= c u^delta-d log(1+u)-b_0,
    c>0, delta>0, d>=0,                                  (B21)

the right side tends to infinity. Therefore a finite u_* can make
`q(u)-b(u)>4 log L+log C+log(1/theta_0)` for every u>=u_*,
where any chosen 0<theta_0<1 is permitted. This proves (B19) even for
n=1, with no beta-function slope in the criterion. A boundary cost
o(u^delta), or a cost of order u^delta with coefficient strictly below
the price coefficient, can be paid. Coupling-independent boundary cost
is sufficient but is not necessary for this renewal arithmetic.

By contrast, a component priced only at creation contributes the old
majorant

    sum_(r>=0) exp[(4+c_B)r log L-n c u_(K-r)^delta].      (B22)

The upper half of (B5) shows that, for fixed n and 0<delta<1, the
logarithm of its terms tends to positive infinity: a linear positive
term in r exceeds a term of order r^delta. For a final linear price
n a_eff u, the lower bracket gives the sufficient geometric criterion
`n a_eff beta_->4+c_B`. This proves only the scope of that estimate;
critical summable prefactors, variable cutoffs and response weights
remain possible, as in F17 and LFPRICE.

Equations (B19)--(B21), not simply deleting r from (B22), are the
requested replacement. B-GAP supplies such factors for fresh gap-event
lineages under the plain forward law. B-MASS prevents assigning them
to every inherited lineage just because it was re-blocked. The actual
matched all-history version of (B19) remains OPEN.

## 5. Matched boundaries and the exact role of SOFTHARD G2

### B-SEAM: normalized real comparison — PROVEN

For real V and ||M||<=1, |h_M(V)|<=1, whence
`exp(-2t)<=k_t(V;M)<=exp(2t)`. If ||M-M'||<=d, comparing integrands
inside Z_t gives

    |log Z_t(M)-log Z_t(M')|<=t d,
    |log k_t(V;M)-log k_t(V;M')|<=2t d.                  (B23)

For arbitrary simultaneous replacement of V and M, the numerator
logarithms differ by at most 2t and normalizer logarithms by at most
2t. Replacing a kernel thus costs at most 4t; deleting it in favor
of Haar density one costs at most 2t. A Wilson plaquette replacement
or deletion costs at most 2u, since 0<=s<=2.

Two integrands with identical measures and hard selectors, differing
in P plaquette factors and C kernels, therefore satisfy two-sided
pointwise domination with logarithmic cost

    D_boundary=2u P+4kappa u C.                            (B24)

Positivity preserves the domination after integration on the same
domain. Shared zero selectors cause no division by zero. Changed
supports, changed source measures or complex cancellation are not covered.

This is the finite-cost wild-data mechanism of SOFTHARD G2, rebuilt
including the field-dependent normalizers. It makes a seam comparison
finite even where a hard constraint could have no compatible fiber.
It gives a **positive debit**. If P+C is bounded per block but nonzero,
this crude debit is of order u, and using it against c u^delta with
delta<1 leaves a negative net majorant for sufficiently large u. This
is failure of this envelope to pay for that threshold, not a lower
bound on the actual seam free energy.

The raw action can be allocated without any reference fiction. Assign
each plaquette an owner block; for n blocks with distinct interior bad
witnesses charge a fraction 0<theta_c<1 of their owned terms. The
charged energy is at least theta_c epsilon^2 n/(2N), and the rest is
nonnegative. Overlap multiplicity m changes the fraction to theta_c/m.
This is an exact split of the original action. On integration it leaves
the uncharged integral divided by Z_A still to estimate. Reusing that
charged fraction at the next step without a new effective-action
decomposition is not a second charge. At effective levels the
decomposition itself is a named required input.

### B-MATCH: cancellation at a matched boundary — PROVEN implication

Suppose two local expansions, on the same domain and reader graph, have
logarithmic coefficients f_X^+ and f_X^- and local prefactor logs v_X^+
and v_X^-. They are actually the two integrals to be compared. Their
nonzero empty-support prefactors must either agree or have their ratio
kept as a separate reference debit; it is not bounded by (B25). Define
G_boundary to be the difference of the displayed supported logarithms.
Suppose

    sup_x sum_(X contains x) sup|f_X^sign|<=q,
    sup_x sum_(X contains x) sup|v_X^sign|<=b,

and every coefficient agrees for X missing the complete boundary reader
set Bdy. The difference then has only supports meeting Bdy, so

    |G_boundary|<=2(q+b)|Bdy|.                             (B25)

Proof: charge each differing support to one of its vertices in Bdy and
upper-bound by the sum over all such vertices; use both signs and both
coefficient families. This is coefficient cancellation of constructed
logarithms, not cancellation of nearby geometry. Uniform q,b and a
bound |Bdy|<=c_partial n would give a uniform per-step boundary debit.
Weighted tails are allowed only with a proved summed reader estimate in
place of that cardinality bound. The actual f^sign,v^sign for (B3) have
not been constructed by B-SEAM.

For a complex reference a(z,y), even the elementary estimate is

    |int a L exp(G)dy / int a dy|
       <= int |a L exp(G)|dy / |int a dy|.                (B26)

If factors are separated, `T_ref=int|a|/|int a|` must be paid. On two
points, weights (1,-1+d), 0<d<1, and multiplier (exp(h),1) give ratio
`1+(exp(h)-1)/d`. Thus a bounded real-pointwise seam cost says nothing
uniform about this complex ratio without cancellation control. This
finite diagnostic is not an asserted zero of Z_A.

For coarse polar continuation V=W exp X, X Hermitian traceless,
||X||<=alpha, the real exponent change of the holomorphic kernel is
`(t/N) Re tr[(cosh X-I)W^*M]`. The positive matrix cosh X-I has trace
at most N(cosh alpha-1); trace duality proves

    |k_t^C(W exp X;M)|<=exp[t(cosh alpha-1)] k_t(W;M).     (B27)

For c_link n kernels this costs kappa u c_link(cosh alpha-1)n in
an absolute numerator. For fixed rho and kappa u>=1, a width
alpha=rho/sqrt(kappa u) has bounded per-link cost, since
cosh x-1<=x^2 cosh x/2. A fixed alpha>0 has an
order-u debit. This is not zero-freeness of a normalized denominator,
nor original-source analyticity or continuation of a moving hard cut.
FR and KR below must cover those separate issues on the same D_*.

## 6. Joint integration before logarithms

### B-JOINT: overlap grouping and its sufficient budget — PROVEN implication

Let a finite family of atoms a_i have nonempty supports S_i in a
product of normalized local measures mu_x. Parameters range over D_*;
the local measures have holomorphic densities against fixed dominating
measures, atoms are holomorphic, selectors are fixed in these
coordinates, and local uniform absolute envelopes justify integration.
Expand the exact finite product integral

    Z=int product_i(1+a_i) product_x dmu_x.                (B28)

Any nontrivial global selection condition must itself be represented
with all its readers, or supplied with an explicit componentwise
factorizing coefficient and the corresponding joint bound below.
Unvisited normalized cells are integrated out before taking absolute
values. Suppose for **every selected set I**, including overlaps,

    int |product_(i in I) a_i| d|mu_(union S_i)|
                                      <=product_(i in I) alpha_i,
    Q=sup_x sum_(i:x in S_i) exp[(mu+2)|S_i|] alpha_i<=1/4. (B29)

If coefficients are present, include the complete coefficient inside
the absolute integral. They must factor across overlap components.
The empty selection coefficient is one. Each component coefficient
reads only that component's union of supports; include any extra readers
by enlarging supports before grouping.
They must also be parameter-independent or holomorphic on D_* with the
same local uniform integration envelopes; boundedness alone is insufficient.
Reference total variations of visited cells are already in (B29).

For each selected set I, form the graph connecting i and j when
S_i intersects S_j. Its connected components are unique. Product
integration factors **between those components**, because they read
disjoint coordinate sets and coefficient selection factors there.
Integrate each complete connected component to a weight w_C. These
weights are an exact hard-core gas with supports union_(i in C) S_i.
This proves the integration/factorization identity before taking a log.
In particular a small-field cluster reading a large region belongs to
that region's component; a shared boundary reader joins both regions.

Here is a reconstruction of the two convergence estimates. Put
v_i=exp[(mu+1)|S_i|]alpha_i and b_i=exp[(mu+2)|S_i|]alpha_i.
Connected selections with a marked atom are bounded by rooted overlap
trees; allowing repeated labels only enlarges the positive bound.
Their exponential recursion is

    T_i=v_i exp(sum_(j:S_j intersects S_i) T_j).

Since the sum of b_j over that overlap is <=Q|S_i|, b_i is a
supersolution. Iteration from zero proves T_i<=b_i. Mark an atom whose
support contains the root and use |union S_i|<=sum|S_i|. The rooted
gas norm at exponent mu+1 is at most Q.

For its logarithm the connected alternating graph coefficient has
modulus at most the number of spanning trees. To see this without an
external tree theorem, totally order the edges. Kruskal's algorithm
assigns a connected graph its unique minimum spanning tree T. For fixed
T, allowed extra edges are exactly those larger than every edge on
their T-path. Hence graphs with that T form an interval [T,R(T)].
Their signed sum is `(-1)^|T|(1-1)^|R(T) minus T|`, of modulus <=1.
Sum over T, and use the same tree recursion for polymers, spending the
remaining unit of support exponent. It bounds the connected log norm
at mu by Q. Repeated polymer labels are included in logarithmic tuples;
root marking changes 1/m! to 1/(m-1)!.

This constructs nonvanishing as well. Multiply all original atoms by a
complex parameter z. The bounds still hold for |z|<=2 with 2Q<=1/2.
The exponential of the convergent connected series agrees with the
finite gas near z=0 by its formal expansion. Analytic continuation gives
equality throughout that disc; at z=1 the gas is nonzero. The stated
holomorphic densities, atoms and envelopes are needed for holomorphy
in D_*, separately from analyticity in this artificial z.

An empty-support scalar is outside (B29); it must be extracted and
shown nonzero with its own local log accounting. This prevents hiding
a denominator zero or an extensive vacuum factor in Q=0.

The exact algebra (B28) is available even on original Haar coordinates:
write each action/kernel/indicator factor as 1+(factor-1) and retain its
full readers. But this is not a small expansion. A nontrivial hard cut
has sup|chi-1|=1, so its elementary single-atom sup majorant already
exceeds 1/4 after support weighting. An integrated reference can do
better; it is its actual joint (B29), not the formal identity, that is
still required for (B3).

For clarity, separate marginal estimates cannot replace this grouping.
With y=+1 or -1 of equal probability and a_1(y)=a_2(y)=epsilon(1+s y),
0<s<1, the joint integral is epsilon^2(1+s^2), while the product of
integrals is epsilon^2. Their connected difference epsilon^2 s^2 has
no distance decay if y is a shared remote reader. Closing that reader
before integration is essential.

Suppose a constructed family of integrated types has charged size n,
full support <=c_s n, and joint absolute weights after normalization,
boundary and continuation debits at most exp(-nu_j n). If the sum of
type coefficients at each root and size is <=A^n, then

    r_j=A exp[(mu+2)c_s-nu_j],
    Q_large,j<=r_j/(1-r_j),  provided r_j<1,
    nu_j=tau_j-c_ref,j-t_ref,j-c_partial b_partial,j
                       -kappa u_j c_link(cosh alpha_j-1). (B30)

This is a geometric sum starting at n=1. The inequality is conditional
on a bound for the **joint absolute integral**; multiplying scalar
estimates obtained under different laws does not prove it. If the input
price is already on the complex domain, omit the last debit. A
small-field atom budget <=1/8 and r_j<=1/9 give Q<=1/4. Thus the
one-step gas can include singletons and all sizes, provided the same
reference and full-support bounds hold. A static count of shapes is
not A for integrated histories. In particular c_s has not been proved
uniform for a persisting component carrying old source readers.

## 7. Returns, failed returns and depth-uniform iteration

### B-EXTRACT: why a return must include renormalization

Even a tiny constant per fine site is amplified by L^4 in one block.
Over K steps it gives a sum with weights L^(4(K-j)); it cannot be
left in a purported uniformly bounded irrelevant activity. At each
step the exact identity must instead extract all required relevant
and marginal local coefficients, including vacuum and coupling terms,
and carry their explicit recursion. Ordinary Taylor subtraction alone
is an identity, not a norm estimate or identification of all gauge and
boundary operators.

A useful limited calculation shows what the positive mechanism would
be. Let F(z) be holomorphic on the ball ||z||<R of a finite-dimensional
complex curvature space, bounded by M, with Taylor terms of degrees
0,1,2 zero. Along every complex radial line the one-variable maximum
principle applied to F(wz)/w^3 gives

    sup_(||z||<R) |F(a z)|<=a^3 M,  0<a<1.

One can prove the bound first on smaller closed balls and pass to R.
For the explicitly defined ideal dilation
`D_L F(z)=L^4 F(L^(-2)z)` this yields

    ||D_L F||<=L^(-2)||F||.                               (B31)

This elementary holomorphic contraction is PROVEN for that operator.
It is not an identity for the actual fluctuating, boundary-dependent
RG map. The latter needs its sea average, derivative terms, source
terms, gauge identities and re-extraction before (B31) is usable.
It supplies a concrete alternative to fresh event prices without
pretending that merely transporting a centered activity contracts.

### B-ITER: sufficient per-step invariant bound — PROVEN implication

Here is an explicit return contract that includes every failed small
component. At each step keep an exact partition of each attempted
return into its successful sector, newly gap-priced continuation,
and remaining completion/chart/coherent-input failures. Include all
crossing small-field clusters before making that partition. Require
the output expansion and reference to satisfy B-JOINT on the same D_*,
with all relevant coefficients extracted exactly. All constants and
majorants below are nonnegative, with B>0 and M>0. In one fixed full
norm, suppose the combined residual norm x_j satisfies

    x_(j+1)<= (lambda+B s_j+eta_j)x_j+C x_j^2+B epsilon_j. (B32)

The terms have precise separate jobs:

- lambda controls the returned irrelevant linear map after extraction;
- s_j bounds the genuinely newly priced continuation per unit input;
  B includes its rooted re-blocking and reader costs;
- eta_j controls **all** remaining failed-return sectors per unit input;
- C x_j^2 bounds nonlinear overlapping groups in the same expansion;
- epsilon_j bounds newly generated activities, with their reference
  and full-support costs already paid.

This is an assumed operator estimate, not a consequence of a scalar
probability bound. In particular B-GAP alone proves neither s_j in this
complex norm nor eta_j. No failed singleton is omitted by a size rule.
Alternatively its exact contribution can be absorbed into another
displayed term, but only with that term's proved bound.

Suppose constants are uniform in volume, depth and admitted history,
0<=x_0<=M, s_j<=s_*, eta_j<=eta_*, epsilon_j<=epsilon_*, and

    theta=lambda+B s_*+eta_*+C M<1,
    B epsilon_*<=(1-theta)M.                              (B33)

For x_j<=M, (B32) is <=theta x_j+B epsilon_*<=M. Induction proves
the invariant bound for every finite K, with the sharper estimate
`x_j<=theta^j x_0+B epsilon_*(1-theta^j)/(1-theta)`.
This proof is independent of beta_±. All five ingredients must be
derived from step j's representation without assuming closure at later
levels. A future-conditioned reference must be included in a separate
ordered induction; it does not inherit the plain-chain estimate (B12).

If s_* and epsilon_* tend to zero like exp(-c u_*^delta) after their
debits, B,C are bounded uniformly, and 1-lambda-eta_* has a fixed
positive lower bound, choose M small enough to reserve that margin
and then u_* large enough. This makes (B33) feasible for singletons.
This is the positive per-step
alternative to the freezing test. If a coherent failed singleton is
simply transported with no extracted contraction or new charge, there
is no justification for a small eta_*. B-MASS identifies the missing
estimate in that prescription. Increasing its support without paid
new blocks does not repair it.

An implementation must also update vacuum and marginal coefficients
with the actual output values, preserve the required source/coarse
domain, and prove the flow bracket when it is consumed. (B33) bounds
only the specified residual norm. It does not by itself bound those
coefficient recursions or establish a physical mass gap.

## 8. Disposition of the five clauses and comparison

| LF-JMBR clause / per-step counterpart | Status on the actual model | What is proved here and what remains |
|---|---|---|
| 1. Exact local representation and common reference | **OPEN**; raw finite representation **PROVEN** | B-RB re-blocks exact sectors and keeps every reader and normalizer. A local adapted representation agreeing with the particular Z_A off the affected boundary, with the actual charts and cuts, is not constructed. |
| 2. Charged joint price and matched boundary | **OPEN** | Bare charge allocation, B-GAP and B-GEOM's smooth-input branch are PROVEN. B-SEAM is finite but its crude debit is too expensive for the sublinear threshold. B-MATCH and B30 are PROVEN implications. The coherent-input branch and the same-reference joint bound are missing. |
| 3. Common nonzero complex reference and TV | **OPEN** | B27 is only a raw numerator envelope. B-JOINT constructs a nonzero reference conditionally on its holomorphic joint atoms and budget. Those inputs for R_h and Z_A, including FR/KR coverage and local TV, remain unsupplied. |
| 4. Joint integration, factorization and summed full supports | **OPEN** at the required quantitative scope; exact overlap algebra **PROVEN** | B-JOINT integrates complete overlaps before logarithms. Its algebra works formally on Haar coordinates, but the actual small A,c_s and alpha_i on a matched reference are not obtained. Boundary and original-source readers cannot be discarded. |
| 5. All returns, all failure alternatives and next-step estimates | **OPEN**; proposed induction **ARGUED** | B-RENEW and B-ITER prove the per-step sufficient criteria, and B31 proves an ideal dilation contraction. The actual extracted operator, coherent-failure bound eta_j, relevant coefficient recursion and invariant full domain/norm remain to be built. |

The whole lemma is OPEN, rather than five separately discharged walls.
For example a successful common-reference expansion could establish
clauses 2--4 together, including zero-freeness. The analysis does not
establish their logical independence or greater difficulty than Route A.

No JMBRA brief or report was found in the provided snapshot or a targeted
filename search under `/Users/jonBridger/ym4d-lanes`. The user was asked
for its location during the work. Pending such an input, the following
is a comparison with the **creation-price/frozen-component architecture
specified in LFPRICE**, not a report on an unseen JMBRA result.

| Issue | LFPRICE frozen-component comparator | Route B attempted here |
|---|---|---|
| Where large fields live | A creation-level region retains a forward cone; small components return. | Every current region is integrated/reclassified at the next level; its dependence survives in activities and readers. |
| Arithmetic if all estimates exist | One creation price pays L^((4+c_B)r); linear price requires the strict sufficient n a_eff beta_->4+c_B. | Repeated new prices pay one factor L^4 per step as B19; returned residuals instead use B33. No slope appears in these two criteria. |
| Sublinear threshold / singleton | Fixed-size sublinear majorant B22 fails. A variable cutoff n(u) of order u^(1-delta) or different response weights remain alternatives. Critical prefactors can repair the separate linear-price equality case. | A new price c u^delta beats fixed per-step entropy. The inherited rough-mean/failed-return branch has not been shown to earn it or contract. |
| Boundary and denominator | Matched boundary logs, all-cut ratios and complex TV are needed. | They are still needed, now at every transition with an invariant activity norm. The finite G2 envelope is not sufficient by itself. |
| Failed small return | Must return, join actually paid blocks, or obtain a sufficient separate history price. | Must enter a controlled successful, newly priced, or coherent-failure term of B32. Relabeling it at the next step is no estimate. |
| Result reached | LFPRICE supplies raw substeps and conditional summation; full LF-JMBR OPEN. | Adds the exact renewal distinction and conditional per-step induction; full LF-JMBR OPEN. |

LARGE55 is a method proposal, not an independently established instance
of this new induction. In fact its section 6.3 still freezes large
components and uses a creation-price history sum; E13 restores a boundary
cost. Its review F2/F3/F9/F10 preserves the geometric, normalization,
complex-reference and failed-return gaps. RLARGE v3 already distinguishes
in-step returns from frozen history prices; REVIEW_RLARGE_V3 S-1/S-2
requires a separate future-tilt bridge. These distinctions are preserved
here rather than treating a renamed induction as a proved simplification.

## 9. Named inputs, remaining construction and evidence limits

The coordinator inputs are requested only at their exact supplied scopes:

- **FR:** an invariant original-source radius and coarse/chart domain for
  these actual sector integrals and predicates, including boundaries.
- **KR:** the finite-coupling interaction, prefactor, contour and remainder
  bounds for the correctly normalized action (B2), including inherited
  activities and every boundary reader.
- **TC:** original-law local charging and joint tails under the actual
  reference needed in (B29)--(B30), with exterior and total-variation
  costs. A plain forward tail on another law does not supply this.

No result of those active lanes is extended or rederived here. Their
existence at a selected-sector scope does not establish these stronger
all-history matches.

**ARGUED next concrete construction:** take one current connected region
and its complete boundary/source readers. In the actual step (B6), split
its next bad output using B16. Keep the rough-input term as an explicit
activity, integrate it with every incident small-field cluster, and
construct the matching Z_A reference and its log on that same sector.
Extract the returned local vacuum/quadratic and any other required
relevant operators after the prescribed sea integration. The decisive
quantity is the norm of the remaining rough-input and completion-failure
operator, eta_j in B32, together with its same-reference boundary/TV
debit. A bound making B33 invariant would turn the conditional singleton
mechanism into an actual per-step proof. At present neither its local
reference nor that operator estimate is supplied.

There is no exhausted-route or physical no-go claim. The contradictions
proved here concern repeated pricing of transported total positive mass
and deriving a complex ratio from a real envelope alone. The failing
estimates B22, the crude G2 debit and the eta_1-threshold charge are
explicitly insufficient majorants, not lower bounds on Yang--Mills
weights. Matched cancellation, stronger geometric regularity, scale
dependent component rules, and renormalized irrelevant contraction remain
live. No numerical experiment was used. Source and file checks are
bookkeeping; the fresh hostile review is separate evidence with its
scope recorded in the log.
