#!/usr/bin/env python3
"""T61 D3: interacting matter in the natural (affine-in-e) coupling class, exact diagonalisation.

2D walker: two orbitals per site, hop along axis j carries sigma_a e_a^j (a in {x,y}):
  H(e) = sum_{j,a} e_a^j M_{ja} + V sum_bonds n_r n_r'
  M_{ja} = sum_r [ psi^dag_r (sigma_a / 2i) eta psi_{r+j} + h.c. ]
4x2 torus, antiperiodic both ways (free spectrum gapped), N=8 fermions (half filling).
Since H is affine in e (interaction is e-independent), E0(e) = min_psi <H(e)> is concave in e.
"""
import numpy as np, itertools, sys
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from scipy.linalg import expm

Lx, Ly = 4, 2
NSITE = Lx * Ly
NMODE = 2 * NSITE
NPART = NMODE // 2
sig = {0: np.array([[0, 1], [1, 0]], complex), 1: np.array([[0, -1j], [1j, 0]], complex)}  # sigma_x, sigma_y

def site(ix, iy): return (ix % Lx) + Lx * (iy % Ly)
def mode(r, s): return 2 * r + s

# basis: all bitstrings with NPART ones
states = np.array([b for b in range(1 << NMODE) if bin(b).count("1") == NPART], dtype=np.int64)
states.sort()
dim = len(states)
def index_of(x):
    return np.searchsorted(states, x)

def hop_matrix(p, q):
    """matrix of c^dag_p c_q on the Fock basis (p != q)."""
    S = states
    occq = (S >> q) & 1
    occp = (S >> p) & 1
    m = (occq == 1) & (occp == 0)
    src = S[m]
    new = src ^ (1 << q) ^ (1 << p)
    lo, hi = min(p, q), max(p, q)
    between = ((1 << hi) - 1) & ~((1 << (lo + 1)) - 1)
    sign = 1 - 2 * (np.bitwise_count(src & between) & 1).astype(np.int64)
    rows = index_of(new); cols = np.nonzero(m)[0]
    return sp.csr_matrix((sign.astype(float), (rows, cols)), shape=(dim, dim))

cache = {}
def cdc(p, q):
    if (p, q) not in cache:
        cache[(p, q)] = hop_matrix(p, q)
    return cache[(p, q)]

# M_{j,a}
def build_M():
    M = {}
    for j in range(2):
        for a in range(2):
            acc = sp.csr_matrix((dim, dim), dtype=complex)
            for ix in range(Lx):
                for iy in range(Ly):
                    r = site(ix, iy)
                    if j == 0:
                        r2 = site(ix + 1, iy); eta = -1.0 if ix == Lx - 1 else 1.0
                    else:
                        r2 = site(ix, iy + 1); eta = -1.0 if iy == Ly - 1 else 1.0
                    for s in range(2):
                        for s2 in range(2):
                            amp = sig[a][s, s2] / (2j) * eta
                            if amp == 0: continue
                            acc = acc + amp * cdc(mode(r, s), mode(r2, s2))
            M[(j, a)] = (acc + acc.getH()).tocsr()
    return M

def build_int():
    # V sum over bonds n_r n_r'; number operator per site
    occ = np.zeros((NSITE, dim))
    for r in range(NSITE):
        for s in range(2):
            occ[r] += (states >> mode(r, s)) & 1
    diag = np.zeros(dim)
    for ix in range(Lx):
        for iy in range(Ly):
            r = site(ix, iy)
            for r2 in (site(ix + 1, iy), site(ix, iy + 1)):
                diag += occ[r] * occ[r2]
    return sp.diags(diag)

M = build_M()
HINT = build_int()

def Hfull(e, V):
    H = V * HINT.astype(complex)
    for j in range(2):
        for a in range(2):
            H = H + e[a, j] * M[(j, a)]
    return H.tocsr()

def ground(e, V, want_vec=False):
    H = Hfull(e, V)
    w, v = eigsh(H, k=2, which="SA")
    o = np.argsort(w); w = w[o]; v = v[:, o]
    if want_vec: return w[0], w[1] - w[0], v[:, 0]
    return w[0]

def gradient(e0, V):
    E0, gap, vec = ground(e0, V, True)
    G = np.zeros((2, 2))
    for j in range(2):
        for a in range(2):
            G[a, j] = np.real(np.vdot(vec, M[(j, a)] @ vec))
    return E0, gap, G

if __name__ == "__main__":
    rng = np.random.default_rng(1)
    print("dim =", dim)
    # free-check: V=0 vs analytic sum over allowed k
    e = np.array([[1.0, 0.3], [0.2, 0.9]])
    kx = 2 * np.pi * (np.arange(Lx) + 0.5) / Lx; ky = 2 * np.pi * (np.arange(Ly) + 0.5) / Ly
    Efree = 0.0
    for a_ in kx:
        for b_ in ky:
            s = np.array([np.sin(a_), np.sin(b_)])
            Efree -= np.linalg.norm(e @ s)
    print("free check: ED %.10f  analytic %.10f" % (ground(e, 0.0), Efree))
    Vs = [0.0, 0.5, 1.0, 2.0]
    # (ii) evenness and (i) concavity
    for V in Vs:
        worst = 1e9
        for _ in range(40):
            e1 = rng.normal(size=(2, 2)) * 0.8 + np.eye(2); e2 = rng.normal(size=(2, 2)) * 0.8 + np.eye(2)
            mid = ground(0.5 * (e1 + e2), V) - 0.5 * (ground(e1, V) + ground(e2, V))
            worst = min(worst, mid)
        ev = abs(ground(e, V) - ground(-e, V))
        print("V=%.1f  concavity: min over 40 pairs of E(mid)-avg = %+.3e   evenness |E(e)-E(-e)| = %.2e" % (V, worst, ev))
    # (iii) curvatures
    axis = np.diag([1.0, -1.0]) / np.sqrt(2)
    face = np.array([[0, 1.0], [1.0, 0]]) / np.sqrt(2)
    rows = []
    for V in Vs:
        E0, gap, G = gradient(np.eye(2), V)
        K = float(np.trace(G))  # <H_hop> at e=1
        out = {"V": V, "E0": E0, "gap": gap, "K": K, "G": G}
        for name, eps in (("axis", axis), ("face", face)):
            h = 0.04
            fv = lambda t: ground(expm(t * eps / 2), V)
            fl = lambda t: ground(np.eye(2) + t * eps / 2, V)
            def d2(f):
                c1 = (f(h) + f(-h) - 2 * f(0.0)) / h**2
                c2 = (f(h / 2) + f(-h / 2) - 2 * f(0.0)) / (h / 2)**2
                return (4 * c2 - c1) / 3
            cvp = d2(fv); cl = d2(fl)
            dia = float(np.sum(G * (eps @ eps / 4)))  # g . e''
            out[name] = (cvp, cl, dia)
        rows.append(out)
        print("V=%.1f  E0=%+.6f gap=%.4f  K=<H_hop>=%+.6f  G=diag(%.5f,%.5f)" % (V, E0, gap, K, G[0, 0], G[1, 1]))
        for name in ("axis", "face"):
            cvp, cl, dia = out[name]
            print("      %s: c_vp=%+.6f  c_lin(affine)=%+.6f  diamagnetic g.e''=%+.6f  c_lin+dia=%+.6f  (K/8=%+.6f)" % (name, cvp, cl, dia, cl + dia, K / 8))
    print("\nseagull needed s(V) = -c_vp(V):")
    for name in ("axis", "face"):
        base = -rows[0][name][0]
        print("  %s: " % name + "  ".join("V=%.1f: %.5f (x%.3f)" % (r["V"], -r[name][0], -r[name][0] / base) for r in rows))
    np.save("d3_rows.npy", np.array([[r["V"], r["K"], r["axis"][0], r["axis"][1], r["face"][0], r["face"][1]] for r in rows]))
