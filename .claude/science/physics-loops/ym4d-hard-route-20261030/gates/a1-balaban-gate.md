lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T05:02Z

# Gate: `library/a1-balaban.md` (row 91)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, statement pinned at d32f4da23. The gated note was written by Codex (row 81). This is one cross-provider read by hand, not an audit, and it grants no status. Balaban's CMP 98, 99 (75-102), 99 (389-434) and 102 were read from the owner's legal copies in `~/ym4d-papers/` (OCR text checked against the PDF where the formula matters); nothing from them is copied here beyond short statements.

**Result: no step fails.** Every gated section is ADVANCE (9.3 is CORRECT-NO-ADVANCE), conditional on the flat input F0. Both resets of Section 8 are depth-uniform, and every OCR reconstruction listed in Section 11 is confirmed in the scans. Four defects, none breaking: D1, F0 also rests on CMP 89 and its port must recheck the level-0 seam; D2, the layer gap must be chosen after the collar and reset lengths; D3, one identity-theorem sentence in 9.1; D4, wording in Section 6. Details are in Sections 7-8 below.

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

The scan of (161) also shows its far term uses the axial linear growth (d(y_1,y_2) + M_Delta) eps_0, not the global bound the note's Section 6 names; see D4.

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
- F0's convention is the default one. CMP 99b (3.16)-(3.19) defines the row mass over b in Lambda_j and the site average Q'_j(U) lambda(y) = sum over B^j(y) of L^{-jd} R(U(Gamma)) lambda(x), which is the note's (7.19) with Balaban's contours. CMP 102 (154) lists only the bond cases with both ends in Lambda'_j or one end in the finer Lambda'_{j-1}. The test discussion after (7) says a missing bond has both ends in Lambda_{j-1}. Both fit only the reading Lambda_j = (bonds touching Omega_j) minus (bonds touching Omega_{j+1}). So Balaban's determining rows in CMP 99a, 99b and 102 omit inward bonds, exactly as the outline's default does. F0, stated "with his row conventions" as CMP 99b's U = 1 case, is therefore the flat input the default problem needs; the auxiliary-boundary part is supplied separately in 7.9. His CMP 96 differs at level 0, which matters only for how F0 gets proved (D1).
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

## 5. Sections 7.6-7.10: transport to the outline's actual average

Checked against the outline at `31a47c543775` (fetched to a scratch folder): (1b) setup L9593-9657, Theorem 1 L9660-9668, order of choice L9916.

**7.6 (direct row estimates): ADVANCE, given the local gauge (7.10).**
- Column norm. A fine link lies in at most L of the L^4 straight segments of a row, and in at most two rows, so the one-step column norm is about L^-3 against row norm L. Both norms are submultiplicative, which gives (7.15). For q_j = a_j/s the derivative is n^-1 P_{j,0}, with row sum C and column sum C n^-4.
- Bootstrap (7.12)-(7.13). It closes in the separated form. The curvature recursion has only the multiplicative factor (1 + C_L alpha_r). The potential recursion's inhomogeneous term C_L omega_r / t_{r+1} sums to a fixed multiple of alpha, so K is chosen after that transfer and alpha after K.
- (7.17) recounted. For fixed b and c: outer coefficient <= C m_r^-3 (column bound of P_{j,r+1}); one-step Hessian with one leg fixed <= C_L; fixed inner leg <= C n_r^-3; summed inner leg <= C n_r. Together this is C_L m_r^-3 n_r^-2 = C_L L^3 n_r / n^3, summing to C_L s (eta/s)^4.
- (7.18) follows by Schur with the mass norm, which is F0's \|\|s^-1 A\|\|_2 energy term.
- (7.10) needs a gradient bound, so axial gauge would not do: transverse differences of axial potentials are not controlled by curvature alone. The note takes it from Proposition 6, conditional on F0, which is correct.

**7.7 (shared-node readout): ADVANCE.** Q'_p (Q'_p)* = 1 in the physical pairings (s_y^4 L^{-4j} = eta^4). (7.20) is the semigroup law at an outer end. (7.22) is the linearized covariance. In (7.23), h_{j-1} = 1 on an all-assigned outer block forces h_j(z) = 1. The reduced-datum inverse D^-1 - D^-1 T D^-1 holds because T D^-1 T = 0. This matches the outline's "Reduced datum" paragraph (triangular, v_z reads only interior bonds of B(z)). The outline's pillar average Q'(lambda)(y) = L^{-4j} sum Ad(T(y,x)) lambda(x) and Balaban's CMP 99b (3.19) are the same map up to the contour family, so at U = 1 they agree.

**7.8 (local perturbation steps on actual rows): ADVANCE.** The site version of (7.15)-(7.16): each one-step transported site average has row sum 1, column sum L^-4, and departure C_L alpha_r. These sum by (7.13). The cutoff commutator Q(c,b)[h(b) - h(c)] is C/M. The section's own two caveats (global parametrix on the new boundary; nonlinear Z-norm normalization) are exactly what 7.9 and 7.10 then supply.

**7.9 (boundary inverse on the auxiliary first member): ADVANCE.**
- ran R = D*D ker Q', with ker Q' vanishing off Omega_1. So R has no entries beyond one step, and DRD* none beyond two.
- (7.24): the curl form is at least 0 and at most C eta^-2 by \|sum v_i\|^2 <= 4 sum \|v_i\|^2. With the Wilson correction at most C eps eta^-2, this gives (a/2) eta^-2 <= K <= C_a eta^-2 for eps < a/(2C).
- The series (7.25) has ratio 1 - a/(4C_a) and range two per factor, so entries vanish until 2m eta >= dist. This gives (7.26) with weight tau^-1 ~ eta^2. Differences cost eta^-1 and eta^-2, which gives F0's weights at s = eta.
- The cover defect is C/M + CM alpha + Ce^{-cM}. The argument is shape-independent and uses no Fourier transform. Correct.

**7.10 (nonlinear normalization): ADVANCE.** (7.30) uses the flat coefficient L for the paired-site increments. The plaquette commutation gives the inhomogeneous term C L^2 omega_r delta = C_L alpha delta t_r^2, which is summable after division by t_{r+1}. The constant-family property of (7.29) makes every nonlinear one-step term contain a difference, hence C_L(r_* + delta) delta t_r, which sums to (7.28). Complex frames are counted with exp(C delta sum t_r), not exp(C delta j). At a seam only (7.20) is added. No depth factor.

## 6. Section 9: holomorphy, representative, restriction

**9.1: ADVANCE, with one sentence to add.** The contraction with G_1 J = 0 and radius 2h is uniform on \|\|B\|\| < r_B. Uniform limits of holomorphic iterates are holomorphic. The recursive axial gauge is unique; conjugators have norm exp(C\|\|B\|\|/(1-L^-1)). Real overlaps agree by orbit uniqueness, so the representative is continuous, hence Borel. Complex overlaps agree by the identity theorem; the overlap of two balls with real centres is convex and meets R^n in an open set.
The sentence to add: the second-order part of (9.1) cites the Euler equation (5.1). That equation was derived for real critical points by thickening the real slice. For complex B it holds because both sides are holomorphic in B and agree on real B. This is the identity theorem the section already uses, but it must be invoked here.

**9.2: ADVANCE.** Each case of the row bookkeeping was checked. An old row with an endpoint in Omega'_j cannot touch Omega'_{j+1}. Otherwise its carrier lies outside Omega'_j and is fixed by descent to level 0, using the semigroup law and (7.20). Varying bonds touch Omega'_1, so their plaquettes lie in Omega'_0. Scales only shrink, L'(p) <= L(p), so regularity persists. Orbit uniqueness then gives (9.3). The note correctly says uniqueness alone would not.

**9.3: CORRECT-NO-ADVANCE.** The literal-identity case is immediate. The note rightly leaves the general torus comparison to Theorem 6(c).

**10: no verdict needed.** (10.1) was checked: tr E = -det E from det(1+E) = 1, \|det E\| <= \|\|E\|\|^2, and both tent sums equal 1. The pointed-core clause (10.2) is honestly left open.

## 7. Defects, ranked by what each breaks

None breaks the conditional theorem or the consumer's statement. Repairs are marked unproved where they are more than a sentence.

**D1. F0's provenance is incomplete, and its port has one convention check (affects how F0 gets discharged, not the implication).**
- Most of F0's statement is the U = 1 case of CMP 99b Theorems 3.1-3.3, (3.48) and (3.132), which are in hand; the note says so in 3.9.
- The proof is not in CMP 99b. Balaban proves those theorems "by constructing a random walk representation similar to that in (2.40), but with different boundary conditions used, and then repeating the arguments of Sect. 2 in [2]" (p. 398). Here [2] is CMP 89 (1983) 571-597, "Regularity and decay of lattice Green's functions", the source of the Hoelder estimates (3.22). So F0 is cited-pending on CMP 89 as well as CMP 95 and 96.
- The outline (L9649) records that CMP 96 (2.3) keeps the level-0 inward bonds (Lambda_0 = Omega_1^c). CMP 99b (3.16), via Lambda_j = Omega_j^(j) \ Omega_{j+1}^(j), and the default problem omit them. So porting F0 from CMP 95/96 is not a verbatim citation at the first seam: the bare bonds crossing dOmega_1 are free in the default problem. The coercivity and kernel bounds there must be rechecked with only the level-1 outward rows and the gradient term controlling them (unproved here, expected routine).
- Repair: relabel F0 as "CMP 99b Thms 3.1-3.3, (3.48), (3.132) at U = 1; proofs in CMP 89, 95, 96, with the level-0 seam rechecked in the difference convention", and add CMP 89 to the texts `lit-balaban.md` lists as not yet reached.

**D2. The order of choice in Section 8 places the layer gap too early (breaks nothing; one line to fix).** The list puts "the summation gap" before "localization size and auxiliary boundary width". The theorem's gap must exceed four lengths:
- rho_sum of 3.7, i.e. (rate) x rho >= C log L;
- the auxiliary collar 4M eta + 4L eta plus a stencil, with M the parametrix side of 7.9;
- a multiple, depending on L, of the reset length R_1M_1 of (163). The enlarged cube of Section F, of side (2M + 4R_1M_1) in the coarser layer's units, must lie in two consecutive layers, and near a seam it can reach across the finer layer. So CMP 102 (1) needs roughly R >= 6L R_1;
- twice the descent collar of 7.2.

All four depend only on L and F0's constants. The gap can therefore be fixed after them and before the radii. This is the outline's order at L9916 (propagator constants; then 𝔐 and rho = R_1𝔐 with (rate) x rho >= C log L; then the radii; then M), and the outline puts no upper bound on 𝔐, rho, M. The 7.9 parametrix side is a walk-scale constant, chosen before rho, and is not the outline's late localisation side M. Balaban's own "R >= R_1" in CMP 102 (1) is equally loose on this point.

**D3. 9.1 uses (5.1) at complex B without saying why it holds there.** One sentence: (5.1) is an identity between functions holomorphic in B that holds for real B, so it holds on the connected complex ball by the identity theorem.

**D4. Section 6 wording, cosmetic.** "The coarse global bound on the far part" should be Balaban's axial linear growth \|B(c)\| <= C(d(y_1, c) + M_Delta) eps_0, which is (161) and is what makes M_Delta = 1 at the pillar. With the crude bound C M eps_0 one only needs R_1M_1 larger, since x e^{-ax/2} -> 0.

Positive findings worth carrying forward:
- (a) Balaban's rows (CMP 99a (1.5), CMP 99b (3.16), CMP 102 (154) and the test discussion after (7)) are the difference reading. So the default no-inward convention is his, at levels j >= 1 in all four papers read, and at level 0 in CMP 99a/99b/102.
- (b) The note's localization by criticality, not minimality, is the version Proposition 8 actually needs; Balaban's p. 301 uses minimality.
- (c) The complex regularity of Phi on the datum polydisc, which the a3-derivative gate kept inside P81, is supplied by (9.2). The conjugators to the axial representative have norm and inverse norm at most exp(C\|\|B\|\|/(1-L^-1)), so plaquette norms are preserved up to a fixed factor.

## 8. Verdict

| Section | Verdict |
|---|---|
| 3.5, 3.6, 3.7 | ADVANCE (unconditional rebuilds; OCR reconstructions confirmed in the scans) |
| 3.8, 3.9 | ADVANCE, conditional on F0 (D1 for provenance) |
| 4, 5 | ADVANCE, conditional on F0 |
| 6 (reset) and 8 (depth induction, both resets) | ADVANCE, conditional on F0; both resets depth-uniform; D2, D4 |
| 7.2 (descent, two-radius class) | ADVANCE |
| 7.6, 7.7, 7.8, 7.9, 7.10 | ADVANCE (7.6 and 7.8 given the local gauge (7.10), which is F0-conditional) |
| 9.1, 9.2 | ADVANCE (D3 for 9.1) |
| 9.3 | CORRECT-NO-ADVANCE |

Depth of check. Sections 3.5-3.7, 4-6, 7.2, 7.6-7.7, 7.9-7.10 and 9 were redone step by step. In 3.8, 3.9 and 7.8 the identities, the reset structure and the comparison with Balaban's text were redone; the parametrix and perturbation estimates were followed as the sketches they are, not re-derived constant by constant.

**First failing step: none.** What stands after this read: F0 implies the outline's default A1 on separated sequences. That is (1b) Theorem 1 (one regular critical residual orbit, linear curvature and current bounds, the unique axial representative), Theorem 3's first half (uniform holomorphic datum balls and the Borel real representative), and the exact restriction of Theorem 6(b). The constants are independent of the depth, the volume and the datum, provided the gap is chosen as in D2. This is P81 as rows 84 and 85 consume it, now conditional on F0 alone.

**Open:**
- F0: CMP 89, 95, 96 not in hand, plus the level-0 seam check of D1.
- The pointed-core admission clause (10.2).
- The kept-inward variant.

Row 81 counts as this conditional theorem, not as closed A1.
