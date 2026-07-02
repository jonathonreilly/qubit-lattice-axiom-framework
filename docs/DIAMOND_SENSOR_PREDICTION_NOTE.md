# Diamond Sensor Prediction Note

**Date:** 2026-04-05 (audit-narrowing refresh: 2026-05-10)
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded experiment-facing discriminator design, intentionally
bounded; **not** a closed lab prediction.
**Status authority:** independent audit lane only.
**Authority role:** records, but does not close, a bounded discriminator
design (lock-in `X`, `Y`, `phi`, widefield phase ramp) for a diamond/NV
setup. The ideal lock-in detector map is supplied by
[`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md).
The remaining open targets are the source-to-NV coupling map and the
absolute lab amplitude/noise budget.

## Purpose

This note turns the cited phase-sensitive / retarded / wavefield lane
notes into one lab-facing **discriminator design** for a diamond/NV
sensor setup.

The goal is **not** a generic force claim and **not** a closed
quantitative prediction.
The goal is one observable that a diamond lock-in microscope can in
principle measure, one standard-physics null, and one minimal control
set, with the explicit limitation that the source-to-NV coupling map and
absolute amplitude budget are still missing.

## Audit boundary

This note assembles a class-B experiment-facing discriminator card by
combining an explicit ideal lock-in detector theorem with upstream
retarded-field / wavefield source-candidate context. It names the
corresponding lock-in observables (`X`, `Y`, `phi = atan2(Y, X)`, `R`,
widefield phase profile). It is **not** a derivation of those upstream
source candidates and **not** a closed NV-coupling forward model.

**Cited authorities and context (one-hop deps where load-bearing; audit
effective status remains ledger-owned):**

- [`docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)
  — supplies the bounded ideal-detector map from a delayed driven source
  history to `X`, `Y`, `phi`, the `pi`-flip/null controls, and a
  widefield phase-slope law. This closes only the detector-map step.
- [`docs/RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md`](RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md)
  — supplies retarded-field causality context used as the
  qualitative motivation for a finite-delay phase-lag signature.
- [`docs/RETARDED_FIELD_DELAY_PROXY_NOTE.md`](RETARDED_FIELD_DELAY_PROXY_NOTE.md)
  — supplies intermediate-layer phase-lag context (`mix` parameter,
  single phase-lag observable). Cited as source-candidate motivation
  only; this note does not ratify its audit status.
- [`docs/SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md)
  — supplies source-resolved wavefield context that motivates the spatial
  phase-ramp readout. Cited as source-candidate motivation only; not a
  validated NV-coupling theorem.

**In-note class-B content (what survives at this scope):**

- a discriminator design naming the lock-in observables `X`, `Y`,
  `phi`, `R`, and the widefield spatial phase profile;
- a qualitative ordering: standard quasi-static null gives `Y ~ 0`,
  `phi ~ 0`, flat phase, while a finite-delay / wave-like coupling
  gives `Y != 0`, `phi != 0`, and a coherent spatial phase ramp that
  strengthens with drive frequency and source-detector separation;
- the toy scaling law `Y/X ~ omega*tau`, `phi = atan(omega*tau)`
  reported by `scripts/diamond_sensor_prediction_probe.py` and checked
  from the cycle-average definitions by
  `scripts/diamond_ideal_lockin_detector_theorem.py`;
- a minimal control list (drive off; source retracted; `pi` reference
  flip; static-source baseline) and a pre-experiment validation step
  (run the same lock-in pipeline on a known magnetic or strain source
  first).

These are class-B / class-A consequences of the ideal detector theorem,
the cited source-candidate context, and a single-delay toy model. They are
**not** a derivation of the source-to-NV coupling map and **not** a
calibrated signal budget.

**Admitted-context derivation gap (real, not import-redirect):**

The note **does not** derive any of:

1. a validated mapping from the cited source-candidate proxies to a real
   NV sensor coupling strength;
2. a calibrated absolute signal budget for a specific NV lab geometry
   that would convert the qualitative ordering into a detectability
   claim.

The detector-map bridge is now explicit and executable, but the remaining
items above are **real D-class derivation gaps**, not dependency-citation
issues.

## Why a lock-in interface is the right scope (not an absolute claim)

The NV literature already supports the relevant readout style:

- phase-sensitive lock-in readout of time-dependent fields in diamond NV
  magnetometry
- widefield / pixel-wise lock-in detection
- NV sensitivity to strain in diamond mechanical structures

That makes a lock-in quadrature or phase-ramp **discriminator design** a
better lab-facing scope than an absolute gravitational-force claim,
which is **not** budgeted by this repo.

The cited phase-sensitive infrastructure and detector-map support:

- [`docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)
- [`docs/RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md`](RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md)
- [`docs/RETARDED_FIELD_DELAY_PROXY_NOTE.md`](RETARDED_FIELD_DELAY_PROXY_NOTE.md)
- [`docs/SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md)

## Concrete discriminator design (scope-bounded; not a closed prediction)

Using the ideal detector theorem and conditional on the cited upstream
retarded-field / wavefield source candidates above, the smallest
defensible experiment-facing **discriminator design** is:

- a driven-source NV lock-in readout should show a nonzero quadrature channel
  `Y` or a nonzero phase lag `phi = atan2(Y, X)` if the coupling is genuinely
  retarded / wave-like
- the same readout should remain phase-null after calibration in the
  standard instantaneous / quasi-static baseline
- in a widefield geometry, the phase should not just shift globally; it
  should form a coherent spatial phase ramp across the NV image if the
  wavefield lane is the right effective description

The direct null is:

- after phase calibration and static-background subtraction, standard
  Newtonian / quasi-static coupling predicts `Y ≈ 0` and no stable spatial
  phase ramp

The discriminator-design expectation, conditional on the cited retarded /
wavefield source candidates and the supplied ideal detector theorem, is:

- finite propagation or wave-scheduling should produce a measurable
  phase-lag / quadrature component
- that quadrature should strengthen as the drive frequency rises and as the
  source-detector separation increases
- in an imaging readout, the phase slope across the field of view should be
  the cleanest discriminator, not raw amplitude

This is the **qualitative ordering** the discriminator card is built
around. It is **not** a calibrated NV detectability claim, since the
validated NV-coupling map and absolute amplitude budget remain open.

## Ideal detector bridge now supplied

The ideal detector bridge is now supplied by
[`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md):

- perfect phase reference
- no technical noise
- no bandwidth or integration limits
- direct predicted outputs for `X`, `Y`, `phi`, and the widefield phase slope

The source-fidelity check comes before detector realism:

- verify that the simulated source trajectory is the intended one
- verify that retarded and instantaneous comparators use the same source history
- only then add instrument-specific filtering or noise

This keeps the experiment card honest: physics prediction first,
instrument model second.

## Minimal control set

The smallest useful control set is:

1. drive off
2. same drive with the source removed or retracted far enough that the
   coupling should be negligible
3. same drive with a `pi` phase flip in the reference channel, to check that
   the extracted quadrature really changes sign
4. static source / no modulation, to remove any DC or slow drift background

If the lab wants a stronger control, the same protocol can be run first on a
known magnetic or strain source to verify the lock-in pipeline before trying
the weaker gravity-facing interpretation.

## Honest limitation

This repo does **not** yet give a defensible absolute gravity amplitude for an
NV lab.

So the claim surface should stay narrow:

- phase-quadrature discriminator: yes
- coherent spatial phase ramp: yes
- absolute gravity detectability: not yet budgeted here
- ideal-detector lock-in map: supplied only at ideal mathematical scope

That is the smallest prediction still worth taking to a diamond lab.

## What would count as a hit

- `Y` survives calibration and is not consistent with zero
- the sign of `Y` flips under the reference `pi` control
- a widefield sensor image shows a stable nonzero phase gradient
- the effect strengthens with frequency / separation in the expected causal
  direction

## What would count as a miss

- quadrature vanishes after calibration
- the phase is flat across the image
- the signal moves only because of instrument lag, heating, or a trivial
  amplitude rescaling

## Experimental framing (scope-bounded)

If this discriminator design is sent to a diamond/NV lab, the cleanest
phrasing is:

"Measure the lock-in quadrature and spatial phase ramp for a driven
source near an NV sensor. The standard quasi-static baseline predicts
no stable quadrature after calibration; under the cited retarded /
wavefield source-candidate context and the ideal lock-in detector theorem,
the discriminator design names a nonzero phase-lag signature as the
qualitative ordering signal. Absolute detectability is not budgeted by
this note."

## References that motivate the readout choice

- NV dual-channel lock-in readout of time-dependent fields:
  [Phys. Rev. B 88, 220410](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.88.220410)
- widefield / per-pixel lock-in detection in diamond NV imaging:
  [Scientific Reports 2022](https://www.nature.com/articles/s41598-022-12609-3)
- NV strain sensitivity in diamond mechanical structures:
  [Scientific Reports 2020](https://www.nature.com/articles/s41598-020-65049-2)

## Final Verdict (scope-bounded)

**Bounded experiment-facing discriminator design only.**

Using the ideal detector theorem and conditional on the cited upstream
retarded-field / wavefield source-candidate context, this row records:

- a discriminator design naming `X`, `Y`, `phi`, `R`, and the spatial
  phase profile;
- a qualitative `phi = atan(omega*tau)` toy scaling under a single-delay
  proxy (class-A consequence; not derived from an NV Hamiltonian);
- a minimal control list and a pre-experiment validation step.

It is **not** a closed lab prediction, **not** a calibrated NV detectability
claim, and **not** a derivation of the cited upstream source candidates.
The validated NV-coupling map and absolute signal budget remain open.

## Repair target

The ideal detector map from a delayed driven source trajectory to `X`,
`Y`, `R`, `phi`, controls, and the widefield phase-slope law is now supplied
by `DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`. The
remaining repair target is the physical source-to-NV coupling and calibrated
amplitude/noise bridge; this note still exposes only the qualitative
ordering and discriminator design.

## Repo-canonical vocabulary

Terminology used in this note matches the repo-canonical vocabulary:
"diamond NV", "phase ramp", "signal budget", "prediction", "protocol",
"lock-in quadrature `Y`", "phase lag `phi`", "spatial phase profile".
No new tags, no new classes, no parent-framing cross-references
implying a class, no status promotion language.
