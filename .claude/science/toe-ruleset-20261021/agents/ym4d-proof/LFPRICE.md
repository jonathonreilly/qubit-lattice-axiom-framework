# LFPRICE — large-field prices, component returns and boundary debits

**Route L on the actual all-cut reference remains OPEN.** M1's proposed
`p(g)^2/g^2` price uses the wrong units when p bounds a fluctuation divided
by g. M2 closes the size-summation arithmetic conditionally, including a
precise rule for small failed returns. M3 gives a consistent **raw** action
allocation and finite normalized-kernel boundary bounds for every fixed
SU(N), N>=2. It also gives an explicit, coupling-independent c_B **if**
matched boundary cluster logarithms are constructed. That matching and
the integrated joint activities are still missing for RD3's Z_A.

PROVEN means the displayed mathematical statement, with its stated
hypotheses, is proved below. ARGUED means a proposed construction. OPEN
means an unmet application obligation. No formal retained status, full
Yang–Mills existence theorem or impossibility theorem is asserted.
Source identities, resource limits and independent-review status are in
[LFPRICE_LOG.md](LFPRICE_LOG.md).

Credit: Tadeusz Balaban for the small/large-field organization and
large-field renormalization; Jonathan Dimock for its detailed exposition,
including [Large fields](https://arxiv.org/abs/1212.5562) and
[Convergence](https://arxiv.org/abs/1304.0705). Those two papers illustrate
three-dimensional scalar phi-four theory. They supply attribution and
methods, not premises for the four-dimensional nonabelian results here.
All load-bearing arguments below are rebuilt. No memory-only [m] item is
used.

## 1. Target, conventions and precise reference

Fix N>=2, odd L>=3, finite compatible four-dimensional tori, normalized
Haar measure and positive kernel parameters. Constants may depend on
N,L,kappa and on explicitly supplied chart/reader parameters; they must
not acquire unmentioned dependence on volume, depth or history. Write

    u_j = 1/g_j^2,
    s(U) = 1 - Re tr(U)/N,
    h_M(V) = Re tr(V^* M)/N,
    k_t(V;M) = exp(t h_M(V))/Z_t(M),
    Z_t(M) = integral exp(t h_M(W)) dW,     t=kappa u_j.       (1)

Here ||M||op<=1: M is the Decision-4 arithmetic mean of unitary
transporters. Subtracting the maximum of h_M, or subtracting the constant
one in the exponent, gives exactly the same normalized kernel. Its
normalizer must always be retained. This is a supplied mathematical
model, not a derivation of a physical action from the framework axioms.

The consumer is [RD4](RD4.md) L2–L9 and [RD3](RD3.md) RC1–RC3. In the
two-step example its all-cut denominator is

    Z_A(V)=integral chi_A(U_1) b_1(U_1) K_1(V,U_1) dU_1,
    Q_h(V)=R_h(V)/Z_A(V).                                    (2)

The inherited-history numerator R_h contains earlier fields, recorded
failures and missing cuts in holes. It is not the same density as b_1.
Z_A is not Z of the full Wilson chain, a relaxed-history partition
function, or an arbitrarily chosen cut-off Gaussian. In particular the
good-only reference and a history allowing bad fields can have different
supports before integration. A pointwise density ratio between those
two integrands is not available merely because both integrals are
positive. Only positive real fibres are divided by their masses.

For history arithmetic, explicitly supply the actual-chain bracket

    v + beta_- r log L - R <= u_(K-r)
                            <= v + beta_+ r log L + R,
    v=u_K>0,   0<beta_-<=beta_+,   R>=0.                     (3)

No beta-function theorem is proved here. Let sigma=mu+2, mu>=0, be RD4's
support-norm exponent. This sigma is unrelated to beta_±. Full supports
include inactive vertices, original source readers and collars. Every
claim below specifies whether it concerns a raw weight, an integrated
real law, a complex ratio or a connected activity.

## 2. M1: threshold units, scale summability and analytic cost

### LF1 — Wilson energy and the two threshold conventions (PROVEN)

For every U in SU(N),

    s(U)=||I-U||HS^2/(2N) >= ||I-U||op^2/(2N),
    0<=s(U)<=2,                 ||I-U||op<=2.                (4)

The identity follows by expanding (I-U)^*(I-U) and taking its trace;
the inequalities follow from the singular values and unitarity. Thus a
plaquette with raw curvature f=||I-U_p||op>=epsilon costs at least
`u epsilon^2/(2N)` in its Wilson action, before normalization or debits.

If the rescaled curvature is F=f/g and its threshold is p(g), then
epsilon=g p(g), and (4) gives **p(g)^2/(2N)**. The extra 1/g^2 has already
been used. If p(g)=c g^(-delta), 0<delta<1, the raw threshold tends to
zero and the price is `c^2 u^delta/(2N)`, not `c^2 u^(1+delta)/(2N)`.
For delta=1 this is the fixed raw threshold epsilon=c. For delta>1 it
eventually exceeds 2, so the raw bad event is empty. A threshold p(g)
diverging in f itself likewise becomes empty. Declaring all group
configurations small then does not put them in a prescribed small chart.
A principal logarithm also has bounded eigenangles; an unbounded lift
is a different integration space and requires its own measure/branches.
A dimensionful continuum curvature may grow after multiplication by an
inverse power of the lattice spacing, but its quadratic action has the
compensating spacing factor. Translate its threshold to f before using (4).

A curvature cut does not by itself bound gauge-fixed link fluctuations:
flat fields and holonomies must be treated. The next lemma concerns a
specified link chart, rather than inferring one from (4).

### LF2 — the singleton test (PROVEN for this majorant)

Put d=4+c_B with c_B>=0 fixed. For any fixed n>=1 and c>0 consider

    sum_(r>=0) exp[d r log L - n c u_(K-r)^delta].           (5)

Uniformity means uniform bounds on finite-depth truncations with v fixed
and (3) satisfied. If 0<delta<1, its last terms cannot tend to zero:
using the upper bracket, their logarithms are at least
`d r log L - n c(v+beta_+ r log L+R)^delta`, which tends to infinity.
Adding fixed powers of u cannot fix the linear-versus-sublinear growth.
This is a failed **upper-bound method**, not a lower bound on any
Yang–Mills history mass. Any finite, fixed component cutoff has the
same problem for a sublinear price. F17-COUNT treated this mechanism;
(5) rebuilds it for the power threshold requested here.

For a final price a_eff u, the geometric sufficient bound instead has
ratio `L^(d-n a_eff beta_-)`. It converges when

    n a_eff beta_- > 4+c_B.                                 (6)

At equality that pure geometric bound diverges. Extra summable factors
can repair equality: for example, on the same bracket, an additional
`(1+u_(K-r))^(-s)` with s>1 is summable, since eventually u_(K-r)
is at least v+(beta_- log L)r/2. Thus (6) is not a general necessary
condition on physical probabilities.

For comparison only, an **unbounded** curvature variable with a proved
action lower bound c F^2/g^2 and threshold F>g^(-delta) would give
c u^(1+delta). Its superlinear growth does beat the linear depth cost
for n=1 and therefore all n>=1, after any smaller debits. That
unbounded-field premise is not (4). In the rescaled Wilson convention,
the coefficient q(u)/u is c u^(delta-1), which tends to zero. It cannot
make (6) hold for singletons by going to weaker coupling.

### LF3 — what a fluctuation cut costs (PROVEN local estimate)

Let one plaquette be a product of four exp(g Z_l), with orientations
included in anti-Hermitian traceless Z_l and ||Z_l||op<=p. Continue the
Wilson expression holomorphically as
`f(g)=1-[tr P(g)+tr P(g)^(-1)]/(2N)`. Expanding the products gives

    f(0)=f'(0)=0,
    f(g)= -g^2 tr((sum_l Z_l)^2)/(2N) + Rem,
    |u Rem| <= (64/6) g p^3 exp(4g p).                     (7)

Indeed the m-th derivative of each product has norm at most
`(4p)^m exp(4|g|p)` by the multinomial formula. Taylor's integral
remainder with m=3 proves (7). This is per plaquette, not a
volume-independent interaction norm. It gives a sufficient vanishing
absolute remainder for p=c g^(-delta), delta<1/3. At and above 1/3
this bound no longer tends to zero; it does not rule out regulator
norms, cancellations or a different expansion. A relative quadratic
estimate needs a coercive one-step form in the chosen gauge sector;
the Wilson quadratic form alone has null directions.

If a chart is known only for link size <epsilon_0, a perturbation ball
of rescaled radius rho about this cut requires
`g(p+rho)<epsilon_0` (and the corresponding margin from its background).
This is a chart containment condition, not a source zero-free theorem.

There is a second, distinct radius cost from the soft kernel. For
V=W exp X, W unitary, X Hermitian traceless, ||X||<=alpha, the
holomorphic numerator uses tr(V^(-1)M)+tr(M^*V). With A=W^*M,

    |k_t^C(W exp X;M)|
        <= exp[t(cosh(alpha)-1)] k_t(W;M).                  (8)

To prove it, its real logarithmic change is
`(t/N) Re tr[(cosh X-I)A]`; cosh X-I is positive and ||A||<=1.
Its trace is at most N(cosh alpha-1). The real normalizer in (1)
does not depend on V and cancels. Multiplication and absolute integration
prove (8) for any real-fine-field raw superposition, including wild M.

If there are at most c_link n terminal readers, c_link>0, and the
available price is c p^2 per core block, spending a fraction
0<theta<1 in (8) requires

    alpha <= arcosh(1+theta c g^2 p^2/(kappa c_link)).       (9)

For gp tending to zero this is of order gp/sqrt(kappa c_link).
When c_link=0 there is no continuation debit from these kernels.
A fixed positive polar width is unaffordable by this estimate for
delta<1; the natural width rho g/sqrt(kappa) is compatible with a
diverging p. For a fixed raw-cut price a u the corresponding width is
`arcosh(1+theta a/(kappa c_link))`. Neither statement controls a
normalized denominator, a V-dependent hard selector, a complex fine-field
normalizer or the original-source radius. Those remain separate inputs.

**M1 disposition.** The unit correction and the failure of the specified
singleton majorant are PROVEN. The proposed mechanism does not close
Route L. Threshold changes may still be useful together with returns;
no theorem against that combined architecture is claimed.

## 3. M3: consistent local allocation and its actual boundary bill

### LF4 — charge the original terms once (PROVEN)

At the bare level partition plaquettes by a fixed deterministic owner
block, assigning every block-interior plaquette to that block. Choose
0<theta<1. For a set Y of n cut-bad blocks, each has an interior
plaquette with f>=epsilon; those witnesses are distinct. Put

    E_Y=theta sum_(p owned by Y) s(U_p),
    E_rest=sum_p s(U_p)-E_Y >=0.

Then `E_Y>=theta epsilon^2 n/(2N)` and the original density is exactly

    exp(-u E_Y) exp(-u E_rest) product_c k_c.               (10)

Hence, on the event,

    1_bad(Y) W <= exp[-theta u epsilon^2 n/(2N)] W_rest,   (11)

where W_rest has exactly the uncharged action and every original kernel
and normalizer. No new minimization, boundary condition or measure is
hidden in W_rest. Multiple disjoint core components use disjoint owned
terms. More generally, for windows of multiplicity at most m, distribute
each nonnegative term among its windows with weight 1/m. Distinct
witnesses counted with multiplicity then give the price
`theta u epsilon^2 n/(2N m)`, with the unused action nonnegative.
The bound is valid also when a window is cut by a boundary only if its
witness and allocated terms are still present; otherwise enlarge the
charged region or leave that block unpriced.

This supplies a locally consistent **raw** PRICE construction. It is
not a bound relative to Z_A: `integral W_rest / Z_A` is still owed.
For an effective main action E(V), the same proof applies if one
actually constructs `E=sum_Y E_Y+E_rest` with these inequalities on
the original domain. A separate free-boundary minimum on each region
cannot be substituted for that decomposition without proof. This is
exactly the local-consistency issue in LARGE55 PRICE/F9.

### LF5 — finite seam response with normalization (PROVEN, every N)

For real V,M in (1), |h_M(V)|<=1, so

    exp(-2t) <= k_t(V;M) <= exp(2t).                       (12)

If ||M-M'||op<=d, then |h_M(V)-h_M'(V)|<=d. Integrating the
pointwise exponential comparison gives

    |log Z_t(M)-log Z_t(M')|<=t d,
    |log k_t(V;M)-log k_t(V;M')|<=2t d.                  (13)

In particular, changing arbitrary means costs at most 4t. Changing
only V with M fixed costs at most 2t; changing both arbitrarily costs
at most 4t, by bounding the numerator difference by 2t and the
normalizer difference by 2t separately. These statements never choose
a smooth maximizer of M, so short or degenerate means cause no problem.

Suppose two raw integrands use the same product Haar measure and the
same selectors, and differ in at most P_boundary Wilson plaquette
factors and C_boundary normalized kernels. All other factors agree.
Replacing a Wilson plaquette by another, or deleting it, costs at
most 2u. Replacing a normalized kernel by another costs at most 4kappa u;
deleting it in favor of the normalized Haar density 1 costs 2kappa u.
Consequently the symmetric comparison with replacements obeys

    |log(w/w')| <= D_boundary,
    D_boundary=2u P_boundary+4kappa u C_boundary.            (14)

Use the corresponding sum with each term's own u_j on multiple levels.
At shared zero selectors interpret the assertion as pointwise domination
in each direction. Positivity integrates it: if integral w'>0, the
ratio of integrals lies between exp(-D_boundary) and exp(D_boundary).
With at most c_P and c_K such factors per boundary vertex, one explicit
raw boundary coefficient is

    b_raw(u)= (2c_P+4kappa c_K)u.                          (15)

Equations (12)–(15) rebuild SOFTHARD G2's finite-cost mechanism with
the field-dependent normalizers included. They hold for rough real
fields and all fixed N. They do not compare different hard-cut supports.

For complex weights a, even a pointwise multiplicative envelope must
retain `T_ref=integral |a|/|integral a|`. On two points with
a=(1,-1+d), 0<d<1, multiplying the first weight by exp(h), h>0,
changes the ratio to `1+(exp(h)-1)/d`. Bounded h alone gives no
uniform complex ratio. This elementary example is not an SU(N) zero.

### LF6 — explicit shadow geometry (PROVEN)

Let Y be a *-connected set of n blocks; the * graph in four dimensions
has maximum degree Delta=80. Let pi^ell be block contraction by L^ell.
Suppose the full boundary-reader set at height ell is contained in
the w-neighborhood of pi^ell Y, for a fixed integer w>=0. Set

    V_w=(2w+1)^4,
    B_0=16 V_w,              B_1=32 V_w/(L-1).

Then

    |Bdy_ell| <= 16 V_w[1+2(n-1)/L^ell],
    sum_(ell=1)^r |Bdy_ell| <= B_0 r+B_1(n-1).             (16)

Proof: a spanning-tree traversal visits Y in at most 2(n-1) star
steps. Break it into consecutive pieces of at most L^ell steps.
Each piece has coordinate span at most L^ell in each direction and
therefore meets at most 2^4 contracted blocks. The number of pieces
is at most 1+2(n-1)/L^ell, including n=1. A w-neighborhood multiplies
cardinality by at most V_w. Sum the geometric series over ell>=1.
An aligned torus quotient cannot increase this count, including wrap
levels. A path may be lifted before doing the count.

For a finite reader rule `C_(ell+1) subset N_s(pi C_ell)` with integer
s>=0, one sufficient uniform halo is w=2s+2: the inclusion
`pi(N_w A) subset N_(ceil(w/L))(pi A)` and
`s+ceil(w/L)<=w` close the induction. Increase w for any extra finite
collar. Exponentially long readers or tails require an additional
summed bound; (16) does not turn them into finite readers. Nor does
counting coarse shadows pay their full original-source footprint.

### LF7 — the boundary coefficient that would suffice (PROVEN implication)

Suppose the two **matched** small-field integrals admit logarithms
with cluster coefficients f_X^+ and f_X^-, and prefactor coefficients
v_X^+ and v_X^-, on the same domain and original-reader graph. Suppose
for each sign

    sup_x sum_(X contains x) sup |f_X^±| <= q,
    sup_x sum_(X contains x) sup |v_X^±| <= b,

and the corresponding coefficients agree whenever X misses Bdy.
Every coefficient of their difference then touches Bdy; summing once
over a vertex of Bdy, allowing overcounting, gives

    |G_boundary| <= b_partial |Bdy|,
    b_partial=2(q+b).                                      (17)

Matching means all untouched actions, local measures, cuts, gauge
Jacobians, normalizers and source readers agree. An interaction that
reads a deleted cone must be included. Mere geometric disjointness is
not matching of the coefficients of logarithms.

Combine (16)–(17). The later boundary bill of one component is at most
`b_partial B_1(n-1)+b_partial B_0 r`. Its n-dependent part is a
one-time reference debit; its depth-dependent part is L^(c_B r), with

    c_B= 32 V_w(q+b)/log L.                                (18)

These are explicit constants, rather than an unspecified O(eta).
They are uniform in coupling only if q,b,w are. This rebuilds a
conditional version of LARGE55 E13, with each debit allocated once.

By contrast (15) is proportional to u. If the raw boundary counts are
bounded per level and one uses that crude envelope at all levels
between K-r and K, the bracket u_(K-s)<=v+beta_+ s log L+R gives a
bill of order `r(v+R)+beta_+ log L*r(r-1)/2`. This is not a constant
times r uniformly in r. It is the inadequacy of that crude estimate,
not a lower bound or an impossibility theorem for the true boundary bill.
Normalized kernel softness gives finiteness, not (17)'s small cluster norm.

**M3 disposition.** LF4–LF6 close raw allocation, finite normalized seam
response and finite-reader geometry. LF7 closes the implication to c_B.
The actual matched logarithms for (2), including all-cut normalization,
remain OPEN; (18) is not an evaluated Yang–Mills boundary constant.

## 4. M2: return small components, keeping boundary activities

### LF8 — exact split and the integration order (PROVEN)

On any finite configuration space of blocks, classify the bad blocks
by fixed local predicates, and then their connected components. The
identity summing indicators of all possible exact bad sets is one.
Partition each resulting family into sizes n<n_0 and n>=n_0. This is
an exact regrouping, with no rarity assumption. Boundary variables y
can be left unintegrated while all fields of the smaller components
are integrated. Their resulting weights are functions of y, with
every original reader retained. Absence-of-other-defect indicators
are part of this identity, not optional factors.

If a mandatory event E has probability p>0, its normalized insertion
is 1_E/p and has integral one. The small parameter p occurs only in
the unnormalized history weight. It cannot also be used as the norm
of that normalized atom. This follows directly by integration and
applies at every group rank.

Even factorization conditional on y is not enough after y integration.
For y=±1 with equal mass and a_1(y)=a_2(y)=epsilon(1+s y),
0<s<1, the integrated product is epsilon^2(1+s^2), whereas the
product of integrated weights is epsilon^2. The connected remainder
epsilon^2 s^2 has no spatial decay if y is a shared distant reader.
Thus an exact expansion must attach that reader or control its
connected correlations. This example diagnoses the inference, not
the actual gauge model. Keeping boundary-condition activities is
necessary bookkeeping; it is not yet their joint local estimate.

### LF9 — multiplicities and a connected expansion (PROVEN implication)

On a graph of maximum degree Delta>=1, the number of connected
n-vertex sets containing a specified root is at most
`max(1,Delta)^(2(n-1))`. Choose a deterministic spanning tree and
its depth-first walk; the walk of length 2(n-1) determines its
visited set. Counting all possible walks gives the bound.
If each core vertex has at most T labels, and the full support lies
in its w-neighborhood, one explicit rooted bound is

    A_geom^n,      A_geom=V_w T max(1,Delta)^2.              (19)

Indeed a root in the support can be within w of at most V_w core
anchors. This applies to bare finite-range shapes and finite labels.
It is not a count of all integrated histories, arbitrary analytic
source labels or long clusters. For those, T must be replaced by
a proved **sum** of type weights, and reader closure must be proved.

Here is the exact analytic contract for using this count. Assume a
common product of normalized local reference measures, holomorphic
on a domain D, after any required cell aggregation. Use a finite atom
family with nonempty finite supports S_i. Extract any empty-support
factor as a separately specified nonzero prefactor; (20) cannot
control such a factor. The empty selected set has coefficient one.
The expansion coefficients c_I, including selection and compatibility
rules, must factor over the overlap components of each selected set I.
Disjoint supports alone do not imply that property for a gas with
additional global selection constraints. The absolute-integral
majorant must bound the **complete coefficient-weighted term**:

    integral_(cells read by I) |c_I product_(i in I) a_i|
                         d|mu_I| <= product_(i in I) alpha_i.

Here alpha_i>=0, and unvisited normalized cells have already been
integrated out before absolute values are taken. For complex measures,
mu_I is the restriction to the visited cells and all its total-variation
cost is included in this bound. Factorization alone does not control
a large coefficient on overlapping atoms. Let

    Q=sup_x sum_(i: x in S_i) exp[(mu+2)|S_i|] alpha_i
      <=1/4.                                               (20)

Expand the finite product/gas of atoms and group its selected sets
by support-overlap components. Product integration factors the
components, giving an exact hard-core polymer gas, before its log
is taken. Put v_i=exp[(mu+1)|S_i|] alpha_i. Connected selections are
bounded by rooted trees, allowing repetitions only in the positive
majorant. The exponential tree recursion

    T_i=v_i exp(sum_(j overlaps i) T_j)

has supersolution T_i<=v_i exp(|S_i|), since its child sum is at
most Q|S_i|. Iteration from zero and root marking bound the integrated
gas norm at exponent mu+1 by Q. For its logarithm the alternating
connected-graph sum is bounded by spanning trees: order graph edges
and assign each connected subgraph its Kruskal tree. Subgraphs with
that tree form an interval between the tree and its allowed extra
edges. Their alternating sum is zero or has unit modulus. The same
tree recursion with the remaining unit of support exponent bounds
the connected-log norm at mu by Q. Tuples in this second expansion
include repeated polymer labels; root marking changes 1/m! to
1/(m-1)!, as required.

To justify the logarithm rather than assume it, multiply original
atoms by a parameter z. The bounds still converge for |z|<=2 since
2Q<=1/2. The finite gas and the exponential of the convergent
connected series agree near z=0 by their graph expansion, hence
through that disc by analyticity. At z=1 the gas is nonzero and
has the constructed logarithm. This is a conditional proof of
connected expansion; it does not assert (20) for the actual chain.

If returned types have full support <=c_s n and joint weights
<=exp(-nu_R n), (19) or its verified integrated replacement A_R
gives, with r_R=A_R exp(sigma c_s-nu_R)<1,

    Q_ret <= sum_(1<=n<n_0) r_R^n <= r_R/(1-r_R).           (21)

Their boundary functions remain atoms in (20). Analogously frozen
types contribute `sum_(n>=n_0) r_F^n`, provided the same factorization
contract holds. Require `Q_sf+Q_ret+Q_frozen<=1/4`; do not allocate
the same unused budget twice. When both defect classes obey a common
r, their total is at most r/(1-r), independently of n_0.

### LF10 — final prices, size cutoffs and failed returns (PROVEN arithmetic)

Let the raw per-block price be a_0 u and the one-time normalization
factor be C_0 u^d, d>=0. For 0<a_eff<a_0 and Delta_a=a_0-a_eff,

    C_0 u^d exp(-a_0 u)
       <= C_0[d/(e Delta_a)]^d exp(-a_eff u),               (22)

with the bracket replaced by 1 for d=0. Differentiate
d log u-Delta_a u to obtain its maximum. Thus a positive power
cannot be absorbed while retaining exactly a_0. All other linear
debits, including complex continuation if used, must be deducted
before choosing a_eff. Negative remaining price supplies no cutoff.

Suppose all final type, placement and other paid costs at depth r
are bounded by `A_0^n L^((4+c_B)r)`, and a_eff>0. This is a
**history-count contract**, separate from the original-source norm.
If frozen components have n>=n_0, set

    n_0=floor((4+c_B)/(a_eff beta_-))+1,
    z=A_0 exp[-a_eff(v-R)]<1.

Then (3) and two geometric sums give

    sum_(r>=0) sum_(n>=n_0)
      A_0^n L^((4+c_B)r) exp(-n a_eff u_(K-r))
      <= z^n_0 / [(1-z)(1-L^(4+c_B-n_0 a_eff beta_-))].    (23)

The denominator is strictly positive. In the convention returning
n<=n_sharp, this is n_sharp=n_0-1. LF7's one-time geometry cost
exp(b_partial B_1 n) belongs in A_0 once, while (18) belongs in
c_B once. The weak-coupling ceiling can ensure z<1, but cannot
repair a negative exponent margin in (23).

Every attempted return of size n<n_0 must (i) actually return with
the activity estimates, (ii) join a larger, genuinely paid component,
or (iii) acquire an extra price making its own depth sum convergent.
Calling it a failed return and freezing it at its original price
does not satisfy the hypothesis n>=n_0. Joining requires charges
on the added blocks; a larger unpriced support is insufficient.

For the sublinear threshold of LF2, a fixed n_0 cannot help. An
alternative still open to investigation is a variable cutoff:
if the net per-block price, after one-block entropy and debits, is
q_net(u)>0, choose n_0(u) so that

    n_0(u) q_net(u) >= a u,
    a beta_->4+c_B.                                        (24)

For q_net(u) comparable to c u^delta, this needs size of order
u^(1-delta). At each depth the sum over n>=n_0(u) is at most
`exp[-a u]/(1-exp[-q_net(u)])`. A uniform positive lower bound
on q_net then permits the geometric depth sum. This proves the
counting possibility; it does not prove return estimates uniform
in a growing cutoff, nor control their enlarged original supports.

Finally returning small objects is not permission to discard them.
Relevant and marginal pieces of their connected activities must
be extracted and their residuals controlled in the next step.
Even an arbitrarily small fixed per-site vacuum term at every level
has a nonuniform volume-weighted sum. Equation (21) proves one-step
smallness only; an R-operation or an explicitly proved alternative
is still needed for scale-uniform induction.

**M2 disposition.** Exact splitting, the conditional connected-gas
estimate and the final-price cutoff are PROVEN. On the actual
all-cut reference the boundary-conditioned activities, their joint
factorization, renormalized returns and treatment of failed returns
remain OPEN. M2 is a viable conditional route, not completed I6.

## 5. SU(N), good/bad scope and the L6 ledger

### LF11 — a thresholded kernel tail for every fixed N (PROVEN)

Let D=2N^2, t>=1 and psi_M(V)=max_W h_M(W)-h_M(V)>=0.
For 0<rho<=1 an operator-norm Haar ball has mass at least

    m_rho >= (1+4N/rho)^(-D).                              (25)

Partition the real and imaginary matrix entries in [-1,1] into
intervals of length rho/(2N). At most (1+4N/rho)^D cells meet
SU(N); choose a group element in each nonempty cell. Every cell
lies in the operator-norm rho ball of its representative, since
the Frobenius distance is at most rho/sqrt(2). Haar invariance
makes all such balls have the same mass. Covering the group proves
(25). This conservative ambient-dimension bound is not the sharp
dimension N^2-1 asymptotic.

The function h_M is 1-Lipschitz in operator distance. On the
1/t ball of any maximizer, psi_M<=1/t. Thus

    integral exp(-t psi_M) >= exp(-1)(1+4Nt)^(-D),
    P_(k_t)(psi_M>=a) <= e(1+4Nt)^D exp(-t a).             (26)

Conditional on the entire past, different output links are independent.
For fixed sets of such link events, multiply (26). For events at
several levels, integrate the latest outputs first, take the uniform
bound over their past, and induct. This proves a joint **plain-chain**
thresholded mismatch bound without SU(2)'s special sharp moment formula.
Equation (22) reserves its polynomial cost when a fixed a>0 is used.

There is no price for arbitrary coarse badness in (26). At M=0 the
kernel is Haar and psi_M is zero for every output. To turn geometric
mismatch into a gap threshold needs a property of M. For example,
if M=W_0 H, W_0 in SU(N), H Hermitian with H>=m I>0, then W_0
maximizes h_M and, writing A=W_0^*V,

    psi_M(V)=tr[(I-A)^* H(I-A)]/(2N)
              >= m ||I-A||op^2/(2N).                      (27)

Expand the trace and use cyclicity to prove the identity. An arbitrary
arithmetic mean need not have this SU(N) polar form with a lower bound
m. Equation (27) is a checked sufficient condition, not an assumption
that all coarse means satisfy it.

Future/history conditioning multiplies the past law by a future
avoidance factor. It destroys the simple use of independent forward
outputs unless the appropriate local tilt comparison is established.
That is the law mismatch in REVIEW_RLARGE_V3 S-1/S-2; (26) does not
resolve it or assert the sharp all-N moment (KS-N).

| Family/domain | What is proved here | What is still required |
|---|---|---|
| Bare interior cut-bad blocks | LF4 price with m=1 for all N | Actual all-cut reference comparison after charging |
| Overlapping curvature windows | LF4 with explicit multiplicity m | Coverage of every witness at boundaries |
| Gap-bad kernel outputs psi>=a | LF11, all means, all N, plain chain | Matched/history/future-tilted version if consumed |
| Geometric mismatch/collar-bad | LF11 if a condition such as (27) holds | Actual geometric-to-gap implication, overlap, other collar tests |
| Good background/fluctuations | LF3 local expansion estimate only | Gauge chart, one-step coercivity and uniform interaction norm |
| Bad coarse field held fixed | Raw density inequalities and LF5 | No small conditional probability of that fixed bad field is claimed |
| Rough real seams | LF5 finite normalized cost | LF7's coupling-independent matched cluster cost |
| Complex coarse output | LF3 raw numerator envelope | Actual normalized zero-free domain and full reader norm |

The argument uses neither a universal chain-convexity claim nor a
universal convexity obstruction. CODEX_REVIEW_LCONV R1/R8/R9 leaves
the proposed one-step/tilted construction open and corrects the
asserted exact coupling-lowering tilt. For clarity the literal tilt is

    exp(lambda t psi) k_t
       = [N_((1-lambda)t)(M)/N_t(M)] k_((1-lambda)t),        (28)

where N_s=integral exp(-s psi_M). The ratio depends on M. A tilt
of a minimized column observable is a further different object.
No such tilt is silently substituted for a changed coupling here.

### What can actually be inserted in RD4 L6

Write that ledger as

    nu_L=tau-c_ref-t_ref-c_partial b_partial
                    -kappa u c_link(cosh alpha-1),
    r_L=A exp(sigma c_s-nu_L),     Q_L<=r_L/(1-r_L).        (29)

It follows simply by multiplying the size-n price, the reference and
boundary envelopes, the continuation envelope and exp(sigma|support|),
and summing over types and then n. If tau and the other envelopes
are already complex-domain estimates, omit the continuation debit.
The mixed connected criterion requires the exact factorization in LF9,
in addition to this scalar sum. An atom budget for small-field
interactions of norm h is at most exp(h)h, by the power series for
exp(H)-1. Reserving 1/8 for it and 1/8 for the complete regional gas
requires r_L<=1/9; hence nu_L>=sigma c_s+log A+log 9.

| L6 input | Constructed value at its proved scope | Exact remaining all-cut requirement |
|---|---|---|
| tau | Bare allocation: theta u epsilon^2/(2N m); rescaled epsilon=gp gives theta p^2/(2N m). Kernel gap: t a before its cap cost. | An effective/original-law charged density with the same local reference as (2), on every relevant defect family |
| c_ref | LF11 cap cost 1+D log(1+4Nt) per priced link; LF10 reserves polynomial losses. LF7 later geometry contributes b_partial B_1 once. These are components, not the whole comparison. | Bound the uncharged/matched reference ratio, including action vacua, all cuts, determinants/Jacobians, kernel normalizers and changes of domain by exp(c_ref n) |
| t_ref | Exactly 0 for any real positive reference actually used in L2 | A nonzero complex reference and T_ref<=exp(t_ref n) for the same connected integrations; positivity gives no complex value |
| b_partial | Raw finite-factor comparison: (2c_P+4kappa c_K)u. Matched cluster comparison: 2(q+b). | Construct the matching cluster/prefactor expansions on (2) with uniform q,b; raw comparison does not cover changed hard supports |
| c_B | Under LF7 and finite reader halo: 32(2w+1)^4(q+b)/log L | The actual readers, including tails, must obey the required summed geometry and coefficient norm |
| A,c_s,c_partial | Static shapes: A_geom in (19), c_s<=V_w and c_partial<=V_w when full supports lie in N_wY | Prove exponential **summed connected integrated** multiplicities and full original-reader sizes; static shape counts alone do not give them |

At a real reference t_ref=0 does not make c_ref known. Calling the
entire unknown ratio L_h merely transfers the work into its bound.
Similarly (18) gives a formula for c_B, not values of q,b for the model.
No collection of raw constants in this table is advertised as a
completed all-cut tuple satisfying (29).

## 6. Exact remaining construction and next decision

**LF-JMBR — OPEN joint matched boundary-return lemma.** For the stable
admissible history/chart class and the original-source/coarse domain
D_* required by RD4, construct the following on the actual R_h and Z_A
of (2), at every step, uniformly in volume, depth and history:

1. An exact change-of-variables/integration representation with explicit
   local reference measures. Untouched factors agree with the all-cut
   denominator. Every changed hard predicate, action term, kernel
   normalizer, gauge factor and original source reader has a named
   support. Changes of support are handled by an actual map or by
   disjoint sectors and their integration, not a nonexistent pointwise
   density ratio. Zero-mass sectors are left zero.
2. A locally consistent charged action and a bound on the **joint**
   absolute integral of its remaining reference change, boundary
   insertions and return factors. Supply tau and c_ref in (29), with
   raw charges used only once. Supply matched boundary coefficients
   obeying LF7 or another explicit debit, and include tail-reader
   geometry rather than silently taking w finite.
3. A common nonzero complex reference and its local total-variation
   accounting, yielding t_ref. Original-source radius, contour and
   finite-coupling remainder estimates are named coordinator inputs;
   they are used only if their exact hypotheses cover these integrals.
   A convergent common-reference expansion may establish zero-freeness
   itself, so these clauses are not asserted to be independent walls.
4. Before taking a log, integrate the large variables together with
   every small-field cluster that reads them, group complete overlaps,
   and prove exact factorization of disjoint resulting types. Prove
   summed type and full-support bounds A,c_s,c_partial satisfying LF9
   and (29). A bound for each separately integrated scalar history
   does not prove this identity.
5. Return all n<n_0 components under those bounds, including every
   failed-return alternative in LF10; extract their required relevant
   terms and prove the next-step estimates. Freeze only components
   meeting the final-price rule, or establish (24) with estimates
   uniform in its variable cutoff. Verify any history-count entropy
   separately from the full original-source norm.

This lemma is the remaining constructive substance of I5/I6 on the
chosen reference, not a weaker solved reformulation. LF4, LF5, LF6 and
LF10 discharge its raw allocation, finite seam, static geometry and
cutoff arithmetic substeps. They do not discharge its integrated
normalization or gluing. The coordinator's fixed source radius,
finite-coupling remainder and original-law coercivity/tails are named
inputs, not rederived or promoted here.

**ARGUED next decision.** Work first on a bounded component with its
complete boundary readers and the same all-cut local measure; construct
both small-field cluster logs and exhibit their cancellation off that
boundary. A uniform LF7 estimate, together with the joint reference
bound in clause 2, would turn (18) into an actual price parameter.
Then set n_0 using the final a_eff and prove the return rule. If finite
reader closure fails, retain tails in a weighted version of that
construction; do not increase a geometric constant to hide them.

## 7. No-go discipline scope check and delivery limits

- **N1 — actual alternatives.** Three requested mechanisms were examined:
  growing thresholds, component returns and local boundary allocation.
  Fixed versus growing cutoffs are alternatives within the second
  mechanism, not invented extra independent families. Fewer than five
  exhausted route families exist here; no five-route packet PASS is
  claimed. The result is a partial construction with honest residuals.
- **N2 — dependencies.** For charge/reference matching versus boundary
  logarithms, neither implication is established here. For either of
  those versus joint integration/factorization, neither implication is
  established. For joint convergence versus zero-freeness, LF9 proves
  the forward implication under its budgets; the converse is not
  established. The separate components of LF-JMBR are not counted as
  independent walls. Raw geometry is already proved under its stated
  finite-reader premise.
- **N3 — hidden conditions.** The load-bearing conditions are explicitly
  the model (1), bracket (3), local chart in LF3, disjoint or bounded
  overlap charges in LF4, identical selectors in LF5, finite-reader
  containment in LF6, matched logarithms in LF7, and the joint
  factorization/TV budgets in LF9. None is inferred from its name.
- **N4 — matching earlier findings.** F17-COUNT concerns raw scale
  counting, matching LF2 only; F17-CRIT preserves the equality escape.
  LARGE55 F9/E13 concern local action/reference debits, matching LF4–LF7.
  RLARGE S-1/S-2 concern future-conditioned laws, matching LF11's
  limitation. LCONV's restricted Hessian examples are not used as a
  counterexample to the actual all-cut construction.
- **N5 — resolution.** Per plaquette: LF1 and LF4. Per link: LF3/LF5/LF11.
  Per fluctuation mode: no spectral/coercivity theorem is proved.
  Per block: charge overlap and finite-range counts are proved.
  Lattice-wide: conditional sums and explicit failed upper estimates
  only; no failed majorant is promoted to divergent Yang–Mills mass.
- **N6 — partial closure.** Correcting the units in M1 and choosing a
  cutoff require no new physical axiom. Reorganizing the reference and
  proving LF-JMBR remain mathematical routes. Approved framework
  primitives are not called missing estimates.
- **N7 — strongest counter-route.** A matched, renormalized boundary
  expansion could cancel the O(u) raw seam bill down to LF7's O(q+b)
  cost, return every small component, and then use (23). This is a
  concrete live route, consistent with LARGE55 E13 and RD4 L1–L8.
  Nothing here excludes it; it is the reason a no-go verdict would be
  unjustified.
- **N8 — prior-art/echo check.** The supplied RD3/RD4, LARGE55 and F17
  arguments already distinguish raw price from normalized reference
  and raw counts from returned sums. The present note does not revive
  zero boundary cost, unchanged a after polynomial absorption, or
  good/bad/SU(2)-to-SU(N) promotions. The repository search and coverage
  limits are recorded in the log; no exhaustive campaign closure is
  claimed.

No numerical experiment was needed for these statements. The sandbox
blocked the required nice priority; it was not bypassed. Analytical
proof and independent review, not numerical samples, are the evidence
for the PROVEN statements. No existing source, instruction, audit,
ledger or axiom file is edited, and no commit is made.
