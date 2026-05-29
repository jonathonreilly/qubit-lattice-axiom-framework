# Handoff

This is a clean replacement for the older broad gravitational-wave scope PR.
It should be reviewed as a narrow artifact repair, not as a physical GR claim.

What changed:

- The source note now states the exact bounded toy-lattice claim.
- The runner output no longer promotes imposed retarded sampling or imposed
  `f^2` action as derived PN/GW physics.
- The primary runner source includes complete Test B and Test C implementations.
- The runner cache is refreshed from the changed source.
- The audit pipeline queues the row for independent audit.

Audit surface:

```text
claim_id: gravitational_wave_probe_note
audit_status: unaudited
effective_status: unaudited
ready: true
deps: []
open_dependency_paths: []
runner_path: scripts/frontier_grav_wave_post_newtonian.py
```

Remaining blocker:

- A separate retained bridge is still needed before citing physical PN/GW
  observables.
