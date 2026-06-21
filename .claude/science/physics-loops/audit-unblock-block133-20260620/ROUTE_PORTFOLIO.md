# Route Portfolio

## Chosen Route: Preserve Embedded Scripts Subpath

For absolute paths, try the embedded `scripts/...` suffix before falling back
to `scripts/<basename>.py`.

Score:

- retained-positive probability: not applicable; tooling only.
- missing-import count: low.
- runner/test availability: high.
- review landability: high.
- blast radius: small, synchronized helper copies plus guard.

## Rejected Route: Basename-Only Recovery

Basename-only recovery loses nested directories and can leave stale absolute
paths unresolved when the checked-out file exists in a subdirectory.

## Rejected Route: Shared Canonicalization Module

Useful later, but broader than needed for this unblock block.
