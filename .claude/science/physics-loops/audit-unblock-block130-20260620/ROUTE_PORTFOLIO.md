# Route Portfolio

## Chosen Route: Header-Aware Cleanup Guard

Teach `cleanup_orphans()` to parse each cache header and preserve the cache
when the header names a runner that still exists after canonicalization.

Score:

- retained-positive probability: not applicable; tooling only.
- missing-import count: low.
- runner/test availability: high.
- review landability: high.
- blast radius: small, one helper plus one regression test.

## Rejected Route: Delete Remaining Orphans

Deleting the 9 remaining dry-run candidates may be correct, but it is a
destructive repository cleanup action. This block only fixes the safety guard
needed before that decision can be reviewed.

## Rejected Route: Rewrite Cache Naming

Changing cache names to include nested paths would touch broad audit surfaces
and is unnecessary for the immediate false-positive cleanup risk.
