# Handoff

This PR is a source-side repair for the flavor carrier parent row.

What changed:

- The parent note now explicitly delegates the clean Layer-A carrier-type
  theorem to the 2026-06-15 split note.
- The parent is marked as the combined conditional packet for physical `hw=1`
  locus, `r=1/2`, and readout-class selections.
- The parent runner now checks that boundary and the split note's boundary.
- The runner/cache scorecard is refreshed from PASS=9 to PASS=15.

What remains open:

- A theorem forcing the staggered/KS `hw=1` physical locus from baseline.
- A derivation or honest demotion of `r=1/2`.
- A readout/index-selection theorem for `delta=2/9`.
- Independent review and audit.

No audit, ledger, queue, publication, front-door, lane-registry, or canonical
harness-index files are changed by this branch. Review-loop was not run because
the user delegated review-loop and landing cleanup to the Codex reviewer.

Next action after reviewer extraction: attack the `hw=1` physical-locus bridge
or pivot to the next highest-impact missing bridge.
