# Handoff

Target:
`busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`.

What changed:

- Rewired the parent note away from a bare Busch/CFMR import.
- Added explicit finite-region routing:
  - native `M_2(C)` effect-Gleason bridge for `|Lambda| = 1`;
  - projection-lattice companion plus spectral decomposition for
    `|Lambda| >= 2`.
- Added the missing cache for
  `scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py`.
- Added cache links to the bridge note.

Boundary:

- No audit ledger/status edits.
- No new axioms.
- No Born-rule parent promotion; the Born chain still has other dependencies.

Suggested reviewer check:

Confirm that the parent note's new markdown links create the intended
dependency surface and that the cache is fresh under `precompute_audit_runners`.
