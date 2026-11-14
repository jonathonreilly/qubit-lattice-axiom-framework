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
