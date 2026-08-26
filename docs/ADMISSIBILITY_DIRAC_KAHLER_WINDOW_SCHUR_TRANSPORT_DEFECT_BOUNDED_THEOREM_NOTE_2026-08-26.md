---
title: "Admissibility — Dirac-Kähler Window-Schur Transport Defect: The Constructive Half Of The Parity Window Law"
date: 2026-08-26
block: 196
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_window_schur_transport_defect_2026_08_26.py
parent_ref: origin/physics-loop/toe-axiom-closure-block195-sectored-interior-os-reconstruction-20260825
parent_commit: 7877b4afac1363b80ac37a28c90182c811f01da1
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# The Window-Schur Transport Defect — the transport-defect functionals of a core are the unique solutions of a twelve-row window-restricted system, that solution is Block 193's mechanism object, and two exact containments turn the compatibility half of Block 193's window law into a theorem, with WINDOW, TRANSPORT, UNIQUE and PROOF fenced as names for matrix properties throughout

**One sentence.** On Block 190's width family at `T = 16` and `T = 20`, at every
one of the twelve valid cores and at both rational points, the `s`-step
transport-defect functional `d_b^(s)` lies in the image of the twelve-column
restriction `A = Q^T[:, J(t0)]`, that restriction has exact rank `12` so the
window-supported solution is **unique**, padding it reproduces Block 193's
`u_b = G^T d_b` **entrywise**, the twelve rows are **exhaustively minimal** for
the two-step and joint families while the one-step family collapses to **four**
at even cores, and the two exact containments `supp(u_b) ⊆ J` **and**
`supp(D_s u_b) ⊆ J` make the **compatibility** direction of Block 193's window
law a **proof** — while the **breaking** direction remains Block 193's censuses,
nothing here is a width induction, and not one line of it supplies gravity.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Six imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE PROOF LANGUAGE IS FENCED BEFORE THE FIRST NUMBER IS READ.**

- **NO GRAVITY IS SUPPLIED.** This block supplies no lapse variable in an ADM
  phase space, no shift vector, no Hamiltonian constraint, no momentum
  constraint, no first-class constraint algebra, no Dirac closure, no Dirac
  observable, no gauge orbit and no diffeomorphism quotient. Nine structures,
  enumerated as a measured constant and gated.
- **NO WIDTH INDUCTION.** The system is solved **separately** at each of the
  twelve cores of `T = 16` and `T = 20`. Nothing propagates from one width to
  the other and no statement is made about any other even `T`. Asserting
  otherwise is a declared mutation (`claim_width_induction`) and it fails gate
  `B`.
- **NO DERIVATION FROM THE STAGGERED RECURRENCE.** The lane's anchor is titled
  *the recurrence proof solve*, and the phrase is kept only in the narrow sense
  it earns: **"recurrence proof" names the constructive Schur form at a fixed
  core of a fixed width** — an exact linear solve of `A v = d` — and names
  nothing else. `claim_recurrence_derivation` fails gate `B`.
- **THE BREAKING DIRECTION IS NOT PROVEN HERE.** Only the **compatibility**
  direction becomes constructive. The converse — that a source **meeting** the
  window **does** break `R` — remains Block 193's exhaustive censuses, `40`
  cells at `T = 16` and `70` at `T = 20`, **cited and not reproved**.
  `claim_breaking_direction_proven` fails gate `B`.
- **NO GENERIC `(m, c)` THEOREM AND NO CONTINUUM.** Two rational points and two
  widths. Two points are not a parameter space and two widths are not a limit.
- **THE READINGS ARE READINGS.** Five of them are enumerated below, and
  `READINGS_LICENSED_CLAIMED = False` is a declared constant with a gate.

**AND ONE HALF-CLOSURE IS THE POINT OF THE BLOCK.** Block 193 landed
`LAW_PROVED_FROM_RECURRENCE_CLAIMED = False` with the open leg named: *a proof
would have to show, from `Q = m H + H D_s - D_s^T H` and the grading, why
`G^T d_b` vanishes off three slices.* This block does **not** do that. It does
something weaker and exactly stateable: it shows that `G^T d_b` **is the unique
solution of an explicitly constructed twelve-row system**, and that this
construction plus one further exact containment **proves one of the law's two
directions** for the whole reflected one-cell source family. The open leg is
**narrowed**, not removed, and the note says which half is still a census.

**EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER
METAPHYSICAL NECESSITY** — the cycle-913 caution, carried verbatim — and every
positive here is candidacy within this formalism and never a claim about nature.

---

## W1 — the wall, and the charter

### What was open

Block 193 proved a locality law by **exhaustion**: a reflected one-cell tangent
at anchor `s` breaks the intertwining identity at core `t0` **iff**
`{s, s+1}` meets `W(t0) = [2⌊t0/2⌋+1, 2⌊t0/2⌋+3]`. It then **reduced** the law
to two measured support facts —

```text
R[a, b]  =  - u_b^T dQ c_a,     u_b := G^T d_b,     c_a := G[:, theta_a],
union_b supp_slices(u_b)  =  W(t0),
supp_slices(dQ_s) ∩ {0..T/2}  =  [2⌊s/2⌋, 2⌊s/2⌋+2],
```

— and stopped there, recording the first of those as measured and not derived.
Three things were open:

1. **Is `u_b` characterised by anything, or is its support a coincidence of the
   inverse?** Nobody had asked whether `u_b` solves a system that the window
   itself determines.
2. **Are twelve rows needed?** The union of supports is not, by itself, a
   minimality statement.
3. **Does the law's compatibility direction actually follow from the support
   fact?** The reduction `R = -u_b^T dQ c_a` was measured; the step from it to
   *disjoint sources cannot break `R`* was asserted.

### The charter

1. **Write the system down.** Make `d_b^(s)` an explicit vector, make the window
   an explicit twelve-column matrix `A = Q^T[:, J(t0)]`, and ask for existence
   and uniqueness.
2. **Solve it twice, and never through `G` the second time.** A restricted route
   that inverts a `12 × 12` minor and checks all `4T` equations is an
   **independent** route; agreeing with `G^T d` then means something.
3. **Read both steps, not one.** Block 193 read only the two-step defect. The
   one-step family is where the parity fine structure lives.
4. **Decide minimality, do not infer it.** Test single-row deletions as
   image-membership questions.
5. **Prove the consequence or say which containment is missing.** The bilinear
   identity has two terms; both must be controlled.

---

## N1 — THE SYSTEM, and its solution is unique

**NOTHING BELOW IS A CONSTRUCTION IF THIS SECTION IS NOT EXACT.**

### The carrier, carried unchanged

Block 190's wrap-edge width family at **two** widths: the staggered
Dirac–Kähler kernel on `Z_T × Z_4` with `eta_t = 1`, `eta_x = (-1)^t` and the
temporal sign `w = -1` on the **wrap edge** `t = T-1`; the grade-raising
`d_K = P1 K P0 + P2 K P1`; the site reflection `theta_s(t) = -t` with fixed
slices `{0, T/2}`; the raising set `A_s` in the closed half `{0..T/2}` excluding
fixed-slice spatial edges; the glue `D_s = A_s - Ps A_s Ps`; and

```text
Q  =  m H  +  H D_s  -  D_s^T H,        G = Q^-1.
```

`H` is Block 191's quarter-weighted four-corner cell average of the **landed**
Block 105 `shear_hodge(c, v)` at **unit volume**, read through the Block 128
module. That import is the only object imported.

### The objects, as formulas

For a core `t0`, index its eight cells `b ↔ (t_b, x_b)` with `t_b ∈ {t0, t0+1}`.
The reflected pairings, the step operators and the **defect columns** are

```text
L_s[a, b]  =  G[idx(t_b + s, x_b), idx(theta_s t_a, x_a)],     K_c = L_0,
W_s        =  K_c^-1 L_s                                       for s = 1, 2,
d_b^(s)    =  e_(t_b+s, x_b)  -  sum_b' W_s[b', b] e_(t_b', x_b')   in QQ^(4T).
```

`d_b^(2)` is Block 193's transport defect; **`d_b^(1)` is this block's
addition**. Each carries **one** entry at `(t_b + s, x_b)` and at most **eight**
on the read pair `{t0, t0+1}`, so no column can exceed **nine** nonzeros — the
sparsity is a property of the formula and it is gated as one (`C-3`).

The **window as a row set of `Q^T`** is the one new construction element:

```text
J(t0)  =  [2⌊t0/2⌋+1, 2⌊t0/2⌋+3] × Z_4          (12 rows),
A      =  Q^T[:, J(t0)]                          ((4T) × 12 over QQ).
```

`J(t0)` is **imposed** from Block 193's measured window. It is not derived here,
and `N4g` says so.

### The domain, and it is Block 193's own rule

Valid cores are those with `t0 + 3 ≤ T/2`:

| `T` | valid cores | `4T` | count |
| ---: | --- | ---: | ---: |
| 16 | `t0 = 1, 2, 3, 4, 5` | 64 | 5 |
| 20 | `t0 = 1, 2, 3, 4, 5, 6, 7` | 80 | 7 |

**The `T = 20` row is the adversarial check's extension.** The solve measured
`t0 = 3, 4` and called them spot checks; the check ran all seven and found no
refutation at any. Twelve cores per point, twenty-four core instances in all.
Gate `C-1`, mutation `break_core_domain`.

### Uniqueness, two ways

```text
rank_QQ(A)  =  12        at every core, both widths, both points.
```

Gate `C-2`. There is also a one-line proof that does not depend on the core:
`rank(Q) = 64` and `80` with two-sided residuals
`nnz(QG - I) = nnz(GQ - I) = 0`, so `Q^T` is invertible and **every** twelve-column
subset of it is linearly independent. Either way, a solution of `A v = d`
supported on the window is unique **when it exists**.

### Existence, through a route that never touches `G`

For each `(core, step)` the eight columns are solved by an **independent
restricted route**: an exact `rref` of `A^T` selects twelve independent rows, the
`12 × 12` minor on those rows is inverted over `QQ`, and the resulting `x` is
checked against **all `4T`** equations before it is padded.

```text
A X_1 = [d_b^(1)]_{b=0..7},    A X_2 = [d_b^(2)]_{b=0..7},
residuals   0   in every equation,
8/8 columns per (core, step),   384 exact vector solves in total
            = 12 cores × 2 points × 2 steps × 8 columns.
```

Gate `C-3`. **The same twelve pivot rows serve both right-hand sides** at every
core — gate `C-4` — so the two step families are solved through one and the same
minor, and a change of right-hand side does not silently change the route.

### The carrier is the landed one

Two landed numbers are **recomputed** from this block's own construction, with
neither Block 190's nor Block 193's runner imported:

```text
b190,  T = 20, t0 = 3:
  (W - V^2)[0,4]  =  53601896033238042551256 / 229758595220483765728625,
  residual from the landed value:  0.

b193,  T = 16, (t0, s, x) = (2, 5, 0):
  R[0,4]  =  3037174141283939810029465524503010112729631934696915991365059975\
             54493148222247708710000000
           / 7770772509599881682908025679856754421787620216378727090524289160\
             6801827087957579200283634261,
  residual from the landed value:  0,     nnz(R) = 32.
```

The `32` is Block 193's own even-core half-density, reproduced. Gate `C-5`,
mutation `break_landed_fingerprints`.

---

## N2 — THE IDENTIFICATION, and it is what turns a measurement into a construction

### The padded solution **is** `G^T d`

```text
nnz( pad_J(v_b^(s))  -  G^T d_b^(s) )  =  0
```

for all eight columns, both steps, every core, both widths, both points. Gate
`D-1`. And the functional solves the original system in the same places:

```text
nnz( Q^T u_b^(s)  -  d_b^(s) )  =  0,          u_b^(s) := G^T d_b^(s).
```

Gate `D-2`.

### Why that is stronger than Block 193's support fact

Block 193 measured that `u_b` **is supported** in the window. Uniqueness
(`C-2`) plus agreement (`D-1`) gives the sharper statement:

> `u_b` **is** the unique window-supported solution of `A v = d_b`.

So Block 193's mechanism object is not a separate vector that happens to live in
the window — it is **the** window-Schur solution, and the window is what
determines it. Gate `D-3`, mutation `break_mechanism_object`.

### The one-step content is exactly half the columns

`W_1`'s column `b` for `b = 0..3` is exactly `e_(b+4)`: the target cell
`(t0+1, x_b)` is **already in the core**, so the `L_1` column is a `K_c` column
and `d_b^(1)` cancels entrywise. Measured, at every core:

```text
d_b^(1)  =  0        for b = 0, 1, 2, 3        (4 of 8 columns),
d_b^(1) != 0         for b = 4, 5, 6, 7.
```

Gate `D-4`. Everything the one-step family says below is therefore a statement
about the four `t0+1`-row columns.

---

## N3 — EXACTNESS, THE PARITY FINE STRUCTURE, AND MINIMALITY

### The two-step union is the full window

```text
union_b supp_rows(v_b^(2))  =  J(t0)          all 12 rows,
union_b supp_slices(v_b^(2)) =  W(t0)          all 3 slices,
```

at every core of both widths and both points, with **no negative-half support at
all**. Gate `E-1`. This is Block 193's `E-7` support fact, now read off the
**solution of the constructed system** rather than off `G^T d`.

### The one-step union is parity-split — and that is the discovery

```text
odd  t0:   union_b supp_slices(v_b^(1))  =  W(t0)          3 slices, 12 rows,
even t0:   union_b supp_slices(v_b^(1))  =  { 2⌊t0/2⌋+1 }  1 slice,   4 rows.
```

The single slice is the window's **first**: slice `3` at `t0 = 2`, slice `5` at
`t0 = 4`, and — in the `T = 20` extension — slice `7` at `t0 = 6`. Gate `E-2`.

### The per-column rule, which names WHICH slices and not only how many

Counting the window slices met by column `b`, and gated so that a `1` means the
window's **first** slice and a `3` means the **whole** window:

| family | parity | `b = 0..7` |
| --- | --- | --- |
| one-step | odd | `(0, 0, 0, 0, 3, 3, 3, 3)` |
| one-step | **even** | `(0, 0, 0, 0, 1, 1, 1, 1)` |
| two-step | odd | `(3, 3, 3, 3, 3, 3, 3, 3)` |
| two-step | **even** | `(1, 1, 1, 1, 3, 3, 3, 3)` |

Gates `E-1` and `E-2`. At even cores each nonzero one-step column carries
exactly **four** coordinates — one per spatial site of that first slice — which
is gated in the same check.

**This is the microscopic shape of the parity switch**, and of why cores `2j`
and `2j+1` share a window. Block 193's *exempt end* at an even core — that the
functionals carry nothing at slice `t0` — is already contained in `F-1`, since
`t0 ∉ W(t0)` there. What the table adds is **sharper** than that: at even cores
the four `t0`-row columns do not merely avoid slice `t0`, they live on the
**first window slice alone** and avoid `t0+2` and `t0+3` as well, and the
one-step columns do the same on four coordinates. It is a **measurement** of
shape, not a derivation of cause; `N4g` fence 4 and reading `R3` say so.

### Minimality, decided and not inferred

Because `rank(A) = 12` makes the solution unique, a row may be deleted from the
allowed support of a family **iff** that coordinate vanishes in every member.
So single-row deletions decide **every** proper subset: any proper subset of
`J(t0)` sits inside one of the twelve one-row-deleted sets. Each deletion is
tested as an **image-membership** question on the restricted eleven columns —
not as a rank count, and not as a reading of the union.

```text
per core and family:  12 deletions,
total:                12 cores × 2 points × 3 families × 12 rows = 864 tests.
```

| family | droppable rows | minimal rows |
| --- | --- | ---: |
| two-step, every core | none | **12** |
| joint one-and-two-step, every core | none | **12** |
| one-step, **odd** core | none | **12** |
| one-step, **even** core | the eight non-first-slice rows | **4** |

Gates `E-3` and `E-4`, mutations `break_minimality`, `break_joint_minimality`,
`break_even_collapse`.

**The twelve-row window is therefore NOT minimal for one-step transport at even
cores.** That is the adversarial check's `P1` qualification, and it is carried
here as content rather than as an erratum: it weakens the attribution if `C2` is
narrated step-by-step, and it does **not** weaken the two-step window or the
single support set that has to handle both steps.

### The two-slice subsets, entry for entry

In the order `first+middle`, `first+last`, `middle+last`:

| family | parity | outcome |
| --- | --- | --- |
| one-step | odd | `(False, False, False)` |
| one-step | **even** | `(True, True, False)` |
| two-step | odd | `(False, False, False)` |
| two-step | even | `(False, False, False)` |

Gate `E-5`, mutation `break_subset_table`. The single `True` pair is the same
even-core collapse seen from the other side: the first slice is enough, so any
subset containing it is enough, and `middle+last` — which omits it — is not.

---

## N4 — THE CONSEQUENCE, and it needs two containments rather than one

### The identity, expanded once

Block 193's reduction is `R[a,b] = -u_b^T dQ c_a`. Expanding
`dQ = m dH + dH D_s - D_s^T dH` once gives, with no matrix product left to hide
anything,

```text
u_b^T dQ  =  u_b^T dH (m I + D_s)  -  (D_s u_b)^T dH.
```

Measured at residual `0` on **every** census cell, gate `F-4`.

**That second term is why `supp(u_b) ⊆ J(t0)` alone proves nothing.** It reads
`D_s u_b`, about which the first containment says exactly nothing. This is the
adversarial check's `C5` refinement and it is folded here as content, not as a
footnote.

### Both containments, exactly

```text
supp(u_b)      ⊆ J(t0)   for every b,   union over b  =  12 of 12 window rows,
supp(D_s u_b)  ⊆ J(t0)   for every b,   union over b  =  10 of 12 window rows,
```

at every core of both widths **and both points**. Gates `F-1`, `F-2`. The two
rows `D_s u` never reaches — not for any `b`, at any core — are the same two
everywhere:

```text
J(t0) \ supp(D_s u)  =  { (2⌊t0/2⌋+2, 0),  (2⌊t0/2⌋+2, 2) }
                     =  the EVEN spatial sites of the window's MIDDLE slice.
```

Gate `F-3`, mutation `break_du_localization`. `D_s u` is therefore localized
**more sharply** than `u`, which is a measured fact of this construction and is
not explained here.

### The theorem

> **Compatibility direction.** Let `dH` be a reflected one-cell source with
> support `S` (its row and column supports are identical, measured in the same
> gate). If `S ∩ J(t0) = ∅`, then `u_b^T dQ = 0` for all eight `b`, hence
> `R = 0`.

*Proof.* Write `dH = Σ_{p,q ∈ S} dH[p,q] E_{p,q}`. The first term of the
identity contracts `u_b` against rows `p ∈ S`; since `supp(u_b) ⊆ J(t0)` and
`S ∩ J(t0) = ∅`, every such `u_b[p]` is zero. The second term contracts
`D_s u_b` against the same rows; since `supp(D_s u_b) ⊆ J(t0)`, every such
`(D_s u_b)[p]` is zero. Both terms vanish identically. ∎

This is an argument about the whole source-cell family, not a sampled
cancellation — and the sampling is done anyway, exhaustively, as a guard.

### The census, exhaustive

Every reflected one-cell source at every positive anchor is built, and those
whose support misses the window are all tested:

```text
T = 16:  16 disjoint source cells per core × 5 cores  =  80,
T = 20:  24 disjoint source cells per core × 7 cores  = 168,
                                              total    = 248 source/core cells,
failures: 0,     all eight u_b simultaneously.
```

Gate `F-5`.

### Two gated instances, one per parity

```text
odd  t0 = 1,  W = {1,2,3},  source (s,x) = (4,0),
              dH slice support {4, 5, 11, 12},   u^T dQ = 0_(8 × 64);
even t0 = 2,  W = {3,4,5},  source (s,x) = (0,0),
              dH slice support {0, 1, 15},       u^T dQ = 0_(8 × 64).
```

Gate `F-6`. Note the even instance: the source sits at the **seam anchor**
`s = 0`, whose `thA_s` image is slice `15`, so its full three-slice support
`{0, 1, 15}` misses `{3, 4, 5}` entirely. The seam anchors are **inside** the
census rather than excluded from it — which is the same discipline that made
Block 193's `⌊t0/2⌋` visible in its own tables.

The **exempt end** itself shows up on the functional side rather than the source
side: at an even core `t0 ∉ W(t0)`, so `F-1` already puts every functional off
slice `t0`, and `N3`'s per-column rule sharpens it to the first window slice
alone for the four `t0`-row columns.

### And the hypothesis is not vacuous

A compatibility theorem whose hypothesis is never violated would be worth
nothing. Three sources that **do** meet the window:

| core | source `(s, x)` | `dH` slices | `nnz(u^T dQ)` |
| ---: | --- | --- | ---: |
| 1 | `(2, 0)` | `{2, 3, 13, 14}` | **60** |
| 2 | `(2, 0)` | `{2, 3, 13, 14}` | **64** |
| 2 | `(4, 0)` | `{4, 5, 11, 12}` | **28** |

Gate `F-7`, mutation `break_nonvacuity`. The theorem separates two **nonempty**
cases, and the direction it does not prove is a real question rather than an
empty one.

---

## N4c — THE SECOND POINT, and what does not move with it

At `(m, c) = (1/2, 1/3)`, whose unit-volume Hodge block — read from the **import**
and gated against a declared literal, not from a rerun — is

```text
B(1/3, 1)  =  [[1,0,0,0],[0,9/8,-3/8,0],[0,-3/8,9/8,0],[0,0,0,1]],
```

the **entire per-core signature** is identical on all twelve cores: window,
`rank(A) = 12`, existence residuals, identification residuals, dual residuals,
both support unions, both per-column slice patterns, the four zero one-step
columns, all three minimality counts, the droppable sets and the two-slice
table. Gates `G-1`, `G-2`.

The carrier is **not** the same object: at `T = 16`,

```text
nnz( Q(9/20, 5/13) - Q(1/2, 1/3) )  =  512   of 512 nonzero entries.
```

Every entry moves and no structural number does.

**And both containments hold here too** — including the ten-row middle-slice
localization of `D_s u`. Gate `G-3`. This **extends** the adversarial check,
which ran its `C5` at the control fixture only.

This is persistence at one additional exact point. It is **not** a generic
`(m, c)` theorem, and `GENERIC_POINT_THEOREM_CLAIMED = False` is gated.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

- **WINDOW** names a set of twelve row indices of an exact rational matrix,
  imported from Block 193's measured law. It is not a region of anything.
- **TRANSPORT DEFECT** names an explicit rational vector with at most nine
  nonzero entries. Nothing transports.
- **SOURCE** names a one-cell volume tangent of the imported Hodge block, plus
  its `thA_s` image cell. It is not matter, and it is not a field.
- **UNIQUE** names `rank(A) = 12` and nothing stronger — uniqueness **within**
  `J(t0)`, not uniqueness of `J(t0)`.
- **PROOF** names a finite exact argument over `QQ` on one constructed matrix
  family at two widths and two rational points.
- **RECURRENCE PROOF** names the constructive Schur form at a fixed core of a
  fixed width. It does **not** name an induction on `T`, and it does not name a
  derivation from the staggered recurrence.

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within this imposed finite matrix construction, at each of the twelve valid
> cores of `T = 16` and `T = 20` and at each of two rational points, the
> transport-defect functional of each core cell is the unique solution of an
> explicitly constructed twelve-row window-restricted linear system, that
> solution coincides entrywise with `G^T d`, twelve rows are minimal for the
> two-step and joint families and four suffice for the one-step family at even
> cores, and the two exact support containments imply that every reflected
> one-cell source disjoint from the window leaves the intertwining residual
> exactly zero.

### Five further fences, all five self-imposed

1. **One direction only.** The converse — sources meeting the window **do**
   break `R` — is **not** proven here. It is Block 193's censuses, `40 + 70`
   cells, cited.
2. **The window is imposed.** No derivation of `2⌊t0/2⌋+1` from the staggering
   is offered. The formula comes from Block 193's measurement.
3. **Minimality is inside `J(t0)`.** Every proper **subset** of the window is
   decided. Whether some **other** twelve-row set of `Q^T` also carries the
   families is **not** decided either way.
4. **The even-core collapse is shape, not cause.** That the one-step family
   lives on the first slice at even cores is measured at twelve cores; why the
   staggering forces it is not derived.
5. **Two widths, two points.** Not a width family theorem, not a parameter-space
   theorem, not a limit.

### What IS derived, stated positively so the fence is not mistaken for a retreat

Given the construction, the compatibility direction is a **theorem** and not a
measurement: it follows from two containments and one algebraic identity, and it
covers **every** source in the family at once, including sources nobody
enumerated. The `248`-cell census is a **guard on the theorem**, not its
evidence. And the identification `u_b = ` the window-Schur solution is a
**characterisation**: it says what Block 193's mechanism object *is*, which the
support measurement alone never did.

---

## READINGS — five of them, and each is a reading

- **`R1`.** *That Block 193's window law is now proven.* Measured: the
  **compatibility** direction is constructive at twelve cores of two widths and
  two points; the **breaking** direction is Block 193's censuses, cited and not
  reproved. **Reading.**
- **`R2`.** *That this is a recurrence proof.* Measured: a Schur-complement
  solve at each fixed core of each fixed width, with no step from `T` to `T+2`
  and no use of the staggered recurrence. **Reading**, and the block's own
  banner says so.
- **`R3`.** *That the even-core single-slice collapse explains the parity
  switch.* Measured: at even cores the one-step family lives on the window's
  first slice and four rows are minimal there. Why the staggering forces that is
  not derived. **Reading.**
- **`R4`.** *That `u_b` is canonical.* Measured: given the twelve window rows it
  is the **unique** supported solution, because `rank(A) = 12`. Whether some
  other twelve-row set also carries the family is not decided. **Reading.**
- **`R5`.** *That the structure is a property of the width family rather than of
  the fixture.* Measured: two rational points on twelve cores. Two points are
  not a parameter space. **Reading.**

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | family |
| ---: | --- | --- | --- |
| 1 | `origin/main`, axiom and registry blobs, worktree blobs, timeout | five pins fixed | `A` |
| 2 | `PARENT_COMMIT` ancestry, both Block 195 artifacts, stale pin carrying neither | exact | `A` |
| 3 | imposed / registered / adopted | `6 / 0 / 0` | `B` |
| 4 | gravity structures enumerated as NOT SUPPLIED | `9` | `B` |
| 5 | `WIDTH_INDUCTION_CLAIMED`, `RECURRENCE_DERIVATION_CLAIMED` | both `False` | `B` |
| 6 | `BREAKING_DIRECTION_PROVEN_CLAIMED` | `False` | `B` |
| 7 | `GENERIC_POINT_THEOREM_CLAIMED`, `CONTINUUM_LIMIT_CLAIMED`, `READINGS_LICENSED_CLAIMED` | all `False`; `5` readings | `B` |
| 8 | valid cores `t0 + 3 <= T/2` | `1..5` at `T=16`, `1..7` at `T=20`; `12` cores | `C` |
| 9 | `rank(Q^T[:, J(t0)])`; `rank(Q)`; `nnz(QG-I)`, `nnz(GQ-I)` | `12`; `64/80`; `0`, `0` | `C` |
| 10 | existence per `(core, step)`; restricted-solve residual; total solves; defect column weight | `8/8`; `0`; `384`; `<= 9` | `C` |
| 11 | one pivot row set for both right-hand sides | `True`, `12` rows | `C` |
| 12 | b190 `(W-V^2)[0,4]`; b193 `R[0,4]`, `nnz(R)` | landed literals; residuals `0`; `32` | `C` |
| 13 | `nnz(pad_J(v_b^(s)) - G^T d_b^(s))` | `0`, both steps, every core | `D` |
| 14 | `nnz(Q^T u_b^(s) - d_b^(s))` | `0`, same places | `D` |
| 15 | `MECHANISM_IS_SOLUTION` | `True` | `D` |
| 16 | identically zero one-step columns | `4` of `8`, `b = 0..3` | `D` |
| 17 | two-step support union; its per-column rule | full `J(t0)`, `12` rows, `3` slices; `(3)^8` odd, `(1,1,1,1,3,3,3,3)` even | `E` |
| 18 | one-step support union; its per-column rule; even-core column weight | `3` slices odd, `1` (first) even; `(0,0,0,0,3,3,3,3)` odd, `(0,0,0,0,1,1,1,1)` even; `4` | `E` |
| 19 | minimal rows, two-step and joint; droppable | `12`, `12`; none | `E` |
| 20 | minimal rows, one-step; deletion tests | `12` odd, `4` even; `864` | `E` |
| 21 | two-slice subset table | `(T,T,F)` for one-step even; else `(F,F,F)` | `E` |
| 22 | `supp(u_b) ⊆ J(t0)`; rows | `True`; `12` | `F` |
| 23 | `supp(D_s u_b) ⊆ J(t0)`; rows; missing | `True`; `10`; middle slice, `x = 0, 2` | `F` |
| 24 | `nnz(u^T dQ - [u^T dH(mI+D_s) - (D_s u)^T dH])` | `0` on every census cell | `F` |
| 25 | disjoint source cells per core; total; failures | `16 / 24`; `248`; `0` | `F` |
| 26 | the two parity instances and their `dH` slice supports | `{4,5,11,12}`, `{0,1,15}`; `0_(8×64)` | `F` |
| 27 | non-vacuity witnesses: `dH` slices; `nnz(u^T dQ)` | `{2,3,13,14}`, `{2,3,13,14}`, `{4,5,11,12}`; `60`, `64`, `28` | `F` |
| 28 | the second point's per-core signature; `nnz(Q - Q')`; the imported unit-volume block at `c = 1/3` | identical on `12` cores; `512`; `B(1/3,1)` | `G` |
| 29 | the second point's minimality counts, droppable sets, subset table | identical | `G` |
| 30 | both containments and the ten-row localization at the second point | `True` | `G` |
| 31 | the note at its final path; `N5` byte-identical; `sp.nsimplify` count | present; verbatim; `0` | `H` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

**Dead end one — reading minimality off the union of supports.** The union is a
minimality statement **only** because uniqueness makes the solution family
canonical. Stated on its own it is an inference from a rank, and the check's
`P1` says so explicitly. What replaced it: `864` single-row deletions tested as
image-membership questions, which decide every proper subset outright.

**Dead end two — narrating existence step-by-step.** *The one-step defect solves
in the window, and so does the two-step defect, so the window is the transport
support* is a sentence that is true clause by clause and wrong as an
attribution: at even cores the one-step family needs only four of the twelve
rows. The honest object is the **joint** family, and that one does need all
twelve.

**Dead end three — proving the consequence from `supp(u_b) ⊆ J` alone.** The
bilinear identity has a `(D_s u_b)^T dH` term. Without the second containment
the argument is a gap papered over by a census. Measuring
`supp(D_s u_b) ⊆ J(t0)` closed it — and revealed the sharper ten-row
localization on the way.

**Dead end four — reaching for the recurrence.** The design proposed deriving
`supp(u_b)` from `Q = m H + H D_s - D_s^T H` and the grading. No such argument
was found. What worked instead was to stop asking *why* the support is three
slices and to ask *what system the functional solves* — which is answerable
exactly, and which is a strictly weaker but genuinely constructive statement.

**What actually worked.** Making every object an explicit vector; solving twice
through routes that share nothing; testing subsets by image membership rather
than by rank; and expanding the bilinear form **once** so that the two terms
that need containment are visible as two terms.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE PROOF LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), BLOCK 193's CORE FRAME AND ITS TRANSPORT-DEFECT FUNCTIONALS READ AT BOTH STEPS (the eight cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_s[a,b] = G[idx(t_b + s, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, the step operators W_s = K_c^-1 L_s for s = 1 and s = 2, and the defect columns d_b^(s) = e_(t_b+s, x_b) - sum_b' W_s[b', b] e_(t_b', x_b') -- THE ONE-STEP FAMILY IS THIS BLOCK'S ADDITION), THE TWELVE WINDOW ROWS READ AS A COLUMN SET OF Q^T (J(t0) = [2 floor(t0/2)+1, 2 floor(t0/2)+3] x Z_4 and A = Q^T[:, J(t0)], IMPOSED FROM BLOCK 193's MEASURED WINDOW AND DERIVED FROM NOTHING), THE VALID CORE DOMAIN t0 + 3 <= T/2 (t0 = 1..5 at T = 16 and t0 = 1..7 at T = 20, the second being THE ADVERSARIAL CHECK's EXTENSION of the solve's two spot-check cores), BLOCK 193's REFLECTED ONE-CELL HODGE TANGENT dH(s,x) = E(s,x) dB E(s,x)^T / 4 + E(thA_s s, x) P_4 dB P_4^T E(thA_s s, x)^T / 4 with thA_s(t) = -1-t together with dQ = m dH + dH D_s - D_s^T dH, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORDS RECURRENCE PROOF AND IS SAID IN THOSE WORDS: 'RECURRENCE PROOF' NAMES THE CONSTRUCTIVE SCHUR FORM AT EACH FIXED CORE OF EACH FIXED WIDTH -- an exact linear solve of A v = d against Q^T's twelve window rows -- AND NAMES NOTHING ELSE. NO STEP HERE DERIVES ANYTHING FROM THE STAGGERED RECURRENCE AND NO STEP PROPAGATES ANYTHING FROM T TO T + 2: TWO WIDTHS ARE NOT AN INDUCTION. ONLY THE COMPATIBILITY DIRECTION OF BLOCK 193's WINDOW LAW IS PROVEN HERE; THE BREAKING DIRECTION REMAINS BLOCK 193's EXHAUSTIVE CENSUSES OF 40 CELLS AT T = 16 AND 70 AT T = 20, CITED AND NOT REPROVED, AND THIS BLOCK SAYS SO FIRST. 'WINDOW' NAMES A SET OF TWELVE ROW INDICES OF AN EXACT RATIONAL MATRIX, 'TRANSPORT DEFECT' NAMES AN EXPLICIT RATIONAL VECTOR WITH AT MOST NINE NONZERO ENTRIES, 'SOURCE' NAMES A ONE-CELL VOLUME TANGENT OF THE IMPORTED HODGE, 'UNIQUE' NAMES rank(A) = 12 AND NOTHING STRONGER, AND 'PROOF' NAMES A FINITE EXACT ARGUMENT OVER QQ ON ONE CONSTRUCTED MATRIX FAMILY. NO GENERIC (m, c) THEOREM IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: TWO WIDTHS AND TWO RATIONAL POINTS ARE NOT A LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE SYSTEM EXISTS AND ITS SOLUTION IS UNIQUE, AND BOTH ARE EXACT. At every one of the twelve valid cores -- t0 = 1..5 at T = 16 and t0 = 1..7 at T = 20 -- and at BOTH rational points (m, c) = (9/20, 5/13) and (1/2, 1/3), the twelve-column restriction A = Q^T[:, J(t0)] has EXACT RANK 12, so a solution of A v = d supported on the window is UNIQUE whenever it exists. That uniqueness has a one-line independent proof as well: rank(Q) = 64 at T = 16 and 80 at T = 20 with two-sided inverse residuals nnz(QG - I) = nnz(GQ - I) = 0, so Q^T is invertible and EVERY twelve-column subset of it is linearly independent. AND THE SOLUTION EXISTS FOR ALL EIGHT COLUMNS AT BOTH STEPS: 8/8 per (core, step), reached by an INDEPENDENT restricted route that never touches G -- an exact rref of A^T selects twelve independent rows, the 12 x 12 minor on those rows is inverted over QQ, and the resulting x is checked against ALL 4T equations before it is padded -- at residual ZERO in every case, 384 exact vector solves in total. THE SAME TWELVE PIVOT ROWS SERVE BOTH RIGHT-HAND SIDES at every core, so the one-step and two-step families are solved through one and the same minor. THE REBUILT CARRIER IS THE LANDED ONE: it reproduces Block 190's (W - V^2)[0,4] = 53601896033238042551256/229758595220483765728625 at T = 20, t0 = 3 and Block 193's R[0,4] = 303717414128393981002946552450301011272963193469691599136505997554493148222247708710000000/77707725095998816829080256798567544217876202163787270905242891606801827087957579200283634261 at T = 16, (t0, s, x) = (2, 5, 0) with nnz(R) = 32, each at residual ZERO, and neither landed runner is imported.\nper_mode: THE IDENTIFICATION, AND IT IS WHAT TURNS A MEASUREMENT INTO A CONSTRUCTION. Padding the restricted solution by zeros outside J(t0) gives G^T d_b ENTRYWISE: nnz(pad(v_b) - G^T d_b) = 0 for all eight columns, at both steps, at every core of both widths and both points. Together with rank(A) = 12 that says something stronger than Block 193's support fact: u_b = G^T d_b is not merely SUPPORTED in the window, it IS the unique window-supported solution of A v = d_b, so BLOCK 193's MECHANISM OBJECT IS THE CONSTRUCTIVE SOLUTION AND NOT A SEPARATE OBJECT THAT HAPPENS TO AGREE WITH ONE. The dual identity is measured in the same places: nnz(Q^T u_b^(s) - d_b^(s)) = 0, so the padded vector is a genuine preimage. AND THE ONE-STEP CONTENT IS EXACTLY HALF THE COLUMNS: FOUR of the eight one-step defects are IDENTICALLY ZERO at every core, because W_1's column b for b = 0..3 is exactly e_(b+4) -- the cell (t0+1, x_b) is already in the core, so d_b^(1) cancels entrywise -- and the whole one-step content lives in b = 4..7.\nper_block: EXACTNESS, THE PARITY FINE STRUCTURE, AND MINIMALITY DECIDED EXHAUSTIVELY. THE TWO-STEP SUPPORT UNION IS THE FULL TWELVE-ROW WINDOW at every core of both widths and both points -- all three slices, all four spatial sites, and no negative-half support anywhere. THE ONE-STEP UNION IS PARITY-SPLIT: all three window slices at ODD cores, and at EVEN cores EXACTLY THE FOUR ROWS OF THE WINDOW'S FIRST SLICE -- slice 3 at t0 = 2, slice 5 at t0 = 4 and, in the T = 20 extension, slice 7 at t0 = 6. That single-slice collapse is the microscopic shape of the parity switch and of the shared window of the cores 2j and 2j+1. TWELVE ROWS ARE MINIMAL, AND MINIMALITY IS DECIDED AND NOT INFERRED: for the two-step family and for the JOINT one-and-two-step family, EVERY single-row deletion from J(t0) fails as an image-membership question at every core of both widths and both points, and since every proper subset of J(t0) is contained in one of those twelve deleted sets, NO PROPER SUBSET CARRIES EITHER FAMILY -- 864 deletion tests, zero droppable rows. THE ONE-STEP FAMILY ALONE IS THE EXCEPTION AND THE ADVERSARIAL CHECK FOUND IT: at even cores exactly the eight non-first-slice rows are droppable, so FOUR rows are minimal and THE TWELVE-ROW WINDOW IS NOT MINIMAL FOR ONE-STEP TRANSPORT AT EVEN CORES. The three two-slice subsets agree entry for entry: in the order first+middle, first+last, middle+last the one-step family at even cores gives (True, True, False) and every other row is (False, False, False). THAT QUALIFICATION IS CARRIED HERE AS CONTENT AND NOT AS AN ERRATUM.\nlattice_wide: THE CONSEQUENCE, AND IT NEEDS TWO CONTAINMENTS RATHER THAN ONE -- WHICH IS THE CHECK's C5 REFINEMENT, FOLDED AS CONTENT. Block 193's bilinear reduction is R[a,b] = -u_b^T dQ G[:, theta_a], and expanding dQ = m dH + dH D_s - D_s^T dH once gives the identity u_b^T dQ = u_b^T dH (m I + D_s) - (D_s u_b)^T dH, measured here at residual ZERO on every census cell. THAT SECOND TERM IS WHY supp(u_b) subset J(t0) ALONE PROVES NOTHING: it reads D_s u_b, about which the first containment says nothing at all. BOTH CONTAINMENTS ARE EXACT: supp(u_b) subset J(t0) on all twelve window rows, and supp(D_s u_b) subset J(t0) on exactly TEN of them, the two rows it never reaches being the spatial sites 0 and 2 of the window's MIDDLE slice -- at every core of both widths and BOTH points. Since a reflected one-cell source has IDENTICAL row and column support S, a source with S disjoint from J(t0) kills both terms identically, so u_b^T dQ = 0 and R = 0 FOR THE WHOLE SOURCE-CELL FAMILY. That is a proof and not a sampled cancellation, and the sampling is done anyway as a guard: 16 disjoint source cells per T = 16 core and 24 per T = 20 core, 248 source/core cells, ZERO failures for the eight u_b simultaneously. Two instances are gated, one per parity, both at T = 16: odd t0 = 1 with window {1,2,3} and source (s,x) = (4,0) whose dH meets slices {4,5,11,12}, and even t0 = 2 with window {3,4,5} and source (s,x) = (0,0) whose dH meets slices {0,1,15}, each giving u^T dQ = 0 as a full 8 x 64 zero block. AND THE HYPOTHESIS IS NOT VACUOUS: three sources that DO meet the window give nnz(u^T dQ) = 60, 64 and 28, so the theorem separates two nonempty cases and the direction it does NOT prove is a real question.\nper_scope: THE STRUCTURE IS OF THE CLASS AND NOT OF THE FIXTURE, AND WHAT REMAINS OPEN IS NAMED. At the second rational point (m, c) = (1/2, 1/3) the ENTIRE per-core signature is identical on all twelve cores -- window, rank, existence residuals, identification residuals, dual residuals, both support unions, both per-column slice patterns, the four zero one-step columns, all three minimality counts, the droppable sets and the two-slice table -- on a carrier that is measurably different, nnz(Q(9/20,5/13) - Q(1/2,1/3)) = 512 of 512 nonzero entries at T = 16. BOTH CONTAINMENTS HOLD AT THE SECOND POINT TOO, WHICH EXTENDS THE ADVERSARIAL CHECK: its C5 was run at the control fixture only, and the ten-row middle-slice localization of D_s u is reproduced here at (1/2, 1/3) as well. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: the BREAKING direction of the law is not proven and stays Block 193's censuses; nothing here is a width induction and no argument propagates from T to T + 2, so the law for arbitrary even T is untouched; the window J(t0) is IMPOSED from Block 193's measurement and no derivation of the formula 2 floor(t0/2) + 1 from the staggering is offered; whether some OTHER twelve-row set also carries the families is NOT decided, because minimality was tested inside J(t0) and not against every row set of Q^T; the even-core single-slice collapse is MEASURED and its mechanism is NOT explained; and two rational points are not a parameter space.\nRESULT: ON THE SITE-GLUED WIDTH FAMILY AT T = 16 AND T = 20 AND AT BOTH RATIONAL POINTS, THE TRANSPORT-DEFECT FUNCTIONALS OF EVERY VALID CORE ARE THE UNIQUE SOLUTIONS OF THE TWELVE-ROW WINDOW-RESTRICTED SYSTEM A v = d WITH A = Q^T[:, J(t0)] AND rank(A) = 12, THE PADDED SOLUTION EQUALS G^T d ENTRYWISE SO BLOCK 193's MECHANISM OBJECT IS THAT SOLUTION, THE TWELVE ROWS ARE EXHAUSTIVELY MINIMAL FOR THE TWO-STEP AND JOINT FAMILIES WHILE THE ONE-STEP FAMILY COLLAPSES TO FOUR AT EVEN CORES, AND THE TWO EXACT CONTAINMENTS supp(u_b) subset J AND supp(D_s u_b) subset J TURN THE COMPATIBILITY DIRECTION OF BLOCK 193's WINDOW LAW INTO A THEOREM FOR THE WHOLE REFLECTED ONE-CELL SOURCE FAMILY. Block 193's LAW_PROVED_FROM_RECURRENCE_CLAIMED = False is thereby narrowed and not removed: ONE DIRECTION IS NOW CONSTRUCTIVE AT TWELVE CORES OF TWO WIDTHS AND TWO POINTS, THE OTHER IS STILL A CENSUS, AND NEITHER IS A WIDTH INDUCTION. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-195 STAND EXACTLY AS LANDED. BLOCK 193 IS NOT CORRECTED: its window law, its censuses, its bilinear reduction and its two measured support facts are reproduced here, and its own named open leg is what this block half-closes. BLOCK 190 IS NOT CORRECTED: its unit-cell monodromy is used as the two-step operator and its fingerprint is reproduced digit for digit. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: TWO widths, TWO rational points, ONE profile at unit volume, ONE window formula and ONE source family -- not a scan, not a limit and not an induction; the window is IMPOSED from Block 193's measurement rather than derived; minimality is decided INSIDE J(t0) and says nothing about other row sets; the breaking direction is NOT proven; and the even-core collapse is measured without a mechanism. FOUR ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the T = 20 ALL-CORE EXTENSION from the solve's two spot-check cores to all seven valid ones; the EXHAUSTIVE MINIMALITY result for the two-step and joint families; its EVEN-CORE FOUR-ROW QUALIFICATION, which weakens the attribution if C2 is narrated step-by-step and is stated here rather than buried; and the C5 TWO-CONDITION REFINEMENT, which is the reason the consequence is proven with supp(D_s u_b) subset J and not with supp(u_b) subset J alone. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE RECURRENCE PROOF SOLVE (block 196 candidate), REC PHASE 1+2 MEASURED and B196 CHECK VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **The breaking direction.** Stopped: it is Block 193's exhaustive censuses,
   and re-proving a census by a second census adds nothing. A structural
   argument for it would be new work, not a repair.
2. **A width induction.** Stopped: nothing found. Two widths agree at every
   number; agreement is not propagation, and this note refuses to call it one.
3. **Deriving `J(t0)`.** Stopped: the window formula stays imported from Block
   193's measurement. No route from the grading to `2⌊t0/2⌋+1` was found.
4. **Other row sets.** Stopped: minimality was decided **inside** `J(t0)`.
   Scanning all `C(4T, 12)` row sets is not a computation this block attempts,
   and no partial scan would be a theorem.
5. **A third width or a third point.** Stopped: two of each is what the check
   confirmed, and a third would have to be checked, not assumed.

### REOPEN IF

1. A **derivation** of the three-slice support from the staggered recurrence is
   found. That is the original open leg of Block 193 and it is still open; this
   block narrowed it to *why does `A v = d` have a solution at all*, which is a
   sharper question than the one Block 193 left.
2. The **even-core collapse** is explained — some grading or parity argument
   forcing the one-step family onto a single slice. That would also explain the
   parity switch itself.
3. A **row set other than `J(t0)`** is found that carries both families, or a
   proof that none does. Either resolves fence `3`.
4. A **third width** reproduces all twenty-four core numbers, at which point the
   width-independence reading gains its first real evidence.
5. The **breaking direction** yields to the same bilinear identity read in the
   other direction — a lower bound on `nnz(u^T dQ)` for sources meeting the
   window. The three non-vacuity witnesses (`60`, `64`, `28`) are the first
   three data points of exactly that question, and their spread is itself
   unexplained.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 195's #69. NO CORRECTION IS LANDED BY THIS
BLOCK AGAINST ANY LANDED NUMBER.** Every item below corrects **this lane's own
solve language** or folds an adversarial-check finding as content; each is a
declared constant with a gate and, where it guards a correction, a mutation.

70. **THE `T = 20` DOMAIN WAS TWO SPOT CHECKS, NOT A WIDTH.** The solve measured
    `t0 = 3, 4` at `T = 20` and called them spot checks. The adversarial check
    ran **all seven** valid cores `t0 = 1..7` and found `C1`–`C5` exact at every
    one, including the farthest valid pair `t0 = 6, 7` whose window `{7,8,9}`
    touches the far seam. The full seven are the declared domain here. Gate
    `C-1`, mutation `break_core_domain`.
71. **THE TWELVE-ROW WINDOW IS NOT MINIMAL FOR ONE-STEP TRANSPORT AT EVEN
    CORES.** The solve reported existence and support for both steps against the
    same window without asking whether twelve rows were needed. They are, for
    the two-step and joint families; they are not for the one-step family at
    even cores, where the **four** rows of the window's first slice suffice and
    two of the three two-slice subsets solve. This is the check's `P1`
    qualification, carried as content. Gates `E-4`, `E-5`, mutations
    `break_even_collapse`, `break_subset_table`.
72. **MINIMALITY IS AN IMAGE-MEMBERSHIP QUESTION, NOT A UNION-OF-SUPPORTS
    OBSERVATION.** Reading the minimal row set off the union of the solution
    supports is valid **only** because `rank(A) = 12` makes the solution unique;
    stated bare it is an inference from a rank. Carried here as an exhaustive
    single-row-deletion test — `864` of them — which decides every proper subset
    because every proper subset sits inside one of them. Gate `E-3`, mutation
    `break_minimality`.
73. **THE CONSEQUENCE NEEDS TWO CONTAINMENTS AND THE SOLVE STATED ONE.** The
    phase 1+2 anchor writes *`u_b` supported in `W(t0)` ⟹ sources missing the
    window cannot break `R`*. The bilinear identity carries a `(D_s u_b)^T dH`
    term, so `supp(u_b) ⊆ J` alone does not close it. Both containments are
    exact here, and `D_s u` is in fact localized to **ten** of the twelve rows.
    This is the check's `C5` refinement, folded as content. Gates `F-2`, `F-3`,
    `F-4`, mutation `break_du_containment`.
74. **"RECURRENCE PROOF" IS THE WRONG NAME FOR WHAT IS PROVED.** The lane's
    anchor is titled *the recurrence proof solve* and its design proposed
    deriving the law from the staggered recurrence. What is delivered is a
    per-core **constructive Schur solve** at two fixed widths: no recurrence is
    used and nothing propagates from `T` to `T + 2`.
    `WIDTH_INDUCTION_CLAIMED = False` and
    `RECURRENCE_DERIVATION_CLAIMED = False` are declared constants. Gates `B-3`,
    `B-4`, mutations `claim_width_induction`, `claim_recurrence_derivation`.
75. **ONLY ONE DIRECTION OF THE LAW IS PROVEN, AND THE PROVEN ONE IS NOT
    VACUOUS.** The solve's own `(vi)` is careful, and it compresses easily into
    *the law is proven*. `BREAKING_DIRECTION_PROVEN_CLAIMED = False` is gated;
    and because a compatibility theorem is worthless if its hypothesis is never
    violated, three window-meeting sources are gated with
    `nnz(u^T dQ) = 60, 64, 28`. Gates `B-5`, `F-7`, mutations
    `claim_breaking_direction_proven`, `break_nonvacuity`.

### The adversarial check

Verdict carried as **WINDOW-SCHUR NOT REFUTED, ALL CORES, BOTH WIDTHS,
MINIMALITY QUALIFIED** (`sol xhigh`, independent rebuild from the landed Block
190 and Block 193 notes rather than an invocation of either runner; findings
preserved at `b196_check_findings.md`, checker at `b196_exact_check.py`).

**NO REFUTATION OF `C1`–`C5` WAS FOUND**, at all five `T = 16` cores and all
seven `T = 20` cores. `P1` **qualified** full-window minimality without refuting
the joint theorem (correction 71). `P2` confirmed persistence at `(1/2, 1/3)` on
all twelve cores. `P3` completed the `T = 20` extension (correction 70).

**THE CHECK'S EXACT WITNESSES ARE REPRODUCED DIGIT FOR DIGIT.** Both landed
fingerprints, the `248`-cell census total, the two parity instances with their
`dH` slice supports `{4,5,11,12}` and `{0,1,15}`, and the two-slice subset table
are **declared literals** in this block's runner rather than printed byproducts.

**AND THE CHECK IS EXTENDED IN FIVE PLACES,** all five re-measured independently
here: minimality decided by **exhaustive single-row deletion** rather than by
the uniqueness argument plus three two-slice probes (`E-3`); the **ten-row
middle-slice localization** of `D_s u`, which the check did not report (`F-3`);
**both containments at the second point**, where the check ran its `C5` at the
control fixture only (`G-3`); the **non-vacuity witnesses**, which the check did
not need but a compatibility theorem does (`F-7`); and the **identically zero
one-step columns**, derived here from `W_1`'s column structure rather than
observed (`D-4`).

**THE CHECK'S PROVENANCE CAVEAT IS ACKNOWLEDGED AND HANDLED.** Neither the Block
190 nor the Block 193 artifact is present on canonical `origin/main`; both are
landed in the stacked physics-loop history. Gate `A-2` binds the **Block 195**
parent artifacts by blob at `PARENT_COMMIT` and in the worktree, and verifies
that the stale pin — the Block 194 tip — is a real ancestor carrying neither,
so *landed* here means exactly *landed in this branch history* and the note says
so rather than implying more.

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–195 number **stands as landed**.
**Block 193 is not corrected**: its window law, its `40`- and `70`-cell
censuses, its bilinear reduction and its two measured support facts are
reproduced here, and its own named open leg is what this block half-closes.
**Block 190 is not corrected**: its unit-cell monodromy is the two-step operator
used throughout and its fingerprint is reproduced digit for digit. Block 191's
cell-average assembly and Block 105's `shear_hodge` are used unchanged.

### Reproduction

```text
python3 scripts/admissibility_dirac_kahler_window_schur_transport_defect_2026_08_26.py
python3 ... --list-mutations
python3 ... --mutation claim_width_induction
```

Baseline expectation: families `A` through `H` PASS, `36` checks, exit `0`.
Thirty-five declared mutations, each flipping **exactly one** family and exiting
nonzero; per-family census `A 2, B 8, C 5, D 3, E 5, F 7, G 3, H 2`. Every
measurement is taken once, before any mutation flag is read, so no gate can
cascade into another. Four exact carrier inverses — two `64 × 64` and two
`80 × 80` — are built once and shared by every gate, and no other inverse in
this runner exceeds `12 × 12`.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE RECURRENCE PROOF SOLVE
(block 196 candidate)**, **REC PHASE 1+2 MEASURED** and **B196 CHECK VERDICT**
anchors.
