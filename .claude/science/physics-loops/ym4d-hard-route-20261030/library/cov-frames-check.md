lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T00:28Z

# cov-frames-check: line-by-line check of `library/cov-frames.md` (FINISH row 646)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, branch `claude/ym4d-hard-route` at 3591d5adc, 2026-11-10. A check by a second Claude model of a file written by Claude Fable 5.2 (medium); same provider, so not a cross-provider check. Not an audit. Source Y = `YM4_1400.tex` of the Sussman-Alpoge experiment repository (ethanwsussman/Yang--Mills-LLM-experiment at 2bc0658f91d2), credited to Sussman and Alpoge with Claude and Codex as authors of its text.

## Verdict

**`library/cov-frames.md` HOLDS, with five repairs (R1 to R5), none of which changes a statement that a consumer uses. No item FAILS. First failing step: none.** The weak-form statements are correct implications from the clauses of section 3, and those clauses are in Y, as stated or as readings of the lines named. One finding goes beyond the file: **Y's bound `C(M) eps_t` for (R-core) does follow**, from the carried extension test `chi_{t,Lambda}` (Bałaban CMP 122, p. 193, (1.75); Y 71437-71441, 78266-78276), with the constant `(4 M_0 + 5 C(M)) eps_t` (item (4), Lemmas A and B). The file's weaker bound `(4 M_0 + 2 C(M) C_2'') e_t` also holds.

| Item | Verdict |
|---|---|
| (1) The clauses of section 3 against Y | HOLDS WITH REPAIR (R1: six line numbers; the pin of (S-gauge) is read, and not needed; the floor `M_2 >= L` is an added choice, Y has `c delta_0 M_2 >= 1`) |
| (2) `B` of the main step: "an end" or "both ends" | HOLDS. Y says "an end" at 71488, 75679-75683, 75700-75704 and 96361; Y 63836 and 63856 say neither. The registry note "Y 63836 says 'both ends'" is not in Y. The statements hold under both readings |
| (3) The ten weak-form statements | HOLDS WITH REPAIR (R2: an unproved and unused clause of Lemma 4.5 (b) on density tests; R3: Bałaban's hypothesis is on all of `Z cap Lambda^c`, so Lemma 5.4 must cite Lemma 5.3 (b); R4: the bound on the plaquettes of `B*(X)` that are not inside `Lambda^pr` rests on Y's form of the proposition, not on Bałaban's (1.78)) |
| (4) (R-core), the constant, Remark 5.5 | HOLDS WITH REPAIR (R5). The certificates alone do not give `C(M) eps_t` (a plaquette of `Ext(X)` at defect `10 eps_t < C_2'' e_t` meets them); the carried extension test does. Remark 5.5 (ii) misreads that test |
| (5) The late stop | HOLDS. Y has the move (Y 63836 (0), 63862, 75677-75686, 78285-78296); the reduction to (TG) is right. Pointer for row 647: Y 78322-78326 may make (TG) unnecessary |
| (6) The weak form for `cov-global` Theorem 5.1 and `cov-xstar` (X5) | HOLDS; at a late stop given (TG). `cov-xstar-check` R5 now applies without its condition |
| (7) (M-cut) and 'minimiser in a box' | stated exactly in item (7): (M-cut) is Y's construction (Y 63856, 72678-72686, 71447-71454); the proposition is Y 71488, citing Bałaban CMP 122 (1989) 175, Proposition 1, p. 194 |
| (8) Ten quoted passages | HOLDS (twelve compared; all word for word; offsets of at most 5 lines; one sentence used for a neighbouring claim) |

Open after this check: (TG) (row 647); (X-ext), the domain of `chi_{t,Lambda}`, read from Bałaban and two converse passages of Y, not a definition in Y; the partition of cells by test cubes (as before); the proposition 'minimiser in a box' and (M-cut), cited and not rebuilt. No numeric job was run (memory free was 52 percent at the start; none was needed). Every step here is a written argument; nothing rests on a computation.


## Repo search

- `grep -n "cov-frames-check\|late-stop-tg\|(TG)" library/open-core.md FINISH.md`: the only rows are 646 (this one) and 647 (`late-stop-tg`, which owns (TG)). I do not attack (TG) here. Rows 633, 636, 637, 638, 639 are the checks and the reading named in the row; I do not redo `cov-global` or `cov-xstar`.
- `library/cov-global-check.md` item (6) already noted the "an end" / "both ends" ambiguity and said the proofs of `cov-global` hold under either reading if (F-main) and (R-core) use the same set; `library/cov-xstar-check.md` R5 is conditional on change (1) of `cov-frames`. Both are used below.
- Sussman-Alpoge text: Y = `/tmp/ym4_1400.tex` (136,637 lines, as the row names it). Every Y quotation below was compared with that file in this session.

## Item (2). The set `B` of the main step: HOLDS

What Y says at each place (read in this session):

| Place | Words | Reading |
|---|---|---|
| Y 71488 (Proposition 'minimiser in a box') | "the map `V_k restricted to Lambda^pr -> A(U_{k,X}(V_k))`, which is a function of `V_k` on the level-`k` bonds having an end point in `Lambda^pr`" | **an end** |
| Y 75680-75683 (first chart of a late stop) | "Central integration has consumed the old box field, including the bonds crossing its boundary. The resulting term has unrestricted fresh Haar coordinates on the bonds with an end in the box." | **an end**; the file quotes it word for word |
| Y 75700-75704 | "A first outgoing row of level `i+1` that reads the box has at least one of its two blocks there, so its middle fine bond has an end in the box. It is one of the free Haar coordinates, even for a row crossing the box face." | **an end** |
| Y 96361 (stage `R` of the other part) | "`b_X` the set of bonds of `T^{(j+1)}` that have an end point in that box. The moves of `R` alter `V_{j+1}` on the bonds of the sets `b_X` and nowhere else ... Each bond of `b_X` has both end points in X." | **an end** (an extra source the file does not cite; it supports change (1)) |
| Y 63836 (3), Y 63856 | "`V_k` is integrated over `Lambda^pr`"; "independent of `V_k` on the box"; "`dV_k restricted to Lambda^pr`"; the cutoff "on the bonds of the box" | **neither**: no rule for the crossing bonds |

I searched Y 63700-63900 for "both end", "an end", "end point", "endpoint": there is no "both ends" there. The registry note "Y 63836 says 'both ends'" (row COV, 2026-11-10, after the three checks) is not supported by the text: Y 63836 is silent, and the only explicit rules in Y (71488, 75680-75683, 75700-75704, 96361) all say "an end". Repair for the registry (for the lead): "Y 63836 does not say which bonds; Y 71488, 75680-75683, 75700-75704, 96361 say 'an end'."

Do the statements of the file hold for each reading?

- *An end* (the file's choice). Lemma 4.4 (b), (c) and the fresh set `B*(X)` are right: a plaquette with a corner `x in Lambda^pr` has its two edges at `x` in `B_main`; a plaquette with no corner in `Lambda^pr` has no edge in `B_main`. `B*(X) minus B(X)` is the set of level-t plaquettes with exactly one corner in `Lambda^pr`: `Lambda^pr` is a product of integer intervals in level-t units, so two adjacent corners in it span an edge with both ends in it, and two diagonal corners `x, x + e_a + e_b` in it force `x + e_a, x + e_b` in it. Checked.
- *Both ends.* Then the move writes fewer bonds, the weak frame statement with `B(X)` holds, and it implies the one with `B*(X)` (a larger `B` gives a weaker statement: Definition 2.0 only asks for conjugacy off `B`). The certificates of Lemmas 5.2, 5.4 are given for every plaquette of `B*(X)`, so Theorem 5.1 holds with either fresh set. Monotone, as the file says.
- One coupling the file states (Remark 5.5 (iii)) and I confirm: the reading of `B_main` and of (M-cut) must be the same set. Y 71450-71453 ("For each non-tree bond, close it by the tree path ... `abs(log(V_k V_Lambda^{-1})(b)) <= C(M) eps_k < M_0 eps_k`") and Y 72682-72686 ("The cutoff in the subsequent draw restricts `V'_m = V_m V_Lambda^{-1}` to its reference ball. Its complement carries zero mass") put the cutoff on every bond of the reference law, which is the integrated set `dV' restricted to Lambda^pr` (Y 63856). With Y 75680-75683 this set contains the crossing bonds.

Verdict on item (2): HOLDS. Change (1) of the file agrees with every explicit statement of Y.

## Item (1). The clauses of section 3 against Y: HOLDS WITH REPAIR (line numbers and two labels)

STATED = Y says the clause in words at the lines given. READ = Y does not say it in one place; the file infers it from the lines given. I read every line range below in this session.

| Clause | Y lines (checked) | Stated or read | Note |
|---|---|---|---|
| (S-ent) | 62173 ("At a step, the earlier entries and standing marks are copied") | STATED | file says 62174; the sentence is on 62173 |
| (S-avg) | 4288 (the step formula with `delta(M(V_k) V_{k+1}^{-1})`), 62050 (a), 65419-65424 | STATED (the delta); READ (carried as long as the lower block is carried, which is (E1) of `i3-cert`) | |
| (S-gauge) | 4285 (blocks `P''` "away from failures and from `Z_k`"); 97398-97399 (gauge region `(P_j'^{~1} cup Z'^{~5})^c`); 75604-75605 ("The block-gauge draw is outside its five-layer enlargement"); 97401-97403 ("For a tested bond `b` both runs therefore obtain `u(b_-) V_{j-1}(b) u(b_+)^{-1}`"); 61979-61980 | support and action STATED; the pin READ | Y 4358 says "If `u = 1` on the coarse sites, then `V^u(y,x) = V(y,x) u(x)^{-1}`": a conditional about contours, not a statement that the draw is pinned. See the remark after the table: the pin is not needed in Lemma 4.1 |
| (S-int) | 4285, 4288 | READ | Y writes the step as one integral over `V_k`; that the level-(l-1) bonds with an end in `Omega_l` leave the point while the others stay stored is the meaning of the regions, not a sentence |
| (S-else) | 4288, 62173 | READ | completeness of the list of writes |
| (D1), (D2) | 72244-72260, 64035-64036, 77767-77778 | as in `cov-x-check` | not re-checked (row scope) |
| (G-collar) | 77767-77768 ("the group is pinned at the next coarse sites, so the coarse row remains fixed"); 97525-97528 (centres in `((Omega_{iota+1}^{~3})^c minus Z''_{iota+1}) cap X`); 97533-97534; 77775-77777 ("Its support is in complete blocks inside the component's exterior buffer. A link moved across the prepared inner face belongs to the collar") | STATED | the file's `K_i^-` is Y's mask written in the box notation of `cov-x` 2.1 |
| (O-order) | 1169-1176; 63836 (1) "for `j = k_flat, ..., k - 1`, one value after another"; 62176 ("Outside the class no entries change") | STATED (the order); READ ("each move is a move of one component") | file says 62177; the sentence is on 62176 |
| (P-test) | 1146-1149 (tests are Borel indicators of the variables); 77758-77760 ("Remove an old indicator only when it equals one on the complete chart used for its removal"); 77778 | STATED | file says 77756-77758 for the removal sentence; it is 77758-77760 |
| (P-collar) | 77744-77763 (order: regularity test, collar gauge, approximate test, completion, removal, sharp split); 77793-77794; 97586-97587 ("On a failure of the local sharp test, the stored prefix uses the untransformed real variables") | STATED | the file proves the stop for both retained forms, which covers Y's two conventions (Y 77797-77801, local and global sharp) |
| (P-late) | 63836 (0) ("If a component leaves after the tree gauge, its frame sum stays with it"); 63862 ("If one of the tests of (1)--(3) fails in a component, that component drops out"); 75677-75686; 78285-78296 | STATED | file says 63857; the sentence is on 63862 |
| (M-int) | 63836 (3); 75679-75683; 97597-97598 ("the Haar refresh uses the box coins and keeps the old variables for the prepared datum"); 75062-75068; 96361 | STATED, with the set "an end" (item (2)) | |
| (M-slot) | 76677-76679; 76011-76013; 76038-76039; 73170-73173; 78288-78290 ("Use the prepared datum for the regularity comparison and the fresh outgoing field for the later averaging rows that read it") | STATED | 78288-78290 is a further source the file does not cite |
| (M-tree) | 63836 (0) (frame sum = insertion of `1 = abs(W_4)^{-1} sum_r 1`); 63849 (`B_0 = B'' cap (shells)`, the tree `T_0` in `B_0`, the core "at no point unfolded"); 75684 ("Its frame tree acts on the old shell variables") | STATED (where it acts); READ (that it writes no bond without an end in `Lambda^pr minus C_h`) | the core-face and outer-face rows are (TG), row 647 |
| (M-ref) | 63856 (`V'_k := V_k V_Lambda^{-1}`, the reference law); 72678-72686; 76679-76680; 65471-65474 | STATED | file says 65472-65474; the sentence starts on 65471 |
| (M-cut) | 63856 ("the cut-off `1{abs((1/i) log V'(b)) < M_0 eps_k` on the bonds of the box}`, in which `M_0` is a constant chosen large after `M`"); 72682-72686; 71447-71454 (healed: "`abs(log(V_k V_Lambda^{-1})(b)) <= C(M) eps_k < M_0 eps_k` ... `chi(Lambda^pr)` ... equal one on the passing support"); 71480-71483 and 63836 (0) (island keeps it) | STATED on "the bonds of the box"; READ that these are `B_main` | see item (2), last point |
| (M-last) | 97609-97611; 71426-71427 ("The final test is `chi_k(X^{~-6})`, evaluated after the draw of the new `V_k`"); 62106 | STATED | 71426-71435 is a further source: it gives `X^{~-6} = H^{~4}` in Y's own words |
| (M-rev) | 63856 (`delta_ax` on a tree "that contains all the sites of this set together with the external bond of `T_0` into the box"); 4366; 76698-76699 | READ (the action on the crossing bonds is the definition of `u . V` at Y 4366) | the conclusion (bounds preserved) is STATED at 76698-76699 |
| (M-else) | 63836 (3) ("the exponentiation that follows it [is] counted separately") | READ | |
| (T-cube) | 62001 ("side of order `M_2 R_t`", `L^2 M_2 <= M`, floor `c delta_0 M_2 >= 1`); 62409-62411 (in level-(t-1) units: cube side `L^2 M_2 R_t`, layers `L M_2 R_t`, cell `L M R_t`); 63165-63166 (`w = M_2 R_t L^t`, side `L w`); 645-647 (partitions into centred half-open cubes); 77819-77820 | side and layers STATED; partition of each cell READ; floor `M_2 >= L` ADDED | file says 77812-77813; the sentence is on 77819-77820. Y's floor is `c delta_0 M_2 >= 1`, not `M_2 >= L`: the file's floor is an added choice (compatible: take `M >= L^3`), which it labels "I assume". The partition clause is the gap that `cov-global-check` (defect 3) already names |
| (T-dens) | 1150-1151; 61976-61978; 62405-62407; 134115-134119 | STATED | |
| (T-carried) | 62050 (c) | STATED | |
| (MC) | 3573; 5139 | STATED | |
| (DB) | 72270-72276, 65419-65424 (Definition T of `i3-cert`) | as in `cov-x-check` | |

**Remark on the pin in Lemma 4.1.** Corollary 2.3 asks `u = 1` at the level-l sites so that rows of level `> l - 1` do not move. At step `l` the only rows of level `> l - 1` are the new level-l rows, and every tested plaquette of level `l` is fresh at the step (Lemma 4.1 of `cov-global` (a)), with its certificate read on the values at the output of the step. So Lemma 4.1 holds without (pin): apply Lemma 2.2 to the rows of level `<= l - 1` only, which is all that the plaquettes of level `<= l - 1` read (their completed edges read level `<= l - 2`). The READ status of the pin in (S-gauge) therefore costs nothing.

**Repair R1 (text for section 3 of the file).** Correct the lines: (S-ent) 62173; (O-order) 62176; removal sentence 77758-77760; (P-late) 63862; (M-ref) 65471-65474; (T-cube) 77819-77820. Add to (M-slot) Y 78288-78290, to (M-int) Y 96361, to (M-last) Y 71426-71435. In (S-gauge) replace the citation of Y 4358 for the pin by: "(read; not used, see Lemma 4.1)". In (T-cube) say: "Y's floor is `c delta_0 M_2 >= 1` (Y 62001); `M_2 >= L` is an added choice, compatible with `L^2 M_2 <= M` when `M >= L^3`".

Verdict on item (1): HOLDS WITH REPAIR R1. Every clause is in Y as stated or as a reading of the lines named; none is contradicted by Y.

## Item (3). The ten weak-form statements, step by step: HOLDS WITH REPAIR (R2, R3, R4; none changes a statement that a consumer uses)

The algebra first.

- **Lemma 2.1.** HOLDS. In the ordered product the inner factors `g(x_i)^{-1} g(x_i)` cancel; a reversed edge enters as `g(e_+) V(e)^{-1} g(e_-)^{-1}`, the same pattern.
- **Lemma 2.2.** HOLDS. A completed edge of level `l` reads only level-(l-1) rows of its double block ((DB)); each moves by `u` at its ends; (MC) moves the average by `u` at the coarse ends `e_+-`, which are points of `Sigma`. Lemma 2.1.
- **Corollary 2.3.** HOLDS. For `l > q` a completed edge of level `l = q + 1` reads level-q rows that do move; (MC) and `u = 1` at the level-(q+1) ends give the same average. The proof covers this through Lemma 2.2; I checked it directly.

The statements of the table.

1. **(F-step), Lemma 4.1.** HOLDS. Each step: members of index `< l` unchanged (S-ent); level `q < l - 1` reads levels `q, q - 1`, not written (S-else); level `l - 1`: a corner in `Lay^det_{l-1}`, none in `Omega_l`, so tested before; edge kinds kept; rows moved by (S-gauge) only. (supp): `Lay^det_{q'} subset Omega_{l-1}^c subset Z_{l-1}` for `q' <= l - 2`, and a standing drop-out of level `s <= l - 1` is in `Z_s subset Z_{l-1}`; the draw is outside `hat Z_{l-1}^{~5}` (Y 75604-75605, 97398-97399). (pin) is not needed (item (1), remark). A mixed loop of level `l - 1` (a row edge and a completed edge at `dOmega_{l-1}`) is covered: its completed edge reads level-(l-2) rows in `Z_{l-1}`, where `u = 1`.
2. **(F-stage) and (D3\*), Lemma 4.2.** HOLDS. (a) A block with centre in `K_i^-` lies in `K_i` (aligned blocks); a moved bond has an end in the block and its other end within `L^i`; the block is at distance `>= 3 a_{i+1} - L^{i+1}/2 > L^i` from `X minus O_{i+1}`; so the bond is in the set of (m3) and is integrated in the same stage. Y says the same in words: "A link moved across the prepared inner face belongs to the collar" (Y 77776-77777). The new row `c` has `M(V_i)(c)` unchanged by the collar gauge ((MC), pin of Y 77767-77768). (b) Every write of another component `X'` has both ends within `L^t < 2 a_t` of `O_t(X') = X'^{[-2 a_t]}`, so in `X'`; `X cap X' = empty`; the core of `X'` is in `G_h(X') subset X'`. This is stronger than (D3\*) as `cov-xstar` uses it (a variable on a bond with an endpoint in X, not only a row). The late-stop writes of `X'` (tree gauge on bonds with an end in `Lambda^pr(X')`) are covered by the same inclusion.
3. **(F-stop) early, Lemma 4.3 (a).** HOLDS. No write after a failed regularity test; at the extension stop Y 78249-78253.
4. **(F-stop) collar split, Lemma 4.3 (b).** HOLDS. (supp): `supp u subset K_j subset X minus Z''_{j+1}`, and `Lay_{q'} cap X subset Z''_j` for `q' < j`; a level-j bond with an end in `supp u` has its other end in `Lay_j` (the shell `Z''_{j+1} minus Z''_j` is wider than `L^j`), so it is a row. The direct argument for level `j + 1` is correct: `3 a_{j+1} - L^{j+1}/2 > 3 L^{j+1}/2 + L^j`.
5. **Late stop, Lemma 4.3 (c).** HOLDS as a reduction to (TG); see item (5).
6. **(F-refresh), Lemma 4.5.** HOLDS WITH REPAIR R2. (a) and the loop part of (b) are right: for `l > t`, `dist(F(p), X) >= (M - 3/2) L^l >= L^{t+1}/2 > L^t` uses `M >= 2` and `L >= 3`, and the bonds of `B_main` are within `L^t` of `Lambda^pr`. **Defect.** (b) also claims that no "density test whose cube contains a corner of it reads through a double block that contains a bond of `B_main`". The proof bounds `F(p)` only. A level-(t+1) test reads the level-(t+1) bonds with both ends in `square^{~4}`, which reaches `4 w_{t+1} = 4 M_2 R_{t+1} L^{t+1}` beyond `square`; the gap that the proof uses is `M L^{t+1}` (Y 62083, `LM` in level-t units), and `4 M_2 R_{t+1} > M` is possible when `R_{t+1} > L^2 / 4`. So the claim is not proved. It is not used: (c) and Theorem 5.1 need only that no *edge value* of a tested plaquette reads the fresh slot, and a level-(t+1) density test certifies `p` through the four edge values of `p` (Lemma 5.1 (iv)), whatever else it reads. **R2 (text):** in Lemma 4.5 (b) delete "nor a density test whose cube contains a corner of it", and end (b) with "so no edge value of `p` reads a bond of `B_main`".
7. **(F-main), Lemma 4.4.** HOLDS. (b): the corners are in `X minus Z''_t = A^t_t` or in `Omega_t` (within `L^t < a_t` of X); every write is on a bond with an end in `Lambda^pr` or in the core. (c): a corner in `Lambda^pr` gives two edges in `B_main`; after (M-ref) all four edges are rows (X in the top member); (M-rev) is a gauge move on the level-t sites of `Lambda^pr`; Lemma 2.1. The tree gauge (M-tree) acts before the draw and on bonds with an end in `Lambda^pr` only, so it touches no plaquette of (b); this is why (TG) is not used here. Right.
8. **(R-ord), Lemma 5.1.** HOLDS, given the partition clause and the floor `M_2 >= L`. (i) cell side `M R_l L^l` over cube side `L M_2 R_l L^l` is `M / (L M_2) >= L`, a power of `L`. (iii) `w_l >= L^{l+1} >= 3 L^l > 3 L^l / 2`. (iv) for `SU(2)`, `norm(e^{iF} - 1) = 2 abs(sin(theta / 2))` and `abs(F) = abs(theta)`; on `2 sin(theta/2) <= 1`, that is `theta <= pi/3`, `theta / (2 sin(theta/2))` increases to `pi / 3`; so `abs(F) <= (pi/3) norm(e^{iF} - 1)`. (AV2) with `alpha = (pi/3) eps_l` gives `(2 pi / 3) eps_l`, and `2 pi / 3 < 2.1`. Y writes `2 eps_k` (Y 134117-134118), which treats the chord as the angle; the file's constant is the honest one, as `cov-xstar-check` R2 found.
9. **(R-last), Lemma 5.2.** HOLDS. The chain `Lambda^pr = H^{[4 u_t]} subset G_{k_0+1} subset H_t subset H_t^{[4 a_t]} = X^{[-6 a_t]}` is the one `cov-global-check` (10) checked; Y says `X^{~-6} = H^{~4}` itself (Y 71431). Healed means the test on every inset cube passed (Y 62105, 97609-97611).
10. **(R-core), Lemmas 5.3, 5.4.** HOLDS WITH REPAIR R3, R4 (and see item (4) for the constant).
    - Lemma 5.3 (a): `F(p) subset H^{[4 u_t + 5 L^t / 2]} subset H^{[8 u_t]} = O_{k_0+1}` (`5/2 <= 4 M`), corners outside `Z''_t = H^{[3 u_t]}`, `F(p)` misses `Z''_t` (aligned blocks): position (Q2) of `cov-xstar`; Theorem 6.1 there. Between `nu_t` and the draw no edge of `p` is written. Right. (b): a plaquette with all corners in `O_t` and none in `Lambda^pr supset Z''_t` has a corner in `K_{t-1}`, so it is in `Fr_{t-1}(X)` and Theorem 6.2 of `cov-xstar` applies; otherwise a corner in `Omega_t`, Lemma 5.1. `C_2'' >= 6 . 4^r L^2 > 2.1` and `e_t >= eps_t`. Right.
    - Lemma 5.4: the four-factor telescoping is right (`norm(V' - 1) <= abs(log V')`, unitary factors). `eps := 2 C_2'' e_t` makes the hypothesis strict. Right.
    - **R3 (citation).** Bałaban's Proposition 1 (CMP 122 (1989) 175, p. 194, which Y cites at Y 71488) puts the hypothesis on **all** of `Z cap Lambda^c`: "satisfying the regularity condition `abs(dV_k - 1) < eps` on the domain `Z cap Lambda^c`" (read from the page image of the owner's copy). So the narrow reading of Remark 5.5 (i) is not the source's reading. The file already proves the wide hypothesis (Lemma 5.3 (b)); the proof of Lemma 5.4 should cite it. **Text:** in the proof of Lemma 5.4 replace "Lemma 5.3 (a) gives the hypothesis" by "Lemma 5.3 (a), (b) give the hypothesis on every level-t plaquette of `X minus Lambda^pr`, which is Bałaban's domain `Z cap Lambda^c`".
    - **R4 (the form of the conclusion).** Bałaban's (1.78) bounds `abs(V_Lambda(dp') - 1)` "for `p' in Lambda`"; Y's restatement bounds `abs(dV_Lambda - 1)` with no restriction. The plaquettes of `B*(X)` with one, two or three corners outside `Lambda^pr` rest on Y's form. **Text:** add to Lemma 5.4: "The bound on the plaquettes of `B*(X)` that are not inside `Lambda^pr` is Y's form of the proposition (Y 71488, no restriction on `p`); Bałaban's (1.78) states it for `p' in Lambda`".

Verdict on item (3): HOLDS WITH REPAIR R2, R3, R4. First failing step: none of the statements; one unproved and unused clause in Lemma 4.5 (b).

## Item (4). (R-core): the constant, the ceiling, Remark 5.5: HOLDS WITH REPAIR (R5); Y's bound `C(M) eps_t` does follow

**The file's bound is a correct implication.** `(4 M_0 + 2 C(M) C_2'') e_t` under the ceiling `(4 M_0 + 2 C(M) C_2'') ebar(gamma) < a_Lambda` follows from Lemmas 5.3, 5.4 (item (3), 10). The ceiling contains `C(M) . 2 C_2'' e_t <= a_Lambda` (the proposition's hypothesis) and the class condition `< a_Lambda` on the plaquettes within distance 1. Right.

**From the invariant alone, Y's bound does not follow.** The certificates of the invariant are upper bounds. A plaquette `q in Ext(X)` whose last fresh move is the last stage has as certificate the guard of position (Q2), with allowance up to `C_2'' e_t = C_2'' R_t^2 eps_t`. A configuration with `norm(dV_t(q) - 1) = 10 eps_t` on one such `q`, and every other certificate met, satisfies the invariant (`10 eps_t < C_2'' e_t` since `C_2'' >= 6 . 4^r L^2`). For it the proposition gives only `C(M) . 10 eps_t`, and with `q` at defect `C_2'' e_t / 2` only `C(M) C_2'' e_t / 2`. So Remark 5.5 (ii) is right that the *certificates* do not give `C(M) eps_t`.

**But the point carries one more test, and it gives the bound.** Remark 5.5 (ii) says: "The passed extension test (2) gives an extension with curvature below `2 eps_t` on the plaquettes that contain a bond of the extension; it is not a bound on the exterior plaquettes." That reading is contradicted by Y and by Bałaban:

- Bałaban, CMP 122 (1989) 175, p. 193, (1.75) (read from the page image): `chi_{k,Lambda} = chi({ inf_{V_k restricted to Lambda} sup_{p in Omega_k^c} abs(U_{k,Z}(dp) - 1) < 2 eps_k eta^2 })`. The sup runs over the bare plaquettes of the whole region `Omega_k^c` of the component, the exterior part included. His (1.80) then uses `chi_{k,Lambda}` to get `abs(U_0(dp) - 1) < 2 eps_k eta^2 + O(1) B_3 B_5 M^5 exp(-delta dist(p, Lambda)) eps_k eta^2`: an exterior bound of order `eps_k`.
- Y 71437-71441: "the new `V_k` gives an extension whose localized bare plaquettes on `Omega_k^c cap X` are strictly below the `2 eps_k eta_k^2` threshold of `chi_{k,Lambda}`."
- Y 78266-78276 (the extendibility stop): "In the top inset the localized critical configuration for this extension has bare curvature bounded by this number times `C L^{-2i}`. The required region `Omega_i^c cap X` lies in that inset."
- Y 76434-76437: "The extendibility indicator reads only the part of `V_i` outside the central box ... The infimum in that test gives a predicate on the exterior."
- `eta_j = L^{-j}` (Y 593), so the threshold is `2 eps_t L^{-2t}` on bare plaquettes.

**(X-ext), read from these lines.** `chi_{t,Lambda} = 1` at a point if and only if there is a configuration `E` of the level-t bonds of X with `E(b) = V_t(b)` on every bond with no end in `Lambda^pr`, whose localized background `U = U_{t,X}(E)` exists, satisfies `M^t U = E` on the level-t bonds with both ends in X (the analogue of (T-dens); Y 134119 "the localized orbit has the prescribed `V_k` there"), and has `norm(dU(q) - 1) < 2 eps_t L^{-2t}` for every bare plaquette `q subset Omega_t^c cap X`. In the quiet boxed nest `Omega_t^c cap X = H^{~8} = O_t` (Y 71429-71430). `chi_{t,Lambda}` is a factor of the term from the test (2) on (Y 63839-63842), it reads only exterior bonds, and an island keeps it (Y 71480-71483).

**Lemma A (exterior bound of order `eps_t`; proved from (X-ext), (AV2), and the write sets of section 3).** Let `(2 pi / 3) eps_t <= alpha_L`. On an admitted trajectory, at every point of the main step of X after the test (2) and up to the draw (M-ref), every `q in Ext(X)` has `norm(dV_t(q) - 1) <= (4 pi / 3) eps_t < 5 eps_t`.

*Proof.* `chi_{t,Lambda}` is carried, so it equals one; take `E`, `U` as in (X-ext). By the proof of Lemma 5.3 (a), `F(q) subset H^{[4 u_t + 5 L^t / 2]} subset O_{k_0+1} subset O_t`. The edges of `q` have no end in `Lambda^pr` and both ends in X, so `(M^t U)(e) = E(e) = V_t(e)` on them. Every bare plaquette of `F(q)` has chord defect `< 2 eps_t L^{-2t} <= 1`, so angle `<= (2 pi / 3) eps_t L^{-2t}` (item (3), 8). (AV2) with `alpha = (2 pi / 3) eps_t` gives `abs(F_q(V_t)) <= (4 pi / 3) eps_t`, and `norm(e^{iF} - 1) <= abs(F)`. The datum loop of `q` is this loop: its edges are rows (corners in `K_{t-1}`), and between the test and the draw no move writes a bond with no end in `Lambda^pr` ((M-int), (M-tree), tests). `square`

**Lemma B (Y's form of (R-core)).** Let `5 C(M) ebar(gamma) <= a_Lambda` and `(4 M_0 + 5 C(M)) ebar(gamma) < a_Lambda`, with `ebar(gamma) >= eps_t`. After the main step with outcome island or healed, every `p in B*(X)` has `norm(W(p) - 1) <= (4 M_0 + 5 C(M)) eps_t`.

*Proof.* The proof of Lemma 5.4 with `eps := 5 eps_t`. The hypothesis of the proposition: on `Ext(X)` by Lemma A (narrow reading). On Bałaban's domain `X minus Lambda^pr` (wide reading, R3): a plaquette with all corners in `O_t^{[-4 a_t]}` has `F(q) subset O_t` (`3 L^t / 2 < 4 a_t`) and Lemma A's argument applies; a plaquette with a corner in `X minus O_t^{[-4 a_t]} = X cap Omega_t^{~4}` has a corner in a carried level-t density cube of `Omega_t^{~4}` (Y 64096-64097, 71431-71433, "the carried `chi_k(Omega_k^{~4})`"), and Lemma 5.1 (iii), (iv) give `(2 pi / 3) eps_t`, carried to the draw as in Remark 5.6 of `cov-global`. `square`

So Y's bound holds with `C(M)` read as `4 M_0 + 5 C(M)` (Y chooses `M_0` after `M`, Y 63856, so this is a constant of the form `C(M)`), and Y's "`psi_l` is `O(1)` for ... a restored core" (Y 65476-65478) is recovered. The narrow reading uses one read clause, (X-ext). The wide reading adds the carried density cubes on `Omega_t^{~4}`, the read statement that `cov-global-check` (14) names for Remark 5.6.

**R5 (text for Remark 5.5 (ii) and section 0, item 2).** Replace the sentences from "The passed extension test (2) gives an extension ..." to "... is not recovered" by: "The test (2) is `chi_{t,Lambda}` of Bałaban's (1.75) (CMP 122, p. 193): an infimum over extensions of the sup of the localized bare curvature over `Omega_t^c cap X` (Y 71437-71441, 78266-78276). It is carried to the draw, and it bounds every plaquette of `Ext(X)` by `(4 pi / 3) eps_t` (check row 646, Lemma A). With `eps = 5 eps_t` the proposition gives `(4 M_0 + 5 C(M)) eps_t` on `B*(X)`, under `(4 M_0 + 5 C(M)) ebar(gamma) < a_Lambda`; this is Y's `C(M) eps_t`. The bound `(4 M_0 + 2 C(M) C_2'') e_t` from the certificates alone also holds and is what the consumers need." In section 0, item 2, and in the tables of sections 0 and 7, the constant may stay as a valid weaker bound; the sentence "I could not derive an exterior bound of order `eps_t`" should go.

Verdict on item (4): HOLDS WITH REPAIR R5. The constant and the ceiling are right; Remark 5.5 (ii) misreads the extension test, and Y's bound follows from it.

## Item (5). The late stop: HOLDS (the move is in Y; the reduction to (TG) is right)

**Y has the move.** Read in this session:

- Y 63836 (0): "Consequently no frame sum is attached to a component that leaves at (2) or during the stages ... If a component leaves after the tree gauge, its frame sum stays with it."
- Y 63862: "If one of the tests of (1)--(3) fails in a component, that component drops out"; the test on `B` and the last-shell test are made in (3) after the tree gauge (Y 63849-63855).
- Y 75677-75686: "There is a different first chart for a component that stops at the shell-field or last-shell test, after central integration and before reference restoration. Central integration has consumed the old box field ... Its frame tree acts on the old shell variables."
- Y 78285-78296 ("The tests retained at a late stop"): "A shell or last-shell failure occurs after the final preparatory guard and the central integration ... Use the prepared datum for the regularity comparison and the fresh outgoing field for the later averaging rows that read it."
- Y 62107: a drop-out fails "after `n <= N_t` stages"; `n = N_t` is allowed. So the late stop is the drop-out of (R4) with `n = N_t`, as the file says.

`cov-global` lists the stop only before the main step (its 4.1, (F-stop) "after `n` completed stages, of either kind"); the file is right that this move is missing there.

**The steps of the reduction (Lemma 4.3 (c)).**

1. The determining sequence does not change: (R4), the sequence of a drop-out after `N_t` stages. HOLDS.
2. The central integration changes no determining row: (M-slot), with Y 76677-76679 and Y 78288-78290 ("Use the prepared datum"). The fresh slot is read by no edge of a tested plaquette while X stands: Lemma 4.5 (b) (loop part; R2). HOLDS.
3. The frame sum writes nothing: Y 63836 (0) inserts `1 = abs(W_4)^{-1} sum_r 1`. HOLDS.
4. The tests write nothing: (P-test). HOLDS.
5. The tree gauge: if it is a site-gauge move (that is (TG)), Lemma 2.2 conjugates every tested loop. HOLDS as an implication.
6. The set at stake without (TG). The tree gauge has `u = 1` at the exterior root (Y 75684-75686, "at fixed exterior root") and in the core (Y 63849, "at no point unfolded"); it can move only bonds with an end at a shell site of `Lambda^pr minus C_h`. A tested plaquette is at stake only if an edge, or a row of the double block of a completed edge, has such an end. The file's description ("levels `h, ..., t` with a corner in `Lambda^pr minus G_h`") is right up to this wording; a level-(q+1) plaquette whose completed edge reads level-q shell rows has its corners within `L^{q+1}` of the shell, so its corners are in `Lambda^pr` or within `L^t` of it. No change to a consumer.
7. (TG) is not needed for healed and island: at those outcomes the tree gauge acts before the draw, on bonds with an end in `Lambda^pr` only; the plaquettes of levels below `t` with a corner in X stop being tested (Lemma 4.4 (a)); those of `B*(X)` are fresh; the others have no edge written. HOLDS.

**For row 647 (not a proof; a pointer).** Y 78322-78326 may make (TG) unnecessary rather than true: "Before marginalizing the central integral, keep its prepared variables. In the framed integral these are `V'' = V' V_0` on the changed coordinates, with `V_0` formed from the retained exterior. This substitution recovers the same datum in each frame summand." Read with Y 75694-75696 ("This permits weights to be evaluated on the reconstructed old shell without imposing any tree condition"), this says that the datum kept at a late stop is the prepared datum `V''` itself, recovered from the tree coordinates, not its image under the tree gauge. If row 647 reads it that way, the late stop has the *same* loops (not only conjugate ones), as at a collar split with the untransformed variables retained (Y 97586-97587). I did not check this reading against the frame-sum bookkeeping of Y 63836 (0); it is row 647's question.

Verdict on item (5): HOLDS. The late stop is a move of Y; Lemma 4.3 (c) is a correct reduction to (TG); (TG) stays open (row 647).

## Item (6). The weak form is enough for its uses: HOLDS (the late stop given (TG))

**`cov-global` Theorem 5.1.** Its proof uses the frame statements only through Lemma 4.1 there (the fresh sets) and Lemma 5.2 (carrying). Lemma 5.2 needs "carried over" in the sense of Definition 4.0: tested before and after, loop conjugate. That is the conclusion of every weak statement of the file. Use by use:

| Use in `cov-global` | What it needs | Given by | Holds |
|---|---|---|---|
| Lemma 4.1 (a), step | level `< l`: tested before, conjugate loop | Lemma 4.1 of the file | yes |
| Lemma 4.1 (b), stage | levels `<= i`: same four values; level `i + 1`: fresh only in `Fr_i(X)` | Lemma 4.2 (a) (with (D1), (D2) at the last stage, `cov-global-check` defect 1) | yes |
| Lemma 4.1 (c), stop and refresh: no fresh plaquette | conjugate loops | Lemma 4.3 (a), (b), Lemma 4.5 (a) | yes |
| the same, late stop (missing in `cov-global`) | conjugate loops | Lemma 4.3 (c) | **given (TG)** |
| Lemma 4.1 (d), main step | fresh only in a set that has a certificate | Lemma 4.4, with `B*(X)` | yes |
| table rows 3, 4 of Theorem 5.1 | certificates on the fresh set | Lemma 5.2 (healed), Lemma 5.4 or Lemma B of item (4) (island) | yes |
| Lemma 5.3 (c), the rim of a mark | plaquettes of the main step of C have all corners in C | `B*(C)`: corners within `L^s` of `Lambda^pr(C) subset C^{[-6 a_s]}` | yes |
| "How the cases come out", footprint astride the rim | not fresh at the main step | no corner in `Lambda^pr` (the rim is at distance `>= 6 a_t - L^t` from `Lambda^pr`) | yes |

The text changes the file lists for `cov-global` (its section 7, item 1) are right and complete for these uses, with one addition: in Lemma 4.1 (c) of `cov-global`, add "a late stop: none, given (TG)", and in the island row of the table of Theorem 5.1 the constant may be `(4 M_0 + 5 C(M)) eps_t` (item (4)) instead of `(4 M_0 + 2 C(M) C_2'') e_t`.

**`cov-xstar` (X5), "Carrying".**

- At the extension stop: Lemma 4.3 (a) gives the same loop. This is R4 of `cov-xstar-check` (only the weak form is needed). Holds.
- At the main step: Lemma 4.4 (b) for the plaquettes of `Fr_{t-1}(X)` with no corner in `Lambda^pr`; those with a corner in `Lambda^pr` are fresh and get (R-last) or (R-core). This is R5 of `cov-xstar-check`, which was conditional on change (1); item (2) confirms change (1), so R5 applies unconditionally. Holds.
- At a late stop: the plaquettes of `Fr_{t-1}(X)` with no corner in `Lambda^pr` keep their loop ((M-tree) writes only bonds with an end in `Lambda^pr`); those with a corner in `Lambda^pr minus Z''_t` (the level-t shell) need (TG). The file says this. Holds given (TG).
- (D3\*): Lemma 4.2 (b), in the stronger form (no write on any bond with an endpoint in X), up to the end of the main step. Holds.

Verdict on item (6): HOLDS; at a late stop, given (TG) (row 647).

## Item (7). What is cited, and from where

- **(M-cut)** is Y's own construction, not a cited theorem. Its sources: Y 63856 (the cut-off `chi(Lambda^pr) = 1{abs((1/i) log V'(b)) < M_0 eps_k on the bonds of the box}`, `M_0` "chosen large after `M`", in the numerator and the denominator of the reference law `s_X`); Y 72678-72686 (the cutoff "restricts `V'_m = V_m V_Lambda^{-1}` to its reference ball. Its complement carries zero mass under that law. There is no failure event for that cutoff on the free Haar argument"); Y 71447-71454 (healed: the density and minimiser bounds give `abs(log(V_k V_Lambda^{-1})(b)) <= C(M) eps_k < M_0 eps_k`, so `chi(Lambda^pr) = 1` on the passing support); Y 71480-71483 and 63836 (0) (an island keeps the cutoff). What the file uses: after the draw, `abs(log V'(b)) < M_0 eps_t` on every bond of `B_main`. That holds on the support of the reference law; on an admitted trajectory it is a carried factor and equals one. The set of bonds is the set of the reference law, `dV' restricted to Lambda^pr`, which item (2) reads as `B_main`.
- **'Minimiser in a box'** is cited twice over. (i) Y's Proposition `prop:large-field-2-4` (Y 71488), with Y's constants `a_Lambda`, `C(M)` chosen after `M` and before `gamma`, the hypothesis "the exterior data satisfy `abs(dV_k - 1) < eps` with `C(M) eps <= a_Lambda`", the class "`abs(dV_k - 1) < a_Lambda` at those level-k plaquettes whose corners all lie within distance 1 of `Lambda^pr`", the conclusion "exactly one critical gauge orbit `V_Lambda` ... `abs(dV_Lambda - 1) <= C(M) eps`", and `U_0 := U_{k,X}(V_Lambda)` with `J(U_0) = 0` in `Lambda^pr`. Y's proof sketch is Y 71491-71497 (contraction in an `M`-dependent ball; axial-gauge Hessian bound `c M^{-5}`; the Poincaré inequality of Bałaban CMP 122 (1989) 355, (1.7)-(1.9)). (ii) Y names its source: Bałaban, CMP 122 (1989) 175, Proposition 1, p. 194 (read from the page image): hypothesis `abs(dV_k - 1) < eps` "on the domain `Z cap Lambda^c`", `eps` sufficiently small; conclusion: exactly one critical orbit of `V_k restricted to Lambda -> A(U_{k,Z}(V_k))` (his (1.77)), a minimum, with `abs(V_Lambda(dp') - 1) < B_5 M^5 eps` "for `p' in Lambda`" (1.78), and an analytic extension. Bałaban says (p. 194) "We will prove later"; the proof is in that paper (Y cites pp. 193-196). Differences that the file's use touches: the domain of the hypothesis (R3), the plaquettes of the conclusion (R4), and `C(M)` for `B_5 M^5`. Neither (M-cut) nor the proposition is rebuilt in `library/`; both stay **cited**.

Verdict on item (7): what is cited is as above. The file's "form used" of the proposition needs R3 and R4.

## Item (8). Ten quoted Y passages against Y: HOLDS

| # | File's quote (place in the file) | Y line (checked) | Faithful? |
|---|---|---|---|
| 1 | "a function of `V_k` on the level-`k` bonds having an end point in `Lambda^pr`" (section 0) | 71488 | word for word |
| 2 | "Central integration has consumed the old box field, including the bonds crossing its boundary. The resulting term has unrestricted fresh Haar coordinates on the bonds with an end in the box" (section 0) | 75679-75683 (file: 75680-75684) | word for word |
| 3 | "the Haar refresh uses the box coins and keeps the old variables for the prepared datum" (M-int) | 97597-97598 | word for word |
| 4 | "A late Haar refresh leaves the old determining datum in the inner slot. The fresh field is used by the outgoing rows" (M-slot) | 76677-76679 | word for word |
| 5 | "A retained row at a bond address shared by the fresh field still reads its old slot" (M-slot) | 76038-76039 | word for word |
| 6 | "The cutoff in the subsequent draw restricts `V'_m = V_m V_Lambda^{-1}` to its reference ball. Its complement carries zero mass" (M-cut) | 72682-72685 | word for word |
| 7 | "The test of `chi_j(X^{~-6})` is made on the newly drawn field in the inset test cubes. Its full local test neighbourhoods stay in X" (M-last) | 97609-97611 | word for word |
| 8 | "only the last test fails, namely `chi_t` of the new field on X less a margin" (M-last) | 62106 | word for word |
| 9 | "the retained determining list still has index `n`" (P-collar) | 77793-77794 | word for word |
| 10 | "The core operation ..., which contains the failed tests, is at no point unfolded" (M-tree) | 63849 | word for word; the elision is "`T_{k_flat}(C_{k_flat})`" |
| 11 | "the plaquette bound at `V_Lambda` is `C eps_m`" (Remark 5.5) | 72691-72692 | word for word |
| 12 | "Because it is a power of `L`, all partitions are nested" (T-cube) | 62001 | word for word, but in Y the subject is `R_k` (the size `R_k` is a power of `L`), not the test cube; the file uses it for the cube grid. With `M_2` a power of `L` the inference is right; the quote alone does not say it |

Line offsets of at most 5 (items 2 and those in R1). No quotation changes the sense of Y. Item 12 is a use of a true sentence for a neighbouring claim; it is covered by the READ label of (T-cube) in item (1).

Verdict on item (8): HOLDS.

## For the lead (I edited no other file)

1. `library/cov-frames.md`: apply R1 to R5 (texts in items (1), (3), (4)).
2. Registry row COV, note of 2026-11-10 after the three checks: "Y 63836 says 'both ends'" should read "Y 63836 does not say which bonds; Y 71488, 75679-75683, 75700-75704 and 96361 say 'an end'".
3. `cov-xstar-check` R5 is no longer conditional (item (2) confirms change (1)).
4. Row 647 (`late-stop-tg`): read Y 78322-78326 and 75694-75696 first (item (5)); they may give the same loops at a late stop without (TG).
5. Row 642 (`cov-apply`): the island constant can be Y's, `(4 M_0 + 5 C(M)) eps_t`, at the cost of the read clause (X-ext) (item (4)); the certificate-only constant `(4 M_0 + 2 C(M) C_2'') e_t` needs no new clause.

RESULT: cov-frames (row 638) HOLDS with five repairs, no item fails, first failing step none: the clauses of section 3 are in Y (six line corrections; the pin of the step's gauge draw is read and not needed; M_2 >= L is an added choice); change (1) is right, Y says "an end" at 71488, 75679-75683, 75700-75704 and 96361 and Y 63836 says neither, so the registry's "Y 63836 says both ends" is wrong; all ten weak-form statements hold (Lemma 4.5 (b) has one unproved, unused clause on density tests; Lemma 5.4 must use Bałaban's wide hypothesis on Z cap Lambda^c, which Lemma 5.3 (b) gives); the late stop is a move of Y and its reduction to (TG) is right; the weak form is enough for cov-global Theorem 5.1 and cov-xstar (X5). New: Y's bound C(M) eps_t for (R-core) does follow, not from the certificates but from the carried extension test chi_{t,Lambda} (Bałaban CMP 122 p. 193 (1.75), Y 71437-71441, 78266-78276), giving (4 M_0 + 5 C(M)) eps_t; Remark 5.5 (ii) of cov-frames misreads that test. Open: (TG) for the late stop (row 647; Y 78322-78326 may remove the need for it); the read clause (X-ext) on the domain of chi_{t,Lambda}; the partition of cells by test cubes; 'minimiser in a box' and (M-cut) cited, not rebuilt.
