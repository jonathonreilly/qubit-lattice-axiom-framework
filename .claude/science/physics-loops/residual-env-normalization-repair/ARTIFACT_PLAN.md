# Artifact Plan

- Patch the source note to replace the ambiguous `z_(0,0)^env` divisor with independent `lambda_env`.
- Patch the runner to check the scale separation symbolically.
- Regenerate audit artifacts so the changed row is queued for re-audit.
- Open a PR; do not apply an audit verdict.
