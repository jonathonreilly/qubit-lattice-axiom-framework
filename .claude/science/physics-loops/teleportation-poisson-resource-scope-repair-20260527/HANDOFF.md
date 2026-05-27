# Handoff

## What Moved

`teleportation_resource_from_poisson_note` is narrowed to an explicit
`open_gate` bounded diagnostic. The old `MINIMAL_AXIOMS_2026-05-03.md` link is
removed in favor of the current canonical A1+A2 premise, and the note states
that the native preparation/readout theorem remains open.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_teleportation_poisson_resource_scope_repair.py`
  - `TOTAL: PASS=20, FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md scripts/frontier_teleportation_poisson_resource_scope_repair.py`
  - clean
- `git diff --check`
  - clean
- `bash docs/audit/scripts/run_pipeline.sh`
  - target row reset to `audit_status=unaudited`
  - `claim_type=open_gate`
  - `runner_path=scripts/frontier_teleportation_resource_from_poisson.py`
  - `helper_runner_paths=["scripts/frontier_bell_inequality.py"]`
  - deps are `minimal_axioms` plus the four retained bounded teleportation rows
  - `open_dependency_paths=[]`

## Remaining Blockers

- Derive native preparation/readout.
- Derive the last-taste-bit logical-carrier selection as a physical carrier.
- Harden beyond the two small default surfaces.

## PR

Draft PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2117
