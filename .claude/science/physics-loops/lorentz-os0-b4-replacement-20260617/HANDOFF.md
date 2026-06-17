# Handoff

Branch: `physics-loop/lorentz-os0-b4-replacement-20260617`

This source-side PR adds an exact-support OS0 replacement bridge for marginal
velocity protection. It should help the audit/review loop avoid treating the
older supplied one-loop RG packet as load-bearing for OS0 downstream uses.

Reviewer extraction guidance:

- keep the old interacting velocity RG row conditional;
- use the new bridge only for OS0 marginal-velocity protection;
- do not treat this as physical Lorentz closure, non-OS0 closure, or a bound
  comparison;
- audit/review owns any status propagation.

Verification to run:

```bash
python3 scripts/cached_runner_output.py --refresh scripts/frontier_emergent_lorentz_os0_b4_replacement_bridge_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_emergent_lorentz_os0_b4_replacement_bridge_2026_06_17.py
python3 scripts/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.py
python3 -m py_compile scripts/frontier_emergent_lorentz_os0_b4_replacement_bridge_2026_06_17.py scripts/frontier_emergent_lorentz_interacting_velocity_rg_attractor_2026_06_06.py
git diff --check
```

Local result before PR: all commands passed; new verifier reports
`TOTAL: PASS=15 FAIL=0`, and the old interacting runner still reports
`TOTAL: PASS=18 FAIL=0`.
