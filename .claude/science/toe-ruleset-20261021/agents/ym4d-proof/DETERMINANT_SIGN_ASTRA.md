# Exact colour reduction and a signed scalar subtraction in the bare coupling

This unit proves new information about the actual coefficient in
[BD](BARE_DETERMINANT_COUPLING_ASTRA.md), without evaluating its remaining
charged contribution. For every N>=2, odd L>=3 and kappa>0,

    b1(N,L,kappa)=N^2 C_L(kappa)-B_L(kappa).

Both functions on the right are independent of N. Their exact matrices
use only scalar and two-by-two colour calculations. The scalar subtraction
has a proved negative bound on an explicit nonempty kappa interval, and an
evaluated fixed-L limit as kappa decreases to zero. Consequently b1/N^2
strictly decreases with N on that interval.

The sign of an individual b1 is STILL OPEN. The result below is not a
negative-sign theorem for SU(N), an evaluated universal beta coefficient,
or an iteration theorem. Full inherited-class closure, a repeated running
trajectory, non-freeness, continuum existence and a positive physical
continuum mass gap remain OPEN.

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

## 1. Literal coefficient, modes and order of limits

The actual mathematical inputs are BD1--BD29, [BM16--BM29](BARE_COUPLING_MATCH_ASTRA.md),
[FK's constrained saddle](FINITE_COUPLING_KERNEL_ASTRA.md), and
[IC30's measure identity](INTERACTING_SELECTED_CORE_ASTRA.md).
Review conclusions are not premises. All original Wilson sources are zero.

The phase is precisely

    F_T=sum_p tr(2I-U_p-U_p^-1)/2
                   +N kappa sum_c [phi_star(M_c)-phi(V_c;M_c)],
    phi(W;M)=tr(W^-1 M^+ + M^- W)/(2N).                  (DS1)

Each mean contains the same 24L^4 paired-order contour words as BD5.
M^- averages their inverses; it is never the inverse of M^+.
The original internal tree is fixed. There are m0=3L^4+1 free links per
coarse cell. Every root, crossing, harmonic and colour mode remains.

Write a_L=(L^2-1)/(12L^2). The coefficient being studied is

    b_N := b1(N,L,kappa)
         = beta_av[sum_c log A_c(U_T)+(1/2)TrLog K_intr],
    K_intr=partial_x^2 F_T(U_T exp x,V)|_(x=0),
    beta_av=(1/12)sum_(mu!=nu) beta_mu nu.               (DS2)

The normalizer amplitude contributes (N^2-1)a_L. The original Haar
Jacobian and coordinate determinant combine exactly into K_intr by BD3;
no ghost determinant, coarse Haar factor or extra Jacobian is added here.
All vacuum constants survive until differentiation annihilates them.

Fix N,L,kappa>0 first. BM's finite-u expansion and BD's volume-first
infrared projection define DS2 on this fixed positive-kappa problem.
In particular volume tends to infinity before the external momentum tends
to zero. Only after that coefficient has been obtained do we consider
kappa decreasing to zero. There is no joint kappa/u/volume limit.
The producer domains and the necessary large-u threshold may depend on
kappa; no positive chart radius uniform down to kappa=0 is asserted.

We retain BD6's scalar matrices and counting normalization:

    A(q)=D(-q)^T D(q), K(q)=A(q)+kappa Q(-q)^T Q(q),
    G(q)=K(q)^-1,       q in [-pi,pi]^4.                 (DS3)

D has 6L^4 rows, Q has four rows, and both have m0 columns. Their entries
are the actual signed path sums with their original owner offsets.
On real q a star denotes conjugate transpose. All integrals below use
dq/(2pi)^4. BD7 supplies a strictly positive gap at every fixed kappa>0,
including q=0. No prime is put on a determinant or inverse.

## 2. Why the constrained saddle simplifies at the required degree

This section proves a finite Taylor identity, not a replacement of the
normalized SU(N) model by a U(N) model.

For one mean near I define

    S=(M^- M^+)^(1/2), W_pol=M^+ S^-1,
    log det W_pol=(1/2)[log det M^+-log det M^-].         (DS4)

Use the principal analytic branches. At real fine fields S is positive
Hermitian and W_pol is unitary. It maximizes Re tr(W^-1 M^+) over U(N):
diagonalize S and use Re R_ii<=1 for the unitary R=W^-1 W_pol.
The maximizing value is tr S.

Every actual path is an SL(N) word. In formal real Lie coordinates let
its logarithm be X_r=X_r,1+X_r,2+..., with tr X_r,j=0. Then

    tr M^+_1=tr M^-_1=0,
    tr M^+_2=tr M^-_2=(1/2)avg_r tr X_r,1^2.

The degree-two logarithmic determinant also subtracts
(1/2)tr(M^+_1)^2=(1/2)tr(M^-_1)^2. Thus DS4 has no terms of degree one
or two: log det W_pol=O(fields^3).

The unitary matrix
W_tilde=W_pol exp[-(log det W_pol)I/N] lies in SU(N) and differs from
W_pol by O(fields^3). Writing log det W_pol=i theta at real fields, their value difference is
exactly tr S times [1-cos(theta/N)], hence O(fields^6).
The actual SU(N) maximum lies between the value at W_tilde and the
full-unitary maximum. Therefore, at real fields,

    0 <= tr S-N phi_star(M) <= C |fields|^6.             (DS5)

FK's actual constrained branch is analytic near I. After composition with
these actual SL(N) path words, real Taylor expansion and polarization of
DS5 give equality with tr S/N through total field degree five. This argument retains the SU(N) scalar
constraint; it proves why that constraint first affects the value at
degree at least six for these SL(N) path inputs.

Put Z=M^- M^+-I. Its degree-one part vanishes, since M^-_1=-M^+_1.
Consequently the actual phase through total field degree four is

    F_loc,4 =
       [sum_(plaquettes owned by cell 0) tr(2I-U_p-U_p^-1)/2
        +kappa sum_(rho=1)^4 tr(I+Z_rho/2-Z_rho^2/8)
        -(kappa/2)sum_rho tr(exp(-B_0rho)M_rho^+
                                      +M_rho^- exp(B_0rho))]_(<=4). (DS6)

Every factor in a word still has BD13's order exp(A_e)exp(x_e), with
inverse exp(-x_e)exp(-A_e). All exponentials and products are truncated
only after preserving this order. The actual words and both arithmetic
means are unchanged. DS6 is a single-trace polynomial with coefficients
independent of N. Its identity/vacuum terms remain in this formula.

A fine Hessian with two external insertions uses total field degree four.
BD10 proves that the critical field's second Cartan variation vanishes;
its first response is exactly

    Phi_mu(p)=kappa G(p)Q(-p)^T e_mu.                    (DS7)

It is independent of N. Thus DS6 computes all vertices used in BD29,
including their actual critical motion. No degree-six statement about
the full determinant or the full effective action follows.

## 3. Colour factors from the stated conventions

Use BD16's real HS-orthonormal anti-Hermitian basis T_a, so
-tr(T_a T_b)=delta_ab. Its completeness identity is

    sum_a (T_a)_ij (T_a)_kl
                   =-delta_il delta_jk+(1/N)delta_ij delta_kl,
    sum_a T_a X T_a=-(tr X)I+X/N,
    sum_a T_a^2=-(N^2-1)I/N.                            (DS8)

To derive the first identity, project a matrix onto its traceless part
using the complexification of this orthonormal basis; the identity
direction supplies the second term. Contracting indices gives the other
two statements. In particular for H=i diag(h_1,...,h_N), with
sum h_i=0 and sum h_i^2=N (the FLOW-unit convention),

    sum_a tr(H^2 T_a^2)=N^2-1,
    sum_a tr(H T_a H T_a)=-1.                            (DS9)

These factors use HS unit fine fluctuations and HS norm sqrt(N) for H.

There is an equally explicit root calculation. Use F_ij=i E_ij, whose
bilinear HS dual is F_ji. Let T_r=i diag(d_r1,...,d_rN) be the neutral
basis. Its completeness is
sum_r d_ri d_rj=delta_ij-1/N. Every cubic coefficient in DS6 is a linear
combination of tr(H[T_a,T_b]): for anti-Hermitian real inputs,
Re tr(H T_a T_b)=tr(H[T_a,T_b])/2, and all polynomial coefficients are real.
Thus neutral cubic entries vanish and a root cubic entry is proportional
to h_i-h_j. The contracted adjoint factor is derived directly:

    sum_(i!=j) (h_i-h_j)^2=2N sum_i h_i^2=2N^2.          (DS10)

Equivalently the HS-basis adjoint Casimir is 2N; multiplying by the
projection colour norm squared N gives 2N^2. This is not an imported
normalization convention.

Here is a complete N-independent recipe for the remaining matrices.
Use DS6 as a formal polynomial calculator in dimension two, including its
unconstrained square-root expression. Put

    H_10=i diag(1,0), H_01=i diag(0,1),
    row colour F_21=i E_21, column colour F_12=i E_12.

Use BD11's external profiles with DS7 and BD17--BD18's exact s,t,z tags
and momentum routing. Define

    v(q;p)  = [s t z] F_loc,4 with H_10,
    W10(q;p)= [s t z_+ z_-] F_loc,4 with H_10,
    W01(q;p)= [s t z_+ z_-] F_loc,4 with H_01.            (DS11)

Define W0(q;p) by the same quartic recipe in dimension one, using H=i
and both fluctuation colours i. All its matrices commute and its cubic
vertex is zero. These small-dimensional substitutions merely evaluate
the universal single-trace polynomial DS6. H_10 is not being passed off
as an SU(2) field, and dimension one is not called SU(1).

For general physical H, a root quartic entry has exactly the form

    W^ij=h_i^2 W10+h_j^2 W01
                      +h_i h_j (W0-W10-W01),
    V^ij=(h_i-h_j)v,
    W_rs=(sum_i h_i^2 d_ri d_si) W0, V_rs=0.            (DS12)

Indeed a trace containing F_ji and F_ij only visits indices i,j; its
remaining two H factors give a quadratic polynomial in h_i,h_j.
When h_i=h_j=1 the background is central on that two-dimensional
subspace, so every such colour trace equals its scalar value and the
quartic matrix is W0. This fixes the mixed coefficient in DS12.
For neutral colours all factors commute, giving its last formula.
The diagonal-torus selection rule excludes all other block mixing.

Summing ALL neutral and root entries yields

    sum_r W_rr=(N-1)W0,
    sum_(i!=j) W^ij=N^2(W10+W01)-N W0.                  (DS13)

The neutral contribution has not been dropped. The sum of the two
quartic traces is N^2(W10+W01)-W0. The exchange trace has factor 2N^2
by DS10 and no neutral contribution.

## 4. Exact reduction of the complete marginal

Set G^+=G(q+p), v^-=v(q+p;-p), and define

    J_C(q;p)=tr_m0[G(q)(W10+W01)
                                  -2G^+ v(q;p) G(q) v^-],
    J_0(q;p)=tr_m0[G(q) W0(q;p)].
    J_N(q;p)=N^2 J_C(q;p)-J_0(q;p).                     (DS14)

The last equality is the full BD20 integrand identity. In particular
there is no extra factor from replacing real root pairs by complex
weight spaces. All entries require only the same m0-dimensional G
and the scalar/two-by-two polynomial calculations in DS11.

Using BD21--BD23's finite momentum-Taylor rules, define

    C_L(kappa)=a_L+(1/24)sum_(mu!=nu)
                    int [P^2]J_C(q;P e_nu) dq/(2pi)^4,
    B_L(kappa)=a_L+(1/24)sum_(mu!=nu)
                    int [P^2]J_0(q;P e_nu) dq/(2pi)^4.
    b_N=N^2 C_L(kappa)-B_L(kappa).                      (DS15)

All constants, the seagull, the exchange and the normalizer amplitude are
retained. The amplitude splits as (N^2-1)a_L=N^2 a_L-a_L.
This is an exact formula for the quadratic marginal, not a polynomial-in-N
identity for the entire interacting action.

At fixed kappa>0 the same gapped finite Laurent inverses as in BD25
justify these integrals and their derivatives. An intrinsic way to carry
their original-reader bounds is to take the finite-volume quadratic
symbols at N=2 and N=3:

    Pi_C=(Pi_3-Pi_2)/5, Pi_0=(4Pi_3-9Pi_2)/5.           (DS16)

Here each Pi includes its amplitude; the subscript 0 denotes the scalar
subtraction, not zero external momentum. DS14 proves DS16 at finite
volume before the limits. Keep the two original source-reader libraries
with their fixed linear coefficients. Their exponential second moments,
canonical agreement and Ward identities are inherited by these finite
linear combinations. No reader is replaced by endpoint support or by a
larger macro-cell. The explicit Fourier formulas evaluate these same
quadratic functions.

In particular Pi_0(0)=Pi_C(0)=0 only after the volume-first identification
of BD25--BD26. No pointwise integrand Ward cancellation is assumed.
The full finite-momentum symbol is not replaced by a Wilson symbol.

## 5. A direct scalar curvature formula

We next evaluate enough of B_L to obtain a sign. No analogous positivity
claim is made for C_L.

For a formal constant infinitesimal coarse curvature F in one plane
mu<nu, BM16 gives fine curvature F/L^2. Its paired contour integrals are

    ell_(rho,y,pi)=B_rho+F s_(rho,y),
    s_(mu,y)=-y_nu/L, s_(nu,y)=y_mu/L,
    s_(rho,y)=0 for rho outside {mu,nu}.                 (DS17)

The common order pi at the two endpoints makes the axial terms cancel.
Their mean is B_rho, and d_f^* of the constant fine curvature is zero.
Thus this field solves the linear classical stationary equation for every
kappa. The gapped inverse uniquely identifies it with DS7's infrared
derivative. BD10 removes its second critical variation. These are the
actual critical profiles, not the brick lift substituted for them.

The affine test is a test of finite jets, not a chart integral on an
unbounded affine field. To see the precise identification, write the
translation-invariant quadratic kernel of Pi_0 as H_mu nu(r).
Its original-reader second moments give absolute convergence of
sum_r |r|^2 |H_mu nu(r)|. The Ward cancellation of its zero-momentum
part rewrites the same-component quadratic form in differences.
For A_mu(X)=-F X_nu the resulting coefficient per cell is
-F^2 sum_r r_nu^2 H_mu mu(r)/4. This equals F^2 beta_mu nu/2.
Thus one may evaluate the local degree-two curvature coefficient and
sum it using those moments. No nonperiodic field is inserted on a torus
and no hard-cut domain is extended.

For the scalar polynomial calculator, let l_(rho,r)(q) be the actual
linear row of one contour; r=(y,pi). Its mean is Q_rho(q).
At curvature F the scalar mean, allowing fine fluctuation x, is

    M=exp(i B_rho) avg_r exp(i F s_r+i l_r x),
    R(F)=avg_r cos(F s_r), theta(0)=B_rho,
    partial_x theta=avg_r[cos(F s_r) l_r]/R(F).           (DS18)

The y distribution is symmetric, so the sine average vanishes.
The exact scalar normalized classical kernel is
kappa R[1-cos(theta-B_rho)]. At x=0, theta=B_rho; its fine Hessian
is therefore kappa R (partial_x theta)^* (partial_x theta).
Define v_rho=avg s_r^2 and T_rho^(mu nu)=avg s_r^2 l_r. Expansion gives

    [F^2]K_kernel,rho
       =(kappa/2)[v_rho Q_rho^*Q_rho
              -Q_rho^* T_rho^(mu nu)-(T_rho^(mu nu))^* Q_rho],
    [F^2]K_Wilson=-(1/(2L^4))D_mu nu^*D_mu nu.           (DS19)

D_mu nu consists of the L^4 fine plaquette rows in that plane.
There is no linear F term in this scalar Hessian, so there is no exchange
term to discard in this calculation. This does not apply to charged roots.

The scalar amplitude's logarithm is -log R/2 up to constants; its F^2
coefficient is v_rho/4. Equivalently it is the one copy of a_L fixed
already by DS15. Since v_mu=v_nu=a_L, its beta contribution is a_L.
The determinant contributes tr(G [F^2]K) to beta: the one-half in TrLog
and the factor two converting the F^2 coefficient into beta cancel.

Now average the twelve ordered planes. Define the four rows

    w_(rho,y)=(1/(6L^2))sum_(eta!=rho) y_eta^2,
    T_rho(q)=avg_(y,pi) w_(rho,y) l_(rho,y,pi)(q),
    avg w_(rho,y)=a_L/2,
    U(q)=T(q)-(a_L/2)Q(q).                              (DS20)

The factor 1/6 is exactly the twelve-plane average of DS19.
The Wilson row sum becomes D^*D. Thus the following formula is exact:

    B_L = a_L
        -(1/(12L^4)) int tr[G A]
        -(kappa a_L/4) int tr[QGQ^*]
        -kappa Re int tr[QG U^*].                       (DS21)

It includes both the positive normalizer-amplitude term and every scalar
seagull contribution. It has no momentum derivatives or omitted boundary
link type.

## 6. The paired-contour ribbon and its explicit norm

We need a bound on the last term of DS21. It follows from the actual
paired-order geometry, rather than a sign assumption about that term.

Let h=(L-1)/2. Let l_ref be the straight root-to-root contour row in
direction rho. The loop formed by a contour and the reversed reference
bounds the ribbon obtained by translating its axial root path through L
steps in direction rho. A step parallel to rho contributes no plaquette;
each of the other |y_eta| steps contributes L plaquettes. Consequently
there is a signed fine plaquette row R_r with

    l_r-l_ref=R_r D,
    sum_(plaquettes and owner offsets) |(R_r)_p|
                        <=L sum_(eta!=rho)|y_eta|<=3Lh. (DS22)

One can build this ribbon strip by strip in the order of that same axial
path. Its top edge is the translated endpoint path precisely because the
orders at both ends are paired. All strips stay in the two-block brick.
Negative steps carry their actual orientations. This proves DS22 also
on the tree quotient, since setting tree cochain values to zero commutes
with the boundary identity.

Since w>=0 and avg w=a_L/2,
avg |w-a_L/2|<=a_L. The reference row cancels from DS20, giving

    U=R D,  R_rho=avg_r (w_r-a_L/2) R_r,
    row absolute coefficient sum of R_rho <=r_L,
    r_L=3Lh a_L=(L-1)(L^2-1)/(8L),
    tr[R(q)R(q)^*]<=4r_L^2             (real q).        (DS23)

This representation is used for an estimate; it does not reassign any
original contour reader. The full original word and owner labels remain.
All boundaries and repeated occurrences in the two-block bricks are
retained.

Because D^*D<=K, we have DGD^*<=I. Hence

    tr[U G U^*]<=tr[R R^*]<=4r_L^2.                    (DS24)

This estimate is uniform in volume, q and positive kappa.

## 7. An exact Schur split retaining the root mode

Let d(q)_rho=exp(iq_rho)-1. The brick injection E satisfies
E^*E=L^3 I, Q E=I, and D E d=0. For q!=0 modulo 2pi set

    g(q)=E d(q)/(L^(3/2)|d(q)|), w(q)=Q g(q),
    |w(q)|^2=L^-3,
    P(q)=d(q)d(q)^*/|d(q)|^2, H(q)=g(q)^perp.            (DS25)

The nullspace of D(q) is exactly span(g). For completeness, unitarily
unfold the quasi-periodic fine cell into its L^4 momenta
k=(q+2pi n)/L modulo 2pi. At one such momentum the elementary identity
sum_(mu<nu)|d_mu a_nu-d_nu a_mu|^2=|d|^2|a|^2-|d^*a|^2
shows that at nonzero k the fine curl has just its one gradient direction
in the kernel. There are L^4 such directions when
q!=0. Internal tree fixing removes L^4-1 independent gradients and leaves
the single root gradient displayed in DS25. At q=0 the extra fine harmonic
directions remain; there are four kernel directions, not one.

Write A_H and Q_H for the restrictions to H(q), and define

    Q_T=(I-P)Q_H,
    S=A_H+kappa Q_T^*Q_T.

In the orthonormal splitting span(g) plus H, the FULL matrix K is

    [ kappa/L^3              kappa w^* Q_H             ]
    [ kappa Q_H^* w          A_H+kappa Q_H^* Q_H        ].

Its exact Schur complement is S. In particular

    det K=(kappa/L^3)det S,
    QGQ^*=P/kappa+Q_T S^-1 Q_T^*,
    QG U^*=Q_T S^-1 U_H^*,
    UGU^*=U_H S^-1 U_H^*.                              (DS26)

Here U g=R D g=0. These are elimination identities which retain the
longitudinal factor and reconstruct the full covariance; they are not
mode deletion. For example the omitted upper-left entry of G is
L^3/kappa+L^6 w^*Q_H S^-1 Q_H^*w, and the upper-right entry is
-L^3 w^*Q_H S^-1.

At q=0 continue to use the full K and G of DS3. On every finite torus its
harmonic modes are present. Their isolated q=0 contribution disappears
from a normalized trace only in the fixed-kappa volume limit. DS26 is
used under that limiting integral, not to discard a finite-volume mode.

Also kappa QGQ^*<=I_4. Define

    y_kappa=kappa int tr[QGQ^*]-1
            =kappa int tr[Q_T S^-1 Q_T^*],  0<=y_kappa<=3,
    x_kappa=Re int tr[QG U^*].                          (DS27)

The integral of tr P is one. Cauchy--Schwarz with DS24 and DS26 gives
the important estimate with the longitudinal part removed exactly:

    kappa |x_kappa|<=2r_L sqrt(kappa y_kappa).           (DS28)

No sign of x_kappa was assumed.

## 8. Explicit bound, limit and admissible interval

Use tr(GA)=m0-kappa tr(QGQ^*) in DS21 and put

    g_L=(3L^2+1)/(16L^2),
    d_L=(L^4-L^2-4)/(48L^4)>0       for L>=3.

The complete scalar expression becomes

    B_L(kappa)=-g_L-d_L y_kappa-kappa x_kappa.           (DS29)

Together with DS28 and completion of the square this yields

    B_L(kappa)
       <=-g_L-d_L y_kappa+2r_L sqrt(kappa y_kappa)
       <=-g_L+(r_L^2/d_L)kappa.                         (DS30)

In particular the explicit nonempty interval is

    0<kappa<=kappa_star(L):=g_L d_L/(2r_L^2)
      =((3L^2+1)(L^4-L^2-4))/
                    (24L^4(L-1)^2(L^2-1)^2),

    B_L(kappa)<=-g_L/2=-(3L^2+1)/(32L^2).              (DS31)

For example L=3 gives kappa_star=119/31104 and B_3<=-7/72.
These are exact rational values obtained from DS23 and DS29, not numerical
estimates of a loop integral.

There is also a controlled two-sided fixed-L asymptotic. Let
C_T=2L^2(4L-3). The linear map which gauges an arbitrary quasi-periodic
fine cochain to the internal tree has at most 1+8h=4L-3 total absolute
coefficients per output edge. It has 4L^4 rows, so its operator norm is
at most C_T.

For a tree cochain a in H(q), decompose its full fine cochain into the
orthogonal transverse part a_perp and a gradient. Tree fixing sends that
gradient to a root gradient; projection onto H removes it. Thus
|a|<=C_T |a_perp|. In the fine Bloch decomposition,

    |D a|^2 >= (4|q|^2/(pi^2 L^2)) |a_perp|^2,

since the smallest fine alias eigenvalue is
4 sum_rho sin^2(q_rho/(2L))>=4|q|^2/(pi^2 L^2).
It follows that

    A_H >= (4|q|^2/(pi^2 L^2 C_T^2)) I,   q!=0.         (DS32)

Each actual contour has length less than 5L; hence
||Q(q)||_F^2<=100L^2. Since S>=A_H and the normalized integral of
|q|^-2 over the Brillouin cube is at most its value 1/4 over the enclosing
four-ball of radius 2pi, DS27 gives

    y_kappa<=kappa M_L,
    M_L=(25pi^2 L^4 C_T^2)/4
                         =25pi^2 L^8(4L-3)^2.          (DS33)

All comparisons here are on the positive H block; they do not apply
an inverse to the singular full curl matrix. Combining DS28--DS29 gives

    |B_L(kappa)+g_L|
                <=(d_L M_L+2r_L sqrt(M_L))kappa,
    lim_(kappa down to 0) B_L(kappa)
                         =-(3L^2+1)/(16L^2).            (DS34)

The constants are deliberately loose but explicit. This is a fixed-L
statement, not a large-L asymptotic. The limiting value is not obtained
by setting kappa=0 in the original fine integral, whose root sector would
then be singular.

## 9. What the new sign result decides and what it does not

For any integers N>M>=2 the exact colour formula gives

    b_N/N^2-b_M/M^2
                       =B_L(kappa)(1/M^2-1/N^2).         (DS35)

Thus throughout DS31's admissible interval,

    b_N/N^2-b_M/M^2
               <=-(g_L/2)(1/M^2-1/N^2)<0.               (DS36)

The same actual-coefficient difference has the evaluated kappa limit
-g_L(1/M^2-1/N^2), with the error from DS34. No limit or bound on C_L
is needed for these comparisons. Once one b_M were proved nonpositive,
DS36 would prove strict negativity for every larger N on the same
parameter point. At present that additional input has not been proved.

An individual sign still depends on C_L. Its charged seagull and exchange
both survive in DS14; neither is replaced by its sign before the
P^2 projection. The exact root Schur split does not by itself control
those external-momentum derivatives, the kappa-dependent Phi derivatives,
or the small-q charged integrand as kappa decreases to zero. Accordingly
no logarithmic asymptotic or universal coefficient is asserted for C_L.

The result materially reduces the outstanding computation: all N share
one m0-dimensional charged integral and the scalar quantity with the
rigorous interval and asymptotic above. A future certified computation
could use DS11--DS15 and DS21--DS34 with interval matrix inverses and
integration errors. It must be separately preregistered. No scientific
numerics, trial sign scans or symbolic coefficient-evaluation runs were
performed for this unit.

The [BR original-cut remainder](BARE_COUPLING_REMAINDER_ASTRA.md) remains a
separate bounded supplier matching BM's literal prefactor. It does not
evaluate C_L or turn these bare coefficients into a repeatable flow.
The original action, all normalization, complete readers, and the
volume-first convention have been preserved. No positivity, non-freeness,
all-history closure, continuum existence or physical-gap theorem is added.

## 10. Primary-literature comparison and provenance

The following bounded reads informed the choice of calculation, without
carrying any mathematical step of the proof.

- Adams and Lee, [arXiv:0709.0781v3](https://arxiv.org/pdf/0709.0781v3),
  section II, (7)--(15), require specified lattice scaling, continuum
  polynomial limits, denominator positivity, a doubler-free condition and
  infrared finiteness. Their logarithmic universality result does not
  supply a bound on this changing-size, constrained tree-block matrix
  family or its finite scheme term. No large-L or small-kappa charged
  asymptotic is imported.
- Hasenfratz and Niedermayer,
  [hep-lat/9706002v1](https://arxiv.org/pdf/hep-lat/9706002v1),
  introduction and section 4, (4.1)--(4.5), distinguish a fixed-point action
  from the finite-kappa marginal operator in the two-dimensional O(N)
  sigma model. Neither their fixed-point input nor their perturbative
  trajectory describes this incoming four-dimensional Wilson step.
- Carena, Gustafson, Lamm, Li and Liu,
  [arXiv:2208.10417v1](https://arxiv.org/pdf/2208.10417v1),
  (9)--(21), (25)--(29), derive background-field quadratic interactions
  for anisotropic U(1)/SU(N) Wilson theory, including the scalar seagull
  and the non-Abelian gauge-fixing/ghost terms. Their generator and
  background-gauge conventions differ from this tree quotient. DS8--DS34
  rebuild the colour and scalar calculation with the actual normalized
  paired-contour kernel. No tabulated coefficient or numerical result is
  imported.

Bałaban and Dimock are credited for the constructive localization and
marginal-extraction architecture behind the local suppliers. The precise
suppliers here are FK's constrained SU saddle, BM's affine critical
response and complete-reader moments, and BD's literal intrinsic
determinant and finite-word projection. All new identities are proved
above for those actual objects.

The mathematical source freezes before the compact
[read manifest](checks/determinant_sign_read_manifest.json) and
[author receipt](checks/determinant_sign_receipt.json). A DIFFERENT fresh
source-first hostile reviewer is required, especially for DS5, the
neutral/root contractions, the affine scalar projection, the ribbon
bound and the retained-root Schur complement. The coordinator owns
publication, Git, shared fronts and audits. No predecessor source or
packet is edited and the author assigns no independent verdict.
