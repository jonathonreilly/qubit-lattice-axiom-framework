# Summary

This PR partially unlocks the audited-conditional gauge parent row by wiring in
already retained-bounded local-frame/minimal-coupling kinematics for the
link-transporter/lattice-connection boundary.

It does not promote the parent row. It explicitly leaves open `MR_color`,
factor-locality, factorwise subgroup selection over `u(6)`/conjugates, chiral
`su(2)_L`, and gauge dynamics/couplings/continuum.

# Science Movement

- Replaces the old unstructured link-connection convention with a narrow
  retained-bounded kinematic bridge from:
  - `FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md`
  - `MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md`
- Adds a source firewall runner checking that the parent note consumes only
  that kinematic bridge and does not close the carrier/gauging/chirality
  blockers.
- Adds a cached runner output and physics-loop handoff pack.

# Checks

```bash
python3 -m py_compile scripts/gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.py
python3 scripts/gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/gauge_algebra_parent_kinematic_bridge_firewall_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/gauge_algebra_supplied_carrier_2026_06_08.py
python3 scripts/cached_runner_output.py --check-only scripts/gauging_selection_discriminator_open_gate_2026_06_08.py
git diff --check
```

All checks passed locally.

# Review

Review-loop not run; user delegated review-loop and landing cleanup to Codex
reviewer.
