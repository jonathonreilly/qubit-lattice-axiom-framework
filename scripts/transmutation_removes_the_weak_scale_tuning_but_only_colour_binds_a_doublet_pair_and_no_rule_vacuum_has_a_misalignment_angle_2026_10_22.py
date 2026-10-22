AUDIT_INPUT_PATHS = ('docs/TRANSMUTATION_REMOVES_THE_WEAK_SCALE_TUNING_BUT_ONLY_COLOUR_BINDS_A_DOUBLET_PAIR_AND_NO_RULE_VACUUM_HAS_A_MISALIGNMENT_ANGLE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Weak scale: generated, not tuned? (finite runner, seeded).

Sections:
  A  dynamical breaking: exact beta coefficients from content, the doublet
     channels and their binders, transmutation algebra, rung count from the
     plaquette-count readings, colour and top-condensation estimates
  B  the scalar as a neighbourhood composite: centre charge of link/edge/rishon
     registers, lattice gap equation + RPA (Goldstone at 0, scalar at 2m),
     Pagels-Stokar arithmetic for a 125 GeV bubble scalar
  C  protection: no misalignment angle for colour-singlet bilinear vacua,
     pair-square 10 Goldstones, the pseudoreal contrast, vacuum subtraction
Measured numbers enter only [E]/[M] items; supplied inputs are named at the end.
"""
import time
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import brentq

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text} | {vals}")


PI = np.pi
LN2 = np.log(2.0)
M_CELL = 2.44e18          # hbar c / L, the register's cell rung (GeV)
V_EW, M_H, M_T, YT_MT = 246.22, 125.1, 172.6, 0.936
MZ, AS_MZ = 91.1876, 0.1180
F_PI, G2 = 0.0921, 0.6517
S_MEAS, S_ERR = -0.05, 0.07

# ---------------------------------------------------------------- A
print("== A. dynamical breaking (transmutation along the rungs)")
# one family of left-handed Weyl multiplets: (colour, dim SU2, Y)
FAM = {"q": ("3", 2, Fr(1, 6)), "u^c": ("3b", 1, Fr(-2, 3)), "d^c": ("3b", 1, Fr(1, 3)),
       "L": ("1", 2, Fr(-1, 2)), "e^c": ("1", 1, Fr(1)), "n^c": ("1", 1, Fr(0))}
CD = {"3": 3, "3b": 3, "1": 1}


def b_nonab(CA, weyl_T_count, cscalar_T_count=Fr(0)):
    return Fr(11, 3) * CA - Fr(2, 3) * weyl_T_count - Fr(1, 3) * cscalar_T_count


nfam = 3
b3 = b_nonab(3, Fr(1, 2) * nfam * sum(d for c, d, y in FAM.values() if c != "1"))
b2 = b_nonab(2, Fr(1, 2) * nfam * sum(CD[c] for c, d, y in FAM.values() if d == 2), Fr(1, 2))
sy2 = sum(CD[c] * d * y * y for c, d, y in FAM.values())
b1 = -Fr(3, 5) * (Fr(2, 3) * nfam * sy2 + Fr(1, 3) * 2 * Fr(1, 4))
bps = {n: (b_nonab(4, Fr(1, 2) * 4 * n), b_nonab(2, Fr(1, 2) * 4 * n)) for n in (1, 3)}
b_hc = b_nonab(2, Fr(1, 2) * 4)            # SU(2)=Sp(2) hypercolour, 4 Weyl doublets
ok = (b1, b2, b3) == (Fr(-41, 10), Fr(19, 6), Fr(7)) and bps[1] == (Fr(40, 3), Fr(6)) \
    and bps[3] == (Fr(32, 3), Fr(10, 3)) and b_hc == 6
check(ok, "A1 [T]", "one-loop coefficients from content (b > 0 asymptotically free): SM (U1 GUT-norm, SU2, SU3) = "
      f"({b1}, {b2}, {b3}); Pati-Salam (SU4, SU2_L) one family {bps[1][0]}, {bps[1][1]}, three families "
      f"{bps[3][0]}, {bps[3][1]}; an Sp(2) factor on 4 Weyl doublets {b_hc}", "exact Fractions")

# A2: bosonic Y = 1/2 doublet bilinears psi_i psi_j and which non-abelian factor holds both
chan = []
names = list(FAM)
for i, a in enumerate(names):
    for b in names[i:]:
        ca, da, ya = FAM[a]
        cb, db, yb = FAM[b]
        csing = {ca, cb} == {"3", "3b"} or (ca == cb == "1")
        dbl = (da, db) in ((2, 1), (1, 2))
        if csing and dbl and abs(ya + yb) == Fr(1, 2):
            binders = (["SU3"] if ca != "1" else []) + (["SU2_L"] if da == db == 2 else [])
            chan.append((a, b, binders))
ok = sorted((a, b) for a, b, _ in chan) == sorted([("q", "u^c"), ("q", "d^c"), ("L", "e^c"), ("L", "n^c")]) \
    and all(bd == (["SU3"] if a == "q" else []) for a, b, bd in chan)
check(ok, "A2 [T]", "colourless |Y| = 1/2 doublet pairs of one family: exactly q u^c, q d^c, L e^c, L n^c; the only "
      "non-abelian factor holding both members is colour (quark pairs); SU(2)_L never holds both (one member is a "
      "singlet); lepton pairs have no non-abelian binder", str([(a, b, bd) for a, b, bd in chan]))

# A3: transmutation: Lambda = M exp(-2pi/(b0 alpha)); d ln Lambda / d ln alpha = ln(M/Lambda)
n_need = np.log2(M_CELL / V_EW)
sens = np.log(M_CELL / V_EW)
db_fac2 = {k: float(b) * LN2 / (2 * PI) for k, b in (("PS3", bps[3][0]), ("HC", b_hc))}
xm = (V_EW / M_CELL) ** 2
d_njl = 0.5 * xm * (np.arcsinh(M_CELL / V_EW) - 0.5) / 0.5      # sphere |k| < M, delta = (I0-I)/I
check(np.isclose(sens, n_need * LN2) and d_njl < 1e-30, "A3 [T]",
      "one-loop transmutation: v/M = 2^-n with n = 2pi/(b0 alpha_cell ln2), and |d ln v / d ln alpha_cell| = n ln2 "
      "for any b0: a 1e-16 hierarchy costs sensitivity 37, not the four-mode route's 1/delta",
      f"v/M = {V_EW / M_CELL:.2e}, n = {n_need:.1f}, sensitivity {sens:.1f}; factor 2 in v <-> d(1/alpha_cell) = "
      f"{db_fac2['PS3']:.2f} (PS, 3 fam), {db_fac2['HC']:.2f} (Sp2); four-mode delta (sphere) {d_njl:.1e}")

# A4: the plaquette-count readings 1/alpha_cell = 4 pi kappa T fix n = 8 pi^2 kappa T/(b0 ln2)
kT = [0.5, 1, 2, 4, 8, 16]
rows, best = [], 1e9
for lab, b0 in (("PS3", float(bps[3][0])), ("PS1", float(bps[1][0])), ("Sp2", 6.0)):
    ns = [8 * PI ** 2 * k / (b0 * LN2) for k in kT]
    best = min(best, min(abs(x - n_need) for x in ns))
    rows.append(f"{lab}: " + ",".join(f"{x:.1f}" for x in ns))
check(best > 3, "A4 [T/E]", "with the per-mode count as the cell coupling the rung count is fixed by content "
      "(n = 8 pi^2 kappa T/(b0 ln2), exact), but the readings double n per step and none lands within 3 rungs of the "
      f"needed {n_need:.1f}; a hit would be look-elsewhere (3 groups x 6 readings, spacing x2)",
      "; ".join(rows) + f"; closest miss {best:.1f} rungs = x{2 ** best:.0e} in v")


# A5: colour route with measured alpha_s (one loop, thresholds)
def inv_as(mu):
    inv, m0, nf = 1 / AS_MZ, MZ, 5
    if mu >= MZ:
        for m, nn in ((M_T, 6),):
            if mu > m:
                inv += (11 - 2 * nf / 3) / (2 * PI) * np.log(m / m0)
                m0, nf = m, nn
        return inv + (11 - 2 * nf / 3) / (2 * PI) * np.log(mu / m0)
    for m, nn in ((4.18, 4), (1.27, 3)):
        if mu < m:
            inv += (11 - 2 * nf / 3) / (2 * PI) * np.log(m / m0)
            m0, nf = m, nn
    return inv + (11 - 2 * nf / 3) / (2 * PI) * np.log(mu / m0)


a_c = PI / (3 * 4 / 3)
mu_c = brentq(lambda lm: inv_as(np.exp(lm)) - 1 / a_c, np.log(0.05), np.log(MZ))
mu_c = np.exp(mu_c)
as_v = 1 / inv_as(V_EW)
mw_qcd = G2 * np.sqrt(3) * F_PI / 2
check(as_v < a_c / 5 and mw_qcd < 0.1, "A5 [E/M]", "colour (the only binder of a doublet pair) reaches the ladder "
      "critical alpha_c = pi/(3 C_F) only at the QCD scale; its own condensate breaks SU(2) x U(1) with v = sqrt(3) f_pi",
      f"alpha_c {a_c:.4f} at mu = {mu_c:.2f} GeV; alpha_s(v) = {as_v:.4f} (x{a_c / as_v:.1f} short); m_W(QCD) = "
      f"{1e3 * mw_qcd:.0f} MeV vs 80377; v/M from colour {np.sqrt(3) * F_PI / M_CELL:.1e} vs {V_EW / M_CELL:.1e}")

# A6: top condensation (BHL one loop): 1/y^2 = 0 at Lambda, run to m_t with SM gauge running
gi0 = np.array([0.4626, 0.6477, 1.1666])       # g1 (GUT), g2, g3 at m_t
bb = np.array([-41 / 10, 19 / 6, 7.0])


def yt_bhl(Lam):
    def rhs(t, u):
        g2s = 1 / (1 / gi0 ** 2 + 2 * bb * t / (16 * PI ** 2))
        c = 8 * g2s[2] + 9 / 4 * g2s[1] + 17 / 20 * g2s[0]
        return -2 / (16 * PI ** 2) * (4.5 - u * c)      # u = 1/y^2
    t1, n = np.log(Lam / M_T), 4000
    h, t, u = -t1 / n, t1, 0.0
    for _ in range(n):
        k1 = rhs(t, u); k2 = rhs(t + h / 2, u + h / 2 * k1)
        k3 = rhs(t + h / 2, u + h / 2 * k2); k4 = rhs(t + h, u + h * k3)
        u += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t += h
    return 1 / np.sqrt(u)


yts = {L: yt_bhl(L) for L in (1e4, 1e10, M_CELL)}
ok = min(yts.values()) > 1.2 * YT_MT
check(ok, "A6 [E/M]", "top-pair condensation (compositeness 1/y^2 = 0 at the cutoff, one-loop SM running): the "
      "quasi-fixed point gives y_t(m_t) far above measured at every cutoff up to the cell; bubble scalar at 2 m_t",
      "; ".join(f"L={L:.0e}: y={y:.3f}, y v/sqrt2~{y * V_EW / np.sqrt(2):.0f}" for L, y in yts.items())
      + f" vs y={YT_MT} (y v/sqrt2 = 163, pole 172.6); m_H(bubble) = {2 * M_T:.0f} vs 125.1")

# ---------------------------------------------------------------- B
print("== B. the scalar as a neighbourhood-configuration composite")
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def rand_su2():
    q = RNG.standard_normal(4); q /= np.linalg.norm(q)
    return q[0] * np.eye(2) + 1j * sum(q[i + 1] * sig[i] for i in range(3))


def adj(g):
    return np.array([[0.5 * np.trace(sig[a] @ g @ sig[b] @ g.conj().T).real for b in range(3)] for a in range(3)])


err = max(np.abs(adj(g) - adj(-g)).max() for g in [rand_su2() for _ in range(20)])
J1 = [np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]), np.array([[0, 0, 1j], [0, 0, 0], [-1j, 0, 0]]),
      np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])]
spins = set()
for k in range(1, 5):
    Jt = []
    for a in range(3):
        tot = np.zeros((3 ** k, 3 ** k), complex)
        for p in range(k):
            ops = [np.eye(3)] * k; ops[p] = J1[a]
            m = ops[0]
            for o in ops[1:]:
                m = np.kron(m, o)
            tot += m
        Jt.append(tot)
    ev = np.linalg.eigvalsh(sum(x @ x for x in Jt))
    for e in ev:
        spins.add(round((-1 + np.sqrt(1 + 4 * max(e, 0))) / 2, 6))
# rishon strings on two bonds: per-bond number zero <=> even length
from itertools import product as iprod
evn = all(len(s) % 2 == 0 for L in range(1, 7) for s in iprod([(0, 1), (0, -1), (1, 1), (1, -1)], repeat=L)
          if sum(x[1] for x in s if x[0] == 0) == 0 and sum(x[1] for x in s if x[0] == 1) == 0)
check(err < 1e-12 and all(abs(s - round(s)) < 1e-6 for s in spins) and evn, "B1 [T]",
      "the global SU(2)_L centre -1 acts trivially on every link register (Ad(-g) = Ad(g)), on edges (singlets) and on "
      "every rishon string of fixed per-bond number (even length); adj^k has integer spin only: no configuration of "
      "links, rishons and edges is a doublet; a Y = 1/2 doublet needs an odd number of doublet fermion modes, so a "
      "boson needs a singlet fermion too: the A2 pairs, dressed by links",
      f"|Ad(g)-Ad(-g)| {err:.0e}; spins in adj^1..4 {sorted(float(x) for x in spins)}; rishon strings <= 6 even: {evn}")

# B2: lattice gap equation + RPA at zero spatial momentum (single-cone band, antiperiodic 20^3)
Ln = 20
k1 = 2 * PI * (np.arange(Ln) + 0.5) / Ln
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
E0 = 2 * np.sqrt(np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2).ravel()
I0 = np.mean(1 / E0)
gcoup = 1.3 / I0                                   # supplied: 30% above critical
mdyn = brentq(lambda m: gcoup * np.mean(1 / np.sqrt(E0 ** 2 + m ** 2)) - 1, 1e-6, 50, xtol=1e-15, rtol=1e-15)
E = np.sqrt(E0 ** 2 + mdyn ** 2)
Pp = lambda q: gcoup * np.mean(4 * E / (4 * E ** 2 - q ** 2))
Ps = lambda q: gcoup * np.mean((4 * E ** 2 - 4 * mdyn ** 2) / E / (4 * E ** 2 - q ** 2))
qs = np.linspace(0.01, 1.99, 50) * mdyn
nozero = all(1 - Ps(q) > 0 for q in qs) and all(1 - Pp(q) < 0 for q in qs)
check(abs(1 - Pp(0)) < 1e-10 and abs(1 - Ps(2 * mdyn * (1 - 1e-9))) < 1e-6 and nozero, "B2 [F]",
      "four-mode bilinear binding at mean field on a 20^3 lattice: the pseudoscalar (eaten) pole sits at q0 = 0 and the "
      "scalar at the threshold 2m for any coupling above critical (identities of the gap equation); no scalar below 2m",
      f"G = 1.3 G_c, m = {mdyn:.3f}/a; 1 - Pi_P(0) = {1 - Pp(0):.0e}; 1 - Pi_S(2m) = {1 - Ps(2 * mdyn * (1 - 1e-9)):.0e}")

# B3: Pagels-Stokar: v^2 = K m^2 ln(Lambda^2/m^2)/(4 pi^2); bubble m_H = 2 m
mf = M_H / 2
expo = 4 * PI ** 2 * V_EW ** 2 / (3 * mf ** 2) / 2          # ln(Lambda/m), K = 3
Kmin = 4 * PI ** 2 * V_EW ** 2 / (mf ** 2 * 2 * np.log(M_CELL / mf))
K_even = 2 * np.ceil(Kmin / 2)
S_K = K_even / (12 * PI)                      # K/2 heavy colour-doublets, S = 1/(6 pi) each
check(expo > np.log(M_CELL / mf) and Kmin > 7, "B3 [E/M]", "a bubble scalar at 125.1 GeV needs constituents at "
      "62.6 GeV; with K = 3 (one coloured Dirac doublet member) the decay-constant sum needs a cutoff far above the "
      "cell; at the cell K >= 8 degenerate chiral states, whose S is excluded",
      f"ln(Lambda/m) = {expo:.0f} (cell: {np.log(M_CELL / mf):.1f}); K_min = {Kmin:.2f}; K = {K_even:.0f}: S = {S_K:.2f} vs "
      f"{S_MEAS}+-{S_ERR} ({(S_K - S_MEAS) / S_ERR:.1f} sigma)")

# ---------------------------------------------------------------- C
print("== C. protection of a light scalar")
# C1: colour-singlet bilinear Sigma (psi in 2_L x N, chi in 2_R x N): Sigma -> gL Sigma gR^T
N = 3
TL = [np.kron(s / 2, np.eye(N)) for s in sig]
T3R = np.kron(sig[2] / 2, np.eye(N))
gens = lambda S: [t @ S for t in TL] + [S @ T3R.T]


def n_unbroken(S):
    M = np.array([g.ravel() for g in gens(S)]).T
    M = np.vstack([M.real, M.imag])
    return 4 - np.linalg.matrix_rank(M, tol=1e-9)


samples = [RNG.standard_normal((2 * N, 2 * N)) + 1j * RNG.standard_normal((2 * N, 2 * N)) for _ in range(30)]
samples += [np.outer(RNG.standard_normal(2 * N), RNG.standard_normal(2 * N)) for _ in range(30)]
samples += [np.kron(np.eye(2), np.diag(RNG.random(N))), np.eye(2 * N)]
mx = max(n_unbroken(S) for S in samples)
ratios = [sum(np.linalg.norm(t @ S) ** 2 for t in TL[:2]) / np.linalg.norm(S) ** 2 for S in samples]
check(mx == 1 and n_unbroken(np.eye(2 * N)) == 1 and np.ptp(ratios) < 1e-12, "C1 [T]",
      "every nonzero colour-singlet psi chi condensate breaks SU(2)_L x U(1)_Y to at most one U(1) (any real "
      "combination of SU(2)_L generators is invertible), and SU(2)_L acts on one index only, so the charged-W mass "
      "sum_(a=1,2) |T_a Sigma|^2 = |Sigma|^2/2 for every Sigma (fixed by f alone): v = f, no misalignment angle, no doublet pNGB",
      f"max unbroken over {len(samples)} vacua {mx}; W-mass ratio {np.mean(ratios):.12f}, spread {np.ptp(ratios):.0e}")

# C2: pair-square 10 = R^6 + R^4; colour su(3) in so(6), su(2)_L in so(4)
lam = np.zeros((8, 3, 3), complex)
lam[0][0, 1] = lam[0][1, 0] = 1; lam[1][0, 1] = -1j; lam[1][1, 0] = 1j; lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1; lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1; lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)


def realify(A):                                  # anti-Hermitian 3x3 -> real 6x6
    return np.block([[A.real, -A.imag], [A.imag, A.real]])


def emb(X6=None, X4=None):
    Z = np.zeros((10, 10))
    if X6 is not None: Z[:6, :6] = X6
    if X4 is not None: Z[6:, 6:] = X4
    return Z


col = [emb(X6=realify(1j * l / 2)) for l in lam]
qi = np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]], float)
qj = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]], float)
su2 = [emb(X4=x / 2) for x in (qi, qj, qi @ qj)]
null = lambda Ms: 10 - np.linalg.matrix_rank(np.vstack(Ms), tol=1e-9)
fix_c, fix_cw = null(col), null(col + su2)
nvec = np.zeros(10); nvec[6:] = RNG.standard_normal(4); nvec /= np.linalg.norm(nvec)
so10 = []
for a in range(10):
    for b in range(a + 1, 10):
        X = np.zeros((10, 10)); X[a, b], X[b, a] = 1, -1; so10.append(X)
img = np.array([X @ nvec for X in so10])
rk = np.linalg.matrix_rank(img, tol=1e-9)
cas = -sum(c @ c for c in col)
P = np.eye(10) - np.outer(nvec, nvec)
ev = np.sort(np.linalg.eigvalsh(P @ cas @ P))[1:]
nt = int(np.sum(np.isclose(ev, 4 / 3))); n0 = int(np.sum(np.isclose(ev, 0)))
check(fix_c == 4 and fix_cw == 0 and rk == 9 and nt == 6 and n0 == 3, "C2 [T]",
      "pair-square 10: colour fixes only the (1,2,2) block and colour + SU(2)_L fix no direction, so a colour-safe pair "
      "condensate breaks EW at its own scale; its 9 Goldstones are a colour triplet (6 real, Casimir 4/3; its Y = -+1/3 is the (6,1,1) charge) "
      "+ 3 eaten: no light doublet", f"fixed dims colour {fix_c}, colour+SU2_L {fix_cw}; broken {rk} = "
      f"{nt} (C3 = 4/3) + {n0} (singlet)")

# C3: pseudoreal contrast SU(4)/Sp(4): Sigma_theta = cos Sigma_B + sin Sigma_H; m_W^2 ~ sin^2 theta
Jm = np.array([[0, 1], [-1, 0]], complex); Z2 = np.zeros((2, 2)); I2 = np.eye(2)
SB = np.block([[Jm, Z2], [Z2, -Jm]]); SH = np.block([[Z2, I2], [-I2, Z2]])
TL4 = [np.block([[s / 2, Z2], [Z2, Z2]]) for s in sig]
mw = lambda th: sum(np.linalg.norm(t @ S + S @ t.T) ** 2 for t in TL4 for S in [np.cos(th) * SB + np.sin(th) * SH])
th = np.linspace(0, PI / 2, 7)
rr = np.array([mw(x) for x in th]) / mw(PI / 2)
uni = np.abs((np.cos(0.4) * SB + np.sin(0.4) * SH) @ (np.cos(0.4) * SB + np.sin(0.4) * SH).conj().T - np.eye(4)).max()
check(np.allclose(rr, np.sin(th) ** 2, atol=1e-12) and uni < 1e-12, "C3 [T]",
      "contrast: four Weyl doublets of a pseudoreal factor give the SU(4)/Sp(4) vacuum manifold, where m_W^2 is "
      "proportional to sin^2 theta (theta = 0 keeps SU(2) x U(1)); v = f sin theta needs content the rules do not "
      "have (A2: no pseudoreal binder holds a doublet pair)", f"m_W^2(theta)/m_W^2(pi/2) = {np.round(rr, 6).tolist()}")

# C4: vacuum subtraction cannot change the m^2 coefficient of the sea energy
Ef = lambda m: -4 * np.mean(np.sqrt(E0 ** 2 + m ** 2))
h = 1e-3
c2 = (Ef(h) - Ef(0)) / h ** 2
c2s = ((Ef(h) - Ef(0.3)) - (Ef(0) - Ef(0.3))) / h ** 2
check(np.isclose(c2, c2s) and abs(c2) > 0.5, "C4 [T/F]",
      "CL-3 measures the response from the vacuum: subtracting the vacuum's value (a constant in the condensate) leaves "
      "the cell-sized m^2 coefficient of the sea energy unchanged; a subtraction that moves with the condensate makes "
      "the potential identically flat and fixes no v", f"dE/d(m^2) at 0: {c2:.4f}/a^2 (subtracted {c2s:.4f}); = -2 I0, "
      f"I0 = {I0:.4f}")

print("supplied: one chiral family x3 (CL-1 content), Pati-Salam and Sp(2) factors as readings, plaquette count")
print("  1/alpha = 4 pi kappa T, ladder alpha_c = pi/(3 C_F), mean-field bubble, single-cone 20^3 band, G = 1.3 G_c,")
print("  M = 2.44e18 GeV; measured: alpha_s(MZ), f_pi, g, gauge couplings at m_t, y_t(m_t), m_H, v, S = -0.05(7).")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
