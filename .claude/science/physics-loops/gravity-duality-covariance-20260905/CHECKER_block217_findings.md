CHECKER VERDICT: PASS-NO-BLOCKER

Every priority claim of block 217 that I could rebuild independently reproduced exactly — the fold
lemma at symbolic signs/moduli/parameters, the trivial strict and `D4_face` twisted stabilisers at
three values of `s`, the forced shear table and its curve values, the union locus `(s)`, the cone's
distinct rational quadrics with the declared coefficients, and the bench multisets with the
`κ = e_t` identity — with one WORDING DEFECT in the note's own one-sentence summary (line 50): the
measured pair of quadrics is NOT related by `ky → −ky`; it differs in the `kt ky` sign alone, exactly
as the note's own `N4` table (line 291) and claim register (line 450) say. No number is wrong.

Machinery: my own fold (an explicit 1/8-weighted average over the eight anchor placements), my own
grade-raising `D(κ)` and lane rules, my own 24 signed permutations, my own 16×16 bench assembly, my
own determinants (`berkowitz`) and charpolys (`sympy Matrix.charpoly` over `QQ(√6)`), my own
coefficient-gcd route for the union locus. Imported read-only and used only where the spec allows:
`b214.formal_cell`, `b215.corner_action`, `b213.metric_candidates`/`quadratic_form`,
`b216.curve_moduli`/`moduli_as_g` (as a cross-check on my hard-coded curve point).
The block's own runner was read but never imported, called or copied.

---

## CK-01 — the fold lemma at symbolic face signs, moduli and parameters — CONFIRMS

Note line 196, verbatim:

> `H0(D07, D16, D25, D34) = H0(s, 0, 0, 0) with s = D07 + D16 + D25 + D34,   at EVERY cell (Block 215's F-1, at symbolic signs);`

Note line 197, verbatim:

> `H0_eo = (s/4) P111,  P111 the unsigned complement permutation;  H0 is linear in s;`

Note lines 198-199, verbatim:

> `H0(s = 0) = h0 I + 2 h_f P_f summed over the three faces,   h0 = (v0 + 3 v1)(v0 v1 + 1)/(8 v0 v1) = (v0 + 3 v1 + 3/v0 + 1/v1)/8,`
> `            2 h_f = -(s_f0 g0 v0 v1 + s_f1 g1)/(4 v0)   on the four two-flip pairs of face f  (12 couplings, one magnitude per face),`

**What I computed.** With the six face signs, the four moduli and the four parameters all symbols, I
built the cell with `b214.formal_cell` and folded it MYSELF (average of the cell's rules over the
eight anchor placements at weight 1/8 — not the runner's `principal_part`), then:

| measurement | value |
| --- | --- |
| `H(D) − H(0) == ((D07+D16+D25+D34)/4) · P111` as an 8×8 identity | **True** |
| `H(0)` free symbols | `g0, g1, s_tx0, s_tx1, s_ty0, s_ty1, s_xy0, s_xy1, v0, v1` — **no parameter** |
| linear in `s` (every entry degree ≤ 1) | **True** |
| `P111` supported only in the even–odd blocks | **True** |
| `h0` two declared forms agree; every diagonal entry equals `h0` | **True**, `h0 = (v0+3v1)(v0v1+1)/(8 v0 v1)` |
| nonzero off-diagonal entries of `H(0)` | 24 ordered = **12 unordered pairs**, every one a two-flip pair |
| entries matching `−(s_f0 g0 v0 v1 + s_f1 g1)/(4 v0)` for their face | **24 of 24** |
| anomalies (nonzero at a 1- or 3-flip pair; zero at a two-flip pair; literal mismatch) | **none** |

DISPOSITION: **CONFIRMS.** The parameters enter only as their sum, only in the complement block, and
the `s = 0` fold is exactly `h0 I` plus the twelve declared couplings, one magnitude per face.

## CK-02 — the stabilisers by direct matrix equality at s = 0, 1/4, −1/3 — CONFIRMS

Note line 226, verbatim:

> `strict stabiliser (E = 1)          an S3_body, both shears alive         the identity alone -- at EVERY s, including s = 0`

Note lines 227-228, verbatim:

> `twisted stabiliser (64 sign vectors)   --                                a D4_face of order 8 about the x axis (0, 1, 0), for EVERY s`
> `                                                                          (no rotation forces s = 0; no rotation outside the D4 is feasible)`

Note lines 229-230, verbatim:

> `the S3_body inside the overlap's twisted stabiliser?                      NO, at every cell`
> `the two assemblies' common covariance                                     one twisted C2_edge (the D4 meets the S3 in {1, one 2-fold})`

**What I computed.** No symbolic-`s` classifier: three *numeric* folds per cell, at `s = 0`,
`s = 1/4` and `s = −1/3`, with the parameters **distributed** (`(1/8, 1/16, 1/16, 0)` and
`(−1/6, 1/12, −1/4, 0)`), which also re-tests CK-01 independently. Strict = `L H L^T = H`; twisted =
some `E` among the 64 sign vectors with `E L H L^T E = H`, tested entrywise on the pre-simplified
`L H L^T`. Masks 2 (signs `(1,1,1,1,−1,1)`, class `(1,−1)`, L+−'s moduli) and 16 (signs
`(1,−1,1,1,1,1)`, class `(−1,1)`, L−+'s moduli).

At **both masks and all three `s`**, identically:

- onsite strict stabiliser (zero parameters): 6 elements, orders `(1,2,2,2,3,3)` with the two 3-folds
  about a body diagonal — mask 2 `{0,7,11,12,16,23}` axes incl. `(1,1,1)`; mask 16 `{0,6,8,15,17,23}`
  axes incl. `(1,−1,1)`. An `S3_body`.
- **overlap strict stabiliser = `{identity}` at every `s`** (including `s = 0`).
- **overlap twisted stabiliser = `{0,1,2,3,20,21,22,23}`, 8 elements, orders `(1, 2,2,2,2,2, 4,4)`,
  the two 4-folds about `(0,1,0)` — a `D4_face` about the `x` axis — the SAME set at every `s`.**
- `S3_body ⊆ twisted`: **False**; intersection = `{identity, g23}` with `g23` of order 2 about the
  edge axis `(1,0,−1)` — **exactly one edge half-turn**, i.e. a `C2_edge`.

(My independent enumeration of the 24 rotations happens to index them in the runner's order, so the
element lists are directly comparable to the receipt's `strict_feasible`/`twisted_feasible`.)

**The structural claim (rechecked explicitly, as instructed).** With `s` symbolic:

- every one of the 24 lifts is **grade-preserving** (zero in every grade-off-diagonal position) —
  measured. Since `E` is diagonal, `supp(E L X L^T E) = supp(L X L^T)`, so the support statement is
  automatically uniform in the 64 sign vectors.
- `H0(0)` has **0** entries in the odd–even blocks (parity-preserving), and the `s`-part is
  `(s/4) P111`, supported **only** in the odd–even blocks.
- over all 24 rotations with `s` symbolic: entries of the residual carrying **both** a constant and
  an `s` term: **0**; `s`-part landing in a same-parity block: **0**; constant part landing in an
  odd–even block: **0**. Same at both masks.

DISPOSITION: **CONFIRMS**, including the supervisor's structural claim — no residual entry is
`a + b s` with both nonzero, so the runner's symbolic-`s` classifier cannot hide an `s` that is
forced by a cancellation.

## CK-03 — the shear relation at symbolic moduli, and the curve — CONFIRMS

Note lines 248-252, verbatim:

> `the two order-3 elements:       g0 = 0  AND  g1 = 0                                      (both shears killed)`
> `two of the order-2 elements:    g0 = 0, g1 = 0 and g0 v0 v1 + g1 = 0`
> `the third order-2 element:      g0 v0 v1 + g1 = 0  AND  g0 v0 v1 - g1 = 0                (hence g1 = 0, g0 v0 v1 = 0)`
> `                                                                                          -- identical at all 8 cells`
> `on the curve:  g0 v0 v1 + g1 = 3/4,  g0 v0 v1 - g1 = -1/4  (pi0 = +1, v0 v1 = 3/4);   7/9, 1/9  (pi0 = -1, v0 v1 = 8/9)`

**What I computed.** At mask 2's signs with `(g0, g1, v0, v1)` symbolic: the cell's own `S3_body`
(the strict stabiliser of the onsite cell, computed by direct matrix equality), then for each of its
elements `L H0(0) L^T − H0(0)`, every nonzero entry factored over `QQ`, keeping the factors that
carry a shear:

| element | order | forced factors |
| --- | :---: | --- |
| `g0` | 1 | — |
| `g7` | 2 | `g0`, `g0 v0 v1 + g1`, `g1` |
| `g11` | 2 | `g0`, `g0 v0 v1 + g1`, `g1` |
| `g12` | 3 | `g0`, `g1` |
| `g16` | 3 | `g0`, `g1` |
| `g23` | 2 | `g0 v0 v1 + g1`, `g0 v0 v1 − g1` |

On Block 213's curve, computed from my own hard-coded moduli (cross-checked against
`b216.curve_moduli`): `π0 = +1`: `(g0 v0 v1 + g1, g0 v0 v1 − g1, v0 v1) = (3/4, −1/4, 3/4)`;
`π0 = −1`: `(7/9, 1/9, 8/9)`.

DISPOSITION: **CONFIRMS.** The order-3 elements force `g0 = g1 = 0`, so no shear-alive strict locus
exists, and the curve violates every variant. The note's exact negative (lines 259-263) holds.

## CK-06 — the Bloch fold at z = (i, 1, 1) — CONFIRMS

Note lines 353-357, verbatim:

> `The identity fails for the form reading (`−K²` is not similarity-invariant under`
> `the Bloch phase) and for the overlap assembly, whose Bloch fold at`
> `z = (i, 1, 1) is **parameter-free** (at symbolic signs, moduli and`
> `parameters: the complement-pair phases `i^{±1}` cancel in the average) and`
> `differs from `H0(0)` in 16 entries — which is why the overlap bench does not`

**What I computed.** My own Bloch fold (the same 1/8 average with the phase `z^Δ`) at
`z = (i, 1, 1)` with everything symbolic: free symbols `g0, g1, s_xy0, s_xy1, v0, v1` — **no
parameter**, and in fact only the `xy` face survives. At the mask-2 witness with the curve moduli it
differs from `H0(0)` in **16** entries.

DISPOSITION: **CONFIRMS.**
