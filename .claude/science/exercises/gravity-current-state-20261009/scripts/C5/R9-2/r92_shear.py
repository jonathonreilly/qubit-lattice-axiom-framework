"""C5 R9-2 (a): uniform-strain (E_g, T_2g) susceptibility of R8-2's universal box+edge stress.

Uniform strain enters through the first moment of the momentum density, i.e. the flow
  dk/de = (1/2) h . p(k)    (RN-L1 normalisation, as V3's scalar: velocity (e/2) h f(k)),
where p = grad(eps^2/2) is the forward value of R8-2's T^{0i} (its gravitating momentum).
Strained vacuum c-number per site: E(e) = < eps_vac(Phi_e^{-1} k) >_k = < J_e eps_vac >  (V3, Liouville).
mu = d^2 E / de^2 at e = 0.  Closed form (proved here, integration by parts on the torus):
  E(e) = E0 + e E1 + e^2 E2,  E2 = -1/2 < div v * (v . grad eps_vac) >,  v = (1/2) h . p.
For E_g, h = diag(1,-1,0): div v = (1/2)(p'(kx) - p'(ky)) = (1/2)(A_xx - A_yy), A = Hess(eps^2/2) - I.
So the integrand vanishes identically wherever A = 0, i.e. on the box: the edge carries all of it.
For T_2g, h = offdiag(x,y): div v = (1/2)(d_x p(ky) + d_y p(kx)) = 0 -> J = 1 -> mu_T2 = 0 (Liouville).

Vacua considered:
  (F) R7-1/R8-2's own class: empty Fock vacuum, number-conserving, normal-ordered stress -> E(e) = 0
      identically: mu_E = mu_T2 = 0 (no zero-point, no sea).
  (Z) conditional: a zero-point eps_vac = +eps/2 (scalar-field reading of the same dispersion), and
  (S) conditional: a filled negative-energy sea eps_vac = -eps (Dirac-sea reading), per mode.
Calibration: V3's NN scalar (f = sin k, omega^2 = m^2 + sum 4 sin^2(k/2)), m = 1 -> mu_E = +1.970389e-3.
Two methods: closed form (uniform grid, trapezoid) and direct flow integration (RK4) + finite-difference Hessian.
"""
import numpy as np, time, sys
from scipy.interpolate import CubicSpline
T0 = time.time()
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def wrap(k): return -(((-k) + np.pi) % (2*np.pi) - np.pi)
def plateau(k, a, b): return sstep((b - np.abs(wrap(k)))/(b - a))

B, B2 = 2.0, 3.1                       # R8-2 / R7-1 script-1 box
# ---- 1D profiles: eps^2 = m^2 + sum g(k_i);  p = g'/2;  p' = g''/2 = 1 + A_ii
def s_lit(k):
    k = wrap(k); r = plateau(k, B, B2); return r*k + (1-r)*np.sin(k)
def g_lit(k): return s_lit(k)**2
Cg = 2*B/np.sin(B)
def up_gap(k):
    kw = wrap(k); ka = np.abs(kw); r = plateau(ka, B, B2)
    return np.sign(kw)*(r*2*ka + (1-r)*Cg*np.sin(ka))
NG = 400001
kg = np.linspace(0, np.pi, NG)
ug = np.concatenate([[0.0], np.cumsum(0.5*(up_gap(kg[1:])+up_gap(kg[:-1]))*np.diff(kg))])
_ucs = CubicSpline(kg, ug)
def g_gap(k):
    k = np.abs(wrap(k)); return np.where(k <= B, k*k, _ucs(np.minimum(k, np.pi)))
def g_nn(k): return 4*np.sin(k/2)**2      # V3 calibration scalar (its own momentum symbol is sin k, not g'/2)

def d1(f, k, h=1e-5): return (f(k+h) - f(k-h))/(2*h)

def profile(name):
    if name == 'L':
        g = g_lit; gp = lambda k: d1(g_lit, k); gpp = lambda k: d1(lambda x: d1(g_lit, x), k, 1e-4)
    elif name == 'G':
        g = g_gap; gp = up_gap; gpp = lambda k: d1(up_gap, k, 1e-5)
    return g, gp, gpp


def flow_direct(m, N, g, f, d=3, vac='Z', de=0.02):
    """direct: E(e) = < eps_vac(Phi_{-e}(k)) >; E_g separable: kx flows with +(1/2)f, ky with -(1/2)f."""
    k = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    def flow1(x, e, ns=400):
        h = e/ns; rhs = lambda y: -0.5*f(y)
        for _ in range(ns):
            a1 = rhs(x); a2 = rhs(x+h/2*a1); a3 = rhs(x+h/2*a2); a4 = rhs(x+h*a3)
            x = x + h/6*(a1+2*a2+2*a3+a4)
        return x
    cvac = 0.5 if vac == 'Z' else -1.0
    def E(e):
        qx = flow1(k.copy(), e); qy = flow1(k.copy(), -e)
        GX, GY = np.meshgrid(g(qx), g(qy), indexing='ij')
        if d == 2: return cvac*np.sqrt(m*m + GX + GY).mean()
        acc = 0.0
        for gz in g(k): acc += np.sqrt(m*m + GX + GY + gz).sum()
        return cvac*acc/N**3
    v = {e: E(e) for e in [-de, -de/2, 0.0, de/2, de]}
    D = lambda e: (v[e] + v[-e] - 2*v[0])/e**2
    return (4*D(de/2) - D(de))/3

# ---- calibration: V3 NN scalar, f = sin k (its momentum symbol), RN-L1 normalisation, zero-point
pr('=== calibration against V3 (NN scalar, f = sin k, RN-L1 norm, zero-point omega/2) ===')
for m in [1.0, 0.5]:
    k = None
    N = 64
    # closed form with f = sin, f' = cos, and grad_j omega = sin(k_j)/omega for g = 4 sin^2(k/2)
    kk = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
    GX, GY = np.meshgrid(g_nn(kk), g_nn(kk), indexing='ij'); SX, SY = np.meshgrid(np.sin(kk), np.sin(kk), indexing='ij')
    CX, CY = np.meshgrid(np.cos(kk), np.cos(kk), indexing='ij')
    tot = 0.0
    for gz in g_nn(kk):
        om = np.sqrt(m*m + GX + GY + gz)
        div = 0.5*(CX - CY); vgrad = 0.5*0.5*(SX*SX - SY*SY)/om
        tot += (div*vgrad).sum()
    mu_cf = 2*(-0.5*tot/N**3)
    mu_fl = flow_direct(m, 32, g_nn, np.sin, d=3, vac='Z')
    pr('  m = %.1f: closed form (N=64) mu_E = %+.9e ; direct flow (N=32) mu_E = %+.9e ; V3 table (L=64): %s'
       % (m, mu_cf, mu_fl, '+1.970389e-03' if m == 1.0 else '+2.467156e-03'))

# ---- R8-2's universal stress: f = p = g'/2 ; f' = g''/2 = 1 + A
pr('=== R8-2 universal box+edge stress: flow f = p = grad(eps^2/2) (forward T^{0i}); box b = %.1f, b2 = %.1f ===' % (B, B2))
pr('  (F) R7-1/R8-2 class, empty Fock vacuum: E(e) = 0 identically -> mu_E = mu_T2 = 0 exactly (normal-ordered T annihilates |0>).')
for name in ['L', 'G']:
    g, gp, gpp = profile(name)
    f = lambda k, gp=gp: 0.5*gp(k); fp = lambda k, gpp=gpp: 0.5*gpp(k)
    for m in [0.3, 1.0]:
        for d in [2, 3]:
            for vac in ['Z', 'S']:
                N = 256 if d == 2 else 160
                kk = 2*np.pi*(np.arange(N)+0.5)/N - np.pi
                gx = g(kk); fx = f(kk); fpx = fp(kk)
                GX, GY = np.meshgrid(gx, gx, indexing='ij'); FX, FY = np.meshgrid(fx, fx, indexing='ij')
                PX, PY = np.meshgrid(fpx, fpx, indexing='ij'); KX, KY = np.meshgrid(kk, kk, indexing='ij')
                cvac = 0.5 if vac == 'Z' else -1.0
                div = 0.5*(PX - PY)
                inb2 = (np.abs(KX) <= B) & (np.abs(KY) <= B)
                tot = box = 0.0; maxdiv_box = np.max(np.abs(div[(np.abs(KX) < B-1e-3) & (np.abs(KY) < B-1e-3)]))
                zl = [0.0] if d == 2 else list(gx)
                zk = [0.0] if d == 2 else list(kk)
                for gz, kz in zip(zl, zk):
                    eps = np.sqrt(m*m + GX + GY + gz)
                    integ = div*cvac*0.5*(FX*FX - FY*FY)/eps
                    tot += integ.sum()
                    if abs(kz) <= B: box += integ[inb2].sum()
                mu = 2*(-0.5*tot/N**d); mub = 2*(-0.5*box/N**d)
                line = '  profile %s m=%.1f d=%d vac=%s: mu_E = %+.6e  (box part %+.1e, edge part %+.6e; max|div v| on box %.1e)' % (name, m, d, vac, mu, mub, mu - mub, maxdiv_box)
                if d == 3 and m == 1.0 and vac == 'Z':
                    mfl = flow_direct(m, 64, g, f, d=3, vac='Z')
                    line += '  [direct flow N=64: %+.6e]' % mfl
                pr(line)
    # T2 check by direct flow (2D, non-separable)
pr('  T_2g: div v = (1/2)(d/dkx p(ky) + d/dky p(kx)) = 0 identically -> J = 1 -> mu_T2 = 0 for every profile/vacuum (Liouville).')
pr('runtime %.1fs' % (time.time() - T0))
with open(__file__.replace('.py', '.out'), 'w') as fh: fh.write('\n'.join(out) + '\n')
