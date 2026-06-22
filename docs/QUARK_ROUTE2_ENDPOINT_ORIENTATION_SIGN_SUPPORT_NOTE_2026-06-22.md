# Quark Route-2 Endpoint Orientation Sign Support

**Date:** 2026-06-22
**Claim type:** bounded_support
**Actual current-surface status:** conditional-support for endpoint orientation sign
**Trace class:** upstream_support
**Runner:** `scripts/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.py`

Actual current-surface status: conditional-support for endpoint orientation sign.

## Scope

Block67 factorized the typed bridge

```text
c_TE = -R_conn
```

into two switches:

```text
c_TE = sigma * R_phys(kappa).
```

This block checks whether the orientation sign `sigma=-1` is independent, or
whether it is already conditionally supplied by the Route-2 endpoint
orientation.

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Exact Sign Algebra

The Route-2 endpoint algebra is

```text
c_TE = gamma_T(center)/gamma_E(center) = s_TE * q_T / q_E.
```

Under the conditional T-side values

```text
s_TE = gamma_T(shell)/gamma_E(shell) = -2
q_T = 5/6 > 0
```

and a positive E-center readout `q_E > 0`, the sign is forced:

```text
sign(c_TE)=sign(shell T/E)=-1.
```

At the target point,

```text
q_E = 15/8
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So the minus sign is conditional endpoint-orientation support, not an
independent color-domain theorem.

## Magnitude Remains Open

The sign result does not derive the magnitude.  With the oriented Rconn ansatz

```text
c_TE = -R_phys(kappa)
R_phys(kappa) = F_adj + kappa(1 - F_adj),
```

the endpoint algebra gives:

| `kappa` | `c_TE` | `q_E` | `rho_E` |
|---:|---:|---:|---:|
| `0` | `-8/9` | `15/8` | `21/4` |
| `1/2` | `-17/18` | `30/17` | `78/17` |
| `1` | `-1` | `5/3` | `4` |

Thus the remaining exact bridge target is the connected selector `kappa=0`,
or an equivalent theorem forcing `|c_TE|=8/9`.

## Result

This block narrows Block67:

```text
sigma=-1
```

is conditionally supported by endpoint orientation once `s_TE=-2`, `q_T>0`,
and `q_E>0` are admitted.

The endpoint triple is still open because the magnitude remains open:

```text
kappa=0
```

has not been derived by the current Rconn packet.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=38, FAIL=0
```
