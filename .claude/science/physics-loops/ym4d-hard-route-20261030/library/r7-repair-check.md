lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T02:53Z

# Check of the row 625 / row 648 parts of `library/r7-count.md`

FINISH row 652 (`r7-repair-check`). Provenance: Claude Fable 5.2, medium, one fresh session, pinned at commit 5aa905506; not an audit. I wrote Theorems A and B of the note (row 618) and none of the parts checked here, which Claude Opus 5.5 wrote (rows 625, 648). Same provider, different model.

Source: Y = YM4_1400.tex of Ethan Sussman and Levent Alpoge (written with Claude and Codex), commit 2bc0658f, the copy at `/tmp/ym4_1400.tex` (136,637 lines, sha256 222ef1bd...9f178). 'Y n' is line n. The geometry is theirs, after Balaban (CMP 119, 122). No computer run was made; every number below is checked by hand. Files read: `library/r7-count.md`, `library/r7-repair.md`, `library/r7-count-check.md`, and the Y lines cited.

Overlap: `grep` of `library/open-core.md` for r7-count, the rim count, `Z_j^+`, the ceiling (G) and Lemma C finds nothing. The FINISH rows on this item are 618, 625, 648 and this one (652), which says it is not a duplicate.

## Verdicts

| item | verdict | one line |
|---|---|---|
| (1) Corollary S against Y 73382-73383 | HOLDS | It is Y's statement, word for word, proved under (G). Y gives no reason for it. |
| (2) the ceiling (G) | HOLDS WITH REPAIR | (G) is not in Y and does not follow from the frame definition: section 2 gives a frame that Y 1102-1113 admits and that breaks Y's comparison. Y does invoke "`gamma` is small" for the one-step comparison (Y 62001), so (G) is one more ceiling of a kind Y already uses. Repair: replace the numeric illustration by the explicit frame, and cite Y 62001. |
| (3) Lemma G, Lemma W | HOLDS WITH REPAIR | Every step is right. Two additions: `Bbar >= 0` is used and must be stated; the existence of `k_0` with `h < k_0 <= k-2` (Y 63774-63777) is assumed, and it follows from (S) (Lemma K below). |
| (4) Lemma R, factor 81 | HOLDS | Each step checked. |
| (5) Lemma C | HOLDS WITH REPAIR | The five inputs match Y word for word. (Y-STEP) for `Omega_t` needs Y 61973 and the display Y 61981-61985, not only Y 62080. The induction is complete; I found no history with an action region that is not a union of cells. |
| (6) Corollary C | HOLDS | The first case of Y 1475-1477 always applies to the action sequence, given that "those cubes" are the level-`j` cells. |
| (7) Lemma I, Remark I | HOLDS WITH REPAIR | Lemma I is right. The claim about Y 84109 is right for `phi_j` as built, given tents anchored near their sites. Three repairs: the same failure occurs on the redone ring of a drop-out if `Lambda_j` of Y 83993 is the label entry; `Lambda^{a+}_j` is the collared integration region (Y 74835-74837), not `Lambda^a_j` plus islands; and RF30 takes "any set of these points" (Y 83995-83996), so only the sentence Y 84108-84109 needs a restriction. |
| (8) quoted passages | HOLDS | Ten passages compared; all texts agree with Y. Four line numbers are off by one. |

Nothing FAILS. Corollary S and Lemma C can go to the authors with the repairs of sections 2, 3 and 5.

## 1. Corollary S against Y 73382-73383

Y's text, Y 73376-73385: "Its carriers are in the enlargements of older islands or of strips of levels at most \(h_t=t-\mathsf N_t\), where \(\mathsf N_t\) is the number of preparatory stages. The stored bonds are in the inner core. The enlargement costs at most one cell of level \(h_t\), and the next two shells have widths at least \(M\check R_t\xi_{h_t}\) and \(LM\check R_t\xi_{h_t}\). The scale comparison \(\check R_{h_t}\le L\check R_t\) therefore puts every carrier inside \(Z''_{h_t+2}\)."

Definitions. `h_t = t - N_t` (Y 73378). `N_j = Rcheck_j`: "The waiting depth is \(\mathsf N_j=\check R_j\)" (Y 1121). `Rcheck_j = R(min_{i<=j} theta_i)`, "where \(R(y)\) is the smallest power of \(L\) not below \((\log y)^r\)" (Y 1108-1113).

Y's reason: none. The sentence names "the scale comparison" as known. The comparisons Y states elsewhere are all between neighbouring levels: `Rcheck_j <= L Rcheck_{j+1}` in the frame definition (Y 1110); `Rcheck_j/Rcheck_{j+1} ∈ {1, L}` (RF29, Y 83974, "The third uses the running minimum and the bounded one-step drop", Y 83981-83982); "\(R_{j+1}/R_j\in\{1,L^{-1}\}\), and two size drops are not consecutive" (Y 73081-73082); `L Rcheck_{h+1} >= Rcheck_h` (Y 128555, 134421). The levels `h_t` and `t` are `Rcheck_t >= L` apart, so none of these gives it.

Corollary S is the same statement: for every `t` with `h_t >= 0`, `Rcheck_{h_t} <= L Rcheck_t`. It is proved under (G), a condition Y does not state. (S) of Lemma W is stronger in range: it gives `Rcheck_i <= L Rcheck_t` for every `i` in `[h_t, t]`.

## 2. The ceiling (G)

**Form.** For all `y >= gamma^{-2}`: `(log(y + c_5 + Bbar L (log y)^r))^r <= L (log y)^r`. It depends on `r, L, c_5, Bbar` and holds for `gamma <= gamma_0(r, L, c_5, Bbar)` (Lemma G, section 3).

**Is it in Y?** No. I searched Y for conditions on `gamma`: Y 1102-1103 (`0 < gamma < e^{-1/2}`), the order and the kinds of condition at Y 72905-72946, the class hypothesis "all \(g_j\le\gamma\)" (Y 72899), RF29 (Y 83964-83984), and every line with `\gamma\le`, `\gamma<`, "ceiling on `gamma`". No line states (G) or a condition that implies it. Two lines show that Y does lower `gamma` after the drift constants for this purpose:

- Y 62001: "Moreover \(\check{R}_k\le L\check{R}_{k+1}\), and two consecutive drops never occur, because \(x\) changes by \(O(1)\) per step and \(\gamma\) is small."
- Y 72946: "A representative condition on \(M\) or on \(\gamma\) asserts that \(e^{-cM}\), \(e^{-c\check{R}_k}\) or a power of \(\log x_k\) dominates constants fixed earlier", and the supremum form "\(\sup_{x\ge\gamma^{-2}}h(x)\le c\)".

Y 62001 is a ceiling on `gamma` for a drift of one or two steps; its exact form is not written. (G) is the same kind of ceiling for a drift of one window, `Rcheck_t` steps. So (G) is new as a stated condition, and it fits Y's order at `gamma` (`(lambda, c_5, Bbar) ≺ gamma`, Y 72931). RF29's first line (Y 83972) gives `theta_m <= (1+beta_0)^2 (n-m) theta_n` above a floor; over a window this still leaves `log theta_{h_t} <= log theta_t + log((1+beta_0)^2 Rcheck_t)`, and the comparison then needs one more floor on `theta`. So RF29 does not give it either.

**Is a new condition needed? Yes: the frame definition alone admits a frame that breaks Y's comparison.**

*Example F.* Constants: `r = 2`, `L = 13`, `0 <= lambda <= 12`, `c_5 >= 0`, `Bbar >= e^{14}`, `e^{-1} <= gamma < e^{-1/2}`. Frame of length `k = 14`:
`theta_j = e^{14} + lambda (10 - j)` for `0 <= j <= 10`, `theta_11 = e^5`, `theta_12 = e^4`, `theta_13 = e^3`, `theta_14 = e^2`.

Check of Y 1102-1110, using only `2.7 < e < 3`.
- Floor: `theta_j >= e^2 >= gamma^{-2}`.
- Each one-step drop `theta_j - theta_{j+1}` is at least `lambda` and at most `Bbar`: it is `lambda` for `j < 10`; `e^{14} - e^5`, which lies between 12 and `e^{14}`, for `j = 10`; and `e^5 - e^4`, `e^4 - e^3`, `e^3 - e^2` after that, each at least `e^2 (e-1) > 7.29 * 1.7 > 12` and less than `e^{14}`. Summing the steps from `i` to `j` gives `lambda (j-i) - c_5 <= theta_i - theta_j <= Bbar (j-i)`.
- `theta` decreases, so `min_{i<=j} theta_i = theta_j`. With `r = 2`: `R(y) = 13` when `1 < (log y)^2 <= 13`, `R(y) = 169` when `13 < (log y)^2 <= 169`, `R(y) = 2197` when `169 < (log y)^2 <= 2197`. For `j <= 10`: `e^{14} <= theta_j <= e^{14} + 120 <= e^{15}` (as `120 <= e^{14}(e-1)`), so `196 <= (log theta_j)^2 <= 225` and `Rcheck_j = 2197`. `(log theta_11)^2 = 25`, `(log theta_12)^2 = 16`: `Rcheck_11 = Rcheck_12 = 169`. `(log theta_13)^2 = 9`, `(log theta_14)^2 = 4`: `Rcheck_13 = Rcheck_14 = 13`.
- `Rcheck_j <= L Rcheck_{j+1}` holds at every `j` (the ratios are 1, except 13 at `j = 10` and `j = 12`). The two drops are not consecutive, so Y 73081-73082 and Y 62001 hold as well.

At `t = 14`: `N_14 = 13`, `h_14 = 1 >= 1`, `Rcheck_{h_14} = 2197 = 13^2 Rcheck_14 > L Rcheck_14 = 169`. Y's comparison fails. ∎

So the step that needs (G) is step (4) of Lemma W: the passage from `theta_i <= m_t + c_5 + Bbar Rcheck_t` to `(log m_i)^r <= L (log m_t)^r`. Example F is excluded by any ceiling `gamma < e^{-1}`; it shows only that the frame definition is not enough, and that the ceiling must come after `Bbar`. (G) is sufficient. I did not look for the weakest sufficient condition.

**Repair text for the note** (in "(G) is new; where it enters", replace the parenthesis "(check, item 7: `r = 10` ... near `13^12`)" by): "(Example F of `library/r7-repair-check.md`, section 2: with `r = 2`, `L = 13`, `lambda <= 12`, `Bbar >= e^{14}`, `e^{-1} <= gamma`, the frame `theta_j = e^{14} + lambda(10-j)` (`j <= 10`), `e^5, e^4, e^3, e^2` satisfies all of Y 1102-1110 and has `Rcheck_{h_14} = 13^2 Rcheck_14`.) Y lowers `gamma` after the drift constants for the one-step comparison (Y 62001: 'two consecutive drops never occur, because `x` changes by `O(1)` per step and `gamma` is small'); (G) is the same kind of ceiling for one window." The old illustration bounds `theta_{h+1}` only and does not exhibit a frame.

## 3. Lemma G and Lemma W, step by step

**Lemma G.** `y >= y_0 >= e`, so `u = y^{1/(2r)} > 1` and `0 < log u <= u`. `(log y)^r = (2r log u)^r <= (2r)^r u^r = (2r)^r y^{1/2}`. `Bbar L (2r)^r y^{1/2} <= y/2` is `y^{1/2} >= 2 Bbar L (2r)^r`, true as `y >= 4 (Bbar L (2r)^r)^2`. `c_5 <= y/2` as `y >= 2 c_5`. So the argument of the outer logarithm is between `y` and `2y` (it is at least `y > 1` because `c_5 >= 0`, `Bbar >= 0`). `log(2y) <= L^{1/r} log y` is `(L^{1/r} - 1) log y >= log 2`, true as `y >= 2^{1/(L^{1/r}-1)}` and `L^{1/r} > 1`. Both sides are positive; raise to the power `r`. For `gamma <= y_0^{-1/2}` every `y >= gamma^{-2}` is at least `y_0`. HOLDS.

**Lemma W.**
- (1) `m_j` is a running minimum; `R` is non-decreasing because `(log y)^r` increases for `y > 1`, `r > 0`. HOLDS.
- (2) Lower frame bound with `lambda >= 0` (Y 72936). HOLDS.
- (3) For `t - Rcheck_t <= i <= t`: `m_i <= theta_i <= theta_t + Bbar (t-i) <= theta_t + Bbar Rcheck_t <= m_t + c_5 + Bbar Rcheck_t`. The third inequality uses `Bbar >= 0`. `Rcheck_t < L (log m_t)^r`: `m_t >= gamma^{-2} > e` gives `(log m_t)^r > 1`, so the least power `L^p` not below it has `p >= 1` and `L^{p-1} < (log m_t)^r`. HOLDS.
- (4) `log m_i > 0`, so `(log m_i)^r <= (log(m_t + c_5 + Bbar L (log m_t)^r))^r <= L (log m_t)^r <= L Rcheck_t` by (3) and (G) at `y = m_t`. `L Rcheck_t` is a power of `L`, so `R(m_i) <= L Rcheck_t`. HOLDS. This is the only use of (G).
- (5) `a_{k_0+1} = u_k` is `M Rcheck_{k_0+1} L^{k_0+1} = M L^k`, so `Rcheck_{k_0+1} = L^{k-k_0-1}`. With `h+1 <= k_0+1 <= k`, (1) and (S) give `L^{k-k_0-1} <= Rcheck_{h+1} <= L^{p+1}`, so `k - k_0 <= p+2`. `k - h = L^p`. `2(p+2) <= L^p`: at `p = 1`, `6 <= L`; and `2(p+3) = 2(p+2) + 2 <= L^p + L^p <= L^{p+1}`. Then `2(k-k_0) <= k-h`. HOLDS.

**Two additions (repair text).**

(a) In the frame paragraph of section 4 add: "`Bbar >= 0`. (If a frame has `Bbar < 0` its upper bound also holds with 0 in place of `Bbar`.)"

(b) Lemma W takes `k_0` from Y 63774-63777, which asserts "\(k_0+1\) be the last index with \(a_{k_0+1}=u_k\), with \(h<k_0\le k-2\)" without proof. Under (S) it exists:

*Lemma K.* Assume the frame, (G), `L >= 13`, and `h = k - Rcheck_k >= 0`. Then the set of `i` with `a_i = u_k` is non-empty, and its last element `i*` satisfies `h+2 <= i* <= k-1`. So `k_0 = i* - 1` has `h < k_0 <= k-2`.

Proof. Write `a_i = M L^{e_i}`, `e_i = i + log_L Rcheck_i`, and `Rcheck_k = L^p`, `p >= 1`. By (1) and the frame's `Rcheck_i <= L Rcheck_{i+1}`, `Rcheck_{i+1}/Rcheck_i ∈ {1, L^{-1}}`, so `e_{i+1} - e_i ∈ {1, 0}`. `e_k = k + p >= k+1`. `k - h = L^p >= 13`, so `h+2 <= k`, and (S) at `i = h+2` gives `e_{h+2} <= h + 2 + p + 1 <= h + L^p = k`, because `p + 3 <= L^p` (at `p = 1`: `4 <= L`; and `p + 4 <= L^p + 1 <= L^{p+1}`). An integer sequence that moves by steps 0 or 1 from a value `<= k` at `h+2` to a value `>= k+1` at `k` takes the value `k` at some `i` in `[h+2, k-1]`; the indices with `e_i = k` form an interval, and its last element is below `k`. ∎

In Example F: `e_11 = 13`, `e_12 = e_13 = 14 = k`, `e_14 = 15`, so `k_0 = 12 = k - 2` exists there too, and (W) holds there (`k - k_0 = 2 <= k_0 - h = 11`). Example F breaks (S), not (W).

## 4. Lemma R and the factor 81

- `y ∉ B_j` means: the cell of `y`, or a cell touching it, is not contained in `Lambda^a_j`. Call it `c'`. By Lemma C `Lambda^a_j` is a union of level-`j` cells and the cells partition the torus, so `c' ⊂ Z^a_j`. The cell of `y` equals or touches `c'`, so it lies in `(Z^a_j)^≈`. HOLDS.
- A cell of the cubic grid in four dimensions has at most `3^4 = 81` cells equal to or touching it (offsets in `{-1, 0, 1}^4`; fewer on a small torus). Each cell of `(Z^a_j)^≈` is assigned to one cell of `Z^a_j` that it equals or touches, so at most 81 cells go to one cell. All cells have `(M Rcheck_j)^4` level-`j` sites. So `#_j((Z^a_j)^≈) <= 81 #_j(Z^a_j)`. HOLDS.
- `sum_j #_j(Z^a_j) <= L^4/(L^4-1) sum_n #_n(Gamma^a_n)` is Steps 2 and 3 of Theorem A, which use (A1), (A2) only. `sum_n #_n(Gamma^a_n) <= 35410 sum_n #_n(Gamma_n)` is inside the proof of Theorem B (inputs (Q), (W)). HOLDS.
- The rim bound: every `y ∉ B_j` is counted, including the sites of `Z^a_j` whose terms vanish. The per-term bound is Y 84110, used as stated.

## 5. Lemma C

**Inputs against Y.**
- (Y-STEP), copy part. Y 62174: "At a step, the earlier entries and standing marks are copied." Agrees. Also Y 63718: "A step leaves earlier entries alone".
- (Y-STEP), cell part. Y 62080: "Every large-field region and every creation set is a union of cells of its own level. Both statements hold for the regions that the steps produce (119, p. 256)." This gives `Z_t`, hence `Lambda_t`. It does not name `Omega_t`. **Repair:** cite for `Omega_t` the construction itself, Y 61973 ("Hulls (\('\), \(\widehat{\cdot}\)) and layers are taken in level-\(t\) cells") with the display Y 61981-61985: `Omega_t^c = Q_t'^{~2} ∪ P_t'^{~4} ∪ H_t`, `H_t = \hat{Y}^{~8}` (`t >= 2`) or `P_0'^{~5}` (`t = 1`, "the level-one hull", Y 61974). Each set is a hull in level-`t` cells with layers of level-`t` cells added, so `Omega_t^c` and `Omega_t` are unions of level-`t` cells. The same display gives `Z_t` as the final `Z^{[n]}`, built from these sets, cells of failures and the boxing map, which replaces a component by its bounding box. So (Y-STEP) can be read off Y's construction and does not rest only on the citation of Balaban.
- (Y-FATE). Y 63684 (class components are components of `Z_k`), Y 62105-62107 with the display Y 62110-62115 (the three fates), Y 62175-62177: "At an operation, a healed component or an island overwrites the older entries on its region, and any mark it swallows ceases to stand. Outside the class no entries change." Agrees.
- (Y-WAIT). Y 62128: "\emph{Marks wait}: a mark of level \(s\) lying inside a class component of level \(t\) satisfies \(s<t_\flat\). Hence standing marks that share a part are nested, their windows \((s_\flat,s]\) are disjoint, and at any one place and level at most one drop-out mark is active." Agrees.
- (Y-NEST). Y 62001: "Because it is a power of \(L\), all partitions are nested." Y 73081-73083: "\(R_{j+1}/R_j\in\{1,L^{-1}\}\), and two size drops are not consecutive. Thus a passage between levels either coarsens these cells by \(L\), or leaves their physical partition unchanged." Agrees. The grids are compatible by Y 73066 ("The torus and all partitions are chosen compatibly").
- (Y-LAB). Y 73087-73092: `Lambda_j ⊂ Omega_j`, `Omega_{j+1} ⊂ Lambda_j`, `Z_j = Lambda_j^c`. Agrees; `Z_s ⊂ Z_t` for `s <= t` follows.
- Reading (K). Y does not define "component". Its use fits (K): "two regions made of level-\(t\) cells that do not touch are separated by at least one cell" (Y 62195), and closed cells (Y 73068-73069). Under (K) two distinct components of a union of closed cells are disjoint, and a connected subset that meets a component lies in it. This is a reading, labelled as such in the log; I agree with it.
- The action sequence. Y 62121 and the display Y 62124-62125, Y 1181-1197 ("A drop-out \(C\) records its former regions \(\Omega_l^\circ\cap C\) ... Outside the affected levels retain the label regions ... Standing marks record the analogous \(\Lambda_l,S_l\) data"). Agrees with clause (iii).

**The induction.** A history is step 1, operation 1, step 2, operation 2, and so on (Y 1183: an operation of level `t` needs `t_flat >= 0`; Y 63684 asks `k_flat >= 1`). Checked case by case.
- Step `t`: new entries are unions of level-`t` cells; every standing mark has level at most `t-1`, so no window reaches level `t`; action = label at level `t`. Right.
- Operation `t`, the preliminary claim. A standing mark `X'` of level `s` that meets a class component `X` lies in `X`: `X' ⊂ Z_s ⊂ Z_t`, `X'` is connected, `X` is a component of `Z_t`. Marks of level `t` are other components of the same class and are disjoint from `X`. Then `s < t_flat` by (Y-WAIT), and the window of `X'` is inside `(s_flat, s]`, below `t_flat`. So on `X`, at levels `t_flat < l <= t`, label entry = action entry before the operation. Right.
- Healed: on `X` the new entries are `X` at every `l <= t` and every mark in `X` ceases to stand (also Y 74830-74831: "all marks in \(X\) removed, including its own"), so action = label = `X` there; outside `X` nothing changes. `Lambda^a_l ∪ X` is a union of level-`l` cells. Right.
- Island: as healed for `l < t` and for `Omega_t`; `Lambda_t` unchanged, and `Lambda^a_t = Lambda_t` on `X` by the preliminary claim. Right.
- Drop-out after `n` stages: label entries change on `X` at `t_flat < l <= t_flat + n` only. Action entries there are `Omega°_l`, `Lambda°_l`, the label entries before the operation, equal to the old action entries by the preliminary claim. Older marks inside `X` keep standing with their own stored regions at their own, lower, windows. So the action sequence is unchanged. Right.
- **`l = t` at a drop-out with `n = N_t`** (Y 62169-62171: "At \(l=s\) the drop-out keeps \(q\) outside \(\Lambda_s\)"; Y 62115: "so \(\Lambda_t\cap X=\emptyset\)"). The window reaches `l = t`. `Omega^a_t ∩ X = Omega°_t = Omega_t(old) ∩ X`, a union of level-`t` cells by the step. `Lambda^a_t ∩ X = Lambda°_t = Lambda_t(old) ∩ X = ∅`, since `X ⊂ Z_t`. This agrees with `Z^a_s = Z_s` (Y 73140). Right.
- **A drop-out whose mark is swallowed later.** Let `X` be a drop-out of level `t`, and let a healed component or island `X''` of level `t' > t` meet it. Then `X ⊂ X''` (as above), the mark ceases to stand, and the entries on `X''` are overwritten by `X''` at `l <= t'` (island: `l < t'` and `Omega_{t'}`). After that no mark stands in `X''`, so action = label on `X''`, a union of cells. The stored regions of `X` are discarded with the mark. If instead `X''` is a later drop-out containing `X`, the mark of `X` keeps standing; the window of `X''` is above `t`, where `Lambda_l ∩ X = ∅` already, and the action entries are unchanged. Right.
- Clause (ii) persists: a later heal or island either contains a mark (and swallows it) or is disjoint from it; a later drop-out changes entries only above the mark's level.

**Attempts to build a history with an action region that is not a union of cells of its level.** (a) A healed `X` of level `t` adjoined at `l < t`: a union of level-`l` cells by (Y-NEST). (b) The late prepared boxes `Z''_i`, `i > k_0`, which are only unions of `M`-cubes (Y 63805-63809): they enter the label entries of a drop-out, never its stored regions. (c) A step after a drop-out: the step reads `Z_t` of the label and writes level `t+1` only. (d) A later region that covers a healed place again (Y 62195: "the recursion is not monotone"): it is a step region of the later level. (e) Nested drop-outs: windows are disjoint by (Y-WAIT), each stores step-made or healed-made entries. (f) An island swallowing a drop-out, at `l = t`: `Lambda_t` unchanged, no window at level `t`. None gives a counterexample. The statement would fail only if (Y-WAIT) failed, that is, if a class component could contain a mark of level in `[t_flat, t)`; Y excludes this by the quarantine condition (Y 63684, third condition).

Verdict: HOLDS WITH REPAIR (the citation for `Omega_t`). Lemma C stays an implication from Y's rules as stated: (Y-WAIT), (Y-FATE) and reading (K) are not rebuilt.

## 6. Corollary C against Y 1475-1477 and Y 1462

Y 1462: "The profiles use the small-field regions of the action sequence." Y 1475-1477: "At level \(j\), put \(\mathsf s_j=M\check R_j\) when \(\Lambda_j\) is a union of those cubes, and \(\mathsf s_j=M\) otherwise. The latter region is a union of \(M\)-cubes."

By Lemma C, `Lambda^a_j` is a union of level-`j` cells for every admitted label and every `j`, including the cases `Lambda^a_j = T` and `Lambda^a_j = ∅`. So the first case always applies, `s_j = M Rcheck_j`. One reading step: "those cubes" has no antecedent in Y 1475 other than the size `M Rcheck_j`; I read it as the level-`j` cells of the fixed grid (Y 62096: creations "are \(M\check{R}_t\)-cubes of level \(t\)"; Y 73081: "The partitions have cell side \(b_j^{\rm cell}\)"). HOLDS.

## 7. Lemma I and Remark I

**Lemma I: HOLDS.** A standing island `I` of level `j` has `Lambda_j ∩ I = ∅` (Y 62106). If a standing drop-out mark `X'` of level `t'` had an active window containing `(x, j)` with `x ∈ I`, then `j <= t'`. `t' = j`: `I` and `X'` are two components of the class of level `j`, disjoint. `t' > j`: at operation `t'`, `I` stands and meets the class component `X'`, so `I ⊂ X'` and `j < t'_flat` by (Y-WAIT), outside the window. So `Lambda^a_j ∩ I = ∅`, `D_j = 0` on `I`, and `phi_j = 0` on `I` (Y 1489-1490).

**The two readings of Y 84108-84109** ("For the actual profile \(\varphi_j\), \(\varphi_jh_z=h_z\) at every base point", base points defined at Y 83993-83995 as "the unit sites lying one layer of \(M\check R_j\)-cells inside" `Lambda_j^+`, "\(\Lambda_j\) together with its level-\(j\) islands").

*Reading D (`phi_j` as Y builds it: from `Lambda^a_j`, Y 1462, 1475, 62128).* Then the sentence is false, in this exact form. Let `p` be a plaquette with `phi_j(p) < 1`. By `sum_y h_y(p) = 1` (Y 95875) some `y` has `h_y(p) > 0`, and `phi_j h_y ≠ h_y` at `p`. So Y 84109 holds if and only if every tent that is non-zero at a plaquette with `phi_j < 1` belongs to a non-base site. Take a standing level-`j` island `I`. It has at least 21 cells per side (Y 63768-63769), so its central plaquette `p` is at distance at least `9 M Rcheck_j` (level-`j` units) from every site outside the one-cell inset of `I`. `phi_j(p) = 0`. A tent with `h_y(p) > 0` has `|x(p) - x(p_y)| <= C_h M` (Y 95876). So if every anchor satisfies `|x(p_y) - y| < (9 Rcheck_j - C_h) M`, that `y` is a base point inside `I`, and Y 84109 fails at it. Y fixes no relation between `y` and its anchor (Y 95874: "anchors \(p_y\in P_K\)"), so the failure is proved under this condition on the anchors, which every tent family centred near its sites satisfies. The note's wording "a base point inside an island whose tent meets the island" is right.

*Reading P (`phi_j` built from `Lambda_j^+`).* Then `phi_j = 1` one cell layer inside `Lambda_j^+` (Y 1494-1495), and Y 84109 holds at every base point whose tent stays in that set. This reading contradicts Y 1475 (`D_j = dist_∞(x, Lambda_j^c)`) and gives the island the weight `x_j` in place of `x_{j-1}` in `x_k(.) = beta - sum_j b_j phi_j` (Y 62212). No line of Y supports it.

So the claim of Remark I is right: under the reading Y's text fixes, Y 84109 fails at island base points; it holds only under reading P.

**Three repairs to Remark I and to the log (d).**

(a) *Drop-out rings.* Y 83989-83993 speaks of "an admitted label" and "the determining sequence", so `Lambda_j` at Y 83993 may be the label entry. On an active drop-out mark `X` with `h < j <= min(k_0, h+n)`, `j < t`, the label entry is `Lambda_j ∩ X = X \ Z''_j(X) = X \ H_j^{[3a_j]}` (Y 62112, 63799), while the action entry is `Lambda°_j = X \ G_j = X \ H_j^{[10a_j]}` (Y 63761). The ring `H_j^{[10a_j]} \ H_j^{[3a_j]}` is seven cells wide, lies in `Lambda_j` and in `Z^a_j`, and its one-cell inset contains base points of the label reading, where `phi_j = 0`. So in that reading Y 84109 fails there too. Lemma R is not affected: these sites are not in `B_j` and are counted in `(Z^a_j)^≈`. Text to add to Remark I: "The same holds on the redone ring `Z^a_j \ Z''_j(X)` of an active drop-out mark if `Lambda_j` at Y 83993 is read as the label entry; `B_j` excludes it and Lemma R counts it."

(b) *`Lambda^{a+}_j`.* The log (d) and the check (row 625, side remark) suggest that `Lambda^{a+}_j` might be `Lambda^a_j` with islands, or that building `phi_j` from it would repair Y 84109. Y 74833-74837 uses `Lambda_j^{a+}` as "the action region and collared integration region of \eqref{hi:action-sequence}", the second argument of `N^{(j-1)}(Omega, Lambda)`, whose count is "the nonpivot integration bonds of level \(j\)" (Y 74849). So `Lambda^{a+}_j` is `Lambda^a_j` with its collar of integration bonds, not with islands. The suggestion has no support in Y and should be dropped. Remark I in the note does not use it.

(c) *What to call it.* RF30's first line is stated for "any set of these points" `𝖸` (Y 83995-83996). So RF30 itself needs no change: one applies it with `𝖸 ⊂ B_j`. Only the sentence Y 84108-84109 is too wide. Text for Remark I, replacing "This is a defect of Y's wording at Y 83993-83994, not a wrong reading": "RF30 allows any set `𝖸` of base points (Y 83995-83996), so it is applied with `𝖸 = B_j`. The sentence Y 84108-84109 then holds for base points in `B_j` (given the tent fit) and not for the base points inside islands."

The tent fit at the points of `B_j` (log (d), last paragraph) rests on the same open input: the position of the anchor. I did not check it further; it is not needed for the count.

## 8. Quoted passages compared with Y

| passage | where quoted | result |
|---|---|---|
| Y 83989-83991, "For the field estimate fix an admitted label through \(k\) ..." | note, section 1 | agrees |
| Y 78873, "Put \(Z_j^+=((\Lambda_j^{\mathsf a})^c)^\sim\)" | note, section 1 | agrees; "Put" is on Y 78872 |
| Y 73133-73141, the action sequence display | note, section 1 | agrees |
| Y 62128, "The choice \(\boldsymbol\nu=0\) gives the action sequence ..." and "Marks wait ..." | note, log | agrees |
| Y 62106, "Healed (every test passed): ..." | note, section 1 | text agrees; the line is Y 62105 (the island is Y 62106, the drop-out Y 62107 with display Y 62110-62115) |
| Y 62245-62246, "\(\Omega^{\boldsymbol\nu}_l\) is a region for \(\pi_l\)", "The action regions are unions of coarse cubes" | note (A2), log (c) | agrees; both are on Y 62245 |
| Y 63684, the class conditions | note (Q3), log | agrees |
| Y 62174-62177, "At a step, the earlier entries ... Outside the class no entries change." | log (c) | agrees |
| Y 1475-1477, `s_j` | log (c), note | agrees |
| Y 73382-73383, the scale comparison | note, Corollary S | agrees |
| Y 84108-84110 | note, section 5 | agrees |

Also: `c_5 = 2 c_2` is Y 72936, not Y 72935; `L >= 13` is Y 650; `N_j = Rcheck_j` is Y 1121; the display of `Omega^nu` is Y 62124-62125.

## Open after this check

1. (G) is an added condition. Y's own ceiling behind Y 62001 is not written, so whether Y's authors intend a ceiling that already covers one window is a question for them.
2. Lemma C rests on Y's rules as stated: (Y-WAIT), (Y-FATE), reading (K). Not rebuilt.
3. The anchor position of the tents (Y 95874-95876), which decides the tent fit at `B_j` and the exact extent of the failure of Y 84109.
4. Not in this item, unchanged from the note: (Q) and Y 63684-63835 used as stated; Y 84113-84114 unexplained.

RESULT: All eight items hold; none fails. Corollary S is Y's comparison `Rcheck_{h_t} <= L Rcheck_t` (Y 73382-73383, stated by Y with no reason) and is proved under (G); (G) is not in Y and is needed beyond the frame definition, shown by an explicit frame (Example F: `r = 2`, `L = 13`, `Bbar >= e^{14}`, `gamma >= e^{-1}`) that satisfies Y 1102-1110 and has `Rcheck_{h_t} = L^2 Rcheck_t`; Y itself uses "`gamma` is small" for the one-step comparison (Y 62001). Lemma G, Lemma W, Lemma R (factor 81), Lemma C, Corollary C and Lemma I are right step by step. Repairs, given as text: state `Bbar >= 0`; prove the existence of `k_0` (Lemma K, new here); cite Y 61973 and Y 61981-61985 for `Omega_t` in (Y-STEP); replace the numeric illustration of (G) by Example F; in Remark I add the drop-out ring, drop the `Lambda^{a+}` suggestion, and say that RF30 is applied with `𝖸 = B_j`. Open: (G) remains an added condition; Lemma C rests on Y's marks-wait and fate rules as stated; the tent anchor position behind Y 84109.
