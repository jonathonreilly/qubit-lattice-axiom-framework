lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T10:29Z

# R7-COUNT: the rim count `sum_j #_j(Z_j^+) <= C sum_n #_n(Gamma_n)`

FINISH row 618, registry row R7-COUNT, root R7 (AGE), step G3 of `library/t0-approach.md`.

Kind of result: proof of a step that Sussman and Alpoge's text (YM4_1400, written with Claude and Codex; cited as Y with line numbers) states as needed and does not prove. The geometry is theirs, after Balaban (CMP 119, 122). Proved by Claude (Fable 5.2, medium), not yet checked by the other model. No computer run; all arithmetic is displayed.

Overlap check: `grep` of `library/open-core.md` for the rim count, `Z_j^+` and R7-COUNT finds nothing. The only rows are FINISH 618 and registry R7-COUNT (this item).

## Verdicts

1. **Reading.** Y uses the count on a fixed label, not on a history. `Z_j^+` is a function of the label's action sequence.
2. **Label reading, action layers: proved (Theorem A), with `C_A = 81 L^4/(L^4-1)`.** Inputs: nesting and alignment of the action sequence, and a one-layer enlargement on the grid of the region. No property of healed components is used.
3. **Label reading, determining layers** (the `Gamma_n` of Y 83989 are the label's own entries, which are the determining sequence): **proved under two named inputs (Theorem B)**, with `C = C_A * 35410`. The two sequences differ only on drop-out marks. The inputs are the quiet-box geometry of Y 63760-63835 with the 100-cell cutoff at every level of the window (Q), and the window inequality (W): `2 (k - k_0) <= k - h`. (W) holds when `N_k = R_k >= 8`, `L >= 3`, and `R` varies by at most a factor 2 over one window (SV). (SV) is a flow input and is not proved here. So `C` depends on `L` only through `C_A`; it is not a function of `(L, M)` alone unless (W) is granted.
4. **History reading: false.** The lead's history (section 4) is a counterexample with ratio `c L^{4(k-j)}`. Y does not use this reading. The healed collars are not in `Z_j^+` of the output label (Y 101134-101136), and Y pays them by the activity of their own operation (Y 78815-78825, 101129-101131).
5. **The use at Y 84116-84125:** given the count, the rim part of the net regular action is at most `C sum_n #_n(Gamma_n)` (section 5). The other parts of `E_k` rest on RF30, which is not this item.

## 1. Which regions are on the left side

Quotes that fix the reading.

- Y 83989-83991: "For the field estimate fix an admitted label through \(k\), with layers \(\Gamma_n=\Omega_n\setminus\Omega_{n+1}\), \(\Omega_0=T_\ell\) and \(\Omega_{k+1}=\emptyset\)."
- Y 78873: "Put \(Z_j^+=((\Lambda_j^{\mathsf a})^c)^\sim\)." Y 84038-84040: "\(Z_j^+\) is the stored large-field region enlarged by one cell layer."
- Y 73133-73141 (hi:action-sequence): "There is also an action sequence. At a level redone by a drop-out it lists what is still stored, rather than what has just been prepared: \(T\supset\Omega^{\mathsf a}_1\supset\Lambda^{\mathsf a+}_1\supset\Lambda^{\mathsf a}_1\supset\Omega^{\mathsf a}_2\supset\cdots\supset\Lambda^{\mathsf a}_s,\ Z_s^{\mathsf a}=Z_s\)."
- Y 62128: "The choice \(\boldsymbol\nu=0\) gives the action sequence, the regions for which the terms were constructed. It governs the index sets of \(\mathbf E_k,\mathbf R_k,\mathbf B_k\), the profiles \(\varphi_j\) and hence \(x_k(\cdot)\)". Same line: "The choice \(\boldsymbol\nu=n\) gives the determining sequence"; Y 62246: "\(\Omega^n_l=\Omega_l\), so that the entries make up the determining sequence".
- Y 84116-84118: "\(\mathbf R_k\) denotes the sum of the normalized remainder differences on the label. The net regular action \(\mathbf E_k\) includes its profile counterterms and rim terms."
- Healed components: Y 62106: "Healed (every test passed): \(\Omega_l,\Lambda_l,S_l\mapsto\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X\) for \(l\le t\), and \(X\) leaves the label." Y 74832-74837: the healed normalization uses "the label with \(X\) adjoined to its regions and all marks in \(X\) removed", with regions \(\Omega_j^{\mathsf a}\cup X,\Lambda_j^{\mathsf a+}\cup X\). Y 101134-101136: "Root a changed term in the healed collar \(C^\sim\) of the deleted choice. In the fixed output label \(S'\) we have \(C^{\sim2}\subset\Lambda_t(S')\)."
- Other uses of the same count are also on a label: Y 78988-78996 (vacuum subtraction, "charge a missing base point in \(Z_j^+\)"), Y 96044-96049, Y 107886-107889 ("The small-field regions are nested in the reduced standing label").

Conclusion. The left side is `sum_j #_j(((Lambda_j^a)^c)^~)` for the action sequence of one fixed label. It is not a sum over regions stored at intermediate times of a history. The parameter `nu` exists only on drop-out marks (Y 62122-62128), so the action sequence and the label entries agree off the active drop-out marks. A healed component is adjoined to the action regions at all levels `l <= t`.

The sentence Y 84113, "It includes the stored collars of healed components", does not fit this: by Y 101136 a healed collar `C^~` lies in the one-layer erosion of `Lambda_t(S')`, so it does not meet `Z_t^+`. I read the sentence as a warning about the history bookkeeping, not as part of the definition. If the authors meant a history sum, section 4 shows that the count is false.

## 2. Theorem A (action layers)

Notation. `T^(n)` is the level-n lattice; a level-(n+1) site is a block of `L^4` level-n sites; `#_n(D)` is the number of level-n sites in `D` (Y 83998). A set is *aligned at level m* if it is a union of level-m unit cubes, that is, its level-(m-1) sites form a union of `L`-blocks. `N_k = #_k(T)`.

Hypotheses, all for one fixed label through `k`.

- (A1) `T = Omega^a_0`, and `Omega^a_1 ⊃ Lambda^a_1 ⊃ Omega^a_2 ⊃ ... ⊃ Lambda^a_k` (Y 73136-73140). Put `Omega^a_{k+1} = empty`.
- (A2) `Omega^a_m` is aligned at level m for `1 <= m <= k` (Y 62246: "The action regions are unions of coarse cubes").
- (A3) `Z^a_j = (Lambda^a_j)^c` is a union of cubes of one partition `pi_j` of `T^(j)` into congruent cubes, and `~` adds only cubes of `pi_j` that touch a cube of `Z^a_j` (Y 62037: "one layer of M-cubes of its level"; Y 84039: "one cell layer"; Y 78897: "the one-layer enlargement costs a fixed multiplicity").

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
  - (Q3) `G_i = H_i^{[10 a_i]}` has at most 100 cells per side at level i, for every `h < i <= k`. Y states this for `i = k` (Y 63768-63770) and `i = k_0+1` (Y 63826); for the other levels it is the same small-box cutoff, which I take as part of the boxing rule and did not find stated level by level.
  - (Q4) `R_i` is non-increasing in `i` (Y 62195).
- (W) `k - k_0 <= k_0 - h` for every active mark.

**Lemma 3 (one mark).** Under (Q) and (W), for each active drop-out mark,
`sum_{i=h+1}^{h+n} #_i(O_i \ Z''_i) <= 35409 * sum_{h<i<=min(k_0,h+n)} #_i(Z''_i)`.

Proof. Early levels, `h < i <= min(k_0, h+n)`. Let `H_i` have `s_mu >= 1` cells on side `mu`. By (Q1), (Q2), `#_i(O_i)/#_i(Z''_i) = prod_mu (s_mu+16)/(s_mu+6) <= (17/7)^4 = 83521/2401`, because `(s+16)/(s+6)` decreases in `s`. So `#_i(O_i \ Z''_i) <= (81120/2401) #_i(Z''_i) <= 34 #_i(Z''_i)`, since `34 * 2401 = 81634`.
Late levels, `k_0 < i <= h+n`; these occur only if every early level was redone, because the stages run upward from `h` (Y 63836 (1)). By (Q1), (Q3) the sides of `O_i` are at most `96 a_i`, so `#_i(O_i) <= (96 M R_i)^4 <= (96 M R_{k_0+1})^4` by (Q4). For an early level `i'`, `Z''_{i'}` has sides at least `7 a_{i'}`, so `#_{i'}(Z''_{i'}) >= (7 M R_{i'})^4 >= (7 M R_{k_0+1})^4` by (Q4). There are at most `k - k_0` late and exactly `k_0 - h` early levels, so by (W) the late sum is at most `(96/7)^4` times the early sum of `#_{i'}(Z''_{i'})`. `(96/7)^4 = 84934656/2401 < 35375`, since `96^2 = 9216`, `9216^2 = 84934656` and `35375 * 2401 = 84935375`. Total factor `34 + 35375 = 35409`. ∎

**Theorem B.** Under (A1)-(A3) for the action sequence, nesting and alignment of the determining sequence, (Q) and (W),
`sum_{j=1}^k #_j(Z_j^+) <= C sum_{n=0}^k #_n(Gamma_n)`, `C = 81 L^4/(L^4-1) * 35410`.

Proof. `Z''_i(X) = Omega_i^c ∩ X`, and for fixed `i` the marks are disjoint, so Lemma 3 summed over marks gives `sum_m #_m((Omega^a_m)^c) <= (1 + 35409) sum_m #_m(Omega_m^c)`. By Lemma 2 for both sequences, `sum_n #_n(Gamma^a_n) = N_k + (L^4-1) sum_m a^a_m <= 35410 [N_k + (L^4-1) sum_m a_m] = 35410 sum_n #_n(Gamma_n)`. Apply Theorem A. ∎

**On (W).** From `a_{k_0+1} = u_k`: `R_{k_0+1} = L^{k-k_0-1}`, so `k - k_0 = 1 + log_L R_{k_0+1}`, and `k - h = N_k = R_k` (Y 62195). So (W) reads `2 (1 + log_L R_{k_0+1}) <= R_k`.
(SV): `R_{h+1} <= 2 R_k` on every window. Given (SV), `L >= 3` and `R_k >= 8`: `f(R) = R - 2 - 2 log_3(2R)` has `f(8) = 6 - 2 log_3 16 > 0` (as `16 < 27`) and `f' = 1 - 2/(R ln 3) > 0` for `R >= 2`, so (W) holds.
(SV) is a statement about the flow: `R_j` is about `(log x_j)^r` (Y 63882) and the drift is bounded, `x_i - x_j <= B_# (j-i)` (Y 2492-2500, row 18 of `t0-approach.md`), which over `N_k = (log x_k)^r` levels changes `log x` by `o(1)` below a coupling ceiling. This is the one input not proved here and not found in our library: **(SV), slow variation of `R` over one window.** Without (W) the constant of Lemma 3 is `34 + 35375 * max_X (k-k_0)/(k_0-h)`, finite for each `k` since `k_0 > h`, and not uniform.

Why the late levels need this. For `i > k_0` the redone box `Z''_i` stays on the scale `u_k` (Y 63787: "The change of scale allows the later boxes to stay on the scale \(u_k\)"), while the stored box `O_i` has at least 17 cells of level i per side. So the action count at such a level is not bounded by the determining count at the same level; it is paid by the `R_k - (k-k_0)` early levels of the same mark.

## 4. History reading: false, and not used

History (the lead's heuristic, now checked against the rules). Take a periodic array of small components created at one step `j`, each a box inside the 100-cell cutoff, pairwise non-touching, filling a fraction `c > 0` of `T`. No other large field. Each is eligible once its window is quiet and is healed at the level `t` with `t - N_t >= j` (Y 62195: "healing at a level \(i<t\) something created at step \(s\) requires \(s\le i-\mathsf N_i\)"). Non-touching components form an admitted family (Y 62197: "a finite collection of possible healed components which touch neither one another nor \(Z_k(\bar h)\)"). The output label is the all-small-field label (Y 62106, 62197), so `Gamma_n = empty` for `n < k`, `Gamma_k = T`, and the right side is `N_k`. If the stored components were counted at the levels `j..t` where they were stored, the left side would be at least `c #_j(T) = c L^{4(k-j)} N_k`. So no `C` independent of `k - j` exists in that reading.

In the label reading the left side of this history is zero: `Z^a_l = empty` for all `l`, and the count is trivial. By section 1 this is the reading Y uses.

Who pays a healed collar. Not the count. Y sums the healed families inside the operation as a polymer gas, and "Each activity contains a healed component" (Y 78822-78824); the bound is "\(Ce^{-5p_0(g_t)/4}\) per root", "including the small factor for each healed collar" (Y 101129-101131). So the factor is the activity of the component's own operation; the erasure of healed clusters (Y 62197) is what removes them from the label, and the window lemma (Y 62195) is what makes the clusters independent. I read these passages and did not check the activity bound.

## 5. From the count to the rim part of `E_k`

Statement. Let the rim terms of level j be `A(phi_j h_y, U_k)` over base points `y` with `phi_j(y) < 1`, with `0 <= A(phi_j h_y, U_k) <= C alpha_{0,j}^2` (Y 84110-84111) and coefficient `|b_j| <= B_#`. Suppose every such `y` is a level-j site of `Z_j^+` (the profile is 1 at every base point one cell layer inside `Lambda_j^+`, Y 83993-83995, 84108-84109: "\(\varphi_jh_z=h_z\) at every base point"). Then

`|sum_j b_j sum_{y rim} A(phi_j h_y, U_k)| <= B_# C sup_j alpha_{0,j}^2 * sum_j #_j(Z_j^+) <= C' sum_n #_n(Gamma_n)`,

by Theorem B. Proof: one term per site, the displayed bound per term, then the count. ∎

The inclusion "rim base point ⊂ `Z_j^+`" is the definition of the profile support (Y 73143: "\(\Lambda^{\mathsf a+}_j\) denotes the specified collared support of the action weights") and I did not check it against the construction of `phi_j`; if the profile collar is wider than one layer, replace 81 by `(2w+1)^4` for `w` layers. The full bound `|E_k| <= C sum_n #_n(Gamma_n)` also needs the first line of RF30 summed over `j` (age factor `L^{-beta_T (n-j)}`, summable) and the boundary sums; those are R7 steps G1, G2 and are not this item.

## Open after this note

1. (SV), slow variation of `R_j` over one window, which gives (W). Flow input; not in Y as a displayed statement and not in our library as far as the R7 files show.
2. (Q3) at the levels other than `k_0+1` and `k`: the 100-cell cutoff for each `G_i` of the window. Read off the boxing rule, not found stated.
3. (A3) on a drop-out mark, where nests are "only unions of M-cubes" (Y 62080): the action regions there are the old step regions, so the grid is the cell grid; I did not check a mark nested in a later mark.
4. Check by the other model: Lemmas 1-3 and Theorems A, B.

RESULT: R7-COUNT holds in the reading Y uses (fixed label, action sequence): proved with `C = 81 L^4/(L^4-1)` against the action layers (Theorem A, no further input), and with `C = 81 L^4/(L^4-1) * 35410` against the determining layers `Gamma_n` of Y 83989 under the quiet-box geometry (Q) and the window inequality (W) (Theorem B); the history reading is false by the lead's healed-density history and is not the one Y uses, healed collars being paid by their own operation's activity; open: (SV) slow variation of `R_j` over a window (gives (W)), the 100-cell cutoff at every window level (Q3), and the other model's check.
