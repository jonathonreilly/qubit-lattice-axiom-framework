lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T17:18Z

# Check of `library/cov-xstar.md` (row 639)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit 0cd1bd5ea. This is one line-by-line
read by a model that did not write the file (it was written by Claude Fable 5.2 medium). It is not an audit.
Source: Sussman and Alpoge, `YM4_1400.tex` at 2bc0658f91d2 (their text names Claude and Codex as authors),
fetched into my own scratch folder; `Y n` is line n. No numeric job was run.

## Verdict

**(COV-X\*) HOLDS, with repairs to the wording only, given the read inputs (D1) to (D6), (D3\*) and (AV2).**
First failing step: none. No item FAILS. Lemma 3.1, Lemmas 4.0, 4.1, 4.2, 5.1, Theorems 6.1, 6.2 and the
table (X6) are correct as implications. Findings 1 to 5 of the file are confirmed. Five repairs (R1 to R5)
are given as text below; none changes a statement, a constant or a moment.

| Item | Verdict |
|---|---|
| (1) Lemma 3.1, edge cases | HOLDS |
| (2) Finding 1 | HOLDS WITH REPAIR (R1, wording: "astride", not "meet") |
| (3) Lemma 4.0 | HOLDS |
| (4) Lemma 4.1 at `l = t` | HOLDS |
| (5) Lemma 4.2, thresholds, factor 3 | HOLDS |
| (6) Lemma 5.1 | HOLDS WITH REPAIR (R2: the source of 2.1). The factor `L^2` at `i = t - 1` is needed in the worst case |
| (7) Theorem 6.1 | HOLDS WITH REPAIR (R3: name (LF), or the 5.3 constant). (Q3) is outside (5.1), as the file says |
| (8) Theorem 6.2, table (X6) | HOLDS |
| (9) The last stage against Y | HOLDS. Y states the one-step average on the new rows at the last stage |
| (10) Quoted Y passages | HOLDS (thirteen compared; all are faithful; line offsets of at most 1) |
| (11) Carrying after `nu_t` | HOLDS WITH REPAIR (R4, R5): the weak form is enough; the main-step clause should follow row 638 |

## Repo search

`grep -n -i "cov-xstar\|COV-X\*"` in `library/open-core.md` and `library/open-registry.md`: only registry
row COV. FINISH rows 633, 635, 636, 638 are near this check. None of them checks `cov-xstar.md`. This
checkout has only `origin/claude/ym4d-hard-route`. Present at this commit: `cov-x-check.md` (row 633;
RESULT: (D1) to (D6) are fair readings of Y), `cov-global-check.md` (row 636) and `cov-frames.md` (row 638).
I do not check those files; I name them where they touch an item.

## Items

### (1) Lemma 3.1: HOLDS

What I checked, for general `i` and at each edge case.

- `F(p) subset O_{i+1}`: `O_{i+1} = H_{i+1}^{[8 a_{i+1}]}` is a union of level-(i+1) cells, so it is a union of
  aligned level-(i+1) blocks. Lemma G (b) of `cov-x` applies.
- (Q1): the block of the corner in `Z''_{i+1}` lies in `F(p)` and in `Z''_{i+1}`. The corner in `K_i` lies
  outside it. Lemma G (c) applies.
- Otherwise `F(p) cap Z''_{i+1}` is empty: `Z''_{i+1}` is a union of aligned level-(i+1) blocks (`H_{i+1}` grid
  for `i + 1 <= k_0`; `M`-cubes of level `i + 1` for `i + 1 > k_0`, Y 63806-63809). So `F(p) subset K_i`.
- `i <= k_0`: `O_i subset G_i subset H_{i+1} subset Z''_{i+1}`. For `i = k_0`: `G_{k_0} subset H subset H^{[u_t]} = Z''_{k_0+1}`.
  So `K_i subset O_{i+1} minus O_i`, the region of (D4) for `i = h` and the second region for `h < i <= k_0`.
- `i >= k_0 + 1`: `O_{k_0+1} minus Z''_{i+1}`, `E^i_{k_0+1}`, ..., `E^i_i` partition `K_i`. The nesting
  `O_{k_0+1} subset ... subset O_{i+1}` is (B3) for `l' <= i <= t - 1`. A footprint in no single piece meets
  two pieces, and so it is astride some `dO_{l'}`, `k_0 < l' <= i`.
- Uniqueness of `l'`. `F(p)` meets `O_{l'}` and `O_{l''}^c`, so its diameter (below `2 L^{i+1}`) is at least
  `dist(O_{l'}, O_{l''}^c) >= 2 a_{l'} + 8 a_{l'+1}` by (B3). This exceeds `2 L^{i+1}` because
  `a_{l'+1} >= L u_t`.
- The second half of (2.1), `a_q >= L u_t` for `q >= k_0 + 2`, is Y's sentence (Y 63776-63778). It follows
  from Y's definition of `k_0 + 1` as the *last* index with `a = u_t`. The values `a_q = M R_q L^q` lie in
  `M L^Z`. The ratio `a_{q+1}/a_q = L R_{q+1}/R_q` is at most `L`, since `R` is non-increasing. Also
  `a_t >= u_t`. If some `a_q < u_t` with `q > k_0 + 1`, then the first later index with `a >= u_t` has
  `a = u_t`, which contradicts "last". So `a_q > u_t`, that is `a_q >= L u_t`.

Edge cases.

- `i = h`: (Q1) gives `N subset O_{h+1} minus O_h` (Lemma 6.3 of `cov-x`, case `l = h + 1 <= k_0`, since `h < k_0`).
  (Q2) gives `R = O_{h+1} minus O_h = Lay^h_h`. (Q3) does not occur.
- `i = k_0`: (Q1) gives `N subset H^{[u_t + 2L^{k_0+1}]} minus H^{[u_t - 2L^{k_0+1}]} subset O_{k_0+1} minus O_{k_0}`.
  (Q2) gives `K_{k_0} subset O_{k_0+1} minus O_{k_0}`. (Q3) does not occur.
- `i = k_0 + 1`: (Q1) gives `N subset H^{[8u_t]} minus H^{[u_t]} = E^{k_0+1}_0`. This needs
  `w_{k_0+1} - w_{k_0+2} >= u_{k_0+2} >= 2L^{k_0+2}`, which is (B2). (Q3) occurs only at `dO_{k_0+1}`, with `d = 1`.
- `i = t - 1`: see item (4). (Q2) has the factor 3 only on `E^{t-1}_{t-1} = O_t minus O_{t-1}`.
- `t - 1 = k_0 + 1`: `w_{t-1} = 2u_t` and `Z''_{t-1} = H^{[u_t]}`. (Q1) gives
  `N subset H^{[3u_t + 2L^t]} minus H^{[3u_t - 2L^t]} subset H^{[8u_t]} minus H^{[u_t]} = E^{t-1}_0`. The only wall is
  `dO_{k_0+1} = dO_{t-1}`, with `d = 1`. The last-stage branch of Step 4 of Lemma 5.1 then gives `L^d = L = R_{k_0+1} <= 2^r L R_t`.

The claim "`F(p)` does not meet `Z''_i`" in (Q1) uses Step 1 of Lemma 4.1. That step is a box computation
that does not use Lemma 3.1, so there is no circularity.

### (2) Finding 1: HOLDS WITH REPAIR (R1)

The definition of `Fr_i(X)` (Lemma 4.1 (b) of `cov-global`) puts all four corners in `O_{i+1}`. The alignment
fact for `O_{i+1}` at level `i + 1` then gives `F(p) subset O_{i+1}`. So no plaquette of `Fr_i(X)` is
*astride* `dO_{i+1}`. The walls of (Q3) are `k_0 < l' <= i`, and `d >= 1`.

A level-(i+1) plaquette astride `dO_{i+1}` has a corner in `X minus O_{i+1}`, which is the old member of
index `i + 1`. The level-(i+1) case of Lemma 4.1 (b) of `cov-global` carries it over with the same loop.
Y treats the same plaquettes with "the original level-`q` density test" (Y 77571-77574, early seam) and
"When `q = l` the bound follows directly from the original positive density test" (Y 77700-77702).

**R1 (text for the file).** Finding 1, second sentence, and the last sentence of Lemma 3.1: replace "it
does not meet `dO_{i+1}`" and "in no case does `F(p)` meet `dO_{i+1}`" with "it is not astride `dO_{i+1}`
(it lies in `O_{i+1}`; it can touch the face from inside, and it is then inside one region of (X1))".
Reason: `F(p)` can contain sites of `O_{i+1}` next to its face. The literal "does not meet" is false if
`dO_{i+1}` is read as the set of boundary sites. Nothing in the proofs uses the literal form.

### (3) Lemma 4.0: HOLDS

- (c1). Definition 3.1 asks for `eps(U; F(p)) <= alpha L^{-2(i+1)}` with `F(p)` inside one clause region. Every
  bare plaquette with corners in `F(p)` has its corners in `R`, so (D4) gives `norm(dU - 1) < t_R`. The
  conversion `abs(F) <= c_0 norm(dU - 1)` gives `c_0 t_R = alpha L^{-2(i+1)}`.
- (c3'). `U` is by definition the background of the guard at `x_{nu_i}`. For (4.1): a level-i bond with both
  ends in `F(p) subset Lay^i_i = A^i_i minus A^i_{i+1}` touches `A^i_i` and has no end in `A^i_{i+1}`, so it is
  in `Gamma_i`. (D5) applies because `F(p) subset O_t` is `2 a_t` from `X^c`.
- (c2'). `p` is tested in `D'_i`: it has a corner in `K_i subset A'_{i+1}`, and its corners are in `O_{i+1}`.
  A row edge has its ends in `O_{i+1}`, so it does not touch `A^i_{i+1} = X minus O_{i+1}`. It is therefore
  in `Gamma'_{i+1} minus Gamma_{i+1}`, a new row, and (m2) gives its value. A completed edge is read on rows of
  `Gamma'_i`. These rows have no end in `K_i`, so (m1) and (m3) leave them unchanged (Lemma 2.1 (a)).
- **What each average reads (the row's question).** The one-step average on a level-(i+1) edge `c` reads the
  level-i bonds of the two order-(i+1) blocks of the ends of `c` (Y 72256-72259: "The two order-`(j+1)` blocks
  of each such row ... all their level-`j` bonds are old determining rows"). The ends of `c` are corners of
  `p`, so these two blocks are among the four blocks whose union is `F(p)`. Every bond read therefore has both
  ends in `F(p)`. This holds for a row edge and for a completed edge, since the double block is the same set.
  By (4.1) every such bond is a row of `D_i` with `V_i = M^i U`. So the average is defined from the datum, and
  `V(c) = M(M^i U)(c) = (M^{i+1} U)(c)`.
- One point the file leaves implicit. The rows of the double block of a completed edge must avoid `Z''_i`.
  The alignment fact does not give this, because `Z''_i` (for `i > k_0`) is a union of level-i `M`-cubes,
  which need not be a union of level-(i+1) blocks. It follows from `F(p) subset R subset Lay^i_i`, which
  excludes `Z''_i`. The proof uses exactly this inclusion, so the step holds.
- The collar gauge (m1) is one at the level-(i+1) sites. The average is covariant at its block centres, so
  the value of the new row does not depend on whether (m1) acts before or after (m2). (D2) states this as
  "the coarse row remains fixed".

### (4) Lemma 4.1 at `l = t`: HOLDS

- `Z''_t = H^{[3u_t - w_t]} = H^{[3u_t]}`, since `w_t = 0`.
- `N_{2L^t}(dZ''_t) = H^{[3u_t + 2L^t]} minus H^{[3u_t - 2L^t]}`.
- `3u_t + 2L^t <= 8u_t`, because `2L^t <= u_t` when `M >= 2`. So `N subset H^{[8u_t]} = O_{k_0+1}`
  (`a_{k_0+1} = u_t`).
- (B2) at `i = t` (valid since `t >= k_0 + 2`) gives `w_{t-1} - w_t >= u_t`. In fact `w_{t-1} = u_t`, or
  `2u_t` when `t - 1 = k_0 + 1`. So `w_{t-1} >= 2L^t`, hence `3u_t - w_{t-1} <= 3u_t - 2L^t`. That is,
  `Z''_{t-1} = H^{[3u_t - w_{t-1}]} subset H^{[3u_t - 2L^t]}`, and `N cap Z''_{t-1}` is empty.
- So `N subset E^{t-1}_0 = O_{k_0+1} minus Z''_{t-1}`.
- `E^{t-1}_0 subset O_t minus Z''_{t-1} = Lay^{t-1}_{t-1}`, because `O_{k_0+1} subset O_t` by (B3) with
  `l' <= t - 1`.
- Y's own region for this case is `X cap (Omega_{k_0+1}^c minus Z''_j)` (Y 77612-77621). Y says this
  "also applies to the last prepared face before the final collar integration" (Y 77643-77645).
- The factor `c` is 1 on `E^{t-1}_0`. Y 63876 puts `c_l = 3` only "adjacent to `Omega_k` at the last
  stage", that is on `O_t minus O_{t-1}`.
- `eps_i <= sqrt(2) eps_{i+1}`: the case `l < s` of the proof of F1 gives `eps_l/eps_s <= sqrt(2)` for any
  `l < s`, using (T1) only.

### (5) Lemma 4.2: HOLDS

The thresholds agree with (D4) and with Y 63876. Y 63876 gives the shell factor
`(1 - beta_s(1 - 2^{-(j-i+1)})) L_flat^{2(i-k_sharp-1)_+}`. Off the shells it gives
`(1 - beta_s/2) c_l L_flat^{2e} eps_j eta_j^2` with `eta_j = L^{-j}` (Y 593). Here `e = 0` for `j <= k_sharp`.
For `j > k_sharp`, `e = (j - l - 1)_+` on `Omega_l minus Omega_{l+1}` (`k_sharp < l <= j`), and
`e = j - k_sharp - 1` between the shells and `Omega_{k_sharp+1}`. `k_sharp` is `k_0`, by the same identity
`M R_{k_sharp+1} L^{k_sharp+1-k} = M`. Inside X these are `E^i_{l'}` and `E^i_0`. For `i <= k_0` the split
into `O_i minus Z''_i` and `O_{i+1} minus O_i` is Y 64224-64227 with `i_0 = i - 1`.

The bound `t_R <= 3 F_i eps_i L^{-2i}` holds in every region:

- `(i - l' - 1)_+ <= i - k_0 - 1` for `l' >= k_0 + 1` and `i >= k_0 + 1`;
- `F_i >= 1`;
- `c_{l'} = 3` only at `i = t - 1`, `l' = t - 1`.

So `alpha = c_0 L^{2(i+1)} t_R <= 3 sqrt(2) c_0 L^2 F_i eps_{i+1}`. The statement that in (Q2) all four
edges are new rows is correct. No corner is in `Z''_{i+1}`, so no edge has both ends in
`Lay'_i = Z''_{i+1} minus Z''_i`.

### (6) Lemma 5.1: HOLDS WITH REPAIR (R2)

**Step 1.**

- (i): (B3) gives `O_{l'+1}^{[-a_{l'+1}]} supset O_{l'}^{[2a_{l'} + 7a_{l'+1}]}`. The erosion of a box
  enlargement is a box, so the inclusion survives the erosion. Also `2L^{i+1} <= 2L^t < 7 L u_t <= 7 a_{l'+1}`.
- (ii): `4 a_{l'} >= 4 u_t >= 2L^{i+1}`.
- (iii): `Z''_q subset H^{[3u_t]} = O_{k_0+1}^{[-5u_t]} subset O_{l'}^{[-5u_t]}`, and `5u_t > 2L^{i+1}`.
- (iv): follows from the nesting and from (iii) applied to `Z''_q` and `Z''_{q+1}` (`q + 1 <= i + 1 <= t`).

**Step 2.**

- The wording "a union of level-l' cells" is loose. What is used is true: every site of `N` lies in a
  level-l' cell inside the (DENS) region.
- Proof. Take `x in N`. If `x in O_{l'}`, its depth is below `2L^{i+1} <= a_{l'}`, so its cell is a boundary
  cell of `O_{l'}` (`O_{l'}` is a union of level-l' cells). That cell misses `O_{l'}^{[-4a_{l'}]}`.
- If `x notin O_{l'}`, its cell lies in `O_{l'}^{[a_{l'}]} subset O_{l'+1}^{[-a_{l'+1}]}` by (i).
- Test cubes partition the cell ((D6)), so the cube of `x` lies in the region.
- The (DENS) region is Y's `(Omega_j^{~4} minus Omega_q^~) cap X` (Y 64699-64716, for every `h < j < m`).
  Y reads it at "that layer's actual determining rows at the old target", that is `D_{l'}` at `nu_{l'}`.
  `cov-x-check.md` accepts this reading.

**The constant 2.1.**

- Y does not state 2.1. Y 134117-134118 states `abs(dV_k - 1) <= 2 eps_k` "on the one-step footprint" for a
  plaquette with a corner in a positive density cube, in the norm.
- Lemma 5.1 needs the angle form `abs(F_q(W))`. With the operator norm of i3-cert 2.3,
  `abs(F) = 2 arcsin(norm(dW - 1)/2) <= 2 arcsin(eps_l)`.
- `arcsin` is convex on `[0, 1]` with `arcsin(1/2) = pi/6`, so `arcsin(x) <= (pi/3) x` on `[0, 1/2]`.
  Hence `abs(F) <= (2 pi/3) eps_l < 2.1 eps_l` once `eps_l <= 1/2`, which is a ceiling on `gamma`.
- The same number comes from (AV2) with `alpha = (pi/3) eps_l` (`rim-scale-check.md`, row (I4)).
- The allowance does not change. Note: the crude conversion `c_0 = pi/2` would give `pi eps_l`. Then
  `pi sqrt(2) = 4.44 > 3`, and the constant `3 . 4^r` would have to be `5 . 4^r`. So the sharp conversion is
  the one to cite.

**R2 (text for the file).** In Step 2 of Lemma 5.1, after "(I4_{l'})", add: "(Y 134117-134118 gives
`abs(dV_{l'} - 1) <= 2 eps_{l'}`; with the norm of i3-cert 2.3, `abs(F) = 2 arcsin(norm/2) <= 2 arcsin(eps_{l'}) <= (2 pi/3) eps_{l'} < 2.1 eps_{l'}`
for `eps_{l'} <= 1/2`)". Also replace "a union of level-l' cells" with "and every site of it lies in a
level-l' cell inside `O_{l'+1}^{[-a_{l'+1}]} minus O_{l'}^{[-4a_{l'}]}`".

**Step 3.**

- `b in B_{q+1}` has its ends in `K_q` and in `O_{q+1} subset O_{q+2}`. So `b` touches `A'_{q+1}`, has no end
  in `A'_{q+2} = X minus O_{q+2}`, and does not touch `A^q_{q+1}`. It is in `Gamma'_{q+1} minus Gamma_{q+1}`.
- The bonds read by `M` on `b` lie in the two order-(q+1) blocks of the ends of `b`. These blocks are inside
  `F` and are unions of aligned order-q blocks, so the bonds are in `B_q`. The induction is correct.
- At `q + 1 = t` (the last stage) there is no member of index `t + 1`, and Lemma 2.1 (a) applies as stated.
- The four edges of `p` are in `B_{i+1}`.

**Step 4.**

- `d <= i - k_0`.
- For `i <= t - 2`: `L^d <= L^{t-k_0-2} = L^{-1} R_{k_0+1} <= 2^r R_{i+1}` by F2 with `l = i + 1`. Then
  `2.1 sqrt(2) 4^r = 2.97 . 4^r <= 3 . 4^r`.
- For `i = t - 1`: `L^d <= R_{k_0+1} <= 2^r L R_t`.
- **The factor `L^2` is needed in the worst case.** Take `i = t - 1` and `l' = k_0 + 1`. Such a plaquette
  exists: `dO_{k_0+1} = dH^{[8u_t]}` lies on the level-t block grid and is `5u_t` outside `Z''_t`. Then
  `L^{2d} eps_{l'} = R_{k_0+1}^2 eps_{k_0+1}`.
- (FR) does not exclude `R_t = R_{k_0+1}/L`. `R` takes values in powers of `L`, and the condition
  `mu_t >= mu_{k_0+1}/2` of the proof of F2 allows one step down. In that case the bound is
  `2.1 sqrt(2) L^2 R_t^2 eps_t`. No constant without `L^2` bounds it by a multiple of `e_t`.
- The factor is a constant fixed with `L`. Y's own `C'` in `C L^{2(q-l)} eps_l <= C' R_q^2 eps_q`
  (Y 77690-77692) contains it.

### (7) Theorem 6.1: HOLDS WITH REPAIR (R3)

- **(Q1), (Q2).** `psi_{i+1} = alpha/eps_{i+1} <= 3 sqrt(2) c_0 L^2 L_flat^{2e}` with `e = (i - k_0 - 1)_+`.
  This is inside (5.1) of i3-cert at level `i + 1`: `A_L >= 3 sqrt(2) c_0 L^2`, and `e <= (i + 1 - k_0)_+`.
  Lemma 2b, through F3 with `0 <= e <= l - k_0` and `l = i + 1 <= t`, gives `2 psi eps_{i+1} <= C_2 e_{i+1}`.
- **(Q3).** `psi_{i+1}` is `3 . 4^r R_{i+1}^2` (or `3 . 4^r L^2 R_t^2`), which is **not** inside (5.1). The
  file says so (section 7) and bounds the defect directly by `2 alpha <= 6 . 4^r L^2 e_{i+1}`, without
  Lemma 2b. So the bound `C_2'' e_{i+1}` is correct.
- What is lost for (Q3) is the spare factor `1/R` of Lemma 2b. Any consumer that reads (5.1) itself, rather
  than `C e_l`, must list (Q3) as the separate kind (K-wall). This is row 634 item (a).
- The moment: `mu = nu_i` in (Q1) and (Q2), and `mu = nu_{l'}` with `h < k_0 < l' <= i` in (Q3). So
  `nu_h <= mu <= nu_i`.
- The ceiling `C_2'' ebar(gamma) <= alpha_L` in section 7 covers every allowance, since `alpha <= C_2'' e/2`.
  This is the same ceiling as repair (d2) of `cov-x-check.md`, with `C_2''`.

**R3 (text for the file).** In the hypotheses of Theorem 6.1, after "(T1), (T3) of `i3-cert`", add "(LF)
(or, without (LF), read `C_2` as the constant `2 . 4^r L^2 L_flat^2 A_L` of i3-cert 5.3)". The proof uses
Lemma 2b, which assumes (LF). The constant is also used without (LF), but the statement does not say so.

### (8) Theorem 6.2 and the table (X6): HOLDS

**Theorem 6.2 (a).**

- If `l > i + 1`, then `A^{i+1}_l = X minus O_l`, which contains no corner. So `l <= i + 1`.
- The tested corner lies in `A^{i+1}_l cap O_l = (X minus Z''_l) cap O_l = K_{l-1}`. So `p in Fr_{l-1}(X)`.
- Corollary 2.2 runs Lemma 2.1 (b) at the stages `i, i - 1, ..., l`, each with `l <= i'`. The direction
  "tested in `D_{i'+1}` implies tested in `D_{i'}`, with equal values" is the one used. So (c2') at `x_{nu_l}`
  holds also at `x_{nu_{i+1}}`.

**Theorem 6.2 (b).** A stage of level `q` makes fresh only level-(q+1) plaquettes with all corners in `O_{q+1}`.
A level-l plaquette with a corner in `X minus O_l` is therefore never fresh at a stage. The two cases cover
everything: `F(p) subset X` puts the corners in X.

(One small point that needs no repair: the theorem concerns levels `l <= t`. Inside X, (D1) has no member of
index above `t`.)

**The table (X6).** I checked each line against Lemma P of `cov-x`.

- P4: by (B1), `N_{2L^l}(dZ''_l) subset O_l`, with margin `5 a_l` or `5 u_t`. So all corners are in `O_l`,
  and the tested corner is in `K_{l-1}`. This is (Q1) at stage `l - 1`.
- P3 with all corners in `O_l`: this is (Q2) or (Q3) at stage `l - 1` (no corner in `Z''_l`).
- P5a in `E^j_0` or `E^j_{l'}` (`l' <= j - 1`): these lie in `O_j`.
  - If `j - 1 >= k_0 + 1`: `E^j_0 subset E^{j-1}_0` because `Z''_{j-1} subset Z''_j`, and `E^j_{l'} = E^{j-1}_{l'}`.
    This is (Q2).
  - If `j - 1 = k_0`: `E^j_0 = O_{k_0+1} minus Z''_{k_0+1} subset O_{k_0+1} minus O_{k_0}`. This is (Q2).
- P5a in `E^j_j` and P5b at `dO_j`: a corner lies outside `O_j`, so this is case (b).
- P5b at `dO_{l'}`, `l' <= j - 1`: `F(p) subset O_{l'}^{[2L^j]} subset O_j`. This is (Q3) at stage `j - 1`,
  with the same `d = j - l'` and the same tests as Lemma 6.4 of `cov-x`.
- P2 (`l = h`) and P6 (a corner in `X minus O_t`) are never fresh at a stage.

The line "the level-j density test; it is (S-ord) read at `nu_j`" names one test read at two moments: the
original step-j test, still carried at `nu_j` (Y 77657-77658: "Use the density test at that face before it is
removed"). This is consistent.

### (9) The last stage against Y: HOLDS

**(D1) at `i = t - 1`.**

- Y 72244-72250 covers "stage `n + 1`" for every `n`, with `j = m_flat + n`. The stages run over
  `j = k_flat, ..., k - 1` (Y 63836 (1)), so `n = N_m - 1` (the last stage) is included. "The only member of
  the sequence that changes is the one of index `j+1`, which grows ... to the prepared member."
- Y 64089-64092 states Lemma 2.1 (b) for the last stage: "Levels below `j` keep their rows. The determining
  set of level `j` loses rows. Its second-kind rows still use the unchanged layers `j-1,j`, so the remaining
  tested plaquettes have their old holonomies."
- The prepared member after the last stage is `X minus Z''_t`. The box `Lambda^pr` is `Z''_t` with one more
  layer of `M`-cubes, "and this layer is the shell of level `k`" (Y 63836 (1)). So level-t rows live on
  `Lambda^pr minus Z''_t`. This agrees with `A^t_t = X minus Z''_t` and with `K_{t-1} = O_t minus Z''_t`.

**(D2), (m2) at `i = t - 1`.**

- **Y states that the last stage writes the one-step average on the new rows.** For every stage:
  - "The two order-`(j+1)` blocks of each such row ... all their level-`j` bonds are old determining rows. The
    averaging delta on the new row is still present when the stage is tested";
  - "Its level-`(j+1)` averages on the new rows give the prospective datum by the retained delta"
    (Y 72256-72264).
- For the last stage by name, Y 64097-64101 says the blocks of a newly tested level-m plaquette lie "in the
  preceding member of level `j`, by the last prepared separation, and outside the old `Omega_m`. Here the
  fine plaquettes are formed from the old determining rows, and the exact one-step average gives the coarse
  bound."
- Y 77643-77645: "This also applies to the last prepared face before the final collar integration."
- So `V_t(c) = M(V_{t-1}(x_{nu_{t-1}}))(c)` on the new level-t rows is Y's statement.
- Y 64227-64231 confirms that the guard used here, at `nu_{t-1}`, is not the final guard. "Every earlier
  guard reads only `X cap Omega_m^c` ... The artificial bare rim occurs only in the final guard."

**(D3\*).** Y has no separate sentence for the last stage beyond Y 63836 (1) ("one value after another") and
Y 63849. (D3\*) stays a read statement. `cov-frames.md` Lemma 4.2 (b) (row 638) states a proof of it; I did
not check that proof.

### (10) The quoted Y passages: HOLDS

I compared thirteen quotes with Y. All are faithful, with line offsets of at most 1.

| Quote | In the file | In Y |
|---|---|---|
| "The other new footprints ... the preceding exterior guard reads the whole carrier" | 77574-77581 | 77575-77581 |
| "At a new level-`q` footprint away from the prepared face ... at most `F_j`" | 77647-77651 | 77647-77651 |
| "The deep exterior clause ... with `l <= j`" | 64223-64227 | 64224-64227 |
| "every earlier guard reads only ... final guard" | 64227-64231 | 64228-64231 |
| "the averaging blocks of a newly tested plaquette ... coarse bound" | 64097-64100 | 64097-64101 |
| "This also applies to the last prepared face ..." | 77644-77645 | 77643-77645 |
| (DENS) "The lower density cubes have bases in ... actual determining rows" | 64699-64716 | 64699-64716 |
| "When `q = l` the bound follows directly ..." | 77699-77701 | 77700-77702 |
| "If a determining plaquette is deleted, the newly made layer uses its own regularity guard" | 76685-76687 | 76685-76687 |
| "Within the covered part use `chi_i^{(n+1)}` ... preceding promotion calculation" | 77817-77825 | 77816-77826 |
| `c_l = 3` adjacent to `Omega_k` at the last stage | 63876 | 63876 |
| stages `j = k_flat, ..., k - 1`, "one value after another" | 63836 (1) | 63836 (1) |
| the tube argument, "`C L^{2(q-l)} eps_l <= C' R_q^2 eps_q`" | 77651-77704 | 77652-77704 |

The gloss `i_0 = min(j - 1, k_0)` in (X1) is the file's own reading. It is consistent with Y 63876 (`e`
between the shells and `Omega_{k_sharp+1}`).

### (11) The carrying after `nu_t` in (X5): HOLDS WITH REPAIR (R4, R5)

- **The weak form is enough.** Lemma 5.2 of `cov-global` (carrying) has one hypothesis: `p` is "carried
  over" in the sense of its Definition 4.0. That means `p` is tested before and after the move, and its loop
  after is a conjugate of its loop before. The proof uses only the conjugacy class ("the norm of `W - 1` is
  invariant under conjugation"). (c2') is then kept only up to conjugation, which is the form that Lemma 5.2
  and the defect bound use. Y says the same: "Any frame changes act at the block endpoints and preserve its
  plaquette defect" (Y 77685-77686).
- So (X5) needs two things from (F-stop): the tested status of `p` does not change, and its loop changes at
  most by conjugation. It does not need "no row and no entry changes".

**R4 (text for the file).** In (X5), "Carrying", replace "a stop at the extension test changes no row and no
entry ((F-stop) of `cov-global`), so `p` is carried over with the same loop" with "at a stop at the extension
test `p` stays tested and its loop changes at most by conjugation (the weak form of (F-stop), row 638). That
is the hypothesis of Lemma 5.2 of `cov-global`, which uses only the conjugacy class of the loop".

**R5 (conditional; text for the file).** `cov-frames.md` (row 638, not checked) reports that the main step
redraws `V_t` on the level-t bonds with *an* end in `Lambda^pr`, not only on those with both ends there
(Y 71488, Y 75680-75684). If that stands, then a plaquette of `Fr_{t-1}(X)` with a corner in `Lambda^pr`
but no edge in the box is fresh at the main step, not carried. In (X5), replace "a plaquette of
`Fr_{t-1}(X)` with no edge in the box" with "a plaquette of `Fr_{t-1}(X)` with no corner in `Lambda^pr`",
and "A plaquette with an edge in the box is fresh" with "A plaquette with a corner in `Lambda^pr` is fresh".
This does not touch Theorem 6.1, which is a statement at `nu_{i+1} <= nu_t`.

## What this check does not cover

- (D1) to (D6) and (D3\*) are read from Y. `cov-x-check.md` accepted (D1) to (D6) as fair readings. (D3\*)
  is row 638's statement.
- (AV1) and (AV2) in local form are cited.
- Lemmas F1, F2, F3, 2b of i3-cert are used as stated. I re-read the proofs of the parts used: the `l < s`
  case of F1, F2, and F3.
- No proof by computer is used. Every step above is a finite box inclusion or an inequality between named
  constants.

RESULT: (COV-X*) HOLDS for every stage h <= i <= t-1, the last included (check of library/cov-xstar.md by Claude Opus 5.5 high; first failing step none; no item FAILS). Lemma 3.1 is exhaustive and disjoint at i = h, k_0, k_0+1, t-1 and when t-1 = k_0+1. Lemmas 4.0, 4.1, 4.2, 5.1, Theorems 6.1, 6.2 and the table (X6) hold. Findings 1 to 5 are confirmed. Y states the one-step average on the new rows at the last stage (Y 72256-72264, 64097-64101). The factor L^2 at i = t-1 is needed in the worst case, so C_2'' = max(C_2, 6 . 4^r L^2) is the right constant for row 634. Repairs to the wording: R1 ("astride dO_{i+1}", not "meet"); R2 (2.1 comes from Y 134117-134118 by the sharp conversion 2 arcsin(eps) <= (2pi/3) eps, not from c_0 = pi/2); R3 (name (LF) in Theorem 6.1); R4 (carrying after nu_t needs only the weak form of (F-stop): tested status kept, loop conjugated); R5 (conditional on cov-frames finding 1, row 638, not checked: the main-step clause of (X5) is "no corner in Lambda^pr"). Open: (D3*) and (D1)-(D6) remain read statements (row 638 for (D3*)); (AV2) is cited.
