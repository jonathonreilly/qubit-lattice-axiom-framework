# Quark Route-2 Current-Projector Idempotence Support

**Date:** 2026-06-22
**Claim type:** bounded_support
**Actual current-surface status:** bounded-support for idempotent current-projector dichotomy
**Trace class:** upstream_support
**Runner:** `scripts/frontier_quark_route2_current_projector_idempotence_support_2026_06_22.py`

Actual current-surface status: bounded-support for idempotent current-projector dichotomy.

## Scope

Block69 showed that channel-respecting two-channel readouts leave `kappa`
free:

```text
R_phys(kappa) = F_adj + kappa F_singlet.
```

This block asks what happens if the readout must come from an exact current
projector.  It tests idempotence:

```text
P(kappa)^2 = P(kappa).
```

This is not an audit verdict.  It does not close the parent
[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
row.

## Exact Dichotomy

Normalize the adjoint coefficient to one.  The singlet coefficient is
`kappa`, so composing the channel map sends

```text
kappa -> kappa^2.
```

Projector idempotence is therefore

```text
kappa^2 = kappa
kappa(kappa - 1) = 0.
```

So idempotence narrows `kappa` to `{0,1}`.

The two exact endpoints are:

| Projector | `kappa` | `R_phys` | Route-2 `rho_E` under Block68 orientation |
|---|---:|---:|---:|
| Connected | `0` | `8/9` | `21/4` |
| Full trace | `1` | `1` | `4` |

idempotence alone does not choose the connected endpoint.  It prunes the
continuous selector family to a binary connected-versus-full choice.

## What Selects Connected

The connected endpoint is selected by either:

```text
P(singlet/disconnected channel) = 0
```

or by idempotence plus an exact strict singlet-suppression premise:

```text
0 <= kappa < 1.
```

Because the idempotent roots are only `0` and `1`, any exact bound excluding
the full-trace endpoint selects `kappa=0`.

The current Rconn packet has bounded OZI-size context, but not an exact
coefficient theorem excluding `kappa=1` as a physical current projector.

## Result

This block upgrades the shape of the remaining selector problem:

```text
continuous kappa family
```

narrows, under idempotence, to

```text
kappa in {0,1}.
```

The remaining missing theorem is no longer an arbitrary rational selector.  It
is an exact exclusion of the full-trace projector or an exact
singlet-annihilation theorem.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_current_projector_idempotence_support_2026_06_22.py
```

Expected result:

```text
TOTAL: PASS=36, FAIL=0
```
