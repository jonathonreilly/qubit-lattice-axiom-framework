"""A31 c1: which nearest-neighbour pair terms are covariant, and which keep the calm
(aligned) emptiness stationary?

(1) Two-qubit Hermitian operators on the z-bond (0, e_z) invariant under the bond's
    stabilizer in the space group, with soldering (possibilities turn with the grid):
      C4 about z through the bond axis (sites fixed),
      C2 about x through the bond midpoint (sites swapped).
    Expect 5: 1, s^z_1 - s^z_2 (telescopes to 0 on the lattice), zz, xx+yy, (s1 x s2)_z.
(2) For H = J s.s + K s^a s^a + D (s_x x s_{x+a})_a summed over the bonds of an open
    2x2x2 cube, the stationarity residual of |n>^8 for random and axis n.
(3) The star-local three-site chirality sum over octants annihilates |nnn>.
"""
import signal, numpy as np
signal.alarm(55)
I2 = np.eye(2); X = np.array([[0,1],[1,0]],complex); Y = np.array([[0,-1j],[1j,0]]); Z = np.diag([1.,-1.]).astype(complex)
P = [I2, X, Y, Z]
def rot(axis, ang):
    n = np.array(axis, float); n /= np.linalg.norm(n)
    return np.cos(ang/2)*I2 - 1j*np.sin(ang/2)*(n[0]*X + n[1]*Y + n[2]*Z)
SWAP = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], complex)
# basis of 16 two-site Paulis
B = [np.kron(P[a], P[b]) for a in range(4) for b in range(4)]
def vec(O): return np.array([np.trace(b.conj().T @ O)/4 for b in B])
u4 = rot([0,0,1], np.pi/2); U4 = np.kron(u4, u4)
u2 = rot([1,0,0], np.pi); U2 = SWAP @ np.kron(u2, u2)
# invariant subspace: O with U O U^dag = O for both generators; solve linear system on coefficient vectors
M = []
for U in (U4, U2):
    T = np.array([vec(U @ b @ U.conj().T) for b in B]).T   # columns: image of basis element
    M.append(T - np.eye(16))
M = np.vstack(M)
s = np.linalg.svd(M, compute_uv=False)
null = np.sum(s < 1e-10)
print(f"(1) dim of covariant two-site operators on a z-bond = {null} (expect 5)")
_, _, Vh = np.linalg.svd(M)
ns = Vh[-null:].conj()
labels = [a+b for a in 'IXYZ' for b in 'IXYZ']
# express a clean basis: project the candidates
cands = {'II': np.kron(I2,I2), 'ZI-IZ': np.kron(Z,I2)-np.kron(I2,Z), 'ZZ': np.kron(Z,Z),
         'XX+YY': np.kron(X,X)+np.kron(Y,Y), 'DMz=XY-YX': np.kron(X,Y)-np.kron(Y,X)}
for k, O in cands.items():
    v = vec(O); r = np.linalg.norm(v - ns.T @ (ns.conj() @ v))
    print(f"    {k:11s} in covariant space: residual {r:.1e}")
for k, O in {'ZI+IZ': np.kron(Z,I2)+np.kron(I2,Z), 'XX-YY': np.kron(X,X)-np.kron(Y,Y), 'XZ+ZX': np.kron(X,Z)+np.kron(Z,X)}.items():
    v = vec(O); r = np.linalg.norm(v - ns.T @ (ns.conj() @ v))
    print(f"    {k:11s} (non-covariant control) residual {r:.2f}")

# (2) stationarity of the aligned emptiness on an open 2x2x2 cube
sites = [(x,y,z) for x in range(2) for y in range(2) for z in range(2)]
idx = {s:i for i,s in enumerate(sites)}; N = len(sites)
def op1(O, i):
    out = np.array([[1.]], complex)
    for j in range(N): out = np.kron(out, O if j==i else I2)
    return out
Sx = [[op1(p, i) for p in (X,Y,Z)] for i in range(N)]
bonds = []
for s_ in sites:
    for a in range(3):
        t = list(s_); t[a] += 1; t = tuple(t)
        if t in idx: bonds.append((idx[s_], idx[t], a))
def H_terms():
    Hh = sum(sum(Sx[i][c] @ Sx[j][c] for c in range(3)) for i,j,a in bonds)
    Hk = sum(Sx[i][a] @ Sx[j][a] for i,j,a in bonds)
    Hd = 0
    for i,j,a in bonds:
        b, c = (a+1)%3, (a+2)%3
        Hd = Hd + Sx[i][b] @ Sx[j][c] - Sx[i][c] @ Sx[j][b]
    return Hh, Hk, Hd
Hh, Hk, Hd = H_terms()
def aligned(n):
    th, ph = np.arccos(n[2]), np.arctan2(n[1], n[0])
    v = np.array([np.cos(th/2), np.exp(1j*ph)*np.sin(th/2)])
    out = np.array([1.], complex)
    for _ in range(N): out = np.kron(out, v)
    return out
def resid(H, psi):
    e = np.vdot(psi, H @ psi).real; return np.linalg.norm(H @ psi - e*psi)
rng = np.random.default_rng(1)
print("(2) stationarity residual ||(H-<H>)|n..n>|| on the open 2x2x2 cube (12 bonds)")
for name, n in [('axis z', [0,0,1]), ('body diag', [1,1,1]), ('random', rng.normal(size=3))]:
    n = np.array(n, float); n /= np.linalg.norm(n); psi = aligned(n)
    print(f"    n={name:9s}: Heisenberg {resid(Hh,psi):.1e}  compass {resid(Hk,psi):.3f}  DM {resid(Hd,psi):.3f}  "
          f"J+K+D mix {resid(Hh+0.3*Hk+0.2*Hd,psi):.3f}")
# (3) three-site chirality on a right-handed octant triple: annihilates symmetric (aligned) states
def chir(i,j,k):
    return (
        Sx[i][0] @ (Sx[j][1] @ Sx[k][2] - Sx[j][2] @ Sx[k][1]) +
        Sx[i][1] @ (Sx[j][2] @ Sx[k][0] - Sx[j][0] @ Sx[k][2]) +
        Sx[i][2] @ (Sx[j][0] @ Sx[k][1] - Sx[j][1] @ Sx[k][0]))
C = chir(idx[(1,0,0)], idx[(0,1,0)], idx[(0,0,1)])
for name, n in [('axis z',[0,0,1]), ('random', rng.normal(size=3))]:
    n = np.array(n,float); n/=np.linalg.norm(n)
    print(f"(3) chirality s_a.(s_b x s_c) on |n..n>, n={name}: ||C psi|| = {np.linalg.norm(C @ aligned(n)):.1e}")
# (2b) no (K, D) != 0 combination is stationary: the two residual vectors are independent
for name, n in [('axis z',[0,0,1]), ('body diag',[1,1,1]), ('random', rng.normal(size=3)), ('random2', rng.normal(size=3))]:
    n = np.array(n,float); n/=np.linalg.norm(n); psi = aligned(n)
    rK = Hk @ psi - np.vdot(psi, Hk @ psi)*psi; rD = Hd @ psi - np.vdot(psi, Hd @ psi)*psi
    sv = np.linalg.svd(np.stack([rK, rD], 1), compute_uv=False)
    print(f"(2b) n={name:9s}: singular values of [r_K, r_D] = {sv[0]:.3f}, {sv[1]:.3f}  (min > 0 => only K=D=0 is stationary)")
