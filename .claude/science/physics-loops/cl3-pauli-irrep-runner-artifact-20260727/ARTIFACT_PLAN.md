# Artifact Plan

1. Move deterministic algebra helpers and N1--N8 rendering into a statically imported source below the helper limit.
2. Keep the complete theorem computation in the primary runner below the primary-source limit.
3. Make normal stdout compact while leaving `--verbose` available.
4. Pin the cache to both helper inputs.
5. Verify normal, independent, hostile, intentional-failure, independent steelman, and restricted-packet preflight.
6. Leave audit-authority files untouched and request independent re-audit.
