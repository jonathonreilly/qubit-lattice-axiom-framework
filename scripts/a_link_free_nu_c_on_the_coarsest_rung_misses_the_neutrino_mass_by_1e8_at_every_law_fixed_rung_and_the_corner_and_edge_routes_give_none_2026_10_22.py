AUDIT_INPUT_PATHS = ('docs/A_LINK_FREE_NU_C_ON_THE_COARSEST_RUNG_MISSES_THE_NEUTRINO_MASS_BY_1E8_AT_EVERY_LAW_FIXED_RUNG_AND_THE_CORNER_AND_EDGE_ROUTES_GIVE_NONE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Neutrino mass rule, second pass: three routes for a Dirac m_nu without a fit.

(a) nu^c, the only link-free mode, read on the coarsest rung available
    (edge block b_e, window top, horizon); Dirac Yukawa suppressed by the
    nested-overlap theorem 2^(-3n/2) (and the contact-reading variants);
(b) the light-mirror corner pairing as a Dirac seesaw through the mirror;
(c) an edge-register (gravity) mediated Dirac mass.
Tags: [T] exact theorem (checked numerically), [D] finite diagnostic,
[E] estimate against measurement. numpy only, seeded, < 50 MB, a few s.
"""
import math
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 60
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = 0
NF = 0


def check(tag, name, ok, detail=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    s = "[%s] [%s] %s" % ("PASS" if ok else "FAIL", tag, name)
    if detail:
        s += " | " + detail
    print(s)


# measured / supplied inputs (eV unless stated)
V = 246.22e9                 # Higgs vev
VD = V / math.sqrt(2.0)      # y v/sqrt2 normalisation of a Dirac mass
DM31, DM21 = 2.51e-3, 7.49e-5
M3, M2 = math.sqrt(DM31), math.sqrt(DM21)
SIGMA_MAX = 0.064
MCELL = 2.44e27              # hbar c / L in eV (L = sqrt(8 pi) l_P)
LCELL = 8.10e-35             # m
H0 = 67.4e3 / 3.0857e22      # 1/s
RH = 2.998e8 / H0            # m
Y3 = M3 / VD                 # needed Dirac Yukawa, m1 -> 0
L2Y = -math.log2(Y3)

print("== A. exact structure")
# A1 nested block-uniform overlap
N = 16
ok = True
worst = 0.0
for a in range(5):
    for b in range(5):
        ua = np.zeros((N, N, N)); sa = 2 ** a
        ua[:sa, :sa, :sa] = 1.0; ua /= np.linalg.norm(ua)
        ub = np.zeros((N, N, N)); sb = 2 ** b
        ub[:sb, :sb, :sb] = 1.0; ub /= np.linalg.norm(ub)
        worst = max(worst, abs(np.sum(ua * ub) - 2.0 ** (-1.5 * abs(a - b))))
check("T", "A1 nested block-uniform readings on rungs a, b overlap by 2^(-3|a-b|/2) (16^3, rungs 0-4)",
      worst < 1e-14, "max dev %.1e" % worst)

# A2 contact readings: share of a coarse-site contact vector in the fine light (k = 0) band
Nf = 8
rows = []
for n in (1, 2):
    bs = 2 ** n
    nc = (Nf // bs) ** 3
    one = np.zeros((Nf, Nf, Nf)); one[::bs, ::bs, ::bs] = 1.0          # one contact per coarse site
    allc = np.ones((Nf, Nf, Nf))                                      # every fine site, weight 1
    dom = allc / bs ** 1.5                                            # domain-normalised
    out = []
    for c in (one, allc, dom):
        # coarse uniform mode coupling to the fine k = 0 mode, per unit y v:
        out.append(np.sum(c) / math.sqrt(Nf ** 3 * nc))
    F = np.fft.fftn(one) / math.sqrt(Nf ** 3)
    folded = np.abs(F[::Nf // bs, ::Nf // bs, ::Nf // bs]) ** 2 / nc  # share per folded fine momentum
    rows.append((n, out, folded.sum(), folded.size))
okA2 = all(abs(o[0] - 2 ** (-1.5 * n)) < 1e-12 and abs(o[1] - 2 ** (1.5 * n)) < 1e-12
           and abs(o[2] - 1) < 1e-12 and abs(s - 1) < 1e-12 for n, o, s, _ in rows)
check("T", "A2 the k = 0 Dirac coupling of a coarse nu^c is 2^(-3n/2) (one contact per coarse site), "
      "2^(+3n/2) (every fine site) or 1 (domain-normalised): the overlap theorem gives suppression only "
      "under the one-contact reading; that contact's weight spreads evenly over the 2^(3n) folded fine "
      "momenta (shares sum to 1), the rest pairs with heavy fine bands", okA2,
      "; ".join("n=%d: %.4f/%.3f/%.3f, sum %.3f over %d" % (n, o[0], o[1], o[2], s, k) for n, o, s, k in rows))

# A3 (b) Dirac seesaw through a mirror pair: det identity and corner form factor
ok = True
worst = 0.0
for _ in range(200):
    yv, mu, D = RNG.uniform(0.01, 1), RNG.uniform(0, 1), RNG.uniform(5, 50)
    Mm = np.array([[0.0, yv], [mu, D]])
    s = np.linalg.svd(Mm, compute_uv=False)
    worst = max(worst, abs(s[0] * s[1] - yv * mu) / (yv * mu + 1e-300))
check("T", "A3 one family, no light Yukawa: rows (nu, N), columns (nu^c, N^c), [[0, y v], [mu, Delta]]: "
      "m_light * m_heavy = y v mu exactly, so m_light = y v mu/Delta (1 + O(.)) (200 random)",
      worst < 1e-12, "max rel dev %.1e" % worst)
worst3 = 0.0
for _ in range(100):
    Y = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    MU = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    Dl = 1e4
    big = np.block([[np.zeros((3, 3)), Y], [MU, Dl * np.eye(3)]])
    s = np.sort(np.linalg.svd(big, compute_uv=False))[:3]
    p = np.sort(np.linalg.svd(Y @ MU / Dl, compute_uv=False))
    worst3 = max(worst3, np.max(np.abs(s - p) / p))
check("T", "A4 three families: light Dirac masses = singular values of Y mu/Delta to O((mu/Delta)^2) "
      "(100 random, Delta = 1e4)", worst3 < 1e-3, "max rel dev %.1e" % worst3)


def fK(k):  # corner form factor stand-in: 0 at K = 0, 1 at R = pi(1,1,1)
    return np.sum(1 - np.cos(k)) / 6.0


ms = []
for kk in (0.0, 1e-3, 2e-3, 4e-3):
    k = np.array([kk, kk, kk])
    Mm = np.array([[0.0, 1.0], [0.3 * fK(k), 10.0]])
    ms.append(np.linalg.svd(Mm, compute_uv=False)[-1])
R = np.pi * np.ones(3)
mR = np.linalg.svd(np.array([[0.0, 1.0], [0.3 * fK(R), 10.0]]), compute_uv=False)[-1]
check("T", "A5 a corner-only light-mirror pairing mu(K) = lam f(K), f(0) = 0: crystal momentum is "
      "conserved, so the K = 0 Dirac mass is exactly 0 and grows as k^2 (no rest mass); full size at R",
      ms[0] < 1e-15 and abs(ms[2] / ms[1] - 4) < 1e-3 and abs(ms[3] / ms[2] - 4) < 1e-3,
      "m(0) = %.1e, m(2k)/m(k) = %.4f, %.4f, m(R) = %.3f" % (ms[0], ms[2] / ms[1], ms[3] / ms[2], mR))

# A6 (c) edge-register toy: edges conserve nu^c number, dressing is flavour-blind
de = 64
A = RNG.normal(size=(de, de)) + 1j * RNG.normal(size=(de, de)); He = (A + A.conj().T) / 2
B1 = RNG.normal(size=(de, de)) + 1j * RNG.normal(size=(de, de)); G1 = (B1 + B1.conj().T) / 2
B2 = RNG.normal(size=(de, de)) + 1j * RNG.normal(size=(de, de)); G2 = (B2 + B2.conj().T) / 2
Fd = np.diag(1 + 0.3 * RNG.uniform(-1, 1, de))      # edge-dependent hop dressing
Fd = (Fd + RNG.normal(size=(de, de)) * 0.01); Fd = (Fd + Fd.T) / 2
Pnu = np.diag([1.0, 0.0]); Pc = np.diag([0.0, 1.0]); X = np.array([[0.0, 1.0], [1.0, 0.0]])


def Htot(y):
    return (np.kron(np.eye(2), He) + 0.2 * np.kron(Pnu, G1) + 0.2 * np.kron(Pc, G2)
            + y * np.kron(X, Fd))


w, U = np.linalg.eigh(Htot(0.0))
Ut = U @ np.diag(np.exp(-1j * w * 3.7)) @ U.conj().T
leak = np.linalg.norm(Ut[:de, de:])
we, Ue = np.linalg.eigh(He)
g = Ue[:, 0]
splits = []
for y in (1e-4, 2e-4):
    # effective nu-nu^c coupling in the edge ground state, first order
    splits.append(abs(g.conj() @ (y * Fd) @ g))
check("T", "A6 edge registers carry no Y or B - L and here conserve nu^c number: with y_nu = 0 the "
      "edge-coupled evolution never mixes nu and nu^c (exact); with y_nu != 0 the induced coupling "
      "is y_nu <F> with F the flavour-blind edge dressing (linear in y_nu)",
      leak < 1e-12 and abs(splits[1] / splits[0] - 2) < 1e-12,
      "leak %.1e, ratio %.6f, <F> = %.3f" % (leak, splits[1] / splits[0], splits[0] / 1e-4))

print("== B. estimates against measurement")
print("   needed Dirac Yukawa y3 = sqrt2 m3/v = %.3e = 2^-%.2f (m1 -> 0, normal ordering)" % (Y3, L2Y))
readings = [("one-contact p=3/2", 1.5, 0.0), ("covariant 8-site p=3/2", 1.5, 3.0),
            ("coarse-update p=5/2", 2.5, 0.0)]
need = {}
for nm, p, pre in readings:
    need[nm] = (L2Y + pre) / p
print("   needed rung n (y0 = 1): " + "; ".join("%s: n=%.2f, b_e=2^n=%.2e" % (k, v, 2 ** v)
                                             for k, v in need.items()))
cands = [("b_e = 32 (budget, s1=0.4)", math.log2(32)), ("b_e = 40", math.log2(40)),
         ("b_e = 45 (budget, s1=0.2)", math.log2(45)), ("floor-to-split 16", 4.0),
         ("window 4+Delta, Delta=1", 5.0), ("horizon c/H0 over L", math.log2(RH / LCELL))]
worst_ratio = 1e300
for nm, n in cands:
    ms_ = []
    for _, p, pre in readings:
        ms_.append(VD * 2 ** (pre - p * n))
    worst_ratio = min(worst_ratio, min(abs(math.log10(m / M3)) for m in ms_))
    print("   %-26s n=%6.2f: m3 = %s eV" % (nm, n, ", ".join("%.1e" % m for m in ms_)))
check("E", "B1 every law-available coarsest rung misses m3 by >= 1e8: b_e at its budget floor 32-45, "
      "the floor-to-split ratio and the window top (Delta = 1) give MeV-GeV Dirac masses (excluded by "
      "KATRIN 0.45 eV and Sigma); the horizon (n ~ 200) gives < 1e-70 eV (excluded by two splittings)",
      worst_ratio > 8, "closest miss 10^%.1f" % worst_ratio)
Dneed = {k: v - 4 for k, v in need.items()}
check("E", "B2 fitting the rung: b_e = 2.3e8 (p=3/2), 9.3e8 (8-site), 1.1e5 (p=5/2), or Delta = 23.8 / "
      "25.8 / 12.7; b_e and Delta are bounded only below, so these are allowed but FITTED",
      all(v > 5.5 for v in need.values()),
      ", ".join("Delta=%.1f" % v for v in Dneed.values()))
p_hit = []
for p in (1.5, 2.5):
    xs = RNG.uniform(0, 1, 20000) * p  # fractional part of the exponent, phase-uniform
    p_hit.append(np.mean(np.minimum(xs, p - xs) <= 1.0))
check("E", "B3 look-elsewhere: with an integer rung the target lies within x2 with P = 1 (p=3/2) and "
      "0.80 (p=5/2), and b_e is continuous: a hit carries no evidence",
      p_hit[0] > 0.99 and abs(p_hit[1] - 0.8) < 0.02, "P = %.3f, %.3f" % tuple(p_hit))

# B4 one coarsest rung for all three nu^c: anarchic O(1) Yukawa matrix, one fitted overall scale
Ns = 200000
Yr = RNG.normal(size=(Ns, 3, 3)) + 1j * RNG.normal(size=(Ns, 3, 3))
sv = np.sort(np.linalg.svd(Yr, compute_uv=False), axis=1)
s1, s2, s3 = sv[:, 0], sv[:, 1], sv[:, 2]
r_meas = DM21 / DM31
rNO = (s2 ** 2 - s1 ** 2) / (s3 ** 2 - s1 ** 2)
rIO = (s3 ** 2 - s2 ** 2) / (s2 ** 2 - s1 ** 2)
sc = np.sqrt(DM31 / (s3 ** 2 - s1 ** 2))
SigNO = sc * (s1 + s2 + s3)
okw = (rNO > r_meas / 1.5) & (rNO < r_meas * 1.5)
pNO = np.mean(okw)
pNOS = np.mean(okw & (SigNO < SIGMA_MAX))
pIO = np.mean((rIO > r_meas / 1.5) & (rIO < r_meas * 1.5))
medS = np.median(SigNO[okw]) if okw.any() else float("nan")
m1med = np.median((sc * s1)[okw])
check("E", "B4 one rung for all three nu^c (the rule's 'coarsest rung'): masses = scale x singular values "
      "of an O(1) matrix; r within x1.5 in %.2f%% (normal) vs %.3f%% (inverted-type); with Sigma < 0.064 "
      "%.2f%% (P(Sigma ok | r ok) = %.0f%%); conditional median Sigma %.3f eV, m1 %.4f eV: the one-rung rule fixes no ratio"
      % (100 * pNO, 100 * pIO, 100 * pNOS, 100 * pNOS / pNO, medS, m1med), pNOS < 0.05 and pNO > pIO)

# B5 routes (b) and (c)
mu_need = Y3
m_v2M = VD * (V / MCELL)
curv = (H0 * LCELL / 2.998e8) ** 2
check("E", "B5 (b) the mirror seesaw needs mu/Delta = %.1e (y = 1): a cell-local mu and Delta give O(1), a "
      "corner-only mu gives 0 at rest (A5), a singlet mu cannot carry v (hypercharge), and mu ~ v^2/M gives "
      "%.1e eV; (c) edge dressing is universal and departs from the vacuum by (H0 L)^2 = %.1e today: no "
      "neutrino-specific suppression" % (mu_need, m_v2M * 1.0, curv),
      m_v2M < M3 / 100 and curv < 1e-100)
print("   Dirac routes: m_ee = 0 exactly (Z4); normal ordering at m1 = 0: m = (0, %.4f, %.4f) eV, "
      "Sigma = %.4f eV, m_beta ~ %.4f eV" % (M2, M3, M2 + M3,
                                              math.sqrt(0.307 * (1 - 0.022) * M2 ** 2 + 0.022 * M3 ** 2)))
print("GATE: (a) b_e/Delta/integer n FITTED -> FAIL (1); parameter-free readings EXCLUDED (B1);"
      " (b) FAIL (supplied mu/Delta, or m = 0 at rest); (c) FAIL (universal, no suppression).")
print("supplied: contact reading (p, which sites), y0 ~ 1, b_e/Delta/rung, mu, Delta, form factor;"
      " measured: splittings, Sigma bound, v, H0, hbar c/L.")
print("elapsed_seconds %.1f" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (NP, NF))
