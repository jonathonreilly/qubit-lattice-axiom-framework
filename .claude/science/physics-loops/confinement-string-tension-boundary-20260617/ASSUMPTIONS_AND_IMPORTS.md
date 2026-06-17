# Assumptions And Imports

Target: `confinement_string_tension_note`

Framework-local content preserved:

- Graph-first SU(3) structural context.
- Declared `g_bare = 1` normalization.
- Exact Wilson plaquette arithmetic `beta = 2 N_c / g_bare^2 = 6`.
- Companion runner checks at beta=6, including finite-volume qualitative
  plaquette and Wilson-loop behavior.

Bounded imports still present:

- Standard SU(3) Yang-Mills confinement/lattice-QCD background.
- Sommer-scale and string-tension lattice inputs at beta=6.
- Two-loop QCD/EFT running and quark-threshold transfer.
- Phenomenological comparator `sqrt(sigma) ~ 440 MeV`.

Science boundary:

This branch does not add an axiom and does not claim a framework-native proof
of four-dimensional Yang-Mills confinement. It converts the source surface into
honest bounded support so downstream audit work can consume the beta=6 support
without inheriting an overstated theorem.
