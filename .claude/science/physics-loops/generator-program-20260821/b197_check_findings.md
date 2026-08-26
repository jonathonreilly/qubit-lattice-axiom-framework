# Block 197 adversarial check — hidden isometry mechanism

Status: **IN PROGRESS**.

Scope fixed by dispatch: exact `Rational`/`QQ` arithmetic only (no
`nsimplify`); construction authority is the tracked, landed-in-campaign Block
190 width-family note and its `v = 1` Hodge construction.  Primary width
`T = 16`, deep core `t0 = 3`, fixtures `(m,c)=(9/20,5/13)` and
`(1/2,1/3)`; `T = 20` is a spot-check.  This is a scratch analysis only: no
source note, audit ledger, runner, commit, or branch is modified.

The verdict below will distinguish direct exact verification from any
parameterized completion search.  “Exhaustive failure” will be claimed only
relative to an explicitly stated exact parameterization.

## Increment 1 — C1–C4 at `T=16`

Independent reconstruction fingerprints agree with Block 190: the control
Hodge is

```
diag(1, [[169/144,-65/144],[-65/144,169/144]], 1),
```

the fresh Hodge is

```
diag(1, [[9/8,-3/8],[-3/8,9/8]], 1),
```

and at both points `K_c-K_c^T=0`, `[W,S]=0`, while
`nnz(S^T K_c S-K_c)=64`.  These are exact entry counts.

**C1 CONFIRMED.**  The exact coefficient matrix for
`X W_0-W_2 X=0` has nullity `2` at both fixtures.

**C2 CONFIRMED, including exhaustiveness on the projective intertwiner
line.**  Substitution of a two-vector exact Sylvester-nullspace basis into the
Gram-conformality equations makes the two independent `2x2` symmetric-form
constraints share one quadratic factor and no root in the complementary
projective chart.  In the checker's nullspace coordinate `t`, the primitive
quadratics are

```
control: 64358813 t^2 + 329444835 t - 164444072,
fresh:       1891 t^2 +      6491 t -       2796.
```

They factor over `QQ` as

```
(227 t - 104)(283519 t + 1581193),
( 31 t -  12)(    61 t +     233),
```

Both roots produce a matrix with lower-right entry nonzero, so normalizing
that entry to `1` loses no branch.  The two representatives are:

```
control, lambda=1:
X* = [[1369/1135, 0], [104/227, 1]]

control, lambda=2323487131056/80383023361:
X# = [[-5331973/1417595, -1581193/283519],
      [-1581193/283519, 1]]

fresh, lambda=1:
X* = [[37/31, 0], [12/31, 1]]

fresh, lambda=53816/3721:
X# = [[-163/61, -233/61], [-233/61, 1]].
```

Thus “two nontrivial solution families” means two nonzero projective rays;
arbitrary common rescaling of `X` rescales `lambda` quadratically.

**C3 CONFIRMED.**  For the `lambda=1` branch,
`nnz(X* V_0-V_2 X*)=4` at both points.  First exact witnesses (entry `(0,0)`)
are `-142376/257645` at the control and `-444/961` at the fresh point.

**C4 CONFIRMED AS STATED.**  With the column-space bases `B0,B2` and their
exact coordinate left inverses `pi0,pi2`, the displayed two-block extension
has `[W,Y]=0` entrywise at both points.  It has rank `4`, and
`nnz(Y^T K_c Y-K_c)=64`; hence it is not a full-core Gram isometry.  First
defect witnesses at `(0,0)` are

```
control:
-48976132744478519489329652146311862124282444534250707666015625
 /33997719455893540048957560867825104440683420084306798815764692622

fresh:
-15161098351719976229483059/10899840437709830045206044732.
```

## Increment 2 — P1 completion found (the theorem upgrades)

Let

```
P_h = (I-S^2)/2,
B_h = a column-space basis of P_h,
pi_h = (B_h^T B_h)^-1 B_h^T.
```

The exact completion is

```
Y' = B2 X* pi0 + B0 X*^-1 pi2 + B_h pi_h
   = B2 X* pi0 + B0 X*^-1 pi2 + P_h.                 (P1.1)
```

This is the C4 light exchange plus the identity on the heavy `S^2=-1`
sector.  The search parameterization was the rational frame
`F=(B0,B2,B_h)` with a pure light-sector swap

```
Y_light = [[0,C],[alpha X*,0]]
```

and an arbitrary exact heavy block commuting with `W_h`.  Exact Gram
congruence forces `alpha^2=1`; the choice `alpha=1`, `C=X*^-1` works.  The
heavy choice `I_4` works.  The structural certificates at both fixtures are:

- `K_02=0` exactly;
- the light-heavy blocks of both `K_c` and `W` are zero exactly;
- the light and heavy squarefree primary polynomials are coprime;
- the C4 light exchange alone has zero light-Gram defect;
- `K_0^-1 X*^T K_2 = X*^-1` exactly.

Thus the `64`-entry C4 full-Gram defect is entirely the omitted heavy block,
not an obstruction in the light exchange.

At both fixtures, direct `8x8` checks give

```
[W,Y'] = 0,
Y'^T K_c Y' = K_c,
Y'^2 = I_8,
rank(Y') = 8
```

entrywise over `QQ`.  In the specified core order, the exact control
completion is

```
Y'_control =
1/1553815 *
[[ 1567504,   146484,    13689,   146484,       0,       0,       0,       0],
 [ -146484,   -13689,  -146484, -1567504,       0,       0,       0,       0],
 [   13689,   146484,  1567504,   146484,       0,       0,       0,       0],
 [ -146484, -1567504,  -146484,   -13689,       0,       0,       0,       0],
 [   30420,   325520,    30420,   325520, 1553815,       0,       0,       0],
 [ -325520,   -30420,  -325520,   -30420,       0,       0,       0,-1553815],
 [   30420,   325520,    30420,   325520,       0,       0, 1553815,       0],
 [ -325520,   -30420,  -325520,   -30420,       0,-1553815,       0,       0]].
```

The exact fresh completion is

```
Y'_fresh =
1/1147 *
[[ 1156,  102,    9,  102,    0,    0,    0,    0],
 [ -102,   -9, -102,-1156,    0,    0,    0,    0],
 [    9,  102, 1156,  102,    0,    0,    0,    0],
 [ -102,-1156, -102,   -9,    0,    0,    0,    0],
 [   18,  204,   18,  204, 1147,    0,    0,    0],
 [ -204,  -18, -204,  -18,    0,    0,    0,-1147],
 [   18,  204,   18,  204,    0,    0, 1147,    0],
 [ -204,  -18, -204,  -18,    0,-1147,    0,    0]].
```

**Upgrade statement (finite exact scope):** at both disclosed rational
fixtures, the extra `p=0/p=2` isospectrality is implemented by an exact
involutive `K_c`-isometry in the full commutant of `W`.  This still supplies no
OS reconstruction or physical transfer interpretation.

## Increment 3 — P2 invariant content

**The triangular shape is not basis-independent.**  For arbitrary exact
changes of sector bases `B0 -> B0 A0`, `B2 -> B2 A2`,

```
W0 -> A0^-1 W0 A0,       K0 -> A0^T K0 A0,
W2 -> A2^-1 W2 A2,       K2 -> A2^T K2 A2,
X  -> A2^-1 X A0.
```

The zero in the upper-right entry and the individual numbers `r,s` need not
survive this transformation.

The invariant content is the simultaneous equivalence

```
X* W0 = W2 X*,            X*^T K2 X* = K0.           (P2.1)
```

Thus `X*` is an isomorphism of the two rational `QQ[z]` modules equipped with
their compressed Gram forms.  Over the quadratic splitting field it sends
`ker(W0-zeta I)` to `ker(W2-zeta I)` for each root `zeta`; it preserves the
eigenvalue label rather than exchanging the reciprocal roots.  The common
light polynomials are

```
control: 39529825 z^2 - 109432706 z + 39529825,
fresh:          233 z^2 -       690 z +       233.
```

There is also an exact determinant interpretation of the displayed `r`.  In
the triangular gauge, `r=det(X*)>0`, and taking determinants of (P2.1) gives

```
r^2 = det(K0)/det(K2).
```

Indeed the two ratios are `1369^2/1135^2` and `37^2/31^2`.  So `r` is the
positive Gram-volume ratio in the chosen oriented column-space bases.  It is
coordinate-covariant, not an absolute scalar under unrelated changes of the
two bases.  The displayed shear is likewise a gauge quantity; in this gauge

```
s = (K0[0,1] - r K2[0,1]) / K2[1,1],
```

with `K0[1,1]=K2[1,1]` exactly.

The two projective branches have a further basis-independent arithmetic
distinction.  Rescaling `X` by a rational multiplies `lambda` by a rational
square, so the square class of `lambda` is projective data.  The `X*` branch
has trivial square class and is the rationally normalizable unit isometry.
The other branch is not rationally normalizable to `lambda=1`:

```
control numerator of lambda#:
2^4 * 3^3 * 7 * 13 * 31 * 37 * 227^2
(denominator = 283519^2),

fresh numerator of lambda#:
2^3 * 7 * 31^2
(denominator = 61^2).
```

Both numerators are nonsquares in `QQ`.

## Increment 4 — P3, `T=20` deep-core spot-check

At `T=20`, `t0=3`, both fixtures again give exact Sylvester nullity `2` and
exactly the same two projective C2 branches, matrices, and `lambda` values as
at `T=16`.  This is nontrivial width persistence: the sector operators obey

```
V0(T20)-V0(T16) = V2(T20)-V2(T16) = 0,
W0(T20)-W0(T16) = W2(T20)-W2(T16) = 0,
```

while each of `K0(T20)-K0(T16)` and `K2(T20)-K2(T16)` has all four entries
nonzero at both fixtures.  Substitution into the changed Grams nevertheless
returns the same two conformal rays.  The completion (P1.1) also retains zero
commutator, zero Gram defect, and `Y'^2=I_8` at `T=20` for both fixtures.

## Final verdict

**CONFIRMED, WITH A POSITIVE P1 UPGRADE.**

- C1, C2, C3, and C4 are exactly correct at both `T=16` fixtures.
- P1 has a full exact solution, (P1.1), displayed above as two rational `8x8`
  matrices.  The hidden `p=0/p=2` isospectrality is therefore implemented by a
  full involutive Gram isometry commuting with `W` at both points.
- C4's non-isometry is real but shallow: it is caused entirely by setting the
  heavy sector to zero.  Its light restriction is already an exact isometry.
- P2's triangular matrix is a basis gauge; the invariant theorem is the
  simultaneous module/Gram equivalence (P2.1), with `r` the positive
  determinant-line/Gram-volume ratio in the displayed gauge.
- P3 confirms the C1-C2 mechanism at `T=20` despite entrywise movement of both
  compressed Grams.

All scientific comparisons above were performed over exact `QQ`.  The checker
contains no floating-point conversion, tolerance, or approximate
rationalization.
