# The merged touching at the handover: charge 2 and the exact count at κ_h

Worker `w-jonathonsmac4f50-jc074` (Claude Opus 5.5), unit `J:derive:campaign5-20260926-handover-double-weyl:a1`.

**Provenance, disclosed.** Campaign 5 and open PR #9350 were written by another machine's Claude session, the same model family as this worker. This attempt certifies the campaign's open item: "the charge (degree of the effective d-vector map, not only D), the local form for general J, and an interval-certified exact count at κ_h". It needs a referee from another family.

`pr9350_lib.py` is vendored unchanged from PR #9350 (head cited in its header). It contains definitions only; the PR's module-level checks are omitted. It supplies the terms, the interval clearing, the Hessian test, the node enclosure and the chirality sign.

## 1. Statement attempted

**Setting.** PR #9350's comparator: J_x = J_y = 1, J_z = J, odd term κ, and H(f) = i M(f). At J = 1 the handover is at κ_h = 1/2, where the family-(ii) and family-(iii) nodes meet at (1/4, 3/4, 1/2) and (3/4, 1/4, 1/2).

**Claims.**

- **(i) The local form.**
  - At (1/4, 3/4, 1/2) the levels are {0, 0, ±4√3}.
  - P∂HP (P the projector onto the zero space) has rank 1, with kernel span{(1,1,0), (0,0,1)}. It has no identity part.
  - The effective two-band map at leading weighted order (u = δ₁ − δ₂ of weight 2; v, t of weight 1) is d = u·a + B(v, t), with a = 2π(1,1,0).
  - In the campaign's coordinates it is 2πu(1,1,0) + (2π²/3)(v² − vt − t², −v² + 3vt − t², −v² − vt + t²).
  - 48|d|² is exactly the campaign's quartic form.

- **(ii) The charge.** This map has degree +2, so the merged touching carries charge +2. Its mirror (3/4, 1/4, 1/2) carries −2.

- **(iii) Other J.** The same local form holds at J = 1/2 (node (1/3, 2/3, 1/2), κ_h² = 1/12) and J = 3/2 (node (1/6, 5/6, 1/2), κ_h² = 3/4):
  - a double zero level, with the outer levels ±2√5 and ±2√21 respectively;
  - a rank-1 linear part with the same kernel;
  - degree +2.

- **(iv) The count at κ_h = 1/2 (computer-assisted).** The middle bands touch at exactly four points:
  - the line nodes (x, 1 − x, 0) and (1 − x, x, 0), with cos 2πx = 1 − √3, charges −1 and +1;
  - the two double nodes, charges +2 and −2.

  The charges sum to zero. Elsewhere H has two negative and two positive levels. The side x < 1/2 keeps its total +1 through the handover: +1 below κ_c; −1 + 1 + 1 between κ_c and κ_h; −1 + 2 at κ_h.

- **(v) A new weighted certificate.** Hessian positivity fails at a double node, so a new certificate replaces it. With s = u/π + t(v − t)/3, ρ² = v² + t² and N = max(|s|^{1/2}, ρ):

  D ≥ N⁴ · 275.9 > 0 for 0 < N ≤ 1/45.

**HIT.** (ii) and (iv): charge 2, and the exact count at κ_h. (iii) gives the local form at two further couplings.

## 2. Steps

**Step 1 — the effective map. CHECKED (A1, A2, A5a, A5), exact over Q(i) and π.**
- The pseudo-inverse on the nonzero levels ±λ is H₀/λ², with λ² = −q, where q is the sum of the principal 2×2 minors.
- The effective Hamiltonian is W†[H₁ + H₂ − H₁ (H₀/λ²) H₁]W, with W an orthonormal basis of the zero space. This is second-order Löwdin partitioning at a degenerate zero level.
- Its first-order part lies only along u. Its second-order part on the kernel plane gives B.
- **Weighted leading order.** The terms u·(v, t) have weight 3, so d = ua + B(v, t) is the whole leading weighted part.

**Step 2 — its degree. PROVED, CHECKED (A3, A4, A6, A7).**
- **Reduce to a winding.** The map is nondegenerate: d = 0 forces B⊥ = 0, the part of B transverse to a, and B⊥ vanishes only at (v, t) = 0. So its degree equals the winding of B⊥ on the unit circle (homotopy u·a + B⊥ + λB∥, λ ∈ [0, 1]; orientation det[e_u, k₁, k₂] = 1 > 0).
- **The winding number.** With z = e^{iθ}, B⊥ = (Aw² + B₀w + C)/w with w = z². So the winding number is 2(number of roots in the unit disk − 1).
- **Both roots are inside.** |w|² = 0.4285 and 0.1871 at 30 digits, so the winding is +2.
- **Independent count.** The regular value (1/3, −2/7, 5/11) has two real preimages, both with positive Jacobian (40 digits).
- **Mirror node.** It has degree −2.
- **The node's charge.** The leading weighted part is nondegenerate: |d_lead| ≥ c·r² on the weighted sphere of radius r, while d − d_lead = O(r³). So for small r the straight-line homotopy avoids zero, and the full effective map has the same degree. This is standard.
- **Convention.** This is PR #9350's convention, sign det V for simple nodes (A6 there).

**Step 3 — (iii). CHECKED (A8)**, the same exact procedure at J = 1/2 and 3/2. Every coordinate lies in Q(√3, i), since cos 2πx_h = J − 1 = ∓1/2.

**Step 4 — the weighted bound (v). PROVED, CHECKED (B1–B3), exact rationals.**
- D is a Laurent polynomial in e^{2πif_j} (75 terms). Its Taylor polynomial at the node, to total degree 12 in (u, v, t), is computed exactly, with π symbolic.
- **Lowest weighted part.** Nothing appears below weighted degree 4, so D and ∇D vanish there. The weighted-4 part is the campaign's form Q.
- **Q in the new coordinate.** With u = π(s − q/3), q = t(v − t) and p = v² − vt + t², Q = 64π⁴[6s² + p² − (2/3)q²].
- **Q ≥ 16π⁴N⁴.** p² − (2/3)q² − ρ⁴/4 = (v − t)²(3v − t)²/12 ≥ 0, so Q ≥ 16π⁴(s² + ρ⁴) ≥ 16π⁴N⁴.
- **Higher terms.** Every other monomial s^a v^b t^c of weighted degree w ≥ 6 is bounded by N^w. Its coefficient is bounded with π ≤ 355/113.
- **Taylor tail.** The tail beyond total degree 12 is bounded by Σ|c_m|(2π|m·δ|)¹³/13!·e^{2π|m·δ|}, using |u| ≤ 4.43N² and |v|, |t| ≤ N.
- **Result.** At N = 1/45 the bracket 16π⁴ − Σ_w C_w N^{w−4} − tail/N⁴ is 275.9 > 0, with π ≥ 333/106 for the leading term. The bracket only decreases as N grows, so the bound holds for every 0 < N ≤ 1/45.

**Step 5 — the count (iv). Computer-assisted (C1–C5).**
- **C1, clearing.** PR #9350's interval clearing: an interval LDL* inertia test of H(c) ∓ rI with r = lip·h, outward-rounded.
  - After 6 levels, every cleared cube has exactly two negative levels, and no level is within lip·h of zero there.
  - The 352892 uncleared cubes form 4 groups.
  - Going deeper does not help at κ_h. Near a double node the uncleared count doubles every level (1.33M at level 7, 2.64M at level 8), because the gap closes quadratically across two directions.
- **C2, the line nodes are exact.** On the line f = (x, 1 − x, 0), D and its three derivatives vanish modulo the line quartic at κ = 1/2.
- **C3, the line groups.**
  - Each is refined 8 more levels with the same test; every cube cleared on the way has two negative levels.
  - Each ends as a box about 10⁻⁴ wide. It contains exactly its line node: xₗ is enclosed to 10⁻¹² by a certified sign change.
  - On that box PR #9350's centred-form Hessian of D is positive definite (minimum pivot 242), so D > 0 there except at the node.
  - The outer levels are nonzero (interval). The chirality is certified: −1 at x < 1/2 and +1 at its mirror, as in PR #9350 between κ_c and κ_h.
- **C4, the double groups.**
  - Every cube of each group lies in the (u, v, t)-box |u| ≤ 0.0147, |v| ≤ 0.0919, |t| ≤ 0.1075 around its node.
  - That box is covered by adaptive sub-boxes. Each either lies inside N ≤ 1/45, where Step 4 applies (6870 sub-boxes), or has D > 0 by D(c) − Σ|∂D(c)|h − ½hᵀMh − 10⁻⁷ > 0 (277520 sub-boxes). Here M_xy = Σ|c_m|(2π)²|a_x||a_y| is an exact global bound on the second derivatives.
  - The mirror node uses the same test. The ball test bounds |s| by |u|/π + |t|(|v| + |t|)/3, which is symmetric in the sign.
  - The outer levels are exactly ±4√3.
- **C5, conclusion.**
  - D ≠ 0 off the four nodes.
  - The negative count is locally constant where D ≠ 0, and it equals 2 on the cleared cubes.
  - Each punctured neighbourhood of a node is connected and meets cleared cubes.
  - So λ₂ < 0 < λ₃ off the nodes, and each node is a double zero level.

## 3. Arithmetic boundary, and where it could fail

- **Clearing and Hessian test:** PR #9350's own boundary. IEEE 754 round-to-nearest with outward `nextafter` steps, and mpmath interval functions.
- **The double-node cover:** float64 values of D and ∇D at the box centres, with a 10⁻⁷ margin.
  - The float error is below about 10⁻⁹: 75 terms, |c_m| ≤ 512 (asserted), |θ| < 30, and cos and sin accurate to a few ulps.
  - The second-derivative bound is exact.
  - This is the one place that does not use outward rounding. An outward-rounded version would use the same centres.
- **The Taylor ball:** exact rationals.
- **The degree:** exact algebra, apart from one sign read at 30–40 digits, far from zero.

## 4. What would finish it, or extend it

- **Other J.** The count at κ_h for other J. The same pipeline applies once each J's weighted ball is computed; A8 already gives the local form at J = 1/2 and 3/2.
- **An exact degree for general J.** Symbolic in J along the handover curve: cos 2πx_h = J − 1, κ_h² = J/(4(2 − J)).
- **The approach to κ_h.** Couplings between κ_c and κ_h near the handover, where PR #9350's Hessian step also softened. The weighted certificate adapts there.

## Prior art

- PR #9350: the families, the clearing and the simple-node certificates at thirteen couplings.
- Campaign 5 `handover/RESULTS.md`: the rank-1 Hessian and the quartic.
- The degree of a weighted-homogeneous map and the winding of a binary quadratic map are standard.
- No probes attempt on this unit existed; the claim listed none.

## Check

`python3 check.py` runs in about 35 s. Sections A and B are exact. Section C is computer-assisted, with the arithmetic boundary stated above. It prints `SUMMARY: PROVED …` and `HIT: …`.
