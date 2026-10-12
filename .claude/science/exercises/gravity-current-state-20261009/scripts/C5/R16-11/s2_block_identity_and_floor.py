"""R16-11 s2 (written before running).  Operator-level algebra checks of the dressing-transfer lemmas on a
small qubit quantum-link cluster (2D U(1) link qubits, 2x2 plaquettes, open cluster: 12 links, 4096 states;
integer Gauss law G(v) = sum of S^z on links at vertex v with signs).  This is an ALGEBRA check of
Lemmas P (projection), F (floor) and M (support-moment, U(1) order) -- not a phase computation.
Pre-registered expectations:
 (P) For psi in H_0 = {G(v)=0 all v}: m1(C; psi, H') == m1(C; psi, H''), H'' = sum_X Pi_X h_X Pi_X
     (Pi_X = projector on G(v)=0 for v touching X), for an arbitrary (law-violating) H' = sum_X h_X.
     Equality to ~1e-12.
 (F) For psi with leakage: |m1(H') - m1(H'')| <= sum_X ||[C^+,[h_X,C]]|| (2 sqrt(q_X) + q_X), q_X = <1-Pi_X>.
 (M) Twirled (gauge-invariant) random local h: ||[C^+,[h,C]]|| has slope 2 in k (U(1): constant strain is
     pure gauge only) and obeys ||[C^+,[h,C]]|| <= 4 ||h|| (S sum_s |c_s| |k| |pos_s-x0|)^2 ; untwirled: slope 0.
"""
import numpy as np, itertools
rng = np.random.default_rng(11)
# 2D cluster: vertices (i,j), 0<=i,j<=2; links: horizontal ((i,j)->(i+1,j)) i<2 ; vertical ((i,j)->(i,j+1)) j<2
links = [((i, j), 0) for i in range(2) for j in range(3)] + [((i, j), 1) for i in range(3) for j in range(2)]
n = len(links); D = 2**n
pos = np.array([np.array(v, float) + 0.5*np.eye(2)[d] for (v, d) in links])
verts = [(i, j) for i in range(3) for j in range(3)]
# S^z eigenvalues for each basis state: bit b -> sz = b - 1/2
bits = ((np.arange(D)[:, None] >> np.arange(n)[None, :]) & 1)
sz = bits - 0.5
def Gv(v):
    g = np.zeros(D)
    for s, (w, d) in enumerate(links):
        if w == v: g += sz[:, s]                 # outgoing
        if tuple(np.array(w) + np.eye(2, dtype=int)[d]) == v: g -= sz[:, s]   # incoming
    return g
Gs = {v: Gv(v) for v in verts}
# Gauss-law values are not all zero-able at open-boundary corner vertices with half-integer S^z; use the
# background-charge convention: H_0 = {G(v) = G0(v)} with G0 the values of the reference state all-up (bits=1)
# choose the largest Gauss sector (background-charge pattern) as H_0, so the test is non-trivial
keys = np.round(np.stack([Gs[v] for v in verts], 1)*2).astype(int)
uniq, inv, cnt = np.unique(keys, axis=0, return_inverse=True, return_counts=True)
ref = int(np.argmax(cnt[inv]))
G0 = {v: Gs[v][ref] for v in verts}
inH0 = np.all([np.isclose(Gs[v], G0[v]) for v in verts], axis=0)
print("cluster: %d links, dim %d, dim H_0 = %d" % (n, D, inH0.sum()))
def links_of(X): return X
def touching(X):
    vs = set()
    for s in X:
        (w, d) = links[s]; vs.add(w); vs.add(tuple(np.array(w) + np.eye(2, dtype=int)[d]))
    return vs
def Pi(X):
    m = np.ones(D, bool)
    for v in touching(X): m &= np.isclose(Gs[v], G0[v])
    return m.astype(float)
def local_term(X, scale=1.0):
    """random Hermitian operator acting on links X (tensor identity elsewhere), as dense DxD"""
    k = len(X); h = rng.normal(size=(2**k, 2**k)) + 1j*rng.normal(size=(2**k, 2**k)); h = (h + h.conj().T)/2*scale
    # embed: index map
    sub = np.zeros(D, int)
    for a, s in enumerate(X): sub += bits[:, s] << a
    rest = np.arange(D).copy()
    for s in X: rest &= ~(1 << s)
    H = np.zeros((D, D), complex)
    same = rest[:, None] == rest[None, :]
    H[same] = h[sub[:, None].repeat(D, 1)[same], sub[None, :].repeat(D, 0)[same]]
    return H
def C_of(k, eps):
    c = np.array([eps[d]*np.exp(1j*np.dot(k, pos[s])) for s, (v, d) in enumerate(links)])
    return (sz @ c), c   # diagonal entries
from scipy.sparse.linalg import eigsh
def dcomm(Cd, H):
    # [C^+,[H,C]] for diagonal C: entries -|C_a - C_b|^2 H_ab (Hadamard form; exact)
    return -np.abs(Cd[:, None] - Cd[None, :])**2 * H
def opnorm(A):
    return abs(eigsh(A, k=1, which='LM', return_eigenvectors=False)[0])
def m1(Cd, H, psi):
    return np.vdot(psi, dcomm(Cd, H) @ psi)
def plaq(i, j):
    return [links.index(((i, j), 0)), links.index(((i, j + 1), 0)), links.index(((i, j), 1)), links.index(((i + 1, j), 1))]
# local terms: the four plaquettes plus two random 5-link sets (so that invariant moves exist inside H_0)
terms = [plaq(0, 0), plaq(1, 0), plaq(0, 1), plaq(1, 1)] + [sorted(set(plaq(0, 0) + [int(rng.integers(n))])) for _ in range(2)]
hs = [local_term(X) for X in terms]
Hp = sum(hs)
Hpp = sum(Pi(X)[:, None]*h*Pi(X)[None, :] for X, h in zip(terms, hs))
# (P)
psi = (rng.normal(size=D) + 1j*rng.normal(size=D))*inH0; psi /= np.linalg.norm(psi)
k = np.array([0.3, 0.1]); eps = np.array([-0.1, 0.3])/np.linalg.norm([-0.1, 0.3])
Cd, c = C_of(k, eps)
a, b = m1(Cd, Hp, psi), m1(Cd, Hpp, psi)
print("(P) m1(H') = %.12f%+.12fi ; m1(H'') = %.12f%+.12fi ; |diff| = %.2e" % (a.real, a.imag, b.real, b.imag, abs(a - b)))
gviol = max(np.abs((Gs[v][:, None] - Gs[v][None, :])*Hpp).max() for v in verts)
gviol0 = max(np.abs((Gs[v][:, None] - Gs[v][None, :])*Hp).max() for v in verts)
print("    max |[G(v),H']| = %.3f (law-violating) ; max |[G(v),H'']| = %.1e" % (gviol0, gviol))
# (F)
chi = (rng.normal(size=D) + 1j*rng.normal(size=D))*(~inH0); chi /= np.linalg.norm(chi)
for eta in [1e-3, 1e-2, 1e-1, 0.3]:
    ps = psi + eta*chi; ps /= np.linalg.norm(ps)
    diff = abs(m1(Cd, Hp, ps) - m1(Cd, Hpp, ps))
    bound = 0.0
    for X, h in zip(terms, hs):
        q = np.vdot(ps, (1 - Pi(X))*ps).real
        bound += opnorm(dcomm(Cd, h))*(2*np.sqrt(q) + q)
    print("(F) eta=%.0e |m1(H')-m1(H'')| = %.3e <= bound %.3e : %s" % (eta, diff, bound, diff <= bound + 1e-12))
# (M)
X = list(range(n))
hfull = local_term(X)
mask = np.ones((D, D), bool)
for v in verts: mask &= np.isclose(Gs[v][:, None], Gs[v][None, :])
htw = hfull*mask
print("(M) twirled h commutes with all G(v): max = %.1e ; nonzero allowed entries: %d" %
      (max(np.abs((Gs[v][:, None] - Gs[v][None, :])*htw).max() for v in verts), mask.sum()))
x0 = pos.mean(axis=0)
for name, d in [('x', [1, 0]), ('diag', [1, 1]), ('gen', [1, 2.3])]:
    d = np.array(d, float); d /= np.linalg.norm(d); e = np.array([-d[1], d[0]])
    ks = np.array([1e-3, 1e-2, 1e-1, 0.3]); ytw, yraw, ratio = [], [], []
    for kk in ks:
        Cd, c = C_of(kk*d, e)
        ytw.append(opnorm(dcomm(Cd, htw))); yraw.append(opnorm(dcomm(Cd, hfull)))
        bnd = 4*opnorm(htw)*(0.5*sum(abs(c[s])*kk*np.linalg.norm(pos[s] - x0) for s in range(n)))**2
        ratio.append(ytw[-1]/bnd)
    print("    dir %-4s twirled slope = %.3f ; untwirled slope = %.3f ; max ratio to U(1) support bound = %.3f" %
          (name, np.polyfit(np.log(ks), np.log(ytw), 1)[0], np.polyfit(np.log(ks), np.log(yraw), 1)[0], max(ratio)))
