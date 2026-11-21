lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T08:17Z

# Check of Example F and Lemma K (`library/r7-repair-check.md`, sections 2 and 3)

FINISH row 657 (`scale-note`), section A. Provenance: Claude Opus 5.5, high, one fresh session, pinned at commit 212781e0c; not an audit. Claude Fable 5.2 wrote Example F and Lemma K (row 652). I did not write them. I wrote neither the rows they repair (625 and 648 were earlier Opus sessions; this session has no memory of them).

Source: Y = `YM4/YM4_1400.tex` of Ethan Sussman and Levent Alpoge (written with Claude and Codex), fetched by me at commit c7fef8b21b58 into `/tmp/sn-w2/src/`; sha1 907b3eba6d02836c65b1f721fc8694b13bfc99d2, identical to `/tmp/ym4_1400.tex` (the 2bc0658f copy). 'Y n' is line n. No computer run: memory was at 49 percent free, and every number below is checked by hand.

Overlap: `grep` of `library/open-core.md` for Example F, Lemma K, `k_0`, the scale comparison and (G) finds nothing. The FINISH rows near it are 618, 625, 648, 652 and 654; row 657 says this is not a duplicate.

## Verdicts

| item | verdict | one line |
|---|---|---|
| Example F | HOLDS | Every condition of Y 1101-1113 holds on the frame, each `Rcheck_j` is right, the two drops are not consecutive, and the comparison fails at `t = 14`. Its exact range is narrower than its use in the note suggests; see A.1 (c)-(d). |
| Lemma K | HOLDS | Every step is right. The proof needs `L >= 4` (Y gives `L >= 13`). It proves every word of Y 63775-63778, including the sentence 'Thus ...', by the steps 0 or 1 of the exponent (A.2 (c)). |

Nothing FAILS. One repair of wording for the note (A.1 (d)): Example F alone shows that the frame definition does not give the comparison when `gamma >= e^{-1}` (at `r = 2`, `L = 13`). It does not by itself show that a ceiling must depend on `Bbar`. That needs the family F(gamma) of A.1 (e), which is new here and not checked by another model.

## A.1 Example F

**Frame.** `r = 2`, `L = 13`, `0 <= lambda <= 12`, `c_5 >= 0`, `Bbar >= e^{14}`, `e^{-1} <= gamma < e^{-1/2}`. Length `k = 14`. `theta_j = e^{14} + lambda (10 - j)` for `0 <= j <= 10`; `theta_11 = e^5`, `theta_12 = e^4`, `theta_13 = e^3`, `theta_14 = e^2`.

**(a) Each condition of Y 1101-1113.** Y 1102-1103: "A frame is a real sequence \(\theta_0,\ldots,\theta_k\ge\gamma^{-2}\), with \(0<\gamma<e^{-1/2}\), such that, for \(i\le j\)".

1. Floor. The least member is `theta_14 = e^2`. `gamma >= e^{-1}` gives `gamma^{-2} <= e^2`. HOLDS. It holds if and only if `gamma >= e^{-1}`.
2. Range of `gamma`: `0 < gamma < e^{-1/2}` is assumed. HOLDS.
3. Two-sided bound (Y 1107-1108), `lambda (j-i) - c_5 <= theta_i - theta_j <= Bbar (j-i)` for `i <= j`. The one-step drops `d_j = theta_j - theta_{j+1}` are: `d_j = lambda` for `0 <= j <= 9`; `d_10 = e^{14} - e^5`; `d_11 = e^5 - e^4 = e^4 (e-1)`; `d_12 = e^4 - e^3 = e^3 (e-1)`; `d_13 = e^3 - e^2 = e^2 (e-1)`.
   - Lower ends. `e^2 (e-1) > 2.7^2 * 1.7 = 7.29 * 1.7 = 12.393 > 12 >= lambda`. `d_11, d_12` exceed `d_13`, since `e^4 > e^3 > e^2`. `d_10 = e^5 (e^9 - 1) >= e^5 > 12`. So every `d_j >= lambda`.
   - Upper ends. `d_j <= e^{14} - e^5` for every `j`: `lambda <= 12 < e^{14} - e^5`, and `d_11, d_12, d_13 < e^5 < e^{14} - e^5` (as `e^9 > 2`). So every `d_j <= Bbar` when `Bbar >= e^{14} - e^5`.
   - For `i < j`, `theta_i - theta_j = sum_{i <= m < j} d_m` lies in `[lambda (j-i), Bbar (j-i)]`, and `lambda (j-i) - c_5 <= lambda (j-i)` as `c_5 >= 0`. At `i = j` both sides read `-c_5 <= 0 <= 0`. HOLDS.
4. `Rcheck_j = R(min_{i<=j} theta_i)` (Y 1109), `R(y)` the smallest power of `L` not below `(log y)^r` (Y 1113). Every `d_j >= 0`, so `theta` does not increase and `min_{i<=j} theta_i = theta_j`. With `r = 2`, `L = 13`: `R(y) = 13` for `1 < (log y)^2 <= 13`; `169` for `13 < (log y)^2 <= 169`; `2197` for `169 < (log y)^2 <= 2197`.
   - `j <= 10`: `e^{14} <= theta_j <= e^{14} + 120 <= e^{15}`, since `e^{15} - e^{14} = e^{14}(e-1) > 120`. So `14 <= log theta_j <= 15`, `196 <= (log theta_j)^2 <= 225`, and `Rcheck_j = 2197`.
   - `(log theta_11)^2 = 25`, `(log theta_12)^2 = 16`: both in `(13, 169]`, so `Rcheck_11 = Rcheck_12 = 169`.
   - `(log theta_13)^2 = 9`, `(log theta_14)^2 = 4`: both in `(1, 13]`, so `Rcheck_13 = Rcheck_14 = 13`. HOLDS.
5. `Rcheck_j <= L Rcheck_{j+1}` (Y 1110). The sequence is `2197` (`j <= 10`), `169, 169, 13, 13`. The ratio `Rcheck_j / Rcheck_{j+1}` is 1 except `2197/169 = 13` at `j = 10` and `169/13 = 13` at `j = 12`. HOLDS.

**(b) No two drops are consecutive.** The drops of `Rcheck` are at `10 -> 11` and `12 -> 13`; the step `11 -> 12` has ratio 1. So Y 73081-73082 ("\(R_{j+1}/R_j\in\{1,L^{-1}\}\), and two size drops are not consecutive") and the claim of Y 62001 ("two consecutive drops never occur") hold on the frame. HOLDS.

**(c) The failure at `t = 14`.** `N_14 = Rcheck_14 = 13` (Y 1121: "The waiting depth is \(\mathsf N_j=\check R_j\)"). `h_14 = 14 - 13 = 1` (Y 73378). `Rcheck_1 = 2197 = 13^3`. `L Rcheck_14 = 169 < 2197`. So `Rcheck_{h_14} = L^2 Rcheck_14 > L Rcheck_14`, and Y 73382-73383 fails. Also `h_14 = 1 >= 1`, the case Y 63745 uses ("since \(h\ge1\)"). HOLDS.

**(d) Exact range.** Fix `r = 2`, `L = 13`, `0 <= lambda <= 12`, `c_5 >= 0`. The sequence above is a frame exactly when
- `e^{-1} <= gamma < e^{-1/2}` (item 1: the floor is attained at `theta_14 = e^2`), and
- `Bbar >= e^{14} - e^5` (item 3: the step `i = 10`, `j = 11` of the upper bound needs `Bbar >= d_10`, and the largest one-step drop is `d_10`).

So the example covers `gamma` in `[e^{-1}, e^{-1/2})` and `Bbar` in `[e^{14} - e^5, infinity)`. The note's round form `Bbar >= e^{14}` is a subset. It covers one pair `(r, L) = (2, 13)`. Y takes `r >= 2` (Y 62001) and "\(L\ge13\) odd" (Y 650) "in addition to the background floors", so Y's own `r` and `L` may be other values. For `(lambda, c_5)` the range above is sufficient; I did not compute the exact set.

What Example F shows, read exactly: for these values the frame definition Y 1101-1113 does not imply the comparison of Y 73382-73383. Every `gamma < e^{-1}` excludes it. So it shows that some added condition is needed. It does not show by itself that the condition must depend on `Bbar`: for `gamma < e^{-1}` the sequence is not a frame. The repair of wording for the note: state the range, and say that the dependence of a ceiling on `Bbar` is not shown by Example F alone (or add F(gamma) below once checked).

**(e) A frame of the same kind for every `gamma` (new here; proved by Claude Opus 5.5, not checked by another model).** The question of row 657 is whether such a frame exists for every `gamma` above some bound or only on the set of (d). Answer: for every `gamma` in `(0, e^{-1/2})`, once `Bbar` is large enough for that `gamma`. At fixed `(r, L, lambda, c_5, Bbar)`, that set is empty or an upper interval in `(0, e^{-1/2})`; in the latter case its supremum is `e^{-1/2}`. It contains no `gamma <= gamma_0` of Lemma G.

*Monotonicity in `gamma`.* `gamma` enters Y 1101-1113 only through the floor `theta_j >= gamma^{-2}` and through `0 < gamma < e^{-1/2}`. If `gamma <= gamma' < e^{-1/2}`, then `gamma'^{-2} <= gamma^{-2}`, so every frame for `gamma` is a frame for `gamma'`. Hence, with all other constants fixed, the set of `gamma` with a frame that breaks the comparison is empty or an upper interval in `(0, e^{-1/2})`. If nonempty, its supremum is `e^{-1/2}`; this endpoint is excluded. By Lemma G it contains no `gamma <= gamma_0(r, L, c_5, Bbar)`.

*Proposition F(gamma).* Let `r > 0`, `L >= 3` an integer, `lambda >= 0`, `c_5 >= 0` and `0 < gamma < e^{-1/2}`. Put `E_q = exp(L^{q/r})` for integers `q >= 1`, `s = L^{1/r} > 1` and `m = ceil(r)`. Let `q` be an integer with (i) `L^{q/r} >= log(gamma^{-2})` and (ii) `L^{q/r} >= 3 lambda m!/(s-1)`; and `L^{q/r} >= 1`. Put `n = L^q - 2` and `t = n + 3 = L^q + 1`, and
`theta_j = E_{q+2} - lambda j` for `0 <= j <= n`, `theta_{n+1} = E_{q+1}`, `theta_{n+2} = (E_q + E_{q+1})/2`, `theta_{n+3} = E_q`.
Then for every `Bbar >= E_{q+2}` this is a frame of length `t`, and `Rcheck_{h_t} = L^2 Rcheck_t` with `h_t = 1`.

Proof. Write `x = L^{q/r} >= 1`, so `log E_q = x`, `log E_{q+1} = s x`, `log E_{q+2} = s^2 x`, and `L^q = x^r`.
1. `R(E_q) = L^q`, since `(log E_q)^r = L^q` is a power of `L`. For `y` in `(E_q, E_{q+1}]`, `(log y)^r` lies in `(L^q, L^{q+1}]`, so `R(y) = L^{q+1}`. In the same way `R(y) = L^{q+2}` for `y` in `(E_{q+1}, E_{q+2}]`.
2. Gaps. For `y >= 0` and an integer `m >= 0`, `e^y >= y^m / m!` (one term of the series). With `e^{(s-1)x} - 1 >= (s-1) x`:
   `E_{q+1} - E_q = e^x (e^{(s-1)x} - 1) >= (s-1) x e^x >= (s-1) x^{m+1}/m! >= (s-1) x^{r+1}/m!`, the last step as `x >= 1` and `m >= r`. By (ii), this is at least `3 lambda x^r`.
   The map `g(y) = e^{sy} - e^y` increases for `y >= 0` (`g'(y) = s e^{sy} - e^y > 0`). So `E_{q+2} - E_{q+1} = g(sx) >= g(x) = E_{q+1} - E_q >= 3 lambda x^r`.
3. Drops. For `j < n`: `theta_j - theta_{j+1} = lambda`. At `j = n`: `theta_n - E_{q+1} = E_{q+2} - E_{q+1} - lambda n >= 3 lambda x^r - lambda (x^r - 2) >= lambda`. At `j = n+1` and `j = n+2`: each drop is `(E_{q+1} - E_q)/2 >= (3/2) lambda x^r >= lambda`. Every drop is at most `E_{q+2}`, since every member is positive and at most `E_{q+2}`. So, as in (a) item 3, the two-sided bound holds for every `Bbar >= E_{q+2}` and every `c_5 >= 0`.
4. Values of `R`. The drops are non-negative, so the running minimum is `theta_j`. For `j <= n`: `E_{q+1} < E_{q+1} + lambda <= theta_n <= theta_j <= E_{q+2}` when `lambda > 0`, and `theta_j = E_{q+2}` when `lambda = 0`; so `Rcheck_j = L^{q+2}`. `theta_{n+1} = E_{q+1}` and `E_q < theta_{n+2} < E_{q+1}`, so `Rcheck_{n+1} = Rcheck_{n+2} = L^{q+1}`. `Rcheck_{n+3} = L^q`.
5. Floor. The least member is `E_q = e^x >= gamma^{-2}` by (i).
6. `Rcheck_j <= L Rcheck_{j+1}`: the ratios are 1 except `L` at `j = n` and at `j = n+2`. These two drops are not consecutive.
7. `N_t = Rcheck_t = L^q`, so `h_t = t - L^q = 1`. As `L^q >= 3`, `1 <= n`, so `Rcheck_1 = L^{q+2} = L^2 Rcheck_t > L Rcheck_t`. ∎

Every number here is a closed expression; no step evaluates one. Since `q` depends on `gamma` through (i), the needed `Bbar >= E_{q+2}` grows as `gamma` decreases. Consequence: at fixed `(r, L, lambda, c_5)`, no ceiling on `gamma` that does not depend on `Bbar` makes the comparison hold for every `Bbar`. Lemma G gives one that does. This is the precise sense of "a ceiling on `gamma` fixed after `Bbar`".

## A.2 Lemma K

*Statement* (row 652). Assume the frame, (G), `L >= 13`, and `h = k - Rcheck_k >= 0`. Then the set of `i` with `a_i = u_k` is non-empty, and its last element `i*` satisfies `h+2 <= i* <= k-1`. So `k_0 = i* - 1` has `h < k_0 <= k-2`.

Here `a_i = M Rcheck_i L^i` (Y 63749: "set \(a_i=M\check R_iL^i\), the side of a level-\(i\) cell") and `u_k = M L^k` (Y 63774).

**(a) Steps.**
1. `e_i = i + log_L Rcheck_i` is an integer, since `Rcheck_i` is a power of `L`. `a_i = M L^{e_i}`, so `a_i = u_k` exactly when `e_i = k`. Right.
2. `Rcheck_k = L^p` with `p >= 1`. Source of this, (b) below. Right.
3. `Rcheck_{i+1}/Rcheck_i` is in `{1, L^{-1}}`. By (1) of Lemma W, `Rcheck_{i+1} <= Rcheck_i`; this uses that `m_j` is a running minimum and that `R` does not decrease, which holds because `(log y)^r` increases on `y > 1` for `r > 0` and every `m_j >= gamma^{-2} > 1`. By Y 1110, `Rcheck_{i+1} >= Rcheck_i / L`. Both are powers of `L`, so the ratio is `1` or `L^{-1}`. Then `e_{i+1} - e_i = 1 + log_L(ratio)` is `1` or `0`. Right.
4. `e_k = k + p >= k + 1`. Right.
5. `k - h = Rcheck_k = L^p >= L >= 2`, so `h + 2 <= k`. Right.
6. (S) at `i = h+2`. (S) needs `max(0, k - Rcheck_k) <= i <= k`, here `h <= h+2 <= k`. It gives `Rcheck_{h+2} <= L Rcheck_k = L^{p+1}`, so `e_{h+2} <= h + 2 + p + 1 = h + p + 3`. Then `e_{h+2} <= h + L^p = k` follows from `p + 3 <= L^p`. Right.
7. `p + 3 <= L^p` for all `p >= 1`: at `p = 1` it is `4 <= L`; if `p + 3 <= L^p`, then `p + 4 <= L^p + 1 <= L^{p+1}` because `L^{p+1} - L^p = L^p (L-1) >= 1`. Right.
8. Discrete intermediate value. Let `j` be the largest index in `[h+2, k]` with `e_j <= k`; it exists since `e_{h+2} <= k`, and `j <= k-1` since `e_k >= k+1`. Then `e_{j+1} >= k+1` and `e_{j+1} <= e_j + 1 <= k+1`, so `e_{j+1} = k+1` and `e_j = k`. By step 3, `e` does not decrease, so `{i : e_i = k}` is an interval; it contains `j` and not `j+1`, so its last element is `i* = j`, with `h+2 <= i* <= k-1`. The row's text says the same in two sentences. Right.
9. `k_0 = i* - 1` gives `h + 1 <= k_0 <= k - 2`. Right.

**(b) Where `Rcheck_k >= L` comes from.** Y 1102-1103: "\(\theta_0,\ldots,\theta_k\ge\gamma^{-2}\), with \(0<\gamma<e^{-1/2}\)". So `m_k = min_{i<=k} theta_i >= gamma^{-2} > e`, and `log m_k > 1`. Then `(log m_k)^r > 1` for `r > 0`. Y 1108 and 1113: `Rcheck_k = R(m_k)`, "the smallest power of \(L\) not below \((\log y)^r\)". A power of `L` that is at least a number above 1 is `L^p` with `p >= 1`. So `Rcheck_k >= L`. This uses only the floor, the range of `gamma` and the definition of `R`; it does not use (G).

**(c) The weakest condition on `L` that the proof needs.** Step 7 needs `p + 3 <= L^p` for every `p >= 1` that occurs; at `p = 1` this is `L >= 4`, and `L >= 4` suffices for all `p`. Step 5 needs `L >= 2`. Lemma W's own proof of (S) needs no bound on `L` beyond `L > 1`. So the proof needs `L >= 4`. Y's `L >= 13` (Y 650) is more than enough. The lemma's hypothesis "`L >= 13`" can be weakened to "`L >= 4`"; for the note, "`L >= 4`, which Y's `L >= 13` gives" is the exact form. ((G) is still used, in step 6 through (S).)

**(d) Which words of Y 63775-63778 it proves.** Y 63775-63778: "In the scale choice used for the preparation, let \(k_0+1\) be the last index with \(a_{k_0+1}=u_k\), with \(h<k_0\le k-2\). Thus \(a_i\le u_k\) up to \(k_0+1\), and \(a_i\ge Lu_k\) thereafter."

- "the last index with \(a_{k_0+1}=u_k\)": Lemma K proves that this index exists (the set is non-empty and, being an interval inside `[h+2, k-1]`, has a last element). Proved.
- "with \(h<k_0\le k-2\)": proved (step 9).
- "Thus \(a_i\le u_k\) up to \(k_0+1\)": for `i <= k_0 + 1`, `e_i <= e_{k_0+1} = k` because `e` does not decrease (step 3). So `a_i <= u_k`. Proved, for every `i` from `0` to `k_0+1`.
- "and \(a_i\ge Lu_k\) thereafter": for `i >= k_0 + 2`, `e_{k_0+2}` is `k` or `k+1` by step 3, and it is not `k` because `k_0 + 1` is the last index with value `k`. So `e_{k_0+2} = k + 1`, and `e_i >= k + 1` for all `i >= k_0 + 2` by monotonicity. So `a_i >= L u_k`. Proved, for every `i` from `k_0+2` to `k`.
- "In the scale choice used for the preparation": this names the choice `a_i = M Rcheck_i L^i` of Y 63749. Nothing to prove.

So Lemma K with the step property of step 3 proves every word of Y 63775-63778. The 'Thus' sentence uses only step 3 (the frame's `Rcheck_j <= L Rcheck_{j+1}` and the running minimum), not (G). The existence of `k_0` with `h < k_0` uses (G), through (S).

Text to add to Lemma K for the note: "Moreover `a_i <= u_k` for `i <= k_0 + 1` and `a_i >= L u_k` for `k_0 + 2 <= i <= k`," with the proof of (d).

**(e) Example F against Lemma K.** `e_i = i + log_13 Rcheck_i`: `e_10 = 10 + 3 = 13`, `e_11 = 11 + 2 = 13`, `e_12 = 12 + 2 = 14`, `e_13 = 13 + 1 = 14`, `e_14 = 14 + 1 = 15`. The last index with `e_i = 14 = k` is 13, so `k_0 = 12 = k - 2`, and `h = 1 < 12`. (W): `k - k_0 = 2 <= k_0 - h = 11`. The check's sentence "Example F breaks (S), not (W)" is right. Note that Example F does not satisfy (G) (it breaks (S)), so it is not an instance of Lemma K; it only shows that `k_0` can exist without (G).

**Verdict: Lemma K HOLDS.** Weakest condition on `L` for the proof: `L >= 4`.

## Section B: edits applied to `library/r7-count.md`

Copy before the edits: `/tmp/sn-w2/r7-count.before.md` (scratch). Seven edits, nothing else changed.

1. Section 1, quote of `Z_j^+`: "Y 78873" became "Y 78872-78873" (r7-repair-check section 8: "Put" is on Y 78872).
2. Section 1, healed components: "Y 62106" became "Y 62105" (section 8).
3. Section 2, (A2): the second "Y 62246" (the quote "The action regions are unions of coarse cubes") became "Y 62245" (section 8).
4. Section 4, frame paragraph: "(Y 72935)" became "(Y 72936)" (section 8), and the sentence "`Bbar >= 0`. (If a frame has `Bbar < 0` its upper bound also holds with 0 in place of `Bbar`.)" was added (section 3 (a)).
5. Section 4, "(G) is new; where it enters": the parenthesis with the numeric illustration (`r = 10`, `L = 13`, `Bbar = 10^6`) was replaced by the repair text of section 2 (Example F and Y 62001), word for word.
6. Section 4, after the proof of Lemma W: Lemma K with its proof (section 3 (b)), with the repair of A.2 above: hypothesis `L >= 4` in place of `L >= 13`, `k - h = L^p >= 4` in place of `>= 13`, the added sentence on `a_i <= u_k` and `a_i >= L u_k` with its proof, and one closing line on where `p >= 1` comes from.
7. Section 5, proof of Lemma C: the citation for `Omega_t` in (Y-STEP) was added: Y 61973 (quoted) and the display Y 61981-61985 (section 5).

Not applied, as the row says: the repairs of r7-repair-check section 7 (Remark I).

Found while editing, not changed (row 657: "Change nothing else"): the display cited as Y 61981-61985 begins at Y 61982 (Y 61981 is blank); the citation was applied as given; in section 1 of r7-count, the quote "\(\Omega^n_l=\Omega_l\), so that the entries make up the determining sequence" is on Y 62245, not Y 62246; the citation "(Y 62106, 62197)" in section 6 for the all-small-field label points at the island rule, while the healed rule is Y 62105.

## Section C: the note and the issue draft

Written: `library/scale-note.md` (Parts 1-3 and "What this note does not show") and `library/scale-note-issue.md` (title, greeting, 16 lines, link placeholder LINK-TO-NOTE). Nothing posted, no issue opened. Every quotation in the note was compared with my fetched copy of Y, `YM4_EM.tex` and `YM4_RT.tex` at c7fef8b21b58 (EM lines 448-452 and RT lines 1027-1033 are the one-step passages; RT's label line is 1032). Local check of the math syntax: every `$`` has its closing pair, the `math` fences are balanced, no raw `\(`, `\[`, `\emph` or `\cref` outside math. The render check through GitHub's markdown API was not run, because it sends the text off this machine; it is the lead's step.

Deviations from the row's wording, by decision of section A:
- The row asks the note to say Example F "shows that the comparison needs a ceiling on gamma that is fixed after Bbar". A.1 (d) finds that Example F alone shows only that some added condition is needed (every `gamma < e^{-1}` excludes it). The note says that, and says that Example F does not show that a ceiling independent of `Bbar` fails. The family F(gamma) of A.1 (e), which would show it, is not in the note: it is new and unchecked.
- The range is stated exactly: `Bbar >= e^{14} - e^5` (the round `e^{14}` is a subset), plus `c_5 >= 0`, `0 <= lambda <= 12`, `r = 2`, `L = 13`.
- The provenance line has one added sentence: Opus added the last sentence of Lemma K and its proof in this check, unchecked by another model.
- Lemma K's hypothesis is `L >= 4`, as A.2 (c) found.

## Note against `library/r7-count.md` (after section B), statement by statement

Places where the wording of a statement differs:

1. Frame constants. r7-count asserts `lambda = c_0/4 >= 0`, `c_5 = 2c_2 >= 0` and `Bbar >= 0` as facts with Y lines. The note states `lambda >= 0`, `c_5 >= 0`, `Bbar >= 0` as assumptions of the lemmas, and `r >= 2`, `L >= 13` odd from Y 62001, 650.
2. "(G) is new". r7-count: "(G) is not one of Y's conditions and does not follow from them". The note: "Your text does not state (G) or a condition that implies it." The note does not say "does not follow".
3. Example F. r7-count gives `lambda <= 12`, `Bbar >= e^{14}`, `e^{-1} <= gamma`, without `c_5 >= 0` or `gamma < e^{-1/2}`, and without the exact range or the limit of what it shows. The note gives all numbers, the exact range and the limit.
4. Lemma W, (W). r7-count: "For every operation of level `k` with window bottom `h` and index `k_0` as above". The note adds the hypothesis `h = k - Rcheck_k >= 0` and says Part 2 proves that `k_0` exists.
5. Corollary S. r7-count: "For every `t` with `h_t >= 0`" (frame and (G) from context). The note states "Assume the frame and (G)" in the corollary.
6. Lemma K. Same statement; the note splits it into two list items and its proof into ten numbered steps. r7-count's proof is compact and has the same steps.
7. Lemma C. r7-count: "For every admitted label through `k` and `1 <= j <= k`, `Lambda^a_j` and `Omega^a_j` are unions of level-`j` cells; every standing island or drop-out mark of level `s` is a union of level-`s` cells contained in `Z_s`." The note: "For every label reached by a history, and every level `l >= 1`", with a third clause (iii), action entries equal label entries outside active drop-out windows (taken from `library/r7-repair.md` (c)). r7-count gives the proof only as a pointer to `library/r7-repair.md` (c); the note gives it in full, with the two cases that r7-repair-check section 5 added (level `l = t` at a drop-out with `n = N_t`; a mark swallowed later).
8. Corollary C. r7-count has no statement of it (one sentence in the proof of Lemma C: "by Lemma C that case does not occur for the action sequence"). The note states Corollary C, with the reading of "those cubes".
9. Lemma G. Same statement and proof; the note writes out `y >= e > 1` and the positivity of the outer logarithm.
