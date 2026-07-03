# Native Gauge Transfer Reduced-A2 Virial Leading Equality Rung Eighteen Bounded Note

**Date:** 2026-06-12

**Claim type:** bounded_theorem

**Boundary:** leading equality derived; subleading sign obstruction-at-exact-step. Claim type is a source-side boundary declaration, never an audit verdict.

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** [scripts/native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.py](../scripts/native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.txt)

No new axiom, literature value, external comparator number, fitted constant, rounded anchor, fitted prefactor, parity proxy, value-from-target step, or float-derived exact rational is used. W90 numerical rows are FENCES ONLY and not proof inputs.

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md) for the retained reduced operator, saddle multiplier, quadratic, and generator.

  Quote anchors:

  ```text
  H(x,y) = x y (x+y) / 2,
  ```

  ```text
  Q(x,y) = x^2 + x y + y^2.
  ```

  ```text
  J - I -> beta^(-1) L,
  ```

  ```text
  T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2).
  ```

- [NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md) for the formal spectral constants and the fixed-weight derivative split.

  Quote anchors:

  ```text
  c_J = A_0 - A_1,
  ```

  ```text
  c_D = B_1/mu_1 - B_0/mu_0
  ```

  ```text
  = Q(x,y) + 3(x+y) beta^(-1/2).
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md) for the fenced finite-row warning about where the strict margin appears.

  Quote anchor:

  ```text
  strict inequality lives at the `1/beta` subleading order
  ```

Plain pointers, not proof inputs: staged W96 for `T_delta` and the parity wall; W95 for the earlier discriminant-route target.

## What Is New Here

Restated from W86: the formal leading constants are

```text
c_J = A_0 - A_1,
A_i = <Phi_i, L Phi_i>,
c_D = B_1/mu_1 - B_0/mu_0,
B_i = <Phi_i, S_(1/2) M_[Q H exp(-Q)] S_(1/2) Phi_i>.
```

Restated from W90: finite rows point to leading equality and a positive subleading witnessed margin, but those rows are fences.

New here versus W96: closed-form eigenfunctions are not needed for the leading equality. The leading equality is forced by a dilation commutator for the retained heat-sandwich operator itself. W96's `T_delta` and parity wall remain relevant to constructive eigenfunctions and to any finite-band route, but they are not proof inputs for the identity below.

## Virial Identity

Let

```text
D = x partial_x + y partial_y,
W = H exp(-Q),
T = S_(1/2) M_W S_(1/2),
S_(1/2) = exp(L/2).
```

The retained polynomials are homogeneous:

```text
D H = 3 H,
D Q = 2 Q.
```

Therefore

```text
D W = (3 - 2Q) W.
```

The generator is homogeneous of degree `-2`:

```text
[D,L] = -2 L.
```

Since this commutator is a scalar multiple of `L`, it exponentiates without a Baker-Campbell-Hausdorff remainder:

```text
[D,S_(1/2)] = - L S_(1/2).
```

Thus the exact operator commutator is

```text
[D,T] = - L T - T L + S_(1/2) M_[(3 - 2Q) H exp(-Q)] S_(1/2).
```

For any reduced eigenpair in the W86 formal leading spectral reading,

```text
T Phi_i = mu_i Phi_i,
A_i = <Phi_i, L Phi_i>,
B_i = <Phi_i, S_(1/2) M_[Q H exp(-Q)] S_(1/2) Phi_i>,
```

taking the eigenstate expectation gives

```text
0 = <Phi_i, [D,T] Phi_i>
  = -2 mu_i A_i + 3 mu_i - 2 B_i.
```

So the state-independent virial relation is

```text
A_i + B_i/mu_i = 3/2.
```

The sign is the plus sign. The wrong signed combination is

```text
A_i - B_i/mu_i = 2 A_i - 3/2,
```

which is not state-independent unless a separate identity fixes every `A_i`.

## Leading Equality

The virial relation immediately gives

```text
A_0 + B_0/mu_0 = A_1 + B_1/mu_1 = 3/2.
```

Rearranging,

```text
A_0 - A_1 = B_1/mu_1 - B_0/mu_0.
```

Therefore

```text
c_J = c_D
```

at the retained leading reduced-A2 level. This is derived from the operator structure and does not use any W90 witness value.

## Finite Witnesses

The runner also solves deterministic saddle finite-block witnesses. It prints `A_i + B_i/mu_i` for the first three states at `beta = 100, 200, 400`; these are convergence checks, not proof inputs.

| beta | state 0 | state 1 | state 2 |
|---:|---:|---:|---:|
| 100 | `1.464854` | `1.454749` | `1.450800` |
| 200 | `1.482438` | `1.477406` | `1.475445` |
| 400 | `1.491222` | `1.488710` | `1.487732` |

The wrong combination remains separated on the same rows. At `beta = 400`, the runner prints approximately

```text
A_i - B_i/mu_i = -4.074133, -5.794714, -6.666694.
```

These rows witness the state-independent leading limit and falsify the wrong signed combination. They do not set any spectral constant.

## Falsifiers

The runner prints exact wrong-structure values:

| substitution | exact value |
|---|---:|
| retained virial constant | `3/2` |
| wrong signed sample, states `A=-1,-2` | `-7/2`, `-11/2` |
| wrong confiner `Q_wrong=x^2+2xy+y^2` but retained `Q` insertion, point `(1,2)` | `-12*exp(-9)` |
| correct `N_c=3` fixed-weight derivative sample `(p,q,beta)=(10,20,100)` | `79/10` |
| wrong `N_c=2` sample | `79/15` |
| wrong heat-generator normalization sample, evaluated with retained `A` | `5/2` |

The wrong confiner row is not a new operator proposal. It is a falsifier for the retained identity: if the middle multiplier is changed while the `Q` insertion is kept as in W86, the pointwise commutator clause no longer matches.

## Subleading Sign

The leading identity does not derive the `1/beta` subleading sign. The exact stopping step is the first corrected operator/eigenpair perturbation needed to sign the subleading coefficient.

The retained authorities supply the fixed-weight diagonal derivative expansion

```text
Q(x,y) + 3(x+y) beta^(-1/2),
```

but the sign of the strict margin also depends on the correction to the heat-sandwich operator and on the perturbation of the first two eigenvectors. Deriving the positive coefficient from W90 rows would be a value-from-target step, so this note stops before that sign claim.

The next path this opens is a source-side first-correction calculation for the scaled saddle operator: derive the corrected `T_beta = T_infty + beta^(-1/2) T_1 + beta^(-1) T_2 + ...` surface, then apply the virial commutator to that corrected perturbation without importing fitted coefficients.

## Two Readings

Reading 1: reduced-leading reading. The commutator identity proves the leading equality for any eigenstate of the retained reduced operator in the W86 formal spectral-pair setting.

Reading 2: finite-beta witness reading. W90 and the runner rows witness a positive strict margin in sampled finite problems, but those rows are fenced evidence. They do not prove the subleading sign coefficient.

## Honest Outcome

Outcome: leading equality derived; subleading sign obstruction-at-exact-step.

Derived here:

```text
A_i + B_i/mu_i = 3/2,
c_J = c_D
```

at leading reduced-A2 order.

Not derived here:

```text
the 1/beta subleading margin coefficient,
the sign of that coefficient,
closed-form Phi_i eigenfunctions,
a finite-band T_delta reduction.
```

## Differentiation From Prior Notes

Restated from W86: the `c_J`, `c_D`, `A_i`, `B_i`, `mu_i` definitions and the fixed-weight diagonal derivative expansion.

Restated from W90: the strict finite margin is witnessed as a subleading effect and remains fenced.

New here versus W96: the leading equality is derived without closed-form eigenfunctions and without a `T_delta` finite-band basis. W96's parity wall still blocks the closed-form eigenfunction route, but it does not block the dilation commutator.

New here versus W95: the discriminant route no longer has to supply the eigenfunctions to settle the leading equality; it remains a possible path for the subleading perturbation calculation.

## No-Go Discipline Gate

Skill freshness: the repo `no-go-discipline` skill was checked against
`origin/main`, and the origin version was followed for this subleading
obstruction statement.

N1 - Alternative route enumeration:

1. Virial/scaling route. ATTEMPTED. It succeeds for the leading identity, but its exact commutator is for `T_infty` and does not sign the first correction.
2. Hellmann-Feynman beta route. ATTEMPTED. W86 supplies the split and the `Q + 3(x+y) beta^(-1/2)` derivative term, but the sign also needs the corrected heat-sandwich operator and perturbed eigenvectors.
3. W90 finite-row promotion. ATTEMPTED as a fence check. Promoting the positive finite products to a derived coefficient would be a value-from-target step.
4. `T_delta` finite-band route. ATTEMPTED by prior W96 pointer. It gives the exact conjugated surface but not a finite-band diagonalization of the retained chamber-positive sandwich.
5. Low-degree closed-form eigenfunction route. RULED OUT BY PRIOR W96 pointer for low-degree closure; it does not supply the first-correction eigenpair perturbation.

N2 - Wall-independence audit:

Collapsed wall set: one wall remains for this note, the first corrected operator/eigenpair perturbation needed to sign the subleading coefficient. The diagonal subleading term, heat-sandwich correction, and eigenvector correction are components of that one perturbation calculation, not independent walls.

N3 - Hidden-wall scan:

The phrase "formal spectral-pair setting" is tied to W86's conditional reduced constants. The phrase "finite witnesses" is non-load-bearing. No phrase in the proof imports a standard external theorem as a proof step; the load-bearing algebra is the displayed commutator.

N4 - Residual matching:

| cited note | residual there | residual here | match |
|---|---|---|---|
| W86 | constants reduced to unknown spectral quantities | leading equality now derived; subleading perturbation not derived | yes |
| W90 | strict margin appears at subleading order in finite rows | subleading sign still not derived | yes |
| W96 | closed-form eigenfunctions / finite-band route not obtained | not needed for leading equality; still not available for subleading sign | yes |

N5 - Rhetoric audit:

The negative is source-local: this note does not derive the subleading coefficient. It does not assert that the coefficient is false, inaccessible, or lattice-wide undecidable.

N6 - Partial-closure path scan:

No new-axiom claim is made. The next path is an import-free perturbation calculation for the retained saddle operator. A convention or label reframe would not by itself provide the corrected operator/eigenpair perturbation.

N7 - Steelman:

A hostile reviewer could argue that the same dilation commutator extends to the corrected scaled operator if the `beta^(-1/2)` diagonal and heat corrections assemble into another homogeneous insertion. If that corrected Ward identity is derived, it may sign the subleading coefficient without closed-form eigenfunctions. The strongest support is W86's exact Hellmann split plus the retained fixed-weight derivative expansion.

N8 - Cross-cycle echo:

W86 and W90 named the same reduced spectral residual from different directions. W96 advanced the algebraic surface to `T_delta` but did not supply the subleading sign. This note retires the leading-equality residual and leaves the narrower first-correction residual.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=28, FAIL=0
```

Scope: native discrete surface and retained reduced-A2 operator only. No continuum, no physical `beta=6`, no Clay or infinite-volume claim, and no audit outcome is asserted.
