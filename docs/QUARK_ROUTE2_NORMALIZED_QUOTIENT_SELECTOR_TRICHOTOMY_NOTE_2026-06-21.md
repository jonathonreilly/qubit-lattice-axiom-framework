# Quark Route-2 Normalized-Quotient Selector Trichotomy

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no-go / exact support boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / exact support boundary
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_normalized_quotient_selector_trichotomy_2026_06_21.py`](../scripts/frontier_quark_route2_normalized_quotient_selector_trichotomy_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_normalized_quotient_selector_trichotomy_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_normalized_quotient_selector_trichotomy_2026_06_21.txt)
**Authority links:** [QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md](QUARK_E_CHANNEL_ENDPOINT_QUOTIENT_LAW_NOTE_2026-04-19.md), [QUARK_ENDPOINT_RATIO_CHAIN_LAW_NOTE_2026-04-19.md](QUARK_ENDPOINT_RATIO_CHAIN_LAW_NOTE_2026-04-19.md), [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)

## Safe Statement

This packet attacks the normalized-quotient route to the Route-2 endpoint
triple from minimal premises.

The upstream quotient and ratio-chain notes identify the live positive target:

```text
q_E := gamma_E(center) / gamma_E(shell) = 15/8
rho_E := beta_E / alpha_E = 21/4
c_TE := gamma_T(center) / gamma_E(center) = -8/9.
```

After the conditional T-side values are granted,

```text
rho_T = beta_T / alpha_T = -1,
mu = alpha_T / alpha_E = -2,
```

the reduced exact family is

```text
P(rho_E) = [[1, 0, rho_E, 0],
            [0, -2, 0, 2]].
```

The normalized quotient is then exactly

```text
q_E = 1 + rho_E / 6.
```

The trichotomy is:

1. A normalized-quotient rule that is blind to the E-center column sees the
   same data for every `rho_E`, so it cannot select `21/4`.
2. A rule that imposes `q_E = 15/8`, `c_TE = -8/9`, or
   `q_E / q_T = 9/4` is exactly equivalent to imposing
   `rho_E = 21/4`; it rewrites the target rather than deriving it.
3. A low-rational or nearest-candidate rule contains many admissible quotient
   values. It selects `15/8` only after using live endpoint distance as a
   comparator, which is bounded evidence rather than a proof input.

Therefore quotient normalization alone is not a missing theorem. The missing
theorem is an independent E-center equation or source/readout primitive that
forces one quotient value.

## Minimal Premise Set

Allowed:

- exact restricted carrier columns;
- exact reduced readout family after the T-side candidates are granted;
- exact quotient algebra over `q_E`, `q_T`, `c_TE`, and `q_E/q_T`;
- exact rational arithmetic.

Forbidden as proof inputs:

- observed quark masses;
- fitted Yukawa or CKM/`J` objectives;
- nearest rational to the live endpoint value;
- a hidden E-center source weight;
- a new target-valued axiom.

Live endpoint distance may appear only as bounded comparator evidence.

## Exact Equivalences

For the reduced family above,

```text
q_T = 5/6,
gamma_T(shell) / gamma_E(shell) = -2,
q_E = 1 + rho_E / 6,
c_TE = (-5/3) / q_E,
q_E / q_T = (6/5) q_E.
```

Thus all of these are the same target equation:

```text
rho_E = 21/4
<=> q_E = 15/8
<=> c_TE = -8/9
<=> q_E / q_T = 9/4.
```

The equivalence is useful support, but it does not decide which equation is
true on the current surface.

## What This Prunes

This block prunes the route:

```text
form a normalized quotient
+ use projective/shell/T-side quotient algebra
=> q_E = 15/8.
```

That implication is false on the current exact premises. The quotient
coordinate faithfully exposes the remaining free parameter; it does not
select the parameter by itself.

## What Remains Open

A positive repair must supply at least one independent premise that evaluates
the E-center column or an equivalent source/readout primitive. Examples:

- a source-domain rule fixing the E-center endpoint weight;
- a tensor readout-map theorem beyond the restricted endpoint carrier;
- a new exact E-center equation whose constants are not imported from the
  target value or live endpoint distance;
- an alternate up-sector scalar-law route outside Route-2 endpoint readout.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_normalized_quotient_selector_trichotomy_2026_06_21.py
```

Current expected result on this branch:

- `TOTAL: PASS=34, FAIL=0`
