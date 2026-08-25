---
title: "Admissibility — Dirac-Kähler Width Family: The Transfer Refutation, The Locality Theorem, And The Unit-Cell Monodromy"
date: 2026-08-25
block: 190
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py
parent_ref: origin/physics-loop/toe-axiom-closure-block189-site-gauge-quotient-20260824
parent_commit: 996e516600ca9d0f679a6f3ab554036068205d2f
current_main: b11811704efa98a12272d572f666e530a807f6c1
registered: 0
adopted: 0
axiom_movement: none
---

# The Width Family, Its Transfer Refutation, Its Locality Theorem, And The Unit-Cell Monodromy — with dispersion, mass scales, the physical time step and transfer positivity fenced as readings

**One sentence.** On a **disclosed variant** of Block 188's site construction —
the same staggered Dirac-Kähler carrier on `Z_T x Z_4` at the same fixture
`(m, c) = (9/20, 5/13)`, but with the antiperiodic temporal sign carried on the
**wrap edge** `t = T-1` instead of at `t = 3` — the naive OS transfer pairing is
**refuted with six exact core witnesses**, the step operator `V = K_c^-1 L_1` is
measured to be a **local** object (width-invariant, position-homogeneous, with a
finite-range boundary layer at **both** seams), and the primitive unit-cell
monodromy `W = K_c^-1 L_2` is computed exactly and **proven spectrally
positive** — and not one line of it is gravity.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Five imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE OBJECT IS A DISCLOSED VARIANT AND THAT IS SAID FIRST.** Block 188's landed
`T = 8` object carries the antiperiodic temporal sign at `t = 3`. This family
carries it at `t = T-1`, because the width generalisation needs a rule that
makes sense at every even `T` and "the far reflection seam" and "the wrap edge"
are the same slice only when `T = 8`. **The fork is measured as a pair rather
than argued:**

| sign placement | `nnz(Q - Q^T)` at `T = 8` | `Ps Q Ps - Q^T` | `det(K[:1,:1])` on the `{1,2}` core |
| --- | ---: | ---: | --- |
| `w(3)` — **Block 188's landed placement** | **144** — their own landed number | `0` | `250811603701251182926764176363850176714557920003089965221914456500/666495028860293624372300921944800123265476111209829299156533225479` — **their landed minor, digit-for-digit** |
| `w(T-1)` — **this block's wrap convention** | **160** | `0` | `6874991398831399275340647912337474750/18307834037130787420472860378633197921` — **a different number** |

Both placements are `Ps`-covariant, so both are admissible OS constructions.
**They are not the same matrix, and this runner measures the difference instead
of asserting the sameness.** Block 188 is neither corrected nor contradicted.

**AND FOUR WORDS ARE FENCED BEFORE ANY NUMBER IS READ.**

- **DISPERSION IS A READING.** What is measured is the characteristic polynomial
  of a finite matrix in two momentum sectors. That `E(0)` and `E(pi)` are the
  energies of a propagating mode **is not derived anywhere**.
- **MASS SCALES ARE A READING.** `theta_1` and `theta_2` are logarithms of
  eigenvalues with exact rational traces. **No mass, no continuum limit and no
  unit is supplied by this block.**
- **THE PHYSICAL TIME STEP IS A READING.** That the two-slice unit cell is *the*
  time step of a theory is a statement about the staggering of *this* carrier,
  not a theorem.
- **TRANSFER POSITIVITY IS A READING.** The positivity of this `8 x 8` spectrum
  is **proven**, exactly, in `N4b`. The Osterwalder–Schrader reconstruction that
  would make it *mean* transfer positivity **is not performed**.

**NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED**, so the absence is a
count and not a mood: lapse function; shift vector; Hamiltonian constraint;
momentum/diffeomorphism constraint; first-class constraint algebra; Dirac
closure; ADM phase space / history transporter; OS reconstruction of a transfer
operator; any continuum limit, any unit and any mass.

**NO GENERALITY IS CLAIMED.** One fixture, one carrier family, four widths. No
bracket, no ray, no edge, no interior.

---

## W1 — the wall, and the charter

### What was open

Block 188 landed full-span site OS positivity and named **the proper OS
transfer** as its open leg. Block 189 classified the site symmetry family and
computed its exact stabiliser, and left that same leg untouched. The obvious
next move — take the one-step pairing `L_1` on a pair core and call
`V = K_c^-1 L_1` the transfer operator — had already failed once on the `T = 8`
carrier, and the question was whether it fails **because the carrier is too
small** or **because the construction forbids it at every width**.

### The charter

1. Generalise the site construction to arbitrary even width and **say plainly
   which convention changed**, with the fork measured.
2. Decide the naive transfer question at width, with witnesses rather than an
   appeal to a global commutator.
3. If it fails, find the object that does not: measure the step operators, ask
   whether they are local, and compute the two-slice monodromy directly.
4. Prove whatever positivity exists **exactly** — no eigenvalue estimates, no
   tolerances, no floats.
5. Fence every word that would turn a spectrum into physics.

---

## N1 — THE CONSTRUCTION CONTROL, and it is two-sided

**NOTHING BELOW IS ABOUT THE LANDED CHAIN'S OBJECT IF THIS SECTION IS NOT
EXACT.**

### The one import, displayed entrywise

The only object this runner imports from the landed chain is Block 105's
`shear_hodge()`, read through the Block 128 module. **Its value is displayed
here rather than described**, at the pinned shear `c = 5/13` and the pinned
**unit volume** `v = 1`:

```
B(5/13, 1) = I_4 + (25/144)(E_11 + E_22) - (65/144)(E_12 + E_21)

           [ 1        0         0      0 ]
         = [ 0    169/144   -65/144    0 ]
           [ 0    -65/144   169/144    0 ]
           [ 0        0         0      1 ]
```

in the zero-based corner order `(1, dx, dt, dx^dt)`. Gate `C-2` compares those
sixteen numbers to `b128.block105.shear_hodge(5/13, 1)` **entrywise, at zero
residual**. The cell embedding is *not* imported: the landed one is fixed to a
single time extent and this block varies the width, so it is rebuilt here at
general even `T` with the same corner order.

### And the Hodge fork is resolved on both sides — which settles the check's C3/C6/C8

The adversarial check could not read this runner and rebuilt the shear block
three different ways, getting three different answers and concluding the
coefficients were unverifiable. **All three rebuilds are reproduced here as
declared controls, and the discrepancy is located exactly.**

| control block | `T = 12` even-core factors | verdict |
| --- | --- | --- |
| **the landed `shear_hodge(5/13, 1)`** | `(5675, 5634, -6845)`, `(6845, 5634, -5675)`, `(39529825, 55889280, 109432706, -55889280, 39529825)` | **this block's numbers** |
| the check's **forensic variant** `I - 2c^2 E_11 - c(E_12+E_21)` | **identical, at every bulk core, for both `V` and `W`** | **spectrally the same object** — which is exactly why the check reproduced every headline coefficient under it |
| the **Block 105 note's own displayed block** = `shear_hodge(5/13, 12/13)` = `diag(12/13, 13/12, 13/12, 13/12)` with `(1,2) = (2,1) = -5/12` | `(1975, 1953, -2365)`, `(2365, 1953, -1975)`, `(4746925, 6783420, 13155959, -6783420, 4746925)` | **the check's own displayed rebuild, digit-for-digit** |
| the check's **unit-shear fallback** `I_4` with `(1,2) = (2,1) = -c` | `(475, 468, -565)`, `(565, 468, -475)`, `(272425, 393120, 755774, -393120, 272425)` | **their second rebuild, digit-for-digit** |

**The discrepancy was a VOLUME CONVENTION and never a disputed measurement.**
The block that produced the check's `B_105` family is not a different formula at
all — it is *this same landed function at* `v = 12/13`. That is why this note
displays the block entrywise **at a pinned volume** instead of describing it,
and why gates `C-14`, `C-15` and `C-16` measure the robustness, the sensitivity
and the reproduction rather than leaving any of the three to a reader's guess.

### The structure, at `T = 12`

| statement | value | gate |
| --- | ---: | :---: |
| `nnz(d_K^2)` — the raising part is a differential | `0` | `C-8` |
| `nnz(Ps H Ps - H)` | `0` | `C-9` |
| `nnz(Ps Q Ps - Q^T)` | `0` | `C-9` |
| cross block `{1..5} x {7..11}` of `Q` | `0` nonzeros — the halves do not couple | `C-10` |
| every adjacent core `t0 = 1,2,3,4`: symmetry residual, rank, minor signs | `0`, `8`, `(+,+,+,+,+,+,+,+)` | `C-11` |
| full `{1..5}` span Gram, exact rank | `8` — **the OS space does not grow with the span** | `C-12` |
| `12 x 12` Schur complement of the `{1,2}` core inside that span | `0` nonzeros — **every core is a frame for the same eight directions** | `C-13` |

---

## N2 — THE NAIVE TRANSFER PAIRING IS REFUTED, and the check's C2 correction is carried as content

### What is exactly true

At `T = 12`, on the bulk cores, the shifted pairings are **not symmetric**:

| core `t0` | `nnz(L_1 - L_1^T)` | `nnz(L_2 - L_2^T)` |
| ---: | ---: | ---: |
| 1 | 48 | 40 |
| 2 | 48 | 40 |
| 3 | 48 | 48 |

**Six exact witnesses, by position and value** — index `0` is the cell
`(t0, 0)` and index `4` is `(t0+1, 0)`:

| core | `k` | position | exact value of `(L_k - L_k^T)` there |
| ---: | ---: | :---: | --- |
| 1 | 1 | `(0,1)` | `839039300251161817029323017210249139894300640625/10790888393902301609279309496845869518844858077209` |
| 1 | 2 | `(0,1)` | `-476073000000/512915117048537` |
| 2 | 1 | `(0,1)` | `-906698597244659770526025093421484375/120809412487309579386522672090695208353` |
| 2 | 2 | `(0,4)` | `-128538968276917302214042968750000000/7914929056239059806431509242611057315467` |
| 3 | 1 | `(0,1)` | `-906698597244659770526025093421484375/120809412487309579386522672090695208353` |
| 3 | 2 | `(0,1)` | `476073000000/512915117048537` |

**Neither naive transfer pairing is self-adjoint on the OS core, at any bulk
position, at this width.**

### The mechanism, and it is a mechanism and not the proof

The global reason is that time translation does not commute with the action, so
it cannot commute with `G = Q^-1` either. Measured at `T = 8`, **in both sign
layers**:

| quantity | `w(3)` (landed) | `w(T-1)` (wrap) |
| --- | ---: | ---: |
| `nnz([tau^2, Q])` | 224 | 208 |
| ordered slice pairs in `supp([tau^2, Q])` | 28 | 26 |
| `[tau^2, Q]_(0,1)` | `-65/576` | `-65/576` — **the same** |
| `nnz([tau^2, G])` | 944 | 864 |

### AND HERE IS THE ADVERSARIAL CHECK'S CORRECTION, CARRIED AS CONTENT

The solve's original wording said that `[tau^k, G] != 0` **proves** every
restricted `L_k` is asymmetric. **It does not, and the check was right.** Global
symmetry of the full shifted pairing is equivalent to the global commutator
vanishing; symmetry *after restriction to one eight-vector core* requires only
the **projected** commutator block to vanish, which is a strictly weaker
condition. A nonzero global commutator is therefore consistent with a symmetric
restriction, and no amount of global support settles a core.

**The six core witnesses above are the proof. The commutator is the mechanism.**
`GLOBAL_MECHANISM_IS_SUFFICIENT = False` is a declared constant in the runner and
gate `D-8` measures it, so the correction cannot be quietly dropped by a later
edit. The mutation `break_mechanism_sufficiency` asserts the sufficiency the
check refused, and it must fail.

---

## N3 — THE STEP OPERATOR IS LOCAL, and locality is a matrix statement

### The dynamics is rigid; the metric is not

| statement | residual | gate |
| --- | ---: | :---: |
| `V2@T16 - V4@T16` entrywise | `0` — **position-homogeneous** | `E-1` |
| `V2@T12 - V2@T16` entrywise | `0` — **width-invariant** | `E-2` |
| `V1@T12 - V1@T16` entrywise | `0` | `E-2` |
| `K_c(2) - K_c(4)` at `T = 16` | **56 nonzero entries** | `E-3` |

with the exact Gram witness

```
(K_c(2) - K_c(4))[0,0]
= 400377448540516729912267326589982089768750145494702722472706914791871900000
  /6123616489153094576092155984273690994586709553556143546606984965959685926729.
```

**The step matrices are equal; the Grams are not.** The boundary layer lives in
the metric data, and the step operator is a function of boundary distance alone.
This is an entrywise matrix equality, not a spectral coincidence — which is what
makes the word *local* honest here.

### Every probed core factors `(2, 2, 4)` over Q

Eighteen cores are probed across `T = 12, 16, 20`. **Every one** of them factors
as two rational quadratics times one rational quartic, and the quadratics are
completely rigid:

- **even cores, at every position and width probed:**
  `5675 z^2 + 5634 z - 6845` and `6845 z^2 + 5634 z - 5675` — each the other's
  reversal;
- **odd cores, at every position and width probed:**
  `1794654055 z^2 + 1598495382 z - 2164653217` and
  `2164653217 z^2 + 1598495382 z - 1794654055`.

### The quartics carry the boundary layer — at BOTH seams

| sector | cores | quartic |
| --- | --- | --- |
| odd, **near seam** | `T = 12, 16, 20` at `t0 = 1` | `38849406107919890625 z^4 + 96204052429420176000 z^3 + 476869355306538239554 z^2 - 108546564308758876800 z + 43833595903292990625` |
| odd, **far seam** (the exact coefficient mirror) | `t0 = T/2 - 3`, i.e. `(12,3)`, `(16,5)`, `(20,7)` | `43833595903292990625 z^4 + 108546564308758876800 z^3 + 476869355306538239554 z^2 - 96204052429420176000 z + 38849406107919890625` |
| odd, **deep** | `(16,3)`, `(20,3)`, `(20,5)` | `20375067515625 z^4 + 50455444752000 z^3 + 257292658829458 z^2 - 50455444752000 z + 20375067515625` |
| even, **interior** | `(12,2)`, `(16,2)`, `(16,4)`, `(20,2)`, `(20,4)`, `(20,6)` | `39529825 z^4 + 55889280 z^3 + 109432706 z^2 - 55889280 z + 39529825` |
| even, **far seam** | `t0 = T/2 - 2`, i.e. `(12,4)`, `(16,6)`, `(20,8)` | `47667825 z^4 + 63213480 z^3 + 101294706 z^2 - 55889280 z + 39529825` |

### AND HERE IS THIS BLOCK'S CORRECTION TO ITS OWN EARLIER WORDING

The solve recorded the even sector as **completely rigid — position- and
width-invariant**, and called it the first exact bulk transfer invariant. **That
is too strong, and the far-seam row above is why.** At `t0 = T/2 - 2` the even
quartic is a *different* polynomial at all three widths. What is true is:

- the even **quadratics** are rigid everywhere probed;
- the even **quartic** is rigid in the **interior** — six cores, three widths;
- and there is a **one-core far-seam layer** whose value is itself **locked
  across `T = 12, 16, 20`**.

So the even sector has its own boundary layer, exactly as the odd sector does;
it is one core deep instead of three, and it sits at the far seam rather than
the near one. The word *everywhere* is not used, and gate `E-8` is the mutation
target `break_far_boundary_layer` that stops the stronger wording from
returning.

---

## N4 — THE MIRROR COVARIANCE, exact at nine coefficients

Let `p` be the primitive degree-8 coefficient vector of `charpoly(V)` at a core
and `q` that of its reflected partner. Measured at `T = 12` (`V1` against `V3`)
and at `T = 16` (`V1` against `V5`), with **zero** coefficient residual:

```
q_j = (-1)^j p_(8-j),   j = 0, ..., 8.
```

Equivalently `q(z)` is proportional to `z^8 p(-1/z)`, which is exactly the
statement

```
spec(V_mirror) = { -1/lambda : lambda in spec(V) }   with multiplicity.
```

The minus sign is the antiperiodic/odd-glue structure; the reciprocal is the
time reflection `theta_s` acting on transfer data. **This is a coefficient
identity, checked coefficient by coefficient, not a numerical eigenvalue
comparison.**

---

## N4a — THE UNIT-CELL MONODROMY, and it is primitive

At `T = 20`, deep cores `t0 = 3` (odd), `4` (even) and `5` (odd):

| statement | value | gate |
| --- | --- | :---: |
| `nnz(W - V^2)` | **32** at every deep core | `F-1` |
| `(W - V^2)[0,4]` at `t0 = 3` | `53601896033238042551256/229758595220483765728625` | `F-2` |
| `(W - V^2)[0,4]` at `t0 = 4` | `-46628656073521939366872/229758595220483765728625` | `F-2` |
| `(W - V^2)[0,4]` at `t0 = 5` | `53601896033238042551256/229758595220483765728625` | `F-2` |

**`tau` does not respect the OS null space even in the bulk, so the monodromy
cannot be built by squaring the step.** `W` is the primitive object.

And its spectrum is **parity-independent** — identical at the odd and even deep
cores, and at a second odd core three slices away:

```
charpoly(W) = (22569375 z^2 - 233631106 z + 22569375)^2
            * (39529825 z^2 - 109432706 z + 39529825)^2
```

### The coefficient identity

The second monodromy quadratic is exactly `a z^2 - c z + a` where
`(a, b, c) = (39529825, 55889280, 109432706)` are the first three coefficients
of the **even `V`-quartic** `a z^4 + b z^3 + c z^2 - b z + a`. **The odd
coefficient `b` drops out.** The first monodromy quadratic is *not* obtained the
same way from the odd-bulk quartic — `(22569375, 233631106)` is new content, and
this note says so rather than generalising a single instance into a rule.

---

## N4b — THE POSITIVITY, PROVEN — and said here, not in a footnote

Both factors are quadratics `a z^2 - c z + a` with `a, c > 0`. Four exact
integer facts settle the spectrum completely, and **not one of them is an
eigenvalue estimate**:

1. **The discriminants are positive integers**, with their factorisations gated:

```
Delta_1 = 233631106^2 - 4*22569375^2 = 52545986939220736
        = 2^8 * 13 * 31 * 37 * 71 * 313^2 * 1979 > 0
Delta_2 = 109432706^2 - 4*39529825^2 = 5725088884359936
        = 2^8 * 3^7 * 7 * 13 * 31 * 37 * 313^2 > 0
```

so each quadratic has **two distinct real roots**.

2. **Each trace exceeds twice its leading coefficient** —
`233631106 > 2*22569375` and `109432706 > 2*39529825` — so the roots are not
merely real but **positive**.

3. **Each constant/leading ratio is exactly `1`**, so the two roots of each
factor are **reciprocal**: `{e^{+theta}, e^{-theta}}`.

4. **The two trace ratios are distinct**, because

```
233631106 * 39529825 - 109432706 * 22569375 = 6765568955757700 != 0,
```

so the four roots are **four distinct numbers**, not two with multiplicity four.

Therefore the monodromy spectrum is **four distinct real positive numbers in two
reciprocal pairs**, each pair doubled, with

```
2 cosh(theta_1) = 233631106/22569375,   2 cosh(theta_2) = 109432706/39529825
```

**exactly, as rationals.**

**AND THE SCOPE IS STATED IN THE SAME BREATH AS THE RESULT.** What is proven is
that a particular constructed `8 x 8` rational matrix has a positive reciprocal
spectrum. That this *is* reflection-positive transfer requires an OS
reconstruction — a Hilbert space, a self-adjoint generator and a
positivity-preserving semigroup — and **this block performs none of it**. The
step operator `V`, by contrast, has negative and complex eigenvalues, which is
consistent with `tau` not being OS-self-adjoint on this class. **The positivity
result is about the unit cell and about nothing larger.**

---

## N4c — THE COMMUTANT, computed exhaustively rather than guessed

Measured at the `T = 20` deep core `t0 = 3`, in the core order.

### `U`, the two-site shift: a Gram isometry that grades the spectrum

| statement | value | gate |
| --- | ---: | :---: |
| `U^T K_c U - K_c` | `0` | `G-1` |
| `[W, U]` | `0` | `G-1` |
| off-sector block `(I-U)/2 * W * (I+U)/2` | `0` nonzeros | `G-2` |
| `U = +1` sector | `(39529825 z^2 - 109432706 z + 39529825)^2` — **both copies of the light pair** | `G-3` |
| `U = -1` sector | `(22569375 z^2 - 233631106 z + 22569375)^2` — **both copies of the heavy pair** | `G-3` |

Block 189's stabiliser generator reappears here as an exact **grading of the
monodromy spectrum**. Their result is extended, not corrected.

### `S`, the one-site shift: a second commutant that is *not* a symmetry of the pairing

| statement | value | gate |
| --- | ---: | :---: |
| `[W, S]`, `S^2 - U`, `S^4 - I` | `0`, `0`, `0` | `G-4` |
| `S^T K_c S - K_c` | **64 nonzero entries** | `G-5` |

with witness

```
(S^T K_c S - K_c)[0,0]
= 2196923328476037505923247454222973532938493206039747366330235451412004291015625
  /2814140416367857864535548440193722522538862625515710221151046656087532099673561724.
```

Its momentum blocks resolve the `U`-sectors into four momenta:

| momentum `p` | exact primitive polynomial |
| ---: | --- |
| 0 | `39529825 z^2 - 109432706 z + 39529825` |
| 1, 3 | `22569375 z^2 - 233631106 z + 22569375` (doubled) |
| 2 | `39529825 z^2 - 109432706 z + 39529825` |

**AND THE `p = 0` / `p = 2` EQUALITY IS NOT FORCED BY THE GROUP.** A cyclic
`Z_4` momentum decomposition forces `p = 1` and `p = 3` to pair (they are
complex-conjugate characters); it forces nothing between the two *real*
characters `p = 0` and `p = 2`. That they carry the same polynomial is an
**additional exact isospectrality of this construction**, and
`MOMENTUM_EQUALITY_IS_GROUP_FORCED = False` is a declared constant with gate
`G-7` on it.

### The census, exhaustive and measured here

All **2048** signed monomial candidates are swept — an optional swap of the two
time layers, times every spatial dihedral action, times every relative sign
pattern up to an overall sign:

- **`W`-commutants: exactly `{I, S, U, S^3}`** — four of 2048;
- **Gram isometries among them: exactly `{I, U}`** — two of four.

In particular no signed spatial reflection and no grade-composed one-site shift
supplies a second pairing-preserving symmetry. The unsigned reflection is
refuted with a **16-entry** commutator and the exact witness
`[W, R]_(0,5) = 16334218/7905965`.

**The residual double degeneracy inside each `U`-sector is therefore not
explained by any monomial symmetry, and this note does not pretend otherwise.**
It is measured, its explanation is open, and `N6` records it as such.

---

## N4d — THE P1 CONVENTION FORK, resolved the other way

The adversarial check's `P1` reported that transposing the pairing convention in
`K_c` alone **changes the spectrum**, with a 64-entry difference, and concluded
that convention robustness needs `K_c` and `L_k` transposed together. **On this
construction the first half does not happen, and the reason is one measured
number.**

| statement | value | gate |
| --- | ---: | :---: |
| `K_c - K_c^T` at the deep core | **`0` — `K_c` is exactly symmetric** | `G-12` |
| **`K`-only transposition:** `nnz(K_c^{-T} L_2 - W)` | **`0` — a measured no-op** | `G-13` |
| **consistent transposition:** `nnz(K_c^{-T} L_2^T - W)` | **48** | `G-14` |
| `charpoly` preserved under the consistent transposition | **yes** | `G-15` |
| `nnz(K_c^{-T} L_2^T - K_c^{-1} W^T K_c)` | **`0`** | `G-16` |

**Because `K_c` is symmetric, `K_c^T = K_c` and the `K`-only variant *is* the
original operator.** It cannot change any spectrum. And the consistent
transposition is a **similarity**, in two lines:

```
W' = K_c^-1 L_2^T = K_c^-1 (K_c W)^T = K_c^-1 W^T K_c^T = K_c^-1 W^T K_c,
```

so `W'` is similar to `W^T` and `charpoly(W') = charpoly(W)` — while moving 48
entries. **The robustness is a theorem here, not a coincidence of these
numbers**, and gate `G-16` measures the similarity residual rather than trusting
the algebra. The mutation `break_konly_vacuity` asserts the check's 64-entry
change and must fail.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The four words, and what each of them actually names here

| word | what is measured | what is **not** derived |
| --- | --- | --- |
| **dispersion** | the characteristic polynomials of two momentum blocks of one `8 x 8` rational matrix | that these are energies of a propagating mode; that a lattice dispersion relation exists at all |
| **mass scale** | `theta_1`, `theta_2` with `2 cosh theta` exactly rational | any mass, any unit, any continuum limit, any ratio with physical meaning |
| **physical time step** | that the staggering of this carrier has period two in time | that the two-slice cell is *the* time step of a theory |
| **transfer positivity** | four distinct real positive reciprocal roots of one matrix, proven exactly | reflection positivity, an OS Hilbert space, a self-adjoint generator, a semigroup |

### And two further fences, both of which this block put on itself

- **THE OBJECT IS A VARIANT.** Every number in `N2`–`N4d` is measured on the
  wrap-edge family. The landed `T = 8` object is reproduced in `N1` under *its*
  placement and is otherwise not the subject of this note.
- **THE WIDTHS STOP AT 20.** "Deep", "bulk" and "converged" here mean *at the
  probed depths and widths*. **Nothing is proven about the infinite-width
  limit.** Three widths agreeing is three widths agreeing.

### What IS derived, stated positively so the fence is not mistaken for a retreat

Six things, all exact: the **refutation** of both naive transfer pairings on
every bulk core, with witnesses; the **entrywise** locality and width-invariance
of the step operator; the **two boundary layers** with their locked values; the
**mirror covariance** as a coefficient identity; the **primitivity, parity
independence and proven positive reciprocal spectrum** of the unit-cell
monodromy; and the **exhaustively computed commutant** with its exact grading of
the spectrum.

---

## READINGS — four of them, and each is a reading

**THE TWO-REGISTER RULE APPLIES: nothing below is measured, and nothing above
licenses any of it.**

- **(R1) THE MONODROMY SPECTRUM IS THE PHYSICAL TRANSFER CONTENT OF THE
  CONSTRUCTION.** That `{e^{±theta_1}, e^{±theta_2}}` is the correlation/gap
  content of a gravitational OS sector **IS A READING.** What is measured is the
  spectrum of `K_c^-1 L_2` on one core of one constructed matrix.
- **(R2) `U` IS A MOMENTUM AND THE TWO SCALES ARE `E(0)` AND `E(pi)`.** That the
  `U = ±1` grading is lattice momentum, and that the two rapidities are a single
  mode's dispersion sampled at `k = 0` and `k = pi`, **IS A READING** — an
  attractive one, and one this block cannot discharge: it has no propagator, no
  spectral function and no second fixture.
- **(R3) THE BOUNDARY LAYERS ARE PHYSICAL SURFACE EFFECTS.** That the near- and
  far-seam quartics describe boundary physics rather than an artefact of the
  glue's half-structure **IS A READING.** The far-seam even layer discovered
  here was not predicted by the reading that preceded it, which is a mark
  against it and is recorded as one.
- **(R4) THE WIDTH-INVARIANCE IS AN INFINITE-VOLUME LIMIT.** **IS A READING.**
  Three widths is three widths.

**AND ONE THING RUNS IN THE OTHER DIRECTION, WHICH IS WORTH SAYING.** "The
transfer is positive, therefore the construction is reflection-positive" is
**not** available. The proven positivity is a property of one `8 x 8` matrix; the
naive transfer that would have carried it to the full construction is **refuted
in `N2` of this very note**. A reading that would have been supported by the
positivity is supported by it **less** after this block than before, not more.

---

## CLAIM REGISTER — formulas, and the family that gates each

**MEASURED register.** Every row is an exact identity, an exact integer or an
exact rational measured by the runner; none is a summary.

| # | claim, as a formula | value | family |
| ---: | --- | --- | :---: |
| 1 | `shear_hodge(5/13, 1) - (I + (25/144)(E11+E22) - (65/144)(E12+E21))` | `0_4` entrywise | `C` |
| 2 | `nnz(Q - Q^T)` at `T=8`, `w(3)` / `w(T-1)` | `144` / `160` | `C` |
| 3 | `nnz(Ps Q Ps - Q^T)` at `T=8`, both placements | `0` / `0` | `C` |
| 4 | `det(K[:1,:1])` at `w(3)` | `250811603701251182926764176363850176714557920003089965221914456500/666495028860293624372300921944800123265476111209829299156533225479` | `C` |
| 5 | `det(K[:2,:2])` at `w(3)` | `9699265179160355495171233606378759680576921193642386633764164130236400111062250000/65542091681979044701359795584266761562795513633598145522262137753727157320281821073` | `C` |
| 6 | `det(K[:1,:1])` at `w(T-1)` | `6874991398831399275340647912337474750/18307834037130787420472860378633197921` | `C` |
| 7 | `nnz(d_K^2)`, `nnz(Ps H Ps - H)`, `nnz(Ps Q Ps - Q^T)` at `T=12` | `0`, `0`, `0` | `C` |
| 8 | nonzeros of the `{1..5} x {7..11}` block of `Q` | `0` | `C` |
| 9 | `(nnz(K_c - K_c^T), rank K_c, sign minors)` at `t0=1,2,3,4`, `T=12` | `(0, 8, (+)^8)` four times | `C` |
| 10 | `rank` of the full `{1..5}` span Gram | `8` | `C` |
| 11 | `nnz` of its `12 x 12` Schur complement on the `{1,2}` core | `0` | `C` |
| 12 | `charfactors(V, W)` under the check's forensic block vs the landed block, `t0 = 1,2,3` | **equal, all six** | `C` |
| 13 | `charfactors(V)` at `t0=2`, `T=12`, under `shear_hodge(5/13, 12/13)` | `(1975,1953,-2365)`, `(2365,1953,-1975)`, `(4746925,6783420,13155959,-6783420,4746925)` | `C` |
| 14 | same, under the check's unit-shear fallback | `(475,468,-565)`, `(565,468,-475)`, `(272425,393120,755774,-393120,272425)` | `C` |
| 15 | `nnz(L_1 - L_1^T)` at `t0=1,2,3`, `T=12` | `(48, 48, 48)` | `D` |
| 16 | `nnz(L_2 - L_2^T)` at the same cores | `(40, 40, 48)` | `D` |
| 17 | the six exact `(L_k - L_k^T)` witnesses, by position and value | the table in `N2` | `D` |
| 18 | `nnz([tau^2, Q])` at `T=8`, `w(3)` / `w(T-1)` | `224` / `208` | `D` |
| 19 | ordered slice pairs of `supp([tau^2, Q])`, both layers | `28` / `26` | `D` |
| 20 | `[tau^2, Q]_(0,1)`, both layers | `-65/576` (common) | `D` |
| 21 | `nnz([tau^2, G])`, both layers | `944` / `864` | `D` |
| 22 | `[tau^k, G] != 0` **suffices** for restricted asymmetry | **`False`** — declared, gated; the six witnesses are the proof | `D` |
| 23 | `nnz(V2@T16 - V4@T16)` | `0` | `E` |
| 24 | `nnz(V2@T12 - V2@T16)`, `nnz(V1@T12 - V1@T16)` | `0`, `0` | `E` |
| 25 | `nnz(K_c(2) - K_c(4))` at `T=16`, and `[0,0]` | `56`; `400377448540516729912267326589982089768750145494702722472706914791871900000/6123616489153094576092155984273690994586709553556143546606984965959685926729` | `E` |
| 26 | factor-degree pattern at all 18 probed cores | `(2, 2, 4)` eighteen times | `E` |
| 27 | even quadratics, all even cores probed | `(5675,5634,-6845)`, `(6845,5634,-5675)` | `E` |
| 28 | odd quadratics, all odd cores probed | `(1794654055,1598495382,-2164653217)`, `(2164653217,1598495382,-1794654055)` | `E` |
| 29 | even quartic at the 6 interior even cores | `(39529825, 55889280, 109432706, -55889280, 39529825)` | `E` |
| 30 | even quartic at `t0 = T/2 - 2`, `T = 12, 16, 20` | `(47667825, 63213480, 101294706, -55889280, 39529825)` — **the far-seam layer** | `E` |
| 31 | odd quartic at `t0 = 1`, `T = 12, 16, 20` | `(38849406107919890625, 96204052429420176000, 476869355306538239554, -108546564308758876800, 43833595903292990625)` | `E` |
| 32 | odd quartic at `t0 = T/2 - 3` | the exact coefficient mirror of row 31 | `E` |
| 33 | odd quartic at `(16,3)`, `(20,3)`, `(20,5)` | `(20375067515625, 50455444752000, 257292658829458, -50455444752000, 20375067515625)` | `E` |
| 34 | `#{ j : q_j != (-1)^j p_(8-j) }`, `T=12` `V1/V3` and `T=16` `V1/V5` | `0`, `0` | `E` |
| 35 | `nnz(W - V^2)` at `T=20`, `t0 = 3, 4, 5` | `32`, `32`, `32` | `F` |
| 36 | `(W - V^2)[0,4]` at those three cores | `53601896033238042551256/229758595220483765728625`, `-46628656073521939366872/229758595220483765728625`, `53601896033238042551256/229758595220483765728625` | `F` |
| 37 | `#{ distinct charpoly(W) over t0 = 3,4,5 }` | `1` — parity-independent | `F` |
| 38 | `charpoly(W)` | `(22569375 z^2 - 233631106 z + 22569375)^2 (39529825 z^2 - 109432706 z + 39529825)^2` | `F` |
| 39 | `c^2 - 4a^2` for each factor | `52545986939220736`, `5725088884359936`, both `> 0` | `F` |
| 40 | their prime factorisations | `2^8·13·31·37·71·313^2·1979`, `2^8·3^7·7·13·31·37·313^2` | `F` |
| 41 | `c > 2a` for each factor | `True`, `True` — roots positive, not merely real | `F` |
| 42 | constant/leading for each factor | `1`, `1` — reciprocal pairs | `F` |
| 43 | `233631106·39529825 - 109432706·22569375` | `6765568955757700 != 0` — four **distinct** roots | `F` |
| 44 | `2 cosh theta_1`, `2 cosh theta_2` | `233631106/22569375`, `109432706/39529825` | `F` |
| 45 | second `W` quadratic vs `(a, -c, a)` from the even `V`-quartic `(a,b,c,-b,a)` | equal — `b` drops out | `F` |
| 46 | `nnz(U^T K_c U - K_c)`, `nnz([W,U])`, off-sector nonzeros | `0`, `0`, `0` | `G` |
| 47 | `charpoly` of the `U = +1` and `U = -1` blocks | `(39529825,...)^2`; `(22569375,...)^2` | `G` |
| 48 | `nnz([W,S])`, `nnz(S^2 - U)`, `nnz(S^4 - I)` | `0`, `0`, `0` | `G` |
| 49 | `nnz(S^T K_c S - K_c)` and its `[0,0]` | `64`; `2196923328476037505923247454222973532938493206039747366330235451412004291015625/2814140416367857864535548440193722522538862625515710221151046656087532099673561724` | `G` |
| 50 | `S`-momentum blocks `p = 0`, `p = 2`, `p = 1,3` | `39529825`-family, `39529825`-family, `22569375`-family | `G` |
| 51 | the `p=0`/`p=2` equality is **group-forced** | **`False`** — declared, gated: an additional isospectrality | `G` |
| 52 | candidates swept; `W`-commutants; Gram isometries among them | `2048`; `{I, S, S^3, U}`; `{I, U}` | `G` |
| 53 | `nnz([W, R])` and `[W,R]_(0,5)` | `16`; `16334218/7905965` | `G` |
| 54 | `nnz(K_c - K_c^T)` at the deep core | `0` | `G` |
| 55 | `nnz(K_c^{-T} L_2 - W)` — the `K`-only transposition | `0` — **a no-op** | `G` |
| 56 | `nnz(K_c^{-T} L_2^T - W)`; `charpoly` preserved | `48`; **yes** | `G` |
| 57 | `nnz(K_c^{-T} L_2^T - K_c^{-1} W^T K_c)` | `0` — the similarity, measured | `G` |
| 58 | `sp.nsimplify` occurrences in the runner's own source | `0` | `H` |

**READING register.** Nothing below is measured, and nothing above licenses any
of it.

| # | reading | status |
| ---: | --- | --- |
| R1 | the monodromy spectrum is the physical transfer content | **READING** — one matrix, one core |
| R2 | `U` is momentum; `theta_1`, `theta_2` are `E(pi)`, `E(0)` of one mode | **READING** — no propagator, no spectral function |
| R3 | the boundary layers are physical surface effects | **READING** — and the far-seam layer was unpredicted by it |
| R4 | width-invariance at three widths is an infinite-volume limit | **READING** |
| R5 | "transfer positivity" for the construction as a whole | **READING** — `N4b`; the OS reconstruction is not performed |
| R6 | "dispersion", "mass scale", "physical time step" | **READING** — `N4g`, with nine structures not supplied |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

**EVERY FORK WAS MEASURED AT ITS FORK, SO NOTHING WRONG LEFT THE SOLVE.**

1. **THE ONE-STEP PAIRING WAS TRIED FIRST — DEAD AT 48 ENTRIES.** `L_1` is the
   object the transfer program *wants*. It is not symmetric at any bulk core.
2. **THE TWO-STEP PAIRING WAS TRIED NEXT, AS THE OBVIOUS REPAIR — DEAD AT 40.**
   The staggering has period two in time, so `L_2` was the natural candidate for
   a self-adjoint pairing. It fails too.
3. **THE WIDTH WAS TRIED AS THE CURE — AND IT IS NOT THE CURE.** The natural
   hypothesis was that `T = 8` is too small for a deep core to exist. `T = 12`,
   `16` and `20` all fail identically, and the mechanism (`N2`) says why.
4. **`W = V^2` WAS ASSUMED BEFORE IT WAS MEASURED — FALSE AT 32 ENTRIES.** The
   monodromy looked like it should be the square of the step. It is not, at any
   deep core, which is what makes `W` primitive rather than derived.
5. **THE EVEN SECTOR WAS CALLED COMPLETELY RIGID — AND THE FAR SEAM REFUTED IT.**
   Six interior cores agreed across three widths, which was taken for
   everywhere. Probing `t0 = T/2 - 2` produced a different quartic at all three
   widths. The claim is now stated with its exception, and `E-8` guards it.
6. **THE SPATIAL REFLECTION WAS THE FIRST GUESS FOR THE RESIDUAL DEGENERACY —
   DEAD AT 16 ENTRIES.** It neither commutes with `W` nor preserves `K_c`. The
   one-site shift `S` was found instead, and *it* is not a Gram isometry, so the
   degeneracy is still unexplained by symmetry. The 2048-candidate census is
   what closes the monomial search rather than a sequence of lucky guesses.
7. **A HODGE FORK CONSUMED AN ENTIRE ADVERSARIAL CHECK — AND IT WAS A VOLUME.**
   Three plausible readings of the shear block gave three different coefficient
   families. The resolution was to stop describing the block and **display it**,
   pinned at `v = 1` and gated entrywise against the import.

---

## N5 — the fence

```
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- THE WIDTH FAMILY (the staggered Dirac-Kahler carrier on Z_T x Z_4 for even T with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 carried ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site Hodge with block B(c) on t < T/2 and P_4 B P_4^T on the far half, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13), at widths T = 8, 12, 16, 20), THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE STEP OPERATOR V = K_c^-1 L_1 AND THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE CORE SYMMETRY CANDIDATES U, S, R and the full 2048-element signed-monomial set, THE SINGLE FIXTURE (9/20, 5/13), and the LANDED Block 105 shear_hodge() read through the Block 128 module -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. AND THE OBJECT IS A DISCLOSED VARIANT AND SAYS SO BEFORE IT SAYS ANYTHING ELSE: BLOCK 188's LANDED T = 8 OBJECT CARRIES THE ANTIPERIODIC SIGN AT t = 3 AND THIS FAMILY CARRIES IT AT t = T-1, AND THE FORK IS MEASURED AS A PAIR -- nnz(Q - Q^T) = 144 at the landed placement, which is BLOCK 188's OWN LANDED NUMBER, and 160 at the wrap edge, with Ps Q Ps = Q^T at ZERO on BOTH SIDES. AND THE WORDS ARE FENCED BEFORE THE NUMBERS ARE READ. DISPERSION IS A READING: what is measured is the characteristic polynomial of a finite matrix in two momentum sectors, and that E(0) and E(pi) are energies of a propagating mode is NOT DERIVED. MASS SCALES ARE A READING: theta_1 and theta_2 are logarithms of exact rational-trace eigenvalues, with no mass, no continuum limit and no unit supplied. THE PHYSICAL TIME STEP IS A READING: that the two-slice unit cell is THE time step of a theory is a statement about a staggered carrier and not a theorem. TRANSFER POSITIVITY IS A READING: the positivity of this 8 x 8 spectrum is PROVEN, and the Osterwalder-Schrader reconstruction that would make it mean transfer positivity IS NOT PERFORMED. NO GRAVITY STRUCTURE IS SUPPLIED -- no lapse function, no shift vector, no Hamiltonian constraint, no momentum or diffeomorphism constraint, no first-class algebra, no Dirac closure and no ADM phase space. NO GENERALITY IS CLAIMED: ONE fixture, ONE carrier family, FOUR widths. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.
per_site: THE CONSTRUCTION CONTROL IS TWO-SIDED AND IT COMES FIRST. THE HODGE: the ONLY imported object is Block 105's shear_hodge() through the Block 128 module, its value at (c, v) = (5/13, 1) is DISPLAYED INLINE ENTRYWISE as I + (25/144)(E11 + E22) - (65/144)(E12 + E21) -- that is diag(1, 169/144, 169/144, 1) with the (1,2) and (2,1) entries -65/144 in zero-based corner order (1, dx, dt, dx^dt) -- and the displayed matrix is gated against the import at ZERO entrywise residual. THE SIGN LAYER: at T = 8 the LANDED placement reproduces BLOCK 188's core minors DIGIT-FOR-DIGIT, first minor 250811603701251182926764176363850176714557920003089965221914456500/666495028860293624372300921944800123265476111209829299156533225479 and second minor 9699265179160355495171233606378759680576921193642386633764164130236400111062250000/65542091681979044701359795584266761562795513633598145522262137753727157320281821073, while the WRAP placement gives 6874991398831399275340647912337474750/18307834037130787420472860378633197921 at the same core -- A DIFFERENT NUMBER, MEASURED, WHICH IS EXACTLY WHY THE VARIANT IS DISCLOSED AND NOT ASSERTED TO BE THEIR OBJECT. AND THE HODGE FORK IS RESOLVED ON BOTH SIDES, WHICH SETTLES THE ADVERSARIAL CHECK'S C3/C6/C8 RATHER THAN ARGUING WITH IT: the check's FORENSIC variant block I - 2c^2 E11 - c(E12+E21) gives the IDENTICAL V and W factorizations at all three T = 12 bulk cores -- which is exactly why the check reproduced every headline coefficient digit-for-digit under it -- while the BLOCK 105 NOTE'S OWN DISPLAYED BLOCK is measured here to be THE SAME LANDED FUNCTION AT VOLUME 12/13, diag(12/13, 13/12, 13/12, 13/12) with the (1,2) and (2,1) entries -5/12, and at that volume every bulk core MOVES: the even core gives (1975, 1953, -2365), (2365, 1953, -1975) and 4746925 z^4 + 6783420 z^3 + 13155959 z^2 - 6783420 z + 4746925, which is THE CHECK'S OWN DISPLAYED REBUILD REPRODUCED DIGIT-FOR-DIGIT, as is their unit-shear fallback's (475, 468, -565), (565, 468, -475) and 272425 z^4 + 393120 z^3 + 755774 z^2 - 393120 z + 272425. THE DISCREPANCY WAS A VOLUME CONVENTION AND NEVER A DISPUTED MEASUREMENT, and that is why this note DISPLAYS the block entrywise at a PINNED volume instead of describing it. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's zeros, counts, signs or coefficient vectors could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate H.
per_mode: THE NAIVE TRANSFER PAIRING IS REFUTED ON THE CORES THEMSELVES, AND THE CHECK'S C2 CORRECTION IS CARRIED AS CONTENT AND NOT AS AN ERRATUM. At T = 12 the one-step and two-step core pairings are ASYMMETRIC at every bulk core: nnz(L_1 - L_1^T) = 48 at t0 = 1, 2, 3 and nnz(L_2 - L_2^T) = 40, 40, 48, with SIX EXACT WITNESSES recorded by position and value. THE GLOBAL MECHANISM IS [tau^k, G] != 0, measured at T = 8 IN BOTH SIGN LAYERS: [tau^2, Q] has 224 nonzeros on 28 ordered slice pairs at the landed placement and 208 on 26 at the wrap edge, with the COMMON exact witness [tau^2, Q]_(0,1) = -65/576, and [tau^2, G] is nonzero in both at 944 and 864 entries. BUT THE CORRECTION IS TAKEN AND IT IS DECLARED AS A CONSTANT: global commutator nonvanishing is NOT BY ITSELF a proof that a RESTRICTED core pairing is asymmetric, because symmetry after restriction to one 8-vector core requires only the PROJECTED commutator block to vanish. THE SIX CORE WITNESSES ARE THE PROOF AND THE COMMUTATOR IS THE MECHANISM.
per_block: THE STEP OPERATOR IS A LOCAL OBJECT, AND LOCALITY IS A MATRIX STATEMENT AND NOT A SPECTRAL ONE. V2@T12, V2@T16 and V4@T16 are EQUAL ENTRYWISE at ZERO residual, and so are V1@T12 and V1@T16: the step dynamics is width-invariant AND position-homogeneous. THE GRAM IS NOT: K_c(2) and K_c(4) at T = 16 differ at EXACTLY 56 ENTRIES, so the boundary layer lives in the metric data. Every probed core factors (2,2,4) over Q with the even quadratics (5675, 5634, -6845), (6845, 5634, -5675) and the odd quadratics (1794654055, 1598495382, -2164653217), (2164653217, 1598495382, -1794654055) invariant throughout. THE ODD QUARTIC CARRIES A NEAR-SEAM LAYER: value 38849406107919890625 z^4 + 96204052429420176000 z^3 + 476869355306538239554 z^2 - 108546564308758876800 z + 43833595903292990625 at t0 = 1 locked at ALL THREE widths, its exact coefficient MIRROR at t0 = T/2 - 3, and the DEEP value 20375067515625 z^4 + 50455444752000 z^3 + 257292658829458 z^2 - 50455444752000 z + 20375067515625 at T = 16 t0 = 3 and T = 20 t0 = 3, 5. AND THE EVEN QUARTIC IS NOT RIGID EVERYWHERE, WHICH CORRECTS THIS BLOCK'S OWN EARLIER WORDING: at the FAR-seam core t0 = T/2 - 2 it is 47667825 z^4 + 63213480 z^3 + 101294706 z^2 - 55889280 z + 39529825 rather than the deep 39529825-family value, and THAT far-seam value is itself LOCKED across T = 12, 16 and 20. The even sector is rigid in the INTERIOR and carries its own one-core far-seam layer. AND THE MIRROR COVARIANCE IS EXACT: q_j = (-1)^j p_(8-j) for all nine coefficients at T = 12 (V1 against V3) and T = 16 (V1 against V5), which is q(z) proportional to z^8 p(-1/z) and therefore spec(V_mirror) = {-1/lambda} with multiplicity.
lattice_wide: THE UNIT-CELL MONODROMY IS PRIMITIVE, PARITY-INDEPENDENT AND POSITIVE, AND THE POSITIVITY IS PROVEN AND NOT ESTIMATED. W != V^2 at EXACTLY 32 entries at every T = 20 deep core t0 = 3, 4, 5, with exact witnesses (W - V^2)_(0,4) = 53601896033238042551256/229758595220483765728625, -46628656073521939366872/229758595220483765728625 and 53601896033238042551256/229758595220483765728625; the monodromy cannot be built by squaring the step and W is the primitive object. charpoly(W) is IDENTICAL at all three deep cores and equals (22569375 z^2 - 233631106 z + 22569375)^2 (39529825 z^2 - 109432706 z + 39529825)^2. THE FOUR POSITIVITY FACTS ARE EXACT INTEGERS: the discriminants are 52545986939220736 = 2^8 * 13 * 31 * 37 * 71 * 313^2 * 1979 and 5725088884359936 = 2^8 * 3^7 * 7 * 13 * 31 * 37 * 313^2, both POSITIVE with their factorizations gated; both traces exceed twice the leading coefficient; both constant/leading ratios are EXACTLY 1 so each pair is reciprocal; and the two trace ratios are DISTINCT because 233631106 * 39529825 - 109432706 * 22569375 = 6765568955757700 != 0. Four distinct real positive roots in two reciprocal pairs, with 2 cosh(theta_1) = 233631106/22569375 and 2 cosh(theta_2) = 109432706/39529825 EXACTLY. AND THE COEFFICIENT IDENTITY IS EXACT: the second monodromy quadratic is a z^2 - c z + a built from the even V-quartic's (a, b, c) = (39529825, 55889280, 109432706), with the odd coefficient b DROPPING OUT.
per_scope: THE COMMUTANT IS COMPUTED EXHAUSTIVELY AND NOT GUESSED, AND THE CHECK'S P1 FORK IS RESOLVED THE OTHER WAY. U (the two-site spatial shift) satisfies U^T K_c U = K_c and [W, U] = 0 at ZERO, with the off-sector block EXACTLY zero, and it GRADES the spectrum: U = +1 carries both copies of 39529825 z^2 - 109432706 z + 39529825 and U = -1 both copies of 22569375 z^2 - 233631106 z + 22569375. S (the ONE-site spatial shift) also commutes with W at ZERO, with S^2 = U and S^4 = I at ZERO, but is NOT a Gram isometry -- S^T K_c S - K_c has EXACTLY 64 nonzero entries with an exact witness -- which is the check's P2 finding rebuilt here on this construction. Its momentum blocks give p = 0 and p = 2 the SAME polynomial and p = 1, 3 the other one, AND THE p = 0 / p = 2 EQUALITY IS DECLARED NOT GROUP-FORCED: it is an ADDITIONAL exact isospectrality. THE CENSUS IS EXHAUSTIVE AND MEASURED IN THIS RUNNER RATHER THAN CITED: all 2048 signed monomial candidates are swept, the W-commutants are EXACTLY {I, S, U, S^3} and EXACTLY {I, U} of them are Gram isometries; the unsigned spatial reflection is refuted with a 16-entry commutator and the exact witness [W, R]_(0,5) = 16334218/7905965. AND THE P1 CORRECTION RUNS THE OTHER WAY ON THIS CONSTRUCTION, WHICH IS THIS BLOCK'S SECOND CORRECTION TO THE CHECK: K_c is EXACTLY SYMMETRIC at the deep core, so the K-ONLY transposition is a MEASURED NO-OP at 0 entries and CANNOT change any spectrum, while the CONSISTENT transposition moves W at EXACTLY 48 entries and still preserves charpoly(W) -- because W' = K_c^-1 W^T K_c is a SIMILARITY, which is a two-line proof and not a coincidence of these numbers.
RESULT: A NAIVE TRANSFER IS REFUTED WITH SIX EXACT WITNESSES, A LOCAL STEP OPERATOR WITH TWO FINITE-RANGE BOUNDARY LAYERS IS EXHIBITED, AND A PRIMITIVE UNIT-CELL MONODROMY WITH A PROVEN POSITIVE RECIPROCAL SPECTRUM AND AN EXHAUSTIVELY COMPUTED COMMUTANT IS COMPUTED IN CLOSED FORM -- AND NOT ONE LINE OF IT IS GRAVITY. The construction control is two-sided and both sides are measured; the displayed Hodge equals the import entrywise; the sign-layer fork is 144 against 160 with Ps-covariance on both sides and the landed minors reproduced digit-for-digit at the landed placement; L_1 and L_2 are asymmetric at every bulk core with six exact witnesses and the global commutator is the MECHANISM and not the proof; the step matrices are width- and position-invariant while the Grams are not, at 56 entries; the odd quartic has a near-seam value, its exact mirror and a deep value, and the even quartic has its own far-seam value locked across three widths; the mirror covariance is exact at nine coefficients; the monodromy is primitive at 32 entries, parity-independent across three deep cores, and positive with factored discriminants and distinct trace ratios; and the commutant is EXACTLY {I, S, U, S^3} with EXACTLY {I, U} isometries out of 2048 candidates. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.
DECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-189 STAND EXACTLY AS LANDED. BLOCK 188 IS NEITHER CORRECTED NOR CONTRADICTED: their T = 8 object is reproduced here DIGIT-FOR-DIGIT under THEIR OWN sign placement, and this block's family is a DISCLOSED VARIANT at a different placement, measured to be a different matrix. BLOCK 189 IS NOT CORRECTED: its stabilizer element U reappears here as the exact mass-scale grading of the monodromy, which extends their result and changes none of it. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE FIXTURE AND NO WINDOW; the four headline words are READINGS and the OS reconstruction that would license them IS NOT PERFORMED; the even quartic's rigidity is NOT global and its far-seam exception is measured here rather than papered over; and the deep-core probes reach T = 20 and no further, so nothing is proven about the infinite-width limit. TWO ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C2 CORRECTION, that the global commutator is a mechanism and the six core witnesses are the proof, which is now a declared constant and a gate; and the P2 S-COMMUTANT, which is now rebuilt, gated and extended by an exhaustive 2048-candidate census. AND TWO CORRECTIONS RUN THE OTHER WAY AND ARE STATED AS SUCH: the check's P1 K-only spectrum change does NOT occur on this construction, because K_c is exactly symmetric and the K-only transposition is a no-op; and the check's C3/C6/C8 coefficient refutations do NOT apply to this construction, because they were computed at a DIFFERENT VOLUME -- the landed shear_hodge() at v = 1 reproduces every stated coefficient, their own two rebuilds are reproduced here digit-for-digit at v = 12/13 and at unit shear, and their forensic variant is measured to be spectrally IDENTICAL to the landed block, which is why the display is now gated entrywise against the import at a PINNED volume. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE PROPER OS TRANSFER -- THE WIDTH RESOLUTION, THE LOCALITY THEOREM SHAPE, THE ODD-SECTOR LOCK, THE UNIT-CELL MONODROMY, THE DEGENERACY MECHANISM and THE B190 CHECK VERDICT AND THE TWO-FORK RESOLUTION anchors.
TOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

- **THE NAIVE OS TRANSFER ON THIS CLASS IS CLOSED, NEGATIVE, WITH MECHANISM.**
  Both `L_1` and `L_2` are asymmetric at every bulk core at every probed width,
  with six exact witnesses and an exact global mechanism. This is not stuck; it
  is answered.
- **THE MONOMIAL SEARCH FOR A SECOND PAIRING SYMMETRY IS CLOSED.** 2048
  candidates, exactly two Gram isometries, both already known. No signed
  reflection and no grade-composed shift exists.
- **THE P1 CONVENTION QUESTION IS CLOSED.** `K_c` is symmetric, so the `K`-only
  fork is vacuous, and the consistent fork is a similarity.

### REOPEN IF

- **the residual in-sector double degeneracy is explained.** It survives the
  exhaustive monomial census, so any explanation must be non-monomial — a
  grading, an anti-unitary, or an accident of this fixture. **A second fixture
  would decide the last of those in one run**, and this block does not have one.
- **the far-seam even layer is explained**, or found at a third seam. Its value
  is locked across three widths, which is exactly the signature that made the
  interior value look like an invariant.
- **an OS reconstruction is actually built** on the unit-cell monodromy. Only
  then does the word *transfer* in `N4b` stop being a reading.
- **a wider carrier moves any locked value.** Everything here stops at `T = 20`.
- **the wrap-edge variant is compared to the landed placement at width.** This
  block measures the fork at `T = 8` only; whether the two placements give the
  same transfer content at `T = 12` and beyond is **not measured here**.

---

## N7 — THE RECORD

### Corrections carried

1. **THE C2 CORRECTION (from the adversarial check), carried as content.**
   `[tau^k, G] != 0` is the **mechanism** and not a proof of restricted core
   asymmetry; the six exact core witnesses are the proof.
   `GLOBAL_MECHANISM_IS_SUFFICIENT = False` is a declared constant with gate
   `D-8` and mutation `break_mechanism_sufficiency`.
2. **THE P2 S-COMMUTANT (from the adversarial check), rebuilt and extended.**
   `S` with `[W,S] = 0`, `S^2 = U`, `S^4 = I`, not a Gram isometry at 64 entries.
   Extended here by the **exhaustive 2048-candidate census**, which the check
   performed and which this runner now performs itself rather than citing.
3. **THE P1 CORRECTION RUNS THE OTHER WAY, and this block says so.** The check's
   `K`-only spectrum change **does not occur** on this construction, because
   `K_c` is exactly symmetric and the `K`-only transposition is a measured no-op.
   Gates `G-12`/`G-13`, mutation `break_konly_vacuity`.
4. **THE C3/C6/C8 COEFFICIENT REFUTATIONS DO NOT APPLY, and the cause is
   located.** They were computed at a **different volume**. The landed
   `shear_hodge()` at `v = 1` reproduces every stated coefficient; the check's
   own two failing rebuilds are reproduced here digit-for-digit at `v = 12/13`
   and at unit shear; and their forensic variant is measured to be spectrally
   identical to the landed block. Gates `C-14`/`C-15`/`C-16`.
5. **THIS BLOCK'S OWN WORDING CORRECTION: the even sector is not rigid
   everywhere.** The far-seam core `t0 = T/2 - 2` carries a different quartic at
   all three widths. Gate `E-8`, mutation `break_far_boundary_layer`.
6. **THE SIGN PLACEMENT IS DISCLOSED, NOT SMUGGLED.** The 144/160 fork with
   `Ps`-covariance on both sides, and the landed minors reproduced under the
   landed placement. Gates `C-4`–`C-7`, mutation `claim_variant_is_landed`.

### The adversarial check

Verdict carried as **CONFIRMED-WITH-TWO-CORRECTIONS**. The check confirmed C1,
C4, C5 and C7 structurally on an independent reconstruction; corrected C2, which
is now a declared constant and a gate; supplied the `S`-commutant and the
census, both now rebuilt here; and flagged C3, C6 and C8 as unverifiable against
its rebuilds — a flag this note **resolves rather than disputes**, by
reproducing all three of its rebuild families and showing the discrepancy is a
volume convention. Its `P1` is corrected in the other direction. **No sentinel
remains anywhere in the runner or in this note.**

### Reproduction

```
python3 scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py
python3 ... --list-mutations
python3 ... --mutation break_konly_vacuity
```

Exact throughout: sympy `Rational`/`Integer` only, `DomainMatrix` over `QQ` for
rank, inverse and determinant at dimensions 48, 64 and 80, exact `factor_list`
over `Q` for every polynomial, and **no float, no tolerance and no
`sp.nsimplify` anywhere** — the last of which is *measured* in the runner's own
source by gate `H-3` rather than promised.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE PROPER OS TRANSFER — THE
WIDTH RESOLUTION**, **THE LOCALITY THEOREM SHAPE**, **THE ODD-SECTOR LOCK**,
**THE UNIT-CELL MONODROMY**, **THE DEGENERACY MECHANISM** and **THE B190 CHECK
VERDICT AND THE TWO-FORK RESOLUTION** anchors.
