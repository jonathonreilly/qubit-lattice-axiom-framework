# Route Portfolio

## Chosen Route: Referenced-Cache Preservation

Scan text files outside `logs/runner-cache/` for cache references and preserve
matching cache files during orphan cleanup.

Score:

- retained-positive probability: not applicable; tooling only.
- missing-import count: low.
- runner/test availability: high.
- review landability: high.
- blast radius: small, one helper path plus one regression test.

## Rejected Route: Delete The Remaining Candidate Set

The CHSH note reference shows deletion is not yet safe for the full candidate
set. Deletion is deferred until cleanup guards no longer report link hazards.

## Rejected Route: Hand-Edit The CHSH Note

That would require deciding whether the note should cite a historical frozen
cache, migrate to a replacement runner, or be demoted. This block is tooling
safety, not claim/audit editorial work.
