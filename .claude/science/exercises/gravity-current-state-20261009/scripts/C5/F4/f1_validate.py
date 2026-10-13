"""F1 validation: (i) t = 0 reproduces R19-34's root dm (+0.041858390) for Psym and every single ordering;
(ii) Ward identity of the constructed vertex at t != 0 (sum_j d_j V_j = D(q) - D(0)) and evenness of M_t;
(iii) explicit 4x4 gamma-matrix check of the reduced mass formula with a general (non-diagonal) vertex, Q0 integral by quadrature;
(iv) the free-band SF Hessians reproduce the archived shear rows (Dirac mu_E per field -1.709412e-2 at m = 0.01; photon +2.8508917e-2 per vector)."""
import numpy as np, time, sys
from f1_lib import *
t0 = time.time()
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
g = Grid([ROOT[0], np.pi - ROOT[0], CPH], 6, 0.25)
print('(i) t = 0: dm/e^2 (R19-34: +0.041858390 at n=8; +0.041858396 at n=6)')
print('   Psym: %+.9f' % dm_sf(F, G, g, 0.0))
for o in (('x','y','z'), ('z','x','y')):
    print('   order %s: %+.9f' % (''.join(o), dm_sf(F, G, g, 0.0, path=o)))
print('(ii) Ward identity / evenness at t = 0.3 on random points')
rng = np.random.default_rng(1)
t = 0.3
q = rng.uniform(0, np.pi, (3, 2000))
def Dat(kx, ky, kz):
    Wz = F.W(kz)
    fx, fy = flowF(F, np.atleast_1d(kx).astype(float), np.atleast_1d(ky).astype(float), Wz, t, 6)
    return np.array([F.s(fx), F.s(fy), F.s(kz) + 0*fx, F.W(fx) + F.W(fy) + Wz])
qx, qy, qz = q; Z = 0*qx
Dq = Dat(qx, qy, qz); D0 = Dat(Z, Z, Z)
corners = {'0': D0, 'x': Dat(qx, Z, Z), 'y': Dat(Z, qy, Z), 'z': Dat(Z, Z, qz), 'xy': Dat(qx, qy, Z), 'xz': Dat(qx, Z, qz), 'yz': Dat(Z, qy, qz), 'q': Dq}
dx = G.d(flowG1(G, qx, +1, t)); dy = G.d(flowG1(G, qy, -1, t)); dz = G.d(qz)
Vx = (2*(corners['x'] - corners['0']) + (corners['xy'] - corners['y']) + (corners['xz'] - corners['z']) + 2*(corners['q'] - corners['yz']))/6/dx
Vy = (2*(corners['y'] - corners['0']) + (corners['xy'] - corners['x']) + (corners['yz'] - corners['z']) + 2*(corners['q'] - corners['xz']))/6/dy
Vz = (2*(corners['z'] - corners['0']) + (corners['xz'] - corners['x']) + (corners['yz'] - corners['y']) + 2*(corners['q'] - corners['xy']))/6/dz
print('   max |sum_j d_j V_j - (D(q) - D(0))| = %.2e  (scale %.2e)' % (np.abs(dx*Vx + dy*Vy + dz*Vz - (Dq - D0)).max(), np.abs(Dq).max()))
Dm = np.array([-a for a in Dat(-qx, -qy, -qz)[:3]] + [Dat(-qx, -qy, -qz)[3]])
print('   oddness of c and evenness of M under q -> -q: max dev %.2e' % np.abs(Dm - Dq).max())
print('   off-diagonal vertex size: max |a_xy| = %.3e, max |a_xx - s-separable| shows non-separability' % np.abs(Vx[1]).max())
print('(iii) explicit gamma-matrix check of the reduced formula (general vertex), 5 random points')
s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
g0 = np.kron(s1, s0); gs = [np.kron(s2, s1), np.kron(s2, s2), np.kron(s2, s3)]   # Euclidean hermitian, anticommuting
I4 = np.eye(4)
from scipy.integrate import quad
for i in range(5):
    cq = Dq[:3, i]; M = Dq[3, i]; Om = np.sqrt(dx[i]**2 + dy[i]**2 + dz[i]**2)
    V = []
    for Vj, dj in ((Vx, dx), (Vy, dy), (Vz, dz)):
        V.append(1j*sum(gs[l]*Vj[l, i] for l in range(3)) + Vj[3, i]*I4)
    def integrand(Q0):
        Sinv = 1j*g0*Q0 + 1j*sum(gs[l]*cq[l] for l in range(3)) + M*I4
        S = np.linalg.inv(Sinv)
        tot = -(-1j*g0) @ S @ (-1j*g0)
        for j in range(3):
            tot = tot - V[j] @ S @ V[j]
        return np.real(np.trace(tot))/4/(Q0**2 + Om**2)/(2*np.pi)
    num = 2*quad(integrand, 0, np.inf, limit=200, epsabs=1e-14, epsrel=1e-12)[0]
    E = np.sqrt(cq @ cq + M*M)
    red = M
    for Vj, dj in ((Vx, dx), (Vy, dy), (Vz, dz)):
        a = Vj[:3, i]; b = Vj[3, i]   # Vj already divided by d_j
        red += (a @ a - b*b)*M - 2*b*(a @ cq)
    red /= (2*E*Om*(E + Om))
    print('   point %d: gamma-matrix %+.12e  reduced %+.12e  diff %.1e' % (i, num, red, num - red))
print('(iv) free-band SF Hessians by integrating the flow (Lemma H), against the archived shear rows')
gF = Grid([ROOT[0], np.pi - ROOT[0], CPH], 8, 0.15)
xx, ww = gF.x, gF.w
def eD(tt):
    tot = 0.0
    for iz in range(len(xx)):
        Wz = F.W(xx[iz])
        fx, fy = flowF(F, xx[:, None], xx[None, :], Wz, tt, 6)
        E = np.sqrt(F.s(fx)**2 + F.s(fy)**2 + F.s(xx[iz])**2 + (0.01 + F.W(fx) + F.W(fy) + Wz)**2)
        tot += ww[iz]*float((ww[:, None]*ww[None, :]*E).sum())
    return -2.0*tot              # 4-comp Dirac sea: -(Nc/2) E per mode
r = hess(eD, 0.02)
print('   Dirac D1 root, m = 0.01: e\'\'(0) = %+.7e (d) %+.7e (Rich)   archived mu_E = -1.709412e-2 (dfam / rR19-35 3.1)' % (r['h1'], r['rich']))
def eG(tt):
    fx = flowG1(G, xx, +1, tt); fy = flowG1(G, xx, -1, tt)
    dX, dY, dZ = G.d(fx), G.d(fy), G.d(xx)
    om = np.sqrt(dX[:, None, None]**2 + dY[None, :, None]**2 + dZ[None, None, :]**2 + 1e-6)
    return float((ww[:, None, None]*ww[None, :, None]*ww[None, None, :]*om).sum())   # vector: 2 pols x omega/2
r = hess(eG, 0.02)
print('   photon Gph(2.9435), reg 1e-3: e\'\'(0) = %+.7e (d) %+.7e (Rich)   archived +2.8508917e-2 (rR19-35 3.1)' % (r['h1'], r['rich']))
print('time %.0f s' % (time.time() - t0))
