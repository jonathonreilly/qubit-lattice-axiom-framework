lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-23T13:59Z

# Check 1426: cross-provider check of row 1424 (`library/gap-rg-two-cycle-astra62.md`)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit 800f52987. One reading by one other model; not an audit.

Moves: the gate of row 1421 (next row 1), the test whether the normalized SU(2) 2^4 block has a four-dimensional signed decrement of kind K-II (row 1418). It decides whether the single-strand two-cycle reading is rejected and whether (7) is the surviving channel to pass on.

## Plan

1. Read row 1424 in full, and row 1421's definitions it uses (z_B, b, the mixed-plaquette labels, formula (3)).
2. Check in order: labels and mixed graph; prefactor C; matrix (1); corner subtraction (2) and traceless coefficient (3); axis swap and identity (4); product subtraction (5) and its scalar series; extension (6); U(1); hand check with H = (3/5, 4/5, 0, 0), K = (1/3, 2/3, 2/3, 0), recomputed with exact rationals in /tmp scratch; ring reading (7) and C_2.
3. Verdict per statement, at most ten defects, decisive outcome.

## Repo search

Searched `library/open-core.md` (564 lines) and the FINISH rows for two-cycle, axis swap or interchange, `(H^{-1}, K)`, `(h.k)^2` and `P_2`. The only hits are rows 1421, 1423, 1424, 1426 and 1430 of this chain. Nothing in open-core names the axis-swap cancellation or the ring scalar. Row 1424 cites row 1421 for the mixed-label formula and its equation (3). It cites Lemma FOREST and row 1339 for the forest and one-cycle reductions. I read the parts of row 1421 that the check uses: the conventions at line 34, z_B at line 96, and the mixed-label section at lines 127-152. Row 1424 credits the SA outline and the account (Ethan Sussman and Levent Alpoge, writing with Claude and Codex) only for the character coefficients and the half-trace. Its calculation is on the bare block and uses no SA statement. So this check needs no SA source.

## Step 1. Labels, prefactor C, matrix (1), subtraction (2), coefficient (3)

**Labels and mixed graph: HOLDS.** I recounted the occupied slots from the geometry of {0,1}^4. P's vertices have x_3 = x_4 = 0, so the bond in direction -3 is exterior at each of them. Each nonroot vertex of P meets the mixed faces of its two incident P edges, so its -3 bond holds two slots. The same holds for Q and the -1 bond. Bond (0,-3) holds the mixed faces of edges 0->e1 and e2->0, plus the outward faces (-3,-1) and (-2,-3), which gives four slots. Bond (0,-1) holds two Q faces and the faces (-3,-1) and (-1,-2). Bond (0,-2) holds only (-1,-2) and (-2,-3). The table is therefore correct. The mixed graph has 8 edges and 7 vertices, so it has two independent cycles. Every slot carries spin 1/2, and each bond admits an invariant.

**Prefactor C: HOLDS.** Row 1421 line 34 gives each face of spin n/2 the weight b_n^{1/4} per corner, with b_n = (n+1) I_{n+1}/I_1. This follows from e^{beta q}/A = sum_n b_n chi_{n/2}, with A = 2 I_1/beta. A mixed face has two corners in B and so carries b^{1/2}. An outward/outward face at 0 has one corner in B and carries b^{1/4}. The total is b^{8/2 + 3/4} = b^{19/4}. The seven bivalent unit tensors delta/sqrt2 sit on 3 + 3 nonroot bonds and on (0,-2), which gives 2^{-7/2}. This matches C = 2^{-7/2} b^{19/4}.

**p, r, t: HOLDS.** |p|^2 = (1/4)(2)(2) = 1, and the same holds for r. <p,r> = (1/4) tr(1) = 1/2. With t = (2r - p)/sqrt3, |t|^2 = (4 + 1 - 2)/3 = 1 and <p,t> = 0. Contracting H_{ij} gives L_p(G) = (1/2) tr(G) I = q(G) I and L_r(G) = G/2.

**Matrix (1): HOLDS.** The bridge closes into a single trace, so pp = tr(q(H) q(K) I) = 2 q(H) q(K) and pr = rp = tr(q(H) K/2) = q(H) q(K). Also rr = tr(HK)/4 = q(HK)/2. Whether the trace is tr(HK) or tr(HK^{-1}) depends on the strip directions. It does not affect any conclusion, because the 3<->4 swap exchanges the two (see Step 2). The trace words printed in the row, multiplied by C/4, give (1); I checked this by hand.

**(2) and (3): HOLD.** M_pp s s^T = C E[q q] [[2,1],[1,1/2]]. Only the rr entry survives the subtraction, and it equals (C/2) E[q(HK) - q(H) q(K)]. Then M_tt = (4 M_rr - 2 M_rp - 2 M_pr + M_pp)/3 = (C/3)(2 E q(HK) - 4 E qq + 2 E qq) = (2C/3) E[q(HK) - q(H) q(K)].

## Step 2. The swap and (4), (5) with its series, (6), U(1), the hand check, (7)

**Axis swap and (4): HOLDS.** Let sigma swap axes 1 and 2 and act on configurations by (sigma U)_e = U_{sigma^{-1} e}. Then sigma maps B_d onto itself, permutes its directed positive links and permutes its internal faces. Face orientations may reverse, but q(g^{-1}) = q(g). So product Haar, w_B, z_B and mu_B are invariant, for d = 4 and for d = 5. Sigma fixes 0, e3, e4 and e3+e4, so the rooted walk of Q is fixed and K(sigma U) = K(U). It sends the rooted walk of P, 0, e1, e1+e2, e2, 0, to its reverse, so H(sigma U) = H(U)^{-1}. Therefore E f(H,K) = E f(H^{-1},K) for every f. The identity H + H^{-1} = 2 q(H) I gives q(HK) + q(H^{-1}K) = 2 q(H) q(K). So E q(HK) = m_d, M = 2C m_d s s^T, and R_d = 0. The argument uses only two facts: mu_B is gauge invariant (not needed here), and mu_B is invariant under the swap. So the zero holds for every beta, in every d >= 4, and for every interior law with that symmetry, not only on I. I recomputed the hand values with exact rationals (scratch `/tmp/ym4d-check1426.hDXpmM/check.py`). Both quaternions have norm 1. The script prints q(H)q(K) = 1/5, q(HK) = -1/3 and q(H^{-1}K) = 11/15. The two integrand values of R_d/C are -16/45 and 16/45, and the averaged identity returns True. With a 2x2 matrix representation of the quaternions and an explicit index contraction of p and r at the two root bonds, the entries of M/C at this pair are pp = 2/5, pr = rp = 1/5 and rr = -1/6. These equal 2qq, qq, qq and q(HK)/2, as (1) states. This is a second implementation of the wiring (explicit indices rather than trace words). It uses my own strand model of the slots, so it is not independent of the geometry reading in Step 1.

**(5): HOLDS.** L_P = b^2 (1/4)(2 m_P) = b^2 m_P/2, from four mixed faces and four bivalent tensors around a closed strip. T = b^{3/4} 2^{-3/2} (2) = b^{3/4}/sqrt2, from three outward corners and three bivalent tensors. So T L_P L_Q = 2^{-5/2} b^{19/4} m_P m_Q = 2C m_P m_Q. In the orthonormal basis (p, t), s = (1, 0), so the residue 2C(m_d - m_P m_Q) p(x)p has zero tt entry, zero mixed entries and zero determinant.

**Series for the scalar: HOLDS.** The functional L is the Haar integral of monomials on S^3. For example E x_0^2 = 1/4, E x_0^4 = 3/24 = 1/8 (equal to the Beta integral (pi/16)/(pi/2)), and E x_0^2 x_1^2 = 1/24. The equalities z_B = A^{-F} S_00, m_d = S_11/S_00 and covariance = (S_11 S_00 - S_10 S_01)/S_00^2 hold by exchanging sum and integral, which is justified by the bound |sum p_f| <= F. The tail bound x^{N+1}/[(N+1)!(1 - x/(N+2))] is the geometric majorant of the series sum_{n>N} x^n/n!. Jensen gives S_00 >= 1. F = 24 for d = 4 and F = 80 for d = 5. No step of the rejection uses these series.

**(6): HOLDS.** F_lambda is gauge invariant, so F_lambda(U) = F_lambda(U^g) for the gauge g that sets the spanning-forest links to 1 with g_0 = 1. The two deleted edges then carry exactly H and K, up to inversion. Choose the singly read edge of P as the deleted edge. Then F_lambda = l(D_{1/2}(H) (x) D(K)) for a fixed linear functional l. The swap gives E[D_{1/2}(H) (x) D(K)] = E[q(H) I_2 (x) D(K)]. A dual strand gives the same result, since conj(H) + conj(H)^{-1} = 2 q(H) I. The root gauge then averages D(K) blockwise to chi_j(K)/(2j+1). D(K) is block diagonal on the sum of V_j (x) M_j, so no off-diagonal blocks occur. Attached trees and separate forest components contribute nothing beyond l, because their links are gauged to 1 or have product Haar law (Lemma FOREST). One remark on scope: on a square whose edges carry different strand numbers, the edge with the fewest strands decides, because any edge can be the deleted one. So the hypothesis of (6) is: some edge of P or of Q carries exactly one fundamental.

**U(1): HOLDS, and it says little.** At a four-slot bond with fixed charges the whole tensor space is one-dimensional, so p = r and X = r - <p,r> p = 0 identically. The fixed-charge zero therefore holds for every U(1) reading of this shape, with or without integration. In this channel the U(1) test cannot separate a non-abelian mechanism from no mechanism. It is a necessary condition only.

**(7) and C_2: HOLDS, with one wording correction (defect 2).** There are 16 mixed faces (b^8), four outward corners (b^1) and 12 nonroot bivalent tensors (2^{-6}), so C_2 = b^9/64. The insertion of t is L_t(G) = (2 G/2 - q(G) I)/sqrt3 = (G - q(G) I)/sqrt3, which is the vector part h over sqrt3. Four t's give 1/9. For pure quaternions, the real part of (hk)^2 is 2(h.k)^2 - |h|^2|k|^2, and h h k k = |h|^2 |k|^2. The trace is twice the real part. I checked these identities and the (7) combination exactly on 200 random rational unit quaternions (scratch `ring.py`, output `ring trace identities True`). Then (Y_alt + Y_grp/3) = (C_2/9) E[4(h.k)^2 - (4/3)|h|^2|k|^2] = (4 C_2/9) E T, with T = (h.k)^2 - |h|^2|k|^2/3. The same-angle reference of Y_alt is (C_2/9) E_R[2(2(h.Rk)^2 - |h|^2|k|^2)] = -(2C_2/27) E|h|^2|k|^2 = -Y_grp/3. So (7) is Y_alt minus its reference, the reading that row 1425 froze.

## Step 3. Lemma L2 (new here): the connected content of the two-square block

I grepped `library/open-core.md` and the FINISH rows for the parity decomposition of D_j(H) under inversion and for "unique connected scalar", with no match. Rows 1425 and 1430 compute E_4 T, but neither states this lemma. Proved by Claude here, not yet checked by the other model.

**Lemma L2.** Fix the two rooted squares P and Q of row 1424 and any exterior label lambda in the class of (6), but with no hypothesis on strand numbers. On the deleted edges, let P carry the representation D and Q carry D'. For each square, take the smallest such representation over its four edges. Then:

(a) The coefficient of R_B/z_B at lambda is a_lambda l(E[D(H) (x) D'(K)]). After the two swaps and the root conjugation, E[D(H) (x) D'(K)] depends on (H,K) only through scalars of the form E[<Phi_L(H), Psi_L(K)>], where L runs over the even integers and Phi_L, Psi_L are the conjugation-covariant components of D and D' in the spin-L part of End(D) and End(D').

(b) The L = 0 terms are products of class functions. They equal the independent-conjugation reference plus scalar covariances such as m_d - m_P m_Q. The colour-sensitive (connected) part is the sum over even L >= 2.

(c) If one square carries only a single fundamental on some edge, then L_max = 1 on that side, and the connected part is zero. This is (6).

(d) If both squares carry spin at most 1 on their deleted edges (two fundamentals on every edge reduce to V_1 + V_0), then the connected part of every such reading is kappa_lambda E T for one scalar T = (h.k)^2 - |h|^2|k|^2/3. Here kappa_lambda is a constant that depends only on the exterior contraction, not on the interior law.

*Proof.* Conjugation covariance: H -> g H g^{-1} acts on End(D) by Ad, so the component of D(H) in the spin-L summand is a covariant map S^3 -> V_L. Every such map has the form f(h_0) Y_L(h), where Y_L is a harmonic polynomial of degree L in the vector part h. Inversion keeps h_0 and sends h to -h, so this component changes sign by (-1)^L. The swap of axes 1 and 2 preserves mu_B, fixes K and inverts H, so every odd-L component of H has zero mean against any function of K. The swap of axes 3 and 4 does the same for K. Common root conjugation projects End(D) (x) End(D') onto its invariants, and by Schur these pair V_L only with V_L. This proves (a). Since L = 0 components are class functions, (b) follows. For (c), End(V_{1/2}) = V_0 + V_1 has no even L >= 2. For (d), End(V_1) = V_0 + V_1 + V_2. The spin-1 matrix of H satisfies R(H^{-1}) = R(H)^T, and its symmetric part is (h_0^2 - |h|^2) I + 2 h h^T, so its V_2 component is 2(h h^T - |h|^2 I/3). The invariant pairing of two V_2 components is tr[(hh^T - |h|^2 I/3)(kk^T - |k|^2 I/3)] = T. With D = V_1 + V_0, the off-diagonal blocks of D(H) vanish, so no other V_2 component appears. QED.

*What L2 adds.* The stabilizer of 0 among the symmetries of the block that preserve P and Q is generated by (12), (34) and (13)(24). These act on the reading by h -> -h, k -> -k and the exchange of h and k. Each of them preserves T. So no symmetry of the block kills T, and its sign is a dynamical question, as row 1424 says. L2 also shows that in the two-strand class every reading's connected part is a fixed multiple of the single moment E T. This bears directly on the first question of check 1431. The crossed-matching decrement of row 1430, X - R = a_2 N/z_4 with N = z_4 E_4 T, is necessarily the row-1425 moment, with a different constant kappa_lambda. Whether a reading shows a decrement or an increment depends only on the sign of kappa_lambda E T relative to its reference. Choosing the reading chooses that sign. By the rule "Equivalent is not progress", the crossed matchings carry no information beyond row 1425's interval for E_4 T. A genuinely new scalar first appears with spin 3/2 or more on every edge of one square (the radial weights f(h_0) then enter), or with L = 4 (spin 2 on both).

## Verdicts

| Statement of row 1424 | Verdict |
|---|---|
| Labels, mixed graph, two independent cycles | HOLDS (CORRECT-NO-ADVANCE) |
| Prefactor C = 2^{-7/2} b^{19/4} | HOLDS |
| Matrix (1) | HOLDS (explicit index contraction at the test pair: 2/5, 1/5, 1/5, -1/6) |
| Corner subtraction (2), traceless coefficient (3) | HOLDS |
| Axis swap: preserves mu_B, maps (H,K) to (H^{-1},K); identity and (4) | HOLDS, for every beta, d >= 4 and every swap-invariant interior law |
| Product subtraction (5) and the series S_ac with its tail and Jensen bound | HOLDS |
| Extension (6) to every reading with a single fundamental on some edge of P or Q | HOLDS |
| U(1) statement | HOLDS, but vacuous in this channel (defect 1) |
| Hand check H = (3/5,4/5,0,0), K = (1/3,2/3,2/3,0) | HOLDS (exact: 1/5, -1/3, 11/15, -16/45, 16/45) |
| Ring reading (7) and C_2 = b^9/64 | HOLDS AFTER CORRECTION of wording (defect 2) |

Overall: **HOLDS.** No line fails. Checked line by line by Claude Opus 5.5 high, first failing step none. Row 1424 was written by gpt-6.2-astra max. This is a check and grants no status.

## Defects (ranked by what each affects; none breaks a conclusion)

1. **The U(1) criterion carries no weight in this channel.** At a four-slot bond with fixed U(1) charges the tensor space is one-dimensional, so X = 0 for every reading, before integration. The same holds for the t-insertions of rows 1425 and 1430. The "exact zero at fixed U(1) charges" in their acceptance rules is automatic, so it separates nothing. A test that can fail is needed, for example the compact U(1) block with charge-two links, or the same reading in SO(3).
2. **(7) is not one coefficient.** Y_alt and Y_grp are coefficients at two different exterior labels. Their combination is the connected part of Y_alt only because the same-angle reference of Y_alt equals -Y_grp/3 (Step 2). Each sign also depends on the orientation of the second strip of a square: reading H^{-1} on it flips both Y_alt and Y_grp. Only the sign of E T is convention free. Row 1425 froze a magnitude, which is consistent with this.
3. **The direction of the bridge is not pinned.** Whether rr reads tr(HK) or tr(HK^{-1}) is not fixed. This is harmless, because the 3<->4 swap exchanges the two.
4. **The scope is understated.** The zero in (4) and (6) is a symmetry identity. It holds for every beta, for every d >= 4 and for every gauge-invariant interior law that is invariant under the swap, not only on the band I. "Throughout [2, 513/256]" is true but weaker than what was proved.

## Decisive outcome

- **The single-strand two-cycle reading is rejected as stated.** The rejection is exact. It rests on the swap of axes 1 and 2 (or 3 and 4) and on H + H^{-1} = 2 q(H) I, and it covers every exterior contraction in which some edge of P or Q carries exactly one fundamental.
- **(7) is the right surviving channel, and it is the only one at two strands.** By Lemma L2 (Step 3; proved by Claude here, not yet checked by the other model), the connected content of any reading with spin at most 1 on every edge of both squares is kappa_lambda E T, where T = (h.k)^2 - |h|^2|k|^2/3. No symmetry of the block kills T.
- **Consequence for check 1431.** Every reading in row 1430's two-strand class reads this same moment, so the crossed-matching decrement is E_4 T of row 1425 with a constant of the other sign. Under "Equivalent is not progress" it is not a new signal. A new scalar first needs spin 3/2 on every edge of one square, where E[h_0 T]-type radial weights enter, or spin 2 on both squares (L = 4).

Next rows suggested (the lead decides):
1. Lean replay of the E_4 T interval (rows 1425 and 1430). Decisive outcome: whether the one surviving scalar is strictly negative on I.
2. A three-strand screen: the leading Taylor coefficient of E[h_0 T] and of the L = 4 scalar on the 2^4 block. Decisive outcome: whether any scalar other than E T exists with the sign a decrement needs, before any four-direction inclusion.

Scratch: `/tmp/ym4d-check1426.hDXpmM/` (`check.py`, `ring.py`, exact Fractions, run with `python3 -I`). No code was committed. No Lean was run.
