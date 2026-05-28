# Handoff

This PR repairs the May 28 conditional batch by changing the source surfaces,
not by editing ledger verdicts by hand.

Draft PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2128

What changed:

- 33 May 28 `audited_conditional` notes received explicit re-audit scope
  text;
- synthesis/frontier rows were demoted to support/meta where no theorem runner
  exists;
- PMNS projector runner now records degenerate eigenspace rotations as an open
  selector boundary, with `PASS=17 FAIL=0`;
- wave direct-dM H=0.25 runner now defaults to the Fam1 seed-1 point used by
  the source note and has a refreshed cache;
- SU(3) Haar MC text now reports the largest discrepancy as about 1.20 SE and
  treats sample-complexity statements as convention-dependent heuristics;
- Newton-Poisson/Friedmann was split to dust-only first-integral scope;
- the earlier Mermin-Wagner and Koide APS items from this batch landed upstream
  through review-loop splits, so this rebased PR preserves the landed main
  versions instead of carrying duplicate edits.

Pipeline result:

- `bash docs/audit/scripts/run_pipeline.sh` completed with no audit-lint errors;
- all 33 target rows now have `audit_status: unaudited`;
- source-demoted metadata rows now compute `effective_status: meta`;
- all target rows have `open_dependency_paths` length 0 after the mechanical
  reset.

Independent audit still owns every effective status decision.
