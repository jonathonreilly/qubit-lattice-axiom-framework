# A nonlinear scalar inverse from a static physical vacuum metric

Claim type: bounded_theorem.
Actual current surface status: conditional-support.
Scientific author: /root.
Primary runner: [scalar_vacuum_metric_check.py](../scripts/scalar_vacuum_metric_check.py).
Executable derivation and synthetic controls: [scalar_vacuum_metric_inverse.py](../scripts/scalar_vacuum_metric_inverse.py).
Weak integral construction: [scalar_vacuum_metric_weak.py](../scripts/scalar_vacuum_metric_weak.py).

A complete, nondegenerate static vacuum metric can determine the revised
candidate's radial scalar profile, kinetic parameter and two potential
coefficients without supplying a scalar boundary value. This is an inverse
within an explicitly supplied action family and single-scalar sector. The
metric, vacuum identification, sector and derivative calibration are inputs.
No actual measured metric has been supplied or tested here.

The earlier [physical-metric ceiling](SCALAR_PHYSICAL_CURVATURE_ENVIRONMENT_BOUNDED_THEOREM_NOTE_2026-10-15.md)
used a scalar equation and a complete scalar boundary. This result instead
uses all independent metric equations and their compatibility. It reconstructs
the field on a nonconstant branch, and tests the potential across an interval.
The earlier [action/scale reconstruction](EXPONENTIAL_SCALAR_ACTION_SCALE_BOUNDED_THEOREM_NOTE_2026-10-14.md)
already separates reconstruction from action selection and explains why a
classical source-free solution cannot fix an overall action coefficient.
That limitation remains.

General static spherical reconstruction in scalar-tensor gravity is established.
[Bronnikov, Badalov and Ibadov, arXiv:2212.04544v1](https://arxiv.org/abs/2212.04544v1),
Section 2, reconstruct the coupling, kinetic function and potential from a
metric, using an angular-time equation and a monotonic scalar parametrization.
[Ernazarov, arXiv:2603.22517v1](https://arxiv.org/abs/2603.22517v1), Section 2,
uses a constant canonical kinetic coefficient and reconstructs the coupling
and potential through a first-order master equation. Those general procedures
are prior methods, not new results of this campaign. Here the coupling's
quadratic form, kinetic/parameter relation and two-coefficient potential are
fixed in advance. Equations (8)--(12) impose that family's compatibility and
recover its parameters where identifiable. No claim of global novelty for
this specialization follows from this limited literature comparison.

## Precise supplied premises and target

Use signature (-+++), natural units, and the physical Jordan metric in the
first linked note. In the sector x=y=0 the action is

```text
S = integral sqrt(-g) [F(z) R/2 - Z (dz)^2 - V(z)],
F=f0(s+z^2), Z=f0/lambda, f0=Q/(1+s)>0, z>0,
0<k<1/3, a=(1-k)(1+3k)/4, lambda=a/(1-3a)>1,
s=(1+k)/[k(1-3k)], Hv>0, nu>0,
V/f0=Hv^2 [3(s+z^4)+(nu/a)z^4(ln z)^2].             (1)
```

There is no material stress tensor on the interval. Material vacuum does not
mean zero scalar stress or zero curvature. In the full supplied three-field
action, F and the z kinetic coefficient are independent of x,y; the potential
and transverse kinetic coefficients are even in x and y. With x=y=0 and their
derivatives zero, both transverse Euler–Lagrange equations vanish. Thus this
is a consistent classical sector. Its physical selection, stability and
preparation are not established by that fact.

Let r range over a connected finite annulus, 0<r_-<r<r_+. In calibrated areal
radius and a common static time coordinate, suppose the full metric is given:

```text
ds^2=-N(r)^2 dt^2+dr^2/B(r)+r^2 dOmega^2,
N>0, B>0, ell=ln N, N in C3, B in C2.                 (2)
```

All statements below concern intervals where the displayed denominators are
nonzero. This excludes neither every solution of the candidate nor every
vacuum metric: it defines the identifiable chart. Horizons, the center,
turning points and other charts need separate treatment. The exact theorem
uses functions on the interval, not a finite list of measured point values.

## Metric equations and material consistency

Write the three mixed Einstein components as

```text
Gt=(B-1)/r^2+B'/r,
Gr=(B-1)/r^2+2B ell'/r,
Ga=B(ell''+ell'^2+ell'/r)+(B'/2)(ell'+1/r),
R=-(Gt+Gr+2Ga).                                      (3)
```

The metric variation of (1), with the kinetic normalization as written, is

```text
F G_mu_nu = 2Z z_,mu z_,nu - g_mu_nu[Z(dz)^2+V]
            +nabla_mu nabla_nu F-g_mu_nu Box F.       (4)
```

For comparison, if a static radial material tensor is allowed, the stresses
required by the metric and scalar are exactly

```text
rho = -F Gt-B Z z'^2-V-B F''-(B'/2+2B/r)F',
pr  =  F Gr-B Z z'^2+V+B(ell'+2/r)F',
pt  =  F Ga+B Z z'^2+V+B F''+(B'/2+B ell'+B/r)F'.     (5)
```

With additional static radial x,y fields, replace Z z'^2 by the full radial
kinetic density and V by the full potential. Equation (5) constructs the
stress that would be needed. It does not construct a material action, prove
an equation of state or show that the material is observed. In particular,

```text
pr'+ell'(rho+pr)+2(pr-pt)/r = -sum_A E_A phi_A',      (6)
```

where E_A is the scalar action variation divided by sqrt(-g). A conserved
reconstructed material tensor checks one contraction of the scalar equations.
For several moving scalar fields it is insufficient to check every equation.
No pressure-isotropy assumption is used in the vacuum inverse below.

## Potential-free inverse and kinetic parameter

Define quantities using the metric alone:

```text
D=B(1/r-ell'),                   D != 0,
u=(Ga-Gt)/D,                     u != 0,
H=Gr-Gt-B(u'+u^2)-(B'/2-B ell')u, H > 0,
j=B u^2/(2H).                                       (7)
```

Here u is a new geometric logarithmic derivative, not the old Einstein-frame
scalar coordinate. The angular-minus-time equation (4) gives F'/F=u.
Put Y=z² and X=s+Y. The radial-minus-time equation then gives

```text
H=B X u^2/(2 lambda Y),
j=lambda Y/(s+Y),
Y=s j/(lambda-j), X=s lambda/(lambda-j).             (8)
```

Thus any admitted solution has 0<j<lambda. The algebraic profile alone is not
sufficient: F'/F=u must still hold. Since s and lambda are constants, this
condition is equivalent to

```text
j'=u(lambda-j),
j(r)=lambda+[j(r0)-lambda] exp[-integral_r0^r u ds].  (9)
```

Although the differential form differentiates the metric once more, the
integral form only requires the quantities in (7). Let I_ab be the integral
of u between distinct radii ra,rb and E_ab=exp(-I_ab). On the connected
u!=0 chart, u has fixed sign, so I_ab!=0. The kinetic parameter is uniquely
fixed by

```text
lambda=(j(rb)-E_ab j(ra))/(1-E_ab),
k=[1-2/sqrt(1+3lambda)]/3.                           (10)
```

The candidate requires lambda>1. This is equivalent to 0<k<1/3; the mapping
is one-to-one because a=(1+2k-3k²)/4 increases from 1/4 to 1/3 on that
interval. Substituting k fixes s, and (8) fixes positive z. The entire
interval must satisfy (9), not just the pair used in (10). No scalar boundary
value, action normalization f0 or density-minimum selector enters this inverse.

## Potential reconstruction and local completeness

The time equation yields

```text
W=V/F=-Gt-H/2-B(u'+u^2)-(B'/2+2B/r)u,
P=V/f0=(s+Y)W,
A(Y)=3(s+Y^2), C(Y)=Y^2(ln Y)^2/(4a),
P(r)=Hv^2 A(Y(r))+(Hv^2 nu) C(Y(r)).                 (11)
```

The factor 1/4 in C comes from ln z=(ln Y)/2. At two radii r1,r2, let
Delta=A1 C2-A2 C1. If Delta!=0, then

```text
Hv^2=(P1 C2-P2 C1)/Delta,
Hv^2 nu=(A1 P2-A2 P1)/Delta.                         (12)
```

Both recovered coefficients must be positive. Equation (11) must subsequently
hold across the interval. Two fitted values do not test a two-coefficient
potential. When Y>1 and varies, C/A is strictly increasing with Y, so distinct
Y values give Delta!=0. In other ranges retain the explicit determinant test.
An inferred potential outside the traversed scalar range remains undetermined.

Conversely, suppose an exact metric satisfying (2),(7) yields one constant
lambda>1 satisfying (9) everywhere, 0<j<lambda everywhere, and positive
coefficients (12) that satisfy (11) everywhere. Construct s,k,z by (8),(10).
The integral identity supplies X'/X=u and C2 regularity of z. The angular-time
and radial-time differences of (4) then hold by (7),(8); (11) supplies its time
equation. Hence every independent metric equation holds. The radial Bianchi
identity gives E_z z'=0. Since z'=u(s+z²)/(2z)!=0, the scalar equation

```text
E_z=2Z Box z+f0 z R-V_z=0                            (13)
```

also holds. The transverse equations vanish by the stated sector consistency.
This proves local solution membership in the full candidate's radial vacuum
sector. It proves neither a global completion nor a unique physical history,
stable environment, matter realization, or selection of that sector.

## Degeneracies and changed premises

Constant z=1 with B=1-2M/r-Hv²r² and N² proportional to B satisfies the actual
positive-Hv candidate for every allowed k and nu, on any interval B>0.
Here F=f0(s+1), V=3Hv² F, R=12Hv² and V_z(1)=12f0 Hv², so (4),(13) hold.
The metric may vary, but u=H=0 and j is undefined. This is a counterexample
to an unqualified claim that a nonconstant metric fixes the scalar parameters.
The inverse explicitly refuses this branch.

Pointwise profile reconstruction without (9) also fails. For N=1,B=2/3,
one gets u=1/(2r), H=1/(6r²), j=1/2. At fixed lambda=2, (8) gives the
constant Y=s/3, whose logarithmic derivative cannot equal u. This analytic
failure is not evidence against all static scalar solutions.

For static radial transverse fields with positive kinetic density K_perp,
the measured H instead contains an additional 2B K_perp/F. For a fixed
candidate lambda,s this yields only

```text
z^2 >= s j/(lambda-j),                              (14)
```

on the same positive chart. Equality at one point does not force transverse
coordinates to vanish. Neither (9) nor the lambda reconstruction is then
guaranteed. Likewise nonzero material rho+pt changes the angular-time equation,
and rho+pr changes the radial-time equation. These are live alternatives, not
theories ruled out by the single-sector inverse. D=0 and isolated u=0 points
require continuation or another chart; no general failure theorem is asserted.
Material with rho=-pr=-pt cancels from both null differences while changing
the inferred potential. Thus those differences cannot establish material
vacuum; trace-free material is also not sufficient.

## Observation requirements and finite-error condition

The pointwise inverse uses N through its third radial derivative and B through its
second. A constant clock normalization cancels. For the earlier ideal static
radial clock/ranging construction, f=N/N0, g=tau'>0 and B=4/(f²g²).
The present inverse therefore requires derivatives through f''' and tau''',
an independently calibrated areal-radius coordinate and coverage on an
interval. That ideal measurement identification and its environmental and
instrument errors must be justified separately. Cassini count records used
elsewhere in the campaign do not supply this static metric simply by existing.

Finite point values alone do not control these derivatives: a smooth
perturbation vanishing at every finite sampled radius can change derivatives
between samples. No observational precision is assigned by this theorem.
The following useful scalar error estimate is conditional on already having
error bounds for the reduced quantities. Suppose estimates ja_hat,jb_hat,I_hat
have absolute errors ea,eb,eI. Set

```text
Ehat=exp(-I_hat), eE=Ehat[exp(eI)-1],
d=abs(1-Ehat)-eE>0,
lambda_hat=(jb_hat-Ehat ja_hat)/(1-Ehat).
abs(lambda-lambda_hat)
 <= [eb+(Ehat+eE)ea+abs(lambda_hat-ja_hat)eE]/d.       (15)
```

Subtract the two exact ratio equations to obtain
delta_lambda=[delta_jb-E delta_ja+(lambda_hat-ja_hat)delta_E]/(1-E);
the displayed bound follows. Correlations need not vanish. Failure of d>0
is inconclusive. Error propagation from instruments to metric derivatives and
from those to H,j, plus potential-coefficient conditioning, remain unsupplied.

Rescaling all calibrated radii by L leaves k,nu and z unchanged while the
reconstructed Hv² scales as L^-2. The overall f0 and Q remain absent from the
vacuum equations. This is a conditional reconstruction of parameters in units
of the radius calibration, not an absolute scale derivation from the axioms
or a measurement of Newton's constant.

## An integral alternative with fewer direct derivative inputs

The same inverse can be formulated without direct measurements of u', N'''
or B''. Keep the qualitative regularity in (2); the following statement reduces
the quantities evaluated, not the regularity class of the exact theorem. Set
q=1/r-ell' and choose any reference r0 in the interval. Integrating (7) gives

```text
u=-q'/q-B'/(2B)-2/r-ell'+1/(B r^2 q),
h(r)=[q(r0)sqrt(B(r0))r0^2 N(r0)]/[q(r)sqrt(B(r))r^2 N(r)]
     * exp integral_r0^r [1/(B(t)t^2 q(t))]dt.        (16)
```

Here h=F/F(r0)>0 and h(r0)=1. The fixed sign of q makes its ratio positive.
The normalized shape uses N,N',B and an integral. Normalizing h does not
choose the scalar amplitude: that unknown is eta=s/X(r0)>0. A candidate has
Y=s(h/eta-1)>0 pointwise. For the integral inverse restrict to 0<eta<inf h,
which supplies a uniform positive margin. This is automatic on a closed
subannulus of a positive solution, but can exclude an open-annulus boundary
limit with eta=inf h. The geometric u needed next uses N'' and B'.

Let w be a nonnegative, nonzero C1 weight with compact support in the interval.
Define

```text
K[w]=integral {w[2ell'/r-B'/(Br)-u^2-(B'/(2B)-ell')u]+w'u}dr,
A[w;eta]=integral w u^2 h/(h-eta) dr.
K[w]=A[w;eta]/(2lambda).                            (17)
```

This is the radial-minus-time equation integrated by parts; its evaluation
needs no u'. Choose two such weights with strictly separated, ordered h
ranges, max h(supp w1)<min h(supp w2). This is possible on a nonempty u!=0
interval because h is strictly monotone. Both A values are positive, and

```text
d log A[w;eta]/deta
 = weighted mean of 1/(h-eta),
d log(A[w1;eta]/A[w2;eta])/deta > 0.                 (18)
```

The positive averaging measure is proportional to w u² h/(h-eta). Thus
K[w1]/K[w2]=A[w1;eta]/A[w2;eta] has at most one admissible eta. Positivity
of K, an actual bracket or range test, and existence of that root remain
requirements. The ratio need not diverge at eta=inf h because the compact
weights may avoid the minimum of h. Recover lambda=A[w1;eta]/(2K[w1]),
require lambda>1, then recover k,s and Y as above. Two moment fits alone do
not prove the radial equation on the interval.

For X=s h/eta the potential equation has the weak form

```text
T[w]=integral X{-w(Gt+Gr)/2+(B u/2)w'
               +w[B'/4-B ell'/2-2B/r]u}dr,
T[w]=Hv^2 integral w*3(s+Y^2)dr
     +(Hv^2 nu) integral w*Y^2(ln Y)^2/(4a)dr.       (19)
```

To verify it, add the derivative of w X B u/2 to w X W in (11), use X'=uX,
and discard the zero compact-support boundary term. Two weights with a
nonzero integrated determinant determine the positive potential coefficients.
If Y>1 on their strictly ordered ranges, monotonic C(Y)/A(Y) gives a nonzero
determinant; otherwise check it explicitly. Later weights test these fitted
coefficients without refitting.

Equations (17),(19) for **every** compact test weight recover the original
continuous radial/time identities and hence the local solution-membership
proof. Finitely many fitted or checked weights are only partial constraints.
The weights are a chosen measurement design, not an action or state selector.
This integral route replaces the highest direct derivatives by finite-window
integrals and a nonlinear amplitude fit. It still requires N'' and B',
equivalently f'' and tau'' under the stated clock/ranging construction, as
well as calibrated intervals, errors, quadrature and conditioning. Those
physical suppliers, material vacuum and field sector remain unestablished.

## Reproduction, discrimination and remaining work

The helper independently constructs the four-dimensional connection and Ricci
tensor, checks the metric equations and radial conservation identity, and
tests the inverse with three locally integrated coupled vacuum solutions on
1<=r<=1.8. Two use the actual supplied potential with (k,Hv,nu)=(.1,.03,1.2)
and (.22,.05,.7). The third adds the explicit alternative
0.15 f0 Hv²(z²-1)³ to that potential. Its original equations are also checked.
All initial data and parameters are synthetic development choices, stored
with results; the inverse routine receives only metric derivatives.

Each profile has 601 rows. Rows 0 and 200 calibrate (10),(12), with the u
integral through row 200; the subsequent 400 rows check consistency without
refitting. The altered potential fits both calibration values but leaves an
out-of-calibration potential residual about 5.04e-6. This demonstrates a
discriminator; it is not an empirical rejection of that alternative. The two
candidate profiles recover k within 3e-13, nu within 6e-11 and z² within
1.1e-11 in the first execution. Original field-equation residuals are below
8e-16. These floating-point residuals are not rigorous error enclosures.

The separate weak helper evaluates (16)--(19) on the same three supplied
synthetic families. Its readout callback returns only r,B,B',ell,ell',ell'';
no B'' or ell''' enters the weak inverse. Two fixed compact polynomial windows
calibrate, and two later windows test. In the first working execution the
candidate k errors are at most1.04e-9 and scalar Y errors at most2.23e-8;
the changed potential leaves later weighted residuals up to3.54e-6. These
weaker numerical accuracies and potential matrix condition numbers up to3435
are retained. No observational precision or complete-interval numerical
certificate is inferred from four windows. The independent Einstein-frame
fixture checks the pointwise inverse through a separate implementation;
the weak extension has its own separately labeled mathematical checks.

Run `python3 scripts/scalar_vacuum_metric_check.py`; the source-bound cache and
paired outputs identify the exact final inputs. Preserved independent
derivations, synthetic results and real code-control failures belong to the
companion [work history](../.claude/science/physics-loops/observations-backward-24h-20261014/material_metric_consistency/HANDOFF.md)
and [scope checklist](../.claude/science/physics-loops/observations-backward-24h-20261014/material_metric_consistency/NO_GO_DISCIPLINE_CHECKLIST.md).

The actual next empirical obligation is a calibrated physical metric and
vacuum/sector test, including derivative uncertainties and independent
prediction intervals. The actual next theory obligation is selecting or
deriving the action and sector while retaining the successful conditional
inverse. No observed arrays are newly opened, no independent empirical test
is claimed, and no full theory of everything or formal audit status follows.

## Proof obligations, imports and review scope

The obligation chain is: supplied candidate action and consistent sector;
direct variation and metric curvature (3)--(6); potential-free algebra and
integrability (7)--(10); potential reconstruction (11),(12); and Bianchi
completeness (13). The mathematical steps are derived here. The action and
physical metric identification remain conditional source premises. The
independent derivation uses a direct four-dimensional Ricci/Hessian calculation
and a different inverse variable. Its initial fixed-parameter result was
frozen before author-source exposure; its later parameter/error comparison is
explicitly post-exposure. A source comparison with prior inverse notes is
separate from numerical checking.

No unproved mathematical lemma is being substituted for the exact local
theorem. The strongest missing physical obligation is to supply a calibrated
metric interval and establish the material and field-sector conditions from
observations. That is stronger than evaluating this inverse and is still open.
An overall units primitive supplies no such data or dimensionless parameter.
The actual fitted/reconstructed values, their errors and their independent
tests require a future empirical protocol.

Two real implementation findings were preserved: the first helper accepted
negative recovered nu and nonfinite error inputs. Explicit domain guards and
regression controls repair them; the exact proof already required positivity
and finite errors. The main three long profiles are separate from a short
negative-nu domain-refusal fixture. All executions are synthetic. Final
source-bound reports, mutation outcomes and source identities are recorded in
the companion handoff. No preceding published science is removed. A future
combined landing must include or first land the declared stacked action/metric
parent and rerun the integrated pipeline; no such landing or audit is claimed.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Ambient boundary and full material/metric consistency remain supplied in the physical-metric ceiling."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Supply a calibrated metric interval and test vacuum/sector and potential consistency against independent measurements."
conditional_surface_status: "Local nonlinear radial-vacuum inverse and solution-membership theorem on the stated regular chart."
hypothetical_axiom_status: null
admitted_observation_status: "No new observed arrays or independent empirical test; synthetic development and out-of-calibration controls only."
claim_type_reason: "Exact implication within a supplied action/sector and calibrated metric, with explicit domain and interval tests."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
