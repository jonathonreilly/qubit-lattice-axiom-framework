# DM Leptogenesis PMNS Algebraic Stationary Diagnostic

**Status:** bounded - sampled algebraic/KKT diagnostic only
**Status authority:** independent audit lane only
**Date:** 2026-04-16 (scope narrowed 2026-05-26)
**Script:** `scripts/frontier_dm_leptogenesis_pmns_analytic_stationary_classification_theorem.py`
**Framework convention:** "axiom" means only `Cl(3)` on `Z^3`

## Scope narrowing (2026-05-26)

The prior audit row was `audited_conditional` because the note claimed more
than the restricted packet closed: a fixed `N_e` reduced surface, a
seed-relative effective-action selector, favored-column closure, and a
branch-count/uniqueness statement were treated as theorem-grade inputs even
though they entered through helper runners and unaudited support notes.

This revision takes the bounded repair path.  The binding claim is now only:

1. the charged Hermitian block used by the imported fixed `N_e` chart has the
   displayed closed form;
2. the `delta -> -delta` conjugation symmetry makes the sampled quantities
   even on the tested real slice;
3. the two sampled stationary representatives reported by the audit-scoped
   multistart diagnostic satisfy the runner's KKT residual check; and
4. those two sampled representatives have the recorded finite action gap.

The note does **not** claim a certified-global branch enumeration, a unique
physical selector, a derivation of the fixed `N_e` surface from the sole axiom,
or a physical off-seed source law.

## Question

What algebraic content remains audit-ready after removing the unsupported
global-selector surface from the original stationary-classification note?

## Bottom line

The current packet supports a bounded diagnostic:

- the closed-form `H_e = Y Y^dagger` expression is exact for the imported chart;
- `H_e(delta)` and `H_e(-delta)` are conjugate, so the sampled action and PMNS
  packet checks are even under `delta -> -delta`;
- the two sampled closure representatives from the multistart support runner
  satisfy the KKT residual check used by the diagnostic; and
- within that sampled pair, the lower-action representative closes the tested
  favored column and is separated from the second representative by a finite
  action gap.

This is useful support for the DM/PMNS lane, but it is not retained selector
authority and not full-stack closure.

## Closed-form reduction

On the imported `N_e` chart,

```text
Y = [[x_1, y_1, 0],
     [0, x_2, y_2],
     [y_3 exp(i delta), 0, x_3]]
```

so

```text
H_e = Y Y^dagger

H_11 = x_1^2 + y_1^2
H_22 = x_2^2 + y_2^2
H_33 = x_3^2 + y_3^2
H_12 = x_2 y_1
H_23 = x_3 y_2
H_13 = x_1 y_3 exp(-i delta)
```

Thus `H_e(delta)` and `H_e(-delta)` are conjugate.  This is the exact algebraic
parity content retained by this narrowed row.

## Sampled KKT Diagnostic

The runner reuses the sampled branch representatives from the multistart
support runner included in the restricted packet.  This use is scoped as a
sampled multistart diagnostic rather than a global selector theorem.

For each sampled representative, the runner checks:

- closure compatibility on the imported fixed chart;
- `delta -> -delta` parity of the sampled action and closure value; and
- numerical smallness of the KKT residual for the imported seed-relative action
  objective and closure constraint.

These checks are residual diagnostics on the sampled representatives.  They do
not prove that no other stationary component exists.

## Sampled Branch Pair

The diagnostic records the following sampled pair:

- lower-action sampled representative:
  - `x = (0.471675, 0.553810, 0.664515)`
  - `y = (0.208063, 0.464382, 0.247555)`
  - `delta ~ 0`
  - `eta / eta_obs = 1` on the tested favored column
- second sampled representative:
  - `x = (0.790189, 0.406763, 0.493049)`
  - `y = (0.586185, 0.167566, 0.166248)`
  - `delta ~ 0`
  - `eta / eta_obs = (1.0, 0.94763529, 0.95876001)`

The sampled-pair action gap remains finite:

```text
Delta S = 0.869750837948
```

## Out Of Scope

This row explicitly does not claim:

- global reduced-surface branch enumeration;
- unique global minimum or unique physical selector status;
- derivation of the fixed `N_e` surface from `Cl(3)` on `Z^3`;
- derivation of the physical off-seed source law; or
- promotion of any unaudited PMNS/relative-action helper row.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_analytic_stationary_classification_theorem.py
```
