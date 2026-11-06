lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T16:56Z

# P8 positivity and limits ports: one line-by-line check (row 342)

First failing step: none, in `library/port/p8-positivity.md` and in `library/port/p8b-limits.md`.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker. Pinned at commit a81e94ca8. Check run 2026-11-06, 04:56Z to 05:15Z. This is one honest reading, not an audit, and it grants no status. Scope: `p8-positivity.md` (B5 = 6.1:lem-reflection-positivity with 6.1:cor-reflection-form; B7 = 6.4:thm-per-ball-bound with the 6.2 lemmas; B8 = 5.12:prop-subsequential-limits and 5.12:lem-limit-positivity) and `p8b-limits.md` (B10 = the 7.4 finite lemmas; B11 = 7.4:thm-infinite-volume (A)-(D); B12 = 7.5 and 7.6; B13 = 7.7:prf-reconstructed-space, with the continuation 7.7:prf-semigroup-hamiltonian). Codex wrote both ports. Source: the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) at 31a47c543775. CA-I, CA-II and the outline were fetched by URL into a scratch folder. Their SHA-256 values equal those at p9-witness.md lines 13-18. Balaban is credited where the ports cite him (CMP 116 (1.26), the H-TREE input). Kind of result: a check of a port of their proofs. No numerics were used, and no numeric job was needed (memory was 63% free).

## Findings

None of these breaks a statement. They are ranked by how much a reader could be misled.

| # | Where | Step | What is wrong | Kind | Repair |
|---|---|---|---|---|---|
| 1 | p8-positivity.md 797 and 814 | B8: admission of the slab observables to the link half-algebra | "Even centred lattices" is not defined. B5 covers the source's side-one torus only if the sites lie in eps'(Z+1/2)^4 and N_T L^K is even. Because L is odd, that means N_T is even. For other N_T, the plane x^0 = 1/2 holds sites, and H-TORUS-RP remains an input. The port does say this, but not in these words. | clarity, not a defect | State the condition N_T even, sites centred, at line 797. |
| 2 | p8-positivity.md 106; source II:60604 | B5: disjoint crossing families at the two planes | Confirmed: the printed "1 > eps" is false at K' = 0, which 6.2:def-cell-reflections admits (K' >= 0). The needed disjointness still holds at N/2 = eps, as the port shows. Under the per-ball floor m >= log_L ell >= 1, one also has N/2 >= L > eps. | harmless slip in the source | As in the port. |
| 3 | p8b-limits.md 154; source II:65871 | B10: a translation descends to T_m | Confirmed but only a wording slip: the source says tau_b "sends 2L^m Z^4 onto itself". It means that tau_b commutes with period translations. Nothing depends on the literal wording. | harmless slip in the source | As in the port. |
| 4 | p8b-limits.md 629; source II:66562, II:67995 | B11(D1): domain of H | The correction is right as a clarification. "Acting in the whole of" and "on all of" could be read as everywhere defined, which fails for an unbounded H (the port's l^2 example is right). The outline already says "densely defined" (SA:25611-25612). Nothing in B11-B13 uses the everywhere-defined reading. | wording | As in the port, domain (42). |
| 5 | p8-positivity.md 690-694 | B7 after the change of units: cell-side floor | The floor L^{m_1} >= L^{m_J} ell(n,R) is stronger than the source's m >= log_L ell. It is sufficient, since ell(n, R L^b) <= L^b ell(n,R) <= L^{m_1} by minimality. It is LSC's own clause (c) floor, and it is eventually met along H-FLOW (1). The port says this. | none needed | None. |
| 6 | p8-positivity.md 160, (P8.8) | B7: t >= 0 | t >= 0 is listed as a hypothesis. It follows from the first two inequalities of (P8.8) at v = 0: e^{-C_low N^4} <= Ztilde(0) <= e^{E_+ N^4}. The source also states it (def-localised-terms, "E_+ + C_low >= 0"). | simplification | Derive it rather than assume it. |

The port's own repairs and filled steps were redone by hand, and each one holds. They are: the explicit tensor-character series (P8.3), which removes the source's only analytic citation in B5 (Fourier decay of a C^infinity class function); the null case of Cauchy-Schwarz; the global Lipschitz gluing; the geometric tails of C_UV and C_face; the Schwarz-lemma step; the local conjugate power series; separability, the diagonal and the extension; the slab admission; the moment-cumulant identities; the Fourier estimate for order 5n+1; the positive-time density; the contraction (40); and the domains of H and P. No fabricated step, label or line anchor was found. Every cited anchor that was spot-checked (28 of them) holds. The 11 statement blocks in p8b section 14 are identical to their CA-II line ranges, by text comparison. Every ported label is PROVED in `library/sa-index/ca-full/index.tsv`.

## Verdict

- **B5** (6.1:lem-reflection-positivity and 6.1:cor-reflection-form): ADVANCE. It is proved, with no input beyond H0 (Haar measure and finite integration). First failing step none.
- **B7** (6.4:thm-per-ball-bound and the 6.2 lemmas, including LSC's change of units): ADVANCE. It is a proved implication from H-LOC, H-DOM, H-STAB/LSC and H-TREE. First failing step none.
- **B8** (5.12:prop-subsequential-limits and 5.12:lem-limit-positivity): ADVANCE. It is a proved implication from H-TORUS-BOUND, H-FIRST-PASSAGE, H-TORUS-FLOOR, H-KERNEL and H-TORUS-RP. B5 discharges H-TORUS-RP when N_T is even (finding 1). First failing step none.
- **B10** (7.4:not-finite-cutoff, lem-torus-transport, lem-lattice-symmetries, lem-half-space, lem-translation-modulus, def-centred-moments, lem-linearity, def-countable-family): ADVANCE. These are proved, with H-AN only. First failing step none.
- **B11** (7.4:thm-infinite-volume (A)-(D), 7.4:prf-equicontinuity, and the cluster-point and iterated-limit remarks): ADVANCE. It is a proved implication from H-CA, H-FLOW, H-PB, H-RP (= B5 on T_m), H-BLOCK, H-AN, H-KER, H-FOURIER and H-SPEC. First failing step none.
- **B12** (7.5:prf-limit-distributions, 7.5:prf-exact-invariance, 7.6:prf-centred-positivity): ADVANCE, on the same inputs. First failing step none.
- **B13** (7.7:prf-reconstructed-space, and 7.7:prf-semigroup-hamiltonian through II:68079): ADVANCE, on the same inputs. First failing step none.

This moves B5, B7, B8 and B10-B13 to "checked line by line by Claude, first failing step none". It closes none of their inputs. Still open, as before:
- H-LOC, H-DOM and H-TORUS-BOUND, that is, B3 at P6's standing. P6 is ported and not yet checked. Its inputs include 5.6:prop-polydisc-holomorphy ("Proof outstanding", II:46167) and the window-data statement (outstanding, II:2810-2812).
- The inputs of frozen LSC.
- H-TREE (Balaban CMP 116 (1.26)).
- H-KERNEL and H-KER, H-FOURIER, H-SPEC, H-BLOCK, H-CA, H-FLOW, H-FIRST-PASSAGE and H-TORUS-FLOOR.
- The T0 clauses that p8b section 13.5 excludes: full O(4), clustering, factorial growth, vacuum uniqueness, Wightman functions, the one-point limit, non-triviality and the forward cone.

The findings contain no correction of value to the account. Findings 2-4 are slips in wording. Nothing is posted; rule 6 applies.

Checked line by line by Claude (Mini worker).

## Section notes

### B5 (p8-positivity.md lines 26-144; source II:60440-60690)

- Statement block (lines 30-45) matches II:60440-60465, including the inversion rule for bonds parallel to e_mu.
- Lines 47-104. The port replaces the source's irreducible expansion, with its asserted Fourier decay, by the explicit series (P8.3) in R^{tensor q}, R = V + Vbar. Redone: Re tr W = chi_R(W)/(2d) with tr 1 = 1; a_q = x_0^q/(q!(2d)^q); sum_q a_q d_q^k = exp(x_0 (2d)^{k-1}). Irreducibility is never used, only unitarity and Haar invariance. The factorisation (P8.5) and (P8.6) was redone index by index and holds. Absolute convergence: |u| <= 1, so sum_alpha c_alpha |G_alpha|^2 <= prod_{x,nu} sum_q a_q d_q^6 < infinity.
- Line 106 (correction at the endpoint N/2 = eps). Redone for N = 2, eps = 1. The two crossing families are distinct edges, and each crossing plaquette uses two mu-links of one family. The same tangential bond can be b^+ for both planes. That is harmless, because a product of two functions of U_+ is a function of U_+.
- Lines 108-114 (positivity) and 133-144 (reflection form, Cauchy-Schwarz by G - tF). Redone; both hold.

### B7 finite lemmas (p8-positivity.md lines 146-410; source II:60692-62125)

- Lines 150-206 (hypotheses) match the source's two readings (II:60744-60762) and its outstanding inputs.
- Lines 210-235 (cells, group, parity, transport). Redone: k -> 2a-1-k; two reflections give an even translation; each direction is dihedral of order n_c; simple transitivity; sgn(g) = (-1)^{sum(k'-k)}; T_g T_h = T_gh from (U o g) o h = U o (gh); T_g maps A_c to A_gc. The four laws (P8.11) hold, using theta in G_ell and simple transitivity. This holds for n_c = 2.
- Lines 237-281 (chessboard value and estimate). Redone. c(F) = (G,G)_theta >= 0 at any face pair. The spreading sequence was checked: k -> 2b-1-k doubles an interval of length s <= n_c/2, and a longer one is completed. The zero-norm case gives |a(Y^0)|^{2^T} <= B^{2^T-1} a(Y^T), using a(Y^t) >= 0 for t >= 1. The labelled-filling maximum argument is right: R_max >= 1 > 0, so both branches of a maximiser are maximisers.
- Lines 283-296 (support placement) match II:61417-61505. The arc count, the component of length >= 4(R+1) > eps, and the translation identity were redone.
- Lines 298-344 (periodised weight). Redone: plaquettes read by a placed source lie in the open cell; T_g e^{A(v,U)} = e^{A(v o g^{-1},U)}; the parity grouping gives (P8.16). The gluing argument for the global Lipschitz bound is right, because the weight vanishes on all faces. The factor two on D_2 is right.
- Lines 348-388 (domain diameter, consequences (a)-(d)) match II:61874-62028 and were redone. Lines 390-408 (anchor count (P8.21), tree sum (P8.22)) were redone: there are at most 2 eta/s_j + 2 grid intervals per coordinate, with eta = R+2+2 s_j.

### B7 estimates and theorem (p8-positivity.md lines 415-706; source II:62127-64568)

- Lines 415-462 (UV bound (P8.23)-(P8.24)). Redone. A contributing domain reads sources 1 and 2, so d_j >= [d L^{K'-j}/(4M) - 4]_+. Cauchy on the circles |zeta_l| = (1-eta) r/(n ||h_l||) stays inside D_h. The filled tail is right: a(R,i) <= A_R L^{4i}. The ratio is L^4 e^{-alpha(L-1)L^i}, which is at most 1/2 once L^i >= (4 log L + log 2)/(alpha(L-1)).
- Lines 464-478 (face bound (P8.25)) were redone: group by the pieces that a domain reads, then use (P8.19) and (P8.22).
- Lines 480-508 (bounded logarithm). Redone: Schwarz's lemma for psi; the zero-norm variables by Liouville; the Cauchy circles give rho = 1/(2 r_frak (Q+1)), inside the logarithm domain. (P8.27) holds.
- Lines 510-558 (chessboard inequality). Redone: ||F_{c,z}||^J = Zhat(w^ch)/Zhat(0) <= exp{Re E(w^ch) + t N^4} by (P8.8) at w^ch, and N^4/J = ell^4. This is where H-DOM is read. (P8.30) follows by (P8.20). There are J|I_c| ball pieces in w^ch. (P8.29) holds.
- Lines 596-618 (holomorphy, mixed derivative). The local conjugate power series replaces the source's Reinhardt-domain argument, and it is right. The q >= 2 and q = 1 cases are right.
- Lines 620-662 (bulk cancellation, cumulant). Redone: (P8.35); the exponent is at most 2n C_face + q t ell^4 <= n(t ell^4 + 2 C_face), using t >= 0. The branch of log Z and the cumulant identity hold. (P8.33) holds with t visible.
- Lines 664-706 (LSC and units). Checked against lsc.md section 1, (4)-(8). (P8.36) is LSC (6)-(7). LSC section 6.1 removes the apparent circle, and B7 reads only LSC (5)-(5b), which do not use the per-ball theorem.

### B8 (p8-positivity.md lines 709-852; source II:59926-60178, II:679-748, II:2936-2952)

- Lines 713-749 (the statement, assumptions 1-4, floor (P8.39) and norm (P8.40)) match II:59926-59970 and II:679-748. H-TORUS-BOUND is B3(iv) at II:2937-2951.
- Lines 751-793 (proof). Redone: the m-independence (N_T L^K sites per side); complexification with factor 2^n; the telescoping bound (P8.42); rational-ball support products (3d margin, radius in (d/4, d/2)); separability of C^1_{B_j} in the sharp norm; nested-square Bolzano-Weierstrass and the diagonal; extension to every tuple by an eta/3 argument. H-KERNEL is kept as a named assumption, as in the source. Symmetry and lattice covariance (O(f)(iota_* U) = O(f o iota)(U)) hold.
- Lines 795-852 (limit positivity). The admission step is right when both time planes are link planes (finding 1). There, a time-space plaquette with barycentre a in (0,1/2) on the mesh has its time range inside [eps/2, 1/2 - eps/2]. This matches II:65290-65302. Redone: (P8.45); the square-free coefficient proof of (P8.46); the centring rule; the partition sum (P8.47), including the empty and singleton conventions; the positive distance between the two reflected families (compact sets in disjoint open slabs).

### B10 and the B11 extraction (p8b-limits.md lines 68-327; source II:65519-67010)

- Lines 29-66 (hypotheses) match (a)-(d) of 7.4:thm-infinite-volume (II:66412-66455), including odd L.
- Lines 70-117 (finite conventions; moment-cumulant (5)-(6) in the algebra with z_i^2 = 0). Redone: 2L^{m+K} site indices per side. The truncation to square-free monomials is a ring map, so (5) and (6) hold. Shift invariance holds.
- Lines 119-144 (transport). Redone: |x-y+2L^m k| >= 2L^m - 2 rho >= 2 rho + 4 when L^m >= 2 rho + 2. The exit-segment argument for the torus Lipschitz bound is right. Supports, distances, translations and W_4 hold.
- Lines 150-162 (lattice symmetries): finding 3. Lines 166-179 (positive slab) were redone. For a time-space plaquette k >= 0, so bond times lie in [eps/2, rho + eps/2], and the distance to x^0 = L^m is at least rho + 1. (9) holds.
- Lines 181-199 (translation modulus (10)) were redone, including the counterexample: g_s(0) = |s| and g_s(s e_1) = -|s|, so Lip g_s >= 2.
- Lines 201-252 (centred moments (11), Phi and Psi (12)-(13), the countable family (14)-(15)) were redone. The factor two between the componentwise and the Euclidean gradient norms is right.
- Lines 258-327 (diagonal extraction, (16)-(19), moving tests, cluster points, iterated limits (20)) were redone. (18) uses d/3 and R' = rho + d/3, and the eta argument closes. The zero-entry correction is right and harmless.

### B11-B13 (p8b-limits.md lines 329-674; source II:67014-68079)

- Lines 329-382 (distributions off the diagonals). Redone: an open set of diameter at most 2R lies in an open radius-2R ball about each of its points; (22) with the factor 2^n (40M)^n; the coefficient bound (24) by nu integrations by parts in a coordinate with |xi_a| >= |xi|/sqrt(4n); the shell count C 2^{(k+1)D}; convergence of (23) in every C^r; (25). nu = 5n+1 leaves the summable exponent -(4n+1), so the order is at most 5n+1.
- Lines 384-406 (exact invariance). Redone: |a - a_j| <= eps_j; the sets Q_{i,j} lie in B_{rho+|a|+1} with gaps d/2; (26) follows from (10) and (17).
- Lines 408-460 (centred positivity). Redone: conj(F_j(theta U)) = sum_q Phi((Theta Fbar)_q)(U), using xhat(theta p) = theta xhat(p) and the invariance of the means; (28); Hermitian symmetry by U -> theta U. The planes x^0 = 0 and L^m are link planes of T_m for every K, so B5 applies. The extension to D(Omega_{q,+}) by partitions of unity and (23) is right, including the q = 0 and q = 1 terms.
- Lines 462-551 (B13). Redone: Cauchy-Schwarz; (32)-(33); the separability estimate (34)-(36) with d_* = min{d_F/2, delta_F}; (37) with d_0 = min{d_F, 2 delta_F}; Q(F, T_t F) = Q(T_{t/2}F, T_{t/2}F) >= 0 by (38).
- Lines 553-674 (semigroup and momenta). Redone: (38)-(40) give the contraction, with r_k^2 <= r_{k+1} and r_k <= (M_F/q_F)^{1/2}. Also redone: strong continuity (41); injectivity; (42); the dyadic identification; uniqueness of H; H Omega = 0; SNAG; the commutant step; the vacuum support at p = 0; the W_3 covariance. Domain wording: finding 4.
- Section 14: each of the eleven blocks is identical to its stated CA-II line range.
