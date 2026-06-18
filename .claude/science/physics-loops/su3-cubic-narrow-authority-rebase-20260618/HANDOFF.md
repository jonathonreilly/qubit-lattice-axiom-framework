# Handoff

This PR is a source-side unlock attempt for the SU(3)^3 cubic colour-anomaly
row. It narrows the row's direct proof inputs to colour-sector suppliers and
adds an explicit Gell-Mann trace derivation for the core cubic indices.

What changed:

- The note no longer uses markdown load-bearing links to the broad
  matter-closure or hypercharge-uniqueness notes for the local SU(3)^3 trace.
- The note cites narrow source suppliers for the graph-first SU(3) carrier,
  left-handed block, right-handed colour slots, and anti-fundamental cubic
  index map.
- The runner verifies the source-side boundary and derives `A(3)=+1`,
  `A(3bar)=-1` from explicit trace algebra.

What remains open:

- Full one-generation matter closure.
- Neutral-singlet branch convention.
- Chirality/time selection.
- Absolute SM hypercharge labelling and uniqueness.
- Independent review and audit.

No audit, ledger, queue, publication, front-door, lane-registry, or canonical
harness-index files are changed by this branch. Review-loop was not run because
the user delegated review-loop and landing cleanup to the Codex reviewer.

Next action after reviewer extraction: consider the full matter-closure bridge
or branch-convention bridge as the next high-impact audit unlock.
