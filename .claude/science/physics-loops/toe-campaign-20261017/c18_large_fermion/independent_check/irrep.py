"""Item 4: the ground doublet on the L = 4 (and L = 8) torus and its 2O irrep under the twisted
site rotations; both lifts to 2O; twist sign; comparison with the single-site cluster doublet."""
import itertools
import numpy as np
import scipy.sparse as sp, scipy.sparse.linalg as spl
from model import *

FD = dict(square=1, triangle=0, plaquette=1, tube=1)
u = solve_gauge(FD)
PS = [(R, *psg(u, R)) for R in ROTS]

# ---- 2O as unit quaternions, own construction
Q = []
for i in range(4):
    for s in (1, -1):
        v = np.zeros(4); v[i] = s; Q.append(v)
for sg in itertools.product((1, -1), repeat=4): Q.append(np.array(sg) / 2)
for i, j in itertools.combinations(range(4), 2):
    for a, b in itertools.product((1, -1), repeat=2):
        v = np.zeros(4); v[i] = a / np.sqrt(2); v[j] = b / np.sqrt(2); Q.append(v)
assert len(Q) == 48
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
def qrot(q):
    w, x, y, z = q
    return np.rint(np.array([[1-2*(y*y+z*z), 2*(x*y-w*z), 2*(x*z+w*y)], [2*(x*y+w*z), 1-2*(x*x+z*z), 2*(y*z-w*x)],
                             [2*(x*z-w*y), 2*(y*z+w*x), 1-2*(x*x+y*y)]])).astype(int)
def qid(q): return [i for i, p in enumerate(Q) if np.allclose(p, q)][0]
def rid(R): return [i for i, S in enumerate(ROTS) if (S == R).all()][0]
QR = [rid(qrot(q)) for q in Q]
chiE12 = np.array([2 * q[0] for q in Q])
chiA2 = np.array([(-1) ** w1(ROTS[QR[i]]) for i in range(48)])
IRR = {'E1/2': chiE12, 'E5/2': chiE12 * chiA2}
def label(ch):
    return {k: round(float(np.real(np.vdot(v, ch))) / 48, 6) for k, v in IRR.items()}

def lifts(D):
    """D: list of 24 matrices (twisted op restricted to an invariant subspace) indexed like ROTS.
    Return all sign assignments M(q) = eps(q) D[R(q)] that are homomorphisms of 2O."""
    out = []
    for signs in itertools.product((1, -1), repeat=48 // 2):
        pass
    # generators: a = C4z lift, b = C3 lift; BFS
    qa = np.array([1, 0, 0, 1]) / np.sqrt(2); qb = np.array([1, 1, 1, 1]) / 2
    for sa, sb in itertools.product((1, -1), repeat=2):
        M = {qid(qa): sa * D[QR[qid(qa)]], qid(qb): sb * D[QR[qid(qb)]]}
        frontier = list(M); ok = True
        while frontier and ok:
            new = []
            for x in list(M):
                for g in (qid(qa), qid(qb)):
                    y = qid(qmul(Q[x], Q[g])); My = M[x] @ M[g]
                    if y in M:
                        if not np.allclose(M[y], My): ok = False; break
                    else: M[y] = My; new.append(y)
                if not ok: break
            frontier = new
        if ok and len(M) == 48:
            # homomorphism and consistency with D up to sign
            assert all(np.allclose(np.abs(np.vdot(M[i].ravel(), D[QR[i]].ravel())), np.vdot(D[QR[i]].ravel(), D[QR[i]].ravel()).real) for i in M)
            assert np.allclose(M[qid(np.array([-1, 0, 0, 0]))], -np.eye(len(D[0])))
            out.append(((sa, sb), np.array([np.trace(M[i]) for i in range(48)])))
    return out

L = 4
def build(L, t1, t2, lam):
    sites = list(itertools.product(range(L), repeat=3)); sid = {n: i for i, n in enumerate(sites)}
    V = lambda n, c: 12 * sid[tuple(x % L for x in n)] + c
    rows, cols, vals = [], [], []
    for n in sites:
        for j, (c1, c2, sh, kind) in enumerate(ETYPES):
            z = -(t1 if kind == 'o' else t2) * (-1.0) ** u[j]
            a, b = V(n, c1), V(tuple(x + y for x, y in zip(n, sh)), c2)
            rows += [b, a]; cols += [a, b]; vals += [z, np.conj(z)]
        for cs in TRIS:
            for q, r in zip(cs, cs[1:] + cs[:1]):
                z = 1j * lam * (-1.0) ** u[EKEY[(q, r, (0, 0, 0))]]
                rows += [V(n, r), V(n, q)]; cols += [V(n, q), V(n, r)]; vals += [z, np.conj(z)]
    H = sp.csr_matrix((vals, (rows, cols)), shape=(12 * L**3, 12 * L**3))
    G = []
    for R, eta, s in PS:
        rr, cc, vv = [], [], []
        for n in sites:
            for c in range(12):
                rr.append(V(tuple(int(x) for x in R @ np.array(n)), rot_corner(R, c))); cc.append(V(n, c))
                vv.append(eta[c] * (-1.0) ** int(np.dot(s, n)))
        G.append(sp.csr_matrix((vv, (rr, cc)), shape=H.shape))
    return H, G

for (t1, t2, lam) in ((-1.0, 0.1, -0.5), (-1.0, 0.3, -0.5), (-1.0, 0.1, 0.5), (-1.0, 0.2, -0.3), (-1.0, -0.1, -0.5)):
    H, G = build(4, t1, t2, lam)
    Hd = H.toarray()
    assert np.allclose(Hd, Hd.conj().T)
    comm = max(abs(g @ H - H @ g).max() for g in G)
    ev, Vv = np.linalg.eigh(Hd)
    m = int(np.sum(ev - ev[0] < 1e-8)); P = Vv[:, :m]
    for tw, twn in ((1j, 'i^w1'), (-1j, '(-i)^w1')):
        D = [(tw ** w1(R)) * (P.conj().T @ (g @ P)) for (R, eta, s), g in zip(PS, G)]
        labs = [(sgn, label(ch)) for sgn, ch in lifts(D)]
        print(f"L=4 t1={t1:+} t2={t2:+} lam={lam:+}: [H,G_R] max {comm:.0e}; ground E={ev[0]:.6f} deg {m}; next {ev[m]-ev[0]:.4f};"
              f" twist {twn}: lifts (sign of C4z-lift, C3-lift) -> {labs}")
    # fixed-convention label: lift with sign(+1) on qa, twist i^w1
# single-site cluster doublet in the same convention
print("\nsingle-site cluster (t2 = 0, one site), same G_R restricted to the origin site:")
for lam in (-0.5, 0.5):
    Hc = bloch(u, np.zeros(3), -1.0, 0.0, lam)
    ev, Vv = np.linalg.eigh(Hc); P = Vv[:, :2]
    D = [(1j ** w1(R)) * (P.conj().T @ Wmat(R, eta) @ P) for R, eta, s in PS]
    print(f"  lam={lam:+}: E={ev[0]:.4f} deg {int(np.sum(ev-ev[0]<1e-8))} gap {ev[2]-ev[0]:.4f}; lifts -> {[(sg, label(ch)) for sg, ch in lifts(D)]}")

# adjoint action on the doublet: the 2x2 'spin' generators transform as T1 (vector) in both cases
print("\nadjoint (SO(3)) image of the doublet rep: compare D_R sigma D_R^dag with R acting on a vector")
H, G = build(4, -1.0, 0.1, -0.5)
ev, Vv = np.linalg.eigh(H.toarray()); P = Vv[:, :2]
D = [(1j ** w1(R)) * (P.conj().T @ (g @ P)) for (R, eta, s), g in zip(PS, G)]
pa = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
Ad = [np.array([[0.5 * np.real(np.trace(pa[i] @ d @ pa[j] @ d.conj().T)) for j in range(3)] for i in range(3)]) for d in D]
# find a fixed orthogonal basis change O with Ad_R = O R O^T for all R  (Ad is a real 3-dim rep; compare characters)
print("  characters of adjoint vs vector rep (should agree class by class):",
      np.allclose([np.trace(a) for a in Ad], [np.trace(R) for R in ROTS]))

# L = 8: lowest levels by sparse diagonalization
H8, _ = build(8, -1.0, 0.1, -0.5)
w = spl.eigsh(H8, k=8, which='SA', return_eigenvectors=False)
print("\nL=8, (t1,t2,lam)=(-1,0.1,-0.5): lowest 8 levels", np.round(np.sort(w), 6))
