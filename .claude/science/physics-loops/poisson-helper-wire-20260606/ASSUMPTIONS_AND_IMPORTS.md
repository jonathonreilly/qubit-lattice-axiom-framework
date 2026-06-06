# Assumptions And Imports

Load-bearing machinery:

- Existing live finite Poisson packet runner
  `scripts/backreaction_poisson_live_threshold_check.py`.
- Existing helper source `scripts/backreaction_poisson.py`.
- Source-packet verifier
  `scripts/backreaction_poisson_live_threshold_source_packet_manifest_2026_06_04.py`.

Imports retired or reduced:

- The helper-source packet import is retired by the scanner-detected static
  import `import scripts.backreaction_poisson as bp`, a fresh primary cache, a
  fresh source-packet verifier cache, and updated verifier JSON.

