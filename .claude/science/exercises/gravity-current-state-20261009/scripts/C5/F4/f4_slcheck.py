"""F4 checks at sample points (t = 0.05, R18-9 root, B1):
 (i)  single-order M-staircase: right vertex V_x^sigma(q,0) (computed from its own definition, photon -q) equals the left vertex of the
      reversed order V_x^{sigma^rev}(0,q)  -> the sigma-averaged family is hermitian (VR = VL);
 (ii) M -> infinity: the sigma-averaged staircase vertex and seagull converge to the straight-line (Peierls) forms
        V_j^SL(0,q) = (q_j/d_j) int_0^1 d_j D_t(s q) ds,   N_j^SL = q_j^2 int_0^1 (1-u) d_j^2 M_t(u q) du,
      at rate O(1/M^2) (derivatives by 4th-order central differences, h = 1e-3; s/u by 48-node Gauss-Legendre on 4 panels)."""
import numpy as np, sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f4_lib import *
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH); t = 0.05; nrk = 4
rng = np.random.default_rng(1)
Q = rng.uniform(0.05, np.pi - 0.05, size=(3, 400))
def Dt(k):
    kx, ky, kz = k
    Wz = F.W(kz); fx, fy = flowF(F, kx, ky, Wz, t, nrk)
    return np.array([F.s(fx), F.s(fy), F.s(kz) + 0*fx, F.W(fx) + F.W(fy) + Wz])
d = np.array([G.d(flowG1(G, Q[0], +1, t, nrk)), G.d(flowG1(G, Q[1], -1, t, nrk)), G.d(Q[2])])
E3 = np.eye(3)
def qS(S): return np.array([Q[i]*(1.0 if a in S else 0.0) for i, a in enumerate(AX)])
# (i) hermiticity of the sigma average
worst = 0.0
for M in (1, 2, 3):
    for sig in itertools.permutations(AX):
        for j, a in enumerate(AX):
            Sb = set(sig[:sig.index(a)])
            Sr = set(sig[::-1][:sig[::-1].index(a)])
            VR = 0.0; VL = 0.0
            for r in range(M):
                B = (r*Q + qS(Sb))/M
                VR = VR + (Dt(Q - B) - Dt(Q - B - E3[j][:, None]*Q[j]/M))
                Br = (r*Q + qS(Sr))/M
                VL = VL + (Dt(Br + E3[j][:, None]*Q[j]/M) - Dt(Br))
            worst = max(worst, float(np.max(np.abs(VR - VL)/d[j])))
print('(i) max |V^sigma(q,0) - V^{sigma rev}(0,q)| over M=1,2,3, all sigma, j, 400 pts: %.2e' % worst)
# (ii) SL forms
xg, wg = np.polynomial.legendre.leggauss(48)
sn = np.concatenate([(xg + 1)/8 + i/4 for i in range(4)]); sw = np.concatenate([wg/8]*4)
h = 1e-3
VSL = np.zeros((3, 4, Q.shape[1])); NSL = np.zeros((3, Q.shape[1]))
for s, wv in zip(sn, sw):
    for j in range(3):
        e = E3[j][:, None]
        f = {m: Dt(s*Q + m*h*e) for m in (-2, -1, 0, 1, 2)}
        d1 = (f[-2] - 8*f[-1] + 8*f[1] - f[2])/(12*h)
        d2 = (-f[-2] + 16*f[-1] - 30*f[0] + 16*f[1] - f[2])/(12*h*h)
        VSL[j] += wv*d1*Q[j]/d[j]
        NSL[j] += wv*(1 - s)*d2[3]*Q[j]**2
WS_ = {0: 1/3, 1: 1/6, 2: 1/3}
def stair(M):
    V = np.zeros((3, 4, Q.shape[1])); N = np.zeros((3, Q.shape[1]))
    for j, a in enumerate(AX):
        oth = [o for o in AX if o != a]
        for r in range(M):
            for S in ([], [oth[0]], [oth[1]], oth):
                V[j] += WS_[len(S)]*(Dt((r*Q + qS(S + [a]))/M) - Dt((r*Q + qS(S))/M))/d[j]
            N[j] += (M - r)*Dt((r*Q + qS([a]))/M)[3] + (M - r - 1)*Dt((r*Q + qS(oth))/M)[3]
            if r >= 1:
                N[j] -= 2*(M - r)*Dt(r*Q/M)[3]
    return V, N
print('(ii) staircase -> straight line (max over 400 pts, j, components):')
print('     ward residual of SL vertex: %.2e' % np.max(np.abs(sum(VSL[j]*d[j] for j in range(3)) - Dt(Q))))
prev = None
for M in (1, 2, 4, 8, 16, 32):
    V, N = stair(M)
    eV = np.max(np.abs(V - VSL)); eN = np.max(np.abs(N - NSL))
    print('     M=%2d  max|V_M - V_SL| %.3e   max|N_M - N_SL| %.3e%s' % (M, eV, eN, '' if prev is None else '   ratios %.2f %.2f' % (prev[0]/eV, prev[1]/eN)))
    prev = (eV, eN)
print('     typical sizes: max|V_SL| %.3f  max|N_SL| %.3f ; non-separable part of V (max|V_SL - V_1|) %.3e' % (np.max(np.abs(VSL)), np.max(np.abs(NSL)), np.max(np.abs(VSL - stair(1)[0]))))
