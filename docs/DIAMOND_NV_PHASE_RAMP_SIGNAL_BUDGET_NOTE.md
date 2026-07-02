# Diamond / NV Phase-Ramp Signal Budget Note

**Date:** 2026-04-05 (audit-narrowing refresh: 2026-05-10)
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** narrow experiment-facing **discriminator** card for the
phase-sensitive lane; **not** a closed signal budget.
**Status authority:** independent audit lane only.
**Authority role:** records, but does not close, a bounded discriminator
card naming the lock-in observables (`X`, `Y`, `phi`, widefield phase
ramp), the qualitative ordering with drive frequency / separation, and
the minimal control stack, using the ideal detector theorem plus cited
upstream retarded / wavefield source-candidate context and the sibling
diamond protocol / prediction notes.
The "signal budget" terminology here refers to the **qualitative
ordering structure**, not to a calibrated absolute amplitude budget.
The remaining open target for a closed signal budget is the physical
source-to-NV coupling and calibrated amplitude/noise bridge.

## One-line read

The best current diamond-facing **discriminator design** is not an
absolute gravity measurement.
It is a lock-in quadrature and spatial phase-ramp null test, conditional
on the cited upstream phase-sensitive source-candidate context and the
ideal lock-in detector theorem.

## Audit boundary

This note assembles a class-B experiment-facing discriminator card by
combining the ideal lock-in detector theorem, upstream retarded /
wavefield source-candidate context, the two sibling diamond protocol /
prediction notes, the propagator-family unification meta note, and the
complex-action carryover / grown companion notes. It is **not** a
derivation of those upstream source candidates and **not** a closed
NV-coupling forward model.

**Cited authorities and context (one-hop deps where load-bearing; audit
effective status remains ledger-owned):**

- [`docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)
  — supplies the bounded ideal-detector map from a delayed driven source
  history to `X`, `Y`, `phi`, the null/`pi`-flip controls, and a
  widefield phase-slope law.
- [`docs/SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md)
  — supplies wavefield-mechanism context. Cited as source-candidate
  motivation for the spatial phase-ramp readout; this note does not
  ratify its audit status.
- [`docs/SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md)
  — supplies source-resolved wavefield context. Cited as source-candidate
  motivation; not a validated NV-coupling theorem.
- [`docs/CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md`](CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md)
  — supplies complex-action carryover context used as motivation for a
  scalar-coupling phase / absorption crossover.
- [`docs/CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md)
  — sibling complex-action grown-companion note, cited as source-candidate
  context.
- [`docs/PROPAGATOR_FAMILY_UNIFICATION_NOTE.md`](PROPAGATOR_FAMILY_UNIFICATION_NOTE.md)
  — propagator-family context; keeps the claim surface narrow ("same
  transport skeleton, different scalar coupling"). It is not a closure.
- [`docs/DIAMOND_SENSOR_PROTOCOL_NOTE.md`](DIAMOND_SENSOR_PROTOCOL_NOTE.md)
  — sibling discriminator protocol; itself bounded and not a closed
  NV prediction.
- [`docs/DIAMOND_SENSOR_PREDICTION_NOTE.md`](DIAMOND_SENSOR_PREDICTION_NOTE.md)
  — sibling discriminator prediction; itself bounded and not a closed
  NV prediction.

**In-note class-B content (what survives at this scope):**

- a discriminator card naming the lock-in observables `X`, `Y`,
  `phi = atan2(Y, X)`, and the widefield spatial phase profile;
- a qualitative ordering: standard quasi-static null gives `Y ~ 0`,
  `phi ~ 0`, flat phase, while a finite-delay / wave-like coupling
  gives `Y != 0`, `phi != 0`, and a coherent spatial phase ramp that
  strengthens with drive frequency and source-detector separation;
- a minimal control stack (drive off; source retracted; `pi`
  reference flip; static-source baseline) and a pre-experiment
  validation step (run the same lock-in pipeline on a known magnetic
  or strain source first);
- a narrow narrative reading of the cited authorities: the wavefield
  lane gives the phase-ramp motivation; the complex-action lanes show
  that a scalar coupling can deform the same propagator into a phase /
  absorption crossover; the propagator-family note keeps the claim
  surface narrow at "same transport skeleton, different scalar
  coupling"; the sibling diamond protocol / prediction notes already
  apply the ideal detector theorem to map that structure onto lock-in
  observables.

These are class-B / class-A consequences of the ideal detector theorem and
the cited upstream phase-ramp / complex-action source-candidate context.
They are **not** a source-to-NV coupling derivation and **not** a calibrated
absolute amplitude budget.

**Admitted-context derivation gap (real, not import-redirect):**

The note **does not** derive any of:

1. a validated mapping from the cited source-candidate proxies to a real
   NV sensor coupling strength;
2. a calibrated absolute signal budget for a specific NV lab geometry
   that would convert the qualitative ordering into a detectability
   claim;
3. a source geometry that is already tied to a specific lab setup;
4. a lab-specific noise-floor estimate.

The detector-map bridge is now explicit and executable, but the remaining
items above are **real D-class derivation gaps**, not dependency-citation
issues. The "signal budget" in the note title refers to the
**qualitative ordering structure**
(drive band × separation, and ordering of `Y`, `phi`, ramp slope), not
to a calibrated absolute amplitude budget.

## What should be measured

Measure the standard lock-in channels:

- `X`: in-phase response
- `Y`: quadrature response
- `phi = atan2(Y, X)`: phase lag

If the setup is widefield, also measure the spatial phase profile across the
NV image.

## Standard null

After calibration and static-background subtraction, the quasi-static /
instantaneous baseline should give:

- `Y ≈ 0`
- `phi ≈ 0`
- no stable spatial phase ramp

That is the null the protocol is built around.

## Discriminator-design expectation (scope-bounded)

Using the ideal detector theorem and conditional on the cited upstream
phase-sensitive / retarded / wavefield source-candidate context above, the
discriminator-design expectation is:

- a nonzero quadrature channel `Y`
- a nonzero phase lag `phi`
- in widefield readout, a coherent spatial phase ramp
- stronger phase-sensitive response as source-detector separation increases
  and as the drive moves away from the quasi-static limit

This is the **qualitative ordering** the discriminator card is built
around. It is **not** a calibrated NV detectability claim; the
validated NV-coupling map and absolute amplitude budget remain open.

## Minimal control stack

Use the smallest control set that distinguishes signal from instrument lag:

1. drive off
2. source retracted far enough that coupling should be negligible
3. same drive with a `pi` reference flip, to verify the quadrature sign
4. static source / no modulation, to remove DC or slow drift backgrounds

If the lab wants one extra validation step, run the same lock-in pipeline on a
known magnetic or strain source first.

## What in-repo evidence motivates this discriminator card

This note is motivated by the cited upstream context and the ideal detector
theorem, not by lab-budgeted amplitude estimates:

- [`docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)
- [`docs/SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md)
- [`docs/SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md)
- [`docs/CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md`](CLAUDE_COMPLEX_ACTION_CARRYOVER_NOTE.md)
- [`docs/CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md`](CLAUDE_COMPLEX_ACTION_GROWN_COMPANION_NOTE.md)
- [`docs/PROPAGATOR_FAMILY_UNIFICATION_NOTE.md`](PROPAGATOR_FAMILY_UNIFICATION_NOTE.md)
- [`docs/DIAMOND_SENSOR_PROTOCOL_NOTE.md`](DIAMOND_SENSOR_PROTOCOL_NOTE.md)
- [`docs/DIAMOND_SENSOR_PREDICTION_NOTE.md`](DIAMOND_SENSOR_PREDICTION_NOTE.md)

The narrative reading of the cited evidence (qualitative motivation,
not a closed bridge):

- the wavefield lane gives the phase-ramp motivation
- the complex-action lanes show that a scalar coupling can deform the same
  propagator into a phase / absorption crossover
- the propagator-family note keeps the claim surface narrow: same transport
  skeleton, different scalar coupling
- the sibling diamond protocol / prediction notes already map that
  structure onto an NV lock-in readout

This narrative is **not** a source-to-lab derivation. The ideal detector
map is supplied, but the bridge from source-candidate proxy fields to a real
NV coupling and calibrated lab units remains the open D-class theorem
target.

## What remains unknown

Before contacting a lab, the repo still does **not** provide:

- a calibrated absolute signal budget
- a source geometry that is already tied to a specific lab setup
- a lab-specific noise-floor estimate
- a validated mapping from the source-candidate proxy fields to a real NV
  sensor coupling strength

So the claim surface stays narrow:

- phase-quadrature discriminator: yes
- coherent spatial phase ramp: yes
- absolute gravity detectability: not yet budgeted here

## What would count as a hit

- `Y` survives calibration and is not consistent with zero
- the sign of `Y` flips under the reference `pi` control
- a widefield image shows a stable nonzero phase gradient
- the phase signal strengthens in the expected causal direction with
  separation / drive changes

## What would count as a miss

- the quadrature vanishes after calibration
- the phase is flat across the image
- the signal is explained entirely by instrument lag, heating, or a trivial
  amplitude rescaling

## Final verdict (scope-bounded)

**Bounded experiment-facing discriminator card; not a closed signal
budget.**

Using the ideal detector theorem and conditional on the cited upstream
phase-sensitive / retarded / wavefield / complex-action source-candidate
context and the sibling diamond protocol / prediction notes, this row
records:

- a discriminator card naming `X`, `Y`, `phi`, and the spatial phase
  profile;
- a qualitative ordering with drive frequency / separation and a
  minimal control stack;
- a narrative reading of the cited evidence at the proxy / structural
  level only.

It is **not** a closed lab signal budget, **not** a calibrated NV
detectability claim, and **not** a derivation of the cited upstream
source candidates. The "signal budget" terminology refers to the
qualitative ordering structure, not to a calibrated absolute amplitude
budget. The validated NV-coupling map and absolute signal budget remain
open.

## Repair target

The ideal detector map to lock-in observables `X`, `Y`, `phi`, controls,
and the spatial phase profile is now supplied by
`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`. The remaining
repair target is the physical source-to-NV coupling and calibrated
amplitude/noise bridge; this note still exposes only the qualitative
ordering and discriminator card.

## Repo-canonical vocabulary

Terminology used in this note matches the repo-canonical vocabulary:
"diamond NV", "phase ramp", "signal budget", "prediction", "protocol",
"lock-in quadrature `Y`", "phase lag `phi`", "spatial phase profile".
No new tags, no new classes, no parent-framing cross-references
implying a class, no status promotion language.
