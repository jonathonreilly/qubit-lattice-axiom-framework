# DM Leptogenesis PMNS Stationary CP Incompatibility Theorem

**Date:** 2026-04-16  
**Status:** support - structural or confirmatory support note
as constructive witnesses for the source-oriented mainline leptogenesis branch  
**Script:** `scripts/frontier_dm_leptogenesis_pmns_stationary_cp_incompatibility_theorem.py`

## Question

Can the current exact PMNS selector families on the fixed native `N_e` seed
surface serve as constructive witnesses for the source-oriented mainline CP
branch?

## Bottom line

No.

The current KKT-filtered PMNS selector families are transport selectors only.
On the current branch they are CP-sheet-indeterminate with respect to the
mainline charged-sector bridge.

The reason is exact and simple:

1. the current selector observables are even under `delta -> -delta`
   on the fixed native `N_e` seed surface:
   - the exact closure data are unchanged
   - the seed-relative selector action is unchanged
   - the current minimum-information deformation cost is unchanged
2. the charged-sector bridge law gives

   `gamma = x_1 y_3 sin(delta)`

3. while the interference channels

   `E1 = delta + rho`

   `E2 = A + b - c - d`

   are even under `delta -> -delta`
4. therefore the intrinsic mainline CP tensor flips sign:

   `cp1(-delta) = -cp1(delta)`

   `cp2(-delta) = -cp2(delta)`.

So the current PMNS selector families cannot realize the constructive
source-oriented mainline CP sheet.

## What this establishes

This resolves the real remaining ambiguity in the PMNS lane for the current
selector families.

Before this theorem, the PMNS route still had two live readings:

- maybe the current PMNS selector family is already the right constructive CP
  witness and only needs better packaging
- or maybe it is only a transport selector and not a baryogenesis witness

The theorem resolves that ambiguity negatively for the **current selector
families**:

- they are transport-useful
- they are not the constructive mainline CP witness
- they determine parity classes, not a theorem-grade CP sign choice
- each selected family has an equally selected opposite-CP partner

## Scope

This theorem is about the **current KKT-filtered selector families**:

- the sampled reduced-surface stationary branches retained by the current
  KKT filter
- the current minimum-information selector law

It does **not** prove that every conceivable PMNS-inspired charged-sector law
is impossible.

It proves only that the current selector families on the fixed native `N_e`
seed surface are CP-sheet-indeterminate on the mainline charged-sector bridge.

## Consequence for the live target

If a positive PMNS-side bridge is still desired, it must move off the current
selector families.

The live constructive target is therefore no longer:

- better transport selection on the current PMNS reduced surface

It is instead:

- a new charged-sector / full-`D` law that breaks the current
  `delta -> -delta` ambiguity and enforces the source-oriented sign pattern
  `gamma > 0`, `E1 > 0`, `E2 > 0`

or else

- a stronger exact no-go proving that no such PMNS-side law exists on the
  current branch.

## Upstream authorities (selector-family + relative-action / min-info + charged-sector)

The runner imports four PMNS-side modules; three have framework wrapper notes:

- [DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MULTISTART_SELECTOR_SUPPORT_NOTE_2026-04-16.md) — selector-family construction (`selector` module).
- [DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md) — relative-action stationarity (`stat` module).
- [DM_LEPTOGENESIS_PMNS_BREAKING_TRIPLET_SOURCE_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_BREAKING_TRIPLET_SOURCE_LAW_NOTE_2026-04-16.md) — charged-sector triplet-channel source law (`triplet_channels_from_active_data`).
- [DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md) — minimum-information source-law module (`minlaw`).

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_stationary_cp_incompatibility_theorem.py
```
