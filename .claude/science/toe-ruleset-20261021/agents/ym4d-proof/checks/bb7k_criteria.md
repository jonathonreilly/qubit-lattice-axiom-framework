# bb7k criteria (lane B session 7; written after BFT_B §21 and Step 1, before checks/bb7k_off.py exists)

Model: d = 2, SU(2), n = 3 (fine sites per coarse step), coarse side 5, box half-width 2n (the setting of checks/bb6n). Box normal
forms by the bb6n descent. Construction KΠ-off (§21.0) with tents σ_5, cut-off ψ (C^∞ step, ψ = 1 on [0, 1.0], 0 on [2.0, ∞);
d = |log| ∈ [0, π]), iterated along axis 0 then axis 1. U0 := a small random field (n max|A| = 0.3, as bb6n). Spread data:
U_s := U0^h with h Haar-random at every site (so the corner normal forms at a site differ by Haar-random root values).
Thresholds are float/descent precision (the descent stops at max|d*w| ≤ 1e-12), as in bb6n; no session-7 constant.
- K1 root values: max_Y|log G^off(U_s)(c_Y)| ≤ 1e-12. PASS required.
- K2 face consistency: at every site with some t_ν = 0, the value computed from the neighbouring cell (t_ν = 1, weight on the upper
  corner) agrees: max distance ≤ 1e-12. PASS required.
- K3 G_0-invariance: for g_0 Haar-random off the roots and 1 at the roots, max link distance between Π^off(U_s^{g_0}) and
  Π^off(U_s) ≤ 1e-8 (normal forms of U_s^{g_0} by descent from perturbed starts). PASS required.
- K4 constant covariance: max link distance between Π^off(U_s^c) and Π^off(U_s)^c ≤ 1e-8 (c Haar). PASS required.
- K5 idempotence: max|log G^off(Π^off(U_s))| ≤ 1e-8 (normal forms of Π^off(U_s) by descent). PASS required.
- K6 root-value covariance for a Haar-random level-0 gauge k: Π^off(U0^k) = Π^off(U0)^{ĥ}, ĥ := gluing of {k(c_X)g_X(U0)}·
  G^off(U0)^{-1}: max link distance ≤ 1e-8 and max_Y d(ĥ(c_Y), k(c_Y)) ≤ 1e-12. PASS required.
- K7 continuity along a gauge path: root values h_t(c_X) = exp(tζ_X), |ζ_X| ≤ 2.5 random, t ∈ {0, 1/40, …, 1} (normal forms of
  U0^{h_t} by NF-cov transport); Ĝ_t := G^off(U0^{h_t})·h_t: max_t max_z d(Ĝ_{t+1/40}, Ĝ_t) ≤ 20·max_t max_X d(h_{t+1/40}(c_X), h_t(c_X)).
  PASS required. Informational: the fraction of sites in the cut-off zone along the path.
- K8 clustered data: on U0, G^off = 𝔪^geo exactly (≤ 1e-14); informational: max distance between 𝔪^geo- and Karcher-glued G.
- K9 informational: in the frame, Π^off(U_s)^{ĥ_s^{-1}} = Π^off(U0) (ĥ_s from h's root values): n·max link |log| of both.
- K10 control (CL-F4): Karcher gluing of the spread corner points of U_s from two different starts (the largest-weight corner and
  the smallest-weight corner) disagrees by ≥ 0.1 at some site, or fails to converge in 200 iterations. PASS required (= the control
  fails as predicted).
Resources: expected < 200 MB, < 5 min.

[RBB7-fix RS7-8, appended 11:15:11 UTC, session 8; criteria above unchanged] K10 was mis-designed: Haar-random corner spreads (<= 2.76 < pi) never reach the antipodal regime where the weighted Karcher mean is non-unique. The control that actually demonstrates CL-F4 for the Karcher gluing is REVIEW_BFT_B_S7 E.2 (near-antipodal probe: non-unique limits on antipodal pairs, an O(1) jump across the cut locus; the cut-off m_w stays continuous).
