# Quark Route-2 Minimal Readout-Coupling Contract Support

**Date:** 2026-06-22
**Type:** exact-support / conditional minimal readout-coupling contract
**Actual current-surface status:** exact-support for a conditional contract; not current-surface closure
**Trace class:** upstream_support
**Primary runner:** [`scripts/frontier_quark_route2_minimal_readout_coupling_contract_support_2026_06_22.py`](../scripts/frontier_quark_route2_minimal_readout_coupling_contract_support_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_minimal_readout_coupling_contract_support_2026_06_22.txt`](../outputs/frontier_quark_route2_minimal_readout_coupling_contract_support_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Scope

Block121 supplies an endpoint-free internal source extension with:

```text
R_conn = 8/9,
kappa = 0.
```

Block122 prunes the shortcut that this internal source algebra alone identifies
the physical Route-2 `P_R/E-T` center-ratio readout. This block records the
minimal contract a future theorem must satisfy in order to consume Block121.

## Minimal Contract

Let `R_* = 8/9` be the internal connected fraction from the Block121 source
jet. A Route-2 readout-coupling theorem is sufficient exactly when it supplies:

```text
C1. internal_kappa_zero:
    Block121's source jet is the source being consumed.

C2. same_source_PR_ET:
    the physical finite P_R/E-T readout is typed as the same source/readout,
    not an external scalar comparator.

C3. channel_assignment:
    the E and T scalar outputs are assigned to the physical Route-2 channels
    before a scalar ratio is formed.

C4. mu_one:
    the physical center-ratio magnitude coupling is fixed to mu=1, so
    |c_TE| = R_* rather than mu R_*.

C5. sign_after_kappa:
    the endpoint orientation sign sigma=-1 is consumed only after the
    connected selector kappa=0 has been established.
```

Then:

```text
c_TE = sigma * mu * R_* = (-1) * 1 * (8/9) = -8/9.
```

No endpoint value is used as an input.

## Single-Clause Failure Models

The contract is intentionally minimal because each clause has a countermodel:

| Missing clause | Failure mode |
|---|---|
| `internal_kappa_zero` | no internal connected fraction is available to consume |
| `same_source_PR_ET` | Block121's source and the physical finite readout can be unrelated |
| `channel_assignment` | the scalar `E/T` ratio is not a typed Route-2 readout |
| `mu_one` | the same source jet permits `mu=9/8`, `mu=1/2`, or other endpoint-free couplings |
| `sign_after_kappa` | sign support can orient a magnitude only after that magnitude is typed |

Thus the contract is sufficient when all clauses hold, and every omitted clause
reopens the bridge.

## Result

This support packet turns the remaining hard primitive into a compact theorem
target:

```text
prove C1-C5 on the current Route-2 surface.
```

Until that happens, Block121 remains upstream support and Block122 remains the
active pruning result for the shortcut from internal source algebra alone to
the physical center-ratio bridge.

Expected runner result:

```text
TOTAL: PASS=70, FAIL=0
```
