# Handoff

Target row: `broad_gravity_derivation_note`.

Repair summary:

- Replaced the broad conditional gravity bundle with a supplied-action algebra
  packet.
- Added a dedicated runner checking source scope plus `k` cancellation and
  phase-rate ratio algebra.
- WEP, time dilation, geodesics, light bending, closure identity, source
  readout, continuum, and null-geodesic bridges are out of scope.

Verification before PR:

- `python3 -m py_compile scripts/broad_gravity_signature_algebra_scope_check.py`
- `python3 scripts/broad_gravity_signature_algebra_scope_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`

Pipeline result:

- Target row queued `unaudited`.
- Audit queue rank: 246.
- Ready queue count: 63.
- Effective status counts after regeneration: `audited_conditional=14`,
  `unaudited=1197`.
- Target row has `open_dependency_paths=[]` after narrowing.
- Stale audit invalidations: 0.

`git diff --check` passed.

Draft PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2201

Reviewer should extract the exact algebra without treating it as a physical
gravity-signature derivation.
