# Quark Route-2 Source-Domain Magnitude Typecast Equivalence No-Go

**Date:** 2026-06-21
**Status:** exact negative boundary / magnitude-typecast no-go
**Runner:** `scripts/frontier_quark_route2_source_domain_magnitude_typecast_equivalence_no_go_2026_06_21.py`
**Primary parents:**
`ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md`,
`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`,
`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`,
`RCONN_DERIVED_NOTE.md`,
`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`

## Scope

This note tests whether the remaining source-domain target can be weakened
from a typed Route-2 readout edge to a scalar magnitude condition.

It cannot. In the positive-lift family, the magnitude condition

```text
|c_TE| = F_adj
```

is not a weaker scalar condition. It is exactly the E-center readout selection
written in magnitude form, unless a separate source-domain theorem types that
magnitude into the Route-2 center ratio.

This note does not supply a typed source-domain theorem. It records the
equivalence and the resulting no-go for magnitude-only repairs.

## Magnitude equivalence

In the positive-lift family,

```text
rho_E > -6,
q_E = 1 + rho_E / 6 > 0.
```

The granted T-side values are

```text
q_T = 5/6,
s_TE = -2.
```

Therefore

```text
c_TE = s_TE q_T / q_E = (-5/3) / q_E
```

and the magnitude is

```text
|c_TE| = (5/3) / q_E.
```

Solving for the readout entry gives the exact inverse

```text
rho_E = 10 / |c_TE| - 6.
```

So every positive magnitude choice selects exactly one `rho_E`.

## Typecast no-go

At `N_c = 3`, the color-domain support gives

```text
F_adj = (N_c^2 - 1) / N_c^2 = 8/9.
```

Substituting that magnitude into the inverse gives

```text
rho_E = 10 / (8/9) - 6 = 21/4.
```

Equivalently,

```text
|c_TE| = F_adj
```

inside the positive-lift family is already the missing E-center readout
selection. It does not reduce the problem unless a future positive theorem
supplies the source-domain typecast

```text
scalar magnitude 8/9 -> Route-2 |c_TE|
```

or lands directly in one of

```text
route2_center_TE_minus_8_9
route2_q_E_15_8
route2_rho_E_21_4.
```

The magnitude/typecast equality is the missing selection.

## Candidate Magnitudes

The runner checks several exact magnitudes. Each one selects its own E-center
readout entry:

| Magnitude | Selected `rho_E` |
|---:|---:|
| `F_adj` at `N_c=2` = `3/4` | `22/3` |
| `F_adj` at `N_c=3` = `8/9` | `21/4` |
| `F_adj` at `N_c=4` = `15/16` | `14/3` |
| `1` | `4` |
| `5/6` | `6` |

This shows why a scalar magnitude needs a typed source theorem. Picking the
`N_c=3` magnitude is exactly picking one member of the E-center readout family.

## Handoff

The next useful positive target is not "find `8/9` again." The repo already
has color-domain `F_adj = 8/9` support. The future positive theorem must source
the magnitude/typecast equality:

```text
|c_TE| = F_adj
```

as a Route-2 readout statement, or directly supply a typed readout landing edge.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_magnitude_typecast_equivalence_no_go_2026_06_21.py
```

Expected branch result:

```text
TOTAL: PASS=33, FAIL=0
VERDICT: |c_TE|=F_adj is equivalent to E-center readout selection unless independently typed.
```
