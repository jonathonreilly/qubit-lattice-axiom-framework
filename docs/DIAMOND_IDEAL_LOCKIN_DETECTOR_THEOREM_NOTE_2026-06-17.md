# Diamond Ideal Lock-In Detector Theorem Note

**Date:** 2026-06-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded support theorem for the ideal detector map only; not an
NV signal-budget claim and not a source-dynamics closure.
**Status authority:** independent audit lane only.

## Purpose

The Diamond/NV handoff notes had a real bridge gap: they named lock-in
observables `X`, `Y`, `phi = atan2(Y, X)`, and a widefield phase ramp, but
they did not isolate the ideal detector theorem that maps a delayed driven
source history into those observables.

This note closes only that mathematical detector-map step.
It does not derive the delayed source field from the framework, does not map a
repo proxy field into an NV Hamiltonian, and does not supply a calibrated
absolute amplitude or lab noise budget.

## Ideal Detector Setup

Fix one driven scalar signal at detector pixel `z`,

```text
signal_z(t) = A_z cos(omega * (t - tau_z)).
```

The ideal lock-in detector has:

- perfect phase reference;
- integer-cycle integration;
- no noise floor;
- no finite bandwidth or spectral leakage;
- no NV transfer coefficient.

Define the cycle-averaged lock-in channels

```text
X_z = 2 <signal_z(t) cos(omega t)>
Y_z = 2 <signal_z(t) sin(omega t)>,
```

where `<...>` is the average over an integer number of drive cycles.

## Theorem

For the ideal detector above,

```text
X_z = A_z cos(omega tau_z)
Y_z = A_z sin(omega tau_z)
phi_z = atan2(Y_z, X_z) = omega tau_z mod 2*pi.
```

If the widefield delay is locally affine,

```text
tau_z = tau_0 + kappa z,
```

and the phases are unwrapped on a window with no branch crossing, then the
spatial phase profile is linear and

```text
d phi / dz = omega kappa.
```

The same calculation gives the built-in controls:

- drive off or source retracted (`A_z = 0`) gives `X_z = Y_z = 0`;
- a static source has zero AC lock-in channel over integer cycles;
- a `pi` reference flip changes the sign of both `X_z` and `Y_z`.

## Runner

The runner
[`scripts/diamond_ideal_lockin_detector_theorem.py`](../scripts/diamond_ideal_lockin_detector_theorem.py)
applies the definitions directly. It numerically integrates the lock-in
channels over whole drive cycles and compares them with the closed formulas
above. It also checks the drive-off/static controls, the `pi` reference flip,
and the widefield phase-slope law.

Representative runner output:

```text
DIAMOND IDEAL LOCK-IN DETECTOR THEOREM
ASSERTIONS: PASS
```

The SHA-pinned cache is
[`logs/runner-cache/diamond_ideal_lockin_detector_theorem.txt`](../logs/runner-cache/diamond_ideal_lockin_detector_theorem.txt).

## Assumption and Import Boundary

| Item | Role | Class | Load-bearing? | Disposition |
| --- | --- | --- | --- | --- |
| delayed sinusoidal source history `A_z cos(omega(t - tau_z))` | input to the ideal detector theorem | admitted detector-test input | yes, for this bounded theorem only | not a framework source derivation |
| integer-cycle lock-in averages | detector definition | framework-external lab idealization | yes | explicitly scoped to ideal detector |
| trigonometric cycle averages | evaluated by the runner from the definitions | framework-applied math | yes | no textbook import is load-bearing |
| NV transfer coefficient / Hamiltonian coupling | physical lab calibration | open import | no, excluded from this theorem | remains outside scope |
| absolute amplitude / noise floor | detectability budget | open import | no, excluded from this theorem | remains outside scope |

No new axiom is introduced. The theorem is a bounded support tool for
detector readout semantics, not a retained source-to-lab prediction.

## Downstream Use

The Diamond sensor prediction, protocol, phase-ramp, and absolute-unit notes
may cite this note for the narrow statement:

```text
a delayed driven source has ideal lock-in channels X, Y, phi and a widefield
phase slope as written above.
```

They may not cite it for:

- derivation of the delayed source from `Cl(3)` on `Z^3`;
- validated coupling from a repo proxy field into an NV center;
- absolute NV counts, volts, sensitivity, or detectability;
- a claim that the standard quasi-static null is experimentally beaten.

## Final Verdict

The ideal detector bridge is now explicit and executable:

- `X`, `Y`, and `phi` follow from the cycle-average definitions;
- the widefield phase-ramp slope is `omega kappa` on the affine-delay window;
- the null, static, and `pi`-flip controls are checked.

The remaining Diamond/NV blockers are downstream physical bridges: the
source-to-field/source-to-NV coupling map and the absolute lab calibration.
