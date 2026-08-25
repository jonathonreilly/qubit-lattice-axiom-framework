---
title: "Admissibility — Dirac-Kähler Boundary Modes And Hodge-Volume Spectral Sensitivity"
date: 2026-08-25
block: 191
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_boundary_mode_volume_sensitivity_2026_08_25.py
parent_ref: origin/physics-loop/toe-axiom-closure-block190-width-family-transfer-monodromy-20260825
parent_commit: e75ad9f4998ae4cc6a25a2e20191e0b9d76ff3fd
current_main: b11811704efa98a12272d572f666e530a807f6c1
registered: 0
adopted: 0
axiom_movement: none
---

# Boundary Modes Of The Unit-Cell Monodromy, And The Hodge-Volume Spectral Sensitivity — with LAPSE PHYSICALITY fenced as a reading throughout

**One sentence.** On Block 190's wrap-edge width family at the same fixture
`(m, c) = (9/20, 5/13)`, the unit-cell monodromy `W = K_c^-1 L_2` is measured at
**every** core of `T = 20`: the light pair is **boundary-rigid**, one heavy copy
is replaced at the seam-adjacent cores by an exactly **non-reciprocal** boundary
quadratic whose coefficients **reverse exactly** between the near and far
seams, the Hodge-volume parameter `v` of Block 105's `shear_hodge(c, v)` moves
the two deep scales in **opposite** directions, and a **localized** volume bump
destroys palindromicity in **every** irreducible factor at every probed core —
and **not one line of this establishes that `v` is a lapse or that these shifts
are lapse physics**.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Six imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE HEADLINE WORD IS FENCED BEFORE THE FIRST NUMBER IS READ, AND IT IS
FENCED HARDER THAN ANY WORD IN BLOCK 190.**

- **LAPSE PHYSICALITY IS A READING, AND IT IS NOT ESTABLISHED HERE.** `v` is
  the **imposed Hodge-volume parameter** of Block 105's `shear_hodge(c, v)`.
  This block supplies **no lapse variable in an ADM phase space, no Hamiltonian
  constraint, no gauge orbit, no quotient, no Dirac observable and no OS
  reconstruction** that would make `W` a physical transfer operator. What is
  **measured** is narrower and is stated as such throughout: *within this
  imposed finite matrix construction, uniform and localized changes of the
  Hodge volume alter the exact monodromy spectrum, while the specified
  reflection covariance survives exactly.*
- **`Ps`-COVARIANCE DOES NOT DECIDE PHYSICAL EQUIVALENCE.** Every profile in
  `N3` satisfies `Ps H Ps = H` and `Ps Q Ps = Q^T` at exactly zero. That proves
  **compatibility with this one reflection** and nothing more. **That two
  `v(t)` profiles are physically inequivalent is NOT proven by this block**, and
  the campaign's Phase-2/Phase-3 wording "the volume dial is PHYSICAL" and
  "lapse inhomogeneity is REAL physics" is carried here **only** as reading
  `R1`/`R2`.
- **"BOUNDARY MODE" IS A NAME FOR A FACTOR, NOT A CLAIM ABOUT A SURFACE.** The
  non-reciprocal quadratic of `N2` is an exact rational factor of a
  characteristic polynomial at a seam-adjacent core. That it *is* an edge
  excitation of a physical boundary **is a reading** (`R3`).
- **`W` IS NOT A TRANSFER OPERATOR HERE.** Block 190 refuted the naive OS
  transfer pairing on this class with six exact witnesses, and that refutation
  is **not** repaired by anything in this note.
- **AND THE CHECK'S P1 IS FOLDED, NOT ARGUED: BOUNDARY-MODE DOMINANCE IS
  REFUTED AS STATED.** The solve's "the edge mode is the bump's antenna" is
  **withdrawn as content**. What is measured is **hybridization**: the boundary
  and bulk-heavy factors **merge into one irreducible `U = -1` quartic** and
  their large roots shift **comparably**, `0.9570159788` against `0.9443699527`.

**TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED**, so the absence is a
count and not a mood: lapse function; shift vector; ADM phase space;
Hamiltonian constraint; momentum/diffeomorphism constraint; first-class
constraint algebra; Dirac closure; Dirac observable; gauge orbit and its
quotient; Osterwalder–Schrader reconstruction of a transfer operator.

**NO GENERALITY IS CLAIMED.** One fixture `(9/20, 5/13)`, two widths `T = 16`
and `T = 20`, four volume profiles, one bump amplitude `v = 4/5`. No bracket,
no ray, no edge, no interior, and **nothing about the infinite-width limit**.

**THE OBJECT IS STILL A DISCLOSED VARIANT.** The carrier is Block 190's
wrap-edge family (`w = -1` at `t = T-1`), which is **not** Block 188's landed
`T = 8` object (`w = -1` at `t = 3`). Block 188, Block 189 and Block 190 are
neither corrected nor contradicted by anything below.

---

## W1 — the wall, and the charter

### What was open

Block 190 closed the naive OS transfer question negatively, exhibited a
width-invariant, position-homogeneous step operator, and computed a primitive
unit-cell monodromy with a proven positive reciprocal spectrum at the **deep**
cores `t0 = 3, 4, 5` of `T = 20`. It left the boundary explicitly untouched:
its own `N6` recorded that all inhomogeneity lives in the metric data and the
finite-range boundary layers, and named the boundary layer as the next object.
Two questions were therefore open and are the whole of this block:

1. **What does `W` do at the seam?** Block 190 probed three deep cores. The
   near-seam and far-seam cores were never computed.
2. **Does the Hodge volume `v` — held at the pinned value `1` throughout Block
   190 — move the spectrum, and does a *localized* `v(t)` move it?**

### The charter

1. Scan **every** core of `T = 20`, `t0 = 1..8`, and report the exact
   factorization at each — no sampling, no deep-core selection.
2. Say **exactly** where the pairing stops describing a bulk object, and gate
   the rule at **both** widths.
3. Turn the volume dial uniformly, then locally, and measure the exact spectra
   — never a description of them.
4. **Fence the word "lapse" before the first number**, and keep the
   established statement narrower than the tempting one at every step.

---

## N1 — THE CONSTRUCTION CONTROL, and the volume law is displayed as a formula

**NOTHING BELOW IS ABOUT THE LANDED CHAIN'S OBJECT IF THIS SECTION IS NOT
EXACT.**

### The one import, and the volume law it generalises

The only object imported from the landed chain is Block 105's `shear_hodge()`,
read through the Block 128 module. Block 190 displayed it at the pinned unit
volume; **this block needs the volume as a variable, so the law itself is
displayed:**

```
shear_hodge(c, v) = diag( v,  v * g(c)^-1,  1/v ),      g(c) = [[1, c], [c, 1]]

                    [ v         0              0        0   ]
                  = [ 0    v/(1-c^2)    -v c/(1-c^2)    0   ]
                    [ 0   -v c/(1-c^2)   v/(1-c^2)      0   ]
                    [ 0         0              0       1/v  ]
```

in the zero-based corner order `(1, dx, dt, dx^dt)`. At `c = 5/13` this is:

| volume | displayed block |
| --- | --- |
| `v = 1` | `diag(1, 169/144, 169/144, 1)` with `(1,2) = (2,1) = -65/144` — **Block 190's pinned matrix** |
| `v = 4/5` | `diag(4/5, 169/180, 169/180, 5/4)` with `(1,2) = (2,1) = -13/36` |

Gate `C-2` compares **both** displayed matrices to `b128.block105.shear_hodge`
entrywise at zero residual, so the note's formula and the landed function are
measured to be the same thirty-two numbers.

### The profile rule, stated once

For even `T` with `half = T/2`, a **volume profile** is a map `v : {0..half-1}
-> Q_{>0}` on the positive anchors. The site Hodge places

```
block(t) = B(c, v(t))                      for t < half,
block(t) = P_4 B(c, v(thA_s(t))) P_4^T     for t >= half,   thA_s(t) = -1-t,
```

and `H` is the quarter-weighted sum of the four-corner embeddings, exactly as
in Block 190. **A uniform profile reproduces Block 190's rule identically**;
the `thA_s` extension is the only new construction element in this block, and
it is the unique extension that keeps the image half the mirror of the
positive half under `theta_s(t) = -t`. Everything downstream —
`d_K = P1 K P0 + P2 K P1`, `A_s`, `D_s = A_s - Ps A_s Ps`,
`Q = m H + H D_s - D_s^T H`, `G = Q^-1`, `K_c`, `L_k`, `V`, `W` — is Block
190's, unchanged.

### The four profiles of this block

| name | `v` on the positive anchors | used by |
| --- | --- | :---: |
| **`v = 1`** | `1` everywhere | `N2`, `N3` baselines |
| **`v = 4/5` uniform** | `4/5` everywhere | `N3` (the dial) |
| **bump `{3,4}`** | `4/5` at `t = 3, 4`; `1` elsewhere | `N4` |
| **bump `{2,3}`** | `4/5` at `t = 2, 3`; `1` elsewhere | `N4` (position dependence) |

`Ps H Ps - H` and `Ps Q Ps - Q^T` are **zero for all four**, gated at `C-3`
and `E-1`.

---

## N2 — THE BOUNDARY MONODROMY, scanned at EVERY core of two widths

**NO CORE IS SAMPLED AND NONE IS SKIPPED.** Block 190 reported `charpoly(W)` at
`t0 = 3, 4, 5` of `T = 20`. Here `t0` runs over `1..T/2` at **both** `T = 16`
and `T = 20`. Write

```
heavy  = 22569375 z^2 - 233631106 z + 22569375          (Block 190's deep pair)
light  = 39529825 z^2 - 109432706 z + 39529825          (Block 190's deep pair)
near   = 43033320714375 z^2 - 445467467014578 z + 48554286398375
mirror = 48554286398375 z^2 - 445467467014578 z + 43033320714375
second = 48554286398375 z^2 - 376762652339458 z + 35686537764375
```

### The table, and it is POSITIONALLY WIDTH-LOCKED

| core, by position | `T = 16` | `T = 20` | `charpoly(W)` | `L_2` reach |
| --- | :---: | :---: | --- | --- |
| `t0 = 1` — **near seam** | `1` | `1` | `heavy · light^2 · near` | bulk |
| interior | `2, 3` | `2, 3, 4, 5` | `heavy^2 · light^2` | bulk |
| `t0 = T/2 - 4` — **far mirror** | `4` | `6` | `heavy · light^2 · mirror` | bulk |
| `t0 = T/2 - 3` — **second layer** | `5` | `7` | `heavy · light^2 · second` | **touches** `T/2` |
| `t0 = T/2 - 2` | `6` | `8` | degree pattern `(2, 2, 4)`, quartic irreducible over `Q` | **crosses** |
| `t0 = T/2 - 1` | `7` | `9` | degree pattern `(2, 2, 4)`, quartic irreducible over `Q` | **crosses** |
| `t0 = T/2` | `8` | `10` | `heavy · light^2 · rev(second)` — **all quadratic again** | **crosses** |

**Every entry in that table is the same polynomial at both widths.** The
boundary layer of `W` is not a `T`-dependent artefact: it is a **finite-range
layer measured at two widths with identical values**, one core thick on the
near side and two cores thick on the far side (`mirror` then `second`), which
is the `P_4`-image asymmetry of the glue showing up in the invariant.

### Three exact facts, each gated

**(1) THE LIGHT PAIR IS BOUNDARY-RIGID.** `light^2` divides `charpoly(W)`
**exactly**, with multiplicity exactly two, at **every** `t0 = 1..T/2 - 3` at
both widths, and again at `t0 = T/2`. **The light mode does not see the
boundary at all.** Gate `C-5`.

**(2) THE HEAVY SECTOR LOSES EXACTLY ONE COPY AT EVERY LAYER CORE.** At the
**six bulk-valid layer cores** — `t0 = 1`, `t0 = T/2 - 4` and `t0 = T/2 - 3`,
at both widths — the multiplicity of `heavy` is exactly one and the missing
copy is replaced by a **non-reciprocal** quadratic. Gate `C-6`. The same
single-copy pattern recurs at the *crossing* core `t0 = T/2`, where it is
gated by `C-7` as a table entry but is **not** claimed as bulk data. The layer
is **mode-selective**: it lives in the heavy sector only.

**(3) THE BOUNDARY FACTORS ARE POSITIVE AND NON-RECIPROCAL, EXACTLY.**

| factor | `a - c` (zero iff reciprocal) | `c/a` (product of roots) | discriminant | roots |
| --- | ---: | :---: | --- | --- |
| `near` | `-5520965684000` | `388434291187/344266565715` | `190083455453828589664707955584 = 2^7·3^4·13·313·70619·96676423·659962871` | two distinct **positive** reals |
| `mirror` | `+5520965684000` | `344266565715/388434291187` | the **same** integer | two distinct **positive** reals |
| `second` | `+12867748634000` | `180555/245659` | `135019158697151741387932171264 = 2^10·13·313·32404681043299888780819` | two distinct **positive** reals |

**`a != c` is the exact statement that the seam breaks `lambda -> 1/lambda`**,
and the discriminants being positive integers with `a > 0`, `-b > 0`, `c > 0`
is the exact statement that both roots are real and positive. **Positivity
survives at the seam; reciprocity does not.** Gates `C-8`, `C-9`.

### The near/far reversal is EXACT, coefficient for coefficient

```
mirror(z) = rev(near)(z),     i.e.   (a, b, c) -> (c, b, a),
```

at both widths — `near` and `mirror` share the same middle coefficient
`-445467467014578` **and the same discriminant**, and their leading and
constant coefficients are exchanged **exactly**. Equivalently, for
`near(z) = a z^2 + b z + c`,

```
z^2 near(1/z) = a + b z + c z^2 = c z^2 + b z + a = mirror(z)
```

identically — no normalisation — so `spec(mirror) = {1/lambda : lambda in
spec(near)}`. This is the seam's mirror covariance acting on the boundary
factor itself, and it is gated at `C-10` at both widths. The same reversal
recurs once more at the far end: at `t0 = T/2` the surviving non-reciprocal
factor is `rev(second)`, gated as a table entry by `C-7` and as a pattern by
`C-14`.

---

## N2a — THE BOUNDARY OF VALIDITY, and it is a rule about the PAIRING and NOT about factoring

**THE CHECK'S C2 CORRECTION IS CARRIED HERE AS CONTENT, AND THIS BLOCK THEN
STRENGTHENS IT AGAINST ITSELF.**

The pairing `L_2[a,b] = G[idx(t_b + 2, x_b), idx(theta_s t_a, x_a)]` reads `G`
at times `{t0+2, t0+3}`. The construction's fixed slices are `{0, T/2}` and the
image half is `t > T/2`. Therefore:

| condition | name | status |
| --- | --- | --- |
| `t0 + 3 < T/2` | interior | admissible |
| `t0 + 3 = T/2` | **touches** the fixed slice | **admissible** |
| `t0 + 3 > T/2` | **crosses** into the image half | **NOT a bulk object** |

**Touching is admissible and crossing is not, and the reason is the definition
of the pairing** — a core whose `L_2` reads the image half is pairing a
physical state against a reflected one, which is a different object from the
one `N2` measures. Verified at both widths: `T = 20, t0 = 7` and `T = 16,
t0 = 5` touch and factor exactly as the table says (gate `C-11`); `T = 20,
t0 = 8` and `T = 16, t0 = 6` cross.

**THE "NON-FACTORING SIGNATURE" IS WITHDRAWN, AND IT IS WITHDRAWN TWICE OVER.**
The solve asserted that boundary-crossing cores are detectable because their
`W` **does not factor over `Q`**. That is false in **both** directions and this
block measures both:

1. **Crossing cores DO factor.** At `T = 16, t0 = 6` and `T = 20, t0 = 8` the
   degree-eight polynomial splits over `Q` with degree pattern **`(2, 2, 4)`** —
   two rational quadratics and one **irreducible rational quartic**. The
   observed signature is *failure to split completely into rational
   quadratics*, not irreducibility. Irreducibility of each quartic has a short
   certificate: the `T = 16` crossing quartic is irreducible **mod 11** and the
   `T = 20` crossing quartic is irreducible **mod 67**, hence irreducible over
   `Q` by Gauss's lemma. Gates `C-12`, `C-13`.
2. **AND SOME CROSSING CORES FACTOR COMPLETELY INTO QUADRATICS.** At
   `t0 = T/2` — deep inside the crossing region at both widths — the pattern
   returns to `heavy · light^2 · rev(second)`, i.e. **`(2, 2, 2, 2)`**. A core
   that crosses can therefore look *exactly* like a clean bulk core. Gate
   `C-14`.

**So no factoring signature can define the validity boundary in either
direction, and the rule stands on the pairing's definition alone.** This is the
check's correction, taken, and then made sharper than the check made it.

---

## N3 — THE UNIFORM VOLUME DIAL, and the two scales move in OPPOSITE directions

At `T = 16`, deep core `t0 = 3`, uniform `v = 4/5`, the exact monodromy
spectrum is

```
charpoly(W) = (31260675 z^2 - 302948719 z + 31260675)^2
            * (50327125 z^2 - 139773119 z + 50327125)^2
```

against Block 190's `v = 1` value `heavy^2 · light^2`. **The FORM is
preserved**: two palindromic quadratics, each squared. Gate `D-2` measures the
form and gate `D-1` the coefficients.

### The form is preserved, exactly

| statement | `v = 1` | `v = 4/5` | gate |
| --- | --- | --- | :---: |
| leading `=` constant (reciprocal) | `22569375`, `39529825` | `31260675`, `50327125` | `D-2` |
| discriminant `b^2 - 4ac` | `52545986939220736`, `5725088884359936` | `87869007137918461`, `9405246751925661` | `D-3` |
| discriminant factorisation | Block 190's | `7^2·13·23·37·101^2·577·27539`, `3^7·7^2·13·31·37·101^2·577` | `D-3` |
| `-b > 2a` (roots positive, not merely real) | yes, yes | yes, yes | `D-4` |
| multiplicity of each factor | `2`, `2` | `2`, `2` | `D-1` |

So the volume dial does **not** break reciprocity, does **not** break
positivity, and does **not** break the two-scale structure. **It moves the two
scales — and it moves them the opposite way.**

### The opposite motions, EXACT and rational

`2 cosh(theta) = -b/a` for a palindromic `a z^2 + b z + a`, so the motion of
each scale is an exact rational difference:

```
heavy:  302948719/31260675 - 233631106/22569375 = -2071568131893/3135706208125   < 0
light:  139773119/50327125 - 109432706/39529825 = +710938392957/79576897760125   > 0
```

Both are exact rationals with **opposite signs**, gated at `D-5` as values and
at `D-6` as signs. Since `acosh(x/2)` is strictly increasing for `x > 2` and
both traces exceed `2a` on both sides, **`theta_heavy` strictly DECREASES and
`theta_light` strictly INCREASES**. That is a theorem about these two rational
numbers, not an inference from decimals.

### The decimals, and the CORRECTED ratio

**THE EXACT TRACES ABOVE ARE PRIMARY. The decimals below are the block's ONE
numeric layer** — `evalf` at 40 digits of the exact expressions
`acosh((-b/a)/2)`, gated to ten decimal places at `D-7`. Nothing numeric is
ever fed back into a construction.

| quantity | `v = 1` | `v = 4/5` |
| --- | ---: | ---: |
| `theta_heavy` | `2.3276840296` | `2.2603806617` |
| `theta_light` | `0.8506775060` | `0.8553292810` |
| `theta_heavy / theta_light` | **`2.7362708113`** | **`2.6427023041`** |

**THE SOLVE'S QUOTED PAIR `2.7361 -> 2.6449` IS WITHDRAWN AND CORRECTED HERE AS
CONTENT.** The exact factors displayed above imply `2.7362708113 ->
2.6427023041`; the second decimal was a supervisor arithmetic slip and the
first was rounded from a truncation. The mutation `break_solve_ratio` asserts
the withdrawn `2.6449` and must fail. Gate `D-8`.

**AND WHAT THIS DOES NOT SHOW.** That the ratio moving means the dial is *not a
conformal or gauge rescaling* is a **reading** (`R1`). What is measured is that
two exact rational traces move in opposite directions under an imposed change
of an imposed parameter.

---

## N4 — THE LOCALIZED BUMP, and what it actually does

The profile is `v = 4/5` at the positive anchors `{3, 4}`, `v = 1` at the other
positive anchors, and on the image half the `P_4` image of the `thA_s(t) =
-1-t` partner. `T = 16` throughout.

### The covariance survives EXACTLY, and that is all it proves

```
nnz(Ps H Ps - H)   = 0,
nnz(Ps Q Ps - Q^T) = 0
```

for **both** bump profiles, gate `E-1`. **This is compatibility with the
reflection and is not an equivalence statement about `v(t)` profiles** —
see `N4g`.

### Palindromicity dies in EVERY irreducible factor, and it is proven exactly

| core | irreducible factors over `Q` | `leading != constant` |
| :---: | --- | :---: |
| `1` | `1345846680 z^2 - 3973376087 z + 1478415455` | ✓ |
| | `24349745880 z^2 - 72455211787 z + 27315109075` | ✓ |
| | `65582920234848542400 z^4 - 1482708604980552127920 z^3 + 8535510836512821008759 z^2 - 1754062292362811443250 z + 91505439094037734375` | ✓ |
| `3` | `573370050 z^2 - 1494466969 z + 531948700` | ✓ |
| | `706236550 z^2 - 1827879139 z + 617587500` | ✓ |
| | `114565459508949172500 z^4 - 2050729233157099637100 z^3 + 9367229822132458083989 z^2 - 1702027048070120587200 z + 78988021416996930000` | ✓ |
| `5` | `988245625 z^2 - 2738989093 z + 1007414244` | ✓ |
| | `12768133475 z^2 - 35396157503 z + 12528288900` | ✓ |
| | `28294075662319609375 z^4 - 513108970448968703250 z^3 + 2332339383938836349679 z^2 - 471493433933816742000 z + 24391099255638855600` | ✓ |

**Nine irreducible factors, nine exact integer inequalities `a != e`.** This is
the exact statement that `W` is no longer conjugate to `W^-1` at any probed
core — inside the bump (`t0 = 3`) *and* away from it (`t0 = 1`, `t0 = 5`).
Gates `E-2`, `E-3`. The quartics are irreducible with short certificates: `t0 =
1` mod `61`, `t0 = 3` and `t0 = 5` mod `11`. Gate `E-4`.

### Root reality, by exact discriminants and exact Sturm counts

| core | quadratic discriminants | quartic real-root count (Sturm) | spectrum |
| :---: | --- | :---: | --- |
| `1` | `7828835401653673969`, `2589293856456096289369` | `2` | 6 real, 1 conjugate pair |
| `3` | `1013417710566306961`, `1596490685498881321` | `0` | 4 real, 2 conjugate pairs |
| `5` | `3519770374790232649`, `613036506422939485009` | `2` | 6 real, 1 conjugate pair |

No root is estimated: the quadratic discriminants are exact positive integers
and the quartic counts are exact Sturm sequences over `Q`. Gate `E-5`.

### The response, and its COMPLETE complex inventory

Roots of the exact bumped polynomials are matched to the `v = 1` roots by the
minimum-total-distance perfect matching over all `8!` bijections; the matching
is a combinatorial **selection**, and every value reported is then computed at
40 digits from the exact algebraic roots.

| core | `nnz(W_bump - W_{v=1})` | max `|Delta lambda|` | the load-bearing displacement |
| :---: | ---: | ---: | --- |
| `1` | `64` | `0.9570159788` | `10.2415182723 -> 11.1984320472 + 0.0139861010 i` |
| `3` | `64` | `1.3978902241` | `10.2541656672 -> 8.8563197380 + 0.0111282045 i` |
| `5` | `64` | `0.0144654296` | `2.3412325139 -> 2.3556979435` |

The operator-level census is gated at `E-6` and the displacements at `E-7`.

**AND THE COMPLEX-PAIR DESCRIPTION IS COMPLETED, NOT REPEATED.** The solve
described the nonreal pairs as `|Im| ~ 0.002-0.003`. **That is true of two of
the four pairs and false of the other two**, and the complete inventory is:

| core | nonreal pairs `Re +/- |Im| i` |
| :---: | --- |
| `1` | `11.1984320472 +/- 0.0139861010 i` |
| `3` | `0.0937130291 +/- 0.0028458544 i` **and** `8.8563197380 +/- 0.0111282045 i` |
| `5` | `0.1046641456 +/- 0.0018623814 i` |

**AND THE COMPLETION IS A CENSUS, NOT AN ADJECTIVE.** Across both bump
positions there are **seven** nonreal pairs. Exactly **one** lies inside the
solve's band `|Im| in [0.002, 0.003]` — the `0.0028458544` pair at `t0 = 3`.
**Two** lie *below* it (`0.0018623814` at `t0 = 5` and `0.0009275825` under the
`{2,3}` bump) and **four** lie *above* it, two of those at four to five times
its width. The split `(below, inside, above) = (2, 1, 4)` is gated at `E-9`,
gate `E-7` gates the max shifts and gate `E-8` the **complete** inventory by
exact algebraic nonreality rather than by a threshold. The mutation
`break_small_imaginary_only` asserts that `0.002-0.003` is a complete
description and must fail.

### The ordering cross-check

At every core of `N3` and `N4`, the directly computed generalized polynomial
`det(z K_c - L_2) / det(K_c)` agrees **coefficientwise at exact zero residual**
with `charpoly(K_c^-1 L_2)`, so no result here depends on the inversion order
or on the core index convention. Gate `E-10`.

---

## N4a — HYBRIDIZATION, and the withdrawal of "the edge is the antenna"

**THE SOLVE SAID THE NEAR-EDGE RESPONSE IS BOUNDARY-MODE DOMINATED. THE
ADVERSARIAL CHECK REFUTED THAT AS STATED, AND THE REFUTATION IS CARRIED HERE AS
CONTENT.**

`U` (the two-site spatial shift) remains an exact Gram isometry and an exact
commutant **at the bumped core**:

```
nnz(U^T K_c U - K_c) = 0,     nnz([W, U]) = 0.
```

Gate `E-11`. It therefore still grades the spectrum — and the grading is
exactly what shows the dominance claim is not invariant:

| sector | `v = 1`, `t0 = 1` | bump `{3,4}`, `t0 = 1` |
| :---: | --- | --- |
| `U = +1` | `light^2` | the **two nonpalindromic quadratics** |
| `U = -1` | `heavy · near` — **two labelled rational factors** | **one irreducible nonpalindromic quartic** |

**The bump destroys the separate "heavy" and "boundary" factor labels: they
hybridize inside a single irreducible `U = -1` quartic.** Gate `E-12`.

And the shifts are **comparable**, not dominated:

```
baseline boundary large root  10.2415182723 -> the pair 11.1984320472 +/- 0.0139861010 i,  |Delta| = 0.9570159788
baseline heavy    large root  10.2541656672 -> the conjugate member of the SAME pair,      |Delta| = 0.9443699527
baseline separation of the two large roots                                                 = 0.0126473949
```

The two baseline large roots were already separated by only `0.0126473949`;
after the bump they are **one conjugate pair with a common real part**, so
assigning either post-bump member as uniquely "the boundary root" is **not
invariant**. The light-sector large roots move by `0.1744261414` and
`0.1914492821` — smaller, and not negligible. Gates `E-13`, `E-14`, and
`E-15` gates the comparability itself as the exact inequality
`| 0.9570159788 - 0.9443699527 | <= 0.0126473949`.

**WHAT SURVIVES, STATED AT ITS CORRECT STRENGTH.** The large response is
concentrated in the `U = -1` sector, which is the sector that contains the
boundary factor. **"Boundary-mode dominated" overstates what the data
identify**, and the mutation `break_edge_antenna` asserts it and must fail.

---

## N4b — THE SECOND BUMP POSITION, and the reach is position-dependent

The profile `v = 4/5` at the positive anchors `{2, 3}` is also exactly
`Ps`-covariant (`E-1`). Its response:

| core | `nnz(W_bump - W_{v=1})` | max matched shift | exact factor behaviour |
| :---: | ---: | ---: | --- |
| `1` | `64` | `0.6880075885` | two nonpalindromic quadratics + irreducible nonpalindromic quartic |
| `3` | `64` | `0.0737486236` | two nonpalindromic quadratics + irreducible nonpalindromic quartic |
| `5` | **`0`** | **`0` exactly** | **the complete `v = 1` factorization survives EXACTLY** |

At `t0 = 1` the large `U = -1` pair is `9.5662376816 +/- 0.0104655833 i`, so
relative to the two nearby baseline large roots the real shifts are about
`-0.688` and `-0.675` — **the sign is reversed** relative to the `{3,4}` bump
and the magnitude falls from `~0.957` to `~0.688`. At `t0 = 3` the maximum
response falls from `1.3978902241` to `0.0737486236`. At `t0 = 5` **the
operator itself, not merely its spectrum, is unchanged at exactly zero
entries.**

**CONCLUSION, AT ITS MEASURED STRENGTH.** Near-edge coupling is **generic
across these two bump positions** rather than a property of `{3,4}` — and
**magnitude, sign and spatial reach are strongly bump-position dependent**, with
an exact zero beyond range. Gates `E-16`, `E-17`.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

| word | what is **measured** | what is **not** derived |
| --- | --- | --- |
| **lapse** | `v`, the second argument of Block 105's `shear_hodge(c, v)`, a positive rational placed on anchors by hand | any lapse function; any ADM phase space in which it lives; any Hamiltonian constraint it multiplies; any gauge orbit; any quotient; any Dirac observable |
| **lapse physicality** | that changing `v`, uniformly or locally, changes the exact spectrum of `W` while `Ps`-covariance survives | that `v(t)` profiles are physically inequivalent; that these eigenvalue shifts are lapse excitations; that anything here cannot be gauged away, since **no gauge group is supplied to gauge it away with** |
| **boundary mode** | an exact rational, non-reciprocal quadratic factor of `charpoly(W)` at a seam-adjacent core | that it is an excitation localized on a physical surface; that a surface exists |
| **volume dial** | two exact rational traces moving in opposite directions | that the dial is not a conformal or gauge rescaling — that is `R1`, and this block has no gauge group to test it against |
| **transfer** | `W = K_c^-1 L_2`, a matrix product of blocks of `Q^-1` | reflection positivity; an OS Hilbert space; a self-adjoint generator; a semigroup — **and Block 190 refuted the naive transfer pairing on this very class** |

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within this imposed finite matrix construction, uniform and localized changes
> of the Hodge volume `v` alter the exact monodromy spectrum, while the
> specified reflection covariance `Ps H Ps = H`, `Ps Q Ps = Q^T` survives
> exactly.

**That is the whole of what is established.** Every stronger sentence in the
campaign's Phase-2 and Phase-3 wording — "the volume dial is PHYSICAL", "lapse
inhomogeneity is REAL physics on this class", "it cannot be gauged away" — is
carried into this note **as a reading and nowhere else**.

### Three further fences, all three self-imposed

- **`Ps`-COVARIANCE IS NOT AN EQUIVALENCE RELATION.** It says the profile is
  compatible with one reflection. Two profiles can both be `Ps`-covariant and
  be related by *anything at all*, including a symmetry this block never looked
  for. **The absence of a gauge group is what makes "cannot be gauged away"
  unavailable**, not the presence of a spectral difference.
- **TWO POSITIONS ARE NOT A SCAN.** `N4b` measures two bump positions. That
  near-edge coupling is *generic* is supported by two data points and is
  stated at exactly that strength.
- **THE WIDTHS STOP AT 20.** "Width-locked" means *at `T = 16` and `T = 20`*.
  Two widths agreeing is two widths agreeing.

### What IS derived, stated positively so the fence is not mistaken for a retreat

Six things, all exact: the **complete boundary-monodromy table** at every core
of two widths, with every entry the same polynomial at the same relative
position; the **exact non-reciprocity** of the boundary factors, with their
**surviving positivity**; the **exact coefficient reversal** between the near
and far seams; the **withdrawal of the factoring signature in both
directions**; the **opposite exact rational trace motions** under the uniform
dial; and the **exact loss of palindromicity in all fifteen moved irreducible
factors** under the localized bump, with an exact zero beyond its reach.

---

## READINGS — five of them, and each is a reading

**THE TWO-REGISTER RULE APPLIES: nothing below is measured, and nothing above
licenses any of it.**

- **(R1) THE VOLUME DIAL IS PHYSICAL — NOT A CONFORMAL OR GAUGE RESCALING.**
  That the two scales moving in *opposite* directions rules out a rescaling
  **IS A READING**. What is measured is `N3`. To rule out a gauge motion one
  needs a gauge group, and this block supplies none.
- **(R2) LOCALIZED LAPSE INHOMOGENEITY IS REAL PHYSICS ON THIS CLASS AND
  CANNOT BE GAUGED AWAY.** **IS A READING**, and the sharpest one in the
  block. What is measured is that a localized `v(t)` changes exact
  characteristic polynomials at every core it reaches while `Ps`-covariance
  survives.
- **(R3) THE BOUNDARY FACTOR IS A PHYSICAL EDGE MODE, AND ITS
  NON-RECIPROCITY IS "AN EDGE BREAKING `lambda -> 1/lambda` AS AN EDGE
  SHOULD".** **IS A READING.** What is measured is `a != c` for four exact
  integer triples.
- **(R4) THE MONODROMY SPECTRUM IS THE TRANSFER CONTENT OF THE
  CONSTRUCTION.** **IS A READING**, carried unchanged from Block 190 and
  **weakened** here rather than strengthened: the bump destroys reciprocity, so
  the `cosh` parametrisation that made the spectrum look like a transfer
  spectrum does not even survive a localized change of an imposed parameter.
- **(R5) THE BOUNDARY LAYER'S WIDTH-LOCK IS AN INFINITE-VOLUME STATEMENT.**
  **IS A READING.** Two widths is two widths.

**AND ONE THING RUNS IN THE OTHER DIRECTION, WHICH IS WORTH SAYING.** The
solve's most quotable line — *the edge mode is the bump's antenna* — is not
weakened here, it is **withdrawn**. The adversarial check refuted it as stated
and this note carries the refutation as content, with the replacing
measurement (`N4a`) gated by five separate gates. A reading that looked
strongest before this block is **gone** after it.

---

## CLAIM REGISTER — formulas, and the family that gates each

**MEASURED register.** Every row is an exact identity, an exact integer, an
exact rational, or a ten-decimal rounding of an exact algebraic object measured
by the runner; none is a summary.

| # | claim, as a formula | value | family |
| ---: | --- | --- | :---: |
| 1 | `shear_hodge(5/13, 1) - (diag(v, v g^-1, 1/v))|_{v=1}` | `0_4` entrywise | `C` |
| 2 | `shear_hodge(5/13, 4/5) - (diag(v, v g^-1, 1/v))|_{v=4/5}` | `0_4` entrywise | `C` |
| 3 | `(nnz(Ps H Ps - H), nnz(Ps Q Ps - Q^T))` for all four profiles | `(0, 0)` four times | `C` |
| 4 | `charpoly(W)` at `t0 = 1`, `T = 16` and `T = 20` | `heavy · light^2 · near` | `C` |
| 5 | `charpoly(W)` at the interior cores of both widths | `heavy^2 · light^2` | `C` |
| 6 | `charpoly(W)` at `t0 = T/2 - 4` | `heavy · light^2 · mirror` | `C` |
| 7 | `charpoly(W)` at `t0 = T/2 - 3` | `heavy · light^2 · second` | `C` |
| 8 | `charpoly(W)` at `t0 = T/2` | `heavy · light^2 · rev(second)` | `C` |
| 9 | multiplicity of `light` at all 14 tabulated cores | `2` fourteen times | `C` |
| 10 | multiplicity of `heavy` at the six layer cores | `1` six times | `C` |
| 11 | `near` | `43033320714375 z^2 - 445467467014578 z + 48554286398375` | `C` |
| 12 | `second` | `48554286398375 z^2 - 376762652339458 z + 35686537764375` | `C` |
| 13 | `a - c` for `near`, `mirror`, `second`, `rev(second)` | `-5520965684000`, `+5520965684000`, `+12867748634000`, `-12867748634000` — all `!= 0` | `C` |
| 14 | `b^2 - 4ac` for `near`/`mirror` and for `second`/`rev(second)` | `190083455453828589664707955584`, `135019158697151741387932171264` | `C` |
| 15 | their prime factorisations | `2^7·3^4·13·313·70619·96676423·659962871`, `2^10·13·313·32404681043299888780819` | `C` |
| 16 | `a > 0`, `-b > 0`, `c > 0` for all four boundary factors | true — **both roots real and positive** | `C` |
| 17 | `mirror = rev(near)` and `rev(second) = rev(second)` coefficientwise | exact | `C` |
| 18 | degree pattern at the touching cores `(16,5)`, `(20,7)` | `(2,2,2,2)` | `C` |
| 19 | degree pattern at the crossing cores `(16,6)`, `(16,7)`, `(20,8)`, `(20,9)` | `(2,2,4)` four times | `C` |
| 20 | crossing quartic irreducibility certificates | irreducible mod `11` at `T=16`, mod `67` at `T=20` | `C` |
| 21 | degree pattern at the crossing cores `(16,8)`, `(20,10)` | `(2,2,2,2)` — **the signature dies from below** | `C` |
| 22 | factoring behaviour **is** the validity signature | **`False`** — declared, gated; the rule is the pairing's definition | `C` |
| 23 | `charpoly(W)` at `T=16`, `t0=3`, uniform `v = 4/5` | `(31260675 z^2 - 302948719 z + 31260675)^2 (50327125 z^2 - 139773119 z + 50327125)^2` | `D` |
| 24 | leading `=` constant for both dial factors | true — palindromic survives the uniform dial | `D` |
| 25 | dial discriminants and factorisations | `87869007137918461 = 7^2·13·23·37·101^2·577·27539`, `9405246751925661 = 3^7·7^2·13·31·37·101^2·577` | `D` |
| 26 | `-b > 2a` for both dial factors | true, true | `D` |
| 27 | `302948719/31260675 - 233631106/22569375` | `-2071568131893/3135706208125 < 0` | `D` |
| 28 | `139773119/50327125 - 109432706/39529825` | `+710938392957/79576897760125 > 0` | `D` |
| 29 | `theta_heavy`, `theta_light` at `v = 1` and `v = 4/5`, ten decimals | `2.3276840296`/`0.8506775060` → `2.2603806617`/`0.8553292810` | `D` |
| 30 | `theta_heavy/theta_light` at `v = 1` and `v = 4/5`, ten decimals | **`2.7362708113` → `2.6427023041`** | `D` |
| 31 | the solve's quoted pair `2.7361 -> 2.6449` | **WITHDRAWN** — kept as a literal so `break_solve_ratio` is a gate | `D` |
| 32 | `(nnz(Ps H Ps - H), nnz(Ps Q Ps - Q^T))` for both bumps | `(0, 0)`, `(0, 0)` | `E` |
| 33 | the nine `{3,4}` irreducible factors at `t0 = 1, 3, 5` | the table in `N4` | `E` |
| 34 | the six `{2,3}` irreducible factors at `t0 = 1, 3` and the survivor at `t0 = 5` | the table in `N4b` | `E` |
| 35 | `#{ moved irreducible factors with leading != constant }` | `15` of `15`, zero exceptions | `E` |
| 36 | bumped quartic irreducibility certificates | mod `61`, `11`, `11` (`{3,4}`); mod `19`, `7` (`{2,3}`) | `E` |
| 37 | bumped quadratic discriminants, all five moved cores | the tables in `N4`, `N4b` | `E` |
| 38 | quartic Sturm real-root counts | `2`, `0`, `2` (`{3,4}`); `2`, `0` (`{2,3}`) | `E` |
| 39 | `nnz(W_bump - W_{v=1})` at the six probed pairs | `64,64,64` (`{3,4}`); `64,64,` **`0`** (`{2,3}`) | `E` |
| 40 | max matched `|Delta lambda|`, ten decimals | `0.9570159788`, `1.3978902241`, `0.0144654296`; `0.6880075885`, `0.0737486236`, `0` | `E` |
| 41 | the complete nonreal inventory, `(Re, |Im|)` at ten decimals | the tables in `N4`, `N4b` — **seven pairs** | `E` |
| 42 | `(below, inside, above)` the band `|Im| in [0.002, 0.003]` | `(2, 1, 4)` of `7` | `E` |
| 43 | `|Im| ~ 0.002-0.003` is a **complete** description | **`False`** — declared, gated | `E` |
| 44 | `det(z K_c - L_2)/det(K_c)` vs `charpoly(K_c^-1 L_2)` at seven cores | equal, residual `0` | `E` |
| 45 | `nnz(U^T K_c U - K_c)`, `nnz([W,U])` at the **bumped** `t0 = 1` | `0`, `0` | `E` |
| 46 | baseline `U = ±1` sector factorisations at `t0 = 1` | `light^2`; `heavy · near` | `E` |
| 47 | bumped `U = ±1` sector factorisations at `t0 = 1` | the two nonpalindromic quadratics; **one irreducible quartic** | `E` |
| 48 | boundary and bulk-heavy large-root displacements, ten decimals | `0.9570159788`, `0.9443699527` | `E` |
| 49 | baseline separation of those two roots, ten decimals | `0.0126473949` | `E` |
| 50 | light-sector large-root displacements, ten decimals | `0.1744261414`, `0.1914492821` | `E` |
| 51 | the two displacements differ by less than the baseline separation | **`True`** — comparable, hence **hybridized and not dominated** | `E` |
| 52 | `sp.nsimplify` occurrences in the runner's own source | `0` | `F` |

**READING register.** Nothing below is measured, and nothing above licenses any
of it.

| # | reading | status |
| ---: | --- | --- |
| R1 | the volume dial is physical, not a conformal/gauge rescaling | **READING** — no gauge group is supplied |
| R2 | localized lapse inhomogeneity is real physics and cannot be gauged away | **READING** — `N4g`, ten structures not supplied |
| R3 | the boundary factor is a physical edge mode | **READING** — it is an exact rational factor |
| R4 | the monodromy spectrum is the transfer content | **READING** — carried from Block 190 and *weakened* here |
| R5 | the two-width lock is an infinite-volume statement | **READING** |
| — | "the edge mode is the bump's antenna" | **WITHDRAWN**, not downgraded — refuted as stated, see `N4a` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

**EVERY FORK WAS MEASURED AT ITS FORK, SO NOTHING WRONG LEFT THE SOLVE — AND
THE FOUR THAT DID GET OUT ARE CORRECTED HERE AS CONTENT.**

1. **THE DEEP CORES WERE SCANNED FIRST AND SAID NOTHING — WHICH WAS THE POINT.**
   `t0 = 2..5` at `T = 20` reproduce Block 190's spectrum exactly. The
   boundary only appears when the cores that Block 190 never computed are
   computed.
2. **`t0 = 6` AT `T = 16` WAS PROBED AS A BULK CORE AND IS NOT ONE — CAUGHT IN
   SOLVE.** Its `L_2` reaches `{8, 9}` and crosses the fixed slice. Its values
   were discarded before they entered any claim, and the touch/cross rule was
   written because of it.
3. **THE NON-FACTORING SIGNATURE WAS ASSERTED AND IS FALSE — TWICE.** The solve
   said crossing cores are detectable by failing to factor over `Q`. The
   adversarial check found they factor `(2,2,4)`; **this note then found a
   crossing core that factors completely into quadratics**, which kills the
   signature from the other side as well. The rule now rests on the pairing's
   definition alone.
4. **A RATIO WAS QUOTED FROM DECIMALS INSTEAD OF FROM THE EXACT FACTORS —
   `2.6449` WAS AN ARITHMETIC SLIP.** The exact factors were right in the solve
   and the decimal derived from them was wrong. The correction is `2.7362708113
   -> 2.6427023041`, and the withdrawn value is now a literal in the runner so
   the correction is a gate.
5. **THE COMPLEX PAIRS WERE DESCRIBED FROM TWO EXAMPLES.** `|Im| ~
   0.002-0.003` was read off two pairs and stated as if it described all of
   them. Of the seven measured pairs it captures **one**. The inventory is now
   complete and its band split is gated.
6. **"THE EDGE MODE IS THE BUMP'S ANTENNA" WAS THE BEST SENTENCE IN THE SOLVE
   AND IT IS WITHDRAWN.** It came from noticing a large shift at `t0 = 1` and
   attributing it to the boundary factor. The `U`-grading shows the boundary
   and heavy factors **merge**, and the two displacements agree to within less
   than the baseline separation of the roots they move. **The mechanism that
   produced the sentence was pattern-matching on a label that the bump
   destroys.**
7. **ONLY TWO BUMP POSITIONS WERE RUN, AND THAT LIMIT IS STATED RATHER THAN
   HIDDEN.** The `{2,3}` probe was added *because* one position cannot
   distinguish "generic near-edge coupling" from "a property of `{3,4}`". It
   showed genericity **and** strong position dependence, which is two findings
   and not one.

---

## N5 — the fence

```
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE HEADLINE WORD IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY (the staggered Dirac-Kahler carrier on Z_T x Z_4 for even T with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13), at widths T = 16 and T = 20), THE VOLUME PROFILE (a map v from the positive anchors {0..T/2-1} to the positive rationals, placed as B(c, v(t)) for t < T/2 and as the P_4 image of the block of its thA_s(t) = -1-t partner for t >= T/2, assembled by the same quarter-weighted four-corner cell average and reducing to Block 190's rule IDENTICALLY at any uniform profile) -- THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT -- THE FOUR PROBED PROFILES (uniform v = 1, uniform v = 4/5, and the LOCALIZED bumps v = 4/5 on the positive anchors {3,4} and on {2,3}), THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE SINGLE FIXTURE (9/20, 5/13) AND THE SINGLE BUMP AMPLITUDE 4/5, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. LAPSE PHYSICALITY IS A READING AND IS NOT ESTABLISHED BY ANYTHING HERE: v is the IMPOSED Block 105 Hodge-volume parameter, and this block supplies NO lapse variable in an ADM phase space, NO Hamiltonian constraint, NO gauge orbit, NO quotient, NO Dirac observable and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, UNIFORM AND LOCALIZED CHANGES OF THE HODGE VOLUME ALTER THE EXACT MONODROMY SPECTRUM WHILE THE SPECIFIED REFLECTION COVARIANCE SURVIVES EXACTLY. Ps-COVARIANCE DOES NOT DECIDE PHYSICAL EQUIVALENCE: Ps H Ps = H and Ps Q Ps = Q^T at ZERO for every profile proves COMPATIBILITY WITH ONE REFLECTION and does NOT prove that two v(t) profiles are physically inequivalent. THE PHYSICAL VOLUME DIAL IS A READING. THE PHYSICAL BOUNDARY MODE IS A READING: 'boundary mode' NAMES AN EXACT RATIONAL FACTOR at a seam-adjacent core. W IS NOT A TRANSFER OPERATOR: Block 190 refuted the naive OS transfer pairing on this class with six exact witnesses and NOTHING HERE REPAIRS IT. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NO GENERALITY IS CLAIMED: ONE fixture, TWO widths, FOUR profiles, ONE bump amplitude, and NOTHING about the infinite-width limit. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.
per_site: THE CONSTRUCTION CONTROL IS THE VOLUME LAW ITSELF, DISPLAYED RATHER THAN DESCRIBED. Block 190 displayed the landed shear block at the PINNED volume v = 1; this block needs v as a VARIABLE, so the LAW is displayed: shear_hodge(c, v) = diag(v, v g(c)^-1, 1/v) with g(c) = [[1,c],[c,1]], which at c = 5/13 is diag(1, 169/144, 169/144, 1) with (1,2) = (2,1) = -65/144 at v = 1 -- BLOCK 190's PINNED MATRIX -- and diag(4/5, 169/180, 169/180, 5/4) with (1,2) = (2,1) = -13/36 at v = 4/5. BOTH displayed matrices are gated ENTRYWISE against b128.block105.shear_hodge at ZERO residual, thirty-two numbers in all. AND EVERY PROFILE IS COVARIANT AT ZERO: nnz(Ps H Ps - H) = 0 and nnz(Ps Q Ps - Q^T) = 0 for uniform v = 1, uniform v = 4/5, the {3,4} bump AND the {2,3} bump -- which is COMPATIBILITY WITH THE REFLECTION AND NOT AN EQUIVALENCE STATEMENT. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's zeros, counts, signs, discriminants or coefficient vectors could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate F.
per_mode: THE BOUNDARY MONODROMY IS SCANNED AT EVERY CORE OF TWO WIDTHS AND THE LAYER IS POSITIONALLY WIDTH-LOCKED. With heavy = 22569375 z^2 - 233631106 z + 22569375, light = 39529825 z^2 - 109432706 z + 39529825, near = 43033320714375 z^2 - 445467467014578 z + 48554286398375, mirror = rev(near), second = 48554286398375 z^2 - 376762652339458 z + 35686537764375 and rev(second): charpoly(W) = heavy*light^2*near at t0 = 1, heavy^2*light^2 at the interior cores, heavy*light^2*mirror at t0 = T/2-4, heavy*light^2*second at t0 = T/2-3 and heavy*light^2*rev(second) at t0 = T/2 -- THE SAME POLYNOMIAL AT THE SAME RELATIVE POSITION AT BOTH T = 16 AND T = 20. THE LIGHT PAIR IS BOUNDARY-RIGID: light^2 divides charpoly(W) with multiplicity EXACTLY TWO at every tabulated core at both widths, so the light mode does not see the boundary. THE HEAVY SECTOR LOSES EXACTLY ONE COPY at each layer core, so the layer is MODE-SELECTIVE. THE BOUNDARY FACTORS ARE POSITIVE AND NON-RECIPROCAL, EXACTLY: near - its reversal has a - c = -5520965684000 and mirror +5520965684000, second +12867748634000 and rev(second) -12867748634000, all NONZERO, which is the exact statement that the seam breaks lambda -> 1/lambda; and the discriminants 190083455453828589664707955584 = 2^7*3^4*13*313*70619*96676423*659962871 and 135019158697151741387932171264 = 2^10*13*313*32404681043299888780819 are POSITIVE with a > 0, -b > 0 and c > 0, which is the exact statement that both roots are REAL AND POSITIVE. POSITIVITY SURVIVES AT THE SEAM; RECIPROCITY DOES NOT. AND THE NEAR/FAR REVERSAL IS EXACT COEFFICIENT FOR COEFFICIENT: mirror(z) = rev(near)(z) and rev(second) is the reversal of second, at BOTH widths.
per_block: THE VALIDITY BOUNDARY IS A RULE ABOUT THE PAIRING AND NOT ABOUT FACTORING, AND THE ADVERSARIAL CHECK'S CORRECTION IS CARRIED AS CONTENT AND THEN STRENGTHENED AGAINST THIS BLOCK'S OWN SOLVE. L_2 reads G at times {t0+2, t0+3}: t0+3 < T/2 is interior, t0+3 = T/2 TOUCHES the fixed slice and is ADMISSIBLE, t0+3 > T/2 CROSSES into the image half and is NOT A BULK OBJECT -- verified at both widths, T = 20 t0 = 7 and T = 16 t0 = 5 touching and factoring exactly as the table says, T = 20 t0 = 8 and T = 16 t0 = 6 crossing. THE SOLVE'S 'NON-FACTORING OVER Q' SIGNATURE IS WITHDRAWN AND IS FALSE IN BOTH DIRECTIONS, MEASURED IN BOTH: crossing cores at t0 = T/2-2 and T/2-1 DO factor over Q, with degree pattern (2,2,4) -- two rational quadratics and ONE IRREDUCIBLE RATIONAL QUARTIC, certified irreducible modulo 11 at T = 16 and modulo 67 at T = 20 and therefore over Q by Gauss's lemma -- so the true signature is FAILURE TO SPLIT COMPLETELY INTO RATIONAL QUADRATICS and never irreducibility; AND the crossing core at t0 = T/2 factors COMPLETELY into rational quadratics as heavy*light^2*rev(second), so a CROSSING core can look EXACTLY like a clean bulk core. NO FACTORING SIGNATURE CAN DEFINE THE VALIDITY BOUNDARY IN EITHER DIRECTION, AND THE RULE STANDS ON THE PAIRING'S DEFINITION ALONE.
lattice_wide: THE UNIFORM VOLUME DIAL PRESERVES THE FORM AND MOVES THE TWO SCALES IN OPPOSITE DIRECTIONS, AND THE SOLVE'S RATIO PAIR IS CORRECTED AS CONTENT. At T = 16, t0 = 3, uniform v = 4/5 the exact spectrum is (31260675 z^2 - 302948719 z + 31260675)^2 (50327125 z^2 - 139773119 z + 50327125)^2: both factors PALINDROMIC and SQUARED, discriminants 87869007137918461 = 7^2*13*23*37*101^2*577*27539 and 9405246751925661 = 3^7*7^2*13*31*37*101^2*577 both POSITIVE, both traces above twice the leading coefficient, so reciprocity, positivity and the two-scale structure ALL SURVIVE. THE TWO EXACT RATIONAL TRACE MOTIONS HAVE OPPOSITE SIGNS: 302948719/31260675 - 233631106/22569375 = -2071568131893/3135706208125 < 0 and 139773119/50327125 - 109432706/39529825 = +710938392957/79576897760125 > 0, and since acosh(x/2) is strictly increasing for x > 2 the heavy rapidity STRICTLY DECREASES and the light one STRICTLY INCREASES -- a theorem about two rational numbers and not an inference from decimals. THE EXACT TRACES ARE PRIMARY AND THE DECIMALS ARE THIS BLOCK'S ONE NUMERIC LAYER, evalf of exact acosh expressions at 40 digits gated to TEN places: theta_heavy 2.3276840296 -> 2.2603806617, theta_light 0.8506775060 -> 0.8553292810, and the RATIO 2.7362708113 -> 2.6427023041. THE SOLVE'S QUOTED PAIR 2.7361 -> 2.6449 IS WITHDRAWN AND CORRECTED HERE AS CONTENT, with the withdrawn value kept as a literal so that break_solve_ratio is a GATE and not a sentence. THAT THE RATIO MOVING MEANS THE DIAL IS NOT A CONFORMAL OR GAUGE RESCALING IS A READING.
per_scope: THE LOCALIZED BUMP KILLS PALINDROMICITY EVERYWHERE IT REACHES, AND BOUNDARY-MODE DOMINANCE IS REFUTED AND REPLACED BY MEASURED HYBRIDIZATION. With v = 4/5 on the positive anchors {3,4}, Ps H Ps = H and Ps Q Ps = Q^T at ZERO, and at t0 = 1, 3 AND 5 -- inside the bump AND away from it -- every one of the NINE irreducible factors has leading != constant as an exact integer inequality, so W is no longer conjugate to its inverse at ANY probed core; the quartics are certified irreducible modulo 61, 11 and 11. Root reality is decided by EXACT quadratic discriminants and EXACT Sturm counts and never estimated: 6 real plus one conjugate pair at t0 = 1, 4 real plus two pairs at t0 = 3, 6 real plus one pair at t0 = 5. THE COMPLEX-PAIR DESCRIPTION IS COMPLETED RATHER THAN REPEATED AND THE COMPLETION IS A CENSUS AND NOT AN ADJECTIVE: of the SEVEN nonreal pairs measured across the two bump positions, TWO lie BELOW the solve's |Im| ~ 0.002-0.003 band, EXACTLY ONE lies INSIDE it and FOUR lie ABOVE it, and the complete inventory carries 11.1984320472 +/- 0.0139861010 i at t0 = 1 and 8.8563197380 +/- 0.0111282045 i at t0 = 3, four to five times the quoted band. THE MAX MATCHED DISPLACEMENTS ARE 0.9570159788 at t0 = 1, 1.3978902241 at t0 = 3 and 0.0144654296 at t0 = 5. AND THE CHECK'S P1 IS FOLDED: U remains an exact Gram isometry and an exact commutant AT THE BUMPED CORE, and the grading is exactly what refutes the dominance claim -- the baseline U = -1 sector is heavy TIMES near, two labelled rational factors, and after the bump it is ONE IRREDUCIBLE NONPALINDROMIC QUARTIC, so the two factors HYBRIDIZE; the two baseline large roots were already only 0.0126473949 apart and become ONE CONJUGATE PAIR WITH A COMMON REAL PART, with matched displacements 0.9570159788 and 0.9443699527 -- COMPARABLE AND NOT DOMINATED -- so assigning either post-bump member as uniquely 'the boundary root' is NOT INVARIANT and 'the edge mode is the bump's antenna' IS WITHDRAWN. AND THE REACH IS BUMP-POSITION DEPENDENT: the {2,3} profile is also exactly Ps-covariant, its t0 = 1 response REVERSES SIGN and falls to 0.6880075885, its t0 = 3 response falls from 1.3978902241 to 0.0737486236, and at t0 = 5 THE OPERATOR ITSELF is unchanged at EXACTLY ZERO ENTRIES. NEAR-EDGE COUPLING IS GENERIC ACROSS THESE TWO POSITIONS; MAGNITUDE, SIGN AND REACH ARE NOT.
RESULT: A MODE-SELECTIVE, POSITIONALLY WIDTH-LOCKED, NON-RECIPROCAL BOUNDARY LAYER OF THE UNIT-CELL MONODROMY IS COMPUTED IN CLOSED FORM AT EVERY CORE OF TWO WIDTHS, THE HODGE VOLUME IS SHOWN TO MOVE THE TWO EXACT SCALES IN OPPOSITE DIRECTIONS, AND A LOCALIZED VOLUME BUMP IS SHOWN TO DESTROY PALINDROMICITY IN EVERY IRREDUCIBLE FACTOR IT REACHES -- AND NOT ONE LINE OF IT IS A LAPSE, A CONSTRAINT, A GAUGE ORBIT OR A PHYSICAL TRANSFER OPERATOR. The volume law is displayed and gated entrywise at both probed volumes; every profile is Ps-covariant at zero; the light pair is boundary-rigid and the heavy sector loses exactly one copy at each layer core; the boundary factors are positive and exactly non-reciprocal with factored discriminants and an exact near/far coefficient reversal; the touch/cross rule is verified at both widths and the factoring signature is withdrawn in BOTH directions; the uniform dial preserves palindromicity, positivity and the two-scale structure while moving the two exact rational traces oppositely; the corrected ratio pair is 2.7362708113 -> 2.6427023041; the bump breaks palindromicity in fifteen irreducible factors across five moved cores, with exact reality certificates and a COMPLETE complex-pair inventory; and boundary-mode dominance is REFUTED and replaced by hybridization with comparable displacements. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.
DECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-190 STAND EXACTLY AS LANDED. BLOCK 190 IS NOT CORRECTED: its deep-core spectrum is reproduced here digit-for-digit as the control at T = 16 t0 = 3 and at T = 20 t0 = 2,3,4,5, and this block only computes the cores it did not. BLOCK 188 IS NEITHER CORRECTED NOR CONTRADICTED and the wrap-edge object remains a DISCLOSED VARIANT of theirs. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE FIXTURE, TWO WIDTHS, ONE BUMP AMPLITUDE AND NO WINDOW; the widths stop at 20 so nothing is proven about the infinite-width limit; the bump is probed at TWO positions and TWO positions are not a scan; and the block's own solve language is corrected in four places rather than papered over. FOUR ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C2 NARROWING, that crossing cores DO factor as (2,2,4) so the non-factoring signature is dropped and the touch/cross rule rests on the pairing's definition -- strengthened here by the measured all-quadratic crossing core at t0 = T/2; the C3 NUMERICAL CORRECTION, that the ratio pair is 2.7362708113 -> 2.6427023041 and not 2.7361 -> 2.6449; the C4 COMPLETION, that the complex-pair band 0.002-0.003 captures EXACTLY ONE of the SEVEN measured pairs -- two lie below it and four above -- with additional pairs at |Im| ~ 0.0111 and ~ 0.0140; and the P1 REFUTATION, that the near-edge response is NOT boundary-mode dominated but a hybridization of the boundary and bulk-heavy factors inside one irreducible U = -1 quartic with comparable displacements. AND THE CHECK'S PHYSICALITY FENCE IS ADOPTED AS THE BLOCK'S OWN HEADLINE: the package establishes HODGE-VOLUME SPECTRAL SENSITIVITY, and LAPSE PHYSICALITY STAYS A READING. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE BOUNDARY-LAYER SOLVE (block 191 candidate), PHASE 4 and B191 CHECK VERDICT anchors.
TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

- **THE BOUNDARY-MONODROMY TABLE IS COMPLETE AT TWO WIDTHS.** Every core of
  `T = 16` and `T = 20` is computed, not sampled, and every entry is the same
  polynomial at the same relative position. There is no core left to probe at
  these widths.
- **THE FACTORING SIGNATURE IS CLOSED, NEGATIVE, IN BOTH DIRECTIONS.**
  Crossing cores factor `(2,2,4)` at `T/2-2` and `T/2-1` and factor completely
  into quadratics at `T/2`. No refinement of "does it factor" can define the
  validity boundary, and the pairing's definition already does.
- **"BOUNDARY-MODE DOMINANCE" IS CLOSED, NEGATIVE, WITH A MECHANISM.** The
  `U`-grading is exact, the merge into one irreducible quartic is exact, and
  the two displacements are measured. This is not stuck; it is answered
  against the solve.

### REOPEN IF

- **a gauge group is actually supplied on this class.** Only then does "cannot
  be gauged away" become a question with an answer, and only then does `R2`
  stop being a reading. **This is the single item that would move the lapse
  leg**, and no amount of further spectral sensitivity substitutes for it.
- **a third bump position, or a second amplitude, is run.** Two positions
  established genericity *and* position dependence; a third would say which of
  those is the robust statement.
- **a wider carrier moves any tabulated value.** The layer is locked at `T =
  16` and `T = 20` and nowhere else.
- **the boundary quadratic is derived rather than measured.** `near` and
  `second` are exact integers with no closed form here; a formula for them in
  terms of `(m, c)` would turn a table into a theorem.
- **an OS reconstruction is built on the unit-cell monodromy.** Block 190's
  open leg, untouched here, and the only thing that would make `W`'s spectrum a
  transfer spectrum.
- **the non-reciprocity is connected to a boundary condition.** `a != c` is
  measured; *which* boundary condition it encodes is not asked here.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 189's #25 — BLOCK 190 RESTARTED ITS LOCAL
NUMBERING AND THIS BLOCK RESUMES THE CUMULATIVE ONE. NO CORRECTION IS LANDED
BY THIS BLOCK AGAINST ANY LANDED NUMBER. Four of the
adversarial check's findings are carried as CONTENT rather than as errata, two
further items correct this block's own solve language, and every one of them is
a declared constant with a gate and a mutation.**

26. **THE C2 NARROWING — THE NON-FACTORING SIGNATURE IS DROPPED.** The solve
    said boundary-crossing cores are detectable because their `W` does not
    factor over `Q`. The check measured `(2,2,4)` with two rational quadratics
    and one irreducible rational quartic at `T = 16, t0 = 6` and `T = 20,
    t0 = 8`. **The signature is withdrawn and the touch/cross rule now stands
    on the pairing's definition.** `FACTORING_IS_A_VALIDITY_SIGNATURE = False`
    is a declared constant, gates `C-12`–`C-15`, mutation
    `break_crossing_signature`.
27. **AND THIS BLOCK STRENGTHENS THAT NARROWING AGAINST ITSELF.** At `t0 = T/2`
    — a **crossing** core at both widths — `charpoly(W)` factors *completely*
    into rational quadratics, `heavy · light^2 · rev(second)`. A crossing core
    can therefore look exactly like a clean bulk core, so the signature fails
    from **below** as well as from above. Gate `C-14`, mutation
    `break_signature_from_below`. **The check found one direction; the scan
    found the other.**
28. **THE C3 NUMERICAL CORRECTION — THE RATIO PAIR.** The solve quoted
    `2.7361 -> 2.6449`. The exact factors it displayed imply `2.7362708113 ->
    2.6427023041`; `2.6449` was an arithmetic slip. The exact traces are
    primary and gated at `D-5`/`D-6`; the decimals are gated at `D-7`/`D-8`;
    the withdrawn value is a literal in the runner so that
    `break_solve_ratio` is a gate and not a sentence.
29. **THE C4 COMPLETION — THE COMPLEX-PAIR BAND.** The solve's `|Im| ~
    0.002-0.003` was read off two pairs. Of the **seven** pairs measured across
    both bump positions it captures **one**; two lie below the band and four
    above, two of those at four to five times its width. The complete
    inventory and the `(2, 1, 4)` split are gated at `E-8`/`E-9`, mutation
    `break_small_imaginary_only`.
30. **THE P1 REFUTATION — "THE EDGE MODE IS THE BUMP'S ANTENNA" IS WITHDRAWN,
    NOT SOFTENED.** The check refuted boundary-mode dominance as stated. This
    note carries the refutation as content and supplies the replacing
    measurement: `U` remains an exact isometry and commutant at the bumped
    core; the baseline `U = -1` sector's two labelled factors **merge into one
    irreducible quartic**; and the two large-root displacements,
    `0.9570159788` and `0.9443699527`, differ by less than the
    `0.0126473949` baseline separation of the very roots they move. Gates
    `E-11`–`E-15`, mutations `claim_edge_dominance` and `break_edge_antenna`.
31. **THE PHYSICALITY FENCE IS ADOPTED AS THE BLOCK'S OWN HEADLINE, AND IT IS
    THE MOST IMPORTANT ITEM IN THIS LIST.** The check's verdict was that the
    package establishes **Hodge-volume spectral sensitivity** and that **lapse
    physicality is not established**. This note's title, its `N0`, its `N4g`,
    its `N5` fence and seven declared constants in family `B` all say so, and
    the campaign's Phase-2/Phase-3 wording is carried only as readings `R1` and
    `R2`. Gates `B-2`–`B-7`, mutations `claim_lapse_physicality`,
    `claim_volume_dial_physical`, `claim_boundary_mode_physical`,
    `claim_profiles_inequivalent` and `claim_transfer_operator`.
32. **AND ONE IN-SOLVE CATCH THAT NEVER BECAME A CORRECTION, RECORDED BECAUSE
    THE MECHANISM IS WORTH KEEPING.** The `t0 = 6` probe at `T = 16` was run
    as a bulk core and is a **crossing** core. It was caught inside the solve,
    its values were discarded before entering any claim, and the touch/cross
    rule of `N2a` was written because of it. **The fork was measured at the
    fork.**

### The adversarial check

Verdict carried as **CONFIRMED WITH MATERIAL NARROWINGS AND TWO NUMERICAL
CORRECTIONS** (`sol xhigh`, cross-model, an independent compact rebuild from the
landed Block 190 note rather than an invocation of its runner; findings
preserved at `b191_check_findings.md`).

**CONFIRMED EXACTLY, ON AN INDEPENDENT RECONSTRUCTION.** The `P3` deep control
at `T = 20, t0 = 3,4,5` and `T = 16, t0 = 3`; the complete `C1` boundary table
coefficient for coefficient, including the near/far reversal and the distinct
`t0 = 7` factor; the `C2` geometric touch/cross rule at both widths; the `C3`
exact `v = 4/5` spectrum and the direction of both trace motions; the `C4`
exact `Ps`-covariance residuals, all nine irreducible factors, the exact
non-palindromicity of every one of them, and all three max shifts.

**NARROWED OR CORRECTED, ALL FOUR NOW GATES RATHER THAN PROSE:** the `C2`
factoring wording (item 26, strengthened by item 27); the `C3` decimals (item
28); the `C4` complex-pair band (item 29); and `P1`'s boundary-mode dominance
(item 30). **The check's `P2` second-bump probe is rebuilt here in full**,
including its exact zero at `t0 = 5`, and its physicality fence is adopted as
this block's headline (item 31). **No sentinel remains anywhere in the runner
or in this note.**

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–190 number **stands as landed**.
Block 190's deep spectrum is reproduced here digit-for-digit at `T = 16,
t0 = 3` and at `T = 20, t0 = 2,3,4,5` as this block's control; this block only
computes the cores it did not. Block 188's landed `T = 8` object is untouched
and the wrap-edge family remains a **disclosed variant** of it.

### Reproduction

```
python3 scripts/admissibility_dirac_kahler_boundary_mode_volume_sensitivity_2026_08_25.py
python3 ... --list-mutations
python3 ... --mutation break_edge_antenna
```

Exact throughout: sympy `Rational`/`Integer` only, `DomainMatrix` over `QQ` for
the five exact inverses (one `80 x 80` and four `64 x 64`, each built once and
shared), exact `factor_list` over `Q` for every polynomial, exact `Sturm`
counts and exact discriminants for every reality statement, finite-field
irreducibility certificates for every quartic, and **no float, no tolerance and
no `sp.nsimplify` anywhere** — the last of which is *measured* in the runner's
own source by gate `F-3` rather than promised. The single numeric layer is
`evalf` at 40 digits of exact algebraic objects, gated to ten decimal places,
and nothing numeric is ever fed back into a construction.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE BOUNDARY-LAYER SOLVE
(block 191 candidate)**, **PHASE 4** and **B191 CHECK VERDICT** anchors.
