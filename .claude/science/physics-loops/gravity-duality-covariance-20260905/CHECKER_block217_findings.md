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

## CK-04 — the union locus in `s` and the cone at masks 2 and 16 — CONFIRMS

Note lines 271-274, verbatim:

> `is exactly `(s)`: **the union locus is`
> ``s = 0`**, Block 214's all-plus statement now at the covariant cells; `det M``
> `has degree 4 in `s` and `det B = M_eo` is `s`-free (the `(s/4) P111` block is`
> `even–odd and `D` changes parity, so it never reaches `M_eo`).`

Note lines 290-292, verbatim:

> `at s = 0:    det M = det B^2,  det B = Q+ Q-,  two DISTINCT quadrics with RATIONAL coefficients (the sqrt 6 cancels), monic in kt^2:`
> `             Q+- = kt^2 + ky^2 + c_xx kx^2 -+ c_ty kt ky + (signs) c_1 (kt kx, kx ky),  the pair differing in the sign of the kt ky term alone;`
> `             pi0 = +1:  c_xx = 59701/57109,  c_1 = 24516/57109,  c_ty = 2988/57109      pi0 = -1:  64961/61889, 27664/61889, 2192/61889;`

Note lines 295-296, verbatim:

> `symbolic s:  det M(s) = P(s, kappa)^2 with P ONE irreducible polynomial over QQ(sqrt 6) of degree 2 in s and 4 in kappa, at all 10`
> `             witnesses: off s = 0 the pair MERGES into an irreducible quartic (squared); on s = 0 it splits into Q+ Q-.`

**What I computed.** `M = H(s) D(κ) + D(κ)^T H(s)` from my own fold and my own grade-raising `D`
(independently built; it agrees entry-for-entry with `b214.raising_matrix()`), `B = M_eo` the 4×4
even–odd block, determinants by `sympy`'s `berkowitz` (not `DomainMatrix`/`ff_det`), and the union
locus by taking the **gcd in `QQ(√6)[s]` of the κ-coefficients of `det M − det B²`** (a PID
computation, not a Groebner basis).

| | mask 2 (`π0 = +1`) | mask 16 (`π0 = −1`) |
| --- | --- | --- |
| `det B` free symbols | `kt, kx, ky` — **`s`-free** | **`s`-free** |
| `deg_s det M`, `deg_κ det M` | 4, 8 | 4, 8 |
| gcd of the coefficients of `det M − det B²` in `s` | `s²`, radical **`(s)`** | `s²`, radical **`(s)`** |
| `det M(0) = det B²` | True | True |
| `det B(0)` factor shape over `QQ(√6)` | two degree-2 factors, multiplicity 1 each | same |
| `Q±` monic-in-`kt²` `(c_xx, |c_tx|, |c_ty|, |c_xy|)` | **(59701/57109, 24516/57109, 2988/57109, 24516/57109)**, `c_yy = 1` | **(64961/61889, 27664/61889, 2192/61889, 27664/61889)**, `c_yy = 1` |
| `Q+ − Q−` | `−5976 kt ky/57109` — **the `kt ky` term alone** | `−4384 kt ky/61889` — **the `kt ky` term alone** |
| distinct / proportional to each other | distinct / **not** proportional | distinct / **not** proportional |
| either `Q±` proportional to the onsite `kᵀ G1 k` | **no** | **no** |
| `det B` proportional to `(kᵀ G1 k)²` | **no** — not one metric's cone | **no** |
| `det M(s)` factor shape `(deg_s, deg_κ, multiplicity)` | **`[(2, 4, 2)]`** — one factor squared | **`[(2, 4, 2)]`** |

The onsite quadrics I read off `b213.metric_candidates` at zero parameters:
`kᵀ G1 k = 9/8 kt² − 3/4 kt kx − 3/4 kt ky + 9/8 kx² − 3/4 kx ky + 9/8 ky²` (mask 2) and
`4/3 (kt² − kt kx + kt ky + kx² − kx ky + ky²)` (mask 16).

DISPOSITION: **CONFIRMS**, every declared coefficient exact, both classes.

## CK-04b — "a pair of distinct rational quadrics related by `ky → −ky`" — CORRECTS

Note line 50, verbatim (the paper's one-sentence summary):

> `quadrics** related by `ky → −ky`, proportional to neither the onsite `kᵀ G1 k``

**What I computed.** `Q+(kt, kx, −ky) − Q−(kt, kx, ky) ≠ 0` at **both** masks. The reason is
elementary and the note's own `N4` table states it correctly: the two quadrics differ in the
`kt ky` sign **alone**, while `ky → −ky` flips the `kt ky` **and** the `kx ky` term, and
`|c_xy| = 24516/57109 ≠ 0` (mask 2), `27664/61889 ≠ 0` (mask 16). No coordinate sign flip can relate
them, since each flip changes exactly two of the three cross terms.

DISPOSITION: **CORRECTS.** A wording defect in the one-sentence summary only. Line 291
("the pair differing in the sign of the `kt ky` term alone"), claim register line 450
("`Q+ Q−`, distinct, rational, `kt ky` sign") and the `N5` fence (line 539, "differing in the sign
of the kt ky term alone") are all correct and are what the runner gates
(`pair_differs_in_kt_ky_only`). Recommended fix: drop "related by `ky → −ky`" from line 50 or
replace it with "differing in the sign of the `kt ky` term alone". **No measured number changes; not
a blocker.**

## CK-05 — the (4,2,2) bench at mask 2 on the star line — CONFIRMS

Note line 320, verbatim:

> `| L+− (mask 2) | `λ⁸ · (55296λ⁴ − 388672λ³ + 698656λ² − 422145λ + 69984)²` (irreducible quartic) | `{0×8, 9/8×2, 16/11×2, 18/11×4}` | `{0×8, 36481/55296×4, 89401/55296×4}` | `{0×8, 1×8}` |`

Note lines 336-343, verbatim:

> `pencil bench charpoly is **exactly** `λ⁸` times the charpoly of`
> ``(H0⁻¹ M(e_t))²` — measured as a polynomial identity at the witness, the`
> `control and the flat cell. At the covariant witness that reads`
> ```text`
> `{9/8 x2, 16/11 x2, 18/11 x4} = G1_tt x {1, 128/99, 16/11, 16/11},   G1_tt = 9/8   (Block 216's four branch constants on the line at 1/4);`
> `the onsite cone at kappa = e_t is the NUMBER det M(e_t) = (64/81) G1_tt^4 (Block 216's c), never zero.`

**What I computed.** My own 16-site `(4,2,2)` bench: my own site indexing, my own periodic assembly
(aliases add), my own onsite and overlap rule dictionaries, my own lane raising rules (whose bench
matrix satisfies `dᴮᵀ = (dᵀ)ᴮ`, checked), `K = H d − dᵀ H`, form `= −K²`, pencil `= −(H⁻¹K)²`
(verified equal to `−(d − H⁻¹dᵀH)²` in every case), charpolys by `sympy Matrix.charpoly` over
`QQ(√6)`. Cell = mask 2 at L+−'s curve moduli, `(D07, D16, D25, D34) = (0, 1/4, −1/4, 1/4)`.

| reading | my multiset / factorization |
| --- | --- |
| onsite form | `λ⁸ (55296λ⁴ − 388672λ³ + 698656λ² − 422145λ + 69984)²` (as a monic charpoly: `/55296²`) — **matches** |
| onsite pencil | **`{0×8, 9/8×2, 16/11×2, 18/11×4}`** |
| overlap form | **`{0×8, 36481/55296×4, 89401/55296×4}`** |
| overlap pencil | **`{0×8, 1×8}`** |
| the same four at zero parameters | overlap form and pencil **identical** to the line point; onsite pencil moves to `{0×8, 9/8×2, 4/3×2, 3/2×4}` |
| `λ⁸ · charpoly((H0⁻¹M(e_t))²) == onsite pencil bench charpoly` | **True** (exact polynomial identity) |
| `charpoly((H0⁻¹M(e_t))²)` | `(8λ − 9)²(11λ − 18)⁴(11λ − 16)²/113379904` |
| `det M(e_t)`, `G1_tt`, `(64/81) G1_tt⁴` | **81/64**, **9/8**, **81/64** |
| `G1_tt × {1, 128/99, 16/11, 16/11}` | `{9/8, 16/11, 18/11, 18/11}` — matches the multiset |

**Bloch union = direct (the note's `F-2`), rebuilt independently.** My own bench momenta
`z ∈ {(1,1,1), (i,1,1)}` (from `exp(2πi m/N)`, `m < N/2`), my own 8×8 Bloch blocks, the product of
the two degree-8 charpolys against the direct degree-16 charpoly, over `QQ(√6, i)`:
**onsite form True, onsite pencil True, overlap form True, overlap pencil True.**

DISPOSITION: **CONFIRMS**, including the `κ = e_t` identity and the four-branch-constant reading.

## CK-07 — the two planted defects through the runner's `main()` — COULD NOT TEST (rule conflict)

The hard operating rules forbid importing, calling or copying the block runner
(`scripts/admissibility_dirac_kahler_overlap_assembly_covariant_cells_2026_09_05.py`); item 7 of the
attack list would require calling its `main()` in-process. I did not run it. The mutation census was
also out of scope by instruction (the supervisor verified the 29-mutation census from the raw
outputs). Every claim in the priority list was instead attacked with independent machinery above.

---

## Scope of the check, stated so it is not over-read

- Attacked at **masks 2 and 16 only** (one witness per rule-A class), plus the symbolic-signs fold
  lemma and Bloch-fold lemma, which are cell-independent and therefore cover all 8.
- **Not** re-measured: the other six rule-A cells' stabilisers and cones; the all-plus `W1` and flat
  controls (stabilisers, cone, bench); the census/star-pattern classification; the authority gate;
  the float/nsimplify gates; the mutation battery.
- Every value above was recomputed from scratch; none was read out of the receipt before computing.

## CK-08 — the two controls (all-plus `W1`, flat), loci and bench — CONFIRMS

Note lines 231-232, verbatim:

> `all-plus W1 control                strict: identity only; twisted: the full O for every s   (Block 215's F-2, at the fold)`
> `flat control                       strict: the D4_face for every s, the other 16 rotations at s = 0 only; twisted: O for every s`

Note lines 321-322, verbatim (the bench control rows):

> `| all-plus `W1` | `λ⁸ (129600λ⁴ − 647676λ³ + 1086353λ² − 711440λ + 147456)²` | `λ⁸ (15λ − 16)² · (4801335λ³ − 18293776λ² + 22913024λ − 9437184)²` | `{0×8, 116281/147456×4, 4844401/3686400×4}` = Block 214's | `{0×8, 1×8}` |`
> `| flat | `λ⁸ (4λ² − 9λ + 4)² (16λ² − 33λ + 16)²` (measured, not declared) | `{0×8, 1×2, 16/15×6}` | `{0×8, 1×8}` | `{0×8, 1×8}` |`

**What I computed** (same independent machinery, at the all-plus signs; `W1` moduli
`(v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4)` read from `b211.W1_MODULI`, flat `(1, 0, 1, 0)`; the three
`s` values with the parameters distributed):

| | `s = 0` | `s = 1/4` | `s = −1/3` |
| --- | --- | --- | --- |
| `W1` strict | `{identity}` | `{identity}` | `{identity}` |
| `W1` twisted | 24 (the full `O`, 4-fold axes `(1,0,0),(0,1,0),(0,0,1)`) | 24 | 24 |
| flat strict | **24 (all)** | **8 = `{0,1,2,3,20,21,22,23}`** (the `D4_face`) | **8** (the same `D4_face`) |
| flat twisted | 24 (`O`) | 24 | 24 |

so exactly "the other 16 rotations at `s = 0` only" at the flat cell; and at zero parameters the flat
onsite cell **is** `I` and the flat overlap fold **is** `I` (both checked as 8×8 identities).

Bench at the line point `(0, 1/4, −1/4, 1/4)`, my own `(4,2,2)`:

- `W1` onsite form `λ⁸ (129600λ⁴ − 647676λ³ + 1086353λ² − 711440λ + 147456)²` — **matches**;
- `W1` onsite pencil `λ⁸ (15λ − 16)² (4801335λ³ − 18293776λ² + 22913024λ − 9437184)²` — **matches**
  (irrational roots, so no multiset — the note's "not four rational constants" holds);
- `W1` overlap form `{0×8, 116281/147456×4, 4844401/3686400×4}`, overlap pencil `{0×8, 1×8}` — **match**;
- flat onsite form `λ⁸ (4λ² − 9λ + 4)² (16λ² − 33λ + 16)²`, onsite pencil `{0×8, 1×2, 16/15×6}`,
  overlap form and pencil `{0×8, 1×8}` — **all match**;
- the `κ = e_t` identity `λ⁸ · charpoly((H0⁻¹M(e_t))²) =` onsite pencil bench charpoly also holds at
  the `W1` control — **True**.

Also checked by inspection of the CK-01 literal at mask 2's signs `(1,1,1,1,−1,1)`: the face products
are `(P_tx, P_ty, P_xy) = (+, −, +)`, so the `tx` and `xy` couplings are both
`−(g0 v0 v1 + g1)/(4 v0)` and the `ty` coupling is `−(g0 v0 v1 − g1)/(4 v0)` — the note's
lines 235-238, and the reason the 4-fold that exchanges `tx` and `xy` and fixes `ty` is the one about
the `x` axis.

DISPOSITION: **CONFIRMS.**
