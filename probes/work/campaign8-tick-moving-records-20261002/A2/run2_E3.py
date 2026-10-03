import time
import numpy as np
from wlib import grid, w3_from, find_nodes_su2, proper_rotations, spin_half
from models import E3

t0 = time.time()
print("E3: U = (d4 + i d.sigma)/|d|, m=2 (2x2, covariant, quasi-local)")
for N in (12, 16, 24, 32, 48):
    K = grid(N) + 0.0
    U, dU = E3(K)
    w, wi = w3_from(U, dU, U.conj().transpose(0, 2, 1))
    print(f"  N={N:2d}  W3={w:+.10f} (imag {wi:+.1e})")

nodes = find_nodes_su2(E3, N=20)
net = {+1: 0, -1: 0}
print(f"  nodes found: {len(nodes)}")
for k0, u0, chi, detJ in sorted(nodes, key=lambda t: (t[1], tuple(np.round(t[0], 3)))):
    net[u0] += chi
    print(f"    k0/pi={np.round(k0/np.pi,4)}  U=({u0:+d})1  chi={chi:+d}")
print(f"  net chirality at quasi-energy 0 (U=+1): {net[1]:+d};  at pi (U=-1): {net[-1]:+d}")

rng = np.random.default_rng(2)
Kr = rng.uniform(0, 2 * np.pi, (40, 3))
U, _ = E3(Kr)
ncov, nimp, nimp_dag = 0, 0, 0
for R in proper_rotations():
    D = spin_half(R)
    UR, _ = E3(Kr @ R.T)
    ncov += np.abs(UR - D @ U @ D.conj().T).max() < 1e-10
    # improper element -R ; spin is axial so D(-R) = D(R)
    UI, _ = E3(Kr @ (-R).T)
    nimp += np.abs(UI - D @ U @ D.conj().T).max() < 1e-10
    nimp_dag += np.abs(UI - D @ U.conj().transpose(0, 2, 1) @ D.conj().T).max() < 1e-10
print(f"  proper rotations satisfied: {ncov}/24;  improper (U(R'k)=D U D^+): {nimp}/24;"
      f"  improper map U -> U^+ instead: {nimp_dag}/24")

# mirror image step: U_M(k) = D^+ U(Mk) D with M = -1 (inversion) = U(-k) here
K = grid(32)
UM, dUM = E3(-K)
dUM = -dUM  # chain rule d/dk U(-k)
w, _ = w3_from(UM, dUM, UM.conj().transpose(0, 2, 1))
print(f"  mirror-image step U(-k): W3={w:+.8f}")

# real-space hopping amplitudes: FFT on 64^3
N = 64
K = grid(N)
U, _ = E3(K)
U = U.reshape(N, N, N, 2, 2)
A = np.fft.fftn(U, axes=(0, 1, 2)) / N ** 3  # A_v with U = sum_v A_v e^{ik.v} -> v index sign flip
n = np.fft.fftfreq(N, 1.0 / N).astype(int)
VX, VY, VZ = np.meshgrid(n, n, n, indexing="ij")
r1 = np.abs(VX) + np.abs(VY) + np.abs(VZ)
norms = np.linalg.norm(A, axis=(3, 4))
print("  max ||A_v|| at graph distance r (|vx|+|vy|+|vz|):")
for r in range(0, 13):
    print(f"    r={r:2d}  {norms[r1 == r].max():.3e}")
print(f"  time {time.time()-t0:.1f}s")
