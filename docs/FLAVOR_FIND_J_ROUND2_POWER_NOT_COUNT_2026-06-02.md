# Flavor J-Hunt Round 2: Fermionic Power Does Not Select the `J` Pairing

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the route "fermionic/Berezin first-order structure selects the antisymmetric `J` doublet pairing".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Runner:** `scripts/flavor_find_J_round2_power_not_count_2026_06_02.py` (SCORECARD 4/4).
**Source:** workflow `wf_d2438beb` -- 5 hunt routes + 3-lens verification + synthesis (12 agents).

## Closed Packet

This note proves only the finite-algebra obstruction inside the round-2
`J`-hunt:

> The fermionic/Berezin determinant power does not by itself choose the
> antisymmetric `J=C-C^2` pairing of the real `C3` doublet.

Equivalently, the route

```text
fermionic first-order matter -> Berezin determinant -> forced det_C/J pairing
```

is pruned. The packet does not derive a physical readout normalization, a
`det_R/Q=1` default, or the `det_C -> r=1/2 -> Q=2/3` mapping.

## Direct Checks

1. **Power is not count.** Fermionic-vs-bosonic Gaussian integration fixes the
   determinant exponent: a Grassmann pair gives a Pfaffian/determinant factor,
   while a real boson gives the inverse square-root determinant. This is an
   exponent statement, not a count of whether the generation doublet should be
   treated as two real modes or one complex mode. On equal footing
   `Pf(aJ_2)=a` and `det(sI_2)^(-1/2)=1/s` are both single-power scalings.

2. **Berezin gives a determinant product, not a Frobenius block-total.** For a
   real Hermitian `C3`-circulant matrix
   `H=aI+bC+conj(b)C^T`, the Berezin integral returns `det(H)`, a product of
   the three real eigenvalue factors. That cubic determinant functional is not
   the quadratic block-total functional
   `E_singlet=3a^2`, `E_doublet=6|b|^2` whose equal-block convention would set
   `r=1/2`.

3. **`C3` admits both invariant bilinears.** The symmetric identity `I` and
   the antisymmetric `J=C-C^2` both satisfy `C^T X C = X`. Therefore the
   finite `C3` covariance condition does not select `J` over `I`. Choosing the
   complex/antisymmetric pairing is an extra structure relative to this packet.

## What This Does Not Claim

This packet intentionally does not use the P1 carrier premise, the round-1
`U(1)_b` measure-neutrality result, or any `det_C`/`det_R` to `r,Q` mapping as
load-bearing authorities. Those may be useful elsewhere, but they are not
provided as one-hop authorities here.

In particular, this note does not derive:

- `det_R/Q=1`;
- `det_C -> r=1/2 -> Q=2/3`;
- a Dirac-vs-Majorana assignment for the generation doublet;
- a framework-native selection of the `J` pairing.

The remaining frontier question is sharper after this no-go: if the flavor
lane needs the `J` pairing, it must come from a separate reality-structure,
instrument, or readout theorem, not from fermionic determinant power alone.

## Provenance

- Power-vs-count, determinant-product-vs-block-total, and the two invariant
  bilinears are verified directly by the paired runner.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.
