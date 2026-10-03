#!/usr/bin/env python3
"""Coordinator's independent check of A31 (own code, from the report's statements).
(a) D1: the space of two-site operators on a z-bond invariant under the soldered bond stabilizer (C4 about the bond
    axis; C2 about x through the bond midpoint, which swaps the sites) is 5-dimensional;
(b) D2: on a 3x3 periodic 2D torus with a uniform product state |n>^9:
    - compass K sigma^a sigma^a (a = bond axis) never leaves |n>^9 stationary (min residual over n > 0),
    - DM D (sigma_x x sigma_{x+a})_a leaves it stationary with no records, NOT next to a record of content -n,
    - Heisenberg J sigma.sigma leaves it stationary next to a -n record;
(c) Theorem S: the KS (pi-flux) sign pattern on Z^3 (4^3 torus) is preserved exactly (as signs) by no face-diagonal
    half turn about any site; its exact site-centred symmetry group is listed."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import numpy as np
from scipy.linalg import expm
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]], complex); Z = np.diag([1.0 + 0j, -1.0])
S = [X, Y, Z]
def su2(R):
    """SU(2) element U with U sigma_i U^dag = sum_j R_ji sigma_j (R proper rotation)."""
    w, v = np.linalg.eig(R)
    ax = np.real(v[:, np.argmin(np.abs(w - 1))]); ax /= np.linalg.norm(ax)
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    for sgn in (1, -1):
        U = expm(-1j * sgn * ang / 2 * sum(ax[i] * S[i] for i in range(3)))
        ok = all(np.allclose(U @ S[i] @ U.conj().T, sum(R[j, i] * S[j] for j in range(3))) for i in range(3))
        if ok:
            return U
    raise RuntimeError("no su2 lift")
# (a)
C4z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float)
C2x = np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]], float)
group = []
for k in range(4):
    group.append((np.linalg.matrix_power(C4z, k), False))
    group.append((np.linalg.matrix_power(C4z, k) @ C2x, True))
SWAP = np.zeros((4, 4));
for i in range(2):
    for j in range(2):
        SWAP[2 * j + i, 2 * i + j] = 1
basis = [np.kron(a, b) for a in [I2] + S for b in [I2] + S]
P = np.zeros((16, 16), complex)
for R, sw in group:
    U = su2(R); UU = np.kron(U, U)
    for c, O in enumerate(basis):
        O2 = UU @ O @ UU.conj().T
        if sw:
            O2 = SWAP @ O2 @ SWAP
        for r, Bm in enumerate(basis):
            P[r, c] += np.trace(Bm.conj().T @ O2) / 4 / len(group)
print("(a) invariant two-site operators on a bond: dim =", int(round(np.trace(P).real)), " (rank %d)" % np.linalg.matrix_rank(P, 1e-9))
# (b) 3x3 torus, 2D, bonds along x and y
Lx = 3; N = Lx * Lx
def op(single, site):
    out = np.array([[1.0 + 0j]])
    for s in range(N):
        out = np.kron(out, single if s == site else I2)
    return out
sig = [[op(S[a], s) for a in range(3)] for s in range(N)]
def site(x, y):
    return (x % Lx) * Lx + (y % Lx)
bonds = []
for x in range(Lx):
    for y in range(Lx):
        bonds.append((site(x, y), site(x + 1, y), 0))
        bonds.append((site(x, y), site(x, y + 1), 1))
def H_terms(J=0.0, K=0.0, D=0.0):
    H = np.zeros((2 ** N, 2 ** N), complex)
    for i, j, a in bonds:
        if J: H += J * sum(sig[i][c] @ sig[j][c] for c in range(3))
        if K: H += K * sig[i][a] @ sig[j][a]
        if D:
            b, c = [(1, 2), (2, 0), (0, 1)][a]
            H += D * (sig[i][b] @ sig[j][c] - sig[i][c] @ sig[j][b])
    return H
def product_state(n):
    th, ph = np.arccos(n[2]), np.arctan2(n[1], n[0])
    v = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    psi = np.array([1.0 + 0j])
    for s in range(N):
        psi = np.kron(psi, v)
    return psi, v
def compress(H, rec_site, vrec):
    """Q_R H Q_R with the record site projected on |vrec>; act on the full space (record site fixed)."""
    Pr = op(np.outer(vrec, vrec.conj()), rec_site)
    return Pr @ H @ Pr
def residual(H, psi):
    E = np.vdot(psi, H @ psi).real
    return np.linalg.norm(H @ psi - E * psi)
rng = np.random.default_rng(3)
HK = H_terms(K=1.0); HD = H_terms(D=1.0); HJ = H_terms(J=1.0)
resK = []
for trial in range(60):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    psi, v = product_state(n); resK.append(residual(HK, psi))
for n in np.eye(3):
    psi, v = product_state(n); resK.append(residual(HK, psi))
print("(b) compass: min residual over 63 axes n = %.3f (never stationary)" % min(resK))
n = rng.normal(size=3); n /= np.linalg.norm(n)
psi, v = product_state(n)
vm = np.array([-np.conj(v[1]), np.conj(v[0])])     # the opposite state -n
print("    DM, no records: residual %.2e" % residual(HD, psi))
# put a -n record at site 0: state = |-n> at site 0, |n> elsewhere
psi_rec = np.array([1.0 + 0j])
for s in range(N):
    psi_rec = np.kron(psi_rec, vm if s == 0 else v)
print("    DM, -n record at site 0 (compressed): residual %.3f" % residual(compress(HD, 0, vm), psi_rec))
print("    Heisenberg, -n record at site 0 (compressed): residual %.2e" % residual(compress(HJ, 0, vm), psi_rec))
psi_recp = psi.copy()
print("    DM, +n record at site 0 (compressed): residual %.2e" % residual(compress(HD, 0, v), psi_recp))
# (c) Theorem S on the KS pattern
L = 4
def eta(xv, a):
    # KS signs: eta_x = 1, eta_y = (-1)^x, eta_z = (-1)^(x+y)
    return [1, (-1) ** xv[0], (-1) ** (xv[0] + xv[1])][a]
def plaq_flux(xv, a, b):
    e = np.eye(3, dtype=int)
    p = eta(xv, a) * eta(xv + e[a], b) * eta(xv + e[b], a) * eta(xv, b)
    return p
fl = {plaq_flux(np.array(v), a, b) for v in itertools.product(range(L), repeat=3) for a, b in ((0, 1), (0, 2), (1, 2))}
print("(c) KS plaquette fluxes on 4^3:", fl)
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[perm[i], i] = sg[i]
        if round(np.linalg.det(R)) == 1: rots.append(R)
def bond_sign_map(R, c):
    """sign of the image bond under rotation R about site c, compared with original: exact preservation check"""
    e = np.eye(3, dtype=int)
    for v in itertools.product(range(L), repeat=3):
        v = np.array(v)
        for a in range(3):
            p1 = (R @ (v - c) + c) % L; p2 = (R @ (v + e[a] - c) + c) % L
            d = (p2 - p1) % L
            if list(d).count(0) == 2 and (d == 1).any():
                b = int(np.argmax(d == 1)); base = p1
            else:
                b = int(np.argmax(d == L - 1)); base = p2
            if eta(base, b) != eta(v, a):
                return False
    return True
c = np.array([0, 0, 0])
keep = [R for R in rots if bond_sign_map(R, c)]
def is_face_diag_halfturn(R):
    return round(np.trace(R)) == -1 and any(abs(R[i, j]) == 1 and abs(R[j, i]) == 1 and i != j and R[k, k] == -1
                                           for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)))
print("    rotations about site (0,0,0) preserving KS signs exactly: %d of 24; face-diagonal half turns among them: %d"
      % (len(keep), sum(is_face_diag_halfturn(R) for R in keep)))
for cc in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
    kk = [R for R in rots if bond_sign_map(R, np.array(cc))]
    print("    about site %s: %d preserved; face-diagonal half turns %d" % (cc, len(kk), sum(is_face_diag_halfturn(R) for R in kk)))
nfd = sum(is_face_diag_halfturn(R) for R in rots)
print("    (sanity: face-diagonal half turns among the 24 rotations = %d)" % nfd)
