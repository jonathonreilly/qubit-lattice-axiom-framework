# Handoff

Target row: `dm_leptogenesis_pmns_projector_interface_note_2026-04-16`.

Repair summary:

- The note now states the missing order convention: eigenvectors are labeled by
  ascending eigenvalue order for both `H_nu` and `H_e`.
- The proof now explains why simple spectra plus ordered labels leave only
  diagonal phase freedom, and why dropping labels leaves row/column
  permutation freedom.
- The runner adds `part2b_simple_spectrum_ordered_label_convention`, which
  verifies phase invariance with labels and visible row/column permutation
  changes without labels.

Verification before PR:

- `python3 -m py_compile scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`
- `python3 scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`
- Pipeline result: target row reset to `unaudited`, ready audit queue rank 3,
  `audited_conditional` count 15, ready queue count 57 after rebase to
  `origin/main@9a157affd`.

Do not merge directly. The reviewer should extract the science and let the
audit lane assign any effective status.
