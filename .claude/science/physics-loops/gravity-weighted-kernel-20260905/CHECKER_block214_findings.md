# Refuting checker — Block 214 (third seat, independent machinery)

CHECKER VERDICT: FIX FIRST — every load-bearing claim I tested reproduces exactly on my own machinery, but the deformed-flat-cell quartic is printed with the wrong sign in three restatements (`Q = |k|⁴ + Q2_flat` should be `Q = |k|⁴ − Q2_flat`), one of them inside the byte-gated `N5` fence.

Checker seat: Opus 5, launched 2026-09-05T07:09Z, hard budget 55 min. All
computations below are my own sympy build of `D(kappa)`, `H0`, `M`, the parity
blocks, the congruence and the loci. The **only** objects taken from Block
213's landed runner are `formal_family`, `witness_table`, `locus_witness_table`,
`solve_witness` (i.e. Block 211's cell solver) and `bipartite_block` /
`metric_candidates` — used as inputs, never as the answer. Nothing of the Block
214 runner is imported, called or copied; it is read only for its literals.
Scratch: `.../scratchpad/b214check3/ck1.py`, `ck2.py`, `ck3.py`.

---

## CK-01 — the raising part `D(kappa)` and its zero row (CONFIRMS)

Note, `N1`, lines 164–166:

> `raising     D(kappa)[c, c + e_mu] = eta_mu(c) k_mu, Block 209's shadow: the twelve entries`
> `            D[1,0]=ky D[2,0]=kx D[4,0]=kt D[3,1]=kx D[3,2]=-ky D[5,1]=kt D[5,4]=-ky D[6,2]=kt`
> `            D[6,4]=-kx D[7,3]=kt D[7,5]=-kx D[7,6]=ky,  with D[0,:] = 0 and D[:,7] = 0.`

Computed: I rebuilt `D` from scratch — corners in `itertools.product((0,1),
repeat=3)` order `(t,x,y)`, `eta(c, mu) = (-1)^sum(c[:mu])`, entry `D[c, c⊕e_mu]
= eta(c,mu) k_mu` kept exactly when `grade(c) = grade(c⊕e_mu) + 1`. Machinery:
my own sympy loop (`ck1.py`).

Value: exactly the twelve entries listed, sign for sign
(`{(1,0):ky, (2,0):kx, (3,1):kx, (3,2):-ky, (4,0):kt, (5,1):kt, (5,4):-ky,
(6,2):kt, (6,4):-kx, (7,3):kt, (7,5):-kx, (7,6):ky}`), row 0 zero, column 7
zero. It also agrees entry for entry with the parent's own
`first_order_matrix(raising_rules(lane_rules(3)), 3, kappa)`. **CONFIRMS.**

## CK-02 — the free names sit where the note says they sit (CONFIRMS)

Note, `N1`, lines 160–163:

> `carriers    exactly the eight antidiagonal entries (0,7),(1,6),(2,5),(3,4) and transposes, in`
> `            Block 209's corner order 0=(0,0,0) 1=(0,0,1) 2=(0,1,0) 3=(0,1,1) 4=(1,0,0) 5=(1,0,1)`
> `            6=(1,1,0) 7=(1,1,1): D07 pairs grade 0 with grade 3; D16, D25, D34 pair a unit corner`
> `            (grade 1) with its complement (grade 2).`

Computed: `b211.solve_pinned(face_system(branch_moduli(*W1_MODULI, ALL_PLUS)),
at_zero=False)` — Block 211's own solve with the four names free — and read off
which matrix slots each free symbol occupies and with what coefficient.
Machinery: Block 211's landed solver (read as an input), my own occupancy scan.

Value: `{'D07': [(0,7,'D07'), (7,0,'D07')], 'D16': [(1,6,'D16'), (6,1,'D16')],
'D25': [(2,5,'D25'), (5,2,'D25')], 'D34': [(3,4,'D34'), (4,3,'D34')]}` — each
name occupies exactly its own antidiagonal pair, symmetrically, with
coefficient `+1` and appears nowhere else in the cell. The naming convention
the note asserts is Block 211's own. Grades: `(0,7)` is `0↔3`, and `(1,6)`,
`(2,5)`, `(3,4)` are each `1↔2`. **CONFIRMS.**

## CK-03 — the parity block identity: `M_eo`, `M_ee`, `M_oo` (CONFIRMS)

Note, `N2`, lines 199–203:

> ```text
> M_ee  =  [[0, u^T], [u, 0_3]],   u = ( (D07 + D34) kt,  (D25 - D07) kx,  (D07 + D16) ky )   on corners (3, 5, 6),
> M_oo  =  [[N, 0], [0, 0]],       N = [[0, (D16 + D25) kt, (D34 - D16) kx],
>                                       [(D16 + D25) kt, 0, -(D25 + D34) ky],
>                                       [(D34 - D16) kx, -(D25 + D34) ky, 0]]        on corners (1, 2, 4), corner 7 empty.
> ```

and line 171: `even/odd order (0; 3,5,6 | 1,2,4; 7): M = [[M_ee, B], [B^T, M_oo]], B parameter-free.`

Computed: `H0 = formal_family(ALL_PLUS, g0, g1, v0, v1)` (symbolic moduli
`v0, g0, v1, g1`, diagonal `(v0, v1, v1, 1/v0, v1, 1/v0, 1/v0, 1/v1)`,
cross-degree entries zero — verified) plus the four symbolic parameters added
to the eight antidiagonal slots; `M = H0 D + D^T H0`; split on
`EVEN = [0,3,5,6]`, `ODD = [1,2,4,7]`. Machinery: my own sympy build (`ck1.py`).

Values:
- `M` is symmetric: **True**.
- `M_eo` contains none of `D07, D16, D25, D34`: **True**, and it equals the
  parent's `bipartite_block(H0|_{params=0}, D, 3)[0]` entry for entry — so `B`
  is literally Block 213's `B`, unchanged.
- `M_ee` equals the claimed bordering **exactly**, sign for sign, including
  the minus in `(D25 − D07) kx`: **True**.
- `M_oo` equals the claimed zero-diagonal `N` with corner 7 empty **exactly**,
  including the minus in `−(D25 + D34) ky`: **True**.

The sign conventions in `u` and in `N` are correct as printed. **CONFIRMS.**

## CK-04 — the `D07` congruence (CONFIRMS)

Note, `N2`, lines 220–234:

> `With `U = I − (D07/D3) E₇₀` (unipotent, `det U = 1`):`
> ```text
> U^T M U   =  M |_{D07 = 0}                                        (exact, symbolic moduli),
> U^T H0 U  =  H0 |_{D07 = 0}  with  D0  ->  D0 - D07^2 / D3  =  v0 - D07^2 v1,   nothing else moved.
> ```
> `So `det M`, the cone and the signature of `M` are **independent of `D07`**`
> `... the Schur complement of the `{0, 7}` pair block`
> ``[[v0, a], [a, 1/v1]]`, positive exactly inside Block 211's bound `a² < v0/v1`.`

Computed at **symbolic moduli, symbolic all four parameters and symbolic
kappa** (`ck1.py`):
- `D3 = H0[7,7] = 1/v1`, `D0 = H0[0,0] = v0` — so the note's identification of
  `D3` as the top-form diagonal entry is right.
- `det U = 1`: **True**.
- `U^T M U − M|_{D07=0} = 0`: **True** (all 64 entries).
- `U^T H0 U − H0|_{D07=0, D0→D0−D07²/D3} = 0`: **True**, nothing else moved.
- `D0 − D07²/D3 = v0 − D07² v1`, which is `> 0` exactly when
  `D07² < v0/v1` — Block 211's bound, recovered on my machinery.

Consequence I derive rather than compute: since `det U = 1`, `det M =
det(U^T M U) = det(M|_{D07=0})`, so `det M` carries no `D07` **identically at
symbolic moduli** — a proof, stronger than a per-witness measurement.
**CONFIRMS.**

## CK-05 — the overlap fold sees only the sum (CONFIRMS)

Note, `N1` line 168–169 and `N2` lines 238–243:

> `assemblies  ... overlap: H0 = H0(0) + (s/4) P111, s = D07 + D16 + D25 + D34, P111 the Hodge-complement`
> `            permutation c -> c + (1,1,1) -- all eight parameter entries have the SAME step mod 2.`
> `... grade parity is preserved **iff `s = 0`**, and `M` depends on the four parameters only through `s``

Computed: I folded Block 105's overlap assembly by my own formula
`H0_ov[a,b] = (1/8) Σ_{i,j : c_i ⊕ c_j = c_a ⊕ c_b} cell[i,j]` (derived from the
rules, not by calling the parent's `overlap_rules`/`folded_matrix`), at symbolic
moduli and symbolic parameters.

Values: `H0_ov − H0_ov(0) − (s/4) P111 = 0` (all 64 entries); `H0_ov(0)` is
grade-parity preserving; the whole even↔odd block of `H0_ov` is the single value
`s/4` on the `P111` pattern and `0` elsewhere — so parity is preserved iff
`s = 0`. `M(overlap)` at `(D07,D16,D25,D34) = (t,0,0,0)`, `(0,t,0,0)` and
`(0,0,t/2,t/2)` are the same matrix entry for entry. **CONFIRMS.**

## CK-06 — the union locus at `W1`, by a route with no Gröbner basis (CONFIRMS)

Note, `N3`, lines 251–258:

> ``det [[A, B], [Bᵀ, C]]` with `B` square equals `det(B)²` whenever `A = 0` **or**`
> ``C = 0`, whatever the other diagonal block. Onsite, `M_oo ≡ 0` iff`
> ``D16 + D25 = D34 − D16 = D25 + D34 = 0`, i.e. on the plane `D16 = D34 = −D25``
> `(for every `D07`). That the plane is also **necessary** is measured: at `W1``
> `and at the two locus witnesses the ideal generated by the `κ`-coefficients of`
> ``det M − det B²` in `(D16, D25, D34)` has a lex Gröbner basis whose radical is`
> `exactly `(D16 − D34, D25 + D34)` — at `W1` the basis is`
> ``{(D16 − D34)², (D16 − D34)(D25 + D34), (D25 + D34)²}`.`

Computed at `W1` (`v0, g0, v1, g1 = 15/16, 1/4, 1, 1/4`, positive definite),
symbolic all four parameters, `det` by fraction-free Bareiss on a
`DomainMatrix` over `QQ[kt,kx,ky,D07,D16,D25,D34]`. **My necessity route is a
linear change of variables plus monomial support, not a Gröbner basis:** set
`a = D16 − D34`, `b = D25 + D34`, `c = D34` and inspect the `(a,b)`-support of
every `κ`-coefficient of `det M − det B²`.

Values:
- `det B` is parameter-free and equals
  `(8/45)(2kt² − kt kx − kt ky + 2kx² − kx ky + 2ky²)(3kt² − 2kt kx + 2kt ky + 3kx² − 2kx ky + 3ky²)`
  — the product of the two Hodge quadrics.
- `det M` contains **no** `D07` (independently proved in CK-04 from `det U = 1`).
- Sufficiency: `det M − det B² = 0` identically on `(D16,D25,D34) = (t,−t,t)`
  for symbolic `t` **and symbolic `D07`**; `M_oo = 0` there while `M_ee ≠ 0`
  there — so the note's use of the `C = 0` half of the block identity is the
  precise one, and `M_ee` is *not* claimed to vanish. I verified the block
  identity `det[[0,B],[Bᵀ,C]] = det(B)²` and `det[[A,B],[Bᵀ,0]] = det(B)²` at
  `n = 4` (sign `+`) on random rational `4 × 4` blocks.
- Necessity: `det M − det B²` has 36 nonzero `κ`-coefficients; in `(a,b)` their
  monomial support is `{(2,0),(1,1),(0,2),(2,2),(3,1),(1,3),(4,0),(0,4)}`, so
  the minimum total `(a,b)`-degree is **2** and the coefficient ideal is
  contained in `(a,b)² = (a², ab, b²)`. The matrix of the `(a², ab, b²)` parts
  has **rank 3**, so the ideal also contains `a², ab, b²`. Hence the coefficient
  ideal **is exactly** `((D16−D34)², (D16−D34)(D25+D34), (D25+D34)²)`, whose
  radical is `(D16−D34, D25+D34)` and whose zero set is exactly the plane.
  This reproduces the note's stated `W1` basis literally. **CONFIRMS.**

## CK-07 — the factorization type and `Q2` at `W1` (CONFIRMS, with one scale caveat)

Note, `N3`, lines 267–274:

> `At symbolic parameters, under both assemblies at `W1`,`
> ``det M = Q²` with `Q` a single irreducible factor over `QQ(parameters)` ...`
> `of total degree 4 in `κ` and of degree **exactly 2 and even** in the parameters: `Q = Q0 + Q2`, `Q0 = ±det B``
> `the degree-diagonal product of the two Hodge quadrics, `Q2` a quadratic form in`
> ``(D16, D25, D34)` ... At `W1`,`
> ``D16` alone: `Q = Q0 + D16² (6 kt² ky² − 3 kt kx ky² + 6 kx² ky²)`, the`
> `checker's quartic recovered.`

Computed: `sp.factor_list(det M)` at `W1`, symbolic parameters.

Values: `det M = (64/2025) · Q²` with **one** irreducible factor `Q`,
multiplicity 2, `κ`-degree 4, parameter-degree exactly 2, homogeneous of degree
2 in `(D16,D25,D34)` and free of `D07`. `Q − Q0` at `D16` alone is
`3 D16² ky² (2kt² − kt kx + 2kx²) = D16²(6 kt² ky² − 3 kt kx ky² + 6 kx² ky²)`
— the note's literal, exactly. **CONFIRMS.**

**Scale caveat (not a blocker).** With the primitive normalisation that makes
the `D16`-alone literal come out as printed, `Q0` is the *bare product* of the
two Hodge quadrics, i.e. `Q0 = ±(45/8) det B`, not `±det B`; the content `8/45`
is carried in the prefactor `64/2025 = (8/45)²`. The note's `Q0 = ±det B` is
therefore right up to that rational content, and its own parenthetical ("the
degree-diagonal product of the two Hodge quadrics") is the exact statement.
Optional wording only.

## CK-08 — the single-quadric fate (CONFIRMS)

Note, `N4`, lines 294–304 (`F-6`, `F-7`).

Computed by two routes, neither the primary's 15-coefficient lex basis in the
six entries of `G`:
1. `det M = (64/2025) Q²`, so `det M = (kᵀGk)⁴` forces `Q = ±(45/8)(kᵀGk)²`,
   i.e. `Q` must have a repeated factor. At `W1`, symbolic parameters,
   `gcd(∂Q/∂kt, ∂Q/∂kx, ∂Q/∂ky) = 1`, so `Q` is squarefree and no such `G`
   exists generically.
2. The residual system by back-substitution (normalise `q`'s `kt²` coefficient,
   read `g01,g02,g11,g12,g22` off the `kt³`/`kt²` coefficients, keep the nine
   remaining coefficients as conditions in the parameters) — result in the
   `ck4` block below.

At `L+−` (onsite): along the whole plane `(D16,D25,D34) = (s,−s,s)` with
symbolic `s`, `det M / (kᵀ G1 k)⁴ = 64/81`, a constant, independent of `s` —
Block 213's single-quadric cone persists on the plane for every `s`. At the
declared off-plane point `D16 = 1/4` the determinant is one irreducible quartic
squared with `gcd` of partials `= 1`, so it is **not** `(kᵀGk)⁴`. **CONFIRMS.**

## CK-09 — the branch constants `128/119` and `5/36` (CONFIRMS)

Note, `N4`, lines 323–326:

> `The `D07` rescaling is exact: at `L+−`, `v1/v0 = 9/8`, so`
> ``1/(1 − D07² v1/v0) = 128/119` at `D07 = 1/4`; `D07² = (v0/v1)(1 − 1/μ) = 5/36``
> `(inside the bound `v0/v1 = 8/9`) would tie the 0-form constant to the`
> `top-form constant `μ = 32/27`, ...`

Computed from `locus_witness_table()`'s moduli by my own pencil arithmetic:
at `L+−`, `(v0,g0,v1,g1) = (√6/3, 1/3, 3√6/8, 1/2)`, so `v1/v0 = 9/8`,
`v0/v1 = 8/9`, `D0 = √6/3`, `D3 = 4√6/9`, `D0 D3 = 8/9 = v0/v1`.
`G2 = μ G1` with `μ = 32/27` (solved as a single scalar over all nine entries).
Then `1/(1 − (1/4)²·9/8) = 1/(119/128) = **128/119**` and
`(v0/v1)(1 − 1/μ) = (8/9)(1 − 27/32) = (8/9)(5/32) = **5/36** < 8/9`.
Both literals exact. **CONFIRMS.**

*Extra, not a defect:* at `L−+` the same arithmetic gives `v1/v0 = 4/3`,
`μ = 27/32 < 1`, hence `(v0/v1)(1 − 1/μ) = −5/36 < 0` — no real `D07` ties the
two constants at `L−+`. The note claims the tuning only at `L+−`, so nothing is
overstated; worth recording because the note's `N4` sentence is easy to read as
symmetric in the two locus witnesses.

## CK-10 — the deformed flat cell: a SIGN that is wrong in three restatements (CORRECTS)

Note, `N4`, lines 339–341 (the primary statement, and it is **correct**):

> ```text
> det M_flat = Q_flat^2,   Q_flat = -|k|^4 + Q2_flat,   D07 absent,   Q2_flat = 0 exactly on the plane D16 = D34 = -D25,
> Q2_flat = D16^2 ky^2 (kt^2 + kx^2) + D25^2 kx^2 (kt^2 + ky^2) + D34^2 kt^2 (kx^2 + ky^2)
>           + 2 D16 D25 kx^2 ky^2 - 2 D16 D34 kt^2 ky^2 + 2 D25 D34 kt^2 kx^2;
> ```

Computed: the flat cell (`(c,v) = (0,1)`) solved through the parent is exactly
`I`; with the four parameters added, `det M_flat` is D07-free and

```text
det M_flat == (-|k|^4 + Q2_flat)^2   ->  True
det M_flat == (+|k|^4 - Q2_flat)^2   ->  True
det M_flat == (+|k|^4 + Q2_flat)^2   ->  False
```

with `Q2_flat` exactly the six-term expression printed at lines 340–341.
`Q2_flat` vanishes identically on the plane, and `det M_flat` on the plane and
at zero parameters is `(|k|⁴)²`. So `N4` line 339 is right.

**But three restatements carry the opposite sign**, and with `Q2_flat` defined
as at line 340 they are false as written:

- CLAIM REGISTER row 4, line 382: `` | 4 | deformed flat cell | `Q = |k|⁴ + Q2_flat`, `D07` absent, plane restores | `D` | ``
- the narrowest true statement, line 456: `` its `det M` is `Q²` with `Q = |k|⁴ + Q2`, `D07` absent, `Q = |k|⁴` restored on ``
- the byte-gated `N5` fence, line 583, `per_site`: `` with a parameter on it is NOT the identity: det M = Q^2, Q = |k|^4 + Q2, D07 absent, |k|^4 restored on the plane. ``

`Q` is defined only up to sign by `det M = Q²`, and flipping it gives
`|k|⁴ − Q2_flat`, **not** `|k|⁴ + Q2_flat`. The correct restatement is
`Q = |k|⁴ − Q2_flat` (equivalently `−|k|⁴ + Q2_flat`). Disposition:
**CORRECTS** — one sign, in three places, one of them inside the byte-gated
fence (so the runner's `N5_FENCE` literal has to move with it). No load-bearing
result changes: `det M_flat`, the `D07` absence and the plane restoration are
all exactly as measured.

## CK-11 — the single-quadric system is inconsistent, exactly (CONFIRMS)

Note, `N4`, lines 296–298 and the fence line 583:

> ``det M = (kᵀ G k)⁴` for some symmetric `G` — one metric's cone — is a`
> `polynomial system in the six entries of `G` and the parameters. Its lex`
> `Gröbner basis is `(1)` — **inconsistent over the algebraic closure** — at `W1``
> `under both assemblies (`F-6`, ...)`

Computed by back-substitution, not by the primary's system in the six `G`
entries: `det M = c Q²`, so `det M = (kᵀGk)⁴` forces `Q = ±√c⁻¹ (kᵀGk)²`; write
`Q = A(kt² + g01 kt kx + g02 kt ky + g11 kx² + g12 kx ky + g22 ky²)²` with
`A = ` the `kt⁴` coefficient (checked `= −6 ≠ 0` at `W1`), read the five `g`'s
off the `kt³`/`kt²` coefficients, and keep the **nine remaining** coefficients
as conditions in `(D16, D25, D34)`.

Values:
- `W1`, onsite, symbolic parameters: the lex Gröbner basis of the nine
  residuals in `(D16,D25,D34)` is `[1]` — inconsistent at **every** parameter
  point (and `Q` carries no `D07`, so all `D07` are covered).
- `W1`, **overlap**, symbolic parameters: `det M = c Q²` with one irreducible
  quartic, and `gcd(∂Q/∂kt, ∂Q/∂kx, ∂Q/∂ky) = 4`, a nonzero constant — `Q` is
  squarefree, so `det M` is never `(kᵀGk)⁴` under overlap either.
- `L+−`, `D16 = 1/4` (off the plane): the residuals include the nonzero
  constants `{2, −4, −4, 53}` — inconsistent.
- `L+−`, along the plane `(s, −s, s)` with symbolic `s`:
  `det M = (1/64)(3kt² − 2kt kx − 2kt ky + 3kx² − 2kx ky + 3ky²)⁴`, i.e. one
  quadric to the fourth for **every** `s`, and `det M / (kᵀ G1 k)⁴ = 64/81`
  exactly. Block 213's single-quadric cone persists on the whole plane and dies
  at the declared point off it. **CONFIRMS `F-6` and `F-7`.**

## CK-12 — the overlap union locus (CONFIRMS)

Note, `N3`, line 259: `` Overlap: the same ideal in `s` has radical `(s)`. ``

Computed at `W1`, overlap fold, symbolic parameters: `det B` is parameter-free;
`det M − det B²` vanishes identically at `s = 0`; substituting
`D07 = s − D16 − D25 − D34`, every `κ`-coefficient has `s`-degree support in
`{2, 4}`, so the coefficient ideal is exactly `(s²)` and its radical is `(s)`.
**CONFIRMS.**

## CK-13 — not tested (COULD NOT TEST, time)

- The `(4,2,2)` bench pencil multiset `{0 ×8, 1 ×6, 16/15 ×2}` at
  `D16 = 1/4` / `D07 = 1/4` on the deformed flat cell (note line 342), and the
  Bloch-union = direct-bench identity (`D-3`, `E`).
- The pencil branch tables of `N4` lines 314–321 other than the `128/119` and
  `5/36` constants (CK-09) — in particular "no algebraic branch" at
  `W1, D16 = 1/4` and the merged irreducible cubic on the plane point.
- The registration statements of `N4c` (lines 356–363), `G-1`/`G-2`.
- The two-quadric eliminant `s²` on the four declared slices (`F-8`, line 280).
  My CK-06/CK-11 results are consistent with it — the quartic is a product of
  two quadrics exactly on the plane, where `s`'s own vanishing is not the
  condition onsite — but I did not compute the eliminant itself.
- The two planted-defect monkeypatches (spec item 8): not attempted, no budget.

Nothing in the untested set is contradicted by anything I did compute.

---

## Summary

| item | what | disposition |
| --- | --- | --- |
| CK-01 | `D(κ)`'s twelve entries, zero row 0, zero column 7 | CONFIRMS |
| CK-02 | the four free names sit on `(0,7),(1,6),(2,5),(3,4)`, coefficient `+1` | CONFIRMS |
| CK-03 | `M_eo` parameter-free; `M_ee = [[0,uᵀ],[u,0]]`; `M_oo = [[N,0],[0,0]]`, all signs | CONFIRMS |
| CK-04 | `UᵀMU = M|₀`, `UᵀH0U = H0|₀` with `D0 → v0 − D07² v1`; bound `D07² < v0/v1` | CONFIRMS |
| CK-05 | overlap `H0 = H0(0) + (s/4)P₁₁₁`; `M` a function of `s` alone | CONFIRMS |
| CK-06 | union locus onsite = the plane, ideal exactly `(a², ab, b²)`, rank 3 | CONFIRMS |
| CK-07 | `det M = (64/2025)Q²`, `Q` irreducible, `Q2` even quadratic; `D16` literal | CONFIRMS |
| CK-08 | `Q` squarefree ⇒ no single metric's cone; plane at `L+−` persists | CONFIRMS |
| CK-09 | `v1/v0 = 9/8`, `μ = 32/27`, `128/119`, `D07² = 5/36 < 8/9` | CONFIRMS |
| CK-10 | flat: `Q = −\|k\|⁴ + Q2_flat` is right; `+Q2_flat` in 3 restatements is wrong | **CORRECTS** |
| CK-11 | single-quadric system inconsistent at `W1` under both assemblies | CONFIRMS |
| CK-12 | overlap union-locus ideal `(s²)`, radical `(s)` | CONFIRMS |
| CK-13 | bench multisets, branch tables, registration, `F-8` eliminant, planted defects | COULD NOT TEST (time) |

No claim I tested is refuted. The one required change before the PR is the
sign in CK-10, at note lines 382, 456 and 583 (the last is byte-gated, so the
runner's `N5_FENCE` literal moves with it).

**Housekeeping for the supervisor:** through my own path error I created a
stray untracked copy of an earlier draft of this file at
`/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/science/physics-loops/gravity-weighted-kernel-20260905/CHECKER_block214_findings.md`
(the MAIN checkout, not this worktree). My operating rules forbid me to run
`rm`, so it is still there; it is untracked and safe to delete, along with the
two directories it created.

Machinery: sympy 8×8 exact linear algebra, `DomainMatrix` fraction-free Bareiss
determinants over `QQ[κ, parameters]` and `QQ(√6)[…]`, `factor_list`, `gcd` of
partials, one `lex` Gröbner basis on my own nine residuals. No float, no
`nsimplify`, no numerical sampling anywhere.
