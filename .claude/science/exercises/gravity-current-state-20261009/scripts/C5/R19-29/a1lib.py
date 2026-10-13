"""R19-29 library: the A_1 face block of the one-loop vacuum response for a pair-creating real scalar
on R18-9's root scalar edge, U vertex with R17-4's E1 extension, time components by R19-5's P1
(exact W1 in the pair channel), ultralocal seagull (R9-9 H-seagull; R18-13 inherited).

Conventions (stated; checked by the Ward-contact test in r1929_struct.py):
  * graviton coupling 1/2 h_{mu nu} T^{mu nu}; gauge direction g(xi)_{mu nu} = p_mu xi_nu + p_nu xi_mu, p = (-omega, q)
    (midpoint variables, d(q) = q on the graviton box: |q_i| <= 1, which holds for every s used here).
  * pair at relative momentum k: legs k + q/2 and -(k - q/2), energies ep = eps(k+q/2), em = eps(k-q/2), E = ep + em.
  * spatial pair amplitude M_ij = V_ij / sqrt(8 ep em), V_ij = tau_ij(k) (E1: q-independent at fixed relative k).
    U: tau_ij = f_i f_j, f = sigma sigma'  (R17-4 offaxis.py docstring).  Optional trace completion: tau_ij -= delta_ij * ell.
  * P1 (R19-5): ordering a (denominator E - omega): a^{0j} = q_i M_ij / E, a^{00} = q_i q_j M_ij / E^2;
                ordering b (denominator E + omega): b^{0j} = -q_i M_ij / E, b^{00} = q_i q_j M_ij / E^2.
  * Pi(e, e'; omega, q) = - < (e:a)(e':a)/(E - omega) + (e:b)(e':b)/(E + omega) >,  <.> = int d^3k/(2pi)^3.
    For spatial e, e' this is R9-9's  -(1/4)<V V'/(ep em) E/(E^2 - omega^2)>.
"""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'arch17_4'))
from zz import ZLaw

r2 = np.sqrt(2.)
n3 = np.array([1., 1., 0.])/r2
a3 = np.array([1., -1., 0.])/r2
b3 = np.array([0., 0., 1.])
def emb(e3):
    e = np.zeros((4, 4)); e[1:, 1:] = e3; return e
E1F = emb(np.outer(a3, a3) - np.outer(b3, b3))     # face1 TT, e:e = 2
NN = emb(np.outer(n3, n3))
TRP = emb(np.outer(a3, a3) + np.outer(b3, b3))       # the other spatial A1 transverse direction

def root_scalar_law(root=None):
    z = np.load(root or os.path.join(HERE, 'root_refR18-9.npy'))
    bs, fr = z[0], z[4]; wA = fr*(np.pi - bs)
    return ZLaw([1.0, 0.0], [bs + wA/2], wA), z

class Scalar:
    def __init__(self, law, m, N, trace=None, quad='mid'):
        self.law, self.m, self.N, self.trace = law, m, N, trace
        if quad == 'mid':
            x = 2*np.pi*(np.arange(N)+0.5)/N - np.pi; w = np.full(N, 1.0/N)
        else:   # composite Gauss-Legendre with panels refined near 0 (for small m)
            x, w = quad
        self.x1, self.w1 = x, w
        K = np.meshgrid(x, x, x, indexing='ij'); self.K = [k.ravel() for k in K]
        W = np.einsum('i,j,k->ijk', w, w, w).ravel(); self.W = W
        self.f0 = [self.f(k) for k in self.K]
    def sig(self, k):
        a = np.abs(k); return np.sign(k)*np.interp(a, self.law.k, self.law.sig)
    def f(self, k):
        a = np.abs(k); s = np.interp(a, self.law.k, self.law.sig); sp = np.interp(a, self.law.k, self.law.sp)
        return np.sign(k)*s*sp
    def eps(self, K):
        g = sum(np.interp(np.abs(k), self.law.k, self.law.sig)**2 for k in K)
        return np.sqrt(self.m**2 + g)
    def tau(self, e3):
        """V_e = sum_ij e_ij tau_ij at relative momentum k (q-independent, E1)."""
        f = self.f0
        V = sum(e3[i, j]*f[i]*f[j] for i in range(3) for j in range(3))
        if self.trace is not None:
            V = V - np.trace(e3)*self.trace(self)
        return V
    def amps(self, qvec):
        """per-k quantities for q = qvec: E, norm, and the spatial amplitude matrix as callables."""
        ep = self.eps([k + q/2 for k, q in zip(self.K, qvec)])
        em = self.eps([k - q/2 for k, q in zip(self.K, qvec)])
        return ep, em
    def block(self, qvec, omega, pols, seagull=None):
        """Pi(e_A, e_B; omega, q) for 4x4 polarization tensors (callables of p allowed). Returns matrix."""
        qvec = np.asarray(qvec, float)
        ep, em = self.amps(qvec); E = ep + em; nrm = 1.0/np.sqrt(8*ep*em)
        f = self.f0
        # M_ij = nrm * tau_ij ; need q.M (vector) and q.M.q
        def Mcontract(e4):
            e3 = e4[1:, 1:]
            sp = self.tau(e3)                                       # e_ij tau_ij
            # q_i M_ij e_{0j} terms: sum_j (e_{0j}+e_{j0}) (q.tau)_j
            qt = [sum(qvec[i]*self._tauij(i, j) for i in range(3)) for j in range(3)]
            qtq = sum(qvec[j]*qt[j] for j in range(3))
            e0j = [e4[0, 1+j] + e4[1+j, 0] for j in range(3)]
            mixa = sum(e0j[j]*qt[j] for j in range(3))/E
            a = nrm*(sp + mixa + e4[0, 0]*qtq/E**2)
            b = nrm*(sp - mixa + e4[0, 0]*qtq/E**2)
            return a, b
        AB = [Mcontract(e) for e in pols]
        n = len(pols); P = np.zeros((n, n))
        for i in range(n):
            for j in range(i, n):
                val = -np.sum(self.W*(AB[i][0]*AB[j][0]/(E - omega) + AB[i][1]*AB[j][1]/(E + omega)))
                P[i, j] = P[j, i] = val
        if seagull is not None:
            P = P + seagull(pols)
        return P
    def _tauij(self, i, j):
        t = self.f0[i]*self.f0[j]
        if self.trace is not None and i == j:
            t = t - self.trace(self)
        return t

def gauge(xi, omega, qvec):
    p = np.r_[-omega, qvec]; xi = np.asarray(xi, float)
    return np.outer(p, xi) + np.outer(xi, p)

def ultralocal_seagull(sc, lam_b):
    """S(e, e') = -Pi^b(q=0, omega=0)(e_sp, e'_sp) + lam_b tr(e_sp) tr(e'_sp): total degree-0 spatial block = lam_b (tr h)^2
    (mu_E = mu_T2 = 0, the root's paid shear rows); no degree-0 h_{0 nu} terms ('solid', R19-23 Sec. 3.3)."""
    def S(pols):
        sp = [emb(e[1:, 1:]) for e in pols]
        P0 = sc.block(np.zeros(3), 0.0, sp)
        tr = np.array([np.trace(e[1:, 1:]) for e in pols])
        return -P0 + lam_b*np.outer(tr, tr)
    return S
