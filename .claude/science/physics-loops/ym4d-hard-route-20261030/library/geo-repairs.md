lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-10T16:29Z

# geo-repairs (FINISH row 631): text repairs to `library/h-geo.md` and `library/rim-scale.md`

Provenance: Claude Opus 5.5, medium effort, Mac mini worker 2, branch `claude/ym4d-hard-route` at 5529d4f26. Text repairs, no new proof. Not an audit. Status: finished 2026-11-09.

Credit. Every "Y n" is line n of Ethan Sussman and Levent Alpoge's `YM4_1400.tex` (their text names Claude and Codex as authors), commit 2bc0658f91d2, fetched by URL into my own scratch folder `/tmp/georep-src/` (136,637 lines, as the row says). The repairs are those of `library/h-geo-check.md` (row 615) and `library/rim-scale-check.md` (row 613), both Claude Opus 5.5; the files repaired are Claude Fable 5.2's (rows 614, 609).

## How the edits are delivered (read first)

The row asks for in-place edits of `library/h-geo.md` and `library/rim-scale.md`. The dispatch for this session says: write only `library/geo-repairs.md` (plus a new file for a newly rebuilt lemma), edit no other file. The dispatch is the narrower instruction, so **I did not edit either file**. Each edit below gives the file, its line at 5529d4f26, the exact old text and the exact new text, so that the lead can apply it mechanically (each old text is unique in its file unless marked). Status words: READY (old/new given, ready to apply), NOT APPLIED (with reason).

## Repo search

Not an open lemma, so no attack; the grep is for overlap. `grep -n` for `geo-repairs`, `h-geo`, `rim-scale` in `FINISH.md`, `library/open-core.md`, `library/open-registry.md`: rows 609, 613, 614, 615 (the files and their checks), registry line 1002 (H-GEO, names this row as the owner of the three text repairs). `library/open-core.md` has no row on these repairs. No other row covers them.

## Part A: `library/h-geo.md`

Y lines read for Part A: Y 648-653, Y 35842-35844, Y 72928-72940, Y 132180-132212, Y 63690-63694, Y 61982-61987, Y 62103-62126, Y 63756-63766.

### A1. `M_1` read as `M_1'`

Basis: Y 650-651 "`R_1 >= L`, `M_1' >= R_1 frakM` and `M >= L^4 M_1'`"; Y 35843 "Write `M_1 = M_1'` in this subsection"; Y 72931 places the global `M_1` before `R_1`, and Y 72939 "`M_1` depends on `L` alone, and `R_1` depends on `L` and `M_1`". Y 132180-132210: the recursive tower is either "the minimal determining tower with `M_1`-cubes" (clearance at least `s`, the second rule) or "the rule with `frakM`-cubes and strict clearance `> R_1 s / L`" (the first rule).

Scope decision. A1 is applied to every statement of h-geo that uses `M_1 >= R_1 frakM` or a quantity built from it. It is NOT APPLIED where h-geo quotes or reports a line of Y in Y's own letter, because there the check could not settle which constant Y means (h-geo-check section 3 for Y 13450, 62436-62437, 63183-63184; section 5 for Y 16102-16106): line 43 (quote of Y 132256-132259), line 45 (Y 16102-16106), line 153 (same), and the list of Y's uses on line 100 (handled by A1-g below). Line 154 (`4 M_1 L^m < 2 a_m`) is left: h-geo-check section 4 shows it for both readings.

**A1-a** (line 13, section 0).
- Old text (exact): ``Y fixes `M >= L^4 M_1 >= L^4 R_1 frakM`.``
- New text: ``Y fixes `M >= L^4 M_1' >= L^4 R_1 frakM` (Y 650-651; `M_1'` is the constant Y 35843 renames `M_1`, see section 1).``
- Y: 650-651, 35843. Status: READY.

**A1-b** (line 23, table row "seam to tower").
- Old: ``| seam to tower, tower layer to tower layer | first rule `> R_1 frakM L^q`; second rule `>= L M_1 L^q`; `mu`-tower `>= L mu L^q` | first rule: by definition; second: `M_1 >= R_1 frakM`; `mu`-tower: needs `mu >= R_1 frakM` (true for `mu = M_1`) | proved here |``
- New: ``| seam to tower, tower layer to tower layer | first rule `> R_1 frakM L^q`; second rule `>= L M_1' L^q`; `mu`-tower `>= L mu L^q` | first rule: by definition; second: `M_1' >= R_1 frakM`; `mu`-tower: needs `mu >= R_1 frakM` (true for `mu = M_1'`) | proved here |``
- Y: 650-651, 35843. Status: READY.

**A1-c** (section 1, after item 2, line 41; insertion of one paragraph, no text removed).
- Old (end of item 2): ``"the localization size `M` is then increased, if necessary".``
- New: the same item, followed by a new paragraph:
  ``Notation (repair, h-geo-check Defect 1). Y uses the letter `M_1` for two constants. The global walk-cube size `M_1` of Y 72931 and Y 72939 ("`M_1` depends on `L` alone, and `R_1` depends on `L` and `M_1`") is chosen before `R_1` and is not assumed `>= R_1 frakM`. The inequality `M_1' >= R_1 frakM` holds for the constant `M_1'` of Y 650-651, which Y 35843 renames `M_1` ("Write `M_1 = M_1'` in this subsection"); Y 49958 and Y 132258 use the renamed constant. In every statement of this file that uses `M_1 >= R_1 frakM`, the constant is `M_1'`. Where a line of Y is quoted or its convention reported (item 4, item 6, section 3's list of Y's uses of the `mu`-tower, section 6 item 2), Y's letter is kept, and which of the two constants Y means there is not settled (h-geo-check sections 3 and 5).``
- Y: 650-651, 35843, 72931, 72939, 49958, 132258. Status: READY.

**A1-d** (line 49, Fact 1.1).
- Old: ``**Fact 1.1.** One `M`-cube of level `q+1` has side `u_{q+1} = L M L^q >= L^5 M_1 L^q >= L^5 R_1 frakM L^q`. Proof: item 2. `square` ``
- New: ``**Fact 1.1.** One `M`-cube of level `q+1` has side `u_{q+1} = L M L^q >= L^5 M_1' L^q >= L^5 R_1 frakM L^q`. Proof: item 2 (`M >= L^4 M_1'`, `M_1' >= R_1 frakM`, Y 650-651, Y 35843). `square` ``
- Status: READY.

**A1-e** (line 51, Fact 1.2).
- Old: ``So a union of level-`q` cells, of `M`-cubes or of `M_1`-cubes of level `q` is a union of aligned cubes of side `frakM xi_q`.``
- New: ``So a union of level-`q` cells, of `M`-cubes or of `M_1'`-cubes of level `q` is a union of aligned cubes of side `frakM xi_q`.``
- Status: READY.

**A1-f** (line 99, second rule).
- Old: ``- second rule: cubes of side `M_1 L^{q+1}` with `dist_infty(C, T_q^c) >= M_1 L^{q+1}`;``
- New: ``- second rule: cubes of side `M_1' L^{q+1}` with `dist_infty(C, T_q^c) >= M_1' L^{q+1}` (Y 661-665, read with Y 35843);``
- Status: READY.

**A1-g** (line 100, `mu`-tower).
- Old: ``- the `mu`-tower of Y 12983-12996 (used with `mu = M_1`: Y 13450, Y 62436-62437, Y 63183-63184): cubes of side `mu L^{q+1}` with `dist_infty(C, T_q^c) >= mu L^{q+1}`.``
- New: ``- the `mu`-tower of Y 12983-12996: cubes of side `mu L^{q+1}` with `dist_infty(C, T_q^c) >= mu L^{q+1}`. Below it is taken with `mu = M_1'`. (Y writes `mu = M_1` at Y 13450, Y 62436-62437, Y 63183-63184; which of its two constants those lines mean is not settled, h-geo-check section 3.)``
- Status: READY. Note: the old text attributed `mu = M_1` to Y; the new text keeps that attribution in Y's letter and does not assert that Y means `M_1'` there.

**A1-h** (line 102, Lemma 3.1; the row's "write `mu = M_1'` and add the consumer's tower").
- Old: ``**Lemma 3.1 (tower gaps).** `dist_infty(T_q^c, T_{q+1}) > R_1 frakM L^q` for the first rule, the second rule, and the `mu`-tower with `mu >= R_1 frakM`. Each `T_q` is a union of aligned cubes of side `frakM L^q`. Every point of `X minus T_q` is within `w_q <= 3 M_1 L^q < M L^{q-3}` of `X^c`.``
- New: ``**Lemma 3.1 (tower gaps).** `dist_infty(T_q^c, T_{q+1}) > R_1 frakM L^q` for the first rule, the second rule, and the `mu`-tower with `mu >= R_1 frakM`, in particular for `mu = M_1'`. Each `T_q` is a union of aligned cubes of side `frakM L^q`. Every point of `X minus T_q` is within `w_q <= 3 M_1' L^q < M L^{q-3}` of `X^c`. The tower that the consumer uses (`rim-scale.md` (G3): "the minimal recursive tower of the component", Y 135196-135197) is a first-rule or a second-rule tower (Y 132180-132210), so it is covered.``
- Y: 650-651, 35843, 132180-132210, 135196-135197. Status: READY.

**A1-i** (line 104, proof of Lemma 3.1). Four replacements inside the one paragraph:
- ``(second rule, `M_1 >= R_1 frakM`, `L > 1`)`` → ``(second rule, `M_1' >= R_1 frakM`, `L > 1`)``; and the preceding ```>= M_1 L^{q+1} = L M_1 L^q > R_1 frakM L^q` `` → ``` `>= M_1' L^{q+1} = L M_1' L^q > R_1 frakM L^q` ```.
- ``Alignment: Fact 1.2 (`frakM | M_1 | M`)`` → ``Alignment: Fact 1.2 (`frakM | M_1' | M`)``.
- ``So `w_{q+1} - w_q <= 2 M_1 L^{q+1}` (second rule and `mu = M_1`), or `<= R_1 frakM L^q + frakM L^{q+1} <= 2 M_1 L^q` (first rule), and `w_q <= 2 M_1 L^q * L/(L-1) <= 3 M_1 L^q <= 3 L^{-4} M L^q < M L^{q-3}`.`` → the same sentence with every `M_1` replaced by `M_1'` (six occurrences).
- Status: READY.

**A1-j** (line 106, note on Y 12993-12996).
- Old: ``With `mu = M_1`, as Y uses it, this holds.``
- New: ``With `mu = M_1'` this holds (Y 650-651). For Y's global walk-cube `M_1` (Y 72939), chosen before `R_1`, it is not implied.``
- Status: READY.

**A1-k** (line 116, the Theorem).
- Old: ``or the `mu`-rule with `mu = M_1`, and``
- New: ``or the `mu`-rule with `mu = M_1'`, and``
- Status: READY.

**A1-l** (line 134, order of constants).
- Old: ``then `M_1 >= R_1 frakM`; then `M >= L^4 M_1` (Y 35853: `M` is increased after the floors);``
- New: ``then `M_1' >= R_1 frakM` (Y 650-651, Y 35843); then `M >= L^4 M_1'` (Y 35853: `M` is increased after the floors);``
- Status: READY. Y's own order (Y 72931) also has `M_1' < M_2 < ... < M` after `R_1`; consistent.

**A1-m** (line 160, RESULT line).
- Old: ``and `M >= L^4 M_1 >= L^4 R_1 frakM`;``
- New: ``and `M >= L^4 M_1' >= L^4 R_1 frakM` (Y 650-651, 35843);``
- Status: READY.

### A2. Theorem: add (H0) and (H5)

Basis: h-geo-check section 4, rows 2 and 8 of its table. Y 10513-10515 (`Omega_0 supset ... supset Omega_k`, `Omega_{k+1} = empty`); Y 28271 and Y 35272 (compatible volume); Y 63692 ("Hence no cell, no box and no neighbourhood of a box wraps around the torus").

**A2-a** (line 116, the Theorem's lead-in).
- Old: ``Then `J` with its no-inward determining set `Gamma_q` of Y 10555-10567 satisfies the geometry hypotheses of `bgc:proper-background` (Y 10513-10520, Y 14937-14948, Y 35262-35275):``
- New: ``Then `J` with its no-inward determining set `Gamma_q` of Y 10555-10567 satisfies the geometry hypotheses of `bgc:proper-background` (Y 10513-10520, Y 14937-14948, Y 28271, Y 35262-35275):``
- Status: READY.

**A2-b** (line 118, insert one clause before (H1)).
- New line before ``- (H1) each `J_q` ...``:
  ``- (H0) `J_0 supset J_1 supset ... supset J_m`, and `J_{m+1} = empty` (Lemma 3.2; the sequence ends at level `m`, as Y 10513-10515 requires with `k = m`);``
- Status: READY.

**A2-c** (line 121, insert one clause after (H4)).
- New line after ``- (H4) no inward row is kept; ...``:
  ``- (H5) compatible volume (Y 28271, Y 35272): `J_q subset T_0 = X` for every `q`; inside `X` every partition used is a nested refinement of the level-`m` cells (Fact 1.2); and no cell, box or neighbourhood of a box wraps around the torus (Y 63692).``
- Status: READY.

**A2-d** (line 125, proof of the Theorem; append two sentences before the closing `square`).
- Old: ``This is the argument of Y 10569-10585. `square` ``
- New: ``This is the argument of Y 10569-10585. (H0): inside `X`, `A` decreases, because every gap of Lemma 2 and of CORE is positive, so `D_q subset D_{q+1}` (Y 63814-63818 states the same nesting); `T` decreases; so Lemma 3.2 (last sentence, `T_0 = X`) gives that `J` decreases; `J_{m+1} = empty` is the convention that the sequence stops at `m`. (H5): `J_q = A_q cap T_q subset T_0 = X`; Fact 1.2 with remark (iii) of section 2 for the partitions; Y 63692 for the torus. `square` ``
- Status: READY.

### A3. Lemma 2 (d): `O_h := Omega_h^c cap X`, with citations

Basis: h-geo-check section 2, item (d). Y gives `O_i = H_i^{[8 a_i]}` only for `i > h` (the step at `h` may create). Y 61983-61986: each step has `Z^{[0]} = bx((Omega_t^c)^{~2} cup R_t'^{~})`, which contains `Omega_t^c`. Y 62103-62125: the three fates (healed, island, drop-out) replace `Omega_l`, `Lambda_l` together on `X` (`Lambda = Z^c`). Y 63818-63820 states `G_h subset Z''_{h+1}(X)` and the separation `>= 3 a_{h+1}` from `G_h` (read; it is the conclusion of (d), not the inclusion `O_h subset G_h`).

**A3-a** (line 87, proof of Lemma 2 (d)).
- Old: ``(d) `D_h = O_h subset G_h subset H_{h+1}`, and `h + 1 <= k_0`, so `Z''_{h+1} = H_{h+1}^{[3 a_{h+1}]}`.``
- New: ``(d) Here `O_h := Omega_h^c cap X`; Y's box form `O_i = H_i^{[8 a_i]}` is stated only for `i > h`, and is not used at `i = h`. `D_h = O_h subset G_h`: each step has `Z^{[0]} = bx((Omega_t^c)^{~2} cup ...) supset Omega_t^c` (Y 61983-61986), and the three fates enlarge `Omega` and `Lambda = Z^c` together (Y 62103-62125). Then `G_h subset H_{h+1}`, and `h + 1 <= k_0`, so `Z''_{h+1} = H_{h+1}^{[3 a_{h+1}]}`; Y 63818-63820 states the same separation `>= 3 a_{h+1}` from `G_h`.``
- Status: READY.

**A3-b, flagged, NOT APPLIED.** The setting paragraph of section 2 (line 55) still reads ``For `h <= i <= m`: `H_i` is a box, `O_i := Omega_i^c cap X = H_i^{[8 a_i]}`, ...``, which states the box form at `i = h`. The row names only Lemma 2 (d), and the rule is to change no statement except as a repair says. After A3-a nothing in the file uses the box form at `i = h` (Lemma 2 (a) uses `G_q`, `H_{q+1}` for `q > h`; (d) now uses `O_h := Omega_h^c cap X`). Suggested wording for the lead, if wanted: ``For `h <= i <= m`: `O_i := Omega_i^c cap X`; for `h < i <= m`, `H_i` is a box and `O_i = H_i^{[8 a_i]}`, ...``. Whether `H_h` and `G_h = H_h^{[10 a_h]}` are given by Y at `i = h` I did not check; the check uses `G_h = Z_h cap X` only.

## Part B: `library/rim-scale.md`

Y lines read for Part B: Y 10508-10512, Y 10528-10531, Y 10540-10543, Y 72302-72306, Y 35624-35628, Y 63756-63766, Y 64226-64232, Y 1260-1274, Y 648-653.

### R-a. `lambda(p)` is the largest pillar level among the corners of `p`

Basis: Y 10540-10541 "For a bare bond or plaquette `e`, let `L(e)` be the largest top scale attached to its corners"; Y 10530-10531, a top of level `j` has pillar `B^j(y)` of side `xi_j`; Y 10510, `eta = L^{-k}`, `xi_j = L^{j-k}`, so `xi_j = L^j eta`; Y 72304-72305, "the local level of the joined stage sequence at `p`".

**R-a-1** (line 56, section 3).
- Old: ``Write `lambda(p)` for the joined level of a bare plaquette `p` (Y's "local level of the joined stage sequence", Y 72304-72305): `lambda = 0` in layer zero of the tower, `lambda = m` in the top layer.``
- New: ``Write `lambda(p)` for the joined level of a bare plaquette `p`: the largest pillar level among the corners of `p`, so that `L(p) = eta L^{lambda(p)}` is Y's assigned scale (Y 10540-10541: "the largest top scale attached to its corners"; a top of level `j` has a pillar of side `xi_j = L^j eta`, Y 10510, Y 10530-10531). Inside one layer of the joined set this is the layer index, Y's "local level of the joined stage sequence" (Y 72304-72305): `lambda = 0` in layer zero of the tower, `lambda = m` in the top layer. At a seam between layers it is the upper level.``
- Status: READY. Line 17 (section 0 table: "`lambda(p)` = joined level") is not changed; it now refers to this definition.

### R-b. `K_w` carries Y's corner-to-readout factor

Basis: Y 35624-35626 "Letting `t` decrease to zero gives `r_U <= 5KP`. The bounded displacement from a corner to the base of a readout changes this constant by a fixed factor."

**R-b-1** (line 141, input (I2)).
- Old: ``; `K_w = 5K` and `delta > 0` are fixed with the geometry.``
- New: ``; `K_w` is `5K` times the fixed factor for the displacement from a corner to the base of a readout (Y 35624-35626), and `K_w`, `delta > 0` are fixed with the geometry.``
- Status: READY.

**R-b-2** (line 219, section 8 item 3).
- Old: ``3. From the geometry: `a_c`, `K`, `delta`, `K_w = 5K`;``
- New: ``3. From the geometry: `a_c`, `K`, `delta`, `K_w` (`5K` times Y's corner-to-readout factor, Y 35624-35626);``
- Status: READY. `c_0 := 5 K_w` (line 146, line 220) is unchanged, as the check says.

### R-c. Theorem 6.2: cite the quiet-box equality, not (G1)

Basis: Y 63760-63765 (`eq:elab-history-quiet-boxes`): `O_i := Omega_i^c cap X = H_i^{[8 a_i]}`, `G_i = H_i^{[10 a_i]}`, `G_k = X`. At `i = k = m`: `X cap Omega_m = X minus O_m = H_m^{[10 a_m]} minus H_m^{[8 a_m]}`, two cells of side `a_m`. (G1) gives only the opposite inclusion (outer two layers inside `Omega_m`).

**R-c-1** (line 156, proof of Theorem 6.2).
- Old: ``The top plaquettes of `V_m` with bonds in `X cap Omega_m` lie in the outer two cell layers (G1), each has a corner``
- New: ``The top plaquettes of `V_m` with bonds in `X cap Omega_m` lie in the outer two cell layers, because `X cap Omega_m = H_m^{[10 a_m]} minus H_m^{[8 a_m]}` (Y 63760-63765, `eq:elab-history-quiet-boxes`, with `O_m = Omega_m^c cap X = H_m^{[8 a_m]}` and `G_m = X = H_m^{[10 a_m]}`); each has a corner``
- Status: READY.

### R-d. Corollary 6.3: the location clause

Basis: rim-scale-check section 2, R-d, as stated there; Y 72146 item (4) (the floor is inside `X cap Omega_m^c`), as cited by the check.

**R-d-1** (line 166, last sentence of the statement of Corollary 6.3).
- Old: ``The four blocks of `P` lie in `X` (alignment, Y 72580-72581) and in `Omega_m`, at least one cell from `X cap Omega_m^c`, so no plaquette of the witness has a corner in the floor.``
- New: ``The four blocks of `P` lie in `X` (alignment, Y 72580-72581) and in `Omega_m`. The floor is inside `X cap Omega_m^c` (Y 72146 item (4)), so no plaquette of the witness has a corner in the floor. (`P` need not be one cell from `X cap Omega_m^c`: it may sit in the second layer, next to `Omega_m^c`.)``
- Status: READY.

**R-d-2** (line 168, proof of Corollary 6.3; append before the closing `square`).
- Old: ```min{(1/4)(4 eps_m)^2, e_*/2} = 4 eps_m^2`. `square` ``
- New: ``` `min{(1/4)(4 eps_m)^2, e_*/2} = 4 eps_m^2`. Location of `P`. If `U_X` exists, a failing `p in E` with corner `x` has `r_U(x) >= c_0 eps_m = 5 K_w eps_m`, so by (I2) `P(x) >= 5 eps_m`; the interior plaquettes contribute at most `eps_m/2` to `P(x)`, so the supremum is attained at a top-type tested plaquette `tau` (a tower plaquette, which is `1` or a top plaquette of `V_m` by (R1), or a top plaquette), with `abs(dV(tau) - 1) >= 5 eps_m e^{delta d_B(x, tau)}`; as `abs(dV(tau) - 1) <= 2`, `d_B(x, tau) <= delta^{-1} log(2/(5 eps_m))`, far less than `M R_m`. Take `P = tau`. If `U_X` is undefined, (I1) does not apply, so the datum is not `a_1`-regular; the interior plaquettes are within `eps_int <= a_1` by (b), so some top plaquette in the outer two layers has defect `> a_1 >= 4 eps_m`; its place is not controlled further. In both cases `P` has bonds in `X cap Omega_m`, hence lies in the outer two layers (R-c) and in `Omega_m`. `square` ```
- Status: READY. This is the check's repair written out; the sentence "the supremum is attained at a top-type tested plaquette" adds one step the check leaves implicit (the set of tested plaquettes is finite, and the interior ones are below `5 eps_m`).

### R-e. Section 7.2: radius `r = 6 frakM xi_n`, and the side condition `r^2 kappa <= eps_*`

Basis: rim-scale-check section 3, R-e: Y's cube is `Q_R = {x : abs(x)_inf <= R}`, a radius (Y 24976, as cited by the check); a gauge cube has side at most `12 frakM xi_n` (Y 1266-1267), so `r = 6 frakM xi_n` covers it and `Q_{8r}` has side `96 frakM xi_n`, which is the side the file already states at line 211. `prop:bg-local-gauge` (Y 25030-25066, as quoted at line 209) needs `r^2 kappa <= eps_*`; with `kappa <= rho xi_n^{-2}` this is `36 frakM^2 rho <= eps_*`.

**R-e-1** (line 209, class-M paragraph).
- Old: ``Put `r = 12 frakM xi_n`, and use `R(U_X) <= rho` on the cube in layers `n, n+1`: `kappa <= rho xi_n^{-2}`, `j <= rho xi_n^{-3}`. Then `xi_n |A| <= 12 C frakM rho` and `xi_n^2 |DA| <= C (1 + 12 frakM) rho`, which is the clause with `a_flat >= 13 C frakM rho`.``
- New: ``Put `r = 6 frakM xi_n` (Y's `Q_r` has radius `r`, so `Q_r` covers a gauge cube of side at most `12 frakM xi_n`), and use `R(U_X) <= rho` on the cube in layers `n, n+1`: `kappa <= rho xi_n^{-2}`, `j <= rho xi_n^{-3}`. The proposition needs `r^2 kappa <= eps_*`, that is `36 frakM^2 rho <= eps_*` (section 8, item 5). Then `xi_n |A| <= 6 C frakM rho` and `xi_n^2 |DA| <= C (1 + 6 frakM) rho`, which is the clause with `a_flat >= 7 C frakM rho`.``
- Status: READY. The constant `7` follows from the two new bounds: `6 C frakM rho <= 7 C frakM rho` and `C(1 + 6 frakM) rho <= 7 C frakM rho` since `frakM >= 1`. Section 8 item 4 keeps "`a_flat >= 13 C frakM * 2 K_w` times the ceiling on `eps_m`"; that is a stronger requirement than the new one and stays sufficient, so it is not changed.

**R-e-2** (line 221, section 8 item 5; append one condition).
- Old: ``, `32 (6 frakM + 1) c_0 eps_m <= a_flat`.``
- New: ``, `32 (6 frakM + 1) c_0 eps_m <= a_flat`, and `36 frakM^2 rho <= eps_*` for the radius `rho` used in section 7.2 (the side condition of `prop:bg-local-gauge` at `r = 6 frakM xi_n`; it holds at weak coupling).``
- Status: READY.

### R-f. Section 7.2: state `R_1 >= 42 L` as a hypothesis (no proof change)

Basis: rim-scale-check section 3, point (i) and R-f: under `R_1 = L` the cube `Q_{8r}` around a gauge cube on the outer face of `Omega_n` leaves `X`, so the line "use `R(U_X) <= rho` on the cube in layers `n, n+1`" fails; with `R_1 >= 42 L` layer `n-1` alone is wide enough. Y 650: "`R_1 >= L`". As the row says, no proof is changed; the check's repaired proof (its R-f paragraph, with the bounds at `R_1 = L^3`) is not copied in.

**R-f-1** (line 199, head of section 7.2; insert one paragraph after the heading and before "Clauses of `rg:structured-local-gauge` ...").
- Old: ``### 7.2 Admission (G0-COV-ADMIT for the final-stage operation), real point``
- New: the same heading, followed by:
  ``**Hypothesis of this section.** `R_1 >= 42 L` (for example `R_1 = L^3`). The floor `R_1 >= L` of Y 650 does not give it: at `R_1 = L` a cube `Q_{8r}` around a gauge cube on the outer face of `Omega_n` can leave `X` (`rim-scale-check.md` section 3, point (i)). No other line of Y that the check found fixes `R_1` from above (Y 651-652, 14941, 16102-16103, 35850 are lower bounds), but this was not searched beyond those lines. The fit (i) named at the end of this section is not proved here; see `rim-scale-check.md` R-f.``
- Status: READY.

## Each changed statement read against its proof (after the edits)

`library/h-geo.md`:

- **Fact 1.1, Fact 1.2** (A1-d, A1-e). Fits: `L M L^q >= L^5 M_1' L^q` from `M >= L^4 M_1'`, then `M_1' >= R_1 frakM` (Y 650-651). Alignment needs only that `M_1'` is a power of `L`.
- **Lemma 3.1** (A1-h, A1-i). Fits. Second rule: `M_1' L^{q+1} = L M_1' L^q > R_1 frakM L^q`. First-rule increment `R_1 frakM L^q + frakM L^{q+1} <= 2 R_1 frakM L^q <= 2 M_1' L^q` uses `R_1 >= L`. Erosion `w_q < 3 M_1' L^q <= 3 L^{-4} M L^q`. The added sentence on the consumer's tower is a citation (Y 132180-132210). That passage writes `M_1` and fixes `M >= L^4 M_1`, `M_1 >= R_1 frakM` (Y 132256-132258), so its `M_1` satisfies the floor the proof uses.
- **Note on Y 12993-12996** (A1-j). Fits. It is a remark, with no proof.
- **Theorem** (A1-k, A2). Fits. (H0) follows from the positive gaps (inclusion `D_q subset D_{q+1}`) and Lemma 3.2. (H5) follows from `J_q subset T_0 = X`, Fact 1.2 and Y 63692. (H1)-(H4) are unchanged and their proof is unchanged. The `mu`-rule is now `mu = M_1'`, which is the case Lemma 3.1 covers.
- **Lemma 2 (d)** (A3-a). Fits. The statement `g_h >= 3 a_{h+1}` is unchanged, and the proof no longer uses the box form at `i = h`. The remaining loose text is in the setting paragraph (A3-b, not applied).
- **Order paragraph, section 0, RESULT** (A1-a, A1-b, A1-l, A1-m). Wording only. Each fits the section 1 notation paragraph (A1-c).

`library/rim-scale.md`:

- **Definition of `lambda(p)`** (R-a). Fits the proof of Theorem 6.2. That proof's last step uses `L(p) = eta L^{lambda(p)}` in `R`, and with R-a this is Y's definition (Y 10540-10541), so the step is now an identity rather than a reading.
- **(I2) and section 8 item 3** (R-b). Fits. The proofs use `K_w` only as the constant of (I2).
- **Theorem 6.2, proof** (R-c). Fits. The needed inclusion is `X cap Omega_m subset` outer two layers, and Y 63760-63765 gives it at `i = m`.
- **Corollary 6.3** (R-d). The statement fits its proof, with one remark on the added proof text (not a new repair):
  1. The location claim needs only that `P` has its bonds in the outer two layers, which `X cap Omega_m` contains by R-c and (G1). The statement already asserts that `P` has its bonds there. So "`P` is in `Omega_m`, hence no corner in the floor" holds without the profile argument.
  2. The profile argument of R-d-2 (the check's case "`U_X` exists") applies (I2), which needs `R(U_X) <= a_c`. In that case the datum's top defects can be as large as `a_1`, so (I1) gives only `R(U_X) <= C_B a_1`, and the file does not state `C_B a_1 <= a_c`. This leaves the distance bound on `tau` conditional, but the location claim does not depend on it (point 1). Unproved remedy: split the cases at `min(a_1, a_c / C_B)` instead of `a_1`.

  Following the row's rule, I did not change the check's text to fix this.
- **Section 7.2, class-M paragraph** (R-e). Fits. With `r = 6 frakM xi_n` the proposition's conclusions give `6 C frakM rho` and `C(1 + 6 frakM) rho`, and its side condition is now listed in section 8 item 5. The stated side `96 frakM xi_n` of `Q_{8r}` (line 211) now agrees with `r`.
- **Section 7.2, hypothesis `R_1 >= 42 L`** (R-f). The proof of section 7.2 is not changed, and it does not yet use the hypothesis: the fit (i) is still listed there as "Not checked". So the hypothesis is stated, but the section still contains no proof that the hypothesis is enough. `rim-scale-check.md` R-f has that argument, and it is not copied in. Section 8 item 1 (the geometry constants) does not list the new floor. The row did not ask for that, so I did not add it.

## Summary

| Repair | File | Status |
|---|---|---|
| A1 (`M_1` -> `M_1'`; Lemma 3.1 `mu = M_1'`, consumer tower first or second rule) | h-geo | READY: 13 edits A1-a to A1-m. NOT APPLIED where h-geo quotes Y in Y's letter (lines 43, 45, 153): which `M_1` Y means there is unsettled. Line 154 holds in both readings and is left as is |
| A2 ((H0), (H5)) | h-geo | READY: A2-a to A2-d |
| A3 (Lemma 2 (d): `O_h := Omega_h^c cap X`; Y 61983-61986, 62103-62125) | h-geo | READY: A3-a. The same loose box form at `i = h` in the setting (line 55) is flagged, NOT APPLIED (not named by the row) |
| R-a (`lambda(p)`) | rim-scale | READY |
| R-b (`K_w`) | rim-scale | READY (two places) |
| R-c (cite Y 63760-63765) | rim-scale | READY |
| R-d (location clause of Corollary 6.3) | rim-scale | READY. Remark: the check's profile step needs `R(U_X) <= a_c`, which is not stated, but the location claim does not depend on it |
| R-e (`r = 6 frakM xi_n`; `36 frakM^2 rho <= eps_*`) | rim-scale | READY. `a_flat >= 13 ...` becomes `7 ...` in 7.2; section 8 item 4 is left unchanged (still sufficient) |
| R-f (`R_1 >= 42 L` as hypothesis of 7.2) | rim-scale | READY as a statement. The proof is unchanged and does not yet use it |

Delivery: none of these edits is applied in place, because the dispatch forbids editing any file except this one. The lead applies them, using the old and new texts above. Each old text was checked to occur exactly once in its file at 5529d4f26. No numeric job was run, and none was needed.

RESULT: All three h-geo repairs (A1-A3) and the six rim-scale repairs (R-a to R-f) are written as exact old/new edits with their Y lines, all READY. They are not applied in place, because the dispatch allows edits only to `library/geo-repairs.md`. A1 is not applied at h-geo's quotes of Y (lines 43, 45, 153). A3's companion box form in the setting (line 55) is flagged and not applied. Every changed statement still fits its proof. Two points stay open: R-d's profile step needs the unstated `R(U_X) <= a_c` (the location claim does not), and R-f's hypothesis `R_1 >= 42 L` is stated but the 7.2 proof does not yet use it (fit (i) stays unchecked in the file). CORE (row 616/640) and the meaning of `M_1` at Y 16102, 62436, 63183 also stay open.
