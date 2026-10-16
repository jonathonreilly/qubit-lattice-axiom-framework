# Independent static physical-metric inverse

## Finding and exposure

For fixed positive s and lambda, the supplied radial action has an algebraic local inverse on a regular nonconstant-scalar branch. It does not require an independent scalar boundary value, but it requires the full ideal metric and its derivatives plus a differential compatibility condition. “Nonconstant metric” alone is insufficient: a nonconstant Schwarzschild metric with V=0 admits every positive constant z. The inverse also does not establish that a measured metric, or the inherited specific potential, is admissible.

This derivation was frozen before access to any author M19 working derivation or source. The supplied action and task description, and the earlier M17 context, are disclosed in `PREMISES_v1.txt`. All equations below were independently derived from that action. The executable checks build the connection and Ricci tensor directly from the four-dimensional metric. No external source, observed data, author implementation, or aggregate was accessed.

## Equations and conventions

Set w=s+z², v=V/f0, A=N'/N and

C=B A+B'/2+2B/r.

Work on an open interval r>0 with N>0, B>0 and finite regular fields. For convenience N in C4 and B in C3 suffice for the metric expressions and compatibility below; a reconstructed solution is required to be C2 with a C1 potential on its scalar range. A prime is d/dr. The metric variation divided by f0 is

w G_mu_nu = (2/lambda) z_,mu z_,nu
             -g_mu_nu[(partial z)²/lambda+v]
             +nabla_mu nabla_nu w-g_mu_nu Box w.

The scalar equation is

E_z=(2/lambda) Box z+z R-v_z=0.

In particular the kinetic normalization is Z, not Z/2. The mixed Einstein components are

G_t=(B-1)/r²+B'/r,

G_r=(B-1)/r²+2BA/r,

G_a=B(A'+A²+A/r)+(B'/2)(A+1/r),

with R=-(G_t+G_r+2G_a). Also Box z=Bz''+Cz', and the mixed Hessian components of w are BA w', B w''+B'w'/2, and B w'/r. Thus the independent metric equations are

w G_t=-Bz'²/lambda-v-Bw''-(B'/2+2B/r)w',

w G_r= Bz'²/lambda-v-B(A+2/r)w',

w G_a=-Bz'²/lambda-v-Bw''-(BA+B'/2+B/r)w'.

These signs and metric slots are independently checked against the direct Ricci/Hessian construction.

## Potential-free reconstruction

Define metric functions

H=B(A-1/r),   K=G_t-G_a.

The time-angular difference gives exactly

H w'=K w.

On an interval H!=0, set p=K/H, so w'=p w. The time-radial difference is

w(G_t-G_r)=-2Bz'²/lambda-Bw''+(BA-B'/2)w'.

Consequently define

J=-(G_t-G_r)/B-p'-p²+(A-B'/(2B))p.

For any solution on that chart,

J=2z'²/(lambda w)=p² w/[2lambda(w-s)].

On the further regular branch p!=0 define

Theta=2lambda J/p².

A finite positive z then requires Theta>1 and is uniquely fixed by

z²=s/(Theta-1),   w=s Theta/(Theta-1).

The positive square root fixes z because positivity was supplied. Equivalently h=1/Theta=p²/(2lambda J) must satisfy 0<h<1, and z²=s h/(1-h). No integration constant or boundary value appears in these formulas. The positive offset s is essential to this normalization: with s=0, which the task excludes, the same difference would merely enforce Theta=1 and would not fix the amplitude.

Pointwise positivity is not sufficient. The reconstructed w must have the derivative already demanded by the time-angular equation:

Theta'+p Theta(Theta-1)=0,

or equivalently h'=p(1-h).

This is a metric compatibility identity on an open interval, not a freely chosen scalar evolution. It typically involves fourth lapse derivatives and third B derivatives. Ideal derivative information and a stable error envelope are substantive suppliers. Near H=0, p=0 or Theta=1 the displayed inverse is ill-conditioned or undefined; a finite sampled metric alone is not such a supplier. A constant normalization of N cancels from every expression. The overall coefficient f0 also cancels, so neither this inverse nor the metric determines f0 or identifies it with measured Newton gravity.

## Inferred potential and completeness

The radial equation fixes the potential value along the reconstructed branch:

v(r)=w[BJ/2-B(A+2/r)p-G_r].

Thus even the potential offset along this range is fixed; it is not an additional integration constant. Since p!=0 and z>0, z'=p w/(2z)!=0. A sufficiently small connected interval has a monotone scalar coordinate, so v(r) defines a single-valued local v(z). Values outside that scalar range remain unconstrained. If a particular V(z) is supplied, equality with V(z(r))/f0 is a separate necessary test; the inverse has not derived that candidate potential or its parameters by definition.

Conversely, on the admitted chart, construct w,z by the formula, impose the differential compatibility and the displayed potential relation. The time-angular difference then vanishes. The identity defining J and its reconstructed kinetic value make the time-radial difference vanish. The radial equation holds by construction, hence all three metric equations hold. Write their residuals as E_t,E_r,E_a. Direct calculation gives the radial Noether identity

E_r'+A(E_r-E_t)+(2/r)(E_r-E_a)=-E_z z'.

All metric residuals vanish, and z'!=0, so the scalar equation follows. This establishes local metric/scalar completeness for absent vacuum matter. It does not solve a separately supplied matter field equation or establish a global regular spacetime. With a reconstructed potential the result is solution membership for some local potential; with a fixed potential it is membership only after the value comparison. No full inherited three-field solution follows from dropping its other fields.

## Degeneracies and decisive failures

1. If H=0 at an isolated point, regularity requires K=0 there. The direct ratio cannot be used. If both vanish, continuation from nearby regular points or differentiated equations may determine a limit, but no general pointwise uniqueness is asserted. If H is identically zero on an open interval, then A=1/r and direct geometry gives K=-1/r² independently of B. That contradicts w>0 in the vacuum time-angular difference. Thus an open N proportional to r interval is excluded by this particular action class and static chart. It is not a statement about horizons or arbitrary matter.

2. If p=0 at an isolated turning point, z'=0 and J=0 there for a solution. Theta is 0/0. No division or scalar-equation conclusion is valid at that point by itself. A regular neighboring solution can impose additional limiting data.

3. If p=0 on an open H!=0 interval, z is constant. A solution must have G_t=G_r=G_a=-Lambda with constant Lambda, v(z0)=Lambda(s+z0²), and the independently imposed scalar condition v_z(z0)=4Lambda z0. Bianchi does not impose the last condition when z'=0. The Schwarzschild-de Sitter metric B=1-2M/r-Lambda r²/3, N²=constant*B realizes these Einstein components. With Lambda=0 and v identically zero, every constant z0>0 is allowed for the same nonconstant Schwarzschild metric. This disproves an unconditional “nonconstant metric fixes z” claim.

4. A useful false-positive witness is N=1, B=2/3, s=lambda=1. It gives p=1/(2r), J=1/(4r²), Theta=2. The algebraic expression would return z=1, but the compatibility residual is 1/r, not zero. Therefore pointwise domain admission is not a solution test.

5. A separate sign witness N=r², B=1 gives p=-4/r, J=-24/r² and Theta=-3lambda. It cannot lie on the positive-scalar regular branch. No negative or complex root should be silently substituted.

r=0, B=0, lapse zeros and boundaries are outside this coordinate proof; they require their own regular limits or charts. These are local degeneracies, not a universal no-go.

## Optional transverse-field qualification

For additional static radial scalar fields with positive kinetic form and the same F(z), let k_perp be their radial kinetic density divided by f0 before multiplication by B. The time-angular relation remains unchanged, while

J=p² w/[2lambda(w-s)]+2 k_perp/w,

Theta=w/(w-s)+4lambda k_perp/(p² w).

Thus the same regular metric supplies at most the necessary lower bound

z² >= s/(Theta-1),

rather than the radial-only equality; Theta>1 is still necessary. Equality at one point only removes kinetic motion there, not the transverse coordinates. Equality on an interval implies constant transverse fields when the kinetic form is positive definite; their potential equations still have to hold. This statement assumes static radial fields, the stated coupling and positive kinetic form. It does not cover arbitrary angular structure or nonspherical stress. I have not read or rechecked any new inherited transverse truncation in this block.

## Independent executable checks and scope

`independent_checks_v1.py` records 35 exact checks with zero failures. They include the direct four-dimensional Ricci/Hessian calculation, metric differences, radial Noether identity, normalization/compatibility algebra, both rejected metric witnesses, the full Einstein plateau and the positive transverse correction. The script does not execute root code.

A separate exact local-jet construction prescribes z=1+r solely as a synthetic verification. Solving the two original potential-free metric equations for B' and A' defines a smooth first-order ODE near r=1, s=1, lambda=2, A=1/5, B=4/5. It yields B'=-4/175, A'=97/700, p=4/5, J=1/5, Theta=5/4, reconstructed z²=4 and v=-181/25. The total derivative along this ODE satisfies compatibility identically. Local existence follows from smoothness of those rational right sides near the stated point, not from an unperformed numerical integration. This fixture tests the general action with an inferred potential; its negative v does not certify admission to the inherited specific positive-potential candidate. It does not select a physical scalar state.

No failed executable attempt occurred in these 35 checks. The constant-scalar, incompatible-positive and wrong-sign metrics are deliberately preserved analytic failure witnesses. No actual measurements, derivative error budget, field boundary, full coupled material model, global solution, theory selection, or novel-literature claim is supplied. This is an independent algebra check, not a formal audit.
