# Bare classical coupling and the full critical prefactor

This unit computes the one-step infrared quadratic coefficient of the actual
normalized arithmetic-contour kernel. It also extracts a bounded finite-u
correction from the full critical prefactor, using the already proved fixed
coarse-domain comparison in IC25–IC32. It does not identify the entire coarse
quadratic symbol with a Wilson symbol. No universal beta-function coefficient
or repeatable coupling trajectory is computed here. Four-dimensional non-free
continuum existence and a positive physical continuum mass gap remain **OPEN**.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Actual bare one-step classical Schur symbol and marginal coefficient; fixed-domain finite-u critical-prefactor matching with an unevaluated full one-loop trace."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## 1. Object, conventions and fixed domains

Fix N>=2, D=N^2-1, odd L>=3, a coarse torus of side T>=2, and
`0<kappa_-<=kappa<=kappa_+`. Hold kappa fixed when u varies. All original
Wilson sources are zero throughout this theorem; this is not a theorem for
an inherited effective action or a history coefficient. The fine spacing is
one until physical units are restored below. The actual density is CB1:

    w(U,V)=exp[-u sum_p s(U_p)] product_c k_(kappa u)(V_c;M_c(U)),
    s(W)=1-Re tr(W)/N,
    k_t(V;M)=exp[-t(1-Re tr(V^-1 M)/N)]/N_t(M),
    N_t(M)=int_SU(N) exp[-t(1-Re tr(W^-1 M)/N)]dW.          (BM1)

Haar is probability Haar. M is the arithmetic mean of the 24L^4 actual
paired contours, with the same axial order at the two ends. It is not a
unitary projection of that mean. The SU(N) maximizer used below is FK's
actual constrained saddle, including its scalar constraint when N>=3.
No U(N) polar maximizer is substituted.

Use CB2's lift U0(V): internal links I and every outgoing crossing link on
face (X,mu) equal to V_(X,mu). Fix CB4's complete axial tree inside each
block, whose parent moves the highest nonzero coordinate toward the root.
Tree gauge integration has volume and Jacobian one. Write

    U_e=exp(a_e)U0_e(V), m0=3L^4+1, n=m0 T^4,
    n0=Dm0, d=Dn, nc=4T^4, sigma^2=N/u.

There are n free links and d scalar coordinates. All crossing, root,
harmonic and colour directions remain. HS coordinates have
`-tr(T_a T_b)=delta_ab`. FLOW/LOCOP coordinates have colour metric
`<A,B>=-tr(AB)/N`; hence a_FLOW coefficient becomes sqrt(N) times that
coefficient in an HS-orthonormal basis. The actual unsubtracted phase and
critical prefactor are

    W_p=tr(2I-U_p-U_p^-1)/2,
    F_u=sigma^2[-log w(U(a),V)-sum_free e log j_N(a_e)],
    F_u'(b_u;V)=0, K_u^*=F_u''(b_u;V),
    P_u=h_N^n (2pi sigma^2)^(d/2)
                 exp[-F_u(b_u;V)/sigma^2-(1/2)LogDet K_u^*]. (BM2)

`dHaar(exp a)=h_N j_N(a) da`. LogDet is the accretive matrix trace-log,
not a principal scalar log of a possibly winding determinant. This is the
full prefactor kept outside WR42a, on the common source-free domain.

For the coefficient estimate use IC's **fixed** preliminary complex coarse
domain about Vbar=I, `V_c=exp(v_c)`, `max ||v_c||HS<rho0`. Choose IC's
local fine domain inside FK20, its gap constants and geometry-only R-box
size first; then its tau, curvature margin and positive rho0 by IC11.
If comparing to the FU/CA/CD representation, take the smaller of their
fixed radii and identify the critical branch in the common uniqueness ball.
Only then choose u_* so that FK's Laplace estimates and IC26–IC28 hold.
All these choices are independent of u>=u_* and T. One can further restrict
to the shrinking HC/WR domain without changing the actual critical branch.
The fixed-domain extension here is of P_u and its critical phase; it is
not an extension of an original hard-cut integral or its contours.

The earlier linear package and UL8 already contain tree normalization.
Sections 2–3 below verify that statement against this particular contour
symbol and give an explicit non-Wilson symbol. IC25–IC32 already supply the
finite-u phase comparison. Sections 4–6 add its actual flat Schur expression,
constant-curvature action coefficient and the reader-to-moment extraction.
Review labels of those sources are not mathematical premises.
The exact source keys are [CB](COVARIANT_SOFT_BACKGROUND_ASTRA.md),
[FK](FINITE_COUPLING_KERNEL_ASTRA.md),
[FU](FINITE_U_CRITICAL_FIELD_ASTRA.md),
[CA](CRITICAL_ACTION_READER_ASTRA.md),
[CD](CRITICAL_DETERMINANT_READER_ASTRA.md),
[IC](INTERACTING_SELECTED_CORE_ASTRA.md), [LOCOP](LOCOP.md),
[SPURION](SPURION.md), [UL](UNIFORM_ONE_LOOP_COUPLING_ASTRA.md), and
[WR](WEIGHTED_RETURN_JETS_ASTRA.md).

## 2. Normalizer cancellation and the complete classical Schur form

Let `psi_c(V,M)=max_(W in SU(N)) Re tr(W^-1 M)/N
                          -Re tr(V_c^-1 M)/N` at real data, continued by FK.
The u-independent scaled tree phase and its stationary value are

    F_T(a;V)=sum_p W_p(a;V)+N kappa sum_c psi_c(a;V),
    F_T'(b_T;V)=0, K_T(V)=F_T''(b_T;V),
    T_1(V)=F_T(b_T;V)/N.                                 (BM3)

The real fine Hessian gap needed for this branch is already supplied by
CB6 and the small Wilson curvature error. It does not use the Haar mass
or the finite-u spread correction. IC section 7 constructs b_T by the
same connected inverse and analytic contraction used for b_u.

At the identity, write the first contour variation as ell_(c,r)(A),
`QA(c)=avg_r ell_(c,r)(A)`. Expanding each SU transporter gives
`Re tr M=N-(1/2)avg ||ell_r||HS^2+O(A^3)`; commutator contributions have
zero trace at this order. Varying the SU saddle W=exp(w) adds
`<w,QA>HS-||w||HS^2/2`. Its quadratic maximum is attained at w=QA.
Consequently

    psi_c^(2)=(1/(2N))||B_c-QA(c)||HS^2,
    (u/N)F_T^(2)=(u/(2N))[||d_f A||HS^2
                                      +kappa||B-QA||HS^2]. (BM4)

The `avg ||ell||^2-||avg ell||^2` spread cancels against the leading
normalizer saddle. Omitting the normalizer would leave an extra classical
penalty and would change this calculation.

Let iota insert zero on fine tree links, D_f=d_f iota, and now restrict Q
to the free-link space. Adjoints in this section use the counting HS metric.
CB6, including its lifted-brick convention at T=2, gives

    K0=D_f^*D_f+kappa Q^*Q >= a_gap I,
    a_gap=1/max(4L^3(L+4)(60L^2)^2,2L^3/kappa_-).

Completing the actual finite-dimensional square gives the entire classical
coarse Hessian, on all coarse link and colour coordinates:

    H_cl=kappa I-kappa^2 Q K0^-1 Q^*,
    u T_1^(2)(B)=(u/(2N))<B,H_cl B>HS.                   (BM5)

No determinant is inferred by deleting gradient or harmonic modes in this
formula. The inverse K0 contains all d fine coordinates. Coarse gradients
have zero Schur energy because Q d_f=d_c ev_root and the fine gradient
with prescribed root values is available before tree gauge fixing. Constant
coarse harmonic fields also have zero Schur energy: their flat brick lift
has d_f A=0 and QA=B. Thus H_cl(0)=0, with no inverse of the coarse zero
mode requested. The quotient used next only computes the Schur *value*.
It does not replace the full Gaussian determinant.

## 3. Actual contour symbol and physical normalization

Put h=(L-1)/2 and y in {-h,...,h}^4. If h_ax(A) is the average root-to-y
axial line integral, the paired end paths give exactly
`Q_root=Q_str-d_c h_ax`. Also `Q_root d_f=d_c ev_root`. These are line
integral identities: the translated end path is subtracted with the same
ordering. In tail-link Fourier coordinates they read

    Q_root,mu nu(q)=delta_mu nu s_L(q_mu) D_L(q)
                                  +(1-exp(iLq_mu)) R_nu(q),
    s_L(t)=sum_(r=0)^(L-1) exp(irt),
    D_L(q)=product_alpha d_L(q_alpha),
    d_L(t)=sin(Lt/2)/(L sin(t/2)),                         (BM6)

where R is the average axial path current. Removable values are understood.
A fixed global shift of roots only changes Fourier phase conventions.
In particular `R(q)d_f(q)=D_L(q)-1`. The R term is a coarse gradient and
is killed by the coarse transverse projection.

Here is the precise alias formula, including link-centre phases. For a
coarse momentum p, take the L^4 aliases `q_K=(p+2pi K)/L` in the fine
Brillouin torus. Set `hat q_mu=2sin(q_mu/2)`,
`lambda(q)=sum_mu hat q_mu^2`, and use link-midpoint Fourier transforms.
Let P_c(p) be projection orthogonal to hat p, for p!=0. The diagonal
straight-leg matrix for alias K is

    S_K,mu nu(p)=delta_mu nu (-1)^(K_mu)
                           L d_L(q_K,mu) D_L(q_K).       (BM7)

Indeed the fine link-centre phase, the sum of L leg phases and the coarse
link-centre phase combine as
`exp(-ip_mu/2) exp(iLq_mu/2) sin(Lq_mu/2)/sin(q_mu/2)`.
This is BM7. In particular
`S_K (i hat q_K)=D_L(q_K) i hat p` exactly. The additional leg-direction
factor d_L(q_mu) in BM7 is essential; a scalar block average alone is wrong.
With unitary Fourier transforms, the fine-to-coarse map has the additional
factor L^-2, since the fine volume is L^4 times the coarse volume.

Minimize first over fine gradients. They fit the coarse longitudinal
part at zero curvature cost. On fine transverse fields the Wilson inverse
is `lambda(q_K)^-1 P_f(q_K)`. Completing this remaining Gaussian square
therefore gives the coarse transverse covariance

    G_perp(p)=kappa^-1 P_c(p)
       +L^-4 P_c(p) sum_K [S_K(p) S_K(p)^*/lambda(q_K)] P_c(p),
    H_cl(p)|_(hat p perpendicular)=G_perp(p)^-1.          (BM8)

For p!=0 no q_K is zero. The fine transverse projector has disappeared
legitimately: `P_c S_K (i hat q_K)=0`. BM8 together with the zero coarse
longitudinal block equals BM5. This also derives, rather than assumes, the
volume normalization in the alias sum.

As p tends to zero, S_0=L I+O(|p|^2),
`lambda(p/L)=|p|^2/L^2+O(|p|^4)`, and the other aliases are bounded.
Thus the residue of G_perp is

    L^-4 L^2 L^2=1,
    H_cl,mu nu(p)=|p|^2 delta_mu nu-p_mu p_nu+O(|p|^4).  (BM9)

This is one scalar copy for every one of the D colours. The classical
infrared coefficient in LOCOP/FLOW normalization is therefore

    beta[T_1]=1,                     u'_tree=u.           (BM10)

Restoring fine physical spacing a_phys, a smooth physical connection has
fine integrated links approximately a_phys A_phys and coarse integrated
links approximately L a_phys A_phys. The coarse curvature is approximately
`(L a_phys)^2 F_phys`; its square is multiplied by the coarse site density
`(L a_phys)^-4`. These factors cancel in four dimensions. BM10 is in these
canonical integrated-link units, not units obtained by silently keeping a
fine-link amplitude on the coarse lattice.

A useful exact check also separates BM10 from a full Wilson matching.
Take p=(0,P,0,0) and polarization mu=1. In BM8 only aliases with
K1=K3=K4=0 contribute. With `lambda_P=4sin^2(P/2)`,

    G_11(P)=kappa^-1
       +sin^2(P/2)/(4L^4) sum_(k=0)^(L-1)
                                  csc^4((P+2pi k)/(2L)).

Differentiate `sum_k csc^2(x+pi k/L)=L^2 csc^2(Lx)` twice, using
`(csc^2 x)''=6csc^4 x-4csc^2 x`. Substitution gives exactly

    G_11(P)=lambda_P^-1+kappa^-1-(1-L^-2)/6,
    H_cl,11(P)=lambda_P/
                   [1+{kappa^-1-(1-L^-2)/6}lambda_P].    (BM11)

The positive covariance formula proves positivity; its continuous value
at P=0 is handled by BM9. Unless the displayed constant vanishes, this
symbol differs from the Wilson symbol lambda_P at nonzero momentum.
After multiplication by u that difference is generally O(u). Matching
the infrared coefficient does not make `u(T_1-W_coarse)` a small arbitrary-
field remainder. Spatial regularity and the LC2-type contraction remain
separate requirements.

## 4. Exact finite-u critical-action Hessian and its first coefficient

Define the spread matrix and the brick-lift derivative in the free space:

    <a,B_sp a>=sum_c avg_r ||ell_(c,r)(iota a)-Qa(c)||HS^2,
    (EB)_e=B_(X,mu) on crossing face (X,mu), zero internally.

Every individual contour of EB is B_c. Hence QE=I and B_sp E=0.
Also CB3 gives `E^*D_f^*D_f E=L^2 d_c^*d_c` exactly. Let
`J_B=D_f^*D_f E`. In the moving physical chart of BM2 the *linear*
absolute fine field is `iota(a+EB)`. The Haar logarithm is log j_N(a),
not log j_N(a+EB).

For the central tilt at t=kappa u write `E_t W=c_N(t)I`. CB's finite-t
normalizer identity and `log j_N(a)=-N||a||HS^2/12+O(a^4)` give at flat
background the exact scaled fine precision

    K_u=K0+kappa(1-c_N(kappa u))B_sp+N^2/(6u) I.          (BM12)

One way to check the normalizer identity is to expand every path to order
two and use the fact that N_t(G) is constant on SU(N). The second variation
along a common path is zero; the remaining variance has coefficient c_N.
The numerator minus this contribution is
`kappa[||Qa||^2+(1-c_N)avg ||ell-Qa||^2]/2` in F_u.
There are no B-mixed kernel terms at this order, since ell(a+EB)-B=ell(a).

Thus the source-free critical *action*, including its Haar logarithm and
normalizer, has the exact quadratic coefficient

    F_u^(2)(a;B)=1/2 [a^*K_u a+2a^*J_B B
                                      +B^*E^*D_f^*D_f E B],
    H_act,u=E^*D_f^*D_f E-J_B^*K_u^-1 J_B,
    [F_u(b_u;V)/sigma^2]^(2)=(u/(2N))<B,H_act,u B>.      (BM13)

The normalizer vacuum has zero field derivatives and remains in F_u.
At u=infinity BM13 equals BM5. The identity QE=I proves this directly
by expanding K0 E and completing the same square in the two coordinates.
Using a Haar mass in the absolute field A instead would produce spurious
mixed and coarse mass terms. BM13 explicitly avoids that error.

Since `0<c_N<1`, the action correction is positive semidefinite and exact:

    H_act,u-H_cl
       =J_B^* K0^-1 [kappa(1-c_N)B_sp+N^2/(6u)I]
                                                    K_u^-1 J_B. (BM14)

The symmetric difference of the two inverses is meant; positivity follows
from K_u>=K0, not from multiplying arbitrary positive matrices. FK18 gives

    1-c_N(t)=D/(2t)+O(t^-2),
    u(K_u-K0)=C1+O(u^-1), C1=(D/2)B_sp+(N^2/6)I.        (BM15)

All constants are uniform on the fixed kappa interval. This establishes an
O(1) **unscaled marginal** action correction, not only an O(1) value bound.
For detail, J_B(0)e_mu=0 because a constant coarse link field lifts flat.
In cell-based block Fourier coordinates J_B has range one. Counting six
incident plaquettes and four edges per plaquette gives row/column
derivative bounds 24 and 24L^3,
so `||J_B(P e_nu)e_mu||<=24 L^(3/2)|P|`. Further,
`||B_sp||<=4*3^4*(5L)^2` is a safe bound: a contour has length <5L,
and an edge can be charged only by the bounded neighboring coarse roots.
Variance is bounded by the mean square of its path sum. Together with
K0,K_u>=a_gap and `P^2/lambda_P<=pi^2/4`, these bounds control BM14/lambda_P
uniformly in volume. The FK remainder and a second resolvent identity
likewise give an O(u^-1) error after the leading unscaled correction.

That leading action coefficient can actually be evaluated without a loop
integral. Put `s_L^2=(L^2-1)/12`, the mean of y_mu^2 in the centered block.
For a constant infinitesimal coarse curvature F in a single plane a<b,
the fine curvature is F/L^2. Start with its symmetric affine fine potential
and gauge it to the specified rooted axial tree. Subtract the brick lift.
The resulting relative coordinate, per block, is

    a_a(y)=-y_b F/L^2                 on every owned a-link,
    a_b(y)= y_a F/L                   on b-crossing links,
    a_b(y)=0                         on internal b-links,
    a_mu(y)=0                        for mu not in {a,b}. (BM16)

Tree-edge values in BM16 are zero. To verify the crossing factor L, the
root path integral in coordinate order 1,...,4 is
`A(root).y+(1/2)sum_(nu<rho) y_nu y_rho F_fine,nu rho`.
At a mu-crossing edge the endpoint relative coordinate changes from h to
-h and the root moves by L e_mu. Subtraction gives coefficient -L y_nu
for nu<mu and -y_nu for nu>mu, in units F_fine,mu nu. Internally it gives
only the latter terms. This proves BM16, including its boundary faces.

All first-order contour integrals of the underlying constant-curvature
field equal `B_mu-L sum_nu y_nu F_fine,mu nu`; the order-dependent axial
terms at the two endpoints cancel. Their mean is B_mu. Also d_f^*F_fine=0.
Thus BM16 solves the classical fine Euler equation, independent of kappa.
It is the bounded solution for the relative coordinate: the gapped K0
inverse has summable kernel, so the homogeneous bounded solution is zero.
This local affine test is not a nonperiodic field inserted on a torus.
Exponential moments, proved below, identify it with the infinite-volume
small-momentum derivative. A coarse gradient changes no relative a at
linear order, so the symmetric and single-polarization affine tests agree.

For FLOW-normalized F, summing the actual fine links and the path variance
in one coarse cell gives

    sum_free e |a_e|FLOW^2=(L+1)s_L^2 |F|FLOW^2,
    sum_c avg_r |ell_r(a)-Qa|FLOW^2
                                   =2s_L^2 L^-2 |F|FLOW^2. (BM17)

The first sum consists of L^4 links with the y_b/L^2 profile and L^3
crossing links with the y_a/L profile. In the second sum, both orientations
of the chosen curvature plane contribute. Other plane cross terms have
zero centered coordinate average. Since C1/N is the Hessian of the
u-independent F_1 below, BM15–BM17 yield

    beta_action,u=u+alpha_act+O(u^-1),
    alpha_act=(L^2-1)[D/(12L^2)+N^2(L+1)/72].            (BM18)

The two terms are respectively the normalizer-amplitude/spread and Haar
coordinate contributions. The large positive Haar contribution is not a
physical loop coefficient: it must be combined with the coordinate
Hessian determinant. That cancellation is retained in the next section.

## 5. The full fixed-domain prefactor comparison already supplied by IC

Use FK17's actual SU(N) saddle Hessian H_c in HS coordinates, with
`A_c=h_N(2pi)^(D/2)(det H_c)^(-1/2)`. On the fixed joint small-field domain,

    -log k_(kappa u)=kappa u psi_c-(D/2)log(kappa u)
                                              +log A_c+E_(kappa u,c),
    F_1(a;V)=sum_c log A_c(a;V)-sum_e log j_N(a_e),
    R_u(a;V)=sigma^-2 sum_c E_(kappa u,c)(a;V),
    F_u=F_T+sigma^2 F_1+sigma^4 R_u
                                -sigma^2(D nc/2)log(kappa u). (BM19)

This is an exact identity, not a formal asymptotic series. FK16 bounds all
fixed local derivatives of R_u uniformly on a fixed fine/coarse domain.
At a=0, F_1' and R_u' vanish for every admitted V by common-path invariance.
Their Hessians do not vanish. In particular BM15 implies
`F_1,aa(0;I)=C1/N`, and F_1(0;V) is the fixed normalizer amplitude vacuum.

For completeness the consumed IC proof has three essential steps. The
actual critical equations and the tree inverse give
`d_u=b_u-b_T=O_v(sigma^2)` and `Q(K_u^*-K_T)<=C sigma^2` in complete-reader
norms. The tree gradient at b_T is zero as a whole, so

    E_act=[F_T(b_u)-F_T(b_T)]/sigma^2
                       +F_1(b_u)-F_1(b_T)+sigma^2 R_u(b_u),
    E_det=(1/2)sum_(j>=1)(-1)^(j+1)
                         Tr[(K_T^-1(K_u^*-K_T))^j]/j.   (BM20)

In E_act the first numerator is the integral of a Hessian contracted with
two d_u factors, hence O(sigma^4). For such scalar contractions the mark
is in the matrix or either vector, costing
`[B(A)+2M(A)]V(h)V(k)`. In E_det a mark in the j matrix factors costs j,
which cancels its displayed divisor. The row/column and full marked norms
of the inverses are those constructed in IC9–IC13; no operator norm is
substituted for a rooted scalar sum. These are IC26–IC28, on the fixed
rho0 domain. They prove the exact full-prefactor identity

    -log P_u=u T_1+Gamma_1+V_vac^P+E_pref,
    Gamma_1=F_1(b_T;V)+(1/2)LogDet K_T(V),
    V_vac^P=-(D nc/2)log(kappa u)-n log h_N
                                      -(d/2)log(2pi sigma^2),
    E_pref=E_act+E_det,      ||E_pref||_reader<=C/u.       (BM21)

`nc log A_0` remains in Gamma_1; the exact scalar normalizer remainder
remains in E_pref. No field-independent factor has been deleted from BM21.
Neither the order-u critical action nor the full order-one determinant is
part of WR's small nonlinear/compact-return logarithm.

Here is the original-reader and domain bookkeeping behind the last norm.
Take IC's mu=1 for definiteness, so its inverse/composition weight is
exp(5|S|) in its fixed R_IC-box partition. Replace a box label S by the
connected union Y of its original coarse cells, keeping every original
coarse datum and fine-coordinate owner in that union. Then
`|Y|<=(2R_IC)^4|S|`. Fix

    0<beta0<=min(1,(2R_IC)^-4,beta_CD),
    ||f||_beta0=sup_x sum_(Y containing x) exp(beta0|Y|)
                                  sup_(max||v||HS<rho0)|f_Y|. (BM22)

A marked original cell belongs to one R_IC box, so this conversion has no
volume multiplier. It explicitly reduces the original-cell rate; it does
not rename an R-box as a microscopic cell. If only the IC representation
is used, omit beta_CD. All R's and rho0 remain fixed. The same scalar
root/substitution marking applied to the analytic local F_1 vertices gives
`||F_1(b_T)||_beta0<=C_1`. For a local majorant
`g(t)=H_1(1-t/a)^(-q)` this costs at most
`d0 exp(5s)[g(t_b)+t_b g'(t_b)]`, with IC's d0,q,s and t_b<a.
The finite determinant homotopy of IC section 3, reapplied to F_T exactly
as in IC section 7, gives `||LogDet K_T||_beta0<=C_D`. Thus
`||Gamma_1||_beta0<=C_1+C_D/2`. These constants can be large but do not
depend on u or T. BM20 has `||E_pref||_beta0<=C_E/u` with coefficient
suprema inside the sums. No shrinking-radius Cauchy bound is used here.
The tree stationary value also has a finite fixed-domain reader norm: the scalar identity
`F_T(b_T)=F_T(0)-int_0^1 s b_T^T F_T''(s b_T)b_T ds` and the same three
marks give it from the local lift action `F_T(0)=L^2 sum_P W(V_P)` and
the connected Hessian bound. This supplies the tree spatial moments used
in the affine test BM16 as well.

The required Haar/determinant cancellation is exactly IC30. At the tree
critical point let E_coord be the differential from left exponential
coordinates into intrinsic right-translated free-link coordinates. Then

    det E_coord=product_e j_N(b_T,e),
    K_T=E_coord^T K_T,intr E_coord,
    Gamma_1=sum_c log A_c(b_T;V)+(1/2)LogDet K_T,intr.     (BM23)

The second differential multiplies the complete tree gradient and vanishes.
The real branch continues on the common small domain. All d modes remain.
If an orthogonal gauge quotient is introduced, IC31 instead reads
`det K_T,intr=det H_perp/det(D_r^*D_r)` for root-pinned gauge directions.
Adding another Faddeev–Popov determinant to the original tree integral
would double count this measure conversion. BM23 keeps the intrinsic
formula and requires no extra gauge determinant.

## 6. A bounded marginal extraction and the unevaluated loop expression

We spell out why BM21 implies an unscaled coefficient estimate. Use a
translation family on the infinite coarse lattice, and let Pi_mu nu(z)
be its Hessian at identity in a fixed FLOW-unit colour H. Finite tori are
used first to define the derivatives, with all modes retained. Their
infinite-volume limit is taken before the infrared limit. For a connected
family with norm A on BM22, ordinary two-direction Cauchy gives

    |D_i D_j f_Y(0)|<=16 N rho0^-2 sup|f_Y|.             (BM24)

Indeed two independent FLOW-unit directions have HS size sqrt(N); circles
of radius rho0/(4sqrt(N)) fit inside the product coarse chart, even when
they act on the same link. A complete reader Y has at most 8D|Y| coarse
scalar inputs. If it contains two input owners, their link-midpoint distance
plus one is at most 8|Y|, since Y is connected in original coarse cells.
Summing the second index and its second spatial moment therefore costs at
most `2^13 N D rho0^-2 |Y|^3 sup|f_Y|`. Finally
`|Y|^3<=6 beta0^-3 exp(beta0|Y|)`. A convenient common bound is

    sum_z (1+|z|_1)^2 |Pi_mu nu(z)|
            <=C_mom A,
    C_mom=2^16 N D/(rho0^2 beta0^3).                     (BM25)

More precisely, the bound holds for the maximum over the first scalar
component of the sum over all second components. Summing the first
components at one owner adds at most 4D. All derivative labels are original
input links; endpoint support has not replaced complete readers. This is the specific C^2 spatial
moment estimate needed for LOCOP L6. It is stronger than a value bound,
and it is obtained from a fixed, not u-shrinking, radius. The same counting
also gives an exponential Hessian row sum: insert
`exp(beta0 |z|_1/16)<=exp(beta0 |Y|/2)` and use
`|Y| exp(beta0 |Y|/2)<=(2/beta0)exp(beta0 |Y|)`. Its bound is
`2^8 N D A/(rho0^2 beta0)`. Thus the momentum kernel is analytic in a
fixed strip; BM25 records the second-moment cost actually consumed here.

The infinite-volume identification also uses the actual local construction.
Choose IC's finite partitions to coincide with one fixed infinite partition
in a box growing with T; place the exceptional R-to-2R closing intervals
at the distant seam. Local patch inverses and local Taylor vertices then
agree literally whenever their complete reader does not reach that seam.
The uniformly convergent inverse/critical/trace words preserve this agreement.
A connected reader through the origin that sees a seam or winds the torus
has at least cT original cells. BM22, with half its rate spent on polynomial
moments, bounds the remaining Hessian tail by `C exp(-c' beta0 T)`.
This proves convergence of the second-moment kernels independently of the
partition choice and the volume sequence. It does not replace a finite
periodic momentum grid by a continuum before taking that limit. Equivalently,
at flat data the gapped block-periodic Green functions have summable images;
closed determinant paths that wind have length at least T and the same tail.

For an entirely specified scalar convention, define

    V_(X,mu)(epsilon)=exp[epsilon cos(P X_nu+theta) H],
    all other V=I,  -tr H^2/N=1, mu!=nu,
    beta_mu nu[F]=lim_(P->0) (2/lambda_P)
       avg_theta lim_(T->infinity) T^-4
                           (d^2/d epsilon^2)F(V(epsilon))|_0,
    beta_av[F]=(1/12)sum_(mu!=nu) beta_mu nu[F].          (BM26)

Initially choose rational P/(2pi) and compatible tori. BM25 supplies the
unique analytic momentum kernel and hence the displayed limit. The theta
average gives `F^(2)/T^4=epsilon^2 Pi_mu mu(P e_nu)/4`.
These factors make beta_av[sum_P s(V_P)]=1.

The prefactor is gauge invariant under coarse root gauge transformations:
U0 transforms under the block-constant fine gauge, a transforms by the
unitary adjoint at its owner, and j_N and all full colour contractions are
invariant. Uniqueness of b_u and the determinant branch preserve this.
At identity its linear term vanishes by global SU(N) invariance. The
quadratic Ward identity is therefore `Pi(p)d_c(p)=0`. Analyticity from
BM25 implies Pi(0)=0. Diagonal components on a coordinate axis are even
by the real Hessian symmetry and translation covariance. BM26 is thus
finite without dividing an unremoved mass term by P^2. Direct differentiation
of the Fourier series bounds each beta_mu nu by C_mom A, after harmless
fixed normalization factors; enlarging C_mom by two would also suffice.
At identity the ordinary exponential-coordinate Hessian equals the
symmetrized invariant group Hessian: their coordinate correction multiplies
the vanishing first gradient. Only this flat field-order-two extraction is
claimed; it is not a full ordered (6,4) class estimate. The argument preserves
all flat harmonic directions rather than removing them with an infrared
regulator. At finite T the determinant can depend on flat holonomies;
its winding terms remain present until the volume limit just proved.
No vanishing finite-torus harmonic determinant response is asserted.

For a B_4-invariant bulk family beta_av is the F^2 coefficient of LOCOP
L4–L6; its six curvature-plane coefficients coincide and orientation-odd
terms are excluded. T_1 has this invariance by the exact paired-contour
relabeling and the fine gauge quotient. Gamma_1 has it too, including its
measure: two rooted tree sections are related by the unique root-pinned
fine gauge change. Each full tree/Haar factorization has unit gauge volume,
so the induced free-group coordinate change preserves product Haar.
At the classical stationary point its intrinsic tangent Jacobian therefore
has determinant of modulus one. The intrinsic Hessian determinant and the
normalizer amplitude in BM23 transform together, and the classical branch
is identified by uniqueness. One can restrict the fixed domain further
to the common neighborhood of the finitely many reflected/permuted trees.
This proves the stated bulk symmetry without assuming that an individual
fixed-tree coefficient is spatially symmetric. The finite-u density
critical point need not be invariant under a nonlinear change of tree
coordinates; no exact B_4 assertion for P_u alone is needed. Its marginal
projection is the explicitly defined beta_av, and any anisotropic
second-moment component of E_pref is bounded by BM25 as well.

Apply BM25 separately to Gamma_1 and E_pref in BM21. Since constants have
zero marginal, linearity and BM10 give the actual bare-prefactor result

    u'_pref:=beta_av[-log P_u]
          =u+b1(N,L,kappa)+O(u^-1),
    b1=beta_av[Gamma_1],
    |b1|<=C_mom(C_1+C_D/2),
    |u'_pref-u-b1|<=C_mom C_E/u.                         (BM27)

The harmless fixed factor two just mentioned may be included in C_mom.
Thus u'_pref=u+O(1) uniformly in volume in this volume-first coefficient
convention. This is not a volume-uniform total-action estimate. The
first action contribution to b1 is the explicit alpha_act in BM18.

Here is the remaining determinant computation, with no suppressed branch
or colour. In BM26 let primes mean total epsilon derivatives, and let
`K=K_T(V(epsilon))` at the actual tree critical point. For each plane,

    b_det,mu nu=lim_(P->0) lim_(T->infinity)
      avg_theta (1/(lambda_P T^4))
                   Tr[K^-1 K''-K^-1 K' K^-1 K']|_0,
    b1=alpha_act+(1/12)sum_(mu!=nu) b_det,mu nu.          (BM28)

All d modes and D colours are traced. The derivatives include the motion
of the actual tree critical field. At epsilon=0 their exact definitions are

    b_T'=-K0^-1 F_T,a epsilon,
    b_T''=-K0^-1[F_T,a epsilon epsilon
          +2F_T,aa epsilon b_T'+F_T,aaa[b_T',b_T']],
    K'=F_T,aa epsilon+F_T,aaa b_T',
    K''=F_T,aa epsilon epsilon+2F_T,aaa epsilon b_T'
                   +F_T,aaaa[b_T',b_T']+F_T,aaa b_T''.   (BM29)

Partial epsilon derivatives in BM29 hold a fixed and differentiate the
actual exponential coarse field and brick lift. These are not derivatives
of a substituted Wilson action. The matrices and vertices are specified
by BM1/BM3 and the full SU normalizer saddle. BM25 and the gapped inverse
justify the differentiations, the volume limit and the two spatial moments.
BM28 is an explicit limit of finite matrix traces to be evaluated, or
equivalently an infinite-volume one-loop Brillouin integral with these
actual vertices.
It is not evaluated here. In particular neither its sign nor a standard
universal beta coefficient is inserted as a computed answer.

There is also a fully finite-u formula: replace K in BM28 by K_u^*, include
its actual critical-field derivatives from F_u, and add the action coefficient
from BM13. This equals beta_av[-log P_u] exactly. BM27 is its controlled
large-u expansion. BM23 explains why the large Haar part of alpha_act must
be combined with the coordinate determinant before any physical comparison.

## 7. Scope, antecedents and what remains

The established claims are BM5/BM8 (the full classical quadratic Schur form),
BM10/BM11 (unit infrared coefficient and its non-Wilson finite-momentum
symbol), BM13–BM18 (actual finite-u critical-action formula and its first
marginal correction), and BM21–BM29 (fixed-domain full-prefactor coefficient
matching with an uncomputed loop trace). No arbitrary reader rate is claimed;
BM22 and BM25 display the rate and radius costs. Sources are fixed at zero,
and no derivatives of a hard selector or selected history are taken.

This does not complete REALRGA, MIXSMALL or the effective action class.
One still needs the actual source/field domains of the entire returned
potential, its tensor extraction and spatial remainder estimates, matching
of the nonlinear tree action beyond its marginal, all histories and their
compact activities, and an iteration with the returned law and parameters.
WR's bare weighted-return jet theorem is a separate small-remainder supplier;
it does not turn BM27 into a repeated trajectory. Positivity, non-freeness,
continuum limits and a physical continuum gap are not inferred.

Bałaban's local effective-action and coupling-extraction programme and
Dimock's gauge/localization expositions are the architectural antecedents.
The precise local producers consumed here are CB1–CB8, FK16–FK21,
FU's fixed-domain branch, CA7/CA11, CD's full determinant homotopy,
IC9–IC13 and IC25–IC32, and LOCOP L4–L7. The earlier LINEAR_PACKAGE
root/straight identity and UL8's tree normalization are credited rather
than presented as new. No all-depth UL loop coefficient is imported.

Three primary literature comparisons were read at the stated bounded scopes:

* Bietenholz–Wiese, [hep-lat/9510026](https://arxiv.org/abs/hep-lat/9510026),
  section 3, equations (3.1)–(3.18): gauge-covariant free-gluon averaging,
  the leg-direction factor and a projected Gaussian inverse. Their input
  is a continuum free Abelian field and their smearing has extra parameters.
  BM6–BM11 instead use the finite-L Wilson covariance and this scalar-kappa
  arithmetic-contour kernel. No perfect-action or interacting theorem is
  transferred from that model.
* Lüscher–Weisz, [hep-lat/9504006](https://arxiv.org/abs/hep-lat/9504006),
  section 5.1, equations (5.1)–(5.4): a multiplicative lattice background
  chart and its adjoint fluctuation transformation. Their perturbative
  background/BRS gauge fixing differs from the probability-Haar rooted
  tree quotient here. Their renormalization theorem is not used to assign
  a value to BM28 or to infer a continuum construction.
* Dimock, [arXiv:1410.2798v3](https://arxiv.org/abs/1410.2798v3),
  section 2.1–2.2, equations (6), (12)–(15): tree path integrals, order
  averaging and covariance in an Abelian theory. The exact group/Haar
  change between non-Abelian rooted sections used above is proved directly,
  with its measure retained. No d=3 scalar/QED estimate becomes a four-
  dimensional SU(N) theorem by citation.

Bałaban CMP109 (1987), 249–301, DOI
[10.1007/BF01215223](https://doi.org/10.1007/BF01215223), is credited for the
small-field effective-action/marginal programme. Its institutional
bibliographic record was checked; the publisher/Euclid full-text fetches did not succeed in this
unit. No unread statement from that paper is a premise. All displayed
model-specific equalities and bounds have their local derivations above.

Only written mathematics and metadata checks were used; no numerical science
run was performed. This source is frozen before its compact provenance packet.
A different fresh hostile review is required. The author assigns neither an
independent LAND nor retained status. The coordinator owns publication and
all shared fronts; predecessor sources and review packets are untouched.
