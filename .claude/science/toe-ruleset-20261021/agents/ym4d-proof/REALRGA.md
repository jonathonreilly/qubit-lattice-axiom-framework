# REALRGA — a real Taylor-seminorm RG induction contract

**A precise replacement contract is specified below. Its elementary real
calculus and conditional cluster/induction implications are PROVEN here;
its realization for the actual gauge theory is OPEN.** In particular, real
positivity resolves nonvanishing on admitted positive fibers. It does not
resolve local normalizer derivatives, mixed-reader prices, or extracted
continuation. The proposed construction is ARGUED as a research route.

PROVEN means the written statement under its displayed hypotheses, not an
audit verdict. CARRIES below means that a source result retains its original
scope in the proposed real contract; it does not upgrade that scope.
This is an author specification, not a Yang–Mills existence or mass-gap proof.
The source snapshot is `cd67e1c9e6bbed8b92fee069de66ef0b25486316`.
[The log](REALRGA_LOG.md) records the freshness limit, evidence and review.

Credit: the method precedent is Bauerschmidt–Brydges–Slade,
[Introduction to a renormalisation group method](https://arxiv.org/abs/1907.05474v2),
Chapter 7, especially Definition 7.1.2 and the Taylor/product calculus;
and Brydges–Slade, [Gaussian integration and normed algebras](https://arxiv.org/abs/1403.7244v2),
Definition 3.3, Proposition 3.7 and its section 5.1 proof. Those works
treat different field spaces. The ordered SU(N) derivatives, normalization
and sufficient real Mayer argument used here are rebuilt below. We choose
Mayer expansion, not an assumed gauge-theory circle-product theorem.
Tadeusz Balaban's large-field organization and Jonathan Dimock's
[Large fields](https://arxiv.org/abs/1212.5562) and
[Convergence](https://arxiv.org/abs/1304.0705) are also credited; those
expositions concern scalar d=3. No recalled [m] item carries proof weight.

## 1. Fixed objects and the exact task

Fix N>=2, odd L>=3, a finite compatible periodic four-dimensional lattice
chain, probability Haar, positive u_j, kappa and t_j=kappa u_j. Use exactly
the supplied Decision-4 arithmetic contour mean M_c(U), with ||M_c||op<=1:

    s(U)=1-Re tr(U)/N,
    k_t(V;M)=exp[t h_M(V)]/Z_t(M),
    h_M(V)=Re tr(V* M)/N,
    Z_t(M)=int_SU(N) exp[t h_M(W)]dW.                 (RGA1)

These are supplied model data, not newly derived physical axioms. At a
step retain the actual objects of JMBRA A2/CHARGE C2:

    R_h(V;J)=int rho_(j,h)(U;J) K_j(V,U)dU,
    Z_(j,A)(V)=int chi_A(U) b_j(U) K_j(V,U)dU,
    b_j(U)=exp[-u_j sum_p s(U_p)],   Q_h=R_h/Z_(j,A).  (RGA2)

rho contains the opened earlier chain and its entire history, including
absences of failures. It is not b_j. All current outcomes are summed when
R_h denotes the unselected transfer. Zero-mass histories remain zero
summands. A conditional law is used only on its nonzero fibers.

J denotes **original** action coefficients and inserted real observables.
For an observable source, every RG kernel, its normalizer, and its prescribed
coupling are held fixed. E.g. K4MATCH (6) is u_0(p)=u_0-h_z(p).
Differentiating a retuned kernel computes a different observable. A separate
flow-parameter derivative, when required, must explicitly include whatever
kernel dependence its definition has; it is not identified with this J
derivative. Jet weights below are frozen while taking derivatives.

All statements range over the finite volumes, levels, admitted boundary
data and histories specified by the eventual producer, with constants
uniform in those quantities. A stable admissible class and the exact
disposition of its complement must be exhibited, not defined as "the
histories on which the desired estimates hold." Uniformity in N or L is
not claimed. FR, KR and TC remain named inputs from the coordinator:
real domains/sector regularity, full interaction/prefactor estimates, and
original-law charges/tails, respectively. Their selected-sector results
are not assumed to cover all of (RGA2).

## 2. The norm, regulators and localization data

### 2.1 Real fields and derivative order — definitions

Work on real group variables and an open real evaluation domain D_j^R,
with all stated uniform jet bounds on that domain. Declare closed inner
evaluation sets and their margins inside D_j^R. Sources still
read their original labels. Exterior fields, inactive regions, past
readers, and all kernel normalizer readers remain in the supported data.
For charts use U_b=Ubar_b exp(a_b), a_b in su(N), inside a specified
injective real chart with a positive interior margin. Complements use
the original Haar variables. No global principal logarithm is assumed.

Set p=6 as the **chosen total field derivative order**, and q=4 for the
initial finite-source contract. For an all-order consumer use the compatible
family q=0,1,2,..., not a conclusion inferred from q=4. No theorem here says
six field derivatives suffice for every RG localization mechanism.

Let D_f,A and D_c,B be right-invariant derivations along the fine and coarse
link arrays, respectively. For example D_f,A F(U,V)=d/dt F(exp(tA)U,V)|0.
The fine arrays include every still-retained earlier-level field. Their
direction norms are max_b ||A_b||op/h_level(b), with
h_l=sqrt(N/u_l); the coarse norm uses h_(j+1). These are choices of
dimensionless derivative units, not fluctuation estimates. Sources have
a declared norm max_a |v_a|/r_(q,a), r_(q,a)>0, in ORIGINAL source units.
For general smeared directions retain their exact linear coefficient map.
The r_(q,a) are jet weights, not certificates of an analytic radius. Their
inverse powers and any q or cutoff dependence are never discarded.

Write |F|_(a,b,c;x) for the supremum of ordered derivatives
D_f^a D_c^b D_J^c F(x) on unit directions, and define

    T_x^(p,q)(F)=sum_(a+b<=p, c<=q)
                         |F|_(a,b,c;x)/(a! b! c!).      (RGA3)

Directions within one group are ordered, not silently commuted; fine,
coarse and source derivations commute across their different variables.
Local coordinate versions use ordinary real Frechet derivatives and pay
the actual chart-change constants. The norm includes mixed fine/coarse/
source derivatives. Restriction to one field species is allowed only
after that species has really been integrated out.

For n specified original-source directions also carry the labelled version

    T_x^(p;[n])(F)=sum_(a+b<=p) sum_(B subset [n])
        (product_(i in B) r_i)/(a! b!)
                   sup |D_f^a D_c^b partial_B F(x)|.    (RGA4)

Here partial_B means one differentiation in each labelled direction.
Directions may coincide if repeated derivatives are wanted. At n=4 all
15 nonempty subsets are retained. There is no 4! in extraction of the
distinct-label coefficient. (RGA3) gives a possibly coarser factorial
upper bound; it never changes that coefficient identity. All jets are
jets of the SAME real functions and project consistently when labels or
orders are removed. Derivative neighborhoods stay inside D_j^R;
no fictitious source cube extending outside it is used.

### 2.2 Field-size regulators and complete supports — definitions

Choose deterministic local owner blocks for plaquettes and kernel links;
enlarge a support to include every reader of its owned factors. One explicit
nonnegative smooth real energy on these variables is

    E_j(B)=sum_(p owned by B) u_j s(U_p)
            +sum_(c owned by B) t_j[1-h_(M_c(U))(V_c)]. (RGA5)

Earlier retained levels have the corresponding terms. On a declared real
chart one may additionally use sum_(b owned by B)||a_b/h_j||HS^2, with
the chart, reference frame and its entire support recorded. This optional
term is not extended across an undeclared logarithm branch. Curvature
control alone does not control gauge directions or holonomies.

For a finite nonnegative multiplicity vector m=(m_B) and a fixed a>0 set

    G_j(m;x)=exp[a sum_B m_B E_j(B;x)],
    ||F||_(T/G_m)=sup_(x in D_j^R) T_x(F)/G_j(m;x).     (RGA6)

Use m=1_X for a basic activity; overlapping products retain m+n, not
1_(X union Y). Thus these are a family of regulated spaces. Since
G_m G_n=G_(m+n), their product maps into the sum-multiplicity space.
Even at order zero F=G_(1_X), H=G_(1_X) have regulated norms one while
FH/G_(1_X)=G_(1_X). The single-regulator norm is not a Banach algebra
on overlaps. There is no inference of a regulator integral bound from
positivity or from the word "large field."

Use the complete connected supports X of RD4/JMBRA on the chosen ambient
block graph, with the graph and all original-reader assignments fixed.
An inactive vertex is a root like any other. If a geometric projection is
used during reblocking, preserve the original argument labels and pay the
complete resulting reader set and any connected hull. No fine source is
replaced by a new coarse source. Define the unregulated output norm

    ||F||_(mu,p,q)=sup_x sum_(X contains x) exp(mu|X|)
                           sup_(D_j^R) T^(p,q)(F_X),    (RGA7)

and the analogous labelled and regulated input norms. mu>0 is fixed along
the claimed induction. A connected support spanning distance d has
|X|>=d+1, so (RGA7) pays a spatial decay cost in that graph's units.
Physical-distance and cross-scale conversions must be stated separately.
Long readers are separate supported terms with summable weights, not
silently truncated. The two cluster stages below spend two units of
support exponent; that reserve must be regenerated at the next step.

The Mayer theorem uses **unregulated integrated jets** in (RGA7).
Regulators are a device for proving its joint input bounds. If an output
regulator is first retained, its full supremum must be debited before
using that theorem. On a small chart E_j(B)<=E_* this costs
exp(a E_* sum m_B); on unrestricted fields E_* may grow with u_j and
does not give a uniform small activity. This choice avoids hiding the
overlap problem in the cluster algebra.

## 3. Library of real replacements

### RGA-P: product, derivatives, and composition — PROVEN

Leibniz for an ordered word of m derivations distributes its positions
between the two factors, preserving their order. Taking suprema gives
the binomial convolution. Division by a!b!c!, followed by summation on
the downward-closed set a+b<=p, c<=q, gives

    T(FH)<=T(F)T(H),
    ||FH||_(T/G_(m+n))<=||F||_(T/G_m)||H||_(T/G_n).    (RGA8)

For (RGA4), distribute each labelled source between the factors; the
products r_B multiply exactly for disjoint subsets. Dropping the
nonnegative terms with repeated labels on the right proves the same
inequality. This also proves T(exp F)<=exp(T(F)) and
T(exp F-1)<=exp(T(F))-1 by absolute convergence of the exponential
series in the finite jet algebra. It gives **direct** bounds on every
included derivative. It supplies no derivative of order outside the
specified set and no estimate from a value bound alone.

For real coordinate maps Psi the chain rule iterated m times is

    D^m(F o Psi)[v_1,...,v_m]
      =sum_(pi partition [m]) D^|pi|F(Psi)
                    [D^|B|Psi[v_i:i in B] : B in pi]. (RGA9)

Induction proves this: the next derivative either joins one of the
existing blocks by differentiating Psi there, or creates a singleton
by differentiating F. Bounding every factor proves the corresponding
finite Bell-polynomial bound. In group coordinates the local vector-field
coefficients and their derivatives are included in Psi's constants.
No Cauchy estimate is used. A source-independent change of field variables
preserves total field order p and source order q. A source-dependent
critical-field substitution can require field order p+q; it is forbidden
in the p=6 contract unless that enlarged hierarchy and its estimates are
explicitly carried. Fixed original Haar coordinates avoid that loss.

### RGA-Z: positivity, real logs, and normalized differentiation — PROVEN

Since |h_M|<=1, e^-t<=Z_t(M)<=e^t, and e^-2t<=k_t<=e^2t.
The integrands are smooth on the compact real group. A positive real tilt
preserves a positive integral on every fixed positive-measure sector.
The all-cut denominator in (RGA2) has such a sector: a sufficiently small
open identity cap satisfies its positive interior cuts. General history
fibers require their own nonempty-support witness; zero fibers are never
divided by. Consequently the real logarithm exists there, and the
normalized real measure has TV=1. Uniform inverse, local log and derivative
bounds do not follow. Nor is positivity asserted for a signed activity or
for a log-MGF after arbitrary nonlinear source counterterms.

For a fixed-domain representation Z(y)=int w(y,x)d lambda(x)>0, suppose
all required derivatives are dominated on real compact parameter sets.
Here w may contain fixed nonnegative selectors. Then

    D E_nu F = E_nu DF + E_nu[F D log w]
                                  - E_nu F E_nu D log w. (RGA10)

The log score is evaluated on the positive support. Alternatively use
derivatives of w itself at its zeros. Differentiating the quotient proves
the formula. In particular D_J log Z and its higher original-source
derivatives are real cumulants when the tilt is linear. For a word I,

    D_I log Z = sum_(pi partition I) (-1)^(|pi|-1)(|pi|-1)!
                                product_(B in pi)(D_B Z/Z). (RGA11)

Order inside each block is inherited from I. The formula follows by
induction from D log Z=(DZ)/Z and Leibniz; for commuting source labels it
is also the coefficient of log(1+w) in t_i^2=0. It includes all normalized
measure derivatives. Bounds on |D_B Z|/Z, not positivity alone, bound it.
For inverses, differentiate Z Z^-1=1 and solve for the highest derivative:

    D_I(Z^-1)=-Z^-1 sum_(empty!=B subset I)
                              (D_B Z) D_(I\B)(Z^-1).   (RGA12)

These are finite direct estimates through the chosen order; no logarithm
branch or complex circle is involved. They can have large constants.
For the single kernel they establish finite smooth jets without selecting
a polar maximizer, even at M=0. Uniform local, large-u and inherited-history
budgets are the OPEN KR/normalizer inputs.

For a positive real Gaussian matrix Q=Q0^(1/2)(1+A)Q0^(1/2), A symmetric,
||A||<1, diagonalization and the real scalar geometric-series integral give

    log det Q=log det Q0+sum_(m>=1)(-1)^(m+1)Tr(A^m)/m.

This is a real log-determinant replacement. Its local matrix expansion,
positive gap, chart Jacobian and derivative bounds remain explicit inputs;
positivity of the Haar integral does not prove positivity of a proposed
gauge-fixed Hessian or determinant.

### RGA-I: integrate the differentiated reference as well — PROVEN implication

Let n_y=w_y/Z_y be a normalized density against a fixed measure, with the
regularity and domination just stated. Leibniz and differentiation under
the integral give, in the external-field/source jet norm,

    T_y(int F_y n_y d lambda) <= int T_y(F_y n_y)d lambda
                                 <= int T_y(F_y)T_y(n_y)d lambda. (RGA13)

For the same actual normalized reference and every selected atom set I,
put A_I(y)=c_I(y) int product_(i in I) f_i(y,x) dnu_y(x).
A sufficient regulator certificate is

    T f_i<=a_i G_(m_i),   T c_I<=c_I^#,
    sup_y int G_(sum m_i) T_y(n_y)d lambda <=R_I,
    c_I^# R_I product_i a_i <= product_i alpha_i.       (RGA14)

It implies sup_y T(A_I)<=product_i alpha_i. Measures, Jacobians, selector
boundary terms and normalizers belong to this inequality, including any
derivative of a changing reference. Coupled inputs must be integrated
jointly. Unvisited normalized cells are integrated to 1 **before** absolute
values or estimates; all their nonzero-order derivatives then vanish.
No extensive product of unused differentiated-density bounds is inserted.

The certificate is sufficient, not necessary. One may prove the complete
integrated jet bound directly, benefiting from cancellations. Conversely,
separate scalar prices or separate regulator moments do not prove it.
Original action fractions allocated to charges and regulator absorption
must sum to at most the available reserve, including prior expenditure.
RGA14 for the actual mixed groups in (RGA2) is **OPEN**.

Fixed integration sectors need not be smooth in integrated variables to
differentiate external parameters. But a hard cut involving a retained
fine/coarse field is not C^6 across its boundary. It cannot be placed in
(RGA3) as a differentiable small atom. Sum such selectors before taking
those jets, or use an exact real domain decomposition/partition of unity
and bound every resulting boundary term. Interiors alone are insufficient
if the operator crosses the boundary. Such a uniformly local construction
for all completion histories is **OPEN**; zero fibers and moving masks
cannot be removed by choosing a real domain.

### RGA-C: real Mayer expansion with finite jets — PROVEN implication

Assume an exact finite representation

    Z_red(y)=sum_(I subset labels) A_I(y),  A_empty=1.   (RGA15)

Each atom has a nonempty connected full support H_i. Require A_I to be C
through the chosen mixed orders on D_j^R, to read only
union H_i, and to factor EXACTLY over the overlap components of I.
This is an identity of functions, hence of their jets. It follows from
product-cell or complete-ancestor integration only when all extra
coefficients, fixed-output kernels, shared boundary variables and future
integrations are included. The actual interacting nu_A is not declared
a product measure. Suppose

    sup_(D_j^R) T(A_I)<=product_(i in I) alpha_i,
    Q=sup_x sum_(i:x in H_i) exp[(mu+2)|H_i|]alpha_i<=1/4. (RGA16)

Then Z_red=exp(sum_X F_X)>0, with real C^(p,q) coefficients and
||F||_(mu,p,q)<=Q (and likewise for the labelled norm).

Proof. Group each selected set into its unique overlap components C,
and use w_C=A_C as the integrated hard-core polymer weight with support
union_(i in C)H_i. Factorization proves the gas identity before a log.
Set v_i=e^((mu+1)|H_i|)alpha_i and b_i=e^((mu+2)|H_i|)alpha_i.
The positive rooted-tree recursion

    T_i=v_i exp(sum_(j:H_j meets H_i) T_j)

has supersolution b_i, since the child sum is <=Q|H_i|. Iteration from
zero bounds the sum of all overlap trees; allowing repeated labels in
this positive bound only enlarges it. Root an atom through x and use
|union H_i|<=sum|H_i|. The integrated gas has norm at mu+1 at most Q.

For its logarithm sum connected incompatibility graphs on polymer tuples,
including repeated polymer labels and 1/m!. Totally order the possible
edges. Graphs having a fixed Kruskal spanning tree T form the interval
between T and T plus the edges later than every edge on their T-path.
Their alternating sum is (-1)^|T|(1-1)^(number of optional edges), of
modulus at most one. The tree bound therefore applies once more, spending
the remaining unit of support exponent. Marking a root changes 1/m! to
1/(m-1)!, giving the claimed supported log bound. RGA8 controls jets of
every product, so this is also uniform convergence of every included
derivative, not only of values. In particular the series converges in
C^(p,q) on every compact subset of the open real domain; no smooth
extension beyond a closed set is inferred from bounds only on that set.

To identify the real logarithm without assuming nonvanishing, multiply
A_I by z^|I|. Both majorants converge absolutely for real |z|<2, since
2Q<=1/2. The formal exponential of the connected series equals the finite
gas: expansion of the exponential partitions each graph into its connected
components. Absolute convergence permits regrouping these power series
and proves equality throughout |z|<2. At z=1 the exponential is positive
and its exponent is the unique real logarithm. This auxiliary counting
series requires no complex physical-source or coarse-field estimates.
Countable atom families follow by absolute convergence with the same
local bounds. A separate empty-support prefactor is NOT bounded by Q;
its sign, real log and all source dependence stay explicit.

### RGA-L and RGA-E: locality and extraction

**RGA-L — OPEN actual producer.** Generate (RGA15) on the actual matched
reference using explicit complete-reader atoms. Long tails must have
their summed jet weights in RGA16, or the weighted-reader construction
of JMBRA A14–A18 with its same mixed jet hypothesis. Exact elimination
multiplies every factor reading the variable before integration and
keeps its original support in the resulting message. This elementary
Fubini rule is PROVEN; its small local weights are not.

STEP55 CX's decoupling Cauchy estimate differentiates once for every added
box. That order is unbounded as support grows. Six field derivatives and
four source jets do not replace it. One permitted real route supplies
a real localization decomposition and proves its full summed jet bound
directly. Another uses repeated real fundamental-theorem-of-calculus
interpolation but must supply all required bond-derivative orders, their
domain compatibility and summable support costs. Neither is established
here. The Mayer theorem begins AFTER this input, not before it.

**RGA-E — PROVEN ideal benchmark; OPEN actual operator.** In a real
curvature chart, F with degree 0–2 jets zero has
|F(x)|<=|x|^3 sup||D^3F||/6 by Taylor's integral remainder. For p>=3,
on a ball of radius R, use the zero-jet norm

    |F|_(irr,p)=max_(3<=r<=p) R^r sup||D^r F||/r!.

It is a norm on that zero-jet subspace, and controls its lower derivatives
by Taylor integration. For the ideal dilation D_L F(x)=L^4 F(L^-2 x),
every term scales by L^(4-2r)<=L^-2, on a smaller input ball. Hence
|D_L F|_(irr,p)<=L^-2 |F|_(irr,p). This replaces the maximum-principle
benchmark of JMBRB B31, without identifying it with the RG map.

The actual extraction Loc_j must specify all vacuum, curvature-quadratic,
source, boundary and other relevant/marginal operators allowed in its
claimed sector, commute with the required symmetries, and retain their
coefficients and recursions. A formal degree-two subtraction does not
identify this list, a running coupling or the interacting contraction.
Real integration must also keep the linear residual, quadratic mismatch,
Haar/chart Jacobian, cut normalization, determinant and inherited density
exactly once. With no contour change E_side=0; this describes a newly
proved real representation, not deletion of an old contour-side term.
Every real complementary sector E_comp remains.

## 4. The step-to-step contract IH_R(j)

The following is a **proposed induction hypothesis and transition test**.
Fix p=6, q and all source weights, domain margins, graph conventions,
mu, a and budgets BEFORE iteration. A family of such hypotheses with
compatible jets is needed when q is unbounded.

| Clause | What is carried at level j | Actual status |
|---|---|---|
| H0: exact state | Unnormalized history densities, all-cut references, complete selectors, and an exact real chart/Haar representation of the same original generating function. Positive fibers are named; zero fibers are zero. All vacuum/source scalars are retained. | Finite transfer algebra CARRIES; admissible local representation OPEN. |
| H1: smooth jets and domains | RGA3/RGA4 on D_j^R, fixed original source coordinates, real interior margins, any chart-change/selector derivatives and the rescaling h_j to h_(j+1). | Definition PROVEN; invariant regularity OPEN. |
| H2: regulators and reserves | Regulated fine/coarse activities with multiplicity labels, disjoint original-action allocations, and RGA14 or a direct complete integrated-jet estimate on the actual reference. | Calculus PROVEN; uniform estimates OPEN. |
| H3: local expansion | Exact overlap factorization, all normalizers and past/future readers, sufficient support reserve mu+2, and Q_(j,q)<=q_*<=1/4. Prefactor log = an explicit scalar plus supported terms of norm <=b_q; an unlocalized source scalar has its own budget. | RGA-C PROVEN implication; matched atoms OPEN. |
| H4: extracted output | Relevant coefficients v_j, specified Loc_j and residual K_j with x_(j,q)=\|\|K_j\|\|_(mu,p,q)<=M_q. Unreturned sectors remain in the state with their references. | Representation/extraction/actual bounds OPEN. |
| H5: transition | Complete returns, new gaps and coherent/chart/completion failures satisfy RGA17 below in the SAME full norm. Reblocking, source weights, regulator conversion, hole costs and localization losses are included in its constants. | Invariance arithmetic PROVEN; operators OPEN. |
| H6: source and consumer records | Compatible marked jets, coefficient normalization and target errors; for all-order/symmetry consumers the additional modules in section 6, including outer expectations and the common sequence. | Finite jet identities PROVEN; uniform modules OPEN. |

Let lambda_q control the returned irrelevant linear operator, s_(j,q)
the genuinely new-gap continuation after matching, eta_(j,q) ALL remaining
failures, e_(j,q) the newly generated input, and B_q,C_q>=0. Require
lambda_q>=0, M_q>0, and, uniformly over the claimed family,
0<=s_(j,q)<=s_*q, 0<=eta_(j,q)<=eta_*q, 0<=e_(j,q)<=e_*q,
with finite nonnegative starred bounds. Require

    x_(j+1,q) <= (lambda_q+B_q s_(j,q)+eta_(j,q)) x_(j,q)
                              +C_q x_(j,q)^2+B_q e_(j,q),
    theta_q=lambda_q+B_q s_*q+eta_*q+C_q M_q <1,
    B_q e_*q <=(1-theta_q)M_q,       x_(0,q)<=M_q.      (RGA17)

Constants may depend on q, N and L but not on the claimed volumes, depth,
history or cutoff. The scalar/labelled source units are included in them.
For all q their growth must additionally meet section 6's all-n bound;
separate finite constants do not suffice. Sources of order q may not be
discarded or estimated by order q+1 at each step without carrying that
higher hierarchy. No endless derivative-order or source-radius loss is
allowed. Likewise support-rate losses cannot be iterated indefinitely.

H3 must be checked for the NEW integrated reference and action, not copied
from the preceding step. b_q and the relevant coefficients need their
own explicit recursions, including the flow bracket if consumed. If a
hole saturation is used, include LIB1's stronger input rate and bounded
hole constant, or prove a compatible alternative; an arbitrary history
does not supply a uniform maximum hole size.

**Induction implication — PROVEN.** If H0–H6 hold initially, the exact
transfer and extraction reproduce H0–H4,H6 at the next scale with their
same declared bounds, and the transition constants satisfy RGA17, then
IH_R holds for every finite depth. Indeed RGA-C supplies the local log
and jets for H3; RGA17 gives x_(j+1,q)<=theta_q M_q+B_q e_*q<=M_q.
Ordinary induction completes the assertion. The demanding premise is the
uniform transition/representation theorem, not this arithmetic. This
note does not assert it for (RGA2).

An alternative continuation clause, at the same fixed norms, is a uniform
m-window bound ||C_(j+m-1)...C_j||<=theta<1, prefix bounds B0 for lengths
<m and return bound D. For r=qm+s the product norm is <=B0 theta^q,
so the continuation sum is <=mB0/(1-theta), and returns cost at most D
times this. Alternatively a common creation envelope
||C_(j+r-1)...C_j A_j||<=a_r with sum_r a_r<infinity controls both each
birth's lifetime and past-birth accumulation at a fixed output. A separate
per-birth lifetime sum is insufficient for that second conclusion.
These norm statements are real versions of CHARGE C24–C25a and RENEW R20;
none supplies the actual coherent margin. Original creation prices are
not operator contractions on arbitrary insertions.

## 5. Carry-over map of the eight requested RG-core units

The map is at each source's stated scope, including its open clauses.
"OBSOLETE" means not required by THIS real contract; the original
complex theorem and any consumer of it are unchanged.

| Unit and located results | Disposition for IH_R | Reason and surviving obligation |
|---|---|---|
| CHARGE C5–C12: one-use allocation and actual real filled-tube/all-cut comparison | **CARRIES** | Positive real estimate with the coupling/cut and j>=j_* conditions intact. Exponentially many original cells pay this extensive family. C13's volume debit still does not provide a local mixed jet price. |
| CHARGE C15–C23: bare saddle/sector algebra, complete continuation, normalized future tilt | **CARRIES** | Real identities, including the negative bare Hessian direction and the surviving reference factor. No smooth arbitrary-background Gaussian is inferred. |
| CHARGE C14,C24–C26: joint prices, extracted windows or both creation sums | **NEEDS-REWORK** | Replace the complex norm by H1–H5, including all differentiated references. Actual local estimates remain OPEN; its scalar real C11 is not a jet estimate. |
| RD3 sections 1–2,5,7–8: nonzero witness, exact normalized transfer, matched comparison and full-factor bookkeeping | **CARRIES** on its real scope | Retain history mass, exterior inverse, all prefactors, additive complements and zero children. All-history uniform budgets remain OPEN. |
| RD3 section 3's finite complex sector/germ and complex-TV debit | **OBSOLETE** as requirements | RGA-Z gives real nonvanishing on admitted fibers. Local real log derivatives and moving-sector regularity need H1–H3; finite positive lower bounds do not close them. |
| RD3 section 4 D14–D16: integrated hard-cut species and normalized mandatory-event diagnostic | Finite real algebra **CARRIES**; quantitative joint jets **NEEDS-REWORK** | Full overlap events and their common product reference remain. A selected event of mass p has normalized insertion 1_E/p of L1 norm one, so its old price cannot be reused. Differentiating retained-field cuts requires RGA-I's explicit treatment. |
| RD3 section 6 D22–D23 hole transfer | **CARRIES** as a Banach-valued fixed-mask inequality; derivative acquisition **NEEDS-REWORK** | The full norm costs 730 at rate 649mu or 1+297 exp(81mu) at the same rate for that specified hole. Use already controlled real jets; no new derivative follows from values. |
| RD4 C1–C4, L1–L4: mandatory extraction, positive cells, exact split and matched real ratio | **CARRIES** | Mandatory mass is spent once; zero fibers and differing hard supports stay explicit. Fixed real positive cells have TV=1. |
| RD4 C6–C9,L6–L8,K1–K3,I1–I4: gas, price, normalized comparison and induction | **NEEDS-REWORK**, with the real algebra CARRIES | Use RGA13–RGA17 with jets. Remove only the genuine complex-TV/polar-continuation debit; retain reference, boundary, entropy, support and numerator costs. Exact final integration is still required before logs. |
| RD4 L5 and the complex domain/contour portions of B2 | **OBSOLETE** in IH_R | Real chart/domain control and all complementary sectors replace their roles; existing contour identities are not partially reused with sides deleted. |
| JMBRA A3–A12: actual replacement, reader elimination, ancestral grouping, coefficient factorization | **CARRIES** | Holds before logs and includes fixed-output kernels. Positive normalized kernels integrate to one only when unread. Real differentiation adds RGA13–RGA14. |
| JMBRA A13–A18: two tree bounds and weighted readers, including roots in tails | **CARRIES** as norm-algebra implications; actual inputs **NEEDS-REWORK** | RGA8/RGA16 provide the real jet version. A14's mixed bounds, complete roots, rates and all reader costs remain. A23's matched estimates are still OPEN. |
| JMBRA A19–A23b: reference survival, matched boundary/tail bounds, charge comparison and bulk source response | **CARRIES** at its real/conditional scope; local joint jets **NEEDS-REWORK** | Kernel normalization does not remove a retained cut's survival denominator. Matching must include the integrated bulk/source remainder; a bare equality away from the core is insufficient. A23a tests only the specified direct-Haar supremum expansion. |
| JMBRA A24–A25 finite complex germ; complex contour costs | **OBSOLETE** requirements | Replaced by positive real fibers plus separate local derivative budgets. Completion-failure witnesses and A27/A28 price/extraction obligations CARRY at their original scope. |
| JMBRB B-RB, B-MASS, B-GAP, B-GEOM, B-RENEW, B-SEAM, B-MATCH | **CARRIES** at their scopes | Reblocking cannot reprice old mass; fresh gap estimates are plain-forward-law bounds; rough coherent inputs and matched boundaries remain. Their scalar estimates alone are not jet estimates. |
| JMBRB B-JOINT,B30,B-ITER | **NEEDS-REWORK** in their hypotheses; grouping/invariance CARRIES | Real jet-integrated bounds replace holomorphic joint bounds. eta_q still includes every coherent/completion failure. Uniformity and relevant recursions are still OPEN. |
| JMBRB B27 polar cost; B31 maximum-principle proof | **OBSOLETE** requirements | RGA-E gives only the corresponding ideal real-dilation benchmark. It does not establish the actual operator contraction. |
| RENEW R-LIN,R-FLUX,R-TUBE,R-CAP,R-EXACT | **CARRIES** at their scopes | Linear localized dilution, coherent finite-horizon persistence, nonuniform compact-kernel return and finite integration identities remain. No uniform plain-forward renewal margin is manufactured. |
| RENEW R-WINDOW,R-GROUP and RENEW-MATCH(m) | Window arithmetic **CARRIES**; actual matched jet construction **NEEDS-REWORK** | RGA-C and H5 give the real sufficient interfaces. The original complex-reference requirement is OBSOLETE here, while operator and mixed bounds remain OPEN. |
| LFPRICE LF1,LF2, real LF3,LF4–LF8,LF10–LF11 | **CARRIES** at their stated real/raw/conditional scopes | Correct threshold units, once-only charge, finite normalized seams, geometry, cutoff arithmetic and fresh-gap caps remain. A failed scalar majorant is not a no-go. LF3's real Taylor bound does not prove the full mixed seminorm bound. |
| LFPRICE LF9 and LF-JMBR clauses 2–5 | **NEEDS-REWORK** | RGA14–RGA17 replace the analytic inputs. The real price is nu_R=tau-c_ref-c_partial b_partial, with regulator/jet costs included in these debits or alpha, never omitted. Complex polar/TV-only terms are OBSOLETE. Clause 1's finite exact representation CARRIES. |
| LIB1 parts A–C, L3–L15 and full-norm correction | **CARRIES** for real jet-valued coefficients, fixed masks | Triangle inequalities are Banach-valued. Full output costs 9M at input rate (1+8M)mu; retaining inactive terms costs 1+9M. Real jets commute with fixed regrouping. The corrected evidence includes inactive roots. |
| LIB1 L16 Cauchy derivative acquisition | **OBSOLETE** as a proof step; **NEEDS-REWORK** as an estimate | Replace it by input real jets and RGA8–RGA9. The regrouping creates no derivatives. Unbounded holes, moving masks and the actual normalized sea/failure input remain OPEN. |

For LFPRICE/RD4's bounded-support type count the real sufficient test is

    r_R=A_type exp[(mu+2)c_s-nu_R] <1,
    exp(h_sf) h_sf + r_R/(1-r_R) <=1/4.               (RGA18)

h_sf and nu_R must now pay the complete jet and regulator cost under the
same matched law. With long readers use their summed actual supports,
not an unproved c_s. All derivative/hole conversions are performed before
claiming this test. The table does not assert any evaluated YM tuple.

## 6. Consumer check and the additional output modules

The output of H0–H5 is a real local finite-jet expansion. It is not by
itself a matching theorem, a continuum limit or a symmetry proof. H6 has
the following explicit modules; all their actual-model estimates are
**OPEN**. These are obligations to carry/verify, not silently assumed
consequences of the word "RG." They specify exactly how to finish the
real interfaces in REALONLY's section 1 table.

**JETS (finite orders).** Carry the conditional original-source log
Phi_j=log E[exp(sum z_i O_i)|U_j] and all its marked jets
J_(j,B)=partial_B Phi_j(0;U_j). Conditional expectations and cumulants
in the following identity use the unperturbed actual chain. For a
nonzero source base point its corresponding tilted law would be required.
Real conditional expectation and the finite nilpotent log identity give

    J_(j+1),B=sum_(pi partition B)
                     kappa(J_j,C:C in pi | U_(j+1)).   (RGA19)

Initially J_(0,{i})=O_i and every higher distinct-source jet is zero for
the stipulated linear tilt. Apply the same identity at the final outer
integration. Singletons and
triples remain; averaging only the inner connected jet is insufficient.
RGA13 includes the measure derivatives used when estimating these identities.
Different actual histories are summed with their masses before any
unconditional conclusion. Source-dependent vacuum terms contribute.

**HIER (all orders and separation).** Choose one of REALONLY R8 or R9,
with constants independent of n and cutoff. In the R9 version the marked
state must control, for EVERY partition pi of n original labels,

    |kappa_outer(kappa_cond(B):B in pi)|
      <= A^n |pi|! product_(B in pi)(|B|!)^p0
                                product_i wbar(delta_i),
    wbar(r)=min(r,1)^-4[log(2+1/min(r,1))]^q0.         (RGA20)

The displayed condition is for n>=2, 0<a<=1, and placements with
min_(i!=j)|x_i-x_j|>=c_*a for a fixed c_*>0. It concerns the centered
scalar field in the Z(a)=1 convention of REALONLY, with first moment zero.
Here p0,q0>=0, A fixed, delta_i is the nearest other insertion distance.
The condition includes singleton conditional means and the actual outer/LF law.
This module must be propagated or established at the final unconditioned
stage; uniform q-by-q constants M_q alone do not establish it. Repeated
same-test raw MGFs of the clover are not postulated. Source windows may
shrink only with their losses paid in RGA20. Include the scalar point
bound |e_hat_a|<=C_X a^-4 and the common convergent hierarchy, or use the
separately specified multiplet/SP_lambda extension of REALONLY section 4.

**MATCH2/MATCH4.** In the actual physical normalization, compare the
marked jets to the specified Gaussian running-coupling reference, with
absolute summed errors. Carry the degree-two total error of WITNESS E11
or its per-scale E12 envelopes, and a degree-four error
|partial_1234(L-L_run)(0)|<=C u^-theta4 for
X_r=u lambda^4 O_r. The error is a derivative estimate, not merely a
small real value error. Retain the terminal covariance and all lower
subset errors needed by RGA19. These are matching inputs of full strength;
positivity and cluster convergence give no matching coefficient or sign.

**EUC and FLOW.** Include real extensive sources for every whole product
used in the flat pressure argument, with NC, PC and COMMON; or the sphere
IMG-K, CD-K, ST and BULK/ALG on their actual laws. These are different
observable families from linear coefficient tilts. For flow include the
real curvature Hessian, remainder and continuity estimates, causal
recursions and the separate spatial variational kernel when consumed.
Such sources and errors must be present in the exact generating functions;
exponentiating a nonlinear product is not licensed by moments of a linear
field. Reflection positivity and the common limiting algebra/sequence are
separate structural inputs, not consequences of positive probability.

| REALONLY consumer | Exact real output needed and implication | Status |
|---|---|---|
| H_reg / OS0, E0' | HIER gives unconditional R8. Total cumulance and sum_pi \|pi\|!<=2^(n-1)n!, followed by the moment expansion, give R8 with b0=p0+2. With its small-separation point bound, collision-flat Taylor order 5n and an integrable weight give \|S_n(F)\|<=C^n(n!)^b0 \|F\|_(10n+1); hence s=11, beta=p0+3 and fixed alpha as in REALONLY section 4. Common convergence is still required. | **PROVEN conditional interface; OPEN HIER.** q=4 does not suffice. |
| PL-1L / WITNESS | MATCH2 gives \|sum_i(D_i-Lambda_i)\|<=C u_k^(-2-theta), including i=K. Alternatively E12 with FLOW-pw sums to this. Real second jets identify covariance by RGA10/RGA19. Free K-dec/LGF and correct normalization remain separate inputs to the witness. | **PROVEN real interface; OPEN matching and flow inputs.** |
| K4MATCH | JETS retains all 15 nonempty subsets and the final outer partition terms. MATCH4 gives \|P-P_run\|<=C u^(-4-theta4), since partial_1234(L-L_run)=u^4(P-P_run), with no 4!. A value-only alternative requires the extra fifth derivatives and loses theta4/5, as REALONLY R5–R6; it is not used here. | **PROVEN real interface; OPEN MATCH4.** |
| Flat H_Euc / TQ2 | For each whole product, positive finite-source pressures are convex: -p(-t)/t<=p'(0)<=p(t)/t. NC removes the common secant width after the cutoff limit; PC removes orientation pressure errors at each fixed t; COMMON gives one volume-first diagonal and extension. Real jets can supply stronger bounds, but finite-cutoff smoothness alone is not NC. | **PROVEN conditional interface; OPEN EUC-flat.** |
| Sphere H_Euc / N5B | Actual-law total covariance, including its terminal term, plus IMG-K bound C(J), CD-K early sum delta(J)->0 and ST oscillation tau(a,J)->0 gives delta(J)+C(J)tau(a,J). Fix J first, then take a->0; retain Z_a^-q and BULK/ALG. These are not inferred to be UV-only estimates. | **PROVEN conditional interface; OPEN EUC-sphere.** |
| REC / OSLEAF | The SAME S_n with E0', E1–E3, reality and S0=1 is its input. Complex test coefficients use multilinearity, not exponential complex-source control. Its complex spacetime continuation is unchanged. No source partition-function inverse is consumed. | **PROVEN compatibility; OPEN complete seed/common limit.** |
| Coupling bracket / tuning | Uniform real C^2 polymer convergence justifies curvature Hessian extraction. With \|partial_b partial_b' F_X(0)\|<=H exp(-kappa_p d(X)) in FLOW's normalized coordinates, its weighted spatial sum is bounded by 64 M^6 H sum_(n>=1)n^3(6400 exp(-kappa_p))^(n-1), finite for kappa_p>log 6400. Matching graph/field units, real remainder, continuity, bracket and FI-1 causal tuning remain required. | **PROVEN replacement of Cauchy; OPEN actual FLOW module.** |
| Flow/source response | If \|beta_j'(u_j)\|<=C/u_j^2<=q_*<1 and S=sum_j C/u_j^2<infinity, differentiating the scalar recurrence gives exp[-S/(1-q_*)]<=du_K/du_0<=exp(S). The spatial response requires its own weighted derivative kernel and LOC-e. Fixed original-source differentiation and flow-parameter variation remain distinct. | **PROVEN scalar implication; OPEN uniform derivative/spatial inputs.** |
| Literal complex RD4/LF-JMBR/STEP55 | IH_R supplies no estimate at nonreal physical sources, complex coarse fields or complex bond parameters. The real contract replaces the listed interfaces only after H0–H6 have been instantiated and accepted as that different producer. | **OPEN implementation; original contract unchanged.** |

For clarity, the HIER combinatorics uses product_B |B|!<=n! and at most
n! set partitions for the subsequent moment expansion. Subset separation
weights are bounded by the full-configuration ones. The collision-flat
step reserves 5n spatial weight powers; at distances below c_*a use the
crude a^-4n point bound and flat Taylor order 4n+1. This is why an
all-n, small-separation estimate is required rather than a finite-source
norm or convergence only on fixed separated tests.

The scalar response inequality follows from
du_K/du_0=product_j(1-beta_j') and
log(1-x)>=-x/(1-q_*), log(1+x)<=x for 0<=x<=q_*.
For the sphere bound use Cauchy–Schwarz on the terminal covariance and
the stated seam oscillation; for the flat bound use the real convex
secants. Neither argument requires a holomorphic log.

## 7. What has been delivered and the next decisive obligation

The replacements actually proved here are the finite real product/chain
calculus, admitted-fiber positivity and real log identities, differentiation
of the complete normalized reference, the conditional jet-valued Mayer
theorem, the ideal real Taylor contraction, and invariant-budget arithmetic.
The norm and its exact transfer obligations are specified, including two
often hidden losses: overlap regulator multiplicity and unbounded-order
localization derivatives. The carry-over and consumer maps are explicit.

The smallest decisive next construction is RGA14–RGA16 for a bounded
mixed core on the actual all-cut reference, retaining at least one coarse
derivative and all four original-source labels, and every completion
alternative. It must include the differentiated normalizer and regulator
overlaps; a scalar CHARGE price is not that test. A successful bounded
example would still require uniform local readers, an extracted coherent
margin or common creation envelope, and the separate HIER/MATCH/EUC/FLOW
modules. Those remain OPEN, with no asserted independence or wall count.

The live alternatives are direct real Haar/cell integration, a real
localized Gaussian construction with all its hypotheses, weighted-reader
tails, and extracted/charged continuation. None is declared exhausted.
This packet makes no no-go claim and supplies no negative-claim certificate.

Evidence: [pre-registered criteria](checks/realrga_criteria.md),
[finite diagnostic source](checks/realrga_check.py), and
[execution receipt](checks/realrga_result.json). The diagnostics are
**NOT RUN**: the sandbox refused `nice` and the preflight observed
niceness 0, so no mathematical test ran. Written proofs carry the author
claims; the required fresh review and its source hashes are recorded in
[the log](REALRGA_LOG.md). No existing prompt, source, audit or ledger was edited.
