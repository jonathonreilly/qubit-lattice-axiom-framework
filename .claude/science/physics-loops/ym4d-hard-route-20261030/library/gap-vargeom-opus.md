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
