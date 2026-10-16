# What photon and tracer records can supply to the scalar inverse

Root-authored continuation, 2026-10-16. This is conditional research support.
The calculations below are proposals until their accompanying controls and
focused check are complete. No observational array is accessed. The action,
flat background, universal matter metric, geometric optics, linear scalar
perturbations, distance registration and differentiability remain premises.
Lensing inversion is known prior art, not a new reconstruction claim.

## 1. Geometry and records before dynamics

Use the matter metric

    dsJ^2 = a(eta)^2[-(1+2 Psi)deta^2 + (1-2 Phi)dx.dx],
    P=(Psi+Phi)/2, J=(Psi-Phi)/2, d tau=a d eta,
    h=(d a/d tau)/a, Hc=(d a/d eta)/a=a h.

Here tau is matter background proper time, eta is conformal time. Observed
proper clocks include the perturbation: dt_o=a_o(1+Psi_o)d eta_o at linear
order in peculiar velocities. Coordinates, conformal time, distances and the
scale factor are not raw observations. They require a registered background
map, which this note does not derive. Put the observer at the origin and let
n point outward to a source; photons travel in direction -n at zeroth order.

The transverse conformal null geodesic gives d^2 x_perp/d chi^2=-2 grad_perp P.
With observer position and initial direction fixed, its first-order integral
gives beta=theta-grad_Omega psi, fixing our sign convention, where

    psi(u,s,n)=2 int_0^s [(s-r)/(s r)] P(u-r,r n) dr, u=eta_o.

This is the flat-distance Born approximation, evaluated on the unperturbed
past cone. The full-sky shear is gamma=(1/2) eth^2 psi. For ell>=2 its
harmonic coefficient is gamma_lm=(1/2)sqrt[(ell+2)!/(ell-2)!] psi_lm.
The shear operator annihilates ell=0,1. Finite sky coverage introduces further
boundary and response issues. Intrinsic shape statistics, reduced shear,
source selection, point-spread response and distance errors are additional
measurement problems; a continuous calibrated gamma or psi is already an
inferred input. No Poisson conversion from potential to mass is used here.

For a fixed u and direction, differentiating the Volterra integral gives

    P_cone(u,r,n) = (r/2) d_r^2[r psi(u,r,n)]
                  = (1/2) d_r[r^2 d_r psi(u,r,n)].

This is Taylor2001 equations3-4 with the time argument made explicit. The
radial inverse annihilates c0(u,n)+c1(u,n)/r. Forward regularity at the observer
or independently supplied boundary information fixes such terms in an ideal
full radial experiment; on an annulus they cannot simply be set to zero.
Angular null modes and radial integration constants are different issues.
The result recovers the accessible angular components of P on the cone, not
an equal-time three-dimensional map and not J.

## 2. Cone time is a coordinate transformation, not an evolution law

For any scalar F define Fhat(u,r,n)=F(eta=u-r,r n). Then

    partial_eta F = partial_u Fhat,
    partial_r|eta F = (partial_r|u + partial_u) Fhat,
    partial_tau F = a^-1 partial_u Fhat,
    partial_tau^2 F = a^-2(partial_u^2 Fhat-Hc partial_u Fhat).

A source-distance derivative on one cone is instead
partial_r Fhat=partial_r|eta F-partial_eta F. It cannot replace the time
derivative. On an annulus, delta F=(eta+r-u0) f(eta,r,n) vanishes on the cone
u0 but can have a nonzero time derivative there. This is a null space of the
restriction operator for unrestricted metrics. It is not a second solution
of the same scalar action and is not a physical non-identifiability theorem.

Repeated cones with an open observer interval (u0,u1) and registered spatial
coordinates give a thin open spacetime strip. For r in [r0,r1], an entire
radial region shares an emission-time interval only in

    eta in [u0-r0, u1-r1].

Its width is (u1-u0)-(r1-r0); an open shared interval requires a positive
width. This rules out a particular direct construction of a wide coeval
volume from a short observing interval. It does not rule out local inference.

In fact, a local derivative needs an open neighborhood, not a common-time
map of the whole survey. At fixed (u,r) every direction has the same eta and
the same homogeneous background coefficients. This permits a shell version
of the previous inverse, subject to the missing potential/clock/rank inputs.
It removes the need for global spatial Fourier histories; it does not make
the requisite local derivatives measurable without error control.

For angular Laplacian Delta_Omega, define the coeval comoving Laplacian

    Lcone Fhat = Fhat_rr+2 Fhat_ru+Fhat_uu
                +(2/r)(Fhat_r+Fhat_u)+Delta_Omega Fhat/r^2.

This equals Delta_x F. Therefore

    (partial_tau^2-a^-2 Delta_x)F
      = a^-2[-Fhat_rr-2 Fhat_ru-(2/r)Fhat_r
              -(Hc+2/r)Fhat_u-Delta_Omega Fhat/r^2].

The second u derivative cancels in the canonical wave operator. The scalar
response also contains Delta_x P and the trace contains P_tau_tau, so this
cancellation alone does not remove all high-order temporal information.

## 3. Pointwise and angular-shell form of the checked inverse

Use the coefficients and notation of MODE_INVERSE_DERIVATION_v1.md and
MODE_TRACE_ROOT_DERIVATION_v1.md. To avoid confusing the coefficient named
a there with the scale factor, call it cD here. The position-space identities
are

    J_tau_tau - a^-2 Delta J
      = -cD J_tau - c J + d P_tau - e a^-2 Delta P + f P,

    2 P_tau_tau + 8h P_tau +(4h_tau+6h^2)P
      = 6q P_tau + Ct P + G J_tau + Ft J.

The five-column row is (-J_tau,-J,P_tau,-a^-2 Delta P,P), with the scalar
wave operator as its right-hand side. The trace row is (P_tau,P,J_tau,J).
All rows on one registered angular shell at one u share the same eta.
Consequently the previously proved coefficient and full-residual tests can
be applied to angular positions or angular harmonics, without a common-time
global Fourier transform. Rank five or rank four respectively must actually
hold. Background derivatives are then obtained along u at fixed r with the
specified clock conversion, not along the source-distance axis.

For calibrated data, the trace inverse gives q=At/6 and G=Et, then
b^2=q/G and x^2=qG on qG>0, with q and G nonzero. The unchanged background
and full scalar/dust/constraint residuals remain mandatory. Angular shear
null modes can be projected out consistently in a full-sky linear problem:
time and radial differentiation and the spherical Laplacian preserve each
ell,m sector. Finite masks and projection errors require their own treatment.
J is still not measured by lensing; tracer inference below is conditional.

A common multiplicative g(tau) in the two ideal fields has the previously
checked joint-gain treatment. A real instrument drift g(u) is a different
object: at fixed eta, u=eta+r, so it has a radial gradient. For g(u)>0,

    Delta_x[g(u) Fhat] = g Delta_x F
       +2 g_u (Fhat_r+Fhat_u)+(g_uu+2g_u/r) Fhat.

It cannot silently be treated as a homogeneous emission-time gain. Channel,
angle and distance dependent responses are still more general. No claim of
automatic calibration removal for an actual survey follows from the ideal
common-gain theorem.

## 4. Redshift and tracer acceleration do not directly report J

For a photon wave covector k and source/observer four-velocities U, the exact
geometric-optics frequency ratio is 1+z=(-U.k)_s/(-U.k)_o. With n outward,
v=dx/deta, and the scalar metric above, the first-order expression at the
specified emission and reception events is

    1+z = (a_o/a_s)(1+epsilon),
    epsilon = Psi_o-Psi_s+n.(v_s-v_o)
              -int_0^s 2 P_eta(u-r,r n) dr.

One derivation uses the conformal covector p_0: its null geodesic equation
gives d ln(-p_0)/d eta=Psi_eta+Phi_eta, while the local measured energy is
(-p_0)(1-Psi+n.v)/a. This fixes the endpoint, Doppler and integral signs.
It does not identify observed redshift with background distance. Replacing
the source time by an observed-redshift label adds background remapping terms.

For successive wavecrests following the same source worldline, dt_o/dt_s=1+z.
Thus, keeping the endpoint times and their registration explicit,

    d ln(1+z)/dt_o
      = [Hc_o-Hc_s(d eta_s/d eta_o)+d epsilon/d eta_o]
          /[a_o(1+Psi_o)],
    d eta_s/d eta_o
      = a_o(1+Psi_o)/[a_s(1+Psi_s)(1+z)].

The derivative of epsilon includes endpoint potential evolution, source and
observer acceleration, changing ray/endpoint terms and the integrated
potential evolution. This equation is an identity for the fully registered
ray family; it is not an estimator from redshift alone. Omitting these terms
does not turn redshift drift into a direct force measurement.

The linear nonrelativistic matter geodesic gives

    partial_eta v + Hc v = -grad_x Psi.

For an irrotational velocity v=grad_x Vv, choose a background/time convention
for the spatial constant and define Z=a Vv. Then

    partial_tau Z = -Psi, J=-partial_tau Z-P.

In cone variables v=-grad-frame velocity is NOT inferred from redshift alone:
the gradient of Vv must use (partial_r+partial_u) radially, plus angular
derivatives. Independent distance, source/observer motion, angular velocity,
velocity bias and non-gravitational forces must be controlled before this
identity supplies Psi. This removes no raw-data calibration assumption yet.

## 5. A physically constrained rank stress test

Distinct wave numbers do not certify rank. For separable time transfers
P_k=T_P(tau) C_k and J_k=T_J(tau) C_k, the trace row rank is at most one and
the scalar row rank is at most two (the extra vector is k^2 C_k). This is an
algebraic statement, not a claim that arbitrary such transfers solve the
coupled field equations at every k.

A more physical conditional stress test uses exact modes of the previously
checked action A=exp(phi), V=(3/2)exp(-2phi), M=1 with

    aE=t, phi=ln(t), rho=t^-3, r=t^-2, H=1/t,
    aJ=t^2, tau=t^2/2, eta=ln(t), b=1.

For a scalar spatial Laplacian eigenfunction of comoving wave number k,

    P=t^(2m), delta_phi=Y P, U=(Y-4m-2)t P,
    delta=[-2 k^2-12m-5+(2-2m)Y] P,
    Y=(8m^2+12m+3)/(2m+3),
    k^2=4 z(8z+9)/(3-8z), z=m(m+1).

These expressions will be checked against every original mode equation,
not only the eliminated response. For positive growing m<(-1+sqrt(5/2))/2,
k is real. At large k all growing exponents approach the same limit. Taking
many k values can then give exact full rank while making the coefficient
inverse extremely ill conditioned. A numerical stress test must retain this
distinction. These initial modes and this background are deliberately
constructed; they are not derived initial conditions or a fit to our universe.

For four rows (m,1,mY,Y), multiplying each row by (2m+3) converts the columns
to polynomials of degree at most three. Their determinant is a constant times
the Vandermonde product divided by the four denominators. Since differences
between high-k growing m values scale as k^-2, the unnormalized determinant
scales as k^-12 for fixed distinct k ratios. The constant, spectrum and
conditioning will be checked before being used.

## 6. Scope and sources

The constructive direction is local angular-shell compatibility on repeated
cones, not supplying a growth function to build a coeval survey volume.
Distance/clock registration, full-metric photon propagation, a separate Psi
channel, sufficient angular response rank, derivative errors, action selection
and initial-state origin remain open. Weak/integrated residuals may reduce
direct differentiation but require a specified test-function window and
background coefficient treatment; no completed weak estimator is claimed.

Primary comparator: Taylor, arXiv:astro-ph/0111605v1, equations3-4; its known
inverse and boundary discussion are used without its Poisson mass conversion.
Oestreicher et al., arXiv:2505.04731v2, section3.1 was read completely for its
observable drift derivation. That derivation expressly omits metric-potential
corrections and assumes an FLRW photon wavevector; it is a comparator for
source/observer and observed-redshift terms, not a substitute for the full
metric expression above. No empirical values or simulation outputs are used.
