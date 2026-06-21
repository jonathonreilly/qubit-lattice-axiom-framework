# Quark Route-2 Source-Count Selector Bridge Boundary

**Date:** 2026-06-21
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Actual current-surface status:** exact-support / selector-boundary.
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict. Effective status remains owned by
the independent audit process after dependency closure.
**Primary runner:** [scripts/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.py](../scripts/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.py)
**Runner cache:** [logs/runner-cache/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.txt](../logs/runner-cache/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.txt)

## Scope

This note sharpens the Route-2 bridge target after the readout-map reduction.
It does not derive the readout triple

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).
```

The contribution is narrower:

1. The compressed bridge
   `c_TE = s_TE / kappa^2` can be written on the current source-count
   source surface as
   `c_TE = -N_pair^3 / N_color^2`.
2. At the current quark source counts `N_pair=2`, `N_color=3`, this is
   exactly the signed adjoint fraction:
   `-N_pair^3/N_color^2 = -8/9 = -F_adj`.
3. This equality is a sharp selector boundary, not a typed source/readout
   derivation. If the color route is physical, it still inherits the
   disconnected-channel selector from `RCONN_DERIVED_NOTE.md`.

So the remaining target is not "find another low rational." It is a typed
theorem saying that the Route-2 center ratio is the connected-color selector
specialization of the source-count bridge.

## One-hop authorities

| Authority | Role used here |
|---|---|
| [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) | Defines `q_T`, `q_E`, `s_TE`, `c_TE`, and the remaining `rho_E` readout entry |
| [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md) | Names the exact E-center lift and typed bridge residual |
| [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) | Establishes that carrier naturality does not select `rho_E` without an added source/readout input |
| [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md) | Names the missing typed edge from color support to the Route-2 center ratio |
| [CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md](CKM_A_SQUARED_BELOW_W2_Y_QUANTUM_CLOSURE_THEOREM_NOTE_2026-04-25.md) | Supplies the source-count read-off `N_pair=2`, `N_color=3` from `Q_L : (2,3)` |
| [CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md](CKM_MAGNITUDES_STRUCTURAL_COUNTS_THEOREM_NOTE_2026-04-25.md) | Supplies the structural-count surface `n_pair=2`, `n_color=3`, `n_quark=6` |
| [RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) | Supplies exact `F_adj=(N_c^2-1)/N_c^2` support and the unresolved physical disconnected-channel selector |

No observed masses, CKM/J target minimization, live endpoint fitting,
nearest-rational selection, or external numerical value is used.

## Exact source-count compression

Use the current quark source counts

```text
N_pair = 2,
N_color = 3,
kappa := N_color / N_pair = 3/2.
```

With the granted T-side shell orientation

```text
s_TE = gamma_T(shell)/gamma_E(shell) = -2 = -N_pair,
```

the compressed covariance bridge target becomes

```text
c_TE = s_TE / kappa^2
     = -N_pair / (N_color/N_pair)^2
     = -N_pair^3 / N_color^2
     = -8/9.
```

The exact adjoint fraction on the same `N_color=3` color surface is

```text
F_adj = (N_color^2 - 1) / N_color^2 = 8/9.
```

Therefore, at the current source counts,

```text
c_TE = s_TE / kappa^2 = -F_adj.
```

Equivalently, the equality is the integer identity

```text
N_pair^3 = N_color^2 - 1.
```

At `(N_pair, N_color) = (2, 3)`, both sides are `8`.

## Endpoint consequence if the typed selector is supplied

The Route-2 endpoint algebra gives

```text
q_T = 1 + (-1)/6 = 5/6,
c_TE = s_TE q_T / q_E.
```

If the typed bridge supplies

```text
c_TE = -F_adj = -8/9,
```

then exact arithmetic gives

```text
q_E = (-2)(5/6)/(-8/9) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

This is a conditional endpoint consequence. It is not a derivation of the
typed bridge itself.

## Selector boundary inherited from color readout

The color authority separates the exact Hilbert-space adjoint fraction from a
physical connected-current selector. In the notation used here, write the
one-parameter physical color readout as

```text
R_phys(xi) = F_adj + xi (1 - F_adj),       0 <= xi <= 1.
```

The connected specialization is `xi=0`; the full-trace specialization is
`xi=1`. If the Route-2 center ratio is typed as

```text
c_TE = -R_phys(xi),
```

then the endpoint readout becomes

```text
rho_E(xi) = 6( (-2)(5/6) / (-R_phys(xi)) - 1 ).
```

The target value is selected only at the connected specialization:

| selector | `R_phys` | `c_TE` | `rho_E` |
|---|---:|---:|---:|
| `xi=0` | `8/9` | `-8/9` | `21/4` |
| `xi=1/2` | `17/18` | `-17/18` | `78/17` |
| `xi=1` | `1` | `-1` | `4` |

Thus a physical color route to `rho_E=21/4` must supply the connected selector
in the Route-2 readout context. The exact source-count identity above shows
why the target is structurally well-posed; it does not select `xi=0`.

## Wrong-structure falsifiers

The exact equality is sensitive to the source-count and orientation data:

| Substitution | Result |
|---|---|
| current counts `(N_pair,N_color)=(2,3)` and `s_TE=-N_pair` | `c_TE=-8/9=-F_adj`, `rho_E=21/4` if typed |
| wrong color count `(2,4)` with `s_TE=-N_pair` | `c_TE=-1/2`, while `F_adj=15/16`; endpoint would give `rho_E=14` |
| wrong pair/color relation `(3,4)` with `s_TE=-N_pair` | `c_TE=-27/16`, while `F_adj=15/16` |
| wrong shell orientation `s_TE=-1` at current counts | `c_TE=-4/9`, not `-8/9` |
| no covariance normalization `kappa=1` | `c_TE=-2`, not `-8/9` |
| full-trace color selector `xi=1` | `rho_E=4`, not `21/4` |

The bridge is therefore not a pattern match to `8/9`; it depends on the
specific source-count identity, the granted shell orientation, and the
connected-selector specialization.

## What this retires

This retires a vague target statement:

```text
some color/readout bridge should produce -8/9.
```

The sharpened target is:

```text
derive a typed source/readout theorem identifying the Route-2 center ratio
c_TE with -R_phys(0), equivalently with s_TE/(N_color/N_pair)^2 at the
current quark source counts.
```

Any proof that keeps `xi` free or does not type the matter-count covariance
to the Route-2 center ratio remains support-only.

## Boundary

This note does not establish:

- `beta_E/alpha_E = 21/4` on the actual current surface;
- `q_E=15/8` on the actual current surface;
- the typed bridge `c_TE=-F_adj`;
- the physical connected-current selector `xi=0`;
- the T-side candidates;
- quark mass closure;
- any audit verdict.

It records exact support for a precise source-count selector target and the
remaining selector boundary.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.py
```

Expected final line:

```text
TOTAL: PASS=44, FAIL=0
```
