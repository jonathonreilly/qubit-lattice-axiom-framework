# ROWS gate: line-by-line check of library/rows.md

First failing step: none

Scope of this check: rows.md read whole by section (§§1-8, Result). Context read: dr.md L1-130 and §3 (L168-222); pw.md §§1-2, §4, §5, §6, §6.1, §7, §8, §9; nl-r9.md §§3-6; cp12.md L36-66; o1-decoupled Definition D (L105) and Lemma P proof (L125); a3-derivative-gate L39-60; drlocp.md L56 (UNQ); d3-local.md L81-86. SA quotations checked against ym4.tex at the cited lines (below). Frozen notes (DR, PW, P82, CP12, IN1) are taken as given; their correctness is not re-checked here.

## §1 (L5-105): scope and constants

- L64: D_R = 8(D_0+r_g+L+1) is fixed from L-dependent geometry only. Correct.
- L75-83, (3): ceilings chosen after A, rho, G. The fourth condition (L81) "A eta|h| <= 1/4 for ||h||_X <= 4 r_R" does not "follow from eta <= m_b" (L85); it reduces, by eta|h(b)| <= m_b|h(b)| <= ||h||_X, to r_R <= 1/(16A). (3) imposes that. Wording only; not a defect.
- L99-105: order of choices agrees with DR L95 and PW §9 (L1053-1084). Nothing chosen before kappa depends on M, kappa-bar or b_0.

## §2 (L107-251): complex rows, with absolute derivatives

- L109-116, (4): this is PW Lemma 3 (4.3), pw.md L272-277, proved there on a complex supremum ball m_c||a||_inf < r_0 at complex first-order references (pw.md L231-253). The citation is correct.
- L122-134: the density factor eta L^{-3j} = eta^4 m_c^{-3} comes from the column product. Checked against PW L278-279 and nl-r9 L111.
- L136-199, (5)-(7): I checked the one-step majorant (6). Its derivative gives (7): d/dz[LAz^2/(1-Az)] <= 2LAz/(1-Az)^2. The coefficient-extraction step is correct: if a nonnegative series has value <= V at s = rho_1, then its n-th coefficient is <= V rho_1^{-n}. With fine inputs t_0 s = L^{-j}s and one factor eta per leg, eta^n L^{jn} = m_c^n. This gives the m_c^{n+1} and eta^4 m_c^{n-3} powers in (5). The n = 1 column case agrees with SA PX152 (ym4.tex L11619-11622) and PW (4.1).
- **Finding 1 (L79-81 with L160-188; minor, repairable).** At step i, the relative error is A delta_i with delta_i <= A(eps_* + 4G r_R) t_i. The first-exit product therefore needs exp((A^2(eps_*+4G r_R) + C A s)/(L-1)) < 2. (3) states this with A, not A^2, and leaves no explicit room for the s-term. Repair: write (3)'s third condition with A^2 (or with one fixed A' >= A^2), and then choose rho_1 by strict inequality. eps_* and r_R are chosen after A, so the order of choices does not change.
- **Finding 2 (L155-199; not fatal; sketch).** For general n, (5) is a compressed majorant-composition sketch. The marked-leg (column) version is one sentence (L190-193). The argument is standard and I find no error in it. But (8) and (10) need only n <= 2. For those, frozen PW Lemma 3 already suffices: (4.3), (4.4), and the phase-alignment fact at pw.md L291-297, applied to the linear functional u -> (DK_a - DK_0)[u](c,b_0) for fixed (c,b_0), with Cauchy in a. General n is used only for the ABS majorants in §7. Repair, if wanted: write the marked-leg recursion with explicit majorant vectors level by level.
- L201-216, (8): I checked it. |K_h - K_0|(c,b_0) <= A_1 rho_1^{-1} eta^4 m_c^{-3} h_c^*, using (5) n = 1 along th with (th)_c^* <= G r_R. The transpose eta^{-4} cancels, and scale comparability (G^3) and multiplicity N finish the bound. h_c^* is the value part of hat-n_b, so the bound by C_R hat-n_b(h) holds. The second line is (5) n = 0. Correct.
- L218-226, (9): ||E_h - I|| <= e^{C eta|h|} - 1 <= e^{1/4} - 1 < 1/2 (for complex h, ||ad h|| <= 2|h| is absorbed in A). The Neumann series gives |R_h| <= 2 and |R_h - I| <= 2(e^{A eta|h|} - 1) <= C eta|h| <= C hat-n_b(h). Correct.
- L231-250, (10): I checked each line from (5) at centre 0 and centre a: the row sums for C and C', the transpose entries with the second line of (5) for the C'' lines, and the weight transfer e^{theta D_R} <= 2. All are correct. The n = 2 difference line uses (5) n = 2 (or the PW route of Finding 2).
- Verdict §2: (Rows) holds on the complex envelope, as DR L77-85 requires, with reads within D_R.

## §3 (L252-354): complex Wilson pairing

- L269-283, (12): the linear insertion sum is eta * (eta * first differences) = eta^2 d_U a, plus the prefix-curl term eta(1 - Ad P_U) times transported values. The higher terms are <= C eta^2 sup|a|^2 <= C eta^2 m^{-2} n(a)^2. The reference term is eps_* eta^2 m^{-2}. Correct. The curl term matches the gate's proved correction (a3-derivative-gate L52-59) and frozen PW L368-374.
- L287-305, (13): I checked it directly. (i) The mixed second generator X is traceless. Its trace at a cyclic rotation P' (conjugate to P_V) is Tr(X(P'-I)), which is <= C eta^2 |P_V - I||v||u|. (ii) For the sixteen ordered insertion terms, Tr(X~_i Y~_j P) for i < j and Tr(Y~_j X~_i P) for j < i reduce at P = I to Tr(X~ Y~), by cyclicity and by the symmetric same-link product. The difference at P != I is Tr(X~ Y~ (P - I)). Complex transports are bounded in the real class gauge. Correct.
- L310-322, (14): the bounds for differencing E_a (C eta|grad a||v| <= C r_R m^{-1}|v|), for the link change (C|a||v|), and for the curl correction (eta^{-1}|P_V - I||v| <= C m^{-1}|v|) are each correct.
- L327-333: inserting (12) and (14) into (13) gives eta^4 m^{-2}(|grad v| + m^{-1}|v|) n(u) + eta^4 m^{-3}|v| n(u), which is (11). The bare boundary case is correct: eta^4 eta^{-3}|v| eta|u| = eta^2|v||u|.
- **Finding 3 (L254-261, L327-333; minor, repairable).** (11) bounds the value term with n_{E_b}(u), the maximum over b's plaquette stencil. DR's (Pair) (dr.md L77, L87-89) uses hat-n_b(h), the maximum over the *row carriers* reading b. A bare row carrier need not contain the perpendicular bonds of b's plaquettes. So "stronger bilinear version" (L254) is not literally shown. This is harmless as used: DR's Theorem 4 (dr.md L201, L210) and rows (40) use (Pair) only through ||h||_{X,w}, which dominates both local maxima up to G and a weight factor 2. Repair: state (Pair) with n_{E_b}, or let hat-n_b include b's plaquette stencil (DR already allows reads of diameter <= D_R).
- L335-353: the absolute-majorant paragraph is a sketch. Formula (15) correctly removes the divided differences.
- Verdict §3: the full-gradient (Pair) holds on the complex envelope in the stencil form of Finding 3. That is the form DR consumes.

## §4 (L355-443): local nonlinear Wilson force

- L371-386, (17): I verified the identity. For traceless 2x2 matrices, {X_q, X_r} = Tr(X_q X_r) I, so Tr(X_p X_r X_q) = -Tr(X_p X_q X_r). Terms with a repeated index cancel by cyclicity. For each triple the right side gives (2T - 2T + 2T)/2 = T. Tr X^3 = Tr(X^2 Y) = 0 kills the other cubic words. Correct.
- L391-400, (18): I recomputed the six commutators of v, w + eta u, -v - eta t, -w. The sum is 2[v,w] + 2eta[v,u] + 2eta[t,w] - eta[v,t] + eta[w,u] - eta^2[u,t]. Matches.
- L402-412: summation by parts. The two plaquettes sharing b in one plane enter with opposite signs, so the force carries a difference of C_p across them. The leading term gives 2 eta grad[a_mu, a_nu], via the exact product rule. The eta-terms are bounded by (2/eta) * eta. Varying the other insertions gives C|a||grad a|. Correct; this is the same as nl-r9 (3.5)-(3.6).
- L414-431, (19): the P_U - I cubic terms, including Tr(X_i^2 X_j P_U) = (1/2)Tr(X_i^2)Tr(X_j(P_U - I)), give C eps_* eta m^{-2}|a|^2. Degree n >= 4 gives eta^{n-4}|a|^{n-1}. Each term is <= C r^2 m^{-3} on ||a||_X <= r, using eta <= m. The boundary bound C eta^{-1}|a|^2 with m = eta is also correct.
- L433-441: the derivative estimate in (16) follows term by term (|u||grad a| + |a||grad u|, etc.). Correct.
- Verdict §4: (16) holds on the complex envelope. It uses no difference of J.

## §5 (L445-583): counting multiplier and column bound

- L449-462, (20): from <QA, nu>_{m^4} = <KA, m^3 nu>, Q^{T,mu} = K^T m^3 and W_0 = m^{-1} Sigma_cnt^{-1} m^3, so Sigma = m^3 W_0^{-1} m^{-1}. This agrees with CP12 (2) (cp12.md L54-57) at mu = m^4, ell = m.
- L464-480, (21): PW (6.4) has the A-equation with -Q^T a Q A - Q^T nu and the constraint QA = f_nu. So nu = -W_0^{-1} f_nu, where W_0 is built from the Green operator *with* the row mass. By CP12 (1) (cp12.md L42-45), this system's multiplier block is Sigma, and the physical saddle block is Sigma - a_0. This matches DR's M_s = M^walk - a_0 I with M^walk = Sigma at s = 1 (dr.md L34, L41) and nl-r9 (4.1). The source norm is correct: PW (6.2) scales f_nu by m (pw.md L597-599), and PW L838-839 gives the same raw-row column statement. The output bound comes from PW (6.3): nu is in local maxima with scaling m^3 nu = zeta (pw.md L609-614). The ell^2 remark at L478 is unnecessary but harmless.
- L482-495, (22): this is PW (7.1) (pw.md L826-828), whose R-norm contains the nu-slot, applied per walk term at j = 0. A_E = C_L is independent of M_1 (PW L652-653, L1072-1073). Correct.
- L497-503, (23): this is PW (8.2), pw.md L994-997. It applies because DR's walk data (dr.md L25) tag each coefficient's full hull, M^walk included. Correct.
- L505-521, (24): with 128 kappa-bar/ell_P <= tau/16 and weight rate <= tau/16, rate 3 tau/8 remains. The endpoint sum uses t_omega >= d(c',c) and P82 I4. The walk count is C_1^n against (A_E/M_1)^n <= 2^{-n}. The row-sum form sup_{c'} sum_c is exactly the Y_w -> Y_w norm. Correct.
- **Finding 4 (L509-511; not a defect).** The text "pays the backward intermediate-pillar sums used in PW (7.1)" with the remaining rate. Those sums were already paid inside PW (7.1) (pw.md L830-834). The allocation is redundant and leaves unused rate. Nothing fails.
- L525-532, (25): the diagonal -a_0 I adds a_0 <= a_0 e^{16 kappa-bar}. Correct.
- L537-568, (26)-(27): the Cauchy-Schwarz constant (eta^4 sum_{b in y} m_b^{-4})^{1/2} is bounded by the pillar volume. (Directly, the R-norm's supremum control of mA and m^2 grad A, from PW (6.3) and (6.9), gives the same.) Summing as in (24) gives (27), hence ||H^T||_{F_w -> Y_w} <= C_H e^{16 kappa-bar}. I checked the transpose computation. This supplies DR's full-gradient column bound directly from frozen PW, as an alternative to O1D Theorem B(c).
- L570-577, (28), possible cycle: C_Sigma and C_H depend on A_E, tau, the M_1 floor, P82 I4 pillar sums, endpoint and colour counts, and a_0. None depends on b_0. Everything chosen after b_0 uses b_0 only as an input: ell_P, and DR's eps_D, c_*, C_D (dr.md L175-185). The NL constants r_0 (29) and C_W (L703) do not involve b_0. **No cycle.** theta_* <= theta_PW <= tau/16 (pw.md L1030), so DR's theta (dr.md L172) lies in range.
- Verdict §5: ||M_s||_{Y_w -> Y_w} <= B and ||H^T||_{F_w -> Y_w} <= B are proved from frozen PW, with absolute walk sums.

## §6 (L584-720): nl-r9 checked and applied

- L590-609, (29)-(30): ball preservation holds: R + 4C_* B R^2 <= 2R iff 16 C_* r_0 <= 1. The Lipschitz constant is 2C_* B R = 8 C_* r_0 <= 1/4. Also 2R <= r_R/8, so (10) applies. Correct.
- L611-629, (31)-(32): d' = NA, Z = h', d'' = N C''(h)[Zu, Zv], and the transpose order Z^T (C''[Zu,.])^T N^T p. I re-derived all of these by implicit differentiation. N^T uses H^T A^T on Y_w, bounded by (10) and (27). Correct.
- L634-655, (33)-(34): each bound follows from (10), (PW), (25), (27) and the Neumann series. The telescoping differences are CBr, CBr, Cr, CBr. Correct.
- L664-672, (35): identical to DR (4) (dr.md L39-46) and nl-r9 (4.4).
- L674-701, (36)-(37): I re-derived the eight derivative terms and checked each bound. The first uses |p_s|_Y <= B gamma_* (from (27) and ||J||_{F,1} <= gamma_*). The seventh uses (16) at radius 2r. Correct.
- L703-719, (38): integration along the segment and DW_s(0) = 0 are correct. C_W is early and independent of b_0.
- Premises of nl-r9 Theorem 6 (nl-r9 L332): [Rows] geometry (§1's G, N, D_0 from P82 I5), the local calculus (10) and (16) (= nl-r9 (3.3), (3.7)), (4.2) (= (PW) + (25) + (27)), and [RED] (fixed by DR (4)). All are supplied. §6 re-derives nl-r9 §§5-6 instead of citing them. So NL does not rest on the unfrozen nl-r9's correctness. It uses only nl-r9 §4's *specification* of M_s, which agrees with dr.md L73 and ONE.
- Verdict §6: NL for exactly DR (4) is proved, on unweighted balls r <= r_0/B, with C_W B^2 r and C_C r.

## §7 (L721-793): absolute majorants and ABS

- L723-750: the majorant notion is a sum of norms of individual walk terms, plus absolute local Taylor coefficients. This is the notion that drlocp UNQ (drlocp.md L56) and D3L §3 (d3-local.md L81-86) ask for. (39) dominates the inverse series in (31) and DR (5).
- L752-768, (40): pairing each column with (11) and using both sums of (27) gives C B ||h||_{X,w}. Correct, given Finding 3's stencil reading.
- L770-790, (41): checked: 4B^2 b_* <= 4 b_0^2 eps_D <= r_0, 4C_* B^2 b_* <= 4C_* b_0^2 eps_D <= 1/4, and 2C_W B^4 b_* = 2C_W b_0^4 eps_D <= 1/8. DR (9) already gives the first and third. The C_* condition is an extra early shrink of eps_D, which DR L187 permits. The second condition is drlocp's B C_der (2R_*) <= 1/2.
- Verdict §7: ABS is supplied on the common balls. The general-n majorant input is the sketch of Finding 2. LIFT and admission are not supplied, and the text says so (L791-792, L827).

## SA quotations

- "From then on only bounds are used" (rows L31): ym4.tex L10562, inside the cited 10562-10578. Verified.
- "Using two row sums would lose the fine density" (rows L33): ym4.tex L11623, inside the cited 11508-11639, at PX152. Verified. The context (a column sum on the fixed leg) matches the use in §2.

## Dependence on unchecked (unfrozen) notes

- o1-decoupled Definition D: used only as the walk and hull *specification*, which frozen DR and PW also import.
- nl-r9: §4's specification of M_s only. Its §§3, 5 and 6 estimates are re-derived in rows §§2, 4 and 6.
- a3-derivative and its gate: only the curl-correction identity, which frozen PW §4.2 (L368-374) also derives.
- No estimate in the result rests on an unchecked note's proof. Through PW the result rests on frozen P82 I1, I2, I4 and I5, and on the h-walk and h-walk-gate repairs that PW imports.

## Findings summary

1. L79-81 / L160-188: A versus A^2 in the first-exit condition (3). Minor; repair stated.
2. L155-199: (5) for general n is a sketch. Not fatal: n <= 2, all that (8) and (10) need, follows from frozen PW Lemma 3. General n is used only for ABS.
3. L254-261 / L327-333: (11) gives (Pair) with plaquette-stencil maxima, not DR's row-carrier hat-n_b. Harmless for DR's use; repair stated.
4. L509-511: redundant rate allocation for intermediate sums. No defect.

## Verdict

These are proved as claimed, conditional on frozen PW, P82, DR, CP12 and IN1, the declared regular-pair envelope, the walk specification, and (P):
- (Rows) on the complex envelope;
- the full-gradient (Pair), in the plaquette-stencil form (Finding 3), which is the form DR's Theorem 4 consumes;
- ||M_s||_{Y_w -> Y_w} <= B, after the early enlargement of b_0, with no cycle in the constants;
- the column bound ||H^T|| <= B;
- nl-r9 (4.2);
- NL for exactly dr.md (4).

ABS on the common balls is supplied at sketch level for the general-n absolute Taylor majorants (Finding 2). All constants come before kappa. They are independent of M, mesh, depth and volume. kappa-bar enters only through B, ell_P and the later radii. Not supplied, as stated in the text: DR admission, LIFT, S-loc.

Checked line by line by Claude (fresh session).
