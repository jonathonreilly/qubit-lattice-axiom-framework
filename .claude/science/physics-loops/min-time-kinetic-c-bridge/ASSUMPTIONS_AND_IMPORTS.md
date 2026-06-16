# Assumptions And Imports

## Consumed Repo Surfaces

- `scale_reference_primitive`, registered in `docs/audit/data/axiom_premise_nodes.json`.
- `kinetic_isotropy_primitive`, registered in `docs/audit/data/axiom_premise_nodes.json`.
- Tick/edge companion row:
  `min_time_step_tied_to_the_lattice_edge_by_causal_locality_ratio_derived_scale_is_the_clock_rate_no_go_narrow_theorem_note_2026-06-08`.

## Explicit Imports

- Exact SI value `c = 299792458 m/s`, used as a unit conversion only.

## Retired Hidden Inputs

- The previous packet did not make the emergent-c-to-physical-c split explicit.
  The repair now separates:
  - structural/lattice side: `c_lattice = 1`, authorized by the kinetic-isotropy
    primitive;
  - physical-unit side: exact SI `c`, used only to convert metres to seconds.

## Forbidden Inputs

- No physical value of `c` is derived from this row.
- No new speed, clock, Lorentz, or time-coordinate axiom is introduced.
- No observed target value is used as a fitted proof input.
