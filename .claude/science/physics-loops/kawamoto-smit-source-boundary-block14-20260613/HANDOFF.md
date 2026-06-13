# Handoff

This PR refreshes a source-side repair for the current high-fanout Kawamoto-Smit
audit blocker on `origin/main@fc08b0519`:
`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`.

The ledger surface still belongs to the auditor. This branch only makes the
source theorem boundary cleaner for re-audit.

What changed:

- The source note now defines the audit target as the abstract
  nearest-neighbor `Cl(3)` scalarization theorem on simply connected `Z^3`
  regions.
- P-KIN, P-SD, P-FLUX, and substep-1 statistics selection are downstream
  physical-use gates, not load-bearing theorem premises.
- The runner keeps the existing exhaustive enumeration, GF(2) cohomology, and
  falsification checks, then adds a section-F source-boundary firewall.
- The runner cache is refreshed with `TOTAL: PASS=58 FAIL=0`.

What this does not do:

- It does not update any audit verdict or effective status.
- It does not close the full staggered-Dirac realization gate.
- It does not claim torus holonomy/APBC selection.

Recommended reviewer/auditor action:

Re-audit the abstract cocycle/gauge classification. If the auditor agrees, the
row should no longer be conditional on missing P-KIN/P-SD/statistics bridges;
those bridges belong to downstream physical-realization rows.
