# Flavor J-Hunt Round 1: Static `J_cs` Is Measure-Neutral

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the route "static A1-native complex structure selects the `det_C` doublet measure".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Runner:** `scripts/flavor_find_J_round1_jcs_measure_neutral_2026_06_02.py` (SCORECARD 5/5).
**Source:** workflow `wf_719da018` -- 5 hunt routes + 3-lens verification + synthesis (12 agents).

## Closed Packet

This note proves only the finite-algebra obstruction inside round 1 of the
`J` hunt:

> The static `C3`-equivariant complex structure
> `J_cs=(C-C^2)/sqrt(3)` is measure-neutral and cannot by itself select the
> `det_C` doublet measure.

The packet also checks that the proposed chiral glue
`Gamma_chi = (2/3)J_all - I` is not `J_cs`: it is a real involution built from
the all-ones matrix, while `J_cs` is anti-Hermitian and squares to
`-P_doublet`.

## Direct Checks

1. **`J_cs` is the finite `C3` complex structure.** It is anti-Hermitian,
   commutes with `C`, satisfies `J_cs^2=-P_doublet`, and has eigenvalues
   `{0,+i,-i}`.

2. **`Gamma_chi` is a different operator.** `Gamma_chi^2=I` with eigenvalues
   `{+1,-1,-1}`. It commutes with `J_cs`, but it is neither equal nor
   proportional to `J_cs`. Therefore the route identifying chirality with the
   `J_cs` holomorphic measure is a false identity inside this finite packet.

3. **The static flow is measure-neutral.** `exp(theta J_cs)` is an `SO(2)`
   rotation on the real doublet plane. It preserves the Hilbert-Schmidt block
   metric `6I` and has determinant one, so the static rotation does not choose
   between the real and holomorphic measure conventions.

4. **The structure is operator-silent for the tested circulant family.**
   `J_cs` commutes with the Hermitian `C3`-circulant family
   `H=aI+bC+conj(b)C^T`, so it supplies no spectral lever that fixes the
   doublet mode count.

## What This Does Not Claim

This packet intentionally does not derive:

- a `Q` default;
- a `det_C`-to-`r,Q` readout map;
- a first-order action or Berezin bridge for the generation coefficient;
- a framework-native selection of `det_C`.

The remaining frontier question is separate: if the flavor lane needs the
`det_C` convention, it must come from a dynamical, instrument, or readout
theorem outside this static-`J_cs` packet.

## Provenance

- `J_cs` algebra, `Gamma_chi != J_cs`, `SO(2)` measure-neutrality, and
  operator-silence are verified directly by the paired runner.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.
