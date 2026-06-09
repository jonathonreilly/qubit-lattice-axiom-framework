# Handoff

This branch updates the D3 upper-bound source chain so the decisive current
finite-set upper edge is native stable-circular-orbit support, not the full
Bertrand theorem.

Main source changes:

- `DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` now
  states that the legacy filename is retained for citation stability, while
  the load-bearing support edge is the native Green-kernel/effective-potential
  stable-circular-orbit calculation.
- `D3_UPPER_BOUND_IMPORT_SCOPE_GATE_NOTE_2026-06-06.md` now certifies
  `{3,4,5} intersect {d : d <= 3} = {3}` using that native edge.
- `DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md` and its
  runner verify the updated dependency graph.
- The Bertrand support note is clarified: it supplies the stable-circular-orbit
  edge but does not derive the full closed-orbit theorem.

Remaining review questions:

- Is the stable-circular-orbit upper edge sufficient for the current finite-set
  composition, given that the full closed-orbit Bertrand theorem is not used?
- Should the legacy wrapper filename be renamed in a later cleanup, or kept
  for citation stability?
- Does the audit lane want this queued as a source graph repair only, or as a
  re-audit of the upper-bound wrapper and gate together?
