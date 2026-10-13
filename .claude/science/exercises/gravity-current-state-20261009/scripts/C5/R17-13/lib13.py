"""R17-13: independent evaluator of the Wilson-Dirac T2g strain shear mass mu_T2^F (SF flow, V0 irrelevant here).

Band (4-comp Wilson): E^2 = sum_j s(k_j)^2 + M^2, M = m + sum_j W(k_j); p_j = d_j(E^2/2) = s_j s'_j + M W'_j; H_xy = W'_x W'_y.
SF (R16-13, C5_R16-13_report.md:90-97): mu_T2^s[E] = -(1/2)<H_xy p_x p_y / E>, Dirac sea mu^F = -Nc mu^s[E]  =>
    mu_T2^F = (Nc/2) < q_x q_y / E >,   q_j := W'_j p_j = W'_j s_j s'_j + M W'_j^2          (form P)
IBP (this probe):  mu_T2^F = (Nc/6) < E^3 W''_x W''_y > - (Nc/2) < E W'_x^2 W'_y^2 >      (form I)
<.> = zone mean.  Both are evaluated on the positive octant (integrands even in each k_j) by composite Gauss-Legendre.

D1(b, r) (R14-1; as coded in R16-13 dirac.D1 / R16-1 r161_laws): on [0, pi], w = pi - 2b, x = (k-b)/w,
    s' = 1 on [0,b], 1 - 2 sstep(x) on [b, pi-b], -1 on [pi-b, pi];  W' = r sqrt(1 - s'^2) = 2 r sqrt(st (1-st)), st = sstep(x).
Independent construction here: s, W by per-node Gauss-Legendre integration of s', W' (no tables, no splines).
"""
import numpy as np

def sstep(x):
    x = np.clip(np.asarray(x, float), 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def dsstep(x):
    x = np.clip(np.asarray(x, float), 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
        d1 = np.where(x > 0, e1/np.where(x > 0, x, 1)**2, 0.0)
        d2 = np.where(x < 1, e2/np.where(x < 1, 1-x, 1)**2, 0.0)
    return (d1*e2 + e1*d2)/(e1+e2)**2

_XG, _WG = np.polynomial.legendre.leggauss(80)

def _cumint(fun, x, npan=4):
    """int_0^x fun(t) dt for each x in [0,1] (vectorized), composite GL npan x 80."""
    x = np.asarray(x, float); out = np.zeros_like(x)
    for p in range(npan):
        a = x*p/npan; c = x*(p+1)/npan; h = 0.5*(c-a); mid = 0.5*(c+a)
        t = mid[..., None] + h[..., None]*_XG
        out += (fun(t)*_WG).sum(-1)*h
    return out

class D1law:
    def __init__(self, b, r):
        assert 0 < b < np.pi/2
        self.b, self.r, self.w = b, r, np.pi - 2*b
        self.Wpi = 2*r*self.w*_cumint(lambda t: np.sqrt(np.maximum(sstep(t)*(1-sstep(t)), 0)), np.array([1.0]))[0]
    def tab(self, k):
        """k in [0, pi]: returns s, s', W, W', W''."""
        k = np.asarray(k, float); b, w, r = self.b, self.w, self.r
        x = np.clip((k - b)/w, 0, 1)
        st = sstep(x)
        sp = np.where(k <= b, 1.0, np.where(k >= np.pi - b, -1.0, 1 - 2*st))
        # s = k - 2 w Phi(x) on the slab, Phi = int_0^x sstep;  mirror: s = pi - k beyond pi-b
        Phi = _cumint(sstep, x)
        s = np.where(k <= b, k, np.where(k >= np.pi - b, np.pi - k, k - 2*w*Phi))
        root = np.sqrt(np.maximum(st*(1-st), 0))
        Wp = 2*r*root
        W = 2*r*w*_cumint(lambda t: np.sqrt(np.maximum(sstep(t)*(1-sstep(t)), 0)), x)
        with np.errstate(divide='ignore', invalid='ignore'):
            Wpp = np.where(root > 1e-300, r*(1-2*st)*dsstep(x)/(w*np.where(root > 1e-300, root, 1)), 0.0)
        return s, sp, W, Wp, Wpp

def gl_panels(breaks, npan, ngl):
    xg, wg = np.polynomial.legendre.leggauss(ngl); ks, ws = [], []
    for a, c in zip(breaks[:-1], breaks[1:]):
        if c - a < 1e-14: continue
        e = np.linspace(a, c, npan+1)
        for e0, e1 in zip(e[:-1], e[1:]):
            h = 0.5*(e1-e0); ks.append(0.5*(e0+e1) + h*xg); ws.append(h*wg)
    return np.concatenate(ks), np.concatenate(ws)

def muT2(law, m, npan=6, ngl=16, Nc=4, form='P', zchunk=None):
    """mu_T2^F per Nc-component Dirac field.  x,y nodes on the slab only (q_j = 0 elsewhere for D1); z on [0, pi]."""
    b = law.b
    kx, wx = gl_panels(getattr(law, 'bxy', [b, np.pi - b]), 2*npan, ngl)
    kz, wz = gl_panels(getattr(law, 'bz', [0.0, b, np.pi - b, np.pi]), npan, ngl)
    sx, spx, Wx, Wpx, Wppx = law.tab(kx)
    sz, spz, Wz, Wpz, Wppz = law.tab(kz)
    tot = 0.0
    Mxy = m + Wx[:, None] + Wx[None, :]
    S2xy = sx[:, None]**2 + sx[None, :]**2
    wxy = wx[:, None]*wx[None, :]
    for iz in range(len(kz)):
        M = Mxy + Wz[iz]; E = np.sqrt(S2xy + sz[iz]**2 + M**2)
        if form == 'P':
            qx = Wpx[:, None]*(sx[:, None]*spx[:, None] + M*Wpx[:, None])
            qy = Wpx[None, :]*(sx[None, :]*spx[None, :] + M*Wpx[None, :])
            val = (Nc/2)*qx*qy/E
        else:
            val = (Nc/6)*E**3*Wppx[:, None]*Wppx[None, :] - (Nc/2)*E*Wpx[:, None]**2*Wpx[None, :]**2
        tot += wz[iz]*np.sum(wxy*val)
    return tot/np.pi**3

def muT2_parts(law, m, npan=6, ngl=16, Nc=4):
    """split mu_T2^F = KK + KM + MM: q = W' s s' (kinetic, K) + M W'^2 (mass, M)."""
    b = law.b
    kx, wx = gl_panels(getattr(law, 'bxy', [b, np.pi - b]), 2*npan, ngl)
    kz, wz = gl_panels(getattr(law, 'bz', [0.0, b, np.pi - b, np.pi]), npan, ngl)
    sx, spx, Wx, Wpx, _ = law.tab(kx); sz, _, Wz, _, _ = law.tab(kz)
    Mxy = m + Wx[:, None] + Wx[None, :]; S2xy = sx[:, None]**2 + sx[None, :]**2; wxy = wx[:, None]*wx[None, :]
    kx_ = Wpx*sx*spx; out = np.zeros(3)
    for iz in range(len(kz)):
        M = Mxy + Wz[iz]; E = np.sqrt(S2xy + sz[iz]**2 + M**2)
        Kx, Ky = kx_[:, None], kx_[None, :]; Mx, My = M*Wpx[:, None]**2, M*Wpx[None, :]**2
        out += wz[iz]*np.array([np.sum(wxy*Kx*Ky/E), np.sum(wxy*(Kx*My + Mx*Ky)/E), np.sum(wxy*Mx*My/E)])
    return (Nc/2)*out/np.pi**3

class DGlaw:
    """R16-13's DG(b, w, r): s' = 1 - sstep((k-b)/w) - sstep((k-k2)/w), k2 = pi-b-w (flat s'=0 plateau), W' = r sqrt(1-s'^2).
    Independent construction (per-node GL integration).  Mirror-symmetric: s(pi-k) = s(k), W'(pi-k) = W'(k)."""
    def __init__(self, b, w, r):
        assert b + w <= np.pi/2 + 1e-12
        self.b, self.w, self.r, self.k2 = b, w, r, np.pi - b - w
        self.bxy = sorted(set([b, b + w, self.k2, np.pi - b])); self.bz = sorted(set([0.0] + self.bxy + [np.pi]))
        self.Wpi = self._W(np.array([np.pi]))[0]
    def _sp(self, t):
        return 1 - sstep((t - self.b)/self.w) - sstep((t - self.k2)/self.w)
    def _W(self, k):
        f = lambda t: self.r*np.sqrt(np.maximum(0, 1 - self._sp(t)**2))
        return _seg_int(f, k, [0.0] + self.bxy + [np.pi])
    def tab(self, k):
        k = np.asarray(k, float); sp = self._sp(k)
        s = _seg_int(self._sp, k, [0.0] + self.bxy + [np.pi])
        Wp = self.r*np.sqrt(np.maximum(0, 1 - sp**2))
        W = self._W(k)
        spp = -(dsstep((k - self.b)/self.w) + dsstep((k - self.k2)/self.w))/self.w
        with np.errstate(divide='ignore', invalid='ignore'):
            Wpp = np.where(Wp > 1e-300, -self.r**2*sp*spp/np.where(Wp > 1e-300, Wp, 1), 0.0)
        return s, sp, W, Wp, Wpp

def _seg_int(fun, k, pts, n=4):
    """int_0^k fun for k in [0, pi], composite GL on each segment of pts (n panels x 80 nodes per segment)."""
    k = np.asarray(k, float); out = np.zeros_like(k)
    for a, c in zip(pts[:-1], pts[1:]):
        hi = np.clip(k, a, c)
        L = hi - a
        for p in range(n):
            e0 = a + L*p/n; e1 = a + L*(p+1)/n; h = 0.5*(e1-e0); mid = 0.5*(e1+e0)
            t = mid[..., None] + h[..., None]*_XG
            out += (fun(t)*_WG).sum(-1)*h
    return out

def dirac_rows(law, m, npan=3, ngl=8, Nc=4):
    """Independent low-memory evaluator of the Dirac rows per 4-comp field (V0 vertex, SF flow), positive octant, z-loop:
    Xi_v = (Nc/8)<|G|^2(|c_z'|^2-1)/E^3> - (Nc/32)<|V_v|^2 A_zz/E^5>  (R16-13 Theorem DT, A-form; vR16-13 item 1),
    |G|^2 = (s_x^2+s_y^2)/4, |V_T2g|^2 = 4 s_x^2 s_y^2, |V_Eg|^2 = (s_x^2-s_y^2)^2, A_zz = s'^2 + s s'' + W'^2 + M W'' - 1 (z);
    mu_E^F = (Nc/8)<(H_xx-H_yy)(p_x^2-p_y^2)/E>,  mu_T2^F = (Nc/2)<W'_x W'_y p_x p_y/E>."""
    br = getattr(law, 'bz', [0.0, law.b, np.pi - law.b, np.pi])
    k, wq = gl_panels(br, npan, ngl)
    s, sp, W, Wp, Wpp = law.tab(k)
    h = 1e-5
    spp = (law.tab(k + h)[1] - law.tab(k - h)[1])/(2*h)
    Sx, Sy = s[:, None], s[None, :]; wxy = wq[:, None]*wq[None, :]
    G2 = 0.25*(Sx**2 + Sy**2); V2T = 4*Sx**2*Sy**2; V2E = (Sx**2 - Sy**2)**2
    Mxy = m + W[:, None] + W[None, :]; S2 = Sx**2 + Sy**2
    acc = np.zeros(5)
    Hx0 = sp**2 + s*spp + Wp**2
    for iz in range(len(k)):
        M = Mxy + W[iz]; E2 = S2 + s[iz]**2 + M**2; E = np.sqrt(E2)
        cz2 = sp[iz]**2 + Wp[iz]**2
        Azz = sp[iz]**2 + s[iz]*spp[iz] + Wp[iz]**2 + M*Wpp[iz] - 1
        a = np.sum(wxy*G2*(cz2 - 1)/E**3)
        tT = np.sum(wxy*V2T*Azz/E**5); tE = np.sum(wxy*V2E*Azz/E**5)
        px = Sx*sp[:, None] + M*Wp[:, None]; py = Sy*sp[None, :] + M*Wp[None, :]
        Hxx = Hx0[:, None] + M*Wpp[:, None]; Hyy = Hx0[None, :] + M*Wpp[None, :]
        muE = np.sum(wxy*(Hxx - Hyy)*(px**2 - py**2)/E)
        muT = np.sum(wxy*Wp[:, None]*Wp[None, :]*px*py/E)
        acc += wq[iz]*np.array([a, tT, tE, muE, muT])
    acc /= np.pi**3
    a, tT, tE, muE, muT = acc
    return np.array([(Nc/8)*a - (Nc/32)*tT, (Nc/8)*a - (Nc/32)*tE, (Nc/8)*muE, (Nc/2)*muT])
