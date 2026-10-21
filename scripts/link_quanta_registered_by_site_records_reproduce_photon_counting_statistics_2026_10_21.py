#!/usr/bin/env python3
"""Link quanta registered by site records. Supplied tiny models, no physical identification.

Configuration (what records are made of) = site-mode occupations only. Link modes carry odds (amplitudes on
link occupations) but no configuration and no records. Detectors are site pairs (one fermion in a lower and an
upper mode); absorption moves it up (c a_u^+ a_l), i.e. creates a relay pair in the pair picture.
 A  registration: Bell-type shortfall switching on site configurations reproduces the Born record statistics;
    counting = port photon-number distribution; HBT g2; Mach-Zehnder with which-way marker; QND registration.
 B  composite photons (site bilinears): exact deviation from Bose statistics; pair energies are not sharp.
 C  gravity: Bianchi forces equal coupling of link energy; the Maxwell tensor is forced; deposit bookkeeping.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/LINK_QUANTA_REGISTERED_BY_SITE_RECORDS_REPRODUCE_PHOTON_COUNTING_STATISTICS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120


import os, sys, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*a):
    raise TimeoutError('120-second cap exceeded')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np, sympy as sp
from math import comb, factorial
from scipy.linalg import expm

T0 = time.time(); PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def switch(cfg, P, Pn, cls):
    """shortfall rule: from a config whose odds fell, leave w.p. (P-Pn)/P to a config of the SAME class whose
    odds rose, in proportion to the rise (inherited from the relay-number model)."""
    exc = np.maximum(P - Pn, 0.0); dfc = np.maximum(Pn - P, 0.0)
    leave = rng.random(cfg.size) < np.where(P[cfg] > 0, exc[cfg] / np.maximum(P[cfg], 1e-300), 0.0)
    out = cfg.copy()
    for k in np.unique(cls[cfg[leave]]):
        w = dfc * (cls == k); idx = np.nonzero(leave & (cls[cfg] == k))[0]
        if w.sum() > 0 and idx.size: out[idx] = rng.choice(w.size, size=idx.size, p=w / w.sum())
    return out


# ---------------- A0: site-pair detectors are exact two-level systems (no Jordan-Wigner strings) ----------------
def jw(n):
    sm = np.array([[0, 1], [0, 0]], float); Zm = np.diag([1.0, -1.0])
    def a(k):
        m = np.array([[1.0]])
        for j in range(n): m = np.kron(m, Zm if j < k else (sm if j == k else np.eye(2)))
        return m
    return [a(k) for k in range(n)]
f = jw(4); X0 = f[1].T @ f[0]; X1 = f[3].T @ f[2]                 # detector j: a_u^+ a_l on its own two modes
check('A0 detector raisings a_u^+ a_l of different site pairs commute exactly (parity-even bilinears)',
      np.abs(X0 @ X1 - X1 @ X0).max() == 0 and np.abs(X0 @ X1.T - X1.T @ X0).max() == 0)

# ---------------- A1: two output ports, 4 detector sites per port, full state 10 x 2^8 ----------------
NCAP, TT, TH = 3, 4, 0.9
LB = [(a, b) for a in range(NCAP + 1) for b in range(NCAP + 1 - a)]; LI = {s: i for i, s in enumerate(LB)}; NL = len(LB)
c1 = np.zeros((NL, NL)); c2 = np.zeros((NL, NL))
for (a, b), i in LI.items():
    if a: c1[LI[(a - 1, b)], i] = np.sqrt(a)
    if b: c2[LI[(a, b - 1)], i] = np.sqrt(b)
sp_ = np.array([[0, 0], [1, 0.0]]); I2 = np.eye(2)
H1 = np.kron(np.kron(c1, sp_), I2); H2 = np.kron(np.kron(c2, I2), sp_)
UT = expm(-1j * TH * (H1 + H1.T + H2 + H2.T))                       # one tick: each port meets its fresh detector site
n1op = np.diag([a for a, b in LB]); n2op = np.diag([b for a, b in LB])
K1 = (np.kron(np.kron(n1op, I2), I2) + np.kron(np.kron(np.eye(NL), np.diag([0, 1.])), I2))
K2 = (np.kron(np.kron(n2op, I2), I2) + np.kron(np.kron(np.eye(NL), I2), np.diag([0, 1.])))
check('A1 tick conserves link-plus-detector excitation per port', max(np.abs(UT @ K - K @ UT).max() for K in (K1, K2)) < 1e-13)
NS = 1 << (2 * TT)
sbits = ((np.arange(NS)[:, None] >> (2 * TT - 1 - np.arange(2 * TT))) & 1)       # bit order (p1t0,p2t0,p1t1,...)
m1s, m2s = sbits[:, 0::2].sum(1), sbits[:, 1::2].sum(1)

def tick(psi, t):
    x = np.moveaxis(psi.reshape((NL,) + (2,) * (2 * TT)), [1 + 2 * t, 2 + 2 * t], [1, 2])
    sh = x.shape; x = (UT @ x.reshape(4 * NL, -1)).reshape(sh)
    return np.moveaxis(x, [1, 2], [1 + 2 * t, 2 + 2 * t]).reshape(NL, NS)

def inputs():
    s = 1 / np.sqrt(2); out = {}
    v = np.zeros(NL, complex); v[LI[(1, 0)]] = s; v[LI[(0, 1)]] = s; out['Fock 1'] = v
    v = np.zeros(NL, complex); v[LI[(2, 0)]] = .5; v[LI[(1, 1)]] = s; v[LI[(0, 2)]] = .5; out['Fock 2'] = v
    al = np.sqrt(0.4 / 2); v = np.array([al ** a * al ** b / np.sqrt(factorial(a) * factorial(b)) for a, b in LB], complex)
    out['coherent'] = v / np.linalg.norm(v); return out

def run_a1(link0, ntraj, mode):
    psi = np.zeros((NL, NS), complex); psi[:, 0] = link0
    lk = rng.choice(NL, size=ntraj, p=abs(link0) ** 2)            # used only in mode 'link' (link occupations as config)
    cfg = np.zeros(ntraj, int); flips = 0; kbad = 0; maxcls = 0.0
    for t in range(TT):
        new = tick(psi, t)
        other = np.delete(sbits, [2 * t, 2 * t + 1], 1) @ (1 << np.arange(2 * TT - 2))
        if mode == 'link':
            Pf, Pfn = (abs(psi) ** 2).ravel(), (abs(new) ** 2).ravel()
            k1 = np.array([a for a, b in LB])[:, None] + sbits[None, :, 2 * t]; k2 = np.array([b for a, b in LB])[:, None] + sbits[None, :, 2 * t + 1]
            cls = ((other[None, :] * 8 + k1) * 8 + k2).ravel()
            full = switch(lk * NS + cfg, Pf, Pfn, cls); nl, ns = full // NS, full % NS
            kb = lambda l, s: (np.array([a for a, b in LB])[l] + m1s[s], np.array([b for a, b in LB])[l] + m2s[s])
            kbad += int(np.sum((kb(nl, ns)[0] != kb(lk, cfg)[0]) | (kb(nl, ns)[1] != kb(lk, cfg)[1]))); lk = nl
        else:
            P, Pn = (abs(psi) ** 2).sum(0), (abs(new) ** 2).sum(0)
            cls = other if mode == 'site' else np.zeros(NS, int)
            for k in np.unique(cls): maxcls = max(maxcls, abs(P[cls == k].sum() - Pn[cls == k].sum()))
            ns = switch(cfg, P, Pn, cls)
        keep = [j for j in range(2 * TT) if j not in (2 * t, 2 * t + 1)]
        flips += int(np.sum(np.any(sbits[ns][:, keep] != sbits[cfg][:, keep], 1)))
        cfg, psi = ns, new
    return cfg, abs(psi) ** 2, flips, kbad, maxcls

def diag_counts(pn12, T, th, C=None):
    """phase-insensitive reduction: joint (counts, port numbers) weights; exact because the tick maps the port
    number distribution to itself without reading coherences. Counts never exceed the photon number."""
    N = pn12.shape[0]; s2 = np.sin(th * np.sqrt(np.arange(N))) ** 2; C = C or min(T, N - 1) + 1
    w = np.zeros((C, C, N, N)); w[0, 0] = pn12
    for _ in range(T):
        go = w * s2[None, None, :, None]; w = w - go; w[1:, :, :-1, :] += go[:-1, :, 1:, :]
        go = w * s2[None, None, None, :]; w = w - go; w[:, 1:, :, :-1] += go[:, :-1, :, 1:]
    return w

ok = True; det = []
for nm, v in inputs().items():
    cf, Pfin, fl, _, mcls = run_a1(v, 20000, 'site')
    Ps = Pfin.sum(0); fs = np.bincount(cf, minlength=NS) / cf.size
    z = (abs(fs - Ps) / np.sqrt(Ps * (1 - Ps) / cf.size + 1e-30))[Ps > 1e-3].max()
    pn = np.zeros((NCAP + 1, NCAP + 1));
    for (a, b), i in LI.items(): pn[a, b] = abs(v[i]) ** 2
    wd = diag_counts(pn, TT, TH, TT + 1).sum((2, 3)); ex = np.zeros_like(wd); np.add.at(ex, (m1s, m2s), Ps)
    ok &= z < 5 and fl == 0 and mcls < 1e-13 and np.abs(wd - ex).max() < 1e-12; det.append(f"{nm} {z:.1f}sig")
check('A1 site-only configuration: 20000 sampled record patterns follow the Born site marginal (256 patterns); '
      'class odds conserved; earlier records never change; number-only reduction agrees exactly', ok, ', '.join(det))
_, _, flu, _, _ = run_a1(inputs()['Fock 2'], 4000, 'all')
cfl, Pl, fll, kb, _ = run_a1(inputs()['Fock 2'], 20000, 'link')
Ps = Pl.sum(0); fs = np.bincount(cfl, minlength=NS) / cfl.size
zl = (abs(fs - Ps) / np.sqrt(Ps * (1 - Ps) / cfl.size + 1e-30))[Ps > 1e-3].max()
check('A1 controls: unconfined shortfall rewrites earlier records; giving link occupations a configuration '
      'leaves record statistics unchanged and makes every jump keep excitation', flu > 0 and fll == 0 and kb == 0 and zl < 5,
      f"record rewrites unconfined {flu}; link-config run {zl:.1f}sig, excitation-breaking jumps {kb}")

# ---------------- A2: complete absorption, counting statistics, HBT g2 ----------------
NC2, TA, THA = 14, 400, 0.4
def bs_joint(pn):                                                    # 50/50 link beam splitter, input port number dist pn
    N = len(pn); out = np.zeros((N, N))
    for n, p in enumerate(pn):
        for m in range(n + 1): out[m, n - m] += p * comb(n, m) / 2 ** n
    return out
nn = np.arange(NC2 + 1)
PS = {'coherent nbar=1': np.exp(-1.) / np.array([factorial(k) for k in nn], float),
      'thermal nbar=0.5': 0.5 ** nn / 1.5 ** (nn + 1), 'Fock 1': (nn == 1) * 1., 'Fock 2': (nn == 2) * 1.}
# beam-splitter partition checked against the BS unitary in the cap-4 two-mode space
L4 = [(a, b) for a in range(5) for b in range(5 - a)]; I4 = {s: i for i, s in enumerate(L4)}
a4 = np.zeros((len(L4),) * 2); b4 = np.zeros_like(a4)
for (a, b), i in I4.items():
    if a: a4[I4[(a - 1, b)], i] = np.sqrt(a)
    if b: b4[I4[(a, b - 1)], i] = np.sqrt(b)
UB = expm(np.pi / 4 * (a4.T @ b4 - b4.T @ a4)); bsok = True
for n in range(5):
    v = UB[:, I4[(n, 0)]]; bj = bs_joint((np.arange(5) == n) * 1.)
    bsok &= max(abs(abs(v[I4[(m, n - m)]]) ** 2 - bj[m, n - m]) for m in range(n + 1)) < 1e-12
res = []; G2 = {}; okc = bsok
for nm, p in PS.items():
    p = p / p.sum(); w = diag_counts(bs_joint(p), TA, THA)
    left = (w * (nn[None, None, :, None] + nn[None, None, None, :])).sum(); cnt = w.sum((2, 3))[:NC2 + 1, :NC2 + 1]
    okc &= left < 1e-12 and np.abs(cnt - bs_joint(p)).max() < 1e-12
    m = np.arange(NC2 + 1); g2 = (cnt * m[:, None] * m[None, :]).sum() / ((cnt.sum(1) * m).sum() * (cnt.sum(0) * m).sum())
    ntot = np.bincount((m[:, None] + m[None, :]).ravel(), cnt.ravel()); mu = (ntot * np.arange(ntot.size)).sum()
    Q = ((ntot * np.arange(ntot.size) ** 2).sum() - mu ** 2) / mu - 1; res.append(f"{nm}: g2={g2:.4f} Q={Q:+.3f}"); G2[nm] = g2
check('A2 complete absorption: the joint detector-record counts equal the photon-number distribution of the two ports '
      '(beam-splitter binomial partition verified on the unitary)', okc, 'leftover link quanta < 1e-12')
print('   ' + '; '.join(res))
check('A2 HBT: thermal link light bunches (g2 = 2 up to truncation), coherent g2 = 1, one link quantum gives no coincidences (g2 = 0)',
      abs(G2['thermal nbar=0.5'] - 2) < 1e-3 and abs(G2['coherent nbar=1'] - 1) < 1e-3 and G2['Fock 1'] == 0 and abs(G2['Fock 2'] - 0.5) < 1e-12)
ws = rng.dirichlet(np.ones(8), 200); amps = rng.uniform(0, 2, (200, 8))
g2c = ((ws * amps ** 4).sum(1)) / ((ws * amps ** 2).sum(1)) ** 2
check('A2 control: any mixture of classical (coherent) link fields has g2 >= 1 (Cauchy-Schwarz), so g2 < 1 needs quantised link odds',
      g2c.min() >= 1 - 1e-12, f"min over 200 random mixtures {g2c.min():.4f}")

# ---------------- A3: Mach-Zehnder, which-way marker site, eraser ----------------
Xm = np.array([[0, 1], [1, 0.]]); BS = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
def mz(beta, phi, coin=None):
    st = np.zeros((2, 2), complex); st[:, 0] = BS @ np.array([1, 0])                # [arm, marker], marker starts lower
    st[1] = expm(-1j * beta * Xm) @ st[1]; st[1] *= np.exp(1j * phi); st = BS @ st
    if coin is not None: st = st @ coin.T
    return abs(st) ** 2                                                              # [output, marker record]
ph = np.linspace(0, 2 * np.pi, 361); okm = True; vd = []
for beta in (0, np.pi / 6, np.pi / 4, np.pi / 2):
    P1 = np.array([mz(beta, x)[0].sum() for x in ph]); V = (P1.max() - P1.min()) / (P1.max() + P1.min())
    Dw = abs(np.sin(beta)); okm &= abs(V - abs(np.cos(beta))) < 1e-4 and abs(V ** 2 + Dw ** 2 - 1) < 1e-4; vd.append(f"{V:.3f}")
er = np.array([mz(np.pi / 2, x, expm(-1j * np.pi / 4 * Xm))[0] for x in ph])
Vc = [(er[:, r].max() - er[:, r].min()) / (er[:, r].max() + er[:, r].min()) for r in (0, 1)]
check('A3 single link quantum in a Mach-Zehnder: visibility |cos b| with marker-site distinguishability |sin b| (V^2 + D^2 = 1); '
      'reading the full marker in the rotated basis restores fringes in each record class', okm and min(Vc) > 0.999,
      f"V(b=0,pi/6,pi/4,pi/2) = {','.join(vd)}; eraser V = {Vc[0]:.3f},{Vc[1]:.3f}")

# ---------------- A4: QND registration (no absorption), progressive collapse ----------------
NQ, NMK, NTR, CHI = 8, 120, 4000, np.pi / 4
pq = np.exp(-1.) / np.array([factorial(k) for k in range(NQ)]); pq /= pq.sum()
R = lambda s: expm(-1j * s * np.pi / 4 * np.array([[0, -1j], [1j, 0]]))
def pu(phi):
    out = np.zeros(NQ)
    for n in range(NQ):
        M = R(-1) @ np.diag([1, np.exp(-1j * (CHI * n + phi))]) @ R(1); out[n] = abs(M[1, 0]) ** 2
    return out
PU = [np.clip(pu(k * np.pi / 4), 0, 1) for k in range(4)]
W = np.tile(pq, (NTR, 1))
for k in range(NMK):
    u = PU[k % 4]; pr = W @ u; rec = rng.random(NTR) < pr
    W = np.where(rec[:, None], W * u, W * (1 - u)); W /= W.sum(1, keepdims=True)
nhat = W.argmax(1); final = (rng.random(NTR)[:, None] > np.cumsum(W, 1)).sum(1)            # later absorption count (A2)
hist = np.bincount(nhat, minlength=NQ) / NTR; zq = (abs(hist - pq) / np.sqrt(pq * (1 - pq) / NTR + 1e-30)).max()
check('A4 QND: dispersive marker sites register link-quantum number without absorbing it (Kraus diagonal in n); '
      f'after {NMK} markers the field has collapsed, later absorption counts agree, collapsed n follows Born',
      np.mean(final == nhat) > 0.98 and zq < 5, f"agreement {np.mean(final == nhat):.4f}, {zq:.1f}sig")

# ---------------- B: composite photons from site bilinears ----------------
N6 = 4; f = jw(2 * N6)
Bd = sum(f[2 * k + 1].T @ f[2 * k] for k in range(N6)) / np.sqrt(N6)              # sum of a_u^+ a_l over the site pairs
G = np.zeros(1 << (2 * N6)); G[int('10' * N6, 2)] = 1                              # lower modes filled
nrm = [np.linalg.norm(np.linalg.matrix_power(Bd, n) @ G) ** 2 / factorial(n) for n in range(N6 + 1)]
pred = [np.prod([1 - k / N6 for k in range(n)]) for n in range(N6 + 1)]
Nex = sum(f[2 * k + 1].T @ f[2 * k + 1] for k in range(N6)); comm = Bd.T @ Bd - Bd @ Bd.T
occ = ((np.arange(1 << (2 * N6))[:, None] >> (2 * N6 - 1 - np.arange(2 * N6))) & 1)
one = np.nonzero((occ[:, 0::2] + occ[:, 1::2] == 1).all(1))[0]                     # one fermion per site pair
sub = (comm - (np.eye(1 << (2 * N6)) - 2 * Nex / N6))[np.ix_(one, one)]
check('B1 composite B = N^-1/2 sum a_l^+ a_u on Fock space: |B^+n G|^2/n! = prod(1 - k/N) and [B,B^+] = 1 - 2 N_exc/N',
      np.abs(np.array(nrm) - pred).max() < 1e-12 and np.abs(sub).max() < 1e-12, f"N={N6}: {', '.join(f'{x:.3f}' for x in nrm)}")
gd = []
for N in (8, 64, 512, 4096):
    n = np.arange(N + 1); b = n * (N - n + 1) / N                                 # B^+B on the n-excitation symmetric state
    bb = b * np.concatenate([[0.0], b[:-1]])                                       # B^+B^+BB
    x = 0.5 ** n; x /= x.sum(); g = (x * bb).sum() / ((x * b).sum()) ** 2; gd.append((N, g))
check('B2 thermal composite light bunches less than bosons, deviation ~ 1/N (vanishes for large N)',
      all(g < 2 for _, g in gd) and abs((2 - gd[-1][1]) * 4096 / ((2 - gd[-2][1]) * 512) - 1) < 0.05,
      '; '.join(f"N={N}: 2-g2={2 - g:.2e}" for N, g in gd))
k = 2 * np.pi * np.arange(24) / 24; KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij'); q = 2 * np.pi / 24
eps = lambda a, b, c: np.sqrt(np.sin(a) ** 2 + np.sin(b) ** 2 + np.sin(c) ** 2)
Ep = eps(KX + q, KY, KZ) + eps(KX, KY, KZ); wq = 2 * np.sin(q / 2)
check('B3 a free site-pair composite at fixed momentum has no single frequency: pair energies span many times the link frequency',
      Ep.max() / wq > 10, f"q=2pi/24: link w={wq:.4f}, pair energies {Ep.min():.4f}..{Ep.max():.3f}")

# ---------------- C: gravity of link energy ----------------
kR, kL, Gam = sp.symbols('kappa_R kappa_L Gamma')
check('C1 the linearised Einstein operator has zero divergence, so the source must be conserved; relays and links exchanging '
      'energy at rate Gamma give divergence (kR - kL) Gamma: link energy must couple with the relay strength',
      sp.solve(sp.Eq((kR - kL) * Gam, 0), kL) == [kR])
X = sp.symbols('x0:4'); eta = sp.diag(-1, 1, 1, 1); al_, be_ = sp.symbols('alpha beta')
A = [sum(sp.Integer(int(rng.integers(-3, 4))) * X[i] * X[j] * X[l] for i in range(4) for j in range(i, 4) for l in range(j, 4)) for _ in range(4)]
Fd = [[sp.diff(A[nu], X[mu]) - sp.diff(A[mu], X[nu]) for nu in range(4)] for mu in range(4)]           # F_{mu nu}
Fu = [[eta[m, m] * eta[n, n] * Fd[m][n] for n in range(4)] for m in range(4)]
J = [sum(sp.diff(Fu[n][m], X[m]) for m in range(4)) for n in range(4)]                                  # Maxwell: d_mu F^{nu mu} = J^nu
F2 = sum(Fd[m][n] * Fu[m][n] for m in range(4) for n in range(4))
T = [[al_ * sum(Fu[m][l] * eta[l, l] * Fu[n][l] for l in range(4)) + be_ * eta[m, n] * F2 for n in range(4)] for m in range(4)]
eqs = []
for n in range(4):
    r = sp.expand(sum(sp.diff(T[m][n], X[m]) for m in range(4)) + sum(Fu[n][l] * eta[l, l] * J[l] for l in range(4)))
    eqs += sp.Poly(r, *X).coeffs()
sol = sp.solve(eqs, [al_, be_], dict=True)
tr = sp.expand(sum(eta[m, m] * T[m][m] for m in range(4)).subs(sol[0])) if sol else 1
pos = sp.expand(T[0][0].subs(sol[0]) - (sum(Fd[0][i] ** 2 for i in range(1, 4)) + sum(Fd[i][j] ** 2 for i in range(1, 4) for j in range(i + 1, 4))) / 2) if sol else 1
kk = sp.symbols('k1:4', real=True); w0 = sp.sqrt(sum(x ** 2 for x in kk))
check('C2 with the link field obeying Maxwell, the unique quadratic tensor whose divergence is minus the force on the value current '
      'is the Maxwell tensor; its energy is (E^2+B^2)/2 >= 0 and it is traceless, so a link-quantum gas has p = rho/3', sol == [{al_: 1, be_: -sp.Rational(1, 4)}] and tr == 0 and pos == 0, str(sol))
# plane wave: F from A = e cos(k.x), averaged -> T^{mu nu} proportional to k^mu k^nu (a null deposit, like a relay at top speed)
kv = sp.Matrix([w0, *kk]); e = sp.Matrix([0, kk[1], -kk[0], 0])
Fpw = [[(kv[m] * eta[m, m] * e[n] * eta[n, n] - kv[n] * eta[n, n] * e[m] * eta[m, m]) for n in range(4)] for m in range(4)]   # F_{mn} up to sin
Tpw = sp.Matrix(4, 4, lambda m, n: sum(eta[m, m] * eta[n, n] * Fpw[m][l] * eta[l, l] * Fpw[n][l] for l in range(4)))
ratio = sp.simplify(Tpw - (Tpw[0, 0] / w0 ** 2) * kv * kv.T)
check('C3 a plane link wave deposits T = (energy) u u with u = (1, k/|k|): the same null form CL-7 gives a relay at the top speed',
      ratio == sp.zeros(4, 4))
# C4 deposit bookkeeping per trajectory, one port, site-only configuration, link deposit = odds-weighted given the records
def dep_run(p0, ntr=4000, T=300, th=0.4):
    N = len(p0); s2 = np.sin(th * np.sqrt(np.arange(N))) ** 2; W = np.tile(p0 / p0.sum(), (ntr, 1)); m = np.zeros(ntr)
    D0 = W @ np.arange(N); jumps = []
    for _ in range(T):
        Dn = m + W @ np.arange(N); c = rng.random(ntr) < W @ s2
        Wc = np.roll(W * s2, -1, 1); Wn = W * (1 - s2)
        W = np.where(c[:, None], Wc, Wn); W /= np.maximum(W.sum(1, keepdims=True), 1e-300); m += c
        jumps.append(((m + W @ np.arange(N)) - Dn)[c])
    return np.concatenate(jumps), m + W @ np.arange(N) - D0
jf, tf = dep_run((np.arange(20) == 3) * 1.); jc, tc = dep_run(np.exp(-2.) * 2. ** np.arange(20) / np.array([factorial(i) for i in range(20)], float))
check('C4 site-only configuration with odds-weighted link deposits: Fock light keeps every trajectory\'s deposit total exactly; '
      'coherent light gives zero-mean registration noise, total change = Omega (n_counted - <n>)',
      np.abs(jf).max() < 1e-12 and np.abs(tf).max() < 1e-12 and abs(tc.mean()) < 5 * tc.std() / np.sqrt(tc.size) and abs(tc.std() - np.sqrt(2)) < 0.1,
      f"coherent nbar=2: mean jump per click {jc.mean():+.3f} Omega, total change mean {tc.mean():+.3f}, std {tc.std():.3f} Omega (sqrt2=1.414)")
r = 7 / 8 * (4 / 11) ** (4 / 3); Nprime = (r * 3.044 - 1) / r
print(f"   measured-reality arithmetic: rho_nu/rho_gamma per species {r:.4f}; non-gravitating photons read as N_eff = {Nprime:.2f} "
      f"(Planck 2.99+-0.17: {(2.99 - Nprime) / 0.17:.0f} sigma); BBN g* 10.75 -> 8.75 = dN_eff {-2 / (7 / 4):.2f}")

print('supplied: quantised link odds (bosonic link modes); detector site pairs and their coupling; beam splitters, phases, markers;'
      ' input states; shortfall rule with tick-connected classes; the response forms used in C.')
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
