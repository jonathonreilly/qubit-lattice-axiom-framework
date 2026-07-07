# Domain-Wall Edge Anomaly-Inflow Spectral Flow: Free-Field Bounded Theorem

**Date:** 2026-07-05
**Type:** bounded_theorem
**Claim scope:** finite free-field linear algebra with a non-dynamical
background `U(1)` field. The runner couples the record-time domain-wall
Hamiltonian to Peierls-link phases, inserts one magnetic flux quantum through
the transverse spatial torus, threads a twist through the remaining spatial
cycle, diagonalizes `H(phi)` on a flux grid, and counts zero crossings of
tracked localized edge levels. It checks a Callan-Harvey-style spectral-flow
pattern at the free-field background-field level. It does not derive, ratify,
or resolve the ABJ anomaly premise.
**Status authority:** independent audit lane only. This note does not set,
predict, or request an audit status.
**Primary runner:** [`scripts/domain_wall_edge_anomaly_inflow_spectral_flow_2026_07_05.py`](../scripts/domain_wall_edge_anomaly_inflow_spectral_flow_2026_07_05.py)
**Runner cache:** [`logs/runner-cache/domain_wall_edge_anomaly_inflow_spectral_flow_2026_07_05.txt`](../logs/runner-cache/domain_wall_edge_anomaly_inflow_spectral_flow_2026_07_05.txt)

## Source context

This note builds on the prior record-time domain-wall construction and uses the
same four-component Wilson-domain-wall diagnostic:

```text
H =
    K_x(A) Gamma_x + K_y(A) Gamma_y + sin(k_z) Gamma_z
  + K_s Gamma_s
  + [m(s) + L_x(A) + L_y(A) + L_s + (1 - cos(k_z))] Gamma_m.
```

The prior domain-wall edge note
[`DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md`](DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md)
and its runner supply the chirality operator
`chi_edge = i Gamma_s Gamma_m`, the mass-sign flip, the record-time
Hamiltonian form, and the localization-window method. The record-occupancy
front note
[`RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md`](RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md)
supplies only the conditional mass/occupancy-gradient-to-formation-arrow
bridge. The spectral-flow result of this note stands independently of that
formation-arrow interpretation.

The ABJ bridge
`ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`
is context only and remains unaudited on the current ledger. This note does
not consume it as authority. The finite check here is narrower: local wall and
anti-wall spectral flows are opposite in the background-field diagnostic, so
the closed record-time torus has zero net flow.

This is not a re-attack on
`A3_ROUTE3_ANOMALY_INFLOW_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r3.md`.
That note bounded anomaly inflow as a Brillouin-zone-corner distinguisher.
Here the question is different: whether the already-constructed domain-wall
edge has the expected local Callan-Harvey-style spectral flow under a
background gauge field.

The native anomaly-core notes
`ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18.md`
and `NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`
remain contextual only. They indicate where an abelian anomaly core would sit
on the left-handed `6 + 2` surface, but no hypercharge or Standard Model
content is assigned here.

## Background gauge field

For a three-dimensional Weyl edge, a pure twist of one spatial cycle gives
paired Weyl-cone branches. The anomaly spectral-flow diagnostic requires the
standard `E . B` handle: one background magnetic flux quantum through the
transverse `x-y` torus and a threaded twist `phi` along the `z` cycle. The
runner implements this with Peierls phases:

```text
U_y(x,y) = exp(i B x),
U_x(L_x - 1,y) = exp(-i B L_x y),
B = 2 pi / (L_x L_y).
```

The runner verifies that the summed plaquette phase is one flux quantum:

```text
sum_plaquette_phase = 6.283185307180 = 2 pi.
```

The threaded flux is represented by the shifted allowed momenta

```text
k_z(n, phi) = 2 pi (n + 0.31) / L_z - pi + phi / L_z  mod 2 pi,
```

with `phi in [0, 2 pi]`. For each `phi` and each `z` momentum, the runner
diagonalizes the actual finite matrix. It then follows the wall-localized and
anti-wall-localized edge states by eigenvector overlap, using the same
site-window localization method as the prior diagnostic.

## Computed checks

With `L_x = L_y = 3`, `N_s = 14`, `L_z = 7`, `M = +0.8`, sharp front, and one
magnetic flux quantum:

```text
wall flow      = +1
anti-wall flow = -1
net flow       = 0
bulk_gap_min   = 0.590028989858
```

The measured zero-crossing intervals are:

| sector | z | E(phi_j) -> E(phi_{j+1}) | k_z(phi_j) -> k_z(phi_{j+1}) | localization weight | edge chirality | sign |
|---|---:|---:|---:|---:|---:|---:|
| wall | 3 | `-0.042490753527 -> +0.022148477848` | `-0.042315329620 -> +0.021798806168` | `0.689764 -> 0.686201` | `+0.990621 -> +0.979238` | `+1` |
| anti-wall | 3 | `+0.042490753527 -> -0.022148477848` | `-0.042315329620 -> +0.021798806168` | `0.860121 -> 0.855437` | `-0.990621 -> -0.979238` | `-1` |

Thus the local wall and anti-wall flows are integer and opposite, and the
closed record-time torus has zero net flow.

The crossing states are edge states rather than bulk states:

- minimum crossing localization weight: `0.686201`;
- minimum crossing `|chi_edge|`: `0.979238`;
- minimum non-edge bulk gap over the flux grid: `0.590028989858`.

The near-zero tracked branch endpoints are printed by the runner. The branch
that crosses on the wall has

```text
E0 = -0.169803467570
Eend = +0.667991805447
min |E| = 0.022148477848
mean chi_edge = +0.992537
```

and the anti-wall partner has

```text
E0 = +0.169803467570
Eend = -0.667991805447
min |E| = 0.022148477848
mean chi_edge = -0.992537
```

## Chirality flip

The runner re-diagonalizes after flipping the mass orientation to `M = -0.8`.
It does not reuse or sign-edit the positive-orientation trajectories. The
measured flows reverse:

```text
M = +0.8: wall=+1, anti=-1
M = -0.8: wall=-1, anti=+1
```

For the flipped run, the wall crossing has negative measured edge chirality
and sign `-1`; the anti-wall crossing has positive measured edge chirality
and sign `+1`. This is the finite-matrix check that the flow sign tracks the
edge chirality. Conditional on the record-occupancy-front arrow identification,
this is also the expected formation-arrow sign tracking.

## Robustness

The integer count is stable under the requested small changes of record-time
lattice size and front width:

| `N_s` | `L_z` | front width | wall flow | anti-wall flow | net | bulk gap |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 5 | 0.00 | `+1` | `-1` | `0` | `0.627870321803` |
| 14 | 7 | 0.00 | `+1` | `-1` | `0` | `0.589795856227` |
| 14 | 7 | 0.45 | `+1` | `-1` | `0` | `0.621469648907` |
| 16 | 7 | 0.00 | `+1` | `-1` | `0` | `0.563638567662` |

The count is therefore stable across this finite free-field sweep and is not
a single-grid fine tuning.

## What is shown

At free-field level, with a non-dynamical background `U(1)` field:

- the record-time domain-wall edge carries an integer local spectral flow
  under one background flux quantum and a threaded twist;
- the wall and anti-wall flows are opposite, so the record-time torus has
  zero net flow;
- the flow sign tracks the measured edge chirality and reverses when the
  domain-wall chirality is flipped;
- the crossing states are localized on the wall/anti-wall;
- the non-edge bulk states remain gapped over the flux sweep.

This is a Callan-Harvey-style anomaly-inflow consistency pattern seen as
finite-matrix spectral flow. It does not spend or ratify the framework's ABJ
premise.

## What is not shown

- The gauge field is a non-dynamical background. No gauge kinetic term,
  gauge dynamics, or interaction is included.
- This is not a derivation, resolution, weakening, replacement, or
  ratification of the ABJ anomaly premise.
- This is not the Brillouin-zone-corner anomaly-inflow distinguisher question.
- No hypercharge map, Standard Model content assignment, or completion
  spectrum is supplied here.
- The dimensional interpretation of record-time as the domain-wall coordinate
  versus physical time is not resolved.
- No strong-CP or theta claim is made.
- No framework import, primitive, axiom, audit status, closure, exhaustion
  claim, only-route claim, or discharge claim is made.

Finite-volume note: on a closed torus the wall and anti-wall are both present,
so the global spectral flow is zero. The runner resolves the local wall and
anti-wall branches by the prior diagnostic's localization-window method after
each diagonalization. The reported local flows are therefore local edge spectral
flows; the global torus remains anomaly-neutral.

## Validation

Run:

```bash
python3 scripts/domain_wall_edge_anomaly_inflow_spectral_flow_2026_07_05.py
```

Observed terminal summary:

```text
TOTAL: PASS=12 FAIL=0
```
