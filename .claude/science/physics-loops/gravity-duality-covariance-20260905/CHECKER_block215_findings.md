CHECKER VERDICT: PASS-NO-BLOCKER

Every load-bearing claim tested on the checker's own machinery reproduces exactly: the lift, the
star and its adjoint identity, the star line and the `M_oo` ideal, the twisted and strict census at
all four representatives (with the per-class distinct-locus counts), the 64-cell scan, the overlap
fold and the controls.

Machinery: the checker built the corner action as the multiplicative extension of the 3x3 signed
permutation on the ordered monomial basis `t < x < y` with an explicit inversion-count sorting sign,
the star from `e_c ^ e_cbar`, and every locus as a per-`(rotation, sign vector)` option list
combined by a pruned union with `rref` canonical parameter ideals and Groebner containment on the
moduli conditions. The runner was read for its literals and never imported, called or copied. Only
Block 214's `formal_cell`/`raising_matrix`/`principal_part`/`cell_with_parameters` and Block 201's
`signed_permutations()` were imported. Scratch: `.../scratchpad/b215check/ck_base.py`, `ck_loci.py`,
`ck1_lift_star.py`, `ck2_census.py`, `ck3_cellscan.py`, `ck4_overlap_controls.py`.

---

## CK-01 — THE LIFT IS A REPRESENTATION AND INTERTWINES `D(kappa)`

Note line 192-193, verbatim: "identity, `L(R₁R₂) = L(R₁)L(R₂)`, element orders `1/2/3/4` in counts
`1/9/8/6`," / "and `L(R) D(κ) L(R)^{-1} = D(Rκ)` for every `R` (with `(Rκ)_ν = Σ_μ R[ν, μ] k_μ`)."

Computed on the checker's own lift (own construction, own sorting sign, no import of the runner):
24 rotations, 24 distinct lifts, all orthogonal, identity present, closed, `L(R1 R2) = L(R1) L(R2)`
for all 576 pairs, order counts `[(1, 1), (2, 9), (3, 8), (4, 6)]`, and
`L(R) D(kappa) L(R)^T = D(R kappa)` for all 24 with `D(kappa)` = Block 214's `raising_matrix()`.
Every lift is `+1` on corner 0 and on corner 7.

**CONFIRMS.**

## CK-02 — `±L(R)` ARE THE ONLY MONOMIAL INTERTWINERS

Note line 467, verbatim: "> rotations intertwining `D(κ)`, with `±L(R)` the only monomial intertwiners;"

Scanned all `256` signed versions of the corner permutation for one rotation of each axis type
(face, edge, body — axis read from the `+1` eigenvector of `R`): the count of sign vectors
intertwining `D(kappa)` is `2` in each case, and the two are exactly `+L(R)` and `-L(R)`.

**CONFIRMS.**

## CK-03 — THE STAR SIGNS, `** = 1`, THE ADJOINT SIGNS, EQUIVARIANCE

Note line 234, verbatim: "star signs   (+1, +1, -1, +1, +1, -1, +1, +1):   * 1 = txy,  * t = +xy,
* x = -ty,  * y = +tx,  * xy = +t, ..."
Note line 236, verbatim: "* D(kappa) = eps_k D(kappa)^T *  on k-forms with eps = (+1, -1, +1) for
k = 0, 1, 2   (the adjoint identity, sign measured);"

Derived independently from `sigma_c` = coefficient of `e_txy` in `e_c ^ e_cbar` (inversion count of
the concatenated ascending index lists, Block 209's corner order): star signs
`(1, 1, -1, 1, 1, -1, 1, 1)`; pair signs on `(0,7), (1,6), (2,5), (4,3)` = `(+, +, -, +)`;
`* * = +1` on every degree (identity matrix); `*` commutes with all 24 lifts;
`P111 = |*|` equals Block 214's `hodge_complement_permutation()` and commutes with exactly `8` of the
24 signed lifts. The adjoint identity, extracted on the correct blocks (rows of degree `2-k`,
columns of degree `k`, both sides mapping `k`-forms to `(2-k)`-forms): `eps = (+1, -1, +1)` for
`k = 0, 1, 2`, each sign unique (the blocks are nonzero, so no sign is vacuous).

**CONFIRMS.**

## CK-04 — THE STAR LINE IS BLOCK 214's PLANE AND IS THE `M_oo` IDEAL

Note line 247-249, verbatim: "> **THE STAR LINE IS `D16 = D34 = −D25` — BLOCK 214's PLANE, LITERAL FOR
LITERAL / > (`PLANE = ("D16 - D34", "D25 + D34")`) — WITH `D07` THE FREE `0 ↔ 3` STAR / > MULTIPLE
(`* 1 = +txy`).**"

Solved `X = lam * (*|_{1->2})` symbolically on the `(y, x, t) x (xy, ty, tx)` block: the unique
solution is `{D16: lam, D25: -lam, D34: lam}`, i.e. the ideal `("D16 - D34", "D25 + D34")`, which is
Block 214's `PLANE` read from the landed module. Independently, the coefficient ideal of the onsite
`M_oo` (from `principal_part(cell, "onsite")`, odd-odd block) in `(D07, D16, D25, D34)` is
`('D16 - D34', 'D25 + D34')` — the same line; `M_oo` at `(lam, lam, lam)` is nonzero
(`2 kt lam` and `-2 ky lam` entries) and identically zero on the star line. The `M_oo` entries are
`(D16 + D25) kt`, `(D34 - D16) kx`, `-(D25 + D34) ky`, matching the note's line 252-253.

**CONFIRMS.**

## CK-05 — THE SHEARS (`E-1`)

Note line 283-286, verbatim: "- **Strict**: only the identity and **one** edge half-turn per class
preserve / both blocks with `E = 1`; every other rotation forces `g0 = 0` or `g1 = 0` or / both. So
strict covariance under any subgroup beyond `C2_edge` kills a / shear, and `T`, `O` kill both."

Recomputed per rotation, per gauge class, on the checker's own option engine (a rotation keeps both
shears iff some admissible sign vector forces no moduli condition). Twisted: `True` for all 24
rotations in all four classes. Strict: exactly `2` rotations per class, at Block 201's indices
`(0, 23)` for `(1, 1)`, `(0, 11)` for `(1, -1)`, `(0, 8)` for `(-1, 1)`, `(0, 21)` for `(-1, -1)` —
index `0` is the identity and the other is an order-2 **edge**-axis element in every class (axis read
from the `+1` eigenvector). These are index-for-index the runner's
`per_rotation_strict_shears_survive` and `per_rotation_twisted_shears_survive`.

**CONFIRMS.**

## CK-06 — THE TWISTED CENSUS AT THE FOUR REPRESENTATIVES (`E-2`)

Note line 296-299, verbatim: "> **TWISTED `O`-COVARIANCE OF THE CURVED FAMILY FORCES ONE LINE AND IT
IS NOT / > THE STAR LINE AT ANY REPRESENTATIVE.** At the all-plus representative it is the / >
diagonal `D16 = D25 = D34`; the shear-alive line meets the star line only at / > the origin
`D16 = D25 = D34 = 0` (measured per class)."

Computed for `1`, `C2_face`, `C2_edge`, `C3_body`, `S3_body`, `T`, `O` at all four representatives,
over **every** member of each class, by direct per-`(rotation, sign vector)` solution sets combined
into a pruned union (a different representation from the runner's: options first, `rref` ideals,
Groebner containment on the moduli conditions). Every component of every locus matches the runner's
declared `TWISTED_LOCI` line for line, e.g. at `(1, 1)` for `C3_body`/`S3_body`/`T`/`O`:
`((), ('D16 - D34', 'D25 - D34'))` plus the six shear-killed components with `('g0',)` or `('g1',)`
and the three other sign lines; at `(1, -1)` and `(-1, 1)` the alive component is
`((), ('D16 + D34', 'D25 + D34'))` = `D16 = D25 = -D34`; at `(-1, -1)` it is the diagonal again.
`C2_edge`-type classes give `((), ('D16 - D25',))`, `((), ('D16 + D25', 'D34'))` and the two
shear-killed `('D16 + D25',)` components. The trivial group, `C2_face` (and `V4_faces`, contained in
the `O` computation) force nothing. The diagonal meets the star line only at the origin (`D25 = D34`
and `D25 = -D34` force `D16 = D25 = D34 = 0`). Distinct-locus counts per class reproduce `E-4`:
`1` for `C3_body`, `S3_body`, `T`, `O`; `3` for `C2_edge`.

**CONFIRMS.**

## CK-07 — THE STRICT CENSUS (`E-3`)

Note line 324-327, verbatim: "> **STRICT `O`-COVARIANCE FORCES THE STAR LINE AND THE FLAT CELL
TOGETHER.** The / > minimal strict class forcing the star line is `C3_body`, and it kills one shear /
> (`g1 = 0` at the all-plus representative, ...)"

At `(1, 1)`: `T` and `O` give `(('g0', 'g1'), ('D16 - D34', 'D25 + D34'))` — the star line with the
flat-shear conditions; `C3_body` gives three distinct loci over its four members, `(('g1',), star)`,
`(('g0',), star)`, `(('g0','g1'), star)` — the runner's declared representative is the `g1` one and
the count `3` is the runner's `strict_distinct_per_class`; `S3_body` likewise `3` with the declared
representative `(('g0',), star)`; `C2_edge` `6` distinct with the declared representative
`(('g0',), ('D16 + D25',))` and one member with **no** forced condition, `((), ('D16 - D34',))`,
which is the shear-alive edge half-turn of CK-05; `C2_face` gives `(('g0','g1'), ())`. No `C3`, `S3`,
`T` or `O` member keeps a shear alive strictly at any representative. The class-representative
caveat is exactly the note's scope qualification 5 (line 457-459) and gate `E-4`; nothing in the
tables is representative-dependent in a way the note does not declare.

**CONFIRMS.**

## CK-08 — `D07` IS FREE (`E-5`)

Note line 273, verbatim: "nonzero denominators). `D07` appears in **no** generator anywhere (`E-5`)."

No generator of any component of any locus computed here — twisted or strict, onsite, any subgroup,
any class, any of the 64 cells — contains `D07`. Mechanism reproduced independently: every lift is
`+1` on corners 0 and 7 (CK-01), so the `(0, 7)` entry maps to `e0 e7 D07` and Block 211's sign
vectors fix `e0 = e7 = +1`.

**CONFIRMS.**

## CK-09 — THE OVERLAP SUM (`F-1`, `F-2`)

Note line 390-392, verbatim: "> **NO SUBGROUP's TWISTED COVARIANCE FORCES `s = 0`.** `s = 0` is
exactly the / > parity-preserving fold, and strict covariance reaches it only through a shear /
> relation."

Verified independently that the overlap `H0` depends on the four parameters only through their sum
(the four entrywise derivatives `dH0/dD07`, `dH0/dD16`, `dH0/dD25`, `dH0/dD34` are equal), and that
with `(D07, D16, D25, D34) = (s, 0, 0, 0)` its even-odd block is exactly `(s/4) P111`. `P111` is the
unsigned star, commutes with the unsigned corner permutation of every rotation and with exactly `8`
of the 24 signed lifts, while the star commutes with all 24 (CK-03). Loci in `s` for `1`, `C2_face`,
`C2_edge`, `C3_body`, `T`, `O` at the four representatives reproduce the runner's declared table
entry for entry: twisted, `s` free in every case (`(((), ()),)`, or `((('g0',), ()), (('g1',), ()))`
for the `C3`-containing subgroups in the two mixed classes — a shear forced on every component,
never `s`); strict, `s = 0` together with `('g0*v0*v1 + g1',)` at `(1, 1)` and `(-1, -1)`, and with
`('g0', 'g0*v0*v1 + g1', 'g0*v0*v1 - g1', 'g1')` for `T`/`O` at the two mixed classes; `1`,
`C2_face` (and `V4_faces`) never force `s`. The all-plus strict relation is `g0 v0 v1 + g1 = 0`
exactly as the note states at line 386-388.

**CONFIRMS.**

## CK-10 — THE CONTROLS (`G-1`, `G-2`, `G-3`)

Note line 399-400, verbatim: "positive definite by exact leading minors / `(15/16, 15/16, 225/256,
15/16, 25/32, 25/32, 1465/2304, 1465/2304)`."

Own exact leading principal minors of `cell_with_parameters("W1")` with `D16 = 1/4` and the other
three zero: `(15/16, 15/16, 225/256, 15/16, 25/32, 25/32, 1465/2304, 1465/2304)`, all positive, at
`D16 - D34 = 1/4 != 0` (off the plane). The folded onsite `H0` **is** the cell, and its even-odd
block entries are exactly `D07, D16, D25, D34` — parity is preserved iff all four vanish, i.e. the
origin, not the plane. The flat cell (`g0 = g1 = 0`, `v0 = v1 = 1`) is the identity at zero
parameters, and its loci are: strict `O`/`T`/`S3`/`C3` = the star line alone; twisted
`O`/`T`/`S3`/`C3` = the four sign lines `D16 = ±D34`, `D25 = ±D34`; `C2_edge`-type = `D16 = ±D25`
(strict, per representative; three distinct sign images over the six members); `1`, `C2_face` =
everything. Identical to the runner's `flat_strict` / `flat_twisted`.

**CONFIRMS.**

## CK-11 — THE 64-CELL SCAN AND `G-4`

Note line 343-345, verbatim: "the four sign lines `D16 = ±D34, D25 = ±D34`; it is the **star line at
exactly / 16 of the 64 cells** and the diagonal at the all-plus cell."
Note line 349-356, verbatim: "**And the 16 cells have a name** (`G-4`, ...): they are exactly the
cells at which a **curved** cell is **strictly** covariant (`E = 1`) under some `S3_body` — the
largest subgroup that keeps both shears alive without any gauge anywhere — and the shear-alive
strict-`S3` locus there is the star line; strict `T` keeps the shears alive at no cell."

Scanned all 64 sign cells (`b211.flipped` over `GAUGE_FACE_ORDER`) on the checker's own engine, with
two generators of `O` (an order-3 and an order-4 element, closure verified to be all 24) after
checking that the generator locus equals the full 24-element locus at the all-plus representative.
Results: exactly **one** shear-alive component at every one of the 64 cells; the four distinct
shear-alive ideals over the scan are `('D16 ± D34', 'D25 ± D34')` — the four sign lines; the star
line `('D16 - D34', 'D25 + D34')` occurs at exactly **16** cells; some `S3_body` keeps both shears
alive under strict covariance at exactly **16** cells, its shear-alive locus there is the star line,
and that cell set is **identical** to the twisted-`O` star-line cell set; strict `T` keeps the shears
alive at **0** cells.

The 16 cells, by face-sign pattern: masks
`{2, 5, 11, 12, 16, 23, 25, 30, 33, 38, 40, 47, 51, 52, 58, 61}` over
`GAUGE_FACE_ORDER = (tx0, ty0, xy0, tx1, ty1, xy1)`. Their characterisation (checker's own, offered
as an addition to the note's `S3` characterisation, not a correction): writing
`P_f = f_offset0 * f_offset1` for each face type, a cell is a star-line cell **iff**
`(P_tx, P_ty, P_xy)` is `(+1, -1, +1)` or `(-1, +1, -1)` — i.e. iff the two-offset product of the
face signs follows the star's own pair-sign pattern `(+, -, +)` on `(tx, ty, xy)` up to a global
sign. Verified exhaustively: that rule selects exactly those 16 masks and no others (8 cells for
each of the two admissible `P` triples). The all-plus cell has `(P) = (+, +, +)` and is therefore not
among them, consistent with its diagonal line.

**CONFIRMS.**

## CK-12 — PLANTED DEFECTS

Spec item 7 (two in-process monkeypatched defects driven through the runner's own `main()`).
**COULD NOT TEST (time)** — the runner's certified baseline takes ~118 s per run and the 70-minute
budget was spent on items 1-6, all of which are independent recomputations rather than re-runs of the
runner. Not a finding against the block: the mutation census is the supervisor's, and every measured
fact the gates assert was recomputed here from scratch.

---

## Summary of dispositions

| item | subject | disposition |
| --- | --- | --- |
| CK-01 | the lift as a representation, intertwining `D(kappa)` | CONFIRMS |
| CK-02 | `±L(R)` the only monomial intertwiners (256-scan, three axis types) | CONFIRMS |
| CK-03 | star signs, `** = 1`, `eps = (+1, -1, +1)`, equivariance, `P111` 8 of 24 | CONFIRMS |
| CK-04 | the star line = Block 214's `PLANE`; `M_oo` coefficient ideal | CONFIRMS |
| CK-05 | the shears: twisted all 24 alive, strict identity + one edge half-turn | CONFIRMS |
| CK-06 | the twisted census at the four representatives (`E-2`, `E-4` counts) | CONFIRMS |
| CK-07 | the strict census (`E-3`), `C3` minimal, `T`/`O` star line + flat | CONFIRMS |
| CK-08 | `D07` free everywhere | CONFIRMS |
| CK-09 | the overlap sum: sum-only, `(s/4) P111`, `s` never forced twisted | CONFIRMS |
| CK-10 | positivity minors, onsite parity, the flat cell | CONFIRMS |
| CK-11 | the 64-cell scan, `G-4`, and the face-sign characterisation of the 16 | CONFIRMS |
| CK-12 | planted defects through the runner's `main()` | COULD NOT TEST (time) |

No REFUTES and no CORRECTS. The one thing the note could add, entirely optional and not a blocker:
the 16 star-line cells have a closed-form face-sign characterisation (CK-11) independent of the
`S3` one already recorded at `G-4`.
