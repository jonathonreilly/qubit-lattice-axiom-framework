# Quark Route-2 Full-Trace Exclusion No-Go

**Date:** 2026-06-22
**Claim type:** no_go
**Actual current-surface status:** no-go for exact full-trace exclusion from current projector/control premises
**Trace class:** negative_route_pruning
**Runner:** `scripts/frontier_quark_route2_full_trace_exclusion_no_go_2026_06_22.py`

Actual current-surface status: no-go for exact full-trace exclusion from current projector/control premises.

## Scope

Block70 reduced the connected-current selector to a binary idempotent choice:

```text
kappa in {0,1}.
```

This block asks whether the current exact controls exclude the `kappa=1`
full-trace endpoint.  They do not.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Exact Binary Pair

The two idempotent current projectors are:

| Projector | `kappa` | Singlet eigenvalue | `R_phys` | Route-2 `rho_E` |
|---|---:|---:|---:|---:|
| Connected | `0` | `0` | `8/9` | `21/4` |
| Full trace | `1` | `1` | `1` | `4` |

The connected endpoint is exactly the singlet-annihilating projector.  The
full-trace endpoint is exactly the projector that keeps the singlet channel.

## Controls Checked

The full-trace endpoint survives every current exact control used in this
stack:

| Control | Connected endpoint | Full-trace endpoint |
|---|---|---|
| Projector idempotence | admits | admits |
| Positivity | admits | admits |
| Channel-scalar form | admits | admits |
| Positive readout domain | admits | admits |
| Endpoint orientation sign | admits | admits |
| CMT scale invariance | admits | admits |
| Bounded OZI-size class | admits | admits |

So the current controls do not distinguish `kappa=0` from `kappa=1` as
admissible exact projectors.  They distinguish only the resulting Route-2
magnitude after an endpoint value is requested.

## Why Full-Trace Exclusion Is an Extra Premise

On the idempotent binary pair, all of the following statements select the
same endpoint:

```text
singlet eigenvalue = 0
0 <= singlet eigenvalue < 1
kappa != 1
rho_E = 21/4
```

The first three are singlet-sensitive readout premises.  The last one is the
target value and cannot be used as a proof input without fitting the selector.

Thus an exact full-trace exclusion is not a weaker consequence of
idempotence, positivity, S3 endpoint sign, CMT scaling, or bounded OZI-size
control.  It is equivalent to adding a singlet-annihilation theorem or an
exact disconnected-current-zero theorem.

## First-Principles Attack Frames

The runner records five attempted frames:

| Frame | Obstruction |
|---|---|
| Traceless color-generator frame | Selects adjoint only by changing the observable into a color-generator insertion. |
| Ward/conservation frame | Constrains total current conservation, not the disconnected-channel coefficient. |
| CMT/naturality frame | Scales adjoint and singlet channels uniformly. |
| Endpoint S3 frame | Fixes the sign once `q_E>0`, not the magnitude. |
| OZI frame | Bounds the singlet size class but leaves `kappa=1` allowed at `1/8`. |

These frames sharpen the remaining theorem target but do not derive it.

## Result

The direct full-trace exclusion route is blocked:

```text
idempotence
+ positivity
+ channel-scalar form
+ positive readout
+ endpoint orientation sign
+ CMT scale invariance
+ bounded OZI-size control
=> kappa != 1
```

is not a current-surface theorem.

The full-trace endpoint survives.  Selecting the connected endpoint still
requires a new exact singlet-annihilation theorem:

```text
P(singlet/disconnected channel) = 0.
```

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_full_trace_exclusion_no_go_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=50, FAIL=0
```
