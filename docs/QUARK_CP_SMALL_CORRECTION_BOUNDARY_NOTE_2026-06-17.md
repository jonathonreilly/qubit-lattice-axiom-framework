# Quark CP Small-Correction Boundary Note

**Date:** 2026-06-17
**Status:** exact-support / bounded-support boundary for the small-correction
residual; no retained-status upgrade
**Runner:** `scripts/frontier_quark_cp_small_correction_boundary.py`
**Parent:** `QUARK_CP_CARRIER_COMPLETION_NOTE_2026-04-18.md`

## Scope

This note addresses one narrow residual in the quark CP-carrier completion:
whether the fitted complex `1-3` carriers can be read as a small perturbative
correction to the Schur-generated `1-3` base.

The answer is negative for the current parent completion. The existing fitted
pair is non-perturbative relative to the Schur base. Therefore the parent
completion should be read as a bounded non-perturbative carrier ansatz, not as
a retained small correction.

This note does not derive `xi_u`, `xi_d`, the comparator targets, or a
framework-native normalization law for the non-perturbative carrier. It also
does not change audit status or claim an effective retained result.

## Exact fitted-solution boundary

The parent completion uses

```text
c13_u(total) = c13_u(base) + xi_u
c13_d(total) = c13_d(base) + xi_d
```

with the fitted values

```text
xi_u = +0.340735147 - 0.063202935 i
xi_d = +0.078186196 + 0.108371050 i
```

and Schur-base terms

```text
c13_u(base) = 3.400565729750e-03
c13_d(base) = 2.011510840850e-02
```

The exact ratios checked by the runner are

```text
|xi_u| / |c13_u(base)| = 101.908728437
|xi_d| / |c13_d(base)| =   6.643337509
```

Thus any sectorwise cap

```text
|xi_s| <= R_s |c13_s(base)|
```

that contains the shipped solution must have

```text
R_u >= 101.908728437
R_d >=   6.643337509
```

and any common cap must have

```text
R >= 101.908728437.
```

This is the exact boundary for the shipped parent fit. Under ordinary
perturbative readings such as `R <= 1`, or even a generous finite-amplitude
reading such as `R <= 5`, the fitted completion is outside the small-correction
class.

The runner also checks that the fitted carrier accounts for nearly all of the
completed `1-3` coefficient:

```text
|xi_u| / |c13_u(total)| = 0.990442514
|xi_d| / |c13_d(total)| = 0.913327261
```

So the carrier is not a small additive tweak hidden behind the completed
coefficient. It is the dominant contribution to the completed `1-3` slot.

## Bounded capped-surface scan

To test whether a nearby small-capped point on the same parent slice can still
recover the CKM/J target, the runner parameterizes

```text
xi_s = rho_s c13_s(base) exp(i phi_s),      0 <= rho_s <= R
```

and lets `m_u/m_c` and `m_c/m_t` move within `1%` of the parent comparators.
It then runs a deterministic finite optimizer against the parent target surface
`(|V_us|, |V_cb|, |V_ub|, J)`.

This scan is bounded numerical evidence, not a proof of a global supremum.
Its role is to prevent the source note from implying that a small capped
completion is already visible in the parent surface.

Current best-found capped fits:

| common cap `R` | `rho_u` | `rho_d` | `|V_us|/T` | `|V_cb|/T` | `|V_ub|/T` | `J/T` | max relative error |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `1` | `0.999920` | `0.999999` | `0.999471` | `1.000255` | `0.972594` | `0.128867` | `0.871133` |
| `2` | `1.999985` | `2.000000` | `0.999757` | `1.000061` | `0.994113` | `0.327177` | `0.672823` |
| `5` | `4.999982` | `3.377115` | `0.996861` | `0.999730` | `1.033197` | `0.571908` | `0.428092` |
| `10` | `9.999950` | `3.551434` | `0.997327` | `0.999781` | `1.029043` | `0.603034` | `0.396966` |
| `50` | `49.999748` | `5.018942` | `0.999370` | `0.999984` | `1.009502` | `0.821279` | `0.178721` |
| `100` | `99.875294` | `6.647672` | `0.999993` | `1.000042` | `1.000562` | `0.984134` | `0.015866` |

The bounded scan aligns with the exact fitted-solution boundary: caps in the
perturbative range do not recover the parent Jarlskog target, and the fit only
approaches the target once the up-sector cap is of the same order as the
fitted non-perturbative carrier.

## Implication for the parent row

This note closes the small-correction interpretation negatively for the parent
completion. It does not make the parent a first-principles quark-mass theorem.
The source-side statement should be:

- the minimal Schur-NNI surface still fails as an intrinsic CKM CP closure;
- the one-complex-`1-3`-carrier-per-sector extension still gives a bounded
  numerical completion;
- that completion is non-perturbative relative to the Schur `1-3` base;
- any retained-grade upgrade still needs a derivation of the carrier
  coefficients, the target/readout bridge, and a framework-native
  normalization for the non-perturbative carrier.

## Validation

Run:

```bash
python3 scripts/frontier_quark_cp_small_correction_boundary.py
python3 scripts/frontier_quark_cp_carrier_completion.py
python3 scripts/cached_runner_output.py scripts/frontier_quark_cp_small_correction_boundary.py --refresh
python3 scripts/cached_runner_output.py scripts/frontier_quark_cp_small_correction_boundary.py --check-only
```

Current expected results:

```text
frontier_quark_cp_small_correction_boundary.py: PASS=9 FAIL=0
frontier_quark_cp_carrier_completion.py: PASS=11 FAIL=0
```
