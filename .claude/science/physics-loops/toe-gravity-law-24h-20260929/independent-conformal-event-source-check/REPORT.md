# Independent check of conformal endpoints and scalar momentum

No material mathematical error was found in the complete frozen derivation
9c672bd09bab84c1f7ab9fe2e7b1b47c2143cfddc2c5f4c88310e9f4565b96c2,
including its declared constant-trace-parameter extension. No correction is
requested. The conclusions concern supplied continuum endpoint data and a
necessary conserved-charge test. They are not a record-source identification,
an evolution construction, formal review, audit or retained-status judgment.

## Independence and source scope

PRE ac02215438fd14c669018332c4e680162a843fb673994bd756586e10ab3b64b4
was frozen at 20:51:22UTC, before the author's 20:52:49 proof freeze and before
opening that proof. The complete contract and root brief disclosed the
conformal/monotone approach. My PRE independently reconstructed the density
factors, positive-resolvent iteration, uniqueness, strict global response,
integrated energy, scalar charge conservation and the charge upper bound.
Section5's variable constant c extension was not in that precomparison;
it was independently worked through after full proof exposure. No stronger
blindness claim is made for it. I authored the earlier spectral precursor
and checked the prior flat-slice identity; this shared history is disclosed.

The literal continuum definitions in provisional PR9398 at
bd6f6e6368d615bfc0437760e2396cd471837cd7 are supplied model inputs. The
canonical note has SHA676b2e267b47c46563ab06667678d649829222373f7df52e6fb0ebdd9903d531;
the requested local worktree bytes match it. I read its canonical law,
conformal and flat compatible-data definitions, scalar/clock conventions and
momentum sign. Its analytic-time theorem is neither needed nor imported.
The matched main prior's exact closed static positive-source argument and
conformal density identity were read at their declared scope, as prior
context rather than a load-bearing existence theorem.

Current science fb5da8dd and selected method7146, with actual axiom,
primitive and registry identities, were reverified. Complete unchanged
procedural/primitive reads from the preceding checks are explicitly reused
in SOURCE_READ_AND_BINDINGS. The supplied continuous metric/scalar carrier,
Hamiltonian, source density, positive branch and clock are not derived from
those primitives. All new contracts/proof/freeze records were read. No
scientific code or numerical experiment was needed or run.

## Literal constraints

For g=psi^4 I and density momentum pi=lambda psi^2 I,
sqrt(g)=psi^6 and g pi=lambda psi^6 I. Therefore the kinetic density is
-c psi^6, c=3a lambda^2/2. Direct conformal curvature gives
R=-8psi^(-5)Delta psi, so the curvature density is +8K psi Delta psi.
The two momentum-constraint contributions cancel as
12lambda psi^5 partial_i psi-12lambda psi^5 partial_i psi.
These computations retain the momentum's density character.

The scalar endpoint equation is consequently

    rho=c psi^6-8K psi Delta psi,
    -8K Delta psi+c psi^5-rho/psi=0.                     (C1)

The source is coordinate energy density. Prescribing density per physical
volume would change this equation. There is no finite-difference product
rule, fixed-band or discrete first-class statement in this reduction.

## Positive solution, uniqueness and support

For c>0 and smooth strictly positive rho, the constants
l=(rho_min/c)^(1/6) and u=(rho_max/c)^(1/6) are barriers.
With F(x,z)=c z^5-rho/z, its derivative
5c z^4+rho/z^2 is positive on all z>0. On [l,u] choose beta above
its maximum. The resolvent of -8KDelta+beta is the positive periodic
heat-semigroup integral. Iteration of beta psi-F(x,psi), beginning at l,
is increasing and stays below u. The right sides are uniformly bounded
and converge in every finite L^p by dominated convergence. The fixed
elliptic inverse gives W^(2,p) convergence, and smoothness follows by
bootstrapping the smooth nonlinearity on the compact positive interval.
No logarithmic boundary, zero lower barrier, small-source restriction or
uncontrolled weak critical-power limit is involved.

Any positive solution lies between the barriers by its minimum and maximum.
Subtracting two solutions and testing against their difference leaves
8K times the squared gradient norm plus the integral of the strictly
monotone F difference. Both are nonnegative; uniqueness follows. The
author's named positive-kernel and elliptic-regularity tools have exactly
their required compact-torus, beta>0 and smooth positive-domain hypotheses.

At fixed c=rho0 and rho=rho0+f, f>=0, the solution has
1<=psi<=(1+||f||_infinity/rho0)^(1/6). The author's difference coefficient

    b=rho0(1+psi+psi^2+psi^3+psi^4)+(rho0+f)/psi

indeed satisfies -8KDelta(psi-1)+b(psi-1)=f. For nonzero f, the
positive resolvent applied to f+(beta-b)(psi-1) gives psi>1 everywhere.
My PRE used the equivalent divided source f/psi and the coefficient
rho0(psi^5-psi^(-1))/(psi-1). Both yield the same strict result.
This is an elliptic support statement, not a signal-speed claim.

Integrating the undivided equation gives exactly

    E=<f>=rho0(<psi^6>-1)+8K<|grad psi|^2>.              (C2)

The gradient term has the displayed positive sign. Nonconstant f forces
nonconstant psi; constant f gives psi=(1+f/rho0)^(1/6). At f=0 the
unique fixed-c solution is one. At lambda=0 and nonzero f>=0,
integrating Delta psi=-f/(8Kpsi) is impossible. If both vanish, every
positive constant psi solves the endpoint constraint, and its scalar
realization has w=0. A positive scalar-clock branch is absent in that
last case. No uniqueness or uniform nonzero-lambda bounds survive there
without further conditions.

The small-source linearization is also correct:
(-8KDelta+6rho0)v=f, including the zero mode. The positive elliptic
linearization has an inverse and supports local smooth parameter
dependence. This verifies the derivative control without supplying a
physical screening law or using the separate analytic evolution theorem.

## Actual scalar realization and charge bounds

For constant phi and the massless supplied scalar, j=w grad phi=0 and
rho=w^2/(2psi^6). Hence the positive endpoint density is

    w=psi^3 sqrt(2rho),  Q=<w>,  Q0=sqrt(2rho0).

For nonzero f>=0 at fixed c=rho0, psi>1 makes w>Q0 at every point.
For M=||f||_infinity, the bound

    sqrt(2)E/[sqrt(rho0+M)+sqrt(rho0)] < Q-Q0

follows by first dropping the strictly larger factor psi^3 and then
rationalizing sqrt(rho0+f)-sqrt(rho0). The strict sign is valid even
when f vanishes on an open region. Cauchy-Schwarz and(C2) give
Q^2<=2<psi^6><rho><=2(rho0+E)^2/rho0, proving the stated upper
bound sqrt(2/rho0)E. It is attained for constant f; nonconstant f has
a positive gradient cost and makes it strict. The first variation
Q-Q0=t sqrt(2/rho0)<f>+O(t^2) follows by integrating the linearized
equation. All factors of two agree with the actual scalar density.

Varying the original massless gradient energy and positive spatial Lie
generator gives

    wdot=aK partial_i(N sqrt(g)g^ij partial_j phi)
         +partial_i(X^i w).

Thus the coordinate integral of w, which is already a density, is
conserved on the torus. One must not insert another volume factor in Q.
Allowing intermediate gradients does not remove this conservation law.
The strictly larger fixed-c endpoint Q therefore cannot be reached from
the initial homogeneous scalar data by a smooth closed evolution of this
action. This only tests that endpoint specification and positive branch.
An external charge supply or changed scalar law is a different problem.

## Post-exposure check of the global trace extension

Now hold the same positive rho fixed and vary c>0. The same existence
proof supplies psi_c. A separate derivative check gives

    [-8KDelta+5c psi_c^4+rho/psi_c^2] partial_c psi_c
       =-psi_c^5.

The positive elliptic inverse makes partial_c psi_c strictly negative.
Consequently Q'(c)=3<sqrt(2rho)psi_c^2 partial_c psi_c><0.
Smooth dependence on compact c intervals is justified by that coercive
linearized operator; equivalently compactness plus uniqueness proves
continuity. The author's barrier estimates bound Q(c) above and below
by positive constants times c^(-1/2). It therefore ranges continuously
from infinity to zero and has a unique solution c_* to Q(c_*)=Q0.

For nonzero f>=0, the already proved Q(rho0)>Q0 gives c_*>rho0.
Let R=<rho>=rho0+E and X=<psi_(c_*)^6>. At the matched charge,
Cauchy gives X>=rho0/R, while the integrated constraint gives c_*X<=R.
Therefore

    rho0<c_*<=R^2/rho0,
    |lambda|<|lambda_*|<=|lambda|R/rho0.

Constant f attains the upper endpoints. For nonconstant f the gradient
term is strictly positive, making the upper bounds strict. The sign of
lambda_* remains an explicit branch choice, independent of c_*. For f=0,
the unique charge match is c_*=rho0 and psi=1. The extension assumes
rho0>0; it does not supply a positive-charge match to the lambda=0 vacuum.

At a nonzero source charge match, psi must be below one somewhere;
otherwise w>=sqrt(2rho) would force Q>Q0. If f vanishes on an open
exterior region, psi cannot be identically one on that region, since(C1)
would force c_*=rho0. This is the precise open-region interpretation of
the author's locality statement; isolated level-one points are not
excluded. Changing the single global trace parameter is itself nonlocal.
All constraints and integrated charge are matched, but no trajectory,
pointwise jump conservation law or local event action is thereby proved.

The report preserves all these limits. Smooth bump data are not silently
fed into an analytic-data theorem; even analytic data would need that
theorem's separate radius/smallness bounds. Signed density increments,
variable mean curvature, nonconformal tensors, source momentum and charge
transfer remain outside this endpoint class. No original rotor or native
record energy has been identified with rho. Only the assigned independent
directory was written; no author source, PR or authority state was changed.
