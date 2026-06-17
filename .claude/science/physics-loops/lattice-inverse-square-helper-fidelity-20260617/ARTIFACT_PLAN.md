# Artifact Plan

Artifacts:

- Update the helper note with a 2026-06-17 implementation-fidelity packet.
- Add `scripts/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py`.
- Add SHA-pinned cache output for the new verifier.
- Add this loop pack for reviewer extraction.

Checks:

- `python3 scripts/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/lattice_3d_inverse_square_kernel.py`

