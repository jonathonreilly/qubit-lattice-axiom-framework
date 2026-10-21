"""BLEAK-1 core: Feynman rules for R19-33's scalar realization on Euclidean Z^4 (a = 1).

Conventions (half-shift Fourier, K7a placement): every object at position x + o is transformed with
exp(-i k.(x+o)), so lattice differences become i*shat(k), shat = 2 sin(k/2), and all vertex symbols are real.

Stress (C4_K2_report.md:61-65; R19-33 r1933_cd_static_cov.py:76-91):
  off-diagonal mu != nu (face centre):  T_mn = 1/4 (D_m phi(x) + D_m phi(x+e_n)) (D_n phi(x) + D_n phi(x+e_m))
  diagonal (site z): T_mm = 1/2 D_m phi(z) D_m phi(z-e_m) - 1/4 sum_{r != m}[(D_r phi(z))^2 + (D_r phi(z-e_r))^2] - 1/2 m^2 phi^2
  D2 (R19-33 sec. 2.2): T_44 -> T_44 + 1/4 (nabla_4^2 phi(z))^2       [dimension 6]
Bilinear vertex: T_A(k) = int_p V_A(p, k-p) phi(p) phi(k-p), V symmetric in its two momenta.

Kernels on symmetric 4x4 sources J at momentum k (index 3 = Euclidean time):
  D_GR  = (J':J - 1/2 trJ' trJ)/shat^2                                  (covariant, W(B4); K7a / de Donder)
  D_fol = J'^TT:J^TT/shat^2 + [1/2 r'r - 1/2(r'A + A'r) + 2 P'p.Pp + 1/2 P'L PL]/qhat^2
          r = J_44, A = theta_ij J_ij, P_i = J_i4, Pp = theta P, PL = qhat.P/|qhat|    (R19-33 sec. 4.1, spatial-TT + bridge)
"""
import numpy as np

def shat(k):
    return 2.0 * np.sin(k / 2.0)

def chalf(k):
    return np.cos(k / 2.0)

def vertex(p1, p2, m2=0.0, d2=False):
    """V_mn(p1,p2), shape (4,4,n). p1, p2: (4,n)."""
    s1, s2, c1, c2 = shat(p1), shat(p2), chalf(p1), chalf(p2)
    n = p1.shape[1]
    V = np.zeros((4, 4, n))
    for m in range(4):
        for nn in range(4):
            if m != nn:
                V[m, nn] = -0.5 * (s1[m] * c1[nn] * s2[nn] * c2[m] + s2[m] * c2[nn] * s1[nn] * c1[m])
        d = -0.5 * s1[m] * s2[m] * np.cos((p1[m] - p2[m]) / 2.0)
        for r in range(4):
            if r != m:
                d = d + 0.5 * np.cos((p1[r] + p2[r]) / 2.0) * s1[r] * s2[r]
        V[m, m] = d - 0.5 * m2
    if d2:
        V[3, 3] = V[3, 3] + 0.25 * s1[3] ** 2 * s2[3] ** 2
    return V

def U_alpha(k, alpha):
    """U^alpha_mn(k) = d/dp1_alpha V_mn(p1, k) at p1 = 0, m = 0 (identical for K2 and D2). Shape (4,4,n)."""
    s, c = shat(k), chalf(k)
    n = k.shape[1]
    U = np.zeros((4, 4, n))
    sa = np.sin(k[alpha])
    for m in range(4):
        U[m, m] = sa * (0.5 - (1.0 if m == alpha else 0.0))
        for nn in range(4):
            if m != nn:
                U[m, nn] = -0.5 * ((1.0 if alpha == m else 0.0) * s[nn] * c[m] + (1.0 if alpha == nn else 0.0) * s[m] * c[nn])
    return U

def kernel_parts(Jp, J, k):
    """Return (W_TT, W_inst, W_GR) bilinear forms, each shape (n,). Jp, J: (4,4,n); k: (4,n)."""
    s = shat(k)
    q = s[:3]
    q2 = np.sum(q * q, axis=0)
    S2 = q2 + s[3] ** 2
    th = np.eye(3)[:, :, None] - q[:, None, :] * q[None, :, :] / q2
    def tt_and_A(M):
        Ms = M[:3, :3]
        A = np.einsum('ijn,jin->n', th, Ms)
        TMT = np.einsum('ijn,jkn,kln->iln', th, Ms, th)
        MTT = TMT - 0.5 * th * A
        return MTT, A
    JTTp, Ap = tt_and_A(Jp)
    JTT, A = tt_and_A(J)
    WTT = np.einsum('ijn,ijn->n', JTTp, JTT) / S2
    rp, r = Jp[3, 3], J[3, 3]
    Pp_, P_ = Jp[:3, 3], J[:3, 3]
    Ppp = np.einsum('ijn,jn->in', th, Pp_)
    Pp = np.einsum('ijn,jn->in', th, P_)
    qn = np.sqrt(q2)
    PLp = np.sum(q * Pp_, axis=0) / qn
    PL = np.sum(q * P_, axis=0) / qn
    Winst = (0.5 * rp * r - 0.5 * (rp * A + Ap * r) + 2.0 * np.sum(Ppp * Pp, axis=0) + 0.5 * PLp * PL) / q2
    trp = np.einsum('iin->n', Jp); tr = np.einsum('iin->n', J)
    WGR = (np.einsum('ijn,ijn->n', Jp, J) - 0.5 * trp * tr) / S2
    return WTT, Winst, WGR

def midpoint_axis(M, lo=0.0, hi=np.pi):
    h = (hi - lo) / M
    return lo + (np.arange(M) + 0.5) * h

def iter_chunks(M, chunk=1 << 17, lo=0.0, hi=np.pi):
    """Yield (k (4,n)) chunks of the M^4 midpoint grid on [lo,hi]^4, chunked over (k4, k1..k3)."""
    ax = midpoint_axis(M, lo, hi)
    K1, K2, K3 = np.meshgrid(ax, ax, ax, indexing='ij')
    sp = np.stack([K1.ravel(), K2.ravel(), K3.ravel()])
    nsp = sp.shape[1]
    for k4 in ax:
        for a in range(0, nsp, chunk):
            b = min(nsp, a + chunk)
            k = np.empty((4, b - a))
            k[:3] = sp[:, a:b]
            k[3] = k4
            yield k
