# Handoff

Branch: `physics-loop/finite-scout-live-packets-20260608`

Target claims:

- `lattice_3d_dense_spent_delay_note`
- `critical_exponents_topology_note_2026-04-10`

What changed:

- Added a live dense spent-delay note narrowed to the runner's `z=2..5` card.
- Added a live critical-exponents finite-scout note matching the runner's current fit/degenerate labels.
- Did not edit runners or audit outputs.

Verification:

```text
python3 scripts/cached_runner_output.py --check-only scripts/lattice_3d_dense_10prop.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_critical_exponents.py
```

Both caches report fresh; critical-exponents runner records `ASSERTIONS: PASS`.

Remaining boundary:

No `z=6` endpoint, asymptotic distance law, universality class, or continuum
critical exponent is claimed.
