# Theta Mass-Side Composition Close on the Shared Occupancy Bridge

**Date:** 2026-07-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem (composition), conditional on the named shared bridge
**Status authority:** independent audit lane only. This source note sets no
audit outcome and changes no registry row.
**Current-main posture (2026-07-07):** theta's Tier-A admission is already
retired on main by the retained 2026-07-05 retirement decision. This note is
banked only as bounded historical/supporting science for the mass-side
composition surface; it does not reopen, modify, or supply authority for that
retirement record.
**Primary runner:**
[`scripts/frontier_theta_mass_side_composition_close_2026_07_03.py`](../scripts/frontier_theta_mass_side_composition_close_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/frontier_theta_mass_side_composition_close_2026_07_03.txt`](../logs/runner-cache/frontier_theta_mass_side_composition_close_2026_07_03.txt)

## Statement

This note composes the theta mass-side chain on one named supplied bridge:

> one record locking one admissible local possibility is one statistical slot, and the relevant locked possibilities for the generation doublet are the K/CPT record-outcome orbits rather than the real components of the fluctuation coordinate.

Conditional on that sentence, the mass-side K-real structure is read as the
same conjugate-symmetric `C_3` object as the flavor doublet's K/CPT
record-outcome orbit reading. Under that single input, the determinant channel
reads the K-real conjugate-paired content.

The composed conclusion on the stated mass surface is:

```text
arg det(M_q) = 0.
```

No positive-mass convention, no independent K-real admission, and no separate
determinant-channel identification is added beyond the shared bridge sentence.

## Composition

**Leg 1: K-real reading from the shared bridge.** The supplied sentence says
that one locked admissible local possibility is one statistical slot and that
the relevant generation-doublet possibilities are K/CPT record-outcome orbits.
For this composition, that is the only input that identifies the mass-side
determinant channel with the K-real conjugate-paired reading.

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

Together, Leg 1 supplies the K/CPT determinant-channel reading, Leg 2 removes
the discrete sign branch, and Leg 3 removes continuous determinant phase
characters. The theta mass-side supplied content therefore reduces to exactly
the one bridge sentence quoted above.

## Single Supplied Sentence

The theta mass side and the flavor occupancy piece now share one supplied
bridge:

> one record locking one admissible local possibility is one statistical slot, and the relevant locked possibilities for the generation doublet are the K/CPT record-outcome orbits rather than the real components of the fluctuation coordinate.

Retiring that sentence retires both the theta mass-side composition here and
the flavor occupancy bridge from the 2026-07-03 occupancy note.

Honest surviving-conditional count: **1**. The 2026-06-12 determinant note's
Record registrability condition is read as absorbed here, on the registry's
own identification: the Tier-A registry states that the mass-side K-real
structure is "the same C_3 conjugate-symmetric object as AC_phi_lambda
sub-admission (i)", and that piece (i)'s "custody K-reality and
det_C/equal-power selectors are its two faces". The shared bridge sentence
supplies the orbit reading of that one object, so both faces — the K-real
custody reading and the determinant-channel selection — are the same supplied
content, not two sentences. The 2026-06-12 conditional sentence guarded by the
runner remains:

> The statement is deliberately conditional on the supplied mass determinant channel.

In this composition, that supplied channel is the mass-side use of the shared
bridge sentence.

Reviewer flag: this absorption reading is the single judgment call in this
note. If a reviewer or the audit lane rejects it, the honest count is two
sentences (the shared bridge plus the registrable-channel membership of the
physical mass readout), and the composition otherwise stands unchanged.

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
- [`tier_a_admissions.json`](audit/data/tier_a_admissions.json) is used only
  for the registry's own identification that warrants the one-sentence versus
  two-sentence conditional count; it is not an audit-status authority.

## Runner

Run:

```bash
python3 scripts/frontier_theta_mass_side_composition_close_2026_07_03.py
```

The runner uses exact rational arithmetic for the finite matrix checks. It
guards the shared bridge sentence, the 2026-07-01 pairing formula content, and
the 2026-06-12 conditional sentence; it checks signed scalar masses on the
same grid used by the 2026-07-01 runner, exact signed-Brannen circulant dials,
the phase-character erasure, the hostile guard, and the one-sentence
conditional count.
