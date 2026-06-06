# Handoff

## Summary

This PR adds a two-site qubit tensor-carrier bridge and wires it into the two
conditional parent rows that were blocked on the ordinary generated
`H_x tensor H_y` / `M_2(C) tensor_C M_2(C)` surface.

The bridge does not add an axiom. It specializes current retained finite-block
tensor-product rows to `Lambda={x,y}` and explicitly preserves the retained
no-go that locality alone does not force tensor composition.

## Claim Movement Proposed For Audit

- `chsh_tsirelson_lattice_qubits_bound_note_2026-05-20`: blocker closed if the
  two-site bridge is accepted.
- `local_tomography_from_qubit_complex_structure_narrow_theorem_note_2026-06-03`:
  old conditional composition premise is replaced by a source-side dependency
  on the two-site bridge.

## Verification

All three relevant runners pass and all caches are fresh. `docs/audit/**` was
not edited.

## Remaining Reviewer Checks

- Confirm that using the retained finite-block tensor-product rows as the
  generated-composite authority is acceptable after the retained no-go.
- Confirm local-tomography wording does not imply a new axiom or universal
  composite rule.
- Confirm CHSH comparison wording stays theory-side and does not claim
  dynamical Bell preparation.
