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

## block03 — 2026-07-08 supervisor review

- Runner worker survived a session disconnect and delivered honestly
  (PASS=3 FAIL=3 with correct spec-defect diagnosis). Supervisor patches:
  even-P identity + Richardson curvature replaces the contaminated
  mixed-parity band fit (4.1e-11 vs the identity); quartic+sextic band fits
  with printed extraction shift; fixed-threshold dichotomy gates decoupled
  from Delta_univ. Final PASS=6 FAIL=0.
- Science findings (drive the block04 restructure): composite inertial mass
  is bandwidth-dominated (M_comp rises with binding while rest energy
  falls); singles-exact source F fails composites by >= 0.6 at U=0.8; F's
  convexity breaks even free composites. Exact finite-spacing WEP for
  rest-energy sources is impossible on this surface (a lattice fact, not a
  framework defect).
- Note worker draft faithful; supervisor removed campaign-internal
  block-label tokens (9 replacements).
- Local disposition: pass.

## block04 — 2026-07-08 supervisor review

- Runner worker delivered honest PASS=4 FAIL=2; both failures were
  supervisor-spec physics errors: shallow bound states larger than the ring
  (kappa_L < 8) corrupting M_comp, and a wrongly expected monotone
  F-violation (it crosses zero at a fine-tuned U). Supervisor patches:
  kappa_L size-validity diagnostic gating every composite extraction;
  L=256/1024 legs; crossing detection reported as a single-configuration
  accidental point. Final PASS=6 FAIL=0.
- Note supervisor-authored (verdict-adjacent surface; worker drafting not
  appropriate per workhorse split). N1-N8 checklist completed pre-ship in
  NO_GO_DISCIPLINE_CHECKLIST.md; gate result PASS for the narrow boundary.
- Local disposition: pass.

## block04 cluster-cap evaluation (3rd PR in ep_record_stiffness family)

Evaluator brief applied locally (no separate agent authorized mid-run):
1. New load-bearing premise: YES — T2 exact convexity boundary, T3
   same-rest-energy/different-inertia witness, T4 scaling-window theorem
   with derived exponents; none present in #5061/#5062.
2. Distinct claim type: YES — reduction + exact negative boundary +
   constructive witness + window theorem vs the prior positive bounded
   theorems.
3. Independently reviewable: YES — standalone note + runner.
4. Marginal review value: YES — this is the lane's decision surface.
Verdict: OPEN.

## block05 — 2026-07-08 supervisor review

- Runner worker delivered PASS=4 FAIL=1 and correctly refused to pass my
  wrong "Galilean control" (lattice-cosine band is not Kohn-exact; its
  curvature varies). Supervisor repair: manifest quadratic-band control
  (first-order Kohn term exact < 1e-12; zone-edge artifact bounded and
  printed) + cosine family kept as a second sum-rule validation (1.3e-11)
  and bandwidth-domination exhibit. Final PASS=5 FAIL=0.
- Science: T1 kinetic-functional sum rule verified 9.3e-10 (three splits;
  symmetric-split second-order term exactly 0); T3 class-level mass-energy
  equivalence no-go (mismatch 9.1/7.5/3.2 binding energies, shape-
  consistent, window-persistent); corollary = mediator requirement
  converging on the record-preservation-forced covariant-hopping class.
- Observed context: contact-on-cosine identity M_comp - 2m = E_B to all
  printed digits (reported, ungated).
- Note supervisor-authored. Local disposition: pass.
- Cluster note: 2nd PR in the composite/matter_inertial family (block03
  was 1st) — under the evaluator threshold.
