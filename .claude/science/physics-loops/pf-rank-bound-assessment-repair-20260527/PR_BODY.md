## Summary

This PR repairs the PF rank-bound citation row as a bounded gap-assessment row.

Loop PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2089

It adds a primary runner and makes explicit that the row does not claim an
all-degree rank theorem or an all-order minimal-annihilator theorem.

## Target Row

- `plaquette_v1_picard_fuchs_ode_rank_bound_citation_note_2026-05-06`

## Verification

- `python3 scripts/frontier_pf_rank_bound_assessment_repair.py`
  - `SUMMARY: PASS=19 FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_BOUND_CITATION_NOTE_2026-05-06.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete
- `git diff --check`
  - clean

## Pipeline Result

- Target row reset to `unaudited`, `claim_type=bounded_theorem`.
- Runner path set to `scripts/frontier_pf_rank_bound_assessment_repair.py`.
- One-hop PF dependencies are retained-bounded.

## Boundaries

- No new axioms.
- No retained retag.
- No all-degree rank theorem.
- No all-order minimal-annihilator theorem.
