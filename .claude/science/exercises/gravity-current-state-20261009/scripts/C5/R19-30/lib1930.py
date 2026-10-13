"""R19-30 library: placement audit of R19-5's massive-species pair kernels (scalar U, Dirac UD) at R9-9's placement.

Conventions (R9-9 / R13-5 / R19-5 / lib199; Lemma P rechecked in r1930_lemmaP.py):
  * site-label ("periodic-gauge") kernel G^{mu nu}(k1,k2): the kernel that obeys W1 with the PERIODIC divergence
    D_j(q) = dsym(q_j) e^{i q_j/2}.  A stress is local  <=>  G is C^infty on the torus T^3 x T^3 (both legs mod 2 pi).
  * tilde (true-position) kernel  M~ = e^{+i q.p} G,  p_{ij} = (e_i + e_j)/2, q the graviton representative wrap(.).
    The one-loop TT rows use M~ with the real tilde TT polarization (R9-9 sec. 3.2: sum h^* T = sum h~^* T~).
  * Lemma P: G smooth  <=>  M~ flips by (-1)^{2 p_l} when q_l crosses +-pi (legs fixed).
Channels:
  * Dirac (R19-5 r195_dirac_exact.py): scattering labelling psi^dag(k1) M psi(k2), q = wrap(k1 - k2), kbar = k2 + q/2;
    pair blocks P+(k1) X P-(k2) and P-(k1) X P+(k2).
  * scalar (R13-5 r135_w1_pair.py): pair creation a^dag_{k1} a^dag_{k2}, q = wrap(k1 + k2), relative K = k1 - q/2.
Laws are evaluated ANALYTICALLY (C^infty; Gauss-Legendre cumulative tables, ~1e-16) so Fourier tails are not limited
by tabulation: scalar G_w(bs, pi - bs) (R18-13 root edge, ZLaw form) and Dirac D1(b, r) (R14-1 / R18-9 root edge)."""
import numpy as np

def sstep(x):
    x = np.clip(np.asarray(x, float), 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def sqrt_st1mst(x):
    """sqrt(st (1 - st)) computed as sqrt(e1 e2)/(e1 + e2): no cancellation in 1 - st (the naive form has ~1e-8
    absolute noise near the slab edges because sqrt amplifies the 1e-16 rounding of 1 - st)."""
    x = np.clip(np.asarray(x, float), 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
        return np.sqrt(e1*e2)/(e1 + e2)

def wrap(k):
    return -(((-np.asarray(k, float)) + np.pi) % (2*np.pi) - np.pi)

def Fplace(q):                       # R19-26's re-placement factor: antiperiodic, F(0)=1, F''(0)=0, F(+-pi)=0
    q = np.asarray(q, float)
    return (9.0*np.cos(0.5*q) - np.cos(1.5*q))/8.0

XG, WGL = np.polynomial.legendre.leggauss(16)
class CumInt:
    """u -> int_0^u fun, u in [0,1]; 4096-panel cumulative 16-pt GL + one GL panel to the target (~1e-16)."""
    def __init__(self, fun, NP=4096):
        self.f, self.NP = fun, NP
        ub = np.linspace(0.0, 1.0, NP + 1); self.ub = ub
        self.cum = np.concatenate([[0.0], np.cumsum(self._gl(ub[:-1], ub[1:]))])
    def _gl(self, a, b):
        a = np.asarray(a, float); b = np.asarray(b, float); h = 0.5*(b - a); m = 0.5*(b + a)
        return h*(self.f(m[..., None] + h[..., None]*XG)*WGL).sum(-1)
    def __call__(self, u):
        u = np.clip(np.asarray(u, float), 0.0, 1.0); i = np.minimum((u*self.NP).astype(int), self.NP - 1)
        return self.cum[i] + self._gl(self.ub[i], u)

_Ist = CumInt(sstep)                                            # int_0^u sstep
_Iw = CumInt(lambda x: 2*sqrt_st1mst(x))

# ---------------- scalar: G_w(bs, w = pi - bs), sigma' = 1 - sstep((|k| - bs)/w) ----------------------------------
class Scalar:
    def __init__(self, bs=2.5261508, m=0.01):
        self.bs, self.w, self.m = bs, np.pi - bs, m
    def sig(self, k):
        k = wrap(k); a = np.abs(k)
        return np.sign(k)*np.where(a <= self.bs, a, a - self.w*_Ist((a - self.bs)/self.w))
    def sigp(self, k):
        return 1.0 - sstep((np.abs(wrap(k)) - self.bs)/self.w)
    def f(self, k):                   # U's per-axis factor f = sigma sigma' = u'/2  (= R13-5's w for U)
        return self.sig(k)*self.sigp(k)
    def eps(self, k):                 # k (..., 3)
        return np.sqrt(self.m**2 + (self.sig(k)**2).sum(-1))

# ---------------- Dirac D1(b, r): h = sum S(k_j) alpha_j + M beta, M = m + sum W(k_j) -------------------------------
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
GAM = np.array([np.block([[Z2, s], [s, Z2]]) for s in (s1, s2, s3)] + [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)])
I4 = np.eye(4, dtype=complex)

class Dirac:
    def __init__(self, b=0.909103707957, r=0.555604225797, m=0.01):
        self.b, self.r, self.m, self.w = b, r, m, np.pi - 2*b
        self.Wpi = self.w*r*float(_Iw(np.array([1.0]))[0])
    def S(self, k):
        k = wrap(k); a = np.abs(k); b, w = self.b, self.w
        v = np.where(a <= b, a, np.where(a >= np.pi - b, np.pi - a, a - 2*w*_Ist((a - b)/w)))
        return np.sign(k)*v
    def dS(self, k):
        return 1 - 2*sstep((np.abs(wrap(k)) - self.b)/self.w)
    def W(self, k):
        return self.w*self.r*_Iw((np.abs(wrap(k)) - self.b)/self.w)
    def dW(self, k):
        k = wrap(k)
        return np.sign(k)*2*self.r*sqrt_st1mst((np.abs(k) - self.b)/self.w)
    def coef(self, k):                # c_a(k), a = x, y, z, beta ;  h = c . GAM
        S = self.S(k); M = self.m + self.W(k).sum(-1)
        return np.concatenate([S, M[..., None]], -1)
    def h(self, k):
        return np.einsum('...a,aij->...ij', self.coef(k), GAM)
    def E(self, k):
        return np.sqrt((self.coef(k)**2).sum(-1))
    def proj(self, k, sgn):
        return 0.5*(I4 + sgn*self.h(k)/self.E(k)[..., None, None])
    def UDcoef(self, k, i, j):
        """UD^{ij}(k) = (1/2)(p_j d_i h + p_i d_j h) as Clifford coefficients (..., 4); p = S S' + M W'."""
        S, Sp, Wp = self.S(k), self.dS(k), self.dW(k); M = self.m + self.W(k).sum(-1)
        p = S*Sp + M[..., None]*Wp
        c = np.zeros(k.shape[:-1] + (4,))
        c[..., i] += 0.5*p[..., j]*Sp[..., i]; c[..., j] += 0.5*p[..., i]*Sp[..., j]
        c[..., 3] += 0.5*(p[..., j]*Wp[..., i] + p[..., i]*Wp[..., j])
        return c

# ---------------- parity classes and the re-placement ------------------------------------------------------------------
EPS3 = [np.array(e) for e in np.ndindex(2, 2, 2)]
def tau(i, j):                        # 2 p_ij mod 2 as a 0/1 vector: the bond-offset parity that sits at p_ij
    t = np.zeros(3, int); t[i] += 1; t[j] += 1; return t % 2

def parity_parts(fun, kb):
    """fun(kb) (..., c) -> dict sigma -> f_sigma(kb), f_sigma(kb + pi e_l) = (-1)^{sigma_l} f_sigma(kb); sum = fun."""
    vals = {tuple(e): fun(kb + np.pi*e) for e in EPS3}
    out = {}
    for s in EPS3:
        acc = 0.0
        for e in EPS3:
            acc = acc + (-1.0)**int(s @ e)*vals[tuple(e)]
        out[tuple(s)] = acc/8.0
    return out

def A_sigma(q, sig, t):               # prod over mismatched directions of F(q_l)
    a = np.ones(q.shape[:-1])
    for l in range(3):
        if sig[l] != t[l]:
            a = a*Fplace(q[..., l])
    return a

def tilde_component(fun, kb, q, i, j, mode):
    """tilde (true-position) amplitude of component ij for a midpoint/per-leg kernel 'fun' evaluated at kb.
    mode: 'raw' (as given), 'FF' (R19-26's F(q_i)F(q_j) on i != j), 'PR' (parity-resolved re-placement)."""
    if mode == 'raw':
        return fun(kb)
    if mode == 'FF':
        v = fun(kb)
        if i != j:
            v = v*(Fplace(q[..., i])*Fplace(q[..., j]))[..., None]
        return v
    if mode == 'PR':
        t = tau(i, j); parts = parity_parts(fun, kb); acc = 0.0
        for s, v in parts.items():
            acc = acc + A_sigma(q, np.array(s), t)[..., None]*v
        return acc
    raise ValueError(mode)

def place_phase(q, i, j):             # e^{-i q.p_ij}: site-label G = phase * tilde
    return np.exp(-0.5j*(q[..., i] + q[..., j]))
