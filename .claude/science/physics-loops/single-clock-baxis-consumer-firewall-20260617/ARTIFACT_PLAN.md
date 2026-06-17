# Artifact Plan

- Patch scoped direct/downstream source notes with explicit B-AXIS boundary
  language.
- Add a deterministic text firewall runner over the patched source set.
- Repair the upstream single-clock runner's textual guard so it matches the
  post-cycle-edge source wording while preserving the no-promotion boundary.
- Run both runners and Python syntax compilation.
