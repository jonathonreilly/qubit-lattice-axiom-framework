# A shrinking original-coordinate chart corollary

This is a short consequence of the explicit estimates in
[SN](SHIFTED_NONLINEAR_READER_RETURN_ASTRA.md), not a second connected-expansion
construction. SN is frozen at SHA256
`47423d924c938f627550ae592d4ef2d5ef3255d6f2e60b2ab0887b9a46425d1b`
and is still under independent review at this unit's preparation. The
corollary depends on its mathematical estimates and inherits any required
correction. Neither that review nor this author's calculations replace an
independent review of the present statement.

The new point is uniformity when the ORIGINAL-a ball and coarse-data tube
shrink with the coupling. The side costs have no remaining inverse-sigma
loss after their actual flux and shift budgets are inserted. The source
radius and original-block support rate stay fixed. The result is not the
literal white-noise cut of STEP55 or the selected cube of GC/OC.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. One uniform construction and the moving scalar parameters

Use exactly SN1's actual finite-u model and full prefactor, with
sigma=sqrt(N/u), D=N^2-1. Choose ONE R, patch rule and complete-reader FU
construction as in SN2--SN6. Keep beta=(16R)^(-4), both covariance tails,
eps, B_E, a, L_hat, h_c, A, W0,W1,E0,E1 and every core/marked constant
at their uniform upper bounds. In particular these constants do not vary
with the chart radius, u or T. The physical covariance itself still has its
actual u and original-data dependence.

Fix preliminary bar_tau,bar_rho,r0 as in SN. Choose r_max>0 below r0/8 and
all fine-chart margins, with r_max<1 and

    eta_max=4A I0 r_max(1+r_max)<=a/128,
    C_max=L_hat^2+2eta_max.

Choose a FIXED positive source radius rho<=bar_rho satisfying FU18 and
SN3's critical-Hessian cap at bar_tau. Shrinking tau later does not require
shrinking rho: all positive majorants N',D_H are monotone in tau. Fix c>0
and kappa_c>0 so that

    c<=min(1/(16D),bar_tau/r_max,sqrt(a/(64D^2 C_max))),
    9 A_G g_*(1+rho) kappa_c<=1/4.                       (SH1)

Here kappa_c is only a coarse-domain constant, not the model coupling kappa.
For any real function p(u) with

    p(u)>=1, p(u)->infinity, sigma p(u)->0,
    r_a(u)=sigma p(u), tau(u)=c sigma p(u),
    delta_*(u)=kappa_c tau(u), eta(u)=kappa_c tau(u),       (SH2)

take the original joint domains
`V_c=exp(v_c)Vbar_c`, max ||v_c||HS<eta(u), with center curvature
<=delta_*(u), and |epsilon_p|<rho. Decreasing either coarse radius is allowed.
For sufficiently large u these radii meet every fixed FU19/SA/CB ceiling.
The tube curvature bound is delta_hat=delta_*+8eta=9kappa_c tau, so SH1
pays the actual force. Real delta_V is not used for this complex supremum.

There is no new critical point. The canonical FU iteration from zero, with
one fixed patch/atom rule, is evaluated on the smaller domain. Its contraction
constant remains <=1/4 and its atom norm remains <=tau(u), by the same
force estimate. Restriction commutes with its absolutely convergent products
and limit. Uniqueness identifies this solution with the actual admitted
critical field b_*(V,epsilon). Atom formulas and readers are not changed by
re-estimating their norms. Normalizing b-atoms by tau(u) in SN7--SN9 is
permitted at each u>0 and keeps their root and marked norms <=1; tau(u)
is a scalar parameter independent of V and epsilon.

For r_a<=r_max, SN10 holds with eta_bar(u)<=eta_max. Moreover
`(L_hat^2+2eta_bar(u))(D tau(u))^2<=a r_a(u)^2/64` by SH1.
The entire side/corner homotopy stays in the same analytic fine chart,
since r_a+2D tau< a_f. All SN domains, pair-derivative orders and factorial
bounds therefore hold uniformly. No numerical experiment or new external
analytic theorem is needed for this substitution.

## 2. Exact cancellation of the side powers of sigma

Put E_c=exp(beta s_c), Q0=A_D 2^(D/2)omega_D and

    V1=C_V E_c(W1+d_c W0), V2=C_V E_c(E1+d_c E0),
    H0=d_h E_c K_g^D 2^(D/2).

These are fixed constants. SN18, SN22 and SN24 become EXACTLY the following
positive majorants, with p=p(u):

    h_v=V1 sigma, h_2=V2 sigma^2,
    h_h=H0 exp(-a p^2/32),
    h_s=Q0 E_c c(1+d_h D) p^D(1+Dcp)^(90D)exp(-a p^2/64),
    h_tr=Q0 E_c L_hat D c^2 p^(D+1)
          *(1+sqrt(2)L_hat Dcp)(1+Dcp)^(90D)exp(-a p^2/64). (SH3)

Indeed `Q_s=Q0 sigma^-1 p^(D-1)(1+Dcp)^(90D)exp(-a p^2/64)`.
Its flux budget is tau=c sigma p. The additional marked translation costs
`K_tr=(L_hat/sigma)(1+sqrt(2)L_hat Dcp)`, but its distinguished side root
has TWO field budgets, D tau^2. Thus both inverse-sigma factors cancel.
This cancellation uses SN24's actual side root; replacing it by a generic
weak-vertex mark would not prove SH3. All colours and complete readers stay.

With h_0=h_v+h_h and C0=1+K_m B_E, define the positive quantity below.
It is SN26--SN27's bound once the smallness conditions are checked:

    epsilon=C0(h_2+h_h)+(C0/h_c+L_hat^2 B_E)h_0^2
                  +2(C0+L_hat^2 B_E h_c)h_s+h_tr.         (SH4)

For fixed positive constants C1,C2 and M=91D+2 it follows that

    epsilon<=C1 sigma^2+C2(1+p^M)exp(-a p^2/64)
            <=C1 sigma^2+C3 exp(-a p^2/128).              (SH5)

The last inequality follows by maximizing p^M exp(-a p^2/128); it requires
no relation between p and sigma. For example one may multiply C2 by
`1+(64M/(a exp(1)))^(M/2)`. All constants are fixed before u,T.
Since p->infinity and sigma->0, SN28's q_h<=1, h_0<=h_c/2, h_s<=h_c/2
and epsilon<=beta/16 hold eventually. The chart conditions hold eventually
because sigma p->0. No sigma p^3 condition is required by these integrated
bounds. Side-dependent vertices still receive their true rare side price;
only no-side singletons use centered parity.

This uses SN's displayed finite-parameter estimates, not an unspecified
threshold u0(r_a,tau) from its fixed-radius existence statement. SH1--SH5
verify every variable inequality uniformly with the constants fixed above.

Consequently, CONDITIONAL ON SN's frozen theorem, the exact original-a
chart integral has the representation

    Z_a(u)=h_N^n(2pi sigma^2)^(d/2)det(K_*)^-1/2
              *exp[-F(b_*)/sigma^2] exp[sum_Y H_(Y,u)],
    sup_x sum_(Y contains x)exp(mu|Y|)sup|H_(Y,u)|<=epsilon,
    mu=beta/2=1/[2(16R)^4]>0,                  Z_a(u)!=0. (SH6)

The integration domain is exactly product_e B_(sigma p(u)) in the original
a coordinates. The critical action, normalized finite-u kernel, h_N,
Haar density and full-colour determinant are unchanged. They are not bounded
by SH5; in particular no extensive critical-action cost is erased. Four
beta/8 support margins are spent exactly as in SN, with the same R and
complete original readers. Their rate does not deteriorate with u.

## 3. What analyticity and derivatives mean on this domain

The source disc rho stays fixed, but the unscaled coarse radius eta(u)
vanishes. On its half-size domain, for scalar-coordinate multiindices
alpha in the coarse v variables and zeta in original epsilon, Cauchy gives

    ||partial_v^alpha partial_epsilon^zeta H||_(mu,mark)
      <=alpha! zeta! [2D/eta(u)]^|alpha|[2/rho]^|zeta|epsilon. (SH7)

Choose scalar polydisc radius eta/(2D) inside each link's HS ball; this
explains the colour factor. Coefficients not reading a differentiated datum
have zero derivative. Positive summability permits the same marked norm.
Thus source derivatives keep a fixed analytic radius, whereas ordinary
coarse derivatives can cost powers of (sigma p)^-1. After rescaling
v=(sigma p) v_hat, the coarse domain radius is the fixed kappa_c c and
these powers cancel in derivatives with respect to v_hat. This is not a
fixed unscaled coarse tube, an all-orders uniform bound on its unscaled
jets, or a statement about u derivatives of an arbitrary function p(u).

## 4. Literal consumer comparison

Only the following bounded portions were read: STEP55 lines469--543;
GC lines1--195 and390--430; OC lines1--65,72--95,190--210,280--310 and
439--540. These compare cuts and domains; their conditional probability
or effective-level theorems are not used to prove SH6.

**STEP55 section5.** Its white noise W has the product HS-ball cutoff
`product_b 1_(|W_b|<=p_W)` and a PRODUCT truncated Gaussian probability
reference. Its field is `A=sigma mathcalC W` about its background, with
square-root decoupling and hypotheses H1--H4, including inherited
interactions and regions with holes. SH6 integrates original-coordinate
balls and uses the exact full critical covariance density. These are not
the same cut or reference. In particular sigma p->0 does not imply its
pointwise interaction condition sigma p^3 small: p=u^(1/4) separates them.
Nor does the small original-block rate mu verify STEP55's H4.

**GC6--GC11.** Its fixed full chart is C_ch=product B_(r/2), and its actual
selected cube uses the SOURCE-FREE finite-u b_0 and
`y=sigma^-1 T_*(a-b_0)`, `T_*=K_0^(1/2)`, with scalar |y_i|<=p_Omega.
This is a scalar cube, not a product of HS balls. For real V in the common
admitted domain, uniqueness identifies b_0 with b_*(V,0). If the admitted
uniform scalar row bounds are M for T_* and M_C for C_0=T_*^-1, and
||b_0||_(infinity,HS)<=C_b delta_V, direct row summation proves

    D_a(sigma p_a) subset Omega(p_Omega)
       if M[p_a+C_b delta_V/sigma]<=p_Omega,
    Omega(p_Omega) subset D_a(sigma p_a)
       if C_b delta_V/sigma+sqrt(D) M_C p_Omega<=p_a.     (SH8)

These are alternative sufficient inclusions with different fixed chart
multipliers; neither asserts equality. They preserve the original cube
and all colours. Fixed multipliers of p preserve SH2--SH5. Since sigma p
vanishes, the auxiliary chart is eventually inside C_ch. Any original
G/cut containment still uses GC6's admitted original margins; its optional
G subset C_ch condition is not obtained by increasing u. No SA box rate
beta>8 is identified with this corollary's original-block mu.

**OC26--OC30.** Its shrinking event is the group cap
`Q_good={Q_X<q_*(u) for all X}`, with
`Q_X=sum_(e owned X)|W_e-U0_e|_n^2` and
`q_*=p_Omega^2/(16pi^2 M^2 u)`. Each chord is <sqrt(q_*); under OC's
trace/injectivity margin, the principal traceless logarithm obeys
`||log Q||HS<=(pi sqrt(N)/2)|Q-I|_n`. Thus the cap lies inside
D_a(sigma p_Omega/(8M)), and then inside the unchanged Omega under its
b_0 margin. This cap is not a product-a ball. The real comparison also
requires the MATERIAL extra condition

    delta_V^2<=c_OC q_*/(8a_bulk V_K),
    V_K=(4K+1)^4, K=K(q_*) from OC7.                     (SH9)

It costs an additional factor of order K^-2 in the sigma p_Omega curvature
window. Our proportional coarse window does not imply it. Intersecting
with that smaller window, and if desired shrinking eta by the same factor,
is possible but is a further restriction with the corresponding extra
Cauchy costs. No complex normalized comparison follows from OC's real one.

For the concrete consumer choice p_Omega=(log(2+u))^alpha_cut,
alpha_cut>5/2, any fixed multiple p_a satisfies SH2 and also
sigma p_Omega^3->0 and sigma^2 p_Omega^12->0. The original-source discs
of SN/GC/OC/FR can be intersected once before u. OC still needs SH9, with K=O(1+log u), and
GC/FR keep their own curvature/chart/G margins. These are parameter and
geometric matches only; no old indicator, measure or normalization is
replaced by identity.

## 5. Scope and preservation

This corollary supplies an explicitly uniform physically shrinking
auxiliary-chart return from SN. It does not close the difference between
that chart and any consumer cut, the original G/Omega decomposition,
complementary or history-dependent returns, holes, effective iteration,
continuum existence or the physical mass gap. It creates no new mechanism
and needs no new primary-paper premise; the consumed estimates are
reconstructed substitutions in the cited mathematical sources.

All preceding sources and packages remain immutable. The source is frozen
before the compact [read manifest](checks/shrinking_chart_return_read_manifest.json)
and [author receipt](checks/shrinking_chart_return_receipt.json). Root owns
fresh review, publication and all Git/front/audit operations.
