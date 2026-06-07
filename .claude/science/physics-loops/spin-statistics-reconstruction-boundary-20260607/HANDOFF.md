# Handoff

This branch repairs the source packet for
`flavor_spin_statistics_forces_modulo_reconstruction_2026-05-31`.

Changed:

- replaced current-surface "forced modulo R" language with bounded route
  pruning;
- preserved the genuine finite T1 engine and taste-spectator checks;
- added a source-boundary guard so the runner fails if P1 forcing is promoted
  without `R`.

Verification:

```bash
PYTHONPATH=scripts python3 scripts/flavor_spin_statistics_forces_modulo_reconstruction_2026_05_31.py
```

Result: `SCORECARD PASS=7 FAIL=0`.

Remaining blockers:

- non-circular `R`;
- bare-qubit boost-spinor embedding independent of a chosen Grassmann/staggered
  fermion frame.

No `docs/audit/**` files are modified.
