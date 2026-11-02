lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T14:22Z

# Gate: `library/excess-shell-end.md` (queue item 26, `shell-gate`, mapped side)

**Provenance.** Model anthropic/claude-opus-5-5, effort high, Mac mini worker, pinned at commit c16e2a968, no subagents. The note under gate was written by OpenAI Codex, so this is a cross-provider read of the note. It is one session. Its checks of Claude-written inputs (`sector-values.md`, `fibre-propagator.md`) are same-model, not independent in model, and not an audit. Verdicts steer research and grant no status.

**State: main sections written; the run section is pending.**

## Verdicts

| Statement | Verdict | Note |
|---|---|---|
| Section 1: extension, weighted (TS), sampled/compatible conversions | ADVANCE | Rechecked line by line |
| (INPUT) + (UP) => (FALL-1) | ADVANCE, as an implication | Recursion, (HF), induction and C_F all hold; D2, D5 are local |
| (INPUT) as supplied to it | CORRECT-NO-ADVANCE | C_E is not delivered by the Gronwall the source names: D2 |
| (FALL-1) is the FALL that DS reads | ADVANCE, as an implication | DS reads less than FALL: D1. COMP-B reads level 0: D5 |
| (TR) + (WAM) + flux => (UP), (UP-constants) | ADVANCE, as an implication | Stronger than (UP) needs: D7 |
| (E-SHELL) => (WAM-shell) | ADVANCE, as an implication | Layer cake, K*w <= M_* w and the division all hold |
| (GLUE-E) => (E-SHELL); (SEAM); (LC) => (E-SHELL) | ADVANCE, as implications | Exact identities; constants A_s >= 2 in the (LC) step |
| b_s nu_* <= 1/2 in the mapped order | WRONG as a usable condition if b_s grows with L; not needed by DS | D1 |
| Two-site, tensor | Arithmetic ADVANCE; as tests CORRECT-NO-ADVANCE | They cannot fail: D3 |
| Kill criterion of Section 2 | WRONG as a kill criterion | D4 |
| (WAM-slab), (GRAM), (MOM) | ADVANCE | Rechecked. In fact 1 + O(nu^2) |

**Result beyond the note.** In the flat linear four-dimensional model, (WAM) and (LC) both hold with absolute constants, by a direct proof from Lemma TP-sharp, in `library/wam-direct-flat.md`. So the note's statement that even linear (LC) is unsupplied is out of date at flat background. This is linear and flat only.

## Defects, ranked by what each breaks

**D1. The rate condition does not survive the mapped order as written, and DS does not need it.** In the order of constants (mapped file, line 24), nu <= delta/4, delta'' and mu come before L, while A_s(L), r(L), M_*(L) come after. So b_s nu <= 1/2 at the consumer's nu asks for b_s bounded free of L. A finite C(L) does not give it. Moving nu after L is not available: mu is read before L, and C_1 of the high-order contraction is absolute in a sum weighted by e^(mu d) (`one-step-closure.md`, line 60). Inside the route it cannot be weakened: (E-SHELL) alone cannot give (WAM) above about 1/(2 r A_s), by the scalar example in `library/wam-direct-flat.md`, Section 4, so the condition is sharp within a factor 2.

*Repair, proved given (FALL) at the smaller rate: Lemma DOM.* The note says choosing nu_* < nu_req "does not prove that consumer's statement". True of the display (FALL), but DS does not read the display. It reads only I_(k-m)(Lambda_m V_t; W_y^+) <= C(L) q^m T_2^2 (`sector-values.md`, lines 218, 220), with the decay in y supplied by Lemma CRUDE. COMP-B likewise reads only a_m <= C q^m T_2^2. Weighted sums are monotone in the weight, and W_y^+ <= C exp(-nu_s d(., y)) pointwise for nu_s <= nu. So (FALL) at any nu_s(L) > 0 gives what DS reads, at the cost of a factor nu_s^-4 in C(L), paid at x_*. The output rate of DS stays delta''/2. As b_s(s) s <= 1/2 for small s whenever A_s, r and a moment are finite, **the condition becomes automatic for DS and COMP-B**. Prop GS in Theorem VAL has W = 1, rate 0. The one reader left is the region clause (below, D6).

**D2. (INPUT)'s C_E is not what the source's Gronwall gives, and its display drops tau.** From (INPUT), E_j <= E_0 + sum_(i <= j) b_i with b_i <= D_EX (f_i + nu_i) E_i + tau_i. The i = j term is implicit, so Gronwall needs D_EX(L)(f_j + nu_j) < 1. At top levels nu_j is about nu, fixed before L, and D_EX = C(L). So this is a second hidden rate condition, D_EX(L) nu < 1, in the source's FALL proof (`sector-values.md`, line 174), not only in this note. Also (UP) at l = k gives E_0 <= K E_k + D tau_k, so the display should read E_j <= C_E (E_k + tau_k). The note flags Gronwall as unchecked, but not these two.

*Repair (unproved in detail, local).* The tau term only enlarges D_0. For C_E: Gronwall upward for the levels with D_EX (f_j + nu_j) <= 1/2, then for the top m_0(L) <= 1 + log_L(2 D_EX nu) levels the crude one-level bound E_j <= C(L) E_(j-1)(W^+) from Stokes on a block, giving C(L)^(m_0(L)), finite. Or use Lemma DOM with nu_s <= 1/(4 D_EX(L)), which removes it outright.

**D3. The two-site and tensor tests do not test the route.** Their arithmetic is right. They cannot fail, for reasons that have nothing to do with Yang-Mills.
- *Tensor.* (sum w)(sum w^-1)/N^2 <= cosh^2(nu diam/2) for any finite set, by Kantorovich, however its points are arranged. The tensor set has diameter at most 3/2 whatever n is. So independence of depth is automatic, and the depth in the construction does nothing.
- *The order nu^2.* By Lemma Q, every orthogonal projection obeys ||W^(1/2) R W^(-1/2)||^2 <= 1 + 4 j^2 + 2 j^4. So 1 + O(nu^2) is generic and is no evidence for this route. It holds in the slab too, so (WAM-slab)'s 1 + D nu is not sharp.
- *What they leave out.* All of the difficulty: closure of the trial (Bianchi), the gauge in H, composite parents per block, and many blocks at once. The slab has many blocks, but in d = 1 curvature space has no closure.
The right test is the closed-trial ratio on the true composite. The run below does it, and it shows that omitting closure gives a false alarm the other way (K3).

**D4. The kill criterion of Section 2 is not one.** "A ratio exceeding 1 + D nu for every D would kill this route" tests the worst trial in the fibre. (WAM) is about the specified trial T. A sup that grows would not refute (WAM) at T, and K3 below is a live example of a sup growing while the route survives. It is the survival half that the note reads correctly: "proves no nonlinear claim".

**D5. "No bare level-0 gradient" is true of SRC, not of DS's whole tree.** DS reads CRUDE, CRUDE reads (COMP), and COMP-B sums S_i^beta from i = 0, with FF_m at m = k, which is the level-0 gradient (`sector-values.md`, lines 190, 194). (FALL-1) stops at level 1.

*Repair, local.* The single term i = 0 needs no decay: ||d_t^(n-1) theta^0||_(l^4) <= ||d_t^(n-1) theta^0||_(l^2) <= X_(n-1), bounded at the order below. So X_n still closes. COMP-B should say so.

**D6. The region clause is a second reader of the rate.** `sector-values.md`, Section 6, reads Prop GS at a cut-off W_0 of rate about 1/r_S. Lemma DOM does not apply, as W_0 is a real cut-off. The (WAM) route needs r_S >= C b_s(L) there. r_S comes after L, so this can be added to its maximum, at the cost of t_0, and I have not checked the budgets t_0 feeds. If (WAM) comes directly at an absolute rate, this goes away.

**D7. (WAM) asks too much.** (UP) already pays (f_l + nu_l) E_l, so A_U(w) <= [1 + D (nu_l + f_l)] A_T(w) + D tau_l is enough, and nonlinear errors can go there. A coefficient O(nu^2) is the truth in the linear model. Only a change of target, no error.

**D8. Section 5's rule is stricter than the consumer.** "If the consumer has already fixed nu_req>0, the (GLUE-E) route must establish its moment at least through nu_req" holds for the display (FALL) only; by D1 a moment at nu_s(L) is enough for DS.

## Direct linear (WAM)

The note leaves linear (LC) open and offers direct (WAM) as an alternative. Written proof in `library/wam-direct-flat.md`, conditional on Lemma TP-sharp at U = 1 and the bumps of Theorem 6, which are same-provider and ungated:

- Lemma WP: ||e^f H||_Eps <= C_1 ||e^f d H|| on ker Q^o in the gauge P_r D^* H = 0, Lipschitz constant of f at most an absolute delta_1.
- Theorem WAM-lin: ||d A_*||_w^2 <= (1 - C_2^2 delta^2)^-1 ||d A_t||_w^2 at an absolute rate, free of L, depth and volume. The proof tests minimality on G := w H - F Q^o(w H) and needs no cut-off.
- Corollary LC-flat: (LC) with C_seam absolute and r = 2, so A_s, r and M_* are absolute, and b_s nu <= 1/2 can be met before L in this model.

Section 5 there proposes the same identity for the nonlinear (WAM) with no gluing, labelled gap: inputs (N1) to (N4), the first target being N(T) = N(U) => ||Q_U^o H|| <= eps ||H||, uniformly in depth.

## Run

`checks/gate_se/`, criteria in `CRITERIA.md`, written before each stage. Linear, flat, a few lattices: a run can refute or guide, and these discharge nothing. Nothing in the chain reads them.

**Stage 1, registered: sup over all 2-forms.** Identities pass (P^2 = P to 3e-16, zero coarse curl of Q(A - A_*) to 2e-16 in real space, rank 3 per coarse momentum). A first version had a bug in the Gram matrix, caught by the identity check; no result of it is used. K1, K2 pass. **K3 FIRED**: D2(M=6)/D2(M=4) = 2.07 (radial), 1.75 (zig), growing to M = 8. So the registered prediction was false for that quantity. Lemma Q is not contradicted: j grows with M there.

**Stage 2, post hoc, written after K3: sup over closed trials**, the actual linear (WAM) ratio. D2c := (rho_c - 1)/nu^2, control w = 1 gives 1 to 1e-14.

| Profile, nu = 0.2 | B=3, M=2 | M=4 | M=6 | M=8 | B=9, M=4 | B=15, M=2 |
|---|---|---|---|---|---|---|
| radial | 0.146 | 0.411 | 0.542 | 0.609 | 0.444 | 0.157 |
| zig | 0.074 | 0.145 | 0.198 | 0.233 | 0.159 | 0.083 |
| step (exploratory) | 0.223 | 0.310 | 0.362 | 0.390 | 0.369 | 0.250 |

K1c passes: B = 9 against B = 3 at M = 4 is 1.08, 1.10. K2c was **not run**: B = 25 was skipped at 40 percent memory free. D2c is flat in nu from 0.1 to 0.4 to within 5 percent, so the law is nu^2. **K3c FIRED**: D2c(M=8)/D2c(M=4) = 1.60 (zig), 1.50 at nu = 0.4 (radial), 1.48 at nu = 0.1 (radial), against a bar of 1.5. I registered that as refuting the hand proof, and the data alone could not clear it: the sequences fit D_oo - c/M and, for zig, roughly log M.

**Stage 3, post hoc, written after K3c: the limit with no torus.** D_oo(s) := sup_p ||Pi_H(p) (s.d_p P(p)) on Ran P(p)||^2 is the second-order coefficient for wide envelopes. Result at B = 3: D_oo(e_0) = 0.323, D_oo(1,1,1,1) = 0.743, at zone-boundary momenta. The 1/M fits of Stage 2, made before this was computed, gave 0.33 and 0.80. Along rays the coefficient falls as |p|^2, 1.1e-6 at |p| = 0.01, so B1 passes and there is no log. Every torus value lies under D_oo, so flag B3 is silent. So K3c fired on an arbitrary bar set in the unsaturated range M = 4 to 8, and D_oo is what decides it. Lemma WP's bound is not contradicted.

The kill criteria of Stages 2 and 3 were written after seeing a failure. Read them as a diagnosis, not as an independent prediction.

## What was and was not read

Read in full: `library/excess-shell-end.md`. Read by range: `sector-values.md` 3A, 3B, Sections 2 (SRC), 4, 6; `one-step-closure.md` Section 10 and its order line; `fibre-propagator.md` to Theorem F, with the statement of F-D; `block-poincare-energy-package.md` Lemmas 1, 4, Theorems 5, 6 and Step 5; `excess-consumer-weight-continuation.md` Section 1 and TR-SLOW; `excess-weighted-fibre-stop.md` around (NF-W); `parts/hard-core--mapped.md` line 24, Text 3.1, (R1) to (R3) in part; grep lines of `parts/hard-core--excess.md`, `heavy-wall.md`, `hw-fine.md` that mention FALL.

Not read, as the firewall says: `library/excess-seam.md`, and no independent-side file. I did not open `library/seam-quadratic*.md`, which the row does not forbid, to keep the (LC) result blind. Disclosure: FINISH.md's own rows 25, 29, 33 state in one line each what `seam-lc` and `seam-quadratic` concluded, including (RATE-exact) at nu before L, and grep lines of `heavy-wall.md` and `hw-fine.md` mention a condition (RATE). I read those lines, so my D1 is not blind to the claim. Its proof and Lemma DOM do not read them. TOP's proof, EX's proof and DS's other inputs were not re-certified.
