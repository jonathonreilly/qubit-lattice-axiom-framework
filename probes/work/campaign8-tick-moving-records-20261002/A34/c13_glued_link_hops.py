"""A34 c13: glued covariance of A40's light links and charged matter hops (own code).

Coarse lattice of V places; the link qubit between x and x+e_a sits on an E place. Glued action: a proper turn R about
a V place moves places and rotates each qubit's Pauli vector by R (u(R) in SU(2)). Light's link: E = sigma^a (oriented
+a), raising operator U = (sigma^b + i sigma^c)/2, (a,b,c) cyclic. Checks:
 (1) phase c(R,a) with u U u^dag = c U' (or c U'^dag if R reverses the link); in particular a C4 about the link's axis;
 (2) the square (ring) term U1 U2 U3^dag U4^dag: total phase under all 24 turns (uniform coefficient covariant?);
 (3) charged-matter hops psi^dag_x M U psi_{x+e_a} + h.c. covariant under all 24 turns, solved as a real linear
     system for the three matrices M^(a): matter with one turn-scalar component (1x1) and with a vector of 3
     components (the triplet over a singlet vacuum, the minimal glued charge of A40 M2);
 (4) neutral vector matter (no link): covariant hops, and the spectrum of the twisting hop i S^a near k = 0;
 (5) for the vector charged hops found: the matrix holonomy around a coarse square with classical links U -> 1.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import itertools, signal
import numpy as np
signal.alarm(28)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0 + 0j, -1.0]); S = [X, Y, Z]
ROT = []
for P in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3)); [M.__setitem__((P[i], i), s[i]) for i in range(3)]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
assert len(ROT) == 24
def su2(R):
    """u with u sigma^i u^dag = sum_j R_ji sigma^j (found by solving the linear intertwiner equation)."""
    A = []
    for i in range(3):
        tgt = sum(R[j, i] * S[j] for j in range(3))
        A.append(np.kron(np.eye(2), S[i].T) - np.kron(tgt, np.eye(2)))  # u S_i - tgt u = 0, row-major vec
    A = np.vstack(A); _, sv, vh = np.linalg.svd(A); u = vh[-1].conj().reshape(2, 2)
    u = u / np.sqrt(abs(np.linalg.det(u))); return u
cyc = {0: (1, 2), 1: (2, 0), 2: (0, 1)}
def Uop(a):
    b, c = cyc[a]; return (S[b] + 1j * S[c]) / 2
def image(R, a):
    v = R @ np.eye(3)[a]; ap = int(np.argmax(np.abs(v))); return ap, int(np.sign(v[ap]))
def phase(R, a):
    u = su2(R); W = u @ Uop(a) @ u.conj().T; ap, s = image(R, a)
    T = Uop(ap) if s > 0 else Uop(ap).conj().T
    c = np.vdot(T, W) / np.vdot(T, T); assert np.allclose(W, c * T, atol=1e-12); return c
# (1)
C4z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float)
print("(1) phase of a z-link's raising operator under a quarter turn about its own axis:", np.round(phase(C4z, 2), 12))
allc = {(k, a): phase(R, a) for k, R in enumerate(ROT) for a in range(3)}
print("    phases over all 24 turns and 3 link directions:", sorted({complex(np.round(c, 9)) for c in allc.values()}, key=lambda z: (z.real, z.imag)))
# (2) explicit 4-qubit check: the square operator P = U(L1) U(L2) U(L3)^dag U(L4)^dag, pushed forward by each turn,
#     equals the image square's own P' or P'^dag (so a uniform coefficient on P + P^dag respects every turn)
E3 = np.eye(3, dtype=int)
def square_links(y, a, b):
    """canonical square at corner y in plane (a,b): list of (link=(site,dir), op) in circulation order"""
    y = np.array(y)
    return [((tuple(y), a), "U"), ((tuple(y + E3[a]), b), "U"), ((tuple(y + E3[b]), a), "D"), ((tuple(y), b), "D")]
def op(a, kind):
    return Uop(a) if kind == "U" else Uop(a).conj().T
def push_link(R, link):
    x, a = link; v = R @ E3[a]; ap = int(np.argmax(np.abs(v))); s = int(np.sign(v[ap])); xr = R @ np.array(x)
    return ((tuple(xr), ap), +1) if s > 0 else ((tuple(xr - E3[ap]), ap), -1)
worst = 0.0
for R in ROT:
    u = su2(R)
    for a, b in ((0, 1), (0, 2), (1, 2)):
        L = square_links((0, 0, 0), a, b)
        imgs = []
        for (link, kind) in L:
            (il, s) = push_link(R, link)
            imgs.append((il, u @ op(link[1], kind) @ u.conj().T))
        sites = [np.array(l[0]) for (l, _) in imgs]
        lo = np.min(np.array([sp for sp in sites]), axis=0)
        dirs = sorted({l[1] for (l, _) in imgs}); a2, b2 = dirs
        K = square_links(tuple(lo), a2, b2)
        order = {k[0]: i for i, k in enumerate(K)}
        f = [None] * 4
        for (il, m) in imgs:
            f[order[il]] = m
        rot = f[0]
        for m in f[1:]: rot = np.kron(rot, m)
        canon = op(K[0][0][1], K[0][1])
        for (l, kind) in K[1:]: canon = np.kron(canon, op(l[1], kind))
        worst = max(worst, min(np.abs(rot - canon).max(), np.abs(rot - canon.conj().T).max()))
print("(2) square term pushed forward by each of 24 turns, 3 planes: max distance to the image square's P or P^dag =",
      f"{worst:.1e}")
# (3)/(4) covariant hops: unknown real vector = (Re, Im) of M^(0), M^(1), M^(2) (each d x d)
def covariant_hops(d, rep, with_link):
    n = 3 * d * d
    def idx(a): return slice(a * d * d, (a + 1) * d * d)
    rows = []
    for k, R in enumerate(ROT):
        D = rep(R)
        for a in range(3):
            ap, s = image(R, a); c = allc[(k, a)] if with_link else 1.0
            # map: M^(a) -> c D M D^T  must equal M^(ap) (s>0) or M^(ap)^dag (s<0)
            L = np.zeros((d * d, n), complex); Rm = np.zeros((d * d, n), complex)
            for e in range(d * d):
                E = np.zeros(d * d); E[e] = 1; Em = E.reshape(d, d)
                L[:, a * d * d + e] = (c * D @ Em @ D.T).reshape(-1)
            Rm[:, idx(ap)] = np.eye(d * d)
            # complex-linear for s>0; for s<0 the target is conj-transposed: handle in real form
            if s > 0:
                A = L - Rm; Areal = np.block([[A.real, -A.imag], [A.imag, A.real]])
            else:
                # c D M D^T - (M')^dag = 0 ; (M')^dag_ij = conj(M'_ji)
                Pt = np.zeros((d * d, d * d))
                for i in range(d):
                    for j in range(d): Pt[i * d + j, j * d + i] = 1
                B = np.zeros((d * d, n), complex); B[:, idx(ap)] = Pt
                Areal = np.block([[L.real, -L.imag], [L.imag, L.real]]) - np.block([[B.real, B.imag], [B.imag, -B.real]])
            rows.append(Areal)
    A = np.vstack(rows); _, sv, vh = np.linalg.svd(A)
    null = vh[np.sum(sv > 1e-9):]
    return [ (v[:n] + 1j * v[n:]).reshape(3, d, d) for v in null ]
scalar = covariant_hops(1, lambda R: np.eye(1), True)
vector = covariant_hops(3, lambda R: R, True)
neutral = covariant_hops(3, lambda R: R, False)
print("(3) charged hops through light's link, covariant under all 24 turns: turn-scalar matter:", len(scalar),
      "real parameters; vector (triplet) matter:", len(vector), "real parameters")
print("(4) neutral vector matter, no link: covariant hops:", len(neutral), "real parameters")
Sx = [np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]), np.array([[0, 0, 1j], [0, 0, 0], [-1j, 0, 0]]),
      np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])]
basis = np.array([np.concatenate([m.reshape(-1).real, m.reshape(-1).imag]) for m in
                  [np.concatenate([h.reshape(-1) for h in hs]) for hs in neutral]])
target = np.concatenate([np.concatenate([(1j * Sx[a]).reshape(-1) for a in range(3)]).real,
                         np.concatenate([(1j * Sx[a]).reshape(-1) for a in range(3)]).imag])
res = np.linalg.lstsq(basis.T, target, rcond=None)[0]
print("    i S^a lies in that space: residual", f"{np.linalg.norm(basis.T @ res - target):.1e}")
dirs = np.random.default_rng(3).normal(size=(200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
sl = []
for n in dirs:
    q = 1e-4 * n
    H = sum(1j * Sx[a] * np.exp(-1j * q[a]) + (1j * Sx[a] * np.exp(-1j * q[a])).conj().T for a in range(3))
    sl.append(np.sort(np.linalg.eigvalsh(H)) / 1e-4)
sl = np.array(sl)
print("    hop i S^a: slopes at k=0 over 200 directions: min/max per band", np.round(sl.min(0), 4), np.round(sl.max(0), 4))
# (5) matrix holonomy of the vector charged hops around a coarse xy square, classical links U -> 1
for v, hs in enumerate(vector):
    Mx, My = hs[0], hs[1]
    Hol = Mx @ My @ Mx.conj().T @ My.conj().T
    ev = np.linalg.eigvals(Hol)
    print(f"(5) vector charged hop #{v}: |M_x| = {np.linalg.norm(Mx):.3f}; square holonomy eigenvalues", np.round(ev, 4))
