# F2 (Schur/metric route) — the blind metric prediction for Block 213

**Route:** F2, independent and blind. **Deliverable:** the PREDICTION of what the
weighted kernel's principal symbol must be **if** the target contract's
hypothesis holds, plus the metric's shear dependence. **No kernel and no symbol
is constructed here** — that is another route's product.

**Framework refresher, as required.** I read COMPLETELY, before any physics:
`docs/MINIMAL_AXIOMS_2026-06-29.md` (Lattice / Qubit / Admissibility / Record,
the qualification clause, the audit-pipeline treatment, and the open-gates list)
and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (the three approved
primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`). **NO new axiom and NO new primitive is proposed,
used, or needed here.** Nothing below depends on any axiom as a premise: it is
finite exact linear algebra over `QQ` and over `QQ(tau, upsilon)` on Block 211's
own landed objects. Nothing is registered and nothing is adopted.

**Scope fence, inherited verbatim from Block 211 and not weakened.** *Scout-grade
finite exact linear algebra on one cell form, not a spacetime and not a
dynamics.* Everything called a "metric", a "cone", a "null cone" or a "symbol"
below is a finite exact algebraic object of one `8 x 8` corner matrix. **CURVED**
is nonuniform face moduli. **ORIENTATION** is a product of three shear signs.
No gravity, no continuum, no equations of motion, no claim about nature.

**Read for this work (complete):** the lane `GOAL.md`; the Block-201 note
`docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md`
and its runner
`scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py`;
the Block-211 note
`docs/ADMISSIBILITY_DIRAC_KAHLER_SIX_FACE_POSITIVITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-27.md`
and its runner
`scripts/admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27.py`;
and, for the landed 2D target only, the `shear_hodge` definition in
`scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py`
(Block 105) as re-imported by
`scripts/admissibility_dirac_kahler_local_dual_patch_descent_2026_08_15.py`
(Block 128). **I opened no other route's output**: no `specs/full_primary.log`,
no `specs/SALVAGE_*`, no draft, no log. I touched no git.

**Arithmetic controls.** Every quantity below is an exact SymPy `Integer`,
`Rational`, or symbol. The script has **zero** Python float literals (checked by
AST) and **zero** `nsimplify` calls. Every claim is a fail-closed `check(...)`
line. Baseline: **`TOTAL: PASS=59 FAIL=0`**, exit `0`.

---

## 0. The one-paragraph answer

The Schur/marginal route identifies the cell metric with the **inverse** of the
cell form's **degree-1 block** (the covariance slot), because that is the slot
Block 105's landed 2D form fills with `v * h^{-1}`. On Block 211's variety that
block is `v1 * M1` with `(M1)_{ab} = delta_{ab} - c_{ab,0}`, so

> **`g(moduli) = (v0/v1) * M1^{-1} = (1 - gamma0^2) * M1^{-1}`, and
> `g^{-1} = M1 / (1 - gamma0^2)`.**

The predicted principal symbol is therefore **proportional to `k^T M1 k`**: the
coefficient matrix of the principal part must be `M1` up to one overall scale.
The metric depends on **`(gamma0, pi0)` only** — the offset-1 shear `gamma1`
does not enter it at all, not even as a conformal factor. At every
positive-definite point of Block 211's family the metric is **Riemannian**, so
its real null cone is **`{0}`** — the falsifiable content is the complex
projective conic, i.e. proportionality of quadratic forms, and I state it that
way. There is exactly **one** fork my route cannot close from the supplied
premises: the degree-2 block supports a **second** metric registering `G1`
instead of `G0`. Applying my own rule to it (rival **A**) the two cones agree
exactly on `G0 = G1`; reading it instead as the Hodge metric slot (rival **B**)
they agree exactly on `G0 + G1 = G0 G1`. A and B themselves agree only at
`G1 = 0`, which is one more way of saying that `D` is a single-metric Hodge form
only at the flat point.

---

## 1. The objects, rebuilt rather than quoted

### 1.1 The landed 2D cell form

Block 105's target, read through Block 128's own import:

```text
shear_hodge(c, v) = diag( v,  v * [[1, c], [c, 1]]^{-1},  1/v )
                  = diag( v,  v/(1-c^2) * [[1, -c], [-c, 1]],  1/v ).
```

Slot by slot: degree 0 carries a **volume** `v`; degree 1 carries `v * h^{-1}`
with the **shape metric** `h = [[1, c],[c, 1]]`; degree 2 carries `1/v`.

### 1.2 Corners, faces, and the direction dictionary — derived, not assumed

Corner index `i in 0..7` is the subset of `{t, x, y}` with bit values
`t = 4, x = 2, y = 1`. The six coordinate faces are the three planes at two
offsets; the face `(p = {i1, i2}, offset o)` occupies the sub-corners
`[o, o+i2, o+i1, o+i1+i2]` (Block 209's order, `order_swap = False`,
`flip = False`), and Block 211 imposes that this `4 x 4` restriction of the
general symmetric `8 x 8` matrix `D` equals `shear_hodge(c_f, v_f)`.

I rebuilt that system from scratch at six independent per-face moduli and
recovered Block 211's own structural facts (checks `A1`–`A5`):

```text
96 entry equations, 36 unknowns,
coefficient matrix A carries NO moduli (free_symbols = {}),
zero columns of A = exactly {D07, D16, D25, D34},
rank A = 32,  rank [A|b] = 33 at a generic rational per-face point.
```

Solving on the per-offset-isotropic normal form (checks `A10`–`A18`) gives the
free parameters `{D07, D16, D25, D34}` and, at the degree-diagonal
representative, the four degree blocks — **with the direction dictionary read
off the solution rather than assumed**:

```text
deg-0 corner  {0}          :  v0
deg-1 corners (4, 2, 1)    == (t, x, y)          :  v1 * M1,   (M1)_ab = delta_ab - c_ab,0
deg-2 corners (3, 5, 6)    == duals of (t, x, y) :  (1/v0) * M2, (M2)_ab = delta_ab - c_ab,1
deg-3 corner  {7}          :  1/v1
corners {0, 7} decouple from all six middle corners.
```

### 1.3 The variety, in this route's own words

`v1 (1 - gamma0^2) = v0` (tie A) and `gamma1^2 = 1 - v0 v1` (tie B), hence
`v0^2 = (1-gamma0^2)(1-gamma1^2)` and `v1^2 = (1-gamma1^2)/(1-gamma0^2)`.
I work in the signed rational chart `G0 = 2 tau/(1+tau^2)`,
`G1 = 2 upsilon/(1+upsilon^2)`, where `G0 = pi0 * gamma0` and `G1 = pi1 * gamma1`
are the **signed** shears of the aligned gauge representative, and
`sqrt(1-G^2) = (1-tau^2)/(1+tau^2)` is rational (checks `A6`–`A9`).

### 1.4 Landed-literal anchors (my conventions are the landed ones)

| anchor | landed value | this rebuild |
| --- | --- | :---: |
| Block 209 all-plus `(3/5, 12/25, 3/4, 4/5)`, deg-1 spectrum | `(-3/20, 6/5, 6/5)` | **matches** (`B1`) |
| same point, deg-2 spectrum | `(-5/4, 15/4, 15/4)` | **matches** (`B2`) |
| `W1` eight leading principal minors | `15/16, 15/16, 225/256, 15/16, 25/32, 25/32, 25/36, 25/36` | **matches** (`B3`) |
| `W2` eight leading principal minors | `7/16, 7/16, 49/256, 7/16, 5/32, 5/32, 25/196, 25/196` | **matches** (`B4`) |
| `W3` eight leading principal minors | `12/25, 9/25, 108/625, 9/25, 297/2000, 891/8000, 429/6400, 143/1600` | **matches** (`B5`) |
| flat point `(0, 1)` | the `8 x 8` identity | **matches** (`B6`) |

---

## 2. The route: the Schur/marginal identification

### 2.1 Which slot is the covariance object

`shear_hodge` fills the degree-1 slot with `v h^{-1}` — an **inverse metric**
weighted by a volume. The 3D cell's degree-1 block is therefore the cell's
**covariance object**:

```text
Gamma := D[{t},{x},{y}] = v1 * M1.
```

This is **named choice 1** (§5). The degree-2 slot is the rival reading (§6).

### 2.2 The identity, and what it certifies

For any symmetric invertible `g` and any index pair `p`, the Schur identity is

```text
(g^{-1})[pp] = ( g[pp] - g[pq] g[qq]^{-1} g[qp] )^{-1} = S_p(g)^{-1}:
the plane restriction of the covariance object is the inverse of the Schur marginal.
```

Block 211's offset-0 face equations say, for each of the three coordinate planes
(check `C1`),

```text
Gamma[pp] = v0 * h_{p,0}^{-1}.
```

Writing `Gamma = nu * g^{-1}` and applying the identity gives
`S_p(g) = (nu/v0) * h_{p,0}`. So **every coordinate plane's Schur marginal is
that face's own 2D shape metric, with one universal constant** — one metric
serves all three faces simultaneously. That is not automatic; it is the content
of the offset-0 face equations, and it is what licenses calling `g` "the cell
metric" at all.

### 2.3 The route re-derives Block 211's variety (bonus, checks `C9`–`C12`)

Imposing only *"there exists ONE symmetric `3 x 3` covariance slot whose three
plane restrictions are the three faces' own objects"* reproduces the landed
variety, four lines and no semialgebraic argument:

1. corner `0` is shared by all three offset-0 faces, so the degree-0 entry is one
   number: `v_tx0 = v_ty0 = v_xy0 =: v0` (an identification, **no division**);
2. the diagonal of `Gamma` is then doubly determined —
   `v0/(1-c_tx0^2) = v0/(1-c_ty0^2) = v0/(1-c_xy0^2)` — forcing
   **per-offset shear-square isotropy**, i.e. Block 211's "no non-isotropic branch"
   for the shears;
3. that same diagonal is also the offset-1 faces' degree-0 entry `v1`, so
   `v0/(1-gamma0^2) = v1` — **that is tie A**;
4. the degree-2 diagonal read from the offset-0 faces is `1/v0`, read from the
   offset-1 faces is `v1/(1-gamma1^2)` — **that is tie B**.

**The two ties are exactly the well-definedness of the two slots.** This is an
independent corroboration of Block 211's `N1`, obtained without its cokernel
computation.

### 2.4 The metric

```text
        g = nu * Gamma^{-1},        nu = v0      (named choice 2, §5)
=>      g = (v0/v1) M1^{-1} = (1 - gamma0^2) M1^{-1},
        g^{-1} = (v1/v0) M1 = M1 / (1 - gamma0^2),      (M1)_ab = delta_ab - c_ab,0.
```

`nu = v0` is the **marginal-exact** normalisation: it is the unique scale for
which `S_p(g) = h_{p,0}` **with no leftover constant** (check `C2`), and the
named identity `(g^{-1})[pp] = S_p(g)^{-1}` is verified symbolically (check `C3`).

In the aligned gauge representative (all three offset-0 shears equal
`G := pi0 * gamma0`), with `J` the all-ones `3 x 3` matrix (checks `C4`, `C5`, `C8`):

```text
g       = (1 - G) I  +  [ G(1 - G) / (1 - 2G) ] J
g^{-1}  = [ (1 + G) I  -  G J ] / (1 - G^2)
spec(g) = { (1-G^2)/(1-2G) once,  (1-G) twice }
g is positive definite  <=>  G < 1/2
        <=>  gamma0 < 1/2 at pi0 = +1,  any gamma0 < 1 at pi0 = -1.
```

That last line is **exactly Block 211's offset-0 half of the PD classification**,
re-derived here as the definiteness of the Schur metric — an independent
corroboration that the identification is internally sound. **It does not break
the fork of §6:** check `C8` is an identity in the symbol `G`, so read at
`G = G1` it says rival A's metric is PD iff `G1 < 1/2` — Block 211's offset-1
half, by the identical argument. Each reading reproduces its own offset's
half of the landed classification, and the classification is exactly the
conjunction of the two — so positivity cannot choose between them.

**Per gauge class** (the class label `pi0` is the invariant; the individual face
signs are gauge, check `D3`, and act on `g` by a momentum-axis reflection
`k_a -> eps_a k_a`):

| class | `G = pi0 gamma0` | `g` | domain |
| :---: | :---: | --- | --- |
| `pi0 = +1` | `+gamma0` | `(1-gamma0) I + [gamma0(1-gamma0)/(1-2gamma0)] J` | PD on `gamma0 < 1/2` |
| `pi0 = -1` | `-gamma0` | `(1+gamma0) I - [gamma0(1+gamma0)/(1+2gamma0)] J` | PD on all `gamma0 < 1` |

`pi1` does not label anything in `g`.

---

## 3. (b) The predicted principal quadratic symbol

**Prediction P1.** If the target hypothesis holds with "the cell metric" read
from the covariance slot, then the principal part of the weighted kernel's
squared symbol is, up to one overall positive scale `lambda(moduli)` with
`lambda(flat) = 1`,

```text
sigma_2(k) = g^{mu nu} k_mu k_nu
           = [ sum_d k_d^2  -  2 sum_{a<b} c_{ab,0} k_a k_b ] / (1 - gamma0^2)
           = [ (1+G) |k|^2  -  G (k_t + k_x + k_y)^2 ] / (1 - G^2)   (aligned gauge).
```

Equivalently and most usably: **the coefficient matrix of the principal part must
be `M1` up to scale.** The cone-defining invariant is the single exact rational

```text
rho_1 := (off-diagonal)/(diagonal) of the coefficient matrix  =  -c_ab,0  =  -G  =  -pi0 gamma0.
```

Because the cone is scale-free, **nothing in P1 depends on named choice 2**;
only choices 1 and 3 — which block, and whether it is read as a covariance object
or a metric — move the cone, and those are the fork of §6.

**Required control (check `D0`).** At the flat point `M1 = I`, `gamma0 = 0`, so
`sigma_2 = k_t^2 + k_x^2 + k_y^2` — exactly the small-`k` limit of
`sum_d sin^2 k_d`. **PASS.**

**Two-dimensional bench, for free.** On a `(4,4)` bench in plane `p` the
predicted principal part is the plane marginal
`k^T h_{p,0}^{-1} k ∝ k_a^2 + k_b^2 - 2 c_{ab,0} k_a k_b`, which is the
restriction of the 3D prediction to `k_c = 0`. The 2D and 3D bench predictions
are consistent **by the very identity this route is named for**, so the two
benches cannot disagree without refuting the route.

### The witness table (exact rationals; aligned gauge representatives)

`v0, v1` are shown to confirm each point sits on the variety (all seven
`D-tie` checks PASS). `rho_A` and `rho_B` are the two rival readings' invariants
(§6); **bold** marks a rival that agrees with the primary at that witness.

| witness | `(G0, G1)` | `(v0, v1)` | `g` | `g^{-1}` | `sigma_2(k) * (1-G0^2)` | `spec(g^{-1})` | sig. | `det g^{-1}` | `rho_1` | `rho_A` | `rho_B` |
| --- | :---: | :---: | --- | --- | --- | --- | :---: | :---: | :---: | :---: | :---: |
| **FLAT** (control) | `(0, 0)` | `(1, 1)` | `I` | `I` | `k_t^2+k_x^2+k_y^2` | `(1,1,1)` | `(3,0)` | `1` | `0` | **`0`** | **`0`** |
| **W1** all-plus `c=1/4` | `(1/4, 1/4)` | `(15/16, 1)` | `(3/4)I + (3/8)J` = diag `9/8`, off `3/8` | diag `16/15`, off `-4/15` | `|k|^2 - (1/2)(k_tk_x+k_tk_y+k_xk_y)` | `(8/15, 4/3, 4/3)` | `(3,0)` | `128/135` | `-1/4` | **`-1/4`** | `1/3` |
| **W3** landed mags `(3/5,4/5)`, one flip per offset | `(-3/5, -4/5)` | `(12/25, 3/4)` | diag `64/55`, off `-24/55` | diag `25/16`, off `15/16` | `|k|^2 + (6/5)(k_tk_x+k_tk_y+k_xk_y)` | `(5/8, 5/8, 55/16)` | `(3,0)` | `1375/1024` | `+3/5` | `+4/5` | `-4/9` |
| **W2** deep `pi=-1`, `gamma=3/4` | `(-3/4, -3/4)` | `(7/16, 1)` | diag `49/40`, off `-21/40` | diag `16/7`, off `12/7` | `|k|^2 + (3/2)(k_tk_x+k_tk_y+k_xk_y)` | `(4/7, 4/7, 40/7)` | `(3,0)` | `640/343` | `+3/4` | **`+3/4`** | `-3/7` |
| **mixed class** `(5/13, 4/5)`, `pi=(+,-)` | `(5/13, -4/5)` | `(36/65, 13/20)` | diag `64/39`, off `40/39` | diag `169/144`, off `-65/144` | `|k|^2 - (10/13)(k_tk_x+k_tk_y+k_xk_y)` | `(13/48, 13/8, 13/8)` | `(3,0)` | `2197/3072` | `-5/13` | `+4/5` | `-4/9` |
| **B209 landed all-plus** `(3/5,4/5)` — **NOT PD** | `(3/5, 4/5)` | `(12/25, 3/4)` | diag `-4/5`, off `-6/5` | diag `25/16`, off `-15/16` | `|k|^2 - (6/5)(k_tk_x+k_tk_y+k_xk_y)` | `(-5/16, 5/2, 5/2)` | `(2,1)` | `-125/64` | `-3/5` | `-4/5` | `4` |
| **PD boundary** `G0 = G1 = 1/2` | `(1/2, 1/2)` | `(3/4, 1)` | **does not exist** (`M1` singular) | diag `4/3`, off `-2/3` | `|k|^2 - (k_tk_x+k_tk_y+k_xk_y)` | `(0, 2, 2)` | `(2,0,1)` | `0` | `-1/2` | **`-1/2`** | `1` |

The two contract witnesses `W1` and `W2` happen to sit on `G0 = G1`, where the
primary and rival A coincide **exactly** (not merely up to scale): at those two
points the offset fork does not bite. It bites hard at `W3`, at the mixed-class
point, and at Block 209's own point.

Fully written out, `sigma_2` at the four contract witnesses:

```text
FLAT :  k_t^2 + k_x^2 + k_y^2
W1   :  ( 16 k_t^2 + 16 k_x^2 + 16 k_y^2 -  8 k_t k_x -  8 k_t k_y -  8 k_x k_y ) / 15
W3   :  ( 25 k_t^2 + 25 k_x^2 + 25 k_y^2 + 30 k_t k_x + 30 k_t k_y + 30 k_x k_y ) / 16
W2   :  ( 16 k_t^2 + 16 k_x^2 + 16 k_y^2 + 24 k_t k_x + 24 k_t k_y + 24 k_x k_y ) /  7
mixed:  (169 k_t^2 +169 k_x^2 +169 k_y^2 -130 k_t k_x -130 k_t k_y -130 k_x k_y ) /144
B209 :  ( 25 k_t^2 + 25 k_x^2 + 25 k_y^2 - 30 k_t k_x - 30 k_t k_y - 30 k_x k_y ) / 16
bdry :  (  4 k_t^2 +  4 k_x^2 +  4 k_y^2 -  4 k_t k_x -  4 k_t k_y -  4 k_x k_y ) /  3
```

In a non-aligned gauge, replace `-G` by `-c_{ab,0}` entry by entry; this is the
reflection `k_a -> eps_a k_a` and changes no invariant.

---

## 4. (c) Do the shear moduli appear, and how — the separate report the GOAL asks for

**`gamma0` appears; `gamma1` does not appear at all.** (Checks `C6`, `C7`.)

- `gamma0` enters through the **signed** combination `G = pi0 gamma0`, and it is
  the whole content of the metric: `g` is a **one-parameter** family in `G`. It
  appears in the cone at first order, as the exact off/diagonal ratio
  `rho_1 = -pi0 gamma0`. So on this route **the kernel-side symbol DOES register
  shear** — the offset-0 shear, exactly and linearly.
- `gamma1` (and `pi1`) do **not** enter `g`. Not in the cone, and — under the
  marginal-exact normalisation — not even as a conformal factor: the volumes
  enter only through `v0/v1 = 1 - gamma0^2` (tie A), which is pure `gamma0`.
  Under the alternative normalisations of §5 choice 2, `gamma1` can enter as an
  **overall scale only**, never in the cone.
- **Named TENSION, recorded and not resolved here** (GOAL's planning constraint
  from PR #7970): the matter side reports `kappa(m, U) = 0` — the staggered mass
  responds to the diagonal metric and to **no** shear. My metric is
  off-diagonal (`3/8`, `-24/55`, `-21/40`, `40/39` at the four witnesses) at
  every curved point. If the kernel's cone is my cone, the kernel registers a
  shear the matter side does not. **That is a tension between two measured
  objects, not a defect in either.**

---

## 5. (a) continued — the choices Block 201/211 did **not** force

Each is a real fork; each is stated so it can be attacked separately.

1. **Which degree block is the covariance object.** Degree 1 (offset-0 faces) vs
   degree 2 (offset-1 faces). **Both** pass the Schur test exactly (checks `C1`
   and `E8`), so the premises do not choose. I take **degree 1**, because it is
   the *lowest* slot and the one the landed 2D form fills with `v h^{-1}` at the
   cell's own anchor corner. This is the fork of §6, and — with choice 3 — it is
   the only thing that changes the cone. *Nothing in Block 201 or 211 selects it.*
   A route-local expectation — that a degree-0/scalar sector's second-order
   operator reads the degree-1 weight relative to the degree-0 weight — points the
   same way, but **that is an expectation about a kernel I did not build, and is
   not offered as a derivation.**
2. **The scale `nu`.** Three natural fixings, all agreeing at flat, **all giving
   the same cone**: (A) `nu = v1` gives `g = M1^{-1}`; (B) `nu = v0`
   ("marginal-exact", my primary) gives `g = (1-gamma0^2) M1^{-1}` and is the
   unique one with `S_p(g) = h_{p,0}` exactly; (C) Hodge self-consistency
   `nu = sqrt(det g)` gives `g = v1^2 det(M1) M1^{-1} = v1^2 adj(M1)` and is the
   only one in which `gamma1` survives, as a conformal factor.
3. **Whether a block is a covariance object or a metric, and the Hodge-dual index
   map.** Needed for the rivals of §6: rival A reads the degree-2 block as a
   covariance object (my rule), rival B as the metric slot; they disagree except
   at `G1 = 0`. Both use the dual-index identification, and there is no
   orientation or wedge selector in the supplied premises — Block 211 says so and
   I inherit it.
4. **Reading `(c, v)` as (shape metric `[[1,c],[c,1]]`, independent volume).**
   This is the literal form of the landed target, so I use it. The "honest metric
   lift" reading — in which the volume would be `sqrt(det h)` — is a different
   convention, and Block 211's `N6` item 2 leaves the choice between them
   **OPEN**. Under the honest-lift reading `v^2 = 1 - c^2` and the family
   collapses; I did not take that branch.
5. **The aligned gauge representative.** Not content: every sign pattern of a
   class is a momentum-axis reflection of it (check `D3`), so the metric is
   class-defined up to the reflection group `diag(+-1,+-1,+-1)`.
6. **The four duality parameters `D07, D16, D25, D34` are set to zero.** They are
   absent from every degree block, so **the metric cannot see them at any value**.
   A kernel built from the full `D`, however, *can*. My prediction is therefore
   duality-parameter-free **by construction**, and if the exact symbol's principal
   part moves with `(a, b, c, d)` inside the open bounded PD region, the
   hypothesis fails for a reason my route cannot represent. **This is the sharpest
   named limitation of the whole note.**
7. **"The cell metric" is a metric on the three lattice directions**, contracted
   with the covector `k`. A form on the 8-dimensional corner space is not a metric
   on directions and cannot have the null cone the contract means.

---

## 6. The fork I cannot close: the degree-2 block, exactly

The offset-1 faces' in-face degree-1 blocks sit at the cell's **degree-2**
corners — and, in the Hodge-dual labelling, at the **same direction index pair**
`(a, b)` as the offset-0 ones (the face in plane `{a,b}` at offset `c` occupies
the corners `{c,a}` and `{c,b}`, whose duals are `b` and `a`). The degree-2 block
therefore carries a second, independent copy of the same structure, and there are
two ways to read it. **I could not close this from the supplied premises.**

**Rival A — my own rule, applied to the offset-1 faces** (checks `E8`–`E10`).
`(1/v0) M2` restricted to plane `p` equals `v1 h_{p,1}^{-1}` exactly, so it *is*
an offset-1 covariance object, and the marginal-exact metric is

```text
g^{(1)} = v0 v1 M2^{-1} = (1 - gamma1^2) M2^{-1},   S_p(g^{(1)}) = h_{p,1} exactly,
symbol  ∝ k^T M2 k,     rho_A = -G1 = -pi1 gamma1.
```

This is the **route-internal** rival: same rule, other offset. Its cone equals
the primary's **iff `rho_1 = rho_A` iff `G0 = G1`** — the two offsets must carry
the *same signed* shear.

**Rival B — the Hodge-slot reading.** In a Hodge convention the degree-2 slot is
`g/V`, i.e. the **metric** rather than its inverse, giving `g' ∝ M2` and

```text
symbol  ∝ k^T M2^{-1} k,   rho_B = G1/(1 - G1).
```

Its cone equals the primary's **iff `G0 + G1 = G0 G1`, i.e. `G1 = G0/(G0-1)`**
(checks `E1`–`E5`), a curve needing `G0` and `G1` of **opposite sign**, so it
lives only in the mixed classes `(+,-)` and `(-,+)`; within one orientation
class it meets the domain **only at flat**, since `G0 G1 < G0 < G0 + G1` for
`G0, G1 in (0,1)` (check `E4`).

**A and B disagree with each other except at `G1 = 0`** (check `E11`:
`-G1 = G1/(1-G1)` iff `G1(G1-2) = 0`). So the degree-2 block is a covariance
object **or** a metric, never both — which is the slot-level form of:

> **Full four-slot Hodge consistency holds only at the flat point** (checks `E6`,
> `E7`): `deg-0 = V` and `deg-3 = 1/V` force `v0 = v1`; tie A then forces
> `gamma0 = 0`; the degree-1 slot is then `v1 I`, so `g = I` and `V = 1`; tie B
> then forces `gamma1 = 0`. **Block 211's `D` is a genuine 3D Hodge cell form for
> a single metric ONLY at the flat point.**

Away from flat, *"the cell metric `g(moduli)`"* in the target contract therefore
**has no referent fixed by the supplied objects**. It is fixed only by a choice,
and this route's product is the exact menu: `rho_1 = -G0` (primary),
`rho_A = -G1`, `rho_B = G1/(1-G1)`, with the exact loci where they coincide.

**Therefore, before the other route's symbol is even read, this much is fixed:**
if the exact symbol has a single cone, at most one of the three readings can be
it at any curved point off the coincidence loci — and if the symbol's cone
**splits by degree sector**, then "the cone = the metric's cone" is false as
stated and the correct statement is a per-sector one. I expect the split; I have
not measured it, and measuring it is the other route's job.

---

## 7. (d) The null cones, exactly

For a positive-definite `g` the **real** null cone is `{0}`. That is not a
technicality here, it is the main structural fact:

> **At every positive-definite point of Block 211's family the Schur cell metric
> is Riemannian, so its real null cone is trivial.** The real null cone becomes
> non-empty **exactly** where the offset-0 PD condition fails, i.e.
> `G0 > 1/2` (check `D2`, using `max (sum k)^2/|k|^2 = 3`).

Hence, over `R`, "the characteristic cone equals the null cone of the cell
metric" is **either vacuous or false**, never informative, on the PD domain the
contract restricts to: both sides of a principal-part comparison are `{0}`, while
`sum_d sin^2 k_d` vanishes on the eight doubler points `k in (pi Z)^3`, which is
not a cone at all. **The falsifiable statement is the complex projective one:**
the principal part's coefficient matrix must be **proportional to `M1`**, i.e.
the projective conic `{k in CP^2 : k^T M1 k = 0}` must be the symbol's. I state
the prediction in that form and give the conics exactly:

Write `N = k_t^2 + k_x^2 + k_y^2` and `P = k_t k_x + k_t k_y + k_x k_y`, so
`(sum k)^2 = N + 2P`. The uniform statement is that the conic is
`(1 + G) N = G (sum k)^2`, equivalently `N = 2G P` — it has real solutions
`k != 0` iff `3G > 1 + G` iff `G > 1/2`.

| witness | `G` | real null cone of `g` | complex projective conic (cleared integers) | `det M1` |
| --- | :---: | --- | --- | :---: |
| FLAT | `0` | `{0}` | `N = 0` | `1` |
| W1 | `1/4` | `{0}` | `2N - P = 0`, i.e. `5N = (sum k)^2` | `25/32` |
| W3 | `-3/5` | `{0}` | `5N + 6P = 0`, i.e. `2N + 3(sum k)^2 = 0` | `44/125` |
| W2 | `-3/4` | `{0}` | `2N + 3P = 0`, i.e. `N + 3(sum k)^2 = 0` | `5/32` |
| mixed | `5/13` | `{0}` | `13N - 10P = 0`, i.e. `18N = 5(sum k)^2` | `972/2197` |
| **B209 non-PD** | `3/5` | **a genuine cone**: `8N = 3(k_t+k_x+k_y)^2` | `5N - 6P = 0` | `-64/125` |
| **PD boundary** | `1/2` | **a line**: `k_t = k_x = k_y`, since `sigma_2 = (2/3)[(k_t-k_x)^2+(k_t-k_y)^2+(k_x-k_y)^2]` | `N - P = 0`, i.e. `3N = (sum k)^2` — **degenerate**, rank `2` | `0` |

The cone is fixed entirely by the single invariant `rho_1 = -G`; every row above
is that one number written out.

**The edge cases the contract requires.**

- **PD boundary `gamma0 -> 1/2^-` at `pi0 = +1`:** `g` **blows up**. The `J`
  coefficient `G(1-G)/(1-2G) -> +inf`; after rescaling,
  `(1-2G) g -> J/4`, a rank-1 form: the metric degenerates by an infinite stretch
  along `(1,1,1)`. The covariance object stays finite and becomes PSD of rank 2
  with kernel `(1,1,1)`, so the real null set **jumps from `{0}` to the line
  `R(1,1,1)`**. **Rival A** degenerates identically (same rule, `G1 -> 1/2^-`).
  **Rival B** degenerates the *other* way: its rescaled symbol tends to
  `(sum k)^2`, whose real zero set is the **plane** `sum k = 0`. Line versus
  plane — the covariance and metric readings are maximally distinguishable
  exactly at the boundary, which makes `G0 = G1 = 1/2` the cheapest single test
  of choice 3.
- **A `pi = -1` class point:** `W2` at `(gamma0, gamma1) = (3/4, 3/4)`,
  `(pi0, pi1) = (-1, -1)`, far past the all-plus kill point `1/2`; `g` is PD with
  `spec(g) = (7/4, 7/4, 7/40)` and the cone is trivial. The mixed class
  `(5/13, 4/5)` with `(pi0, pi1) = (+1, -1)` is included as a second, independent
  class witness with rational volumes `(36/65, 13/20)`.
- **The non-PD contrast (not required, but decisive):** at Block 209's own
  all-plus `(3/5, 4/5)` point the Schur metric is **Lorentzian**, signature
  `(2,1)`, with a genuine real cone `8|k|^2 = 3(sum k)^2` around the `(1,1,1)`
  axis. **The only witnesses with a nontrivial real cone are the ones the
  contract's PD restriction excludes.** Any route that reports a nontrivial real
  cone at a PD point is not reporting my metric's cone.

---

## 8. How to refute me

Each item is a single exact test; none needs a float.

1. **Kill the identification.** Take the exact symbol at `W1`, expand to second
   order at `k -> 0`, and read its coefficient matrix `C`. If `C` is **not** a
   scalar multiple of `M1 = [[1,-1/4,-1/4],[-1/4,1,-1/4],[-1/4,-1/4,1]]` —
   equivalently if `off(C)/diag(C) != -1/4` — **P1 is dead at `W1`** and the
   whole route is wrong, not merely mis-normalised.
2. **Kill it by the shear it registers.** If the principal part moves with
   `gamma1` at fixed `(gamma0, pi0)` — compare `W3` `(G0,G1) = (-3/5,-4/5)`
   against any other point with `G0 = -3/5` — then the covariance slot is not
   degree 1, and a degree-2 reading (or a mixture) is right.
   Prediction: `rho_1` at both is `+3/5`.
3. **Kill it by a rival.** Use `W3`, the mixed-class point, or Block 209's point
   — the three witnesses where the readings separate. If
   `off(C)/diag(C) = rho_A = -G1` (`+4/5`, `+4/5`, `-4/5` respectively), rival A
   wins; if it is `rho_B = G1/(1-G1)` (`-4/9`, `-4/9`, `+4`), rival B wins; my
   choice 1 was then the wrong branch. **`W1` and `W2` cannot discriminate the
   primary from rival A** — they lie on `G0 = G1` — so a route that tests only
   those two has tested nothing about the fork.
4. **Kill it by no shear at all.** If `C` is a multiple of the identity at a
   curved witness, then the symbol's cone is the *flat* cone while the cell is
   curved, and *"the cone = the metric's cone"* is **refuted** for **all three**
   readings simultaneously (each coincides with `I` only at flat). This
   outcome would also *resolve* the §4 tension in the matter side's favour.
5. **Kill it by degree splitting.** If the spin-diagonalised symbol is not
   `(one quadratic form) x I` but carries different cones on different degree
   sectors, then the contract's phrase "the cell metric" has no referent away
   from flat, and the correct completion witness is my §6 menu
   `(rho_1, rho_A, rho_B)` per sector plus the exact remainder.
6. **Kill it by the duality parameters.** Vary `(a,b,c,d)` inside the open
   bounded PD box of Block 211's `N4` (`a^2 < 15/16`, `b^2, c^2, d^2 < 16/15`
   at `W1`). If the principal part moves, my metric — which cannot see them —
   is not the symbol's cone, whatever else is true. See §5 choice 6.
7. **Kill my arithmetic.** Re-run the script. It reproduces Block 209's two
   landed spectra and all three landed witness minor lists; if any of those
   fail, my corner dictionary (`t=4, x=2, y=1`; degree-2 corners `3,5,6` dual to
   `t,x,y`) is wrong and every matrix above shifts with it.
8. **Kill the boundary claim.** At `G0 = 1/2` I predict the real null set is the
   line `k_t = k_x = k_y` and that `det(g^{-1}) = 0`. A symbol whose principal
   part stays nondegenerate as `gamma0 -> 1/2^-` at `pi0 = +1` refutes the
   identification at the boundary even if it holds in the interior.

**What would NOT refute me:** disagreement in the overall scale `lambda(moduli)`
(choice 2 is free, and the cone is scale-free); disagreement in the
higher-than-quadratic remainder (I predict nothing there); disagreement about
which sign pattern in a class is used (gauge, check `D3`).

---

## 9. What this note does and does not supply

**Supplied:** an exact metric formula on Block 211's variety, its per-class form,
its PD region (matching the landed offset-0 classification), the exact principal
symbol it forces, its exact cones at seven moduli points, the exact shear
dependence, the exact discriminants among the three readings of the two blocks,
and the exact statement that `D` is a single-metric Hodge form only at flat.

**Not supplied:** any kernel; any symbol of any kernel; any dynamics, energy,
mass, gravity, spacetime, curvature, continuum limit, or claim about nature; any
selector among the three readings; any statement about oblique faces; any
statement about the shape-rule-versus-honest-lift question, which Block 211
leaves open and this note does not touch. **Every negative here is non-supply
within this formalism and never metaphysical necessity.**

---

## 10. Check ledger — `TOTAL: PASS=59 FAIL=0`

| family | checks | content | status |
| --- | :---: | --- | :---: |
| `A` | 19 (`A0`–`A18`) | independent rebuild of the six-face system; `96`/`36`, constant integer `A`, zero columns `{D07,D16,D25,D34}`, `rank 32`, generic `rank[A|b] = 33`; the chart and both ties; consistency at rank `32`; the four free parameters; the direction dictionary; the four degree blocks; `{0,7}` decoupling | ALL PASS |
| `B` | 6 (`B1`–`B6`) | landed literals: both Block 209 spectra; `W1`, `W2`, `W3` eight-minor lists; the flat identity | ALL PASS |
| `C` | 12 (`C1`–`C12`) | `Gamma[pp] = v0 h^{-1}`; `S_p(g) = h_p` exactly; the named identity `(g^{-1})[pp] = S_p^{-1}`; the closed forms; no `gamma1` in `g`; `v0/v1 = 1-gamma0^2`; `spec(g)`; the four-line re-derivation of the variety | ALL PASS |
| `D` | 11 (7 tie + `D0`–`D3`) | every witness on the variety; the flat control `sum_d k_d^2`; the aligned closed form; real cone non-empty iff `G0 > 1/2`; gauge = axis reflections | ALL PASS |
| `E` | 11 (`E1`–`E11`) | `M1 M2 = lambda I + mu J`; the three cone invariants `rho_1, rho_A, rho_B`; both agreement loci (`G0 = G1` and `G0+G1 = G0G1`); same-sign impossibility for the latter; the degree-2 block IS an offset-1 covariance object and its marginal-exact metric; A-vs-B only at `G1 = 0`; full Hodge consistency only at flat | ALL PASS |

Reproduce: `python3 f2_schur_metric.py` (exit `0`, `~40 s`). AST-verified: `0`
float literals, `0` `nsimplify` calls.

---

## 11. The script, inline and complete

```python
#!/usr/bin/env python3
"""F2 blind route (Block 213): Schur/marginal identification of the cell metric.

Independent route product: the metric g(moduli) predicted from Block 211's
cell form by the Schur-marginal identity (g^{-1})[pp] = S_p(g)^{-1}, and the
principal quadratic symbol g^{mu nu} k_mu k_nu it forces.  No kernel is built.

Exact only: sympy Rational/symbol.  No floats.  Fail-closed asserts.
"""
import sys

import sympy as sp

PASSES = []
FAILS = []


def check(name, cond, detail=""):
    ok = bool(cond)
    (PASSES if ok else FAILS).append(name)
    print(("[PASS] " if ok else "[FAIL] ") + name + (("  " + str(detail)) if detail else ""))
    return ok


# ------------------------------------------------------------------ conventions
# corner index i in 0..7 <-> subset of {t,x,y}.  bit values: t=4, x=2, y=1.
BIT = {"t": 4, "x": 2, "y": 1}
DIRS = ["t", "x", "y"]
PLANES = [("t", "x"), ("t", "y"), ("x", "y")]
PLABEL = {("t", "x"): "tx", ("t", "y"): "ty", ("x", "y"): "xy"}


def shear_hodge(c, v):
    """Block 105's landed 2D cell form, read through Block 128's own import."""
    metric = sp.Matrix([[1, c], [c, 1]])
    return sp.diag(v, v * metric.inv(), 1 / v)


def face_corners(plane, offset_bit):
    """Block 209 sub-corner order [o, o+i2, o+i1, o+i1+i2]."""
    a, b = plane
    i1, i2 = BIT[a], BIT[b]
    o = offset_bit
    return [o, o ^ i2, o ^ i1, o ^ i1 ^ i2]


def faces():
    """six coordinate faces: (plane, offset index 0/1, offset corner bit)."""
    out = []
    for plane in PLANES:
        third = [d for d in DIRS if d not in plane][0]
        out.append((plane, 0, 0))
        out.append((plane, 1, BIT[third]))
    return out


# ------------------------------------------------- A. rebuild the six-face system
print("=" * 78)
print("A. INDEPENDENT REBUILD OF THE SIX-FACE SYSTEM (convention anchor)")
print("=" * 78)

d = {}
unknowns = []
for i in range(8):
    for j in range(i, 8):
        s = sp.Symbol(f"D{i}{j}")
        d[(i, j)] = s
        d[(j, i)] = s
        unknowns.append(s)
D = sp.Matrix(8, 8, lambda i, j: d[(i, j)])
check("A0 unknowns = 36 (symmetric 8x8)", len(unknowns) == 36, len(unknowns))

cs, vs = {}, {}
for plane, off, _bit in faces():
    cs[(plane, off)] = sp.Symbol(f"c_{PLABEL[plane]}{off}")
    vs[(plane, off)] = sp.Symbol(f"v_{PLABEL[plane]}{off}")

eqs = []
for plane, off, bit in faces():
    corners = face_corners(plane, bit)
    target = shear_hodge(cs[(plane, off)], vs[(plane, off)])
    for a in range(4):
        for b in range(4):
            eqs.append(D[corners[a], corners[b]] - target[a, b])
check("A1 equation count = 96", len(eqs) == 96, len(eqs))

A, b = sp.linear_eq_to_matrix(eqs, unknowns)
check("A2 coefficient matrix carries NO moduli", A.free_symbols == set(), sorted(map(str, A.free_symbols)))
zero_cols = [unknowns[j] for j in range(A.cols) if all(A[i, j] == 0 for i in range(A.rows))]
check("A3 zero columns = {D07,D16,D25,D34}",
      sorted(map(str, zero_cols)) == ["D07", "D16", "D25", "D34"], sorted(map(str, zero_cols)))
rankA = A.rank()
check("A4 rank(A) = 32", rankA == 32, rankA)

generic = {}
for k, (plane, off) in enumerate([(p, o) for p in PLANES for o in (0, 1)]):
    generic[cs[(plane, off)]] = sp.Rational(1, 3 + k)
    generic[vs[(plane, off)]] = sp.Rational(2 + k, 5)
Ab = A.row_join(b).subs(generic)
rankAb = Ab.rank()
check("A5 rank([A|b]) = 33 at a generic rational per-face point (=> generic rank 33)",
      rankAb == 33, rankAb)

# ---------------------------------------- the per-offset-isotropic normal form
tau, ups = sp.symbols("tau upsilon")           # rational chart, signed
G0 = 2 * tau / (1 + tau ** 2)                  # signed offset-0 shear  (= pi0 * gamma0)
G1 = 2 * ups / (1 + ups ** 2)                  # signed offset-1 shear  (= pi1 * gamma1)
r0 = (1 - tau ** 2) / (1 + tau ** 2)           # = sqrt(1 - G0^2) on |tau| < 1
r1 = (1 - ups ** 2) / (1 + ups ** 2)           # = sqrt(1 - G1^2)
V0 = sp.simplify(r0 * r1)                      # v0 = sqrt((1-G0^2)(1-G1^2))
V1 = sp.simplify(r1 / r0)                      # v1 = sqrt((1-G1^2)/(1-G0^2))
check("A6 chart: r0^2 = 1-G0^2", sp.simplify(r0 ** 2 - (1 - G0 ** 2)) == 0)
check("A7 chart: r1^2 = 1-G1^2", sp.simplify(r1 ** 2 - (1 - G1 ** 2)) == 0)
check("A8 tie A: v1 (1-G0^2) = v0", sp.simplify(V1 * (1 - G0 ** 2) - V0) == 0)
check("A9 tie B: G1^2 = 1 - v0 v1", sp.simplify(G1 ** 2 - (1 - V0 * V1)) == 0)

iso = {}
for plane, off, _bit in faces():
    iso[cs[(plane, off)]] = G0 if off == 0 else G1
    iso[vs[(plane, off)]] = V0 if off == 0 else V1

A_iso = A
b_iso = sp.simplify(b.subs(iso))
Ab_iso = sp.simplify(A_iso.row_join(b_iso))
check("A10 on the isotropic aligned normal form the system is CONSISTENT (rank 32)",
      Ab_iso.rank() == 32, Ab_iso.rank())

sol = sp.solve([sp.Eq(e, 0) for e in (A_iso * sp.Matrix(unknowns) - b_iso)], unknowns, dict=True)
assert len(sol) == 1
sol = sol[0]
free = [u for u in unknowns if u not in sol]
check("A11 free parameters are exactly the four duality pairings",
      sorted(map(str, free)) == ["D07", "D16", "D25", "D34"], sorted(map(str, free)))

# degree-diagonal representative: the four duality parameters set to zero
rep = {u: sp.Integer(0) for u in free}
Dsol = sp.simplify(D.subs(sol).subs(rep))

DEG1 = [BIT["t"], BIT["x"], BIT["y"]]              # corners 4, 2, 1  (1-forms t,x,y)
DEG2 = [7 ^ BIT["t"], 7 ^ BIT["x"], 7 ^ BIT["y"]]  # corners 3, 5, 6 (2-forms dual to t,x,y)
check("A12 degree-1 corners in (t,x,y) order = (4,2,1)", DEG1 == [4, 2, 1], DEG1)
check("A13 degree-2 corners in dual (t,x,y) order = (3,5,6)", DEG2 == [3, 5, 6], DEG2)

Gamma = sp.simplify(Dsol[DEG1, DEG1])            # the covariance slot
Delta = sp.simplify(Dsol[DEG2, DEG2])            # the metric slot
J3 = sp.ones(3, 3)
I3 = sp.eye(3)
M1 = sp.simplify((1 + G0) * I3 - G0 * J3)
M2 = sp.simplify((1 + G1) * I3 - G1 * J3)
check("A14 deg-0 entry = v0", sp.simplify(Dsol[0, 0] - V0) == 0)
check("A15 deg-3 entry = 1/v1", sp.simplify(Dsol[7, 7] - 1 / V1) == 0)
check("A16 deg-1 block = v1 * M1 (M1 = I - offset-0 shear pattern)",
      sp.simplify(Gamma - V1 * M1) == sp.zeros(3, 3))
check("A17 deg-2 block = (1/v0) * M2 (dual index order)",
      sp.simplify(Delta - M2 / V0) == sp.zeros(3, 3))
check("A18 corners {0,7} decouple from the six middle corners",
      all(sp.simplify(Dsol[c, m]) == 0 for c in (0, 7) for m in (1, 2, 3, 4, 5, 6)))

# ------------------------------------------------ B. landed-literal cross checks
print()
print("=" * 78)
print("B. LANDED-LITERAL CROSS CHECKS (Block 209 / Block 211 numbers)")
print("=" * 78)


def at(g0s, g1s, v0v, v1v, signs0=None, signs1=None):
    """Build D at an exact rational moduli point (signed shears, aligned gauge
    unless explicit sign triples are given)."""
    s0 = signs0 if signs0 else [1, 1, 1]
    s1 = signs1 if signs1 else [1, 1, 1]
    sub = {}
    for k, plane in enumerate(PLANES):
        sub[cs[(plane, 0)]] = sp.Integer(s0[k]) * g0s
        sub[cs[(plane, 1)]] = sp.Integer(s1[k]) * g1s
        sub[vs[(plane, 0)]] = v0v
        sub[vs[(plane, 1)]] = v1v
    Apt, bpt = A, b.subs(sub)
    assert Apt.row_join(bpt).rank() == 32, "point is OFF the compatible variety"
    s = sp.solve([sp.Eq(e, 0) for e in (Apt * sp.Matrix(unknowns) - bpt)], unknowns, dict=True)[0]
    Dp = D.subs(s).subs({u: sp.Integer(0) for u in unknowns if u not in s})
    return sp.Matrix(8, 8, lambda i, j: sp.together(Dp[i, j]))


def spectrum(M):
    out = []
    for val, mult in sp.Matrix(M).eigenvals().items():
        out.extend([sp.simplify(val)] * mult)
    return sorted(out, key=lambda z: sp.Rational(z))


def minors8(M):
    return [sp.factor(sp.Matrix(M)[:n, :n].det()) for n in range(1, 9)]


D209 = at(sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(12, 25), sp.Rational(3, 4))
check("B1 Block 209 all-plus point: deg-1 spectrum = (-3/20, 6/5, 6/5)",
      spectrum(D209[DEG1, DEG1]) == [sp.Rational(-3, 20), sp.Rational(6, 5), sp.Rational(6, 5)],
      spectrum(D209[DEG1, DEG1]))
check("B2 Block 209 all-plus point: deg-2 spectrum = (-5/4, 15/4, 15/4)",
      spectrum(D209[DEG2, DEG2]) == [sp.Rational(-5, 4), sp.Rational(15, 4), sp.Rational(15, 4)],
      spectrum(D209[DEG2, DEG2]))

DW1 = at(sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(15, 16), sp.Integer(1))
want = [sp.Rational(15, 16), sp.Rational(15, 16), sp.Rational(225, 256), sp.Rational(15, 16),
        sp.Rational(25, 32), sp.Rational(25, 32), sp.Rational(25, 36), sp.Rational(25, 36)]
check("B3 W1 eight leading principal minors match the landed list", minors8(DW1) == want, minors8(DW1))

DW2 = at(sp.Rational(3, 4), sp.Rational(3, 4), sp.Rational(7, 16), sp.Integer(1),
         signs0=[-1, -1, -1], signs1=[-1, -1, -1])
want2 = [sp.Rational(7, 16), sp.Rational(7, 16), sp.Rational(49, 256), sp.Rational(7, 16),
         sp.Rational(5, 32), sp.Rational(5, 32), sp.Rational(25, 196), sp.Rational(25, 196)]
check("B4 W2 eight leading principal minors match the landed list", minors8(DW2) == want2, minors8(DW2))

DW3 = at(sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(12, 25), sp.Rational(3, 4),
         signs0=[1, 1, -1], signs1=[1, 1, -1])
want3 = [sp.Rational(12, 25), sp.Rational(9, 25), sp.Rational(108, 625), sp.Rational(9, 25),
         sp.Rational(297, 2000), sp.Rational(891, 8000), sp.Rational(429, 6400), sp.Rational(143, 1600)]
check("B5 W3 (landed magnitudes, one flip per offset) minors match the landed list",
      minors8(DW3) == want3, minors8(DW3))

DFLAT = at(sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(1))
check("B6 flat point returns the 8x8 identity", DFLAT == sp.eye(8))

# --------------------------------------------------- C. the Schur/marginal route
print()
print("=" * 78)
print("C. THE SCHUR/MARGINAL DERIVATION (this route's own content)")
print("=" * 78)


def schur(M, keep):
    """Schur marginal S_p(M) = M[pp] - M[pq] M[qq]^-1 M[qp]."""
    drop = [i for i in range(M.rows) if i not in keep]
    App = M[keep, keep]
    Apq = M[keep, drop]
    Aqq = M[drop, drop]
    return sp.simplify(App - Apq * Aqq.inv() * Apq.T)


# C1: the plane restriction of the covariance slot IS the face's own object
ok = True
for k, plane in enumerate(PLANES):
    keep = sorted([DIRS.index(plane[0]), DIRS.index(plane[1])])
    h = sp.Matrix([[1, G0], [G0, 1]])
    ok &= sp.simplify(Gamma[keep, keep] - V0 * h.inv()) == sp.zeros(2, 2)
check("C1 Gamma[pp] = v0 * h_p0^{-1} for all three coordinate planes (offset-0 faces)", ok)

# C2: the marginal-exact metric.  g := nu * Gamma^{-1}, nu = v0.
nu = V0
g = sp.simplify(nu * Gamma.inv())
ginv = sp.simplify(g.inv())
ok = True
for plane in PLANES:
    keep = sorted([DIRS.index(plane[0]), DIRS.index(plane[1])])
    h = sp.Matrix([[1, G0], [G0, 1]])
    ok &= sp.simplify(schur(g, keep) - h) == sp.zeros(2, 2)
check("C2 S_p(g) = h_p0 EXACTLY for all three planes (marginal-exact normalisation nu = v0)", ok)

ok = True
for plane in PLANES:
    keep = sorted([DIRS.index(plane[0]), DIRS.index(plane[1])])
    ok &= sp.simplify(ginv[keep, keep] - schur(g, keep).inv()) == sp.zeros(2, 2)
check("C3 the named identity (g^{-1})[pp] = S_p(g)^{-1} holds", ok)

# C4: closed form  g = (1-G) I + G(1-G)/(1-2G) J
Gs = sp.Symbol("G")
g_closed = (1 - Gs) * I3 + Gs * (1 - Gs) / (1 - 2 * Gs) * J3
check("C4 closed form g = (1-G) I + [G(1-G)/(1-2G)] J,  G = pi0*gamma0",
      sp.simplify(g - g_closed.subs(Gs, G0)) == sp.zeros(3, 3))
check("C5 g^{-1} = [(1+G) I - G J] / (1-G^2)  (= M1 / (1-G^2))",
      sp.simplify(ginv - M1 / (1 - G0 ** 2)) == sp.zeros(3, 3))
check("C6 g does NOT contain the offset-1 shear (no upsilon anywhere)",
      ups not in sp.simplify(g).free_symbols, sorted(map(str, sp.simplify(g).free_symbols)))
check("C7 the volumes enter only through v0/v1 = 1-G0^2",
      sp.simplify(V0 / V1 - (1 - G0 ** 2)) == 0)

# C8: eigenvalues of g and the PD criterion  <=>  Block 211's offset-0 condition
gg = g_closed
ev = sp.Matrix(gg).eigenvals()
check("C8 spec(g) = { (1-G^2)/(1-2G) once, (1-G) twice }",
      {sp.simplify(k): v for k, v in ev.items()} ==
      {sp.simplify((1 - Gs ** 2) / (1 - 2 * Gs)): 1, sp.simplify(1 - Gs): 2},
      {sp.simplify(k): v for k, v in ev.items()})

# C9-C12: the marginal system's own consistency conditions reproduce Block 211's variety,
#     imposing ONLY "there is ONE symmetric 3x3 covariance slot Gamma whose three plane
#     restrictions are the three offset-0 face objects" (and the dual statement).
ctx, cty, cxy = sp.symbols("ctx cty cxy")
# step 1: corner 0 is shared by all three offset-0 faces => the deg-0 entry is ONE number.
check("C9 volume equalisation is an identification of the shared deg-0 corner (no division)",
      len({face_corners(p, 0)[0] for p in PLANES}) == 1, {face_corners(p, 0)[0] for p in PLANES})
# step 2: with v_f0 = v0 the diagonal of Gamma is doubly determined => shear squares equalise.
v0s = sp.Symbol("v0s", positive=True)
diag_from = {("t", "x"): v0s / (1 - ctx ** 2),
             ("t", "y"): v0s / (1 - cty ** 2),
             ("x", "y"): v0s / (1 - cxy ** 2)}
cons = []
for a in DIRS:
    vals = [diag_from[p] for p in PLANES if a in p]
    cons.append(sp.numer(sp.together(sp.simplify(vals[0] - vals[1]))))
sol_iso = sp.solve(cons, [ctx, cty], dict=True)
check("C10 well-definedness of the covariance diagonal forces per-offset shear-square isotropy",
      all(sp.simplify(s[ctx] ** 2 - cxy ** 2) == 0 and sp.simplify(s[cty] ** 2 - cxy ** 2) == 0
          for s in sol_iso) and len(sol_iso) > 0, sol_iso)
# step 3: the deg-1 DIAGONAL is also pinned by the offset-1 faces' deg-0 entry (= v1) => tie A.
tieA = sp.simplify(V0 / (1 - G0 ** 2) - V1)
check("C11 tie A is 'the covariance diagonal read from offset-0 = the one read from offset-1'",
      tieA == 0, tieA)
# step 4: the deg-2 diagonal read from offset-0 faces (1/v0) = the one read from offset-1
#         faces (v1/(1-G1^2))  => tie B.
tieB = sp.simplify(1 / V0 - V1 / (1 - G1 ** 2))
check("C12 tie B is the same statement for the deg-2 slot", tieB == 0, tieB)

# ------------------------------------------------------- D. the witness table
print()
print("=" * 78)
print("D. WITNESS TABLE — exact metric, symbol, cone")
print("=" * 78)
kt, kx, ky = sp.symbols("k_t k_x k_y")
kvec = sp.Matrix([kt, kx, ky])

WITNESSES = [
    ("FLAT control        (G0,G1)=(0,0)",        sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(1)),
    ("W1 all-plus         g=1/4, pi=(+,+)",      sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(15, 16), sp.Integer(1)),
    ("W3 landed mags flip (3/5,4/5), pi=(-,-)",  sp.Rational(-3, 5), sp.Rational(-4, 5), sp.Rational(12, 25), sp.Rational(3, 4)),
    ("W2 deep pi=-1       g=3/4, pi=(-,-)",      sp.Rational(-3, 4), sp.Rational(-3, 4), sp.Rational(7, 16), sp.Integer(1)),
    ("Mixed class         (5/13,4/5), pi=(+,-)", sp.Rational(5, 13), sp.Rational(-4, 5), sp.Rational(36, 65), sp.Rational(13, 20)),
    ("B209 landed all-plus (3/5,4/5) NOT PD",    sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(12, 25), sp.Rational(3, 4)),
    ("PD boundary         G0=G1=1/2",            sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(3, 4), sp.Integer(1)),
]

rows = []
for label, g0v, g1v, v0v, v1v in WITNESSES:
    tieA = sp.simplify(v1v * (1 - g0v ** 2) - v0v)
    tieB = sp.simplify(g1v ** 2 - (1 - v0v * v1v))
    check(f"D-tie {label}: on the Block-211 variety", tieA == 0 and tieB == 0, (tieA, tieB))
    M1v = (1 + g0v) * I3 - g0v * J3
    M2v = (1 + g1v) * I3 - g1v * J3
    ginv_v = sp.simplify(M1v / (1 - g0v ** 2))
    if sp.simplify(sp.Matrix(M1v).det()) != 0:
        g_v = sp.simplify(sp.Matrix(ginv_v).inv())
    else:
        g_v = None
    Q = sp.expand(sp.simplify((kvec.T * ginv_v * kvec)[0, 0]))
    spec_ginv = spectrum(ginv_v)
    signature = (sum(1 for e in spec_ginv if e > 0), sum(1 for e in spec_ginv if e < 0),
                 sum(1 for e in spec_ginv if e == 0))
    Qdual = sp.expand(sp.simplify((kvec.T * sp.Matrix(M2v).inv() * kvec)[0, 0])) if sp.Matrix(M2v).det() != 0 else None
    prop = sp.simplify(sp.Matrix(M1v) * sp.Matrix(M2v))
    lam = sp.simplify(prop[0, 0])
    prop_scalar = sp.simplify(prop - lam * I3) == sp.zeros(3, 3)
    rows.append((label, g_v, ginv_v, Q, spec_ginv, signature, Qdual, prop_scalar, sp.simplify(sp.Matrix(ginv_v).det())))
    print()
    print("-" * 70)
    print(label)
    print("  g (marginal-exact, nu=v0)      =", None if g_v is None else list(g_v))
    print("  g^{-1} = M1/(1-G0^2)           =", list(ginv_v))
    print("  sigma_2(k) = g^{mu nu}k_mu k_nu=", Q)
    print("  spec(g^{-1})                   =", spec_ginv, " signature (+,-,0) =", signature)
    print("  det(g^{-1})                    =", sp.simplify(sp.Matrix(ginv_v).det()))
    print("  deg-2 (offset-1) rival symbol  =", Qdual)
    print("  M1*M2 scalar? (cones agree)    =", prop_scalar)

check("D0 FLAT control: sigma_2 = k_t^2 + k_x^2 + k_y^2",
      sp.simplify(rows[0][3] - (kt ** 2 + kx ** 2 + ky ** 2)) == 0, rows[0][3])

Gv = sp.Symbol("Gv")
Qgen = sp.expand(((1 + Gv) * (kt ** 2 + kx ** 2 + ky ** 2) - Gv * (kt + kx + ky) ** 2) / (1 - Gv ** 2))
check("D1 aligned-gauge closed form: sigma_2 = [(1+G)|k|^2 - G (sum k)^2] / (1-G^2)",
      all(sp.simplify(Qgen.subs(Gv, gv) - row[3]) == 0
          for gv, row in zip([w[1] for w in WITNESSES], rows)))
check("D2 the real null cone is non-empty  <=>  G0 > 1/2  <=>  offset-0 PD FAILS "
      "(max of (sum k)^2/|k|^2 is 3)",
      all(((sp.Rational(1, 20) * i) > sp.Rational(1, 2))
          == (1 + sp.Rational(1, 20) * i - 3 * sp.Rational(1, 20) * i < 0)
          for i in range(1, 20)))


# gauge covariance: EVERY sign pattern with product pi0 is a momentum-axis reflection
# of the aligned representative (so the metric is class-defined up to axis reflections).
def m1_of(signs, gmag):
    c = {("t", "x"): signs[0] * gmag, ("t", "y"): signs[1] * gmag, ("x", "y"): signs[2] * gmag}
    M = sp.eye(3)
    for (a, bb), val in c.items():
        M[DIRS.index(a), DIRS.index(bb)] = -val
        M[DIRS.index(bb), DIRS.index(a)] = -val
    return M


gmag = sp.Rational(3, 5)
ok = True
for signs in [(1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1)]:          # pi0 = -1 cell
    target = m1_of(signs, gmag)
    aligned = m1_of((-1, -1, -1), gmag)
    hit = any(sp.simplify(sp.diag(*e) * aligned * sp.diag(*e) - target) == sp.zeros(3, 3)
              for e in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1),
                        (1, -1, -1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)])
    ok &= hit
check("D3 corner-sign gauge acts on the metric by a momentum-axis reflection: every "
      "sign pattern of a class is an eps-conjugate of the aligned representative", ok)

# ------------------------------------------------------- E. the fork and no-goes
print()
print("=" * 78)
print("E. THE FORK: deg-1 vs deg-2, and full Hodge consistency")
print("=" * 78)
a0, a1 = sp.symbols("G0 G1")           # signed shears, treated as free coordinates
M1a = (1 + a0) * I3 - a0 * J3
M2a = (1 + a1) * I3 - a1 * J3
prodJ = sp.expand(M1a * M2a)
lam = sp.simplify(prodJ[0, 0] - prodJ[0, 1])
off = sp.simplify(prodJ[0, 1])
check("E1 M1*M2 = lam*I + mu*J with mu = -(G0 + G1 - G0 G1)",
      sp.simplify(off + (a0 + a1 - a0 * a1)) == 0, off)
# cone invariant rho = off-diagonal / diagonal of the symbol's coefficient matrix
rho1 = sp.simplify(-a0)
rho2 = sp.simplify(sp.Matrix(M2a).inv()[0, 1] / sp.Matrix(M2a).inv()[0, 0])
check("E2 cone invariants: rho1 = -G0 (offset-0 route), rho2 = G1/(1-G1) (offset-1 route)",
      sp.simplify(rho2 - a1 / (1 - a1)) == 0, (rho1, rho2))
check("E3 rho1 = rho2 <=> G0 + G1 = G0 G1 (the cone-agreement curve)",
      sp.simplify(sp.factor(sp.numer(sp.together(rho1 - rho2))) + (a0 + a1 - a0 * a1)) == 0
      or sp.simplify(sp.factor(sp.numer(sp.together(rho1 - rho2))) - (a0 + a1 - a0 * a1)) == 0,
      sp.factor(sp.numer(sp.together(rho1 - rho2))))
check("E4 same-sign (one orientation class) => the curve meets the domain only at flat: "
      "for G0,G1 in (0,1), G0 G1 < G0 < G0+G1",
      all(sp.Rational(i, 12) * sp.Rational(j, 12) < sp.Rational(i, 12) + sp.Rational(j, 12)
          for i in range(1, 12) for j in range(1, 12)))
sample = sp.solve(sp.Eq(a0 + a1 - a0 * a1, 0), a1)[0]
check("E5 agreement curve solved: G1 = G0/(G0-1) (opposite signs, so classes (+,-) and (-,+) only)",
      sp.simplify(sample - a0 / (a0 - 1)) == 0, sample)

# E8-E11: the ROUTE-INTERNAL rival.  Applying THIS route's own rule to the offset-1
#     faces: their in-face degree-1 blocks sit at the cell's degree-2 corners and, in the
#     Hodge-dual index labelling, at the SAME direction index pair.  So (1/v0) M2 is an
#     offset-1 covariance object and the marginal-exact metric is g1 = v0 v1 M2^{-1}.
ok = True
for plane in PLANES:
    keep = sorted([DIRS.index(plane[0]), DIRS.index(plane[1])])
    h1 = sp.Matrix([[1, G1], [G1, 1]])
    ok &= sp.simplify(Delta[keep, keep] - V1 * h1.inv()) == sp.zeros(2, 2)
check("E8 (1/v0)M2[pp] = v1 * h_p1^{-1}: the deg-2 block IS an offset-1 covariance object "
      "in the dual index labelling", ok)
g1met = sp.simplify(V1 * Delta.inv())
ok = True
for plane in PLANES:
    keep = sorted([DIRS.index(plane[0]), DIRS.index(plane[1])])
    h1 = sp.Matrix([[1, G1], [G1, 1]])
    ok &= sp.simplify(schur(g1met, keep) - h1) == sp.zeros(2, 2)
check("E9 route-internal rival: S_p(g1) = h_p1 exactly, g1 = v0 v1 M2^{-1} = (1-gamma1^2) M2^{-1}",
      ok and sp.simplify(g1met - (1 - G1 ** 2) * sp.Matrix(M2).inv()) == sp.zeros(3, 3))
check("E10 rival-A cone invariant is rho_A = -G1 (so its symbol is k^T M2 k up to scale); "
      "rho_1 = rho_A  <=>  G0 = G1",
      sp.simplify(sp.Matrix(M2)[0, 1] / sp.Matrix(M2)[0, 0] + G1) == 0)
check("E11 rival-A and rival-B (the Hodge-slot reading) agree only at G1 = 0: "
      "-G1 = G1/(1-G1) <=> G1(G1-2) = 0",
      sp.solve(sp.Eq(-a1, a1 / (1 - a1)), a1) == [0, 2],
      sp.solve(sp.Eq(-a1, a1 / (1 - a1)), a1))

# full 4-slot Hodge consistency: deg-0 = V, deg-1 = V g^{-1}, deg-2 = g/V, deg-3 = 1/V
step1 = sp.solve(sp.Eq(V0, V1), tau)                    # deg-0 = V and deg-3 = 1/V  =>  v0 = v1
check("E6 full Hodge step 1: deg-0/deg-3 force v0 = v1, and tie A then forces G0 = 0",
      step1 == [0], step1)
step2 = sp.solve(sp.Eq(G1 ** 2, 1 - V0 * V1).subs(tau, 0), ups)   # tie B at G0 = 0, v0 = v1 = 1
check("E7 full Hodge step 2: with G0 = 0 the deg-1 slot is v1*I so g = I, V = 1, v0 = v1 = 1, "
      "and tie B then forces G1 = 0  =>  FLAT ONLY",
      sp.solve(sp.Eq(V0.subs(tau, 0), 1), ups) == [0],
      (step2, sp.solve(sp.Eq(V0.subs(tau, 0), 1), ups)))

print()
print("=" * 78)
print(f"TOTAL: PASS={len(PASSES)} FAIL={len(FAILS)}")
print("=" * 78)
if FAILS:
    print("FAILED:", FAILS)
    sys.exit(1)
```
