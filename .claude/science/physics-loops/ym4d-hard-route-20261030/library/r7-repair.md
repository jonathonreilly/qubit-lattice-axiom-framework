lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T01:09Z

# r7-repair (FINISH row 648): log of the repair of `library/r7-count.md`

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, branch `claude/ym4d-hard-route` at c67b4f939. Not an audit. I wrote the check `library/r7-count-check.md` (row 625); I did not write `library/r7-count.md` (Claude Fable 5.2, row 618). So the new proofs below (Lemma C, the island repair) are written by the same model as the check and need a check by another model.

Source: YM4_1400.tex of Sussman and Alpoge (written with Claude and Codex), commit 2bc0658f91d2, fetched into my own scratch folder (136,637 lines). 'Y n' is line n. Credit: the geometry is theirs, after Balaban (CMP 119, 122); the lead lemma for (W) is the lead's (row 618 result text), checked in row 625; Theorems A, B are Fable's (row 618). No computer run; arithmetic is displayed.

## Repo search and overlap

- `grep` of `library/open-core.md`, `library/open-registry.md` and the FINISH rows for r7-count, rim, `Z_j^+`, "union of cells", "unions of cells", islands with profiles: the only rows on this item are 618, 625, 648. No other row covers (C) or the island question.
- `library/core-gaps.md` (row 621, checked in row 640) uses "step regions and healed or island fillings are unions of cells" inside its proof of (G) (its line 96) and lists Y 62080's sentence "every large-field region ... is a union of cells of its own level" as out of its scope (its line 156). Lemma C below uses the same Y rules (Y 62103-62116, 62128, 62174-62177, 62001) and the same induction over operations; it is a different statement (the action sequence, not the gaps), so no overlap.

## Edits made to `library/r7-count.md`

(a) New section "4. The window inequality (W)": the ceiling (G), the lead lemma (Lemma W) with the proof of the check, the proof that (G) holds for `gamma <= gamma_0(r, L, c_5, Bbar)`, the statement that (G) is not in Y and enters Y's order at `gamma` (Y 72930-72931, 72946), and Corollary S, the scale comparison `Rcheck_i <= L Rcheck_t` for `t - Rcheck_t <= i <= t`, which contains Y's `Rcheck_{h_t} <= L Rcheck_t` (Y 73382-73383). The note's (SV) is removed.
(b) Section 5 replaced by Lemma R of the check (rim `Rcheck_j` layers of `M`-cubes deep; factor 81 on the cell grid), now unconditional given Lemma C, and with the island repair of (d).
(c), (d) below; their results are in the note as Lemma C and Remark I.
Also, per the check: (Q3) is marked as holding at every window level (Y 63684), (A2) cites Y 62245, the verdicts and the open list are updated. The history-reading section is kept, renumbered 6.

## (c) Input (C): PROVED from Y's update rules (Lemma C)

**What Y states.** Definition of the action sequence: Y 62121 ("A drop-out's mark keeps the regions `Omega°_l = Omega_l ∩ X`, and likewise `Lambda°_l, S°_l`, which X possessed before the operation"), Y 62123-62126 (`Omega^nu_l ∩ X = X \ Z''_l(X)` for `t_flat < l <= t_flat + nu(X)`, `= Omega°_l` for `t_flat + nu(X) < l <= t_flat + n(X)`), Y 62128 ("The choice `nu = 0` gives the action sequence"), Y 73133-73141 (display hi:action-sequence), Y 62169-62171 (the same rule for `Lambda_l`, `l < s`; at `l = s` the drop-out stays outside `Lambda_s`). Outside the active windows of standing drop-out marks the action entries are the label entries.
- Y 62080 (Proposition, geometry): "Every large-field region and every creation set is a union of cells of its own level. Both statements hold for the regions that the steps produce (119, p. 256). ... In these sequences and nests the boxes are only unions of `M`-cubes". The "sequences and nests" are the stage and prepared sequences (determining entries inside drop-out windows).
- Y 62245-62246 ([1.6]): "`Omega^nu_l` is a region for `pi_l`" and "The action regions are unions of coarse cubes". This is the form Y states for the action sequence; "coarse cube" is not defined there, and `pi_l` is the `M`-cube partition (Y 643-644). So Y states only "union of `M`-cubes" for `Lambda^a_l`.
- Y 1475-1477: "put `s_j = M Rcheck_j` when `Lambda_j` is a union of those cubes, and `s_j = M` otherwise. The latter region is a union of `M`-cubes." With Y 1462 ("The profiles use the small-field regions of the action sequence") this provides for an action region that is not a union of cells. It is a provision, not a statement that the case occurs.

So Y does not state (C). It follows from Y's rules, as follows.

**Inputs from Y, used as stated (not rebuilt).**
- (Y-STEP) The step of level `t` produces entries `Omega_t, Lambda_t` that are unions of level-`t` cells (Y 62080, second and third sentences; Balaban 119, p. 256), and copies the earlier entries and the standing marks (Y 62174: "At a step, the earlier entries and standing marks are copied").
- (Y-FATE) The operation of level `t` acts on the components `X` of its class, components of `Z_t` (Y 63684, 63720-63721), by the three fates of Y 62103-62116; "a healed component or an island overwrites the older entries on its region, and any mark it swallows ceases to stand. Outside the class no entries change" (Y 62175-62177).
- (Y-WAIT) "Marks wait: a mark of level `s` lying inside a class component of level `t` satisfies `s < t_flat`. Hence standing marks that share a part are nested, their windows `(s_flat, s]` are disjoint" (Y 62128).
- (Y-NEST) Level-`(j+1)` cells are unions of level-`j` cells: "Because it is a power of `L`, all partitions are nested" (Y 62001), and "a passage between levels either coarsens these cells by `L`, or leaves their physical partition unchanged" (Y 73081-73083, with `R_{j+1}/R_j ∈ {1, L^{-1}}`). Hence for `l <= t` every level-`t` cell is a union of level-`l` cells, and the complement of a union of level-`l` cells is a union of level-`l` cells (the cells partition the torus, Y 643-646).
- (Y-LAB) Labels are nested, `Lambda_{j+1} ⊂ Omega_{j+1} ⊂ Lambda_j` (Y 73088-73092), so `Z_s ⊂ Z_t` for `s <= t`.
- Reading (K): components of a union of closed cells are its connected components as a point set (closed cells, Y 73068-73071), so a connected subset of `Z_t` lies in one component of `Z_t`, and a component of a union of level-`t` cells is a union of level-`t` cells.

**Lemma C.** For every label of a history, every level `l >= 1` of it: (i) `Omega^a_l` and `Lambda^a_l` are unions of level-`l` cells; (ii) every standing marked component (island or drop-out) of level `s` is a union of level-`s` cells, and is contained in `Z_s` of the label; (iii) at a place `x` and level `l` that lie in no active window of a standing drop-out mark, the action entries equal the label entries.

*Proof.* Induction along the history (steps and operations in their order). Before step 1 there are no entries.

(iii) holds by definition: `nu` acts only on drop-out marks inside their windows (Y 62121-62126).

*Step `t`.* By (Y-STEP) the new entries `Omega_t, Lambda_t` are unions of level-`t` cells, and all earlier entries and marks are copied, so (ii) and (i) at levels `< t` persist. At level `t` no standing mark has an active window: a mark of level `s <= t-1` has window `(s_flat, s]`, below `t`. So by (iii) `Omega^a_t = Omega_t`, `Lambda^a_t = Lambda_t`: (i) at `t`.

*Operation of level `t`.* Let `X` be a class component. `X` is a component of `Z_t`, and `Z_t = Lambda_t^c` is a union of level-`t` cells (step `t`, (Y-NEST)), so by (K) `X` is a union of level-`t` cells, hence of level-`l` cells for `l <= t` (Y-NEST).

First, the entries on `X` at window levels are free of older windows. Let `X'` be a standing drop-out mark of level `s` with `X' ∩ X ≠ ∅`. By (ii) `X' ⊂ Z_s ⊂ Z_t` (Y-LAB); `X'` is connected (it was a component of `Z_s` at its creation, and its level-`s` entries have not changed since, else it would have been swallowed and would not stand), so by (K) `X' ⊂ X`. By (Y-WAIT) `s < t_flat`, so the window `(s_flat, s]` of `X'` lies below `t_flat`. Hence at every `(x, l)` with `x ∈ X`, `t_flat < l <= t`, no older window is active, and by (iii) the label entries there equal the action entries before the operation.

Now the three fates, using `X` a union of level-`l` cells for `l <= t`:
- Healed: `Omega_l, Lambda_l ↦ Omega_l ∪ X, Lambda_l ∪ X` for `l <= t`, and every mark inside `X` ceases to stand (Y 62105, 62175-62176). So the new action entries are the old action entries outside `X` (Y 62177) and `X` itself on `X`: `Lambda^a_l(new) = (Lambda^a_l(old) \ X) ∪ X`, a union of level-`l` cells. Same for `Omega^a_l`. (ii): the marks that stand are untouched.
- Island: the same for `l < t` and for `Omega_t`; `Lambda_t` unchanged, `X ⊂ Z_t` (Y 62106-62107). (i) as for healed at `l < t`, and at `l = t` for `Omega`; `Lambda^a_t` unchanged. (ii): `X` is a new standing mark of level `t`, a union of level-`t` cells, `X ⊂ Z_t`.
- Drop-out after `n` stages: the label entries change only on `X` at `t_flat < l <= t_flat + n` (Y 62109-62116; `Lambda_t ∩ X = ∅` before and after). The action entries there are `Omega°_l = Omega_l(old) ∩ X` and `Lambda°_l = Lambda_l(old) ∩ X` (Y 62121, 62125), which by the first point equal the old action entries on `X`. So the operation does not change the action sequence on `X`, and outside the class nothing changes (Y 62177). (i) persists. (ii): `X` is a new standing mark of level `t`, a union of level-`t` cells, `X ⊂ Z_t`.
Different class components are disjoint, so the fates compose. ∎

**Corollary C.** (C) holds: for every admitted label through `k` and `1 <= j <= k`, `Lambda^a_j` is a union of level-`j` cells, and so is `Lambda^a_j ∪ (standing level-j islands)`. Hence in Y 1476 the first case always applies to the action sequence: `s_j = M Rcheck_j`. The case `s_j = M` can occur only for a stage or prepared (determining) region (Y 62080, last sentences; Y 63805-63809), which the profiles do not use (Y 1462, 62128).

**Answer to (c).** (C) is proved from Y's rules (Lemma C), so Lemma R holds unconditionally (given Y's geometry inputs) with the factor 81 on the cell grid. The form Y states, "unions of coarse cubes" / "region for `pi_l`" (Y 62245-62246), is weaker; with that form alone the rim of an `M`-cube of `Z^a_j` costs up to `(2 Rcheck_j + 1)^4` `M`-cubes and the constant is not uniform (check, item 8), so the stronger form is needed and is now proved. Y 1476 is not evidence against (C): it is a fallback that the action sequence never uses.

Gap labels: (Y-STEP) and the class-component rule are Y's statements used as stated; Y cites Balaban 119 p. 256 for (Y-STEP) and we have not rebuilt it. Reading (K) is the standard one and Y's text does not spell it out.

## (d) Islands in the base points: a defect of Y's text, not a wrong reading; the count needs nothing new

**The lines.**
- Y 1462: "The profiles use the small-field regions of the action sequence." Y 1475: `D_j(x) = dist_∞(x, Lambda_j^c)`; Y 1482: `phi_j(x) = ∫ psi(u) 1{D_j(x - s_j u) >= s_j/2} du`; Y 1489-1490: `phi_j` "vanishes where `D_j <= s_j/4`".
- Y 1452-1454: the regular index map `I^E_j(S) ⊂ {(z, X) : z ∈ Lambda_j ∩ T^(j), ...}`; Y 1515-1525: the label exponent carries `sum_{(z,X) ∈ I^E_j} {E^(j)(X,U,z) - E^(j)(X,1,z)} - sum_j b_j A(phi_j, U)`.
- Y 62106-62107: an island of level `t` leaves `Lambda_t` unchanged, "Thus `X ⊂ Z_t` remains, as a component without inner regions. On it, `T'_t(X)` is kept together with its variables, its measure and its factors."
- Y 83993-83995: "Let `Lambda_j^+` be `Lambda_j` together with its level-`j` islands. Base points are the unit sites lying one layer of `M Rcheck_j`-cells inside this set." Y 84026: RF30 sums over `X ⊂ Lambda_j^+`. Y 84108-84109: "For the actual profile `phi_j`, `phi_j h_z = h_z` at every base point."
- Y 73143: "`Lambda^{a+}_j` denotes the specified collared support of the action weights"; no other line of Y defines `Lambda^{a+}_j` or `Lambda_j^+` (fixed-string grep: `Lambda_j^+` occurs only at Y 83993, 84026; `Lambda^{\mathsf a+}` only at Y 62248, 73138, 73143).

**Lemma I.** Let `I` be a standing island of level `j` in an admitted label through `k >= j`. Then `I ⊂ Z^a_j`, so `D_j = 0` and `phi_j = 0` on `I` (indeed on `{D_j <= s_j/4}`, which contains `I`).

*Proof.* `Lambda_j ∩ I = ∅` (Y 62106, island; later steps copy, Y 62174, and a later heal or island that overwrote it would swallow it, Y 62175). If some `x ∈ I` lay in the active window of a standing drop-out mark `X'` of level `t'` at level `j`, then `X' ∩ I ≠ ∅` and `j <= t'`. `j = t'` is impossible: then `I` and `X'` are two components of the class of level `t'`, which are disjoint. So `j < t'`, and by the argument of Lemma C `I ⊂ X'` (`I` is an older standing mark meeting the class component `X'`), and by (Y-WAIT) `j < t'_flat`, so `j` is not in the window `(t'_flat, t'_flat + n]`: contradiction. So by Lemma C (iii) `Lambda^a_j ∩ I = Lambda_j ∩ I = ∅`. ∎

**Consequence.** Take the profile as Y builds it (Y 1462, 1475: from the action member `Lambda^a_j`). A base point `z` of `Lambda_j^+` that lies one cell layer inside an island `I` has `phi_j = 0` on `I`, so `phi_j h_z = h_z` fails as soon as `h_z` is nonzero somewhere on `I` (for instance at its anchor, if the anchor lies in `I`). So Y 84109 is false at such base points. A large island (at least 3 level-`j` cells per side, which the class allows: "small" means inside a cube of `O(1)` cells, Y 63684) has such base points.

**Defect or wrong reading?** A defect of Y's text, at Y 83993-83994 (the set `Lambda_j^+` of RF30), not a wrong reading of the profile. Reasons: three lines (Y 1462, 1475, 1453) fix that both the profile and the regular level-`j` terms of the label exponent live on `Lambda_j` (action, without islands), and an island's own action is kept in `T'_t(X)` (Y 62107). The only reading that would save Y 84109 is that `phi_j` is built on `Lambda_j^+` (or that `Lambda^{a+}_j` means `Lambda^a_j` plus islands). The chain `Omega^a_j ⊃ Lambda^{a+}_j ⊃ Lambda^a_j` (Y 73136-73140) admits that, since islands lie in `Omega_j \ Lambda_j` (Y 62106), but no line of Y says it, and it would contradict Y 1475 and leave the counterterm on islands without the regular terms it cancels (Y 1453: `z ∈ Lambda_j`).

**What the count needs in each case.**
- Case D (Y as written; repair: base points are taken one cell layer inside `Lambda^a_j`, without islands, and RF30's first line sums `X ⊂ Lambda^a_j`). Island sites are then not base points; they lie in `Z^a_j` (Lemma I), so they are inside the cell enlargement of `Z^a_j`, and their rim counterterms `A(phi_j h_y, U_k)` (zero unless the tent reaches `{phi_j > 0}`) are counted by Lemma R as it stands. Nothing new: (C) for `Lambda^a_j` (Corollary C), factor 81.
- Case P (the other reading: `phi_j` built on `Lambda_j^+ = Lambda^a_j ∪ ` level-`j` islands). Then `phi_j h_z = h_z` at island base points (given the tent fit below), and the non-base sites are in the cell enlargement of `(Lambda_j^+)^c ⊂ Z^a_j`. The count needs `Lambda_j^+` to be a union of level-`j` cells: Corollary C (islands are standing marks, unions of level-`j` cells, Lemma C (ii)). Factor 81, the same bound `81 #_j(Z^a_j)`. In this case Y's regular index map (Y 1453) would also have to be extended to island sites; that is Y's construction, not the count.
So in either case the count closes with the same constant; the choice affects only the cancellation structure of RF30's first line, which is not this item. I recommend Case D: it changes one phrase of Y (83993-83994) and nothing else.

**Tent fit (used by Y 84109 at the base points of Case D; not the count; unchecked part named).** Under Corollary C, `s_j = M Rcheck_j`. A base point `z` has its cell and the 80 cells touching it in `Lambda^a_j`, so `D_j(z) >= M Rcheck_j` in level-`j` units, up to the boundary convention of half-open cells (Y 644, 73068-73071: a fixed number of neighbouring cells). The tent `h_z` is supported within `C_h M` level-`j` units of its anchor (Y 95875-95876: `|x(p) - x(p_y)| <= C_h M a_{K-j}`). If the anchor lies within `M` of `z` (not checked: Y 95874 says only "anchors `p_y ∈ P_K`"), then on `supp h_z`, `D_j >= M Rcheck_j - (C_h + 2) M >= 3 M Rcheck_j/4` once `Rcheck_j >= 4 (C_h + 2)`, which holds for `gamma <= gamma_1(r, L, C_h)` since `Rcheck_j >= (log gamma^{-2})^r` (Y 1102-1113). Then `phi_j = 1` on `supp h_z` and `phi_j h_z = h_z`. Open: the anchor position (gap, outside this item).

