# Independent derivation and frozen checks

Only the source note, supplied input JSON and plan have been read. No author
calibration runner or output has been opened. This reasoning and the numerical
fixtures below are frozen before implementing the independent computation.

For point centers x_j(alpha) and y_i(phi)=delta+R e_i(phi), set d_ij=y_i-x_j.
Then F_ij=G m M d_ij/|d_ij|^3. Differentiating the pair energy
U=-G m M/|d_ij| under an inner rotation gives
U_alpha=-G m M (x_j cross y_i)_z/|d_ij|^3. Thus N_inner=-U_alpha.
For centered axes, U depends on phi-alpha, so N_inner=+U_phi.
For offset axes, N_inner-U_phi=(delta cross sum F_inner)_z; equality of the
two opposite-center torques cannot be assumed. A complex-step energy derivative
will be compared with a separate Cartesian force/cross-product implementation.

Centered pair classes give nine pairs as three copies of three angular
differences. For any odd real torque N, b_n=(1/pi) integral N sin(n phi),
while c_n=(1/(2pi)) integral N exp(-in phi); hence c_n=-i b_n/2.
The same factor follows for any real signal by pairing positive and negative
orders. The third-harmonic leading coefficient follows from
P3(cos phi)=(3 cos(phi)+5 cos(3phi))/8: summing the nine phases cancels the
first term, and inner torque is +U_phi, yielding +135 G m M r^3/(8 R^4).
The next relative correction is order (r/R)^2; the exact integration will be
used at the supplied geometry.

Let B=A3/G. The quantity Ncal_published/B is a consistency reconstruction of
the G used in a computed nominal calibration. It is not an independent G
measurement. Both 6.6742e+11 and the explicitly labeled 6.6742e-11 candidate
will be retained. Their predictions differ by exactly 1e22. Supplied masses,
radii, offsets, uncertainties and the two different printed radial corrections
will not be retuned. At the centered geometry, linear sensitivity coefficients
will be obtained by analytically differentiating the exact integrand. Since
A3 is linear in each mass, its corresponding derivative is exactly A3/m or
A3/M. Covariance is not supplied, so any root-sum-square diagnostic is conditional.
Offset direction will be stipulated along x; this is a model choice, not an
inferred actual orientation. Published gamma will be compared by arithmetic
using Nmeas/(Ncal+deltaN), with uncertainty propagation labeled conditional.

The Fourier transform of (Delta-mu^2)g=-4pi delta gives
4pi/(p^2+mu^2). Integrating the axial momentum produces exp(-q|z|)/(2q);
the transverse angular integral cancels the remaining Fourier constants and
gives integral k dk J0(k transverse_distance) exp(-q|z|)/q.
The Bessel addition theorem gives the stated sum over all integer angular
orders. Equivalently, the derivative jump is -2 for exp(-q|z|)/q, and angular
and radial completeness produce -4pi delta3. On the axis, q substitution gives
integral_mu^infinity exp(-q d)dq=exp(-mu d)/d. Energy for ordinary densities is
-G integral rho_A rho_B g with each cross pair counted once; adding 1/(4pi)
would change the point-force law.

For a centered N-wedge pattern, the angular Fourier integral is zero unless
n is divisible by N. At nonzero n=N*l it is 2N sin(n beta)/n, and at n=0 it
is the nonzero area angle 2N beta. The source's formula explicitly concerns
positive l and should not be extended to n=0. Multiplying the two coefficients
and adding +/-n gives 8 sin(n beta_A) sin(n beta_B)/l^2. The two z integrals
are exp(-q d)(1-exp(-q t_A))(1-exp(-q t_B))/q^2. Combined with k/q from the
kernel this yields the displayed negative cosine-energy coefficient and its
q^-3 integrand. Torque amplitude is n|U_n|. The integrand's length dimension
is 5: k dk/q^3 has dimension length, each radial integral has length^2.
Signed contrast sources do not turn signed net mass into a total-variation bound.

Numerical controls to implement, with no author-output access until frozen:

1. Direct Cartesian nine-pair torque and independent complex-step energy
   derivatives, centered and offset, at phases 0.17, 0.51 and 1.06. Relative
   comparisons use 2e-10 and a geometry-scaled absolute floor 1e-14 at G=1.
2. Adaptive angular quadrature of the centered third sine coefficient versus
   FFTs with 48, 96 and 192 equally spaced full-period samples, tolerance 2e-10.
   Small-radius checks q=1/20,1/40,1/80 verify approach to 135/8 and quadratic
   relative remainder. Missing real-amplitude factor is a countercontrol.
3. Exact-input geometry predictions, G consistency, radial/vertical/combined
   corrections, analytic mass/radius sensitivities and conditional gamma
   arithmetic. All published differences are outputs, not pass/fail targets.
4. Point-kernel axial identity and angular versus Bessel harmonic coefficients
   for r=.34, r'=.61, d=.47, mu=0,.8,2 and n=0,1,3. Adaptive integration
   tolerances are abs 1e-13/relative 2e-10; comparisons allow relative 2e-8.
5. Complete direct six-dimensional wedge-volume energy at 32 phases over its
   period, compared with the Fourier/Bessel coefficient. Synthetic fixture:
   N=3, n=3, beta_A=.17, beta_B=.21, radial A=[.2,.6], B=[.25,.55],
   t_A=.12, t_B=.16, d=.4, rho_A=1.3, rho_B=.8, mu=.7, G=1.
   Tensor Gauss orders 4,6,8 in each of r,theta,z; repeat order 6 at 48 phases.
   Independent Bessel radial quadrature uses orders 24 and 40 with outer
   abs tolerance 1e-14/relative 2e-10. Finest volume agreement tolerance is
   2e-6 relative, with decreasing volume-order differences. A spurious 1/(4pi)
   or a single complex-order coefficient must miss the direct energy result.

These floating checks are not interval certificates. Every owned execution
will be bytecode-disabled and externally bounded at 120 seconds, preserving
actual stdout/stderr and failure or timeout records. Numerical failure will
be preserved before any repair. No physical exclusion, scalar charge,
environmental vacuum, actual alignment or independent observation is inferred.
