# DM Leptogenesis PMNS Minimum-Information Source Law

**Date:** 2026-04-16 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded conditional theorem — verifies consequences of an
adopted post-axiom selector law on the fixed native `N_e` seed surface.
The selector itself is an explicit definition imported from information
geometry; it is NOT derived from Cl(3) on Z^3.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding runner; it does not set
or predict an audit outcome.
**Primary runner:** `scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py`
**Framework convention:** "axiom" means only `Cl(3)` on `Z^3`.

## Purpose

This wrapper note documents the framework's `mininfo_source_law` PMNS-side
module so that downstream notes can register it as a one-hop dependency in
the citation graph. Several `audited_conditional` rows (notably
`dm_leptogenesis_pmns_selector_bank_cp_sheet_blindness_theorem_note_2026-04-16`,
`dm_leptogenesis_pmns_off_seed_triplet_sign_boundary_note_2026-04-16`, and
`dm_leptogenesis_pmns_stationary_cp_incompatibility_theorem_note_2026-04-16`)
named "mininfo_source_law" as a missing dependency edge; this wrapper closes
that admission at the citation-graph level.

## Adopted selector law

Conditional on adopting the minimum-information selector `I_seed` as a
post-axiom convention on the fixed native `N_e` seed surface:

1. Keep the already-derived native seed pair `(xbar, ybar)` fixed.
2. Determine the transport-favored flavor column `i_*` from the exact
   transport-extremal class.
3. Among all positive off-seed sources on that fixed seed surface satisfying
   `eta_{i_*} / eta_obs = 1`, choose the one minimizing the exact
   information-deformation cost

   ```
   I_seed = D_KL(x || x_seed) + D_KL(y || y_seed) + (1 - cos delta).
   ```

Adopting `I_seed` picks out a unique exact-closure off-seed source on the
transport-favored column.

## What this runner does NOT prove

- That `I_seed` follows from `Cl(3)` on `Z^3`.
- That `I_seed` is the unique correct selector. Alternative selectors exist;
  see [DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md)
  and [DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md).
- Baseline-framework closure for the PMNS-assisted `N_e` branch.

## Inputs and outputs

The runner consumes:
- the native `N_e` seed pair `(xbar, ybar)` from the active-projector
  reduction;
- the transport-favored column index from the exact transport-extremal
  class;
- the observed CP asymmetry `eta_obs` and the thermal package constants
  from `dm_leptogenesis_exact_common`.

It outputs:
- a unique low-`I_seed` exact-closure off-seed source on the
  transport-favored column;
- the conditional value of `I_seed` at the chosen source.

## Boundary

This wrapper note records the bounded-theorem character of the
`mininfo_source_law` runner. It does not claim:
- a framework-level derivation of the selector law `I_seed`;
- uniqueness of `I_seed` among admissible selectors;
- closure of the PMNS-assisted DM-leptogenesis chain.

Its only function is to provide a citeable one-hop authority for the
runner's adopted definition so downstream notes can register it cleanly.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_mininfo_source_law.py
```
