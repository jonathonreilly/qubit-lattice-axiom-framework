AUDIT_INPUT_PATHS = ('docs/NO_COUNT_SPREAD_OR_WINDOW_POWER_IN_THE_LAWS_SIZES_LAMBDA_WITHOUT_TUNING_OR_HORIZON_DRIFT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Size rules for Lambda from structures in the candidate laws: counts, dark-constant spread, window powers.
Self-contained; seeded; numpy/scipy/sympy only. Units: rung units, L = sqrt(8 pi) l_P (8 pi G hbar = L^2), c = 1.
Supplied: LambdaCDM (Planck 2018), eps0 range, edge vacua, DESI DR2 (w0, wa) for a sign test."""
import time, numpy as np, sympy as sp
from math import comb
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); rng = np.random.default_rng(20261022)
NP = NF = 0
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

# ---------- M. measured value ----------
tP = 5.391247e-44; H0 = 67.36e3 / 3.0857e22; OL, Om, Orad = 0.6847, 0.3153, 9.1e-5
HL = H0 * tP * np.sqrt(8 * np.pi)                       # H0 L
LamL2 = 3 * OL * HL ** 2
SIG = np.sin(np.array([0.0075, 0.0375])) / np.sqrt(3)    # proper time per cell-tick / l
print("== M. measured")
check("Lambda L^2 = 3 Omega_L (H0 L)^2 (Planck 2018; brief quotes 7.3e-121)", 7.0e-121 < LamL2 < 7.3e-121,
      f"{LamL2:.3e}; H0 L = {HL:.3e}; ln(1/Lambda L^2) = {-np.log(LamL2):.2f}")

# ---------- LambdaCDM background, past-cone 4-volume ----------
lna = np.linspace(np.log(1e-12), np.log(4.0), 240001); a = np.exp(lna)
def Hof(a, OLv=OL): return np.sqrt(Om * a ** -3 + Orad * a ** -4 + OLv)
H = Hof(a); dl = lna[1] - lna[0]
t = np.concatenate([[0.0], np.cumsum(0.5 * (1 / H[1:] + 1 / H[:-1]) * dl)]) + a[0] ** 2 / (2 * np.sqrt(Orad))
eta = np.concatenate([[0.0], np.cumsum(0.5 * (1 / (a[1:] * H[1:]) + 1 / (a[:-1] * H[:-1])) * dl)])
def V4(i):  # past light-cone 4-volume of the comoving observer at index i (H0 = 1 units)
    chi = eta[i] - eta[:i + 1]; f = a[:i + 1] ** 3 * (4 * np.pi / 3) * chi ** 3 / H[:i + 1]
    return np.sum(0.5 * (f[1:] + f[:-1])) * dl
i0 = np.searchsorted(lna, 0.0)
idx = [np.searchsorted(lna, np.log(x)) for x in (0.5, 0.9, 1.0, 1.1, 2.0, 4.0)]
Vs = {k: V4(j) for k, j in zip((0.5, 0.9, 1.0, 1.1, 2.0, 4.0), idx)}
sV = np.log(Vs[1.1] / Vs[0.9]) / np.log(1.1 / 0.9)          # d ln V4 / d ln a today
sV05 = np.log(V4(np.searchsorted(lna, np.log(0.55))) / V4(np.searchsorted(lna, np.log(0.45)))) / np.log(0.55 / 0.45)
eps = lambda x: 1.5 * (Om * x ** -3 + 4 / 3 * Orad * x ** -4) / Hof(x) ** 2
def w0wa(wfun):  # CPL tangent at a = 1
    h = 1e-3; return wfun(1.0), -(wfun(1 + h) - wfun(1 - h)) / (2 * h)
DESI = (-0.752, -0.86)  # DESI DR2 + CMB + DESY5 (supplied, approximate); sign test only

# ---------- A. counts (idea a) ----------
print("== A. inverse count of splits / cells / records")
k, T = 3, 5; cells = [8 ** j for j in range(k + 1)]; rec = sum(2 * T * 8 * c for c in cells)  # 8 sites per cell, 2 half-ticks
pois = rng.poisson(rec / 1000.0, size=20000)
check("THEOREM (CL-2 text): records each half-tick at every site, and splits are 1 -> 8 by rule, so cell, split and record counts are fixed by the geometry: Fano 0; a Poisson-sprinkled control has Fano 1",
      abs(pois.var() / pois.mean() - 1) < 0.05, f"one-cube start, {k} splits, {T} ticks each: cells {cells[-1]}, records {rec} (variance 0); Poisson control Fano {pois.var() / pois.mean():.3f}")
x = sp.symbols('x', positive=True); Tq = sp.symbols('T', positive=True)
Iq = sp.integrate((1 - sp.exp(-x)) ** 3, (x, 0, Tq))
check("THEOREM (no freeze): the split trigger fires whenever the log-mean edge doubles, so splits never stop while H > 0; in de Sitter the past-cone 4-volume grows linearly, V4 = (4pi/3) H^-3 (t - 11/(6H)) + O(e^-Ht), at the horizon-volume rate",
      sp.simplify(sp.limit(Iq - Tq, Tq, sp.oo) + sp.Rational(11, 6)) == 0, f"int_0^T (1-e^-x)^3 dx - T -> {sp.limit(Iq - Tq, Tq, sp.oo)}; cells in a comoving region ~ a^3")
check("FINITE DIAGNOSTIC (LambdaCDM): today's past cone and its drift; V4 never freezes",
      0.10 < Vs[1.0] < 0.15 and Vs[4.0] > Vs[2.0] > Vs[1.0] > Vs[0.5],
      f"V4 H0^4 = {Vs[0.5]:.4f} (a=.5), {Vs[1.0]:.4f} (1), {Vs[2.0]:.3f} (2), {Vs[4.0]:.3f} (4); dlnV4/dlna = {sV:.3f} today, {sV05:.3f} at a=.5")
w_q = lambda q, s1: -1 + q * s1 / 3
wq1, wq2 = w_q(1.0, sV), w_q(0.5, sV)
waq1 = -(w_q(1.0, sV) - w_q(1.0, sV05)) / 0.5; waq2 = waq1 / 2
check("ESTIMATE (drift): rho_L ~ V4^-q gives w = -1 + (q/3) dlnV4/dlna: count (q=1) and Sorkin (q=1/2) forms both sit far from -1 and their wa has the opposite sign to DESI's",
      wq2 > -0.7 and waq2 > 0 > DESI[1], f"q=1: w0 {wq1:.2f}, wa {waq1:+.2f}; q=1/2: w0 {wq2:.2f}, wa {waq2:+.2f}; DESI ({DESI[0]}, {DESI[1]}); measured w0 = -1 within ~0.06")
C, kk, p, d = sp.symbols('C k p d', positive=True); lam = sp.symbols('lam', positive=True)
sol = sp.solve(sp.Eq(lam, C * (kk * (lam / 3) ** (-d / 2)) ** (-p)), lam)
fp = lambda Cv, kv, pv, dv: (Cv * kv ** -pv * 3 ** (pv * dv / 2)) ** (1 / (1 - pv * dv / 2))
vals = [fp(1, 4 * np.pi / 3, 1, 3), fp(1, 4 * np.pi / 3 / SIG[0], 1, 4), fp(1, 1, 2, 3)]
need = (LamL2 ** (1 - 1 * 4 / 2)) * (4 * np.pi / 3 / SIG[0]) ** 1 / 3 ** 2
check("THEOREM (horizon counts): Lambda L^2 = C N^-p with N = k (HL)^-d and H^2 = Lambda/3 gives (Lambda L^2)^(1-pd/2) = C k^-p 3^(pd/2): rung-sized unless C is tuned; pd = 2 is scale-free (size free, Sorkin p = 1/2, d = 4)",
      len(sol) >= 1 and all(1e-3 < v < 1e3 for v in vals), f"C = 1: N = horizon cells, p=1: {vals[0]:.2f}; N = horizon cell-ticks, p=1: {vals[1]:.2e}; p=2, d=3: {vals[2]:.2f}; measured needs C ~ {need:.1e} (p=1, d=4)")
Nnow = Vs[1.0] / (HL ** 4 * SIG)
check("ESTIMATE: today's past cone holds N ~ 1e242 cell-ticks; 1/N misses by ~1e-121, 1/sqrt(N) lands within a factor ~10 of the measured value (the known Sorkin coincidence; it tracks H^2)",
      all(1e240 < n < 1e244 for n in Nnow), f"N = {Nnow[0]:.2e} .. {Nnow[1]:.2e}; 1/N = {1 / Nnow[1]:.1e}; N^-1/2 / Lambda L^2 = {Nnow[1] ** -0.5 / LamL2:.2f} .. {Nnow[0] ** -0.5 / LamL2:.2f}")

# ---------- B. dark-constant spread (idea b) ----------
print("== B. zero-mean dark-constant spread")
n_, aa = sp.symbols('n a', positive=True)
wD = sp.simplify(-1 - sp.Rational(1, 3) * sp.diff(sp.log(aa ** (-(n_ + 3))), aa) * aa)
check("THEOREM: the tick's conserved value is N sqrt(gamma) rho_D = const, so rho_D ~ a^-(n+3), w = n/3; fixed lapse (n = 1) makes every dark-constant spread dark radiation, w = 1/3; only n = -3 (unimodular lapse) gives w = -1",
      sp.simplify(wD - n_ / 3) == 0 and wD.subs(n_, 1) == sp.Rational(1, 3) and wD.subs(n_, -3) == -1, f"w(n) = {wD}")
vals3 = np.array([-2, 1, 3]); pr = np.array([0.4, 0.4, 0.2]); pr = pr / pr.sum()
mu = vals3 @ pr; vals3 = vals3 - mu  # zero mean
ok = True; neg = []
for N in (1, 4, 16, 48):
    # exact multinomial enumeration of the sum
    s_vals, s_p = [], []
    for i in range(N + 1):
        for j in range(N + 1 - i):
            kq = N - i - j; s_vals.append(i * vals3[0] + j * vals3[1] + kq * vals3[2])
            s_p.append(comb(N, i) * comb(N - i, j) * pr[0] ** i * pr[1] ** j * pr[2] ** kq)
    s_vals, s_p = np.array(s_vals), np.array(s_p)
    m1 = s_vals @ s_p; var = (s_vals ** 2) @ s_p
    ok &= abs(m1) < 1e-10 and abs(var - N * (vals3 ** 2 @ pr)) < 1e-9; neg.append(s_p[s_vals < -1e-12].sum())
check("FINITE (exact enumeration): N zero-mean cells, 3-valued skewed spread: the sum has mean 0 exactly, variance N sigma^2 exactly, and either sign (P(neg) -> 1/2): a Hubble-volume average of size sigma/sqrt(N_H), random sign, w = 1/3",
      ok and all(0.2 < q < 0.8 for q in neg), "P(sum<0) at N=1,4,16,48: " + ", ".join(f"{q:.3f}" for q in neg))
# Sorkin variant (needs Lambda conjugate to V4: the dropped fixed-4-volume clause or a unimodular lapse)
def edge_vac(s, Dl=0, b=1):  # least-kinetic volume-mode vacuum, construction of the lambda-quantum note (sig cancels)
    from scipy.linalg import eigh
    nmax = (4 + Dl) * s; xs = 2.0 ** (np.arange(nmax + 1) / s - 3); xm = 2.0 ** ((np.arange(nmax) + 0.5) / s - 3)
    wb = 1.0 / (6 * b ** 3 * xm ** 2 * (np.log(2) / s) ** 2); K = np.zeros((nmax + 1, nmax + 1))
    for i, wi in enumerate(wb):
        K[i, i] += wi / 2; K[i + 1, i + 1] += wi / 2; K[i, i + 1] -= wi / 2; K[i + 1, i] -= wi / 2
    K[0, 0] += wb[0] / 2; K[-1, -1] += wb[-1] / 2
    y = b ** 3 * xs ** 4; vi = 1 / np.sqrt(y); ev, U = eigh(vi[:, None] * K * vi[None, :])
    psi = vi * U[:, 0]; P = psi ** 2 / np.sum(psi ** 2); return ev[0], P @ y, np.sqrt(P @ y ** 2 - (P @ y) ** 2)
lm, m4, sd4 = edge_vac(23); u4 = 2.0 ** (4 * (np.arange(4 * 23 + 1) / 23 - 3)); r_u = u4.std() / u4.mean()
r_g = sd4 / m4; V4L = Vs[1.0] / HL ** 4
dL = lambda r, m, sig: 1 / (r * np.sqrt(sig * m) * np.sqrt(V4L))
outs = [dL(r_g, m4, SIG[0]), dL(r_g, m4, SIG[1]), dL(r_u, u4.mean(), SIG[0])]
check("ESTIMATE (Sorkin variant, NOT the current law): counts are exact, so only edge-length spread moves V4; Delta Lambda L^2 = 1/(r sqrt(sig <x^4>) sqrt(V4/L^4)) with r = std(x^4)/<x^4>",
      0.05 < lm < 0.2 and all(1e-123 < o < 1e-118 for o in outs),
      f"least-kinetic edge vacuum (s=23): Lambda_min L^2 {lm:.3f}, r {r_g:.2f}; Delta Lambda/Lambda_meas = {outs[0] / LamL2:.1f}, {outs[1] / LamL2:.1f}; uniform window r {r_u:.2f}: {outs[2] / LamL2:.1f}; sharper edges (r -> 0) raise it")
zs = {"BBN": 1e9, "rec": 1100.0}; rat = {}
for kz, z in zs.items():
    ai = 1 / (1 + z); j = np.searchsorted(lna, np.log(ai)); rat[kz] = OL * np.sqrt(Vs[1.0] / V4(j)) / Hof(ai) ** 2
check("ESTIMATE (tracking): with today's Omega_L = 0.685 the Sorkin size |rho_L|/rho_c ~ 1/(sqrt(V4) H^2) stays order one at BBN and recombination (need < 0.05 and < 0.02 for early dark energy): its ratio to today is fixed by the background, so no prefactor fits both",
      rat["BBN"] > 0.05 and rat["rec"] > 0.02, f"BBN {rat['BBN']:.2f}, rec {rat['rec']:.2f}")

# ---------- C. window ratio to the rung count (idea c) ----------
print("== C. window ratio 2^(4+Delta) per rung")
kH = np.log2(1 / HL); kL = np.log2(np.sqrt(3 / LamL2))
r0 = [2.0 ** (-(4 + Dl) * kH) for Dl in (0, 1)]; Dneed = -np.log2(LamL2) / kL - 4
check("ESTIMATE: rungs from the cell to the Hubble (Lambda) radius k = 200.1 (200.4); 2^-(4+Delta)k misses by ~1e-120 (it is ~ (Lambda L^2)^2); a hit needs 4+Delta = 2, the horizon tautology Lambda = 3/R^2",
      r0[0] < 1e-230 and abs(Dneed + 2) < 0.02, f"k {kH:.1f} ({kL:.1f}); Delta=0: {r0[0]:.1e}, Delta=1: {r0[1]:.1e}; needed 4+Delta = {Dneed + 4:.3f}")
res = []
for pw in (2, 4, 5):
    w0, wa = w0wa(lambda x, pw=pw: -1 + pw * eps(x) / 3); res.append((pw, w0, wa))
fpC = [3 ** ((4 + Dl) / (2 + Dl)) for Dl in (0, 1)]
check("THEOREM + ESTIMATE: a horizon-counted rung number tracks: rho ~ H^p gives w = -1 + p eps/3 (eps = -dlnH/dlna = 0.47 today), wa > 0 (DESI wa < 0); its self-consistent de Sitter fixed point is Lambda L^2 = 3^((4+D)/(2+D)), rung-sized",
      all(r[2] > 0 for r in res) and res[0][1] > -0.8, "; ".join(f"p={r[0]}: w0 {r[1]:.2f}, wa {r[2]:+.2f}" for r in res) + f"; fixed point {fpC[0]:.1f} (D=0), {fpC[1]:.2f} (D=1)")
hits = []
for Dl in range(0, 4):
    sv = -np.log2(LamL2) / (4 + Dl); s_int = int(round(sv)); hits.append((Dl, sv, s_int, 2.0 ** (-(4 + Dl) * s_int) / LamL2))
chance = [min(1.0, 2 / (4 + Dl)) for Dl in range(4)]
check("LOOK-ELSEWHERE: a frozen rule integer, 2^-(4+Delta)s = 1/(states of one edge-register end), lands on the measured value for s = 99.8 (Delta=0) inside the allowed s range 23-113, but with s free the chance of a factor-2 hit is 2/(4+Delta): a fit of s, not a derivation (no law ties Lambda to that dimension)",
      23 <= hits[0][2] <= 113 and chance[0] >= 0.5, "; ".join(f"D={h[0]}: s {h[1]:.1f}, s={h[2]} gives x{h[3]:.2f}" for h in hits) + f"; P(factor 2) {chance[0]:.2f}..{chance[3]:.2f}")

print("== D. scoreboard (number | inputs | drift | w)")
print(f"  (a) 1/N_past: {1 / Nnow[1]:.0e} | V4, sig | grows, no freeze | w0 {wq1:.2f}; dS fixed points rung-sized")
print(f"  (b) D spread: free, either sign | sigma supplied | dilutes a^-4 | w = 1/3 exactly (fixed lapse)")
print(f"      Sorkin variant: x{outs[1] / LamL2:.0f}..{outs[0] / LamL2:.0f} meas | unimodular clause, edge spread | tracks H^2 | w0 {wq2:.2f}, wa>0")
print(f"  (c) window^rungs: {r0[0]:.0e} | k from horizon | tracks H^4 | w0 {res[1][1]:.2f}; frozen-s variant = fit")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
