# A parameter-free finite-wavelength benchmark on the winding matching

2026-09-21. Root derivation and analysis protocol, written after seeing the
mode-averaged N<=128 production outcomes. This is an explicitly post-outcome
mechanistic follow-up. No parameter is fitted to those outcomes. The existing
production protocol, analyzer and original assessment remain unchanged.

The objective is to distinguish finite-wavelength damping and dispersion
already present in the supplied microscopic generator from an implementation
error or an unjustified asymptotic interpretation. The exact first-derivative
calculation below is stronger than a phenomenological fit. Exponentiating
that derivative is still only a closure benchmark at gamma!=0.

## 1. Exact orthogonal projection of the generator

Use the winding matching with every white endpoint w_u=u+e_1 and the uniform
fourteen-color law. A nonfixed routing channel is a translation by

    a_delta = delta-e_1.

The six directions remain present; the fixed direction contributes zero.
Let k=Q/N, z_delta=k.a_delta, and let F(k) be the normalized six-component
Fourier field (E,B) with covariance I_6, as in the frozen production protocol.
Define P as the L2 projection onto the linear single-color Fourier functions
at this wavevector. Constants and the seven unused color moments are treated
in the full tangent space before restricting to these six moments.

Write A_delta for the probability-current Jacobian before restriction. At
uniform p, S_delta p=0 and A_delta=2 diag(p) S_delta. For the **actual** local
current c_delta(eta)(xi_u-xi_v), conditioning on one of its four colors gives
these exact linear projection coefficients, in order (l,u,v,r):

    A_delta/4,  (k0/2)I,  -(k0/2)I,  A_delta/4,           (1)

on the probability tangent. The two middle coefficients include the usual
mean subtraction outside that tangent. The factor 1/4 in the context terms
includes the physical outer rate half.

For phi(u)=exp(-ik.u), the Fourier coefficient of the exchange is
phi(u)(exp(-iz_delta)-1). The four single-site fields in (1) reindex with
multipliers exp(-iz_delta),1,exp(+iz_delta),exp(+2iz_delta). Consequently

    P L F(k) = B(k) F(k),
    B(k) = -d(k) I_6 - i A_6(q_eff(k)),                   (2)
    d(k) = 2 k0 sum_delta sin^2(z_delta/2),
    q_eff(k) = (1/2) sum_delta
                        [sin(2z_delta)-sin(z_delta)] delta.

Here A_6(q)=[[0,-c C_q],[c C_q,0]], C_q v=q cross v, and
c=2/7 at the production values gamma=1, uniform colors. For a general gamma
the signed coefficient in A_6 is 2 gamma/7. The anti-Hermitian drift -i A_6
and scalar negative symmetric part have the same conventions as the original
analysis. In particular q_eff(k)=k+O(|k|^3).

The scalar symmetric part is already anisotropic in this winding fixture.
For the fundamental phase theta=2pi/N,

    k=theta e_1:
      d=2k0[sin^2(theta)+4 sin^2(theta/2)],
      q_eff=(1/2)[sin(4theta)-sin(2theta)]e_1;

    k=theta e_2 or theta e_3:
      d=4k0 sin^2(theta/2),
      q_eff=[sin(2theta)-sin(theta)]e_i.                  (3)

Thus d(theta e_1)=4k0 theta^2+O(theta^4), whereas the other
two axes have d(theta e_i)=k0 theta^2+O(theta^4). This anisotropy is a
property of the chosen winding matching, not an anisotropic rate parameter
fitted to the data. On the Euler observation scale, N d(Q/N)=O(1/N).

## 2. What exponentiating the projection does and does not establish

Let C(t)=E[F(t)F(0)^dagger] at microscopic time t. Equation (2) gives the
exact initial derivative C'(0)=B(k). It does not in general imply
C(t)=exp(tB(k)): the generator also sends linear functions into higher-degree
color functions. At gamma=0 the rates are constant swaps, the linear space
is invariant, and this exponential covariance is exact. At gamma!=0 this
requires an additional closure that has not been proved.

There is a useful finite check of that distinction. The symmetric exchange
part preserves the linear space and the remaining part is antisymmetric in
the invariant product L2 space. If R=(I-P)L F, then

    C''(0) = B(k)^2 - E[R R^dagger].                      (4)

The last matrix is positive semidefinite. A nonzero value explicitly rules
out identifying the projected exponential with the exact finite-time
covariance in that example. A four-position routing cycle with the same
four-distinct-context rate law is an auxiliary finite control; it is not
the excluded N=4 physical cubic torus.

The winding benchmark uses

    C_proj(N,t) = exp(N t B(Q/N))                          (5)

at the original five macroscopic times, without fitting or adjusting k0,
gamma, wave speed, initial variance or damping. It is labelled a projected
generator benchmark throughout. The conditional Euler theorem remains a
separate asymptotic proof; agreement with (5) is not a proof of a diffusive
correction law or a stronger theorem.

## 3. Observables and prospective comparison

With the same continuum predictor U, transverse/longitudinal projectors and
anti-Hermitian rotation D used by the original analyzer, benchmark values
for the four original statistics are

    error = 2 - Re tr(U^dagger C_proj)/3,
    transverse auto = Re tr(P_T C_proj)/4,
    signed cross = Re tr(D^dagger C_proj)/4,
    longitudinal auto = Re tr(P_L C_proj)/2.              (6)

The error uses exact stationary equal-time covariance I_6 at both endpoints;
it does not pretend that (5) is a deterministic dissipative trajectory with
decaying equal-time variance. Retaining this distinction is essential for
the propagation-error comparison.

Before printing or comparing production by-axis aggregates, freeze the exact
local projection controls, the auxiliary-cycle closure countercontrol and
all predictions for N=16,32,64,128,256. Then compare the original winding
cells by axis and by the original three-mode average, with the original
whole-history uncertainty. No fitted damping coefficient, selected subset,
rescaled observation time or revised original protocol is allowed.

The irregular matching is not translation invariant and has no scalar
Fourier symbol (2); it is outside this proposed benchmark. A future
inhomogeneous projected-generator computation would require its actual
matching operator, not insertion of an averaged dimer direction into (2).
No result from the still-running N=256 follow-up is used to choose (1)-(6).
