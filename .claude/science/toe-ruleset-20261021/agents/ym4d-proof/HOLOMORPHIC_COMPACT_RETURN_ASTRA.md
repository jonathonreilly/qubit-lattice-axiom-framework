# Holomorphic original-cut return with frozen physical selectors

This proves a complete-original-reader connected logarithm for the actual
bare original-cut partition function on a nonempty complex coarse tube
and a fixed original-source polydisc. The first reference is the physical
product chart frozen at a real coarse center. Every compact numerator
fine variable, its rough mean, its positive normalizer, and every selector
remain REAL or frozen exactly as specified below. Only small complementary
chart variables are deformed.

The coarse radius has order sigma p/K^2. An optional exact comparison with
the transported original-a chart adds a distinct transport-bearing log.
It is not assigned the compact-only decay rate. The old white Omega
matching, inherited histories, effective-class iteration, full non-free
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

Bałaban's localization and Dimock's exposition are constructive antecedents.
No scalar or d=3 theorem is transferred to full4D SU(N). The supplied
action is a premise, and review verdicts are not mathematical premises.
In particular the frozen-transport source used below is checked as source
mathematics; its independent review status supplies no estimate.

## 1. The actual holomorphic object and two different chart integrals

Fix N>=2, odd L>=3, T>=2, u>=N and the admitted compact positive kappa
interval. Keep the original tree quotient, lifted T=2 seam convention,
all free whole links and all root, harmonic, crossing and colour modes of
[SC](SOURCE_LOCAL_COMPACT_RETURN_ASTRA.md). Put

    D=N^2-1, m0=3L^4+1, k=D m0, sigma^2=N/u,
    n=m0 T^4, d=k T^4, V_c=exp(v_c)Vbar_c,
    max_c||v_c||HS<eta, |epsilon_p|<rho.                (HC1)

Vbar is REAL with curvature at most delta. All selectors use this fixed
Vbar, and U0bar=U0(Vbar). E_X is the set of m0 free positive links owned
by block X. Coarse/source labels are the ORIGINAL ones. For the actual
24L^4 forward words and their inverse words write M_c^+,M_c^-; the latter
is not the inverse of the former. The actual holomorphic density is

    w_epsilon(U,V)=exp[-u sum_p(1+epsilon_p)s(U_p)]
             product_c exp[(kappa u)/(2N)
                    tr(V_c^-1 M_c^+ + M_c^- V_c)]/Z_(kappa u)(M_c).

On REAL fine U, M_c is the original compact mean and Z_(kappa u)(M_c)>0
is the original compact integral. It is independent of the output V.
No real-part operation or complex conjugation is applied to complex v.
On small complex fine charts use s(P)=tr(2I-P-P^-1)/(2N) and the actual
paired-word analytic normalizer. Their RF/RC zero-free domain is used
there; positivity is asserted only for the unchanged REAL rough inputs.

Let chi_cut be the original block-INTERIOR plaquette cut; it is independent
of V. Let C_a^fr be the physical chart U_e=exp(a_e)U0bar_e,
||a_e||HS<r_a on every free whole link. The three actual objects are

    Z_cut(V,epsilon)=int_(real SU(N)^E)dH chi_cut(U)w_epsilon(U,V),
    Z_a^fr(V,epsilon)=int_(C_a^fr)dH w_epsilon(U,V),
    Z_a^tr(V,epsilon)=int_(transported product chart C_a(V))dH w_epsilon.
                                                                  (HC2)

The last integral is the holomorphic small-chart chain, with its actual
Haar form. A hard cut is not evaluated at its complex fine points.
Impose r_a<=epsilon_1/8, so the REAL frozen chart lies in chi_cut.
No whole-domain change of variables is made in Z_cut.

Use physical frozen coordinates a throughout the proof. On any active
whole-link set Lambda, keep the physical exterior z fixed. Only its
touching links must have bar_y=Log(z U0bar^-1) small; deep exterior may
be arbitrary compact. The exact touching phase, including ACTIVE Haar
logs, is F_L^fr=-sigma^2 log w_L-sigma^2 sum_(e in Lambda)log j_N(a_e).
Its relation to the actual phase at output Vbar is

    F_L^fr=F_L^bar+sum_(touching kernels c)Xi_c,
    Xi_c=-(kappa/2)tr[Vbar_c^-1(exp(-v_c)-I)M_c^+
                                  +M_c^-(exp(v_c)-I)Vbar_c].       (HC3)

Wilson terms, physical fine means, original compact normalizers and
frozen-coordinate Haar factors stay in F_L^bar. Xi changes only the kernel
numerator. Non-touching factors are the exact common W_out, with physical
exterior Haar; inactive Haar is not inserted into F_L^fr.

## 2. Actual frozen critical data and the regional chart correction

We consume and reconstruct the relevant estimates of
[FT](FROZEN_TRANSPORTED_CHART_ASTRA.md), exact source SHA256
`c7cea2f9bb096af300a9a978c945d9c5d68ae5e63581654a3034902d000d70b8`.
Use ONE ambient RF/RC cover and R_amb,beta throughout. All constants in
this section and the denominator estimates below are computed at fixed
preliminary ceilings before q,K,u or the final radii are chosen.

Here is the actual perturbation check. On RF's fine polydisc of radius
a_f0, a word has length <=5L and its exponentials have norm <=exp(D a_f0).
The exponential series and trace inequality give
|Xi_c|<=eta H_X, H_X=2N kappa_+ exp(1+5L D a_f0). Combine Xi_c with its
original kernel vertex; no new fine stencil or incidence is introduced.
With q_f=(8L^4+8)D, f_X(t)=H_X(1-t/a_f0)^(-q_f), use FT5's explicit
J1,J2,N_X,D_X. These are coefficient-level bounds: factor Xi as the sum
of its original v components times the integral of its derivative at t v.
Thus the eta factor and every Vbar/v reader survive all root marks.

For Y=c_y zeta the regional force is bounded by

    F_bd^fr=g_*(1+rho)delta+eta J1
         +(K_Q+rho B_src+eta J2)Y+(1+rho)N(Y)+eta N_X(Y).
    Y<=tau/2, A_G F_bd^fr<=tau/4,
    A_G[rho B_src+eta J2+(1+rho)N'(2tau)+eta N_X'(2tau)]<=1/4,
    D_H(2tau,rho)+eta D_X(2tau)<=d_reg.                 (HC4)

The boundary term is retained even at flat Vbar. Expanding the actual
fixed-point equation into the RF substitution trees gives the same
pointwise unique critical point and its full-reader atoms. With Y=0,
the GLOBAL branch satisfies the sharper bound

    (F^fr)'(b_fr)=0,
    V_beta(b_fr)<=t_fr:=B_delta delta+B_eta eta,
    B_delta=2A_G g_*(1+rho), B_eta=2A_G J1.             (HC5)

The critical covariance is the ordered inverse series about the actual
real-center lift precision Kbar, including its finite-u spread and Haar
terms. It is C_fr=P+E_lift+T_crit, with BOTH tails and their full original
readers. FT10's Neumann and marked-product estimates give fixed
M_beta(E)<=e and B_beta(E)<=B_E, where
e<=min(c0/8,1/(4v_I),a/(64v_I^2)), a=c0/g_cov^2. The real finite core P
has the same ambient patch geometry. Every principal P[I] retains the
inverse row bound v_I and accretivity used below. Coarse v, real Vbar,
original sources, active membership and boundary membership remain in
each atom. No principal precision is substituted for a marginal covariance.

The full GLOBAL frozen prefactor is exactly

    K_fr=(F^fr)''(b_fr), C_fr=K_fr^-1,
    P_fr=h_N^n(2pi sigma^2)^(d/2)
                      exp[-LogDet K_fr/2-F^fr(b_fr)/sigma^2].       (HC6)

Restore every constant vacuum to F^fr. All finite-u normalizers, Haar,
dimension, determinant and critical-action terms occur in HC6 once.
Its extensive size is not estimated as small.

For Lambda=J_R and fixed physical exterior define I_R^fr and I_R^tr as
the actual touching integrals on frozen and transported product charts.
The equality with the named RC transported integral must be checked:
on an active crossing link Phi_t(a)=Log[exp(a)exp(t v_c)] satisfies
j_N(Phi_t(a))det D Phi_t(a)=j_N(a). This is Haar right-invariance on
real coordinates, extended holomorphically on the fixed log branch.
The cofactor velocity q_e=det(D Phi_t)(D Phi_t)^-1 partial_t Phi_t has
norm <=4^(D+2)eta. Differentiating the pulled-back top form gives the exact
boundary current integral, with PLUS sign and all its product corners.
The phase identity includes the logarithm of this Jacobian; critical
points in the two coordinate densities are NOT identified.

FT's actual frozen phase and that current therefore give

    log(I_R^fr/I_R^tr)=sum_Y R_(R;Y),
    sup_x sum_(Y contains x)e^((beta/2)|Y|)sup|R_(R;Y)|<=theta_tr,
    |log(I_R^fr/I_R^tr)|<=theta_tr |R|.                 (HC7)

The last inequality sums over owners of active crossing links, a subset
of R. It retains the full original readers, including remote covariance
and critical-field readers. It is not an absolute critical-action bound.
Both actual integrals are nonzero. Their common W_out cancels only in
this same conditional ratio and is kept in global identities.

The envelope theta_tr is the explicit 2E_T of FT31--FT35. In that notation

    E_T=2(C0+L_hat^2 B_E h_c)h_T+(2h_T/h_c)j_S+j_T,
    h_T=Q_s e^(beta s_c)d_h D C_J eta,
    j_S=K_tr Q_s e^(beta s_c)D tau tau_s,
    j_T=K_tr Q_s e^(beta s_c)D C_J eta tau_s,
    tau_s=tau+C_d eta.                                 (HC8)

Here Q_s is FT31's full D-dimensional sphere/flux bound, not a new norm
hypothesis. Every sigma^-1 and current cofactor is present. Its density
forest differentiates only normalized Gaussians at x-w(x); neither a
current nor an indicator is differentiated. Its two charged rescalings
preserve at least one new current through reader regrouping and the log.
Consequently, on FT's explicit shrinking domain and uniformly in R,z,T,

    theta_tr<=C_T(eta/sigma)(1+p^(91D+1))exp[-a p^2/64].             (HC9)

C_T is fixed by those finite formulas. No norm of an arbitrary compact
insertion is inferred from HC7. Q-good physical boundaries have
||bar_y||HS<=zeta/16, and eta<=zeta/16 puts their transported logarithms
inside zeta/2. Thus both named fibres in HC7 have their ACTUAL boundary
domains. Section 7 below verifies all these restrictions simultaneously.

## 3. The frozen local compact difference and its single energy payment

Use Q_X=sum_(e in E_X)||U_e-U0bar_e||HS^2/N. Set c,a_bulk,a_shell,alpha,
K,V_K exactly as SC4--SC7 and QC2, with the same fixed rho_0<1:

    c=min((1-rho_0)/[8(30L^2)^2 L^3(L+20)],kappa_-/[8L^3]),
    a_bulk=6(1+rho_0)m0,
    a_shell=24(1+rho_0)+4kappa_+(5L)^2, alpha=min(1,c/(8a_shell)),
    g_shell=log(1+alpha),
    K=ceil max(1,(8/g_shell)^2,(2/g_shell)[1+log(2500m0/q)]),
    V_K=(4K+1)^4, r=4K+4.                               (HC10)

For an r-connected set A put I_j=N_(2j)A, R_j=N_(2j+1)A and
S_j=N_(2j+2)A minus R_j. The LOCAL selector is exactly CG6:

    ell_Aj=1_(Q_X>=q on A) 1_(Q_X<q on R_j minus A)
       *1_(Q(S_j)<=alpha Q(I_j))
       *product_(i<j)1_(Q(S_i)>alpha Q(I_i)), 0<=j<K.    (HC11)

Every test, failure and absence is frozen at Vbar. For a history h of
such cores at pairwise distance >r, the exact partition is
Pi_h=1_good(O_h) product_h ell_Aj, where R_h=union_h R_j and O_h is its
complement. The bad set determines its r-components, and compact shell
growth gives exactly one first successful j per component: failure for
all j contradicts (1+alpha)^K q>4m0(4K+1)^4. Hence sum_h Pi_h=1.
Q=q is assigned to bad. This is independent of v and epsilon.

Fix real exterior z q-good on S_j and write R=R_j. Define the actual
integrals with all touching original factors and the original chi_R:

    N_Aj^c=int_(real SU(N)^J_R)dH chi_R ell_Aj w_R(U,V),
    N_Aj^(a,fr)=int_(C_a^fr on J_R)dH chi_R ell_Aj w_R(U,V),
    N_Aj^out=N_Aj^c-N_Aj^(a,fr)
          =int_(real SU(N)^J_R minus C_a^fr)dH chi_R ell_Aj w_R(U,V),
    B_Aj^c=N_Aj^c/I_R^fr, B_Aj^a=N_Aj^(a,fr)/I_R^fr,
    D_Aj^fr=N_Aj^out/I_R^fr.                            (HC12)

The numerator difference is ONE physical complement. Its pointwise
majorant has no factor two. The subtraction does not move a fine variable
or a rough kernel mean. All compact numerator domains and densities have
their original real Haar factors and original positive normalizers.

We now check why [QC](QUADRATIC_COARSE_RETURN_ASTRA.md), source SHA256
`515260d02f0a21e3dea55db2b98cb6ab00ece16684d40179df609922204798c7`,
applies to this LOCAL selector and this complement. Its energy and Schur
proof uses A-bad, the first shell and q-good touching boundary; it does
not use SC's longer absence predicate or smaller connectivity range.
For e=Re epsilon, define its actual energy E_R^e and reset A_ref^e at
Vbar. On HC11 the same physical filling and reset prove

    E_R^e>=c Q_I, Q_I=Q(I_j)>=q|A|, |R|<=V_K|A|,
    A_ref^e<=a_bulk delta^2|R|+a_shell Q_s,
    a_bulk delta^2|R|<=c Q_I/8, a_shell Q_s<=c Q_I/8.    (HC13)

The original brick estimate also pays exterior plaquettes: with
B_fill=30L^2, every labelled brick occurs at most eight times, and its
plaquettes not in P_R read only S_j. Their total cost is <=192Q_s.
Thus QC6--QC7 give

    sum_(c in C_R)[1-h(Vbar_c;M_c)]<=A_E E_R^e+A_Q Q_s,
    A_E=1/kappa_-+16B_fill^2/(1-rho_0), A_Q=384B_fill^2.

For a REAL word Q the paired numerator expansion gives
|h(exp(v)Vbar;M)-h(Vbar;M)|
<=sqrt(2/N)||v||HS sqrt(1-h(Vbar;M))+e^eta||v||HS^2/(2N).
The original Z_t(M) cancels identically. Young's inequality, with actual
|C_R|<=8|R|, consequently gives

    |w_R,epsilon(U,V)|<=w_R,e(U,Vbar)
          exp{u[E_R^e/32+(a_shell/4)Q_s+C_num eta^2|R|]},
    C_num=128kappa_+^2 A_E/N
           +16kappa_+^2 A_Q/(N a_shell)+4exp(1)kappa_+/N.            (HC14)

This holds on every real numerator point, including rough means and the
restricted complement in HC12. No complex positivity is assumed.

For the denominator used at this intermediate step use the ACTUAL
transported I_R^tr of QC5, with the SAME fixed physical z. Its full
Haar-inclusive critical phase is Phi_R(v,a;bar_y,epsilon). QC10--QC17
bound the local mixed derivatives on fixed Cauchy radii r_f,r_v, subtracting
and restoring identical constant vacua. The mixed norm is L_vf and coarse
Hessian norm L_vv; the actual critical inverse has norm <=2/gamma.
Their checked zero-field force and full Schur calculation yield

    ||A_v(0)||2<=a_v delta sqrt(|R|)+b_v||bar_y||2,
    ||A_vv(v)||op<=B_v=L_vv+2L_vf^2/gamma,
    a_v=G_v+2L_vf G_0 sqrt(k)/gamma,
    b_v=L_vf(1+2B_*/gamma),
    |A_R(v)-A_R(0)|/sigma^2
       <=u[(a_bulk delta^2|R|+a_shell Q_s)/8+C_den eta^2|R|],
    C_den=4B_v/N+16a_v^2/(N^2 a_bulk)
                              +4pi^2 b_v^2/(N a_shell).            (HC15)

These constants are the explicit QC13--QC18 derivative counts, fixed
before the actual radii. The estimate uses ||bar_y||2^2<=pi^2N Q_s/4.
It includes the active Haar and ORIGINAL normalizer derivatives and
differentiates v with exterior physical z fixed. No frozen stationary
point is substituted for this transported critical point.

Keep QC19's FIXED positive source radius rho. Its actual imaginary-source
Schur argument has Re A_R(0,epsilon)/sigma^2<=u(A_ref^e+S_src),
S_src<=c Q_I/8. This follows from the source-force L2 bound and
A''=grad H_s^T(K_R^*)^-1 grad H_s, with Re A'(0)=0, at v=0.
The signed reset minimum retains all normalizer logarithms before using
their nonpositive sign. It is not an absolute O(u tau^2|R|) estimate.

With C_quad=C_num+C_den, impose
delta^2<=c q/(8a_bulk V_K), eta^2<=c q/(32C_quad V_K).
The complete pointwise energy remaining in the ratio to I_R^tr is

    (31/32)E_R^e-A_ref^e-S_src-(a_shell/4)Q_s
       -(a_bulk delta^2|R|+a_shell Q_s)/8-C_quad eta^2|R|
       >=[(31-8-4-1-1)/32]c Q_I-c q|A|/32
       >=c q|A|/2.                                    (HC16)

This calculation pays each original energy once. It remains valid on any
further restriction of HC11, in particular the physical chart complement.
The compact normalizer cap, all k|R| determinant modes, h_N and Gaussian
dimension give exactly QC24's p(u)=p0+p1log(1+u), p1=4D+k/2, with its
explicit fixed p0. The remaining compact Haar mass is <=1.

Finally multiply by the ACTUAL I_R^tr/I_R^fr from HC7, with the inverse
sign in its logarithm. Thus each of B^c,B^a,D^fr satisfies

    sup |B_Aj^c|,sup |B_Aj^a|,sup |D_Aj^fr|
       <=exp{[p(u)+theta_tr]V_K|A|-c u q|A|/2}.          (HC17)

The only new price here is theta_tr |R|. No region volume or denominator
normalization is dropped. Outside q-good touching boundary set these
coefficients to zero before evaluating an unadmitted denominator.
Their native locality follows from the ORIGINAL physical integrals HC12,
not by relabeling individual regional critical-field or covariance atoms
with smaller supports. The complete touching-data reader is contained in
N_(2K+4)(A), hence in the Gamma_A used below.

## 4. Exact simultaneous resummation on frozen domains

For distinct r-components the active R_j are at distance at least seven.
Their touching ORIGINAL physical factor sets are disjoint. Assign each
plaquette, normalized kernel and cut to its actual touching region once,
and every other factor to W_out,h. Then

    chi_cut w_epsilon=chi_(O_h)W_out,h product_h chi_Rj w_Rj.        (HC18)

The source labels and fine means are unaltered. A q-good exterior obeys
its original interior cut, as does the real frozen chart. Conditional
integration in the ONE actual global frozen-chart density supplies
product_h I_Rj^fr, not a product of arbitrarily normalized reference laws.
Let <.>_fr denote this density divided by nonzero Z_a^fr. Exactly

    Z_cut/Z_a^fr=sum_h <1_good(O_h) product_h B_Aj^c>_fr,
               1=sum_h <1_good(O_h) product_h B_Aj^a>_fr.            (HC19)

The empty term is the all-good cap divided by Z_a^fr in both lines.
It is not one by itself. No variation-one property is assigned to <.>_fr.

Expand B^c=B^a+D^fr. For a selected family s put
R_s=union_s R_j, H_s=(union_s N_r(A)) minus R_s. First integrate the
dummy frozen chart variables in R_s; D^fr depends only on its real S_j,
disjoint from every selected R. In the remaining variables impose q-good
on H_s. Every remaining bad component is at distance >r from selected
A; its first-shell choice is unchanged. Conversely each history containing
s gives exactly this remaining component configuration.

The necessary annular intersection is kept: N_r(A) may meet an unselected
R_k, but cannot contain its bad core. The intersection lies in R_k minus
that core, where its ell already enforces q-good. For another SELECTED
R_k the condition must instead be removed, since its chart variables are
dummy and I_Rk^fr must remain uncapped. This is why ALL selected regions
are removed in H_s. Summing the unselected chart histories therefore gives

    sum_(h contains s)<1_good(O_h) product_s D_Aj^fr
                                     product_(h minus s)B_Aj^a>_fr
       =<1_good(H_s) product_s D_Aj^fr>_fr.             (HC20)

This is a finite bijection on fixed REAL integration domains. It holds
for complex v and epsilon, without analytic continuation of any predicate.
It does not use CG32's hybrid transported sea functional.

Group selected cores by overlap of Gamma_A=N_(r+2)A. For each group g
retain its entire list, n_g=|union_g A|, Gamma_g=union_g Gamma_A and
H_g=(union_g N_r A) minus (union_g R_j). Any cross-group annular or
range-r conflict would force Gamma overlap. Thus groups with disjoint
ORIGINAL Gamma_g reconstruct exactly the selected family, and

    Theta_g^fr=1_good(H_g) product_g D_Aj^fr,
    Z_cut/Z_a^fr=<sum_(Gamma-compatible F)product_(g in F)Theta_g^fr>_fr,
    |H_g|<=H_K n_g, H_K=(8K+9)^4,
    |Theta_g^fr|<=b_g^fr
       :=exp{[p(u)+theta_tr]V_K n_g-c u q n_g/2}.        (HC21)

Every fine argument of Theta is REAL and in H_g. Define it as zero off
the actual joint cap before evaluating its ratios. It is measurable in
these variables and holomorphic in v,epsilon. Its COMPLETE native reader
is Gamma_g, including Vbar, original v outputs, sources and every frozen
absence/failure. H_g may be empty; its nonempty reader and field-free
coefficient are retained. No full exterior cap remains after HC20.

## 5. The marked frozen-phase Gaussian construction

We now verify the extension of [MK](MARKED_COMPACT_CHART_ASTRA.md), source
`04f79ed4d0c58e97f3cade072631966b577f02754f9a96d6dcd18ee2f3045800`,
to the actual frozen phase. Its proof did not differentiate a compact
insertion, but its constants and critical field must be recomputed.

Use FT22's fixed preliminary vertex majorant

    f_F(t)=2[(1+bar_rho)H+bar_eta H_X](1-t/a_f)^(-q_f).

Taylor-expand original vertices first, then substitute the HC5 critical
atoms. Use FT23's A3,B3,A4,B4,A_sh,B_sh and choose A>=max(1,A_sh,A3,A4).
These include Vbar/v/source readers and all output perturbations, without
adding vertices. For ternary OWNER flags ordinary/side/marked, at most
3^(q_f) choices give

    W0=2*3^(q_f)A_sh, W1=2*3^(q_f)B_sh,
    E0=2A4+2A3^2, E1=2B4+4A3B3+2A3^2(B3+B4)/A,
    eta_bar=4AI0 r_a(1+r_a)<=a/128, I0=15,
    Q=q_f k, s=k t_fr/sigma.                            (HC22)

All of these are explicit fixed-ceiling constants except the displayed
small regulator. In particular there is no 1/eta, 1/q or 1/zeta in W0,W1.

Fix a compatible F in HC21 and M=union_g H_g. Keep a_M=sigma x_M REAL.
Translate only complementary original-a blocks using the full-block
Stokes identity of MK10. For side blocks H disjoint M put

    z=x-m_M-t m_H, m=b_fr/sigma,
    Omega0=product_(m0 whole links)B_(r_a/sigma)^D,
    Z_cut/P_fr=sum_(F,H) (-1)^|H| int
        product_g Theta_g^fr(sigma x_Hg) product_(X in H)(m_X.n_X)
                           g_(C_fr)(z) product_v[1+W_v(z)].        (HC23)

The measure is real R^(k|M|) with Theta's actual cap, partial Omega0 and
dt_X on H, and Omega0 on remaining blocks. It is defined as zero before
evaluating any vertex off a marked cap. W_v is the remainder of the
actual F_v^fr after all jets through degree two at b_fr, divided by
sigma^2 as in MK. All product sides and corners are retained. Rough
numerator inputs inside Theta remain real; shifted regional chart
variables occurring in the reference are only dummy variables.

After selecting DISTINCT nonlinear vertices W and exterior bad blocks B,
the exact activation and flags are

    B disjoint M union H union F_b(W), H disjoint M,
    J_v^m=M intersect B_v, J_v^s=H intersect B_v,
    I=all k scalar coordinates in M union H union B union F_b(W).   (HC24)

Keep presence AND absence before primitive grouping. All remaining
unconstrained modes integrate to one, giving PRINCIPAL C_fr[I]. Complete
coefficient readers are enlarged by the same Q_X,Q_v=N_(16R_amb) collars
and widehat_Gamma_g=N_(16R_amb)(Gamma_g). Their overlap components retain
original Gamma compatibility and every flag. They have disjoint fields,
block-diagonal P[I], and core inverses/determinants reading each component
once. The cardinality bound is |I_B|<=k|S_B|. Empty-field groups remain.

For completeness the normalized density list is the exact determinant
loop/inverse chain series with G=P[I]^-1:

    g_(P+E)(z)=g_P(z) exp{sum_(j>=1)(-1)^j Tr[(GE)^j]/(2j)
                    +(1/2)sum_(j>=1)(-1)^(j-1)z^T(GE)^j Gz}.

Both E tails and every original reader are expanded. Radius-two independent
component-pair masks stay accretive; real forest masks preserve the row
bound e. Let b_P=1/c0, ell=-log(1-v_I e)/2,
t_E=v_I^2e/(1-v_I e), c_*=2b_P^2/a+b_P+t_E+1,
L_hat=sqrt(2)max(1,sqrt(2exp(1)c_*)) and K_m as MK15.
Scalar optimized Cauchy estimates and translation expansion give, at any
multiindex nu,

    A_I exp[-a||x||^2/8] L_hat^|nu| product_i sqrt(nu_i!)
         *2^(k(|M|+|H|)/2) exp[L_hat^2 s^2(|M|+|H|)],
    A_I=(b_P/(2pi))^(|I|/2)exp(|I|ell),
    K_tr=(L_hat/sigma)(1+sqrt(2)L_hat s).               (HC25)

The factorial inequality is sqrt((nu_i+j)!)<=2^((nu_i+j)/2)
sqrt(nu_i!)sqrt(j!), and sum z^j/sqrt(j!)<=sqrt(2)exp(z^2).
An E-reader mark costs K_m D_x(I), whose full pin sums to B_E. A shift
mark costs K_tr sum_(X in M union H)d_x^b(X), where the ACTUAL HC5 atoms
satisfy sum_X d_x^b(X)<=t_fr. No coarse derivative is taken in this forest.
Every artificial covariance derivative acts on this normalized density
alone; compact functions, sources, v, normals and flags are fixed.

The original incidence bounds each polynomial degree by 6I0=90 regardless
of forest order. With fixed C_bar>=L_hat^2+2eta_bar and

    t_fr<=r_a/(16k), C_bar(k t_fr)^2<=a r_a^2/64,
    M90=2^90 max(1,(2880/a)^45), K_g=max(1,e^ell sqrt(8b_P/a)),
    C_V=Q(1+Q)(K_g M90)^Q,
    L_M=K_g^k 2^(k/2)(1+s)^(90k)exp[C_bar s^2],
    a_g=b_g^fr L_M^|H_g|,                              (HC26)

the integrated mixed jets are at most
L_hat^|nu| product_i sqrt(nu_i!) times primitive weights. The weak vertex
weight is C_V sigma w, or C_V sigma^2 e for the signed no-mark/no-side
singleton. Bad and side weights are EXACTLY MK20's q_h and Q_s|b_i;S|
with t_b=t_fr and p=r_a/sigma. Their full k-dimensional body, face area,
Haar/Gaussian normalization and sigma^-1 flux are retained. Marked blocks
cost L_M each, without using a large-field Gaussian tail there. Assign
shifted polynomial costs once per marked/side block using incidence 15,
not once per forest edge. None of these costs is ambient-volume cost.

## 6. Complete readers and the two charged logarithm sums

Take xi=beta/8, s_c=(32R_amb+1)^4, d_c=(9L^4+5)s_c, d_h=s_c.
The full primitive budgets, now uniform on the joint v,epsilon domain, are

    h_v=C_V sigma e^(beta s_c)(W1+d_cW0),
    h_2=C_V sigma^2 e^(beta s_c)(E1+d_cE0),
    h_h=d_h e^(beta s_c)q_h,
    h_s=Q_s e^(beta s_c)t_fr(1+d_h k),
    h_g=sup_x sum_(g:x in widehat_Gamma_g)e^(beta|widehat_Gamma_g|)a_g,
    h_0=h_v+h_h, h=h_0+h_s+h_g,
    h_c=min(xi/2,1/[4(1+L_hat^2e)],xi/[8k(1+L_hat^2e)]).           (HC27)

The finite covariance forest identity follows by the independent-pair
heat identity and the clock/path-minimum proof, exactly as in MK23.
No derivative of a hard function or of a path minimum is substituted.
At disconnected masks, already grouped field functions factor. Allocate
unordered child Gaussian legs SCALAR by SCALAR: their sums are
sum y^j/sqrt(j!) and sum sqrt((j+1)!)y^j/j!, bounded by e^(2y),e^(4y)
for y<=1/2. With h<=h_c, primitive overlap and Gaussian attachment
recursions each spend one xi. Full raw supports include all base,
tree-E, density-E and translation-b readers, including both coarse data
Vbar and v and every original source. Raw base compatibility is retained.

For translation marks the actual distinguished root matters. Side flux
and shift masses give j_s=K_tr Q_s e^(beta s_c)k t_fr^2. For a marked
buffer, first retain the rare group containing its field owner X:

    sum_g e^(beta|widehat_Gamma_g|)a_g K_tr sum_(X in H_g)d_x^b(X)
       <=K_tr h_g sum_X d_x^b(X)
       <=j_g:=K_tr t_fr h_g.                           (HC28)

Both tree sums are linear in this distinguished primitive weight; their
ordinary child supersolutions are unchanged. Thus this pin survives the
sums with j_g, without an ambient force norm or a lost rare weight.
With C0=1+K_mB_E the complete-reader raw bound is

    ||a_raw||_(beta-2xi,mark)<=C0 h+L_hat^2B_E h^2+j_s+j_g.          (HC29)

This is the new frozen-phase application of the all-order density argument,
not an inference from local moments. Realness of the coarse output was
not used: its former role was small analytic control, the real finite
core, and the sharper global b bound, now supplied by HC3--HC5.

Assume h_0,h_s<=h_c/4 and h_g<=h_c/2. The no-compact raw family has bound

    epsilon_a=C0(h_2+h_h)+(C0/h_c+L_hat^2B_E)h_0^2
                              +2(C0+L_hat^2B_E h_c)h_s+j_s.

Only its centered signed singleton receives parity. This is cancellation
under x->-x, so complex v and epsilon do not change it. Rescale compact
primitive amplitudes alone by h_c/(2h_g), holding every density, b, source,
coarse parameter and regulator fixed. HC28 scales once, j_s does not.
Undoing at least one factor for each compact raw species proves

    epsilon_g=2(C0+L_hat^2B_E h_c+j_s/h_c)h_g+j_g.       (HC30)

If h_g=0 this subfamily is empty. Require epsilon_a,epsilon_g<=xi/4.
Regroup overlapping FULL readers while retaining old base incompatibility;
one xi pays its positive overlap trees and a fourth xi pays the hard-core
connected logarithm via the fixed-order Kruskal graph partition. To keep
the compact charge, first multiply compact-bearing RAW weights by
xi/(4epsilon_g). The total raw budget is <=xi/2; the two final sums have
norm <=xi/2. Every compact log term gained that factor, giving

    Z_cut=P_fr exp(sum_Y H_cut,Y), Z_a^fr=P_fr exp(sum_Y H_fr,Y),
    log(Z_cut/Z_a^fr)=sum_Y Psi_Y^comp,
    ||Psi^comp||_(beta/2,mark)<=2epsilon_g.             (HC31)

The index set retains primitive identity, ternary flag PRESENCE/ABSENCE,
original Gamma compatibility, contour faces and signs, scalar endpoints,
density/translation lists, reader groups and incompatibility graphs.
At zero compact roots its coefficient list equals the frozen-chart list
term by term. Thus every Psi^comp contains a compact group; two unrelated
O(sigma^2) bulk logarithms were not subtracted. Field-free groups remain.
The convergent gas proves actual nonvanishing, with the accretive log
branch, and restores every full P_fr factor. Local agreement holds whenever
the complete original (Vbar,v,epsilon) and membership data agree on Y.

## 7. One ledger and a common nonempty complex tube

There are TWO new expenditures from HC17's retained c u q n_g/2.
Impose the explicit conditions

    theta_tr V_K<=c u q/16,
    (C_bar k^2/N)t_fr^2 H_K<=c q/16.                  (HC32)

The first pays the regional fr/tr denominator correction. The second
pays the full marked-buffer translation C_bar s^2|H_g|. Therefore

    a_g<=exp{[p(u)V_K+D_bulk H_K-3c u q/8]n_g},
    D_bulk=k log K_g+(k/2)log2+90k log(1+p).            (HC33)

This is the explicit ledger 1/2-1/16-1/16=3/8; QC22's energy was not
reused. Source debits and coarse quadratic debits were already spent in
HC16. The residual positive terms include every dimension, determinant,
Haar, normalization, polynomial and collar-volume price.

The core union of a group is connected at range 8K+12 and its r-components
are unique. Shell choices cost at most K^(n_g). With

    W_K=(8K+13+32R_amb)^4, Delta_K=max(1,(16K+25)^4-1),
    t_g=K exp[beta W_K+p(u)V_K+D_bulk H_K-3c u q/8],
    h_g<=W_K t_g/(1-Delta_K^2 t_g), Delta_K^2t_g<1,      (HC34)

one pays full reader size by W_K n_g and counts connected sets by a
depth-first traversal with <=Delta_K^(2(n_g-1)) choices. A marked reader
box has <=W_K possible nearby core anchors. Wrapped tori only lower
these counts.

Here is a SINGLE radius construction, without an unspecified shrinking
intersection. Fix the common RF/RC/FT preliminary cover and constants,
QC's local Cauchy constants, and rho>0 satisfying QC19 and strict source
contraction/Hessian inequalities at tau=eta=0. Choose c_tau>0 with slack
in QC27/FT21, for example smaller than their displayed bounds and
sqrt(a)/(32D sqrt(C_bar)). Choose c_z>0 so
c_y c_z<=c_tau/4 and
A_G(K_Q+rho B_src+bar_eta J2)c_y c_z<=c_tau/16;
also choose it below QC28's k_y c_tau/c_y. All these are fixed positive
choices on the same atom library. Then set

    p=log(2+u)^alpha_cut, alpha_cut>5/2,
    r_a=sigma p, tau=c_tau sigma p, zeta=c_z sigma p,
    0<c_q<=min(1/(2N),c_z^2/(64pi^2N)), q=c_q sigma^2 p^2,
    delta=d_delta sqrt(q)/(4K(q)+1)^2,
    eta=d_eta sqrt(q)/(4K(q)+1)^2.                     (HC35)

Choose FIXED POSITIVE d_delta,d_eta small enough that

    d_delta^2<=c/(8a_bulk), d_eta^2<=c/(32C_quad),
    (B_delta d_delta+B_eta d_eta)^2
                                      <=c N/(4096 C_bar k^2).     (HC36)

Such choices exist, since every displayed constant was fixed first and is
finite. For K>=1, H_K/V_K<=256. Substitution of HC35--HC36 therefore
proves the second HC32 condition for ALL such K. It also proves the
reset and QC quadratic conditions exactly, not asymptotically.

The remaining checks have explicit limiting margins. delta/tau, eta/tau
and t_fr/r_a are O(K^-2); K(q)->infinity and K(q)=O(log u). Thus FT7,
RF/RC with delta_hat=delta+8eta, eta<=zeta/16, QC's fixed local output
cap and every global HC26 shift margin hold for all sufficiently large u.
The regional tau_s/tau tends to one, so the strict c_tau choice pays
the regional FT contour and its Gaussian shift. Nonlinear boundary force
remainders in HC4 are O((sigma p)^2), leaving the chosen linear reserve.
The q-good principal-log condition and chart-cut inclusion hold because
q,r_a->0 and sqrt(2Nq)<=r_a. The source radius remains the fixed rho.

By HC9, theta_tr V_K is at most a fixed polynomial in p,log u times
exp[-a p^2/64]. It tends to zero, while u q=N c_q p^2 tends to infinity.
Hence the FIRST HC32 condition holds eventually with its stated 1/16
reserve. Every chart convergence condition has bound O(sigma^2) plus
a polynomial in p times exp[-a p^2/64]. These observations yield one
finite u_0, independent of regions and T, after increasing it for the
finite list of stated inequalities. No unknown eta_RC or collapsing
unproved domain remains in this construction.

In HC34 the positive exponent is O((log u)^5), whereas u q=N c_q p^2
and 2alpha_cut>5. Enlarging this same u_0 gives

    h_g<=exp[-c u q/8], K_tr t_fr<=C(1+p)^2,
    h_v=O(sigma), h_2=O(sigma^2),
    h_h+h_s+j_s<=C(1+p)^(91k+2)exp[-a p^2/64].         (HC37)

The side sigma^-1 is cancelled by the actual flux t_fr=O(sigma p),
and its second translation factor by the second t_fr. All HC27/HC30
smallness conditions follow. The reader/log rescalings introduce only
fixed constants and this polynomial factor, so the resulting bound is

    ||log(Z_cut/Z_a^fr)||_(beta/2,mark)
                                 <=exp[-c N c_q p^2/32].           (HC38)

This holds on the FULL HC35 v tube and fixed original-source polydisc,
uniformly in T, with all inequalities and energy expenditures just checked.

## 8. Transported reference, derivatives and exact remaining scope

For the GLOBAL FT chart ratio let R_Y^tr=H_(empty;Y)-H_(all;Y).
Its sign is log(Z_a^fr/Z_a^tr), and its complete-reader norm is <=theta_tr.
Thus the exact optional comparison is

    log(Z_cut/Z_a^tr)=sum_Y[Psi_Y^comp+R_Y^tr],
    ||log(Z_cut/Z_a^tr)||_(beta/2,mark)
       <=exp[-c N c_q p^2/32]
           +C_T(eta/sigma)(1+p^(91D+1))exp[-a p^2/64].              (HC39)

The two species have distinct witnesses: a compact group and a transport
current. The second has no compact charge. After absorbing its displayed
polynomial one can bound the sum by
exp[-c N c_q p^2/32]+exp[-a p^2/128] for sufficiently large u; one may
not label the combined result with the compact-only rate automatically.
This statement does not transport any Theta, rough numerator or hard cut.

For a fixed original coarse/source multiindex ell,nu, at half the tubes
all displayed log families have their corresponding marked bounds times

    ell! nu! (2D/eta)^|ell| (2/rho)^|nu|.              (HC40)

Scalar Cauchy radii eta/(2D),rho/2 lie inside the full HS/source domains.
Derivatives outside Y's actual original labels vanish. The growing inverse
eta costs are retained; fixed-order losses can be absorbed into a weaker
rare exponent since log(eta^-1)=O(log u)=o(p^2). No fixed wider coarse
domain, uniform unscaled derivative class, or effective RG norm is claimed.
Selectors depend on the fixed REAL center, which is not differentiated.
Coefficient agreement requires agreement of that center data as well as
v and the original sources on the complete reader.

The original G and white Omega retain their definitions: G tests all fine
plaquettes and the original root-straight transporters; Omega is the
source-free white cube a=b_0+sigma C_0w, |w_i|<=p_Omega. At the original
real-center margins the literal decomposition remains

    Z_cut=Z_sec+I_(G minus Omega)+I_(G^c).              (HC41)

HC38 does not separately bound those two events or identify Z_sec with
either product chart. No frozen Omega(Vbar) continuation is equated with
a transported original sector. The new result concerns the actual cut
integral and the explicitly named chart references only.

This is one BARE step. Arbitrary future-conditioned kernel products,
inherited effective histories, effective-class closure, non-free continuum
existence and a positive physical continuum mass gap are not proved.
There is no new gauge deletion or axiom. Bałaban and Dimock are credited
for the localization architecture; the finite forest proof and the needed
sharp-domain/normalizer estimates are supplied locally, not imported from
their scalar or gauge theorems. No new external literature theorem is
invoked in this unit. The earlier bounded primary comparisons in MK/FT
do not supply this holomorphic compact return.

The mathematical source is frozen before the minimal author manifest and
receipt. A DIFFERENT fresh hostile source-first review is required.
No scientific numerical run or predecessor/shared-front/Git/PR/audit edit
belongs to this author unit. Root owns review and publication.
