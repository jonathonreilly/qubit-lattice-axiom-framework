# Handoff

This PR is a source-side audit unlock for the 13 uncovered conditional rows.
The reviewer should not merge generated audit results from this branch; none
are staged intentionally.

Important science change:

- The Planck-time row now consumes the current companion tick/edge row at its
  graph/count scope, because current main has that companion as
  `audited_clean` / `retained_bounded`. The remaining boundary is physical
  `c` normalization, explicitly not a derived dynamics theorem in this packet.

Local pipeline effect before restoring generated files:

- 13 target rows became `audit_status=unaudited`, `effective_status=unaudited`,
  and `ready=true`.
- Overall simulated `audited_conditional` count fell from 52 to 39.

Review focus:

- confirm no residual certificate overpromotes a hard bridge;
- confirm the Planck-time dependency-state repair is faithful to the current
  companion claim scope;
- hand the ready rows to the independent audit loop.
