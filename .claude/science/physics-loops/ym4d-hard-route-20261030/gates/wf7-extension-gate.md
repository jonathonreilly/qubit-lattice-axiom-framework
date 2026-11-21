lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T23:50Z

# Check of `library/wf7-extension.md` (queue row 147)

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, commit 072138cc3 of `claude/ym4d-hard-route`. One reading by one other model. Not an audit and not a human review. The note is by Codex (row 145). SA line numbers refer to `YM4_sketch_500.tex` at `31a47c543775`, fetched once into a scratch folder (sha256 d7f77d4d...). Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for WF3-WF15, OA7-OA8, R8-R9 and the window construction; Tadeusz Balaban for composition and restriction at a critical background's own averages (CMP 109 pp. 275-276, CMP 119 p. 276, both re-read here from `~/ym4d-papers`).

Status: complete.

## Verdicts

**First failing step: none.** Three wording repairs (W1-W3 below) break nothing. Section 6 of this report records a route the note does not list (Balaban's own, unproved here) that may make row 148's uniform localization unnecessary.

| Statement | Verdict |
|---|---|
| Section 5, (5.1)-(5.12): projection-first extension (5.1) fails exact hereditary restriction | **ADVANCE.** Checked line by line by Claude, first failing step none. The test is admissible. The failure survives the nu anchor and the t-integral, and it survives any fixed collar (OA8 allows one). |
| (5.2)-(5.6), the explicit old Green's function | ADVANCE, every identity redone by hand |
| Section 2, (2.1)-(2.2) | CORRECT-NO-ADVANCE. This restates `old-depth.md`, checked in row 141. |
| Section 2, (2.3)-(2.4) and the consumer quotient | ADVANCE as stated. This is a failed inference: the printed argument WF11-WF12/WF14-WF15 cannot carry a bulk term of per-base size delta_k sigma_j^3. It is not a counterexample to an improved route (b), and the note says so. |
| Section 3, restriction lemma, (3.1), (3.2) | ADVANCE. The lemma is Lemma CR again (checked row 141). (3.1) is the product rule. (3.2) is the fundamental theorem at physical endpoints. |
| (4.1) | ADVANCE once its counting premise is stated (W1) |
| (4.4) datum lemma, (4.5) collar estimate, node paragraph (4.6) | ADVANCE as implications from T4, AX, AV, MS, PW and the stated common-chart premises |
| (4.7)-(4.8) | ADVANCE |
| Section 6, (6.1)-(6.2) | ADVANCE as a finite identity on its stated premises (W3). The volume-uniform complex bound is open, as the note says. |
| Result, items 1-4, and "where rank 4 stops" | Correct as scoped. The stopping statement concerns projection-first completions only. |

## 1. Counterexample first: Section 5

### 1.1 The old Green's function, (5.2)-(5.6), redone

- (5.3). With s_m = a_{mL} - a_{mL-1}, the equations (5.2) give slopes a_{mL+r+1} - a_{mL+r} = s_m - (r+1) lambda_m. Summing gives a_{mL+r} = y_m + (r+1)s_m - lambda_m r(r+1)/2, and the slope at r = L-1 gives s_{m+1} = s_m - L lambda_m. Correct.
- Block sums. sum_{r<L}(r+1) = L(L+1)/2 and sum_{r<L} r(r+1) = (L-1)L(L+1)/3. These give u_m and y_{m+1} as printed.
- (5.4). Substitute lambda_m = (s_m - s_{m+1})/L. Then u_{m+1} - u_m = L s_{m+1} - A(2s_{m+1} - s_m - s_{m+2}) = A s_m + B s_{m+1} + A s_{m+2}, with A = (L^2-1)/(6L) and B = L - 2A. Also B - 2A = L - 4A = (L^2+2)/(3L). Correct.
- (5.5). Put c_m = (-1)^m (r^m + r^{n-m}). Then c_{m-1} + c_{m+1} = -(r + r^{-1})c_m, so Bc_m + A(c_{m-1} + c_{m+1}) = 0 for m != 0. The case m = n-1 wraps correctly because n is even, so c_n = c_0. At m = 0, B(1 + r^n) - 2A(r + r^{n-1}) = A(r^{-1} - r)(1 - r^n), using B = A(r + r^{-1}). Correct.
- Invertibility. The quadratic form is at least (B - 2A) sum v_m^2. Correct, also for n = 2, where the matrix is [[B, 2A], [2A, B]].
- (5.6). With s_{m+1} = g_{m+1} - g_m, the left side of (5.4) is the difference of two shifted Green's equations, which is 1_{m+1=0} - 1_{m=0}. For m != 0, A(g_{m-1} + g_{m+1}) = -Bg_m and 2A + B = L, so lambda_m = g_m/A. This is never zero, because r^m + r^{n-m} > 0. The slopes sum to zero, so a is periodic. Fixing y_0 sets the common mean to zero. Correct.
- 4D saddle. Take odd L with centred blocks. Each direction-2 contour term is odd in y_2 - x_2, so the linearized average of the direction-2 slice field has no component on direction-1, 3 or 4 rows, for any fixed contour order. A multiplier independent of x_2 pairs to zero with the site-gradient part: reindex x -> x - L e_2 on the torus. The action gradient (d^T d w) has only a direction-2 component, -partial_1^2 a, and w is divergence free. So the 1D solution is the full linearized old background, and its current on block m is a fixed nonzero multiple of lambda_m T. This agrees with `old-depth.md` (4.5) and (4.8), which passed row 141.

### 1.2 Admissibility of the test

- **The input pair.** By R8 (SA 5747-5759), P = (U, A', J) and the shifted configuration is e^{i eta H} e^{i eta A'} U. So U_+(P) = e^{i eta A'}U is the direct choice, and (5.1) is exactly `old-depth.md` (7.14) with this choice. P_eps = (1, eps a, 0), where a is the step potential on block 0. At a fixed mesh, its plaquette angles are O(eta eps) and its gradient is O(eps/eta). So for eps small at that mesh, it meets the simple and tower conditions of SA Theorem 5 (SA 9746 onward), with the bounds used at SA 15880-15890. An exact identity needs no mesh-uniform amplitude. Admissible.
- **The step response.** SA 5770-5795 requires R9 to vanish at B' = 0 and to split over wall-components when s vanishes on separating cubes. `o1-decoupled.md` Theorem B(d) proves this splitting for Definition D. At J = 0 every branch coefficient j_beta of `h-walk.md` Section 7 vanishes, so H_1(s) has the W-system expansion. Admissible.
- **The member (5.10).** It is polynomial in J, invariant under conjugation, carries no stored colour spectator, and vanishes at the vacuum. These are exactly the hypotheses of the vacuum-only argument (SA 13859-13880 Proposition PW19, and SA 16056-16067). The window machinery has to file every such member, so a single one suffices. Admissible.
- **The grid.** All parameters are 0 or 1, inside |s| < e^{kappa-bar}. A full slab of zero cubes leaves at least three cubes per direction, as Lemma WC needs, and hypothesis (P) holds for a grid of large side. The perturbation of P is strictly inside the slab. Admissible.
- **Order of choices.** Fix L, then M, then k so that (5.8) < sigma_1^3/4. At that k, choose D so that (5.9) < sigma_1^3/4. Then choose the torus (n even, a multiple of the periods, with n >= 2D + slab width, so the slab is at distance >= D from R_z on both sides). Finally choose eps, a and nu small. Nothing chosen earlier depends on anything chosen later. Correct.
- **The old-unit current at z.** D(J o Pi_1)(1)h = L h follows because h is the depth-k flat lift, critical for a sequence containing the depth-1 truncation (Lemma CR, linearized). Then (Lh)_2 = -(q_{m+1} - q_m)T depends only on x_1, so the forward and the backward direction-2 bonds at z see the same value. The note's placement condition ("nearby tests in the same constant-current part") therefore holds automatically.

### 1.3 The anchor and the t-integral (the row's question)

Write X(eps, a) = i eta_k H_k(s; P_eps, B'(a)) and let J(eps, a, nu, t) be the current at b in S_z of Pi_1(e^{(t + nu zeta)X} U_eps). Let c_{ijk} be its Taylor coefficient of eps^i a^j nu^k.

- c_000 = 0, because the projection of 1 has zero current.
- c_001 = 0, because at eps = a = 0 the field is 1 for every nu and t.
- c_101 = 0, because X(eps, 0) = 0 (R9 vanishes at B' = 0), so at a = 0 the field is U_eps whatever nu and t are.

The member is a constant times sum_b (1/2) tr J(b)^2. Its eps-a-nu coefficient is the sum of tr(c_alpha c_beta) over alpha + beta = (1,1,1). By the three facts above it reduces to tr(c_100 c_011), which is tr(A_b C_b). Here c_011 = D(J o Pi_1)(1)[zeta X_1] does not depend on t: t multiplies a only through the (t + nu zeta)aX_1 term, so it enters at order a, not at order a nu. Both statements in the note's paragraph after (5.12) are therefore exact.

- Subtracting Psi_eps(a, 0; s) removes a nu-independent function, so it leaves the nu-derivative unchanged.
- The t-integral of a t-independent nonzero coefficient is nonzero.
- One more point: the computation does not even need X to be independent of eps (splitting). Any eps-dependence of X enters J at order eps a nu, which multiplies c_000 = 0. Splitting is needed only to show that the culprit is Pi_1 and not the step response.

The holomorphy step is also correct. If the anchored, t-integrated function were the same at P_eps and P_0 for all small (eps, a), its derivative in eps would vanish identically, and so would the eps-a coefficient. Since the box map (WF13a) reads only R_z, the removed origin, projected minus inner, carries the nonzero coefficient (5.12).

### 1.4 What the requirement is, and scope

The exact requirement is SA 16194-16213 (with WF13 and wall-component heredity, SA 16216-16238) and OA8 (SA 16846-16852): "After the parameters outside a domain Y are set to zero, a local potential uses only the free coordinates in Y", and "every local term uses only the pair on Y". OA8 allows a fixed collar. (5.5)-(5.6) give lambda_m != 0 on every block, so no fixed collar works, as the note says.

The scope paragraph is accurate. The test refutes (5.1) with only the step's decoupling. It does not touch (3.2), (4.8), or an extension that localizes the old projection itself. One point to add: the obstruction does not depend on the choice U_+(P) = e^{i eta A'}U. Any choice in which P reaches Pi_j through a global map, with s entering only via H_k, gives the same coefficient tr(A_b C_b), with A_b the old current response to the change of U_+ off Y. The only exceptions are choices with no such dependence, or choices that themselves localize. So "route (a) as worded fails" is a fair summary.

**Literature.** The note says Balaban localizes after composing. This is confirmed. CMP 109 p. 275, (3.24)-(3.25), evaluates the old background on a fixed domain, U_j(box_0, ...), with U_{k+1} replaced by U_{k+1}(box_0, M'(U)) extended by U outside box_0. P. 276 defers "a final localization". CMP 119 p. 276 says: "After the completion of the operations of Sects. 3-5 [I] we localize the obtained expressions", using random-walk expansions for the sequence {Omega_j} (Theorems 3.7-3.10 of CMP 99, 389-434). So the published construction is local from the start, box first, and its final localization resums the step-level functions. It is not a global projection with parameters only in the step response. This supports the note's N7 and its diagnosis of (5.1). Section 6 of this report draws the consequence for row 148.

## 2. Section 2: does the consumer inequality fail for (2.3)?

Yes, as the note states it: the printed argument fails, and no counterexample is claimed.

- **(2.1)-(2.2).** These restate `old-depth.md` and its row-141 check. At z = 1/2, |z^2 - z| = 1/4. The error O(sigma^{-3} e^{-a/sigma}) is O(sigma^5) by e^x >= x^8/8!, so the coefficient is >= sigma_1^3/8 for old windows. A bound C sigma e^{-cM/sigma} would force sigma^2 e^{cM/sigma} <= 8C, which is false by e^x >= x^3/6. Correct.
- **The WF11 chain.** SA 16100-16112: Cauchy in the member core costs g_j/alpha_j times the pair change. WF5 gives delta_k/alpha_j <= s_k rho_j. One nu-derivative is taken, then the sum runs over C_M sigma_j^{-4} old bases. A per-base change |nu| delta_k sigma_j^3, the size (2.2) shows at the tested bond, therefore gives C s_k g_j rho_j sigma_j^{-1}. Correct.
- **WF12 and WF14-WF15.** SA 16115-16132 and 16299-16330 need this to be at most C s_k g_j rho_j^3 sigma_j^{alpha_H} (regular, summable weight omega = C(1+a)^{3/2} L^{-alpha_H a}) or at most C s_k d_j rho_j^2 (vacuum-only). WF1 (SA 15719-15731) gives 1 <= rho_j <= C(1+a)^{1/2}. The two quotients are bounded below by L^{(1+alpha_H)a}/(C_0^2(1+a)) and by L^a/(C_0 (1+a)^{1/2}). Both are unbounded. The arithmetic is correct.
- **References.** `WF7` is defined at SA 15861 and cited only at 16102 and 16270, as the note says.
- **Scope.** The lower bound (2.2) is a pair-level coefficient. It is not a lower bound on a member's change: constant-colour invariance or a current-square member can kill first order. The note says this itself. So the verdict is "(b) with (7.11) alone does not pass the printed consumers". That is a failed inference, enough to choose between (a) and (b). It is not a theorem that route (b) is impossible.

## 3. Section 3: the restriction lemma, (3.1), (3.2)

- **Restriction lemma.** This is Lemma CR (row 141, ADVANCE): the variation argument, then continuation by the identity theorem on the connected datum chart. Nothing new is claimed.
- **(3.1).** Redone. W^g_b = g_- W_b g_+^{-1} gives Wdot^g_b = a_- W^g_b + g_- Wdot_b g_+^{-1} - W^g_b a_+, with a = gdot g^{-1}. The based current gives [a_-, J^g]. And (W^u)^v = W^{vu}. Correct.
- **(3.2).** At complete physical endpoints both V(0) and V(1) are critical for sequences containing the old truncation. Lemma CR and gauge invariance identify G(Pi_j(V(i))) with G(P_i), and the fundamental theorem of calculus does the rest. The window decomposition holds because d/dt is linear in the direction eta H_k, and at each bond the shifts (t + nu zeta_b) H_b commute. The note says correctly that this is no identity off the physical locus. Correct.
- **Collar support.** M_T W - M_T V vanishes on the common old rows, because W has V's S^{<=j} averages. Correct.
- **Literature reading.** Checked against `~/ym4d-papers/cmp109.txt`, pp. 273-278. Correct as far as it goes: composition, removal of the part outside box_3 through the response decay ((3.21), small factor O((L^j eta)^N)), gauge transport of J and B ((3.28)-(3.29)), and the deferred "final localization" (p. 276).
- **One point the reading leaves out, which matters for the next step.** Balaban's old background is not a global projection. It is U_j(box_0): CMP 109 p. 273 builds it on the cube sequence {box_n} around the window (condition (iv), p. 262). Identity (3.38) on p. 278 is restriction at that local background. See Section 6 below.

## 4. Section 4: (4.1)-(4.8)

- **(4.1).** The MS count is C(R+1)^4 L^{8+8R/rho} (`a1-balaban.md` 3.7). So S_gamma < infinity needs gamma > 8 log L / rho, and that note's (3.13) takes rho >= 16 log L / gamma. The kernel hypothesis (4.2) needs 2 gamma <= theta, the T4 rate. Together: rho >= 32 log L / theta. The phrase "gamma below the response rate and above its counting threshold" presupposes exactly this (W1). In a constant top layer the count is polynomial, and any gamma > 0 works.
- **(4.4).** Each step was redone:
  - R7 gives one power of sigma_j for a potential, so AV gives |v'_c| <= C delta_k sigma_j.
  - T4 for the global old datum, with the native count, gives the same bound for W.
  - AV again gives |w'_c|.
  - (4.1) gives b_x and B_x <= 2 C_0 r S_gamma.
  
  It is an implication, and its premises (PW, chart membership with ||v||, ||w|| <= C_0 r) are stated.
- **(4.5).** F_R(w) - F_R(v) = integral of DF_R(v + t beta) beta dt. The nu-derivative of the base point is (1-t)v' + tw'. Cauchy on the r-neighbourhood (the W1 repair of `old-depth-gate.md` is included) bounds D^2 F_R[u, e_c] by (K/r) e^{-2 gamma d(x,c)}. For c in C, e^{-2 gamma d} <= e^{-gamma D} e^{-gamma d}, which gives K e^{-gamma D}(b_x + a B_x / r). Correct.
- **Node paragraph and (4.6).**
  - The pillar sum is sum_q xi_q / xi_n <= (1 - L^{-1})^{-1}.
  - The ordered-product derivative is correct, and the current commutator is the one in (3.1).
  - The caveat "both sides identified with this same F_R" is right and necessary.
- **(4.7).** sum_{q<j} xi_q <= xi_j/(L-1) and sum_{q<j} xi_{q+1} <= L xi_j/(L-1). Correct.
- **(4.8).** The density of d is >= 1/xi_j, so a member at depth d_0 M xi_k has D >= d_0 M/sigma_j - (rho + L M_frak)/(L-1) - b_*. Choosing M after the fixed sizes gives e^{-cM/sigma_j}. This is an old-to-old implication.

## 5. Section 6: (6.1)-(6.2)

- At theta = 1 only C = Q survives, and F = f_Lambda.
- With theta = 0 off Y, every term with C not inside Y vanishes. For C inside Y, f_{B u C} reads only Y, given the stated premises.
- Let K_2 be an active component separated from B u K_1. Then f_{B u C} = f_{B u (C n K_1)}, so the K_2 sum factors as prod(theta + 1 - theta) = 1, and every theta-derivative on K_2 vanishes. Equivalently, the Mobius coefficients g_C = sum_{C' in C} (-1)^{|C \ C'|} f_{B u C'} vanish unless B u C is connected.
- With theta = s, splitting of the step response (Theorem B(d)) keeps both properties.
- Finite FTC gives sum_K F[K|B] = F(1) = f_Lambda.
- (6.2) follows from |s| + |1 - s| <= 1 + 2R. It is volume-uniform only for real s in [0, 1].

The note's statement that a uniform bound on the connected coefficients g_C is the open part is accurate.

## 6. For the lead: a route the note does not list (Balaban's), unproved

The note compares the box pair with a global object, either the assigned pair q or Pi_j(V), and every removed-background difficulty comes from that comparison. Balaban does not make it. CMP 109 (3.18) writes the old activity for X inside box_2 through the local background U_j(box_0), and (3.21) removes only the shift outside box_3. In SA terms (call it BF, box first):

- **Construction.** For a small member X at base z (X inside box^{~2}, inside R_z), use WF4's box map at every t, for every window cutoff zeta' of the partition:
  Phi(s,t,nu) = G~(X, P^box_z(M^j(e^{i eta_k (t + nu zeta') H_k(s;P,B')} U_+(P))|_{R_z})),
  with H_k the decoupled response of Definition D.
- **Physical identity.** At complete physical pairs with s = 1, V(0) and V(1) are critical for the step's two ambient sequences (depths k and k+1). In a constant top layer containing R_z, the box tower with its level-zero boundary rows lies memberwise in both, after truncation at the old depth j. So Lemma CR, or SA's own Theorem 6(b) (SA 9776-9780: U_{B'}(M_{B'}(U_B(V)|_{Omega'_0})) = U_B(V)|_{Omega'_0} for Omega'_q inside Omega_q), gives P^box_z(V(i)) = P_i on R_z, up to gauge, and G(X, P_1) - G(X, P_0) = sum over windows of the integral of d_nu Phi dt. Windows with zeta' = 0 on R_z contribute exactly zero.
- **The terms.**
  - Grouped windows give WF13a unchanged, with WF8-WF10.
  - Non-grouped windows that meet R_z give terms whose datum change lies at current distance >= c M from z. A small X gets the box map's own T4 decay e^{-cM/sigma_j}. This is (4.4)-(4.5) with beta = 0 and a single map, so no two-map comparison and no node identification is needed. A larger X gets the decay from its own kappa_far share, as in SA's long-domain tails. WF11-WF12 then apply verbatim.
  - There is no background-removed origin at all. So Section 2's bulk defect never enters, and neither does (5.1)'s nonlocality.
  - The nu-derivative is linear in the cutoff, so the non-grouped windows sum to a single term per base, with cutoff 1 - zeta_grouped on R_z. This is Balaban's (3.21) second term, the part outside box_3.
- **Heredity.** Every term reads V only on R_z. U_+(P) is local, and the Definition-D response is hereditary. In Section 5's test, U_eps = U_0 on R_z, so the two completions give the same function.
- **Admissibility.** SA asserts the window identity only at complete physical pairs, and lets the local formulas define the extension (SA 15840-15846). So BF is a specification change of the same kind as (7.14). It agrees with Balaban's own construction (CMP 109 (3.18)-(3.25), (3.38)).
- **First place it could die.** The physical identity at a seam. If R_z is not in a constant top layer, the box tower need not lie in the ambient sequences. SA Theorem 6(c) then gives only an exponentially small endpoint mismatch, not an identity. The meet map restores the identity, but it must then be identified with WF4 for WF8's cancellation. This is the same open requirement the note records for route (a).
- **Second point to check.** Use Definition D's response inside the box datum, not a separately built box response. A box response would bring back a response-removed origin, and its same-depth comparison gives only e^{-cM} ((7.13)), which WF12 cannot absorb.

None of this is proved here. If BF holds, row 148's uniform localization of a global projection is not needed in constant-top windows, and rank 4's WF7 reduces to the seam identification and single-map decay. I suggest the lead weigh BF before row 148 starts.

## Defects (none breaks a consumer)

1. **W1, (4.1).** State the counting premise rho >= 32 log L / theta (from `a1-balaban.md` (3.13) with 2 gamma <= theta). It holds once rho is chosen after L and theta, as in `wf-room-2.md` Theorem L.
2. **W2, inputs and status.** Row 136 is now done (first failing step none), so `removed-fix.md`'s repaired theorems are checked inputs, not pending ones. Result item 3 should list the two further inputs Section 5.3 uses: `old-depth.md` Section 4 (the family) and `h-walk.md` Section 7 (H_1(s) at J = 0).
3. **W3, Section 6.** Name the adjacency in "component of A containing B". Face-sharing matches SA's wall-components and Lemma WC. Also fix the reading of "step response restricted to that component": Definition D with s = 0 off the component. Either reading leaves the finite identity intact.

Strengthening, not a defect: Section 5's obstruction does not depend on the choice U_+(P) = e^{i eta A'}U. Any choice in which P reaches Pi_j through a global map, with s entering only through H_k, gives the same nonzero coefficient tr(A_b C_b).

## Result

**Checked line by line by Claude, first failing step none** in `library/wf7-extension.md`. The note was proved by Codex and is not human-reviewed.

- **ADVANCE.**
  - Section 5's counterexample: (5.1) fails exact hereditary restriction, at an admissible window and member (5.10), and the failure survives the nu anchor, the t-integral and any fixed collar.
  - The explicit Green's function (5.5)-(5.6), redone by hand. An exact-arithmetic run agreed, as a guide only.
  - The Section 2 consumer quotients, as a failed inference for the printed WF11-WF15 argument.
  - (3.2) and the restriction lemma.
  - (4.4), (4.5), the node comparison and (4.8), as implications from T4, AX, AV, MS and PW.
  - (6.1)-(6.2), as finite algebra.
- **Open, as the note says.**
  - A volume-uniform complex bound for any localization of a global old projection (row 148).
  - The seam identification of the old meet with WF4.
- **New, unproved.** Balaban's box-first construction (Section 6) avoids both obstructions in constant-top windows. Its first possible failure is the endpoint identity at seams.
