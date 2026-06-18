# Summary

This PR removes an imported math step from the newly audited-conditional flavor
holonomy no-go by proving the character-suppression kernel on the retained
finite link surface.

It does not close the parent row. The physical sector-to-representation/readout
bridge remains open.

# Science Movement

- Adds a finite kernel theorem for `r_R = r0 * |chi_R(U)/d_R|^2 <= r0`.
- Proves the character bound via
  `d^2 - |sum z_i|^2 = sum_{i<j}|z_i-z_j|^2 >= 0`.
- Adds a runner/cache checking dependency status, fibre averaging, the
  non-enhancement bound, free `r0` propagation, and parent-row firewalls.
- Wires the parent holonomy no-go to cite the kernel while preserving the open
  physical sector-readout bridge.

# Checks

```bash
python3 -m py_compile scripts/flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.py
python3 scripts/flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.py
python3 scripts/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.py
git diff --check
```

All checks passed locally.

# Review

Review-loop not run; user delegated review-loop and landing cleanup to Codex
reviewer.
