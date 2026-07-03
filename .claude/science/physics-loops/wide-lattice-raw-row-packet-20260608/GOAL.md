# Goal

Repair `wide_lattice_h2t_distance_law_note` by satisfying the audit-requested
raw-row inclusion route. The previous restricted packet verified a frozen log,
but the source note did not itself include the raw distance and `F~M` sweep
rows.

This branch adds those rows to the note and extends the verifier to check that
the note table contains every parsed raw row.
