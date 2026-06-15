# Handoff

This PR repairs the uncovered terminal conditional
`koide_first_order_selector_is_the_chiral_lr_coupling_not_a_symmetry_narrow_note_2026-06-05`
from `origin/main@fc08b0519`.

What changed:

- The source note no longer frames the row as a positive theorem deriving the
  physical Koide `r=1/2` selector.
- The retained auditable payload is narrowed to exact bounded algebraic
  localization: phase independence, clock-character block balance, native
  `R3` anticommuting no-go, and separate-factor escape algebra.
- The runner now checks the new boundary and bans the old positive-selector
  wording.
- The runner cache is refreshed.

What this does not do:

- It does not update any audit verdict or effective status.
- It does not derive the physical `AC_phi_lambda -> M(b) x sigma_+` coupling.
- It does not derive the physical first-order/readout weighting or Koide
  `r=1/2`.

Recommended reviewer/auditor action:

Re-audit this row as bounded algebraic localization and no-go demarcation. The
physical selector remains an open downstream gate.
