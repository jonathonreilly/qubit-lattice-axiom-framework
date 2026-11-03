lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T23:50Z

# Check of `library/wf7-extension.md` (queue row 147)

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, commit 072138cc3 of `claude/ym4d-hard-route`. One reading by one other model. Not an audit and not a human review. The note is by Codex (row 145). SA line numbers refer to `YM4_sketch_500.tex` at `31a47c543775`, fetched once into a scratch folder (sha256 d7f77d4d...). Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for WF3-WF15, OA7-OA8, R8-R9 and the window construction; Tadeusz Balaban for composition and restriction at a critical background's own averages (CMP 109 pp. 275-276, CMP 119 p. 276, both re-read here from `~/ym4d-papers`).

Status: in progress. Sections are written as they are checked.

## Verdicts

**First failing step: none so far** (Sections 2, 3 and 5 done; 4 and 6 in progress).

| Statement | Verdict |
|---|---|
| Section 5, (5.1)-(5.12): projection-first extension (5.1) fails exact hereditary restriction | **ADVANCE.** Checked line by line by Claude, first failing step none. The test is admissible. The failure survives the nu anchor and the t-integral, and it survives any fixed collar (OA8 allows one). |
| (5.2)-(5.6), the explicit old Green's function | ADVANCE, every identity redone by hand |
| Section 2, (2.1)-(2.2) | CORRECT-NO-ADVANCE. This restates `old-depth.md`, checked in row 141. |
| Section 2, (2.3)-(2.4) and the consumer quotient | ADVANCE as stated. This is a failed inference: the printed argument WF11-WF12/WF14-WF15 cannot carry a bulk term of per-base size delta_k sigma_j^3. It is not a counterexample to an improved route (b), and the note says so. |
| Section 3, restriction lemma, (3.1), (3.2) | ADVANCE. The lemma is Lemma CR again (checked row 141). (3.1) is the product rule. (3.2) is the fundamental theorem at physical endpoints. |

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

- **The input pair.** By R8 (SA 5747-5759), P = (U, A', J) and the shifted configuration is e^{i eta H} e^{i eta A'} U. So U_+(P) = e^{i eta A'}U is the direct choice, and (5.1) is exactly `old-depth.md` (7.14) with this choice. P_eps = (1, eps a, 0), where a is the step potential on block 0. At a fixed mesh, its plaquette angles are O(eta eps) and its gradient is O(eps/eta). So for eps small at that mesh, it meets the core clauses of SA 15880-15890 and the tower clauses. An exact identity needs no mesh-uniform amplitude. Admissible.
- **The step response.** SA 5770-5795 requires R9 to vanish at B' = 0 and to split over wall-components when s vanishes on separating cubes. `o1-decoupled.md` Theorem B(d) proves this splitting for Definition D. At J = 0 every branch coefficient j_beta of `h-walk.md` Section 7 vanishes, so H_1(s) has the W-system expansion. Admissible.
- **The member (5.10).** It is polynomial in J, invariant under conjugation, carries no stored colour spectator, and vanishes at the vacuum. These are exactly the hypotheses of the vacuum-only argument (SA 13859-13880 Proposition PW19, and SA 16056-16067). The window machinery has to file every such member, so a single one suffices. Admissible.
- **The grid.** All parameters are 0 or 1, inside |s| < e^{kappa-bar}. A full slab of zero cubes leaves at least three cubes per direction, as Lemma WC needs, and hypothesis (P) holds for a grid of large side. The perturbation of P is strictly inside the slab. Admissible.
- **Order of choices.** Fix L, then M, then k so that (5.8) < sigma_1^3/4. At that k, choose D so that (5.9) < sigma_1^3/4. Then choose the torus (n even, a multiple of the periods, with n >= 2D + slab width, so the slab is at distance >= D from R_z on both sides). Finally choose eps, a and nu small. Nothing chosen earlier depends on anything chosen later. Correct.
- **The old-unit current at z.** D(J o Pi_1)(1)h = L h follows because h is the depth-k flat lift, critical for a sequence containing the depth-1 truncation (Lemma CR, linearized). Then (Lh)_2 = -(q_{m+1} - q_m)T depends only on x_1, so the forward and the backward direction-2 bonds at z see the same value. Remark: the note's "nearby tests in the same constant-current part" is stronger than needed.

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

**Literature.** The note says Balaban localizes after composing. This is confirmed. CMP 109 p. 275, (3.24)-(3.25), evaluates the old background on a fixed domain, U_j(box_0, ...), with U_{k+1} replaced by U_{k+1}(box_0, M'(U)) extended by U outside box_0. P. 276 defers "a final localization". CMP 119 p. 276 says: "After the completion of the operations of Sects. 3-5 [I] we localize the obtained expressions", using random-walk expansions for the sequence {Omega_j}. So the published construction is local from the start and is then resummed. It is not a global projection with parameters only in the step response. This supports the note's N7 and Section 6, and it is the template for row 148.
