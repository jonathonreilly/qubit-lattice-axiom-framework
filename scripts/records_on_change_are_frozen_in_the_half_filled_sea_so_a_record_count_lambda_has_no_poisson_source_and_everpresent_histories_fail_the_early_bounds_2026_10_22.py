AUDIT_INPUT_PATHS = ('docs/RECORDS_ON_CHANGE_ARE_FROZEN_IN_THE_HALF_FILLED_SEA_SO_A_RECORD_COUNT_LAMBDA_HAS_NO_POISSON_SOURCE_AND_EVERPRESENT_HISTORIES_FAIL_THE_EARLY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Everpresent Lambda from record counts: does record-on-change (or a split / Born-coin record rule) give
Poisson counts, and what Lambda, history and (w0, wa) follow?
Self-contained; seeded; numpy/scipy only. Units: rung units, L = sqrt(8 pi) l_P (8 pi G hbar = L^2), c = 1.
Per site and half-tick the proper 4-volume is v_c = (sig/2) L^4, sig = sin(eps0)/sqrt3 (CL-1 fixed lapse).
Supplied: the 1D pair-walk toy (CL-1 gate form, eps = 0.6, mu = 0.3), the half-filled sea, LambdaCDM (Planck 2018),
the eps0 range, the S/V stochastic dynamics (Ahmed-Dodelson-Greene-Sorkin model 1), BBN/CMB bounds (approximate),
DESI DR2 (w0, wa) central values for a box comparison."""
import time, itertools, numpy as np
from scipy.special import logsumexp, beta
from scipy.integrate import quad
from scipy.optimize import linprog
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

# ---------------- toy: 1D pair walk ring, half-filled Floquet sea ----------------
def gates(N, th_e, th_o, phi):
    Ue = np.eye(N, dtype=complex); Uo = np.eye(N, dtype=complex)
    c, s = np.cos(th_e), np.sin(th_e)
    for j in range(0, N, 2):                       # even half-tick exp(-i th_e R), R = pair hop
        Ue[j, j] = Ue[j+1, j+1] = c; Ue[j, j+1] = Ue[j+1, j] = -1j*s
    c, s = np.cos(th_o), np.sin(th_o)
    for j in range(1, N, 2):                       # odd half-tick exp(+i th_o R), ring holonomy phi on the closing bond
        k = (j+1) % N; ph = np.exp(1j*phi) if k == 0 else 1.0
        Uo[j, j] = Uo[k, k] = c; Uo[j, k] = 1j*s*ph; Uo[k, j] = 1j*s*np.conj(ph)
    return Ue, Uo
def sea(N, eps, mu, phi):
    Ue, Uo = gates(N, eps - mu/2, eps + mu/2, phi)
    w, v = np.linalg.eig(Uo @ Ue); idx = np.argsort(np.angle(w))[:N//2]
    Q, _ = np.linalg.qr(v[:, idx]); return Ue, Uo, Q
CONF = {}
def confs(N):
    if N not in CONF:
        cs = list(itertools.combinations(range(N), N//2)); occ = np.zeros((len(cs), N), int)
        for i, c in enumerate(cs): occ[i, list(c)] = 1
        CONF[N] = (cs, occ)
    return CONF[N]
def odds(Phi, cs):
    p = np.array([abs(np.linalg.det(Phi[list(c), :]))**2 for c in cs]); return p/p.sum()
def support(occ, pairs):
    keys = np.stack([occ[:, i] + occ[:, j] for i, j in pairs], 1)
    return (keys[:, None, :] == keys[None, :, :]).all(2)
def plan(p, q, occ, pairs, eps_list=(1, .3, .1, .03), tol=1e-11, it=4000):
    """CL-2 transport: fewest occupation changes, then greatest entropy (eps -> 0 Sinkhorn on the half-tick support)."""
    if 0.5*abs(p - q).sum() < 1e-12: return np.diag(p)   # identical odds: the identity is the unique zero-change plan
    M = support(occ, pairs); C = (occ[:, None, :] != occ[None, :, :]).sum(2).astype(float)
    f = np.zeros(len(p)); g = np.zeros(len(p)); lp, lq = np.log(p), np.log(q)
    for e in eps_list:
        LK = np.where(M, -C/e, -np.inf)
        for k in range(it):
            g = e*(lq - logsumexp(LK + f[:, None]/e, axis=0)); f = e*(lp - logsumexp(LK + g[None, :]/e, axis=1))
            if k % 10 == 0 and abs(np.exp(logsumexp(LK + f[:, None]/e + g[None, :]/e, axis=0)) - q).max() < tol: break
    return np.exp(LK + f[:, None]/e + g[None, :]/e)
def chain(N, eps, mu, phi):
    cs, occ = confs(N); ev = [(j, j+1) for j in range(0, N, 2)]; od = [(j, (j+1) % N) for j in range(1, N, 2)]
    Ue, Uo, Q = sea(N, eps, mu, phi); pA = odds(Q, cs); pB = odds(Ue @ Q, cs)
    return dict(pA=pA, pB=pB, P1=plan(pA, pB, occ, ev), P2=plan(pB, pA, occ, od), occ=occ, Ue=Ue, Uo=Uo, ev=ev)
def counting(ch, W):
    """records-on-change in window W: rate per site per half-tick and long-time Fano factor (tilted Perron root)."""
    occ = ch['occ']; Hw = (occ[:, None, W] != occ[None, :, W]).sum(2).astype(float)
    K1 = ch['P1']/ch['pA'][:, None]; K2 = ch['P2']/ch['pB'][:, None]
    lam = lambda s: np.log(np.max(abs(np.linalg.eigvals((K1*np.exp(s*Hw)) @ (K2*np.exp(s*Hw))))))
    h = 0.02; a, b, c = lam(-h), lam(0.0), lam(h); m = (c - a)/(2*h); v = (c - 2*b + a)/h**2
    return m/2/len(W), (v/m if m > 1e-12 else float('nan'))
EPS, MU = 0.6, 0.3
print("== A. records on change in the half-filled sea (1D pair walk, CL-1 gate form, eps %.1f, mu %.1f)" % (EPS, MU))
# A1 theorem: K (site-diagonal antiunitary) reverses each half-tick when the holonomy is real -> odds equal -> frozen
tvs = []; Krev = []
for N in (8, 10, 12):
    for (e, m) in ((EPS, MU), (0.0375, 0.01)):
        Ue, Uo, Q = sea(N, e, m, np.pi); cs, _ = confs(N)
        Krev.append(max(abs(Ue.conj() - Ue.conj().T).max(), abs(Uo.conj() - Uo.conj().T).max()))
        tvs.append(0.5*abs(odds(Q, cs) - odds(Ue @ Q, cs)).sum())
check("THEOREM: a site-diagonal antiunitary K reversing both half-ticks (K U K = U^dag, real holonomy) gives equal odds at both half-ticks, so the fewest-change transport is the identity: record-on-change makes ZERO vacuum records (count 0, variance 0, Fano 0/0)",
      max(Krev) < 1e-15 and max(tvs) < 1e-12, f"N = 8,10,12, two (eps, mu): |KUK - U^dag| {max(Krev):.0e}, TV(p_A, p_B) <= {max(tvs):.1e}")
# A2 control: ring holonomy breaks K. Rate, window Fano, LP check, size dependence, exact 2pi gauge check
ch = chain(10, EPS, MU, np.pi + 1.0)
res = {w: counting(ch, list(range(w))) for w in (2, 4, 10)}
cs8, occ8 = confs(8); ch8 = chain(8, EPS, MU, np.pi + 1.0)
M = support(occ8, ch8['ev']); C = (occ8[:, None, :] != occ8[None, :, :]).sum(2).astype(float); n8 = len(cs8)
ii, jj = np.where(M); Aeq = np.zeros((2*n8, len(ii))); Aeq[ii, np.arange(len(ii))] = 1; Aeq[n8 + jj, np.arange(len(ii))] = 1
lp = linprog(C[ii, jj], A_eq=Aeq, b_eq=np.r_[ch8['pA'], ch8['pB']], bounds=(0, None), method="highs")
cost_s = (ch8['P1']*C).sum()
check("control (holonomy pi+1 breaks K): the sea moves; the eps->0 entropic plan reaches the LP fewest-change minimum",
      abs(cost_s - lp.fun) < 1e-6*max(lp.fun, 1e-12) + 1e-9, f"N = 8: Sinkhorn {cost_s:.6e} vs LP {lp.fun:.6e} changes per half-tick")
F2, F4, F10 = res[2][1], res[4][1], res[10][1]
check("control counts are COLLECTIVE, not Poisson: the window Fano factor grows in proportion to the window (Var ~ w^2), so a 4-volume count has no sqrt(N) law",
      abs(F10/F2 - 5) < 1.5 and abs(F4/F2 - 2) < 0.4, f"N = 10: rate {res[10][0]:.2e}/site/half-tick; F(w=2) {F2:.2f}, F(4) {F4:.2f}, F(10) {F10:.2f}")
rN = []
for N, chN in ((6, chain(6, EPS, MU, np.pi + 1.0)), (8, ch8), (10, ch)):
    rN.append(counting(chN, list(range(N)))[0])
Ue, Uo, Q = sea(10, EPS, MU, 2*np.pi); tv2pi = 0.5*abs(odds(Q, confs(10)[0]) - odds(Ue @ Q, confs(10)[0])).sum()
check("1D T-breaking is only the ring holonomy mod 2 pi (holonomy 2 pi is exact gauge: frozen); at fixed holonomy the rate per site falls with N, so the bulk vacuum stays frozen",
      tv2pi < 1e-12 and rN[0] > rN[1] > rN[2], f"TV at 2 pi {tv2pi:.0e}; rate N = 6, 8, 10: {rN[0]:.2e}, {rN[1]:.2e}, {rN[2]:.2e}")
# A3 adiabatic drift of the mass angle (expansion reads edges only through mN): local Poisson hops, rate prop. to drift
cs, occ = confs(10); ev = [(j, j+1) for j in range(0, 10, 2)]; out = []
for d in (0.02, 0.005):
    _, _, Q0 = sea(10, EPS, MU, 0.0); p0 = odds(Q0, cs)
    Ue1, _, Q1 = sea(10, EPS, MU + d, 0.0); p1 = odds(Ue1 @ Q1, cs); P = plan(p0, p1, occ, ev)
    Hm = (occ[:, None, :] != occ[None, :, :]).sum(2); m = (P*Hm).sum(); var = (P*Hm**2).sum() - m*m
    H2 = (occ[:, None, :2] != occ[None, :, :2]).sum(2); m2 = (P*H2).sum(); v2 = (P*H2**2).sum() - m2*m2
    Pm = 1 - np.trace(P); Hcond = -(P[P > 0]*np.log(P[P > 0]/np.repeat(p0[:, None], 252, 1)[P > 0])).sum()
    out.append((m/10/d, var/m, v2/m2, Hcond, Pm))
c_ramp = out[1][0]
hb = lambda x: -x*np.log(x) - (1-x)*np.log(1-x)
check("drift of the mass angle mu by d per half-tick: the only structural Poisson-like source: rate c*d per site (c computed), one-step Fano -> 2 (independent single hops), fresh entropy H(Y|X) within the Fano-inequality bound h(P_move) + P_move ln(M-1)",
      abs(out[0][0]/out[1][0] - 1) < 0.03 and abs(out[1][1] - 2) < 0.01 and all(o[3] <= hb(o[4]) + o[4]*np.log(31) + 1e-12 for o in out),
      f"c = {c_ramp:.3f}; F(ring) {out[1][1]:.3f}, F(pair) {out[1][2]:.3f}; H(Y|X) {out[1][3]:.2e} nats/half-tick at d = 0.005")

# ---------------- B. Lambda magnitude with the computed prefactor ----------------
print("== B. Lambda_rms from conjugacy with the record-count 4-volume")
x = np.linspace(-40, 40, 2**14); dxg = x[1] - x[0]; s0 = 1.7; psi = np.exp(-x**2/(4*s0**2)); psi /= np.sqrt((abs(psi)**2).sum()*dxg)
k = 2*np.pi*np.fft.fftfreq(len(x), dxg); pk = abs(np.fft.fft(psi))**2; pk /= pk.sum()
sx = np.sqrt((x**2*abs(psi)**2).sum()*dxg); sk = np.sqrt((k**2*pk).sum())
check("prefactor: phase (Lambda/L^2) V4 makes Lambda/L^2 conjugate to V4; a minimum-uncertainty packet has sigma_V sigma_(Lambda/L^2) = 1/2, so Lambda_rms L^2 = L^4/(2 sigma_V) with sigma_V^2 = (F/r) v_c V4",
      abs(sx*sk - 0.5) < 1e-6, f"Gaussian product {sx*sk:.8f}")
tP = 5.391247e-44; H0 = 67.36e3/3.0857e22; OL, Om, Orad = 0.6847, 0.3153, 9.1e-5
HL = H0*tP*np.sqrt(8*np.pi); LamL2 = 3*OL*HL**2; SIG = np.sin(np.array([0.0075, 0.0375]))/np.sqrt(3)
Hf = lambda a: np.sqrt(Orad/a**4 + Om/a**3 + OL)
chi = lambda a1: quad(lambda y: 1/(y*y*Hf(y)), a1, 1, limit=200)[0]
VH4 = quad(lambda a: (4*np.pi/3)*a**3*chi(a)**3/(a*Hf(a)), 1e-8, 1, limit=200)[0]
u4 = VH4/HL**4                                       # past-cone 4-volume today in L^4
Lam = lambda rF: 0.5*np.sqrt(rF/(SIG/2))/np.sqrt(u4)
r_poi = Lam(1.0)/LamL2
check("imported Poisson record per site per half-tick (r = 1, F = 1), or a Born coin p = 1/2 per site per half-tick (r/F = 1): Lambda_rms overshoots the measured value",
      r_poi.min() > 1, f"V4 = {VH4:.4f} H0^-4 = {u4:.2e} L^4; Lambda_rms/measured = {r_poi.min():.1f} to {r_poi.max():.1f} (eps0 range)")
muT = 172.7/1.2209e19*np.sqrt(8*np.pi)*SIG          # top-quark mass angle per tick, the largest SM mN
r_exp = c_ramp*muT*HL*SIG/2; r_spl = HL*SIG/2/np.log(2)
check("records on change under the laws: vacuum 0 (A1); expansion drives changes only through mass angles (r = c mu_top H sig L/2) and splits at most one random change per site per split: both give Lambda far below measured",
      (Lam(r_exp/2)/LamL2).max() < 1e-30 and (Lam(r_spl/2)/LamL2).max() < 1e-28,
      f"r_exp <= {r_exp.max():.1e} -> {(Lam(r_exp/2)/LamL2).max():.0e} x measured; r_split <= {r_spl.max():.1e} -> {(Lam(r_spl/2)/LamL2).max():.0e} x measured")
A_of = lambda rF: 0.5*np.sqrt(2*rF/SIG)               # S/V amplitude: Lambda L^2 = A * B(u)/u
print(f"  amplitude map: Lambda L^2 = A B(u)/u, B standard Brownian in u = V4/L^4, A = (1/2) sqrt(2 r/(F sig)); ADGS alpha = A/(8 pi);"
      f" Poisson per half-tick gives A = {A_of(1)[1]:.1f} to {A_of(1)[0]:.1f}")

# ---------------- C. stochastic history (ADGS model 1 with computed amplitude) ----------------
print("== C. history: S/V everpresent Lambda on the past light cone, self-consistent Friedmann")
rad, eds = 4*np.pi/840, (4*np.pi/3)*81*beta(9, 4)*16/81
check("THEOREM (tracking): rms Omega_L = A/(3 sqrt(V H^4)) with V H^4 = 4 pi/840 (radiation), 0.0338 (matter, beta function), 0.123 today: Lambda ~ H^2 at every epoch, early rms 2.9x today's",
      abs(rad - 0.014960) < 1e-6 and abs(eds - 0.033849) < 1e-5,
      f"rms/A: radiation {1/(3*np.sqrt(rad)):.2f}, matter {1/(3*np.sqrt(eds)):.2f}, today {1/(3*np.sqrt(VH4)):.2f}")
def hist(A, nh, seed, dx=0.02, x0=np.log(1e-20), x_on=None):
    rng = np.random.default_rng(seed); a0 = np.exp(x0); sr = np.sqrt(Orad)
    ch_ = np.full(nh, a0/sr); I = np.array([np.full(nh, sr**-(k+1)*a0**(k+5)/(k+5)) for k in range(4)])
    v = np.full(nh, (4*np.pi/3)/280*a0**8/Orad**2); on = x_on is None
    b = np.sqrt(v)*rng.standard_normal(nh) if on else np.zeros(nh); lam = (A/3)*b/v; alive = np.ones(nh, bool)
    xs = np.append(np.arange(x0 + dx/2, 0, dx), 0.0); ag = 1/(1 + np.linspace(0, 2, 11))
    ig = {int(np.argmin(abs(xs - np.log(a)))): k for k, a in enumerate(ag)}
    iB = int(np.argmin(abs(xs - np.log(2.5e-10)))); iR = int(np.argmin(abs(xs - np.log(1/1100.))))
    Lz = np.zeros((len(ag), nh)); oB = oR = np.zeros(nh)
    for i, xx in enumerate(xs):
        a = np.exp(xx); H2m = Orad*a**-4 + Om*a**-3; H2 = H2m + lam; alive &= H2 > 0
        dt = dx/np.sqrt(np.where(alive, H2, H2m)); ch_ += dt/a
        w = a**3*dt; I[0] += w; I[1] += w*ch_; I[2] += w*ch_**2; I[3] += w*ch_**3
        vn = np.maximum((4*np.pi/3)*(ch_**3*I[0] - 3*ch_**2*I[1] + 3*ch_*I[2] - I[3]), v)
        if not on and xx >= x_on: on = True; b = np.sqrt(vn)*rng.standard_normal(nh)
        elif on: b = b + np.sqrt(vn - v)*rng.standard_normal(nh)
        v = vn; lam = np.where(alive, (A/3)*b/v, 0.0)
        if i == iB: oB = lam/(H2m + lam)
        if i == iR: oR = lam/(H2m + lam)
        if i in ig: Lz[ig[i]] = lam
    return dict(oB=oB, oR=oR, L=Lz, alive=alive, ag=ag)
gauss_p = lambda c, h, s: (np.exp(-0.5*(c/s)**2)/(np.sqrt(2*np.pi)*s))*2*h   # P(|X - c| < h), X ~ N(0, s), narrow window
best = 0; rows = []
for A in (0.05, 0.1, 0.15, 0.2):
    r = hist(A, 12000, 20261022); al = r['alive']; L0 = r['L'][0]
    pB = (al & (abs(r['oB']) < 0.065)).mean(); pR = (al & (abs(r['oR']) < 0.03)).mean()
    s0_ = np.std(L0[al]) if al.sum() > 10 else 0.95*A; p0 = gauss_p(OL, 0.02, s0_)
    pall = (pB/max(al.mean(), 1e-9))*(pR/max(al.mean(), 1e-9))*al.mean()*p0 if al.mean() > 0 else 0.0
    best = max(best, pall); rows.append(f"A {A:.2f}: alive {al.mean():.3f}, P(BBN) {pB:.3f}, P(rec) {pR:.3f}, rms OL0 {s0_:.3f}, P(today) {p0:.0e}")
print("  " + "\n  ".join(rows))
check("histories from a = 1e-20 (crunch = H^2 <= 0): survival needs A <~ 0.15, where today's rms Omega_L <= 0.09, so Omega_L = 0.685 is a >= 7 sigma fluctuation; the best factorised joint probability (alive x BBN x recombination x today) is tiny",
      best < 1e-8, f"max over A of P(all) ~ {best:.0e} (bounds: |OL(BBN)| < 0.065, |OL(z=1100)| < 0.03, |OL0 - 0.685| < 0.02)")
cpl = lambda Lv, ag: np.linalg.lstsq(np.stack([-3*np.log(ag), -3*(np.log(ag) + 1 - ag)], 1), np.log(Lv/Lv[0]), rcond=None)[0]
r = hist(0.5, 40000, 9, x0=np.log(1e-8), x_on=np.log(0.25)); al = r['alive']; L0 = r['L'][0]
sel = al & (abs(L0 - OL) < 0.02) & (r['L'] > 0).all(0); ws = np.array([cpl(r['L'][:, j], r['ag']) for j in np.where(sel)[0]])
w0, wa = ws[:, 0] - 1, ws[:, 1]
desi = ((abs(w0 + 0.75) < 0.12) & (abs(wa + 0.86) < 0.5)).mean(); lcdm = ((abs(w0 + 1) < 0.1) & (abs(wa) < 0.3)).mean()
check("late-window diagnostic (switched on at z = 3, A = 0.5, early bounds ignored, conditioned on today's Omega_L): CPL fits to rho_L(z <= 2) scatter by O(1), almost none near DESI or LambdaCDM",
      len(w0) > 30 and desi < 0.1 and np.percentile(w0, 84) - np.percentile(w0, 16) > 0.5,
      f"n = {len(w0)}; w0 median {np.median(w0):+.2f} [{np.percentile(w0,16):+.2f}, {np.percentile(w0,84):+.2f}], wa {np.median(wa):+.2f} [{np.percentile(wa,16):+.2f}, {np.percentile(wa,84):+.2f}]; DESI box {desi:.3f}, LCDM box {lcdm:.3f}")

# ---------------- D. conflicts ----------------
print("== D. conflicts")
check("conflict ledger: (i) CL-3 vacuum standard holds Lambda a constant per proper 4-volume with w = -1 and the hinge bound |dw| < 6e-4; everpresent Lambda gives |w + 1| ~ O(1); (ii) the register's 'a size law must not drift with the horizon' fails by construction (C, tracking); (iii) under record-on-change voids carry no records, so V4 = count gives empty space no 4-volume; (iv) record-reading (every site every half-tick) gives Fano 0 (lambda-rule-2)",
      max(tvs) < 1e-12 and best < 1e-8, "no structural record rule tested here supplies volume-law Poisson counts in the frozen vacuum")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time()-T0:.1f} s)")
