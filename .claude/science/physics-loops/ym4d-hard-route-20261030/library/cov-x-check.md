lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T16:38Z

# Check of `library/cov-x.md` (row 633)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, commit 5b09dbe3b. This is one line-by-line check by a model that did not write `cov-x.md` (Claude Fable 5.2 wrote it). It is not an audit. Source: YM4_1400.tex at Sussman-Alpoge commit 2bc0658f91d2, fetched by URL into an own scratch folder (136,637 lines). "Y n" is line n of that file. The source text is by Sussman and Alpoge, with Claude and Codex as authors of their text. The stage test and the nest are Bałaban's (CMP 122). No numerics were run. No subagents were used.

Repo search: `library/open-core.md` has no COV entry. FINISH rows 622, 628, 630, 632 and 634 are near this item, but none checks `cov-x.md`. I attacked no open lemma. Case P1 (levels below `h`) belongs to row 632, and I did not touch it.

## 0. Verdict

**(COV-X) for levels `>= h`: HOLDS** as an implication from D1 to D6. I found D1 to D6 to be fair readings of Y. The first failing step is none. Theorem 6.1 and the seven cases stand as written.

I found two defects. Neither breaks (COV-X).

- **(d1) Section 7 does not give Lemma 6 of `i3-cert` verbatim.** Definition 7.1 removes the rim top plaquettes from the tower holonomies (level `m`, not interior). Corollary 7.3 therefore carries an extra hypothesis: "no corner in a carried top density cube". Theorem 9.1 (i) of `i3-cert` covers every non-tower holonomy and has no such exclusion. The remarks of `i3-cert` (lines 443 and 594) say that (i) excludes these plaquettes, but the theorem's text does not say so. Short repair, matching Y: let a tower holonomy be any tested plaquette that is not interior, at every level. Y 13100-13102 has exactly two kinds: "Either `R(p) ⊂ W^{(-2)}`, or `R(p) ⊂ Q_a` for a part with `q <= j_a`", with `j_a = m`. Then "not a tower holonomy" means interior, and Lemma 6 is Lemma 7.2 (a) word for word. Level-m collar plaquettes are then bounded through (R1), as Y does at Y 13118-13125. The other repair is to add the exclusion to the text of Theorem 9.1 (i).
- **(d2) Edit 3 of section 8 is not enough.** The constant `C_2' = max(C_2, 6 . 4^r)` must also replace `C_2` in the coupling ceiling (H5) of `i3-cert` Theorem 9.1, which reads `C_2 ebar(gamma) <= alpha_L` and `c_0 C_2 ebar(gamma) <= min(eps_L, L^2/C_L)`. The coarse supplier of P5b needs `alpha = 3 . 4^r e_j <= alpha_L`, and case A of Lemma 4 then reads `eps(W; D(P)) <= c_0 C_2' e_j`. Both need the ceiling with `C_2'`.

## 1. Item (1): D1 and D2 — HOLDS

- **D1.** Y 72244-72250: "The only member of the sequence that changes is the one of index `j+1`, which grows from `Omega_{j+1}` to the prepared member." Y 63836, operation (1): the stages run for `j = k_flat, ..., k-1`, "one value after another". So at the entrance `nu_i`, the members `h < q <= i` are prepared (`X minus Z''_q`), the members `q > i` are `Omega_q cap X = X minus O_q`, and the members `q <= h` are the old ones. Y 63799-63803 gives `Z''_i(X)` with `Z''_i = O_i^{[-5 a_i]} = H_i^{[3 a_i]}`, or `H_{k_0+1}^{[3 u_k - w_i]}`. I recomputed the layers `A_q minus A_{q+1}` and the collar `K_i = O_{i+1} minus Z''_{i+1}`. Each one in D1 is correct, given `Z''_i subset O_i subset G_i subset H_{i+1}` (Y 63813-63817).
- **D2.** Y 72252-72266: new rows have both ends outside `Omega_{j+1}`, their blocks lie inside the old member at level `j`, "the averaging delta on the new row is still present when the stage is tested", and "the other prospective rows have their old values". Y 77767-77768: "the group is pinned at the next coarse sites, so the coarse row remains fixed". Y 63836 (1): the collar variables are "integrated out as in a small-field step". (m2) is a constraint identity carried at `nu_i`, not a move. The note's reading, "`V_{i+1}(c) = M(V_i(x_{nu_i}))(c)` at `nu_{i+1}`", follows from it, because the gauge is pinned at the coarse sites. One point is not literal in Y: the support of the collar gauge is "complete blocks inside the component's exterior buffer" (Y 77775-77776), not "level-i bonds with an endpoint in `K_i`". The note needs only that the gauge does not touch `Gamma'_i` or any row of another level. That holds because the gauge acts at level-i sites of `K_i` and fixes the coarse sites. D3 ("no other move") is a reading that rests on (G2) of row 632. I did not check D3 beyond Y 63849.

## 2. Item (2): D4 — HOLDS

- Y 63876 gives the shell thresholds `(1 - beta_s(1 - 2^{-(j-i+1)})) L_flat^{2(i-k#-1)_+} eps_i eta_i^2` and the exterior thresholds `(1 - beta_s/2) c_l L_flat^{2e} eps_j eta_j^2`. There `e = (j-l-1)_+` on `Omega_l minus Omega_{l+1}`, `e = j - k# - 1` between the shells and `Omega_{k#+1}`, `e = 0` for `j <= k#`, and `c_l <= 3`. `k#` is `k_0` (both are defined by `R_{k_0+1} = L^{k-k_0-1}`). Y uses `eta_i^2` and `L^{-2i}` for the same quantity (Y 64380). The regions of D4 are the intersections of these regions with `X`.
- Y 64223-64228: "The deep exterior clause is in `Omega_{i_0+1}^c` ... the other exterior clauses are in `Omega_l minus Omega_{l+1}` with `l <= j`." Y 64406-64414 and 64728-64731 give `i_0 = j` at the new stage `q = j+1 <= k_0+1`. So the guard at `nu_i`, for `i <= k_0`, has the deep exterior `O_i minus Z''_i` and the region `O_{i+1} minus O_i`. This is D4's split. Y 77622-77623 merges them at `i = k_0`. Every inclusion in the note lands in `O_{i+1} minus O_i`, which lies inside either reading.
- Stage zero: Y 64406-64408 ("The original stage-zero guard tests plaquettes contained in `Omega_h minus Omega_q`"). Y 64430-64434 confirms that it is a carried test, removed in the collar integral.
- Containment: Y 64278 says "The final shell and exterior clauses both require containment". Y 64370-64373 says "Neither containment clause of the next guard tests it". Crossing tests are optional: "In a split with an added crossing test" (Y 64384) and "For an operation using these additional tests" (Y 64435). The sentence of D4 is a fair reading. Finding 1 of `cov-x.md` (no crossing clause in the default operation) is correct.

## 3. Item (3): D5 — HOLDS

Y 63836 (1) says the stage tests are "formed with backgrounds localised in X". Y 13057-13059 says "The localized datum agrees with the original datum on old rows". Y 13128-13130 says "The real background theorem applies to this regular datum on the joined sequence". The background of a constrained problem satisfies `M^q U = V_q` on every row of every level of its determining set (Y 63876: "If two backgrounds satisfy the same constraints on a region ..."). Y 77629-77630 states the consequence used in the note: "The local preceding background has the actual old level-`j` datum on this footprint." The rows away from `X^c` are ambient rows by `library/h-geo.md` Lemma 3.1. Every footprint used lies in `O_m`, at distance `2 a_m` from `X^c` (Y 63761).

## 4. Item (4): D6 — HOLDS, and Lemma 6.4 has a supplier

- (I4_l): Y 134113-134117 says "The positive density test gives bare curvature less than `eps_k eta_k^2` there. The local small-curvature average estimate gives `|dV_k - 1| <= 2 eps_k` on the one-step footprint, since the localized orbit has the prescribed `V_k` there." The level is generic. `2.1` comes from `2 arcsin(eps) <= 2.1 eps` for small `eps` (`library/rim-scale-check.md`). Completed values: Y 77712-77721 says "the surviving one-step delta gives `V_i(c) = M(V_{i-1})(c)`".
- T5: Y 64005-64008 says "The surviving level-`h` density tests at this first stage have bases in `Z_h cap Omega_h cap X`". Y 64022-64025 says "The retained bottom tests read the frozen core". Y 63836 (3) says they stay under the core operation through the main step. So they are carried at `N`.
- T4: Y 62050 (c) and Y 64096-64097.
- **The decision the row asks for.** The level-l' tests near the wall are carried at `nu_{l'}`. Y 64697-64716 is about the transition `j -> q = j+1`, with `h < j < m`. It says: "The lower density cubes have bases in `(Omega_j^{~4} minus Omega_q^~) cap X` ... Hence the whole density box is in the old prepared layer `j`. Use that layer's actual determining rows at the old target." Y 77673 says "Use the density test at that face before it is removed", and Y 77684-77686 says "Its level-`l` plaquettes are covered by the original density test with its full halo. Before deletion this gives `|dV_l - 1| <= C eps_l` there." So a level-l' test is carried at `nu_{l'}` and reads `D_{l'}`. Lemma 6.4 has its supplier. The base set `O_{l'+1}^{[-a_{l'+1}]} minus O_{l'}^{[-4 a_{l'}]}` follows from Y 61973 and the erosion formula (Y 63790-63797). Partitions are nested because `R` is a power of `L` (Y 62001).

## 5. Item (5): Lemma G and Lemma P — HOLDS

Lemma G: `F(p)` is the union of four order-l blocks centred at the corners. (a), (b) and (c) are immediate. (b) needs `S` to be a union of aligned level-l blocks. This holds for `Omega_{l+1}`, `O_h`, `G_h`, `Z''_l`, `Z''_{l+1}` and `O_m` (Y 63805-63809; `h-geo` Fact 1.2).

Lemma P: I redid the case split by level. `l < h` uses `Omega_{l+1} supset Omega_h`. For `l = h`, a corner in `O_h` and a corner in `A_h` lie within `L^h <= 2 a_h` of each other, so the second corner is in `G_h minus O_h`. `h < l <= j` splits by a corner in `Z''_l`. For P5, the boxes `Z''_j subset O_{k_0+1} subset ... subset O_m` are nested by (B1) and (B3). For (B3) I checked `O_{i+1} = H_{i+1}^{[8 a_{i+1}]} supset G_i^{[8 a_{i+1}]} = O_i^{[2 a_i + 8 a_{i+1}]}`, using `G_i subset H_{i+1}` (Y 63756). Two walls are at least `8 a_{l'+1} >= 8 L u_m > 4 L^j` apart, so `l'` is unique. Every tested plaquette of level `>= h` with `F(p) subset X` falls in exactly one case. One loose phrase is not used: "then the corners are in `Lay_{l-1} cup Lay_l`" (section 4, line 245).

## 6. Item (6): Lemma 5.1 and Corollary 5.2 — HOLDS

`Gamma_q` reads only the members `q` and `q+1`, and D1 changes only the member `i+1`. So `Gamma_q` is fixed for `q` not in `{i, i+1}`. `Gamma'_i` is `Gamma_i` without the bonds that touch `K_i`, and `Gamma_{i+1} subset Gamma'_{i+1}`. By D2, `Gamma'_i` and the rows of other levels keep their values. In (b), the completed status uses `A_{l-1}` and `A_l`, which are fixed for `l <= i`. Corollary 5.2 (i) is a downward induction that uses only the "only if" direction of (b). Corollary 5.2 (ii) is (i) at `i = l` with (a). The edge values are equal, not only conjugate. This rests on D2: the gauge is pinned at the coarse sites.

## 7. Item (7): Lemma 6.3 — HOLDS

Step 1 inclusions, checked one by one:

- `l <= k_0`: `N subset H_l^{[3a_l + 2L^l]} minus H_l^{[3a_l - 2L^l]}`. Since `2L^l <= 3a_l` and `3a_l + 2L^l <= 8a_l`, this is inside `O_l minus H_l subset O_l minus O_{l-1}`, by (B1) `O_{l-1} subset G_{l-1} subset H_l`. That set is the region `O_{i+1} minus O_i` of the guard at `nu_i`. It is the stage-zero region when `i = h`.
- `l = k_0 + 1`: `w_{k_0+1} = 2u_m`, so `Z''_l = H^{[u_m]}` and `O_l = H^{[8 u_m]}`. Since `2L^l <= u_m`, `N subset O_l minus H subset O_{k_0+1} minus O_{k_0}`.
- `l >= k_0 + 2`: we need `w_{l-1} - w_l >= u_l >= 2 L^l`. I checked it from the formula of `w`. For `k_0 + 2 <= l - 1`, the difference is exactly `u_l`. For `l - 1 = k_0 + 1`, either `l = m` and the difference is `2u_m`, or `w_{k_0+2} <= u_m L/(L-1)` and `2u_m - w_{k_0+2} >= u_m (L-2)/(L-1) >= u_{k_0+2}` (this uses `m - k_0 - 2 >= 1`). The top end is `3u_m - w_l + 2L^l <= 8 u_m`. So `N subset O_{k_0+1} minus Z''_i = E^i_0`.

The thresholds are `eps_i L^{-2i}` for `i <= k_0` and `L_flat^{2(i-k_0-1)} eps_i L^{-2i}` on the deep exterior with `c = 1` (Y 63876). `eps_{l-1}/eps_l <= sqrt(2)` is Lemma F1 of `i3-cert` (case `l < s`). It holds for every pair `l < s`, not only for adjacent levels.

Step 2: `F(p) subset Lay^i_i`, so every level-i bond in it is a row of `D_i`. D5 then applies.

Step 3: a row edge of `p` in `D'_i` has both ends in `O_{i+1}`, so it is a new row with value `M(V_i(x_{nu_i}))`. A completed edge has both ends in `Z''_{l} minus Z''_i`. Its double block lies in `Z''_l`, which is a union of aligned level-l blocks, so the double block misses `K_i`. Its lower rows are in `Gamma'_i subset Gamma_i` with the values of `D_i`. Hence `V(c) = (M^l U)(c)`. The guard at `nu_i` is in force at the entrance (Definition 4.2 (E2) of `i3-cert`, at stage `i`) and equals one on an admitted trajectory.

## 8. Item (8): Lemma 6.4 — HOLDS

- (i): `O_{l'}^{[2L^j]} subset O_{l'}^{[2a_{l'} + 7a_{l'+1}]} subset O_{l'+1}^{[-a_{l'+1}]}`, by (B3).
- (ii): `4 a_{l'} >= 4 u_m >= 2 L^j`.
- (iii): `Z''_t subset H^{[3u_m]} = O_{k_0+1}^{[-5u_m]} subset O_{l'}^{[-2L^j]}`.
- (iv): from (i) and (iii), `N subset K_t` for `l' <= t < j`, and `N subset Lay^t_t`.

At `nu_{l'}` the member `l'` is already `X minus Z''_{l'}`. So both sides of the wall lie in `Lay^{l'}_{l'}`, and every level-l' bond in `F` is a row of `D_{l'}`. This is the key point, and it is right.

Step 3 induction: a bond `b` in `B_{t+1}` has both ends in `F subset K_t`, inside `O_{t+1}`. So `b` is in `Gamma'_{t+1}` and is not an old row, so it is new. The order-(t+1) blocks of its ends are unions of aligned order-t blocks, so the bonds read by `M` are in `B_t`. The induction closes. The edges of `p` are in `B_j` and are rows.

Step 4: `d <= m - k_0 - 2`, so `L^{2d} <= L^{-2} R_{k_0+1}^2 <= 4^r R_j^2` (Lemma F2 of `i3-cert` with `l = j`). With `eps_{l'} <= sqrt(2) eps_j` (Lemma F1, any `l' < j`), `2.1 sqrt(2) < 3`. So the constant `3 . 4^r` is correct, and the defect is `<= 6 . 4^r e_j`. This is Y 77684-77704 with one footprint in place of Y's tube. Coarse (AV2) at depth `d` is Y's "full-carrier estimate ... once at depth `q - l`" (Y 77697-77699), read and not rebuilt, as the note says.

## 9. Item (9): Lemmas 6.2, 6.5 and Theorem 6.1 — HOLDS

- 6.2: in P3, `F(p) subset Lay^j_l`, which is a shell clause of T9. For `l = h`, the part `Z''_{h+1} minus G_h` lies in the first shell under both readings: Y 64410 ("contained in `Y`"), and the core `C_h = X cap Z_h` kept apart by Y 63836 (1). In P5a, the threshold is at most `3 L_flat^{2(j-k_0-1)} eps_j L^{-2j}`, since `(j-l'-1)_+ <= j-k_0-2`. All corners are in `Lay^j_l`, so no edge is completed.
- 6.5: `X minus O_m` and `G_h minus O_h` are unions of cells of their level. Every corner lies in a cube whose test is carried at `N` (T4, T5). (I4) bounds the datum loop of the point itself, so no (c2') is needed.
- Theorem 6.1: `sqrt(2) c_0 L^2 <= A_L`, `3 c_0 <= A_L` and `2.1 eps_l <= C_2 e_l`, so (5.1) and Lemma 2b give `C_2 e_l` outside P5b. P5b gives `6 . 4^r e_j`. The constants in the table of section 0 match the lemmas.

## 10. Item (10): Section 7 — HOLDS as written; see (d1)

Lemma 7.2 (a): every point at distance `> 3 M_1 L^m` from `X^c` is in every `T_q` (`h-geo` Lemma 3.1). So on `F(p)` the joined and the global prospective sequences agree member by member. The tested, row and completed status and the values agree, by Y 13057-13059 ("agrees with the original datum on old rows"). Lemma 7.2 (b) and (c): `3 M_1 L^m + 4 L^m < 2 a_m` puts `F(p)` in `X cap Omega_m`, and `X cap Omega_m subset A'_{l+1}` for `l < m`. Corollary 7.3 follows. Its link to Lemma 6 of `i3-cert` needs repair (d1). Corollary 7.4: by (G2) of `i3-cert`, `D(P)` lies in the old `Lay_j`, and its level-j plaquettes have their blocks in `F(P)`. I did not reread all of Lemma 4.

## 11. Item (11): the four edits of section 8

1. (c2) to (c2'), and (s1) to the edge form. **Needed:** at `nu_i` the P4 plaquette is not a tested plaquette of `D(x_{nu_i})`, because it has no corner in `A^i_{i+1} = X minus O_{i+1}`. At `nu_{l'}` the P5b loop is not a level-j loop at all. **Enough:** Lemma 3.2 gives the bound at `x_N` directly from (c2') and (AV2).
2. Items 3 and 5 take the guard before promotion. **Needed:** in the default operation T9 has no clause astride `dZ''_j` or the earlier faces (Y 64370-64373, 64384, 64435). The crossing clause that (E2) of `i3-cert` cites is the optional `kappa_x` of the final inset split (Y 64308-64313). **Enough:** Lemma 6.3 works in both operations.
3. Add (K-wall) with `psi_j <= 3 . 4^r R_j^2`. **Needed:** the walls `dO_{l'}`, `k_0 < l' <= j`, lie in `K` and are not read by T9 (Y 77647-77704). **Not enough as written:** see (d2), the ceiling (H5) with `C_2'`. The spare factor `1/R_l` of Lemma 2b is used nowhere else in `i3-cert`. I grepped for it: only lines 207, 345, 353 and 361 mention it, and all are inside F3 and 2b. So dropping it breaks nothing.
4. Case A of Lemma 4 with `C_2'`. **Needed:** `D(P)` for `P` in `K` near a wall contains level-j plaquettes of case P5b, because `dO_{l'} subset K = O_m minus Z''_m`. **Enough**, together with (d2).

RESULT: (COV-X) for levels >= h HOLDS (Claude Opus 5.5 check of cov-x.md; first failing step none; D1-D6 are fair readings of Y; the level-l' density tests are carried at nu_{l'} per Y 64697-64716 and 77673-77686, so Lemma 6.4 has its supplier). Repairs: (d1) Corollary 7.3 yields Lemma 6 of i3-cert only if "tower holonomy" means every non-interior tested plaquette, as in Y 13100-13102, or if Theorem 9.1 (i) excludes rim top plaquettes; (d2) edit 3 must also put C_2' in place of C_2 in the coupling ceiling (H5); edits 1, 2 and 4 are needed and enough. Open: P1 (levels below h, row 632) and D3 (rests on (G2) of row 632).
