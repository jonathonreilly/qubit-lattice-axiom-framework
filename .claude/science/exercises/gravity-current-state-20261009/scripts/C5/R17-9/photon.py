"""R17-9: one-loop graviton-cone shift Xi for a free lattice photon (and, by the same pipeline, a real scalar), q || z.

Photon law (stated): generalized forward difference D_j(k) = i sigma(k_j) e^{i k_j/2}, sigma(k) = sgn(k) d(|k|), d even,
  smooth, periodic, d = |k| in the box, d' in [0,1] (R16-10's subclass C_sub: whole-zone v_max <= 1).  omega^2 = sum_j d(k_j)^2.
  Rotated frame A~_j = e^{-i k_j/2} A_j: continuum Maxwell with momentum vector sigma(k) (antiperiodic; amplitudes invariant).
TT vertex (stipulated): canonical Maxwell stress T_ij = Ebar_i Ebar_j + Bbar_i Bbar_j of SITE-AVERAGED fields
  Ebar_j = a(k_j) E_j, Bbar_x = a(k_y) a(k_z) B_x, ..., averaging symbol a(k) = e^{-ik/2} c(k).
  VU (main): c = d'(|k|)  [= cos(k/2) for the NN photon, i.e. plain nearest-link averaging; c = 1 in the box, c(pi) = 0 -> local].
  (c = 1, no averaging, is a half-shift kernel ~ 1/r: non-local, the photon analogue of Lemma M; not used.)
Pair amplitude for photons (k1,l1),(k2,l2), from canonical quantization (both terms with the same sign):
  amp = -(1/2)[ sqrt(w1 w2) e(C1 eps1, C2 eps2) + e(Ct1 X1 eps1, Ct2 X2 eps2)/sqrt(w1 w2) ],  X v = sigma x v,
  sum_{l1 l2} |amp|^2 = tr(P1 N P2 N^T),  N = (1/2)[sqrt(w1w2) C1 e C2 + X1^T Ct1 e Ct2 X2/sqrt(w1w2)],  P = 1 - s s^T/w^2.
Same convention as the real scalar (R9-9): amp_s = e_ij tau_ij/(2 sqrt(e1 e2)), Pi = -< sum|amp|^2 E/(E^2 - w^2) > + seagull.
Xi = d_{q^2} Pi(0,q) + d_{w^2} Pi(w,0); beta = -<sum|amp|^2/E^3>, alpha by exact grid shifts q = 2 pi n/N + Richardson.
Continuum check (q=0, sigma=k, c=1): N reduces to (w/2)[e(eps1,eps2) - e(k^ x eps1, k^ x eps2)] = helicity-2 projection."""
import numpy as np
from sublum import sstep

def kgrid(N):
    return (np.arange(N) + 0.5)*2*np.pi/N - np.pi

class PhotonProfile:
    """d'(a) on [0, pi] given as a function; d = int d'.  sigma(k) = sgn(k) d(|k|) (odd), c(k) = d'(|k|) (even)."""
    def __init__(self, dprime, name, nf=400001):
        a = np.linspace(0, np.pi, nf); dp = dprime(a)
        self.a, self.dp = a, dp
        self.dt = np.concatenate([[0.0], np.cumsum(0.5*(dp[1:] + dp[:-1])*(a[1]-a[0]))])
        self.name = name; self.dpi = self.dt[-1]
        self.maxdp, self.mindp = dp.max(), dp.min()
    def d(self, k): return np.interp(np.abs(k), self.a, self.dt)
    def dpr(self, k): return np.interp(np.abs(k), self.a, self.dp)
    def sig(self, k): return np.sign(k)*self.d(k)
    def c(self, k): return self.dpr(k)
    def samples(self, n):   # for zz.mu_E: g = d^2, f = (g/2)' = sigma sigma'
        kk = kgrid(n); s = self.sig(kk); return s*s, s*self.dpr(kk)

def photonG(b):            # R14-1's G(b) symbol used as photon: d' = 1 - sstep((a-b)/(pi-b))
    return PhotonProfile(lambda a: 1 - sstep((a - b)/(np.pi - b)), 'gammaG(%.4f)' % b)
def photonGw(b, w):        # R14-3's G_w(b, w): d' = 1 - sstep((a-b)/w), flat zero after b+w
    return PhotonProfile(lambda a: 1 - sstep((a - b)/w), 'gammaGw(%.4f,%.4f)' % (b, w))
def photonNN():
    return PhotonProfile(lambda a: np.cos(a/2), 'gammaNN')

def crossmat(s):           # s: (..., 3) -> (..., 3, 3) with X v = s x v
    X = np.zeros(s.shape[:-1] + (3, 3))
    X[..., 0, 1] = -s[..., 2]; X[..., 0, 2] = s[..., 1]
    X[..., 1, 0] = s[..., 2];  X[..., 1, 2] = -s[..., 0]
    X[..., 2, 0] = -s[..., 1]; X[..., 2, 1] = s[..., 0]
    return X

EPOL = {'T2g': np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], float), 'Eg': np.diag([1.0, -1.0, 0.0])}

def photon_W(law, N, n, pol, cmode='VU'):
    """returns arrays over the grid: W = sum|amp|^2, E = w1 + w2, for the pair (k, q-k), q = 2 pi n/N along z."""
    k = kgrid(N); s = law.sig(k); c = law.c(k)
    j = np.arange(N); j2 = (n - j - 1) % N; jm = (N - 1 - j)
    q = 2*np.pi*n/N
    cE1 = law.c(k - q/2)      # E1 variant: z form factor at the relative momentum K_z = k_z - q/2, same on both legs
    e = EPOL[pol]
    out_W = np.empty((N, N, N)); out_E = np.empty((N, N, N))
    Y, Z = np.meshgrid(j, j, indexing='ij')
    for ix in range(N):
        X_ = np.full_like(Y, ix)
        s1 = np.stack([s[X_], s[Y], s[Z]], -1)
        s2 = np.stack([s[jm[X_]], s[jm[Y]], s[j2[Z]]], -1)
        if cmode == 'VU':
            c1 = np.stack([c[X_], c[Y], c[Z]], -1); c2 = np.stack([c[X_], c[Y], c[j2[Z]]], -1)
        elif cmode == 'E1':
            c1 = np.stack([c[X_], c[Y], cE1[Z]], -1); c2 = c1
        else:
            raise ValueError(cmode)
        ct1 = np.stack([c1[..., 1]*c1[..., 2], c1[..., 0]*c1[..., 2], c1[..., 0]*c1[..., 1]], -1)
        ct2 = np.stack([c2[..., 1]*c2[..., 2], c2[..., 0]*c2[..., 2], c2[..., 0]*c2[..., 1]], -1)
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2)
        Ae = rw[..., None, None]*c1[..., :, None]*e[None, None]*c2[..., None, :]
        X1 = crossmat(s1); X2 = crossmat(s2)
        Mid = ct1[..., :, None]*e[None, None]*ct2[..., None, :]
        Bp = np.einsum('...ji,...jk,...kl->...il', X1, Mid, X2)/rw[..., None, None]
        Nm = 0.5*(Ae + Bp)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        out_W[ix] = np.einsum('...ij,...jk,...kl,...il->...', P1, Nm, P2, Nm)
        out_E[ix] = w1 + w2
    return out_W, out_E

def photon_xi(law, N, pol, shifts=(1, 2), cmode='VU'):
    W0, E0 = photon_W(law, N, 0, pol, cmode)
    beta = -np.mean(W0/E0**3); Pi0 = -np.mean(W0/E0)
    D = {}
    for n in shifts:
        W, E = photon_W(law, N, n, pol, cmode); D[n] = -np.mean(W/E) - Pi0
    q1 = 2*np.pi*shifts[0]/N; r = shifts[1]/shifts[0]
    alpha = (r**4*D[shifts[0]] - D[shifts[1]])/((r**4 - r**2)*q1**2)
    return alpha + beta, alpha, beta

def scalar_xi_grid(gfun, N, pol, m, shifts=(1, 2)):
    """same pipeline for a real scalar with U vertex: |V|^2 = 4 f_x^2 f_y^2 (T2g), (f_x^2 - f_y^2)^2 (Eg); eps^2 = m^2 + sum g."""
    k = kgrid(N); g, f = gfun(k)
    j = np.arange(N)
    fx, fy = f[:, None], f[None, :]
    V2 = 4*fx**2*fy**2 if pol == 'T2g' else (fx**2 - fy**2)**2
    gxy = g[:, None] + g[None, :]
    def Pi(n):
        j2 = (n - j - 1) % N
        e1 = np.sqrt(m*m + gxy[:, :, None] + g[None, None, :]); e2 = np.sqrt(m*m + gxy[:, :, None] + g[j2][None, None, :])
        A2 = V2[:, :, None]/(4*e1*e2); E = e1 + e2
        return -np.mean(A2/E), -np.mean(A2/E**3)
    Pi0, beta = Pi(0)
    D = {n: Pi(n)[0] - Pi0 for n in shifts}
    q1 = 2*np.pi*shifts[0]/N; r = shifts[1]/shifts[0]
    alpha = (r**4*D[shifts[0]] - D[shifts[1]])/((r**4 - r**2)*q1**2)
    return alpha + beta, alpha, beta

def continuum_check(nsamp=2000, seed=1):
    """q = 0, sigma = k, c = 1: tr(P N P N^T) vs the helicity-2 formula (w^2/4)*2*[(e11-e22)^2 + 4 e12^2]_perp."""
    rng = np.random.default_rng(seed); worst = 0.0
    for _ in range(nsamp):
        kv = rng.normal(size=3); w = np.linalg.norm(kv); kh = kv/w
        for pol, e in EPOL.items():
            X1 = crossmat(kv); X2 = crossmat(-kv)
            Nm = 0.5*(w*e + X1.T @ e @ X2/w)
            P = np.eye(3) - np.outer(kh, kh)
            Wv = np.trace(P @ Nm @ P @ Nm.T)
            a = np.cross(kh, [0.3, 0.7, 0.2]); a /= np.linalg.norm(a); bb = np.cross(kh, a)
            e11, e22, e12 = a @ e @ a, bb @ e @ bb, a @ e @ bb
            ref = (w*w/4)*2*((e11 - e22)**2 + 4*e12**2)
            worst = max(worst, abs(Wv - ref)/max(ref, 1e-12))
    return worst

def photon_W_VM(law, N, n, pol):
    """VM (second local vertex, minimal placement): E_i E_j at the site with E_x averaged along x, E_y along y (T2g; c_x c_y),
    E_x^2, E_y^2 on their own links (Eg; no averaging); B_x averaged along y and B_y along x so the T2g B-product sits at the
    z-link midpoint, B_x^2, B_y^2 at their own plaquette centres (Eg) -- every B-product sits at z + 1/2, so it carries the
    relative phase exp(i(k1z + k2z)/2) (representatives; this keeps the amplitude periodic, hence local)."""
    k = kgrid(N); s = law.sig(k); c = law.c(k)
    j = np.arange(N); j2 = (n - j - 1) % N; jm = (N - 1 - j)
    e = EPOL[pol]
    out_W = np.empty((N, N, N)); out_E = np.empty((N, N, N))
    Y, Z = np.meshgrid(j, j, indexing='ij')
    for ix in range(N):
        X_ = np.full_like(Y, ix)
        s1 = np.stack([s[X_], s[Y], s[Z]], -1); s2 = np.stack([s[jm[X_]], s[jm[Y]], s[j2[Z]]], -1)
        one = np.ones_like(s1[..., 0])
        if pol == 'T2g':
            cE = np.stack([c[X_], c[Y], one], -1); cB = np.stack([c[Y], c[X_], one], -1)
        else:
            cE = np.stack([one, one, one], -1); cB = cE
        ph = np.exp(0.5j*(k[Z] + k[j2[Z]]))
        w1 = np.sqrt((s1*s1).sum(-1)); w2 = np.sqrt((s2*s2).sum(-1)); rw = np.sqrt(w1*w2)
        Ae = rw[..., None, None]*cE[..., :, None]*e*cE[..., None, :]
        Mid = cB[..., :, None]*e*cB[..., None, :]
        Bp = np.einsum('...ji,...jk,...kl->...il', crossmat(s1), Mid, crossmat(s2))/rw[..., None, None]
        Nm = 0.5*(Ae + ph[..., None, None]*Bp)
        P1 = np.eye(3) - s1[..., :, None]*s1[..., None, :]/(w1*w1)[..., None, None]
        P2 = np.eye(3) - s2[..., :, None]*s2[..., None, :]/(w2*w2)[..., None, None]
        out_W[ix] = np.real(np.einsum('...ij,...jk,...kl,...il->...', P1, Nm, P2, np.conj(Nm)))
        out_E[ix] = w1 + w2
    return out_W, out_E

def photon_xi_VM(law, N, pol, shifts=(1, 2)):
    W0, E0 = photon_W_VM(law, N, 0, pol)
    beta = -np.mean(W0/E0**3); Pi0 = -np.mean(W0/E0)
    D = {n: -np.mean(np.divide(*photon_W_VM(law, N, n, pol))) - Pi0 for n in shifts}
    q1 = 2*np.pi*shifts[0]/N; r = shifts[1]/shifts[0]
    alpha = (r**4*D[shifts[0]] - D[shifts[1]])/((r**4 - r**2)*q1**2)
    return alpha + beta, alpha, beta
