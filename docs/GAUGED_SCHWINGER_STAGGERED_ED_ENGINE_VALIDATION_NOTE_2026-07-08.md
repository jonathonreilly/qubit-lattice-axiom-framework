# Gauged Schwinger Staggered ED Engine Validation Note

**Date:** 2026-07-08
**Type:** exact_support (machinery validation, no physics claim)
**Claim type:** exact_support
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py`](../scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/gauged_schwinger_staggered_ed_engine_2026_07_08.txt`](../logs/runner-cache/gauged_schwinger_staggered_ed_engine_2026_07_08.txt)

## Purpose

This note records validation of the exact-diagonalization machinery for the
gauged-surface campaign that attacks the static-comparator no-go's named escape:
the mediator requirement.  The model is Hamiltonian staggered fermions with
`U(1)` links, an electric term, and the ring Gauss law reduced to a single
Wilson-line rotor.

The construction is declared import **I-GAUGE**: a comparator/bridge
instantiation in `d = 1` of the covariant-hopping interaction class that the
record-preservation dynamics-form theorem forces.  It is a bridge realization,
not a derivation of the framework's gauged surface.

## Convention Note

The Hamiltonian one-body band is

```text
    E(p) = sqrt(m^2 + sin^2 p)
```

for the first-order kernel.  The two-step
`arcsinh(sqrt(m^2 + sin^2 p))` form in the free staggered two-step dispersion
note is its transfer cousin.  The engine states this split explicitly and never
conflates the Hamiltonian first-order kernel with the two-step transfer
dispersion.

## Validation Surface

The runner checks the finite-volume ED bookkeeping used by the I-GAUGE
comparator:

- charge-zero ring Gauss sector with staggered charge
  `q_n = occ_n - background_n`;
- a finite Wilson-line rotor cutoff `W in [-W_MAX, W_MAX]`;
- magnetic translation by two staggered sites on vectors whose support stays in
  the finite-`W` interior;
- the decoupled `U_holo = 1` Hamiltonian comparator for the free-dispersion
  check, because the exact `g = 0` boundary holonomy still shifts `W`.

This is an engine validation note only.  The validated object is the
finite-volume diagonalization and projection machinery, not the physical
adequacy of the I-GAUGE surface.

## Validated Properties

The runner reports the following residuals on the validation grid:

- gauge/translation symmetry commutator `4.9e-16`, with exact Gauss/charge
  checks;
- free-limit particle-hole dispersion agreement `3.5e-14` against the
  one-body Hamiltonian theory;
- Wilson-rotor truncation convergence from `W_MAX = 3` to `W_MAX = 4` at
  `3e-14`;
- momentum-sector reassembly versus the unprojected spectrum `7.4e-14` across
  the `(m, g)` validation grid;
- a gapped meson with momentum resolution: gaps `0.9687` at `g = 0.6` and
  `1.3285` at `g = 1.0`, for `N = 12`, `m = 0.3`;
- the two-body truncation projector reproduces the free limit to `1.4e-14`.
  At `g = 1.0`, the projected two-body meson gap is `1.5469` versus the
  full-Fock gap `1.3285`.

The last comparison is context for the next measurement block: the roughly
`16%` discrepancy is the band-curvature-level effect that block will quantify.
It is not asserted here as a physics claim.

## Engineering Flags

The runner deliberately surfaces all three construction flags in its `TOTAL`
line:

- `Q0-ring-Gauss`: the ring Gauss law forces total staggered charge
  `Q_tot = 0`;
- `finite-W-translation-interior`: at finite rotor cutoff, magnetic
  translation is checked on interior-supported vectors, since it is not an
  everywhere-defined unitary on the truncated rotor;
- `g0-Uholo-shifts-W`: the exact `g = 0` boundary holonomy shifts `W`, so the
  free-dispersion comparator uses the explicitly decoupled `U_holo = 1` form.

These flags are part of the validated contract.  They are not hidden
approximations.

## Relation To Upstream Notes

The dynamics-form theorem forces the gauge-invariant-local class whose leading
matter interaction is covariant hopping.  I-GAUGE is a `d = 1` comparator/bridge
instantiation of that forced class, using the Schwinger-chain-style Hamiltonian
surface described above.

The static-comparator no-go leaves a mediator requirement: static,
momentum-independent relative interactions cannot supply composite
mass-energy equivalence as an identity.  This note validates machinery for the
gauged mediator surface that attacks that named escape; it does not close the
escape or establish equivalence.

The free staggered two-step dispersion note supplies the transfer-matrix cousin
of the free staggered dispersion.  The present runner instead checks the
Hamiltonian first-order one-body band `sqrt(m^2 + sin^2 p)`, and treats the two
conventions as distinct.

## Boundaries

- `d = 1` comparator only.
- Validation sizes `N in {8, 12}`.
- I-GAUGE is an import/bridge realization, not a derivation from the axioms.
- No equivalence claim is made.
- No gravitational content is supplied.
- No derivation of the framework's gauged surface is attempted.
- This note sets no audit status.  Independent audit is required.

## Dependencies

- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  -- the forced covariant-hopping class that I-GAUGE instantiates.
- [`COMPOSITE_MASS_ENERGY_EQUIVALENCE_STATIC_COMPARATOR_NO_GO_NOTE_2026-07-08.md`](COMPOSITE_MASS_ENERGY_EQUIVALENCE_STATIC_COMPARATOR_NO_GO_NOTE_2026-07-08.md)
  -- the mediator requirement this campaign attacks.
- [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
  -- the transfer cousin of the Hamiltonian one-body band (convention split).

## Runner And Cache

Primary runner:
[`scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py`](../scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py)

Runner cache:
[`logs/runner-cache/gauged_schwinger_staggered_ed_engine_2026_07_08.txt`](../logs/runner-cache/gauged_schwinger_staggered_ed_engine_2026_07_08.txt)

Supervisor-executed runner result:

```text
TOTAL PASS elapsed~6s flags=Q0-ring-Gauss,finite-W-translation-interior,g0-Uholo-shifts-W
```

## Changelog

- **2026-07-08.** Initial source note for the gauged Schwinger staggered ED
  engine validation lane.  It records exact-support machinery validation only
  and sets no audit status.
