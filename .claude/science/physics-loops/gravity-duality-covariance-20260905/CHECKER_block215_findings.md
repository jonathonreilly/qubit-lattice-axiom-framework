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
