# Goal

Repair the source-resolved Green-kernel artifact mismatch for:

- `source_resolved_exact_green_pocket_note`
- `source_resolved_propagating_green_pocket_note`

The auditor-specified repair target is to reconcile the Green-kernel definition
across source notes, runner print strings, executable code, and cached output.

This branch keeps the executable convention and makes it explicit:

```text
rho_eps = sqrt(dx^2+dy^2+dz^2) + eps
kernel = exp(-mu rho_eps) / rho_eps
```

No continuum Green theorem, size-transfer theorem, or retained dynamics
derivation is claimed.
