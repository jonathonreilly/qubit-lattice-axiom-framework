---
claim_id: quark_route2_rconn_magnitude_sign_split_exact_support_note_2026-06-21
claim_type: exact-support
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
---

# Route-2 Rconn Magnitude/Sign Split Exact Support Note

**Date:** 2026-06-21
**Runner:** `scripts/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.py`
**Output:** `outputs/frontier_quark_route2_rconn_magnitude_sign_split_2026_06_21.txt`
**Status:** exact support for a conditional sign-reduction theorem; not an endpoint derivation.

## Scope

This note narrows the Route-2 color/readout residual.  Previous packets named
the missing signed bridge

```text
R_conn = 8/9 ?=> c_TE := gamma_T(center)/gamma_E(center) = -8/9.
```

The current support bank does not derive that typed bridge.  The sharper split
is:

```text
typed magnitude bridge: |c_TE| = R_conn = 8/9
sign selection: q_E > 0 forces c_TE < 0.
```

So, once a typed magnitude bridge is supplied, the sign is no longer an
independent import.  The open blocker becomes the typed magnitude bridge from
the SU(3) color scalar into the Route-2 center T/E readout ratio.  This is not
a derivation of the endpoint triple; it is not a derivation of the typed magnitude bridge.

## Authority Surface

The exact readout-map note gives the endpoint algebra

```text
q_T   := gamma_T(center) / gamma_T(shell)
q_E   := gamma_E(center) / gamma_E(shell)
s_TE  := gamma_T(shell) / gamma_E(shell)
c_TE  := gamma_T(center) / gamma_E(center) = s_TE q_T / q_E.
```

The active Route-2 stretch premise grants

```text
q_T = 5/6,       s_TE = -2.
```

The repaired `R_conn` note preserves only the exact color fraction

```text
F_adj = (N_c^2 - 1)/N_c^2 = 8/9 at N_c = 3,
```

not an unconditional physical/readout selector.  The source-domain bridge
no-go records that color projection by itself does not supply the sign or the
endpoint orientation.  The registration/positivity no-go records that
positivity gives only the one-sided Route-2 bound

```text
rho_E > -6.
```

Because `q_E = 1 + rho_E/6`, this is exactly the same sign-domain statement as

```text
q_E > 0.
```

## Theorem

Let

```text
c_TE = s_TE q_T / q_E.
```

With `s_TE = -2` and `q_T = 5/6`,

```text
s_TE q_T = -5/3.
```

Therefore, for every positivity-admissible `q_E > 0`,

```text
c_TE = (-5/3) / q_E < 0.
```

If a typed magnitude bridge supplies

```text
|c_TE| = R_conn = 8/9,
```

then positivity removes the positive branch and forces

```text
c_TE = -8/9.
```

The endpoint algebra then gives

```text
q_E = (-2)(5/6)/(-8/9) = 15/8,
rho_E = 6(q_E - 1) = 6(15/8 - 1) = 21/4.
```

So the exact conditional chain is:

```text
typed |center T/E| = R_conn  plus  q_E > 0
    => center T/E = -R_conn
    => q_E = 15/8
    => rho_E = 21/4.
```

## Branch Table

| Supplied center condition | q_E | rho_E | Positivity |
|---|---:|---:|---|
| `c_TE = -8/9` | `15/8` | `21/4` | passes |
| `c_TE = +8/9` | `-15/8` | `-69/4` | fails `q_E > 0` and `rho_E > -6` |
| `|c_TE| = 8/9` without positivity | two branches | two branches | ambiguous |
| positivity without `|c_TE| = 8/9` | continuum | continuum | does not select `rho_E` |

This table explains why the earlier source-domain statement had to demand a
signed bridge.  With positivity included, the sign can be discharged, but the
magnitude remains open.

## What Remains Open

The current support bank still has no typed edge

```text
SU(3) color fraction F_adj = 8/9
    -> |gamma_T(center)/gamma_E(center)| = 8/9.
```

An untyped scalar equality is not enough.  The needed theorem must identify the
SU(3) color projection with the Route-2 support/readout center ratio, or prove
an equivalent source-domain relation.  Until that bridge is supplied, the
endpoint triple remains support-only:

```text
(-1, -2, 21/4)
```

is exact after the magnitude bridge and positivity, but not derived from the
current bank.

## Wrong-Structure Falsifiers

The sign split keeps the same load-bearing controls as the bounded E-center
attempt.

| Substitution | Exact consequence |
|---|---|
| Correct denominator `6`, `N_c=3`, magnitude `8/9`, positivity | `q_E=15/8`, `rho_E=21/4` |
| Wrong color count `N_c=2`, denominator `6` | `q_E=20/9`, `rho_E=22/3` |
| Wrong center-excess denominator `5`, `N_c=3` | `q_E=9/5`, `rho_E=4` |
| Wrong center-excess denominator `12`, `N_c=3` | `q_E=33/16`, `rho_E=51/4` |
| Positivity alone with no magnitude bridge | many positive `q_E`; no selected endpoint |

## Claim Status

Actual current surface status: `exact-support`.

Trace class: `upstream_support`.

Reachability: `supports` the S3/Route-2 readout endpoint target by reducing
one open bridge.  It does not close the readout endpoint target, does not apply
an audit verdict, and does not introduce a new axiom.

Open import after this note:

```text
typed magnitude bridge |gamma_T(center)/gamma_E(center)| = R_conn.
```

## Runner Certificate

The paired runner checks:

- exact rational endpoint arithmetic;
- branch splitting for `c_TE = +/- 8/9`;
- equivalence of `rho_E > -6` and `q_E > 0`;
- that positivity forces the negative center-ratio sign;
- that positivity alone leaves a continuum;
- wrong-structure falsifiers for `N_c` and the center-excess denominator;
- the absence of the magnitude bridge in the local typed-edge inventory; and
- authority anchors in the current Route-2 and `R_conn` notes.

Expected local certificate:

```text
TOTAL: PASS=52 FAIL=0
```
