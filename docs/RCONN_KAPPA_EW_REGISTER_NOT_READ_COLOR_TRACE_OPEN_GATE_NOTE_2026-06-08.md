# Rconn Kappa EW Register-Not-Read Color-Trace Open Gate

**Date:** 2026-06-08
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_rconn_kappa_ew_register_not_read.py`](../scripts/frontier_rconn_kappa_ew_register_not_read.py)
**Cached log:**
[`logs/runner-cache/frontier_rconn_kappa_ew_register_not_read.txt`](../logs/runner-cache/frontier_rconn_kappa_ew_register_not_read.txt)
(TOTAL: PASS=10 FAIL=0)

## Purpose

This note preserves the exact algebraic support behind a possible
`κ_EW = 0` route without claiming that the current framework already supplies
the route.

The retained no-go [`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md) establishes
the exact SU(`N_c`) Fierz adjoint fraction
`F_adj = (N_c^2 - 1)/N_c^2` (`= 8/9` at `N_c = 3`) but leaves the physical
EW-current readout selector free:

```text
R_phys(κ_EW) = F_adj + κ_EW(1 - F_adj),
κ_EW = 0 -> 8/9,    κ_EW = 1 -> 1.
```

The possible route is:

```text
If a future retained theorem proves that the register-not-read discipline
governs the color operator-trace channel, then the registered channel is the
traceless connected channel and κ_EW = 0.
```

That antecedent is not proved here and is not supplied by the Record axiom.
This note records the open gate and the exact algebra that makes the route
worth testing.

## Inputs

| Input | Source | Role |
|---|---|---|
| `R_phys = F_adj + κ_EW(1 - F_adj)` and the prior failed CMT/OZI selector routes | [`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md) | open selector left by the retained no-go |
| exact Fierz `S + C` channel decomposition and `F_adj = (N_c^2 - 1)/N_c^2` | [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md) | exact group-theory support |
| `N_c = 3` from spatial `d = 3` (`Z^3`) | [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`NATIVE_GAUGE_CLOSURE_NOTE`](NATIVE_GAUGE_CLOSURE_NOTE.md) | fixes the `8/9` specialization if the route closes |

No PDG value, fitted number, new axiom, new primitive, or Tier-A admission is
load-bearing in this note.

## Exact Algebraic Support

For a color matrix `G`, the SU(`N_c`) Fierz completeness identity gives

```text
Tr_color[G G^\dagger] =
  (1/N_c) |Tr G|^2 + 2 Σ_A |Tr[G t^A]|^2
  = S + C.
```

In the orthonormal operator basis `{I/sqrt(N_c), sqrt(2) t^A}`:

- `S = (1/N_c)|Tr G|^2` is exactly the `I/sqrt(N_c)` trace component.
- `C = 2 Σ_A |Tr[G t^A]|^2` is the traceless adjoint component.
- The channel-count fraction for the traceless component is
  `(N_c^2 - 1)/N_c^2 = F_adj`.

The runner verifies this decomposition for `N_c = 2, 3, 4, 5`, verifies that
the adjoint generators are traceless, verifies the `κ_EW = 0` and `κ_EW = 1`
algebra, and verifies the `N_c`-universal channel-count fraction.

## Open Gate

To close the route, a separate theorem must show that the framework's
register-not-read discipline applies to this color operator-trace split and
identifies the `I/sqrt(N_c)` trace channel as an unregistered reference rather
than registered readout content.

If that theorem is later retained or explicitly admitted, then:

```text
registered channel = traceless connected channel,
κ_EW = 0,
R_conn = F_adj = (N_c^2 - 1)/N_c^2.
```

At `N_c = 3`, this gives `R_conn = 8/9`.

## Boundary

This note does not establish:

- that Record supplies a color-trace readout context;
- that Record identifies arbitrary operator traces with registered outcomes;
- a weighting, normalization, probability, or measurement rule;
- the missing `κ_EW` selector as an unconditional theorem;
- the separate Route-2 `c_TE = -R_conn` bridge;
- the `ρ_E` readout;
- a retained status before independent audit.

It preserves a precise open route: exact Fierz trace/traceless algebra plus a
single missing color-trace register-not-read theorem.

## Command

```bash
python3 scripts/frontier_rconn_kappa_ew_register_not_read.py
```

Expected: `TOTAL: PASS=10 FAIL=0`.
