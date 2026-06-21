# Route Portfolio

## Chosen Route: Fix Null Canonicalization And Regenerate Packet-Deps

Treat `None` runner paths as empty in the canonicalizers, then refresh
`audit_packet_script_deps.json` and its cache transcript through the precompute
runner-cache wrapper.

Score:

- retained-positive probability: not applicable; tooling only.
- missing-import count: low.
- runner/test availability: high.
- review landability: medium; generated JSON is large but scoped.
- blast radius: packet-deps support surface and two cache transcripts.

## Rejected Route: Commit Generated Output Without Source Fix

The first refresh made null runner rows look like missing file `"None"` paths.
That output was not reviewable as-is.

## Rejected Route: Run Audits For The 389 Pending Helper-Import Claims

The user explicitly requested source-side unblock PRs, not audits.
