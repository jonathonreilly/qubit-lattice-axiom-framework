"""On-shell O(k^4) fingerprints on the Kuhn complex (b=0): scalar P1, Maxwell Whitney, vs Regge TT law."""
import numpy as np, itertools, fem
from fem import SIMPLICES, simplex_geom, edge
g0 = np.eye(4)

def scalar_hol(k):
    S = 0j
    for vs in SIMPLICES:
        E, vol = simplex_geom(vs, g0)
        gp = np.linalg.solve(E, np.array([np.exp(1j*k@v) for v in vs])[1:] - np.exp(1j*k@vs[0]))
        gm = np.linalg.solve(E, np.array([np.exp(-1j*k@v) for v in vs])[1:] - np.exp(-1j*k@vs[0]))
        S += vol * gm @ gp
    return S

def maxwell_hol(k):
    def Fof(k, vs, Einv):
        Fe = np.zeros((4, 4, 15), complex)
        for i in range(1, 5):
            for j in range(i+1, 5):
                r = np.zeros(15, complex)
                for (p, q) in [(0, i), (i, j), (j, 0)]:
                    c, anc, sg = edge(vs[p], vs[q]); r[c] += sg*np.exp(1j*k@anc)
                Fe[i-1, j-1] = 2*r; Fe[j-1, i-1] = -2*r
        return np.einsum('ma,abc,nb->mnc', Einv, Fe, Einv)
    Q = np.zeros((15, 15), complex)
    for vs in SIMPLICES:
        E, vol = simplex_geom(vs, g0); Ei = np.linalg.inv(E)
        Q += 0.5*vol*np.einsum('mnc,mnd->cd', Fof(-k, vs, Ei), Fof(k, vs, Ei))
    return Q

def golden(f, lo, hi):
    gr = (5**.5-1)/2; a, b = lo, hi; c, d = b-gr*(b-a), a+gr*(b-a); fc, fd = f(c), f(d)
    for _ in range(200):
        if fc < fd: b, d, fd = d, c, fc; c = b-gr*(b-a); fc = f(c)
        else: a, c, fc = c, d, fd; d = a+gr*(b-a); fd = f(d)
        if b-a < 1e-15: break
    return (a+b)/2

def kv(ks, om): return np.array([ks[0], ks[1], ks[2], 1j*om])

dirs = {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1), 'face-': (1,-1,0), 'body-': (1,1,-1), 'gen': (3,1,2), 'gen2': (1,-2,3)}
for name, n in dirs.items():
    n = np.array(n, float); n /= np.linalg.norm(n)
    regge = -(1 + (n**4).sum())/12
    res = []
    for km in (0.08, 0.04):
        ks = km*n
        om_s = golden(lambda om: abs(scalar_hol(kv(ks, om))), 0.8*km, 1.1*km)
        def s2(om):
            s = np.sort(np.linalg.svd(maxwell_hol(kv(ks, om)), compute_uv=False)); return s[1]/s[-1]
        om_m = golden(s2, 0.8*km, 1.1*km)
        sv = np.sort(np.linalg.svd(maxwell_hol(kv(ks, om_m)), compute_uv=False)); 
        res.append((km, (om_s**2/km**2-1)/km**2, (om_m**2/km**2-1)/km**2, sv[:4]/sv[-1]))
    (k1, s1, m1, _), (k2, s2_, m2, sv) = res
    # Richardson on alpha (O(k^2) corrections)
    sa = (4*s2_-s1)/3; ma = (4*m2-m1)/3
    print(f"{name:6s} Regge-law {regge:+.6f}  scalar {sa:+.6f}  Maxwell {ma:+.6f}  maxwell sv(on-shell) {np.array2string(sv, precision=1)}")
