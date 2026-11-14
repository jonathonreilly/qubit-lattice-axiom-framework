lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T00:47Z

# Row 960, `gap-vargeom-opus`: varying geometry for the seed (analysis plus GUIDE)

Started 2026-11-14T12:47Z on Mac mini worker 2, pinned at commit 2883c69d9 on branch `claude/ym4d-hard-route`.
Author: Claude Opus 5.5 at max effort. Not yet checked by the other model; the check is row 961.
Research-stage working state. Nothing here is a public claim.

Builds on: the Sussman-Alpoge complete account (CA-I, CA-II, CA-III at 31a47c543775; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text), and our notes `gap-seed-shape.md` (Theorem SH), Lemma E', Proposition B3, `gap-fc-max.md` (row 947), `gap-lsij-scale-opus.md` (row 954). Credit is repeated at each use.

Labels: PROVED (written argument, checkable by hand), CONDITIONAL (on named inputs), GUIDE (a run; it may refute or guide, it never proves), ARGUED (heuristic reasoning, not a proof), OPEN.

## Plan (at most eight steps; one step per response, appended as it finishes)

1. Read the inputs: the seed definition S(a; B), Theorem SH (`gap-seed-shape.md` 1.4-1.5), Lemma E', Proposition B3, row 947's (LSI-J-seed), row 954's Lemma GAP-R, row 706's dilute-gas sizes. Grep `open-core.md` and the FINISH rows for any lemma this row would attack (rule 0a).
2. Set up time-varying geometries exactly: maps between the slice spaces of different boxes (column insertion, restriction, extension, block averaging). State which keep positivity, gauge invariance and the periodic family. Time-symmetric shapes (grow then shrink, lens) and what reflection positivity gives.
3. Derive the best extrapolation inequality each geometry supports, from a small slice to the large box.
4. Compare with Theorem SH (ii), Lemma E' and Proposition B3: threshold and box size needed.
5. Fact tests: free photon and compact U(1); frozen Q_8 and 2T; SMALL-BOX (beta-dependent size).
6. GUIDE in a solvable model (free photon, 2D Z_N or U(1), small boxes): compare the large-box thermal sum with each small-slice quantity at matched couplings.
7. Verdict: does varying geometry buy anything over the static tools, with the reason.
8. RESULT line.

## Step log

(Each step's result is appended below as it finishes.)

### Step 1 (done 2026-11-14T13:05Z): inputs read, duplicate check (READ; no new claim)

**Repo search (rule 0a).** `grep -n -i "vargeom|varying geometry|time-varying|lens|grow then shrink|column insertion|small slice"` on `library/open-core.md`, `library/l17c.md` and FINISH.md: only rows 960-962 and two uses of "Lipschitz lens" (a domain in the complex beta plane, rows 680 and 685; unrelated). `grep -i "seed|LSI-J|extrapolat|thermal sum"` on `open-core.md` and `l17c.md`: no line about the seed. Row 962 (`gap-constraints-max`, worker 1, a brainstorm) lists constraints and ideas "in the spirit of" this row; it attacks no lemma that this row attacks. No duplicate. I proceed.

**Read at 2883c69d9.** FINISH row 960, How we work, Working efficiently, Rules; GOAL.md; `gap-seed-shape.md` in full (Lemma E2, Proposition B3, Theorem SH, the table of 1.5, Sections 3-6 and the row-707 lead note); `gap-crux-restate.md` Section 1 and Lemmas K, X, E' (3.4); `gap-transfer.md` Notation and Section 1 (the operator T_P); `gap-seed-check.md` Lemma 1.1 (every box with sides at least 3); `gap-fc-max.md` Steps 1-5.2 and 7 (Theorem BR, Lemma J, Corollary BR-J, (LSI-J-seed), 7.4); `gap-lsij-scale-opus.md` 4.2 (Lemma GAP-R); `gap-direction-max.md` lines 175-191 and 308-313 (X, Proposition HC).

**Objects used below (quoted in short).**
- B = (b_1, b_2, b_3) a periodic spatial box, sides at least 3. T_B = T_P the transfer operator of `gap-transfer.md` Section 1 on H_B = L^2(SU(2)^(E_B)), zero on non-invariant functions; positive, trace class, simple top eigenvalue lambda_0(B) with a positive invariant eigenfunction (Lemma 1.1 of `gap-seed-check.md`). Z(t, B) = Tr T_B^t is the Wilson partition function of the torus B x Z/t.
- S(t; B) = Tr T_B^t/lambda_0(B)^t - 1, g(t; B) = X(t; B) = log(1 + S(t; B)) = log Z(t, B) - t e(B), e(B) = log lambda_0(B).
- Static tools: (T) S(t + t') <= S(t) S(t'); Lemma A (a) (Tr S^(jk) <= (Tr S^k)^j); Lemma K (the deficit kappa(y) = e(y) - ell y is >= 0, convex, non-increasing); Lemma X ((y - x) kappa(y) <= g(x; y) for x < y); Lemma E' (1 + S(a; h) <= (1 + S(a; b))^(h/(b - a)), h >= b > a); Lemma E2 (deficit read at a second time t' < b); Proposition B3; Theorem SH and its table (3/10 at ratio >= 24). All PROVED and checked (rows 698, 699, 707).
- Crux (row 947, check 949): (LSI-J-seed)_a, a log-Sobolev inequality for the two-slice vacuum law J on B = (24a)^3 with alpha_J >= 2 beta K_a, K_a = (C_beta + 3 log a)/(a - 2), a even, a >= 30. Necessary (row 947 4.2): E_1(B) >= K_a, that is b E_1 > 24 C_beta + 72 log a (about 384 + 72 log a) with b = 24a. Row 954 Lemma GAP-R (conditional): R_J >= 1/(2 beta E_1) when E_1 <= 1.

**Sussman-Alpoge account (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; CA at 31a47c543775, fetched by URL to /tmp/lane960-sa).** The index `library/sa-index/ca-full/index.tsv` has no "transfer matri", "transfer operator", "volume change", "torus change" or "different volume" title. It has the chessboard family: CA-II 6.2 `lem-chessboard-value`, `lem-chessboard-estimate`, `lem-chessboard-inequality`, and CA-II 8.7 `lem-chessboard-torus` (line 108696, PROVED): reflection positivity int F theta F d mu_un >= 0 for every reflection of a torus with any periods n_mu >= 3 (odd allowed, through sites or bonds), and the chessboard estimate <F> <= <prod over tiles of F^[m]>^(1/n_c) for tiles of side s dividing every period. Read in full (lines 108696-108760). This is the reflection-positivity tool Step 2 uses for time-symmetric shapes. No varying-geometry statement was found in the account.

### Step 2 (done 2026-11-14T13:40Z): time-varying geometries set up exactly

Notation as in Step 1. X_B = G^(E_B), G = SU(2), du the product Haar measure; H_B = L^2(X_B); M_B = multiplication by e^(-V_B/2); C_B = S_(K_0) the time-like kernel operator; P_B the gauge projection; T_B = M_B C_B P_B M_B (`gap-transfer.md` 1.6: T_P = T P = P T P).

**2.1 The insertion map (decimation in one direction). PROVED.**
Let B = (b_1, b_2, b_3) and B^+ = (b_1 + 1, b_2, b_3), all sides >= 3. Write sites as (k, x') with k the first coordinate. The planes k = 0 and k = 1 of B^+ collapse to the plane 0 of B. Define rho: X_(B^+) -> X_B, for x' in the transverse torus:
- direction-1 link of B at m = 0: rho(u')_((0,x'),1) := u'_((0,x'),1) u'_((1,x'),1) (the two-link path 0 -> 1 -> 2 of B^+);
- direction-1 link of B at 1 <= m <= b_1 - 1: rho(u')_((m,x'),1) := u'_((m+1,x'),1) (the last one is the wrap link b_1 -> 0 of B^+);
- transverse link (i = 2, 3) of B at m = 0: rho(u')_((0,x'),i) := u'_((0,x'),i) (plane 0 kept, plane 1 dropped); at m >= 1: rho(u')_((m,x'),i) := u'_((m+1,x'),i).
Put (J f)(u') := f(rho(u')). Then:
- (J1) rho pushes du' to du: every coordinate of rho(u') is one Haar link or a product of two Haar links not used elsewhere, so the coordinates are independent and Haar. Hence J: H_B -> H_(B^+) is an isometry, J 1 = 1, and f >= 0 gives J f >= 0. J^* is the conditional expectation given rho: (J^* F)(u) = E[F(u') | rho(u') = u]. J^* J = I. J^* is Markov (positive, J^* 1 = 1).
- (J2) Gauge covariance. For h' in G^(Lambda^+) put h(0, x') := h'(0, x') and h(m, x') := h'(m + 1, x') for m >= 1. Then rho(h' . u') = h . rho(u'). (For the composite link: h'(0,x') u'_1 h'(1,x')^(-1) h'(1,x') u'_2 h'(2,x')^(-1) = h(0,x') rho_((0,x'),1) h(1,x')^(-1).) The map h' -> h pushes Haar to Haar. So P_(B^+) J = J P_B and J^* P_(B^+) = P_B J^*: J maps gauge-invariant functions to gauge-invariant functions. Gauge transformations on the dropped plane k = 1 act trivially on rho.
- (J3) Centre flips. With the flip planes chosen as in Lemma 1.1 (iv) of `gap-seed-check.md` (the plane x_k = 0 for k = 2, 3; for k = 1 the links ((0,x'),1) of B^+ and of B), J C_k^B = C_k^(B^+) J for k = 1, 2, 3. So J preserves the sixteen centre sectors.
- (J4) Translations in directions 2 and 3 commute with J; translations in direction 1 do not (the momenta 2 pi n/b_1 and 2 pi n/(b_1 + 1) differ).
- (J5) Composition: inserting planes one after another gives, for any boxes B <= B' (b_i <= b'_i), a Markov isometry J_(B'B): H_B -> H_(B') with (J1)-(J4). Doubling every side is the decimation u'_(2y,1) u'_(2y+1,1) of every direction (a block-spin map that keeps every second plane).

**2.2 Mixed transfer operators and the 4D complexes they define. PROVED (Fubini, as in `gap-transfer.md` 1.2-1.7).**
Put T_(B,B^+) := M_B C_B P_B J^* M_(B^+): H_(B^+) -> H_B, and T_(B^+,B) := T_(B,B^+)^* = M_(B^+) J C_B P_B M_B. T_(B,B^+) is the integral operator with kernel
  e^(-V_B(u)/2) A^0_B(u, rho(u')) e^(-V_(B^+)(u')/2),   A^0_B(u, v) := integral over G^(Lambda_B) of prod over l in E_B of c(h(x_l) v_l h(y_l)^(-1) u_l^(-1)) dh,
which is real, continuous, strictly positive, and invariant under gauge transformations of u and of u' (by (J2)). For boxes B_0, ..., B_(n-1), B_n = B_0, consecutive ones equal or differing by one insertion or one removal, put
  Z(G) := Tr( T_(B_0,B_1) T_(B_1,B_2) ... T_(B_(n-1),B_0) ),   T_(B,B) := T_B.
Z(G) is the integral of e^(-S_G) over the links of a 4D cell complex G: the spatial plaquettes of every slice (each once), the time-like 4-gons between equal slices, and at a step B -> B^+ one time-like polygon for each link l of B, the 4-gon g(x_l) rho(u')_l g(y_l)^(-1) u_l^(-1) or, at a composite link, the 5-gon. The time-like links of the step sit at the sites of B; the sites of the inserted plane of B^+ have no time-like link to the B-slice.
- (G1) G is not a rectangular torus, so it is outside the periodic family of the account (CA-II 8.7 allows any periods, but only rectangular tori). Proof: in a 4D rectangular torus every link lies in exactly 6 plaquettes. A transverse link of the inserted plane in the B^+-slice lies in 4 spatial plaquettes and at most one time-like one (forward); the backward one does not exist. QED
- (G2) The one time-varying shape that stays a torus is the moving box: Z = Tr(T_B^a tau^k), tau the translation by k sites in direction 1. It is the torus Z^4 modulo the lattice spanned by (a, k, 0, 0), (0, b_1, 0, 0), (0, 0, b_2, 0), (0, 0, 0, b_3). It is not rectangular for k not 0 mod b_1. Its average over k is the zero-momentum trace: (1/b_1) sum over k of Tr(T_B^a tau^k) = Tr(T_B^a Pi_(p_1 = 0)).
- (G3) Block averaging in Balaban's sense (an average of group elements projected back to the group) does not push Haar to Haar, so it gives no Markov isometry; decimation (2.1) is the exact one. Restriction to a sub-box with open faces leaves the periodic family (open boundary), and an extension by a fixed state psi on the inserted links, f -> (f o rho) psi, is Markov only for psi = 1, which is J.

**2.3 Time-symmetric shapes (grow, hold, shrink) and reflection positivity. PROVED.**
Let B_s = B_0, B_1, ..., B_m = B_L grow by one insertion per step, and Y := T_(B_m,B_(m-1)) ... T_(B_1,B_0): H_s -> H_L. The lens holds B_s for k steps, grows in m steps, holds B_L for a steps and shrinks back:
  Z_lens(k, a) := Tr( T_s^k Y^* T_L^a Y ) = || T_L^(a/2) Y T_s^(k/2) ||_HS^2 = sum over i, j of lambda_i(s)^k lambda_j(L)^a |<phi_j^L, Y phi_i^s>|^2 >= 0,
with (lambda_i(s), phi_i^s), (lambda_j(L), phi_j^L) the eigenpairs of T_s, T_L on the invariant spaces. Reflection positivity across the two time planes of symmetry is the Hilbert-Schmidt Cauchy-Schwarz inequality: for two growth paths Y_1, Y_2 (other insertion planes or orders),
  |Tr( T_s^k Y_1^* T_L^a Y_2 )| <= Z_lens(Y_1)^(1/2) Z_lens(Y_2)^(1/2).
Iterating over several lenses glued in time gives the chessboard form (the analogue, on these complexes, of CA-II 8.7 (a), (b) of Sussman and Alpoge on rectangular tori). These bound a MIXED geometry by PURE ones from above.

**2.4 Where the seed sits in this language.** S(a; B_L) = Tr T_L^a/lambda_0(L)^a - 1 needs an UPPER bound on the trace over ALL eigenvalues of T_L and a LOWER bound on lambda_0(L). The static tools get the upper bound from Lemma A in a spatial direction mu of a rectangular torus (Z(a, h, c, d) = Tr (T^(mu))^h <= Z(a, b, c, d)^(h/b)), and the lower bound from Lemma K (kappa >= 0, that is e(B) >= ell b along the enlarged direction). Step 3 asks what the complexes of 2.2-2.3 add to each side.

### Step 3 (done 2026-11-14T14:20Z): the best extrapolation inequality each geometry supports

**3.0 Frame.** For boxes B_s <= B_L (side by side) and a time t, an extrapolation inequality bounds g(t; B_L) = log Tr T_L^t - t e(B_L) by small-box quantities. It needs (N) an upper bound on Tr T_L^t over ALL levels and (D) a lower bound on e(B_L). Lemma E2 takes (N) from Lemma A along a spatial direction of a rectangular torus, (D) from Lemma K (b) (kappa >= 0), and reads the small box's deficit kappa(b) by Lemma X (crossing symmetry). Duplicate check for this step: a small-box criterion for a LOCAL law (Dobrushin-Shlosman type, all boundary conditions) is owned by rows 691/693 (`gap-ds-gauge.md`, `gap-ds-gauge-check.md`) and `gap-blockcrit-opus.md` (its Proposition CEIL: no vertex-block bound at beta >= 0.775). I do not attack it; 3.6 only names where varying geometry would meet it.

**3.1 Lemma DEN (the denominator has no room). PROVED.** Let B, h, t, t' be as in Lemma E2, and let E_low be any lower bound for e(B^h), from a lens, a trial state or anything else. Using E_low in place of Lemma K (b) in the proof of Lemma E2 gives at best
  g(t; B^h) <= (h/b) [ g(t; B) + t kappa(b) ] - t (E_low - ell h)_+ ,
and the subtracted term is at most t kappa(B^h) <= (t/(h - t'')) g(t''; B^h) for every integer 3 <= t'' < h.
Proof. The proof of Lemma E2 gives t kappa(h) + g(t; B^h) <= (h/b)(t kappa(b) + g(t; B)), with kappa(h) = e(h) - ell h; E_low <= e(h) gives kappa(h) >= E_low - ell h; Lemma X for the pair (t'', h) gives kappa(h) <= g(t''; B^h)/(h - t''). QED
Consequence (t'' = t, and g(t; B^h) <= U for the old right side U): the bound improves from U to at least U (1 - t/(h - t)). On the seed slab (h = 24a, t = a) any improvement of the denominator, by any geometry, is at most 1/23 of g, about 4.3 percent. For the seed this is nothing.

**3.2 The lens: identities and lower bounds only. PROVED.** Y, Z_lens as in 2.3; nu_0 >= nu_1 >= ... the eigenvalues of the positive trace-class operator Y T_s^k Y^* on H_L.
- (L1) Z_lens(k, a) = sum over j of lambda_j(L)^a w_j, with w_j := <phi_j^L, Y T_s^k Y^* phi_j^L> >= 0.
- (L2) Lower bounds on the top level: lambda_0(L)^a >= Z_lens(k, a)/Tr(T_s^k Y^* Y), and lambda_0(L)^a >= <psi, T_L^a psi> for psi = Y phi/||Y phi||. By 3.1 they improve no extrapolation by more than t/(h - t).
- (L3) Z_lens(k, a) <= lambda_0(L)^a ||Y||^2 Tr T_s^k. Normalised, the lens is bounded by a small-box thermal sum: Z_lens/(lambda_0(L)^a ||Y||^2 lambda_0(s)^k) <= 1 + S(k; B_s).
- (L4) Ky Fan: for every n, sum over j < n of w_j <= sum over i < n of nu_i, and nu_i <= ||Y||^2 lambda_i(s)^k. So the levels of T_L that the lens weighs with w_j >= w_* number at most ||Y||^2 lambda_0(s)^k (1 + S(k; B_s))/w_*.
- (L5) An upper bound of S(a; B_L) from Z_lens needs a coverage constant: if w_j >= c w_0 for every level j >= 1 of T_L, then S(a; B_L) <= (Z_lens(k, a)/(lambda_0(L)^a w_0) - 1)/c. No small-box quantity bounds c from below: c is an overlap of the eigenvectors of T_L with the image of Y. By (L4) the image covers at most as many levels as the small box carries.

**3.3 Lemma NO-OP (no operator comparison). PROVED.** For every lens operator Y of 2.3 (growth ending at B_L), every C > 0 and all integers t, t' >= 1, the operator inequality T_L^t <= C Y T_s^(t') Y^* on H_L,inv is false.
Proof. (i) T_L is injective on H_L,inv: for invariant f, T_L f = M C M f (P commutes with M and C, and M f is invariant); M is multiplication by a function >= e^(-3 beta |B_L|) > 0; C is convolution on the compact group G^(E) by prod over l of c(u_l), whose Fourier coefficients are products of the coefficients of c(g) = e^(-beta) e^((beta/2) tr g), all strictly positive (`gap-transfer.md` Statement (2): T is positive). So <f, T_L^t f> > 0 for f in H_L,inv, f not 0. (ii) The last factor of Y is T_(B_m,B_(m-1)) = M_(B_L) J C P M, so Ran Y is inside M_(B_L) Ran J. Take a plaquette p of the inserted plane of the last step (both transverse directions, at x_1 = 1) and f := e^(V_L/2) tr U_p, which is bounded, gauge invariant and not 0. For g in Ran J, <f, M_(B_L) g> = E[tr U_p g o rho] = E[tr U_p] E[g o rho] = 0, because U_p uses only links that rho drops, so it is independent of rho(u'), and E tr U_p = 0 under Haar. So f is orthogonal to Ran Y, Y^* f = 0, and the constant C times <f, Y T_s^(t') Y^* f> = 0 is below <f, T_L^t f> > 0. QED
Meaning. No geometry with a growth step gives a linear comparison of the large-box transfer operator with the small one, however large the constant. What remains is a trace comparison, Tr T_L^t <= C Tr(T_s^(t') Y^* Y). Normalised, it reads 1 + S(t; B_L) <= C' (1 + S(t'; B_s)). Since log(1 + S) is extensive (in a massive gas, g(t; B_L) = (|B_L|/|B_s|) g(t; B_s) to leading order, `gap-seed-shape.md` Section 2), C' must grow like exp((|B_L|/|B_s| - 1) g(t; B_s)). A linear (trace) comparison loses that factor. The static power form 1 + S(t; B_L) <= (1 + S(t; B_s))^(|B_L|/|B_s| (1 + ...)) is exact at leading order (ARGUED in the gas; Step 6 tests it in a solvable model).

**3.4 Hoelder on varying complexes. PROVED; the word "only" below is ARGUED.**
- If the boxes vary only in directions 2 and 3, the complex is S^1 x M (x_1 periodic, M a 3D complex in (t, x_2, x_3)). The construction of `gap-transfer.md` Section 1 with x_1 as time and M as slice (spatial action of M, time-like kernel along x_1, gauge projection) gives a positive trace-class transfer operator in direction 1 (positivity as in its Statement (2): T = M C M with C a convolution with positive Fourier coefficients); this is the product-direction case of the reflection positivity of CA-II 8.7 (a) of Sussman and Alpoge. So Lemma A holds in x_1: Z(n_1 = h) <= Z(n_1 = b)^(h/b). This compares two complexes with the same varying part M. It never turns a varying complex into a rectangular one.
- If the slices along a direction are operators between different spaces (A_i: H_(i+1) -> H_i), Hoelder for Schatten norms gives |Tr(A_1 ... A_n)| <= product of ||A_i||_n, and ||A_i||_n^n = Tr((A_i^* A_i)^(n/2)) is the partition function of the zigzag complex (A_i^*, A_i repeated). This is the chessboard bound: a varying complex is bounded ABOVE by zigzag or rectangular ones.
- The seed needs an upper bound on a RECTANGULAR torus. In every inequality of the static method and of 3.2-3.4 such an upper bound comes from Lemma A along a product direction of that same torus. I found no other source. So varying complexes enter only on the bounded side.

**3.5 Crossing symmetry. ARGUED.** Lemma X uses W(x, y) = W(y, x): one rectangular torus read along two directions. Exchanging t and x_1 in a complex with a growth step gives a different complex (the step's 5-gons and missing time-like links of (G1) become a step in x_1), so a varying complex has no crossing identity. The small box's deficit kappa(b), which is where E2 loses (Step 4), has no lens analogue.

**3.6 The moving box (shear). PROVED.** Tr(T_B^a tau^k) = sum over i of lambda_i^a e^(i k p_i) (tau commutes with T_B; p_i the momentum in direction 1). Averaging over k gives Tr(T_B^a Pi_p). With S_p(a; B) := Tr(T_B^a Pi_p)/lambda_0^a - delta_(p,0): S(a; B) = sum over p of S_p(a; B). The vacuum has p = 0. The seed counts every momentum, so the shear changes no count. A momentum-resolved seed would need min energy at p >= min energy at p = 0: OPEN, and not a geometry question.

**3.7 (LSI-J) through a change of geometry. PROVED (marginal step); the rest CONDITIONAL or owned elsewhere.**
- (M) If a law mu on X x X' satisfies Ent_mu(Phi^2) <= (2/alpha) E_mu |grad Phi|^2, then its marginal on X satisfies the same with grad_x, same alpha (take Phi = phi(x)).
- J (row 941 (A1)) is the limit as T grows of the law of two consecutive slices of the torus B_L x Z/T in the axial gauge (temporal links 1 except at one time, away from the two slices); `gap-transfer.md` Statement (6). So an LSI with constant alpha for those LOCAL torus laws in the spatial-link variables, uniform in T, gives (LSI-J)_alpha on B_L (CONDITIONAL on that LSI; the passage to the limit is for smooth bounded Phi).
- This replaces the non-local J (row 947 7.3: "J has no known local specification") by a local parent. A small-box criterion for the parent's LSI is the Dobrushin-Shlosman type route of rows 691/693 and `gap-blockcrit-opus.md`, capped there at beta >= 0.775 for vertex blocks; not attacked here. The rate (LSI-J-seed) asks, alpha_J >= 2 beta K_a, is not changed by this step.
- A growth step gives J no product or Markov relation across boxes: (rho x rho)_* J_L is not J_s in general (ARGUED: decimation changes the effective couplings of the slice law).

**3.8 Table (each line: the best inequality found for that geometry).**

| Geometry | Best inequality found | Numerator (N) | Denominator (D) | Against SH, E', B3 |
|---|---|---|---|---|
| Rectangular tori (static) | Lemma E2, B3, SH | Lemma A (Hoelder in a product direction) | Lemma K (b), exact up to t kappa(h) | reference |
| Lens (grow, hold, shrink) | (L1)-(L5); lower bounds on lambda_0(B_L) | none: Lemma NO-OP; a trace comparison is linear and loses exp(volume ratio x g) | variational; at most t/(h - t) gain (DEN) | strictly weaker |
| Varying in directions 2, 3 only | Lemma A in x_1 between complexes with the same varying part | compares varying with varying | none new | no seed statement |
| Varying along the transfer direction | chessboard: varying <= zigzag/rectangular | wrong side for the seed | none new | no seed statement |
| Moving box (shear) | momentum resolution S = sum over p of S_p | same count | same | no gain |
| Two-slice law to 4D parent (3.7) | (LSI-J) from an LSI of a local law, same alpha | n/a | n/a | moves (LSI-J) to the DS-type route of rows 691/693 (capped at beta >= 0.775 for vertex blocks); no rate gain |

What is left for Step 4: where exactly the static method loses against the truth, and whether any of those losses is one a geometry could remove.

### Step 4 (done 2026-11-14T15:00Z): comparison with Theorem SH, Lemma E' and Proposition B3; where the static method loses

**4.1 Exact slack of Lemma E2. PROVED (an identity from its proof).** Write U for the right side of Lemma E2 and D_H := (h/b) log W(t, b) - log W(t, h) >= 0 for the slack of Lemma A (Hoelder). Then
  U - g(t; B^h) = D_H + t kappa(h) + (h/b) t [ g(t'; B)/(b - t') - kappa(b) ],
three non-negative terms: the Hoelder slack (N), the dropped deficit of the large box (D), and the slack of Lemma X for the small box (X). Theorem SH adds a fourth: (T) in the form g(qa; B) <= log(1 + s^q) and S(ja) <= S(pa)^(j/p).
In the ideal gas of `gap-seed-shape.md` Section 2 (F = f|n| + sum over mu of (|n|/n_mu) w(n_mu); GUIDE model): kappa(y) = c d w(y), g(t; y) = y c d w(t), D_H = t c d ((h/b) w(b) - w(h)), so (N) and (D) are of size t c d w(b), exponentially small in b, while (X) is (h/b) t c d [b w(t')/(b - t') - w(b)], of size e^(-m t'), and (T) loses the multiplicity: in a gas with M one-particle levels near the bottom, S(qa) is about M e^(-m q a) against s^q about M^q e^(-m q a), a factor M^(q-1). So the static method loses in (X) and (T). (N) and (D) are tight to exponential accuracy.

**4.2 What a geometry would have to do for each term.**
- (N): nothing to gain (4.1).
- (D): **Lemma OVL. PROVED.** Let psi in H_L,inv be a unit vector, c_0 := <Omega_L, psi>, r_1 := lambda_1(L)/lambda_0(L) < 1, and E_low := (1/t) log <psi, T_L^t psi>. If E_low > ell h (the trial state beats Lemma K (b) at time t), then |c_0|^2 > (e^(-t kappa(h)) - r_1^t)/(1 - r_1^t).
  Proof. <psi, T_L^t psi> = lambda_0^t (|c_0|^2 + sum over i >= 1 of |c_i|^2 r_i^t) <= lambda_0^t (|c_0|^2 + (1 - |c_0|^2) r_1^t). E_low > ell h = e(h) - kappa(h) means <psi, T_L^t psi> > lambda_0^t e^(-t kappa(h)). Rearrange. QED
  On the seed slab with S(a; B_L) <= 3/10 and t = a, h = 24a: t kappa(h) <= g/23 <= log(1.3)/23 < 0.0115 (Lemma X) and r_1^t <= S <= 0.3, so a trial state, lens or otherwise, helps the denominator only if its squared overlap with the vacuum of the large box exceeds 0.983. A state that close to Omega_L is the large-box vacuum to two digits; a decimation lift of a small-box state has an overlap that falls with the inserted area (measured in Step 6).
- (X): needs an upper bound on kappa(b) = e(b) - ell b better than g(t'; b)/(b - t'). The upper bound on e(b) is free (e(b) <= (1/t) log Z(t, b)). So it needs a LOWER bound on ell = inf over y of e(y)/y, that is, lower bounds on e(y) for all large y. Lemma X gets it exactly from crossing symmetry. A varying geometry gets lower bounds on e(y) only from trial states that glue y/b copies of the small-box vacuum; each seam costs a defect energy delta. That gives kappa(b) <= delta per seam. In a massive theory kappa(b) is about e^(-m b) and the Lemma X bound about e^(-m t'), while a local seam costs order (cross-section) x beta. So gluing is far weaker than crossing (ARGUED; Step 6 measures delta in a solvable model). A complex with a growth step has no crossing identity (3.5).
- (T): **sharp in the class. PROVED.** For an operator with one positive excited level, S(t) = r_1^t and S(qa) = S(a)^q for every real q >= 1: equality. The two-phase Ising model of `gap-seed-shape.md` 4.1 is in the class and approaches this (lambda_1/lambda_0 -> 1, the others -> 0). So no inequality that reads only seed values and the class properties improves (T). To improve it, a statement must count the levels of T_B (spectral information). A geometry adds a new partition function, not a level count: by Lemma NO-OP and (L4) it does not see the levels of T_L that the small box lacks.

**4.3 A static refinement found on the way (NOT varying geometry). PROVED by hand; not checked.**
**Lemma Q (real second times).** For every box B, every integer a >= 1 and every real tau >= a with tau an integer: S(tau; B) <= S(a; B)^(tau/a).
Proof. S(t; B) = sum over i >= 1 of r_i^t, the t-th power of the l^t norm of the sequence (r_i) (all 0 < r_i < 1). The l^p norm is non-increasing in p > 0, so S(tau)^(1/tau) <= S(a)^(1/a). (This is Lemma A (a) applied to the positive trace-class operator (T_B/lambda_0) on the orthocomplement of Omega_B, read for real exponents.) QED
**Theorem SH' (Theorem SH with real p, q).** Theorem SH and Proposition B3 hold for real 1 <= p <= q and p <= j, whenever pa and qa are integers and qa < min b_i: the proof of SH uses (T) only in the forms g(pa; B) <= log(1 + s^p), g(qa; B) <= log(1 + s^q) and S(ja) <= S(pa)^(j/p), all given by Lemma Q, and Lemma E2 and B3 need only integer times t = pa, t' = qa. The scaled pair (ja, jB) has the integers jpa, jqa. QED
**New line of the table of 1.5: r = 2, step (j, p, q) = (2, 1, 3/2), a even.** beta_i = 2a/(2a - 3a/2) = 4, Pi = 64, C = (2/3) 63 = 42, phi(x) = [(1 + x)^8 (1 + x^(3/2))^336 - 1]^2. Hand check for 0 <= x <= x_0 = 1/550: u := 8 log(1 + x) + 336 log(1 + x^(3/2)) <= x (8 + 336 x_0^(1/2)); sqrt(550) > 23.45 and 336/23.45 < 14.33, so u <= 22.33 x <= 0.04061; e^0.04061 < 1.04145 (series 1 + 0.04061 + 0.000825 + 0.0000112 + ...); e^u - 1 <= u e^u <= 23.26 x; phi(x) <= 541.1 x^2. So K = 541.1, K x_0 = 0.984 < 1. **Threshold 1/550 at ratio 2** (was 1/1650 by two stages and 1/3500 by step 3), with rate log(1/(541.1 s))/a. In (ii), E = (2 x 2/(2 - 1))^3 = 64 and E s_k <= 64/550 < 1; e E/K = 0.32 < 1, so log(e E/K) < 0, k_0 = 0, and m(L^3) >= (1/a)[log(1/(K s)) - 2^(-k) log(e E/K)] >= log(1/(541.1 s))/a for every integer L >= b = 2a.
  Other steps tried by hand (GUIDE values, not proved): (3, 1, 3/2) about 1/700; (2, 1, 1.4) and (2, 1, 1.6) slightly worse than 3/2; at r = 2.5 the integer step (2, 1, 2) stays best; at r = 1.5 the real q gives about the old 1/12000 (the deficit term x^(q - p) decays too slowly); at r = 4 the integer (2, 2, 3) stays best. So the refinement matters at 2 <= r < about 2.3.
  Correction to `gap-seed-shape.md` 1.7 (and its check, `gap-seed-shape-check.md` 1.7): "For r <= 2 only p = q = 1 is available" holds for integer q only; with Lemma Q any integer second time t' with a < t' < b is available.
  Consumer note (for the lead, not acted on): `gap-finishline-opus.md` lines 101 and 189 quote the r = 2 threshold 1/1650; Theorem SH' gives 1/550 there, if row 961's check confirms Lemma Q and the hand check.
  Box size (GUIDE, the one-particle model of `gap-seed-shape.md` Section 5): a factor 3 in the threshold moves m a by about log 3 = 1.1, so at r = 2 the model's seed box shrinks from about m a = 10.4, m b = 20.8 to about 9.3 and 18.6 correlation lengths.

**4.4 Answer for Step 4.** No varying geometry of Steps 2-3 is strictly better than Theorem SH, Lemma E' or Proposition B3, in the threshold or in the box size. The reasons, term by term: (N) and (D) leave no room (4.1, DEN, OVL); (X) needs crossing symmetry, which varying complexes lack, or a seam cost below the deficit, which local gluing cannot give; (T) is sharp in the class and needs level counting, which no geometry supplies (NO-OP, (L4)). The only gain found is static: Lemma Q and Theorem SH' (threshold 1/550 at ratio 2).

### Step 5 (done 2026-11-14T15:20Z): fact tests

**5.1 Theorem SH' (threshold 1/550 at ratio 2) does not fire for U(1)-type models. PROVED (hand).**
- Compact Gaussian model Z_R of `gap-seed-shape.md` 4.2 (in the class, no gap): 1 + S(a; b^3) = theta(A) theta(A')^3 prod over k not 0 of (1 - e^(-a eps_k))^(-1) >= 1 + sum over k not 0 of e^(-a eps_k) (theta >= 1). The six momenta k = +-2 pi e_i/b have 2 cosh eps = 2 + 4 sin^2(pi/b), so eps = 2 asinh(sin(pi/b)) <= 2 pi/b and a eps <= pi at b = 2a. So S(a; (2a)^3) >= 6 e^(-pi) > 0.259 > 1/550, for every R and every a.
- Free photon (Gaussian mode model; two polarisations): the same six momenta give S >= 12 e^(-pi) > 0.518. (Scope: the photon's zero modes put it outside the class, as for the massless scalar in 4.2 there; the bound only needs the twelve levels.)
- Compact Wilson U(1) in its Coulomb phase: photon-like levels at energy about 2 pi/b are RECALLED, not rebuilt; with them S is of order one at ratio 2 (GUIDE level only).

**5.2 Frozen Q_8 and 2T, and Z_2 at large beta. RECALLED.** The flat-connection (flux) sectors of the 3-torus become degenerate with the vacuum, so S(a; B) >= 7 - o(1) (row 697 file, for Z_2; the same count for any group with centre Z_2). Far above 1/550: SH' does not fire. The decimation map J and the lens identities hold for finite groups too (2.1 uses only Haar invariance; NO-OP uses a non-trivial character with zero mean and positive Fourier coefficients of c, both true for finite groups), and they claim no gap. PASS.

**5.3 SMALL-BOX.** SH' keeps the hypothesis type of Theorem SH: a seed at one fixed coupling on one box. At a fixed box and large beta the SU(2) seed is large (perturbative gluon and toron levels at energies of order 1/b; ARGUED, RECALLED), so the box size must grow with beta, and the hypothesis carries that size. SH' lowers the bar from 1/1650 to 1/550; it adds no small-box claim. PASS.

**5.4 The extrapolation question itself, against U(1). PROVED (model in the class).** In the compact Gaussian model, for every fixed a: S(a; L^3) >= sum over k not 0 of e^(-a eps_k(L)), and the number of k with a eps_k(L) <= 1 grows like (L/a)^3, so S(a; L^3) -> infinity as L -> infinity, while every quantity on a fixed small box (any geometry, any time) is fixed. So no inequality "S(a; L^3) <= F(small-box data)" with F independent of L holds in the class. A valid extrapolation must let the time grow with the box, as Theorem SH does (a_k = j^k a). This is the U(1) form of the reason why Steps 3-4 find no small-slice gain: the seed of a large box at a fixed time is extensive, and only the joint scaling of time and box keeps it small.

**5.5 Lemmas of Steps 2-4 (J1-J5, G1-G3, L1-L5, NO-OP, DEN, OVL, Lemma Q).** Each is an identity or an inequality valid in the whole class (any compact group, including U(1), Q_8, 2T, and the Ising model); none claims a gap. They pass the fact tests by not claiming one.
