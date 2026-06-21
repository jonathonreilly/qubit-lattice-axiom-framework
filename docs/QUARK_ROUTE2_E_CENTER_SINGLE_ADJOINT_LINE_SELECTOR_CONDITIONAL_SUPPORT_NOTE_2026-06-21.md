# Route-2 E-Center Single-Adjoint-Line Selector: Conditional Support and the Exact Primitive That Would Force 21/4

**Date:** 2026-06-21
**Claim type:** conditional support / source-primitive map
**actual_current_surface_status:** conditional-support
**trace_class:** upstream_support
**reachability_to_target:** supports
**conditional_surface_status:** conditional on an accepted single-adjoint-line source selector
**hypothetical_axiom_status:** single-adjoint-line source selector absent from the current source bank
**proposal_allowed:** false
**Status authority:** branch-local physics-loop artifact only. This note writes no audit verdict, does not retag any ledger row, and does not update repo-wide authority surfaces.
**Primary runner:** [`scripts/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.py`](../scripts/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.py) (`PASS=27 FAIL=0`)
**Runner output:** [`outputs/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.txt`](../outputs/frontier_quark_route2_e_center_single_adjoint_line_selector_conditional_2026_06_21.txt)

## Question

The S3/Route-2 readout gate has reduced the remaining endpoint problem to the E-side entry

```text
rho_E := beta_E/alpha_E = 21/4,
q_E = 1 + rho_E/6 = 15/8.
```

Prior no-gos show that shell normalization, T-side endpoint data, channel preservation, low-rational filters, Rconn/Fierz support, and E-center-blind constraints do not select `rho_E`. The open escape clause is therefore precise: add an E-center endpoint ratio, source-domain rule, or stronger readout-map primitive.

This note tests one such primitive:

```text
single-adjoint-line source selector:
  the source domain supplies one typed line in the SU(3) adjoint space,
  and the E-center excess reads the normalized complement rank.
```

This is not claimed to be present on the current source bank. The point is to identify exactly what kind of primitive would work, and what it would force.

## Conditional Arithmetic

For SU(3),

```text
dim(adj) = 8.
```

If a typed source selector supplies one distinguished adjoint line, then its complement has rank

```text
8 - 1 = 7.
```

Reading the E-center excess as normalized complement rank gives

```text
e_E = 7/8.
```

The Route-2 center denominator is already fixed by the endpoint carrier:

```text
q_E = 1 + rho_E/6.
```

So the conditional single-line complement primitive gives

```text
rho_E = 6 e_E = 6 * 7/8 = 21/4,
q_E = 1 + e_E = 15/8.
```

With the granted T-side values `q_T=5/6` and shell `T/E=-2`,

```text
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

Thus the same primitive also recovers the signed center ratio targeted by the Rconn bridge:

```text
gamma_T(center)/gamma_E(center) = -8/9.
```

The magnitude `8/9` equals the SU(3) adjoint channel fraction `F_adj=(N_c^2-1)/N_c^2` at `N_c=3`, but the E-excess itself is `7/8`. This distinction matters: directly reading `F_adj=8/9` as the E-excess gives the wrong Route-2 endpoint.

## Uniqueness Among Integer-Rank Adjoint Projectors

For an integer-rank adjoint projector of rank `k`, the same complement-rank readout would give

```text
e_E = k/8,
q_E = 1 + k/8,
rho_E = 6k/8 = 3k/4.
```

The runner enumerates `k=0..8`. The target is reached only at

```text
k = 7.
```

So if the selector is required to be an adjoint projector-rank readout, the primitive is sharply constrained: it must be a codimension-one adjoint complement. Reading the selected line itself (`k=1`), the full adjoint (`k=8`), or `F_adj=8/9` directly as the E-excess all fail.

## Current-Surface Firewall

This packet does not assert that the current source bank supplies a single-adjoint-line selector. It does not derive the line from Record/Quantum, Rconn, Fierz algebra, Route-2 endpoint algebra, or measured calibration.

The current source-domain bridge note says the typed edge from `R_conn=8/9` to the Route-2 signed center ratio is absent. The E-center blindness note says a positive repair must supply information that evaluates the E-center column. This conditional primitive would supply such information, but it is an additional source selector, not a consequence of the existing bank.

## What This Adds

This block narrows the positive target from a vague "source/readout primitive" to a concrete falsifiable primitive:

```text
Does the framework have a typed source-domain reason to select one adjoint line,
and to read the E-center excess as the complement rank?
```

If yes, the Route-2 E-side value follows exactly. If no, this conditional support stays outside the actual current surface.

## Falsifiers

The primitive fails if any of these is true:

- no source-domain structure selects a single adjoint line;
- the E-center readout is the line itself rather than the complement;
- the readout uses the full adjoint fraction `8/9` as the E-excess;
- the selected line is arbitrary or fitted to the endpoint target rather than typed by source geometry;
- the source rule is not allowed as a Route-2 readout-map primitive.

## Load-Bearing Inputs

- [`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) - owner of the open Route-2 endpoint triple.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) - endpoint algebra and `q_E = 1 + (beta_E/alpha_E)/6`.
- [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) - current-surface freedom of `rho_E` without an E-center/source/readout primitive.
- [`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md`](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md) - E-center-blind constraints cannot select `rho_E`.
- [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) - current typed bank lacks the Rconn-to-center-ratio bridge.
- [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md) - exact `F_adj=8/9` support, used here only as a comparator for the center-ratio magnitude.

## Forbidden-Imports Check

No observed masses, fitted Yukawa values, CKM/J target minimization, PDG values, nearest-rational selection, measured-calibration fitting, or literature values are used. The conditional proof uses only exact integer dimensions, exact Route-2 endpoint algebra, and the explicitly introduced single-line source selector.

## Status

This is conditional support. It is useful because it identifies an exact primitive that would force the missing E-side entry and gives falsifiers for that primitive. It is not actual current-surface closure.
