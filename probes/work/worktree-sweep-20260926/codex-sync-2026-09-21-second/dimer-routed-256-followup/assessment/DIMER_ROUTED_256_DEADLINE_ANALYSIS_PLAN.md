# Deadline reconciliation and descriptive analysis of the N=256 follow-up

2026-09-21, before root aggregate access to any N=256 fields. The sixteen
seeds, geometry fixtures, two-process concurrency, ordering and hard deadline
remain unchanged. No new trajectories or substitutions are authorized here.

Static reading of the frozen wrapper found that execute() returns a different
row shape when a job is not started at the deadline: it includes job/status,
whereas final SUMMARY sorting expects N/kind/replicate at the top level.
Consequently a run with unstarted jobs can preserve all rows in PROGRESS but
fail while writing SUMMARY. Do not edit the active frozen wrapper or its
dispatch identity. After it exits, a separate reconciler must authenticate
the frozen sources and receipts, normalize the saved row shapes, and preserve
the original failure logs. Its output is a new RECOVERY_SUMMARY, never an
overwritten or purported original SUMMARY.

The original analyzer intentionally refuses an incomplete sixteen-history
study. A separate, source-bound censored adapter may report all completed
histories descriptively, alongside every failed or unstarted declaration.
It keeps the original four observables, all three directions, all five times,
normalization, 10,000 whole-history bootstrap draws and seed202609211900.
It does not pool with the earlier N<=128 study, fit an exponent, or choose
histories from their outcomes. With fewer than two completed histories in a
geometry, standard errors and bootstrap intervals are unavailable rather
than zero. A geometry with no completed history is still listed.

Completion before a wall-clock deadline is not guaranteed to be independent
of trajectory outcomes. Intervals from the completed subset are therefore
descriptive conditional summaries, not a claim of an unbiased completed
sixteen-history experiment or a correction for censoring. The final report
must state the actual sample counts and incomplete-study status.

The preselected endpoint reconstructions remain replicate3 and replicate7
in each geometry, with no substitution if a selected history is incomplete.
Selected JSON fields may be consumed for validation after an independently
reconstructed binary endpoint is sealed; aggregate analysis waits until the
run ends. All intermediate-time fields remain authenticated outputs unless
separately reconstructed.
