"""C4 / RW / W3 part B: khronometric (BPS / non-projectable Horava IR) kinetic structure + the anomaly.
Unitary gauge (pi = zeta = 0), fields Phi, s, Psi, E with B = s + E_dot (s = sigma = B - E_dot, the
spatial-diffeo-invariant shift combination), M_P^2 = 1:
  L_KH = 1/2[K_ij K_ij - lam K^2] + xi[(grad Psi)^2 - 2 grad Phi.grad Psi] + (eta/2)(grad Phi)^2
         - g4 (lap Psi)^2                    [g4: FDiff-invariant 4-derivative (R^2-type) potential term]
  K_ij = -Psi_dot delta_ij - d_i d_j s
  F    = a[-grad Phi.grad E - 1/2 (grad s)^2]                       (anomaly, part A)
  X_m4 = c4 * Phi * h_ii = c4 * Phi * (-6 Psi + 2 lap E)              (local lapse-trace mass term)
Checks: (0) lam = xi = 1, eta = g4 = 0 reproduces W2's L_GR; (1) a = 0 reproduces the GSS khronon speed;
(2) a != 0, c4 = 0: E multiplies only Phi => Phi = 0 on shell (projectable lapse), BPS eta is inert,
    scalar ghost or tachyon at every k for every lam (analytic K_Psi, potential);
(3) c4 = -a/2: E drops out exactly; one scalar; healthy at all k iff lam < 1/3 (and 0 < eta < 2 xi);
    for lam > 1: ghost below k*^2 = |a|/(lam - 1), healthy above;  (4) c4 = -a/2 + delta: Phi frozen again;
(5) g4 > 0 fixes only the UV."""
import sys; sys.path.insert(0, '.')
import sympy as sp, numpy as np
from w3_lib import *

lam, xi, eta, a, c4, g4 = sp.symbols('lam xi eta a c4 g4', real=True)
Phi, s, Psi, E = [F(n) for n in ('Phi', 's', 'Psi', 'E')]
Kij = [[-dt(Psi)*(1 if i == j else 0) - sp.diff(s, X[i], X[j]) for j in range(3)] for i in range(3)]
Ktr = sum(Kij[i][i] for i in range(3))
KK = sum(Kij[i][j]**2 for i in range(3) for j in range(3))
L_KH = sp.Rational(1, 2)*(KK - lam*Ktr**2) + xi*(dot(grad(Psi), grad(Psi)) - 2*dot(grad(Phi), grad(Psi))) \
       + eta/2*dot(grad(Phi), grad(Phi)) - g4*lap(Psi)**2
Fa = a*(-dot(grad(Phi), grad(E)) - sp.Rational(1, 2)*dot(grad(s), grad(s)))
Xm4 = c4*Phi*(-6*Psi + 2*lap(E))

# (0) normalisation vs W2
B = F('B'); sig = B - dt(E)
L_GR = (-3*dt(Psi)**2 + dot(grad(Psi), grad(Psi)) - 2*dot(grad(Phi), grad(Psi)) - 2*dt(Psi)*lap(sig))
Ltest = L_KH.subs({lam: 1, xi: 1, eta: 0, g4: 0}).subs(s, sig)
ok, f, el = euler_zero(sp.expand((Ltest - L_GR).doit()), None)
print("(0) L_KH(lam=1, xi=1, eta=0) - L_GR(W2) is a total derivative:", ok)

fields4 = [Phi, s, Psi, E]
M4 = fourier_matrix(L_KH + Fa + Xm4, fields4)
print("    Fourier form (Phi, s, Psi, E):"); sp.pprint(M4)
pars = (lam, xi, eta, a, c4, g4)

# (1) a = 0: khronometric, fields Phi, s, Psi
M3 = fourier_matrix(L_KH, [Phi, s, Psi])
det3 = sp.factor(sp.simplify(M3.det()))
Wsym = sp.symbols('W')
root = sp.solve(sp.Eq(det3.subs(w, sp.sqrt(Wsym)), 0), Wsym)
print("\n(1) a = 0 det:", det3)
print("    khronon w^2 =", [sp.factor(r.subs(g4, 0)) for r in root])
gam, al = sp.symbols('gamma alpha')
cS2 = sp.factor([r for r in root if r != 0][0].subs({g4: 0, xi: 1, eta: al, lam: 1 + gam})/k**2)
gss = (2 - al)*gam/(al*(2 + 3*gam))
print("    c_S^2 (xi=1, eta=alpha, lam=1+gamma) =", cS2, "; GSS(beta=0) =", sp.factor(gss), "; equal:", sp.simplify(cS2 - gss) == 0)

# (2) a != 0, c4 = 0: analytic reduction
print("\n(2) anomaly, c4 = 0:")
det4 = sp.factor(sp.simplify(M4.subs({c4: 0}).det()))
print("    det M =", det4)
r4 = sp.solve(sp.Eq(det4.subs(w, sp.sqrt(Wsym)), 0), Wsym)
print("    w^2 roots:", [sp.factor(r) for r in r4], " (eta-independent:", all(not r.has(eta) for r in r4), ")")
# analytic K_Psi with Phi = 0: integrate out s
KPsi = sp.Rational(3, 1)*(1 - 3*lam)/2 - (1 - 3*lam)**2*k**2/(2*((1 - lam)*k**2 - a))
print("    K_Psi(k) = (3-9lam)/2 - (1-3lam)^2 k^2 / (2[(1-lam)k^2 - a]);  potential term in L: + (xi k^2 + g4 k^4)|Psi|^2")
print("    -> w^2 = -(xi k^2 - g4 k^4)/K_Psi ... check vs root:",
      sp.simplify(r4[0] - (-(xi*k**2 - g4*k**4)/KPsi)) == 0 if len(r4) == 1 else r4)
cf, Mf, dMf, poly = spectrum_tools(M4, pars)
ks = np.logspace(-3, 3, 25)
def scan(pv, label, ks=ks):
    tags = []
    for kv in ks:
        tags.append(classify(cf, Mf, dMf, kv, pv))
    summ = {}
    for kv, tg in zip(ks, tags):
        key = ','.join(sorted(t for t, _ in tg)) or 'none'
        summ.setdefault(key, []).append(kv)
    txt = '; '.join(f"{kk}: k in [{min(v):.2g},{max(v):.2g}] ({len(v)} pts)" for kk, v in summ.items())
    print(f"    {label}: {txt}")
for av in (-1.0, +1.0):
    for lv in (-1.0, 0.0, 0.2, 0.5, 0.9, 1.0, 1.01, 1.1, 2.0):
        for ev in (1e-3, 1.0):
            scan((lv, 1.0, ev, av, 0.0, 0.0), f"a={av:+g} lam={lv:5.2f} eta={ev:g} c4=0")
# null vector Phi component on the mode (Phi = 0 forced)
pv = (1.05, 1.0, 1.0, -1.0, 0.0, 0.0)
for kv in (0.1, 1.0, 10.0):
    for tg, r in classify(cf, Mf, dMf, kv, pv):
        Mv = np.array(Mf(np.sqrt(abs(r)) if r > 0 else 1j*np.sqrt(-r), kv, *pv), dtype=complex)
        v = np.linalg.svd(Mv)[2][-1].conj()
        print(f"    lam=1.05 a=-1 k={kv}: mode {tg} w^2={r:+.4g}; |Phi|/|v| = {abs(v[0])/np.linalg.norm(v):.1e}")

# (3) c4 = -a/2: E decouples
print("\n(3) c4 = -a/2 (local lapse-trace term tuned against the anomaly):")
M4t = sp.simplify(M4.subs(c4, -a/2))
print("    E row/column of the Fourier form vanish identically (E only in a total derivative -a div(Phi grad E)):",
      all(sp.simplify(M4t[3, j]) == 0 and sp.simplify(M4t[j, 3]) == 0 for j in range(4)))
M3a = M4t[:3, :3]
det3a = sp.factor(sp.simplify(M3a.det()))
print("    det M (Phi, s, Psi) =", det3a)
pars3 = (lam, xi, eta, a, g4)
cf3, Mf3, dMf3, _ = spectrum_tools(M3a, pars3)
def scan3(pv, label, ks=ks):
    summ = {}
    for kv in ks:
        tg = classify(cf3, Mf3, dMf3, kv, pv)
        key = ','.join(sorted(t for t, _ in tg)) or 'none'
        summ.setdefault(key, []).append(kv)
    print(f"    {label}: " + '; '.join(f"{kk}: k in [{min(v):.2g},{max(v):.2g}] ({len(v)})" for kk, v in summ.items()))
for av in (-1.0, +1.0):
    for lv in (-1.0, 0.0, 0.2, 0.5, 0.9, 1.01, 1.1, 2.0):
        for ev in (1e-3, 1.0, 2.5):
            kst = np.sqrt(abs(av)/(lv - 1)) if (lv > 1 and av < 0) else float('nan')
            scan3((lv, 1.0, ev, av, 0.0), f"a={av:+g} lam={lv:5.2f} eta={ev:g} [k*={kst:.3g}]")
# (4) mistuning delta
print("\n(4) c4 = -a/2 + delta (a=-1, lam=1.05, eta=1):")
for dl in (1e-6, 1e-3, 1e-1):
    scan((1.05, 1.0, 1.0, -1.0, 0.5 + dl, 0.0), f"delta={dl:g}")
# (5) FDiff-invariant 4-derivative potential term g4 (c4 = 0)
print("\n(5) g4 (lap Psi)^2 added, c4 = 0, a = -1:")
for lv in (0.2, 1.05):
    scan((lv, 1.0, 1.0, -1.0, 0.0, 1.0), f"lam={lv} g4=1")
print("\n(5b) g4 added with c4 = -a/2, a = -1, lam = 1.05, eta = 1:")
scan3((1.05, 1.0, 1.0, -1.0, 1.0), "g4=1")
