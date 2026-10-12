# Independent static-action and candidate-validator check

2026-10-12. Narrow mathematical/source review with synthetic controls only.
This is not a formal audit, actual field calculation, empirical fit, or
validation of the pending sphere-classification work. The scientific author
and all author files remain unchanged by this reviewer.

## Disposition and pinned sources

No material variational, primitive, convexity, or numerical-gate implementation
error was found in the pinned subjects. One mathematical qualification and one
downstream interpretation limit are recorded below. Actual candidate-specific
field evidence is pending; passing synthetic controls does not supply it.

| Source | SHA-256 |
| --- | --- |
| DIRECT_STATIC_ACTION.md | `8ad17721005d193be2c37423fc4682ae14c4c765436b6aa30bcd0bece5005e65` |
| direct_validate_inverse_fields.py | `aa1a07fd5553c119160772ee6ca69fbc698f31010f4f0df3f692d23817d50dc1` |

Both snapshots are stored beside this report. The runtime manifest also pins
the previously reviewed protocol, operator, fit, solar basis, and field solver.
Their bytes remained unchanged through this synthetic check. In particular the
operator is `fe1d5256bb1d867602b4c5c6f68a7c683db1f3ea485d9d85c572b3f8ffccfadb`
and the field solver is
`701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00`.

## Variations, primitive, and convexity

Independent integration by parts gives

    delta_Phi S = integral [Delta Phi_N/(4 pi G) - rho] delta Phi,
    delta_Phi_N S = integral [Delta Phi - div(N grad Phi_N)] delta Phi_N/(4 pi G).

Thus the mixed-gradient and matter-coupling signs produce the two stated
Poisson equations. Fixed endpoint or compactly supported variations remove
the boundary term. Smooth test variations preserve stipulated singular-source
coefficients; sheet and point-source equations retain their weak interpretation.
The static functional has energy units, as expected before a time integration.
`F` and each `B` have acceleration-squared units.

For a single ramp, independently integrate `b(sqrt(u))` from zero to s. Below
`L^2` this is s. Between the knots, the antiderivative is
`[u log(H/sqrt(u))+u/2]/log(H/L)`; including the lower constant branch leaves
the document's exact expression

    B(s) = [s log(H/sqrt(s)) + (s-L^2)/2]/log(H/L).

At `H^2` it reaches `(H^2-L^2)/(2 log(H/L))`. The values and first derivatives
match at both joins. This supplies the stated first variation without a new
surface delta on a response-knot level set. It does not assert a classical
second derivative at every knot.

Off the response knots, differentiating with respect to U gives

    grad_U F(|U|^2) = 2 N(A) U,
    Hessian_U F = 2 N(A) I + 2 N'(A) U U^T/A.

The transverse eigenvalues are `2N` and the longitudinal eigenvalue is
`2[N+A N']`. Their nonnegativity reduces to exactly the previously checked
D inequalities at each upper interval edge. The gradient is continuous at
knots, and its one-sided Hessians are positive semidefinite for D. Restricting
the function to any straight line then gives nondecreasing one-dimensional
derivative across both smooth pieces and joins, establishing global convexity.
At U=0, the low branch is quadratic with Hessian `2(1+sum w)I`.

The displayed classical Hessian/Jacobian formula should explicitly say
**off knots**; at a nonzero-weight knot the classical Hessian generally does
not exist. One-sided limits and the continuous gradient are sufficient for
the stated convexity claim. The author has acknowledged this qualification
and plans a separately pinned wording fix. No change to the D constraint or
primitive is required.

This convexity belongs to the constitutive term. The full mixed-gradient
functional has Hessian blocks proportional to `[0,-2I;-2I,H_F]` and is not a
jointly positive quadratic form even when `H_F` is positive. The note correctly
does not claim Hamiltonian positivity, relativistic ghost freedom, causal
propagation, or quantum completion from the static result.

## Boundary extension and numerical obligations

The extension constructs new radii strictly below the old minimum and above
the old maximum, extending each endpoint by a factor of two. It concatenates
the old radial array and both old vector arrays unchanged between those new
pieces. Angular nodes/weights, scored radii, midplane field values, and angular
mode cutoff are retained. The extra source evaluation uses the same frozen
baryonic construction and mass-to-light ratio at Hankel order 8192, only on
the new edge nodes. The old interior does not undergo a new Hankel evaluation.
The cached extension is tied to the base-cache hash and checks its own hash.

Consequently this candidate-specific boundary comparison preserves the
interior integrand and quadrature nodes. It measures the effect of the added
inner/outer domain at the chosen edge evaluation accuracy. It is not a
uniform interior Hankel-order test, a separated tail error bound, or interval
certification. Those stronger claims are not made by the code.

For every successful non-null fit candidate, the main path passes the original
full-precision weights to the base, doubled radial/angular/mode grid, and
extended-domain projections. It compares direct base forces against the exact
Newtonian-baseline matrix force, checks positive radial forces in all four
representations, and imposes maxima over all scored radii:

- direct versus matrix: `<=0.003`, using the matrix force as denominator;
- radial/angular refinement: `<=0.005`, using base direct force;
- candidate-specific boundary extension: `<=0.003`, using base direct force.

These limits are consistent with the frozen projection/refinement/boundary
obligations. The candidate pass requires every original galaxy to pass.
Failed candidates and their force arrays remain in the receipts. No extra
velocity data are read by this validator.

A numerical-field pass does **not** establish that the exact LP rectangle
allowance survives projection at precisely the fitted LP t. This validator
does not recompute rectangle violations with the final direct fields. The
author has acknowledged that separate obligation and will recompute the
required allowance from direct/refined/boundary forces while retaining LP t
as a grid optimum. This is a downstream interpretation limit, not a failure
of the numerical gates implemented here.

## Independent synthetic evidence

`check_static_and_validation.py` uses fresh scalar quadrature and finite
variations for the action and literal transcription of the proposed primitive.
It executes pinned validator bytes as subjects. The boundary test substitutes
a closed-form synthetic vector source for RingField and uses only tiny local
fixture files. The main-path test substitutes known force arrays and geometry
receipts; it does not exercise or claim the actual galaxy solver accuracy.

- Eight primitive values agree with independently integrated ramps to
  `3.56e-15` absolute error. A physical-scale rescaling verifies acceleration-
  squared homogeneity. One-sided first derivatives agree at both knots.
- A one-dimensional fixed-endpoint variation crossing a ramp knot gives
  absolute first-variation errors `2.08e-13` for Phi and `2.28e-12` for Phi_N.
  The manufactured matter density makes the sign of the source term testable.
- The vector Hessian agrees with direct second differences of the scalar
  primitive to `1.22e-8`. Its three eigenvalues agree with the transverse and
  longitudinal formulas. A strict-D two-ramp example passes 250 deterministic
  Jensen probes across both knots and tails. An allowed M example has negative
  longitudinal eigenvalue `-6.21217`, confirming why M alone is insufficient.
- An irregular five-radius synthetic grid is extended from `[.5,4]` to
  `[.25,8]`. Every original radius, field-vector value, and unchanged geometry
  array is preserved bit-for-bit. Only four added radii are evaluated. Cache
  reuse makes no new source call; altering the parent cache is rejected.
- Eight mock fit candidates exercise the actual validator main path. Only the
  clean candidate passes. Separate matrix, refinement, boundary, negative-force,
  nonfinite-force, one-galaxy-only, and refined-negative-force failures all
  prevent an aggregate pass. Infeasible/null fits are excluded. All 72 projection
  calls receive weight bytes identical to the input fit fixture, and the
  doubled-grid requests are verified.

The check ran in 0.014 seconds in Python, with peak resident memory 79,921,152
bytes and one-thread settings. No empirical inputs, real galaxy fields, fits,
author edits, commits, pushes, or formal audit operations were performed.
The runtime receipt pins source snapshots, this report, the executable fixture,
and its successful result/log.
