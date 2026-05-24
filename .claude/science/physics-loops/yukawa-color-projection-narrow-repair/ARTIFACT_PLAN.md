# Artifact Plan

## Source

- Replace `F_adjoint = 8/9` scoped language with `f_adj,dim = 8/9`.
- State explicitly that `F_adjoint(M)` and `R_conn` are dynamical trace ratios
  outside the row.

## Generated Audit Artifacts

- Regenerate the audit pipeline.
- Confirm the row is `unaudited`, queue rank 1, and `ready: Y`.
- Include generated effective-status publication views changed by the audit
  reset.

## Verification

- Run the Fierz runner and exact companion.
- Run the full audit pipeline and strict lint suite.
