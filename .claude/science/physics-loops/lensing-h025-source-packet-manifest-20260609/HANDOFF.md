# Handoff

Branch: `physics-loop/lensing-h025-source-packet-manifest-20260609`

Target claim:
`lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07`

What changed:

- Added `scripts/frontier_lensing_h025_source_packet_manifest_2026_06_09.py`.
- The manifest recursively lists local helper scripts for the H=0.25 edge-kernel
  certificate.
- It checks the heavy H=0.25 runner cache is fresh and SHA-pinned.
- It checks the source fine-H slope certificate and structured edge-kernel JSON
  output are present and coherent.
- The source note now links the manifest runner/cache.

Verification:

```text
python3 scripts/frontier_lensing_h025_source_packet_manifest_2026_06_09.py
TOTAL: PASS=5 FAIL=0

python3 scripts/cached_runner_output.py scripts/frontier_lensing_h025_source_packet_manifest_2026_06_09.py
status: ok
```

Remaining boundary:

The exact signed-tail asymptotic order remains open. This branch only closes the
fine-H source-packet artifact gap.

Next action:

Open a PR for reviewer extraction and independent re-audit. Do not edit
`docs/audit/**`.
