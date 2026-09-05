CHECKER VERDICT: PASS-NO-BLOCKER

Every load-bearing claim of the block-218 note that I could reach in the budget was rebuilt from
scratch (my own periodic bench, my own Bloch fold, my own `Z`-conjugation similarity, sympy
`factor_list`/`charpoly` in place of the runner's `DomainMatrix` charpolys) and reproduced exactly;
two items are CORRECTS-grade precisions of wording, none of them touches a number.

Method note. Parent runners were imported read-only for their landed primitives only
(`b213.lane_rules/raising_rules/transpose_rules/onsite_rules/overlap_rules/formal_family/
metric_candidates/quadratic_form/bench_momenta/multiset_of`, `b214.raising_matrix`,
`b216.formal/moduli_as_g/W1_MODULI/FLAT_MODULI/BRANCH_TABLE`, `b217.curve_moduli`). The block-218
runner `scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py` was
read but never imported, called or copied. The bench, the Bloch blocks, the phase matrix `Z`, the
identities, the ratios, the cross term, `det M`, the control's factor shapes, the overlap fold and
the `32 x 32` charpolys are my own code in the checker scratch (`b218check/ck.py`, `a.py`-`g.py`).

---

### CK-01 — the bench at extent (4,4,2)  — CONFIRMS

Note line 181, verbatim:
> `bench       Block 213's bench_matrix at extent (4,4,2): sites 32; raising bench matrix 64 nonzero entries, 0 between sites differing`

and line 182:
> `            only in y; Bloch momenta z = (1,1,1), (1,i,1), (i,1,1), (i,i,1) with kappa_z = (0,0,0), (0,1,0), (1,0,0), (1,1,0);`

Computed: my own periodic bench (site loop, step wrapped modulo the extent, aliases added) on
`raising_rules(lane_rules(3))` at `(4,4,2)`. **32 sites; 64 nonzero entries; 0 entries between
sites differing only in `y`.** My bench equals `b213.bench_matrix` entrywise (a cross-check of my
own construction, not a premise). My own momenta `exp(2 pi i m/N)`, `m < N/2`, reproduce
`b213.bench_momenta((4,4,2)) = ((1,1,1), (1,I,1), (I,1,1), (I,I,1))` — the mixed fine point
`(i,i,1)` is present. Independently: the declared witness face signs `(+,+,+,+,-,+)` satisfy
Block 213's rule A (`S1 = -E S0 E`, residual zero on the symbolic family).

### CK-02 — the raising Bloch block, additivity, `d^2 = 0`  — CONFIRMS

Note lines 211-213, verbatim:
> `d_B(z) = sum_mu (z_mu - 1/z_mu)/2 * D(e_mu)      an exact 8 x 8 identity at symbolic z (the lane's forward +eta/2 and backward -eta/2`
> `                                                  links along mu add to (eta/2)(z_mu - 1/z_mu) on the graded entries; D(e_mu) = eta);`
> `at z_mu = i:  (i - (-i))/2 = i;   at z_mu = 1:  0;   so d_B(z) = i D(kappa_z),  kappa_z = e_t [z_t = i] + e_x [z_x = i]:`

Computed on my own Bloch fold at symbolic `z = (zt, zx, zy)`: `d_B(z) - sum_mu (z_mu - 1/z_mu)/2
D(e_mu) = 0` exactly (8 x 8 zero matrix). `D(e_t)^2 = D(e_x)^2 = D(e_y)^2 = 0`; all nine
anticommutators `D(e_mu)D(e_nu) + D(e_nu)D(e_mu) = 0`; `D(e_t + e_x) = D(e_t) + D(e_x)` and
`D(e_t + e_x)^2 = 0`. At the four points `d_B - i D(kappa_z) = 0`, mixed point included.

### CK-03 — the transposed Bloch block and the sign bookkeeping  — CONFIRMS (item 3 recheck)

Note lines 233-235, verbatim:
> `to `0` (the row grade is one higher), so `Z D Z⁻¹ = i D` and`
> ``Z Dᵀ Z⁻¹ = −i Dᵀ`, and the conjugated operator is `−(D − H0⁻¹ Dᵀ H0)` with`
> ``D = D(κ_z)`; its negative square is `−(D − H0⁻¹ Dᵀ H0)² = (D + H0⁻¹ Dᵀ H0)²`

Computed explicitly at all four points: `bloch(transpose_rules(raising), z)` equals
`d_B(1/z)^T` **and** equals `-d_B(z)^T` **and** equals `-i D(kappa_z)^T`. So the transposed block
is the Hermitian transpose at a unimodular point, and the sign bookkeeping is:
`Z d_B Z^-1 = i (i D) = -D`, `Z d_B^dag Z^-1 = -i (-i D^T) = -D^T`, `Z H_B Z^-1 = H0`, hence
`Z (d_B - H_B^-1 d_B^dag H_B) Z^-1 = -(D - H0^-1 D^T H0)`, verified as a matrix identity (not by
charpoly) at every point, at the witness, at `W1` and at the flat cell. `A = H0^-1 D^T H0` satisfies
`A^2 = 0`, so `-(D-A)^2 = (D+A)^2 = (H0^-1 M(kappa_z))^2` — verified as matrices, both sides.

### CK-04 — the onsite Hodge block is a similarity  — CONFIRMS (strengthened)

Note lines 224-225, verbatim:
> `z^{c_j − c_i}`, so `H_B(z) = Z⁻¹ H0 Z` with `Z = diag(z^c)` — measured True at`
> `all four points at the witness, the control and the flat cell. Mutation `break_onsite_similarity`.`

Computed at **symbolic** `z = (zt, zx, zy)` (stronger than the four measured points):
`H_B(z) - Z^-1 H0 Z = 0` at the witness line cell, the `W1` line cell and the flat line cell.

### CK-05 — the mixed-point identity  — CONFIRMS

Note lines 244-245, verbatim:
> `**The mixed-point identity holds exactly**: the onsite pencil Bloch block at`
> ``(i, i, 1)` has the charpoly of `(H0⁻¹ M(e_t + e_x))²` at the witness, the`

Computed by DIRECT SIMILARITY, not by charpoly comparison:
`Z (-(d_B - H_B^-1 d_B^dag H_B)^2) Z^-1 - (H0^-1 M(kappa_z))^2 = 0` at all four points and all
three cells (witness line, `W1` line, flat line); the charpolys agree as a corollary. Eigenvalue
multisets of `-(operator)^2` at the witness, by `factor_list` over `QQ(sqrt 6)` on my own 8 x 8
charpoly, matching `(H0^-1 M)^2` term by term:

```
(i,1,1) and (1,i,1):  {9/8 x2, 16/11 x2, 18/11 x4}
(i,i,1):              {3/2 x2, 64/33 x2, 24/11 x4}
(1,1,1):              {0 x8}
flat: {1 x2, 16/15 x6} at both pure points, {2 x2, 32/15 x6} at the mixed point
```

The form reading fails at every nonzero point (witness and `W1`): its charpoly differs from the
principal part's at each of `(1,i,1)`, `(i,1,1)`, `(i,i,1)`. Overlap: see CK-09.

### CK-06 — the cone's shape: `G1`, `Q`, and the branch constants  — CONFIRMS

Note lines 283-284, verbatim:
> ``G1 = D1/D0` at the witness is `(3/8)·[[3, −1, −1], [−1, 3, −1], [−1, −1, 3]]`,`
> `so `Q(κ) = κᵀ G1 κ` takes the values `9/8`, `9/8`, `3/2` at `e_t`, `e_x`,`

and lines 288-290, verbatim:
> `(i,1,1):  {9/8, 16/11, 18/11} / (9/8) = {1 x2, 128/99 x2, 16/11 x4}`
> `(1,i,1):  {9/8, 16/11, 18/11} / (9/8) = {1 x2, 128/99 x2, 16/11 x4}`
> `(i,i,1):  {3/2, 64/33, 24/11} / (3/2) = {1 x2, 128/99 x2, 16/11 x4}       = Block 216's BRANCH_TABLE[("L+-", "line 1/4")] at every point.`

Computed with Block 213's `metric_candidates` on my own witness cell at **zero** parameters and at
the line point (they agree — `G1` is parameter-free here, since the four duality entries sit off the
unit-corner block): `G1 = [[9/8, -3/8, -3/8], [-3/8, 9/8, -3/8], [-3/8, -3/8, 9/8]]`, i.e. exactly
`(3/8)[[3,-1,-1],[-1,3,-1],[-1,-1,3]]`. `Q(e_t) = Q(e_x) = 9/8`, `Q(e_t + e_x) = 3/2`. Dividing my
own pencil multisets by `Q` at each of the three points gives `{1 x2, 128/99 x2, 16/11 x4}` at all
three, identical to `b216.BRANCH_TABLE[("L+-", "line 1/4")] = (('1',2,True), ('128/99',2,True),
('16/11',4,True))`. Every nonzero eigenvalue at the three points is a branch constant times one
quadric value: CONFIRMED.

### CK-07 — the cross term and `det M` at the witness  — CONFIRMS

Note lines 306-308, verbatim:
> `G1_tx(bench) = (Q(e_t + e_x) - Q(e_t) - Q(e_x))/2 = (3/2 - 9/8 - 9/8)/2 = -3/8  =  G1[t, x]  (the entry of D1/D0);`
> `the plane restriction read off the bench: (G1_tt, G1_tx, G1_xx) = (9/8, -3/8, 9/8);   the pure points coincide (Q(e_t) = Q(e_x));`
> `det M on the line: ONE quadric to the fourth power over QQ(sqrt 6), 81/64 at e_t, 81/64 at e_x, 4 at e_t + e_x,  4 / (81/64) = (4/3)^4 = (Q_mixed / Q_t)^4.`

Computed: `(Q_mixed - Q_t - Q_x)/2 = (3/2 - 9/8 - 9/8)/2 = -3/8`, equal to `G1[0,1]`. Plane
restriction `(9/8, -3/8, 9/8)`. My own `det M(kappa)` (symbolic `kt, kx, ky`, `M = H0 D + D^T H0`)
factors over `QQ(sqrt 6)` as `(81/64) * ((3kt^2 - 2kt kx - 2kt ky + 3kx^2 - 2kx ky + 3ky^2)/3)^4` —
**factor shape `[(2, 4)]`, one quadric to the fourth**; the quadric is `(8/9) Q(kappa)`, so
`det M = (64/81) Q^4`, Block 216's `CONE_ON_LINE_CONSTANTS` value. Values `81/64`, `81/64`, `4` at
`e_t`, `e_x`, `e_t + e_x`; `4/(81/64) = 256/81 = (4/3)^4 = (Q_mixed/Q_t)^4`.

### CK-08 — the all-plus `W1` control  — CONFIRMS

Note lines 332-334 and 339, verbatim:
> `W1, onsite pencil blocks:   (i,1,1): (15 lam - 16)^2 (4801335 lam^3 - 18293776 lam^2 + 22913024 lam - 9437184)^2     -- Block 217's cubic`
> `                            (1,i,1): (15 lam - 16)^2 (385 lam - 256)^2 (12471 lam^2 - 45584 lam + 36864)^2`
> `                            (i,i,1): (5 lam - 8)^2 (4801335 lam^3 - 27171928 lam^2 + 46940160 lam - 25165824)^2`
> `det M on the line at W1:    TWO DISTINCT QUADRICS, each squared (256/225 at e_t, 1024/225 at e_t + e_x) -- a union of two, Block 217's F-3.`

Computed with my own charpolys and `factor_list` over `QQ`: the three factor shapes reproduce
coefficient for coefficient — `(15,-16)^2 (4801335,-18293776,22913024,-9437184)^2` at `(i,1,1)`;
`(15,-16)^2 (385,-256)^2 (12471,-45584,36864)^2` at `(1,i,1)`; `(5,-8)^2 (4801335,-27171928,
46940160,-25165824)^2` at `(i,i,1)`. The rational roots are `16/15, 16/15, 8/5` = `W1`'s
`Q(kappa_z)` with `G1 = [[16/15,-4/15,-4/15],...]` and `(8/5 - 16/15 - 16/15)/2 = -4/15 = G1_tx`.
The cubics and the quadratic are irreducible over `QQ` (they are `factor_list` irreducibles), the
two pure points differ, no branch constant exists. `det M` at `W1` factors as two **distinct**
quadrics each squared, `2kt^2 - kt kx - kt ky + 2kx^2 - kx ky + 2ky^2` and
`3kt^2 - 2kt kx + 2kt ky + 3kx^2 - 2kx ky + 3ky^2`, constant `64/2025`; values `256/225` at `e_t`
and `1024/225` at `e_t + e_x`.

### CK-09 — the overlap fold per point  — CONFIRMS (strengthened)

Note lines 352-354, verbatim:
> `(1,1,1):  parity block (D07 + D16 + D25 + D34)/4 . P111          -- Block 217's (s/4) P111`
> `(1,i,1):  parameter-free           (i,1,1):  parameter-free       -- Block 217's G-2 at both pure points`
> `(i,i,1):  parity block (-D07 - D16 + D25 + D34)/4 . P111        -- ALL FOUR parameters, through a SIGNED sum`

Computed on a **fully generic symmetric 8 x 8 cell** (36 free symbols — strictly more general than
symbolic face signs, moduli and parameters, so it subsumes the note's test): the part of the overlap
Bloch fold that depends on the four complement-pair entries `a07, a16, a25, a34` is
`0` at `(1,i,1)` and `(i,1,1)` (parameter-free); equals `((a07 + a16 + a25 + a34)/4) * P111` at
`(1,1,1)`; and equals `((-a07 - a16 + a25 + a34)/4) * P111` at `(i,i,1)`, with `P111` the
complement permutation. The signed sum and its sign pattern are exactly as claimed. The overlap
fold is **not** a similarity `Z^-1 H0 Z` at any nonzero point (checked), and the overlap block
charpoly differs from the principal part's under both readings at all three nonzero points, at the
witness and at `W1` — the note's `False` row is reproduced.

### CK-10 — line vs zero parameters, and the `t`/`x` distinction  — CONFIRMS, with one wording precision (CORRECTS)

Note lines 374-376, verbatim:
> `overlap, witness:   (i,1,1) and (1,i,1) DIFFER:  form {36481/55296 x4, 89401/55296 x4} against {51529/55296 x4, 69169/55296 x4};`
> `                                                 pencil R5's {1 x8} against {227/263 x4, 263/227 x4}`
> `overlap, W1:        form coincides (Block 214's OVERLAP_FORM_W1 at both);  pencil differs: {1 x8} against {55/71 x4, 71/55 x4}`

Reproduced exactly, all eight literals: witness `(i,1,1)` form `{36481/55296 x4, 89401/55296 x4}`,
pencil `{1 x8}`; witness `(1,i,1)` form `{51529/55296 x4, 69169/55296 x4}`, pencil
`{227/263 x4, 263/227 x4}`; `W1` form `{116281/147456 x4, 4844401/3686400 x4}` at both pure points
(= `b214.OVERLAP_FORM_W1`'s nonzero part), pencil `{1 x8}` at `(i,1,1)` against
`{55/71 x4, 71/55 x4}` at `(1,i,1)`. Onsite at the witness: the two pure points coincide.
Also reproduced: witness `(i,i,1)` overlap pencil `{490/299 x8}` at zero parameters and the
quadratic-to-the-fourth `(17837 lam^2 - 58604 lam + 48020)^4` on the line (its roots
`29302/17837 +- 588 sqrt 6 /17837`, each multiplicity 4); the `(i,i,1)` overlap **form** on the line
is an irreducible quartic squared **over QQ** and an irreducible quadratic squared, twice (a
`sqrt 6`-conjugate pair), over `QQ(sqrt 6)` — the note's table entry at line 276 says "an
irreducible quartic squared" without naming the field, and the note's own scope line says the
charpolys are taken over `QQ(sqrt 6)`; the shape is field-dependent here and only the `QQ` reading
is the true one. **CORRECTS (wording, no number affected).**

Second precision. Note line 363-364 reads "the overlap bench charpolys at the line point **equal**
the zero-parameter ones at both pure points and **differ** at the mixed point". True as stated for
charpolys. But at the **zero Bloch point** `(1,1,1)` the overlap fold matrices at the line point and
at zero parameters are **not** equal (the parity block `(s/4) P111` is nonzero on the line, where
`s = 1/4`); their charpolys both collapse to `lam^8` because `d_B(1,1,1) = 0`, which is why the bench
charpoly claim survives. The spec's phrasing "the overlap bench **blocks** at the line point equal
the zero-parameter ones at the pure points" holds at the two pure fine points and must not be read
as covering `(1,1,1)`. **CORRECTS (scope of a word, no number affected).**

### CK-11 — Bloch union = direct on the explicit `32 x 32`  — CONFIRMS

Note lines 267-269, verbatim:
> `**Bloch union = direct** (Block 213's E-gate: the direct `32 × 32` charpoly over`
> ``QQ(√6)` against the product of the four `8 × 8` block charpolys over`
> ``QQ(√6, i)`), and the zero Bloch point contributes eight zeros everywhere. Per`

Computed by a different route from the runner's `DomainMatrix` charpolys: sympy's `charpoly` on my
own explicit `32 x 32` bench pencil symbol `-(d - H^-1 d^T H)^2`, against the product of my four
`8 x 8` block charpolys. Both requested cases agree exactly and are degree 32:
**witness onsite pencil** (direct multiset `{0 x8, 9/8 x4, 16/11 x4, 3/2 x2, 18/11 x8, 64/33 x2,
24/11 x4}` — the four blocks' union, eight zeros from `(1,1,1)`) and **`W1` onsite pencil**
(irrational, agreement checked at the polynomial level). Both charpolys finished in under a second.

### CK-12 — planted defects through the runner's `main()`  — COULD NOT TEST

Spec item 8 requires monkeypatching the runner in-process, which requires importing it; the hard
rule forbids importing or calling the block runner, and the mutation census is the supervisor's to
verify from the primary's raw outputs. Not attempted. The `break_*` mutation names are therefore
unexercised here; every family they guard was instead re-derived independently above.

---

### One defect found, and it was mine

My first pass reported the `Z`-conjugation identity as **False** at the witness and at `W1`. The
cause was in my own checker code, not in the block: passing Python `int` `1` as a Bloch phase makes
`1 ** -1` a Python **float**, which silently floated the whole fold. After sympifying the phases the
identity is exact everywhere. Recorded because it is exactly the failure mode the note's `I-2`
no-float gate exists to catch, and the block's own runner is clean of it (its phases come from
`b213.bench_momenta`, which are sympy objects).
