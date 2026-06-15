# Assumptions And Imports

Retained/source dependencies kept:

- `MINIMAL_AXIOMS_2026-06-05.md`
- `AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md`
- `STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`
- `STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`

Supplied row-local context:

- Kawamoto-Smit phase exhibit / `staggered_dirac_realization_gate`

The patch does not derive the realization gate and does not ask the audit lane
to treat it as retained. It only prevents the graph builder from mistaking a
non-load-bearing reminder for a one-hop dependency.
