"""R16-13 module: Dirac (and scalar) one-loop graviton-cone shift Xi and strain shear masses on a 3D zone grid.

Dirac band: h(k) = sum_a c_a(k) gamma_a, {gamma_a, gamma_b} = 2 delta_ab, Nc components, E = |c|.
  4-comp Wilson (D1): c = (S_x, S_y, S_z, M), M = m + W_x + W_y + W_z.
  8-comp Clifford-flat (R10-5): c = (S_x, S_y, S_z, W_x, W_y, W_z, m).
TT vertex (stipulated, R10-5's Clifford-index vielbein, extended): Gamma = G . gamma, G independent of k_z (q || z).
  T2g: G = (S_y/2, S_x/2, 0, ...)  [c.G = S_x S_y];  Eg: G = (S_x/2, -S_y/2, 0, ...) [c.G = (S_x^2 - S_y^2)/2].
  Optional Wilson part (variant VW): G_beta = lamW * R_x R_y (T2g) or lamW*(R_x^2 - R_y^2)/2 (Eg), W = R^2/2.
Pair weight: t(k,k') = tr[P+(k') Gamma P-(k) Gamma] = (Nc/4)[|G|^2 (1 + c.c'/(E E')) - 2 (c.G)(c'.G)/(E E')].
Pi_F(w,q) = -< 2 t(k,k+q z) (E+E') / ((E+E')^2 - w^2) > + seagull;  Xi = d_{q^2} Pi + d_{w^2} Pi.
  beta = -< t0/(4E^3) >;  alpha by exact grid shifts q = 2 pi n/N (n=1,2,4) + Richardson (R10-5's method).
Scalar (real, R9-9): Pi_B = -(1/4) <|V|^2/(e e') (e+e')/((e+e')^2-w^2)>, Xi_B = (1/32)<|V|^2 A_zz/e^5>.
Strain (R9-2 universal flow dk/de = h.p/2, p = grad(E^2/2), H = Hess(E^2/2)), per real scalar (eps_vac = eps/2):
  mu_E^s = -(1/8) <(H_xx - H_yy)(p_x^2 - p_y^2)/eps>,   mu_T2^s = -(1/2) <H_xy p_x p_y/eps>.
  Dirac sea (eps_vac = -(Nc/2) E): mu^F = -Nc * mu^s[E].
"""
import numpy as np, sys
sys.path.insert(0, '.')
from sublum import sstep, dsstep, wrap, SymS

def kgrid(N):
    return (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi

class D1:
    """R14-1 D1(b, r): s = R13-4 odd symbol S(b); W' = r sqrt(1 - s'^2) = 2 r sqrt(st(1-st)) on [b, pi-b]."""
    def __init__(self, b, r, zig=None):
        self.b, self.r = b, r
        self.A = SymS(b)
        self.zig = zig
        # fine table for W(k), |k| in [0, pi]
        kk = np.linspace(0, np.pi, 400001)
        wp = self._dWabs(kk)
        self.kk = kk
        self.Wt = np.concatenate([[0.0], np.cumsum(0.5 * (wp[1:] + wp[:-1]) * (kk[1] - kk[0]))])
        self.Wpi = self.Wt[-1]
    def _dWabs(self, a):
        st = sstep((a - self.b) / self.A.w)
        return 2 * self.r * np.sqrt(np.maximum(0, st * (1 - st)))
    def S(self, k): return self.A.s(k)
    def dS(self, k): return self.A.ds(k)
    def d2S(self, k): return self.A.d2s(k)
    def W(self, k):
        a = np.abs(wrap(np.asarray(k, float)))
        return np.interp(a, self.kk, self.Wt)
    def dW(self, k):
        k = wrap(np.asarray(k, float))
        return np.sign(k) * self._dWabs(np.abs(k))
    def d2W(self, k, h=1e-6):
        return (self.dW(k + h) - self.dW(k - h)) / (2 * h)
    def vmax(self, m, n=4001):
        """whole-zone max |grad E| for the 4-comp non-separable band, by dense random+grid search (lower bound) plus line maxima."""
        k = np.linspace(-np.pi, np.pi, n)
        S, Sp, W, Wp = self.S(k), self.dS(k), self.W(k), self.dW(k)
        best = 0.0
        # sample 3D on a coarse grid
        n3 = 121
        k3 = np.linspace(-np.pi, np.pi, n3)
        S3, Sp3, W3, Wp3 = self.S(k3), self.dS(k3), self.W(k3), self.dW(k3)
        X, Y, Z = np.meshgrid(np.arange(n3), np.arange(n3), np.arange(n3), indexing='ij')
        M = m + W3[X] + W3[Y] + W3[Z]
        E2 = S3[X]**2 + S3[Y]**2 + S3[Z]**2 + M**2
        g2 = sum((S3[I] * Sp3[I] + M * Wp3[I])**2 for I in (X, Y, Z))
        best = max(best, float(np.sqrt(np.max(g2 / E2))))
        return best

def dirac_xi(law, m, N, pol='T2g', Nc=4, kind='D1', lamW=0.0, shifts=(1, 2, 4), Rtab=None):
    """Xi_F for one Dirac field (Nc components) with the vielbein TT vertex; 3D midpoint grid N^3."""
    k = kgrid(N)
    S, W = law.S(k), law.W(k)
    X, Y = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
    Sx, Sy = S[X][..., None], S[Y][..., None]
    if pol == 'T2g':
        cG_perp = Sx * Sy
        G2 = 0.25 * (Sx**2 + Sy**2)
    else:
        cG_perp = 0.5 * (Sx**2 - Sy**2)
        G2 = 0.25 * (Sx**2 + Sy**2)
    if kind == 'D1':
        Mperp = m + W[X][..., None] + W[Y][..., None]
        Mz = Mperp + W[None, None, :]
        Sz = S[None, None, :]
        E2 = Sx**2 + Sy**2 + Sz**2 + Mz**2
        if lamW != 0.0:
            R = Rtab
            Rx, Ry = R[X][..., None], R[Y][..., None]
            Gb = lamW * (Rx * Ry if pol == 'T2g' else 0.5 * (Rx**2 - Ry**2))
            G2 = G2 + Gb**2
        else:
            Gb = 0.0
    else:  # 8-comp Clifford-flat: c = (S, W per direction, m)
        Ep2 = m * m + Sx**2 + Sy**2 + W[X][..., None]**2 + W[Y][..., None]**2
        Sz = S[None, None, :]; Wz = W[None, None, :]
        E2 = Ep2 + Sz**2 + Wz**2
        Gb = 0.0
    E = np.sqrt(E2)
    def chi(n):
        if n == 0:
            Ez = E;
            if kind == 'D1':
                cc = E2; cGp = cG_perp + (Gb * Mz if lamW != 0 else 0.0); cGq = cGp
            else:
                cc = E2; cGp = cG_perp; cGq = cGp
        else:
            if kind == 'D1':
                Sz2 = np.roll(Sz, -n, axis=2); Mz2 = np.roll(Mz, -n, axis=2)
                E2b = Sx**2 + Sy**2 + Sz2**2 + Mz2**2
                cc = Sx**2 + Sy**2 + Sz * Sz2 + Mz * Mz2
                cGp = cG_perp + (Gb * Mz if lamW != 0 else 0.0)
                cGq = cG_perp + (Gb * Mz2 if lamW != 0 else 0.0)
            else:
                Sz2 = np.roll(Sz, -n, axis=2); Wz2 = np.roll(Wz, -n, axis=2)
                E2b = Ep2 + Sz2**2 + Wz2**2
                cc = Ep2 + Sz * Sz2 + Wz * Wz2
                cGp = cG_perp; cGq = cG_perp
            Ez = np.sqrt(E2b)
        t = (Nc / 4.0) * (G2 * (1 + cc / (E * Ez)) - 2 * cGp * cGq / (E * Ez))
        return float(np.mean(2 * t / (E + Ez)))
    c0 = chi(0)
    d = []
    for n in shifts:
        q = 2 * np.pi * n / N
        d.append(-(chi(n) - c0) / q**2)
    r1 = (4 * d[0] - d[1]) / 3; r2 = (4 * d[1] - d[2]) / 3
    alpha = (16 * r1 - r2) / 15
    cG0 = cG_perp + (Gb * Mz if (kind == 'D1' and lamW != 0) else 0.0)
    t0 = (Nc / 4.0) * (2 * G2 - 2 * cG0**2 / E2)
    beta = -float(np.mean(t0 / (4 * E**3)))
    return dict(alpha=alpha, beta=beta, Xi=alpha + beta, raw=d[0] + beta)

def strain_mu(law, m, N, kind='D1'):
    """per-real-scalar-form mu_E^s, mu_T2^s for dispersion E (4-comp D1 non-separable or separable)."""
    k = kgrid(N)
    S, Sp, Spp = law.S(k), law.dS(k), law.d2S(k)
    W, Wp, Wpp = law.W(k), law.dW(k), law.d2W(k)
    I = np.arange(N)
    X, Y, Z = np.meshgrid(I, I, I, indexing='ij')
    if kind == 'D1':
        M = m + W[X] + W[Y] + W[Z]
        E2 = S[X]**2 + S[Y]**2 + S[Z]**2 + M**2
        px = S[X] * Sp[X] + M * Wp[X]; py = S[Y] * Sp[Y] + M * Wp[Y]
        Hxx = Sp[X]**2 + S[X] * Spp[X] + Wp[X]**2 + M * Wpp[X]
        Hyy = Sp[Y]**2 + S[Y] * Spp[Y] + Wp[Y]**2 + M * Wpp[Y]
        Hxy = Wp[X] * Wp[Y]
    else:
        E2 = m * m + S[X]**2 + S[Y]**2 + S[Z]**2 + W[X]**2 + W[Y]**2 + W[Z]**2
        px = S[X] * Sp[X] + W[X] * Wp[X]; py = S[Y] * Sp[Y] + W[Y] * Wp[Y]
        Hxx = Sp[X]**2 + S[X] * Spp[X] + Wp[X]**2 + W[X] * Wpp[X]
        Hyy = Sp[Y]**2 + S[Y] * Spp[Y] + Wp[Y]**2 + W[Y] * Wpp[Y]
        Hxy = 0.0 * E2
    E = np.sqrt(E2)
    muE = -0.125 * float(np.mean((Hxx - Hyy) * (px**2 - py**2) / E))
    muT = -0.5 * float(np.mean(Hxy * px * py / E))
    return muE, muT

class Fn:
    """simple law from analytic callables S, dS, d2S, W, dW, d2W."""
    def __init__(self, S, dS, d2S, W, dW, d2W):
        self.S, self.dS, self.d2S, self.W, self.dW, self.d2W = S, dS, d2S, W, dW, d2W
