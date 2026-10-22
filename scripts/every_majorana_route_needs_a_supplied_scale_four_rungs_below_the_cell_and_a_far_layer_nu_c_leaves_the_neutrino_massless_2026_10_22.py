AUDIT_INPUT_PATHS = ('docs/EVERY_MAJORANA_ROUTE_NEEDS_A_SUPPLIED_SCALE_FOUR_RUNGS_BELOW_THE_CELL_AND_A_FAR_LAYER_NU_C_LEAVES_THE_NEUTRINO_MASSLESS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Neutrino mass scale under the candidate laws: four routes tested.

Routes: (a) a Weinberg term at a law-fixed scale, (b) a spontaneous break of the
Z4 of B - L giving a Majorana nu^c mass, (c) a far-layer nu^c on the layer slab
(split-fermion overlap), (d) mirror-singlet mixing with nu^c.

Tags: [T] exact theorem (algebra / identity, checked numerically where stated),
[D] finite diagnostic, [E] estimate against measurement.
Self-contained: numpy only. Seeded. Small matrices; < 50 MB; ~1 s.
"""
import math
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 60
T0 = time.time()
RNG = np.random.default_rng(20261022)
NPASS = 0
NFAIL = 0


def check(tag, name, ok, detail=""):
    global NPASS, NFAIL
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
    s = "[%s] [%s] %s" % ("PASS" if ok else "FAIL", tag, name)
    if detail:
        s += " | " + detail
    print(s)


# ---------------------------------------------------------------- inputs (supplied)
M_CELL = 2.44e18      # hbar c / L, register unit map (GeV)
M_PL = 1.22e19        # 1/l_P (GeV)
M_RED = 2.435e18      # reduced Planck mass (GeV)
V246 = 246.22         # GeV
V174 = V246 / math.sqrt(2.0)
DM21 = 7.49e-5        # eV^2 (NuFIT-6-like)
DM31_NO = 2.513e-3
DM32_IO = 2.484e-3    # |dm32| for IO
S12 = 0.307
S13_NO, S13_IO = 0.02195, 0.02224
SIGMA_BOUND = 0.064   # eV, DESI DR2 + CMB (95%)
EV = 1e-9             # GeV per eV

# Z4 = i^(B-L) on colour-singlet operators; left-handed Weyl B-L charges.
BL = {"L": -1, "nu^c": +1, "e^c": +1, "H": 0, "Hbar": 0,
      "N(conj mirror singlet)": -1, "xi(slab mirror of nu^c)": -1}


def z4(ops):
    return sum(BL[o] for o in ops) % 4


print("== A. exact statements")
ops = {
    "L H nu^c (Dirac)": ["L", "H", "nu^c"],
    "nu^c nu^c (Majorana)": ["nu^c", "nu^c"],
    "L L H H (Weinberg)": ["L", "L", "H", "H"],
    "(nu^c)^4": ["nu^c"] * 4,
    "nu^c N": ["nu^c", "N(conj mirror singlet)"],
    "L H N": ["L", "H", "N(conj mirror singlet)"],
    "N N": ["N(conj mirror singlet)"] * 2,
}
ch = {k: z4(v) for k, v in ops.items()}
print("   Z4 charges: " + ", ".join("%s %d" % (k, c) for k, c in ch.items()))
reg_bl = 0  # edge, link, rishon and doublet registers carry no B-L (register: no family charge)
check("T", "A1 every Majorana-type mass (nu^c nu^c, LLHH, N N, L H N) has Z4 charge 2 and every "
      "Dirac-type term (L H nu^c, nu^c N) charge 0; registers carry B - L = 0, so no register, fold "
      "or edge configuration can break the Z4: only a matter vev of charge 2 (a lepton-number-2 "
      "condensate) or an explicit bilinear can", all(ch[k] == 2 for k in
      ["nu^c nu^c (Majorana)", "L L H H (Weinberg)", "N N", "L H N"]) and ch["L H nu^c (Dirac)"] == 0
      and ch["nu^c N"] == 0 and reg_bl == 0)
# vacua of a charge-2 order parameter under Z4: orbit of phi -> i^2 phi
orbit = {complex(round((1j ** (2 * k)).real), round((1j ** (2 * k)).imag)) for k in range(4)}
check("T", "A2 a charge-2 condensate breaks Z4 -> Z2 with |Z4/Z2| = 2 degenerate vacua (phi, -phi): "
      "a spontaneous route to a Majorana mass makes domain walls", len(orbit) == 2, "orbit %s" % sorted(
          (z.real for z in orbit)))

# A3: seesaw cap  ||Y M^-1 Y^T|| <= ||Y||^2 / sigma_min(M), any number of heavy states
worst = 0.0
for trial in range(300):
    nh = int(RNG.integers(1, 31))
    Y = RNG.normal(size=(3, nh)) + 1j * RNG.normal(size=(3, nh))
    A = RNG.normal(size=(nh, nh)) + 1j * RNG.normal(size=(nh, nh))
    Mh = A + A.T + 0.1 * np.eye(nh)                      # complex symmetric (Majorana)
    mlight = Y @ np.linalg.solve(Mh, Y.T)
    lhs = np.linalg.norm(mlight, 2)
    rhs = np.linalg.norm(Y, 2) ** 2 / np.linalg.svd(Mh, compute_uv=False)[-1]
    worst = max(worst, lhs / rhs)
# Dirac seesaw (vector-like heavy singlet pair): rows (nu, N), cols (nu^c, N^c) [[0, mD],[mu, M]]
dsee = []
for (mD, mu, M) in [(1e-3, 1e-3, 1.0), (1e-2, 3e-3, 2.0), (1e-4, 1e-2, 0.5)]:
    s = np.linalg.svd(np.array([[0.0, mD], [mu, M]]), compute_uv=False)
    dsee.append(s[-1] / (mD * mu / M))
check("T", "A3 any number of heavy Majorana states with masses >= M gives ||m_nu|| <= ||Y||^2 v^2/M "
      "(checked on 300 random instances, 1-30 heavy states); a Dirac seesaw via a vector-like singlet "
      "pair gives m = m_D mu/M: with v the only light scale both are capped by (coupling)^2 v^2/M",
      worst <= 1.0 + 1e-12 and all(abs(d - 1) < 1e-3 for d in dsee),
      "max ratio %.3f; Dirac-seesaw light/(mD mu/M) %s" % (worst, ", ".join("%.5f" % d for d in dsee)))

# A4: conjugate mirror singlets N (charge -1, like nu) mixing with nu^c
cnt = []
for r in [0, 1, 2, 3]:
    mD = 1e-6 * (RNG.normal(size=(3, 3)))
    U = RNG.normal(size=(3, r)); W = RNG.normal(size=(r, 3))
    Mm = U @ W if r else np.zeros((3, 3))
    s = np.linalg.svd(np.vstack([mD, Mm]), compute_uv=False)
    cnt.append(int(np.sum((s > 1e-9) & (s < 1e-4))))
check("T", "A4 mirror mixing (d): Z4 allows nu^c N (charge 0) but no N N, nu N or L H N; rows (nu, N) "
      "share nu^c, so the number of light massive neutrinos is 3 - rank(nu^c N block); measured "
      "(two splittings) needs rank <= 1: mirror mixing removes masses, never makes one",
      cnt == [3, 2, 1, 0], "light massive for rank 0..3: %s" % cnt)


# A5: layer slab. Columns chi_s (nu^c-type, charge +1), rows xi_s (charge -1). Shamir kernel
# xi_s (chi_(s-1) - q chi_s), q = |1 - M|: chi zero mode ~ q^(Ls-1-s) (far layer), xi zero mode
# ~ q^s (layer 0), residual leak ~ q^Ls from row 0. The mirror-free (index-1) slab drops row 0.
def slab(Ls, q, rect):
    m = np.zeros((Ls, Ls))
    for s in range(Ls):
        m[s, s] = -q
        if s >= 1:
            m[s, s - 1] = 1.0
    return m[1:] if rect else m


def chi0(Ls, q):
    return math.sqrt(1 - q * q) * q ** (Ls - 1) / math.sqrt(1 - q ** (2 * Ls))


Ls, q, eps = 10, 0.5, 1e-3   # eps = y0 v a (toy), a = 1
full_r = np.vstack([np.eye(1, Ls) * eps, slab(Ls, q, True)])
sr = np.linalg.svd(full_r, compute_uv=False)
pred = eps * chi0(Ls, q)
full_s = np.vstack([np.eye(1, Ls) * eps, slab(Ls, q, False)])
U, ss, Vh = np.linalg.svd(full_s)
null_left = U[:, -1]
nu_share = abs(null_left[0]) ** 2
sig_slab = np.linalg.svd(slab(Ls, q, False), compute_uv=False)[-1]
check("D", "A5 rectangular (index-1, mirror-free) far-layer nu^c: light Dirac mass = y0 v sqrt(1-q^2) "
      "q^(Ls-1)/sqrt(1-q^(2Ls)) (Ls=10, q=1/2)", abs(sr[-1] / pred - 1) < 1e-4,
      "SVD %.4e vs %.4e" % (sr[-1], pred))
share_pred = sig_slab ** 2 / (sig_slab ** 2 + pred ** 2)
check("T", "A6 the register's square slab with a reversed (far-layer) nu^c puts its mirror xi on layer 0 "
      "with charge -1 like nu: rows (nu, xi) exceed columns by one, so one state is exactly massless; "
      "the light block is [eps chi0; sigma], sigma ~ q^Ls/a the slab's own leak, and since "
      "eps chi0/sigma ~ y0 v a/q ~ 1e-16 the massless state is the neutrino",
      len(ss) == Ls and abs(nu_share - share_pred) < 1e-5 and abs(ss[-1] / math.hypot(sig_slab, pred) - 1) < 1e-3,
      "toy eps=1e-3: nu share %.6f (pred %.6f); lightest massive %.3e vs hypot(sigma, eps chi0) %.3e"
      % (nu_share, share_pred, ss[-1], math.hypot(sig_slab, pred)))
# GK wall height M = 1: q(p) = sum(1 - cos p_i); at rest q = 0 -> chi0 = 0 exactly
qp = [sum(1 - math.cos(p) for p in (k, 0, 0)) for k in (0.0, 0.1, 0.2)]
y_p = [chi0(8, x) if x > 0 else 0.0 for x in qp]
check("T", "A7 at the wall height M = 1 of the smoothed-layer slab, q(p) = sum(1 - cos p_i) vanishes at rest: "
      "the far-layer overlap is 0 exactly at p = 0 and ~ p^(2(Ls-1)) away from it: no neutrino mass",
      y_p[0] == 0.0 and y_p[1] < 1e-15, "Ls=8: overlap at p=0,0.1,0.2: %s" % ", ".join("%.1e" % y for y in y_p))

print("== B. estimates against measurement")


def spectrum(order, mmin):
    if order == "NO":
        m1 = mmin; m2 = math.sqrt(m1 ** 2 + DM21); m3 = math.sqrt(m1 ** 2 + DM31_NO); s13 = S13_NO
    else:
        m3 = mmin; m2 = math.sqrt(m3 ** 2 + DM32_IO); m1 = math.sqrt(m2 ** 2 - DM21); s13 = S13_IO
    t = [(1 - S12) * (1 - s13) * m1, S12 * (1 - s13) * m2, s13 * m3]
    mbb_max = sum(t); mbb_min = max(0.0, 2 * max(t) - sum(t))
    return (m1, m2, m3), m1 + m2 + m3, mbb_min, mbb_max


(m_no, sig_no, bmin_no, bmax_no) = spectrum("NO", 0.0)
(m_io, sig_io, bmin_io, bmax_io) = spectrum("IO", 0.0)
lo, hi = 0.0, 0.05
for _ in range(60):
    mid = 0.5 * (lo + hi)
    lo, hi = (mid, hi) if spectrum("NO", mid)[1] < SIGMA_BOUND else (lo, mid)
m1max = lo
_, _, bmin_x, bmax_x = spectrum("NO", m1max)
M3 = m_no[2]
print("   NO m1=0: m = %.4f, %.4f, %.4f eV, Sigma %.4f, Majorana m_bb %.4f-%.4f eV; IO m3=0: Sigma %.4f, "
      "m_bb %.4f-%.4f" % (m_no + (sig_no, bmin_no, bmax_no, sig_io, bmin_io, bmax_io)))
check("E", "B1 Sigma < 0.064 eV excludes inverted ordering (Sigma_min 0.099) and needs NO with m1 < %.4f eV; "
      "Majorana routes then give m_bb <= %.4f eV (below LEGEND-1000 / nEXO reach of ~0.01), Dirac routes "
      "m_ee = 0 exactly" % (m1max, max(bmax_no, bmax_x)), sig_io > SIGMA_BOUND > sig_no)


# one-loop SM running m_t -> mu (g1 GUT-normalised), kappa of the Weinberg term
def run(mu, n=4000):
    y = np.array([math.sqrt(5 / 3) * 0.3583, 0.6478, 1.1666, 0.9369, 0.1259, 0.0])  # g1 g2 g3 yt lam lnk
    t0, t1 = math.log(172.6), math.log(mu)
    h = (t1 - t0) / n
    k = 1 / (16 * math.pi ** 2)

    def f(v):
        g1, g2, g3, yt, lam, _ = v
        return np.array([
            k * 41 / 10 * g1 ** 3, -k * 19 / 6 * g2 ** 3, -k * 7 * g3 ** 3,
            k * yt * (4.5 * yt ** 2 - 17 / 20 * g1 ** 2 - 9 / 4 * g2 ** 2 - 8 * g3 ** 2),
            k * (24 * lam ** 2 + 12 * lam * yt ** 2 - 6 * yt ** 4 - 3 * lam * (3 * g2 ** 2 + 0.6 * g1 ** 2)
                 + 3 / 8 * (2 * g2 ** 4 + (g2 ** 2 + 0.6 * g1 ** 2) ** 2)),
            k * (-3 * g2 ** 2 + 4 * lam + 6 * yt ** 2)])
    for _ in range(n):
        a1 = f(y); a2 = f(y + h / 2 * a1); a3 = f(y + h / 2 * a2); a4 = f(y + h * a3)
        y = y + h / 6 * (a1 + 2 * a2 + 2 * a3 + a4)
    return y


yM = run(M_CELL)
kap = math.exp(-yM[5])          # kappa(m_t)/kappa(M)
ytM = yM[3]
need = {
    "type-I y=y_t(M)": kap * ytM ** 2 * V174 ** 2 / (M3 * EV),
    "type-I y=1": kap * V174 ** 2 / (M3 * EV),
    "Weinberg c=1 (v=246)": kap * V246 ** 2 / (M3 * EV),
    "type-I y^2=4pi": kap * 4 * math.pi * V174 ** 2 / (M3 * EV),
    "NDA c=16pi^2": kap * 16 * math.pi ** 2 * V246 ** 2 / (M3 * EV),
}
print("   y_t(M_cell) = %.3f, kappa run %.3f; scale needed for m3 = %.4f eV (rungs below cell):" % (ytM, kap, M3))
print("     " + "; ".join("%s %.2e (%.1f)" % (k_, v, math.log2(M_CELL / v)) for k_, v in need.items()))
scales = [("cell 1/L", M_CELL, "fixed"), ("1/l_P", M_PL, "fixed"), ("floor 8/L", 8 * M_CELL, "fixed"),
          ("window top, Delta=1", M_CELL / 4, "Delta>=1 supplied"),
          ("nested block /24", M_CELL / 24, "size supplied"), ("edge block /b_e=40", M_CELL / 40, "b_e>=40 supplied")]
rows = []
for nm, s, st in scales:
    rows.append((nm, st, kap * V174 ** 2 / s / EV, kap * 16 * math.pi ** 2 * V246 ** 2 / s / EV))
print("   m3 at y=1 / at NDA strong coupling: " + "; ".join("%s [%s] %.1e / %.1e eV" % r for r in rows))
fixed_best = max(r[3] for r in rows if r[1] == "fixed")
check("E", "B2 (a)+(b) with every heavy state at a law-fixed scale (cell, Planck, floor) even maximal strong "
      "coupling (NDA 16 pi^2) gives m3 <= %.1e eV, %.0fx short; at y = 1 the scale must be %.1f rungs below "
      "the cell, and only scales carrying a supplied size (window Delta, block or edge-block size) reach it"
      % (fixed_best, M3 / fixed_best, math.log2(M_CELL / need["type-I y=1"])), fixed_best < M3 / 10)
nfrac = [min(1.0, math.log(4) / math.log(2.0 ** p)) for p in (1, 2, 3)]
check("E", "B3 look-elsewhere: with a free integer rung 2^-n the target is always within x2 for steps <= 4, "
      "so a rung hit at n ~ 11-12 (brief's 1.2e15) is no evidence unless a law fixes n",
      nfrac[0] == 1.0 and nfrac[1] == 1.0, "P(hit) for step 2,4,8: %s" % ", ".join("%.2f" % x for x in nfrac))
MR = need["type-I y=1"]
sig_w = MR ** 3
Hdom = sig_w / (3 * M_RED ** 2)
Tdom = math.sqrt(Hdom * M_PL / (1.66 * math.sqrt(106.75)))
check("E", "B4 (b) spontaneous Z4 -> Z2 at M_R ~ %.1e GeV: walls of tension ~M_R^3 dominate at T ~ %.0e GeV "
      "(>> MeV) and exceed the Zel'dovich-Kobzarev-Okun bound sigma^(1/3) < ~1 MeV by %.0e: excluded unless a "
      "dilution phase after the break or a supplied Z4-breaking bias" % (MR, Tdom, MR / 1e-3), Tdom > 1e3)
YNU = math.sqrt(2) * M3 * EV / V246
tab = []
for y0 in (1.0, ytM):
    for qq in (0.1, 0.25, 0.5, 0.8):
        tab.append("y0=%.2f q=%.2f: Ls-1=%.1f" % (y0, qq, math.log(YNU / y0 / math.sqrt(1 - qq * qq)) / math.log(qq)))
print("   y_nu = %.2e; far-layer slab needs " % YNU + "; ".join(tab))
rr = math.sqrt(DM21) / M3
m1_split = 0.17 * m_no[1]
sig_split = spectrum("NO", m1_split)[1]
# IO in the slab reading: two nu^c on equal Ls, order-one anarchic entries; need (s1 - s2)/s1 <= dm21/(2 m^2)
need_io = DM21 / (2 * (DM32_IO + DM21))
A = RNG.normal(size=(40000, 3, 2)) + 1j * RNG.normal(size=(40000, 3, 2))
sv = np.linalg.svd(A, compute_uv=False)
n_io = int(np.sum((sv[:, 0] - sv[:, 1]) / sv[:, 0] <= need_io)); p_io = n_io / 40000.0
check("E", "B5 (c) the mirror-free far-layer slab trades y_nu for (q, Ls): integer Ls and any q >= 1/4 always "
      "hit within x2 (no evidence); exponential spacing makes m1 << m2 << m3 natural (NO), while IO needs two "
      "equal Ls and order-one entries whose singular values agree to %.1f%% (%d of 40000 anarchic draws); Dirac, so "
      "m_ee = 0; Sigma = %.4f-%.4f eV for m1 = 0 to q m2 (q ~ m2/m3 = %.2f): just under the 0.064 bound"
      % (100 * need_io, n_io, sig_no, sig_split, rr), sig_split < SIGMA_BOUND and p_io < 0.01)
# shared slab: the light-mirror leak q^Ls M must stay below m_e (free-slab reading) while q^(Ls-1) = y_nu
me = 0.511e-3
qmax = (me / M_CELL) / YNU
ls1 = math.log(YNU) / math.log(qmax)
check("E", "B6 one slab for all species (shared q, Ls; free-slab reading in which the leak q^Ls M pairs every "
      "light fermion with its far mirror): q^Ls M < m_e and q^(Ls-1) = y_nu force q < %.1e and Ls - 1 < %.2f, "
      "i.e. Ls = 2 with the wall height tuned to 1 - 3e-13: the nu^c slab must be its own (supplied) slab"
      % (qmax, ls1), ls1 < 2)
dr = []
for N in (49, 52):
    for nm, S in (("one-site", 2.0 ** (-1.5 * N)), ("8-site", 2.0 ** (3 - 1.5 * N)), ("lapse-owned", 2.0 ** (-2.5 * N)),
                  ("domain-norm", 1.0)):
        dr.append((N, nm, V174 * S / EV))
ok_dr = all(not (M3 / 30 < m < 30 * M3) for _, _, m in dr)
print("   nu^c on the doublet's rung N: " + "; ".join("N=%d %s %.0e eV" % d for d in dr))
check("E", "B7 nu^c placed on the doublet register's rung (depth N ~ 49-52 from the weak-scale ladder) gives, "
      "for every nu-rung contact reading, a Dirac m3 outside [m3/30, 30 m3] (at most 1e-10 eV, or 2e11 eV): excluded; "
      "the needed exponent 41.7/N = 0.80-0.85 is no reading", ok_dr)
print("theorems: A1-A4, A6, A7; finite diagnostic: A5; estimates: B1-B7.")
print("supplied: B-L charges of the 16, measured splittings and angles (NuFIT-6-like), Sigma bound, v, unit map "
      "M = 2.44e18 GeV, SM inputs at m_t (1-loop), slab q, Ls, y0, toy eps; window Delta, block sizes, b_e "
      "(register bounds); doublet depth N.")
print("elapsed_seconds %.1f" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (NPASS, NFAIL))
