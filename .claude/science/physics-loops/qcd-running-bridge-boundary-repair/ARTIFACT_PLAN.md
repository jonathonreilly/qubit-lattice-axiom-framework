# Artifact Plan

## Source Note

- Rename/scope the row as a running-kernel bridge at an admitted boundary.
- Remove markdown one-hop citations to plaquette/rho source rows.
- Preserve downstream reuse rule: this row transfers alpha_s, it does not
  derive the boundary value.

## Runner

- Replace plaquette-derived constants with an admitted `alpha_s(v)` constant.
- Rename the independence check from plaquette insertion to boundary
  provenance.
- Keep the 18-pass verification surface intact.

## Generated Audit Data

- Regenerate citation graph, audit ledger, queue, and runner classification.
- Confirm `qcd_low_energy_running_bridge_note_2026-05-01` has `deps: []`
  and `ready: true`.
