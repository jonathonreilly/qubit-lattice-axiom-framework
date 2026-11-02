# Frozen and transported original charts with one critical prefactor

This constructs a complete-original-reader logarithm comparing the fixed
physical product chart C_a(Vbar) with the transported product chart C_a(V),
for complex V near a fixed real coarse field Vbar. The proof includes
deterministic regional whole-link fibres with fixed real sufficiently small
touching exterior fields. It uses one actual phase in frozen physical fine
coordinates and one critical prefactor for every transport mask. A new
boundary current retains its nonlinear coordinate map and cofactor velocity.
Its rare Gaussian bound survives the connected logarithm.

Only these product charts move. No hard Q, G, Omega or history predicate,
and no rough compact fine numerator, is transported. The result supplies
a pure-chart comparison and a nonzero frozen regional chart denominator.
It does not construct the connected marked compact-return gas. Full non-free
continuum existence and a positive physical continuum mass gap remain OPEN.

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

Bałaban's small/large-field localization and Dimock's exposition are the
constructive antecedents. The new coordinate-current and flagged counting
steps are proved here; no scalar or three-dimensional theorem is imported
as a four-dimensional SU(N) result. Review labels are not premises.

## 1. Actual fibres and a frozen-coordinate phase

Use the supplied bare density, pinned block-tree quotient, original source
labels and lifted T=2 seam convention of
[SC](SOURCE_LOCAL_COMPACT_RETURN_ASTRA.md), frozen at
`c39e78ac1d31024d5266e16ace022fa86497a6d09c45aa25b215ffa390533dff`.
The actual local library and regional construction are
[RF](REGIONAL_CRITICAL_FIELD_ASTRA.md), frozen at
`45a5665fc51683f026370e774ca8590b221bc5c9e13c07502225226cb13c962b`,
and [RC](REGIONAL_CHART_RETURN_ASTRA.md), frozen at
`b098d18ad22946d7b1e0a4d497e0b5d98250674e06803263d1106f14bf659094`.
The consumed Gaussian/reader construction is
[SN](SHIFTED_NONLINEAR_READER_RETURN_ASTRA.md), frozen at
`47423d924c938f627550ae592d4ef2d5ef3255d6f2e60b2ab0887b9a46425d1b`.
Their explicit estimates, with the modifications below, are used.

Fix N>=2, D=N^2-1, odd L>=3, T>=2, u>=N, sigma^2=N/u and kappa in
the fixed positive interval. There are m0=3L^4+1 free WHOLE links per
block and n0=D m0 scalar coordinates. Retain every colour, root, winding
and crossing mode. Nonroot gauge Haar volume and the tree Jacobian are one.

Fix real Vbar of admitted curvature delta and write V_c=exp(v_c)Vbar_c,
max_c ||v_c||HS<eta. Use ONE physical coordinate

    U_e=exp(a_e) U0_e(Vbar).                              (FT1)

Negative edges are inverses. For each original coarse link c, let M_c^+
be the arithmetic mean of its 24L^4 original forward words and M_c^-
the mean of their inverse words. Thus the holomorphic numerator is
h_c(V;U)=[tr(V_c^-1 M_c^+)+tr(M_c^- V_c)]/(2N).
On real fields this is the original Re tr(V_c^* M_c^+)/N. M_c^- is not
the inverse of M_c^+, and no complex conjugation is continued.

Let Lambda be any deterministic subset of free whole links. Use RF's
fixed stencils I_xi and B(Lambda)=union_(I_xi meets Lambda)(I_xi minus
Lambda). The physical exterior z is fixed. Only B(Lambda) is assumed
small, with bar_y_e=Log[z_e U0_e(Vbar)^-1] and
max_B ||bar_y_e||HS<zeta; deep exterior can be arbitrary real compact.
All components below use the same ambient cover and original stencil list.
The active touching-factor phase, including ACTIVE Haar logs, is

    F_L^fr(a;bar_y,v,epsilon)
       =-sigma^2 log w_L,epsilon(exp(a)U0(Vbar),z;V)
                       -sigma^2 sum_(e in Lambda)log j_N(a_e).      (FT2)

Every original physical factor touching Lambda occurs once in w_L.
Cross-boundary terms and their original sources are retained. Non-touching
factors, including any empty-stencil constants, form the exact common
physical factor W_out. Inactive Haar factors are part of the exterior
physical measure, not inserted into FT2. Consequently a full physical
fibre is W_out times the touching integral defined below. W_out is never
bounded by an extensive surrogate or divided away inside the density.

Let F_L^bar denote RF's actual phase at coarse output Vbar, with the SAME
fixed physical boundary. The exact identity is

    F_L^fr=F_L^bar+sum_(touching kernels c) Xi_c,
    Xi_c=-(kappa/2)tr{Vbar_c^-1(exp(-v_c)-I)M_c^+
                             +M_c^-(exp(v_c)-I)Vbar_c}.             (FT3)

Indeed sigma^2(kappa u)=N kappa. The Wilson terms, fine means, ORIGINAL
compact normalizers and frozen-coordinate Haar terms in FT2 do not change
when only the output V changes. They are retained in F_L^bar. FT3 is not
a claim that a normalizer is constant as its fine arguments vary. All its
fine arguments during the present proof stay in its proved small-field
analytic domain; no rough compact argument is complexified.

## 2. A local perturbation construction of the actual frozen critical field

Write a_f0 for RF13's fine scalar radius, H for its actual vacuum-subtracted
bound, q_f=(8L^4+8)D, s0=9^4, d0=(9L^4+5)s0, d1=q_f d0,
d2=q_f^2 d0. Fix a preliminary eta0<=1/64. A word has length <=5L.
On the RF fine polydisc each exponential and inverse exponential has
operator norm <=exp(D a_f0); the unitary frozen lift has norm one.
The series bound ||exp(+-v)-I||HS<=exp(eta0)||v||HS and the trace
inequality therefore prove, uniformly in u,T and the real center,

    |Xi_c|<=eta H_X,
    H_X=2N kappa_+ exp(1+5L D a_f0).                    (FT4)

Each Xi_c has the original kernel root and v_c's original endpoints.
It is combined with that kernel vertex, so no new stencil incidence is
introduced. Its fine Taylor coefficients obey eta times the Cauchy
majorant f_X(t)=H_X(1-t/a_f0)^(-q_f). Define

    S_X(t)=f_X'(t)-f_X'(0)-t f_X''(0),
    J1=2d1 exp(beta s0)f_X'(0),
    J2=2d2 exp(beta s0)f_X''(0),
    N_X(t)=d1 exp(beta s0)[S_X(t)+t S_X'(t)],
    D_X(t)=2d2 exp(beta s0)[f_X''(t)+t f_X'''(t)].        (FT5)

These bounds are for sums of individual coefficient suprema. One can
factor Xi_c as sum_alpha v_(c,alpha) times the integral of its derivative
at t v_c, 0<=t<=1; thus the eta factor is valid at the coefficient level,
including v=0. Root marks cost d1 or d2. Marks in substituted fields
choose a Taylor slot and give t S_X' or t f_X'''. This is precisely the
direct monomial count behind RF13, now applied to the explicit FT3.
The coefficients retain the local v and Vbar readers, not just their bounds.

Use Kbar=F_0''(0;Vbar), with its full finite-u spread and Haar terms, as
the lift precision. Its principal Kbar_L, inverse G_L and geometry-only
patch core P_L are RF8--RF11 at the REAL center. Choose RF16's same
ambient R>=4 and beta=(16R)^-4; no transport mask will change this core.
Keep RF's gamma,B,c0,m_G,b_G,A_G,K_Q,N,B_src,D_H,d_reg and c_y.
For Y=c_y zeta define the actual frozen force budget

    F_bd^fr=g_*(1+rho)delta+eta J1
        +(K_Q+rho B_src+eta J2)Y+(1+rho)N(Y)+eta N_X(Y).              (FT6)

It follows by substituting bar_y^B in the actual full force and projecting
onto Lambda. In particular the regional boundary term does not vanish at
flat Vbar. Its complete boundary-membership reader is still N_9(owner).
Impose, on one fixed joint domain,

    Y<=tau/2, A_G F_bd^fr<=tau/4,
    A_G[rho B_src+eta J2+(1+rho)N'(2tau)+eta N_X'(2tau)]<=1/4,
    d_fr:=D_H(2tau,rho)+eta D_X(2tau)<=d_reg.             (FT7)

All constants were fixed before the actual radii. These restrictions have
positive solutions: first reduce preliminary tau,rho,eta, then choose
zeta,delta,eta smaller as needed. Restricting eta again does not alter
the coefficient formulas. Also retain the original local coarse/fine
analytic ceilings and RF/RC bounds whenever comparing to their named
transported integral. Those intersections have positive radii.

For completeness the fixed-point map is RF19 with the additional local
linear Hessian H_v=Xi''(0) and nonlinear term N_v from Xi. Its constant
term is the actual projected force at bar_y^B. Its norm recursion is

    Psi(t)=A_G[F_bd^fr+(rho B_src+eta J2)t
       +(1+rho)(N(t+Y)-N(Y))+eta(N_X(t+Y)-N_X(Y))].       (FT8)

On 0<=t<=tau it has Psi(0)<=tau/4 and derivative <=1/4. Expanding
Picard iteration into the same rooted substitution trees gives absolutely
convergent canonical atoms, with

    partial_a F_L^fr(b_L)=0,
    V_beta(b_L)<=t_L:=2A_G F_bd^fr<=tau/2.               (FT9)

Ordinary scalar-supremum contraction identifies the same point in the
small complex cube; a pointwise exterior field is not assigned an
unproved marked norm. The construction is holomorphic in v,epsilon and
the admitted boundary coordinates. All masks, original source labels,
real-center data and complete boundary readers stay in each tree.

Set K_L^*=partial_a^2 F_L^fr(b_L), Delta_L=K_L^*-Kbar_L. FT7 gives
Q_beta(Delta_L)<=d_fr. Apply the ACTUAL ordered inverse identity

    C_L=(K_L^*)^-1=P_L+E_lift,L+T_crit,L,
    T_crit,L=sum_(j>=1)G_L(-Delta_L G_L)^j.              (FT10)

The root/marked products of RF22 give, with h=m_G d_fr,
M(T_crit)<=m_G h/(1-h) and
B(T_crit)<=b_G h/(1-h)+m_G d_fr(m_G+b_G)/(1-h)^2.
Together with RF11 this bounds BOTH tails by
M_beta(E)<=e:=2e_*/3 and B_beta(E)<=B_E at fixed preliminary ceilings.
The proof is the Neumann series and marking either the first G or one
Delta G factor. It preserves every original reader and membership flag.
The real P_L has Re P_L>=c0 and RF24's exponential entry envelope.
Every principal P_L[I] has inverse G with Re G>=a:=c0/g^2,
||G||<=b_P:=1/c0 and absolute row/column bound v_I. Keep
e_*<=min(c0/8,1/(4v_I),a/(64v_I^2)). No inverse principal precision
is substituted for a Gaussian marginal covariance.

The source-linear Hessian, output-linear Hessian, boundary field and all
critical corrections occur in FT8--FT10. Local agreement follows by the
same finite-word argument as RF: fix the ambient vertex/Taylor/path list,
keep zero coefficients for excluded memberships, and take its absolutely
convergent limit. Agreeing original (Vbar,v,epsilon,bar_y) data and active
membership on a complete reader give identical coefficients. This is a
new frozen-coordinate family, not an identification with RC's stationary
point in transported coordinates.

## 3. The actual holomorphic coordinate map and its boundary current

On an active crossing link assigned to coarse link c define

    Phi_(e,t)(a)=Log[exp(a)exp(t v_c)], 0<=t<=1;         (FT11)

on other links it is the identity. This order follows from
U0_e(V)=exp(v_c)U0_e(Vbar). All maps below use the traceless principal
branch reached from zero. Fix a preliminary HS neighborhood with
||a||HS<=1/32 and eta0<=1/64. The matrix log argument stays within
operator distance 1/2 of I. Its convergent power series, whose derivative
norm is <=2 there, gives

    ||Phi_t(a)-a||HS<=4eta,
    ||D_a Phi_t||<=4, ||(D_a Phi_t)^-1||<=4,
    ||partial_t Phi_t||HS<=4eta.                        (FT12)

For the inverse use Log[exp(z)exp(-t v_c)]; its argument remains on a
fixed slightly larger neighborhood, e.g. ||z||HS<1/8. These derivative
bounds also follow directly from the exponential derivative integral.
All scalar Cauchy radii used for these maps are fixed preliminary radii,
not r_a, zeta or tau. No inverse shrinking radius enters FT12.

Define the cofactor velocity vector

    q_e(t,a)=det(D Phi_t(a))(D Phi_t(a))^-1 partial_t Phi_t(a),
    ||q_e||2<=C_J eta, C_J=4^(D+2).                    (FT13)

The maps and q_e depend only on v_c and that one fine parameter a.
Their original coarse reader lies in the fixed collar of e. In particular
q_e=0 at v_c=0. Identity links have identically zero current.

The analytic Haar identity is EXACT:

    j_N(Phi_t(a)) det D Phi_t(a)=j_N(a).                 (FT14)

For real anti-Hermitian a,v this is local right-invariance of normalized
Haar measure, with the orientation continued from the identity. The two
sides are holomorphic in all D complex scalar coordinates of a and v.
Their equality on real open coordinate balls extends successively in
each variable; the log domain and determinant branch above fix it uniquely.
Thus the pullback of the frozen physical top form equals the transported
original Haar top form. In particular the phases obey

    F_L^tr(a;z,v,epsilon)
      =F_L^fr(Phi_1(a);bar_y,v,epsilon)
                           -sigma^2 sum_e log det D Phi_(e,1)(a_e).
                                                                  (FT15)

The boundary coordinates in F^tr are Log[z_e U0_e(V)^-1]. The derivative
of the last term need not vanish. Mapping one critical point by Phi does
not establish stationarity for the other coordinate density.

For any holomorphic f on the sweep of a full D-colour ball B_r, direct
differentiation of the pullback top form proves

    int_(Phi_1(B_r)) f(z) dz-int_(B_r) f(a) da
       =int_0^1 dt int_(partial B_r) f(Phi_t(a)) q_e(t,a).n(a) dS(a).
                                                                  (FT16)

Indeed the derivative of f(Phi_t)det D Phi_t is the divergence in a of
f(Phi_t)q_e. The cofactor divergence identity follows by cancellation
of the mixed second derivatives in the alternating determinant formula.
Integrate that identity over the real ball. This proves FT16 also for
complex maps; it is not a change of a hard indicator into a holomorphic
function. Tensoring FT16 over links gives every product face and corner,
each with its own shared t_e. There is no curvature or normal derivative.

## 4. One full prefactor for all deterministic transport masks

For M subset the active crossing links let D_M be the product chain
Phi_(e,1)(B_ra) for e in M and B_ra otherwise, all in frozen coordinates.
Define the ACTUAL touching integrals

    I_L,M=h_N^|Lambda| int_(D_M) exp(-F_L^fr(a)/sigma^2) da,
    P_L^fr=h_N^|Lambda|(2pi sigma^2)^(D|Lambda|/2)
                 exp[-LogDet K_L^*/2-F_L^fr(b_L)/sigma^2].          (FT17)

I_L,empty is the fixed physical chart fibre. For M equal to all active
crossing links, FT14 makes it RC's transported physical chart fibre with
the SAME fixed exterior z. W_out P_L^fr is the full physical prefactor.
Every kernel vacuum, boundary constant, finite-u term, determinant and
Haar dimension is present. No bound declaring this prefactor small is
used. Its cancellation between masks is exact. The accretive logarithm
branch is the one continued from the real positive Hessian.

Apply FT16 first on every transported link. Call the selected transport
faces T_f subset M. On all remaining volume links apply the constant
critical-translation identity
int_B f(x-m)=int_B f(x)-int_0^1 int_(partial B)(m.n)f(x-tm).
Call those old critical faces H_f, disjoint from T_f. With p=r_a/sigma,
m=b_L/sigma and real sphere parameter x_e, the Gaussian argument is

    z_e=x_e-w_e(x_e),
    w_e=t_e m_e                              for e in H_f,
    w_e=m_e-[Phi_(e,t_e)(sigma x_e)-sigma x_e]/sigma
                                               for e in T_f,
    w_e=0                                    otherwise.            (FT18)

The old flux is -b_e.n_e/sigma. The new flux is
q_e(t_e,sigma x_e).n_e/sigma, with its PLUS sign. These signs are
included once. The surface measure is the real sphere measure at radius
p, not the area measure of an undeclared translated surface. The q_e
factor is its full pullback cofactor velocity. Its sigma^-1 comes from
sigma^(D-1) surface scaling divided by sigma^D volume scaling.

Writing R_xi for the remainder of the actual F_xi^fr at b_L as in RC7,
FT16 and the old translation identity give exactly

    I_L,M/P_L^fr=sum_(T_f subset M, H_f subset Lambda\T_f)
       int [product_H (-b_e.n_e/sigma)]
           [product_T (q_e(t_e,sigma x_e).n_e/sigma)]
                 g_(C_L)(x-w(x)) product_xi exp[-R_xi(x-w(x))].    (FT19)

The measure has spheres on H_f union T_f, balls on all other active
links, and independent unit-interval parameters on every face. All active
Haar factors already occur in F^fr; FT19 does not multiply them a second
time. No boundary coordinate or physical exterior variable is moved.

Here is an explicit complete-reader bound for the variable shifts.
The local vector d_e(t,x)=Phi_(e,t)(sigma x)-sigma x has one local atom
and ||d_e||HS<=4eta. Giving it the conservative N_4(owner) reader gives
V_beta(d)<=C_d eta, with

    C_d=4D m0 9^4 exp(beta 9^4),
    tau_s=tau+C_d eta, s=D tau_s/sigma.                 (FT20)

Suprema include all real sphere parameters. Multiplying by the fixed
H_f,T_f flags cannot increase the component or marked sums. Consequently
the unscaled shift family b_e or b_e-d_e has component-root bound tau_s
and full marked bound tau_s. Its coefficients may depend on x_e; this
dependence is confined to that same active link and is never differentiated.

Fix preliminary ceilings bar_tau,bar_zeta,bar_eta satisfying the producer
conditions, and bar_tau_s>=bar_tau+C_d bar_eta. Choose a_f<a_f0/2 and
r_t<a_f/16 with bar_tau_s+r_t<a_f/2. At actual radii require

    r_a<min(r_t/8,1/64), 2(r_a+tau_s)<=r_t,
    tau_s<=min(bar_tau_s,r_a/(16D)),
    eta_bar=4A I0 r_a(1+r_a)<=a/128,
    (L_hat^2+2eta_bar)(D tau_s)^2<=a r_a^2/64.           (FT21)

Here I0=15; A,L_hat are fixed ceiling constants defined below, before
r_a is chosen. Every actual physical field in FT19 lies within
r_a+2D tau_s of the frozen lift. Thus the whole sweep lies in the original
small-field normalizer domain. FT21 uses the REGIONAL tau from FT6--FT9,
not the smaller global curvature-only shift of the mixed-cap theorem.

## 5. Nonlinear primitives and all face-pattern flags

For each touching original vertex use the enlarged root N_13(x_xi),
s_v=27^4, d_v=(9L^4+5)s_v and d_1v=q_f d_v, as in RC. The frozen
boundary coordinates and every boundary-membership decision are inside
this root. From FT4 and the old vacuum-subtracted local bound a valid
active-field difference bound is 2[(1+bar_rho)H+bar_eta H_X]. Use

    f_F(t)=2[(1+bar_rho)H+bar_eta H_X](1-t/a_f)^(-q_f).              (FT22)

The common original vacuum and the actual value F_xi^fr(0;bar_y,v) are
only removed for a derivative estimate; both stay in FT17. Center Taylor
coefficients have root mass e^(beta s_v) f_F^(l)(bar_tau)/l! and marked
mass d_v e^(beta s_v)[f_F^(l)(bar_tau)+bar_tau f_F^(l+1)(bar_tau)]/l!.
These follow by expanding first at active fine zero and then in the
actual b_L atoms; exterior fields are bounded coefficient arguments.

A pattern now has three possibilities per active link: no face, old
critical face, new transport face. Disjoint H_xi,T_xi must equal the
intersections of H_f,T_f with that vertex's active stencil. Normalize
the combined shift atoms by tau_s; their component and marked norms are
<=1 by FT20, even when the local d atom depends on x_e. The same cubic
AM--GM estimate as SN8 applies pointwise. Binomial expansion has at most
2^l choices for a monomial of degree l. Valid fixed-ceiling bounds are

    A_sh=8e^(beta s_v) f_F'''(bar_tau+r_t)/6,
    B_sh=8d_1v e^(beta s_v)
       [4f_F'''(bar_tau+r_t)+(bar_tau+r_t)f_F''''(bar_tau+r_t)]/6,
    K_pat=3^q_f, W0=2K_pat A_sh, W1=2K_pat B_sh.         (FT23)

Center marks use bar_tau; a translated slot mark selects one of l slots
and uses its normalized full marked norm. The larger bar_tau+r_t in B_sh
safely pays both. Local x-dependent coefficients are bounded before the
sums. The monomial field degree used for Gaussian moments is unaffected:
the normalized local d factors have bound one, and no derivative hits them.
The Mayer union-convolution sum is exactly
sum_(k>=1) a^(star k)/[k(2A)^(k-1)], with
A>=max(1,A_sh,A3,A4), where the fixed-ceiling unshifted bounds are

    A3=e^(beta s_v)f_F'''(bar_tau+r_t)/6,
    B3=d_v e^(beta s_v)[f_F'''(bar_tau+r_t)
                                  +bar_tau f_F''''(bar_tau+r_t)]/6,
    A4=e^(beta s_v)f_F''''(bar_tau+r_t)/24,
    B4=d_v e^(beta s_v)[f_F''''(bar_tau+r_t)
                               +bar_tau f_F'''''(bar_tau+r_t)]/24.

Its individual coefficients obey

    |f_(xi,H_xi,T_xi;S)|<=chi sigma P3 exp(2A sigma P3) w_(xi;S),
    P3=sum_(i in I_xi active)(|x_i|+(tau_s/sigma)1_face(i))^3.       (FT24)

chi retains balls on all selected non-face active slots. The geometric
series and its marked derivative give W0,W1. This explicitly pays all
three-state patterns; two-state SN constants are not silently reused.
No-face signed singletons have the old even-part bound
sigma^2(P4+P3^2). Expanding the even Mayer part as
exp(-R_even)cosh(R_odd)-1 and bounding the two positive geometric
convolutions at radius 2A gives, with all reader unions retained,

    E0=2A4+2A3^2,
    E1=2B4+4A3 B3+2A3^2(B3+B4)/A.

For instance each geometric convolution has mass <=2 and marked
derivative <=2B_j/A; marking either odd factor in its square gives
2A3 B3. These are NC12--NC15 recomputed using the actual f_F above.
To verify the signed cancellation, every density list is
even under simultaneous x->-x, its selected product of whole-link balls
is symmetric, and it has no shift. Its odd Taylor part therefore integrates
to zero coefficientwise, even for complex boundary/source/output data.
Face species receive no parity improvement.

After selecting distinct original vertices W, expand only their unused
volume balls as one minus exterior failures. The bad-link set B_f obeys

    B_f disjoint H_f union T_f union F_L(W),
    H_xi=H_f intersect L_xi, T_xi=T_f intersect L_xi.     (FT25)

All D coordinates on each retained whole link are active. Unused Gaussian
coordinates integrate to one, giving the principal C_L[I] on
I=scalar(F_L(W) union H_f union T_f union B_f). Since w is supported
on retained faces and depends only on their own x, the marginal identity
holds for each fixed complex shifted active argument. No nonlinear
vertex is evaluated on an unbounded bad coordinate. Empty W,H_f,T_f,B_f
has value exactly one; there is no residual-only vacuum. Empty Lambda
likewise has touching integral and prefactor both equal to one.

Primitive species are a selected nonlinear reader atom, a signed bad link,
an old flux atom -b_(e,alpha;S)n_alpha/sigma, and a new local flux
q_(e,alpha)(t,sigma x)n_alpha/sigma. Each face has ONE measure and t_e,
shared with every touching selected vertex. A link cannot have both kinds
of face, and each original vertex and face is used once.
Enlarge primitive readers by Q_xi=N_(16R)(x_xi) or Q_e=N_(16R)(X_e).
Keep s_c=(32R+1)^4, d_c=(9L^4+5)s_c, d_h=m0 s_c. These are AMBIENT
collars, including holes and small-torus cases. Partition primitive readers
by overlap, retaining their lists, both face flags and the mask requirement
e in M on a new face. Then P_L[I] is block diagonal between components;
each inverse-core block and determinant reads its component once.
Presence AND absence conditions in FT25 are internal because touching
stencils have intersecting collars. Endpoint factorization is therefore
exact before any covariance forest is applied.

## 6. Density-only forests with the actual variable shifts

Use the fixed critical covariance FT10. Set

    t=v_I e<=1/4, t_E=v_I^2 e/(1-t)<=a/48, ell=-log(1-t)/2,
    c_*=2b_P^2/a+b_P+t_E+1,
    L_jet=max(1,sqrt(2 exp(1)c_*)), L_hat=sqrt(2)L_jet,
    K_m=v_I/[2(1-t)]+v_I^2(16/a+1)/(1-t)^2.             (FT26)

Between distinct primitive components mask only E entries by independent
pair variables s_jk. The radius-two polydisc is accretive exactly as in
SN14; quantitative bounds use real masks in [0,1]. With G=P_L[I]^-1,
the density has the exact determinant-loop/inverse-chain expansion

    g_(P+E)(z)=g_P(z) exp{sum_(k>=1)(-1)^k Tr[(GE)^k]/(2k)
                  +(1/2)sum_(k>=1)(-1)^(k-1)z^T(GE)^kGz}.          (FT27)

Expand BOTH E tails and the exponential into ordered lists with their
factorials. Row/column sums give the loop bound |I|ell and chain bound
t_E|z|^2/2. Scalar Cauchy radii sqrt(nu_i/(2c_*)) give
A_I exp(-a|x|^2/8)L_jet^|nu| product_i sqrt(nu_i!), where
A_I=(b_P/(2pi))^(|I|/2)exp(|I|ell). An E-reader mark costs
K_m D_z(I), with D_z(I)=sum_(i in I,j,S contains z)e^(beta|S|)sup|E_S(i,j)|
and sum_i d_z(i)<=B_E. This is the full normalized density estimate;
the determinant and remote diagonal readers have not been dropped.

Now Taylor-expand that density at the REAL x in the variable w(x).
For each fixed x, sqrt((nu_i+k_i)!)<=2^((nu_i+k_i)/2)
sqrt(nu_i!)sqrt(k_i!). The convergent positive series
S(y)=sum y^k/sqrt(k!) obeys S(y)<=sqrt(2)exp(y^2) and
S'(y)<=sqrt(2)sqrt(1+2y^2)exp(y^2), by Cauchy--Schwarz with weights 2^-k.
FT20 therefore gives the mixed density bound

    A_I exp(-a|x|^2/8)L_hat^|nu| product_i sqrt(nu_i!)
              2^(D(|H_f|+|T_f|)/2) exp[L_hat^2 s^2(|H_f|+|T_f|)]. (FT28)

All local d and nonlocal b coefficients keep their actual readers.
A reader mark in a shift has the EXTRA factor

    K_tr sum_(e in H_f union T_f) d_z^w(e),
    K_tr=(L_hat/sigma)(1+sqrt(2)L_hat s),
    sum_e d_z^w(e)<=tau_s.                              (FT29)

Suprema in d_z^w include the real surface parameters. The location of
this pin is an actual face; it is not reassigned to an arbitrary bulk
vertex. Flux marks and marks in nonlinear arguments have already been
paid by their primitive readers and W1.

The notation in FT28 means [partial_z^nu g(z)] at z=x-w(x), NOT the
derivative in x of the composition g(x-w(x)). The covariance derivative
identity is consequently

    partial_(s_jk) int Psi(x) g_(C(s))(x-w(x))
       =sum_(i in I_j,l in I_k)E(i,l)
                   int Psi(x)[partial_zi partial_zl g_(C(s))(z)]
                                                   evaluated at z=x-w(x).
                                                                  (FT30)

Here w, b, d, q, normals, hard balls, surface parameters and the flagged
nonlinear vertices are fixed under the artificial covariance parameters.
No field derivative of Phi or a hard boundary is taken. Gaussian domination
and FT28 justify every finite-order derivative. At disconnected pair masks
the density and the already grouped primitives factor exactly. Apply the
finite path-minimum forest identity to independent pairs and only then
evaluate its real forest mask. Its elementary monomial proof partitions
pair clocks by their unique maximum spanning forest; radius-two analyticity
permits passage to the density integral. No derivative of a path minimum
or of an original-data reader weakening is substituted.

## 7. Integrated rare currents, scalar factorials and marked bounds

Each scalar belongs to <=I0=15 distinct original vertices. Repeated Mayer
powers were absorbed in the regulator, so the remaining polynomial degree
per scalar is <=6I0=90. The regulator is bounded by
exp[2eta_bar|x|^2+2eta_bar s^2(|H_f|+|T_f|)]. FT21 pays its shift cost
together with FT28. With omega_D the unit-sphere area, set

    M90=2^90 max(1,(2880/a)^45), K_g=max(1,exp(ell)sqrt(8b_P/a)),
    C_V=q_f(1+q_f)(K_g M90)^q_f,
    q_h=K_g^D 2^(D/2)exp(-a p^2/32),
    Q_s=(b_P/(2pi))^(D/2)exp(D ell)2^(D/2)omega_D
             p^(D-1)sigma^-1(1+s)^(90D)exp(-a p^2/64).             (FT31)

The bound (1+x)^j exp(-a x^2/64)<=M90 for j<=90 follows by maximizing
x^j exp(-a x^2/64). Bad-link tails use exponential Markov under the
variance-8/a product Gaussian. A face keeps its original sphere |x_e|=p,
the full D-dimensional area, and sigma^-1 flux. FT21 bounds the shift
exponential by exp(a p^2/64), leaving the rare factor displayed in Q_s.
No convex-set inclusion is substituted for an integral identity.

The integrated mixed jet is bounded by L_hat^|nu| product_i sqrt(nu_i!)
times primitive weights C_V sigma w_(xi;S), q_h,
Q_s sup|b_(e,alpha;S)|, and Q_s C_J eta respectively. A no-face
singleton can use C_V sigma^2 e_(xi;S). Counting all scalar flux components
by D gives the following complete-reader budgets:

    h_v=C_V sigma e^(beta s_c)(W1+d_c W0),
    h_2=C_V sigma^2 e^(beta s_c)(E1+d_c E0),
    h_h=d_h e^(beta s_c)q_h, h_0=h_v+h_h,
    h_S=Q_s e^(beta s_c)tau(1+d_h D),
    h_T=Q_s e^(beta s_c)d_h D C_J eta,
    j_S=K_tr Q_s e^(beta s_c)D tau tau_s,
    j_T=K_tr Q_s e^(beta s_c)D C_J eta tau_s,
    C0=1+K_m B_E,
    h_c=min(beta/16,1/[4(1+L_hat^2 e)],
                         beta/[64n0(1+L_hat^2 e)]).     (FT32)

The old flux mark uses V_beta(b)<=tau; a new flux is one local function
inside Q_e, so its mark costs the collar incidence d_h. The j budgets
sum the actual face flux at e and then its shift pin d_z^w(e) from FT29.
This retains the new rare factor even for a remote critical-field reader.
There is no inverse sigma factor attached to an unrelated volume root.

Here are the full counting details needed for this new species. Spend
delta_b=beta/8 for primitive overlap trees, and another delta_b for scalar
Gaussian attachments. With primitive budget h=h_0+h_S+h_T<=h_c, the
overlap-tree recursion has supersolution a_o exp(beta|S_o|). Allocate
k_i unordered child Gaussian legs to each scalar i: the multinomial gives
1/k_i!, while FT28 gives sqrt((k_i+incoming_i)!). Thus the scalar sums
are sum y^k/sqrt(k!) and sum sqrt((k+1)!)y^k/k!, bounded by exp(2y)
and exp(4y) for y<=1/2. Their arguments are at most L_hat^2 e h.
The dimension inequality is |I_B|<=n0|S_B|, including every colour and
inactive reader block; it is never replaced by an intrinsic-region count.
FT32 pays the attachment exponent with the second support margin.

Raw connected species retain their primitive lists, Gaussian tree E atoms,
density lists and shift decorations. Base supports remain disjoint; their
complete supports also include ALL E and shift readers. Ordinary reader
marks cost C0 h; marking a Gaussian tree edge costs L_hat^2 B_E h^2.
For a shift-reader mark, root the primitive tree at its actual marked
face and the Gaussian tree at that component. Both positive recursions
are linear in that distinguished root weight and retain the same child
supersolutions. Its cost is j_S+j_T, not a volume force estimate. Thus

    norm_(beta-2delta_b,marked)(raw)
                  <=C0 h+L_hat^2 B_E h^2+j_S+j_T.       (FT33)

This verifies the additional variable-shift/current species directly.
All forest derivatives carry the individual scalar factorials; no
factorial of all legs of a component is used.

Assume h_0,h_S,h_T<=h_c/4. For raw species with no face, signed singleton
parity and positive degree-two rescaling give
E_0=C0(h_2+h_h)+(C0/h_c+L_hat^2 B_E)h_0^2. For species with a face,
rescale ONLY face primitive weights by h_c/[2(h_S+h_T)], holding every
field, covariance and regulator fixed. Each such species gains at least
that factor, and each distinguished j root gains exactly it. Hence

    E_all=E_0+2(C0+L_hat^2 B_E h_c)(h_S+h_T)+j_S+j_T.    (FT34)

To preserve specifically NEW transport rarity, rescale only new-face
primitive weights by h_c/(2h_T). The ordinary h_0+h_S stays <=h_c/2.
j_S is unchanged; j_T is multiplied by that factor. Undoing it in FT33
proves, for the ENTIRE transport-bearing raw family,

    E_T=2(C0+L_hat^2 B_E h_c)h_T+(2h_T/h_c)j_S+j_T.      (FT35)

If h_T=0 this family is empty and E_T=0. This count includes old faces,
all mixed corners and arbitrary vertex/density/critical-reader attachments.
It is not just a bound on a single transport surface.

## 8. A canonical connected logarithm with a transport witness

Require sigma<=1, q_h<=1, the three h bounds above, and

    E_all<=delta_b/2, E_T<=delta_b/2.                    (FT36)

Regroup raw species by overlap of their complete readers, retaining their
old base compatibility internally. Every admissible raw family has one
such partition; reader-disjoint groups reconstruct it. A third delta_b
pays this overlap recursion. A fourth pays the connected logarithm:
partition connected graphs by a fixed-order Kruskal tree; each allowed
extra-edge set is a Boolean interval, whose alternating sum is zero or
has modulus one. The rooted exponential tree recursion with neighbor
budget <=delta_b pays that last margin. At mu=beta/2 this constructs

    I_L,M=P_L^fr exp[sum_(connected Y) H_(L,M;Y)],
    sup_x sum_(Y contains x)e^(mu|Y|)sup|H_(L,M;Y)|<=E_all.         (FT37)

Finite atom/forest/list truncations, followed by the positive bounds,
justify all rearrangements. The graph identity holds first near zero
common activity multiplier and extends throughout its unit disc by these
absolute bounds. It proves nonvanishing of the actual integral, not a
formal logarithm of a possibly zero expression.

An extra counting step preserves transport rarity through BOTH final
operations. In their positive sums multiply just transport-bearing RAW
activities by lambda=delta_b/(2E_T)>=1. Non-transport raw mass is at most
E_all<=delta_b/2 and scaled transport mass at most delta_b/2. Both last
recursions still have total neighbor budget <=delta_b. Every final
transport-bearing coefficient gains at least lambda. Undoing it bounds
their complete-reader norm by 2E_T. For E_T=0 there are none. This avoids
the unjustified inference that a marked subfamily's norm automatically
survives regrouping without an extra argument.

All transport masks use ONE decorated library. A coefficient retains the
list of its new faces and is multiplied by product_(e in that list)1_(e in M).
Repeated occurrences in logarithm graphs retain this binary acceptance
factor. Everything else, including b_L,C_L and the full prefactor, is
independent of M. Therefore corresponding H coefficients agree when
original data, Lambda membership and transport flags agree on Y.
If A is the set of owners of M symmetric-difference M', then exactly

    log(I_L,M/I_L,M')=sum_(Y meets A) D_(M,M';Y),
    sup_x sum_(Y contains x)e^(mu|Y|)sup|D_(M,M';Y)|<=Theta:=2E_T,
    |log(I_L,M/I_L,M')|<=Theta |A|.                     (FT38)

For each decorated coefficient the difference of its two binary acceptance
factors has modulus <=1 and vanishes unless a new face at a changed owner
occurs. This proves FT38 from the transport-bearing coefficient bound,
not by subtracting two extensive critical actions or two volume estimates.
The distinguished logarithm is zero at v=0. Theta contains the eta factor
from the exact transport current. Constants in the bound need not be small.

## 9. Nonempty radius order, shrinking tubes and physical boundaries

The fixed-radius order is: fix N,L,kappa interval and RF's real-center
class; choose ONE ambient R and all lift/marked constants; choose preliminary
source/fine/output/boundary/critical ceilings so FT7 and the tail caps have
slack; compute FT22--FT26 and all local map constants; then choose r_a,
then tau and eta so FT20--FT21 hold; then reduce zeta,delta,eta and rho
to satisfy FT7 and the named RF/RC domain intersection. Choose u large
last for FT36. The constants in FT4, FT12, FT22 and FT26 were fixed
before this last restriction. All choices are independent of Lambda,T.

For an explicit shrinking family take

    p=(log(2+u))^alpha_cut, alpha_cut>5/2, r_a=sigma p,
    tau=c_tau sigma p, zeta=c_z sigma p,
    delta<=c_delta sigma p, eta<=c_eta sigma p.          (FT39)

Choose fixed positive c_tau first, then c_eta and c_z sufficiently small,
and c_delta smaller as necessary, so

    c_tau+C_d c_eta<=min(1/(16D),sqrt(a)/[8D sqrt(L_hat^2+a/64)]),
    c_y c_z<=c_tau/2,
    A_G[g_*(1+rho)c_delta+J1 c_eta
                       +(K_Q+rho B_src+bar_eta J2)c_y c_z]<=c_tau/8.
                                                                  (FT40)

Choose also c_eta<=c_z/16 when using the named RC physical-boundary
specialization. Nonlinear terms in FT6 are O((sigma p)^2); the remaining
force reserve makes FT7 eventual. Fix rho at a positive preliminary
value satisfying its strict contraction/Hessian inequalities at tau=eta=0.
All nonlinear derivative and output Hessian debits tend to zero. The
original RF/RC conditions using delta+8eta and boundary Y are met by
further reducing these fixed constants, not by changing the atom library.

For p>=1, FT31--FT35 give finite fixed constants C_i with

    E_all<=C1 sigma^2+C2(1+p^(91D+2))exp(-a p^2/64),
    Theta<=C3 (eta/sigma)(1+p^(91D+1))exp(-a p^2/64).    (FT41)

In the second estimate j_S/h_c is eventually bounded: it is itself a
polynomial in p times the same Gaussian rare factor. The powers follow
from p^(D-1), (1+s)^(90D), and K_tr tau_s=O(p+p^2); all n0,d_h and
full-reader constants remain in the fixed C_i. Thus FT36 holds for all
sufficiently large u, uniformly in regions and volume. No numerical
threshold is claimed.

For the physical q-good regional specialization require SC5's
sqrt(q)<=zeta/(8pi sqrt(N)) and sqrt(Nq)<2sin(pi/(2N)). SC6 then gives
the actual fixed real principal logs ||bar_y_e||HS<=zeta/16 on every
touching boundary link. With eta<=zeta/16 their transported coordinates
Log[exp(bar_y_e)exp(-v_c)] have norm <=zeta/2 by the same fixed log
series. Thus both named fibres lie on their actual domains, and FT38
supplies a nonzero frozen chart denominator with these FIXED exterior
physical fields. It asserts neither a conditional Q-cap denominator nor
nonvanishing with arbitrary near-boundary exterior values.

For q=c_q sigma^2 p^2, take c_q<=c_z^2/(64pi^2 N). SC's further
real-curvature restriction delta=O(sigma p/K^2) is compatible with FT39.
This pure-chart theorem also admits eta=O(sigma p/K^2), or the narrower
SC width O(sigma^2 p^2/K^4), by restriction of the SAME coefficients.
It does not remove any coarse-width restriction of a rough compact
numerator. The proposed quadratic compact debit in
[QC](QUADRATIC_COARSE_RETURN_ASTRA.md) is not a premise here.

At half the admitted v,epsilon tubes, mixed scalar jets of FT38 obey
the corresponding marked norm bound times
ell! nu! (2D/eta)^|ell| (2/rho)^|nu|. A derivative at an original label
outside Y is zero. Cauchy costs are retained; there is no claim of uniform
unscaled coarse derivatives or a fixed wider RG consumer domain.

## 10. Exact use for Delta_chart and the remaining physical gap

For Lambda=E and all crossing links transported, let
R_Y=H_(E,empty;Y)-H_(E,all;Y). The correction retained in CG32--CG33 is now

    Delta_chart=Z_a^fr/Z_a^tr-1=exp(sum_Y R_Y)-1,
    sup_x sum_(Y contains x)e^(mu|Y|)sup|R_Y|<=Theta.     (FT42)

For a finite torus this yields |Delta_chart|<=exp(Theta T^4)-1. The
local logarithm, not Delta_chart itself, has a volume-uniform rooted
bound. [CG](COMPACT_RETURN_GLUING_ASTRA.md), frozen at
`924628d1ff6f3d6cdeef614b6126c54bfa28c657a06734991ceb3e969b6cf9d2`,
has additional hard selectors and bounded real-buffer insertions.
FT42 does not move any of them. Nor does it transport a compact slice or
white-coordinate Omega continuation. The marked compact expectation
estimate, inherited-history normalization, wider-domain RG matching,
continuum existence, non-freeness and positive physical continuum gap
remain separate unproved obligations.

[Lohmann, arXiv:1411.1107v1, section 2.1.4 and Remark 2](https://arxiv.org/html/1411.1107v1)
treats Gaussian parameter derivatives and an ultralocal site-product cutoff
in a single-scale boson/spin setting; its stated initial covariance
assumptions include symmetry and normality. Those hypotheses do not supply
this nonlinear SU(N) contour current. FT27--FT35 rebuild the required
density-only derivative and mixed-reader estimates for the actual full
matrix, without transferring field derivatives onto the boundary.
[Dimock, arXiv:1212.5562v2, sections 3.13--3.14](https://arxiv.org/html/1212.5562v2#S3.SS13)
localizes fluctuation integrands before the cluster logarithm in scalar
phi-four, d=3. The analogy motivates keeping the original readers and
boundary terms; its theorem is not this gauge-model transport identity.
Bałaban's [large-field localization work](https://doi.org/10.1007/BF01238433)
is credited as antecedent. The earlier accessible publisher abstract was
used only for scope; no uninspected full-text estimate is invoked.

This source is frozen before its compact
[read manifest](checks/frozen_transported_chart_read_manifest.json) and
[receipt](checks/frozen_transported_chart_receipt.json).
[PROCESS_LIGHT](PROCESS_LIGHT.md) requires a DIFFERENT fresh hostile
reviewer. Review targets include the exact numerator-only perturbation,
regional force budget, actual Haar/cofactor identities, nonlinear shift
jets, scalar factorials, three-state flags, transport rarity after the
logarithm, and the retained compact/hard-predicate limitations.
No science numerical run, predecessor/shared-front/Git/PR or audit edit
belongs to this author unit. Root owns independent review and integration.
