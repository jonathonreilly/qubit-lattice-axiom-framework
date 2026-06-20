# Emergent Lorentz Velocity RG Exchange-Matrix Exact Support

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Type:** exact support theorem / upstream support
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_velocity_rg_exchange_matrix_2026_06_18.py`](../scripts/frontier_emergent_lorentz_velocity_rg_exchange_matrix_2026_06_18.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_velocity_rg_exchange_matrix_2026_06_18.txt`](../logs/runner-cache/frontier_emergent_lorentz_velocity_rg_exchange_matrix_2026_06_18.txt)

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "Exact exchange-matrix support for the one-loop velocity-RG form; physical one-loop coefficients and LV-bound sufficiency remain open."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This proves the exchange-matrix algebra for any positive mutual-drag coefficients. It does not derive the physical one-loop coefficients from framework interactions."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target And Blocker

This note targets the conditional row
`emergent_lorentz_interacting_velocity_rg_attractor_note_2026-06-06`.
The current audit repair text asks for retained one-hop authorities deriving:

```text
the framework-specific one-loop velocity RG, the spatial-only power-divergent
mixing coefficient, and the physical anomalous dimension/sufficiency comparison
against LV bounds.
```

This source note addresses only the first item's algebraic core: the exact
exchange matrix behind the supplied one-loop velocity RG. It does not derive
the physical loop coefficients, the spatial-only power-divergent coefficient,
the fixed-point anomalous dimension, or LV-bound sufficiency.

## Statement

Let `v_F` and `v_B` be the fermion and boson limiting speeds in a two-sector
interacting packet. Suppose the one-loop speed flow has the following
exchange properties:

1. the common-speed line `v_F = v_B` is fixed;
2. the flow is linear in the speed mismatch at the one-loop order under test;
3. each sector is dragged toward the other with positive coefficients `a,b > 0`;
4. there is no independent common-speed source term in this subproblem.

Then the beta function is forced to be

```text
d/dl [v_F] = [-a   a] [v_F]
     [v_B]   [ b  -b] [v_B],
```

equivalently

```text
dv_F/dl = a (v_B - v_F),
dv_B/dl = b (v_F - v_B).
```

The common-speed vector `(1,1)` is the zero mode. The weighted common speed
`b v_F + a v_B` is invariant. The only nonzero eigenvalue is `-(a+b)`.
Therefore

```text
d(v_F - v_B)/dl = -(a+b) (v_F - v_B),
```

so the speed-difference mode is IR-attractive for every positive pair `a,b`.
For the speed ratio `eta = v_F/v_B` with `v_B > 0`,

```text
d eta/dl = -(eta - 1)(a + b eta),
```

so every positive `eta != 1` flows toward `eta = 1`.

## What This Retires

This retires the purely algebraic import hidden in the parent packet's phrase
"supplied one-loop velocity RG form." Once a framework-specific one-loop
calculation supplies positive mutual-drag coefficients `a,b`, the attraction
claim no longer needs a literature analogy or numerical sample: the exact
matrix proves the fixed line, invariant weighted speed, and attractive
difference eigenmode.

The parent note's earlier numerical runner checked one sample packet. This note
turns that sample into a parameter-free exact theorem over all positive
coefficients.

## What Remains Open

This note does not derive the physical one-loop coefficients `a,b` from the
framework's actual interacting matter/gauge vertices. It does not show that the
coefficients are positive on the physical sector. It does not compute the
spatial-only power-divergent coefficient, the fixed-point anomalous dimension,
or the LV-bound sufficiency inequality.

The remaining bridge is therefore sharper:

```text
derive the framework's interacting vertices and one-loop counterterm, prove
that they instantiate positive a,b in this exact exchange matrix, then combine
that with the spatial mixing coefficient and LV-bound comparison.
```

## Import Ledger

| Input | Role | Class | Disposition |
|---|---|---|---|
| Linear one-loop speed flow | Scope of this support theorem | conditional setup | not derived here |
| Positive mutual-drag coefficients `a,b` | Load-bearing attraction condition | open physical loop input | named residual |
| Exact exchange-matrix algebra | What this note proves | framework-independent exact support | discharged by runner |
| Physical LV-bound comparison | Downstream sufficiency question | open bridge | not addressed |

## Verification

Run:

```bash
python3 scripts/frontier_emergent_lorentz_velocity_rg_exchange_matrix_2026_06_18.py
```

Expected final line:

```text
TOTAL: PASS=37 FAIL=0
```

## Audit Boundary

This note does not run audit, set audit status, or promote the interacting
Lorentz row. It is an exact-support artifact for one sub-blocker. Independent
review and audit must decide whether it can serve as a one-hop authority in the
parent chain.
