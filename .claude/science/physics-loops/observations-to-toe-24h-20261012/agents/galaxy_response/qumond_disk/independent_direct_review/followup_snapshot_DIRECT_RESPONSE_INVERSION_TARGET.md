# Direct-author next target: reconstruct the acceleration response

2026-10-12, after takeover by the user chat. This is a mathematical reduction
and a proposed next test, not a completed empirical result. The exponential
response's published-data tension was already exposed. A response family
chosen now is model development; none of the old data becomes a blind test.

The next observation-driven question is whether the *shape* of a shared
gravity response can satisfy the galaxy and solar constraints. It is too
early to infer a failure of that whole mechanism from one interpolation
formula, especially before replacing the algebraic galaxy approximation.
The exact field calculation remains the immediate prerequisite.

## Remove an arbitrary acceleration-coordinate choice

Let A be the Newtonian acceleration magnitude in SI units, and let N(A) be a
supplied nonincreasing enhancement, approaching one at high A. A parameter
a0 is merely a choice of argument when writing N(A)=nu(A/a0); it need not
be an independently meaningful fitted parameter for an arbitrary function.
Under the existing point-Sun, uniform external-field QUMOND boundary problem,
the inherited kernel formula is

    Q2 = (9/8) g_Ne^(3/2)/sqrt(G M_sun)
         integral_0^infinity W(A/g_Ne) [-N'(A)] dA.

This follows by substituting q=A/a0 and eta=g_Ne/a0 into the existing
dimensionless expression. All powers of a0 cancel. W is dimensionless;
g_Ne^(3/2)/sqrt(G M_sun) has units s^-2. The derivative-weighted integral
is dimensionless. No numerical acceleration scale has been inserted into
this dimensional reconstruction.

For an absolutely continuous N with the inherited convergence bounds, define
dm(A)=-N'(A)dA. Positivity makes the solar response a positive linear
functional of this measure. A fixed decline N(A1)-N(A2) supplies the earlier
interval lower bound multiplied by min W on that interval. Conversely, the
value at one acceleration alone gives no strictly positive lower bound if
the permitted location of its decline is unbounded: W tends to zero at
both endpoints. The acceleration interval on which observations require a
decline is therefore load-bearing, not merely the existence of a boost.

## The full galaxy equation is also linear in a fixed response

For a fixed baryonic source and fixed boundary conditions, U=grad(Phi_N) is
known. Write P for the Poisson/longitudinal projection used in the direct
disk derivation. The actual galaxy gradient is P[N(|U|)U]. Although the
source-to-field theory is nonlinear in mass, its map from N to the field is
linear when U is held fixed. Thus for fixed basis responses b_j and

    N(A)=1+sum_j w_j b_j(A),

each radial prediction has the form

    g_i = g_Newton,i + sum_j w_j K_ij,
    K_ij = radial component of P[b_j(|U|)U] at measurement i.

This uses the full disk projection, not b_j(g_Newton,i)g_Newton,i. The
coefficients K_ij are not assumed positive: disk geometry and the nonlocal
projection can change a radial contribution's sign. For the same basis, the
solar observable is Q2=sum_j w_j q_j, with q_j>=0 for decreasing b_j.
Linearity alone proves this reduction; no galaxy or solar value has been fit
to demonstrate it. Its physical premises remain the chosen field equation,
shared response, matter profiles, source normalization and boundaries.

A possible declared basis uses an enhancement equal to one below A_lo,
falling linearly in log A over [A_lo,A_hi], and zero above A_hi. Nonnegative
weights guarantee monotonicity. Such basis functions are absolutely
continuous, with derivative jumps at the knots. Extending the inherited C1
kernel theorem to these functions needs an explicit dominated-convergence
or piecewise integration argument before use. A sharp step must not be
silently substituted for that regularity proof. Smooth compact transition
bases are another option.

## Prerequisites and future data roles

First finish the fixed-source full-field calculation and its independent
check. Next validate response-basis kernels against analytic source controls,
direct full-field superpositions and the positive solar integral. Source
mass-to-light changes alter U and consequently the kernels; they cannot be
treated as another fixed linear column without derivation.

Any combined response reconstruction must freeze its function family,
acceleration window, baryonic treatment, loss or compatibility rule, treatment
of solar uncertainties, and exposure accounting before its first fit. The
existing 84/19 split remains provenance rather than an unexposed validation
set. The current data are processed curves and fitted ephemeris summaries,
with incomplete nuisance covariance. Their joint use supplies a conditional
feasibility comparison, not a likelihood or a universal observational no-go.

Feasibility on a finite nonnegative basis would exhibit one candidate under
those assumptions. Infeasibility would constrain that discretized family and
its stated error/uncertainty bounds; it would not exclude every monotone
function, different matter model, field completion, or theory of gravity.
No claimed result in this target note completes quantum matter, relativistic
gravity, cosmology, or a theory of everything.
