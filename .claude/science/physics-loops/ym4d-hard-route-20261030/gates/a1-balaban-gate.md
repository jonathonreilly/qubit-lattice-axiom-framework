lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T05:02Z

# Gate: `library/a1-balaban.md` (row 91)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, statement pinned at d32f4da23. The gated note was written by Codex (row 81). This is one cross-provider read by hand, not an audit, and it grants no status. Balaban's CMP 98, 99 (75-102), 99 (389-434) and 102 were read from the owner's legal copies in `~/ym4d-papers/` (OCR text checked against the PDF where the formula matters); nothing from them is copied here beyond short statements.

Status: in progress; sections are added as they are checked.

## 0. OCR reconstructions (note Section 11), checked against the scans

Rendered from the PDFs (PyMuPDF, scratch folder outside the repository) and read directly:

| Claim in the note | Scan | Verdict |
|---|---|---|
| CMP 98 (130)-(131): the quadratic-term sum runs over L^j+...+L, the exponent over (L^{2j}+...+L^2)eta^2 alpha_0 | p. 38 | confirmed |
| CMP 98 (154): bracket 1 - L^-2 + 4dC'_1 alpha_0 L^-3 + (C''_1 L^-2/C_3)(1 + 4dC'_1 alpha_0 L^-2 + C_2 L^-1 alpha_1 + 2dC_3 L^-1 alpha_1)^2; (155) asks only for <= 1 | p. 41 | confirmed; the note's choice C_3 >= 6C''_1, 4dC'_1 alpha L^-1 <= 1/4, square <= 3 gives 1 - L^-2/4, which is stronger than (155) needs |
| CMP 98 (157): right side C_3\|A\| < C_3 alpha_1 | p. 42 | confirmed |
| CMP 99b (3.48): (L^j eta)^-4 (L^j' eta)^-d e^{-delta_0 d} | p. 398 | confirmed |
| CMP 99b (3.132): O(1)(L^j eta)^-2 (L^j' eta)^-d e^{-delta_1 d}, same for G_1 | p. 422 | confirmed |
| CMP 99b Theorem 3.12: the covariant-Laplacian inequality of (3.42) "does not hold for G, G_1"; (3.133) for H has no Laplacian entry | pp. 422-423 | confirmed |
| CMP 102 (160): (8d^2L^2 + 4L^2\|x-y\|) eps_1 | p. 303 | confirmed |
| CMP 102 (162): weight (d(y_1,y_2)+1)(L^{j_2} eta)^-1 at rate delta_0/2 | p. 303 | confirmed |
| CMP 102 (166)-(167): coefficient 1/8 | p. 304 | confirmed |

One reading note, not a defect: the note's Section 6 says the far part of (6.3) uses "the coarse global bound" \|B\| <= CM eps_0. Balaban's (161) uses the axial linear growth \|B(c)\| <= C(d(y_1,c) + M_Delta) eps_0, which is what gives M_Delta = 1 at the central pillar. With the crude bound the far term carries an extra R_1M_1, which is still absorbed by choosing R_1M_1 larger in (163), since x e^{-ax/2} -> 0. Either reading closes.

## 1. Sections 3.5-3.7: rebuilt CMP 98 and CMP 99 (75-102) inputs

**3.5 (CMP 98 Props 2, 4, 5 for Balaban's average): ADVANCE.** Redone:
- Curvature recursion (3.6) and its uniformity: with w_m = L^{2(n-m)} v_m, (3.6) gives w_{m+1} - w_m <= C L^{2(m+1-n)} w_m^2, and the sum of L^{2(m+1-n)} over m < n is at most (1-L^-2)^-1, so w_m < 2 alpha at every step once 4C alpha/(1-L^-2) < 1. Correct, and this is Balaban's (48)-(54).
- Analytic remainder: dividing the one-step bound (linear norm L(1+C alpha t_m^2), remainder C L^2 x square) by t_{m+1} = L t_m gives exactly a_{m+1} <= (1+C alpha t_m^2) a_m + C t_{m+1} a_m^2; the bootstrap (product <= 5/4, quadratic sum <= r/4) gives a_m < 2r and (3.7), matching Balaban's (133). Correct.
- Derivative induction: (3.9) is (154) verbatim, and the stated choices close it with slack. Kernel scaling s_j^{1-d} for the eta^d pairing checked from the segment count. Correct.

**3.6 (CMP 99a Lemma 1 and the current estimate): ADVANCE.** (3.10): interior links cost at most (d-1)(L-1) relative plaquettes of size 2 alpha_0 L^-2; moving a crossing link across the face costs at most 2d(d-1)L^2 of them; together 2(d-1)alpha_0/L + 4d(d-1)alpha_0 + alpha_1 <= 4d^2 alpha_0 + alpha_1. This is the bound Balaban states and uses on CMP 102 p. 303 (checked in the scan). (3.11): each term scales correctly. The cubic plaquette remainder eta^3\|A\|^3, divided by eta^2 and differenced, gives \|A\|^3. The reference-curvature commutator gives alpha_0 s^-2 \|A\| after the divergence. The commutator differences give \|A\|\|grad A\|. Correct as an estimate; it does not need the printed coefficients.

**3.7 (mixed-scale sums): ADVANCE.** Redone. Crossing a complete layer i costs layer-length at least rho, so \|j_y - j_z\| <= 1 + d/rho, which is (3.12). The ball and mesh count gives at most C(R+1)^4 L^{8+8R/rho} tops per scale and 3 + 2R/rho scales. With rho >= 2(8+\|p\|) log L / a, the shell [m, m+1) contributes at most C L^{8+\|p\|} (m+2)^{q+5} e^{-am/2}, so (3.13) holds. In the convolution bound the scale powers telescope exactly (s_w^{-d} s_w^d = 1, and the ratios multiply), and summing the halved exponentials successively gives b^n S(a/2)^{n-1}. Correct. The bound needs the layer separation rho to exceed 2(8+\|p\|) log L / a, where a is the F0 decay rate. This ties the admissible separation to F0's rate. The note states it ("once the separation exceeds its fixed lower bound"); the outline's separation parameter has to be chosen after F0's rate.

## 2. Sections 3.8-3.9: the gauge theorem and the background propagators, reduced to F0

**3.8 (CMP 99a Theorem 2, Proposition 6, inhomogeneous slice): ADVANCE, conditional on F0.** Checked against CMP 99a pp. 83-88 in the OCR.
- The truncation mismatch with coefficient one on the coarse mismatch and a geometric curvature sum is Balaban's (1.65)-(1.66). He gets \|U'^j - 1\| < 8d^2 alpha_0 (1 + L^-2 + ...) + alpha_1 < 11d^2 alpha_0 + alpha_1 by iterating Lemma 1.
- The a priori reset (3.19) is Balaban's Proposition 3, (1.55)-(1.64). That proof has the same structure as the note's: G(U_0) applied to the current bound; the alpha_2\|grad A\| term absorbed by B_0 36d alpha_2 <= 1/2; the restriction (1.61) on the preliminary alpha_2 is met because alpha_2 = C'_1 B_1(alpha_0+alpha_1) and (1.64) holds for small data. The reset is an a priori bound for any slice potential of preliminary size alpha_2, so the per-layer L^2 loss of the ascent never accumulates. Its constants are those of the curved vector inverse, which Section 3.9 reduces to F0. Depth-uniform.
- The fixed-point equations (3.17)-(3.18), the uniqueness of the normalizing gauge, and the inhomogeneous slice RD*A = f used only for transversality are correct as reconstructed. The remark that CMP 99a Theorem 8 asserts second-order bounds without a bound on Df, and that they are not used, is right and matters.
- Proposition 6 at reference 1 uses only flat inverses, so it is not circular.

**3.9 (CMP 99b, curved from flat): ADVANCE, conditional on F0.**
- The algebra of (3.27) was redone. S = 1 - DG'RD* kills D lambda for lambda in ker Q', and K-hat_1 D G'R f = DRf, so G_1 DR = DG'R. Taking adjoints, RD*G_1 Q* = 0 and RD*G_1 DR = R. Hence Q Pi = RD* Pi = 0 and the fibre inverse needs both subtractions. ran R = D*D ker Q' follows from R being the orthogonal projection onto ker(Q'G').
- The small-gauge series (3.24) keeps the covariant-Laplacian estimate for the uncorrected G_0: the perturbation is local first order, so Delta T_f^-1 (E T_f^-1)^n stays bounded. It loses that estimate for the Delta'_pi-corrected operators, as Balaban's Theorem 3.12 says. Section 5 uses the Laplacian only for G_0, H_0 and for flat operators, which is consistent.
- The three-error parametrix (3.25), the C' construction (3.95), and the mass commutator -S*aQ + Q*aS (3.102)-(3.104) are correct as sketched.
- F0's convention is the default one. CMP 99b (3.16)-(3.19) defines the row mass over b in Lambda_j and the site average Q'_j(U) lambda(y) = sum over B^j(y) of L^{-jd} R(U(Gamma)) lambda(x), which is the note's (7.19) with Balaban's contours. CMP 102 (154) lists only the bond cases with both ends in Lambda'_j or one end in the finer Lambda'_{j-1}. The test discussion after (7) says a missing bond has both ends in Lambda_{j-1}. Both fit only the reading Lambda_j = (bonds touching Omega_j) minus (bonds touching Omega_{j+1}). So Balaban's determining rows omit inward bonds, exactly as the outline's default does. F0 as stated "with his row conventions" is therefore the flat input the default problem needs; the auxiliary-boundary part is supplied separately in 7.9.
- One provenance correction (defect D1 below): CMP 99b proves Theorems 3.1-3.3 by "repeating the arguments of Sect. 2 in [2]" (p. 398), and its [2] is Balaban, CMP 89 (1983) 571-597, "Regularity and decay of lattice Green's functions". The Hoelder input (3.22) is of that paper's type. F0 is cited-pending on CMP 89 as well as CMP 95 and 96.

## 3. Sections 4-5: the common chart, the critical equation, second derivatives

**4 (CMP 102 Propositions 2-6): ADVANCE, conditional on Section 3 and F0.** Redone:
- Straightening: qT + C(T) = qA' - qH D + D = qA' and RD*T = RD*A' use only qH = 1 and RD*H = 0. The ball \|X\| <= r/B_0 is mapped into itself when 4C_2 B_0 r <= 1. Cauchy on radius 3r gives Lipschitz constant 9C_2 B_0 r. (4.2) follows by differentiating the fixed point.
- (4.3) re-expanded from F(T(A')). The quadratic part of -<H D(A'), J> is -(1/2)<A', W A'>, so Delta_1 = Delta_pi - W, and the four remaining terms are exactly as written. The force bound uses Delta_pi H = Q*(QGQ*)^-1 s^-1 - Q* a s^-1, which follows from G^-1 H = Q*(QGQ*)^-1 s^-1, DRD*H = 0 and QH = s^-1. The cubic action term is <eta^2 dA, sum [a_i, a_j]> because 1 - Re tr e^{i theta} has only even powers of theta. The eta F(U_0) A^3 term scales to at most alpha_0 r^2 s^-3.
- (4.5): for tangent dA, <dA, K_1 H_1 B> = <Q dA, .> - <RD* dA, D* H_1 B> = 0, and S H_1 B = H_1 B because RD*G_1 Q* = 0. The contraction numbers check: the image is at most j + B_0 C_4 (r+h)^2, the Lipschitz constant at most 4 B_0 C_4 (r+h), and the invariant radius 2j + 2h works once 9 B_0 C_4 (j+h) <= 1. The uniqueness ball is fixed before the existence ball, as it must be.

**5 (CMP 102 Proposition 7): ADVANCE, conditional on F0.** (5.1) re-derived: the Euler equation for all dA' in ker q gives Delta A' = Q* lambda - J + W A' - V~'(A'); P_0* kills ran Q*; P_0* G_0^-1 A_0 = G_0^-1 A_0 since Q A_0 = 0; P_0* G_0^-1 H_0 B = 0; and RD*A' = 0. This gives exactly (Delta + DRD*) A_0 = -P_0*J + P_0*W A' - P_0* V~'(A'). The Weitzenboeck split (5.2), the DPD* bound from (3.49), and the summation by parts for (Delta_pi - Delta) H B (only gauge-direction terms, which carry J) are correct. The note uses the Laplacian estimate only for the uncorrected G_0, H_0 and never for G_1, H_1. That respects CMP 99b Theorem 3.12.

## 4. The two resets and the depth induction (Sections 6, 7.2, 8)

**6 (Proposition 8, the radius reset): ADVANCE, conditional on F0.** I checked it line by line against CMP 102 pp. 300-304 (scan).
- (6.3) is (161), and B_3 = 72d^3L^3B_0S_* is (162). With (163), the linear term is at most (1/4) M_Delta max{B_3 eps_1, eps_0/2}, which is (164). The nonlinear term is at most (1/8) M' eps_0, which is (165)-(167). At the central pillar these give m/2 with m = max{B_3 eps_1, eps_0/2}. Then (3.11) gives regularity m/2 + Cm^2 <= m, which is (168).
- Iterating (6.6) on the same field and datum is legitimate: every smallness hypothesis is monotone in eps_0, and the output radius is again at most eps_0. The limit argument is an ordinary real inequality.
- The note proves criticality of the localized field from criticality alone. The localized constraint set lies inside the original one, by the semigroup law of the averages and the frozen outer bare layer; the restriction argument of 9.2 justifies this. Balaban uses minimality at this point (p. 301, "a minimum of this functional in the space (150)") although his Proposition 8 is stated for critical points. The note's version is the one Proposition 8 needs.
- Depth: the localized problem at a centre of layer j has j nested artificial layers, but every constant used is depth-free. Those are F0's constants (stated for the localized sequences), C_2 and C_4 from 3.5, and S_* from 3.7 (uniform once the separation is at least rho_sum). So B_3, R_1M_1 and a_5 are fixed before the depth. This reset is depth-uniform.

**7.2 (seam descent and the two-radius class): ADVANCE.**
- Exact lift: interior fine plaquettes are 1. Plaquettes with two parallel crossing links give V_k(c) 1 V_k(c)^-1 1 = 1. Corner plaquettes equal a coarse plaquette holonomy, so interior tests are copied with no factor. With internal links 1, every contour of an interior row crosses its face once, so the actual mean returns V_k(c) exactly.
- Seam: the outward-row error C(L)eps comes from closed loops in the fixed outer block. The middle pivot lies in exactly L of the L^4 straight segments, which gives derivative L^-3 Ad(T_c), and it lies in no other row. The contraction with \|(D f)^-1\| <= 2L^3 closes for C(L) eps L^3 < 1/2. The crossing links are inward bonds of level k-1, so they are free in the default convention and become determining after the merge.
- Class invariance: modifications are confined to the deleted seam's collar. Old collars are later lifted in the interior with no amplification. A gap of more than twice the collar width (rho > 2wL in the units used) keeps every remaining protected collar untouched. So (E, e) = (C_down e, e) persists to depth 0, and the seed loss is C_down once, not C_down^k.

**8 (conditional uniform orbit): ADVANCE, conditional on F0; this is where both resets enter, and both are depth-uniform.**
- *Reset 1 (inside the induction).* The depth-(k-1) orbit is regular at BE in its own units, hence C_1 BE with C_1 = C(L) L^3 as a depth-k reference. Its level-k averages equal V exactly, by the semigroup law and the exact pivot section, so the depth-k mismatch is zero. Sections 4-5 give radius C C_1 BE. Applying (8.1) with datum size E returns BE. The only requirement is C C_1 B C_down eps_1 <= a_5, which involves no depth.
- *Reset 2 (at the top).* The enlarged class gives B C_down eps_1. (8.1) applied with the original datum, whose tests are at most eps_1 everywhere, returns B eps_1.
- *Base case.* At depth 0 every fine link is prescribed. The test bound gives r <= CE, the current being at most 2(d-1) plaquette differences divided by eta^3.
- *Uniqueness.* Every competitor in U_k(eps_0) enters the chart about U_0 through the gauge theorem with alpha_0 = max(eps_0, C_1 BE) and zero mismatch. The fixed ball r_* is chosen before the data.

No depth factor survives. A grep of the note for "standard", "similar" and "assume" finds nothing used on the critical path beyond F0. The 7.5 alternative is explicitly not used.
