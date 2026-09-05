CHECKER VERDICT: PASS-NO-BLOCKER

Every load-bearing claim of block 216 that I could rebuild independently reproduced exactly — the `M_oo`
lemma at symbolic face signs, the necessity radical at five gauge-class witnesses plus a `QQ(√6)` curve
witness, the 64-cell census and the rule-A/rule-B sign identity, the two covariant witnesses with their
`S3_body` stabilisers, `μ`, the cone constants, and the symbol's invariance sets — with one cosmetic
in-note inconsistency (`CK-04`) and one imprecise structural sentence (`CK-02`).

Machinery: my own script `S/ck.py`. I import only the LANDED parents (Block 213 `formal_family`,
`onsite_rules`, `folded_matrix`, `first_order_matrix`, `raising_rules`, `lane_rules`, `metric_candidates`,
`quadratic_form`, `proportionality_minors`; Block 214 `formal_cell`; Block 215 `rotations`,
`corner_action`, `sign_vectors`; Block 211 `leading_minors`, `W1_MODULI` literal). The block-216 runner was
read but never imported, called or copied. Different routes throughout: determinants by **Berkowitz on
sympy Matrices** (not `ff_det`/`DomainMatrix` Bareiss); the necessity variety by **factorisation of the
κ-coefficients into pure powers of the two line forms** (not a Gröbner radical); the stabilisers by
**direct matrix equality** `L H Lᵀ = H` over the 24 lifts; the parameter loci by **rref of the linear
coefficient rows** (not `constraints`/`subgroup_locus`); the pencil by `det(M − t H0)` factored (not the
`(H0⁻¹M)²` DomainMatrix charpoly). Mask convention verified independently:
`tuple(itertools.product((1,-1), repeat=6))[mask]` over `GAUGE_FACE_ORDER`.

---

CK-01 — THE `M_oo` LEMMA AT SYMBOLIC FACE SIGNS. CONFIRMS.

Note line 205-206, verbatim:
> `M_oo = [[0, kt (D16 + D25), -kx (D16 - D34), 0], [., 0, -ky (D25 + D34), 0], [., ., 0, 0], [0, 0, 0, 0]]     on (y, x, t, txy),`
> `free symbols {D16, D25, D34, kt, kx, ky}:  NO shear, NO volume, NO face sign, NO D07.`

Built `H = formal_cell(s_tx0…s_xy1 symbolic; g0, g1, v0, v1 symbolic; D07, D16, D25, D34)`, folded the
onsite rules myself, `M = H0 D(κ) + D(κ)ᵀ H0`, took the odd index set `(1, 2, 4, 7) = (y, x, t, txy)`.
Measured, entry for entry:

    M_oo = [[0, kt*(D16 + D25), -kx*(D16 - D34), 0],
            [kt*(D16 + D25), 0, -ky*(D25 + D34), 0],
            [-kx*(D16 - D34), -ky*(D25 + D34), 0, 0],
            [0, 0, 0, 0]]
    free symbols = {D16, D25, D34, kt, kx, ky}     (exactly the declared six; no s_*, no v*, no g*, no D07)

The coefficient ideal of `M_oo` in `(D07, D16, D25, D34)`, by rref of the linear coefficient rows (my route,
not a radical): generators `(D16 - D34, D25 + D34)` — Block 214's `PLANE` literal for literal — and `M_oo`
vanishes identically on `(D16, D25, D34) = (λ, -λ, λ)`. Also confirmed `H0` IS the cell (the onsite folding
is the identity on it).

CK-02 — THE STRUCTURAL REASON. CORRECTS (imprecise, not wrong; the conclusion stands).

Note line 210-212, verbatim:
> The reason is structural: `(H D)_{oo}[i, j] = Σ_m H[i, m] D[m, j]` needs `m`
> of degree `deg j + 1`, even, so only the cross block `X` on `(1,2,4) × (3,5,6)`
> contributes — the degree blocks, where the signs and the shears live, meet
> `D_{oo} = 0`; and `D07` sits on corner 7, which nothing raises.

Measured: `D_oo = 0` (TRUE, the odd-odd block of the raising matrix vanishes); column 7 of `D` is
identically zero (TRUE — nothing raises to grade 3 from grade 3, so `D[m, 7] = 0` for every `m`); row 0 of
`D` is identically zero. The clause "`D07` sits on corner 7, which nothing raises" is only half the
mechanism: it kills the `(i, 7)` entries of `(H D)_oo`, but the `(7, j)` entries are killed by the
**zero row 0** of `D` (the only route for `D07 = H[7, 0]` into `(HD)[7, j] = Σ_m H[7, m] D[m, j]` is
`m = 0`, and `D[0, j] = 0` because nothing has grade `-1`). Since `M` is symmetric the two halves are
equivalent and the conclusion — no `D07` in `M_oo` — is exactly right; only the one-line reason is
one-sided. The supervisor's own formulation ("D07 killed by the zero row 0 of D") is the complementary
half and also correct. No number moves. Suggested wording: "…and `D07` sits on the `(0, 7)` pair, which
`D`'s zero row 0 and zero column 7 both kill."

Also checked at line 205: `(HD)_oo` picking up only the `1↔2` cross block is right, but note that the
`i = 7` row needs `H[7, m]` for `m ∈ {3, 5, 6}`, which vanishes because the four parameters sit only on
`(0,7), (1,6), (2,5), (3,4)` — that is why the `txy` row and column of `M_oo` are zero, and it is a
statement about the FAMILY, not about `D`. Measured true.

CK-03 — THE BLOCK IDENTITY AND SUFFICIENCY. CONFIRMS.

Note line 215-218, verbatim:
> identity `det [[A, B], [Bᵀ, 0]] = det(B)²` — verified at generic symbolic
> `4 × 4` blocks (`26` symbols, fraction-free)

Rebuilt with a symmetric generic `A` (10 symbols) and a fully generic `B` (16 symbols) = 26 free symbols;
Berkowitz determinant: `det [[A, B], [Bᵀ, 0]] - det(B)² = 0` identically. With `M_oo = 0` on the star line
(CK-01) this gives `det M = det B²` on the line at EVERY cell, so sufficiency is indeed a lemma and not a
witness table. CONFIRMS.

CK-04 — THE CLASS REPRESENTATIVES. CORRECTS (internal inconsistency in the note).

Note line 236-237, verbatim:
> (`D-3`: the class representatives `5, 2, 16, 12`). Mutations

This contradicts the note's own line 186 ("class representatives (the least mask): 5, 2, 11, 12") and its
own claim register, row 7 (line 457): "one witness per class | representatives `5, 2, 11, 12`". The
receipt agrees with 11: `union class_representative_masks (-1, 1): 11`. Measured here: with
`π = (s_tx0 s_ty0 s_xy0, s_tx1 s_ty1 s_xy1)`, class `(-1, +1)` among the 16 star cells is `{11, 16, 38, 61}`
and its least mask is **11**, not 16. So line 236's "`16`" is a typo for "`11`". Cosmetic — mask 16 IS a
star cell in that same class, so the sentence's content (a witness per class) is true either way, and
nothing downstream depends on it. Suggested fix: line 236 → `5, 2, 11, 12`.

CK-05 — THE NECESSITY HALF AT ONE WITNESS PER GAUGE CLASS. CONFIRMS (and by a stronger route).

Note line 224-225, verbatim:
> `radical_generators`; over `QQ(√6)` with `r² − 6` adjoined at the curve
> points) has radical **exactly** `(D16 − D34, D25 + D34)`:

At `W1`'s moduli `(v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4)` with `D07 = 0` and `(D16, D25, D34)` symbolic, at
masks **5, 2, 11, 12** (the four gauge classes) and **16**, I formed `P = det M - det(B)²` by Berkowitz,
took its 36 nonzero `κ`-coefficients, and (a) confirmed every one vanishes on `(λ, -λ, λ)`, so
`I ⊆ (D16 - D34, D25 + D34)`; (b) **factored** them and found, at every mask, coefficients that are a
nonzero rational times a PURE power of a single line form — e.g. at mask 5:
`-256*(D16 - D34)**2/675` and `-256*(D25 + D34)**2/675`; at mask 2: `256*(D16 - D34)**2/125`,
`256*(D25 + D34)**2/125`; at mask 11: `1792*(D16 - D34)**2/675`, `1792*(D25 + D34)**2/675`; at mask 12:
`256*(D16 - D34)**2/1125`, `256*(D25 + D34)**2/1125`; at mask 16: `-1792*(D16 - D34)**2/675`,
`1792*(D25 + D34)**2/675`. Hence `(D16 - D34)² ∈ I` and `(D25 + D34)² ∈ I`, so
`√I ⊇ (D16 - D34, D25 + D34)`, and with (a) `√I = (D16 - D34, D25 + D34)` **exactly**. This is a
Gröbner-free proof of the same statement, so the note's radical is not an artefact of its radical routine.
Also measured at the `QQ(√6)` curve witness — L+−'s moduli `(√6/3, 1/3, 3√6/8, 1/2)` at its own cell,
mask 2: 36 coefficients, all vanishing on the line, with pure coefficients `4*(D16 - D34)**2`,
`4*(D25 + D34)**2`, `-3*(D16 - D34)**2`, `-3*(D25 + D34)**2`. Same radical.

Positive definiteness by exact leading minors at zero parameters (Block 211's `leading_minors`, my call):
mask 2 at L+−'s moduli `(√6/3, 3/4, √6/4, 3/4, 3√6/16, 27/64, 9√6/64, 3/8)`, all `> 0`; mask 16 at L−+'s
`(√6/3, 8/9, 8√6/27, 8/9, 64√6/243, 512/729, 512√6/2187, 128/243)`, all `> 0`. CONFIRMS.

CK-06 — THE CENSUS IDENTITY. CONFIRMS.

Note line 270-273, verbatim:
> `Block 213 rule A (S1 = -E S0 E):  {2, 11, 16, 25, 38, 47, 52, 61}   8 cells, classes (+1, -1) and (-1, +1), P = (+, -, +)`
> `Block 213 rule B (S1 = +E S0 E):  {5, 12, 23, 30, 33, 40, 51, 58}   8 cells, classes (+1, +1) and (-1, -1), P = (-, +, -)`
> `Block 215 star pattern:           the union of the two lines above  16 cells`
> `intersection:                     ALL 16;   with the positive rule-A cells: ALL 8;   nearest rule-A cell to a rule-B star cell: 3 face flips.`

Reproduced Block 213's census myself on `formal_family` at symbolic positive moduli, `metric_candidates`,
`proportionality_minors` and a lex Gröbner basis in `(g0, g1)`, all 64 cells:

    (g0, g1)                 48 cells, all four classes
    (g0*g1 + g0 - g1,)        4 cells, class (1, -1)
    (g0*g1 - g0 + g1,)        4 cells, class (-1, 1)
    (g0*g1 - g0 - g1,)        4 cells, class (1, 1)
    (g0*g1 + g0 + g1,)        4 cells, class (-1, -1)

— `COINCIDENCE_CENSUS` literal for literal. The 16 curve cells are
`(2, 5, 11, 12, 16, 23, 25, 30, 33, 38, 40, 47, 51, 52, 58, 61)` and equal the 16 star-pattern cells
(computed independently from `(P_tx, P_ty, P_xy) = (s_tx0 s_tx1, s_ty0 s_ty1, s_xy0 s_xy1) = ±(+, -, +)`):
TRUE. Rule A computed directly from `s_f1 = -E_i E_j s_f0` with `E = diag(1, -1, 1)` on `(t, x, y)`:
`{2, 11, 16, 25, 38, 47, 52, 61}`, identical to the `P = (+, -, +)` set; rule B from `s_f1 = +E_i E_j s_f0`:
`{5, 12, 23, 30, 33, 40, 51, 58}` = the `P = (-, +, -)` set. Rule-A classes `{(1, -1), (-1, 1)}`, rule-B
classes `{(1, 1), (-1, -1)}`. Hamming distance from each of the 16 star cells to the nearest rule-A cell:
`0` at the eight rule-A cells and `3` at all eight rule-B cells — the note's "3 face flips". The sign
identity `P_f = ∓E_i E_j = ±E_k` (note lines 278-281) checks: `(-E_tE_x, -E_tE_y, -E_xE_y) = (+1, -1, +1)`
= `(E_y, E_x, E_t)` = Block 215's `STAR_PAIR_SIGNS[1:] = (1, -1, 1)` on `(y, x, t)`. CONFIRMS.

CK-07 — THE COVARIANT WITNESS, STABILISER AND LOCUS. CONFIRMS.

Note line 302-303, verbatim:
> `strict stabiliser of the zero-parameter cell                  an S3_body: orders (1, 2, 2, 2, 3, 3) -- both shears alive with E = 1`
> `its parameter locus (Block 215's constraints, E = 1)           (D16 - D34, D25 + D34) with NO forced condition: the star line, shears alive`

By direct matrix equality `L(R) H L(R)ᵀ = H` over Block 215's 24 lifts (no `constraints`, no
`subgroup_locus`), at the transported curve points:

    mask 2  (L+−, moduli (√6/3, 1/3, 3√6/8, 1/2)): stabiliser (0, 7, 11, 12, 16, 23), orders (1,2,2,2,3,3),
            closed under multiplication, 3-fold axis (1, 1, 1)
    mask 16 (L−+, moduli (√6/3, 1/2, 4√6/9, 1/3)): stabiliser (0, 6, 8, 15, 17, 23), orders (1,2,2,2,3,3),
            closed, 3-fold axis (1, -1, 1)

Both agree with the receipt's `witness table` rotation indices. The strict parameter locus of the whole
stabiliser, by rref of the linear coefficient rows of `L H(params) Lᵀ - H(params)`: generators
`(D16 - D34, D25 + D34)` with the forced-moduli set **empty** at both cells — the star line, no condition
on the moduli, both shears alive. The cell with `(λ, -λ, λ)` on the line is preserved by all six: TRUE at
both. Curve and tie membership re-verified: `g0 - g1/(1 + π0 g1) = 0`, `v0² - (1 - g0²)(1 - g1²) = 0`,
`v1² - (1 - g1²)/(1 - g0²) = 0` at both. CONFIRMS.

CK-08 — THE READINGS AND THE CONE CONSTANTS. CONFIRMS.

Note line 305-307, verbatim:
> `the two readings                                               G2 = mu G1 with mu = 32/27 (class (+1, -1)) or 27/32 (class (-1, +1))`
> `the graded cone (zero parameters)                              det B = c (k^T G1 k)^2`
> `the cone ON THE STAR LINE, multiple symbolic                   det M = c (k^T G1 k)^4,  c = 64/81 (pi0 = +1), 9/16 (pi0 = -1): NO lam-dependence`

Measured entry by entry: `G2/G1 = 32/27` at mask 2 (class `(1, -1)`), `= 27/32` at mask 16 (class
`(-1, 1)`) — a single ratio, every entry, so `G2 = μ G1` exactly.
`G1 = [[9/8, -3/8, -3/8], [-3/8, 9/8, -3/8], [-3/8, -3/8, 9/8]]` at mask 2 and
`[[4/3, -2/3, 2/3], [-2/3, 4/3, -2/3], [2/3, -2/3, 4/3]]` at mask 16.
With `Q = kᵀ G1 k`: `det B / Q² = 8/9` (mask 2) and `3/4` (mask 16) — constants, so the graded cone is one
quadric squared. On the star line with `λ` **symbolic** and `D07 = 0`: `det M / Q⁴ = 64/81` (mask 2) and
`9/16` (mask 16) — exactly the declared `c`, and with **no** `λ` in it. Repeated with `D07` **also
symbolic**: `det M / Q⁴` is still `64/81` and `9/16` — so "one metric's cone for every line multiple and
every `D07`" (note lines 311-313) is measured here directly, not inferred from the congruence. CONFIRMS.

CK-09 — THE SYMBOL: IDENTITY, INVARIANCE SETS, INVARIANT DIMENSIONS. CONFIRMS.

Note line 352-360, verbatim:
> Block 213's identity `det B = D3 (kᵀ D1 k)(kᵀ E adj(D2) E k)` holds at every
> witness. Under `κ → Rκ` the two quadrics and `det B` are each invariant for
> **exactly** the six rotations of the strict stabiliser — the `S3_body` — and
> for no other of the 24; the `S3`'s 3-fold axis is one of the four body
> diagonals (all four occur across the 8 cells), and each quadric lies in the
> **two-dimensional** space of `S3`-invariant quadratic forms
> `span(|k|², (n·k)²)` (e.g. at L+−, `n = (1, 1, 1)`:
> `kᵀ D1 k = (√6/2)|k|² − (√6/8)(n·k)²`, `kᵀ E adj(D2) E k = (3/2)|k|² − (3/8)(n·k)²`,
> proportional — the coincidence).

Measured at both witnesses. `det B - D3 (kᵀ D1 k)(kᵀ E adj(D2) E k) = 0` identically: TRUE at masks 2 and
16. Invariance sets under `κ → Rκ` over all 24 rotations: `q1`, `q2` and `det B` each give exactly
`(0, 7, 11, 12, 16, 23)` at mask 2 and exactly `(0, 6, 8, 15, 17, 23)` at mask 16 — identical to the
stabilisers of CK-07, so "exactly the `S3` and no other of the 24" holds. Dimension of the space of
quadratic forms invariant under the stabiliser: **2**; under the full 24: **1**. The span coefficients at
L+− with `n = (1, 1, 1)` come out `q1 = (√6/2)|k|² − (√6/8)(n·k)²` and `q2 = (3/2)|k|² − (3/8)(n·k)²` —
the note's numbers exactly; at L−+ with `n = (1, -1, 1)`, `q1 = (2√6/9)(|k|² + (n·k)²)`,
`q2 = (2/3)(|k|² + (n·k)²)`. `q1/q2` is κ-free at both (the coincidence). CONFIRMS.

CK-10 — THE BRANCHES ON THE COVARIANT LINE. CONFIRMS (see below for the symbolic-λ case).

Note line 326, verbatim:
> | `L+−` (`v0 v1 = 3/4`, `v1/v0 = 9/8`) | `1` (×2), `(32/27)/(1 − 4λ²/3)` (×2), `(4/3)/(1 − 4λ²/3)` (×4) | `1, 128/99, 16/11, 16/11` | `128/119, 128/99, 16/11, 16/11` |

CK-11 — THE TWO RESCALINGS AND THE POSITIVITY BOUNDS. (see below)

Note line 332-337, verbatim:
> rescales the top-form constant `μ` and the transverse pair by the same factor
> `1/(1 − λ²/(v0 v1))` (measured at both witnesses: `12/11` and `128/119` at
> `λ = 1/4`) and leaves the 0-form constant `1`; `D07` rescales the 0-form
> constant alone by `1/(1 − D07² v1/v0)` — Block 214's `128/119` at L+−, and
> `12/11` at L−+, re-measured on the covariant line — and leaves the others.
> The transverse pair stays a degenerate pair (multiplicity 4) on the line. The
> denominators are the line's positivity bounds: `λ² < v0 v1` and `D07² < v0/v1`.

CK-12 — THE TWISTED IDENTITY. (see below)

Note line 366-368, verbatim:
> rotation `T = E L` (four admissible twists for the order-4 generator at L+−)
> the symbol is not invariant: `Tᵀ M(κ) T = M_{E'}(R⁻¹κ)` with `E' = Lᵀ E L`,
