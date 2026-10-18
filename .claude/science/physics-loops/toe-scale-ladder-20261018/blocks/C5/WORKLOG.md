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
