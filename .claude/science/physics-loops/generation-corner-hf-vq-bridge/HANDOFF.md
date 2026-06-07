# Handoff

## What This PR Does

Adds a finite periodic screened-Poisson/Hartree-Fock source bridge for the audited conditional
generation-corner `delta_ij` target.

The bridge proves, on `Lambda_L=(Z/LZ)^3`, that:

- normalized translation characters diagonalize the periodic graph Laplacian;
- `-G(Lap+mu^2 I)^-1` has multiplier `Vq(q)=-G/(eps(q)+mu^2)`;
- the two-corner Slater Hartree-minus-exchange mutual energy is
  `(Vq(0)-Vq(k_i-k_j))/N`;
- for the three `hw=1` corners every pair has `eps(Delta k)=8`, so the pair coupling is equal
  and negative for `G>0, mu^2>0`.

## What It Does Not Do

- It does not edit audit results.
- It does not mark the target retained.
- It does not widen the retained bounded open-cubic mediator to a universal periodic physical
  mediator theorem.
- It does not close the physical flavor magnitude or IR completion.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.py
PYTHONPATH=scripts python3 scripts/generation_localization_corner_protected_delta_runner.py
```

Observed:

- Bridge runner: `PASS=16 FAIL=0`.
- Target runner: `PASS=13 FAIL=0`.

## Reviewer Ask

Review whether the one-hop bridge is acceptable exact support for re-auditing
`generation_localization_momentum_corner_delta_ji_protected_narrow_theorem_note_2026-06-06`.
If accepted, the independent audit lane can decide the target's actual verdict.

PR URL: pending.
