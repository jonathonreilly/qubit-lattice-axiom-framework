# Narrow metadata-check correction

The first inspection completed at exit 0. Its case named altered_original_body appended bytes to the complete note rather than changing a byte inside an original body. It correctly demonstrated note-integrity rejection, but its name was more specific than its action. Its complete source-at-launch, receipt and streams remain unchanged in metadata_runs/inspection.

The current inspector flips one byte strictly inside the first original body's recorded interval. Its comparison field was also renamed from independent_interval_comparison to direct_original_interval_comparison to avoid any implication of independent scientific review. The recorder gained an optional safe attempt label so the corrected run can coexist with the first one. No proposal, historical source, mathematical body or previous receipt changed. The corrected run is metadata_runs/inspection_02; this is a metadata-test repair, not new science.
