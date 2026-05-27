# Assumptions And Imports

## Explicit Assumptions

- C3 acts by the three-cycle matrix `C` on the generation/source triplet.
- The source tangent is Hermitian and C3-invariant.
- The candidate route supplies a connected source tangent, so the identity
  normalization direction is quotiented out.
- The candidate route supplies a reflection-even neutral scalar source, so the
  reflection-odd splitter direction is excluded.
- The top row, if this route closes, must be a nontrivial C3 character line.

## What If Wrong

- If connectedness is not physical, the identity direction `B_a` remains and
  source responses are underdetermined.
- If reflection evenness is not physical, `B_y` remains and response
  magnitudes can be `0` or `1/sqrt(2)` instead of `1/sqrt(6)`.
- If the top row is the trivial C3 line, the `B_x` response magnitude is
  `2/sqrt(6)`, not `1/sqrt(6)`.
- If same-surface dynamics does not provide the C3 line assignment, this block
  remains exact support only.

## Forbidden Imports

No `H_unit`, `yt_ward_identity`, `y_t_bare`, PDG/observed mass, `alpha_LM`,
plaquette/u0, fitted selector, Planck, or alpha_s input is used.

