lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T16:58Z

# Check of row 1036 (`library/gap-boundary-q.md`): queue row 1037, `gap-boundary-q-check-opus`

Checker: Claude Opus 5.5, max effort, Mac mini worker 3, started 2026-11-16T04:58Z, at commit 904e6a771.
Object of check: `library/gap-boundary-q.md` (row 1036, written by Claude Fable 5.2 medium; same provider, so this is not an independent-provider check).
No new attack (row 1037 instruction). Verdicts per item: HOLDS, HOLDS AFTER CORRECTION, FAILS with the first failing line.

## Plan (at most eight steps; one step per response, result appended before the next)

1. Read FINISH.md rules (efficiency, build on published work), row 1036 and row 1034 entries, and `library/gap-boundary-q.md` in full; record its statement inventory and line anchors here.
2. Test first (a): the cube value Q = 4 beta xbar for n_100 = n_010 = i, n_110 = j, by hand from the definitions in the file.
3. Test first (b) and (c): the sign of H_c in Theorem H4; whether the frame class matches row 1034's pin-measurable site frames (read row 1034's file for the frame definition).
4. Line-by-line check of Theorem GR (boundary gradient = gauge move followed by pin move W_l) and the cube values of Q(d lambda) and H_c with xbar and kappa from the character expansion.
5. Line-by-line check of Theorem TP (positivity in the 4D cell at the trivial pin for every box) and Theorem H4 (beta <= 3).
6. Line-by-line check of Lemma MASS (60 b sum lambda_head^2 |D_l n|), Proposition SIGN, and the U(1) control.
7. Judge the ARGUED meaning: route (ii) closed at the pinned boundary as an exact mechanism; check what it consumes and what it delivers against row 1034/1036 and open-core.
8. Verdict table and RESULT line.

## Step log

(Each step below is appended when finished.)

### Step 1 (done 2026-11-16T05:05Z): rules, rows, and the statement inventory of row 1036

Read: FINISH.md L1-84, L299-360 (Joining, Working efficiently, Rules), rows 1034-1037 (L1115-1118); GOAL.md in full; `library/gap-boundary-q.md` L1-391 in full (the object of check, at commit 904e6a771; last touched by 8497b991e).
Rule notes that bind this check: no computer-assisted step (a run may refute or guide only); check reports give a verdict per statement and only the defects that break something; no new attack (row 1037).

Inventory of row 1036 (line anchors in `library/gap-boundary-q.md`):

| Item | Lines | Claim | Mark in row 1036 |
|---|---|---|---|
| Definitions | L31-44 | conventions of row 1011 3.1-3.2; Q(theta) := - E[V Psi_V]; H_c = Q - Var(Psi) | from rows 1011, 1018, 1026 |
| GR (a)-(e) | L65-97 | (d lambda) n = gauge move g = exp(eps lambda n) then pin move W_l; Psi, Q, H_c formulas | PROVED |
| CUBE-Z | L99-120 | Z_c = e^{b_0 t(h)} G(t(h)), G(t) = sum_d d u_d^5 U_{d-1}(t); xbar, kappa | PROVED |
| CUBE (i)-(iv) | L122-137 | Q(d lambda) = beta xbar (abs(delta_1)^2 + abs(delta_2)^2) + b_0 abs(delta_1 - delta_2)^2; H_c = (b_0 + kappa) abs(delta_1 - delta_2)^2 | PROVED |
| Examples A, B; covariant cube frame | L139-153 | A: Q = 4 beta xbar, H_c = 0; B: H_c > 0; covariant pin frame on the cube has D n = 0 | PROVED |
| GUIDE run | L155-167 | numbers only | GUIDE |
| TP | L173-191 | box, trivial pin: Q(d lambda) = sum_p beta_p w_p xbar_p abs(sum [p:l] b_l)^2 | PROVED |
| TP4 | L193-211 | 4D cell: Q = beta [sum_i (1 + xbar_i) abs(delta_i)^2 + (1/2) sum_{i<j} abs(delta_i - delta_j)^2] | PROVED |
| OPEN-SET | L213-229 | plaquette-axis covariant frame: Q(d lambda) >= beta (1 + xbar_1)/2 on an open set of pins | PROVED |
| SIGN | L231-244 | one link: Q = 2 e_l (1 - cos alpha) + 2 sin(alpha) nu . E[N_l] | PROVED |
| (Q-INV) verdict | L246-259 | FAILS | verdict |
| H4 (i), (ii) | L269-293 | beta <= 3, one delta_i: H_c(1; (d lambda) n) > 0; open set for the axis frame | PROVED |
| MASS | L295-309 | abs(Q(d lambda)) <= 60 b sum lambda_head^2 abs(D_l n) in 4D | PROVED |
| (O2) verdict | L311-322 | FAILS for every C | verdict |
| U(1) | L326-330 | every statement passes, zero gain | PROVED |
| Meaning | L332-345 | route (ii) closed at the pinned boundary as an exact mechanism | ARGUED |

Sources still to read for the definitions (Step 2 onward): row 1011 3.1-3.2 (`library/gap-pinned-cell-gauge-max.md`), Lemma FLOW (`library/gap-short-step-max.md` 4.1), row 1026 7.1, row 1034 Theorem BD and 6.5-6.6 (`library/gap-sym-reg.md`), check 1035 Step 5 and the class test (`library/gap-sym-reg-check-opus.md`).

### Step 2 (done 2026-11-16T05:25Z): test (a), the cube value Q = 4 beta xbar, by hand. PASSES (three derivations)

Definitions read and used: row 1011 3.1-3.3 (`library/gap-pinned-cell-gauge-max.md` L131-201: cell, weights w_p = 1/(number of tiling cells containing p), action, Z_c, F_c, Proposition A); Lemma FLOW and Lemma PROJ (`library/gap-short-step-max.md` L217-246: Psi_V = V A + div V, H_c = - E[V Psi_V] - Var(Psi_V)). Row 1036's Q(theta) := - E_omega[V Psi_V] (L41) is FLOW's first term. For a field V that is fixed (a function of the pin only) on every link, div V = 0, Psi_V = V A, and V Psi_V is the second derivative of A along the flow e^{eps V}.

Setting of the test: cube {0,1}^3, lower face pinned to the trivial pin, n_100 = n_010 = i, n_110 = j, lambda = indicator of 110. Then V = (d lambda) n is: - n_100 = - i on l_1 = (100 -> 110); - n_010 = - i on l_2 = (010 -> 110); + n_110 = j on the free vertical link (110 -> 111); 0 elsewhere.

**Derivation 1 (direct flow, no use of GR).** Only three plaquettes contain a moving link.
- Lower plaquette p_0: holonomy 1 . e^{- eps i} . (e^{- eps i})^{-1} . 1 = 1 for every eps. Contribution 0.
- Side plaquette (100; 2, 3): holonomy e^{- eps i} e^{eps j} R_1, R_1 = V_110 T^{-1} V_100^{-1} (three free links). The constant gauge transformation fixes the trivial pin and the law, so E[Im R_1] = 0, and E[t(X R_1)] = t(X) xbar with X = e^{- eps i} e^{eps j}, t(X) = cos^2(eps) (Re(i j) = 0). - (d/d eps)^2 at 0 gives 2 xbar. Contribution 2 beta xbar.
- Side plaquette (010; 1, 3): the same, 2 beta xbar.
- Top plaquette: no moving link.
So Q(d lambda) = 4 beta xbar. This equals row 1036 4.3 (ii) at delta_1 = delta_2 = j - i (abs(delta_i)^2 = 2, delta_1 - delta_2 = 0) and the claim of 4.4 Example A (L140).

**Derivation 2 (row 1036's route).** GR (b) at omega = 1, tau = 1: b_{l_i} = - D_{l_i} n = n_110 - n_tail = delta_i. TP-type expansion of t(W_i) = 1 - eps^2 abs(delta_i)^2/2 + O(eps^3); lower plaquette W_1 W_2^{-1} = e^{- eps n_100} e^{eps n_010} = 1 here. Same value 4 beta xbar.

**Derivation 3 (a different data path: a Ward identity in the plaquette variables of CUBE-Z, checking Var(Psi) and H_c).** In the variables Y_k = omega_k T_k'^{-1} of CUBE-Z (L112-115) the flow is Y_2 -> X Y_2, Y_3 -> X Y_3, with Y_1, Y_4 fixed, and the top holonomy Y_1^{-1} Y_2^{-1} Y_3 Y_4 does not move. Simultaneous left translation Y_2 -> e^{s a} Y_2, Y_3 -> e^{s a} Y_3 (a a unit imaginary) preserves Haar measure and the top factor, so integration by parts gives E[Psi_a^2] = - E[(d/ds)^2 A] = beta (E t(Y_2) + E t(Y_3)) = 2 beta xbar, with Psi_a = - beta a . (Im Y_2 + Im Y_3). Here Psi = - beta (j - i) . (Im Y_2 + Im Y_3) = sqrt(2) Psi_a for a = (j - i)/sqrt(2), so Var(Psi) = 4 beta xbar. Then H_c = Q - Var(Psi) = 0, which matches the gauge return: along the pin curve h(eps) = 1, and Z_c depends on t(h) only (CUBE-Z), so F_c is constant (L133-134, 4.3 (iii) at delta_1 = delta_2).

Verdict on test (a): **PASSES.** Q = 4 beta xbar(beta), H_c = 0, Var(Psi) = 4 beta xbar, with xbar = E_1[t_p] of a side plaquette, in (0, 1). Derivation 3 does not use FLOW's identity H_c = Q - Var or GR; it agrees with both.

**GR (a)-(e) re-derived in the same pass (recorded here so it survives; Step 4 adds the rest).**
- (a) For a pinned link (x -> y): g_x^{-1} exp(eps (lambda_x - lambda_y) n_x) omega_l g_y = exp(- eps lambda_y n_x) exp(eps lambda_y Ad(omega_l) n_y) omega_l. Correct (the two exponentials along n_x commute; omega e^v = e^{Ad(omega) v} omega). Free link out of z in L: its head is free, g = 1 there, the factor cancels. Free links into L do not exist by the definition of L; other free links carry V = 0 and g = 1 at both ends (lambda = 0 off L). The box claim (L67-69: for S_mu >= 2 the head of a free link out of L is free) holds: a free link (z, mu) at a boundary site z needs 0 < z_k < S_k for k != mu, so z_mu = 0 and its head has mu-coordinate 1 < S_mu. HOLDS.
- (b) exp(eps tau v) = 1 + eps tau v - eps^2 tau^2/2 + O(eps^3) for a unit imaginary v; the product gives W'(0) = - tau D n, W''(0) = - tau^2 abs(D n)^2 - 2 tau^2 n x m, and the second derivative b^2 + 2 c of exp(eps b + eps^2 c) gives c = - tau^2 n x m = tau^2 n x D n. HOLDS.
- (c) With R_(l,a) A = - a . N_l: Psi = - sum b_l . N_l = sum tau_l (D_l n) . N_l. Cross-check by PROJ's gauge identity X(G) = 0 with G = (d lambda) n + lambda_head D n: the links with head in L are all pinned, so the same formula follows. HOLDS.
- (d) A is affine in each link; the second derivative along the pin curve is sum_l Re(W_l''(0) omega_l S_l) + M(b) (ordered pairs give the factor 2). Re(W'' omega S) = - tau^2 abs(D n)^2 Re(omega S) - 2 tau^2 (n x D n) . N_l. HOLDS.
- (e) Z_c(e^{eps B} omega) = Z_c(omega_eps): left translation of the free links by e^{eps V} preserves Haar measure, then gauge invariance of A. F'' = - E[A''] - Var(A'). HOLDS.
