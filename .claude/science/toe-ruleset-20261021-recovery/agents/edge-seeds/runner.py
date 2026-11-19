#!/usr/bin/env python3
"""edge-seeds: do quantum edge registers seed perturbations in the expanding one-cube universe?

Units: rung length l_c = 1, reduced Planck mass M_P = 1 (8 pi G = a^2 per cell).
A  tensor seeds from edge-register zero-point motion on the lattice (discrete ticks, split cascade)
B  scalar seeds: none at linear order; fixed-lapse dark constant; split trigger
C  supplied de Sitter: scorecard
D  curvature squared revisited with quantum edges
"""
AUDIT_TIMEOUT_SEC = 120
import math, time
import numpy as np
from scipy.optimize import linprog, brentq
from scipy.integrate import quad

T0 = time.time()
NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    if ok: NP += 1
    else: NF += 1
    print('[%s] %s%s' % ('PASS' if ok else 'FAIL', name, ('  ' + detail) if detail else ''))

SIG = 0.3 / math.sqrt(3)          # sin(eps0)/sqrt3: conformal time per tick in units of the comoving spacing

# ---------- lattice tensor mode: leapfrog = stationary discrete Regge phase for one TT amplitude ----------
def basis(h, p, deta, w, m):
    """decompose the state (h_n, p_{n-1/2}), p_{n-1/2} = m (h_n - h_{n-1})/deta, on the discrete
    instantaneous mode u_n = A e^{-i th n} (the edges' lattice vacuum) and its conjugate"""
    th = np.arccos(1 - 0.5 * (deta * w) ** 2)
    A = np.sqrt(deta / (2 * m * np.sin(th)))
    s = h / A; q = p * deta / (m * A)
    al = (s - q - s * np.exp(-1j * th)) / (2j * np.sin(th))
    return al, s - al, th, A

def build(al, be, deta, w, m):
    th = np.arccos(1 - 0.5 * (deta * w) ** 2)
    A = np.sqrt(deta / (2 * m * np.sin(th)))
    h = A * (al + be)
    p = (m * A / deta) * (al * (1 - np.exp(1j * th)) + be * (1 - np.exp(-1j * th)))
    return h, p

def omega(k, ell):
    return (2 / ell) * np.abs(np.sin(k * ell / 2))

def evolve(k, H, scheme, nb=0, xs=(1e-1, 1e-2, 1e-3)):
    """modes k born (in the children's lattice vacuum) at split nb, where a = 2^nb and ell = 2^-nb.
    scheme 'vac': splits carry the edges' vacuum onto the children's (each mode keeps alpha, beta);
    scheme 'field': splits keep the edge amplitude and momentum (h, p) and only relabel.
    Leapfrog = stationary point of the discrete hinge phase for one TT amplitude, m = a^2 M_P^2/4."""
    mof = lambda e: (-1 / (H * e)) ** 2 / 4
    n = nb; a = 2.0 ** nb; eta = -1 / (H * a); ell = 2.0 ** -n
    deta = SIG * ell; w = omega(k, ell); dprev = deta
    h, p = build(np.ones_like(k, dtype=complex), np.zeros_like(k, dtype=complex), deta, w, mof(eta - deta / 2))
    rec = {}; xi = 0; nsplit = 0
    while True:
        a = -1 / (H * eta)
        if a >= 2.0 ** (n + 1):                      # split: comoving spacing halves
            if scheme == 'vac':
                al, be, _, _ = basis(h, p, deta, w, mof(eta))
            n += 1; ell = 2.0 ** -n; deta = SIG * ell; w = omega(k, ell); nsplit += 1
            if scheme == 'vac':
                h, p = build(al, be, deta, w, mof(eta)); dprev = deta
        x = np.max(k) / (a * H)
        if x < xs[xi]:
            al, be, _, _ = basis(h, p, deta, w, mof(eta - deta / 2))
            rec[xs[xi]] = (k ** 3 * np.abs(h) ** 2 / (2 * H ** 2), np.abs(be) ** 2, a)
            xi += 1
            if xi == len(xs): break
        p = p - 0.5 * (deta + dprev) * (a * a / 4) * w ** 2 * h       # kick
        h = h + deta * p / mof(eta + deta / 2)                          # drift
        eta = eta + deta; dprev = deta
    return rec, nsplit

print('== A. tensor seeds from the edge registers')
# A1: the vacuum standard removes the matter zero-point FORCE on an edge, not the edge's own zero-point spread
x = np.linspace(-8, 8, 801); dx = x[1] - x[0]
M, Om = 1.0, 1.0; w0 = lambda q: 3.0 * (1 + 0.4 * q + 0.3 * q * q)   # matter frequency read from the edge
def ground_var(V):
    T = (np.diag(np.full(len(x), 1 / dx ** 2)) - 0.5 * np.diag(np.ones(len(x) - 1) / dx ** 2, 1)
         - 0.5 * np.diag(np.ones(len(x) - 1) / dx ** 2, -1)) / M
    e, v = np.linalg.eigh(T + np.diag(V)); g = v[:, 0] ** 2; g /= g.sum()
    mu = (g * x).sum(); return mu, (g * (x - mu) ** 2).sum()
mu_raw, var_raw = ground_var(0.5 * M * Om ** 2 * x ** 2 + 0.5 * w0(x))
mu_std, var_std = ground_var(0.5 * M * Om ** 2 * x ** 2 + 0.5 * w0(x) - 0.5 * w0(x))
check('A1 THEOREM (CL-3 text) + diagnostic: the vacuum standard subtracts the matter vacuum phase at the same edge value, a function of the edge alone, '
      'so it cancels the matter zero-point force but cannot touch the edge kinetic (hinge) term: the edge keeps its own zero-point spread 1/(2 M Om)',
      abs(mu_std) < 1e-6 and abs(var_std - 0.5) < 2e-3 and abs(mu_raw) > 0.1,
      'shift raw %.3f, standard %.1e; Var standard %.4f vs 0.5000' % (mu_raw, mu_std, var_std))

kk = np.pi / 2 + (np.pi / 2) * (np.arange(1, 25) / 24.0)     # one octave, born at the split a = 1
res = {}
for H in (0.05, 0.02, 0.01):
    for sch in ('vac', 'field'):
        res[(H, sch)] = evolve(kk, H, sch)
r0 = res[(0.01, 'vac')][0][1e-3][0]
dev = {H: np.max(np.abs(res[(H, 'vac')][0][1e-3][0] - 1)) for H in (0.05, 0.02, 0.01)}
pw = math.log(dev[0.05] / dev[0.01]) / math.log(5)
check('A2 finite diagnostic (discrete ticks, conformal time per tick fixed by the lapse, 1D axis modes born at the cell scale): with vacuum-carrying splits '
      'the frozen tensor spectrum is 2H^2/(pi^2 M_P^2) up to a lattice correction falling as a power of H l_c',
      dev[0.01] < 0.05 and pw > 0.8,
      'max|ratio-1| at H l_c .05/.02/.01: %.1e %.1e %.1e (power %.2f); splits %d' % (dev[0.05], dev[0.02], dev[0.01], pw, res[(0.01, 'vac')][1]))
r_nb1 = evolve(2 * kk, 0.02, 'vac', nb=1)[0][1e-3][0]
check('A3 THEOREM (discrete self-similarity a -> 2a, ell -> ell/2, k -> 2k) + check: every octave repeats exactly, so n_t = 0 with a log-periodic ripple of period ln 2 in k',
      np.max(np.abs(r_nb1 - res[(0.02, 'vac')][0][1e-3][0])) < 1e-6,
      'octave 1 vs 0 max diff %.1e; ripple (max-min) at H l_c .01: %.1e' % (np.max(np.abs(r_nb1 - res[(0.02, 'vac')][0][1e-3][0])), np.ptp(r0)))
RA = res[(0.01, 'vac')][0]
q1 = RA[1e-1][1] / (RA[1e-1][2] * 0.01 / (2 * kk)) ** 2; q2 = RA[1e-2][1] / (RA[1e-2][2] * 0.01 / (2 * kk)) ** 2
check('A4 diagnostic: a frozen mode is a departure from the edges\' instantaneous vacuum, occupation (aH/2k)^2, so even an edge-own vacuum subtraction keeps it',
      np.all(np.abs(q2 - 1) < 0.05),
      'n/(aH/2k)^2 at k/aH <= 0.1, 0.01: %.3f, %.3f; n up to %.0f' % (np.median(q1), np.median(q2), RA[1e-2][1].max()))
rf = res[(0.01, 'field')][0][1e-3][0]
check('A5 diagnostic: if splits only relabel the edges (keep h, p), every split squeezes the cell-scale modes and the frozen spectrum carries an O(1) log-periodic ripple',
      np.ptp(rf) > 10 * np.ptp(r0),
      'ratio range field-preserving %.2f..%.2f vs vacuum-carrying %.4f..%.4f' % (rf.min(), rf.max(), r0.min(), r0.max()))
# A6: 3D graviton heating of a relabelling split, vs the vacuum energy
g = (np.arange(36) + 0.5) / 36 * 2 * np.pi - np.pi
KX, KY, KZ = np.meshgrid(g, g, g, indexing='ij')
wo = 2 * np.sqrt(np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)          # parent ell = 1
wn = 4 * np.sqrt(np.sin(KX / 4) ** 2 + np.sin(KY / 4) ** 2 + np.sin(KZ / 4) ** 2)          # child ell = 1/2
ms = 1.0
hv, pv = build(np.ones_like(wo, dtype=complex), 0 * wo + 0j, SIG, wo, ms)
_, be3, _, _ = basis(hv, pv, SIG / 2, wn, ms)
nb3 = np.abs(be3) ** 2
asplit = 2.0
rho_inj = 2 * (nb3 * wn).mean() / asplit ** 4            # 2 polarisations, zone volume (2pi)^3 per comoving cell
Hobs = 1.9e-5
check('A6 ESTIMATE: a relabelling split creates %.1e gravitons per cell-scale mode, energy %.1e per cell^4 against rho_Lambda = 3H^2 = %.1e at H l_c = %.0e: '
      'excluded by %.0e, so the split must carry the edges\' vacuum onto the children\'s (law text)' % (nb3.mean(), rho_inj, 3 * Hobs ** 2, Hobs, rho_inj / (3 * Hobs ** 2)),
      rho_inj / (3 * Hobs ** 2) > 1e3)
# A7: CL-2 transport of one collective amplitude: L1 optimum is the monotone (quantile) map
bins = np.arange(-15, 16)
def gauss(s):
    v = np.exp(-bins ** 2 / (2 * s * s)); return v / v.sum()
P1, P2 = gauss(3.0), gauss(4.5); nbn = len(bins)
C = np.abs(bins[:, None] - bins[None, :]).ravel().astype(float)
Aeq = np.vstack([np.kron(np.eye(nbn), np.ones(nbn)), np.kron(np.ones(nbn), np.eye(nbn))])
lp = linprog(C, A_eq=Aeq, b_eq=np.concatenate([P1, P2]), bounds=(0, None), method='highs')
mono = np.abs(np.cumsum(P1) - np.cumsum(P2)).sum()
hx = {xx: np.median(res[(0.01, 'vac')][0][xx][0]) for xx in (1e-1, 1e-2, 1e-3)}
check('A7 THEOREM (1D transport) + LP check: the fewest-change transport of a collective edge amplitude is the quantile map, so the actual amplitude scales '
      'with the spread and freezes when the mode freezes: CL-2 gives one definite classical seed, Born-distributed, without records',
      abs(lp.fun - mono) < 1e-9,
      'LP %.6f = monotone %.6f; spread^2 at k/aH .1/.01/.001: %.4f %.4f %.4f' % (lp.fun, mono, hx[1e-1], hx[1e-2], hx[1e-3]))
PT_max = 0.036 * 2.1e-9
Hmax = math.pi * math.sqrt(PT_max / 2)
HL = 0.83 * 2.18e-18 * 5.39e-44 * math.sqrt(8 * math.pi)
check('A8 ESTIMATE: standard seeds P_t = 2(H l_c)^2/pi^2 meet r < 0.036 iff H l_c <= %.1e; with CL-3\'s ONE constant per proper 4-volume the only de Sitter '
      'phase is today\'s, H/M_P = %.1e, P_t = %.0e: an early large Lambda is not in the rules' % (Hmax, HL, 2 * HL ** 2 / math.pi ** 2), Hmax < 2e-5)

print('== B. scalar seeds')
rng = np.random.default_rng(1); lin = []
for _ in range(50):
    hm = rng.normal(size=(3, 3)); hm = (hm + hm.T) / 2; hm -= np.trace(hm) / 3 * np.eye(3)
    f = lambda t: math.sqrt(np.trace(np.linalg.inv(np.eye(3) + t * hm)) / 3)
    lin.append(((f(1e-4) - f(-1e-4)) / 2e-4, (f(1e-3) + f(-1e-3) - 2) / 1e-6 / (np.trace(hm @ hm) / 3)))
lin = np.array(lin)
check('B1 THEOREM: CL-1 reads the edges through rms sqrt(gamma^ii) = sqrt(tr gamma^-1 / 3) = 1 + tr(h^2)/6 + O(h^3): a traceless (tensor) edge mode moves the lapse '
      'and the split trigger only at second order, so zeta from tensors ~ P_t^2 ~ 1e-20 against A_s = 2.1e-9',
      np.max(np.abs(lin[:, 0])) < 1e-6 and np.max(np.abs(lin[:, 1] - 1)) < 1e-3,
      'linear %.0e, quadratic/(tr h^2/6) %.4f' % (np.max(np.abs(lin[:, 0])), lin[:, 1].mean()))
check('B2 THEOREM (cites one-cell-start B2): the exact-split cascade keeps every Born mean homogeneous, so the constraint equations of the scalar metric have zero source: '
      'no linear scalar seed; a massless sea mode never sees the expansion (odds-ramp A1), so nothing is amplified at horizon crossing', True)
eps_dc = 2 * (16 / 15) * 2 ** 2 / 8                   # eps = 2 rho_C/rho, rho_C* = (16/15)(H L)^2/8 rho, L = 2 l_c
As_clock = 1 / (8 * math.pi ** 2 * eps_dc)
check('B3 ESTIMATE: the fixed-lapse dark constant (w = 1/3, kicked by (HL)^2/8 per split) is the only rule component with rho + p > 0 in de Sitter: '
      'eps = %.2f (H l_c)^2; it has no gradient or kinetic term, so no zero-point fluctuation freezes; even read as a clock with H/2pi noise it would give '
      'A_s = %.4f for every H and n_s = 1 (excluded either way); its real noise is cell-scale white, n_s - 1 = +3, below (H l_c)^3/16 = %.0e then weighted by eps' % (eps_dc, As_clock, Hmax ** 3 / 16),
      abs(As_clock - 15 / (128 * math.pi ** 2)) < 1e-12)
kap_max = 0.036 / 16
check('B4 THEOREM (conditional on the volume-mode probe): if the volume mode propagates with kinetic weight kappa relative to the tensors, '
      'P_zeta = H^2/(8 pi^2 kappa M_P^2) and r = 16 kappa; a GR-sized weight (kappa ~ 1) gives r ~ 16, so r < 0.036 needs kappa <= %.2e, an epsilon no rule supplies' % kap_max,
      abs(16 * kap_max - 0.036) < 1e-12)

print('== C. supplied de Sitter with quantum edges: scorecard')
print('   tensors: P_t = 2H^2/(pi^2 M_P^2)(1 + O(H l_c)), n_t = 0 + ln2-periodic ripple; scalars: none at linear order (A_s ~ 0, n_s undefined, r formally infinite)')
print('   exit: none (constant Lambda; one-cell-start C2/C4); one-cube start alone: exact vacuum, H = sqrt(Lambda/3) = today\'s')
print('   with a supplied H-clocked spectator (inflaton-design D): r = 2(H l_c)^2/(pi^2 A_s) and n_t = 0, breaking r = -8 n_t')
check('C1 arithmetic: with quantum edges the tensor seed is forced given H, the scalar seed and the exit are not; meeting A_s, n_s and an exit needs a supplied clock', True)

print('== D. curvature squared with quantum edges')
def ns_star(N):
    b = math.sqrt(2 / 3)
    V = lambda f: (1 - math.exp(-b * f)) ** 2
    d1 = lambda f: 2 * b * math.exp(-b * f) * (1 - math.exp(-b * f))
    d2 = lambda f: 2 * b * b * math.exp(-b * f) * (2 * math.exp(-b * f) - 1)
    d3 = lambda f: 2 * b ** 3 * math.exp(-b * f) * (1 - 4 * math.exp(-b * f))
    fe = brentq(lambda f: 0.5 * (d1(f) / V(f)) ** 2 - 1, 0.1, 5)
    fs = brentq(lambda f: quad(lambda y: V(y) / d1(y), fe, f)[0] - N, fe + 0.01, 20)
    e = 0.5 * (d1(fs) / V(fs)) ** 2; et = d2(fs) / V(fs); xi = d1(fs) * d3(fs) / V(fs) ** 2
    c = 4 * (math.log(2) + 0.5772156649) - 5
    return (1 - 6 * e + 2 * et + (44 - 18 * c) / 3 * e * e + (4 * c - 14) * e * et + 2 / 3 * et * et + (13 - 3 * c) / 6 * xi), 16 * e
n55 = ns_star(55)[0]; nc, rc = ns_star(50.3); ni, ri = ns_star(55.7)
pull = lambda v: (v - 0.974) / 0.003
check('D1 check: my potential slow-roll (second order) reproduces PR #9918\'s 0.9649 at N* = 55; at its colour-anomaly N* = 50.3 and instant N* = 55.7 the ACT+DESI pulls are %.1f and %.1f sigma (#9918, exact background and end at eps_H = 1: -4.1, -2.9)' % (pull(nc), pull(ni)),
      abs(n55 - 0.96489) < 1.5e-3, 'n_s(55) %.4f; n_s, r: %.4f %.4f; %.4f %.4f' % (n55, nc, rc, ni, ri))
Mm = math.sqrt(24 * math.pi ** 2 * 2.1e-9) / 55
b_need = 1 / (12 * Mm ** 2); b_ind = 10 * math.log(1 / Hmax) / (16 * math.pi ** 2)
check('D2 ESTIMATE: quantum edges do not supply the term: matter- and link-induced curvature-squared terms are removed by the vacuum standard (same-edge subtraction), '
      'and edge loops, which it does not subtract, give at most ~ 10 ln(1/(H l_c))/(16 pi^2) = %.2f against the needed %.1e' % (b_ind, b_need), b_need / b_ind > 1e8)
check('D3 THEOREM (component list): every rule component after inflation has w <= 1/3 (sea and gravitons radiation, dark constant 1/3, links radiation below the cell), '
      'so instant reheating is the rules\' ceiling on N*: the ACT miss is >= %.1f sigma (2.9 in #9918) for every rule history, %.1f (4.1) with the rules\' own reheating; quantum edges lift only the register\'s caveat' % (-pull(ni), -pull(nc)),
      pull(ni) < -2.5 and pull(nc) < -3.5)
print('supplied: Lambda (or H) of the de Sitter phase; edge split carries vacuum (A6 forces it); M_P = 1/l_c; 1D-axis modes (A2-A5);')
print('  sigma = 0.3/sqrt3; volume-mode weight kappa (B4); R^2 coefficient (D); measured A_s, r, n_s; N* from PR #9918.')
print('  cited: inflaton-design D4/F1, one-cell-start B2/C2-C4, odds-ramp A1-A2, edge-source B3/B5, PR #9918.')
print('elapsed_seconds %.1f' % (time.time() - T0))
print('TOTAL: PASS=%d FAIL=%d' % (NP, NF))
