import time
import numpy as np
from wlib import grid, w3_from, find_nodes_su2, proper_rotations, spin_half
from models import E1

t0 = time.time()
print("E1: U = Sx Sy Sz (2x2, strictly local, each layer one hop)")
for N in (8, 12, 16, 24):
    K = grid(N)
    U, dU = E1(K)
    unit = np.abs(U @ U.conj().transpose(0, 2, 1) - np.eye(2)).max()
    w, wi = w3_from(U, dU, U.conj().transpose(0, 2, 1))
    print(f"  N={N:2d}  max|UU^+-1|={unit:.1e}  W3={w:+.3e} (imag {wi:+.1e})")

nodes = find_nodes_su2(E1, N=24)
print(f"  nodes found: {len(nodes)}")
net = {+1: 0, -1: 0}
for k0, u0, chi, detJ in sorted(nodes, key=lambda t: (t[1], tuple(np.round(t[0], 3)))):
    net[u0] += chi
    print(f"    k0/pi={np.round(k0/np.pi,4)}  U=({u0:+d})1  chi={chi:+d}  detJ={detJ:+.3f}")
print(f"  net chirality at quasi-energy 0 (U=+1): {net[1]:+d};  at pi (U=-1): {net[-1]:+d}")

# covariance under the 24 proper rotations (spin-1/2 soldering)
rng = np.random.default_rng(1)
Kr = rng.uniform(0, 2 * np.pi, (40, 3))
U, _ = E1(Kr)
ncov = 0
for R in proper_rotations():
    D = spin_half(R)
    UR, _ = E1(Kr @ R.T)  # U(R k)
    err = np.abs(UR - D @ U @ D.conj().T).max()
    ncov += err < 1e-10
print(f"  proper rotations R with U(Rk) = D(R) U(k) D(R)^+ : {ncov}/24")
print(f"  time {time.time()-t0:.1f}s")
