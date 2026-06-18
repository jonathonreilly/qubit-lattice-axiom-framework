# Handoff

This PR is a source-side scope repair for the universal GR polarization-frame
row.

What changed:

- The note now claims exact finite frame-orbit support instead of an exhaustive
  universal blocker/no-go.
- The note names the useful finite certificate: nondegenerate 10D symmetric
  prototype, scalar-line agreement, stable rank-2 scalar-channel projector,
  and frame-dependent complement coefficients.
- The runner title and assertions now verify that boundary.

What remains open:

- A covariant full polarization-frame/projector bundle.
- A distinguished connection or horizontal distribution.
- A curvature-localization operator `Pi_curv`.
- Full Einstein/Regge dynamics-law closure.
- Independent review and audit.

No audit, ledger, queue, publication, front-door, lane-registry, or canonical
harness-index files are changed by this branch. Review-loop was not run because
the user delegated review-loop and landing cleanup to the Codex reviewer.

Next action after reviewer extraction: decide whether to attack the positive
`Pi_curv`/bundle theorem or pivot to the observable-principle T1-d bridge.
