"""F4 Lemma 4 check (locality): torus continuity of the vertex at the zone face q_y = +-pi.
Reflection covariance gives V_x(0, R_y q) = (a_x, -a_y, a_z, b)(q), so V_x is continuous across q_y = pi iff a_y(q_x, pi, q_z) = 0
(a_y = gamma_y component of V_x).  Same for b-type components of V_y? (V_y(0,R_y q) = -(...) with d_y odd: handled by d's own sign.)
Also J and the 26-neighbour identity: J's phase = straight line with multilinear link interpolation for hops with |n_j| <= 1 (proved
in the report; here the weights int (1-s)^2, int s(1-s), int s^2 = 1/3, 1/6, 1/3 are printed)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f4_lib import *
F = Ferm(*ROOT, mflow=0.01); G = Phot(CPH)
rng = np.random.default_rng(2)
n = 300
qx = rng.uniform(0.05, np.pi - 0.05, n); qz = rng.uniform(0.05, np.pi - 0.05, n)
for t in (0.0, 0.05):
    def Dt(k):
        kx, ky, kz = k
        Wz = F.W(kz); fx, fy = flowF(F, kx, ky, Wz, t, 4)
        return np.array([F.s(fx), F.s(fy), F.s(kz) + 0*fx, F.W(fx) + F.W(fy) + Wz])
    for qy in (np.pi, np.pi - 1e-3):
        Q = np.array([qx, qy + 0*qx, qz])
        def qS(S): return np.array([Q[i]*(1.0 if a in S else 0.0) for i, a in enumerate(AX)])
        out = []
        for M in (1, 2, 4):
            V = 0.0
            for r in range(M):
                for S in ([], ['y'], ['z'], ['y', 'z']):
                    V = V + WS[len(S)]*(Dt((r*Q + qS(S + ['x']))/M) - Dt((r*Q + qS(S))/M))
            out.append(np.max(np.abs(V[1])))
        print('t=%.2f q_y=%.4f: max |gamma_y part of d_x V_x| over %d pts: P %.2e  S2 %.2e  S4 %.2e' % (t, qy, n, *out))
s = np.polynomial.legendre.leggauss(20); u = 0.5*(s[0] + 1); w = 0.5*s[1]
print('multilinear weights int(1-s)^2, int s(1-s), int s^2 =', np.round([np.sum(w*(1-u)**2), np.sum(w*u*(1-u)), np.sum(w*u**2)], 12), '(Psym base weights 1/3, 1/6, 1/3)')
