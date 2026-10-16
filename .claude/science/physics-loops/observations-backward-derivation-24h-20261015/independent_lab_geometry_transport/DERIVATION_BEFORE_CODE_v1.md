# Independent derivation and frozen controls

The source note alone has been read. No author geometry-transport runner or
result has been opened. This derivation and the following small test selection
are frozen before implementing and running the independent checks.

Use v=y-x and g(r)=exp(-m r)/r. Then g'=-r h and
K=(Jx).v h=-(Jx).gradient_y g. The radial Hessian of g has eigenvalues

    lambda_radial = exp(-m r)[(m r)^2+2m r+2]/r^3,
    lambda_tangent = -(1+m r)exp(-m r)/r^3.

For m>=0 its operator norm is lambda_radial. Therefore

    gradient_y K = -Hessian(g) Jx,
    gradient_x K = J gradient(g) + Hessian(g) Jx,

and their norms are at most L lambda_radial and r h+L lambda_radial.
These are no larger than the stated constants, because
lambda_radial <= h+r|h'|=exp(-m r)(m r+2)^2/r^3.
This supplies an alternative Hessian proof of the two conservative constants;
no optimality is claimed or needed. Direct differentiation also gives

    (r h)' = -exp(-m r)[(m r)^2+2m r+2]/r^3,
    (h+r|h'|)' = -exp(-m r)[(m r)^3+5(m r)^2+12m r+12]/r^4.

Both are negative for r>0,m>=0, including m=0. They may thus be bounded
at r=d. Integrating the differential along simultaneous straight paths gives
Cx|delta x|+Cy|delta y| if every path pair remains in r>=d,|Jx|<=L.
The lower gap d0-epsilon_A-epsilon_B and convexity of the transverse lever
norm provide sufficient certificates. Merely positive endpoint gaps do not:
x=(0,0,0), y=(1,0,0), y'=(-1,0,0) has endpoint gap 1 but midpoint gap 0.
It also has finite unconstrained W1=2 for one moving atom, while its sole
straight transport path is inadmissible. This is a domain countercontrol,
not a claimed failure of every possible endpoint inequality.

Let Pi_A and Pi_B have total masses M_A and M_B. Integrating the pointwise
bound over their product gives M_B Cx D_A+M_A Cy D_B, since the unaffected
factor contributes its full mass. D_A and D_B are mass-weighted displacement
moments, not mean displacements. Replacing them by an infimum needs one common
admissible class with uniform constants; a sequence of forbidden optimizers
does not provide the needed proof. Unequal masses and signed measures are not
covered by that positive equal-mass transport statement.

For c_n=(1/(2pi)) integral Y(phi)exp(-in phi), a uniform pointwise bound B
gives |delta c_n|<=B. The sine/cosine coefficients and real harmonic amplitude
are -2Im(c_n),2Re(c_n),2|c_n|. Their differences are therefore bounded by 2B.
This is conservative: no sharp Fourier norm is claimed. As a generic Fourier
countercontrol, sign(cos phi) has complex c_1=2/pi and real cosine coefficient
4/pi; transferring the complex envelope B=1 directly to a real coefficient
would fail. This test waveform is not presented as a realizable apparatus.

Frozen controls:

1. Symbolically verify the radial Hessian eigenvalues, both derivative
   polynomials, and the nonnegative difference between the printed radial
   factor and the Hessian norm. Compare complex-step gradients of the original
   torque kernel with the independent Hessian expressions for m=0,.9,4 at
   two nonsingular coordinate pairs. Relative tolerance 2e-10, absolute 1e-12.
2. A split mass-preserving discrete coupling, with masses M_A=2.4,M_B=1.7:
   A starting points [(.3,.1,0),(.3,.1,0),(-.2,.25,-.1)], weights [.4,.5,1.5],
   displacements [(.04,-.01,.02),(-.02,.03,.01),(.01,.02,-.015)];
   B starts [(.25,.15,1.5),(.25,.15,1.5),(-.35,.2,1.6)], weights [.6,.4,.7],
   displacements [(-.03,.02,-.025),(.015,-.035,.01),(.02,.01,-.02)].
   Use d0=1.5 and epsilon_i=max displacement, L=.6. Rotate B and B' together
   around z at 64 angles. The vertical original gap, triangle inequality and
   endpoint lever establish the path certificate uniformly in angle. Check
   point changes, product integration and n=1,2,3 complex/real coefficients
   for m=0,.9,4. Also independently factor the product integral into its masses
   and first moments. No unverified Wasserstein optimizer is inserted.
3. Retain the endpoint-gap/inadmissible-path example above. A zero-net-mass
   contrast at A=(.5,0,0),(-.5,0,0) with signs +1,-1 and B=(0,1,1) has
   massless torque 8/27 rather than zero; this checks the net-mass shortcut.
4. Evaluate only the source's explicitly stipulated scale illustration with
   exact rational SI conversions: masses .65749 g and 1.19856 g, L=.027 m,
   d0=50 micrometers, both epsilons=1 micrometer, reference G=6.6742e-11 and
   unit scalar strength, for m=0 and 20000/meter. Preserve both complex and
   real envelopes, with no comparison to a chosen measured harmonic and no
   claim that these displacements were measured.

Owned executions will use -B, PYTHONDONTWRITEBYTECODE=1, and an external
120-second timeout. Preserve actual output/failures before any repair. The
independent outputs will be frozen before reading or replaying author code.
