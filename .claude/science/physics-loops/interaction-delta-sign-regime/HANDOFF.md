# Handoff

Branch: `physics-loop/interaction-delta-sign-regime-20260607`

Target row:
`interaction_asymmetry_delta_occupation_curvature_two_body_structure_theorem_note_2026-06-06`

What changed:

- The note now states the exact Schur effective coupling formula
  `K_off=t^2*U/[eps(eps+U)]`.
- The sign law is scoped to `eps>0`, `eps+U>0`; the note explicitly does not
  claim a global sign lock through the denominator crossing.
- The runner verifies the formula, verifies sign agreement in the no-resonance
  samples, and verifies an outside-regime sample where the old unconditional sign
  law fails.
- The runner cache was refreshed and reports `TOTAL: PASS=13 FAIL=0`.

Checks:

- Compile, runner, cache refresh/check passed.
- No `docs/audit` files were changed.

Remaining blockers:

- The actual `delta` sign/scale from the retained two-body mediator remains open.
- Independent audit must decide whether this clears the recorded
  `scope_too_broad` verdict.
