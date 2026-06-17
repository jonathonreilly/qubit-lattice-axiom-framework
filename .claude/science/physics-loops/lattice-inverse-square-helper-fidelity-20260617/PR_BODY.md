## Summary

This PR supplies the source-side implementation-fidelity packet requested by the audit row for `lattice_3d_inverse_square_kernel_helper_note_2026-04-04`.

It adds a verifier that checks:

- documented width-6 comparator constants and helper functions;
- the actual inverse-square propagation expression `w / L^2`;
- preservation of the spent-delay action expression;
- SHA-current zero-exit cache for `scripts/lattice_3d_inverse_square_kernel.py`;
- the wrapper-only boundary in the source note.

This does not claim a retained inverse-square theorem, a downstream tail-law theorem, or an audit status change.

## Trace Gate

- Target: `lattice_3d_inverse_square_kernel_helper_note_2026-04-04`
- Audit hook: “Re-check with scripts/lattice_3d_inverse_square_kernel.py if the intended audit target is implementation fidelity rather than wrapper-level definitional scope.”
- Trace class: `direct_blocker_closure`
- Reachability: supports re-audit of implementation-fidelity surface only

## Checks

```bash
python3 scripts/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py
python3 scripts/cached_runner_output.py --refresh scripts/lattice_3d_inverse_square_kernel_helper_fidelity_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/lattice_3d_inverse_square_kernel.py
```

Review-loop disposition: reviewer-owned, not run locally.
