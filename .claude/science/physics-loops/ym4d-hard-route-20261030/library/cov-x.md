lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T12:30Z

# cov-x: the assignment (COV) for footprints inside X (FINISH row 628)

Status: DONE 2026-11-10 (one session, Claude Fable 5.2, medium; not checked by another model; no numerics run).

Queue row: FINISH 628. Pinned at commit 1c6a760bb. Source: Sussman and Alpoge, `YM4_1400.tex` at commit
2bc0658f91d2 of the Yang--Mills-LLM-experiment repository; `Y n` is line n of that file.

Credit. The assignment is Sussman and Alpoge's (their text names Claude and Codex as authors): paragraphs
"The datum at an early prepared seam" and "The datum at a compressed prepared seam" (Y 77557-77704), with
Y 65406-65474, 76654-76689, 77810-77831, 78298-78322, 72243-72281, 64221-64232, 64699-64737, 13095-13130.
The stage test and the nest are Bałaban's (CMP 122 (1989) 175, (1.24), p. 182; I read the printed page).
This note writes Y's prose as lemmas with the containments as inclusions of boxes. It uses the notation of
`library/i3-cert.md` (Claude Fable 5.2), `library/inset-chart.md` and `library/h-geo.md`.
Labels: **proved** (a written argument from the stated hypotheses), **read** (a definition or statement
of Y used as a hypothesis, with its lines; not rebuilt), **gap**.
One session of Claude Fable 5.2 (medium). Not checked by another model. No numeric job was run.

## 0. Result

**Verdict: stop condition (iii), in a narrow form.** For every tested plaquette of level `l >= h` of the
old global datum `D(x_N)` with footprint in `X`, a supplier is given and its three conditions are proved
(Theorem 6.1), from six definitions of Y that I read and did not rebuild (D1 to D6, section 2). For the
levels `l < h` (footprint in the core `O_h`) the statement reduces to (COV) at the earlier moment `nu_h`
(the entrance of the first stage of `X`), for the history inside the core. That is the invariant (COV-G)
of FINISH row 632 (`cov-global`), cases "an older mark in the floor of X" and (S-ord). I did not attack it:
row 632 covers it. No counterexample.

| Case (Lemma P) | Level, position of `F(p)` | Supplier, moment | Defect at `x_N` | Status |
|---|---|---|---|---|
| P1 | `l < h`, `F(p) subset O_h` | the supplier that (COV) gives at `nu_h`; the stages do not change the loop (Lemma 5.1) | as at `nu_h` | **reduced to row 632** |
| P2 | `l = h`, mixed at the wall `dO_h` | level-h density test of the core (T5), at `N` | `2.1 eps_h` | **proved** (D6) |
| P3 | `h <= l < j`, `F(p) subset Lay_l` (shell `l`) | shell clause of T9 at `N`; for `l = h` with a corner in `G_h`: T5 | `2 c_0 L_flat^{2(l-k_0-1)_+} eps_l` | **proved** (D4, D5, D6) |
| P4 | `h < l <= j`, mixed at the prepared face `dZ''_l` (items 3 and 5) | exterior clause of the **preceding** guard of the stage of level `l - 1`, at the entrance `nu_{l-1}` of that stage | `2 sqrt(2) c_0 L^2 L_flat^{2(l-k_0-2)_+} eps_l` | **proved** (D1 to D5) |
| P5a | `l = j`, `F(p)` in one exterior region of T9 | exterior clause of T9 at `N` | `6 c_0 L_flat^{2(j-k_0-1)} eps_j` | **proved** (D4, D5) |
| P5b | `l = j`, `F(p)` astride an original wall `dO_{l'}`, `k_0 < l' <= j` (not in the list of six) | level-l' density tests at `nu_{l'}`, then the exact averages of depth `j - l'` | `6 . 4^r e_j` | **proved** (D1 to D3, D6) |
| P6 | `l = m` | top density test T4 at `N` | `2.1 eps_m` | **proved** (D6) |

Four findings for the lead.

1. **Item 5 as the row states it fails; Y's own supplier closes it.** The row asks for the stage test
   "at the moment just after" the stage of level `i`, with a crossing clause astride `dZ''_{i+1}`. In the
   default operation that test has no such clause: its shell clause and its exterior clause both require
   containment (Y 64270-64280, 64371-64373, 78316-78319). The missing clause is `kappa_x` at `dZ''_{i+1}` in
   `chi_m^{(i-h+1)}`; it exists only in the split with an added crossing test (Y 64384-64386) and at the
   final stage of the inset rule. Y does not use it for the datum. Y's supplier is the guard **before**
   the promotion: at the entrance of the stage of level `i` the whole footprint lies in one exterior
   region of the preceding guard, in the layer of index `i`, and the loop is the level-(i+1) plaquette of
   the averages of that background (Y 77557-77589 for `i + 1 <= k_0`, Y 77609-77645 for `i + 1 > k_0`).
   Lemma 6.3 proves this with boxes. The same lemma gives item 3 (the last prepared face), so item 3 does
   not need the crossing clause of T9 either.
2. **(c2) must be weakened.** At the moment of the supplier of P4 the plaquette is a tested plaquette of
   the *prospective* datum `D'(x_nu)`, not of the old datum `D(x_nu)`. In P5b the supplier bounds level-l'
   plaquettes, and the loop at `N` is the plaquette of their `(j - l')`-fold average. So (c2) of
   `library/i3-cert.md` 5.4 is replaced by (c2') of section 3: the loop at `x_N` equals the loop that the
   supplier bounds. Corollary 5.2 of `i3-cert` holds with (c2') by the same two lines.
3. **A seventh case, with a larger constant.** A level-j loop astride an original wall `dO_{l'}`,
   `k_0 < l' < j`, is not bounded by T9 at `N` under the containment reading, and I found no test at scale `j`
   that reads the bare plaquettes astride that wall at any moment (the level-j density tests have bases
   within `4 a_j` of `dO_j`, and these walls are at least `8 a_j` inside `O_j`). Y treats it at Y 77647-77704 with the original
   density test of level `l'` and gets `C L^{2(j-l')} eps_l' <= C' R_j^2 eps_j`. This is the reason for
   `e_l = R_l^2 eps_l` (Y 65409-65411). Consequence: at these loops `psi_j` is of order `R_j^2`, not
   `<= C R_j`; (5.1) of `i3-cert` fails there, and the bound `C e_l` has no spare factor `1/R_l`. Lemma 2b
   of `i3-cert` must be read as `2 psi_l eps_l <= C_2' e_l`, `C_2' = max(C_2, 6 . 4^r)`. This case uses
   neither (LF) nor `L_flat`.
4. **(c3) at a mixed loop.** A guard reads the background localized in `X`, which is constrained on all
   rows of all levels, so it carries the level-l rows and the level-(l-1) rows together (D5). A density
   test does not: its local orbit has prescribed level-l values only, the value on a completed bond being
   the one-step average of the lower rows (Y 76655-76657, 77712-77721). So (s1) of Definition 5.1 of
   `i3-cert` fails for (K-ord) at a mixed loop as written. Lemma 2 needs only the weaker (s1') of
   section 3, which holds.

Lemma 6 of `i3-cert` (third point of the row) is proved in section 7 with "tower holonomy" defined by a
set; it is Y 13095-13130 for `W = X`.

## 1. Repo search

- `grep -n -i "cov" library/open-core.md`: no entry for COV, `cov-x`, supplier or stage test. FINISH rows:
  624 (`i3-cert`, done; states (COV)), 628 (this row), 629 (`cov-read`, done; a reading), 630 (check of
  `i3-cert`), 632 (`cov-global`, the part outside `X`). `library/open-registry.md` line 1006 (COV) names
  this row for footprints in `X`. No other row covers footprints in `X` at levels `>= h`. Row 632 covers
  the history inside the core (its G1 and its case "an older mark in the floor of X"); I stop there.
- `grep -l "early prepared seam\|compressed prepared seam\|original wall" library/*.md library/prior/*.md`:
  `library/prior/cov-read.md` only (its table rows for Y 77557-77590 and Y 77609-77656). It records what Y
  says and proves nothing. `library/i3-cert.md` 5.4 did not use these two paragraphs.
- This checkout has the ref `origin/claude/ym4d-hard-route` only; `origin/main` and the other PR branches
  are not present, so I did not search them.
- Used from the lane: `library/i3-cert.md` sections 2 to 5 and 7 (frame lemmas F1, F2, Lemma 2, Lemma 4);
  `library/h-geo.md` section 2 and Lemma 3.1; `library/inset-chart.md` sections 2, 3;
  `library/rim-scale.md` (I4) with the constant of `library/rim-scale-check.md`.

## 2. Setting, and the six definitions read from Y

Lengths are in bare units, distances in the sup norm. `m` is the depth, `h = m - N_m >= 1`, `j = m - 1`.
`a_i = M R_i L^i` (cell side), `u_i = M L^i`. `B^{[s]}` is the box `B` with each face moved outward by `s`
(inward for `s < 0`). For a box `B` and `s > 0` put `N_s(dB) := B^{[s]} minus B^{[-s]}`.

### 2.1 Boxes (Y 63748-63826; `library/h-geo.md` section 2)

`H_i` (`h <= i <= m`) are boxes with `G_{i-1} subset H_i` for `i > h`, `O_i := Omega_i^c cap X = H_i^{[8 a_i]}`,
`G_i = H_i^{[10 a_i]}`, `G_m = X`. Here `Omega_i` is the label before the operation. `k_0` has
`h < k_0 <= m - 2` and `a_{k_0+1} = u_m`, so

`L^{m - k_0 - 1} = R_{k_0+1}`,  and `a_i >= L u_m` for `i >= k_0 + 2`   (Y 63776-63778).   (2.1)

Write `H := H_{k_0+1}`. The prepared boxes are `Z''_i = H_i^{[3 a_i]}` (`h < i <= k_0`) and
`Z''_i = H^{[3 u_m - w_i]}` (`k_0 < i <= m`), `w_{k_0+1} = 2 u_m`, `w_m = 0`, `w_i = sum_{q=i+1}^m u_q` otherwise.

**Facts B (proved from the formulas; (B2) is `library/h-geo.md` Lemma 2).**

- (B1) `O_h subset G_h subset Z''_{h+1} subset ... subset Z''_m subset O_m`. For `i <= k_0`:
  `O_i subset G_i subset H_{i+1}`. For every `i`: `Z''_i subset H^{[3 u_m]} = O_{k_0+1}^{[-5 u_m]}`.
- (B2) `dist(Z''_i, X minus Z''_{i+1}) >= u_{i+1} = M L^{i+1}` for `h < i < m`; and
  `w_{i-1} - w_i >= u_i` for `k_0 + 2 <= i <= m`.
- (B3) For `k_0 + 1 <= l' <= j`: `O_{l'} supset O_{k_0+1}`, and `O_{l'+1} supset O_{l'}^{[2 a_{l'} + 8 a_{l'+1}]}`.

*Proof.* (B1): `Z''_i subset O_i` for `i <= k_0` since `3 a_i <= 8 a_i`; `O_i subset G_i subset H_{i+1}`;
`H_{i+1} subset Z''_{i+1}` for `i + 1 <= k_0`, and `H subset H^{[u_m]} = Z''_{k_0+1}`. So for `i <= k_0`,
`Z''_i subset H`. For `i > k_0`, `0 <= w_i <= 2 u_m` gives `H^{[u_m]} subset Z''_i subset H^{[3 u_m]}`, and
`O_{k_0+1} = H^{[8 u_m]}`. `Z''_m = H^{[3 u_m]} subset O_{k_0+1} subset O_m` by (B3). (B3):
`O_{i+1} = H_{i+1}^{[8 a_{i+1}]} supset G_i^{[8 a_{i+1}]} = O_i^{[2 a_i + 8 a_{i+1}]}`. `square`

Every `Z''_q`, `O_q`, `G_q` with `q >= l` is a union of aligned level-l blocks (`library/h-geo.md` Fact 1.2
and remark (iii) of its section 2).

### 2.2 The definitions read from Y

I state each as a definition. None is rebuilt here. The proofs below use nothing else about the operation.

**(D1) The sequence at the entrance of a stage (Y 72244-72250, 63836 item (1)).** `nu_i` is the entrance
of the stage of level `i` of the operation on `X`, `h <= i <= j`; `nu_j = N`. Inside `X` the region
sequence in force at `nu_i` is

`A^i_q = Omega_q cap X` (`q <= h`),  `A^i_q = X minus Z''_q` (`h < q <= i`),  `A^i_q = X minus O_q` (`i < q <= m`).

Its layers `Lay^i_q := A^i_q minus A^i_{q+1}` inside `X` are: `Z''_{q+1} minus Z''_q` (`h < q < i`);
`Z''_{h+1} minus O_h` (`q = h < i`); `O_{i+1} minus Z''_i` (`q = i > h`); `O_{h+1} minus O_h` (`q = i = h`);
`O_{q+1} minus O_q` (`i < q < m`); `X minus O_m` (`q = m`). The collar of the stage is
`K_i := O_{i+1} minus Z''_{i+1}`, and the prospective sequence is `A'_q = A^i_q` for `q != i + 1`,
`A'_{i+1} = A^i_{i+1} cup K_i = X minus Z''_{i+1}`. So the prospective sequence at `nu_i` is `A^{i+1}`.
`D_i := D(x_{nu_i})` and `D'_i := D'(x_{nu_i})` are the old and the prospective datum (Definition 4.1 of
`i3-cert`); `Gamma_q`, `Gamma'_q` their row sets.

**(D2) The stage as moves (Y 72252-72260, 64035-64036, 77767-77778).** Between `nu_i` and `nu_{i+1}` the
variables of the point with support in `X` change as follows, and in no other way. (m2) Each new row `c`
(a level-(i+1) bond in `Gamma'_{i+1} minus Gamma_{i+1}`) gets the value `V_{i+1}(c) = M(V_i)(c)`, the
average over its double block of the values at `x_{nu_i}` (constraint (E1), carried at `nu_i`). (m1) The
collar gauge acts on level-i bonds with an endpoint in `K_i`; it is one at the level-(i+1) sites, "so the
coarse row remains fixed". (m3) The level-i bonds with an endpoint in `K_i` and no endpoint in `A^i_{i+1}`
are integrated and leave the point.

**(D3) No other move (SEQ).** Between `nu_h` and `N` no move of another structure of the history changes
a row with an endpoint in `X`, or a region of the sequence inside `X`. (The stages of one operation run
"one value after another", Y 63836 (1); "The core operation ..., which contains the failed tests, is at no
point unfolded", Y 63849. For the other components this is the frame lemma (G2) of row 632 applied to
them.)

**(D4) The guard (Y 63876; Y 64223-64228, 64252-64255, 64270-64280, 64406-64414, 64719-64727, 77576-77585,
77617-77627; Bałaban (1.24)).** `chi_m^{(i-h)}`, the preceding guard at `nu_i`, equals one at `x_{nu_i}`
only if the background `U^{(i-h)}_{m,X}(x_{nu_i})` is defined and, for each *clause region* `R` of the list
below and each bare plaquette with all four corners in `R`, `norm(dU - 1) < t_R`:

- shells `Lay^i_q`, `h <= q < i`: `t = (1 - beta_s(1 - 2^{-(i-q+1)})) L_flat^{2(q-k_0-1)_+} eps_q L^{-2q}`;
- for `i = h`: the region `O_{h+1} minus O_h`, `t = (1 - beta_s/2) eps_h L^{-2h}`;
- for `h < i <= k_0`: `O_i minus Z''_i` and `O_{i+1} minus O_i`, each with `t = (1 - beta_s/2) eps_i L^{-2i}`;
- for `i > k_0`: the deep exterior `E^i_0 := O_{k_0+1} minus Z''_i`, `t = (1 - beta_s/2) L_flat^{2(i-k_0-1)} eps_i L^{-2i}`,
  and `E^i_{l'} := O_{l'+1} minus O_{l'}` for `k_0 < l' <= i`, `t = (1 - beta_s/2) c_{l'} L_flat^{2(i-l'-1)_+} eps_i L^{-2i}`, `c_{l'} <= 3`.

For the first shell `q = h` I use only the part `Z''_{h+1} minus G_h` of `Lay^i_h` (Y's first shell is
"contained in `Omega_h minus Omega_q`" and in `Y = Z''_q`, Y 64406-64410; whether the clause also reads the
core part `G_h minus O_h` does not matter below). Bałaban's list merges the last two regions
(`Omega_{j-1} minus Omega_{j+1}`), and Y 77622-77623 treats the exterior at `i = k_0` as one region. Every
proof below places a footprint inside one region of the list above, so it holds under the merged readings
too. A bare plaquette astride two regions is read by no clause: "The final shell and exterior clauses both
require containment" (Y 64278).

**(D5) The background of the guard (Y 63864, 77629-77630, 13043-13059).** `U^{(i-h)}_{m,X}(x)` is a real
configuration on the bare bonds of `X` with `M^q U = V_q(x)` on every row of level `q` of the joined
determining set of the sequence `A^i` with the tower `T` of `X`, for all `q` at once. The joined rows with
both ends at distance more than `3 M_1 L^m` from `X^c` are the rows of `A^i` there, with the values of
`D_i` (`library/h-geo.md` Lemma 3.1: `X minus T_q` is within `3 M_1 L^q` of `X^c`).

**(D6) Density tests (Y 61973, 62001, 62050, 62078, 64005-64008, 64022-64025, 64699-64716, 77709-77721,
134113-134120).** A level-l test cube has side `M_2 R_l L^l`; the test cubes of level `l` partition every
level-l cell. `chi_l(square)` is a function of the level-l datum of the moment on a neighbourhood of
`square`, where the value on a bond that is not a row is the one-step average of the lower rows.

- (I4_l) If `chi_l(square) = 1` at a point, every level-l plaquette `q` with a corner in `square` has
  `abs(F_q) <= 2.1 eps_l` for the datum loop of that point (rows, and one-step averages on completed
  edges). This is (I4) of `library/rim-scale.md` at a general level, with the constant of
  `library/rim-scale-check.md`; Y 134113-134120 states it for a level-k plaquette.
- (DENS) Carried, and so equal to one on an admitted trajectory: at `N`, `chi_m(square)` for every level-m
  test cube in `Omega_m` (T4); at every `nu_i`, `chi_h(square)` for every level-h test cube in
  `G_h minus O_h` (T5: "bases in `Z_h cap Omega_h cap X`"); at `nu_{l'}`, `h < l' <= j`, `chi_{l'}(square)` for
  every level-l' test cube in `(Omega_{l'}^{~4} minus Omega_{l'+1}^{~}) cap X = O_{l'+1}^{[-a_{l'+1}]} minus O_{l'}^{[-4 a_{l'}]}`
  (T10 at level `l'`; the enlargements `~` are in cells of the level of the region, Y 61973). At `nu_{l'}`
  these tests read the rows of `Lay^{l'}_{l'}` ("Use that layer's actual determining rows", Y 64715-64716).

Also used: (AV2) of `i3-cert` 2.3, on the bare lattice and on the lattice of level `l'` (the averaging
map of each level is the same map in its own units, Y 4905-4960); the frame lemmas F1, F2 of `i3-cert`;
`c_0 = pi/2`.

## 3. The supplier in the form used here

Let `p` be a tested plaquette of level `l >= 1` of `D(x_N)`. For an edge `c` of `p` write `V(c)` for its
datum value: `V_l(c)` on a row edge, `M(V_{l-1})(c)` on a completed edge.

**Definition 3.1.** A *bare supplier* of `p` with allowance `alpha <= alpha_L` is a moment `nu <= N`, a
test `T` carried at `nu` and a real configuration `U` on the bare bonds of `F(p)` with

- (c1) `F(p)` lies in one region on which `T(x_nu) = 1` gives a bare bound, and `eps(U; F(p)) <= alpha L^{-2l}`;
- (c2') `(M^l U)(c) = V(c)` at `x_N`, for each of the four edges `c` of `p`;
- (c3') `U` is the restriction to `F(p)` of the configuration that `T` reads at `x_nu`.

A *coarse supplier* of depth `d = l - l'` is the same with a configuration `W` on the level-l' bonds of
`F(p)`: (c1) `abs(F_q(W)) <= alpha L^{-2d}` for every level-l' plaquette `q` of `F(p)`, each bounded by a
test carried at `nu`; (c2') `(M^d W)(c) = V(c)` at `x_N`; (c3') `W` is the level-l' datum at `x_nu`.

(c2') follows from (c2), (c3) and (s1) of `i3-cert` when these hold, and it is all that the proof of
Lemma 2 there uses.

**Lemma 3.2.** If `p` has a bare supplier, or a coarse supplier, with allowance `alpha`, its defect at
`x_N` is at most `2 alpha`. For a coarse supplier of depth 0 it is at most `alpha`.

*Proof.* By (c2') the datum loop of `p` at `x_N` is `(M^l U)(dp)`, respectively `(M^d W)(dp)`. (AV2) on the
bare lattice with (c1) gives `abs(F_p) <= 2 alpha`; (AV2) on the level-l' lattice, depth `d`, gives the
same; for `d = 0` the loop is the plaquette of `W`. `norm(e^{iF} - 1) <= abs(F)`. `square`

**Lemma G (footprints).** Let `p` be a level-l plaquette, `l >= 1`.
(a) Every point of `F(p)` is within `3 L^l / 2` of every corner of `p`, and `F(p)` has diameter `2 L^l`.
(b) Let `S` be a union of aligned level-l blocks. If no corner of `p` is in `S`, `F(p) cap S` is empty. If
all corners are in `S`, `F(p) subset S`.
(c) Let `B` be a box. If `F(p)` meets `B` and is not contained in `B`, then `F(p) subset N_{2 L^l}(dB)`.

*Proof.* (a) `F(p)` is a box of sides `2L^l, 2L^l, L^l, L^l` and the corners are the centres of its four
blocks. (b) `F(p)` is the union of the blocks of the corners. (c) A point of `F(p)` is within `2 L^l` of a
point of `B` and of a point outside `B`. `square`

## 4. The partition (proved)

`x_N in Ent_N`, and `p` is a tested plaquette of level `l >= 1` of `D(x_N) = D_j` with `F(p) subset X`
(Definition T of `i3-cert`: a corner in `A^j_l`, no corner in `A^j_{l+1}`; then the corners are in
`Lay^j_{l-1} cup Lay^j_l`).

**Lemma P.** Exactly one of the following holds.

- (P1) `l < h`. Then `F(p) subset O_h`.
- (P2) `l = h` and a corner of `p` is in `O_h`. Then another corner is in `O_h^{[L^h]} minus O_h subset G_h minus O_h`.
- (P3) `h <= l < j` and all corners are in `Lay^j_l`. Then `F(p) subset Lay^j_l`, that is
  `F(p) subset Z''_{l+1} minus Z''_l` for `l > h` and `F(p) subset Z''_{h+1} minus O_h` for `l = h`.
- (P4) `h < l <= j` and a corner of `p` is in `Z''_l`. Then `F(p) subset N_{2 L^l}(dZ''_l)`.
- (P5) `l = j` and no corner is in `Z''_j`. Then `F(p) subset O_m minus Z''_j`, and either
  (P5a) `F(p)` lies in one of the regions `E^j_0 = O_{k_0+1} minus Z''_j`, `E^j_{l'} = O_{l'+1} minus O_{l'}`
  (`k_0 < l' <= j`), or (P5b) there is exactly one `l'` with `k_0 < l' <= j` such that `F(p)` meets `O_{l'}`
  and is not contained in it; then `F(p) subset N_{2 L^j}(dO_{l'})`.
- (P6) `l = m`. Then a corner of `p` is in `X minus O_m = X cap Omega_m`.

*Proof.* The cases are disjoint by the level and by the stated positions. Exhaustion, by the level.

`l < h`: no corner is in `A^j_{l+1} = Omega_{l+1} cap X`, a union of level-l blocks, so by Lemma G (b)
`F(p) subset X minus Omega_{l+1} subset X minus Omega_h = O_h` (the label is decreasing and `l + 1 <= h`).

`l = h`: no corner is in `A^j_{h+1} = X minus Z''_{h+1}`, so `F(p) subset Z''_{h+1}` (Lemma G (b)). If a corner
is in `O_h`: some corner is in `A^j_h = X minus O_h`, and two corners of a level-h plaquette are within
`L^h` of each other; `L^h <= 2 a_h`. This is (P2). Otherwise all corners are in `Z''_{h+1} minus O_h = Lay^j_h`,
and Lemma G (b) with `S = O_h` gives (P3).

`h < l < j`: no corner is in `X minus Z''_{l+1}`, so `F(p) subset Z''_{l+1}`. If a corner is in `Z''_l`, another
one is outside (a corner is in `A^j_l = X minus Z''_l`), so `F(p)` meets `Z''_l` and its complement, and
Lemma G (c) gives (P4). Otherwise Lemma G (b) with `S = Z''_l` gives (P3).

`l = j`: no corner is in `A^j_m = X minus O_m`, so `F(p) subset O_m`. A corner in `Z''_j` gives (P4) as
before. Otherwise `F(p) subset O_m minus Z''_j`. By (B1), (B3) the boxes
`Z''_j subset O_{k_0+1} subset O_{k_0+2} subset ... subset O_j subset O_m` are nested (`j >= k_0 + 1`), so the
regions `E^j_0, E^j_{k_0+1}, ..., E^j_j` partition `O_m minus Z''_j`. If `F(p)` is in none of them, it meets
some `O_{l'}` and its complement; then `F(p) subset N_{2 L^j}(dO_{l'})` (Lemma G (c)). Two walls `dO_{l'}`,
`dO_{l''}`, `l' < l''`, are at distance at least `8 a_{l'+1} >= 8 L u_m > 4 L^j` by (B3) and (2.1), so `l'` is
unique.

`l = m`: a corner is in `A^j_m = X minus O_m`. `square`

Remark. Items 2 to 6 of `i3-cert` 5.4 are P3, P4 with `l = j`, P5a, P4 with `l < j`, P6. Item 1 is P1 with
P2. P5b is not in that list.

## 5. What a stage changes (proved from D1 to D3)

**Lemma 5.1.** Assume (D1), (D2), (D3). Let `h <= i < j`.

(a) `D_{i+1} = D'_i`. In detail: the sequence at `nu_{i+1}` is `A^{i+1}`; the rows of level `q notin {i, i+1}`
are those of `D_i` with the same values; `Gamma'_i subset Gamma_i` with the same values;
`Gamma_{i+1} subset Gamma'_{i+1}` with the same values on `Gamma_{i+1}`; each new row `c` has
`V_{i+1}(c) = M(V_i(x_{nu_i}))(c)`.

(b) Let `p` be a level-l plaquette with `l <= i`. Then `p` is a tested plaquette of `D_{i+1}` if and only
if it is a tested plaquette of `D_i` and (when `l = i`) no corner of `p` is in `K_i`. In that case the
datum values `V(c)` of its four edges are the same at `x_{nu_i}` and at `x_{nu_{i+1}}`.

*Proof.* (a) `Gamma_q` is defined from the members of index `q` and `q + 1` (the level-q bonds that touch
`A_q` and have no endpoint in `A_{q+1}`). By (D1) only the member of index `i + 1` changes, and it grows by
`K_i`. So `Gamma_q` is unchanged for `q notin {i, i+1}`; `Gamma'_i` is `Gamma_i` without the bonds that
have an endpoint in `K_i`; `Gamma'_{i+1} supset Gamma_{i+1}`. By (D2) and (D3) the only variables that
change are the new rows, which get the stated values, and level-i bonds with an endpoint in `K_i`. No
bond of the second kind is in `Gamma'_i`, and none is a row of another level.

(b) The tested status depends on `A_l` and `A_{l+1}`. For `l < i` both are unchanged. For `l = i`,
`A_l` is unchanged and `A'_{l+1} = A_{l+1} cup K_i`; this gives the equivalence. Values: a row edge of `p`
in `D_{i+1}` is in `Gamma'_l`; for `l < i` this is `Gamma_l`, for `l = i` it is a subset of `Gamma_i`, and
in both cases the value is unchanged by (a). Conversely, for `l = i` a row edge of `p` in `D_i` has its
endpoints among the corners of `p`, which are not in `K_i`, so it is in `Gamma'_i`. An edge is completed
when both ends are in `A_{l-1} minus A_l`, which is unchanged since `l <= i`; its value is the average of
level-(l-1) rows of its double block, unchanged by (a) since `l - 1 < i`. `square`

**Corollary 5.2.** (i) A tested plaquette of level `l <= j` of `D_j` is, for every `i` with
`max(l, h) <= i <= j`, a tested plaquette of `D_i`, with the same edge values, hence the same datum loop
(not only a conjugate). (ii) For `h < l <= j` it is a tested plaquette of `D'_{l-1} = D_l` with the same
edge values.

*Proof.* Lemma 5.1 (b) downward from `i + 1 = j` to `i = max(l, h)`; (ii) is the case `i = l` with (a). `square`

This is the statement that the row asks for "the stages between `i` and `j`": Y 72246-72251 ("The only
member of the sequence that changes is the one of index `j+1` ... The level-`j` determining rows that
remain are a subset of the old rows. The margin from the next region leaves the higher row read sets
unchanged") applied at each stage, and Y 77590-77600. Y 65522-65523 is the case of the last stage.

## 6. The suppliers

Throughout, `x_0, ..., x_N` is an admitted trajectory (Definition 4.3 of `i3-cert`), so every test carried
at a moment `nu <= N` equals one at `x_nu`, and (E1) holds at each `nu_i`. `gamma` is so small that each
allowance below is at most `alpha_L`; by Lemma F4 of `i3-cert` this is a ceiling on `gamma` that depends
on `(L, L_flat, r, c_5, Bbar)` only.

**Theorem 6.1 (COV-X for levels `>= h`).** Assume (D1) to (D6), (FR), (T1), (T3) of `i3-cert`. Let `p` be a
tested plaquette of level `l >= h` of `D(x_N)` with `F(p) subset X`. Then `p` has a supplier in the sense of
Definition 3.1, or is bounded directly by (I4_l), as in the table of section 0. Its defect at `x_N` is at
most `C_2' e_l`, with `C_2' := max(C_2, 6 . 4^r)` and `C_2` of Lemma 2b of `i3-cert` (which uses (LF); without
(LF) take the constant `2 . 4^r L^2 L_flat^2 A_L` of its 5.3).

*Proof.* Lemma P, then Lemmas 6.2 to 6.5. In cases P3, P4, P5a the allowance is `psi_l eps_l` with
`psi_l <= 3 sqrt(2) c_0 L^2 L_flat^{2e}`, `e <= (l - k_0 - 1)_+`, which is (5.1) of `i3-cert`, so Lemma 2b there
gives `2 psi_l eps_l <= C_2 e_l`. In P2, P6 and P3 with a corner in the core the defect is at most
`2.1 eps_l <= C_2 e_l`. In P5b it is at most `6 . 4^r e_j`. `square`

### 6.2 Cases P3 and P5a: the preceding guard T9 at `N` (items 2 and 4)

**Lemma 6.2.** Let `p` be in case P3 with no corner in `G_h`, or in case P5a. Then
`nu = N`, `T = chi_m^{(j-h)}` (T9), `U = U^{(j-h)}_{m,X}(x_N)` is a bare supplier with
`alpha = c_0 L_flat^{2(l-k_0-1)_+} eps_l` (P3), `alpha = 3 c_0 L_flat^{2(j-k_0-1)} eps_j` (P5a).

*Proof.* (c1). P3, `l > h`: `F(p) subset Lay^j_l`, a shell region of (D4), threshold at most
`L_flat^{2(l-k_0-1)_+} eps_l L^{-2l}`. P3, `l = h`, no corner in `G_h`: `F(p) subset Z''_{h+1} minus G_h` by
Lemma G (b) with `S = G_h`; this is the part of the first shell that (D4) uses. P5a: `F(p)` is in one
exterior region, threshold at most `3 L_flat^{2(j-k_0-1)} eps_j L^{-2j}`. A bare plaquette with corners in
`F(p)` has all corners in the region. `abs(F) <= c_0 norm(dU - 1)`.
(c3') is the definition of T9.
(c2'). All corners of `p` are in `Lay^j_l`, so no edge is completed. Each edge `c` touches `A^j_l` and has
no endpoint in `A^j_{l+1}`: it is in `Gamma_l`. `F(p) subset O_m`, and `O_m` is at distance `2 a_m > 3 M_1 L^m + L^m`
from `X^c` (`X = O_m^{[2 a_m]}`, `a_m >= L^4 M_1 L^m`). So by (D5) `(M^l U)(c) = V_l(c)`. `square`

### 6.3 Case P4: the guard before the promotion (items 3 and 5; the crux)

**Lemma 6.3.** Let `h < l <= j`, `i := l - 1`, and let `p` be in case P4 (a corner in `Z''_l`). Then
`nu = nu_i`, `T = chi_m^{(i-h)}` (the preceding guard at the entrance of the stage of level `i`),
`U = U^{(i-h)}_{m,X}(x_{nu_i})` is a bare supplier with `alpha = sqrt(2) c_0 L^2 L_flat^{2(l-k_0-2)_+} eps_l`.

*Proof.* By Lemma P, `F(p) subset N := N_{2 L^l}(dZ''_l)`.

Step 1 (c1): `N` lies in one exterior region `R` of `chi_m^{(i-h)}`, and `R subset Lay^i_i`. Three cases.

- `l <= k_0`. `Z''_l = H_l^{[3 a_l]}`, so `N subset H_l^{[3 a_l + 2 L^l]} minus H_l^{[3 a_l - 2 L^l]} subset H_l^{[8 a_l]} minus H_l subset O_l minus O_{l-1}`,
  because `2 L^l <= 3 a_l` and `O_{l-1} subset H_l` (B1). `R = O_{i+1} minus O_i`: for `i = h` it is the region of
  the stage-zero guard, for `h < i < k_0` the second exterior region. `R subset O_{i+1} minus Z''_i = Lay^i_i`
  since `Z''_i subset O_i` (for `i = h`, `Lay^h_h = R`).
- `l = k_0 + 1`. `Z''_l = H^{[u_m]}`, `O_l = H^{[8 u_m]}`, `O_{l-1} subset H`, `2 L^l <= u_m`; so again
  `N subset O_l minus O_{l-1} = R subset Lay^i_i`, `i = k_0`.
- `l >= k_0 + 2`. `Z''_l = H^{[3 u_m - w_l]}`, so `N subset H^{[3 u_m - w_l + 2 L^l]} minus H^{[3 u_m - w_l - 2 L^l]}`.
  `3 u_m - w_l + 2 L^l <= 8 u_m`, and `w_i - w_l >= u_l >= 2 L^l` by (B2), so
  `H^{[3 u_m - w_i]} subset H^{[3 u_m - w_l - 2 L^l]}`. Hence `N subset H^{[8 u_m]} minus H^{[3 u_m - w_i]} = O_{k_0+1} minus Z''_i = E^i_0 =: R`,
  the deep exterior of the guard at `nu_i` (`i >= k_0 + 1`), and `R subset O_{i+1} minus Z''_i = Lay^i_i`.

In each case the threshold of `R` is at most `L_flat^{2(i-k_0-1)_+} eps_i L^{-2i}` (the factor `c_{l'}` is one
in these regions). So

`eps(U; F(p)) <= c_0 L_flat^{2(l-k_0-2)_+} eps_{l-1} L^{-2(l-1)} <= sqrt(2) c_0 L^2 L_flat^{2(l-k_0-2)_+} eps_l L^{-2l}`,

by `eps_{l-1}/eps_l <= sqrt(2)` (proof of Lemma F1 of `i3-cert`, case `l < s`).

Step 2 (c3'): `U` is the background that the guard reads at `x_{nu_i}`. Every level-i bond `b` with both
ends in `F(p)` has its ends in `Lay^i_i`, so it touches `A^i_i` and has no endpoint in `A^i_{i+1}`: it is a
row of `D_i`. `F(p) subset O_m`, so by (D5) (as in 6.2) `(M^i U)(b) = V_i(b)(x_{nu_i})`.

Step 3 (c2'): By Corollary 5.2 (ii), `p` is a tested plaquette of `D'_i`, and its edge values at `x_N` are
its edge values in `D'_i`. Let `c` be an edge of `p`; its double block lies in `F(p)`.
If `c` is a row edge in `D'_i`: its endpoints are in `F(p) subset O_{i+1}`, so `c` does not touch
`A^i_{i+1} = X minus O_{i+1}`; it is not an old row, so it is a new row, and by (D2)
`V_l(c) = M(V_i(x_{nu_i}))(c)`.
If `c` is a completed edge in `D'_i`: its value is `M(V_i)(c)` over the rows of `Gamma'_i` in its double
block, which have the values of `D_i` (Lemma 5.1 (a)).
In both cases, by Step 2, `V(c) = M(M^i U)(c) = (M^l U)(c)`. `square`

Remarks. (1) This is Y's argument: "In the layer of index `j` before promotion ... The local preceding
background has the actual old level-`j` datum on this footprint. Every first-kind link of the new test
is promoted there, and every second-kind link uses the same retained level-`j` blocks. Their common
coarse values are exactly the one-step averages ... The guard on the full bare carrier and the averaging
estimate give a defect at most `C_L F_j eps_j`" (Y 77621-77638), "The preceding guard is available before
deletion ... This also applies to the last prepared face before the final collar integration"
(Y 77641-77645); for `l <= k_0`, Y 77575-77589.
(2) No crossing clause is used, and no clause of a guard later than `chi_m^{(i-h)}`. The test is used at
its own moment; Lemma 1 of `i3-cert` makes it available at `x_N`.
(3) The supplier that the row proposes (the guard `chi_m^{(i-h+1)}` after the stage) needs a bound on the
bare plaquettes astride `dZ''_l`. In the default operation no clause of that guard reads them (D4;
Y 64278, 64371-64373). In the operation with the added crossing tests (Y 64384-64386, 64437-64463) it
has the clause `kappa_x` at `(1 - 3 beta_s/4) F_i eps_i L^{-2i}`, and then the three clauses with Lemma 2a
of `i3-cert` give a second supplier, with the same `alpha` up to the factor 3. I did not write that
variant out; it is not needed.

### 6.4 Case P5b: an original wall in the exterior (not in the list of six)

**Lemma 6.4.** Let `p` be in case P5b at the wall `dO_{l'}`, `k_0 < l' <= j`, and `d := j - l'`. Then
`nu = nu_{l'}`, the level-l' density tests of (DENS) and `W :=` the level-l' datum of `D_{l'}` on `F(p)` are a
coarse supplier of depth `d`, with `alpha = 3 . 4^r e_j` if `d >= 1`. The defect of `p` at `x_N` is at most
`6 . 4^r e_j` if `d >= 1`, and at most `2.1 eps_j` if `d = 0`.

*Proof.* `F := F(p) subset N := N_{2 L^j}(dO_{l'}) = O_{l'}^{[2 L^j]} minus O_{l'}^{[-2 L^j]}`.

Step 1 (position). (i) `O_{l'}^{[2 L^j]} subset O_{l'+1}^{[-a_{l'+1}]}`, by (B3) and `2 a_{l'} + 7 a_{l'+1} >= 2 L^j`.
(ii) `O_{l'}^{[-4 a_{l'}]} subset O_{l'}^{[-2 L^j]}`, since `a_{l'} >= u_m` by (2.1). (iii) Every `Z''_t` lies in
`O_{k_0+1}^{[-5 u_m]} subset O_{l'}^{[-5 u_m]} subset O_{l'}^{[-2 L^j]}` by (B1), (B3); so `N cap Z''_t` is empty for
every `t`. (iv) Hence `N subset O_{t+1} minus Z''_t = Lay^t_t` and `N subset O_{t+1} minus Z''_{t+1} = K_t` for `l' <= t < j`,
and `N subset Lay^j_j`.

Step 2 (c1, c3'). By (i), (ii), `N` lies in `O_{l'+1}^{[-a_{l'+1}]} minus O_{l'}^{[-4 a_{l'}]}`, a union of level-l'
cells. Each site of it is in a level-l' test cube inside it, and by (DENS) the test of that cube is
carried at `nu_{l'}`. By (iv) every level-l' bond with both ends in `F` is a row of `D_{l'}`. So by (I4_{l'}),
every level-l' plaquette `q` with its corners in `F` has `abs(F_q(W)) <= 2.1 eps_{l'}`.

Step 3 (c2'). For `l' <= t <= j` let `B_t` be the set of level-t bonds `b` such that the order-t blocks
of both endpoints lie in `F`. Claim: every `b in B_t` is a row of `D_t`, and `V_t(b)(x_{nu_t}) = (M^{t-l'} W)(b)`.
For `t = l'` this is Step 2. Let it hold for `t < j`, and let `b in B_{t+1}`. Its endpoints are in
`F subset K_t subset A'_{t+1}`, and not in `X minus O_{t+1} supset A^t_{t+2}`; so `b` is in `Gamma'_{t+1}`, and it
does not touch `A^t_{t+1} = X minus O_{t+1}`, so it is a new row. By (D2), `V_{t+1}(b) = M(V_t(x_{nu_t}))(b)`.
The average reads the level-t bonds of the double block of `b`; these are in `B_t`. So
`V_{t+1}(b) = M(M^{t-l'} W)(b) = (M^{t+1-l'} W)(b)`, and by Lemma 5.1 (a) this is the value at `x_{nu_{t+1}}`,
where `b` is a row of `D_{t+1} = D'_t`. The four edges of `p` are in `B_j`, and they are rows (all corners
are in `Lay^j_j`). So `V(c) = (M^d W)(c)` at `x_N`.

Step 4 (allowance). `d = 0`: the loop of `p` is the plaquette of `W`, bounded by Step 2. `d >= 1`:
`2.1 eps_{l'} = alpha' L^{-2d}` with `alpha' = 2.1 L^{2d} eps_{l'}`. Now `d <= j - k_0 - 1 = m - k_0 - 2`, so by (2.1)
`L^{2d} <= L^{-2} R_{k_0+1}^2`, and Lemma F2 of `i3-cert` (with `k = m`, `l = j`) gives `R_{k_0+1} <= 2^r L R_j`.
So `L^{2d} <= 4^r R_j^2`. With `eps_{l'} <= sqrt(2) eps_j`: `alpha' <= 2.1 sqrt(2) 4^r R_j^2 eps_j <= 3 . 4^r e_j`.
Lemma 3.2. `square`

Remarks. (1) This is Y 77651-77704: "A remaining new footprint meets an original face `dOmega_l`, with
`k_0+1 <= l <= q`. Consecutive original walls ... are separated by at least `8a_{l+1}`, so the footprint
meets only one wall level. Use the density test at that face before it is removed. ... the level-`q` field
on the remaining tube is the iterated average of the same `V_l` ... Apply the full-carrier estimate ...
once at depth `q-l`. This gives a bound `C L^{2(q-l)} eps_l <= C' R_q^2 eps_q`." Y's tube of width `3u/2`
is replaced here by the single footprint, which is enough for one plaquette.
(2) Under Bałaban's merged last region `Omega_{j-1} minus Omega_{j+1}` the wall `l' = j` is inside a region of
T9 and Lemma 6.2 applies to it as well. The walls `l' < j` are not: at `N` they separate two regions of
every reading of (1.24), and the guards of the earlier stages read them only at the scale `l'`.
(3) One averaging estimate of depth `d` is applied once. The constant `6 . 4^r` is not a product over
levels: `L^{2d}` is the exact scale factor, and it is bounded by `R^2` through the compression identity.

### 6.5 Cases P2, P6, and P3 at the core: density tests at `N` (items 1 (part) and 6)

**Lemma 6.5.** (a) In case P6 the defect of `p` at `x_N` is at most `2.1 eps_m`. (b) In case P2, and in case
P3 with `l = h` and a corner in `G_h`, it is at most `2.1 eps_h`.

*Proof.* (a) A corner of `p` is in `X minus O_m`, a union of level-m cells inside `Omega_m`. It lies in a
level-m test cube inside `Omega_m`, whose test is carried at `N` (DENS, T4). (I4_m). (b) A corner of `p` is
in `G_h minus O_h` (Lemma P for P2; in P3 the corners are outside `O_h`). `G_h minus O_h` is a union of
level-h cells, so the corner is in a level-h test cube inside it, whose test is carried at `N` (DENS, T5).
(I4_h). `square`

Here `nu = N`, and (c2') is void: (I4_l) bounds the datum loop of the point itself, with the completed
edges read as one-step averages. This is finding 4 of section 0.

### 6.6 Case P1: the core (item 1; reduced, not proved)

**Lemma 6.6.** Assume (D1) to (D3). Let `p` be in case P1 (`l < h`, `F(p) subset O_h`). Then `p` is a tested
plaquette of `D_h = D(x_{nu_h})` with the same datum loop.

*Proof.* Corollary 5.2 (i) with `max(l, h) = h`. `square`

So any supplier of `p` at a moment `nu <= nu_h` is a supplier at `N`. What is missing is the supplier at
`nu_h`: the statement (COV) at the moment `nu_h` for the tested plaquettes of level `< h` with footprint
in `O_h`. The core `G_h = X cap Z_h` holds an older large-field region with its own history (`H_h` is the
hull of `X cap Z_{h-1}`, not empty, Y 63767-63768): ordinary places with the density tests of their levels,
and possibly older standing marks, islands and restored cores. Y: "the tests and delta functions that
stand under the core operation ... make the data stored in the core regular" (Y 63876); "The old core also
keeps its own tests" (Y 77816). This is (COV-G) of FINISH row 632 at an earlier moment (its steps G1, G3
and the case "an older mark in the floor of X" of G4). I stop here: row 632 covers it.

The induction is well founded: (COV-X) at `N` uses (COV) only at the earlier moment `nu_h`, and row 632
uses (COV-X) only at moments that are not later than the one it treats.

## 7. Lemma 6 of `i3-cert` (third point of the row; proved, with one definition)

`T_0 = X supset T_1 supset ... supset T_m` is the tower of `X`, `A' = A^m` the prospective sequence at `N`
(`A'_m = X minus Z''_m`), `J_q = A'_q cap T_q` the prospective joined sequence. The joined datum has the
global prospective value on each row of the joined set that is a row of `A'`, and the face lift of `V_m`
on the other rows ("The localized datum agrees with the original datum on old rows. On a new collar row
it is the exact face lift", Y 13057-13062). Put

`Int := { x in X : dist(x, X^c) > 3 M_1 L^m + 2 L^m }`.

**Definition 7.1.** A tested plaquette `p` of the joined datum, of level `l`, is *interior* if
`F(p) subset Int`; a *tower holonomy* if it is not interior and `l < m`; a *rim top plaquette* if it is not
interior and `l = m`.

**Lemma 7.2.** (a) An interior `p` is a tested plaquette of the global prospective datum `D'(x_N)`, with
the same edge values, and `F(p) subset X`. (b) A rim top plaquette has all corners in `X cap Omega_m`, so a
corner in a carried top density cube. (c) A tower holonomy has all corners in `X cap Omega_m` and none in
`T_{l+1}`.

*Proof.* Every `y` with `dist(y, X^c) > 3 M_1 L^m` is in `T_q` for all `q <= m` (`library/h-geo.md` Lemma 3.1).
(a) All sites of `F(p)` are such points. So for each of them and each `q`, membership in `J_q` and in `A'_q`
agree. The tested status (a corner in the member `l`, none in the member `l + 1`), the row status of an
edge, and the completed status of an edge are therefore the same for the two sequences. A row edge has
the global value by the definition of the joined datum. A completed edge is the average of the
level-(l-1) bonds of its double block, which lies in `F(p)`; these are rows of both sequences with the
same values. (b), (c): `F(p)` has a point within `3 M_1 L^m + 2 L^m` of `X^c` and diameter at most `2 L^m`, so
all of it is within `3 M_1 L^m + 4 L^m < 2 a_m` of `X^c`, hence outside `O_m = X^{[-2 a_m]}`: `F(p) subset X cap Omega_m`.
For (b), `X minus O_m` is covered by the level-m test cubes in `Omega_m` (DENS). For (c), the corners are in
`X cap Omega_m subset A'_{l+1}` and not in `J_{l+1}`, so not in `T_{l+1}`. `square`

**Corollary 7.3 (Lemma 6 of `i3-cert`).** A tested plaquette of the prospective joined datum of `X` that is
not a tower holonomy and has no corner in a carried top density cube is interior; it is a tested
plaquette of the global prospective datum with footprint in `X` and the same loop.

This is Y 13095-13130 with `W = X`, `j_a = m` ("Every joined test is of one of two kinds ... In the interior
case all determining rows used by the test are ambient rows. The holonomy, including its one-step
averages on mixed rows, is the original holonomy"). The step that `i3-cert` took as a definition is now
the set `Int`. Not proved here: that a tower holonomy is one or a top plaquette of `V_m`; that is (R1) of
`library/rim-scale.md` (Y 13118-13125), and the certificate does not need it from this row.

**Corollary 7.4 (part (i) of the certificate needs footprints in `X` only).** In Lemma 4 of `i3-cert`,
applied to a prospective tested plaquette `P` with `F(P) subset X`, Corollary 5.2 of `i3-cert` is used for
`P` itself (cases `l <= j` and case B) or for the level-j plaquettes of the stencil `D(P)` (case A). The
footprint of such a level-j plaquette is the union of the order-j blocks of its corners, which lie in
`F(P)`. So only tested plaquettes with footprint in `X` occur. `square`

## 8. What is proved, what is read, what stays open

Proved here, from (D1) to (D6): Facts B, Lemma G, Lemma P (the partition), Lemma 5.1 and Corollary 5.2
(what the stages change), Lemmas 6.2 to 6.6, Theorem 6.1, Lemma 7.2 with its corollaries.

Read, not rebuilt (each is a definition of Y's operation, or a statement that another file owns):

1. (D1), (D2): the sequence and the moves of a stage. Y gives them in prose (Y 72244-72260, 77767-77778).
2. (D3): no move of another structure inside `X` between `nu_h` and `N`. For the other components this is
   (G2) of row 632.
3. (D4): the regions and thresholds of the guard. Two readings exist (Y's list and Bałaban's merged last
   region); the proofs hold under both. The thresholds are quoted.
4. (D5): the background of the guard has the rows of all levels of the sequence of its moment.
5. (D6): (I4_l) at a general level (the constant `2.1` is from `library/rim-scale-check.md`), and (DENS),
   the list of density tests carried at `nu_{l'}` and at `N`. The base sets are Y 64699-64701 (lower
   levels), Y 64005-64008 (level `h`), Y 62050 (c) (level `m`). Lemma 6.4 depends on the first: if the
   level-l' tests near the wall `dO_{l'}` were not carried at `nu_{l'}`, case P5b would have no supplier.
6. (AV2) on a coarse lattice (Lemma 3.2, coarse supplier): the averaging corollary of Y applied to the
   lattice of level `l'`. Same status as (AV2) in `i3-cert` 2.3.

Open:

- **P1 (levels below `h`, the core):** (COV) at `nu_h` for footprints in `O_h`. Owner: row 632.
- The first shell: whether the clause of the guard reads `G_h minus O_h` is not decided; it is not needed
  (Lemma 6.5 (b) covers every plaquette with a corner there).

For the lead (registry row COV, and `library/i3-cert.md`; I did not edit them):

1. Replace (c2) of `i3-cert` 5.4 by (c2') of section 3, and (s1) of its Definition 5.1 by the edge form
   in (c2'). Corollary 5.2 of `i3-cert` is then Lemma 3.2.
2. Item 3 and item 5 of `i3-cert` 5.4 have one supplier, the guard before the promotion (Lemma 6.3). The
   repair proposed in `i3-cert` item 5 (the stage test just after the stage, with a crossing clause) is
   not available in the default operation.
3. Add the seventh kind, (K-wall): original density test at the wall, depth `j - l'`, `psi_j <= 3 . 4^r R_j^2`.
   The table of `i3-cert` 5.2 and the bound (5.1) do not contain it. Lemma 2b there becomes
   `2 psi_l eps_l <= C_2' e_l`; the claim `psi_l <= C (log theta_l)^r` (Y 65479-65480) holds for the shells
   and fails at these walls, where `psi` is of order `(log theta)^{2r}`. Every consumer I know of
   (`i3-cert` Lemmas 3, 4, 5) uses `C e_l` only, so nothing breaks; `C_3` becomes `2 c_0 L^2 C_F(1) C_2'`.
4. In case A of Lemma 4 of `i3-cert` (the new level-m plaquettes of the final stage) the stencil `D(P)`
   can contain level-j plaquettes of case P5b. They have the bound `6 . 4^r e_j`, so case A gives
   `2 L^2 c_0 C_2' C_F(1) e_m`. Y's own treatment of the final stage is the same (Y 64097-64102).

RESULT: (COV-X) proved for every tested plaquette of level >= h with footprint in X (Theorem 6.1: seven cases by level and position, each with test, moment, box containment, and equality of the loop), from six definitions of Y that were read and not rebuilt; item 5 holds with the guard before the promotion (the row's supplier, the stage test after the stage, lacks the crossing clause in the default operation), a seventh case at the original walls is added with constant 6 . 4^r e_j, (c2) is weakened to (c2'), and Lemma 6 of i3-cert is proved with "tower holonomy" defined by a set. Open: levels below h in the core (reduced to (COV) at the entrance of the first stage, which is row 632), and a check of (D1) to (D6) against Y by another model.
