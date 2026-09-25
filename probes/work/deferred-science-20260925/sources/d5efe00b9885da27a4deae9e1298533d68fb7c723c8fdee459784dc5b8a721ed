"""Exploratory spectral-increment diagnostics; not a proof or audit runner."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scripts.postmark_electric_exact_side_fixed_index_kernel_2026_09_24 import finite_spin_matrix

for spin in (32, 64, 128, 256, 512, 768):
    lo, hi, diagonal, offdiag, _ = finite_spin_matrix(spin)
    eigenvalues = eigh_tridiagonal(diagonal, offdiag, eigvals_only=True,
                                   lapack_driver="auto")
    phase = (spin * (spin + 1) / 4.0) * eigenvalues
    increments = np.diff(phase)
    second = np.diff(increments)
    wrapped = np.abs((increments + np.pi) % (2.0 * np.pi) - np.pi)
    print(f"S={spin} dim={len(eigenvalues)}")
    print("  phase_increment_range=", float(increments.min()), float(increments.max()))
    print("  wrapped_increment_fraction<0.1=", float(np.mean(wrapped < 0.1)))
    print("  wrapped_increment_fraction<0.01=", float(np.mean(wrapped < 0.01)))
    print("  second_difference_range=", float(second.min()), float(second.max()))
    print("  second_difference_median_abs=", float(np.median(np.abs(second))))
