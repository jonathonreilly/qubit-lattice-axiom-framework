---
title: "Admissibility — Dirac-Kähler Hybridization Mechanism And The Support-Cutoff Law"
date: 2026-08-25
block: 192
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_hybridization_mechanism_support_cutoff_2026_08_25.py
parent_ref: origin/physics-loop/toe-axiom-closure-block191-boundary-mode-volume-sensitivity-20260825
parent_commit: 36f54ab2ad6e51cbe2bf6b8b604b63236f2c936e
current_main: b11811704efa98a12272d572f666e530a807f6c1
registered: 0
adopted: 0
axiom_movement: none
---

# The First-Order Hybridization Mechanism In Closed Form, And The Exact Support-Cutoff Law — with PERTURBATION, LOCKING and CUTOFF fenced as names for matrix properties throughout

**One sentence.** On Block 190's wrap-edge width family at the same fixture
`(m, c) = (9/20, 5/13)` and the same width `T = 16`, Block 191's localized
Hodge-volume bump `v = 1 - delta` is **differentiated**: the response of the
unit-cell monodromy `W = K_c^-1 L_2` is obtained in **closed form** by a
four-step chain of displayed identities that never inverts a symbolic matrix,
its ten per-factor first-order trace responses are exact rationals obeying four
exact sum rules, and the response **vanishes exactly** at three of the twelve
probed `(bump, core)` pairs — at first order *and* at two finite amplitudes —
in a pattern that is **directional and not radial**; and **not one line of this
supplies a lapse, a perturbation of a physical system, a light cone or a
continuum limit**.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Six imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE PERTURBATION LANGUAGE IS FENCED BEFORE THE FIRST NUMBER IS READ.**

- **NO GRAVITY IS SUPPLIED AND NO PHYSICAL PERTURBATION IS PERFORMED.** `delta`
  is a dial on the **imposed Hodge-volume parameter** of Block 105's
  `shear_hodge(c, v)`, and the word **response** names `d/d(delta)` of a
  rational matrix entry at `delta = 0`. This block supplies **no lapse variable
  in an ADM phase space, no Hamiltonian constraint, no gauge orbit, no
  quotient, no Dirac observable and no OS reconstruction** that would make `W` a
  physical transfer operator.
- **"HYBRIDIZATION", "LOCKING" AND "SUPPORT CUTOFF" NAME PROPERTIES OF EXACT
  RATIONAL MATRICES.** *Hybridization* names the joint sign behaviour of two CRT
  trace components of one `8 x 8` rational matrix. *Locking* names **that joint
  sign behaviour and no magnitude agreement whatever**. *Support cutoff* names
  **entrywise equality of two exact `8 x 8` matrices**. None of the three names
  a mode, a coupling, a screening length or a physical mechanism.
- **THE SOLVE'S RELATIVE-AGREEMENT QUANTIFIER IS DROPPED, NOT SOFTENED AND NOT
  RENORMALIZED.** The adversarial check measured the `{2,3}` heavy/boundary
  relative difference **above** the quoted rational threshold `1/100` under the
  heavy-reference, boundary-reference **and** symmetric normalizations. This
  block therefore claims **the sign structure only**, records the two exact
  differences and six exact relative readings in the quantifier's place, and
  carries `THRESHOLD_HOLDS_AT_BOTH_POSITIONS = False` as a declared constant
  with a gate and a mutation. See correction 33.
- **THE SUPPORT CUTOFF IS NOT A LIGHT CONE.** It is a statement about which
  exact matrices are equal. **No propagation speed, no causal structure, no
  screening length and no continuum limit** is supplied or implied, and the
  pattern is not even monotone in distance (`N4`).
- **AND THE MECHANISM OF THE CUTOFF IS NOT DERIVED.** "Empty-cross routing" is a
  **reading** (`R4`) and a **named open leg**. Its naive form is **refuted here
  by measurement**: `dG` is dense at `3968` of `4096` entries at every cutoff
  pair, `dK_c` is full, and one measured pair overlaps the read window and still
  gives `0_8`.

**TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED**, so the absence is a
count and not a mood: lapse function; shift vector; ADM phase space;
Hamiltonian constraint; momentum/diffeomorphism constraint; first-class
constraint algebra; Dirac closure; Dirac observable; gauge orbit and its
quotient; Osterwalder–Schrader reconstruction of a transfer operator.

**NO GENERALITY IS CLAIMED.** One fixture `(9/20, 5/13)`, one width `T = 16`,
four bump positions, three probe cores, three amplitudes `delta = 1/5, 1/7,
1/100` with the halving `1/200`. **Four positions are not a scan and three
cores are not a scan.**

**THE OBJECT IS STILL A DISCLOSED VARIANT.** The carrier is Block 190's
wrap-edge family (`w = -1` at `t = T-1`), which is **not** Block 188's landed
`T = 8` object (`w = -1` at `t = 3`). Blocks 188, 189, 190 and 191 are neither
corrected nor contradicted by anything below.

---

## W1 — the wall, and the charter

### What was open

Block 191 measured Block 105's Hodge volume `v` **at points**: uniform `v = 1`,
uniform `v = 4/5`, and two localized bumps at amplitude `4/5`. It reported the
near-edge response as a *hybridization* of the boundary and bulk-heavy factors
and left three things explicitly open in its own `N6`:

1. **The response was measured, never derived.** Every number came from
   rebuilding `W` at a second volume and differencing. No formula gave the
   response as a function of the bump.
2. **Its `{2,3}` zero at `t0 = 5` was unexplained.** Block 191 recorded
   `nnz(W_bump - W_{v=1}) = 0` at that one probe and named it "out of range".
   Whether it was a root coincidence, a resultant vanishing, or something
   stronger was not decided.
3. **The reach was described as position-dependent but never tabulated.** Two
   bump positions against three cores is not a table.

### The charter

1. **Derive the response**, as a chain of displayed identities in which **no
   symbolic matrix is ever inverted**, and gate every link at exactly zero.
2. **Split the response by spectral factor**, exactly, with CRT projectors whose
   defining congruences are checked rather than assumed.
3. **Tabulate the reach** over every valid `(bump, core)` pair, at first order
   **and** at finite amplitude, and say exactly which pairs are zero.
4. **Carry the adversarial check's refutation as content**, and keep the claimed
   statement narrower than the tempting one at every step.

---

## N1 — THE METHOD THEOREM, and it is a chain of four displayed identities

**NOTHING BELOW IS ABOUT THE LANDED CHAIN'S OBJECT IF THIS SECTION IS NOT
EXACT.**

### The one import, differentiated

Block 105's landed law, read through the Block 128 module, is

```text
shear_hodge(c, v) = diag(v, v g(c)^-1, 1/v),   g(c) = [[1, c], [c, 1]].
```

At `c = 5/13` its two probed values are gated **entrywise** against the import —
thirty-two numbers, zero residual:

```text
shear_hodge(5/13, 1)   = [[1,       0,        0,       0],
                          [0,   169/144,  -65/144,     0],
                          [0,   -65/144,  169/144,     0],
                          [0,       0,        0,       1]],
shear_hodge(5/13, 4/5) = [[4/5,     0,        0,       0],
                          [0,   169/180,   -13/36,     0],
                          [0,    -13/36,  169/180,     0],
                          [0,       0,        0,     5/4]].
```

This block needs the **derivative** rather than a second value, so the import is
read at a **symbolic** volume `v = 1 - delta` and differentiated entrywise:

```text
dB := d/d(delta) shear_hodge(c, 1 - delta) |_{delta = 0}
    = -E00 - (169/144)(E11 + E22) + (65/144)(E12 + E21) + E33
    = [[-1,        0,         0,    0],
       [ 0,  -169/144,   65/144,    0],
       [ 0,    65/144, -169/144,    0],
       [ 0,        0,         0,    1]].
```

**The two scalar corners move in OPPOSITE directions**: `dB[0,0] = -1` and
`dB[3,3] = +1`, because the law carries `v` in one corner and `1/v` in the
other. Gate `C-1` compares this displayed matrix to the symbolic derivative of
the import at **zero residual**; nothing here is a hand-differentiation of a
transcribed formula.

### The chain, stated once

`H` is a **quarter-weighted four-corner cell sum**, so its derivative is *the
same cell sum over the bumped times alone*. For a bump on the positive anchors
`A`, the bumped times are `A` together with the image anchors whose
`thA_s(t) = -1-t` partner lies in `A`, and the image blocks carry
`P_4 dB P_4^T`:

```text
(1)  dH = (1/4) sum_{t in A}          sum_x  E(t,x) dB          E(t,x)^T
        + (1/4) sum_{t : thA_s(t) in A} sum_x  E(t,x) P_4 dB P_4^T E(t,x)^T,
(2)  dQ = m dH + dH D_s - D_s^T dH            [D_s does not depend on delta],
(3)  dG = -G dQ G                             [G = Q^-1 at v = 1, KNOWN],
(4)  dW = K_c^-1 (dL_2 - dK_c W)              [dK_c, dL_2 = restrictions of dG].
```

**NO SYMBOLIC MATRIX IS EVER INVERTED.** Step `(3)` uses the *already computed*
`64 x 64` rational inverse at `v = 1`, and step `(4)` uses the *already
computed* `8 x 8` core Gram inverse. That is the whole of the method.

### Every link is gated at exactly zero

| identity | residual | gate |
| --- | ---: | --- |
| `nnz(dH_symbolic - dH_cellsum)` at each bump | `0` | `C-4` |
| `nnz(dQ_symbolic - dQ_law)` at each bump | `0` | `C-4` |
| `nnz(Q dG + dQ G)` at each bump | `0` | `C-5` |
| `nnz(dG Q + G dQ)` at each bump | `0` | `C-5` |
| `nnz(dK_c W + K_c dW - dL_2)` at all twelve pairs | `0` | `C-6` |
| `nnz(Ps H Ps - H)`, `nnz(Ps Q Ps - Q^T)` at the baseline | `0`, `0` | `C-3` |

The symbolic route in row one is **not** the chain re-run: the displayed profile
is built with `delta` a sympy symbol and differentiated **entrywise before any
inverse is formed**, and only then compared to the cell-sum route. Rows three
and four are **both** resolvent equations, left and right, so `dG` is pinned as
a two-sided derivative and not merely as a left one.

### The fingerprints

```text
nnz(dH) = 56  at every one of the four bumps,
nnz(dQ) = 200 at the ODD-anchor bumps {1,2} and {3,4},
        = 152 at the EVEN-anchor bumps {2,3} and {4,5},
nnz(dG) = 3968 of 4096  at every one of the four bumps.
```

The `dQ` count depends only on the **parity of the leading anchor**, which is the
staggered sign `eta_x = (-1)^t` showing up in the derivative. **`dG` is dense**,
and that single number is what refutes the routing account in `N4b`.

---

## N1a — THE INDEPENDENT ROUTE, because a chain that gates only against itself proves nothing

The chain above is algebra. It is checked against a route that shares **no step
with it**: `W` is rebuilt from scratch at two exact rational amplitudes, forward
differences are formed over `QQ`, and the exact first linear elimination is
applied.

```text
D(h) = (W(h) - W(0)) / h,     R = 2 D(h/2) - D(h),     h = 1/100.
```

At each of the four response pairs, and **entrywise in all sixty-four entries**:

```text
|R_ij - dW_ij|  <=  |D(h/2)_ij - dW_ij|  <=  |D(h)_ij - dW_ij|,
max_ij |R_ij - dW_ij|  <  1/10000  <  max_ij |D(h/2)_ij - dW_ij|,
max_ij |dW_ij|  >  1/4.
```

Every one of those is an **exact rational comparison** — no float, no tolerance.
The elimination lands within `1/10000` of the propagated derivative while the
operator's own scale exceeds `1/4`, so the two routes agree to better than one
part in `2500` of the object being measured, and the agreement **improves
monotonically** as the step halves.

**AND AT THE THREE CUTOFF PAIRS THE FINITE-DIFFERENCE ROUTE IS EXACT, NOT
MERELY CONVERGENT.** Where `W(delta) = W(0)` identically, `(W(delta) - W(0))/delta`
**equals** `dW` entrywise at `delta = 1/5` *and* at `delta = 1/7`, at zero
residual. The independent route reproduces the zeros of `N4` exactly rather than
approximately. Gate `C-8`.

---

## N2 — THE TEN RATIONALS, and the projectors are congruence-gated

### The baseline control

Block 191's landed factorization is reproduced here digit-for-digit as this
block's control, with

```text
heavy    = 22569375 z^2 - 233631106 z + 22569375,
light    = 39529825 z^2 - 109432706 z + 39529825,
boundary = 43033320714375 z^2 - 445467467014578 z + 48554286398375,
```

and

```text
charpoly(W) = heavy * light^2 * boundary   at t0 = 1,
charpoly(W) = heavy^2 * light^2            at t0 = 3.
```

Gate `D-1`. **The word "boundary" names this rational factor and nothing
physical.**

### The projectors, built and then certified

For each labelled factor `f` of multiplicity `k` in `chi = charpoly(W)`,

```text
M_f = chi / f^k,     q_f = M_f * (M_f^-1 mod f^k)  mod chi,     P_f = q_f(W).
```

Nothing here is assumed. **Every** congruence is checked as a **zero polynomial
residual over `QQ`**:

```text
q_f - 1 = 0  mod f^k,      q_f = 0  mod g^l  for every other factor g,
nnz( sum_f P_f - I_8 ) = 0,      nnz( (prod_f f)(W) ) = 0.
```

Gate `D-6`.

### The ten values

At `t0 = 1` the spectrum carries three labelled factors and at `t0 = 3` it
carries two, so the two response bumps give exactly **ten** per-factor
first-order trace responses `tr(P_f dW)`. **All ten are nonzero.**

| bump | core | factor | exact `tr(P_f dW)` | `x 10^10` |
| --- | ---: | --- | ---: | ---: |
| `{3,4}` | `1` | heavy | `840153195543/196300900625` | `42799253232` |
| `{3,4}` | `1` | boundary | `59790687128721117/13862573301236875` | `43131016031` |
| `{3,4}` | `1` | light | `21615004253318/12284407006475` | `17595480386` |
| `{2,3}` | `1` | heavy | `-421462341183472199/177215545561734375` | `-23782470090` |
| `{2,3}` | `1` | boundary | `-29381217534120895221181/12514784612024119828125` | `-23477205917` |
| `{2,3}` | `1` | light | `22866757183474123654/19424018367789224675` | `11772413283` |
| `{3,4}` | `3` | heavy | `-152770523741944777898/10738971376744546875` | `-142258060276` |
| `{3,4}` | `3` | light | `-6227354334614993838/3884803673557844935` | `-16030036156` |
| `{2,3}` | `3` | heavy | `-1495288291042/1427461510575` | `-10475156633` |
| `{2,3}` | `3` | light | `-2705696606558/2456881401295` | `-11012727782` |

**The exact rationals are primary. The decimals are this block's one numeric
layer** — `evalf` of exact rationals at 40 digits, gated to ten places, and
never fed back into a construction. Gates `D-2`, `D-3`, `E-7`.

### The four sum rules

```text
tr(dW) = sum_f tr(P_f dW),  at exact equality, at all four (bump, core) pairs:

{3,4}, t0=1:  2702603990428664601847792/261056210615088396173125
{2,3}, t0=1:  -1322424657623802056150231913430788608
              /372647692749599431888443061718296875
{3,4}, t0=3:  -83526662690302770407422046496832
              /5276875808912607540299962640625
{2,3}, t0=3:  -953207325986164736/443602221410818725
```

Gates `D-4`, `D-5`.

### And the check's P1 is folded, and strengthened

The adversarial check asked whether replacing the full multiplicities `f^k` by
the **squarefree** total `prod_f f` changes the trace responses. It does not —
and the reason is stronger than trace agreement:

```text
P_f(full multiplicities) - P_f(squarefree total) = 0_8,  entry for entry,
for every factor at both cores.
```

The two constructions produce **the same matrix**, not merely the same trace.
Gate `D-7`. This is carried as content, credited to the check (correction 40).

---

## N3 — THE RESPONSE TABLE, and the solve's quantifier is dropped

### What is claimed: the sign structure and two exact differences

At the near-edge core `t0 = 1`:

```text
bump {3,4}:  heavy > 0,  boundary > 0,  light > 0,
bump {2,3}:  heavy < 0,  boundary < 0,  light > 0.
```

**The heavy and boundary responses share a sign at each position and flip
together between them; the light response does not flip.** That is the whole of
the claim, and it is gated at `E-3` and `E-4`.

Their exact differences are **nonzero**, so the two factors do **not** respond
identically:

```text
|heavy - boundary|  =  61132656/1842661567   at bump {3,4},
                    =  56249856/1842661567   at bump {2,3},
```

and — a fact the solve never noticed — **both differences carry the same
denominator `1842661567`**. Gates `E-1`, `E-2`.

### What is NOT claimed, and why

The solve asserted that the heavy and boundary responses agree to within the
rational threshold `1/100` **at both bump positions**. The adversarial check
measured otherwise, and this block measures the same thing independently. The
six exact relative readings, as integers over `10^10`:

Writing `d` for the exact difference and `h`, `b` for the two responses, the
three standard normalizations are `d/abs(h)`, `d/abs(b)` and the symmetric
`2d/(abs(h) + abs(b))`:

| bump | heavy reference | boundary reference | symmetric |
| --- | ---: | ---: | ---: |
| `{3,4}` | `77516025` | `76919774` | `77216748` |
| `{2,3}` | `128356799` | `130025768` | `129185893` |

Against the threshold `1/100 = 100000000` in the same units: `{3,4}` is **below
it under all three normalizations** and `{2,3}` is **above it under all three**.

```text
THRESHOLD_BY_POSITION            = { {3,4}: True,  {2,3}: False }
THRESHOLD_HOLDS_AT_BOTH_POSITIONS = False
```

**THE QUANTIFIER IS THEREFORE DROPPED AND NOT RENORMALIZED.** No normalization
is hunted for under which the statement becomes true; the exact ratios are
displayed and the claim is reduced to the sign structure. `break_relative_readings`
and `claim_locking_threshold` make the correction a **gate and not a sentence**.
Corrections 33 and 34.

### At `t0 = 3` the position dependence is a ratio, not an adjective

```text
tr(P_heavy dW) / tr(P_light dW)  at t0 = 3:

ON-SITE      bump {3,4}:  37533905844768035289054578457791
                          /4229425500383349914656444790625,   8 < r < 9,
DISTANCE-ONE bump {2,3}:  232340137594542523/244263525398539845,
                                                             9/10 < r < 1.
```

The on-site bump is **heavy-dominated** and the distance-one bump is
**scale-balanced**, and both statements are exact rational **inequalities** and
not roundings. The solve's "`9:1`" is a rounding of `8.8744690837` and is
recorded as such (correction 41). Gates `E-5`, `E-6`.

---

## N4 — THE SUPPORT-CUTOFF LAW, and it is this block's centre

**THIS IS THE ADVERSARIAL CHECK'S DISCOVERY, CARRIED AS CONTENT AND CREDITED.**

### The table, over every valid pair

The four bump positions all lie in the positive-anchor domain `{0..7}`, and the
three cores all satisfy Block 191's touch/cross rule `t0 + 3 <= T/2 = 8`. That
is twelve valid `(bump, core)` pairs, and `nnz(dW)` at each is:

| `nnz(dW)` | `t0 = 1` | `t0 = 3` | `t0 = 5` |
| --- | ---: | ---: | ---: |
| bump `{1,2}` | `64` | `64` | **`0`** |
| bump `{2,3}` | `64` | `64` | **`0`** |
| bump `{3,4}` | `64` | `64` | `64` |
| bump `{4,5}` | **`0`** | `64` | `64` |

**Nine pairs full, three pairs exactly zero.** Gate `F-1`.

### The same table at finite amplitude

`nnz(W(delta) - W(0))` at `delta = 1/5` is **the same twelve-entry table**, and
the three zeros are reproduced again at `delta = 1/7`:

```text
first order  ==  delta = 1/5  ==  the table above,   entry for entry,
delta = 1/7  reproduces all three zeros.
```

So the cutoff is **not a linearization artefact**: at the three pairs the whole
`8 x 8` monodromy is unchanged **entrywise** at a finite bump of amplitude
one-fifth. Gates `F-2`, `F-3`, `F-4`, `F-5`.

### It is DIRECTIONAL, not radial

```text
bump {3,4} REACHES t0 = 5;   bump {2,3} does NOT.
bump {4,5} MISSES  t0 = 1;   bump {3,4} reaches it.
```

**"The response decays with distance" is FALSE as a description of this table.**
A bump nearer the core in one direction can be invisible while a bump farther
away in the other is not. This withdraws the solve's global-decay reading
(correction 38).

### The extra position is a CUTOFF, not a persistence

Bump `{4,5}` at `t0 = 1` is a **valid** probe: `{4,5}` lies in `{0..7}` and
`t0 + 3 = 4 < 8` is interior. Its exact first-order triple is

```text
( tr(P_heavy dW), tr(P_boundary dW), tr(P_light dW) )  =  (0, 0, 0),
tr(dW) = 0.
```

That is a **trivial equality** and **not** the survival of a nonzero response at
a third position. Recording it as "the locking persists" would be false.
Correction 36, gate `F-6`.

### And Block 191's zero is hereby identified

Block 191 recorded `nnz(W_bump - W_{v=1}) = 0` for bump `{2,3}` at `t0 = 5` and
named it "out of range". It is **whole-operator invariance**, not a root
coincidence and not a vanishing resultant:

```text
W_{bump {2,3}, delta = 1/5}(t0 = 5)  -  W_0(t0 = 5)  =  0_8   entrywise.
```

Correction 35.

---

## N4b — THE MECHANISM, measured; and the routing account, refuted

### What is exact

At every cutoff pair the underlying pairings are **not** individually fixed. At
`delta = 1/5`:

| pair | `nnz(K_c(delta) - K_c)` | `nnz(L_2(delta) - L_2)` |
| --- | ---: | ---: |
| `({1,2}, t0=5)` | `64` | `60` |
| `({2,3}, t0=5)` | `64` | `60` |
| `({4,5}, t0=1)` | `64` | `64` |

**Both pairings move in sixty to sixty-four of their sixty-four entries.** What
is exact is that they move **together**:

```text
first order:   dL_2 = dK_c W                          at zero residual,
finite delta:  L_2(delta) = M L_2  with  M = K_c(delta) K_c^-1,
               at zero residual, and nnz(M - I_8) = 64.
```

`W = K_c^-1 L_2` is invariant under **exactly** that motion — a common **left
factor** on the pairing pair — and that is the entire cancellation. Gate `F-7`.
Note precisely what this is: it is the **form** of the cancellation, and it is
informative because of the table above. The content is that `K_c` and `L_2` each
move in almost every entry while their quotient does not move at all.

### What is refuted

The solve's narrative account was that the empty-cross block structure of `Q`
**routes `G dQ G` away** from far cores. In its naive support form that account
is **false here, measured**:

```text
nnz(dG)   = 3968 of 4096   at EVERY bump, including all three cutoff pairs,
nnz(dK_c) = 64             at each cutoff pair (first order),
nnz(dL_2) = 60, 60, 64     at ({1,2},5), ({2,3},5), ({4,5},1) (first order).
```

**Nothing is routed away.** The derivative of the resolvent is dense, both
restrictions are full, and the zero appears only after the quotient is formed.
`SUPPORT_ROUTING_IS_THE_MECHANISM = False`, gate `F-8`, correction 39.

### And the support-overlap signature is sufficient but NOT necessary

Define the bump's **measured** site-time support (read off `dH`, never asserted)
and the core's read window (the column times `{t0, t0+1, t0+2, t0+3}` and the
`theta_s` row times):

```text
support({1,2}) = {1,2,3,13,14,15}      window(t0=1) = {1,2,3,4,14,15}
support({2,3}) = {2,3,4,12,13,14}      window(t0=3) = {3,4,5,6,12,13}
support({3,4}) = {3,4,5,11,12,13}      window(t0=5) = {5,6,7,8,10,11}
support({4,5}) = {4,5,6,10,11,12}
```

Then, **measured over all twelve pairs**:

- **Emptiness forces the zero**, in `2` of `2` cases: `({1,2}, 5)` and
  `({2,3}, 5)` have empty overlap and both give `0_8`.
- **Non-emptiness does NOT force a nonzero response.** `({4,5}, t0 = 1)`
  overlaps the window at `t = 4` and still gives `0_8` — **exactly one
  counterexample among the ten overlapping pairs.**

```text
OVERLAP_EMPTY_IMPLIES_ZERO   = True   (2 of 2)
OVERLAP_IS_A_CUTOFF_SIGNATURE = False (1 counterexample of 10)
```

**NO SUPPORT SIGNATURE DEFINES THE CUTOFF**, and the derivation of its mechanism
is **open**. Gate `F-9`, reading `R4`, correction 39.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

| word | what it names in this block | what it does NOT name |
| --- | --- | --- |
| *response* | `d/d(delta)` of a rational matrix entry at `delta = 0` | any physical perturbation of any system |
| *hybridization* | the joint sign behaviour of two CRT trace components | a mixing of physical modes |
| *locking* | that joint sign behaviour, and **no** magnitude agreement | any bound on how close two numbers are |
| *support cutoff* | entrywise equality of two exact `8 x 8` rational matrices | a light cone, a causal horizon, a screening length |
| *boundary* | an exact rational factor of `charpoly(W)` at a seam-adjacent core | an edge excitation of a physical surface |
| *on-site*, *distance-one* | index arithmetic on `{0..7}` | a metric distance in any geometry |

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within one imposed finite matrix construction at one fixture and one width,
> the first derivative of an exact rational `8 x 8` matrix with respect to a
> one-slice dial on an imposed Hodge-volume parameter is computed in closed form
> without inverting a symbolic matrix; its ten CRT trace components at two dial
> positions and two cores are exact nonzero rationals obeying four exact sum
> rules; and the derivative is the exact zero matrix at three of twelve probed
> `(dial position, core)` pairs, at first order and at two finite dial values.

### Three further fences, all three self-imposed

1. **The pairing-gauge identity of `N4b` is a restatement, not an explanation.**
   That `L_2(delta) = M L_2` with `M = K_c(delta) K_c^-1` is *equivalent* to
   `W(delta) = W(0)`. It earns its place only because the table beside it shows
   both pairings moving in almost every entry — the equivalence is what rules
   out "nothing moved", and it is not a derivation of why.
2. **Twelve pairs is not a law about all pairs.** Cores `t0 = 0, 2, 4` are not
   probed, `T = 20` is not probed, and no second fixture exists.
3. **The `1/10000` in `N1a` is a bound, not an error estimate.** It certifies
   agreement between two routes at one step size. It is not a convergence proof
   and no order constant is extracted.

### What IS derived, stated positively so the fence is not mistaken for a retreat

The four identities of `N1` are **theorems about this construction**, not
measurements: `dH` is the cell sum because `H` is a cell sum; `dQ` is affine in
`dH` because `D_s` is `delta`-independent; `dG = -G dQ G` is the resolvent
derivative and is gated on **both** sides; and `dW = K_c^-1 (dL_2 - dK_c W)` is
the derivative of a quotient. **The method transfers to any profile, any core
and any width of this family unchanged** — that much is general even though no
number here is.

---

## READINGS — five of them, and each is a reading

- **`R1`.** *That the ten rationals are couplings of physical modes.* They are
  traces of `P_f dW` for an imposed `W`. **Reading.**
- **`R2`.** *That the joint sign flip of the heavy and boundary components means
  the two factors form one physical sector.* Measured: two trace components
  share a sign and flip together at two dial positions. **Reading.**
- **`R3`.** *That the support cutoff is a lattice light cone or a finite
  propagation speed.* Measured: three exact matrix equalities. The pattern is
  **not monotone in distance**, which is already evidence against the reading.
  **Reading.**
- **`R4`.** *That the cutoff is produced by empty-cross routing of `G dQ G`.*
  The naive support form of this is **refuted** in `N4b` by a dense `dG` and one
  counterexample. Some correct account exists; it is **not derived here** and is
  a **named open leg**. **Reading.**
- **`R5`.** *That the on-site/distance-one ratio contrast is a decay law.* Two
  positions at one core are two numbers. **Reading.**

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | family |
| ---: | --- | --- | --- |
| 1 | `origin/main`, axiom and registry blobs, worktree blobs, timeout | five pins fixed | `A` |
| 2 | `PARENT_COMMIT` ancestry, both Block 191 artifacts, stale pin carrying neither | exact | `A` |
| 3 | imposed / registered / adopted | `6 / 0 / 0` | `B` |
| 4 | gravity structures enumerated as NOT SUPPLIED | `10` | `B` |
| 5 | `GRAVITY_SUPPLIED`, `HYBRIDIZATION_PHYSICAL`, `CONTINUUM_LIMIT`, `TRANSFER_OPERATOR`, `MECHANISM_DERIVED`, `GENERALITY` | all `False` | `B` |
| 6 | `LOCKING_THRESHOLD_CLAIMED` | `False` — the dropped quantifier | `B` |
| 7 | `dB` vs the symbolic derivative of the import | residual `0` | `C` |
| 8 | displayed shear law at both probed volumes | residual `0`, 32 numbers | `C` |
| 9 | `(nnz(Ps H Ps - H), nnz(Ps Q Ps - Q^T))` | `(0, 0)` | `C` |
| 10 | `nnz(dH_sym - dH)`, `nnz(dQ_sym - dQ)` per bump | `0`, `0` | `C` |
| 11 | `nnz(Q dG + dQ G)`, `nnz(dG Q + G dQ)` per bump | `0`, `0` | `C` |
| 12 | `nnz(dK_c W + K_c dW - dL_2)`, all twelve pairs | `0` | `C` |
| 13 | `(nnz(dH), nnz(dQ), nnz(dG))` by bump | `56`, `200/152`, `3968` | `C` |
| 14 | finite-difference route: entrywise monotone, `e_R < 1/10000 < e_{h/2}`, scale `> 1/4` | all true | `C` |
| 15 | finite-difference route at the three cutoff pairs | **exact**, residual `0` | `C` |
| 16 | `charpoly(W)` at `t0 = 1`, `t0 = 3` | `heavy·light^2·boundary`, `heavy^2·light^2` | `D` |
| 17 | the ten `tr(P_f dW)` | the table in `N2` | `D` |
| 18 | all ten responses nonzero | `True` | `D` |
| 19 | the four `tr(dW)` totals | the block in `N2` | `D` |
| 20 | the four sum rules | exact equality | `D` |
| 21 | every CRT congruence, both systems; `sum_f P_f = I_8`; squarefree annihilator | residual `0` | `D` |
| 22 | `P_f(full) - P_f(squarefree)` | `0_8` entrywise | `D` |
| 23 | `abs(heavy - boundary)` at both bumps | `61132656/1842661567`, `56249856/1842661567` | `E` |
| 24 | shared denominator of both differences | `1842661567` | `E` |
| 25 | joint sign flip of heavy and boundary | `True` | `E` |
| 26 | light sign stability at both positions | `True` | `E` |
| 27 | on-site ratio at `t0 = 3` | exact, `8 < r < 9` | `E` |
| 28 | distance-one ratio at `t0 = 3` | exact, `9/10 < r < 1` | `E` |
| 29 | the six relative readings and the ten response decimals | the tables in `N2`, `N3` | `E` |
| 30 | `THRESHOLD_BY_POSITION`, `THRESHOLD_HOLDS_AT_BOTH_POSITIONS` | `{True, False}`, `False` | `E` |
| 31 | `nnz(dW)` over the twelve pairs; exactly three zeros | the table in `N4` | `F` |
| 32 | `nnz(W(1/5) - W(0))` over the twelve pairs | the same table | `F` |
| 33 | first-order table `==` finite table | `True` | `F` |
| 34 | the three zeros at `delta = 1/7` | `0` | `F` |
| 35 | the `({4,5}, t0=1)` triple and `tr(dW)` | `(0, 0, 0)`, `0` | `F` |
| 36 | `dL_2 - dK_c W` at the cutoff pairs; `L_2(delta) - M L_2`; `nnz(M - I_8)` | `0`, `0`, `64` | `F` |
| 37 | `(nnz(K_c(delta) - K_c), nnz(L_2(delta) - L_2))` at the cutoff pairs | `(64,60)`, `(64,60)`, `(64,64)` | `F` |
| 38 | `nnz(dG)`; `SUPPORT_ROUTING_IS_THE_MECHANISM` | `3968`; `False` | `F` |
| 39 | overlap-empty pairs; counterexample and its intersection; `OVERLAP_IS_A_CUTOFF_SIGNATURE` | `2 of 2`; `({4,5},1)` at `{4}`; `False` | `F` |
| 40 | the note at its final path; `N5` byte-identical; `sp.nsimplify` count | present; verbatim; `0` | `G` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

1. **THE ROUTE THAT WAS NOT TAKEN: symbolic inversion of `Q(delta)`.** The
   direct way to get `dW` is to invert `Q(delta)` with `delta` a symbol and
   differentiate the result. At `64 x 64`, with one entry of every shear block
   carrying `1/(1-delta)`, that is not a usable computation. The chain of `N1`
   exists precisely to avoid it, and the discipline it buys is measurable:
   **the only `delta = 0` inverse ever formed is one `64 x 64`, formed once and
   shared by every bump, every core and every derivative in the block.**
2. **THE CERTIFICATE THAT CANNOT BE AN EQUALITY.** An exact finite-difference
   elimination for `dW` was sought and does not exist: `W(delta)` is a rational
   function of `delta` of very high degree — `G(delta) = adj(Q)/det(Q)` at
   dimension `64` — so **no** finite linear elimination is exact at a generic
   pair. That is why `N1a` states a **convergence certificate with exact
   rational bounds** rather than an equality, and why the exactness that *is*
   available — at the three cutoff pairs, where `W(delta)` is constant — is
   stated and gated **separately**.
3. **THE IMAGE PARTNERS ARE THE EASY THING TO MISS, AND THE COST IS MEASURED.**
   Summing `dH` over the bumped **positive** anchors alone gives `nnz(dH) = 28`
   against the correct `56`, and disagrees with the entrywise symbolic
   derivative of the displayed profile in exactly those `28` entries, at every
   one of the four bumps. The `thA_s(t) = -1-t` image partners carry
   `P_4 dB P_4^T` and must be summed too. **Gate `C-4` catches that omission
   before any inverse is formed**, which is exactly why it differentiates the
   displayed profile rather than re-running the chain.
4. **THE ROUTING ACCOUNT CAME IN AS A CONJECTURE AND LEFT AS A GATE.** The solve
   proposed that the empty-cross block structure of `Q` routes `G dQ G` away
   from far cores. Measuring `nnz(dG) = 3968` killed the support form of it in
   **one number**; the follow-up search for a support *signature* then produced
   the `({4,5}, t0 = 1)` counterexample. **Both measurements are now gates
   (`F-8`, `F-9`), and the mechanism is a named open leg rather than a
   sentence.** The conjecture was not quietly dropped and it was not kept.
5. **"NINE TO ONE" WAS A ROUNDING, AND ROUNDINGS DO NOT SURVIVE HERE.** The
   on-site heavy/light ratio is `8.8744690837`, not `9`. It is stated as an
   exact rational with an exact rational bracket `8 < r < 9`, and the solve's
   round number appears in this note **only** where it is being withdrawn.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE PERTURBATION LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 (the staggered Dirac-Kahler carrier on Z_16 x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, 8}, the raising set A_s in the CLOSED half {0..8} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13)), BLOCK 191's VOLUME PROFILE (a map v from the positive anchors {0..7} to the positive rationals, placed as B(c, v(t)) for t < 8 and as the P_4 image of the block of its thA_s(t) = -1-t partner for t >= 8, assembled by the quarter-weighted four-corner cell average), THE ONE-PARAMETER BUMP FAMILY v = 1 - delta -- THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT -- THE FOUR BUMP POSITIONS {1,2}, {2,3}, {3,4}, {4,5} AND THE THREE VALID CORES t0 = 1, 3, 5, THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE THREE LABELLED FACTORS heavy, light and boundary WITH THEIR CRT PROJECTORS, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module AT A SYMBOLIC VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED AND NO PHYSICAL PERTURBATION IS PERFORMED: delta is a dial on an IMPOSED Hodge-volume parameter, 'response' names d/d(delta) of a rational matrix entry at delta = 0, and this block supplies NO lapse variable in an ADM phase space, NO Hamiltonian constraint, NO gauge orbit, NO quotient, NO Dirac observable and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, THE FIRST-ORDER RESPONSE OF THE EXACT MONODROMY TO A ONE-SLICE VOLUME BUMP IS COMPUTED IN CLOSED FORM WITHOUT INVERTING A SYMBOLIC MATRIX, AND IT VANISHES EXACTLY AT THREE OF TWELVE (bump, core) PAIRS. 'HYBRIDIZATION', 'LOCKING' AND 'SUPPORT CUTOFF' NAME PROPERTIES OF EXACT RATIONAL MATRICES: 'hybridization' NAMES the joint sign behaviour of two CRT trace components, 'locking' NAMES that joint sign behaviour AND NOT ANY MAGNITUDE AGREEMENT, and 'support cutoff' NAMES entrywise equality of two exact 8 x 8 matrices. THE SOLVE'S RELATIVE-AGREEMENT QUANTIFIER IS DROPPED, NOT SOFTENED: the adversarial check measured the {2,3} heavy/boundary relative difference ABOVE the quoted rational threshold 1/100 under the reference-relative and symmetric normalizations, so THIS BLOCK CLAIMS THE SIGN STRUCTURE ONLY and records six exact relative readings in its place. THE SUPPORT CUTOFF IS NOT A LIGHT CONE: it is a statement about which exact matrices are equal, and NO propagation speed, NO causal structure and NO continuum limit is supplied or implied. THE MECHANISM OF THE CUTOFF IS NOT DERIVED: 'empty-cross routing' is a READING and a NAMED OPEN LEG, and the naive support-overlap account is REFUTED HERE BY MEASUREMENT -- dG is DENSE at 3968 of 4096 entries at every cutoff pair, dK_c is FULL, and the pair ({4,5}, t0 = 1) overlaps the read window at t = 4 and still gives 0_8. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NO GENERALITY IS CLAIMED: ONE fixture, ONE width, FOUR bump positions, THREE cores, THREE amplitudes, and NOTHING about the infinite-width or continuum limit. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE METHOD THEOREM IS A CHAIN OF FOUR DISPLAYED IDENTITIES AND NO SYMBOLIC MATRIX IS EVER INVERTED. With v = 1 - delta on the bumped positive anchors: dB = d/d(delta) shear_hodge(c, 1-delta) at delta = 0 = -E00 - (169/144)(E11+E22) + (65/144)(E12+E21) + E33 -- GATED entrywise at ZERO against the SYMBOLIC derivative of the IMPORTED shear_hodge, and the underlying law gated at BOTH probed volumes, thirty-two numbers; dH = the SAME quarter-weighted cell sum over the bumped anchors AND their thA_s image partners, with P_4 dB P_4^T on the images; dQ = m dH + dH D_s - D_s^T dH, exact because D_s does not depend on delta; dG = -G dQ G with the KNOWN v = 1 inverse; and dW = K_c^-1 (dL_2 - dK_c W). EVERY LINK IS GATED AT EXACTLY ZERO: nnz(dH_symbolic - dH_cellsum) = 0 and nnz(dQ_symbolic - dQ_law) = 0 by entrywise symbolic differentiation of the displayed profile BEFORE any inverse is formed, nnz(Q dG + dQ G) = 0 and nnz(dG Q + G dQ) = 0 on BOTH the left and right resolvent equations, and nnz(dK_c W + K_c dW - dL_2) = 0 at all twelve pairs. THE FINGERPRINTS ARE MEASURED: nnz(dH) = 56 at every bump, nnz(dQ) = 200 for the odd-anchor bumps {1,2} and {3,4} and 152 for the even-anchor bumps {2,3} and {4,5}, and nnz(dG) = 3968 at every bump. AND THE CHAIN IS GATED AGAINST AN INDEPENDENT ROUTE: exact-rational forward differences of W at delta = 1/100 and 1/200 with the exact first linear elimination 2 D(h/2) - D(h) converge to the propagated dW ENTRYWISE MONOTONICALLY in all sixty-four entries and to within 1/10000 of it while the operator's own scale exceeds 1/4 -- and at the three cutoff pairs the finite-difference route is EXACT, equal to dW entrywise at BOTH delta = 1/5 and delta = 1/7. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's zeros, signs, differences or traces could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate G.\nper_mode: THE TEN RATIONALS AND THE FOUR SUM RULES ARE EXACT AND THE PROJECTORS ARE CONGRUENCE-GATED. At t0 = 1 the baseline spectrum is heavy*light^2*boundary and at t0 = 3 it is heavy^2*light^2, so the two bumps give TEN per-factor first-order trace responses tr(P_f dW), ALL NONZERO: bump{3,4} at t0=1 gives heavy 840153195543/196300900625, boundary 59790687128721117/13862573301236875 and light 21615004253318/12284407006475; bump{2,3} at t0=1 gives heavy -421462341183472199/177215545561734375, boundary -29381217534120895221181/12514784612024119828125 and light 22866757183474123654/19424018367789224675; bump{3,4} at t0=3 gives heavy -152770523741944777898/10738971376744546875 and light -6227354334614993838/3884803673557844935; bump{2,3} at t0=3 gives heavy -1495288291042/1427461510575 and light -2705696606558/2456881401295. EACH PROJECTOR IS P_f = q_f(W) with q_f = M_f (M_f^-1 mod f^k) mod chi and M_f = chi/f^k, and EVERY congruence q_f = 1 mod f^k, q_f = 0 mod g^l is a ZERO POLYNOMIAL RESIDUAL over QQ; the projectors SUM TO I_8 at zero residual and the squarefree total ANNIHILATES W at zero residual. ALL FOUR SUM RULES tr(dW) = sum_f tr(P_f dW) hold at EXACT EQUALITY. AND THE CHECK'S P1 IS FOLDED AS CONTENT AND STRENGTHENED: the projectors built from the FULL multiplicities and from the SQUAREFREE total are THE SAME MATRIX ENTRY FOR ENTRY, which is strictly stronger than the trace agreement the solve needed.\nper_block: THE RESPONSE TABLE CLAIMS THE SIGN STRUCTURE AND THE EXACT DIFFERENCES, AND THE SOLVE'S QUANTIFIER IS DROPPED AS CONTENT. At t0 = 1 the heavy and boundary responses share a sign at each position and FLIP TOGETHER between them -- both positive at {3,4}, both negative at {2,3} -- while the light response is POSITIVE at both, so the light factor is sign-stable where the other two are not. Their exact differences are |heavy - boundary| = 61132656/1842661567 at {3,4} and 56249856/1842661567 at {2,3}: BOTH NONZERO, so the two factors do NOT respond identically, and BOTH OVER THE SAME DENOMINATOR 1842661567. THE ADVERSARIAL CHECK REFUTED THE SOLVE'S RELATIVE-AGREEMENT QUANTIFIER AT ONE OF ITS TWO REQUIRED POSITIONS AND THE QUANTIFIER IS THEREFORE DROPPED AND NOT RENORMALIZED: the six exact relative readings, as integers over 10^10, are 0.0077516025, 0.0076919774 and 0.0077216748 at {3,4} against the heavy reference, the boundary reference and the symmetric normalization, and 0.0128356799, 0.0130025768 and 0.0129185893 at {2,3} -- so the quoted rational threshold 1/100 holds at {3,4} under all three normalizations and FAILS at {2,3} under all three, and THRESHOLD_HOLDS_AT_BOTH_POSITIONS = False is a declared constant with a gate and a mutation. AT t0 = 3 THE POSITION DEPENDENCE IS A RATIO AND NOT AN ADJECTIVE: the ON-SITE bump {3,4} is heavy-dominated at the exact ratio 37533905844768035289054578457791/4229425500383349914656444790625, strictly between 8 and 9, and the DISTANCE-ONE bump {2,3} is scale-balanced at 232340137594542523/244263525398539845, strictly between 9/10 and 1.\nlattice_wide: THE SUPPORT-CUTOFF LAW, AND IT IS THE CHECK'S DISCOVERY CARRIED AS THIS BLOCK'S CENTRE. Over the TWELVE valid (bump, core) pairs -- bumps {1,2}, {2,3}, {3,4}, {4,5} against cores t0 = 1, 3, 5 -- nnz(dW) is 64 at NINE pairs and EXACTLY ZERO at THREE: ({1,2}, t0=5), ({2,3}, t0=5) and ({4,5}, t0=1). THE SAME THREE ZEROS APPEAR AT FINITE AMPLITUDE: nnz(W(delta) - W(0)) is the SAME TWELVE-ENTRY TABLE at delta = 1/5, and the three zeros are reproduced at delta = 1/7, so the WHOLE 8 x 8 monodromy is unchanged ENTRYWISE and the cutoff is NOT a linearization artefact. THE CUTOFF IS DIRECTIONAL AND NOT RADIAL: bump {3,4} REACHES t0 = 5 while bump {2,3} does NOT, and bump {4,5} MISSES t0 = 1 while bump {3,4} reaches it, so 'the response decays with distance' is FALSE as a description of this table. THE EXTRA POSITION IS A CUTOFF AND NOT A PERSISTENCE: bump {4,5} at t0 = 1 is a VALID probe -- {4,5} lies in the positive-anchor domain {0..7} and t0+3 = 4 < 8 is interior -- and its exact first-order triple is (0, 0, 0) with tr(dW) = 0, which is a TRIVIAL equality and NOT the survival of a nonzero response. B191's {2,3} EXACT ZERO IS HEREBY IDENTIFIED: it is not a root shift or a resultant but WHOLE-OPERATOR INVARIANCE at t0 = 5.\nper_scope: THE MECHANISM IS MEASURED AS A PAIRING GAUGE AND THE ROUTING READING IS REFUTED BY MEASUREMENT. The underlying pairings are NOT individually fixed at any cutoff pair: at delta = 1/5, nnz(K_c(delta) - K_c) = 64 at all three and nnz(L_2(delta) - L_2) is 60, 60 and 64, so BOTH pairings move in almost every entry. What is exact is that they move TOGETHER: dL_2 = dK_c W at ZERO residual at first order, and at finite delta the common left factor M = K_c(delta) K_c^-1 satisfies L_2(delta) = M L_2 at ZERO residual with M - I nonzero in all 64 entries. W = K_c^-1 L_2 is invariant under exactly that motion, and THAT is the whole of the cancellation. THE EMPTY-CROSS ROUTING ACCOUNT IS A READING AND A NAMED OPEN LEG, AND ITS NAIVE FORM IS REFUTED HERE: dG is DENSE at 3968 of 4096 entries at every cutoff pair, so nothing is routed away in the support sense; and the support-overlap signature is SUFFICIENT BUT NOT NECESSARY -- emptiness of the overlap between the bump's measured site-time support and the core's read window forces the zero in BOTH cases where it holds, but ({4,5}, t0 = 1) OVERLAPS that window at t = 4 and still gives 0_8, the ONE counterexample among the ten overlapping pairs. NO SUPPORT SIGNATURE DEFINES THE CUTOFF, AND THE DERIVATION OF ITS MECHANISM IS OPEN.\nRESULT: THE FIRST-ORDER RESPONSE OF THE UNIT-CELL MONODROMY TO A ONE-SLICE HODGE-VOLUME BUMP IS OBTAINED IN CLOSED FORM BY A FOUR-STEP DERIVATIVE CHAIN THAT NEVER INVERTS A SYMBOLIC MATRIX, TEN EXACT PER-FACTOR RATIONALS AND FOUR SUM RULES ARE COMPUTED AND CONGRUENCE-GATED, AND AN EXACT DIRECTIONAL SUPPORT CUTOFF IS ESTABLISHED AT THREE OF TWELVE (bump, core) PAIRS AT FIRST ORDER AND AT TWO FINITE AMPLITUDES -- AND NOT ONE LINE OF IT IS A LAPSE, A CONSTRAINT, A LIGHT CONE, A PROPAGATION SPEED OR A CONTINUUM LIMIT. The displayed dB is gated against the symbolic derivative of the import; every link of the chain closes at exactly zero on both resolvent equations; an independent exact-rational finite-difference route converges entrywise and is EXACT at the cutoff pairs; the ten rationals are all nonzero and the full and squarefree projectors agree entrywise; the solve's relative-agreement quantifier is DROPPED and replaced by six exact readings and the sign structure; and the naive support-routing account of the cutoff is REFUTED by a dense dG and by one measured counterexample. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-191 STAND EXACTLY AS LANDED. BLOCK 191 IS NOT CORRECTED: its t0 = 1 and t0 = 3 baseline factorizations are reproduced here digit-for-digit as this block's control, and its {2,3} exact zero at t0 = 5 is reproduced and then EXPLAINED as whole-operator invariance rather than revised. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE fixture, ONE width, FOUR bump positions, THREE cores and THREE amplitudes -- four positions are not a scan; the cutoff's MECHANISM IS NOT DERIVED and is a named open leg; and the block's own solve language is corrected in two places rather than papered over. FOUR ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C3 REFUTATION, that the relative-agreement quantifier fails at {2,3} under all three standard normalizations and is therefore DROPPED with only the sign structure claimed; the C4 IDENTIFICATION, that B191's {2,3} zero is whole-operator invariance at t0 = 5 and not a root shift; the P2 RECLASSIFICATION, that bump {4,5} at t0 = 1 is an exact SUPPORT CUTOFF with triple (0,0,0) and NOT a persistence of nonzero locking; and the P1 STRENGTHENING, that the full-multiplicity and squarefree CRT projectors agree ENTRY FOR ENTRY and not merely in trace. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE HYBRIDIZATION MECHANISM SOLVE (block 192 candidate), HYB PHASE 1 MEASURED, HYB PHASE 2 and B192 CHECK VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **Symbolic inversion of `Q(delta)`.** Stopped: not needed and not tractable.
   The chain supersedes it.
2. **Any second-order or full-`delta` expansion.** Stopped: this block computes
   a **first** derivative and two finite amplitudes. Second-order coefficients
   are not computed and are not claimed to vanish anywhere.
3. **A derivation of the cutoff's mechanism.** Stopped **as an open leg, not as
   a refutation**: the naive support account is dead (`N4b`), and no replacement
   is offered.
4. **Any statement about magnitude agreement between the heavy and boundary
   responses.** Stopped: the quantifier is dropped and only signs are claimed.
5. **Any continuum, infinite-width or propagation-speed reading.** Stopped at
   `N0` and fenced at `N4g`.

### REOPEN IF

1. **The cutoff table is extended to cores `t0 = 0, 2, 4` and to `T = 20`.** If
   the three-zero pattern survives a full core scan at a second width, the
   directionality becomes a candidate *law* rather than a twelve-entry table.
2. **A correct mechanism is found for the pairing gauge.** The object to explain
   is precise: why the perturbation acts on `(K_c, L_2)` by a **common left
   factor** at exactly those three pairs, given that `dG` is dense at all of
   them.
3. **A second fixture is run.** Every rational here carries `(9/20, 5/13)` in
   it. Whether the *zeros* are fixture-independent is a sharp, cheap question
   and is not answered here.
4. **The `({4,5}, t0=1)` counterexample is explained.** It is the one pair that
   overlaps the read window and still cuts off. Any account of the mechanism
   must produce it.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 191's #32. NO CORRECTION IS LANDED BY THIS
BLOCK AGAINST ANY LANDED NUMBER.** Four of the adversarial check's findings —
`C3`, `C4`, `P2` and `P1`, items 33, 35, 36 and 40 — are carried as **content**
rather than as errata; five further items (34, 37, 38, 39, 41) correct or
extend this block's own solve language; and every one of the nine is a declared
constant with a gate and a mutation.

33. **THE C3 REFUTATION — THE RELATIVE-AGREEMENT QUANTIFIER IS DROPPED.** The
    solve claimed the heavy and boundary responses agree within the rational
    threshold `1/100` at **both** bump positions. Measured independently here:
    `{3,4}` is below it under all three standard normalizations and `{2,3}` is
    above it under all three. **The quantifier is dropped and only the sign
    structure is claimed.** `THRESHOLD_HOLDS_AT_BOTH_POSITIONS = False` is a
    declared constant, gates `B-4`/`E-7`, mutation `claim_locking_threshold`.
34. **AND THE REPLACEMENT IS EXACT, NOT A RENORMALIZATION.** No normalization is
    hunted for under which the statement becomes true. What replaces it is the
    pair of exact differences `61132656/1842661567` and `56249856/1842661567`,
    their shared denominator `1842661567`, and the six exact relative readings
    of `N3`. Gates `E-1`, `E-2`, `E-7`, mutations `break_response_differences`,
    `break_shared_denominator`, `break_relative_readings`.
35. **THE C4 IDENTIFICATION — BLOCK 191's ZERO IS WHOLE-OPERATOR INVARIANCE.**
    Block 191 recorded its `{2,3}` zero at `t0 = 5` as "out of range" and left
    its nature open. It is `W(1/5) - W(0) = 0_8` **entrywise**, reproduced at
    `delta = 1/7` and at first order. Gates `F-2`, `F-4`, `F-5`, mutations
    `break_finite_cutoff_table`, `break_second_amplitude`, `break_operator_zeros`.
36. **THE P2 RECLASSIFICATION — THE EXTRA POSITION IS A CUTOFF, NOT A
    PERSISTENCE.** Bump `{4,5}` at `t0 = 1` is valid and gives the exact triple
    `(0, 0, 0)`. Recording that as "the locking persists at a third position"
    would be false: it is a **trivial** equality. Gate `F-6`, mutation
    `break_extra_bump_triple`.
37. **AND THIS BLOCK EXTENDS THE CHECK'S TWO ZEROS INTO A TABLE.** The check
    exhibited two zeros. Scanning all twelve valid pairs finds a **third**,
    `({1,2}, t0 = 5)`, and shows the pattern is exactly three of twelve at first
    order and at both finite amplitudes. **The check found the phenomenon; the
    scan found its shape.** Gates `F-1`–`F-3`.
38. **THE SOLVE'S GLOBAL-DECAY READING IS WITHDRAWN.** "The bump response decays
    with distance" is **false** as a description of the table: bump `{3,4}`
    reaches `t0 = 5` while bump `{2,3}` does not, and bump `{4,5}` misses
    `t0 = 1` while bump `{3,4}` reaches it. The cutoff is **directional**. Gate
    `F-1`, mutation `break_cutoff_table`.
39. **AND THE EMPTY-CROSS ROUTING MECHANISM IS REFUTED IN ITS NAIVE FORM AND
    NAMED AS AN OPEN LEG.** `dG` is dense at `3968` of `4096` entries at every
    cutoff pair and both restrictions are full, so nothing is routed away; and
    the support-overlap signature is **sufficient but not necessary**, with
    exactly one counterexample, `({4,5}, t0 = 1)`, overlapping at `t = 4`.
    `SUPPORT_ROUTING_IS_THE_MECHANISM = False` and
    `OVERLAP_IS_A_CUTOFF_SIGNATURE = False` are declared constants, gates
    `F-8`/`F-9`, mutations `break_dense_resolvent`, `break_overlap_rule`, and
    `claim_mechanism_derived` guards the open leg itself.
40. **THE P1 STRENGTHENING, CREDITED TO THE CHECK.** The check asked whether the
    squarefree replacement changes the traces. It does not, and the reason is
    stronger: the two projector constructions give **the same matrix entry for
    entry**. Gate `D-7`, mutation `break_squarefree_projectors`.
41. **AND ONE IN-SOLVE CATCH, RECORDED BECAUSE THE ROUNDING WAS LOAD-BEARING.**
    The solve wrote the on-site heavy/light contrast as "`9:1`". The exact ratio
    is `37533905844768035289054578457791/4229425500383349914656444790625` and
    lies strictly between `8` and `9`. It is stated as an exact rational with an
    exact bracket, and the round number survives only as the withdrawn value.
    Gate `E-5`, mutation `break_onsite_ratio`.

### The adversarial check

Verdict carried as **CONFIRMED EXCEPT ONE QUANTIFIER, WITH TWO DISCOVERIES
FOLDED** (`sol xhigh`, cross-model, an independent compact rebuild from the
landed Block 190 and Block 191 notes rather than an invocation of either runner;
findings preserved at `b192_check_findings.md`).

**CONFIRMED EXACTLY, ON AN INDEPENDENT RECONSTRUCTION.** The `C1` derivative
chain including the image-partner contributions and every defining-equation
residual, with its own exact-rational finite-difference convergence route; all
ten `C2` rationals and all four sum rules; the `C4` nonvanishing of all ten
components; and the `P1` CRT congruences with full/squarefree agreement.

**REFUTED AS WORDED, NOW A GATE RATHER THAN PROSE:** `C3`'s relative-agreement
quantifier (correction 33, replaced by 34).

**THE TWO DISCOVERIES ARE THIS BLOCK'S CENTRE**, and both are credited to the
check: the identification of Block 191's zero as whole-operator invariance
(correction 35) and the reclassification of the extra position as an exact
support cutoff (correction 36). This block extends them into the twelve-pair
directional table (correction 37) and refutes the routing account of their
mechanism (correction 39).

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–191 number **stands as landed**.
Block 191's `t0 = 1` and `t0 = 3` baseline factorizations are reproduced here
digit-for-digit as this block's control, and its `{2,3}` zero at `t0 = 5` is
reproduced and then **explained** rather than revised. Block 188's landed
`T = 8` object is untouched and the wrap-edge family remains a **disclosed
variant** of it.

### Reproduction

```
python3 scripts/admissibility_dirac_kahler_hybridization_mechanism_support_cutoff_2026_08_25.py
python3 ... --list-mutations
python3 ... --mutation break_overlap_rule
```

Exact throughout: sympy `Rational`/`Integer` only, `DomainMatrix` over `QQ` for
the twelve exact `64 x 64` inverses — **one at `delta = 0`, built once and shared
by every bump, every core and every derivative**, and eleven more at the finite
amplitudes — exact `factor_list` over `Q` for the baseline control, exact
polynomial arithmetic over `QQ` for every CRT congruence, and **no float, no
tolerance and no `sp.nsimplify` anywhere** — the last of which is *measured* in
the runner's own source by gate `G-3` rather than promised. The single numeric
layer is `evalf` at 40 digits of exact rationals, gated to ten decimal places,
and nothing numeric is ever fed back into a construction.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE HYBRIDIZATION MECHANISM
SOLVE (block 192 candidate)**, **HYB PHASE 1 MEASURED**, **HYB PHASE 2 — THE
MECHANISM NUMBERS** and **B192 CHECK VERDICT** anchors.
