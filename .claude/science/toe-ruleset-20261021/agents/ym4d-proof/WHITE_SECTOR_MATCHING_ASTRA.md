# Matching the original white cube to the original-coordinate chart

This constructs a connected logarithm of the ratio of two ACTUAL bare-step
integrals: SA's unchanged source-free white scalar cube and RC's product of
original-a Hilbert--Schmidt balls. The coarse field is real and fixed while
the original Wilson sources range over a fixed positive complex polydisc.
The comparison keeps the full physical critical prefactor until its exact
cancellation. Its generally extensive action and determinant are not error
terms. The conclusion is a small complete-reader logarithm, not an
exponentially rare bound on that entire logarithm.

Bałaban's constructive localization and Dimock's expositions are the
antecedents. The needed mathematical libraries are [SA](COVARIANT_SOURCE_ACTIVITY_ASTRA.md),
the corrected [FR](FIXED_SOURCE_RADIUS_ASTRA.md),
[RF](REGIONAL_CRITICAL_FIELD_ASTRA.md), and
[RC](REGIONAL_CHART_RETURN_ASTRA.md). Their source arguments, not reviewer
verdicts or author diagnostics, are used. A fresh independent review of this
new matching is required. No predecessor is modified.

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

## 1. The two integrals and their original coordinates

Fix N>=2, odd L>=3, coarse side T>=2, u>=N, and the admitted compact
positive kappa interval. Let D=N^2-1, m0=3L^4+1, n=m0 T^4,
d=Dn, n0=D m0 and sigma^2=N/u. Use the SAME pinned internal block trees,
free positive whole links E, HS-orthonormal real scalar basis and lift U0(V)
as SA1--SA3 and RF1. All colours, root, crossing and harmonic degrees remain.
The integrated nonroot gauge Haar volume and tree-change Jacobian are one.
No new gauge slice or mode projection is made.

For real coarse V put delta_V=max_P ||I-V_P||op and choose a ceiling
delta>=delta_V. Coefficient suprema over coarse data mean the real class
delta_V<=delta, as well as the stated original-source polydisc. Arbitrary
compatible holonomy is allowed; the links need not be close to I. The actual phase is

    U_e(a)=exp(a_e)U0_e(V),
    F_epsilon(a)=sigma^2[-log w_epsilon(U(a),V)
                                      -sum_(e in E)log j_N(a_e)],
    F_epsilon=F_0+sum_p epsilon_p W_p,
    W_p=tr(2I-U_p-U_p^-1)/2.                              (WS1)

Here w contains every original paired-word kernel with t=kappa u FIXED,
its field-dependent compact normalizer, and the original Wilson factors.
Negative edges continue by inverse, and transposes are bilinear. The Haar
density h_N j_N(a_e) occurs once per retained link. The actual lift
Hessian K_b=F_0''(0) includes the finite-t spread and N^2/(6u) Haar term.
It is neither a tree Hessian nor a physical continuum mass operator.

Let b_epsilon be the actual small critical point of WS1 and put

    K_epsilon=F_epsilon''(b_epsilon),
    b_0=b_epsilon|_(epsilon=0), K_0=F_0''(b_0),
    C_0=K_0^(-1/2), T_0=C_0^-1=K_0 C_0,
    Omega={a=b_0+sigma C_0 w: w in [-p,p]^d}.             (WS2)

Thus C_0 is the SOURCE-FREE CRITICAL inverse square root. It is not
K_b^(-1/2), a critical covariance, or a collection of independent colour
square roots. Omega is frozen as epsilon varies. It is the original SA15
scalar cube, also used in IC21 and GC7; it is not a white HS ball.
Throughout p is the original p_Omega. If it is already fixed, the
conditions below are tested on that same p; no replacement cutoff is inferred.

Write D_a=product_(e in E)B_(r_a), with the original-a HS radius r_a. Define

    Z_Omega=h_N^n int_Omega exp(-F_epsilon(a)/sigma^2) da,
    I_a=h_N^n int_(D_a) exp(-F_epsilon(a)/sigma^2) da.     (WS3)

All bounds below include the domain conditions in sections 3 and 7.
For the original-event interpretation retain SA30:
with A_box=sqrt(D)[C_b delta+sigma p M_C], require
A_box<r_ch, delta+4A_box<delta_f and 5L A_box<eta_G, together with
its original threshold margins. Then Omega subset G subset chi_cut.
Choose r_a<=epsilon_1/8 as in SC3: an internal plaquette has defect
<=4r_a<epsilon_1, so D_a also lies in the original cut. The original cut
restricts block-interior PLAQUETTES, not every free link. Neither G nor
Omega is redefined. No inclusion between Omega and D_a is needed.

These are integrals of the full nonlinear density, with no retained history
inserted. The raw kernel vacuum, including the all-zero
4T^4 sigma^2 log Ntilde_(kappa u)(I), stays in F. Vacuum subtraction below
is only a device for bounding derivatives.

## 2. Complete readers for the actual half powers

Here is a conservative re-instantiation of SA7--SA14. It also fixes the
metric and colour counts needed before converting its R-box labels to
original blocks. RF5 supplies gamma I<=K_b<=B I, sup-distance range two,
and the actual radius-three entry readers. Set

    vK=n0*5^4, b_abs=vK B, b_s=max(1,gamma,b_abs), r0=8,
    m_w=(1/8)log(1+gamma/(4b_s)),
    Q_m=n0 coth(m_w/2)^4, S_m=2b_s exp(8m_w).             (WS4)

An entry has magnitude <=B and at most vK columns can meet a row; hence
b_abs bounds BOTH absolute scalar endpoint sums of individual envelopes.
Face-distance range eight is a conservative consequence of sup-range two.
The weighted perturbation has both endpoint bounds
(exp(8m_w)-1)2b_s<=gamma/2. The Schur inequality, followed by a Neumann
inverse, proves for every real principal compression and lambda>=0

    |(K_b,Omega+lambda)^-1(i,j)|
                    <=2 exp[-m_w d_1(X_i,X_j)]/(gamma+lambda).

The periodic distance sum is bounded by its Z^4 sum Q_m. No operator-decay
assertion alone is used as a reader norm.

Choose ONE integer R>=8, before volume, sources and final radii, large enough
for the white residual bound below AND RF16's stronger patch/tail bound.
Partition the coarse torus into product R-boxes with sides between R and
2R, taking one interval in a direction shorter than R. The two constructions
use this same numerical R but have different explicitly retained atom
families. For a white box q let Omega_q=N_R(q), and enlarge its full reader
to D_q=N_(R+8)(q), filled by R-boxes. Each contains at most s=9^4 boxes and
each box belongs to at most J=9^4 such labels. Indeed its one-dimensional
extent is <=2R+2(R+8)<=6R; at most eight partition intervals intersect it.
The reverse incidence obeys the same count. Periodic identifications reduce
counts. For T<R the one reader is the whole torus.

Assign each local K_ij the complete reader N_3(X_i) union N_3(X_j).
Principal entries inside Omega_q read N_(R+3)(q); a residual endpoint is
within sup-distance two of an inside index, so its entry reader is inside
N_(R+5)(q). Thus D_q contains every original V reader and every endpoint.
The enlargement does not discard or truncate an inverse.

Use R-box input weight beta_w=9, w_w=exp(beta_w s), and n_w=n0(2R)^4.
For atoms A_ij;S take individual coefficient suprema before summation:

    M_w(A)=max{max_i sum_(j,S), max_j sum_(i,S)}
                                      exp(beta_w|S|) sup|A_ij;S|,
    B_w(A)=sup_q sum_(i,j,S contains q)
                                      exp(beta_w|S|) sup|A_ij;S|,
    Q_w=M_w+B_w.                                         (WS5)

The vector norm V_w is the maximum of its component-root and full marked
incidence sums. A label contains the endpoints and ALL original coefficient
readers. Products obey M(AB)<=M(A)M(B),
B(AB)<=B(A)M(B)+M(A)B(B), and V(Ah)<=Q(A)V(h).
The second marked term requires the column bound. A nonzero matrix product
joins its labels at the summed scalar index.

Define, exactly,

    P_q(lambda)=(K_b,Omega_q+lambda)^-1 1_q,
    R_q(lambda)=-1_(Omega_q^c)K_b(K_b,Omega_q+lambda)^-1 1_q,
    p_w(lambda)=2w_w Q_m/(gamma+lambda),
    r_w(lambda)=2w_w S_m n0 coth(m_w/4)^4
                                exp(-m_w R/2)/(gamma+lambda).

Then (K_b+lambda)P=I-R_w. The residual endpoints have d_1>R; reserve half
the exponential and sum the rest. This proves M(P)<=p_w, M(R_w)<=r_w.
There are at most J marked q and n_w columns per q, so
B(P)<=J n_w p_w and B(R_w)<=J n_w r_w. Choose R with r_w(0)<1/2.
Its exponential decrease permits this simultaneously with RF's O(1/R)
condition, whose required endpoint constants are R-independent. Recompute
RF6--RF18, RC3--RC13 and ALL the following white budgets at that R.

The exact inverse and its marked bound are

    G_lambda=sum_(k>=0)P R_w^k=(K_b+lambda)^-1,
    Q_w(G_lambda)<=A_w/(gamma+lambda),
    A_w=2w_w Q_m[(1-r_w(0))^-1
                             +J n_w(1-r_w(0))^-2].       (WS6)

Marking the initial P or any residual gives the squared denominator.
All unions are connected and retain the whole D_q. Symmetrizing each atom
with its transpose preserves both bounds and its full reader.

For later use, a local lift family has the explicit finite bound

    Q_w(K_b)<=Q_K:=[1+n0(2R+10)^4]w_w b_abs.             (WS7)

A marked R-box restricts the row owner to its sup-distance-five collar;
its size is <=(2R+10)^4. This is a scalar-entry count, including every
colour. The local entry reader occupies at most s R-boxes.

## 3. One domain and equality of the actual critical branches

Use the common actual local analytic radius a_f and vacuum-subtracted bound
H from SA/RF, enlarged for a Wilson vertex separately. Choose them on fixed
preliminary fine/coarse ceilings before the final radii. Put
q_f=(8L^4+8)D and use conservative radius-four vertex roots. The white counts
d_w0=(9L^4+5)(2R+8)^4, d_w1=q_f d_w0 and d_w2=q_f^2 d_w0 bound respectively
the root, force and ordered Hessian incidences. Define

    f(t)=H(1-t/a_f)^(-q_f), S(t)=f'(t)-f'(0)-t f''(0),
    N_w(t)=d_w1 w_w[S(t)+t S'(t)],
    g_w=6sqrt(N)d_w1 w_w, B_src,w=2d_w2 w_w f''(0),
    D_w(t,rho)=2d_w2 w_w{f''(t)-f''(0)+t f'''(t)
                                  +rho[f''(t)+t f'''(t)]}. (WS8)

These are SA10's positive coefficient counts with enlarged root counts.
The linear force is bounded by g_w(1+rho)delta: only Wilson forces survive
at a=0, and their traceless insertions pair with P_0-I. Kernel and Haar
forces vanish separately there. The source Hessian remains; it has bound
rho B_src,w. The nonlinear force starts at degree two and is bounded by
(1+rho)N_w. A mark is on the root or on a substituted field, giving S+tS'.
This expansion is in the original V and original epsilon, before solving
for a field.

Choose a fixed preliminary bar_tau>0, then rho_0>0, so both RF17 and

    bar_tau<min(a_f/16,r_CB/(8sqrt(D))),
    (A_w/gamma)[rho_0 B_src,w
                          +(1+rho_0)N_w'(bar_tau)]<=1/4,
    d_w:=D_w(bar_tau,rho_0), A_w d_w<=gamma/2             (WS9)

hold, with all source radii inside the supplied ones. This is possible
because N_w'(0)=D_w(0,0)=0. Choose a preliminary delta_pre>0 afterward,
inside both curvature classes and with
(A_w/gamma)g_w(1+rho_0)delta_pre<=bar_tau/4.
The exact Picard equation a=G_0[-F_epsilon'(a)+K_b a] converges in the white
atom space and gives

    V_w(b_epsilon)<=C_b delta,
    C_b=2(A_w/gamma)g_w(1+rho_0),
    Q_w(K_epsilon-K_b)<=d_w.                            (WS10)

This is the same coefficient construction as SA13, with the larger
constants and readers just specified. It retains the source-linear Hessian.
Its coefficient list is fixed independently of epsilon, so source-zero
subtraction below is coefficientwise.
To match an already chosen SA instance literally, retain its finite
C_b,old and positive delta_A,old,rho_0,old. Further require
rho_0<=rho_0,old and delta_pre<=min(delta_A,old,bar_tau/(2C_b,old)).
These fixed restrictions put its original branch inside the same small cube.

For RC take Lambda=E and restrict its final tau_a<=bar_tau and joint domain
to the above real curvature class and source disc. Recompute its local
Mayer constants at the fixed ceilings before choosing r_a, tau_a and its
final curvature/boundary radii in RC8/RC13/RC17. Require delta<=delta_*,a
and all RF17--RF18 inequalities for those chosen radii. The full-region
boundary is empty. Its unused positive boundary ceiling need not be zero.

The original SA branch and both new representations solve the SAME actual
equation F_epsilon'(a)=0 in the ordinary scalar cube ||a||infinity<=bar_tau. To check uniqueness there, remove the
root marks from WS8's positive Taylor counts: the ordinary row Lipschitz
bound of H_epsilon+DN is at most
rho_0 B_src,w+(1+rho_0)N_w'(bar_tau). The inverse row bound is <=A_w/gamma.
Thus the pointwise Picard map has Lipschitz constant <=1/4 on that cube.
The segment between the two solutions stays there, so their difference
has norm <=one quarter of itself and is zero. Their precisions and
critical phase values therefore agree. This is a functional uniqueness
argument; the SA-type and RF atom decompositions have NOT been identified
by intersecting scalar radii or replacing P_Lambda by a compression of
another constructed core.

The ordered critical resolvent series gives, uniformly for lambda>=0,

    (K_epsilon+lambda)^-1
                =G_lambda sum_(k>=0)[-(K_epsilon-K_b)G_lambda]^k,
    Q_w((K_epsilon+lambda)^-1)
                         <=A_w/(gamma+lambda-A_w d_w).  (WS11)

Its complete-reader series is absolutely integrable against
lambda^(-1/2)/pi. At epsilon=0, real positivity and the scalar substitution
lambda=x t^2 show
pi^-1 int_0^infinity lambda^-1/2/(x+lambda) d lambda=x^-1/2.
Diagonalizing the REAL positive K_0 proves that this integral is its
positive inverse square root. Integration of the coefficient majorant
therefore yields the ACTUAL family

    Q_w(C_0)<=Q_C:=A_w/sqrt(gamma-A_w d_w),
    Q_w(T_0)<=Q_T:=(Q_K+d_w)Q_C, T_0=K_0 C_0.            (WS12)

The product proof WS5 supplies its marked bound as well as both endpoint
bounds. C_0 commutes with K_0 by its resolvent formula, so T_0 is its
positive inverse and T_0^2=K_0. All dimensions are retained. This is the
needed complete-reader half-power supplier; no finite white-coordinate
incidence is claimed.

A Cauchy--Stieltjes inverse-square-root representation is also described
by [Benzi--Simoncini, arXiv:1501.07376v1](https://arxiv.org/html/1501.07376v1),
section 2.2. The directly inspected window is recorded in the manifest.
Their entry-decay discussion is not a theorem about our coefficient
readers. WS4--WS12 rebuild the endpoint, marked, normalization and branch
steps used here.

## 4. Source recentering and every scalar end contour

Let K_0 and C_0 remain fixed in epsilon and put

    h=sigma^-1 T_0(b_epsilon-b_0),
    Q=C_0^T K_epsilon C_0=I+Epsilon_G.                   (WS13)

Do not confuse the matrix Epsilon_G with the original source array.
Cauchy's formula in the common radial source parameter, on the SAME
coefficient family at radius rho_0, gives for rho<=rho_0/2

    V_w(b_epsilon-b_0)<=2 C_b delta rho/rho_0,
    Q_w(K_epsilon-K_0)<=2d_w rho/rho_0,
    Q_w(Epsilon_G)<=C_E rho, V_w(h)/p<=C_h rho delta/(sigma p),
    C_E=2Q_C^2 d_w/rho_0, C_h=2Q_T C_b/rho_0.             (WS14)

The lift Hessian cancels coefficientwise in the second line; every
critical-field and matrix-product reader remains. Symmetrize the precision
atoms with their transposes. Set M_C=B_C=Q_C as safe separate bounds.

Write z=w-h. Exact critical Taylor expansion gives

    sigma^-2 F_epsilon(b_0+sigma C_0 w)
      =sigma^-2 F_epsilon(b_epsilon)+(1/2)z^T Q z+U(z),
    U=sum_v sigma^-2{F_v(b_epsilon+sigma C_0 z)-F_v(b_epsilon)
       -sigma F_v'(b_epsilon)C_0z
       -(sigma^2/2)F_v''(b_epsilon)[C_0z,C_0z]}.          (WS15)

Only the SUM of the linear jets vanishes. Full constant and quadratic sums
are the displayed critical action and Q, including Haar and normalizers.

Put r=1/16. The exact one-dimensional chain replacing [-p-h_i,p-h_i] is

    Gamma(h_i)=[-p,p]+[-p-h_i,-p]+[p,p-h_i].             (WS16)

A holomorphic primitive verifies the orientations directly. Tensoring the
identity gives all 3^d bulk/end/corner choices, with each segment's complex
dz_i measure and its sign. This is not the centered cube alone. The scalar
functional bounds below allow |h_i|/p<=r/4. On its entire homotopy,
|z_i|<=(1+r)p, and all original fine scalar arguments lie in the analytic
chart if

    C_b delta+sigma(1+r)p M_C<a_f/2.                    (WS17)

Thus Stokes is used only on a proved holomorphic fine domain. The original
cut is one on the original real Omega before this operation; it is not
transported as an extra analytic indicator. No G-minus-Omega or history
indicator is deformed.

To localize U, Taylor-expand the ORIGINAL local vertices at zero before
substituting the b and C_0 atoms. Every resulting reader contains the
vertex root, every substituted field/whitening reader, and every white
coordinate appearing. For a reader S the resulting U_S is bounded and
holomorphic on |z_i|<=(1+r)p in all its used coordinates. It does not require
evaluating an original vertex at an uncontrolled removed coordinate.

For t=C_b delta, x=sigma(1+r)p M_C, y=sigma(1+r)p B_C, set
T3=f(t+x)-f(t)-x f'(t)-x^2 f''(t)/2. Root, background and whitening marks
give the explicit bound

    ||U||_(beta_w)<=sigma^-2 d_w0 w_w(1+rho_0)
                              [T3+t partial_t T3+y partial_x T3]
                     <=A_U sigma p^3,                 (WS18)
    A_U=(1+rho_0)d_w0 w_w H 2^(q_f+3)(1+r)^3/(6a_f^3)
       *{[(q_f)_3+(q_f)_4]M_C^3+3(q_f)_3 B_C M_C^2}.

Here (q)_k=q(q+1)...(q+k-1). The inequalities follow from the integral
third remainder, its t derivative, and its x derivative, with t+x<=a_f/2.
This uses all-order convergent Taylor majorants, not a truncated model.
The price is sigma p^3. No bounded physical-slot incidence is silently
asserted for white coordinates.

## 5. The checked FR Gaussian/decorated library

Use FR10--FR20 with beta_w=9 and output R-box rate mu_w=1. Let

    delta_G=Q_w(Epsilon_G)+V_w(h)/p,
    z_p=(2pi)^-1/2 int_(-p)^p exp(-x^2/2) dx,
    Z_p(Epsilon_G,U,h)=z_p^-d(2pi)^-d/2
        int_(product_i Gamma(h_i))
                    exp[-z^T(I+Epsilon_G)z/2-U(z)] dz.   (WS19)

For its explicit sufficient constants take C_s=B_s=2^20,
A_FR=2^20(1+C_s+B_s)^20 and
delta_0=h_0=min(r/256,1/(2^20 A_FR)).
Choose, after the preliminary field ceilings, a FIXED

    0<rho<=min(rho_0/2,delta_0/[2(1+C_E+C_h)]),
    delta<=min(delta_pre,sigma p), p>=1,
    A_U sigma p^3<=h_0/2.                              (WS20)

Then delta_G<=delta_0/2. These are original-source radii, not rho p^2
smallness conditions.

Here are the load-bearing FR checks for the nonlocal whitening.
Split diagonal precision atoms eta_i from off-diagonal pairs, factor the
scalar q_p(eta_i,h_i/p), and normalize each contour functional nu_i so
nu_i(1)=1 exactly. FR7--FR8 prove |q_p|>1/4 and the coefficient moment bound

    exp[C_s(a_i+s_i)] B_s^(k_i) k_i!,
    s_i=sum_(j!=i)e_ij<=1/64, a_i<=r/4.                 (WS21)

At k_i=a_i=s_i=0 its value is ONE. The proof inserts exp(|z_i|/16),
uses |z_i|^k<=k!16^k exp(|z_i|/16), and Cauchy on fixed eta_i,h_i/p circles.
End segments retain Re[(1+eta_i)z_i^2]>=3p^2/4. Coefficient marks on the
scalar normalizer are included. All these bounds hold for bounded
holomorphic readers on the finite polydisc, not for arbitrary readers
on the full real Gaussian domain.

First Mayer-group U_S by overlap of their complete readers. A decoration
Y is one object containing ALL white coordinates owned in Y; unused
coordinates are singleton objects. Keep internal precision pairs in the
object exponent. Between objects use the exact precision-pair forest with
u_AB=-sum_(i in A,j in B)(Epsilon_G)_ij z_i z_j and path-minimum factors
in exp(sum t_F u_AB). Its coefficient proof assigns independent edge
variables with distribution x^(n_e); the possible maximum spanning forests
partition probability one. This is a precision-exponential identity,
not an incomplete covariance path-minimum derivative.

Expand each edge into scalar endpoints and all coefficient readers.
If k_i endpoints arrive at coordinate i, its factorial is the INDIVIDUAL
k_i! in WS21. After distributing children l_i, their child factorials
leave l_i+1 at the incoming endpoint and one elsewhere. The planted recursion is

    T_i<=exp(epsilon_i)(1-x_i)^-2
       [1+sum_(Y contains i) a_Y^* exp(sum_(k in I(Y),k!=i)epsilon_k)
                                      product_(k in I(Y),k!=i)(1-x_k)^-1],
    x_i=B_s^2 sum_j e_ij T_j, epsilon_i=C_s(a_i+s_i).     (WS22)

The crucial sums are <=delta_G |Y| for both
sum_(i in I(Y))(a_i+s_i) and sum_(i in I(Y),j)e_ij.
They follow from the FULL marked incidence in WS5/WS14, not from a bound
on how many physical vertices see a white coordinate. With T<=2 the
attachment cost is <=exp[(C_s+4B_s^2)delta_G |Y|].
The FR slack maps T into [1,2] and gives derivative row sum <1/2.
Mark a decoration, a tree/internal pair, or a scalar functional; these
exhaust also readers remote from their endpoints. Internal-pair marking
adds two legs, replacing the geometric root factor by
2B_s^2(1-x)^-3. The marked endpoint sum is B_w(Epsilon_G), not a volume.

Compatibility retains occupied scalar coordinates and decoration cores;
external readers may overlap. Reader intersection overcounts actual
incompatibility for the bound. Its hard-core tree sum, with the remaining
support-weight margins, converges. An isolated undecorated coordinate
contributes one and no polymer. This checks the all-order factorial,
mode-count and reader hypotheses of FR, without using the original-coordinate
incidence 90 or a high-degree Holder shortcut.

Distinguish the TWO Gaussian conclusions precisely:

    L_G:=log Z_p(Epsilon_G,0,h)
          =-(1/2)TrLog Q+T_p,
    ||T_p||_(mu_w)<=C_FR delta_G exp(-p^2/64), T_p|_(epsilon=0)=0,
    J_p:=log Z_p(Epsilon_G,U,h)-L_G,
    ||J_p||_(mu_w)<=C_FR A_U sigma p^3.                  (WS23)

C_FR is the fixed universal constant in the displayed FR proof. The raw
quadratic log L_G contains the O(rho) FULL determinant term; it is not
itself a rare boundary correction. For U=0 only, FR9 compares polynomial
moments to the full Gaussian. Absolute summation of residual quadratic
powers is justified inside the integral by
sum_(i<j)e_ij|z_i z_j|<=sum_i s_i|z_i|^2/2. A changed tail/end reserves
exp(-p^2/64) while leaving positive quadratic precision. This does not
extend a bounded nonlinear decoration to the full real domain.
The full Gaussian gives det Q^-1/2, with branch one at Epsilon_G=0.
Cauchy in a multiplier of U supplies the J_p estimate. All series are in
original readers and original sources, and their convergence proves the
nonvanishing used in WS23 before division.

## 6. Exact physical prefactor and the matched logarithm

For the real affine white change, its Euclidean Gram determinant is
det(C_0^T C_0)=det K_0^-1. Its positive square root is det C_0, so the
Jacobian is sigma^d det C_0. Hence WS15--WS19 give EXACTLY

    Z_Omega=h_N^n(2pi sigma^2)^(d/2) det C_0
               exp[-F_epsilon(b_epsilon)/sigma^2]
                          z_p^d exp[-(1/2)TrLog Q+T_p+J_p]. (WS24)

No second Haar factor or omitted Gaussian mode is hidden in this formula.
The matrix Epsilon_G has absolute endpoint norm <1, so TrLog Q is its
convergent trace series. The RF accretive determinant branch for K_epsilon
agrees with continuation from the positive K_0. The finite identity
det Q=(det C_0)^2 det K_epsilon and equality at epsilon=0 imply on the
connected source polydisc

    TrLog Q=LogDet K_epsilon-LogDet K_0,
    det C_0 exp[-(1/2)TrLog Q]=exp[-(1/2)LogDet K_epsilon]. (WS25)

This uses analytic continuation of scalar determinants, not a false
multiplicative identity for noncommuting matrix square roots. In particular
the untruncated Gaussian determinant has been matched, not called rare.

Keep the full prefactor

    P_epsilon=h_N^n(2pi sigma^2)^(d/2)
         exp[-(1/2)LogDet K_epsilon-F_epsilon(b_epsilon)/sigma^2]. (WS26)

It is generally extensive and non-small. Its source action can be of order
rho delta^2/sigma^2 per block. The finite-u normalizer vacuum, all colours,
root and harmonic modes are present. IC30--IC31's intrinsic-Hessian/Gram
conversion concerns a TREE-phase stationary point and is not applied to
the Haar-inclusive b_epsilon. In particular that point need not be
stationary for the Haar-free physical action. No gauge-slice change occurs
between WS24 and the chart formula, so no extra root Gram or FP factor
is inserted or canceled.

For complete phase bookkeeping, let F_empty be the sum of any original
empty-field-stencil vertices. RF/RC at Lambda=E uses
F_E=F_epsilon-F_empty. Multiply its whole-region result by the explicit
outside factor exp(-F_empty/sigma^2). This restores WS3 and WS26 even if
such vertices are present. Original scalar vacua inside nonempty original
vertices are already retained there and are not reassigned empty stencils.
Functional uniqueness in section 3 and RC9/RC14 now give

    Z_Omega=P_epsilon z_p^d exp(T_p+J_p),
    I_a=P_epsilon exp(H_a), ||H_a||_(beta_a/2)<=epsilon_a,
    beta_a=(16R)^-4.                                    (WS27)

Here epsilon_a is EXACTLY RC13, recomputed with its full RF covariance
family, both tails, all colour densities, side and corner primitives, and
RC6's local envelopes at the common preliminary ceilings. Impose its
sigma<=1, q_h<=1, h_0,a<=h_c/2, h_s<=h_c/2 and
epsilon_a<=beta_a/16, as well as RC8. Nothing in WS23 replaces that chart
construction or identifies its core with C_0's parametrix.

Fill every white R-box reader S by all its original blocks Y. It remains
connected and |Y|<=(2R)^4|S|. A marked original block belongs to exactly
one R-box; grouping equal filled readers by the triangle inequality adds
no root multiplicity. Thus a white output rate 1 gives original-block
rate 1/(2R)^4 with its same rooted bound. Take

    mu=min{1/(2R)^4,beta_a/2}=beta_a/2>0,
    Gamma_a:=log(Z_Omega/I_a)
               =d log z_p+T_p+J_p-H_a.                 (WS28)

This is a convergent sum of complete connected ORIGINAL readers. Assign
the remaining constant mode term n0 log z_p to each original block.
Its rooted norm is n0 exp(mu)|log z_p|; it is not omitted as a vacuum.
The exact bound is

    ||Gamma_a||_mu
      <=n0 exp(mu)|log z_p|
        +C_FR delta_G exp(-p^2/64)+C_FR A_U sigma p^3+epsilon_a. (WS29)

Both integrals and their ratio are nonzero on the stated source polydisc.
The logarithm agrees at epsilon=0 with the real logarithm of the positive
ratio; the convergent connected series fixes its continued branch. No
absolute error proportional to total volume is substituted for WS29.
No atomwise matching of different covariance decompositions was needed:
only the proved common physical b_epsilon,K_epsilon and full phase.

On the half source polydisc, for any scalar original-source multiindex nu,
the norm of partial_epsilon^nu Gamma_a is bounded by WS29 times
nu!(2/rho)^|nu|. For nonzero nu the constant d log z_p differentiates to zero.
A source outside a coefficient's full reader has derivative zero.
The source-normalized ratio is exactly exp[Gamma_a(epsilon)-Gamma_a(0)].
Its logarithm has the corresponding twice-WS29 bound without the constant
mode term. This is local connected control, not a volume-uniform bound on
the unnormalized scalar ratio.

## 7. Nonempty shrinking regime and precise consumer scope

The parameter order is substantive. First fix common preliminary analytic
ceilings and the actual lift gap. Choose the single R satisfying WS6 and
RF16; compute both libraries at this R. Choose common bar_tau,rho_0 under
WS9 and RF17. Compute RC6's local envelopes and WS18's A_U on those fixed
ceilings. Fix rho by WS20. Then choose the chart radius and final RF domain
under RC8/RC13; later restrictions change none of the coefficient formulas.
This avoids a radius defined using a majorant that already depends on
that unknown radius. All constants may be large, but are finite and
independent of u,T. No old two-unit RD support margin is assumed.

For an explicit asymptotic family take p_a=p and

    r_a=sigma p, tau_a=c_a sigma p,
    0<c_a<=min{1/(16D),
              sqrt(a_P)/(8D sqrt(L_hat^2+a_P/64))}.       (WS30)

Here a_P,L_hat are the actual recomputed RC constants. Use RC17's
positive k_y,k_v and its choices
Y=k_y tau_a, zeta=Y/c_y, delta_*=eta=k_v tau_a.
This proves the nonempty RF domain, even though only its real-V slice
and empty boundary are used here. Restrict

    delta<=min(delta_pre,sigma p,k_v c_a sigma p)

and retain WS17 and the original Omega/G/cut margins.
Take p to infinity with sigma p^3 to zero. For example every fixed
p=(log(2+u))^alpha, alpha>5/2, satisfies these limits and the existing
GC cutoff-power requirement for sufficiently large u. It does not remove
GC/SC's additional hypotheses or their narrower coarse-center windows.

RC18 gives
epsilon_a<=C1 sigma^2+C2(1+p^(91D+2))exp(-a_P p^2/64).
Also, for p>=1, the elementary Gaussian tail bound gives
|log z_p|<=C p^-1 exp(-p^2/2) with an absolute finite C.
Consequently

    ||Gamma_a||_mu<=C3 sigma p^3+C4 sigma^2
                      +C5(1+p^(91D+2))exp(-c p^2),
    c=min(1,a_P)/64>0.                                  (WS31)

The leading proved bound is polynomial in sigma. A purely rare bound
would require an additional matched cancellation of J_p-H_a; WS31 does
not supply it. Source Cauchy radii stay fixed. The admitted real curvature
window shrinks; no fixed unscaled coarse domain follows.

The native SA/FR theorem restricts V to a real curvature class; SA explicitly
disclaims a product complex coarse domain. IC has a source-free holomorphic
transported white chain, but that does not extend FR's mixed original-source
reader suprema. This unit therefore makes NO joint coarse/source claim.
Such an extension must build the WS4--WS14 coefficient bounds uniformly on
one common complex coarse tube, check the actual joint vertex majorants
and WS17 there, and identify the transported chain and determinant branches.
A complex hard Omega predicate is not an analytic object to be continued.
The same real-V scalar cube is all that has been matched here.

The literal STEP55 section 5 consumer uses a product of white su(N) BALLS,
a slice covariance and potentially inherited effective polymers; its S9
correction also retains the main action and full Gaussian normalization.
WS28 supplies none of those extra identifications. The scalar cube is not
invariant under general root colour rotations; IC's white-ball Ward theorem
is separate. No new Ward identity or weakening of the original non-free
physical target is inferred.

The actual identity remains Z_cut=Z_Omega+I_(G minus Omega)+I_(G^c).
If a later proved log of Z_cut/I_a is supplied on the SAME physical domain
and normalization, subtraction of WS28 would give its bare-cut/white log.
That later theorem is not a premise here, and no separate history,
G-minus-Omega or G^c connected estimate is asserted by this subtraction.
Rough exteriors, arbitrary histories, effective-step identification,
multiscale iteration, non-free continuum existence and the positive
physical continuum mass gap remain OPEN.

No scientific numerical experiment was needed. Only this source and
checks/white_sector_matching_* are authored. The mathematical source is
frozen before the compact read manifest and receipt, then sent for fresh
independent review. Author checks are identity/provenance checks, not proof.
Root owns publication, Git, shared fronts, audits and integration.
