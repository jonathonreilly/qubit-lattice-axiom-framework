"""R7-5 script 1: one-loop IR Lorentz violation (dimension-4 speed term) of a scalar's
self-energy on Z^3 x R (continuous time), for box-confined laws in four classes.

Conventions (Euclidean external P = (w, p), p0 = i w).  Gamma2 = p0^2 - p^2 - mu^2 - Pi_M, with -i Pi_M the
amputated 1PI diagram.  Fermion loop: Pi_M = +g^2 J_f;  scalar loop: Pi_M = -g^2 J_s.
Collins et al. xi = d2Pi/dp0^2 + d2Pi/dp1^2 at p = 0 (p0 = i w => d2/dp0^2 = -d2/dw^2); c^2 = 1 + xi/2.
We report  dc2 = (g^2/16 pi^2) * XI,   XI_f = -8 pi^2 (J_ww - J_pp),  XI_s = +8 pi^2 (J_ww - J_pp).
Collins prediction (fermion loop, f(|k|/L) on each fermion propagator, m/L -> 0):
  xi = (g^2/6pi^2)(1 + 2 int_0^inf x f'(x)^2 dx)  =>  XI = (4/3)(1 + 2 int x f'^2).

Fermion loop (Yukawa g phi psibar psi), Euclidean, continuous k0 done by residues:
  J = int d3k/(2pi)^3 4[(M M' - s.s') I0 - I2] * V(k, k+p)
  I0 = (E1+E2)/(2E1E2((E1+E2)^2+w^2)),  I2 = (1/2)[1/(2E1)+1/(2E2) - (w^2+E1^2+E2^2) I0]
Scalar loop (g phi chi chibar):  J = int d3k/(2pi)^3 I0 * V.

Classes:
  P   : point vertex (V = 1), R7-1 box dispersion s(k) = k on |k_i| <= b1, Wilson term zero in box.
  FF  : frame-fixed box form factor V = chi(k) chi(k+p), chi = prod_i plateau(k_i; c1, c2), c2 < b1.
  INV : scalar loop, V = F(M^2)^2 with M^2 = (E1+E2)^2 - |p|^2 the on-shell pair invariant mass,
        F compact (plateau Lam1, support Lam2); both time orderings (Feynman k0 integral).
  Collins comparator: continuum, V = f(|k|) f(|k+p|).

IR handling: partition of unity in the loop momentum, phi_in(|k|) (radial plateau r1 < r2) with
the inner part done in spherical coordinates (continuum integrand, exact there) and the outer part
on a 3D BZ grid (no IR scale there).  J_ww analytic in w; J_pp: Cauchy contour (inner, analytic)
or Richardson finite differences (outer, C^inf non-analytic)."""
import numpy as np, time, sys
from numpy.polynomial.legendre import leggauss

OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def plateau(x, x1, x2):
    return 1.0 - sstep((np.abs(x) - x1)/(x2 - x1))

# ---------------- integrands (vectorised; E's etc. may be complex for the Cauchy trick) ----------
def ferm_integrand(E1, E2, MMp_minus_ss, w2):
    W = E1 + E2
    I0 = W/(2*E1*E2*(W*W + w2))
    I2 = 0.5*(1/(2*E1) + 1/(2*E2) - (w2 + E1*E1 + E2*E2)*I0)
    return 4*(MMp_minus_ss*I0 - I2)

def ferm_dw2(E, MM_minus_ss):
    """d/d(w^2) of the fermion integrand at w = 0, p = 0 (E1 = E2 = E)."""
    W = 2*E
    I0 = W/(2*E*E*W*W)
    dI0 = -W/(2*E*E*W**4)
    dI2 = 0.5*(-I0 - (2*E*E)*dI0)
    return 4*(MM_minus_ss*dI0 - dI2)

def scal_integrand(E1, E2, w2):
    W = E1 + E2
    return W/(2*E1*E2*(W*W + w2))

def scal_dw2(E):
    W = 2*E
    return -W/(2*E*E*W**4)

# ---------------- spherical-coordinate continuum integrals (p along z) --------------------------
def radial_nodes(kmax, m, nper=48):
    edges = [0.0]
    x = m/8
    while x < kmax:
        edges.append(x); x *= 2
    edges.append(kmax)
    edges = sorted(set(edges))
    xg, wg = leggauss(nper)
    ks, ws = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        ks.append(0.5*(b-a)*xg + 0.5*(b+a)); ws.append(0.5*(b-a)*wg)
    return np.concatenate(ks), np.concatenate(ws)

def sph_J_derivs(kind, m, weight_k, vert=None, kmax=None, h0=None, ncirc=24, nth=64):
    """Continuum part: returns (J_ww, J_pp) of int d3k/(2pi)^3 weight(|k|) * vert * integrand.
    vert(k2, kp2) multiplies (analytic functions of |k|^2 and |k+p|^2), e.g. Collins f f."""
    k, wk = radial_nodes(kmax, m)
    c, wc = leggauss(nth)
    K, C = np.meshgrid(k, c, indexing='ij')
    WK = np.outer(wk*K[:, 0]**2*weight_k(k), wc) * 2*np.pi/(2*np.pi)**3
    # J_ww at p = 0
    E = np.sqrt(K*K + m*m)
    V0 = 1.0 if vert is None else vert(K*K, K*K)
    if kind == 'f':
        dw2 = ferm_dw2(E, m*m - K*K)
    else:
        dw2 = scal_dw2(E)
    J_ww = 2*np.sum(WK*V0*dw2)
    # J_pp via Cauchy contour in complex h (analytic integrand)
    if h0 is None: h0 = 0.25*m
    th = 2*np.pi*np.arange(ncirc)/ncirc
    acc = 0.0
    for t in th:
        h = h0*np.exp(1j*t)
        kp2 = K*K + 2*K*h*C + h*h
        E1 = np.sqrt(K*K + m*m + 0j); E2 = np.sqrt(kp2 + m*m)
        V = 1.0 if vert is None else vert(K*K + 0j, kp2)
        if kind == 'f':
            val = ferm_integrand(E1, E2, m*m - (K*K + K*h*C), 0.0)
        else:
            val = scal_integrand(E1, E2, 0.0)
        acc += np.sum(WK*V*val)*np.exp(-2j*t)
    c2 = acc/ncirc/h0**2
    return J_ww, 2*c2.real, abs(c2.imag)

# ---------------- lattice functions ------------------------------------------------------------
class BoxLattice:
    """R7-1 box law: s(k) = k on |k| <= b1, -> sin k by b2; Wilson term r sum (1-rho)(1-cos k)."""
    def __init__(self, b1, b2, m, r=1.0):
        self.b1, self.b2, self.m, self.r = b1, b2, m, r
    def rho(self, k): return plateau(k, self.b1, self.b2)
    def s(self, k):
        r = self.rho(k); return r*k + (1-r)*np.sin(k)
    def Wil(self, k):
        return self.r*(1 - self.rho(k))*(1 - np.cos(k))

def lattice_outer_J(lat, kind, phi_in_r, vert_box=None, w2=0.0, h=0.0, N=96, chunk=8):
    """Outer part on the BZ grid: int_BZ d3k/(2pi)^3 (1 - phi_in(|k|)) * V * integrand, p = h z."""
    ks = -np.pi + 2*np.pi*np.arange(N)/N
    dk3 = (2*np.pi/N)**3/(2*np.pi)**3
    KY, KZ = np.meshgrid(ks, ks, indexing='ij')
    sy, sz = lat.s(KY), lat.s(KZ); Wy, Wz = lat.Wil(KY), lat.Wil(KZ)
    szp = lat.s(KZ + h); Wzp = lat.Wil(KZ + h)
    if vert_box is not None:
        cy, cz, czp = vert_box(KY), vert_box(KZ), vert_box(KZ + h)
    tot = 0.0
    for i0 in range(0, N, chunk):
        kx = ks[i0:i0+chunk][:, None, None]
        sx, Wx = lat.s(kx), lat.Wil(kx)
        kk = np.sqrt(kx**2 + KY[None]**2 + KZ[None]**2)
        wout = 1 - phi_in_r(kk)
        if kind == 'f':
            M1 = lat.m + Wx + Wy[None] + Wz[None]
            M2 = lat.m + Wx + Wy[None] + Wzp[None]
            E1 = np.sqrt(sx**2 + sy[None]**2 + sz[None]**2 + M1**2)
            E2 = np.sqrt(sx**2 + sy[None]**2 + szp[None]**2 + M2**2)
            ss = sx**2 + sy[None]**2 + sz[None]*szp[None]
            val = ferm_integrand(E1, E2, M1*M2 - ss, w2)
        else:
            # doubler-free scalar: eps^2 = m^2 + sum_i w(k_i), w = k^2 in box, >= b1^2 outside
            E1 = np.sqrt(lat.m**2 + lat.wsc(kx) + lat.wsc(KY)[None] + lat.wsc(KZ)[None])
            E2 = np.sqrt(lat.m**2 + lat.wsc(kx) + lat.wsc(KY)[None] + lat.wsc(KZ + h)[None])
            val = scal_integrand(E1, E2, w2)
        if vert_box is not None:
            cx = vert_box(kx)
            val = val*(cx*cy[None]*cz[None])*(cx*cy[None]*czp[None])
        tot += np.sum(wout*val)
    return tot*dk3

def lattice_outer_derivs(lat, kind, phi_in_r, vert_box=None, N=96, hs=(0.02, 0.01)):
    J0 = lattice_outer_J(lat, kind, phi_in_r, vert_box, 0.0, 0.0, N)
    # J_ww analytically in w2: finite difference in w2 is exact-enough? use small w2 Richardson
    dws = []
    for dw in (1e-3, 5e-4):
        Jw = lattice_outer_J(lat, kind, phi_in_r, vert_box, dw, 0.0, N)
        dws.append(2*(Jw - J0)/dw)   # J_ww = 2 dJ/d(w^2)
    J_ww = 2*dws[1] - dws[0]
    d2 = []
    for h in hs:
        Jh = lattice_outer_J(lat, kind, phi_in_r, vert_box, 0.0, h, N)
        d2.append(2*(Jh - J0)/h**2)
    J_pp = (4*d2[1] - d2[0])/3
    return J_ww, J_pp, d2

def run_collins():
    pr('== (A) Collins comparator: continuum fermion loop, f(|k|/Lam) on each propagator, Lam = 1 ==')
    tests = {
        'f = exp(-x^2)        ': (lambda x2: np.exp(-x2), 0.5),
        'f = 1/(1+x^2)^2      ': (lambda x2: 1/(1+x2)**2, None),
        'f = exp(-x^4)        ': (lambda x2: np.exp(-x2*x2), None),
    }
    # int x f'^2 numerically
    xs = np.linspace(0, 40, 400001)
    for name, (f, exact) in tests.items():
        fx = f(xs**2); fp = np.gradient(fx, xs)
        I = np.trapezoid(xs*fp**2, xs)
        pred = (4/3)*(1 + 2*I)
        for m in (0.02, 0.005):
            vert = lambda k2, kp2: f(k2)*f(kp2)
            Jww, Jpp, im = sph_J_derivs('f', m, lambda k: np.ones_like(k), vert, kmax=12.0, nth=96)
            XI = -8*np.pi**2*(Jww - Jpp)
            pr(f'  {name} m={m:<6}  int x f\'^2 = {I:.6f}  XI = {XI:+.6f}   Collins (4/3)(1+2I) = {pred:.6f}   ratio {XI/pred:+.5f}')
    pr('  scalar loop (g phi chi chibar, g dimensionful) with the same f: XI_s*Lam^2 is the dimensionless LV;')
    for Lam in (1.0, 2.0, 4.0):
        f = lambda x2: np.exp(-x2/Lam**2)
        vert = lambda k2, kp2: f(k2)*f(kp2)
        Jww, Jpp, im = sph_J_derivs('s', 0.01, lambda k: np.ones_like(k), vert, kmax=12.0*Lam, nth=96)
        XI = 8*np.pi**2*(Jww - Jpp)
        pr(f'    Lam={Lam}: XI_s = {XI:+.6e}  (units 1/mass^2)   XI_s*Lam^2 = {XI*Lam**2:+.6f}')

def run_box(kind, b1, b2, m, r, vert_c=None, N=96, r1=0.8, r2=1.6, label='', hs=(0.02, 0.01)):
    lat = BoxLattice(b1, b2, m, r)
    phi_in = lambda kk: plateau(kk, r1, r2)
    Jww_i, Jpp_i, im = sph_J_derivs(kind, m, phi_in, None, kmax=r2)
    vb = None if vert_c is None else (lambda k: plateau(k, vert_c[0], vert_c[1]))
    Jww_o, Jpp_o, d2 = lattice_outer_derivs(lat, kind, phi_in, vb, N=N, hs=hs)
    sgn = -1.0 if kind == 'f' else 1.0
    XI = sgn*8*np.pi**2*((Jww_i + Jww_o) - (Jpp_i + Jpp_o))
    pr(f'  {label} b1={b1} b2={b2} m={m} r={r} N={N}: inner(J_ww-J_pp)={Jww_i-Jpp_i:+.6e} '
       f'outer={Jww_o-Jpp_o:+.6e} (FD h1/h2: {d2[0]:+.6e}/{d2[1]:+.6e})  XI = {XI:+.6f}')
    return XI

def run_inv():
    pr('== (D) INV class: scalar loop, F(M^2) of the on-shell pair invariant mass, both time orderings ==')
    Lam1, Lam2, m = 1.0, 1.6, 0.2
    F = lambda M2: plateau(np.sqrt(np.maximum(M2.real, 0)), Lam1, Lam2)
    # Minkowski evaluation below threshold: Pi(E,p) = int d3k/(2pi)^3 F^2/(4E1E2) * 2W/(W^2 - E^2)
    # one-ordering comparator: Pi_a = int F^2/(4E1E2) * 1/(W - E)  (times 2 for normalisation)
    k, wk = radial_nodes(3.0, m, nper=96)
    c, wc = leggauss(256)
    K, C = np.meshgrid(k, c, indexing='ij')
    WK = np.outer(wk*k**2, wc)*2*np.pi/(2*np.pi)**3
    for s0 in (0.0, 0.09, 0.15):
        rows = []
        for p in (0.0, 0.3, 0.6, 0.9):
            E2ext = s0 + p*p
            E1 = np.sqrt(K*K + m*m); E2 = np.sqrt(K*K + 2*K*p*C + p*p + m*m)
            W = E1 + E2; M2 = W*W - p*p
            FF = F(M2)**2
            full = np.sum(WK*FF/(4*E1*E2)*2*W/(W*W - E2ext))
            Eext = np.sqrt(E2ext + 0j)
            # one time ordering only (instant form, no Z graph), with relativistic normalisation:
            one = np.sum(WK*FF/(4*E1*E2)*(1/(W - Eext))).real*2
            rows.append((p, full, one))
        base_full, base_one = rows[0][1], rows[0][2]
        pr(f'  s = E^2 - p^2 = {s0}:')
        for p, full, one in rows:
            pr(f'    p={p:.1f}  Pi_full = {full:.12f}  (diff {full-base_full:+.2e})   '
               f'Pi_one-ordering = {one:.8f} (diff {one-base_one:+.2e})')
    # support check: largest constituent momentum component on supp F at |p| <= 0.9
    E1 = np.sqrt(K*K + m*m)
    mx = 0
    for p in (0.0, 0.9):
        E2 = np.sqrt(K*K + 2*K*p*C + p*p + m*m); M2 = (E1+E2)**2 - p*p
        on = F(M2) > 0
        mx = max(mx, np.max(np.where(on, np.maximum(K, np.sqrt(K*K+2*K*p*C+p*p)), 0)))
    pr(f'  largest |k| of either leg on supp F for |p| <= 0.9: {mx:.4f}  (box edge b1 = 2.0 => inside)')

def run_inv_lattice(N=128):
    """Lattice realisation of INV: doubler-free scalar dispersion, F of the lattice pair mass."""
    pr('== (E) INV on the lattice: 3D BZ sum with lattice eps (doubler-free) vs continuum ==')
    b1, b2, m = 2.0, 3.0, 0.2
    Lam1, Lam2 = 1.0, 1.6
    def wsc(k):
        r = plateau(k, b1, b2)
        return r*k*k + (1-r)*(np.pi**2/2)*(1 - np.cos(k))
    ks = -np.pi + 2*np.pi*np.arange(N)/N
    # minimum of w outside the box (sanity: doubler-free)
    kk = np.linspace(-np.pi, np.pi, 200001); ww = wsc(kk)
    pr(f'  min w(k) on |k| >= b1: {ww[np.abs(kk) >= b1].min():.4f} (b1^2 = {b1*b1})')
    F = lambda M2: plateau(np.sqrt(np.maximum(M2, 0)), Lam1, Lam2)
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
    out = {}
    for (Eext2, p) in ((-0.04, 0.0), (-0.04 + 0.09, 0.3), (-0.04 + 0.36, 0.6)):
        E1 = np.sqrt(m*m + wsc(KX) + wsc(KY) + wsc(KZ))
        E2 = np.sqrt(m*m + wsc(KX) + wsc(KY) + wsc(KZ + p))
        W = E1 + E2; M2 = W*W - p*p
        val = F(M2)**2/(4*E1*E2)*2*W/(W*W - Eext2)
        J = val.sum()*(2*np.pi/N)**3/(2*np.pi)**3
        out[p] = J
        pr(f'  s = -0.04, p = {p}: Pi_lattice = {J:.10f}')
    pr(f'  spread over p: {max(out.values()) - min(out.values()):.2e}')
    k, wk = radial_nodes(3.0, m, nper=96); c, wc = leggauss(256)
    K, C = np.meshgrid(k, c, indexing='ij'); WK = np.outer(wk*k**2, wc)*2*np.pi/(2*np.pi)**3
    E1 = np.sqrt(K*K + m*m); W = 2*E1
    cont = np.sum(WK*F(W*W)**2/(4*E1*E1)*2*W/(W*W + 0.04))
    pr(f'  continuum (spherical quadrature) value at s = -0.04: {cont:.10f}; lattice - continuum = {out[0.0]-cont:+.2e}')

if __name__ == '__main__':
    t0 = time.time()
    run_collins()
    pr('== (B) class P: point Yukawa vertex, box Dirac fermion (s = k, Wilson = 0 in box) ==')
    for m in (0.2, 0.1, 0.05, 0.02, 0.01):
        run_box('f', 2.0, 3.0, m, 1.0, None, N=128, label='P ')
    for N in (96, 160):
        run_box('f', 2.0, 3.0, 0.02, 1.0, None, N=N, label='P ')
    for (b1, b2, r) in ((1.5, 2.8, 1.0), (2.6, 3.1, 1.0), (2.0, 3.0, 0.5), (1.0, 2.5, 1.0)):
        run_box('f', b1, b2, 0.02, r, None, N=128, r1=0.4, r2=0.9, label='P ')
    run_box('f', 2.6, 3.1, 0.02, 1.0, None, N=192, r1=0.4, r2=0.9, label='P ')
    pr('== (C) class FF: frame-fixed box form factor chi(k)chi(k+p) inside the relativistic box (b1 = 2) ==')
    for m in (0.05, 0.02, 0.01):
        run_box('f', 2.0, 3.0, m, 1.0, (1.0, 1.9), N=128, r1=0.4, r2=0.9, label='FF c=(1.0,1.9)')
    for N in (96, 160):
        run_box('f', 2.0, 3.0, 0.02, 1.0, (1.0, 1.9), N=N, r1=0.4, r2=0.9, label='FF c=(1.0,1.9)')
    for c in ((0.5, 0.95), (0.25, 0.475)):
        run_box('f', 2.0, 3.0, 0.01, 1.0, c, N=160, r1=c[0]*0.3, r2=c[0]*0.6, label=f'FF c={c}')
    run_inv()
    run_inv_lattice()
    pr(f'runtime {time.time()-t0:.1f}s')
    with open(__file__.replace('.py', '.out'), 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')
