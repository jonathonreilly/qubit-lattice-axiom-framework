AUDIT_INPUT_PATHS = ('docs/COUPLING_DILUTION_EXCLUDES_THE_LEFT_RIGHT_SLAB_UNDER_ONE_CELL_COUPLING_AND_ITS_SHARED_HYPERCHARGE_HITS_A_LANDAU_POLE_BELOW_THE_CUTOFF_BOUNDED_THEOREM_NOTE_2026-10-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Coupling dilution in the left-right slab (shared SU(3) x U(1)_Y bulk, SU(2) per wall).

Tests one common cell coupling against measured alpha_s, alpha_2, alpha_Y with one-loop running.
Labels: [T] exact, [E] estimate with supplied numbers.
"""
import math
import numpy as np

AUDIT_TIMEOUT_SEC = 120
RNG = np.random.default_rng(20261025)
PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + (": " + detail if detail else ""))


# ---------------- supplied numbers ----------------
MZ = 91.1876
AS_MZ = 0.1180
AEM_INV = 127.95
S2W = 0.23122
VEW = 246.0
LAMS = (2.4e18, 1.22e18)
VPS = (1e8, 1e9, 1e10, 1e11)
CNORM = {"SM": 1.0, "GUT": 3.0 / 5.0, "cell1/6": 36.0}  # 1/alpha_common = c/alpha_Y
MF = {"u": 2.2e-3, "d": 4.7e-3, "s": 0.095, "c": 1.27, "b": 4.18, "t": 172.7,
      "e": 0.511e-3, "mu": 0.1057, "tau": 1.777}
A2_INV_MZ = AEM_INV * S2W
AY_INV_MZ = AEM_INV * (1.0 - S2W)
A3_INV_MZ = 1.0 / AS_MZ
TP = 2.0 * math.pi

# ---------------- P1: layer-chain zero mode [T] ----------------
print("P1 layer chain zero mode (Gaussian, in-layer 1/g_k^2, stiffness kappa)")
from fractions import Fraction as Fr


def g00_exact(ginv, kap, p2):
    """G_00 of M = p2 diag(ginv) + kap Lap (tridiagonal), exact rationals (Thomas algorithm)."""
    n = len(ginv)
    d = [p2 * ginv[i] + kap * (1 if i in (0, n - 1) else 2) for i in range(n)]
    if n == 1:
        d = [p2 * ginv[0]]
    off = -kap
    # solve M x = e0 by elimination from the far end: Schur complement onto site 0
    s = d[n - 1]
    for i in range(n - 2, -1, -1):
        s = d[i] - off * off / s
    return 1 / s


errs = []
for Ls in (2, 5, 16, 50):
    ginv = [Fr(int(x), 100) for x in RNG.integers(30, 300, Ls)]  # 1/g_k^2, rational
    S = sum(ginv)
    for kap in (Fr(1, 10), Fr(1), Fr(10)):
        p2 = Fr(1, 10 ** 30)
        errs.append(float(abs(p2 * g00_exact(ginv, kap, p2) * S - 1)))
    p2 = Fr(1, 10 ** 30)
    errs.append(float(abs(p2 * g00_exact(ginv, Fr(0), p2) * ginv[0] - 1)))  # disordered: wall only
check("P1 flat mode 1/g4^2 = sum 1/g_k^2; wall-local g4 = g_wall", max(errs) < 1e-8,
      "max rel err %.1e over Ls in {2,5,16,50}" % max(errs))
print("  common g0: 1/alpha_shared = Ls/alpha0, 1/alpha_wall = 1/alpha0 -> a3 : a_sh : a2 = 1/Ls : 1/Ls : 1")

# ---------------- P2: hypercharge matching at v' [T] ----------------
gL, gp, gY = 0.65, 0.65, 0.45
v, vp = 1.0, 1e3
# basis (W3L, W3', B_sh); H: (gL W3L - gY B), H': (gp W3' - gY B)
a = np.array([gL, 0, -gY]); b = np.array([0, gp, -gY])
M2 = 0.25 * (v ** 2 * np.outer(a, a) + vp ** 2 * np.outer(b, b))
w, U = np.linalg.eigh(M2)
ph = U[:, 0]
e_num = gL * ph[0] / 1.0  # coupling of photon to T3L
e_pred = 1.0 / math.sqrt(1 / gL ** 2 + 1 / gp ** 2 + 1 / gY ** 2)
# v=0: massless plane; Y_low coupling of light field (T3'=0, Y_sh=y) and mirror (T3'=1/2, Y_sh=1/6)
bb = b / np.linalg.norm(b)
n = np.array([0, gY, gp]); n /= np.linalg.norm(n)
glow = gY * n[2]
gmir = gp * 0.5 * n[1] + gY * (1 / 6) * n[2]
err2 = max(abs(abs(e_num) - e_pred) / e_pred, abs(n @ bb),
           abs(1 / glow ** 2 - (1 / gY ** 2 + 1 / gp ** 2)) * glow ** 2,
           abs(gmir / glow - (0.5 + 1 / 6)))
check("P2 Y_low = T3' + Y_sh, 1/aY(v') = 1/a_sh + 1/a2'", err2 < 1e-10, "max err %.1e" % err2)

# ---------------- one-loop b coefficients from field lists ----------------
# entry: (type, colour T*mult, SU2L T*mult, sum Y^2 over components)  type 'W' Weyl, 'S' complex scalar
def fam_light():
    # (name, ncol, n2L, Y, weyl)
    return [("qL", 3, 2, 1 / 6), ("uR", 3, 1, 2 / 3), ("dR", 3, 1, -1 / 3), ("L", 1, 2, -1 / 2), ("eR", 1, 1, -1.0)]


def bvec(weyl, scal):
    """weyl/scal: list of (ncol, n2L, Y, mult). returns (bY_SMnorm, b2, b3)."""
    bY = b2 = b3 = 0.0
    for lst, f in ((weyl, 2 / 3), (scal, 1 / 3)):
        for nc, n2, Y, m in lst:
            bY += f * Y * Y * nc * n2 * m
            if n2 == 2:
                b2 += f * 0.5 * nc * m
            if nc == 3:
                b3 += f * 0.5 * n2 * m
    return np.array([bY, b2 - 22 / 3, b3 - 11.0])


SMW = [(nc, n2, Y, 3) for _, nc, n2, Y in fam_light()]
SMS = [(1, 2, 0.5, 1)]
bSM = bvec(SMW, SMS)
check("b(SM) = (41/6, -19/6, -7) from field list", np.allclose(bSM, [41 / 6, -19 / 6, -7]),
      "(%.4f, %.4f, %.4f)" % tuple(bSM))
# above v': mirror family under (colour, SU2L singlet, Y_sh): q'R (3, SU2' doublet -> mult 2), u'L, d'L, l'R (x2), e'L
MIRW = [(3, 1, 1 / 6, 6), (3, 1, 2 / 3, 3), (3, 1, -1 / 3, 3), (1, 1, -1 / 2, 6), (1, 1, -1.0, 3)]
MIRS = [(1, 1, 0.5, 2)]
bHI = bSM + bvec(MIRW, MIRS) - np.array([0, -22 / 3, -11.0])
check("b(above v') = (41/3, -19/6, -3) [shared Y, wall SU2L, shared colour]",
      np.allclose(bHI, [41 / 3, -19 / 6, -3]), "(%.4f, %.4f, %.4f)" % tuple(bHI))


def dirac_b(nc, Q):  # vector-like Dirac fermion below v' : Y_low = Q both chiralities
    return np.array([2 / 3 * Q * Q * nc * 2, 0.0, (2 / 3 * 0.5 * 2) if nc == 3 else 0.0])


QM = {"u": (3, 2 / 3), "c": (3, 2 / 3), "t": (3, 2 / 3), "d": (3, -1 / 3), "s": (3, -1 / 3), "b": (3, -1 / 3),
      "e": (1, -1.0), "mu": (1, -1.0), "tau": (1, -1.0)}


def run_up(vp, Lam, spread):
    """Return dict: inverse couplings at Lam (aY_sh, a2, a3) or pole scale; spread: mirror at m_f v'/v."""
    inv = np.array([AY_INV_MZ, A2_INV_MZ, A3_INV_MZ])
    mu = MZ
    thr = sorted([(MF[f] * vp / VEW, f) for f in MF]) if spread else []
    b = bSM.copy()
    for m, f in thr:
        if m > mu:
            inv = inv - b / TP * math.log(m / mu); mu = m
        b = b + dirac_b(*QM[f])
    inv = inv - b / TP * math.log(vp / mu); mu = vp
    inv[0] = inv[0] - inv[1]  # matching: 1/a_sh = 1/aY_low - 1/a2'(v'), a2' = a2 (P_slab)
    pole = None
    if bHI[0] > 0 and inv[0] > 0:
        pole = vp * math.exp(TP * inv[0] / bHI[0])
    inv_sh_vp = inv[0]
    inv = inv - bHI / TP * math.log(Lam / vp)
    return inv, pole, inv_sh_vp


print("P3 shared U(1) after matching at v' (b_sh = 41/3 above v')")
poles_ok = True
lines = []
for spread in (False, True):
    for vp in VPS:
        inv, pole, ivp = run_up(vp, LAMS[0], spread)
        lines.append("  v'=%.0e %s: 1/a_sh(v')=%.1f  pole=%.2e GeV  1/a_sh(2.4e18)=%.1f" %
                     (vp, "spread" if spread else "single", ivp, pole, inv[0]))
        poles_ok &= pole < LAMS[0]
        if pole >= LAMS[1]:
            lines.append("    (clears the 1.22e18 cutoff reading)")
print("\n".join(lines))
check("P3 Landau pole of shared U(1) below cutoff for all v' in [1e8,1e11]", poles_ok,
      "pre-set cutoff 2.4e18, both threshold variants")
# smallest v' with pole above cutoff (single threshold)
lo, hi = 1e8, 1e18
for _ in range(80):
    mid = math.sqrt(lo * hi)
    if run_up(mid, LAMS[0], False)[1] < LAMS[0]:
        lo = mid
    else:
        hi = mid
vp_min = hi
print("  pole clears 2.4e18 only for v' > %.2e GeV (face-swap window ends 1e11)" % vp_min)

# ---------------- P4: Ls-free equality of shared factors ----------------
print("P4 shared factors equal at cutoff: c/a_sh vs 1/a3 (Ls-free)")
inv_sm = np.array([AY_INV_MZ, A2_INV_MZ, A3_INV_MZ]) - bSM / TP * math.log(LAMS[0] / MZ)
for k, c in CNORM.items():
    print("  control (SM running, no mirror) %-7s ratio %.3f" % (k, c * inv_sm[0] / inv_sm[2]))
ok4 = True
for k, c in CNORM.items():
    f = lambda vp: c * run_up(vp, LAMS[0], False)[0][0] / run_up(vp, LAMS[0], False)[0][2] - 1
    lo, hi = vp_min * 1.0001, 1e17
    if f(lo) * f(hi) < 0:
        for _ in range(80):
            mid = math.sqrt(lo * hi)
            lo, hi = (mid, hi) if f(lo) * f(mid) > 0 else (lo, mid)
        inv = run_up(hi, LAMS[0], False)[0]
        print("  %-7s equal only at v'=%.2e (outside window), there Ls_fit=(1/a3)/(1/a2)=%.3f" % (k, hi, inv[2] / inv[1]))
        ok4 &= hi > 1e11 and inv[2] / inv[1] < 1.5
    else:
        print("  %-7s never equal for v' in (%.1e, 1e17)" % (k, vp_min))
check("P4 in window (pole) no c equalises shared couplings; equality needs v' > 1e11 and Ls_fit < 1.5", ok4)

# ---------------- P5: Ls fit from colour/SU2 ----------------
print("P5 Ls_fit = (1/a3)/(1/a2) at cutoff")
fits = []
for Lam in LAMS:
    s = inv_sm if Lam == LAMS[0] else np.array([AY_INV_MZ, A2_INV_MZ, A3_INV_MZ]) - bSM / TP * math.log(Lam / MZ)
    row = ["SM %.3f" % (s[2] / s[1])]
    fits.append(s[2] / s[1])
    for vp in VPS:
        inv = run_up(vp, Lam, True)[0]
        fits.append(inv[2] / inv[1]); row.append("%.0e:%.3f" % (vp, inv[2] / inv[1]))
    print("  L=%.2e  " % Lam + "  ".join(row))
print("  asymptotes: SM b3/b2 = %.3f, LR %.3f" % (bSM[2] / bSM[1], bHI[2] / bHI[1]))
Lneed = (2 * A2_INV_MZ - A3_INV_MZ) / ((-bSM[2] / TP) - 2 * (-bSM[1] / TP))
print("  Ls=2 (SM running) needs ln(L/MZ) = %.0f, L ~ 1e%.0f GeV" % (Lneed, (Lneed + math.log(MZ)) / math.log(10)))
check("P5 no integer Ls >= 2 fits colour/SU2 at either cutoff", max(fits) < 1.5, "max Ls_fit %.3f" % max(fits))

# ---------------- P6: downward prediction ----------------
print("P6 alpha0 = alpha2(cutoff); predict alpha_s(MZ), alpha_Y(MZ) [v'=1e10 spread; L=2.4e18]")


def run_down(Ls, c, vp, Lam):
    up = run_up(vp, Lam, True)[0]
    a0 = up[1]  # 1/alpha0 = 1/a2(L)
    inv3L, invshL = Ls * a0, Ls * a0 / c
    # down: Lam -> v' with bHI, then v' -> MZ with spread thresholds
    inv3 = inv3L + bHI[2] / TP * math.log(Lam / vp)
    ish = invshL + bHI[0] / TP * math.log(Lam / vp)
    iY = ish + (A2_INV_MZ - bSM[1] / TP * math.log(vp / MZ))  # + 1/a2'(v') (= a2(v'), SU2 unaffected)
    thr = sorted([(MF[f] * vp / VEW, f) for f in MF], reverse=True)
    b = bSM + sum(dirac_b(*QM[f]) for f in MF)
    mu = vp
    for m, f in thr:
        iY += b[0] / TP * math.log(mu / m); inv3 += b[2] / TP * math.log(mu / m)
        mu = m; b = b - dirac_b(*QM[f])
    iY += b[0] / TP * math.log(mu / MZ); inv3 += b[2] / TP * math.log(mu / MZ)
    return 1 / inv3 if inv3 > 0 else float("inf"), 1 / iY


for Ls in (1, 2, 5, 46, 58):
    s3, sY = run_down(Ls, CNORM["cell1/6"], 1e10, LAMS[0])
    sG = run_down(Ls, CNORM["GUT"], 1e10, LAMS[0])[1]
    print("  Ls=%-3d a_s(MZ)=%.4g  1/aY(MZ)=%.1f (cell) %.1f (GUT)  [meas 0.118, 98.4]" % (Ls, s3, 1 / sY, 1 / sG))
a0sm = inv_sm[1]
for Ls in (1, 2):
    print("  control SM-only Ls=%d: a_s(MZ)=%.4f" % (Ls, 1 / (Ls * a0sm + bSM[2] / TP * math.log(LAMS[0] / MZ))))
best = (9e9, None)
for c in CNORM.values():
    for vp in VPS:
        for Lam in LAMS:
            for Ls in np.linspace(1, 100, 991):
                s3, sY = run_down(Ls, c, vp, Lam)
                e = max(abs(s3 / AS_MZ - 1), abs(sY * AY_INV_MZ - 1))
                if e < best[0]:
                    best = (e, (Ls, c, vp, Lam, s3, 1 / sY))
e, (Ls, c, vp, Lam, s3, iy) = best
print("  best joint: Ls=%.1f c=%.2f v'=%.0e L=%.2e a_s=%.4f 1/aY=%.1f (max rel err %.2f)" % (Ls, c, vp, Lam, s3, iy, e))
check("P6 no continuous Ls in [1,100] fits alpha_s and alpha_Y within 10%", e > 0.10, "best max rel err %.2f" % e)
ok_s = [L for L in np.linspace(1, 100, 991) if 0.110 <= run_down(L, 36, 1e10, LAMS[0])[0] <= 0.126]
print("  Ls giving a_s in [0.110,0.126]: %s" % (("%.2f..%.2f" % (min(ok_s), max(ok_s))) if ok_s else "none in [1,100]"))
check("P6 alpha_s window (if any) excludes Ls >= 2", (not ok_s) or max(ok_s) < 2)

# ---------------- P7: per-layer strengths (per-factor couplings) ----------------
print("P7 per-layer beta3 = 6 (1/a3)/(4 pi Ls)")
rows = []
for spread in (True, False):
    for vp in (1e8, 1e11):
        i3 = run_up(vp, LAMS[0], spread)[0][2]
        b3 = 6 * i3 / (4 * math.pi)
        rows.append((vp, i3, b3))
        print("  %s v'=%.0e: 1/a3(L)=%.1f  beta3=%.1f/Ls; Ls_max(beta>=3)=%.1f; Ls 46..58: %.2f..%.2f"
              % ("spread" if spread else "single", vp, i3, b3, b3 / 3, b3 / 46, b3 / 58))
check("P7 reproduces wall-local D2 (14.9/Ls at v'=1e8, Ls_max ~5)", abs(rows[0][2] - 14.9) < 0.3 and rows[0][2] / 3 < 6,
      "%.2f/Ls" % rows[0][2])
check("P7 portal window Ls 46-58 disjoint from flat-colour Ls <= ~7", all(r[2] / 46 < 3 and r[2] / 3 < 7 for r in rows))

# ---------------- P8: SU(2) wall-locality vs one coupling ----------------
i2L = inv_sm[1]
inv_bulk_max = 2.45 * 4 * math.pi / 4  # beta = 4/g^2 = 4 (1/a)/(4 pi) <= 2.45 (wall-local A2, Ls=4)
ratio = i2L / inv_bulk_max
print("P8 SU(2): wall 1/a2(L)=%.1f vs confining bulk 1/a <= %.2f -> ratio %.1f" % (i2L, inv_bulk_max, ratio))
check("P8 one coupling cannot give weak SU2 wall + confining SU2 bulk (ratio > 5)", ratio > 5, "%.1f" % ratio)

print("VERDICT: EXCLUDES the LR slab under one common cell coupling (P3 pole, P4, P5/P6, P8).")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
