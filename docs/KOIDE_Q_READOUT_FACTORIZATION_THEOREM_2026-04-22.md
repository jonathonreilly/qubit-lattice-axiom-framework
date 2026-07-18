# Koide Q Readout Rank/Kernel Quotient Theorem

**Date:** 2026-04-22
**Claim type:** bounded_theorem
**Status:** exact finite-dimensional rank/kernel/image/fiber/quotient theorem;
not a selector-classification or physical-closure theorem
**Primary runner:** `scripts/frontier_koide_q_readout_factorization_theorem.py`

## Exact scope

This note proves only the quotient theorem for the readout obtained from the
explicitly defined returned operator

```text
A(W) = P_{T_1} Γ_1 W Γ_1 P_{T_1}.
L_t(W) = B_t^* A(W) B_t,  t in {0,1}.
```

The basis calculation below proves `L_0(W)=L_1(W)`. The map used in the
quotient theorem is their common `3 x 3` diagonal restriction
`L(W):=L_0(W)=L_1(W)`, while the full six-state restriction of `A(W)` is
`diag(L(W),L(W))`. Thus the codomain `Diag_3(R)` is an explicit restriction,
not a type-identification of the full `16 x 16` operator.

For the separately declared selector class

```text
𝒮_L = {S : S = Φ composed with L for some Φ on Diag_3(R)},
```

kernel invariance is an immediate **definitional corollary**. It is not a
classification theorem. In particular, the separately listed adjectives
"local", "bosonic/even in `Γ_1`", "first-live", "species-resolving", and
"`C_3`-covariant" do not by themselves exclude every `z`-sensitive scalar in
the material proved here. No non-circular admissibility theorem connecting
those adjectives to `𝒮_L` is supplied or claimed.

## 1. Basis-level construction

Use the ordered basis

```text
|a,b,c;t>,  a,b,c,t in {0,1},
```

of `C^16`, where the final bit `t` is the time/chirality copy. The defined
branch convention is

```text
Γ_1 = X tensor I tensor I tensor I,
Γ_1 |a,b,c;t> = |1-a,b,c;t>.
```

Thus `Γ_1` flips the first spatial bit and preserves `t`. Every spatial
projector includes both time copies:

```text
P_s = |s;0><s;0| + |s;1><s;1|.
```

Order the returned species basis as

```text
T_1 = ((1,0,0), (0,1,0), (0,0,1)).
```

For each `t=0,1`, let `B_t : R^3 -> C^16` embed the three standard basis
vectors as the correspondingly ordered `|s;t>` states, and define the
restriction of a `16 x 16` operator `A` by `B_t^* A B_t`. The full six-state
restriction is the direct sum of the `t=0` and `t=1` restrictions.

The one-hop transitions from `T_1` are, identically on both time copies,

```text
(1,0,0) --Γ_1--> (0,0,0),
(0,1,0) --Γ_1--> (1,1,0),
(0,0,1) --Γ_1--> (1,0,1).
```

The spatial slot `(0,1,1)` is not reached. Consequently, for either `t`,

```text
B_t^* P_{T_1} Γ_1 P_{(0,0,0)} Γ_1 P_{T_1} B_t = diag(1,0,0),
B_t^* P_{T_1} Γ_1 P_{(1,1,0)} Γ_1 P_{T_1} B_t = diag(0,1,0),
B_t^* P_{T_1} Γ_1 P_{(1,0,1)} Γ_1 P_{T_1} B_t = diag(0,0,1),
B_t^* P_{T_1} Γ_1 P_{(0,1,1)} Γ_1 P_{T_1} B_t = 0.
```

There is no hidden single-copy convention: the corresponding full
six-state restrictions are two identical `3 x 3` blocks.

## 2. Exact map and quotient theorem

Define the four-slot weight operator

```text
W(u,v,w,z)
  = u P_{(0,0,0)} + v P_{(1,1,0)}
  + w P_{(1,0,1)} + z P_{(0,1,1)}.
```

The basis calculation gives, on each time copy,

```text
L(u,v,w,z) = diag(u,v,w),
```

so, after identifying `Diag_3(R)` with `R^3` by its diagonal, the exact
matrix is

```text
L = [ I_3  0 ].
```

It follows directly that

```text
rank(L) = 3,
im(L) = Diag_3(R),
ker(L) = span{e_z},  e_z = (0,0,0,1).
```

For `d=(d_1,d_2,d_3)`, the fiber is

```text
L^{-1}(diag(d_1,d_2,d_3))
  = {(d_1,d_2,d_3,z) : z in R}.
```

Equivalently, `L(x)=L(y)` if and only if `x-y` lies in `span{e_z}`.

Let `J : R^3 -> R^4` be `J(d_1,d_2,d_3)=(d_1,d_2,d_3,0)`. Then

```text
L J = I_3,
I_4 - J L = e_z e_z^T,
L e_z = 0.
```

These identities construct mutually inverse maps between the quotient and
the image, rather than merely counting dimensions. Therefore

```text
R^4 / span{e_z}  is isomorphic to  Diag_3(R).
```

This rank/kernel/image/fiber/quotient statement is the theorem of the note.

## 3. `C_3` intertwining and invariant quadratics at their actual scope

On the coefficient and diagonal spaces, declare the forward cycles

```text
rho_4(u,v,w,z) = (w,u,v,z),
rho_3(d_1,d_2,d_3) = (d_3,d_1,d_2).
```

The unreachable coordinate is fixed. With these explicitly declared
orientations,

```text
rho_3 L = L rho_4.
```

This is the exact `C_3` intertwining statement. It concerns the displayed
linear representations and does not classify scalar selectors on `R^4`.

If `q(d)=d^T Q d` is a real quadratic scalar on the image, then
`q(rho_3 d)=q(d)` exactly when

```text
Q = [[a,b,b],
     [b,a,b],
     [b,b,a]].
```

Thus the invariant quadratic space on `Diag_3(R)` is two-dimensional; for
example it is spanned by `(d_1+d_2+d_3)^2` and
`(d_1-d_2)^2+(d_2-d_3)^2+(d_3-d_1)^2`. This algebra is established only on
the image of `L`. It supplies no independent theorem that a scalar originally
defined on all four coefficients must ignore `z`.

Indeed, `S_z(u,v,w,z)=z` is invariant under the declared `rho_4` cycle but is
not constant on `ker(L)`. This gives an exact finite-dimensional warning
against treating `C_3` covariance as the missing classification theorem.

## 4. Definitional selector corollary

Declare, separately from the theorem,

```text
𝒮_L = {S : R^4 -> R | there exists Φ : Diag_3(R) -> R with S = Φ composed with L}.
```

For `S` in `𝒮_L` and any real `eta`,

```text
S(W + eta e_z)
  = Φ(L(W + eta e_z))
  = Φ(L(W))
  = S(W).
```

This is a definitional corollary of membership in `𝒮_L` plus `L e_z=0`.
Because `L` is surjective, the corresponding `Φ` is unique once `S` is in
that class. Neither existence of `Φ` nor membership in `𝒮_L` is derived from
the separate locality, parity, species-resolution, or covariance adjectives.

## 5. Honest boundary and frozen baseline

This note does not:

1. classify every local, bosonic, first-live, species-resolving, or
   `C_3`-covariant scalar as an element of `𝒮_L`;
2. identify any physical charged-lepton selector with a member of `𝒮_L`;
3. identify the diagonal image or a reduced determinant carrier as the
   physical charged-lepton carrier;
4. fix `D_red = I_2`, a response-unit normalization, or any source law;
5. derive `Q=2/3`, a mass spectrum, a comparator match, or the separate
   Brannen `delta` bridge;
6. add an axiom, admission, primitive, carrier, physical input, premise
   entry, or authority import.

The remaining honest boundary is a non-circular physical/admissibility
classification theorem, if one is sought. The present result stops at the
exact finite-dimensional quotient and its explicitly definition-driven
selector corollary.
