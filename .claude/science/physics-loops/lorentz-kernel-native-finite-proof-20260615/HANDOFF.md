# Handoff

This PR prepares `lorentz_kernel_positive_closure_note`, a critical ready row
with large downstream fanout, for audit.

What changed:

- The note no longer uses Stone's theorem as a load-bearing textbook import.
- The finite fixed-`H_lat` theorem is proved directly: diagonalize the finite
  Hermitian matrix, define `U(t)` entrywise, prove unitarity/group law/generator
  equation/uniqueness on the finite system.
- The runner adds finite spectral reconstruction and generator-equation checks.
- The runner cache is refreshed with `PASS=43 FAIL=0`.

What this does not do:

- It does not update any audit verdict or effective status.
- It does not close the gravity-card directional-measure kernel.
- It does not assert uniqueness across all possible lattice actions or all
  conceivable kernels.

Recommended reviewer/auditor action:

Audit the row as a bounded fixed-`H_lat` finite matrix theorem, with Stone's
theorem treated as parallel continuum context rather than an imported
load-bearing input.
