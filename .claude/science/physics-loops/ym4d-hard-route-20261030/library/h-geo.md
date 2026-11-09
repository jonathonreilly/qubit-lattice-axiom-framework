lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T09:35Z

# h-geo: geometry of the joined determining set (FINISH row 614)

Status: finished 2026-11-09 (one session, started 21:35Z). Pinned at 64bf74e70. Not checked by another model.
Provenance: one session of Claude Fable 5.2 (medium), worker on the Mac mini. No numeric job was run; everything is by reading and by hand. Research-stage working state; it grants no status.

Credit. The objects (regions, class, prepared nest, towers, the background proposition) are Ethan Sussman and Levent Alpoge's, in `YM4_1400.tex` (their text names Claude and Codex as authors), commit 2bc0658f91d2, fetched by URL into a scratch folder; "Y n" is line n of that file. The method is Tadeusz Bałaban's (CMP 119, CMP 122). The induction over histories that section 4 cites is `library/geo-5.md` (Codex, rows 118-124; Claude check row 127). Everything quoted from Y is `unchecked` unless a proof is written here.

## 0. Result

**H-GEO holds: case (a).** Every consecutive pair of members of the joined determining set of a class component `X` of level `m`, at the final stage and at every earlier stage, has gap at least `L M xi_q` or (in the tower) greater than `R_1 frakM xi_q`. The floor of `bgc:proper-background` is `R_1 frakM xi_q`, and Y fixes `M >= L^4 M_1 >= L^4 R_1 frakM`. So the nest gaps exceed the floor by a factor at least `L^5`. Stop condition (i).

| Pair | Gap (bare units, level `q` to `q+1`) | Floor `R_1 frakM L^q` met by | Status |
|---|---|---|---|
| nest to nest, early `h < q < k_0` | `>= 7 a_q + 3 a_{q+1}` | factor `>= 7 L^4` | proved here from Y's box formula |
| nest to nest, change of scale `q = k_0` | `>= 7 a_q + u_m` | factor `>= 7 L^4` | proved here |
| nest to nest, compressed `k_0 < q < m` | `>= u_{q+1} = L M L^q` (equality for `q >= k_0+2`) | factor `>= L^5` | proved here |
| core to first prepared member, `q = h` | `>= 3 a_{h+1}` | factor `>= 3 L^5` | proved here |
| inside the core, `q < h` | `>= L M L^q` | factor `>= L^5` | **cited**: Y `prop:large-field-2-3` (Y 62080-62087) and `geo-5.md` 3.2-3.3; not rebuilt against Y |
| nest to seam (prepared level `m` meets `Omega_m`) | no pair: both sides are in layer `m` at the final stage; at an earlier stage the pair is prepared member `j+1` to old member `j+2`, gap `>= 8 a_{j+2}` | factor `>= 8 L^5` | proved here |
| seam to tower, tower layer to tower layer | first rule `> R_1 frakM L^q`; second rule `>= L M_1 L^q`; `mu`-tower `>= L mu L^q` | first rule: by definition; second: `M_1 >= R_1 frakM`; `mu`-tower: needs `mu >= R_1 frakM` (true for `mu = M_1`) | proved here |
| joined (ambient meet tower) | minimum of the two | Lemma 3 | proved here |

Answers to the row's questions:

1. Constants: section 1. Y has **no separate existence statement with smaller margins** for prepared backgrounds (searched the phrases listed in section 1; a phrase search, not a proof of absence). None is needed: "smaller margins" (Y 63824-63826) means one `M`-cube instead of a cell of side `M Rcheck`, and one `M`-cube is still `L^5` times the floor of the one statement `bgc:proper-background`.
2. Case (a), sections 2-5.
3. Not needed. `K_w`, `delta`, `a_0`, `a_1`, `C_B` are those of the fixed geometry and do not depend on `m`, on the stage or on the shape of `X` (Y 35272-35275: constants depend on the floors, `L`, `alpha`, "not on depth, the number of pillars, the volume, or the shapes and number of components of the regions").

What stays open is in section 6. Short form: the core gaps (`q < h`) are cited, not rebuilt against Y; Y's two conventions for "separated" (section 1, item 6) should not be mixed by a consumer.

## 1. Repo search, and the constants in Y

Repo search (this folder; the only remote branch on this machine is `claude/ym4d-hard-route`). Match found: `library/geo-5.md` section 3 (rows 118-124, check row 127) proves, for the outline `YM4_sketch_500.tex` under adopted rules, that label, action and prepared sequences have gap `>= M xi_i` through every fate and stopping choice, and that joined sequences have gap `> rho xi_i`. It takes the one-`M`-cube nest gap as a retained local requirement (its (3.1)) and does not compare with the floor of Y's `bgc:proper-background`. I do not redo its induction. New here: the gap (3.1) derived from Y's explicit box formula, the comparison with the floor `R_1 frakM`, and the tower rules of Y. `library/open-core.md` has no row for this statement; `library/open-registry.md` line 1000 is this item.

Constants (all powers of `L`):

1. Y 637-645: "Fix powers of `L` called `frakM, M_1', M`, a gap `rho = R_1 frakM` ... The first two sizes concern backgrounds and walks; `M` is the localization cube size. They are not interchangeable. The partition `pi_j` consists of the centered, half-open `M`-cubes in level-`j` units."
2. Y 649-651 (again Y 35848-35853, Y 49957-49959, Y 132258-132259): `L >= 13` odd, `R_1 >= L`, `M_1' >= R_1 frakM`, `M >= L^4 M_1'`, "in addition to the background floors". Order (Y 35853-35855): the background floors come first, "the localization size `M` is then increased, if necessary".
3. Y 14937-14944 (geometry of `bgc:proper-background`, by Y 35270): `frakM >= m^s`, `R_1 >= L`, `R_1 frakM >= L^2 rho`, `rho >= r^s`; "the gap in `mb:separation` is greater than `R_1 frakM xi_j`"; the level-`k` circle has at least `6 rho` sites. Regions are unions of aligned cubes of side `frakM xi_j` (Y 10513-10515). Here `rho` is the `rho` of `mb:separation` (Y 10518-10520), so Y 49962 writes `rho = L^{-2} R_1 frakM`. Item 1 uses the letter `rho` for `R_1 frakM` itself. Below, "floor" always means `R_1 frakM xi_j`, the larger of the two.
4. Y 62001: `Rcheck_k` is a power of `L` (so `>= 1`), "all partitions are nested"; `M_2` has `L^2 M_2 <= M`. Y 63781, 63797: `a_i = M Rcheck_i L^i` (cell side), `u_i = M L^i` (side of an `M`-cube of level `i`), bare units. The `M` of the history chapter is the localization size of item 1: Y 132256-132259 ("the original `pi_k`-cells have side `M/L`. The inequalities `M >= L^4 M_1` and `M_1 >= R_1 frakM`"), Y 97436 (`10 M_1 < M Rcheck_j`).
5. Torus: Y 61911, `ell L^{K-j} >= 2 L^{11} M Rcheck_j` for `j <= k`.
6. A different convention, not the one `bgc:proper-background` uses: Y 16102-16106 calls a sequence separated when the members are unions of `M_1`-cubes with gaps `> R_1 M_1 xi_j`. The second-rule tower (gap `L M_1 xi_q`) does not meet that literally when `R_1 >= L`. It is outside this item; see section 6.

Smaller margins: searched Y for "smaller margin", "prepared background", "separation of only one", "one M-cube", "reduced margin", "narrow". The hits are Y 62094 ("the estimates of [the background and propagator chapters] must hold with a separation of only one `M`-cube"), Y 63824-63826 and Y 71321. No second existence statement.

**Fact 1.1.** One `M`-cube of level `q+1` has side `u_{q+1} = L M L^q >= L^5 M_1 L^q >= L^5 R_1 frakM L^q`. Proof: item 2. `square`

**Fact 1.2 (alignment).** For odd `L` and powers `s | s'` of `L`, each centered cube of side `s' L^q` is a union of centered cubes of side `s L^q`, and of centered cubes of side `s L^{q'}` for `q' <= q`. So a union of level-`q` cells, of `M`-cubes or of `M_1`-cubes of level `q` is a union of aligned cubes of side `frakM xi_q`. Proof: in one coordinate a centered interval of odd length `N s` is the union of `N` centered intervals of length `s`. `square`

## 2. The members inside `X`, and the nest gaps

Setting (Y 63684-63705, 63776-63811). `k = m`, `h = m_flat = m - N_m >= 1`, `X` a class component of `Z_m`; lengths in bare units. For `h <= i <= m`: `H_i` is a box, `O_i := Omega_i^c cap X = H_i^{[8 a_i]}`, `G_i := Z_i cap X = H_i^{[10 a_i]}`, `G_m = X`, and `G_{i-1} subset H_i` (Y 63783-63792). The index `k_0` has `h < k_0 <= m-2` and `a_{k_0+1} = u_m`. With `w_{k_0+1} = 2 u_m`, `w_m = 0`, `w_i = sum_{q=i+1}^m u_q` for `k_0+2 <= i < m`, the prepared boxes are (Y 63798-63803)

`Z''_i(X) = H_i^{[3 a_i]}` for `h < i <= k_0`,  `Z''_i(X) = H_{k_0+1}^{[3 u_m - w_i]}` for `k_0 < i <= m`.

I checked the derivation of this formula from the distance rule of Y 63799-63811 (`8 a_i - 5 a_i`; `8 u_m - 5 u_m - w_i`, which needs `5 u_m + w_i <= 8 u_m`, true by (2.2) below).

Members (Y 72244-72250: at stage `n+1`, `j = h+n`, "the only member of the sequence that changes is the one of index `j+1`, which grows from `Omega_{j+1}` to the prepared member"). So inside `X`, before the tower is joined, the stage-`(n+1)` prospective sequence `A_0 supset ... supset A_m` is

- `A_q cap X = Omega_q cap X` for `q <= h` (old label),
- `A_q cap X = X minus Z''_q(X)` for `h < q <= j+1` (prepared),
- `A_q cap X = X minus O_q` for `j+1 < q <= m` (old label).

The final stage is `j+1 = m`: no member of the third kind. Write `D_q := X minus A_q` (the hole of level `q`), so the gap of the pair `(q, q+1)` inside `X` is `g_q := dist_infty(D_q, X minus D_{q+1})`. For concentric-type boxes `B subset B'`, `dist_infty(B, B'^c)` is the least face offset; if `B' supset B^{[s]}` it is at least `s`.

**Lemma 2 (nest gaps).** With `Rcheck_i >= 1` and `L >= 3`:

- (a) `h < q < k_0`: `g_q >= 7 a_q + 3 a_{q+1}`.
- (b) `q = k_0`: `g_q >= 7 a_{k_0} + u_m`.
- (c) `k_0 < q < m`: `g_q = w_q - w_{q+1} >= u_{q+1}`, with equality for `q >= k_0 + 2`.
- (d) `q = h`: `g_h >= 3 a_{h+1}`.
- (e) upper splice at a stage before the last, pair (prepared `j+1`, old `j+2`): `g_{j+1} >= 8 a_{j+2}`; old pairs `q >= j+2`: `g_q >= 2 a_q + 8 a_{q+1}`.
- (f) `dist_infty(Z''_m(X), X^c) >= 5 u_m + 2 a_m`.

In every case `g_q >= L M L^q`, hence `g_q >= L^5 R_1 frakM L^q` by Fact 1.1.

*Proof.* (a) `H_{q+1} supset G_q = H_q^{[10 a_q]}`, so `Z''_{q+1} = H_{q+1}^{[3 a_{q+1}]} supset H_q^{[10 a_q + 3 a_{q+1}]} = (Z''_q)^{[7 a_q + 3 a_{q+1}]}`.
(b) `Z''_{k_0+1} = H_{k_0+1}^{[3 u_m - 2 u_m]} = H_{k_0+1}^{[u_m]} supset H_{k_0}^{[10 a_{k_0} + u_m]}`.
(c) The two boxes are enlargements of the same box `H_{k_0+1}` by `3 u_m - w_q` and `3 u_m - w_{q+1}`, both inside `O_{k_0+1} subset X`, so the gap is `w_q - w_{q+1}`. For `k_0 + 2 <= q < m`: `w_q - w_{q+1} = u_{q+1}` (for `q = m-1` this is `w_{m-1} - 0 = u_m`). For `q = k_0 + 1`: if `k_0 + 2 = m` the gap is `2 u_m`. Otherwise

`w_{k_0+2} = sum_{r=k_0+3}^m u_r <= u_m sum_{s>=0} L^{-s} = u_m L/(L-1)`,  (2.2)

so the gap is at least `u_m (L-2)/(L-1) >= u_m / L >= u_{k_0+2}`, using `(L-2)/(L-1) >= 1/L` for `L >= 3` and `m >= k_0 + 3`.
(d) `D_h = O_h subset G_h subset H_{h+1}`, and `h + 1 <= k_0`, so `Z''_{h+1} = H_{h+1}^{[3 a_{h+1}]}`.
(e) `Z''_{j+1} subset O_{j+1}`: for `j+1 <= k_0` because `3 a <= 8 a`; for `j+1 > k_0` because `Z''_{j+1} subset H_{k_0+1}^{[3 u_m]} subset H_{k_0+1}^{[8 u_m]} = O_{k_0+1}` and `O_i subset G_i subset H_{i+1} subset O_{i+1}`. And `O_{i+1} = H_{i+1}^{[8 a_{i+1}]} supset H_i^{[10 a_i + 8 a_{i+1}]} = O_i^{[2 a_i + 8 a_{i+1}]}`.
(f) `Z''_m = H_{k_0+1}^{[3 u_m]}`, `O_{k_0+1} = H_{k_0+1}^{[8 u_m]} subset O_m`, and `X = O_m^{[2 a_m]}`.
Last sentence: `a_i >= u_i = M L^i` since `Rcheck_i >= 1`; in (a), (b) `7 a_q >= 7 M L^q`, and with `M >= L^4 R_1 frakM` this is `7 L^4` times the floor (the term `3 a_{q+1}` gives `3 L^5`); (c)-(e) are at least `u_{q+1}`. `square`

Remarks. (i) The equality in (c) is Y's own statement (Y 62088-62091): the compressed gaps are exactly one `M`-cube of the later level, and nothing smaller occurs. (ii) Closed cubes against sites: the conventions differ by at most one bare spacing on each side, and the margin over the floor is a factor `L^4` at least, so the strict inequality of the floor holds under either convention. (iii) Alignment: each `Z''_q(X)` is a union of level-`q` cells or of `M`-cubes of level `q` (Y 63804-63809), `X` is a union of level-`m` cells; by Fact 1.2 each `A_q cap X` is a union of aligned cubes of side `frakM xi_q`.

## 3. The tower at `dX` and the join

Y's tower rules on a first member `T_0 = X` (Y 656-667, bare units):

- first rule: `T_{q+1}` = union of the aligned cubes `C` of side `frakM L^{q+1}` with `C subset T_q` and `dist_infty(C, T_q^c) > R_1 frakM L^q`;
- second rule: cubes of side `M_1 L^{q+1}` with `dist_infty(C, T_q^c) >= M_1 L^{q+1}`;
- the `mu`-tower of Y 12983-12996 (used with `mu = M_1`: Y 13450, Y 62436-62437, Y 63183-63184): cubes of side `mu L^{q+1}` with `dist_infty(C, T_q^c) >= mu L^{q+1}`.

**Lemma 3.1 (tower gaps).** `dist_infty(T_q^c, T_{q+1}) > R_1 frakM L^q` for the first rule, the second rule, and the `mu`-tower with `mu >= R_1 frakM`. Each `T_q` is a union of aligned cubes of side `frakM L^q`. Every point of `X minus T_q` is within `w_q <= 3 M_1 L^q < M L^{q-3}` of `X^c`.

*Proof.* `T_{q+1}` is a finite union of cubes each satisfying the distance test, so the distance from `T_q^c` is at least the tested bound: `> R_1 frakM L^q` by definition (first rule); `>= M_1 L^{q+1} = L M_1 L^q > R_1 frakM L^q` (second rule, `M_1 >= R_1 frakM`, `L > 1`); `>= L mu L^q > R_1 frakM L^q` (`mu`-tower). An empty member has infinite distance. Alignment: Fact 1.2 (`frakM | M_1 | M`), with `T_0 = X`. Erosion: a point discarded at step `q+1` lies in a rejected cube, which meets `T_q^c` or fails its test, so it is within (side + tested gap) of `T_q^c`, and `T_q^c` is within `w_q` of `X^c`. So `w_{q+1} - w_q <= 2 M_1 L^{q+1}` (second rule and `mu = M_1`), or `<= R_1 frakM L^q + frakM L^{q+1} <= 2 M_1 L^q` (first rule), and `w_q <= 2 M_1 L^q * L/(L-1) <= 3 M_1 L^q <= 3 L^{-4} M L^q < M L^{q-3}`. This is Y's `htc:geometry` (Y 35857-35887), re-derived. `square`

Note on Y 12993-12996: the display there concludes `mu xi_{q+1} > rho xi_q` from `mu >= max{rho, frakM, L^2}`. If `rho` is read as in item 3 of section 1 (`rho = L^{-2} R_1 frakM`), that is weaker than the floor; the floor needs `mu >= R_1 frakM`. With `mu = M_1`, as Y uses it, this holds.

**Lemma 3.2 (join).** Let `A_0 supset ... supset A_m` and `T_0 supset ... supset T_m` be two sequences with `dist_infty(A_q^c, A_{q+1}) > f_q` and `dist_infty(T_q^c, T_{q+1}) > f_q`, complements in the torus. Then `J_q := A_q cap T_q` is decreasing and `dist_infty(J_q^c, J_{q+1}) > f_q`. If only the gaps of `A` inside `T_0` are known, namely `dist_infty(A_q^c cap T_0, A_{q+1} cap T_0) > f_q`, the conclusion still holds.

*Proof.* `J_q^c = A_q^c cup T_q^c` and `J_{q+1} subset A_{q+1} cap T_{q+1}`, so the distance is at least `min{dist(A_q^c, A_{q+1} cap T_{q+1}), dist(T_q^c, T_{q+1})}`. For the last sentence split `A_q^c` into its part in `T_0` and its part in `T_0^c subset T_q^c`; the second part is at distance `> f_q` from `T_{q+1}`. `square`

This is the definition of the joined sequence in both places where Y gives one: `Omega^W_q = Omega_q meet Theta_q` (Y 13002-13010, with the tower as mask for `q <= j_a = m`) and `Omega'_q = Omega^flat_q meet X_{[q]}` (Y 37069-37078, whose proof says "their next-member gaps are bounded below by the minimum of the two original gaps", Y 37102-37103). The cube-wise meet equals the set intersection here, because both factors are unions of the same aligned `frakM xi_q`-cubes (Fact 1.2).

## 4. Theorem (H-GEO) and its proof

**Theorem.** Let Y's constants be fixed as in section 1 (items 2-5). Let `X` be a class component of level `m` (Y 63684-63693), `n+1 <= N_m` a stage, `A` the prospective stage sequence of section 2, `T` a tower of `X` of depth `m` by the first rule, the second rule, or the `mu`-rule with `mu = M_1`, and `J_q = A_q cap T_q`, `0 <= q <= m`. Assume the label before the operation satisfies `dist_infty(Omega_q^c, Omega_{q+1}) >= L M xi_q` for `q < h` (hypothesis CORE; it is Y's `prop:large-field-2-3`). Then `J` with its no-inward determining set `Gamma_q` of Y 10555-10567 satisfies the geometry hypotheses of `bgc:proper-background` (Y 10513-10520, Y 14937-14948, Y 35262-35275):

- (H1) each `J_q` is a union of the aligned cubes of side `frakM xi_q`; `frakM` is an odd power of `L`;
- (H2) `dist_infty(J_q^c, J_{q+1}) > R_1 frakM xi_q` for `0 <= q < m`;
- (H3) the level-`m` coordinate circle has at least `6 rho` sites;
- (H4) no inward row is kept; every outward row of level `q >= 1` has its outer end in `J_{q-1} minus J_q`, a top of level `q-1`, whose level-`q` block lies in `J_{q-1}` and outside `J_q`.

The constants `L`, `frakM`, `R_1`, `rho` are the fixed ones; nothing depends on `m`, `n`, `N_m`, `Rcheck`, or on `X`.

*Proof.* (H1): section 2 remark (iii) for `A_q cap X` with `q >= h`; for `q < h` the old regions are unions of cells of their level (Y 62080); Lemma 3.1 for `T_q`; intersections of unions of cubes of one partition are such unions. (H2): inside `X`, Lemma 2 gives `g_q >= L^5 R_1 frakM xi_q` for `q >= h`, and CORE with Fact 1.1 gives the same for `q < h` (use `Omega_q^c cap X` against `Omega_{q+1} cap X`). The first gap `q = 0` is in CORE: `Omega_0` is `Omega_1` enlarged by one layer of level-1 cells (Y 61973), so the gap is `a_1 >= L M` in bare units. Lemma 3.1 gives the tower gaps. Lemma 3.2 (last sentence, `T_0 = X`) gives (H2). (H3): the circle has `ell L^{K-m} >= 2 L^{11} M` sites (section 1 item 5), and `6 rho <= 6 R_1 frakM <= 6 L^{-4} M`. (H4): the definition `Gamma_q` excludes inward rows. For an outward row `(y, x)` of level `q`, `y in J_q`, `x notin J_q`, `|x - y| = xi_q = L xi_{q-1} < R_1 frakM xi_{q-1}`, so by (H2) at `q-1` the point `x`, and every point within `R_1 frakM xi_{q-1} - xi_q` of it, is in `J_{q-1}`; the level-`q` block of `x` has half-side `xi_q / 2 <= R_1 frakM xi_{q-1} - xi_q` (as `R_1 frakM >= 13 L`), lies in `J_{q-1}`, and is outside `J_q` because `J_q` is a union of level-`q` blocks (H1). This is the argument of Y 10569-10585. `square`

The three parts named in the row, and the four kinds of pair:

- nest to nest: Lemma 2 (a)-(c), with (d) at the core;
- nest to seam: at the final stage the prepared member of level `m` is `X minus Z''_m(X)`, which contains `X cap Omega_m = X minus O_m`. The old wall `dO_m` lies inside layer `m` and is not a boundary between members, so it carries no separation condition. At an earlier stage the seam is the pair of Lemma 2 (e);
- seam to tower: by Lemma 2 (f) and Lemma 3.1 the nest is at distance `>= 5 u_m + 2 a_m` from `X^c` and the tower lives within `M L^{m-3}` of `X^c`, so the two do not meet: the band between them lies in every `A_q` and in every `T_q`, hence in layer `m` of the joined sequence, and every boundary of a joined member is either a nest boundary (Lemma 2) or a tower boundary (Lemma 3.1);
- tower layer to tower layer: Lemma 3.1.

Order of constants. `L >= 13` odd; then the background floors `m^s`, `r^s` and `frakM`, `R_1`, `rho` (Y 14937-14944), which fix `a_0, a_1, C_B` of `bgc:proper-background` and `K_w`, `delta` of the profile; then `M_1 >= R_1 frakM`; then `M >= L^4 M_1` (Y 35853: `M` is increased after the floors); then the coupling ceiling (`Rcheck` large), then `ell`. Lemma 2 uses only `M >= L^4 R_1 frakM` and `Rcheck >= 1`. No constant chosen earlier depends on one chosen later.

Rates. The decay conditions that Y states for consumers of the layer gaps are in terms of the same floor (Y 49967-49970: `delta_{0,red} R_1 frakM >= 8(4 log L + log 2)` and two more). A sequence that meets the floor meets them; the nest meets them with `L M` in place of `R_1 frakM`.

## 5. Attempt at case (b)

I looked for a pair below the floor before writing the proof.

- Thinnest nest: `N_m` large, so `m - k_0` compressed levels with gaps exactly `u_{q+1}`. That is the minimum, by Lemma 2 (c), and it is `L^5` floors.
- The junction `q = k_0 + 1`, where `w` changes rule: gap `2 u_m - w_{k_0+2} >= u_m (L-2)/(L-1) > 0`. No collapse.
- Tower against nest: the tower erodes at most `M L^{m-3}` into `X`; the nest stays `2 a_m + 5 u_m` inside. No interaction.
- Units: "one `M`-cube of the later level" is `L M` in level-`q` units (Y 62084-62087), not `frakM`. The floor is in `frakM`. The risk recorded in the row came from reading `M` as `frakM`; Y 641-642 says they "are not interchangeable".
- Class conditions (Y 63684-63693) restrict `X` to quiet single boxes without operations in the window; they fix the formulas of section 2 and admit no other shape inside the window. Older marks lie in the core (`s < m_flat`, Y 62128) and fall under CORE.

No configuration below the floor exists under Y's definitions, given CORE.

## 6. What stays open

1. **CORE** (levels below `h` inside `G_h`): gaps `>= L M xi_q` for every admissible earlier history, including nests kept by older drop-outs. Y states it (`prop:large-field-2-3`, Y 62080-62087). `geo-5.md` 3.2-3.3 proves it through every fate for the outline's rules, with (3.1) as input; Lemma 2 above supplies (3.1) from Y's box formula for a class component of any level. I did not re-read Y's healing, island and drop-out rules against `geo-5.md`. Smallest next step: one reading pass that maps `geo-5.md` 3.3 onto Y 62103-62136 and Y 63716-63760.
2. Y's second convention for "separated" (Y 16102-16106: `M_1`-cubes, gap `> R_1 M_1 xi_j`) is not met literally by the second-rule tower, and is met by the compressed nest only if `L M > R_1 M_1`. `bgc:proper-background` does not use it (Y 35270 points to Y 14927-14948). A consumer that cites the propagator summary of Y 16098 on the joined set must check which convention its proof needs. Not in scope here.
3. The identification of the joined **datum** (three kinds of tested holonomy, Y 13099-13131, Y 134205-134212) needs, beyond H-GEO, that the four-layer band of `M_1`-cubes at `dX` lies in ambient layer `m`. By Lemma 2 (f) it does: `4 M_1 L^m < 2 a_m`. I state this as a remark; the datum bounds themselves are (I3) of `rim-scale.md`, not in scope.
4. The formula for `Z''_i(X)` and the existence of `k_0` with `h < k_0 <= m-2` are Y's (Y 63797-63803); `library/geoh.md` line 186-190 proves the existence of such a depth above a scale floor.
5. Not checked by another model.

Consequence for `rim-scale.md`: in the table of its section 6.4, the row "H-GEO, not checked" becomes "holds, given CORE". Theorem 6.2 (RIM-REG) has its existence input; its remaining inputs are (I3) and INSET-CHART, unchanged.

RESULT: H-GEO holds (case (a), stop (i)): every consecutive pair of the joined set (nest-nest, core-nest, seam, tower) has gap at least `L M xi_q >= L^5 R_1 frakM xi_q` or, in the tower, `> R_1 frakM xi_q`, proved by hand from Y's box formula and `M >= L^4 M_1 >= L^4 R_1 frakM`; Y has no separate smaller-margin existence statement and needs none; `K_w`, `delta` do not depend on `m`. Open: the core gaps below level `m_flat` are cited (Y `prop:large-field-2-3`, `geo-5.md` 3.2-3.3), not rebuilt against Y; no cross-model check.
