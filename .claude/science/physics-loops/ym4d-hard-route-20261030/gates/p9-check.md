lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T16:30Z

# P9 witness ports: one line-by-line check (row 341)

First failing step: `library/port/p9-witness.md` line 483 (C9(d), existence of a reflected test pair). It is repairable, and it is inherited from the account (II:145463). In `library/port/p9b-extraction.md`: none.

Pinned at commit 50b8bafeb; check run 2026-11-06 from 04:30Z. Scope: `library/port/p9-witness.md` (C9 = 8.18:thm-torus-witness, C10 = 8.22:thm-volume-transfer, C11 = 8.1:thm-two-point-witness, and the assembly 8.22:cor-transfer-depth-floor and 8.22:cor-reference-torus-kernel) and `library/port/p9b-extraction.md` (C5 = 8.2:prop-gaussian-extraction). Codex wrote both ports. Source: the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) at 31a47c543775, CA-I, CA-II and CA-III, fetched by URL into a scratch folder. Balaban is credited where the ports cite him. Kind of result: a check of a port of their proofs. In places it is also a correction of their text (finding 1, and the endpoint, notation and tail points the ports already flag). No numerics were used. Memory was 64% free; no job was needed.

## Findings

| # | Where | Step | What is wrong | Kind | Repair |
|---|---|---|---|---|---|
| 1 | p9-witness.md 483 and 1105; source II:145463, II:142705-142720, CA-I 2361-2364 | C9(d) and the R^4 positivity: "such pairs exist" | T(d;1) is empty. supp f in B(x,d) and Lip f <= ||f||/d force f(y) <= ||f||(1-|y-x|/d)_+, whose integral is (pi^2/10) d^4 ||f|| < d^4 ||f||. So for theta at or near 1, C9 and clause (iv) are vacuous, and the four consequences of C9(d) (and dim H^curv >= 2 on R^4) are not derived. The port instead changes the threshold without saying so ("choose the coupling/depth thresholds for that parameter"). | repairable, not fatal | State (d) for theta <= 1/2. Then f = (1-|y-x|/r)_+ (or the C^1 bump (1-|y-x|^2/r^2)_+^2) with r = 9d/10, centred 19d/10 from a lattice mirror, gives (f, iota f) in T(d; theta) with no threshold change (Section 2). |
| 2 | p9-witness.md 473-481, 1105 | Use of H-CK in C9(d) | Not wrong; it is a simplification. (A5) of 8.21:cor-consequences-torus follows from (A1), whose finite-K kernel bounds are K-free. So C9(d) needs no separate continuum-kernel input and keeps the constants 2/9 and 8/3. The continuum kernel still enters through (h3) of 8.1:lem-kernel-bounds (H3-CONT in p3-free.md). | none needed | Drop (A5) and H-CK from C9; keep (h3). |
| 3 | p9-witness.md 536; source II:68978-68982, II:69048-69069 | H-depth: s_W(g) is a first admissible integer, not a tail floor | Confirmed. r(s) can rise by 2 between consecutive s, so s - r(s) >= s_* and 2B(r(s)+1) <= xunder_s are not shown to be upward closed, but s(d) >= s_W(g) is how they are used. | repairable | The port's repair: define s_W(g) as the least tail floor. It exists by the printed proof and only raises the floor. |
| 4 | p9b-extraction.md 563; source II:77030-77032 vs (8.2:eq-gaussian-extraction-3) | Tail sum F12 | Confirmed. r(e^{-c_loc(D-l_r)} + ...) is not bounded by M^2 e^{-c_loc D} with the printed rate. | repairable | A smaller rate. C11's D_square floor, chosen through c_a, absorbs it. The port keeps it as H-tail-sum. |
| 5 | p9b-extraction.md 260; source II:77439-77443 | C1: support of G_1 G_2 | Confirmed. With B_l(p) a graph ball, the product lies in B_{3l+6C_W}(p_1), not in general in a ball of radius l+6C_W. | repairable | Use 3l+6C_W, or keep H-support. |
| 6 | p9-witness.md 668, 740, 697 | F11.2, F11.5, F11.3 | Confirmed gaps in the source, filled correctly by the port: compressed maxima divided by ||f_1|| ||f_2|| (II:72482-72484, 72573-72575); division by sharp norms where the lower bound has sup norms (II:72782-72784); and the factor c_M in the (gamma-src) ceiling (II:73293). | repairable, done in the port | As in the port. |
| 7 | p9-witness.md 456, 503, 587, 906, 1055; p9b 561 | C9.1, C9.2, C11.1, C11.2, C-V1, C2 | All six corrections are correct (Sections 2-5). | — | As in the port. |
| 8 | source II:72596-72597 | Relative size of n eps^2 s^sharp q_W | It carries theta^-3, not theta^-1; still dominated by theta^-4. | harmless slip | None needed. |

## Verdict

Both ports are faithful. Every statement block is verbatim (Section 0). The proofs follow the account's route, and no fabricated step or label was found. Every filled step (F9.1-F9.4, F10.1-F10.3, F11.1-F11.8, FV.1-FV.2, and F1-F17 of p9b) was redone by hand and holds.

- **C10:** a proved implication from H-VT (a)-(f). First failing step none.
- **C11:** a proved implication from the port's named use-site hypotheses (H-source-use, H-GXa, H-GXb, H-add, the ledger), with the tail-floor repair of s_W. First failing step none.
- **C5:** a proved implication from its named hypotheses, including H-jet, H-tail-sum and H-support. First failing step none. Its consumer mapping to H-GXa and H-GXb is correctly left open: printed clauses (a) and (b) do not contain the bounds the witness cites.
- **C9 and the assembly:** proved implications after the repair of finding 1 (theta <= 1/2), with C-V1. For C9(d), the continuum kernel is needed only through (h3).

This moves P9 (C5, C9, C10, C11 and the two 8.22 corollaries) to "checked line by line by the other model, with the repairs above". It closes none of their open inputs. Still open, as before: H-source-use (8.21:lem-source, outstanding), H-GXa and H-GXb (no printed supplier), H-C3/C4/C6/C7/C8, H-jet, H-tail-sum, (h3) of 8.1:lem-kernel-bounds, H-free-torus, and the B01-B24 Balaban inputs.

Finding 1 is a small correction to the account's text (II:145463 and CA-I 2361-2364). Its value to them is low, because restricting theta is trivial. Nothing is posted; rule 6 applies.

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
  - *F11.2 is a needed repair.* The source replaces indexed letters by their maxima (II:72482-72484) and then divides by ||f_1|| ||f_2|| (II:72573-72575). A bound in max(||f_1||, ||f_2||)^2 over ||f_1|| ||f_2|| is not uniform in the ratio of the two norms. S^T, M and the classes F^+, T are invariant under f_i -> c_i f_i with c_i > 0, and S^T and M are bilinear. So normalising ||f_1|| = ||f_2|| = 1 first, or keeping the indices, restores the bound with the printed constants.
  - *Source slip, harmless:* the relative size of n eps^2 s^sharp q_W carries theta^-3 (theta^-1 from s^sharp, theta^-2 from c_M theta^2), not theta^-1 as printed at II:72596-72597. It is still dominated by the theta^-4 of (8.1:eq-large-field-remainders-9). The port's "its fixed theta-factor" (line 697) is consistent with this.
  - *F11.3 is correct and needed.* (gamma-src) reads sup F_src <= theta^4 c_M/(64 C_tot) (II:73293). With the relative coefficient C-hat of (W7), it gives the relative bound C-hat c_M/(64 C_tot). That is <= 1/64 only if C_tot >= c_M C-hat. The port's choice C_tot >= max{C-hat, c_M C-hat} closes this for any c_M. The same holds for (C_0-src) and (W8).
- **Local remainder, (W9)-(W11), lines 709-750: correct.** The five term kinds give [4(E_0+B_0+C_e+1)+1] e^{-kappa'' d} (II:72734-72740). The anchor count and the nu = 0 estimates are those of II:72742-72765.
  - *F11.4:* y^4 e^{-a y/2} decreases for y >= 16/a, so the nu-th ratio is <= C_a e^{-a 3^nu/2} <= C_a e^{-a nu/2}, and the series converges.
  - *F11.5 is a needed repair.* The source divides by c_M theta^2 g^4 ||f_1||_sharp ||f_2||_sharp (II:72782-72784), but (8.1:eq-main-term-a) has sup norms. With ||f||_sharp = max{||f||_inf, 40M Lip_{k0} f} (II:100478) and Lip_{k0} f <= ||f||_inf/(theta rho), we get ||f||_sharp = ||f||_inf once rho >= 40M/theta. That floor is a member of (8.1:eq-constants-ceiling-c). It uses rho >= C_0, which is the source's own standing condition (II:72190).
  - *(W11) persistence:* the map rho -> kappa'' rho/(32M) - 4 log(rho/M) increases for rho >= 128M/kappa''.
- **Extraction remainder, (W12) and F11.6, lines 752-799: correct.** r - r_1 >= ceil((p_0/2+1) log_L log xbar_s) + r_0 - 1, because ceil(log_L(20 L rho)) <= ceil(log_L(20 L C_W(s))) + 1 when rho < L C_W(s), that is when s >= 1. Then T_6 <= A_0^4 L^{8-8 r_0}, T_5 <= L^{4-4 r_0} and T_4 <= A_0^4/C_D. The first entry of D_square is <= 1 + c_a^-1 (20 p_0 log xbar_s + 8 log(L C_0 A_0^2) + log C_D). All these match II:72905-72952.
- **Irrelevant remainder and F11.7, lines 801-817: correct.** rho^-2 p_0(g_{k0})^4 <= C_0^-2, because p_0 increases in g^-2 and x <= xbar_s. Then 7 C_b/C_0^2 <= 1/64 when C_0^2 >= 448 C_b. Making the E_a allocation explicit (M/(6 64) per term) is a valid reading of "under the same order of constants" (II:73045-73046).
- **F11.8 and C11.2, lines 882-906: correct.** Each majorant has log <= A(1 + t^{r_R}) + B t + D log t - c A_0 t^{p_0}, with p_0 >= 5 r_R and p_0 > 1. Also (eps_j/eps_k0)^2 <= 2 (2^{1/p_0})^{2 p_0} = 8. And sup Rcheck^4/p_0^2 is bounded since 4 r_R <= 2 p_0. The source's claim that F_src "is decreasing for y >= y_0" (II:73393-73394) is not proved; the radius function may jump. Only the tail supremum is needed, and it is non-increasing in X by inclusion. "gamma_W is defined as the largest g" (II:73273) assumes that a largest admissible g exists; any positive admissible ceiling suffices.
- **H-depth, line 536: the gap is real, and the repair is right.** s_W(g) is the least s meeting three conditions (8.1:eq-coupling-envelope-d). The proof (II:69048-69069) shows only that the set contains all large integers. But the theorem assumes s(d) >= s_W(g) and uses the conditions at s(d). r(s) is a sum of two ceilings of slowly increasing arguments, so r(s+1) - r(s) can be 2, and then s - r(s) drops by 1. Likewise 2B(r(s)+1) <= xunder_s can fail just after a jump of r, since 2B >= 2 lambda > lambda. So upward closure is not shown. The port's repair (least tail floor; it exists by the proof just cited) is correct. It only raises the floor.
- **Final count, lines 908-915: correct.** |S^T - M| <= 6M/32 < M/4. N_{K-s} lies in [1 - d_W, 1 + d_W], inside [2/3, 4/3], by (gamma-7).

Standing: C11 is a proved implication from the port's named hypotheses, with the tail-floor repair of s_W. The port's statement-to-supplier qualifications (H-source-use, H-GXa, H-GXb) are accurate descriptions of what the account leaves open (II:71368-71370 "proof is incomplete at the step marked (*)"; 8.21:lem-source outstanding).

## 4. Reference-torus assembly, p9-witness.md lines 917-1107

Sources read: 8.22:lem-signed-translates and its remark II:141854-141990; 8.22:def-expansion-consistency and its proof II:142166-142314; the proof of 8.22:cor-transfer-depth-floor II:142372-142470; the proof of 8.22:cor-reference-torus-kernel and the infinite-volume consequences II:142633-142720.

Result: **first failing step none**, except that the positivity sentence at line 1105 inherits the empty-class issue of Section 2.

- **Signed translates, lines 1013-1049: correct.** r <= r' < 2r and |Gamma| = (2 floor(R/(16r')) + 1)^4 >= (R/(32r))^4. The balls are 2r apart and lie in B(y,R). Each f_i vanishes on its sphere, so ||F^sigma||_inf = ||f_i||_inf. The exit/entry argument gives Lip F^sigma <= Lip f_i, which is enough; the source also proves the reverse inequality. The sign average leaves |Gamma| D(f_1,f_2). With R = 1, r = 5d, d <= 1/40 and eps <= d: ||f_i||_sharp <= 40M||f_i||_inf/(theta d), so C_T(g) = 5^4 32^4 (40M/theta)^2 C_VT = 160^4 (40M/theta)^2 C_VT. That matches II:141984-141990.
- **m_star = m_T(g_-(g)), line 1053: correct.** l <= 32L <= L^11 M <= L^{m_T} (II:142206, II:142381).
- **C-V1, line 1055: correct.** gamma_star^V is the supremum of A = {eta : m_star(g) <= m_V(g) for all g in (0, eta]}. The proof (II:142222-142226) shows only that A is closed downward. Both exponents are integer step functions of g, so the supremum need not lie in A. Requiring g < gamma_star^V, or keeping m_star <= m_V at the endpoint as a hypothesis, is the right fix.
- **(V2) and FV.1, lines 1057-1065: correct.** These are (8.22:eq-expansion-consistency-b). Unlike s_W, the source defines s_T as a least tail floor and says so (II:142242-142243: "no monotonicity in s of their left sides is needed or claimed").
- **Transfer, lines 1067-1088: correct.** It matches II:142386-142470 step by step: s_T >= 1, d < L C_W(s) L^-s <= 1/40, L^-K < d, the midpoint ball of radius 5d, the lifts, M_star >= (4/9) b_0 c_K xbar_s^-2 ||f_1|| ||f_2||, a transfer cost of at most (1/9) b_0 c_K xbar_s^-2 ||f_1|| ||f_2|| = M_star/4, and |R_K| <= 1/2.
- **Line 1090: correct.** The optional comparison K_s^(m)/K_star ~ 1 is not used.
- **Limit modes, lines 1092-1103: correct.** It is the closed-interval argument of II:142633-142690. No limits are exchanged.
- **Line 1105 (positivity in R^4): repairable, the same issue as Section 2.** Both routes need a pair in T(d; theta): a reflected pair for the port's route, and any C^1 pair for the account's dichotomy route (II:142705-142720). T(d;1) is empty, so for theta near 1 the conclusion dim H^curv >= 2 is not derived. *Repair:* for theta <= 1/2, f(y) = (1 - |y-x|^2/r^2)_+^2 with r = 9d/10 is C^1, with integral pi^2 r^4/12 > 0.53 d^4 and Lip f = 8/(3 sqrt 3 r) < 1.72/d <= 1/(theta d). Centred 19d/10 from a lattice mirror, the pair (f, iota f) lies in T(d; theta), and so do its dilates. The reflected route also needs reflection positivity of the R^4 limit at that mirror, which H-limit must state.
- **Line 1105, "H-CK ... its absence has not been cured by the closed-interval argument".** This is too strong for C9(d); see Section 2. It is right for (h3) of 8.1:lem-kernel-bounds.

Standing: the assembly is a proved implication from C9(a) on T_m_star, C10, H-flow and the limit construction, with C-V1 as stated in the port and theta <= 1/2 for the positivity consequences.

## 5. C5 (8.2:prop-gaussian-extraction), p9b-extraction.md

Sources read: the statement II:77279-77433 (the port's block is verbatim, 155 lines, no difference); the proof II:77434-77772; the tower proof II:77774-77859; the window bound and tails of the one-point lemma II:76970-76990 and II:77018-77050; 8.2:def-local-observables II:74118-74160; 8.2:def-two-densities II:77201-77268; 8.1:rem-extraction-errors II:71180-71236.

Result: **first failing step none.** The port follows the source's route. Its two corrections and its named open inputs (H-jet, H-tail-sum, H-support) are accurate.

- **Clause (a), F1 and C1, lines 235-260: correct.** The Cauchy bound j! M^2 rho^-j for the product holds on the product tube. *C1 is right:* B_l(p) is the set of bonds within graph distance l of p (II:74126-74127). Two supports in B_l(p_1) and B_l(p_2) at distance <= 6C_W need not lie in a ball of radius l + 6C_W; the port's interval example shows it for l > 3C_W. The printed size l + 6C_W holds if d(p_1, p_2) <= 6C_W. In general the product lies in B_{3l+6C_W}(p_1). *Repair:* use 3l + 6C_W (still comparable to C_W, since l_W is), or keep the enclosure as an admission, as the port does.
- **Recursion (P9b.4)-(P9b.5), F2, lines 262-293: correct.** This is (8.2:eq-gaussian-extraction-6).
- **Carried remainders (P9b.6)-(P9b.10), F3-F4, lines 295-368: correct.** It uses the window bound sup kappa <= 2 eps_{k0+i+1} <= 4 g P (II:76976-76979). That bound is on the curvature of the whole level window, so it also bounds the box curvature kappa-bar^B. This justifies the port's "both barred curvatures" (line 336). The source writes the bound only for kappa-bar (II:77553-77554), but it uses it for kappa^B too (II:77738-77740: g^4 kappa kappa^B becomes g^4 (g p_0)^2). The port's allocation avoids the source's identification of g^4 kappa-bar kappa-bar^B with the final-level member g^4 (kappa_1 + kappa_2) kappa^B_W (II:77572-77575). The small-coupling admission P >= 1, that is x >= exp(A_0^(-1/p_0)), is needed for g^5 Pi <= g^5 P Pi and is now explicit.
- **One step, F5 and (P9b.14), lines 370-417: correct.** E^Phi is the bilinear remainder of DM = u + v. The chain rule for D^2(G o B) adds DG[D^2 B] and D^2 Q. The port names their estimate H-jet and does not claim it.
- **Two-line term, F6, lines 419-447: correct.** E xi_a xi_b xi_c xi_d = K_ab K_cd + K_ac K_bd + K_ad K_bc. Symmetric Hessians give Cov(H_1[xi,xi], H_2[xi,xi]) = 2 E H_1[xi,xi'] H_2[xi,xi'], hence the coefficient g^4/2.
- **One-line term, F7-F9, lines 449-506: correct.** By Cauchy-Schwarz with E|DG_a[xi]|^2 <= C L^-4i (C_ax mu_2 kappa_a)^2 we get (8.2:eq-gaussian-extraction-1). The degree-two Taylor term of g^2 u_1^T C u_2 with u_a(0) = 0 is g^2 (Du_1 Z)^T C (Du_2 Z). Its trace against Gamma_j times g_j^2/2 gives g_i^2 g_j^2 (H_1 x H_2)[Gamma_i, Gamma_j], once for each unordered pair. F9 correctly records that the flat calculation does not give the non-flat terms.
- **Colour factor, F10, lines 508-534: correct.** (H_1 x H_2)[Gamma_i, Gamma_j] = n c_i c_j, and (n/2) sum g_i^4 c_i^2 + n sum_{i<j} g_i^2 g_j^2 c_i c_j = (n/2)(sum g_i^2 c_i)^2.
- **Error collection, F11, line 540-559: correct.**
- **C2, line 561: correct.** The carried Psi_i value is identified with the G_a-Hessian expression at II:77642-77647. Psi_i is defined with Hess M_{a,i} (II:77620-77622), so the replacement error (P9b.14) is missing there. It has the order of errors already collected.
- **F12, line 563: the gap is real.** The one-point lemma's tails sum to r(e^{-c_loc(D - l_r)} + e^{-c_w b^2/C}) (8.2:eq-remainder-recursion-5, II:77030-77032). C5's display (8.2:eq-gaussian-extraction-3) prints M^2(e^{-c_loc D} + e^{-c_w p_0^2}), with no factor r and no loss l_r. So the printed constants are not derived. A repair needs a smaller rate. The consumer can absorb that, because D_square in (8.1:eq-extraction-remainder-1) is chosen through c_a. The port keeps this as H-tail-sum and does not change a rate; that is correct.
- **Clause (c), F13-F14, lines 567-626: correct.** The increments are orthogonal, the conditional covariance of a Gaussian vector under linear conditioning is constant, the sum telescopes, and |cov_n(X_I, Y_I)| <= C_eta L^-4I. The source writes Cov(ell_p1, ell_p2) for g_12 (II:77780) while the statement has the factor n^-1. The port's per-colour reading fixes this notational slip.
- **F15-F16, lines 628-673: correct.** G_inf^2 - G_r^2 = 2 G_r t_r + t_r^2, and Cov = E Cov(.|Z) + Cov(m_1, m_2).
- **H-GXa and H-GXb mapping, lines 675-699: correct.** (P9b.25) is (8.1:eq-extraction-errors-1) verbatim in content. The witness says it recalls that bound "from clause (a) of the Gaussian extraction" (II:71185-71186). Printed clause (a) of C5 has no such six-term bound, and printed clause (b) has no 7 C_b rho^-2 p_0^4 bound. So the witness cites contents that the final proposition does not print. The port names this as an open supplier mapping, which is right.
- **F17, lines 705-720: correct as arithmetic** under the outline's ET3 inputs: x^-2 r^8 t^{2p} A <= C' x^-2 [t^{21p-q} + t^{18p} x^-a], and q >= 21p + 1 gives t^{21p-q} <= 1/t.

Every label cited in the input tables of both ports was looked up in CA-I or CA-II. Each exists at the cited line, or within one line of it, with the standing the port states ("Stated; proof incomplete", "Proof outstanding", or a remark placeholder). No fabricated label or step was found.

Checked line by line by Claude (Mini worker).
