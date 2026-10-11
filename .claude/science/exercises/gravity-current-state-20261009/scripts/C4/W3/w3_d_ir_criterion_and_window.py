"""C4 / RW / W3 part D (uses the symbol pickled by part C2).
(1) IR criterion: with the shift made massive in the IR (the anomaly's -(a/2)(grad s)^2) and the lapse frozen
    or massive, the IR scalar's kinetic and gradient coefficients are the bare two-derivative ones:
      K0 = (3 - 9 lam)/2 + 12 c4 + 36 c5        (coefficient of Psi_dot^2; health needs K0 > 0)
      G0 = xi + 12 c0 + 36 c1 + 4 c2 + 12 c3    (coefficient of +(grad Psi)^2 in L; health needs G0 < 0)
    Check the sign pattern on every healthy hit of part C2.
(2) Static weak field of the hits at k >> mu (k = 100): source J*Phi (pressureless matter couples to h00);
    report G_eff/G_GR (= Phi k^2 relative to the GR value) and gamma = Psi/Phi; and c_T^2 = (1-8c0)/(1+8c4).
(3) Constrained search: c_T = 1 imposed exactly (c0 = -c4), lam - 1 in (0.001, 0.095), eta in (0,2):
    healthy hits and their static gamma."""
import sys, pickle; sys.path.insert(0, '.')
import sympy as sp, numpy as np
from w3_lib import w, k
M = pickle.load(open('w3_c2_symbol.pkl', 'rb'))
lam, eta, a = sp.symbols('lam eta a', real=True)
ms = sp.symbols('m0:5', real=True); cs = sp.symbols('c0:13', real=True)
pars = (lam, eta, a) + ms + cs
Mf = sp.lambdify((w, k, *pars), M, 'numpy'); dMf = sp.lambdify((w, k, *pars), sp.diff(M, w), 'numpy')
def roots_W(kv, pv):
    Ws = np.array([0.0, 1.0, -1.0])
    d = [np.linalg.det(np.array(Mf(np.sqrt(complex(W)), kv, *pv), dtype=complex)) for W in Ws]
    # det = A W^2 + B W + C
    C = d[0]; A = (d[1] + d[2])/2 - C; Bc = (d[1] - d[2])/2
    return np.roots([A, Bc, C]) if abs(A) > 1e-14*max(abs(Bc), abs(C), 1e-300) else (np.array([-C/Bc]) if abs(Bc) > 0 else np.array([]))
def classify(kv, pv):
    out = []
    for r in roots_W(kv, pv):
        if abs(r.imag) > 1e-7*max(1, abs(r)): out.append('COMPLEX'); continue
        r = r.real
        if r <= 0: out.append('TACHYON'); continue
        wv = np.sqrt(r); v = np.linalg.svd(np.array(Mf(wv, kv, *pv), dtype=complex))[2][-1].conj()
        Ek = wv*np.real(v.conj() @ np.array(dMf(wv, kv, *pv), dtype=complex) @ v)
        out.append('healthy' if Ek > 0 else 'GHOST')
    return out
ks = np.logspace(-4, 5, 28)
def healthy(pv):
    for kv in ks:
        if any(t != 'healthy' for t in classify(kv, pv)): return False
    return True
def K0G0(pv):
    lv = pv[0]; c = pv[8:]
    return (3 - 9*lv)/2 + 12*c[4] + 36*c[5], 1 + 12*c[0] + 36*c[1] + 4*c[2] + 12*c[3]
def static(pv, kv=100.0):
    Ms = np.array(Mf(0.0, kv, *pv), dtype=complex)
    J = np.array([1.0, 0, 0, 0], dtype=complex)
    v = np.linalg.solve(Ms, J)
    return v
gr = (1.0, 0.0, 0.0) + (0.0,)*5 + (0.0,)*13
# GR reference (a = 0, all extras 0): E is a gauge zero mode -> use B = E = 0 subsystem
Mgr = np.array(Mf(0.0, 100.0, *gr), dtype=complex)[np.ix_([0, 2], [0, 2])]   # static: s and E are gauge zero modes
v2 = np.linalg.solve(Mgr, np.array([1.0, 0], dtype=complex)); vgr = np.array([v2[0], 0, v2[1], 0])
print(f"GR reference static (k=100; s, E static gauge modes dropped): Phi k^2 = {vgr[0].real*1e4:+.4f}, gamma = Psi/Phi = {(vgr[2]/vgr[0]).real:+.4f}")
hits_by_p = pickle.load(open('w3_c2_hits.pkl', 'rb'))
hits = [h for p in hits_by_p for h in hits_by_p[p]]
print(f"(1)+(2) {len(hits)} healthy hits from C2:")
okpat = 0
for pv in hits:
    K0, G0 = K0G0(pv)
    v = static(pv)
    cT2 = (1 - 8*pv[8])/(1 + 8*pv[12])
    okpat += (K0 > 0 and G0 < 0)
    print(f"   lam={pv[0]:.4f} K0={K0:+.3f} G0={G0:+.3f}  c_T^2={cT2:.3f}  G_eff/G_GR={(v[0]/vgr[0]).real:+.3f}  gamma={(v[2]/v[0]).real:+.3f}")
print(f"   hits with K0 > 0 and G0 < 0: {okpat}/{len(hits)}")
rng = np.random.default_rng(11)
def logu(lo, hi, n): return np.sign(rng.uniform(-1, 1, n))*10**rng.uniform(lo, hi, n)
print("(3) constrained search with c_T = 1 exactly (c0 = -c4):")
nh = 0; rows = []
for i in range(4000):
    c = logu(-3, 0, 13); c[0] = -c[4]
    pv = (1 + rng.uniform(0.001, 0.095), rng.uniform(0.01, 1.99), -1.0) + tuple(logu(-3, 1, 5)) + tuple(c)
    K0, G0 = K0G0(pv)
    if not (K0 > 0 and G0 < 0): continue   # necessary (IR) condition from (1); skip the rest to save time
    if healthy(pv):
        nh += 1; v = static(pv); rows.append(((v[2]/v[0]).real, (v[0]/vgr[0]).real, pv))
print(f"   {nh} healthy hits with c_T = 1 out of 4000 draws")
for g, G, pv in sorted(rows, key=lambda r: abs(r[0] - 1))[:8]:
    print(f"   gamma={g:+.4f} G_eff/G_GR={G:+.4f} lam={pv[0]:.4f} eta={pv[1]:.3f} K0G0={tuple(round(q, 3) for q in K0G0(pv))} max|c|={np.max(np.abs(pv[8:])):.2f}")
