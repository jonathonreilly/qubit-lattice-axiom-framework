# Artifact Plan

1. Compact the primary passing transcript without weakening checks.
2. Refresh its content-pinned cache and verify the full body is below 6000
   characters.
3. Add an independent scalar-trace response runner with a declared fingerprint
   for the primary source and no runtime dependency on either cache.
4. Cache the independent run and expose both SHA/input pins in the note.
5. Run lint, both runners, audit packet inspection, and review-loop.
