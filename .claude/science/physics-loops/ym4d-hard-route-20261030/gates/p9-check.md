lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T16:30Z

# P9 witness ports: one line-by-line check (row 341)

Started 2026-11-06T04:30Z. Pinned at commit 50b8bafeb. Work in progress: sections are added as the check runs.

Scope: `library/port/p9-witness.md` (C9 8.18:thm-torus-witness, C10 8.22:thm-volume-transfer, C11 8.1:thm-two-point-witness, with 8.22:cor-transfer-depth-floor and cor-reference-torus-kernel) and `library/port/p9b-extraction.md` (C5 8.2:prop-gaussian-extraction). Both ports were written by Codex. Sources: the Sussman-Alpoge complete account at 31a47c543775 (CA-III), fetched by URL into a scratch folder.

## 0. Sources and statement blocks

- CA-I, CA-II, CA-III and the outline were fetched at 31a47c543775 into a scratch folder. Their SHA-256 values equal the table at p9-witness.md lines 13-18.
- The anchors hold: 8.1:thm-two-point-witness at II:71279, 8.2:prop-gaussian-extraction at II:77279, 8.22:thm-volume-transfer at II:141540, 8.22:cor-transfer-depth-floor at II:142317, 8.22:cor-reference-torus-kernel at II:142607, 8.18:thm-torus-witness at II:144922.
- Each of the nine `latex` blocks in p9-witness.md was compared with CA-II, character for character. All nine are verbatim: C9 = II:144922-145029, C10 = II:141540-141583, C11 = II:71279-71367, the four excerpts at II:73250-73333, cor-transfer-depth-floor = II:142316-142371, cor-reference-torus-kernel = II:142607-142632.

## 1. C10 (8.22:thm-volume-transfer), p9-witness.md lines 359-443

Source proof: II:141585-141852, read in full.

Result: **first failing step none.** The port follows the source step for step: placement, the reflected source W_z and its two mirror conditions, the chessboard bound (VT1), four applications of the trace lemma with k = L^(m-m') odd, the stability and zero-source bounds (VT2), the one counterterm E'' formed on T_m', the bounds |h_m|, |h_m'| <= Q_star, and the Schwarz-Cauchy step.

Filled steps, each redone by hand:

- F10.1 (line 420). For finite K the lattice is finite and O(w_z) = z_1 O(F_1) + z_2 O(F_2) is bounded in U on compact z-sets. So Z_v(w_z) is entire, and h_v is holomorphic on D because E'' is (per-ball bound, part (i), inside H-VT(c)). Correct.
- F10.2 (lines 422-433). Fix z in D with N(z) = |z_1|a_1 + |z_2|a_2 > 0 and put phi(t) = (h_v(tAz/N(z)) - 1)/(Q+1) on |t| < 1. Then |phi| <= 1 and phi(0) = 0, so Schwarz gives |h_v(z) - 1| <= (Q+1)N(z)/A. On the closed polydisc |z_i| <= b_i = A/[2a_i(2Q+2)] we get N(z) <= A/(2Q+2) < A, so |h_v - 1| <= 1/2 and |Log h_v| <= sum 2^-n/n = log 2. Cauchy: |d1 d2 Log h_v(0)| <= log 2/(b_1 b_2) = log 2 (2Q+2)^2 (2r/rho)^2 a_1 a_2. Two volumes give the factor 2 log 2 of C_VT. Correct. The case a_i = 0 is also correct: then F_i = 0, and neither w_z nor E'' depends on z_i.
- F10.3 (line 441). d1 d2 log Z = Z_12/Z - Z_1 Z_2/Z^2 at z = 0 is the connected two-point function. Correct.

Minor wording, not failures:

- Line 363: "the least power of L above 16(R+1)". The source (II:141587) has ">=". Nothing depends on this.
- Line 363: the port credits the invariance of the sharp norms to `1.1:lem-invariance`. The source (II:141598-141600) uses the translation invariance of the sup norm and the Lipschitz constant. The fact is true either way.
- Lines 387-391: the port does not repeat that, for r = 2, the upper stability bound is applied to the real system of four functions at (z, conj z) on the polydisc of radius rho/2 (II:141700-141702). Line 371 records it. Nothing is lost.

Standing: C10 is a proved implication from H-VT (a)-(f), as the account states. The port adds no unproved step.

## 2. C9 (8.18:thm-torus-witness), p9-witness.md lines 445-513

Sources read: the proof II:145030-145114; 8.21:cor-consequences-torus and its proof II:145314-145518; the test class and depth II:68377-68452 (8.1:not-test-pairs-kernel); the witness class II:68722-68796; the two case propositions II:144388-144430 and II:144797-144840.

Result: **first failing step: line 483** (existence of the reflected pair). It is repairable, and it is inherited from the source. Every other step stands.

Step by step:

- **C9.1, lines 449-456: correct.** The account defines s(d) = min{s >= 0 : C_W(s) L^-s <= d} (II:68430). So s(d) >= n holds if and only if d < min_{j<n} C_W(j) L^-j, for an integer n >= 1. At d equal to that minimum, s(d) < n. So the supremum in C9 is not attained, and "d <= d_W^T" must read "d < d_W^T". "The largest d" at II:144832-144836 has the same defect. For a non-integer n, use ceil(n). Nothing downstream depends on the endpoint.
- **Part (a), line 458: correct.** It is the source's case split. The below-horizon proposition sets gamma_W^T = min{gamma_W, gamma_*^dagger} (II:144413). It gives |R_K| <= 1/4 on Case V. The beyond-horizon proposition (II:144797) gives the same display under (8.18:eq-torus-witness-a).
- **Part (b), lines 460-467: correct.** (4/9)(1/2) = 2/9 and (16/9)(3/2) = 8/3. The envelope 0 < g^-2 + lambda s - c_5 <= g_{K-s}^-2 <= g^-2 + B(s+1) is (A2) of the corollary, with its positive left end. Then t -> t^-2 reverses the order.
- **Part (c), line 469: correct.**
- **F9.1 and F9.2, lines 471-473: correct.** A limit of reals in a fixed closed interval stays in it. The subsequence step is sound.
- **Remark (simplification), lines 473-481.** The limit step of C9(d) needs no separate continuum-kernel input. By (A1) of the corollary, the finite-K kernel bounds c_K||f1|| ||f2|| <= K_{K,s}(f1,f2) <= C_K||f1|| ||f2|| hold with K-free constants. So every limit point of the kernel factors lies in [c_K, C_K]||f1|| ||f2||. That interval is inside the one that (A5) asks of the unwritten 8.21:lem-continuum-kernel (II:145220, "not written out here"). The port says this at line 481. Its caveat "whenever the limit convention tests exactly the same pair" is met: (A3) takes the limits at fixed g, m, d and the same pair. So (A5) can be dropped from 8.21:cor-consequences-torus and from C9. Its parts (b) and (c) then hold with the stronger constants 2/9 and 8/3 (no theta^2, no factor 100). *What this does not remove:* the lower kernel bound inside (A1) rests on (h3) of 8.1:lem-kernel-bounds (II:69939-69955). That is a continuum-kernel statement too, carried as H3-CONT in `library/port/p3-free.md`. So the continuum kernel stays on the chain through (h3), and the port's H-CK hypothesis drops out of C9's limit step only.
- **Line 483: FAILS as written (repairable).** The step needs a reflected pair (f, iota f) in T(d; theta) for the theorem's own theta. The port writes "Such bumps exist with some fixed positive shape parameter; choose the coupling/depth thresholds for that parameter". That silently changes the threshold gamma_W^T of the statement. The source has the opposite gap: it asserts "such pairs exist" (II:145463) for every theta in (0,1]. That assertion is false at theta = 1. Proof: supp f in B(x,d) and Lip f <= ||f||/d give f(y) <= ||f|| (1 - |y-x|/d)_+, so the integral of f is at most ||f|| 2 pi^2 d^4 (1/4 - 1/5) = (pi^2/10) ||f|| d^4 < ||f|| d^4. So T(d;1) is empty. For theta at or near 1 the theorem is vacuous, and none of the four consequences in (d) is derived. The same holds for CA-I 2361-2364, which says every later letter of clause (iv) has a non-empty admissible set "for every theta in (0,1]".
  - *Repair.* State (d) for theta <= 1/2 (any theta < pi^2/10 works). For theta <= 1/2, take f = (1 - |y-x|/r)_+ with r = 9d/10, centred at distance 19d/10 from a lattice mirror. Then the integral of f is pi^2 (0.9)^4 d^4/10 > 0.64 d^4 >= theta d^4, Lip f = 10/(9d) <= 1/(theta d), supp f is inside B(x,d), and dist(supp f, supp iota f) = 2d lies in [d, 6d]. So (f, iota f) lies in T(d; theta) and no threshold changes. Its dilates lie in T(sigma d; theta). So the same pair serves the other three consequences.
- **Positive variance, lines 483-491, given the pair: correct.** With A = O(f) - E O(f) and Omega = 1, reflection invariance gives <A,A> = E[O(iota f)O(f)] - E O(iota f) E O(f) = S^T(iota f, f). The three entries converge by (A3).
- **F9.3, lines 493-499: correct.** C_W(s) = C_W0 A_0^2 (log xbar_s)^{2 p_0} >= 1 (II:68418-68422). So t <= s(d) < 1 + t + log_L C_W(s-1), and the last term is O(log log s) at fixed g. Hence s/t -> 1, c/log(1/d)^2 <= Q(d) <= C/log(1/d)^2, and d^-eps Q(d) >= c eps^3 log(1/d)/6 -> infinity. The class conditions are dilation covariant.
- **Scale invariance, line 501: correct.** The three cases a > 0, a = 0, a < 0 contradict the lower bound, Q -> 0, and the upper bound.
- **C9.2 and F9.4, line 503: correct.** At zero charge the Maxwell quotient is identically 0, so "tends to a strictly positive constant at any charge" (II:145496) is false there. The conclusion (c3) still holds there, because Q > 0. At a non-zero charge the scaling count is right: d^-8 against d^8, a cross term O(d^4), a square O(d^8). The step rests on H-free-torus, which the port keeps as a named input.
- **g_eff, lines 505-511: correct.** g_eff^-4 = b_0/Q, and the square roots give the two constants (3/(800 C_K))^(1/2) and (9/(2 c_K theta^2))^(1/2).

Standing: with the repair above, C9 is a proved implication from H-age, H-flow, H-positive, H-limit and H-free-torus, with the continuum kernel entering only through (h3) inside H-kernel.

## 3. C11 (8.1:thm-two-point-witness), p9-witness.md lines 515-915

Sources read: the main term II:71970-72181; the profile remainder II:72182-72287; the large-field remainders II:72288-72641; the spanning local remainder II:72642-72820; the extraction remainder II:72821-73003; the irrelevant remainder II:73004-73054; the constants and ceiling II:73214-73440; the envelope, room, depth and floor definitions and proofs II:68920-69075; the kernel-bounds hypotheses II:69925-69975; the sharp norm II:100478.

Result: **first failing step none.** The port is a complete deduction from its named use-site hypotheses (H-source-use, H-GXa, H-GXb, H-depth, H-add and the ledger). Every correction it makes is correct, and every filled step checks.

- **Main term, (W1)-(W3), F11.1, lines 540-585: correct.** With tau_h > 0, d_i tau = tau Phi_i and d_1 d_2 tau = tau(Psi + Phi_1 Phi_2) give S^T = E Psi + Cov(Phi_1, Phi_2). In the summed index, m_i = c_i^0 and the deep pieces vanish (II:72126-72141), so (sh)' = R^mL = 0 and (W3) is (8.1:eq-main-term-6).
- **C11.1, line 587: correct, notational only.** R^{Psi,live} is the signed E Cov_{E_h} at II:72124, and a majorant at II:72563. R^loc is E Psi^span at II:72124, and is set equal to the majorant r^loc at II:72684. All source bounds are built from sup and E|.| bounds; for example (8.1:eq-local-remainder-1) is |Psi^span| <= r^loc. So |R| <= B_R holds with the same constants. The live pairings sit in R^L and in R^{Psi,live}, by (8.1:eq-main-term-5) and (8.1:eq-main-term-4). The sentence at II:73229 ("contained in R^{Psi,live}") is too narrow, as the port says.
- **Profile remainder, lines 589-620: correct.** xi_i <= 160 d_W C_h M/(theta^2 rho), and xi <= 1/3 by d_W <= 1/3 (gamma-7) and rho >= 160 C_h M/theta^2. Then 2 xi + xi^2 <= 3 xi, C_prof >= 3 2^8 160, and the floor (32/3) C_prof (C_K/c_K) C_h M/theta^2 gives r^prof <= 1/32.
- **Large-field remainder, (W4)-(W8), lines 622-707: correct.** (W5) and (W6) are the source's displays in the summed bookkeeping (II:72470-72475, and (8.1:eq-large-field-remainders-7) with S^h = 0). The live weight enters linearly: P(B_1 and B_2) <= min P(B_i) <= min{n_1, n_2} q^lv.
  - *F11.2 is a needed repair.* The source replaces indexed letters by their maxima (II:72474-72476) and then divides by ||f_1|| ||f_2|| (II:72573-72575). A bound in max(||f_1||, ||f_2||)^2 over ||f_1|| ||f_2|| is not uniform in the ratio of the two norms. S^T, M and the classes F^+, T are invariant under f_i -> c_i f_i with c_i > 0, and S^T and M are bilinear. So normalising ||f_1|| = ||f_2|| = 1 first, or keeping the indices, restores the bound with the printed constants.
  - *Source slip, harmless:* the relative size of n eps^2 s^sharp q_W carries theta^-3 (theta^-1 from s^sharp, theta^-2 from c_M theta^2), not theta^-1 as printed at II:72596-72597. It is still dominated by the theta^-4 of (8.1:eq-large-field-remainders-9). The port's "its fixed theta-factor" (line 697) is consistent with this.
  - *F11.3 is correct and needed.* (gamma-src) reads sup F_src <= theta^4 c_M/(64 C_tot) (II:73293). With the relative coefficient C-hat of (W7), it gives the relative bound C-hat c_M/(64 C_tot). That is <= 1/64 only if C_tot >= c_M C-hat. The port's choice C_tot >= max{C-hat, c_M C-hat} closes this for any c_M. The same holds for (C_0-src) and (W8).
- **Local remainder, (W9)-(W11), lines 709-750: correct.** The five term kinds give [4(E_0+B_0+C_e+1)+1] e^{-kappa'' d} (II:72734-72740). The anchor count and the nu = 0 estimates are those of II:72742-72765.
  - *F11.4:* y^4 e^{-a y/2} decreases for y >= 16/a, so the nu-th ratio is <= C_a e^{-a 3^nu/2} <= C_a e^{-a nu/2}, and the series converges.
  - *F11.5 is a needed repair.* The source divides by c_M theta^2 g^4 ||f_1||_sharp ||f_2||_sharp (II:72786-72788), but (8.1:eq-main-term-a) has sup norms. With ||f||_sharp = max{||f||_inf, 40M Lip_{k0} f} (II:100478) and Lip_{k0} f <= ||f||_inf/(theta rho), we get ||f||_sharp = ||f||_inf once rho >= 40M/theta. That floor is a member of (8.1:eq-constants-ceiling-c). It uses rho >= C_0, which is the source's own standing condition (II:72190).
  - *(W11) persistence:* the map rho -> kappa'' rho/(32M) - 4 log(rho/M) increases for rho >= 128M/kappa''.
- **Extraction remainder, (W12) and F11.6, lines 752-799: correct.** r - r_1 >= ceil((p_0/2+1) log_L log xbar_s) + r_0 - 1, because ceil(log_L(20 L rho)) <= ceil(log_L(20 L C_W(s))) + 1 when rho < L C_W(s), that is when s >= 1. Then T_6 <= A_0^4 L^{8-8 r_0}, T_5 <= L^{4-4 r_0} and T_4 <= A_0^4/C_D. The first entry of D_square is <= 1 + c_a^-1 (20 p_0 log xbar_s + 8 log(L C_0 A_0^2) + log C_D). All these match II:72905-72952.
- **Irrelevant remainder and F11.7, lines 801-817: correct.** rho^-2 p_0(g_{k0})^4 <= C_0^-2, because p_0 increases in g^-2 and x <= xbar_s. Then 7 C_b/C_0^2 <= 1/64 when C_0^2 >= 448 C_b. Making the E_a allocation explicit (M/(6 64) per term) is a valid reading of "under the same order of constants" (II:73045-73046).
- **F11.8 and C11.2, lines 882-906: correct.** Each majorant has log <= A(1 + t^{r_R}) + B t + D log t - c A_0 t^{p_0}, with p_0 >= 5 r_R and p_0 > 1. Also (eps_j/eps_k0)^2 <= 2 (2^{1/p_0})^{2 p_0} = 8. And sup Rcheck^4/p_0^2 is bounded since 4 r_R <= 2 p_0. The source's claim that F_src "is decreasing for y >= y_0" (II:73393-73394) is not proved; the radius function may jump. Only the tail supremum is needed, and it is non-increasing in X by inclusion. "gamma_W is defined as the largest g" (II:73273) assumes that a largest admissible g exists; any positive admissible ceiling suffices.
- **H-depth, line 536: the gap is real, and the repair is right.** s_W(g) is the least s meeting three conditions (8.1:eq-coupling-envelope-d). The proof (II:69049-69069) shows only that the set contains all large integers. But the theorem assumes s(d) >= s_W(g) and uses the conditions at s(d). r(s) is a sum of two ceilings of slowly increasing arguments, so r(s+1) - r(s) can be 2, and then s - r(s) drops by 1. Likewise 2B(r(s)+1) <= xunder_s can fail just after a jump of r, since 2B >= 2 lambda > lambda. So upward closure is not shown. The port's repair (least tail floor; it exists by the proof just cited) is correct. It only raises the floor.
- **Final count, lines 908-915: correct.** |S^T - M| <= 6M/32 < M/4. N_{K-s} lies in [1 - d_W, 1 + d_W], inside [2/3, 4/3], by (gamma-7).

Standing: C11 is a proved implication from the port's named hypotheses, with the tail-floor repair of s_W. The port's statement-to-supplier qualifications (H-source-use, H-GXa, H-GXb) are accurate descriptions of what the account leaves open (II:71368-71370 "proof is incomplete at the step marked (*)"; 8.21:lem-source outstanding).
