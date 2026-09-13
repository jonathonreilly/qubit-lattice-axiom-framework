# Checker recovery

The first nonlinear force checker was invoked before the exact finite-solution
JSON existed. It stopped at FileNotFoundError without evaluating a mathematical
predicate. Its source is preserved as check_block10_nonlinear_force_first.py.
The final version waits for the exact check first. A redundant late stress
mutation block was also removed before mathematical execution: its first link
had zero stress in the selected fixture. The existing full-force comparison
and temporal-only residual scaling already test the missing correction.

The exact finite checker then failed its final negative control: it set the
first x stress to zero, but that edge already had zero gradient in the fixture.
The unchanged source correctly remained compatible. The first source is
preserved as check_block10_force_first.py. The final control removes the next
nonzero x stress and tests its pairing with an explicit exact kernel vector.
It also uses the exact DomainMatrix rank to avoid repeated slow generic rank
calculations. The symbolic all-period projections and exact finite solution
had completed before that control failure; no physics formula was changed.
