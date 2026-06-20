# Native Gauge Transfer Reduced-A2 Subleading Sign Rung Nineteen Bounded Note

**Date:** 2026-06-12

**Claim type:** bounded_theorem

**Boundary:** partial-with-named-missing-link. Claim type is a source-side boundary declaration, never an audit verdict.

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** [scripts/native_gauge_transfer_reduced_a2_subleading_sign_rung_nineteen_bounded_2026_06_12.py](../scripts/native_gauge_transfer_reduced_a2_subleading_sign_rung_nineteen_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_reduced_a2_subleading_sign_rung_nineteen_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_reduced_a2_subleading_sign_rung_nineteen_bounded_2026_06_12.txt)

No new axiom, literature value, external comparator number, fitted constant, rounded anchor, fitted prefactor, parity proxy, value-from-target step, or float-derived exact rational is used. W90 finite rows are fenced witnesses only and are not proof inputs for any sign claim.

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md) for the retained saddle profile, A2 chamber, and half-slice generator.

  Quote anchors:

  ```text
  r_(p,q)(beta) = d_(p,q) exp[-3 C2(p,q)/beta] * (1 + lower-order terms).
  ```

  ```text
  H(x,y) = x y (x+y) / 2,
  Q(x,y) = x^2 + x y + y^2.
  ```

  ```text
  J - I -> beta^(-1) L,
  L = (1/3)(partial_xx - partial_xy + partial_yy),
  ```

- [NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md) for the fixed-weight derivative split and the formal `c_J`, `c_D` definitions.

  Quote anchors:

  ```text
  3 C2(p,q) / beta
    = Q(x,y) + 3(x+y) beta^(-1/2).
  ```

  ```text
  c_J = A_0 - A_1,
  ```

  ```text
  c_D = B_1/mu_1 - B_0/mu_0,
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12.md) for the derived leading virial equality and for the named corrected-Ward next step.

  Quote anchors:

  ```text
  A_i + B_i/mu_i = 3/2,
  c_J = c_D
  ```

  ```text
  The leading identity does not derive the `1/beta` subleading sign.
  ```

  ```text
  derive the corrected `T_beta = T_infty + beta^(-1/2) T_1 + beta^(-1) T_2 + ...` surface
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md) for the fenced finite-row warning that the strict margin is subleading.

  Quote anchor:

  ```text
  strict inequality lives ENTIRELY at the `1/beta` subleading order
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_DISCRIMINANT_CONJUGATION_RUNG_SEVENTEEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_DISCRIMINANT_CONJUGATION_RUNG_SEVENTEEN_BOUNDED_NOTE_2026-06-12.md) for the prior `T_delta` pointer and its retained stopping point.

  Quote anchor:

  ```text
  Both readings agree on the stopping point: after deriving `T_delta`, the proof needs a finite-band/diagonalization identity for the retained heat sandwich
  ```

Plain pointers, not proof inputs: W90's positive finite products and the MACHINERY solver.

## What Is New Here

Restated from W79/W86/W97:

```text
T_infty = S M_[H exp(-Q)] S,
S = exp(L/2),
H = x y (x+y)/2,
Q = x^2 + x y + y^2,
L = (1/3)(partial_xx - partial_xy + partial_yy),
A_i + B_i/mu_i = 3/2,
c_J = c_D
```

New here:

1. The retained saddle-surrogate scaled diagonal is expanded through `beta^(-1)`.
2. The six-neighbor heat side is expanded through its first nonleading term.
3. The resulting saddle-surrogate `T_1` and `T_2` are written explicitly.
4. The half-integer cancellation is tested at the source level and found not derivable from the supplied authorities: the `beta^(-1/2)` insertion is nonzero, swap-even, and mixed-degree.
5. The exact obstruction is named before the sign step: the first-correction Ward/eigenpair identity, plus the exact Wilson lower-order diagonal factors hidden by W79's `lower-order terms`.

## Corrected Saddle-Surrogate Operator

Set

```text
epsilon = beta^(-1/2),
u = x + y,
H = x y u / 2,
Q = x^2 + x y + y^2.
```

From the retained saddle diagonal

```text
r_sad_(p,q)(beta) = d_(p,q) exp[-3 C2(p,q)/beta],
d_(p,q) = (p+1)(q+1)(p+q+2)/2,
```

with `p = x sqrt(beta)` and `q = y sqrt(beta)`,

```text
beta^(-3/2) d_(p,q)
  = H + epsilon G_1 + epsilon^2 G_2 + O(epsilon^3),
G_1 = (u^2 + 2 x y)/2,
G_2 = 3u/2.
```

The exponent gives exactly

```text
3 C2(p,q)/beta = Q + 3u epsilon.
```

Therefore the saddle-surrogate diagonal multiplier has the exact retained expansion

```text
W_beta^sad = exp(-Q) [H + epsilon P_1 + epsilon^2 P_2 + O(epsilon^3)],
P_1 = G_1 - 3u H,
P_2 = G_2 - 3u G_1 + (9u^2/2) H.
```

The six-neighbor half-slice expansion gives

```text
beta/2 (J-I) = L/2 + beta^(-1) C_4 + O(beta^(-2)),
```

where

```text
C_4 =
  (1/72)(partial_xxxx + partial_yyyy)
  - (1/36)(partial_xxxy + partial_xyyy)
  + (1/24) partial_xxyy.
```

Let

```text
S = exp(L/2),
E_2 = integral_0^1 exp((1-t)L/2) C_4 exp(tL/2) dt.
```

Then the saddle-surrogate corrected operator is

```text
T_beta^sad = T_infty + epsilon T_1^sad + epsilon^2 T_2^sad + O(epsilon^3),
T_1^sad = S M_[exp(-Q) P_1] S,
T_2^sad = S M_[exp(-Q) P_2] S
        + E_2 M_[exp(-Q) H] S
        + S M_[exp(-Q) H] E_2.
```

Homogeneity bookkeeping:

```text
[D,L] = -2L,
[D,C_4] = -4C_4,
D[3u] = 3u,
P_1 has polynomial degrees 2 and 4,
P_2 has polynomial degrees 1, 3, and 5.
```

The mixed degrees in `P_1` and `P_2` matter. The corrected Ward identity is not a scalar-degree repeat of W97's leading identity.

## Exact Wilson Caveat

The expansion above is the explicit `r_sad` surface. W79's retained exact-Wilson statement is weaker:

```text
r_(p,q)(beta) = d_(p,q) exp[-3 C2(p,q)/beta] * (1 + lower-order terms).
```

No supplied authority gives those lower-order exact-Wilson factors through `epsilon^2`. If the missing factor is

```text
1 + epsilon a_1(x,y) + epsilon^2 a_2(x,y) + ...
```

then the exact Wilson-scaled multiplier would acquire extra terms

```text
epsilon a_1 H exp(-Q)
```

and

```text
epsilon^2 [a_2 H + a_1 P_1] exp(-Q).
```

Those terms are not derivable from the retained refs supplied here. This is a load-bearing obstruction, not a formatting gap.

## Half-Integer Term

The heat side contributes no `epsilon` term because the six-neighbor recurrence is paired under opposite shifts. The diagonal side does contribute the explicit saddle-surrogate insertion

```text
P_1 = (u^2 + 2xy)/2 - 3uH.
```

This insertion is swap-even:

```text
P_1(x,y) = P_1(y,x).
```

It is also nonzero. At `(x,y)=(1,2)`,

```text
P_1(1,2) = -41/2.
```

Therefore the diagram swap does not by itself cancel the `epsilon` contribution. It preserves the swap sectors. A cancellation of the `beta^(-1/2)` contribution to `c_J - c_D` would need a first-correction Ward identity or a direct perturbation identity for the top two eigenpairs of the corrected operator.

The finite W90 rows are consistent with a killed half-integer margin, but promoting that consistency to a derived cancellation would be value-from-target. This note does not claim deliverable (2) as derived.

## Subleading Sign

W97 derives the leading state-independent identity

```text
A_i + B_i/mu_i = 3/2.
```

For `T_beta^sad`, the next Ward calculation must include the nonhomogeneous insertion `P_1`, the `C_4` heat correction, and the first-order perturbation of the eigenvectors. The supplied authorities do not give an identity that reduces these state-dependent pieces to a sign-definite expression.

Outcome: obstruction-at-exact-step for the sign. The exact missing step is:

```text
derive a corrected first-order Ward/eigenpair identity for T_beta that proves
the beta^(-1/2) contribution to c_J - c_D cancels, then derive the
beta^(-1) coefficient as an exact-rational expression or a proven inequality.
```

Until that step is supplied, a positive `beta*(c_J-c_D)` witness cannot be upgraded into a proof.

## Fenced Witness Rows

The runner recomputes a small W90-style finite grid as a consistency witness. These rows are not proof inputs.

| beta | shell | `c_J - c_D` | `beta*(c_J-c_D)` |
|---:|---:|---:|---:|
| 30 | 21 | printed by runner | printed by runner |
| 60 | 28 | printed by runner | printed by runner |
| 120 | 37 | printed by runner | printed by runner |

They witness the same direction as W90. The derivation above does not use them to set a coefficient or sign.

## Falsifiers

The runner prints exact wrong-structure values:

| check | exact value |
|---|---:|
| leading virial constant | `3/2` |
| correct fixed-weight derivative at `(p,q,beta)=(10,20,100)` | `79/10` |
| wrong saddle correction `2(x+y)` at the same point | `38/5` |
| correct `P_1(1,2)` | `-41/2` |
| wrong `N_c=2` `P_1(1,2)` | `-23/2` |
| correct `P_2(1,2)` | `135/2` |
| wrong `N_c=2` `P_2(1,2)` | `39/2` |
| wrong dimension omitted `P_1(1,2)` | `-27` |
| wrong dimension omitted `P_2(1,2)` | `243/2` |
| swap check `P_1(1,2)-P_1(2,1)` | `0` |

These are falsifiers for normalization, `N_c=3`, dimension, and parity shortcuts. They are not spectral constants.

## Honest Outcome

Outcome: partial-with-named-missing-link.

Derived here:

```text
T_1^sad and T_2^sad for the retained saddle-surrogate operator,
the absence of a heat-side beta^(-1/2) term,
the nonzero swap-even structure of the diagonal beta^(-1/2) insertion,
the exact obstruction before the half-integer cancellation and sign step.
```

Not derived here:

```text
the exact Wilson T_1 and T_2 including lower-order diagonal factors,
the beta^(-1/2) cancellation in c_J - c_D,
the beta^(-1) coefficient of c_J - c_D,
the sign of that coefficient.
```

Both readings of the ambiguity:

Reading 1: saddle-surrogate reading. The explicit formulas above give `T_1^sad` and `T_2^sad`. Even on this reading, the first-correction Ward/eigenpair identity is not supplied, so the half-integer cancellation and the sign do not follow.

Reading 2: exact-Wilson reading. W79's `lower-order terms` can alter both `T_1` and `T_2`. On this reading, the corrected operator itself is not complete to order `1/beta`, so the sign calculation is blocked earlier.

The next path this opens is a source-side derivation of the exact Wilson lower-order diagonal factors or a Ward identity strong enough to show that those factors assemble into a state-independent cancellation.

## Differentiation From Prior Notes

Restated from W86/W79: the saddle profile, `Q + 3(x+y) beta^(-1/2)` fixed-weight derivative, and formal `c_J`, `c_D` definitions.

Restated from W97: the leading virial identity and leading equality `c_J = c_D`.

Restated from W90: finite rows point toward a positive subleading witnessed margin, fenced from the proof.

New here versus W97: the explicit saddle-surrogate `T_1^sad`, `T_2^sad`, and the reason swap parity does not derive the half-integer cancellation.

Scope: native discrete surface and retained reduced-A2 operator only. No continuum, no physical `beta=6`, no Clay or infinite-volume claim, and no audit outcome is asserted.

## No-Go Discipline Gate

Skill freshness: the repo `no-go-discipline` skill was checked against
`origin/main`, and the origin version was followed for this subleading
obstruction statement.

N1 - Alternative route enumeration:

1. Corrected Ward route. ATTEMPTED. It reaches explicit saddle-surrogate `T_1` and `T_2`, but the first-correction identity needed to cancel the half-integer term is not supplied by W97.
2. Swap route. ATTEMPTED. It does not derive cancellation because `P_1` is swap-even and nonzero.
3. Direct perturbation route. ATTEMPTED. It needs first-order eigenvector corrections and exact Wilson lower-order diagonal factors that the supplied authorities do not give.
4. Finite W90 promotion. ATTEMPTED as a fence check. Promoting the positive finite products to a sign proof would be value-from-target.
5. `T_delta` finite-band route. RULED OUT BY PRIOR W96 pointer for this step. It gives a conjugated surface but not a diagonalization identity for the retained heat sandwich.

N2 - Wall-independence audit:

The collapsed wall is one first-correction calculation. The missing exact Wilson diagonal factors and the missing first-correction eigenpair/Ward identity are components of that calculation; presenting them as independent final walls would overcount.

N3 - Hidden-wall scan:

`saddle-surrogate` is an explicit boundary, not a hidden admission. `finite witness` is non-load-bearing. `exact-Wilson reading` is a separate reading of the same obstruction and is not used as a proof input.

N4 - Residual matching:

| cited note | residual there | residual here | match |
|---|---|---|---|
| W86 | formal constants reduce to spectral quantities | corrected first-order quantities still need a spectral/Ward identity | yes |
| W90 | finite strict margin appears subleading | witness still fenced; sign not derived | yes |
| W96 | `T_delta` lacks finite-band/diagonalization identity | closed-form perturbation route still lacks eigenpair control | yes |
| W97 | leading equality derived; subleading sign not derived | this note advances `T_1^sad`, `T_2^sad` but stops before sign | yes |

N5 - Rhetoric audit:

The negative statement is source-local: this note does not derive the half-integer cancellation or the sign. It does not assert that the sign is false or inaccessible.

N6 - Partial-closure path scan:

Three partial paths remain live: derive exact Wilson `a_1,a_2`; prove a corrected Ward identity that cancels the `epsilon` term state-independently; or compute the first two corrected eigenpairs by direct retained-operator substitution. None is classified here as requiring a new axiom.

N7 - Steelman:

A hostile reviewer could derive a corrected Ward identity in which the mixed-degree `P_1` insertion, the diagonal derivative correction, and the eigenvector perturbation telescope after taking the difference between states `0` and `1`. W97 explicitly names this corrected-Ward route, and W86 supplies the exact fixed-weight derivative structure that could feed it. That is why this note ships as partial-with-named-missing-link instead of a stronger negative claim.

N8 - Cross-cycle echo:

W86 and W90 already located the same residual at the reduced spectral comparison. W96 moved the closed-form route to `T_delta` but did not supply the finite-band identity. W97 retired the leading equality residual. This note narrows the remaining residual to the first-correction Ward/eigenpair calculation and the exact Wilson lower-order diagonal factors.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_reduced_a2_subleading_sign_rung_nineteen_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=37, FAIL=0
```
