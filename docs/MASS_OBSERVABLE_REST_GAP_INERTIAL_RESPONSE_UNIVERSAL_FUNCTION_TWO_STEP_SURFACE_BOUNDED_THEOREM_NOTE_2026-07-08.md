# Mass Observable Rest-Gap and Inertial Response Universal Function on the Two-Step Surface -- Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On the free `U = 1`, `d = 3` staggered two-step transfer
surface, with real species coefficient `m > 0` and
`E(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu))` from the d-dimensional
two-step dispersion note, this note identifies the realized one-particle mass
observable, computes its rest-gap and inertial-response readouts, and proves
that they are two readouts of one free datum through a species-independent
universal function. The result consumes the declared two-step dynamics import,
the declared on-site mass-sector import, the declared blocked-time
normalization import, and the approved realized-state primitive named below.
It narrows the Record-stiffness no-go residuals only to those declared imports;
it does not close any source-side or framework-only residual.
**Status authority:** independent audit lane only; sets no audit status.
**Primary runner:**
[`scripts/mass_observable_two_step_surface_2026_07_08.py`](../scripts/mass_observable_two_step_surface_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/mass_observable_two_step_surface_2026_07_08.txt`](../logs/runner-cache/mass_observable_two_step_surface_2026_07_08.txt)

## Why This Note Exists

The Record-stiffness context-independence no-go leaves open a separate theorem
deriving a continuous local energy/action context and a separate theorem
identifying an inertial rest-gap readout for physical matter. This note
addresses only the second item after declaring the transfer-derived
one-particle dynamics from the two-step positivity and d-dimensional dispersion
authorities.

The conditional shared-coupling template records an exact ratio-one statement
for a supplied first-order scalar kernel `E^2 = m^2 + K(p)`. The two-step
staggered surface used here has instead
`E(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu))`, so the finite-lattice-spacing
rest-gap readout and the curvature-defined inertial-response readout must be
computed on this transfer surface rather than copied from the template.

## Imports And Premises

- **I-DYN.** The real-time one-particle dynamics are
  `H_eff = -log(T_2)/(2 a_tau)` from the free staggered two-step transfer. The
  bounded authorities are the two-step positivity note for the transfer/log
  object and the d-dimensional dispersion note for the `d = 3` symbol. This is
  the same declared premise shape as the microcausality note's M2b leg, but
  that note is not an additional authority here. This narrows the no-go
  residual R1 to the declared transfer-derived, RP-positive chain; it does not
  close R1.
- **I-MASS.** The on-site mass sector has a free coefficient `m > 0` per
  species. This is the declared sector licensed by the dynamics-form
  record-preservation class whose leading terms include on-site mass. The
  value freedom of `m` is conceded as the lambda-freedom displayed by the
  Record-stiffness no-go's two-completion countermodel. The two-step positivity
  and d-dimensional dispersion notes supply the same positive-mass surface for
  the free staggered transfer.
- **I-TIME.** The blocked-time normalization is declared. The
  `kinetic_isotropy_primitive` covers the structural tick/edge footing, and
  the theorem statements below use normalization-free identities or ratios.
- **Realized-state use.** The approved `realized_state_primitive` is consumed
  pointwise for the realized kinetic branch from the realized-branch selection
  note. The staggered realization chain `AC_phi_lambda` remains an open gate,
  with expected downstream verdict `audited_conditional / dependency_not_retained`.

The imports in I-DYN, I-MASS, and I-TIME are bounded imports. They are not new
axioms and are not primitives. The only primitive consumed here is the approved
`realized_state_primitive` named above.

## Statement

On the free `U = 1`, `d = 3` two-step transfer surface, let

```text
    E(p) = arcsinh(sqrt(m^2 + sum_{mu=1}^3 sin^2 p_mu)),    m > 0.
```

**T1 - well-definedness / taste scalarity.** The one-particle forward-channel
symbol is `E(p) I_8`, scalar on the `2^3` cell space and taste-degenerate. The
mass observable of the realized one-particle sector is therefore a single
number per species, not a taste-split family.

**T2 - rest gap.** The spectral rest gap of `H_eff` is

```text
    m_gap := min_p E(p) = E(0) = arcsinh(m).
```

**T3 - gapped band projection.** For `m > 0`,
`E(p) >= arcsinh(m)` globally, and the minimum margin is attained at the
eight Dirac corners. The band projection is smooth and exponentially
localized because the denominator `E(p)` is bounded away from zero. At `m = 0`
the projection is singular exactly at the eight Dirac points. On this surface,
mass is the object that makes a persistent one-particle sector well-defined.

**T4 - inertial response coefficient.** The spectral curvature at the rest
point is

```text
    (d^2 E / d p_3^2)|_0 = 1 / (m sqrt(1 + m^2)).
```

Define the inertial-response coefficient

```text
    M_I := m sqrt(1 + m^2).
```

A companion inertial-closure theorem (separate science block) shows that `M_I`
governs packet acceleration. This note only defines and computes `M_I` as a
spectral invariant.

**T5 - universal-function identity.** The rest gap and the inertial-response
coefficient obey

```text
    M_I = (1/2) sinh(2 m_gap),
    M_I / m_gap = 1 + (2/3) m^2 + O(m^4).
```

Rest gap and inertial-response coefficient are not equal at finite lattice
spacing. They are two readouts of one free datum through a species-independent
universal function, and they coincide in the scaling window `m << 1`. This
corrects the ratio-one language of the conditional shared-coupling template:
that exact equality holds for the naive first-order kernel
`E^2 = m^2 + K(p)`, a larger dynamics import that is not used here.

## Proof Sketch

For T1, the d-dimensional dispersion authority folds the lattice into a
`2^d` two-site-cell basis and proves that the staggered phase algebra reduces
the free two-step symbol to the scalar function
`arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu))`. In `d = 3`, the cell space has
dimension `8`. The same authority proves taste degeneracy because
`sin^2(k_mu + pi r_mu) = sin^2 k_mu`, so the forward-channel symbol is
`E(p) I_8`.

For T2, T1 reduces the rest-gap computation to the scalar function `E(p)`.
Since `sum_mu sin^2 p_mu >= 0`, the minimum of the square-root argument is
`m^2`, attained when every `sin p_mu` vanishes. Therefore
`min_p E(p) = arcsinh(m)`.

For T3, T2 gives the positive lower bound `E(p) >= arcsinh(m)` for `m > 0`.
In the full `d = 3` Brillouin zone, `sin p_mu = 0` for
`p_mu in {0, pi}`, giving the eight Dirac corners as the exact minimum set.
The gapped denominator in the T1 symbol gives a smooth projection on the
`m > 0` surface, and the same analytic transfer-symbol mechanism used by the
d-dimensional dispersion authority gives exponential localization. Setting
`m = 0` removes the T2 lower bound exactly at those eight points, so the
projection denominator is singular there.

For T4, restrict the T1 symbol to the rest line
`p_1 = p_2 = 0`, `p_3 = q`:

```text
    E(q) = arcsinh(sqrt(m^2 + sin^2 q)).
```

Near `q = 0`,

```text
    sin^2 q = q^2 + O(q^4),
    sqrt(m^2 + sin^2 q) = m + q^2/(2m) + O(q^4),
    E(q) = arcsinh(m) + q^2/(2m sqrt(1 + m^2)) + O(q^4).
```

Thus `(d^2 E / d q^2)|_0 = 1/(m sqrt(1 + m^2))`, and T4 defines the reciprocal
coefficient `M_I = m sqrt(1 + m^2)`.

For T5, T2 gives `m_gap = arcsinh(m)`, hence `sinh(m_gap) = m` and
`cosh(m_gap) = sqrt(1 + m^2)`. Therefore

```text
    (1/2) sinh(2 m_gap)
      = sinh(m_gap) cosh(m_gap)
      = m sqrt(1 + m^2)
      = M_I.
```

Expanding `m sqrt(1 + m^2) / arcsinh(m)` at small `m` gives
`1 + (2/3) m^2 + O(m^4)`, which proves the stated scaling-window comparison.

## Discharge Audit

The Record-stiffness context-independence no-go leaves R1 open as:

> "A separate theorem deriving a continuous local energy/action context from the framework."

Status after this note: R1 is NARROWED to the declared I-DYN chain
`H_eff = -log(T_2)/(2 a_tau)`, with the transfer object supplied by the
two-step positivity authority and the `d = 3` symbol supplied by the
d-dimensional dispersion authority. R1 is not closed.

The same no-go leaves R2 open as:

> "A separate theorem identifying an inertial rest-gap readout for physical matter."

Status after this note: the readout is identified and computed by T2, T4, and
T5 conditional on I-DYN, I-MASS, I-TIME, and the approved realized-state
primitive. The dynamical half, that `M_I` governs actual packet acceleration,
belongs to the companion inertial-closure theorem (separate science block) and
is not proved here.

The no-go's two-completion countermodel is untouched on the value of `m`: the
lambda-freedom is conceded. The same countermodel is untouched on the source
side: the gamma freedom remains a block04/source-side issue. This note claims
only the T1-T5 identities within the realized completion selected by the
declared imports and primitive.

## Consequence

On the declared transfer surface, there is a single scalar one-particle mass
observable per species. Its rest-gap readout is `arcsinh(m)`, and its
curvature-defined inertial-response readout is `m sqrt(1 + m^2)`. T5 makes the
relation between those readouts a universal function of the rest gap rather
than an equality at finite lattice spacing.

This narrows the conditional template's inertial-readout residual to a
transfer-derived computation on the free realized two-step surface. It does
not supply the source coefficient, a gravitational coupling identity, or a
derivation of the free value `m` from the current axiom surface.

## Boundaries

- Free `U = 1` surface only.
- `d = 3` two-step staggered one-particle transfer only.
- Representative-level licensed surface inheritance is only the inheritance
  allowed by the realized-branch selection note's boundaries.
- No claim is made from the four axioms alone.
- No gauged or interacting transfer theorem is proved here.
- No gravitational content is supplied.
- No WEP claim is supplied.
- No source-side gamma identity is supplied.
- No value-side derivation of `m` is supplied.
- The packet-acceleration theorem is delegated to the companion
  inertial-closure note (separate science block).
- This note sets no audit status.
- Independent audit is still required.

## Dependencies

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  supplies the free staggered two-step positive transfer/log-transfer
  authority and the one-axis exact dispersion anchor.
- [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the `d = 3` dispersion, taste-degenerate two-site-cell scalarity,
  and analytic transfer-symbol locality mechanism used by T1-T3.
- [`EP_RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md`](EP_RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md)
  supplies the R1/R2 residuals and the lambda/gamma two-completion firewall
  respected by the discharge audit.
- [`EP_RECORD_STIFFNESS_CONDITIONAL_SHARED_COUPLING_TEMPLATE_NOTE_2026-06-07.md`](EP_RECORD_STIFFNESS_CONDITIONAL_SHARED_COUPLING_TEMPLATE_NOTE_2026-06-07.md)
  supplies the conditional ratio-one template that T5 restricts to its
  first-order scalar-kernel dynamics import.
- [`REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md`](REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md)
  supplies the realized-branch surface boundary consumed pointwise by the
  approved realized-state primitive.

## Runner And Cache

Primary runner:
[`scripts/mass_observable_two_step_surface_2026_07_08.py`](../scripts/mass_observable_two_step_surface_2026_07_08.py)

Runner cache:
[`logs/runner-cache/mass_observable_two_step_surface_2026_07_08.txt`](../logs/runner-cache/mass_observable_two_step_surface_2026_07_08.txt)

Current local runner result:

```text
TOTAL: PASS=7 FAIL=0
```

Load-bearing residuals from the cached run: taste-degeneracy eigenvalue
spread `3.0e-14` across the `L = 8` Brillouin-zone grid, rest-gap and
global-gap residuals exactly `0` on the checked grids, sympy-exact inertial
curvature and universal-function identities (symbolic residual `0`, series
coefficients `(0, 2/3, 0)` for `m^1, m^2, m^3`), generator-invariance
spectrum deviations `<= 1.8e-14`, and the historical width-proxy contrast
`1/(m sigma)` varying by exactly `3.0x` while both spectral readouts carry
no width dependence.

## Changelog

- **2026-07-08.** Initial bounded-theorem note with paired runner; local
  runner result `TOTAL: PASS=7 FAIL=0`.
