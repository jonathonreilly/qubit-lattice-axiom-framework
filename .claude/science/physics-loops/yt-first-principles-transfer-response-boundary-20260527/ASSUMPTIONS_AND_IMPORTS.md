# Assumptions And Imports

## Explicit Assumptions

- A differentiable positive Hermitian finite-volume transfer matrix exists on
  the candidate surface.
- Vacuum, W, and top rows are isolated eigenvalue rows for the response
  calculation.
- The same source coordinate acts on W and top rows.
- The local EW mass identities can be applied to the same pole surface if a
  physical pole/action surface is accepted.

## What If Wrong

- If the transfer matrix is not positive/Hermitian, the theorem cannot provide
  a physical pole-response row; the route must fall back to direct correlator
  measurement.
- If the eigenvalues are not isolated, Feynman-Hellmann rows are not
  coefficient-certified; the strict certificate must include gap/plateau
  evidence.
- If the source is not the same for W and top, source normalization does not
  cancel.
- If the EW mass identities are not on the same surface, the response ratio is
  only formal support.

## Forbidden Inputs Avoided

No `H_unit`, `yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG
target, `alpha_LM`, plaquette/u0, Planck pin, alpha_s, or fitted top selector
is used as proof input.
