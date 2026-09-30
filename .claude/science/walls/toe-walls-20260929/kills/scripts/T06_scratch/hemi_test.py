#!/usr/bin/env python3
"""T06 test: measure typing of the Born wall (hemisphere readouts), Wootters scan, fixture check.

Pre-registered in PREREG.md (same folder). No repository file is read or edited.
Normalised Haar measure on S^2: dmu = dOmega/(4 pi). Density f is w.r.t. dmu, so int f dmu = 1.
Axisymmetric densities are functions f(t), t = u.q. A hemisphere readout is the event {n.u > 0},
n at angle theta from q.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import eval_legendre
from scipy.integrate import quad

RES = {}
NGL = 400
X, W = leggauss(NGL)


def gl(f, a, b):
    """Gauss-Legendre on [a,b] for a vectorised f."""
    if b <= a:
        return 0.0
    x = 0.5 * (b - a) * X + 0.5 * (b + a)
    return 0.5 * (b - a) * np.sum(W * f(x))


def hemi_axisym(f, theta):
    """int_{n.u>0} f(u.q) dmu(u), n at polar angle theta from q, 0<theta<pi.
    Polar coordinate s about q: t = cos s, dmu = sin s ds dphi /(4 pi).
    Fraction of phi with n.u>0 is arccos(clip(-A/B,-1,1))/pi, A=cos(theta)cos(s), B=sin(theta)sin(s)."""
    ct, st = np.cos(theta), np.sin(theta)

    def integrand(s):
        A = ct * np.cos(s)
        B = st * np.sin(s)
        with np.errstate(divide='ignore', invalid='ignore'):
            r = np.where(B > 1e-300, -A / B, np.where(A > 0, -np.inf, np.inf))
        frac = np.arccos(np.clip(r, -1.0, 1.0)) / np.pi
        return f(np.cos(s)) * frac * np.sin(s) / 2.0

    s1 = np.arctan(abs(ct) / st)  # |A| = B at s1 and pi - s1
    # RUN 2 FIX (numeric only): also split at s = pi/2, the kink/discontinuity of t_+^k densities
    pts = [0.0, s1, np.pi / 2, np.pi - s1, np.pi]
    pts = sorted(set(pts))
    return sum(gl(integrand, pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def leg_coeffs(f, lmax=15):
    """f(t) = sum a_l P_l(t) w.r.t. dmu (dmu -> dt/2 for axisymmetric); split at t=0 for kinks."""
    a = []
    for l in range(lmax + 1):
        g = lambda t: f(t) * eval_legendre(l, t)
        val = gl(g, -1, 0) + gl(g, 0, 1)
        a.append((2 * l + 1) / 2.0 * val)
    return np.array(a)


def c_l(l):
    return 0.5 * quad(lambda t: eval_legendre(l, t), 0, 1)[0]


out = []


def P(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


# ---------------- Part A: Funk-Hecke eigenvalues of the hemisphere transform ----------------
P("== A. hemisphere transform of P_l(u.q): numeric vs c_l P_l(cos theta)")
thetas = [0.3, 0.9, 1.5, 2.2, 2.9]
maxerr_odd = 0.0
maxerr_even = 0.0
for l in range(0, 10):
    err = 0.0
    for th in thetas:
        num = hemi_axisym(lambda t: eval_legendre(l, t), th)
        pred = c_l(l) * eval_legendre(l, np.cos(th))
        err = max(err, abs(num - pred))
    P(f"  l={l}: c_l={c_l(l): .8f} max|num-pred|={err:.2e}")
    if l % 2 == 0 and l >= 2:
        maxerr_even = max(maxerr_even, max(abs(hemi_axisym(lambda t: eval_legendre(l, t), th)) for th in thetas))
    maxerr_odd = max(maxerr_odd, err)
RES['A_max_num_pred_err'] = maxerr_odd
RES['A_even_l_ge2_max_abs_value'] = maxerr_even
P(f"  A: max |num-pred| = {maxerr_odd:.2e}; even l>=2 max |value| = {maxerr_even:.2e}")
RES['A_pass'] = bool(maxerr_odd < 1e-8 and maxerr_even < 1e-8)
P("  A PASS" if RES['A_pass'] else "  A FAIL")

# ---------------- Part B1: Kochen-Specker density ----------------
P("== B1. KS density f=4 t_+ : hemisphere probability vs cos^2(theta/2)")
fKS = lambda t: 4.0 * np.maximum(t, 0.0)
errKS = max(abs(hemi_axisym(fKS, th) - np.cos(th / 2) ** 2) for th in np.linspace(0.05, np.pi - 0.05, 25))
a = leg_coeffs(fKS, 15)
odd_l = [l for l in range(1, 16, 2)]
P("  Legendre coeffs odd l:", {l: float(np.round(a[l], 12)) for l in odd_l})
P("  Legendre coeffs even l:", {l: float(np.round(a[l], 12)) for l in range(0, 16, 2)})
P(f"  max |g_KS - cos^2(theta/2)| = {errKS:.2e}")
odd_hi = max(abs(a[l]) for l in odd_l if l >= 3)
RES['B1_err'] = errKS
RES['B1_odd_l_ge3_max_coeff'] = float(odd_hi)
RES['B1_pass'] = bool(errKS < 1e-8 and odd_hi < 1e-10 and abs(a[1] - 2.0) < 1e-10)
P("  B1 PASS" if RES['B1_pass'] else "  B1 FAIL")

# ---------------- Part B2: even perturbations invisible ----------------
P("== B2. even perturbations leave all hemisphere probabilities unchanged")
rng = np.random.default_rng(20260929)
# general (non-axisymmetric) check on the sphere via a symmetric quadrature: density = KS(q) + eps*E,
# E an even random quartic form minus its mean.  Use a product grid symmetric under u -> -u.
nth, nph = 400, 800
xg, wg = leggauss(nth)
ph = (np.arange(nph) + 0.5) * 2 * np.pi / nph
# Full sphere grid (cos s, phi); antipodal symmetric because xg symmetric and ph -> ph+pi is in the grid.
CS, PH = np.meshgrid(xg, ph, indexing='ij')
SN = np.sqrt(1 - CS ** 2)
U = np.stack([SN * np.cos(PH), SN * np.sin(PH), CS], axis=-1)  # (nth,nph,3)
WT = (wg[:, None] * np.ones(nph)[None, :]) / (2.0 * nph)  # sums to 1
q = np.array([0.0, 0.0, 1.0])
def rand_even_form(deg=4):
    T = rng.normal(size=(3,) * deg)
    idx = np.einsum('...i,...j,...k,...l,ijkl->...', U, U, U, U, T)
    return idx - np.sum(WT * idx)
E = rand_even_form()
dens0 = 4.0 * np.maximum(U @ q, 0.0)
eps = 0.5
dens1 = dens0 + eps * E
dens1_min = float(dens1.min())
maxdiff = 0.0
for _ in range(20):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    h0 = np.sum(WT * dens0 * ((U @ n) > 0))
    h1 = np.sum(WT * dens1 * ((U @ n) > 0))
    maxdiff = max(maxdiff, abs(h1 - h0))
P(f"  perturbed density min={dens1_min:.3f} (positivity not needed for the identity); total mass={np.sum(WT*dens1):.12f}")
P(f"  max |H(f+eps E) - H(f)| over 20 random readouts = {maxdiff:.2e}")
RES['B2_maxdiff'] = float(maxdiff)
RES['B2_pass'] = bool(maxdiff < 1e-8)
P("  B2 PASS" if RES['B2_pass'] else "  B2 FAIL")

# ---------------- Part B3: dipole-only density ----------------
P("== B3. dipole-only density 1+a.u : positivity and Born purity")
best = None
for amag in np.linspace(0, 1.4, 141):
    posmin = 1 - amag
    if posmin >= -1e-12:
        best = amag
purity_from_hemi = 4 * (hemi_axisym(lambda t: 1 + best * t, 1e-6) - 0.5) / 1.0  # (1+r)/2 at theta~0 => r = 2(H-1/2)
r_born_equiv = 2 * (hemi_axisym(lambda t: 1 + best * t, 1e-6) - 0.5)
P(f"  largest |a| with density >= 0: {best:.3f}; hemisphere probability at n=q: {hemi_axisym(lambda t: 1+best*t,1e-6):.6f}")
P(f"  equivalent Born purity r = 2(H-1/2) = {r_born_equiv:.6f} (Born pure state would need 1)")
RES['B3_max_a'] = float(best)
RES['B3_max_born_purity'] = float(r_born_equiv)
RES['B3_pass'] = bool(abs(best - 1.0) < 1e-9 and abs(r_born_equiv - 0.5) < 1e-4)
P("  B3 PASS" if RES['B3_pass'] else "  B3 FAIL")

# ---------------- Part B4: Gibbs kernels ----------------
P("== B4. Gibbs kernels e^{beta t}: odd multipoles and deviation from an affine hemisphere law")
ths = np.linspace(0.05, np.pi - 0.05, 40)
rows = []
for beta in [0.5, 1.0, 2.0, 4.0]:
    Z = np.sinh(beta) / beta
    f = lambda t, b=beta, Z=Z: np.exp(b * t) / Z
    a = leg_coeffs(f, 15)
    Wl = {l: a[l] ** 2 / (2 * l + 1) for l in range(1, 16, 2)}
    frac_hi = sum(v for l, v in Wl.items() if l >= 3) / sum(Wl.values())
    g = np.array([hemi_axisym(f, th) for th in ths])
    A = np.stack([np.ones_like(ths), np.cos(ths)], axis=1)
    coef, *_ = np.linalg.lstsq(A, g, rcond=None)
    dev = float(np.max(np.abs(g - A @ coef)))
    rows.append((beta, frac_hi, dev, coef[1]))
    P(f"  beta={beta}: odd-weight fraction at l>=3 = {frac_hi:.4f}; max deviation from best affine g = {dev:.4f}; fitted slope {coef[1]:.4f}")
RES['B4_rows'] = [tuple(map(float, r)) for r in rows]
# RUN 2: pass rule follows the pre-registered PROSE (nonzero and increasing with beta), not the run-1 code thresholds
RES['B4_pass'] = bool(all(r[1] > 0 and r[2] > 0 for r in rows) and all(rows[i][1] < rows[i+1][1] and rows[i][2] < rows[i+1][2] for i in range(len(rows)-1)))
P("  B4 PASS" if RES['B4_pass'] else "  B4 FAIL")

# ---------------- Part B5: power kernels have zero forcing ----------------
P("== B5. power kernels f_k = 2(k+1) t_+^k: positivity, covariance, antipodal normalisation, g(0)=1 all hold; Born only at k=1")
gk = {}
b5 = []
for k in [0, 1, 2, 3, 4]:
    f = lambda t, k=k: 2 * (k + 1) * np.where(t > 0, np.maximum(t, 0.0) ** k, 0.0)
    mass = gl(lambda t: f(t) / 2.0, 0, 1)  # dmu -> dt/2
    g = np.array([hemi_axisym(f, th) for th in ths])
    born = np.cos(ths / 2) ** 2
    anti = max(abs(hemi_axisym(f, th) + hemi_axisym(f, np.pi - th) - 1) for th in [0.4, 1.0, 1.4])
    dev = float(np.max(np.abs(g - born)))
    g0 = hemi_axisym(f, 1e-7)
    gk[k] = g
    b5.append((k, mass, g0, anti, dev))
    P(f"  k={k}: mass={mass:.10f} g(0)={g0:.8f} antipodal-sum error={anti:.1e} max|g-Born|={dev:.4f}")
RES['B5_rows'] = [tuple(map(float, r)) for r in b5]
RES['B5_pass'] = bool(all(abs(r[1] - 1) < 1e-9 and abs(r[2] - 1) < 1e-4 and r[3] < 1e-8 for r in b5)
                      and all(r[4] > 1e-3 for r in b5 if r[0] != 1) and b5[1][4] < 1e-8)
P("  B5 PASS" if RES['B5_pass'] else "  B5 FAIL")

# ---------------- Part B6: preparation contextuality footprint ----------------
P("== B6. KS densities of I/2 from decompositions {+-z} and {+-x}")
dz = 0.5 * (4 * np.maximum(U @ np.array([0, 0, 1.0]), 0) + 4 * np.maximum(U @ np.array([0, 0, -1.0]), 0))
dx = 0.5 * (4 * np.maximum(U @ np.array([1.0, 0, 0]), 0) + 4 * np.maximum(U @ np.array([-1.0, 0, 0]), 0))
l1 = float(np.sum(WT * np.abs(dz - dx)))
mh = 0.0
mh_grid = 0.0
def gKS(th):
    th = min(max(th, 1e-9), np.pi - 1e-9)
    return hemi_axisym(fKS, th)
for _ in range(50):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    mh_grid = max(mh_grid, abs(np.sum(WT * dz * ((U @ n) > 0)) - 0.5), abs(np.sum(WT * dx * ((U @ n) > 0)) - 0.5))
    # RUN 2: exact 1D evaluation (each decomposition is a mixture of two axisymmetric KS densities)
    tz = np.arccos(np.clip(n @ np.array([0, 0, 1.0]), -1, 1)); tx = np.arccos(np.clip(n @ np.array([1.0, 0, 0]), -1, 1))
    pz = 0.5 * (gKS(tz) + gKS(np.pi - tz)); px = 0.5 * (gKS(tx) + gKS(np.pi - tx))
    mh = max(mh, abs(pz - 0.5), abs(px - 0.5))
P(f"  L1 distance between the two content densities = {l1:.4f} (2*sqrt2-2 = {2*np.sqrt(2)-2:.4f})")
P(f"  max |hemisphere prob - 1/2| over 50 readouts: exact 1D = {mh:.2e}; 2D grid (indicator discontinuity) = {mh_grid:.2e}")
RES['B6_l1'] = l1
RES['B6_hemi_dev'] = float(mh)
RES['B6_pass'] = bool(l1 > 0.1 and mh < 1e-8)
P("  B6 PASS" if RES['B6_pass'] else "  B6 FAIL")

# ---------------- Part C: Wootters / constant Fisher information scan ----------------
P("== C. constant Fisher information scan, I(theta)=g'^2/(g(1-g)) on theta in [0.05, pi-0.05]")
th = np.linspace(0.05, np.pi - 0.05, 600)
h = 1e-5


def fisher(gfun):
    g = gfun(th)
    dg = (gfun(th + h) - gfun(th - h)) / (2 * h)
    return dg ** 2 / (g * (1 - g))


def d1(gfun, t0):
    return (gfun(t0 + h) - gfun(t0 - h)) / (2 * h)


fams = {}
for lam in [0.5, 0.8, 0.95, 1.0]:
    fams[f"Born lam={lam}"] = lambda t, lam=lam: (1 + lam * np.cos(t)) / 2
for beta in [0.5, 1.0, 2.0]:
    fams[f"binary Gibbs tanh beta={beta}"] = lambda t, b=beta: (1 + np.tanh(b * np.cos(t))) / 2
fams["lane witness (1+t^3)/2"] = lambda t: (1 + np.cos(t) ** 3) / 2
fams["lane witness (1+t)/2+t(1-t^2)/8"] = lambda t: (1 + np.cos(t)) / 2 + np.cos(t) * (1 - np.cos(t) ** 2) / 8
fams["T3-type cos^2(3 theta/2)"] = lambda t: np.cos(1.5 * t) ** 2
fams["cone cos^2(theta/4+pi/8)"] = lambda t: np.cos(t / 4 + np.pi / 8) ** 2
for k in [0, 2, 3, 4]:
    # measure-derived power kernels, interpolated from the exact quadrature grid
    gvals = np.array([hemi_axisym(lambda x, k=k: 2 * (k + 1) * np.where(x > 0, np.maximum(x, 0.0) ** k, 0.0), tt) for tt in np.linspace(0.02, np.pi - 0.02, 300)])
    grid = np.linspace(0.02, np.pi - 0.02, 300)
    fams[f"measure power kernel k={k}"] = lambda t, grid=grid, gvals=gvals: np.interp(t, grid, gvals)
c_rows = []
constant_smooth_monotone = []
for name, gf in fams.items():
    I = fisher(gf)
    ratio = float(I.max() / I.min())
    s0 = d1(gf, 1e-3 + 0.0)  # slope near theta=0 (theta cannot be negative; use one-sided)
    s0 = (gf(np.array([2e-3])) - gf(np.array([1e-3])))[0] / 1e-3
    s1 = (gf(np.array([np.pi - 1e-3])) - gf(np.array([np.pi - 2e-3])))[0] / 1e-3
    smooth = bool(abs(s0) < 5e-3 and abs(s1) < 5e-3)
    gg = gf(th)
    mono = bool(np.all(np.diff(gg) < 1e-9) or np.all(np.diff(gg) > -1e-9))
    anti = float(np.max(np.abs(gf(th) + gf(np.pi - th) - 1)))
    c_rows.append((name, ratio, smooth, mono, anti))
    P(f"  {name:38s} Imax/Imin={ratio:10.4g}  C1-smooth={smooth!s:5}  monotone={mono!s:5}  antipodal-err={anti:.1e}")
    if ratio < 1 + 1e-6 and smooth and mono and anti < 1e-6:
        constant_smooth_monotone.append(name)
P("  constant-I, C1, monotone, antipodal-normalised members:", constant_smooth_monotone)
RES['C_rows'] = [(n, float(r), bool(s), bool(m), float(a)) for n, r, s, m, a in c_rows]
RES['C_constant_smooth_monotone'] = constant_smooth_monotone
RES['C_pass'] = bool(constant_smooth_monotone == ["Born lam=1.0"])
P("  C PASS" if RES['C_pass'] else "  C FAIL")
# side facts about the ODE solutions
kappa_half = fams["cone cos^2(theta/4+pi/8)"]
P(f"  cone member: I const={fisher(kappa_half).mean():.5f}, slope at theta->0 = {(kappa_half(np.array([2e-3]))-kappa_half(np.array([1e-3])))[0]/1e-3:.4f} (nonzero => cone singularity on the sphere)")
t3 = fams["T3-type cos^2(3 theta/2)"]
P(f"  T3-type member: I const={fisher(t3).mean():.5f} (=9/ (kappa^2=9)?), monotone={c_rows[[r[0] for r in c_rows].index('T3-type cos^2(3 theta/2)')][3]}")

# ---------------- Part F: fixture vs records-as-fields ----------------
P("== F. finite fixture mu_A(1|n)=(n+1)/8 vs Heisenberg thermal records-as-fields (six binary neighbours)")
ns = np.arange(7)
mu_A = (ns + 1) / 8.0
bs = np.linspace(0.0, 3.0, 30001)
best_b, best_err = None, 9.0
for b in bs:
    p = (1 + np.tanh(b * (2 * ns - 6))) / 2
    e = np.max(np.abs(p - mu_A))
    if e < best_err:
        best_err, best_b = e, b
p = (1 + np.tanh(best_b * (2 * ns - 6))) / 2
P(f"  best b=beta|J| (min over max error) = {best_b:.4f}; min max-error = {best_err:.4f}")
P("  n:", list(ns), "mu_A:", np.round(mu_A, 4).tolist(), "thermal:", np.round(p, 4).tolist())
# same with least squares
best_b2, best_r = None, 9.0
for b in bs:
    p2 = (1 + np.tanh(b * (2 * ns - 6))) / 2
    r = np.sqrt(np.mean((p2 - mu_A) ** 2))
    if r < best_r:
        best_r, best_b2 = r, b
P(f"  least-squares b = {best_b2:.4f}, rms = {best_r:.4f}")
RES['F_min_max_error'] = float(best_err)
RES['F_pass'] = bool(best_err >= 0.02)
P("  F PASS (fixture is not a records-as-fields law)" if RES['F_pass'] else "  F FAIL")

P("== SUMMARY", {k: v for k, v in RES.items() if k.endswith('_pass')})
import json
with open(__file__.replace('hemi_test.py', 'hemi_result.json'), 'w') as fh:
    json.dump(RES, fh, indent=1, default=str)
with open(__file__.replace('hemi_test.py', 'hemi_result.txt'), 'w') as fh:
    fh.write("\n".join(out))
