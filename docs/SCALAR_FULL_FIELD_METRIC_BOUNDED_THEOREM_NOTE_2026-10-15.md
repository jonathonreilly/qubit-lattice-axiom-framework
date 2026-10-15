# A necessary metric test with all three scalar fields active

Claim type: bounded_theorem.
Actual current surface status: conditional-support.
Scientific author: /root.
Primary runner: [scalar_full_field_metric_check.py](../scripts/scalar_full_field_metric_check.py).
Executable controls: [scalar_full_field_metric.py](../scripts/scalar_full_field_metric.py).

The supplied revised scalar action implies a necessary test of a static radial
vacuum metric without setting either transverse scalar to zero. Positive
transverse kinetic and potential terms constrain the metric, and determine
the two squared transverse amplitudes for fixed trial parameters and field
normalization. This is an extension of the
[single-sector inverse](SCALAR_VACUUM_METRIC_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md),
not a unique full-field inverse or a sufficient solution test. No actual
measured metric or new observation array is used.

## Supplied action and domain

Use the complete physical Jordan action in the
[environment note](SCALAR_PHYSICAL_CURVATURE_ENVIRONMENT_BOUNDED_THEOREM_NOTE_2026-10-15.md),
signature (-+++), and its natural-unit convention. Divide by the constant
positive f0=Q/(1+s). The action density is

```text
L/f0 = X R/2 - (dz)^2/lambda - qx (dx)^2 - qy (dy)^2 - P,
X=s+z^2, z>0, 0<k<1/3, Hv>0, nu>0,
a=(1-k)(1+3k)/4, lambda=a/(1-3a), s=(1+k)/[k(1-3k)],
Dperp=1+2(1+k)(x^2+y^2)/3,
qx=(1+s)z^2 4k/(9Dperp), qy=(1+s)z^2 k/(3Dperp),
P=P0+Ax x^2+Ay y^2,
P0=Hv^2[3(s+z^4)+(nu/a)z^4(ln z)^2],
Ax=Hv^2 k X^2 z^rx/(1+s), Ay=2Hv^2 k X^2 z^ry/[3(1+s)],
rx=(1-k)/a, ry=(1+k)/a.                                      (1)
```

These functions and parameters are candidate inputs. This calculation does
not derive their selection. The fields are classical static radial fields,
and there is no material stress tensor on the interval. This still allows
nonzero scalar stress. On a connected finite annulus with calibrated physical
areal radius, take

```text
ds^2=-N(r)^2 dt^2+dr^2/B(r)+r^2 dOmega^2,
N>0, B>0, ell=ln N, N in C3, B in C2.                         (2)
```

An actual candidate has C2 scalar fields. Horizons, the center, nonradial or
time-dependent fields and material environments are outside this statement.
The quantities below use exact functions, not a finite collection of noisy
points. No error envelope for an observed metric is supplied.

## Metric reconstruction with an explicit unknown amplitude

The mixed Einstein components and Ricci scalar are

```text
Gt=(B-1)/r^2+B'/r,
Gr=(B-1)/r^2+2B ell'/r,
Ga=B(ell''+ell'^2+ell'/r)+(B'/2)(ell'+1/r),
R=-(Gt+Gr+2Ga).                                               (3)
```

Define the physical kinetic density divided by f0,
K=B[z'^2/lambda+qx x'^2+qy y'^2]. Direct metric variation gives

```text
X Gt=-K-P-B X''-(B'/2+2B/r)X',
X Gr= K-P-B(ell'+2/r)X',
X Ga=-K-P-B X''-(B'/2+B ell'+B/r)X'.                           (4)
```

Subtracting the time equation from the angular equation cancels every kinetic
term and the complete potential. On a chart d=B(1/r-ell')!=0 it gives

```text
u=(Ga-Gt)/d=X'/X,
X_C(r)=C exp(integral from r0 to r of u(t)dt),
z_C=sqrt(X_C-s),  C>0, X_C>s throughout the chart.              (5)
```

C=F(r0)/f0 remains an unknown trial field amplitude. Unlike the one-field
inverse, this construction does not infer k or C uniquely. Neither u!=0 nor
division by H is required here. Absolute Q cancels from these vacuum equations.

Set

```text
H=Gr-Gt-B(u'+u^2)-(B'/2-B ell')u,
W=-Gt-H/2-B(u'+u^2)-(B'/2+2B/r)u,
K=X H/2, P_rec=X W,
T=X H/2-B z'^2/lambda.                                       (6)
```

The last two identities follow from the radial-time difference and the time
equation. In an actual solution T=B(qx x'^2+qy y'^2)>=0. The factor B belongs
to T; confusing T with the coordinate kinetic coefficient changes the scalar
equation. Positivity is conditional on the parameter domain in (1).

## Full-field potential envelope and conditional squares

For fixed trial k,Hv,nu,C define

```text
Lz=B z''+(B'/2+B ell'+2B/r)z',
Delta=P_rec-P0,
E=2Lz/lambda+zR-2T/z-P0,z,
lx=4z/X+rx/z, ly=4z/X+ry/z, ly-lx=2k/(az)>0.                  (7)
```

Because partial_z qx=2qx/z and likewise for qy, the full z equation is
E=Ax,z x^2+Ay,z y^2. The coefficients satisfy Ax,z=lx Ax and Ay,z=ly Ay.
Putting Ux=Ax x^2 and Uy=Ay y^2 therefore yields

```text
Delta=Ux+Uy, E=lx Ux+ly Uy, Ux>=0, Uy>=0.
Hence T>=0, Delta>=0, lx Delta<=E<=ly Delta.                    (8)
```

This proves the necessary metric compatibility test. Its two envelope
remainders are exactly (ly-lx)Uy and (ly-lx)Ux. All z>0 are allowed; the exact
base-potential derivative

```text
P0,z=Hv^2 z^3[12+(nu/a)(4ln^2z+2ln z)]
```

is kept, including its possibly negative regulator contribution below z=1.
For computation, an equivalent expression is

```text
E=LX/(lambda z)+zR-XH/z-P0,z,
LX=X[B(u'+u^2)+(B'/2+B ell'+2B/r)u].                           (9)
```

It follows by substituting X''=2z'^2+2zz'' into (7); the z'^2 terms cancel.
Equations (3)--(9) use N''' and B''. They do not reduce or calibrate those
measurement requirements. A constant rescaling of N leaves them unchanged.

Conversely, only at the level of local potential algebra, (8) yields

```text
Ux=(ly Delta-E)/(ly-lx), Uy=(E-lx Delta)/(ly-lx),
x^2=Ux/Ax, y^2=Uy/Ay.                                       (10)
```

There is no division by Delta. When Delta=0 both potential shares and E
vanish. Equality at an envelope endpoint sets one coordinate to zero at that
radius, not its derivative. On an entire open interval Delta=0 forces x=y=0
identically and hence T=0. A failed inequality excludes the specified trial
from this supplied static radial vacuum class. It does not reject every trial
or a different action or material environment.

## Why this is not a solution-membership theorem

Let xi=x^2 and eta=y^2 from (10). On an interval where both are positive and
differentiable, an actual solution additionally requires

```text
T=B(1+s)kz^2/[1+2(1+k)(xi+eta)/3]
  * [xi'^2/(9xi)+eta'^2/(12eta)].                             (11)
```

This follows from x'^2=xi'^2/(4xi) and y'^2=eta'^2/(4eta). At zeros an actual
smooth signed square-root continuation is needed; a 0/0 limit can hide a
nonzero derivative. Pointwise positivity does not prove such continuation.
The baseline metric regularity need not give the additional differentiability
needed for (11), much less both remaining scalar equations.

Even when the metric and z equations and kinetic consistency hold, the two
transverse Euler--Lagrange equations still require individual verification:

```text
Ex/f0=2qx Lx+2B qx' x'-B(partial_x qx)x'^2
      -B(partial_x qy)y'^2-2Ax x=0,
Ey/f0=2qy Ly+2B qy' y'-B(partial_y qx)x'^2
      -B(partial_y qy)y'^2-2Ay y=0.                            (12)
```

Here qx',qy' are total radial derivatives, including their z dependence.
Bianchi supplies only Ez z'+Ex x'+Ey y'=0. With Ez=0 it is one contraction
of two remaining equations, not proof of both. Constant nonzero transverse
coordinates also have zero transverse kinetic density and positive potential;
kinetic equality alone does not select the zero sector. Signs, global
completion, initial preparation and stability remain open.

## Checks, provenance and observational scope

The working protocol fixes two synthetic local full-field states before
execution. The author implements a separate Einstein-areal initial-value
system with gE=X gJ. Its field metric is hzz=2/(lambda X)+6z^2/X^2,
hxx=2qx/X, hyy=2qy/X and potential U=P/X^2. A third-order local Taylor jet
is obtained by differentiating that system, then transformed to Jordan areal
radius. These are regular local ODE jets, not integrated global spacetimes.
The inverse receives metric jets, trial k,Hv,nu and X; it does not receive
x,y or their derivatives.

The controls check all three original Jordan metric equations and all three
original scalar equations, reconstruct x^2,y^2,T,z',z'', and check a strictly
interior positive envelope at each point. The initial working execution has
24 passes and zero failures at 50 decimal digits with fixed scaled tolerance
1e-35. Floating-point residuals are diagnostics, not rigorous enclosures.
Parameters, initial state and metric are synthetic development inputs; the
trial normalization is supplied, not recovered from observations.

A focused independent derivation was frozen before exposure to the author's
new derivation or code. It gives 34 exact symbolic/rational controls of the
metric identities, envelope, squares and kinetic consistency, including
zero/negative-share and wrong-normalization witnesses. That reviewer had
previously seen the inherited action and one-field metric formulas. Its
rational example is a potential-algebra fixture, not another spacetime.
Later final-source comparison is separately recorded. No empirical validation
is inferred from either set of controls.

Run `python3 scripts/scalar_full_field_metric_check.py`. Exact source identities,
execution limits, failures, mutation outcomes and review scope are in the
companion [handoff](../.claude/science/physics-loops/observations-backward-24h-20261014/full_field_metric/HANDOFF.md).
This coherent extension leaves the published one-field proof and its evidence
unchanged. No global novelty claim is made for the algebraic elimination.

The observation-first next obligation is to supply a calibrated physical
metric interval, derivative errors and material-vacuum justification, then
test trial ranges without selecting them from the same withheld measurements.
This result removes x=y=0 only for the necessary compatibility test. It does
not derive the candidate action, scales, initial state, C, k,Hv,nu, actual
environment or measurement identification, and it does not establish a TOE.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "The single-field vacuum inverse supplies x=y=0; the full-field and calibrated metric suppliers remain open."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Supply calibrated metric/error and material-vacuum inputs; test candidate trials and both transverse equations."
conditional_surface_status: "Necessary full-three-field radial vacuum metric envelope and algebraic squared amplitudes for supplied trials."
hypothetical_axiom_status: null
admitted_observation_status: "No new observed arrays or independent empirical test; two synthetic local solution jets."
proposal_allowed: false
proposal_allowed_reason: "Action, trial parameters and amplitude, physical calibration and solution completion remain conditional."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
