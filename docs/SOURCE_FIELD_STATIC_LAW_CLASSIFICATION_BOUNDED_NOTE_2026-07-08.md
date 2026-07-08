# The Static Field Law For The Energy Source -- Shift-Symmetric Uniqueness, Forced Background Subtraction On Compact Surfaces, And The Charge-Sector Exhibit

**Date:** 2026-07-08
**Type:** bounded_theorem (exact lattice identities + measured window
legs + one measured comparator exhibit)
**Claim type:** bounded_theorem
**Claim scope:** Within the declared class of static field laws for a
potential sourced by the derived energy density -- linear, local,
translation-invariant, stable quadratic dynamics `L = mu^2 + c(-Delta)
+ lambda Delta^2` -- this note proves three exact structural facts and
exhibits their window behavior. (1) The Poisson/Newtonian member is the
unique shift-symmetric point of the class (`mu = 0` iff `L` annihilates
constants iff long-range). (2) On a compact surface, a source with
nonzero total -- and the energy density's total is POSITIVE, unlike
charge -- admits NO static solution at the shift-symmetric point unless
the background mean is subtracted: window gravity on this surface must
couple to energy CONTRASTS. (3) The framework's realized gauge sector
already produces exactly the subtracted `d = 1` Poisson response for
its charge source (ring Gauss law), including the measured
vacuum-screening onset. The field HALF of gravity remains underived:
nothing here derives the field's existence or its dynamics from the
axioms -- this note pins the target equation class and its forced
structure. No audit status is set.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/source_field_static_law_classification_2026_07_08.py`](../scripts/source_field_static_law_classification_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/source_field_static_law_classification_2026_07_08.txt`](../logs/runner-cache/source_field_static_law_classification_2026_07_08.txt)

## Why This Note Exists

The conserved-density classification reduced the gravitational source
to `gamma x` (energy density). The remaining gap is the field: what
generates the potential that the source couples to. Deriving that
dynamics is the named milestone, not this note's claim. What this note
does is make the target precise: within the minimal lawful class of
static field equations, symmetry and compactness force enough structure
that the remaining derivation problem is sharply posed -- and one
nontrivial structural consequence (background subtraction) follows
already.

## Premises

- Source form by citation: `gamma x` energy density (the classification
  note's corollary, with its named premises).
- **P-FIELD-CLASS (named premise):** the static field law is linear,
  local, translation-invariant, and stable (quadratic energy functional
  bounded below); symbol `L(k) = mu^2 + c lambda_lattice(k) + lambda
  lambda_lattice(k)^2` with `lambda_lattice` the lattice Laplacian
  symbol. Nonlinear self-sourcing and derived field dynamics are
  explicitly out of scope.

## Statements

**T1 -- shift-symmetric uniqueness (exact).** `L` annihilates constants
iff `mu = 0` iff the response is long-range (no exponential screening).
Runner: kernel of `-Delta` has multiplicity EXACTLY 1 (constants) in
`d = 1, 2, 3` with printed spectral gaps; `L_0 . 1 = 0` exactly;
`L_mu . 1 = mu^2 != 0`. The three-way equivalence massless <=>
shift-symmetric <=> long-range is exhibited numerically alongside the
exact symbol identities.

**T2 -- forced background subtraction on compact surfaces (exact).**
At `mu = 0` on a periodic lattice, `L_0 phi = rho` with `sum rho != 0`
is INCONSISTENT (the zero-mode equation reads `0 = rho_0`; runner
prints the exact inconsistency residual `1.0`); the mean-subtracted
source solves exactly (residual `1.8e-15`); any `mu > 0` solves
unsubtracted (`3.3e-16`). Because the energy density -- unlike charge --
has strictly positive total, a Newtonian (shift-symmetric) window law
on the framework's compact surface CANNOT couple to the raw energy
density: it must couple to the contrast `rho_E - <rho_E>`. This is a
definite structural statement with the shape of the cosmological
subtraction, forced here by lattice solvability alone.

**T3 -- window behavior of the classified members (measured).** The
subtracted `mu = 0` Green's function reproduces the Newtonian window
form: in `d = 3`, `1/(4 pi c r)` within `1-4%` for `r in [2, 5]` at
`16^3`, improving at every radius at `24^3`; in `d = 1` the ring
Green's function is EXACTLY `-|x|/2 + x^2/(2L) + const` to `3.2e-14` --
and the `x^2/(2L)` term IS the background subtraction made visible.
The `mu > 0` members are Yukawa-screened with range matching the exact
lattice relation `xi = 1/(2 asinh(mu/2))` to `0.1-0.5%`.

**T4 -- the charge-sector exhibit (measured on the comparator).** The
framework's realized gauge sector already implements this entire
structure for its charge source. On the staggered Schwinger ring with
an external neutral charge pair inserted through the Gauss law
(`N = 12`, `m = 0.3`): the measured ground-state electric-field
profile shows one unit of flux between the charges and compensated
field outside -- the subtracted `d = 1` Poisson solution -- with flux
contrast `0.93 / 0.90 / 0.81` at `g = 0.6` for separations `2 / 4 / 6`.
The ring Gauss law's total-charge-zero constraint is T2's solvability
dichotomy realized physically. The measured screening onset (contrast
falling to `0.84 / 0.39 / 0.27` at `g = 1.0`) is the vacuum
polarization correcting the bare law -- reported as physics, not
failure.

## What Remains Underived (stated plainly)

The existence of a field with `P-FIELD-CLASS` dynamics coupled to the
energy contrast is NOT derived from the axioms. The framework derives
the source form (energy density, one constant) and realizes the
complete source-field-response pattern in its charge sector; whether
the axioms force an analogous field for the ENERGY current -- the
graviton analog of the Gauss-law rotor -- is the sharply-posed open
problem this note defines. Candidate shapes for the next campaign: an
emergent collective mode of the record/link sector sourced by energy
contrasts, or a second forced gauge structure from the dynamics-form
theorem applied to the energy current.

## Boundaries

- P-FIELD-CLASS is a premise class (linear, local, static, stable,
  quadratic); nonlinearity, retardation, and derivation of the field
  are out of scope.
- T3's window gates are measured with printed finite-size trends;
  T1/T2 identities are exact to the printed floats.
- T4 is a `d = 1` charge-sector exhibit on the declared comparator;
  the energy-sector analog is the open problem, not a claim.
- No gravitational dynamics is derived; no WEP row is closed.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`NOETHER_SOURCE_CURRENT_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md`](NOETHER_SOURCE_CURRENT_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md)
  -- the derived source form this note takes as input.
- [`GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md`](GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md)
  -- machinery for the T4 exhibit (the Q0-ring-Gauss flag is T2's
  dichotomy in engine form).
- [`WEP_SOURCE_REDUCTION_FINITE_SPACING_BOUNDARY_SCALING_WINDOW_BOUNDED_NOTE_2026-07-08.md`](WEP_SOURCE_REDUCTION_FINITE_SPACING_BOUNDARY_SCALING_WINDOW_BOUNDED_NOTE_2026-07-08.md)
  -- the window-WEP frame the classified law would close into.

## Runner And Cache

Primary runner:
[`scripts/source_field_static_law_classification_2026_07_08.py`](../scripts/source_field_static_law_classification_2026_07_08.py)

Runner cache:
[`logs/runner-cache/source_field_static_law_classification_2026_07_08.txt`](../logs/runner-cache/source_field_static_law_classification_2026_07_08.txt)

Supervisor-executed runner result:

```text
TOTAL LAW-CLASSIFIED flags=subtraction-forced-on-compact,shift-symmetric-unique-massless,charge-sector-realizes-d1-poisson,screening-onset=yes,no-grav-dynamics-derived,no-audit-status-set elapsed=0.58s
```

Load-bearing residuals: kernel multiplicity 1 in all three dimensions;
zero-mode inconsistency exactly `1.0` unsubtracted vs `1.8e-15`
subtracted; `d = 1` ring law exact to `3.2e-14`; `d = 3` window match
`1-4%` improving with size; Yukawa range relation `0.1-0.5%`; flux
contrasts as quoted with monotone screening onset.

## Changelog

- **2026-07-08.** Initial note. Worker-drafted runner,
  supervisor-reviewed (external-charge Gauss insertion verified: the
  electric diagonal is rebuilt from `W + cumsum(q_int + q_ext)` on the
  neutral-pair sector) and supervisor-executed.
