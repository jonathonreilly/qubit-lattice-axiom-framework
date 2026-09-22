# PR8148–8150 source recovery

This directory preserves all 66 original changed-file occurrences, including complete scientific notes, runners, actual control programs, outputs and author histories. Each deterministic gzip file decodes to the original bytes; no trailing whitespace or history is discarded. The portable `original-manifest.json` records original Git mode/blob, frozen head, path, decoded SHA-256 and archive SHA-256. Decode a payload with `gzip -dc PATH.gz`; compare its digest with the manifest.

The three positive canonical notes retain the valid identities, sufficient constructions and exact finite witnesses. Original universal clock/mixture exclusions, necessity classifications and environment exclusions are deferred. The arbitrary fixed-environment necessity argument additionally has a proof gap. The full original proofs are preserved here without current authority; the original branches must remain recovery handles. Historical cache files are not current canonical evidence.

## Original-to-current claim mapping

- PR8148: current source `docs/ADMISSIBILITY_RULE_FORMATION_RATE_IDENTITIES_AND_FINITE_WINDOW_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md`; original full note and primary are stored in `8148/`. All other original versions remain mapped in the manifest.
- PR8149: current source `docs/ADMISSIBILITY_RULE_FORMATION_UNIT_CONDITIONAL_IDENTITIES_AND_FINITE_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md`; original full note and primary are stored in `8149/`. All other original versions remain mapped in the manifest.
- PR8150: current source `docs/ADMISSIBILITY_RULE_FORMATION_LAW_FLIP_IDENTITIES_AND_FINITE_MIXTURE_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md`; original full note and primary are stored in `8150/`. All other original versions remain mapped in the manifest.

The primary runner basenames and mutation identifiers retain their historical names for continuity. Their current scopes and literal input declarations point to the corrected notes. No scientific result is assigned to this README.
