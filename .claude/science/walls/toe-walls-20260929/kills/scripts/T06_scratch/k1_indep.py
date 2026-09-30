#!/usr/bin/env python3
"""Kill-check T06: independent checks (Claude Sonnet 5.5, same family as attacker).
K1 exact hemisphere / cosine-transform multipliers (sympy, exact).
K2 scaled-effect representability in the attack's own typing (pure states -> KS density forced).
K3 octahedral-only covariance: positive, cubic-covariant, readout-affine law with Born on all six axis readouts, not Born elsewhere.
K4 constant-Fisher ODE class and the T3-type 'C1-smooth=False' flag in hemi_test.py.
"""
import numpy as np, sympy as sp
from numpy.polynomial.legendre import leggauss
t = sp.symbols('t')
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# ---- K1: exact multipliers
P("== K1 exact multipliers")
c = {}; m = {}
for l in range(0, 41):
    Pl = sp.legendre(l, t)
    c[l] = sp.Rational(1, 2) * sp.integrate(Pl, (t, 0, 1))          # hemisphere (Funk-Hecke), mu-normalised
    m[l] = sp.integrate(2 * t * Pl, (t, 0, 1))                         # cosine transform of Y_l: int 2|t| P_l dt/2*2 -> mean of 2|t|P_l
P("  c_1..c_9 (exact):", [str(c[l]) for l in range(1, 10)])
P("  all odd c_l nonzero (l<=39):", all(c[l] != 0 for l in range(1, 40, 2)), "; all even c_l (2<=l<=40) zero:", all(c[l] == 0 for l in range(2, 41, 2)))
P("  cosine-transform multipliers m_l = int_0^1 2 t P_l(t) dt, even l:", [str(m[l]) for l in range(0, 11, 2)])
P("  all even m_l nonzero (l<=40):", all(m[l] != 0 for l in range(0, 41, 2)))

# ---- K2: scaled effects have no deterministic-cell image once pure states have certainty
# Born on all hemispheres at pure r => f_odd = 2 r.u, mean|f_odd| = 1 => slack 0 => f = |f_odd| + f_odd = 4 (r.u)_+ a.e.
P("== K2 scaled effects c P(n), 0<c<1, in the attack's own typing")
P("  Argument: Born on hemispheres at pure r => mean|f_odd|=1 => f=4(r.u)_+ (no slack).  A state-independent cell C with")
P("  mu_r(C)=c(1+r.n)/2 for all pure r needs sym(1_C):=(1_C(u)+1_C(-u))/2 = c/2 a.e. (cosine transform injective, m_l!=0), i.e.")
P("  1_C(u)+1_C(-u)=c in {0,1,2}: impossible for 0<c<1.  Numeric illustration below.")
# fine sphere grid, antipodally closed
nth, nph = 200, 400
xg, wg = leggauss(nth); ph = (np.arange(nph) + 0.5) * 2 * np.pi / nph
CS, PH = np.meshgrid(xg, ph, indexing='ij'); SN = np.sqrt(1 - CS**2)
U = np.stack([SN*np.cos(PH), SN*np.sin(PH), CS], -1).reshape(-1, 3)
WT = (np.repeat(wg, nph) / (2.0*nph))
nvec = np.array([0, 0, 1.0])
def mu_r_cell(cellmask_or_w, rhat):
    f = 4*np.maximum(U @ rhat, 0)
    return float(np.sum(WT * f * cellmask_or_w))
rng = np.random.default_rng(7)
rhats = rng.normal(size=(60, 3)); rhats /= np.linalg.norm(rhats, axis=1)[:, None]
for cc in (1.0, 2/3, 0.4):
    target = np.array([cc*(1 + r @ nvec)/2 for r in rhats])
    # candidate 1: deterministic hemisphere cell (c=1 works, c<1 cannot)
    hemi = (U @ nvec > 0).astype(float)
    e1 = np.max(np.abs(np.array([mu_r_cell(hemi, r) for r in rhats]) - target))
    # candidate 2: hemisphere thinned by an independent coin of bias c (NOT a function of content)
    e2 = np.max(np.abs(np.array([mu_r_cell(cc*hemi, r) for r in rhats]) - target))
    # candidate 3: best deterministic cell of the form {n.u > s} (cap) with area matched to c/2 from the hemisphere family
    best = 9
    for s in np.linspace(-0.99, 0.99, 199):
        cap = (U @ nvec > s).astype(float)
        e = np.max(np.abs(np.array([mu_r_cell(cap, r) for r in rhats[:20]]) - target[:20]))
        best = min(best, e)
    P(f"  c={cc:.4f}: max err hemisphere cell {e1:.3e}; hemisphere x independent coin(c) {e2:.3e}; best cap cell {best:.3e}")

# ---- K3: octahedral-only covariance
P("== K3 lattice-only (octahedral) covariance: readout-affine, positive, Born on all six axis readouts, not Born at generic n")
lam = 0.6; beta = 0.8
def h_q(u, q):
    return q[0]*u[:, 0]**3 + q[1]*u[:, 1]**3 + q[2]*u[:, 2]**3 - 0.5*(u @ q)
def fodd(u, q):
    return 2*lam*(u @ q) + beta*h_q(u, q)
def dens(u, q):
    fo = fodd(u, q); m = np.sum(WT*np.abs(fo))
    return np.abs(fo) + (1 - m) + fo, m   # f = even part (|f_odd|+slack) + f_odd: positive, mass 1
axes = [np.array(v, float) for v in ([1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])]
qs = rng.normal(size=(8, 3)); qs /= np.linalg.norm(qs, axis=1)[:, None]
maxaxis = 0; maxgen = 0; minf = 9; maxm = 0
for q in qs:
    f, m = dens(U, q); minf = min(minf, f.min()); maxm = max(maxm, m)
    for n in axes:
        p = float(np.sum(WT*f*((U @ n) > 0)))
        maxaxis = max(maxaxis, abs(p - (1 + lam*(q @ n))/2))
    for _ in range(10):
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        p = float(np.sum(WT*f*((U @ n) > 0)))
        maxgen = max(maxgen, abs(p - (1 + lam*(q @ n))/2))
P(f"  min density {minf:.3f} (>=0), max mean|f_odd| {maxm:.3f} (<=1); max |P - Born| on the six axis readouts {maxaxis:.2e} (grid error); at random n {maxgen:.3e}")
# octahedral covariance check: f_{Rq}(Ru) == f_q(u) for the 90-degree rotation about z and a 3-fold about (111)
def rotz(): return np.array([[0,-1,0],[1,0,0],[0,0,1.0]])
def r111(): return np.array([[0,0,1.0],[1,0,0],[0,1,0]])
cov = 0
for R in (rotz(), r111()):
    q = qs[0]; fo1 = fodd(U, q); fo2 = fodd(U @ R.T, R @ q)
    cov = max(cov, float(np.max(np.abs(fo1 - fo2))))
P(f"  covariance residual of f_odd under two cubic rotations: {cov:.2e}")
# affinity in q of the odd part (readout-level): fodd is linear in q
q1, q2 = qs[0], qs[1]
aff = float(np.max(np.abs(fodd(U, 0.3*q1+0.7*q2) - (0.3*fodd(U, q1)+0.7*fodd(U, q2)))))
P(f"  linearity (readout-level affinity) residual in q: {aff:.2e}")

# ---- K4: constant Fisher class and the flag
P("== K4 constant-Fisher ODE class; smoothness flag artifact")
th = np.linspace(0.05, np.pi-0.05, 400)
for kap in (1, 3, 5, 0.5):
    g = lambda x, k=kap: np.cos(k*x/2)**2
    I = (np.gradient(g(th), th)**2)/(g(th)*(1-g(th)))
    anti = np.max(np.abs(g(th)+g(np.pi-th)-1)); mono = bool(np.all(np.diff(g(th)) <= 1e-12))
    P(f"  g=cos^2(k*theta/2), k={kap}: I~{np.mean(I):.3f} (=k^2/4*... ) antipodal err {anti:.1e}, g(0)={g(0):.3f}, monotone={mono}")
g3 = lambda x: np.cos(1.5*x)**2
s0 = (g3(2e-3)-g3(1e-3))/1e-3
P(f"  T3-type slope used by hemi_test.py's smooth flag: {s0:.4e} (threshold 5e-3); exact g'(0)=0, g''(0)={-(9/2):.2f}")
open('k1_result.txt', 'w').write("\n".join(out))
