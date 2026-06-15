# Handoff

This PR targets `teleportation_resource_from_poisson_note`.

It wires two existing candidate packets into the audited row:

- `TELEPORTATION_MICROSCOPIC_CLOSURE_NOTE.md`
- `TELEPORTATION_APPARATUS_DYNAMICS_CLOSURE_NOTE.md`

The target runner now verifies the row cites those packets, the packets retain
their bounded apparatus/readout gates, and the row still refuses retained/status
promotion. The remaining open items are resource preparation beyond offline
diagonalization, uniqueness from the framework axioms, detector scaling, and
independent audit acceptance.

Verification:

```bash
python3 scripts/frontier_teleportation_resource_from_poisson.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_teleportation_resource_from_poisson.py --tail-chars 12000
python3 scripts/cached_runner_output.py --check-only scripts/frontier_teleportation_microscopic_closure.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_teleportation_apparatus_dynamics_closure.py
```
