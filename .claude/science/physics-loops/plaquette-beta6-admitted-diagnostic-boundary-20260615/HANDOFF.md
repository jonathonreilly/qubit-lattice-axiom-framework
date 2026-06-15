# Handoff

This branch repairs `plaquette_beta6_perturbative_derivation_bounded_obstruction_note_2026-05-27`
by explicitly electing the admitted-input runner-local diagnostic option named
by audit.

Changed source files:

- `docs/PLAQUETTE_BETA6_PERTURBATIVE_DERIVATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-27.md`
- `scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py`
- `logs/runner-cache/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.txt`

Local pipeline evidence:

- Runner: `TOTAL: PASS=32, FAIL=0`
- Full `bash docs/audit/scripts/run_pipeline.sh` passed.
- Before generated audit outputs were restored, the row became
  `effective_status: unaudited`, `ready: true`, with no old conditional blocker.

Remaining science:

- Derive or audit separate authority for the NSPT packet, beta=6 normalization,
  MC comparator, F2 comparator, or a non-perturbative beta=6 plaquette route.

This PR does not edit audit verdicts or generated audit/publication/status
surfaces.
