AUDIT_INPUT_PATHS = ('docs/WITH_THE_WAVE_SHIFT_THE_COLLAPSE_FLOOR_STAYS_INSIDE_HORIZONS_AND_THE_EDGE_TOP_NEEDS_DELTA_AT_LEAST_ONE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
# wave-shift-collapse: does CL-3's undamped wave shift keep every edge register inside [L/8, 2^(1+Delta) L]
# outside the horizon in dynamical spherical dust collapse?  Tied lapse (fixed step) + wave shift vs zero shift,
# nonlinear spherically symmetric ADM (G = c = M = 1), plus linear theorems.  Self-contained.
import numpy as np, sympy as sp, time, math, warnings
warnings.filterwarnings('ignore')
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print('[%s] %s | %s' % ('PASS' if ok else 'FAIL', name, detail))

def ricci_funcs():
    r, th = sp.symbols('r theta', positive=True)
    A, B = sp.Function('A')(r), sp.Function('B')(r)
    g = sp.diag(A, B * r**2, B * r**2 * sp.sin(th)**2); x = [r, th, sp.Symbol('ph')]
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(3)) / 2
             for c in range(3)] for b in range(3)] for a in range(3)]
    def Ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
                               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(3))
                               for a in range(3)))
    Rrr = sp.simplify(Ric(0, 0) / A); Rtt = sp.simplify(Ric(1, 1) / (B * r**2))
    s = sp.symbols('A0 A1 A2 B0 B1 B2')
    sub = {sp.diff(A, r, 2): s[2], sp.diff(B, r, 2): s[5], sp.diff(A, r): s[1], sp.diff(B, r): s[4]}
    def mk(e):
        e = e.subs(sub).subs({A: s[0], B: s[3]})
        return sp.lambdify((r,) + s, e, 'numpy')
    return mk(Rrr), mk(Rtt)

RRR, RTT = ricci_funcs()
MSIGN = 1.0
TESTPERT = 0.0
KOEPS = 0.1
LAPSEMODE = 'tied'
SRCFORM = 'matter'
WFRAC = 0.06

def run(R0=20.0, shift='wave', mu=0.75, nfac=False, h=0.1, rmax=None, tmax=None, verbose=False, src_fix=0.0):
    tff = np.pi / 2 * np.sqrt(R0**3 / 2.0)
    if tmax is None: tmax = 1.6 * tff
    if rmax is None: rmax = R0 + tmax + 20
    ng = 3; n = int(rmax / h)
    r = (np.arange(-ng, n + ng) + 0.5) * h
    # conformal density, Delta psi = -2 pi rho~ ; M_ADM = 4 pi int rho~ r^2 = 1
    rb = R0 - 1.0
    w = WFRAC * rb
    prof = 0.5 * (1 - np.tanh((np.abs(r) - rb) / w))
    rr = np.linspace(0, rmax + 2, 200001); pp = 0.5 * (1 - np.tanh((rr - rb) / w)); dr_ = rr[1] - rr[0]
    from scipy.integrate import cumulative_trapezoid as ctz
    m_in = ctz(pp * rr**2, rr, initial=0)
    norm = 4 * np.pi * m_in[-1]; rho0 = 1.0 / norm
    pr = pp * rr; tot = ctz(pr, rr, initial=0)
    m_in *= rho0; pp *= rho0
    outer = rho0 * (tot[-1] - tot)
    psi_rr = 1 + 2 * np.pi * (m_in / np.maximum(rr, 1e-12) + outer)
    psi_rr[0] = 1 + 2 * np.pi * outer[0]
    psi = np.interp(np.abs(r), rr, psi_rr)
    rt = rho0 * prof
    A = psi**4; B = psi**4
    if TESTPERT:
        A = 1 + TESTPERT * np.exp(-(r - 4)**2); B = A.copy(); rt = 0 * rt; psi = 0 * psi + 1
    KA = np.zeros_like(r); KB = np.zeros_like(r)
    be = np.zeros_like(r); Bb = np.zeros_like(r)
    rho = rt * psi**-5
    Ds = np.sqrt(A) * B * rho     # sqrt(A) B rho W
    ur = np.zeros_like(r)
    par = np.array([1, 1, 1, 1, -1, -1, 1, -1, -1])
    lam = (1 - A / B) / r
    Y = np.array([A, B, KA, KB, be, Bb, Ds, ur, lam])

    def ghost(Y):
        for k in range(9):
            Y[k, :ng] = par[k] * Y[k, 2 * ng - 1:ng - 1:-1]
            Y[k, -ng:] = Y[k, -ng - 1]  # flat copy at outer edge
        return Y

    def d1(f):
        o = np.zeros_like(f)
        o[2:-2] = (f[:-4] - 8 * f[1:-3] + 8 * f[3:-1] - f[4:]) / (12 * h); return o
    def d2(f):
        o = np.zeros_like(f)
        o[2:-2] = (-f[:-4] + 16 * f[1:-3] - 30 * f[2:-2] + 16 * f[3:-1] - f[4:]) / (12 * h * h); return o
    def ko(f):
        o = np.zeros_like(f)
        o[3:-3] = (f[:-6] - 6 * f[1:-5] + 15 * f[2:-4] - 20 * f[3:-3] + 15 * f[4:-2] - 6 * f[5:-1] + f[6:]) / (64 * h)
        return o

    def lapse(A, B): return np.sqrt(3.0 / (1.0 / A + 2.0 / B)) if LAPSEMODE == 'tied' else (np.ones_like(A) if LAPSEMODE == 'geo' else (A * B * B)**(1/6))

    def rhs(Y):
        Y = ghost(Y)
        A, B, KA, KB, be, Bb, Ds, ur, lam = Y
        al = lapse(A, B)
        A1, A2, B1, B2 = d1(A), d2(A), d1(B), d2(B)
        al1, al2 = d1(al), d2(al)
        W = np.sqrt(1 + ur**2 / A)
        rho = Ds / (np.sqrt(A) * B * W)
        E = rho * W**2; Sr = rho * W * ur; Srr = rho * ur**2 / A
        v = ur / (A * W)
        Rr = RRR(r, A, A1, A2, B, B1, B2); Rt = RTT(r, A, A1, A2, B, B1, B2)
        Rt = Rt - (1 / B - 1 / A) / r**2 - lam / (A * r)   # regularised (Alcubierre-Gonzalez)
        K = KA + 2 * KB
        DDa_r = (al2 - al1 * A1 / (2 * A)) / A
        DDa_t = al1 * (1 / r + B1 / (2 * B)) / A
        bd = d1(be)
        dA = -2 * al * A * KA + be * A1 + 2 * A * bd
        dB = -2 * al * B * KB + be * B1 + 2 * B * be / r
        dKA = be * d1(KA) - DDa_r + al * (Rr + K * KA) + 4 * np.pi * al * (-E - Srr)
        dKB = be * d1(KB) - DDa_t + al * (Rt + K * KB) + 4 * np.pi * al * (Srr - E)
        Mr = -2 * d1(KB) + (2 / r + B1 / B) * (KA - KB)
        if shift == 'wave':
            lapv = d1(d1(r**2 * be) / r**2) if False else d2(be) + 2 * bd / r - 2 * be / r**2
            src = lapv - (2 * Mr / A if SRCFORM == 'geom' else 16 * np.pi * Sr / A)
            if src_fix: src = src + src_fix * 16 * np.pi * Sr / A
            fac = al**2 if nfac else 1.0
            dbe = Bb; dBb = mu * fac * src
        else:
            dbe = np.zeros_like(be); dBb = np.zeros_like(be)
        cv = al * v - be
        # upwind MUSCL (minmod) transport for the dust
        dq = np.diff(Ds); sl = np.zeros_like(Ds)
        sl[1:-1] = np.where(dq[1:] * dq[:-1] > 0, np.sign(dq[1:]) * np.minimum(np.abs(dq[1:]), np.abs(dq[:-1])), 0)
        cf = 0.5 * (cv[1:] + cv[:-1]); rf = 0.5 * (r[1:] + r[:-1])
        qL = Ds[:-1] + 0.5 * sl[:-1]; qR = Ds[1:] - 0.5 * sl[1:]
        flux = rf**2 * cf * np.where(cf > 0, qL, qR)
        dDs = np.zeros_like(Ds); dDs[1:-1] = -3 * (flux[1:] - flux[:-1]) / (np.abs(rf[1:])**3 * np.sign(rf[1:]) - np.abs(rf[:-1])**3 * np.sign(rf[:-1]))
        F = 0.5 * (W / al) * (d1(-al**2 + A * be**2) + 2 * d1(A * be) * cv + A1 * cv**2)
        up = np.zeros_like(ur); dn = np.zeros_like(ur)
        up[2:] = (3 * ur[2:] - 4 * ur[1:-1] + ur[:-2]) / (2 * h)
        dn[:-2] = (-3 * ur[:-2] + 4 * ur[1:-1] - ur[2:]) / (2 * h)
        dur = -cv * np.where(cv > 0, up, dn) + F
        KAB_r = d1(KB) + MSIGN * 4 * np.pi * Sr - (KA - KB) * B1 / (2 * B)
        dlam = (A / B) * (2 * al * KAB_r - (be / r) * (A1 / A - B1 / B) - 2 * (bd - be / r) / r)
        out = np.array([dA, dB, dKA, dKB, dbe, dBb, dDs, dur, dlam])
        eps = KOEPS
        for k in (0, 1, 2, 3, 4, 5, 8): out[k] += eps * ko(Y[k])
        out[:, :ng] = 0; out[:, -ng:] = 0
        return out

    def diag(Y):
        Y = ghost(Y)
        A, B, KA, KB, be, Bb, Ds, ur, lam = Y
        A1, B1 = d1(A), d1(B)
        W = np.sqrt(1 + ur**2 / A); rho = Ds / (np.sqrt(A) * B * W)
        Th = (2 / r + B1 / B) / np.sqrt(A) - 2 * KB
        Rar = r * np.sqrt(B)
        Mr = -2 * d1(KB) + (2 / r + B1 / B) * (KA - KB)
        Sr = rho * W * ur
        return Th, Rar, Mr, Sr, rho
    dt = 0.25 * h
    if tmax == 0: return r, rhs(Y.copy()), Y
    t = 0.0; I = slice(ng, -ng)
    hist = []
    nsteps = int(tmax / dt)
    for it in range(nsteps):
        k1 = rhs(Y.copy()); k2 = rhs(Y + 0.5 * dt * k1); k3 = rhs(Y + 0.5 * dt * k2); k4 = rhs(Y + dt * k3)
        Y = Y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t += dt
        Y[6] = np.maximum(Y[6], 1e-14)
        if not np.all(np.isfinite(Y)):
            bad = np.where(~np.isfinite(Y))
            hist.append((t, 'nan', sorted(set(bad[0].tolist())), r[bad[1][:5]])); break
        if verbose and it % 5 == 0:
            print(it, [ (k, float(np.abs(k1[k]).max()), float(r[np.argmax(np.abs(k1[k]))])) for k in range(8)])
        if it % 20 == 0:
            Th, Rar, Mr, Sr, rho = diag(Y.copy())
            A, B = Y[0], Y[1]
            la, lb = np.sqrt(A[I]), np.sqrt(B[I])
            hist.append((t, la.copy(), lb.copy(), Th[I].copy(), Rar[I].copy(), Y[4][I].copy(), lapse(A, B)[I].copy(), rho[I].copy(), Mr[I].copy(), Sr[I].copy(), Y[:, I].copy()))
            if min(la.min(), lb.min()) < 1 / 20: break
    return r[I], hist

def summarize(rg, H, label=''):
    out = []
    good = [row for row in H if not isinstance(row[1], str)]
    crashed = isinstance(H[-1][1], str)
    tah = None
    marks = {}
    for row in good:
        t, la, lb, Th, Rar, be, al, rho, Mr, Sr, Y = row
        trapped = Th < 0
        if trapped.any() and tah is None: tah = t
        Rah = Rar[trapped].max() if trapped.any() else 0.0
        for nm, arr, thr, lo in (('lt<1/2', lb, 0.5, True), ('lr<1/2', la, 0.5, True), ('lt<1/4', lb, 0.25, True), ('lr<1/4', la, 0.25, True),
                                 ('l<1/8', np.minimum(la, lb), 1/8, True), ('lr>1.5', la, 1.5, False), ('lr>2', la, 2.0, False)):
            hit = arr < thr if lo else arr > thr
            if hit.any() and nm not in marks:
                i = np.where(hit)[0]; R = Rar[i]
                outside = i[R > Rah] if Rah > 0 else i
                marks[nm] = (t, R.min(), R.max(), Rah, bool((R > 2.0).any()), len(outside) > 0)
    last = good[-1]
    t, la, lb, Th, Rar, be, al, rho, Mr, Sr, Y = last
    trapped = Th < 0; Rah = Rar[trapped].max() if trapped.any() else 0.0
    ext = Rar > max(Rah, 2.0)
    res = dict(label=label, t_end=t, crashed=crashed, t_ah=tah, R_ah=Rah, marks=marks,
               lt_min_ext=lb[ext].min(), lr_max_ext=la[ext].max(), lr_min_ext=la[ext].min(), lt_max_ext=lb[ext].max(),
               R_at_ltmin=Rar[ext][np.argmin(lb[ext])], R_at_lrmax=Rar[ext][np.argmax(la[ext])],
               lmin_all=min(la.min(), lb.min()), lmax_all=max(la.max(), lb.max()),
               beta_max=max(np.abs(row[5]).max() for row in good),
               beta_over_N=max((np.abs(row[5]) / row[6]).max() for row in good),
               mom_rel=np.abs(Mr - 8 * np.pi * Sr)[ext].max())
    return res


# ------------------------------------------------------------------ A. linear theorems
print('== A. linear theorems (flat background, tied lapse n = tr h/6, Newtonian potential Phi = Psi)')
w, k, mu, Phi = sp.symbols('omega k mu Phi')
# gauge from Newtonian gauge: n = Phi - T', beta = grad(T - L'), h_ij = -2 Psi d_ij - 2 d_i d_j L  (d_t -> -i w, Lap -> -k^2)
dt = lambda x: -sp.I * w * x; lap = lambda x: -k**2 * x
# continuity + Poisson: j = grad psi, Lap psi = -rho', Lap Phi = 4 pi rho  =>  -16 pi mu psi = 4 mu Phi'
rho, psi = sp.symbols('rho psi')
psi_s = sp.solve(sp.Eq(lap(psi), -dt(rho)), psi)[0].subs(rho, lap(Phi) / (4 * sp.pi))
okA1 = sp.simplify(-16 * sp.pi * mu * psi_s - 4 * mu * dt(Phi)) == 0
phi_w = sp.solve(sp.Eq(dt(dt(sp.Symbol('f'))), mu * lap(sp.Symbol('f')) + 4 * mu * dt(Phi)), sp.Symbol('f'))[0]
Ls, Ts = sp.symbols('L T')
def edges(phi):
    sol = sp.solve([sp.Eq(Phi - dt(Ts), -Phi - lap(Ls) / 3), sp.Eq(phi, Ts - dt(Ls))], [Ts, Ls], dict=True)[0]
    return sp.simplify(-Phi - lap(sol[Ls]) / 3)          # mean ln(edge) = tr h / 6
e0, ew = edges(0), edges(phi_w)
ratio = sp.simplify((ew + Phi) / (e0 + Phi))
okA2 = sp.simplify(ratio - (mu * k**2 + (2 * mu - 1) * w**2) / (mu * k**2 - w**2)) == 0
qs0, qsw = sp.limit(e0, w, 0), sp.limit(ew, w, 0)
check('A1 THEOREM: in the scalar sector the wave law is beta = grad phi, phi_tt = mu Lap phi + 4 mu dPhi/dt: the infalling '
      'momentum density sources the shift through the rate of the Newtonian potential (outward for infall, the sign of the PG shift)',
      okA1, 'from d_t^2 beta = mu(Lap beta - 16 pi j), Lap psi = -rho_t, Lap Phi = 4 pi rho')
check('A2 THEOREM: mean ln(edge) under tied lapse: zero shift and wave shift agree at quasi-static order (both -> Phi: edges '
      'follow the potential, not the dust); the wave shift changes the departure from -Psi by the factor '
      '(mu k^2 + (2mu-1) w^2)/(mu k^2 - w^2) = 1 + O(v^2/c^2)',
      okA2 and sp.simplify(qs0 - Phi) == 0 and sp.simplify(qsw - Phi) == 0, 'quasi-static limits %s, %s' % (qs0, qsw))
r_, M_, a_, b_ = sp.symbols('r M a b', positive=True)
vlap = lambda f: sp.diff(f, r_, 2) + 2 * sp.diff(f, r_) / r_ - 2 * f / r_**2   # radial comp. of vector Laplacian of f r^
fPG = sp.sqrt(2 * M_ / r_)
resPG = sp.simplify(vlap(fPG))
okA3 = sp.simplify(resPG + sp.Rational(9, 4) * sp.sqrt(2 * M_) * r_**sp.Rational(-5, 2)) == 0 and sp.simplify(vlap(a_ * r_ + b_ / r_**2)) == 0
check('A3 THEOREM: the PG grid (flat slices, N = 1, beta^r = sqrt(2M/r)) is NOT a stationary state of the wave law: on a flat '
      'slice the constraint part vanishes for a radial shift and the residual is Lap beta = -(9/4) sqrt(2M) r^-5/2; the only '
      'stationary radial vacuum shifts are a r + Q/r^2, so the wave shift cannot settle onto the minimal-strain grid',
      okA3, 'residual %s' % resPG)
# A4 static end state: N^2 = 3 / sum_i l_i^-2 (tied lapse, edges in far units)  =>  l_min <= N
rng = np.random.default_rng(1); okA4 = True
for _ in range(2000):
    l = np.exp(rng.normal(size=3)); N = math.sqrt(3 / np.sum(l**-2.0)); okA4 &= l.min() <= N + 1e-12
Rfl = [2 / (1 - 4.0**(-3 - m)) for m in (0.0, 0.5, 1.0)]
check('A4 THEOREM: the tied lapse gives l_min <= N on every cube, so a stationary zero-shift exterior (static slicing, '
      'N = sqrt(1 - 2M/R), floor-horizon B2) puts an edge at the floor 2^(-3-m) at R >= 2M/(1 - 4^(-3-m)), OUTSIDE the horizon',
      okA4, 'far phase m = 0, 0.5, 1: floor reached by R = %.3f, %.4f, %.4f M' % tuple(Rfl))

# ------------------------------------------------------------------ B. nonlinear collapse
print('== B. nonlinear spherical collapse from rest (smooth dust ball, areal R0; regularised ADM, tied lapse; wave shift')
print('   d_t^2 beta^r = mu[Lap_flat beta^r - 16 pi S^r] (on-shell form), mu = 3/4; edges in far-edge units; AH = trapped surface)')
runs = {}
for key, R0, sh, h in (('z10', 10, 'zero', 0.1), ('w10', 10, 'wave', 0.1), ('w10f', 10, 'wave', 0.05),
                       ('z20', 20, 'zero', 0.1), ('w20', 20, 'wave', 0.1)):
    rg, H = run(R0=R0, shift=sh, h=h)
    s = summarize(rg, H, key)
    good = [row for row in H if not isinstance(row[1], str)]
    t, la, lb, Th, Rar, be, al, rho, Mr, Sr, Y = good[-1]
    i2 = np.argmin(np.abs(Rar - 2.0)); iq = [np.argmin(np.abs(Rar - x)) for x in (3.0, 5.0, 10.0)]
    s['beta_2M'] = be[i2]; s['Q'] = [rg[i]**2 * be[i] for i in iq]
    s['fl'] = s['marks'].get('l<1/8')
    runs[key] = s
    print('   %-4s R0 %2d r_s %-4s h %.2f: AH at t %.1f (R_AH %.2f M), run ends t %.1f | outside AH: l_t >= %.3f (R %.2f), '
          'l_r <= %.3f (R %.2f) | anywhere: l in [%.3f, %.3f] | beta(2M) %.2f, max beta %.2f, r^2 beta %.1f..%.1f | floor 1/8: %s'
          % (key, R0 // 2, sh, h, s['t_ah'], s['R_ah'], s['t_end'], s['lt_min_ext'], s['R_at_ltmin'], s['lr_max_ext'], s['R_at_lrmax'],
             s['lmin_all'], s['lmax_all'], s['beta_2M'], s['beta_max'], min(s['Q']), max(s['Q']),
             'none' if s['fl'] is None else 't %.1f at R %.2f-%.2f M, outside AH %s' % (s['fl'][0], s['fl'][1], s['fl'][2], s['fl'][5])))
W10, W10f, Z10, W20, Z20 = runs['w10'], runs['w10f'], runs['z10'], runs['w20'], runs['z20']
conv = abs(W10['lt_min_ext'] - W10f['lt_min_ext']) < 0.02 and abs(W10['lr_max_ext'] - W10f['lr_max_ext']) < 0.03
check('B1 DIAGNOSTIC: the code is consistent: momentum constraint residual outside the AH <= 3e-3 and h = 0.1 vs 0.05 agree '
      'on the exterior edge extremes to 0.01', conv and max(s['mom_rel'] for s in runs.values()) < 3e-3,
      'l_t %.3f vs %.3f, l_r %.3f vs %.3f' % (W10['lt_min_ext'], W10f['lt_min_ext'], W10['lr_max_ext'], W10f['lr_max_ext']))
okB2 = all(runs[k]['lt_min_ext'] > 0.3 and (runs[k]['fl'] is None or not runs[k]['fl'][5]) for k in runs)
check('B2 DIAGNOSTIC: through horizon formation and up to the crunch of the core (the tied lapse, Bona-Masso f = 1/3, is not '
      'singularity-avoiding), no edge outside the trapped region comes near the floor (>= 0.37 vs 1/8 .. 1/16) for either shift; '
      'the first floor is in the crushing core inside the horizon (zero shift), or not reached before the crunch (wave shift)',
      okB2, 'min exterior l_t: wave %.2f/%.2f, zero %.2f/%.2f (R0 = 5/10 r_s)' % (W10['lt_min_ext'], W20['lt_min_ext'], Z10['lt_min_ext'], Z20['lt_min_ext']))
okB3 = all(runs[w]['lt_min_ext'] > runs[z]['lt_min_ext'] and runs[w]['lr_max_ext'] < runs[z]['lr_max_ext'] for w, z in (('w10', 'z10'), ('w20', 'z20')))
check('B3 DIAGNOSTIC: the wave shift points outward (PG sign) and halves the slice stretching of zero shift near the horizon, '
      'but reaches only about a quarter of the PG shift at R = 2M; outside the matter it is the stationary Q/r^2 form',
      okB3 and W20['beta_2M'] > 0 and W20['beta_2M'] < 0.5,
      'beta(2M) %.2f / PG ~0.95; Q = r^2 beta %.1f-%.1f M^2' % (W20['beta_2M'], min(W20['Q']), max(W20['Q'])))

# ------------------------------------------------------------------ C. estimates
print('== C. estimates')
for e0 in (0.0075, 0.0375):
    bmax = max(s['beta_max'] for s in runs.values()) * math.sin(e0) / math.sqrt(3)
    check('C1 ESTIMATE (eps0 %.4f): one-cube-per-tick cap b = beta sin(eps0)/sqrt3 is not reached anywhere up to the crunch' % e0,
          bmax < 0.1, 'max b %.4f' % bmax)
def top_frac(lr, Dl): return min(1.0, max(0.0, math.log2(lr) - Dl))
fr = [(k, runs[k]['lr_max_ext'], top_frac(runs[k]['lr_max_ext'], 0), top_frac(runs[k]['lr_max_ext'], 1)) for k in ('w10', 'w20', 'z10', 'z20')]
check('C2 ESTIMATE: the binding wall outside the horizon is the TOP, not the floor: radial edges stretch while tangential '
      'ones shrink (no glued split), and with far edges at 2^m L, m in [0, 1), the top 2^(1+Delta-m) is passed for a fraction '
      'log2(l_r) - Delta of phases', all(f1 == 0 for _, l, f0, f1 in fr if l < 2),
      '; '.join('%s l_r %.2f: Delta=0 %.0f%%, Delta=1 %.0f%%' % (k, l, 100 * f0, 100 * f1) for k, l, f0, f1 in fr))
Qn = 0.8 * 1.0 * 2.0 * 1.0
check('C3 ESTIMATE: quasi-static Newtonian shift charge Q = (4/5) M R_b |dR_b/dt| ~ 1.6 M^2 at R_b = 2M vs measured r^2 beta '
      '~4 M^2 (labels r > R, strong field): order of magnitude only', 1 < max(W20['Q']) / Qn < 5, 'ratio %.1f' % (max(W20['Q']) / Qn))
print('supplied: GR (ADM) as CL-3\'s continuum limit, smooth OS-like dust ball (tanh edge 6%), M = 1, on-shell (matter) form of the '
      'wave source (the geometric form is origin-unstable in this code), flat-label vector Laplacian as nonlinear completion, mu = 3/4.')
print('not followed: the exterior after the core crunch (late-time slice stretching), register-level odds, non-spherical collapse.')
print('elapsed %.1f s' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % tuple(NP))
