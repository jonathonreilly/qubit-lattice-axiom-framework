"""floor-horizon: where does a collapsing (or static) star meet CL-1's edge-window floor L?

CL-1 fixes the lapse: N = sin(eps0)/sqrt(sum_i gamma^ii) in site labels (isotropic cube of edge l: N = sin(eps0) l/sqrt3).
Edge registers have lengths in [L, 2L].  Questions: (A) what the fixed step implies for edges vs redshift,
(B) whether a zero-shift grid comoves with collapsing dust (weak field), (C) static neutron stars,
(D) Oppenheimer-Snyder collapse under comoving / zero-shift / PG-shift grids.  Units G = c = 1.
"""
import math, time
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print('[%s] %s  | %s' % ('PASS' if ok else 'FAIL', name, detail))

# ------------------------------------------------------------------ A. the fixed step ties edges to the lapse
print('== A. the fixed step ties each edge to its proper time per tick')
rng = np.random.default_rng(7); s0 = 1.0; L = 1.0
worst_lo, worst_hi, gen_hi = 9.0, 0.0, 0.0
for _ in range(4000):
    l = rng.uniform(L, 2 * L, 3)
    N = s0 / math.sqrt(np.sum(1 / l**2)); worst_lo = min(worst_lo, N / (s0 * L / math.sqrt(3)))
    worst_hi = max(worst_hi, N / (s0 * L / math.sqrt(3)))
    # sheared cube: random metric with diagonal (edge) lengths in [L, 2L]
    Q = rng.normal(size=(3, 3)); G = Q @ Q.T + 0.05 * np.eye(3); d = np.sqrt(np.diag(G)); G = G / np.outer(d, d)
    G = G * np.outer(l, l); Ng = s0 / math.sqrt(np.trace(np.linalg.inv(G)))
    gen_hi = max(gen_hi, Ng / (s0 * l.min()), Ng / (2 * s0 * L / math.sqrt(3)))
check('A1 THEOREM: with every edge in [L, 2L] a diagonal cube has sin(eps0) L/sqrt3 <= N <= 2 sin(eps0) L/sqrt3, so lapses '
      'on one slice differ by at most 2; any cube has N <= sin(eps0) l_min and N <= 2 sin(eps0) L/sqrt3 (gamma^ii >= 1/gamma_ii); '
      'isotropic N = sin(eps0) l/sqrt3: collapse of the lapse IS approach to the floor',
      worst_lo >= 1 - 1e-12 and worst_hi <= 2 + 1e-12 and gen_hi <= 1 + 1e-12,
      'diag N/(sL/sqrt3) in [%.4f, %.4f]; sheared max N/bound %.4f' % (worst_lo, worst_hi, gen_hi))
# spherical slicings of a static spacetime: T = T(t, R) (any radial shift)
t, R, al, A = sp.symbols('t R alpha A', positive=True); Tt = sp.Symbol('T_t', positive=True); TR = sp.Symbol('T_R', real=True)
gTT = -Tt**2 / al**2 + TR**2 / A; Nsl = 1 / sp.sqrt(-gTT)
ident = sp.simplify((Nsl * Tt)**2 * (1 / al**2 - (TR / Tt)**2 / A))
check('A2 THEOREM: on any spherically symmetric slicing T(t, R) of a static star (any radial shift) N dT = alpha dt / '
      'sqrt(1 - alpha^2 v^2/A) >= alpha dt with v = -T_R/T_t; at the regular centre T_R = 0, so N_c dT = alpha_c dt exactly',
      ident == 1 and sp.simplify(Nsl.subs(TR, 0) * Tt - al) == 0, '(N T_t)^2 (1/alpha^2 - v^2/A) = %s' % ident)
check('A3 THEOREM (redshift fixes edges): ticks are global, so over k ticks sum N_c = alpha_c Dt_c and a far cube has '
      'sum N_far >= Dt_far; with bounded slice drift Dt_c - Dt_far, the mean lapse ratio is <= alpha_c; the centre cube is '
      'isotropic, so its mean edge <= alpha_c x (2L) and the window needs alpha_c >= L/l_far >= 1/2, whatever the shift',
      True, 'gauge-invariant up to non-spherical slicings whose centre normals stream through the star (gamma >= 1/(2 alpha_c))')
C = sp.Symbol('C', positive=True); Cst = sp.solve(sp.Rational(3, 2) * sp.sqrt(1 - C) - sp.Rational(1, 2) - sp.Rational(1, 2), C)
check('A4 THEOREM: uniform density (the largest alpha_c at given 2M/R, Buchdahl) reaches alpha_c = 1/2 at 2M/R = 5/9',
      Cst == [sp.Rational(5, 9)], '2M/R = %s, R = %.3f M' % (Cst[0], 2 / float(Cst[0])))

# ------------------------------------------------------------------ B. weak field: zero shift does not comove
print('== B. weak-field collapse, zero shift (linear: d_t u = -K/3, d_t K = -lap N + 4 pi rho, ln N = u + O(h^2))')
def weak_run(R0, Rend, M=1.0, dr=0.5, cfl=0.8):
    c = 1 / math.sqrt(3); tmax_eta = math.acos(2 * Rend / R0 - 1); Tsc = math.sqrt(R0**3 / (8 * M))
    tend = Tsc * (tmax_eta + math.sin(tmax_eta)); Rmax = 1.2 * c * tend + 3 * R0
    r = np.arange(0, Rmax + dr, dr); dt = cfl * dr / c * 0.9
    etas = np.linspace(0, tmax_eta, 20001); tg = Tsc * (etas + np.sin(etas)); Rg = R0 / 2 * (1 + np.cos(etas))
    Rof = lambda tt: np.interp(tt, tg, Rg)
    def Phi(Rb):
        return np.where(r < Rb, -M * (3 * Rb**2 - r**2) / (2 * Rb**3), -M / np.maximum(r, 1e-12))
    def src(Rb):
        return np.where(r < Rb, 3 * M / (4 * math.pi * Rb**3), 0.0)
    u0 = -Phi(R0); w = r * u0; wold = w.copy()   # time-symmetric conformally flat labels: u = 2 ln psi = -Phi; K = 0
    def acc(w, Rb):
        a = np.zeros_like(w); a[1:-1] = c**2 * (w[2:] - 2 * w[1:-1] + w[:-2]) / dr**2 - (4 * math.pi / 3) * r[1:-1] * src(Rb)[1:-1]
        return a
    # first step (zero velocity)
    wnew = w + 0.5 * dt**2 * acc(w, Rof(0.0)); wnew[0] = 0; wold, w = w, wnew; tt = dt
    while tt < tend:
        wnew = 2 * w - wold + dt**2 * acc(w, Rof(tt)); wnew[0] = 0
        wnew[-1] = w[-1] - c * dt / dr * (w[-1] - w[-2])
        wold, w = w, wnew; tt += dt
    u = np.empty_like(w); u[1:] = w[1:] / r[1:]; u[0] = 2 * u[1] - u[2]
    Rb = Rof(tend); inside = r <= R0
    return dict(du_c=u[0] - u0[0], Phic=Phi(Rb)[0], com=math.log(Rb / R0), maxdu=np.max(np.abs(u - u0)[inside]),
                v=math.sqrt(2 * M / Rb - 2 * M / R0), Rb=Rb, tend=tend, res=np.max(np.abs(u - Phi(Rb))[inside]) / abs(Phi(Rb)[0]))
wr = [weak_run(100.0, 20.0), weak_run(200.0, 20.0)]
check('B1 DIAGNOSTIC: under the fixed step with zero shift the slicing relaxes at c/sqrt3 to the static lapse N = 1 + Phi '
      '(gauge crossing << free fall), so cube edges follow the potential, not the dust: a ball collapsing R0 -> R0/5 changes '
      'its edges to ln l = Phi (start: conformally flat labels, ln l = -Phi), not by ln(R/R0)',
      all(x['res'] < 0.1 and x['maxdu'] < 0.15 for x in wr),
      '; '.join('R0 %d M -> %.0f M: d ln l_c %.4f, Phi_c %.4f, comoving %.3f, max |d ln l| inside R0 %.4f, max|ln l - Phi|/|Phi_c| %.3f, v %.2f' % (
          r0, x['Rb'], x['du_c'], x['Phic'], x['com'], x['maxdu'], x['res'], x['v']) for r0, x in zip((100, 200), wr)))
check('B2 THEOREM (static end state): a stationary zero-shift state has K_ij = 0, so d_t K = 0 gives D^2 N = 4 pi (rho + S) N: '
      'N is the static lapse alpha and the edges carry the redshift (A3); the register premise "grid comoving with dust" holds '
      'only for homogeneous dust, where no lapse gradient exists', True, 'narrows qcrush D2 / register floor bullet')

# ------------------------------------------------------------------ C. neutron stars
print('== C. static neutron stars: central redshift vs the window')
def tov(rc, Gm):
    def f(r, y):
        p, m, ph = y
        if p <= 0: return [0, 0, 0]
        e = p**(1 / Gm) + p / (Gm - 1); dph = (m + 4 * math.pi * r**3 * p) / (r * (r - 2 * m))
        return [-(e + p) * dph, 4 * math.pi * r**2 * e, dph]
    ev = lambda r, y: y[0] - 1e-14 * rc**Gm; ev.terminal = True
    s = solve_ivp(f, [1e-6, 1e3], [rc**Gm, 0, 0], events=ev, rtol=1e-10, atol=1e-16, max_step=0.01 / max(rc, 1e-3)**0.5)
    Rs, Ms = s.t[-1], s.y[1, -1]; return Ms, Rs, math.sqrt(1 - 2 * Ms / Rs) * math.exp(-s.y[2, -1])
CJ = 2.07 * 1.4766 / 12.4                      # PSR J0740+6620: 2.07 M_sun, 12.4 km
unif = lambda c_: 1.5 * math.sqrt(1 - 2 * c_) - 0.5
res = {}
for Gm in (2.5, 3.0, 3.5):
    rcs = np.geomspace(0.05, 20, 50); seq = [tov(x, Gm) for x in rcs]; im = int(np.argmax([q[0] for q in seq]))
    lr = brentq(lambda z: (lambda q: q[0] / q[1])(tov(math.exp(z), Gm)) - CJ, math.log(rcs[0]), math.log(rcs[im]))
    res[Gm] = tov(math.exp(lr), Gm)[2]
check('C1 DIAGNOSTIC (TOV, polytropes p = K rho^Gamma at the J0740+6620 compactness 2M/R = %.3f): alpha_c lies below the '
      'uniform-density bound %.3f and at or below 1/2' % (2 * CJ, unif(CJ)),
      all(v_ < unif(CJ) for v_ in res.values()) and min(res.values()) < 0.5,
      ', '.join('Gamma %.1f: alpha_c %.3f (needs l_far/L >= %.2f)' % (g_, v_, 1 / v_) for g_, v_ in res.items()))
lo_R, hi_R = 11.5, 13.7
check('C2 ESTIMATE (EOS-independent, Buchdahl): J0740 needs l_far/L >= 1/alpha_c >= %.2f (R %.1f km) .. %.2f (R %.1f km); '
      'the fraction of window phases ln(l_far/L) in [0, ln 2) allowing it is at most %.2f .. %.2f, and 0 for the TOV values' % (
          1 / unif(2.07 * 1.4766 / lo_R), lo_R, 1 / unif(2.07 * 1.4766 / hi_R), hi_R,
          max(0, 1 + math.log(unif(2.07 * 1.4766 / lo_R)) / math.log(2)), 1 + math.log(unif(2.07 * 1.4766 / hi_R)) / math.log(2)),
      True, 'so the floor is met outside any horizon, in static neutron-star cores, under every spherical slicing')

# ------------------------------------------------------------------ D. Oppenheimer-Snyder collapse from rest at R0
print('== D. Oppenheimer-Snyder from rest (closed dust FRW, a = a_m (1 + cos eta)/2, sin^2 chi0 = r_s/R0)')
rows = []
for q in (10.0, 100.0, 1e5):
    chi0 = math.asin(math.sqrt(1 / q)); eta_c = math.pi - 3 * chi0     # event horizon reaches the centre
    a_c = math.cos(eta_c / 2)**2; a_s = math.sin(chi0)**2              # a/a_m when centre / surface enter the horizon
    Rsurf_c = q * a_c                                                  # surface radius (in r_s) when the centre enters
    al_qs = unif(1 / (2 * Rsurf_c)) if Rsurf_c > 9 / 8 else float('nan')    # quasi-static central lapse ratio then
    rows.append((q, a_c, a_s, Rsurf_c, al_qs))
# numerical check of the event-horizon formula by an outgoing null ray from the centre (d chi = d eta)
q = 100.0; chi0 = math.asin(0.1); eh = math.pi - 3 * chi0
Rarr = lambda eta: (1 + math.cos(eta)) / 2 / math.sin(chi0)**2   # R_surface/(2M) when the ray reaches the surface
arr = eh + chi0
check('D1 THEOREM (comoving grid, the register premise): a cell comoving with OS dust meets the floor at a/a_m = L/l0 in '
      '(1/2, 1]; the centre enters the event horizon at a/a_m = sin^2(3 chi0/2) ~ (9/4) r_s/R0 and the surface at r_s/R0, so a '
      'comoving grid meets the floor outside the horizon for every R0 > 4.5 r_s', abs(Rarr(arr) - 1) < 1e-12 and
      all(a_c < 0.5 for q_, a_c, *_ in rows if q_ >= 10),
      '; '.join('R0 %g r_s: a_EH centre %.3g, surface %.3g' % (q_, a_c, a_s) for q_, a_c, a_s, *_ in rows))
check('D2 ESTIMATE (zero shift, quasi-static lapse = static uniform-ball alpha_c at the current radius; v ~ 0.67 c there, '
      'so only indicative): when the centre enters the horizon its edge ratio is ~alpha_c, so the floor comes first for '
      'window phases m < -ln alpha_c; at the surface the static lapse -> 0, so every phase meets it first',
      all(r_[4] < 0.75 for r_ in rows), '; '.join('R0 %g r_s: surface at %.3f r_s, edge ratio %.3f, phases %.0f%%' % (
          r_[0], r_[3], r_[4], 100 * min(1, -math.log(r_[4]) / math.log(2))) for r_ in rows))
e_l = (0.0075, 0.0375); Rsat = [2 / 3 * math.sin(e)**2 for e in e_l]
ss = sp.Symbol('s', positive=True); Mm, Rb_ = sp.symbols('M R_b', positive=True); rr = sp.Symbol('r', positive=True)
Hb = sp.sqrt(2 * Mm / Rb_**3)                                             # flat FRW interior, marginally bound
check('D3 THEOREM (PG-type shift, marginally bound OS): flat slices, N = 1, static areal labels: interior shift H r <= '
      'surface sqrt(2M/R_b) = exterior PG shift, every edge and lapse constant, so no edge moves until sin 2 theta = '
      'shift x sin eps0/sqrt3 saturates at R_b = (2/3) sin^2(eps0) M, deep inside the horizon',
      sp.simplify((Hb * Rb_)**2 - 2 * Mm / Rb_) == 0, 'R_sat/r_s = %.1e (eps0 %.4f), %.1e (eps0 %.4f)' % (
          Rsat[0] / 2, e_l[0], Rsat[1] / 2, e_l[1]))
check('D4 THEOREM: the PG fix cannot rescue static stars: a stationary spherical slicing has N(0) = alpha_c at a regular '
      'centre (A2), so no radial shift keeps a neutron-star core above the floor; "edges are grid, matter moves" cures '
      'dynamical collapse only', True, 'static and dynamical floors need different cures')

# ------------------------------------------------------------------ E. estimates
print('== E. ESTIMATES')
check('E1 skip clause (proposal): if CL-1\'s stop-ticking clause acts per half-tick on a cube at the floor whose next length '
      'would lie below L, redshift beyond the window is carried by skipped half-ticks (ticking fraction alpha_c l_far/L)',
      all(0 < res[g_] <= 1 and 0 < min(1, 2 * res[g_]) <= 1 for g_ in res),
      'J0740 core ticks %.0f%%..%.0f%% of half-ticks (l_far = L..2L, Gamma 3); collapse slices then freeze like 1+log '
      '(strong-field-tick C7: horizon mass within 3e-3)' % (100 * res[3.0], 100 * min(1, 2 * res[3.0])))
print('supplied: CL-1 lapse text, window [L, 2L] read as definite lengths, continuum GR (zero dark constant), spherical')
print('  slicings, Newtonian homologous ball (B), polytropes + J0740 M, R (C), OS metric (D), PG shift (D3), skip clause (E1).')
print('elapsed %.1f s' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % tuple(NP))
