"""R19-19 (b)/(d): Taylor structure of the one-loop vacuum TT self-energy and the O(p^4) remainder left by (S**).
Model: NN lattice scalar eps^2 = m^2 + sum 4 sin^2(k_i/2), U vertex with R17-4's E1 extension
  V_e(k) = sum_ij e_ij f_i f_j, f_i = sin k_i, pair (k + q/2, k - q/2).
R9-9: Pi(omega, q) = S2 - 1/4 < W/(e+ e-) * E/(E^2 - omega^2) >, W = V_e^2, E = e+ + e-; S2 (ultralocal seagull) drops out
of every row except mu, and out of the remainder.
Rows: Xi = d Pi/d q^2 + d Pi/d omega^2 at 0 (R17-4 values for NN/U at m = 1: face1 -1.245452931e-4, face2 -2.289166113e-4).
(S**) keeps only the LI form through O(p^2), so the gravitating remainder is R(omega, q) = Pi - [Pi(0,0) + alpha q^2 + beta omega^2]
(+ a LI piece Z(omega^2 - q^2), which vanishes on shell).  On shell (omega = |q| = s): R = c4(n,e) s^4 + O(s^6).
Dispersion with the remainder: omega^2 = q^2 [1 + (2/M^2) c4 q^2], 2/M^2 = 16 pi at a = l_P (R9-9 normalization)."""
import numpy as np, sys
r2 = np.sqrt(2)
def pols():
    z = np.array([0, 0, 1.]); fd = np.array([1, 1, 0])/r2
    Eg = np.diag([1., -1, 0]); T2 = np.zeros((3, 3)); T2[0, 1] = T2[1, 0] = 1
    a = np.array([1, -1, 0])/r2; bz = z
    F1 = np.outer(a, a)-np.outer(bz, bz); F2 = np.outer(a, bz)+np.outer(bz, a)
    return [('Eg', z, Eg), ('T2g', z, T2), ('face1', fd, F1), ('face2', fd, F2)]
P = pols()

class Grid:
    def __init__(self, N, m):
        k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
        self.k = np.stack(np.meshgrid(k, k, k, indexing='ij'))   # 3 x N x N x N
        self.m = m
        f = np.sin(self.k)
        self.W = {}
        for nm, n, e in P:
            V = np.einsum('ij,i...,j...->...', e, f, f)
            self.W[nm] = V*V
    def eps(self, shift):
        kk = self.k + shift[:, None, None, None]
        return np.sqrt(self.m**2 + (4*np.sin(kk/2)**2).sum(0))
    def F(self, nm, n, om, s):
        ep = self.eps(+s*n/2); em = self.eps(-s*n/2); E = ep + em
        return -0.25*np.mean(self.W[nm]/(ep*em)*E/(E*E - om*om))

def run(N, m, svals=(0.4, 0.2, 0.1, 0.05)):
    g = Grid(N, m)
    print('\n=== NN scalar, U vertex (E1), m = %g, N = %d ===' % (m, N)); sys.stdout.flush()
    for nm, n, e in P:
        F0 = g.F(nm, n, 0.0, 0.0)
        h = 0.02
        # alpha, beta by symmetric 5-point Richardson in s^2 / omega^2
        def d2(fun):
            a1 = (fun(h) - F0)/h**2; a2 = (fun(2*h) - F0)/(2*h)**2
            return (4*a1 - a2)/3
        alpha = d2(lambda x: g.F(nm, n, 0.0, x)); beta = d2(lambda x: g.F(nm, n, x, 0.0))
        Xi = alpha + beta
        line = '%-6s Xi = %+.9e (alpha %+.6e, beta %+.6e)' % (nm, Xi, alpha, beta)
        # on-shell remainder after (S**)
        rem = []
        for s in svals:
            R = g.F(nm, n, s, s) - F0 - Xi*s*s
            rem.append((s, R, R/s**4))
        line += '\n        on-shell R/s^4: ' + '  '.join('s=%.2f: %+.4e' % (s, c) for s, R, c in rem)
        # off-shell remainder scaling along a ray (omega, q) = t*(0.6, 1.0)
        offs = []
        for t in (0.2, 0.1, 0.05):
            om, s = 0.6*t, 1.0*t
            R = g.F(nm, n, om, s) - F0 - alpha*s*s - beta*om*om
            offs.append(R)
        line += '\n        off-shell ray (0.6t, t): R(t)/R(t/2) = %.3f, %.3f (16 = pure p^4)' % (offs[0]/offs[1], offs[1]/offs[2])
        print(line); sys.stdout.flush()

if __name__ == '__main__':
    for N, m in [(48, 1.0), (64, 1.0), (96, 0.5), (128, 0.3)]:
        run(N, m)
