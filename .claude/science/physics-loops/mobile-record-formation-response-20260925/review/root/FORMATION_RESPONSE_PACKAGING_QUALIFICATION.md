# Preserved first staging failure and narrow packaging correction

The initial 137-file allowlist was staged but not committed. git diff --cached
--check stopped with exit2 because the unchanged historical generation1 runner
cache has an extra blank line at EOF when copied beneath the evidence packet:

    .claude/science/physics-loops/mobile-record-formation-response-20260925/author_history/publication_generation1/logs/runner-cache/original_formation_and_field_response_budget_2026_09_25.txt:29: new blank line at EOF.

The enclosing Python recorder stopped at its check=True diff command before
running git commit. No scientific source or sealed evidence failed or changed.

That duplicate historical cache is therefore omitted from publication rather
than normalized. Its complete original bytes remain unchanged in the preserved
generation1 archive, with hash and recovery path in EXTERNAL_EVIDENCE.json.
The canonical generation2 cache remains included at its declared path. The
original137-file allowlist and first packaging program remain preserved outside
the publication; the final allowlist is explicitly named GENERATION2. This
changes no theorem, evidence payload, cache fingerprint or reviewed claim.
