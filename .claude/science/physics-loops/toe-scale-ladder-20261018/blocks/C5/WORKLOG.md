# C5 WORKLOG — equivariant three-winding

## 2026-10-18 18:55 UTC — start
- Read SCIENCE_WORKFLOW s2, SCALE_LADDER_MAP C5, CUBIC_COVARIANCE_FREEZES note (item 4: "every moving walk
  found has three-winding zero" — search only) and TWO_QUBIT_SITE_UNFREEZES note (Remark after Thm 6: Clifford
  family lies in a copy of S^5 in U(4); H^3(S^5)=0 so W3=0). Note: the image is S^5 (unit vectors of R^6:
  f,h1,h2,g1,g2,g3), not S^4 as the map text says.
- Plan / key idea found while reading: W3 vanishes for EVERY strictly finite-range (Laurent polynomial)
  unitary on T^3, independent of covariance, by algebraic K-theory: K_1(C[Z^3]) = C^* x Z^3
  (Bass-Heller-Swan / fundamental theorem, regular ring), so U (+) 1 = diag(c z^m,1,..) * (elementary
  matrices), elementary matrices are null-homotopic, W3 is a homotopy invariant. Covariance therefore is
  not the obstruction; strict finite range is. Positive control: smooth (analytic, NOT finite-range)
  O-covariant map V_M = (M - sum cos k + i sin k . sigma)/norm has W3 in {0, +-1, -+2}.
- Literature: arXiv/APS blocked by proxy (403); HNU text not readable here. Web search found no explicit
  statement of the finite-range W3 vanishing theorem (not proof of absence).

## 19:40 UTC — scripts s1-s3 done, s4 running
- s1 (positive control V_M, conventions): run1 FAILED 3 convergence checks (threshold 1e-6 at N=32->64 too
  strict for M=3.5, 0.5, -3.5); log kept as logs/s1_run1_superseded_convergence_threshold.log. Rerun adds
  N=96 and requires shrinking differences, last < 1e-6: PASS=19 FAIL=0. Convention sign c = -1
  (W3[V_2] = -1). Values W3[V_M] = c*(0,1,-2,1,0) confirmed.
- s2 (Clifford lemma): EXACT: Phi^* tr(theta^3) = 0 pointwise on S^5 (sympy, 20 components), stronger
  than the two-qubit note's H^3(S^5)=0 remark; control nonzero on S^3. b* member exact-grid W3=0. PASS=10.
- s3 (battery, 21 finite-range walks n=2,3,4 incl. D2/D3/D4 covariant): exact-grid W3=0 all; independent
  signed-preimage degree 0 for SU(2) ones (calibrated -1 on V_2). PASS=27.
- s4 early output: fit to V_2 at range 1 with growing unitarity penalty stalls at unitarity defect 3.75e-2
  with W3 = -1 (cannot reach unitarity without crossing det=0) -> compactness corollary (defect bound eps_r>0).

## 19:45 UTC — s4 adversarial fit: falsified my optimizer prediction; s4b added
- s4 run 1 was killed by the 30-min background limit (log kept: logs/s4_run1_killed_at_30min_timeout_incomplete.log).
  Its content FALSIFIED my docstring prediction: at range 2 the penalty continuation reached unitarity
  defect 6.7e-5 with W3 = -1, min|det| ~ 1, sup||U - V_2|| = 0.34 (decreasing defect ~ w^-0.8).
  Not a contradiction of Theorem K (not exactly unitary) but it is the one place a counterexample could
  show up numerically: if defect -> 0 with bounded coefficients and det bounded away from 0, the limit
  would be an exact range-2 unitary with W3 = -1. Wrote s4b_defect_floor.py: continue the penalty to
  w = 3e6, then pure unitarity minimization (LM), tracking defect / min|det| / W3. Prediction from K +
  compactness: defect floor eps_2 > 0 or det collapse.
- s4 rerun with fewer duplicate starts and the empirical assertions replaced by integer-W3 checks
  (disclosed in the script comment). Chain s4 -> s4b -> s5 running on one core.
- Draft NOTE.md written.

## 21:12 UTC — defect floors
- s4 rerun: PASS=17 FAIL=0 (integer W3 along the continuation; truncation controls W3=-1, not unitary).
- s4c (r=1): penalty continuation to w=3e7 and pure-unitarity LM: defect plateaus at ~6e-3 with W3=-1,
  min|det| 0.993; PASS=2. Consistent with K + compactness (eps_1 <~ 6e-3, upper bound only).
- s4b (r=2): defect 6.8e-5 (w=3e3), 1.3e-5 (3e4), 3.9e-6 (3e5), 3.5e-6 (3e6): flattening; sup||U-V_2||
  rising 0.34 -> 0.55. Pure LM stage pending. eps_2 is small but the run so far shows no approach to 0.

## 22:02 UTC
- s4b stopped by me during its slow LM stage (background time limit); penalty-stage log renamed
  logs/s4b_defect_floor_penalty_stage_stopped_in_pure_stage.log; params saved. s4d continues from them:
  defect 3.3e-6 -> 1.82e-6 (last stage step 1.85e-6 -> 1.82e-6), W3 = -1, min|det| = 1.000. PASS=2.
  eps_2 <~ 2e-6: numerics cannot distinguish a floor of this size from 0; positivity rests on K. Flagged.
- s5: four generic exact range-1 one-qubit unitaries (27 nonzero hops, unitary 1e-15, moving) all W3 = 0.
  r = 2 and n = 4 trials running.
- NOTE.md updated (Corollary D numbers, evidence table, disclosure of falsified optimizer prediction).

## 22:35 UTC — wrap-up
- s5 run 1 stalled in the r=2 finite-difference solve (log kept: s5_run1_stopped_in_r2_trial.log); rerun
  without r=2: PASS=6 FAIL=0 (4 n=2 and 2 n=4 generic moving range-1 unitaries, W3 = 0).
- Final logs: s1 19/0, s2 10/0, s3 27/0, s4 17/0, s4c 2/0, s4d 2/0, s5 6/0 (superseded/stopped logs kept).
- Outcome: obstruction theorem (Theorem K, conditional on SK_1(C[Z^3]) = 0), sharp witness V_M
  (O-covariant analytic, infinite range, W3 = -1/+2). Load-bearing: K step 2.

## 23:12 UTC — review dispositions applied to NOTE.md (REVIEW.md §7): scope (total W3), coefficient 1, N hypotheses, cf. Dubail–Read, defect numbers 1.99e-6/1.63e-6, second proof cited, provenance + status line.
