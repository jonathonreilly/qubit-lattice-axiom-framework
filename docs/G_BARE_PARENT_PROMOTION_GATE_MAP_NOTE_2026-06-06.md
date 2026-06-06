# g_bare Parent Promotion Gate Map

**Date:** 2026-06-06
**Claim type:** meta
**Status:** branch-local no-go gate map; negative route pruning.
**Lane:** `g_bare` normalization / DM relic mapping dependency closure.
**Runner:** `scripts/frontier_g_bare_parent_promotion_gate_map_2026_06_06.py`

This note is a branch-local science-loop artifact. It does not retag any
ledger row, update any authority surface, or propose a new framework axiom.

## Targeted Review Gate

The active review queue item
`2026-05-03-gbare-parent-retention-gate` says the salvaged rescaling-freedom
and constraint-vs-convention candidate rows must be independently audited and
carried with dependency closure before `G_BARE_DERIVATION_NOTE.md` or any
downstream `g_bare = 1` status surface cites them as closing the old repair
target.

The current parent note already reflects that gate: the parent theorem is open
until both 2026-05-03 repair candidates are independently accepted, retained-
grade dependency closure is checked, and the parent row is re-audited on the
changed source and dependency surface. The same parent note states that the
canonical connection normalization remains an admitted upstream convention
layer and is not derived from the minimal lattice/one-site algebra baseline
alone.

The 2026-05-28 promotion-panel finding sharpens the obstruction: the algebra
identities are not the missing part. The missing part is whether the
normalization scalar `N_F = 1/2` is forced by the framework baseline or is an
admitted convention. Under the current source surface, the panel classifies
`N_F = 1/2` as the single load-bearing admission, and the L3 notes as
invariance/robustness results rather than uniqueness results.

## Gate Predicates

| Predicate | Current source-surface result | Consequence |
|---|---:|---|
| Conditional Wilson / Ward algebra identities are available | yes | They support the conditional core. |
| Both 2026-05-03 repair candidates are enough by themselves | no | The parent still needs independent audit plus dependency closure. |
| Parent row has completed re-audit on the changed surface | no | Parent status remains open. |
| `N_F = 1/2` is forced by the one-qubit / `Z^3` baseline | no | Parent cannot move from bounded/conditional support to an unconditional physical normalization statement. |
| L3 invariance proves L3 uniqueness | no | Robustness along a convention orbit is not selection of the orbit point. |
| Per-site `SU(2)` spin scale already propagates to gauge `su(3)` | no | The staggered-Dirac realization gate remains the non-circular route. |

Therefore the route

```text
conditional algebra core + L3 invariance => parent promotion
```

is blocked on the current surface.

## No-Go Statement

The current source surface supports the conditional statement:

```text
given the accepted canonical normalization N_F = 1/2 and the Wilson/Ward
matching premises, g_bare = 1 and beta = 6 follow algebraically.
```

It does not support the stronger parent statement:

```text
the minimal one-qubit / Z^3 framework forces N_F = 1/2 and hence forces
g_bare = 1 without an admitted normalization or realization premise.
```

The obstruction is exact at the level of premise accounting. An invariance
theorem can show that changing some convention coordinate leaves the computed
`g_bare` unchanged, but it cannot by itself select `N_F = 1/2`. A parent
promotion route must either:

1. close the staggered-Dirac realization gate that propagates the per-site
   spin-double-cover scale to the gauge `su(3)` trace surface, or
2. explicitly remain conditional on the accepted normalization convention and
   avoid parent-surface promotion language.

## Route Classifier

| Route | Status | Why |
|---|---|---|
| Conditional Wilson matching at fixed `N_F = 1/2` | exact support | The algebra is already the supported core. |
| Ward/two-representation identity at fixed residue | exact support | It is a simultaneous-constraint identity, not a source of the trace scale. |
| L3 trace-surface and scalar invariance | exact support / boundary | Invariance is not uniqueness. |
| Parent re-audit after two repair candidates | open | Requires independent audit/dependency closure and parent re-audit. |
| Per-site `SU(2)` scale to gauge `su(3)` scale | open hard residual | Requires the staggered-Dirac realization bridge. |
| Dynamical fixed point, maximum entropy, mean-field iteration, or lattice beta selector for `g = 1` | no-go | The parent note already records these routes as not selecting `g = 1`. |

## What This Unlocks

This does not unlock a new positive `g_bare` claim. It does unlock a clean
work queue split:

- the conditional algebra core can be reused as exact support at fixed
  normalization;
- parent-surface promotion should not be attempted by re-running algebra-only
  checks;
- bounded-to-stronger status work should focus on the staggered-Dirac
  realization route or on explicit admitted-premise bookkeeping;
- downstream DM provenance notes can cite the conditional core honestly while
  keeping the normalization admission visible.

## Imports And Boundaries

- No observed physical constants are used.
- No fitted selector or same-surface family argument is introduced.
- Literature context from the panel remains non-load-bearing.
- No repo-wide audit verdict is applied here.
- No claim is made that `g_bare = 1` is false; the conditional statement is
  preserved.

## Verification

Run:

```bash
python3 scripts/frontier_g_bare_parent_promotion_gate_map_2026_06_06.py
```

Expected summary:

```text
TOTAL: PASS=45, FAIL=0
```
