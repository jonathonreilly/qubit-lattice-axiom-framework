lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-11T00:59Z

# cov-apply (FINISH row 642): log of the repairs applied to cov-global.md and cov-xstar.md

Provenance: Claude Opus 5.5, medium effort, Mac mini worker 2, at commit b8ca1b907. Not an audit. Repairs from `library/cov-global-check.md` (row 636) and `library/cov-xstar-check.md` (row 639), both by Claude Opus 5.5 high.

## Repo search

Searched this lane folder for `cov-apply`: FINISH row 642 (this row), the COV row of `library/open-registry.md`, item 5 of `library/cov-frames-check.md` (an optional island constant addressed to this row, not in the row text; see the end), and `library/i3-apply.md` (names this row only). No earlier application of these repairs exists. No open lemma is attacked here.

## Log

### (a) `library/cov-global.md` (repairs of `library/cov-global-check.md`, section 4)

Every edit below was a text replacement whose old string matched exactly once. No other statement or proof step was changed.

1. Defect (1). Section 4.3, (COV-X*): after "`nu_h <= mu <= nu_{i+1}`", added "with defect at `x_{nu_{i+1}}` at most `C_2'' e_{i+1}`, where `C_2'' = max(C_2, 6 . 4^r L^2)` (the form of `library/cov-xstar.md` Theorem 6.1)". APPLIED.
2. Defect (1) and the row's own item. Theorem 5.1, second row of the table: `<= C_2' e_l` (`cov-x` Theorem 6.1) became `<= C_2'' e_l`, `C_2'' = max(C_2, 6 . 4^r L^2)` ((COV-X*); cov-xstar Theorem 6.1). APPLIED.
3. Defect (1), the matching proof line. The last line of the proof of Theorem 5.1 now says the bound in the second line is the allowance of (COV-X*), carried by Lemma 5.2. Before, it read "`cov-x` Lemma 3.2 with the allowances of its Theorem 6.1". APPLIED. This is the proof step the defect names: once the allowance is stated, the line rests on it.
4. Defect (2). Section 4.1, (F-stage): added a sentence. At `i = t - 1`, (F-stage) is the read hypothesis (D3*) of cov-xstar, that is (D1), (D2), (D3) at the last stage with exit `nu_t` and `A^t_q = X minus Z''_q`, citing Y 64097-64100, 64119-64124 and 77644-77645. Y states it in prose, not at the level of rows. APPLIED.
5. Defect (2). Proof of Lemma 4.1 (b), "Levels `q <= i`": added that cov-x Lemma 5.1 (b) is stated for `i < t - 1`. At `i = t - 1` its proof reads only (D1) and (D2), and it goes through word for word with (D3*). APPLIED.
6. Defect (3). Section 4.2, (R-ord): after "The test cubes of level `l` partition each level-l cell", added a note. The clause is not stated in Y (Y 62001 gives only "side of order `M_2 R_l`, well inside a cell"). It is a choice of the construction: the grid of side `M_2 R_l L^l`, with `M` a power of `L`. APPLIED. The fit with every other choice of `M` is not proved here, as the check says.
7. Defect (4). Proof of Lemma 5.3 (c), in the list of possible last fresh moves: added "nor the main step of C itself, whose box plaquettes have all corners in C (every corner is within `L^s` of `Lambda^pr(C) subset H_s(C) subset C^{[-6 a_s]}`)". APPLIED. The justification in parentheses is the one from item (11) of the check.
8. Defect (5), the constant 2.1. (R-ord): added that 2.1 is not a number in Y (Y 76667-76668, "of order `eps_q`"). It is (I4) of `library/rim-scale.md`, with the constant of `rim-scale-check.md`. APPLIED. The note also gives the derivation from Y 134117-134118 found later by `cov-xstar-check.md` R2: `2 arcsin(eps) <= (2 pi/3) eps < 2.1 eps` for `eps <= 1/2`. The two checks agree on this: rim-scale is the repository source, and Y gives `2 eps` for `abs(dV - 1)`. I verified the inequality by hand: arcsin is convex on `[0, 1]`, so `arcsin x <= (pi/3) x` on `[0, 1/2]`, because `arcsin(1/2) = pi/6`.
9. Defect (5), the reference bound. Finding 5 of section 0 and the head of (R-core): "Y 63836 (2), 63876 (4)" became "the reference bound Y 71488 (with Y 63864 as summary); the extension test Y 63836 (2)". APPLIED. The citation "63876 (4)" in the head of (F-main) was left as it was, because the defect is about the reference bound and not F-main. NOT APPLIED there, for that reason.
10. Defect (5), the conjugation sentence. "Y 76674-76676" became "Y 76676-76677" in all three places: (F-step), (F-main) and section 6 item 2. APPLIED.
11. Defect (5), R1. Section 2: "`R_l` is a power of `L` and is non-increasing in `l` (Y 62001)" now says `R_k <= L R_{k+1}` and that the partitions are nested, quoting Y 62001, with "non-increasing alone would not give this". APPLIED.
12. Defect (5), Lemma 3.0. "An operation of level `s > m`" became "`s >= m` other than the one on C". A parenthesis was added: for `s = m` the components are other components of `Z_m(S'_m)`, so they are disjoint from C. APPLIED.
13. The row's item: `R_h >= 1` and `M >= 2` in Lemma 3.2. Both are added to the hypotheses ("with `M >= 2` and `R_h >= 1`"). In the proof of (iii), the chain is now `a_h = M R_h L^h >= M L^h >= M L^{m+1}`, with the reason for `R_h >= 1` (Y 62001: the smallest power of `L` not less than `(log min x_i)^r`, which is at least 1 when `min x_i >= e`). APPLIED.
14. Defect (6) (i3-cert, (c2') form of (COV)). NOT APPLIED: the row gives it to row 643, and `i3-cert.md` is not an output of this row.
15. Not applied, because the row text does not name them:
    - the 4.3 table rows still marked **gap**. Item (16)(a) of the check confirms they are instances of cov-xstar Theorem 6.1.
    - the list of hypotheses that Y does not state, which is in section 4 of the check: the island exterior bound `eps <= 2 eps_k`, the set of "bonds of the box", and the density cubes on `Omega_t^{~4}` for Remark 5.6. The partition clause, the constant 2.1 and the F-stage at the last stage are labelled by edits 4, 6 and 8.
    - section 6, "What stays open", item 1 and item 4. These are now out of date: row 633 is done, and cov-xstar proves item 1.

    These are for the lead.

### (b) `library/cov-xstar.md` (R1 to R5 of `library/cov-xstar-check.md`)

Each edit replaced text that matched exactly once and used the repair text of the check word for word. Only connecting words were changed.

16. R1, first place. Finding 1, second sentence: "it does not meet `dO_{i+1}`" became "it is not astride `dO_{i+1}` (it lies in `O_{i+1}`; it can touch the face from inside, and it is then inside one region of (X1))". APPLIED.
17. R1, second place. The last sentence after Lemma 3.1: "in no case does `F(p)` meet `dO_{i+1}` or leave `O_{i+1}`" became "in no case is `F(p)` astride `dO_{i+1}` or outside `O_{i+1}`", followed by the same parenthesis. APPLIED.
18. R2, Step 2 of Lemma 5.1. After "(I4_{l'})", added: Y 134117-134118 gives `abs(dV_{l'} - 1) <= 2 eps_{l'}`, so `abs(F) = 2 arcsin(norm/2) <= 2 arcsin(eps_{l'}) <= (2 pi/3) eps_{l'} < 2.1 eps_{l'}` for `eps_{l'} <= 1/2`. APPLIED. Checked by hand: arcsin is convex on `[0, 1]`, and `arcsin(1/2) = pi/6`.
19. R2, Step 2, second part. "a union of level-l' cells" became "and every site of it lies in a level-l' cell inside `O_{l'+1}^{[-a_{l'+1}]} minus O_{l'}^{[-4a_{l'}]}`". APPLIED.
20. R3. In the hypotheses of Theorem 6.1, after "(T1), (T3) of `i3-cert`", added "(LF) (or, without (LF), read `C_2` as the constant `2 . 4^r L^2 L_flat^2 A_L` of i3-cert 5.3)". APPLIED.
21. R4. Section 6, "Carrying" in (X5): "a stop at the extension test changes no row and no entry ((F-stop) of `cov-global`), so `p` is carried over with the same loop" was replaced by the weak form. At a stop at the extension test, `p` stays tested and its loop changes at most by conjugation (the weak form of (F-stop), row 638). That is the hypothesis of Lemma 5.2 of cov-global, which uses only the conjugacy class of the loop. APPLIED.
22. R5. Applied as the row directs, since the lead found Y 71488 as `cov-frames.md` quotes it. In (X5), "a plaquette of `Fr_{t-1}(X)` with no edge in the box" became "... with no corner in `Lambda^pr`". "A plaquette with an edge in the box is fresh" became "A plaquette with a corner in `Lambda^pr` is fresh". APPLIED. As the check says, this does not touch Theorem 6.1.

## Note for the lead (no edit made)

- **Bonds of the box: the two files now use different sets.** After R5, cov-xstar (X5) uses the one-end set (the level-t bonds with an end in `Lambda^pr`, as at Y 71488). cov-global (F-main) still says "the level-t bonds with both ends in `Lambda^pr`", and Lemma 4.1 (d) and `B(X)` are built on that. Under the one-end reading, the (F-main) clause "a level-t plaquette with no edge in the box ... loop conjugated" is false for a plaquette that has a corner in `Lambda^pr` and only one-end bonds. Such a plaquette is redrawn. `cov-global-check.md` item (6) found that cov-global holds under either reading, provided (F-main) and (R-core) use the same set. To make the two files agree, cov-global needs three changes: "both ends" becomes "an end" in (F-main); `B(X)` becomes "the level-t plaquettes with an edge in the box" under the one-end set, which includes the plaquettes with a corner in `Lambda^pr`; and the healed case of Theorem 5.1 must then cover corners within one level-t unit of `Lambda^pr`. The check says this case still holds. I did not make these changes, because the row does not name them.
- Not applied, because the row does not name them (see edit 15): the "gap" rows of the table in 4.3 of cov-global, its section 6 items 1 and 4, and the hypotheses of section 4 of cov-global-check that Y does not state (`eps <= 2 eps_k` at an island, the set of box bonds, and the cubes on `Omega_t^{~4}` for Remark 5.6).
- `cov-frames-check.md` item 5 offers this row an optional island constant `(4 M_0 + 5 C(M)) eps_t`, at the cost of the read clause (X-ext). It is not in the row text, so it is NOT APPLIED.
- Row 643 still owns defect (6) of cov-global-check, the (c2') form of (COV) in `i3-cert`.

No proof by computer. No numeric job was run. The only edits were to `library/cov-global.md`, `library/cov-xstar.md` and this log.

RESULT: All the named repairs are applied: to cov-global.md, defects (1) to (5) of cov-global-check, plus R_h >= 1 and M >= 2 in Lemma 3.2 and C_2'' = max(C_2, 6 . 4^r L^2) in Theorem 5.1; to cov-xstar.md, R1 to R5 of cov-xstar-check, R5 included. Not applied, as outside the row: defect (6) (row 643), the gap rows in the 4.3 table, and the list of hypotheses Y does not state. Open: cov-global still uses the both-ends set of box bonds in (F-main) and B(X), while cov-xstar now uses the one-end set; the lead should choose one set for both files.
