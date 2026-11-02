# The source-zero bare marginal remainder

The actual bare original-cut integral, divided by its full finite-u critical
prefactor, has an infrared quadratic marginal of order O(1/u). The proof uses
the existing centered product-HS-ball expansion, its exact original-chart
side/corner formula, and the actual real compact-return jets. In particular,
a centered reference can have a fixed coarse analytic domain even though the
comparison with the original chart has a shrinking domain. An auxiliary
boundary fugacity keeps that comparison logarithm rare after differentiation.

This is a one-step, original-source-zero statement. The full critical action,
Haar term, determinant and normalized-kernel vacuum remain in the prefactor.
No coefficient or sign of a one-loop term is evaluated. The concurrent
[bare coupling matching unit](BARE_COUPLING_MATCH_ASTRA.md) is under separate
review and none of its new conclusions is a premise here. Inherited-class
closure, iteration, non-freeness, continuum existence and a positive physical
continuum mass gap remain **OPEN**.

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

## 1. Exact integral and common prefactor

Fix N>=2, D=N^2-1, odd L>=3, a coarse torus of side T>=2, and kappa in its
admitted positive compact interval. Kappa stays fixed as u increases. Set

    sigma^2=N/u, m0=3L^4+1, n=m0 T^4, d=Dn.

Use the original pinned internal trees, CB's lift U0(V), internal links I
and outgoing crossing-face links V_c. The tree quotient has gauge volume
and Jacobian one. All free whole links, colours, crossing, root and harmonic
coordinates remain. The T=2 lifted-seam convention changes no integration
mode. In HS coordinates, -tr(T_alpha T_beta)=delta_alpha,beta, write
U_e=exp(a_e)U0_e(V). All original Wilson sources are identically zero.
The actual probability-Haar density and its local holomorphic continuation are

    w_0(U,V)=exp[-u sum_p s(U_p)] product_c k_(kappa u)(V_c;M_c(U)),
    s(W)=tr(2I-W-W^-1)/(2N),
    k_t(V;M)= exp{t tr(V^-1 M^+ + M^- V)/(2N)}/Z_t(M),
    Z_t(M)=int_SU(N) exp{t tr(W^-1 M^+ + M^- W)/(2N)}dW.    (BR1)

M^+ averages the actual 24L^4 paired contour words and M^- their inverses.
They are not inverse matrices. On real inputs Z_t is its positive compact
integral. On small complex inputs it uses the checked CB/FU local branch;
no rough complex mean is needed here. The equivalent exp[-t(1-...)] numerator
and normalizer have their constants canceled exactly, not discarded.

Let chi_cut be the ORIGINAL block-interior plaquette cut. Define

    Z_cut,T(V)=int chi_cut(U) w_0(U,V) dHaar(U),
    F_u(a;V)=sigma^2[-log w_0(exp(a)U0(V),V)-sum_e log j_N(a_e)],
    F_u'(b_u;V)=0, K_u=F_u''(b_u;V), C_u=K_u^-1,
    P_u,T(V)=h_N^n(2pi sigma^2)^(d/2)
                   exp[-F_u(b_u;V)/sigma^2-(1/2)TrLog K_u]. (BR2)

Here dHaar(exp a)=h_N j_N(a)da. C_u denotes the covariance, not its square
root. The accretive trace-log branch is fixed from positive real K_u.
These definitions are FU1/FU21/FU24/FU30 and NR1/NR37. They do not use a
classical replacement Hessian. Every normalized-kernel, Haar and vacuum
term occurs once, with the full d-dimensional determinant.

The original-a chart, at the actual physical coarse argument V, is

    Z_a,T(V)=h_N^n int_(product_e B_(r_a)^D)
                                      exp[-F_u(a;V)/sigma^2] da. (BR3)

For real V this is a genuine physical chart; for complex V it is the
transported holomorphic top-form contour. BW2 identifies it with WR39's
transported whole-region chart, including the restored empty-field-stencil
factors. On the common real domain all critical branches solve this same
F_u'=0 in the same uniqueness cube. Thus their b_u, K_u and P_u coincide.
This identifies actual finite-dimensional objects, without identifying
unrelated covariance atom expansions by their bounds.

The main quantity is the real logarithm

    R_u,T(V)=log[Z_cut,T(V)/P_u,T(V)].                       (BR4)

It is not normalized to vanish at V=I. All scalar Gaussian and truncated
Gaussian vacuum contributions remain until the marginal derivative kills
field-independent terms.

## 2. Fixed choices, shrinking parameters and precise inputs

The mathematical suppliers are [FU](FINITE_U_CRITICAL_FIELD_ASTRA.md),
[NR](NONLINEAR_READER_RETURN_ASTRA.md),
[SN](SHIFTED_NONLINEAR_READER_RETURN_ASTRA.md),
[SH](SHRINKING_CHART_RETURN_ASTRA.md),
[WR](WEIGHTED_RETURN_JETS_ASTRA.md), and BW2's literal-object identification.
Their review descriptions are not premises. The changed parameter order
and the boundary-fugacity step are proved below.

First choose ONE common FU/NR/SN cover, its geometry-only patch/order rules,
strict principal-core and two-tail margins, and preliminary analytic ceilings.
Keep its R, beta=(16R)^-4, a>0, L_hat, B_E, h_c and all marked constants fixed.
NR6 requires the actual total covariance tail to have endpoint norm at most
min(c0/8,1/(4v_I),a/(64v_I^2)); its reader-marked norm B_E need only be finite.
The two tails are E_lift and T_crit. No critical-Hessian principal compression
is substituted for the actual local lift core.

Choose fixed positive bar_tau, r_max and rho0 so that bar_tau+r_max is inside
the common fine chart, NR12 and SN10 hold at r_max, and FU18--FU19 give its
actual critical branch on

    D0={V_c=exp(v_c): max_c ||v_c||HS<rho0}.                (BR5)

One can keep a fixed original-source disc rho while making these choices,
then evaluate at source zero. FU19 uses delta_hat=8rho0 about I and permits
rho0>0 independent of u,T. In particular b_u and the full covariance atom
library are analytic on D0. This assertion is about the small-field phase
and a centered auxiliary contour, not about Z_cut on D0.

Next choose the positive constants of WR34, with any extra reductions
required by SH1. Use its source-zero family

    p=p_a=log(2+u)^alpha, alpha>5/2, r_a=sigma p,
    q=c_q sigma^2 p^2, K=K(q)=O(log u),
    delta(u)=d_delta sqrt(q)/(4K+1)^2,
    xi(u)=d_xi sqrt(q)/(4K+1)^2.                          (BR6)

They are chosen with WR's genuine cap/buffer margins. On the product coarse
tube of radius xi about I, the SAME FU iteration has norm at most tau=c r_a,
where c>0 satisfies SH1. Restriction and re-estimation of its convergent
atoms do not change the critical solution or its coefficients. Explicitly,
FU21 gives ||b_u||_v<=16 A_G g_*(1+rho)xi, and xi/r_a=O(K^-2).
Consequently, for sufficiently large u,

    D tau<=r_a/16,
    (L_hat^2+2 eta_bar)(D tau)^2<=a r_a^2/64,
    r_a+2D tau<a_f, xi<rho0/2, r_a<r_max, r_a<=epsilon_1/8. (BR7)

These are the actual side-sweep margins. The first displayed inequality
follows from SH1's stronger tau<=r_a/(16D). No fixed-domain critical shift
is assumed smaller than r_a away from the shrinking tube. Because U0 is I
on internal links, the original interior plaquette defect on BR3 is at
most 4r_a<epsilon_1. Thus its original cut is automatic, as in SC section 1 after SC3.

All choices precede a volume-independent large-u threshold. The final
reader rate is gamma=min(beta/2,gamma_WR)>0, where gamma_WR is WR38's
actual original-block rate. If the libraries use the same R this is beta/2.
Taking a minimum changes neither library nor its original readers. No
macro-cell relabeling or promotion to an exp[(mu+2)|Y|] norm occurs.

The existing derivative contracts consumed here are as follows.

* NR's covariance, nonlinear and even-vertex constants are uniform on D0.
  Only its cutoff/regulator parameters will be re-estimated in section 3.
* SN12 is an exact finite-volume side/corner identity with the same b_u,C_u.
  SN22--SN27 pay every side root and every Gaussian translation reader.
* WR38 bounds the ACTUAL moving-center, fully integrated compact-return
  coefficients and their real ordered (6,4) jets. WR40 identifies their
  logarithm with log(Z_cut/Z_a) on this real family.

The last item is stronger than a value bound on separately centered
coefficients. Its proof uses the real all-link Haar pullback, fixed selectors
in those variables, real positive-normalizer jets, and a finite multiaffine
replacement whose jets equal the actual integral's jets before applying the
same density-only forest. That is the specific supplier reused here.

## 3. Centered balls on a fixed coarse domain

For each u use the genuinely auxiliary contour a=b_u+sigma z with

    D_p=product_e {||z_e||HS<p},
    R_v(z)=sigma^-2[F_v(b_u+sigma z)-F_v(b_u)
             -sigma F_v'(b_u)z-(sigma^2/2)F_v''(b_u)[z,z]],
    J_cent(V)=int_(D_p) g_(C_u)(z) exp[-sum_v R_v(z)] dz,
    Z_cent(V)=P_u(V) J_cent(V).                           (BR8)

Individual vertices need not be stationary; the summed first derivative is
zero by BR2. The Gaussian is the FULL normalized density with covariance
C_u, including its determinant. Multiplying it by BR2 gives the Jacobian
h_N^n sigma^d of this affine contour exactly. This is an integral identity,
not an inclusion of two cutoff domains.

Here r_a=sigma p decreases but the critical-field ceiling bar_tau and D0
stay fixed. The following verifies the change from NR's fixed-r_a statement.
Its coefficient families W0,W1,E0,E1 are computed at fixed fine/critical
ceilings. NR11's ordinary and even Mayer bounds retain respectively sigma
and sigma^2. Its sole nonlinear cutoff regulator is

    eta_r=2 A d_inc r_a(1+r_a), d_inc=15,

which only decreases below the already chosen bound at r_max. The local
fine arguments obey bar_tau+r_a<bar_tau+r_max<a_f. Thus this argument needs
no bound bar_tau<r_a. The hard-link Gaussian charge is exactly

    q_H=K_g^D 2^(D/2) exp[-a p^2/32].                     (BR9)

NR21's product Gaussian moments M90, the maximum scalar degree 6*15=90,
the active determinant factors, the principal-core inverse bounds, both
covariance tails and all reader-marked constants are unchanged.

For clarity, write the resulting primitive budgets as

    h_v=V1 sigma, h_2=V2 sigma^2,
    h_h=H0 exp[-a p^2/32], h_0=h_v+h_h,
    C0=1+K_m B_E,
    epsilon_0=C0(h_2+h_h)+(C0/h_c+L_hat^2 B_E)h_0^2.       (BR10)

The fixed V1,V2,H0 can be the larger common SN/NR constants. The displayed
L_hat likewise enlarges NR's L_jet. For large u, h_0<=h_c/2 and
 epsilon_0<=beta/16, uniformly on D0. Consequently

    J_cent=exp[sum_Y H_Y^cent],
    ||H^cent||_gamma,D0<=epsilon_0
                         <=C_cent sigma^2+C_tail exp[-a p^2/32]. (BR11)

The norm is sup_x sum_(Y contains x) exp(gamma|Y|) sup|H_Y| over complete
connected original-block readers. It is never a bound on the total log
without its reader labels.

The parity reason is coefficientwise. Every zero-side normalized Gaussian
density-list term is even under z->-z, and each link ball is symmetric.
For one nonlinear primitive the odd Mayer part therefore integrates to
zero at EACH complete reader, for every V in D0 at the fixed u. NR11's even
bound is sigma^2 times an integrated fourth/sixth Gaussian moment. Species
with at least two ordinary primitives have degree at least two: multiplying
only their amplitudes by h_c/h_0 in the positive counting bound and undoing
the multiplier gives the second term of BR10. No primitive-free residual
vacuum exists, because the empty normalized Gaussian marginal is one.

The density-only forest retains product_i sqrt(nu_i!), not a factorial of
all legs. Its per-coordinate child sums are H0(y)<=exp(2y) and
H1(y)<=exp(4y) for y<=1/2 (NR28--NR30), with exponent linear in the active
reader size. Marks in density loops/chains cost K_m B_E and a marked tree
edge costs L_hat^2 B_E h_0^2. The two reader regroupings then spend their
actual beta/8 margins. These explicit inequalities, not a threshold depending
on a formerly fixed r_a, establish BR11 for the family BR6.

No white-coordinate change is made in BR8. At real V, writing
z=K_u^-1/2 w would turn D_p into a coupled moving body in w. It is not the
supplied original scalar cube Omega. That cube and its fractional-whitening
readers are not replaced or used in this proof. The necessary covariance
readers here are the actual NR two-tail readers, and the full determinant
is retained. In particular no factor z_p^d from a different Gaussian
truncation is silently canceled. The Gaussian truncation contribution in
BR8 remains in its hard-link primitives, even when it depends on V.

## 4. Exact boundary fugacity and a rare comparison logarithm

Restrict only this comparison to the xi tube. Fix the SAME atom, component,
scalar ordering and regrouping rules as in BR8. Put m=b_u/sigma. Let H be
a subset of free whole links, let t_e in [0,1] for e in H, and let m_H
vanish off H. SN12 gives the following finite polynomial in a new scalar zeta:

    J_zeta(V)=sum_(H subset free links) (-zeta)^|H|
       int_[0,1]^H int_(product_(e in H) sphere_p^D
                        times product_(e not in H) B_p^D)
         [product_(e in H) (m_e . n_e)]
         g_(C_u)(y-t m_H) product_v exp[-R_v(y-t m_H)] dS dy dt,
    J_0=J_cent,                 J_1=Z_a/P_u.              (BR12)

The dot product is bilinear, not conjugate-linear. This is the actual
translated top-form identity, with all faces and corners. The translations
have Jacobian one; all nonlinear Haar densities stay in F_u. The new zeta
is a bookkeeping parameter on actual side fluxes, not a physical source
or a datum requiring a volume-sized reader.

The exact primitive expansion consists of nonlinear vertices, remaining
volume-link failures, and side fluxes. Each original vertex and link is
selected at most once. For a vertex v its side pattern is exactly H intersect
its field stencil, and the same t_e is retained wherever that side occurs.
Incompatible hard failures vanish. The full active Gaussian marginal is
C_u[I], with its normalized determinant and both tails. The forest acts only
on that density, never on a normal, side parameter, hard predicate or vertex.
Each side primitive contributes ONE factor zeta throughout this construction.

At zeta=0 every side disappears. The surviving nonlinear functions are
precisely NR's centered functions, including their cutoffs and parity
coefficients. The active sets, core components, density lists, scalar forests
and connected-reader regroupings then equal those of BR11 coefficient by
coefficient. This is a common canonical library, not equality inferred from
two total integral bounds. All critical-field, local, normalizer, covariance,
translation and boundary readers are retained before taking their union.

Here are the actual side budgets from SH3, included to check the amplification.
With E_c=exp(beta s_c), Q0=A_D 2^(D/2)omega_D and fixed d_h, they are

    h_s=Q0 E_c c(1+d_h D) p^D(1+Dcp)^(90D) exp[-a p^2/64],
    h_tr=Q0 E_c L_hat D c^2 p^(D+1)
               (1+sqrt(2)L_hat Dcp)(1+Dcp)^(90D) exp[-a p^2/64],
    epsilon_s=2(C0+L_hat^2 B_E h_c)h_s+h_tr.              (BR13)

In particular h_s+h_tr<=C(1+p^(91D+2)) exp[-a p^2/64].
There is no hidden inverse sigma: the surface charge is proportional to
sigma^-1 p^(D-1) and its flux supplies tau=c sigma p. The extra Gaussian
translation mark has one more sigma^-1 but its distinguished side root
supplies D tau^2 (SN24). This explains the second displayed charge.

Multiplying each side flux by zeta multiplies h_s and h_tr by |zeta|.
The latter remains linear because its marked root is itself a side primitive;
the translated-field readers do not create a side-free term. All Gaussian
scalar-factorial, normal, surface and corner bounds are otherwise unchanged.
SN26 treats the no-side species by BR10. SN27's rescaling of only side
amplitudes gives, for the entire side-containing raw family, |zeta|epsilon_s.
This statement retains arbitrary ordinary vertices attached to the sides.

Set

    R_s=exp[a p^2/256], epsilon_hat=epsilon_0+R_s epsilon_s. (BR14)

Since R_s(h_s+h_tr)<=C(1+p^(91D+2))exp[-3a p^2/256], for large u

    R_s>=2, h_0<=h_c/2, R_s h_s<=h_c/2,
    q_H<=1, epsilon_hat<=beta/16.

Thus the actual same Gaussian-tree and reader-overlap estimates converge
uniformly for |zeta|<=R_s. The four beta/8 margins are exactly the existing
SN margins: primitive components, scalar attachments, complete-reader
regrouping and the connected logarithm. No new growing order factorial is
introduced by zeta, since it merely counts side primitives.

The resulting holomorphic coefficient family satisfies

    J_zeta=exp[sum_Y H_Y(zeta)],
    ||H(zeta)||_(beta/2)<=epsilon_hat, |zeta|<=R_s,
    H_Y(0)=H_Y^cent.                                     (BR15)

As in SN29, the equality is first the finite-activity graph identity, then
extends to unit activity by its absolutely convergent series. Finite atom
and list truncations and the positive majorants justify the limits. This
also proves nonvanishing before a logarithm is assigned, on the entire
zeta disc and the xi coarse tube. The finite-volume polynomial BR12 is
not assumed nonzero merely because it is close in a volume-dependent norm.

Cauchy's formula, applied coefficientwise on that disc, gives

    Delta_Y=H_Y(1)-H_Y(0),
    ||Delta||_(gamma,xi)<=epsilon_hat/(R_s-1)
                  <=(beta/8) exp[-a p^2/256]=:A_side,
    log(Z_a/Z_cent)=sum_Y Delta_Y.                       (BR16)

Indeed the k-th zeta coefficient has norm at most epsilon_hat R_s^-k;
summing k>=1 proves the bound. These terms have at least one actual side
primitive. This is the rare bound for the connected comparison log, not
subtraction of two extensive actions. At real data the branches are the
real logarithms of positive chart integrals and agree with BR15.

## 5. The actual compact complement and real unscaled jets

Use WR38 with h=sqrt(N) and all original absolute-source weights r_p=1,
then evaluate at J=0. These are allowed fixed polynomial bounds in u. Its
actual coefficients Psi_Y^diag have

    log(Z_cut/Z_a)=sum_Y Psi_Y^diag,
    sup_x sum_(Y contains x) exp(gamma|Y|)
            sup_real T_(sqrt(N),1)^(6,4)(Psi_Y^diag)
               <=exp[-kappa_d p^2]=:A_comp,
    kappa_d=c N c_q/64>0.                                (BR17)

The norm is WR1's sum of ordered invariant derivatives divided by m!n!,
with dense max-link operator-norm field directions and the actual original
source directions. Positivity in its rough-normalizer proof is used at
REAL source and REAL physical coarse arguments. No complex coarse extension
of the compact numerator, nor differentiation of a hard selector, follows
from BR17 or is required here.

The equality is WR40's actual real open-domain family. Its original source
convention remains J_p=u epsilon_p with u and every kernel fixed; this unit
sets J=0 and takes no source derivatives. All original source labels remain
in the complete-reader labels. No selected-history coefficient is differentiated
by inference from its value. WR's real moving-center jet construction supplies
the derivative of the actual family rather than a fixed-center partial jet.

Combining the exact real identities gives

    R_u,T=sum_Y [H_Y^cent+Delta_Y+Psi_Y^diag].              (BR18)

The full P_u cancels by its single definition BR2. This is an identity of
fully integrated bare functions. It asserts neither fine/exterior derivative
control nor conditional regional compact denominators.

## 6. Unscaled Hessians and every second spatial moment

Let E_alpha=sqrt(N)T_alpha be a FLOW-orthonormal colour basis. Thus a unit
colour H has -tr(H^2)/N=1 and ||H||HS=sqrt(N). Coordinates v_(X,mu)^alpha
are defined by V_(X,mu)=exp(sum_alpha v_(X,mu)^alpha E_alpha).
For i=(X,mu,alpha), j=(Y,nu,beta), use the ordinary Hessian at v=0.
If the indices are on the same link, it equals
( D_i D_j+D_j D_i )/2 at I; on different links the derivatives commute.
This explicitly relates the coordinate Hessian to WR's ordered convention.

For an analytic coefficient f_S on an HS product tube of radius eta,
substitute v_i=sE_alpha and v_j=tE_beta (their sum when on the same link).
The two circles |s|=|t|=eta/(4sqrt(N)) lie in its half tube. Therefore

    |partial_i partial_j f_S(I)|<=16N eta^-2 sup|f_S|.     (BR19)

Repeated directions use two distinct scalar parameters and obey the same
bound. No tiny-domain cost is suppressed. A coefficient is differentiated
only through its actual original readers. For the real Psi coefficients,
BR17 and 1/2! in WR1 give |partial_i partial_j Psi_S(I)|<=2 a_S^comp,
where the common positive envelopes have gamma norm at most A_comp.
The symmetrization just stated proves this even if an individual coefficient
has a nonzero first jet.

Write d_T(X,Y) for periodic coarse l1 distance and set theta=gamma/16.
For the Hessian of a full function define

    M_(2,theta,T)(F)=sup_i sum_j (1+d_T(X_i,X_j))^2
          exp(theta d_T(X_i,X_j)) |partial_i partial_j F(I)|. (BR20)

The same column bound follows from Hessian symmetry. If S is a connected
reader of s original blocks containing X_i, it reads at most 4D s coarse
scalar coordinates. Its input-owner distances satisfy 1+d_T<=8s; this
generous bound also covers the collar/endpoint conventions and corners.
Thus the analytic contribution of this S is at most

    2^12 N D eta^-2 s^3 exp(gamma s/2) sup|f_S|.

The elementary maximum bound s^3<=6(gamma/2)^-3 exp(gamma s/2) pays the
entire second input count and second spatial moment. The analogous real-jet
bound replaces 16N eta^-2 by 2. With the safe constant
C_m=2^20 N D gamma^-3, BR11, BR16--BR19 prove uniformly in T

    M_(2,theta,T)(R_u,T)
       <=C_m [rho0^-2 A_cent+xi^-2 A_side+A_comp]=:B_u,
    A_cent=C_cent sigma^2+C_tail exp[-a p^2/32].           (BR21)

This bound includes an exponential spatial margin. Every mark and input
multiplicity was paid on original readers; no total-volume estimate was
renamed local. For a unit colour H, the row and column bounds also control
the colour-contracted quadratic form by the elementary Schur inequality.

In particular the domain cost for the side term is exactly

    xi^-2=u(4K+1)^4/(N d_xi^2 c_q p^2).                  (BR22)

Consequently, for fixed constants independent of u,T and c0'>0,

    B_u<=C/u+C[1+u(4K+1)^4/p^2]exp[-c0' p^2]
        <=C/u+C' exp[-c_* p^2],
    c0'=min(a/256,kappa_d), c_*=c0'/2>0,                 (BR23)

after increasing the threshold. The last step uses log u+O(log log u)=o(p^2).
The separate compact estimate required alpha>5/2 already in BR6. No relation
to a next-scale coupling or field weight is used.

For comparison, WR39's chart bound alone, with its actual xi Cauchy cost,
gives sigma^2 xi^-2=O(K^4/p^2)=o(1). It already supplies a weaker marginal
estimate after the same reader counting. Its collapsed h=O(sigma) norm
alone would not do so. The fixed-domain centered parity bound and the rare
side comparison are what improve that estimate to BR23.

## 7. Volume first, Ward identity and marginal extraction

The infinite-volume object here is a local Hessian kernel, not an extensive
limit of R_u,T. At each fixed u, choose the same geometry-only atom and
ordering rules on growing tori, agreeing with a fixed infinite-lattice rule
near any fixed finite patch. The R-box partitions can have sides R to 2R;
put the finitely many adjustments needed to close a torus at its far seam.
The WR buffers have finite radius K(u) at this stage. All local phase words,
tree choices, cut labels, collars, normalizer atoms and memberships agree
on a reader that misses that seam. FU's canonical iteration and the explicit
NR/SN/WR coefficient formulas then agree there term by term.

Any differing or winding reader through a fixed input must reach that seam,
and so contains a number of original blocks proportional to its distance.
The same BR21 counting, retaining a smaller fraction of its exponential
margin, bounds the corresponding Hessian row tails by C(u)exp(-c gamma T).
For each fixed u this tends to zero. It proves existence and independence
of the local thermodynamic limit, with its second spatial moment and a
remaining exponential moment. All finite-T harmonic modes were present
before this limit; no finite-torus zero-mode deletion is used.

BR1, chi_cut, the repeated block lift/tree rule and BR2 are invariant under
coarse translations and real coarse root gauges. To check the latter, extend
g_X constantly within each fine block. It preserves the internal tree and
maps a_e to Ad_(g_(X_e))a_e. The Haar density and HS metric are invariant,
and F_u(Ad_g a;V^g)=F_u(a;V). Uniqueness gives b_u(V^g)=Ad_g b_u(V);
K_u is conjugated by the real orthogonal full-colour Ad_g matrix. Thus P_u
is invariant, including its determinant and every normalization. Z_cut is
invariant by the real fine-Haar change of variables and gauge invariance of
the actual interior cut. It follows that the ACTUAL R_u,T is invariant.
These statements also follow directly for Z_a and Z_cent, but are not
assumed for arbitrary individual reader coefficients.

Global colour conjugation forces the first derivative at I to vanish,
because su(N) has no invariant nonzero linear functional. Differentiating
the coarse gauge identity therefore gives the finite-volume Hessian Ward
identity. Translation invariance passes to the infinite-volume kernel.
Writing its Fourier symbol as Pi_u(P), the exponential moment gives an
analytic symbol and the Ward identity is

    Pi_u(P) d(P)=0, d_mu(P)=exp(iP_mu)-1.

Take P=t e_nu and divide by t before t->0: Pi_u(0)e_nu=0 for every nu.
Hence Pi_u(0)=0. This is a statement after the thermodynamic limit.
Finite-torus holonomy responses are not set to zero by a nonexistent
periodic gauge parameter. Symmetry of the real Hessian implies the scalar
diagonal kernel for a fixed orientation and colour is even under X->-X.

For a FLOW-unit Cartan H and mu!=nu, use the actual coarse links

    V_(X,mu)=exp[epsilon cos(P_T X_nu+vartheta)H],
    V_(X,k)=I for k!=mu,

where P_T is an allowed torus momentum tending to fixed nonzero P. Define

    beta_(mu,nu)[F]=lim_(P->0) (2/lambda(P))
       average_vartheta lim_(T->infinity, P_T->P)
          T^-4 partial_epsilon^2 F_T(V)|_(epsilon=0),
    lambda(P)=4 sin^2(P/2),
    beta_av[F]=(1/12) sum_(mu!=nu) beta_(mu,nu)[F].        (BR24)

This is UL2's volume-first plane-wave normalization, stated explicitly rather
than importing its loop conclusions. The coefficient of epsilon^2 in the
phase-averaged density is Pi_(mu,mu)^H(P e_nu)/4. For the nearest-neighbor
Wilson sum sum_p s(V_p), BR24 is one. Thus these are canonical coarse link
units. A coarse curl is a_c^2 F to leading physical order and a coarse
cell has volume a_c^4; these factors cancel in four dimensions. Restoring
the coarse spacing therefore inserts no extra L in this F^2 coefficient.

The zero constant term and evenness just proved give

    beta_(mu,nu)[R_u]=-(1/2) sum_(Z in Z^4) Z_nu^2
                               H_(mu,mu)^H(Z),
    |beta_av[R_u]|<=B_u/2
                       <=C/u+C' exp[-c_* p^2]=O(1/u).   (BR25)

Absolute second-moment convergence justifies the Taylor limit and all
interchanges. The bounds hold for each ordered transverse plane, so the
average requires no unproved hypercubic symmetry of an auxiliary patch
construction. Identifying a complete marginal tensor with a single scalar
Wilson tensor would require the relevant symmetry/extraction statement;
the present averaged projection does not make the full coarse symbol a
nearest-neighbor symbol. BR25 is the requested source-zero remainder bound.

## 8. Scope, literature and review boundary

BR25 controls log(Z_cut/P_u), including its actual original-cut compact
return. It leaves the full prefactor projection unevaluated. If a separate
prefactor calculation is established, linearity contributes -beta_av[R_u]
to the physical action -log Z_cut. No bare matching, sign or value of b1,
universal running coefficient, repeatable trajectory or inherited law is
inferred here. The result supplies neither all-history extraction bounds
nor the larger native support rates of the effective-class contracts.
Reflection positivity of an extracted continuum theory, non-freeness,
continuum existence and a physical continuum gap are not proved.

Bałaban's constructive localization and Dimock's exposition are the principal
antecedents. The following primary checks were used to identify the required
boundary/parity issues, not to import a theorem across models.

* [Feldman--Knörrer--Trubowitz, Part 3](https://arxiv.org/html/1609.01747v1),
  introduction and the construction around (21)--(25), retains a determinant,
  a displaced contour, and the remaining Stokes boundary pieces for a bosonic
  many-body model on a three-dimensional lattice. Its introduction explicitly
  says that the full small-error proof is not completed. It supplies no
  four-dimensional SU(N) reader estimate; BR12--BR16 use the actual SN library.
* [Dimock, Small Fields](https://arxiv.org/pdf/1108.1335), section 4.6,
  Lemma 21 and Appendix B, Theorem 27, exponentiates localized fluctuations
  for scalar phi^4_3, with its ultralocal probability reference and a specified
  polymer decay threshold. Those hypotheses are not the present correlated
  gauge Gaussian and small original-block rate. NR/SN's density forests,
  scalar factorials and four explicit margins provide the needed replacement.
* [Temme, Uniform Asymptotic Methods](https://arxiv.org/pdf/1308.1547),
  section 2.2, (2.9)--(2.11), records the even-coefficient Laplace expansion
  for analytic scalar amplitudes with convergence domains. It supplies no
  volume-uniform connected estimate or cutoff-domain identity. The per-reader
  parity cancellation and the actual boundary comparison above supply those
  extra requirements in this bare model.

The source is frozen before its compact
[actual-read manifest](checks/bare_coupling_remainder_read_manifest.json) and
[author receipt](checks/bare_coupling_remainder_receipt.json). No numerical
science run or predecessor edit is used. A DIFFERENT fresh hostile reviewer
must check the fixed-domain re-estimation, the side-fugacity grading and the
volume-first moment passage. Root owns review dispatch, publication, Git,
shared fronts and audits. This author supplies no independent review verdict.
