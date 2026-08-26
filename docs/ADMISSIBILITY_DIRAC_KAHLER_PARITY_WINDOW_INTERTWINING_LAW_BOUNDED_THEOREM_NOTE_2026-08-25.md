---
title: "Admissibility — Dirac-Kähler Parity-Resolved Window Law Of The Intertwining Residual"
date: 2026-08-25
block: 193
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_parity_window_intertwining_law_2026_08_25.py
parent_ref: origin/physics-loop/toe-axiom-closure-block192-hybridization-mechanism-20260825
parent_commit: afb66fc43c8858cc6a1d4cf943a14085e45be3f1
current_main: b11811704efa98a12272d572f666e530a807f6c1
registered: 0
adopted: 0
axiom_movement: none
---

# The Parity-Resolved Window Law Of The Intertwining Residual, And The Bilinear Mechanism That Produces It — with WINDOW, TRANSPORT and HARMONIC fenced as names for matrix properties throughout

**One sentence.** On Block 190's wrap-edge width family at the same fixture
`(m, c) = (9/20, 5/13)` and at **two** widths `T = 16` and `T = 20`, Block 192's
named open leg is closed by reduction: the first-order intertwining residual
`R = dL_2 - dK_c W` is resolved into a **bilinear form**
`R[a,b] = -u_b^T dQ G[:, theta_a]`, the exact set of one-cell Hodge tangents
that make it nonzero is determined to be a **three-slice window whose exempt
end switches with the parity of the core**, and `W(delta) = W(0)` matrix-exact
is measured to be **equivalent** to `R = 0` in both directions over sixty exact
finite rebuilds — and **not one line of this supplies a light cone, a locality
principle, a propagation speed or a continuum limit**.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Seven imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE LOCALITY LANGUAGE IS FENCED BEFORE THE FIRST NUMBER IS READ.**

- **NO GRAVITY IS SUPPLIED.** `delta` is a dial on the **imposed Hodge-volume
  parameter** of Block 105's `shear_hodge(c, v)`, and *response* names
  `d/d(delta)` of a rational matrix entry at `delta = 0`. This block supplies
  **no lapse variable in an ADM phase space, no Hamiltonian constraint, no
  gauge orbit, no quotient, no Dirac observable and no OS reconstruction** that
  would make `W` a physical transfer operator.
- **"WINDOW", "TRANSPORT", "HARMONIC" AND "RESPONSE" NAME PROPERTIES OF EXACT
  RATIONAL MATRICES.** *Window* names the set of time slices carrying the
  nonzero rows of eight explicitly constructed vectors. *Two-step transport*
  names the linear relation `L_2 = K_c W`. *Q-harmonic* names membership in the
  kernel of `Q` on the rows where a source vanishes. None of the four names a
  cone, a horizon, a signal or a speed.
- **THE WINDOW IS NOT A LIGHT CONE AND NOT A LOCALITY PRINCIPLE.** It is a
  statement about which exact `8 x 8` rational matrices are zero. **No
  propagation speed, no causal structure, no screening length and no continuum
  limit** is supplied or implied, and the window is not even symmetric about the
  core — its exempt end is at the top for odd cores and at the bottom for even
  ones (`N3`).
- **THE PARITY-INDEPENDENT WINDOW IS REFUTED, NOT SOFTENED AND NOT
  RENORMALIZED.** The solve proposed the single window `[t0, t0+2]` for every
  core. The adversarial check measured the **even** cores carrying
  `[t0+1, t0+3]` instead, and this block reproduces that independently: at
  `t0 = 2` the anchors `s = 1` and `s = 5` carry the **opposite** statuses from
  the solve's rule, and the admissible `t0+3` cell **breaks** with `nnz(R) = 32`
  exactly where the odd cores exempt it. `PARITY_INDEPENDENT_WINDOW_CLAIMED =
  False` is a declared constant with a gate and a mutation. See correction 42.
- **AND THE LAW IS NOT PROVED FROM THE STAGGERED RECURRENCE.** It is **reduced**
  to the bilinear identity plus **two measured support facts**, and the closed
  forms of those two supports are **measured at two widths and derived from
  nothing**. `LAW_PROVED_FROM_RECURRENCE_CLAIMED = False`, gate `B-7`.

**TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED**, so the absence is a
count and not a mood: lapse function; shift vector; ADM phase space;
Hamiltonian constraint; momentum/diffeomorphism constraint; first-class
constraint algebra; Dirac closure; Dirac observable; gauge orbit and its
quotient; Osterwalder–Schrader reconstruction of a transfer operator.

**NO GENERALITY IS CLAIMED.** One fixture `(9/20, 5/13)`, two widths `T = 16`
and `T = 20`, one profile family, three amplitudes `delta = 1/5, 1/3, 2/5`.
**Two widths are not a scan and one fixture is not a family.**

**THE OBJECT IS STILL A DISCLOSED VARIANT.** The carrier is Block 190's
wrap-edge family (`w = -1` at `t = T-1`), which is **not** Block 188's landed
`T = 8` object (`w = -1` at `t = 3`). Blocks 188 through 192 are neither
corrected nor contradicted by anything below.

---

## W1 — the wall, and the charter

### What was open

Block 192 established an exact **support cutoff**: over its twelve valid
`(bump, core)` pairs the monodromy response vanished at exactly three. It left
three things explicitly open in its own `N6`:

1. **The mechanism was not derived.** "Empty-cross routing" was named as a
   **reading and an open leg**, and its naive support form was refuted there by
   a dense `dG` (`3968` of `4096` entries).
2. **Its overlap signature had one counterexample.** Comparing the bump's `dH`
   support against the core's read window `{t0, t0+1, t0+2, t0+3}` predicted a
   nonzero response at `({4,5}, t0 = 1)`, which is exactly `0_8`.
3. **Twelve pairs is not a law.** Cores `t0 = 0, 2, 4` were not probed, `T = 20`
   was not probed, and the four bump positions were not a scan.

### The charter

1. **Refine the source** from a two-anchor bump to a **single reflected cell**,
   so that the incidence question has an answer per slice rather than per bump.
2. **Prove the equivalence** `W(delta) = W(0) <=> R = 0` in **both** directions,
   at first order and at three exact finite amplitudes.
3. **Derive the residual** as a closed-form bilinear pairing so that the whole
   question becomes a statement about **supports**.
4. **Tabulate the incidence exhaustively** at two widths and every core parity,
   and say exactly which cell breaks and which does not.
5. **Carry the adversarial check's refutation as the block's central law**, and
   attack the surviving exemption until it either falls or is exhausted.

---

## N1 — THE EQUIVALENCE, and it is measured in both directions

**NOTHING BELOW IS ABOUT THE LANDED CHAIN'S OBJECT IF THIS SECTION IS NOT
EXACT.**

### The one new construction element

Block 192 perturbed with a **bump**: two adjacent positive anchors at once. This
block perturbs with **one cell**. For a positive anchor `s` and a spatial anchor
`x`, with `E(t,x)` the four-corner cell embedding and `thA_s(t) = -1-t`:

```text
dH(s, x) = (1/4) E(s, x)          dB              E(s, x)^T
         + (1/4) E(thA_s(s), x)  P_4 dB P_4^T    E(thA_s(s), x)^T,

dB = d/d(delta) shear_hodge(c, 1 - delta) |_{delta = 0}
   = -E00 - (169/144)(E11 + E22) + (65/144)(E12 + E21) + E33.
```

`dB` is gated **entrywise at zero** against the symbolic derivative of the
imported `shear_hodge`, and the underlying law is gated at both probed volumes —
thirty-two numbers, gate `C-1`. And the refinement is gated against what it
refines:

```text
sum_{s in A} sum_{x=0..3} dH(s, x)  =  Block 192's bump tangent dH_A,
```

at **zero residual at all four of Block 192's bumps**, gate `C-2`. The one-cell
tangent is a *decomposition* of the landed object, not a different object.

### The residual, and the two tables

With `dQ = m dH + dH D_s - D_s^T dH` (exact, because `D_s` does not depend on
the profile), `dG = -G dQ G`, and `dK_c`, `dL_2` the core restrictions of `dG`:

```text
R := dL_2 - dK_c W,        dW = K_c^-1 R,        so  R = K_c dW.
```

Over the **twenty** valid `(bump, core)` pairs at `T = 16` — Block 192's four
bumps against cores `t0 = 1, 2, 3, 4, 5` — `nnz(R)` is

| `nnz(R)` | `t0 = 1` | `t0 = 2` | `t0 = 3` | `t0 = 4` | `t0 = 5` |
| --- | ---: | ---: | ---: | ---: | ---: |
| bump `{1,2}` | `64` | `64` | `64` | **`0`** | **`0`** |
| bump `{2,3}` | `64` | `64` | `64` | **`0`** | **`0`** |
| bump `{3,4}` | `64` | `64` | `64` | `64` | `64` |
| bump `{4,5}` | **`0`** | `32` | `64` | `64` | `64` |

**Five exact zeros, fourteen full entries and one at HALF density.** The three
odd-core columns are Block 192's landed twelve-entry cutoff table, reproduced
here entry for entry as this block's control (gate `C-8`).

### And the finite table is the same table, entry for entry

`nnz(W(delta) - W(0))` is rebuilt from scratch at **three** exact amplitudes —
`delta = 1/5`, `1/3` and `2/5` — over all twenty pairs, sixty finite rebuilds:

```text
nnz(W(delta) - W(0))  ==  nnz(R)     for every (bump, core) and every delta,
                                     ENTRY FOR ENTRY, all sixty.
```

That is strictly stronger than the biconditional it implies. In particular the
`32` at `({4,5}, t0 = 2)` is a `32` at every amplitude, so the half-density
break is **not** a first-order artefact. Gates `C-4`, `C-5`, `C-6`.

**Therefore, measured in both directions over sixty cells:**

```text
W(delta) = W(0)  matrix-exact   <=>   R = dL_2 - dK_c W = 0.
```

The adversarial check's six requested cells sit inside this table: the zeros
`({1,2}, 5)`, `({2,3}, 5)`, `({4,5}, 1)` and the dense
`({3,4}, 5)`, `({2,3}, 1)`, `({2,3}, 3)`, at first order **and** at both of its
amplitudes. Gate `C-7`.

### The route is gated against the definitional one

Everything below computes `R` from the eight-row/eight-column contraction of
`N2b` rather than by forming the whole `64 x 64` `dG`. The two routes are
compared entrywise at **ten** gate pairs — one breaking and one compatible
anchor at each of the five cores — at **zero residual**, gate `C-3`. And the
carrier controls close at **both** widths:

```text
nnz(Q G - I) = nnz(Ps H Ps - H) = nnz(Ps Q Ps - Q^T) = 0   at T = 16 and T = 20.
```

---

## N2 — THE HARMONIC-RESPONSE DERIVATION, in three pillars

### The object that does all the work

For the core `t0`, index its eight cells `b <-> (t_b, x_b)` with
`t_b in {t0, t0+1}`. The **two-step transport defect functional** of the `b`-th
column is the vector

```text
d_b  :=  e_{(t_b+2, x_b)}  -  sum_{b'} W[b', b] e_{(t_b', x_b')}     in QQ^{4T}.
```

It has at most nine nonzero entries: one at `t_b + 2` — which is `t0+2` for
the four `t0` cells and `t0+3` for the four `t0+1` cells — and up to eight on
the read pair `{t0, t0+1}`.

### Pillar 1 — `W` is DEFINED by the transport relation, not fitted

`K_c W = L_2` is, entry for entry, the statement

```text
G[(t_b+2, x_b), theta_a]  =  sum_{b'} G[(t_b', x_b'), theta_a] W[b', b],
i.e.        d_b^T G[:, theta_a] = 0        for all a, b.
```

Measured `nnz(K_c W - L_2) = 0` at **every** core frame at **both** widths —
sixteen frames — gate `D-1`. This is an identity of the definition and it is
what the rest of the derivation perturbs.

### Pillar 2 — the response field is `Q`-harmonic off the source

Set

```text
y_a := dQ G[:, theta_a],        rho_a := G y_a  =  -dG[:, theta_a].
```

Then `Q rho_a = y_a` trivially, so `rho_a` lies in `ker Q` on **every row where
`y_a` vanishes**. That is only content if `y_a` does not vanish more than `dQ`
does, and it does not:

```text
row support of y_a  ==  row support of dQ,   in all 240 tested columns,
                                             with ZERO cancellations,
Q rho_a - y_a = 0,                           ZERO failures in the same 240.
```

The `dQ` row-support sizes for the one-cell tangents at anchors `s = 0..7` are

```text
T = 16:  (12, 14, 16, 16, 16, 16, 14, 12),
T = 20:  (12, 14, 16, 16, 16, 16, 16, 16, 14, 12),
```

and — this is the fact the whole law rests on — the **positive-half slice
support** is exactly

```text
supp_slices(dQ_s) ∩ {0..T/2}  =  [ 2*floor(s/2),  2*floor(s/2) + 2 ],
```

three slices, **not** the four that a naive range count of `D_s` would give:
for even `s` the lower tail `s-1` is killed and for odd `s` the upper tail
`s+2` is. Gates `D-2`, `D-3`, `D-4`.

### Pillar 3 — `R = 0` is EXACTLY the same relation, applied to the response

```text
R[a, b]  =  - d_b^T rho_a.
```

Measured as `nnz(relation + R) = 0` at **all thirty** `(anchor, core)` pairs at
`T = 16`, gate `D-5`. So the content of `R = 0` is precisely:

> the perturbed response field obeys the **same** two-step transport relation on
> the core frame that the unperturbed columns obey by definition.

And since `R = K_c dW` with `K_c` invertible, `R = 0` if and only if `dW = 0`.
Measured `nnz(dW) = nnz(R)` and `nnz(K_c dW - R) = 0` at all **forty** cells,
gate `D-7`.

---

## N2b — THE BILINEAR FORM, and it turns the law into a support statement

Writing `u_b := G^T d_b` — so `u_b[i] = G[(t_b+2, x_b), i] - sum_{b'} W[b',b]
G[(t_b', x_b'), i]` — and `c_a := G[:, theta_a]`, pillar 3 becomes

```text
R[a, b]  =  - u_b^T dQ c_a.
```

**`R` is therefore LINEAR in the Hodge tangent**, and the entire incidence
question is a question about the **support of the eight vectors `u_b`**.
Expanding `dQ`'s definition once gives the closed form for a raw tangent
`dH = E_{p,q}` with no matrix product at all:

```text
R[a, b]  =  -( u_b[p] * ((m I + D_s) c_a)[q]  -  (D_s u_b)[p] * c_a[q] ).
```

That closed form is gated against the matrix route at eight `(p, q)` gates at
zero residual, gate `D-6`. It is what makes the exhaustive censuses of `N3b`
and `N4` computable at all.

Note also what pillar 1 says in this notation: `d_b^T G[:, theta_a] = 0` is
`u_b[theta_a] = 0`. **The eight functionals vanish at the eight `theta_s`
partner sites by construction**; where else they vanish is measured, and is the
whole of `N4`.

---

## N3 — THE PARITY-RESOLVED WINDOW LAW, and it is this block's centre

**THIS IS THE ADVERSARIAL CHECK'S P2 DISCOVERY, CARRIED AS THE LAW AND
CREDITED.**

### The table, exhaustively, at `T = 16`

Anchors `s = 0..7` against cores `t0 = 1..5`, every one of the four spatial
anchors giving the identical pattern — **forty cells**:

| `nnz(R)` | `s=0` | `s=1` | `s=2` | `s=3` | `s=4` | `s=5` | `s=6` | `s=7` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `t0 = 1` (odd) | `64` | `64` | `64` | `64` | `0` | `0` | `0` | `0` |
| `t0 = 2` (even) | `0` | `0` | `64` | `64` | `32` | `32` | `0` | `0` |
| `t0 = 3` (odd) | `0` | `0` | `64` | `64` | `64` | `64` | `0` | `0` |
| `t0 = 4` (even) | `0` | `0` | `0` | `0` | `64` | `64` | `32` | `32` |
| `t0 = 5` (odd) | `0` | `0` | `0` | `0` | `64` | `64` | `64` | `64` |

**Read the parity.** The break interval moves by **two** from `t0 = 1` to
`t0 = 2` and then **stands still** from `t0 = 2` to `t0 = 3`. It is not a
function of `t0`; it is a function of `floor(t0/2)`.

### The law

```text
A reflected one-cell tangent at anchor s BREAKS the intertwining identity
at core t0  <=>  s in [ 2*floor(t0/2),  2*floor(t0/2) + 3 ]
            <=>  {s, s+1}  meets  W(t0),

with the EFFECTIVE RESPONSE WINDOW

W(t0)  =  [ 2*floor(t0/2) + 1,  2*floor(t0/2) + 3 ]
       =  [ t0,   t0+2 ]     for ODD  t0,
       =  [ t0+1, t0+3 ]     for EVEN t0.
```

**The core's footprint is four slices `{t0, t0+1, t0+2, t0+3}` — the read pair
that `K_c` samples and the predicted pair that `L_2` samples — and the window is
always exactly three of them, with ONE exempt end that SWITCHES WITH PARITY:**

```text
ODD  t0:  the LAST predicted slice  t0+3  is exempt,
EVEN t0:  the FIRST read slice      t0    is exempt.
```

Gates `E-1`, `E-3`.

### The same law at a second width

At `T = 20` the valid cores are `t0 = 1..7` and the anchors are `s = 0..9` —
**seventy cells**, spatially uniform, **zero exceptions**:

| `nnz(R)` | `s=0` | `s=1` | `s=2` | `s=3` | `s=4` | `s=5` | `s=6` | `s=7` | `s=8` | `s=9` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `t0 = 1` | `64` | `64` | `64` | `64` | `0` | `0` | `0` | `0` | `0` | `0` |
| `t0 = 2` | `0` | `0` | `64` | `64` | `32` | `32` | `0` | `0` | `0` | `0` |
| `t0 = 3` | `0` | `0` | `64` | `64` | `64` | `64` | `0` | `0` | `0` | `0` |
| `t0 = 4` | `0` | `0` | `0` | `0` | `64` | `64` | `32` | `32` | `0` | `0` |
| `t0 = 5` | `0` | `0` | `0` | `0` | `64` | `64` | `64` | `64` | `0` | `0` |
| `t0 = 6` | `0` | `0` | `0` | `0` | `0` | `0` | `64` | `64` | `32` | `32` |
| `t0 = 7` | `0` | `0` | `0` | `0` | `0` | `0` | `64` | `64` | `64` | `64` |

The adversarial check's nine-cell `T = 20` spot check — anchors `{3,4,7}`
against cores `{3,5,7}` — is the sub-table of this one, and agrees in all nine.
Gate `E-2`.

### The break density is a fingerprint, not a binary

Over the four breaking anchors `2*floor(t0/2) .. 2*floor(t0/2)+3` **in order**:

```text
ODD  cores:  (64, 64, 64, 64)      -- every break is a FULL 8 x 8,
EVEN cores:  (64, 64, 32, 32)      -- the two upper breaks are HALF-dense.
```

At both widths, at every valid core. Gate `E-4`. The `32` is not a near-miss:
it is `32` at first order and `32` at every one of the three finite amplitudes
(`N1`), so it is a genuine half-rank feature of the even cores and not a
cancellation that a larger `delta` would fill in.

### The law's domain is exactly Block 191's touch/cross rule, measured

The cores that violate `t0 + 3 <= T/2` — `t0 = 6, 7` at `T = 16` and
`t0 = 8, 9` at `T = 20` — **do not obey the law**, and their functionals do not
carry a three-slice window at all:

```text
t0 = 6, T = 16:  supp_slices(u) = {0..8, 11..15},   NOT a three-slice window,
t0 = 7, T = 16:  supp_slices(u) = {0..7, 10..15},   NOT a three-slice window.
```

The validity rule is therefore not a bookkeeping convenience carried over from
Block 191 — it is **where this law's hypotheses actually stop**, and it is
recorded as a measurement rather than as an assumption. Gate `E-9`.

An exact unexpected-break witness, digit for digit as the adversarial check
recorded it, at `(t0, s) = (2, 5)`:

```text
R[0,4] = 303717414128393981002946552450301011272963193469691599136505997554493148222247708710000000
         /77707725095998816829080256798567544217876202163787270905242891606801827087957579200283634261.
```

Under the solve's parity-independent rule that cell was predicted compatible.
It is not.

---

## N3b — THE EXEMPTION, ATTACKED EXHAUSTIVELY, AND ITS DUAL

The exempt end is the sharp part of the law, so it is attacked rather than
asserted. At the odd cores `t0 = 1, 3` the high end `s = t0 + 3` survives
**every** attack:

| attack at odd `t0` | directions | breaks |
| --- | ---: | ---: |
| the admissible one-cell tangent, all four spatial anchors | `4` | `0` |
| all `4 x 4` cell-block matrix-unit directions, **including the eight asymmetric ones** | `16` | `0` |
| raw units with row on any positive slice `t0+3 .. T/2`, **arbitrary column** (`t0 = 1`) | `1280` | `0` |
| the same at `t0 = 3` | `768` | `0` |

**No linear Hodge tangent whose positive-side row support begins at `t0+3` can
break the odd-core relation.** Gate `E-5`.

**And at the even cores that same exemption is FALSE, measured:**

| the same attack at even `t0` | directions | breaks |
| --- | ---: | ---: |
| the admissible `t0+3` cell, all four spatial anchors | `4` | `4`, each at `nnz(R) = 32` |
| the sixteen cell-block directions | `16` | `8` |
| raw units, row on slices `t0+3 .. T/2`, arbitrary column (`t0 = 2`) | `1024` | `256` |
| the same at `t0 = 4` | `512` | `256` |

What the even cores carry instead is the **dual** exemption at the **low** end,
and it is exhaustive there — and it fails at the odd cores, which is the parity
switch seen from the other side:

| low-end census, rows on slices `0 .. t0` | directions | breaks |
| --- | ---: | ---: |
| `t0 = 2` (even) | `768` | `0` |
| `t0 = 4` (even) | `1280` | `0` |
| `t0 = 1` (odd) | `512` | `256` |
| `t0 = 3` (odd) | `1024` | `256` |

Gate `E-6`. **The exempt end is not an accident of the cell source's shape: it
is a property of the whole tangent space at that core, and it switches with
parity.**

---

## N4 — THE MECHANISM, reduced to two measured support facts

### Support fact one: the functionals ARE the window

```text
union_b  supp_slices(u_b)  =  [ 2*floor(t0/2) + 1,  2*floor(t0/2) + 3 ],
```

at **every** valid core, at **both** widths, with **no negative-half support at
all**. Gate `E-7`. And the structural origin of the shift is visible in the
per-functional breakdown: at every **even** core exactly **four** of the eight
functionals **collapse** to a single slice with four nonzero entries,

```text
even t0:  supp_slices(u_b) = { t0+1 }        for b = 0..3   (the t0 cells),
                           = { t0+1, t0+2, t0+3 }  for b = 4..7,
odd  t0:  supp_slices(u_b) = { t0, t0+1, t0+2 }    for ALL eight b.
```

The four `t0`-row functionals of an even core carry **nothing at slice `t0`**.
That is the exempt end, in one line.

### Support fact two: the source's rows

```text
supp_slices(dQ_s) ∩ {0..T/2}  =  [ 2*floor(s/2),  2*floor(s/2) + 2 ],
supp_rows(dH(s,x))            =  slices {s, s+1}  and  their thA_s images.
```

### The law follows

Since `R[a,b] = -u_b^T dQ c_a`, a tangent whose `dQ` rows miss `supp(u_b)`
gives `R = 0` **immediately**. Measured, the converse holds too, and in its
sharpest form — on raw Hodge-tangent matrix units, where the column is
irrelevant:

```text
R(E_{p,q}) != 0   <=>   the ROW slice of p lies in W(t0),   for EVERY column q.

T = 16:  5 valid cores x 4096 units = 20480,   768 breaking per core,
T = 20:  7 valid cores x 6400 units = 44800,   960 breaking per core,
                                      65280 units,  ZERO mismatches.
```

Gate `E-8`. The cell law is then a corollary: `dH(s,x)` has rows exactly on
`{s, s+1}` and on its two image slices, the image slices lie in
`{0} ∪ [T/2, T-1]`, and every window measured here lies inside `[1, T/2 - 1]` —
so the image rows never meet `W(t0)` and the cell breaks **if and only if**
`{s, s+1}` meets `W(t0)`. (That last containment is a measurement over the
twelve valid cores of the two widths, not a general fact about `T`.)

### Block 192's open leg, and its one counterexample

Block 192's overlap signature compared the bump's **`dH`** support against the
**naive four-slice read window** `{t0, t0+1, t0+2, t0+3}`, and had exactly one
counterexample. Replace the two wrong objects by the two measured ones — `dQ`'s
support, and `supp(u_b)` — and the counterexample becomes an ordinary instance:

```text
bump {4,5}:   supp_slices(dQ)  =  {4, 5, 6}      (positive half),
core t0 = 1:  W(1)             =  {1, 2, 3},
              intersection      =  EMPTY          ->   R = 0.
```

The naive window was **one slice too wide** at odd cores; that one slice is
`t0+3`, and it is exactly the exempt end. **There is no counterexample left
among the twenty pairs.** Corrections 46 and 47.

### What is NOT closed

The two support facts are **measured**. Their closed forms hold at two widths
and at every valid core tested, and they are **not derived from the staggered
recurrence**. A proof would have to show, from `Q = m H + H D_s - D_s^T H` and
the grading, why `G^T d_b` vanishes off three slices. That is the named open
leg this block leaves, and `B-7` gates it.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

| word | what it names in this block | what it does NOT name |
| --- | --- | --- |
| *window* | the slices carrying the nonzero rows of eight explicit rational vectors | a light cone, a causal horizon, a support of a signal |
| *transport* | the linear relation `L_2 = K_c W` between exact rational matrices | motion of anything through anything |
| *harmonic* | membership in `ker Q` on rows where a source vanishes | a wave, a mode, a field equation of physics |
| *response* | `d/d(delta)` of a rational matrix entry at `delta = 0` | any physical perturbation of any system |
| *read slice*, *predicted slice* | which shifted pairing samples the slice, `K_c` or `L_2` | past and future |
| *exempt end*, *parity switch* | index arithmetic on `{0..T/2}` | a chirality, a sublattice symmetry of nature |

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within one imposed finite matrix construction at one fixture and two widths,
> the first-order derivative of an exact rational `8 x 8` matrix with respect to
> a one-cell dial on an imposed Hodge-volume parameter is the exact zero matrix
> for precisely those dial positions whose two-slice support misses a
> three-slice interval determined by `floor(t0/2)`; the same zero set is
> reproduced by exact rebuilds at three finite dial values; and the residual
> that decides it is a bilinear pairing of two explicitly constructed families
> of rational vectors.

### Three further fences, all three self-imposed

1. **The bilinear identity is a rewriting, not an explanation.** That
   `R[a,b] = -u_b^T dQ c_a` follows from `dG = -G dQ G` and the definitions in
   three lines. It earns its place because it converts an incidence question
   into a support question — not because it explains why the support is what it
   is.
2. **Two widths is not a width family.** `T = 16` and `T = 20` share
   `T/2` even; nothing here probes `T/2` odd, and no infinite-width statement
   is made or implied.
3. **The half-density `32` is a measured count, not a rank claim.** No rank,
   kernel dimension or invariant subspace of the even-core residual is computed
   or asserted.

### What IS derived, stated positively so the fence is not mistaken for a retreat

The chain of `N2` consists of **theorems about this construction**, not
measurements: `K_c W = L_2` is `d_b^T G[:, theta_a] = 0` by definition;
`Q rho_a = y_a` is immediate; `R[a,b] = -d_b^T rho_a` is the derivative of the
same relation; `R = K_c dW` is the derivative of a quotient; and the bilinear
form and its raw-unit closed form follow by expanding `dQ` once. **All of that
transfers to any profile, any core and any width of this family unchanged.**
What does not transfer without measurement is the *support* of `u_b`.

---

## READINGS — five of them, and each is a reading

- **`R1`.** *That the window is a lattice light cone or a finite propagation
  speed.* Measured: which exact rational matrices are zero. The window is not
  symmetric about the core and its exempt end **switches with parity**, which is
  already evidence against the reading. **Reading.**
- **`R2`.** *That the read/predicted split is a past/future split.* `K_c` and
  `L_2` are two shifted samplings of one symmetric rational matrix `G`.
  **Reading.**
- **`R3`.** *That the parity switch reflects a physical sublattice or chirality.*
  Measured: `supp(u_b)` depends on `t0` through `floor(t0/2)`. The staggered
  sign `eta_x = (-1)^t` is in the construction by hand. **Reading.**
- **`R4`.** *That "`Q`-harmonic" means the response solves a field equation.*
  It means a vector lies in a kernel on some rows. **Reading.**
- **`R5`.** *That the half-density `32` at the even cores is a rank-four
  response.* It is a count of nonzero entries. No rank is computed.
  **Reading.**

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | family |
| ---: | --- | --- | --- |
| 1 | `origin/main`, axiom and registry blobs, worktree blobs, timeout | five pins fixed | `A` |
| 2 | `PARENT_COMMIT` ancestry, both Block 192 artifacts, stale pin carrying neither | exact | `A` |
| 3 | imposed / registered / adopted | `7 / 0 / 0` | `B` |
| 4 | gravity structures enumerated as NOT SUPPLIED | `10` | `B` |
| 5 | `GRAVITY_SUPPLIED`, `LOCALITY_SUPPLIED`, `CONTINUUM_LIMIT`, `TRANSFER_OPERATOR`, `GENERALITY` | all `False` | `B` |
| 6 | `PARITY_INDEPENDENT_WINDOW_CLAIMED` | `False` — the refuted window | `B` |
| 7 | `LAW_PROVED_FROM_RECURRENCE_CLAIMED` | `False` — the named open leg | `B` |
| 8 | `dB` vs the symbolic derivative of the import; the law at both volumes | residual `0`, 32 numbers | `C` |
| 9 | `(nnz(QG - I), nnz(Ps H Ps - H), nnz(Ps Q Ps - Q^T))` at `T = 16` and `T = 20` | `(0,0,0)`, `(0,0,0)` | `C` |
| 10 | `sum_{s,x} dH(s,x) - ` Block 192's bump tangent, all four bumps | `0` | `C` |
| 11 | the defect route vs the full `dG` route, ten gate pairs | residual `0` | `C` |
| 12 | `nnz(R)` over the twenty valid `(bump, core)` pairs | the table in `N1` | `C` |
| 13 | `nnz(W(delta) - W(0))` at `delta = 1/5, 1/3, 2/5`, sixty rebuilds | the same table, entry for entry | `C` |
| 14 | `W(delta) = W(0) <=> R = 0`, both directions | `True`, sixty of sixty | `C` |
| 15 | the check's six cells: three zeros, three dense | exact | `C` |
| 16 | Block 192's twelve-entry cutoff table and its three cutoff pairs | reproduced; instances | `C` |
| 17 | `nnz(K_c W - L_2)` at sixteen core frames, both widths | `0` | `D` |
| 18 | `dQ` row-support sizes; positive slice supports | `(12,14,16,…)`; `[2⌊s/2⌋, 2⌊s/2⌋+2]` | `D` |
| 19 | row support of `y_a` `==` row support of `dQ`, 240 columns | `0` mismatches | `D` |
| 20 | `Q rho_a - y_a`, same 240 columns | `0` failures | `D` |
| 21 | `nnz(response relation + R)`, thirty `(anchor, core)` pairs | `0` | `D` |
| 22 | the raw-unit closed form vs the matrix route, eight gates | residual `0` | `D` |
| 23 | `R = K_c dW`; `nnz(dW) = nnz(R)` at forty cells | residual `0`; equal | `D` |
| 24 | the forty-cell incidence table at `T = 16`, spatially uniform | the table in `N3` | `E` |
| 25 | the seventy-cell incidence table at `T = 20`, spatially uniform | law holds, zero exceptions | `E` |
| 26 | the window: three of four footprint slices, offsets `(0,2)` odd / `(1,3)` even | parity-switched | `E` |
| 27 | the break density over the four breaking anchors | `(64,64,64,64)` / `(64,64,32,32)` | `E` |
| 28 | the odd-core exemption census: `4`, `16`, `1280`, `768` directions | `0` breaks | `E` |
| 29 | the even-core refutation and the dual low-end exemption | `32`; `8/16`; `256/1024`, `256/512`; `0/768`, `0/1280` | `E` |
| 30 | `union_b supp_slices(u_b)` `==` the window; four collapsed functionals per even core | `True`; `4` | `E` |
| 31 | the raw-unit law over `20480 + 44800` units | `0` mismatches; `768`/`960` breaking | `E` |
| 32 | the validity boundary and the exact `(2,5)` witness | law fails outside `t0+3 <= T/2`; exact | `E` |
| 33 | the note at its final path; `N5` byte-identical; `sp.nsimplify` count | present; verbatim; `0` | `F` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

1. **THE ROUTE THAT WAS NOT TAKEN: forming `dG` per direction.** Block 192's
   route builds the whole `64 x 64` `dG = -G dQ G` for each tangent. At four
   bumps that is affordable; at `65280` raw tangent directions it is not. The
   bilinear form of `N2b` reduces each direction to a scalar pair, and **the
   only `delta = 0` inverses ever formed are one `64 x 64` and one `80 x 80`,
   each built once and shared by every core, every anchor and every census in
   the block.** The definitional route is kept and gated (`C-3`) precisely
   because the fast one is the whole computation.
2. **THE SUPPORT ACCOUNT THAT WAS REFUTED, AND WHY IT WAS NEARLY RIGHT.**
   Block 192 tested `dH`-support against the four-slice read window and found
   one counterexample. Both objects were wrong by one step: `dH` is not what
   pairs against `u_b` (`dQ` is), and the read window is one slice too wide at
   odd cores. Fixing both makes the signature exact on all twenty pairs. **The
   conjecture was not dropped and it was not kept; it was corrected in two named
   places.**
3. **THE PARITY WAS FOUND BY BEING WRONG ABOUT IT.** The solve proposed one
   window for all cores on the strength of an eighteen-cell odd-core census.
   The adversarial check ran the even cores and refuted it in two entries. The
   even cores were not "more of the same data" — they were the only data that
   could have falsified the rule, and they did.
4. **THE `s = 0` AND `s = T/2 - 1` ANCHORS WERE MISSING FROM THE SOLVE'S
   CENSUS, AND THEY ARE THE ONES THAT PIN THE INTERVAL.** The solve tabulated
   `s = 1..6`. At `t0 = 1` the break set is `{0,1,2,3}` and the solve saw only
   `{1,2,3}`; at `t0 = 5` it is `{4,5,6,7}` and the solve saw only `{4,5,6}`.
   Both endpoints touch a fixed slice (`0` or `T/2`) and both **obey the law**.
   Without them the break set looks like three cells at `t0 = 1` and four
   elsewhere, which is what made a `floor(t0/2)` reading invisible.
5. **THE INVALID CORES WERE RUN ON PURPOSE.** `t0 = 6, 7` at `T = 16` are
   outside Block 191's touch/cross rule and were measured anyway. They do not
   obey the law and their functionals are nearly dense. That is the difference
   between a validity rule that is carried forward and one that is **shown to
   be load-bearing**.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE LOCALITY LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13)), BLOCK 191's VOLUME PROFILE AND BLOCK 192's BUMP FAMILY v = 1 - delta AT THE THREE AMPLITUDES 1/5, 1/3 AND 2/5, THE REFLECTED ONE-CELL HODGE TANGENT dH(s,x) -- THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT -- THE PROBE DOMAIN of anchors s = 0..T/2-1 at all four spatial anchors against cores t0 = 1..T/2-1 under BLOCK 191's touch/cross rule t0+3 <= T/2, THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE TWO-STEP TRANSPORT DEFECT FUNCTIONALS d_b AND u_b = G^T d_b, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module AT A SYMBOLIC VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED AND NO LOCALITY PRINCIPLE IS ESTABLISHED: delta is a dial on an IMPOSED Hodge-volume parameter, 'response' names d/d(delta) of a rational matrix entry at delta = 0, and this block supplies NO lapse variable in an ADM phase space, NO Hamiltonian constraint, NO gauge orbit, NO quotient, NO Dirac observable and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, THE EXACT SET OF ONE-CELL HODGE TANGENTS THAT MAKE THE FIRST-ORDER INTERTWINING RESIDUAL NONZERO IS A THREE-SLICE INTERVAL WHOSE POSITION DEPENDS ON THE PARITY OF THE CORE. 'WINDOW', 'TRANSPORT', 'HARMONIC' AND 'RESPONSE' NAME PROPERTIES OF EXACT RATIONAL MATRICES: 'window' NAMES the set of slices carrying the nonzero rows of the transport-defect functionals, 'two-step transport' NAMES the linear relation L_2 = K_c W, 'Q-harmonic' NAMES membership in the kernel of Q on the rows where a source vanishes, and 'response' NAMES a derivative of a rational matrix entry. THE WINDOW IS NOT A LIGHT CONE AND NOT A LOCALITY PRINCIPLE: it is a statement about which exact matrices are zero, and NO propagation speed, NO causal structure, NO screening length and NO continuum limit is supplied or implied. THE PARITY-INDEPENDENT WINDOW IS REFUTED, NOT SOFTENED: the adversarial check measured the even cores carrying the SHIFTED window [t0+1, t0+3], so at t0 = 2 the anchors s = 1 and s = 5 carry the OPPOSITE statuses from the solve's rule and the admissible t0+3 cell BREAKS with nnz(R) = 32 where the odd cores exempt it, and PARITY_INDEPENDENT_WINDOW_CLAIMED = False is a declared constant with a gate and a mutation. THE LAW IS NOT PROVED FROM THE STAGGERED RECURRENCE: it is REDUCED to the bilinear identity R[a,b] = -u_b^T dQ G[:, theta_a] together with TWO MEASURED SUPPORT FACTS -- that the union slice support of the eight functionals u_b is EXACTLY the three slices [2 floor(t0/2)+1, 2 floor(t0/2)+3] and that a one-cell tangent at anchor s carries dH rows exactly on the slices {s, s+1} -- and both support facts are MEASURED at two widths and DERIVED FROM NOTHING. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NO GENERALITY IS CLAIMED: ONE fixture, TWO widths, ONE profile family, THREE amplitudes, and NOTHING about the infinite-width or continuum limit. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE EQUIVALENCE IS MEASURED IN BOTH DIRECTIONS AND THE FINITE TABLE IS THE FIRST-ORDER TABLE ENTRY FOR ENTRY. W(delta) = W(0) matrix-exact IF AND ONLY IF R = dL_2 - dK_c W = 0: over the TWENTY valid (bump, core) pairs at T = 16 -- bumps {1,2}, {2,3}, {3,4}, {4,5} against cores t0 = 1, 2, 3, 4, 5 -- nnz(R) is 64 at FOURTEEN pairs, 32 at ONE pair, and EXACTLY ZERO at FIVE; and nnz(W(delta) - W(0)) at delta = 1/5, 1/3 AND 2/5 reproduces that table ENTRY FOR ENTRY in all SIXTY finite rebuilds, so the biconditional holds sixty times over and the zero set is not a linearization artefact. THE ADVERSARIAL CHECK'S SIX REQUESTED CELLS SIT INSIDE IT: ({1,2}, 5), ({2,3}, 5) and ({4,5}, 1) are the exact zero matrix and ({3,4}, 5), ({2,3}, 1) and ({2,3}, 3) are fully dense. BLOCK 192's THREE LANDED CUTOFF PAIRS ARE GATED AS INSTANCES and its twelve-entry odd-core table is reproduced entry for entry as this block's control. THE ONE-CELL TANGENT IS GATED AGAINST BLOCK 192's BUMP TANGENT: summing this block's dH(s,x) over the two anchors of a bump and over all four spatial anchors reproduces Block 192's cell-sum tangent at ZERO residual at all four bumps. THE CARRIER CONTROLS CLOSE AT BOTH WIDTHS: nnz(Q G - I) = nnz(Ps H Ps - H) = nnz(Ps Q Ps - Q^T) = 0 at T = 16 and at T = 20, and the displayed dB is gated entrywise at ZERO against the SYMBOLIC derivative of the IMPORTED shear_hodge with the underlying law gated at BOTH probed volumes, thirty-two numbers. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's exemptions could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate F.\nper_mode: THE DERIVATION IS THREE PILLARS AND A BILINEAR FORM, AND EVERY PILLAR IS GATED AT EXACTLY ZERO. With d_b = e_{(t_b+2, x_b)} - sum_b' W[b',b] e_{(t_b', x_b')} and u_b = G^T d_b: (i) K_c W = L_2 is EXACTLY d_b^T G[:, theta_a] = 0 for the eight unperturbed core columns, so W is DEFINED by the two-step transport relation and not fitted -- nnz(K_c W - L_2) = 0 at EVERY core at BOTH widths, sixteen frames; (ii) the response field rho_a = G dQ G[:, theta_a] satisfies Q rho_a = dQ G[:, theta_a] and is therefore Q-HARMONIC on every row where the source vanishes, and its row support equals the FULL row support of dQ with NO cancellation in all 240 tested columns and ZERO harmonic failures; and (iii) R[a,b] = -d_b^T rho_a, so R = 0 is EXACTLY the statement that the response field obeys the same defect relation as the unperturbed columns -- nnz(response relation + R) = 0 at all THIRTY (anchor, core) pairs. THE BILINEAR FORM FOLLOWS: R[a,b] = -u_b^T dQ G[:, theta_a], so R is LINEAR in the Hodge tangent and the whole law is a statement about the SUPPORT of the eight vectors u_b. THE dW LINK IS EXACT: R = K_c dW at zero residual, so R = 0 if and only if dW = 0, and nnz(dW) = nnz(R) at all FORTY cells. THE MEASURED SOURCE ROWS: the dQ row-support sizes for anchors s = 0..7 at T = 16 are (12, 14, 16, 16, 16, 16, 14, 12) and their positive slice supports are EXACTLY [2 floor(s/2), 2 floor(s/2)+2] at every anchor and at BOTH widths.\nper_block: THE PARITY-RESOLVED WINDOW LAW, AND IT IS THE CHECK'S DISCOVERY CARRIED AS THIS BLOCK'S CENTRE. A reflected one-cell tangent at anchor s BREAKS the intertwining identity at core t0 IF AND ONLY IF s lies in [2 floor(t0/2), 2 floor(t0/2) + 3], equivalently if and only if its support {s, s+1} meets the THREE-SLICE WINDOW [t0, t0+2] for ODD t0 and [t0+1, t0+3] for EVEN t0. THE CORE'S FOOTPRINT IS FOUR SLICES {t0, t0+1, t0+2, t0+3} AND THE WINDOW IS ALWAYS THREE OF THEM, WITH ONE EXEMPT END THAT SWITCHES WITH PARITY: the LAST predicted slice t0+3 is exempt at odd cores and the FIRST read slice t0 is exempt at even cores. MEASURED ON FORTY CELLS AT T = 16 (anchors 0..7 against cores 1..5) AND SEVENTY AT T = 20 (anchors 0..9 against cores 1..7), spatially uniform in all four spatial anchors, with ZERO exceptions. THE BREAK DENSITY IS A FINGERPRINT AND NOT A BINARY: over the four breaking anchors in order the densities are (64, 64, 64, 64) at every odd core and (64, 64, 32, 32) at every even core, at BOTH widths. THE VALIDITY BOUNDARY IS MEASURED AND IS EXACTLY BLOCK 191's TOUCH/CROSS RULE: the cores t0 = 6, 7 at T = 16 and t0 = 8, 9 at T = 20 violate t0+3 <= T/2 and do NOT obey the law, and their functional supports are not three-slice windows. AN EXACT UNEXPECTED-BREAK WITNESS IS RECORDED digit for digit at (t0, s) = (2, 5), entry R[0,4].\nlattice_wide: THE EXEMPTION IS ATTACKED EXHAUSTIVELY AT THE ODD CORES AND REFUTED AT THE EVEN ONES. At the odd cores t0 = 1 and t0 = 3 the t0+3 exemption survives every attack: the admissible reflected one-cell tangent gives nnz(R) = 0 at ALL FOUR spatial anchors; ALL SIXTEEN 4x4 cell-block matrix-unit directions, INCLUDING the eight asymmetric ones, give the exact zero matrix; and every raw matrix unit whose ROW lies on any positive slice from t0+3 through T/2 with an ARBITRARY column anywhere in the 64-dimensional carrier gives the exact zero matrix -- 1280 of 1280 at t0 = 1 and 768 of 768 at t0 = 3. AT THE EVEN CORES THAT SAME EXEMPTION IS FALSE, MEASURED: the admissible t0+3 cell BREAKS with nnz(R) = 32 at t0 = 2 and t0 = 4, eight of the sixteen cell-block directions break, and 256 of 1024 raw directions break at t0 = 2 and 256 of 512 at t0 = 4. WHAT THE EVEN CORES CARRY INSTEAD IS THE DUAL EXEMPTION AT THE LOW END, AND IT IS EXHAUSTIVE THERE: 768 of 768 raw directions give zero at t0 = 2 and 1280 of 1280 at t0 = 4, while the same low-end census BREAKS at the odd cores, 256 of 512 at t0 = 1 and 256 of 1024 at t0 = 3. THE EXEMPT END IS THEREFORE NOT A COINCIDENCE OF THE CELL SOURCE: it is a property of the whole tangent space, and it switches with parity.\nper_scope: THE MECHANISM IS REDUCED TO TWO MEASURED SUPPORT FACTS, AND BLOCK 192's REFUTED OVERLAP SIGNATURE IS REPAIRED. FACT ONE: the union of the slice supports of the eight transport-defect functionals u_b is EXACTLY the three-slice window [2 floor(t0/2)+1, 2 floor(t0/2)+3] at EVERY valid core at BOTH widths, with NO negative-half support at all; and at every even core exactly FOUR of the eight functionals COLLAPSE to a single slice with four nonzero entries, which is the structural origin of the shifted window. FACT TWO: a one-cell tangent at anchor s carries dH rows exactly on the slices {s, s+1}. TOGETHER WITH THE BILINEAR IDENTITY THEY GIVE THE LAW, AND THE RAW-UNIT FORM IS SHARPER STILL: for a raw Hodge tangent E_{p,q} the residual is nonzero IF AND ONLY IF the ROW p lies on one of the three window slices, for EVERY column q -- 20480 units at T = 16 and 44800 at T = 20, 65280 in all, with ZERO mismatches, and exactly 768 breaking units per core at T = 16 and 960 at T = 20. BLOCK 192 LEFT A NAMED OPEN LEG AND ONE MEASURED COUNTEREXAMPLE, AND BOTH ARE SETTLED HERE: its overlap signature compared the dH support against the naive FOUR-slice read window {t0, t0+1, t0+2, t0+3}, which is ONE SLICE TOO WIDE at odd cores; replacing dH by dQ and the naive window by the measured supp(u_b) makes the pair ({4,5}, t0 = 1) an ordinary instance -- the bump's dQ slices are {4, 5, 6} and the window is {1, 2, 3}, disjoint -- and there is NO counterexample left among the twenty pairs. WHAT REMAINS OPEN IS NAMED: the closed forms of the two supports are MEASURED at two widths and are NOT derived from the staggered recurrence.\nRESULT: THE EXACT SET OF ONE-CELL HODGE TANGENTS THAT BREAK THE INTERTWINING IDENTITY IS DETERMINED AT TWO WIDTHS AND IS A THREE-SLICE WINDOW WHOSE EXEMPT END SWITCHES WITH THE PARITY OF THE CORE, THE EQUIVALENCE W(delta) = W(0) IF AND ONLY IF R = 0 IS MEASURED IN BOTH DIRECTIONS OVER SIXTY FINITE REBUILDS, THE HARMONIC-RESPONSE DERIVATION IS GATED IN ALL THREE PILLARS, AND THE MECHANISM IS REDUCED TO A BILINEAR FORM AND TWO MEASURED SUPPORT FACTS -- AND NOT ONE LINE OF IT IS A LIGHT CONE, A LOCALITY PRINCIPLE, A PROPAGATION SPEED, A CONSTRAINT OR A CONTINUUM LIMIT. The parity-independent window the solve proposed is REFUTED and carried as the block's central correction; the odd-core exemption is confirmed against an exhaustive raw-unit attack and its even-core dual is exhibited; Block 192's twelve-entry cutoff table is reproduced as a control and extended to twenty entries; and Block 192's refuted overlap signature is REPAIRED with its single counterexample explained away. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-192 STAND EXACTLY AS LANDED. BLOCK 192 IS NOT CORRECTED: its twelve-entry cutoff table is reproduced here entry for entry as this block's control, its three cutoff pairs are gated as instances of the window law, and its NAMED OPEN LEG is closed by reduction rather than by revision. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE fixture, TWO widths, ONE profile family and THREE amplitudes -- two widths are not a scan; the closed forms of the two supports are MEASURED and not derived from the recurrence; and the law's domain is bounded by a validity rule that is itself measured rather than proved. SEVEN ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the P2 REFUTATION, that the window is NOT parity-independent and the even cores carry [t0+1, t0+3]; the C2 CONFIRMATION of the odd-core incidence, extended here from eighteen cells to forty; the C3 SURVIVAL of the t0+3 exemption against an exhaustive raw-unit attack, extended here to all sixteen cell-block directions and to the even-core dual; the C1 EQUIVALENCE on the six requested cells, extended here to twenty pairs and sixty finite rebuilds; the C4 DERIVATION pillars, all three reproduced independently; the P1 WIDTH check at T = 20, extended here from nine cells to seventy; and the P3 ALL-AMPLITUDE check at three exact rationals, extended here to every bump and every core. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE CUTOFF MECHANISM DERIVATION (block 193 candidate), CUT PHASE A MEASURED, CUT PHASE B MEASURED, CUT PHASE B3 MEASURED, CUT PHASE C MEASURED and B193 CHECK VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **A proof of the two support facts from the staggered recurrence.** Stopped
   **as an open leg, not as a refutation**: the facts hold at two widths and
   every valid core, and no derivation of them is offered.
2. **Any statement about `T/2` odd.** Stopped: both widths here have `T/2` even
   (`8` and `10`), and the `floor(t0/2)` structure is measured only there.
3. **Any second-order or full-`delta` expansion.** Stopped: this block computes
   a **first** derivative and three finite amplitudes. Second-order coefficients
   are not computed and are not claimed to vanish anywhere.
4. **Any rank or invariant-subspace reading of the half-density `32`.**
   Stopped: it is a count of nonzero entries and nothing else is computed.
5. **Any locality, light-cone, propagation or continuum reading.** Stopped at
   `N0` and fenced at `N4g`.

### REOPEN IF

1. **A width with `T/2` odd is run.** The whole law is stated through
   `floor(t0/2)`, and `T/2` odd is the cheapest test that could break it.
2. **A second fixture is run.** Every residual here carries `(9/20, 5/13)` in
   it. Whether the *supports* are fixture-independent is a sharp, cheap question
   and is not answered here.
3. **`supp(u_b)` is derived.** The object to explain is precise: why
   `G^T d_b` — a full column combination of a dense `64 x 64` inverse — vanishes
   off three consecutive slices, and why four of the eight collapse to one slice
   at even cores.
4. **The half-density `32` is explained.** The even cores break at exactly half
   the entry count on their two upper anchors, at every amplitude and at both
   widths. Nothing here says why.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 192's #41. NO CORRECTION IS LANDED BY THIS
BLOCK AGAINST ANY LANDED NUMBER.** Seven of the adversarial check's findings are
carried as **content** rather than as errata; three further items correct or
extend this block's own solve language; and every one of the ten is a declared
constant with a gate and, where it guards a correction, a mutation.

42. **THE P2 REFUTATION — THE WINDOW IS NOT PARITY-INDEPENDENT.** The solve
    claimed the single window `[t0, t0+2]` at every core on the strength of an
    eighteen-cell odd-core census. Measured independently here: at `t0 = 2` the
    anchors `s = 1` and `s = 5` carry the **opposite** statuses from that rule,
    and at `t0 = 4` so do `s = 3` and `s = 7`. The even cores carry
    `[t0+1, t0+3]`. **The rule is refuted and replaced, and the replacement is
    this block's central law.** `PARITY_INDEPENDENT_WINDOW_CLAIMED = False`,
    gates `B-4`/`E-1`/`E-3`, mutation `claim_parity_independent`.
43. **AND THE EXEMPT END SWITCHES RATHER THAN THE WINDOW MOVING.** The core's
    footprint is four slices and the window is always **three** of them. What
    parity changes is **which end is exempt**: the last predicted slice `t0+3`
    at odd cores, the first read slice `t0` at even ones. Gate `E-3`, mutation
    `break_parity_switch`.
44. **THE UNIFIED FORM, WHICH MAKES THE SWITCH A CONSEQUENCE AND NOT A SECOND
    HYPOTHESIS.** `W(t0) = [2⌊t0/2⌋+1, 2⌊t0/2⌋+3]`. Cores `t0 = 2j` and
    `t0 = 2j+1` share **the same** window and the **same** break set — the law
    depends on `t0` only through `⌊t0/2⌋`, and the parity statement is that one
    formula read two ways. Gates `E-1`, `E-3`, `E-7`.
45. **THE C3 EXEMPTION IS CONFIRMED, EXTENDED AND GIVEN A DUAL.** The check
    attacked the odd-core `t0+3` exemption with ten symmetric cell-block
    directions and `1280`/`768` raw units; this block runs **all sixteen**
    cell-block directions including the asymmetric ones and reproduces the raw
    censuses exactly, then measures the **even-core** versions, which **break**
    (`256/1024` and `256/512`), and the **dual low-end** exemption, which is
    exhaustive at the even cores (`0/768`, `0/1280`) and fails at the odd ones.
    Gates `E-5`, `E-6`, mutations `break_odd_exemption`, `break_even_refutation`.
46. **THE MECHANISM IS REDUCED, NOT ASSERTED, AND BLOCK 192's OPEN LEG IS
    CLOSED BY REDUCTION.** `R[a,b] = -u_b^T dQ G[:, theta_a]` is exact and makes
    `R` linear in the tangent; the law is then two support facts. Block 192
    named "empty-cross routing" a reading and an open leg; this block replaces
    it with a measured statement and names precisely what remains open — the
    closed forms of the two supports. Gates `D-6`, `E-7`, `E-8`, `B-7`,
    mutations `break_unit_closed_form`, `break_support_facts`,
    `break_raw_unit_law`, `claim_law_proved`.
47. **AND BLOCK 192's REFUTED OVERLAP SIGNATURE IS REPAIRED, NOT REPEATED.**
    Its `({4,5}, t0=1)` counterexample came from comparing `dH` support against
    the naive four-slice read window. Using `dQ`'s support and the measured
    three-slice `supp(u_b)`, that pair is an ordinary instance —
    `{4,5,6} ∩ {1,2,3} = ∅` — and **no counterexample remains among the twenty
    pairs.** Gate `E-8`, correction folded as content; Block 192's own numbers
    are untouched.
48. **THE SOLVE'S EIGHTEEN CELLS ARE EXTENDED TO FORTY AND SEVENTY, AND THE
    MISSING ANCHORS ARE THE ONES THAT MATTERED.** `s = 0` and `s = T/2-1` are
    admissible anchors and were absent from the solve's census; both obey the
    law, and without them the break set looks like three cells at `t0 = 1` and
    four elsewhere, which is what hid the `⌊t0/2⌋` structure. Gates `E-1`,
    `E-2`, mutations `break_window_sixteen`, `break_window_twenty`.
49. **THE LAW'S DOMAIN IS EXACTLY BLOCK 191's TOUCH/CROSS RULE, AND IT IS
    MEASURED RATHER THAN INHERITED.** `t0 = 6, 7` at `T = 16` and `t0 = 8, 9` at
    `T = 20` violate `t0+3 <= T/2`; they were run anyway, they do **not** obey
    the law, and their functionals are nearly dense. Gate `E-9`, mutation
    `break_validity_boundary`.
50. **THE BREAK DENSITY IS A FINGERPRINT, NOT A BINARY, AND IT IS NEW.**
    `(64,64,64,64)` at odd cores and `(64,64,32,32)` at even ones, at both
    widths, at first order **and** at all three finite amplitudes. Neither the
    solve nor the check recorded it. Gate `E-4`, mutation
    `break_break_density`.
51. **AND THE EQUIVALENCE IS STRENGTHENED FROM A ZERO-SET STATEMENT TO AN
    ENTRYWISE ONE.** The check verified `nnz(R) = 0 <=> nnz(W(delta)-W(0)) = 0`
    on six cells at two amplitudes. Measured here on twenty pairs at three
    amplitudes, the two tables agree **entry for entry**, not merely in their
    zero sets — sixty of sixty. Gates `C-5`, `C-6`, mutations
    `break_finite_table`, `break_equivalence`.

### The adversarial check

Verdict carried as **CORE CONFIRMED, PARITY EXTENSION REFUTED — AND THE
REFUTATION FOLDED AS THE LAW** (`sol xhigh`, cross-model, an independent compact
rebuild from the landed Block 190 and Block 191 notes rather than an invocation
of either runner; findings preserved at `b193_check_findings.md`, checker at
`b193_exact_check.py`).

**CONFIRMED EXACTLY, ON AN INDEPENDENT RECONSTRUCTION.** `C1`'s identity ⟺
invariance equivalence on all six requested cells at both amplitudes; `C2`'s
eighteen-cell odd-core incidence table, `18/18`; `C3`'s survival of the `t0+3`
exemption under exhaustive attack; all three `C4` derivation pillars; `P1`'s
nine-cell `T = 20` spot check; and `P3`'s three exact amplitudes.

**REFUTED AS WORDED, NOW THE BLOCK'S CENTRE RATHER THAN PROSE:** `P2`'s
parity-independent window (correction 42, replaced by 43 and 44).

**THE CHECK'S EXACT WITNESS IS REPRODUCED DIGIT FOR DIGIT.** The
`(t0, s) = (2, 5)` entry `R[0,4]` of `N3` is the checker's recorded rational,
numerator and denominator, and it is a **declared literal** in this block's
runner rather than a printed byproduct.

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–192 number **stands as landed**.
Block 192's twelve-entry cutoff table is reproduced here entry for entry as this
block's control, its three cutoff pairs are gated as **instances** of the window
law, and its named open leg is **closed by reduction rather than by revision**.
Block 188's landed `T = 8` object is untouched and the wrap-edge family remains
a **disclosed variant** of it.

### Reproduction

```
python3 scripts/admissibility_dirac_kahler_parity_window_intertwining_law_2026_08_25.py
python3 ... --list-mutations
python3 ... --mutation break_even_refutation
```

Exact throughout: sympy `Rational`/`Integer` only, `DomainMatrix` over `QQ` for
the exact inverses — **one `64 x 64` and one `80 x 80` at `delta = 0`, each
built once and shared by every core, every anchor and every census in the
block**, plus twelve more `64 x 64` at the finite amplitudes (four bumps by
three exact amplitudes) and the small `8 x 8` Gram inverses, one per core frame
and one per finite rebuild — and **no float, no tolerance, no `evalf` and no
`sp.nsimplify` anywhere**, the last of which is *measured* in the runner's own
source by gate `F-3` rather than promised. This block has **no numeric layer at
all**: every quantity it reports is an exact rational or a count of nonzero
exact entries.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE CUTOFF MECHANISM
DERIVATION (block 193 candidate)**, **CUT PHASE A MEASURED**, **CUT PHASE B
MEASURED — THE MECHANISM IDENTIFIED**, **CUT PHASE B3 MEASURED — THE EDGE
ASYMMETRY**, **CUT PHASE C MEASURED — THE WINDOW LAW** and **B193 CHECK
VERDICT** anchors.
