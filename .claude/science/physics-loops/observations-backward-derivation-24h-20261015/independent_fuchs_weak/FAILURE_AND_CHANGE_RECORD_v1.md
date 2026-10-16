# Failure, source-change and exposure record

- The independent first pass and complex supplement both completed on their
  first attempt. There was no owned timeout, runtime error, failed control or
  silently discarded attempt. Stderr contains intentionally emitted progress
  records. The two author synthetic replays also completed without error;
  their stderr files are empty.
- The initial source v1 omitted the force-off condition in its equation (4)
  wording and overstated what full column rank proves. These issues were
  identified before reading author code, reported to the author and corrected
  only by the author in v2. The old source remains preserved. Exact source
  bytes and the v1-to-v2 diff are in the source snapshot and
  `V1_TO_V2_DELTA_v1.json`. No equation changed.
- The author disclosed progress counts while independent work proceeded.
  After the separate complex proof/fixture freeze, the author also reported
  its coarse-quadrature residual. That communication was not access to author
  implementation or output artifacts. The independence claim concerns the
  derivation, fixtures, implementations and freeze before artifact access;
  this was not a blinded review of author progress.
- The author's historical complex v1 run failed one of 20 controls at
  `1.0229861322125439e-10` versus a fixed `1e-10` threshold. The unchanged
  historical source, output and run metadata are embedded losslessly in
  `AUTHOR_SYNTHETIC_EXPOSURE_v1.json`. This was not an independently executed
  failed attempt. Its v2 diff is preserved as a JSON UTF-8 string with byte
  count and SHA256 in `AUTHOR_COMPLEX_CONTROL_V1_TO_V2_DELTA_v1.json`.
  Halving the synthetic step and adding three convergence checks produced
  23 passing controls; the v2 replay is byte identical to the author's
  receipt. No tolerance was loosened and no historical failure was removed.
- The complex-probe extension is explicitly post-exposure development work.
  It is not a holdout, and two probes on one interval are correlated summaries.
- The shared fit output calls probe counts `train_windows` and
  `validation_windows`; consumers must distinguish these from physical time
  windows in the complex case. No author file was changed for this check.
- All 15 pinned author sources and receipts matched their respective frozen
  snapshots in the final binding. First-pass independent proof, code and
  output files were left unchanged. No raw trace, raw acquisition receipt or
  development-results artifact was accessed, and no development runner was
  executed. No git, lock, PR or external application action was taken.
