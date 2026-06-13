# Assumptions And Imports

Current support:

- Exact scalar observable generator.
- Exact `3+1` lift on `PL S^3 x R`.
- Exact tensor-valued variational candidate.
- Unique symmetric quotient kernel on the finite prototype.
- Exact rank-2 scalar-channel projector.

Open imports:

- A covariant `3+1` polarization-frame/projector bundle.
- A distinguished connection or horizontal distribution on the complement.
- A full curvature-localization operator `Pi_curv`.
- An Einstein/Regge dynamics law.

This PR does not supply those objects. It prevents downstream rows from using
the support packet as if those objects had been supplied.
