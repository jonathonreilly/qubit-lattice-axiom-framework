# Assumptions And Imports

Allowed front-door premises:

- `minimal_axioms` from `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `realized_state_primitive` from
  `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`.

Retained/no-go memory and bounded support used as constraints:

- `docs/RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md`:
  occurrence strength only; no formation rule, rate, clock, or stochastic
  process.
- `docs/RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md`: finite
  supplied-context instrument interface.
- `docs/RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md`:
  finite context/generator nonidentifiability.
- `docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md`: post-record
  append/count consumes atoms; it does not produce them.
- `docs/POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md`:
  finite certificates alone do not determine unbounded law.

Not imported:

- no measurement primitive;
- no readout-context selector;
- no Born-probability axiom;
- no branch-selection primitive beyond realized-state pointwise evaluation;
- no production kernel, Hamiltonian, Markov generator, clock, or rate;
- no IID/reset law or empirical-frequency bridge;
- no direct-limit, tightness, or projective-consistency family principle.
