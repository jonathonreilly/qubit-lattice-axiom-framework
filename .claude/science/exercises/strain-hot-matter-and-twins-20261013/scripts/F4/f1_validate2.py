"""F1 validation part 2: (iii) gamma-matrix check (fixed double division in f1_validate.py); (iv') photon SF Hessian with small steps
(the photon flow is strongly nonlinear in its 0.198-wide edge: Lipschitz ~ 15, so d = 0.02 is outside the asymptotic regime)."""
import numpy as np, time
from f1_lib import *
from scipy.integrate import quad
t0 = time.time()
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
rng = np.random.default_rng(1); t = 0.3
q = rng.uniform(0, np.pi, (3, 5)); qx, qy, qz = q; Z = 0*qx
def Dat(kx, ky, kz):
    Wz = F.W(kz)
    fx, fy = flowF(F, np.atleast_1d(kx).astype(float), np.atleast_1d(ky).astype(float), Wz, t, 6)
    return np.array([F.s(fx), F.s(fy), F.s(kz) + 0*fx, F.W(fx) + F.W(fy) + Wz])
C = {'0': Dat(Z, Z, Z), 'x': Dat(qx, Z, Z), 'y': Dat(Z, qy, Z), 'z': Dat(Z, Z, qz), 'xy': Dat(qx, qy, Z), 'xz': Dat(qx, Z, qz), 'yz': Dat(Z, qy, qz), 'q': Dat(qx, qy, qz)}
dx = G.d(flowG1(G, qx, +1, t)); dy = G.d(flowG1(G, qy, -1, t)); dz = G.d(qz)
Vx = (2*(C['x'] - C['0']) + (C['xy'] - C['y']) + (C['xz'] - C['z']) + 2*(C['q'] - C['yz']))/6/dx
Vy = (2*(C['y'] - C['0']) + (C['xy'] - C['x']) + (C['yz'] - C['z']) + 2*(C['q'] - C['xz']))/6/dy
Vz = (2*(C['z'] - C['0']) + (C['xz'] - C['x']) + (C['yz'] - C['y']) + 2*(C['q'] - C['xy']))/6/dz
s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
g0 = np.kron(s1, s0); gs = [np.kron(s2, s1), np.kron(s2, s2), np.kron(s2, s3)]; I4 = np.eye(4)
print('(iii) explicit 4x4 Euclidean gamma matrices, Q0 by quadrature, vs the reduced mass formula (t = 0.3, Psym vertex)')
for i in range(5):
    cq = C['q'][:3, i]; M = C['q'][3, i]; Om = np.sqrt(dx[i]**2 + dy[i]**2 + dz[i]**2)
    V = [1j*sum(gs[l]*Vj[l, i] for l in range(3)) + Vj[3, i]*I4 for Vj in (Vx, Vy, Vz)]
    def integrand(Q0):
        S = np.linalg.inv(1j*g0*Q0 + 1j*sum(gs[l]*cq[l] for l in range(3)) + M*I4)
        tot = -(-1j*g0) @ S @ (-1j*g0)
        for j in range(3): tot = tot - V[j] @ S @ V[j]
        return np.real(np.trace(tot))/4/(Q0**2 + Om**2)/(2*np.pi)
    num = 2*quad(integrand, 0, np.inf, limit=400, epsabs=1e-15, epsrel=1e-13)[0]
    E = np.sqrt(cq @ cq + M*M); red = M
    for Vj in (Vx, Vy, Vz):
        a = Vj[:3, i]; b = Vj[3, i]; red += (a @ a - b*b)*M - 2*b*(a @ cq)
    red /= (2*E*Om*(E + Om))
    print('   point %d: gamma-matrix %+.12e  reduced %+.12e  diff %.1e   |a_off| = %.2e' % (i, num, red, num - red, abs(Vx[1, i]) + abs(Vy[0, i])))
print("(iv') photon Gph(2.9435), reg 1e-3, per vector: e''(0) of <omega o Phi^g_t>  (archived +2.8508917e-2, Laplace 1D-moment form)")
for n, hm in ((8, 0.15), (8, 0.08), (10, 0.05)):
    gF = Grid([CPH], n, hm); xx, ww = gF.x, gF.w
    def eG(tt):
        fx = flowG1(G, xx, +1, tt, 8); fy = flowG1(G, xx, -1, tt, 8)
        dX, dY, dZ = G.d(fx), G.d(fy), G.d(xx)
        om = np.sqrt(dX[:, None, None]**2 + dY[None, :, None]**2 + dZ[None, None, :]**2 + 1e-6)
        return float((ww[:, None, None]*ww[None, :, None]*ww[None, None, :]*om).sum())
    for d in (0.004, 0.001):
        r = hess(eG, d)
        print('   n=%d hmax=%.2f (%d nodes) d=%.3f: (d) %+.9e  (2d) %+.9e  Rich %+.9e' % (n, hm, len(xx), d, r['h1'], r['h2'], r['rich']), flush=True)
print('time %.0f s' % (time.time() - t0))
