# A simultaneous weak-coupling and large-volume gauge-field limit

Personal derivation, 2026-09-16. **Provisional author theorem proposal.**
Depends on the provisional Block02 energy/defect theorem and its restricted
quadratic Wilson matter model. No independent review or audit. This note
addresses equal-time gauge characteristic functions. Fixed-g infrared phases,
fermion correlations, real-time dynamics, finite clocks, and law selection
are separate questions.

Load-bearing dependencies: the [uniform energy and oscillator-defect estimate](BLOCK02_UNIFORM_GROUND_ENERGY_AND_OSCILLATOR_DEFECT.md) and [compact-field bound](BLOCK01_UNIFORM_COMPACT_FIELD_AND_SOFT_RESPONSE.md), both proved in this proposal.

## 1. Statement and normalization

Keep the finite-volume operators P,Z,Q,M,Omega,Omega_p of Block02 and its
translation-invariant normalized full ground-space trace rho. Suppose

    rho[sum_l Q_l^*Q_l+||Z_perp||^2]/V <= delta_(g,L),
    rho(1-cos theta_p)<=B0 g^2,                         (1)

uniformly in plaquette position. Block02 supplies
`delta_(g,L)<=C(sqrt(g)+L^-1)` for the specified paired Wilson model.
The nonnegative quartic term in that theorem can be discarded here.

Let u be a fixed real finite-support link array and v a fixed real
finite-support plaquette array on the infinite cubic lattice, embedded in
each sufficiently large periodic box. Define

    A_(g,L)=P(u)+Z(v),       chi_(g,L)(t)=rho exp(it A_(g,L)),
    kappa_L=u.Omega_L.u+v.Omega_(p,L).v.                 (2)

Smearing is linear in the coefficients, without complex conjugation unless
an adjoint is written. For t in any fixed compact real interval,

    |chi_(g,L)(t)-exp(-t^2 kappa_L/4)|
        <=C_(u,v,tmax)[sqrt(delta_(g,L))+g].             (3)

Constants are independent of g and L. The Fourier symbols Omega(k) and
Omega_p(k) are continuous, including at k=0, and bounded. Therefore local
quadratic forms converge by ordinary Riemann sums, and along every joint
sequence g->0, L->infinity,

    rho exp(i[P(u)+Z(v)])
      -> exp[-(u.Omega_infty.u+v.Omega_(p,infty).v)/4].   (4)

This is the equal-time centered free transverse gauge-field characteristic
functional with the supplied weights. The limiting longitudinal and
harmonic components have zero covariance. The statement is about the
specified ground ensemble and rescaled observables; it does not identify
a photon pole in the interacting theory at fixed g.

## 2. Translation positivity controls nonlocal proof operators

For a complex link smear f write Q(f)=sum_l f_l Q_l. Translation invariance
makes the positive matrix `rho(Q_(x,i)^*Q_(y,j))` block circulant. With the
unnormalized Fourier transform `f_hat(k)=sum_x exp(ik.x) f(x)`, positivity
and the trace identity give

    ||Q(f)||_rho^2:=rho(Q(f)^*Q(f))
       <= [rho(sum_l Q_l^*Q_l)/V] sup_k ||f_hat(k)||^2.  (5)

Indeed, each Fourier covariance block is positive semidefinite. Bound its
quadratic form by its trace times ||f_hat||^2 and sum the blocks with the
factor 1/V. Their trace sum is V times the on-cell covariance trace.
The same argument applies to the self-adjoint vector Z_perp.

At every discrete wave number ||M(k)||<=1. Consequently the smear

    xi=u+i Mv                                             (6)

has a Fourier supremum bounded by the finite-support l1 norms of u and v,
uniformly in L. It follows that

    ||Q(xi)||_rho<=C_(u,v) sqrt(delta),
    ||Z_perp(v)||_rho<=C_v sqrt(delta).                    (7)

This is not an absolute spatial-summability claim about the kernel of M.
Such a claim would be unwarranted for a polar/Riesz multiplier. Formula (5)
is the reason the nonlocal annihilation operator is usable uniformly.

## 3. Algebra of the approximate annihilator

Put B=Q(xi), R=Z_perp(v), and A=P(u)+Z(v). Since M is real,

    A=(B+B^*)/2+R.                                       (8)

The exact basic commutator is

    [P_l,Z_p]=-i S_pl cos theta_p.                        (9)

Let Pi=M^*M and v_perp=(I-Pi)v. Direct substitution of xi into (9) gives

    [B,A]=kappa_L+D(theta),                              (10)
    D(theta)=sum_p f_p(cos theta_p-1),
    f_p=(Su)_p(M^*u)_p+(Omega_p v)_p v_p
                         -i(Su)_p(v_perp)_p.             (11)

For example, the two imaginary cross terms combine into
`-i(Su).diag(cos theta).v_perp`. Its constant part vanishes because
Su belongs to range S and v_perp is orthogonal to that range. The remaining
constant terms are u.Omega.u and v.Omega_p.v. This checks both the sign and
the absence of an imaginary covariance in (2).

By Cauchy--Schwarz, ||M||<=1, and ||S||=||Omega_p||<=w0,

    sum_p |f_p| <= w0(||u||_2^2+||v||_2^2+||u||_2||v||_2).  (12)

In particular, the multiplication commutator is bounded at each finite
volume and its coefficient sum is bounded uniformly in volume. Equation
(1) and `(1-cos theta)^2<=2(1-cos theta)` imply

    ||D||_rho<=C_(u,v) g.                               (13)

## 4. Transport controls defects on the intervening states

At finite g,L, A is a constant first-order angle-translation generator plus
a smooth bounded real multiplication operator. It is self-adjoint on the
domain of P(u), including after restriction to the physical space. Its
unitary `U(r)=exp(irA)` is translation by `r g W_E^(1/2)u` multiplied by a
phase of modulus one. Consequently conjugating a multiplication function
by U(r) just translates its argument; the extra phase cancels.

For a plaquette cosine the argument displacement has magnitude

    |h_p(r)|=|r| g |(W_B^(-1/2)Su)_p|
        <= |r| g b_min^(-1/2)||Su||_2.                  (14)

The sign of the displacement depends on the conjugation order and is
irrelevant for this bound. The pointwise Lipschitz inequality for cosine
and (1) give

    ||(cos(theta_p+h_p(r))-1)||_rho
       <=g[sqrt(2B0)+|r| b_min^(-1/2)||Su||_2].          (15)

Combining (11)-(12) with (15) yields

    ||D U(r)||_rho<=C_(u,v) g(1+|r|).                   (16)

No invariance of rho under U(r) is assumed. This explicit transported
estimate is needed; the untransported bound (13) alone would not justify
the following Duhamel step.

## 5. Characteristic differential equation

All identities can first be evaluated on smooth ground vectors. Finite
volume has a finite-rank smooth ground projection; U(r) preserves smooth
functions. The commutator (10) is bounded, so its Duhamel identity extends
from that core. Differentiability of chi also follows from finite second
moments of A. For t>=0,

    [B,U(t)] = i int_0^t U(s)[B,A]U(t-s) ds
             = it kappa_L U(t)
                       +i int_0^t U(s)D U(t-s) ds.     (17)

The normalized trace state satisfies the useful Cauchy--Schwarz estimates

    |rho(U B)|<=||B||_rho,
    |rho(B^* U)|<=||B||_rho,
    |rho(R U)|<=||R||_rho,                              (18)

where U is unitary and R is self-adjoint. These use B on the ground vectors,
never the generally large creator norm ||B^*||_rho. Using (8) and moving B
past U with (17),

    chi'(t)=-(kappa_L/2)t chi(t)+epsilon(t),
    |epsilon(t)|<=||B||_rho+||R||_rho
                      +(1/2)int_0^t ||D U(t-s)||_rho ds
       <=C_(u,v,tmax)[sqrt(delta)+g].                   (19)

The state Cauchy--Schwarz bound on the integral is valid with the extra
left unitary U(s): `|rho(U(s)X)|<=||X||_rho`.

With chi(0)=1 and kappa_L>=0, variation of constants gives

    chi(t)-exp(-kappa_L t^2/4)
       =int_0^t exp[-kappa_L(t^2-s^2)/4] epsilon(s) ds.  (20)

The kernel is <=1 for 0<=s<=t. This proves (3) for nonnegative t; for
negative t use chi(-t)=overline(chi(t)). With Block02 the coarse error is
O(g^(1/4)+L^(-1/2)+g) for fixed smears. It is not a uniform estimate for
smears whose support or coefficients themselves grow with the volume.

## 6. Infinite volume and remaining obligations

The symbols in (2) are positive square roots of continuous finite-dimensional
matrix functions on the compact Brillouin torus. The square-root map is
continuous even at a zero eigenvalue, so no singular inverse symbol occurs
in kappa_L. Fixed local smears have trigonometric-polynomial Fourier
transforms. This proves the Riemann-sum limit used in (4) and completes the
stated single-exponential characteristic result, conditional on Block02.

A joint algebra/state formulation involving products of these exponentials
requires an additional asymptotic Weyl-product estimate. Matter observables
and factorization also require separate arguments. Neither is silently
included in (4). Real-time evolution is not inferred from this equal-time
result, and no assertion is made about a fixed nonzero microscopic coupling.
