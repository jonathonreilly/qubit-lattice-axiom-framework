# Critical Exponents vs Graph Topology Finite Scout Live Packet

**Date:** 2026-04-10; live-source repair 2026-06-08
**Status:** bounded-support finite scout; proposed for independent re-audit, not effective retained.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_critical_exponents.py`](../scripts/frontier_critical_exponents.py)
**Primary runner cache:** [`logs/runner-cache/frontier_critical_exponents.txt`](../logs/runner-cache/frontier_critical_exponents.txt)

## Purpose

This note restores a current source surface for the legacy claim id
`critical_exponents_topology_note_2026-04-10`. The archived note failed because
its beta table was stale relative to the live runner.

This repaired note keeps only the current finite-size scout result and removes
any universality-class or asymptotic exponent inference.

## Live Claim

The live runner evaluates six configured graph families:

| family | base | n | G_crit | beta | R² | phi_sat | status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `random_geometric_s8` | `random_geometric` | 64 | 1.0 | `nan` | `nan` | 0.4128 | `degenerate` |
| `random_geometric_s10` | `random_geometric` | 100 | 2.0 | 0.7328 | 0.9656 | 0.3894 | `fit` |
| `growing_n64` | `growing` | 64 | 14.0 | 0.3675 | 0.9451 | 0.4977 | `fit` |
| `layered_cycle_8x8` | `layered_cycle` | 64 | 5.0 | 0.3348 | 0.9162 | 0.4928 | `fit` |
| `causal_dag_10x6` | `causal_dag` | 55 | 1.0 | `nan` | `nan` | 0.5438 | `degenerate` |
| `causal_dag_8x8` | `causal_dag` | 57 | 1.0 | `nan` | `nan` | 0.6235 | `degenerate` |

The runner asserts:

```text
[PASS] six configured families were evaluated
[PASS] fit labels match the live finite scout set
[PASS] degenerate labels match the live finite scout set
[PASS] all fitted rows have R^2 >= 0.90
[PASS] fitted beta spread exceeds 0.35
[PASS] all degenerate rows have non-finite beta and R^2
[PASS] all saturation readouts are finite
ASSERTIONS: PASS
```

## Boundary

This row claims only a finite-size topology scout: three nondegenerate fitted
rows have different beta values, and three configured rows are degenerate under
the runner's criteria. It does not claim a universality class, asymptotic
critical exponent, continuum limit, or effective retained status before
independent audit.

The archived stale note remains historical provenance only:
[`archive_unlanded/topology-stale-runners-2026-04-30/CRITICAL_EXPONENTS_TOPOLOGY_NOTE_2026-04-10.md`](../archive_unlanded/topology-stale-runners-2026-04-30/CRITICAL_EXPONENTS_TOPOLOGY_NOTE_2026-04-10.md).
