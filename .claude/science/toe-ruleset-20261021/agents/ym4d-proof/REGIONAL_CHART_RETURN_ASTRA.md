# Regional original-coordinate charts with actual small exterior data

This extends [SN](SHIFTED_NONLINEAR_READER_RETURN_ASTRA.md) and
[SH](SHRINKING_CHART_RETURN_ASTRA.md) to arbitrary deterministic sets of
whole gauge-fixed free links. The new producer is
[RF](REGIONAL_CRITICAL_FIELD_ASTRA.md), frozen at SHA256
`45a5665fc51683f026370e774ca8590b221bc5c9e13c07502225226cb13c962b`.
All 592 source lines were read and its consumed interfaces checked below.
RF was awaiting review when this unit began; its fresh independent review
subsequently accepted this unchanged source. Its displayed mathematical
arguments and checked domains, not that verdict, are the premises below.
No global critical point is merely restricted to a region, and no exterior
force is silently set to zero. This new chart unit needs its own fresh review.
The regional chart includes every side and corner. All original vertices,
normalizers, Haar factors and outside-only actions are assigned explicitly.
The result concerns small complex exterior fine coordinates on a stated
product domain; it is not rough-boundary control, a hard-history conditional
denominator, an all-cut return or a multiscale theorem. Continuum existence
and a positive physical mass gap remain open.

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

## 1. What is new, and the exact regional object

SN proves a whole-torus original-a chart logarithm; its normalized active
marginals are not conditional regional precision matrices. SH retunes that
same chart to radius sigma p. [IC](INTERACTING_SELECTED_CORE_ASTRA.md) and
[SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md) treat selected white domains, and
[STEP55](STEP55.md)'s hole statement remains an implication of its stated
hypotheses. [GC](GRADED_COMPLEMENT_ASTRA.md)13--GC18 instead study a real conditional phase on sets of block-owned
links; its constrained minimizer can lie on the chart boundary, and its
KKT comparison prices a different denominator. None of these inspected
statements supplies the regional joint critical-field input used here.

Keep the ambient torus, pinned tree quotient and actual finite-u model of
SN1. Write E for all its free positive whole links, m0=3L^4+1, n=m0 T^4,
D=N^2-1, n0=D m0 and sigma^2=N/u. Choose a deterministic subset Lambda of E, with
arbitrary holes and disconnected components. Do not fix another gauge or
delete a root, colour, crossing or harmonic mode inside Lambda. Put
n_L=|Lambda| and d_L=D n_L. The active coordinates are a_e. Boundary
coordinates y_e are introduced only on B(Lambda) below; deeper exterior
links remain actual compact fields, without a chosen small logarithm.
Negative edges still use the actual inverse, and t=kappa u stays real and fixed.

Use the SAME original local phase vertices F_v as SN, including source
and base Wilson as one vertex, each complete normalized compact-kernel
vertex, and every Haar logarithm. Their declared whole-link stencils L_v
are fixed by the original formulas. Define

    V_L={v:L_v intersects Lambda},
    B(Lambda)=union_(v in V_L)(L_v minus Lambda),
    F_L(a;y)=sum_(v in V_L)F_v(a_Lambda,y_B),
    I_L(y)=h_N^(n_L) integral_(product_Lambda B_ra)
                                      exp[-F_L(a;y)/sigma^2] da. (RC1)

Only y on B(Lambda) is required to be small. Zero extension y^B elsewhere
is a device for evaluating touching vertices, which have no other exterior
field inputs. It does not replace any physical deep exterior link by the
lift. Every touching F_v(0;y), lower jet, finite-u vacuum and normalizer
stays in F_L. A zero nonlinear remainder creates no primitive but does not
remove its phase. Empty-stencil original vertices stay outside even when
Lambda=E. Selection of every touching stencil reads its local membership.

For arbitrary fixed real exterior free links U_out, define W_out^H to be
the product of ALL original Wilson/source and normalized-kernel factors
whose fixed field stencils miss Lambda. Haar factors belong to their
measures. When boundary coordinates match U_out, the physical conditional
chart Haar fibre is exactly

    Z_L^H(U_out;V,epsilon)=W_out^H(U_out;V,epsilon)
                                      I_L(y_B(V);V,epsilon),
    y_e(V)=log[U_out,e U0_e(V)^-1], e in B(Lambda).        (RC2)

This is RF27's factorization, not a bound on W_out^H. Deep exterior fields
may be arbitrary real compact links and are never moved with U0(V). The
quantified physical specialization is checked in section 6 below.

For comparison, IF the entire exterior also has small coordinates, set
F_out=sum_(v not in V_L)F_v(y_ext), so F=F_L+F_out exactly, and put
J_out=product_(e not in Lambda)j_N(y_e). Then

    Z_L^coord=exp[-F_out/sigma^2] I_L,
    Z_L^H=exp[-F_out/sigma^2] I_L/J_out,
    dH_out=h_N^(n-n_L) J_out dy.                         (RC2a)

Z_L^coord is the fibre relative to h_N^(n-n_L)dy. Multiplying the second
formula by dH_out recovers the full original joint top form, with exactly
h_N^n and one copy of every Haar density. The division removes only the
inactive Haar factors already assigned to the exterior measure. There is
no reference normalization or additional regional FP factor. For rough
far exterior we use RC2, not a fictitious global coordinate F_out.

## 2. Checked frozen producer interface and one common construction

RF supplies the following interface on one common domain, for every Lambda:
`V_c=exp(v_c)Vbar_c`, max ||v_c||HS<eta, center curvature <=delta_*,
|epsilon_p|<rho, and max_(e in B(Lambda))||y_e||HS<zeta.
The curvature supremum is delta_hat=delta_*+8eta. All constants and domains
below are uniform in the ambient volume and the shape of Lambda.

* An actual holomorphic active critical field b_L with
  partial_a F_L(b_L;y)=0 and complete-reader vector norm V_beta(b_L)<=tau.
  Its phase includes the nonzero coarse AND exterior boundary force.
* Its actual active Hessian and covariance
  K_L*=partial_a^2 F_L(b_L;y), C_L=K_L*^-1. The reference lift is the
  principal K_L=K[Lambda], not a global critical Hessian restricted after
  solving a different problem.
* One AMBIENT patch cover, radius R>=4 and beta=(16R)^-4, with
  P_L=sum_A chi_A K_(A intersect Lambda)^-1 chi_A,
  C_L=P_L+E_lift,L+T_crit,L. Empty patch compressions contribute zero.
  Every label keeps the complete ambient patch/read collar and membership
  of all used free links. It is never clipped to active blocks.
* Re P_L>=c0, and the individual entry envelope
  sup|P_L(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)]. The two complete-reader
  tails have total M_beta<=eps and finite B_beta<=B_E, with

      eps<=e_*=min(c0/8,1/(4v_I),a/(64v_I^2)),
      g=(2n0/gamma)coth(m/4)^4, a=c0/g^2,
      v_I=(2n0/c0)coth(theta/2)^4,
      theta=min(m/2,c0/(2A_1)),
      A_1=(2n0/gamma)sum_Z |Z|_1 exp(-m|Z|_1/2).          (RC3)

  Coefficient suprema are inside the row, column and marked sums. Large
  B_E is retained. All continuous original data, including y, are read.
* Canonical atom agreement: coefficients with reader S agree whenever
  their actual original data AND Lambda membership agree on S, with an
  ambient indexing/ordering fixed independently of Lambda.

The boundary force is explicitly paid by RF12--RF20. The zero-extended
vector y^B reads the boundary-membership mask in N_9(owner), so its bound is
`Y=c_y zeta`, `c_y=n0*19^4 exp(beta*19^4)`. This includes every incident
stencil membership decision; the smaller N_1 count is not used. Set Q_K
equal to RF15's K_Q. The checked force/derivative conditions are

    A_G{g_*(1+rho)delta_hat+(Q_K+rho B_src)Y+(1+rho)N(Y)}<=tau/4,
    A_G{rho B_src+(1+rho)N'(tau+Y)}<=1/4,
    D_H(tau+Y,rho)<=d_H:=D_H(2tau,rho)<=d_reg,
    d_reg=min(gamma/4,1/(4m_G),c0/(32m_G^2),e_*/(4m_G^2)). (RC4)

These are RF15--RF18 on the SAME regional family, with Y<=tau/2 and
RF17's stronger N'(2tau),D_H(2tau,rho) conditions imposed. RF19 is the
actual boundary-force contraction, including H_epsilon; RF20 gives
V_beta(b_L)<=2A_G F_bd<=tau/2. RF21--RF23 give total tail mass
<=2e_*/3 and B_E=b_lift+b_crit. Fix eps=2e_*/3 and bound B_E at
the preliminary ceilings; later restrictions only improve these budgets.
RF24 proves the active-core inverse bounds, and its section 5 proves
canonical agreement. These source arguments, not
its review, are the dependency. Its constants N,D_H,m_G,A_G and
d_reg retain their RF meaning; our enlarged primitive reader counts below
do not redefine them.

Use this new regional family throughout. P_L is generally not P[Lambda]
for the old whole-torus patch sum. Intersecting two scalar domains does
not identify those atom decompositions. The conjugation argument in SN2
applies to every principal P_L[I]: its inverse G has absolute row/column
bound v_I, Re G>=a and ||G||<=b_P=1/c0. The index restriction only decreases
the ambient geometric sums. Small holes require no additional mode deletion.
Both tails, all colours and full membership readers stay in the subsequent
determinant-loop and inverse-chain expansion.

## 3. Local nonlinear vertices with the frozen exterior kept as data

Let a_f0,H be RF's common radius and bound for the vacuum-subtracted
source-free local vertices, with the Wilson source factor paid separately.
RF's fine-coordinate radius a is denoted a_f0 here; our a is RF's a_P.
Choose a_f<a_f0/2 and an exterior ceiling bar_zeta<a_f0/4.
After the regional R is fixed, choose positive ceilings
bar_tau<a_f/64,bar_rho<=1,bar_zeta and a preliminary coarse
tube satisfying RF17--RF18. Fix r_t<a_f/16 with bar_tau+r_t<a_f/2.
These choices precede the local majorants and the eventual r_a.
For a touching v, regard
F_v(a_(L_v intersect Lambda);y) as a function of its ACTIVE fields, with
exterior y frozen. On |a_i|<a_f,

    |F_v(a_active;y)-F_v(0_active;y)|<=2(1+bar_rho)H.      (RC5)

For each unmultiplied vertex both terms differ from the SAME original
all-zero fine-field vacuum by at most H; |1+epsilon|<=1+bar_rho.
That vacuum and F_v(0;y) are still retained in RC1's phase. Local exterior data stay as coefficient arguments, not new integrated
coordinates. Their full N_9 boundary-mask readers are nevertheless retained.

There are at most q=(8L^4+8)D active scalar slots and I0=15 distinct original
vertices per active scalar. Restriction can only reduce these counts.
Enlarge the original radius-four vertex root to N_13(x_v). This contains
N_9(X_e) for every field owner X_e in its stencil. Thus all boundary-mask
and physical-substitution readers are paid, including inactive blocks. Use
`s_v=27^4`, `d_v=(9L^4+5)s_v`, `d_1v=q d_v` for these primitive readers.
These replace SN's s0,d0,d1 only in the nonlinear-vertex budgets. Compute
all Taylor/Mayer constants at fixed preliminary
bar_tau,bar_rho,bar_zeta ceilings using

    f_reg(t)=2H(1-t/a_f)^(-q),
    A_l=(1+bar_rho)e^(beta s_v) f_reg^(l)(bar_tau)/l!,
    B_l=d_v(1+bar_rho)e^(beta s_v)
              [f_reg^(l)(bar_tau)+bar_tau f_reg^(l+1)(bar_tau)]/l!. (RC6)

Use ambient monomials with explicit active masks; do not sum over region
choices or introduce an extra active-pattern entropy. The root mark pays
every local exterior y and stencil/boundary-membership reader.
A mark in b_L's substituted atoms uses its full producer norm. Taylor is
only in active variables, so there is no new uncharged exterior attachment.
The proofs of the shifted coefficient envelopes SN8--SN9 and centered
parity envelopes [NC](NONLINEAR_CHART_ACTIVITY_ASTRA.md)12--NC15 now use
RC6, including its changed factor 2H, enlarged reader counts and active
radius, with SN's fine remainder radius r0 replaced by r_t. Recompute
A,W0,W1,E0,E1 from these envelopes; do not copy the old numerical majorants.

More explicitly define, for active z and each touching v,

    R_(v,L)(z;y)=sigma^-2{F_v(b_L+sigma z;y)-F_v(b_L;y)
       -sigma partial_a F_v(b_L;y)z
       -(sigma^2/2)partial_a^2 F_v(b_L;y)[z,z]}.           (RC7)

Only the SUM of its linear jets vanishes. The quadratic sum is exactly
K_L*. No exterior gradient equation is asserted. A side pattern is now
J subset (L_v intersect Lambda); exterior link slots stay at their fixed y.
The translation expansion in b_L/tau has exactly the same binomial, marked
and per-coordinate bounds as SN7--SN9. For a nonlinear singleton with
NO side, signed active integrals have the same parity, even with nonzero complex y in their
coefficients. No side species receives that parity improvement.

The parameter order is: one regional R/tail family; fixed preliminary
source/field/exterior ceilings satisfying the producer bounds; RC5--RC6's
majorants; then r_a, then actual tau, then smaller zeta,delta_*,eta satisfying
RC4. Require

    r_a<r_t/8, eta_bar=4A I0 r_a(1+r_a)<=a/128,
    tau<=min(bar_tau,r_a/(16D)),
    (L_hat^2+2eta_bar)(D tau)^2<=a r_a^2/64,              (RC8)

with 2(r_a+tau)<=r_t. The fixed source radius can remain
positive; the boundary force requires an actual positive small zeta, not
arbitrary exterior fields. All changes must restrict the same canonical
regional family. Its boundary-force and Hessian choices are part of the
producer check, not consequences of the contour argument.

## 4. Exact regional contour and primitive compatibility

Write b=b_L, C=C_L, m=b/sigma and p=r_a/sigma. The full regional prefactor is

    P_L*=h_N^(n_L)(2pi sigma^2)^(d_L/2)det(K_L*)^-1/2
                                             exp[-F_L(b;y)/sigma^2]. (RC9)

Use exp[-LogDet(K_L*)/2] with RF25's accretive matrix-log branch.
Since K_L* and its inverse are accretive, this is exactly the normalized
Gaussian branch continued from the positive real matrix, with all d_L
colours and modes. The critical action includes F_L(0;y), its boundary
values and all field-dependent normalizers; RC14 will not bound that action.
The original active chart becomes product_(e in Lambda)(B_ra-b_e)/sigma. The product
ball translation identity gives EXACTLY

    I_L/P_L*=sum_(H subset Lambda)(-1)^|H| int_[0,1]^H
      int_(sphere_p^H times B_p^(Lambda\H))
       product_(e in H)(m_e.n_e) g_C(x-tm_H)
          product_(v in V_L)[1+W_(v,L)(x-tm_H;y)] dS_H dx dt_H. (RC10)

Here W=exp(-R)-1. Differentiating a ball integral gives the minus outward
flux; tensoring gives every corner. All active D-colour sphere measures,
flux sigma powers and t parameters are retained. The exterior y is never
translated. On the entire sweep the active fine field is bounded by
r_a+2D tau<a_f; inactive fields remain below bar_zeta. Thus every original
local vertex stays in its proved analytic chart along the full homotopy.

Expand distinct TOUCHING vertices, and the remaining active balls by
inclusion-exclusion. If W is the selected vertex set, H the sides and B
bad active links, exact admissibility is

    B subset Lambda, B disjoint H union F_L(W),
    F_L(W)=union_(v in W)(L_v intersect Lambda),
    J_v=H intersect L_v.                                (RC11)

Keep balls on every selected active non-side slot. No nonlinear vertex
is evaluated outside its active chart. The active Gaussian marginal is
C_L[I], the principal covariance, where I contains all scalar colours of
F_L(W) union H union B. All other active fields marginalize to one by the
normalized complex Gaussian identity, continued in the translated active
arguments. They are not exterior y fields. Empty W,H,B gives exactly one.

Use the same three primitives as SN: one selected nonlinear reader atom,
one signed bad active link, and one flux atom -b_(e alpha;S)n_alpha/sigma
with its sphere and shared t_e. This absorbs the sign in RC10 once.
Membership of every vertex stencil is retained in its root. Add the fixed
AMBIENT collars Q_v=N_(16R)(x_v) and Q_e=N_(16R)(X_e); never intersect
these with Lambda. Thus s_c=(32R+1)^4, d_c=(9L^4+5)s_c and d_h=m0 s_c
are unchanged upper bounds, including small tori. N_13(x_v) is inside
Q_v for R>=4; no mask collar is lost in this statement.

Partition primitives by overlap of their enlarged complete readers. Each
component keeps its primitive list and side flags, not just their union
S_B. Its fields I_B are active, but S_B can contain many inactive blocks.
Core P_L is block diagonal between these components; its patch membership
and data readers lie in the corresponding S_B. Each inverse-core block
and determinant reads S_B ONCE. If a side lies in a selected vertex's active
stencil, their collars meet. Hence both presence and absence constraints
in RC11 and every shared t_e are internal to a component. Base disjointness
reconstructs exactly one admissible original primitive family.

## 5. Uniform density, side and connected bounds

Set the matrix constants from SN4 using the new RC3 budgets:
`t=v_I eps`, `t_E=v_I^2 eps/(1-t)`, `ell=-log(1-t)/2`,
`c_*=2b_P^2/a+b_P+t_E+1`, `L_hat=sqrt(2)max(1,sqrt(2exp(1)c_*))`,
and `K_m=v_I/[2(1-t)]+v_I^2(16/a+1)/(1-t)^2`.
The fixed regional family and pair masks, rather than a global critical
covariance compression, are used in the exact normalized loop/chain series.
For |s_BB'|<2 its accretivity is >=3c0/4 and inverse precision >=12a/25.
Only density factors are differentiated; frozen exterior data, side flags,
fluxes, cuts and nonlinear primitives remain fixed.

The mixed-density estimate SN16--SN19 holds for every scalar multiindex nu
with L_hat^|nu| product_i sqrt(nu_i!). The active polynomial degree per
coordinate is at most 6I0=90. Restriction of a stencil does not increase it.
Exterior fine fields are bounded coefficient data, so they add no moment,
cutoff or integration dimension. With the recomputed A define, as in SN18,

    M90=2^90 max(1,(2880/a)^45), K_g=max(1,exp(ell)sqrt(8b_P/a)),
    C_V=q(1+q)(K_g M90)^q, A_D=(b_P/(2pi))^(D/2)exp(D ell).

The primitive weights are

    a_vertex=C_V sigma w_(v,J;S), a_bad=q_h,
    a_side=Q_s sup|b_(e alpha;S)|,
    q_h=K_g^D 2^(D/2)exp(-a p^2/32),
    Q_s=A_D 2^(D/2)omega_D p^(D-1)sigma^-1
                   (1+D tau/sigma)^(90D)exp(-a p^2/64).  (RC12)

All active determinants and surface measures are included. A Gaussian
translation reader mark keeps its actual side root and costs
`K_tr=(L_hat/sigma)(1+sqrt(2)L_hat D tau/sigma)`. Both covariance tails
and their full membership/exterior readers contribute B_E as in SN.

For clarity the resulting positive budgets are exactly

    h_v=C_V sigma e^(beta s_c)(W1+d_c W0),
    h_2=C_V sigma^2 e^(beta s_c)(E1+d_c E0),
    h_h=d_h e^(beta s_c)q_h,
    h_s=Q_s e^(beta s_c)tau(1+d_h D), h_0=h_v+h_h,
    h_tr=K_tr Q_s e^(beta s_c)D tau^2,
    C0=1+K_m B_E,
    h_c=min(beta/16,1/[4(1+L_hat^2 eps)],
                           beta/[64n0(1+L_hat^2 eps)]),
    epsilon=C0(h_2+h_h)+(C0/h_c+L_hat^2 B_E)h_0^2
                          +2(C0+L_hat^2 B_E h_c)h_s+h_tr. (RC13)

Use sigma<=1, q_h<=1, h_0<=h_c/2, h_s<=h_c/2 and epsilon<=beta/16.
For fixed r_a,tau these hold for sufficiently large u. These thresholds
remain independent of Lambda and T, despite possibly large marked constants.

Here are the shape-dependent hypotheses in the connected proof. Primitive
incidences are bounded by the ambient d_c,d_h. The Gaussian attachment
recursion uses |I_B|<=n0|S_B|, not a count of active blocks or an intrinsic
region volume. The normalized empty marginal is one, so no residual-only
vacuum can survive when a region or component is empty. The independent-pair
heat identity and subsequent path-minimum forest evaluation are unchanged.
Every derivative scalar is active; the per-coordinate factorial recursion
therefore has exactly the same supersolution. Reader regrouping preserves
old base compatibility, including membership and side patterns. These
checks justify each of SN23--SN29 for the actual regional objects.

Spend beta/8 separately on primitive components, scalar Gaussian
attachments, complete-reader regrouping and the connected logarithm. It
follows under the stated producer contract that

    I_L/P_L*=exp[sum_(connected ambient Y) H_(Lambda,Y)(V,epsilon,y)],
    sup_x sum_(Y contains x)e^(mu|Y|)sup|H_(Lambda,Y)|<=epsilon,
    mu=beta/2>0.                                        (RC14)

The supremum over x is over ALL ambient blocks, including holes and exterior
readers. This is not an active-support norm with the boundary erased. The
canonical small-log branch comes from its convergent connected series and
has zero constant activity term. P_L* is nonzero on the same admitted domain.
Thus I_L is nonzero on the joint boundary-coordinate domain. The full
physical fibre retains W_out^H in RC2; its physical specialization is
checked separately below. When the entire exterior is in the
small coordinate chart, RC2a also has its explicit nonzero analytic factors;
this is not an analytic-chart assertion about arbitrary rough far fields.

## 6. Physical specialization, local agreement and shrinking charts

For the actual physical specialization fix real compact U_out, with no
condition on its deep values. At the real coarse center suppose
`U_out,e=exp(bar y_e)U0_e(Vbar)` on B(Lambda), with
||bar y_e||HS<=zeta/8. Impose the ONE common restriction

    zeta<=1/4, eta<=zeta/16.                             (RC15)

This is inside RF27's tube and avoids two different physical domains.
On internal lift links the boundary coordinate is constant. On crossing
links it is the principal logarithm of Q=exp(bar y_e)exp(-v_c). Since the
first factor is unitary and eta<=1,
`||Q-I||HS<=||bar y_e||HS+exp(eta)eta<=zeta/8+2eta<=zeta/4`.
Thus ||Q-I||op<1/2 and the logarithm series gives
`||log Q||HS<=2||Q-I||HS<=zeta/2`. Its trace is zero by determinant one
and continuity of the small branch. The composition y_B(V) is holomorphic
and maps into RF's independent boundary domain with room to spare.
The additional coarse-link reader is N_1(owner), contained in the already
paid N_9 boundary-mask label. Every coefficient bound and reader survives
this substitution, including the enlarged N_13 local-vertex roots.

Therefore RC14 applies to the actual touching part of RC2 with U_out held
fixed. An outside-only kernel has all actual fine inputs fixed real, so
its mean and original compact normalizer stay fixed and that normalizer
is positive. Only its numerator varies with coarse V. These numerators and
outside Wilson/source weights are exponentials, so W_out^H is pointwise holomorphic
and nonzero for this FIXED real exterior. Combined with RC14 this proves
nonvanishing of the actual bare physical chart fibre on the matched tube.
No uniform price, small logarithmic norm or history ratio for W_out^H
follows; its exact normalization remains in RC2. No arbitrary deep link is
holomorphically moved with the lift, and no zero-free theorem for a rough complex-moved mean is asserted.

For Lambda empty, F_L=0, d_L=0, the empty determinant and zero-dimensional
Gaussian integral are one, and there are no primitives. Hence I_empty=1,
P_empty*=1 and H_(empty,Y)=0. RC2 gives the actual bare local density
w_epsilon(U_out;V), without any hard indicators. If the whole exterior has small coordinates, RC2a gives exp(-F(y)/sigma^2)
relative to h_N^n dy and the same physical fibre.
For Lambda=E, the outside-only field-free vertices still multiply the
regional prefactor; their sum restores the exact whole-torus SN phase.

At the same ambient torus, u and common parameters, fix an order of original
vertices, scalar indices, atom words and forest/cluster labels independent
of Lambda. A primitive reads all local
membership decisions in its stencil. Core matrix entries read every used
patch membership; their inverses and accretive determinant branches read
S_B. Producer b and E atoms carry their stipulated complete membership
readers. Thus every finite decorated coefficient with final reader Y is
identical whenever all original continuous data and region membership agree
on Y, with boundary values compared where defined. Gaussian integration
dimensions, active cuts and side patterns are
then identical as well. Normalized integration over unused modes adds one,
not a hidden exterior-dependent determinant.

All rearrangements are absolutely convergent at RC13. Passing to their
limits and the connected series preserves this canonical property:

    H_(Lambda,Y)=H_(Lambda',Y)
       whenever their actual data and membership agree on Y. (RC16)

This is coefficientwise local agreement on a common ambient construction.
It is not a bound on a ratio of regional integrals. Their full critical
phases, dimensions, determinants, outside-only factors and Haar reference
measures need their own matching before any such ratio estimate is claimed.

For a physically shrinking chart set r_a=sigma p, tau=c sigma p as in
SH, with the RECOMPUTED regional constants and
`0<c<=min(1/(16D),sqrt(a)/(8D sqrt(L_hat^2+a/64)))`.
This enforces RC8 whenever eta_bar<=a/128. Fix a positive rho<=bar_rho
at RF17's preliminary ceiling. The boundary and coarse choices are explicit:

    C_N=N''(bar_tau/2)/2,
    B_bd=1+Q_K+rho B_src+(1+rho)C_N bar_tau/2,
    k_y=min(1/2,1/(8A_G B_bd)),
    k_delta=1/(8A_G g_*(1+rho)),
    k_v=min(k_delta/9,k_y/(16c_y)),
    Y=k_y tau, zeta=Y/c_y, delta_*=eta=k_v tau.           (RC17)

N(0)=N'(0)=0 and its positive Taylor majorant gives N(Y)<=C_N Y^2 for
Y<=bar_tau/2. Therefore the boundary part of A_G F_bd is <=tau/8 and
the coarse part is <=tau/8. Also Y<=tau/2, delta_hat=9k_v tau and
eta<=zeta/16. RF17 is preserved by monotonicity as tau decreases; all fixed
curvature/analytic ceilings hold for sufficiently large u. This proves the
required nonempty common domain with a FIXED rho, rather than assuming
that a regional critical point fits the shrinking chart.

At fixed preliminary ceilings all RC6 constants stay fixed. SH3's
substitutions in RC12--RC13 cancel every sigma pole in h_s and h_tr.
For p->infinity and sigma p->0,

    epsilon<=C1 sigma^2+C2(1+p^(91D+2))exp(-a p^2/64).     (RC18)

Coarse and boundary-data Cauchy radii shrink with tau; their unscaled
finite-order derivatives retain the corresponding inverse-radius powers.
This is not fixed unscaled boundary/coarse analyticity or a consumer-history
identity. A fixed nonzero boundary displacement need not stay admissible
as u grows. Only the actual shrinking boundary family is covered; arbitrary
deep exterior values remain separately retained.

## 7. Remaining boundary and history interfaces

An arbitrary deterministic active shape is allowed, but its exterior data
must satisfy the stated small complex chart on B(Lambda) and its force
budget. Deep exterior fields remain in the exact separate physical outside factor.
This does not cover GC's general constrained-boundary minimum, arbitrary
rough collars, field-dependent histories, original G/Omega cuts or the
compact cut complement. It supplies no physical denominator ratio after
moving any of those indicators. Effective input identification, iteration,
continuum existence and a positive physical gap remain further targets.

No scientific numerics are used. The changed arguments are the active-only
Taylor majorant, exact outside/Haar bookkeeping, ambient membership/collar
counts and canonical agreement; the connected mechanism is SN's checked
one with all its constants recomputed. Earlier sources remain immutable.
Freeze order is mathematical source, compact provenance, then fresh
independent review. The [read manifest](checks/regional_chart_return_read_manifest.json)
records exact consumed ranges and identities; the
[receipt](checks/regional_chart_return_receipt.json) records author checks,
which are not independent proof. No new external theorem is imported.
Root owns Git, publication, shared fronts and audits.
