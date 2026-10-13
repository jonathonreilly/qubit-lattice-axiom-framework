"""R19-16: repaired R19-9 photon kernel.  Importing this module PATCHES lib199 (orig/ copy, unmodified file) in place:

  (R0) the photon law gammaG_w(b, w), b = 2.9435, w = pi - b, is evaluated ANALYTICALLY (its definition, photon.py:39-40:
       d' = 1 - sstep((a - b)/w), d = int_0 d'), not from the archived 400001-point trapezoid table + linear interpolation:
         c(k)     = 1 - sstep((|k| - b)/w)                     (closed form)
         sigma(k) = sgn(k) d(|k|),  d(x) = x (x <= b),  d(x) = x - w S((x - b)/w) (b < x <= pi),  S(u) = int_0^u sstep
       S is evaluated to ~1e-17 by a 4096-panel cumulative table built with 16-point Gauss-Legendre, plus one GL panel
       to the target.  sigma is then C^infinity on the twisted torus and sigma' = c exactly (up to rounding).
  (R1) divided difference Delta_j = (sigma_j(k1)^2 - sigma_j(k2)^2)/dsym(q_j), q = wrap(k1 - k2), with NO finite-width
       fallback and NO branch switch: ONE formula, valid uniformly on the whole torus (Hadamard's lemma):
         Delta_j = [q_j/dsym(q_j)] * int_0^1 g'(k2_j + t q_j) dt,   g' = (sigma^2)' = 2 sigma c   (periodic, C^infinity),
       q/dsym(q) = 1 exactly for |q| <= 1 (plateau = 1 there) and C^infinity, nonzero, on (-pi, pi].  The integral is done by
       composite 16-pt Gauss-Legendre (panels <= HMAX) split at the non-analytic points +-b, +-pi (C^infinity but flat there).
       At q_j = 0 exactly it is g'(k2_j) -- the analytic limit, no 0/0.  (The direct quotient is kept only as an optional
       cross-check branch, active if QS is set finite; default QS = inf.)
  (R2) single soft leg: time components by the analytic Neumann series in h(k_soft), on BOTH sides, everywhere on the
       support of phiA (not the eigenprojector Sylvester sum, whose projectors divide by omega_soft^2):
         left soft  (full x T2): X = -sum_n h1^n R (h2^+)^{n+1}     (solves h1 X - X h2 = R P_T2)
         right soft (T1 x full): X = +sum_n (h1^+)^{n+1} R h2^n     (solves h1 X - X h2 = P_T1 R)
       At k_soft = 0 exactly: X = -R h2^+ resp. (h1^+) R -- finite, the limit.  On the physical block these equal the
       eigen-sum solution (unique off-shell solution; checked).
Everything else (pieces C, B, glue, fibre identification, VW vertex, graviton dsym) is lib199's, unmodified."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'orig'))
import lib199 as L
from r99_profiles import sstep, wrap

BG = L.BG
WG = np.pi - BG                         # photonGw(BG, pi - BG): transition width (lib199.py:30)
XG, WGL = np.polynomial.legendre.leggauss(16)

# ---- (R0) analytic law ----------------------------------------------------------------------------------------------
NP = 4096
_ub = np.linspace(0.0, 1.0, NP + 1)
def _gl_int(f, a, b):
    """int_a^b f, 16-pt GL, vectorized over arrays a, b."""
    a = np.asarray(a, float); b = np.asarray(b, float)
    h = 0.5*(b - a); m = 0.5*(b + a)
    t = m[..., None] + h[..., None]*XG
    return h*(f(t)*WGL).sum(-1)
_Scum = np.concatenate([[0.0], np.cumsum(_gl_int(sstep, _ub[:-1], _ub[1:]))])

def S_of_u(u):
    u = np.clip(np.asarray(u, float), 0.0, 1.0)
    i = np.minimum((u*NP).astype(int), NP - 1)
    return _Scum[i] + _gl_int(sstep, _ub[i], u)

def d_exact(x):
    x = np.asarray(x, float)
    out = x.copy()
    m = x > BG
    if np.any(m):
        out[m] = x[m] - WG*S_of_u((x[m] - BG)/WG)
    return out

def sig(k):
    k = np.asarray(k, float)
    return np.sign(k)*d_exact(np.abs(k))

def cfun(k):
    return 1.0 - sstep((np.abs(np.asarray(k, float)) - BG)/WG)

def gprime(k):
    """(sigma^2)' at wrapped k: 2 sigma(k) c(k); periodic and C^infinity (c is flat zero at |k| = pi)."""
    k = np.asarray(k, float)
    k = np.where((k > -np.pi) & (k <= np.pi), k, wrap(k))      # wrap only outside the zone (no rounding inside)
    return 2.0*sig(k)*cfun(k)

class AnalyticPhotonLaw:
    """same interface as photon.PhotonProfile (d, dpr, sig, c, samples, name), analytic."""
    def __init__(self):
        self.name = 'gammaGw(%.4f,%.4f) analytic' % (BG, WG); self.dpi = float(d_exact(np.array([np.pi]))[0])
    def d(self, k): return d_exact(np.abs(np.asarray(k, float)))
    def dpr(self, k): return cfun(k)
    def sig(self, k): return sig(k)
    def c(self, k): return cfun(k)
    def samples(self, n):
        kk = (np.arange(n) + 0.5)*2*np.pi/n - np.pi; s = self.sig(kk); return s*s, s*self.dpr(kk)

# ---- (R1) uniform analytic divided difference ------------------------------------------------------------------------
QS = np.inf        # single uniform formula; set finite only to cross-check against the direct quotient
QREF = 0.25        # a generic |q| used by the tests (the earlier draft's switch point)
HMAX = 0.02        # max GL panel length in k
_BREAKS = np.array([-np.pi, -BG, BG, np.pi])

def _zone(k):
    """representative in (-pi, pi]; the identity (no rounding) when k is already there."""
    return k if -np.pi < k <= np.pi else float(wrap(np.array([k]))[0])

def dd1(k1, k2):
    """Delta for one component: (sigma(k1)^2 - sigma(k2)^2)/dsym(wrap(k1 - k2)), analytic everywhere.
    The integration segment is the actual one, [k2, k1u] with k1u = k1 or k1 -+ 2 pi (the image with k1u - k2 = q_w, the
    graviton's own wrap convention, incl. the tie q_w = +pi), so no wrap() rounding enters it; q_w = wrap(k1 - k2) enters
    only the factor q/dsym(q), which is exactly 1 for |q| <= 1."""
    k1 = _zone(k1); k2 = _zone(k2)
    q = float(wrap(np.array([k1 - k2]))[0])
    if abs(q) > QS:
        s1, s2 = sig(np.array([k1]))[0], sig(np.array([k2]))[0]   # g = sigma^2 is periodic
        return (s1*s1 - s2*s2)/float(L.dsym(np.array([q]))[0])
    dk = k1 - k2                    # choose the image of k1 with k1u - k2 = q (the SAME image as the graviton's wrap(q);
    k1u = k1 if abs(dk - q) < 1.0 else (k1 - 2*np.pi if dk > q else k1 + 2*np.pi)   # matters at the tie |q| = pi)
    if k1u == k2:
        return float(gprime(np.array([k2]))[0])
    lo, hi = (k2, k1u) if k1u > k2 else (k1u, k2)
    pts = [lo, hi]
    for m in (-2, 0, 2):
        for p in _BREAKS + m*np.pi:
            if lo < p < hi: pts.append(p)
    pts = np.sort(np.array(pts))
    tot = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        n = max(1, int(np.ceil((b - a)/HMAX)))
        e = np.linspace(a, b, n + 1)
        tot += _gl_int(gprime, e[:-1], e[1:]).sum()
    mean = tot/(hi - lo)            # mean of g' over the segment = int_0^1 g'(k2 + t (k1u - k2)) dt
    return mean if abs(q) <= 1.0 else mean*(q/float(L.dsym(np.array([q]))[0]))

def divdiff(k1, k2):
    return np.array([dd1(float(k1[j]), float(k2[j])) for j in range(3)])

# ---- (R2) analytic soft-leg solver (both sides) ----------------------------------------------------------------------
def neumann_left(R, k1, k2, nmax=400):
    h1 = L.hmat(sig(k1)); h2, w2, Pp2, Pm2, PT2, _ = L.projs(k2)
    hp = (Pp2 - Pm2)/w2
    X = np.zeros((6, 6), complex); T = R @ hp
    for n in range(nmax):
        X -= T
        T = h1 @ T @ hp
        if np.abs(T).max() < 1e-300 or np.abs(T).max() < 1e-20*np.abs(X).max(): break
    return X

def neumann_right(R, k1, k2, nmax=400):
    h2 = L.hmat(sig(k2)); h1, w1, Pp1, Pm1, PT1, _ = L.projs(k1)
    hp = (Pp1 - Pm1)/w1
    X = np.zeros((6, 6), complex); T = hp @ R
    for n in range(nmax):
        X += T
        T = hp @ T @ h2
        if np.abs(T).max() < 1e-300 or np.abs(T).max() < 1e-20*np.abs(X).max(): break
    return X

def piece_A(k1, k2, Msp, left_full, series=True):
    d = L.dsym(wrap(k1 - k2))
    M = np.zeros((4, 4, 6, 6), complex); M[1:, 1:] = Msp
    if series:
        solve = (lambda R: neumann_left(R, k1, k2)) if left_full else (lambda R: neumann_right(R, k1, k2))
    else:
        solve = lambda R: L.sylv(R, k1, k2, left_full)
    for j in range(3):
        R = np.einsum('i,iab->ab', d, Msp[:, j]); M[0, 1+j] = solve(R); M[1+j, 0] = M[0, 1+j]
    R = np.einsum('j,jab->ab', d, M[0, 1:]); M[0, 0] = solve(R)
    return M

# keep handles to the originals for comparisons
ORIG = dict(sig=L.sig, cfun=L.cfun, divdiff=L.divdiff, piece_A=L.piece_A)
def patch():
    L.sig = sig; L.cfun = cfun; L.divdiff = divdiff; L.piece_A = piece_A
def unpatch():
    for k, v in ORIG.items(): setattr(L, k, v)
patch()
