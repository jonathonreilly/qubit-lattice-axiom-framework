# Route Portfolio

## Route A: periodic plane-wave density-kernel bridge

Status: executed.

This directly attacks the audit blocker with a finite torus theorem and
runner: plane waves diagonalize the periodic Laplacian, the Green kernel has
eigenvalue `-G/(eps+mu^2)`, and the Slater density-density mutual energy is
`(Vq(0)-Vq(k-l))/N`.

## Route B: derive physical IR scale

Status: deferred.

This would attempt to pin `G`, `mu^2`, or effective volume. The parent row
explicitly leaves magnitude open, so this is not needed for the current
conditional repair.

## Route C: transport the open-cubic packet directly

Status: rejected as insufficient alone.

Boundary transport without the finite torus Fourier derivation would repeat
the audit's dependency objection.
