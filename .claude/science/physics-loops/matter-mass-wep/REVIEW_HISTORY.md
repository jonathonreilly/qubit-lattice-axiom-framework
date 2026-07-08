# Review History — matter-mass-wep

(none yet)

## block01 — 2026-07-08 supervisor review

- Worker deliverables: note + runner, both reviewed line-by-line.
- Defects found and fixed by supervisor: spec-relative references ("File (2)",
  "Block02") leaked into the repo note (replaced with authority names /
  plain companion language); worker-handoff SUMMARY prints removed from the
  runner's output (moved to docstring), cache regenerated.
- Math verified independently: T4 expansion, T5 identity and series
  coefficient 2/3, R1/R2 quotes checked verbatim against the no-go note.
- Runner executed by supervisor: TOTAL: PASS=7 FAIL=0, residuals at machine
  precision; CHECK-01 ties the replicated transfer construction to the
  independent scalar dispersion (3.0e-14).
- Local disposition: pass.

## block02 note — 2026-07-08 supervisor review (in progress)

- Worker FLAGGED A REAL PROOF GAP in the supervisor-authored T3: a 3-sigma_p
  window plus finite fourth moments does not control Gaussian tails, and the
  rest-point on-axis fourth derivative is not a valid uniform bound constant
  (transverse Hessian entries of E_33 contribute).
- Supervisor repair: T3 restated for window-supported densities with the
  sup-Hessian window constant C4(m) (on-axis rest-point value retained as its
  exact lower bound, preserving the T4 divergence exhibit); new T3' Gaussian
  tail corollary with explicit exponentially small addend, to be printed by
  the runner.
- Runner must gain: numerical C4^win computation, eps_tail print per run,
  and a gated bound-compliance leg. To be patched at runner review.

## block02 runner — 2026-07-08 supervisor review

- Worker's own run honestly reported PASS=4 FAIL=3 with correct diagnosis:
  spec-design defects (historical widths gated as if in-window; on-axis-only
  C4 comparator; flat window cap).
- Supervisor patches: mass-dependent window p_*(m)=min(pi/4, 0.6m); gated
  sweep widened to sigma_x in {3,4.5,6,9,12} with m in {0.5,1,2}; m=0.2 and
  historical widths demoted to reported out-of-window context; gate changed
  to T3/T3' bound-compliance (C4_win numeric + eps_tail) + informativeness;
  collapse refit as A*sigma_p^2 + B*sigma_p^4 on smallest-g residuals with
  the ISOTROPIC comparator A_iso = (1/2) M_I |d4_ax + 2 d4_mx|; new CHECK-08
  verifies the note's closed form lower-bounds C4_win (seeded with exact
  rest-point Hessian).
- Final: TOTAL PASS=8 FAIL=0. A/A_iso within 1% at all gated masses;
  resid/bound = 0.4494 equals the predicted spectral-norm slack; m=0 control
  width-splits as required; position/momentum gauge agreement 4.6e-13.
- Local disposition: pass.
