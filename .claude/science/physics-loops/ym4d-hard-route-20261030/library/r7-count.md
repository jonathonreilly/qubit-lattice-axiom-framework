lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T10:29Z

# R7-COUNT: the rim count `sum_j #_j(Z_j^+) <= C sum_n #_n(Gamma_n)`

FINISH row 618, registry row R7-COUNT, root R7 (AGE), step G3 of `library/t0-approach.md`.

Kind of result: proof of a step that Sussman and Alpoge's text (YM4_1400, written with Claude and Codex; cited as Y with line numbers) states as needed and does not prove. The geometry is theirs, after Balaban (CMP 119, 122). Proved by Claude (Fable 5.2, medium); checked line by line by Claude Opus 5.5 high (row 625, `library/r7-count-check.md`). No computer run; all arithmetic is displayed.

Revised 2026-11-10 by Claude Opus 5.5 high (FINISH row 648, log `library/r7-repair.md`), by the verdict of the check: section 4 (the window inequality (W) from the ceiling (G); the lead's lemma, row 618) and section 5 (the rim, Lemma R; with Lemma C, which proves input (C), and Remark I on islands) are new; (SV) is removed; (Q3) holds at every window level. Sections 4 and 5 carry the check's proofs, which have been checked once (row 625); Lemma C and Remark I are new in row 648 and are not checked.

Overlap check: `grep` of `library/open-core.md` for the rim count, `Z_j^+` and R7-COUNT finds nothing. The only rows are FINISH 618 and registry R7-COUNT (this item).

## Verdicts

1. **Reading.** Y uses the count on a fixed label, not on a history. `Z_j^+` is a function of the label's action sequence.
2. **Label reading, action layers: proved (Theorem A), with `C_A = 81 L^4/(L^4-1)`.** Inputs: nesting and alignment of the action sequence, and a one-layer enlargement on the grid of the region. No property of healed components is used.
3. **Label reading, determining layers** (the `Gamma_n` of Y 83989 are the label's own entries, which are the determining sequence): **proved (Theorem B)**, with `C = C_A * 35410 = 81 L^4/(L^4-1) * 35410`, a function of `L` alone. The two sequences differ only on drop-out marks. Inputs: the quiet-box geometry of Y 63748-63835 (Q), with the small-box cutoff at every level of the window (Y 63684), and the window inequality (W): `2 (k - k_0) <= k - h`. (W) is proved in section 4 (Lemma W) from Y's frame conditions and one new ceiling (G) on `gamma`, which is not in Y and fits Y's order of constants at `gamma`.
4. **History reading: false.** The lead's history (section 6) is a counterexample with ratio `c L^{4(k-j)}`. Y does not use this reading. The healed collars are not in `Z_j^+` of the output label (Y 101134-101136), and Y pays them by the activity of their own operation (Y 78815-78825, 101129-101131).
5. **The use at Y 84116-84125:** the rim part of the net regular action is at most `C' sum_n #_n(Gamma_n)` (section 5, Lemma R). The rim is `Rcheck_j` layers of `M`-cubes deep, not one; it is counted on the cell grid, which needs (C): `Lambda^a_j` is a union of level-`j` cells. (C) is proved from Y's update rules (Lemma C). Base points inside islands (Y 83993) do not fit the profile as Y builds it (Remark I); the count is the same in either reading. The other parts of `E_k` rest on RF30, which is not this item.
6. **Corollary S:** the scale comparison `Rcheck_{h_t} <= L Rcheck_t` that Y uses without proof at Y 73382-73383 holds under (G).

## 1. Which regions are on the left side

Quotes that fix the reading.

- Y 83989-83991: "For the field estimate fix an admitted label through \(k\), with layers \(\Gamma_n=\Omega_n\setminus\Omega_{n+1}\), \(\Omega_0=T_\ell\) and \(\Omega_{k+1}=\emptyset\)."
- Y 78872-78873: "Put \(Z_j^+=((\Lambda_j^{\mathsf a})^c)^\sim\)." Y 84038-84040: "\(Z_j^+\) is the stored large-field region enlarged by one cell layer."
- Y 73133-73141 (hi:action-sequence): "There is also an action sequence. At a level redone by a drop-out it lists what is still stored, rather than what has just been prepared: \(T\supset\Omega^{\mathsf a}_1\supset\Lambda^{\mathsf a+}_1\supset\Lambda^{\mathsf a}_1\supset\Omega^{\mathsf a}_2\supset\cdots\supset\Lambda^{\mathsf a}_s,\ Z_s^{\mathsf a}=Z_s\)."
- Y 62128: "The choice \(\boldsymbol\nu=0\) gives the action sequence, the regions for which the terms were constructed. It governs the index sets of \(\mathbf E_k,\mathbf R_k,\mathbf B_k\), the profiles \(\varphi_j\) and hence \(x_k(\cdot)\)". Same line: "The choice \(\boldsymbol\nu=n\) gives the determining sequence"; Y 62246: "\(\Omega^n_l=\Omega_l\), so that the entries make up the determining sequence".
- Y 84116-84118: "\(\mathbf R_k\) denotes the sum of the normalized remainder differences on the label. The net regular action \(\mathbf E_k\) includes its profile counterterms and rim terms."
- Healed components: Y 62105: "Healed (every test passed): \(\Omega_l,\Lambda_l,S_l\mapsto\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X\) for \(l\le t\), and \(X\) leaves the label." Y 74832-74837: the healed normalization uses "the label with \(X\) adjoined to its regions and all marks in \(X\) removed", with regions \(\Omega_j^{\mathsf a}\cup X,\Lambda_j^{\mathsf a+}\cup X\). Y 101134-101136: "Root a changed term in the healed collar \(C^\sim\) of the deleted choice. In the fixed output label \(S'\) we have \(C^{\sim2}\subset\Lambda_t(S')\)."
- Other uses of the same count are also on a label: Y 78988-78996 (vacuum subtraction, "charge a missing base point in \(Z_j^+\)"), Y 96044-96049, Y 107886-107889 ("The small-field regions are nested in the reduced standing label").

Conclusion. The left side is `sum_j #_j(((Lambda_j^a)^c)^~)` for the action sequence of one fixed label. It is not a sum over regions stored at intermediate times of a history. The parameter `nu` exists only on drop-out marks (Y 62122-62128), so the action sequence and the label entries agree off the active drop-out marks. A healed component is adjoined to the action regions at all levels `l <= t`.

The sentence Y 84113, "It includes the stored collars of healed components", does not fit this: by Y 101136 a healed collar `C^~` lies in the one-layer erosion of `Lambda_t(S')`, so it does not meet `Z_t^+`. I read the sentence as a warning about the history bookkeeping, not as part of the definition. If the authors meant a history sum, section 4 shows that the count is false.

## 2. Theorem A (action layers)

Notation. `T^(n)` is the level-n lattice; a level-(n+1) site is a block of `L^4` level-n sites; `#_n(D)` is the number of level-n sites in `D` (Y 83998). A set is *aligned at level m* if it is a union of level-m unit cubes, that is, its level-(m-1) sites form a union of `L`-blocks. `N_k = #_k(T)`.

Hypotheses, all for one fixed label through `k`.

- (A1) `T = Omega^a_0`, and `Omega^a_1 ⊃ Lambda^a_1 ⊃ Omega^a_2 ⊃ ... ⊃ Lambda^a_k` (Y 73136-73140). Put `Omega^a_{k+1} = empty`.
- (A2) `Omega^a_m` is aligned at level m for `1 <= m <= k` (Y 62245: "`Omega^nu_l` is a region for `pi_l`", with `nu = 0`; `pi_l` is the partition into `M`-cubes of level `l`, Y 643-644, and `M` is a power of `L`; Y 62245: "The action regions are unions of coarse cubes"). Lemma C (section 5) gives more: `Omega^a_m` is a union of level-`m` cells.
- (A3) `Z^a_j = (Lambda^a_j)^c` is a union of cubes of one partition `pi_j` of `T^(j)` into congruent cubes, and `~` adds only cubes of `pi_j` that touch a cube of `Z^a_j` (Y 62037: "one layer of M-cubes of its level"; Y 84039: "one cell layer"; Y 78897: "the one-layer enlargement costs a fixed multiplicity"). Here `pi_j` is the `M`-cube partition and `~` one layer of `M`-cubes (Y 645-646, 62037, 84040-84041; check, row 625, item 2). If `~` at Y 84039 is read as one layer of level-`j` cells instead, Theorem A still holds with the same 81, on the cell grid, because `Z^a_j` is a union of cells by Lemma C (section 5); so both readings of Y 84039 give the count.

Put `Gamma^a_n = Omega^a_n \ Omega^a_{n+1}` for `0 <= n <= k`, `g_n = #_n(Gamma^a_n)`, and `a_m = #_m((Omega^a_m)^c)` for `1 <= m <= k`.

**Lemma 1 (layer identity).** `a_m = sum_{n<m} L^{-4(m-n)} g_n` for `1 <= m <= k`, and `N_k = sum_{n<=k} L^{-4(k-n)} g_n`.

Proof. By (A2), `(Omega^a_{n+1})^c` is aligned at level n+1, so `#_n((Omega^a_{n+1})^c) = L^4 a_{n+1}` for `0 <= n < k`. For `n = 0`: `g_0 = #_0((Omega^a_1)^c) = L^4 a_1`. For `1 <= n < k`: `Gamma^a_n = (Omega^a_{n+1})^c \ (Omega^a_n)^c` and (A1) give `g_n = L^4 a_{n+1} - a_n`. So `a_{n+1} = L^{-4}(a_n + g_n)`, with `a_1 = L^{-4} g_0`, and induction on m gives the first formula. Last, `g_k = #_k(Omega^a_k) = N_k - a_k`, so `N_k = g_k + a_k`. ∎

**Lemma 2 (sum).** `sum_{n=0}^k g_n = N_k + (L^4 - 1) sum_{m=1}^k a_m`.

Proof. Add `g_0 = L^4 a_1`, `g_n = L^4 a_{n+1} - a_n` (`1 <= n < k`) and `g_k = N_k - a_k`. ∎

Lemmas 1 and 2 use only nesting and alignment, so they hold for the determining sequence `Omega_m` as well (Y 62080: nested; aligned at its own level, Y 78888: "\(\Omega_{m+1}\) is aligned at level \(m+1\)").

**Theorem A.** Under (A1)-(A3),
`sum_{j=1}^k #_j(Z_j^+) <= 81 L^4/(L^4-1) * sum_{n=0}^k #_n(Gamma^a_n)`.

Proof. Step 1. By (A3) each cube of `Z_j^+` is a cube of `Z^a_j` or touches one; a cube has at most `3^4 = 81` cubes of `pi_j` touching or equal to it, and all cubes of `pi_j` have the same number of sites. So `#_j(Z_j^+) <= 81 #_j(Z^a_j)`.
Step 2. For `j < k`, (A1) gives `Z^a_j ⊂ (Omega^a_{j+1})^c`, so `#_j(Z^a_j) <= L^4 a_{j+1} = sum_{n<=j} L^{-4(j-n)} g_n` by Lemma 1. For `j = k`, `#_k(Z^a_k) <= N_k = sum_{n<=k} L^{-4(k-n)} g_n`.
Step 3. Sum over j and exchange: `sum_j #_j(Z^a_j) <= sum_n g_n sum_{j>=n} L^{-4(j-n)} <= (1 - L^{-4})^{-1} sum_n g_n`. ∎

This is the two-line identity of `t0-approach.md` R7 (c), now with the alignment step written (the layers `Gamma_n` are not aligned at level j, so the identity has to go through the complements `a_m`).

## 3. Theorem B (determining layers)

Now `Gamma_n = Omega_n \ Omega_{n+1}` with the label entries, as in Y 83989. By Lemma 2 for both sequences, it is enough to compare `sum_m #_m((Omega^a_m)^c)` with `sum_m #_m(Omega_m^c)`.

Where the sequences differ (Y 62112-62128). For an active drop-out mark `X` of level `k_X = k`, window bottom `h = k - N_k`, stopped after `n <= N_k` stages:
`Omega_i ∩ X = X \ Z''_i(X)` and `Omega^a_i ∩ X = Omega°_i ∩ X` for `h < i <= h+n`; all other entries agree. Put `O_i = X \ Omega°_i`. Then `Z''_i ⊂ O_i` (Y 62103: "increasing boxes in \(\Omega_l^c\cap X\)"), so
`(Omega^a_i)^c = Omega_i^c ⊔ ⋃_X (O_i(X) \ Z''_i(X))`, the union over marks with `h_X < i <= h_X + n_X`.
For fixed `i` these marks are pairwise disjoint in space (Y 62128: "at any one place and level at most one drop-out mark is active").

Inputs.

- (Q) Quiet boxes, Y 63748-63835, with `a_i = M R_i L^i` (cell side, bare units), `u_i = M L^i`:
  - (Q1) `O_i = H_i^{[8 a_i]}`, `H_i` a nonempty box on the level-i cell grid (Y 63759-63768).
  - (Q2) `Z''_i = H_i^{[3 a_i]}` for `h < i <= k_0`, where `a_{k_0+1} = u_k` and `h < k_0 <= k-2` (Y 63772-63803).
  - (Q3) `G_i = H_i^{[10 a_i]}` has at most 100 cells per side at level i, for every `h < i <= k`. This is the first class condition, Y 63684: "for `k_flat <= i <= k` the set `X ∩ Z_i` is a single component of `Z_i` and is small, that is, contained in a cube of `O(1)` level-`i` cells", with `h = k_flat` (Y 63720) and `G_i = Z_i ∩ X` (Y 63721); Y names the cutoff 100 at `i = k` (Y 63770) and uses it at `i = k_0+1` (Y 63828-63829). (Check, row 625, item 5.) If the `O(1)` is another fixed `n_sm >= 21`, replace `(96/7)^4` by `((n_sm - 4)/7)^4` below.
  - (Q4) `R_i` is non-increasing in `i` (Y 62195).
- (W) `k - k_0 <= k_0 - h` for every active mark.

**Lemma 3 (one mark).** Under (Q) and (W), for each active drop-out mark,
`sum_{i=h+1}^{h+n} #_i(O_i \ Z''_i) <= 35409 * sum_{h<i<=min(k_0,h+n)} #_i(Z''_i)`.

Proof. Early levels, `h < i <= min(k_0, h+n)`. Let `H_i` have `s_mu >= 1` cells on side `mu`. By (Q1), (Q2), `#_i(O_i)/#_i(Z''_i) = prod_mu (s_mu+16)/(s_mu+6) <= (17/7)^4 = 83521/2401`, because `(s+16)/(s+6)` decreases in `s`. So `#_i(O_i \ Z''_i) <= (81120/2401) #_i(Z''_i) <= 34 #_i(Z''_i)`, since `34 * 2401 = 81634`.
Late levels, `k_0 < i <= h+n`; these occur only if every early level was redone, because the stages run upward from `h` (Y 63836 (1)). By (Q1), (Q3) the sides of `O_i` are at most `96 a_i`, so `#_i(O_i) <= (96 M R_i)^4 <= (96 M R_{k_0+1})^4` by (Q4). For an early level `i'`, `Z''_{i'}` has sides at least `7 a_{i'}`, so `#_{i'}(Z''_{i'}) >= (7 M R_{i'})^4 >= (7 M R_{k_0+1})^4` by (Q4). There are at most `k - k_0` late and exactly `k_0 - h` early levels, so by (W) the late sum is at most `(96/7)^4` times the early sum of `#_{i'}(Z''_{i'})`. `(96/7)^4 = 84934656/2401 < 35375`, since `96^2 = 9216`, `9216^2 = 84934656` and `35375 * 2401 = 84935375`. Total factor `34 + 35375 = 35409`. ∎

**Theorem B.** Under (A1)-(A3) for the action sequence, nesting and alignment of the determining sequence, (Q) and (W),
`sum_{j=1}^k #_j(Z_j^+) <= C sum_{n=0}^k #_n(Gamma_n)`, `C = 81 L^4/(L^4-1) * 35410`.

Proof. `Z''_i(X) = Omega_i^c ∩ X`, and for fixed `i` the marks are disjoint, so Lemma 3 summed over marks gives `sum_m #_m((Omega^a_m)^c) <= (1 + 35409) sum_m #_m(Omega_m^c)`. By Lemma 2 for both sequences, `sum_n #_n(Gamma^a_n) = N_k + (L^4-1) sum_m a^a_m <= 35410 [N_k + (L^4-1) sum_m a_m] = 35410 sum_n #_n(Gamma_n)`. Apply Theorem A. ∎

**On (W).** (W) is proved in section 4 (Lemma W). Without (W) the constant of Lemma 3 is `34 + 35375 * max_X (k-k_0)/(k_0-h)`, finite for each `k` since `k_0 > h`, and not uniform. The earlier input (SV), `R_{h+1} <= 2 R_k`, is withdrawn: the `Rcheck_j` are powers of `L >= 13`, so a factor 2 means equality, which is neither given nor needed.

Why the late levels need this. For `i > k_0` the redone box `Z''_i` stays on the scale `u_k` (Y 63787: "The change of scale allows the later boxes to stay on the scale \(u_k\)"), while the stored box `O_i` has at least 17 cells of level i per side. So the action count at such a level is not bounded by the determining count at the same level; it is paid by the `R_k - (k-k_0)` early levels of the same mark.

## 4. The window inequality (W) from the ceiling (G)

The lemma is the lead's (FINISH row 618, result text); the proof below is the one checked in row 625 (`library/r7-count-check.md`, item 7).

Frame (Y 1102-1113): `theta_i >= gamma^{-2}` with `0 < gamma < e^{-1/2}`; for `i <= j`, `lambda(j-i) - c_5 <= theta_i - theta_j <= Bbar (j-i)`; `Rcheck_j = R(m_j)`, `m_j = min_{i<=j} theta_i`, where `R(y)` is the smallest power of `L` not below `(log y)^r`; `Rcheck_j <= L Rcheck_{j+1}`. Constants: `r >= 2` (Y 62001), `lambda = c_0/4 >= 0`, `c_5 = 2 c_2 >= 0` (Y 72936), `L >= 13` (Y 650). `Bbar >= 0`. (If a frame has `Bbar < 0` its upper bound also holds with 0 in place of `Bbar`.) Window: `N_t = Rcheck_t` (Y 1121, 62195), `t_flat = t - N_t` (Y 62103), the window bottom of the operation of level `k` is `h = k_flat = k - Rcheck_k` (Y 63720), `R_j = Rcheck_j` (Y 73075). The index `k_0`: `a_{k_0+1} = u_k` with `a_i = M Rcheck_i L^i`, `u_k = M L^k` and `h < k_0 <= k-2` (Y 63749, 63774-63777).

**Ceiling (G).** For all `y >= gamma^{-2}`: `(log(y + c_5 + Bbar L (log y)^r))^r <= L (log y)^r`.

**Lemma G.** (G) holds when `gamma <= gamma_0 := y_0^{-1/2}`, `y_0 = max{2 c_5, 4 (Bbar L (2r)^r)^2, 2^{1/(L^{1/r} - 1)}, e}`.

Proof. Let `y >= y_0`. With `u = y^{1/(2r)} > 1`, `log y = 2r log u <= 2r u`, so `(log y)^r <= (2r)^r y^{1/2}` (both sides positive as `y > 1`). Then `Bbar L (log y)^r <= Bbar L (2r)^r y^{1/2} <= y/2`, because `y^{1/2} >= 2 Bbar L (2r)^r`; and `c_5 <= y/2`. So `y + c_5 + Bbar L (log y)^r <= 2y`, and `log(2y) = log y + log 2 <= L^{1/r} log y`, because `(L^{1/r} - 1) log y >= log 2` for `y >= 2^{1/(L^{1/r}-1)}`. Raise to the power `r`. ∎

**(G) is new; where it enters.** (G) is not one of Y's conditions and does not follow from them: Y's frame conditions on `Rcheck` are one-step (`Rcheck_j <= L Rcheck_{j+1}`, Y 1110; `R_{j+1}/R_j ∈ {1, L^{-1}}`, Y 73081-73082), and across one window `theta` may rise by `Bbar (Rcheck_k - 1)`, which can move `R` by many factors of `L` (Example F of `library/r7-repair-check.md`, section 2: with `r = 2`, `L = 13`, `lambda <= 12`, `Bbar >= e^{14}`, `e^{-1} <= gamma`, the frame `theta_j = e^{14} + lambda(10-j)` (`j <= 10`), `e^5, e^4, e^3, e^2` satisfies all of Y 1102-1110 and has `Rcheck_{h_14} = 13^2 Rcheck_14`.) Y lowers `gamma` after the drift constants for the one-step comparison (Y 62001: 'two consecutive drops never occur, because `x` changes by `O(1)` per step and `gamma` is small'); (G) is the same kind of ceiling for one window. (G) depends on `r, L, c_5, Bbar` only. In Y's order (Y 72930-72931) these all precede `gamma`: `r ≺ L ≺ ... ≺ (lambda, c_5, Bbar) ≺ gamma`. So (G) is one more ceiling on `gamma`, of the kind Y's order admits at `gamma` ("a condition arising in the construction fits the order if, at the last of the constants on which it depends, it is of the kind named", Y 72940-72946). No earlier constant is restricted.

**Lemma W.** Assume the frame and (G).
(S) For every `t` and every `i` with `max(0, t - Rcheck_t) <= i <= t`: `Rcheck_i <= L Rcheck_t`.
(W) For every operation of level `k` with window bottom `h` and index `k_0` as above: `2 (k - k_0) <= k - h`, that is `k - k_0 <= k_0 - h`.

Proof. (1) `m_j` does not increase in `j` and `R` does not decrease, so `Rcheck_j` does not increase.
(2) For `i <= j`, `theta_i >= theta_j + lambda (j-i) - c_5 >= theta_j - c_5`, so `theta_j - c_5 <= m_j <= theta_j`.
(3) Let `t - Rcheck_t <= i <= t`. Then `m_i <= theta_i <= theta_t + Bbar (t - i) <= m_t + c_5 + Bbar Rcheck_t`, by the upper frame bound and (2). Since `m_t >= gamma^{-2} > e`, `(log m_t)^r > 1`; with `Rcheck_t = L^p` the least power of `L` not below it, `p >= 1` and `L^{p-1} < (log m_t)^r`, so `Rcheck_t < L (log m_t)^r`.
(4) By (3), monotonicity of `log` and (G) at `y = m_t >= gamma^{-2}`: `(log m_i)^r <= (log(m_t + c_5 + Bbar L (log m_t)^r))^r <= L (log m_t)^r <= L Rcheck_t`. `L Rcheck_t` is a power of `L` not below `(log m_i)^r`, so `Rcheck_i = R(m_i) <= L Rcheck_t`. This is (S).
(5) Let `Rcheck_k = L^p`, `p >= 1` by (3). From `a_{k_0+1} = u_k`: `Rcheck_{k_0+1} = L^{k-k_0-1}`. As `h + 1 <= k_0 + 1`, (1) and (S) at `i = h+1` give `Rcheck_{k_0+1} <= Rcheck_{h+1} <= L^{p+1}`, so `k - k_0 <= p + 2`. And `k - h = Rcheck_k = L^p`. So (W) follows from `2(p+2) <= L^p`, true for `L >= 6`, `p >= 1`: at `p = 1` it is `6 <= L`; and `2(p+3) = 2(p+2) + 2 <= L^p + L^p <= L^{p+1}`. ∎

Lemma W takes `k_0` from Y 63774-63777, which asserts "\(k_0+1\) be the last index with \(a_{k_0+1}=u_k\), with \(h<k_0\le k-2\)" without proof. Under (S) it exists:

*Lemma K* (row 652; checked line by line by Claude Opus 5.5 in row 657, `library/scale-note-check.md`, with the repair of its section A.2). Assume the frame, (G), `L >= 4` (Y's `L >= 13` gives it), and `h = k - Rcheck_k >= 0`. Then the set of `i` with `a_i = u_k` is non-empty, and its last element `i*` satisfies `h+2 <= i* <= k-1`. So `k_0 = i* - 1` has `h < k_0 <= k-2`. Moreover `a_i <= u_k` for `i <= k_0 + 1` and `a_i >= L u_k` for `k_0 + 2 <= i <= k`.

Proof. Write `a_i = M L^{e_i}`, `e_i = i + log_L Rcheck_i`, and `Rcheck_k = L^p`, `p >= 1`. By (1) and the frame's `Rcheck_i <= L Rcheck_{i+1}`, `Rcheck_{i+1}/Rcheck_i ∈ {1, L^{-1}}`, so `e_{i+1} - e_i ∈ {1, 0}`. `e_k = k + p >= k+1`. `k - h = L^p >= 4`, so `h+2 <= k`, and (S) at `i = h+2` gives `e_{h+2} <= h + 2 + p + 1 <= h + L^p = k`, because `p + 3 <= L^p` (at `p = 1`: `4 <= L`; and `p + 4 <= L^p + 1 <= L^{p+1}`). An integer sequence that moves by steps 0 or 1 from a value `<= k` at `h+2` to a value `>= k+1` at `k` takes the value `k` at some `i` in `[h+2, k-1]`; the indices with `e_i = k` form an interval, and its last element is below `k`. For the last sentence: `e` does not decrease, so `e_i <= e_{k_0+1} = k` for `i <= k_0 + 1`; and `e_{k_0+2}` is `k` or `k+1` and is not `k`, since `k_0 + 1` is the last index with `e_i = k`, so `e_i >= k+1` for `i >= k_0 + 2`. ∎

Only `L >= 4` is used (in `p + 3 <= L^p`); `p >= 1` comes from the floor `theta_i >= gamma^{-2} > e` (Y 1102-1103), which gives `(log m_k)^r > 1`, and the definition of `R` (Y 1108-1113). The last sentence uses only the steps 0 or 1, not (G).

For a standing mark of level `t < k` the same holds with `t` in place of `k`; Lemma 3 uses (W) once per mark, at the mark's own level, window and `k_0`.

**Corollary S (Y's scale comparison).** For every `t` with `h_t = t - N_t >= 0`: `Rcheck_{h_t} <= L Rcheck_t`. This is (S) at `i = h_t`. Y uses it without proof at Y 73382-73383 ("The scale comparison `Rcheck_{h_t} <= L Rcheck_t` therefore puts every carrier inside `Z''_{h_t+2}`"); it holds under (G).

## 5. From the count to the rim part of `E_k`

Replaces the first version of this section, which assumed that every rim base point lies in `Z_j^+`. That is false (check, row 625, item 8): `Z_j^+` adds one layer of `M`-cubes, while the rim is a layer of level-`j` cells, `Rcheck_j` layers of `M`-cubes deep. The fallback `(2w+1)^4` with `w = Rcheck_j` is not uniform, since `Rcheck_j >= (log gamma^{-2})^r` grows with `theta_j`. The repair counts the rim on the cell grid.

**Setting.** The profile `phi_j` is built from the action member `Lambda^a_j` (Y 1462: "The profiles use the small-field regions of the action sequence"; Y 62128): `D_j = dist_∞(., (Lambda^a_j)^c)` in level-`j` units, `phi_j = 0` where `D_j <= s_j/4`, `phi_j = 1` where `D_j >= 3 s_j/4` (Y 1475-1494). A level-`j` cell is a cube of side `M Rcheck_j` (level-`j` units) of the level-`j` cell grid (Y 73075-73083); `s_j = M Rcheck_j` when `Lambda^a_j` is a union of cells (Y 1476). The base points are the set `B_j` of level-`j` sites `y` whose cell and the cells touching it lie in `Lambda^a_j` (Y 83993-83995, without the islands: Remark I below). With the tents `h_y` (`h_y >= 0`, `sum_y h_y = 1`, Y 95875-95876) and `A(w, U)` linear in the weight `w`, `A(phi_j, U) = sum_{z ∈ B_j} A(phi_j h_z, U) + sum_{y ∉ B_j} A(phi_j h_y, U)`. Y asserts `phi_j h_z = h_z` for `z ∈ B_j` (Y 84108-84109; the tent fit, log `library/r7-repair.md` (d)), and the rim terms, `y ∉ B_j`, obey `0 <= A(phi_j h_y, U_k) <= C alpha_{0,j}^2` (Y 84110), with coefficient `|b_j| <= B_#`.

**Lemma C (input (C)).** For every admitted label through `k` and `1 <= j <= k`, `Lambda^a_j` and `Omega^a_j` are unions of level-`j` cells; every standing island or drop-out mark of level `s` is a union of level-`s` cells contained in `Z_s`.

Proof: `library/r7-repair.md`, section (c), by induction along the history from Y's rules: steps produce unions of cells and copy older entries (Y 62080, 62174; for `Omega_t`, Y 61973, "Hulls (\('\), \(\widehat{\cdot}\)) and layers are taken in level-\(t\) cells", with the display Y 61981-61985, `Omega_t^c = Q_t'^{~2} ∪ P_t'^{~4} ∪ H_t`); healed components and islands overwrite with a class component, a union of level-`t` cells, hence of level-`l` cells for `l <= t` (Y 62001, 62105-62107, 73081-73083); a drop-out does not change the action sequence, because the stored entries `Omega°_l, Lambda°_l` (Y 62121-62126) are free of older windows by "marks wait" (Y 62128). Y itself states only the weaker "unions of coarse cubes" (Y 62245) and provides `s_j = M` for a `Lambda_j` that is not a union of cells (Y 1476); by Lemma C that case does not occur for the action sequence. Not yet checked by another model.

**Lemma R (rim count).** Let `(Z^a_j)^≈` be `Z^a_j = (Lambda^a_j)^c` together with every level-`j` cell that touches a cell of `Z^a_j`. Then `T^(j) \ B_j ⊂ (Z^a_j)^≈` and `#_j((Z^a_j)^≈) <= 81 #_j(Z^a_j)`. Hence, under the inputs of Theorem B and (G),
`sum_{j=1}^k #_j(T^(j) \ B_j) <= 81 L^4/(L^4-1) sum_n #_n(Gamma^a_n) <= 81 L^4/(L^4-1) * 35410 * sum_n #_n(Gamma_n)`.

Proof. Let `y ∉ B_j`. Some cell `c'` equal to or touching the cell of `y` is not contained in `Lambda^a_j`. By Lemma C, `Lambda^a_j` is a union of cells, and the cells partition the torus, so `c' ∩ Lambda^a_j = ∅`, that is `c' ⊂ Z^a_j`. So the cell of `y` is in `(Z^a_j)^≈`. Assign each cell of `(Z^a_j)^≈` to a cell of `Z^a_j` that it equals or touches; each cell of `Z^a_j` receives at most `3^4 = 81` cells, and all cells have `(M Rcheck_j)^4` level-`j` sites, so `#_j((Z^a_j)^≈) <= 81 #_j(Z^a_j)`. Steps 2 and 3 of Theorem A give `sum_j #_j(Z^a_j) <= L^4/(L^4-1) sum_n #_n(Gamma^a_n)`, and the proof of Theorem B gives `sum_n #_n(Gamma^a_n) <= 35410 sum_n #_n(Gamma_n)`. ∎

No condition on the tent range is used: a non-base site is in the cell enlargement whatever its tent does.

**The rim bound.** `|sum_j b_j sum_{y ∉ B_j} A(phi_j h_y, U_k)| <= B_# C sup_j alpha_{0,j}^2 * 81 L^4/(L^4-1) * 35410 * sum_n #_n(Gamma_n)`: one term per non-base site, the bound of Y 84110 per term, then Lemma R. ∎ The same count bounds the number of sites `z ∈ Lambda^a_j \ B_j`, at which regular level-`j` terms (Y 1453) have no tent of their own; their bound belongs to RF30, step G1 of R7, not this item.

**Remark I (islands; log (d)).** Y takes base points one cell layer inside `Lambda_j^+ = Lambda_j ∪ ` level-`j` islands (Y 83993-83994), but builds `phi_j` from `Lambda_j` (Y 1462, 1475), and a standing level-`j` island lies in `Z^a_j` (log, Lemma I), where `phi_j = 0`. So Y 84109 (`phi_j h_z = h_z` at every base point) fails at a base point inside an island whose tent meets the island. This is a defect of Y's wording at Y 83993-83994, not a wrong reading: Y 1453 puts the regular level-`j` terms at `z ∈ Lambda_j` only, and an island keeps its own action in `T'_t(X)` (Y 62107). Repair used here: base points inside `Lambda^a_j` only; island sites are then non-base sites in `Z^a_j`, counted by Lemma R with no change. In the other reading (`phi_j` built on `Lambda_j^+`), Lemma R holds with `(Lambda_j^+)^c ⊂ Z^a_j` in place of `Z^a_j`, since `Lambda_j^+` is a union of level-`j` cells by Lemma C; same constant.

The full bound `|E_k| <= C sum_n #_n(Gamma_n)` also needs the first line of RF30 summed over `j` (age factor `L^{-beta_T (n-j)}`, summable) and the boundary sums; those are R7 steps G1, G2 and are not this item.

## 6. History reading: false, and not used

History (the lead's heuristic, now checked against the rules). Take a periodic array of small components created at one step `j`, each a box inside the 100-cell cutoff, pairwise non-touching, filling a fraction `c > 0` of `T`. No other large field. Each is eligible once its window is quiet and is healed at the level `t` with `t - N_t >= j` (Y 62195: "healing at a level \(i<t\) something created at step \(s\) requires \(s\le i-\mathsf N_i\)"). Non-touching components form an admitted family (Y 62197: "a finite collection of possible healed components which touch neither one another nor \(Z_k(\bar h)\)"). The output label is the all-small-field label (Y 62106, 62197), so `Gamma_n = empty` for `n < k`, `Gamma_k = T`, and the right side is `N_k`. If the stored components were counted at the levels `j..t` where they were stored, the left side would be at least `c #_j(T) = c L^{4(k-j)} N_k`. So no `C` independent of `k - j` exists in that reading.

In the label reading the left side of this history is zero: `Z^a_l = empty` for all `l`, and the count is trivial. By section 1 this is the reading Y uses.

Who pays a healed collar. Not the count. Y sums the healed families inside the operation as a polymer gas, and "Each activity contains a healed component" (Y 78822-78824); the bound is "\(Ce^{-5p_0(g_t)/4}\) per root", "including the small factor for each healed collar" (Y 101129-101131). So the factor is the activity of the component's own operation; the erasure of healed clusters (Y 62197) is what removes them from the label, and the window lemma (Y 62195) is what makes the clusters independent. I read these passages and did not check the activity bound.

## Open after this note

1. Check by another model of Lemma C and Remark I (new in row 648, written by Claude Opus 5.5, which also wrote the check of row 625).
2. Y's geometry used as stated, not rebuilt: step regions are unions of cells of their level (Y 62080, citing Balaban 119 p. 256), the class conditions and quiet boxes (Y 63684, 63748-63835).
3. The tent fit behind Y 84109 at base points: the position of the anchor `p_y` relative to `y` is not fixed by Y 95874-95876. If it is within `M` of `y`, the fit holds once `Rcheck_j >= 4(C_h + 2)`, a ceiling on `gamma` (log, (d)). Not needed for the count.
4. Whether the `O(1)` of Y 63684 is the 100 of Y 63770 (any fixed `n_sm >= 21` works, with `((n_sm - 4)/7)^4`).
5. Y 84113-84114 ("stored collars of healed components ... an actual window/history count") is not explained by Y; section 1 reads it.

RESULT: R7-COUNT holds in the reading Y uses (fixed label, action sequence). Theorem A: `C_A = 81 L^4/(L^4-1)` against the action layers. Theorem B: `C = 81 L^4/(L^4-1) * 35410` against the determining layers `Gamma_n` of Y 83989, given Y's quiet-box geometry (Q) and (W). (W) is proved (Lemma W) from Y's frame conditions and one new ceiling (G) on `gamma`, which holds for `gamma <= gamma_0(r, L, c_5, Bbar)` and fits Y's order at `gamma`; the same lemma proves Y's unproved scale comparison `Rcheck_{h_t} <= L Rcheck_t` (Y 73382-73383). The rim terms of `E_k` are bounded by `C' sum_n #_n(Gamma_n)` (Lemma R, factor 81 on the cell grid), with input (C) proved from Y's update rules (Lemma C); the base points inside islands (Y 83993) are a wording defect of Y that does not change the count (Remark I). The history reading is false and is not the one Y uses. Open: the other model's check of Lemma C and Remark I; Y's geometry at Y 62080 and Y 63684-63835 used as stated; the tent fit behind Y 84109.
