# Quark Route-2 Local-Current Singlet-Annihilation No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for singlet annihilation from local-current premises
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_local_current_singlet_annihilation_no_go_2026_06_22.py`

Actual current-surface status: no-go for singlet annihilation from local-current premises.

## Scope

After Blocks69-72, the remaining selector theorem can be written as:

```text
kappa = 0.
```

Equivalently:

```text
P(singlet/disconnected channel) = 0.
```

This block asks whether locality of the lattice current, Ward normalization,
color-singlet form, CMT scaling, or finite OZI-size control forces that
singlet-annihilation statement.  They do not.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Premise Split

There are two different objects:

| Object | `kappa` | Role |
|---|---:|---|
| Local full current | `1` | Direct local color-scalar current readout retaining the singlet channel. |
| Connected cumulant | `0` | Disconnected-subtraction readout that annihilates the singlet channel. |

The connected endpoint is exactly the connected-cumulant premise.  It is not
the same statement as locality of the bare current.

## Local-Current Controls

The full-trace endpoint satisfies the local-current controls checked here:

| Control | Full trace `kappa=1` |
|---|---|
| Site-local current form | admits |
| Ward normalization | admits |
| Color-singlet observable | admits |
| CMT scale invariance | admits |
| Finite OZI-size class | admits |

Thus local full current remains admitted.  These controls do not imply
`kappa=0`.

## What Does Select `kappa=0`

The connected-cumulant premise:

```text
read the connected two-point function
```

or equivalently:

```text
subtract the disconnected/singlet channel exactly
```

does select `kappa=0`.  But that is the missing readout premise itself.  It is
not derived from local-current locality or Ward normalization in this block.

## Stuck Fan-Out

| Frame | Result |
|---|---|
| Site-locality | Local full current remains admitted. |
| Ward identity | Normalizes the current but leaves disconnected coefficient free. |
| Color-singlet EW current | Supports full trace as a direct local color-scalar current. |
| Cluster/cumulant | Selects connected only by adding disconnected subtraction. |
| OZI suppression | Bounds singlet size but does not give exact zero. |

All five frames hit the same wall: exact zero is a connected-subtraction
statement.

## Route-2 Consequence

With the oriented Route-2 chain:

```text
R_phys(kappa) = 8/9 + kappa/9
q_E = (5/3) / R_phys(kappa)
rho_E = 6(q_E - 1),
```

the endpoints are:

| Readout | `kappa` | `rho_E` |
|---|---:|---:|
| Connected cumulant | `0` | `21/4` |
| Bounded subtracted current | `1/2` | `78/17` |
| Local full current | `1` | `4` |

The target endpoint is exactly the connected-cumulant endpoint, but selecting
it requires the connected-cumulant premise.

## Result

The direct local-current route is blocked:

```text
local lattice current
+ Ward normalization
+ color-singlet form
+ CMT scale invariance
+ finite OZI-size control
=> singlet annihilation
```

is not a current-surface theorem.

The remaining positive target is unchanged but sharper:

```text
derive exact disconnected-current subtraction as the physical Route-2 readout,
or derive the same `kappa=0` selector from another typed source-domain theorem.
```

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_local_current_singlet_annihilation_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=44, FAIL=0
```
