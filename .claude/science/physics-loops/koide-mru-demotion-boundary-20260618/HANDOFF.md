# Handoff

This PR is a source-side repair for the Koide MRU demotion row.

What changed:

- The source note now claims bounded demotion / bridge-corollary support,
  rather than full retained closure through both bridge and block-total routes.
- The block-total Frobenius route is kept as independent bounded support, not
  a standalone physical scalar-measure closure theorem in this row.
- The displayed cubic trace phase term is corrected to
  `3(b^3+bbar^3)`.
- The bridge runner now verifies the corrected trace formula and the source
  boundary.

What remains open:

- A physical scalar-measure bridge for block-total Frobenius as standalone
  closure.
- A derivation of the MRU `SO(2)` quotient.
- Independent review and audit.

No audit, ledger, queue, publication, front-door, lane-registry, or canonical
harness-index files are changed by this branch. Review-loop was not run because
the user delegated review-loop and landing cleanup to the Codex reviewer.

Next action after reviewer extraction: attack either the physical scalar-measure
bridge for block-total Frobenius or pivot to the next high-impact missing
bridge (`T1-d`, `B-AXIS`, or anomaly-forces-time premise bridges).
