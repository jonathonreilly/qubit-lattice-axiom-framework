# Goal

Repair `FLAVOR_FIND_J_ROUND1_JCS_MEASURE_NEUTRAL_2026-06-02` so its source
surface matches the algebra the audit already found closed.

The repaired packet keeps:

```text
static J_cs is measure-neutral and cannot select det_C
Gamma_chi is not J_cs
```

It removes the unsupported `Q` default, `det_C` readout map, and first-order
action conclusion from the claim surface.
