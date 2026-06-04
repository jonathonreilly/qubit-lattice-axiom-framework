# Handoff

This branch repairs the Picard-Fuchs rank-bound row's source-packet blocker.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2613

## What Changed

- The rank-bound citation note now names a complete primary/helper source
  manifest with caches and JSON outputs.
- A new source-packet verifier confirms the note links every manifest path,
  the helper sources are untruncated and contain the load-bearing rank-matrix
  functions, and the caches are SHA-fresh.
- The all-order runner's Bostan-Salvy-Schost prose typo now says `R + D`,
  matching the code and output.

## Verification

```bash
python3 -m py_compile scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py scripts/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.py scripts/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.py
```

## Remaining Boundary

The branch should be handed to independent audit as re-audit-ready exact
support. It does not modify audit ledger results.
