# Native Gauge Transfer Reduced-A2 Discriminant Conjugation Rung Seventeen Bounded Note

**Date:** 2026-06-12

**Claim type:** open_gate
**Type:** source-side obstruction note

**Claim boundary:** this note records a partial attempt with a named missing link at the reduced spectral step. The claim type is a source-side boundary declaration, never an audit verdict.

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** [scripts/native_gauge_transfer_reduced_a2_discriminant_conjugation_rung_seventeen_bounded_2026_06_12.py](../scripts/native_gauge_transfer_reduced_a2_discriminant_conjugation_rung_seventeen_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_reduced_a2_discriminant_conjugation_rung_seventeen_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_reduced_a2_discriminant_conjugation_rung_seventeen_bounded_2026_06_12.txt)

No new axiom, literature value, external comparator number, fitted constant, rounded anchor, fitted prefactor, parity proxy, or value-from-target step is used. Rung eleven's finite rows remain fences and consistency witnesses, not proof inputs. All exact constants below are integer polynomial coefficients or the retained rational normalizations already present in the reduced operator.

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md) for the retained saddle multiplier, generator, and chamber.

  Quote anchors:

  ```text
  H(x,y) = x y (x+y) / 2
  ```

  ```text
  Q(x,y) = x^2 + x y + y^2.
  ```

  ```text
  on the scaled A2 dominant chamber.
  ```

- [NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md) for the reduced heat-sandwich operator and the spectral-constant definitions.

  Quote anchors:

  ```text
  T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2).
  ```

  ```text
  c_D = B_1/mu_1 - B_0/mu_0
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md) for the finite-row warning about the subleading margin.

  Quote anchor:

  ```text
  strict inequality lives at the `1/beta` subleading order
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_CLOSED_FORM_RUNG_SIXTEEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_CLOSED_FORM_RUNG_SIXTEEN_BOUNDED_NOTE_2026-06-12.md) for the named N7 route pursued here.

  Quote anchor:

  ```text
  boundary factor `H` may be exactly the Weyl-chamber ground-state density
  ```

## What Is New Here

Restated from rungs nine and eleven: the reduced object is

```text
T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2),
S_t = exp(t L),
L = (1/3)(partial_xx - partial_xy + partial_yy),
H = x y (x+y) / 2,
Q = x^2 + x y + y^2,
```

on the retained chamber `x,y >= 0`.

New here versus rung sixteen: rung sixteen named the discriminant route as a steelman but did not derive the discriminant, the antisymmetrization parity issue, or the conjugated operator. This note derives:

```text
delta = x y (x+y),        H = delta / 2,
```

and the exact Doob-conjugated heat-sandwich operator acting on `g = Phi/delta`:

```text
T_delta = exp(L_delta/2) M_[H exp(-Q)] exp(L_delta/2).
```

The derivation stops at a named missing identity: the missing identity is a finite-band or diagonalization identity for `T_delta`. The chamber-positive multiplier is `|delta|/2`, not signed `delta/2`, after full-plane antisymmetrization. Without a proof that this retained heat-sandwich operator is diagonalized by a constructive basis, no closed-form spectral constants are derived here.

## Discriminant Identification

The retained positive roots in the chamber coordinates are

```text
x, y, x+y.
```

Their product is

```text
delta = x y (x+y),
```

so the retained multiplier is exactly

```text
H = delta / 2.
```

Use the wall reflections

```text
s_x(x,y) = (-x, x+y),
s_y(x,y) = (x+y, -y),
s_{x+y}(x,y) = (-y, -x).
```

Each preserves `Q`, and each flips `delta`. A polynomial anti-invariant under the first two wall reflections must vanish on `x=0` and `y=0`; applying the third wall gives the factor `x+y`. Therefore every polynomial anti-invariant has the factor `delta`. In degree below 3 the anti-invariant space is zero; in degree 3 it is one-dimensional and spanned by `delta`. This proves the requested uniqueness up to scale in the polynomial/Gaussian class used for the direct-substitution route.

The coordinate swap `x <-> y` is a diagram-swap pointer, not the wall-reflection sign test. It leaves `xy(x+y)` unchanged. That is a useful ambiguity check: a proof that needs `x <-> y` or `v -> -v` to flip this retained `delta` is proving a different sign convention.

In `u = x+y`, `v = x-y`, the retained objects are

```text
H = u (u^2 - v^2) / 8,
Q = (3 u^2 + v^2) / 4,
L = (1/3) partial_uu + partial_vv.
```

## Antisymmetrization And Conjugation

For smooth Weyl-anti-invariant full-plane functions in this chamber problem, write

```text
Phi = delta * g,
```

with `g` Weyl-invariant in the polynomial/Gaussian class. The exact local generator conjugation uses `L delta = 0`:

```text
L(delta g) = delta L_delta g,
```

where

```text
L_delta g = L g + ((2 delta_x - delta_y)/(3 delta)) partial_x g
              + ((-delta_x + 2 delta_y)/(3 delta)) partial_y g.
```

Equivalently,

```text
L_delta g =
  (1/3) partial_uu g + partial_vv g
  + [2(3u^2 - v^2)/(3u(u^2-v^2))] partial_u g
  - [4v/(u^2-v^2)] partial_v g.
```

Thus the exact chamber-side conjugated spectral equation is

```text
T_delta g = mu g,
T_delta = exp(L_delta/2) M_[H exp(-Q)] exp(L_delta/2).
```

This is the load-bearing conjugation rung sixteen only named. It does not turn the retained sandwich into the bare Dunkl/Calogero heat semigroup. The multiplier `H exp(-Q)` remains inside the sandwich.

The full-plane parity accounting is the obstruction to using signed-polynomial heat algebra as the proof. If an anti-invariant function is represented as `Phi = delta g`, then multiplying by signed `delta` maps it into a Weyl-invariant parity sector. The chamber operator instead multiplies by the positive chamber value of `H`; after antisymmetric full-plane extension that multiplier is `|delta|/2`. This preserves the anti-invariant sector, but it is not the signed polynomial `delta/2`.

Therefore a signed full-plane computation with `M_[delta exp(-Q)/2]` solves a parity-changed operator. The retained object requires either a direct chamber proof or a new identity for the `|delta|`/`T_delta` heat sandwich.

## Noncommutation Check

The reduced object is a heat semigroup sandwich. It is not the bare conjugated generator. The commutator is already nonzero on `1`:

```text
exp(Q) [L, M_[H exp(-Q)]] 1
  = x y (x+y) (x^2 + x y + y^2 - 4) / 2.
```

At `(x,y)=(1,2)`, this gives

```text
[L, M_[H exp(-Q)]] 1 = 9*exp(-7).
```

This is why the generalized-Hermite or Dunkl generator basis is not a proof of the retained sandwich spectrum without the missing finite-band or diagonalization identity for `T_delta`.

## Falsifiers

The runner prints these exact values:

| check | value |
|---|---:|
| `delta(1,2)` | `6` |
| `delta(s_x(1,2))` | `-6` |
| `delta(swap(1,2))` | `6` |
| signed `delta * anti` at `(1,2)` and `s_x(1,2)` | `36`, `36` |
| `|delta| * anti` at `(1,2)` and `s_x(1,2)` | `36`, `-36` |
| B2-style degree-4 product at `(1,2)` | `30` |
| G2-style degree-6 product at `(1,2)` | `1680` |
| A1 single-root product at `(1,2)` | `1` |
| correct `L(u^2+v^2)` | `8/3` |
| raw unnormalized second-difference value | `8` |
| commutator value at `(1,2)` | `9*exp(-7)` |

These are wrong-structure substitutions. They are not used to set a spectral constant.

## Honest Outcome

Outcome: partial-with-named-missing-link at the exact spectral step.

Derived here:

```text
H = delta/2,
delta = x y (x+y),
```

the degree-three anti-invariant uniqueness, the chamber/full-plane parity distinction, and the exact conjugated operator `T_delta`.

Not derived here:

```text
Phi_0, Phi_1, mu_0, mu_1,
A_0, A_1, B_0, B_1,
c_J, c_D,
c_J = c_D,
the 1/beta subleading margin coefficient or its sign.
```

No closed-form `Phi_0`, `Phi_1`, `mu_i`, `A_i`, `B_i`, `c_J`, `c_D`, or subleading margin coefficient is derived here. The next path this opens is to prove a retained finite-band/diagonalization identity for `T_delta`, or to derive the first two chamber eigenpairs by direct substitution into the actual heat-sandwich operator.

## Two Readings

Reading 1: signed-polynomial full-plane reading. This makes `H exp(-Q) = delta exp(-Q)/2` polynomial, but it changes Weyl parity inside the sandwich: signed `delta` maps anti-invariant input to invariant middle data. This reading does not prove the retained chamber operator.

Reading 2: chamber-positive Dirichlet reading. This is the retained object. The full-plane multiplier is `|delta| exp(-Q)/2`, and the quotient equation is the exact `T_delta` equation above. This reading keeps the operator fixed, but the constructive spectrum is not obtained here.

Both readings agree on the stopping point: after deriving `T_delta`, the proof needs a finite-band/diagonalization identity for the retained heat sandwich, or explicit eigenfunctions checked by direct substitution into that same operator.

## Differentiation From Prior Notes

Restated from rungs nine and eleven: the block-Hellmann definitions of `c_J` and `c_D`, the reduced operator `T_infty`, and the finite-row warning that the strict margin is subleading.

Restated from rung sixteen: the discriminant route was named as a steelman target.

New here versus rung sixteen: `H=delta/2` is proved as the A2 discriminant, the degree-three anti-invariant uniqueness is checked, the signed-versus-positive full-plane parity issue is isolated, `[L,M] != 0` is printed exactly, and the conjugated operator `T_delta` is derived explicitly.

## No-Go Discipline Gate

Skill freshness: `docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` and the current `no-go-discipline` skill were read and followed for this bounded source note.

N1 - Alternative route enumeration:

1. Discriminant identification. ATTEMPTED. It succeeds: `H=delta/2` with `delta=xy(x+y)`.
2. Signed full-plane polynomial route. ATTEMPTED. It changes Weyl parity in the middle of the sandwich, so it is not the retained chamber operator.
3. Delta-Doob conjugation route. ATTEMPTED. It succeeds through `T_delta`, but leaves the same positive discriminant multiplier inside the heat sandwich.
4. Naive generalized-Hermite route. ATTEMPTED. The nonzero commutator and the remaining `M_[H exp(-Q)]` sandwich block promotion to a generator eigenbasis proof.
5. Rung-eleven finite-row promotion. ATTEMPTED as a fence check. Promoting those rows to constants would be value-from-target, so they are not proof inputs.

N2 - Wall-independence audit:

The collapsed wall is one missing identity: diagonalize or finite-band reduce the retained `T_delta` heat sandwich. The parity issue and nonzero commutator are not separate final walls; they explain why the common shortcut does not supply that identity.

N3 - Hidden-wall scan:

The phrases "retained object", "chamber-positive", and "heat sandwich" are tied to the one-hop authorities above. The phrase "Weyl-invariant" is used for the explicit reflection action displayed in this note, not as an external theorem.

N4 - Residual matching:

| cited note | residual there | residual here | match |
|---|---|---|---|
| rung nine | reduced spectral constants not derived | same spectral pair remains missing after conjugation | yes |
| rung eleven | finite rows cannot settle subleading sign | finite rows remain fenced | yes |
| rung sixteen | product/separable route did not derive eigenpairs | discriminant route now reaches `T_delta` then stops | yes |

N5 - Rhetoric audit:

The negative statement is source-local: this note does not derive the eigenpairs or constants. It does not assert that the eigenpairs cannot be derived, and it does not make a lattice-wide or continuum claim.

N6 - Partial-closure path scan:

Two next paths remain live. One is an exact finite-band or diagonalization identity for `T_delta`. The other is a direct chamber substitution proof for explicit `Phi_0` and `Phi_1`. Neither is classified here as requiring a new axiom.

N7 - Steelman:

A hostile reviewer could argue that the `delta`-Doob transform is already the right variable, and that `M_[H exp(-Q)]` becomes a tractable multiplication operator in a non-polynomial invariant coordinate such as the positive square root of the discriminant square. If that identity is derived on the retained chamber, the present obstruction would turn into a constructive spectral calculation. The strongest source-side support is rung sixteen's N7 pointer that the boundary factor may be the Weyl-chamber ground-state density.

N8 - Cross-cycle echo:

Rung nine and rung eleven named the same reduced spectral step from different sides: rung nine through formal constants, rung eleven through finite rows and the subleading margin. This note advances the algebraic surface to `T_delta`; it does not retire the reduced spectral step.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_reduced_a2_discriminant_conjugation_rung_seventeen_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=29, FAIL=0
```

Scope: native discrete surface and the retained reduced-A2 operator only. No continuum limit, no physical `beta=6`, no Clay or infinite-volume Yang-Mills claim, and no audit outcome is asserted.
