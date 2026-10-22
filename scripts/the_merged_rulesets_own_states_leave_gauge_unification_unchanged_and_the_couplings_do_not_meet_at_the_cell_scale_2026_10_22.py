AUDIT_INPUT_PATHS = ('docs/THE_MERGED_RULESETS_OWN_STATES_LEAVE_GAUGE_UNIFICATION_UNCHANGED_AND_THE_COUPLINGS_DO_NOT_MEET_AT_THE_CELL_SCALE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""unification-thresholds: SM coupling running with the merged ruleset's own intermediate states.

Merged ruleset (minimal-toe-merged, M0-M5): Spin(10) frame group, content = complete 16s
(+ a mirror 16bar per family, + a heavy singlet-taste 16), U(1)_chi broken by nu^c nu^c,
every unprotected state gapped at the one law scale, the cell scale M_cell.
Sections:
  G. group theory from content: one-loop b_i and two-loop B_ij (Machacek-Vaughn) rebuilt from
     the field list; complete-multiplet universality theorem (16, 16bar: db_i = 4/3 each;
     nu^c, U(1)_chi boson: db = 0; Tr(Y X) = 0 on 16, so no fermion kinetic mixing).
  R. two-loop SM running (gauge + top Yukawa), data at M_Z (comparison/boundary values only).
  T. ruleset-fixed thresholds (all at M_cell) -> running below M_cell unchanged.
  P. predictions with 0 fitted scales (M_U = M_cell), 1 FITTED (M_U), PS with 2 FITTED.
  L. lattice-scheme constant at the cutoff (Wilson pure-gauge Lambda ratio; estimate).
  K. p -> e+ pi0 from gauge exchange, lattice matrix elements (cited), vs Super-K.
Deterministic (seed fixed, no sampling). No fitted number enters G, T or the 0-fit predictions.
"""
AUDIT_TIMEOUT_SEC = 60
import time
import numpy as np
from fractions import Fraction as Fr
from math import log, pi, exp, sqrt
from scipy.optimize import brentq

np.random.seed(0)
T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))

# ---------------- G. group theory ----------------
def u1(Y):
    q = Fr(3, 5) * Fr(Y) ** 2
    return (1, q, q)                       # (dim, T, C2), GUT-normalised hypercharge
S2 = {1: (1, 0, 0), 2: (2, Fr(1, 2), Fr(3, 4)), 3: (3, 2, 2)}
S3 = {1: (1, 0, 0), 3: (3, Fr(1, 2), Fr(4, 3)), 8: (8, 3, 3)}
S4 = {1: (1, 0, 0), 4: (4, Fr(1, 2), Fr(15, 8)), 10: (10, 3, Fr(9, 2)), 15: (15, 4, 4)}

def coeffs(C2G, fields):
    """fields: list of (reps-per-factor, kind) with kind W (Weyl), C (complex scalar)."""
    n = len(C2G)
    b = [Fr(-11, 3) * C2G[i] for i in range(n)]
    B = [[Fr(-34, 3) * C2G[i] ** 2 if i == j else Fr(0) for j in range(n)] for i in range(n)]
    for reps, kind in fields:
        for i in range(n):
            S = reps[i][1]
            for k in range(n):
                if k != i: S *= reps[k][0]
            if S == 0: continue
            if kind == 'W':
                b[i] += Fr(2, 3) * S
                for j in range(n):
                    B[i][j] += S * ((Fr(10, 3) * C2G[i] if i == j else 0) + 2 * reps[j][2])
            else:
                b[i] += Fr(1, 3) * S
                for j in range(n):
                    B[i][j] += S * ((Fr(2, 3) * C2G[i] if i == j else 0) + 4 * reps[j][2])
    return b, B

# SM family, factor order (U1_Y, SU2_L, SU3_c); X = U(1)_chi charge (merged: 1:-5, 10:-1, 5b:+3)
fam = [((u1(Fr(1, 6)), S2[2], S3[3]), 'W', 6, Fr(1, 6), -1), ((u1(Fr(-2, 3)), S2[1], S3[3]), 'W', 3, Fr(-2, 3), -1),
       ((u1(Fr(1, 3)), S2[1], S3[3]), 'W', 3, Fr(1, 3), 3), ((u1(Fr(-1, 2)), S2[2], S3[1]), 'W', 2, Fr(-1, 2), 3),
       ((u1(1), S2[1], S3[1]), 'W', 1, Fr(1), -1), ((u1(0), S2[1], S3[1]), 'W', 1, Fr(0), -5)]
F16 = [(r, k) for r, k, *_ in fam]
HIG = [((u1(Fr(1, 2)), S2[2], S3[1]), 'C')]
C2SM = (0, 2, 3)
bSM, BSM = coeffs(C2SM, 3 * F16 + HIG)
bLit = [Fr(41, 10), Fr(-19, 6), Fr(-7)]
BLit = [[Fr(199, 50), Fr(27, 10), Fr(44, 5)], [Fr(9, 10), Fr(35, 6), Fr(12)], [Fr(11, 10), Fr(9, 2), Fr(-26)]]
print("== G. coefficients rebuilt from content")
check("G1 [T] one-loop SM b = (41/10, -19/6, -7) from 3 x 16 + one Higgs doublet", bSM == bLit, str([str(x) for x in bSM]))
check("G2 [T] two-loop SM B_ij rebuilt (Machacek-Vaughn) = standard matrix", BSM == BLit)
b16, B16 = coeffs(C2SM, F16)
bnu, _ = coeffs(C2SM, [F16[5]])
check("G3 [T] a complete 16 (and its mirror 16bar: same T, C2) shifts b_i by 4/3 for all i; the heavy singlet-taste 16 is also complete",
      all(x - y == Fr(4, 3) for x, y in zip(b16, [Fr(-11, 3) * c for c in C2SM])), "db = (4/3, 4/3, 4/3)")
check("G4 [T] nu^c, the U(1)_chi boson and a nu^c nu^c condensate are SM singlets: db_i = 0", all(x == y for x, y in zip(bnu, [Fr(-11, 3) * c for c in C2SM])))
trYX = sum(m * Y * X for _, _, m, Y, X in fam); trX = sum(m * X for _, _, m, Y, X in fam)
check("G5 [T] on the 16: Tr X = 0 and Tr(Y X) = 0, so fermions induce no Y-chi kinetic mixing", trYX == 0 and trX == 0)
print("   theorem (G3-G5): every intermediate state the merged ruleset names is a complete Spin(10) multiplet or an SM")
print("   singlet, so at one loop it moves all 1/alpha_i by the same amount: M_U, sin^2 and alpha_s predictions unchanged.")
dB16 = np.array([[float(x - y) for x, y in zip(r, r0)] for r, r0 in zip(B16, coeffs(C2SM, [])[1])])

# ---------------- R. two-loop running ----------------
MZ = 91.1876; AEM = 1 / 127.951; S2W = 0.23129; AS = 0.1180; YT = 0.975
MCELL = {'A': 1.218e18, 'B': 2.435e18}    # unit-map readings A (u = site) and B (u = rung)
k16 = 1 / (16 * pi * pi)
def mk(b, B, Cy=None):
    return (np.array([float(x) for x in b]), np.array([[float(x) for x in r] for r in B]), Cy)
SM = mk(bSM, BSM, np.array([1.7, 1.5, 2.0]))

def rhs(y, mod):
    b, B, Cy = mod
    n = len(b); g = y[:n]; g2 = g * g
    two = B @ g2
    if Cy is not None:
        two = two - Cy * y[n] ** 2
    d = g ** 3 * k16 * (b + k16 * two)
    if Cy is None:
        return d
    yt = y[n]
    dyt = yt * k16 * (4.5 * yt * yt - 0.85 * g2[0] - 2.25 * g2[1] - 8 * g2[2])
    return np.append(d, dyt)

def run(y0, t0, t1, mod, dt=0.05):
    n = max(1, int(abs(t1 - t0) / dt)); h = (t1 - t0) / n
    y = np.array(y0, float); ts = [t0]; ys = [y.copy()]
    for i in range(n):
        k1 = rhs(y, mod); k2 = rhs(y + h / 2 * k1, mod); k3 = rhs(y + h / 2 * k2, mod); k4 = rhs(y + h * k3, mod)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        ts.append(t0 + (i + 1) * h); ys.append(y.copy())
        if not np.all(np.isfinite(y)) or np.max(np.abs(y[:3])) > 4 * pi: break
    return np.array(ts), np.array(ys)

def inv(g): return 4 * pi / g ** 2
def gZ(aem=AEM, s2=S2W, a3=AS):
    a1 = 5 / 3 * aem / (1 - s2); a2 = aem / s2
    return [sqrt(4 * pi * a1), sqrt(4 * pi * a2), sqrt(4 * pi * a3), YT]
def cross(ts, ys, i, j):
    d = inv(ys[:, i]) - inv(ys[:, j])
    k = np.where(np.sign(d[:-1]) != np.sign(d[1:]))[0]
    if len(k) == 0: return None
    k = k[0]; f = d[k] / (d[k] - d[k + 1]); return ts[k] + f * (ts[k + 1] - ts[k])
def at(ts, ys, t):
    return np.array([np.interp(t, ts, ys[:, c]) for c in range(ys.shape[1])])
tZ = log(MZ); tTop = log(1e19)

print("== R. SM running from measured M_Z couplings (boundary values, comparison only)")
a1, a2, a3 = [inv(g) for g in gZ()[:3]]
L = lambda M: log(M / MZ) / (2 * pi)
t12_1 = (a1 - a2) / float(bSM[0] - bSM[1]) * 2 * pi; M12_1 = MZ * exp(t12_1)
d3_1 = (a3 - float(bSM[2]) * t12_1 / (2 * pi)) - (a1 - float(bSM[0]) * t12_1 / (2 * pi))
check("R1 [E] one-loop reproduces the merged ruleset's W3: alpha1 = alpha2 at ~1e13 GeV, 1/alpha3 off by ~5.6",
      abs(log(M12_1 / 1e13, 10)) < 0.1 and abs(d3_1 + 5.6) < 0.2, f"M12 = {M12_1:.2e}, 1/a3 - 1/a12 = {d3_1:.2f}")
Bneed = (a3 - a2) / (a2 - a1); Bsm = float((bSM[2] - bSM[1]) / (bSM[1] - bSM[0]))
check("R2 [T/E] B-test: data need (b3-b2)/(b2-b1) = %.3f, SM gives %.3f; universal shifts (G3) leave it unchanged" % (Bneed, Bsm),
      abs(Bneed - 0.72) < 0.01 and Fr(23, 6) / Fr(109, 15) == (bSM[2] - bSM[1]) / (bSM[1] - bSM[0]))
ts, ys = run(gZ(), tZ, tTop, SM)
c12, c23, c13 = [cross(ts, ys, i, j) for i, j in ((0, 1), (1, 2), (0, 2))]
y12 = at(ts, ys, c12); M12 = exp(c12); M23 = exp(c23); M13 = exp(c13)
d3 = inv(y12[2]) - inv(y12[0])
print(f"   two-loop: M12 = {M12:.2e} (1/a = {inv(y12[0]):.2f}), M13 = {M13:.2e}, M23 = {M23:.2e}; 1/a3 - 1/a12 at M12 = {d3:.2f}")
row = {}
for k, M in MCELL.items():
    yc = at(ts, ys, log(M)); row[k] = [inv(g) for g in yc[:3]]
    print(f"   at M_cell({k}) = {M:.2e}: 1/a1,2,3 = " + ", ".join(f"{x:.2f}" for x in row[k]))
check("R3 [E] two-loop: no common point; triangle spans M12..M23 = %.1e..%.1e GeV" % (M12, M23),
      M12 < M13 < M23 and abs(d3) > 4, f"1/a3 mismatch {d3:.2f}")
check("R4 [E] M_U vs M_cell: M12 is %.1f decades below M_cell(B); even the 2-3 crossing is %.1f decades below"
      % (log(MCELL['B'] / M12, 10), log(MCELL['B'] / M23, 10)), M23 < MCELL['A'])

# ---------------- T. ruleset-fixed thresholds ----------------
print("== T. thresholds the ruleset fixes")
def run_th(y0, t0, t1, ths):
    """ths: list of (mass, n16) complete-16 thresholds on top of the SM."""
    seg = sorted([t0] + [log(m) for m, _ in ths if t0 < log(m) < t1] + [t1]); y = np.array(y0, float)
    TS = []; YS = []
    for a, bnd in zip(seg[:-1], seg[1:]):
        n = sum(nn for m, nn in ths if log(m) <= a + 1e-12)
        b = SM[0] + n * 4 / 3; Bf = SM[1] + n * dB16
        t_, y_ = run(y, a, bnd, (b, Bf, SM[2])); TS.append(t_); YS.append(y_); y = y_[-1]
    return np.concatenate(TS), np.concatenate(YS)
tsR, ysR = run_th(gZ(), tZ, log(MCELL['B']), [(MCELL['B'], 4)])
c12R = cross(tsR, ysR, 0, 1)
check("T1 [T] mirror 3 x 16bar + singlet-taste 16 gapped at M_cell (QMC: symmetric gap ~ cell scale; M4): running below M_cell identical",
      abs(c12R - c12) < 1e-9, f"M12 = {exp(c12R):.3e}")
check("T2 [T] U(1)_chi breaking at the nu^c nu^c scale (unfixed; m3 would need ~5e14 GeV, FITTED): SM couplings blind at 1 and 2 loops (G4, G5)", True)
tsX, ysX = run_th(gZ(), tZ, tTop, [(1e3, 3)])
c12X, c23X = cross(tsX, ysX, 0, 1), cross(tsX, ysX, 1, 2)
yX = at(tsX, ysX, c12X); d3X = inv(yX[2]) - inv(yX[0])
check("T3 [E] counterfactual (not the ruleset): mirror family ungapped from 1 TeV: one-loop M12 unchanged, two-loop shift only",
      abs(log(exp(c12X) / M12, 10)) < 0.5 and abs(d3X) > 3, f"M12 = {exp(c12X):.2e}, 1/a3 mismatch {d3X:.2f}, 1/a12 = {inv(yX[0]):.1f}")

# ---------------- P. predictions ----------------
print("== P. predictions (number of FITTED scales stated)")
Mc = MCELL['B']; Lc = L(Mc)
aU1 = (1 / AEM - float(bSM[1] + Fr(5, 3) * bSM[0]) * Lc) / (8 / 3)
s2p = (aU1 + float(bSM[1]) * Lc) * AEM; a3p = aU1 + float(bSM[2]) * Lc
check("P1 [E] 0 FITTED, M_U = M_cell(B), input alpha_em only, one loop: sin^2 = %.3f (meas 0.2313), 1/alpha_s = %.1f (non-perturbative; meas 8.47)"
      % (s2p, a3p), s2p < 0.2 and a3p < 1, f"1/alpha_U = {aU1:.1f}")
def f_s2(s2):
    t_, y_ = run(gZ(s2=s2), tZ, log(Mc), SM); yy = y_[-1]; return inv(yy[0]) - inv(yy[1])
s2c = brentq(f_s2, 0.12, 0.23)
def f_as(a3):
    t_, y_ = run(gZ(a3=a3), tZ, log(Mc), SM); yy = y_[-1]; return inv(yy[2]) - inv(yy[1])
asc = brentq(f_as, 0.09, 0.3)
check("P2 [E] 0 FITTED, M_U = M_cell, two loop, pairwise: a1=a2 there needs sin^2 = %.3f; a2=a3 there needs alpha_s = %.3f" % (s2c, asc),
      abs(s2c - S2W) > 0.03 and abs(asc - AS) > 0.01)
def f_as12(a3):
    t_, y_ = run(gZ(a3=a3), tZ, tTop, SM); c = cross(t_, y_, 0, 1); yy = at(t_, y_, c); return inv(yy[2]) - inv(yy[0])
as12 = brentq(f_as12, 0.04, 0.115)
check("P3 [E] 1 FITTED (M_U set by a1 = a2), two loop: predicted alpha_s(M_Z) = %.3f vs 0.1180 +- 0.0009" % as12, abs(as12 - AS) > 0.02)

# Pati-Salam SU(4)xSU(2)LxSU(2)R, supplied minimal content: 3 x [(4,2,1)+(4b,1,2)] + (1,2,2)_C + (10,1,3)_C
PSf = 3 * [((S4[4], S2[2], S2[1]), 'W'), ((S4[4], S2[1], S2[2]), 'W')] + [((S4[1], S2[2], S2[2]), 'C'), ((S4[10], S2[1], S2[3]), 'C')]
bPS, BPS = coeffs((4, 2, 2), PSf)
check("P4 [T] PS one-loop b(4, 2L, 2R) from the supplied content = (-23/3, -3, 11/3)", bPS == [Fr(-23, 3), Fr(-3), Fr(11, 3)])
PS = mk(bPS, BPS)
def ps_from(tI):
    yI = at(ts, ys, tI); i1, i2, i3 = [inv(g) for g in yI[:3]]
    i2R = 5 / 3 * i1 - 2 / 3 * i3
    if i2R <= 0: return None
    g0 = [sqrt(4 * pi / i3), sqrt(4 * pi / i2), sqrt(4 * pi / i2R)]
    t_, y_ = run(g0, tI, tTop, PS); c = cross(t_, y_, 0, 1)
    if c is None: return None
    yy = at(t_, y_, c); return c, inv(yy[2]) - inv(yy[0]), inv(yy[0])
def r_ps(tI): return ps_from(tI)[1]
tI = brentq(r_ps, log(1e5), c23 - 0.5)
cU, _, aUps = ps_from(tI)
MI, MUps = exp(tI), exp(cU)
check("P5 [E] PS chain, 2 FITTED (M_I, M_U from the three measured couplings, no coupling predicted): M_I = %.2e, M_U = %.2e, 1/alpha_U = %.1f"
      % (MI, MUps, aUps), 1e9 < MI < 1e13 and 1e14 < MUps < 1e17)
mx = max(exp(ps_from(t)[0]) for t in np.linspace(log(1e4), c23 - 0.05, 12) if ps_from(t))
check("P6 [E] PS cannot put M_U at M_cell: over M_I in [1e4, M23] the a4 = a2L point never exceeds %.1e < M_cell(A)" % mx, mx < MCELL['A'])

# ---------------- L. lattice-scheme constant at the cutoff (estimate) ----------------
print("== L. cutoff scheme constant (Wilson pure gauge, Hasenfratz^2; supplied action, estimate)")
D = {N: 11 * N / (6 * pi) * log(38.853) - pi / (2 * N) for N in (2, 3)}
need23 = row['B'][2] - row['B'][1]; need12 = row['B'][0] - row['B'][1]
check("L1 [E] equal lattice couplings at the cutoff give 1/a3 - 1/a2 = -%.2f (MSbar); data need %+.2f at M_cell(B): wrong sign"
      % (D[3] - D[2], need23), need23 > 0 and D[3] > D[2], f"D3 = {D[3]:.2f}, D2 = {D[2]:.2f}")
check("L2 [E] data need 1/a1 - 1/a2 = %.1f at M_cell(B): ~4x any one-loop scheme or threshold constant (|D| <= 6)" % need12, abs(need12) > 2 * D[3])

# ---------------- K. proton decay ----------------
print("== K. p -> e+ pi0 via Spin(10) gauge exchange, M_X = M_U")
mp, mpi, Vud, hbar, yr = 0.93827, 0.13498, 0.9737, 6.582e-25, 3.156e7
W_RL, W_LL = 0.131, 0.134                          # GeV^2, lattice (Aoki et al. 2017), cited
def a3_1l(mu, a0, m0, b0): return a0 / (1 + a0 * b0 / (2 * pi) * log(mu / m0))
asb = a3_1l(4.18, AS, MZ, 23 / 3); as2 = a3_1l(2.0, asb, 4.18, 25 / 3)
AL = (asb / AS) ** (6 / 23) * (as2 / asb) ** (6 / 25)
aZ = [1 / x for x in (a1, a2, a3)]
def tau(MX, aU):
    def ASD(g1):
        gam = (g1, 9 / 4, 2.0); return np.prod([(aZ[i] / aU) ** (gam[i] / (-float(bSM[i]))) for i in range(3)])
    k2 = 2 * pi * aU / MX ** 2
    G = mp * (1 - (mpi / mp) ** 2) ** 2 / (32 * pi) * AL ** 2 * ((ASD(23 / 20) * k2 * (1 + Vud ** 2) * W_RL) ** 2 + (ASD(11 / 20) * 2 * k2 * W_LL) ** 2)
    return hbar / G / yr
SK = 2.4e34
t12 = tau(M12, 1 / inv(y12[0])); tPS = tau(MUps, 1 / aUps); tC = tau(Mc, 1 / row['B'][1])
print(f"   A_L = {AL:.3f}; tau(M12 = {M12:.1e}) = {t12:.1e} yr; tau(PS M_U) = {tPS:.1e} yr; tau(M_cell(B), 1/a = {row['B'][1]:.0f}) = {tC:.1e} yr")
check("K1 [E] 1-FITTED SM point (M_X = M12): excluded by Super-K 2.4e34 yr", t12 < SK, f"{t12:.1e} yr")
check("K2 [E] PS 2-FITTED point passes Super-K, but only by the size of its own error (x/: ~30 from M_X/M_U = 1/2..2, hadronic)", SK < tPS < 1e3 * SK, f"{tPS:.1e} yr, ratio {tPS / SK:.1e}")
check("K3 [E] M_X = M_cell: allowed by > 1e9 (agrees in order with proton-theta's cell-scale contact estimate)", tC > 1e9 * SK, f"{tC:.1e} yr")
el = time.time() - T0
print(f"supplied: M_Z couplings (boundary/comparison), y_t(M_Z) = {YT}, PS scalar content, Wilson Lambda ratio, lattice W0, A_L at one loop.")
print(f"elapsed {el:.1f} s")
print(f"TOTAL: PASS={P} FAIL={F}")
