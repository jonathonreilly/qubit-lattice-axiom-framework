# De Sitter Curvature Gap Is Not a Fierz-Pauli Mass Diagnostic

**Date:** 2026-06-08
**Claim type:** bounded_theorem / spectral-scale diagnostic
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:**
[`scripts/de_sitter_curvature_gap_not_fierz_pauli_mass_diagnostic_2026_06_08.py`](../scripts/de_sitter_curvature_gap_not_fierz_pauli_mass_diagnostic_2026_06_08.py)
**Runner cache:**
[`logs/runner-cache/de_sitter_curvature_gap_not_fierz_pauli_mass_diagnostic_2026_06_08.txt`](../logs/runner-cache/de_sitter_curvature_gap_not_fierz_pauli_mass_diagnostic_2026_06_08.txt)

## Summary

This note preserves the narrow, useful part of the R1 graviton-mass branch:

```text
An infrared spectral gap proportional to 1/R is a curvature gap.
It vanishes as R -> infinity, so it is not by itself a
scale-independent Fierz-Pauli mass parameter.
```

Applied to the cited de Sitter/S3 TT-spectrum scale, the energy scale is
proportional to `hbar c / R`. If `R` is set to a Hubble-radius comparator, the
associated Compton length is order the Hubble radius. Sub-Hubble Yukawa factors
are therefore practically indistinguishable from `1/r` at laboratory and
solar-system scales, while order-one deviations occur only at the same infrared
curvature scale.

That is a diagnostic distinction, not a proof that the framework has already
constructed a full massless spin-2 sector.

## Runner-Checked Content

The runner checks:

- `m_gap(R) proportional 1/R`, so the gap decreases by the same factor when
  `R` is enlarged and tends to zero in the flat limit;
- the Hubble-radius comparator gives a Compton length of order `R`;
- the resulting Yukawa factor is negligible at sub-cosmological scales and
  order one only at the curvature radius;
- source guardrails prevent this diagnostic from being read as lambda=1,
  diffeomorphism, stress-conservation, or gravity-sign closure.

`TOTAL: PASS=4 FAIL=0`.

## What This Establishes

If a cited "graviton mass" is exactly the curvature spectral scale
`m_gap(R) proportional 1/R`, then that number does not represent a
scale-independent Fierz-Pauli mass. It is an infrared curvature scale that
disappears in the flat limit.

The `1/r` versus Yukawa comparison remains the standard diagnostic contrast:
a strictly massless Green function gives `1/r`, while a scale-independent
Fierz-Pauli mass would give `exp(-m r)/r`.

## What Remains Open

- Framework-native construction of a conserved stress tensor for the relevant
  interacting sector.
- Emergent spin-2 gauge invariance or diffeomorphism closure.
- The `lambda=1` gravity atom.
- The sign of the gravitational coupling.
- Any claim that a retained `1/r` diagnostic alone proves the full massless
  spin-2 uniqueness-theorem hypotheses.

## Forbidden Imports

- No new axiom, primitive, or Tier-A admission is introduced.
- No Planck-scale or physical-unit primitive is consumed as a derivation input.
- `H0`, `hbar`, and `c` are used only to evaluate the cited curvature-scale
  comparator; this note does not derive those constants or use them as
  framework premises.
- The de Sitter/S3 TT spectrum is cited as the source of the curvature-scale
  comparison, not reproven here.
- This note sets no audit status.

## Dependencies

- [GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md](GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md)
  supplies the cited de Sitter/S3 curvature-gap identity.
- [GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md)
  supplies the separate `1/r` diagnostic context. This note does not promote
  that context into a full spin-2 uniqueness closure.

## Honest Auditor Read

Audit this as a bounded spectral-scale diagnostic: a `1/R` de Sitter curvature
gap is not a scale-independent Fierz-Pauli mass. Do not audit it as a proof that
the framework has satisfied the full masslessness, gauge-invariance,
diffeomorphism, or gravity-sign requirements of the broader gravity program.
