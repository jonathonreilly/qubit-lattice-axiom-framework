# Channel-Count Guard Canonical Note

**Status:** bounded - bounded or caveated result note
Date: 2026-04-02
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/guard_reconciliation_n100_q003_certificate.py`](../scripts/guard_reconciliation_n100_q003_certificate.py)
**Runner cache:** [`logs/runner-cache/guard_reconciliation_n100_q003_certificate.txt`](../logs/runner-cache/guard_reconciliation_n100_q003_certificate.txt)

This note is the canonical writeup for the dense-prune gravity-repair guard.
It folds together:

- script reconciliation
- same-graph guard results
- seed-level replay behavior
- the current safe claim

**2026-05-26 audit-packet repair:** the load-bearing scope is narrowed to the
aggregate `N=100, q=0.03` dense same-graph pocket reproduced by the primary
runner above. The runner executes the canonical dense guard script with
`DENSE_GUARD_LAYERS=100` and `DENSE_GUARD_QS=0.03`, producing the cached stdout
needed for re-audit. Seed-selective examples are context only and are not
load-bearing in this repaired packet.

Primary scripts:

- [`scripts/dense_prune_channel_count_guard.py`](../scripts/dense_prune_channel_count_guard.py)
- [`scripts/channel_count_guarded_prune.py`](../scripts/channel_count_guarded_prune.py)
- [`scripts/channel_count_threshold_sweep.py`](../scripts/channel_count_threshold_sweep.py)

Supporting diagnostics:

- [`scripts/dense_prune_path_cancellation_audit.py`](../scripts/dense_prune_path_cancellation_audit.py)
- [`scripts/dense_prune_flip_seed_replay.py`](../scripts/dense_prune_flip_seed_replay.py)

## Mechanism Summary

The old coarse guards were protecting the wrong quantity.

- coarse reach/core metrics stay flat when gravity flips
- frozen-field controls do not explain the flip
- weighted-flow proxies are not enough
- path-cancellation diagnostics point to **effective detector channel count** (`eff_ch`) as the useful vulnerable quantity

So the guard story is now:

- pruning can break gravity by collapsing detector-channel support for the deflection pattern
- a useful guard should protect `eff_ch`, not generic reach

## Why The Two Guard Scripts Disagree

They are not the same experiment.

[`scripts/channel_count_guarded_prune.py`](../scripts/channel_count_guarded_prune.py) is a narrow fixed-`q=0.10` pilot:

- `N = 80, 100, 120`
- fixed `q = 0.10`
- guard rule: stop when `eff_ch` falls below `80%` of the original baseline
- unguarded arm: one-step `_prune_graph(..., q=0.10, n_iters=1)`
- guarded arm: custom iterative loop with `max_iter=3`

[`scripts/dense_prune_channel_count_guard.py`](../scripts/dense_prune_channel_count_guard.py) is the broader dense same-graph study:

- `N = 80, 100, 120`
- `q` sweep: `0.03, 0.05, 0.10`
- guard rule: keep `eff_ch` above `max(2.5, current_eff * 0.85)`
- unguarded arm: `_prune_graph(..., q, PRUNE_ITERS)`
- guarded arm: binary-search acceptance on the removable low-`D` set

So the disagreement is methodological, not a bug:

- the pilot asks whether a strict fixed-`q=0.10` guard can stop flips
- the dense script asks whether a more flexible same-graph guard preserves the decoherence gain across pruning strengths

## Canonical Guard Read

Treat [`scripts/dense_prune_channel_count_guard.py`](../scripts/dense_prune_channel_count_guard.py) as the canonical same-graph guard study.

Current safe read from that script:

- strongest pocket: `N=100, q=0.03`
- plain pruning:
  - `Δpur = +0.0094`
  - `Δgrav = -3.2356`
  - flips `= 3`
- channel-count-guarded:
  - `Δpur = -0.0039`
  - `Δgrav = -0.1272`
  - flips `= 0`

Interpretation:

- the guard materially improves the gravity story where the plain lane fails
- the decoherence gain does not survive in this aggregate pocket; the guarded
  arm pays a small bounded purity cost (`d_pur = -0.0039`) while preserving
  the gravity sign and removing flips
- this is a **narrow bounded workaround**, not a general asymptotic rescue

At `N=80`, the dense script shows help but not a full fix.

At `N=120`, the dense script is not interpretable as a positive extension under the current setup.

## Narrow Fixed-q Pilot Read

[`scripts/channel_count_guarded_prune.py`](../scripts/channel_count_guarded_prune.py) is still useful, but only as a regression pilot for the strict fixed-`q=0.10` case.

Its current read is:

- `N=80`: flips can be driven to `0`, with `pur_p < pur_b`
- `N=100`: gravity stays positive under the guard, but some flips remain
- `N=120`: the graph is already too fragile; the guard effectively blocks all pruning

This is consistent with a bounded mechanism:

- the guard helps most while `eff_ch` is still recoverable
- once baseline `eff_ch` is already too low, the guard becomes a “do not touch” detector rather than a repair tool

## Seed-Level Read (context only)

The seed-level examples below are not load-bearing for this repaired packet.
The prior seed note is retained as a context pointer, but the current audit
target is the aggregate `N=100, q=0.03` runner certificate above.

Supporting note:
- `DENSE_PRUNE_GUARD_SEED_NOTE.md`

Seed-level replay says, as contextual diagnostics:

- some historically flip-prone seeds are rescued by the guard
- some are not
- rescue tracks preserved `eff_ch`, not a generic change in mean behavior

Clean rescue examples:

- `N=80`, seed `12`
- `N=100`, seed `13`

Clean non-rescue example:

- `N=100`, seed `3`

So the contextual mechanism read is:

- **seed-selective channel preservation**
- not a pure averaging artifact

## Threshold Sweep Status

[`scripts/channel_count_threshold_sweep.py`](../scripts/channel_count_threshold_sweep.py) is the right next map:

- thresholds: `0.70, 0.75, 0.80, 0.85, 0.90`
- `q`: `0.03, 0.05, 0.10`
- `N = 80, 100`

Its purpose is to tell us whether the canonical `N=100, q=0.03` pocket is:

- a one-threshold coincidence
- or the center of a real bounded guard basin

Until that sweep lands, do not overstate the size of the viable guard region.

## Current Safe Claim

The canonical guard story is:

- coarse reach/core guards are too blunt
- `eff_ch` is the right diagnostic family
- in the aggregate `N=100, q=0.03` certificate, channel-count preservation
  reduces gravity damage and removes flips relative to plain pruning
- the strongest bounded pocket is `N=100, q=0.03`
- the fix is bounded, not asymptotic

## Runner-backed N=100, q=0.03 certificate

The primary runner reports:

```text
100 plain   q=0.03 valid=4 pur_b=0.9080 pur_p=0.9174 d_pur=+0.0094
                         grav_b=+1.5462 grav_p=-1.6894 d_grav=-3.2356
                         eff_b=5.005 eff_p=2.447 removed=115.0 flips=3
100 guarded q=0.03 valid=6 pur_b=0.9138 pur_p=0.9098 d_pur=-0.0039
                         grav_b=+1.5963 grav_p=+1.4691 d_grav=-0.1272
                         eff_b=5.159 eff_p=5.056 removed=14.5 flips=0
```

This supports only the narrow aggregate read: the channel-count guard preserves
`eff_ch` in the `N=100, q=0.03` pocket and eliminates the plain-prune flip
count in that aggregate comparison at a small bounded purity cost. It does not
prove a seed-level rescue law or a simultaneous purity-improvement theorem.

## Avoid

Do not currently say:

- the guard “solves” dense-prune gravity
- the guard works uniformly at `N=80, 100, 120`
- the dense-prune lane is asymptotically repaired

The honest wording is:

- **channel-count preservation is the right mechanism family**
- **the guard yields a narrow same-graph gravity-preservation signal at small
  bounded purity cost**
- **the lane still dies or freezes out at larger `N`**
