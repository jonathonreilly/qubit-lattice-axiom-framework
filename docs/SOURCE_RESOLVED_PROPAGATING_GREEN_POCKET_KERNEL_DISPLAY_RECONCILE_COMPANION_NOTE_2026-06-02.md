# Source-Resolved Propagating Green Pocket -- Kernel Display Reconciliation

**Date:** 2026-06-02
**Claim type:** meta
**Review boundary:** source-note candidate. Later independent review sets the
ledger state; this note does not set or predict it.
**Primary runner:** [`scripts/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.py`](../scripts/audit_companion_source_resolved_propagating_green_pocket_kernel_display_reconcile.py)

## Purpose

This companion reconciles a display convention in
[`SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md`](SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md).
The parent note displays the Green-kernel family as

```text
K_disp(d) = exp(-mu d)/(d + eps),
```

while the registered runner evaluates

```text
K_exec(d) = exp(-mu (d + eps))/(d + eps).
```

These are not the same unscaled kernel. They differ by the constant factor

```text
K_exec(d) = exp(-mu eps) K_disp(d),
```

independent of distance. The parent runner calibrates the field by

```text
gain = FIELD_TARGET_MAX / max_abs(raw_field),
```

so the same constant factor cancels exactly in the calibrated field.

## Cancellation

Let `c = exp(-mu eps)`. For every layer and site,

```text
raw_exec = c raw_disp.
```

Therefore

```text
max_abs(raw_exec) = c max_abs(raw_disp),
gain_exec = gain_disp / c,
gain_exec raw_exec = gain_disp raw_disp.
```

The Green field actually passed into the propagator is therefore identical under
both display conventions.

The propagating Green field is built by the linear recurrence

```text
prop[0] = green[0],
prop[layer] = mix prop[layer-1] + (1 - mix) green[layer].
```

Linearity preserves the same identity after calibration. The instantaneous
control field uses a separate kernel and is not affected by this Green-kernel
display choice.

## Verified Surface

The verifier instantiates the parent finite packet:

- `h = 0.5`, `W = 3`, `L = 20`;
- four in-bounds clipped cross-source nodes;
- `s in {0.001, 0.002, 0.004, 0.008}`;
- `mix = 0.9`, `FIELD_TARGET_MAX = 0.02`;
- `mu = 0.08`, `eps = 0.5`.

It checks:

- pointwise factor identity `K_exec/K_disp = exp(-mu eps)`;
- calibrated Green-field equality;
- calibrated propagating-Green-field equality;
- equality of the parent observables across the two conventions;
- reproduction of the parent frozen table ranges under the executed convention.

## Boundaries

This companion does not edit the parent note or parent runner, does not change
any parent generated state, and does not introduce new physics. It records that
the displayed and executed Green-kernel conventions are equivalent only after
the parent runner's self-consistent gain calibration. Without that calibration
they are distinct unscaled kernels.

Whether the parent display should be changed to the executed convention is a
separate source-edit question.
