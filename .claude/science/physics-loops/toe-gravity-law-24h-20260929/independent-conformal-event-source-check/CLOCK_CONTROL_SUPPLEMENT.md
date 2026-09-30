# Focused supplement: actual homogeneous and pointwise clock controls

No material mathematical error was found in
HOMOGENEOUS_AND_POINTWISE_CLOCK_CONTROL.md
5e018bfbcf45ff6ac39eb697c85f35b1d8011974db59eb20be49171d7e0c1e59.
The entire control and freeze were read, then the actual PR9398 source
equations36–48 were reread completely, including their metric-dependent
lapse variation and scope. The earlier endpoint derivation9c672bd0 and my
receiptbea5cecb remain unchanged. This is a focused follow-up, not a new
general review, formal verdict, audit or scientific novelty claim. There
is no blindness claim: the control existed before this assignment and was
read before the reconstruction below. No numerical computation was needed.

## Direct Hamiltonian and time orientation check

In the homogeneous isotropic subspace write g=q I and pi=p I. The actual
canonical one-form is 3p dq, so the restricted bracket is {q,p}=1/3.
For constant positive supplied w0 the literal clock Hamiltonian(36) is

    H_clock=-(3a/(2w0))q^2 p^2+w0/2.

This retains the metric dependence of N=q^(3/2)/w0; varying an external
fixed lapse instead would not be the stated off-constraint Hamiltonian.
All spatial derivatives of the homogeneous fields vanish; the curvature
contribution to Hamiltonian variation vanishes at its constant lapse.
Isotropy is preserved by the full canonical variation. Thus

    qdot=-a q^2 p/w0,  pdot=a q p^2/w0,  (qp)dot=0.

With q(0)=1,p(0)=lambda, one obtains exactly
q=exp(-a lambda t/w0) and p=lambda exp(a lambda t/w0).
The scalar equation gives phidot=Nw0/sqrt(g)=1 and wdot=0.
The lapse is positive; the constraints hold since q^2 p^2=lambda^2 and
w0^2=3a lambda^2. This independently checks the actual source's equation48,
rather than only reparameterizing a presumed solution.

Since psi=q^(1/4), the endpoint parameters are

    r=exp(3a lambda t/(2w0)),
    psi^6=1/r,  rho=w0^2/(2psi^6)=rho0 r,
    lambda_c=p/psi^2=lambda r,  c=rho0 r^2.

For constant f>0, r=1+f/rho0 and the displayed time
2w0 log(1+f/rho0)/(3a lambda) is correct. It is positive for lambda>0
and negative for lambda<0. It reproduces exactly the endpoint theorem's
upper-equality case c=(rho0+f)^2/rho0 at unchanged scalar charge w0.
The metric is positive and all these homogeneous quantities are finite at
each finite t. This explicit homogeneous solution does not extend the
separate analytic approximation theorem beyond its quantitative time and
norm domain.

The increasing rho here is a coordinate energy density w0^2/(2sqrt(g)).
It grows on the contracting forward branch through the changing geometry,
while the scalar density momentum w0 stays fixed. It is not an original
formation event, apparatus work or added energy supply. No identification
of a rotor expectation with this rho is made by either calculation.

## Pointwise conservation and the nonconstant endpoint restriction

The actual full massless scalar equation is

    wdot=aK div(N sqrt(g)g^(-1)grad phi)+div(Xw).

In the stipulated phi=t, zero-shift clock, both terms vanish pointwise.
Thus initially constant w0 remains that same function, which is stronger
than conservation of its integral. Resetting the supplied clock density
to a different endpoint function would change the specified law.

A CMC conformal endpoint with this w0 therefore has
rho=rho0 psi^(-6). Substitution into the exact density constraint yields

    -8KDelta psi+c psi^5-rho0 psi^(-7)=0.

For c>0 the derivative of the last two terms is
5c psi^4+7rho0 psi^(-8)>0. The positive constant
z_*=(rho0/c)^(1/12) solves the equation. Subtracting its equation and
integrating against psi-z_* gives the sum of 8K||grad psi||^2 and a
strictly positive monotonicity integrand unless psi=z_*. Hence every
positive smooth periodic solution in this endpoint class is constant,
and so is rho. The inverse-seventh power, root exponent and signs are
all fixed by the coordinate-density convention.

Consequently choosing the one global c to match only integrated scalar
charge does not make a nonconstant CMC conformal endpoint accessible in
this zero-shift scalar clock. The argument does not assume that the
intermediate geometry remains conformal: pointwise conservation and the
final endpoint equation suffice. It also supplies no such exclusion for
different shift/source/clock prescriptions or different endpoint classes.
A nonzero shift changes w through div(Xw), rather than violating its
integrated conservation law. Those alternatives require their own dynamics;
the control does not claim that any one of them realizes an event.

All conclusions retain the original nonzero-lambda positive-clock domain.
They do not prove a physical record clock, a local event action, actual
work, or a no-go for canonical gravity. No correction to the author's
narrow statement is requested. Only this supplement and its separate
identity record were added; the previous report and freeze were not edited.
