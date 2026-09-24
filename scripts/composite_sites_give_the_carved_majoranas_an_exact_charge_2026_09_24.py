#!/usr/bin/env python3
"""Composite sites give the carved Majoranas an exact charge: one qubit per site cannot, two can.

Setting (all supplied, none adopted): Kitaev-type record carvings (open PRs 9048, 9054, 9112) give Majorana
fermions in a Z2 gauge field, one matter Majorana per unrecorded site, with no exact U(1). This runner certifies
what an exact charge costs, on supplied models, as finite diagnostics.

1. One qubit per site: no charge between components. In Kitaev's representation the physical operators are the
   ones invariant under D_j = b^x b^y b^z c. A Majorana bilinear i c_j c_k between two DISCONNECTED carving components
   is odd under D_j, so the projector P onto the physical space annihilates it: P (i c_j c_k) P = 0, while a bond
   bilinear of one component survives. The SO(2) rotating two translated copies of a carving into each other
   therefore has no physical generator, and e^{i theta Q} leaks out of the physical space by |sin theta|.
2. Composite sites (D-comp): pair each dynamical site with one neighbour into a dimer; one qubit plays the gauge
   role tau, the other the matter role sigma (D-roles). The bond between neighbouring dimers I, J of type lambda is
   (tau^lambda_I tau^lambda_J)(sigma_I . sigma_J), weight four. Its support is the four corners of a plaquette,
   pairwise within distance sqrt 2; no closed star of seven sites contains it. The family of such terms is
   covariant under the 24 proper rotations (orbit 24 of the (dimer axis, bond direction) pair); the choice of one is
   the role pattern.
3. Exact solvability with a charge (Yao-Lee form). On a star of four dimers with bond types x, y, z and couplings
   J = (1.0, 0.8, 0.6), exact diagonalization of the 8-qubit spin model gives exactly four levels -3e, -e, e, 3e with
   e = sqrt(Jx^2 + Jy^2 + Jz^2) and degeneracies 32, 96, 96, 32: three Majorana flavours with one mode of energy
   e each, as the Yao-Lee reduction predicts. The total matter spin S = sum sigma/2, a sum of one-qubit operators,
   commutes with H exactly; the largest S^z in the four levels is 1, 2, 2, 1: one flavour excitation raises the
   charge by exactly one, so the complex fermion f = (c^x + i c^y)/2 has charge one under S^z (the zero modes
   carry spin too, so the ground level is a mixture of multiplets, printed).
4. A time-reversal-odd term that keeps the charge: kappa (tau^x_1 tau^z_0 tau^y_2)(sigma_1 . sigma_2) on the path
   1-0-2 is odd under time reversal, commutes with S, and the spin spectrum equals the three-flavour free-fermion
   spectrum with the next-nearest hopping kappa u u (i c_1 c_2), to 1e-12.
5. A layer: the honeycomb (brick-wall) network of dimers with the odd term has, per flavour, Kitaev's Bloch
   Hamiltonian; its lower band has Chern number of modulus one at J = (1, 1, 1), kappa = 0.2 (Fukui-Hatsugai,
   36^2), flipping sign with kappa. The charged complex fermion inherits it, so the layer's chiral edge mode
   carries unit S^z charge.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys

import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 600

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1.0 + 0j, -1.0])
SIG = [X, Y, Z]


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def site_op(n, i, op):
    return kron(*([I2] * i + [op] + [I2] * (n - i - 1)))


def majoranas(n_pairs):
    """2 n Majoranas on n qubits by Jordan-Wigner: gamma_{2j} = Z..Z X_j, gamma_{2j+1} = Z..Z Y_j; {g_a, g_b} = 2 delta."""
    out = []
    for j in range(n_pairs):
        string = [Z] * j
        out.append(kron(*(string + [X] + [I2] * (n_pairs - j - 1))))
        out.append(kron(*(string + [Y] + [I2] * (n_pairs - j - 1))))
    return out


# ------------------------------------------------ 1. one qubit per site: no charge between components
g = majoranas(4)                                        # two sites x four Majoranas: (b^x, b^y, b^z, c) each
b1, c1 = g[0:3], g[3]
b2, c2 = g[4:7], g[7]
D1 = b1[0] @ b1[1] @ b1[2] @ c1
D2 = b2[0] @ b2[1] @ b2[2] @ c2
I16 = np.eye(16, dtype=complex)
P = 0.25 * (I16 + D1) @ (I16 + D2)
Q = 1j * c1 @ c2                                        # the would-be charge density between two components
u12 = 1j * b1[2] @ b2[2]                                # a Z2 link variable of a common component
K12 = 1j * c1 @ u12 @ c2                                # a bond bilinear of one component
anti = np.abs(Q @ D1 + D1 @ Q).max()
leak = [np.linalg.norm((I16 - P) @ expm(1j * th * Q) @ P, 2) for th in (0.3, np.pi / 2)]
check("one qubit per site: a Majorana bilinear between two components is not physical, a bond bilinear of one component is",
      abs(np.trace(P).real - 4) < 1e-12 and np.abs(P @ Q @ P).max() < 1e-12 and anti < 1e-12
      and abs(np.linalg.norm(P @ K12 @ P, 2) - 1) < 1e-12 and abs(leak[0] - abs(np.sin(0.3))) < 1e-12 and abs(leak[1] - 1) < 1e-12,
      f"physical projector rank {np.trace(P).real:.0f}; |P (i c_j c_k) P| = {np.abs(P @ Q @ P).max():.0e}; the bilinear anticommutes "
      f"with D_j ({anti:.0e}); the bond bilinear survives with norm {np.linalg.norm(P @ K12 @ P, 2):.3f}; leakage of exp(i theta Q) "
      f"out of the physical space {leak[0]:.4f} at theta = 0.3 (= |sin theta|) and {leak[1]:.0f} at pi/2")

# ------------------------------------------------ 2. the composite bond term's support and covariance
tau_I, sig_I, tau_J, sig_J = (0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1)      # parallel dimers along z, bond along x
support = [tau_I, sig_I, tau_J, sig_J]
dists = [np.linalg.norm(np.subtract(a, b)) for a, b in itertools.combinations(support, 2)]
stars_containing = 0
for s in itertools.product(range(-2, 4), repeat=3):
    star = {s} | {tuple(np.add(s, d)) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]}
    stars_containing += all(p in star for p in support)
rots = [np.array(Pm) * np.array(sg)[:, None] for Pm in itertools.permutations(np.eye(3, dtype=int)) for sg in itertools.product((1, -1), repeat=3)]
rots = [R for R in rots if round(np.linalg.det(R)) == 1]
orbit = {(tuple(R @ np.array([0, 0, 1])), tuple(R @ np.array([1, 0, 0]))) for R in rots}
check("the composite bond term sits on a plaquette's four corners, in no single star, and its family is covariant",
      len(rots) == 24 and max(dists) - np.sqrt(2) < 1e-12 and stars_containing == 0 and len(orbit) == 24,
      f"weight 4; pairwise distances up to {max(dists):.3f}; closed stars containing the support: {stars_containing}; "
      f"orbit of the (dimer axis, bond direction) pair under the 24 proper rotations: {len(orbit)}")

# ------------------------------------------------ 3. Yao-Lee reduction on a star of four dimers
n_dim = 4                                               # dimers 0 (centre), 1, 2, 3 (leaves); qubit 2i = tau_i, 2i+1 = sigma_i
nq = 2 * n_dim
dim = 2 ** nq
Jc = {1: (0, 1.0), 2: (1, 0.8), 3: (2, 0.6)}           # leaf -> (bond type, coupling)


def tau(i, a):
    return site_op(nq, 2 * i, SIG[a])


def sig(i, a):
    return site_op(nq, 2 * i + 1, SIG[a])


def bond(i, j, lam, J):
    return J * (tau(i, lam) @ tau(j, lam)) @ sum(sig(i, a) @ sig(j, a) for a in range(3))


H = sum(bond(0, leaf, lam, J) for leaf, (lam, J) in Jc.items())
Stot = [0.5 * sum(sig(i, a) for i in range(n_dim)) for a in range(3)]
comm_S = max(np.abs(H @ S - S @ H).max() for S in Stot)
ev, V = np.linalg.eigh(H)
eps = np.sqrt(sum(J * J for _, J in Jc.values()))
levels = sorted({round(e, 8) for e in ev})
degs = [int(np.sum(np.abs(ev - lv) < 1e-6)) for lv in levels]
pred = [round(x, 8) for x in (-3 * eps, -eps, eps, 3 * eps)]
Sz = Stot[2]
S2 = sum(S @ S for S in Stot)
sz_max, multiplets = [], []
for lv in levels:
    idx = np.abs(ev - lv) < 1e-6
    W = V[:, idx]
    szv = np.linalg.eigvalsh(W.conj().T @ Sz @ W)
    sz_max.append(int(round(szv.max())))
    s2v = np.linalg.eigvalsh(W.conj().T @ S2 @ W)
    spins = [round((-1 + np.sqrt(1 + 4 * x)) / 2, 6) for x in s2v]          # S from S(S+1)
    multiplets.append({int(round(sv)): int(round(spins.count(sv) / (2 * sv + 1))) for sv in sorted(set(spins))})
check("four dimers in a star: exactly four levels -3e, -e, e, 3e with degeneracies 32, 96, 96, 32; the matter spin is conserved and one flavour excitation raises the largest S^z by one",
      comm_S < 1e-12 and len(levels) == 4 and np.allclose(levels, pred, atol=1e-8) and degs == [32, 96, 96, 32]
      and sz_max == [1, 2, 2, 1],
      f"[H, S] = {comm_S:.0e}; e = {eps:.6f}; levels {[round(l, 6) for l in levels]} with degeneracies {degs}; "
      f"largest S^z per level {sz_max}; multiplets (spin: count) per level {multiplets}")

# ------------------------------------------------ 4. a time-reversal-odd term that keeps the charge, still free
kappa = 0.35
H3 = kappa * (tau(1, 0) @ tau(0, 2) @ tau(2, 1)) @ sum(sig(1, a) @ sig(2, a) for a in range(3))
Tmat = kron(*([Y] * nq))                                # time reversal: T A T^-1 = Y..Y conj(A) Y..Y
T_H = Tmat @ H.conj() @ Tmat
T_H3 = Tmat @ H3.conj() @ Tmat
comm_S3 = max(np.abs(H3 @ S - S @ H3).max() for S in Stot)
ev3 = np.linalg.eigvalsh(H + H3)


def free_spectrum(A):
    """Many-body energies of H = (i/2) c^T A c for three flavours (each positive single-particle energy taken -+)."""
    lam = np.linalg.eigvals(1j * A).real                 # comes in -+ pairs; each positive one is a mode
    pos = [e for e in lam if e > 1e-9]
    zero = int(np.sum(np.abs(lam) <= 1e-9)) // 2         # a pair of zero eigenvalues is one zero mode
    one = [0.0]
    for e in pos:
        one = [x + s * e for x in one for s in (1, -1)]
    one = sorted(one * (2 ** zero))
    three = [0.0]
    for _ in range(3):
        three = [x + y for x in three for y in one]
    return np.array(sorted(three))


A = np.zeros((4, 4))
for leaf, (lam, J) in Jc.items():                      # tau^l_0 tau^l_leaf (sigma.sigma) = u sum_a i c^a_leaf c^a_0
    A[leaf, 0] += J
    A[0, leaf] -= J
A3 = A.copy()
A3[1, 2] += kappa                                       # kappa u_10 u_02 sum_a i c^a_1 c^a_2
A3[2, 1] -= kappa
ratio = dim // len(free_spectrum(A))
spec_free = np.repeat(free_spectrum(A), ratio)
spec_free3 = np.repeat(free_spectrum(A3), ratio)
dev0 = np.abs(np.sort(ev) - spec_free).max()
dev3 = np.abs(np.sort(ev3) - spec_free3).max()
check("the odd three-dimer term is time-reversal odd, keeps the matter spin, and leaves the spectrum free with next-nearest hopping",
      np.abs(T_H - H).max() < 1e-12 and np.abs(T_H3 + H3).max() < 1e-12 and comm_S3 < 1e-12 and dev0 < 1e-10 and dev3 < 1e-10,
      f"T H T^-1 = H to {np.abs(T_H - H).max():.0e}, T H3 T^-1 = -H3 to {np.abs(T_H3 + H3).max():.0e}; [H3, S] = {comm_S3:.0e}; "
      f"spin spectrum vs three-flavour free spectrum: {dev0:.0e} without and {dev3:.0e} with the odd term (each free level repeated {ratio} times)")

# ------------------------------------------------ 5. a honeycomb layer of dimers: per-flavour Chern number
def bloch(a, b, J, kap):
    """Kitaev's honeycomb Bloch Hamiltonian in the (A, B) basis, (q.n1) = 2 pi a, (q.n2) = 2 pi b."""
    f = 2 * (J[0] * np.exp(2j * np.pi * a) + J[1] * np.exp(2j * np.pi * b) + J[2])
    d = 4 * kap * (np.sin(2 * np.pi * a) - np.sin(2 * np.pi * b) + np.sin(2 * np.pi * (b - a)))
    return np.array([[d, 1j * f], [-1j * np.conj(f), -d]])


def chern(J, kap, N=36):
    grid = np.linspace(0, 1, N, endpoint=False)
    U = {(i, j): np.linalg.eigh(bloch(a, b, J, kap))[1][:, :1] for i, a in enumerate(grid) for j, b in enumerate(grid)}
    tot = 0.0
    for i in range(N):
        for j in range(N):
            q = [U[(i, j)], U[((i + 1) % N, j)], U[((i + 1) % N, (j + 1) % N)], U[(i, (j + 1) % N)]]
            tot += np.angle(np.prod([np.vdot(q[m], q[(m + 1) % 4]) for m in range(4)]))
    return tot / (2 * np.pi)


gap = min(abs(np.linalg.eigvalsh(bloch(a, b, (1, 1, 1), 0.2))[0]) for a in np.linspace(0, 1, 60, endpoint=False)
          for b in np.linspace(0, 1, 60, endpoint=False))
c_plus, c_minus = chern((1, 1, 1), 0.2), chern((1, 1, 1), -0.2)
check("a honeycomb layer of dimers with the odd term: per-flavour Chern number of modulus one, flipping with the sign of the odd term",
      abs(abs(c_plus) - 1) < 1e-6 and abs(c_plus + c_minus) < 1e-6 and gap > 0.1,
      f"J = (1, 1, 1), kappa = 0.2: gap {gap:.3f}, Chern number {c_plus:+.4f}; kappa = -0.2: {c_minus:+.4f}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
