# Quark Route-2 Lift Coordinate Selector Gate Note

**Date:** 2026-06-21
**Status:** no-go / coordinate-selector boundary.
**Primary runner:** `scripts/frontier_quark_route2_lift_coordinate_selector_gate_2026_06_21.py`
**Output:** `outputs/frontier_quark_route2_lift_coordinate_selector_gate_2026_06_21.txt`

## Claim Boundary

The current Route-2 stack already isolates a tempting exact value:

```text
kappa = w_T / w_E = (1/2) / (1/3) = 3/2,
kappa^2 = 9/4.
```

With the granted T-side lift

```text
q_T = 5/6,
```

the endpoint target follows if the inverse-square channel ratio acts on the
multiplicative lift coordinate:

```text
q_E = q_T kappa^2 = (5/6)(9/4) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

This block asks whether the current bank supplies the missing coordinate
selector: why the inverse-square ratio should act on `q_X`, rather than on
the additive slope `rho_X` or the source increment `q_X - 1`.

## Result

It does not. The value `9/4` is present, but the coordinate selector is not.

The obstruction is exact:

| Coordinate receiving the `9/4` ratio | E lift | E slope |
|---|---:|---:|
| multiplicative lift `q_X` | `15/8` | `21/4` |
| increment `q_X - 1` | `5/8` | `-9/4` |
| additive slope `rho_X` | `5/8` | `-9/4` |
| inverse lift `q_T / (9/4)` | `10/27` | `-34/9` |

All of these are exact T-calibrated coordinate maps. Only the first gives the
target. Therefore the endpoint does not follow from the inverse-square value
alone; it follows only after selecting the multiplicative lift coordinate.

## Source/Readout Boundary

The current readout algebra exposes the E-center unknown additively:

```text
q_E = 1 + rho_E / 6,
rho_E = beta_E / alpha_E.
```

The current source carrier is also additive in the center-excess slot:

```text
K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T).
```

Those surfaces do not supply a theorem saying that channel weights scale
`q_X` multiplicatively. The existing Schur quadratic no-go already states the
same sharp gap from the symmetry side: `lambda = q_E/q_T = kappa^2` is
equivalent to an inverse-square lift law, but no named functional produces
that law.

## Current-Surface Firewall

This block does not close the parent endpoint triple. It narrows the positive
target to the exact missing coordinate selector:

```text
derive that the selected inverse-square channel weight scales q_X itself,
not rho_X and not q_X - 1.
```

Equivalently, a future proof must supply a typed multiplicative-lift readout
law. Reusing the value `9/4` without this coordinate theorem is an import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_lift_coordinate_selector_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=31, FAIL=0
```
