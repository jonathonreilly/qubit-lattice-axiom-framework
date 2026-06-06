# Assumptions And Imports

Load-bearing machinery:

- Existing dense spent-delay endpoint runner
  `scripts/lattice_3d_dense_z2_z6_endpoint_check.py`.
- Existing dense helper source `scripts/lattice_3d_dense_10prop.py`.
- Source-packet verifier
  `scripts/lattice_3d_dense_z2_z6_endpoint_source_packet_manifest_2026_06_05.py`.

Imports retired or reduced:

- The helper-source packet import is retired by the scanner-detected static
  import `import scripts.lattice_3d_dense_10prop as dense`, a fresh endpoint
  cache, and a fresh source-packet verifier cache.

