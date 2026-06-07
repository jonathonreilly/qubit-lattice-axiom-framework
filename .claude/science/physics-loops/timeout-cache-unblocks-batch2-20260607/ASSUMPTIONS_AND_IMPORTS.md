# Assumptions And Imports

No new science premise is introduced.

The L2 tail repair relies on the existing frozen log
`logs/2026-04-04-lattice-3d-l2-tail-stats.txt`, because the source note's
post-2026-05-18 narrowed claim is explicitly the width-8 frozen-log table and
post-peak fit. The default runner now verifies that log and recomputes the
tail fit from the logged centroids. Full recomputation remains available with
`--recompute`, but it is not used as the default audit artifact.

The FM-transfer and persistent-record repairs add only `AUDIT_TIMEOUT_SEC`
declarations and refreshed SHA-pinned caches. Their numerical logic is
unchanged.
