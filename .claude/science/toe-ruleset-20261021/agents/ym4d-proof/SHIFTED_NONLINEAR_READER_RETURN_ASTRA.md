# A connected return for the fixed original-coordinate chart

This unit combines the actual critical-field contour, including every side
and corner, with complete covariance-reader localization. It constructs a
connected logarithm for the **fixed original-a auxiliary chart**, on a fixed
positive joint source/coarse domain and for sufficiently large u. The whole
critical action, normalized compact kernel, Haar constant and full critical
colour determinant remain outside the small logarithm. Fresh independent
review is required.

Side flags and their parameters are part of primitive components before
any Gaussian forest is taken. Every side-dependent local vertex, flux,
Gaussian translation atom and covariance reader is retained. Only a singleton
nonlinear species with no side uses centered parity. The original cut
outside this chart, G/Omega, arbitrary histories, complementary integrals,
effective iteration and continuum limits are not closed. Four-dimensional
continuum existence and a positive physical mass gap remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Complete-reader logarithm and same-reference nonvanishing for the fixed original-a auxiliary chart, including every actual critical-field side/corner term."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Exact object and one common producer construction

Use the supplied finite-u Wilson/normalized paired-S4-prime model with
N>=2, D=N^2-1, odd L>=3, T>=2, real u>=N, sigma^2=N/u, and kappa in its
fixed admitted positive interval. There are n=m0 T^4 free links,
m0=3L^4+1, n0=Dm0, d=Dn. All colour, root, crossing and harmonic modes
remain; the pinned tree quotient has integrated gauge volume and Jacobian
one. In the original coordinates U_e(a)=exp(a_e)U0_e(V), set

    F=F_0+sum_p epsilon_p W_p,
    F_0=sigma^2[-log w_0-sum_e log j_N(a_e)],
    b=b_*(V,epsilon), F'(b)=0, K_*=F''(b), C=K_*^-1,
    D_a=product_e B_(r_a),
    Z_a=h_N^n integral_(D_a) exp[-F(a)/sigma^2] da.         (SN1)

The finite-t compact normalizer and Haar logarithm occur once inside F;
h_N occurs once outside. Negative complex edges use inverses. Only original
Wilson sources vary; t=kappa u stays fixed real. On complex data Z_a means
this fixed-coordinate analytic chart integral, not a complex hard predicate.

The needed producer sources are [FU](FINITE_U_CRITICAL_FIELD_ASTRA.md),
[NC](NONLINEAR_CHART_ACTIVITY_ASTRA.md),
[SC](SHIFTED_CHART_RETURN_ASTRA.md), and
[NR](NONLINEAR_READER_RETURN_ASTRA.md). The entire NR source and the NC
coefficient/mark/parity arguments were read. Their reviews are status
information, not proof premises. NR was under review at this unit's start;
its final review subsequently accepted the unchanged source. This note
checks and rebuilds its consumed interfaces before extending them.

The constructions may previously have used different R and radii. Here
choose ONE patch cover, ONE R, and ONE complete-reader FU atom family.
Recompute all bounds on that construction. Intersecting two scalar domains
would not identify two different lists of atoms. Original data are
`V_c=exp(v_c)Vbar_c`, max ||v_c||HS<eta, |epsilon_p|<rho, with center
curvature <=delta_*. Joint suprema use delta_hat=delta_*+8eta throughout.
A real delta_V is not substituted for this tube supremum.

## 2. Common row algebra, tail and radius order

Here is the consumed matrix library and its hypothesis check. Keep the
actual lift core P=sum_A chi_A K_A^-1 chi_A. Its entry envelope is
`sup|P(i,j)|<=(2/gamma)exp[-m d_1(X_i,X_j)]`, because the principal inverse
has that envelope and sum_A chi_A(i)chi_A(j)<=1. On the common tube Re P>=c0.
With the NR3--NR5 geometric constants

    g=(2n0/gamma)coth(m/4)^4,
    A_1=(2n0/gamma)sum_(z in Z^4)|z|_1 exp[-m|z|_1/2],
    theta=min(m/2,c0/(2A_1)), v_I=(2n0/c0)coth(theta/2)^4,
    a=c0/g^2, b_P=1/c0,                                  (SN2)

every principal P[I] has inverse G with absolute row/column sum <=v_I,
Re G>=a and ||G||<=b_P. Conjugation by exp(theta distance) changes each
endpoint sum by <=theta A_1<=c0/2, so the conjugated inverse has norm
<=2/c0; undo the weight and sum the geometric series. This holds on
arbitrary disconnected I and all tori. The constants are independent of R.

Write a_f for FU's fine-coordinate radius a; a in SN2 is instead the
precision bound. Set J=16^4, C_chi=16(1+sqrt(2J)), and use FU5's b_abs.
For an integer R>=4 let
`r_PC=exp(1)(2J C_chi*8*b_abs*g)/R`, as derived in FU6--FU8.
Choose the common R and FU Hessian budget exactly as follows:

    e_*=min(c0/8,1/(4v_I),a/(64v_I^2)),
    r_PC<=min(1/4,c0/(32p_PC),e_*/(4p_PC)),
    p_PC=exp(1)Jg, beta=(16R)^-4,
    d_H<=min(d_* of FU17,e_*/(4m_G^2)).                   (SN3)

The actual covariance is C=P+E with E=E_lift+T_crit, not only one tail.
FU's exact ordered inverse series and its marked product rule give
M_beta(E_lift)<=e_*/3 and M_beta(T_crit)<=e_*/3. Fix eps<=e_* bounding
their total M_beta, and the finite B_E obtained by adding FU10 and FU26
for their marked sums. Both use suprema of individual scalar entries on
the original joint domain. B_E may be large. R enlarges the fixed cover
and reduces beta; no earlier support rate is retained.

Set

    t=v_I eps<=1/4, t_E=v_I^2 eps/(1-t)<=a/48,
    ell=-(1/2)log(1-t), c_g=2b_P^2/a+b_P,
    c_*=c_g+t_E+1,
    A0=v_I/[2(1-t)], A2=v_I^2/[2(1-t)^2],
    K_m=A0+2A2(16/a+1), L_jet=max(1,sqrt(2exp(1)c_*)),
    L_hat=sqrt(2)L_jet.                                  (SN4)

The remaining positive-radius order is noncircular. After R, recompute
FU's m_G,A_G and all marked constants. Select preliminary positive ceilings
bar_tau<a_f/64 and bar_rho<=1, small enough to satisfy FU18 and the SN3
critical-tail cap. Fix r0<a_f/16 with bar_tau+r0<a_f/2. Compute the local
Cauchy/reader constants below at those CEILINGS. Choose r_a next. Only
then reduce the actual tau<=bar_tau, rho<=bar_rho and delta_*,eta by FU19.
All those restrictions still select the same actual b by FU uniqueness.
The coefficients on the smaller tube are bounded by the ceiling constants.
Run one FU iteration on the final domain and use those resulting atoms
everywhere. Ceiling majorants do not define a second covariance family.
The last step is to take u large; none of these radii depends on u,T.

## 3. Shifted local vertices with complete original readers

Let v denote original local vertices: the base Wilson term and its source
are ONE vertex (1+epsilon_p)W_p; each kernel and Haar vertex occurs once.
Put q=(8L^4+8)D, I0=15, s0=9^4, v0=9L^4+5, d0=v0 s0 and d1=q d0.
Each field stencil I_v has <=q scalar coordinates, and a scalar belongs
to <=I0 distinct original vertices. Let L_v be its whole-link stencil.
A connected root S_v of size <=s0 contains the stencil and every original
coarse/source datum. All local constants are for the actual finite-u
vacuum-subtracted vertices; the vacuum itself stays in SN1's phase.

Use f(t)=H(1-t/a_f)^(-q), the FU/NC Cauchy majorant. At fixed u define

    R_v(z)=sigma^-2[F_v(b+sigma z)-F_v(b)
                  -sigma F_v'(b)z-sigma^2 F_v''(b)[z,z]/2]. (SN5)

The first jets are subtracted individually; only their SUM is zero.
Field-free vertices have R_v=0 and are not primitive species.
Expand first at fine field zero, then substitute b's FU atoms. NC5's
homogeneous coefficient families j_(v,l;S), l>=3, have weighted root and
marked masses bounded by

    A_l=(1+bar_rho)exp(beta s0)f^(l)(bar_tau)/l!,
    B_l=d0(1+bar_rho)exp(beta s0)
                   [f^(l)(bar_tau)+bar_tau f^(l+1)(bar_tau)]/l!. (SN6)

The root mark costs d0. A mark in an attached b chooses one substituted
factor and costs its full marked norm <=bar_tau. Finite slot incidence
pays the sum over original vertices. This is the direct Cauchy/attachment
proof; b is a solved original-data function, not independent new data.

For actual tau>0 with V_beta(b)<=tau write each scalar atom as
b_(i;S)=tau p_(i;S). The p family has component-root norm <=1 and full
marked norm <=1. This fixed normalization is only analytic bookkeeping;
all original readers remain attached. Let J subset L_v be a proposed
side pattern and t_e in [0,1] for e in J. Define

    chi_v^J=product_(e in L_v\J)1_(|y_e|<=p), p=r_a/sigma,
    f_v^J(y,t)=chi_v^J[exp(-R_v(y-t m_J))-1], m=b/sigma.   (SN7)

In an actual term each J-coordinate is on its full colour sphere |y_e|=p.
No assertion about f_v^J on arbitrary large J-coordinates is needed.
Its translated R is expanded in the p atoms as well as in its center atoms.
Every such coefficient carries its original root and all attachments.

Here are explicit uniform envelopes for every pattern. Assume
2(r_a+tau)<=r0. Translation of a degree-l monomial has at most 2^l choices,
counting binomial multiplicities. With |sigma y_i|<=r_a and each selected
shift amplitude <=tau, each choice obeys the cubic AM--GM estimate

    sigma^(l-2)|product of l field/shift factors|
        <=sigma(r_a+tau)^(l-3) P_3^J(v,y),
    P_3^J=sum_(i in I_v)(|y_i|+(tau/sigma)1_(link(i) in J))^3.

To verify it divide every factor by (r_a+tau)/sigma, use weighted AM--GM
on its cube, and use that the resulting average lies in [0,1]. Factors
p_(i;S) remain in the coefficient family. Since
`2^l(r_a+tau)^(l-3)=8[2(r_a+tau)]^(l-3)`, Taylor's integral remainder
gives the root bound A_sh below. Marking a translated p factor has at
most l choices. The sum with l is bounded by three times the third
remainder plus its radius derivative. Root and center marks are already
in B_l; d1 safely also overcounts the translated slot incidences. Hence

    A_sh=8(1+bar_rho)exp(beta s0)f'''(bar_tau+r0)/6,
    B_sh=8d1(1+bar_rho)exp(beta s0)
          [4f'''(bar_tau+r0)+(bar_tau+r0)f''''(bar_tau+r0)]/6. (SN8)

There exist individual positive reader families a_(v,J;S) with these
root and marked bounds and with
`|R_(v,J;S)|<=sigma P_3^J a_(v,J;S)` on the mixed chart. For clarity,
the marked sum in B_sh ranges over all v and all labels containing its
fixed mark, but one fixed choice of pattern for each v. Below we explicitly
pay for summing all patterns. Supremum is taken before the atom sums and
includes all t_e in [0,1].

Let A>=max(1,A_sh,A3_base,A4_base), with the latter constants from NC7 at
the same ceilings. Union-convolve the a family and set
`w_(v,J)=sum_(k>=1)a_(v,J)^(*k)/[k(2A)^(k-1)]`. Expanding the Mayer
exponential and using
`Y^(k-1)/(k-1)!<=(2A)^(-(k-1))exp(2AY)` gives

    |f_(v,J;S)|<=chi_v^J sigma P_3^J exp(2A sigma P_3^J)w_(v,J;S).

The weighted root mass is <=2A_sh; a mark in one of k factors cancels
the denominator k and gives <=2B_sh. There are at most K_pat=2^q patterns,
so valid simultaneous root/marked budgets are

    W0=2K_pat A_sh,               W1=2K_pat B_sh.          (SN9)

This overcounts inadmissible pattern choices only in positive bounds.
For J=empty the exact centered parity families of NC12--NC15 are kept,
with budgets E0,E1 computed at the same ceilings. Their coefficientwise
even part costs sigma^2(P_4+P_3^2), at fixed actual u, b and covariance.
The larger A bounds their regulator too. No parity is assigned to J!=empty.

## 4. Final chart/shift choice and exact flagged expansion

Choose r_a>0 below r0/8 and every required fine chart margin, with

    eta_bar=4A I0 r_a(1+r_a)<=a/128.                     (SN10)

The ceiling constants were fixed first, so this is a positive choice.
Then take actual tau>0 small enough that

    tau<=min(bar_tau,r_a/(16D)), s_*=D tau,
    C_sh=L_hat^2+2eta_bar,
    C_sh s_*^2<=a r_a^2/64,                             (SN11)

and choose rho,delta_*,eta by the already checked FU conditions, including
SN3's critical Hessian budget. In particular V_beta(b)<=tau on the joint
tube and the critical-tail construction is the one common construction
from section 2. All radii remain positive. On every product translation
sweep, `max|b_i|+max|sigma(y_i-t_i m_i)|<=r_a+2D tau<a_f`.
Thus the entire contour, not merely its endpoints, stays in the proved
fine analytic chart. The original good/cut margins are imposed separately
only when placing the real auxiliary chart inside them.

Set

    P_*=h_N^n(2pi sigma^2)^(d/2)det(K_*)^-1/2 exp[-F(b)/sigma^2].

The determinant branch is fixed by the accretive covariance. Substitution
onto the translated real chain, followed by the ball divergence identity,
gives exactly

    Z_a/P_*=sum_(H subset links)(-1)^|H| integral_[0,1]^H
       integral_(sphere_p^H x B_p^(H^c))
           product_(e in H)(m_e.n_e) g_C(y-tm_H)
                              product_v[1+W_v(y-tm_H)] dS_H dy_Hc dt_H. (SN12)

Here W_v=exp(-R_v)-1. The sign follows from
`d/dt integral_B F(y-tm)=-integral_sphere(m.n)F(y-tm)`.
Each side has its own real outward normal, entire D-colour sphere and t
integral. Tensoring gives every corner. Translation has Jacobian one.
The sigma^d factor together with b/sigma, surface sigma^(-(D-1)) and
bulk sigma^-D scalings reduces to the original-coordinate top form;
no flux scale or Haar/kernel factor is lost.

Expand the distinct original vertices, and write remaining balls as one
minus exterior failures. Retain balls on every selected vertex's non-side
slots. The exact families are selected vertices W, side links H and bad
links B, with B disjoint from H union F(W), F(W)=union_(v in W)L_v.
For each selected v its pattern is REQUIRED to equal J_v=H intersect L_v.
The active whole-link set is F(W) union H union B. All other Gaussian
coordinates marginalize exactly, with principal covariance C[I], not
inverse principal precision. The shift is supported on H subset I, so
the Gaussian marginal identity extends to y_I-tm_H by entire analyticity
in the active arguments. No inactive mean or volume-wide force price is
introduced. The active measure has spheres on H,
exteriors on B, and balls on F(W)\H. Thus no vertex Taylor series is used
on an exterior bad coordinate. At empty W,H,B the normalized marginal is
exactly one; there is no residual vacuum.

## 5. Primitive components before the Gaussian forest

A nonlinear primitive is (v,J,S), one actual reader atom of f_v^J. A bad
primitive is a link e with signed exterior indicator. A side primitive
is (e,alpha,S), one flux atom `-b_(e alpha;S)n_alpha/sigma`, with its
sphere and its single parameter t_e. This absorbs SN12's (-1)^|H|;
no second side sign is applied. A side link and an original vertex
are each selected at most once; bad/side/vertex compatibility and
J_v=H intersect L_v are imposed exactly.

Let x_v be the original owner block, with S_v subset N_4(x_v), and X_e
the owner of link e. Enlarge the nonlinear primitive reader by
Q_v=N_(16R)(x_v), and the side/bad reader by Q_e=N_(16R)(X_e). For a side the original flux reader S is retained
as well. The actual patch geometry gives

    |Q|<=s_c=(32R+1)^4, d_c=(9L^4+5)s_c, d_h=m0 s_c.     (SN13)

These collars contain every core patch reader touching their field stencils,
including the bounded whole-torus case. Partition the enlarged primitive
readers into overlap-connected components B_j, retaining every primitive
and side flag, not just their union S_j. Their field sets I_j are disjoint,
and P[I] is block diagonal by j. Each inverse-core block and determinant
reads S_j, charged once, not once per inverse factor.

The pattern condition is local WITHIN these components. If e in L_v is
a side, Q_e and the collar of v meet, so they belong to the same component.
Conversely a side in a different component cannot change v's pattern.
Thus both the presence and absence requirements in J_v=H intersect L_v
are preserved when components are separated. Components carry one shared
t_e for every side used by their vertices; t is not copied per vertex.

Their unique partition is invertible: internally admissible components
with disjoint S_j reconstruct one admissible primitive family. This is
why side flags cannot be added independently after the forest. A positive
count may later drop compatibility or repeat formal objects, but no field
moment is asserted for those fictitious families.

## 6. Mixed density/translation jets and marked readers

For a fixed collection of components, mask only E entries between different
I_j by independent pair variables s_jk, leaving within-block E unchanged.
For |s_jk|<2, Re(P[I]+E_I(s))>=3c0/4 and its norm is <=5g/4;
its inverse therefore has Hermitian part >=12a/25. The pair polydisc is
analytic. Fixed spheres, bounded vertex slots and Gaussian domination on
exterior coordinates justify holomorphy of its integrated functions.
All quantitative bounds use real forest masks with |s_jk|<=1. Side flags, t, b and all primitive functions remain fixed under
this artificial covariance interpolation; no stationarity for its
intermediate matrices is asserted or needed.

Put G=P[I]^-1. The normalized density ratio is exactly

    g_(P[I]+E_I(s))(x)=g_(P[I])(x)exp L_I(x),
    L_I=sum_(k>=1)(-1)^k Tr[(GE_I(s))^k]/(2k)
                +(1/2)sum_(k>=1)(-1)^(k-1)x^T(GE_I(s))^kGx. (SN14)

This is the full determinant logarithm and inverse correction. Expand E
into BOTH original reader tails and the exponential into ordered lists
omega with its list factorial. G factors split over I_j, so all their
readers lie in the fixed S_j. Row algebra gives loop bound |I|ell and
chain bound t_E||x||^2/2. A reader mark x_0 in an E occurrence has pin

    d_(x_0)(i)=sum_(j,a:x_0 in S_a)exp(beta|S_a|)sup|E_a(i,j)|,
    D_(x_0)(I)=sum_(i in I)d_(x_0)(i), sum_i d_(x_0)(i)<=B_E.

A marked loop cancels its 1/k and costs A0D; a marked chain splits into
two geometric resolvents and costs A2D||x||^2. Young's inequality and
Gaussian absorption give, for each scalar multiindex nu,

    sum_omega weighted sup|partial^nu g_omega(y)|
       <=A_I exp[-a||y||^2/8] L_jet^|nu| product_i sqrt(nu_i!),
    A_I=(b_P/(2pi))^(|I|/2)exp(|I|ell).                  (SN15)

The E-reader-marked sum has the extra factor K_mD_(x_0)(I). Optimized
Cauchy radii sqrt(nu_i/(2c_*)) prove the factorials; no component-total
factorial replaces them. These are precisely NR15--NR20, with SN2--SN4
checking every hypothesis for the one common critical covariance.

Now expand only the density translation y-tm_H. If k is supported on
side coordinates, then

    sqrt((nu_i+k_i)!)<=2^((nu_i+k_i)/2)sqrt(nu_i!)sqrt(k_i!).

This follows from the binomial coefficient <=2^(nu_i+k_i). Dividing by
the translation Taylor k_i! leaves the entire series
`S(x)=sum_(k>=0)x^k/sqrt(k!)`. Cauchy--Schwarz with weights 2^-k gives
S(x)<=sqrt(2)exp(x^2) and
S'(x)<=sqrt(2)sqrt(1+2x^2)exp(x^2). Expand every m atom with its complete
original reader. Scalar component-root sums are <=tau; their link l1 sum
is <=s_*=D tau. Therefore the mixed list/shift coefficient sum is bounded by

    A_I exp[-a||y||^2/8]
       L_hat^|nu| product_i sqrt(nu_i!)
       2^(D|H|/2)exp[L_hat^2(s_*/sigma)^2|H|].             (SN16)

The E-reader mark keeps the same K_mD factor. This includes all mixed
orders and all cross terms of nu and k. It does not invoke SC22, which
had no Gaussian forest legs.

For a mark x_0 in a Gaussian translation b occurrence, set

    d^b_(x_0)(e)=sum_(alpha,S:x_0 in S)
                          exp(beta|S|)sup|b_(e alpha;S)|,
    sum_e d^b_(x_0)(e)<=tau,
    s=s_*/sigma, K_tr=(L_hat/sigma)(1+sqrt(2)L_hat s).     (SN17)

Differentiating S's positive series bounds that marked mixed jet by SN16
times `K_tr sum_(e in H)d^b_(x_0)(e)`. All nu factorials are unchanged.
Flux and nonlinear-argument marks are already primitive-reader marks;
SN17 counts precisely the additional Gaussian-translation readers.

## 7. Integrated primitive weights, including true side rarity

For distinct original vertices, their shifted regulator obeys
`product exp(2A sigma P_3^J)<=exp[eta_bar sum_i(|y_i|+
(tau/sigma)1_(link(i) in H))^2]`. The bound follows from
sigma(|y_i|+tau/sigma)<=r_a+tau and the incidence I0. The same eta_bar
bounds the unshifted even regulator sigma P_3+sigma^2 P_4. Hence the
regulator costs at most
`exp[2eta_bar||y||^2+2eta_bar(s_*/sigma)^2|H|]`.

Extract one cubic polynomial per selected standard vertex; repeated
powers of one Mayer exponential were already absorbed in that regulator.
For a parity singleton use P_4+P_3^2<=P_4+qP_6. Original distinctness
bounds every scalar exponent by 6I0=90. Shifted powers are bounded by
`(1+s)^(90D|H|)` times polynomials in 1+|y_i|. The explicit finite constant

    M90=2^90 max(1,(2880/a)^45)

bounds `(1+x)^j exp(-a x^2/64)` for 0<=j<=90: use
1+x<=2max(1,x) and maximize x^j exp(-a x^2/64).
There are at most q polynomial coordinates per vertex. Together with
2eta_bar<=a/64 this leaves at least exp(-3a||y||^2/32) from SN16.
Retain the weaker exp(-a||y||^2/16), and define

    K_g=max(1,exp(ell)sqrt(8b_P/a)),
    C_V=q(1+q)(K_g M90)^q,
    q_h=K_g^D 2^(D/2)exp[-a p^2/32],
    A_D=(b_P/(2pi))^(D/2)exp(D ell),
    Q_s=A_D 2^(D/2)omega_D p^(D-1) sigma^-1
                              (1+s)^(90D)exp[-a p^2/64]. (SN18)

A hard coordinate has no selected vertex slot, so the exponential Markov
bound under the scalar variance-8/a product Gaussian gives q_h. A side
retains its sphere area omega_D p^(D-1), flux sigma^-1, and all colours.
Its shift exponential is at most exp(ap^2/64) by SN11, while its retained
Gaussian decay is exp(-ap^2/16). The looser exp(-ap^2/64) in Q_s therefore
has genuine slack; every displayed polynomial cost is paid. Bulk active
normalizers cost K_g per scalar and are assigned at most q times per
vertex. No unused-mode determinant appears.

For every admissible primitive family, the integrated mixed density-jet
sum, including t_H integrals of volume one, is bounded by

    L_hat^|nu| product_i sqrt(nu_i!) product_o a_o,
    a_(v,J,S)=C_V sigma w_(v,J;S), a_bad,e=q_h,
    a_side,(e,alpha,S)=Q_s sup|b_(e alpha;S)|.             (SN19)

At a fixed primitive decoration, secondary density E and Gaussian-translation
decorations are summed with their individual beta reader weights as in
SN15--SN17. Base primitive weights remain in a_o; their support weights
are charged in SN22. Union weights are bounded by the product weights.
The E-reader-marked version has K_mD_(x_0)(I). The translation
reader-marked version has the additional SN17 pin, supported ONLY on
actual side links. The normal factors are bounded by one. Sphere
coordinates never receive independent component cutoffs, and a side
measure occurs once even if several vertices use its link.

For a single nonlinear primitive with no side, the signed integral can
use `a_even=C_V sigma^2 e_(v,S)`. Each density list is even under y->-y;
there is no translation and its ball is symmetric, so its odd part
integrates to zero coefficientwise at fixed u. A pattern J!=empty cannot
be such a singleton: it requires its side primitive. A singleton side
uses SN19 with no parity improvement.

## 8. Exact forests and complete reader supports

Differentiate in an independent component pair. Both determinant and
inverse give the heat identity

    partial_(s_jk) integral Phi g_(C_I(s))(y-tm_H)
       =sum_(i in I_j,l in I_k) E(i,l)
                    integral Phi partial_i partial_l g_(C_I(s))(y-tm_H). (SN20)

Phi includes every flagged vertex, fixed ball/exterior, normal flux and
sphere/t measure. None is differentiated. The two symmetric off-block
entries cancel the heat identity's 1/2. At a disconnected forest mask,
the density and all mixed measures/vertices factor over the forest's
component unions. Each vertex's side pattern and shared t variables were
already internal to its primitive component. Nonlocal original-data
coefficients are retained for subsequent reader localization.

Use independent-pair derivatives and THEN evaluate at the path-minimum
forest mask. The finite forest identity follows by assigning a pair of
monomial degree k a clock with distribution t^k and partitioning by the
unique maximum spanning forest. Conditioning its tree clocks gives the
path minima and derivative factors. Analyticity on the radius-two pair
polydisc permits passage from monomials. No derivative of a minimum or
of an original-reader weakening monomial is substituted here.

A raw connected species consists of a nonempty admissible collection of
primitive components with disjoint base supports S_j, a tree on them,
scalar E endpoints/atoms on its edges, a density list omega, and a
Gaussian-translation Taylor/critical-field decoration. Its coefficient
is the corresponding exact mixed integral from SN12 and SN20. Its support is

    B_z=union_j S_j,
    S_z=B_z union (tree E readers) union (density E readers)
                                      union (translation b readers). (SN21)

Every S_z is connected. Tree E labels join the connected S_j; each density
atom has an active endpoint; each translation b atom is anchored at a
side already in B_z. All fields and every original reader, including
remote diagonal covariance readers, are present. The inverse-core block
reader S_j is charged once. Absolute convergence in SN16--SN19 justifies
these decompositions at each finite forest order.

The raw gas has compatibility B_z disjoint. This preserves primitive
uniqueness, bad/side compatibility AND the presence/absence side patterns.
It is not merely field exclusion. Full S_z can overlap and will be regrouped
exactly after their marked bounds are proved. There is no degree-zero
raw species because the empty normalized marginal is one.

## 9. Primitive, attachment and new marked-translation budgets

Take delta=beta/8, beta1=beta-delta, beta2=beta-2delta. Primitive weighted
root budgets, including one core collar per primitive, are

    h_v=C_V sigma exp(beta s_c)(W1+d_c W0),
    h_2=C_V sigma^2 exp(beta s_c)(E1+d_c E0),
    h_h=d_h exp(beta s_c)q_h,
    h_s=Q_s exp(beta s_c)[tau+d_h D tau],
    h_0=h_v+h_h, h=h_0+h_s.                              (SN22)

A flux-reader mark costs the full marked b norm tau. A collar mark costs
d_h times the link component sum D tau. Vertex shifted-argument marks
are already in W1. Every h_s has its explicit rare side Q_s; h_s is not
assumed comparable to sigma.

If h<=delta, components satisfy
`sup_x sum_(B:x in S_B) exp(beta1|S_B|)u_B<=h`,
u_B=product_(o in B)a_o. Root an overlap tree at a primitive whose
reader contains x. The recursion `T_o=v_o exp(sum_(o' overlaps o)T_o')`
has supersolution `a_o exp(beta|S_o|)`, since its neighbor sum is at most
h|S_o|. This proves the bound without using moments of repeated formal
vertices. Admissibility is relaxed only in this positive count.

At rate beta2 use the scalar-coordinate Gaussian attachment recursion.
With an incoming leg i at B, allocate k_j unordered child legs to each
scalar j. The multinomial gives 1/k_j!, and SN19 gives
sqrt((k_j+1_(j=i))!). Thus H0(y)=sum y^k/sqrt(k!) and
H1(y)=sum sqrt((k+1)!)y^k/k! appear, with
`y_j=L_hat^2 sum_(B',l in I_B') e_jl T(B',l)` and
`e_jl=sum_a exp(beta|S_a|)sup|E_a(j,l)|`.
Their bounds for y<=1/2 are H0<=exp(2y), H1<=exp(4y).
The supersolution `T(B,i)<=u_B exp(beta1|S_B|)` is stable if

    h<=h_c:=min(delta/2,1/[4(1+L_hat^2 eps)],
                             delta/[8n0(1+L_hat^2 eps)]). (SN23)

Indeed each fixed scalar l is contained in components of total weight <=h,
so y_j<=L_hat^2 eps h, and |I_B|<=n0|S_B|. The attachment exponent is
linear in |S_B| and is paid by the second delta. The no-incoming root has
the same supersolution. This independently checks NR28--NR30 with the
new mixed-jet constant; no factorial of all legs on B is used.

Three ordinary raw-reader marks work exactly with these checked bounds:
a base mark costs h; a density E mark costs K_m B_E h by its scalar pin;
a marked tree E edge splits into two rooted incoming-leg subtrees and
costs at most L_hat^2 B_E h^2. The unoriented ordering factor is 1/2,
so replacing it by one is safe. All scalar colours are inside eps and B_E.

The fourth mark, in a Gaussian-translation b, needs a separate argument.
Using the generic h bound for it would introduce unnecessary inverse
powers of sigma without a rare witness. Instead root at its ACTUAL side
primitive. For fixed marked box x_0, give a side primitive o=(e,alpha,S)
the additional weight `K_tr d^b_(x_0)(e)`. Its weighted total is bounded by

    h_tr=K_tr Q_s exp(beta s_c) (D tau)tau.               (SN24)

This follows by summing flux atoms at e (<=D tau), then summing
`d^b_(x_0)(e)` over e (<=tau). The extra translation reader is paid by its
own beta weight; its endpoint belongs to the side's base support.

Here is the precise transport of that root through both positive tree
sums. In the primitive overlap-tree recursion, replace the activity of
the distinguished root primitive by its marked weight, leaving every
child ordinary. The already bounded child exponential costs at most
exp(delta|S_o|), so its root norm is bounded by that marked primitive's
beta-weighted sum. For the Gaussian tree, root at the component containing
this marked primitive. Its child bound costs at most the second support
margin; the remaining sum is just the preceding marked component sum.
Equivalently all factors are linear in their distinguished root activity.
Summing possible marked occurrences is an overcount of a union mark,
and proves the raw translation-reader bound h_tr. No pin is rooted at an
unrelated weak vertex. This argument is a positive counting identity,
not factorization of a coupled Gaussian integral.

Writing C0=1+K_m B_E, the initial complete-reader raw bound is therefore

    ||a_raw||_(beta2,mark) <= C0 h+L_hat^2 B_E h^2+h_tr.   (SN25)

Every mark in SN21 is now paid, including flux, shifted nonlinear argument,
Gaussian translation, determinant loops and both covariance tails.

## 10. Parity only without sides, and a genuinely rare side norm

Assume h_0<=h_c/2 and h_s<=h_c/2. For species with NO side, use the
singleton even bound h_2 or hard bound h_h. For their primitive degree
>=2, multiply only the ordinary primitive amplitudes by h_c/h_0, holding
u,b,C and every regulator fixed. The positive bounds still hold at h_c;
undoing the degree-two multiplier gives

    epsilon_0=C0(h_2+h_h)+[C0/h_c+L_hat^2 B_E]h_0^2.      (SN26)

If h_0=0 use zero for this contribution. This is fixed-u homogeneity of
the positive counting weights. The parity belongs only to signed centered
singletons; it is not parity of an absolute shifted Mayer moment.

For all species having at least one side, multiply ONLY side primitive
amplitudes by t_s=h_c/(2h_s)>=1. The ordinary budget stays <=h_c, and
h_tr is multiplied by exactly t_s because its distinguished root is a
side primitive. Every actual side-containing species is multiplied by
at least t_s. Apply SN25 and undo this factor to obtain

    epsilon_side=2(C0+L_hat^2 B_E h_c)h_s+h_tr,
    epsilon=epsilon_0+epsilon_side.                       (SN27)

For h_s=0 there is no side and h_tr=0. This proves a rare norm for the
ENTIRE side-containing raw family, not just a rare pointwise flux. In
particular no side singleton has received a fictitious sigma^2 parity
improvement. The fictitious multiplier does not vary u or b or the side
location; it rescales already defined primitive weights only.

For the fixed prior choices, h_v=O(sigma), h_2=O(sigma^2), while h_h,
h_s and h_tr are fixed polynomials in sigma^-1 times exp(-c/sigma^2).
Consequently, for all sufficiently large u, the explicit conditions

    sigma<=1, q_h<=1, h_0<=h_c/2, h_s<=h_c/2,
    epsilon<=delta/2                                     (SN28)

hold uniformly in T and on the common original-data product domain.
In that regime epsilon is bounded by
`C_1 sigma^2+C_2(1+sigma^-M)exp[-a r_a^2/(64sigma^2)]`
with M=91D+2 and finite C_1,C_2 fixed before u,T. These may be enormous;
no numerical threshold or continuum scaling is asserted.

## 11. Exact full-reader regrouping and the fixed-chart logarithm

At finite volume SN27 makes the absolute raw activity sum finite. Its gas
still imposes base B_z disjointness. For each such family join species
whose complete S_z overlap, retaining the old base compatibility inside
each connected subfamily Gamma. Assign it activity product_(z in Gamma)a_z
and full support S_Gamma=union S_z. Every raw family has one such connected
partition. Conversely, reader-disjoint Gamma reconstruct one original
base-compatible family, since reader disjointness implies base disjointness
across them. All side-pattern constraints were already preserved by base
compatibility. This is an exact regrouping of SN12, not a change of model.

Spend a third delta from beta2 to beta3=beta-3delta. The rooted overlap
tree recursion for raw species has supersolution
`sup|a_z|exp(beta2|S_z|)` because its neighbor sum is <=epsilon|S_z|
<=delta|S_z|. Therefore the regrouped gas norm at beta3 is <=epsilon.
For its connected logarithm spend the fourth delta, leaving mu=beta/2.
The absolute alternating connected graph coefficient is bounded by its
spanning-tree count: partition graphs by a fixed-order Kruskal minimum
tree, whose allowed extra edges form a Boolean interval; the alternating
sum in each interval is zero or has modulus one. The same rooted
exponential recursion is stable with the beta3 budget. It proves

    Z_a/P_*=exp[sum_(connected original-block Y) H_Y(V_Y,epsilon_Y)],
    sup_x sum_(Y contains x)exp(mu|Y|)sup|H_Y|<=epsilon,
    mu=beta/2=1/[2(16R)^4]>0.                             (SN29)

Each coefficient retains all original readers in SN21 and is holomorphic
on their projected joint domain. The graph identity holds near zero common
activity multiplier; absolute convergence throughout its unit disc extends
it to one. Finite atom/list truncations followed by the positive bounds
justify every regrouping, derivative, mixed contour integral and limit.
Thus SN29 proves nonvanishing before assigning a logarithm branch.

All four margins beta/8 were spent separately: primitive components,
scalar Gaussian attachments, complete-reader regrouping and the logarithm.
Translation and shifted-vertex marks used their actual beta atom budgets;
no unchanged RD two-unit margin or larger FR rate is imported. The branch
of the small logarithm tends to zero as u grows on the specified regime.

Finally P_* is holomorphic and nonzero on the common FU domain: its critical
action exponential, positive Haar constant, sigma power and accretive
Gaussian determinant branch are all nonzero. Therefore

    Z_a=h_N^n(2pi sigma^2)^(d/2)det(K_*)^-1/2
           exp[-F(b)/sigma^2] exp[sum_Y H_Y] !=0.         (SN30)

This is the fixed original-a auxiliary chart and its SAME critical
reference, not the centered contour substituted for it. The entire
finite-u critical action, source vacuum, compact normalizer, Haar factors
and full d-dimensional determinant remain. The small norm is for the last
logarithm only; it does not bound or cancel the extensive prefactor.

## 12. Remaining interfaces and provenance boundary

SN30 closes the fixed auxiliary-chart return specified in SN1. It does
not identify that chart with the entire original-cut transform. Outside
this chart, retained G/Omega conditions, arbitrary hard histories and
any other failure event remain exact complementary terms. No such
nonholomorphic indicator was moved through the complex contour. Their
same-component ratios and normalizers still need their own theorems.
Effective-level identification, multiscale iteration, continuum existence
and a positive physical continuum gap are further open targets; the
one-step Gaussian precision here is not an interacting mass gap.

SC supplied the exact actual contour and the warning to keep nonlinear
field-slot cuts; NR supplied the actual covariance-tail library and the
per-coordinate attachment mechanism. NC supplied the original vertex
and parity coefficient families. The new steps are the common construction,
flag-compatible primitive organization, shifted reader envelopes, mixed
translation/forest jets, marked side-root transport and rare side-family
rescaling. The preceding argument rebuilds the changed steps and checks
the consumed interfaces. Review verdicts are not mathematical premises.

Bałaban's constructions and Dimock's expositions are the constructive
antecedents. No new external theorem is imported by citation and no
numerical experiment is used. All earlier source/package bytes remain
immutable. The source is frozen before its compact
[read manifest](checks/shifted_nonlinear_reader_return_read_manifest.json)
and [author receipt](checks/shifted_nonlinear_reader_return_receipt.json).
Root commissions a fresh hostile review and owns PR #10114 integration,
Git, shared fronts and all audit operations. This author issues no
independent verdict or retained-grade status.
