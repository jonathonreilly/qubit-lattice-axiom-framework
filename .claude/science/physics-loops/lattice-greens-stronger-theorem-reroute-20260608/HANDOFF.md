# Handoff

This PR repairs `lattice_greens_1_over_r_from_heat_kernel_resolvent_theorem_note_2026-06-07`.

Science change:

- The exact A1 heat-kernel resolvent identity remains the row's own result.
- The direct local-CLT proof route remains open as alternate math.
- The leading `1/(4 pi r)` asymptotic is now routed through the stronger native
  lattice-correction theorem for the same kernel.
- The runner verifies the stronger theorem note, SHA-fresh cache, and expansion
  signal.
- Physical `G_Newton` calibration remains excluded.

Verification:

```text
python3 scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
python3 -m py_compile scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
git diff --name-only -- docs/audit
```

No audit files are modified.
