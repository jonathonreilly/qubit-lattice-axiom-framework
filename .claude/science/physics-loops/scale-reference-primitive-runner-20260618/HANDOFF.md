# Handoff

This branch makes `scale_reference_primitive` audit-ready by adding a primary
source-boundary runner and SHA-pinned cache. The runner checks the already
recorded owner approval, registry binding, Tier-A non-target classification,
no-laundering clauses, and axiom-premise purity guard.

What this does not do:

- It does not audit `scale_reference_primitive`.
- It does not retag the ledger or effective-status outputs.
- It does not add a new axiom or primitive.
- It does not derive `a/l_P = 1`.
- It does not supply any dimensionless physics.

Reviewer extraction path: keep the source note runner pointer, runner, and
cache together. The loop pack can be retained or dropped at reviewer discretion.

Next exact action after this PR: target the new YT conditional carrier bridge,
or add a similar boundary runner for the high-load `minimal_axioms` meta row.
