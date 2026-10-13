"""R19-29 bracket for the R19-30 heads-up (unrefereed): a MODEL of R19-5's literal Dirac pair block, in which the UD pair
kernel's component (i,j) carries the uncancelled placement phase phi_ij = exp(i sgn q.p_ij), p_ii = e_i, p_ij = (e_i+e_j)/2
(R19-30 report: 'a relative phase e^{iq_x} on zz against xx/yy/xy' for face1), conjugate phase in the conjugate channel.
Time components by P1 on the phased kernel (real midpoint d(q) = q). Hermitian Gram form
   Gam(A,B) = (Nc/4)[A*.B (1+u.v) - (u.A*)(v.B) - (u.B)(v.A*)],  Pi_AB = -<Gam_a(A,B)/(E-w) + conj(Gam_a(A,B))-type b term>.
Compares with the rows' convention (sgn = 0).  usage: python r1929_dirac_lit.py bf r m N"""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch18'))
from content3 import D1q
from a1lib import emb, E1F, n3, gauge
bf, r, m, N = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
law = D1q(bf, r); Nc = 4
x = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
K = [k.ravel() for k in np.meshgrid(x, x, x, indexing='ij')]; Wt = 1.0/N**3
S0 = [law.S(k) for k in K]; Sp0 = [law.dS(k) for k in K]; W0 = [law.W(k) for k in K]; Wp0 = [law.dW(k) for k in K]
M0 = m + sum(W0); p0 = [S0[i]*Sp0[i] + M0*Wp0[i] for i in range(3)]
def Gunit(i, j):
    e3 = np.zeros((3, 3)); e3[i, j] += 0.5; e3[j, i] += 0.5
    ep = [sum(e3[a, jj]*p0[jj] for jj in range(3)) for a in range(3)]
    return [ep[a]*Sp0[a] for a in range(3)] + [sum(Wp0[ii]*ep[ii] for ii in range(3))]
GU = {(i, j): Gunit(i, j) for i in range(3) for j in range(i, 3)}
def Gph(e3, q, sgn):
    out = [0j*M0 for _ in range(4)]
    for (i, j), g in GU.items():
        c = e3[i, j] + (e3[j, i] if i != j else 0.0)
        if c == 0: continue
        pij = (np.eye(3)[i] + np.eye(3)[j])/2
        ph = np.exp(1j*sgn*(q @ pij))
        for a in range(4): out[a] = out[a] + c*ph*g[a]
    return out
def block(q, w, pols, sgn):
    q = np.asarray(q, float)
    cv = lambda Ks: [law.S(k) for k in Ks] + [m + sum(law.W(k) for k in Ks)]
    cp = cv([k + qq/2 for k, qq in zip(K, q)]); cm = cv([k - qq/2 for k, qq in zip(K, q)])
    Ep = np.sqrt(sum(c*c for c in cp)); Em = np.sqrt(sum(c*c for c in cm)); E = Ep + Em
    u = [c/Ep for c in cp]; v = [c/Em for c in cm]; uv = sum(a*b for a, b in zip(u, v))
    Gqq = Gph(np.outer(q, q), q, sgn)
    vecs = []
    for e in pols:
        esp = e[1:, 1:]; wv = np.array([e[0, 1+j] + e[1+j, 0] for j in range(3)])
        Gs = Gph(esp, q, sgn); Gqw = Gph(np.outer(q, wv), q, sgn)
        Ga = [Gs[a] + Gqw[a]/E + e[0, 0]*Gqq[a]/E**2 for a in range(4)]
        Gb = [Gs[a] - Gqw[a]/E + e[0, 0]*Gqq[a]/E**2 for a in range(4)]
        vecs.append((Ga, Gb))
    def gram(A, B):   # sum over pair states of conj(amp_A) amp_B
        Ac = [np.conj(a) for a in A]
        AB = sum(a*b for a, b in zip(Ac, B)); uA = sum(a*b for a, b in zip(u, Ac)); vB = sum(a*b for a, b in zip(v, B))
        uB = sum(a*b for a, b in zip(u, B)); vA = sum(a*b for a, b in zip(v, Ac))
        return (Nc/4)*(AB*(1 + uv) - uA*vB - uB*vA)
    n = len(pols); P = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(n):
            # creation channel a: conj(a_A) a_B ; conjugate channel b: amplitudes conj -> conj(b_B) b_A = conj(gram(b_A, b_B))
            P[i, j] = -Wt*np.sum(gram(vecs[i][0], vecs[j][0])/(E - w) + np.conj(gram(vecs[i][1], vecs[j][1]))/(E + w))
    return P
def seagull(lam, sgn):
    def S(pols):
        sp = [emb(e[1:, 1:]) for e in pols]; tr = np.array([np.trace(e[1:, 1:]) for e in pols])
        return -block(np.zeros(3), 0.0, sp, sgn) + lam*np.outer(tr, tr)
    return S
t4 = np.array([1., 0, 0, 0]); nx = np.r_[0., n3]
print('Dirac D1(%.6f, %.6f) m=%g N=%d' % (bf, r, m, N))
for sgn, lab in ((0, "rows' convention (midpoint, no residual phase) = this report"), (1, 'literal R19-5 model, phase +'), (-1, 'literal R19-5 model, phase -')):
    print('\n== %s ==' % lab)
    s = 0.05; q = s*n3
    for w in (0.0, 0.05, 0.2):
        P = block(q, w, [E1F, gauge(t4, w, q), gauge(nx, w, q)], sgn)
        print('   s=%.2f omega=%.2f  e1.Pi.g0 = %+.3e%+.3ei  e1.Pi.gn = %+.6e%+.3ei  g0.Pi.g0 = %+.6e' % (s, w, P[0, 1].real, P[0, 1].imag, P[0, 2].real, P[0, 2].imag, P[1, 1].real))
    v = []
    for s in (0.02, 0.01):
        P = block(s*n3, s, [E1F], sgn)[0, 0] - block(0*n3, 0.0, [E1F], sgn)[0, 0]; v.append(P.real/s**2/4)
    print('   face1 raw row (dface units) %+.6e' % ((4*v[1] - v[0])/3))
    for lam in (0.0, 1e-2):
        Sg = seagull(lam, sgn); line = []
        for s in (0.08, 0.04, 0.02):
            q = s*n3; w = s
            P = block(q, w, [E1F, gauge(t4, w, q), gauge(nx, w, q)], sgn) + Sg([E1F, gauge(t4, w, q), gauge(nx, w, q)])
            P1G = P[0, 1:]; PG1 = P[1:, 0]
            sch = P1G @ np.linalg.solve(P[1:, 1:], PG1)
            line.append('s=%.2f |Pi_1g0|=%.2e Schur/s^2=%+.4e%+.1ei' % (s, abs(P[0, 1]), sch.real/s**2, sch.imag/s**2))
        print('   lam_b=%g: ' % lam + ' | '.join(line))
