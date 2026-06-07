# Route Portfolio

1. Primary-runner source-packet inlining.
   - Status: executed.
   - Rationale: directly targets the artifact blocker by forcing the
     target-specific runner to check linked source paths, helper source
     markers, fresh helper caches, and the manifest cache/JSON zero-failure
     result.

2. Manifest-only exposure.
   - Status: insufficient.
   - Rationale: the manifest already passed, but the audit blocker remained
     because restricted-packet review still needed complete helper source
     exposure tied to the target row.

3. Broaden to a wave portability law.
   - Status: rejected for this PR.
   - Rationale: the note explicitly remains a bounded target replay feeding
     pair/batch surfaces, not an independent theorem-grade surface.
