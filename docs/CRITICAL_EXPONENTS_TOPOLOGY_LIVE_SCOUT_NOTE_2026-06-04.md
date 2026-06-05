# Critical Exponents Topology Live Scout Note

**Date:** 2026-06-04
**Status:** bounded-support finite-size scout; independent audit required before any effective status change
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_critical_exponents.py`](../scripts/frontier_critical_exponents.py)
**Cached runner output:** [`logs/runner-cache/frontier_critical_exponents.txt`](../logs/runner-cache/frontier_critical_exponents.txt)

## Scope

This note repairs the live, reauditable surface for the archived
`critical_exponents_topology_note_2026-04-10` row. It does not unarchive the
old note, edit the audit ledger, or restore the stale table. It records the
current runner output and the assertions now enforced by the runner.

The scope is a finite-size scout over six configured graph representatives:

- `random_geometric_s8`
- `random_geometric_s10`
- `growing_n64`
- `layered_cycle_8x8`
- `causal_dag_10x6`
- `causal_dag_8x8`

No multi-size scaling collapse, multi-seed robustness theorem, universal
critical exponent, or new universality class is claimed.

## Live Runner Table

```text
Family                    base                   n   G_crit     beta      R^2  phi_sat       status
----------------------------------------------------------------------
random_geometric_s8       random_geometric      64      1.0      nan      nan   0.4128   degenerate
random_geometric_s10      random_geometric     100      2.0   0.7328   0.9656   0.3894          fit
growing_n64               growing               64     14.0   0.3675   0.9451   0.4977          fit
layered_cycle_8x8         layered_cycle         64      5.0   0.3348   0.9162   0.4928          fit
causal_dag_10x6           causal_dag            55      1.0      nan      nan   0.5438   degenerate
causal_dag_8x8            causal_dag            57      1.0      nan      nan   0.6235   degenerate
```

## Assertion Surface

The runner now asserts the current finite scout criteria:

```text
SAFE READ
  [PASS] six configured families were evaluated
  [PASS] fit labels match the live finite scout set
  [PASS] degenerate labels match the live finite scout set
  [PASS] all fitted rows have R^2 >= 0.90
  [PASS] fitted beta spread exceeds 0.35
  [PASS] all degenerate rows have non-finite beta and R^2
  [PASS] all saturation readouts are finite
  finite-size scout only: no universality class or asymptotic exponent claim
ASSERTIONS: PASS
```

## Safe Read

The live bounded statement is:

> In this finite configured scout, three graph representatives have admissible
> onset fits with fitted `beta` values `0.7328`, `0.3675`, and `0.3348`, while
> three representatives are degenerate under the same acceptance criterion.
> The fitted beta spread is evidence that topology affects this finite-size
> onset diagnostic.

This is not evidence by itself for an asymptotic universality class. The
degenerate rows are explicitly excluded from positive exponent evidence.

## Boundaries

This packet does not claim:

- the archived 2026-04-10 table;
- six fitted topology rows;
- universality-class discovery;
- asymptotic critical exponents;
- multi-seed robustness;
- finite-size scaling collapse;
- an audit-derived effective status before independent audit.
