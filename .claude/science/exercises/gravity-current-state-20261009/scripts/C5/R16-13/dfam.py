"""R16-13: Dirac edge family DG(b, w, r) (4-comp Wilson, D1-type) and tensor Gauss-Legendre quadrature evaluators.
s' = 1 - sstep((k-b)/w) - sstep((k-k2)/w) on [0, pi], k2 = pi - b - w   (=> s(pi) = 0, s odd; plateau of length pi-2b-2w)
W' = r sqrt(1 - s'^2) on [0, pi], W even.   Requires b + w <= pi/2.
Lemma V1 (proved here): if |s'| <= 1 and s'^2 + 3 W'^2 <= 1 pointwise, then |grad E| <= 1 on the whole zone.
Evaluators (pointwise forms, any quadrature):
  Xi_F,v = (Nc/8) <|G|^2(|c_z'|^2 - 1)/E^3> - (Nc/32) <|V_v|^2 A_zz/E^5>,  |V_T2g|^2 = 4 S_x^2 S_y^2, |V_Eg|^2 = (S_x^2 - S_y^2)^2
  mu^F = -Nc mu^s[E],  mu_E^s = -(1/8)<(H_xx-H_yy)(p_x^2-p_y^2)/E>,  mu_T2^s = -(1/2)<H_xy p_x p_y/E>."""
import numpy as np
from sublum import sstep, dsstep

class DG:
    def __init__(self, b, w, r, nf=200001, name=None):
        assert b + w <= np.pi/2 + 1e-12
        self.b, self.w, self.r = b, w, r
        self.k2 = np.pi - b - w
        kk = np.linspace(0, np.pi, nf); self.kk = kk
        sp = self._sp(kk)
        wp = r*np.sqrt(np.maximum(0, 1 - sp**2))
        dk = kk[1]-kk[0]
        self.St = np.concatenate([[0.0], np.cumsum(0.5*(sp[1:]+sp[:-1])*dk)])
        self.Wt = np.concatenate([[0.0], np.cumsum(0.5*(wp[1:]+wp[:-1])*dk)])
        self.Spi, self.Wpi = self.St[-1], self.Wt[-1]
        self.name = name or 'DG(b=%.3f,w=%.3f,r=%.3f)' % (b, w, r)
    def _sp(self, a):
        return 1 - sstep((a - self.b)/self.w) - sstep((a - self.k2)/self.w)
    def _spp(self, a):
        return -(dsstep((a - self.b)/self.w) + dsstep((a - self.k2)/self.w))/self.w
    def breaks(self):
        b, w, k2 = self.b, self.w, self.k2
        return sorted(set([0.0, b, b + w, k2, k2 + w, np.pi]))
    # odd/even extensions on [-pi, pi]
    def tables(self, k):
        a = np.abs(k); sg = np.sign(k)
        S = sg*np.interp(a, self.kk, self.St)
        sp = self._sp(a); Sp = sp
        Spp = sg*self._spp(a)
        W = np.interp(a, self.kk, self.Wt)
        wp = self.r*np.sqrt(np.maximum(0, 1 - sp**2)); Wp = sg*wp
        with np.errstate(divide='ignore', invalid='ignore'):
            Wpp = np.where(wp > 1e-300, -self.r**2*sp*self._spp(a)/np.where(wp > 1e-300, wp, 1), 0.0)
        return S, Sp, Spp, W, Wp, Wpp

def gl_nodes(breaks, npan=6, ngl=12):
    """composite GL on [0, pi] with panels refined inside each break interval; mirrored to [-pi, pi]."""
    xg, wg = np.polynomial.legendre.leggauss(ngl)
    ks, ws = [], []
    for a, c in zip(breaks[:-1], breaks[1:]):
        if c - a < 1e-14: continue
        edges = np.linspace(a, c, npan + 1)
        for e0, e1 in zip(edges[:-1], edges[1:]):
            h = 0.5*(e1 - e0); mid = 0.5*(e1 + e0)
            ks.append(mid + h*xg); ws.append(h*wg)
    k = np.concatenate(ks); w = np.concatenate(ws)
    k = np.concatenate([-k[::-1], k]); w = np.concatenate([w[::-1], w])
    return k, w/(2*np.pi)          # weights normalized to zone mean

def evaluate(law, m, npan=6, ngl=12, Nc=4, breaks=None):
    k, wq = gl_nodes(breaks or law.breaks(), npan, ngl)
    S, Sp, Spp, W, Wp, Wpp = law.tables(k)
    n = len(k)
    wx = wq[:, None, None]; wy = wq[None, :, None]; wz = wq[None, None, :]
    Sx, Sy, Sz = S[:, None, None], S[None, :, None], S[None, None, :]
    M = m + W[:, None, None] + W[None, :, None] + W[None, None, :]
    E2 = Sx**2 + Sy**2 + Sz**2 + M**2
    E = np.sqrt(E2)
    wt = wx*wy*wz
    mean = lambda f: float(np.sum(wt*f))
    cp2 = (Sp**2 + Wp**2)[None, None, :]
    Azz = (Sp**2 + S*Spp + Wp**2)[None, None, :] + M*Wpp[None, None, :] - 1
    G2 = 0.25*(Sx**2 + Sy**2)
    out = {}
    aterm = (Nc/8)*mean(G2*(cp2 - 1)/E**3)
    out['a'] = aterm
    for pol, V2 in (('T2g', 4*Sx**2*Sy**2), ('Eg', (Sx**2 - Sy**2)**2)):
        st = -(Nc/32)*mean(V2*Azz/E**5)
        out['s_' + pol] = st
        out[pol] = aterm + st
    px = Sx*Sp[:, None, None] + M*Wp[:, None, None]
    py = Sy*Sp[None, :, None] + M*Wp[None, :, None]
    Hxx = (Sp**2 + S*Spp + Wp**2)[:, None, None] + M*Wpp[:, None, None]
    Hyy = (Sp**2 + S*Spp + Wp**2)[None, :, None] + M*Wpp[None, :, None]
    Hxy = Wp[:, None, None]*Wp[None, :, None]
    out['muE'] = -Nc*(-0.125*mean((Hxx - Hyy)*(px**2 - py**2)/E))
    out['muT2'] = -Nc*(-0.5*mean(Hxy*px*py/E))
    return out

def vmax_sample(law, m, n=81, seed=0):
    """sampled whole-zone max |grad E| (lower bound; Lemma V1 gives the upper bound 1)."""
    k = np.linspace(-np.pi, np.pi, n)
    S, Sp, Spp, W, Wp, Wpp = law.tables(k)
    X, Y, Z = np.meshgrid(np.arange(n), np.arange(n), np.arange(n), indexing='ij')
    M = m + W[X] + W[Y] + W[Z]
    E2 = S[X]**2 + S[Y]**2 + S[Z]**2 + M**2
    g2 = sum((S[I]*Sp[I] + M*Wp[I])**2 for I in (X, Y, Z))
    return float(np.sqrt(np.max(g2/E2)))
