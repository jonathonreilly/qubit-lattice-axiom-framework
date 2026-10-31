# Actual bare-return jets in original source and coarse-link units

This supplies finite ordered real coarse/source jets of the actual bare
connected original-cut return, with every original reader retained. There
are two distinct constructions: fixed-center output jets obtained from
the holomorphic producers, and real moving-center jets obtained after an
exact Haar pullback and a finite Taylor lift of the rough insertions. The
second construction does not continue a rough mean to complex arguments.
It includes the moving finite-core covariance and its determinant.

The native REALRGA/MIXSMALL input rate mu+2 is not established here. A
smaller-rate finite-jet product/tree interface has an explicit smallness
threshold. Fully integrated output jets supply no retained fine-field jet
estimate. The complete critical action, determinant, kernel vacuum and
Wilson matching remain separate. All-history closure, extraction,
non-free continuum existence and a physical continuum mass gap remain OPEN.

    actual_current_surface_status: bounded-support
    author_proposal_status: pending_fresh_independent_review
    target_claim_type: bounded_theorem
    trace_class: upstream_support
    reachability_to_target: partially_closes
    audit_required_before_effective_retained: true
    bare_retained_allowed: false
    full_existence_established: false
    physical_continuum_mass_gap_established: false

Bałaban's gauge localization and Dimock's exposition are antecedents. The
supplied bare action is a premise; no scalar/d=3 conclusion, new physical
axiom or review verdict is used as a mathematical premise.

The local antecedents are [SC](SOURCE_LOCAL_COMPACT_RETURN_ASTRA.md),
[RF](REGIONAL_CRITICAL_FIELD_ASTRA.md),
[NR](NONLINEAR_READER_RETURN_ASTRA.md),
[RC](REGIONAL_CHART_RETURN_ASTRA.md),
[CG](COMPACT_RETURN_GLUING_ASTRA.md), and
[MK](MARKED_COMPACT_CHART_ASTRA.md). Their exact consumed identities
and bounded read coverage belong to this source's post-freeze manifest.

## 1. Exact consumers, producers and units

Read [REALRGA](REALRGA.md), especially RGA2--RGA4, RGA7--RGA10 and
RGA14--RGA17, [REALRGB](REALRGB.md) G1/G6--G9/G30--G35,
[MIXSMALL](MIXSMALL.md) MS3--MS9, and [EXTCONT](EXTCONT.md)
E2--E4/E10--E17. Their contracts are different:

* REALRGA has total fine-plus-coarse order p=6 and source order q_src=4,
  separately, not total mixed order four. Its field directions have
  max-link operator norm at most h_level=sqrt(N/u_level). Its original
  absolute-source directions satisfy |xi_p|<=r_p, with frozen weights r_p.
* REALRGB G1 has total order four on the joint relative-source/coarse
  space with the l1 direction norm. That bound alone gives neither the
  order-ten mixed jets nor a volume-independent dense-direction bound.
* The RGA Mayer input is an UNREGULATED jointly integrated jet bound.
  Multiplicity regulators multiply with m+n on overlaps. No single-copy
  regulator bound is substituted for this input.
* The output reader is the entire original microscopic connected reader,
  including inactive, source, covariance, boundary and normalization
  readers. Endpoint support, field support and a new macro-cell graph
  cannot replace it.

For one fully integrated output function F define explicitly

    D_B F(V)=d/dt F((exp(t B_c)V_c)_c)|_(t=0),
    T_(h,r)^(6,4)(F)
      =sum_(m=0)^6 sum_(n=0)^4 [1/(m! n!)]
          sup_(max_c||B_ic||op<=h, |xi_jp|<=r_p)
                |D_B1 ... D_Bm D_J,xi1 ... D_J,xin F|.           (WR1)

Use the displayed invariant derivative convention regardless of the name
given to left/right invariance. Operators in a word keep their order.
All fine variables have actually been integrated in WR1. An unresolved
fine/exterior variable is not removed by setting its derivative to zero.
The inherited full-history function rho_j is not replaced by a bare b_j.

At this one bare step the original Wilson coupling u0 IS the displayed u.
The exact source change is

    -u sum_p(1+epsilon_p)s(U_p)=-sum_p(u+J_p)s(U_p),
    J_p=u epsilon_p, D_J,xi=u^-1 D_epsilon,xi.                    (WR2)

Hold u, kappa, every normalized kernel and every other coupling fixed.
If a consumer's original source uses u0 instead of this step's u, replace
the denominator u everywhere below by that actual u0; no scale identity
is inferred. Differentiation of a running coupling is a different operation.

Take N>=2, odd L>=3, T>=2, the original pinned-tree quotient, all free
whole links, and all root/harmonic/crossing/colour modes. Write

    D=N^2-1, m0=3L^4+1, k=D m0, sigma^2=N/u,
    beta=(16 R)^-4, gamma=beta/2.                                (WR3)

R is ONE fixed ambient patch radius satisfying the RF/NR/MK requirements.
Its geometry-only patch cutoffs, original labels and orderings are fixed
before shrinking any radius. If R is changed, beta must be recomputed.
Use rho>0 fixed before u, q and K. With the exact SC shell K(q), set

    p_cut=log(2+u)^alpha, alpha>5/2, r_a=sigma p_cut,
    q=c_q sigma^2 p_cut^2, V_K=(4K+1)^4, H_K=(8K+9)^4,
    delta=d_delta sqrt(q)/(4K+1)^2,
    eta=d_eta sqrt(q)/(4K+1)^2.                                  (WR4)

All positive constants satisfy the actual SC/RF/RC/FT restrictions; the
further explicit choices for moving-center jets are in section 7.
The source symbol q_src=4 is unrelated to the charge threshold q.

The fixed-center objects in [FT](FROZEN_TRANSPORTED_CHART_ASTRA.md)
FT37--FT38 and [HC](HOLOMORPHIC_COMPACT_RETURN_ASTRA.md) HC31--HC40 are

    Z_a^fr=P_fr exp(sum_Y H_Y^fr),
    log(Z_a^fr/Z_a^tr)=sum_Y R_Y^tr,
    log(Z_cut/Z_a^fr)=sum_Y Psi_Y^comp.                           (WR5)

Their coefficient envelopes, with individual suprema inside the sum, give

    ||H^fr||_gamma <= A_ch=C1 sigma^2
                       +C2(1+p_cut^(91D+2))exp(-a p_cut^2/64),
    ||R^tr||_gamma <= A_tr=C3(eta/sigma)
                       (1+p_cut^(91D+1))exp(-a p_cut^2/64),
    ||Psi^comp||_gamma <= A_comp=exp(-kappa_c p_cut^2),
    kappa_c=c N c_q/32.                                          (WR6)

The first two clauses use FT787, SHA256
c7cea2f9bb096af300a9a978c945d9c5d68ae5e63581654a3034902d000d70b8.
The third uses the EXACT frozen HC734, SHA256
890a56113ad3ceac890ec72efe59b40f73bbda283c8dfb69c331bc4ea5376c49.
The parent reports HC's separate fresh review is complete without source
changes. Its frozen mathematics, not that verdict, supplies the third
clause. The moving-center construction below instead uses MK's real
identity and its explicit density proof, RF/NR/RC's chart libraries and
MS's real calculus. This new finite-jet extension awaits its own review.

In WR5, V=exp(v)Vbar and Vbar, the physical chart and all selectors remain
FIXED while v varies. Each Y reads the actual (Vbar,v,epsilon) on Y.
Sums of H^fr+Psi^comp or Psi^comp+R^tr have the sum of the two stated
bounds. Keep the distinct compact and transport exponents. In every case

    P_fr=h_N^n(2pi sigma^2)^(d/2)
                   exp[-LogDet K_fr/2-F_fr(b_fr)/sigma^2]          (WR7)

is retained exactly once, with all kernel vacua and Haar terms restored.
No estimate in this source makes log P_fr small.

## 2. Actual ordered Lie jets on a strictly smaller center chart

Evaluate WR5 at real V=exp(vhat)Vbar, max||vhat||HS<eta/4,
real |epsilon_p|<rho/4, and eta<=1/64. Keep Vbar fixed. For an ordered
word use the genuine composition

    V_c(t)=exp(t_m B_mc)...exp(t_1 B_1c)exp(vhat_c)Vbar_c,
    v_c(t)=Log[exp(t_m B_mc)...exp(t_1 B_1c)exp(vhat_c)].          (WR8)

Then partial_(t_1)...partial_(t_m) F(V(t)) at zero is the ordered
D_B1...D_Bm F. The reversed exponential order in WR8 is intentional.
On the fixed principal log neighborhood, the exponential product series
gives ||P-I||HS<=exp(sum||t_i B_i||HS)-1. The logarithm series, telescoped
term by term, is Lipschitz with constant at most two when both matrix
arguments are within operator distance 1/2 of I. Thus

    ||v(t)-vhat||HS <=4 sqrt(N) h sum_i |t_i|.                    (WR9)

Choose |t_i|<=eta/(16 m sqrt(N)h) for m>0. The displacement is <=eta/4,
so the image stays inside the eta/2 tube. This checks the group vector
field coefficients and their derivatives by actual composition; an
ordinary coordinate derivative is not renamed an invariant derivative.

Put r_*=max_p r_p, and epsilon(s)=epsilon+sum_(j=1)^n s_j xi_j/u.
Taking |s_j|<=u rho/(4n r_*) leaves the source in the rho/2 polydisc.
If a weight is zero its direction is absent. With an envelope a_Y for
F_Y on the full product tube, joint Cauchy in these independent variables
gives

    |D_B^m D_J^n F_Y|
      <=a_Y (16m sqrt(N)h/eta)^m (4n r_*/(u rho))^n.             (WR10)

Every parameter is differentiated once. There is no additional m!n!
in WR10. Repeated physical directions are permitted as distinct formal
parameters. Put 0^0=1 and

    P6(x)=sum_(m=0)^6 (16m)^m x^m/m!,
    Q4(y)=sum_(n=0)^4 (4n)^n y^n/n!.
    ||F||_(gamma;6,4;h,r)
      <= ||F||_gamma P6(sqrt(N)h/eta) Q4(r_*/(u rho)).            (WR11)

This is a direct dense max-link estimate, independent of reader size and
volume. It is not conversion of REALRGB's l1 estimate. It applies to each
WR5 family and their stated sums, with its own actual envelope.

Recentring this SAME function at Vhat means substituting
v=Log(exp(w)exp(vhat)), with Vbar fixed. Re-running HC with Vhat as the
physical center changes its selectors, chart and coefficient library.
WR11 alone does not differentiate V -> Psi(V,0), or produce a coherent
global real potential by choosing a new center at every point.

## 3. Complete label counts and actual test-function pairings

An original coarse block owns four positive coarse links and at most
6L^4 original positive plaquette source labels. A complete reader Y
contains the owners of every argument it reads. Therefore

    #coarse scalar coordinates read <=4D |Y|,
    #original plaquette source labels read <=6L^4 |Y|.            (WR12)

These are counts at ONE bare step. Seams and repeated plaquette
occurrences do not identify distinct original source labels. A deeper
ancestor family needs its actual new label count; WR12 is not a depth
independent all-history statement.

Choose an HS-orthonormal su(N) basis T_alpha, so ||T_alpha||op<=1.
Expand dense directions componentwise; every component of an operator
norm h array is at most sqrt(N)h. Define T_abs by summing the absolute
ordered scalar jets, with component weight sqrt(N)h, source weights r_p,
and the same 1/(m!n!). This dominates WR1 and any ordered tensor pairing
whose coefficient for a word is bounded by the product of these weights.
It is a stated pairing criterion, not an identification of all norms
called a test-function norm.

For d_rate>0 let

    B0(d_rate)=1,
    Bj(d_rate)=max(1,[j/(e d_rate)]^j), j>=1.

The elementary maximum of t^j exp(-d_rate t) gives
|Y|^j exp(-d_rate|Y|)<=Bj(d_rate). Applying WR10 to single basis
directions and summing WR12 proves

    ||F||_(gamma-d_rate;T_abs) <=||F||_gamma C_abs,
    C_abs=sum_(m=0)^6 sum_(n=0)^4 B_(m+n)(d_rate)/(m!n!)
       *[64m D sqrt(N)h/eta]^m
       *[24n L^4 r_*/(u rho)]^n.                              (WR13)

Thus d_rate=beta/8 leaves the honest rate 3beta/8. Every beta-dependent
constant is displayed; the largest polynomial reader loss is order ten.
No source derivative is counted only at a coarse shadow.

For four labelled original source profiles f_i(p) and their weights r_i,
use the actual directions xi_i(p)=r_i f_i(p). For each B subset [4],
n=|B|, the source factor in WR10 becomes

    (4n)^n product_(i in B) [||xi_i||infty/(u rho)].              (WR14)

Sum ALL 16 subsets and the m=0,...,6 field terms, with 1/m! but no 1/n!.
All 15 nonempty source subsets and repeated labels are retained. If an
absolute tensor/test-function bound is used instead, keep the actual
sum_(p read by Y)|xi_i(p)|, bounded if desired by
6L^4|Y| ||xi_i||infty. A normalization of a profile must be specified
before replacing this quantity by one.

## 4. Real all-link pullback and a local moving-center jet supplier

For REAL coarse V now use the real change of variables on every free link

    U_e=Z_e U0_e(V).                                             (WR15)

It preserves the product Haar measure. The pinned tree remains I;
U0=I on within-block links and equals the corresponding V_c on a
crossing link. Exact unitary invariance gives

    Q_X(U;V)=sum_(e owned by X)||Z_e-I||HS^2/N.                   (WR16)

Consequently the q-good cap, q-bad cores, first successful shells and all
absence/failure selectors are independent of V in Z coordinates. The
original cut tests block-INTERIOR plaquettes. None of their links crosses
a block face, so U0=I on each of them and chi_cut(U)=chi_cut(Z).
The product chart is Z_e=exp(a_e), ||a_e||HS<r_a, also fixed. This
argument does not move the original G or white Omega predicate.

Let D_Aj be MK/CG's actual compact-minus-chart difference, divided by its
matched regional chart integral I_R, with R=N_(2j+1)A. At real V it is
ONE positive outside-chart integral divided by ONE positive chart
integral. All touching factors and normalizers remain in both. Under
WR15 and fixed real relative exterior Z_out, both integration domains
are fixed, including their original cuts and local selectors. Each is
a smooth positive integral at real sources. If its numerator domain
has zero Haar measure, it is identically zero, including all these jets.
Otherwise its positive numerator is nonzero.

Here and only here use positivity at REAL |epsilon|<rho/4. A complex
source value is not put into a positive quotient estimate. Complex
fixed-center source jets have the separate WR10 proof.

The local rough-input derivative costs can be kept explicit. Put
ell=5L-4, t=kappa u and d0=(9L^4+5)9^4. At most d0|R| original
plaquette/kernel factors touch R, by the actual radius-four stencils.
MS4's positive Bell polynomials at a constant score B are

    M0=I0=C0=1,
    Mj(B)=sum_(pi partition [j]) B^|pi|,
    Lj(B)=sum_pi (|pi|-1)! product_(Q in pi) M_|Q|(B),
    Ij(B)=sum_pi |pi|! product_(Q in pi) M_|Q|(B),
    Cj(B)=sum_(l=0)^j binom(j,l) Ml(B) I_(j-l)(B).              (WR17)

All have nonnegative coefficients; Mj,Lj,Ij,Cj have degree at most j.
They follow by differentiating exp(H), log Z and Z^-1 with ordered
Leibniz words. The positions assigned to a block keep their original
order, so commutation of invariant derivatives is not assumed.

Each center derivative differentiates an actual fine path of length ell
and, in a kernel numerator, its one coarse output. Unitary factors have
norm one. For b>=1,

    |D^b s(U_p)| <=(4h)^b,
    |D^b log k_t(V_c;M_c(U))|
       <=t[(ell+1)h]^b+(ell h)^b Lb(t).                         (WR18)

The last term is the actual derivative of the compact normalizer, by
MS8--MS9: integrate its exponent against its positive normalized law,
then use WR17. It is generally polynomial in u, not O(1).
Under WR15 the crossing fine direction is conjugated by Z_e, preserving
its norm. A source derivative contributes at most 2r_* if b=0 and
r_*(4h)^b if b>=1. Two source derivatives of the logarithmic density
vanish, since the source dependence is linear and kernels are held fixed.

One convenient uniform score bound through total order ten is

    S=1+2r_*+sum_(b=1)^10 {
        u(1+rho)(4h)^b+t[(ell+1)h]^b
                       +(ell h)^b Lb(t)+r_*(4h)^b},
    B_R=d0 |R| S,
    Q_64(B)=sum_(m=0)^6 sum_(n=0)^4 C_(m+n)(B)/(m!n!).           (WR19)

It bounds every ordered mixed score in the real positive numerator and
denominator, including retained exterior coarse readers. Positivity and
WR17, with differentiation under the fixed compact integrals, prove

    T_(h,r)^(6,4)(D_Aj) <=Q_64(B_R)
          exp{p(u)V_K|A|-c u q |A|/2},
    p(u)=p0+p1 log(1+u).                                        (WR20)

This is MS6 applied to these actual two integrals, not to a signed
connected coefficient. The real value estimate is MK3/CG16 with its
single retained c u q/2 reserve. No variation-one assertion is made
about a complex chart law.

For the actual group insertion

    Theta_g=1_good(H_g) product_(A,j in g) D_Aj,
    n_g=|union_g A|,
    |H_g|<=H_K n_g, |widehat_Gamma_g|<=W_K n_g,
    W_K=(8K+13+32R)^4,

the hard function is fixed in Z and is not differentiated. Ordered
Leibniz gives T(product F_i)<=product T(F_i). Because Q_64 has degree
at most ten with positive coefficients,

    Q_64(B)<=Q_64(1)(1+B)^10,
    product_g Q_64(B_R) <=exp(D_jet n_g),
    D_jet=log Q_64(1)+10 log(1+d0 S V_K).                         (WR21)

Here |R|<=V_K|A|, 1+A n<=(1+A)^n for integers n>=1, and the selected
cores are disjoint. Thus WR20 supplies an ACTUAL local moving-center
jet price. No fine Z-buffer derivative is asserted: that hard cap is
only measurable in Z. If h,r_* are bounded by fixed powers of u, then
D_jet=O(log u+log K); the constants depend on those specified powers.

## 5. A finite Taylor lift, with the actual moving Gaussian core

We now pass WR21 through the exact density-only forest. This step uses
more than the statement that a finite jet norm is an algebra.
Let xi=d_xi sqrt(q)/(4K+1)^2 be an auxiliary coarse radius, fixed as in
section 7, and at a real evaluation point V define

    R_h=min(1,xi/(64 sqrt(N)h)),
    R_J=min(1,u rho/(32r_*)),
    W_c(z)=exp(R_h z_6 B_6c)...exp(R_h z_1 B_1c)V_c,
    epsilon_p(z,s)=epsilon_p+R_J sum_(i=1)^4 s_i xi_ip/u.         (WR22)

Zero directions may fill unused slots. On |z_i|,|s_i|<2, WR9 puts W
in the xi coarse tube and epsilon in the rho/2 source tube. The real
curvature of V is <delta, and the actual transported chart library uses
delta_hat=delta+8xi. In this section W moves the center AND the output.
It is not FT's fixed-center perturbation with b_fr identified with b_tr.

For each real fine buffer Z_Hg, take the Taylor polynomial of the
actual REAL function Theta_g(W(z),epsilon(z,s);Z_Hg), retaining only
monomials square-free in these ten parameters. Call it T_g(z,s;Z_Hg).
Its coefficients are the genuine derivatives at the real point; this
definition needs only those finite real derivatives, not a holomorphic
extension of the rough integral. Terms containing the same parameter
twice are discarded. The selector in WR16 is independent of all ten
parameters. Since R_h,R_J<=1, WR21 implies

    sup_(|z|,|s|<=2)|T_g| <= C_T exp(D_jet n_g) b_g,
    C_T=2^10 6!4!,
    b_g=exp{p(u)V_K n_g-c u q n_g/2}.                          (WR23)

Indeed the sum over subsets of m of six and n of four positions is
bounded by 6!4! times the factorial-normalized WR1 sum, then by 2^10
on the radius-two polydisc. T_g retains its full original Gamma_g and
is a bounded measurable function of the same real buffer. Put it equal
to zero off the actual fixed joint cap before using a chart vertex.

First identify these jets at finite volume, before any infinite atom sum.
In fixed real a coordinates write w_a(a;W,epsilon) for the actual
transported chart density, including j_N(a) and its constant Haar factor.
Define the auxiliary finite-volume model

    N_T(z,s)=int_(product ||a_e||HS<r_a) da w_a(a;W,epsilon)
                       sum_(Gamma-compatible F) product_(g in F) T_g,
    R_T(z,s)=N_T(z,s)/Z_a^tr(W,epsilon).                         (WR23a)

The finite torus has finitely many cores, shells and compatible families.
At real center/source data the actual identity with Theta in place of
T follows from the real Haar pullback WR15 and MK's exact selected-
difference resummation. The regional numerator and denominator integrals
have fixed domains. Their derivatives through order ten are dominated
on compact real parameter neighborhoods: all underlying fine groups
are compact, their smooth densities are bounded, and their positive
normalizers and regional chart integrals have positive minima there.
This finite-volume observation is only a differentiability argument;
none of its possibly extensive constants is called a local estimate.

Thus differentiation of the finite real identity under its integrals
is valid. Square-free Taylor classes of Theta and T coincide, so WR23a
and the actual real Z_cut/Z_a^tr have the same ten-parameter square-free
jets at zero. RC proves that the common chart denominator in WR23a is
holomorphic and nonzero. At zero the ratio is strictly positive; a local
log branch therefore exists, and the two normalized log jets agree by
the finite reciprocal/log Taylor formulas. This only proves their local
jet identification. The uniform nonvanishing, reader bounds and
termwise derivative convergence on the large auxiliary polydisc are
proved by the forest below, not assumed in this argument.

The small-chart part has an ACTUAL holomorphic continuation here:

    F(a;W,epsilon)=-sigma^2 log w_epsilon(exp(a)U0(W),W)
                                      -sigma^2 sum_e log j_N(a_e),
    F'(b)=0, K_*=F''(b), C=K_*^-1,
    K(W)=F_0''(0;W),
    P(W)=sum_A chi_A [K(W)|A]^-1 chi_A,
    C(W,epsilon)=P(W)+E_lift(W)+T_crit(W,epsilon).                (WR24)

These are RF9--RF20/NR2--NR8 on their transported chart domain, not an
assumed covariance for a rough numerator. The actual normalized kernels
and Haar logarithms are included. Their local analytic normalizer domain
contains every small-chart fine input on the stated tube. All fine
arguments hidden in T_g remain real or occur only in its real derivatives.

This chart library is canonical in the ACTUAL W. The phase is defined
by U=exp(a)U0(W) and the same actual density; a real center is only a
coordinate chart for its analytic domain. K(W) is its actual zero-field
Hessian, P(W) uses that K and the fixed geometry-only patches, and every
patch inverse is unique. RF's substitution fixed point is unique in the
common tau ball, so its b(W,epsilon) agrees on overlapping parameter
charts. The normalizer logarithms use the same branch from their real
positive values; the small-chart paired-word expansion fixes that branch.
The atom formulas use these local vertices and the one fixed ordering,
not a choice of a new real center or new patches at each evaluation.
Consequently every finite decorated coefficient reads only its original
W/source data on its complete Y. Equal data there give equal coefficient
functions and equal restricted-direction jets. This verifies the needed
coherence, rather than inferring it from a uniform family of value bounds.

For clarity the needed moving-core estimates are already proved in NR,
including complex W. The geometry-only cutoffs do not move. Principal
patch inverse resolvent bounds and weighted conjugation give

    Re P>=c0 I, ||P||op<=g_cov,
    max(row,col)sum sup|P[I]^-1(i,j)|<=v_I,
    ||P[I]^-1||op<=b_P=1/c0,
    Re P[I]^-1>=a I, a=c0/g_cov^2,
    M_beta(E)<=e<=min(c0/8,1/(4v_I),a/(64v_I^2)),
    B_beta(E)<=B_E.                                            (WR25)

The precision bound follows from
Re(P^-1)=P^{-*}(Re P)P^-1 and ||P||<=g_cov. It does not require P to
be real at the complex parameter. Every P[I] inverse and determinant
reads its full patch-component reader, including all W arguments there.
The coefficient suprema in WR25 are inside the original marked sums.
For principal P[I], the exponential-conjugation argument is uniform in
I and in the torus, including the whole-torus small-volume patch.
No mode is removed. Both E tails and their full readers remain.

The global critical branch obeys, by RF14's actual force and contraction,

    V_beta(b)<=t_d=2 A_G g_*(1+rho)(delta+8xi).                  (WR26)

Its substitutions have the RF complete-reader coefficients. Thus
moving b, moving P and moving C all have their ACTUAL analytic dependence
on the auxiliary parameters. They are not held constant during jet
extraction. The extensive prefactor is the full transported-coordinate
P_*=h_N^n(2pi sigma^2)^(d/2)exp[-LogDet K_*/2-F(b)/sigma^2].
It cancels in the compact/chart ratio before this finite-jet estimate.

## 6. Normalized density factorials, pins and exact jet extraction

Use MK11--MK13's finite-domain expansion in the Z coordinates: marked
blocks stay real; translate the other original chart blocks by b; keep
every whole-block side/corner, normal, presence/absence flag, original
Gamma incompatibility, and original nonlinear vertex. Replace only
Theta_g by T_g. Unused modes integrate to one. For each activated I,
the covariance is the principal C[I], never an inverse principal precision.
At disconnected component masks P[I] is block diagonal because each
component includes every patch touching its fields. The determinant
therefore factors on those exact components even when W is complex.

Retain the normalized determinant and inverse lists

    g_(P+E)(x)=g_P(x) exp{
       sum_(j>=1)(-1)^j Tr[(G E)^j]/(2j)
       +(1/2)sum_(j>=1)(-1)^(j-1) x^T(G E)^j G x}, G=P[I]^-1.   (WR27)

Independent component-pair masks of radius two preserve accretivity;
real forest masks preserve the e row bound. Expand every E atom and
every matrix index. With

    ell_E=-log(1-v_I e)/2, t_E=v_I^2 e/(1-v_I e),
    c_*=2b_P^2/a+b_P+t_E+1,
    L_hat=sqrt(2)max(1,sqrt(2 exp(1)c_*)),
    s_d=k t_d/sigma,

the optimized scalar Gaussian Cauchy proof of MK15 gives, for every
scalar multiindex nu and every auxiliary parameter in WR22,

    A_I exp[-a||x||^2/8] L_hat^|nu| product_i sqrt(nu_i!)
       *2^(k(|M|+|H|)/2) exp[L_hat^2 s_d^2(|M|+|H|)],
    A_I=(b_P/(2pi))^(|I|/2)exp(|I| ell_E).                     (WR28)

To check the uniform extension: the determinant modulus is bounded using
the singular-value lower bound c0; the quadratic lower bound is WR25;
the absolutely convergent loop/chain majorant uses v_I e<1; translation
uses sqrt((nu_i+j)!)<=2^((nu_i+j)/2)sqrt(nu_i!)sqrt(j!) and
sum_j z^j/sqrt(j!)<=sqrt(2)exp(z^2). These inequalities do not use
realness of W. They include the entire normalization of g_P.

The forest differentiates only this normalized Gaussian density in
scalar fine arguments. It does not differentiate T_g, a hard cap, a
normal, a boundary or a path-minimum clock. Moving-center derivatives
are recovered later as auxiliary coefficients. Thus no new scalar
Gaussian derivative factorial is introduced. The original incidence
15 bounds polynomial degree by 90. With the same fixed majorants as MK,

    L_M=K_g^k 2^(k/2)(1+s_d)^(90k)exp(C_bar s_d^2),
    a_g^J=C_T exp(D_jet n_g)b_g L_M^|H_g|,                     (WR29)

where K_g=max(1,exp(ell_E)sqrt(8b_P/a)) and
C_bar>=L_hat^2+2 eta_bar, the mixed integrals have the same
L_hat^|nu| product sqrt(nu_i!) bound times primitive weights.
The ordinary/side/bad weights are exactly MK's weights recomputed at
t_b=t_d. Their no-mark/no-side singleton is still O(sigma^2) by the
same centered parity. Every other small-chart argument is analytic on
WR22, so this parity is an identity there.

In particular keep their actual k-dimensional surface and Gaussian costs:

    A_k=(b_P/(2pi))^(k/2)exp(k ell_E),
    C_area=m0 omega_D v_D^(m0-1),
    q_h=K_g^k 2^(k/2)exp(-a p_cut^2/32),
    Q_s=A_k 2^(k/2) C_area p_cut^(k-1) sigma^-1
                              (1+s_d)^(90k)exp(-a p_cut^2/64).

Here v_D and omega_D are the unit D-ball volume and unit sphere area;
the block body is the product of m0 whole-link balls. The body contains
the k-ball of radius p_cut and every boundary point has norm at least
p_cut. Each product face and every side selection remains in the exact
integral. These are upper bounds on their total contribution, not a
replacement of the body by the contained ball.

A complete-reader pin through P or its determinant lies in the whole
base component and is paid by its collar cardinality. An E-reader pin
uses the original B_E and the explicit normalized list constant

    K_m=v_I/[2(1-v_I e)]
                     +v_I^2(16/a+1)/(1-v_I e)^2.

Differentiating the trace and inverse geometric majorants in WR27 gives
K_m D_x(I), where D_x(I) sums all weighted |E_S(i,j)| with i in I
and x in S. Its unrestricted pin sum is exactly bounded by B_E.
A b-reader pin uses

    K_tr=(L_hat/sigma)(1+sqrt(2)L_hat s_d),
    sum_X d_x^b(X)<=t_d.

In particular the marked-buffer pin retains its charged root:

    sum_g exp(beta|widehat_Gamma_g|) a_g^J K_tr
                         sum_(X in H_g)d_x^b(X)
       <=K_tr h_g^J t_d=:j_g^J,
    h_g^J=sup_x sum_(g:x in widehat_Gamma_g)
                           exp(beta|widehat_Gamma_g|)a_g^J.      (WR30)

Every derivative parameter has only the original local link/source data
in its coefficient. The auxiliary variables themselves create no new
physical readers. There is no ambient-volume derivative charge.

The actual normalized heat identity for two distinct components is

    partial_(s_BB') int Phi g_(C_I(s))(x-shift)
       =sum_(i in I_B,j in I_B') E(i,j)
                     int Phi partial_i partial_j g_(C_I(s))(x-shift).

The two symmetric off-block entries cancel its usual factor 1/2.
Phi includes T_g, every flag, boundary and flux and is fixed under this
artificial covariance derivative. The finite forest formula follows on
pair monomials by partitioning independent edge clocks into their unique
maximum spanning forest; a non-tree clock lies below the path minimum.
Analyticity on the radius-two pair polydisc extends that polynomial
identity. The derivative is taken before evaluating its path-minimum
mask. These arguments are uniform in the auxiliary physical parameters.

For completeness the all-order sums used after WR28 are unchanged:
allocate child legs by scalar index, using
sum y^j/sqrt(j!)<=exp(2y) and
sum sqrt((j+1)!)y^j/j!<=exp(4y) for y<=1/2. The first two rooted
recursions spend xi_b=beta/8 each, for primitive components and Gaussian
attachments. With the actual MK h_0,h_s and h=h_0+h_s+h_g^J, require

    h<=h_c=min(xi_b/2,1/[4(1+L_hat^2 e)],
                            xi_b/[8k(1+L_hat^2 e)]),
    h_0,h_s<=h_c/4, h_g^J<=h_c/2.

Explicitly s_c=(32R+1)^4, d_c=(9L^4+5)s_c, d_h=s_c, and
h_0=h_v+h_h, where

    h_v=C_V sigma exp(beta s_c)(W1+d_c W0),
    h_2=C_V sigma^2 exp(beta s_c)(E1+d_c E0),
    h_h=d_h exp(beta s_c)q_h,
    h_s=Q_s exp(beta s_c)t_d(1+d_h k).

W0,W1,E0,E1,C_V are MK's fixed Taylor/ternary-flag and signed singleton
majorants on the same NR complex small-chart library. Their field/source
and complete-reader suprema are taken before the sums. WR24--WR26 put
this transported phase inside exactly that library; no compact derivative
is charged to these ordinary constants.

Put C0=1+K_m B_E and keep the actual side pin
j_s=K_tr Q_s exp(beta s_c)k t_d^2. The raw norm is bounded by

    C0 h+L_hat^2 B_E h^2+j_s+j_g^J.

Multiply compact primitive AMPLITUDES alone by h_c/(2h_g^J), keeping
all auxiliary parameters, densities, phases, contours and T_g fixed.
The ordinary child supersolutions are unchanged and WR30 scales once.
Undoing one factor on each compact-bearing species gives

    epsilon_g^J=2(C0+L_hat^2 B_E h_c+j_s/h_c)h_g^J+j_g^J.        (WR31)

The ordinary bound is explicitly

    epsilon_a=C0(h_2+h_h)+(C0/h_c+L_hat^2 B_E)h_0^2
                           +2(C0+L_hat^2 B_E h_c)h_s+j_s.

Require epsilon_a and epsilon_g^J to be <=xi_b/4. The two
remaining reader-overlap and Kruskal logarithm trees each spend xi_b.
Rescale compact RAW weights by xi_b/(4epsilon_g^J), then undo their
surviving mark. Exactly as the displayed recursions show, the entire
absolute compact-bearing logarithm on the auxiliary polydisc satisfies

    ||Psi^lift||_gamma <=2 epsilon_g^J.                         (WR32)

This argument proves a convergent decorated library, not just moments.
Both sides/corners, all flags, every density/translation reader and the
field-free groups are included. It retains at least one compact root.

Finally, work modulo the ideal generated by z_i^2 and s_i^2. T_g is
the exact Taylor class of the real Theta_g in that finite quotient.
The actual chart libraries are analytic and hence have their genuine
Taylor classes. Multiplication, integration on these fixed domains,
the absolutely convergent density/forest sums and the connected log
preserve this class. Equivalently, distribute each of the ten derivative
positions among factors; every resulting term is exactly the coefficient
retained in the square-free product. The normalization and logarithm
derivatives are included because WR27 and the connected log are taken
before coefficient extraction.

Cauchy on the unit auxiliary circles bounds each such coefficient by
the same absolute decorated majorant in WR32. Dividing by R_h^m R_J^n
recovers the actual ordered real derivatives. Summing the WR1 factorials
uses sum_(m<=6)1/m! sum_(n<=4)1/n!<exp(2). We obtain

    ||Psi^diag||_(gamma;6,4;h,r)
          <=2 exp(2) R_h^-6 R_J^-4 epsilon_g^J.                (WR33)

Here Psi^diag is the actual canonical MK compact/chart log at real V,
with selectors and physical reference centered at V. Its coefficient
formula is the fixed MK decorated library, evaluated at that real data.
For every point of the open real curvature/source domain the same
majorants control all derivatives on a real neighborhood. Uniform
absolute convergence of every included derivative therefore justifies
termwise differentiation and proves C^(6,4), not merely pointwise formal
jets. Local agreement persists on complete readers. This supplies the
moving-center derivative seam for THIS bare ratio only.

## 7. Parameter order, the surviving rare price and chart remainders

Fix the RF/NR/MK common cover, its analytic ceilings and strict tail/source
margins first. Choose c_tau,c_z,c_q with the actual SC/RC cap, boundary
and chart conditions. Keep the original fixed rho. Let

    B_d=2 A_G g_*(1+rho),
    B_d^2(d_delta+8d_xi)^2<=c N/(4096 C_bar k^2),
    d_delta^2<=c/(8 a_bulk), d_delta>0, d_xi>0.                 (WR34)

These are fixed positive choices, followed by WR4 and
xi=d_xi sqrt(q)/(4K+1)^2. Since H_K/V_K<=256, they imply

    (C_bar k^2/N)t_d^2 H_K<=c q/16.                            (WR35)

This pays the marked-buffer translation from the actual c u q/2 local
reserve. There is no fr/tr correction in this diagonal construction:
its regional denominator is already the same real product chart at V.
For all sufficiently large u, delta_hat/tau and t_d/r_a are O(K^-2),
where tau=c_tau sigma p_cut. RF's contraction, all small-field analytic
normalizer domains, the RC chart margins and MK's full-block shift
conditions hold with slack. In particular t_d<=r_a/(16k) and
C_bar(k t_d)^2<=a r_a^2/64. All thresholds are independent of T.

Define

    D_bulk=k log K_g+(k/2)log2+90k log(1+p_cut),
    D_J=log C_T+D_jet,
    Delta_K=max(1,(16K+25)^4-1),
    t_g^J=K exp[beta W_K+p(u)V_K+D_bulk H_K+D_J-7c u q/16].     (WR36)

The group core is connected at range 8K+12, shell choices cost at most
K^n, a depth-first traversal costs Delta_K^(2(n-1)), and a pinned reader
has at most W_K possible core anchors. WR29 and WR35 therefore give

    h_g^J<=W_K t_g^J/(1-Delta_K^2 t_g^J),
    Delta_K^2 t_g^J<1.                                         (WR37)

This counts actual microscopic readers, including their growing collars.
For any specified polynomial bounds on h and r_* with constants
independent of volume, the positive terms
in WR36 are O((log u)^5), whereas u q=N c_q p_cut^2 and 2alpha>5.
Thus a finite volume-independent threshold makes h_g^J<=exp(-c u q/8),
all WR31 smallness conditions valid and the finite powers in WR33
harmless. In particular, after increasing that threshold,

    ||Psi^diag||_(gamma;6,4;h,r)
                <=exp[-kappa_d p_cut^2], kappa_d=c N c_q/64.     (WR38)

This includes unscaled h=1,r_*=1 as well as h comparable to sigma. It is
a fixed finite-order real result, not analyticity of a rough moved mean.

The transported chart-only remainder is already supplied by RC14/RC18
at Lambda=E on the same transported coarse tube:

    Z_a^tr(V)=P_*(V) exp(sum_Y H_Y^tr(V)),
    ||H^tr||_gamma<=C1 sigma^2
                     +C2(1+p_cut^(91D+2))exp(-a p_cut^2/64).     (WR39)

Apply WR8--WR11 with eta replaced by xi to this genuine chart family.
Consequently the actual REAL bare original-cut logarithm has

    Z_cut(V,J)=P_*(V,J)exp(sum_Y[H_Y^tr+Psi_Y^diag]),             (WR40)

with finite mixed jets of its small remainder bounded by the sum of
WR11/WR39 and WR38. This is a real open-domain family using the fixed
ambient library, not a pointwise choice of unrelated physical centers.
P_* is its actual transported-coordinate critical prefactor and remains
outside the small norm. It need not equal FT's off-diagonal P_fr.

For the consumer's next-scale field weight, exactly

    h_out=sqrt(N/u'),
    h_out/xi=sqrt(u/u') (4K+1)^2/(d_xi sqrt(c_q)p_cut).           (WR41)

Thus h_out/xi=O(K^2/p_cut) only IF u'/u has a fixed positive lower
bound. That flow estimate is not proved here. In the concrete supplied
weight h=sigma this ratio tends to zero since alpha>5/2. With r_*=1,
or more generally bounded r_*/u, the WR11 polynomial stays bounded
when h/xi does. The nonlinear chart remainder then remains O(sigma^2)
plus its explicit Gaussian rare term. With h=1 the crude sixth-order
chart bound includes sigma^2 xi^-6, which can grow like
u^2 K^12/p_cut^6. Its smallness is NOT asserted. By contrast the rare
return in WR38 pays any fixed inverse-radius or polynomial-in-u cost.

An absolute ordered tensor norm for the diagonal family follows directly
from WR33's common derivative envelopes and WR12. After a loss d_rate,
one may multiply its right-hand side by

    C_diag_abs=sum_(m=0)^6 sum_(n=0)^4
          B_(m+n)(d_rate) (4D sqrt(N))^m (6L^4)^n.              (WR42)

Indeed each basis direction with size h and each source singleton with
its actual weight is among WR1's allowed directions. The missing
1/(m!n!) only enlarges the bound in WR42. Taking d_rate=beta/8 leaves
3beta/8 and explicitly pays all finite reader multiplicities. Labelled
four-source jets follow by the same position-subset construction, without
source factorials; one can multiply WR33 by 6!4! if a coarse common
bound is preferred. All original labels remain visible.

In particular, for fixed volume-independent constants C_h,C_J and
h<=C_h sigma, r_*<=C_J u, the actual combined remainder in WR40 obeys

    ||H^tr+Psi^diag||_(3beta/8;T_abs)
        <=C_beta sigma^2+exp[-kappa_* p_cut^2],
    kappa_*=min(a/128,kappa_d/2)>0,                            (WR42a)

for all sufficiently large u. Once h/xi<=1, one explicit choice is

    C_beta=C1 sum_(m=0)^6 sum_(n=0)^4 B_(m+n)(beta/8)/(m!n!)
                   *(64m D sqrt(N))^m*(24n L^4 C_J/rho)^n.

Its constants and the threshold depend on N,L,R,rho,C_h,C_J, not T.
To verify this directly,
h/xi tends to zero, r_*/(u rho) stays bounded, R_h is eventually one,
R_J^-1<=max(1,32C_J/rho), and the finite powers of p_cut in WR39 are
absorbed by half its Gaussian exponent. The reader-factor constants
in WR42 are fixed and can be absorbed by half the compact exponent.
This is the explicit weighted small-remainder conclusion, excluding P_*.

## 8. The honest rate interface and its two tree sums

No previous estimate implies the native exp[(mu+2)|H|] input at mu>0:
gamma=beta/2 is smaller than two. For a purely logical counterexample,
put constant analytic coefficients exp[-(gamma+e0)n]/n^2 on a nested
connected reader path of length n through a fixed cell. The gamma norm
is uniformly finite, whereas every rate greater than gamma+e0 has
unbounded norm as the volume grows. Analyticity or finite derivatives
do not repair this rate implication. This is not a Yang--Mills no-go.

Here is the exact smaller-rate version of RGA-C. Let T be WR1 or its
labelled finite-jet version. Assume an actual finite representation

    Z_red=sum_(I subset labels) A_I, A_empty=1,
    T(A_I)<=product_(i in I) alpha_i,                            (WR43)

with nonempty complete readers H_i, exact factorization over their
overlap components, and real C^(6,4) functions on one open domain.
For arbitrary mu,d1,d2>0 set lambda=mu+d1+d2 and suppose

    Q_lambda=sup_x sum_(i:x in H_i)exp(lambda|H_i|)alpha_i
                          <=(1/4)min(1,d1,d2).                  (WR44)

Then the actual connected log is C^(6,4), nonzero before taking its
log, and has the unregulated complete-reader norm at mu at most Q_lambda.
The proof keeps every beta-dependent threshold:

Ordered Leibniz distributes word positions, preserving their order.
Division by m!n! and summation on the downward-closed rectangle proves
T(FG)<=T(F)T(G). Labelled sources are distributed by subsets, with no
extra label factorial. This is RGA8's finite calculus, rebuilt here.

Group each selected set into its unique overlap components. For the
first positive rooted-tree sum use v_i=exp((mu+d2)|H_i|)alpha_i and
b_i=exp(lambda|H_i|)alpha_i. Its recursion
T_i=v_i exp(sum_(j:H_j meets H_i)T_j) has supersolution b_i because
the child sum is <=Q_lambda|H_i|<=d1|H_i|. Repeated labels only
enlarge this positive bound. The integrated overlap gas thus has norm
at mu+d2 at most Q_lambda. The second tree sum for its log has the
same supersolution because Q_lambda<=d2. The alternating connected
graph sum is bounded by a tree: graphs with the same fixed-order
Kruskal tree form the interval between that tree and its allowable
extra edges, whose signed sum has modulus at most one. Rooting at a
cell changes the usual 1/m! to 1/(m-1)! and yields the supported norm.

To establish the logarithm identity, multiply A_I by z^|I|. At |z|<2
both child sums are still bounded by 2Q_lambda, below each available
margin. The formal graph/component identity is absolutely convergent
there and equals the finite sum. At z=1 it is the exponential of the
real connected series, hence positive. Uniform convergence of every
included derivative gives C^(6,4) on compact subsets of the open domain.
No complex physical input or rough analytic continuation is needed.

Choose, explicitly,

    lambda=3beta/8, d1=d2=beta/16, mu=beta/4,
    Q_lambda<=beta/64.                                         (WR45)

These numbers retain the microscopic graph and spend precisely the two
available small margins. They do NOT verify the old RGA16 as written.
Nor may this loss be repeated indefinitely without regenerating a common
rate and its input budget at the next step.

There is one useful actual application requiring no new expectation
estimate. For the already integrated small remainder F_Y in WR40, or
one of its separately stated return families, define k_Y=exp(F_Y)-1.
Then exp(sum F_Y)=product_Y(1+k_Y) exactly, its selected coefficients
are products of the k_Y, and T(k_Y)<=exp(T(F_Y))-1. If its lambda norm
is B, their Q_lambda is at most exp(B)B. For B<=beta/128 it is
<=beta/64. WR45 applies to THIS integrated representation. This does
not prove RGA14's joint estimates before integration, an interacting
reference-law bound, or a bound on the omitted P_*.

## 9. Precise delivered interface and remaining tasks

WR11--WR14 supply fixed-physical-center ordered output/source jets for
FT's families and HC's compact family. WR20--WR21 supply local
moving-center jets directly from the real positive actual regional
integrals. WR22--WR38 propagate them
through the actual normalized density library and supply real diagonal
bare compact/chart connected jets, with an honest microscopic reader
rate. WR39--WR42 combine those with the already available chart remainder.
WR45 is a rate-parameterized finite-jet consumer for those integrated
families. The latter two results do not require HC's separate
complex-compact theorem. All new statements await this source's review.

The following are still separate actual-class obligations:

* Derivatives of retained fine fields, arbitrary regional exterior fields
  or hard buffer variables. Fully integrated output bounds do not provide
  them. The real pullback used here fixes relative exterior Z for its
  local supplier, not arbitrary physical-boundary derivatives.
* The full P_* action, determinant, Haar/reference and normalized-kernel
  vacuum budgets, main Wilson matching, real extraction and the actual
  u' flow needed for WR41. EXTCONT's extraction is not an automatic
  consequence of a small nonlinear/return remainder.
* Original G/Omega matching, inherited effective histories, all original
  source orders/locations through depth, matched conditional reference
  laws, and regeneration of the same full derivative/support norm.
  EXTCONT's hole completion requires its actual jet price before using
  a hole-counting bound; no arbitrary-hole theorem is added here.
* Positivity properties needed for the continuum construction beyond the
  finite real integrals, non-freeness, continuum existence and a positive
  physical continuum gap. None follows from this one bare step.

## 10. Primary comparisons and source-freeze discipline

[Brydges--Slade, arXiv:1403.7244v2](https://arxiv.org/pdf/1403.7244v2),
Definition 3.1, Example 3.2, Definition 3.3, Proposition 3.7 and section
5.1, define a weighted finite-difference test-function dual seminorm and
prove its product property. Their fields and test functions are specified
bosonic/fermionic lattice objects; the abstract product property is not
a 4D SU(N) localization theorem. The zero-difference test-function bound
does justify an absolute coefficient pairing AFTER its weights and labels
are mapped. WR12--WR14 state that map explicitly for ordered group jets;
WR1/WR44 use their own ordered Leibniz proof rather than importing a norm
inclusion. The primary PDF passages were read; the HTML retry failed.

[Dimock, arXiv:1212.5562v2](https://arxiv.org/abs/1212.5562v2),
sections 3.13--3.14 as read in this author's preceding unit, explains
localization and analyticity in a scalar setting. [Lohmann,
arXiv:1411.1107v1](https://arxiv.org/html/1411.1107v1), section 2.1.4
and Remark 2, treats a site-product cutoff and its covariance hypotheses.
Neither supplies moving hard-selector jets of this gauge model. Here
WR15--WR16 prove that the relevant selectors actually become fixed, and
WR23--WR32 keep the rough factors measurable while the forest acts on
the normalized small-chart density. These are bounded primary comparisons,
not assertions that the cited scalar theories imply gauge closure.

This mathematical source is frozen before its compact manifest and
mechanical receipt. The author requests a DIFFERENT fresh source-first
hostile reviewer. No numerical physics runs, additional workers, changes
to predecessors, shared fronts, Git, PRs or audit files are made here.
The parent owns integration and publication. Author checks are not review.
