# Handoff

This PR repairs the highest-load audited conditional row by making the
Kawamoto-Smit theorem surface proof-exact.

What changed:

- `BlockT1` / substep-1 statistics is no longer a theorem premise.
- B1 is explicitly downstream realization context for full-gate consumers.
- The runner prints that B1 is `CONTEXT (not theorem premise)`.
- The paired cache was refreshed.

Local regenerated citation graph check shows this row's dependencies reduce to
the retained Cl(3) per-site uniqueness and retained fermion-parity rows. No
generated audit data is committed.
