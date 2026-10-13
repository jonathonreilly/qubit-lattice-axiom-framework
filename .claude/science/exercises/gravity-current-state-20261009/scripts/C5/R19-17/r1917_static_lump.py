"""C5 R19-17 (a): is the lattice vacuum stress a LOCAL functional of a lumpy V1 lattice (static part)?
Model: NN real scalar on Z^3, sites fixed in comoving labels, local scale factor a(z) (planar lump):
  ds^2 = -dt^2 + a(z)^2 (dx^2+dy^2+dz^2);  H = sum_sites pi^2/(2 a^3) + (a^3 m^2/2) phi^2
          + sum_{x,y links at z} a(z) (dphi)^2/2 + sum_{z links} a_{z+1/2} (dphi)^2/2,
  a_{z+1/2} = (a_z + a_{z+1})/2  (stencil choice, stated).
Fourier in x,y (midpoint grid, no zero modes) -> independent 1D chains in z (exact ground state).
Physical energy density rho(z) = <site energy>/a_z^3 (z-link energy split half/half).
Order-0 adiabatic prediction: rho_hom(a(z)) = homogeneous ground-state density at the local spacing.
Order-2 local ansatz: r(z) = rho - rho_hom = [alpha (d ln a)^2 + beta d^2 ln a]/a^4  (comoving d = d/dz).
Tests: (1) residual scales as width^-2 (order 2); (2) (alpha, beta) fitted on one profile predict others
(universality = locality of the functional); (3) far tails vanish (local)."""
import numpy as np
from scipy.interpolate import CubicSpline
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

NT = 16                                   # transverse midpoint grid per axis
kt = 2*np.pi*(np.arange(NT)+0.5)/NT
g = 4*np.sin(kt/2)**2
OM2 = (g[:, None] + g[None, :]).ravel()   # transverse Omega_perp^2 (lattice units)

def rho_profile(a, m):
    Nz = len(a); ah = 0.5*(a + np.roll(a, -1))          # a_{z+1/2}
    M = a**3; Mi = 1/np.sqrt(M)
    e = np.zeros(Nz)
    idx = np.arange(Nz); nxt = (idx+1) % Nz
    for O2 in OM2:
        K = np.diag(a**3*m*m + a*O2 + ah + np.roll(ah, 1))
        K[idx, nxt] -= ah; K[nxt, idx] -= ah
        D = Mi[:, None]*K*Mi[None, :]
        w2, V = np.linalg.eigh(D); w = np.sqrt(w2)
        Gff = 0.5*Mi[:, None]*((V/w) @ V.T)*Mi[None, :]      # <phi phi^T>
        Gpp = 0.5/Mi[:, None]*((V*w) @ V.T)/Mi[None, :]      # <pi pi^T>
        dg = np.diag(Gff)
        dphi2 = dg + dg[nxt] - 2*Gff[idx, nxt]
        site = np.diag(Gpp)/(2*M) + (a**3*m*m + a*O2)*dg/2
        link = ah*dphi2/2
        e += site + 0.5*(link + np.roll(link, 1))
    return e/len(OM2)/a**3

def rho_hom(aval, m, Nz=64):
    return rho_profile(np.full(Nz, aval), m)[0]

Nz = 128; z = np.arange(Nz) - Nz/2
def lna_profile(kind, A, w):
    if kind == 'gauss':  return A*np.exp(-z**2/(2*w*w))
    if kind == 'sech2':  return A/np.cosh(z/w)**2
    if kind == 'bump2':  return A*(np.exp(-(z-w)**2/(2*w*w)) - 0.6*np.exp(-(z+w)**2/(1.0*w*w)))
def derivs(f):
    d1 = (np.roll(f, -1) - np.roll(f, 1))/2; d2 = np.roll(f, -1) - 2*f + np.roll(f, 1)
    return d1, d2

for m in (0.0, 0.5):
    pr(f'\n===== mass m = {m} (lattice units; comoving spacing 1) =====')
    if m == 0.0:
        e00 = rho_hom(1.0, m); hom = lambda aa: e00/aa**4
        pr(f'  e0(a=1) = {e00:.8f};  massless: rho_hom(a) = e0/a^4 (check a=1.2: rel.dev {rho_hom(1.2,m)*1.2**4/e00 - 1:.2e})')
    else:
        agrid = np.linspace(0.70, 1.40, 57)
        tab = np.array([rho_hom(aa, m) for aa in agrid]); cs = CubicSpline(agrid, tab); hom = lambda aa: cs(aa)
        pr(f'  e0(a=1) = {rho_hom(1.0, m):.8f}; spline check at a=1.037: {cs(1.037) - rho_hom(1.037, m):.2e}')
    cases = [('gauss', 0.08, 8), ('gauss', 0.08, 16), ('sech2', -0.10, 10), ('bump2', 0.06, 9), ('gauss', 0.16, 12)]
    res = {}
    for kind, A, w in cases:
        la = lna_profile(kind, A, w); a = np.exp(la)
        r = rho_profile(a, m) - hom(a)
        d1, d2 = derivs(la)
        res[(kind, A, w)] = (r, d1, d2, a)
        sel = np.abs(z) > 5*w
        far = np.abs(r[sel]).max() if np.any(sel) else float('nan')
        pr(f'  {kind:6s} A={A:+.2f} w={w:2d}: max|r| = {np.abs(r).max():.4e} (rho0 = {float(hom(1.0)):.4f}); max|r| at |z|>5w = {far:.2e}')
    r8 = np.abs(res[('gauss', 0.08, 8)][0]).max(); r16 = np.abs(res[('gauss', 0.08, 16)][0]).max()
    pr(f'  width scaling (gauss A=0.08): max|r|(w=8)/max|r|(w=16) = {r8/r16:.3f}  (local order 2: 4)')
    def fitAB(key):
        r, d1, d2, a = res[key]; X = np.vstack([d1**2/a**4, d2/a**4]).T
        coef, *_ = np.linalg.lstsq(X, r, rcond=None); return coef
    for fitkey in [('gauss', 0.08, 16), ('sech2', -0.10, 10)]:
        al, be = fitAB(fitkey)
        pr(f'  fit on {fitkey}: alpha = {al:+.6f}, beta = {be:+.6f}')
        for key, (r, d1, d2, a) in res.items():
            pred = (al*d1**2 + be*d2)/a**4
            pr(f'     predict {str(key):24s}: max|r - pred|/max|r| = {np.abs(r-pred).max()/np.abs(r).max():.3e}')
    la = lna_profile('gauss', 0.01, 16); a = np.exp(la); r = rho_profile(a, m) - hom(a); d1, d2 = derivs(la)
    pr(f'  small amplitude A=0.01 w=16: r*a^4/d2 at centre = {r[Nz//2]*a[Nz//2]**4/d2[Nz//2]:+.6f} (-> beta + alpha d1^2/d2, d1=0 at centre)')

open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
