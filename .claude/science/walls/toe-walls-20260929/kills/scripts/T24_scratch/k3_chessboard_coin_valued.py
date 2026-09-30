"""Kill check k3: attack test B1 used a coin-SCALAR covariant chessboard term.  Here the chessboard term is coin-VALUED:
   V = sum_x sum_w eps(x) psi^dag(x) (a_w + b_w.sigma) psi(x+w) + h.c.,  covariant under O with full soldering
   (a_{gw}=a_w, b_{gw}=g b_w, complex a,b), ranges 1-2.
Project onto the 16 zero modes of H0 = sigma.S on the L=8 torus (plane waves at the 8 corners x 2 coin states) and
report the 16x16 block: which corner pairs couple, and is each coupling block a multiple of the 2x2 identity?"""
import itertools, sys
import numpy as np
sys.path.insert(0, "rerun")
from common import O, SIG
rng = np.random.default_rng(99)
L = 8
N = L ** 3
coords = np.array(list(itertools.product(range(L), repeat=3)))
eps = np.array([(-1) ** (x + y + z) for x, y, z in coords], float)
def T(w):
    tgt = (coords + np.array(w)) % L
    perm = (tgt[:, 0] * L + tgt[:, 1]) * L + tgt[:, 2]
    M = np.zeros((N, N)); M[np.arange(N), perm] = 1.0     # (T psi)(x) = psi(x+w)
    return M
corners = list(itertools.product([0, 1], repeat=3))
def planewave(n):
    k = np.pi * np.array(n)
    return np.exp(1j * coords @ k) / np.sqrt(N)
def build_V(r, amp):
    ws = [w for w in itertools.product(range(-r, r + 1), repeat=3) if w != (0, 0, 0)]
    a0 = {w: rng.normal() + 1j * rng.normal() for w in ws}
    b0 = {w: rng.normal(size=3) + 1j * rng.normal(size=3) for w in ws}
    a = {}; b = {}
    for w in ws:
        a[w] = 0; b[w] = np.zeros(3, complex)
    for w in ws:
        for g in O:
            wp = tuple(int(x) for x in g @ np.array(w))
            a[wp] += a0[w] / len(O)
            b[wp] += (g @ b0[w]) / len(O)
    V = np.zeros((2 * N, 2 * N), complex)
    E = np.diag(eps)
    for w in ws:
        t = a[w] * np.eye(2) + sum(b[w][i] * SIG[i] for i in range(3))
        V += np.kron(t, E @ T(w))
    V = amp * (V + V.conj().T) / 2
    return V
# H0 and zero-mode subspace
Tx = [T(e) for e in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
S = [(Tx[a] - Tx[a].T) / 2j for a in range(3)]
H0 = sum(np.kron(SIG[a], S[a]) for a in range(3))
cols = []
lab = []
for n in corners:
    for s in range(2):
        e = np.zeros(2); e[s] = 1
        cols.append(np.kron(e, planewave(n))); lab.append((n, s))
P = np.array(cols).T
assert np.abs(H0 @ P).max() < 1e-12
res = {}
for r in [1, 2]:
    worst_nonscalar = 0.0
    pairs_seen = set()
    for trial in range(5):
        V = build_V(r, 1.0)
        B = P.conj().T @ V @ P                     # 16x16
        for i, n in enumerate(corners):
            for j, m in enumerate(corners):
                blk = B[2 * i:2 * i + 2, 2 * j:2 * j + 2]
                if np.abs(blk).max() > 1e-9:
                    q = tuple((np.array(n) + np.array(m)) % 2)
                    pairs_seen.add((q, "diag" if i == j else "offdiag"))
                    tr = np.trace(blk) / 2
                    worst_nonscalar = max(worst_nonscalar, np.abs(blk - tr * np.eye(2)).max())
    print(f"range {r}: coupled corner pairs (relative wavevector n+m mod 2, kind) seen = {sorted(pairs_seen)}; "
          f"max deviation of a coupling block from a multiple of 1 = {worst_nonscalar:.1e}")
    res[r] = worst_nonscalar
