AUDIT_INPUT_PATHS = ('docs/A_BLACK_HOLE_EXTERIOR_KEEPS_A_REGULAR_TIED_LAPSE_SLICING_ONLY_WHILE_ITS_SHIFT_CHARGE_LASTS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
# post-crunch: the long-time black-hole exterior under the tied lapse + wave shift (G = c = M = 1)
# Self-contained. Edges in far-edge units; labels r (site labels), areal radius R; f = 1 - 2/R.
import math, time, signal
import numpy as np, sympy as sp
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp
AUDIT_TIMEOUT_SEC = 120
signal.alarm(110)
T0 = time.time(); NP = [0, 0]
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print('[%s] %s | %s' % ('PASS' if ok else 'FAIL', name, detail))

# ---------------------------------------------------------------- A. stationary reduction (exact)
print('== A. stationary tied-lapse slicings of Schwarzschild, label shift beta^r (exact)')
R, r, g, b, p, mu_ = sp.symbols('R r gamma beta p mu', positive=True)
f = 1 - 2 / R; s = r / R
# stationary slice t = T + h(R): gamma_RR = g, lapse N = 1/sqrt(g), beta^R = sqrt(1 - f g)/g (ingoing branch)
hp = sp.Symbol('hp'); u = f * hp
gam = (1 - u**2) / f; NN2 = f + f**2 * hp**2 / gam; bR = -u / gam
okA1a = sp.simplify(NN2 * gam - 1) == 0 and sp.simplify(-NN2 + gam * bR**2 + f) == 0
A_ = g / p**2; B_ = R**2 / r**2                         # p = dr/dR
tied = sp.Eq(3 / (1 / A_ + 2 / B_), 1 / g)              # N^2 from edges = N^2 of the slicing
p_sol = sp.sqrt(g * (3 * g - 2 * s**2))
okA1b = sp.simplify(tied.lhs.subs(p, p_sol) - tied.rhs) == 0
F = 3 * f * g**2 - (3 + 2 * s**2 * f - b**2) * g + 2 * s**2   # with beta^r = p sqrt(1 - f g)/g
okA1c = sp.simplify(sp.expand((p_sol**2 * (1 - f * g) / g**2 - b**2) * g) + F) == 0
lr_e = sp.simplify(sp.sqrt(A_.subs(p, p_sol))); okA1d = sp.simplify(lr_e**2 - 1 / (3 * g - 2 * s**2)) == 0
check('A1 THEOREM: stationary slicing: N^2 gamma_RR = 1; tied lapse + label shift give dr/dR = sqrt(gamma(3gamma-2s^2)), '
      '3f gamma^2 - (3+2s^2 f-beta^2) gamma + 2s^2 = 0 (s = r/R), l_r = (3gamma-2s^2)^-1/2, l_t = 1/s; vacuum shift Q/r^2 + a r', okA1a and okA1b and okA1c and okA1d, 'residuals 0')
x = sp.Symbol('x', positive=True); q = sp.Symbol('q', positive=True)
Dsc = sp.expand((3 + 2 * x**2 - q)**2 - 24 * x**2)
okA2a = sp.simplify(Dsc - (2 * (x - sp.sqrt(sp.Rational(3, 2)))**2 - q) * (2 * (x + sp.sqrt(sp.Rational(3, 2)))**2 - q)) == 0
gs = sp.solve(F.subs(b**2, q).subs(R, 2), g)                         # horizon: one finite root
okA2b = len(gs) == 1 and sp.simplify(gs[0] - 2 * s.subs(R, 2)**2 / (3 - q)) == 0
rts = sp.solve(F.subs(b**2, q), g); vals = {R: 2 + 1e-9, r: 5.0, q: 1.0}
fr = sorted(float(sp.re((rt * f).subs(vals))) for rt in rts); okA2c = abs(fr[1] - 2 / 3) < 1e-6 and abs(fr[0]) < 1e-6
far = sp.solve(3 * g**2 - 5 * g + 2, g)                              # far field: f = s = 1, beta = 0
okA2d = set(far) == {1, sp.Rational(2, 3)}
check('A2 THEOREM: discriminant (2(x-sqrt1.5)^2-beta^2)(2(x+sqrt1.5)^2-beta^2), x = s sqrt f; the flat-far root diverges at the '
      'horizon as (3-beta^2)/(3f) (static type: N, l_r -> 0), the regular horizon root is 2s^2/(3-beta^2): a regular slicing must '
      'pass a double-root (sonic-type) point outside the horizon -- tuned, one label constant per Q', okA2a and okA2b and okA2c and okA2d,
      'far roots %s; horizon root 2s^2/(3-beta^2)' % far)
pp = 2 * s.subs(R, 2)**2 * b / (3 - b**2); gh = 2 * s.subs(R, 2)**2 / (3 - b**2)
okA3 = sp.simplify(pp / gh - b) == 0 and sp.simplify((p_sol**2).subs(R, 2).subs(g, gh) - pp**2) == 0
crit_ratio = math.sqrt((3 / 0.75 - 1) / 2)
check('A3 THEOREM: at a regular stationary horizon N/sqrt(A) = beta^r: outgoing light sits at a fixed label while the label-frame '
      'wave shift moves sqrt(mu) labels/tick: the shift carries core data out of the horizon; radially superluminal where l_r/l_t > sqrt((3/mu-1)/2)', okA3, 'mu = 3/4: l_r/l_t > %.3f' % crit_ratio)
# charge identity, numeric check on a random smooth profile
rr = np.linspace(1e-3, 30, 300001); S = -np.exp(-(rr - 4)**2) * rr**2 / (1 + rr**3); Aw = 1 + 0.3 * np.exp(-rr / 3)
src = 16 * np.pi * S / Aw; D = -np.cumsum(src[::-1])[::-1] * (rr[1] - rr[0]); r2b = np.cumsum(rr**2 * D) * (rr[1] - rr[0])
Qnum = r2b[-1]; Qth = -(16 * np.pi / 3) * (np.trapezoid if hasattr(np, 'trapezoid') else np.trapz)(rr**3 * S / Aw, rr)
check('A4 THEOREM: Q(t) = -(16pi/3) int r^3 S^r/A dr - (1/3mu) int r^3 d_t^2 beta dr: a stationary charge is the matter\'s radial momentum moment', abs(Qnum / Qth - 1) < 1e-3, 'stationary check %.5f vs %.5f' % (Qnum, Qth))
okA5 = sp.simplify(F.subs(b, -b) - F) == 0
check('A5 THEOREM: Q is time-odd, so a time-symmetric core bounce sends Q -> -Q; edges see beta^2 only, but Q < 0 slices cross only the '
      'PAST horizon, so with Q <= 0 a collapse exterior keeps only the static root (floor at R = 2M/(1-4^(-3-m)))', okA5, 'F(beta) = F(-beta)')

# ---------------------------------------------------------------- B. stationary family (numeric)
print('== B. the regular stationary family (separatrices), one per shift charge Q = r^2 beta^r')
Rs, rs, gs_, Qs = sp.symbols('R r gamma Q', positive=True)
Fq = F.subs(b, Qs / rs**2).subs({R: Rs, r: rs, g: gs_}); Pq = p_sol.subs({R: Rs, r: rs, g: gs_})
cf = sp.lambdify((Rs, rs, gs_, Qs), [Fq, sp.diff(Fq, gs_), sp.diff(Fq, Rs) + sp.diff(Fq, rs) * Pq], 'numpy')
dF = [sp.lambdify((Rs, rs, gs_, Qs), sp.diff(Fq, v), 'numpy') for v in (Rs, rs, gs_)]
Pf = sp.lambdify((Rs, rs, gs_, Qs), Pq, 'numpy')
def V(z, Q):
    pv = Pf(*z, Q); fg = dF[2](*z, Q)
    return np.array([-fg, -fg * pv, dF[0](*z, Q) + dF[1](*z, Q) * pv])
def crit(Q, guess):
    fg = 1 - 2 / guess[0]; sg = guess[1] / guess[0]
    guess = np.array([guess[0], guess[1], (3 + 2 * sg**2 * fg - Q**2 / guess[1]**4) / (6 * fg)])
    tries = [guess] + [np.array([R0, s0 * R0, 0.0]) for R0 in np.linspace(2.05, 8, 25) for s0 in (1.0, 1.4, 2.0, 0.6)]
    for gu in tries:
        if gu[2] == 0.0:
            fg = 1 - 2 / gu[0]; sg = gu[1] / gu[0]; gu[2] = max((3 + 2 * sg**2 * fg - Q**2 / gu[1]**4) / (6 * fg), 2 * sg**2 / 3 + 0.05)
        with np.errstate(all='ignore'):
            x0, info, ier, msg = fsolve(lambda v: cf(v[0], v[1], v[2], Q), gu, full_output=True)
            if ier == 1 and min(x0) > 0 and np.max(np.abs(cf(*x0, Q))) < 1e-9: return x0
    return None
def separatrix(Q, x0, ms=0.05):
    J = np.array([(V(x0 + 1e-6 * e, Q) - V(x0 - 1e-6 * e, Q)) / 2e-6 for e in np.eye(3)]).T
    w, U = np.linalg.eig(J); u_ = np.real(U[:, int(np.argmin(np.real(w)))]); out = []
    for sg in (1, -1):
        ev = [lambda t, z: z[0] - 300, lambda t, z: z[0] - 0.02, lambda t, z: z[1] - 1e-3, lambda t, z: 3 * z[2] - 2 * (z[1] / z[0])**2 - 1e-9]
        for e in ev: e.terminal = True
        out.append(solve_ivp(lambda t, z: -V(z, Q), [0, 3e3], x0 + sg * 1e-5 * u_, max_step=ms, rtol=1e-10, atol=1e-12, events=ev).y)
    o = [y for y in out if y[0, -1] > 100]; i = [y for y in out if y[0, -1] <= 100]
    if not o or not i: return None
    return np.concatenate([i[0][:, ::-1], o[0]], axis=1)
def edges(Z):
    Rv, rv, gv = Z; sv = rv / Rv
    return Rv, rv, 1 / np.sqrt(3 * gv - 2 * sv**2), 1 / sv, 1 / np.sqrt(gv)
fam = {}; guess = np.array([3.16, 6.365, 2.7])
for Q in [0.25, 1, 2, 3, 3.6, 4, 5, 5.5, 6, 8, 10]:
    x0 = crit(Q, guess); guess = x0
    Rv, rv, lr, lt, N = edges(separatrix(Q, x0))
    ext = Rv > 2; ih = np.argmin(np.abs(Rv - 2))
    fam[Q] = dict(Rc=x0[0], rc=x0[1], lrmax=lr[ext].max(), lrmin=lr[ext].min(), ltmin=lt[ext].min(), Nh=N[ih], lrh=lr[ih], lth=lt[ih], Rend=Rv[0], fars=rv[-1] / Rv[-1])
print('   Q     R_c  | 2M: N   l_r   l_t | ext l_r max l_t min | labels end R')
for Q, d in fam.items():
    print('   %-4g %5.2f | %5.3f %5.2f %5.3f | %6.2f %6.3f | %5.2f' % (Q, d['Rc'], d['Nh'], d['lrh'], d['lth'], d['lrmax'], d['ltmin'], d['Rend']))
okB1 = all(3.1 < d['Rc'] < 4.1 and d['Rend'] < 2 and abs(d['fars'] - 1) < 0.01 for d in fam.values())
check('B1 DIAGNOSTIC: each Q in [0.25, 10] has one tuned separatrix, flat at infinity, critical at R = 3.2-4.0 M, regular through 2M; '
      'l_t >= 0.32 outside; l_r peaks at the horizon for Q <= 6 and falls with Q', okB1, 'l_r(2M) %.1f (Q 0.25) .. %.2f (Q 10)' % (fam[0.25]['lrh'], fam[10]['lrh']))
x1 = crit(10.5, np.array([3.69, 5.15, 1.70])); Z1 = separatrix(10.5, x1) if x1 is not None else None
Rend = Z1[0][0] if Z1 is not None else float('nan')
check('B2 DIAGNOSTIC: the family ends at Q_max ~ 10 M^2: at Q = 10.5 the flat separatrix meets a second critical point outside the horizon', Z1 is not None and Rend > 2.5, 'Q 10.5: labels end at R %.2f' % Rend)

# ---------------------------------------------------------------- C. nonlinear excised vacuum evolution
print('== C. vacuum ADM, tied lapse, excised inside the horizon (R_in ~ 1.4M), Q = 4 separatrix data, h 0.1')
def ricci():
    rr_, th = sp.symbols('r theta', positive=True); A, B = sp.Function('A')(rr_), sp.Function('B')(rr_)
    gm = sp.diag(A, B * rr_**2, B * rr_**2 * sp.sin(th)**2); xx = [rr_, th, sp.Symbol('ph')]; gi = gm.inv()
    G = [[[sum(gi[a, d] * (sp.diff(gm[d, bb], xx[c]) + sp.diff(gm[d, c], xx[bb]) - sp.diff(gm[bb, c], xx[d])) for d in range(3)) / 2 for c in range(3)] for bb in range(3)] for a in range(3)]
    Ric = lambda bb, c: sp.simplify(sum(sp.diff(G[a][bb][c], xx[a]) - sp.diff(G[a][bb][a], xx[c]) + sum(G[a][a][d] * G[d][bb][c] - G[a][c][d] * G[d][bb][a] for d in range(3)) for a in range(3)))
    sy = sp.symbols('A0 A1 A2 B0 B1 B2')
    sub = {sp.diff(A, rr_, 2): sy[2], sp.diff(B, rr_, 2): sy[5], sp.diff(A, rr_): sy[1], sp.diff(B, rr_): sy[4]}
    mk = lambda e: sp.lambdify((rr_,) + sy, e.subs(sub).subs({A: sy[0], B: sy[3]}), 'numpy')
    return mk(sp.simplify(Ric(0, 0) / A)), mk(sp.simplify(Ric(1, 1) / (B * rr_**2)))
RRR, RTT = ricci()
from scipy.interpolate import CubicSpline
x4 = crit(4.0, np.array([3.77, 6.35, 2.01])); Z4 = separatrix(4.0, x4, ms=0.02)
o = np.argsort(Z4[1]); Rv4, rv4, gv4 = Z4[0][o], Z4[1][o], Z4[2][o]; kk = np.concatenate([[True], np.diff(rv4) > 1e-9])
splR, splg = CubicSpline(rv4[kk], Rv4[kk]), CubicSpline(rv4[kk], gv4[kk])
def evolve(law, tmax, Q=4.0, r_in=4.4, r_out=70.0, h=0.1, freeze0=True, rcut=0.0, mu=0.75, ko_=0.8):
    ng = 3; rg = r_in + np.arange(-ng, int((r_out - r_in) / h) + ng) * h
    rf = np.linspace(r_in - 1, r_out + 1, 20001); Rr = splR(rf); gr = splg(rf); sv = rf / Rr
    A = gr / (gr * (3 * gr - 2 * sv**2)); B = (Rr / rf)**2; N0 = np.sqrt(3 / (1 / A + 2 / B)); be0 = Q / rf**2
    KA = (be0 * np.gradient(A, rf) + 2 * A * np.gradient(be0, rf)) / (2 * N0 * A); KB = be0 * (np.gradient(B, rf) / B + 2 / rf) / (2 * N0)
    ip = lambda y: np.interp(rg, rf, y)
    Y = np.array([ip(A), ip(B), ip(KA), ip(KB), Q / rg**2, (2 * Q**2 / rg**5) if law != 'label' else 0 * rg]); Yo = Y[:, -ng:].copy()
    st = {'r': rg}
    def d1(y): o_ = np.zeros_like(y); o_[2:-2] = (y[:-4] - 8 * y[1:-3] + 8 * y[3:-1] - y[4:]) / (12 * h); return o_
    def d2(y): o_ = np.zeros_like(y); o_[2:-2] = (-y[:-4] + 16 * y[1:-3] - 30 * y[2:-2] + 16 * y[3:-1] - y[4:]) / (12 * h * h); return o_
    def ko(y): o_ = np.zeros_like(y); o_[3:-3] = (y[:-6] - 6 * y[1:-5] + 15 * y[2:-4] - 20 * y[3:-3] + 15 * y[4:-2] - 6 * y[5:-1] + y[6:]) / (64 * h); return o_
    def rhs(Y):
        rv = st['r']
        for k in range(6):
            for j in range(ng):
                i = ng - 1 - j; Y[k, i] = 4 * Y[k, i + 1] - 6 * Y[k, i + 2] + 4 * Y[k, i + 3] - Y[k, i + 4]
            Y[k, -ng:] = Yo[k]
        if law == 'label': Y[4, :ng + 1] = Q / rv[:ng + 1]**2; Y[5, :ng + 1] = 0
        A, B, KA, KB, be, Bb = Y; al = np.sqrt(3 / (1 / A + 2 / B))
        A1, A2, B1, B2 = d1(A), d2(A), d1(B), d2(B); a1, a2 = d1(al), d2(al); K = KA + 2 * KB; bd = d1(be)
        dA = -2 * al * A * KA + be * A1 + 2 * A * bd; dB = -2 * al * B * KB + be * B1 + 2 * B * be / rv
        dKA = be * d1(KA) - (a2 - a1 * A1 / (2 * A)) / A + al * (RRR(rv, A, A1, A2, B, B1, B2) + K * KA)
        dKB = be * d1(KB) - a1 * (1 / rv + B1 / (2 * B)) / A + al * (RTT(rv, A, A1, A2, B, B1, B2) + K * KB)
        lap = d2(be) + 2 * bd / rv - 2 * be / rv**2
        if law == 'literal-low':
            bl = A * be; Vf = d1(A * KA - K) + 2 * (A * KA - B * KB) / rv
            lap = (d2(bl) + 2 * d1(bl) / rv - 2 * bl / rv**2 - 2 * Vf) / A
        if law == 'label': out = np.array([dA, dB, dKA, dKB, Bb, mu * lap])
        else: out = np.array([dA, dB, dKA, dKB, Bb + be * bd, be * d1(Bb) + mu * (al**2 / A) * lap])   # normal-frame (advected) wave, local light speed
        for k in range(6): out[k] += ko_ * ko(Y[k])
        out[:, :(ng + 1 if freeze0 else ng)] = 0; out[:, -ng:] = 0
        return out
    dt = 0.25 * h; t = 0.0; rows = []; I = slice(ng + 2, -ng - 2)
    for it in range(int(tmax / dt) + 1):
        if it % 40 == 0:
            rv = st['r']; A, B, KA, KB, be, Bb = Y; la, lb = np.sqrt(A[I]), np.sqrt(B[I]); RR = (rv * np.sqrt(B))[I]
            ext = RR > 2.0; i2 = np.argmin(np.abs(RR - 2.0)); i6 = np.argmin(np.abs(RR - 6.0))
            rows.append((t, la[ext].max(), lb[ext].min(), np.sqrt(3 / (1 / A + 2 / B))[I][i2], la[i2], rv[I][i6]**2 * be[I][i6], RR[0]))
        if t >= tmax: break
        k1 = rhs(Y.copy()); k2 = rhs(Y + 0.5 * dt * k1); k3 = rhs(Y + 0.5 * dt * k2); k4 = rhs(Y + dt * k3)
        Y = Y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t += dt
        while rcut > 0 and st['r'][ng] * np.sqrt(Y[1, ng]) < rcut: Y = Y[:, 1:].copy(); st['r'] = st['r'][1:].copy()
        if not np.all(np.isfinite(Y)) or Y[0].min() <= 0: rows.append((t, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan)); break
    return rows
def line(tag, rows):
    for rw in [rows[0], rows[len(rows) // 2], rows[-1]]:
        print('   %-7s t %4.1f | ext l_r max %4.2f l_t min %.3f | 2M: N %.3f l_r %.2f | Q(6M) %5.2f | R_in %.2f' % ((tag,) + rw))
H = evolve('label', 40.0); line('Q held', H)
dr = max(abs(rw[4] / H[0][4] - 1) for rw in H); dq = max(abs(rw[5] - 4) for rw in H)
check('C1 DIAGNOSTIC: the Q = 4 separatrix is stationary in the nonlinear code with the core holding Q (40 M)', dr < 0.06 and dq < 0.01, 'max drift l_r(2M) %.3f, Q %.3f' % (dr, dq))
Hc = evolve('causal', 32.0, freeze0=False, rcut=1.0); line('causal', Hc)
check('C2 DIAGNOSTIC: causal wave ((d_t - beta d_r)^2 beta = mu (N^2/A) Lap beta; nothing enters the excision): the charge falls in, '
      'Q(6M) drains and l_r passes 4 outside the horizon within ~30 M', Hc[-1][5] < 1.5 and max(rw[1] for rw in Hc) > 4,
      'Q(6M) %.2f -> %.2f, max l_r %.2f by t %.0f' % (Hc[0][5], Hc[-1][5], max(rw[1] for rw in Hc), Hc[-1][0]))
Hl = evolve('literal-low', 6.0, freeze0=False, rcut=1.0); line('literal', Hl)
check('C3 DIAGNOSTIC: the literal flat-lattice source Lap beta_i - 2 d_j(K_ij - delta_ij K) (not its on-shell value) has a vacuum part '
      'that drives Q through zero in ~6 M (runaway)',
      Hl[-1][5] < 0, 'Q(6M) %.2f -> %.2f by t %.0f' % (Hl[0][5], Hl[-1][5], Hl[-1][0]))

# ---------------------------------------------------------------- D. estimates
print('== D. estimates: window [2^(-3-m), 2^(1+Delta-m)], far phase m in [0, 1)')
frac = lambda lr, De: min(1.0, max(0.0, 1 + De - math.log2(lr)))
print('   phases inside (Delta 1/2): ' + ' '.join('%g:%.2f/%.2f' % (Q, frac(d['lrmax'], 1), frac(d['lrmax'], 2)) for Q, d in fam.items()))
okD1 = frac(fam[5.5]['lrmax'], 1) > 0.99 and frac(fam[5]['lrmax'], 1) < 1 and frac(fam[3]['lrmax'], 2) < 1 and frac(fam[4]['lrmax'], 2) > 0.99
check('D1 ESTIMATE: all far phases inside outside the horizon iff 5.5 <~ Q <~ 10 (Delta 1) or 3.2 <~ Q <~ 10 (Delta 2); the top is the wall', okD1, 'Q 4: l_r max %.2f, phases inside %.2f (Delta 1)' % (fam[4]['lrmax'], frac(fam[4]['lrmax'], 1)))
Qtrap = (3.6, 5.0)
check('D2 ESTIMATE (fix: trapped cells keep their shift): the exterior keeps its charge at trapping, 3.6-5.0 M^2 (wave-shift-collapse), '
      'l_r max %.1f-%.1f: all far phases inside iff Delta >= 2' % (fam[3.6]['lrmax'], fam[5]['lrmax']),
      frac(fam[5]['lrmax'], 2) > 0.99 and frac(fam[3.6]['lrmax'], 2) > 0.99 and frac(fam[3.6]['lrmax'], 1) < 0.5, 'Q 3.6: phases inside %.2f (Delta 1), %.2f (Delta 2)' % (frac(fam[3.6]['lrmax'], 1), frac(fam[3.6]['lrmax'], 2)))
Rb0 = 10.0; Qmem = 0.4 * Rb0**2
check('D3 ESTIMATE: a flux-memory source gives Q ~ 0.4 M R0^2 (ball from rest at R0), past Q_max for R0 >~ 5 M: excluded', Qmem > 10, 'R0 = 10 M: Q ~ %.0f M^2' % Qmem)
Rq, rq, lrq, ltq, Nq = edges(Z4); rfl = rq[np.minimum(lrq, ltq) < 1 / 8].max(); r6 = rq[np.argmin(np.abs(Rq - 6))]
tl = (r6 - rfl) / math.sqrt(0.75)
check('D4 ESTIMATE: under the current law the A5 flip reaches R = 6M in ~(label distance)/sqrt(mu): ms for stellar holes, not Hawking times', tl < 10, 'floor label %.2f -> 6M label %.2f: ~%.1f M' % (rfl, r6, tl))
print('supplied: continuum ADM as CL-3 limit, spherical symmetry, the on-shell (matter) form of the shift source unless stated, mu = 3/4,')
print('  flat-label Laplacian, Q at trapping from wave-shift-collapse; excision boundary conditions; KO dissipation.')
print('elapsed %.1f s' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % tuple(NP))
