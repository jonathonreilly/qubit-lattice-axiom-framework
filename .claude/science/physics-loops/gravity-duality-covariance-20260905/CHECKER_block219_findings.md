CHECKER VERDICT: PENDING

Independent refuting checker (Opus 5) for block 219 — the three-direction (4,4,4) bench at
the covariant witness. Work in progress; the verdict line is rewritten when the run closes.

Machinery: Block 213's `bench_matrix` / `bloch_matrix` / `raising_rules` / `transpose_rules`,
Block 214's `raising_matrix` / `principal_part`, Block 216's `measure_census` / `BRANCH_TABLE`,
Block 217's `formal` / `curve_moduli` / `moduli_as_g`, Block 218's `phase_matrix` conventions and
Block 211's `leading_minors`, imported read-only. Everything downstream — the Bloch blocks, the
pencil and form symbols, the similarity, the eigenvalue multisets, the seven quadric values, the
read-off, the rescaled constants, the control factor shapes and the overlap fold — is rebuilt in
this seat. The block-219 runner was read for its literals and conventions and never imported,
called or copied. Every Bloch phase is `sp.sympify`d before use.

---

## CK-01 — the bench at extent (4,4,4): 64 sites, 192 raising entries, 64 y-links, eight momenta

Note line 184-186, verbatim:

> bench       Block 213's bench_matrix at extent (4,4,4): 64 sites; raising bench matrix 192 nonzero entries, 64 of them between sites
>             differing only in y (the y direction now carries its link); Bloch momenta (z_t, z_x, z_y) in {1, i}^3, in Block 213's order
>             (1,1,1), (1,1,i), (1,i,1), (1,i,i), (i,1,1), (i,1,i), (i,i,1), (i,i,i) with kappa_z = (0,0,0), e_y, e_x, e_x+e_y, e_t, e_t+e_y,

Computed, on Block 213's `bench_sites`, `bench_matrix(raising_rules(lane_rules(3)), (4,4,4))` and
`bench_momenta((4,4,4))` built in this seat, with the site index decoded independently
(`idx -> (idx//16, (idx//4)%4, idx%4)`, checked against `b213.site_index` at all 64 sites):

- `len(bench_sites) = 64`; raising bench matrix shape `(64, 64)`; **192** nonzero entries.
- Nonzero entries joining sites that differ **only in y**: **64**. (Also measured, not claimed by
  the note: 64 differ only in t and 64 only in x — the 192 split 64/64/64, so the y direction
  carries exactly the same link count as t and x. This is the fact that makes "the y direction now
  carries its link" true rather than merely nonvacuous.)
- `bench_momenta((4,4,4))` returns exactly eight tuples, every entry in `{1, I}`, in the order
  `(1,1,1), (1,1,I), (1,I,1), (1,I,I), (I,1,1), (I,1,I), (I,I,1), (I,I,I)` with
  `kappa_of` giving `(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)`
  = `0, e_y, e_x, e_x+e_y, e_t, e_t+e_y, e_t+e_x, e_t+e_x+e_y`.

Disposition: **CONFIRMS** (every literal in the sentence, including the momentum order and the
kappa assignment, reproduced exactly).

---

## CK-02 — the Bloch-point lemma at symbolic z with z_y live

Note line 217, verbatim:

> d_B(z) = sum_mu (z_mu - 1/z_mu)/2 * D(e_mu)      an exact 8 x 8 identity at symbolic z, z_y a free symbol of the Bloch block (measured);

and note line 221, verbatim:

> D(e_mu)^2 = 0, the D(e_mu) anticommute, hence D(kappa_z)^2 = 0 at all eight points, D(e_t + e_x + e_y)^2 = 0 included.

Computed at `z = (z_t, z_x, z_y)` as three sympy symbols (sympified), against
`sum_mu ((z_mu - 1/z_mu)/2) * D(e_mu)` with `D` = Block 214's `raising_matrix` substituted at the
unit kappas:

- residual after `sp.simplify` on all 64 entries: **0**. `z_y` is in the free symbols of BOTH
  sides, so the identity is not vacuous in y (the specific trap: a lemma stated at symbolic z but
  measured only where z_y = 1 would pass with `z_y` absent — it is present here).
- `D(e_t)^2 = D(e_x)^2 = D(e_y)^2 = 0`: True, True, True. All three anticommutators
  `D(e_a)D(e_b) + D(e_b)D(e_a)` vanish (ta/ty/xy): True, True, True.
- `D(e_t+e_x+e_y) = D(e_t)+D(e_x)+D(e_y)` (D is linear in kappa): True, and its square is 0.
- `D(kappa_z)^2 = 0` at all eight kappas: True at all eight.
- The raising Bloch block equals `i D(kappa_z)` at all eight points, `(i,i,i)` included: True at
  all eight, checked entrywise (not by charpoly).

Also measured, and worth recording because it is a live way to get the pencil wrong: the
transposed raising Bloch block is `-i D(kappa_z)^T` at all eight points, and at `(i,i,i)` it is
**not** equal to the transpose of the raising Bloch block (`i D^T` vs `-i D^T`). A checker or
runner that used `d_B.T` in place of Block 213's `transpose_rules` fold would build a different
pencil. The runner uses `transpose_rules`; this seat used `transpose_rules` too, after checking
that the two genuinely differ.

Disposition: **CONFIRMS**.

---

## CK-03 — the identity at all eight points, upgraded from charpoly equality to DIRECT SIMILARITY

Note lines 235-238, verbatim:

> With `d_B = i D(κ_z)`, `H_B = Z⁻¹ H0 Z` and `D(κ_z)² = 0` the onsite pencil
> block at every point has the charpoly of `(H0⁻¹ M(κ_z))²` (Block 218's
> mechanism, verified there by direct similarity by its checker; here the
> measurement is the charpoly identity):

and note line 246, verbatim:

> **The triply-mixed identity holds exactly** at all five cells;

The note measures a **charpoly** identity. Charpoly equality is weaker than similarity: two
matrices can share a charpoly and not be conjugate. I tested the stronger statement directly.

Computed: for each cell and each of the eight points, `Z * P * Z^-1` entrywise against
`(H0^-1 M(kappa_z))^2`, where `P = -(d_B - H_B^-1 d_B^T H_B)^2` is the onsite pencil Bloch block
built in this seat from Block 213's `bloch_matrix` and `transpose_rules`, `Z = diag(z^c)` over
Block 209's corners, and `H0`, `M` are Block 214's `principal_part`. The residual is taken after
`sp.radsimp` on all 64 entries — a zero matrix, not a zero determinant or a zero charpoly.

Result: **Z P Z⁻¹ = (H0⁻¹M(κ_z))² exactly, at all eight points, at all five cells**
(witness line, witness λ=1/2, witness D07=1/4, W1 line, flat line) — 40 of 40 matrix identities.
`(i,i,i)` with `κ = e_t + e_x + e_y` included.

The mechanism, which is what makes it an identity and not a coincidence: at a fine point
`Z D(κ_z) Z⁻¹ = i D(κ_z)` and `Z⁻¹ D(κ_z) Z = −i D(κ_z)` (the raising entries lower the corner
grade in exactly the directions κ selects), hence
`Z op Z⁻¹ = −(D − H0⁻¹D^T H0)` and, because `D² = (H0⁻¹D^TH0)² = 0`,
`−(D − B)² = DB + BD = (D + B)² = (H0⁻¹M)²`. The sign flip on the cross term is invisible to the
charpoly and to the square, which is why the note's weaker measurement still lands on the truth.

Independently confirmed en route: `H_B(z) = Z⁻¹ H0 Z` at all eight points at all five cells
(40 of 40), and Block 214's `principal_part` `H0` equals Block 213's `folded_matrix` at each cell.

Also computed, on the same machinery, the failure side (note line 243-244: the form reading and
the overlap assembly are `False` at the three pure, three doubly-mixed and triply-mixed columns).
At the witness line point, charpoly identity vs `(H0⁻¹M)²` / `M²`:

| construction | `(1,1,1)` | seven nonzero points |
| --- | :---: | :---: |
| onsite pencil | True | True (all 7) |
| onsite form | True | False (all 7) |
| overlap form | True | False (all 7) |
| overlap pencil | True | False (all 7) |

Disposition: **CONFIRMS**, and strengthens: the note claims charpoly equality, the stronger
similarity `Z P Z⁻¹ = (H0⁻¹M(κ_z))²` holds exactly.

---

## CK-04 — the shape in three directions: the seven Q values and the branch constants

Note lines 287-289, verbatim:

> pure points:          {9/8, 16/11, 18/11} / (9/8) = {1 x2, 128/99 x2, 16/11 x4}
> doubly-mixed points:  {3/2, 64/33, 24/11} / (3/2) = {1 x2, 128/99 x2, 16/11 x4}
> triply-mixed point:   {9/8, 16/11, 18/11} / (9/8) = {1 x2, 128/99 x2, 16/11 x4}       = Block 216's BRANCH_TABLE[("L+-", "line 1/4")] at all seven.

Computed on a different route from the runner's: the eight onsite pencil blocks built in this seat,
their eigenvalues by sympy's `Matrix.eigenvals()` over the algebraic field (not by a DomainMatrix
charpoly and not by root-finding on a declared polynomial), `G1 = D1/D0` by Block 213's
`metric_candidates`, `Q(κ) = κᵀ G1 κ` by Block 213's `quadratic_form` at the kappas my own
`kappa_of` assigns.

- `G1` at the witness = `[[9/8, −3/8, −3/8], [−3/8, 9/8, −3/8], [−3/8, −3/8, 9/8]]`
  = `(3/8)[[3,−1,−1],[−1,3,−1],[−1,−1,3]]`, **identical at all three parameter points**
  (line, λ=1/2, D07=1/4) — parameter-free, as declared.
- `Q` computed (not assumed): `9/8` at `e_t`, `e_x`, `e_y`; `3/2` at `e_t+e_x`, `e_t+e_y`,
  `e_x+e_y`; `9/8` at `e_t+e_x+e_y`. The supervisor's hand value
  `3(9/8) + 6(−3/8) = 27/8 − 18/8 = 9/8` agrees with the computed `κᵀG1κ`.
- Block multisets at the witness line point, measured:
  `{9/8 ×2, 16/11 ×2, 18/11 ×4}` at `(i,1,1)`, `(1,i,1)`, `(1,1,i)` **and at `(i,i,i)`**;
  `{3/2 ×2, 64/33 ×2, 24/11 ×4}` at `(i,i,1)`, `(i,1,i)`, `(1,i,i)`; `{0 ×8}` at `(1,1,1)`.
- Every nonzero eigenvalue divided by that point's `Q`: `{1 ×2, 128/99 ×2, 16/11 ×4}` at
  **all seven** nonzero points, matching `b216.BRANCH_TABLE[("L+-", "line 1/4")]`
  = `(('1',2), ('128/99',2), ('16/11',4))` including the multiplicities 2/2/4.

Disposition: **CONFIRMS** (all 21 nonzero-eigenvalue/quadric ratios at all seven points).

---

## CK-05 — G1 read off the bench, and the seventh-point check

Note lines 302-305, verbatim:

> G1_tt = Q(e_t) = 9/8,  G1_xx = Q(e_x) = 9/8,  G1_yy = Q(e_y) = 9/8;
> G1_tx = (Q(e_t + e_x) - Q(e_t) - Q(e_x))/2 = (3/2 - 9/4)/2 = -3/8,  G1_ty = -3/8,  G1_xy = -3/8       = the six entries of D1/D0;
> the seventh point:  Q(e_t + e_x + e_y) predicted = G1_tt + G1_xx + G1_yy + 2 (G1_tx + G1_ty + G1_xy) = 27/8 - 18/8 = 9/8;  measured 9/8.  CONSISTENT.
> det M on the line:  ONE quadric to the fourth power over QQ(sqrt 6), (64/81) Q^4 at all seven points: 81/64 (pure), 4 (doubly-mixed), 81/64 (triply-mixed).

Computed **bench-only**: the smallest nonzero eigenvalue at each of the six points, read off my own
eigenvalue multisets with no reference to `G1`, then the six entries by the stated formula.

- diagonal: `(9/8, 9/8, 9/8)`; off-diagonal: `(−3/8, −3/8, −3/8)`.
- the read-off matrix divided entrywise by `D1/D0` is the all-ones matrix — the read-off equals
  `G1` in **all nine** entries, not merely in the six that were fitted.
- seventh point: predicted `9/8`, measured `9/8`. Consistent.
- `det M(κ)` at the seven points: `81/64` (pure), `4` (doubly-mixed), `81/64` (triply-mixed);
  `det M / Q⁴` = `64/81` at **all seven** points.

Disposition: **CONFIRMS**.

---

## CK-06 — Block 216's two rescalings on the bench, positivity first

Note lines 195-196, verbatim:

> positivity  the second line multiple's eight leading minors, BEFORE use: (sqrt6/3, 3/4, sqrt6/4, 3/4, sqrt6/8, 3/16, sqrt6/24, 1/9), all
>             positive; lambda^2 = 1/4 < v0 v1 = 3/4 (Block 216's VOLUME_PRODUCTS); the D07 point and the line point positive definite too.

Computed with Block 211's `leading_minors` on the 8×8 formal cell at `(0, 1/2, −1/2, 1/2)`:
`(√6/3, 3/4, √6/4, 3/4, √6/8, 3/16, √6/24, 1/9)` — **the eight literals, in order, exact**, all
positive. `λ² = 1/4 < 3/4 = b216.VOLUME_PRODUCTS["L+-"]`. The line point's minors
`(√6/3, 3/4, √6/4, 3/4, 11√6/64, 363/1024, 1331√6/12288, 1331/4608)` and the D07 point's
`(√6/3, 3/4, √6/4, 3/4, 11√6/64, 363/1024, 1331√6/12288, 158389/589824)` are all positive too.

Note lines 328-329 and 338-342, verbatim:

> same `Q`: the pure-`t` multiset `{9/8 ×2, 2 ×2, 9/4 ×4}`, the doubly-mixed
> `{3/2 ×2, 8/3 ×2, 3 ×4}`; Bloch = direct; `G1` read off the bench unchanged

> constants times `Q`: the pure-`t` multiset `{144/119 ×2, 16/11 ×2, 18/11 ×4}`,
> the doubly-mixed `{192/119 ×2, 64/33 ×2, 24/11 ×4}`; Bloch = direct. **The
> bench-only read-off of `G1` is now rescaled**: the smallest nonzero eigenvalue
> is `(128/119) Q`, so the six entries read off the bench are `(128/119) G1`
> — the read-off recovers `G1` up to the overall factor the `D07` rescaling puts

Computed:

- `λ = 1/2`: pure points `{9/8 ×2, 2 ×2, 9/4 ×4}`, doubly-mixed `{3/2 ×2, 8/3 ×2, 3 ×4}`,
  triply-mixed `= ` the pure one. Ratios to `Q`: `{1 ×2, 16/9 ×2, 2 ×4}` at **all seven** points.
  Block 216's symbolic `BRANCH_TABLE[("L+-","line symbolic")]` evaluated by me at
  `lam_line = 1/2` gives `(16/9, 2), (2, 4), (1, 2)` — the same three constants with the same
  multiplicities; at `lam_line = 1/4` it gives `(128/99, 2), (16/11, 4), (1, 2)`.
  `r = 1/(1 − λ²/(v0 v1))`: `r(1/2) = 3/2`, `r(1/4) = 12/11 = b216.LINE_RESCALE["L+-"]`;
  `{1, (32/27)r, (4/3)r} = {1, 16/9, 2}` at `r = 3/2`. The bench read-off of `G1` at `λ = 1/2`
  is unchanged: `(9/8, 9/8, 9/8; −3/8, −3/8, −3/8)`, ratio to `G1` the all-ones matrix.
- `D07 = 1/4`: pure `{144/119 ×2, 16/11 ×2, 18/11 ×4}`, doubly-mixed
  `{192/119 ×2, 64/33 ×2, 24/11 ×4}`, triply-mixed `=` the pure one. Ratios to `Q`:
  `{128/119 ×2, 128/99 ×2, 16/11 ×4}` at all seven. `1/(1 − D07² v1/v0) = 128/119`
  = `b216.D07_RESCALE["L+-"]`, recomputed from `b216.VOLUME_RATIOS`. The bench read-off is
  `(144/119, 144/119, 144/119; −48/119, −48/119, −48/119)`, whose entrywise ratio to `G1` is
  `128/119` in all nine entries, and whose seventh-point prediction `144/119` equals the measured
  `144/119`. I also checked the premise of the read-off: `144/119` really is the smallest of
  `{144/119, 16/11, 18/11}` and `192/119` the smallest of `{192/119, 64/33, 24/11}`, so the
  constant-1 branch is still the one the bench-only rule picks.

Disposition: **CONFIRMS**, including the corrected `(128/119) G1` read-off literal.

---

## CK-07 — Bloch union = direct on the explicit 64 × 64, by sympy's charpoly

Note lines 267-268, verbatim:

> witness the onsite pencil direct multiset is
> `{0 ×8, 9/8 ×8, 16/11 ×8, 3/2 ×6, 18/11 ×16, 64/33 ×6, 24/11 ×12}`, per block:

Computed by a route the runner does not use: the 64 × 64 onsite pencil symbol built with **plain
sympy matrices** (`sp.Matrix.inv()` on the 64 × 64 bench Hodge matrix, then
`-(d − H⁻¹dᵀH)²`), its characteristic polynomial by sympy's own `Matrix.charpoly` (Berkowitz on
the explicit matrix, not `DomainMatrix.charpoly` over `QQ(√6)`), against the product of my eight
8 × 8 block charpolys.

- direct charpoly degree **64**; `direct − union = 0` exactly.
- direct multiset `{0 ×8, 9/8 ×8, 16/11 ×8, 3/2 ×6, 18/11 ×16, 64/33 ×6, 24/11 ×12}`,
  multiplicities summing to 64 — the note's literal, digit for digit.
- Wall time for the whole route: **3.2 s** (bench build 2.1 s, 64 × 64 sympy inverse and symbol
  0.2 s, direct charpoly 0.5 s, the eight blocks and their product 0.4 s). The note's `N1` timing
  claim ("under one second" for one direct degree-64 charpoly over `QQ(√6)`) is consistent with
  what I see; the direct check plainly fits, and no substitute gate is needed.

Disposition: **CONFIRMS**.

---

## CK-08 — the all-plus W1 control: every factor shape at all eight points

Note lines 352-357, verbatim:

> W1's G1 = D1/D0 = (16/15) [[1, -1/4, -1/4], [-1/4, 1, -1/4], [-1/4, -1/4, 1]];  Q = 16/15 (pure), 8/5 (doubly-mixed), 8/5 (triply-mixed);
> the rational branch (Q, x2) is present at every nonzero point, and the six entries read from these Q values are W1's G1, the seventh consistent;
> the rest:  (i,1,1), (1,1,i), (i,i,1), (1,i,i):  an IRREDUCIBLE CUBIC squared (Block 218's cubics at t and at t + x);
>            (1,i,1):  (385 lam - 256)^2 times an irreducible quadratic squared;   (i,1,i):  (1155 lam - 2048)^2 times an irreducible quadratic squared;
>            (i,i,i):  (5 lam - 8)^2 (165 lam - 256)^2 (4157 lam^2 - 26952 lam + 43008)^2 -- 256/165 is no branch constant times 8/5 (the ratio is 32/33);
> det M on the line at W1:  TWO DISTINCT QUADRICS, each squared: 256/225 at the pure points, 1024/225 at t + x and x + y, 4096/225 at t + y, 3136/225 at t + x + y

Computed on the W1 cell built in this seat (all-plus signs, Block 216's `W1_MODULI`
`(15/16, 1/4, 1, 1/4)`, the line parameters), the eight onsite pencil blocks, each charpoly
factored over `QQ` with `sp.factor_list`:

- `W1's G1 = [[16/15, −4/15, −4/15], [−4/15, 16/15, −4/15], [−4/15, −4/15, 16/15]]`
  = `(16/15)[[1,−1/4,−1/4],[−1/4,1,−1/4],[−1/4,−1/4,1]]`. `Q = 16/15` at the three pure points,
  `8/5` at the three doubly-mixed **and** at the triply-mixed point.
- The `Q` root appears with multiplicity exactly 2 at every one of the seven nonzero points
  (`15λ−16` squared at the pure points, `5λ−8` squared at the four mixed points): True at all seven.
- Factor shapes, measured (all factors squared, degrees summing to 8):
  - `(i,1,1)`, `(1,1,i)`: `(15λ−16)² (4801335λ³ − 18293776λ² + 22913024λ − 9437184)²` — the two
    pure-`t` / pure-`y` blocks are **identical**, and the cubic is irreducible over `QQ`.
  - `(i,i,1)`, `(1,i,i)`: `(5λ−8)² (4801335λ³ − 27171928λ² + 46940160λ − 25165824)²` — irreducible
    cubic squared, and the `tx` and `xy` blocks are identical.
  - `(1,i,1)`: `(15λ−16)² (385λ−256)² (12471λ² − 45584λ + 36864)²`.
  - `(i,1,i)`: `(5λ−8)² (1155λ−2048)² (4157λ² − 28616λ + 49152)²`.
  - `(i,i,i)`: `(5λ−8)² (165λ−256)² (4157λ² − 26952λ + 43008)²`.
  - `(1,1,1)`: `λ⁸`.
  - Irreducible-factor degree pattern over the seven nonzero points in the note's `t, x, y, tx, ty,
    xy, txy` order: `(3, 2, 3, 3, 2, 3, 2)` — the claim-register literal at note line 469.
- `(256/165) / (8/5) = 32/33`, which is none of `{1, 128/99, 16/11}`: the note's "no branch
  constant" is right.
- `det M` at W1: `256/225` at all three pure points, `1024/225` at `t+x` and `x+y`, `4096/225` at
  `t+y`, `3136/225` at `t+x+y`. Symbolically `det M` is a product of exactly **two distinct**
  quadrics, each squared (`((2,2),(2,2))`, two distinct factors).
- The note's own qualification is right: the six entries read from W1's rational branch **do**
  reproduce W1's `G1` (`G1_tx` read off `= −4/15 = G1_tx`) and the seventh point is consistent
  (predicted `8/5`, measured `8/5`). So the read-off is not what separates the witness from the
  control; the shape is. Confirmed, exactly as the note states.

Disposition: **CONFIRMS** (every literal, including the two linear factors and the two quadratics
the note names, plus the `(385λ−256)` / `(1155λ−2048)` assignment to `x` / `ty` respectively).

---

## CK-09 — the overlap fold at symbolic signs, moduli and parameters

Note lines 374-375, verbatim:

> (i,1,i):  (-D07 + D16 - D25 + D34)/4 . P111                       -- NEW;  on the star line +3/16
> (1,i,i):  (-D07 + D16 + D25 - D34)/4 . P111                       -- NEW;  on the star line -1/16

Computed on Block 214's `formal_cell` at **symbolic** face signs `(s_tx0 … s_xy1)`, symbolic moduli
`(g0, g1, v0, v1)` and symbolic parameters `(D07, D16, D25, D34)` — Block 213's `overlap_rules`,
then `bloch_matrix` at each sympified momentum, then the even↔odd block (Block 213's `even_odd`).
`P111` was taken as `4 · ∂E(1,1,1)/∂D07` and checked to be parameter-free, so the comparison is a
genuine matrix identity and not a fit.

- parity block `= c(z) · P111` **exactly**, entrywise, at all four parameter-carrying points, with
  `c = (D07+D16+D25+D34)/4` at `(1,1,1)`, `(−D07−D16+D25+D34)/4` at `(i,i,1)`,
  `(−D07+D16−D25+D34)/4` at `(i,1,i)`, `(−D07+D16+D25−D34)/4` at `(1,i,i)`.
- on the star line `(0, 1/4, −1/4, 1/4)`: `−1/16` at `(i,i,1)`, `+3/16` at `(i,1,i)`, `−1/16` at
  `(1,i,i)` — the three declared values.
- the parity block is the **zero matrix** at `(i,1,1)`, `(1,i,1)`, `(1,1,i)` and `(i,i,i)`, and no
  parameter symbol survives anywhere in the Bloch matrix at those four points.
- overlap pencil block multisets at the witness line point: `{25774/13445 ×4, 22246/9917 ×4}` at
  `(i,1,i)` and `{825/371 ×4, 537/227 ×4}` at `(i,i,i)` — the note's two literals, exact.
  (Also measured, not claimed: `{1 ×8}` at `(i,1,1)` and `(1,1,i)`, `{227/263 ×4, 263/227 ×4}` at
  `(1,i,1)`, and irrational pairs over `QQ(√6)` at `(i,i,1)` and `(1,i,i)`.)
- the overlap bench identifies `t` with `y` (charpolys at `(i,1,1)` and `(1,1,i)` identical) and
  distinguishes `x`; the onsite bench identifies all three pure points, and its triply-mixed
  charpoly equals the pure one.

Disposition: **CONFIRMS**.

---

## CK-10 — CORRECTION: "the five parameter-free points" is four; the fifth agreement is the zero point

Note lines 383-386, verbatim:

> parameter-free at odd weight, three signed sums at weight two. Consequently the
> overlap bench charpolys at the line point **equal** the zero-parameter ones at
> the five parameter-free points and **differ** at the three doubly-mixed points
> (form and pencil).

The same phrase recurs at note line 438 ("the overlap block charpolys at the line point equal the
zero-parameter ones exactly at the five parameter-free points") and inside the byte-gated `N5`
fence at note line 551 ("so the overlap bench at the line point equals the zero-parameter one
exactly at the five parameter-free points").

Measured: the overlap Bloch fold carries all four parameters at **`(1,1,1)`** as well as at the
three doubly-mixed points — `parameters_present` at `(1,1,1)` is `('D07','D16','D25','D34')`, and
the note's own fold table at line 371 states `(1,1,1)`'s parity block as
`(D07 + D16 + D25 + D34)/4 · P111`, which on the star line is `1/16`, not zero. So the
parameter-free points number **four**, not five: `(i,1,1)`, `(1,i,1)`, `(1,1,i)`, `(i,i,i)`.

The line-vs-zero charpoly comparison does agree at **five** points — the four parameter-free ones
**plus `(1,1,1)`** — but at `(1,1,1)` it agrees for an unrelated reason: `κ_z = 0` there, so the
raising Bloch block is the zero matrix and both readings give the zero 8 × 8 symbol
(`λ⁸`) at every parameter value. The agreement at `(1,1,1)` is not evidence of a parameter-free
fold; it is the zero point being blind to the fold entirely. Measured line-vs-zero, both readings:
True at `(1,1,1)`, `(1,1,i)`, `(1,i,1)`, `(i,1,1)`, `(i,i,i)`; False at `(1,i,i)`, `(i,1,i)`,
`(i,i,1)`.

The note's own CLAIM REGISTER row 17 (line 470) states this correctly — "parameter-free at four
points; three signed sums; line = zero at five points" — so the register and the prose disagree,
and the register is the one that matches the machine. Three sentences carry the wrong label,
including one inside the byte-gated fence.

No number moves: the count of charpoly agreements (five) and the count of parameter-free folds
(four) are both correct in the note somewhere; only the phrase "the five parameter-free points"
merges them into a false description. Suggested repair: "at the four parameter-free points and at
the zero point, where the block vanishes identically".

Disposition: **CORRECTS** (wording defect in three places, one of them byte-gated; no mathematics
affected, no landed number touched).

---

## CK-11 — the flat control and the smaller-extent reproduction

Note lines 202-204, verbatim:

> the flat cell at zero parameters gives R5's `{0 ×8, 1 ×24, 2 ×24, 3 ×8}` =
> Block 213's `expected_flat_multiset((4,4,4))` under both assemblies and both
> readings, direct (`C-3`, mutation `break_flat_control`);

Computed: the direct 64 × 64 charpoly at the flat cell `(1, 0, 1, 0)` at zero parameters, built
and factored in this seat under all four constructions (onsite/overlap × form/pencil), sympy
`charpoly` then `sp.roots`:

- all four give degree 64 with multiset `{0 ×8, 1 ×24, 2 ×24, 3 ×8}`, multiplicities summing to 64.
- `b213.expected_flat_multiset((4,4,4))` = `((0,8),(1,24),(2,24),(3,8))` — identical.

Disposition: **CONFIRMS**.
