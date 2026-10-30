# Matched physical regional chart ratios with complete readers

This constructs a log ratio of two actual bare physical chart Haar fibres,
using one real exterior template and one ambient construction. It extends
[RF](REGIONAL_CRITICAL_FIELD_ASTRA.md), SHA256
`45a5665fc51683f026370e774ca8590b221bc5c9e13c07502225226cb13c962b`, and
[RC](REGIONAL_CHART_RETURN_ASTRA.md), SHA256
`b098d18ad22946d7b1e0a4d497e0b5d98250674e06803263d1106f14bf659094`.
Both frozen source interfaces are checked below. Their independent-review
status is provenance, not a proof step; this ratio unit needs fresh review.

The new comparison cancels identical actual deep factors first, retains
every mode, determinant and inactive-Haar term, and then uses a common
virtual small field to price the remaining action. Smallness is required
on the changed links as well as both boundary sets. It does not compare
rough changed links, transport original G/Omega cuts, or normalize a hard
history or inherited effective weight. Continuum existence and a positive
physical continuum mass gap remain open.

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

## 1. Existing results and the matched physical domain

[SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md)26--SA27 cancels connected terms
when selected Gaussian/face measures change. Its normalized pinned ratio
and contour continuation do not compare regional Haar fibres with different
numbers of active modes. [CA](CRITICAL_ACTION_READER_ASTRA.md)8 supplies
the scalar three-mark contraction; CA9 still keeps its extensive critical
action. [CD](CRITICAL_DETERMINANT_READER_ASTRA.md)13--CD19 supplies the full
finite homotopy and critical trace series. RF25 reconstructs those series
on actual regional principal matrices. RC16 proves local agreement but
explicitly leaves full-prefactor ratios separate. The steps below match
those exact objects; no preceding ratio verdict is used as an input.

Use RF's N>=2, odd L>=3, T>=2 and admitted positive kappa interval.
Keep the ambient torus, rooted gauge, u,kappa and original Wilson sources
fixed in both fibres; u must meet RC's explicit chart inequalities.
Let E be the globally gauge-fixed free WHOLE links, D=N^2-1, m0=3L^4+1,
n0=D m0 and sigma^2=N/u. Choose deterministic
Lambda,Lambda' subsets of E and set

    Gamma=Lambda union Lambda', Delta=Lambda symmetric_difference Lambda',
    C={X_e:e in Delta}, R_ref=Delta union B(Gamma),
    B(A)=union_(v:I_v intersects A)(I_v minus A).          (MR1)

Every original field stencil I_v is fixed geometrically, including every
colour and every membership flag it reads. Directly from this definition,
`R_ref=Delta union B(Lambda) union B(Lambda')`. An outside-Gamma field in
a vertex touching Gamma is in B(Gamma); a Gamma field inactive in one
region is in Delta. These two observations prove both inclusions.

Choose ONE geometry-only R, beta=(16R)^-4, atom indexing, source/coarse
product domain, auxiliary radius r_a and field ceiling tau satisfying
RF16--RF18 and RC3--RC13. In particular, with RF's constants,

    delta_hat=delta_*+8eta, Y=c_y zeta,
    c_y=n0*19^4 exp(beta*19^4),
    F_bd=g_*(1+rho)delta_hat+(K_Q+rho B_src)Y+(1+rho)N(Y),
    t_b=2A_G F_bd<=tau/2, Y<=tau/2,
    d_H=D_H(2tau,rho)<=d_reg, m_G d_H<=1/4.              (MR2)

RC supplies the small logarithm with norm <=epsilon_ch at mu=beta/2;
its fixed-radius or shrinking-chart explicit smallness inequalities must
hold. Both regional patch cores are rebuilt from A intersect Lambda and
A intersect Lambda'; neither is identified with P[Lambda]. All large
marked constants are evaluated on common preliminary ceilings. For scalar
families, ||a||_lambda denotes sup_x sum_(S contains x) exp(lambda|S|)
sup|a_S|. Matrix M_beta,B_beta and vector V_beta are RF's coefficientwise
row/column, full-reader marked and component/marked norms.

Fix ONE actual real compact template U_ref on E, used whenever a link is
inactive. At the same real coarse center Vbar require

    U_ref,e=exp(bar xi_e)U0_e(Vbar), ||bar xi_e||HS<=zeta/8
       for every e in R_ref,
    zeta<=1/4, eta<=zeta/16,
    V_c=exp(v_c)Vbar_c, max_c||v_c||HS<eta,
    delta_(Vbar)<=delta_*, |epsilon_p|<rho.              (MR3)

There is no condition on the template at common active links or deep
common exterior links. This is a genuine nonempty physical domain: choose
U_ref=U0(Vbar) on R_ref and arbitrary real compact values elsewhere, then
use the already positive RF/RC radii. No radius depends on |Delta| or the
shape of either region. The SAME template, kernel parameter and original
sources are used on both sides.

On R_ref set xi_e(V)=log[U_ref,e U0_e(V)^-1]. An internal lift link gives
a constant coordinate. For a crossing lift link,
`U_ref,e U0_e(V)^-1=exp(bar xi_e)exp(-v_c)` and
`||exp(bar xi_e)exp(-v_c)-I||HS<=zeta/8+2eta<=zeta/4`.
The principal log series gives ||xi_e||HS<=zeta/2; it is holomorphic and
traceless. Thus MR3 maps into both RF boundary domains on the SAME tube.
It has the N1 coarse reader already paid by the N9 membership collar.
Only for the later virtual construction, define xi_e=0 off R_ref.
This definition is by cases; no logarithm of a rough unused link is taken.

Let Z_A^H denote RC2's unnormalized physical Haar fibre: integrate the
actual bare density w_epsilon over product_(e in A)B_ra in its ORIGINAL
left coordinates, with U_ref fixed on E minus A. It has every original
Wilson/source and normalized compact-kernel factor and every active Haar
measure, and no hard indicators. Its analytic continuation is RC's one.
The ratio below compares these evaluated fibres, not separately normalized
conditional probability laws.

## 2. Cancel the actual deep factor before introducing a virtual phase

Write V_A={v:I_v intersects A}, n_A=|A| and d_A=D n_A. Let W_deep^H be
the product of the original NON-HAAR physical vertices whose stencils miss
Gamma, including every field-free physical factor. All their fine inputs
are the same actual real U_ref or pinned tree links in the two fibres.
Their normalized kernels have the same fixed real means and positive
compact normalizers; numerators and Wilson/source weights are exponentials.
Thus W_deep^H is nonzero on MR3 and cancels IDENTICALLY. No bound on its
size, logarithm or derivatives is taken, and no deep physical link is moved
with U0(V).

Use the actual RF fields b_A, zero-extended only after solving their own
regional equations, with exterior data xi on B(A). Define

    h_A=b_A+(1-I_A)xi, A in {Lambda,Lambda'},
    F_Gamma(h)=sum_(v in V_Gamma) F_v(h),
    J_(Gamma\A)(xi)=product_(e in Gamma\A)j_N(xi_e),
    q_sigma=log h_N+(D/2)log(2pi sigma^2).               (MR4)

For v touching Gamma but missing A, all its fields lie in
`(Gamma minus A) union B(Gamma)`, hence in R_ref and are fixed at their
actual template coordinates. For v touching A, h_A agrees with b_A and
its actual RF exterior arguments on the entire stencil. Consequently the
exact RF/RC factorization, including the complete critical determinant,
is

    Z_A^H=W_deep^H exp(n_A q_sigma)
       exp[-LogDet K_*,A/2] exp[-F_Gamma(h_A)/sigma^2]
       exp[H_A] / J_(Gamma\A)(xi),
    H_A=sum_Y H_(A,Y).                                 (MR5)

The division by J removes the inactive Haar vertices added when the phase
is enlarged from V_A to V_Gamma. It does not remove an active Haar measure.
The h_N^(n_A), sigma^(d_A), (2pi)^(d_A/2) and full-colour determinant are
all present. RC's entire side/corner construction is in H_A; no contour is
replaced by a centered integral here.

Dividing MR5 gives an exact logarithmic expression whose exponential is
the physical ratio:

    L=(n_Lambda-n_Lambda')q_sigma
      -(LogDet K_*,Lambda-LogDet K_*,Lambda')/2
      -[F_Gamma(h_Lambda)-F_Gamma(h_Lambda')]/sigma^2
      +H_Lambda-H_Lambda'
      +sum_e(1_Lambda(e)-1_Lambda'(e))log j_N(xi_e).      (MR6)

Only e in Delta contributes in the last line. Its PLUS sign follows from
`Gamma minus Lambda=Lambda' minus Lambda` and the two denominators in MR5.
Every log j has its branch zero at xi=0. LogDet is the trace of the
accretive matrix logarithm, not the principal scalar log of det K_*.
Unequal dimensions have not been hidden in an alleged determinant ratio
of matrices on the same space.

Now, and only after W_deep^H has canceled, add the SAME V_(Gamma)^c
virtual phase to the two action values. The fields h_Lambda,h_Lambda'
are identical outside Gamma, so each original vertex missing Gamma has
identical virtual arguments. Hence

    F_Gamma(h_Lambda)-F_Gamma(h_Lambda')
       =F_epsilon(h_Lambda)-F_epsilon(h_Lambda')
       =[F_epsilon(h_Lambda)-F_epsilon(0)]
          -[F_epsilon(h_Lambda')-F_epsilon(0)].           (MR7)

All virtual fields are small and will satisfy V_beta(h_A)<=tau below.
No virtual outside factor is equated to a rough physical outside factor.
MR7 is the addition and subtraction of identical analytic expressions,
after the actual physical cancellation. It also cancels every original
zero-field vertex value termwise, including finite-u kernel vacua and all
source values. No z_t replacement for a field-dependent normalizer is made.

RF14 supplies a bound for the FULL phase force g0. It does not by itself
justify assigning that bound to a touching sub-sum's boundary gradient.
MR7 is the exact identity permitting its use below; no additional estimate
for the boundary gradient of F_Gamma is assumed.

## 3. Full-reader virtual fields and the nonstationary action estimate

Membership of R_ref is local: Delta uses the owner's two flags and
B(Gamma) uses all incident original stencils. Give each xi_e atom the
reader N9(X_e), containing both regions' required flags and its original
physical/coarse data. This includes the N1 reader of the physical log.
The same count as RF12 gives

    V_beta(xi)<=Y,
    V_beta((1-I_A)xi)<=Y,
    V_beta(h_A)<=s_h:=t_b+Y<=tau.                        (MR8)

The inactive mask adds only its owner, already in N9. Bounds use individual
coefficient suprema before summing, including suprema over deterministic
masks. One does not sum over region choices. Many changed or boundary links
do not turn MR8 into an extensive vector norm. The actual b_A atoms keep
RF's complete readers; this is not a second critical-field construction.

Use a fixed common library of all ambient scalar indices, local monomials
and original vertex roots, retaining zero coefficients under masks. The xi
library is the SAME in the two h families. RF's canonical agreement shows
that corresponding h_A coefficients agree whenever the two active masks
agree on their full reader. In particular a difference coefficient with
reader S disjoint from C is zero. The additional R_ref flags are part of S
and are common to the pair; they are not invisible global choices.

Let G0=g_*(1+rho)delta_hat. The full phase, with every finite-u normalizer
and Haar logarithm, obeys RF14--RF15. For 0<=s<=1 set A_s=F_epsilon''(s h_A).
Taylor's exact scalar identity is

    F_epsilon(h_A)-F_epsilon(0)
       =g0^T h_A+int_0^1(1-s)h_A^T A_s h_A ds,
    V_beta(g0)<=G0,
    M_beta(A_s)<=k_M+D_H(s_h,rho),
    B_beta(A_s)<=k_B+D_H(s_h,rho).                       (MR9)

Here k_M=exp(beta*11^4)b_abs and k_B=n0*11^4*k_M, as in RF15.
No global stationarity of h_A is asserted. The inactive coordinates need
not satisfy any Euler equation. The segment stays in the original analytic
fine chart because s_h<=tau obeys RF17; RF's local Taylor/reader proof
applies to any vector atom family in that ball, including MR8.

Here are the contraction bounds used in MR9. For vector families f,h,
a mark in either factor of sum_i f_i h_i gives
`||f^T h||_beta<=2 V_beta(f)V_beta(h)`. For a matrix family A and vectors
h,k, a mark in h, in A, or in k gives respectively its row, full marked,
or column estimate. Thus, with all scalar colours summed,

    ||h^T A k||_beta<=[2M_beta(A)+B_beta(A)]V_beta(h)V_beta(k).
                                                                  (MR10)

Each product reader contains the contracted field endpoint, so its union
is connected. The nonlinear Hessian is Taylor-expanded before insertion
of the actual h atoms, so all newly inserted reference and critical-field
readers remain. The reference values are field atoms here: RF13's original
vertex counts apply with their N9 attachments charged through Y. Its root
and occurrence marks are precisely RF13's D_H.
Integration over s is justified by the same uniform positive majorant.

Consequently there are actual connected coefficient families a_(A,S) with

    [F_epsilon(h_A)-F_epsilon(0)]/sigma^2=sum_S a_(A,S),
    ||a_A||_beta<=A_ref,
    A_ref={2G0 s_h+[2k_M+k_B+3D_H(s_h,rho)]s_h^2/2}/sigma^2.
                                                                  (MR11)

Fix the common original coefficient/atom ordering before grouping labels.
Every corresponding word in these two action families has the same
coefficient when S misses C, by the h agreement and the fixed full phase.
Absolute convergence preserves that equality after grouping. Thus
`a_(Lambda,S)-a_(Lambda',S)=0` for S disjoint from C, and its difference
family has norm <=2A_ref. This cancellation precedes taking absolute sums;
there is no sum of two total-volume action bounds. This is the actual
zero-vacuum action price; it is generally not a small irrelevant remainder.

## 4. Determinant, inactive Haar and normalized chart terms

RF25's regional determinant uses the SAME ambient patches for
`K_theta,A=(1-theta)B I_A+theta K_A`. Its inverse has
`M<=m_det=p_RF/(1-r_RF)` and `B_beta<=b_det=n_R p_RF/(1-r_RF)^2`,
where p_RF,r_RF,n_R are RF6's fixed constants. Define

    a_K=exp(beta*11^4)(b_abs+B), b_K=n0*11^4*a_K,
    C_det=n0 exp(beta)|log B|+b_det a_K+m_det b_K
                           +(m_G+b_G)d_H/(1-m_G d_H).   (MR12)

The Jacobi integral gives d_A log B plus the trace of this inverse times
K_A-B I_A. Marking its two factors costs b_det a_K+m_det b_K. The critical
ordered trace series has X=G_A Delta_A, M(X)<=m_G d_H and
B_beta(X)<=(m_G+b_G)d_H; its j-th trace's 1/j cancels the j marked choices.
This proves the last term in MR12, including the complete determinant.
Closed scalar paths retain connected readers and every patch membership.
The d_A log B term is a singleton-block count of actual active scalar modes.

These are canonical regional formulas. Applying the local-agreement check
to every patch inverse, matrix mask and critical-field attachment gives

    LogDet K_*,A=sum_S l_(A,S), ||l_A||_beta<=C_det,
    l_(Lambda,S)-l_(Lambda',S)=0 if S intersect C is empty. (MR13)

The interpolating matrices are accretive; Jacobi continuation from B I_A
agrees with Tr Log K_*,A, including zero-dimensional matrices. No branch
constant or full determinant is normalized away. The contribution to MR6
therefore has rooted norm <=C_det, after its factor one half.

For an explicit bound on the remaining Haar term, work in the same HS
orthonormal scalar coordinates. Pulling the invariant top form back by
a -> exp(a) gives the differential determinant

    j_N(a)=det_sl(N,C)[(1-exp(-ad a))/(ad a)]
          =det_sl(N,C)[sinh(ad a/2)/(ad a/2)].           (MR14)

Both quotients mean their entire power series at zero. No inverse of ad a
is taken and none of its zero directions is removed.
To verify the differential, differentiate the matrix exponential power
series and group it as int_0^1 exp(-s ad a)ds after translation to the
identity. Its determinant is the coordinate Haar density with value one
at zero. Tr(ad a)=0, so the exponential half-factor has determinant one.
This derives the formula with the original h_N still outside j_N.
For a normalization check, left/right multiplication on matrices gives
Tr[(ad a)^2]=2N tr(a^2); the scalar identity mode contributes zero. Thus
log j_N(a)=N tr(a^2)/12+O(||a||^4), giving the actual real-coordinate
Haar Hessian N^2/(6u) I in F_0, as retained in RF5.

For r=||a||HS<=1/4, ||ad a/2||op<=r. The series for sinh(z)/z gives
`||sinh(z)/z-I||<=r^2 cosh(r)/6<=r^2/3<=1/48`.
The logarithm series then has norm <=2r^2/3. Taking the trace over all D
scalar directions proves, on the branch zero at the origin,

    |log j_N(a)|<=(2D/3)||a||HS^2,
    J_ref=(2/3)c_y zeta^2.                              (MR15)

Assign each signed inactive-Haar term in MR6 its N9 owner reader. At most
m0*19^4 links meet a fixed mark, and each xi has norm <=zeta. Thus MR15's
J_ref is its full weighted rooted budget at beta. Its coefficient is zero
unless its own link is changed, so every such reader meets C. This argument
does not use a coordinate Jacobian at any rough deep exterior link.

Finally RC14 and RC16, on the same physical pullback and atom family, give

    ||H_A||_mu<=epsilon_ch, mu=beta/2,
    H_(Lambda,Y)-H_(Lambda',Y)=0 if Y intersect C is empty. (MR16)

Their presence/absence of active cuts and all side flags are exactly those
in RC. Full-reader agreement applies because the template and all original
continuous data are common. The physical boundary substitution stays within
MR3 and adds no reader beyond the already paid N9/N13 collars. No outside
Haar factor is contained in this small chart logarithm.

## 5. The anchored complete-reader logarithm

Put n_A(x)=#{e in A:X_e=x}. For each owner block x give
`[n_Lambda(x)-n_Lambda'(x)]q_sigma` the singleton label {x}.
Its magnitude is at most m0|q_sigma| and it vanishes outside C. Combine
these mode terms with minus one half MR13's difference, minus MR11's
difference, MR15's signed Haar family and MR16's difference. Lowering the
beta weights to mu costs nothing. This constructs connected readers Y with

    Z_Lambda^H(U_ref;V,epsilon)/Z_Lambda'^H(U_ref;V,epsilon)
       =exp[L], L=sum_(connected Y, Y intersects C) r_Y,
    sup_x sum_(Y contains x)exp(mu|Y|)sup|r_Y|<=Q_sigma,
    Q_sigma=exp(mu)m0|q_sigma|+C_det+2A_ref+J_ref+2epsilon_ch,
    mu=beta/2.                                         (MR17)

The supremum and every coefficient use the actual common physical domain
MR3. It ranges over all ambient blocks, including holes and exterior
readers. Every nonzero term, constant or nonconstant in the continuous data,
meets C. The result is not an endpoint-only support estimate. All infinite
critical-field, covariance, determinant and cluster sums have already
converged absolutely in the displayed complete-reader norms before their
differences and regrouping are taken. No sum over alternative regions is
introduced, and no extra support margin is asserted.

The expression is holomorphic in the original V and epsilon on MR3. At
real data both physical fibres are strictly positive; all determinant and
Haar branches above and the convergent RC logarithms are real there.
Therefore L is the real logarithm of the positive ratio there, with its
unique indicated holomorphic continuation. Its exponential is MR6's exact
physical ratio, not merely a formal power series or a bound conditional on
an unspecified denominator. RC's nonvanishing and the exact nonzero outside
factor ensure the denominator is nonzero on the whole common tube.

Summing by a marked block of C yields

    |L|<=|C|Q_sigma,
    exp(-|C|Q_sigma)<=|Z_Lambda^H/Z_Lambda'^H|<=exp(|C|Q_sigma).
                                                                  (MR18)

If C is empty the entire coefficient family is zero and the ratio is one.
For an empty region its determinant and integral are one; MR5 still has
all its actual outside density. These cases require no removed colour or
extra gauge factor. A mode contribution cannot be canceled by identifying
matrices of different dimensions.

A limited spatial consequence is also explicit. Set nu=mu/2=beta/4. Any
connected Y containing x and meeting C has |Y|>=dist(x,C)+1. Hence
`sum_(Y contains x)exp(nu|Y|)sup|r_Y|<=Q_sigma exp[-nu dist(x,C)]`.
This is localization of this matched one-step log ratio, not a physical
continuum correlation or mass-gap statement. On half source/coarse tubes,
finite scalar Cauchy jets retain their multiindex factors
`alpha! k! (2/rho)^|alpha| (2D/eta)^|k|` multiplying Q_sigma.
A derivative outside its full reader vanishes. No unscaled derivative radius is kept fixed when eta shrinks.

## 6. A physically shrinking matched comparison

Use RC17's fixed preliminary majorants, ONE R,beta and positive fixed rho.
Choose the constant c after those majorants, satisfying RC's explicit
upper bound, and set r_a=sigma p, tau=c sigma p. Keep

    Y=k_y tau, zeta=Y/c_y, delta_*=eta=k_v tau,
    k_y=min(1/2,1/(8A_G B_bd)),
    k_v=min(1/[72A_G g_*(1+rho)], k_y/(16c_y)),
    B_bd=1+K_Q+rho B_src+(1+rho)N''(bar_tau/2)bar_tau/4.  (MR19)

These are RC17's same constants, not a new regional atom decomposition.
They give Y<=tau/2, A_G F_bd<=tau/4, eta<=zeta/16 and
G0=9g_*(1+rho)k_v tau. For p -> infinity and sigma p -> 0 all the fixed
fine/coarse caps and RC13's explicit integral conditions eventually hold.
The template must satisfy MR3 on the EXTRA changed-link set at each u.
A fixed nonzero changed-link displacement need not stay in this domain;
perfect matching on R_ref and arbitrary deep real values is a nonempty
example for every u.

Let bar d_H=D_H(2bar_tau,rho) and use it in C_det and the following constants.
They were fixed BEFORE c. With s_h<=tau, MR11 and MR15 imply

    2A_ref<=C_A c^2 p^2,
    C_A=36g_*(1+rho)k_v+2k_M+k_B+3bar d_H,
    J_ref=C_J c^2 sigma^2 p^2, C_J=2k_y^2/(3c_y),
    exp(mu)m0|q_sigma|
       <=(exp(mu)n0/2)log u
          +exp(mu)m0|log h_N+(D/2)log(2pi N)|.           (MR20)

RC18 gives epsilon_ch<=C1 sigma^2+C2(1+p^(91D+2))exp(-a_P p^2/64).
Consequently the per-changed-block price in MR17 is bounded by the explicit
mode term O(log u), the finite full-determinant/normalization term O(1),
the tunably small coefficient C_A c^2 times p^2, and a vanishing remainder.
The Haar remainder vanishes because sigma p -> 0. The source radius rho
remains positive and fixed; the physical coarse and reference-coordinate
radii shrink. The constants multiplying c^2 are independent of the later
choice of c within its fixed allowed interval. RC's side polynomial
constants may also be bounded using that fixed upper endpoint for c.

No original-energy charge has been spent. These inequalities do not show
that this normalization price is beaten by a particular complement or
history estimate. Such a comparison must use its actual matched domain,
its remaining factors and the same reader rate.

## 7. Scope and source handling

The construction compares deterministic whole-link regions of arbitrary
shape, using one fixed physical exterior template and small coordinates
on R_ref, with exact cancellation of arbitrary deep common exterior factors.
It supplies an actual complete-reader logarithm and price for this bare
matched chart ratio. It does not cover rough changed links, an exterior
integration, data-dependent history selectors, original G/Omega cuts or
inherited effective actions. Next-step identification, multiscale control,
continuum existence and a positive physical mass gap remain separate.

No numerical physics experiment or new external theorem is used. The local
Haar calculation and the changed scalar/canonical steps are derived above;
the RF/RC source constructions, rather than their review reports, supply
only their specified inputs. Earlier sources stay immutable. Source freeze
precedes the [read manifest](checks/matched_regional_ratio_read_manifest.json)
and [author receipt](checks/matched_regional_ratio_receipt.json), then fresh
independent review. Author checks are not independent evidence. Root retains
all Git, publication, shared-front and audit actions.
