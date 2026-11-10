lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-10T16:29Z

# geo-repairs (FINISH row 631): text repairs to `library/h-geo.md` and `library/rim-scale.md`

Provenance: Claude Opus 5.5, medium effort, Mac mini worker 2, branch `claude/ym4d-hard-route` at 5529d4f26. Text repairs, no new proof. Not an audit. Status: in progress, written section by section.

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
- New: ``This is the argument of Y 10569-10585. (H0): `A` decreases (section 2, Lemma 2 (d) at `q = h`) and `T` decreases, so Lemma 3.2 gives that `J` decreases; `J_{m+1} = empty` is the convention that the sequence stops at `m`. (H5): `J_q = A_q cap T_q subset T_0 = X`; Fact 1.2 with remark (iii) of section 2 for the partitions; Y 63692 for the torus. `square` ``
- Status: READY.

### A3. Lemma 2 (d): `O_h := Omega_h^c cap X`, with citations

Basis: h-geo-check section 2, item (d). Y gives `O_i = H_i^{[8 a_i]}` only for `i > h` (the step at `h` may create). Y 61983-61986: each step has `Z^{[0]} = bx((Omega_t^c)^{~2} cup R_t'^{~})`, which contains `Omega_t^c`. Y 62103-62125: the three fates (healed, island, drop-out) replace `Omega_l`, `Lambda_l` together on `X` (`Lambda = Z^c`). Y 63818-63820 states `G_h subset Z''_{h+1}(X)` and the separation `>= 3 a_{h+1}` from `G_h` (read; it is the conclusion of (d), not the inclusion `O_h subset G_h`).

**A3-a** (line 87, proof of Lemma 2 (d)).
- Old: ``(d) `D_h = O_h subset G_h subset H_{h+1}`, and `h + 1 <= k_0`, so `Z''_{h+1} = H_{h+1}^{[3 a_{h+1}]}`.``
- New: ``(d) Here `O_h := Omega_h^c cap X`; Y's box form `O_i = H_i^{[8 a_i]}` is stated only for `i > h`, and is not used at `i = h`. `D_h = O_h subset G_h`: each step has `Z^{[0]} = bx((Omega_t^c)^{~2} cup ...) supset Omega_t^c` (Y 61983-61986), and the three fates enlarge `Omega` and `Lambda = Z^c` together (Y 62103-62125). Then `G_h subset H_{h+1}`, and `h + 1 <= k_0`, so `Z''_{h+1} = H_{h+1}^{[3 a_{h+1}]}`; Y 63818-63820 states the same separation `>= 3 a_{h+1}` from `G_h`.``
- Status: READY.

**A3-b, flagged, NOT APPLIED.** The setting paragraph of section 2 (line 55) still reads ``For `h <= i <= m`: `H_i` is a box, `O_i := Omega_i^c cap X = H_i^{[8 a_i]}`, ...``, which states the box form at `i = h`. The row names only Lemma 2 (d), and the rule is to change no statement except as a repair says. After A3-a nothing in the file uses the box form at `i = h` (Lemma 2 (a) uses `G_q`, `H_{q+1}` for `q > h`; (d) now uses `O_h := Omega_h^c cap X`). Suggested wording for the lead, if wanted: ``For `h <= i <= m`: `O_i := Omega_i^c cap X`; for `h < i <= m`, `H_i` is a box and `O_i = H_i^{[8 a_i]}`, ...``. Whether `H_h` and `G_h = H_h^{[10 a_h]}` are given by Y at `i = h` I did not check; the check uses `G_h = Z_h cap X` only.
