# Native Gauge Transfer Diagonal Domination Obstruction Note

**Date:** 2026-06-12
**Claim type:** open_gate
**Type:** source-side obstruction note

Status authority: independent audit lane only. This source note does not set or predict an audit outcome.

**Primary runner:** [scripts/native_gauge_transfer_diagonal_domination_rung_nine_bounded_2026_06_12.py](../scripts/native_gauge_transfer_diagonal_domination_rung_nine_bounded_2026_06_12.py)

**Runner cache:** [logs/runner-cache/native_gauge_transfer_diagonal_domination_rung_nine_bounded_2026_06_12.txt](../logs/runner-cache/native_gauge_transfer_diagonal_domination_rung_nine_bounded_2026_06_12.txt)

No literature value, new axiom, external citation, fitted selector, fitted
prefactor, or new comparator number is used. The finite trend rows below are
witnesses only. They are not proof inputs for the large-beta constants.

## One-Hop Authorities

- [NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)
  for the exact finite-block split and the named H8-D target.

  Quote anchor:

  ```text
  Thus the derivative inequality is exactly equivalent, on the finite block, to
  ```

  ```text
  Delta_J + Delta_D <= 0
  Delta_J = <v_1, J v_1> - <v_0, J v_0>
  Delta_D = <v_1, E_beta D_beta' E_beta v_1>/lambda_1
            - <v_0, E_beta D_beta' E_beta v_0>/lambda_0.
  ```

- [NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_OPERATOR_NORM_REMAINDER_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md)
  for the scaled saddle diagonal, the half-slice semigroup surface, and the
  already named exact-Wilson-to-saddle wall.

  Quote anchors:

  ```text
  beta^(-3/2) r_(p,q)(beta)
      -> H(x,y) exp[-Q(x,y)],
  H(x,y) = x y (x+y) / 2,
  Q(x,y) = x^2 + x y + y^2.
  ```

  ```text
  E_beta = exp((beta/2)(J - I)).
  ```

- [GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md)
  for the source character and exact six-neighbor recurrence.

  Quote anchor:

  ```text
  X(W) = (1/3) Re Tr W = (chi_(1,0)(W) + chi_(0,1)(W)) / 6.
  ```

- [NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md](NATIVE_GAUGE_TRANSFER_WILSON_TO_SADDLE_UNIFORM_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md)
  for the sharpened value-side localization of the exact-Wilson-to-saddle
  wall.

  Quote anchor:

  ```text
  No source-side value of K_W(a) is derived in this note.
  ```

## What Is New Here

The block-Hellmann rung-eight note already supplied the finite Hellmann split
and witnessed that `Delta_D` is positive while `Delta_J` is negative on the
sampled post-peak grid. The operator-remainder rung-eight note already
supplied the saddle profile and half-slice semigroup surface. This note adds
the derivative-side saddle reduction:

```text
r_sad_(p,q)(beta) = d_(p,q) exp[-3 C2(p,q)/beta],
d_(p,q) = (p+1)(q+1)(p+q+2)/2,
C2(p,q) = (p^2 + q^2 + p q + 3p + 3q)/3.
```

At fixed integer weight `(p,q)`,

```text
beta * r_sad_(p,q)'(beta) / r_sad_(p,q)(beta)
  = 3 C2(p,q) / beta.
```

This identity is taken in the FIXED-INTEGER-WEIGHT sense: the SU(3)
dimension prefactor `d_(p,q)` is `beta`-independent and contributes
zero to `r_sad'/r_sad`, so only the exponent `-3 C2(p,q)/beta` is
differentiated. (This is distinct from differentiating the
`a`-fixed-prefactor profile `r ~ beta^(3/2) H(a) exp(-Q(a))`, which
would instead give the prefactor scaling `3/2`; that operation is NOT
used here. The subleading `3(x+y) beta^(-1/2)` term displayed below is
the fixed-weight signature.)

With `x = p / sqrt(beta)` and `y = q / sqrt(beta)`, this becomes

```text
3 C2(p,q) / beta
  = Q(x,y) + 3(x+y) beta^(-1/2).
```

Therefore the leading diagonal-derivative multiplier supplied by the saddle
profile is `Q(x,y) / beta`. This is a derived saddle identity, not a fit to
the measured `Delta_D` rows.

Combining that with the internally checked six-neighbor Taylor generator gives
the formal large-beta constant expressions, conditional on a limiting isolated
spectral pair `(mu_i, Phi_i)` of the reduced operator

```text
T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2).
```

The formal constants are

```text
c_J = A_0 - A_1,
A_i = <Phi_i, L Phi_i>,
L = (1/3)(partial_xx - partial_xy + partial_yy),
```

and

```text
c_D = B_1/mu_1 - B_0/mu_0,
B_i = <Phi_i, S_(1/2) M_[Q H exp(-Q)] S_(1/2) Phi_i>.
```

Under this reading,

```text
Delta_J ~ -c_J / beta,
Delta_D ~  c_D / beta.
```

The requested domination would require `c_D <= c_J` plus a uniform subleading
bound. The authorities above do not supply closed-form `Phi_i`, a proven
inequality comparing the two Rayleigh quotients, or a uniform exact-Wilson
remainder that transfers this saddle statement back to `r_(p,q)(beta)`.

## Honest Outcome

Outcome: obstruction-at-exact-step.

The exact obstruction is not the finite Hellmann split and not the saddle
diagonal derivative. Those are available. The obstruction is the next analytic
step:

```text
derive or bound c_D <= c_J for the reduced spectral pair, then transfer it to
the exact Wilson diagonal with explicit active-window and tail remainders.
```

Reporting numerical values for `beta*(-Delta_J)` and `beta*Delta_D` does not
derive `c_J` or `c_D`. Those witnesses are still useful because they locate the
margin, but using them as fitted constants would be a value-from-target step.

## Two Readings Of The Ambiguity

Reading 1: formal saddle-spectrum reading. The equations above identify
`c_J` and `c_D` as reduced-operator spectral quantities. This is the strongest
available analytic reading, but it stops at unknown eigenfunctions and an
unproved quotient inequality.

Reading 2: finite-block trend reading. Define

```text
C_J^wit(beta,N) = beta*(-Delta_J(beta,N)),
C_D^wit(beta,N) = beta*Delta_D(beta,N).
```

These are finite witnesses, not constants. The runner prints them to test
consistency with the formal `1/beta` scale and to expose the narrow margin.
They are not used to prove `c_D <= c_J`.

## Witness Rows

The runner recomputes the finite-block rows below with the exact Wilson
diagonal derivative. The tight finite row is fenced as evidence only:

| beta | shell | C_J^wit | C_D^wit | C_J^wit - C_D^wit | C_D^wit/C_J^wit |
|---:|---:|---:|---:|---:|---:|
| 20 | 12 | 0.831287608242 | 0.733024709589 | 0.098262898653 | 0.881794342080 |
| 30 | 16 | 0.837307840913 | 0.776931164272 | 0.060376676642 | 0.927891901053 |
| 40 | 18 | 0.847762095819 | 0.793560913913 | 0.054201181906 | 0.936065575268 |
| 50 | 22 | 0.845980865746 | 0.810590301970 | 0.035390563776 | 0.958166236131 |

The last ratio restates the known tightness signal. It is evidence for the
shape of the obstruction, not a proof of the limiting ratio.

## Falsifiers

Wrong-structure substitutions visibly change the finite or reduced rows:

| substitution | row |
|---|---:|
| correct exact finite row, beta `20`, shell `12` | `Delta_J + Delta_D = -0.004913144933` |
| wrong derivative recurrence scale `1/5` instead of `1/6` | `Delta_J + Delta_D = +0.002417102163` |
| wrong half-slice source scale `J=0` on the same finite row | `Delta_J + Delta_D = +0.026142350801` |
| correct reduced saddle ratio, beta `20`, shell `12` | `0.203758341733` |
| wrong saddle constant `2 C2/beta` | `0.273042774766` |
| wrong dimension factor omitted from the saddle diagonal | `0.157783689333` |
| wrong reduced source scale `J=0` | `0.943492137331` |

These falsifiers do not prove the desired domination. They show that the
normalization, `N_c = 3` saddle exponent, and `SU(3)` dimension factor are
load-bearing.

## Differentiation From Prior Notes

Restated from the block-Hellmann rung-eight note: the finite-block split, the
definitions of `Delta_J` and `Delta_D`, the witnessed signs, and the tight
finite ratio.

Restated from the operator-remainder rung-eight note: the saddle multiplier
`H exp(-Q)`, the scaling `p,q = O(sqrt(beta))`, and the half-slice semigroup
surface.

New in this note: the derivative-side saddle identity
`beta r_sad'/r_sad -> Q`, the local six-neighbor Taylor generator check, the
formal expressions for `c_J` and `c_D`, and the precise statement that the
constants are spectral quantities not derived by the current authorities.

## Negative-Claim Discipline Gate

Skill freshness: the repo-native no-go discipline instructions were read
before review. This gate records a partial obstruction with named residuals
only.

N1 - Alternative route enumeration:

1. Direct exact-Wilson differentiation. ATTEMPTED. The exact recurrence gives
   `r'`, but the step from pointwise diagonal derivatives to `c_D <= c_J`
   requires spectral control of the top two branches.
2. Saddle diagonal derivative. ATTEMPTED. This note derives
   `beta r_sad'/r_sad -> Q`, but the comparison still depends on the reduced
   eigenfunctions.
3. J-expectation asymptotics. ATTEMPTED. The six-neighbor Taylor check supplies
   the local `J-I -> beta^(-1)L` generator on interior smooth tests, but
   converting that into a value of `c_J` again needs the reduced spectral pair.
4. Finite trend extrapolation. ATTEMPTED as a witness only. It is rejected as a
   proof input because fitted constants would violate the anti-fabrication
   rule.
5. Operator-remainder transfer. ATTEMPTED by prior note. The exact-Wilson
   `wilson_to_saddle_uniform(a)` estimate is explicitly still missing.

N2 - Wall-independence audit:

The collapsed wall set is one main wall with one transfer consequence:
derive the reduced spectral inequality `c_D <= c_J`, then transfer it through
the exact Wilson active-window and tail estimates. The transfer does not help
unless the reduced inequality exists; the reduced inequality does not prove the
exact Wilson claim without transfer.

N3 - Hidden-wall scan:

The phrases "conditional on a limiting isolated spectral pair" and "uniform
subleading bound" are explicit walls, not background assumptions. No appeal to
standard perturbation theory is used as the proof of H8-D.

N4 - Residual matching:

The block-Hellmann rung-eight note matches the derivative-domination residual.
The operator-remainder rung-eight note matches the saddle-profile and
reduced-operator context. The Wilson-to-saddle obstruction note matches the
exact-Wilson transfer residual. None of them supplies the missing reduced
spectral inequality.

N5 - Rhetoric audit:

The negative statement is at the source-note derivation level: this note does
not derive `c_D <= c_J`. It does not assert that the inequality is false, and
it does not make a lattice-wide impossibility claim.

N6 - Partial-closure path scan:

Two partial-closure paths remain live: prove the reduced spectral inequality
directly, or prove a stronger exact-Wilson operator inequality that bypasses
the separated constants. Neither path is classified as requiring a new axiom.

N7 - Steelman:

A hostile reviewer could argue that `T_infty` has hidden total-positivity or
oscillation structure: the first non-Perron mode may have a variationally
ordered `L` penalty, while the `Q` insertion may be bounded by the same nodal
energy. If such a principle is derived from the `A_2` Weyl-chamber semigroup
and the positive multiplier `H exp(-Q)`, it could produce `c_D <= c_J` without
fitting the finite rows. This note has not supplied that principle.

N8 - Cross-cycle echo:

The closest existing echo is the operator-norm remainder note, where the
geometric saddle piece is available but the exact Wilson-to-saddle estimate is
not. The same lesson applies here: saddle algebra is useful, but the
load-bearing exact-Wilson or reduced-spectral inequality must be supplied
before the half-line derivative claim can be assembled.

## Verification

Run:

```bash
python3 scripts/native_gauge_transfer_diagonal_domination_rung_nine_bounded_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=29, FAIL=0
```
