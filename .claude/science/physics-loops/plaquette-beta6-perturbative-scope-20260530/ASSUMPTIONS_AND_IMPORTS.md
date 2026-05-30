# Assumptions And Imports

Open imports intentionally left explicit:

- The 16-term NSPT plaquette coefficient packet.
- The beta=6 Wilson-gauge normalization and bare-coupling conversion.
- The F2-scale convention used by the diagnostic.
- The Monte Carlo comparator value used as the target.

Native retained content preserved by this branch:

- Exact arithmetic evaluation of the supplied perturbative series.
- Deterministic truncation and Pade-family diagnostics over the supplied packet.
- The runner-local obstruction statement that the supplied packet and tested acceleration families do not bridge the supplied comparator gap.

No new axiom, retained authority row, or imported-value promotion is introduced here.
