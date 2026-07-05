# Diamond Sensor Protocol Note

**Date:** 2026-04-05 (audit-narrowing refresh: 2026-05-10)
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded lab-facing discriminator protocol, intentionally
bounded; **not** a closed NV prediction.
**Status authority:** independent audit lane only.
**Authority role:** records, but does not close, a bounded discriminator
protocol (lock-in `X`, `Y`, `phi`, widefield phase ramp; minimal control
stack; qualitative ordering table) for a diamond/NV collaborator. The
ideal lock-in detector map is supplied by
[`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md).
The remaining open targets are the source-to-NV coupling map and the
absolute lab amplitude/noise budget.

## Purpose

This note turns the cited phase-sensitive / retarded / wavefield lane
into a concrete **discriminator protocol** a diamond/NV collaborator
could evaluate. It is **not** a closed protocol in the sense of a
calibrated lab signal budget; the source-to-NV coupling map and the
absolute calibration are still missing.

The repo does **not** yet support a defensible absolute gravity
amplitude for an NV experiment. So the claim surface stays narrow:

- phase-quadrature discriminator design: yes
- coherent spatial phase ramp design: yes
- absolute gravity detectability: not budgeted here

## Audit boundary

This note assembles a class-B experiment-facing protocol card by combining
an explicit ideal lock-in detector theorem with upstream retarded-field /
wavefield source-candidate context. It names the corresponding lock-in
observables (`X`, `Y`, `phi = atan2(Y, X)`, widefield phase profile). It is
**not** a derivation of those upstream source candidates and **not** a
closed NV-coupling forward model.

**Cited authorities and context (one-hop deps where load-bearing; audit
effective status remains ledger-owned):**

- [`docs/DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md)
  — supplies the bounded ideal-detector map from a delayed driven source
  history to `X`, `Y`, `phi`, the `pi`-flip/null controls, and a
  widefield phase-slope law. This closes only the detector-map step.
- [`docs/RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md`](RETARDED_FIELD_CAUSALITY_PROBE_NOTE.md)
  — supplies retarded-field causality context used as
  qualitative motivation for a finite-delay phase-lag signature.
- [`docs/RETARDED_FIELD_DELAY_PROXY_NOTE.md`](RETARDED_FIELD_DELAY_PROXY_NOTE.md)
  — supplies intermediate-layer phase-lag context. Cited as
  source-candidate motivation for the qualitative ordering with drive
  frequency and separation; this note does not ratify its audit status.
- [`docs/SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md`](SOURCE_RESOLVED_WAVEFIELD_ESCALATION_NOTE.md)
  — supplies source-resolved wavefield context that motivates the spatial
  phase-ramp readout. Cited as source-candidate motivation only; not a
  validated NV-coupling theorem.

**In-note class-B content (what survives at this scope):**

- a discriminator protocol naming the lock-in observables `X`, `Y`,
  `phi`, and the widefield spatial phase profile;
- a qualitative ordering table: standard quasi-static null gives
  `Y ~ 0`, `phi ~ 0`, flat phase, while a finite-delay / wave-like
  coupling gives `Y != 0`, `phi != 0`, and a coherent spatial phase
  ramp that strengthens with drive frequency and source-detector
  separation;
- a minimal control stack (drive off; source retracted; `pi`
  reference flip; static-source baseline) and a pre-experiment
  validation step (run the same lock-in pipeline on a known magnetic
  or strain source first);
- the same qualitative content reported by
  `scripts/diamond_sensor_protocol_probe.py`, with the detector-map
  identities checked from the cycle-average definitions by
  `scripts/diamond_ideal_lockin_detector_theorem.py`.

These are class-B / class-A consequences of the ideal detector theorem,
the cited source-candidate context, and qualitative-ordering reasoning.
They are **not** a source-to-NV coupling derivation and **not** a calibrated
signal budget.

**Admitted-context derivation gap (real, not import-redirect):**

The note **does not** derive any of:

1. a validated mapping from the cited source-candidate proxies to a real
   NV sensor coupling strength;
2. a calibrated absolute signal budget for a specific NV lab geometry
   that would convert the qualitative ordering table into a
   detectability claim.

The detector-map bridge is now explicit and executable, but the remaining
items above are **real D-class derivation gaps**, not dependency-citation
issues.

## What the lab should measure

Measure the lock-in channels:

- `X`: in-phase response
- `Y`: quadrature response
- `phi = atan2(Y, X)`: phase lag

If the setup is widefield, also record the spatial phase profile across the NV
image.

## Ideal detector bridge now supplied

The ideal detector bridge is supplied by
[`DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`](DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md):

- same driven source history in every comparator
- perfect phase reference
- no noise floor
- no finite-bandwidth or spectral-leakage model
- direct output for `X`, `Y`, `phi`, and spatial phase profile

This remains the required precondition before lab-specific detector realism.
It checks source fidelity first and keeps the physics prediction
separate from detector artefacts.

## Standard null

After calibration and static-background subtraction, the quasi-static /
instantaneous Newtonian baseline should give:

- `Y ≈ 0`
- `phi ≈ 0`
- no stable spatial phase ramp

## Discriminator-design expectation (scope-bounded)

Using the ideal detector theorem and conditional on the cited upstream
retarded-field / wavefield source candidates above, the
discriminator-design expectation is:

- a nonzero quadrature channel `Y`
- a nonzero phase lag `phi`
- a coherent spatial phase ramp in widefield readout
- strengthening of the quadrature / phase signal with increasing drive
  frequency and increasing source-detector separation

This is the **qualitative ordering** the protocol card is built around.
It is **not** a calibrated NV detectability claim, since the validated
NV-coupling map and absolute amplitude budget remain open.

## Minimal control stack

Use the smallest control set that lets the collaborator tell signal from
instrument lag:

1. drive off
2. source retracted far enough that the coupling should be negligible
3. same drive with a `pi` reference flip, to verify the quadrature sign
4. static source / no modulation, to remove DC or slow drift backgrounds

If the lab wants an extra control, first run the same lock-in pipeline on a
known magnetic or strain source to validate the instrumentation.

## Suggested scan points

The repo cannot justify calibrated amplitude numbers yet, so the protocol is
expressed as an ordering table rather than a quantitative prediction table.

Suggested scan classes:

- drive frequency: low, mid, high
- source-detector separation: near, mid, far

| scan class | standard null expectation | discriminator-design expectation (under cited retarded / wavefield proxy) |
| --- | --- | --- |
| low drive, near separation | `X` dominates, `Y ~ 0`, `phi ~ 0` | weakest signal candidate; likely small or marginal |
| low drive, far separation | `X` dominates, `Y ~ 0`, `phi ~ 0` | weak phase lag if any |
| mid drive, near separation | `X` dominates, `Y ~ 0`, `phi ~ 0` | detectable `Y` is more plausible |
| mid drive, far separation | `X` dominates, `Y ~ 0`, `phi ~ 0` | stronger phase lag or quadrature than near separation |
| high drive, near separation | `X` dominates, `Y ~ 0`, `phi ~ 0` | stronger phase-sensitive response than low drive |
| high drive, far separation | `X` dominates, `Y ~ 0`, `phi ~ 0` | strongest candidate for a coherent `Y` and phase ramp |

The qualitative ordering is the key claim of the discriminator design:

- under the cited retarded / wavefield source-candidate context and the
  supplied ideal detector theorem: `Y` and `phi` should grow with drive
  frequency and separation
- standard null: `Y` stays near zero after calibration

Absolute amplitudes are **not** budgeted by this table.

## What would count as a hit

- `Y` survives calibration and is not consistent with zero
- the sign of `Y` flips under the `pi` reference control
- the phase is not flat across the image in widefield mode
- the effect strengthens in the high-drive / far-separation direction

## What would count as a miss

- quadrature vanishes after calibration
- the phase is flat across the field of view
- the signal moves only because of instrument lag, heating, or trivial
  amplitude rescaling

## Honest limitation

This repo does not yet provide a calibrated gravity amplitude for NV sensors.

So the strongest defensible lab-facing artifact is a discriminator protocol:

- ideal-detector lock-in map at bounded mathematical scope
- phase-sensitive lock-in readout
- standard quasi-static null
- sign-flip control
- optional spatial phase-ramp imaging

## Experimental framing (scope-bounded)

The cleanest phrasing for a lab contact is:

"Measure the lock-in quadrature and spatial phase profile for a driven
source near an NV sensor. The standard quasi-static baseline predicts
no stable quadrature after calibration; under the cited retarded /
wavefield source-candidate context and the ideal lock-in detector theorem,
the discriminator protocol names a nonzero phase-lag signature that
strengthens with drive frequency and source-detector separation as the
qualitative ordering signal. Absolute detectability is not budgeted by this
protocol."

## References

- NV dual-channel lock-in readout of time-dependent fields:
  [Phys. Rev. B 88, 220410](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.88.220410)
- widefield / per-pixel lock-in detection in diamond NV imaging:
  [Scientific Reports 2022](https://www.nature.com/articles/s41598-022-12609-3)
- NV strain sensitivity in diamond mechanical structures:
  [Scientific Reports 2020](https://www.nature.com/articles/s41598-020-65049-2)

## Final Verdict (scope-bounded)

**Bounded experiment-facing discriminator protocol only.**

Using the ideal detector theorem and conditional on the cited upstream
retarded-field / wavefield source-candidate context, this row records:

- a discriminator protocol naming `X`, `Y`, `phi`, and the spatial
  phase profile;
- a qualitative ordering table for drive frequency × separation under
  the same single-delay / wave-like proxy;
- a minimal control stack and a pre-experiment validation step.

It is **not** a closed lab protocol, **not** a calibrated NV detectability
claim, and **not** a derivation of the cited upstream source candidates.
The validated NV-coupling map and absolute signal budget remain open.

## Repair target

The ideal detector map deriving `X`, `Y`, `phi`, the spatial phase ramp,
and the frequency / separation ordering from a delayed driven source is now
supplied by `DIAMOND_IDEAL_LOCKIN_DETECTOR_THEOREM_NOTE_2026-06-17.md`.
The remaining repair target is the physical source-to-NV coupling and
calibrated amplitude/noise bridge; this note still exposes only the
qualitative ordering and discriminator protocol.

## Repo-canonical vocabulary

Terminology used in this note matches the repo-canonical vocabulary:
"diamond NV", "phase ramp", "signal budget", "prediction", "protocol",
"lock-in quadrature `Y`", "phase lag `phi`", "spatial phase profile".
No new tags, no new classes, no parent-framing cross-references
implying a class, no status promotion language.
