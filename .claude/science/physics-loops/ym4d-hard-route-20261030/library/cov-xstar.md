lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T14:12Z

# cov-xstar: the supplier inside X at the exit of each stage (COV-X*) (FINISH row 635)

Status: DONE 2026-11-10 (one session, Claude Fable 5.2, medium; not checked by another model; no numeric
job was run). Pinned at commit e75d7360c. Source: Sussman and Alpoge, `YM4_1400.tex` at commit
2bc0658f91d2 of the Yang--Mills-LLM-experiment repository; `Y n` is line n of that file.

Credit. The argument is Sussman and Alpoge's (their text names Claude and Codex as authors): the
paragraphs "The datum at an early prepared seam" and "The datum at a compressed prepared seam"
(Y 77557-77704), "The datum tested before a stage is integrated" (Y 72243-72281), the final stage
(Y 64088-64102), the density bases (Y 64699-64716), the clause regions (Y 63876, 64221-64228). The stage
test and the nest are Bałaban's (CMP 122 (1989) 175, (1.24)). This note writes that prose as lemmas with
inclusions of boxes, for every stage. It extends `library/cov-x.md` (Claude Fable 5.2, row 628) and serves
`library/cov-global.md` (Claude Fable 5.2, row 632); neither is checked. Notation of those two files.
Labels: **proved** (a written argument from the stated hypotheses), **read** (a definition or statement
of Y used as a hypothesis, with its lines; not rebuilt), **gap**.

## 0. Result

**Verdict: stop condition (i).** (COV-X*) is proved for every stage `h <= i <= t - 1` (Theorem 6.1), from
the six definitions (D1) to (D6) that `library/cov-x.md` reads from Y, used at every stage including the
last one. The direction fixed by the lead holds: the supplier is at the entrance `nu_i` of the stage (the
guard before the promotion), or at the earlier moment `nu_{l'}` (the density tests at an original wall).
No clause of a guard at the exit of a stage is used, and no crossing test. No counterexample.

**Uniform promotion lemma (Lemma 3.1 with Lemmas 4.1, 4.2, 5.1).** Let `h <= i <= t - 1` and
`p in Fr_i(X)`. Then exactly one of three positions holds, and each has a supplier:

| Position of `F(p)` | Stages | Supplier, moment | Allowance `alpha` (defect `<= 2 alpha`) | Status |
|---|---|---|---|---|
| (Q1) a corner in `Z''_{i+1}`; `F(p) subset N_{2 L^{i+1}}(dZ''_{i+1})`, in one exterior region of the guard | all `i` | guard `chi_t^{(i-h)}` at `nu_i`, bare | `sqrt(2) c_0 L^2 L_flat^{2(i-k_0-1)_+} eps_{i+1}` | **proved** (Lemma 4.1; it is Lemma 6.3 of `cov-x`, now also for `i = t - 1`) |
| (Q2) no corner in `Z''_{i+1}`, `F(p)` in one exterior region `R subset Lay^i_i` (this is (U1)) | all `i`; the only other position for `i <= k_0` | guard `chi_t^{(i-h)}` at `nu_i`, bare | `3 sqrt(2) c_0 L^2 L_flat^{2(i-k_0-1)_+} eps_{i+1}` | **proved** (Lemma 4.2) |
| (Q3) `F(p)` astride one original wall `dO_{l'}`, `k_0 < l' <= i` (this is (U2)) | `i >= k_0 + 1` only | level-l' density tests at `nu_{l'}`, coarse, depth `i + 1 - l' >= 1` | `3 . 4^r e_{i+1}` for `i <= t - 2`; `3 . 4^r L^2 e_t` for `i = t - 1` | **proved** (Lemma 5.1) |

In every case the defect of `p` at `x_{nu_{i+1}}` is at most `C_2'' e_{i+1}`, with
`C_2'' := max(C_2, 6 . 4^r L^2)` and `C_2` of Lemma 2b of `library/i3-cert.md`.

Five findings for the lead.

1. **The wall `dO_{i+1}` is not among the walls of (U2).** The row asks for `k_0 < l' <= i + 1`. A plaquette
   of `Fr_i(X)` has all corners in `O_{i+1}`, a union of aligned level-(i+1) blocks, so `F(p) subset O_{i+1}`:
   it does not meet `dO_{i+1}`. The walls are `k_0 < l' <= i`, and the depth `i + 1 - l'` is at least 1. A
   level-(i+1) plaquette astride `dO_{i+1}` has a corner in the old member `X minus O_{i+1}`; it is carried
   over by the stage (Lemma 4.1 (b) of `cov-global`), it is fresh only at step `i + 1`, and its supplier is
   (S-ord). Y's sentence "When `q = l` the bound follows directly from the original positive density test"
   (Y 77699-77701) is this case.
2. **(U2) occurs only in the compressed range `i >= k_0 + 1`.** For `i <= k_0` the collar `K_i` lies in the
   single region `O_{i+1} minus O_i` (because `O_i subset Z''_{i+1}`), so (U1) holds for every exterior
   plaquette. For `i = h` this region is the region of the stage-zero guard (Y 77575-77579).
3. **The constant at the last stage has one more factor `L^2`.** At `i = t - 1` the depth can be
   `t - k_0 - 1`, so `L^{2d} <= R_{k_0+1}^2 <= 4^r L^2 R_t^2` (Lemma F2 of `i3-cert`); for `i <= t - 2` it is
   `d <= t - k_0 - 2` and the factor `L^2` is absent, as in Lemma 6.4 of `cov-x`. So `C_2'` of `cov-x`
   (`max(C_2, 6 . 4^r)`) becomes `C_2'' = max(C_2, 6 . 4^r L^2)` in the table of Theorem 5.1 of `cov-global`
   and in the repairs of row 634. Nothing else changes: the consumers use `C e_l` only.
4. **The guard at `N` is never the first supplier.** Theorem 6.2 states (COV-X) at every stage exit as a
   dichotomy: a tested plaquette of level `l >= h + 1` with footprint in X has either all corners in `O_l`,
   and then it lies in `Fr_{l-1}(X)` and has the supplier of the uniform lemma at a moment `<= nu_{l-1}`; or
   a corner in `X minus O_l = Omega_l cap X`, and then it is fresh only at step `l` and has (S-ord). So in
   Theorem 6.1 of `cov-x`, case P4 is the uniform lemma, and the suppliers of cases P3, P5a (the guard T9
   at `N`) and of P5b at `l' = j` are second suppliers (section 6).
5. **What (m2) of the last stage writes.** The level-t bonds with both ends in `O_t`, at least one end
   outside `Z''_t`: each gets `V_t(c) = M(V_{t-1})(c)` by the retained averaging delta. Y 64097-64100: "the
   averaging blocks of a newly tested plaquette are in the preceding member of level `j`, by the last
   prepared separation, and outside the old `Omega_m`. Here the fine plaquettes are formed from the old
   determining rows, and the exact one-step average gives the coarse bound." Y 77644-77645: "This also
   applies to the last prepared face before the final collar integration." So the last stage is a stage
   like the others, and the guard that supplies it is T9 of `cov-x` at `nu_{t-1}`.

What stays open: (D1) to (D6) are read from Y, not rebuilt, and (D1) to (D3) are used here at the last
stage too (section 2). The check of this file by another model.

## 1. Repo search

- `grep -n -i "cov-x\|COV-X\|promotion lemma\|Fr_i" library/open-core.md`: no entry. FINISH rows near this
  one: 628 (`cov-x`, done), 632 (`cov-global`, done; states (COV-X*) in 4.3 and lists the two instances that
  are not written), 633, 636 (checks), 634 (`i3-repairs`), 637 (`cov-frames-read`, done), 638 (`cov-frames`,
  the read statements F, (R-ord), (R-last), (R-core)). No other row proves (COV-X*). Row 638 owns the frame
  statements; I use (D1) to (D3) as read and do not attack them.
- `grep -l -i "promotion lemma\|Fr_i(X)\|COV-X\*\|preceding exterior" library/*.md library/prior/*.md parts/*.md`:
  `library/cov-global.md` (the statement), `library/open-registry.md` (row COV), `library/prior/cov-read.md`
  (a reading of Y 77557-77590). No proof of the exterior position or of the last stage.
- This checkout has the ref `origin/claude/ym4d-hard-route` only (`git branch -r`); `origin/main` and the
  other YM4D PR branches are not present, so I did not search them.
- `library/cov-x-check.md`, `library/cov-global-check.md` are not present at this commit.

## 2. Setting, and what is read

X is a class component of level `t` with window from `h`. In `cov-x` the depth is `m` and `j = m - 1`;
here `m = t`, `j = t - 1`. Lengths are in bare units, distances in the sup norm. `a_q = M R_q L^q`,
`u_q = M L^q`; `M >= 2`. Boxes `H_q, O_q, G_q, Z''_q`, the index `k_0` (`h < k_0 <= t - 2`), `H = H_{k_0+1}`,
Facts (B1) to (B3), (2.1), and the alignment fact (every `Z''_q, O_q, G_q` with `q >= l` is a union of aligned
level-l blocks): `cov-x` 2.1. Footprints and Lemma G: `cov-x` section 3. Suppliers: Definition 3.1 and
Lemma 3.2 of `cov-x`, with the exit `nu_{i+1}` of the stage in the place of `N`. `c_0 = pi/2`.

`Fr_i(X)` (`h <= i <= t - 1`): the level-(i+1) plaquettes with all four corners in `O_{i+1}` and at least
one corner in `K_i = O_{i+1} minus Z''_{i+1}` (Lemma 4.1 (b) of `cov-global`).

**Read, as in `cov-x` 2.2, with the lines given there:** (D1) the sequence `A^i` at the entrance `nu_i` and
the prospective sequence `A^{i+1}`; (D2) the moves (m1), (m2), (m3) of the stage; (D3) no other move in X;
(D4) the clause regions and thresholds of the guard `chi_t^{(i-h)}` at `nu_i`; (D5) its background; (D6)
(I4_l) and (DENS). Three points on their range.

- (D1), (D2) are stated in `cov-x` for `h <= i <= j`, so they include the last stage `i = t - 1`; its exit
  is `nu_t`, and its prospective sequence is `A^t` (`A^t_q = X minus Z''_q` for `h < q <= t`). Y states them
  for "stage `n + 1` of the operation of level `m`", `j = m_flat + n`, every `n` (Y 72243-72260), and names
  the last stage at Y 64088-64100 and Y 77644-77645. The stages are `j = k_flat, ..., k - 1` (Y 63836 (1)).
- (D3) is stated in `cov-x` between `nu_h` and `N = nu_{t-1}`. I use it between `nu_h` and `nu_t`:
  **(D3\*)** between `nu_h` and `nu_t` no move of another structure changes a row with an endpoint in X or
  a region of the sequence inside X. Same lines (Y 63836 (1) "one value after another", Y 63849, Y 77775);
  it is part of (F-stage) of `cov-global` 4.1, which row 638 owns.
- (DENS) for the levels `h < l' <= t - 1`: Y 64699-64716 states it for every `h < j < m` ("The lower density
  cubes have bases in `(Omega_j^{~4} minus Omega_q^~) cap X` ... Hence the whole density box is in the old
  prepared layer `j`. Use that layer's actual determining rows at the old target"). So the level-l' tests
  near the wall `dO_{l'}` are carried at `nu_{l'}` in the generality needed here (every wall has
  `k_0 < l' <= i <= t - 1`). This is what the row asks under (X4).

**Lemma 2.1 (the stage, every `i`; proved from (D1), (D2), (D3\*)).** Lemma 5.1 of `cov-x` holds for every
`h <= i <= t - 1`: (a) `D_{i+1} = D'_i`; the rows of level `q notin {i, i+1}` are unchanged;
`Gamma'_i subset Gamma_i` and `Gamma_{i+1} subset Gamma'_{i+1}` with the same values; each new row `c` has
`V_{i+1}(c)(x_{nu_{i+1}}) = M(V_i(x_{nu_i}))(c)`. (b) A level-l plaquette, `l <= i`, is tested in `D_{i+1}` if
and only if it is tested in `D_i` and (for `l = i`) has no corner in `K_i`; then its four edge values are
the same at `x_{nu_i}` and `x_{nu_{i+1}}`.

*Proof.* The proof of Lemma 5.1 of `cov-x` uses the stage of level `i` only through (D1), (D2), (D3). For
`i = t - 1` the member that changes has index `t`, there is no member of index `t + 1`, and each sentence of
that proof holds as written. `square`

**Corollary 2.2.** Let `h < l <= i + 1 <= t`. A tested plaquette of level `l` of `D_{i+1}` is a tested
plaquette of `D_l = D'_{l-1}` with the same four edge values.

*Proof.* Lemma 2.1 (b) downward from `i` to `l`. `square`

## 3. The regions of the guard and the partition (X1, X2; proved)

**(X1) The exterior regions of the guard at `nu_i`, from (D4).**

- `i = h`: one region, `O_{h+1} minus O_h = Lay^h_h`.
- `h < i <= k_0`: `O_i minus Z''_i` and `O_{i+1} minus O_i`. Their union is `O_{i+1} minus Z''_i = Lay^i_i`.
  The one wall between them is `dO_i`.
- `k_0 < i <= t - 1`: `E^i_0 = O_{k_0+1} minus Z''_i` and `E^i_{l'} = O_{l'+1} minus O_{l'}`, `k_0 < l' <= i`.
  The boxes `Z''_i subset O_{k_0+1} subset O_{k_0+2} subset ... subset O_{i+1}` are nested ((B1), (B3)), so
  these regions partition `O_{i+1} minus Z''_i = Lay^i_i`. The walls between them are `dO_{l'}`,
  `k_0 < l' <= i`.

So in each range the exterior regions cover `Lay^i_i` as a set, and each lies in `Lay^i_i`. A footprint in
`Lay^i_i` that is in no region is astride a wall: `dO_i` for `h < i <= k_0`, and `dO_{l'}` with
`k_0 < l' <= i` for `i > k_0`. This agrees with Y 64223-64227: "The deep exterior
clause is in `Omega_{i_0+1}^c`, where `i_0 + 1 <= j`, and the other exterior clauses are in
`Omega_l minus Omega_{l+1}` with `l <= j`" (`i_0 = min(j - 1, k_0)`). Thresholds: at most
`F_i eps_i L^{-2i}` with `F_i := L_flat^{2(i-k_0-1)_+}` in every exterior region, except the factor
`c_{l'} <= 3` (`c = 3` only at `i = t - 1`, `l' = t - 1`; Y 63876).

**Lemma 3.1 (partition of `Fr_i(X)`; proved).** Let `h <= i <= t - 1` and `p in Fr_i(X)`. Then
`F(p) subset O_{i+1}`, and exactly one of the following holds.

- (Q1) A corner of `p` is in `Z''_{i+1}`. Then `F(p) subset N_{2 L^{i+1}}(dZ''_{i+1})`.
- (Q2) No corner is in `Z''_{i+1}`, and `F(p)` lies in one exterior region `R` of (X1) with
  `R != O_i minus Z''_i`. Then `F(p) subset K_i cap R`.
- (Q3) No corner is in `Z''_{i+1}`, `i >= k_0 + 1`, and there is exactly one `l'` with `k_0 < l' <= i` such
  that `F(p)` meets `O_{l'}` and is not contained in it. Then `F(p) subset N_{2 L^{i+1}}(dO_{l'}) cap K_i`.

For `i <= k_0` only (Q1) and (Q2) occur, and in (Q2) `R = O_{i+1} minus O_i`. In no case does `F(p)` meet
`Z''_i` (for `i = h`: `O_h`), and in no case does `F(p)` meet `dO_{i+1}` or leave `O_{i+1}`.

*Proof.* `O_{i+1}` is a union of aligned level-(i+1) blocks and contains the four corners, so
`F(p) subset O_{i+1}` (Lemma G (b)).

If a corner is in `Z''_{i+1}`: another corner is in `K_i`, outside `Z''_{i+1}`, so `F(p)` meets the box
`Z''_{i+1}` and its complement, and Lemma G (c) gives (Q1).

Otherwise `Z''_{i+1}` is a union of aligned level-(i+1) blocks that contains no corner, so
`F(p) cap Z''_{i+1}` is empty (Lemma G (b)) and `F(p) subset O_{i+1} minus Z''_{i+1} = K_i`.

Case `i <= k_0`. By (B1), `O_i subset G_i subset H_{i+1} subset Z''_{i+1}` (for `i = k_0`:
`H subset H^{[u_t]} = Z''_{k_0+1}`). So `K_i subset O_{i+1} minus O_i`, which is the region of the stage-zero
guard for `i = h` and the second exterior region for `h < i <= k_0`. This is (Q2).

Case `i >= k_0 + 1`. By (B1), `Z''_{i+1} subset O_{k_0+1}`, and `Z''_i subset Z''_{i+1}`. The sets
`O_{k_0+1} minus Z''_{i+1} subset E^i_0` and `E^i_{l'}` (`k_0 < l' <= i`) partition `K_i`. If `F(p)` is in one
of them, (Q2) holds. If not, `F(p)` meets some `O_{l'}`, `k_0 < l' <= i`, and its complement, and Lemma G (c)
gives `F(p) subset N_{2 L^{i+1}}(dO_{l'})`. Uniqueness: for `k_0 < l' < l'' <= i`, by (B3) and (2.1) the walls
`dO_{l'}`, `dO_{l''}` are at distance at least `8 a_{l'+1} >= 8 L u_t > 2 L^{i+1}`, the diameter of `F(p)`.

The cases are disjoint by their statements. `F(p) cap Z''_i` is empty: in (Q2), (Q3) because
`Z''_i subset Z''_{i+1}` (and `O_h subset Z''_{h+1}`); in (Q1) by Step 1 of Lemma 4.1 below. `square`

## 4. (Q1) and (Q2): the guard before the promotion (X3; proved)

Throughout sections 4 to 6, `x_0, ..., x_N` is an admitted trajectory, so each test carried at a moment
equals one at the point of that moment, and (E1) holds at each `nu_i`; `gamma` is so small that each
allowance is at most `alpha_L` (a ceiling on `gamma` that depends on `(L, L_flat, r, c_5, Bbar)` only, by
Lemma F4 of `i3-cert`).

**Lemma 4.0 (the three steps).** Let `h <= i <= t - 1`, let `p` be a level-(i+1) plaquette with all corners
in `O_{i+1}` and a corner in `K_i`, and let `R` be a clause region of the guard `chi_t^{(i-h)}` at `nu_i` with
threshold `t_R`, such that `F(p) subset R subset Lay^i_i`. Then `nu = nu_i`, `T = chi_t^{(i-h)}`,
`U = U^{(i-h)}_{t,X}(x_{nu_i})` is a bare supplier of `p` at `x_{nu_{i+1}}` with `alpha = c_0 L^{2(i+1)} t_R`.

*Proof.* (c1). A bare plaquette with its corners in `F(p)` has all corners in `R`, so (D4) gives
`norm(dU - 1) < t_R`, and `abs(F) <= c_0 norm(dU - 1)`. So `eps(U; F(p)) <= c_0 t_R = alpha L^{-2(i+1)}`.

(c3'). `U` is the background that the guard reads at `x_{nu_i}`. Moreover: every level-i bond `b` with both
ends in `F(p)` has its ends in `Lay^i_i = A^i_i minus A^i_{i+1}`, so it touches `A^i_i` and has no endpoint
in `A^i_{i+1}`: it is a row of `D_i`. `F(p) subset O_{i+1} subset O_t`, and `O_t` is at distance
`2 a_t > 3 M_1 L^t + L^t` from `X^c`. So by (D5), `(M^i U)(b) = V_i(b)(x_{nu_i})`.   (4.1)

(c2'). `p` is a tested plaquette of `D'_i = D_{i+1}` (a corner in `K_i subset A^{i+1}_{i+1}`; no corner in
`A^{i+1}_{i+2} subset X minus O_{i+1}`). Let `c` be an edge of `p`; its double block lies in `F(p)`.
If `c` is a row edge of `D'_i`: its ends are in `O_{i+1}`, so `c` does not touch `A^i_{i+1} = X minus O_{i+1}`
and is not an old row; it is a new row, and by Lemma 2.1 (a) `V_{i+1}(c)(x_{nu_{i+1}}) = M(V_i(x_{nu_i}))(c)`.
If `c` is a completed edge of `D'_i`: its value at `x_{nu_{i+1}}` is `M(V_i)(c)` over the rows of `Gamma'_i` in
its double block; these are rows of `Gamma_i` with the values of `x_{nu_i}` (Lemma 2.1 (a)).
In both cases the average reads level-i bonds with both ends in `F(p)`, and (4.1) gives
`V(c)(x_{nu_{i+1}}) = M(M^i U)(c) = (M^{i+1} U)(c)`. `square`

**Lemma 4.1 ((Q1), every stage).** In case (Q1), `F(p)` lies in one exterior region `R subset Lay^i_i` of the
guard at `nu_i`, with `t_R <= F_i eps_i L^{-2i}`. So `p` has the bare supplier of Lemma 4.0 with
`alpha = sqrt(2) c_0 L^2 F_i eps_{i+1}`, `F_i = L_flat^{2(i-k_0-1)_+}`.

*Proof.* Put `l = i + 1` and `N = N_{2 L^l}(dZ''_l)`. Step 1 of the proof of Lemma 6.3 of `cov-x` gives
`N subset R` in three cases. Its first two cases (`l <= k_0`, `l = k_0 + 1`) do not involve the top level.
Its third case, `l >= k_0 + 2`, is written there for `l <= j`; for `l = t` it reads: `Z''_t = H^{[3 u_t]}`
(`w_t = 0`), so `N subset H^{[3 u_t + 2 L^t]} minus H^{[3 u_t - 2 L^t]}`; `3 u_t + 2 L^t <= 8 u_t`; and
`w_{t-1} - w_t >= u_t >= 2 L^t` by (B2) (if `t - 1 = k_0 + 1` the difference is `2 u_t`), so
`H^{[3 u_t - w_{t-1}]} subset H^{[3 u_t - 2 L^t]}`. Hence `N subset H^{[8 u_t]} minus Z''_{t-1} = E^{t-1}_0`, the
deep exterior of the guard at `nu_{t-1}`, and `E^{t-1}_0 subset O_t minus Z''_{t-1} = Lay^{t-1}_{t-1}`.
In each case the factor `c_{l'}` is one. `eps_i <= sqrt(2) eps_{i+1}` (proof of Lemma F1 of `i3-cert`, case
`l < s`). Lemma 4.0. `square`

**Lemma 4.2 ((Q2) = (U1), every stage).** In case (Q2), `p` has the bare supplier of Lemma 4.0 at `nu_i`,
with `alpha = 3 sqrt(2) c_0 L^2 F_i eps_{i+1}` (without the factor 3 unless `i = t - 1` and
`R = O_t minus O_{t-1}`).

*Proof.* `R subset Lay^i_i` by (X1). Thresholds, by range. `i = h`: `(1 - beta_s/2) eps_h L^{-2h}`.
`h < i <= k_0`: `R = O_{i+1} minus O_i`, `(1 - beta_s/2) eps_i L^{-2i}`. `i > k_0`: for `R = E^i_0` it is
`(1 - beta_s/2) L_flat^{2(i-k_0-1)} eps_i L^{-2i}`; for `R = E^i_{l'}` it is
`(1 - beta_s/2) c_{l'} L_flat^{2(i-l'-1)_+} eps_i L^{-2i}`, and `(i - l' - 1)_+ <= i - k_0 - 1` since `l' > k_0`.
So `t_R <= 3 F_i eps_i L^{-2i} <= 3 sqrt(2) L^2 F_i eps_{i+1} L^{-2(i+1)}`. Lemma 4.0. In case (Q2) no corner
is in `Z''_{i+1}`, so no edge of `p` is completed and all four edges are new rows. `square`

Remarks. (1) Y for (Q2): "The other new footprints lie in the old exterior `Omega_q^c minus Z''_j`. At the
first promotion their full carrier is in the region `Omega_{i_flat} minus Omega_{i_flat+1}` of the
stage-zero test. At later promotions the preceding exterior guard reads the whole carrier" (Y 77574-77581);
"At a new level-`q` footprint away from the prepared face, use the same calculation when it is contained
in a single preceding exterior region. The factors in those clauses are at most `F_j`" (Y 77647-77651).
(2) Under the merged readings of the clause list (Bałaban's last region `Omega_{j-1} minus Omega_{j+1}`;
the single exterior region at `i = k_0`, Y 77622-77623) each region used above lies in a region of the
merged list with the same threshold bound, so Lemmas 4.1, 4.2 hold; some (Q3) plaquettes then also have
the supplier of Lemma 4.2.
(3) The region `O_i minus Z''_i` (`h < i <= k_0`) contains no footprint of `Fr_i(X)`: it lies in
`Z''_{i+1}`, at distance at least `2 a_i` from `K_i` (`G_i = O_i^{[2 a_i]} subset Z''_{i+1}`).

## 5. (Q3): an original wall (X4; proved)

**Lemma 5.1 ((Q3) = (U2)).** Let `k_0 + 1 <= i <= t - 1`, `p in Fr_i(X)` in case (Q3) at the wall `dO_{l'}`,
`k_0 < l' <= i`, and `d := i + 1 - l' >= 1`. Then `nu = nu_{l'}`, the level-l' density tests of (DENS) and
`W :=` the level-l' datum of `D_{l'}` on `F(p)` are a coarse supplier of `p` at `x_{nu_{i+1}}` of depth `d`,
with `alpha = 3 . 4^r e_{i+1}` if `i <= t - 2` and `alpha = 3 . 4^r L^2 e_t` if `i = t - 1`.

*Proof.* The proof of Lemma 6.4 of `cov-x` with `i + 1` in the place of `j`. I give each step with the
inequalities that change. `F := F(p) subset N := O_{l'}^{[2 L^{i+1}]} minus O_{l'}^{[-2 L^{i+1}]}`. Note
`2 L^{i+1} <= 2 L^t <= u_t <= a_q` for every `q >= k_0 + 1` ((2.1), `M >= 2`).

Step 1 (position). (i) `O_{l'}^{[2 L^{i+1}]} subset O_{l'+1}^{[-a_{l'+1}]}`, by (B3) (`l' <= t - 1`) and
`2 L^{i+1} <= 2 a_{l'} + 7 a_{l'+1}`. (ii) `O_{l'}^{[-4 a_{l'}]} subset O_{l'}^{[-2 L^{i+1}]}`. (iii) Every `Z''_q`
lies in `O_{k_0+1}^{[-5 u_t]} subset O_{l'}^{[-5 u_t]} subset O_{l'}^{[-2 L^{i+1}]}` ((B1), (B3)); so `N cap Z''_q` is
empty for every `q`. (iv) Hence, for `l' <= q <= i`: `N subset O_{l'+1} minus Z''_q subset O_{q+1} minus Z''_q = Lay^q_q`
and `N subset O_{q+1} minus Z''_{q+1} = K_q`.

Step 2 (c1, c3'). By (i), (ii), `N` lies in `O_{l'+1}^{[-a_{l'+1}]} minus O_{l'}^{[-4 a_{l'}]}`, a union of level-l'
cells; each site of it is in a level-l' test cube inside it, whose test is carried at `nu_{l'}` ((DENS),
`h < l' <= t - 1`). By (iv) with `q = l'`, every level-l' bond with both ends in `F` is a row of `D_{l'}`. By
(I4_{l'}), every level-l' plaquette `q` with its corners in `F` has `abs(F_q(W)) <= 2.1 eps_{l'}`.

Step 3 (c2'). For `l' <= q <= i + 1` let `B_q` be the set of level-q bonds `b` such that the order-q blocks
of both endpoints lie in `F`. Claim: every `b in B_q` is a row of `D_q`, and
`V_q(b)(x_{nu_q}) = (M^{q-l'} W)(b)`. For `q = l'` this is Step 2. Let it hold for some `q <= i`, and let
`b in B_{q+1}`. Its ends are in `F subset K_q subset A^{q+1}_{q+1}`, and in `O_{q+1}`, so not in
`A^q_{q+1} = X minus O_{q+1}` nor in `A^q_{q+2}`: `b` is a new row of the stage of level `q`. By Lemma 2.1 (a),
`V_{q+1}(b)(x_{nu_{q+1}}) = M(V_q(x_{nu_q}))(b)`. The average reads the level-q bonds of the double block of
`b`; these are in `B_q`. So `V_{q+1}(b)(x_{nu_{q+1}}) = (M^{q+1-l'} W)(b)`, and `b` is a row of `D_{q+1}`. The
four edges of `p` are in `B_{i+1}`. So `V(c)(x_{nu_{i+1}}) = (M^d W)(c)`. For `i = t - 1` the last step of the
induction is the last stage; Lemma 2.1 covers it.

Step 4 (allowance). `2.1 eps_{l'} = alpha' L^{-2d}`, `alpha' = 2.1 L^{2d} eps_{l'}`, and
`eps_{l'} <= sqrt(2) eps_{i+1}` (Lemma F1 of `i3-cert`, case `l < s`). `d <= i - k_0`. If `i <= t - 2`:
`d <= t - k_0 - 2`, so by (2.1) `L^d <= L^{-1} R_{k_0+1} <= 2^r R_{i+1}` (Lemma F2 of `i3-cert` with `l = i + 1`).
If `i = t - 1`: `L^d <= L^{t-k_0-1} = R_{k_0+1} <= 2^r L R_t`. So `alpha' <= 2.1 sqrt(2) 4^r R_{i+1}^2 eps_{i+1} <= 3 . 4^r e_{i+1}`,
respectively `3 . 4^r L^2 e_t`. `square`

Remarks. (1) This is Y 77651-77704, with the single footprint in the place of Y's tube; Y's range
`k_0 + 1 <= l <= q` contains `l = q`, which is finding 1. (2) The moment `nu_{l'}` is not later than `nu_i`;
it is not earlier than `nu_h`, since `l' > k_0 > h`. (3) (AV2) is applied once, on the lattice of level `l'`,
at depth `d` (Lemma 3.2 of `cov-x`).

## 6. The last stage, and the statement at every stage exit (X5, X6)

**Theorem 6.1 (COV-X\*).** Assume (D1), (D2), (D3\*), (D4), (D5), (D6), (FR), (T1), (T3) of `i3-cert`, (AV2).
Let X be a class component of level `t` with window from `h`, `h <= i <= t - 1`, and `p in Fr_i(X)` tested
at the exit `nu_{i+1}` of the stage of level `i`. Then `p` has a supplier in the sense of Definition 3.1
of `cov-x`, with (c1), (c2'), (c3') and `nu_{i+1}` in the place of `N`, at a moment `mu` with
`nu_h <= mu <= nu_i < nu_{i+1}`. Its defect at `x_{nu_{i+1}}` is at most `C_2'' e_{i+1}`,
`C_2'' = max(C_2, 6 . 4^r L^2)`.

*Proof.* Lemma 3.1, then Lemma 4.1, 4.2 or 5.1, and Lemma 3.2 of `cov-x`. In (Q1), (Q2) the allowance is
`psi eps_{i+1}` with `psi <= 3 sqrt(2) c_0 L^2 L_flat^{2e}`, `e = (i - k_0 - 1)_+ <= (i + 1 - k_0)_+`; this is
(5.1) of `i3-cert` at the level `i + 1`, and Lemma 2b there gives `2 psi eps_{i+1} <= C_2 e_{i+1}` (under (LF);
without (LF), with the constant of its 5.3). In (Q3) the defect is at most `6 . 4^r L^2 e_{i+1}`. `square`

**(X5) The last stage `i = t - 1`.** `Fr_{t-1}(X)`: the level-t plaquettes with corners in `O_t` and a
corner in `K_{t-1} = O_t minus Z''_t`. Since `t - 1 >= k_0 + 1`, the regions are `E^{t-1}_0`,
`E^{t-1}_{l'}` (`k_0 < l' <= t - 1`), all inside `O_t`, which is two level-t cells inside X; "every earlier guard
reads only `X cap Omega_m^c` ... The artificial bare rim occurs only in the final guard" (Y 64227-64231).
The guard is T9 of `cov-x`, `chi_t^{(t-1-h)}` at `nu_{t-1}`, with the background `U^{(t-1-h)}_{t,X}`.

- What (m2) writes: finding 5. The new rows are the level-t bonds with both ends in `O_t` and an end in
  `K_{t-1}`; all four edges of a (Q2) or (Q3) plaquette are such rows; a (Q1) plaquette also has completed
  edges in `Z''_t minus Z''_{t-1}`, with the same averages.
- Suppliers: (Q1) at the last prepared face, in `E^{t-1}_0` (Lemma 4.1); (Q2) in one region, with the factor
  3 in `O_t minus O_{t-1}` (Lemma 4.2); (Q3) at a wall `dO_{l'}`, `k_0 < l' <= t - 1` (Lemma 5.1).
- Carrying. The supplier is at a moment `<= nu_{t-1}`, and (c2') is proved at `x_{nu_t}`. After `nu_t`:
  a stop at the extension test changes no row and no entry ((F-stop) of `cov-global`), so `p` is carried
  over with the same loop. At the main step a plaquette of `Fr_{t-1}(X)` with no edge in the box is tested
  before and after, with a conjugate loop ((F-main); Lemma 4.1 (d) of `cov-global`). Lemma 5.2 of
  `cov-global` (carrying) then keeps the supplier with the same allowance. A plaquette with an edge in the
  box is fresh at the main step; its supplier is (R-last) or (R-core) of `cov-global`, not this row.
  The carrying rests on (F-stop), (F-main), which are read statements of `cov-global` (row 638).
- Comparison with Y 76685-76687 ("If a determining plaquette is deleted, the newly made layer uses its own
  regularity guard") and Y 77817-77825 ("Within the covered part use `chi_i^{(n+1)}` ... On footprints
  covered by the literal clauses, the prospective guard gives the curvature bounds used in the block
  averages. At a prepared or original wall use the coarse holonomy bound from the preceding promotion
  calculation"). Y gives two suppliers for a new plaquette whose footprint a literal clause of the
  prospective guard covers: that guard (at the exit), and the preceding guard (Y 77647-77651). At the walls
  Y gives only the preceding calculation. Theorem 6.1 uses the preceding one everywhere; the "own
  regularity guard" of the new layer is a second supplier where its clauses contain the footprint, and it
  is not needed. For the last stage the prospective guard is the final one, which has the bare rim; the
  supplier here does not read it.

**Theorem 6.2 (COV-X at every stage exit; proved from Theorem 6.1).** Same hypotheses. Let
`h <= i <= t - 1` and let `p` be a tested plaquette of level `l >= h + 1` of `D_{i+1} = D(x_{nu_{i+1}})` with
`F(p) subset X`. Then exactly one of two holds.

- (a) All corners of `p` are in `O_l`. Then `l <= i + 1`, `p in Fr_{l-1}(X)`, `p` is tested at `nu_l`, and
  `p` has the supplier of Theorem 6.1 for the stage of level `l - 1`, at a moment `<= nu_{l-1}`, with (c2') at
  `x_{nu_{i+1}}` and defect at most `C_2'' e_l`.
- (b) A corner of `p` is in `X minus O_l = Omega_l cap X`. Then `p` is not fresh at any stage of X.

*Proof.* (a) `p` has a corner in `A^{i+1}_l`. If `l > i + 1` this set is `X minus O_l`, which contains no
corner; so `l <= i + 1`, and the corner is in `(X minus Z''_l) cap O_l = K_{l-1}`: `p in Fr_{l-1}(X)`. By
Corollary 2.2, `p` is tested in `D_l` with the same four edge values as in `D_{i+1}`. Theorem 6.1 at the
stage of level `l - 1` gives the supplier with (c2') at `x_{nu_l}`, hence at `x_{nu_{i+1}}`.
(b) The fresh plaquettes of the stage of level `q` are in `Fr_q(X)` and have level `q + 1` and all corners
in `O_{q+1}` (Lemma 4.1 (b) of `cov-global`). `square`

In case (b), and for the level `l = h`, the plaquette is fresh only at step `l` (or its supplier is the
core test T5), and its certificate in `cov-global` is (S-ord) (Lemma 4.2 there, given (R-ord)); Lemma 6.5
of `cov-x` gives the direct bound `2.1 eps_l` at the levels `h` and `t`.

**(X6) Theorem 6.1 of `cov-x` (the exit `nu_{t-1} = N` of the stage of level `t - 2`), case by case.**

| Case of `cov-x` | From the uniform lemma | Status of the supplier of `cov-x` |
|---|---|---|
| P4 (`h < l <= j`, a corner in `Z''_l`) | yes: (Q1) at the stage of level `l - 1` | the same supplier (Lemma 6.3 there) |
| P3, `h < l < j`, all corners in `O_l` | yes: (Q2) or (Q3) at the stage of level `l - 1`, moment `<= nu_{l-1}` | T9 at `N` (Lemma 6.2) is a second supplier |
| P3, a corner in `X minus O_l`; P3 with `l = h` | no; case (b), (S-ord) at step `l`, or T5 | T9 at `N` is a second supplier |
| P5a, `F(p) subset E^j_0` or `E^j_{l'}` with `l' <= j - 1` | yes: all corners in `O_j`, so (Q2) at the stage of level `j - 1` (`E^j_0 subset E^{j-1}_0`; for `j - 1 = k_0` the region is `O_j minus O_{j-1}`) | T9 at `N` is a second supplier |
| P5a, `F(p) subset E^j_j = O_m minus O_j` | no; case (b), (S-ord) at step `j` | T9 at `N` is a second supplier |
| P5b at `dO_{l'}`, `l' <= j - 1` | yes: (Q3) at the stage of level `j - 1`; the same supplier | Lemma 6.4 there |
| P5b at `dO_j` (depth 0) | no; case (b) | the level-j density test; it is (S-ord) read at `nu_j` |
| P2, P6 | no; not fresh at a stage | density tests T5, T4 |

So every instance of Theorem 6.1 of `cov-x` that concerns a plaquette made new by a stage follows from
the uniform lemma, with a supplier at the entrance of that stage or earlier. For the datum `D(x_N)` the
guard T9 at `N` is the first supplier of no plaquette. It is the supplier of the plaquettes of
`Fr_{t-1}(X)` in positions (Q1), (Q2), at the exit `nu_t`.

## 7. Constants (X7)

| Position | Allowance `alpha` | Defect | Uses |
|---|---|---|---|
| (Q1) | `sqrt(2) c_0 L^2 L_flat^{2(i-k_0-1)_+} eps_{i+1}` | `2 alpha <= C_2 e_{i+1}` | (D4), F1, Lemma 2b |
| (Q2) | `3 sqrt(2) c_0 L^2 L_flat^{2(i-k_0-1)_+} eps_{i+1}` | `2 alpha <= C_2 e_{i+1}` | (D4), F1, Lemma 2b |
| (Q3), `i <= t - 2` | `3 . 4^r e_{i+1}` | `6 . 4^r e_{i+1}` | (I4), F1, F2, (2.1) |
| (Q3), `i = t - 1` | `3 . 4^r L^2 e_t` | `6 . 4^r L^2 e_t` | the same |

`C_2 = 2^{r+1} L L_flat^2 A_L` (Lemma 2b of `i3-cert`, under (LF)); `C_2'' := max(C_2, 6 . 4^r L^2)`. In (Q1),
(Q2) the factor is `psi_{i+1} <= 3 sqrt(2) c_0 L^2 L_flat^{2e}` with `e = (i - k_0 - 1)_+`, inside (5.1) of
`i3-cert`. In (Q3) `psi_{i+1}` is of order `R_{i+1}^2`: no spare factor `1/R`, and neither (LF) nor `L_flat`
is used (finding 3 of `cov-x`). Ceiling on `gamma`: `C_2'' ebar(gamma) <= alpha_L` (Lemma F4 of `i3-cert`),
with `alpha_L` of (AV2) on the bare lattice and on a coarse lattice (the same map in its own units).

## 8. What is proved, what is read, what stays open

Proved here, from (D1), (D2), (D3\*), (D4), (D5), (D6): Lemma 2.1, Corollary 2.2, (X1), Lemma 3.1 (the
partition), Lemmas 4.0, 4.1, 4.2, 5.1, Theorems 6.1, 6.2, the table (X6).

Read, not rebuilt:

1. (D1), (D2), (D3\*) at every stage, the last one included. Row 638 (`cov-frames`) owns (F-stage), which
   contains them. If the last stage did not write `V_t = M(V_{t-1})` on the new rows by a retained delta,
   Theorem 6.1 would fail at `i = t - 1`; Y states it (Y 64097-64100, 72258-72260).
2. (D4): the clause regions and thresholds of each guard `chi_t^{(i-h)}`, `h <= i <= t - 1`. The proofs
   place each footprint in one region of the finest reading of the list, so they hold under the merged
   readings.
3. (D5): the background of the guard has the rows of all levels of the sequence `A^i`.
4. (D6): (I4_l) and (DENS) at the levels `k_0 < l' <= t - 1`, at `nu_{l'}`, reading the rows of `Lay^{l'}_{l'}`
   (Y 64699-64716). Lemma 5.1 depends on it.
5. (AV2) on the bare lattice and on a coarse lattice; Lemmas F1, F2, 2b of `i3-cert`; the alignment fact
   and (B1) to (B3) of `cov-x` 2.1.
6. (F-stop), (F-main) and Lemma 5.2 of `cov-global`, only for the carrying after `nu_t` in (X5).

Open: nothing inside (COV-X*) given the read statements. Not done: a check by another model; the read
statements as statements on the actual operation (rows 633, 636, 638).

For the lead (I edited no other file):

1. In `library/cov-global.md` 4.3 the two rows marked **gap** are closed by Theorem 6.1; the bound in the
   table of its Theorem 5.1 (second line) is `C_2'' e_l` with `C_2'' = max(C_2, 6 . 4^r L^2)`, not `C_2'`.
   The moment is in `[nu_h, nu_{l-1}]`.
2. For row 634: where `cov-x` section 8 item 3 says `C_2' = max(C_2, 6 . 4^r)` and `psi_j <= 3 . 4^r R_j^2`,
   the top level needs `psi_t <= 3 . 4^r L^2 R_t^2` (new level-t plaquettes at an original wall).
3. The walls of (U2) are `k_0 < l' <= i`, not `<= i + 1` (finding 1); registry row COV can record that the
   seventh kind occurs only at the stages `i >= k_0 + 1`.

RESULT: (COV-X*) proved for every stage h <= i <= t-1, the last included (Theorem 6.1, stop condition (i)): each plaquette of Fr_i(X) is in exactly one of three positions, and has a supplier at the entrance of the stage or earlier — the guard before the promotion for a footprint at the prepared face or in one exterior region, the level-l' density tests with exact averages for a footprint astride an original wall dO_{l'}, k_0 < l' <= i (only for i >= k_0+1; the wall dO_{i+1} does not occur) — with defect at most max(C_2, 6 . 4^r L^2) e_{i+1} (one more factor L^2 than cov-x, at the last stage); Theorem 6.2 gives (COV-X) at every stage exit. Open: the definitions (D1) to (D6) of cov-x are read from Y and not rebuilt, here used also at the last stage, and the file is not checked by another model.
