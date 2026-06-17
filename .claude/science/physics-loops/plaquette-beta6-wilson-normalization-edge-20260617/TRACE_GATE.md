# Trace Gate

## Targeted Blocker

Audit-named blocker text included four authority gaps:

- NSPT coefficient packet;
- beta=6 Wilson normalization;
- MC comparator;
- F2 comparator.

This PR targets only the second gap.

## Dependency Edge Added

`PLAQUETTE_BETA6_PERTURBATIVE_DERIVATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-27.md`
now depends on
`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`
for `beta = 2 N_c / g_bare^2`.

## Boundary

The Wilson small-a theorem derives coefficient matching inside the supplied
standard Wilson plaquette action and canonical trace normalization. It does
not derive action-surface selection, physical `beta = 6`, or `g_bare = 1`.
