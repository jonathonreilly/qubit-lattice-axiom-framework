# Quark Route-2 Log-Odds Selector Stretch No-Go

**Date:** 2026-06-22
**Type:** no-go / first-principles stretch attempt on the Route-2 bias selector
**Actual current-surface status:** no-go for the minimal RN/Fisher/same-record premise set selecting the Route-2 log-odds displacement
**Trace class:** negative_route_pruning
**Primary runner:** [`scripts/frontier_quark_route2_log_odds_selector_stretch_no_go_2026_06_22.py`](../scripts/frontier_quark_route2_log_odds_selector_stretch_no_go_2026_06_22.py)
**Cached output:** [`outputs/frontier_quark_route2_log_odds_selector_stretch_no_go_2026_06_22.txt`](../outputs/frontier_quark_route2_log_odds_selector_stretch_no_go_2026_06_22.txt)

This is not an audit verdict. It does not run audit workers and does not apply
audit outcomes.

## Stretch Target

Blocks102-105 reduce the Route-2 connected-cumulant endpoint route to a
single hard selector:

```text
select |h| = (1/2) log 2
```

in the two-outcome sharp-record RN chart. This block makes a first-principles
attempt to derive that selector from the minimal current premises rather than
only naming it.

## Minimal Premise Set

```text
A_min:
1. a typed same-source signed record epsilon in {-1,+1};
2. the normalized sharp-record RN chart mu_h(epsilon)
   = P0(epsilon) exp(h epsilon) / Z(h);
3. the Block102 binary same-record normal form;
4. the P-cal connected-cumulant subtraction once the same source is supplied.

Forbidden imports:
- endpoint value c_TE = -8/9;
- endpoint-value reversal through rho_E, beta_E/alpha_E, or readout fitting;
- fitted source-measure bias;
- observed or comparator target values.
```

## Result

The stretch attempt does not derive the selector. The minimal premises give a
one-parameter orbit

```text
q = exp(2h) > 0,
E_h[epsilon] = (q-1)/(q+1).
```

The connected-cumulant condition `kappa=0` selects the two-point orbit

```text
q in {2, 1/2}
```

equivalently `|h| = (1/2) log 2`. But the allowed RN/Fisher structure treats
all positive `q` as valid sharp-record source laws. Normalization, unit Fisher
tangent at the origin, cumulant/Mobius connectedness, and sign inversion
`h -> -h` do not distinguish `q=2` from any other nonzero source
displacement.

## Fan-Out Synthesis

| Frame | Attempt | Result | Missing primitive |
|---|---|---|---|
| Symmetry | Use sign inversion `h -> -h` | Gives a paired orbit, not its magnitude | Route-2 magnitude selector |
| Unit tangent | Use Fisher unit score at `h=0` | Fixes local scale, not finite displacement | Route-2 finite source field |
| Cumulant | Use connected subtraction | Computes `1 - m^2` after `m` is known | Route-2 one-point bias |
| P_R readout | Pull bias from exact four-slot readout | Provides labels/readout, not a probability law | Route-2 source/readout typing |
| RN chart | Use exponential family structure | Admits every positive log-odds `q` | Route-2 log-odds selector |

## Refined Missing Primitive

```text
Route-2 log-odds selector theorem:

from the physical Route-2 source/readout structure, construct the same-source
signed record and prove that its sharp-record RN source law has log-odds
|h| = (1/2) log 2, equivalently q = exp(2|h|) = 2, without using endpoint
values or fitted source weights.
```

No endpoint value is used.

Expected runner result:

```text
TOTAL: PASS=80, FAIL=0
```
