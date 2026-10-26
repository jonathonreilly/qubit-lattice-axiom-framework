# DM Leptogenesis PMNS Observable-Relative-Action Law

**Type:** bounded_theorem
**Date:** 2026-04-16 (initial); 2026-05-16 prose recast so the load-bearing
objective is expressed by its effective-action identity; physical minimization
and the observed-target constraint remain supplied selection premises.
**Status:** support - structural / confirmatory support note attached to the
already-landed `DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16`.  
**Script:** `scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py`  
**Framework baseline:** physical `Cl(3)` local algebra on the `Z^3`
spatial substrate.

## Role of this note

This note evaluates the operational PMNS-assisted off-seed source selector as
an adopted constrained source-selection prescription.
The relative-action identity below fixes the objective's algebraic form; it
neither derives a physical minimization postulate nor selects the observed-target
constraint `eta / eta_obs = 1`. Numerical solutions therefore give conditional
source witnesses, not independent predictions of the baryon asymmetry.

## Selector law (operational form)

On the fixed native charged-lepton-active seed surface, define the exact
relative bosonic action

`S_rel(H_e || H_seed) = Tr(H_seed^{-1} H_e) - log det(H_seed^{-1} H_e) - 3`

where:

- `H_seed` is the exact aligned-seed charged Hermitian block
- `H_e` is the charged Hermitian block induced by the off-seed source

Then:

1. determine the favored flavor column `i_*` from the finite numerical transport-search
   witness
2. among all positive off-seed sources on the same seed surface satisfying
   `eta_{i_*} / eta_obs = 1`, choose the one minimizing `S_rel`

## Objective identity and the supplied selection prescription

For positive-definite Hermitian `H_seed` and `H_e`, the positive-definite
seed-normalized matrix `Y = H_seed^{-1/2} H_e H_seed^{-1/2}` satisfies

`S_rel(Y) = sup_K [ log det(I + K) - Tr(K Y) ]`

where the supremum is over Hermitian `K` with `I+K` positive definite,
with unique maximizer `K_* = Y^{-1} - I`. That is, `S_rel` is the **exact
Legendre dual** of the baseline-framework scalar observable generator
`W(K) = log det(I + K)`. This identity is proved and numerically exercised
in `DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16`
(`scripts/frontier_dm_leptogenesis_pmns_relative_action_stationarity_theorem.py`,
Part 1) and is **re-exercised inside this note's own runner** in Part 0 so
the derivation chain is visible from the support runner alone.

This identity does not discharge the physical selection premise. The
operational calculation additionally supplies:

- the seed surface and favored transport column;
- the observed-target equality `eta_{i_*}(H_e) / eta_obs = 1`;
- minimization of this objective on that constraint surface.

The sampled feasible-start search yields a candidate on the examined patch.
The separate constrained-stationarity diagnostic in that stationarity note
records an Euler-Lagrange residual at its `2e-5` tolerance boundary (its
canonical cache fails at `3.3e-5`; another platform gave `1.97e-5`), so the
candidate is not certified stationary, locally minimal or unique, and no
physical source law follows.

## Output of the operational law on the current branch

The operational law selects:

- `x_rel = (0.47167533, 0.55381069, 0.66451397)`
- `y_rel = (0.20806279, 0.46438280, 0.24755440)`
- `delta_rel ~ 0`

so the off-seed source is

- `xi_rel = (-0.09165800, -0.00952264, 0.10118064)`
- `eta_rel = (-0.09860388, 0.15771613, -0.05911224)`
- `delta_rel ~ 0`

and the resulting transport values are

`eta / eta_obs = (1.0, 0.75917896, 0.48458840)`,

with the numerical relative action value `S_rel = 0.240906701369` (matches the
Legendre-dual functional to ~1e-12 in the runner's Part 0).

The favored column remains column `0`; its imposed equality is met to the
reported numerical precision. This is not an independent observational match.

## What this note still does not claim

This note does **not** claim, on its own:

1. a branch-global analytic proof that no second disconnected closure
   component exists anywhere else on the full seed surface
2. a full PMNS microscopic solve beyond the current branch
3. promotion of any upstream row beyond what
   `DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16`
   itself claims

The objective identity is exact on its stated positive-definite domain.
The constrained source is numerical candidate support on the sampled patch;
these samples establish neither exact nor global uniqueness.

## Command

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_leptogenesis_pmns_relative_action_stationarity_theorem_note_2026-04-16](DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md)
