"""R19-25 s6: per-slot occupation tail of the CCR lattice vacuum (3D massless, omega = |qhat|), pre-registered 07:04Z.
 Reduced one-slot state of a Gaussian vacuum is thermal in its symplectic basis: nu = sqrt(<phi^2><pi^2>), nbar = nu - 1/2,
 weight at n >= d is (nbar/(nbar+1))^d. Scenario arithmetic only (suggested): if the finite-d defects of s3/s4 act with
 this weight, d for 1e-15 and 1e-102, and qubits per cell for 10 slots (covariant) at log2(d) each."""
import numpy as np
M = 160
k = (np.arange(M) + 0.5)*2*np.pi/M - np.pi
kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
w = np.sqrt((2*np.sin(kx/2))**2 + (2*np.sin(ky/2))**2 + (2*np.sin(kz/2))**2)
phi2 = np.mean(1/(2*w)); pi2 = np.mean(w/2)
nu = np.sqrt(phi2*pi2); nbar = nu - 0.5; lam = nbar/(nbar + 1)
print(f"<phi^2> = {phi2:.5f}, <pi^2> = {pi2:.5f}, nu = {nu:.5f}, nbar = {nbar:.5f}, tail ratio lambda = {lam:.5f}, decay rate -ln(lambda) = {-np.log(lam):.4f}")
for eps in [1e-15, 1e-102]:
    d = int(np.ceil(np.log(eps)/np.log(lam)))
    print(f"  eps = {eps:.0e}: d >= {d}, log2(d) = {np.log2(d):.2f} qubits/slot, 10 slots/cell -> {10*np.ceil(np.log2(d)):.0f} qubits/cell")
