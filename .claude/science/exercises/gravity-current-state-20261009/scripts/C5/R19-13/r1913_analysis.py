"""R19-13 analysis.
(A) 3D plane insertion, scalar: per-site best radius-R isometric insertion cost dE3(R) = BZ average over transverse
    q of the per-chain optimum c(M_q, R) (r1913_scan_*.out), M_q^2 = m^2 + 4 sin^2(qy/2) + 4 sin^2(qz/2).
(B) Rigorous lower bound (any operation on the slab, any state): per chain with gap M_q,
        dE_q >= M_q * D_T^2 >= M_q * (Delta<O>)^2 / 4,
    O = cos(lam (phi_bL - phi_bR)), old separation d = 2R+1, new separation d+1, lam optimised.
(C) Thresholds at a = l_P: persistent net excitation 3 dE/a^3 per Hubble time < rho_L  <=> dE < rho_L/3;
    registered formula 3H dE tau_ins / a^3 < rho_L  <=> dE * tau_ins < rho_L/(3H), tau_ins >= R (Lieb-Robinson).
"""
import glob, re, numpy as np
from scipy import integrate, special
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from r1913_lib import chain_corr

H0 = 67.4 / 3.0857e19 * 5.391e-44; rhoL = 0.685 * 3 * H0 ** 2 / (8 * np.pi)    # RECALLED inputs, as R19-10
thr_persist = rhoL / 3
thr_reg = rhoL / (3 * H0)
print('rho_L = %.4e ; persistent threshold dE < %.3e ; registered threshold dE*tau < %.3e' % (rhoL, thr_persist, thr_reg))

def load(pattern):
    tab = {}
    for f in glob.glob(pattern):
        R = int(re.search(r'_R(\d+)\.out', f).group(1))
        d = np.loadtxt(f)
        tab[R] = (d[:, 0], d[:, 1])
    return tab
main = load('r1913_scan_R*.out'); gap = load('r1913_scan_gap_R*.out')
FLOOR = 5e-14

def cfun(R, use_gap=False):
    M, c = main[R]
    if use_gap and R in gap:
        Mg, cg = gap[R]
        keep = M < 0.99
        M = np.concatenate([M[keep], Mg]); c = np.concatenate([c[keep], cg])
    o = np.argsort(M); M = M[o]; c = np.clip(c[o], FLOOR, None)
    sp = CubicSpline(np.log(M), np.log(c))
    def f(Mq):
        Mq = np.asarray(Mq)
        out = np.exp(sp(np.log(np.clip(Mq, M[0], M[-1]))))
        out = np.where(Mq > M[-1], FLOOR, out)
        return np.where(out <= 1.0001 * FLOOR, 0.0, out)
    return f

# graded midpoint grid on [0, pi]^2
NQ = 500
t = (np.arange(NQ) + 0.5) / NQ; p = 3.0
qv = np.pi * t ** p; wv = np.pi * p * t ** (p - 1) / NQ / np.pi
QY, QZ = np.meshgrid(qv, qv, indexing='ij'); WW = np.outer(wv, wv)
S = 4 * np.sin(QY / 2) ** 2 + 4 * np.sin(QZ / 2) ** 2
print('quadrature weight sum = %.10f' % WW.sum())

print('\n(A) 3D scalar plane insertion: best radius-R isometric insertion, cost per inserted site (upper bound = explicit Gaussian isometry)')
res = {}
for m in (0.0, 0.1, 0.3, 1.0):
    Ms = np.sqrt(m * m + S)
    row = []
    for R in sorted(main):
        f = cfun(R, use_gap=(m >= 1.0))
        val = (WW * f(Ms)).sum()
        # IR tail below the smallest tabulated M (only m=0): bracket [0, area * c(Mmin)*2]
        row.append((R, val))
    res[m] = row
    print('  m=%.1f: ' % m + '  '.join('R=%d:%.3e' % rv for rv in row))
R0 = np.array([r for r, _ in res[0.0]]); V0 = np.array([v for _, v in res[0.0]])
print('  m=0 local exponents -dln dE/dln R:', '  '.join('%d-%d:%.2f' % (R0[i], R0[i + 1], -np.log(V0[i + 1] / V0[i]) / np.log(R0[i + 1] / R0[i])) for i in range(len(R0) - 1)))
sel = R0 >= 10
pf = np.polyfit(np.log(R0[sel]), np.log(V0[sel]), 1)
print('  m=0 fit R>=10: dE3 = %.3e * R^%.3f' % (np.exp(pf[1]), pf[0]))
K5 = V0 * R0 ** 5
print('  m=0 dE3*R^5:', '  '.join('R=%d:%.3e' % (r, k) for r, k in zip(R0, K5)))
R1 = np.array([r for r, _ in res[1.0]]); V1 = np.array([v for _, v in res[1.0]])
print('  m=1 successive ratios dE3(R)/dE3(R+1):', '  '.join('%d:%.1f' % (R1[i], V1[i] / V1[i + 1]) for i in range(len(R1) - 1) if R1[i + 1] - R1[i] == 1 and V1[i + 1] > 0))
kap1 = np.arccosh(1 + 0.5)
print('  chain decay rate kappa(M=1) = arccosh(1.5) = %.4f ; exp(4 kappa) = %.1f' % (kap1, np.exp(4 * kap1)))

# (B) lattice lower bound
def LB_chain(M, R):
    Gx, Gp, e0 = chain_corr(float(M), 2 * R + 2)
    d = 2 * R + 1
    a = Gx[0] - Gx[d]; b = Gx[0] - Gx[d + 1]
    if b - a < 1e-13:      # drop unresolved terms: the bound stays a bound (sum of nonnegative terms)
        return 0.0
    u = np.log(b / a) / (b - a)
    Dl = np.exp(-u * a) - np.exp(-u * b)
    return M * Dl * Dl / 4

print('\n(B) rigorous lower bound per inserted site (any slab operation), lattice correlators, BZ average')
LBres = {}
for m in (0.0, 1.0):
    out = []
    for R in (1, 2, 4, 8, 16, 32, 64, 128, 256):
        # integrate over M_q via the radial variable: use a 1D table in M then the 2D grid
        Mtab = np.logspace(np.log10(max(m, 1e-6) if m > 0 else 1e-6), np.log10(np.sqrt(m * m + 8)), 160)
        ltab = np.array([LB_chain(Mi, R) for Mi in Mtab])
        Ms = np.sqrt(m * m + S)
        # piecewise-linear in ln M, and zero below the first node (keeps it a lower bound up to interpolation error)
        vals = np.interp(np.log(Ms), np.log(Mtab), ltab, left=0.0, right=0.0)
        lb = (WW * vals).sum()
        out.append((R, lb))
    LBres[m] = out
    print('  m=%.1f: ' % m + '  '.join('R=%d:%.3e' % rv for rv in out))
for (R, lb) in LBres[0.0]:
    ub = dict(res[0.0]).get(R)
    if ub:
        print('    m=0 R=%d: lower bound %.3e <= best isometry %.3e (ratio %.2f)' % (R, lb, ub, ub / lb))
for (R, lb) in LBres[1.0]:
    ub = dict(res[1.0]).get(R)
    if ub:
        print('    m=1 R=%d: lower bound %.3e <= best isometry %.3e (ratio %.2f)' % (R, lb, ub, ub / lb))

# (C) continuum asymptotic of the lower bound (M << 1 regime, small-q DOS 1/(4 pi) in eps = M^2)
#   delta = G(d)-G(d+1) -> (1/pi)[K0(Md) - K0(M(d+1))],  a = G0 - G(d) -> (1/pi)[ell(M) - K0(Md)], ell = pi*G0_lattice
Mt = np.logspace(-6, -1, 11)
ellc = np.array([np.pi * chain_corr(float(Mi), 0)[0][0] + 0.5 * np.log(Mi) for Mi in Mt])
print('\n(C) pi*G0(M) + (1/2) ln M (should tend to a constant c0):', ' '.join('%.6f' % v for v in ellc))
c0 = ellc[0]
def LB_cont(d, m=0.0):
    """Continuum-asymptotic evaluation of the lattice lower bound (M << 1): G(n) -> K0(Mn)/(2 pi),
    delta = G(d)-G(d+1) = (1/2pi) int_{Md}^{M(d+1)} K1 ~ M K1(M(d+1/2))/(2 pi) (midpoint, rel. error O(M^2)),
    a = G0 - G(d) = (c0 - ln(M)/2)/pi - K0(Md)/(2 pi); optimised lambda gives Delta = exp(-u a) delta/b."""
    def integrand(lnM):
        M = np.exp(lnM)
        dl = M * special.k1(M * (d + 0.5)) / (2 * np.pi)
        a = (-0.5 * np.log(M) + c0) / np.pi - special.k0(M * d) / (2 * np.pi)
        if not (dl > 0 and a > 0):
            return 0.0
        r = dl / a
        ua = np.log1p(r) / r
        Dl = np.exp(-ua) * dl / (a + dl)
        return (1 / (4 * np.pi)) * 2 * M ** 3 * Dl * Dl / 4      # d eps = 2 M^2 d lnM, times M Dl^2 / 4
    lo = np.log(max(m, 1e-4 / d)); hi = np.log(min(m + 80.0 / d, 0.5))
    if hi <= lo:
        return 0.0
    return integrate.quad(integrand, lo, hi, limit=400, epsrel=1e-9, epsabs=0)[0]
for (R, lb) in LBres[0.0]:
    if R >= 4:
        print('  R=%d: lattice LB %.4e ; continuum asymptotic %.4e (ratio %.3f)' % (R, lb, LB_cont(2 * R + 1), lb / LB_cont(2 * R + 1)))

def solve_R(fun, thr, lo=1.0, hi=1e40):
    g = lambda lr: np.log(fun(np.exp(lr))) - np.log(thr)
    return np.exp(brentq(g, np.log(lo), np.log(hi), xtol=1e-6))
print('\n(D) required R (proved lower bound on the requirement, evaluated with the continuum asymptotic)')
for m, lab in ((0.0, 'massless scalar'), (1e-17, 'scalar m a = 1e-17 (SM-like)'), (1e-10, 'scalar m a = 1e-10')):
    f_p = lambda R: LB_cont(2 * R + 1, m)
    try:
        Rp = solve_R(f_p, thr_persist, 30, 1e35)
    except Exception as e:
        Rp = float('nan')
    f_r1 = lambda R: LB_cont(2 * R + 1, m) * 1.0
    f_rR = lambda R: LB_cont(2 * R + 1, m) * R
    try:
        Rr1 = solve_R(f_r1, thr_reg, 30, 1e35); RrR = solve_R(f_rR, thr_reg, 30, 1e35)
    except Exception as e:
        Rr1 = RrR = float('nan')
    print('  %s: persistent (dE<rho_L/3): R > %.2e a ; registered with tau_ins = 1 t_P: R > %.2e a ; with tau_ins = R t_P: R > %.2e a' % (lab, Rp, Rr1, RrR))
    if m == 0.0:
        print('     photon (2 transverse massless scalars, suggested identification): persistent R > %.2e a' % solve_R(lambda R: 2 * LB_cont(2 * R + 1), thr_persist, 30, 1e35))

# central estimates from the computed best isometry (m=0 fit), suggested extrapolation
A5, p5 = np.exp(pf[1]), pf[0]
print('\n(E) central estimate from the explicit-isometry fit dE3 = %.3e R^%.3f (suggested extrapolation):' % (A5, p5))
print('  persistent: R ~ %.2e a ; registered tau=R: R ~ %.2e a ; photon x2 persistent: R ~ %.2e a' % (
    (thr_persist / A5) ** (1 / p5), (thr_reg / A5) ** (1 / (p5 + 1)), (thr_persist / (2 * A5)) ** (1 / p5)))
# gapped m=1: exponential extrapolation from the last two reliable R
r1 = [(r, v) for r, v in res[1.0] if v > 1e-12]
(ra, va), (rb, vb) = r1[-2], r1[-1]
rate = np.log(va / vb) / (rb - ra)
Rp1 = rb + np.log(vb / thr_persist) / rate
print('  m=1 (rate %.3f per site from R=%d,%d): persistent R ~ %.1f a ; registered (tau=R) R ~ %.1f a' % (rate, ra, rb, Rp1, rb + np.log(vb * rb / thr_reg) / rate))
# mass needed for R <= 10 to work (gapped chain decay 4*kappa(m), prefactor from m=1 at R=10 scale): suggested
for thrname, thr in (('persistent', thr_persist), ('registered tau=10', thr_reg / 10)):
    kap = np.log(1.0 / thr) / 40.0
    print('  %s with R=10: needs 4*kappa*10 >~ ln(1/thr) -> kappa >~ %.2f -> m a >~ %.1f (suggested, prefactor ~1)' % (thrname, kap, np.sqrt(2 * np.cosh(kap) - 2)))
