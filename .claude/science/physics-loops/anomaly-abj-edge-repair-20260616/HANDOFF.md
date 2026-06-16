# Handoff

This PR repairs the critical anomaly-forces-time ABJ bridge source packet.

The source note now exposes the actual dependency shape on current `main`:
nonabelian gauge closure and the bounded abelian surface are framework-side
inputs; `P-HY`, `P-COMP`, `P-REC`, and `P-ABJ/P1` are declared premise edges;
`B-AXIS` belongs only to the parent theorem's `d_t = 1` cap. The runner checks
that shape and the exact rational anomaly arithmetic, and now passes
`SUMMARY` equivalent `PASS=76 FAIL=0`.

No audit files are edited. Independent audit owns any status change.

PR: pending

Next exact action after PR creation: patch this file and `STATE.yaml` with the
PR URL, then push the metadata update.
