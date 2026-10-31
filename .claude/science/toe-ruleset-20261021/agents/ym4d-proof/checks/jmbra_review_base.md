# JMBRA — reader-closed soft-kernel integration and the matched return

**LF-JMBR remains OPEN on the actual uniform RD3 reference.** This note
constructs the exact real-sector representation, proves how to integrate
selected reader groups before taking a logarithm, and gives a weighted
version that retains arbitrarily long readers. The estimates needed to
make those groups small on `R_h/Z_A` are not supplied by kernel
normalization. An explicit positive-measure completion-failed singleton
also prevents silently omitting the small-failure branch.

PROVEN labels a mathematical statement with the hypotheses displayed here;
ARGUED labels a proposed application; OPEN labels an unmet obligation.
The five-clause disposition is in section 9. No retained/audit status,
full RG induction, Yang–Mills existence or impossibility result is claimed.
Source identities, resource limits and review are in [JMBRA_LOG.md](JMBRA_LOG.md).

Credit: Tadeusz Balaban for the large-field renormalization organization and
Jonathan Dimock for its exposition in [Large fields](https://arxiv.org/abs/1212.5562)
and [Convergence](https://arxiv.org/abs/1304.0705). Those papers concern a
scalar model in three dimensions. They provide methods and attribution,
not a four-dimensional SU(N) premise. All mathematics used below is rebuilt;
no memory-only `[m]` statement carries weight.

## 1. Exact target and the two different densities

Fix N>=2, odd L>=3, a finite compatible periodic four-dimensional lattice
chain, normalized Haar measures, positive u_j and kappa. These are supplied
model data, not consequences derived here from framework axioms. Write

    s(U)=1-Re tr(U)/N,
    k_t(V;M)=exp(t Re tr(V* M)/N)/Z_t(M),
    Z_t(M)=int exp(t Re tr(W* M)/N)dW,   t=kappa u_j.       (A1)

M is the Decision-4 arithmetic mean of the specified unitary contour
transporters, so ||M||op<=1. In particular Z_t(M)>0 at real fine fields
and int k_t(V;M)dV=1. The entire normalizer is part of the kernel's reader
set: it reads every fine link needed by M. The arithmetic mean is not
replaced by an average of logarithms or a straight path.

At the two-step RD3 interface, the exact objects are

    R_h^epsilon(V)=int Xi_h exp(-S_0^epsilon) K_0 K_1 dU_0 dU_1,
    Z_A(V)=int chi_A(U_1) b_1(U_1) K_1(V,U_1)dU_1,
    b_1=exp(-u_1 sum_p s(U_1,p)),
    Q_h=R_h/Z_A.                                         (A2)

Here Xi_h is the complete earlier failure record, including absence of
other failures. All current failure records have been summed in R_h.
Thus Xi_h reads U_0,U_1, not the new V. At a general step use the same
opened earlier chain. Sources occur in the original Wilson coefficients;
they do not alter the prescribed kernels. Current V is held fixed in (A2).

The target is LFPRICE section 6, all five clauses, on the same original
source/coarse domain D_* as RD4, uniformly in volume, depth and a specified
stable admissible history/chart class. That class and its invariant budgets
are not defined by calling a history legal. RD's exact decision tree is
broader. No assertion below that uses all legal histories silently proves
uniform smallness on a smaller, as-yet-unspecified class.

A full support counts original source readers, integration cells, inactive
vertices and fixed boundary readers on the consumer's ambient block graph.
Choose connected hulls when needed and pay their actual size. Projecting a
fine source or contracting a hole does not remove that reader. A shared
boundary variable joins groups before that variable is integrated.

The named supplier interfaces are FR (fixed original-source/coarse domain
and fixed-sector maps), KR (the complete interaction/prefactor remainder),
and TC (joint original-law charges/tails with their actual exterior costs).
Their selected-sector results are not assumed to cover (A2). No active
coordinator calculation is repeated or strengthened here.

## 2. An actual all-cut representation without a support division

**PROVEN — finite algebraic part of clause 1.** Set
rho_h(U_1)=int Xi_h exp(-S_0^epsilon)K_0 dU_0 and J_h=rho_h/b_1.
Division by b_1 is harmless on real U_1 because b_1 is strictly positive.
No division by chi_A or by a possibly zero history mass is made.

For each B subset A use its G_2 components Y, where G_2 joins blocks at
periodic sup-distance at most two. Interior variables I(Y), Wilson
readers P(Y), and output-kernel readers C(Y) of separated components are
disjoint: each kernel contour stays in its two endpoint blocks and each
plaquette has nearest-neighbor support. Their radius-one collars are
disjoint. Allocate the original factors once as

    b_1 K_1=W_out product_Y w_Y,
    w_Y=exp(-u_1 sum_(p in P(Y))s_p) product_(c in C(Y))k_c,
    C_Y(eta,V)=int chi_Y w_Y dU_I(Y),
    dnu_A=chi_A b_1 K_1 dU_1/Z_A.                        (A3)

The remainder W_out reads no replaced interior. At every real eta,V,
C_Y>0: an open product cap of interior links near identity satisfies the
interior plaquette cuts, and w_Y is strictly positive. Each cut threshold
is positive. A source-independent lower bound exists at finite volume;
no useful uniform lower bound is inferred here.

With fresh replacement coordinates Uhat define the JOINT operation

    T_B J_h=(product_Y C_Y)^(-1)
       int zeta_B(Uhat) product_Y w_Y(Uhat;eta,V)
           J_h(Uhat_I(B),eta) dUhat_I(B).                 (A4)

For B empty use T_empty J_h=J_h. Then exactly

    Q_h^epsilon(V)=E_nu_A sum_(B subset A) T_B J_h.       (A5)

Proof. In the B summand the function T_B J_h is independent of the old
coordinates U_I(B). Their integral against chi_B product_Y w_Y in nu_A
is product_Y C_Y, cancelling precisely the denominator in (A4). The
remaining integrand has chi_(A\B), the new bad interiors zeta_B, W_out
and the complete inherited density b_1 J_h. Summing the disjoint identity
product_(Q in A)(chi_Q+zeta_Q)=1 proves (A5). Compact Haar domains,
bounded real kernels and finite source sets justify Fubini, also at
complex original sources with V real. No success-only gas has replaced
the sum. A zero-mass history gives a zero summand throughout.

There is also a representation entirely in product Haar coordinates:
lift Z_A to (U_0,U_1) by integrating a dummy Haar U_0. Its integrand is
chi_A b_1 K_1; the numerator integrand is Xi_h exp(-S_0^epsilon)K_0 K_1.
Common factors such as K_1 agree literally. All other differences remain
explicit, including the entire inherited density versus b_1. There is no
claim that these differences occur only near the named bad component.
Every primitive action/kernel factor has its original finite reader set.
The gauge change of variables here is the identity: Haar is unchanged and
no gauge determinant is inserted or discarded.

For explicit predicate factors, fix a history prefix and, for every
nonempty connected candidate Y in its active set, put

    b_Y=(product_(Q in Y)zeta_Q)
        (product_(Q in N_2(Y)\Y, Q active)chi_Q)(1-a(Y)).
    I_F=product_(Y in F)b_Y product_(Y notin F)(1-b_Y).   (A6)

a(Y) is the actual size/completion indicator. On a configuration b_Y=1
exactly for a maximal bad component which fails that test. Hence I_F is
one exactly for the specified complete failure list. Its product over
levels is Xi_h. Every completion reader and every absence factor stays
in (A6); candidate supports need not be small. Alternatively the exact
chi/zeta sector sum used in (A5) can be kept without expanding (A6).
These are finite sums and local-coordinate integrals, not a pointwise
ratio between measures with different hard supports.

**OPEN application boundary.** (A5) performs the exact reference matching,
but the law nu_A is interacting and T_B acts on a joint J_h. In general
T_B J_h is not a product over Y. A reference containing the inherited
density is a different reference from Z_A. The proofs below specify
precisely when further factorization and smallness become valid.

## 3. Reader closure as an exact integration algorithm

**PROVEN — elimination with all incident factors.** Consider finitely many
integration variables with product Haar (or a stated product of local
measures), and a product of bounded factors. To integrate a variable x,
multiply every current factor reading x, integrate that product in x,
and replace those factors by the resulting function. Its reader set is
the union of their readers minus x, together with all parameter readers.
Record the original support before removing the integration coordinate.
Fubini proves this operation exactly; induction proves the full algorithm.
If another factor later reads a resulting message, it belongs to the next
group. Integrating two factors separately which both read x is a different
operation and is not licensed by this identity.

For a paired numerator/reference elimination use the same order and
factor allocations. Mark every unequal primitive factor, measure or
selector. A new message is identical in the two integrals whenever every
factor entering it was identical. This follows by integrating identical
functions against the same measure. Thus equality propagates outside the
dependency closure of the marked inputs. A closure can reach the whole
lattice; the algorithm proves no uniform diameter or size bound.

Here is the sharper use of the normalized soft structure. Let C be a
finite set of integrated vertices of a directed acyclic graph. A vertex
v has one probability kernel p_v(dx_v|x_par(v),y); roots have normalized
Haar. y denotes fixed outside variables. For Decision 4, each output link
is one vertex and p_v is k_v dHaar. Internal parents precede their children.
The law

    dP_y(x_C)=product_(v in C)p_v(dx_v|parents,y)          (A7)

has mass one: integrate the latest internal vertex first and continue.
Kernels whose outputs are outside C and which read C are NOT in (A7);
they remain factors of the integrand. This distinction includes a fixed
terminal V in (A2). Positivity is used for norm bounds, not to drop factors.

For a factor f_i, let A_i be all its integrated readers and all their
ancestors within C, recursively. Its complete support H_i contains its
original parameter/fixed-field readers, A_i and all outside parents of
the kernels for A_i, represented on the original block graph. Include
any connected hull required by the consumer. In particular an outside
parent remains a reader even when all its children have been integrated.

**PROVEN — ancestral integration and grouping.** For a selected finite
collection I of such factors, let A_I=union_(i in I) A_i. Removing vertices
of C\A_I in reverse order integrates their kernels to one: no selected
factor reads them, and a child in A_I would make them ancestors in A_I.
Consequently

    E_Py product_(i in I)f_i
       =int product_(v in A_I)p_v product_(i in I)f_i.    (A8)

If I splits into overlap components I_1,...,I_m using the COMPLETE H_i,
the integrated ancestor sets of different components are disjoint and no
kernel edge joins them. A cross edge would put its parent in both closures.
The remaining product measures/kernels therefore separate, giving

    E_Py product_(i in I)f_i
                 =product_a E_Py product_(i in I_a)f_i. (A9)

Shared fixed y readers are conservatively merged by the H_i rule. If y
is integrated later, its law and every factor reading it must first be
included in the grouping; (A9) conditional on y is not that later identity.
For real probability kernels,

    int product_(i in I)|f_i| dP_y
                             <=product_(i in I)||f_i||infinity. (A10)

Proof: bound the factors pointwise and use the normalization of (A7).
It is a contraction in sup norm, not a probability estimate for a fixed
bad coarse field. Empty I has integral one. Empty-support constants must
be kept separately; a zero constant prevents a logarithm.

The reader-free forward cone is the special case I empty. The presence
of a reader f gives E_P f, not one. Wilson action terms, cuts, determinants
from a proposed chart, and past selectors are additional factors, never
normalized creators merely by notation. A kernel-only ancestor closure is
therefore insufficient if any of these factors is left unexpanded outside
the purported closure.

**ARGUED implementation on (A5).** Expand a supplied small-field factor
as 1+f_X. In each selected term attach all clusters which read the core,
their ancestors, shared variables and further selected overlaps; then
use (A8). This integrates every selected reading cluster exactly once.
Unselected factors equal one in that term because the FULL product has
been expanded, not because their dependence was ignored. Closing the core
against every possible long cluster at once could fill the whole lattice;
termwise closure avoids that operation. Establishing small input factors
for the actual interacting nu_A/J_h remains OPEN.

## 4. Exact disjoint-type factorization before any logarithm

**PROVEN — conditional algebra and quantitative theorem.** Suppose an exact
representation, possibly after sector/cell aggregation, is

    Z=sum_(I subset labels)c_I E_P product_(i in I)f_i,    (A11)

with c_empty=1. The nonempty H_i are connected full supports. Require
c_I to factor over their overlap components, including any compatibility
rules. Require the complete coefficient-weighted term on each component
to satisfy

    int |c_I product_(i in I)f_i| d|P_(A_I)|
                                     <=product_(i in I)alpha_i. (A12)

Use either (A7) with the closure property (A9), or an explicit normalized
product-cell reference with the same property. In the complex case that
property and (A12) include all local total variations; unvisited normalized
cells are integrated before taking absolute values. Constants outside
(A11) are accounted for separately. Holomorphy additionally requires fixed
selectors, holomorphic densities/factors/coefficients on one common domain,
and locally integrable envelopes. None follows merely from a norm bound.

For each connected selected set J form its integrated type

    w_J=c_J E_P product_(i in J)f_i,    S_J=union_(i in J)H_i.

Every selected set has a unique partition into overlap components.
Equation (A9) and the coefficient hypothesis factor its integral into
product_J w_J. Summing gives exactly the hard-core gas of these types;
types with the same support may be combined. This proves factorization
BEFORE taking a logarithm, including connected groups containing several
large cores. Every primitive factor in a group is integrated jointly.

Let mu>=0, sigma=mu+2 and

    Q=sup_x sum_(i:x in H_i)exp(sigma |H_i|)alpha_i <=1/4. (A13)

Then the gas logarithm exists and has full rooted norm at exponent mu
at most Q. Here is a proof, rather than a citation of LF9. Put
v_i=exp((mu+1)|H_i|)alpha_i and b_i=e^|H_i| v_i. A connected selection
with a marked label has a spanning tree of its overlap graph. Bounding
by all rooted trees, including repeated labels only in the positive
majorant, gives the recursion

    T_i=v_i exp(sum_(j:H_j intersects H_i)T_j).

The sum of b_j in this exponent is at most Q|H_i|. Starting the recursion
at zero therefore gives T_i<=b_i, since Q<=1. The exponential accounts
for unordered children with their factorials; any tree on a set of
distinct labels occurs, so the bound covers every connected selection.
Marking one constituent through x and using |union H_i|<=sum|H_i|
proves that the integrated gas norm at exponent mu+1 is at most Q.

For the logarithm, expand connected incompatibility graphs of the
integrated polymers, allowing repeated polymer labels in the tuples.
Fix an edge order. Connected subgraphs with a given Kruskal spanning
tree T are precisely the interval between T and T plus edges later than
every edge of their T-path. Their alternating sum is (-1)^|T| times a
product of factors (1-1), hence has modulus at most one. The spanning-tree
majorant and the preceding recursion with the remaining unit of support
exponent give log norm <=Q. Root marking changes 1/m! to 1/(m-1)!,
which is exactly the rooted-tree coefficient used here.

To justify the logarithm rather than presume nonvanishing, multiply every
original atom by an auxiliary z. Both majorants converge locally uniformly
for |z|<2 (indeed on |z|<=2 since 2Q<=1/2). Near zero the elementary finite
graph expansion equals the logarithm of the finite gas. The exponential
of the convergent connected series therefore equals that gas throughout
the disc by analytic continuation, so the gas is nonzero at z=1. The
parameter envelopes then give holomorphy on the specified physical domain.
No denominator in (A2) has been shown to satisfy (A13) by this theorem.

## 5. Weighted readers, including roots lying in a tail

An exponentially decaying reader is not a finite-range reader. Use its
actual connected support as an additional atom label. The next estimate
supplies a weighted alternative when there is no deterministic bound
|support|<=c_s times the number of bad core blocks.

**PROVEN — weighted grouping implication.** Fix an output exponent sigma>=0.
Let the small-field/tail atoms have weights alpha_i and full supports H_i;
let charged core atoms have weights a_gamma and full supports D_gamma.
Assume the exact coefficient factorization and joint bound (A12) for the
MIXED family. Suppose, for some eta>=0,

    q_eta=sup_x sum_(i:x in H_i)
                    exp((sigma+1+eta)|H_i|)alpha_i <1/2,
    d=sup_x sum_(gamma:x in D_gamma)
                    exp((sigma+1)|D_gamma|)a_gamma,
    q_eta+d<=1/2.                                        (A14)

Group all selected overlaps as in section 4. Let W_core be the family of
integrated groups containing at least one core, retaining their complete
supports. Then

    ||W_core||_sigma <= d/(1-2q_eta).                     (A15)

This includes roots lying outside the core. To prove it, replace alpha_i
in the positive tree bound by e^(eta|H_i|)alpha_i, and multiply every
core weight by R=(1/2-q_eta)/d, if d>0. R>=1. The first tree bound of
section 4, which needs only total input <=1, bounds the integrated norm
at exponent sigma by q_eta+Rd=1/2. Every group containing at least one
core has gained a factor at least R. Divide the bound by R to obtain
(A15). If d=0 every core term vanishes and (A15) is immediate. This
argument marks an arbitrary OUTPUT root, so it does not replace the
full rooted norm by a core-root norm.

If a group reaches graph distance at least r from the union of its core
supports, its selected small-field supports have total cardinality at
least r. Indeed an overlap chain of connected supports joins such a
vertex to a core; the length outside cores is bounded by that sum.
The extra e^(eta sum|H_i|) in the same majorant then gives

    ||W_core,extent>=r||_sigma
                         <=exp(-eta r)d/(1-2q_eta).      (A16)

Thus long readers are retained and paid, not truncated. Countably many
tail labels are allowed when (A14) and the stated integration envelopes
hold: apply the finite result and pass to the absolutely convergent
majorant. Changing the source graph or its distance needs a new check.

For comparison, for one fixed core D with weight a, the same rooted-tree
recursion at that core gives the useful anchored bound

    sum_(connected decorations) exp(sigma|union|)|weight|
                          <=a exp((sigma+q_eta)|D|).     (A17)

This follows because the sum of possible child tree weights touching D
is at most q_eta|D|. Alone (A17) is NOT a full-root estimate; (A15) is
needed for a root on a distant decoration. Neither estimate manufactures
the joint bound (A12) from separately integrated one-core probabilities.

At a fixed full-support exponent, an entire arbitrarily long tail family
can therefore fit in the LF9 criterion directly. For example, at
sigma=mu+2, a verified small-field integrated budget Q_sf together with

    Q_sf+d/(1-2q_eta)<=1/4                               (A18)

is a sufficient remaining gas budget, provided the reference and grouping
are exactly those just proved. It is not an evaluated Yang–Mills tuple.
If the consumer insists on hard bounds A,c_s,c_partial by CORE size, (A15)
is an explicit weighted alternative, not a proof of those hard bounds.
The actual model's q_eta,d and the original-reader incidence remain OPEN.

## 6. What still has to match Z_A

**PROVEN — normalization leaves a survival factor.** In a raw cone with
law (A7), let chi be the product of all retained reference predicates.
Its integrated reference is a(y)=E_Py chi, not one. If removing those
predicates leaves the uninserted raw cone, its numerator is one, and its
relative factor is 1/a(y) whenever a(y)>0. With readers F and G the
actual pair is E_P(F)/E_P(chi G). A cone identity estimates neither that
denominator nor the connected logarithm of its ratio.

This loss is already possible for a normalized Decision-4 single-link
kernel. Take SU(2), M=-I and q(V)=Re tr(V)/2. Then
k_t(V;-I)=e^(-t q(V))/Z. For 0<delta<1 choose
E_delta={q>=1-delta} and B_delta={q<=-1+delta}; B_delta has positive
Haar mass m_delta. The numerator of P(E_delta) is at most e^(-t(1-delta));
the normalizer is at least m_delta e^(t(1-delta)). Hence

    0<P(E_delta)<=m_delta^(-1)e^(-2t(1-delta)),
    1/P(E_delta)>=m_delta e^(2t(1-delta)).               (A19)

Every assertion follows by integration on those sets; positive measure
follows from nonempty open neighborhoods of I and -I. This is an
admissible mean for the one-link kernel family. It is not asserted to be
the actual all-cut good event, or to lie in the desired stable chart
class. It disproves only a universal coupling-independent reference
comparison from soft normalization alone. A matched good reference may
avoid this situation, but its proof must say how.

For any real positive reference w and positive real e^g with |g|<=a,
integrating gives e^(-a)<=int we^g/int w<=e^a. For complex w the true
bound is instead

    |int w(e^g-1)/int w|<=T_ref(e^a-1),
    T_ref=int|w|/|int w|.                                (A20)

It follows by the triangle inequality, whenever int w is nonzero. On two
points w=(1,-1+epsilon), 0<epsilon<1, and g=(a,0), the ratio is
1+(e^a-1)/epsilon. Thus finite pointwise kernel envelopes cannot set
T_ref=1. No Wilson zero is claimed by this diagnostic.

**PROVEN — the matched boundary implication, with its hypotheses.** Suppose
the two COMPLETE integrals have local logarithmic coefficients F_X^+/-
and prefactor coefficients v_X^+/-, holomorphic on the same domain. Suppose
they agree whenever their full supports miss Bdy, and, for each sign,

    sup_x sum_(X contains x)(||F_X||+||v_X||)<=q+b.

Then, by summing each nonzero difference through a vertex of Bdy,

    |G_boundary|<=2(q+b)|Bdy|.                            (A21)

If instead the available norm has exp(eta|X|), the portion reaching
distance r from Bdy costs at most 2(q+b)|Bdy|e^(-eta r), since such a
connected support has at least r vertices. This is a weighted boundary
version; it assumes the coefficients and their matching have actually
been constructed, including changed measures and all original readers.
Equal bare factors away from Bdy do not alone imply equality of integrated
logarithmic coefficients there; their eliminated dependencies must match.

For completeness, a finite halo gives an explicit depth debit. If the
height-ell boundary lies in the w-neighborhood of the L^ell contraction
of a star-connected n-block core, a spanning-tree traversal of 2(n-1)
steps can be split into pieces of length at most L^ell. Each piece meets
at most 16 contracted blocks. Thus, with V_w=(2w+1)^4,

    sum_(ell=1)^r |Bdy_ell|
       <=16 V_w r +[32 V_w/(L-1)](n-1).
    c_B=32 V_w(q+b)/log L.                               (A22)

This proves the constant in L^(c_B r); the other term is charged once
in the size budget. Initial halo containment is required. Long readers
need (A14)/(A21)'s weighted version; their existence does not establish
this finite-w premise. In particular raw k bounds only give
e^(-2t)<=k<=e^(2t): summing that O(u_j) bill over levels is not an
evaluation of a coupling-independent c_B.

**OPEN — the decisive actual inequality.** For each mixed connected group
G with n charged core blocks, a matched construction would have to prove,
under the SAME local reference and on D_*, a bound of the form

    int |complete coefficient * charged weight * readers * returns|
          d|matched local reference|
       <=exp[-tau n+c_ref n+t_ref n+b_partial|Bdy_G|],    (A23)

with the numerator continuation charged separately if not already included.
Its full weighted summed version must satisfy (A13) or (A18). tau is
earned from disjointly allocated original action terms; the remaining
reference, boundary and return factors stay INSIDE this joint integral.
No value of c_ref or b_partial for this actual integral has been obtained
by (A8). Replacing its left side by a name is not a proof of it.

**PROVEN — the direct contraction/supremum attempt fails its smallness
test.** Take product Haar roots and keep each original Wilson factor as
1+f_p, with f_p=exp(-u_0 s_p)-1, using (A10)'s supremum majorant.
Set one link of a plaquette to g=diag(-1,-1,1,...,1) and its other links
to identity. Its s_p is 4/N, so this particular majorant satisfies

    Q>=exp(mu+2)(1-exp(-4u_0/N))>1/4
       when u_0>-(N/4)log(1-exp(-(mu+2))/4).             (A23a)

Every full support is nonempty; closing ancestors can only increase its
size. Other atoms contribute nonnegative terms to Q. This evaluates the
failure of the specified, actually available sup-norm expansion, rebuilding
RD4's direct-Haar diagnostic. It does not refute joint L1 estimates or an
adapted Gaussian/interacting reference. Kernel contraction alone leaves
this order-one Wilson atom intact at weak coupling.

For charge accounting, expanding (I-U)*(I-U) gives
s(U)=||I-U||HS^2/(2N)>=||I-U||op^2/(2N). If disjoint bare bad blocks each
own a distinct interior plaquette with distance at least epsilon, charging
a fraction theta in (0,1) of their owned original action gives
tau_raw=theta u_0 epsilon^2/(2N) per block, with the uncharged action
nonnegative. If a term is owned at most m times, use theta/m instead.
This is the elementary raw allocation already in LFPRICE, not a new
original-law coercivity result. On the effective step b_1 is bookkeeping:
b_1 J_h=rho_h, so charging b_1 without estimating the compensating J_h
does not price rho_h. A TC estimate or an actual consistent effective
action construction is still required before inserting tau into (A23).

## 7. Common complex reference: the exact finite result and its limit

**PROVEN — a common finite germ for (A2).** Fix real Vbar and write
V_c=Vbar_c exp Z_c. Continue each terminal kernel with exponent
t[tr(V_c^(-1)M)+tr(M*V_c)]/(2N); the real-fine normalizer is unchanged.
All earlier fine fields remain real and integrated. The relative exponent
H of either integrand in (A2) obeys

    |H|<=r:=2u_0 sum_p|epsilon_p|
                 +t_1 sum_c(e^(||Z_c||op)-1).            (A24)

Use s<=2, ||M||<=1 and ||e^(+/-Z)-I||<=e^||Z||-1 to prove this bound.
The denominator has no source term. Fixed prior predicates do not alter
the estimate. Normalize the positive real reference at Vbar. If r<pi/2,
each e^H has real part at least e^(-r)cos r. Integration gives

    |E e^H|>=e^(-r)cos r>0,
    T_ref<=e^(2r)/cos r.                                 (A25)

Compact-domain domination proves holomorphy and the right half-plane
fixes the logarithm. Zero-mass numerator sectors remain zero rather than
being normalized. Positivity of the all-cut reference follows from a
cap with every level-one interior link near identity and positive kernels.

For a fixed source polydisc |epsilon_p|<rho_*, the sufficient bound (A24)
contains 2u_0|P_0|rho_* and therefore does not keep r<pi/2 uniformly as
volume grows. This is a failure of the sufficient sector bound, not a
proof of an actual zero. The common-domain part of clause 3 stays OPEN.
A convergent matched expansion satisfying section 4 could itself provide
nonvanishing and local TV accounting; these are not independent barriers.
Any current selector depending on V must be summed, kept on a fixed sector,
or given an exact analytic fixed-domain treatment before (A24) is used.

## 8. Small components and completion failures

**PROVEN — an actual isolated completion-failed singleton.** At one RD
stage take a block torus of side at least seven, 0<epsilon_cut<2,
0<epsilon_loc<2 and size threshold at least one. Let Q be the origin block.
Set g=diag(-1,-1,1,...,1) on an interior e_1 link at within-block coordinates
(1,1,1,1) in Q, and identity on all other links initially. Every plaquette
reading that link stays inside Q for L>=3. Q is bad and all other block
interior cuts are good.

Now put a second g on an e_1 link crossing the block boundary from block
e_2 to block e_1+e_2. Choose its transverse within-block coordinates equal
to one. Both blocks lie in N_1(Q) and are distinct from Q. A plaquette in
the e_1,e_3 plane through this crossing link lies entirely in N_1(Q) and
reads no variable in I(Q). Its other three links are identity, so its
curvature distance is two. Every plaquette affected by the crossing link
crosses a block boundary and is not an interior plaquette of any block.
Consequently the bad-block set is still exactly {Q}.

RD's completion functional is

    e_flat(eta,V;Q)=min_(Ucirc_I(Q))[
       max_(p wholly in N_1(Q))||I-Ucirc_p||op
         +max_(c in C(Q))||V_c-S_c(Ucirc)||op].            (A26)

The displayed exterior plaquette is fixed for every completion. Therefore
e_flat>=2, for every V. The singleton fails completion although its size
passes. The straight path S in (A26) is the prescribed completion map;
it is not substituted for Decision 4's mean in any kernel.

Choose a positive delta smaller than
min(epsilon_cut,2-epsilon_cut,2-epsilon_loc)/8. Vary every link within a
delta operator-norm cap. Telescoping the four unitary factors bounds every
plaquette change by 4delta. All the strict cut and completion inequalities
persist. The product cap has positive Haar mass, and the finite Wilson
weight and all soft kernels are strictly positive. Thus this is a
positive-measure failed-singleton sector, including at fixed real V.

This witness concerns RD's legal-history class. A stable chart class may
exclude the rough exterior plaquette, but must state that exclusion and
handle its complement. The exterior action can also provide an extra
charge; no claim is made that it cannot. Enlarging the geometrical support
without allocating that action is not such a charge.

**PROVEN — exact return partition, OPEN — its estimates.** For each bad-set
sector, sort its connected components by n<n_0 or n>=n_0, and integrate
the former jointly with their selected readers by sections 2–4. This is
an exact finite regrouping whether a chart completion succeeds or fails.
Split each small sector into its actual successful and failed-completion
indicators. Both pieces remain; their sum is the original piece. Exact
integration of the failed piece does not make its normalized activity
small, nor does it put its output in the small-field chart.

A completed construction must assign EVERY n<n_0 failure one of:
an estimated return, a merger into a sufficiently large genuinely charged
component, or an extra suppression paying its own depth sum. Define these
dispositions by a disjoint partition, not by a choice made after dropping
an inconvenient term. The witness above proves that the completion-failed
branch of RD's decision tree cannot be discarded on size grounds alone.

Here is the exact price test. Supply the actual-chain lower bracket
u_(K-r)>=v+beta_- r log L-R_0, beta_->0. After all costs suppose frozen
types of n charged blocks have total weight at depth r bounded by
A_0^n L^((4+c_B)r)e^(-n a_eff u_(K-r)), a_eff>0. Put

    n_0=floor((4+c_B)/(a_eff beta_-))+1,
    z=A_0 e^(-a_eff(v-R_0))<1.

Substitution of the bracket and two geometric sums prove

    sum_(r>=0,n>=n_0) weights
       <=z^n_0/[(1-z)(1-L^(4+c_B-n_0 a_eff beta_-))].     (A27)

Polynomial creation costs must already be paid: for a_0>a_eff and d>0,
u^d e^(-a_0 u)<= [d/(e(a_0-a_eff))]^d e^(-a_eff u),
by maximizing d log u-(a_0-a_eff)u. For d=0 use constant one. No spent
price is reused when choosing n_0. A small unreturned failure of size n
does not meet (A27)'s lower-size premise; an additional per-depth exponent
lambda_r would need n a_eff beta_-+lambda_r/log L>4+c_B with a strict
uniform margin if its extra weight is e^(-lambda_r r).

For a sublinear net price q_net(u)~c u^delta, delta<1, a fixed n_0 has
no such guarantee. A variable cutoff satisfying
n_0(u)q_net(u)>=a u, a beta_->4+c_B, yields
sum_(n>=n_0(u))e^(-n q_net(u))<=e^(-a u)/(1-e^(-q_net(u))).
A uniform positive lower bound on q_net pays that denominator. Uniform
return estimates up to the growing cutoff and their full-reader norms
are still required. This is an alternative, not an exhausted route.

Finally let F_ret denote a legitimately constructed connected return log
and let L_rel be an explicitly specified local projection onto the
required relevant/marginal operators. The algebraic split
F_ret=L_rel F_ret+(1-L_rel)F_ret is exact; it proves no RG estimate. What
is still needed is the actual symmetry-compatible projection, matching
vacuum/coupling terms and a bound such as

    ||(1-L_rel)F_next||_sigma
       <=lambda ||F_input,irr||_sigma+B_generated,
    lambda<1,  B_generated<=(1-lambda)h_*.                (A28)

No L_rel, lambda or B_generated satisfying (A28) on the actual history
family has been produced here. Even a source-independent returned vacuum
term cannot be discarded: repeating a fixed nonzero per-block term over
levels weights it by the number of blocks at each level. One-step
smallness and mass preservation do not imply the required scale induction.

## 9. Clause-by-clause disposition and exact next task

| LF-JMBR clause | Status | What was proved and what remains |
|---|---|---|
| 1. Exact representation, matching untouched factors, support sectors | **PROVEN at the finite algebraic level.** | (A3)–(A6) use actual R_h/Z_A, explicit Haar/replacement integrals, full original factors and disjoint sectors; zero masses stay zero. The identities hold at every finite step. They do not claim a bounded-size reference-cell construction or the uniform complex domain required in clause 3. |
| 2. Joint charged/reference/boundary estimate | **OPEN.** | The exact integrals and weighted sufficient estimates are specified. (A23) and its rooted sum are unproved for the actual reference. Kernel normalization leaves the reference survival factor; (A19) rules out obtaining a universal bound from that property alone. |
| 3. Common nonzero complex reference and local TV | **OPEN.** | (A24)–(A25) prove only a finite germ. (A13) would prove more if instantiated. The fixed-volume sector estimate fails the uniform-radius test; FR/KR/TC are not promoted to all-history inputs. |
| 4. Integrated overlap types, factorization, summed full supports | **OPEN as a complete actual-model clause.** | (A8)–(A12) prove exact factorization for complete ancestral groups and coefficient rules; (A14)–(A18) pay long readers and roots in their tails under a joint norm. Actual small coefficients, matched references and their full-reader budgets remain unconstructed. No deterministic c_s by core size is asserted for arbitrary tails. |
| 5. All small returns, failed alternatives and next-step extraction | **OPEN.** | The exact partition and positive failed-singleton witness are proved. (A27) is the final-price criterion, not a verified price for those failures. The alternative charges/mergers/returns and the quantitative extraction (A28) remain unproved. |

The complete LF-JMBR lemma is therefore not supplied. The new constructive
content is the ancestral integration/factorization rule, its weighted
full-root estimate and the explicit legal failed-singleton sector. The
algebra in section 2 rebuilds RD's existing identity for this application;
the generic graph estimates are not claimed as novel general mathematics.

**ARGUED next concrete task.** On a bounded core, construct a paired local
reference for (A4), retaining the exterior plaquette branch of section 8
and all selected ancestors from section 3. Produce a joint bound (A23)
with explicit original-reader weights satisfying (A14), for both the
successful and failed completion pieces. Its data must include the
inherited-versus-bare comparison; omitting that comparison changes Z_A.
Then test (A18) and the final-price rule using only the remaining charges.
This is a substantial unresolved construction, of comparable strength to
the missing joint part of LF-JMBR, not a minor lemma renamed as progress.

## 10. No-Go Discipline Gate — partial attempt, no exhaustion claim

**N1.** The actual attempted family is the soft-kernel elimination/reader
route, with strict closure and weighted selected tails as two variants.
A paired Gaussian/conditional reference and a connected-cumulant treatment
of the interacting all-cut law remain live alternatives. Smooth sector
partitions could change boundary derivatives; they are untested here.
These are not five exhausted families. No negative-packet PASS is claimed.

**N2.** The obligations are not counted as independent walls. Let J mean
the matched joint norm/representation (clauses 2/4), Z the common complex
domain (3), and R the invariant return/extraction (5). J on a specified
complex domain with (A13) implies nonvanishing there, hence that part of Z.
Z alone does not here establish J. R includes J/Z at subsequent steps;
one-step J or Z does not here establish R. The J–R and Z–R reverse
implications beyond those definitional inclusions remain unresolved.

**N3.** Explicit hypotheses are finite supplied model, correct creator
normalization, complete ancestry, fixed analytic selectors, coefficient
factorization, joint TV majorants, original connected supports, actual
coupling bracket and final allocated charges. None is obtained from its
name. No approved framework primitive is used as an analytic estimate or
classified as a missing physical axiom.

**N4.** RD3's mandatory-event diagnostic concerns normalization: for
p=P(E)>0, int|1_E/p|dP=1, so its weighted small-atom test cannot be <=1/4.
That identity is rebuilt here and does not attack an unnormalized joint
return. CODEX_REVIEW_LARGE F2/F9 concerns cone readers, matching and spent
prices; sections 3, 6 and 8 retain those exact issues. LIB1's full-support
qualification concerns filled inactive regions; the present weighted
estimates count all such readers rather than invoking an active norm.

**N5.** (A19) is a one-kernel-family inference diagnostic; (A20) a finite
complex-measure diagnostic; (A26) an actual one-block legal-history witness;
(A24) a finite-lattice sufficient-domain estimate. None proves a
modewise, continuum, physical-spectrum or all-route obstruction. No
numerical result or unexecuted check is reported as passed.

**N6.** Exact support sectors, a matched adapted reference, a changed
mathematical norm with proved consumer compatibility, or an extra paid
failure branch require mathematics, not a new axiom. (A15) already supplies
a conditional positive route around literal finite reader closure.

**N7.** Strongest live counter-route to any broad negative conclusion:
construct the actual all-cut conditioned local law, match its smooth
quadratic part and all prefactors, and expand the remaining readers using
(A8)–(A18). Cancellation of common coefficients may reduce the crude
O(u) boundary bill to (A21), and the exterior witness in section 8 may
supply an additional usable charge. Proving those joint estimates and
the subsequent extraction could close the route. Nothing here excludes it.

**N8.** LFPRICE/LF7–LF10, RD3/RC1–RC3, RD4/L1–L10, LIB1's inactive-term
proof and SOFTHARD/G1–G2 already preserve these reference/norm boundaries.
The inspected reader-closure search also found weighted critical-field and
Hessian elimination work with different objects; those are not a matched
history-return theorem. No complete repo/literature novelty or exhaustion
claim is made. Source locators and search scope are recorded in the log.

Scientific status: `open`; claim type: `positive_theorem`; contribution:
`upstream_support`, partially closing the exact construction. Independent
review does not confer retained status. No axiom, ledger, existing source
or editable prompt is modified, and no commit is made.
