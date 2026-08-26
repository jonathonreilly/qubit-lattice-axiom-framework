---
title: "Admissibility — Dirac-Kähler Spatial Embedding and the Momentum Positivity Boundary: The X = 4 Spectrum Embeds Verbatim at X = 8 and the Positivity Does Not Follow It"
date: 2026-08-26
block: 198
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_spatial_embedding_momentum_boundary_2026_08_26.py
parent_ref: origin/physics-loop/toe-axiom-closure-block197-hidden-involutive-isometry-20260826
parent_commit: de78bc55790ea4509af0cf9c4de1830e8284ac76
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# The Spatial Embedding Theorem and the Momentum Positivity Boundary — on a second carrier `Z_16 × Z_8` the half-lattice shift splits the deep core into two exact eight-dimensional sectors, the even one reproduces the landed `Z_16 × Z_4` monodromy verbatim and stays real, positive and reciprocal, and the odd one carries one new irreducible palindromic quartic whose four roots are nonreal — so the monodromy positivity does **not** extend to the new momentum sectors, and this lane's own scouting sentence that it does is false

**One sentence.** At `T = 16`, `(m, c) = (9/20, 5/13)`, unit volume and the deep
core `t0 = 3`, the construction is rebuilt at a second spatial extent `X = 8`
and closes there exactly — `nnz(d_K^2) = 0`, `nnz(Ps H Ps - H) = 0`,
`nnz(Ps Q Ps - Q^T) = 0`, an **empty** directed cross block, `rank(Q) = 128`
with two-sided inverse residuals `0`, and a `16 × 16` core Gram with **all
sixteen** leading principal minors positive; the half-lattice shift `U_4` then
splits that core into two eight-dimensional sectors that are block diagonal for
**both** the Gram and the monodromy, the even sector satisfies
`charpoly(W_e) = charpoly(W_4)` exactly against a **rebuilt** `X = 4` carrier
and is **similar to it over `QQ`**, and the odd sector carries one new
irreducible palindromic quartic whose `u`-substitution discriminant is exactly
`-7271743246281426848714247040000` — so all four of its roots are nonreal and
off the unit circle. Positivity is therefore **scoped to the embedded sector**,
the failure on the new sectors is a **measured boundary** of a transfer property
rather than a defect of the build — both sector Grams are positive definite —
and not one line of it supplies gravity.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Six imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE SCOPE OF THE WORD *POSITIVITY* IS FENCED BEFORE THE FIRST NUMBER IS
READ, BECAUSE TWO DIFFERENT POSITIVITIES ARE IN PLAY AND THIS NOTE NEVER LETS
THEM MERGE.**

- **NO GRAVITY IS SUPPLIED.** This block supplies no lapse variable in an ADM
  phase space, no shift vector, no Hamiltonian constraint, no momentum
  constraint, no first-class constraint algebra, no Dirac closure, no Dirac
  observable, no gauge orbit and no diffeomorphism quotient. Nine structures,
  enumerated as a measured constant and gated.
- **POSITIVITY IS SCOPED TO THE EMBEDDED SECTOR.** The monodromy spectrum is
  real, positive and reciprocal on the `U_4`-**even** sector and **nonreal** on
  the `U_4`-**odd** sector. No positivity claim is made for the `X = 8` core as
  a whole. `claim_positivity_unscoped` fails gate `B`.
- **THE NEW-SECTOR NONREALITY IS A MEASURED BOUNDARY AND NOT A DEFECT.** The
  carrier closes at `rank(Q) = 128` with inverse residuals `0`, the cross block
  is empty, and the reflected pairing is **positive definite on exactly the
  sector whose spectrum is nonreal** — `8` of `8` positive minors on each of
  `K_e` and `K_o`. What fails is the *monodromy spectral* positivity and
  nothing else. `claim_new_sector_defect` fails gate `B`.
- **THE LARGER-UNIT-CELL QUESTION IS A NAMED OPEN LEG.** Whether an
  `X = 8`-native larger unit cell restores monodromy positivity on the new
  sectors is neither built, probed nor excluded here.
  `claim_larger_cell_decided` fails gate `B`.
- **NO GENERIC `(m, c)` THEOREM AND NO CONTINUUM.** One width, one rational
  point, one core, one unit volume, two spatial extents. That is not a
  parameter space, not a refinement family and not a limit.
- **THE READINGS ARE READINGS.** Five of them are enumerated below, and
  `READINGS_LICENSED_CLAIMED = False` is a declared constant with a gate.

**AND THE BLOCK REFUTES ITS OWN SCOUTING RECORD, WHICH IS THE REASON THE FENCE
IS WRITTEN THIS WAY.** The campaign's `SCOUT S1 RESULT` anchor recorded a
*strong pass* with the positivity of the new quartic left as *check pending*.
The check came back negative and the negative is the block: the `u`-substitution
discriminant is strictly negative, the quartic has **no** real root, and the
positivity does not extend. That sentence is corrected **as content** — see
correction `82` — and not as an erratum.

**EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER
METAPHYSICAL NECESSITY** — the cycle-913 caution, carried verbatim — and every
positive here is candidacy within this formalism and never a claim about nature.

---

## W1 — the wall, and the charter

### What was open

Every transfer result from Block 190 to Block 197 lives at **one** spatial
extent, `X = 4`. Block 190 fixed the carrier `Z_T × Z_4`, computed the deep-core
monodromy `W = K_c^-1 L_2` and found

```text
charpoly(W)  =  (22569375 z^2 - 233631106 z + 22569375)^2
                (39529825 z^2 - 109432706 z + 39529825)^2   at (9/20, 5/13),
```

Block 194 re-declared that same pair while varying `(m, c)`, Block 193 the
window law, Block 197 the isometric commutant. Not one of them changed `X`.
Three things were open:

1. **Does the construction even close at another extent?** The reflection, the
   raising-set restriction and the cell Hodge are all written against `Z_4`.
2. **If it closes, what happens to the spectrum?** A refinement could scramble
   it, extend it, or leave it alone with additions.
3. **If the spectrum extends, does the positivity extend with it?** Everything
   the lane calls a transfer property depends on the roots being real, positive
   and reciprocal.

### The charter

1. **Rebuild, do not port.** The `X = 4` comparison values are rebuilt here from
   the same formulas rather than read out of a landed runner, so *verbatim* is a
   measurement and not a citation.
2. **Make the embedding a sector statement.** Two polynomials agreeing is a
   coincidence until there is an operator behind it. Ask for a similarity.
3. **Ask the positivity question in both directions.** A boundary is only a
   boundary if the other side is measured too.
4. **Say which positivity.** The reflected pairing and the monodromy spectrum
   are different objects and a failure of one is not a failure of the other.
5. **Certify the sign without a radical.** A discriminant sign carried by a
   `31`-digit integer must not depend on any tolerance anywhere.

---

## N1 — THE CONSTRUCTION AT `X = 8`, and every statement in it is an exact entry count

**NOTHING BELOW IS AN EMBEDDING IF THIS SECTION IS NOT EXACT.**

### The carrier, carried unchanged with the extent promoted to a parameter

Block 190's wrap-edge construction at `T = 16`, written at a general spatial
extent `X`:

- the staggered Dirac–Kähler kernel on `Z_T × Z_X` with `eta_t = 1`,
  `eta_x = (-1)^t` and the temporal sign `w = -1` on the **wrap edge**
  `t = T-1`;
- the grade `deg(t, x) = t mod 2 + x mod 2` and the grade-raising
  `d_K = P1 K P0 + P2 K P1`;
- the site reflection `theta_s(t) = -t` with fixed slices `{0, T/2}`;
- the raising set `A_s` = the `d_K` entries in the **closed** half `{0..T/2}`
  **excluding** fixed-slice spatial edges;
- the glue `D_s = A_s - Ps A_s Ps`;
- the completion `Q = m H + H D_s - D_s^T H`.

`H` is Block 191's quarter-weighted four-corner cell average at Block 190's seam
convention, built from the **one imported object**, the landed Block 105
`shear_hodge(c, v)` read through the Block 128 module at unit volume and at
`c = 5/13`:

```text
B(5/13, 1) = diag( 1, [[169/144, -65/144], [-65/144, 169/144]], 1 ).
```

### What closes, at both extents

| quantity | `X = 4` | `X = 8` |
| --- | ---: | ---: |
| `nnz(d_K^2)` | `0` | `0` |
| `nnz(Ps H Ps - H)` | `0` | `0` |
| `nnz(Ps Q Ps - Q^T)` | `0` | `0` |
| directed cross block of `Q` | `0` | `0` |
| `rank(Q)` | `64` of `64` | `128` of `128` |
| `nnz(Q G - I)`, `nnz(G Q - I)` | `0`, `0` | `0`, `0` |
| `nnz(K_c - K_c^T)` at `t0 = 3` | `0` | `0` |
| leading principal minor signs of `K_c` | `(+)^8` | `(+)^16` |

The **directed cross block** is the count of nonzero entries of `Q` from the
strict past half `{1..7}` to the strict future half `{9..15}`. It is `0`: the
glue never connects the two open halves directly, which is the structural fact
the reflected pairing rests on.

The core Gram's definiteness is the **exact Sylvester criterion over `QQ`** —
sixteen leading principal minors, all with strictly positive determinant, no
eigenvalue computed anywhere. That the `X = 8` core is a `16`-dimensional
positive definite OS core is what makes the later boundary statement a statement
about the *spectrum* and not about the *pairing*.

### The one expensive step, and it happens once

Exactly **one** `128 × 128` exact inverse and **one** `64 × 64` exact inverse
are built in the runner, each once, by exact fraction-free arithmetic over `QQ`
through `DomainMatrix`. Every gate below reads them. No other inverse in the
runner exceeds `16 × 16`, and the whole run is under a minute.

---

## N2 — THE EMBEDDING, and it is a sector statement and a similarity

### The half-lattice split

The core frame at `t0 = 3` is the `2X` cells `b <-> (t_b, x_b)` with
`t_b ∈ {3, 4}`, the reflected pairings

```text
L_k[a, b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)],   G = Q^-1,
K_c = L_0,        W = K_c^-1 L_2.
```

`U_j` is the `j`-site spatial shift of the core cells, acting on **both** time
layers. The half-lattice shift `U_{X/2} = U_4` gives the two real projectors

```text
P_e = (I + U_4)/2,        P_o = (I - U_4)/2.
```

Measured: `rank(P_e) = rank(P_o) = 8`, `nnz(P_e^2 - P_e) = nnz(P_o^2 - P_o) = 0`,
`nnz(P_e + P_o - I_16) = 0`. With `B_e`, `B_o` column-space bases and
`pi = (B^T B)^-1 B^T` the exact coordinate left inverses,

```text
W_e = pi_e W B_e,   W_o = pi_o W B_o,   K_e = B_e^T K_c B_e,   K_o = B_o^T K_c B_o.
```

### It is a genuine direct sum, which is what makes *sector* the right word

```text
nnz(B_e^T K_c B_o)  =  0,
nnz(pi_e W B_o)     =  0,        nnz(pi_o W B_e)  =  0,
charpoly(W) - charpoly(W_e) charpoly(W_o)  =  0.
```

Both the Gram and the monodromy are block diagonal for the split. Nothing below
would be a statement about a *sector* if any of those four were nonzero.

### The embedding itself

Against a `Z_16 × Z_4` carrier **rebuilt here** at the same width, the same
fixture, the same volume and the same core:

```text
charpoly(W_e) - charpoly(W_4)  =  0        as monic polynomials over QQ.
```

That is an identity of degree-`8` polynomials, not an agreement of a few
displayed coefficients. Its primitive factors are the landed pair, digit for
digit:

```text
heavy  =  (22569375, -233631106, 22569375),     multiplicity 2,
light  =  (39529825, -109432706, 39529825),     multiplicity 2,
```

and the rebuilt `X = 4` carrier returns Block 194's own declared
monic-normalization scalar, `22569375^2 · 39529825^2 =
795955611005101889386962890625`.

### And the agreement is a similarity, not a coincidence of coefficients

Equal characteristic polynomials do not imply similarity in general. Here they
do, and it is measured by the **elementary divisor census** — the canonical
similarity invariant, the Frobenius normal form read off without computing it:

```text
dim ker p(M)^k  for  p ∈ {heavy, light},  k = 1, 2, 3:

  W_e :  heavy (4, 4, 4),   light (4, 4, 4)
  W_4 :  heavy (4, 4, 4),   light (4, 4, 4)
```

Both censuses agree and both charpolys agree, so `W_e` and `W_4` have the same
invariant factors and are similar over `QQ`. Independently, the Sylvester space
`{X : X W_4 = W_e X}` has dimension `16` — the expected
`2·2^2 + 2·2^2` for two irreducible quadratics each of multiplicity two — and a
**deterministic** sweep of integer combinations of its basis exhibits a member
of rank `8` intertwining at residual `0`. The trial index is reported, so the
search is reproducible and is not a random draw.

### What the odd sector carries

```text
q(z) =  1035991876210625 z^4 - 10651994137075200 z^3
      + 31207521664211586 z^2 - 10651994137075200 z + 1035991876210625,
```

irreducible over `QQ`, palindromic, of multiplicity `2`. So the whole `X = 8`
deep-core characteristic polynomial is

```text
charpoly(W) = (22569375 z^2 - 233631106 z + 22569375)^2
              (39529825 z^2 - 109432706 z + 39529825)^2
              q(z)^2
              / 854282575605737410298720470187055375971422309970855712890625
```

— the entire `X = 4` spectrum plus **one** new doubly degenerate palindromic
quartic and nothing else.

---

## N3 — THE COMMUTANTS, and the parity law that makes the split a measurement

**All eight** spatial shifts commute with the unit-cell monodromy:

```text
nnz([W, U_j]) = 0    for every j = 0..7,      nnz(U_1^8 - I_16) = 0.
```

In particular the two the scouting design named, `nnz([W, U_2]) =
nnz([W, U_4]) = 0`. But the Gram splits them by parity:

```text
nnz(U_j^T K_c U_j - K_c)  =  (0, 256, 0, 256, 0, 256, 0, 256),   j = 0..7.
```

The **four even** shifts are exact `K_c`-isometries; the **four odd** ones each
carry a `256`-entry defect. The same parity law holds at the landed extent on
its own core — all four `X = 4` shifts commute, with Gram defects `(0, 64, 0,
64)` — which is Block 190's own `S`-versus-`U` asymmetry reproduced at the new
extent's scale.

Two things follow and both matter for reading N2 correctly. First, the shift
group **grades** the monodromy without preserving the pairing, so a momentum
split is never automatic here. Second, the projector `P_e = (I + U_4)/2` is
built from an element that **is** an isometry, which is why `K_c` is block
diagonal for the split at all — a projector built from `U_1` would not have
been.

---

## N4 — THE MOMENTUM BOUNDARY, and it is measured in both directions

Write `q(z) = A z^4 + B z^3 + C z^2 + B z + A` with

```text
A = 1035991876210625,   B = -10651994137075200,   C = 31207521664211586.
```

### Two polynomial identities carry the whole argument

```text
z^4 q(1/z) - q(z)              =  0,
q(z) - z^2 q_u(z + 1/z)        =  0,      q_u(u) = A u^2 + B u + (C - 2A).
```

Both are gated at residual `0`. The first says the root set is closed under
`z -> 1/z` and the root product is exactly `1`. The second reduces every
question about the four roots to one question about a real quadratic:

```text
q_u(u) = 1035991876210625 u^2 - 10651994137075200 u + 29135537911790336.
```

### The discriminant, and a sum-of-squares certificate for its sign

```text
B^2 - 4 A (C - 2A)  =  -7271743246281426848714247040000   <  0.
```

The sign is certified **without evaluating a single radical**, by an exact
identity in `QQ[u]`:

```text
4 A q_u(u) - (2 A u + B)^2  =  7271743246281426848714247040000.
```

So `4 A q_u` is a perfect square plus a strictly positive integer, and since
`A > 0` the quadratic `q_u` is strictly positive on **all** of `RR`. Its vertex
and minimum are exact rationals,

```text
u*        =  213039882741504 / 41439675048425,
q_u(u*)   =  2908697298512570739485698816 / 1657587001937   >  0,
```

and at the two points that matter for the unit circle,
`q_u(2) = 11975517142482436` and `q_u(-2) = 54583493690783236`, both positive.

### Two consequences, counted directly rather than inferred

**No real root.** A real root `z` of `q` forces a real root `u` of `q_u`, and
`q_u` has `0` of them. Counted directly on `q` itself: `0` real roots, leaving
`4` distinct **nonreal** roots.

**No unimodular root, counted twice.** A unimodular root `z` forces a real root
`u` of `q_u` in `[-2, 2]`, and there are `0`. That count is confirmed by a
second route that never mentions `u` at all — the Cayley transform
`z = (1 + i w)/(1 - i w)`, which carries the real `w`-axis onto the unit circle
minus `{-1}`:

```text
(1 - i w)^4 q((1 + i w)/(1 - i w))
    =  54583493690783236 w^4 + 49983140813895672 w^2 + 11975517142482436,
```

a **real** polynomial — its imaginary part vanishes identically — whose real
roots are exactly the unimodular roots of `q` other than `z = -1`. It has `0`,
and `z = ±1` are excluded by its constant and leading coefficients, which are
exactly `q(1) = 11975517142482436` and `q(-1) = 54583493690783236`, both
nonzero. Every coefficient of that transform is positive and its odd
coefficients vanish, so it is visibly definite; the count is gated regardless.

So the four new-sector eigenvalues are nonreal **and** off the unit circle, in a
reciprocal-conjugate quadruple `{z, 1/z, z̄, 1/z̄}`.

### The other direction, gated in the same detail

On the embedded sector the opposite holds:

| | `heavy` | `light` |
| --- | ---: | ---: |
| discriminant | `52545986939220736` | `5725088884359936` |
| sign | `+` | `+` |
| root product `c/a` | `1` | `1` |
| root sum `-b/a` | `233631106/22569375` | `109432706/39529825` |

Positive discriminant, root product exactly `1`, positive root sum: both roots
of each are real, positive and reciprocal. Counted on the product: `4` distinct
real roots, `4` of them positive, `0` negative. **Monodromy positivity holds on
the embedded sector and fails on the new one, and both halves are measured.**

### Which positivity does *not* fail

```text
nnz(K_e - K_e^T) = nnz(K_o - K_o^T) = 0,
minor signs of K_e = (+)^8,      minor signs of K_o = (+)^8.
```

The reflected pairing is positive definite on **both** sectors, including the
one whose spectrum is nonreal. The new momentum sectors are therefore a measured
**boundary** of a transfer property, not a defect of the construction — and
both halves of that sentence are gated.

### And it is neither of Block 194's two failure modes

Block 194 separated its positivity failures into a **real negative reciprocal
pair** below the Hodge edge and a **complex unimodular pair** beyond it. This is
neither. The `u`-quadratic has no real root at all, so the quadruple is nonreal
*and* non-unimodular; and it occurs at `c = 5/13`, well inside the Hodge edge
`|c| = 1`, at a fixture where the `X = 4` spectrum is fully positive. Block 194
is not corrected — its two modes stand as landed — and this is a third one,
reached by changing the *extent* rather than the *shear*.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

- **EMBEDDING** names an exact equality of characteristic polynomials together
  with a `QQ`-similarity between one `8`-dimensional compressed operator and one
  rebuilt `8 × 8` monodromy, at one core of one width at one rational point.
  Nothing is embedded in anything except in that sense.
- **MOMENTUM SECTOR** names the image of an exact rational idempotent built from
  a permutation of sixteen indices. There is no momentum.
- **REFINEMENT** names *the same formulas evaluated at `X = 8` instead of
  `X = 4`*. No limit is taken and no third extent exists in this block.
- **POSITIVITY** names two different statements, never merged: (i) the positive
  definiteness of the reflected pairing `K_c`, which **holds** on the whole
  `16`-dimensional core and on each sector separately; (ii) the reality and
  positivity of the monodromy spectrum, which **holds** on the embedded sector
  and **fails** on the new one.
- **BOUNDARY** names the fact that (ii) holds on one sector and fails on
  another, at exact rational data. It is not a curve, not an edge in `(m, c)`
  and not a phase transition.
- **HEAVY** and **LIGHT** order two roots of two rational quadratics. No mass is
  supplied.

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within this imposed finite matrix construction, at `T = 16`, unit volume,
> `(m, c) = (9/20, 5/13)` and the deep core `t0 = 3`, the `Z_16 × Z_8` carrier
> closes exactly; the half-lattice shift `U_4` splits its `16`-dimensional core
> into two `8`-dimensional sectors block diagonal for both `K_c` and `W`; the
> even sector's compressed monodromy has the same characteristic polynomial as
> the rebuilt `Z_16 × Z_4` monodromy and is similar to it over `QQ`, so the
> landed heavy/light pair appears there verbatim with real positive reciprocal
> roots; and the odd sector's compressed monodromy has characteristic polynomial
> `q(z)^2 / A^2` with `q` irreducible palindromic and `disc q_u < 0`, so its
> four eigenvalues are nonreal and off the unit circle.

### Five further fences, all five self-imposed

1. **Two extents, not a family.** `X ∈ {4, 8}`. Nothing is measured at `X = 16`
   and nothing here constrains it.
2. **Existence, not derivation.** *Why* the old spectrum embeds verbatim is not
   derived. The embedding is exhibited.
3. **One fixture.** `(9/20, 5/13)` at unit volume. The boundary is measured
   there and nowhere else, and Block 194's census shows this construction's
   positivity is `(m, c)`-sensitive.
4. **One core, one width.** `t0 = 3`, `T = 16`. Nothing is claimed at another
   core or another width.
5. **The open leg is open.** No larger-unit-cell construction is built, so the
   question of whether one restores positivity is not answered in either
   direction.

### What IS derived, stated positively so the fence is not mistaken for a retreat

Given the construction, the sector decomposition is a **theorem**: four exact
zero counts make it a direct sum of both structures at once. The embedding is a
**theorem**: a polynomial identity plus two equal elementary divisor censuses
plus an exhibited nonsingular intertwiner. And the failure of positivity on the
new sectors is a **theorem** and not an observation: one sum-of-squares identity
in `QQ[u]` settles the sign of the discriminant with no tolerance and no radical,
and the two root counts follow from it by two independent exact routes.

---

## READINGS — five of them, and each is a reading

- **`R1`.** *That the `X = 4` physics survives spatial refinement.* Measured: at
  one width, one fixture and one core, the compressed monodromy on the
  `U_4`-even sector has charpoly equal to the rebuilt `X = 4` monodromy's and is
  similar to it over `QQ`. Nothing is measured at a third extent and no
  refinement limit is taken. **Reading.**
- **`R2`.** *That the new momentum sectors are unphysical, or that their nonreal
  spectrum is an error.* Measured: their eigenvalues are nonreal and off the
  unit circle, **and** the core Gram restricted to them is positive definite
  with `8` of `8` positive minors. Which of the two facts is the physical one is
  not decided here. **Reading.**
- **`R3`.** *That these numbers are a dispersion relation and that `heavy` and
  `light` are masses.* Measured: roots of exact rational polynomials. On the
  embedded sector the trace `T = z + 1/z` is real and exceeds `2`, so
  `acosh(T/2)` exists; on the new sectors `T` is nonreal and no `acosh` exists.
  No physical energy and no mass is supplied by any line here. **Reading.**
- **`R4`.** *That an `X = 8`-native larger unit cell would restore positivity.*
  Measured: **nothing**. No larger-cell construction is built, probed or
  excluded in this block. It is a named open leg and it is named rather than
  answered. **Reading.**
- **`R5`.** *That the momentum boundary is a property of the construction class
  rather than of this fixture.* Measured: one width, one rational point, one
  core, one unit volume and two spatial extents. **Reading.**

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | family |
| ---: | --- | --- | --- |
| 1 | `origin/main`, axiom and registry blobs, worktree blobs, timeout | five pins fixed | `A` |
| 2 | `PARENT_COMMIT` ancestry, both Block 197 artifacts, stale pin carrying neither, audit inputs | exact; `9` of `9` readable | `A` |
| 3 | imposed / registered / adopted | `6 / 0 / 0` | `B` |
| 4 | gravity structures enumerated as NOT SUPPLIED | `9` | `B` |
| 5 | `POSITIVITY_UNSCOPED_CLAIMED` | `False` | `B` |
| 6 | `NEW_SECTOR_IS_DEFECT_CLAIMED`, `LARGER_CELL_DECIDED_CLAIMED` | both `False` | `B` |
| 7 | `GENERIC_POINT_THEOREM_CLAIMED`, `CONTINUUM_LIMIT_CLAIMED`, `READINGS_LICENSED_CLAIMED` | all `False`; `5` readings | `B` |
| 8 | `nnz(d_K^2)` at both extents | `0` | `C` |
| 9 | imported unit-volume block at `c = 5/13`; `nnz(Ps H Ps - H)` | `diag(1, [[169/144,-65/144],[-65/144,169/144]], 1)`; `0` | `C` |
| 10 | `nnz(Ps Q Ps - Q^T)` at both extents | `0` | `C` |
| 11 | directed cross block `{1..7} → {9..15}` at both extents | `0` | `C` |
| 12 | `rank(Q)`; `nnz(QG-I)`, `nnz(GQ-I)`; count of `128 × 128` inverses built | `64` / `128`; `0`, `0`; `1` | `C` |
| 13 | `nnz(K_c - K_c^T)`; minor signs of `K_c` | `0`; `(+)^8` / `(+)^16` | `C` |
| 14 | `rank(P_e)`, `rank(P_o)`; `nnz(P^2-P)`; `nnz(P_e+P_o-I)` | `(8, 8)`; `(0, 0)`; `0` | `D` |
| 15 | `nnz(B_e^T K_c B_o)`; the two `W` cross blocks; `charpoly(W) - charpoly(W_e)charpoly(W_o)` | `0`; `(0, 0)`; `0` | `D` |
| 16 | `charpoly(W_e) - charpoly(W_4)` against a REBUILT `X = 4` carrier | `0` | `D` |
| 17 | elementary divisor census `dim ker p(M)^k`; `dim{X : X W_4 = W_e X}`; intertwiner rank and residual | `4` for every `(p, k)` on both; `16`; `8`, `0` | `D` |
| 18 | `heavy`, `light` as primitive tuples, at `X = 8` on the even sector AND at `X = 4` | `(22569375, -233631106, 22569375)`, `(39529825, -109432706, 39529825)` | `D` |
| 19 | the new factor; multiplicity; irreducible; palindromic | `(1035991876210625, -10651994137075200, 31207521664211586, -10651994137075200, 1035991876210625)`; `2`; `True`; `True` | `D` |
| 20 | full `X = 8` factor list and content; the rebuilt `X = 4` content | `heavy^2 light^2 q^2` over `1/854282575605737410298720470187055375971422309970855712890625`; `1/795955611005101889386962890625` | `D` |
| 21 | `nnz([W, U_j])`, `j = 0..7`; `nnz(U_1^8 - I)` | `(0,)^8`; `0` | `E` |
| 22 | `nnz([W, U_2])`, `nnz([W, U_4])` | `0`, `0` | `E` |
| 23 | `nnz(U_j^T K_c U_j - K_c)`, `j = 0..7` | `(0, 256, 0, 256, 0, 256, 0, 256)` | `E` |
| 24 | the same parity law at `X = 4`: commutators; Gram defects | `(0,0,0,0)`; `(0, 64, 0, 64)` | `E` |
| 25 | `z^4 q(1/z) - q(z)`; `q(z) - z^2 q_u(z+1/z)`; `q_u` | `0`; `0`; `(1035991876210625, -10651994137075200, 29135537911790336)` | `F` |
| 26 | `disc q_u` and its sign; vertex; minimum; `q_u(±2)` | `-7271743246281426848714247040000`, `-1`; `213039882741504/41439675048425`; `2908697298512570739485698816/1657587001937`; `11975517142482436`, `54583493690783236` | `F` |
| 27 | `4 A q_u(u) - (2 A u + B)^2` | `7271743246281426848714247040000`, residual `0` | `F` |
| 28 | real `u`-roots; real roots of `q`; distinct nonreal; new-sector positivity | `0`; `0`; `4`; `False` | `F` |
| 29 | Cayley transform; imaginary part zero; its real roots; `q(1)`, `q(-1)`; unimodular total | `(54583493690783236, 0, 49983140813895672, 0, 11975517142482436)`; `True`; `0`; `11975517142482436`, `54583493690783236`; `0` | `F` |
| 30 | heavy/light discriminants, signs, root products, root sums; distinct real / positive / negative; embedded positivity | `52545986939220736`, `5725088884359936`; `(+,+)`; `(1,1)`; `(233631106/22569375, 109432706/39529825)`; `4/4/0`; `True` | `F` |
| 31 | `nnz(K_e - K_e^T)`, `nnz(K_o - K_o^T)`; minor signs of `K_e`, `K_o` | `(0, 0)`; `(+)^8`, `(+)^8` | `F` |
| 32 | the note at its final path; `N5` byte-identical; `sp.nsimplify` count | present; verbatim; `0` | `G` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

**Dead end one — reading the factorization as the theorem.** The first pass
factored `charpoly(W)` at `X = 8`, saw the two landed quadratics appear
unchanged, and called that the embedding. It is not: two polynomials sharing
factors says nothing about which subspace carries which, and *the entire `X = 4`
spectrum embeds verbatim* is a claim about an operator. What replaced it: find
the projector that splits the core, check that **both** `K_c` and `W` are block
diagonal for it, and only then compare the compressed operator to a rebuilt
`X = 4` monodromy — as a polynomial identity, and then as a similarity.

**Dead end two — proving similarity by exhibiting an intertwiner.** A first
attempt built one fixed integer combination of the `16`-dimensional Sylvester
basis and found it singular, which proves nothing. The fix was to stop treating
similarity as something an example demonstrates: the elementary divisor census
`dim ker p(M)^k` is a **canonical invariant**, it decides similarity outright,
and the exhibited nonsingular intertwiner is then a witness rather than the
argument. The deterministic sweep that finds one is reported with its trial
index so it is reproducible.

**Dead end three — reading the discriminant sign off its value.** The
discriminant is a `31`-digit negative integer against coefficients above
`10^30`, and a note whose whole content is that sign cannot rest on a
subtraction anyone has to trust. Completing the square turns it into an identity
in `QQ[u]` — `4 A q_u(u) - (2 A u + B)^2` is a **constant**, and that constant is
positive — which is checkable by expansion and depends on no tolerance. This is
also the reason `sp.nsimplify` is counted in the runner's own source and
required to be zero.

**Dead end four — calling the new sector's failure the same failure Block 194
found.** The obvious move was to file it under that block's complex-unimodular
mode. It is not that mode: the Cayley transform is a definite quartic with no
real root, so the roots are off the unit circle, and the fixture sits well
inside the Hodge edge where Block 194's complex mode never occurred. Separating
the modes took one transform and kept a landed classification from being
silently widened.

**Dead end five — saying *positivity fails* without a qualifier.** The sentence
is ambiguous in a construction that has both a reflected pairing and a transfer
spectrum, and the ambiguity would have read as *the OS core broke at `X = 8`*.
It did not: `K_o` is positive definite. Measuring the sector Grams took four
lines and turned a defect report into a boundary.

**What actually worked.** Rebuilding the comparison rather than citing it;
demanding an operator behind a polynomial coincidence; asking a canonical
invariant instead of exhibiting an example; certifying a sign by an identity
instead of a subtraction; and counting the same thing twice by two routes that
share no algebra.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE WORD POSITIVITY IS SCOPED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE CONSTRUCTION AT T = 16 WITH THE SPATIAL EXTENT PROMOTED FROM A FIXTURE TO A PARAMETER (the staggered Dirac-Kahler carrier on Z_T x Z_X with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), THE SECOND SPATIAL EXTENT X = 8 WHICH IS THIS BLOCK's ONE NEW CONSTRUCTION ELEMENT AND IS ONE CARRIER AND NOT A FAMILY (Z_16 x Z_8 at the SINGLE control fixture (m, c) = (9/20, 5/13) at unit volume, built beside the landed Z_16 x Z_4 carrier at the SAME width, the SAME fixture, the SAME volume and the SAME deep core t0 = 3), BLOCK 190's CORE FRAME AT THE DEEP CORE t0 = 3 WIDENED WITH THE EXTENT (the 2X cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, and the UNIT-CELL MONODROMY W = K_c^-1 L_2), THE HALF-LATTICE MOMENTUM SPLIT (the spatial shifts U_j by j sites on both time layers of the core, the two real projectors P_e = (I + U_{X/2})/2 and P_o = (I - U_{X/2})/2 as exact rational idempotents of equal rank X summing to I_{2X}, the column-space bases B_e, B_o and their exact coordinate left inverses pi = (B^T B)^-1 B^T), BLOCK 190's AND BLOCK 194's LANDED HEAVY/LIGHT PAIR AT THE CONTROL IMPOSED AS THE COMPARISON TARGET AND ALSO REBUILT HERE RATHER THAN ONLY CITED (22569375 z^2 - 233631106 z + 22569375 and 39529825 z^2 - 109432706 z + 39529825), and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME and at the ONE rational shear 5/13 -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORDS EMBEDDING AND POSITIVITY AND IS SAID IN THOSE WORDS: 'EMBEDDING' NAMES AN EXACT EQUALITY OF CHARACTERISTIC POLYNOMIALS AND A QQ-SIMILARITY BETWEEN ONE 8-DIMENSIONAL COMPRESSED OPERATOR AND ONE REBUILT 8 x 8 MONODROMY, AT ONE CORE OF ONE WIDTH AT ONE RATIONAL POINT, AND NAMES NOTHING ELSE. 'POSITIVITY' NAMES TWO DIFFERENT STATEMENTS AND THE NOTE NEVER LETS THEM MERGE: THE POSITIVE DEFINITENESS OF THE REFLECTED PAIRING K_c, WHICH HOLDS ON THE WHOLE 16-DIMENSIONAL CORE AND ON EACH SECTOR SEPARATELY AT 8 OF 8 POSITIVE LEADING PRINCIPAL MINORS, AND THE REALITY AND POSITIVITY OF THE MONODROMY SPECTRUM, WHICH HOLDS ON THE EMBEDDED SECTOR AND FAILS ON THE NEW ONE. THE SCOUTING RECORD's SENTENCE THAT THE NEW PALINDROMIC QUARTIC IS POSITIVE IS FALSE AND IS CORRECTED HERE AS CONTENT: THE u-SUBSTITUTION DISCRIMINANT IS EXACTLY -7271743246281426848714247040000, ALL FOUR NEW-SECTOR ROOTS ARE NONREAL, AND NO POSITIVITY CLAIM IS MADE FOR THE X = 8 CORE AS A WHOLE. THE NEW-SECTOR NONREALITY IS A MEASURED BOUNDARY OF A TRANSFER PROPERTY AND NOT A DEFECT OF THE CONSTRUCTION: THE CARRIER CLOSES AT rank(Q) = 128 WITH TWO-SIDED INVERSE RESIDUALS ZERO, THE CROSS BLOCK IS EMPTY, AND THE GRAM IS POSITIVE DEFINITE ON EXACTLY THE SECTOR WHOSE SPECTRUM IS NONREAL. WHETHER AN X = 8-NATIVE LARGER UNIT CELL RESTORES MONODROMY POSITIVITY ON THE NEW SECTORS IS A NAMED OPEN LEG AND IS NEITHER BUILT, PROBED NOR EXCLUDED HERE. NO GENERIC (m, c) THEOREM IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: ONE WIDTH, ONE RATIONAL POINT, ONE CORE, ONE UNIT VOLUME AND TWO SPATIAL EXTENTS ARE NOT A PARAMETER SPACE AND ARE NOT A REFINEMENT LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONSTRUCTION SURVIVES THE SPATIAL REFINEMENT INTACT, AND EVERY STATEMENT IN THIS SECTION IS AN EXACT ENTRY COUNT. At T = 16, (m, c) = (9/20, 5/13), unit volume and the deep core t0 = 3, the carrier is rebuilt at BOTH spatial extents from the same formulas, and at BOTH: nnz(d_K^2) = 0 with grade deg(t, x) = t mod 2 + x mod 2; the imported unit-volume Hodge block diag(1, [[169/144, -65/144], [-65/144, 169/144]], 1) assembles by Block 191's quarter-weighted four-corner cell average to nnz(Ps H Ps - H) = 0; the completion obeys nnz(Ps Q Ps - Q^T) = 0; and the DIRECTED CROSS BLOCK IS EMPTY at 0 entries from the strict past half {1..7} to the strict future half {9..15}. THE CARRIER CLOSES AT BOTH EXTENTS: rank(Q) = 128 of 128 at X = 8 and 64 of 64 at X = 4, with two-sided inverse residuals ZERO in both cases. EXACTLY ONE 128 x 128 EXACT INVERSE AND ONE 64 x 64 EXACT INVERSE ARE BUILT IN THIS RUNNER, EACH ONCE, AND EVERY GATE BELOW READS THEM RATHER THAN RECOMPUTING THEM. AND THE DEEP-CORE GRAM IS SYMMETRIC AND POSITIVE DEFINITE AT BOTH EXTENTS: nnz(K_c - K_c^T) = 0, with ALL SIXTEEN leading principal minors strictly positive on the 16-cell X = 8 core and all eight strictly positive on the 8-cell X = 4 core, by the exact Sylvester criterion over QQ and with no eigenvalue computed anywhere.\nper_mode: THE EMBEDDING, AND IT IS A SECTOR STATEMENT AND A SIMILARITY RATHER THAN A COINCIDENCE OF COEFFICIENTS. The half-lattice shift U_4 gives the real projectors P_e = (I + U_4)/2 and P_o = (I - U_4)/2, exact rational idempotents of ranks 8 and 8 whose sum is I_16 at residual 0. BOTH THE GRAM AND THE MONODROMY ARE BLOCK DIAGONAL FOR THAT SPLIT, WHICH IS WHAT MAKES 'THE EMBEDDED SECTOR' A SECTOR AT ALL: nnz(B_e^T K_c B_o) = 0 and both compressed monodromy cross blocks are 0, and charpoly(W) = charpoly(W_e) charpoly(W_o) at residual 0. ON THE EVEN SECTOR THE COMPRESSED MONODROMY REPRODUCES THE X = 4 MONODROMY EXACTLY: charpoly(W_e) - charpoly(W_4) = 0 as monic polynomials over QQ, where W_4 is the Z_16 x Z_4 monodromy REBUILT HERE at the same width, fixture, volume and core rather than cited from a runner. AND THE AGREEMENT IS A SIMILARITY: the elementary divisor census dim ker p(M)^k is (4, 4, 4) for the heavy factor and (4, 4, 4) for the light one, for BOTH W_e and W_4, so the two have the same Frobenius normal form; the Sylvester space {X : X W_4 = W_e X} has dimension 16; and a deterministic sweep of integer combinations exhibits a member of rank 8 intertwining at residual 0. THE EMBEDDED SPECTRUM IS BLOCK 190's AND BLOCK 194's LANDED PAIR VERBATIM, EACH SQUARED: 22569375 z^2 - 233631106 z + 22569375 and 39529825 z^2 - 109432706 z + 39529825 as primitive integer tuples, at X = 8 on the even sector AND at X = 4 on the rebuilt carrier. THE ODD SECTOR CARRIES EXACTLY ONE NEW FACTOR, OF MULTIPLICITY TWO, IRREDUCIBLE OVER QQ AND PALINDROMIC: 1035991876210625 z^4 - 10651994137075200 z^3 + 31207521664211586 z^2 - 10651994137075200 z + 1035991876210625. SO THE WHOLE X = 8 DEEP-CORE CHARACTERISTIC POLYNOMIAL IS THE ENTIRE X = 4 SPECTRUM PLUS ONE NEW DOUBLY DEGENERATE PALINDROMIC QUARTIC AND NOTHING ELSE, over the exact content 1/854282575605737410298720470187055375971422309970855712890625.\nper_block: THE MOMENTUM POSITIVITY BOUNDARY, AND IT IS THIS BLOCK's CENTRE AND ALSO A REFUTATION OF ITS OWN SCOUTING RECORD. Write the new factor q(z) = A z^4 + B z^3 + C z^2 + B z + A with A = 1035991876210625, B = -10651994137075200 and C = 31207521664211586. TWO POLYNOMIAL IDENTITIES CARRY THE WHOLE ARGUMENT AND BOTH ARE GATED AT RESIDUAL ZERO: z^4 q(1/z) = q(z), so the root set is closed under z -> 1/z and the root product is exactly 1; and q(z) = z^2 q_u(z + 1/z) with q_u(u) = A u^2 + B u + (C - 2A) = 1035991876210625 u^2 - 10651994137075200 u + 29135537911790336. THE DISCRIMINANT OF q_u IS NEGATIVE, EXACTLY: B^2 - 4 A (C - 2A) = -7271743246281426848714247040000. THE SIGN IS CERTIFIED WITHOUT EVALUATING A SINGLE RADICAL, BY AN EXACT SUM OF SQUARES: 4 A q_u(u) - (2 A u + B)^2 = 7271743246281426848714247040000 identically, so 4 A q_u is a perfect square plus a strictly positive integer and q_u is strictly positive on ALL of RR, with vertex u* = 213039882741504/41439675048425, minimum q_u(u*) = 2908697298512570739485698816/1657587001937, q_u(2) = 11975517142482436 and q_u(-2) = 54583493690783236. TWO CONSEQUENCES FOLLOW AND BOTH ARE COUNTED DIRECTLY RATHER THAN INFERRED: a REAL root z of q forces a REAL root u of q_u and q_u has 0 of them, so q has 0 real roots and 4 distinct NONREAL roots; and a UNIMODULAR root z of q forces a real root u of q_u in [-2, 2] and q_u has 0 of those, a count CONFIRMED BY A SECOND ROUTE THAT NEVER MENTIONS u -- the Cayley transform (1 - i w)^4 q((1 + i w)/(1 - i w)) is the REAL polynomial 54583493690783236 w^4 + 49983140813895672 w^2 + 11975517142482436, whose imaginary part vanishes identically and whose real roots are exactly the unimodular roots of q other than z = -1, and it has 0 of them, while z = 1 and z = -1 are excluded by q(1) = 11975517142482436 and q(-1) = 54583493690783236, both nonzero. SO THE FOUR NEW-SECTOR EIGENVALUES ARE NONREAL AND OFF THE UNIT CIRCLE, IN A RECIPROCAL-CONJUGATE QUADRUPLE. ON THE EMBEDDED SECTOR THE OPPOSITE HOLDS AND IS GATED IN THE SAME DETAIL: the heavy and light discriminants are 52545986939220736 and 5725088884359936, both strictly positive; both root products are exactly 1; both root sums 233631106/22569375 and 109432706/39529825 are positive; so all 4 distinct roots are real, positive and reciprocal, with 0 negative. THE SCOUTING RECORD's POSITIVITY SENTENCE IS THEREFORE FALSE AND IS CARRIED HERE AS CORRECTION 82 RATHER THAN AS AN ERRATUM.\nlattice_wide: THE COMMUTANTS, AND THE PARITY LAW THAT MAKES THE SPLIT A MEASUREMENT. ALL EIGHT spatial shifts commute with the unit-cell monodromy exactly: nnz([W, U_j]) = 0 for every j = 0..7, with nnz(U_1^8 - I_16) = 0. IN PARTICULAR THE TWO SHIFTS THE SCOUTING DESIGN NAMED COMMUTE: nnz([W, U_2]) = nnz([W, U_4]) = 0. BUT THE GRAM SPLITS THEM BY PARITY, AND THAT IS WHY THE MOMENTUM SPLIT IS A MEASUREMENT AND NOT A GROUP IDENTITY: nnz(U_j^T K_c U_j - K_c) = (0, 256, 0, 256, 0, 256, 0, 256) for j = 0..7, so the FOUR EVEN shifts are exact K_c-isometries and the FOUR ODD ones each carry a 256-entry Gram defect. THE SAME PARITY LAW HOLDS AT THE LANDED EXTENT ON ITS OWN CORE -- all four X = 4 shifts commute and the Gram defects are 0 for j = 0, 2 and strictly positive for j = 1, 3, which is Block 190's own S-versus-U asymmetry read at the new extent's scale. SO THE SHIFT GROUP GRADES THE MONODROMY WITHOUT PRESERVING THE PAIRING, EXACTLY AS IT DID AT X = 4, AND THE HALF-LATTICE PROJECTORS ARE BUILT FROM AN ISOMETRIC ELEMENT U_4 RATHER THAN FROM A NON-ISOMETRIC ONE. THE FAILURE MODE ON THE NEW SECTORS IS ALSO SEPARATED FROM BOTH OF BLOCK 194's: that block classified its positivity failures as a REAL NEGATIVE reciprocal pair below the Hodge edge and as a COMPLEX UNIMODULAR pair beyond it. This one is NEITHER -- the u-quadratic has no real root at all, so the quadruple is nonreal AND non-unimodular, and it occurs at c = 5/13, well inside the Hodge edge, at a fixture where the X = 4 spectrum is fully positive.\nper_scope: WHICH POSITIVITY FAILS IS SAID EXPLICITLY, BECAUSE TWO DIFFERENT ONES ARE IN PLAY, AND WHAT REMAINS OPEN IS NAMED. THE REFLECTED PAIRING STAYS POSITIVE DEFINITE ON THE NEW SECTOR: the compressed Grams K_e = B_e^T K_c B_e and K_o = B_o^T K_c B_o are exactly symmetric and BOTH carry 8 of 8 strictly positive leading principal minors. What fails on the new sectors is the REALITY AND POSITIVITY OF THE MONODROMY SPECTRUM and nothing else, so the new momentum sectors are a MEASURED BOUNDARY of a transfer property and NOT a defect of the construction -- and both halves of that sentence are gated. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: whether an X = 8-NATIVE LARGER UNIT CELL -- a two-site-wide cell matched to the refined lattice rather than the four-corner cell carried from X = 4 -- restores monodromy positivity on the new sectors is NOT decided, because no such construction is built here; WHY the old spectrum embeds verbatim is NOT derived, and the embedding is exhibited rather than explained; ONE core t0 = 3, ONE width T = 16, ONE rational point (9/20, 5/13) and ONE unit volume are probed, and two spatial extents are not a refinement family; no third extent is measured, so nothing here is a statement about X = 16 or about a limit; and no Osterwalder-Schrader reconstruction, no transfer interpretation and no physical dispersion reading of any root in this note is supplied by any line of this block.\nRESULT: ON A SECOND CARRIER Z_16 x Z_8 AT THE CONTROL FIXTURE AND THE DEEP CORE t0 = 3, THE HALF-LATTICE SHIFT U_4 SPLITS THE 16-DIMENSIONAL CORE INTO TWO 8-DIMENSIONAL SECTORS THAT ARE BLOCK DIAGONAL FOR BOTH THE GRAM AND THE MONODROMY; THE EVEN SECTOR REPRODUCES THE Z_16 x Z_4 MONODROMY EXACTLY -- charpoly(W_e) = charpoly(W_4) AS MONIC POLYNOMIALS OVER QQ, WITH EQUAL ELEMENTARY DIVISOR CENSUSES AND AN EXPLICIT NONSINGULAR RATIONAL INTERTWINER, SO BLOCK 190's AND BLOCK 194's LANDED HEAVY/LIGHT PAIR EMBEDS VERBATIM AND STAYS REAL, POSITIVE AND RECIPROCAL; AND THE ODD SECTOR CARRIES ONE NEW IRREDUCIBLE PALINDROMIC QUARTIC OF MULTIPLICITY TWO WHOSE u-SUBSTITUTION DISCRIMINANT IS EXACTLY -7271743246281426848714247040000, SO ALL FOUR OF ITS ROOTS ARE NONREAL AND OFF THE UNIT CIRCLE AND THE MONODROMY POSITIVITY DOES NOT EXTEND TO THE NEW MOMENTUM SECTORS. THAT IS A MOMENTUM POSITIVITY BOUNDARY, IT IS MEASURED IN BOTH DIRECTIONS, AND IT REFUTES THIS LANE's OWN SCOUTING SENTENCE THAT THE NEW QUARTIC IS POSITIVE. THE REFLECTED PAIRING IS POSITIVE DEFINITE ON BOTH SECTORS, SO THE BOUNDARY IS A PROPERTY OF THE TRANSFER SPECTRUM AND NOT A DEFECT OF THE BUILD. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-197 STAND EXACTLY AS LANDED. BLOCK 190 AND BLOCK 194 ARE NOT CORRECTED: their heavy/light pair at the control is rebuilt here from the same formulas at the same width, fixture, volume and core, reproduced digit for digit, and shown to EMBED in the refined carrier rather than to be revised by it; Block 194's two failure modes stand as landed and this block's new mode is separated from both rather than merged with either. THIS BLOCK's OWN DEFECTS ARE DISCLOSED: ONE width, ONE rational point, ONE core, ONE unit volume and TWO spatial extents -- not a refinement family, not a parameter space and not a limit; the embedding is EXHIBITED and not DERIVED; the larger-unit-cell question is NAMED and not answered; and no third extent is measured, so nothing here constrains X = 16. ONE ITEM IS FOLDED FROM THE ADVERSARIAL CHECK AS THE BLOCK's CENTRE AND NOT AS AN ERRATUM: the REFUTATION of the scouting record's positivity sentence for the new quartic, carried as correction 82 with its exact negative discriminant, its sum-of-squares certificate and its two root counts. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its SCOUT MODE, S1 DESIGN, SCOUT S1 RESULT and BATCH-1 CHECK VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **The larger `X = 8`-native unit cell.** Stopped: it is a **new
   construction**, not a variation. The four-corner cell Hodge is carried from
   `X = 4`; a two-site-wide cell matched to the refined lattice would need its
   own assembly rule, its own seam convention and its own reflection check
   before any spectrum it produced could be compared to anything. That is a
   block, not a leg of this one.
2. **A third extent.** Stopped: `X = 16` is a `256 × 256` exact inverse at
   `T = 16`. It is feasible but it is not this block's question — two extents
   already decide whether the spectrum extends, and a third would only begin a
   family that one point cannot support.
3. **Deriving the embedding.** Stopped: nothing found. No argument from
   `Q = m H + H D_s - D_s^T H` and the grading produces the verbatim
   reappearance of the `X = 4` spectrum, and this note refuses to dress
   exhibition as derivation.
4. **The `(m, c)` dependence of the boundary.** Stopped: Block 194 showed the
   `X = 4` positivity is `(m, c)`-sensitive, so the new sectors' behaviour
   almost certainly is too. Measuring that is a census, and a census at
   `128 × 128` per point is a block of its own.
5. **Any physical reading of the nonreal quadruple.** Stopped: `R2` and `R3`
   name the two readings on offer and neither is licensed here.

### REOPEN IF

1. A larger `X = 8`-native unit cell is built and its odd-sector quartic has a
   **positive** `u`-discriminant — in which case the boundary is an artifact of
   the imported cell rather than of the refinement.
2. A third extent shows the even-sector embedding **failing**, in which case the
   `X = 4 -> X = 8` agreement is a coincidence of two small extents rather than
   a structure.
3. Any `(m, c)` is found where the new sectors are real and positive while the
   embedded ones are too, which would make the boundary a property of the
   fixture rather than of the extent.
4. The `256`-entry odd-shift Gram defect turns out to be removable by a
   different core frame, which would make the parity law a frame artifact and
   the sector split arbitrary.
5. The reflected pairing is found to be **indefinite** on the odd sector at some
   nearby fixture, in which case the failure there really would be an OS failure
   and not only a spectral one.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 197's `#81`. NO CORRECTION IS LANDED BY THIS
BLOCK AGAINST ANY LANDED NUMBER.** Every item below corrects **this lane's own
scouting language** or folds an adversarial-check finding as content; each is a
declared constant with a gate and, where it guards a correction, a mutation.

82. **THE SCOUTING RECORD'S POSITIVITY SENTENCE FOR THE NEW QUARTIC IS FALSE.**
    The `SCOUT S1 RESULT` anchor records a *strong pass — batch-land candidate*
    with *check pending (positivity of the new quartic + the embedding as a
    theorem)*. The check is negative and the negative is this block's centre:
    `q_u` has discriminant exactly `-7271743246281426848714247040000`, so `q`
    has **no** real root and no unimodular one, and monodromy positivity does
    not extend to the new momentum sectors. Carried as content, with the
    sum-of-squares certificate and both root counts. Gates `B-3`, `F-2`, `F-3`,
    `F-4`, mutations `claim_positivity_unscoped`,
    `break_u_discriminant_sign`, `break_sos_certificate`.
83. **"THE ENTIRE `X = 4` SPECTRUM EMBEDS VERBATIM" WAS A COEFFICIENT STATEMENT
    AND IS UPGRADED TO A SECTOR STATEMENT.** The anchor's phrasing is about
    factors of one characteristic polynomial. Measured here: the `U_4`-even
    `8`-dimensional sector's compressed monodromy has charpoly **equal** to the
    rebuilt `X = 4` monodromy's, both cross blocks vanish, and the two operators
    are **similar over `QQ`** by equal elementary divisor censuses with an
    exhibited nonsingular rational intertwiner. Gates `D-2`, `D-3`, `D-4`,
    mutations `break_sector_cross_blocks`, `break_embedded_charpoly`,
    `break_sector_similarity`.
84. **THE NEW-SECTOR FAILURE IS A THIRD MODE, NOT EITHER OF BLOCK 194'S TWO.**
    That block separated a real negative reciprocal pair below the Hodge edge
    from a complex **unimodular** pair beyond it. This one is neither: the
    Cayley transform is a definite quartic with `0` real roots, so the quadruple
    is nonreal **and** non-unimodular, and it occurs at `c = 5/13`, well inside
    the edge. Block 194 is not corrected; a mode is added beside its two, and it
    is reached by changing the **extent** rather than the shear. Gate `F-5`,
    mutation `break_unimodular`.
85. **"POSITIVITY FAILS" WAS AMBIGUOUS AND THE NOTE MUST SAY WHICH.** In a
    construction carrying both a reflected pairing and a transfer spectrum, the
    bare sentence reads as an OS failure. Measured: `K_c` is positive definite
    on the whole `16`-dimensional core and on **each** sector separately, `8` of
    `8` minors on `K_o` included. What fails is the monodromy spectral
    positivity alone, so the new sectors are a **boundary** and not a defect,
    and `NEW_SECTOR_IS_DEFECT_CLAIMED = False` is a declared constant. Gates
    `B-4`, `C-6`, `F-7`, mutations `claim_new_sector_defect`,
    `break_core_gram_definiteness`.
86. **THE LARGER-UNIT-CELL QUESTION IS NAMED AND NOT PROBED, AND SAYING SO IS
    PART OF THE RESULT.** The batch verdict names it as a new open leg. No such
    construction is built here, and `LARGER_CELL_DECIDED_CLAIMED = False` is a
    declared constant so the leg cannot be read as answered in either direction.
    Gate `B-5`, mutation `claim_larger_cell_decided`.
87. **THE COMPARISON VALUES ARE REBUILT, NOT CITED, AND THAT CHANGES WHAT
    *VERBATIM* MEANS.** Reading Block 190's or Block 194's declared literals
    would make the embedding a comparison against a note. The `Z_16 × Z_4`
    carrier is rebuilt here from the same formulas at the same width, fixture,
    volume and core, and it returns both quadratics **and** Block 194's own
    monic-normalization scalar `795955611005101889386962890625`. Gates `D-3`,
    `D-5`, `D-7`, mutations `break_heavy_verbatim`, `break_light_verbatim`.

### The adversarial check

Verdict carried as **SPATIAL EMBEDDING CONFIRMED, NEW-QUARTIC POSITIVITY
REFUTED** (`sol xhigh`, independent rebuild from the landed Block 190 note
rather than an invocation of its runner; findings preserved at
`scout_batch1_findings.md`).

**THE STRUCTURAL PACKAGE AND THE FACTORIZATION WERE CONFIRMED EXACTLY** — the
four zero counts, the sixteen positive minors, the two commutators and the
three-factor factorization all came back digit for digit. **THE POSITIVITY
CLAIM WAS REFUTED** by the exact negative `u`-discriminant, and that refutation
is correction `82`.

**THE CHECK IS EXTENDED IN FOUR PLACES,** all four re-measured independently
here: the embedding is promoted from a factor list to a **sector statement with
a `QQ`-similarity** (`D-2`, `D-3`, `D-4`); the shift census is run over **all
eight** shifts with their Gram defects rather than the two the design named
(`E-1`, `E-3`); the unimodular count is taken a **second time by the Cayley
transform**, which shares no algebra with the `u`-substitution, and the failure
mode is separated from both of Block 194's (`F-5`); and the **sector Grams** are
measured, which is what turns *positivity fails* into *which positivity fails*
(`F-7`).

**THE CHECK'S SCOPE IS NARROWED HERE IN ONE PLACE, DELIBERATELY.** Its `S2`
argument for positivity on a whole cone is not used anywhere in this block; the
positivity statements here are about two specific compressed operators at one
fixture, and nothing is asserted about any cone.

**THE PROVENANCE CAVEAT IS ACKNOWLEDGED AND HANDLED.** The Block 190 and Block
194 artifacts are not present on canonical `origin/main`; they are landed in the
stacked physics-loop history. Gate `A-2` binds the **Block 197** parent
artifacts by blob at `PARENT_COMMIT` and in the worktree, and verifies that the
stale pin — the Block 196 tip — is a real ancestor carrying neither, so *landed*
here means exactly *landed in this branch history* and the note says so rather
than implying more.

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–197 number **stands as landed**.
**Blocks 190 and 194 are not corrected**: their heavy/light pair at the control
is rebuilt here and reproduced digit for digit, and it is shown to **embed** in
the refined carrier rather than to be revised by it. Block 194's two failure
modes stand as landed and this block's third mode is separated from both rather
than merged with either. Block 191's cell-average assembly and Block 105's
`shear_hodge` are used unchanged.

### Reproduction

```text
python3 scripts/admissibility_dirac_kahler_spatial_embedding_momentum_boundary_2026_08_26.py
python3 ... --list-mutations
python3 ... --mutation claim_positivity_unscoped
```

Baseline expectation: families `A` through `G` PASS, `36` checks, exit `0`.
Thirty-five declared mutations, each flipping **exactly one** family and exiting
nonzero; the per-family mutation census is `A 2, B 8, C 6, D 7, E 4, F 6, G 2`
against a check census of `A 2, B 8, C 6, D 7, E 4, F 7, G 2`. Every measurement
is taken once, before any mutation flag is read, so no gate can cascade into
another. **Exactly one `128 × 128` exact inverse and one `64 × 64` exact inverse
are built, each once and shared by every gate**, and no other inverse in this
runner exceeds `16 × 16`; the whole baseline run is under a minute.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **SCOUT MODE**, **S1 DESIGN**,
**SCOUT S1 RESULT** and **BATCH-1 CHECK VERDICT** anchors.
