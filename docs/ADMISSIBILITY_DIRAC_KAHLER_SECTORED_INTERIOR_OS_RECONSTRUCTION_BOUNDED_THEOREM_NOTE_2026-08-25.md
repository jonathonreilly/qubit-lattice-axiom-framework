---
title: "Admissibility — Dirac-Kähler Sectored Interior OS Reconstruction: The Light-Sector Evolution Operator"
date: 2026-08-25
block: 195
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_sectored_interior_os_reconstruction_2026_08_25.py
parent_ref: origin/physics-loop/toe-axiom-closure-block194-transfer-package-mc-generality-20260825
parent_commit: 4cbd56203b020475bc9b24cf04a2d24bfe6da43f
current_main: b11811704efa98a12272d572f666e530a807f6c1
registered: 0
adopted: 0
axiom_movement: none
---

# The Sectored Interior OS Reconstruction — the two-slice shift descends to the eight-dimensional quotient from an interior window, is a positive self-adjoint operator on one momentum sector and carries an exact rank-two defect on the other, with HILBERT SPACE, EVOLUTION, SELF-ADJOINT, POSITIVE and MASS fenced as names for matrix properties throughout

**One sentence.** On Block 190's width family at `T = 16` and `T = 20` the
eight-dimensional OS quotient `H` exists and is positive semidefinite of rank
eight; the two-slice shift does **not** descend from the seam-anchored prefix
presentations the solve tested — invariant obstruction ranks `2, 1, 1` — but
**does** descend, at obstruction rank `0`, from an interior window; and the
descended operator splits along the momentum involution into a **light sector on
which it is a positive self-adjoint operator** and a **heavy sector on which its
self-adjointness defect has exact rank two** — and **not one line of this
supplies gravity, a semigroup, a generator, a Hamiltonian, a continuum time or a
continuum limit**.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Seven imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE RECONSTRUCTION LANGUAGE IS FENCED BEFORE THE FIRST NUMBER IS READ.**

- **NO GRAVITY IS SUPPLIED.** This block supplies no lapse variable in an ADM
  phase space, no shift vector, no Hamiltonian constraint, no momentum
  constraint, no first-class constraint algebra, no Dirac closure, no Dirac
  observable, no gauge orbit and no diffeomorphism quotient. Nine structures,
  enumerated as a measured constant and gated.
- **THE RECONSTRUCTION IS PARTIAL, AND THIS BLOCK SAYS SO FIRST.** The heavy
  sector's defect is exactly rank two and **nothing here removes it**. Asserting
  a complete OS-self-adjoint evolution on all of `H` is a declared mutation
  (`claim_full_reconstruction`) and it fails gate `B`.
- **NO SEMIGROUP AND NO GENERATOR.** One fixed `8 × 8` rational matrix is
  measured. No family `{T^n}` is constructed, no logarithm is taken, no
  generator is extracted and nothing here is a Hamiltonian.
- **NO PHYSICAL MASS.** `theta = acosh(T/2)` is a **logarithm of an algebraic
  number** attached to an exact rational matrix. *Heavy* and *light* **order two
  such numbers**. No particle, no energy, no dispersion relation.
- **THE HEAVY READING STAYS A READING.** Only the **light** sector's `theta` is
  licensed as the spectrum of an OS-self-adjoint positive operator. The heavy
  `theta` remains a property of a matrix that is **not** self-adjoint in the OS
  form.
- **THE DEGENERATE-COPY PAIRING IS REFUTED, NOT ASSUMED.** The rank-two defect
  does **not** pair the two canonical momentum-degenerate copies; the round-2
  check refuted that reading and this block gates the refutation.
- **NO CONTINUUM.** Two widths, two rational points, one profile at unit volume,
  one two-slice shift.

**AND ONE ENUMERATION CHANGED, WHICH IS THE POINT OF THE BLOCK.** Blocks 190 to
194 each listed **ten** unsupplied gravity structures, the tenth being
*Osterwalder–Schrader reconstruction of a transfer operator*. This block lists
**nine**, because it supplies a **sectored, interior-window, single-operator**
version of exactly that tenth item — on **one** of two sectors, with the other
obstructed at rank two. That is the whole change, and it is stated here rather
than buried: nine, not ten, and the missing one is not a relaxation of the fence
but the block's measured content.

**EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER
METAPHYSICAL NECESSITY** — the cycle-913 caution, carried verbatim — and every
positive here is candidacy within this formalism and never a claim about nature.

---

## W1 — the wall, and the charter

### What was open

Blocks 190 to 194 built a transfer package — a positive palindromic-squared
monodromy with two scales, a `U`-grading, parity independence, a locality window
and an `(m, c)` split — and every statement in it was about **pair cores**:
positive-definite `8 × 8` frames carrying **no quotient at all**. Block 190
refuted the naive OS transfer pairing at that level. Three things were therefore
open:

1. **Does the OS Hilbert space even exist here?** Nobody had computed the
   reflected Gram of the **full** positive span.
2. **Does the two-slice shift descend to it?** A core-level asymmetry can be
   pure null-direction contamination, invisible on the quotient — or it can be
   real.
3. **If it descends, is it self-adjoint and positive?** That is the whole
   content of *reconstruction*, and no block had asked it on a quotient.

The solve answered (2) with a **no-go**, and the first adversarial round
**refuted** that no-go by exhibiting interior windows on which the descent
works. This block is what is left standing after that refutation, plus what the
second round confirmed and fenced.

### The charter

1. **Compute `H` itself** — the full-span reflected Gram — and certify its rank
   and its positive semidefiniteness **without a floating inertia call**.
2. **Scope the obstruction honestly**: report the prefix failure as a failure of
   the **presentation**, with an **invariant** measure, and carry the check's
   basis-dependence correction as a **construction** rather than a hedge.
3. **Take the loophole seriously**: build the descended operator on the interior
   window and ask the reconstruction questions of it.
4. **Split the verdict if the object splits.** Do not report one answer for two
   sectors.
5. **Gate the round-2 fence**, so the strongest available reading of the defect
   is refuted in the runner rather than merely avoided in the prose.

---

## N1 — `H` EXISTS, and it is eight-dimensional

**NOTHING BELOW IS ABOUT AN OS QUOTIENT IF THIS SECTION IS NOT EXACT.**

### The construction, carried unchanged

The carrier is Block 190's wrap-edge width family, now read at **two** widths:
the staggered Dirac–Kähler kernel on `Z_T × Z_4` with `eta_t = 1`,
`eta_x = (-1)^t` and the temporal sign `w = -1` on the **wrap edge** `t = T-1`;
the grade-raising `d_K = P1 K P0 + P2 K P1`; the site reflection
`theta_s(t) = -t` with fixed slices `{0, T/2}`; the raising set `A_s` in the
closed half `{0..T/2}` excluding fixed-slice spatial edges; the glue
`D_s = A_s - Ps A_s Ps`; and the completion

```text
Q  =  m H  +  H D_s  -  D_s^T H,        G = Q^-1.
```

`H` is Block 191's quarter-weighted four-corner cell average of the **landed**
Block 105 `shear_hodge(c, v)` at **unit volume**, read through the Block 128
module. That import is the only object imported.

The **new** objects are read on the whole positive span rather than on a pair
core. Let `X_A` be the span of the cells of the slices `{1, ..., T/2-1}`:

```text
K_AA[a,b] = G[idx(t_b,   x_b), idx(theta_s t_a, x_a)]        (the OS Gram)
M_2 [a,b] = G[idx(t_b+2, x_b), idx(theta_s t_a, x_a)]        (the shifted form)
H         = X_A / rad(K_AA).
```

### The Gram closes, and `H` is eight-dimensional

| `(m, c)` | `T` | `X_A` | `rank(K_AA)` | `nnz(K_AA - K_AA^T)` |
| --- | ---: | ---: | ---: | ---: |
| `(9/20, 5/13)` | 16 | `28` | **8** | `0` |
| `(9/20, 5/13)` | 20 | `36` | **8** | `0` |
| `(1/2, 1/3)` | 16 | `28` | **8** | `0` |
| `(1/2, 1/3)` | 20 | `36` | **8** | `0` |

Gate `C-1`, with `rank(Q) = 64` and `80`.

### And it is POSITIVE SEMIDEFINITE of that rank, certified without a float

Symmetric of rank eight is not enough: an OS Hilbert space needs the form to be
**positive**. The certificate is exact and uses **no floating inertia call**.
Take the eight-column frame `E` of the pivot representatives, and set

```text
K_c = E^T K_AA E,      V#  = K_c^-1 E^T K_AA,      P = E V#.
```

Then all eight leading minors of `K_c` are **positive** — Sylvester on a matrix
whose symmetry residual is measured `0` in the same gate — and

```text
nnz( K_AA - K_AA E K_c^-1 E^T K_AA )  =  0,
nnz(V# E - I) = nnz(P^2 - P) = nnz(P^T K_AA - K_AA P) = nnz(K_AA (I - P)) = 0.
```

The Schur residual being exactly zero says the whole form is recovered from the
frame; the four projector identities say `E` is an exact **isometric section**
of the quotient. Hence `K_AA` is positive semidefinite of rank eight and `H` is
a genuine eight-dimensional inner-product space. Gates `C-2`, `C-3`.

---

## N2 — THE PREFIX OBSTRUCTION AND THE INTERIOR LOOPHOLE

### The question, stated as a kernel containment

For a domain `D` of slices write `K_AD` for the full-row, `D`-column restriction
of the Gram and `M_2` for the same restriction of the shifted form. The
assignment `[g] |-> [tau^2 g]` is representative-independent **exactly when**

```text
ker(K_AD)  is contained in  ker(M_2),
```

equivalently when the **invariant** obstruction

```text
rank( vstack(K_AD, M_2) )  -  rank(K_AD)
```

vanishes. That number, and not a count of basis vectors, is what this block
measures.

### The seam-anchored prefix domains do obstruct

| `T` | `dmax` | `rank(K_AD)` | `dim ker(K_AD)` | **invariant obstruction rank** |
| ---: | ---: | ---: | ---: | ---: |
| 16 | 5 | 8 | 12 | **2** |
| 16 | 4 | 8 | 8 | **1** |
| 16 | 3 | 8 | 4 | **1** |
| 20 | 7 | 8 | 20 | **2** |
| 20 | 6 | 8 | 16 | **1** |
| 20 | 5 | 8 | 12 | **1** |

Identical at `(9/20, 5/13)` and `(1/2, 1/3)`. Gate `D-1`, and `G-3` for the
second point. `rank(K_AD) = 8` **throughout**: the prefix already spans the
quotient, so its failure is a failure of the **presentation** and not of the
quotient.

### The check's `C2` correction, carried as a CONSTRUCTION

The solve reported *how many kernel vectors violate*. The adversarial check
showed those counts are **not invariants of the kernel**. The repair here is not
a hedge but three explicit presentations of **the same** kernel:

- the **default** presentation — SymPy's nullspace basis, which is what the
  solve read;
- the **adapted** presentation — the pivot columns of `M_2 N` followed by a
  basis of `ker(M_2 N)` pulled back through `N`;
- the **all-violating** presentation — the adapted one with a single violating
  vector added to every joint-null vector.

| `T` | `dmax` | default | adapted | all-violating | `dim ker` |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 5 | `8` | **`2`** | `12` | 12 |
| 16 | 4 | `6` | **`1`** | `8` | 8 |
| 16 | 3 | `2` | **`1`** | `4` | 4 |
| 20 | 7 | `14` | **`2`** | `20` | 20 |
| 20 | 6 | `12` | **`1`** | `16` | 16 |
| 20 | 5 | `8` | **`1`** | `12` | 12 |

All three are exact bases — the runner measures the rank of each spanning set
and requires it to equal the nullity — and the adapted count is **exactly the
invariant rank** while the all-violating count is **exactly the nullity**.
Therefore

> the number of violating kernel vectors is **not** an invariant; the **rank**
> is.

Gate `D-2`, mutation `break_basis_dependence`.

### What IS invariant, and it is the support

The residual `M_2 N` has column support meeting **every** positive slice —
`{1..7}` at `T = 16` and `{1..9}` at `T = 20` — at every listed depth and both
points. Unlike the counts, this is unchanged by any kernel-basis change, because
the column space is. Gate `D-3`.

### The loophole, and it is why this block exists

The adversarial check scanned every contiguous window whose `+2` shift stays in
the positive span, and found that windows off **both** seam layers descend. This
block carries the widest such window per width — the ones obeying `start >= 2`
and `end + 2 <= T/2 - 2`:

| `T` | interior window `D` | `rank(K_AD)` | `dim ker(K_AD)` | obstruction |
| ---: | --- | ---: | ---: | ---: |
| 16 | `{2, 3, 4}` | 8 | 4 | **0** |
| 20 | `{2, 3, 4, 5, 6}` | 8 | 12 | **0** |

At both points. The kernels are **nontrivial** — dimension four and twelve — so
this is not the vacuous case, and `rank(K_AD) = 8` means the window **surjects
onto all of `H`**. Gate `D-4`, mutation `break_interior_loophole`.

**The solve's reading is corrected here, not softened.** *Bulk-distributed and
width-persistent* was an artifact of measuring a presentation-dependent count on
seam-anchored domains only. The obstruction is a **near-seam** phenomenon, and
the honest scope of the negative result is exactly the prefix presentations.

---

## N3 — THE DESCENT, and its spectrum is the landed monodromy

### The operator

On the interior window the pushforward is well defined, so

```text
T_2  =  q_A  tau^2  q_D^-1
```

is a genuine operator on the whole eight-dimensional quotient. In the pivot
section — the eight cells returned by the exact `rref` pivots of `K_AD`, which
are the pair core at slices `{2, 3}` — it is

```text
K_c T_2 = M_2c ,        residual nnz(K_c T_2 - M_2c) = 0 ,
```

with `K_c` symmetric (`nnz(K_c - K_c^T) = 0`) and all eight leading minors
positive: the quotient carries a genuine inner product. Gate `E-1`.

### Shifted reflection positivity holds as a FORM

The symmetric part of the shifted form has all eight leading minors **positive**
at both widths and both points:

```text
leading-minor signs of ( M_2c + M_2c^T ) / 2   =   (+,+,+,+,+,+,+,+).
```

So what fails on the heavy sector is **symmetry**, not positivity — a
distinction the whole block turns on. Gate `E-2`.

### The spectrum, and it is not new content

`charpoly(T_2)` factors over `QQ` into exactly the two **landed Block 194**
primitive palindromic quadratics, each of multiplicity two, at **both** widths:

| `(m, c)` | light factor | heavy factor |
| --- | --- | --- |
| `(9/20, 5/13)` | `39529825 z^2 - 109432706 z + 39529825` | `22569375 z^2 - 233631106 z + 22569375` |
| `(1/2, 1/3)` | `233 z^2 - 690 z + 233` | `739 z^2 - 7258 z + 739` |

The coefficients are Block 194's landed `T = 16` values; that the **same** pair
appears at `T = 20` is measured **here**, and is consistent with Block 190's
width-independence rather than inherited from it. Gate `E-3`. Block 194's monic-normalization correction is **carried forward as
the same formula** rather than re-committed: SymPy's characteristic polynomial
is monic, so for factors `a_l z^2 + b_l z + a_l` and `a_h z^2 + b_h z + a_h`,

```text
(a_l z^2 + b_l z + a_l)^2 (a_h z^2 + b_h z + a_h)^2  =  s · charpoly_monic(T_2),
                                            s  =  (a_l a_h)^2 ,
```

with `s = 795955611005101889386962890625` and `s = 29648362969`, each at exactly
zero polynomial residual. Gate `E-4`, mutation `break_monic_normalization`.

### And the descended operator IS the landed `W`

Taking the **deep pair core** `t0 = 3` as the section reproduces Block 190's own
matrices entrywise:

```text
nnz( K_section - K_c(t0 = 3) ) = 0 ,     nnz( M_section - L_2(t0 = 3) ) = 0 ,
```

so in that section `T_2 = K_c^-1 L_2 = W`. Gate `E-5`. This is the sharpest
correction of the solve in the block: the monodromy spectrum is **operator
content on the interior window**, not merely frame content — the earlier reading
was a consequence of the prefix no-go, and the prefix no-go was the wrong scope.

---

## N4 — THE SECTOR THEOREM, and it is the block

### The split is orthogonal and exact

Let `U` be the two-site spatial shift on the eight representatives. Then

```text
nnz( U^T K_c U - K_c ) = 0 ,      nnz( T_2 U - U T_2 ) = 0 ,
nnz( b_+^T K_c b_- )   = 0 ,      nnz( b_+^T M_2c b_- ) = 0 ,
```

at both widths and both points, so `H = H_+ (+) H_-` is an orthogonal direct sum
of two four-dimensional sectors for **both** forms, and `T_2` preserves each.
Gate `F-1`.

### The light sector: a positive self-adjoint operator

In the rational light basis `e_(t,0) + e_(t,2)` and `e_(t,1) + e_(t,3)` for the
two core slices:

```text
nnz( M_+ - M_+^T ) = 0                       (the shifted form is SYMMETRIC)
leading-minor signs of K_+ = (+,+,+,+)       (the Gram is POSITIVE DEFINITE)
leading-minor signs of M_+ = (+,+,+,+)       (the form  is POSITIVE DEFINITE)
nnz( K_+ T_+ - T_+^T K_+ ) = 0               (T_+ is K_+-SELF-ADJOINT)
```

at both widths and both points. Since `M_+ = K_+ T_+` is symmetric,
`<T_+ v, w>_{K_+} = <v, T_+ w>_{K_+}`; since `M_+` is positive definite,
`<T_+ v, v>_{K_+} > 0` for every `v != 0`. **`T_+` is a positive self-adjoint
operator on the light sector of `H`.** Gate `F-2`.

**Its spectrum, with no radical ever evaluated.** `charpoly(T_+)` is the light
quadratic **squared**; the quadratic annihilates `T_+` exactly; its constant
equals its leading coefficient, so the two roots have product `1`; its
discriminant is positive and is **not** a perfect square —
`5725088884359936` at `(9/20, 5/13)` and `258944` at `(1/2, 1/3)`, tested by
integer square root and never by a radical; and its trace `-b/a` exceeds `2`.
Therefore the eigenvalues are the reciprocal pair `e^{±theta_light}`, each of
multiplicity two, with `theta_light = acosh(T/2) > 0` real. Gate `F-3`.

### The heavy sector: an exact rank-two obstruction

```text
leading-minor signs of K_-                 = (+,+,+,+)
leading-minor signs of (M_- + M_-^T)/2     = (+,+,+,+)
rank( M_- - M_-^T )                        = 2
nnz ( M_- - M_-^T ) = nnz(K_- T_- - T_-^T K_-) = 8
charpoly(T_-)                              = the HEAVY quadratic squared
```

at both widths and both points. The heavy sector's Gram and the symmetric part
of its shifted form are positive definite, and its evolution is nevertheless
**not** OS-self-adjoint. Gate `F-4`.

### The defect is entirely heavy, and exactly so

On the whole quotient `D = M_2c - M_2c^T` has rank `2` with `32` nonzero
entries, and its spectral-projector ranks in the order `(+,+)`, `(-,-)`,
`(+,-)`, `(-,+)` are

```text
( 0 , 2 , 0 , 0 ) ,
```

with `nnz(U^T D U - D) = 0` and `nnz(U D - D U) = 0`. Zero on the light sector,
two on the heavy sector, zero on both cross blocks — at both widths and both
points. Gate `F-5`.

**That split is the theorem.** The light mode of this gravitational sector has a
reconstructed positive self-adjoint two-slice evolution on its sector of `H`;
the heavy mode has an exact rank-two obstruction to one.

### None of it is a pivot artifact

Two **declared** alternative sections are carried: the deep pair core at slices
`{3, 4}`, and a **scattered** eight-cell section deliberately not closed under
the displayed `U`. For the exact change of section `P`,

```text
det P != 0 ,
nnz(K_alt - P^T K_c P) = nnz(M_alt - P^T M_2c P) = 0 ,
nnz(T_alt - P^-1 T_2 P) = 0 ,      nnz(U_alt^2 - I) = 0 ,
```

and every sector statement — light defect rank `0`, heavy defect rank `2`, both
positivity certificates — is reproduced. For the scattered section `U_alt` is
**not** a coordinate permutation, which is exactly the point: the sector
statements are congruence and similarity statements about the quotient, not
facts about a lucky basis. Gate `F-6`.

---

## N4b — THE DEFECT, AND WHAT IT IS NOT

### Its exact shape, over `QQ`, with no normalisation

In the **declared** heavy basis
`-e_(2,0)+e_(2,2)`, `-e_(2,1)+e_(2,3)`, `-e_(3,0)+e_(3,2)`, `-e_(3,1)+e_(3,3)`
at `T = 16` and `(9/20, 5/13)`, the heavy defect is the exact rational multiple
`s J` of an integer skew matrix,

```text
s = 15412245266178664398193359375000000
    / 12468368115055868578374473995988256597352642542544230293 ,

J = [[            0,            0, -499791697674660,  1588013041094501],
     [            0,            0,   12377859914160,   -39328790486076],
     [ 499791697674660, -12377859914160,            0,                0],
     [-1588013041094501,  39328790486076,            0,                0]] ,
```

and it factors exactly as a two-direction wedge

```text
D_- = gamma ( u v^T - v u^T ) ,     gamma = -s ,
u = (0, 0, 2034493740, -6464298239) ,      v = (-245659, 6084, 0, 0) ,
u^T u = 45926316500837688721 ,   v^T v = 60385359337 ,   u^T v = 0 ,
```

at zero reconstruction residual. The directions are left **unnormalised** on
purpose: normalising them would introduce square roots and the certificate would
leave `QQ`. Gate `F-7`.

### The stronger reading is REFUTED, and the refutation is gated

The heavy discriminant

```text
52545986939220736  =  2^8 · 13 · 31 · 37 · 71 · 313^2 · 1979
```

is **not** a rational square, so the heavy rational module is two isomorphic
copies of **one** irreducible quadratic module. The one-site spatial shift,
restricted to the heavy sector, is an exact commuting **complex structure**:

```text
nnz( S_-^2 + I ) = 0 ,        nnz( S_- T_- - T_- S_- ) = 0 ,
```

which canonically distinguishes those two copies after scalar extension. A
defect that **purely paired** the copies would satisfy `S_-^T D_- S_- = D_-`. It
does not:

```text
nnz( S_-^T D_- S_- - D_- ) = 8 ,      nnz( S_-^T D_- S_- + D_- ) = 8 ,
rank( (D_- + S_-^T D_- S_-)/2 ) = 4 , rank( (D_- - S_-^T D_- S_-)/2 ) = 4 .
```

Both parity components have **full** rank four, so the rank-two cancellation
mixes cross-copy and within-copy parts. The only basis-free statements this
block makes about the defect are that it is **rank two**, **entirely heavy** and
**`U`-equivariant**; its block-off-diagonal appearance in the displayed
coordinates is a coordinate fact and **not** a spectral theorem. Gate `F-8`,
mutations `break_pairing_fence` and `claim_defect_pairs_copies`.

---

## N4c — THE SECOND POINT, and what moves with it

At `(m, c) = (1/2, 1/3)` and at **both** widths: obstruction rank `0`, `K_c`
symmetric with eight positive leading minors, defect rank `2`, projector ranks
`(0, 2, 0, 0)`, the light form symmetric and positive definite, the heavy
symmetric part positive definite — every structural invariant unchanged. Gate
`G-1`.

The **coefficients** move, as they must: `(233, -690, 233)` and
`(739, -7258, 739)` against `(39529825, -109432706, 39529825)` and
`(22569375, -233631106, 22569375)`, with monic scalar `29648362969` against
`795955611005101889386962890625`. Gate `G-2`. **The structure is of the class
and the coefficients are of the point** — and two points are not a scan.

The prefix obstruction also persists unchanged at the second point — ranks
`2, 1, 1` at both widths, the same kernel dimensions, the same all-slice
support — so the near-seam failure is a property of the **presentation** and not
of the point. Gate `G-3`.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

- **`Hilbert space`** names a **rank-eight quotient** of a finite rational
  vector space by the radical of an exact rational form. No completion, no
  infinite dimension, no separability question.
- **`evolution`** names **one fixed `8 × 8` rational matrix**. Not a semigroup,
  not a flow, not a one-parameter family.
- **`self-adjoint`** names `nnz(K T - T^T K) = 0` in that finite form. It is not
  essential self-adjointness and there is no domain question.
- **`positive`** names **exact leading-minor signs of a symmetric rational
  matrix**. Sylvester's criterion certifies definiteness for a symmetric matrix
  and for nothing else, so every gate that reads those signs measures the
  symmetry residual of the same matrix in the same gate.
- **`mass`**, **`heavy`**, **`light`** order two numbers `acosh(T/2)` for
  rational traces `T > 2` — **logarithms of algebraic numbers**.
- **`interior`** names `start >= 2` and `end + 2 <= T/2 - 2` at two widths. It
  is not a bulk, not a thermodynamic limit and not an asymptotic statement.

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within this imposed finite matrix construction at `T = 16` and `T = 20`, at
> `(m, c) = (9/20, 5/13)` and `(1/2, 1/3)`, the reflected Gram of the full
> positive span is positive semidefinite of rank eight; the two-slice shift has
> invariant obstruction ranks `2, 1, 1` from the seam-anchored prefix
> presentations and obstruction rank `0` from the stated interior window; and the
> operator it induces on the eight-dimensional quotient is, on the `U = +1`
> sector, self-adjoint and positive for the quotient Gram, and on the `U = -1`
> sector has an antisymmetric part of exact rank two.

### Four further fences, all four self-imposed

1. **THE INTERIOR WINDOW IS IMPOSED, NOT DERIVED.** It comes from the
   adversarial check's contiguous-window scan at two widths. No
   width-independent proof of the near-seam and far-seam boundary layers is
   offered here.
2. **THE RANK TWO IS MEASURED, NOT EXPLAINED.** Why the heavy defect is rank two
   rather than four — or zero — has no mechanism in this block.
3. **NOTHING IS SAID ABOUT OTHER PRESENTATIONS.** Whether some other admissible
   presentation of the same quotient carries a self-adjoint **heavy** sector is
   not decided either way.
4. **TWO WIDTHS ARE NOT A FAMILY THEOREM.** Every statement is gated at `T = 16`
   and `T = 20` and at nothing else.

### What IS derived, stated positively so the fence is not mistaken for a retreat

The equivalence *descent if and only if kernel containment if and only if zero stacked-rank excess* is
**derived**, and it is what makes the obstruction an invariant rather than a
count. The positive semidefiniteness of `K_AA` is **derived** from the frame's
minors plus the exact Schur identity. The self-adjointness and positivity of
`T_+` are **derived** from the symmetry and definiteness of `M_+` — not read off
a spectrum. And the sector statements are **derived** as congruence and
similarity invariants, which is why two alternative sections reproduce them.

---

## READINGS — five of them, and each is a reading

- **`R1`.** *That `theta_light` is a physical mass because it is now the
  spectrum of a genuine self-adjoint operator.* Measured: `acosh(T/2)` for a
  rational `T` attached to a `4 × 4` rational matrix. The operator upgrade is
  real; the physics is not supplied. **Reading.**
- **`R2`.** *That `theta_heavy` is a mass at all.* Measured: an eigenvalue of a
  matrix that is **not** self-adjoint in the OS form. Weaker than `R1`, and
  fenced twice. **Reading.**
- **`R3`.** *That the rank-two defect pairs the two momentum-degenerate copies.*
  **Refuted** — the `S`-parity components each have rank four. Not a reading:
  a false statement, gated as false.
- **`R4`.** *That the interior window is "the bulk" and the seam layers are
  boundary effects that vanish in a limit.* Measured: two windows at two widths.
  No limit is taken. **Reading.**
- **`R5`.** *That this is an OS reconstruction of the gravitational sector.*
  Measured: one two-slice operator on one sector of a finite quotient, with the
  other sector obstructed. **Reading**, and the block's own banner says so.

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | family |
| ---: | --- | --- | --- |
| 1 | `origin/main`, axiom and registry blobs, worktree blobs, timeout | five pins fixed | `A` |
| 2 | `PARENT_COMMIT` ancestry, both Block 194 artifacts, stale pin carrying neither | exact | `A` |
| 3 | imposed / registered / adopted | `7 / 0 / 0` | `B` |
| 4 | gravity structures enumerated as NOT SUPPLIED | `9` | `B` |
| 5 | `FULL_RECONSTRUCTION_CLAIMED`, `HEAVY_READING_LICENSED_CLAIMED` | both `False` | `B` |
| 6 | `DEFECT_PAIRS_COPIES_CLAIMED`, `SEMIGROUP_CLAIMED` | both `False` | `B` |
| 7 | `PHYSICAL_MASS`, `CONTINUUM_LIMIT` | both `False` | `B` |
| 8 | `rank(Q)`, `X_A`, `rank(K_AA)`, `nnz(K_AA - K_AA^T)` | `64/80`, `28/36`, `8`, `0` | `C` |
| 9 | frame minors, exact Schur residual | `(+)^8`, `0` | `C` |
| 10 | `nnz(V#E - I)`, `nnz(P^2 - P)`, `nnz(P^T K - K P)`, `nnz(K(I-P))` | `(0,0,0,0)` | `C` |
| 11 | prefix invariant obstruction ranks; `rank(K_AD)`; nullities | `2,1,1` both widths; `8`; the table in `N2` | `D` |
| 12 | the three presentations: default, adapted `= rank`, all-violating `= nullity`, each an exact basis | the table in `N2` | `D` |
| 13 | `VIOLATION_COUNT_IS_INVARIANT` | `False` | `D` |
| 14 | residual row-slice support, invariant under basis change | all positive slices | `D` |
| 15 | interior windows: obstruction, nullity, `rank(K_AD)` | `0`; `4/12`; `8` | `D` |
| 16 | quotient dimension; `nnz(K_c - K_c^T)`; `K_c` minors; `nnz(K_c T_2 - M_2c)` | `8`; `0`; `(+)^8`; `0` | `E` |
| 17 | `(M_2c + M_2c^T)/2` minors | `(+)^8` | `E` |
| 18 | `charpoly(T_2)` = the two landed quadratics, multiplicity `2`, both widths | the table in `N3` | `E` |
| 19 | `(a_l z^2+b_l z+a_l)^2 (a_h z^2+b_h z+a_h)^2 = s · charpoly_monic`, `s = (a_l a_h)^2` | residual `0`, two scalars | `E` |
| 20 | deep pair-core section reproduces `K_c(t0=3)`, `L_2(t0=3)` | `(0, 0)` | `E` |
| 21 | `nnz(U^T K_c U - K_c)`, `nnz(T_2 U - U T_2)`, both cross blocks | `0`, `0`, `(0, 0)` | `F` |
| 22 | light: defect rank/`nnz`, self-adjointness residual, `K_+` and `M_+` minors | `0`, `0`, `0`, `(+)^4`, `(+)^4` | `F` |
| 23 | light spectrum: quadratic squared, annihilation, discriminants, product `1`, trace `> 2` | exact, both points | `F` |
| 24 | heavy: defect rank/`nnz`, `K_-` and `Sym(M_-)` minors, charpoly | `2`, `8`, `(+)^4`, `(+)^4`, `heavy^2` | `F` |
| 25 | complete defect rank, `nnz`, projector ranks, `U`-equivariance | `2`, `32`, `(0,2,0,0)`, `(0,0)` | `F` |
| 26 | two alternative sections: `det P != 0`, congruence, similarity, `U_alt^2 = I`, sectors unchanged | `(0,0,0,0)` | `F` |
| 27 | scattered section's `U_alt` is a coordinate permutation | `False` | `F` |
| 28 | the wedge: `s`, `J`, `gamma = -s`, `u`, `v`, norms, residual | exact, residual `0` | `F` |
| 29 | heavy discriminant is a perfect square; `S_-^2 + I`; `[S_-, T_-]` | `False`; `0`; `0` | `F` |
| 30 | `nnz(S^T D S - D)`, `nnz(S^T D S + D)`; `S`-parity component ranks; `DEFECT_PURELY_PAIRS_COPIES` | `(8, 8)`; `(4, 4)`; `False` | `F` |
| 31 | the second point's structural sextuple, both widths | unchanged | `G` |
| 32 | the second point's polynomials and monic scalar | changed | `G` |
| 33 | the second point's prefix ranks, nullities, support | `2,1,1`; unchanged | `G` |
| 34 | the note at its final path; `N5` byte-identical; `sp.nsimplify` count | present; verbatim; `0` | `H` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

**Dead end one — counting violating kernel vectors.** The solve's `8/12`,
`6/8`, `2/4` are counts of one unspecified basis. The same kernel admits a basis
in which exactly `rank` many violate and one in which **all** of them do. What
survives is the rank. This is `N2`, and it is the correction that reopened the
question.

**Dead end two — testing only seam-anchored prefixes.** Every domain the solve
tested started at slice `1`. Moving the window off both seam layers changes the
answer completely. A no-go tested on one family of presentations is a statement
about that family.

**Dead end three — reading a core-level asymmetry as a quotient statement.**
Block 190's `L_2 - L_2^T` is a **pair-core** residual. On the quotient the right
object is `M_2c - M_2c^T`, and its rank-two heaviness is invisible at core
level.

**Dead end four — treating `M_2c`'s positive leading minors as a positivity
certificate.** `M_2c` is not symmetric, so its minors certify nothing. The
positivity statement that **is** true is about the symmetric part, and that is
what `E-2` gates.

**What actually worked.** Replacing every count by a **rank**, every
"the operator exists" by an explicit **kernel containment**, and every
positivity claim by **leading minors of a matrix whose symmetry residual is
measured zero in the same gate** — and then splitting along `U` before asking
the self-adjointness question, rather than after.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE RECONSTRUCTION LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), THE FULL POSITIVE SPAN X_A over the slices {1..T/2-1} with its REFLECTED GRAM K_AA[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)] and its TWO-SLICE SHIFTED PAIRING M_2[a,b] = G[idx(t_b+2, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE SEAM-ANCHORED PREFIX DOMAINS D = {1..dmax} for dmax in {5, 4, 3} at T = 16 and {7, 6, 5} at T = 20, THE INTERIOR WINDOWS D = {2, 3, 4} at T = 16 and D = {2..6} at T = 20 CHOSEN BY THE ADVERSARIAL CHECK's OWN SCAN AND DERIVED FROM NOTHING, THE PIVOT SECTION of eight representative cells with its two DECLARED ALTERNATIVE SECTIONS, THE MOMENTUM INVOLUTION U as the two-site spatial shift and the ONE-SITE SHIFT S, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORDS OS RECONSTRUCTION AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, ON AN INTERIOR WINDOW AND ON ONE OF ITS TWO MOMENTUM SECTORS, THE TWO-SLICE SHIFT DESCENDS TO THE EIGHT-DIMENSIONAL QUOTIENT AS A POSITIVE SELF-ADJOINT OPERATOR -- AND ON THE OTHER SECTOR IT DOES NOT. THE RECONSTRUCTION IS PARTIAL AND THIS BLOCK SAYS SO FIRST. 'HILBERT SPACE' NAMES A RANK-EIGHT QUOTIENT OF A FINITE RATIONAL VECTOR SPACE BY THE RADICAL OF AN EXACT RATIONAL FORM, 'EVOLUTION' NAMES ONE FIXED 8 x 8 RATIONAL MATRIX AND NEVER A SEMIGROUP, 'SELF-ADJOINT' NAMES nnz(K T - T^T K) = 0 IN THAT FINITE FORM, 'POSITIVE' NAMES EXACT LEADING-MINOR SIGNS OF A SYMMETRIC RATIONAL MATRIX, and 'MASS' NAMES acosh(T/2) FOR A RATIONAL TRACE T > 2 AND THEREFORE A LOGARITHM OF AN ALGEBRAIC NUMBER. NO SEMIGROUP IS SUPPLIED, NO GENERATOR IS SUPPLIED, NO CONTINUUM TIME IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: TWO WIDTHS AND TWO RATIONAL POINTS ARE NOT A LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE OS HILBERT SPACE EXISTS AND IT IS EIGHT-DIMENSIONAL, AND THE PREFIX NO-GO OF THE SOLVE IS NARROWED BY THE ADVERSARIAL CHECK's OWN LOOPHOLE. The reflected Gram of the FULL positive span is EXACTLY SYMMETRIC at nnz(K_AA - K_AA^T) = 0 and has EXACT RANK 8 at T = 16 (28 x 28) and T = 20 (36 x 36) and at both (m, c) = (9/20, 5/13) and (1/2, 1/3), so H = X_A / rad(K_AA) is EIGHT-DIMENSIONAL; and it is POSITIVE SEMIDEFINITE OF RANK EIGHT rather than merely symmetric of rank eight, certified WITHOUT A FLOATING INERTIA CALL by an eight-column frame E whose compressed Gram K_c = E^T K_AA E has all EIGHT leading minors POSITIVE together with the EXACT SCHUR IDENTITY nnz(K_AA - K_AA E K_c^-1 E^T K_AA) = 0 and the projector identities nnz(V# E - I) = nnz(P^2 - P) = nnz(P^T K_AA - K_AA P) = nnz(K_AA (I - P)) = 0 for V# = K_c^-1 E^T K_AA and P = E V#. ON THE SEAM-ANCHORED PREFIX DOMAINS D = {1..dmax} THE TWO-SLICE SHIFT DOES NOT DESCEND: the invariant obstruction rank(M_2 | ker K_AD) is 2, 1, 1 at dmax = 5, 4, 3 and again 2, 1, 1 at dmax = 7, 6, 5, at BOTH widths and BOTH points, and the residual column support meets EVERY positive slice. THE SOLVE'S COUNTS OF VIOLATING KERNEL VECTORS WERE PRESENTATION-DEPENDENT AND THE CORRECTION IS CARRIED AS A CONSTRUCTION: in SymPy's default nullspace presentation the counts are 8, 6, 2 and 14, 12, 8, in an ADAPTED presentation of the SAME kernel -- pivot columns of M_2 N followed by ker(M_2 N) pulled back through N -- exactly rank many vectors violate, namely 2, 1, 1, and in an ALL-VIOLATING presentation obtained by adding one violating vector to every joint-null one, ALL of them violate, namely 12, 8, 4 and 20, 16, 12; all three presentations are exact bases of the same kernel, so THE COUNT IS NOT AN INVARIANT AND THE RANK IS. AND THE PREFIX PRESENTATION IS NOT THE QUOTIENT: on the INTERIOR windows D = {2, 3, 4} at T = 16 and D = {2..6} at T = 20 the obstruction rank is EXACTLY ZERO with kernels of dimension 4 and 12 -- nontrivial, not vacuous -- and rank(K_AD) = 8, so the window surjects onto all of H.\nper_mode: THE DESCENT EXISTS ON THE INTERIOR WINDOW AND ITS SPECTRUM IS THE LANDED BULK MONODROMY. Because ker(K_AD) is contained in ker(M_2) on the interior window, the assignment [g] |-> [tau^2 g] is representative-independent and T_2 = q_A tau^2 q_D^-1 is a genuine operator on the whole eight-dimensional quotient; in the pivot section it is T_2 = K_c^-1 M_2c with nnz(K_c T_2 - M_2c) = 0. THE COMPRESSED GRAM IS A GENUINE INNER PRODUCT: nnz(K_c - K_c^T) = 0 with all eight leading minors POSITIVE. THE SHIFTED FORM IS POSITIVE AS A FORM: the symmetric part (M_2c + M_2c^T)/2 has all eight leading minors POSITIVE at both widths and both points, so shifted reflection positivity holds on H and what fails is SYMMETRY and not positivity. THE SPECTRUM IS NOT NEW CONTENT AND THAT IS THE POINT: charpoly(T_2) factors over QQ into exactly the two LANDED Block 194 primitive palindromic quadratics, each of multiplicity two, at BOTH widths -- (22569375 z^2 - 233631106 z + 22569375) and (39529825 z^2 - 109432706 z + 39529825) at (9/20, 5/13), and (233 z^2 - 690 z + 233) and (739 z^2 - 7258 z + 739) at (1/2, 1/3) -- and BLOCK 194's MONIC-NORMALIZATION CORRECTION IS CARRIED FORWARD AS THE SAME FORMULA rather than re-committed: the product of those factors equals s times the MONIC characteristic polynomial with s = (a_light a_heavy)^2 exactly, s = 795955611005101889386962890625 and s = 29648362969, each at ZERO polynomial residual. AND THE OPERATOR IS THE LANDED ONE: taking the DEEP PAIR CORE t0 = 3 as the section reproduces Block 190's K_c and L_2 entrywise, so the descended operator IS W = K_c^-1 L_2 in that section, with change-of-section congruence residuals nnz(K_alt - P^T K P) = nnz(M_alt - P^T M P) = 0 and similarity residual nnz(T_alt - P^-1 T_2 P) = 0. THE MONODROMY SPECTRUM IS THEREFORE OPERATOR CONTENT ON THE INTERIOR WINDOW AND NOT MERELY FRAME CONTENT, WHICH IS THE SOLVE'S OWN READING CORRECTED.\nper_block: THE SECTOR THEOREM, AND IT IS THE BLOCK. The momentum involution U -- the two-site spatial shift -- is an EXACT ISOMETRY of the quotient Gram at nnz(U^T K_c U - K_c) = 0 and commutes with the descended operator at nnz(T_2 U - U T_2) = 0, and its two eigenspaces are ORTHOGONAL for both forms at nnz(b_+^T K_c b_-) = nnz(b_+^T M_2c b_-) = 0, so H splits as an ORTHOGONAL DIRECT SUM of a four-dimensional LIGHT sector U = +1 and a four-dimensional HEAVY sector U = -1 and the descended operator preserves each. ON THE LIGHT SECTOR THE RECONSTRUCTION IS COMPLETE: in the rational basis e_(t,0) + e_(t,2) and e_(t,1) + e_(t,3) the restricted shifted form is ENTRYWISE SYMMETRIC at nnz(M_+ - M_+^T) = 0, both K_+ and M_+ have all four leading minors POSITIVE, and therefore T_+ = K_+^-1 M_+ satisfies nnz(K_+ T_+ - T_+^T K_+) = 0 and is a POSITIVE SELF-ADJOINT OPERATOR for the inner product K_+; its characteristic polynomial is the LIGHT quadratic squared, its trace exceeds 2 with positive discriminant and unit root product, so its spectrum is the doubly degenerate positive reciprocal pair e^{+/- theta_light} -- 5725088884359936 and 258944 are the two discriminants and neither is a perfect square. ON THE HEAVY SECTOR IT IS NOT: K_- and the symmetric part (M_- + M_-^T)/2 both have all four leading minors POSITIVE and the characteristic polynomial is the HEAVY quadratic squared, but the antisymmetric defect D_- = M_- - M_-^T is NONZERO of EXACT RANK 2, so nnz(K_- T_- - T_-^T K_-) = 8 and T_- is NOT self-adjoint in the OS form. THE DEFECT IS ENTIRELY HEAVY AND EXACTLY LOCALIZED: on the whole quotient the defect M_2c - M_2c^T has rank 2 with 32 nonzero entries, and its spectral-projector ranks in the order (+,+), (-,-), (+,-), (-,+) are (0, 2, 0, 0) -- ZERO on the light sector, TWO on the heavy sector and ZERO on both cross blocks -- at both widths and both points. THAT SPLIT IS THE THEOREM: THE LIGHT MODE OF THE GRAVITATIONAL SECTOR HAS A RECONSTRUCTED POSITIVE SELF-ADJOINT TWO-SLICE EVOLUTION ON ITS SECTOR OF H, AND THE HEAVY MODE HAS AN EXACT RANK-TWO OBSTRUCTION TO ONE.\nlattice_wide: THE DEFECT IS RANK TWO, HEAVY AND U-EQUIVARIANT -- AND IT IS NOT A PAIRING OF THE TWO DEGENERATE COPIES, WHICH IS THE ROUND-TWO FENCE. On the whole quotient the defect is EXACTLY U-EQUIVARIANT at nnz(U^T D U - D) = 0 and nnz(U D - D U) = 0. In the DECLARED heavy basis -e_(2,0) + e_(2,2), -e_(2,1) + e_(2,3), -e_(3,0) + e_(3,2), -e_(3,1) + e_(3,3) at T = 16 and (m, c) = (9/20, 5/13) it is the exact rational multiple s J of the integer skew matrix J with rows (0, 0, -499791697674660, 1588013041094501), (0, 0, 12377859914160, -39328790486076), (499791697674660, -12377859914160, 0, 0) and (-1588013041094501, 39328790486076, 0, 0), where s = 15412245266178664398193359375000000/12468368115055868578374473995988256597352642542544230293, and it admits the EXACT two-direction wedge factorization D_- = gamma (u v^T - v u^T) with gamma = -s, u = (0, 0, 2034493740, -6464298239), v = (-245659, 6084, 0, 0), u^T u = 45926316500837688721, v^T v = 60385359337, u^T v = 0 and ZERO reconstruction residual. THE STRONGER READING IS REFUTED AND THE REFUTATION IS GATED. The heavy rational module is two isomorphic copies of one irreducible quadratic module -- the heavy discriminant 52545986939220736 = 2^8 x 13 x 31 x 37 x 71 x 313^2 x 1979 is NOT a rational square -- and the ONE-SITE spatial shift restricted to the heavy sector is an EXACT commuting complex structure with nnz(S_-^2 + I) = 0 and nnz(S_- T_- - T_- S_-) = 0, which canonically distinguishes the two momentum copies after scalar extension. A defect that PURELY PAIRED those copies would satisfy S_-^T D_- S_- = D_-. IT DOES NOT: nnz(S_-^T D_- S_- - D_-) = 8 and nnz(S_-^T D_- S_- + D_-) = 8, and the S-even and S-odd components (D_- +/- S_-^T D_- S_-)/2 EACH have exact rank 4, so the rank-two cancellation mixes cross-copy and within-copy parts. THE ONLY BASIS-FREE STATEMENTS ARE THAT THE DEFECT IS RANK TWO, ENTIRELY HEAVY AND U-EQUIVARIANT; ITS BLOCK-OFF-DIAGONAL APPEARANCE IN THE DISPLAYED COORDINATES IS A COORDINATE FACT AND NOT A SPECTRAL THEOREM.\nper_scope: THE SECTORED STRUCTURE IS NOT A PROPERTY OF THE PIVOT SECTION AND NOT A PROPERTY OF THE FIXTURE, AND WHAT REMAINS OPEN IS NAMED. TWO DECLARED ALTERNATIVE SECTIONS -- the deep pair core at slices {3, 4}, and a SCATTERED eight-cell section deliberately NOT closed under the displayed U -- reproduce every sector statement exactly: the change of section P has nonzero determinant, the congruence residuals for K and M and the similarity residual for T_2 are ZERO, the induced involution satisfies U_alt^2 = I exactly and for the scattered section is NOT a coordinate permutation, and the light defect rank 0, the heavy defect rank 2, both sector polynomials and all four positivity certificates are UNCHANGED. THE STRUCTURE PERSISTS AT THE SECOND POINT (m, c) = (1/2, 1/3) AT BOTH WIDTHS -- obstruction rank 0, K_c symmetric with eight positive minors, defect rank 2, projector ranks (0, 2, 0, 0), light form symmetric and positive-definite, heavy symmetric part positive-definite -- WHILE THE POLYNOMIALS CHANGE, from (39529825, -109432706) and (22569375, -233631106) to (233, -690) and (739, -7258): THE STRUCTURE IS OF THE CLASS AND THE COEFFICIENTS ARE OF THE POINT. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: no semigroup is constructed and no generator is extracted, so nothing here is a Hamiltonian; the heavy sector's rank-two defect is CHARACTERIZED and NOT REMOVED, and no mechanism explaining WHY it is rank two rather than four is offered; the interior windows are the adversarial check's own scan at two widths and no width-independent proof of the near-seam and far-seam boundary layers is supplied; the descent is measured on TWO widths and TWO rational points and a finite pair of widths is not a continuum; and whether any OTHER admissible domain presentation of the same quotient carries a self-adjoint heavy sector is NOT decided either way.\nRESULT: ON THE SITE-GLUED WIDTH FAMILY AT T = 16 AND T = 20, THE EIGHT-DIMENSIONAL OS QUOTIENT H EXISTS AND IS POSITIVE SEMIDEFINITE OF RANK EIGHT, THE TWO-SLICE SHIFT FAILS TO DESCEND FROM THE SEAM-ANCHORED PREFIX PRESENTATIONS AT INVARIANT OBSTRUCTION RANKS 2, 1, 1 BUT DESCENDS EXACTLY FROM THE INTERIOR WINDOWS AT OBSTRUCTION RANK 0, AND THE DESCENDED OPERATOR -- WHOSE SPECTRUM IS THE LANDED BULK MONODROMY AND WHICH IS THE LANDED W IN THE DEEP PAIR-CORE SECTION -- SPLITS ALONG THE MOMENTUM INVOLUTION INTO A LIGHT SECTOR ON WHICH IT IS A POSITIVE SELF-ADJOINT OPERATOR AND A HEAVY SECTOR ON WHICH ITS SELF-ADJOINTNESS DEFECT IS EXACTLY RANK TWO. The prefix violation counts of the solve are corrected to invariant ranks by an explicit three-presentation construction; the solve's bulk-distributed and width-persistent reading is corrected to a NEAR-SEAM artifact of the prefix presentation; the solve's conclusion that NO descended two-step evolution exists on H is REFUTED and replaced by the sectored statement; the solve's reading that the monodromy spectrum is FRAME content and not OPERATOR content is corrected on the interior window; and the reading that the rank-two defect pairs the two momentum-degenerate copies is REFUTED and fenced. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-194 STAND EXACTLY AS LANDED. BLOCK 190 IS NOT CORRECTED: its refutation of the naive OS transfer pairing was a statement about PAIR CORES, which are positive-definite frames carrying no quotient, and this block's sectored result on the QUOTIENT neither contradicts it nor repairs it. BLOCK 194 IS NOT CORRECTED: its monic-normalization identity is carried forward here as the same formula. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: TWO widths, TWO rational points, ONE profile at unit volume, ONE interior window per width and ONE two-slice shift -- not a scan, not a limit and not a semigroup; the interior windows were found by the adversarial check's scan and are IMPOSED here rather than derived; the boundary-layer mechanism that makes near-seam and far-seam windows fail is NOT proved; the heavy defect's rank two is MEASURED and its mechanism is NOT explained; and the positivity certificates are leading-minor sign tests applied ONLY to matrices whose symmetry residual is measured ZERO in the same gate, because leading minors certify definiteness for a symmetric matrix and for nothing else. SIX ITEMS ARE FOLDED FROM THE TWO ADVERSARIAL CHECK ROUNDS AS CONTENT AND NOT AS ERRATA: round one's C2 PRESENTATION-DEPENDENCE correction, carried as a three-presentation construction; round one's INTERIOR-WINDOW LOOPHOLE, which is the reason this block exists; round one's N2 finding that the image-metric wall is DOWNSTREAM of the null-transport wall and must be collapsed; round one's N-DISCIPLINE PARTIAL-NARROWING to the seam-anchored prefix presentations; round two's P1 BASIS-INDEPENDENCE, gated here as congruence and similarity on two declared alternative sections; and round two's P2 REFUTATION of the degenerate-copy pairing reading, gated here as the S-invariance residuals and the rank-four S-parity components. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE OS RECONSTRUCTION SOLVE (block 195 candidate), OSR PHASE 1 MEASURED, OSR PHASE 2 MEASURED, B195 CHECK VERDICT, OSR PHASE 3+4 MEASURED and B195 ROUND-2 VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **Repairing the heavy sector.** Stopped: the defect is exactly rank two, it
   is `U`-equivariant, and no modification of the section, the metric or the
   window removes it within this block. Removing it by changing the OS metric
   would be new data, not a repair.
2. **Proving the boundary-layer rule.** Stopped: which windows descend is
   measured at two widths; no recurrence argument was found.
3. **A semigroup.** Stopped at the fence: one operator is not a dynamics, and
   `T_2^n` was not computed, examined or claimed.
4. **A third width or a third point.** Stopped: two of each is what the check
   confirmed, and a third would have to be checked, not assumed.
5. **Anything downstream of `theta`.** Stopped at the fence: `theta` is a
   logarithm of an algebraic number, on the light sector as much as on the
   heavy one.

### REOPEN IF

1. A **mechanism** is found for the rank-two heaviness — a symmetry or a
   recurrence forcing `rank(M_2c - M_2c^T) = 2` and forcing it into `U = -1`.
   That is the single highest-value follow-on, because it would turn the
   sectored theorem into a structural one.
2. A **presentation** is found on which the heavy sector is self-adjoint, or a
   proof that none exists. Either resolves fence `3` of `N4g`.
3. The **boundary-layer rule** is derived rather than scanned, at which point
   the interior window stops being an imposed object.
4. A **third width** reproduces the sectored split with the same invariants,
   which would make width-independence a measured family statement rather than
   a two-point coincidence.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 194's #60. NO CORRECTION IS LANDED BY THIS
BLOCK AGAINST ANY LANDED NUMBER.** Every item below corrects **this lane's own
solve language** or folds an adversarial-check finding as content; each is a
declared constant with a gate and, where it guards a correction, a mutation.

61. **THE VIOLATION COUNTS WERE PRESENTATION-DEPENDENT.** The solve reported
    `8/12`, `6/8`, `2/4` at `T = 16` and `14/20`, `12/16`, `8/12` at `T = 20`
    as if they measured the obstruction. They measure one nullspace basis. The
    invariant is the **rank** — `2, 1, 1` at both widths — and the repair is
    carried as a three-presentation construction on the same kernel, adapted
    giving exactly the rank and all-violating giving exactly the nullity. Gate
    `D-2`, mutation `break_basis_dependence`.
62. **"BULK-DISTRIBUTED, WIDTH-PERSISTENT" WAS AN ARTIFACT.** The solve read
    all-slice residual support plus persistence at both widths as evidence of a
    bulk obstruction. Measured here: the support statement is true and
    invariant, but the obstruction is a **near-seam** phenomenon — interior
    windows descend exactly. The two facts are compatible and the inference
    between them was wrong. Gates `D-3`, `D-4`.
63. **THE NO-GO IS NARROWED TO THE SEAM-ANCHORED PREFIX PRESENTATIONS.** The
    solve concluded that **no** descended two-step evolution operator exists on
    `H`. That is false as worded: `T_2 = q_A tau^2 q_D^-1` exists on the whole
    quotient from the interior window, at both widths and both points. The
    honest negative statement is about the prefix presentations `D = {1..dmax}`,
    and the adversarial check's `N1`–`N8` gate recorded exactly that demotion.
    Gate `D-4`, mutation `break_interior_loophole`.
64. **THE TWO WALLS WERE NOT INDEPENDENT.** The solve presented the failure of
    the pushforward and the failure of the Riesz form as a two-lemma argument.
    The check's `N2` showed the second is **downstream** of the first —
    `K_AA S_2 N = 0` implies `S_2^T K_AA S_2 N = 0` — so they must be collapsed
    into one wall. The genuinely independent wall is **OS-self-adjointness**,
    and that is the wall this block resolves per sector.
65. **THE MONODROMY SPECTRUM IS OPERATOR CONTENT, NOT MERELY FRAME CONTENT.**
    The solve's closing line was that the positive two-scale spectrum is a
    property of a frame and not of any operator. On the interior window it is
    the spectrum of a representative-independent operator on `H`, and in the
    deep pair-core section that operator **is** Block 190's `W` entrywise. Gate
    `E-5`.
66. **THE DISPLAYED CHARACTERISTIC POLYNOMIAL IS AGAIN UNNORMALIZED.** The
    phase-3+4 anchor displays `charpoly(T_2)` as the bare product of integer
    quadratics, exactly the defect Block 194's `C1` correction repaired. Carried
    forward here as the same identity, `s = (a_l a_h)^2` at zero residual, and
    not re-committed. Gate `E-4`, mutation `break_monic_normalization`.
67. **LEADING MINORS CERTIFY DEFINITENESS ONLY FOR A SYMMETRIC MATRIX.** The
    phase-3+4 anchor reports "all eight leading minors of the descended form
    positive". Both `K_c` **and** `M_2c` do have eight positive leading minors,
    but `M_2c` is not symmetric, so only the first is a positivity certificate.
    The true positivity statement about the shifted form is about its
    **symmetric part**, and that is what is gated. Gate `E-2`, and every
    positivity gate in this block measures its matrix's symmetry residual in the
    same check.
68. **THE DEFECT DOES NOT PAIR THE TWO DEGENERATE COPIES.** The natural reading
    of a rank-two `U`-equivariant defect on a doubly degenerate heavy sector is
    that it pairs the two spectral copies. Round two refuted it:
    `nnz(S^T D S - D) = 8`, `nnz(S^T D S + D) = 8`, and both `S`-parity
    components have rank four. What survives is rank two, entirely heavy and
    `U`-equivariant. Gate `F-8`, mutations `break_pairing_fence`,
    `claim_defect_pairs_copies`.
69. **"THE RECONSTRUCTION" IS SECTORED, AND THE NEGATIVE HALF LEADS.** The
    lane's phase-3+4 summary reads as a positive result with a caveat. It is a
    **split**: complete on the light sector, obstructed at exact rank two on the
    heavy one. `FULL_RECONSTRUCTION_CLAIMED = False` and
    `HEAVY_READING_LICENSED_CLAIMED = False` are declared constants with gates
    `B-3` and `B-4` and mutations `claim_full_reconstruction`,
    `claim_heavy_reading_licensed`.

### The adversarial check

Verdict carried as **SECTORED INTERIOR RECONSTRUCTION CONFIRMED TWICE, PAIRING
READING REFUTED** — **two** rounds (`sol xhigh`, cross-model, independent
rebuilds from the landed Block 190 note rather than invocations of any runner;
findings preserved at `b195_check_findings.md` and `b195r2_check_findings.md`,
checker at `b195r2_exact_probe.py`, gated runs `47/0`, `52/0`, `27/0`).

**ROUND ONE REFUTED THE SOLVE AND THE REFUTATION IS THIS BLOCK'S SUBJECT.** The
broad descent no-go fell to an explicit interior-window construction
(corrections 61–63); the count claim fell to a basis change (correction 61); the
image-metric wall was shown to be downstream of the null-transport wall
(correction 64). `C1` — the rank-eight Gram — was confirmed exactly.

**ROUND TWO CONFIRMED THE SECTORED PACKAGE AND FENCED ITS ONE OVERREACH.**
`C1`–`C5` confirmed at both widths; `P1` basis-independence confirmed as
congruence under alternative sections, including a section not closed under `U`;
`P3` structural persistence confirmed at `(1/2, 1/3)`; and `P2` **refuted** the
degenerate-copy pairing reading (correction 68).

**BOTH CHECKS' EXACT WITNESSES ARE REPRODUCED DIGIT FOR DIGIT.** The heavy
defect's scale `s`, its integer skew matrix `J`, the wedge vectors and their
norms, the heavy discriminant `52545986939220736` and its factorisation, and the
`(8, 8)` / `(4, 4)` pairing residuals are **declared literals** in this block's
runner rather than printed byproducts.

**AND THE CHECKS ARE EXTENDED IN FOUR PLACES,** all four re-measured
independently here: the positive-semidefiniteness certificate for `K_AA` via the
exact Schur identity and the four projector identities (`C-2`, `C-3`); the
three-presentation basis-dependence construction, which makes the correction a
theorem rather than an observation (`D-2`); the identification of the descended
operator with the landed `W` in the deep pair-core section (`E-5`); and the
positive-definiteness of the **symmetric part** of the shifted form on all of
`H`, which locates the failure precisely in symmetry rather than in positivity
(`E-2`).

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–194 number **stands as landed**.
**Block 190 is not corrected**: its refutation of the naive OS transfer pairing
was a statement about **pair cores** — positive-definite frames carrying no
quotient — and this block's quotient-level result neither contradicts it nor
repairs it. **Block 194 is not corrected**: its monic-normalization identity is
carried forward here as the same formula, and its two landed quadratics at both
points are reproduced exactly as the spectrum of the descended operator. Block
191's cell-average assembly and Block 105's `shear_hodge` are used unchanged.

### Reproduction

```text
python3 scripts/admissibility_dirac_kahler_sectored_interior_os_reconstruction_2026_08_25.py
python3 ... --list-mutations
python3 ... --mutation claim_full_reconstruction
```

Baseline expectation: families `A` through `H` PASS. Thirty-five declared
mutations, each flipping **exactly one** family and exiting nonzero; per-family
census `A 2, B 8, C 3, D 4, E 5, F 8, G 3, H 2`. Every measurement is taken
once, before any mutation flag is read, so no gate can cascade into another.
Four exact carrier inverses — two `64 × 64` and two `80 × 80` — are built once
and shared by every gate.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE OS RECONSTRUCTION SOLVE
(block 195 candidate)**, **OSR PHASE 1 MEASURED**, **OSR PHASE 2 MEASURED**,
**B195 CHECK VERDICT**, **OSR PHASE 3+4 MEASURED** and **B195 ROUND-2 VERDICT**
anchors.
