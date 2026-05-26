# SU(3) L_s=2 Cube Uniform-Pairing Shortcut No-Go

**Date:** 2026-05-03; narrowed 2026-05-26
**Claim type:** no_go
**Status:** bounded no-go for the uniform-pairing shortcut route.
**Runner:** [`scripts/frontier_su3_cube_index_graph_shortcut_open_gate.py`](../scripts/frontier_su3_cube_index_graph_shortcut_open_gate.py)

## Purpose

This row keeps the finite part of the L_s=2 cube shortcut calculation and
removes the broader bridge language. The useful result is a conditional
route no-go:

> even if the nontrivial cube trace is granted the uniform-pairing index-graph
> ansatz, the resulting Perron value is too small to close the bridge-support
> target.

This does not require proving that the actual SU(3) Wigner/intertwiner trace
equals the ansatz. It says that the ansatz route, by itself, is insufficient.

## Finite Shortcut Calculation

For the L_s=2 periodic cube skeleton:

```text
unique spatial plaquettes = 12
directed links = 24
cyclic index nodes = 48
index identifications = 48
connected components = 8
```

Under the uniform-pairing shortcut ansatz, the trace factor is

```text
T_lambda(candidate) = d_lambda^(N_components - N_links)
                    = d_lambda^(8 - 24)
                    = d_lambda^(-16).
```

The runner then forms the candidate boundary-character profile

```text
rho_candidate_(p,q)(6)
  = (d_(p,q) c_(p,q)(6) / c_(0,0)(6))^12 * d_(p,q)^(-16),
rho_candidate_(0,0)(6) = 1,
```

and inserts it into the existing finite source-sector Perron solve.

## No-Go Result

The runner computes

```text
rho_(1,0)(6) = rho_(0,1)(6) = 2.124624e-01
rho_(1,1)(6) = 5.587932e-03
P_candidate(6) = 0.4291049969
```

The comparison target declared for this route is

```text
P_target(6) = 0.5935306800,
epsilon_witness = 3.03e-4.
```

The gap is

```text
|P_target(6) - P_candidate(6)| = 0.1644256831,
```

which is more than five hundred times the witness scale. Therefore the
uniform-pairing shortcut cannot close the bridge target on this finite
calculation.

## Boundary

This row does not claim:

- that the actual SU(3) nontrivial cube Wigner/intertwiner trace equals
  `d_lambda^(-16)`;
- that the actual cube trace has been computed;
- that the source-sector bridge parent theorem closes;
- that the gauge-scalar temporal observable bridge is promoted;
- any new axiom or audit verdict.

Future work can still compute the actual Wigner/intertwiner traces. If they
disagree with the uniform-pairing ansatz, this row remains a no-go for the
shortcut route only. If they agree with the ansatz, this row says that route
still misses the bridge target.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_su3_cube_index_graph_shortcut_open_gate.py
```
