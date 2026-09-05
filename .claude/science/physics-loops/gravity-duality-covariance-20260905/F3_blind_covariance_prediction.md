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

Scripts backing every COMPUTED claim are in
`S = <scratch>/b215blind/`: `q1_star.py`, `q23_rotations.py`, `q34_twisted.py`,
`q3_refine.py`, `q3_cells.py`.

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
