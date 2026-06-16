# Artifact Plan

- Patch Hartree runner with explicit one-electron-density convention.
- Add a brute-force small-grid direct pair-integral normalization certificate.
- Patch Jastrow runner so the baseline records inheritance from the repaired
  Hartree normalization.
- Patch packet verifier to require the new source and cache needles.
- Regenerate Hartree, Jastrow, and packet-verifier caches.
- Update the source note with the repair boundary, cache lines, and no-status
  lift language.
