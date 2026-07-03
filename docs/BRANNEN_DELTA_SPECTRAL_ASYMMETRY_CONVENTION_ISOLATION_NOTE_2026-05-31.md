# Brannen Delta and Spectral-Asymmetry Convention Boundary

**Date:** 2026-05-31
**Type:** open_gate
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Claim boundary:** finite `C_3` weight/angle comparison plus an observational
charged-lepton mass comparator. This note adopts no radian convention and sets no
verdict.
**Primary runner:** [`scripts/frontier_brannen_delta_spectral_asymmetry_convention_isolation.py`](../scripts/frontier_brannen_delta_spectral_asymmetry_convention_isolation.py)
**Runner cache:** [`logs/runner-cache/frontier_brannen_delta_spectral_asymmetry_convention_isolation.txt`](../logs/runner-cache/frontier_brannen_delta_spectral_asymmetry_convention_isolation.txt)
**No-promotion statement:** This source note records an open convention
boundary only; it creates no promotion, no registry edit, and no audit verdict.

## Result

The runner checks four bounded facts about the Brannen delta lane.

1. The finite `C_3` doublet Lefschetz/Molien weight is exactly
   `L_3(1,2)=2/9`.
2. Reducing the PDG charged-lepton masses through the Brannen ansatz gives an
   observational comparator `delta ~= 0.22223 rad`, close to the bare rational
   `2/9`. The masses are comparator data, not proof inputs.
3. The finite angle objects already in the lane do not equal the bare-radian
   value `delta = 2/9`: the Plancherel-step angle is `(2/9)pi`, the eta-holonomy
   angle is `2pi(2/9)`, the spin-Dirac eta for `(1,2)` is zero, the tested finite
   eta is integer-valued, and the circulant `H(theta)` has fixed Fourier
   eigenvectors with zero Berry connection. The exact one-factor-of-pi comparison
   `(2/9)pi = pi * (2/9)` is taken against the bare framework rational `2/9`, not
   against the empirical PDG-derived angle (which differs from `2/9` at order
   `1e-4`).
4. The formula `(N^2-1)/(12N)` for the Lefschetz/Molien family equals the rank
   fraction `(N-1)/N^2` only at `N=3`; the shared `2/9` is not a family identity.

The durable conclusion is therefore narrow: the same rational `2/9` appears on the
same finite `C_3` doublet lane, but the step from a dimensionless rational to the
bare-radian phase remains a convention/input boundary.

## 2026-06-13 Downstream Boundary Alignment

This row is now a sharper convention locator because the surrounding bounded
rows are explicit:

- [`FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md`](FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md)
  carries the finite `2/9` flavor-asymmetry weight.
- [`KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md`](KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md)
  keeps dimensionless radian/native-unit bookkeeping separate.
- [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
  remains the no-go anchor for deriving the bare-radian bridge from the tested
  A1 route.
- [`KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md`](KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_NARROW_THEOREM_NOTE_2026-06-08.md)
  gives bounded support for the shared orientation structure.

The updated runner checks those status anchors and the exact distinction among
`2/9`, `pi*(2/9)`, and `2*pi*(2/9)`. It still does not adopt a period-1-radian
normalization or derive the physical Brannen phase.

## Boundary

This note does not derive `delta = 2/9 rad`, does not prove a no-coincidence closure,
and does not ratify period-1-radian normalization. It records which eta/holonomy
routes fail for the tested finite objects and leaves the period-normalization bridge
open for a future source theorem or explicit convention note.

## No-Go Discipline Gate

**N1.** Routes tested: direct finite weight, Plancherel angle, eta-holonomy,
circulant Berry phase, and `N`-family identity. None derives the bare-radian value.
**N2.** The period-normalization wall and the eta/holonomy wall are independent.
**N3.** PDG masses are marked as observational comparator data; they are not proof
premises.
**N4.** The residual matches the existing radian-normalization bridge, not a new
axiom request.
**N5.** "Convention boundary" means the radian assignment remains open; the finite
`2/9` weight is still structural.
**N6.** A future period-normalization convention or a separate Fisher/source theorem
could close the boundary without changing axioms.
**N7.** The strongest counterargument is that the PDG agreement motivates a period-1
reading. This note treats that as evidence to investigate, not as a derivation.
**N8.** The same residual appears in the radian-bridge and native-unit-separation
notes; this note only localizes it for the Brannen delta lane.

## Load-Bearing Authorities

[AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
[KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md](KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md)
[KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
[KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md](KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md)
[NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md](NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md)

## Repair Log

**2026-06-20 — runner_artifact_issue repair.** Clarified the pi-factor comparison
wording is against bare `2/9`, not the empirical PDG angle; not load-bearing for
the verdict; no value changed. The Section C labels and the bare-rational comment
in `frontier_brannen_delta_spectral_asymmetry_convention_isolation.py` now state
explicitly that the exact `(2/9)pi = pi * (2/9)` comparison is taken against the
bare framework rational `delta = 2/9`, not the empirical PDG-derived angle (which
differs at order `1e-4`). The comparison itself and all numeric values are
unchanged; the runner still reports 16/16 checks passed.
