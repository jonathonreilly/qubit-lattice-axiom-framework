# AC_phi_lambda Occupancy Determinant-Power Split Exact Support

**Date:** 2026-07-04
**Claim type:** bounded_theorem
**Status:** source-side exact support; independent audit required before any
effective-status change. This note does not derive `r = 1/2`, does not choose
the orbit/holomorphic horn, does not adopt the orbit-occupancy premise, does
not introduce a K-real primitive, does not retire `AC_phi_lambda` or
`AC_phi_lambda(i)`, and does not edit any Tier-A registry, axiom, primitive,
audit verdict, or publication surface.
**Current-main posture (2026-07-06):** live `main` now records Tier-A count
zero: theta was retired 2026-07-05 by retained derivation, and
`AC_phi_lambda` was retired by owner-governance adoption. This note banks the
historical determinant-power split support only; it does not reopen, modify,
or re-grade either retirement record, `tier_a_admissions.json`, or
owner-governed premise data.
**Primary runner:**
[`scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py`](../scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.txt`](../logs/runner-cache/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.txt)

## Target

The July 4 hygiene reclassified the per-lane `r` value of
`AC_phi_lambda(i)` to realized-state registration. The live Tier-A residual is
now narrower:

```text
which grain/statistics the matter action implements:
sector-tied/count-twice or orbit/holomorphic/count-once
```

The first-order staggered determinant theorem already shows that the
one-component staggered matter measure gives a first-order holomorphic
generation determinant and that count-twice behavior appears on the K-real
restriction `c = conj(b)`. Current-main no-supply packets correctly block the
shortcut from determinant or Record/axiom support to immediate retirement. This
note adds the missing reusable algebraic support underneath the fork: for any
complex kernel, the realified count is
exactly the squared-modulus determinant, while the holomorphic Berezin count is
the complex determinant to first power.

## Exact Statement

Let `K = X + iY` be an `n x n` complex matrix, with `X` and `Y` real. Its real
linear representation is

```text
R(K) = [[X, -Y],
        [Y,  X]].
```

Then

```text
det_R R(K) = det_C(K) * conjugate(det_C(K)) = |det_C(K)|^2.
```

The runner proves this symbolically for a generic `2 x 2` complex kernel and
checks the scalar and scaling cases exactly. It also computes the holomorphic
Berezin Gaussian directly by exterior algebra and obtains

```text
Integral exp(chibar K chi) = det_C(K)
```

to the first power. Therefore the count-once/count-twice binary is a
determinant-power binary:

| Reading | Kernel object | Determinant power | Slot interpretation |
|---|---|---|---|
| Holomorphic/orbit | `K` complex-linear | `det_C(K)` | one complex/K-orbit slot |
| Realified/sector-tied | `R(K)` real-linear | `|det_C(K)|^2` | two real sector slots |

The same identity is the abstract reason the C3 first-order theorem localizes
count-twice to `c = conj(b)`: imposing the K-real/tied section turns the
holomorphic independent variables into a conjugate pair and supplies the
mixed `b*bbar` term. With `c` independent the determinant is holomorphic; on
the tied section it is squared-modulus/count-twice data.

## What Moves

This block strengthens the AC(i) route map:

1. The remaining occupancy atom is not an unexplained phrase. It is exactly
   the choice between a complex determinant counted once and its realified
   determinant counted twice.
2. The determinant-power split is source-side algebra, independent of fitted
   lepton values or owner governance.
3. The first-order staggered determinant theorem and the current-main
   no-supply packets are reconciled: the first-order theorem supplies the
   holomorphic branch as valid route material; the no-go boundary remains
   correct because a physical theorem must still select that branch as the
   matter action's readout.

## What Does Not Move

- `AC_phi_lambda` is not retired.
- `AC_phi_lambda(i)` is not retired.
- The orbit/holomorphic horn is not selected.
- The sector/K-real horn is not selected.
- `r = 1/2` is not derived, predicted, or preferred.
- The orbit-occupancy premise candidate is not adopted.
- No physical generation Yukawa coupling form is derived.
- No K/CPT-site-basis physical predicate is derived.
- No registry, primitive, axiom, audit status, or publication status is edited.
- `AC_phi_lambda(ii)` / R-eta and theta are untouched.

## Relation To Existing Blocks

- [`ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md`](ACPHILAMBDA_OCCUPANCY_SELECTION_REALIZED_STATE_REDUCTION_NOTE_2026-06-11.md)
  reclassifies the value face and names the measure-side realization binary as
  the survivor. This note supplies exact determinant-power support for that
  survivor.
- [`KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  computes the staggered surface and localizes the count-twice term to
  `c = conj(b)`. This note abstracts the same fork as
  `det_C` versus `det_R(realification)`.
- [`ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md)
  remains valid: axioms and approved primitives do not select the physical
  matter-action statistics horn.
- [`ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md`](ACPHILAMBDA_OCCUPANCY_FORMATION_APPEND_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md)
  remains valid: Record formation/additivity does not identify the occupancy
  dictionary or formation rule.
- [`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`](CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md)
  and [`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`](GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md)
  already identify the value-facing fork as `det_C`/block-count versus
  `det_R`/dimension. This note makes the determinant-power identity explicit.

## Remaining Live Routes

1. **Physical horn-selection theorem.** Derive that the actual matter action
   implements the holomorphic/K-orbit readout or the realified/K-real readout.
2. **Physical coupling theorem.** Derive the relevant generation coupling
   channel rather than supplying a probe kernel.
3. **K/CPT-site-basis bridge.** Derive the physical antiunitary predicate whose
   tied section is being read.
4. **Durability or governance route.** Adopt a narrow owner-ratified premise if
   derivation is not required.
5. **R-eta route.** Separately derive the density-read-as-angle identification.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py
```

Expected close: `FAIL=0`.

**Independent audit required.** This note asserts no effective-status change.
