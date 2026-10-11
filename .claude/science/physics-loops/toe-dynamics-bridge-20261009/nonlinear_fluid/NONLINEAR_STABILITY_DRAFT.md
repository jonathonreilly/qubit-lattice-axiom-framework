# Nonlinear fluid stability — root derivation

Source contract: the unchanged D3Q27 parent at
73a76d2141d30d75c6aebfb2f2f9baa6e0a025bf, with current main
a13caa4885f547c8d206265b031ba7649e539fd9. This is a proposed proof for
independent checking, not an audit verdict. Root derived the stability estimate;
a separate probe derives all correctors and finite moment identities.

## 1. Model and bilinear algebra

Use V={-1,0,1}^3, e=|v|^2, M_v=(2/3)^(3-e)(1/6)^e, and all 288
reversible four-distinct-velocity collisions ij <-> kl preserving v and e.
Let nu_r=e_k+e_l-e_i-e_j, W=diag(M), q_r=kappa_r M_i M_j,
B=W^-1 sum_r q_r nu_r nu_r^T. All rates are fixed and positive. Let P be
the M-orthogonal projection onto K=span{1,v_x,v_y,v_z,e}, Q=I-P,
R=(B+P)^-1-P, and lambda>0 the least positive eigenvalue of B.

Define the real symmetric bilinear map

    Gamma(g,h) = W^-1 sum_r (q_r/2) nu_r
        (g_i h_j+g_j h_i-g_k h_l-g_l h_k).

Then for every pair of fields P Gamma(g,h)=0. For U in K,

    Gamma(U,U)=B(U^2/2).

The latter follows reaction by reaction from U_i+U_j=U_k+U_l, so
(U_k^2+U_l^2-U_i^2-U_j^2)/2=U_i U_j-U_k U_l. These identities hold
pointwise for spatially varying coefficients. No factorization of random
variables is involved.

The actual nonlinear kinetic equation for f=M(1+delta g) is exactly

    g_t + T g/delta + B g/delta^2 = Gamma(g,g)/delta,
    T=diag(v) dot grad_x,

on the normalized torus (R/2pi Z)^3. This uses fluctuation amplitude delta,
unlike the earlier delta^3 limit. The collision law, streaming and clock
are supplied mathematical premises.

## 2. Explicit Sobolev constants

For integer s>=3 use the weighted Fourier norm
||g||_s^2=sum_k (1+|k|^2)^s sum_v M_v |g_hat_v(k)|^2.
Write m=min_v M_v=1/216 and S=sum_r q_r. The shell count
(2n+1)^3-(2n-1)^3=24n^2+2 gives

    sum_{k in Z^3}(1+|k|^2)^(-s)
       <= 1+26[1+1/(2s-3)] < 36.

Thus ||g_v||_infty <= E ||g||_s with E=6/sqrt(m).
Weighted Fourier convolution gives, for any scalar fields,

    ||ab||_{H^s} <= C_s ||a||_{H^s} ||b||_{H^s},
    C_s=6*2^s.

Indeed <k>^s <= 2^(s-1)(<l>^s+<k-l>^s), followed by Young's
convolution inequality and the preceding Fourier l1 bound, proves the claim.
This proof first applies to finite Fourier sums and then to their limits.

A deliberately conservative explicit bilinear bound is

    ||Gamma(g,h)||_s <= G_s ||g||_s ||h||_s,
    G_s=4 C_s S/m^(3/2).

For one reaction ||W^-1 nu||_M<=2/sqrt(m), and each scalar component
has H^s norm <=||g||_s/sqrt(m). Applying the scalar product bound to the
four products with the factor 1/2 proves the displayed constant by summation.
P, Q and B commute with Fourier differentiation and Sobolev weights.
Conservation therefore also gives exact H^s orthogonality
<e,Gamma(g,h)>_s=<Qe,Gamma(g,h)>_s.

## 3. Full correctors and fluid equations

Now use the parent's supplied isotropic rate
alpha=(-4579+3 sqrt(7614177))/1072 on its nine axial exchanges and unit
rates on the other reactions. Set nu=67/361 and D=4/49. Let real smooth
periodic fields rho,j,pi be given on [0,L], satisfying

    div j=0,
    j_t + (j dot grad)j + grad pi = nu Delta j,
    rho_t + (2/5) j dot grad rho = D Delta rho.

Only a supplied smooth lifetime is claimed, not global 3D regularity.
Take pi to have zero spatial mean, define A=(5-3e)/2 and

    U=rho A+3j dot v.
    H(r,J,E)=r A+3J dot v+(3/2)E(e-1).

H has moments (r,J,E). The periodic mean of rho_t is zero because
div j=0. Define the local vector F1=(2/5)rho j-D grad rho, and set

    J1=F1-mean(F1),
    E1=3pi+|j|^2-mean(|j|^2),
    w=Q(U^2/2)-RTU+H(0,J1,E1),
    z=R[2 Gamma(U,w)-U_t-Tw].

The spatially constant subtraction in E1 fixes its mean and has no effect
on the corrector solvability. In particular w has zero spatially integrated
mass, momentum and energy, and z has zero moments pointwise.

All five components of P(U_t+Tw)=0 must be checked, not only its Leray
projection. The parent supplies the following complete moments of the
microscopic portion of w:

    mass flux = 0,
    stress = j tensor j - (|j|^2/3)I - 2nu D(j),
    energy flux = -(2/3)rho j + (20/147)grad rho.

The first two come from the exact quadratic equilibrium stress and the
isotropic constitutive map. The energy flux follows because e v-(5/3)v
is microscopic, its quadratic moment is -(2/3)rho j, and the linear heat
flux is +(20/147)grad rho at E=0.

Adding H(0,J1,E1), the projected order-zero conditions are exactly

    rho_t+div J1=0,
    j_t+div[j tensor j-(|j|^2/3)I-2nu D(j)]+grad E1/3=0,
    (5/3)div J1+div[-(2/3)rho j+(20/147)grad rho]=0.

The first follows from div J1=(2/5)j dot grad rho-D Delta rho=-rho_t.
The second is the supplied momentum
equation, including the pressure correction and div j=0. The third is
-(5/3)[rho_t+(2/5)j dot grad rho-D Delta rho]=0. Hence

    BU=0,
    TU+Bw-Gamma(U,U)=0,
    U_t+Tw+Bz-2Gamma(U,w)=0.

The last equality uses both full projected compatibility and BR=Q.
Let G_delta=U+delta w+delta^2 z. Its full nonlinear residual is exactly

    Res_delta = delta R1 + delta^2 R2 + delta^3 R3,
    R1=w_t+Tz-2Gamma(U,z)-Gamma(w,w),
    R2=z_t-2Gamma(w,z),
    R3=-Gamma(z,z).

No asymptotic term has been discarded. Smoothness is an explicit hypothesis
ensuring all these H^s norms are finite. Denote

    K0=sup_{[0,L]}(||U||_s+||w||_s+||z||_s),
    S0=sup_{[0,L]}(||R1||_s+||R2||_s+||R3||_s).

For 0<delta<=1, ||G_delta||_s<=K0 and ||Res_delta||_s<=delta S0.

## 4. Uniform stability and existence

Suppose a real initial family satisfies
||g_delta(0)-G_delta(0)||_s<=I0 delta with I0 independent of delta.
The simple preparation g_delta(0)=U(0) is allowed with
I0=||w(0)||_s+||z(0)||_s. Put

    a0=G_s^2(2K0+1)^2/(2lambda),
    C0=exp(a0 L)(I0+L S0).

Assume 0<delta<=1, delta C0<=1/2, and
delta E(K0+1)<=1/2. Then the nonlinear kinetic initial-value problem
has a unique solution in C([0,L],H_M^s) intersect C^1([0,L],H_M^(s-1)),
and

    sup_{t<=L} ||g_delta(t)-G_delta(t)||_s <= C0 delta,
    sup_{t<=L} ||g_delta(t)-U(t)||_s
       <= delta[C0+sup||w||_s+sup||z||_s].

Moreover f_delta,v=M_v(1+delta g_delta,v)>=M_v/2 throughout the interval.

Proof. The Fourier generator -i diag(v dot k)/delta-B/delta^2 is
dissipative in every H_M^s. Its exponential defines a contractive C0
semigroup. Gamma is locally Lipschitz in H_M^s by the proved product
estimate, so the usual Picard contraction on the integral equation gives
a unique local mild solution and continuation while its H^s norm remains
bounded. This can also be established directly by successive approximation
on a ball, using T<=c delta/[G_s(1+||g(0)||_s)] for the initial interval;
there is no assertion that this local construction alone is uniform in delta.

Set e=g_delta-G_delta and y=||e||_s^2. For a smooth local solution,

    (1/2)y' + (lambda/delta^2)||Qe||_s^2
      <= (G_s/delta)||Qe||_s(2||G_delta||_s+||e||_s)||e||_s
         + ||e||_s ||Res_delta||_s.

Streaming is skew-adjoint. Every collision error is microscopic because
P Gamma=0. While ||e||_s<=1, Young's inequality absorbs half the
microscopic dissipation and leaves

    (1/2)y' + (lambda/(2delta^2))||Qe||_s^2
       <= a0 y + delta S0 sqrt(y).

There is no 1/delta in a0. Applying the scalar inequality to
sqrt(y+eta^2) and then sending eta to zero gives

    ||e(t)||_s <= exp(a0 t)(||e(0)||_s+delta S0 t)
               <= C0 delta <= 1/2.

Continuity prevents exit from the bootstrap ball. The H^s norm stays
bounded by K0+1, so successive local continuations reach L. The energy calculation is justified directly by applying a finite Fourier
projection to the mild error equation. Each retained Fourier mode is C^1
in time; the streaming term cancels in the finite energy identity. The
projections of e and its H^s-continuous forcing converge uniformly on
every compact local time interval, so the integrated energy identity passes
to the limit. No extra spatial derivative is needed for this step.
At a putative finite maximal time, the bounded H^s nonlinearity is Bochner
integrable. The mild formula therefore has an H^s endpoint limit, to which
the same local Picard argument applies. This establishes continuation, not
just a formal bootstrap. Finally T:H^s->H^(s-1) and the equation give
the stated C^1 H^(s-1) regularity. The Fourier embedding and smallness condition give positivity.
Uniqueness follows from the same local Lipschitz integral equation.

Important limit: this theorem compares with an explicitly supplied smooth
solution of the displayed nonlinear system. It does not assert global
existence, unsuppressed acoustic convergence, physical entropy identification,
or a finite-particle/mesh limit. Those are separate obligations.

## 5. Prior art and independent evidence still required

Current-main searches for incompressible/Navier-Stokes/nonlinear fluid found
the lane map but no matching supplied-model nonlinear convergence theorem.
The parent already proves the constitutive coefficients and the 2/5 moment;
these are dependencies, not new claims. Bellouquid's 2002 paper
"The Incompressible Navier-Stokes for the Nonlinear Discrete Velocity Models"
(https://arxiv.org/abs/nlin/0306036) supplies established methodological context.
Its stated preparation and Euclidean-domain convergence theorem are not
imported as a black-box certificate for this quantitative periodic statement.
The complete argument above is to be checked on its own hypotheses.

Before publication: independently check full correctors, Fourier product and
stability constants, mild-solution continuation, conservation/positivity,
and exact nonlinear residual. A primary runner should exercise actual finite
velocity algebra and a nonconstant advected-shear/thermal solution, with
deliberate faulty conservation/pressure/thermal/residual controls. Numerical
checks cannot certify the analytic convergence argument.
