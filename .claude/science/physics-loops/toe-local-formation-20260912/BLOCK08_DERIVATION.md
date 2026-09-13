# The flat hyperdiagonal mode fails a nonlinear compatibility condition

Author conditional derivation, 2026-09-13; same-author checks complete, independent review pending.
This concerns the supplied Euclidean length Regge action on the unit 4D
path complex. It is not an axiom obstruction or a physical energy claim.

## 1. Exact one-cube family

Keep axis, face and body squared lengths flat and vary only the main
hyperdiagonal squared length by lambda_x in cube x. In each of its 24 path
simplices the metric is I+(lambda_x/2)(e_first e_last^T+e_last e_first^T).
It is positive definite for |lambda_x|<2, so the following family consists
of ordinary nondegenerate Euclidean simplices with matching shared faces.

A triangle containing that hyperdiagonal is (0,u,1111). With m=|u|, its area is

A_m(lambda)=sqrt(m(4-m)/4-lambda^2/16).

There are eight such triangles with m=1 or3, each incident to six simplices,
and six with m=2, each incident to four simplices. A full hyperdiagonal
triangle belongs to only its own cube. The inverse of the displayed metric,
contracted with the simplex barycentric normals, gives their angles

theta_1=acos(sqrt((4-lambda^2)/(2(8-lambda^2)))),
theta_2=acos(-2lambda/(8-lambda^2)).                            (1.1)

For m1 or3 the two missing internal normals have dot product -1 and squared
norms 2 and 1+(1-lambda^2/4)^(-1). For m2 their dot product is
(lambda/2)/(1-lambda^2/4) and their squared norms are both
1+(1-lambda^2/4)^(-1). The interior angle uses minus the normalized dot
product, fixing the sign in (1.1).

Let d1=2pi-6theta1 and d2=2pi-4theta2. Schlaefli yields the exact derivative
of the action per cube along this family,

f'(lambda)=-(lambda/16)[8 d1/A1+6 d2/A2], f(0)=0.              (1.2)

Indeed only these fourteen triangle areas vary, A'_m=-lambda/(16A_m).
All area-times-angle-derivative terms cancel in the action derivative.
Equation (1.2) also proves additivity for independent lambda_x: each derivative
involves only its own cube's full-diagonal triangle star. Thus
S({lambda_x})-S(0)=sum_x f(lambda_x) on a finite periodic complex.

## 2. Cubic term and second-order equation

Expansion of (1.1) at zero gives

d1=-sqrt(3)lambda^2/8+O(lambda^4),
d2=-lambda-13lambda^3/96+O(lambda^5).

Since A1=sqrt(3)/2+O(lambda^2), A2=1-lambda^2/32+O(lambda^4),

f'(lambda)=3lambda^2/8+lambda^3/8+O(lambda^4),
f(lambda)=lambda^3/8+lambda^4/32+O(lambda^5).                 (2.1)

The flat hyperdiagonal Hessian row vanishes for EVERY first-order edge
variation. To see this directly, write its full equation as
E_hyper=sum_(t contains hyper)(partial A_t/partial q_hyper)delta_t.
Both the deficit and that area derivative vanish at the right flat background:
partial A/partial q_hyper=(q_leg1+q_leg2-q_hyper)/(16A)=0.
Differentiating E_hyper once therefore gives zero in all directions.

Suppose q(epsilon) is differentiable at zero and consists of exact stationary configurations, with
q(0) flat, whose first derivative is a nonzero pure hyperdiagonal field v_x.
At a cube with v_x!=0, the coefficient of epsilon^2 in E_hyper is
3v_x^2/8 from (2.1). Since q(epsilon)-q(0)=epsilon v+o(epsilon), analyticity of the equation
and its identically zero first derivative give this coefficient plus
o(epsilon^2). Thus even a nonanalytic higher-order correction cannot cancel it
while preserving the specified first derivative. Thus no such curve
exists. This is a bounded linearization-instability statement: a nonzero
linearized solution in this specified extra-null subspace is not tangent to
an actual differentiable family of nonlinear vacuum solutions.

## 3. Adding a constant flat metric tangent does not cure it

A stronger version follows without solving the nonlinear equations. Let G=I+H
be a nearby constant positive metric, set all ordinary edges to their exact
flat G-lengths, and let mu_x be the excess squared hyperdiagonal over its
flat G-value. The exact action again separates into a sum of one-cube
functions f_G(mu_x), with f_G(0)=f'_G(0)=0 because G is globally flat.
The part cubic in (H,mu) is

S_3(H,{mu_x})=sum_x [mu_x^3/8
                    +(mu_x^2/4)sum_(a<b) H_ab].             (3.1)

To derive its mixed coefficient, differentiate the hyperdiagonal Hessian
at G=I. Only the m2 deficits have a first mu derivative, equal to -1. For
such a split u+v=1111, the linear change of the area derivative is
-(2u^T H v)/(16A_2), where A_2=1. Across the six size-two subsets, each
off-diagonal entry H_ab crosses four splits, so sum_u 2u^T H v=8sum_(a<b)H_ab.
Consequently delta_H f''_G(0)=sum_(a<b)H_ab/2. Its Taylor coefficient is
one half of this, giving (3.1). No mu H^2 term occurs since f'_G(0)=0 for
all constant G.

Project the second-order stationarity equation onto any uniform off-diagonal
flat-metric variation while holding mu fixed in these local coordinates.
The cubic term contributes sum_x v_x^2/4. The first derivative of this projected equation vanishes in every direction,
because the Hessian annihilates the uniform flat-metric direction. Therefore
arbitrary o(epsilon) corrections to the tangent cannot change the leading
epsilon^2 projection. For real v this is positive unless v vanishes identically.
Thus even after adding an arbitrary constant flat-metric first derivative,
a real nonzero hyperdiagonal excess cannot be the tangent of a differentiable family
of nonlinear stationary configurations. This does not cover arbitrary
nonconstant first-order metric, curvature or displacement fields.

## 4. Exact scope and live alternatives

The extra quadratic null direction is therefore not an independently free
nonlinear vacuum mode near this particular flat complex. This conclusion
does not apply to the four physical vertex-displacement directions at
nonzero momentum, nor does it prove that the two tensor classes fail to
continue. Mixed curved tangents need their own compatibility calculation.
The Euclidean action's cubic sign is not a Lorentzian Hamiltonian stability test.

Five genuinely different alternatives remain: change the tangent by including
nonconstant metric fields; solve the nonlinear compatibility equations as
constraints on the allowed initial data; expand around a nonorthogonal flat
triangulation; change the action by a specified curvature term; or use a
different geometric variable/triangulation and compare its physical observables.
None is excluded by this calculation, and none requires an axiom edit merely
because this direction failed. Source or boundary forces also change the
stationarity equation and lie outside the vacuum claim.

The immediate consequence for the campaign is to preserve the exact linear
Regge/source theorem while refusing to infer unrestricted nonlinear degrees
of freedom from its nullity. The new physical matter/source interface and its nonlinear constraints remain
a real next obligation. A formal scope stress test and cold proof pass remain
before any milestone handoff.

## 5. Same-author evidence

check_block08.py passed 31 checks in 2.55 seconds on its first fixed run.
Exact Taylor expansion confirms (2.1). All ten hinge normal-area identities
are checked against literal triangle Gram determinants, and all ten normal
planes against literal edge vectors. A separate census of six 2+2 splits
checks the mixed shear coefficient.

A 65-digit nonlinear cell-action implementation uses projected legs and hinge
Gram matrices, independently of the normal-angle expressions in (1.1).
At lambda +/-0.2 its direct action agrees with the integral of (1.2) within
1.4e-63. Along (mu,H_12)=(epsilon,c epsilon), c=0,1,-1, two-step odd-part
extrapolations at .002 and .001 give cubic coefficients 1/8,3/8,-1/8 within
1.3e-12. These finite-step values support the separately derived coefficients;
there is no interval remainder certificate or independently reviewed theorem.

A useful cancellation control is a two-cube excess (a,-a): its cubic action
sums to zero, but each hyperdiagonal equation has leading 3a^2/8, and the
uniform-shear projection has leading a^2/2. Vanishing action on a path is not
stationarity. The stronger differentiable-curve statement follows analytically
from the zero first derivative of the projected equation; it does not require
another numerical sweep.
