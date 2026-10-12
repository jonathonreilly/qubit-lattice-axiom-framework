"""P1 (lane RP, C4): exact mu_E(m) per species from the V3 Jacobian formula, and its small-(ma) expansion.

Normalisation (one for all species): RN-L1.  E-channel flow velocity v = (1/2) hhat f(k), hhat = diag(1,-1,0),
f = the species' local momentum symbol with unit slope at the physical zero.  mu_E = d^2/deps^2 of the vacuum
energy per lattice site (cell a^3), lattice units.  Jacobian formula (V3, refereed):
   E_vac(eps) = < J_eps(k) e_vac(k) >_BZ ,  J''(0) = div(v div v)  =>  mu_E = -< grad(e_vac) . v  div v >_BZ .

Species (proved below in the report, checked here):
  KG scalar, f = sin k, e_vac = +omega/2, omega^2 = M^2 + sum 4 sin^2(k/2):
        F(M) = (1/8) < (cos kx - cos ky)^2 (cos kx + cos ky) / omega >
  staggered fermion (V3 symbol 1/2 sin 2p, sea -omega_s/2):  -1/2 F(2m)
  naive fermion, taste-singlet symbol 1/2 sin 2p:             -2   F(2m)
  naive fermion, nearest-neighbour symbol sin p:              G(m) = 1/2 <(s_x^2 c_x - s_y^2 c_y)(c_x - c_y)/omega_n>
  naive-dispersion boson (bosonic doublers), symbol 1/2 sin 2p: +1/2 F(2m)
  photon, option A (canonical/Poynting orbital flow, f = sin q): 2 F(0)
  photon, option B (Maxwell in a unimodular diagonal metric a=(e^eps, e^-eps, 1)):  2 F_B(0),
        F_B(M) = 1/2 d^2/deps^2 < sqrt(M^2 + e^-eps Kx^2 + e^eps Ky^2 + Kz^2) >   (metric-coupled KG scalar)

kz is integrated in closed form (complete elliptic integrals); (kx,ky) by polar Gauss-Legendre around every
singular point with geometric radial panels.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import ellipk, ellipe, ellipkm1
import sys

# ---------- kz-averages:  J_s(a,b) = (1/pi) int_0^pi (a - b cos t)^(-s) dt ----------
def _parts(d, b):   # d = a - b >= 0 supplied exactly (avoids cancellation near the singular point)
    u = d + 2*b; p = d/u; mm = 1 - p
    return u, p, mm, ellipkm1(p), ellipe(mm)
def Jm12(a, b, d=None):   # s = -1/2  (mean of sqrt)
    d = a - b if d is None else d
    u, p, mm, K, E = _parts(d, b)
    return (2/np.pi)*np.sqrt(u)*E
def J12(a, b, d=None):
    d = a - b if d is None else d
    u, p, mm, K, E = _parts(d, b)
    return (2/np.pi)*K/np.sqrt(u)
def J32(a, b, d=None):
    d = a - b if d is None else d
    u, p, mm, K, E = _parts(d, b)
    return (2/np.pi)*E/(d*np.sqrt(u))
def J52(a, b, d=None):
    d = a - b if d is None else d
    u, p, mm, K, E = _parts(d, b)
    return (2/(3*np.pi))/np.sqrt(u)/d*((2*E-K)/u + 2*E/d)

def check_J():
    t = np.linspace(0, np.pi, 200001)
    out = []
    for a, b in [(2.3, 2.0), (3.7, 2.0), (1.2, 0.5), (0.8, 0.5)]:
        for s, fn in [(-0.5, Jm12), (0.5, J12), (1.5, J32), (2.5, J52)]:
            direct = np.trapezoid((a-b*np.cos(t))**(-s), t)/np.pi
            out.append(abs(fn(a, b)/direct - 1))
    return max(out)

# ---------- polar quadrature over a square centred on a singular point ----------
def polar_nodes(cx, cy, h, nphi=48, nr=20, npan=26):
    xg, wg = leggauss(nphi); xr, wr = leggauss(nr)
    X = []; Y = []; W = []
    for e in range(4):
        pe = e*np.pi/2
        for (lo, hi) in [(pe-np.pi/4, pe), (pe, pe+np.pi/4)]:
            phi = 0.5*(hi-lo)*xg + 0.5*(hi+lo); wphi = 0.5*(hi-lo)*wg
            rmax = h/np.cos(phi-pe)
            br = np.concatenate([[0.0], 2.0**(-np.arange(npan-1, -1, -1))])   # geometric panels in r/rmax
            for i in range(npan):
                r0, r1 = br[i], br[i+1]
                t = 0.5*(r1-r0)*xr + 0.5*(r1+r0); wt = 0.5*(r1-r0)*wr
                R = t[None, :]*rmax[:, None]
                WW = wphi[:, None]*wt[None, :]*rmax[:, None]*R
                X.append(cx + R*np.cos(phi)[:, None]); Y.append(cy + R*np.sin(phi)[:, None]); W.append(WW)
    return np.concatenate([x.ravel() for x in X]), np.concatenate([y.ravel() for y in Y]), np.concatenate([w.ravel() for w in W])

KX, KY, WK = polar_nodes(0.0, 0.0, np.pi)               # KG: one singular point
WK = WK/(2*np.pi)**2
PN = [polar_nodes(cx, cy, np.pi/2) for cx in (0.0, np.pi) for cy in (0.0, np.pi)]   # naive: four
PX = np.concatenate([p[0] for p in PN]); PY = np.concatenate([p[1] for p in PN]); WP = np.concatenate([p[2] for p in PN])/(2*np.pi)**2

cx_, cy_ = np.cos(KX), np.cos(KY)
NXY = (cx_ - cy_)**2*(cx_ + cy_)
KX2 = 4*np.sin(KX/2)**2; KY2 = 4*np.sin(KY/2)**2
A0 = 6 - 2*cx_ - 2*cy_                                   # omega^2 = M^2 + A0 - 2 cos kz
D0 = KX2 + KY2                                           # A0 - 2, exact

def F(M):            # flow-coupled KG scalar
    return np.sum(WK*NXY*J12(None, 2.0, M*M + D0))/8
def F_coeffs():      # analytic Taylor coefficients c0, c2, c4 (all convergent)
    return (np.sum(WK*NXY*J12(None, 2.0, D0))/8,
            np.sum(WK*NXY*(-0.5)*J32(None, 2.0, D0))/8,
            np.sum(WK*NXY*(3/8)*J52(None, 2.0, D0))/8)
def F_B(M):          # metric-coupled KG scalar, unimodular exponential parametrisation
    d = M*M + D0
    return 0.5*np.sum(WK*((KX2 + KY2)/2*J12(None, 2.0, d) - (KY2 - KX2)**2/4*J32(None, 2.0, d)))
def F_B_c2():
    d = D0
    return 0.5*np.sum(WK*(-(KX2 + KY2)/4*J32(None, 2.0, d) + 3*(KY2 - KX2)**2/8*J52(None, 2.0, d)))

sx, sy, cpx, cpy = np.sin(PX), np.sin(PY), np.cos(PX), np.cos(PY)
GN = (sx**2*cpx - sy**2*cpy)*(cpx - cpy)
AN = sx**2 + sy**2 + 0.5                                 # omega_n^2 = m^2 + AN - 1/2 cos(2 pz)
DN = sx**2 + sy**2
def G(m):            # naive fermion, nearest-neighbour symbol sin p (4 components, sea -2 omega_n per site)
    return 0.5*np.sum(WP*GN*J12(None, 0.5, m*m + DN))
def naive_half2p(m): # naive fermion with symbol 1/2 sin 2p, computed directly on the naive dispersion
    c2x, c2y = np.cos(2*PX), np.cos(2*PY)
    return -(1/8)*np.sum(WP*(c2x - c2y)**2*(c2x + c2y)*J12(None, 0.5, m*m + DN))
def G_c0c2():
    return 0.5*np.sum(WP*GN*J12(None, 0.5, DN)), 0.5*np.sum(WP*GN*(-0.5)*J32(None, 0.5, DN))

def photon_metric_check(rng):
    """lattice Maxwell (noncompact, Yee) in a unimodular diagonal metric: eigenfrequencies^2 vs sum K_i^2/a_i."""
    err = 0.0
    for _ in range(20):
        q = rng.uniform(-np.pi, np.pi, 3); e = rng.uniform(-0.5, 0.5)
        a = np.exp(np.array([e, -e, 0.0]))
        d = np.exp(1j*q) - 1                              # forward difference symbols
        C = np.array([[0, -d[2], d[1]], [d[2], 0, -d[0]], [-d[1], d[0], 0]])   # (curl A)_i
        D = np.diag(a)
        M = np.sqrt(D) @ C.conj().T @ D @ C @ np.sqrt(D)  # H = 1/2 E^T D E + 1/2 B^T D B, B = C A
        ev = np.sort(np.linalg.eigvalsh(M))
        Om2 = np.sum(4*np.sin(q/2)**2/a)
        err = max(err, abs(ev[0]), abs(ev[1]-Om2), abs(ev[2]-Om2))
    return err

if __name__ == '__main__':
    rng = np.random.default_rng(7)
    print('checks')
    print(f'  elliptic kz-averages vs direct quadrature: max rel err = {check_J():.1e}')
    print(f'  lattice Maxwell in diagonal unimodular metric: max |eig - {{0, Om^2, Om^2}}| = {photon_metric_check(rng):.1e}')
    print(f'  F(1) = {F(1.0):+.12e}   (referee V3: +1.970388641877e-03)')
    print(f'  -1/2 F(1) [staggered m=0.5, RN norm] x4 = {-0.5*F(1.0)*4:+.10e}  (referee V1-norm continuum: -3.940777283755e-03)')
    print(f'  -1/2 F(2) [staggered m=1, RN norm] = {-0.5*F(2.0):+.6e}  (V3 table: -5.29e-4)')
    for m in [0.3, 1.0]:
        print(f'  naive fermion, symbol 1/2 sin2p, direct = {naive_half2p(m):+.12e} ; -2F(2m) = {-2*F(2*m):+.12e}')
    # quadrature convergence: rebuild with more nodes
    X2, Y2, W2 = polar_nodes(0.0, 0.0, np.pi, nphi=64, nr=28, npan=34); W2 = W2/(2*np.pi)**2
    c2x, c2y = np.cos(X2), np.cos(Y2)
    for M in [0.0, 0.05, 1.0]:
        alt = np.sum(W2*(c2x-c2y)**2*(c2x+c2y)*J12(None, 2.0, M*M + 4*np.sin(X2/2)**2 + 4*np.sin(Y2/2)**2))/8
        print(f'  quadrature convergence F({M}): {F(M):+.15e} vs finer {alt:+.15e}  diff {F(M)-alt:+.1e}')
    sys.stdout.flush()

    print('\n(1) exact mu_E(m) per species, RN-L1 normalisation, per lattice site')
    print('   m      KG F(m)        stag -F(2m)/2   naive(1/2sin2p)  naive(sin p) G   naiveBoson F(2m)/2  KG metric F_B(m)')
    for m in [0.0, 0.01, 0.1, 0.3, 0.5, 1.0, 2.0]:
        print(f'  {m:4.2f}  {F(m):+.6e}  {-0.5*F(2*m):+.6e}  {-2*F(2*m):+.6e}  {G(m):+.6e}  {0.5*F(2*m):+.6e}  {F_B(m):+.6e}')
    print(f'  photon option A (2 F(0)) = {2*F(0.0):+.8e};  photon option B (2 F_B(0)) = {2*F_B(0.0):+.8e}')

    print('\n(2) small-M expansion of F(M) = c0 + c2 M^2 + c4 M^4 + c6L M^6 ln M + c6 M^6 + O(M^8 ln M)')
    c0, c2, c4 = F_coeffs()
    c6L = 1/(384*np.pi**2)
    print(f'  c0 = {c0:+.12e}\n  c2 = {c2:+.12e}\n  c4 = {c4:+.12e}\n  c6L (analytic 1/(384 pi^2)) = {c6L:+.12e}')
    Ms = np.array([0.04, 0.06, 0.08, 0.1, 0.13, 0.16, 0.2, 0.25, 0.3])
    R = np.array([(F(M) - c0 - c2*M**2 - c4*M**4)/M**6 for M in Ms])
    A = np.stack([np.log(Ms), np.ones_like(Ms), Ms**2*np.log(Ms), Ms**2, Ms**4*np.log(Ms), Ms**4], 1)
    sol = np.linalg.lstsq(A, R, rcond=None)[0]
    print(f'  fit of (F - c0 - c2M^2 - c4M^4)/M^6 on M in [0.04,0.3]: c6L = {sol[0]:+.6e} (analytic {c6L:+.6e}), c6 = {sol[1]:+.6e}')
    A2 = np.stack([np.ones_like(Ms), Ms**2*np.log(Ms), Ms**2, Ms**4*np.log(Ms), Ms**4], 1)
    sol2 = np.linalg.lstsq(A2, R - c6L*np.log(Ms), rcond=None)[0]
    c6 = sol2[0]
    print(f'  with c6L fixed analytic: c6 = {c6:+.6e}; next: d8L = {sol2[1]:+.3e}, d8 = {sol2[2]:+.3e}')
    for M in [0.05, 0.1, 0.2, 0.5]:
        ser = c0 + c2*M**2 + c4*M**4 + (c6L*np.log(M) + c6)*M**6
        print(f'  series check M={M}: F = {F(M):+.14e}, series to M^6 = {ser:+.14e}, diff = {F(M)-ser:+.2e}')
    sys.stdout.flush()

    print('\n(2b) naive fermion with symbol sin p: G(m) = g0 + g2 m^2 + g4L m^4 ln m + g4 m^4 + ...')
    g0, g2 = G_c0c2(); g4L = -1/(2*np.pi**2)
    Ms2 = np.array([0.02, 0.03, 0.05, 0.07, 0.1, 0.13, 0.16, 0.2])
    Rg = np.array([(G(M) - g0 - g2*M**2)/M**4 for M in Ms2])
    Ag = np.stack([np.log(Ms2), np.ones_like(Ms2), Ms2**2*np.log(Ms2), Ms2**2, Ms2**4*np.log(Ms2), Ms2**4], 1)
    sg = np.linalg.lstsq(Ag, Rg, rcond=None)[0]
    sg2 = np.linalg.lstsq(Ag[:, 1:], Rg - g4L*np.log(Ms2), rcond=None)[0]
    print(f'  g0 = {g0:+.10e}, g2 = {g2:+.10e}')
    print(f'  fit: g4L = {sg[0]:+.6e} (analytic -1/(2 pi^2) = {g4L:+.6e}); with analytic g4L: g4 = {sg2[0]:+.6e}')

    print('\n(2c) metric-coupled scalar F_B (and photon option B = 2 F_B(0))')
    b0 = F_B(0.0); b2 = F_B_c2()
    Rb = np.array([(F_B(M) - b0 - b2*M**2)/M**4 for M in Ms])
    Ab = np.stack([np.log(Ms), np.ones_like(Ms), Ms**2*np.log(Ms), Ms**2, Ms**4*np.log(Ms), Ms**4], 1)
    sb = np.linalg.lstsq(Ab, Rb, rcond=None)[0]
    print(f'  b0 = {b0:+.10e}, b2 = {b2:+.10e}; fit of M^4 block: coefficient of M^4 ln M = {sb[0]:+.3e} (expected 0: continuum invariance), b4 = {sb[1]:+.6e}, next M^6 ln M = {sb[2]:+.3e}')
    np.savez('/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/P1/p1_coeffs.npz',
             c0=c0, c2=c2, c4=c4, c6L=c6L, c6=c6, g0=g0, g2=g2, g4L=g4L, g4=sg2[0], b0=b0, b2=b2, b4=sb[1], b6L=sb[2])
