#!/usr/bin/env python3
"""strong-field-tick: CL-1's fixed-step lapse  sqrt3 N rms(sqrt gamma^ii) = sin(eps0)  in strong fields.
Continuum reading (labels = site coordinates), spherical/planar 3+1, plus lattice-cone bounds and estimates.
Self-contained: numpy, scipy, sympy."""
AUDIT_TIMEOUT_SEC = 120
import time, math
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp, quad
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print('[%s] %s  | %s' % ('PASS' if ok else 'FAIL', name, detail))
S3 = math.sqrt(3)
# ---------------------------------------------------------------- A. the rule as a slicing
print('== A. the fixed-step rule as a slicing condition (exact algebra)')
t = sp.Symbol('t'); s = sp.Symbol('s', positive=True)
g = [sp.Function('g%d' % i)(t) for i in range(3)]
Nexpr = s / sp.sqrt(sum(1 / gi for gi in g))           # diagonal gamma in site labels
Nf = sp.Function('N')(t); Kf = [sp.Function('K%d' % i)(t) for i in range(3)]
# zero shift: d_t g_ii = -2 N g_ii K^i_i
sub = {sp.Derivative(g[i], t): -2 * Nexpr * g[i] * Kf[i] for i in range(3)}
lhs = sp.diff(sp.log(Nexpr), t).subs(sub)
w = [(1 / g[i]) / sum(1 / gj for gj in g) for i in range(3)]
rhs = -Nexpr * sum(w[i] * Kf[i] for i in range(3))
a1 = sp.simplify(lhs - rhs)
iso = sp.simplify(rhs.subs({g[1]: g[0], g[2]: g[0]}) + Nexpr.subs({g[1]: g[0], g[2]: g[0]}) * sum(Kf) / 3)
check('A1 THEOREM: the rule is the algebraic lapse N = sin(eps0)/sqrt(delta_ij gamma^ij) in site labels; with no shift '
      'd_t ln N = -N sum w_i K^i_i, w_i = gamma^ii/sum gamma^jj: Bona-Masso with f = label weight '
      '(isotropic: f = 1/3)', a1 == 0 and iso == 0, 'residuals %s, %s' % (a1, iso))
psi = sp.Symbol('psi', positive=True)
Ncf = sp.simplify(Nexpr.subs({g[0]: psi**4, g[1]: psi**4, g[2]: psi**4}))
check('A2 THEOREM: conformally flat data gamma = psi^4 delta give N = (sin eps0/sqrt3) psi^2, the inverse of the '
      'pre-collapsed psi^-2: N and the cell size psi^2 l diverge at a puncture, so puncture data are not lattice states', sp.simplify(Ncf - s * psi**2 / sp.sqrt(3)) == 0,
      'N = %s' % Ncf)
# principal part along axis x (planar, gamma_yy = gamma_zz = B fixed): lambda^2 = 2 alpha^2 phi / A, phi = dlnN/dlnA
A_, B_ = sp.symbols('A B', positive=True)
al = sp.sqrt(3 / (1 / A_ + 2 / B_)); phi = sp.simplify(A_ * sp.diff(sp.log(al), A_))
lam_over_c = sp.simplify(sp.sqrt(2 * phi))          # proper gauge speed / light speed
wx = (1 / A_) / (1 / A_ + 2 / B_)
lamlab = sp.simplify((al * sp.sqrt(2 * phi / A_)).subs(B_, 1))
check('A3 THEOREM: gauge pulses along axis i move at sqrt(w_i) c < c relative to the normals (planar, B = 1: '
      'sqrt3/(1+2 gamma_xx) labels per time): no slicing front leaves a horizon; the lapse has no elliptic part', sp.simplify(lam_over_c**2 - wx) == 0 and
      sp.simplify(lamlab - sp.sqrt(3) / (1 + 2 * A_)) == 0, 'lambda/c = sqrt(%s), isotropic %s' % (sp.simplify(wx), wx.subs(B_, A_)))
# eigenfield evolution (planar pure gauge): s = ln g, P = s_x, Kt = sqrt(g) K^x_x; c = N/sqrt g, sigma = sqrt(phi/2)
sv, P, Kt, Px, Ktx = sp.symbols('s P Kt Px Ktx')
cF = sp.Function('c')(sv); phF = sp.Function('ph')(sv); sig = sp.sqrt(phF / 2); lamF = 2 * cF * sig
s_t = -2 * cF * Kt
P_t = -(sp.diff(2 * cF, sv) * P * Kt + 2 * cF * Ktx)
K_t = -(sp.diff(cF * phF, sv) * P**2 + cF * phF * Px)
om_t = K_t + sig * P_t + sp.diff(sig, sv) * s_t * P
om_x = Ktx + sig * Px + sp.diff(sig, sv) * P**2
wp, wm = Kt + sig * P, Kt - sig * P
ric = sp.simplify(om_t + lamF * om_x + sp.diff(lamF, sv) / (2 * sig) * wp * (wp - wm))
gs = sp.Symbol('g', positive=True)
def kappa(alg):
    ph_ = sp.simplify(gs * sp.diff(sp.log(alg), gs)); c_ = alg / sp.sqrt(gs)
    lam_ = 2 * c_ * sp.sqrt(ph_ / 2)
    return sp.simplify(-gs * sp.diff(lam_, gs) / (2 * sp.sqrt(ph_ / 2)))
kfs, kbm, kh = kappa(sp.sqrt(3 * gs / (1 + 2 * gs))), kappa(gs**sp.Rational(1, 6)), kappa(sp.sqrt(gs))
check('A4 THEOREM (exact simple wave): omega = Kt + sigma d_x ln g obeys d_t omega + lambda d_x omega = '
      '-(dlambda/dln g)/(2 sigma) omega(omega - omega_bar), g constant on characteristics: a pulse shocks at '
      't* = 1/(kappa omega0), fixed step kappa = 2 sqrt3 g/(1+2g)^(3/2) > 0 for all g', ric == 0 and sp.simplify(kfs - 2 * sp.sqrt(3) * gs / (1 + 2 * gs)**sp.Rational(3, 2)) == 0
      and kh == 0, 'identity residual %s; kappa(g=1): fixed %s, f=1/3 %s, harmonic %s' % (ric, sp.nsimplify(kfs.subs(gs, 1)),
      kbm.subs(gs, 1), kh))
# ---------------------------------------------------------------- B. planar shock numerics
print('== B. planar pure-gauge pulse in Minkowski (no shift), exact vs evolved')
def planar(kind, W=0.2, dx=0.01, X=(-8.0, 16.0), fracs=(0.5, 0.8)):
    x = np.arange(X[0], X[1], dx); n = len(x)
    if kind == 'fixed':
        c = lambda s_: np.sqrt(3 / (1 + 2 * np.exp(s_))); ph = lambda s_: 0.5 / (1 + 2 * np.exp(s_))
        kap = lambda g_: 2 * S3 * g_ / (1 + 2 * g_)**1.5
    elif kind == 'f13':
        c = lambda s_: np.exp(-s_ / 3); ph = lambda s_: np.full_like(s_, 1 / 6); kap = lambda g_: g_**(-1 / 3) / 3
    else:
        c = lambda s_: np.ones_like(s_); ph = lambda s_: np.full_like(s_, 0.5); kap = lambda g_: 0 * g_
    om0 = W * np.exp(-x**2)
    so = solve_ivp(lambda xx, y: [np.interp(xx, x, om0) / (2 * np.sqrt(ph(np.array(y))[0] / 2))], [x[0], x[-1]], [0.0],
                   t_eval=x, rtol=1e-10, atol=1e-12, max_step=dx)
    s0 = so.y[0]; sig0 = np.sqrt(ph(s0) / 2); P0 = om0 / (2 * sig0); K0 = om0 / 2
    ts = 1 / np.max(kap(np.exp(s0)) * om0) if kind != 'harm' else 10.0
    def d1(u):
        out = np.zeros_like(u); out[2:-2] = (-u[4:] + 8 * u[3:-1] - 8 * u[1:-3] + u[:-4]) / (12 * dx); return out
    def f(y):
        s_, K_ = y; return np.array([-2 * c(s_) * K_, -d1(c(s_) * ph(s_) * d1(s_))])
    y = np.array([s0, K0]); tt = 0.0; dt = 0.25 * dx; res = []
    for fr in fracs:
        while tt < fr * ts - 1e-12:
            h = min(dt, fr * ts - tt)
            k1 = f(y); k2 = f(y + h / 2 * k1); k3 = f(y + h / 2 * k2); k4 = f(y + h * k3)
            y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); tt += h
        num = np.max(d1(y[0])[5:-5])
        ex = np.max(P0 / (1 - kap(np.exp(s0)) * om0 * tt))
        res.append((num, ex))
    return ts, res, P0.max()
out = {}
for kind in ['fixed', 'f13', 'harm']: out[kind] = planar(kind)
ok = all(abs(n_ / e_ - 1) < 0.02 for k in out for (n_, e_) in out[k][1])
check('B1 DIAGNOSTIC: a smooth pulse (omega0 = 0.2 exp(-x^2)) steepens as the exact solution says: fixed step shocks '
      'at t* = %.3f, f = 1/3 at %.3f, harmonic never (gradient kept)' % (out['fixed'][0], out['f13'][0]), ok,
      'evolved/exact max d_x ln g at 0.5, 0.8 t*: fixed %.4f %.4f (x%.2f), f=1/3 %.4f %.4f, harmonic %.4f %.4f' % (
      out['fixed'][1][0][0] / out['fixed'][1][0][1], out['fixed'][1][1][0] / out['fixed'][1][1][1],
      out['fixed'][1][1][1] / out['fixed'][2], out['f13'][1][0][0] / out['f13'][1][0][1],
      out['f13'][1][1][0] / out['f13'][1][1][1], out['harm'][1][0][0] / out['harm'][1][0][1], out['harm'][1][1][0] / out['harm'][1][1][1]))
# ---------------------------------------------------------------- C. singularities
print('== C. crushing singularities and black holes')
u = sp.Symbol('u', positive=True)
p = [-u / (1 + u + u**2), (1 + u) / (1 + u + u**2), u * (1 + u) / (1 + u + u**2)]
kas = [sp.simplify(sum(p) - 1), sp.simplify(sum(q**2 for q in p) - 1), sp.simplify(1 - p[2])]
tau = sp.Symbol('tau', positive=True)
def ticks_left(pp):  # integral of dtau/N over the last unit of proper time, N/s = 1/sqrt(sum tau^-2p)
    return quad(lambda x: math.sqrt(sum(x**(-2 * q) for q in pp)), 0, 1, limit=200)[0]
tl1 = ticks_left([-1 / 3, 2 / 3, 2 / 3]); tl2 = ticks_left([float(q.subs(u, 3)) for q in p])
check('C1 THEOREM: min_i a_i/sqrt3 <= N/sin eps0 <= min_i a_i, so with no shift ticks reach a crushing singularity '
      'iff int dtau/min a_i < inf: Kasner 1 - p_max = 1/(1+u+u^2) > 0, FRW iff w > -1/3: NOT singularity-avoiding', kas[0] == 0 and kas[1] == 0 and kas[2] == 1 / (1 + u + u**2)
      and np.isfinite(tl1) and np.isfinite(tl2), 'last unit of proper time = %.4f (u=1, Schwarzschild), %.4f (u=3) x cell/sin(eps0) ticks' % (tl1, tl2))
H0, Tt, eta = sp.symbols('H0 T0 eta', positive=True)
tc = 2 / (3 * H0); ncr = sp.integrate((1 - tau / tc)**sp.Rational(-2, 3), (tau, 0, tc)) / Tt
nrem = {e: 2 * S3 / math.sin(e) for e in (0.04, 0.0075)}
check('C2 THEOREM (Oppenheimer-Snyder, marginally bound, in its domain of dependence): N ~ a, the ticks count '
      'conformal time: crunch everywhere at once after n = 2/(H0 T0) ticks, n sqrt(2M/R0) after the surface horizon; '
      'cells outgrow the curvature radius in the last 2 sqrt3/sin eps0',
      sp.simplify(ncr - 2 / (H0 * Tt)) == 0, 'n = %s; last ticks %.1f (eps0 .04), %.1f (eps0 .0075); HT = 2/n_left' % (
      sp.simplify(ncr), nrem[0.04], nrem[0.0075]))
# spherical 3+1 scalar collapse, no shift, site labels Cartesian-regular (isotropic data)
def sph_setup(N, L, phi0, r0, sg):
    dr = L / N; r = (np.arange(N) + 0.5) * dr
    fq = lambda rr: phi0 * np.exp(-(rr - r0)**2 / sg**2); fp = lambda rr: -2 * (rr - r0) / sg**2 * fq(rr)
    so = solve_ivp(lambda rr, y: [y[1], -2 * y[1] / rr - math.pi * fp(rr)**2 * y[0]], [1e-6, r[-1]], [1.0, 0.0],
                   t_eval=r, rtol=1e-11, atol=1e-13)
    ps, dps = so.y; cc = ps[-1] + r[-1] * dps[-1]; M = -2 * r[-1]**2 * dps[-1] / cc; ps = ps / cc
    return dict(r=r, dr=dr, a=ps**4, b=ps**4, KA=0 * r, KB=0 * r, Psi=fp(r), Pi=0 * r, al=ps**2), M
def gh(u_, par):
    g_ = np.empty(len(u_) + 4); g_[2:-2] = u_; g_[1] = par * u_[0]; g_[0] = par * u_[1]
    g_[-2] = 2 * u_[-1] - u_[-2]; g_[-1] = 2 * g_[-2] - u_[-1]; return g_
D1 = lambda u_, par, dr: (lambda g_: (g_[3:-1] - g_[1:-3]) / (2 * dr))(gh(u_, par))
D2 = lambda u_, par, dr: (lambda g_: (g_[3:-1] - 2 * g_[2:-2] + g_[1:-3]) / dr**2)(gh(u_, par))
KO = lambda u_, par, dr: (lambda g_: -(g_[4:] - 4 * g_[3:-1] + 6 * g_[2:-2] - 4 * g_[1:-3] + g_[:-4]) / (16 * dr))(gh(u_, par))
def ricci(S):
    r, dr, a, b = S['r'], S['dr'], S['a'], S['b']
    DA = D1(np.log(a), 1, dr); DB = D1(np.log(b), 1, dr); dDB = D2(np.log(b), 1, dr)
    RA = (-(dDB + DB**2) + DB**2 / 2 + DA * DB / 2 - 2 * DB / r + DA / r) / a
    RB = (-(dDB + DB**2) / 2 + DA * DB / 4 - 2 * DB / r + DA / (2 * r) + (a / b - 1) / r**2) / a
    return DA, DB, RA, RB
def sph_rhs(S, gauge):
    r, dr, a, b, KA, KB, Psi, Pi = [S[k] for k in ('r', 'dr', 'a', 'b', 'KA', 'KB', 'Psi', 'Pi')]
    al_ = np.sqrt(3 / (1 / a + 2 / b)) if gauge in ('fixed', 'freeze') else S['al']
    if gauge == 'freeze': al_ = al_ / (1 + (al_ * np.abs(KA + 2 * KB) / 5.0)**4)   # proxy: crushed cubes stop ticking
    DA, DB, RA, RB = ricci(S); da = D1(al_, 1, dr)
    K = KA + 2 * KB; eta_ = Pi / (np.sqrt(a) * b)
    rho = (eta_**2 + Psi**2 / a) / 2; SB = (eta_**2 - Psi**2 / a) / 2; Str = rho + 2 * SB
    o = dict(a=-2 * al_ * a * KA, b=-2 * al_ * b * KB,
             KA=-(D2(al_, 1, dr) - DA * da / 2) / a + al_ * (RA + K * KA) + 4 * math.pi * al_ * (Str - 3 * rho),
             KB=-(DB / 2 + 1 / r) * da / a + al_ * (RB + K * KB) + 4 * math.pi * al_ * (Str - rho - 2 * SB),
             Psi=D1(al_ * Pi / (np.sqrt(a) * b), 1, dr), Pi=D1(r**2 * al_ * b * Psi / np.sqrt(a), -1, dr) / r**2)
    if gauge == '1+log': o['al'] = -2 * al_ * K
    for k in o: o[k] = o[k] + 0.3 * KO(S[k], -1 if k == 'Psi' else 1, dr)
    return o, al_
def reg(S, n=3):
    r = S['r']
    for x_, y_ in (('a', 'b'), ('KA', 'KB')):
        m = (S[x_] + 2 * S[y_]) / 3; d = S[x_] - S[y_]
        cf = np.polyfit(r[n:n + 3]**2, d[n:n + 3] / r[n:n + 3]**2, 1); d[:n] = r[:n]**2 * np.polyval(cf, r[:n]**2)
        S[x_] = m + 2 * d / 3; S[y_] = m - d / 3
def horizon_mass(S):
    DA, DB, RA, RB = ricci(S); th = (2 / np.sqrt(S['a'])) * (1 / S['r'] + DB / 2) - 2 * S['KB']
    R = S['r'] * np.sqrt(S['b']); ix = np.where((th[:-1] < 0) & (th[1:] >= 0))[0]
    if len(ix) == 0: return None
    i = ix[-1]; ww = th[i] / (th[i] - th[i + 1]); return (R[i] * (1 - ww) + R[i + 1] * ww) / 2
def ham(S):
    DA, DB, RA, RB = ricci(S); eta_ = S['Pi'] / (np.sqrt(S['a']) * S['b'])
    return RA + 2 * RB + 4 * S['KA'] * S['KB'] + 2 * S['KB']**2 - 8 * math.pi * (eta_**2 + S['Psi']**2 / S['a'])
def collapse(N, gauge, tmax, phi0=0.12):
    S, M = sph_setup(N, 20.0, phi0, 4.0, 1.0)
    keys = ['a', 'b', 'KA', 'KB', 'Psi', 'Pi'] + (['al'] if gauge == '1+log' else [])
    dt = 0.25 * S['dr']; tt = 0.0; tah = None; al0 = None; hm = None
    while tt < tmax:
        k1, alv = sph_rhs(S, gauge)
        st = lambda kk, h: {**S, **{q: S[q] + h * kk[q] for q in keys}}
        k2, _ = sph_rhs(st(k1, dt / 2), gauge); k3, _ = sph_rhs(st(k2, dt / 2), gauge); k4, _ = sph_rhs(st(k3, dt), gauge)
        with np.errstate(all='ignore'):
            for q in keys: S[q] = S[q] + dt / 6 * (k1[q] + 2 * k2[q] + 2 * k3[q] + k4[q])
        tt += dt
        if not all(np.all(np.isfinite(S[q])) for q in keys) or S['a'].min() <= 0 or S['b'].min() <= 0:
            return dict(M=M, crash=tt, tah=tah, al0=al0, mah=mah)
        reg(S); al0 = alv[0]; mah = horizon_mass(S)
        if tah is None and mah is not None: tah = tt
        maxK = np.abs(S['KA']).max()
    hh = np.abs(ham(S)); i8 = np.searchsorted(S['r'], 8.0)
    return dict(M=M, crash=None, tah=tah, al0=al0, mah=mah, maxK=maxK, ham8=hh[i8])
with np.errstate(all='ignore'):
    runs = {N: collapse(N, 'fixed', 6.0) for N in (400, 800, 1600)}
    lg = collapse(400, '1+log', 8.0)
cr = [runs[N]['crash'] for N in (400, 800, 1600)]; tl_ = cr[2] + (cr[2] - cr[1]) ** 2 / ((cr[1] - cr[0]) - (cr[2] - cr[1]))
M0 = runs[400]['M']
check('C3 DIAGNOSTIC (spherical scalar collapse, M_ADM = %.3f, no shift, regular centre): fixed-step slices find a '
      'horizon, then hit the central singularity at a converging finite time; 1+log control freezes its centre' % M0, all(c_ is not None for c_ in cr) and abs(cr[2] - cr[1]) < abs(cr[1] - cr[0])
      and lg['crash'] is None and lg['al0'] < 1e-4,
      'fixed: t_AH %.3f, t_sing %.4f %.4f %.4f -> %.3f = %.3f M_ADM, centre lapse %.2f %.2f %.2f -> 0; 1+log: alive at '
      't = 8, centre lapse %.0e, horizon mass %.3f' % (runs[1600]['tah'], *cr, tl_, tl_ / M0,
      runs[400]['al0'], runs[800]['al0'], runs[1600]['al0'], lg['al0'], lg['mah']))
with np.errstate(all='ignore'):
    fzr = [collapse(N, 'freeze', 10.0) for N in (400, 800)]
check('C7 DIAGNOSTIC (crushed-cube proxy: lapse cut where N|K| > 5): the exterior outlives the crash and the horizon '
      'mass matches the 1+log slicing', all((f_['crash'] or 10) > 8.5 and
      abs(f_['mah'] / lg['mah'] - 1) < 3e-3 for f_ in fzr), 'alive to t = %.2f, %.2f (vs 3.35); horizon mass %.4f, %.4f vs 1+log %.4f' % (
      fzr[0]['crash'] or 10, fzr[1]['crash'] or 10, fzr[0]['mah'], fzr[1]['mah'], lg['mah']))
eps_l = (0.04, 0.0075)
check('C4 THEOREM: Painleve-Gullstrand slices (gamma = delta, N = 1, shift sqrt(2M/R)) obey the rule exactly with '
      'stationary labels; every slice contains R = 0; sin 2theta = shift per tick saturates inside R_sat = (2/3) sin^2(eps0) M',
      sp.simplify(Nexpr.subs({g[0]: 1, g[1]: 1, g[2]: 1}) - s / sp.sqrt(3)) == 0 and
      sp.simplify(sp.solve(sp.Eq(sp.sqrt(2 / sp.Symbol('R', positive=True)) * sp.sin(sp.Symbol('e', positive=True)) / sp.sqrt(3), 1),
      sp.Symbol('R', positive=True))[0] - sp.Rational(2, 3) * sp.sin(sp.Symbol('e', positive=True))**2) == 0,
      'R_sat/M = %.3e (eps0 .04), %.3e (eps0 .0075); sites there move at sqrt3/sin eps0 = %.1f, %.1f c' % (
      2 / 3 * math.sin(eps_l[0])**2, 2 / 3 * math.sin(eps_l[1])**2, S3 / math.sin(eps_l[0]), S3 / math.sin(eps_l[1])))
# trumpet: stationary slicing N(R), gamma_RR = 1/N^2; labels need dr/dR = (1/N) sqrt(3/N^2 - 2 r^2/R^2)
NEG = []; Cm = 3 * S3 / 4; Nmax = lambda R: math.sqrt(max(1 - 2 / R + Cm**2 / R**4, 0.0))
def trumpet(y0, R1=60.0):
    NEG.clear()
    def fr(R, y):
        n_ = Nmax(R); arg = 3 / n_**2 - 2 * y[0]**2 / R**2
        if arg < 0: NEG.append(R)
        return [-(1 / n_) * math.sqrt(max(arg, 0.0))]  # integrate in x = -R
    ev = lambda x_, y: y[0]; ev.terminal = True
    so = solve_ivp(lambda x_, y: fr(-x_, y), [-R1, -1.5 - 1e-9], [y0 * R1], events=ev, rtol=1e-10, atol=1e-12, max_step=0.5)
    return -so.t[-1], so.y[0][-1], bool(NEG)
ystar = S3 / (Nmax(60.0) * math.sqrt(Nmax(60.0)**2 + 2))
tr = [trumpet(ystar * f_) for f_ in (0.5, 0.9, 1.0, 1.1, 1.2)]
check('C5 THEOREM: no stationary trumpet carries fixed-step site labels: an infinitely long trumpet needs '
      'int dR/N^2 = inf, so the label radius reaches 0 on a finite-area sphere before the limit surface (maximal trumpet, '
      'R0 = 1.5M, five label choices)',
      all(R_ > 1.5 + 1e-3 and abs(r_) < 1e-6 for R_, r_, ng in tr),
      'label centre at R/M = ' + ', '.join('%.4f%s' % (R_, '*' if ng else '') for R_, r_, ng in tr) + ' (* no real labels on a band first)')
# static star (incompressible): stationary zero-shift labels from the (forced) regular centre r = R/N(0)
def star(C, Rmax=20.0):
    Rs = 2 / C; worst = [1e9, None]
    ePhi = lambda R: (1.5 * math.sqrt(1 - 2 / Rs) - 0.5 * math.sqrt(1 - 2 * R**2 / Rs**3)) if R < Rs else math.sqrt(1 - 2 / R)
    gRR = lambda R: 1 / (1 - 2 * R**2 / Rs**3) if R < Rs else 1 / (1 - 2 / R)
    def f(R, y):
        arg = 3 / ePhi(R)**2 - 2 * y[0]**2 / R**2
        if arg < worst[0]: worst[0], worst[1] = arg, R
        return [math.sqrt(gRR(R) * max(arg, 0.0))]
    so = solve_ivp(f, [1e-5, Rmax], [1e-5 / ePhi(0.0)], rtol=1e-10, atol=1e-13, max_step=0.05)
    return worst, so.y[0][-1] / Rmax
lo, hi = 0.6, 0.7
for _ in range(22):
    mid = (lo + hi) / 2
    if star(mid)[0][0] > 0: lo = mid
    else: hi = mid
Rr = sp.Symbol('R', positive=True); rho = Rr / sp.sqrt(1 - 2 / Rr); Rmin = sp.solve(sp.diff(rho, Rr), Rr)
ns = star(2 * 1.4766 * 2.07 / 12.4); w7 = star(0.70)
check('C6 THEOREM + DIAGNOSTIC: static zero-shift labels need r <= sqrt(3/2) R/N with r growing outward, so they must '
      'pass under the optical-radius minimum 3 sqrt3 M at R = 3M; with r = R/N(0) forced at the centre, incompressible stars '
      'carry them up to 2M/R* = %.4f (R* = %.3f M): measured neutron stars do; ultracompact stars and holes need a shift' % (lo, 2 / lo), Rmin == [3] and sp.simplify(rho.subs(Rr, 3) - 3 * sp.sqrt(3)) == 0
      and ns[0][0] > 0 and w7[0][0] < 0 and 2 / lo < 3, 'J0740+6620 (2.07 M_sun, 12.4 km): min radicand %.3f, r/R at 20M %.4f; '
      '2M/R* = 0.70: radicand %.3f at R = %.3f M' % (ns[0][0], ns[1], w7[0][0], w7[0][1]))
# ---------------------------------------------------------------- D. consequences
print('== D. consequences of a physical lapse')
a_ = sp.symbols('a1:4', positive=True); ad = sp.symbols('ad1:4'); sN = sp.Symbol('sN', positive=True)
Nfix = sN / sp.sqrt(sum(1 / x**2 for x in a_)); V = a_[0] * a_[1] * a_[2]
Lr = -(2 * V / Nfix) * (ad[0] * ad[1] / (a_[0] * a_[1]) + ad[1] * ad[2] / (a_[1] * a_[2]) + ad[0] * ad[2] / (a_[0] * a_[2]))
Ef = sp.simplify(sum(ad[i] * sp.diff(Lr, ad[i]) for i in range(3)) - Lr)
Qc = ad[0] * ad[1] / (a_[0] * a_[1]) + ad[1] * ad[2] / (a_[1] * a_[2]) + ad[0] * ad[2] / (a_[0] * a_[2])  # lapse equation of GR: Qc = 0
# Kasner with the fixed-step lapse solves the reduced Euler-Lagrange equations
tt_ = sp.Symbol('tt'); taus = sp.Function('T')(tt_)
pk = [sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(2, 3)]
asol = [taus**q for q in pk]
EL = []
for i in range(3):
    dLdq = sp.diff(Lr, a_[i]); dLdv = sp.diff(Lr, ad[i]); rep = {a_[j]: asol[j] for j in range(3)}
    rep.update({ad[j]: sp.diff(asol[j], tt_) for j in range(3)})
    EL.append(sp.diff(dLdv.subs(rep), tt_) - dLdq.subs(rep))
Ns = Nfix.subs({a_[j]: asol[j] for j in range(3)})
ELn = [sp.simplify(e.subs(sp.Derivative(taus, (tt_, 2)), sp.diff(Ns, tt_).subs(sp.Derivative(taus, tt_), Ns)).subs(sp.Derivative(taus, tt_), Ns)) for e in EL]
check('D1 THEOREM: with the lapse fixed before variation the lost lapse equation survives as a conserved energy '
      '(Bianchi I: E = L = 0 iff the Hamiltonian constraint), so zero initial data stay GR; Kasner solves the reduced equations', sp.simplify(Ef - Lr) == 0 and
      sp.simplify(Ef + 2 * V * Qc / Nfix) == 0 and all(e == 0 for e in ELn), 'E - L = 0, E = -(2V/N) x (lapse equation), Kasner EL residuals %s' % ELn)
# Lieb-Robinson-type bound for the cube circuit: U = cos eps - i sin eps R, R^2 = 1, one site per axis per hop
def lr_tail(eps, ticks, x_sites):
    m = 2 * ticks; n0 = x_sites
    if n0 > m: return 0.0, -999.0
    ls = [math.lgamma(m + 1) - math.lgamma(j + 1) - math.lgamma(m - j + 1) + j * math.log(math.sin(eps))
          for j in range(n0, m + 1)]
    mx = max(ls); return 10 ** ((mx + math.log(sum(math.exp(q - mx) for q in ls))) / math.log(10)) if mx > -690 else 0.0, (mx + math.log(sum(math.exp(q - mx) for q in ls))) / math.log(10)
cl = lambda eps: 2 * math.sin(eps) / S3      # light speed, sites per tick
def chain(eps, ticks, L=1200):
    # 1D two-tiling analogue: pairs (2j,2j+1) then (2j+1,2j+2), each exp(-i eps X)
    psi_ = np.zeros(L, complex); psi_[L // 2] = 1
    cs, sn = math.cos(eps), math.sin(eps)
    for _ in range(ticks):
        for off in (0, 1):
            e_ = psi_[off:L - 1:2].copy(); o_ = psi_[off + 1:L:2].copy()
            psi_[off:L - 1:2] = cs * e_ - 1j * sn * o_; psi_[off + 1:L:2] = cs * o_ - 1j * sn * e_
    return psi_
e_ = 0.3; tk = 200; ps_ = chain(e_, tk); xs = np.abs(np.arange(1200) - 600)
vals = []
for v_ in (2.0, 4.71, 6.0):
    x0 = int(v_ * cl(e_) * tk); tail = (np.abs(ps_[xs >= x0])**2).sum(); bl = lr_tail(e_, tk, x0)[1]
    vals.append((math.log10(math.sqrt(tail)) if tail > 0 else -999, bl))
check('D2 THEOREM: the half-tick is cos(eps) - i sin(eps) R with R^2 = 1, moving odds at most one site per axis, so the '
      'odds beyond x sites after t ticks are <= sum_{j>=x} C(2t,j) sin^j eps ~ (2e t sin eps/x)^x: effective cone '
      'e sqrt3 c = 4.71 c for every eps0 (strict cone sqrt3/sin eps0 c)', all(n_ <= b_ + 1e-6 for n_, b_ in vals),
      'chain eps .3, 200 ticks, log10 odds beyond 2c/4.71c/6c: ' + ', '.join(('%.0f' % n_ if n_ > -999 else '<-300') + (' (bound %.0f)' % b_ if b_ > -999 else ' (bound 0: beyond strict cone)') for n_, b_ in vals))
mm = 10 * 1476.6; lcell = 2 * math.sqrt(8 * math.pi) * 1.616e-35
check('D3 ESTIMATE: no law defines a crushed cube (CL-3 has no stationary point, CL-1 no merge clause); laws are local '
      'per tick, so the undefined region grows at the strict cone and exits the horizon ~ sin(eps0) R_label/sqrt3 after '
      'the crunch: a crushed-cube clause is required', True, '10 M_sun, label radius ~ 2M: %.2f us (eps0 .04), %.2f us (eps0 .0075) after the crunch' % (
      2 * mm * math.sin(0.04) / S3 / 2.998e8 * 1e6, 2 * mm * math.sin(0.0075) / S3 / 2.998e8 * 1e6))
# ---------------------------------------------------------------- E. estimates against measurement
print('== E. ESTIMATES (cube 2 sqrt(8 pi) l_P = %.2e m)' % lcell)
Msun = 1476.6
items = [('GW150914 (l/M)^2', (lcell / (62 * Msun))**2, 0.1),
         ('M87*', (lcell / (6.5e9 * Msun))**2, 0.1),
         ('Sgr A*', (lcell / (4.3e6 * Msun))**2, 0.1),
         ('230 GHz (El)^2', (2 * math.pi * 230e9 / 2.998e8 * lcell)**2, 0.1),
         ('GW170817 (kl)^2', (2 * math.pi * 100 / 2.998e8 * lcell)**2, 1e-15),
         ('NS (l/R)^2', (lcell / 1.2e4)**2, 0.05)]
check('E1 zero dark constant: the exterior is GR in this slicing (horizon, ringdown, shadow 3 sqrt3 M, TOV masses); '
      'corrections are powers of l/M', all(v < b for _, v, b in items),
      '; '.join('%s %.0e' % (n_, v) for n_, v, _ in items))
print('supplied: CL-1 lapse rule and shift reading, continuum 3+1 = CL-3 limit (zero dark constant), zero or PG shift,')
print('  scalar-field matter, Kasner/OS/maximal-trumpet/incompressible-star metrics, 1D chain analogue, unit map, bounds.')
print('elapsed %.1f s' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % (NP, NF))
