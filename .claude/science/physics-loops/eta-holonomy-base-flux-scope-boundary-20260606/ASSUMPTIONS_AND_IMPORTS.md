# Assumptions And Imports

## Repo Inputs

- `docs/repo/ACTIVE_REVIEW_QUEUE.md` supplies the blocker text and salvage
  direction.
- `docs/repo/CONTROLLED_VOCABULARY.md` supplies status vocabulary and wording
  constraints.
- The closed PR #2207 commit supplies historical context only. This branch does
  not copy its no-go claim.

## Mathematical Inputs

- Pauli matrix algebra for `sigma_1`, `sigma_2`, `sigma_3`.
- The standard staggered phase convention
  `eta_mu(x) = (-1)^(sum_{nu < mu} x_nu)` on `Z^3`.
- A nearest-neighbor graph treated as a graph is a 1-dimensional CW complex.
  It has no plaquette 2-cells unless a cubical/fillable complex is added as a
  separate premise.

## Forbidden Imports

- No assertion that compared detour swaps are the same element of `B_2(Z^3)`.
- No assertion that a one-token plaquette loop is null-homotopic in
  `UD_2(Z^3)`.
- No Koide/generation dial setting, selector, fitted value, or observed target
  value is used.

## Open Imports

- A retained-grade or packet-contained `UD_2(Z^3)` homotopy bridge for the
  detour swaps remains open.

