"""F5 (c): knock-on of the rule onto the vacuum's degree-0 entries.
(1) one-loop additive mass along the rank-one strain h = e_z e_z (R19-35's 'nn', which carries trace) and the isotropic h = 1:
    dm(t) at t = 0, +-d, +-2d (not even: first and second derivatives by central differences, Richardson);
(2) the free Dirac vacuum per field e(t; m) = -2 <E_m o Phi_t^(m)> (R19-35 H4 / Lemma H units; weight w = -Nc/2 = -2):
    e_m = de/dm at t = 0 (= -2 <M/E>), e_tm along nn, and the shear-row check e_tt along E_g against the registered -1.709412e-2.
Octant quadrature (diagonal h: integrand even in each q_j); GL panels as F1.  argv: n hmax mph d"""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
t00 = time.time()
n, hm, mph, d = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
br = mkbreaks(ROOT[0], CPH, mph)
xo = panels(br, n, hm)
print('grid n=%d hmax=%.2f mph=%d (%d nodes), d=%.4f; R18-9 root B1 Psym; per e^2, SF units' % (n, hm, mph, len(xo[0]), d), flush=True)
def derivs(h):
    f = {s: dm_gen(F, G, h, xo, xo, xo, s*d) for s in (0, 1, -1, 2, -2)}
    g1 = (f[1] - f[-1])/(2*d); g2 = (f[2] - f[-2])/(4*d)
    h1 = (f[1] - 2*f[0] + f[-1])/d**2; h2 = (f[2] - 2*f[0] + f[-2])/(4*d*d)
    return f[0], (4*g1 - g2)/3, (4*h1 - h2)/3
for lab, h in (('nn = e_z e_z', H_NN), ('iso = 1', H_ISO), ('E_g (check vs F1)', H_EG)):
    f0, g, hh = derivs(h)
    print('  %-18s dm0 %+.10f  d_t dm %+.7e  d2_t dm %+.7e   [%.0f s]' % (lab, f0, g, hh, time.time() - t00), flush=True)
# free Dirac vacuum (per field), 3D GL octant grid; flows depend on m through M
x, w = xo
X, Y, Z = x[:, None, None], x[None, :, None], x[None, None, :]
WW = w[:, None, None]*w[None, :, None]*w[None, None, :]
def evac(t, m, h, nrk=4):
    Fm = Ferm(*ROOT, mflow=m)
    tot = 0.0
    for i0 in range(0, len(x), 8):
        sl = slice(i0, i0 + 8)
        a, b, c = flow3(Fm, h, X, Y, Z[:, :, sl], t, nrk)
        M = m + Fm.W(a) + Fm.W(b) + Fm.W(c)
        E = np.sqrt(Fm.s(a)**2 + Fm.s(b)**2 + Fm.s(c)**2 + M*M)
        tot += float((WW[:, :, sl]*E).sum())
    return -2*tot
m0, dmm, dt = 0.01, 1e-4, 0.01
em = (evac(0.0, m0 + dmm, H_NN) - evac(0.0, m0 - dmm, H_NN))/(2*dmm)
# <M/E> directly
Mv = m0 + F.W(X) + F.W(Y) + F.W(Z); Ev = np.sqrt(F.s(X)**2 + F.s(Y)**2 + F.s(Z)**2 + Mv*Mv)
print('  e_m = de/dm (FD) %+.8f ;  -2<M/E> %+.8f   (per Dirac field, m = 0.01)' % (em, -2*float((WW*Mv/Ev).sum())), flush=True)
def etm(h):
    e = lambda t, m: evac(t, m, h)
    return ((e(dt, m0 + dmm) - e(dt, m0 - dmm)) - (e(-dt, m0 + dmm) - e(-dt, m0 - dmm)))/(4*dt*dmm)
print('  e_tm along nn %+.6e ; along iso %+.6e' % (etm(H_NN), etm(H_ISO)), flush=True)
def ett(h, m=m0):
    e = lambda t: evac(t, m, h)
    e0 = e(0.0); h1 = (e(dt) - 2*e0 + e(-dt))/dt**2; h2 = (e(2*dt) - 2*e0 + e(-2*dt))/(4*dt*dt)
    return (4*h1 - h2)/3
print('  row check: e_tt along E_g %+.7e (registered mu_E per Dirac field -1.709412e-2); along nn %+.7e (R19-35 Hess(nn) +2.164325e-2)'
      % (ett(H_EG), ett(H_NN)), flush=True)
print('  e_t along nn (one-point, per unit h_zz) %+.6e' % ((evac(dt, m0, H_NN) - evac(-dt, m0, H_NN))/(2*dt)), flush=True)
print('time %.0f s' % (time.time() - t00))
