# Artifact Plan

Artifacts:

- live note: `docs/CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NOTE_2026-06-17.md`
- exact runner: `scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py`
- cached runner output: `logs/runner-cache/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.txt`
- source-edge retarget: `docs/work_history/ckm/CABIBBO_BOUND_NOTE.md`

Verification:

- run the new structural runner;
- refresh and check its cache;
- run the legacy calibrated runner as a regression;
- run Python compilation and diff guards;
- check that no audit/status surfaces were edited.
