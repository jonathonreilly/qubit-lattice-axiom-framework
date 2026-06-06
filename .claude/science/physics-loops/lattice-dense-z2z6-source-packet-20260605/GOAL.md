# Goal

Repair the audit blocker for
`lattice_3d_dense_spent_delay_z2_z6_endpoint_note_2026-05-29` by exposing the
transitive dense-lattice helper source and paired caches that the endpoint
runner uses.

This loop does not attempt to change the audit ledger. The target outcome is a
reviewable source-packet repair PR that lets the independent audit lane decide
whether the bounded finite `z=2..6` endpoint packet is now complete.
