# Handoff

This branch repairs the source-side blocker for
`gauge_vacuum_plaquette_tensor_transfer_perron_solve_note`.

What changed:

- The gauge Perron runner now reconstructs the all-forward `L_s=2` PBC cube
  graph internally.
- It computes the Schur rho from the same Bessel coefficients used by the rest
  of the note and verifies `P_Schur,L2(6)=0.429104996947`.
- The note no longer imports that finite Schur value from a sibling SU3 row.

What remains open:

- The physical 3D spatial Wilson environment rho.
- The untruncated tensor-transfer Perron solve.
- The thermodynamic/canonical plaquette value.

Recommended reviewer action:

1. Inspect the finite graph/rho/Perron subcheck in
   `scripts/frontier_gauge_vacuum_plaquette_tensor_transfer_perron_solve.py`.
2. Confirm the note's boundary does not overclaim physical plaquette closure.
3. If accepted, queue the row for re-audit; do not apply an audit verdict in
   this PR.
