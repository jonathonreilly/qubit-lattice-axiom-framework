lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T07:13Z

# UM1 for the actual intrinsic action (queue row 178)

Proved by Claude, not yet checked by the other model. Research-stage working state; no status.

Commit read: 9a35fdcba. All sections written.

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
- *The intrinsic potential.* P^{G,A}(P; y) := T_3[S_P(1; .) + G_P](y). At a complete physical pair this is SA 7604's remainder sum_b O(g|B|^3). The constant term is x A(U_{k+1}). The linear term vanishes, since the current is the image of a multiplier (SA 7866). The quadratic term is SA's Gaussian form, built from A = C_V^T (G^(2)_V + Delta_k) C_V (SA 10200-10212), with the factor x/t that SA keeps separate (SA 7864). The pivot and Haar logarithms (SA 7479-7487) are not in P^{G,A}; Remark 8.2 treats them.

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

## 4. Two lemmas on the decoupled response

**Lemma P (plaquette shift).** Let P be in D, s in D_R and ||u||_inf < r_R. Then for every bare plaquette p,

  ||dU(P; s; u)(p) - dU_+(p)|| <= C_1 eta^2 ||u||_inf,   C_1 = C_pl B C_B',   (4.1)

where C_pl depends only on the core conditioning.

*Proof.* Put h = H(P; s, u). By [R9], ||h||_{X,1} <= 2B C_B' ||u||_inf =: e <= 2c B^{-3}, which is small. With xi = 1 the X-norm gives |h(b)| <= e and |nabla_U h| <= e at every bond. Let p have links W_i = e^{i eta h_i} U_i, so that dU(p) = W_1 W_2 W_3^{-1} W_4^{-1}. Move each exponential to the left through the U_+ factors. This gives dU(p) = e^{i eta h_1} e^{i eta h_2'} e^{-i eta h_3'} e^{-i eta h_4'} dU_+(p), with h_2' = Ad(U_1) h_2, h_3' = Ad(dU_+(p) U_4) h_3 and h_4' = Ad(dU_+(p)) h_4. Hence h_2' - h_4' = eta nabla_mu h_nu - (Ad dU_+(p) - 1) h_4. Also h_3' - h_1 = eta nabla_nu h_mu + (Ad dU_+(p) - 1) Ad(U_4) h_3. Here nabla is the covariant difference quotient of SA 10252. So c_p := h_1 + h_2' - h_3' - h_4' obeys |c_p| <= 2 eta e + C alpha eta^2 e. The second-order BCH remainder of the four factors is at most C eta^2 e^2, using ||Ad T|| <= 2 for the partial products at the core. So ||dU(p) dU_+(p)^{-1} - 1|| <= C eta^2 e, and ||dU_+(p)|| <= 2 gives (4.1). QED

**Lemma S (splitting and heredity of the R9 response).** Let s be in D_R and N = {Delta : s_Delta = 0}. Let W be a wall-component of P_f \ N, and let I_W be the bare bonds whose base point lies in a cube of W and in no closed cube of N. Then:

- (i) H(P; s, u)(b) = 0 for every bond b based in a closed cube of N;
- (ii) for b in I_W, H(P; s, u)(b) = H(P; s 1_W, u)(b). This value depends on (P, u) only through their restrictions to the union of W.

*Proof.* **Step 0 (one tagged term).** Let T(s) be H(s), H_1(s), G(s), M_s or a transpose of one of these, and let T(s)(b, c) != 0 with b in I_W. The tag of the term is nonzero, so its tag set meets no cube of N. The tag set is connected and contains the cube of b. By Lemma WC, every cube that meets it lies in W. Three things follow. The monomial depends on s only through s|_W, so the term is unchanged at s 1_W. Its coefficient reads the pair only in the union of W, by [D]. By [S-loc], the r_loc-neighbourhood of c lies in cubes of W and meets no cube of N. If instead b is based in a closed cube of N, then T(s)(b, .) = 0 by (d) of Theorem B. This holds for all four operators, by [D].

**Step 1 (one Picard step).** As in `gates/dec-field-gate.md` 4.1, R9 is the pair of contractions a = Phi_s(a) := H_1(s) B'(u) - G(s) W_s(a) and h = Phi'_s(h) := a - H(s) C(h), with H = h. Here W_s = W_s^red is (4.4) of `nl-r9.md`. It contains the inner solution z_s(a) of z = a - H(s) C(z), which is the same equation as d = C(a - H(s) d) with z = a - H(s) d. Each term of Phi_s and Phi'_s is a tagged operator applied to a finite chain of local maps and tagged operators. The inverses inside (4.3)-(4.4) of `nl-r9.md` are Neumann series of such chains, which converge by [NL]. Apply Step 0 along a chain, starting from its output end. The first operator puts its input point c, with its r_loc-neighbourhood, inside W and away from N. The local map at c then reads only at points of cubes of W. The next tagged operator has its output there, so Step 0 applies to it again. By induction along the chain, every read lies in the union of W. Hence, for b in I_W, Phi_s(a)(b) depends on (a, P, u) only through a|_{I_W} and (P, u) restricted to the union of W, and it equals Phi_{s 1_W}(a)(b). The same holds for Phi'_s. For z_s(a), apply the same induction to its own Picard iterates z_{m+1} = a - H(s) C(z_m) and pass to the limit. If b is based in a closed cube of N, then Phi_s(a)(b) = 0 and Phi'_s(h)(b) = a(b).

**Step 2 (iterates).** The solution of Proposition 5.1 is the limit, in the X-norm and hence bond by bond, of the Picard iterates from zero: first a_{n+1} = Phi_s(a_n), then h_{m+1} = Phi'_s(h_m) with a = lim a_n. The iterates stay in the balls of Proposition 5.1. By induction on n, using Step 1, two things hold. First, a_n(b) = 0 when b is based in a cube of N. Second, for b in I_W, a_n(b) equals the n-th iterate at s 1_W and depends on (P, u) only through the union of W. Limits keep both properties. The same induction applies to h_m. This proves (i) and (ii). QED

**Corollary R (rooting and heredity of one bracket).** Let Y be a finite set of fine cubes that contains X_0(p). Fix s = 1 on X_0(p) and s = 0 off Y. Let W_0 be the wall-component of Y that contains X_0(p).

- (a) Psi_p(s; y) depends on s only through s|_{W_0}, and on (P, y) only through their restrictions to the union of W_0. Hence v_p(Y) = 0 when Y is not face-connected.
- (b) Given [RT], v_p(Y) is the same function on every local domain that contains Y.

*Proof.* The bonds of p have base points at corners of p. Every cube that contains a corner of p meets p, so it lies in X_0(p). Hence these bonds lie in I_{W(s)}, where W(s) is the component of X_0(p) for the given s. Any zero of s inside K only shrinks W(s) inside W_0. So Lemma S(ii) gives Psi_p(s) = Psi_p(s 1_{W(s)}), and the stated dependence on (P, y), since y enters only through u = g y. Suppose Y has a second component W_1. Then Psi_p(s) = Psi_p(s 1_{Y \ W_1}) for every s in the bracket domain. So the derivative in s_Delta vanishes for Delta in W_1, and the bracket is zero. For (b): every tagged term that survives has its full field hull in the union of W_0. By [RT] its value is the same for every problem whose region geometry agrees there. The local maps are the same. So the Picard iterates agree on I_{W_0}, and the limits agree. QED

## 5. The cubic remainder of one anchor

**Lemma T.** Let Y_0 be a 2x2 complex matrix with ||Y_0|| <= A. Let Z be holomorphic on |nu| < r_1, with Z(0) = 0, ||Z(nu)|| <= B|nu| and r_1 >= 4. Put f(nu) = (1/2) det(Y_0 + Z(nu)) = sum_n f_n nu^n. Then

  sum_{n >= 3} |f_n| <= 8AB r_1^{-2} + 2B^2 r_1^{-1},   and   |sum_{n >= 3} f_n mu^n| <= mu^2 (8AB r_1^{-2} + 2B^2 r_1^{-1})  for 0 <= mu <= 1.   (5.1)

*Proof.* For 2x2 matrices, det(X + Z) = det X + tr(adj(X) Z) + det Z. Here adj X has the singular values of X in reverse order, and |tr W| <= 2||W||. So g(nu) := tr(adj(Y_0) Z(nu)) obeys |g| <= 2AB|nu|, and k(nu) := det Z(nu) obeys |k| <= B^2 |nu|^2. Cauchy on |nu| = r := r_1/2 >= 2 gives |g_n| <= 2AB r^{1-n} and |k_n| <= B^2 r^{2-n}. Sum over n >= 3, using sum_{n>=3} r^{1-n} <= 2r^{-2} and sum_{n>=3} r^{2-n} <= 2r^{-1}. Then sum_{n>=3} |f_n| <= 2AB r^{-2} + B^2 r^{-1}, which is (5.1). The second bound uses mu^n <= mu^2 for n >= 3. QED

**Application to the anchors.** Fix s in the bracket domain of Section 2, with complex s_Delta allowed, s = 1 on X_0(p) and s = 0 off Y. Fix P in D and y in the box. Put mu = max over bonds b in Y of |y(b)| / b_*, and assume mu > 0. By Corollary R(a), Psi_p reads y only on the union of Y. So we may set y_hat = y/mu on Y and y_hat = 0 elsewhere; then ||g nu y_hat||_inf <= |nu| delta.

- *Action anchor.* f(nu) = a_p(U(P; s; g nu y_hat)) = (1/2) det(Y_0 + Z(nu)), with Y_0 = dU_+(p) - 1 and Z(nu) = dU(P; s; g nu y_hat)(p) - dU_+(p). [Core] gives A = C_0 alpha eta^2. Lemma P gives B = C_1 delta eta^2 on |nu| < r_1 = r_R/delta. Then Psi_p(s; y) = x(p) sum_{n>=3} f_n mu^n. Use alpha <= r_R, |x(p)| <= (1+c) g^{-2} and mu^2 <= b_*^{-2} sum_{b in Y} |y(b)|^2 = g^2 delta^{-2} sum_{b in Y} |y(b)|^2. Then

  |Psi_p(s; y)| <= A_p delta eta^4 sum_{b in Y} |y(b)|^2,   A_p = (1+c)(8 C_0 C_1 + 2 C_1^2)/r_R.   (5.2)

- *Gauge anchor.* f(nu) = gf_(y,x)(V_k(g nu y_hat)) = (1/2) det Z(nu) with Z(nu) = V(y,x)(g nu y_hat) - 1. Here Y_0 = 0, because the background means are 1 on P'' ([Core]). By [QC], B = C_G delta on |nu| < r_1 = r_G/delta. With |w_G| <= (1+c) g^{-2},

  |w_G T_3[gf_(y,x)(V_k(g .))](y)| <= A_G delta sum_{b in Y_G(y,x)} |y(b)|^2,   A_G = 2(1+c) C_G^2 / r_G.   (5.3)

Both need delta <= min{r_R, r_G}/4, so that r_1 >= 4. This holds for t large, since delta(t) -> 0 and r_R, r_G are fixed earlier.

There is no factor 1/alpha in (5.2). The core radius alpha enters only through the cross term A, and the Cauchy radius r_R/delta of the response does not shrink with alpha. A cruder Cauchy radius alpha/delta, as in SA (SI12), would give delta/alpha. That would also suffice, since alpha is fixed before t.

## 6. Proof of Theorem U

**(E).** Let Q = P_f \ X_0(p) and F(s_Q) = Psi_p(s_Q + 1_{X_0(p)}). F is holomorphic on D_R, which contains [0,1]^{P_f}. Induction on |Q|, using F(.., 1) = F(.., 0) + int_0^1 dF/ds, gives the finite identity

  F(1_Q) = sum over K in Q of int_{[0,1]^K} prod_{Delta in K} d/ds_Delta F(s_K, 0) ds_K.

The term for K is v_p(K u X_0(p)). So sum over Y containing X_0(p) of v_p(Y) = Psi_p(1). Now sum over the finitely many p, and add the gauge anchors. Since T_3 is linear, sum_Y V^{G,A}(Y) = T_3[S_P(1; .) + G_P]. At a complete physical pair, [ID] identifies S_P(1; .) with x A(U_k(V_k(g .))). So the sum is P^{G,A}.

**(L).** For V^A this is Corollary R. For V^G, the read set of a gauge anchor has diameter at most C_L < M by [QC]. So it meets at most two cubes per coordinate direction. Y_G(y,x) is then a face-connected block of at most 16 cubes, and the anchor reads only its union.

**(H).** Psi_p is a composition of holomorphic maps: the R9 response ([R9]), exp, matrix products and det. T_3 is a Cauchy integral in nu. The s-derivatives in a bracket are Cauchy integrals with locally uniform bounds, so their integral over the compact cube [0,1]^K is holomorphic in (P, y, x). For the O(tau^3) claim, Psi_p(s; tau y) = sum_{n>=3} f_n(s, y) tau^n, and brackets keep this.

**(B).** In a bracket, take each Cauchy circle about s_Delta in [0,1] with radius rho = e^{kappa-bar - 1}. Then |s_Delta| <= 1 + rho < e^{kappa-bar} = R for kappa-bar >= 1, so the circles lie in D_R. On that polydisc, s = 0 off Y and s = 1 on X_0(p) still hold, so (5.2) applies. Each coordinate is differentiated once, so there is no factorial:

  |v_p(Y)| <= e^{-(kappa-bar - 1)|K|} A_p delta eta^4 sum_{b in Y} |y(b)|^2,   |K| >= |Y| - 16.

At most 6 (M/eta)^4 |Y| bare plaquettes p have X_0(p) in Y: each p is fixed by its base site and its orientation. Hence

  |V^A(Y)| <= 6 A_p M^4 e^{16(kappa-bar - 1)} |Y| e^{-(kappa-bar - 1)|Y|} delta sum_{b in Y} |y(b)|^2.

A face-connected Y has d_f(Y) <= |Y| - 1, by a spanning tree of face-adjacent cube centres. Then |Y| e^{-(kappa-bar - 1)|Y|} = |Y| e^{-|Y|} e^{-(kappa-bar - 2)|Y|} <= e^{-1} e^{-lambda_V (d_f(Y) + 1)} <= e^{-lambda_V d_f(Y)}, with lambda_V = kappa-bar - 2. Also sum_{b in Y} |y(b)|^2 = M^4 (M^{-4} sum_{b in Y} |y(b)|^2). So

  |V^A(Y)| <= a^A e^{-lambda_V d_f(Y)} M^{-4} sum_{b in Y} |y(b)|^2,   a^A = 6 A_p M^8 e^{16(kappa-bar - 1)} delta.   (6.1)

For the gauge part, at most 16 M^4 pairs (y,x) have read sets that meet a given cube, when 2 C_L + 2L <= M: such pairs have block bases in a box of side M + 2C_L + 2L, and each block has fewer than L^4 pairs. Also |Y_G| <= 16 and d_f(Y_G) <= 15. So by (5.3),

  |V^G(Y)| <= a^G e^{-lambda_V d_f(Y)} M^{-4} sum_{b in Y} |y(b)|^2,   a^G = 16 A_G M^8 e^{15 lambda_V} delta.   (6.2)

Adding (6.1) and (6.2) gives (B) with

  K_GA = 6 A_p M^8 e^{16(kappa-bar - 1)} + 16 A_G M^8 e^{15(kappa-bar - 2)}.   (6.3)

K_GA depends on c, L, M, kappa-bar, C_0 and the R9 and chart constants (B, C_B', C_1, C_G, r_R, r_G). It does not depend on t, depth, volume or the number of labels.

**Scope of (B).** The same proof gives (B) on any enlarged box {|y(b)| < k_1 b_*}, with delta replaced by k_1 delta, whenever k_1 delta <= min{r_R, r_G}/4. In (UM3)-(UM4) the coarse Gaussian parameters enter only J, so V^{G,A}(Y) does not depend on them. It is therefore holomorphic and bounded on those enlarged discs as well. QED

## 7. The rate, UM19 and the order of constants

**(R).** If (B) holds at rate lambda_V, it holds with the same a_GA at every rate lambda <= lambda_V. UM19 asks lambda - lambda_0 >= Theta/L + sigma_0. `um-envelope.md` Section 5 chooses one common rate lambda strictly inside its window (8), lambda_0 + sigma_0 + Theta/L < lambda < kappa/(2 C_h^WF) - eps_rate. That choice comes before kappa-bar. So the intrinsic type meets UM1 at the common rate if and only if kappa-bar >= lambda + 2. Theta = t_0 + t_1 kappa is fixed before kappa-bar, so this floor does not feed back.

**Order of choice.** Each line uses only earlier lines.

1. L; then the constants of [D] (a_*, tau_L, B_L, C_W, nu_1, N_L).
2. M_1 >= M_W(L), and 31 M_1 >= C_L for [S-loc].
3. kappa and lambda, by `um-envelope.md` (8).
4. kappa-bar >= max{the row 9 floors, Theta + 1, lambda + 2}.
5. l_P >= max{8 r_1 + 1, 256 kappa-bar/tau_L} ([D]).
6. M: M >= l_P xi_max / 2, M >= 2 C_L + 2L, `um-envelope.md` (9), and the other existing floors.
7. The radii: alpha <= r_R, and the core and current radii of `um-envelope.md`.
8. Last, t: delta(t) <= min{r_R, r_G}/4, and K_GA delta(t) at most the intrinsic share of a_* in UM23.

K_GA in (6.3) depends only on lines 1-7. So the order closes.

## 8. Scope, a remark, and what stays open

**8.1 Scope.** The step region is single-scale, as in the UM chapter. The expansion is the node-free interior: gauge anchors on the blocks P'', and the action on the whole region. The node and seam terms, with their constant and linear parts, stay in the boundary exponent (SA 7601). They are not treated here. Layered regions are also not treated. There, (5.2) for a bare plaquette in a layer of scale xi < 1 carries xi^{-4} from Lemma P, and the weighted decay of R9 in d_B units must pay for it. This is SA's "every layer is measured in its own scale"; I did not write it.

**8.2 Remark: pivot and Haar logarithms (SA 7479-7487).** These pieces of P^(k) are not in P^{G,A}. They are strictly local by (QC25). The pivot term is the sum over c of log det(1 + E_c(u)), with ||E_c(u)|| <= C L^9 ||u||_inf by (QC23) and ||C_V|| <= C L^4. The Haar term is the sum over b of log(sigma(a_b(u))/sigma_0), and |log(sigma(a)/sigma_0)| <= |a|^2 for small |a|. File each term on the cubes that meet its read set, and count as for (6.2), using g|y| <= g(1 + |y|^2). This gives SA (UM1) for them, with amplitude at most C L^9 M^4 e^{15 lambda} g. That is of order g, far below delta. Proved here from SA's (QC23)-(QC25), which the ledger lists as unchecked. They vanish at u = 0, but they are not cubic.

**8.3 Kill attempts and cruxes.** Three known failure modes were checked against this proof.

- `gates/dec-field-gate.md` 4.1(iii): Proposition 5.1 does not deliver R9's splitting. Lemma S supplies it, by Picard induction. It does not use uniqueness under restriction, which would meet a gradient-norm problem at cut edges.
- Lemma 2.1 of `joint-loc.md`: uniform holomorphy with one boundary comparison does not bound rooted brackets. Here the bound is holomorphy on the full polydisc in every fine-cube parameter, which gives (R-1)^{-|K|} directly, as in (5.5) of `joint-loc.md`.
- The 1/alpha loss of a naive Cauchy radius: the det split in Lemma T avoids it.

None of these breaks Theorem U.

**8.4 What this changes.**

- (8) of `b4-step.md` holds as an implication. With it, the first reduction of `b4-step.md` (the coupling disc UM12-UM13) has its input for the intrinsic type. Heredity and rooting for this type are now supplied.
- B1 still reads (6), which is `um-envelope.md` (7) with the adopted inverse-root series. B1 also reads the remaining structural identities of UM (the normalized functional and wall factorization). This note does not check them.
- B4 and 1.6 still need: all potential types at one common rate; the finer derivatives of SA 4021-4037; layered regions; and seams.

**First input that fails:** none in this derivation. These inputs are not checked by the other model, or not checked anywhere:

- Lemma S, Corollary R, Lemmas P and T and Theorem U: proved by Claude, not yet checked.
- [QC]: SA (QC23)-(QC25), listed as unchecked in the ledger.
- The source map u -> B'(u) inside [ID]: read in SA, not rebuilt.
- The read radii C_L in [S-loc]: not computed. The fallback (a wider tag collar) removes the need.

No numeric job was run, and no step rests on a computation.

## Result

**Proved by Claude, not yet checked by the other model: Theorem U, the outline's UM1 for the actual intrinsic action/gauge potential, as an implication.** The family V^{G,A}(Y) has these properties:

- It is exact at complete physical pairs.
- It is face-connected and rooted, with read support in Y, and hereditary.
- It is holomorphic on the complex fluctuation box and the external cores.
- It obeys |V^{G,A}(Y)| <= K_GA delta(t) e^{-(kappa-bar - 2) d_f(Y)} M^{-4} sum_{b in Y} |y(b)|^2, uniformly in depth and volume.

It meets UM19 at the common UM rate once kappa-bar >= lambda + 2, inside the order of `um-envelope.md`.

The new step is Lemma S: R9's response splits over wall-components and is hereditary. `gates/dec-field-gate.md` records that this was not delivered.

Section 1: Codex's Gaussian comparison (7) in `b4-step.md` Section 5 is ADVANCE, checked line by line by Claude, first failing step none.

Open: the inputs listed in 8.4; (6) for B1; and the rest of B4 and 1.6.
