"""NF-1 (a)/(b) extension: other uniform strain channels (T2g, A1 trace) on the staggered law, direct 8x8 (nf1_sigma8.py's evaluator).
Generic SF flow of the staggered band: dk/dtau = (t/2) h.p(k), p_j = s(k_j) s'(k_j) (odd, pi-periodic in every k_l), non-separable for T2g.
Photon UNSTRAINED here (F1's 'photon unstrained' branch): the registered frame photon is singular for T2g (G-F5a, TESTS:9391), and the
protection argument does not use the photon's strain law.  Control: the eps-Wilson term r_c = 0.3 under the same flows.
argv: N"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else '24']
src = open(os.path.join(HERE, 'nf1_sigma8.py')).read()
exec(src.split("x = -np.pi + (np.arange(N)")[0])
x = -np.pi + (np.arange(N) + 0.5)*2*np.pi/N
def cM_gen(F, t, h):
    h = np.asarray(h, float)
    def cM(kx, ky, kz):
        kx, ky, kz = np.broadcast_arrays(np.asarray(kx, float), np.asarray(ky, float), np.asarray(kz, float))
        y = np.stack([kx, ky, kz])
        if t != 0.0:
            def f(y):
                M = F.mflow + F.W(y[0]) + F.W(y[1]) + F.W(y[2])
                p = np.stack([F.s(y[j])*F.ds(y[j]) + M*F.dW(y[j]) for j in range(3)])
                return 0.5*t*np.tensordot(h, p, axes=1)
            nst = 6; dt = 1.0/nst
            for _ in range(nst):
                k1 = f(y); k2 = f(y + 0.5*dt*k1); k3 = f(y + 0.5*dt*k2); k4 = f(y + dt*k3)
                y = y + dt/6*(k1 + 2*k2 + 2*k3 + k4)
        c = [F.s(y[j]) for j in range(3)]; M = F.W(y[0]) + F.W(y[1]) + F.W(y[2])
        return c[0], c[1], c[2], M
    return cM
d0 = G.d(x)
H_T2G = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]; H_A1 = np.eye(3); H_EG = np.diag([1., -1., 0.])
print('NF-1 other strain channels, direct 8x8, full-BZ midpoint N = %d, photon unstrained; per e^2' % N)
for lab, h in (('T2g', H_T2G), ('A1', H_A1), ('Eg', H_EG)):
    for rc in (0.0, 0.3):
        out = {}
        for t in (0.0, 0.1, 0.2):
            S = sigma8(cM_gen(FermC(rc), t, h), d0, d0, d0, x)
            out[t] = report('%s rc=%.1f t=%+.2f' % (lab, rc, t), S, float('nan'))
        print('   %s rc=%.1f: coarse 2[f(d)-f(0)]/d^2 (d=0.1) %+.4e (d=0.2) %+.4e' % (lab, rc, 2*(out[0.1]-out[0.0])/0.01, 2*(out[0.2]-out[0.0])/0.04), flush=True)
