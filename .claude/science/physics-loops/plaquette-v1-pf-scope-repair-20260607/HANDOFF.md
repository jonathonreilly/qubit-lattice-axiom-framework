# Handoff

Science block: plaquette V1 Picard-Fuchs finite-window scope repair.

Files to review:

- `docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_BOUNDED_SYNTHESIS_NOTE_2026-05-06.md`
- `scripts/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.py`
- `logs/runner-cache/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.txt`
- `outputs/su3_v1_picard_fuchs_minimality_extended_2026_05_06.json`

What changed:

- The source note is narrowed to finite checked windows and finite beta=6
  companion readout.
- Overbroad all-order/minimal-rank language is removed or explicitly negated.
- The runner footer/cache now says finite-window certificate rather than
  operationally closed minimality.
- The refreshed cache reports `SUMMARY: CERTIFICATE PASS=6 FAIL=0`.

What did not change:

- No audit ledger/result files were edited.
- No new axiom was introduced.
- No retained status is claimed by this PR.

Next exact action: reviewer/auditor should re-audit
`plaquette_v1_picard_fuchs_ode_bounded_synthesis_note_2026-05-06` against the
narrowed source packet.
