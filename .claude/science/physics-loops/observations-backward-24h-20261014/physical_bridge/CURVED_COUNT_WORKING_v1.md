# Dynamic vacuum curvature: field comparison and actual coherent counts

Date: 2026-10-15. Author /root. Status: open working derivation; independent
curvature check dispatched before exposure to this source. No observations
opened, state selected, energy budget inferred or action adopted.

## Complete supplied scope

Use the candidate stationary-vacuum linear scalar equation, with physical
coupling delta log A=alpha h and Einstein mass m^2=B H^2, B>12, H>0. The
complete source action and its B formula were read in
EXPONENTIAL_SCALAR_CURVED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-14.md.
The homogeneous scalar perturbation stress is quadratic at that vacuum, so
linear scalar propagation can use the fixed background. This is not a source
solution or a derivation of the actual cosmological environment.

Use the spatially flat de Sitter chart, with conformal time measured from the
initial slice, a(t)=1/(1-Ht), a(0)=1, 0<=t<=T<1/H. This is one chart on the
supplied vacuum, not a claim of a global timelike Killing energy. The physical
metric is A(h)^2 a(t)^2 eta and A(0)=1. Geometric-optics coordinate null rays
are straight, but measured proper time and the body dynamics contain a(t).

## Exact field and observable transformation

The source-free scalar equation is

    h''+2 mathcalH h'-Delta h+a^2 m^2 h=0,
    mathcalH=a'/a=H/(1-Ht).

Set chi=a h. Then

    chi''-Delta chi+V(t)chi=0,
    V=a^2 m^2-a''/a=(B-2)H^2/(1-Ht)^2,
    mu0=sqrt(B-2)H>0.

For any previously derived joint response
O[h]=sum integral[c h-(1-u^2)W.(grad h+u h')], the exact transformed weights are

    W_tilde=W/a,
    c_tilde=[c+(1-u^2)mathcalH W.u]/a.

The second term in c_tilde must not be omitted on a moving reference path.
The clock/orbit adjoint is formed using the curved reference lapse
ell=a sqrt(1-u^2) and its actual reference dynamics, not a flat calibrated
operator with a new field name. The full conformal test-body equation is
u'=-(1-u^2)[mathcalH u+alpha(grad h+u h')], to first scalar order with the
corresponding velocity/position variations in its reference Jacobian.

At the initial a=1 slice, the quadratic Einstein-frame energy measured by
comoving observers is

    E_phys=Q integral[(chi'-H chi)^2+|grad chi|^2+B H^2 chi^2].

The action's scalar kinetic normalization is -Q (partial h)^2, not -Q/2.
The positive frozen-oscillator norm is
N0=integral[chi'^2+|grad chi|^2+mu0^2 chi^2]. With r=1/sqrt(B-2),

    lambda_- N0 <= E_phys/Q <= lambda_+ N0,
    lambda_±=1+3r^2/2 ± sqrt(r^2+9r^4/4).

Indeed the (chi',mu0 chi) block is [[1,-r],[-r,1+3r^2]]; its determinant is
1+2r^2>0 and the spatial-gradient coefficient1 lies between the eigenvalues.
This is a conversion on the specified initial slice, not a conserved global
de Sitter physical energy or a measured upper energy budget. At other slices
the comoving energy has a further 1/a factor after the chi substitution.

## Controlled varying-potential comparison

Write V=mu0^2+U(t), with U C1 on[0,T]. Define

    S=integral_0^T |U|, U0=||U||infinity, U1=||U'||infinity,
    R=exp(S/mu0).

For the displayed de Sitter potential,

    S=mu0^2 H T^2/(1-HT),
    U0=mu0^2[(1-HT)^(-2)-1], U1=2H mu0^2/(1-HT)^3.

For each k let omega=sqrt(k^2+mu0^2), f(0)=1,f'(0)=i omega and
f''+[omega^2+U]f=0. Its variation-of-constants representation is

    f=A_+ exp(i omega t)+A_- exp(-i omega t),
    f'=i omega[A_+ exp(i omega t)-A_- exp(-i omega t)],
    A_+'=iU/(2omega)[A_++A_- exp(-2i omega t)],
    A_-'=-iU/(2omega)[A_+ exp(2i omega t)+A_-],
    A_+(0)=1,A_-(0)=0.

The l1 matrix norm is |U|/omega. Gronwall gives
|A_+|+|A_-|<=R, sum|A_sigma'|<=R U0/mu0, and
sum|A_sigma''|<=R[U1/mu0+U0+U0^2/mu0^2]. The last inequality uses the
derivative of the oscillatory off-diagonal coefficients as well as U'.
Also |f-exp(i omega t)|<=R S/omega and
|f'-i omega exp(i omega t)|<=R S. This comparison preserves the same chi
initial data; its common energy amplitude uses the frozen initial omega.

All following weights are the transformed c_tilde,W_tilde, written c,W for
brevity. Define C=sum||c||1, Wsum=sum||W||1 and D=(1+beta)Wsum. The direct
clock-response difference is bounded globally by R S C/omega^2. The force
difference below any K is bounded by R S D/omega. Hence their radial L2
contributions are bounded using

    integral_0^infinity k^2/(k^2+mu0^2)^2 dk=pi/(4mu0),
    integral_0^K k^2/(k^2+mu0^2) dk<=K.

Only the force needs a high-frequency BV estimate. For each sign sigma and
direction n, put

    d_sigma=1-sigma v n.u,
    b_sigma=(1-u^2)(sigma v n-u)/d_sigma,
    j_sigma=-(b_sigma.W)',
    r_sigma=(b_sigma+(1-u^2)u).W.

After one exact integration by parts the branch force response is
omega^(-1) integral[A_sigma j_sigma-A_sigma' r_sigma]
exp(i sigma omega t-i k n.x). After the second BV integration by parts its
absolute value is <=omega^(-2) TV[(A_sigma j_sigma-A_sigma' r_sigma)/d_sigma].
All zero-extension jumps are retained. Compact continuous W with W' BV and
C3 paths suffice; compact L2 c remains enough for the clock comparison.

Let V_F bound the sum over paths of TV(j_sigma/d_sigma), and G_F bound the
sum ||j_sigma/d_sigma||1, uniformly in sigma,v,n. Let V_R and R_L bound the
corresponding sums TV(r_sigma/d_sigma) and ||r_sigma/d_sigma||1. A conservative
uniform sum of both frequency branches is

    C_F=2R[V_F+(U0/mu0)(G_F+V_R)
                  +(U1/mu0+U0+U0^2/mu0^2)R_L].

Thus the difference from the frozen massive force has high-k bound
(C_F+V_F)/k^2. The factor2 is conservative; it allows the two branches to
attain their suprema at different times.

Computable suppliers use delta=1-beta and B0,B1,B2 from the mass note:

    G_F,A <= [B1||W||1+B0||W'||1]/delta,
    R0=B0+beta, R1=B1+(1+2beta^2)||u'||infinity,
    R_L,A <= R0||W||1/delta,
    V_R,A <= [R1||W||1+R0||W'||1]/delta
                         +||u'||infinity R0||W||1/delta^2.

V_F is the force-only supplier already derived in the mass refinement. Sum
the per-path suppliers. These depend on the calibrated response, not on an
assumed scalar spatial profile.

Combining low/high pieces with the real-energy normalization and minimizing
over K yields the explicit bound

    epsilon_U <= 1/(sqrt(2)pi) [
       R S C sqrt(pi/(4mu0))
                  +2 sqrt(R S D (C_F+V_F))].                         (C1)

If S=0 the operators are exactly equal. If D=0, the force is absent and only
the first term is needed. The cutoff optimizer for nonzero terms is
K=(C_F+V_F)/(R S D); zero cases use the infimum of the all-K bound.
This is a conservative mathematical enclosure for the exact fixed-background
linear evolution, not a finite-frequency quadrature fitted to an expected
answer. Add the independently checked frozen-mass correction epsilon_mu0 to
compare with a massless propagation operator using the SAME transformed,
curved-reference count weights. It is not a comparison to uncorrected flat
clocks or flat reference trajectories.

For an observed scalar contrast with a justified projected error e, the result
would imply

    E_phys >= Q lambda_- max(0,|r|-e)^2 /
                         [sqrt(G0)+epsilon_mu0+epsilon_U]^2.

The denominator-zero case requires separate feasibility. Neither r as a
scalar residual, e, Q,H,B nor an energy upper budget is supplied by this
conditional inequality.

## Derive a curved coherent finite-count contrast explicitly

Choose a comoving station at0 and comoving spacecraft at L e1, with ideal
instantaneous coherent turnaround, source proper frequency constant, and
alpha*kappa absorbed into the displayed response. At reception t, emission
and bounce conformal times are t-2L,t-L. Define d(t)=1-Ht, a=1/d and
P(t)=t-Ht^2/2. The linear comoving orbit/clock equations for chi give

    (a delta u)'=-alpha grad chi,
    xi(t)=xi0+v0 P(t)
                 -alpha integral_0^t [P(t)-P(s)] grad chi(s,x) ds,
    eta(t)=eta0+alpha integral_0^t chi(s,x) ds.

The fixed receiver-proper-time phase response is

    Phi(t)=eta_s(t-2L)-[a(t-2L)/a(t)]eta_s(t)
        +a(t-2L)e1.[xi_s(t-2L)+xi_s(t)-2xi_b(t-L)].

For FOUR equally spaced reception times t_i=t0+i Delta, t0>2L, i=0..3,
choose gamma=(-1,3,-3,1) and beta_i=d(t_i-2L)gamma_i. This is derived from
the actual curved reference, not chosen to match a scalar signal. Since gamma
annihilates polynomials of degree<=2, sum beta=0 and every initial position,
velocity and shared-clock response cancels EXACTLY: beta*a(t_i-2L)=gamma,
P is quadratic, and 1-a_e/a_r=2HL a_e. Transverse first-order position/velocity
coefficients vanish in this straight-line reference; the ideal spacecraft
clock is not independently observed.

The endpoint contrast sum beta_i Phi(t_i) is an actual combination of three
successive proper-time-normalized counts: if Delta_tau_i=tau(t_(i+1))-tau(t_i),
take count coefficient l_i=-Delta_tau_i sum_(j<=i) beta_j. Then its endpoint
coefficients are beta. This conversion is necessary because conformal-time
spacing is not proper-time spacing.

Define compact functions

    F_a^H(s)=sum_i gamma_i [P(t_i-a)-P(s)] 1_(s<t_i-a).

The transformed chi weights are

    W_s=e1(F_2L^H+F_0^H), W_b=-2e1 F_L^H,
    c_s=sum_i gamma_i[d(t_i-2L)1_(s<t_i-2L)
                              -d(t_i)1_(s<t_i)], c_b=0.

The force weights are continuous, compact and have BV first derivatives;
the direct clock weight is piecewise constant. The exact zero-offset column
also cancels:

    integral c_s=sum_i gamma_i[d(t_i-2L)(t_i-2L)-d(t_i)t_i]=0.

This removes the sqrt(mu0) term in the comparison for this observation.
It does not select a homogeneous physical scalar field or a measured H.
Uncertainty in H or the reference operator requires a quantified leakage
bound; numerical near-cancellation is not exact elimination.

At L=3/5,t0=7/5,Delta=1,H=0 the contrast is the difference of the two M6
contrasts. Its exact massless Gram must therefore be329/(54pi), providing an
independent limiting control. At H>0 the massless propagation Gram is computed
with the derived H-dependent weights; their interval endpoints are affine
in the angular variable, allowing exact polynomial integration. No result of
that new computation or independent curvature review is claimed yet.
