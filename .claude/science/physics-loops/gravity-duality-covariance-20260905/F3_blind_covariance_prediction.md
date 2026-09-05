# F3 — BLIND SEAT (Block 215): the covariance question, answered from the landed inputs alone

**Date:** 2026-09-05  **Seat:** sealed blind seat, independent of the primary seat.
**Budget:** 75 minutes.  **Type:** prediction note.

**Independence statement.** Nothing under
`.claude/science/physics-loops/gravity-duality-covariance-20260905/` was read except
`specs/block215_blind.md`; no file whose name contains `duality_covariance` /
`DUALITY_COVARIANCE` was read; no `REVIEW_HISTORY`/`HANDOFF`/`STATE` of any pack was
read. The only sources are the four listed inputs:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (all).
- Block 211 `ADMISSIBILITY_DIRAC_KAHLER_SIX_FACE_POSITIVITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-27.md`
  lines 146-330, 437-462.
- Block 214 `ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md`
  lines 102-289.
- `scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py`
  lines 802-870 and 1161-1200 (imported, not re-read elsewhere).

**Disclosure (leak, incidental and post-hoc).** The worktree is shared with the primary
seat. After every result below was already written and committed (commits
`1b19d418a7`, `b57f07fb8e`, `43e7985cb1`), a `git log --oneline` run to collect my own
commit shas showed one interleaved commit *subject line* of the primary seat's, which
mentions a subgroup census and a 64-cell scan. I read no file of theirs — in particular
not `scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py`, whose
name contains `duality_covariance` — and nothing below was written or changed after
seeing it. Recording it so the comparison can discount it.

Scripts backing every COMPUTED claim are in `S = <scratch>/b215blind/`:
`q1_star.py` (star and cross block), `q23_rotations.py` (representation, subgroups,
untwisted commutants), `q34_twisted.py` and `q3_refine.py` (twisted covariance, parameter
action), `q3_cells.py`, `q3_cells2.py`, `q34_extra.py` (all 64 sign cells), `q_union.py`
and `q_final.py` (`M_ee`/`M_oo` validation against Block 214 and the union locus). All
computations are exact (sympy, rationals and symbols; no floats anywhere).

---

## 0. Conventions, all fixed from the sources

**Corner order** (runner line 803, `itertools.product((0,1), repeat=3)` in `(t, x, y)`;
identical to Block 214 line 161):

```text
0=(0,0,0) 1=(0,0,1) 2=(0,1,0) 3=(0,1,1) 4=(1,0,0) 5=(1,0,1) 6=(1,1,0) 7=(1,1,1)
grades      0         1         1         2         1         2         2         3
```

Corner `c` is read as the basis form `e_c = dx^{mu_1} ^ ... ^ dx^{mu_k}` over the
directions `mu` with `c_mu = 1`, taken in the increasing order `(t, x, y) = (0, 1, 2)`.

**The staggering sign** (runner lines 822-826):
`eta(c, mu) = (-1)^(sum(c[:mu]))` — the parity of the coordinates *before* `mu`. This is
exactly the Koszul sign of inserting `dx^mu` into `e_{c\mu}`:
`dx^mu ^ e_{c\mu} = eta(c, mu) e_c`. Every sign below is built from this and nothing else.

**The raising part** (Block 214 lines 165-166), rebuilt from `eta` alone and verified
entry-for-entry against the twelve quoted entries, and against the runner's own
`raising_rules(lane_rules(3))` with `kappa_mu = i sin k_mu` (COMPUTED, `q1_star.py`):

```text
D(kappa)[c, c - e_mu] = eta(c, mu) k_mu   for c_mu = 1;   D[0,:] = 0, D[:,7] = 0.
D = left exterior multiplication by the 1-form kappa = kt dt + kx dx + ky dy.
```

**The cell form** (Block 211 lines 281-300), with the six face shears kept independent:

```text
H = D = [v0] (+) v1*M1 on (1,2,4) (+) M2/v0 on (3,5,6) (+) [1/v1],
M1 = [[1,-c_xy0,-c_ty0],[-c_xy0,1,-c_tx0],[-c_ty0,-c_tx0,1]],
M2 = [[1,-c_tx1,-c_ty1],[-c_tx1,1,-c_xy1],[-c_ty1,-c_xy1,1]],
plus a = D07 at (0,7) and X = [[0,0,b],[0,c,0],[d,0,0]] (rows 1,2,4; cols 3,5,6),
b = D16, c = D25, d = D34.
```

COMPUTED cross-check: this hand-built family with `c_f0 = g0, c_f1 = g1` equals the
runner's own `formal_family(b211.ALL_PLUS, g0, g1, v0, v1)` entry for entry
(`q23_rotations.py`). The all-plus class is the class in which Block 214's `M_ee`/`M_oo`
(lines 199-203) and its plane are stated, so every class-dependent statement below is
given in **the all-plus class** unless another class is named.

---

## Q1 — THE STAR

### The sign rule, derived from `eta`

Define `sigma(c)` by `e_c ^ e_chat = sigma(c) e_7`, where `chat = c + (1,1,1) mod 2`. Built
by inserting the directions of `c` one at a time into `e_chat`, each insertion
contributing exactly one factor `eta(., mu)` — so the rule is a consequence of the lane's
`eta` and of the orientation `vol = dt ^ dx ^ dy`, with no new convention. COMPUTED
(`q1_star.py`), in corner order `0..7`:

```text
sigma = ( +1, +1, -1, +1, +1, -1, +1, +1 )
Star e_c = sigma(c) e_chat,   Star = Star^T,   Star^2 = I  (all COMPUTED).
```

`Star` is the Hodge star of the cube complex: the unsigned Hodge-complement permutation
`P111` of Block 214 line 169 is `Star` with the orientation signs stripped,
`P111 = Star . diag(sigma)`.

**The co-differential check (PROVED by computation, `q23_rotations.py`).** With
`Gamma = diag((-1)^grade(c))`,

```text
Star D(kappa) Star  =  Gamma D(kappa)^T  =  - D(kappa)^T Gamma      (exact, 8 x 8).
```

So `Star` is precisely the star that turns the raising part into the adjoint/lowering part
`D^T` up to the grade sign: on `p`-forms, `Star D Star = (-1)^(p-1) D^T`. That fixes
`Star` uniquely up to an overall sign (the orientation choice); the overall sign does not
enter any conclusion below.

### The 1-form -> 2-form block

Restricted to corners `(1, 2, 4) -> (6, 5, 3)`:

```text
Star dy = Star e_1 = + e_6,     Star dx = Star e_2 = - e_5,     Star dt = Star e_4 = + e_3.
sign pattern  ( +, -, + )  on (1->6, 2->5, 4->3).
```

Laid out in the block layout of `X` (rows corners `1,2,4`; columns corners `3,5,6`) the
star block is

```text
Star_{1->2} = [[0,0,1],[0,-1,0],[1,0,0]]      (the same matrix in either transposition).
```

### The answer

**YES — and exactly.** COMPUTED (`q1_star.py`): the unique solution of
`X = lam * Star_{1->2}` is

```text
b = lam,   c = -lam,   d = lam        i.e.   D16 = D34 = -D25,
```

which is **verbatim Block 214's union locus plane** (line 253: "the plane
`D16 = D34 = -D25` (for every `D07`)"). The cross block `X` is a scalar multiple of the
Hodge star of the cube complex **iff** `b = d = -c`. No different plane arises: the sign
pattern `(+, -, +)` is forced by `eta` and the orientation, and it matches the plane's
`(+, -, +)` pattern in `(D16, D25, D34)`.

*Extension to the full 8 x 8 (COMPUTED).* `sigma(0) = sigma(7) = +1`, so the full star
line in the four parameters is `(a, b, c, d) = lam (1, 1, -1, 1)`; the plane
`D16 = D34 = -D25` is exactly that line with `D07` released. On the full star line
`s = a + b + c + d = 2 lam`, which vanishes only at `lam = 0` — see Q4.

**Status: PROVED** (sign rule derived from `eta`; the identification `X = lam Star`
is a two-line linear solve, re-run symbolically).

---

## Q2 — THE ROTATIONS

### The representation

The Lattice axiom supplies "proper cubic rotations about each site"
(`MINIMAL_AXIOMS_2026-06-29.md` line 38). A proper cubic rotation is a signed permutation
matrix `A` of the three directions `(t, x, y)` with `det A = +1` (COMPUTED: there are
exactly 24). Its action on the corner basis is the exterior power,

```text
rho(A)[c', c] = det( A[rows of c', cols of c] )      (0 unless grade(c') = grade(c)),
```

which is exactly "signs from the wedge/orientation of each corner's degree": `rho` is the
unique extension of `A` to `Lambda(R^3) = R^8` as an algebra map.

COMPUTED verifications (`q23_rotations.py`), all True:

```text
24 distinct matrices;  closed under multiplication;  orders 1/2/3/4 with counts 1/9/8/6;
rho orthogonal (signed permutation);  rho grade-preserving;
rho(A) D(kappa) rho(A)^{-1} = D(A kappa)   for all 24  (the required intertwining);
rho(A) Star rho(A)^{-1} = Star             for all 24  (the star is equivariant);
rho(A) P111 rho(A)^{-1} = P111             for only  8  of 24.
```

The intertwining is also PROVED structurally: `D(kappa)` is left multiplication by the
1-form `kappa` in `Lambda(R^3)`, and `rho` is an algebra automorphism, so
`rho(kappa ^ w) = (A kappa) ^ rho(w)`.

### Covariance of the cell form

`R H R^T = H` with `R = rho(A)` orthogonal is the statement that `H` lies in the commutant
of the representation. COMPUTED for all **11 conjugacy classes of subgroups** (30 subgroups
found, matching `S_4`), giving both the dimension of the commutant in `Sym(8)` (36
unknowns) and the conditions inside the family.

| subgroup (order, type) | #conj | dim commutant in `Sym(8)` | forced on the six shears | forced on `(a,b,c,d)` |
| --- | :---: | :---: | --- | --- |
| `1` | 1 | 36 | none | none |
| `C2` face-180 | 3 | 20 | `c_tx0=c_ty0=c_tx1=c_ty1=0` | none |
| `C2` edge-180 | 6 | 20 | `c_ty0=c_xy0`, `c_ty1=-c_xy1` | `D25 = -D34` |
| `C3` body-diagonal | 4 | 14 | `c_tx0=c_xy0, c_ty0=-c_xy0; c_tx1=c_ty1=c_xy1` | **`D16=D34=-D25`** |
| `V4` (three face-180s) | 1 | 12 | **all six = 0 (flat)** | none |
| `V4` (two edge + one face) | 3 | 12 | `c_tx0=c_ty0=c_tx1=c_ty1=0` | `D16 = -D25` |
| `C4` face-axis | 3 | 14 | **all six = 0 (flat)** | `D16 = -D25` |
| `S3 = D3` body-diagonal | 4 | 9 | `c_tx0=-c_xy0, c_ty0=c_xy0; c_tx1=-c_xy1, c_ty1=-c_xy1` | **`D16=D34=-D25`** |
| `D4` face-axis | 3 | 9 | **all six = 0 (flat)** | `D16 = -D25` |
| `A4 = T` | 1 | 6 | **all six = 0 (flat)** | **`D16=D34=-D25`** |
| `O` (all 24) | 1 | 6 | **all six = 0 (flat)** | **`D16=D34=-D25`** |

(The shear conditions are stated for the computed class representative; conjugating the
subgroup permutes the direction labels and hence the sign pattern. Magnitudes are never
constrained to differ within an offset, so every entry above is a genuine family point.)

### The four answers

1. **Full group `O`.** `R H R^T = H` for all 24 forces (i) the plane
   `D16 = D34 = -D25`, i.e. `X = gamma Star` — *the same line as Q1*; (ii) `g0 = g1 = 0`,
   the **flat cell** (with Block 211's ties A/B this pins `v0 = v1 = 1`); (iii) nothing on
   the diagonal moduli beyond what the family already imposes. The commutant is
   6-dimensional: `[[D0, a],[a, D3]]` on `{0,7}`, `alpha I` on `Lambda^1`, `beta I` on
   `Lambda^2`, `gamma Star` across — exactly Schur's lemma for
   `Lambda = 1 (+) V (+) V (+) 1` with `V` the 3-dimensional vector irrep. **PROVED**
   (structural, plus COMPUTED).
2. **Which subgroups force the plane?** Exactly those containing a 3-fold (body-diagonal)
   axis: `C3`, `S3`, `A4`, `O`. Every subgroup with no order-3 element leaves at least one
   parameter free of the plane relation (`D4`, `C4` and the non-normal `V4` force only
   `D16 = -D25`; the edge `C2` only `D25 = -D34`; the normal `V4` and the face `C2` force
   nothing at all on the parameters). **COMPUTED.**
3. **Which force `D16 = D25 = D34 = 0`? NONE.** **PROVED:** `Star` commutes with all 24
   `rho(A)` (COMPUTED above, and structurally because `det A = +1`), so the star line
   `(b, c, d) = lam(1, -1, 1)` is covariant under the *whole* group; no subgroup of proper
   rotations can force the three grade-1/2 parameters to vanish. Only an improper element
   can: for the inversion `rho(-I) = Gamma = diag((-1)^grade)`, `Gamma H Gamma = H` forces
   every odd-parity entry to vanish, i.e. **`D07 = D16 = D25 = D34 = 0`**. The Lattice
   axiom supplies proper rotations only (line 38), so parity is not available.
4. **Is `D07` ever constrained? NO — never, by any proper rotation.** **PROVED:** `rho(A)`
   acts on corner 0 by `+1` and on corner 7 by `det A = +1`, so the `(0,7)` entry is a
   rotation invariant, for every subgroup including `O`. `D07` is the pseudoscalar
   pairing; it is odd under parity and even under every proper rotation. (This is the
   representation-theoretic counterpart of Block 214's congruence result at lines 220-234,
   where `D07` also drops out of `det M`, the cone and the signature.)

### Convention validation (this is what makes the rest quotable)

Rebuilding `M = H D(kappa) + D(kappa)^T H` from `eta` alone, at symbolic moduli and
symbolic parameters in the all-plus class, reproduces Block 214's measured blocks
**exactly** (COMPUTED, `q_union.py`), in its even/odd order `(0; 3,5,6 | 1,2,4; 7)`:

```text
M_ee = [[0, u^T],[u, 0]],  u = ( (D07+D34) kt, (D25-D07) kx, (D07+D16) ky )   [line 200]
M_oo = [[N, 0],[0, 0]],    N = [[0,(D16+D25)kt,(D34-D16)kx],
                                [(D16+D25)kt,0,-(D25+D34)ky],
                                [(D34-D16)kx,-(D25+D34)ky,0]]                 [lines 201-203]
M_eo = B is parameter-free                                                    [line 189]
```

so the corner order, the `eta` signs, the raising part and the family are all in the
lane's conventions, and nothing below rests on a re-invented sign.

Two further COMPUTED facts used later: `M_oo` contains no shear at all, so the union locus
`M_oo = 0` is **the same plane `D16 = D34 = -D25` in all 64 sign cells**; and
`Gamma P111 Gamma = -P111` while `Gamma H0(0) Gamma = H0(0)`.

---

## Q3 — TWISTED COVARIANCE

Twisted covariance: for each rotation there is a corner-sign gauge `E_R = diag(+-1)` with
`rho(R) H rho(R)^T = E_R H E_R`, i.e. `(E_R rho(R)) H (E_R rho(R))^T = H`.

**Lemma 1 (PROVED).** The set of rotations admitting some `E_R` is a subgroup: if
`rho(R1) H rho(R1)^T = E1 H E1` and likewise for `R2`, then, using that a signed
permutation conjugates a diagonal sign matrix to another diagonal sign matrix
(`rho E rho^T = E^pi`), `rho(R1R2) H rho(R1R2)^T = (E2' E1) H (E1 E2')` with
`E2' = rho(R1) E2 rho(R1)^T`. So the question is decidable rotation by rotation.

**Lemma 2 (PROVED).** Twisted covariance is a gauge invariant: for `H' = E H E`,
`rho H' rho^T = E^pi (E_R H E_R) E^pi = (E^pi E_R E) H' (E E_R E^pi)`. Gauge-equivalent
cells therefore have gauge-equivalent answers.

**Lemma 3 (PROVED).** If `g0 != 0`, the three `Lambda^1` off-diagonal entries all have
magnitude `v1 |g0|`, so the twisted condition on that block forces `e_{pi(i)} eps_i = f1`
(one global sign), i.e.

```text
E_R rho(R) restricted to Lambda^1 = f1 * (unsigned permutation of the axes),
```

and likewise `f2 * P` on `Lambda^2`. **The gauge exactly strips the orientation signs of
the rotation.** That is why curvature can survive.

### Do the shears survive full-`O` twisted covariance? **YES.**

COMPUTED (`q34_twisted.py`, `q3_cells.py`; 24 rotations x 256 gauges x all 64 sign cells,
exact): with `D07 = D16 = D25 = D34 = 0`, **all 24** rotations are twisted-covariant for
**every** curved family point in **every** one of the 64 shear-sign cells. A curved cell is
therefore never excluded by covariance-up-to-gauge. This is the exact counterpart of Block
211 lines 239-242 ("the individual signs are therefore not content"); relatedly PROVED:
the product of the three off-diagonal entries of a degree block is invariant under both
`rho` (the sign factors multiply to `(eps_1 eps_2 eps_4)^2 = 1`) and `E`, so Block 211's
class labels `(pi0, pi1)` are rotation invariants.

### With the parameters on, the twisted locus is the star line, up to gauge

COMPUTED (`q3_cells.py`, exact, all 64 cells): with `g0, g1` generic and nonzero, the locus
of `(D07, D16, D25, D34)` twisted-covariant under **all 24** rotations is, in each cell,
exactly one 2-plane:

```text
|D16| = |D25| = |D34|,   D07 free,
signs:  D16 = s_b D34,  D25 = s_c D34,
        s_b = s_xy0 s_tx0 s_tx1 s_xy1,   s_c = s_xy0 s_ty0 s_ty1 s_xy1.
```

In the **all-plus** cell that reads `D16 = D25 = D34`; each of the four sign patterns
occurs in exactly 16 cells. By Lemma 2, and because the pattern is the gauge image of
`(+, -, +)`, this locus is **the corner-sign-gauge orbit of the Hodge star line of Q1**:

> **TWISTED FULL-`O` COVARIANCE OF A CURVED CELL <=> THE CROSS BLOCK IS THE HODGE STAR, UP
> TO SCALE AND UP TO THE CORNER-SIGN GAUGE. `D07` STAYS FREE.**

### The largest subgroup under which a curved cell survives *untwisted*

COMPUTED (`q3_cells2.py`, all 64 cells x 24 rotations, exact): the untwisted stabiliser of
a curved family point is

```text
order 6  (S3 = D3: element orders 1,2,2,2,3,3)   in exactly 16 of the 64 sign cells,
order 2                                          in the other 48,
```

unchanged when the parameters are put on the star line. So **the largest subgroup under
which a curved cell survives untwisted covariance is the trigonal `D3` of order 6 about a
cube body diagonal** — never `D4`, `A4` or `O`, which all force `g0 = g1 = 0` (Q2 table).
The 16 trigonal cells are distributed **4 in each of Block 211's four gauge classes
`(pi0, pi1)`** (COMPUTED), so every gauge class contains such a point. What that subgroup
forces on the four parameters (Q2 table, `S3` row):

```text
D16 = D34 = -D25   (Block 214's union-locus plane),   D07 free.
```

And the sharpest cross-check in this block (COMPUTED, `q_union.py` + `q_final.py`):

> **THE 16 SIGN CELLS WHOSE CURVED POINTS CARRY THE ORDER-6 TRIGONAL STABILISER ARE
> *EXACTLY* THE 16 SIGN CELLS IN WHICH THE FULL-`O` TWISTED-COVARIANCE LOCUS COINCIDES
> WITH BLOCK 214's UNION-LOCUS PLANE `D16 = D34 = -D25`. THE TWO SETS ARE IDENTICAL,
> 16 = 16, 4 PER GAUGE CLASS.**

In the other 48 cells (the all-plus cell among them) the twisted locus and the union plane
meet only at `D16 = D25 = D34 = 0`, Block 213's degree-diagonal slice.

---

## Q4 — THE OVERLAP SUM

### `s` is *not* a rotation invariant

COMPUTED (`q34_twisted.py`): each `rho(R)` induces a signed permutation of
`(D07, D16, D25, D34)` (the antidiagonal positions map to antidiagonal positions because
corner complementation commutes with the corner permutation). The space of
rotation-invariant linear functionals of the four parameters is exactly **two**-dimensional:

```text
invariants:   D07        and        D16 - D25 + D34.
s = D07 + D16 + D25 + D34  is changed by 16 of the 24 rotations
(e.g. the axis transposition x <-> y:  s -> D07 - D16 - D25 + D34).
```

The second invariant is the trace of the star-transported cross block
`T = X . Star in End(Lambda^1)`, which is `T = diag(D34, -D25, D16)` in axis order
`(t, x, y)`; `X = lam Star` is exactly `T = lam I`. So the covariant content of the cross
block is `tr T`, not `s`. **The premise of the question fails: `s` is not protected.**

### Rotation covariance of the fold *does* force `s = 0`

COMPUTED: `rho(R) P111 rho(R)^T = P111` for only **8** of the 24 rotations, and those 8 are
exactly the `D4` fixing the `x` axis — the *middle* coordinate of the corner order. `P111`
is not a covariant object; the covariant Hodge-complement operator is `Star` (equivariant
under all 24, COMPUTED), and `P111 = Star . diag(sigma)` differs from it exactly by the
orientation signs.

**PROVED.** In `H0 = H0(0) + (s/4) P111` the parameter-free part `H0(0)` is
grade-block-diagonal, so it has no entry in any antidiagonal position; the mismatch
`rho P111 rho^T - P111` lives entirely in those positions and cannot be cancelled.
Therefore, for any rotation outside that `D4`,

```text
rho H0 rho^T = H0   =>   s = 0.
```

Rotation covariance of the folded overlap form forces `s = 0` on its own — a second and
weaker-hypothesis route to Block 214's `s = 0` locus (line 259: "Overlap: the same ideal in
`s` has radical `(s)`").

### The principle that forces `s = 0`, stated exactly

Let `Gamma = diag((-1)^grade(c))` be the grade-parity involution. Then (COMPUTED):

```text
Gamma H0(0) Gamma = H0(0),     Gamma P111 Gamma = -P111,
so   Gamma H0 Gamma = H0   <=>   s = 0.
```

**The principle is: the folded overlap form preserves grade parity — it is block diagonal
for `Lambda^even (+) Lambda^odd`, equivalently it commutes with `Gamma`.** Two exact
remarks:

1. `Gamma = rho(-I)` is precisely the exterior-algebra action of the **lattice inversion**
   `x -> -x`. Grade-parity preservation of the fold *is* covariance under inversion. The
   Lattice axiom names "proper cubic rotations" only (`MINIMAL_AXIOMS_2026-06-29.md`
   line 38), so inversion is **not supplied**, and nothing in the inputs forces `s = 0` by
   parity. (PROVED, from the axiom text.)
2. Under the **onsite** assembly (`H0 = D` exactly, Block 214 line 167) the same principle
   is strictly stronger: `Gamma H0 Gamma = H0` forces `D07 = D16 = D25 = D34 = 0` — the
   whole degree-diagonal slice, not just `s = 0`. The overlap fold sees the parameters only
   through `s` (Block 214 lines 238-243), which is why one assembly gives a 4-condition and
   the other a 1-condition version of the same principle.

On the star line `(D16, D25, D34) = lam(1, -1, 1)`, `s = D07 + lam`: Q2's covariant locus
does **not** force `s = 0`; only the fold's own covariance, or parity, does.

---

## Q5 — THE PRINCIPLE

### The covariance clause, verbatim

`docs/MINIMAL_AXIOMS_2026-06-29.md`, Admissibility / Local Constraint, lines 56-57:

> "There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations."

and the sentence it governs, lines 59-61:

> "For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions."

### What the clause attaches to

The clause is about **the rule** — a map from nearest-neighbour conditions to a probability
distribution on the one-site domain `M_2(C)`. It is not about any matrix. Three separate
things would have to be **supplied** before the cell form `H` could inherit it:

1. **An identification bridge.** A retained derivation identifying `H` (or the pencil
   `(M, H0)`) with content of that rule. Nothing in the inputs does this: Block 214's own
   charter says (line 139) "Every object below is an **imposed measured object** of the
   landed chain, read through its own runner", and the axiom memo says explicitly that
   Admissibility "does not ... choose a Hamiltonian or transfer operator, supply
   transition-probability or weight values" (lines 118-121). A weight is exactly what `H`
   is. **NOT SUPPLIED.**
2. **An action on the eight corners.** The Lattice axiom supplies rotations of `Z^3`
   (line 38); it does not supply an action on the corner index. Q2's `rho` is the exterior
   power, and it is the *unique* choice that intertwines the imposed raising part
   (`rho D(kappa) rho^-1 = D(R kappa)`, COMPUTED) — but that uniqueness is a property of
   the imposed kernel, not of the axiom. Reading the corner index as a form index is itself
   a bridge. **NOT SUPPLIED** (though pinned by the lane's own construction, which is why
   Q2's answer is stable).
3. **An action on the conditions.** Covariance of a rule is
   `rule(R . condition) = R . rule(condition)`; **invariance** `R H R^T = H` of a single
   form follows only for conditions fixed by `R`. So one needs the rotation action on the
   nearest-neighbour conditions (which moduli/sign data `R` produces). **NOT SUPPLIED.**

**The one thing the inputs do let me say about item 3 (PROVED).** Block 211's variety is
*per-offset isotropic* (line 214-215: "the six-face-compatible moduli variety is exactly
the per-offset-isotropic family"), so the conditions carry no direction labels except the
six shear signs, whose content is only `(pi0, pi1)` (Block 211 lines 239-242) — and
`(pi0, pi1)` is rotation invariant (Q3, PROVED). **If** the natural action is used, every
rotation therefore fixes every condition of the family, and covariance-of-the-rule
collapses to *invariance up to the corner-sign gauge* of each cell form — precisely Q3's
twisted covariance, not Q2's untwisted covariance. That is the sharpest statement the
inputs support, and it is conditional on items 1-3.

### Classification

**OPEN / NOT SUPPLIED — a bridge obligation, not a theorem.** It is exactly the case the
axiom memo's Qualification names (lines 86-89): "Further physical structure requires a
retained derivation or bridge, or explicit approved-primitive registration, before use as
a premise. A choice not fixed by the supplied structure remains a named conditional or open
dependency." I do not decide it. I note only that it is *decidable in either direction by
supplying item 1 alone*, and that the two available readings give different answers:

```text
reading A  (H must be rotation-INVARIANT):        flat cell, X = gamma Star, D07 free.
reading B  (H must be invariant UP TO GAUGE):     any curved cell, X = Star up to gauge
                                                  and scale, D07 free.
neither reading constrains D07; only parity (not supplied) does.
```

### One corollary worth recording (PROVED)

If `rho H rho^T = H` then `M(R kappa) = rho M(kappa) rho^T`, because
`rho D(kappa) rho^T = D(R kappa)`. Hence for a covariant cell form the principal part's
`det M`, its factorization type and its cone are **cubic-rotation-invariant functions of
`kappa`**. Block 214's off-plane quartic at `W1` with `D16` alone (line 274),
`6 kt^2 ky^2 - 3 kt kx ky^2 + 6 kx^2 ky^2`, is manifestly not such a function (it carries
`kt kx ky^2` and no `ky^4`), which is consistent: that slice is off both covariance loci.

---

## SUMMARY OF PREDICTIONS

```text
Q1  star signs sigma = (+,+,-,+,+,-,+,+); 1-form block (+,-,+);
    X = lam Star  <=>  D16 = D34 = -D25.  The star line IS Block 214's plane.  PROVED.
Q2  rho = exterior power; 24, closed, orders 1/9/8/6, intertwines D.  Full O forces the
    flat cell AND the plane; the plane is forced by exactly the subgroups with a 3-fold
    axis (C3, S3, A4, O); nothing forces D16=D25=D34=0; D07 is never constrained.
Q3  curvature survives full-O twisted covariance for every sign cell; with parameters on,
    the twisted locus is the gauge orbit of the star line (all-plus: D16=D25=D34).
    Largest untwisted subgroup with curvature = trigonal D3, order 6, in 16 of 64 cells,
    and it forces exactly the plane.  Those 16 cells = the cells where twisted locus =
    union plane.
Q4  s is NOT invariant (invariants: D07 and D16-D25+D34); P111 is covariant under only 8
    of 24; rotation covariance of the folded overlap forces s = 0; the exact principle is
    Gamma H0 Gamma = H0 with Gamma = diag((-1)^grade) = rho(-I), i.e. inversion covariance,
    which the Lattice axiom does not supply.
Q5  the clause governs the RULE; three items (identification bridge, corner action,
    condition action) would have to be supplied; none is.  OPEN / NOT SUPPLIED.
```

## COULD NOT TEST / declared dependencies

- **Q4 depends on one property of `H0(0)` I could not read**: that the parameter-free
  overlap fold has no entry in the four antidiagonal positions (it is how Block 214 writes
  the fold at lines 168-169 — all parameter content sits in `P111`). If `H0(0)` did carry a
  parameter-free antidiagonal part `A0`, covariance would read
  `rho(A0 + (s/4)P111) rho^T = A0 + (s/4)P111` and would fix `s` to some constant rather
  than necessarily `0`. Stated as a dependency, not paraphrased away.
- I did not compute the covariance of the *pencil branches*, the coincidence locus, or the
  positivity region under rotations; nothing here touches Block 211's `N3`/`N4` bounds.
- I did not enumerate improper elements beyond the inversion `Gamma`; since
  `O_h = O x {1, -I}`, that is complete for the full cubic group (`O_h` covariance =
  Q2's `O` answer plus `Gamma`, which kills all four parameters).
- No claim is made about which reading (A or B of Q5) the lane should adopt.
