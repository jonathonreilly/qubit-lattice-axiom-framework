# Native Gauge Transfer Reduced-A2 Eigenvalue-Ratio eps-Cancellation Rung Twenty Bounded Note

**Date:** 2026-06-12

**Claim type:** bounded_theorem

**Boundary:** eps-cancellation DERIVED (eigenvalue-ratio object, lattice-exact); eps^2 sign has positive computed support; partial-with-named-missing-link for the fully a-priori sign. Claim type is a source-side boundary declaration, never an audit verdict.

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** [scripts/native_gauge_transfer_reduced_a2_eigenvalue_ratio_eps_cancellation_rung_twenty_bounded_2026_06_12.py](../scripts/native_gauge_transfer_reduced_a2_eigenvalue_ratio_eps_cancellation_rung_twenty_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_reduced_a2_eigenvalue_ratio_eps_cancellation_rung_twenty_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_reduced_a2_eigenvalue_ratio_eps_cancellation_rung_twenty_bounded_2026_06_12.txt)

No new axiom, literature value, external comparator number, fitted constant, rounded anchor, fitted prefactor, parity proxy, value-from-target step, or float-derived exact rational is used. W90 finite rows and every numerical coefficient in the runner are fenced cross-check witnesses only; they are not proof inputs for any derived statement.

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md) for the Hellmann split and the formal `c_J`, `c_D`, `A_i`, `B_i`, `mu_i` definitions.

  Quote anchors:

  ```text
  c_J = A_0 - A_1,
  ```

  ```text
  c_D = B_1/mu_1 - B_0/mu_0,
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12.md) for the leading equality and the reduced operator.

  Quote anchors:

  ```text
  A_i + B_i/mu_i = 3/2,
  ```

  ```text
  c_J = c_D
  ```

- [NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_UNIFORM_BESSEL_LOCAL_CLT_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md) for the scalar local-CLT atom (integer powers of `1/t`).

  Quote anchor:

  ```text
  P_1(a) = (a^4 - 6 a^2 + 3) / 24.
  ```

- [NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_WEYL_DETERMINANT_ASSEMBLY_RUNG_TEN_BOUNDED_NOTE_2026-06-12.md) for the determinant propagation of the scalar correction.

  Quote anchor:

  ```text
  Determinant multilinearity gives the finite algebraic expansion
  ```

- [NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md) for the retained saddle profile, generator, and chamber.

  Quote anchors:

  ```text
  H(x,y) = x y (x+y) / 2,
  Q(x,y) = x^2 + x y + y^2.
  ```

- [NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md) is a fenced witness pointer for the `1/beta` subleading scale (the `beta(c_J-c_D) -> ~1.66` cross-check).

  Quote anchor:

  ```text
  strict inequality lives ENTIRELY at the `1/beta` subleading order
  ```

## What Is New Here

The native half-line transfer operator is `T(beta) = exp((beta/2) J) D_beta exp((beta/2) J)` on the su(3) dominant-weight lattice; `lambda_0 > lambda_1` are its top two eigenvalues. The campaign asks for the SIGN of the `1/beta` subleading margin of the gap, after the leading equality `c_J = c_D` (RUNG_EIGHTEEN). This note:

1. Identifies the CORRECT object for the margin: the eigenvalue ratio. With `Lambda(beta) = log(lambda_1/lambda_0)`, the finite-`beta` Hellmann margin is

   ```text
   c_J(beta) - c_D(beta) = -beta d/dbeta Lambda(beta).
   ```

2. DERIVES the `eps`-cancellation (`eps = beta^(-1/2)`): the `beta^(-1/2)` coefficient of `Lambda` vanishes, so the margin starts at `1/beta` (no half-integer term).

3. Records the corrected first-correction structure (translation conjugation `T_1 = [R, T_0]`) and the `P_2` reduction.

4. Records positive computed support for the `eps^2` sign `a_2 > 0` (so the gap ratio decreases / the margin is positive), resting on two computed spectral facts (`a_2^heat`, `a_2^LC`), with the fully a-priori sign named as the remaining link.

## The Reduced Operator And The Correct Object

The reduced (leading) operator is

```text
T_0 = S M_[H exp(-Q)] S,  S = exp(L/2),
L = (1/3)(partial_xx - partial_xy + partial_yy),
H = x y (x+y)/2,  Q = x^2 + x y + y^2,  u = x + y.
```

Its scaled corrections (RUNG_NINE/saddle + RUNG_TEN local-CLT) give `T_beta = T_0 + eps T_1 + eps^2 T_2 + O(eps^3)` with the first polynomial `P_1 = (u^2 + 2xy)/2 - 3uH` and `T_1 = S M_[P_1 exp(-Q)] S`.

The leading equality `c_J = c_D` (RUNG_EIGHTEEN) makes the leading `1/beta` coefficient of `Delta_J + Delta_D = d/dbeta Lambda` vanish, so the margin sits at the next order. The correct object for that next order is the eigenvalue ratio `Lambda`, not a static expectation: `c_J(beta) - c_D(beta) = -beta d/dbeta Lambda(beta)` by the Hellmann split.

## eps-Cancellation (Derived)

**The first correction is an infinitesimal translation conjugation.** With `R = partial_x + partial_y`:

```text
R H = (u^2 + 2xy)/2,   R Q = 3u,
R[H exp(-Q)] = (R H - 3u H) exp(-Q) = P_1 exp(-Q),
[R, L] = 0   (constant-coefficient operators)  =>  [R, S] = 0.
```

Therefore

```text
T_1 = S M_[P_1 exp(-Q)] S = S M_[R(H exp(-Q))] S = [R, T_0].
```

**First-order eigenvalue shift vanishes.** For any simple eigenpair `T_0 Phi_i = mu_i Phi_i` of the self-adjoint `T_0`,

```text
mu_i^(1) = <Phi_i | T_1 | Phi_i> = <Phi_i | [R, T_0] | Phi_i>
         = mu_i <Phi_i|R|Phi_i> - mu_i <Phi_i|R|Phi_i> = 0.
```

This is **lattice-exact with no boundary assumption**: for the finite lattice matrix `T_0` (symmetric) and ANY matrix `C` representing `R`, `<v | [C, T_0] | v> = 0` for every eigenvector `v` of `T_0`, by the same one-line identity. (The runner verifies this on a random symmetric matrix and a random `C`.)

**The ratio cancellation.** Expanding `lambda_i(eps) = mu_i + eps mu_i^(1) + eps^2 mu_i^(2) + ...`,

```text
coeff_eps( Lambda ) = coeff_eps( log(lambda_1/lambda_0) ) = mu_1^(1)/mu_1 - mu_0^(1)/mu_0
```

exactly. With `mu_i^(1) = 0` this is `0`, so `Lambda` has no `beta^(-1/2)` term and the margin `c_J - c_D = -beta d/dbeta Lambda` starts at `1/beta`. The necessary-and-sufficient condition for the cancellation is the WEAKER statement that `mu_i^(1)/mu_i` is state-independent; `mu_i^(1) = 0` each-state suffices.

**Exact-Wilson witness.** Built on the exact-Wilson recurrence (Bessel/Weyl determinant; native discrete, no continuum), `Lambda(beta)` over `beta in {60,90,120,150,200}` fits `Lambda = L_inf + b beta^(-1/2) + a_2 beta^(-1) + a_3 beta^(-3/2)` with `b` consistent with `0` (`|b| < 0.02`, about four orders below `a_2`) and `a_2 ~ 1.67` (force-`b=0` gives `a_2 ~ 1.67`). The fuller campaign sweep to `beta = 500` gives `b ~ 6.6e-5` and `a_2 = 1.663`, matching the RUNG_ELEVEN/W90 cross-check `beta(c_J-c_D) -> ~1.66`. These are fenced witnesses, not proof inputs.

## eps^2 Sign

The `1/beta` coefficient of `Lambda` is `a_2 = mu_1^(2)/mu_1 - mu_0^(2)/mu_0`, the second-order eigenvalue-perturbation difference. Using the standard Rayleigh-Schrodinger second order with `T_1 = [R, T_0]` (which simplifies the off-diagonal sum, since `<Phi_k|T_1|Phi_i> = (mu_i - mu_k)<Phi_k|R|Phi_i>`) and `C_4 = (1/8) L^2` (the heat correction identity), `a_2` decomposes as

```text
a_2 = a_2^heat + a_2^LC,
a_2^heat = (1/4)(||L Phi_1||^2 - ||L Phi_0||^2),
a_2^LC   = (the W87/W88 local-CLT-weighted spatial-average difference).
```

`a_2^heat` is a difference of `L`-Dirichlet energies of the top two reduced eigenstates; it is positive in the computed reduced surface because the first-excited reduced state `Phi_1` is more `L`-curved than the Perron state `Phi_0` (`||L Phi_1||^2 > ||L Phi_0||^2`, computed and grid-stable; the runner witnesses `a_2^heat ~ 1.0 > 0`). `a_2^LC` is a genuine moment of the indefinite local-CLT function and is positive by computation (`~ +0.85`, grid-stable; campaign value), its sign not forcible from positivity alone. Thus the computed reduced surface supports `a_2 > 0`, with the sign resting on `a_2^heat > 0` (near-analytic) AND `a_2^LC > 0` (computational). The exact-Wilson `a_2 ~ 1.66` is the fenced cross-check.

## Differentiation From The Superseded First-Correction Attempt

A prior (un-landed) first-correction attempt routed the cancellation through the STATIC virial defect `A_i + B_i/mu_i` of the corrected reduced operator, claiming `coeff_eps(A_i + B_i/mu_i) = -mu_i^(1)/(2 mu_i) = 0`. That is the wrong object. The static virial defect's `eps`-coefficient carries an additional term from the translation of the `Q`-insertion:

```text
R(Q H exp(-Q)) = (3u H + Q P_1) exp(-Q),
```

so `B_i` (which contains the `Q`-insertion) is NOT translation-invariant, even though `A_i = <Phi_i|L|Phi_i>` is (`[R, L] = 0`). The dropped `3u H exp(-Q)` term is nonzero and state-dependent (`3u H = 27` at `(x,y) = (1,2)`), so `coeff_eps(A_i + B_i/mu_i)` does not vanish and the static virial defect does not have a zero `eps` slope. The eigenvalue-ratio object used here is the correct one; the cancellation follows from `mu_i^(1) = 0` applied to the eigenvalues, not to the static defect. (The runner verifies the `R(Q H exp(-Q))` identity and the nonzero dropped term.)

## Falsifiers

| check | value |
|---|---:|
| `P_1(1,2)` | `-41/2` |
| `P_2(1,2)` | `135/2` |
| dropped translation-of-Q term `3u H` at `(1,2)` | `27` (nonzero) |
| A1 (`N_c=2`) discriminant degree | `1` (vs A2 cubic `2H` degree `3`) |
| `<v|[C,T_0]|v>` for eigenvector of symmetric `T_0` | `~1e-15` (lattice-exact) |
| exact-Wilson `b` (`beta^(-1/2)` coeff of `Lambda`) | `~0` (`<0.02`) |
| exact-Wilson `a_2` | `~1.67` (in `(1.55,1.75)`, positive) |

These show `N_c=3`, the cubic discriminant structure, and the eigenvalue-ratio object are load-bearing.

## Honest Outcome

Outcome: eps-cancellation DERIVED; eps^2 sign positive as computed support; partial-with-named-missing-link for the fully a-priori sign.

Derived here:

```text
T_1 = [R, T_0],  mu_i^(1) = 0  (lattice-exact),
coeff_eps( log(lambda_1/lambda_0) ) = mu_1^(1)/mu_1 - mu_0^(1)/mu_0 = 0,
so the gap-ratio margin c_J - c_D = -beta d/dbeta log(lambda_1/lambda_0) starts at 1/beta.
```

Computationally supported here (sign), not a-priori derived:

```text
a_2 = a_2^heat + a_2^LC > 0,
a_2^heat = (1/4)(||L Phi_1||^2 - ||L Phi_0||^2) > 0  (near-analytic Dirichlet-energy difference),
a_2^LC > 0  (computed local-CLT moment).
```

Not derived here:

```text
a fully a-priori proof of ||L Phi_1||^2 > ||L Phi_0||^2 (a nodal/oscillation argument on T_0),
a fully a-priori proof of a_2^LC > 0,
the exact a_2 value from the reduced operator (the reduced estimate a_2^heat + a_2^LC ~ 1.0 + 0.85
  ~ 1.85 overshoots the exact-Wilson ~1.66, so the reduced-operator second-order model captures the
  SIGN, not the value),
continuum / physical beta=6 / infinite-volume transfer.
```

The next path this opens is an a-priori nodal/oscillation argument for `||L Phi_1||^2 > ||L Phi_0||^2` and a sign argument for `a_2^LC`, plus reconciling the reduced-operator second-order value with the exact-Wilson `a_2`.

## Two Readings

Reading 1: eigenvalue-ratio (correct object). `c_J - c_D = -beta d/dbeta log(lambda_1/lambda_0)`; the `eps`-cancellation is `coeff_eps(Lambda) = 0` from `mu_i^(1) = 0`; the `eps^2` margin is `a_2 = mu_1^(2)/mu_1 - mu_0^(2)/mu_0 > 0`.

Reading 2: static virial defect (incorrect object, recorded for differentiation). The defect `A_i + B_i/mu_i` has a nonzero state-dependent `eps`-coefficient from the `Q`-insertion translation, so it does not deliver the cancellation; it is not the finite-`beta` margin.

Both readings agree the leading equality is `3/2`-virial (RUNG_EIGHTEEN) and that `mu_i^(1) = 0` from `T_1 = [R, T_0]`; they differ on which object carries the subleading margin.

## No-Go Discipline Gate

Skill freshness: the repo `no-go-discipline` skill was checked against
`origin/main`, and the origin version was followed for this subleading
sign-boundary statement.

N1 - Alternative route enumeration:

1. Eigenvalue-ratio route. ATTEMPTED. Succeeds for the `eps`-cancellation (`mu_i^(1)=0`, lattice-exact) and gives the computed `eps^2` sign decomposition.
2. Static-virial-defect route. ATTEMPTED. Rejected: wrong object (nonzero `eps`-slope from the `Q`-insertion translation).
3. Second-order RS sign. ATTEMPTED. `a_2^heat` near-analytic positive; `a_2^LC` positive by computation.
4. Exact-Wilson recurrence. ATTEMPTED as witness. Confirms `b ~ 0` and `a_2 ~ 1.66`, fenced.
5. Fully a-priori `||L Phi_1||^2 > ||L Phi_0||^2`. NOT supplied (named open).

N2 - Wall-independence audit:

The `eps`-cancellation is fully closed (one derived statement). The remaining wall is one object: an a-priori sign of `a_2` (its two computed pieces `a_2^heat`, `a_2^LC`), plus reconciling the reduced/exact-Wilson `a_2` value.

N3 - Hidden-wall scan:

"Reduced operator", "eigenvalue ratio", and "lattice-exact" are tied to the authorities and to the runner identities. No appeal to a standard external theorem is used as a proof step; the load-bearing algebra is the displayed commutator and ratio expansion.

N4 - Residual matching:

| cited note | residual there | residual here | match |
|---|---|---|---|
| RUNG_NINE/EIGHTEEN | subleading sign open after leading equality | `eps`-cancellation derived; sign positive (computed) | yes |
| RUNG_TEN | local-CLT atom / determinant propagation | used for `a_1=0` and `a_2^LC` | yes |
| RUNG_ELEVEN/W90 | finite positive `1/beta` margin | reproduced as fenced witness `a_2 ~ 1.66` | yes |

N5 - Rhetoric audit:

The negative is source-local: the fully a-priori `eps^2` sign and the exact `a_2` value are not derived here. No impossibility, continuum, or lattice-wide claim is made.

N6 - Partial-closure path scan:

Live paths: an a-priori nodal/oscillation proof of `||L Phi_1||^2 > ||L Phi_0||^2`; an `a_2^LC` sign argument; reconciliation of the reduced-operator and exact-Wilson `a_2`. None is classified as requiring a new axiom.

N7 - Steelman:

A reviewer could argue the reduced-operator second-order value overshoot (`a_2^heat + a_2^LC ~ 1.0 + 0.85 ~ 1.85` vs exact-Wilson `~1.66`) signals a missing `T_2` contribution; this note treats the reduced second order as capturing the SIGN only and fences the exact value to the exact-Wilson witness, so the overshoot is disclosed, not hidden.

N8 - Cross-cycle echo:

RUNG_EIGHTEEN retired the leading-equality residual. This note retires the `eps`-cancellation residual (for the correct eigenvalue-ratio object) and narrows the remaining residual to the a-priori `eps^2` sign.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_reduced_a2_eigenvalue_ratio_eps_cancellation_rung_twenty_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=22, FAIL=0
```

Scope: native discrete surface and the retained reduced-A2 operator only. No continuum limit, no physical `beta=6`, no Clay or infinite-volume Yang-Mills claim, and no audit outcome is asserted.
