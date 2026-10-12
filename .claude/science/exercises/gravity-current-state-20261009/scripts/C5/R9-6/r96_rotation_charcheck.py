"""R9-6, script 3c: integrator floor of the characteristic check (B) for the BALL packets at theta = pi:
same packets, same field u = j(k) x n, RK4 with 160 vs 320 steps.  Expect ~16x reduction if the residual is RK4 error."""
import numpy as np
from r81_common import BoxLaw
m, B, B2 = 0.5, 2.6, 3.0
law = BoxLaw(m, B=B, B2=B2)
def jfun(k):
    h = 1e-6
    return law.s(k)*(law.s(k + h) - law.s(k - h))/(2*h)
def flow(k, theta, n, nst):
    h = theta/nst
    for _ in range(nst):
        u = lambda kk: np.cross(jfun(kk), n)
        a1 = u(k); a2 = u(k + 0.5*h*a1); a3 = u(k + 0.5*h*a2); a4 = u(k + h*a3)
        k = k + (h/6)*(a1 + 2*a2 + 2*a3 + a4)
    return k
def rot(k, theta, n):
    c, s = np.cos(theta), np.sin(theta)
    return k*c + np.cross(n, k)*s + np.outer(k @ n, n)*(1 - c)
NG, H = 40, 0.04
off = (np.arange(NG) - (NG - 1)/2)*H
G3 = np.stack(np.meshgrid(off, off, off, indexing='ij'), -1).reshape(-1, 3)
out = []
for nlab, n, c0 in [('z', np.array([0.0, 0.0, 1.0]), np.array([1.5, 0.8, 0.3])),
                    ('(1,2,2)/3', np.array([1.0, 2.0, 2.0])/3.0, np.array([1.2, -0.9, 0.7]))]:
    s0 = 0.08; K = c0[None, :] + G3
    psi = lambda k: np.exp(-((k - c0)**2).sum(-1)/(4*s0*s0))
    nrm = np.sqrt((psi(K)**2).sum()); th = np.pi
    Kt = rot(K, th, n); cont = psi(rot(Kt, -th, n))
    for nst in (160, 320):
        lat = psi(flow(Kt.copy(), th, n, nst))
        line = 'axis %s, ball packet, theta = pi, RK4 steps %d: on-grid leakage %.2e' % (nlab, nst, np.sqrt(((lat - cont)**2).sum())/nrm)
        print(line, flush=True); out.append(line)
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
