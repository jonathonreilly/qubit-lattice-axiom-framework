---
title: "Admissibility — Dirac-Kähler Transfer-Package `(m, c)` Generality: The Split Theorem"
date: 2026-08-25
block: 194
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_transfer_package_mc_generality_2026_08_25.py
parent_ref: origin/physics-loop/toe-axiom-closure-block193-parity-window-intertwining-law-20260825
parent_commit: 37a5f926c9e15745faaffda66b308f0d04e76e47
current_main: b11811704efa98a12272d572f666e530a807f6c1
registered: 0
adopted: 0
axiom_movement: none
---

# The Split Generality Theorem Of The Transfer Package — the structural legs are `(m, c)`-universal on the searched set and positivity is not, with MASS, SCALE, POSITIVITY and GENERIC fenced as names for matrix properties throughout

**One sentence.** Blocks 190 to 193 established a transfer package at **one**
fixture `(m, c) = (9/20, 5/13)`; promoting that pair to a **variable** splits the
package in two — Ps-covariance, palindromicity, the perfect-square form,
`[W, U] = 0`, parity independence and the window-cell invariance hold at **every
one of 192** admissible points of an exact rational search, while the positive
two-scale reading **fails at 98 of them** in two exactly separated modes divided
by the Hodge edge `det g(c) = 1 - c^2` — and **not one line of this supplies a
mass spectrum, a dispersion relation, a transfer operator, a boundary curve in
the `(m, c)` plane or a continuum limit**.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Seven imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE GENERALITY LANGUAGE IS FENCED BEFORE THE FIRST NUMBER IS READ.**

- **NO GRAVITY IS SUPPLIED.** `(m, c)` is a pair of dials on the **imposed**
  mass term and Block 105's `shear_hodge(c, v)`. This block supplies no lapse
  variable in an ADM phase space, no shift vector, no Hamiltonian constraint, no
  momentum constraint, no first-class constraint algebra, no Dirac closure, no
  Dirac observable, no gauge orbit, no quotient and **no Osterwalder–Schrader
  reconstruction** that would make `W` a physical transfer operator. Ten
  structures, enumerated as a measured constant and gated.
- **POSITIVITY IS NOT GENERIC, AND THIS BLOCK SAYS SO FIRST.** The headline is a
  **split**, and the negative half is half the result. Asserting generic
  positivity is a declared mutation (`claim_positivity_generic`) and it fails
  gate `B`.
- **NO WINDOW BOUNDARY CURVE.** The census is a **finite set of exact rational
  points**. No edge is fitted, nothing is interpolated between points, and no
  point outside the searched set is asserted either way.
- **THE CENSUS IS NOT EXHAUSTIVE.** *Generic* here means **a count over `M × C`**
  and nothing wider. A 192-point search is not a statement about admissible
  `(m, c)` space.
- **NO PHYSICAL MASS.** `theta = acosh(T/2)` is a **logarithm of an algebraic
  number** attached to an exact rational matrix. *Heavy* and *light* **order two
  such numbers**. No particle, no energy, no dispersion relation.
- **`W` IS NOT A TRANSFER OPERATOR.** Block 190 refuted the naive OS transfer
  pairing on this class and nothing here repairs it.
- **NO CONTINUUM.** One width, one profile family, one bump, a finite grid of
  exact rationals.

**EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER
METAPHYSICAL NECESSITY** — the cycle-913 caution, carried verbatim — and every
positive here is candidacy within this formalism and never a claim about nature.

---

## W1 — the wall, and the charter

### What was open

Blocks 190 through 193 built an increasingly detailed transfer package — a
positive palindromic-squared monodromy with two scales, a `U`-grading, parity
independence, a boundary-mode structure and a parity-resolved locality window —
and every one of them read it at **the same** `(m, c) = (9/20, 5/13)`. Three
things were therefore open:

1. **Was any of it a property of the class, or of the fixture?** No block had
   varied `(m, c)` at all.
2. **If some legs are generic, are they all?** The package was always presented
   as one object; nothing had tested whether it could come apart.
3. **Where does it end?** No block had looked for a point where a leg fails, so
   no scope statement about `(m, c)` had any evidence under it.

### The charter

1. **Vary the pair** across a five-point grid including two fresh points, and
   gate every leg of the package **per point**.
2. **Hunt the boundary** — deliberately probe points where a leg should fail —
   and if one falls, make the failure the result rather than an embarrassment.
3. **Separate the legs** that survive from the ones that do not, and refuse to
   report the package as a single verdict if it is not one.
4. **Carry the adversarial check's corrections as content**, in particular the
   `C1` monic-normalization defect, as **formulas** and not as prose hedges.
5. **Fence the census as points**, never as a region, and keep the citation
   boundary between what the runner gates and what it cites explicit.

---

## N1 — THE FIVE-POINT DEEP-ODD PACKAGE, exact at every point

**NOTHING BELOW IS ABOUT THE LANDED CHAIN'S OBJECT IF THIS SECTION IS NOT
EXACT.**

### The construction, and the one thing that changed

The carrier is Block 190's wrap-edge width family at `T = 16`, unchanged: the
staggered Dirac–Kähler kernel on `Z_16 × Z_4` with `eta_t = 1`,
`eta_x = (-1)^t` and the temporal sign `w = -1` on the **wrap edge** `t = T-1`;
the grade-raising `d_K = P1 K P0 + P2 K P1`; the site reflection
`theta_s(t) = -t` with fixed slices `{0, 8}`; the raising set `A_s` in the closed
half `{0..8}` excluding fixed-slice spatial edges; the glue
`D_s = A_s - Ps A_s Ps`; and the completion

```text
Q  =  m H  +  H D_s  -  D_s^T H,        G = Q^-1,
K_c[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)],
L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)],
W        = K_c^-1 L_2.
```

The **only** thing this block changes is that `(m, c)` is now read as a
variable. `H` is assembled by Block 191's quarter-weighted four-corner cell
average from the landed Block 105 shear Hodge

```text
B(c, v) = diag( v,  v g(c)^-1,  1/v ),      g(c) = [[1, c], [c, 1]],
```

read through the Block 128 module. **That import is the only object imported**,
and the freedom in its first argument is exactly the freedom exercised here.

### The grid

| point | provenance |
| --- | --- |
| `(9/20, 5/13)` | the control — the fixture of Blocks 190–193 |
| `(1, 5/13)` | Block 188's known-positive site fixture |
| `(9/20, 3/5)` | Block 188's second known-positive fixture |
| `(1/2, 1/3)` | **fresh** — rebuilt independently by the adversarial check |
| `(2/3, 1/5)` | **fresh** — rebuilt independently by the adversarial check |

### The carrier closes at every point

`rank(Q) = 64`, `nnz(Q G - I) = 0`, `nnz(Ps Q Ps - Q^T) = 0`, and the four core
Gram ranks at `t0 = 2, 3, 4, 5` are `(8, 8, 8, 8)` — at all five points. Gate
`C-1`.

### The deep odd core, `t0 = 3`

At every point `charpoly(W)` factors over `QQ` into **exactly two** primitive
palindromic integer quadratics, each of **multiplicity two**:

| `(m, c)` | first primitive factor | second primitive factor |
| --- | --- | --- |
| `(9/20, 5/13)` | `22569375 z^2 - 233631106 z + 22569375` | `39529825 z^2 - 109432706 z + 39529825` |
| `(1, 5/13)` | `26527 z^2 - 444930 z + 26527` | `51097 z^2 - 289682 z + 51097` |
| `(9/20, 3/5)` | `12475 z^2 - 273738 z + 12475` | `53125 z^2 - 142538 z + 53125` |
| `(1/2, 1/3)` | `233 z^2 - 690 z + 233` | `739 z^2 - 7258 z + 739` |
| `(2/3, 1/5)` | `17099 z^2 - 159050 z + 17099` | `21709 z^2 - 81434 z + 21709` |

Gate `C-2`.

### The check's `C1` correction, carried as a FORMULA

The adversarial check found the solve's displayed equalities **literally false**,
and the repair is exact rather than verbal. SymPy's characteristic polynomial is
**monic**, so for primitive factors `a_1 z^2 + b_1 z + a_1` and
`a_2 z^2 + b_2 z + a_2`,

```text
(a_1 z^2 + b_1 z + a_1)^2 (a_2 z^2 + b_2 z + a_2)^2  =  s · charpoly_monic(W),
                                              s  =  (a_1 a_2)^2 .
```

That identity — **not merely the table of scalars** — is what gate `C-3`
measures: the scalar is confirmed to equal the squared product of the two
leading coefficients at every point, and the polynomial residual is exactly `0`.

| `(m, c)` | `s` |
| --- | ---: |
| `(9/20, 5/13)` | `795955611005101889386962890625` |
| `(1, 5/13)` | `1837245025097114161` |
| `(9/20, 3/5)` | `439216851806640625` |
| `(1/2, 1/3)` | `29648362969` |
| `(2/3, 1/5)` | `137791066603200481` |

### The spectral form, gated twice over

The check also left a **warning** that this block takes seriously: at four
admissible points a palindromic quadratic splits over `QQ` into reciprocal
*linear* factors, so **irreducible-factor degree alone is not a valid positivity
checker**. This block therefore gates two things that are degree-blind.

**One — the perfect-square palindromic form.** The monic characteristic
polynomial is palindromic and is the exact square of a degree-four palindromic
polynomial

```text
charpoly_monic(W) = p(z)^2 ,   p(z) = z^4 + alpha z^3 + beta z^2 + alpha z + 1,
```

**verified by expansion**, not inferred from the multiplicities. Since
`z^-2 p(z) = (T^2 - 2) + alpha T + beta` under `T = z + 1/z`, all four reciprocal
root pairs are governed by the **trace polynomial**

```text
q(T)  =  T^2  +  alpha T  +  (beta - 2).
```

**Two — the scale census, with no radical ever evaluated.** The number of roots
of `q` above `2`, strictly inside `(-2, 2)` and below `-2` is read off the signs
of `q(2)`, `q(-2)` and the vertex `-alpha/2`. `T > 2` is the hyperbolic branch
`T = 2 cosh(theta)`, hence a **positive** reciprocal pair `e^{±theta}`; `T < -2`
is a **negative** real reciprocal pair; `|T| < 2` gives a **complex** pair on the
unit circle. Positivity is exactly the census `(2, 0, 0)`.

Gate `C-5` requires the census `(2, 0, 0)`, requires the **independent**
per-factor discriminant/trace/constant route to agree with it at every point,
and requires the two scales to be **distinct**. Gate `C-4` requires the
perfect-square form. Gate `C-6` requires `nnz([W, U]) = 0`.

---

## N2 — PARITY INDEPENDENCE AND THE WINDOW CELL, generic on the grid

**The true parity test.** `charpoly(W, t0 = 2)` equals `charpoly(W, t0 = 3)`
exactly, at all five points. Gate `D-1`.

**The window cell.** Block 193's parity-resolved window law predicts that a
`{2, 3}` volume bump does **not** break the intertwining identity at `t0 = 5`.
Measured at every grid point with `v = 4/5`:

```text
nnz( W_bump(t0 = 5)  -  W_1(t0 = 5) )  =  0 .
```

Gate `D-2`. This is Block 193's law gated as an **instance** at five new `(m, c)`
points, not a re-derivation of it.

**And it is a nontrivial cancellation.** The invariance is not the trivial
statement that nothing moved: the core Gram itself moves in **64 of its 64**
entries under the same bump,

```text
nnz( K_bump(t0 = 5)  -  K_1(t0 = 5) )  =  64 ,
```

so `W = K_c^-1 L_2` is invariant through an exact **quotient cancellation**
between a moved Gram and a moved shifted pairing. Gate `D-3`.

---

## N2b — THE BOUNDARY LAYER, and the solve's own mis-aim

**The mis-aim, stated plainly.** The solve read `t0 = 4` as the even-deep core
and compared its characteristic polynomial against `t0 = 3` as a *parity test*.
At `T = 16` that is wrong: `t0 = 4 = T/2 - 4` is a **far boundary-layer** core,
and the even-deep representative is `t0 = 2`. The solve's `parityW = False`
lines compared **deep against boundary** and are **meaningless as parity tests**.
Correction 55 below; the real parity test is `N2`.

**What `t0 = 4` does carry, and it is generic.** Block 191's boundary-mode
structure replicates at every grid point: the factorization is

```text
(heavy)^1  (light)^2  (boundary)^1 ,
```

with exactly one **new** quadratic of multiplicity one, and that quadratic is
**non-reciprocal** — leading and constant coefficients differ, so its roots are
not a reciprocal pair — with a strictly positive discriminant.

| `(m, c)` | boundary quadratic |
| --- | --- |
| `(9/20, 5/13)` | `48554286398375 z^2 - 445467467014578 z + 43033320714375` |
| `(1, 5/13)` | `3750468703 z^2 - 54521277270 z + 3250592053` |
| `(9/20, 3/5)` | `173474375 z^2 - 2051118834 z + 93475175` |
| `(1/2, 1/3)` | `1098595 z^2 - 9936202 z + 1011691` |
| `(2/3, 1/5)` | `209535268 z^2 - 1901760850 z + 204452743` |

Gates `E-1`, `E-2`, `E-3`.

---

## N3 — THE SPLIT, and it is the block

### The census frame

The adversarial check searched the full Cartesian set

```text
M = {1/100, 1/50, 1/20, 1/10, 1/5, 1/3, 1/2, 2/3, 1, 2, 5, 10}            (12)
C = {-99/100, -9/10, -3/4, -1/2, -1/5, 0, 1/5, 1/3, 1/2, 3/4,
     9/10, 19/20, 99/100, 101/100, 6/5, 3/2, 2}                           (17)
```

— `204` exact rational candidates. The **twelve with `c = 2`** are excluded
because baseline `Q` is exactly singular there; this block **re-measures** that
exclusion at both ends of `M` and finds `rank(Q) = 62` of `64`, so the
singularity is a corank-two property of `Q` and not of the Hodge block (whose
denominator `1 - c^2 = -3` is perfectly finite there). `192` admissible remain.
Gate `F-1`.

### The two halves

| leg | census |
| --- | ---: |
| deep monic charpoly palindromic | `192 / 192` |
| the perfect-square palindromic form | `192 / 192` |
| `[W, U] = 0` | `192 / 192` |
| `charpoly(W, t0=2) = charpoly(W, t0=3)` | `192 / 192` |
| bump `{2,3}` window cell at `t0 = 5` | `192 / 192` |
| `Ps` covariance | `192 / 192` |
| **all eight roots real and positive** | **`94 / 192`** |
| **positivity failure** | **`98 / 192`** |

**That table is the theorem.** The structural legs are universal on the searched
set; positivity is not. They are not one object and this block declines to
report them as one.

### The citation boundary, stated so it cannot be mistaken

The runner **gates a twelve-point subset re-measured in full** and **cites** the
192-point totals, which were measured **offline** and are **not re-run** by the
runner. The subset is chosen to span the split — six positive, six failing —
across both fresh fixtures, both signs of `c`, both extremes of `M`, the
zero-shear point and three points beyond the Hodge edge:

| `(m, c)` | verdict | scale census |
| --- | --- | --- |
| `(1/2, 1/3)` | positive | `(2,0,0)` |
| `(2/3, 1/5)` | positive | `(2,0,0)` |
| `(1/100, -99/100)` | positive | `(2,0,0)` |
| `(1/2, 1/2)` | positive | `(2,0,0)` |
| `(2, -1/2)` | positive | `(2,0,0)` |
| `(1/3, 0)` | positive | `(2,0,0)` |
| `(1/100, 3/4)` | **fails** | `(1,0,1)` |
| `(1/20, 9/10)` | **fails** | `(1,0,1)` |
| `(10, 3/4)` | **fails** | `(1,0,1)` |
| `(10, 99/100)` | **fails** | `(1,0,1)` |
| `(5, 101/100)` | **fails** | `(0,2,0)` |
| `(1/10, 3/2)` | **fails** | `(1,1,0)` |

All five structural legs hold at **12 of 12** — including at every point where
positivity fails. The core-Gram motion that makes the window cell nontrivial is
`64` of `64` at every subset point except the zero-shear point `(1/3, 0)`, where
it is `48` of `64`; it is nonzero everywhere, which is all the nontriviality
argument needs. Gates `F-2`, `F-3`, `F-6`.

Two of these are the `QQ`-split points the check warned about: at `(1/2, 1/2)`
the factorization is `(2z-5)^2 (5z-2)^2 (4z^2 - 57z + 4)^2` and at `(2, -1/2)` it
is `(z-13)^2 (13z-1)^2 (61z^2 - 1102z + 61)^2`. Both are **positive**, both have
a linear-factor pair, and both pass the perfect-square and scale-census tests —
which is exactly why this block does not use factor degree as a checker.

### The exact witness

At `(m, c) = (1/100, 3/4)`,

```text
charpoly_monic(W) = (57536 z^2 + 5175457 z + 57536)^2
                    (1322536 z^2 - 2645457 z + 1322536)^2
                    / 5790210286399072239616 .
```

The first factor has discriminant `26772113593665 > 0`, root product exactly `1`
and root sum `-5175457/57536 < 0` — so its two roots are **real, reciprocal and
both strictly negative**. The second retains a positive reciprocal pair with
discriminant `2036853665`, and its trace `2645457/1322536` exceeds `2` by
exactly `385/1322536` — the witness sits close to the sign boundary on both
sides at once. Gate `F-4`.

**And the thinnest margin in the whole census is thinner still, at a point that
PASSES.** At `(1/100, -99/100)` — inside the gated subset — the light scale is
`T = 520153019601/260073505000`, which exceeds `2` by

```text
T - 2  =  6009601 / 260073505000   ~  2.3 x 10^-5 .
```

That is the sharpest reason `sp.nsimplify` is gated to **zero** occurrences: its
rational tolerance maps a small nonzero rational to exactly `0`, and a single
such call at that point would flip a passing sign test either way.

---

## N3b — THE FAILURE SET IS NOT ONE MODE, and the Hodge edge separates them

**This is this block's own refinement of the check.** The check reported its
positivity failures as *negative reciprocal pairs*. Measured here, the failing
set contains a **second mode**: at `(5, 101/100)` and `(1/10, 3/2)` the failing
pairs are **complex and unimodular**, carrying **no negative pair at all**. The
scale census separates the modes exactly:

| census | meaning |
| --- | --- |
| `(2,0,0)` | positive — both pairs `e^{±theta}` |
| `(1,0,1)` | one **negative** real reciprocal pair |
| `(1,1,0)` | one **complex** unimodular pair |
| `(0,2,0)` | **both** pairs complex |

**And the separation is the Hodge edge.** The shear metric is
`g(c) = [[1, c], [c, 1]]` with `det g = 1 - c^2`, so `|c| > 1` is exactly where
`g` is **indefinite**. On the searched set: every point with `c > 1` fails, and
fails in the **complex** mode; every negative-pair failure and every positive
point sits at `|c| < 1`. Gate `F-5`.

### The cited column table

Per shear column, `(positive, negative-pair, complex-pair)` over the twelve
searched masses:

| `c` | pos | neg | cplx | | `c` | pos | neg | cplx |
| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| `-99/100` | `9` | `3` | `0` | | `1/2` | `10` | `2` | `0` |
| `-9/10` | `10` | `2` | `0` | | `3/4` | `0` | `12` | `0` |
| `-3/4` | `10` | `2` | `0` | | `9/10` | `0` | `12` | `0` |
| `-1/2` | `10` | `2` | `0` | | `19/20` | `0` | `12` | `0` |
| `-1/5` | `12` | `0` | `0` | | `99/100` | `0` | `12` | `0` |
| `0` | `12` | `0` | `0` | | `101/100` | `0` | `0` | `12` |
| `1/5` | `11` | `1` | `0` | | `6/5` | `0` | `0` | `12` |
| `1/3` | `10` | `2` | `0` | | `3/2` | `0` | `0` | `12` |
| | | | | | **total** | **`94`** | **`62`** | **`36`** |

**Two whole-column facts follow, and both are counts over a finite search and
nothing more.**

1. The **four** columns `c = 3/4, 9/10, 19/20, 99/100` fail at **every one** of
   the twelve searched masses by a negative pair. This **extends** the check's
   single `c = 3/4` observation to four columns.
2. The **three** columns beyond the Hodge edge fail at every searched mass by
   the complex mode.

**No curve is fitted through these columns and no point between them is asserted
either way.** Gates `F-7`, `F-8`.

---

## N4 — THE MONOTONICITY CHAIN, exact and fenced as discrete

At fixed `m = 1/2`, varying only `c`:

| `c` | `T_heavy` | `T_light` | cross-product certifying `T_heavy > T_light` |
| ---: | ---: | ---: | ---: |
| `1/5` | `63258/7619` | `28762/9629` | `389973604` |
| `1/4` | `6223/709` | `575/193` | `793364` |
| `1/3` | `7258/739` | `690/233` | `1181204` |
| `2/5` | `12922/1171` | `6298/2141` | `20291044` |
| `9/20` | `3084847/250021` | `1534683/525061` | `1236029872324` |

Every one of the ten traces exceeds `2`, so `theta = acosh(T/2)` is real and
strictly positive at every point. The adjacent exact differences as `c` rises:

| step | `Delta T_heavy` | `Delta T_light` |
| --- | ---: | ---: |
| `1/5 -> 1/4` | `2563115/5401871 > 0` | `-14391/1858397 < 0` |
| `1/4 -> 1/3` | `547125/523951 > 0` | `-805/44969 < 0` |
| `1/3 -> 2/5` | `1050240/865369 > 0` | `-9856/498853 < 0` |
| `2/5 -> 9/20` | `381584475/292774591 > 0` | `-21077875/1124155601 < 0` |

**The conclusion, and its exact scope.** `acosh(T/2)` is positive and strictly
increasing for `T > 2`; `T_heavy` strictly increases and `T_light` strictly
decreases along the chain; both stay positive. Therefore

```text
theta_heavy / theta_light   strictly increases   along these five points.
```

**ON THIS FIVE-POINT DISCRETE GRID AND NOWHERE ELSE.** This is not a theorem of
continuous monotonicity between grid points, it is not a dispersion relation,
and it is not a statement about any mass ratio in nature. Gates `G-1` to `G-4`;
`CONTINUOUS_MONOTONICITY_CLAIMED = False` is a declared constant with a gate and
the mutation `break_ratio_monotonicity`.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

- **`scale`** names a root `T` of the rational quadratic `q(T)`, nothing more.
- **`theta`** names `acosh(T/2)` for `T > 2` — a **logarithm of an algebraic
  number**. It is not an energy, a mass or an inverse length.
- **`heavy` / `light`** **order two such numbers**. The ordering is an
  arithmetic comparison of two rationals, certified by an integer
  cross-product.
- **`positivity`** names the statement that eight roots of one rational
  polynomial are real and positive. It is not reflection positivity, not
  operator positivity and not OS positivity.
- **`window`** in *positivity window* names **the set of searched points at
  which a sign test passes**. It is not a region, not an interval and not a
  domain. (In *window cell* it is Block 193's locality window, carried
  unchanged.)
- **`generic`** names **a count over `M × C`**. It carries no measure, no
  topology and no density statement.

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within this imposed finite matrix construction at `T = 16`, over the `192`
> admissible points of the exact rational set `M × C`, the six structural legs
> listed in `N3` hold with zero exceptions, and the statement that all eight
> roots of `charpoly(W)` at `t0 = 3` are real and positive holds at `94` of them
> and fails at `98`, the failures splitting into `62` carrying a negative real
> reciprocal pair and `36` — exactly the points with `c > 1` — carrying complex
> unimodular pairs.

### Three further fences, all three self-imposed

1. **The universality is COUNTED, not DERIVED.** No proof from the staggered
   recurrence is offered for why palindromicity, the perfect-square form,
   `[W, U] = 0`, parity independence or the window cell should be `(m, c)`-
   independent. They are measured at 192 points and that is all.
2. **The positivity window's boundary is NOT located.** A finite set of points
   cannot locate a boundary. The column table shows where the searched columns
   change character; it does not show where the change happens.
3. **The Hodge-edge coincidence is MEASURED, not proved.** That the complex-mode
   points are exactly the `c > 1` points is a fact about **these three searched
   columns**. No mechanism connecting `det g(c) < 0` to unimodular monodromy
   pairs is supplied.

### What IS derived, stated positively so the fence is not mistaken for a retreat

The monic-normalization identity `s = (a_1 a_2)^2` is **derived and gated as an
identity**, not tabulated. The reduction of eight-root positivity to the two
roots of `q(T)` is **derived** from the perfect-square palindromic form. The
implication *`T_heavy` up and `T_light` down and both `> 2`* ⟹ *ratio up* is
**derived** from monotonicity of `acosh`. And the split itself is a **theorem
about this construction**: two legs of one package have provably different
scopes.

---

## READINGS — five of them, and each is a reading

- **`R1`.** *That `theta_heavy/theta_light` is a mass ratio.* Measured: a ratio
  of two logarithms of algebraic numbers attached to a rational matrix.
  **Reading.**
- **`R2`.** *That the positivity window is a physical stability region.*
  Measured: a set of rational points at which a discriminant/sign test passes.
  **Reading.**
- **`R3`.** *That the Hodge edge `|c| = 1` causes the complex mode.* Measured: a
  coincidence at three searched columns. No mechanism is supplied.
  **Reading.**
- **`R4`.** *That the universal legs are universal because of a symmetry.* No
  symmetry argument is given anywhere in this block. **Reading.**
- **`R5`.** *That `94/192` is a probability, a density or a measure.* It is a
  count over a set someone chose by hand. **Reading.**

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | family |
| ---: | --- | --- | --- |
| 1 | `origin/main`, axiom and registry blobs, worktree blobs, timeout | five pins fixed | `A` |
| 2 | `PARENT_COMMIT` ancestry, both Block 193 artifacts, stale pin carrying neither | exact | `A` |
| 3 | imposed / registered / adopted | `7 / 0 / 0` | `B` |
| 4 | gravity structures enumerated as NOT SUPPLIED | `10` | `B` |
| 5 | `POSITIVITY_GENERIC_CLAIMED` | `False` — the refuted half | `B` |
| 6 | `WINDOW_BOUNDARY_CURVE_CLAIMED`, `CENSUS_EXHAUSTIVE_CLAIMED` | both `False` | `B` |
| 7 | `PHYSICAL_MASS`, `TRANSFER_OPERATOR`, `CONTINUUM_LIMIT` | all `False` | `B` |
| 8 | `rank(Q)`, `nnz(QG-I)`, `nnz(PsQPs-Q^T)`, Gram ranks, five points | `64`, `0`, `0`, `(8,8,8,8)` | `C` |
| 9 | the five primitive factor pairs at `t0 = 3`, multiplicity `2`, palindromic | the table in `N1` | `C` |
| 10 | `(a_1 z^2+b_1 z+a_1)^2 (a_2 z^2+b_2 z+a_2)^2 = s · charpoly_monic(W)`, `s = (a_1 a_2)^2` | residual `0`, five scalars | `C` |
| 11 | `charpoly_monic(W) = p(z)^2`, `p` degree-four palindromic, by expansion | `True`, five points | `C` |
| 12 | scale census `(2,0,0)`; per-factor route agrees; two scales distinct | `True`, five points | `C` |
| 13 | `nnz([W, U])` | `0`, five points | `C` |
| 14 | `charpoly(W, t0=2) = charpoly(W, t0=3)` | exact, five points | `D` |
| 15 | `nnz(W_bump(t0=5) - W_1(t0=5))`, `{2,3}` at `v = 4/5` | `0`, five points | `D` |
| 16 | `nnz(K_bump - K_1)` at `t0 = 5` | `64`, five points | `D` |
| 17 | `t0 = 4` shape `(heavy)^1 (light)^2 (boundary)^1` | five points | `E` |
| 18 | the five boundary quadratics | the table in `N2b` | `E` |
| 19 | boundary quadratic non-reciprocal, positive discriminant | `True`, five points | `E` |
| 20 | census frame `12 × 17 = 204`; `c = 2` re-measured `rank(Q) = 62` | `192` admissible | `F` |
| 21 | five structural legs on the twelve-point subset | `12 / 12` each | `F` |
| 22 | subset span, and the two declared point lists | `6` positive, `6` failing | `F` |
| 23 | the `(1/100, 3/4)` witness: factors, scalar, discriminants, root signs | exact | `F` |
| 24 | failure modes per subset point; negative vs complex counts | `4` / `2`; not one mode | `F` |
| 25 | the cited census totals, internally consistent | `192`, `94`, `98` | `F` |
| 26 | measured-only discipline on the window | `True`, no curve | `F` |
| 27 | the cited column table and its two whole-column facts | `(94, 62, 36)` | `F` |
| 28 | the five exact `(T_heavy, T_light)` pairs; all ten `> 2` | the table in `N4` | `G` |
| 29 | the five integer cross-products | all `> 0` | `G` |
| 30 | the four adjacent differences, heavy up and light down | exact rationals | `G` |
| 31 | ratio increasing on the grid; continuous monotonicity | `True`; `False` | `G` |
| 32 | the note at its final path; `N5` byte-identical; `sp.nsimplify` count | present; verbatim; `0` | `H` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

**Dead end one — factor degree as a positivity checker.** The first pass tested
positivity by requiring exactly two irreducible palindromic quadratics of
multiplicity two. That passes `188/192` and **misclassifies the four `QQ`-split
points**, which are positive. The check flagged this in advance. Replaced by the
degree-blind perfect-square + scale-census route, which gives `192/192` on the
structural leg and the correct `94/192` on positivity, and whose agreement with
an independent per-factor route is itself gated.

**Dead end two — reading `t0 = 4` as the even-deep core.** See `N2b`. The
even-deep representative at `T = 16` is `t0 = 2`.

**Dead end three — reporting one verdict.** The solve's phase-1 and phase-2
results both read "generic", because both were measured on a five-point grid
where positivity happens to hold everywhere. The five-point grid is **not** a
boundary hunt, and a package that has never been pushed has never been scoped.

**What actually worked.** Reducing eight-root positivity to the two roots of one
rational quadratic `q(T)`, and then reading the root positions off three signs
rather than off any radical. Every positivity statement in this block is three
rational sign comparisons.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE GENERALITY LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 WITH ITS MASS/SHEAR PAIR (m, c) PROMOTED FROM A FIXTURE TO A VARIABLE (the staggered Dirac-Kahler carrier on Z_16 x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, 8}, the raising set A_s in the CLOSED half {0..8} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), THE FIVE-POINT GRID of the control (9/20, 5/13), Block 188's two known-positive fixtures (1, 5/13) and (9/20, 3/5) and the two FRESH points (1/2, 1/3) and (2/3, 1/5), THE ADVERSARIAL CHECK's SEARCHED RATIONAL SET M x C of 204 candidates imposed as a CENSUS FRAME AND NOT AS A DOMAIN, THE TWELVE-POINT RE-MEASURED SUBSET chosen to span the split, BLOCK 191's UNIT VOLUME PROFILE AND ITS {2, 3} BUMP AT v = 4/5, THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2 with its momentum shift U, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module AT A VARYING RATIONAL SHEAR -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit, NO quotient and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, THE TRANSFER PACKAGE SPLITS -- ITS STRUCTURAL LEGS HOLD AT EVERY ADMISSIBLE POINT OF A 192-POINT RATIONAL SEARCH AND ITS POSITIVITY LEG FAILS AT 98 OF THEM. 'MASS', 'SCALE', 'HEAVY', 'LIGHT', 'POSITIVITY', 'WINDOW' AND 'GENERIC' NAME PROPERTIES OF EXACT RATIONAL MATRICES: 'scale' NAMES a root T = z + 1/z of a rational quadratic, 'theta' NAMES acosh(T/2) for T > 2 and therefore a LOGARITHM OF AN ALGEBRAIC NUMBER, 'heavy' and 'light' ORDER two such numbers, 'positivity' NAMES the statement that eight roots of one rational polynomial are real and positive, and 'generic' NAMES a count over a FINITE SEARCHED SET. NO PHYSICAL MASS IS SUPPLIED AND NO DISPERSION RELATION IS SUPPLIED. NO WINDOW BOUNDARY CURVE IS SUPPLIED: the census is a FINITE SET OF EXACT RATIONAL POINTS, no edge is fitted, nothing is interpolated between points and no point outside the searched set is asserted either way. THE CENSUS IS NOT EXHAUSTIVE AND 'GENERIC' IS SCOPED TO M AND C AND TO NOTHING WIDER. NO CONTINUUM. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE FIVE-POINT DEEP-ODD PACKAGE IS EXACT AT EVERY POINT, AND THE CHECK'S C1 CORRECTION IS CARRIED AS A FORMULA RATHER THAN AS A HEDGE. At the deep odd core t0 = 3 each of the five grid points gives charpoly(W) with EXACTLY TWO primitive palindromic integer quadratics, each of MULTIPLICITY TWO: (22569375 z^2 - 233631106 z + 22569375) and (39529825 z^2 - 109432706 z + 39529825) at the control; (26527, -444930) and (51097, -289682) at (1, 5/13); (12475, -273738) and (53125, -142538) at (9/20, 3/5); (233 z^2 - 690 z + 233) and (739 z^2 - 7258 z + 739) at (1/2, 1/3); and (17099 z^2 - 159050 z + 17099) and (21709 z^2 - 81434 z + 21709) at (2/3, 1/5). THE POLYNOMIAL SymPy RETURNS IS MONIC, SO THOSE DISPLAYED INTEGER PRODUCTS ARE THE CHARACTERISTIC POLYNOMIAL ONLY AFTER DIVISION BY AN EXACT SCALAR, AND THE SCALAR IS EXACTLY THE SQUARED PRODUCT OF THE TWO LEADING COEFFICIENTS: 795955611005101889386962890625, 1837245025097114161, 439216851806640625, 29648362969 and 137791066603200481, each gated at ZERO polynomial residual. THE CARRIER CLOSES AT EVERY POINT: rank(Q) = 64, nnz(Q G - I) = 0, nnz(Ps Q Ps - Q^T) = 0 and all four core Gram ranks are 8. THE SPECTRAL FORM IS GATED TWICE OVER: the monic charpoly is PALINDROMIC and is the EXACT SQUARE of a degree-four palindromic polynomial p(z) = z^4 + alpha z^3 + beta z^2 + alpha z + 1 verified by expansion and NOT inferred from the multiplicities, and positivity is established by TWO INDEPENDENT EXACT ROUTES that AGREE at every point -- a per-factor discriminant/trace/constant test, and a SCALE CENSUS on the trace polynomial q(T) = T^2 + alpha T + (beta - 2) that counts roots above 2, inside (-2, 2) and below -2 from the signs of q(2), q(-2) and the vertex, WITH NO RADICAL EVER EVALUATED. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, and this block's margins are as thin as T - 2 = 6009601/260073505000 at the census point (1/100, -99/100), which is INSIDE the gated subset and is POSITIVE, so a single such call could manufacture or destroy positivity; this runner calls it ZERO TIMES, counted in its own source by gate H.\nper_mode: PARITY INDEPENDENCE, THE WINDOW CELL AND THE BOUNDARY LAYER ARE ALL (m, c)-GENERIC ON THE GRID. At all five points charpoly(W, t0 = 2) equals charpoly(W, t0 = 3) EXACTLY, which is the TRUE parity test; and the {2, 3} volume bump at v = 4/5 leaves the t0 = 5 monodromy MATRIX-EXACTLY unchanged at residual 0 while the core Gram K_c itself moves in 64 of its 64 entries, so the window-cell invariance is a NONTRIVIAL QUOTIENT CANCELLATION and not a trivial identity. THE SOLVE'S OWN t0 = 4 LEG WAS MIS-AIMED AND THE MIS-AIM IS CARRIED AS A CORRECTION: at T = 16 the core t0 = 4 = T/2 - 4 is a FAR BOUNDARY-LAYER core and NOT the even-deep representative -- that is t0 = 2 -- so the parityW comparisons the solve read at t0 = 4 compared deep against boundary and were MEANINGLESS AS PARITY TESTS. What t0 = 4 does carry is Block 191's BOUNDARY-MODE STRUCTURE, and that structure REPLICATES AT ALL FIVE POINTS: the factorization is (heavy)^1 (light)^2 (boundary)^1 with exactly one NEW quadratic of multiplicity one, and that quadratic is NON-RECIPROCAL -- leading and constant differ -- with a strictly positive discriminant, at (9/20, 5/13), (1, 5/13), (9/20, 3/5), (1/2, 1/3) and (2/3, 1/5) alike.\nper_block: THE SPLIT, AND IT IS THE BLOCK. The adversarial check searched the full Cartesian set M = {1/100, 1/50, 1/20, 1/10, 1/5, 1/3, 1/2, 2/3, 1, 2, 5, 10} against C = {-99/100, -9/10, -3/4, -1/2, -1/5, 0, 1/5, 1/3, 1/2, 3/4, 9/10, 19/20, 99/100, 101/100, 6/5, 3/2, 2} -- 204 exact rational candidates. THE TWELVE WITH c = 2 ARE EXCLUDED BECAUSE BASELINE Q IS EXACTLY SINGULAR THERE, RE-MEASURED HERE AT BOTH ENDS OF M AT RANK 62 OF 64, leaving 192 admissible. ON THOSE 192: palindromicity, the perfect-square form, [W, U] = 0, parity independence and the {2, 3} window cell hold at 192 OF 192 WITH ZERO EXCEPTIONS, while POSITIVITY HOLDS AT ONLY 94 AND FAILS AT 98. THE STRUCTURAL LEGS ARE UNIVERSAL ON THE SEARCHED SET AND POSITIVITY IS NOT, AND THAT IS THE THEOREM. THE RUNNER GATES A TWELVE-POINT SUBSET RE-MEASURED IN FULL -- SIX POSITIVE AND SIX FAILING, spanning both fresh fixtures, both signs of c, both extremes of m, the zero-shear point and three points beyond the Hodge edge -- AND CITES THE FULL 192-POINT CENSUS, WHICH IS MEASURED OFFLINE AND IS NOT RE-RUN BY THE RUNNER; that citation boundary is stated here so no reader mistakes a cited count for a gated one. THE EXACT WITNESS IS (m, c) = (1/100, 3/4), where charpoly(W) = (57536 z^2 + 5175457 z + 57536)^2 (1322536 z^2 - 2645457 z + 1322536)^2 / 5790210286399072239616: the first factor has discriminant 26772113593665 > 0, root product exactly 1 and root sum -5175457/57536 < 0, so its two roots are real, reciprocal and BOTH STRICTLY NEGATIVE, while the second retains a positive reciprocal pair with discriminant 2036853665.\nlattice_wide: THE FAILURE SET IS NOT ONE MODE, AND THE HODGE EDGE SEPARATES THE TWO. The adversarial check reported its positivity failures as NEGATIVE reciprocal pairs. Measured here, the failing set contains a SECOND MODE the check did not separate: at (5, 101/100) and (1/10, 3/2) the failing pairs are COMPLEX AND UNIMODULAR, carrying NO negative pair at all, and the scale census distinguishes the modes exactly -- (2,0,0) positive, (1,0,1) one negative real pair, (1,1,0) one complex pair, (0,2,0) both pairs complex. THE SEPARATION IS THE HODGE EDGE ITSELF: the displayed shear metric is g(c) = [[1, c], [c, 1]] with det g = 1 - c^2, so |c| > 1 is exactly where g is INDEFINITE, and on the searched set EVERY point with c > 1 fails in the COMPLEX mode while EVERY negative-pair failure and EVERY positive point sits at |c| < 1. THE CITED COLUMN TABLE MAKES IT ARITHMETIC: over the sixteen admissible shear columns at twelve searched masses each, (positive, negative-pair, complex-pair) is (9,3,0) at c = -99/100, (10,2,0) at -9/10, -3/4 and -1/2, (12,0,0) at -1/5 and 0, (11,1,0) at 1/5, (10,2,0) at 1/3 and 1/2, (0,12,0) at 3/4, 9/10, 19/20 and 99/100, and (0,0,12) at 101/100, 6/5 and 3/2 -- totalling 94, 62 and 36. TWO WHOLE-COLUMN FACTS FOLLOW AND BOTH ARE COUNTS OVER A FINITE SEARCH AND NOTHING MORE: the FOUR columns c = 3/4, 9/10, 19/20 and 99/100 fail at EVERY ONE of the twelve searched masses by a negative pair, which EXTENDS the check's single c = 3/4 observation to four columns; and the THREE columns beyond the Hodge edge fail at every searched mass by the complex mode. NO CURVE IS FITTED THROUGH THESE COLUMNS AND NO POINT BETWEEN THEM IS ASSERTED EITHER WAY.\nper_scope: THE MONOTONICITY CHAIN IS EXACT, DISCRETE AND FENCED AS DISCRETE. At fixed m = 1/2 over c in {1/5, 1/4, 1/3, 2/5, 9/20} the exact traces T = 2 cosh(theta) = -b/a are T_heavy = 63258/7619, 6223/709, 7258/739, 12922/1171 and 3084847/250021 against T_light = 28762/9629, 575/193, 690/233, 6298/2141 and 1534683/525061. Every one of the ten exceeds 2, so acosh(T/2) is real and strictly positive at every point; T_heavy > T_light is certified by the exact integer cross-products 389973604, 793364, 1181204, 20291044 and 1236029872324, all strictly positive; and the four adjacent differences are 2563115/5401871, 547125/523951, 1050240/865369 and 381584475/292774591 for the heavy trace against -14391/1858397, -805/44969, -9856/498853 and -21077875/1124155601 for the light one. SINCE acosh(T/2) IS POSITIVE AND STRICTLY INCREASING FOR T > 2, theta_heavy STRICTLY INCREASES AND theta_light STRICTLY DECREASES ALONG THE CHAIN AND BOTH STAY POSITIVE, SO theta_heavy / theta_light STRICTLY INCREASES -- ON THIS FIVE-POINT DISCRETE GRID AND NOWHERE ELSE. THIS IS NOT A THEOREM OF CONTINUOUS MONOTONICITY BETWEEN GRID POINTS, IT IS NOT A DISPERSION RELATION, AND IT IS NOT A STATEMENT ABOUT ANY MASS RATIO IN NATURE. WHAT REMAINS OPEN IS NAMED: WHY the structural legs are universal is NOT derived -- they are COUNTED over a finite search and no proof from the staggered recurrence is offered; the positivity window's boundary is NOT located, because a finite set of points cannot locate one; and the coincidence between the Hodge edge |c| = 1 and the complex-mode boundary is MEASURED at the searched columns and NOT proved.\nRESULT: THE TRANSFER PACKAGE OF BLOCKS 190 TO 193 SPLITS UNDER VARIATION OF (m, c): ITS STRUCTURAL LEGS -- Ps-COVARIANCE, PALINDROMICITY, THE PERFECT-SQUARE FORM, [W, U] = 0, PARITY INDEPENDENCE AND THE WINDOW-CELL INVARIANCE -- HOLD AT ALL 192 ADMISSIBLE POINTS OF THE SEARCHED RATIONAL SET WITH ZERO EXCEPTIONS, WHILE ITS POSITIVITY LEG FAILS AT 98 OF THEM IN TWO EXACTLY SEPARATED MODES DIVIDED BY THE HODGE EDGE -- AND NOT ONE LINE OF IT IS A MASS SPECTRUM, A DISPERSION RELATION, A TRANSFER OPERATOR, A BOUNDARY CURVE IN THE (m, c) PLANE OR A CONTINUUM LIMIT. The five-point deep-odd package, the parity independence, the window cell and Block 191's boundary-mode structure are exact at every grid point; the check's C1 monic-normalization correction is carried as a FORMULA with the scalar identified as the squared product of the leading coefficients; the check's positivity witness is reproduced digit for digit; the check's single-column c = 3/4 observation is extended to four whole columns; a SECOND failure mode the check did not separate is exhibited and located at the Hodge edge; and the theta-ratio monotonicity is proved exactly and fenced as discrete. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-193 STAND EXACTLY AS LANDED. BLOCK 193 IS NOT CORRECTED: its parity-resolved window law is carried here unchanged as the source of this block's window-cell leg, and the {2, 3} cell at t0 = 5 is gated as an INSTANCE of it at five new (m, c) points. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE width, ONE profile family, ONE bump, a FIVE-POINT grid and a 192-POINT rational search -- a finite search is not a parameter space; the runner GATES twelve points and CITES the other 180, so the full-census counts are CITATIONS and not gated measurements; the universality of the structural legs is COUNTED and not DERIVED; the positivity window's boundary is NOT located and no curve is fitted; and the coincidence of the complex-mode boundary with the Hodge edge |c| = 1 is MEASURED at the searched columns and NOT proved. SIX ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C1 MONIC-NORMALIZATION correction, carried as a formula with its scalar identified; the C2, C3 and C4 CONFIRMATIONS at both fresh points, extended here to all five; the P1 EXTREME-POINT failures, folded as the first half of the split; the P2 BOUNDARY HUNT and its 192-point census, folded as the block's centre; the P2 WARNING that irreducible-factor degree alone is not a valid positivity checker, which is why this block gates the perfect-square form and the scale census instead; and the P3 MONOTONICITY chain, reproduced exactly and fenced as discrete. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE (m,c) GENERALITY SOLVE (block 194 candidate), GEN PHASE 1 MEASURED, GEN PHASE 2 MEASURED and B194 CHECK VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **Locating the positivity boundary.** Stopped: a finite point search cannot
   locate a boundary, and fitting one would be the exact overreach `N0` forbids.
2. **Proving the universality of the structural legs.** Stopped: no argument
   from the staggered recurrence was found, and counting is not proving.
3. **Explaining the Hodge-edge coincidence.** Stopped: measured at three
   columns, mechanism unknown.
4. **A second width.** Stopped: this block varies `(m, c)` at `T = 16` only, and
   two variations at once would confound both.
5. **Anything downstream of `theta`.** Stopped at the fence: `theta` is a
   logarithm of an algebraic number and nothing in this block licenses more.

### REOPEN IF

1. A **symmetry or recurrence argument** is found that forces palindromicity and
   the perfect-square form for all `(m, c)` — that would convert `192/192` from
   a count into a theorem and is the single highest-value follow-on.
2. A **mechanism** is found linking `det g(c) < 0` to unimodular monodromy
   pairs, which would turn the Hodge-edge coincidence into a boundary result.
3. The positivity condition is reduced to a **closed-form inequality in
   `(m, c)`** — with `q(T)`'s coefficients now explicit, `q(2) > 0` and
   `alpha < -4` are two rational inequalities in `(m, c)` and this may be
   tractable directly.
4. A **second width** reproduces the split with the same column structure.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 193's #51. NO CORRECTION IS LANDED BY THIS
BLOCK AGAINST ANY LANDED NUMBER.** Six of the adversarial check's findings are
carried as **content** rather than as errata; three further items correct this
block's own solve language; and every one of the nine is a declared constant
with a gate and, where it guards a correction, a mutation.

52. **THE `C1` MONIC-NORMALIZATION CORRECTION.** The solve displayed
    `charpoly(W)` as an unnormalized product of integer quadratics. SymPy's
    characteristic polynomial is **monic**, so those equalities are **literally
    false**. Measured and repaired here as an identity rather than a hedge:
    `(a_1 z^2+b_1 z+a_1)^2 (a_2 z^2+b_2 z+a_2)^2 = s · charpoly_monic(W)` with
    `s = (a_1 a_2)^2` exactly, residual `0` at all five points. Gate `C-3`,
    mutation `break_monic_normalization`.
53. **POSITIVITY IS NOT GENERIC — THE SOLVE'S HEADLINE IS REFUTED.** The solve
    concluded "every leg of the transfer package is GENERIC over the `(m, c)`
    grid". The check's boundary hunt found `98` of `192` admissible searched
    points where positivity **fails**. **The package splits, and the split is
    this block's central result.** `POSITIVITY_GENERIC_CLAIMED = False`, gate
    `B-3`, mutation `claim_positivity_generic`.
54. **AND THE STRUCTURAL LEGS SURVIVE THE SAME HUNT UNTOUCHED.** The other half
    of the correction, and it is a positive one: palindromicity, the
    perfect-square form, `[W, U] = 0`, parity independence and the window cell
    hold at `192/192` — **including at every failing point**. The solve was
    right about the structure and wrong about positivity, and saying only the
    second half would be as inaccurate as saying only the first. Gates `F-2`,
    `F-6`.
55. **THE `t0 = 4` LEG WAS MIS-AIMED AND ITS `parityW` LINES ARE MEANINGLESS.**
    At `T = 16`, `t0 = 4 = T/2 - 4` is a **far boundary-layer** core, not the
    even-deep one. The solve's `t0 = 3` vs `t0 = 4` comparisons compared deep
    against boundary. The true parity test is `t0 = 2` vs `t0 = 3` and is `N2`;
    what `t0 = 4` actually establishes is that **Block 191's boundary-mode
    structure is `(m, c)`-generic**, which is `N2b`. Gates `D-1`, `E-1`.
56. **IRREDUCIBLE-FACTOR DEGREE IS NOT A VALID POSITIVITY CHECKER.** The check
    warned that at `(1/2, ±1/2)` and `(2, ±1/2)` a palindromic quadratic splits
    over `QQ` into reciprocal linear factors while the monic polynomial stays
    palindromic. Confirmed here, and acted on: this block gates the **degree-
    blind** perfect-square form and scale census instead, and carries two of
    those four points inside the re-measured subset. Gates `C-4`, `C-5`.
57. **THE FAILURE SET IS NOT ONE MODE — THIS BLOCK'S OWN REFINEMENT.** The check
    reported its failures as **negative reciprocal pairs**. Measured here: `36`
    of the `98` failures — exactly the points with `c > 1` — carry **complex
    unimodular** pairs and **no negative pair at all**. The scale census
    separates the modes exactly. `ALL_FAILURES_ARE_NEGATIVE_PAIRS = False`,
    gate `F-5`, mutation `break_failure_modes`.
58. **AND THE `c = 3/4` OBSERVATION EXTENDS TO FOUR WHOLE COLUMNS.** The check
    recorded that all twelve searched masses fail at `c = 3/4`. Measured here,
    the same holds at `9/10`, `19/20` and `99/100` — four mass-uniform columns,
    `48` points — and the three columns beyond the Hodge edge are mass-uniform
    in the complex mode. Gate `F-8`, mutation `break_census_columns`.
59. **THE CENSUS IS CITED, NOT GATED, AND THE BOUNDARY IS DECLARED.** The runner
    re-measures **twelve** points in full and cites the remaining `180`. Saying
    "`192/192`" without saying which of those numbers a gate actually verified
    would overstate the runner. Gate `F-6` states the boundary in its own text.
60. **"GENERIC" IS SCOPED, AND NO WINDOW CURVE IS DRAWN.** The solve's word
    *generic* is replaced throughout by **a count over `M × C`**, and the
    positivity window is reported as **measured points only** — no fitted edge,
    no interpolation, no extrapolation. `CENSUS_EXHAUSTIVE_CLAIMED = False`,
    `WINDOW_BOUNDARY_CURVE_CLAIMED = False`, gates `B-4`, `B-5`, `F-7`,
    mutations `claim_census_exhaustive`, `claim_window_boundary_curve`,
    `break_window_measured_only`.

### The adversarial check

Verdict carried as **STRUCTURE UNIVERSAL, POSITIVITY WINDOWED — AND THE SPLIT IS
THE THEOREM** (`sol xhigh`, cross-model, an independent compact rebuild from the
landed Block 190/191/192 notes rather than an invocation of any runner; findings
preserved at `b194_check_findings.md`, checker at `b194_exact_probe.py`).

**CONFIRMED EXACTLY, ON AN INDEPENDENT RECONSTRUCTION.** `C1`'s primitive
factors, positivity, two-scale separation and `[W, U] = 0` at both fresh points;
`C2`'s parity independence; `C3`'s whole-matrix window-cell invariance; `C4`'s
boundary-layer shape and non-reciprocal boundary factor; and `P3`'s five-point
monotonicity chain.

**CORRECTED, AND CARRIED AS A FORMULA:** `C1`'s displayed equalities
(correction 52).

**REFUTED AS WORDED, NOW THE BLOCK'S CENTRE RATHER THAN PROSE:** the solve's
generic positivity (correction 53).

**THE CHECK'S EXACT WITNESS IS REPRODUCED DIGIT FOR DIGIT.** The `(1/100, 3/4)`
factors, the monic scalar `5790210286399072239616` and the discriminants
`26772113593665` and `2036853665` are **declared literals** in this block's
runner rather than printed byproducts.

**AND THE CHECK IS EXTENDED IN THREE PLACES,** all three re-measured
independently here: the second failure mode and its Hodge-edge location
(correction 57), the four mass-uniform negative columns (correction 58), and the
degree-blind positivity route the check's own warning implied (correction 56).

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–193 number **stands as landed**.
Block 193's parity-resolved window law is carried unchanged and its `{2,3}` cell
at `t0 = 5` is gated as an **instance** at five new `(m, c)` points. Block 191's
boundary-mode structure is confirmed, not revised. Block 188's two
known-positive fixtures are reproduced as positive. Block 190's refutation of
the naive OS transfer pairing stands and nothing here repairs it.

### Reproduction

```text
python3 scripts/admissibility_dirac_kahler_transfer_package_mc_generality_2026_08_25.py
python3 ... --list-mutations
python3 ... --mutation claim_positivity_generic
```

Baseline expectation: families `A` through `H` PASS. Thirty-six declared
mutations, each flipping **exactly one** family and exiting nonzero; per-family
census `A 2, B 8, C 6, D 3, E 3, F 8, G 4, H 2`. Every measurement is taken
once, before any mutation flag is read, so no gate can cascade into another.
Every `64 × 64` exact inverse is built once per `(m, c, profile)` and shared.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE (m,c) GENERALITY SOLVE
(block 194 candidate)**, **GEN PHASE 1 MEASURED**, **GEN PHASE 2 MEASURED** and
**B194 CHECK VERDICT** anchors.
