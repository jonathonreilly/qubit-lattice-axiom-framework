# Near-degenerate eigenvector correction

The initial checker failed its ground/trial orthogonality tolerance for
L=8, g=0.2. The unrestricted dense eigensolver gave a parity remainder of
4.2012196e-9 and overlap -4.2012195e-9 across a gap6.38976e-6. The exact
Majorana anticommutator and commutator identities already passed. This is
near-degenerate eigenvector mixing, not a failed strong-zero-mode identity.

The corrected checker diagonalizes the two exact parity blocks separately,
checks the reconstructed ground-state residual, and retains the original
tight algebraic orthogonality test. The initial output is preserved below
its original filename suffix. No tolerance was relaxed or theorem changed.
