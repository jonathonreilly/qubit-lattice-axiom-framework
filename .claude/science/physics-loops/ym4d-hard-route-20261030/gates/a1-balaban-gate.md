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
