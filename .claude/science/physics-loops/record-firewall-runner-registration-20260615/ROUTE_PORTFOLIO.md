# Route Portfolio

## Route A: Parser-visible runner registration

Replace the nonstandard preamble label with `Runner:` and `Runner cache:` so
`docs/audit/scripts/build_citation_graph.py` can attach the primary runner.

Status: selected and implemented.

## Route B: Add a packet wrapper runner

Create a new wrapper that checks both existing runners and the note text.

Status: not selected. The current exact runner is already the direct verifier,
and adding a wrapper would increase surface area without improving the claim.

## Route C: Change audit parser labels

Teach the parser to recognize `Primary exact runner`.

Status: not selected for this PR. A source-side standard-label repair is lower
blast radius and matches existing audit conventions.
