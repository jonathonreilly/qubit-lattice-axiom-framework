lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T15:24Z

# Check of `library/r7-count.md` and of the lead lemma for (W) (FINISH row 625)

Provenance: Claude Opus 5.5, high effort, branch `claude/ym4d-hard-route` at 75754cba9; Mac mini worker 2. Not an audit. The checked note was written by Claude Fable 5.2 (row 618); the lead lemma for (W) is in the result text of row 618. I wrote neither. Same provider (Anthropic) as the author, different model.

Source: YM4_1400.tex of Sussman and Alpoge (written with Claude and Codex), commit 2bc0658f91d2, fetched into my own scratch folder (136,637 lines; byte-identical to `/tmp/ym4_1400.tex`). 'Y n' is line n. No computer run; arithmetic is displayed.

Overlap check: `grep` of `library/open-core.md` for r7-count, rim count, `Z_j^+`, (Q3), the window inequality and the ceiling (G) finds nothing; FINISH has only rows 618 and 625 for R7-COUNT. Repo search: inside this lane folder, `library/r7-count.md` is the only prior note on the count (registry row R7-COUNT also cites `t0-approach.md` R7 (c) and `prior/first-tests.md` section 2).


## (1) The reading: HOLDS

Every occurrence of `Z_j^+` in Y (fixed-string grep, 14 lines: Y 72886, 78873, 78878, 78897, 78991, 78994, 78996, 84038, 84039, 84112, 96045, 96049, 107886) is on one label, and its definition is through the action member:

- Y 78873: "Put \(Z_j^+=((\Lambda_j^{\mathsf a})^c)^\sim\)", inside "the loaded label sum" `L_c(S)` of one label `S` (Y 78865-78880).
- Y 62128: the action sequence ("\(\boldsymbol\nu=0\)") "governs the index sets of \(\mathbf E_k,\mathbf R_k,\mathbf B_k\), the profiles \(\varphi_j\)". Y 73148-73153 confirms the split of uses: "Density tests and the last-shell test use the action regions. Coupling and vacuum weights use their specified action supports."
- Y 84038-84039 (RF30, the place of use): "\(\mathcal R_j\) consists of domains outside \(Z_j^+\), and \(Z_j^+\) is the stored large-field region enlarged by one cell layer", for "an admitted label through \(k\)" (Y 83989).
- Y 78990-78996 (vacuum subtraction of one label against the empty label), Y 96044-96049 (`T_j(S_empty; w) - T_j(S; w)`, one standing label), Y 107886-107889 ("The small-field regions are nested in the reduced standing label"): each is a difference between one label and the empty label; `Z_j^+` is that label's.

No use of the count on regions outside the action sequence of the label was found, so the refutation clause does not fire. The action sequence is a function of the label: `Omega^nu` is "the geometric label obtained by stopping the operations after `nu` stages" (Y 62128), and the stored regions `Omega°_l` are kept by the mark (Y 62121). Healing adjoins `X` to the action regions as well (Y 74830-74836: `Omega_j^a ∪ X`, `Lambda_j^{a+} ∪ X`).

Two remarks, neither a defect of the note. (a) Y 84113-84114 ("stored collars of healed components ... an actual window/history count") is not explained by Y; the note's reading of it (and the lead's, row 618) is an interpretation, correctly labelled as such. (b) The note's section 1 quotes Y 62106 for "Healed" and 62128 for `nu`; in the pinned file the healed bullet is Y 62105, the drop-out display Y 62109-62116, the `nu` display Y 62123-62126 and the two-sequence sentence Y 62128. Line drift of one, harmless.

## (2) Hypotheses (A1)-(A3): HOLD (A3 after a reading fixed from Y's notation)

- **(A1) HOLDS.** Y 73136-73140 and again Y 62248: `T ⊃ Omega^a_1 ⊃ Lambda^{a+}_1 ⊃ Lambda^a_1 ⊃ Omega^a_2 ⊃ ... ⊃ Lambda^a_s`.
- **(A2) HOLDS.** Y 62245: "Let \(\boldsymbol\nu'\le\boldsymbol\nu\). Then \(\Omega^{\boldsymbol\nu}_l\) is a region for \(\pi_l\)", and `nu = 0` is the action sequence (Y 62128). `pi_l` is the partition into "centered, half-open M-cubes in level-l units" (Y 643-644) with `M` a power of the odd `L` (Y 73078, 651); an `M`-cube of level `l` is a union of `M^4` level-`l` unit cubes, so a region for `pi_l` is aligned at level `l`. The note cites Y 62246 ("unions of coarse cubes"); the sharper line is Y 62245.
- **(A3) HOLDS, with `pi_j` = the `M`-cube partition of level `j`.** Y 645-646: "\(Y^{\sim n}\) means addition of \(n\) layers in the partition currently named", and Y 62037: "the enlarged component \(X^\sim\), that is, \(X\) together with one layer of \(M\)-cubes of its level". `(Lambda^a_j)^c` is a union of `pi_j` cubes: the action regions are regions for `pi_j` (Y 62245) and "In these sequences and nests the boxes are only unions of \(M\)-cubes" (Y 62080); the late prepared boxes are unions of `M`-cubes of level `i` on the `u_i` grid, compatible with the cell grid because `L` is odd (Y 63805-63809). So every set involved is a union of cubes of the one partition `pi_j`, and the 81 of Theorem A step 1 is right.
  - Drop-out mark `X` of level `t`: at levels `t_flat < l <= t_flat + n` the action member is the stored `Omega°_l` (Y 62121, 62125), a region for `pi_l` (Y 62245). Holds.
  - Mark `Y'` of level `s` nested in a later mark `X` of level `t`: "Marks wait": `s < t_flat`, windows disjoint, "at any one place and level at most one drop-out mark is active" (Y 62128). A drop-out leaves all entries outside its window unchanged (Y 62115), so at the levels of `Y'`'s window the action member inside `Y'` is still `Y'`'s stored region, and at the levels of `X`'s window it is `X`'s stored region. A healed component or island swallows the mark (Y 62121), and then both sequences receive `∪ X` (Y 62105-62106). Holds.
  - **Wording risk, not a failure.** Y 84039 says "one cell layer", and "cells" of level `j` are elsewhere the `M Rcheck_j`-cubes (Y 62096, 63749). If `~` meant a layer of such cells, Step 1 fails on nests, which are only unions of `M`-cubes (Y 62080): one `M`-cube enlarged by one cell layer has volume up to `(2 Rcheck_j + 1)^4` `M`-cubes, not uniform in `j`. Y's own notation (Y 645-646, 62037) and the next lines (Y 84040-84041: "\(\Omega^\sim\) has one level-\(j\) localization layer added") fix the `M`-cube reading; the check adopts it. A reader of 84039 alone could take the other.

## (3) Lemma 1, Lemma 2, Theorem A: HOLD

Checked line by line.

- Lemma 1. `(Omega^a_{n+1})^c` aligned at level `n+1` gives `#_n((Omega^a_{n+1})^c) = L^4 a_{n+1}` (one level-`(n+1)` site and `L^4` level-`n` sites per level-`(n+1)` unit cube, the fixed boundary convention of Y 644). `g_0 = L^4 a_1` since `Omega^a_0 = T`; `g_n = L^4 a_{n+1} - a_n` from `Omega^a_{n+1} ⊂ Omega^a_n`; `g_k = N_k - a_k` since `Omega^a_{k+1}` is empty. Induction: `a_{m+1} = L^{-4}(sum_{n<m} L^{-4(m-n)} g_n + g_m) = sum_{n<=m} L^{-4(m+1-n)} g_n`. Holds.
- Lemma 2. `L^4 a_1 + sum_{n=1}^{k-1} (L^4 a_{n+1} - a_n) + N_k - a_k = N_k + L^4 sum_{m=1}^k a_m - sum_{m=1}^k a_m`. Holds for `k >= 1`.
- Theorem A. Step 1: each cube of `Z_j^+` is assigned to a cube of `Z^a_j` it equals or touches; at most `3^4 = 81` cubes per cube; all `pi_j` cubes have `M^4` level-`j` sites. Step 2: `Omega^a_{j+1} ⊂ Lambda^a_j` gives `Z^a_j ⊂ (Omega^a_{j+1})^c`, so `#_j(Z^a_j) <= L^4 a_{j+1} = sum_{n<=j} L^{-4(j-n)} g_n`; at `j = k`, `#_k(Z^a_k) <= N_k`, the same form by Lemma 1. Step 3: `sum_{j=1}^k sum_{n<=j} L^{-4(j-n)} g_n <= sum_n g_n sum_{q>=0} L^{-4q}`. Holds, `C_A = 81 L^4/(L^4-1)`.
- The note's remark that Lemmas 1-2 hold for the determining sequence: nesting Y 62080, alignment Y 78888 and Y 62245 with `nu = n`. Holds; Y 83989-83991 sets `Omega_0 = T_l`, `Omega_{k+1}` empty, as used.

## (4) The difference of the two sequences: HOLDS

On an active drop-out mark `X` of level `t` stopped after `n` stages, for `t_flat < i <= t_flat + n`: `Omega_i ∩ X = X \ Z''_i(X)` (Y 62110-62111, `nu = n`) and `Omega^a_i ∩ X = Omega°_i` (Y 62125, `nu = 0`); everywhere else the two sequences agree (Y 62115 "all other entries unchanged"; `nu` is defined only on drop-out marks, Y 62121-62126). With `O_i(X) = X \ Omega°_i`: `(Omega^a_i)^c ∩ X = O_i(X)` and `Omega_i^c ∩ X = Z''_i(X)`. The inclusion `Z''_i(X) ⊂ O_i(X)` is `Omega^0_i ⊂ Omega^n_i` (Y 62245: "\(\Omega^{\boldsymbol\nu'}_l\subset\Omega^{\boldsymbol\nu}_l\)"), equivalently Y 62103 ("increasing boxes in \(\Omega_l^c\cap X\)", with `Omega_l` the entry before the operation), and also Y 63813 (`Z''_i ⊂ O_i`). Disjointness at one level: Y 62128, "at any one place and level at most one drop-out mark is active". So `(Omega^a_i)^c = Omega_i^c ⊔ ⋃_X (O_i(X) \ Z''_i(X))`, a disjoint union, and `#_i` is additive over it.

The note writes the mark level as `k`; for a standing mark of level `t < k` the same holds with `t`, `t_flat = t - N_t` and the boxes of the operation at `t` (Y 63684-63835 is written at the operation's own level). Lemma 3 is per mark, so this changes nothing.
