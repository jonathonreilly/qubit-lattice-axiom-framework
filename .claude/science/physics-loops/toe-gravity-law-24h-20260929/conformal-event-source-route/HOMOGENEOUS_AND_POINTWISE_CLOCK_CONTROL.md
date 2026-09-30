# Actual clock control and the residual endpoint gap

This supplements the checked endpoint derivation without changing it. It is
an elementary control using the literal scalar clock already supplied in
PR9398 at bd6f6e6368d615bfc0437760e2396cd471837cd7, equation(48), not a new
physical-source construction or separate milestone.

Write lambda for the INITIAL homogeneous trace parameter and
rho0=3a lambda^2/2, w0=sqrt(2rho0). For the supplied positive scalar clock,
zero shift and phi=t, the exact homogeneous solution is

    g(t)=exp(-a lambda t/w0) I,
    pi(t)=lambda exp(a lambda t/w0) I,
    w(t)=w0.

Define r(t)=exp(3a lambda t/(2w0)). Then the same solution expressed in
the conformal endpoint notation has

    psi(t)^6=1/r(t), rho(t)=rho0 r(t),
    lambda_c(t)=lambda r(t), c(t)=rho0 r(t)^2.

For a spatially constant increment f_const>0, choosing

    t_f=2w0 log(1+f_const/rho0)/(3a lambda)

gives precisely the charge-matched constant-source upper-equality case in
the endpoint theorem. It is a forward clock time for lambda>0 and a backward
time for lambda<0. The metric stays positive at every finite such time.
The homogeneous formulas directly satisfy the actual ODEs and constraints;
applying a separate uniform analytic approximation estimate would still
require its stated interval/norm conditions. No trajectory from the
nonconstant endpoint construction follows from this one homogeneous control.

This also clarifies the meaning of the prescribed coordinate-density
increment: here it increases through geometry during a closed solution.
It is NOT record production or external work, and no original rotor process
has been identified with it.

For a nonconstant f the supplied zero-shift clock has a stronger obstruction
than the integrated-charge test alone. Its actual scalar equation gives
wdot=0 pointwise when phi=t; thus initial constant w0 remains constant. Any
CMC conformal endpoint with this same w0 must obey

    rho=rho0 psi^(-6),
    -8K Delta psi+c psi^5-rho0 psi^(-7)=0.               (1)

For c>0 the nonlinearity c z^5-rho0 z^(-7) is strictly increasing on z>0.
Its constant positive zero is z_*=(rho0/c)^(1/12). Subtract this constant
solution from any positive periodic solution, multiply by the difference
and integrate. Both gradient and monotone terms are nonnegative; hence
psi=z_* everywhere. Its rho is therefore constant as well.

Consequently the nonconstant conformal endpoints that match Q in the main
calculation still cannot be reached from the homogeneous state in THIS
zero-shift scalar-clock evolution. The pointwise w restriction has not been
paid by choosing the one global trace parameter. A shift can advect a
coordinate density, and changed source/clock laws, inhomogeneous initial
data, nonconformal endpoints or explicit charge transfer are separate
questions. This argument does not turn a gauge-specific endpoint condition
into a no-go for all canonical gravity or for local physical events.
