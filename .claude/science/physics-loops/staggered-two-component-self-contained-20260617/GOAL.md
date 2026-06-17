# Goal

Repair the source-side blocker for
`staggered_dirac_kinetic_class_two_component_exclusion_narrow_theorem_note_2026-06-11`.

The audit blocker was not the CAR obstruction itself; it said the row still
depended on the unaudited realization-gate note to supply the check-18 rival
and residual context. This block makes the rival self-contained:

- `D_2c = sum_mu sigma_mu tensor nabla_mu` is defined and rebuilt directly;
- the realization gate is downstream consumer/context only;
- the runner adds firewalls against reintroducing the gate as markdown/YAML
  upstream dependency.

This is a source PR only. It does not audit, land, retag, or edit ledger/status
surfaces.
