# Theta Mass-Side Composition Close on the Shared Occupancy Bridge

**Date:** 2026-07-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem (composition), conditional on two independent bridges
**Status authority:** independent audit lane only. This source note sets no
audit outcome and changes no registry row.
**Current posture (2026-07-11):** this is a conditional composition surface.
Historical decisions supply no premise and current status is set only by the
independent audit lane.
**Primary runner:**
[`scripts/frontier_theta_mass_side_composition_close_2026_07_03.py`](../scripts/frontier_theta_mass_side_composition_close_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/frontier_theta_mass_side_composition_close_2026_07_03.txt`](../logs/runner-cache/frontier_theta_mass_side_composition_close_2026_07_03.txt)

## Statement

This note composes the theta mass-side chain on two distinct conditional
bridges:

1. the charged-lepton matter action counts the `K`/CPT orbit once; and
2. that charged-lepton carrier is the same physical channel that controls the
   quark determinant readout.

Conditional on both statements, the mass-side K-real structure is read as the
same conjugate-symmetric `C_3` object as the flavor doublet's K/CPT
record-outcome orbit reading. Under those two inputs, the determinant channel
reads the K-real conjugate-paired content.

The composed conclusion on the stated mass surface is:

```text
arg det(M_q) = 0.
```

No positive-mass convention is added. The determinant-channel identification
is explicitly separate from the charged-lepton occupancy grain.

## Composition

**Leg 1: charged-lepton occupancy grain.** The first conditional states that
the physical charged-lepton matter action counts the `K`/CPT orbit once. It
does not identify a quark determinant channel.

**Leg 1b: cross-sector determinant readout.** The second conditional identifies
the charged-lepton carrier with the physical quark determinant channel. This is
an independent physical bridge, not a consequence of Leg 1.

**Leg 2: orientation forced on both signs.** The 2026-07-01 mass-orientation
note gives the pairing formula, in the ASCII form guarded by the runner:

```text
det(M_KS + m I) = (prod over positive lambda of (m^2 + lambda^2)) * m^(2z) >= 0 for every real m of either sign.
```

The determinant is even in `m`, so the positive-mass convention is not
load-bearing for the orientation. The same factorization applies to a
Hermitian generation mass on the flavor tensor factor: each real signed root
feeds one scalar factor of the same nonnegative form.

**Leg 3: phase erasure.** The 2026-06-12 determinant-readout note supplies the
continuous determinant phase character result inside the multiplicative
determinant/block-composition class. K/CPT orbit registration forces
`exp(i k arg det M)` to have `k = 0`. The hostile guard remains outside:
`cos(arg det M)` is K-even, but it violates the multiplicative
independent-block composition law.

Together, Legs 1 and 1b conditionally supply the K/CPT determinant-channel
reading, Leg 2 removes the discrete sign branch, and Leg 3 removes continuous
determinant phase characters. The theta mass-side content therefore remains
conditional on both the occupancy-grain bridge and the independent
cross-sector determinant-readout bridge.

## Two Independent Open Dependencies

The charged-lepton statistical grain and the quark determinant readout are
separate derivation obligations. Closing the former does not close the latter.
The 2026-06-12 conditional sentence guarded by the runner remains:

> The statement is deliberately conditional on the supplied mass determinant channel.

Historical decision text at
`docs/audit/data/premise_decision_history.json` does not collapse those two
conditions or supply either one.

## Boundaries

The gauge side is untouched. The three gauge-side sub-walls remain:
`theta_gauge`, the real-positive Wilson action surface, and
multi-plaquette/large-winding gauge data.

This note makes no theta value claim beyond `arg det(M_q) = 0` on the stated
mass surface.

The audit lane owns statuses, and the registry is untouched.

## Dependencies

- [`KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md`](KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md)
  supplies the shared one-record-one-slot bridge sentence used by Leg 1.
- [`THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md`](THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md)
  supplies the signed-mass pairing formula used by Leg 2.
- [`STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md`](STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the determinant phase-character erasure and the guarded supplied
  mass determinant-channel conditional used by Leg 3.
- [`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
  records the zero-weight charged-lepton occupancy-grain obligation.
- [`THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`](THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md)
  records the distinct zero-weight quark determinant cross-sector obligation.
- `docs/audit/data/premise_decision_history.json` is provenance only.

## Runner

Run:

```bash
python3 scripts/frontier_theta_mass_side_composition_close_2026_07_03.py
```

The runner uses exact rational arithmetic for the finite matrix checks. It
guards the shared bridge sentence, the 2026-07-01 pairing formula content, and
the 2026-06-12 conditional sentence; it checks signed scalar masses on the
same grid used by the 2026-07-01 runner, exact signed-Brannen circulant dials,
the phase-character erasure, the hostile guard, and the two-condition count.
