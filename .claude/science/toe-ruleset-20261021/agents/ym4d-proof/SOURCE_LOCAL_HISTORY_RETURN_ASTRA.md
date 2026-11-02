# Actual hard histories with a fixed zero-source return reference

## Contract and current target

Recorded on 2026-10-29 after source inspection and exploratory route selection,
before the new proof write-up and checker execution. This is a new author unit
in the existing PR #10114 lane. Intended claim type: bounded theorem. The
checkpoint below is an author argument at its stated bounded scope;
independent review is pending. No audit authority or full Yang–Mills existence/physical-gap claim is
made. The proved small activity is specifically `a_Y=h_Y t_Y`, on the
explicit completion-good return class. The complementary `f_Y=(1-h_Y)t_Y`
remains unpriced in the exact partition; zero-source normalization does not
make arbitrary histories rare.

The corrected [fixed-reference continuation](SOURCE_LOCAL_RETURN_CONTINUATION_ASTRA.md)
at pushed commit `e4464249d9729a0bf7725be67611aa95aba5df01` has SHA-256
`ac985bb9b41a0d9d52ead7c2932df73e59c713c28c5c45f0629003552eee1243`.
Its [independent review](REVIEW_SOURCE_RETURN_CONTINUATION_ASTRA.md) has SHA-256
`3e366f02225d5f2f35ad3d8dff445e368ed0d0e2f07a7a956d1f3e0af51cd5ee`;
the [review receipt](checks/review_source_cont_receipt.json) has SHA-256
`e79eda07e76fb95a25c93d3869556cecbed735179051c62c97cbf7e140c219c0`.
All three hashes were checked; the complete final note and review were read.
The two repairs are inherited: complex-B analyticity of a hard history needs a
separately justified holomorphic pullback, and dependencies use actual links.
These frozen inputs will not be modified.

**Target/domain.** Construct an exact level-zero return on finite periodic
four-dimensional lattices, fixed N>=2 and odd block side L>=3, real u=1/g^2,
and fixed positive kappa. Retain the actual Wilson action, normalized soft
kernel, cube-interior plaquette cuts, all frozen collar/anchor links and all
failure/outside-chart terms. Original coefficient sources epsilon enter only
the Wilson coefficients u(1+epsilon_p); the kernels keep their prescribed
real coupling. The initial source domain to test is |epsilon_p|<=lambda/u
with lambda fixed independently of volume and component size. Coarse and
external fine fields are real SU(N) unless an additional complex domain is
proved explicitly. No extension from auxiliary fluctuation decay to physical
mass gap is allowed.

**Consumers and premises.** [STEP55](STEP55.md) sections 5.1–5.4 and S8/S9,
[its R11 review](CODEX_REVIEW_STEP.md), [LARGE55](LARGE55.md) sections 6.1–6.4
and E13/E14, and [SRC2 MB/R3](SRC2_55.md) require an actual normalized source
return, not only an exponential identity for a substitute integral. The actual
frozen numerator/denominator and interior links are specified in
[RLARGE sections 3 and 5](RLARGE.md); the collar rule and its unresolved
sigma-restricted gas are in its sections 2.2–2.4 and [PLD 9.4](PLD.md).
The relevant [LARGE review](CODEX_REVIEW_LARGE.md), [SRC2 review](CODEX_REVIEW_SRC2.md)
and [B2 action-identification caveat](CODEX_REVIEW_B2.md) remain controlling
limits. The actual bare action and compact group Haar measure are model data,
not new physical axioms. The reviewed [CX-R](RECOVERY_CLUSTER_ASTRA.md) and
[its review](REVIEW_RECOVERY_CLUSTER_ASTRA.md) supply the repulsive polymer
cluster/tree mechanism only where its norms are actually verified.

**Construction under test.** Keep the cut-good denominator at zero source,
then compensate the common source-weighted sea by an explicit local source
factor. Test whether this exact Fubini rewrite eliminates the need to divide
by each complex-source history integral. Group nearby bad cubes so each
component's actual completion collar reads no other component's integrated
links. Classify returned/failure components by an explicit source-independent
completion test. Prove their partition identity first, then the price and
connected original-source norm of the returned gas. Retain arbitrary hard
history insertions by the exact replacement operator rather than assigning
them a product measure. An excluded-polymer/boundary comparison may resolve a
part of the reference interface; it must not be called a multilevel COL proof.

**Alternate route and failure criterion.** Finite-range approximations of
b,C plus L1 boundary-layer bounds remain an alternative. Pointwise Taylor
expansion of an indicator is invalid. A radius-r ball localization has volume
O(r^4), so an e^(-mr) tail alone does not pay an e^(beta|support|) norm. That
specific unproved conversion is not used as a theorem or global no-go. If the
fixed-reference rewrite omits a source action, reads a replaced collar link,
or leaves a normalization mismatch, preserve the failed calculation and
repair or choose a different construction.

**Decisive checks (before execution).** (1) Exhaustive finite-state direct
summation versus the exact source-dressed return with nonconstant boundary
data and complex coefficients; remove each compensation/reference factor as
negative controls. (2) A hard history reading both returned interiors must be
handled by the replacement integral, and replacing it by independent events
must fail a witness. (3) Actual four-dimensional plaquette/contour incidence
must justify the collar range, factor allocation and per-cube counts, including
periodic small tori. (4) Independent algebra/tree enumeration must check
connected supports and boundary cancellation, with a remote-source/connector
omission control. (5) An actual nonabelian one-cube Haar slice or analytic
specialization must verify the source compensation and retain the normalized
kernel; scalar checks alone cannot prove the Yang–Mills match. Finite checks
are diagnostics. Uniform all-order conclusions require the written proof.

**Success witness and limits.** A coherent result must give exact formulas for
Xi_h, Z_ref,h, numerator, denominator, local source dressing and every
failure term, plus an actual-model price and summable original-source norm
on its stated domain. The full coarse-field/history induction, sea average,
higher-level exact action, renormalization, N1/N2, OS existence and physical
gap remain open unless separately proved. This unit attempts a new producer;
it is not a renamed package equivalent to those goals.

Methodology/current-main revision is
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`, freshly supplied by the coordinator.
Previously completed unchanged procedure/primitive reads are reused; AGENTS,
SCIENCE_WORKFLOW and the current physics-loop entry were refreshed directly.
The coordinator holds the lock and owns commit/push/review. This worker writes
only this file and `checks/source_history_return_*`, with no git, PR, shared
summary, audit or worker mutations.

## 1. Actual raw density, cuts, collars and references

All formulas in this section refer to level zero. Let the torus have T>=2
blocks in each direction, each with L^4 fine sites. Coarse anchors are the
block centres. All fine and coarse links are actual SU(N) matrices. Put
D=N^2-1, g=u^(-1/2), and use the source convention

    s(U_p)=1-Re tr(U_p)/N,
    delta S(U)=u sum_p epsilon_p s(U_p),
    w_epsilon(U;V)=exp[-u sum_p s(U_p)-delta S(U)]
                    product_c k_(kappa u)(V_c;Mbar_c(U)).       (H1)

The kernels are the actual normalized Decision-4 kernels. Their coupling
kappa u is held fixed when epsilon varies. With the notation of the reviewed
continuation, s_p=N s and sigma^2=N/u, so u epsilon s=sigma^(-2)epsilon s_p.
No vacuum term, normalizer or source-only term has been divided out of (H1).
Fix kappa in [kappa_min,kappa_max] with 0<kappa_min<=kappa_max<infinity.

Let I(Y) be the links whose two endpoints lie in one block Q in Y. A link
between different blocks is always frozen in the local integral, including
all links needed by the fixed collars. Let P(Y) be the Wilson plaquettes
reading any link of I(Y), and C(Y) the coarse links with an endpoint block
in Y. Put

    w_Y^0(U_I;data_Y)=exp[-u sum_(p in P(Y))s(U_p)]
                       product_(c in C(Y))k_(kappa u)(V_c;Mbar_c(U)),
    delta S_Y(U)=u sum_(p in P(Y))epsilon_p s(U_p),
    w_Y^epsilon=w_Y^0 exp(-delta S_Y).                          (H2)

Precisely, data_Y retains all fine links with both endpoints in the block
collar N_1(Y) but outside I(Y), together with V on C(Y). The density (H2)
reads only a subset; the completion test (H11) also reads the retained collar
plaquettes. These are restrictions of the same actual U,V, not new independent
background coordinates. Repeated appearance of one original coefficient in several candidate activities is
permitted; within each term it retains its plaquette label. The kernel means
use the actual order-averaged contours of length <=p_L=5L-4, entirely within
the two endpoint blocks. Every factor reading I(Y) is included in (H2).
Including an occasional kernel independent of I(Y) merely retains that same
factor in both local integrals; it never changes the raw identity.

Keep RLARGE's actual indicators exactly:

    chi_Q(U)=product_(p wholly interior to Q)
                    1{||I-U_p||op<epsilon_1},
    zeta_Q=1-chi_Q,    chi_Y=product_(Q in Y)chi_Q,
    zeta_Y=product_(Q in Y)zeta_Q.                              (H3)

Here epsilon_1>0 is a fixed cut, not the coefficient source epsilon. It is
chosen within any further chart ceiling needed by a later consumer; the
identities themselves require no small chart. Each interior plaquette uses
only I(Q), which is essential below. Define the actual local integrals

    D_Y^0(data_Y)=int chi_Y(U) w_Y^0(U;data_Y) dHaar(U_I(Y)),
    N_Y^epsilon(data_Y)=int zeta_Y(U) w_Y^epsilon(U;data_Y)dHaar(U_I(Y)),
    D_Y^epsilon(data_Y)=int chi_Y(U) w_Y^epsilon(U;data_Y)dHaar(U_I(Y)). (H4)

The data and denominator are different objects. The function D_Y^0 is strictly positive
for EVERY real data_Y,V and every nonempty Y: all interior links in a sufficiently
small open cap around I make chi_Y=1, irrespective of the frozen exterior;
the exact real density is strictly positive and continuous on the compact
integration domain. The cap has positive Haar measure. This argument makes
no assertion that every numerator/history has positive mass. A zero-measure
history has zero numerator and is retained as zero. We never divide by it.

Define `Z_epsilon[Xi](V)=int Xi(U,V)w_epsilon(U;V)dHaar(U)` and
`Z_epsilon(V)=Z_epsilon[1](V)`. This is the unnormalized one-step density at
the fixed coarse field V, not the partition function after integrating V.
The common sea reference is the actual positive number and measure

    Z_cut^0(V)=int product_Q chi_Q(U) w_0(U;V)dHaar(U)>0,
    dnu_cut^0(U;V)=product_Q chi_Q(U)w_0(U;V)dHaar(U)/Z_cut^0(V).
                                                                  (H5)

Its positivity follows by restricting all fine links near I. It is allowed
to be very small. No lower bound uniform in volume, nor clustering of this
measure, is inferred. Z_cut^0 retains all vacuum, Haar and kernel factors.
For every history in the construction below the common Z_ref,h is exactly
Z_cut^0(V); this is a proved alternative return normalization, not a claim
that an older unspecified Z_ref,h happened to equal it.

There is NO change of integration chart in (H1)-(H5). Haar is normalized
probability on every link, all gauge orbits are integrated, and no anchor or
collar link is gauge-transformed. Consequently no Faddeev-Popov determinant,
Gaussian determinant or contour side is missing: none has been introduced.
If a later calculation introduces the predecessor's tree/white sector Omega,
the exact local split is D_Y^0=D_(Y,Omega)^0+D_(Y,Omega^c)^0 (and the same for
N), with the actual chi_Y/zeta_Y in each summand. Only the first summand may
then use (C8), with its actual pulled-back indicator and full prefactor. The
present construction integrates both summands as written, including all
outside-chart, holonomy and white-cut-failure configurations.

## 2. The exact source compensation and hard-history replacement

On the graph of blocks join distinct blocks whose periodic sup-distance is
at most 2. Call this graph G_2. For any bad set B of blocks, let C_2(B) denote
its connected components. Distinct components have distance at least 3.
Their collars A(Y):=N_1(Y) are disjoint. The sets I(Y),P(Y),C(Y) are disjoint
across these components, and no factor in w_Y^0 reads I(Y') for another
component Y'. Every datum in (H2) is supported in A(Y); |A(Y)|<=81|Y|.
The collar is connected in the ordinary nearest-neighbour block graph even
when Y is connected only in G_2: radius-one cubes of G_2-neighbouring roots
overlap. Periodic identifications only reduce these counts. This grouping
merges some of the old star-components; it changes neither chi_Q nor any raw
weight. It is specified before using a collar-dependent return rule.

Define the source-dressed local activity

    t_Y^epsilon(U;V)=exp(delta S_Y(U)) N_Y^epsilon(data_Y)/D_Y^0(data_Y).
                                                                  (H6)

It depends on the actual sea links inside A(Y), including links of I(Y)
through the explicit compensator. It is entire in the original coefficients
on P(Y); it does not require D_Y^epsilon!=0. At epsilon=0 it is exactly the
old frozen activity N_Y^0/D_Y^0. Where D_Y^epsilon is nonzero, its relation to
the old source-dependent quotient is explicitly

    t_Y^epsilon=exp(delta S_Y(U)) [D_Y^epsilon/D_Y^0]
                                    [N_Y^epsilon/D_Y^epsilon].     (H7)

The middle factor is an actual cut-good conditional expectation. Dropping it
or the first factor would change the return.

For any bounded measurable hard-history insertion Xi(U,V), independent of
epsilon, define the replacement operator for a bad set B, including B empty,

    (T_B^epsilon Xi)(U;V)
       = product_(Y in C_2(B))[exp(delta S_Y(U))/D_Y^0(data_Y)]
         int product_(Y in C_2(B))[zeta_Y(Uhat)w_Y^epsilon(Uhat;data_Y)]
                  Xi(Uhat_I(B),U_outside_I(B);V)dHaar(Uhat_I(B)).     (H8)

For B empty this is Xi. Interacting or correlated histories remain in the
JOINT integral. No product approximation to Xi is made. Its exact identity is

    Z_epsilon[Xi](V)/Z_cut^0(V)
       = E_(nu_cut^0)[ exp(-delta S(U)) sum_(B subset blocks)
                                                    T_B^epsilon Xi(U;V)]. (H9)

Proof. Fix B. In the all-cut integrand, exp(-delta S) times the first factors
in (H8) equals exp(-delta S_rest), with
`delta S_rest=delta S-sum_(Y in C_2(B))delta S_Y`. Its plaquettes read no
I(B) link. Integrating the original sea coordinates in I(B) therefore gives
product_Y D_Y^0, which cancels precisely the denominators in (H8). What
remains is the original raw integral with zeta_Q on B and chi_Q off B, times
Xi. Summing the finite identity product_Q(chi_Q+zeta_Q)=1 proves (H9).
Every Haar, kernel, vacuum and normalization factor has cancelled by its
identical occurrence, not by an estimate. Fubini is valid for complex sources:
all domains are compact and the finite-volume integrands are bounded.

For Xi=1, (H8) factorizes and (H9) becomes

    Z_epsilon(V)/Z_cut^0(V)
      = E_(nu_cut^0)[ exp(-delta S(U)) G_epsilon(U,V)],
    G_epsilon=sum_(Gamma compatible) product_(Y in Gamma)t_Y^epsilon.
                                                                  (H10)

The polymers Y are nonempty G_2-connected sets. Compatibility means distance
between sets is >=3, equivalently A(Y) and A(Y') are disjoint. There is a
bijection between compatible collections Gamma and their bad-set union B.
This exact gas is not yet small: failure activities still occur.

## 3. An actual completion collar and an exact failure-history sum

Use RLARGE CL's same completion criterion, with all its links retained:

    e_flat(data_Y;Y)=min_(Ucirc in SU(N)^I(Y))[
       max_(plaquettes p wholly in N_1(Y))||I-Ucirc_p||op
       +max_(c in C(Y))||V_c-S_c(Ucirc)||op].                    (H11)

Ucirc agrees with the frozen sea data outside I(Y). S_c is the actual
straight path between anchors. Compactness and continuity give the minimum.
All exterior inputs in (H11) lie in A(Y), and none lies in another component's
I(Y') when the components are G_2-separated. The function is continuous in
real data and its threshold indicator is measurable. It is not holomorphic.

Fix n_* in positive integers or n_*=infinity, and define

    h_Y(data_Y)=1{|Y|<=n_*}1{e_flat(data_Y;Y)<=epsilon_loc},
    a_Y^epsilon=h_Y t_Y^epsilon,
    f_Y^epsilon=(1-h_Y)t_Y^epsilon.                            (H12)

Thus a successful return uses the actual completion collar. Every size or
collar failure is retained in f_Y. In particular no small collar-bad component
is silently thrown away. This is an explicitly constructed, one-generation
classification. It is not an assertion that the earlier unspecified joint
sigma^J or an inherited multilevel history has already been matched. RLARGE's
sample-wise sigma_Q implies a suitable completion when it holds throughout
Y, but its sample-wise hard indicator is not equated with (H12).

For an original configuration U, form B(U) from (H3), then its G_2-components.
Let F(U,V) be exactly the components with h_Y(data_Y)=0. The actual retained
history indicator is

    Xi_F(U,V)=1{F(U,V)=F}.                                    (H13)

The finite family {Xi_F} partitions unity, including possible empty/zero-mass
histories. A failure collection F is compatible. Let P(F) be the successful
polymers compatible with every Y in F, and set

    G_ret,F^epsilon=sum_(Gamma subset P(F), compatible)
                                      product_(Y in Gamma)a_Y^epsilon.

Then the individual history and the full return identities are

    Z_epsilon[Xi_F]/Z_cut^0
       =E_(nu_cut^0)[ exp(-delta S) product_(Y in F)f_Y^epsilon
                                               G_ret,F^epsilon],
    Z_epsilon/Z_cut^0
       =E_(nu_cut^0)[ exp(-delta S) sum_(F compatible)
                        product_(Y in F)f_Y^epsilon G_ret,F^epsilon]. (H14)

Proof. Split each t_Y=a_Y+f_Y in (H10). For the individual-history statement,
apply the same Fubini proof to each original bad set. The value h_Y is
unchanged when ANY of the disjoint component interiors is replaced, since
its completion test depends only on the frozen collar outside their union.
Consequently the success/failure labels in the raw integral and the sea
integrand agree. Summing successful components gives (H14). This last
invariance would fail for a collar reading another replaced interior; it is
why the chosen grouping is a sufficient explicit safeguard. It also makes
compatibility exactly disjointness of the full supports; no minimality of
this grouping is claimed. An arbitrary extra hard insertion still
uses (H8), rather than multiplication by its value on the sea sample.

No history-specific partition function is inverted in (H14). All references
are (H4)-(H5), strictly positive real zero-source integrals. Whether a complex
source makes the integrated Z_epsilon[Xi_F] zero is immaterial to this identity.
The complete failure sum, all exterior gauge data and all large coarse fields
remain present. The next estimate concerns only the a_Y part of this exact
formula.

## 4. Price from the actual normalized Wilson/soft density

This re-derives the needed bare CL estimate, with its actual indicators and
references, rather than importing the effective-level action under a new name.
Let c_H in (0,1] satisfy Haar{||U-I||op<=r}>=c_H r^D for 0<r<=1. Such a
positive fixed-N constant follows directly from the exponential Haar chart on
a fixed ball; it is the same cap bound used by [RLARGE CL](RLARGE.md) and
[LARGE TL](LARGE55.md). Define

    n_l=4L^3(L-1),       n_P=6n_l,       p_L=5L-4,
    A_L=3L(L-1)/2,
    b_1=n_P+12 kappa_max(1+A_L)^2,
    b_0=16n_P+12 kappa_max p_L^2,
    r=epsilon_1/16,
    epsilon_loc<=min{epsilon_1/4,epsilon_1/sqrt(4N b_1)},
    0<epsilon_1<=1,     u>=max{1,1/kappa_min},
    a=epsilon_1^2/(4N),
    P_0=D(n_l/2+8),
    C_0=exp(8+b_0 r^2)c_H^(-(n_l+8))
                                  kappa_max^(8D)r^(-D n_l).       (H15)

These constants are fixed before volume or source number varies. Each fine
link meets six unoriented plaquettes, so |P(Y)|<=n_P|Y|; |I(Y)|=n_l|Y| and
|C(Y)|<=8|Y|. The constants may be very large. The theorem asserts existence
of a sufficiently large u at these fixed parameters, not a practical value.

For any actual mean M of unitary contours, ||M||op<=1. If V_0 maximizes
Re tr(V^-1 M), then on the radius-1/t Haar cap about V_0 the kernel exponent
loses at most 1. Thus

    k_t(V;M)<=e c_H^(-1)t^D,       t>=1.                         (H16)

This bound uses the ACTUAL kernel normalizer. Also its uncentered normalizer
is <=1 because phi_M>=0, so k_t>=exp(-t phi_M). These upper/lower estimates
are used in different places and neither removes log N_t from the action.

On zeta_Y=1, every Q supplies a distinct interior plaquette with
s(U_p)>=epsilon_1^2/(2N). All remaining Wilson terms are nonnegative. Haar
mass is one. Therefore

    N_Y^0 <= [e c_H^(-1)(kappa_max u)^D]^(8|Y|)
                                 exp[-u epsilon_1^2|Y|/(2N)].    (H17)

When h_Y=1, choose a minimizing completion Ucirc from (H11). Restrict every
integrated link to ||U_b-Ucirc_b||op<=r g. Telescoping unitary products gives
||I-U_p||op<=epsilon_loc+4rg<=epsilon_1/2, so every actual chi_Q equals one.
Moreover s(U_p)<=epsilon_loc^2+16r^2g^2. The paired S4' contour differs from
the straight anchor path by at most A_L completion-plaquette norms: attach
the L-by-1 ribbons along the transverse axial path, whose total transverse
length is at most 3(L-1)/2. All these plaquettes lie in the two endpoint
blocks, hence N_1(Y). Therefore

    ||V_c-T_c^sigma(U)||op
       <=(1+A_L)epsilon_loc+p_Lrg.

The actual arithmetic contour mean gives
`phi_M(V)=average_sigma,y s(V^-1 T_y^sigma)`; hence its contribution is
bounded by the same squared-distance bound. Using (x+y)^2/2<=x^2+y^2 and
then enlarging 8 to 12 yields on these caps

    w_Y^0 >= exp[-u b_1 epsilon_loc^2|Y|-b_0r^2|Y|].

There is no gauge fixing: cap volumes multiply in the original independent
Haar coordinates, around the actual completion. Consequently

    D_Y^0 >= [c_H(rg)^D]^(n_l|Y|)
                       exp[-u b_1 epsilon_loc^2|Y|-b_0r^2|Y|],
    h_Y N_Y^0/D_Y^0 <= [C_0 u^(P_0)exp(-a u)]^|Y|.             (H18)

This applies to G_2-connected Y of any size; connectedness was not used in
the price. The cap constants do not grow with the box enclosing Y. It also
explains why an arbitrary completion-bad component has not been priced.

Now restrict ONLY the original coefficient sources by

    |epsilon_p|<=lambda/u,       0<=lambda<infinity fixed.       (H19)

Since 0<=s<=2 on real SU(N), |delta S_Y(U)|<=2lambda n_P|Y|.
The same bound applies to the source in N_Y^epsilon. Combining both factors
in (H6), not just the numerator, gives the actual source-uniform price

    sup_(real U,V; (H19)) |a_Y^epsilon(U,V)| <= q(u,lambda)^|Y|,
    q(u,lambda)=exp(4lambda n_P) C_0 u^(P_0)exp(-a u).          (H20)

Every t_Y is gauge invariant under the joint transformation of its actual
fine/coarse data: change variables in the integrated interior links, use Haar
invariance and the gauge covariance of the paired contour means. The same
holds for h_Y because the completion set is carried bijectively to the new
completion set and both norms in (H11) are invariant. Fixed block translations
and hypercubic symmetries carry these families covariantly, with their
coefficient labels carried along. No gauge-variant proxy observable is used.

This is entire original-source dependence and a pointwise bound at EVERY
real coarse field. The hard completion selector can be used in this bound
because it is source-independent. It remains a hard function of real sea
and coarse fields; no coarse holomorphy is asserted for h_Y a_Y.

The restriction (H19) is appropriate to a fixed external Wilson-energy
source: epsilon_p=-h(p)/u with ||h||infinity<=lambda. It is not the largest
source class supplied by the same estimate. The following corollary was
identified after the initial checks and is checked separately before freeze.

**Fixed relative-source corollary.** Choose fixed rho>=0 and lambda>=0 with
`rho<a/(4n_P)`, and put

    D_(rho,lambda)(u)={epsilon: |epsilon_p|<=rho+lambda/u},
    a_eff=a-4rho n_P>0,
    q_(rho,lambda)(u)=exp(4lambda n_P)C_0 u^P_0 exp(-a_eff u).
    sup_(real U,V; D_(rho,lambda)(u)) |a_Y^epsilon|
                                      <=q_(rho,lambda)(u)^|Y|. (H20c)

Indeed |delta S_Y|<=2(u rho+lambda)n_P|Y| both in the compensator
and the numerator. Multiplying these two bounds and (H18) proves (H20c)
without changing the denominator, kernel or completion test. In particular

    rho_0=a/(8n_P)>0, lambda=0  gives  a_eff=a/2,              (H20d)

a fixed original-relative-coefficient polydisc independent of u,T,history
and source count. Formula (H20) is exactly the case rho=0, with a_eff=a.
The bound retains its conservative two-factor source cost. The necessary
strict positive remainder a_eff is explicit; no suppression at or above
rho=a/(4n_P) follows from this estimate.

This convention is the bare field u(1+epsilon) in [SRC2 section 3.2 and
MB](SRC2_55.md): only the bare Wilson coefficient changes, and the prescribed
RG kernel K remains fixed. SRC2's rho_0 is an existential positive constant,
so (H20d) supplies a possible radius for THIS producer without assuming a
specified larger radius. Its completed representation also requires the
normalized sea expectation, flow, all coarse fields after integration and
all levels. Those requirements do not follow from the radius corollary.

### 4.1 A frustrated-data stress test; the selector is essential

Zero-source normalization does not make arbitrary hard histories rare. Here
are two actual-model checks of the domain distinction.

First, if a coarse plaquette P has ||I-V_P||op=2 and all four of its coarse
links belong to C(Y), any completion in (H11), with maximum fine curvature
A and straight-link mismatch B, satisfies

    2<=L^2 A+4B<=L^2(A+B),  hence e_flat>=2/L^2.              (H20a)

The first inequality fills the coarse straight square by its L^2 actual fine
plaquettes, then telescopes its four links against V. The square lies in
N_1(Y) when Y includes its four endpoint blocks. Thus a sufficiently small
completion threshold excludes this coarse holonomy. There is no claim that
the conditional density of such a field is small merely because D_Y^0>0.

Second, take N=2,L=3 and vary the single central fine link U of one block Q,
fixing all other fine links incident to it to I. Its six Wilson plaquettes
all have s(U_p)=s(U), and they lie in Q. Set the eight coarse links incident
to Q equal to -I. Exact paired-contour enumeration gives

    M_c(U)=(1-p_c)I+p_c U^(sign_c),
    p_(out,0)=4/27, p_(in,0)=1/9,
    p_(out/in,mu)=10/81 for mu=1,2,3; sum_c p_c=1.

The signs are plus for outgoing and minus for incoming. These finite counts
are exhaustively verified from all 8*24*3^4 actual contour words in the author
checker; no continuum approximation enters. Write U=cos(theta)I+i sin(theta)
n.sigma. Then a_c=1-p_c(1-cos(theta)), M_c has singular radius
r_c=(a_c^2+p_c^2 sin(theta)^2)^(1/2), and the centered exponent at V_c=-I
is a_c+r_c. On the cut-good set, 1-cos(theta)<=epsilon_1^2/2 and r_c>=a_c>0.
Using (H16)'s centered form and dropping the nonnegative Wilson action gives

    W_good <= [e c_H^(-1)t^3]^8
                               exp[-16t+t epsilon_1^2],

where W_good is the unnormalized one-link conditional integral, t=kappa u.
In the radius-r_0 cap about -I, 1-cos(theta)>=2-r_0^2/2. If
2-r_0>epsilon_1 this cap is cut-bad. The exact uncentered normalizer <=1,
the cap mass and the Wilson bound supply

    W_bad >= c_H r_0^3 exp[-12u-16t+t(2-r_0^2/2)],
    W_good/W_bad <= [e c_H^(-1)t^3]^8/(c_H r_0^3)
           *exp[-{kappa(2-r_0^2/2-epsilon_1^2)-12}u].        (H20b)

With epsilon_1=1/2,r_0=1/10,kappa=10 the coefficient in braces is
109/20>0, so the conditional cut-failure probability tends to ONE as u grows.
This is a conditional single-link slice of the actual Wilson/soft density,
not an assertion about D_Y^0 with every interior link integrated.

To make this a completion-bad collar configuration while leaving every other
cube cut-good, fix the INTER-BLOCK fine link `(1,3,3,3)->(2,3,3,3)` to -I;
all its neighbouring links are I. Its transverse plaquette has holonomy -I
and lies between the collar blocks (0,1,1,1) and (1,1,1,1), both in N_1(Q).
No cube-interior plaquette reads this inter-block link, so no additional
zeta cube is created. This plaquette is untouched by every completion on
I(Q), and those two blocks are outside the endpoint blocks of the eight
kernels just used. It forces e_flat>=2 without changing the displayed
one-link conditional density. When the central link is cut-bad, the actual
bad component is just Q, h_Q=0, and its contribution stays in f_Q in (H14).
The price (H18) was never applied to it. This explicit stress test rejects applying q(u,lambda)^|Y| to
all histories; it neither estimates nor discards the failure/sea sum.

## 5. Connected original-source logarithms of the returned gas

Here the sea sample U and real coarse field V stay fixed. This section proves
a pointwise gas theorem for the ACTUAL weights (H6),(H12),(H20). It does not
integrate (H14) or imply clustering of nu_cut^0.

Fix a desired block-support rate mu>=0. In this section choose either
(H20) or (H20c), write its bound as q, and use its corresponding a_eff
(a_eff=a for (H19)). All suprema use D_(rho,lambda)(u). Put

    s_0=81,  Delta=5^4-1=624,  A_0=Delta^2,
    r_q=q exp((mu+1)s_0),
    d_q=s_0 r_q/(1-A_0 r_q),
    require A_0 r_q<1 and d_q<=1/4.                           (H21)

An explicit sufficient threshold is obtained without solving an asymptotic
inequality. Set

    B_*=log C_0+4lambda n_P+(mu+1)s_0+log(2A_0+8s_0),
    u>=max{1,1/kappa_min,(2P_0/a_eff)^2,2max(B_*,0)/a_eff}.     (H21a)

For u>=1, log u<=sqrt(u), and hence P_0 log u<=a_eff u/2 at this
threshold. Thus r_q<=1/(2A_0+8s_0), which implies both conditions in
(H21). All constants are uniform in T, U,V, n_* and failure collection F.
For a fixed block x, the number of G_2-connected sets of size m containing x
is at most Delta^(2m-2): choose a deterministic spanning tree rooted at x and
its depth-first traversal; the visited set recovers the original set. If
x belongs to A(Y), a root of Y lies in N_1(x), of size at most s_0. Thus

    sup_x sum_(Y: x in A(Y)) |a_Y^epsilon| exp((mu+1)|A(Y)|)
       <= s_0 sum_(m>=1)A_0^(m-1) r_q^m = d_q.                (H22)

This pays both animal entropy and the complete actual collar/source support.
It is not a bound inferred only from matrix entries or fixed derivatives.
Small tori reduce the degree, support sizes and number of sets; the same
bounds remain valid without any T>=R requirement.

For clarity, the cluster step is stated with its exact labels. Let
`J(Y,Y')=1` when A(Y) intersects A(Y'), including Y=Y'. For an ordered tuple
(Y_1,...,Y_n), let phi^T be the sum over connected graphs on {1,...,n} of
product_edges[-J(Y_i,Y_j)], with phi^T=1 when n=1. Define

    V_X^F(epsilon;U_X,V_X)
       =sum_(n>=1)1/n! sum_(Y_1,...,Y_n allowed by F;
                              union_i A(Y_i)=X)
                         phi^T(Y_1,...,Y_n) product_i a_Yi^epsilon.
                                                                  (H23)

Each nonzero term has connected X in the nearest-neighbour block graph.
Every original coefficient and every actual sea/coarse field read occurs in
X, before and after summing histories at FIXED F. The F dependence in (H23)
is only the explicit allowed-polymer list; it adds no remote source argument.
A hard h_Y can enter as a bounded local coefficient in U,V because the only
analytic variables claimed here are the original epsilon_p.

The repulsive hard-core tree bound used in the independently reviewed
[CX-R proof](RECOVERY_CLUSTER_ASTRA.md) applies directly: replace
|a_Y| by w_Y=|a_Y|exp(mu|A(Y)|). The sum of child weights incompatible with
a root Y, with the root-child tree majorant exp(|A(Y')|), is at most
`d_q |A(Y)|<=|A(Y)|`, by marking an intersection vertex and using (H22).
The rooted-tree recursion therefore bounds the total rooted cluster at Y
by w_Y exp(|A(Y)|). The repulsive graph-to-tree inequality, with no signed
probability interpretation, then gives after marking a polymer containing x

    sup_x sum_(X contains x) exp(mu|X|)
         sup_(real U,V; D_(rho,lambda)(u)) |V_X^F| <= d_q.                 (H24)

One may take a common nonnegative coefficient majorant independent of F,U,V
by replacing every activity by q^|Y| before these sums. This permits all
subtractions below coefficient by coefficient. The same argument applies to
any excluded list of polymers. It proves absolute convergence before the
logarithm is used. The finite-gas formal connected-graph identity and analytic
continuation from a scalar activity multiplier 0 to 1 give exactly

    G_ret,F^epsilon=exp(sum_X V_X^F),     G_ret,F^epsilon!=0.  (H25)

This does NOT assert nonvanishing of any f_Y, Xi_F numerator, or the sea
average in (H14). The source-normalized returned logarithm is the exact sum
`sum_X[V_X^F(epsilon)-V_X^F(0)]`, with rooted norm <=2d_q, and every summand
vanishes at zero source. It is strictly local in the ORIGINAL fine
coefficient coordinates; no substitution b(B,epsilon) is needed. Cauchy on
an inner polydisc gives the usual derivative bounds with explicit radius
rho+lambda/u when positive, including the fixed radius (H20d); finite
derivative tests are not used as a
substitute for this all-order construction.

The units of (H24) are level-zero blocks, one containing L^4 fine sites.
If a consumer instead groups R^4 such blocks into one R-box, map each X to
its set of R-boxes, preserving all local data. Connectedness is preserved,
|image X|<=|X|, and the rooted norm is at most R^4 d_q (the actual maximum
number of blocks per box if smaller). R is fixed before choosing u. No
uniformity in RG depth or changed higher-level actions follows from this
conversion.

### 5.1 Exact excluded-history and boundary comparisons

Write A_F=union_(Y in F)A(Y). The allowed gas is exactly the same set of
activities with A(Y) disjoint from A_F. Canonical (H23) coefficients cancel
when their union X is disjoint from A_F. Thus

    log(G_ret,F/G_ret,empty)
        =-sum_(X intersects A_F)V_X^empty,
    absolute value <= d_q |A_F|.                              (H26)

The equality uses the fact that an excluded activity has support intersecting
A_F; the common coefficient formula agrees for all the others. All factors
in (H26) are the source-dependent ones at the same epsilon. Taking its
source difference costs at most 2d_q |A_F|. A bound on this extensive log is
not a bound independent of |F| on its exponential.

For a sharper comparison, for any block set O define G_O by keeping only
activities with A(Y) contained in O. On the finite torus Omega,

    log G_Omega-log G_O-log G_(Omega minus O)
       = sum_(connected X meeting both sides)V_X.             (H27)

Every such nearest-neighbour connected X meets the inner vertex boundary
of O. By (H24) the right side has modulus at most d_q |boundary_in O|.
The same statement holds for the source difference with 2d_q. This supplies
a boundary price for this returned gas, with its full interior factor G_O
retained. It does not erase the interior reference or prove COL compatibility
of the sea average: the boundary activities still READ the actual cone/sea
links. LARGE55's multilevel I5 needs that additional integration argument.

## 6. Relation to the old denominator and complex coarse fields

The raw D_Y^epsilon in (H4) is exactly RLARGE's source-perturbed cut-good
inner denominator, including all boundary links, action and normalized kernel.
For fixed real data it is entire in epsilon but need not be zero-free on a
size-independent disc for all |Y|. The construction above requires only
D_Y^0>0 and bypasses such an inference. It does not reinterpret the old
quotient as (H6); their relation is (H7).

There is a separate elementary, limited domain where the old denominator is
zero-free. Let |Y|=m, keep the exterior fine links real and fixed, and write
each coarse link in C(Y) as V_c=W_c exp Z_c, W_c in SU(N), Z_c traceless
complex, ||Z_c||op<=r_c. The holomorphic kernel numerator is

    exp[-kappa u(1-(tr(V_c^-1 M_c)+tr(M_c^*V_c))/(2N))],

where M_c and M_c^* are functions of the REAL integration/exterior variables;
the actual kernel normalizer is unchanged. The exponent change from W_c
has modulus <=kappa_max u(exp(r_c)-1). On the fixed Haar/cut domain, therefore

    |D_Y^epsilon(V)/D_Y^0(W)-1| <= exp(A_m)-1,
    A_m=2u rho n_P m+8 kappa_max u(exp(r_c)-1)m,
    |epsilon_p|<=rho.                                         (H28)

For A_m<log 2 this proves nonvanishing and a specified logarithm near 1.
It holds at arbitrary real coarse centres W. At m<=n_*<infinity it supplies
an explicit common epsilon/coarse neighbourhood by choosing the two terms
small enough. Its coarse width is O(1/(u n_*)), not the O(g) tube claimed by
the full return consumer. The unrestricted-size theorem (H25) uses no such
coarse extension and allows either source radius (H19) or (H20c).

The hard completion selectors in (H12), and hard Xi_F in (H13), remain
functions on REAL coarse data. (H28) for the unselected integrals does not
make those selectors holomorphic. Their sum reconstructs the analytic raw
integral; individual selected pieces may fail to be analytic in coarse B.
This is the precise difference from source holomorphy at fixed real data.
No contour deformation of a hard cutoff, no complex indicator and no unit
Jacobian for an unperformed chart change is assumed.

## 7. Author evidence, checkpoint and exact remaining work

The source construction was saved before the first checker execution. The
final [exact checker](checks/source_history_return_exact.py),
[actual S4/SU(2) checker](checks/source_history_return_su2.py), and
[fixed-radius checker](checks/source_history_return_radius.py) completed with
exit code zero and empty stderr. Their final outputs are
[exact attempt 04](checks/source_history_return_exact_attempt04.json),
[SU(2) attempt 03](checks/source_history_return_su2_attempt03.json), and
[radius attempt 01](checks/source_history_return_radius_attempt01.json).
They report **54 checks and 20 controls, 74 predicates in total**, all true.
The controls include explicit omitted-factor calculations and structural
counterexample witnesses; this is not a claim of 20 separate mutated-runner
executions. Elapsed times reported internally were about 0.60 s, 6.65 s and
0.002 s.
Exact commands, source/output hashes, runtime versions and freeze time are
bound by the [checkpoint receipt](checks/source_history_return_receipt.json).
These are author checks, not a fresh referee or formal verification.

- **Exact raw replacement.** Direct enumeration of 256 four-interior states,
  with 16 all-cut sea states, normalized boundary-dependent kernels and
  separately labelled rational-complex source factors, agrees exactly with
  (H9). The 16 compatible bad-component collections and their actual failure
  histories reproduce the direct raw integrals individually. Omitting the
  compensator, freezing the denominator at different boundary data, dropping
  the kernel normalizer, dropping an exterior source-only factor, or dropping
  the common vacuum/reference factor gives a different rational-complex value.
  An impossible history is retained as zero, without division by its mass.
- **Hard histories and original sources.** A correlated insertion reading
  both replaced interiors agrees with the JOINT replacement integral.
  Evaluating it on the unreplaced sea, or replacing it by the tested product
  event, fails. An unmerged collar selector changes when its neighbour is
  replaced; grouping the two interiors restores its invariance. Changing a
  remote original coefficient outside P(Y) leaves the activity exactly
  unchanged, while changing a local original coefficient changes it.
- **All-order proof mechanism checked at finite order.** For the three-polymer
  path gas Z=1+a+b+c+ac, direct formal logarithm coefficients through degree
  four agree with independent connected-graph enumeration, including repeated
  polymers. The coefficient abc is 1 while ac is 0: the remote contribution
  needs its connector. Exact support unions, excluded-side cancellation and
  the crossing-boundary terms are checked. The infinite-order conclusion is
  the written tree bound (H22)-(H25), not this finite enumeration.
- **Fixed relative-source radius.** After the coordinator identified the
  stronger direct bound, six exact arithmetic predicates and two controls
  checked (H20c)-(H21a) on 16 parameter choices and 96 exponent evaluations.
  The mixed source cost equals the stated a_eff formula; rho=0 recovers
  (H20), while rho_0=a/(8n_P) leaves exactly a/2. Reusing the original decay
  at positive rho fails, and the critical rho=a/(4n_P) leaves no positive
  decay budget in this bound. The revised u threshold pays the polynomial
  and entropy costs. This corrects an unnecessarily restrictive initial
  domain statement; it does not price a failed history or the sea integral.
- **Actual geometric incidence.** On the periodic T=2,L=3 four-dimensional
  lattice, the checker enumerates 5,184 fine links and all paired contours.
  Each block has 216 interior links, each fine link meets six plaquettes,
  and the actual single-block P(Y) count is 648, below the safe 1,296 bound.
  Every contour stays in its two endpoint blocks; an interior link is read
  by at most eight coarse kernels and an inter-block link by at most one.
  The written proof supplies the bounds for general fixed L,T.
- **Actual nonabelian Haar slice.** Fix all fine links except one central link
  to I and keep the eight actual S4 means. Noncommuting SU(2) coarse matrices
  in two different Lie directions are checked by exact matrix/quaternion
  algebra. The Haar normalizer is retained as H(x)=2 I_1(x)/x, verified both
  by ten exact Haar moment coefficients and by its Haar integral. Independent
  theta and quaternion-scalar coordinates agree for good/bad integrals and
  the source compensation at 65 decimal digits, tolerance 1e-45. The return
  error was about 1.5e-67; removing its compensator changes the result by
  about 0.02498. Normalizer, nonlinear cut-boundary and coarse-axis omission
  controls also fail as required. These are non-interval quadratures and a
  conditional one-link slice, not the full cube Haar integral.
- **Frustrated conditional data.** The exact word counts in (H20b) and its
  positive exponent 109/20 are checked. At u=20,kappa=10 the same actual
  one-link conditional model gives log10 P(cut-good) about -226.96. The
  inter-block rough collar is checked to leave all cube-interior cuts and
  the eight relevant kernel means unchanged, while forcing completion
  failure. The asymptotic statement follows from the written cap inequalities;
  the displayed finite number is a non-interval diagnostic. It is not an
  unconditional Wilson-measure counterexample.

**Preserved failures and corrections.** The first exact execution stopped
at an assertion expecting at least one of the fixture's admissible failure
collections to have zero mass. All those collections were realized: this
was an unsupported fixture expectation, not a failure of the replacement
identity. Its [original source](checks/source_history_return_exact_attempt01.py),
[empty stdout](checks/source_history_return_exact_attempt01.json) and
[assertion traceback](checks/source_history_return_exact_attempt01.stderr)
are retained. The corrected check constructs an explicitly impossible
history and verifies its zero integral. Later exact versions strengthen the
collar/connector tests and vary independently labelled source coordinates;
the earlier successful versions and outputs are preserved. The initial
frustrated-collar probe used a rough interior plaquette in a diagonal block;
that would create another bad cube. The final probe instead uses the explicit
INTER-BLOCK link in section 4.1 so that no new interior-cut failure is created.
The earlier SU(2) source/output versions are retained and do not certify this
additional final property. A first packaging pass also rejected a stale cached
hash for the mutable earlier repair-provenance JSON. Its current bytes match
the coordinator's committed review update and the frozen repaired-source
hashes; the [packaging failure record](checks/source_history_return_packaging_attempt01.json)
preserves that distinction. All seven frozen science/review/receipt inputs
matched. No failed run is reported as a completed pass.

**Provenance and prior-art scope.** The complete corrected predecessor and
complete fresh review were read. Exact current consumer ranges in STEP,
LARGE, SRC2, B2 and their reviews, together with RLARGE's full actual return,
CL and ribbon proof, PLD's sea/collar obligation, Decision 4 and the relevant
paired-contour implementation, are listed in the
[read coverage](checks/source_history_return_read_coverage.json). Unchanged
prior procedure/primitive and generic-cluster reads are reused at their
recorded scope. A combined instruction refresh was truncated; it is not
represented as a new complete read. Current-main statement searches at
`ca2bc7ddf64790da96cd43d42017d000fbfe4808` used zero-source-denominator/return,
source-dressed-gas, source/sea compensation, fixed-reference-hard-history and
completion-collar/source variants. Hits were unrelated scalar-source/compiler
and record notes; no matching construction was found in those searches.
The closest actual result is RLARGE's zero-source CL/Fubini rewrite. The new
step is its explicitly compensated original-source replacement with genuine
hard histories, a completion-gated pointwise complex-source gas, and an exact
failure/reference partition. This is limited repository novelty evidence,
not a claim of literature priority or a new version of the old bare CL price.

**Frozen positive scope, subject to fresh independent review.** (H9) and
(H14) rewrite the FULL level-zero raw Haar density, with arbitrary hard
insertions handled by (H8), every complement retained, and no chart or complex
history denominator substituted. The smallness conclusion is only for
`a_Y=h_Y t_Y`: it follows from the ACTUAL bare Wilson/soft action and the
explicit completion caps, then gives (H23)-(H27) on the original source discs
(H19),(H20c), including a fixed positive relative radius, for arbitrary real
sea/coarse fields. This pointwise source-local
logarithm is a new producer input to a sea calculation, not that calculation.

The still-unestimated expression is precisely the expectation in (H14):
`E_nu_cut^0[exp(-delta S) sum_F product f_Y exp(sum_X V_X^F)]`.
The failure weights f_Y and their interaction with this sea need control;
zero-source denominators, the small successful gas and the boundary identity
do not supply it. Hard completion/actual-history selectors have no asserted
complex-B continuation. The one-step classification is not an already proved
multilevel inherited-history construction. Higher-level actions need their
actual analogues of (H2),(H17),(H18), including inherited interactions and
renormalization; the minimum-defined E_NA is not relabelled as E_cb. A prescribed radius beyond (H20c), the large-coarse-field source density after
the sea average, full N1/N2, OS0–OS3 existence and physical mass gap remain open.
No covariance, gas norm, cap price or conditional tail is identified with a
physical spectral gap.

The next concrete task is to integrate these exact local replacements against
the actual cut sea while retaining the completion-bad families, first on a
specified collar domain. It must prove a source-local normalized sea estimate
or a separately priced larger defect architecture; merely renaming this
remaining expectation as a new polymer theorem would not close it.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Exact bare hard-history return and completion-good source gas; the failure/sea sum, induction, existence and physical gap remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

No frozen predecessor/report, shared summary or audit surface was edited.
No git/PR operation, worker spawn, permission prompt or physical-axiom change
was performed. The coordinator owns commit, push and fresh independent review.
