# Assumptions And Imports

## Retained repo inputs

- Existing SU(3) Cartan-torus character machinery used by
  `scripts/frontier_su3_cube_perron_solve.py`.
- Existing source-sector factorization form used for the Reference B recovery.
- Existing finite L_s=2 site/link indexing conventions.

## Explicit local convention

- The source row now defines an all-forward quotient encoder. Nominal reverse
  steps in a +d1 +d2 -d1 -d2 traversal are represented by the same forward
  directed edge after L_s=2 PBC site identification.

## Open imports

- This block does not prove that the quotient encoder is the Wilson
  orientation/count theorem.
- This block does not compute non-trivial SU(3) intertwiner traces.
- This block does not establish a quantitative P_cube(6) lower bound beyond the
  trivial sector.
