# Route Portfolio

1. Sync the note and runner to the current 14+7 snapshot. Chosen because it
   directly closes the row-count blocker.
2. Add three missing `trace_normalization_reference` rows. Rejected because the
   current ledger has 7 matching rows and this PR does not manufacture audit
   rows.
3. Unstack from #2966 and duplicate the measure/weight repair. Rejected because
   it would create avoidable conflicts with the already-open row-count PR.
