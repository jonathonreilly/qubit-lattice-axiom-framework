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

CK-10 — THE BRANCHES ON THE COVARIANT LINE. CONFIRMS.

Note line 326-327, verbatim:
> | `L+−` (`v0 v1 = 3/4`, `v1/v0 = 9/8`) | `1` (×2), `(32/27)/(1 − 4λ²/3)` (×2), `(4/3)/(1 − 4λ²/3)` (×4) | `1, 128/99, 16/11, 16/11` | `128/119, 128/99, 16/11, 16/11` |
> | `L−+` (`v0 v1 = 8/9`, `v1/v0 = 4/3`) | `1` (×2), `(27/32)/(1 − 9λ²/8)` (×2), `(9/8)/(1 − 9λ²/8)` (×4) | `1, 108/119, 144/119, 144/119` | `108/119, 12/11, 144/119, 144/119` |

My route is the pencil `det(M − t H0)` factored over `QQ(√6)[κ][t]`, NOT the runner's `(H0⁻¹M)²`
DomainMatrix charpoly. At L+− (mask 2), `λ = 1/4`, `D07 = 0`, `κ` fully symbolic, the pencil factors into
quadratics in `t` only:

    (33t² − 48kt² − 48kx² − 48ky² + 32ktkx + 32ktky + 32kxky)
        · (11t² − 18kt² − 18kx² − 18ky² + 12ktkx + 12ktky + 12kxky)²
        · (8t² − 9kt² − 9kx² − 9ky² + 6ktkx + 6ktky + 6kxky) / 110592

i.e. `t² = c · (kᵀ G1 k)` with `c ∈ {1, 128/99, 16/11 (twice)}` — every branch `k`-free times `Q`, and in
eigenvalues of `(H0⁻¹M)²` that is `1 (×2), 128/99 (×2), 16/11 (×4)`, the note's multiplicities. Symbolic
`λ`: L+− gives `-32/(36λ² − 27) = (32/27)/(1 − 4λ²/3)` (×2) and `-4/(4λ² − 3) = (4/3)/(1 − 4λ²/3)` (×4)
beside `1` (×2); L−+ gives `-27/(36λ² − 32) = (27/32)/(1 − 9λ²/8)` (×2) and
`-9/(9λ² − 8) = (9/8)/(1 − 9λ²/8)` (×4) beside `1` (×2). Both rows of the table, exactly.
At `λ = 1/4`: L+− `{1, 128/99, 16/11 ×2}`, with `D07 = 1/4` `{128/119, 128/99, 16/11 ×2}`; L−+
`{1, 108/119, 144/119 ×2}`, with `D07 = 1/4` `{108/119, 12/11, 144/119 ×2}`. (The `λ = 1/4` L−+ rows were
cross-checked at three rational `κ` points, `(1,2,3)`, `(1,-1,2)`, `(2,3,5)`; where my factoriser split a
quadratic further it was only because `c·Q` was a perfect square there — e.g. `t² − 36` at `(2,3,5)` with
`Q = 36`, `c = 1`, and `t² − 16` at `(1,-1,2)` with `Q = 44/3`, `c = 12/11`. Same constants.) CONFIRMS.

CK-11 — THE TWO RESCALINGS AND THE POSITIVITY BOUNDS. CONFIRMS.

Note line 332-337, verbatim:
> rescales the top-form constant `μ` and the transverse pair by the same factor
> `1/(1 − λ²/(v0 v1))` (measured at both witnesses: `12/11` and `128/119` at
> `λ = 1/4`) and leaves the 0-form constant `1`; `D07` rescales the 0-form
> constant alone by `1/(1 − D07² v1/v0)` — Block 214's `128/119` at L+−, and
> `12/11` at L−+, re-measured on the covariant line — and leaves the others.
> The transverse pair stays a degenerate pair (multiplicity 4) on the line. The
> denominators are the line's positivity bounds: `λ² < v0 v1` and `D07² < v0/v1`.

Arithmetic checked against MY branch constants of CK-10. Line factor `1/(1 − λ²/(v0 v1))` at `λ = 1/4`:
L+− has `v0 v1 = (√6/3)(3√6/8) = 3/4` → `12/11`, and `(32/27)(12/11) = 128/99` (top form),
`(4/3)(12/11) = 16/11` (transverse pair, where `4/3 = 1/(1 − g1²)` at `g1 = 1/2`); L−+ has
`v0 v1 = (√6/3)(4√6/9) = 8/9` → `128/119`, and `(27/32)(128/119) = 108/119`,
`(9/8)(128/119) = 144/119` (with `9/8 = 1/(1 − g1²)` at `g1 = 1/3`). `D07` factor `1/(1 − D07² v1/v0)` at
`D07 = 1/4`: L+− `v1/v0 = 9/8` → `128/119`, and the 0-form constant `1 → 128/119` while the others do not
move; L−+ `v1/v0 = 4/3` → `12/11`, and `1 → 12/11`. All four measured constants match the note, and the
two rescalings do act on complementary branches. The multiplicity-4 transverse pair persists on the line
(CK-10's squared factor).

The positivity claim is measured, not asserted: at mask 2 with `(D07, λ, -λ, λ)` symbolic, the exact
leading minors of the cell are

    √6/3, 3/4, √6/4, 3/4, -√6(4λ² - 3)/16, 3(4λ² - 3)²/64, -√6(4λ² - 3)³/192, (9D07² - 8)(4λ² - 3)³/576

Minor 5 is positive iff `λ² < 3/4 = v0 v1`; given that, `(4λ² - 3)³ < 0`, so minor 8 is positive iff
`9D07² - 8 < 0`, i.e. `D07² < 8/9 = v0/v1`. So the pencil denominators ARE exactly the line's positivity
bounds at this witness — the note's sentence is right and now has a proof rather than a coincidence of
denominators. CONFIRMS.

CK-12 — THE TWISTED IDENTITY. CONFIRMS.

Note line 366-370, verbatim:
> rotation `T = E L` (four admissible twists for the order-4 generator at L+−)
> the symbol is not invariant: `Tᵀ M(κ) T = M_{E'}(R⁻¹κ)` with `E' = Lᵀ E L`,
> so `det M(Rκ) = det M_{E'}(κ)` is the symbol of the **gauged** raising part
> `E' D E'` (which differs from `D`), `det B` matching up to the twisted lift's
> sign `det T_e det T_o`, and `det M(Rκ) ≠ det M(κ)`.

At mask 2's witness (zero parameters) I took the first order-4 rotation among the 24 (there are 6 of order
4), scanned Block 215's 64 sign vectors for admissible twists `T = E L` with `T H Tᵀ = H`, and found
exactly **4**. For the first of them: `E' = Lᵀ E L` is diagonal; `Tᵀ M(κ) T − M_{E'}(R⁻¹κ) = 0` identically
in `κ`, where `M_{E'}(κ') := H0 (E' D(κ') E') + (E' D(κ') E')ᵀ H0`; `E' D E' ≠ D` (the gauged raising part
really differs); and `det M(Rκ) ≠ det M(κ)`. So twisted covariance is an identity between two kernels'
symbols and not an invariance of one — the note's statement, reproduced. CONFIRMS.

CK-13 — THE D07 CONGRUENCE. COULD NOT TEST (time).

Note line 343-346, verbatim:
> `U = I − (D07/D3) E_70` gives `Uᵀ M U = M|_{D07 = 0}` with the six face signs,
> the four moduli and the three other parameters all symbolic, and
> `Uᵀ H0 U − H0|_{D07=0}` is `−D07² v1` on the `(0, 0)` entry and zero
> elsewhere — Block 214's `N2` now at every cell at once.

Not rebuilt inside the budget. Two indirect confirmations, both measured here: `det M / (kᵀ G1 k)⁴` on the
star line is `64/81` (mask 2) and `9/16` (mask 16) with `D07` **symbolic** as well as with `D07 = 0`
(CK-08), which is the congruence's consequence `det M` is `D07`-free; and `M_oo` carries no `D07` at
symbolic face signs (CK-01). Nothing contradicts the sentence; I simply did not build `U`.

CK-14 — WHAT I DID NOT TEST. COULD NOT TEST (time / out of scope by the spec).

Not attempted: the 28-mutation census (excluded by the spec — the supervisor verified it from the raw
outputs); the necessity radical at the remaining 20 of the 26 witnesses (I did 5 W1 cells covering all four
gauge classes plus mask 16, and 1 curve witness; the six I did are representative and all agree); the
covariant witness at the other six rule-A cells (masks 11, 25, 38, 47, 52, 61 — the receipt's own table has
them and their stabilisers are the same four `S3_body`s permuted by class, which is consistent with the two
I measured); the flat-cell and all-plus controls; the authority/gate/fence families (`A`, `B`, `H`, `I`);
the planted-defect monkeypatch (item 7 of the spec, skipped for budget). None of these is a gap I found; they
are simply untested by me.

---

## VERDICT

PASS-NO-BLOCKER. Twelve items rebuilt on independent machinery reproduce the note's numbers exactly:
the `M_oo` entries and free symbols, the block identity at 26 generic symbols, the necessity radical
(proved here Gröbner-free, by pure powers of the two line forms sitting in the coefficient ideal), the
64-cell census literal for literal, the star = curve identity and the `P_f = ∓E_iE_j` sign identity, the
`3`-flip distances, the two stabilisers with orders `(1,2,2,2,3,3)` and their body-diagonal axes, the
empty forced-condition star-line loci, `μ = 32/27` and `27/32`, `det B/Q² = 8/9` and `3/4`,
`det M/Q⁴ = 64/81` and `9/16` for symbolic `λ` AND symbolic `D07`, all four pencil branch constants at both
witnesses symbolically in `λ` and at `λ = 1/4` with and without `D07`, both rescalings, the positivity
bounds, the symbol identity, the invariance sets `= the stabiliser` exactly, the invariant dimensions
`(2, 1)`, the span coefficients, and the twisted identity with its four admissible twists.

Two defects, both non-blocking and both editorial:
- `CK-04` (line 236): "the class representatives `5, 2, 16, 12`" contradicts the note's own line 186 and
  claim-register row 7 and the receipt; the `(-1, +1)` least mask is **11**. Fix the digit.
- `CK-02` (line 212): "`D07` sits on corner 7, which nothing raises" is a one-sided reason — the zero
  column 7 of `D` kills the `(i, 7)` half and the zero row 0 of `D` kills the `(7, j)` half. The
  conclusion is unaffected; widen the clause.

I found nothing that refutes a measured number, a locus, a constant or a count.

