"""R16-13: Dirac zigzag hybrid DZ(b, l, nz, wt, r): 4-comp Wilson D1-type, s odd, s(pi) = 0.
s' = 1 on [0, b]; nz (even) zigzag segments of length l with values -1, +1, ... (sharp C^inf turns of width wt);
then R13-4's step 1 -> -1 over the middle [k0, pi - b] (k0 = b + nz l); s' = -1 on [pi - b, pi] (mirror box).
W' = r sqrt(1 - s'^2) (Lemma V1: r <= 1/sqrt3 => whole-zone v_max <= 1)."""
import numpy as np
from sublum import sstep, dsstep
class DZ:
    def __init__(self, b, l, nz, wt, r, nf=200001):
        self.b, self.l, self.nz, self.wt, self.r = b, l, nz, wt, r
        self.k0 = b + nz*l; self.Lm = np.pi - b - self.k0
        assert self.Lm > 2*wt and nz % 2 == 0
        kk = np.linspace(0, np.pi, nf); self.kk = kk
        sp = self._sp(kk); wp = r*np.sqrt(np.maximum(0, 1 - sp**2)); dk = kk[1]-kk[0]
        self.St = np.concatenate([[0.0], np.cumsum(0.5*(sp[1:]+sp[:-1])*dk)])
        self.Wt = np.concatenate([[0.0], np.cumsum(0.5*(wp[1:]+wp[:-1])*dk)])
        self.Spi, self.Wpi = self.St[-1], self.Wt[-1]
    def _turns(self):
        # breakpoints of the zigzag: b, b+l, ..., b+nz*l ; values before/after
        pts = [self.b + j*self.l for j in range(self.nz + 1)]
        vals = [1.0] + [(-1.0 if j % 2 == 0 else 1.0) for j in range(self.nz)] + [1.0]
        return pts, vals
    def _sp(self, a):
        pts, vals = self._turns(); wt = self.wt
        sp = np.full_like(a, 1.0)
        for j, p in enumerate(pts):
            sp = sp + (vals[j+1] - vals[j])*sstep((a - p + wt/2)/wt)
        # middle step 1 -> -1 on [k0, pi - b]
        sp = sp - 2*sstep((a - self.k0)/self.Lm)*(a >= self.k0) if False else sp - 2*sstep((a - self.k0)/self.Lm)
        return sp
    def _spp(self, a):
        pts, vals = self._turns(); wt = self.wt
        d = np.zeros_like(a)
        for j, p in enumerate(pts):
            d = d + (vals[j+1] - vals[j])*dsstep((a - p + wt/2)/wt)/wt
        return d - 2*dsstep((a - self.k0)/self.Lm)/self.Lm
    def breaks(self):
        pts, _ = self._turns(); br = [0.0]
        for p in pts: br += [p - self.wt/2, p + self.wt/2]
        br += [np.pi - self.b, np.pi]
        return sorted(set([x for x in br if 0 <= x <= np.pi]))
    def tables(self, k):
        a = np.abs(k); sg = np.sign(k)
        S = sg*np.interp(a, self.kk, self.St); Sp = self._sp(a); Spp = sg*self._spp(a)
        W = np.interp(a, self.kk, self.Wt); wp = self.r*np.sqrt(np.maximum(0, 1 - Sp**2)); Wp = sg*wp
        with np.errstate(divide='ignore', invalid='ignore'):
            Wpp = np.where(wp > 1e-300, -self.r**2*Sp*self._spp(a)/np.where(wp > 1e-300, wp, 1), 0.0)
        return S, Sp, Spp, W, Wp, Wpp
