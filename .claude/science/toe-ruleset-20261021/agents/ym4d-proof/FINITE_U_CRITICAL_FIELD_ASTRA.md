# Joint finite-u critical field and a positive reader covariance extension

The actual finite-u critical field is **already constructed in SA13**.
This unit does not claim its first existence. The new bounded result is a
joint original-source / complex-coarse-data construction at the small reader
rate supplied by PC, followed by a covariance extension at its actual
critical Hessian. The positive local covariance core stays at the lift;
the change to the critical Hessian is an additional small signed atom family.
Independent review of this new unit is required.

All statements concern one step of the supplied Wilson / normalized
paired-S4-prime model, including its finite-t normalizer, Haar density and
all free colour/root/harmonic directions. A Gaussian reference at this
critical point is not an interacting covariance or a physical mass gap.
Full four-dimensional continuum existence **and a positive physical
continuum mass gap remain OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Joint original-source/coarse continuation of the existing actual finite-u critical field and a small complete-reader extension of the positive lift covariance core."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. What the predecessors already prove

| Source and actual range used | Existing result | Boundary retained here |
|---|---|---|
| [CB8--CB14](COVARIANT_SOFT_BACKGROUND_ASTRA.md), sections 3--4 | Actual finite-u lift Hessian, centered local analytic vertices, small-curvature critical point, local coarse continuation and source branch | This is a coordinate-density critical point, not a global compact minimizer or a cut-integral theorem |
| [SA10--SA14](COVARIANT_SOURCE_ACTIVITY_ASTRA.md), section 3 | Complete original-reader critical-field atoms for real admitted V and a fixed complex Wilson-source disc; actual critical inverse and inverse square root | Its field construction requires small fixed curvature, **not** delta_V<=sigma p; it does not assert a common complex coarse product domain |
| [FR1--FR3, FR21--FR25](FIXED_SOURCE_RADIUS_ASTRA.md) | Uses that same actual finite-u b_e to center the selected contour, with no linear remainder | Its integral requires delta_V<=c_* sigma p, a small sigma p^3 and the stated margins; FR9's uncut comparison is only for polynomials |
| [IC6--IC13](INTERACTING_SELECTED_CORE_ASTRA.md) | Source-free critical-field and whitening atoms on a fixed complex original-coarse tube | The interacting remainder theorem has additional large-u/sector conditions; it is not imported here |
| [PC1--PC31](POSITIVE_READER_COVARIANCE_ASTRA.md) | Actual lift covariance has a positive local complete-reader core, small residual atoms, complex accretivity and exact Gaussian endpoint factorization | Output rate is only beta=(16R)^(-4); no integrated derivative-tree or returned-denominator theorem |

The [PC review](REVIEW_POSITIVE_READER_COVARIANCE_ASTRA.md), SHA256
`306195ea1bb4694d5fe00cab544490684a67f3ee7f3bffae0caca8fd14e5d37e`,
confirms that bounded source unchanged. PC source SHA256 is
`68bb7798bfcc0806c65531ab894e3e7f67ef1c155afd6da2f20f1b9dc2bb8da8`.
The needed estimates are rebuilt in section 3 before use.

[UNIFORM_SOFT_MINIMIZER_ASTRA.md](UNIFORM_SOFT_MINIMIZER_ASTRA.md), lines 1--31,
explicitly concerns the u-stripped **tree phase**. Its displayed quadratic
spread cancels, unlike the actual finite-u density. It is not a premise for
this critical field, its Hessian or its covariance.

## 2. Exact phase and joint parameter domain

Fix N>=2, D=N^2-1, odd L>=3, T>=2, u>=1, and kappa in its fixed positive
compact interval. Put m0=3L^4+1, n=m0 T^4, n0=Dm0, d=n0 T^4 and
sigma^2=N/u. The internal root-pinned tree quotient has integrated gauge
volume and Jacobian one. All d scalar coordinates remain. The lift has
internal links I and crossing-face links V_c; every actual paired
transporter equals V_c there. For T=2 its flat-brick coercivity argument
excludes the extra far periodic seam, not any actual integration mode.

In the fixed full-colour HS coordinates let U_e(a)=exp(a_e)U0_e(V), and
use the exact unsubtracted phase

    F_epsilon(a;V)=F_0(a;V)+sum_p epsilon_p W_p(a;V),
    F_0=sigma^2[-log w_0(U(a),V)-sum_free e log j_N(a_e)],
    W_p=tr(2I-U_p-U_p^-1)/2, K(V)=F_0''(0;V).              (FU1)

Only the original Wilson coefficients vary. The kernel t=kappa u stays
real and fixed. The normalized compact kernel, including its denominator,
is inside F_0; so is log j_N, exactly once. The normalized Haar constant
h_N is outside. Complex continuation uses inverses of negative edges and
the separate means `average T_tau` and `average T_tau^-1`, never a
conjugated complex field or inverse of an arithmetic mean.

CB's flat-brick recovery and actual second variation give

    K=H_V+E_V+kappa(1-c_N(kappa u))B_V+N^2/(6u)I,
    H_V>=a_gap I, B_V>=0, max(row_HS,col_HS)||E_V||<=24 delta_V,
    a_gap=1/max(4L^3(L+4)(60L^2)^2,2L^3/kappa_-),
    gamma=a_gap/2, delta0=min(1/24,a_gap/48),
    B=25+24 kappa_+(5L)^2+N^2/6, b=D B, c0=1/(2B).         (FU2)

Here c_N is the actual compact tilted-Haar mean, 0<c_N<1. The Wilson
error counts four Hessian entries per incident plaquette and six
plaquettes per link. The nonnegative path spread and Haar Hessian remain.
For real delta_V<=delta0, `gamma I<=K<=B I`, with scalar row/column bound
b, field range two in coarse sup distance and radius-three original-data
readers. Principal compressions are on every owned link and colour.

Fix a real center Vbar of curvature at most delta_*, to be chosen below,
and take the independent product domain

    V_c=exp(v_c)Vbar_c, max_c||v_c||HS<eta,
    |epsilon_p|<rho for every original fine plaquette.     (FU3)

Neither eta nor rho depends on u,T. Choose preliminary radii inside CB9's
joint local complex charts. Vacuum-subtracted local vertices, and Wilson
vertices separately, have a common bound H on a fine-coordinate polydisc
of radius a, uniform on a slightly larger preliminary coarse tube. There
are at most q=(8L^4+8)D scalar slots per vertex. Each scalar coordinate is
read by at most six Wilson terms, eight kernel terms and one Haar term.
CB9 proves these bounds for real u>=1 at fixed real t. The stronger FK/IC
large-u remainder theorem is not used to extend that domain.

For clarity, the local third-derivative Cauchy count also provides a finite
J0 such that

    max(row,col)||K(exp(v)Vbar)-K(Vbar)||<=J0 max||v_c||HS. (FU4)

For example, on a smaller common scalar radius a0 with bound H0,
`J0=1000q^3(H0+1)/a0^3` bounds the at most 15q^2 incident third derivatives
and colour conversions. Restrict the preliminary coarse radius below
min(a0/4,1/100,gamma/(4J0)). Then every principal K_A is complex symmetric
and accretive by 3gamma/4. This is a perturbation of the actual real matrix,
not positivity of a complex continuation by assertion.

## 3. Rebuilt lift covariance library and its full atom budget

Use coarse l1 distance, range r0=8, and set

    b_c=b+gamma/4,
    m=(1/8)log(1+gamma/(4b_c)),
    g_inv=(2n0/gamma)coth(m/4)^4,
    vK=n0*5^4, b_abs=vK*(B+gamma/4), J_abs=vK*J0.           (FU5)

Conjugating K_A by exp(m distance) changes both its row and column sums
by at most gamma/4. Cauchy--Schwarz bounds the operator norm by the
geometric mean of those sums; an accretive matrix with lower bound
alpha has inverse norm <=1/alpha. Undoing the weight therefore gives
`sup|K_A^-1(i,j)|<=2 exp[-m d_1(i,j)]/gamma`. Summing with half the
exponential rate over all n0 scalar modes per cell gives g_inv in both
endpoint sums. The torus-distance sum is bounded by the Z^4 sum. The
entrywise supremum envelope of K costs b_abs, and that of K-K(Vbar)
costs J_abs max||v||. This pays the exchange between suprema and sums.

Here and below labels are connected sets of **original coarse blocks**
containing field endpoints and every coarse/source reader, including both
ends of a coarse-link datum. For a matrix-atom family define M_beta as the
maximum weighted absolute row and column sum, with the suprema of
individual coefficients on FU3 **inside** the sums. Let B_beta be its
weighted absolute sum of all scalar entries whose label contains a fixed
cell, maximized over the cell; Q_beta=M_beta+B_beta. Repeated labels and
paths may be retained as distinct atoms. Scalar colour sums are explicit.

For completeness the geometry and residual argument are as follows. Fix
R>=4. If T<16R, use one whole-torus patch, whose cardinality is <(16R)^4.
Otherwise partition the torus into product intervals of lengths R to 2R.
For each box Q let f_Q be a smooth bump equal to one on Q, supported in
its R-neighborhood in the continuous torus, with sup-Lipschitz constant
16/R. Put chi_Q=f_Q/(sum f^2)^(1/2), so sum chi_Q^2=1. Its support on
owners is inside N_(R+1)(Q). Let

    A_Q=N_(2R)(Q), S_Q=N_(2R+4)(Q),
    J=16^4, s_R=(16R)^4, n_R=n0 s_R,
    C_chi=16(1+sqrt(2J)), beta=1/s_R, w=exp(1).             (FU6)

Every S_Q is connected, has <=s_R cells, and at most J labels meet a cell.
The denominator of chi is >=1; its Lipschitz bound follows by taking the
Euclidean norm of at most 2J bump differences. Thus chi has Lipschitz
constant C_chi/R. Its collar has width enough for K's range two. All
cutoffs and labels are fixed by geometry, not by V,epsilon,u. For the
whole-torus patch chi=1. These counts also retain the small-torus cost.

With zero-extended principal inverse G_A=K_A^-1, define

    P_A=chi_A G_A chi_A, P=sum_A P_A,
    D_A=chi_A(G_A-c0 I_A)chi_A,
    R_A=-[K,chi_A]G_A chi_A, Rcal=sum_A R_A.               (FU7)

Because chi_A is supported in A,
`chi_A K G_A chi_A=chi_A^2`. Expanding K chi_A proves exactly
`KP=I-Rcal`. Boundary entries are included; the collar puts every nonzero
residual endpoint inside A. Both G_A and R_A read only S_A. For real V,
G_A>=2c0 I_A, so D_A>=0 as a **whole** full-colour matrix and
`P=c0 I+sum D_A`.

For a residual row, each K-neighbor pair meets at most 2J cutoff
differences, each <=C_chi r0/R. Sum the inverse row by g_inv and the K
row by b_abs. For a residual column, first restrict to <=J final cutoffs,
then sum the K column and inverse column in that order. Hence, with

    p=w J g_inv, r=w(2J C_chi r0 b_abs g_inv)/R,
    d_core=p+w J c0,
    r<=min(1/4,c0/(32p)),                                 (FU8)

one has `M_beta(P)<=p`, `M_beta(Rcal)<=r`,
`B_beta(P)<=n_R p`, `B_beta(Rcal)<=n_R r`, and
`M_beta(D)<=d_core`, `B_beta(D)<=n_R d_core`. The marked estimates use
<=J labels per mark and <=n_R rows per patch before summing. The constants
p and the numerator of r are independent of R because w=exp(1), so the
choice is possible. An operator bound alone would not supply these sums.

For products, consecutive supports meet at the summed scalar index, and

    M_beta(AB)<=M_beta(A)M_beta(B),
    B_beta(AB)<=B_beta(A)M_beta(B)+M_beta(A)B_beta(B).       (FU9)

The second term requires the column bound of A. Apply this to the ordered
series `K^-1=P sum_(j>=0)Rcal^j`. Symmetrize each j>=1 path product with
its transpose; the exact sum K^-1-P is already symmetric. This preserves
the maximum endpoint sum and the full label. Writing E_lift for that
family gives

    G:=K^-1=c0 I+sum_A D_A+sum_l E_lift,l,
    M_beta(E_lift)<=e_lift:=p r/(1-r)<=c0/16,
    B_beta(E_lift)<=b_lift:=n_R p[r/(1-r)+r/(1-r)^2].       (FU10)

At complex V the large local component need not be positive. The exact
resolvent difference and the inverse endpoint sums give

    M_0({D_A(V)-D_A(Vbar)})<=J g_inv^2 J_abs max||v||.

Reduce a fixed radius eta_PC so this is <c0/8 on `max||v||<eta_PC`.
The local core at Vbar is positive, so independently weakening its whole
components by real factors in [0,1] and E_lift by modulus-one factors
leaves accretivity >=13c0/16. This rebuilds the PC input, including its
complex distinction. Every local formula is on the projected tube and
agrees on overlapping centers because it uses the actual V readers.

Assign c0 I's scalar diagonal entries singleton owner labels. The full
matrix-atom norm needed for the nonlinear fixed point is the finite,
generally very large number

    m_G=c0 exp(beta)+d_core+e_lift,
    b_G=n0 c0 exp(beta)+n_R d_core+b_lift,
    A_G=m_G+b_G,              Q_beta(G)<=A_G.              (FU11)

No smallness of A_G is asserted. It is paid by the following choices of
field, curvature, coarse and source radii. This rate beta is the one used
throughout the new construction; no larger SA/FR box rate is substituted.

## 4. Complete-reader force and nonlinear composition

For vector atoms h_i;S let V_beta(h) be the maximum of their component
root sum and full marked-incidence sum, both weighted by exp(beta|S|)
and with coefficient suprema inside. Multiplication satisfies

    V_beta(Ah)<=Q_beta(A)V_beta(h).                        (FU12)

For a mark in A use its marked sum and the component sum of h; for a mark
in h use A's column sum and h's marked sum. These estimates also define a
complete normed space of absolutely summable holomorphic atom families,
with products grouped by support union. The functions of original data
are bounded on their projected product domains. Uniform limits preserve
holomorphy and locality. Pointwise evaluation is a continuous map from
this space; stationarity below is a pointwise matrix identity.

Give each local phase vertex its radius-four reader label, including its
original Wilson source when present. The safe finite counts are

    s0=9^4, v0=9L^4+5, d0=v0*9^4, d1=q d0, d2=q^2 d0,
    f(t)=H(1-t/a)^(-q), S(t)=f'(t)-f'(0)-t f''(0),
    N(t)=d1 exp(beta s0)[S(t)+t S'(t)],
    B_src=2d2 exp(beta s0) f''(0),
    D_H(t,rho)=2d2 exp(beta s0){f''(t)-f''(0)+t f'''(t)
                              +rho[f''(t)+t f'''(t)]}.    (FU13)

There are 6L^4 Wilson, 4 kernel and m0 Haar vertices per block. A given
mark meets <=d0 root vertices; d1,d2 also pay all scalar force outputs and
ordered Hessian endpoints. These loose counts include all colours and
periodic incidences. They are in original-block units.

Let `delta_hat=delta_*+8eta`. Telescoping the four perturbed coarse-link
factors gives `||I-V_P||<=delta_hat` on FU3 when eta<=1/100; inverse
factors and transported insertions have bounded norms there. Differentiating
a Wilson trace pairs a traceless insertion with P-I or P^-1-I, so a safe
bound per scalar insertion is `4sqrt(N)delta_hat`.

The kernel force is zero **separately at every mean** even at complex V:
all contours agree at V_c, their averaged first variation is a common
SL(N,C) tangent, the numerator trace derivative is zero, and compact Haar
invariance makes the normalizer constant along real common-path tangents.
Its holomorphic continuation gives zero on their complex span. The Haar
logarithm has zero first derivative at zero. Thus, with

    g=F_epsilon'(0), H_epsilon=sum_p epsilon_p W_p''(0),
    g_*=4sqrt(N)d1 exp(beta s0),
    V_beta(g)<=g_*(1+rho)delta_hat,
    Q_beta(H_epsilon)<=rho B_src,                         (FU14)

there is no spurious O(rho) force independent of curvature. At a real V
the same bound holds with its actual delta_V instead of delta_hat. At
exactly flat complex V the force is exactly zero, including nontrivial
compatible holonomies and arbitrary sources in the admitted disc.

The fixed-point decomposition must retain the **linear source Hessian**:

    F_epsilon'(a)=g+K a+H_epsilon a+N_0(a)+N_epsilon(a),
    N_0=F_0'(a)-F_0'(0)-K a,
    N_epsilon=sum_p epsilon_p[W_p'(a)-W_p'(0)-W_p''(0)a].   (FU15)

Only N_0 and N_epsilon start at quadratic order. With K=F_0''(0), dropping
H_epsilon a is not the critical-point equation for the actual source.

Expand each local vertex first in the fine coordinates at zero. Cauchy
bounds its degree-j coefficients by H a^(-j), with the q-slot monomial
count summed by f. Substituting vector atoms of norm <=t attaches each
factor at a slot in the root label, so every union stays connected. A mark
at the root costs S(t); a mark in an attached field costs tS'(t).
Consequently

    V_beta(N_0(a)+N_epsilon(a))<=(1+rho)N(t),
    V_beta(N_0(a)-N_0(a')+N_epsilon(a)-N_epsilon(a'))
       <=(1+rho)N'(t)V_beta(a-a'),
    Q_beta(F_epsilon''(a)-K)<=D_H(t,rho).                 (FU16)

The difference bound follows by telescoping one substituted factor, then
marking; differentiating the positive scalar majorant counts both choices.
The Hessian majorant uses two root endpoints and either a root mark or one
attached mark, explaining f'' and t f'''. All source and coarse coefficients
retain their original labels. No solved field is treated as new independent
data. The same direct local Taylor count, without attached marks, bounds
the ordinary pointwise Hessian row/column norm for any scalar field with
max_i|a_i|<=t. This latter fact is used for local convexity, not inferred
by assigning an arbitrary pointwise field a small marked vector norm.

## 5. Nonempty choices and the joint actual critical field

Define the target Hessian budget

    d_* = min(gamma/4,1/(4m_G),c0/(32m_G^2)).              (FU17)

Choose tau>0 and then rho>0 such that

    tau<min(a/8,r_CB/(4sqrt(D))),
    A_G[rho B_src+(1+rho)N'(tau)]<=1/4,
    D_H(tau,rho)<=d_*.                                   (FU18)

Here r_CB is the real/complex pointwise uniqueness radius in CB. These
choices are possible because N'(0)=D_H(0,0)=0. If a specified auxiliary
chart must contain the center, tau can also be made smaller than its
radius divided by 4sqrt(D). This is an auxiliary choice, not a change to
G, Omega or the original cut.

Retain rho below the previously admitted SA/CB source radii; it may also
be reduced below FR's fixed source radius. Finally choose positive
`delta_*<=min(delta0,delta_CB,delta_A)` and
`eta<min(eta_PC,rho_CB,V)` so that

    delta_hat=delta_*+8eta<=min(delta_CB/2,delta_A),
    A_G g_*(1+rho)delta_hat<=tau/4.                        (FU19)

To compare with a particular IC tube, additionally reduce its real-center
curvature and eta to that tube's positive bounds. Every radius remains
positive and independent of u,T,p. All atom norms, including the possibly
large A_G, are fixed before these final choices. No delta<=sigma p condition
has been used for critical-field existence.

On the V_beta ball of radius tau, iterate from a_0=0 using

    a_(j+1)=-G[g+H_epsilon a_j+N_0(a_j)+N_epsilon(a_j)].  (FU20)

FU12--FU19 give contraction constant <=1/4, and the image norm is at most
tau/4+tau/4=tau/2. The space is complete: the weighted l1 coefficient sums
are complete, and bounded holomorphic functions on each projected open
domain are complete in their sup norm. The iterations therefore converge
uniformly to connected complete-reader atoms a_* satisfying

    F_epsilon'(a_*;V)=0,
    V_beta(a_*)<=2 A_G g_*(1+rho)delta_hat.                (FU21)

All original coarse and source variables occur in the same product domain
FU3. Uniform convergence proves their joint holomorphy. The formulas depend
on actual V,epsilon; changing the reference center on an overlapping tube
does not change the iteration or its limit. At exactly flat complex V,
a_*=0 since the initial force vanishes. For real data the field is real.

The ordinary scalar sup-norm map has the same contraction bound by the
unmarked local estimates. Thus a_* is unique in that small complex cube.
For real V and real epsilon, the pointwise Hessian estimate after FU16 and
FU17 gives throughout the real cube

    F_epsilon''(a;V)>=3gamma/4 I.                         (FU22)

It is therefore the unique local minimum of the smooth coordinate-density
action there. This is neither a global minimum on the compact configuration
space nor a statement that the center lies in a required good event.
The cube lies inside CB's HS uniqueness ball. On real V, the field is
precisely SA13's b(V,epsilon), by that already proved pointwise uniqueness;
at epsilon=0 on an admitted IC tube and its stated u-domain it is IC12's
b_u. The field's real and source-free existence are reused results, now
with a checked joint domain
and the reader rate needed by the covariance extension.

There is also a useful source-difference estimate, not a new replacement
for SA23. Put b_0=a_*(V,0). Subtract FU20 at the same V. The difference of
the maps evaluated at b_0 is bounded by
`A_G rho[g_*delta_hat+B_src V_beta(b_0)+N(V_beta(b_0))]`.
Using the contraction bound and `N(t)<=N'(tau)t` yields

    V_beta(a_*(V,epsilon)-b_0)<=C_src rho delta_hat,
    C_src=2A_G g_*[1+2A_G(B_src+N'(tau))].                 (FU23)

On real V replace delta_hat by delta_V. At real zero curvature it vanishes
exactly. The Hessian source term need not vanish there: critical covariance
can still change at flat V when original Wilson coefficients change.

## 6. Critical-Hessian covariance with the lift core unchanged

Set

    K_*=F_epsilon''(a_*;V)=K+Delta,
    Q_beta(Delta)<=d_H:=D_H(tau,rho)<=d_*.                 (FU24)

FU16 proves this for the actual finite-t/Haar/source Hessian. Each atom
contains both Hessian endpoints, its root vertex, every substituted
critical-field reader and the original source labels. K_* is still local
in its **field indices**, but its entries generally read distant original
data through a_*. Principal compressions of K_* would not be local
coefficient functions of their patches. We do not use them as the positive
local core.

Instead retain D_A from FU7 and expand around the full lift inverse G:

    K_*^-1=G(I+Delta G)^-1,
    T_crit=sum_(j>=1) G(-Delta G)^j,
    K_*^-1=G+T_crit.                                     (FU25)

The displayed order follows from `(K+Delta)G=I+Delta G`. Expand every
factor into its complete-reader atoms. Consecutive labels meet at their
summed index; union labels are connected. Symmetrize each product with
its transpose; the exact total K_*^-1-G is symmetric.

Put `h=d_H m_G`, `b_h=d_H(m_G+b_G)`. FU9 gives the quantitative bounds

    h<=1/4,
    M_beta(T_crit)<=t_crit:=m_G h/(1-h)<=c0/16,
    B_beta(T_crit)<=b_G h/(1-h)+m_G b_h/(1-h)^2.            (FU26)

Indeed the first and second budgets of Delta are each <=d_H. The
j-th product has endpoint bound m_G h^j and marked bound
`b_G h^j+j m_G b_h h^(j-1)`. Their two geometric sums prove FU26.
Absolute uniform convergence proves joint holomorphy on the same source
and coarse domain. This family is small in its endpoint norm; its marked
sum is only finite. It is generally nonzero at zero source on curved
backgrounds, so no false source-normalized cancellation is asserted.

For independent real 0<=theta_A<=1 and independent complex factors
|zeta_l|,|xi_j|<=1 define

    C_*=c0 I+sum_A theta_A D_A(V)
                +sum_l zeta_l E_lift,l(V)
                +sum_j xi_j T_crit,j(V,epsilon).          (FU27)

The large local components are the same whole matrices as before, and
only they require nonnegative real weakening. Comparing them to Vbar
costs <c0/8; the two small tails cost at most c0/16 each. Thus

    Re C_* >=3c0/4 I=:alpha_* I,
    ||C_*||op<=U_*:=c0+d_core+e_lift+t_crit,
    Re C_*^-1>=alpha_*/U_*^2 I.                          (FU28)

Here alpha_* is a scalar accretivity constant, distinct from the vector
critical field a_*(V,epsilon). The precision identity is
`Re C_*^-1=C_*^{-*}(Re C_*)C_*^-1`, followed by
`||x||<=U_*||C_*^-1 x||`. At all weakening factors one, C_*=K_*^-1.
For real parameters and real residual factors it is a positive real
covariance. The actual real K_* is >=3gamma/4, while the complex K_*
has Hermitian part >=gamma/2 by FU4/FU24. These are different statements
from the interpolated covariance bound.

Attach to each complete label a geometry-only spanning-tree monomial in
bond parameters in [0,1], exactly as in PC. All FU27 bounds continue to
hold. If all bonds crossing a partition of coarse cells vanish, every
atom whose **reader label** crosses that partition vanishes, including a
diagonal covariance atom with remote readers. Every surviving covariance
block depends only on original V and epsilon readers in its own part.
The full normalized Gaussian factors by those parts: its density is
`(2pi)^(-d/2) exp[-Tr Log C_*/2-x^T C_*^-1 x/2]`, and the principal
matrix logarithm, determinant and quadratic form are direct sums.
The accretive branch is fixed by continuation from real positive matrices.
This is Gaussian endpoint factorization, not factorization of the actual
interacting law or of an unchanged hard-history indicator.

## 7. Centered identity and remaining consumer obligations

At the physical, undeformed endpoint the pointwise Taylor identity is

    F_epsilon(a_*+sigma x)=F_epsilon(a_*)
                       +(sigma^2/2)x^T K_* x+sigma^2 R_*(x),
    R_*(x)=sigma^(-2)[F_epsilon(a_*+sigma x)-F_epsilon(a_*)]
                                       -x^T K_* x/2.      (FU29)

On `max_i|sigma x_i|+V_beta(a_*)<a`, this exact remainder equals the
convergent series `sum_(j>=3) sigma^(j-2)F_epsilon^(j)(a_*)[x^j]/j!`.
There is no linear remainder because FU21 is actual stationarity. Individual
local phase vertices need not be stationary. The difference identity is
holomorphic wherever the full affine field stays in the proved local chart;
the series is asserted only with the displayed common margin. It does not
assert that a center or covariance obtained by independently weakening
atoms is stationary for a separately weakened nonlinear phase.

For real V,epsilon and a fixed auxiliary product chart D_a inside the proved
fine chart in original a coordinates, on which the original cut is
automatic as in PS, the raw
chart integral has the exact ordinary real-translation formula

    Z_a=h_N^n(2pi sigma^2)^(d/2) det(K_*)^(-1/2)
           exp[-F_epsilon(a_*)/sigma^2]
           integral_((D_a-a_*)/sigma) dmu_(K_*^-1)(x)
                                                   exp[-R_*(x)]. (FU30)

The original chart is translated, not replaced by a centered ball. The
full finite-u critical action, compact normalizer, Haar constant and full
d-dimensional determinant remain. At complex source the corresponding
shift is a complex contour operation with boundaries; FU30 is not a
permission to replace it by a real Gaussian integral. An unchanged hard
history remains an additional exact reader. No new estimate for that
contour or history follows from stationarity alone.

SA/FR retain an unscaled source-critical-action budget
O(rho delta_V^2/sigma^2) on their stated real-coarse domain, hence
O(rho p^2) on their selected window. Neither this action nor
the interacting determinant/reference normalization has been canceled
here. The current chart-boundary author's unfinished argument is not used
as a premise. Both exact complementary pieces outside the selected sector,
and any additional chart complement, remain in the original integral.

The new rate is only beta=(16R)^(-4) in original blocks. Products above
preserve it; a fixed-order derivative can spend a smaller margin beta-beta'
as in PC, with its full coefficient chain rule. This supplies no unchanged
RD consumer with its two-unit weight cost, nor FR's eight-unit box margin.
Any regrouping, norm conversion or smaller-margin cluster proof must be
performed explicitly. No all-order Gaussian/interacting derivative tree,
hard surface, corner trace or reference cancellation has been summed.
The new precision coefficient is alpha_*/U_*^2; a combined nonlinear
regulator must choose its auxiliary/source radii against that coefficient,
not reuse PS's gamma unchanged.

Still open are the full probability-sensitive return expansion, arbitrary
histories and effective-level identification, complex nonvanishing of the
original cut transform, multiscale iteration, continuum existence and the
physical continuum mass gap. This is a positive bounded extension, not a
no-go or an exhaustion statement.

## 8. Provenance and review boundary

Bałaban's constructions and Dimock's expositions are the architectural
antecedents. This unit rebuilds the used local inverse, marked-composition,
contraction and resolvent steps from the actual source formulas; no new
external theorem import or numerical experiment is needed. The SA, FR,
IC and PC results are credited at their exact scopes rather than renamed
as discoveries. Their frozen bytes and the entire PC/PS author packets
remain unchanged.

The new mathematical source is frozen before its author check/read packet
is packaged. The packet records exact input hashes, bounded read coverage,
reused same-revision methodology and the protected packets. Requested
Astra/max is not independent backend attestation. A fresh hostile review
must examine this unit's joint-domain and critical-tail argument. The
coordinator owns PR #10114 integration, shared fronts, Git and audit gates;
this author performs none of those operations. No author-issued LAND or
retained-grade status is supplied.
