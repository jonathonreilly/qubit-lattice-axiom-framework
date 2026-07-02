# Koide Amplitude and Brannen Phase Joint-Sourcing Shortcut: Tested-Class Narrow No-Go

**Date:** 2026-06-04
**Type:** no_go
**Claim type:** no_go (route-specific, tested-class shortcut pruning).
**Claim scope:** within the tested Z3/C3 shortcut classes enumerated
below, no tested native object jointly supplies the Brannen phase
`delta = 2/9` as an argument and the Koide/Brannen amplitude
`beta/a = 1/sqrt(2)` (or the cosine coefficient `sqrt(2)`) as a
modulus. The tested classes are: the documented `(N-1)/N^2` mechanisms
at `N=3`, C3 orbit sums and partial orbit sums, the eigenvalue DFT
coefficient, APS eta scans over `p <= 12`, Fisher-Rao polar/azimuth
coordinates, and the real `Q`-to-`delta` ratio. This prunes only the
shortcut "derive the amplitude for free from the phase object." It does
not prove that every possible future native structure is exhausted.
**actual_current_surface_status:** narrow route-pruning no-go. The
amplitude/equipartition gate and the `delta = 2/9` phase gate both
remain open.
**bare_retained_allowed:** false
**Status authority:** independent audit lane only.
**Runner:** [`scripts/koide_amplitude_phase_joint_or_independent.py`](./../scripts/koide_amplitude_phase_joint_or_independent.py)
**Runner cache:** [`logs/runner-cache/koide_amplitude_phase_joint_or_independent.txt`](./../logs/runner-cache/koide_amplitude_phase_joint_or_independent.txt)

## Question

The charged-lepton Brannen form uses two admitted pieces of data:

```text
x_k / a = 1 + sqrt(2) cos(delta + 2 pi k/3),  k = 0,1,2.
```

The amplitude slot is equivalent to `beta/a = 1/sqrt(2)` and to the
Koide-cone condition `Q = 2/3` through the
[Koide lightcone primitive](KOIDE_LIGHTCONE_PRIMITIVE_THEOREM_NOTE_2026-05-10.md).
The phase slot is the Tier-A admitted `delta = 2/9` input in the
[Brannen BAE delta note](CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md).

This note asks a narrow shortcut question: do the tested native Z3/C3
objects that produce `2/9` also force the amplitude slot? If yes, the
phase route would collapse the amplitude gate. If no, the two gates
remain separate.

## Result

For the tested classes, the shortcut fails.

1. The `(N-1)/N^2` mechanisms that land on `2/9` at `N=3` produce
   `2/9` as a real value: modulus `2/9`, argument `0`.
2. The object that has argument `2/9`, the unit phase `exp(i 2/9)`,
   has modulus `1`, not `1/sqrt(2)` or `sqrt(2)`.
3. C3 orbit sums, partial orbit sums, the eigenvalue DFT coefficient,
   and APS eta scans over `p <= 12` do not produce an object with both
   argument `2/9` and modulus in `{sqrt(2), 1/sqrt(2)}`.
4. In Fisher-Rao coordinates, the amplitude is a polar/colatitude
   condition while the phase is an azimuth/longitude coordinate.
5. The real `delta = Q/3` relation links two real values; it is not a
   modulus/argument identity for one complex object.

Therefore the tested route "one native object gives both pieces" is
pruned. The note does not derive either input and does not close future
two-input or new-structure routes.

## Standing Inputs and Imports

- `delta = 2/9` is consumed as the existing Tier-A admitted input; this
  note does not derive it.
- The amplitude target uses the `Q = 2/3` / `beta/a = 1/sqrt(2)` algebra
  from the Koide lightcone primitive.
- The Fisher-Rao polar-coordinate restatement is cited from
  [Koide Fisher-Rao spherical reorganization](KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01.md).
- No observed lepton masses, PDG values, fitted selectors, new axiom,
  new primitive, or new admission are used.
- The [Lattice + Quantum + Record baseline](MINIMAL_AXIOMS_2026-06-04.md)
  does not decide either gate.

## No-Go Discipline Gate

| Gate | Review |
|---|---|
| N1 alternative routes | Tested at least five routes: (1) one complex Brannen coefficient `b`; (2) the documented `(N-1)/N^2` mechanisms: APS eta, anomaly coefficient, Bernoulli/color variance, Hurwitz/Bernoulli value, Burnside/K-theory, unit character phase; (3) C3 orbit sums, partial orbit sums, DFT coefficient, and APS eta scan over `p <= 12`; (4) Fisher-Rao polar/azimuth coordinates; (5) the real `Q`-to-`delta` ratio; (6) cross-`N` consistency of the cone amplitude versus `(N-1)/N^2`. |
| N2 wall independence | The amplitude/equipartition gate and the phase/longitude gate are independent in the tested surfaces: closing the phase route does not set the polar amplitude, and setting the amplitude does not select `delta = 2/9`. |
| N3 hidden-wall scan | The note consumes `delta = 2/9` as an admitted Tier-A input and explicitly leaves both gates open. It does not use Record, the minimal axioms, or a primitive to decide the shortcut. |
| N4 residual matching | The residual is exactly the shortcut residual: "one tested native Z3/C3 object supplies both phase and amplitude." This is narrower than "the amplitude is underivable" or "all native routes are exhausted." |
| N5 rhetoric audit | "Independent" means independent across the tested route classes and coordinate slots. It does not exclude a future two-input structure, a non-tested object, or a future theorem that derives both from a deeper source. |
| N6 partial-closure paths | A future convention/readout theorem could still relate the gates; that would be a new positive route, not contradicted by this tested-class no-go. |
| N7 steelman | The strongest counterargument is that the same C3 structure controls both the generation count and the `2/9` phase, so a deeper representation-theoretic object might bind the amplitude too. This note does not rule that out globally; it only shows the tested modulus/argument and orbit/eta/Fisher-ratio shortcuts do not supply the binding. |
| N8 cross-cycle echo | This matches the current Koide residual picture: the amplitude/equipartition route and phase route remain separate audit targets. The note prunes a shortcut, not the targets themselves. |

**No-go gate result:** PASS for the narrowed tested-class shortcut no-go.

## What This Establishes

- The tested `(N-1)/N^2`, orbit-sum, DFT, eta-scan, Fisher-coordinate,
  and real-ratio surfaces do not jointly source the amplitude and phase.
- Constructing `b = (1/sqrt(2)) exp(i 2/9)` is only a posit: modulus and
  argument are independent coordinates unless a separate theorem binds
  them.
- The amplitude and phase gates should remain separate audit targets.

## What This Does Not Establish

- It does not derive `delta = 2/9`.
- It does not derive `beta/a = 1/sqrt(2)` or `r = 1/2`.
- It does not prove that the amplitude is underivable.
- It does not rule out a future two-input theorem, a non-tested native
  object, or a deeper positive theorem that binds the two gates.
- It does not add or retire any axiom, primitive, or Tier-A admission.

## Verification

```bash
python3 scripts/koide_amplitude_phase_joint_or_independent.py
```

Expected summary:

```text
SCORECARD: PASS=27 FAIL=0
```

## Cross-References

- [Koide lightcone primitive](KOIDE_LIGHTCONE_PRIMITIVE_THEOREM_NOTE_2026-05-10.md)
  - amplitude / `Q = 2/3` algebraic target.
- [Koide Fisher-Rao spherical reorganization](KOIDE_FISHER_RAO_SPHERICAL_REORGANIZATION_NOTE_2026-06-01.md)
  - polar/azimuth coordinate interpretation.
- [Brannen BAE delta Tier-A note](CHARGED_LEPTON_BRANNEN_BAE_DELTA_TIER_A_BOUNDED_THEOREM_NOTE_2026-05-30.md)
  - admitted Brannen form and `delta = 2/9` input.
- [Koide APS eta parity route](KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md)
  - real `eta(1,2;3) = 2/9` phase-route surface.
- [Koide Q-delta formal identity](KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md)
  - formal-only `Delta_3 = Q_3/3` arithmetic; not a physical Brannen-phase
    or charged-lepton offset authority.
