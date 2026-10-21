---
claim_id: scale_ladder_gravity_burn_and_turn_source_tensor_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Exact plane-wave identity for a supplied front turning rule on supplied lossless walks, finite deterministic local momentum-balance diagnostics for packets, and a finite clock comparison; no physical source identification, derivation of the turning rule, gravity field equation or clock law."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/scale_ladder_gravity_burn_and_turn_source_tensor_2026_10_21.py
---

# Burn and turn contributions to a source tensor on supplied walks

Claim type: bounded_theorem.
Primary runner: `scripts/scale_ladder_gravity_burn_and_turn_source_tensor_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the walks, coins, front rules or tensor assignments below. The terms burn and relay are as defined in the [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight. This note reports what follows from explicitly supplied choices.

## Supplied model

A lossless walk has components labelled by step directions d. Each tick a site coin mixes them, then each component moves one link along its d. A front carries one label, steps along it each tick and follows the Born odds of the walk every tick. Between ticks a front turns from d to d' at the flow 2 eps P_d P_d' / rho, where P are the local odds, rho their sum, and eps the band frequency of the packet. The minimal net flow needed to keep the fronts at the Born odds is added to this. Each burn adds eps d d to the stress. Each turn adds -(d'-d)(d'-d)/4, which is minus one for a reversal.

## Plane-wave identity

For an eigenmode u of U(k)=diag(exp(-i k.d)) C the odds P_d=|u_d|^2 are the same before and after each tick, so only the exchange flow acts. Summing over ordered pairs with P normalised,

    sum_{d != d'} 2 eps P_d P_d' (d'-d)(d'-d)/4 = eps(<d d> - v v),   v = sum_d P_d d.

The diagonal pairs contribute nothing, and the cross terms give minus v v. Burns therefore plus turns equal eps v v exactly. By the eigenphase derivative of U(k), v is the group velocity. Every component of the total, including the off-diagonal shear, matches eps v v. The identity holds for any walk of this form and any band. The runner checks it on a two-component walk on a line, a six-direction walk on Z^3, and an eight-direction walk whose steps are the body diagonals. The eight-direction steps are the forward links of the D4 carrier. Burns alone miss by order one in every case.

The trace of the turn term is eps(<|d|^2> - v^2). On the line |d|=1 equals the walk's limiting speed, and the trace is eps(1-v^2). This approaches m^2/eps, with m the rest frequency, as the coin angle goes to zero. On the six-direction walk steps have length one but the coarse speed is lower. The trace then differs from m^2/eps; the runner reports a difference above 5 percent at two momenta. The turn count is therefore not a relativistic clock on these 3D walks.

## Local balance for packets

For a packet the expected front densities equal the Born odds at every tick. The burn momentum eps sum_d d P'_d (post-coin odds P') then obeys an exact tick balance: it changes by minus the divergence of the burn stress plus the turn impulse density. The runner smooths these fields with a Gaussian of half the packet width. It compares the impulse with minus the divergence of the smoothed turn stress, relative to the divergence of the burn stress. On the line the residual falls roughly in proportion to the inverse width over widths 30, 60 and 120, while the impulse alone stays of order a half. On the six-direction walk, for packets moving along (1,1,0) at widths 3, 5 and 8, the residual again falls with width while the impulse alone stays near one. These are finite diagnostics of a leading-gradient balance, not a proof of exact local conservation.

## Scope

The coins, coin angles, exchange rule, per-turn stress and the use of the band frequency for eps are supplied. The six-direction band is a tracked eigenband whose dispersion is anisotropic. It is used as a lossless mode, not as a relativistic particle. No gravity field equation, physical source, derivation of the turning rule or clock law is established.
