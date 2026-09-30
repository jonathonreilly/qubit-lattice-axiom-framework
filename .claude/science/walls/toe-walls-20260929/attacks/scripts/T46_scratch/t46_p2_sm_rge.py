"""T46 P2: does a framework-named UV scale rescue the 5/6 exponent?
3-generation one-loop SM Yukawa RGE (Machacek-Vaughn, convention L = -Qbar Y_d d H - Qbar Y_u u Htilde),
one-loop gauge running (optionally 2-loop gauge), start at mu = m_t with QCD-run masses.

p(mu) := ln|V_cb(mu)| / ln[ m_s(mu)/m_b(mu) ]   (the exponent the bridge would need at scale mu)
Assumes an SM desert up to the chosen scale (flagged hidden premise).
"""
import sys
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from qcdrun import QCD

VH = 246.22
MPL = 1.220890e19
MT0 = 163.0

def ckm(s12=0.22501, s23=0.0422, s13=0.00369, d=1.144):
    c12, c23, c13 = [np.sqrt(1 - x*x) for x in (s12, s23, s13)]
    e = np.exp(1j*d)
    return np.array([
        [c12*c13, s12*c13, s13/e],
        [-s12*c23 - c12*s23*s13*e, c12*c23 - s12*s23*s13*e, s23*c13],
        [s12*s23 - c12*c23*s13*e, -c12*s23 - s12*c23*s13*e, c23*c13]])

def pack(Yu, Yd, g):
    return np.concatenate([Yu.real.ravel(), Yu.imag.ravel(), Yd.real.ravel(), Yd.imag.ravel(), g])

def unpack(y):
    Yu = (y[0:9] + 1j*y[9:18]).reshape(3, 3)
    Yd = (y[18:27] + 1j*y[27:36]).reshape(3, 3)
    return Yu, Yd, y[36:39]

B1 = np.array([41/10, -19/6, -7.0])
B2 = np.array([[199/50, 27/10, 44/5], [9/10, 35/6, 12], [11/10, 9/2, -26]])
CT = np.array([[17/10, 1/2, 3/2], [3/2, 3/2, 1/2], [2.0, 2.0, 0.0]])  # (t,b,tau)

def rhs(t, y, ytau, loop2, kyuk):
    Yu, Yd, g = unpack(y)
    g1, g2, g3 = g
    k = 1/(16*np.pi**2)
    T = np.trace(3*Yu@Yu.conj().T + 3*Yd@Yd.conj().T).real + ytau**2
    Gu = 17/20*g1**2 + 9/4*g2**2 + 8*g3**2
    Gd = 1/4*g1**2 + 9/4*g2**2 + 8*g3**2
    YuYu = Yu@Yu.conj().T; YdYd = Yd@Yd.conj().T
    dYu = k*((1.5*kyuk*(YuYu - YdYd))@Yu + (T - Gu)*Yu)
    dYd = k*((1.5*kyuk*(YdYd - YuYu))@Yd + (T - Gd)*Yd)
    dg = k*B1*g**3
    if loop2:
        yt2 = np.sort(np.linalg.eigvalsh(YuYu))[-1]; yb2 = np.sort(np.linalg.eigvalsh(YdYd))[-1]
        y2 = np.array([yt2, yb2, ytau**2])
        dg = dg + k**2*g**3*(B2@(g**2) - CT@y2)
    return np.concatenate([dYu.real.ravel(), dYu.imag.ravel(), dYd.real.ravel(), dYd.imag.ravel(), dg])

def observables(Yu, Yd):
    Uu, su, _ = np.linalg.svd(Yu); Ud, sd, _ = np.linalg.svd(Yd)
    ou = np.argsort(su); od = np.argsort(sd)
    Uu, su = Uu[:, ou], su[ou]; Ud, sd = Ud[:, od], sd[od]
    V = Uu.conj().T@Ud
    return su, sd, np.abs(V)

def setup(yt0=0.9369, asMZ=0.1180, Vcb0=0.0422, MS2=0.0934, MB=4.18, g1=0.4629, g2=0.6478,
          mt=MT0, ytau=0.0102, kyuk=1.0):
    q = QCD(asMZ=asMZ, mb=MB, mt=mt)
    a3 = q.alpha_s(mt)
    g3 = np.sqrt(4*np.pi*a3)
    m = {'d': q.mass(0.00467, 2.0, mt), 's': q.mass(MS2, 2.0, mt), 'b': q.mass(MB, MB, mt),
         'u': q.mass(0.00216, 2.0, mt), 'c': q.mass(1.27, 1.27, mt)}
    yd = np.sqrt(2)*np.array([m['d'], m['s'], m['b']])/VH
    yu = np.array([np.sqrt(2)*m['u']/VH, np.sqrt(2)*m['c']/VH, yt0])
    V = ckm(s23=Vcb0)
    Yu = np.diag(yu).astype(complex)
    Yd = V@np.diag(yd)   # basis with Yu diagonal
    return pack(Yu, Yd, np.array([g1, g2, g3])), q, m

def evolve(y0, tlist, loop2=False, kyuk=1.0, ytau=0.0102):
    s = solve_ivp(rhs, [tlist[0], tlist[-1]], y0, t_eval=tlist, args=(ytau, loop2, kyuk),
                  rtol=1e-10, atol=1e-13, method='DOP853')
    out = []
    for i in range(len(s.t)):
        Yu, Yd, g = unpack(s.y[:, i])
        su, sd, V = observables(Yu, Yd)
        out.append((np.exp(s.t[i]), su[2], sd[1]/sd[2], V[1, 2], g.copy(), sd, su))
    return out

def curve(**kw):
    loop2 = kw.pop('loop2', False); kyuk = kw.pop('kyuk', 1.0)
    y0, q, m = setup(**kw, kyuk=kyuk)
    t = np.linspace(np.log(MT0), np.log(MPL), 400)
    res = evolve(y0, t, loop2=loop2, kyuk=kyuk)
    mu = np.array([r[0] for r in res]); yt = np.array([r[1] for r in res])
    R = np.array([r[2] for r in res]); V = np.array([r[3] for r in res])
    p = np.log(V)/np.log(R)
    return mu, yt, R, V, p

if __name__ == "__main__":
    mu, yt, R, V, p = curve()
    print("one-loop gauge + one-loop Yukawa, SM desert")
    print(f"start mu={mu[0]:.1f}: y_t={yt[0]:.4f} R=m_s/m_b={R[0]:.6f} V_cb={V[0]:.5f} p={p[0]:.4f}")
    for mu_t in (246.22, 1e3, 1e4, 1e6, 1e8, 1e10, 1e12, 1e14, 2e16, MPL):
        i = np.argmin(np.abs(np.log(mu/mu_t)))
        print(f" mu={mu[i]:10.3e}  y_t={yt[i]:.4f}  R={R[i]:.6f}  V_cb={V[i]:.5f}  p={p[i]:.4f}   R/R0={R[i]/R[0]:.4f}  V/V0={V[i]/V[0]:.4f}")
    # crossing
    f = lambda i: p[i] - 5/6
    idx = np.where(np.diff(np.sign(p - 5/6)))[0]
    if len(idx):
        i = idx[0]
        lm = np.interp(5/6, [p[i], p[i+1]], [np.log10(mu[i]), np.log10(mu[i+1])])
        print(f" p = 5/6 at mu* ~ 10^{lm:.2f} GeV")
    else:
        print(" p never reaches 5/6 up to M_Pl; p(M_Pl) =", p[-1])
