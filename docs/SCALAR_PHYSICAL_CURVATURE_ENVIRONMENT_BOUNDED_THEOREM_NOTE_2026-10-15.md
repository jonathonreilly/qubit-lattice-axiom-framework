# Bounding the scalar environment from the physical static metric

Claim type: bounded_theorem.
Actual current surface status: conditional-support.
Scientific author: /root.
Primary runner: [scalar_physical_curvature_check.py](../scripts/scalar_physical_curvature_check.py).

A homogeneous density minimum does not determine the field inside a finite body.
The earlier [finite-body result](EXPONENTIAL_SCALAR_FINITE_BODY_BOUNDED_THEOREM_NOTE_2026-10-14.md)
already gave excursion, force and uniqueness bounds in a flat, held-source,
radial-channel model. The result here removes those particular restrictions
from a necessary environmental bound: it uses the complete three-field action
and the physical static metric, with no identification of the action's Q with
a measured Newton constant. The actual metric and ambient boundary still have
to be supplied and calibrated. No observed metric array or empirical test is used.

## Supplied action and exact claim domain

Use the [complete candidate action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md),
signature (-+++), natural units, phi=(u,x,y), and
```text
S = Q integral sqrt(-gE) [R_E/2 - K_AB dphi^A dphi^B - 2 Hv^2 U]
    + S_m[A^2 gE, matter],
Q>0, Hv>0, nu>0, 0<k<1/3,
a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/[k(1-3k)],
E=exp(2alpha u), F=1+sE, J=1+(1-3a)sE,
D=1+2(1+k)(x^2+y^2)/3,
K=diag[J/F^2, (1+s)4k/(9FD), (1+s)k/(3FD)],
A^2=(1+s)E/F,
U=3/2+3s(E-1)^2/(2F^2)
  +(k/2)x^2 exp[-(1-k)u/alpha]
  +(k/3)y^2 exp[-(1+k)u/alpha]
  +nu(1+s)u^2/(2F^2).
```
The action, potential, fields, universal matter metric, k, nu, Hv and Q remain
conditional candidate inputs. This calculation does not derive or select them.

Let gJ=A^2 gE be the physical metric and z=exp(-alpha u)>0; z is a field
coordinate, not an observed redshift. All scalar fields and the metric are
static on a bounded smooth spatial domain Omega:
```text
ds_J^2=-N(X)^2 dt^2+h_ij(X)dX^i dX^j,
L_J f = [N sqrt(h)]^-1 partial_i[N sqrt(h) h^ij partial_j f].
```
Take N,h smooth enough to define continuous curvature and classical elliptic
comparison (C3 on the closure suffices), N bounded away from zero, h uniformly
positive definite, and finite C2 scalar fields. The boundary of Omega includes
every connected boundary component. A finite bound z<=zB on that complete
boundary, with zB>=1, is an explicit premise. A horizon or an uncontrolled
inner boundary is outside this domain.

Write R_J for the four-dimensional physical Ricci scalar, not the spatial
curvature. Let c=(R_J)_+/2 and solve the uniquely defined Dirichlet problem
```text
-L_J P=c,  P|boundary=0,  P>=0,
Pmax=sup_Omega P,  lambda=a/(1-3a)>0,  eta=lambda Pmax.
```
If eta<1, every solution in this class necessarily obeys
```text
z(X) <= zB [1+lambda P(X)/(1-eta)] <= zB/(1-eta).       (1)
```
No field-gradient or force bound, existence, dynamical attraction, material stability or unique environment
is inferred. Failure of eta<1 is inconclusive. The inequality is not claimed
uniform as k approaches1/3, an elliptic metric degenerates, or eta approaches1.

## Derivation from the complete action

The useful simplification is an exact change of variables, not a new action
selector. Put f0=Q/(1+s) and Z=Q(1-3a)/[a(1+s)]. Then
1-3a=(1-3k)^2/4>0. The Weyl transformation, after a total divergence is removed,
gives
```text
S = integral sqrt(-gJ) [
 f0(s+z^2) R_J/2 - Z (dz)^2
 - Q z^2 {4k(dx)^2/(9D)+k(dy)^2/(3D)} - V_J
] + S_m[gJ,matter],

V_J = 3Q Hv^2(s+z^4)/(1+s)
 + Q Hv^2 nu z^4(ln z)^2/[a(1+s)]
 + Q Hv^2 k x^2(s+z^2)^2 z^rx/(1+s)^2
 + 2Q Hv^2 k y^2(s+z^2)^2 z^ry/[3(1+s)^2],
rx=(1-k)/a>0, ry=(1+k)/a>0.                           (2)
```
For example the radial kinetic coefficient is
```text
(Q/A^2)[K_uu-3(partial_u ln A)^2](du/dz)^2 = Z,
```
because J-3a=(1-3a)F. The constant and base potential combine to the first
quartic expression in (2); the positive vacuum energy has not been subtracted.
Variation at fixed physical metric leaves no direct matter-z term.

The complete static z equation is
```text
L_J z = -(lambda/2) R_J z
 + {Q z [4k |grad x|_J^2/(9D)+k |grad y|_J^2/(3D)]
     +(1/2) partial_z V_J}/Z.                         (3)
```
Both transverse gradient terms are nonnegative. For z>=1, every potential
derivative in (2) is nonnegative and the base derivative is strictly positive.
The nontrivial factors are
```text
d[z^4(ln z)^2]/dz = z^3[4(ln z)^2+2ln z] >=0,
d[(s+z^2)^2 z^r]/dz
 = z^(r-1)(s+z^2)[r(s+z^2)+4z^2] >0, r>0.
```
This sign argument does not set x=y=0 or assume negligible material pressure.
It does require static scalar fields: Lorentzian time-gradient terms would not
have these spatial signs. The prescribed universal matter coupling is essential.

The sign domain is substantive. At x=y=0,
```text
partial_z V_J = Q Hv^2 z^3/[a(1+s)]
               {12a+nu[4(ln z)^2+2ln z]}.
```
At z=exp(-1/4), the bracket is12a-nu/4, which is negative for nu>48a.
Thus the parameter-uniform proof cannot simply replace zB>=1 with an arbitrary
positive boundary. That counterexample disproves the extended derivative-sign
claim, not every possible environmental bound below z=1.

For v=(z-zB)_+, the weak Kato inequality for this uniformly elliptic,
lapse-weighted divergence operator and (3) imply
```text
-L_J v <= lambda c(v+zB),  v|boundary=0.                (4)
```
On z>zB, the positive terms in (3) can be dropped in this direction and
R_J replaced by its positive part. On the complementary set, the right side
of (4) is nonnegative. Positive Dirichlet Green comparison therefore gives
```text
v <= lambda G[c v]+lambda zB P.
```
Finite fields on the compact closure have finite V=sup v. Positivity gives
V<=eta(V+zB), hence V<=eta zB/(1-eta). Inserting that bound into the pointwise
Green comparison proves (1). This uses neither a chosen effective mass nor
convexity nor a homogeneous density minimum.

## Complementary bound when the potential scale is supplied

The focused independent derivation also produced a pointwise maximum argument;
root then checked its factors directly against (2),(3). At an interior maximum
z>zB, L_J z<=0. The positive transverse terms and the base quartic imply
R_J>=12Hv^2 z^2 there. Consequently

```text
z <= max[zB, sqrt(max(sup R_J,0)/(12Hv^2))].           (9)
```

Keeping the nonnegative regulator replaces the square-root threshold by the
unique root, when sup R_J>12Hv^2, of

```text
Fcurv(t)=12Hv^2 t^2+(2nu Hv^2/a)t^2 ln(t)[2ln(t)+1], t>=1.
Fcurv'(t)=24Hv^2 t+(2nu Hv^2/a)t[4ln(t)^2+6ln(t)+1]>0.
```

For sup R_J<=12Hv^2 the threshold is1. The ceiling is the maximum of this
threshold and zB. It can be combined with (1) by taking the smaller admitted
bound. This complementary statement needs the numerical Hv, unlike (1).
It does not infer Hv from cosmic expansion or select it to fit a body.

## Consequences and what they measure

Let zCap=zB/(1-eta). The exact conformal factor and
[local coupling norm](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md)
give
```text
A^2 >= (1+s)/(s+zCap^2),
Fgrav=Q/A^2 <= Q(s+zCap^2)/(1+s),
Fgrav/Fgrav(zB) <= (s+zCap^2)/(s+zB^2) <= (1-eta)^-2,
q=beta^2 = a z^2/[z^2+(1-3a)s]
 <= a zCap^2/[zCap^2+(1-3a)s].                        (5)
```
The last inequality follows from the strictly positive derivative of q with z.
Writing qB=a zB^2/[zB^2+(1-3a)s] also gives
```text
q <= a qB/[qB+(a-qB)(1-eta)^2].                       (6)
```
Here qB>=k because zB>=1. It is the coupling at the stated boundary ceiling,
not automatically a measured boundary coupling. A calibrated coupling bound
could be inserted only with its complete force/range/matching assumptions.

Fgrav is the coefficient of R_J/2 in the action. It is not, without a response
model, the inverse of an experimentally calibrated Newton constant. Equations
(1),(5) eliminate an absolute Q identification from this necessary bound; they
do not determine Q, a source mass or a material equation of state. A proposed
homogeneous interior value beyond zCap is incompatible with the stated
metric/boundary class, not a theory-wide or observational exclusion.

## Constructing P from a spherical physical metric

Use physical areal radius r, with a regular center and
```text
ds_J^2=-N(r)^2 dt^2+dr^2/B(r)+r^2 dOmega^2,  0<=r<=L.
```
Writing ell=ln N gives
```text
R_J=-2B(ell''+ell'^2+2ell'/r)-B'ell'-2B'/r+2(1-B)/r^2,
L_J f=B f''+(2B/r+B ell'+B'/2)f'.                     (7)
```
For c=(R_J)_+/2, regularity and P(L)=0 give the direct quadrature
```text
P(r)=integral_r^L ds/[N(s)s^2 sqrt(B(s))]
       integral_0^s dt N(t)t^2 c(t)/sqrt(B(t)).
```
It is nonincreasing, so Pmax=P(0). For certified bounds
Nmin<=N<=Nmax, B>=Bmin>0 and (R_J)_+<=Rmax,
```text
Pmax <= (Nmax/Nmin) Rmax L^2/(12 Bmin).                (8)
```
These are sufficient metric error envelopes, not quantities inferred from
unreported data. A constant rescaling of N changes neither (7) nor P, so no
absolute clock normalization is required. Actual metric reconstruction, second
derivative control, staticity, radius calibration and boundary information remain.

For an ideal continuum of stationary physical clocks and vacuum radial ranging,
let f(r)=N(r)/N(r0) be the lapse ratio inferred from the reciprocal received/emitted
frequency ratio. Let tau(r) be the roundtrip proper time at the fixed emitter r0,
with an instantaneous reflection and independently calibrated areal endpoint r>r0
on the outward side of the emitter. The center-emitter case uses r0=0 and
the regular limit at the center. On such an interval the radial null equation gives

```text
tau(r)=2N(r0) integral_r0^r ds/[N(s)sqrt(B(s))],
g(r)=tau'(r)=2/[f(r)sqrt(B(r))],
B(r)=4/[f(r)^2 g(r)^2],
R_J=2B[-f''/f+(f'/f)^2+(f'/f)(g'/g)+2g'/(rg)]
    +2(1-B)/r^2.                                    (10)
```

These are exact geometric identities within this declared static spherical
measurement model, not data-derived profiles. They distinguish the two needed
metric functions rather than replacing either with a GR density law. A finite
noisy set of clock/range values needs derivative-error control before (10) yields
a curvature bound. Small function-value errors alone do not control second
derivatives: a smooth compact ripple epsilon b(r)cos(r/epsilon) has vanishing
amplitude and growing second derivatives. This is a kinematic error-control
example, not a full candidate solution or a measurement impossibility theorem.

An exact full candidate-vacuum check is z=1,x=y=0 with
N^2=B=1-Hv^2 r^2 and R_J=12Hv^2, on a ball strictly before the horizon.
Equation(3) balances partial_z V_J/(2Z)=6lambda Hv^2 against its curvature term.
The Green solution is
```text
P(r)=ln[B(r)/B(L)],  Pmax=-ln(1-Hv^2 L^2).
```
Thus the full positive vacuum curvature is retained. Schwarzschild has R_J=0;
a vacuum exterior still has its inner boundary, which cannot be dropped when
applying a finite-domain comparison.

## Primary-source comparison

The physical-frame curvature source is established scalar-tensor structure:
[Salgado, gr-qc/0509001v2](https://arxiv.org/pdf/gr-qc/0509001v2),
Section II, supplies a single-field convention comparison. The conformal kinetic
transformation is compared with [Kaiser, 1003.1159v2](https://arxiv.org/pdf/1003.1159v2),
Sections II and the opening of III. The candidate-specific algebra and comparison
above are displayed, rather than inferred from those sources or claimed novel
merely because they use physical curvature.

[Khoury and Weltman, astro-ph/0309411v2](https://arxiv.org/pdf/astro-ph/0309411v2),
Sections II-III, provides the competing finite-body matching example: its supplied
runaway potential, coupling, densities and boundary determine an approximate
shell response. That shell factor and its ambient minimum are not imported here.
[Philipp et al., 1702.08412v2](https://arxiv.org/pdf/1702.08412v2), Section III,
compares the stationary clock relation; it does not provide the spatial metric.
[Faber and Visser, astro-ph/0512213v2](https://arxiv.org/pdf/astro-ph/0512213v2),
Sections2-9, compares combining dynamical and lensing metric information. Their
GR density/pressure interpretation is not used as a scalar-theory curvature law.

These are bounded primary reading scopes with version/hash records in the
independent source packet, not an exhaustive novelty search or current empirical
admission. Exterior Weyl/tidal information is not an interior Ricci bound.
Static geometry alone also does not establish static scalar fields. Both
qualifications are retained in the theorem premises above.

## Computation, failed attempts and observational status

Author exact checks derive the transformed action from its original expressions,
vary the full Jordan action, contract the Christoffel curvature directly, and
check Schwarzschild/de Sitter/anti-de Sitter limits. The Green quadrature is
compared with a separately solved elliptic boundary-value problem. Six synthetic
radial scalar solves then check the global and pointwise ceilings and an
independent integrated flux residual. They solve the scalar equation in supplied
metrics, not the complete Einstein/matter system. They are mathematical
development controls, not astronomical or laboratory observations.

The frozen synthetic protocol uses k=0.1, nu=0.0001, unit domain radius,
zB=1, N=1-epsilon r^2, B=1-b r^2, (b,epsilon) equal to
(0.01,0.005), (0.08,0.04), (0.07,-0.015), and Hv=0.005 or0.05.
All supplied N,B are positive. Their curvature is monotone in r^2, with
derivative4epsilon(3epsilon-4b)/(1-epsilon r^2)^2, so endpoint bounds
suffice for (8). The protocol precedes those numerical outputs. No parameter
was fitted to make a measured outcome agree.

An initial symbolic control could not simplify two equivalent logarithms
without the static-chart domain. It is preserved as48passed/1failed.
The repaired control parametrizes Hv^2 L^2=1-exp(-p), p>0, covering the entire
admitted domain; it changes no field equation, tolerance or synthetic input.
The initial density-trace route reconstructed a prior bound and retained Q;
it is preserved as an unpromoted route. The physical-metric route above is the
substantive change. Independent review and final source-bound execution are
recorded separately in the campaign evidence packet.

The complete physical action, actual initial/ambient state, absolute scales,
calibrated metric with curvature errors, static domain, and observational
identification of q or Fgrav remain open suppliers. No environmental solution,
new independent empirical test, formal audit grade or TOE is asserted.
