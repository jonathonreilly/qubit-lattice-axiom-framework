# Assumptions and Imports

## Minimal premise set (`A_min`)

- Lattice: `Z^3`, standard translations/rotations and nearest-neighbor
  adjacency.
- Qubit: one local possibility domain with algebraic presentation `M_2(C)` at
  each site.
- Admissibility: one translation/rotation-covariant nearest-neighbor rule whose
  available local possibilities vary with neighbor conditions.
- Record: records form; one permanent admissible possibility per recorded
  site; record-content-only finite additive scalar readout.
- Elementary finite-dimensional quantum linear response and calculus as
  mathematical infrastructure.

Forbidden proof inputs: observed `y_t`, accepted endpoint values, fitted
selectors, plaquette or coupling values, accepted logistic/erf/smoothstep
profiles, UV cuts, scan thresholds, Standard Model beta functions, and
literature values.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Lattice + Qubit + Admissibility + Record | Defines the current framework model class | zero-input structural | `MINIMAL_AXIOMS_2026-06-29.md` | yes | yes | already the approved axiom surface | used |
| Scale-reference primitive | Units conversion only | approved primitive | `SCALE_REFERENCE_PRIMITIVE_NOTE.md` | no | no | none needed | checked; supplies no kernel content |
| Kinetic-isotropy primitive | Structural `c_t=c_s` only | approved primitive | `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | no | no | none needed | checked; supplies no dynamics |
| Realized-state primitive | Pointwise evaluation slot only | approved primitive | `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | no | no | none needed | checked; supplies no state/boundary/observable |
| Pauli algebra | Constructs the exact one-site countermodel | standard mathematics | finite-dimensional linear algebra | yes | yes | direct symbolic verification | used |
| Kubo/Duhamel first variation | Computes the response kernel | standard mathematics | finite-dimensional unitary evolution | yes | yes | direct matrix derivation in runner | used |
| `pi` | Selects one allowed countermodel frequency | mathematical constant | exact mathematics | yes, only as a witness | yes | no retirement needed; not a physical fit | used |
| Physical `y_t(v)` target | Old scan comparator | observational/fitted comparator | prior runner | no | no | remove from proof | retired |
| Accepted logistic bridge | Old kernel background | fitted input | prior runner | no | no | remove from proof | retired |
| UV window/profile families/cuts | Old scan selection | unsupported/fitted import | prior runner | no | no | remove from proof | retired |
| Microscopic dynamics/source/readout packet | Needed for any positive physical closure | open derivation obligation | absent from current supplied surface | no for negative theorem; yes for positive theorem | no for no-go | new retained theorem chain | exposed blocker |

No load-bearing fitted, observed, conditional, or literature input remains in
the negative theorem.
