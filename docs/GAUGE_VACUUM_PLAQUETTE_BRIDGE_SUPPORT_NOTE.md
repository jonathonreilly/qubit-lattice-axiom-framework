# Gauge-Vacuum Plaquette Scalar-Bridge Finite Support Packet

**Date:** 2026-04-16 (support stack); 2026-05-24 (scope repaired to a
bounded finite scalar-bridge support packet).
**Type:** bounded_theorem
**Claim scope (post-2026-05-24 narrowing):** the load-bearing claim is only
the finite scalar/local support packet checked by
`scripts/frontier_gauge_vacuum_plaquette_bridge_support.py`. At `beta = 6`,
the runner verifies the local Wilson source-response identity, Bessel/Weyl
agreement for the one-plaquette readout, additivity of independent local
blocks, the accepted scalar `3+1` completion ratio `A_inf/A_2 = 2/sqrt(3)`,
the exact four-link scaling identity for a plaquette monomial, the coordinate
incidence factor `Gamma_coord = 3/2`, and the resulting candidate comparator
against the historical same-surface plaquette value.
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane. The `bounded_theorem` label is a
source-side claim-boundary declaration, not an audit verdict.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_bridge_support.py`

This note does **not** claim the full interacting gauge-vacuum plaquette
reduction law at `beta = 6`. It does not derive the physical 3D Wilson
environment boundary character `Z_6^env(W)`, the tensor-transfer Perron state,
or an analytic closure of canonical `P(6)`. The candidate value is support
context only, not a retained physical prediction.

## Question

Which scalar/local bridge ingredients are actually runner-backed, independent
of the still-open physical Wilson-environment solve?

## Answer

The bounded packet closes six finite support ingredients:

1. The local one-plaquette Wilson expectation equals the derivative of the
   local source generator.
2. The local Wilson generator is additive on independent blocks.
3. Bessel-determinant and Weyl-integration evaluations agree for
   `P_1plaq(6)`.
4. The accepted scalar `3+1` completion ratio is exactly
   `A_inf / A_2 = 2 / sqrt(3)`.
5. The plaquette monomial has exact four-link scaling
   `P(u_0 V) = u_0^4 P(V)`.
6. The hypercubic `3+1` incidence factor is exactly
   `Gamma_coord = 6/4 = 3/2`.

The packet also records two support checks:

- no lower link power preserves the plaquette scaling identity;
- the composed support candidate at `beta = 6` stays within `2e-4` of the
  historical canonical same-surface comparator.

Those checks are useful bridge evidence. They do not prove the interacting
plaquette reduction law.

## Bounded Ingredient 1: local Wilson source-response

For the one-plaquette Wilson weight

`Z_1plaq(beta) = int dU exp[(beta/3) Re Tr U]`,

the source-deformed local generator is

`W_loc(j) = log Z_1plaq(beta+j) - log Z_1plaq(beta)`.

The runner checks at `beta = 6` that

`dW_loc/dj |_(j=0) = d/d beta log Z_1plaq(beta) = P_1plaq(beta)`.

It also checks the same local readout by both the Bessel-determinant mode sum
and Weyl integration on the torus.

## Bounded Ingredient 2: scalar temporal completion ratio

The imported scalar completion authorities establish the accepted-class ratio

`A_inf / A_2 = 2 / sqrt(3)`.

The runner checks the ratio and the fourth-root scalar factor used by the
support candidate:

`Gamma_sc = (2 / sqrt(3))^(1/4)`.

## Bounded Ingredient 3: four-link plaquette scaling

For the oriented plaquette density

`P(U) = (1/3) Re Tr(U_1 U_2 U_3^dag U_4^dag)`,

uniform link rescaling gives the exact algebraic identity

`P(u_0 V) = u_0^4 P(V)`.

The runner checks this on sampled `SU(3)` links and also checks that the
wrong lower power does not preserve the identity.

## Bounded Ingredient 4: coordinate incidence factor

On the hypercubic `3+1` lattice, each link lies in six plaquettes and each
plaquette has four links, so the finite incidence factor is

`Gamma_coord = 6/4 = 3/2`.

## Support Candidate Context

Composing the scalar/local support factors gives the candidate

`beta_eff = beta * (3/2) * (2 / sqrt(3))^(1/4)`.

At `beta = 6`, the runner reports:

- `beta_eff = 9.329531846652698`;
- `P_1plaq(beta_eff) = 0.593530679977098`;
- historical same-surface comparator `0.5934`;
- difference `1.30679977098e-4`.

This is support evidence only. The note does not claim that the full
interacting Wilson plaquette equals this candidate.

## Open Target: physical plaquette bridge

The open theorem-grade target remains the physical nonperturbative bridge:

derive the actual `beta = 6` interacting Wilson plaquette readout from the
full source-sector environment, including the physical boundary character
measure and tensor-transfer/Perron data.

The exact constant-lift law is also not available as a fallback: the retained
obstruction row proves that a constant multiplicative lift cannot be the full
interacting Wilson answer.

## What This Closes

- bounded local Wilson source-response check at `beta = 6`;
- bounded Bessel/Weyl agreement for the local one-plaquette readout;
- bounded scalar `3+1` temporal completion ratio check;
- exact finite four-link scaling identity for the plaquette monomial;
- exact finite `3+1` coordinate incidence factor;
- support-only candidate comparison against the historical same-surface
  plaquette value.

## What This Does Not Close

- the physical 3D Wilson environment boundary character `Z_6^env(W)`;
- tensor-transfer Perron state or full environment readout;
- the full interacting plaquette reduction law at `beta = 6`;
- analytic closure of canonical `P(6)`;
- repo-wide repinning of the canonical plaquette;
- retained-grade promotion of this note.

## Commands Run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_bridge_support.py
```

Expected summary:

- `EXACT PASS=6 SUPPORT=2 FAIL=0`

## Audit Dependency Repair Links

This graph-bookkeeping section records the bounded inputs for the finite
support packet. It does not promote this note, apply an audit verdict, or
close the full physical plaquette bridge.

- [gauge_scalar_temporal_completion_theorem_note](GAUGE_SCALAR_TEMPORAL_COMPLETION_THEOREM_NOTE.md)
  supplies the accepted scalar temporal-completion class.
- [scalar_3plus1_temporal_ratio_note](SCALAR_3PLUS1_TEMPORAL_RATIO_NOTE.md)
  supplies `A_inf / A_2 = 2/sqrt(3)`.
- [gauge_vacuum_plaquette_constant_lift_obstruction_note](GAUGE_VACUUM_PLAQUETTE_CONSTANT_LIFT_OBSTRUCTION_NOTE.md)
  supplies the retained obstruction to a naive exact constant-lift law.

The tensor-transfer/Perron/environment rows are deliberately not load-bearing
for this bounded support packet. They remain separate open science targets.
