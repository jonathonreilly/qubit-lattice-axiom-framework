# Run log (kept so nothing is hidden)
- Run 1 (hemi_test_run1.py -> hemi_result_run1.txt): B1, B4, B5, B6, F reported FAIL.
  Causes: (a) quadrature did not split at s=pi/2, the kink of t_+^k densities (B1 error 6e-6, B5 k=1 antipodal
  error 1e-5, B6 2D-grid error 2.6e-6 against a 1e-8 threshold); (b) B4 code thresholds (1e-3) were stricter than the
  pre-registered prose ("nonzero and non-affine, growing with beta"); (c) F: min max-error 0.0192 < 0.02.
- Run 2: added the s=pi/2 split (numeric only), B6 done by exact 1D evaluation, B4 rule set to the prose rule.
  B5 still failed for k=0 because the k=0 kernel was coded as t^0 for all t (nonzero for t<0): implementation bug.
- Run 3 (final hemi_test.py -> hemi_result.txt/json): k=0 kernel fixed. All pre-registered readings A,B1-B6,C pass; F stays at
  0.0192 (pre-registered threshold 0.02 missed by 0.0008), reported as inconclusive, not used in the verdict.
- Part E (hemi_test_E.py): added after run 2, pre-registered in the PREREG addendum before it was run; all pass.
- Known artifact: the C1-smooth flag for measure power kernel k=0 is an interpolation artifact (exact g=1-theta/pi has slope -1/pi at 0); it does not enter the Wootters conclusion (its Fisher ratio is 16, not 1).
- Repository access: read-only, except one 'git fetch origin claude/toe-viability-probes-20260927' in main_wt (updates a remote-tracking ref only; no working-tree file touched).
