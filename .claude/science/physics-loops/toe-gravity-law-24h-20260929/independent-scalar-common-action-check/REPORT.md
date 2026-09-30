# Focused independent coupled-scalar proof check

2026-09-30. No blocking mathematical discrepancy was found in the author
proof bound below. It supplies a consistent massless canonical scalar
coupling, grid-uniform short analytic-time comparison for the actual
finite Hamiltonian, and an explicit nonempty family of compatible
analytic continuum initial data. This is a dependent component of the
same nonlinear approximation construction, not formal review, audit,
retained status, a native matter derivation, or an original-record
gravitational coupling.

The checked REPORT has SHA256
`647b1ed39b9fac225b5db07e34fdf64babad273640c99dd471b50f34e8bafd35`.
The author freeze is 03:25:13 UTC. This check covers that proof, before
any diagnostic implementation or execution. It does not cover later
diagnostic code/results or later changes to the proof. SOURCE_BINDINGS.json
records the exact contract and parent-proof dependencies.

## Independence and actual work

I read only the new CONTRACT initially. PRECOMPARISON.md was frozen
at 03:26:08 UTC with SHA256
`8a4bd3c514d172600905de5e24870c0a905f2188c4fcc390b5f0a3643b20295a`
before opening the author REPORT. It independently derived the scalar
and metric variations, full continuum algebra, augmented analytic
structure, conformal coefficients and an explicit convergent iteration.
I used a radius 1/100 with a simple sufficient smallness bound; the
author uses radius 1/128 and different explicit constants. Their
agreement was assessed after the freeze, not assumed beforehand.

I then read the complete REPORT and FREEZE. No numerical computation,
author-code import/execution, external theorem import, shared edit or
new delegation was used. The previously checked gravity spectral and
centered proofs are reused only for their stated analytic quantifiers.
I do not independently endorse all prior-art comparisons in the new
author context paragraph; the new coefficients and contraction below
were obtained directly from the supplied law.

## Coupled canonical variation and full algebra

Set S=sqrt(det g), B=S g^{-1}, s=aK, and z=D phi. The supplied matter
density is M=w^2/(2S)+(s/2)B^ij z_i z_j. Since w=n^3 W, the normalized
mean cancels the density-coordinate Poisson factor. Actual skew summation
by parts gives phi_dot=w/S and w_dot=s D_i(B^ij z_j). The scalar-gradient
augmentation satisfies z_dot=D(w/S), preserving z-Dphi exactly in time.

The metric velocity is unchanged because M contains no metric momentum.
Its conjugate equation acquires the actual local stress -M_g, at fixed
w,z. For a symmetric metric variation E, independently differentiating
the density gives

    delta M=-w^2 tr(g^{-1}E)/(4S)+(s/2)B'[E]^ij z_i z_j,
    B'[E]=S[(1/2)tr(g^{-1}E)g^{-1}-g^{-1}E g^{-1}].

Inserting both entries of an off-diagonal E is equivalent to the stated
six-coordinate convention pi_offdiag=p_offdiag/2. Thus the metric
response is included rather than treating the scalar as test matter.
The existing q=Dg,r=DB adjoint equations and exact consistency identities
are unaffected, including B_g outside D V_r. No finite spatial chain
rule is introduced. All equations in author (2) agree with this variation.

The canonical action has the correct density pairing mean(pi:gdot+w
phidot). For the finite evolution, N=1 and X=0 are fixed and variation
is in the canonical fields. The proof does not assert that varying
finite multipliers produces a preserved finite first-class constraint
surface. Its exact constraint algebra is explicitly a continuum result.

In that continuum, the scalar functional derivatives give directly

    {C_m[N],C_m[M]}=G_m[s g^{-1}(N dM-M dN)].

For the mixed terms, the curvature/scalar bracket is zero. The kinetic
metric/scalar bracket is pointwise in metric variation, with the same
factor NM in the two orders, so the antisymmetrized cross sum cancels.
This latter cancellation remains true on the finite grid, but the pure
finite scalar bracket need not have the continuum form. The report
correctly separates those assertions.

The complete gravity-plus-scalar spatial generator is the cotangent
momentum map: it acts on g as a covariant metric, on pi as its density
dual, on phi as a scalar and on w as a density. Therefore M transforms
as a scalar density, which proves the full GC identity, while the two
independent carriers give the full GG identity. Combining the scalar
CC calculation with the already checked gravity bracket yields the
common structure shift s g^{-1}(N dM-M dN). The choice s=aK is essential
to that common coefficient. This is not merely coefficient-jet closure.

The total densities are exactly C_g+M and
J_k=pi^ij partial_k g_ij-2partial_j(g_ik pi^ij)+w partial_k phi.
At unit lapse/zero shift the same smearing derivation gives J_dot=0 and
C_dot=partial_j(s g^ij J_i). These are total constraints; the separate
gravity and matter momentum densities need not be conserved. Metric
dependence of the shift is retained in the continuum functional algebra.
There is no inference of finite exact closure from canonical Jacobi.

## Analytic evolution and actual finite constraints

The enlarged U=(h,p,q,r,phi,w,z) still has the form
F0(U)+sum P(U)D_j Q(U). The new maps are polynomial in w,z and analytic
in the metric on the same regular ball. The metric-safe condition is
unchanged, while the initial total norm, local majorants and Lipschitz
constants must be increased. Section 3 explicitly does so.

Its extra initial bound on z follows from the summed gradient seminorm,
so no additional factor three is missing. Using ||phi0|| rather than
removing its mean is harmlessly conservative. The metric velocity
estimate is still permitted with the enlarged M, since the actual
velocity remains T_p. The original shrinking-radius, continuation,
compactness and time-ordered Volterra proofs then apply with the new
constants and a new positive common time. The proof does not silently
keep the vacuum's numerical constants or require a lower derivative
symbol bound.

The initial scalar-gradient mismatch adds the sampling commutator on
phi0. The finite source adds the scalar P,Q terms. The previously
checked spectral exponential bound and centered all-alias epsilon^2
bound therefore transfer with enlarged constants. The actual finite
total densities include w z_k and the scalar energy, in addition to
the literal gravity densities. Their at-most-one-derivative form in
augmented U gives the smaller-radius error estimate. Exact continuum
propagation then turns this into finite constraint bounds for compatible
initial data. Neither initial finite defects nor later high modes are
discarded. The centered Hamiltonian remains supported on radius-one
stars, with equation stencils of radius at most two.

## Independent conformal normalization

For phi=b f, w=0, g=psi^4 I and pi^ij=-(2H/a)psi^2 delta^ij, the two
gravity momentum-density terms are respectively
-(24H/a)psi^5 partial_k psi and +(24H/a)psi^5 partial_k psi. Their
cancellation requires H constant and is exact in the continuum.

The trace contractions give the kinetic density -(6H^2/a)psi^6.
Computing the conformal Christoffels, or inserting omega=2log psi into
the three-dimensional conformal expression, gives
R=-8psi^{-5}Delta psi. The squared-gradient terms cancel. Adding the
scalar density (aK b^2/2)psi^2 q, q=sum_i(partial_i f)^2, produces

    Delta psi+lambda q psi-c_H psi^5=0,
    lambda=a b^2/16, c_H=3H^2/(4aK).

These signs and constants agree with author (7). Taking the mean fixes
c_H=lambda<q psi>/<psi^5>, and therefore
H^2=(a^2 K b^2/12)<q psi>/<psi^5>. No arbitrarily prescribed H is
being smuggled into the compatibility equation. Either expansion sign
can subsequently be supplied.

Writing psi=1+u and using the genuine negative-symbol Delta_0^{-1}
gives exactly author (8). In particular the minus sign in front of
lambda Delta_0^{-1} is correct. The input to that inverse is identically
mean zero, so its omission of the zero Fourier mode loses no equation.
On the period-2pi torus its mean-zero Wiener norm is at most one.

## Contraction constants and compatible data

Let R=1+r, d=2-R^5 and B=||q|| at rho=2sigma0. On the complex ball
||u||<=r, the denominator's distance from 1 is at most R^5-1; its
modulus is consequently at least d. Direct product and quotient bounds
give the author's

    A=R+R^6/d=2R/d,
    L=1+6R^5/d+5R^10/d^2.

For clarity, the derivative of the quotient c(u) is bounded by
B[1/d+5R^5/d^2]. Multiplying by (1+u)^5 and adding the derivative of
that factor yields the three terms in the report. This independently
reproduces its Lipschitz constant without invoking a conformal-method
existence theorem or an unpriced elliptic regularity estimate.

Under lambda B<=min(r/(2A),1/(2L)), the map sends the radius-r ball
into radius r/2 and has Lipschitz constant at most 1/2. Banach iteration
from zero therefore has the stated tail bound
2 lambda B A 2^{-m}. Reality and zero mean are preserved. The limit
is positive on the real torus because psi>=1-r. Nonconstant real f
makes q nonnegative and not identically zero; hence c(u)>0 and H^2>0
for b!=0. Real trigonometric f makes all stated input norms explicitly
finite at any fixed radius, and condition (10) supplies a computable
nonzero amplitude interval.

The factor three in the metric entry norm is essential and is present.
At the author's r=1/128 the exact upper bound is
3[(129/128)^4-1]=25462275/268435456<1/8. The momentum bound
6|H|R^2/a also has the correct three-diagonal normalization. Thus the
constructed data really satisfy the analytic evolution hypotheses.

As a separate check recorded before comparison, f=cos x_1 gives the
first iterate u_1=-(lambda/8)cos(2x_1) and leading
H^2=a^2 K b^2/24+O(b^4). This checks both the inverse-Laplacian sign
and the kinetic normalization. Nonzero b with this f cannot yield a
constant psi, so the class includes an inhomogeneous metric as well
as a nonconstant scalar. Conformality and w=0 specify initial data
only; the theorem evolves the full coupled fields afterwards.

## Scope and outstanding factual controls

The proof-only continuation is valid at the supplied massless-scalar,
analytic near-flat, unit-lapse scope stated above. It gives actual
compatible continuum data and actual finite Hamiltonian approximations.
It does not derive this scalar from the original rotor records or walker,
identify a physical source clock, prove exact finite constraints, cover
arbitrary conformal data, or establish long-time/Sobolev stability.

I did not implement, read or check any diagnostic in this check of the
frozen proof. A future finite contraction solve must distinguish its
truncation/rounding error from the exact analytic solution. A future
trajectory must include the metric stress and report literal finite
total constraints, including their initial defects. Such factual
controls need new source bindings; their existence or success has not
been presumed here. No formal disposition or downstream physical
claim follows from this focused check.
