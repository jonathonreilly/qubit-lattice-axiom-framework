lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T17:04Z

# Check of row 993 (`library/gap-idab-opus.md`): line-by-line, against Balaban's page images and the Sussman-Alpoge lines it quotes

Provenance: Claude Opus 5.5, max effort, Mac mini worker 3, branch `claude/ym4d-hard-route` at commit d5eace7be. Queue row 994. Not an audit. The checked note was written by Claude Opus 5.5 high, so this check is same provider and is not independent; a gpt-6-astra check is held for the Codex reset. No commit, no push; the relay copies this file.

Credit: the objects checked come from Balaban (CMP 99, 102, 109, 119) and from Ethan Sussman and Levent Alpoge's complete account (CA-I, CA-II, CA-III at 31a47c543775; text by Claude and Codex). The rebuild under check is by Claude Opus 5.5 high (row 993).

Status: started 2026-11-15T05:04Z.

## Plan (at most eight steps; one step per response, appended before the next)

1. Read the checked note in full. Repo search. List every item the row names, with the note's line and the sources it quotes. Find SA L14091-14107.
2. Lemma C (constants of CMP 119 (3.15) and (3.33): torus-free numbers per bond, site or coordinate), from the page images.
3. Lemma ZB (a)-(d), including z^(k)(c) = L^9 at U = 1 (CMP 109 p. 268, CMP 119 p. 267), from the page images.
4. The E_0^(j) readings and the counterexample (CMP 119 (2.27), wrapping domains).
5. Step 4: the block map identity (CMP 109 (0.3), G(y,x), (0.10)-(0.12) against SA (QC1)-(QC3)) and Lemma LR.
6. Lemmas V, R, GS, PS, QD and MIN (CMP 109 (2.4)-(2.11), CMP 102 (174)).
7. (b2), (b3), the (ID-b) assembly, and whether (r4) can be settled from SA L14091-14107.
8. Verdict table (HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line) and the RESULT line.

## Working log

### Step 1. Inputs, items, sources (05:20Z)

**Repo search.** `grep` for `gap-idab`, `ID-a'`, `(ID-b)` over `library/`, `gates/`, `checks/`: hits only in `gap-iloc-opus.md` (row 990, which poses the items), `gap-det-check-opus.md` (row 989), `gap-idab-opus.md` (the note under check) and this file. `library/open-core.md` and `library/l17c.md`: no hit. No other check of row 993 exists. This is a check item, so no lemma is attacked.

**Note under check.** `library/gap-idab-opus.md` at d5eace7be, 279 lines, read in full. Its header says it was pinned at 0ee089f92; its step times (05:10Z-08:00Z) are wrong per the lead note in row 993 (run 04:44Z-04:59Z). Not relevant to the mathematics.

**Sources fetched (scratch, not committed).** SA outline `YM4_sketch_500.tex` and CA-I `theorem_0_complete_account_raw_I.tex` at 31a47c543775 from github.com/ethanwsussman/Yang--Mills-LLM-experiment into `/tmp/idab-check-994/sa/`. Outline SHA-256 d7f77d4da3eb...4b6f, the hash the note gives (d7f77d4d...). So the note's outline line numbers refer to this file. Balaban's PDFs in `~/ym4d-papers/` (CMP 99 389, 102 277, 109 249, 119 243), rendered page by page to PNG with PyMuPDF in `/tmp/idab-check-994/png/` and read as images. PDF page = journal page - first page + 1 (checked against the note's own pairs: CMP 119 p. 267 = PDF 25, p. 273 = PDF 31).

**Items the row names, with the note's lines.**

| # | Item | Note lines | Sources it quotes |
|---|---|---|---|
| 1 | Lemma C | L91-108 | CMP 119 (3.15) p. 267, (3.33) p. 273; CMP 109 (0.15) p. 255, (2.10) p. 267 |
| 2 | Lemma ZB (a)-(d), value L^9 at U = 1 | L89, L112-120 | CMP 109 (2.4) p. 266, h p. 267, p. 268; CMP 119 p. 267, p. 273; row 990 (QC15)-(QC16) |
| 3 | E_0 readings (i), (ii) and the counterexample | L122-125 | CMP 119 (2.25)-(2.27) p. 259, p. 273; CA-I L104010-104013, L106125-106150 |
| 4 | Step 4: block map identity, Lemma LR | L127-145 | CMP 109 (0.3) p. 252, (0.4)-(0.12) pp. 253-254; SA L7946-7958; CA-I L800-840 |
| 5 | Lemmas V, R, GS, PS | L156-171 | elementary; pr-lay (6)-(7) |
| 6 | Lemma QD | L168, L237-244 | SA L9634, L10139, L10212 |
| 7 | Lemma MIN (and B1) | L186-197, L227-231 | CMP 109 (0.21), (1.5), (2.6)-(2.8); CMP 102 (74)-(102), (174)-(177); CMP 99 p. 394 |
| 8 | (b2), (b3), (ID-b) assembly, (r4) | L199-219, L235 | CMP 109 (0.19), (1.5), (1.8), (2.5), (2.11), p. 268; SA L6854, L7180-7188, L10200-10208, L14091-14107 |

**SA L14091-14118, read now (for item 8, (r4)).** L14091-14107 define, at a regular complex pair P = (U, J), Delta_k(P) = (Q G_1 Q^T)^{-1} - a - E^(2)[H_1^T J] and A(P) = C_V^T (GF^(2)_V + Delta_k(P)) C_V, with "C_V eliminates the pivot bonds", "The many-scale rows Q come from the straightened average", "E^(2) comes from the plain one-step constraint on V". The next paragraph, L14109-14118, says: "At a background pair P_W = (U_+, J(U_+)), the form in (eq:actual-regular-precision) is the Hessian on the fibre of A o U_k + GF_k. ... Thus the Gaussian of the step is C^(k) = A(P_W)^{-1}. Soft gauge fixing supplies the positive quadratic form on the orbit directions". Whether this settles (r4) is decided in Step 7, after the normalizations of Balaban's (2.10)-(2.12) are read from the page images.

### Step 2. Lemma C, from the page images of CMP 119 (05:40Z)

**Read from the images** (CMP 119, PDF pages 13, 24, 25, 26, 31, 32 = journal pp. 255, 266, 267, 268, 273, 274; 130 dpi; the OCR was not used for any formula):

- p. 267, (3.15): the exponent carries A_k(1/g_k^2, U_{k+1}) + log g_k d(g)|B(Gamma_{k+1})^*| + log sigma_0 |B(Gamma_{k+1})^*| - log z (L^4 - 1)|Gamma_{k+1}|, then z^(k) int dA_k|_{Omega_{k+1}} chi'_k(Omega_{k+1}) exp[-(1/2)<A_k, C^* Delta^(k) C A_k> + P^(k)(g_k, U_{k+1}, A_k)]. p. 268 continues (3.15) with the field exp i[g_k C A_k - h Dtilde(g_k C A_k)] V^(k). The note's transcription (its L95-97) is exact.
- p. 255, (2.2): Gamma_0 = Omega_1^c, Gamma_j = Omega_j^(j) \ Omega_{j+1}^(j) (1 <= j <= k-1), Gamma_k = Omega_k^(k); "This definition is meant for sets of points, bonds and plaquettes". So Gamma_{k+1} = Omega_{k+1}^(k+1), and at P_0 (Omega_{k+1} the whole torus) it is the whole coarse torus T^(k+1).
- p. 266, (3.10)-(3.11): V^(k) minimizes A(U_k) under Vbar_k = V_{k+1} on Gamma_{k+1} and V_k(y,x) = 1 for y in Gamma_{k+1}, x in B(y); "This minimum is given by V^(k) = M^k(U_{k+1})"; V'_k = V_k (V^(k))^{-1} on B(Gamma_{k+1}).
- p. 273, (3.33): read exactly as the note quotes it (L56), with the sum over c in Lambda_{k+1}^(k+1) and "The last term is a number, which contributes to the vacuum energy renormalization, so we include it into the definition of E_0^(k)".
- p. 274, (3.36)-(3.39): -(1/2) log det(C^* Delta^(k) C) = -(1/2) log lambda_0 |Lambda^(k)*_{k+1}| + (1/2) int_0^inf dlambda (lambda_0 + lambda)^{-1} Tr(...) (3.36); (3.37) defines E_0^(k+1)(Lambda_{k+1}, U_{k+1}, b), a per-bond function: chi(b)[-(1/2) log lambda_0 + resolvent term + characteristic-function term] + g_k int dt <tr V'_k ...>_t; (3.38): the logarithm = sum_c log z^(k)(c) + sum_{b in Lambda^(k)_{k+1}} E_0^(k+1)(Lambda_{k+1}, b) + const, "The constant above is the constant in (3.33), included into the vacuum renormalization E_0^(k)"; (3.39): covariance for the per-bond terms when Omega_j = Lambda_j = T_eta.

**Correction to the note's Step 2a (L61).** The note says (3.39) "states covariance for the localized terms (3.37), whose first term is the localized z-factor". From the image, (3.37) does not contain z^(k)(c): it defines the per-bond function E_0^(k+1)(b), whose first term is -(1/2) log lambda_0. The z-factors are the separate first sum of (3.38). The sentence before (3.39), "The terms in (3.38) are gauge invariant. If they are constructed assuming ... then they are also Euclidean covariant", covers both sums of (3.38), but the display (3.39) is written for E^(k+1)(U_{k+1}, b) only. Nothing in the note's chain rests on this sentence: Lemma ZB (c) proves the covariance of z^(k)(c) directly. Verdict for that quote: HOLDS AFTER CORRECTION (replace "whose first term is the localized z-factor" by "the per-bond terms; the z-factors are the separate sum of (3.38)").

**Notation hazard found (affects item 3).** CMP 119 uses E_0 for two objects: E_0^(k) "the vacuum renormalization" (a constant, pp. 273-274) and E_0^(k+1)(Lambda_{k+1}, U_{k+1}, b) of (3.37), a field-dependent per-bond term that, at U = 1, contains the per-bond share of -(1/2) log det. The note's two readings (Step 3) do not name the second object. See Step 4 below.

**Lemma C. Verdict: HOLDS.** Each constant of (3.15) and (3.33) is a coefficient times a count. Coefficients: d(g) log g_k, log sigma_0, -log z, (1/2) log 2 pi (the last from int_R e^{-x^2/2} dx = sqrt(2 pi) and Fubini). None contains the torus side n; they depend on the group, on g_k, and on the gauge-fixing parameters of the normalizer z (the note says (alpha, eps_0); if Balaban's z at step k carries g_k and eps_k instead, it is still torus-free, which is all Lemma C claims). Counts at P_0: |Gamma_{k+1}| = n^4 by (2.2) (a set of coarse points); |B(Gamma_{k+1})^*| and N are counts of a set of level-k bonds that is invariant under the coarse translations L Z^4. A simpler argument than the note's tiling: on the torus of side nL (level-k units), the n^4 coarse translates of one fundamental cell of side L partition the bonds (counted as pairs (site, direction)), so any coarse-translation-invariant bond set has n^4 times its count in one cell, for every n >= 1. Both of the note's candidate meanings of B(Gamma_{k+1})^* (all bonds of the blocks and corridors, 4L^4 per coarse site; or these minus the pivots, 4L^4 - 4) are such sets. So every constant is (torus-free number) x n^4. The note's tiling argument is also correct. Not settled, and not needed: which of the two counts Balaban's "*" denotes.

