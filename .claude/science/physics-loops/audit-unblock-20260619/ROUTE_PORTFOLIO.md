# Route Portfolio

## Selected Route: Dynamic Helper Parser Repair

Patch `_parse_script_imports` so AST calls to `load_frontier` contribute the
literal helper filename to the helper set when the target `scripts/<stem>.py`
exists.

Score:

- Audit-unblock value: high, because it removes a packet-completeness class-C
  risk for queued claims.
- Science risk: low, because it changes packet source visibility only.
- Blast radius: medium, because the citation graph and downstream generated
  audit/publication surfaces are regenerated.

## Rejected Route: CL4C Archive Metadata Repair

The initial CL4C archive candidate runner passed locally, but the row was
dropped by the regenerated pipeline as a gated/archive source. It was restored
out of the branch because it did not unblock the live audit queue.

## Deferred Route: More Metadata Repairs

A live scan after excluding already-open PR targets and archive/gated rows did
not find remaining metadata-only candidates lacking `Claim type:` metadata.
The next block should rescan current `origin/main` after open PR movement.
