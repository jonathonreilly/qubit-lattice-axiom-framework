lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T16:56Z

# P8 positivity and limits ports: one line-by-line check (row 342)

Status: in progress (started 2026-11-06T04:56Z). Sections are written as they are checked.

Pinned at commit a81e94ca8. Scope: `library/port/p8-positivity.md` (B5, B7, B8) and `library/port/p8b-limits.md` (B10-B13). Codex wrote both ports. Source: the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) at 31a47c543775, CA-I and CA-II, fetched by URL into a scratch folder. Kind of result: a check of a port of their proofs.

## Working notes, section by section

### B5 (p8-positivity.md lines 26-144; source II:60440-60690)

- Statement block (lines 30-45) matches II:60440-60465, including the inversion rule for bonds parallel to e_mu.
- Lines 47-104. The port replaces the source's irreducible expansion, with its asserted Fourier decay, by the explicit series (P8.3) in R^{tensor q}, R = V + Vbar. Redone: Re tr W = chi_R(W)/(2d) with tr 1 = 1; a_q = x_0^q/(q!(2d)^q); sum_q a_q d_q^k = exp(x_0 (2d)^{k-1}). Irreducibility is never used, only unitarity and Haar invariance. The factorisation (P8.5) and (P8.6) was redone index by index and holds. Absolute convergence: |u| <= 1, so sum_alpha c_alpha |G_alpha|^2 <= prod_{x,nu} sum_q a_q d_q^6 < infinity.
- Line 106 (correction at the endpoint N/2 = eps). Redone for N = 2, eps = 1: the two crossing families are distinct edges, and each crossing plaquette uses two mu-links of one family. The same tangential bond can be b^+ for both planes, which is harmless because a product of two functions of U_+ is a function of U_+. Correct and harmless; the source's K' range is not needed.
- Lines 108-114 (positivity) and 133-144 (reflection form, Cauchy-Schwarz by G - tF). Redone; both hold.
- B5 verdict: first failing step none.

### B7 finite lemmas (p8-positivity.md lines 146-410; source II:60692-62125)

- Lines 210-235 (cells, group, parity, transport). Redone: k -> 2a-1-k; two reflections give an even translation; each direction is dihedral of order n_c; simple transitivity; sgn(g) = (-1)^{sum(k'-k)}; T_g T_h = T_gh from (U o g) o h = U o (gh); T_g maps A_c to A_gc. The four laws (P8.11) hold, using theta in G_ell and simple transitivity. Holds for n_c = 2.
- Lines 237-281 (chessboard value and estimate). Redone. c(F) = (G,G)_theta >= 0 at any face pair. The spreading sequence was checked (k -> 2b-1-k doubles an interval of length s <= n_c/2; a longer one is completed). The zero-norm case gives |a(Y^0)|^{2^T} <= B^{2^T-1} a(Y^T), using a(Y^t) >= 0 for t >= 1. The labelled-filling maximum argument is right: R_max >= 1 > 0, so both branches of a maximiser are maximisers. First failing step none.
- Lines 283-296 (support placement) match II:61417-61505. Arc count, the component of length >= 4(R+1) > eps, and the translation identity were redone.
- Lines 298-344 (periodised weight). Redone: plaquettes read by a placed source lie in the open cell; T_g e^{A(v,U)} = e^{A(v o g^{-1},U)}; the parity grouping gives (P8.16). The gluing argument for the global Lipschitz bound is right, because the weight vanishes on all faces. The factor two on D_2 is right.
- Lines 348-388 (domain diameter, consequences (a)-(d)) match II:61874-62028, redone. Lines 390-408 (anchor count (P8.21), tree sum (P8.22)) redone: at most 2 eta/s_j + 2 grid intervals per coordinate with eta = R+2+2 s_j.
- No defect in this block.

### B7 estimates and theorem (p8-positivity.md lines 415-706; source II:62127-64568)

- Lines 415-462 (UV bound (P8.23)-(P8.24)). Redone. A contributing domain reads sources 1 and 2, so d_j >= [d L^{K'-j}/(4M) - 4]_+. Cauchy on the circles |zeta_l| = (1-eta) r/(n ||h_l||) stays inside D_h. The filled tail is right: a(R,i) <= A_R L^{4i}; the ratio is L^4 e^{-alpha(L-1)L^i}, at most 1/2 once L^i >= (4 log L + log 2)/(alpha(L-1)).
- Lines 464-478 (face bound (P8.25)) redone: grouping by the pieces that a domain reads, then (P8.19) and (P8.22).
- Lines 480-508 (bounded logarithm). Redone: Schwarz's lemma for psi; the zero-norm variables by Liouville; the Cauchy circles give rho = 1/(2 r_frak (Q+1)), inside the logarithm domain. (P8.27) holds.
- Lines 510-558 (chessboard inequality). Redone: ||F_{c,z}||^J = Zhat(w^ch)/Zhat(0) <= exp{Re E(w^ch) + t N^4} by (P8.8) at w^ch (this is where H-DOM is read), and N^4/J = ell^4. (P8.30) by (P8.20). There are J|I_c| ball pieces in w^ch. (P8.29) holds.
- Lines 596-618 (holomorphy, mixed derivative). The local conjugate power series replaces the source's Reinhardt-domain argument and is right. The q >= 2 and q = 1 cases are right.
- Lines 620-662 (bulk cancellation, cumulant). Redone: (P8.35); the exponent is at most 2n C_face + q t ell^4 <= n(t ell^4 + 2 C_face), using t >= 0. Note: t >= 0 follows from (P8.8) at w = 0. The branch of log Z and the cumulant identity hold. (P8.33) holds with t visible.
- Lines 664-706 (LSC and units). Checked against lsc.md section 1 (4)-(8). (P8.36) is LSC (6)-(7). ell(n, R L^b) <= L^b ell(n,R) holds by minimality. The floor L^{m_1} >= L^{m_J} ell(n,R) is stronger than the source's m >= log_L ell, and the port says so; that floor is LSC's own clause (c).
- B7 verdict: first failing step none. It is a proved implication from H-LOC, H-STAB/LSC, H-TREE and H-DOM.
