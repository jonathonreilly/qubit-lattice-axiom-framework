---
title: "Admissibility — Dirac-Kähler Hidden Involutive Isometry: The Operator That Forces Block 190's Extra Isospectrality"
date: 2026-08-26
block: 197
series: toe-axiom-closure
status: bounded theorem note
runner: scripts/admissibility_dirac_kahler_hidden_involutive_isometry_2026_08_26.py
parent_ref: origin/physics-loop/toe-axiom-closure-block196-window-schur-transport-defect-20260826
parent_commit: a3d8d7b0673c57d949d0f1944feaa2fc90877ae1
current_main: 76df4becc8233080bc5a10a4baf55f83e80f8f2d
registered: 0
adopted: 0
axiom_movement: none
---

# The Hidden Involutive Isometry — Block 190's `p = 0` / `p = 2` isospectrality is implemented by an exact involutive `K_c`-isometry in the full commutant of the unit-cell monodromy, that operator is not a signed monomial and so lay outside the 2048-candidate census by construction, and the triangular display of its light part is a basis gauge whose only invariant content is the simultaneous module-and-Gram equivalence of the two sectors

**One sentence.** On Block 190's width family at `T = 16` and `T = 20`, at the
deep core `t0 = 3` and at both rational points, the exact Sylvester space
`{X : X W_0 = W_2 X}` has dimension `2`, the Gram-conformality condition
`X^T K_2 X = lam K_0` leaves **exactly two** projective rays decided by one
primitive quadratic that factors over `QQ`, the `lam = 1` ray carries an
intertwiner `X*` that **simultaneously** identifies `(K_0, K_2)`, and
`Y' = B_2 X* pi_0 + B_0 X*^-1 pi_2 + Ph` satisfies `[W, Y'] = 0`,
`Y'^T K_c Y' = K_c` and `Y'^2 = I_8` **entrywise over `QQ`** — so Block 190's
recorded leftover, that the `p = 0` / `p = 2` equality is *not group-forced*, is
**explained and not contradicted**: the forcing operator exists, it is
**non-monomial**, and the census that missed it was exhaustive over the wrong
class. Nothing here intertwines the step operator, nothing here is basis-free
except the two displayed identities, and not one line of it supplies gravity.

---

## N0 — THE BANNER, and it comes before any numeral

**NOTHING HERE IS REGISTERED AND NOTHING HERE IS ADOPTED.** Six imposed
objects, zero registered, zero adopted, zero axiom movement.

**THE SCOPE OF THE WORD *SYMMETRY* IS FENCED BEFORE THE FIRST NUMBER IS READ.**

- **NO GRAVITY IS SUPPLIED.** This block supplies no lapse variable in an ADM
  phase space, no shift vector, no Hamiltonian constraint, no momentum
  constraint, no first-class constraint algebra, no Dirac closure, no Dirac
  observable, no gauge orbit and no diffeomorphism quotient. Nine structures,
  enumerated as a measured constant and gated.
- **THE SYMMETRY IS MONODROMY-LEVEL AND NOTHING WIDER.** `Y'` commutes with
  **one core's** monodromy `W` and preserves **one core's** Gram `K_c`. It does
  **not** intertwine the step sectors: `nnz(X* V_0 - V_2 X*) = 4` at both
  fixtures and both widths, with exact witnesses. `claim_step_level_symmetry`
  fails gate `B`.
- **THE TRIANGULAR DISPLAY IS A BASIS GAUGE.** `X* = [[r, 0], [s, 1]]` is a
  property of the chosen column-space bases. Under `B_0 -> B_0 A_0`,
  `B_2 -> B_2 A_2` the upper-right zero does **not** survive and `r` is
  multiplied by `det A_0 / det A_2` — both **measured here** on explicit
  rational base changes. `claim_basis_independent_triangle` fails gate `B`.
- **BLOCK 190 IS NOT CORRECTED.** Its census classified the **signed
  monomials**; it is rebuilt here candidate for candidate and confirmed. `Y'`
  **extends** the isometric commutant beyond the monomials and contradicts
  nothing in it. `claim_b190_corrected` fails gate `B`.
- **NO GENERIC `(m, c)` THEOREM AND NO CONTINUUM.** One core, two widths, two
  rational points. That is not a parameter space and it is not a limit.
- **THE READINGS ARE READINGS.** Five of them are enumerated below, and
  `READINGS_LICENSED_CLAIMED = False` is a declared constant with a gate.

**AND ONE NAMED LEFTOVER IS THE POINT OF THE BLOCK.** Block 190 wrote, in its
own `per_scope` fence: *"Its momentum blocks give `p = 0` and `p = 2` the SAME
polynomial and `p = 1, 3` the other one, AND THE `p = 0` / `p = 2` EQUALITY IS
DECLARED NOT GROUP-FORCED: it is an ADDITIONAL exact isospectrality."* This
block does not weaken that sentence. It shows the equality **is** forced — by an
operator that is not in the group Block 190 swept, and whose existence that
sweep could not have decided either way.

**EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER
METAPHYSICAL NECESSITY** — the cycle-913 caution, carried verbatim — and every
positive here is candidacy within this formalism and never a claim about nature.

---

## W1 — the wall, and the charter

### What was open

Block 190 computed `charpoly(W)` at the deep core in closed form and found it to
be a product of two **squared** quadratics,

```text
charpoly(W)  =  (22569375 z^2 - 233631106 z + 22569375)^2
                (39529825 z^2 - 109432706 z + 39529825)^2      at (9/20, 5/13).
```

The `U = S^2` grading explains **half** of that: `U = +1` carries both copies of
the second quadratic and `U = -1` both copies of the first. It does not explain
why the `U = +1` eigenspace splits under `S` into two two-dimensional pieces
with the **same** quadratic. Block 190 then swept all `2048` signed monomials on
the core, found the `W`-commutants to be exactly `{I, S, U, S^3}` with exactly
`{I, U}` of them Gram isometries — and stopped, recording the residue as an
additional exact isospectrality that no monomial forces.

Three things were open:

1. **Is there an intertwiner at all, and how many?** Nobody had solved
   `X W_0 = W_2 X` on this construction.
2. **Is any intertwiner a Gram isometry?** Isospectrality alone gives a
   similarity; it gives nothing about `K_c`.
3. **Does anything extend to the whole core?** A `2 x 2` fact about compressed
   blocks is not a statement about `W`'s commutant.

### The charter

1. **Solve the Sylvester system exactly**, and report the *dimension*, not an
   example.
2. **Decide the isometry condition projectively.** `X` and `cX` are the same
   map; `lam` is not.
3. **Ask the scope question before the extension question.** If `X*` also
   intertwined the step sectors the object would be carrier-level and the story
   would be different.
4. **Extend, or say exactly what obstructs.** And if the first extension fails,
   find out *where* the failure lives before naming it.
5. **Separate what is displayed from what is true.** A triangular matrix in one
   basis is a coordinate, not a theorem.

---

## N1 — THE SECTOR SPLIT, and every statement in it is an exact entry count

**NOTHING BELOW IS A MECHANISM IF THIS SECTION IS NOT EXACT.**

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
module. That import is the only object imported. The rebuilt carrier is bound to
the landed one by Block 190's own witness:

```text
(W - V^2)[0,4]  at T = 20, t0 = 3  =  53601896033238042551256
                                      /229758595220483765728625,
nnz(W - V^2) = 32,        residual 0,
rank(Q) = 64 and 80,      nnz(QG - I) = nnz(GQ - I) = 0.
```

Gate `C-1`, mutation `break_landed_fingerprint`.

### The core frame, and the shift that grades but does not preserve

For the core `t0 = 3` index the eight cells `b ↔ (t_b, x_b)`,
`t_b ∈ {t0, t0+1}`. The reflected pairings and the two operators are

```text
L_k[a, b]  =  G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)],     K_c = L_0,
V          =  K_c^-1 L_1        (the step),
W          =  K_c^-1 L_2        (the unit-cell monodromy).
```

`S` is the **one-site** spatial shift of the eight cells,
`S : (t, x) ↦ (t, x+1 mod 4)`, and `U = S^2`. Measured:

```text
nnz(K_c - K_c^T) = 0,     nnz([W, S]) = 0,     nnz(S^4 - I) = 0,
nnz(S^2 - U) = 0,
nnz(S^T K_c S - K_c) = 64,        nnz(U^T K_c U - K_c) = 0.
```

**That `64` is the whole reason there is a question.** `S` grades the monodromy
without preserving the pairing, so the equality of the two `S`-momentum blocks
is not a corollary of `S` being a symmetry: `S` is not one. Gate `C-2`, mutation
`break_shift_defect`.

### The three sectors, as formulas

The one new construction element of this block is the `S`-momentum refinement of
Block 190's `U`-grading:

```text
P0 = (I + S + S^2 + S^3)/4,    P2 = (I - S + S^2 - S^3)/4,
Ph = (I - S^2)/2,              P0 + P2 + Ph = I_8.
```

Three exact rational idempotents of ranks `2`, `2` and `4`. `B_p` is a
column-space basis of `P_p`, `pi_p = (B_p^T B_p)^-1 B_p^T` its exact coordinate
left inverse, and the compressions are

```text
W_p = pi_p W B_p,     V_p = pi_p V B_p,
K_p = B_p^T K_c B_p,  K_02 = B_0^T K_c B_2.
```

The sector labels are eigenvalue statements and are gated as such:

```text
nnz(S B_0 - B_0) = 0,     nnz(S B_2 + B_2) = 0,     nnz(U B_h + B_h) = 0.
```

So `p = 0` and `p = 2` are the two **real** momentum sectors of `S` and the
heavy sector is the `U`-odd complement. Gate `C-3`, mutation
`break_sector_dims`.

### The isospectrality, as primitive integer tuples

```text
charpoly(W_0)  =  charpoly(W_2)  =  39529825 z^2 - 109432706 z + 39529825
                                                      at (9/20, 5/13),
                                  =       233 z^2 -       690 z +       233
                                                      at (1/2, 1/3),
heavy quadratic  =  22569375 z^2 - 233631106 z + 22569375   and
                          739 z^2 -      7258 z +       739,
gcd(light, heavy) = 1.
```

The light and heavy squarefree primaries are **coprime** — which is what later
makes the sector-by-sector argument legitimate rather than convenient. Gate
`C-4`, mutation `break_isospectrality`.

At the fresh point the two compressed monodromies are small enough to print:

```text
W_0  =  [[31/37, -34/37], [-7310/8621, 18307/8621]],
W_2  =  [[37/31, -34/31], [-7310/7223, 12769/7223]].
```

They are not equal, and they are not obviously conjugate.

---

## N2 — THE SOLUTION SPACE, and what is decided is projective

### The Sylvester space, exactly

`X W_0 - W_2 X = 0` is four linear equations in the four entries of `X` over
`QQ`. Its coefficient matrix has nullity

```text
dim {X : X W_0 = W_2 X}  =  2      at every width and both points.
```

Gate `D-1`, mutation `break_sylvester_dim`. At the control point the measured
basis is

```text
X_0 = [[5634/6845, 358930811/388416787], [1, 0]],   det = -358930811/388416787,
X_1 = [[1135/1369, -164444072/388416787], [0, 1]],  det = 1135/1369,
```

and the first of those is the element the phase-1 solve displayed, with the
`det = -358930811/388416787` that anchor recorded. **This basis is a
coordinate**, fixed here as the exact rational nullspace the solver returns and
therefore reproducible, but determined only up to `GL_2(QQ)`. What follows is
stated in it and two of the quantities inherit that: the primitive quadratic's
coefficients and the ray coordinate `alpha : beta` are basis-tied. The **branch
count**, the two `lam` values and the normalized representatives `X*`, `X#` are
not — they are properties of the intertwiner plane and the normalization
`X[1,1] = 1`.

### The isometry condition, decided by one quadratic

Write `X = a X_0 + b X_1` and `D = X^T K_2 X`. Conformality of `D` to `K_0` is
the vanishing of the two `2 x 2` minors

```text
D[0,0] K_0[0,1] - D[0,1] K_0[0,0],       D[0,0] K_0[1,1] - D[1,1] K_0[0,0],
```

and — this is the fact that makes the count exhaustive rather than lucky —
**both minors equal one and the same primitive quadratic** in the affine
coordinate `t = a/b`:

```text
control:  64358813 t^2 + 329444835 t - 164444072
             =  (227 t - 104)(283519 t + 1581193),
fresh:         1891 t^2 +      6491 t -       2796
             =  ( 31 t -  12)(    61 t +     233),
```

with both quotients **units**, and the chart at infinity carries **no** branch.
So there are exactly `2` nonzero projective rays and the enumeration is complete
inside the plane. Gate `D-2`, mutation `break_branch_count`.

### The two rays, with their exact data

```text
unit ray:    alpha = (104/227) beta,   lam = 1,
             X* = [[1369/1135, 0], [104/227, 1]]        (control),
             alpha = (12/31) beta,     lam = 1,
             X* = [[37/31, 0], [12/31, 1]]              (fresh);

other ray:   alpha = -(1581193/283519) beta,
             lam = 2323487131056 beta^2 / 80383023361,
             X# = [[-5331973/1417595, -1581193/283519],
                   [-1581193/283519, 1]]                (control),
             alpha = -(233/61) beta,   lam = 53816 beta^2 / 3721,
             X# = [[-163/61, -233/61], [-233/61, 1]]    (fresh).
```

Both representatives have nonzero lower-right entry, so normalizing that entry
to `1` loses no branch. Gate `D-3` binds the ray coordinates and the two `lam`
values; gate `D-4` binds `X*` entry by entry. The `X#` entries are **displayed**
rather than separately gated, because `X# = alpha X_0 + X_1` normalized is
determined by the ray coordinate that `D-3` does bind. Mutations
`break_lambda_branch`, `break_triangular_entries`.

### `lam` is not projective data; its square class is

Rescaling `X ↦ beta X` multiplies `lam` by `beta^2` — measured symbolically, not
asserted. So *"two nontrivial solution families"* names **two rays**, and the
basis-free arithmetic that separates them is the **square class** of `lam`:

```text
control:  lam#  =  2^4 * 3^3 * 7 * 13 * 31 * 37 * 227^2  /  283519^2,
fresh:    lam#  =  2^3 * 7 * 31^2                        /      61^2,
```

both numerators **nonsquare** in `QQ`. The unit ray has trivial square class and
is the rationally normalizable one; the other ray is **not** rationally
normalizable to `lam = 1`. Gate `D-5`, mutation `break_square_class`.

### And `r` is a Gram-volume ratio, not an absolute scalar

Take determinants of `X*^T K_2 X* = K_0`:

```text
r^2  =  det K_0 / det K_2  =  1874161/1288225 = 1369^2/1135^2   (control),
                           =       1369/961   =   37^2/  31^2   (fresh),
```

with the displayed shear obeying, in this gauge,

```text
s  =  (K_0[0,1] - r K_2[0,1]) / K_2[1,1],       K_0[1,1] = K_2[1,1] exactly.
```

At the fresh point that last equality is visible:
`K_0[1,1] = K_2[1,1] = 2947295521/301772314200`.

**And the gauge is probed, not asserted.** With `A_0 = [[1,1],[0,1]]`,
`A_2 = [[1,0],[1,1]]` the transformed intertwiner is

```text
A_2^-1 X* A_0  =  [[1369/1135, 1369/1135], [-849/1135, 286/1135]]  (control),
                  [[  37/31,     37/31  ], [  -25/31,    6/31  ]]  (fresh),
```

— the upper-right **zero is gone** — while both invariant identities survive at
residual `0`. With `A_0 = diag(2, 1)`, `A_2 = I` the number `r` itself moves
from `1369/1135` to `2738/1135`, and `r^2 = det K_0 / det K_2` still holds in
the new gauge because both sides scale by `4`. Gate `D-6`, mutation
`break_determinant_law`.

---

## N3 — THE SCOPE, and the census that could not have seen it

### `X*` does not intertwine the step sectors

```text
nnz(X* V_0 - V_2 X*)  =  4        at every width and both points,
first witness (0,0)   =  -142376/257645     (control),
                      =     -444/961        (fresh).
```

Gate `E-1`, mutation `break_step_scope`. The mechanism is a statement about the
pair `(W, K_c)` and about nothing else — which is exactly why it is invisible
one level down, and exactly why the monomial sweep was looking in the wrong
place.

### Block 190's census, rebuilt candidate for candidate

The candidate set is **Block 190's own**, taken from its landed definition
rather than reinvented: an optional swap of the two time layers, times every
spatial dihedral action (`4` rotations × `2` reflections), times every relative
sign pattern **up to an overall sign** — `2 · 8 · 2^7 = 2048` matrices. Rebuilt
here rather than cited:

```text
candidates                                    2048,
commute with W                                   4   =  {I, S, U, S^3},
unnamed survivors                                0,
of those, Gram isometries                        2   =  {I, U},
per-power Gram defect (S^0, S^1, S^2, S^3)  (0, 64, 0, 64).
```

Every number is Block 190's, including the overall-sign quotient that makes the
commutant count `4` and not `8`. Gate `E-2`, mutations
`break_monomial_census`, `break_isometric_monomials`.

**And its refuted candidate stays refuted, with both landed witnesses
reproduced.** The unsigned spatial reflection `R : (t, x) ↦ (t, -x)` gives

```text
nnz([W, R])  =  16,     [W, R][0,5]  =  16334218/7905965   (control),
                                     =        2414/1165    (fresh),
```

and the first nonzero of `S^T K_c S - K_c` at `T = 20` and the control fixture
is Block 190's own declared literal,

```text
2196923328476037505923247454222973532938493206039747366330235451412004291015625
/2814140416367857864535548440193722522538862625515710221151046656087532099673561724.
```

Gate `E-5`, mutation `break_reflection_refutation`.

### And `Y'` is not in it

```text
row weights of Y'          (4, 4, 4, 4, 5, 5, 5, 5),
is_monomial(Y')            False,
Y' equals a censused monomial   False,
is_monomial(U Y')          False.
```

Gates `E-3`, `E-4`, mutation `break_nonmonomial`. **That is the whole of the
explanation for why the sweep missed it.** The isometric monomial commutant is
`{I, U}`; the isometric commutant proper contains at least `{I, U, Y', UY'}`,
and two of those four have four and five nonzeros per row. No signed monomial of
the core equals either, and no enlargement of the sign set would have reached
them.

---

## N4 — THE COMPLETION, and the naive one is not it

### The naive two-block extension, and its exact defect

```text
Y  =  B_2 X* pi_0  +  B_0 (K_0^-1 X*^T K_2 / lam) pi_2,
nnz([W, Y])  =  0,      rank(Y)  =  4,      nnz(Y^T K_c Y - K_c)  =  64,
first witness (0,0), T = 16:
  control  -48976132744478519489329652146311862124282444534250707666015625
           /33997719455893540048957560867825104440683420084306798815764692622,
  fresh    -15161098351719976229483059/10899840437709830045206044732.
```

`[W, Y] = 0` is real and is this lane's own phase-3 result: `Y` is a
non-monomial element of `W`'s commutant. But `Y` is **not** a Gram isometry, and
the phase-3 solve attributed that to a per-sector `lam` mismatch and named the
full-core completion an open refinement. Gate `F-4`, mutation
`break_naive_extension`.

### Where the defect actually lives

```text
light exchange  [[0, X*^-1], [X*, 0]]:   nnz( . ^T K_light . - K_light) = 0,
heavy identity  I_4:  nnz([W_h, I_4]) = 0,   nnz(I_4^T K_h I_4 - K_h) = 0.
```

The light exchange is **already an exact isometry**. The entire `64`-entry
defect is the **zeroed heavy sector** — `Y` has rank `4` because it kills four
dimensions, and a map that kills a subspace cannot preserve a nondegenerate
form on it. Gate `F-5`, mutation `break_defect_diagnosis`.

### The completion, entrywise

```text
Y'  =  B_2 X* pi_0  +  B_0 X*^-1 pi_2  +  Ph,
```

and at both fixtures and both widths, over `QQ` and entrywise,

```text
nnz([W, Y'])  =  0,    nnz(Y'^T K_c Y' - K_c)  =  0,
nnz(Y'^2 - I_8)  =  0,    rank(Y')  =  8.
```

In the core cell order the exact control completion is `1/1553815` times

```text
[[ 1567504,   146484,    13689,   146484,       0,       0,       0,       0],
 [ -146484,   -13689,  -146484, -1567504,       0,       0,       0,       0],
 [   13689,   146484,  1567504,   146484,       0,       0,       0,       0],
 [ -146484, -1567504,  -146484,   -13689,       0,       0,       0,       0],
 [   30420,   325520,    30420,   325520, 1553815,       0,       0,       0],
 [ -325520,   -30420,  -325520,   -30420,       0,       0,       0,-1553815],
 [   30420,   325520,    30420,   325520,       0,       0, 1553815,       0],
 [ -325520,   -30420,  -325520,   -30420,       0,-1553815,       0,       0]]
```

and the exact fresh completion is `1/1147` times

```text
[[ 1156,  102,    9,  102,    0,    0,    0,    0],
 [ -102,   -9, -102,-1156,    0,    0,    0,    0],
 [    9,  102, 1156,  102,    0,    0,    0,    0],
 [ -102,-1156, -102,   -9,    0,    0,    0,    0],
 [   18,  204,   18,  204, 1147,    0,    0,    0],
 [ -204,  -18, -204,  -18,    0,    0,    0,-1147],
 [   18,  204,   18,  204,    0,    0, 1147,    0],
 [ -204,  -18, -204,  -18,    0,-1147,    0,    0]].
```

Gates `F-1`, `F-2`, mutations `break_completion_matrix`,
`break_completion_identities`.

### The four certificates that license the sector argument

```text
nnz(K_02)                                   =  0,
light-heavy block of K_c in (B_0,B_2,B_h)   =  0,
light-heavy block of W  in (B_0,B_2,B_h)    =  0,       rank(frame) = 8,
gcd(light squarefree, heavy squarefree)     =  1,
nnz(K_0^-1 X*^T K_2 - X*^-1)                =  0.
```

The cross Gram vanishes, the frame is block-diagonal for **both** `K_c` and `W`,
and the primaries are coprime — so every element of `W`'s commutant has zero
light-heavy blocks and no heavy choice can repair or spoil a light obstruction.
The last line is why the `lam = 1` reverse map is literally `X*^-1`. Gate `F-6`,
mutation `break_sector_certificates`.

### And the sign is forced

The searched family was the pure light swap `[[0, C], [alpha X*, 0]]` with `C`
any reverse intertwiner and any exact heavy block commuting with `W_h`. Exact
Gram congruence gives

```text
defect[0,0]  =  K_0[0,0] (alpha - 1)(alpha + 1),      roots  alpha = ±1,
```

so `alpha^2 = 1` is **forced**; `alpha = +1` with `C = X*^-1` and the heavy
identity is the branch taken. Gate `F-7`, mutation `break_alpha_forcing`.

### The Klein four-group

With `U = S^2`:

```text
nnz(U Y' - Y' U)  =  0,
{I, U, Y', UY'}:  four distinct elements, each involutive, each a K_c-isometry,
                  each commuting with W.
```

So the **isometric** commutant of `W` contains a Klein four-group, two of whose
elements are non-monomial. Gate `F-3`, mutation `break_klein_group`. Whether the
isometric commutant *equals* that group is **not** decided here, and reading
`R4` says so.

---

## N4c — THE SECOND WIDTH AND THE SECOND POINT, and what moves with them

At `T = 20`, same core, the Sylvester dimension, **both** projective branches
with both `lam` values, the triangular entries and the completion `Y'` with all
three identities are **identical** to `T = 16` at both points. Gate `G-1`,
mutation `break_width_persistence`.

**That agreement is not an identity, because the data it is computed from
moves:**

```text
nnz(W(20) - W(16))    = 0,    nnz(V(20) - V(16))    = 0,
nnz(W_p(20) - W_p(16)) = 0,   nnz(V_p(20) - V_p(16)) = 0,
nnz(K_0(20) - K_0(16)) = 4,   nnz(K_2(20) - K_2(16)) = 4,
nnz(K_c(20) - K_c(16)) = 64.
```

Every entry of both compressed Grams changes, and the branches are re-derived
against the changed Grams and come back the same rays. Gate `G-2`, mutation
`break_gram_motion`. Without this measurement the `T = 20` line would be a
tautology dressed as a persistence, and the note says so.

At `(m, c) = (1/2, 1/3)`, whose unit-volume Hodge block — read from the
**import** and gated against a declared literal, not from a rerun — is

```text
B(1/3, 1)  =  [[1,0,0,0],[0,9/8,-3/8,0],[0,-3/8,9/8,0],[0,0,0,1]],
```

every structural statement above holds, on a carrier that is measurably
different:

```text
nnz( Q(9/20, 5/13) - Q(1/2, 1/3) )  =  512   of 512 nonzero entries at T = 16.
```

Gate `G-3`, mutation `break_second_point`. This is persistence at one additional
exact point and at one additional width. It is **not** a generic `(m, c)`
theorem and it is **not** a width family theorem.

---

## N4g — THE INTERPRETATIONS FENCE (required section)

### The words, and what each of them actually names here

- **SYMMETRY** names an exact rational `8 x 8` matrix that commutes with one
  core's monodromy and preserves one core's Gram. Nothing is invariant under it
  except those two matrices.
- **ISOSPECTRALITY** names the equality of two `2 x 2` characteristic
  polynomials over `QQ`. No spectrum of anything physical is involved.
- **MOMENTUM SECTOR** names the image of an exact rational idempotent built from
  a permutation of eight indices. There is no momentum.
- **HIDDEN** names *not in the class Block 190 swept*, and nothing more
  romantic.
- **INVOLUTIVE ISOMETRY** names `Y'^2 - I_8 = 0` and `Y'^T K_c Y' - K_c = 0` as
  exact zero matrices over `QQ`.
- **`r`** names `det X*` in a chosen pair of column-space bases. It is
  coordinate-covariant, not an absolute scalar.

### The narrowest true statement, written out so it cannot be paraphrased upward

> Within this imposed finite matrix construction, at the core `t0 = 3` of
> `T = 16` and `T = 20` and at each of two rational points, the space of
> intertwiners between the two `S`-momentum compressions of the unit-cell
> monodromy is two-dimensional, exactly two of its projective rays carry a
> Gram-conformal intertwiner, one of those normalizes to `lam = 1`, and that
> intertwiner extends by the identity on the `U`-odd sector to an exact
> involutive `K_c`-isometry commuting with the whole monodromy — an operator
> that is not a signed monomial and that does not intertwine the step operator.

### Five further fences, all five self-imposed

1. **Existence, not derivation.** *Why* this carrier admits such an isometry is
   not derived. The operator is exhibited; no argument from `Q = m H + H D_s -
   D_s^T H` and the grading produces it.
2. **Containment, not equality.** The isometric commutant is shown to **contain**
   `{I, U, Y', UY'}`. No sweep of the non-monomial isometric commutant is
   performed, so it is not shown to equal it.
3. **One core.** `t0 = 3`. Nothing is claimed at `t0 = 1, 2, 4, 5` or at any
   core of `T = 20` other than `3`.
4. **Two widths, two points.** Not a width family theorem, not a parameter-space
   theorem, not a limit.
5. **The display is a gauge.** Every number in `[[r, 0], [s, 1]]` is a
   coordinate. The two identities `X* W_0 = W_2 X*` and `X*^T K_2 X* = K_0` are
   the content, and `r^2 = det K_0 / det K_2` is the only relation between the
   display and anything basis-free.

### What IS derived, stated positively so the fence is not mistaken for a retreat

Given the construction, the count of isometric intertwiners is a **theorem**:
one primitive quadratic, factored over `QQ`, with the chart at infinity checked
— exactly two rays, and the enumeration is closed. The completion is a
**theorem**: three exact zero matrices at four `(width, point)` instances. And
the reason Block 190's sweep could not have found it is a **theorem** and not a
narrative: `Y'` has rows of weight four and five, and every censused candidate
has rows of weight one.

---

## READINGS — five of them, and each is a reading

- **`R1`.** *That the `p = 0` / `p = 2` isospectrality is now explained.*
  Measured: it is **implemented** by an exact involutive Gram isometry in `W`'s
  commutant, at one core of two widths and two points. **Why** the carrier
  admits such an isometry is not derived. **Reading.**
- **`R2`.** *That `Y'` is a symmetry of a theory.* Measured: an exact rational
  `8 x 8` matrix commuting with one core's monodromy and preserving one core's
  Gram. It does not intertwine the step operators and no reconstruction is
  performed from it. **Reading.**
- **`R3`.** *That `r` is an invariant of the sector pair.* Measured: in the
  displayed gauge `r = det X* > 0` and `r^2 = det K_0 / det K_2`; under
  independent base changes `r` is multiplied by `det A_0 / det A_2`. It is
  coordinate-covariant, not absolute. **Reading.**
- **`R4`.** *That the isometric commutant **is** `{I, U, Y', UY'}`.* Measured:
  those four are exact, involutive, mutually distinct Gram isometries commuting
  with `W`. Whether the isometric commutant is exactly that group is not decided.
  **Reading.**
- **`R5`.** *That the mechanism is a property of the width family rather than of
  this core and this fixture.* Measured: one core, two widths, two rational
  points. **Reading.**

---

## CLAIM REGISTER — formulas, and the family that gates each

| # | claim | value | family |
| ---: | --- | --- | --- |
| 1 | `origin/main`, axiom and registry blobs, worktree blobs, timeout | five pins fixed | `A` |
| 2 | `PARENT_COMMIT` ancestry, both Block 196 artifacts, stale pin carrying neither | exact | `A` |
| 3 | imposed / registered / adopted | `6 / 0 / 0` | `B` |
| 4 | gravity structures enumerated as NOT SUPPLIED | `9` | `B` |
| 5 | `STEP_LEVEL_SYMMETRY_CLAIMED`, `BASIS_INDEPENDENT_TRIANGLE_CLAIMED` | both `False` | `B` |
| 6 | `BLOCK190_CORRECTED_CLAIMED` | `False` | `B` |
| 7 | `GENERIC_POINT_THEOREM_CLAIMED`, `CONTINUUM_LIMIT_CLAIMED`, `READINGS_LICENSED_CLAIMED` | all `False`; `5` readings | `B` |
| 8 | `rank(Q)`; `nnz(QG-I)`, `nnz(GQ-I)`; b190 `(W-V^2)[0,4]`, `nnz(W-V^2)` | `64/80`; `0`, `0`; landed literal, `32` | `C` |
| 9 | `nnz(K_c-K_c^T)`; `nnz([W,S])`; `nnz(S^4-I)`; `nnz(S^2-U)` | `0`; `0`; `0`; `0` | `C` |
| 10 | `nnz(S^T K_c S-K_c)`; `nnz(U^T K_c U-K_c)` | `64`; `0` | `C` |
| 11 | `rank(P0, P2, Ph)`; `S B_0 = +B_0`, `S B_2 = -B_2`, `U B_h = -B_h` | `(2, 2, 4)`; residuals `(0,0,0)` | `C` |
| 12 | `charpoly(W_0) = charpoly(W_2)`; the heavy quadratic | `(39529825, -109432706, 39529825)` / `(233, -690, 233)`; `(22569375, -233631106, 22569375)` / `(739, -7258, 739)` | `C` |
| 13 | `dim{X : X W_0 = W_2 X}` | `2` | `D` |
| 14 | the shared conformality quadratic; its factors; quotients; branch at infinity | `(64358813, 329444835, -164444072)` / `(1891, 6491, -2796)`; `(227t-104)(283519t+1581193)` / `(31t-12)(61t+233)`; units; none | `D` |
| 15 | branch count; the two rays `alpha : beta`; the two `lam` | `2`; `104/227`, `-1581193/283519` / `12/31`, `-233/61`; `1`, `2323487131056/80383023361` / `1`, `53816/3721` | `D` |
| 16 | `lam(beta X) = beta^2 lam(X)` | exact | `D` |
| 17 | `X*` entries `(r, X*[0,1], s, X*[1,1])` | `(1369/1135, 0, 104/227, 1)` / `(37/31, 0, 12/31, 1)` | `D` |
| 18 | square class of `lam#` | `2^4·3^3·7·13·31·37·227^2 / 283519^2`, `2^3·7·31^2 / 61^2`; both nonsquare | `D` |
| 19 | `r^2 = det K_0/det K_2`; the shear gauge formula; `K_0[1,1] = K_2[1,1]` | `1874161/1288225` / `1369/961`; exact; exact | `D` |
| 20 | gauge probe: triangle survives; invariants survive; `r` moves | `False`; `True`; `True` | `D` |
| 21 | `nnz(X* V_0 - V_2 X*)`; first witnesses | `4`; `-142376/257645` / `-444/961` | `E` |
| 22 | monomial candidates (Block 190's own set); commuting; unnamed survivors; isometric | `2048`; `4` = `{I,S,U,S^3}`; `0`; `2` = `{I,U}` | `E` |
| 23 | per-power Gram defects `(S^0, S^1, S^2, S^3)` | `(0, 64, 0, 64)` | `E` |
| 24 | `Y'` row weights; `is_monomial(Y')`; `Y'` in census; `is_monomial(UY')` | `(4,4,4,4,5,5,5,5)`; `False`; `False`; `False` | `E` |
| 25 | `nnz([W, R])`; `[W,R][0,5]`; first nonzero of `S^T K_c S - K_c` at `T = 20`, control | `16`; `16334218/7905965` / `2414/1165`; Block 190's landed literal | `E` |
| 26 | `Y' = B_2 X* pi_0 + B_0 X*^-1 pi_2 + Ph` entrywise | `1/1553815 ·` and `1/1147 ·` the declared integer matrices | `F` |
| 27 | `nnz([W,Y'])`, `nnz(Y'^T K_c Y' - K_c)`, `nnz(Y'^2-I_8)`; `rank(Y')` | `(0, 0, 0)`; `8` | `F` |
| 28 | `{I, U, Y', UY'}`: size, `nnz(UY'-Y'U)`, involutive, isometric, commuting, distinct | `4`; `0`; all `True` | `F` |
| 29 | naive `Y`: `nnz([W,Y])`, `rank`, `nnz(Y^T K_c Y - K_c)`, witnesses | `0`; `4`; `64`; declared literals at `T=16` | `F` |
| 30 | light-exchange Gram defect; heavy identity commutator and Gram defect | `0`; `(0, 0)` | `F` |
| 31 | `nnz(K_02)`; light-heavy blocks of `K_c` and `W`; `rank(frame)`; primary gcd; `nnz(K_0^-1 X*^T K_2 - X*^-1)` | `0`; `0`, `0`; `8`; `(1)`; `0` | `F` |
| 32 | roots of the `alpha` Gram defect | `-1`, `+1` | `F` |
| 33 | `T = 20`: Sylvester dim, branches, `X*` entries, `Y'`, its three residuals | identical to `T = 16` | `G` |
| 34 | `nnz` motion `T=20 - T=16` for `W`, `V`, `W_p`, `V_p`; `K_0`, `K_2`; `K_c` | `0`; `4`, `4`; `64` | `G` |
| 35 | the imported unit-volume block at `c = 1/3`; `nnz(Q - Q')`; the second point's structural counts | `B(1/3,1)`; `512`; identical | `G` |
| 36 | the note at its final path; `N5` byte-identical; `sp.nsimplify` count | present; verbatim; `0` | `H` |

---

## N4h — THE DERIVATION PATH, WITH ITS DEAD ENDS

**Dead end one — looking for the mechanism among monomials.** Block 190 swept
`2048` candidates and its sweep was correct and exhaustive. The lesson is that
exhaustiveness over a class says nothing outside it: the operator that forces
the equality has rows of weight four and five, and no amount of enlarging the
sign set would have reached it. What replaced the search: solve the intertwining
equation itself and let the solution space report its own dimension.

**Dead end two — treating the intertwiner as a matrix rather than a ray.** The
phase-2 solve reported *two nontrivial solution families* and gave `lam` values.
But `lam` is not an invariant of a family: rescaling `X` multiplies it by a
square. The honest statement needed the square class, and once that was computed
the two rays turned out to be genuinely inequivalent — one rationally
normalizable, one not.

**Dead end three — the naive two-block extension.** `Y = B_2 X* pi_0 + B_0 (…)
pi_2` commutes with `W` exactly, which is a real result, and it is not an
isometry, which was read as a per-sector normalization mismatch. It is not:
`rank(Y) = 4`. The map annihilates the heavy sector, and the light part it does
carry is *already* an exact isometry. The repair was one term, `+ Ph`, and it
was invisible while the defect was being read as a normalization problem.

**Dead end four — displaying the triangular form as the result.** `[[r,0],[s,1]]`
at both fixtures looks like a structure theorem and is a coordinate. What
survives a change of sector bases is `X* W_0 = W_2 X*` together with
`X*^T K_2 X* = K_0`, and the only bridge from the display to anything basis-free
is `r^2 = det K_0 / det K_2`. Testing that by an explicit rational base change
took four lines and moved the whole claim from *shape* to *equivalence*.

**What actually worked.** Solving exactly instead of exhibiting; asking for a
dimension instead of an element; reducing the quadratic system to one primitive
polynomial and factoring it; checking the chart at infinity so the count could
be called complete; and asking *where* a defect lives before naming its cause.

---

## N5 — the fence

```text
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE SCOPE OF THE WORD SYMMETRY IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 AND T = 20 (the staggered Dirac-Kahler carrier on Z_T x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), BLOCK 190's CORE FRAME AT THE DEEP CORE t0 = 3 (the eight cells b <-> (t_b, x_b) with t_b in {t0, t0+1}, the reflected pairings L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1 with K_c = L_0, the STEP operator V = K_c^-1 L_1 and the UNIT-CELL MONODROMY W = K_c^-1 L_2), THE S-MOMENTUM REFINEMENT OF BLOCK 190's U-GRADING, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT (the one-site spatial shift S on the core, the real momentum projectors P0 = (I + S + S^2 + S^3)/4 and P2 = (I - S + S^2 - S^3)/4 and the heavy projector Ph = (I - S^2)/2, three exact rational idempotents of ranks 2, 2 and 4 summing to I_8), THE SECTOR COMPRESSIONS ON COLUMN-SPACE BASES (B_p a column-space basis of P_p and pi_p = (B_p^T B_p)^-1 B_p^T its exact coordinate left inverse, giving W_p = pi_p W B_p, V_p = pi_p V B_p, K_p = B_p^T K_c B_p and the cross Gram K_02 = B_0^T K_c B_2), BLOCK 190's 2048-ELEMENT SIGNED-MONOMIAL CANDIDATE SET REBUILT HERE FROM ITS OWN LANDED DEFINITION AS THE CONTRAST CLASS AND NOT CITED (an optional swap of the two time layers, times every spatial dihedral action of the core -- 4 rotations and 2 reflections -- times every relative sign pattern UP TO AN OVERALL SIGN, 2 * 8 * 2^7 = 2048 matrices), and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module at UNIT VOLUME -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORD SYMMETRY AND IS SAID IN THOSE WORDS: 'SYMMETRY' NAMES AN EXACT RATIONAL 8 x 8 MATRIX THAT COMMUTES WITH ONE CORE's MONODROMY AND PRESERVES ONE CORE's GRAM -- IT IS A MONODROMY-LEVEL STATEMENT ABOUT THE PAIR (W, K_c) AND NAMES NOTHING ELSE. X* DOES NOT INTERTWINE THE STEP SECTORS: nnz(X* V_0 - V_2 X*) = 4 at BOTH FIXTURES AND BOTH WIDTHS, SO NOTHING HERE IS A SYMMETRY OF THE CARRIER, OF THE STEP OPERATOR, OR OF A THEORY. THE TRIANGULAR DISPLAY X* = [[r, 0], [s, 1]] IS A BASIS GAUGE AND NOT AN INVARIANT: under B_0 -> B_0 A_0 and B_2 -> B_2 A_2 the sector data transforms as W_p -> A_p^-1 W_p A_p, K_p -> A_p^T K_p A_p and X -> A_2^-1 X A_0, the upper-right ZERO does NOT survive, and r is multiplied by det A_0 / det A_2 -- BOTH MEASURED HERE ON EXPLICIT RATIONAL BASE CHANGES. THE INVARIANT STATEMENT IS PRIMARY AND IS THE ONE TO QUOTE: X* SIMULTANEOUSLY INTERTWINES (W_0, W_2) AND IDENTIFIES (K_0, K_2), i.e. X* W_0 = W_2 X* AND X*^T K_2 X* = K_0. BLOCK 190 IS NOT CORRECTED: ITS CENSUS CLASSIFIED THE SIGNED MONOMIALS, IT IS REBUILT HERE CANDIDATE FOR CANDIDATE AND CONFIRMED, AND Y' EXTENDS THE ISOMETRIC COMMUTANT BEYOND THE MONOMIALS RATHER THAN CONTRADICTING ANYTHING IN IT. NO GENERIC (m, c) THEOREM IS SUPPLIED AND NO CONTINUUM LIMIT IS SUPPLIED: ONE CORE, TWO WIDTHS AND TWO RATIONAL POINTS ARE NOT A PARAMETER SPACE AND ARE NOT A LIMIT. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE SECTOR SPLIT, AND EVERY STATEMENT IN IT IS AN EXACT ENTRY COUNT. At the deep core t0 = 3 of both widths and at BOTH rational points (m, c) = (9/20, 5/13) and (1/2, 1/3), the rebuilt carrier is the LANDED one: rank(Q) = 64 at T = 16 and 80 at T = 20 with two-sided inverse residuals ZERO, and Block 190's own witness (W - V^2)[0,4] at T = 20, t0 = 3 comes back as 53601896033238042551256/229758595220483765728625 with nnz(W - V^2) = 32, at residual ZERO and without importing that runner. THE CORE GRAM IS EXACTLY SYMMETRIC: nnz(K_c - K_c^T) = 0. THE ONE-SITE SHIFT COMMUTES AND IS NOT AN ISOMETRY, WHICH IS THE WHOLE REASON THERE IS A QUESTION: nnz([W, S]) = 0 and nnz(S^4 - I) = 0 with S^2 = U at ZERO, while nnz(S^T K_c S - K_c) = 64 -- Block 190's own number -- and nnz(U^T K_c U - K_c) = 0. So the shift GRADES the monodromy without preserving the pairing, and the p = 0 / p = 2 equality it produces is NOT forced by S being a symmetry, because S is not one. THE THREE SECTORS HAVE EXACT DIMENSIONS 2, 2 AND 4, with the eigenvalue certificates S B_0 = +B_0, S B_2 = -B_2 and U B_h = -B_h at residual ZERO -- p = 0 and p = 2 are the two REAL momentum sectors and the heavy sector is the U-ODD complement. AND THE ISOSPECTRALITY IS EXACT: charpoly(W_0) and charpoly(W_2) are the SAME primitive integer tuple, (39529825, -109432706, 39529825) at the control and (233, -690, 233) at the fresh point, disjoint from the heavy quadratics (22569375, -233631106, 22569375) and (739, -7258, 739) whose squares complete Block 190's charpoly(W).\nper_mode: THE SOLUTION SPACE IS DECIDED AND NOT SAMPLED, AND WHAT IS DECIDED IS PROJECTIVE. The exact Sylvester system X W_0 - W_2 X = 0 is four linear equations in four unknowns over QQ and its nullity is EXACTLY 2 at every width and both points. Imposing X^T K_2 X = lam K_0 on that plane gives two 2 x 2 symmetric-form constraints; writing X = a X_0 + b X_1 and D = X^T K_2 X, the conformality is the vanishing of the minors D[0,0] K_0[0,1] - D[0,1] K_0[0,0] and D[0,0] K_0[1,1] - D[1,1] K_0[0,0], and BOTH equal ONE primitive quadratic in t = a/b: 64358813 t^2 + 329444835 t - 164444072 at the control and 1891 t^2 + 6491 t - 2796 at the fresh point, with both quotients UNITS. They factor over QQ as (227 t - 104)(283519 t + 1581193) and (31 t - 12)(61 t + 233), and the chart at infinity carries NO branch, so the count of TWO nonzero projective rays is EXHAUSTIVE and not a search result. THE UNIT RAY IS alpha = (104/227) beta at the control and (12/31) beta at the fresh point, and normalizing X[1,1] = 1 on it gives the lam = 1 isometry with X* = [[1369/1135, 0], [104/227, 1]] and [[37/31, 0], [12/31, 1]] EXACTLY. THE OTHER RAY IS alpha = -(1581193/283519) beta and -(233/61) beta with lam = 2323487131056/80383023361 and 53816/3721. lam SCALES AS beta^2 UNDER A COMMON RESCALING OF X, so lam itself is not projective data and ITS SQUARE CLASS IS: the second lam has numerator 2^4 * 3^3 * 7 * 13 * 31 * 37 * 227^2 over denominator 283519^2 at the control and 2^3 * 7 * 31^2 over 61^2 at the fresh point, both NONSQUARE in QQ, so the second ray is NOT rationally normalizable to lam = 1 and the two rays are genuinely distinct isometry classes. AND r IS A GRAM-VOLUME RATIO AND NOT AN ABSOLUTE SCALAR: taking determinants of X*^T K_2 X* = K_0 gives r^2 = det K_0 / det K_2 = 1874161/1288225 = 1369^2/1135^2 and 1369/961 = 37^2/31^2, the displayed shear obeys s = (K_0[0,1] - r K_2[0,1]) / K_2[1,1] with K_0[1,1] = K_2[1,1] exactly, and an explicit base change with det A_0 = 2, det A_2 = 1 MOVES r from 1369/1135 to 2738/1135 while the identity r^2 = det K_0 / det K_2 still holds in the new gauge.\nper_block: THE COMPLETION, AND IT IS THE CHECK's DISCOVERY CARRIED AS CONTENT. The naive two-block extension Y = B_2 X* pi_0 + B_0 (K_0^-1 X*^T K_2 / lam) pi_2 commutes with the monodromy EXACTLY -- nnz([W, Y]) = 0 -- but has rank 4 and nnz(Y^T K_c Y - K_c) = 64, and the solve recorded that defect as a per-sector normalization mismatch and the full-core completion as OPEN. THAT DIAGNOSIS WAS WRONG AND THE REPAIR IS ONE TERM: the light exchange [[0, X*^-1], [X*, 0]] has light-Gram defect EXACTLY 0, so the entire 64-entry defect is the ZEROED HEAVY SECTOR. Restoring it by the identity gives Y' = B_2 X* pi_0 + B_0 X*^-1 pi_2 + Ph, and at BOTH fixtures and BOTH widths, over QQ and entrywise, [W, Y'] = 0, Y'^T K_c Y' = K_c, Y'^2 = I_8 and rank(Y') = 8. The exact control completion is 1/1553815 times the integer matrix with rows (1567504, 146484, 13689, 146484, 0, 0, 0, 0), (-146484, -13689, -146484, -1567504, 0, 0, 0, 0), (13689, 146484, 1567504, 146484, 0, 0, 0, 0), (-146484, -1567504, -146484, -13689, 0, 0, 0, 0), (30420, 325520, 30420, 325520, 1553815, 0, 0, 0), (-325520, -30420, -325520, -30420, 0, 0, 0, -1553815), (30420, 325520, 30420, 325520, 0, 0, 1553815, 0), (-325520, -30420, -325520, -30420, 0, -1553815, 0, 0); the fresh completion is 1/1147 times (1156, 102, 9, 102, 0, 0, 0, 0), (-102, -9, -102, -1156, 0, 0, 0, 0), (9, 102, 1156, 102, 0, 0, 0, 0), (-102, -1156, -102, -9, 0, 0, 0, 0), (18, 204, 18, 204, 1147, 0, 0, 0), (-204, -18, -204, -18, 0, 0, 0, -1147), (18, 204, 18, 204, 0, 0, 1147, 0), (-204, -18, -204, -18, 0, -1147, 0, 0). FOUR EXACT CERTIFICATES LICENSE THE SECTOR-BY-SECTOR ARGUMENT: nnz(K_02) = 0, the light-heavy blocks of K_c and of W vanish at 0 and 0 entries in the frame (B_0, B_2, B_h) of rank 8, the light and heavy squarefree primaries are COPRIME, and K_0^-1 X*^T K_2 = X*^-1 at residual 0. alpha^2 = 1 IS FORCED AND NOT CHOSEN: the light swap [[0, X*^-1], [alpha X*, 0]] preserves K_light exactly at alpha = -1 and alpha = +1 and nowhere else. AND THE ISOMETRIC COMMUTANT CONTAINS A KLEIN FOUR-GROUP: with U = S^2 the four elements {I, U, Y', UY'} are mutually distinct, all involutive, all K_c-isometries and all commuting with W, with nnz(UY' - Y'U) = 0.\nlattice_wide: THE SCOPE IS MONODROMY-LEVEL, AND THAT IS EXACTLY WHY THE MONOMIAL CENSUS COULD NOT SEE IT. X* DOES NOT INTERTWINE THE STEP SECTORS: nnz(X* V_0 - V_2 X*) = 4 at every width and both points, with exact first witnesses -142376/257645 at the control and -444/961 at the fresh point. BLOCK 190's CENSUS IS REBUILT HERE CANDIDATE FOR CANDIDATE RATHER THAN CITED, AND FROM ITS OWN LANDED CANDIDATE DEFINITION: all 2048 candidates are swept, EXACTLY 4 commute with W -- {I, S, U, S^3}, with ZERO unnamed survivors -- and EXACTLY 2 of those are Gram isometries, {I, U}, with per-power Gram defects (0, 64, 0, 64) for S^0, S^1, S^2, S^3. BLOCK 190's REFUTED CANDIDATE STAYS REFUTED WITH ITS LANDED WITNESSES REPRODUCED: the unsigned spatial reflection R has nnz([W, R]) = 16 with [W, R][0,5] = 16334218/7905965 at the control and 2414/1165 at the fresh point, and the first nonzero of S^T K_c S - K_c at T = 20 and the control fixture is Block 190's own declared literal 2196923328476037505923247454222973532938493206039747366330235451412004291015625/2814140416367857864535548440193722522538862625515710221151046656087532099673561724. Y' IS NOT A MONOMIAL: its row weights are (4, 4, 4, 4, 5, 5, 5, 5) and it equals no censused candidate, and neither does UY'. So the isometric monomial commutant is {I, U} and the isometric commutant proper contains at least {I, U, Y', UY'}, two of whose elements lie outside the sweep BY CONSTRUCTION. THIS IS AN EXTENSION OF BLOCK 190 AND NOT A CORRECTION TO IT: every number in that census is reproduced here, and what changes is only that the ADDITIONAL exact isospectrality Block 190 recorded as NOT GROUP-FORCED is now exhibited as forced by a NON-MONOMIAL involutive isometry.\nper_scope: THE MECHANISM IS OF THE CLASS AND NOT OF THE FIXTURE, THE PERSISTENCE IS NOT VACUOUS, AND WHAT REMAINS OPEN IS NAMED. At T = 20 the Sylvester dimension, BOTH projective branches with both lam values, the triangular entries and the completion Y' with all three identities are IDENTICAL to T = 16 at both points. That agreement is not an identity, because the data it is computed from MOVES: W, V, W_0, W_2, V_0 and V_2 are width-invariant at residual 0, while EACH of K_0 and K_2 changes in ALL FOUR entries and the core Gram K_c changes in ALL 64 -- so the branches are re-derived against changed Grams and return the same rays. At the second rational point (1/2, 1/3), whose imported unit-volume block is diag(1, [[9/8, -3/8], [-3/8, 9/8]], 1), every structural statement above holds on a carrier that is measurably different: nnz(Q(9/20,5/13) - Q(1/2,1/3)) = 512 of 512 nonzero entries at T = 16. WHAT REMAINS OPEN IS NAMED AND NOT PAPERED OVER: WHY the carrier admits such an isometry is NOT derived, and the operator is exhibited rather than explained; whether the isometric commutant is EXACTLY the Klein four-group is NOT decided, because no exhaustive sweep of the non-monomial isometric commutant is performed; ONE core t0 = 3 is probed and nothing is claimed at any other core; two widths are not a width family theorem and two rational points are not a parameter space; and no Osterwalder-Schrader reconstruction, no transfer interpretation and no physical reading of Y' is supplied by any line of this block.\nRESULT: ON BLOCK 190's WIDTH FAMILY AT T = 16 AND T = 20, AT THE DEEP CORE t0 = 3 AND AT BOTH RATIONAL POINTS, THE p = 0 / p = 2 ISOSPECTRALITY OF THE UNIT-CELL MONODROMY IS IMPLEMENTED BY AN EXACT INVOLUTIVE K_c-ISOMETRY IN THE FULL COMMUTANT OF W: THE SYLVESTER SPACE HAS DIMENSION 2, THE GRAM-CONFORMALITY CONDITION LEAVES EXACTLY TWO PROJECTIVE RAYS DECIDED BY ONE PRIMITIVE QUADRATIC, THE lam = 1 RAY CARRIES AN INTERTWINER X* THAT SIMULTANEOUSLY IDENTIFIES (K_0, K_2), AND Y' = B_2 X* pi_0 + B_0 X*^-1 pi_2 + Ph SATISFIES [W, Y'] = 0, Y'^T K_c Y' = K_c AND Y'^2 = I_8 ENTRYWISE OVER QQ. Block 190's recorded leftover -- that the p = 0 / p = 2 equality is NOT GROUP-FORCED by any signed monomial -- is thereby EXPLAINED AND NOT CONTRADICTED: the forcing operator exists and is non-monomial, so the 2048-candidate sweep was exhaustive over the wrong class. THE SCOPE IS MONODROMY-LEVEL AND THE TRIANGULAR DISPLAY IS A GAUGE, AND BOTH ARE SAID BEFORE THE RESULT IS. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-196 STAND EXACTLY AS LANDED. BLOCK 190 IS NOT CORRECTED: its carrier, its core frame, its unit-cell monodromy, its shift algebra, its 64-entry S-Gram defect with its exact witness, its refuted spatial reflection and its 2048-candidate commutant census are all rebuilt here and reproduced, and its own declared leftover is what this block resolves. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE core, TWO widths, TWO rational points and ONE profile at unit volume -- not a scan, not a limit and not a width family theorem; the operator is EXHIBITED and its existence is NOT derived from the carrier; the isometric commutant is shown to CONTAIN a Klein four-group and is NOT shown to equal one; and the triangular display is a basis gauge whose entries carry no invariant meaning beyond r^2 = det K_0 / det K_2. THREE ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the FULL COMPLETION Y', which the solve had recorded as a named OPEN refinement; the DIAGNOSIS of the naive extension's 64-entry Gram defect as the zeroed heavy sector rather than a per-sector normalization mismatch; and the BASIS-DEPENDENCE of the triangular form together with the invariant statement that replaces it. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE p=0/p=2 ISOSPECTRALITY MECHANISM (block 197 candidate), ISO PHASE 1 MEASURED, ISO PHASE 2 MEASURED, ISO PHASE 3 MEASURED and B197 CHECK VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
```

---

## N6 — STOP AND REOPEN

### STOPPED, and why each is stopped

1. **Deriving the existence of `Y'`.** Stopped: nothing found. No argument from
   `Q = m H + H D_s - D_s^T H` and the grading produces the operator, and this
   note refuses to dress exhibition as derivation.
2. **Deciding the full isometric commutant.** Stopped: containment is proven,
   equality is not attempted. The non-monomial isometric commutant is a
   variety, not a finite list, and no partial scan of it would be a theorem.
3. **Other cores.** Stopped: `t0 = 3` is the deep core Block 190 used for the
   commutant census, and that is the comparison this block owes. Other cores
   would have to be measured, not assumed.
4. **A third width or a third point.** Stopped: two of each is what the check
   confirmed, and a third would have to be checked.
5. **Any reading of `Y'` as a physical symmetry.** Stopped: no
   Osterwalder–Schrader reconstruction, no transfer interpretation, no state
   space. `R2` names the temptation and refuses it.

### REOPEN IF

1. A **derivation** of `Y'` from the carrier is found — some grading, reflection
   or reciprocity argument forcing an involutive isometry that exchanges the two
   real momentum sectors. That would turn `R1` from a reading into a theorem.
2. The **isometric commutant is decided**, either by exhibiting a fifth element
   or by proving the Klein four-group exhaustive. That resolves `R4` and fence
   `2`.
3. **Another core** reproduces the mechanism, at which point the phrase *a
   property of the width family* gains its first real evidence.
4. The **second ray** acquires meaning. Its `lam` is a fixed nonsquare class at
   both points, and nothing here says what a non-normalizable conformal
   intertwiner is for.
5. The **heavy sector** turns out to admit its own nontrivial isometric
   intertwiner, in which case `Y'` is one member of a larger family rather than
   the completion of a light exchange.

---

## N7 — THE RECORD

### Corrections carried

**THE LEDGER CONTINUES FROM BLOCK 196's #75. NO CORRECTION IS LANDED BY THIS
BLOCK AGAINST ANY LANDED NUMBER.** Every item below corrects **this lane's own
solve language** or folds an adversarial-check finding as content; each is a
declared constant with a gate and, where it guards a correction, a mutation.

76. **THE TRIANGULAR FORM IS A BASIS GAUGE AND THE SOLVE DISPLAYED IT AS A
    STRUCTURE.** The phase-3 anchor writes *"the `λ=1` isometric intertwiner is
    TRIANGULAR with generic shape `X* = [[r, 0], [s, 1]]` … the SAME structural
    form at both points (the mechanism is generic)."* The shape is a property of
    the column-space bases: under `B_0 -> B_0 A_0`, `B_2 -> B_2 A_2` the
    upper-right zero does not survive and `r` is multiplied by
    `det A_0 / det A_2`. Both are measured here on explicit rational base
    changes. The invariant statement — `X*` simultaneously intertwines
    `(W_0, W_2)` and identifies `(K_0, K_2)` — is primary throughout, and
    `r^2 = det K_0 / det K_2` is the only relation carrying the display to
    anything basis-free. This is the check's `P2`, carried as content. Gates
    `B-4`, `D-6`, mutations `claim_basis_independent_triangle`,
    `break_determinant_law`.
77. **THE NAIVE EXTENSION'S DEFECT WAS MISATTRIBUTED, AND THE COMPLETION
    EXISTS.** The phase-3 anchor records *"`Y` is not a full-Gram isometry under
    the naive normalization (the per-sector `λ` mismatch; the full-core
    isometric completion is a NAMED OPEN refinement)."* The cause is not a
    normalization: `rank(Y) = 4`, the map annihilates the heavy sector, and its
    light restriction has light-Gram defect exactly `0`. Adding `Ph` gives
    `Y'` with `[W, Y'] = 0`, `Y'^T K_c Y' = K_c` and `Y'^2 = I_8` all exact.
    This is the check's `P1` upgrade, carried as content and displayed
    entrywise. Gates `F-1`, `F-2`, `F-5`, mutations `break_completion_matrix`,
    `break_defect_diagnosis`.
78. **"A NEW NON-MONOMIAL ELEMENT OF `W`'s COMMUTANT" IS THE WRONG PLACEMENT OF
    THE CLAIM.** The commutant of `W` already contains `S`, which has a
    `64`-entry Gram defect — so *non-monomial element of the commutant* is a
    weak statement. What is new is an element of the **isometric** commutant,
    and that is the set the census actually constrained. Block 190's census is
    rebuilt from **its own landed candidate definition** and confirmed: `4` of
    `2048` commute, `{I, S, U, S^3}`, of which `2` are isometries, `{I, U}`,
    with zero unnamed survivors — and its refuted reflection reproduced with
    both landed witnesses. `BLOCK190_CORRECTED_CLAIMED = False` is a declared
    constant. Gates `B-5`, `E-2`, `E-3`, `E-5`, mutations
    `claim_b190_corrected`, `break_monomial_census`,
    `break_isometric_monomials`, `break_reflection_refutation`.
79. **"TWO NONTRIVIAL SOLUTION FAMILIES" NAMES TWO PROJECTIVE RAYS, NOT TWO
    MATRICES.** Rescaling `X` by a rational multiplies `lam` by a rational
    square, so the displayed `lam#` values are gauge-dependent and their
    **square class** is not. Both `lam#` numerators are nonsquare, so the second
    ray is not rationally normalizable to `lam = 1` — which is the basis-free
    distinction between the two rays and is stated here rather than implied by
    two displayed numbers. Gates `D-3`, `D-5`, mutations `break_lambda_branch`,
    `break_square_class`.
80. **THE MECHANISM IS MONODROMY-LEVEL AND THE SCOPE MUST BE SAID FIRST.** The
    phase-3 anchor states the `V`-scope refutation, and it is easy to read the
    result as a symmetry of the construction. `X* V_0 - V_2 X*` has `4` nonzero
    entries with exact witnesses at both fixtures and both widths;
    `STEP_LEVEL_SYMMETRY_CLAIMED = False` is a declared constant and the banner
    carries it before the first numeral. Gates `B-3`, `E-1`, mutations
    `claim_step_level_symmetry`, `break_step_scope`.
81. **THE `T = 20` PERSISTENCE IS ONLY MEANINGFUL BECAUSE THE GRAMS MOVE.** The
    check reports `T = 20` agreement; stated bare it invites the reading that
    nothing was recomputed. Measured here: `W`, `V`, `W_p` and `V_p` are
    width-invariant at residual `0`, while **each** of `K_0`, `K_2` moves in all
    four entries and `K_c` in all `64`. The branches are therefore re-derived
    against changed data. Gates `G-1`, `G-2`, mutations
    `break_width_persistence`, `break_gram_motion`.

### The adversarial check

Verdict carried as **HIDDEN-ISOMETRY CONFIRMED, WITH A POSITIVE `P1` UPGRADE**
(`sol xhigh`, independent rebuild from the landed Block 190 note rather than an
invocation of its runner; findings preserved at `b197_check_findings.md`,
checker at `b197_exact_check.py`).

**`C1`–`C4` WERE CONFIRMED EXACTLY** at both `T = 16` fixtures, including
exhaustiveness on the projective intertwiner line. **`P1` SUCCEEDED WHERE THIS
LANE'S OWN EXTENSION FAILED** and its completion is correction `77`. **`P2`
IDENTIFIED THE INVARIANT CONTENT** and is correction `76`. **`P3` CONFIRMED THE
MECHANISM AT `T = 20`.**

**THE CHECK'S EXACT WITNESSES ARE REPRODUCED DIGIT FOR DIGIT.** Both `8 x 8`
completions, both branch quadratics with their factorizations, both `lam#`
factorizations, the two `C3` witnesses and the two `C4` Gram-defect witnesses
are **declared literals** in this block's runner rather than printed byproducts.

**AND THE CHECK IS EXTENDED IN FIVE PLACES,** all five re-measured independently
here: Block 190's `2048`-candidate census is **rebuilt from its own landed
definition** rather than cited — with its refuted reflection and its two landed
witnesses reproduced digit for digit — so the *why the sweep missed it* claim is
a measurement (`E-2`, `E-3`, `E-5`); the basis-dependence of the triangular form
is **probed** on two explicit rational
base changes rather than argued from the transformation law (`D-6`); the
`lam ↦ beta^2 lam` scaling is verified **symbolically** rather than by
inspection (`D-3`); the Klein four-group `{I, U, Y', UY'}` is measured as a
group — commuting, involutive, isometric, distinct — which the check noted but
did not gate (`F-3`); and the `T = 20` motion of the two compressed Grams is
measured, which is what makes the persistence non-vacuous (`G-2`).

**THE CHECK'S SCOPE IS ALSO NARROWED HERE IN ONE PLACE, DELIBERATELY.** Its
`P1` parameterization allowed *any* exact heavy block commuting with `W_h`; this
note claims only the branch it exhibits, `alpha = +1` with the heavy identity,
and gates `alpha^2 = 1` as forced rather than claiming the heavy choice is
unique.

**THE PROVENANCE CAVEAT IS ACKNOWLEDGED AND HANDLED.** The Block 190 artifact is
not present on canonical `origin/main`; it is landed in the stacked physics-loop
history. Gate `A-2` binds the **Block 196** parent artifacts by blob at
`PARENT_COMMIT` and in the worktree, and verifies that the stale pin — the Block
195 tip — is a real ancestor carrying neither, so *landed* here means exactly
*landed in this branch history* and the note says so rather than implying more.

### What is NOT corrected

Every Block 104, 105, 106, 107, 128 and 181–196 number **stands as landed**.
**Block 190 is not corrected**: its carrier, its core frame, its unit-cell
monodromy, its shift algebra, its `64`-entry `S`-Gram defect and its
`2048`-candidate commutant census are all rebuilt here and reproduced, and its
own declared leftover is what this block resolves. Block 191's cell-average
assembly and Block 105's `shear_hodge` are used unchanged.

### Reproduction

```text
python3 scripts/admissibility_dirac_kahler_hidden_involutive_isometry_2026_08_26.py
python3 ... --list-mutations
python3 ... --mutation claim_basis_independent_triangle
```

Baseline expectation: families `A` through `H` PASS, `37` checks, exit `0`.
Thirty-seven declared mutations, each flipping **exactly one** family and
exiting nonzero; per-family census `A 2, B 8, C 4, D 6, E 5, F 7, G 3, H 2`.
Every measurement is taken once, before any mutation flag is read, so no gate can
cascade into another. Four exact carrier inverses — two `64 × 64` and two
`80 × 80` — are built once and shared by every gate, and no other inverse in
this runner exceeds `8 × 8`.

### Provenance

`CAMPAIGN_20260824_GRAVITY_MAINLINE.md`, at its **THE p=0/p=2 ISOSPECTRALITY
MECHANISM (block 197 candidate)**, **ISO PHASE 1 MEASURED**, **ISO PHASE 2
MEASURED**, **ISO PHASE 3 MEASURED** and **B197 CHECK VERDICT** anchors.
