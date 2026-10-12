"""C4 / RW / W3 part C: the most general h-local completion (unitary gauge), scalar sector.
L = L_KH(lam, xi=1, eta) + F(a) + sum_i m_i * (5 h-local mass terms) + sum_j c_j * (13 h-local, T-even,
rotation-invariant two-derivative terms with no time derivative on lapse h00 or shift h0i).
Fields Phi(=h00), B (h0i = d_i B), Psi, E (h_ij = -2 Psi delta_ij + 2 d_i d_j E); B = s + E_dot.
M_P^2 = 1, a = -1 (physical sign; |a| sets the unit: mu^2 = |a|/2).  Health test: every root w^2(k) of
det M = 0 real positive with positive Krein energy, for k on a log grid 1e-3..1e3 (IR k << mu to UV k >> mu).
Searches: (S1) masses only, KH in the window-like corner lam = 1.05, eta = 0.5; (S2) masses + 13 breaking
terms O(1); (S3) same with lam free in (1, 2]; report the healthy hits and their structure."""
import sys, time; sys.path.insert(0, '.')
import sympy as sp, numpy as np
from w3_lib import *

lam, eta, a = sp.symbols('lam eta a', real=True)
ms = sp.symbols('m0:5', real=True)
cs = sp.symbols('c0:13', real=True)
Phi, s, Psi, E = [F(n) for n in ('Phi', 's', 'Psi', 'E')]
B = s + dt(E)
xi = 1
Kij = [[-dt(Psi)*(1 if i == j else 0) - sp.diff(s, X[i], X[j]) for j in range(3)] for i in range(3)]
Ktr = sum(Kij[i][i] for i in range(3)); KK = sum(Kij[i][j]**2 for i in range(3) for j in range(3))
L_KH = sp.Rational(1, 2)*(KK - lam*Ktr**2) + xi*(dot(grad(Psi), grad(Psi)) - 2*dot(grad(Phi), grad(Psi))) + eta/2*dot(grad(Phi), grad(Phi))
Fa = a*(-dot(grad(Phi), grad(E)) - sp.Rational(1, 2)*dot(grad(s), grad(s)))
h00 = Phi; h0 = grad(B)
hij = [[-2*Psi*(1 if i == j else 0) + 2*sp.diff(E, X[i], X[j]) for j in range(3)] for i in range(3)]
tr = sum(hij[i][i] for i in range(3))
R = range(3)
masses = [h00**2, dot(h0, h0), sum(hij[i][j]**2 for i in R for j in R), tr**2, h00*tr]
two = [sum(sp.diff(hij[i][j], X[l])**2 for i in R for j in R for l in R),            # (d_k h_ij)^2
       sum(sp.diff(tr, X[l])**2 for l in R),                                            # (d h_ii)^2
       sum(sum(sp.diff(hij[i][j], X[i]) for i in R)**2 for j in R),                     # (d_i h_ij)^2
       sum(sp.diff(hij[i][j], X[i], X[j]) for i in R for j in R)*tr,                    # d_i d_j h_ij h_kk
       sum(dt(hij[i][j])**2 for i in R for j in R),                                     # hdot_ij^2
       dt(tr)**2,                                                                       # hdot_ii^2
       sum(sp.diff(h0[j], X[i])**2 for i in R for j in R),                              # (d_i h_0j)^2
       sum(sp.diff(h0[i], X[i]) for i in R)**2,                                         # (d_i h_0i)^2
       sum(h0[i]*sp.diff(dt(hij[i][j]), X[j]) for i in R for j in R),                   # h_0i d_j hdot_ij
       sum(h0[i]*sp.diff(dt(tr), X[i]) for i in R),                                     # h_0i d_i hdot_jj
       sum(sp.diff(h00, X[i])*sp.diff(tr, X[i]) for i in R),                            # d h00 . d h_jj
       sum(sp.diff(h00, X[i])*sp.diff(hij[i][j], X[j]) for i in R for j in R),         # d_i h00 d_j h_ij
       dot(grad(h00), grad(h00))]                                                       # (d h00)^2
L = L_KH + Fa + sum(m*q for m, q in zip(ms, masses)) + sum(c*q for c, q in zip(cs, two))
t0 = time.time()
M = fourier_matrix(L, [Phi, s, Psi, E])
pars = (lam, eta, a) + ms + cs
cf, Mf, dMf, poly = spectrum_tools(M, pars)
print(f"symbol built in {time.time()-t0:.1f}s; det degree in w^2 = {poly.degree()}")

ks = np.logspace(-3, 3, 19)
def health(pv, ks=ks):
    bad = 0; nmodes = set(); kinds = {}
    for kv in ks:
        try:
            out = classify(cf, Mf, dMf, kv, pv)
        except Exception:
            return 99, {}, set()
        nmodes.add(len(out))
        for tg, r in out:
            if tg != 'healthy':
                bad += 1; kinds[tg] = kinds.get(tg, 0) + 1
    return bad, kinds, nmodes

# sanity: pure KH, a=0 (healthy khronon, 1 mode); W2/KH + anomaly (pathological)
z5, z13 = (0.0,)*5, (0.0,)*13
print("check KH a=0 lam=1.05 eta=0.5:", health((1.05, 0.5, 0.0) + z5 + z13))
print("check KH + anomaly a=-1:", health((1.05, 0.5, -1.0) + z5 + z13))
print("check KH + anomaly + m4=-a/2:", health((1.05, 0.5, -1.0, 0, 0, 0, 0, 0.5) + z13))

rng = np.random.default_rng(20261011)
def search(label, n, gen):
    hits = []; best = (1e9, None)
    t0 = time.time()
    for i in range(n):
        pv = gen()
        b, kinds, nm = health(pv)
        if b < best[0]: best = (b, pv, kinds, nm)
        if b == 0: hits.append((pv, nm))
    print(f"{label}: {n} samples, {len(hits)} healthy at all 19 k; best bad count {best[0]} {best[2] if best[1] is not None else ''} ({time.time()-t0:.0f}s)")
    return hits, best

def logu(lo, hi, size=None):
    return np.sign(rng.uniform(-1, 1, size))*10**rng.uniform(lo, hi, size)
# S1: masses only, lam=1.05, eta=0.5
hits1, best1 = search("S1 masses only (lam=1.05, eta=0.5)", 3000,
                      lambda: (1.05, 0.5, -1.0) + tuple(logu(-3, 1, 5)) + z13)
# S2: masses + breaking two-derivative terms O(1e-3..1)
hits2, best2 = search("S2 masses + 13 breaking terms (lam=1.05, eta=0.5)", 3000,
                      lambda: (1.05, 0.5, -1.0) + tuple(logu(-3, 1, 5)) + tuple(logu(-3, 0, 13)))
# S3: lam in (1,2], eta in (0,2)
hits3, best3 = search("S3 as S2 with lam in (1,2], eta in (0,2)", 3000,
                      lambda: (1 + rng.uniform(0.001, 1), rng.uniform(0.01, 1.99), -1.0) + tuple(logu(-3, 1, 5)) + tuple(logu(-3, 0, 13)))
np.save('w3_c_hits.npy', np.array([h[0] for h in hits1 + hits2 + hits3], dtype=float) if hits1 + hits2 + hits3 else np.zeros((0, 21)))
for lab, hits in (("S1", hits1), ("S2", hits2), ("S3", hits3)):
    for pv, nm in hits[:5]:
        print(f"  {lab} hit: lam={pv[0]:.3f} eta={pv[1]:.3f} masses={np.round(pv[3:8], 4).tolist()} modes={sorted(nm)}")
        print(f"         breaking c = {np.round(pv[8:], 4).tolist()}")
