lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T07:13Z

# UM1 for the actual intrinsic action (queue row 178)

Proved by Claude, not yet checked by the other model. Research-stage working state; no status.

Commit read: 9a35fdcba. Work in progress; sections are written as they close.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the UM chapter (SA 14280-14800), the local Gaussian comparison (SA 13893-14090) and the step anatomy (SA 7590-7640). Tadeusz Balaban for the background-field and localisation constructions (CMP 95-122). SA means `YM4_sketch_500.tex` at `31a47c543775`, fetched once to a scratch folder.

## 1. Check of `b4-step.md` Section 5, the Gaussian comparison (7) (Codex)

Provenance: Claude Opus 5.5, effort max, commit 9a35fdcba. One line-by-line reading by the other model. Not an audit.

**Verdict: ADVANCE, as an implication from (6).** Checked line by line by Claude, first failing step none. It agrees with SA (FG1)-(FG12).

The steps, each redone:

- **D_0.** D_0 >= C_0 >= ||C_0^{-1}||^{-1} >= K_G^{-1}, since C_0 Gamma_0 Gamma_0^T C_0 >= 0. Also ||D_0|| <= K_G + K_G^2 K_G^2. Correct.
- **D - D_0.** Telescoping the three factors of C Gamma Gamma^T C gives ||D - D_0|| <= eps_G + 4(K_G + eps_G)^3 eps_G. Bilinear transposes keep operator norms. Correct.
- **Re D^{-1}.** For a complex symmetric S, the entrywise real part is the Hermitian part. If ||D - D_0|| <= 1/(2K_G), then ||D^{-1}|| <= 2K_G and ||D^{-1} - D_0^{-1}|| <= 2K_G^2 ||D - D_0||. So Re D^{-1} >= (K_G + K_G^4)^{-1} - C(K_G) eps_G. Correct.
- **Q_0.** Expanding (b - C_0 Gamma_0 xi)^T C_0^{-1} (b - C_0 Gamma_0 xi) + |xi|^2 gives b^T C_0^{-1} b - 2 b^T Gamma_0 xi + xi^T (I + Gamma_0^T C_0 Gamma_0) xi, the form of Q_0. The shear L_0 and its inverse have norm <= 1 + K_G^2. So Q_0 >= min(1, K_G^{-1}) (1 + K_G^2)^{-2}. Then ||Q - Q_0|| <= C(K_G) eps_G needs ||C^{-1} - C_0^{-1}|| <= 2 K_G^2 eps_G, which is the resolvent identity. No dimension enters. Correct.
- **Marginal.** The Schur complement is C^{-1} - Gamma (I + Gamma^T C Gamma)^{-1} Gamma^T. Woodbury with U = C Gamma, V = Gamma^T C gives D^{-1}. Here I + Gamma^T C Gamma = Q_xixi has positive real part, so it is invertible. det Q = det C^{-1} (eliminate the b block) and det Q = det Q_xixi det D^{-1} (eliminate xi). So det D = det C det(I + Gamma^T C Gamma). Correct.
- **Branch.** The identities hold at real symmetric data by real Gaussian integration. Real symmetric C and real Gamma form a totally real set of full dimension, so one-variable identity theorems extend them. Determinants do not vanish on the convex ball, so the root continues from the positive reference root. Correct.
- **(7).** |J[F]| <= F_* |det D|^{-1/2} det(Re D^{-1} - 2 rho)^{-1/2}. Write D = D_0(I + E_2) and Re D^{-1} - 2 rho = D_0^{-1}(I + E_1). Then ||E_2|| <= C eps_G and ||E_1|| <= C(eps_G + rho). With |tr E^n| <= m ||E||^n, each factor is at most (1 - ||E||)^{-m/2} <= e^{m ||E||} for ||E|| <= 1/2. This gives F_* e^{A_K(eps_G + rho) m}. Only m enters. Correct.
- **Failed cutoffs.** On the failed set, sum over P_0 of |b_beta|^2 >= v b^2. The blocks are disjoint, so |b|^2 is at least that sum. Hence the indicator is at most e^{(gamma/2)(|b|^2 - v b^2)}, and (7) at rho + gamma/2 gives the tail. Correct.

**Scope.** This is (7) given (6). Input (6) is `um-envelope.md` (7) with the adopted inverse-root series (`inv-root.md`, `carrier-adopt.md` Section 1); I did not recheck it. The tilt |b|^2 must be the Euclidean norm in the same orthonormal coordinates as D. The per-bond norm |B(b)|^2 of UM1 must be a sum of squares of those coordinates. I take that as part of the coordinate convention; no defect.

## 2. The scalar, the family, and the claim

**Setting.** Work at step k -> k+1 in level-k units: the lattice T^(k) has spacing 1 and the bare spacing is eta. The step region is single-scale (xi = 1), as in the UM chapter (SA 14290: one periodic cube lattice). Layered regions are outside this note (Section 8).

- *Free coordinates.* y(b) in C^3 on the nonpivot bonds b of the step region, u = g y, g = t^{-1/2}. The box is B_b = {|y(b)| < b_* for all b}, b_* = delta/g. So ||u||_inf < delta on the box.
- *Fibre chart* (SA (QC24)). a(u) = Psi_V(C_V u) solves the one-step constraint, is holomorphic for ||u||_inf < r_Q = c L^{-9}, and is exactly finite range. The level-k field is V_k(u) = e^{i a(u)} V.
- *Pairs.* P = (U_+, J) in the local complex core D. Core bound: ||dU_+(p) - 1|| <= C_0 alpha eta^2 at every bare plaquette p. A *complete physical pair* has U_+ = U_{k+1}(W), J = J(U_+), V = M^k U_+.
- *Fine grid.* P_f is the grid of fine cubes of side M. Parameters s = (s_Delta), Delta in P_f, on D_R = {|s_Delta| < R}, R = e^{kappa-bar}.
- *Response.* H(P; s, u) is the R9 solution (SA 10356-10404) with Definition D operators on the partition P_f and with source B'(u), the straightened-row datum change of V_k(u). Put U(P; s; u) = e^{i eta H(P; s, u)} U_+.
- *Local actions.* For SU(2) and its continuation to SL(2,C), a_p(U) = 1 - (1/2) tr dU(p) = (1/2) det(dU(p) - 1), since det X = 1 gives det(1 - X) = 2 - tr X. Likewise gf_(y,x)(V) = (1/2) det(V(y,x) - 1) for the block means on the blocks P'' (SA 7182, 7878).
- *Scalar.* With x(p) the Wilson weight and w_G the gauge weight, |x(p) - t| <= c t and |w_G - t| <= c t,

  S_P(s; y) = sum_p x(p) a_p(U(P; s; g y)),   G_P(y) = w_G sum_{(y,x), y in P''} gf_(y,x)(V_k(g y)).

- *Cubic remainder.* T_3 f(y) = f(y) - f(0) - Df(0)[y] - (1/2) D^2 f(0)[y, y]. Along a ray, T_3 f(y) = sum_{n >= 3} c_n, where f(nu y) = sum_n c_n nu^n.
- *The intrinsic potential.* P^{G,A}(P; y) := T_3[S_P(1; .) + G_P](y). At a complete physical pair this is SA 7604's remainder sum_b O(g|B|^3). The constant term is x A(U_{k+1}). The linear term vanishes, since the current is the image of a multiplier (SA 7866). The quadratic term is (1/2)<y, A y> with SA's A = C_V^T (G^(2)_V + Delta_k) C_V (SA 10200-10212). The pivot and Haar logarithms (SA 7479-7487) are not in P^{G,A}; Remark 8.2 treats them.

**The family.** For a bare plaquette p, let X_0(p) be the set of fine cubes that meet p. It has at most 16 cubes and is face-connected (proof of Lemma WC, `o1-decoupled.md`). For a finite set Y of fine cubes with Y containing X_0(p), put K = Y \ X_0(p) and

  Psi_p(s; y) = T_3[ x(p) a_p(U(P; s; g .)) ](y),
  v_p(Y; P, y) = int_{[0,1]^K} prod_{Delta in K} d/ds_Delta  Psi_p(s_K + 1_{X_0(p)}; y) ds_K,   (s = 0 off Y).

Put V^A(Y) = sum over p with X_0(p) in Y of v_p(Y). For a gauge pair (y,x), let Y_G(y,x) be the set of fine cubes meeting the read set of gf_(y,x)(V_k(g .)), and let V^G(Y) be the sum of w_G T_3[gf_(y,x)(V_k(g .))] over the pairs with Y_G(y,x) = Y. Finally V^{G,A}(Y) = V^A(Y) + V^G(Y), with the type tag "intrinsic".

**Theorem U (UM1 for the intrinsic potential).** Assume the inputs of Section 3. Then, uniformly in depth, volume and the label count:

- (E) *Exactness.* At every complete physical pair and every y in the box, sum_Y V^{G,A}(Y; P, y) = P^{G,A}(P; y). The sum is finite.
- (L) *Locality and heredity.* V^{G,A}(Y; P, y) depends on (P, y) only through their restrictions to the union of Y. It is zero unless Y is face-connected. It is the same function on every local domain that contains Y.
- (H) *Holomorphy.* It is holomorphic in (P, y, x) on D x B_b x {|x(p) - t| < ct}. Also V^{G,A}(Y; P, tau y) = O(tau^3).
- (B) *Bound.* For y in B_b,

  |V^{G,A}(Y; P, y)| <= a_GA e^{-lambda_V d_f(Y)} M^{-4} sum_{b in Y} |y(b)|^2,   lambda_V = kappa-bar - 2,   a_GA = K_GA delta,

  with K_GA of (6.3), which depends on L, M, kappa-bar and the R9 constants, and not on t, depth or volume.
- (R) *Rate.* UM19 holds for lambda_V, and for every smaller common rate lambda, once kappa-bar >= lambda + 2. This is one further floor on kappa-bar. It fits the order of `um-envelope.md` Section 5, which fixes lambda before kappa-bar.

Since a_GA e^{-lambda d_f} M^{-4} sum |y|^2 <= a_GA e^{-lambda d_f}(1 + M^{-4} sum |y|^2), (B) is SA (UM1) with a_Y <= a_GA. It is (8) of `b4-step.md`, with C_M delta replaced by K_GA delta.

## 3. Named inputs

Each input states what is used, its source and who checked it.

- **[R9]** For ||B'||_{Y,1} = b < c B^{-4}, with B = C e^{16 kappa-bar}, R9 has a unique solution in the balls of `dec-field.md` Proposition 5.1. It is jointly holomorphic in (P, s, B') on D x D_R, and ||H||_{X,1} <= 2Bb. Proposition 5.1 is an implication from [PW] and [NL] (checked by Claude, row 134). [PW] is `pw-bridge.md`, and [NL] is `nl-r9.md` under [RED], [Rows], [PW] and (O1); both were checked by Claude (row 138). *Anchoring:* H(P; s, 0) = 0, by uniqueness, since W_s^red(0) = 0 and C(0) = 0.
- **[D]** Definition D and Theorem B of `o1-decoupled.md` (checked by Codex, row 129), with the partition P_f. Hypothesis (P) holds when M >= l_P xi_max / 2. Theorem B needs l_P >= max{8 r_1 + 1, 256 kappa-bar/tau_L}, so this is a floor on M after kappa-bar. Splitting (d) is proved there for H(s). Its proof uses four facts only: each term's hull is connected; the hull contains the term's output and input; the tag runs over the cubes that meet the enlarged hull; and the coefficient reads fields only on its hull. These facts hold for H_1(s) and M_s, which are their own walk expansions with the same full-hull convention (`o1-decoupled.md` 2.1, `nl-r9.md` Section 4). They hold for G(s) by `pw-bridge.md` (7.4): there, each composite is tagged once on every cube that meets the union of its factors' full read hulls and connecting stencils, and that union is connected. So (d) holds for all four operators, with the same proof.
- **[S-loc]** Every untagged local coefficient of R9 reads its arguments and the pair within distance r_loc <= C_L of its output: C at a row, K and K^T, N_0, C', the diagonal a_0 of M_s, and the source map u -> B'(u). Every tag set contains the r_loc-neighbourhood of the term's output and input supports. Under Definition D, kappa^sharp has half-side 4 L^2 M_1 xi. This is more than 31 M_1 xi beyond the half-side of kappa^(4) when L >= 3. So [S-loc] holds once 31 M_1 >= C_L, which is a floor on M_1 after L. *Fallback:* enlarge every tag collar by r_loc. Lemma P of `o1-decoupled.md`, and with it [PW] and [NL], then hold with r_1 + r_loc in place of r_1, at the cost of a larger floor on l_P. I read [S-loc] against [Rows] ("each carrier has bounded determining diameter") and Definition D. I did not compute C_L.
- **[RT]** The walk terms read the region geometry only on their full field hull: `h-walk-fix.md` Lemma N and Theorems W', T', H' (checked by Codex, row 132). This is used only for the last clause of (L).
- **[ID]** At s = 1 and a complete physical pair, U(P; 1; u) lies in the gauge orbit of U_k(V_k(u)), the critical background of the fluctuated datum. Sources: (I-a) of `o1-decoupled.md` (checked, row 129); `nl-r9.md` Section 4, by which (4.4) is the slice gradient at physical data; A1, which is Balaban CMP 102 Theorem 1 (checked, row 81); and SA 10200-10212. a_p is gauge invariant, so the representative does not matter. This is an implication from those sources. I read the source map u -> B'(u) as SA defines it, but I did not rebuild it.
- **[QC]** SA (QC23)-(QC25): a(u) is holomorphic for ||u||_inf < r_Q = c L^{-9}, it is exactly finite range, and ||a(u)||_inf <= C L^4 ||u||_inf. The ledger lists this as unchecked (`sa-ledger.md` rows L8234, L8292). The block means of V_k(u) are holomorphic for ||u||_inf < r_G <= r_Q, with ||V(y,x) - 1|| <= C_G ||u||_inf on the blocks P''.
- **[Core]** For P in D: ||dU_+(p) - 1|| <= C_0 alpha eta^2. On the blocks P'' the background means are 1 (SA 7866). The radii are chosen after M and kappa-bar, with alpha <= r_R (`um-envelope.md` row 16).

Here r_R := min{c B^{-4}/C_B', r_Q}, where ||B'(u)||_{Y,1} <= C_B' ||u||_inf for ||u||_inf < r_Q. All constants are uniform in depth, mesh, volume and M_1 above the floors, as in [R9] and [D].
