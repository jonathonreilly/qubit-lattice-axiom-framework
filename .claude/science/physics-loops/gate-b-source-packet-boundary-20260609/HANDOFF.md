# Gate B Source-Packet Boundary Handoff

This branch repairs the Gate B conditional audit blocker by explicitly
registering the three row-local supplied ingredients:

- `GB-S1` valley-linear source/action rule;
- `GB-S2` propagation/readout semantics;
- `GB-S3` generated-connectivity rule.

The branch does not claim retained Gate B dynamics. It makes the current source
packet audit-visible and adds a runner gate that fails if the manifest or
status boundary is removed.

Verification planned:

```bash
python3 scripts/gate_b_connectivity_tolerance.py
python3 scripts/cached_runner_output.py scripts/gate_b_connectivity_tolerance.py
python3 -m py_compile scripts/gate_b_connectivity_tolerance.py
```
