# Check of library/tpi.md (TPI-FREE, tasks 13.1-13.2)

Checked line by line by Claude (Opus 5.5), 2026-11-08. One check, one reading.
Not an audit. No status granted.

**Verdict: PASS.** The join (8)-(16) is correct as written. Every inequality,
constant and index shift holds, for all 0 <= j <= K, uniformly in K, j, m
and position. All ported rows match their sources, with the same block map,
norms and law. No domain mismatch. Four wording fixes are listed; none is a gap.

Abbreviations: N = YM4_1400.tex; SA = YM4_sketch_500.tex; CA-II as in the note.

## A. The new argument (3)-(16)

1. CONFIRMED. tpi:171-176, (3). N_j = l/a_j = 2L^(m+K-j) >= 2, also at j = K
   (N_K = 2L^m). N:41668-41670 and N:25814-25816 admit depth k >= 0 and any
   integer side M >= 2. So every level, j = 0 and j = K included, is in the
   source domain.
2. CONFIRMED. tpi:183-192, (4). N:41699-41701 gives Q v = h^5 sum_{x in B(y)} sum_t v.
   With w = h v this is n^(-4) sum sum w = S_n w, the same straight row as
   SA:8521-8527 (CF8) and the A_j of N:4329-4332. dw = h^2 d_h v and
   sum|dw|^2 = h^4 sum|d_h v|^2 are correct. Blocked law and inverse use the same map.
3. CONFIRMED. tpi:194-249, (5). Matches N:41886-42038. Zero force gives
   H_h = K_0^(-1) Q^# S^(-1), as N:42030 and N:100999-101002. The bound
   ||A||_{X_alpha} <= C(||b||_inf) contains ||D A||_inf; the curl is two first
   differences, so C_H = 2C_alpha. Constants are uniform in depth, volume and
   holonomy (N:42004-42006). Trivial holonomy is included.
4. CONFIRMED, wording fix W1. tpi:251-263. R_g D^# H_h B = 0 follows as stated.
   ran R_g = L(ker q) is elementary both ways (q G_s L lambda = q lambda).
   The step "minimizes curl energy" needs one more sentence: with the penalty
   zero, the saddle equation is the Euler equation of the convex curl energy on
   Q v = B, hence a minimizer. This is N:101010-101013.
5. CONFIRMED. tpi:265-283, (6). Matches N:101013-101019. S_n(const c) = n c;
   S_n d lambda = d_c q lambda; q is onto; closed coarse 1-forms on the torus are
   gradients plus constants. The two fibres agree, so (6) is the least-norm
   exact curvature with datum d_c B, as in N:4339 and SA:7649.
6. CONFIRMED. tpi:285-291, (7). The l^inf -> l^inf norm of a real matrix is its
   largest row l^1 sum. Sign data have sup norm 1.
7. CONFIRMED. tpi:298-319, (8). Row sums n^2 and column sums n^(-2) match
   SA:8531-8542 / N:5579-5590 (CF8-CF9). So ||A_j|| <= 1, with periodic
   multiplicity. V_j = P_c V_j P_c and <u,V_j u> = ||P A_j^* P_c u||^2 <= <u,P_c u>.
   The actual blocked law is used, not a fresh Maxwell law.
8. CONFIRMED. tpi:321-347, (9)-(10). T_c is defined on E_c, C_j lies in E_c,
   congruence keeps order, and T_c T_c^* = (d_c^* d_c|X_c)^(-1).
9. CONFIRMED. tpi:349-374, (11). CA-II:69557-69560 proves Delta_1 = -Delta
   componentwise; it relabels to the coarse torus. X_c is orthogonal to constants
   and Delta_c-invariant. Character normalization N^(-2) and eigenvalue
   4 sum sin^2(pi k/N) are correct.
10. CONFIRMED. tpi:376-391, (12). sin t >= 2t/pi on [0, pi/2] needs |k_mu| <= N/2;
    true. Denominator >= 16|k|^2/N^2. Shell count 64r^3 + 16r <= 80r^3.
    1/|k|^2 <= 1/r^2. Sum gives 5q(q+1)/(2N^2) <= 5/8 + 5/(4N) <= 5/4 for N >= 2.
11. CONFIRMED. tpi:394-401, (13). Diagonal bound plus P3:464-470 (F11).
12. CONFIRMED. tpi:405-419, (14). Y_j = P_{W_j}F is the least-norm element of
    E with A_j f = C_j (N:4333-4334). d_c B_j = C_j, so Y_j = h^2 T_h B_j pathwise,
    and R_j = h^4 T_h S_j T_h^T in plain coordinates. A field identity, not
    an equality of minima.
13. CONFIRMED. tpi:421-443, (15)-(16). R_j(p,p) <= (5/4) C_H^2 h^4, h^4 = L^(-4j) =
    (a/a_j)^4. j = 0: A_0 = identity, R_0 = P. j = K: bound C_R a^4, R_K kept.
    The max{1, .} in C_R is harmless (W4).

## B. Ported rows of the final table

14. CONFIRMED. Row 1 (tpi:513). SA:7634-7641 = N:4329-4332 define A^(j) with the
    stated formula. Contraction: SA:8521-8554 = N:5568-5605. Wording fix W3: the
    row cites N:4324; the body cites N:4329. Use 4329.
15. CONFIRMED. Row 2 (tpi:514). SA:7641-7649, N:4333-4340: nesting, conditional
    expectation P_{W_k}F, F = P_{W_K}F + sum C_(j)F. SA:26028-26036 = N:100448-100456:
    C_(j) = C^bg_{K,K-j+1} - C^bg_{K,K-j} and C^bg_{K,K} = C^free, hence
    R_j = C^bg_{K,K-j} = P_{W_j}. (17) is telescoping.
16. CONFIRMED. Row 3 (tpi:515). N:101043-101077 treats closed forms, constants,
    gradients and normalized gauge integration for the full flat laws; 101075 says
    the same bare slice arises in either gauge. SA:26143-26148 only asserts it.
    This row is not used in (8)-(16).
17. CONFIRMED. Row 4 (tpi:516). N:41659-42061 and N:100989-101029, at trivial
    flat reference, straight row, centered blocks: same law and map as A_j.
    Premises: row seeds include h = 1 (N:41764). Landau gap
    N:25865-26019 holds for every k >= 0, M >= 2, and any real colour.
    The deeper scalar premises (N:123124-123433, 24496-24593, 25131-25169)
    were checked for location and statement only, not re-proved here.
    Wording fix W2: tpi:145-150 paraphrases the compactness step;
    N:25941-25950 uses trigonometric interpolation and Rellich. The content is equivalent.
18. CONFIRMED. tpi:89-126. CA-II:69958-69965 states (2) under (h1)
    (69927-69929), cited to Balaban. The note does not use (2). N:102280 has no
    antecedent; "coarse covariance" occurs only at N:6223, 102280, 106650.
19. CONFIRMED. SA:32521-32524: a_s = L^(-s), s = K-j, eta_j = L^(-j). So
    a^SA_{K-j} = a_j and eta_j = a/a_j (tpi:465-466).

## C. The stipulated input

20. CONFIRMED. tpi:469-474, 521. The slice estimate (SA:7646, 26138;
    N:4337, 100994) is |C_(j)| <= C eta_{j-1}^4 exp(-delta d/a_{j-1}). In TP1
    units: (a/a_{j-1})^4 = L^4 (a/a_j)^4, and exp(-delta d/a_{j-1}) <=
    exp(-delta d/a_j). So only C changes. Barycentre shift <= sqrt(2) a <= sqrt(2) a_j
    costs a fixed factor. It is used exactly as stated. It is not used in (8)-(16).
    items/tpi.txt:3 allows it as stated work.
21. CONFIRMED. Apart from that estimate, every input to (16)-(17) is a written
    proof in N, SA or CA-II, or is proved in the note. The full-P comparison (2.4)
    is outside the FREE target (prior/tpi.md:41-47).

## D. "No new supplier lemma remains" (tpi:500)

22. CONFIRMED. This is right as scoped: the residual bound needs neither (2),
    H1-MIN nor any Balaban paper. It still rests on the stipulated slice estimate
    and on N's written strong-inverse chain (finding 17).

## Wording fixes (none is a gap)

- W1: tpi:262. Add the Euler-equation and convexity sentence (finding 4).
- W2: tpi:145-150. Say this paraphrases the source's Rellich argument.
- W3: tpi:513. N:4324 -> N:4329.
- W4: notation. S (Schur, tpi:229) vs S_j (tpi:339); P vs P_s; C_j vs constants C.
  Rename S to S_Q, for example. C_R = max{1, .} can be 5C_H^2/4 since (15) covers j = 0.
