# Assumptions And Imports

No new axiom, Tier-A admission, observation, or fitted value is introduced.

Inputs consumed:

- `docs/LATTICE_3D_INVERSE_SQUARE_KERNEL_HELPER_NOTE_2026-04-04.md` as the
  existing wrapper note under audit.
- `scripts/lattice_3d_inverse_square_kernel.py` as the helper implementation
  named by the note and audit guidance.
- `logs/runner-cache/lattice_3d_inverse_square_kernel.txt` as the SHA-pinned
  zero-exit output of the existing helper runner.

The new verifier checks implementation fidelity only. It does not derive the
inverse-square branch from retained framework primitives and does not promote
downstream tail-statistics claims.

