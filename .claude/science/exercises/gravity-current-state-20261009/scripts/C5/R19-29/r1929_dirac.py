"""R19-29: the same A_1 face-block checks for one Wilson-Dirac field on D1(b_f, r) with R18-5's UD vertex at the pair
midpoint (P-R18-5c, as in R18-13's dface.py), time components by P1 (R19-5), ultralocal seagull.
Pair legs k +- q/2; Gram form of the two-band pair weight (R16-13 dirac.py docstring, generalized to A != B):
   Gamma_AB = (Nc/4) [ A.B (1 + u.v) - (u.A)(v.B) - (u.B)(v.A) ],  u = c(k+q/2)/E+, v = c(k-q/2)/E-,
   Pi_AB(omega) = - < Gamma(A_a, B_a)/(E - omega) + Gamma(A_b, B_b)/(E + omega) >,  E = E+ + E-.
A_a, A_b = G-vectors of the effective spatial tensors e_sp +- sym(q x w)/E + e_00 q x q / E^2  (w_j = e_0j + e_j0).
UD: G_a = (e.p)_a S'_a (a = x, y, z), G_beta = W'.e.p, p_i = S_i S'_i + M W'_i, M = m + sum W, all at the midpoint k.
usage: python r1929_dirac.py bf r m N"""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18'))
from content3 import D1q
from a1lib import emb, E1F, n3, a3, b3, gauge
t0 = time.time()
bf, r, m, N = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
law = D1q(bf, r); Nc = 4
x = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
K = [k.ravel() for k in np.meshgrid(x, x, x, indexing='ij')]; Wt = 1.0/N**3
S0 = [law.S(k) for k in K]; Sp0 = [law.dS(k) for k in K]; W0 = [law.W(k) for k in K]; Wp0 = [law.dW(k) for k in K]
M0 = m + sum(W0); p0 = [S0[i]*Sp0[i] + M0*Wp0[i] for i in range(3)]
def cvec(Ks):
    S = [law.S(k) for k in Ks]; M = m + sum(law.W(k) for k in Ks)
    return S + [M]
def G(e3):
    e3 = 0.5*(e3 + e3.T) if np.ndim(e3) == 2 else e3
    ep = [sum(e3[a, j]*p0[j] for j in range(3)) for a in range(3)]
    return [ep[a]*Sp0[a] for a in range(3)] + [sum(Wp0[i]*ep[i] for i in range(3))]
def Gsym(Ma):   # Ma: list of 3x3 arrays-of-arrays? we pass constant tensors only
    return G(Ma)
def block(qvec, omega, pols, sea=None):
    qvec = np.asarray(qvec, float)
    cp = cvec([k + q/2 for k, q in zip(K, qvec)]); cm = cvec([k - q/2 for k, q in zip(K, qvec)])
    Ep = np.sqrt(sum(c*c for c in cp)); Em = np.sqrt(sum(c*c for c in cm)); E = Ep + Em
    u = [c/Ep for c in cp]; v = [c/Em for c in cm]; uv = sum(a*b for a, b in zip(u, v))
    Gqq = G(np.outer(qvec, qvec))
    vecs = []
    for e in pols:
        esp = e[1:, 1:]; w = np.array([e[0, 1+j] + e[1+j, 0] for j in range(3)])
        Gs = G(esp); Gqw = G(np.outer(qvec, w))
        Ga = [Gs[a] + Gqw[a]/E + e[0, 0]*Gqq[a]/E**2 for a in range(4)]
        Gb = [Gs[a] - Gqw[a]/E + e[0, 0]*Gqq[a]/E**2 for a in range(4)]
        vecs.append((Ga, Gb))
    def gram(A, B):
        AB = sum(a*b for a, b in zip(A, B)); uA = sum(a*b for a, b in zip(u, A)); vB = sum(a*b for a, b in zip(v, B))
        uB = sum(a*b for a, b in zip(u, B)); vA = sum(a*b for a, b in zip(v, A))
        return (Nc/4)*(AB*(1 + uv) - uA*vB - uB*vA)
    n = len(pols); P = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            val = -Wt*np.sum(gram(vecs[i][0], vecs[j][0])/(E - omega) + gram(vecs[i][1], vecs[j][1])/(E + omega))
            P[i, j] = P[j, i] = val
    if sea is not None: P = P + sea(pols)
    return P
def seagull(lam):
    def S(pols):
        sp = [emb(e[1:, 1:]) for e in pols]
        tr = np.array([np.trace(e[1:, 1:]) for e in pols])
        return -block(np.zeros(3), 0.0, sp) + lam*np.outer(tr, tr)
    return S
print('Dirac D1(%.6f, %.6f), UD midpoint, m = %g, N = %d, Nc = 4' % (bf, r, m, N))
t4 = np.array([1., 0, 0, 0]); nx = np.r_[0., n3]
s = 0.05; q = s*n3
print('(1) Ward-contact test, bubble only, s = %.3f' % s)
for w in (0.0, 0.03, 0.05, 0.2):
    P = block(q, w, [E1F, gauge(t4, w, q), gauge(nx, w, q)])
    print('   omega=%.3f e1.Pi.g0 = %+.2e  e1.Pi.gn = %+.10e  g0.Pi.g0 = %+.10e  g0.Pi.gn = %+.6e  gn.Pi.gn = %+.10e' % (w, P[0, 1], P[0, 2], P[1, 1], P[1, 2], P[2, 2]))
print('(3) face1 row [Pi_11(s,s) - Pi_11(0,0)]/s^2 /4 (dface normalization e:e = 1/2):')
v = []
for s in (0.02, 0.01):
    P = block(s*n3, s, [E1F])[0, 0] - block(0*n3, 0.0, [E1F])[0, 0]; v.append(P/s**2/4); print('   s=%.2f %+.8e' % (s, v[-1]))
print('   Richardson %+.8e' % ((4*v[1] - v[0])/3))
print('(4) Schur/s^2 on shell (bubble + ultralocal seagull, total degree-0 = lam_b (tr h)^2), e:e = 2 units:')
for lam in (0.0, 1e-2):
    Sg = seagull(lam); line = []
    for s in (0.08, 0.04, 0.02):
        q = s*n3; w = s
        P = block(q, w, [E1F, gauge(t4, w, q), gauge(nx, w, q)], sea=Sg)
        sch = P[0, 1:] @ np.linalg.solve(P[1:, 1:], P[0, 1:])
        line.append('s=%.2f Pi_1g0=%+.1e Pi_1gn=%+.3e Schur/s^2=%+.4e' % (s, P[0, 1], P[0, 2], sch/s**2))
    print('  lam_b=%g:' % lam); [print('     ', l) for l in line]
print('runtime %.1f s' % (time.time() - t0))
