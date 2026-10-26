AUDIT_INPUT_PATHS = ('docs/D4_ROUTE_PREDICTIONS_UNDER_FINITE_RUNG_ZOOM_MATTER_LIV_FALLS_SIXTEENFOLD_PER_RUNG_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""D4 route predictions recomputed under the rules as proposed: finite-rung zoom fermion (rules 2-3), Borici slab (rule 5),
NN triangle links (rule 7, not zoomed), metric-only hinge-sum graviton (rules 8-9). Root slicing, E* = hbar c / a, a = 2L.
Self-contained (numpy, scipy, sympy). Seeded. Units: D4 coordinates (roots length sqrt2); site spacing a = 1/sqrt2."""
import itertools, time
import numpy as np, sympy as sp
from scipy.optimize import brentq
AUDIT_TIMEOUT_SEC = 120
t0 = time.time(); rng = np.random.default_rng(20261026)
NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
R = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2], float)
rt = np.array([1., 1, 0, 0]); ut = rt / np.sqrt(2)
PR = np.array([[1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]], float).T / np.sqrt(2)   # slice cube axes
DIRS = {'axis': [1, 0, 0], 'face': [1, 1, 0], 'body': [1, 1, 1]}
unit = lambda v: np.array(v, float) / np.linalg.norm(v)
# ---------------- C1 exact species constants: on shell p^2 = kappa J6 + O(p^8)
p = sp.symbols('p0:4'); P2 = sum(x**2 for x in p)
J6 = sum(x**6 for x in p) + 15 * sum(p[i]**2 * p[j]**2 * p[k]**2 for i, j, k in itertools.combinations(range(4), 3))
rp = [sum(int(r[i]) * p[i] for i in range(4)) for r in R]
Kser = sp.expand(sum(x**2 / 2 - x**4 / 24 + x**6 / 720 for x in rp))
sser = [sp.expand(sum(int(r[m]) * (x - x**3 / 6 + x**5 / 120) for r, x in zip(R, rp))) for m in range(4)]
s2 = sp.expand(sum(c**2 for c in sser))
deg = lambda e, d: sp.Add(*[t for t in sp.Add.make_args(e) if sp.Poly(t, *p).total_degree() == d])
divP2 = lambda e: sp.div(sp.Poly(e, p[0]), sp.Poly(P2, p[0]))[1].is_zero
ks_, kf_ = sp.Rational(1, 540), sp.Rational(1, 90)
okS = sp.expand(deg(Kser, 2) - 6 * P2) == 0 and divP2(deg(Kser, 4)) and divP2(sp.expand(deg(Kser, 6) + 6 * ks_ * J6))
okF = sp.expand(deg(s2, 2) - 144 * P2) == 0 and divP2(deg(s2, 4)) and divP2(sp.expand(deg(s2, 6) + 144 * kf_ * J6))
# photon (triangle plaquettes, axis slicing, numerical): beta = -kappa J6(i, n)/2
Rp = np.array([r for r in R if tuple(r) > tuple(-r)]); idx = {tuple(r): i for i, r in enumerate(Rp)}; tri = []
for r1 in R:
    for r2 in R:
        if r1 @ r2 == -1:
            y = np.zeros(4); L = []
            for r in (r1, r2, -(r1 + r2)):
                t = tuple(r); i, sg = (idx[t], 1.) if t in idx else (idx[tuple(-r)], -1.); L.append((i, sg, y + r / 2)); y = y + r
            tri.append(L)
TI = np.array([[l[0] for l in T] for T in tri]); TS = np.array([[l[1] for l in T] for T in tri]); TM = np.array([[l[2] for l in T] for T in tri])
def Kph(q):
    C = np.zeros((len(tri), 12), complex); Cm = np.zeros_like(C); ar = np.arange(len(tri))
    for j in range(3):
        np.add.at(C, (ar, TI[:, j]), TS[:, j] * np.exp(1j * TM[:, j] @ q)); np.add.at(Cm, (ar, TI[:, j]), TS[:, j] * np.exp(-1j * TM[:, j] @ q))
    return Cm.T @ C
def Emb(q):
    x = Rp @ q; return Rp * np.where(abs(x) < 1e-12, 1., np.sin(x / 2) / np.where(abs(x) < 1e-12, 1, x / 2))[:, None]
Qh, _ = np.linalg.qr(np.hstack([Rp, rng.normal(size=(12, 8))])); H0 = Qh[:, 4:]
def Meff(q):
    K = Kph(q); Ep, Em = Emb(q), Emb(-q)
    return Em.T @ K @ Ep - Em.T @ K @ H0 @ np.linalg.solve(H0.T @ K @ H0, H0.T @ K @ Ep)
def Eph(k):
    return brentq(lambda E: np.sort(np.real(np.linalg.eigvals(Meff(np.array([1j * E, *k]))[1:, 1:])))[1], .97 * np.linalg.norm(k), 1.03 * np.linalg.norm(k), xtol=1e-15)
J6v = lambda v: float(np.real(sum(x**6 for x in v) + 15 * sum(v[i]**2 * v[j]**2 * v[k]**2 for i, j, k in itertools.combinations(range(4), 3))))
ks = np.array([0.05, 0.1, 0.2]); nb = unit([1, 1, 1])
bph = np.linalg.lstsq(np.vstack([ks**2, ks**4, ks**6]).T, np.array([Eph(k * nb) / k - 1 for k in ks]), rcond=None)[0][1]
kg_ = -2 * bph / J6v(np.array([1j, *nb]))
check("C1 [T] on shell p^2 = kappa J6 (no dim 6): kappa_scalar = 1/540, kappa_fermion = 1/90 exact; photon (triangles) 1/1440",
      okS and okF and abs(kg_ * 1440 - 1) < 1e-3, f"sympy ideal test mod p^2 exact; photon kappa*1440 = {kg_ * 1440:.5f}")
# root slicing: beta(n) in (ka)^4 = -2 kappa J6(i t + n)
J6r = {d: J6v(1j * ut + PR @ unit(n)) for d, n in DIRS.items()}
beta = lambda kap, d: -2 * kap * J6r[d]
def Esc(k):
    kv = PR @ k; return brentq(lambda E: np.sum(1 - np.cos(R @ kv) * np.cosh((R @ rt) * E)), 1e-14, 3 * np.linalg.norm(k) / np.sqrt(2)) * np.sqrt(2)
bsc = {d: 4 * np.linalg.lstsq(np.vstack([ks**2, ks**4, ks**6]).T, np.array([Esc(k * unit(n)) / k - 1 for k in ks]), rcond=None)[0][1] for d, n in DIRS.items()}
check("C1b root-slicing scalar: direct band solve = -2 kappa J6(i t + n) (face, body); slice cube axes 0",
      all(abs(bsc[d] / beta(1 / 540, d) - 1) < 1e-3 for d in ('face', 'body')) and abs(J6r['axis']) < 1e-12,
      " ".join(f"{d} {bsc[d]:+.4e}/{beta(1 / 540, d) if d != 'axis' else 0:+.4e}" for d in DIRS))
bE0 = {d: beta(1 / 90, d) for d in DIRS}; bG = {d: beta(1 / 1440, d) for d in DIRS}
# ---------------- C2 zoom rungs from the NN start: E_n(k) = 2^n E_0(k / 2^n)
def fq(c):
    s = c.sum(-1); return (s * s - 0.5 * (c * c).sum(-1) + 2 * c.prod(-1)) / 16
a2 = np.array(list(itertools.product(range(2), repeat=4)), float); reps = []
for c in np.vstack([a2, a2 + .5]):
    if not any((lambda d: np.allclose(d, np.round(d)) or np.allclose(d - np.floor(d), .5))((c - r) / 2) for r in reps): reps.append(c)
reps = np.array(reps) * 2 * np.pi
def G_nn(q):
    A = 2 - np.cos(q @ R.T).sum(-1) / 12; B = np.sin(q @ R.T) @ R / 12; d = A * A + np.sum(B * B, -1); return A / d, B / d[..., None]
def G_rung(q, n, al=0.5):
    if n == 0: return G_nn(q)
    s = np.zeros(q.shape[:-1]); r = np.zeros(q.shape); sf = np.zeros(q.shape[:-1])
    for lk in reps:
        Q = (q + lk) / 2; f2 = fq(np.cos(Q)) ** 2; sq, rq = G_rung(Q, n - 1, al); s += 0.5 * f2 * sq; r += 0.5 * f2[..., None] * rq; sf += 0.5 * f2
    return s + al * (1 - sf), r
Nth = 256; th = 4 * np.pi * np.arange(Nth) / Nth; PH = np.exp(1j * np.outer(np.arange(Nth), th) / 2) / Nth
def E_slice(vec_of_p, m):
    c = PH @ vec_of_p; return np.sqrt(2) * np.log(abs(c[m] / c[m + 1]))
def E_newton(k):
    def F(E):
        q = 1j * E * ut + k; A = 2 - np.cos(R @ q).sum() / 12; B = np.sin(R @ q) @ R / 12; return A * A + B @ B
    E = np.linalg.norm(k) + 0j
    for _ in range(40): E = E - F(E) / ((F(E + 1e-7) - F(E - 1e-7)) / 2e-7)
    return E.real
idm = 0; fitr = {}
kfit = np.array([0.3, 0.4, 0.5])
for n in (0, 1, 2, 3):
    Es = []
    for kk in kfit:
        k = PR @ (kk * nb); _, r = G_rung(th[:, None] * rt[None] / 2 + k[None], n); E = E_slice(r @ ut, 28)
        Es.append(E); idm = max(idm, abs(E / (2**n * E_newton(k / 2**n)) - 1))
    fitr[n] = 4 * np.polyfit(kfit**4, np.array(Es) / kfit - 1, 1)[0]
b0n = 4 * np.linalg.lstsq(np.vstack([ks**2, ks**4, ks**6]).T, np.array([E_newton(PR @ (k * nb)) / k - 1 for k in ks]), rcond=None)[0][1]
check("C2 [T+F] rung n light band E_n(k) = 2^n E_0(k/2^n) (blocking keeps poles): beta_n = beta_0/16^n; beta_0 = -J6/45 = 6x scalar",
      idm < 1e-9 and abs(b0n / bE0['body'] - 1) < 1e-3 and all(abs(fitr[n] / fitr[0] * 16**n - 1) < 1e-2 for n in (1, 2)),
      f"identity rel {idm:.0e} (n<=3, body); NN beta_0 body {b0n:+.4e} vs {bE0['body']:+.4e}; slice-fit ratio*16^n n=1,2,3: "
      + " ".join(f"{fitr[n] / fitr[0] * 16**n:.3f}" for n in (1, 2, 3)) + " (k^8 terms at k a<=.35)")
# ---------------- C3 exact fixed point and C4 Borici residual mass
JL = 8
def Pi(q):
    out = np.ones(q.shape[:-1])
    for j in range(1, JL + 1): out = out * fq(np.cos(q / 2.0 ** j))
    q2 = np.sum(q * q, -1); return out * np.exp(-(9 / 32) * q2 / (3 * 4.0 ** JL) - (17 / 2048) * q2 ** 2 / (15 * 16.0 ** JL))
def chi(x, N):
    u = np.clip((x - (N - 2)) / 2.0, 0, 1); g = lambda t: np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.)
    return g(1 - u) / (g(1 - u) + g(u))
aa = np.array(list(itertools.product(range(-6, 7), repeat=4)), float); IM = np.vstack([aa, aa + 0.5]) * 2 * np.pi
IM = IM[np.linalg.norm(IM, axis=1) <= 12 * np.pi]
def fold(q):
    x = q / (2 * np.pi); a = np.round(x); b = np.floor(x) + 0.5
    return q - 2 * np.pi * np.where((np.sum((x - a) ** 2, -1) <= np.sum((x - b) ** 2, -1))[:, None], a, b)
def Gstar(q, al=0.5):
    q = fold(q); rho = np.zeros((len(q), 4)); st = max(1, 200000 // len(IM))
    for i in range(0, len(q), st):
        Q = q[i:i + st, None, :] + IM[None]; Q2 = np.sum(Q * Q, -1)
        w = Pi(Q) ** 2 / Q2 * chi(np.sqrt(Q2) / (2 * np.pi), 5); rho[i:i + st] = np.einsum('pl,plm->pm', w, Q)
    return al + 0 * rho[:, 0], rho
dfp, bfp, slab = 0, 0, {}
for d in ('face', 'body', 'axis'):
    for kk in (0.25, 0.5):
        k = PR @ (kk * unit(DIRS[d])); s, r = Gstar(th[:, None] * rt[None] / 2 + k[None])
        if d != 'axis': dv = abs(E_slice(r @ ut, 12) / kk - 1); dfp = max(dfp, dv); bfp = max(bfp, dv / (kk / np.sqrt(2))**4)
        for mu in (0.2, 0.1):   # (D* + mu)^-1 = G (1 + mu G)^-1, vector part r / ((1 + mu s)^2 + mu^2 r^2)
            E = E_slice((r @ ut) / ((1 + mu * s) ** 2 + mu * mu * np.sum(r * r, -1)), 12); slab[(d, kk, mu)] = E * E - kk * kk
check("C3 [F] exact fixed point (#10098 image tower): lowest band = |k| on face/body rays; dim 8 bounded far below beta_3",
      dfp < 1e-7 and bfp < 1e-2 * abs(bE0['body']) / 16**3, f"max |E/k - 1| {dfp:.1e}; |beta_inf| < {bfp:.0e} vs |beta_3| {abs(bE0['body']) / 4096:.1e}")
an = {mu: max(slab[(d, .5, mu)] for d in ('axis', 'face', 'body')) - min(slab[(d, .5, mu)] for d in ('axis', 'face', 'body')) for mu in (0.2, 0.1)}
check("C4 [F] Borici slab (D_eff = D* + mu): E^2 - k^2 constant over k and rays to 1e-6; its anisotropy scales as mu^2",
      max(abs(v - slab[('body', .25, .2)]) for kk_, v in slab.items() if kk_[2] == .2) < 1e-6 and 3.5 < an[.2] / an[.1] < 4.5,
      f"m_eff^2 {slab[('body', .25, .2)]:.6f} (mu = 0.2); anisotropy at k = .5: {an[.2]:.1e} (mu .2), {an[.1]:.1e} (mu .1), ratio {an[.2] / an[.1]:.2f}")
# ---------------- C5 thresholds (E* = hbar c / 2L)
hbarc, lP = 1.97327e-16, 1.616255e-35; Lc = np.sqrt(8 * np.pi) * lP; Es = hbarc / (2 * Lc)   # GeV
me, mp = 0.51100e-3, 0.93827
xs = np.linspace(1e-4, 1 - 1e-4, 200001)
def th_gee(be, bg):
    G = np.max(xs * (1 - xs) * (be * (xs**5 + (1 - xs)**5) - bg)); return (me**2 * Es**4 / (2 * G))**(1 / 6) * 1e9 if G > 0 else None
def th_cher(be, bg):
    h = np.max((1 - xs) / xs * (bg * xs**5 - be * (1 - (1 - xs)**5))); return (me**2 * Es**4 / (2 * h))**(1 / 6) * 1e9 if h > 0 else None
wall = lambda b: (mp**2 * Es**4 / (20 * b))**(1 / 6) * 1e9
EQG = lambda b: Es / (2 * b)**0.25 if b > 0 else np.inf
f = lambda x: '-' if x is None else ('inf' if x == np.inf else f"{x:.2e}")
print(f"  E* = {Es:.4e} GeV (L = {Lc:.3e} m). |beta| in (ka)^4, body ray (max): photon {abs(bG['body']):.3e}, NN fermion {abs(bE0['body']):.3e}")
print("  rung | |b_e| | b_e/b_g | gamma->ee eV | e->e gamma eV | A-wall eV/A flow (frozen) | E_QG,4 e GeV")
rows = {}
for n in (0, 1, 2, 3, 'inf'):
    be = abs(bE0['body']) / 16**n if n != 'inf' else 0.0; bg = abs(bG['body'])
    rows[n] = (th_gee(be, bg), th_cher(be, bg), wall(max(be, bg)), wall(be) if be > 0 else np.inf)
    print(f"  {n!s:>4} | {be:.2e} | {be / bg:7.4f} | {f(rows[n][0]):>9} | {f(rows[n][1]):>9} | {rows[n][2]:.2e} ({f(rows[n][3])}) | {f(EQG(be))}")
check("C5 n = 0 reproduces #10094 (gamma -> ee 1.9e20 eV body; wall 9.9e20 A eV with the face coefficient); n = 1: b_e = b_g, both closed",
      abs(rows[0][0] / 1.9e20 - 1) < 0.05 and abs(wall(abs(bE0['face'])) / 9.9e20 - 1) < 0.05 and rows[1][0] is None and rows[1][1] is None,
      f"gamma->ee {rows[0][0]:.3e}; wall(face) {wall(abs(bE0['face'])):.3e}, wall(body) {rows[0][2]:.3e}")
check("C5b n >= 2 (and the exact fixed point): electron faster than the (unzoomed) photon -> e -> e gamma opens above 1e20 eV; gamma -> ee closed",
      all(rows[n][0] is None and rows[n][1] is not None and rows[n][1] > 1e20 for n in (2, 3, 'inf')),
      f"e -> e gamma: n=2 {rows[2][1]:.2e}, n=3 {rows[3][1]:.2e}, inf {rows['inf'][1]:.2e} eV (body); E_QG,4 photon {EQG(abs(bG['body'])):.2e} GeV")
# ---------------- C6 graviton dim-6 birefringence (d4-gravity A law, a = site spacing)
Egw = 4.135668e-15 * 100 / 1e9   # GeV, h f at 100 Hz
dc = (1 / 3) * (Egw / Es)**2; slip_hw = (Egw * 1e9 / Es)**2; slip_hf = (Egw * 1e9 / (2 * np.pi) / Es)**2
check("C6 graviton splitting at 100 Hz = 2A (E/E*)^2, 2A <= 1/3 (axis), 1/4 (face), 0 (body); 1e-62 only via an eV/GeV slip",
      1e-80 < dc < 1e-79 and 1e-63 < slip_hf < slip_hw < 1e-60, f"|dc| = {dc:.2e} (a = 2L); with a = L: {dc / 4:.1e} (#10100); slip (E in eV / E* in GeV)^2 = {slip_hf:.0e}..{slip_hw:.0e}")
# ---------------- C7 cubic (retired) photon decay, exact two-body kinematics with the photon term
def cubic(S):
    bq, bg = S / 6 - 1 / 24, S / 24; G = np.max(xs * (1 - xs) * (bq * (1 - 3 * xs * (1 - xs)) - bg))
    return (me**2 * Es**2 / (2 * G))**0.25 * 1e9 if G > 1e-15 else None
cf = lambda S: (144 * (4 * S - 1) / (3 * S - 1)**2)**0.25 * np.sqrt(me * Es) * 1e9
cx, cfc, cs, cb = cubic(1.0), cubic(0.5), cubic(0.6), cubic(1 / 3)
check("C7 cubic gamma -> e+e-: k_th(S) = (144 (4S-1)/(3S-1)^2)^(1/4) sqrt(m_e E*), S = sum n^4: axis 80, face 122 PeV, body closed",
      abs(cx / 8.0e16 - 1) < .02 and abs(cfc / 1.22e17 - 1) < .02 and cb is None and abs(cx / cf(1.0) - 1) < 1e-3,
      f"axis {cx:.3e}, face {cfc:.3e}, sky-average ray (S = 3/5) {cs:.3e} eV; 160 PeV needs S = 0.41; body closed")
# ---------------- C8 nucleon lifetimes (proton-theta formula)
hb, yr, mN = 6.582e-25, 3.156e7, 0.9389
chan = [('e+pi0', 0.135, 2.4e34, (0.131, 0.134)), ('nubarK+', 0.4937, 5.9e33, (0.041, 0.139)), ('pi+nubar', 0.1396, 3.9e32, (0.186, 0.189)), ('n:pi0nubar', 0.135, 1.1e33, (0.131, 0.134))]
tau = lambda Lam, W, A, mM: hb / (mN / (32 * np.pi) * (1 - mM**2 / mN**2)**2 * (A * W / Lam**2)**2) / yr
inv_a = 1.2209e19 / np.sqrt(8 * np.pi); Ls_c = np.sqrt(inv_a**3 / 2.11e18)
maps = {'cubic': (Ls_c, Ls_c / np.sqrt(8)), 'D4': (Es, Es / np.sqrt(8))}
T = {mp_: [(tau(L1, np.mean(W), 1.5, mM), tau(L2, max(W), 3.0, mM), b) for _, mM, b, W in chan] for mp_, (L1, L2) in maps.items()}
for mp_ in T: print(f"  tau {mp_} (Lam {maps[mp_][0]:.2e}..{maps[mp_][1]:.2e} GeV) central/worst yr: " + " ".join(f"{c[0]}={t[0]:.1e}/{t[1]:.1e}" for c, t in zip(chan, T[mp_])))
check("C8 nucleon lifetime: 5.3e42 yr = cubic WORST case (pi+ nubar, cell, A = 3, max W); 1e46 = cubic CENTRAL nubar K+ only",
      abs(min(t[1] for t in T['cubic']) / 5.3e42 - 1) < .05 and abs(T['cubic'][1][0] / 1.1e46 - 1) < .05 and min(t[1] / t[2] for t in T['D4']) > 1e7,
      f"D4 map: shortest central {min(t[0] for t in T['D4']):.1e} yr, worst {min(t[1] for t in T['D4']):.1e} yr; min margin vs bounds {min(t[1] / t[2] for t in T['D4']):.0e}")
# ---------------- C9 slab depth needed for the residual mass (Borici, r = 1/3 per layer, alpha = 1/2)
mres = lambda Ls: (lambda mu: mu / (1 + mu / 2))(2 * 3.0**-Ls / (1 - 3.0**-Ls)) * Es / np.sqrt(2)
Lse = next(L for L in range(2, 200) if mres(L) < me); Lsn = next(L for L in range(2, 200) if mres(L) < 0.45e-9)
check("C9 [E] Ls is not spectrum-inert: m_res(Ls = 8) is cell-scale; m_res < m_e needs Ls >= 46, < 0.45 eV (KATRIN) needs Ls >= 58",
      mres(8) > 1e13 and Lse == 46 and Lsn == 58, f"m_res(8) = {mres(8):.1e} GeV; Ls_min(e) {Lse}, Ls_min(nu) {Lsn}")
print(f"runtime {time.time() - t0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
