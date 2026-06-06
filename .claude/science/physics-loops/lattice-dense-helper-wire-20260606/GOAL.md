# Goal

Repair the helper-source artifact blocker for
`lattice_3d_dense_spent_delay_z2_z6_endpoint_note_2026-05-29`.

The audited conditional row requested the full
`scripts/lattice_3d_dense_10prop.py` helper source in the restricted packet and
`helper_runner_paths` detection. Current main already exposes the helper source
in prose and has a source-packet verifier, but the endpoint runner used an
import form missed by `scripts/audit_packet_script_deps.py`, and the verifier
cache was absent. This branch makes the helper detectable and cache-addressable.

