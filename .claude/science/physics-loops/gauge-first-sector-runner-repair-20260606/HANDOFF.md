# Handoff

## Summary

This branch restores two missing gauge-vacuum first-sector runner paths named
by audit blockers.

## Rank-One Boundary Runner

Path:
`scripts/frontier_gauge_vacuum_plaquette_first_sector_rank_one_factorized_class_boundary_2026_04_19.py`

Key checks:

- `E_3 v_min = Z_min` to numerical precision.
- `T_min^3 e_0 = v_min` to numerical precision.
- `D_back = M^-1 T_min M^-1` is unique because `M = exp(3J)` is invertible.
- `||offdiag(D_back)||_F = 0.250338180104`, so the unique pullback is not
  diagonal.
- Positive conjugation-symmetric diagonal-family search reproduces
  `||a(D)-v_min|| = 0.135462193873` and sample residual `0.228465894557`.

## Tail Underdetermination Runner

Path:
`scripts/frontier_gauge_vacuum_plaquette_first_sector_tail_underdetermination_theorem_2026_04_19.py`

Key checks:

- Zero extension and explicit exponentially decaying positive tail extension
  agree exactly on the retained four-weight packet.
- Both reproduce `Z_min` on the retained projection.
- Both factorized-class transfers are self-adjoint, conjugation-symmetric, and
  positive semidefinite on the truncated box.
- The same source operator `J` gives different Perron/Jacobi packets:
  `m1` gap `2.606e-04`, `m2` gap `2.399e-04`, `alpha0` gap `2.606e-04`,
  and `beta1` gap `3.019e-05`.

## Reviewer Notes

- No `docs/audit/**` files are changed.
- No framework axiom is introduced.
- No source-note or publication surface is retagged.
- If accepted, the reviewer/auditor can queue the two target rows for
  re-audit because their named runner paths now exist and pass.

## Next Exact Action

After this PR is opened, refresh the current audit backlog on main and search
for the next missing-runner or conditional row where the blocker names a
repairable executable artifact.
