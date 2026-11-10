lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T00:28Z

# cov-frames-check: line-by-line check of `library/cov-frames.md` (FINISH row 646)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, branch `claude/ym4d-hard-route` at 3591d5adc, 2026-11-10. A check by a second Claude model of a file written by Claude Fable 5.2 (medium); same provider, so not a cross-provider check. Not an audit. Source Y = `YM4_1400.tex` of the Sussman-Alpoge experiment repository (ethanwsussman/Yang--Mills-LLM-experiment at 2bc0658f91d2), credited to Sussman and Alpoge with Claude and Codex as authors of its text.

Verdict: (in progress; written at the end)

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

