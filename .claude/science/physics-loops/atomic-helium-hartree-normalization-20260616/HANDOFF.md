# Handoff

PR purpose: source-side repair for the latest failed audit row
`work_history.atomic.hydrogen_helium_atomic_companion_note_2026-04-18`.

The blocker named a helium Hartree Coulomb-integral normalization issue. This
branch makes the convention explicit:

- `rho=|phi|^2` is one-electron normalized;
- `E_pair=sum rho V_H[rho]` is the single electron-electron pair expectation
  for `phi(r1)phi(r2)`;
- with total density `n=2rho`, the same one-pair integral is
  `(1/4) sum n V_H[n]`;
- `(1/2) sum n V_H[n]` would count two such pairs on this two-electron
  product-state surface.

Reviewer focus:

- Confirm the pair-integral convention is scientifically correct.
- Confirm the finite-Rydberg/d=3-selection prose remains outside the scoped
  finite-box claim.
- Confirm no audit result or effective-status surface was edited.

Next action: review and, if accepted, let the independent audit/review lane
rerun status movement.
