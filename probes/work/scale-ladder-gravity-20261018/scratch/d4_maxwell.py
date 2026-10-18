"""Whitney 1-form Maxwell on a generic periodic complex (D4 cone): leading symbol, on-shell O(k^4), birefringence."""
import sys, itertools, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
C = pickle.load(open('d4.pkl', 'rb')); tix = {t: i for i, t in enumerate(C.types)}
def edge_ref(v1, v2):
    key, anc = RG._key_pair(v1, v2)
    (t1, t2, rel) = key
    # orientation: class goes from (anc, t1) to (anc+rel, t2); sign +1 if v1 is that start
    sgn = 1 if (tuple(v1[0]) == tuple(anc) and v1[1] == t1 and tuple(np.add(anc, rel)) == tuple(v2[0]) and v2[1] == t2) else -1
    return C.ekey[key], np.array(anc, float), sgn
PRE = []
for vs in C.simp:
    P = np.array([C.pos(v) for v in vs]); E = P[1:] - P[0]; vol = np.sqrt(np.linalg.det(E @ E.T))/24
    tris = []
    for i in range(1, 5):
        for j in range(i+1, 5):
            tris.append((i-1, j-1, [edge_ref(vs[p], vs[q]) for (p, q) in [(0, i), (i, j), (j, 0)]]))
    PRE.append((np.linalg.inv(E), vol, tris))
def maxwell(k):
    k = np.asarray(k, complex); Q = np.zeros((C.E, C.E), complex)
    def F(kk, Ei, tris):
        Fe = np.zeros((4, 4, C.E), complex)
        for a, b, es in tris:
            r = np.zeros(C.E, complex)
            for c, anc, sg in es: r[c] += sg*np.exp(1j*kk @ anc)
            Fe[a, b] = 2*r; Fe[b, a] = -2*r
        return np.einsum('ma,abc,nb->mnc', Ei, Fe, Ei)
    for Ei, vol, tris in PRE:
        Q += 0.5*vol*np.einsum('mnc,mnd->cd', F(-k, Ei, tris), F(k, Ei, tris))
    return Q
def lmap(k):
    M = np.zeros((C.E, 4), complex)
    for (t1, t2, rel), c in C.ekey.items():
        v = C.evec[c]; z = k @ v; ph = np.exp(1j*k @ C.OFF[t1])*(1.0 if abs(z) < 1e-14 else (np.exp(1j*z)-1)/(1j*z))
        M[c] = ph*v
    return M
def gauge(k):           # vertex scalars: A_e = chi(end) - chi(start)
    G = np.zeros((C.E, len(C.types)), complex)
    for (t1, t2, rel), c in C.ekey.items():
        G[c, tix[t2]] += np.exp(1j*np.asarray(k, complex) @ np.array(rel, float)); G[c, tix[t1]] -= 1
    return G
rng = np.random.default_rng(1)
k = 0.4*rng.standard_normal(4); Q = maxwell(k); s = np.sort(np.linalg.svd(Q, compute_uv=False)); s /= s[-1]
print("nullity", int((s < 1e-10).sum()), "gauge rank", np.linalg.matrix_rank(gauge(k)), "|QG|", np.abs(Q @ gauge(k)).max())
# leading symbol vs continuum
dev = 0
for _ in range(4):
    kd = rng.standard_normal(4); kd /= np.linalg.norm(kd); A = rng.standard_normal(4); r = []
    for e in (2e-3, 1e-3):
        kk = e*kd; Fc = 1j*(np.outer(kk, A) - np.outer(A, kk)); cont = 0.5*np.real(np.sum(np.conj(Fc)*Fc))
        r.append(np.real(np.conj(lmap(kk) @ A) @ maxwell(kk) @ (lmap(kk) @ A))/cont)
    dev = max(dev, abs((4*r[1]-r[0])/3 - 1))
print("leading symbol / continuum - 1:", f"{dev:.1e}")
pickle.dump(None, open('/dev/null', 'wb'))
