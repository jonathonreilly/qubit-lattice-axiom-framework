#!/usr/bin/env python3
"""T45 test: quark CP phase arctan sqrt5. Pre-registration: PREREG.md (same folder).
Run:  python3 t45_test.py   (numpy only)
"""
import numpy as np
from math import pi, sqrt, atan, atan2, acos, degrees, radians
from fractions import Fraction

rng = np.random.default_rng(45)
OUT = {}

def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# ------------------------------------------------------------------ Test A
hdr("A. Gauge covariance of a 1+5 projector on Q_L = (2,3)")
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)
T = [s1 / 2, s2 / 2, s3 / 2]
gm = np.zeros((8, 3, 3), complex)
gm[0][0, 1] = gm[0][1, 0] = 1
gm[1][0, 1] = -1j; gm[1][1, 0] = 1j
gm[2][0, 0] = 1; gm[2][1, 1] = -1
gm[3][0, 2] = gm[3][2, 0] = 1
gm[4][0, 2] = -1j; gm[4][2, 0] = 1j
gm[5][1, 2] = gm[5][2, 1] = 1
gm[6][1, 2] = -1j; gm[6][2, 1] = 1j
gm[7] = np.diag([1, 1, -2]) / sqrt(3)
t = gm / 2
I2, I3 = np.eye(2), np.eye(3)
gens_full = [np.kron(a, I3) for a in T] + [np.kron(I2, b) for b in t]
Q = np.kron(np.diag([2 / 3, -1 / 3]), I3)              # T3 + Y, Y = 1/6
gens_ewsb = [np.kron(I2, b) for b in t] + [Q]

def commutant_dim(gens, n=6):
    rows = []
    for G in gens:
        rows.append(np.kron(G, np.eye(n)) - np.kron(np.eye(n), G.T))
    M = np.vstack(rows)
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv < 1e-10)), M

dimA1, _ = commutant_dim(gens_full)
dimA2, M2 = commutant_dim(gens_ewsb)
print("commutant dim  SU(2)xSU(3) on (2,3):        ", dimA1, "(expect 1: scalars only)")
print("commutant dim  SU(3)_c x U(1)_em after EWSB:", dimA2, "(expect 2: P_u, P_d)")
# nullspace of the EWSB case -> check diagonal entries of its projectors
_, S, Vh = np.linalg.svd(M2)
null = Vh[np.sum(S > 1e-10):].conj()
mats = [v.reshape(6, 6, order="F") for v in null]
# Hermitian idempotents in span: combos a P_u + b P_d with a,b in {0,1}
Pu = np.kron(np.diag([1, 0]), I3); Pd = np.kron(np.diag([0, 1]), I3)
inspan = all(np.linalg.matrix_rank(np.array([m.flatten() for m in mats] + [P.flatten()]), tol=1e-8)
             == len(mats) for P in (Pu, Pd))
print("P_u, P_d lie in the commutant:", inspan)
print("diag entries of covariant projectors: P_u ->", np.diag(Pu).real, " P_d ->", np.diag(Pd).real,
      "(only 0 or 1: no fractional weight)")

# gauge orbit of the democratic vector: weight of a basis vector is not invariant
u = np.kron(np.ones(2), np.ones(3)) / sqrt(6)
e = np.zeros(6, complex); e[0] = 1
def haar_su(n):
    Z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Qm, R = np.linalg.qr(Z)
    Qm = Qm @ np.diag(np.diag(R) / abs(np.diag(R)))
    return Qm / (np.linalg.det(Qm) ** (1 / n))
ws = []
for _ in range(20000):
    g = np.kron(haar_su(2), haar_su(3))
    ws.append(abs(np.vdot(e, g @ u)) ** 2)
ws = np.array(ws)
print("w=|<e|g u>|^2 over gauge orbit of u: min %.4f  max %.4f  (u itself: 1/6 = %.4f)" %
      (ws.min(), ws.max(), 1 / 6))
A_pass = (dimA1 == 1 and dimA2 == 2 and ws.max() > 0.5 and ws.min() < 0.01)
print("TEST A", "PASS" if A_pass else "FAIL")
OUT["A"] = dict(commutant_full=dimA1, commutant_ewsb=dimA2, w_min=float(ws.min()), w_max=float(ws.max()), pass_=bool(A_pass))

# ------------------------------------------------------------------ Test B
hdr("B. Is delta = arctan sqrt5 a rational multiple of pi (finite-group / root-of-unity phase)?")
delta = atan(sqrt(5))
c2 = np.cos(2 * delta)
print("delta = %.10f deg, cos(2 delta) = %.12f (=-2/3: %s)" % (degrees(delta), c2, abs(c2 + 2 / 3) < 1e-12))
niven = {Fraction(0), Fraction(1, 2), Fraction(-1, 2), Fraction(1), Fraction(-1)}
print("Niven: rational cos of rational*pi must lie in {0,+-1/2,+-1}; -2/3 in set?", Fraction(-2, 3) in niven)
x = delta / pi
best = min((abs(x - p / q), p, q) for q in range(1, 3001) for p in range(0, q + 1))
print("closest p/q (q<=3000) to delta/pi: %d/%d  |diff| = %.3e (a rational would give ~0)" % (best[1], best[2], best[0]))
B_pass = (Fraction(-2, 3) not in niven) and best[0] > 1e-9
print("TEST B", "PASS" if B_pass else "FAIL")
OUT["B"] = dict(cos2delta=float(c2), closest_rational=[best[1], best[2]], diff=float(best[0]), pass_=bool(B_pass))

# ------------------------------------------------------------------ CKM helpers
def ckm_std(s12, s23, s13, dl):
    c12, c23, c13 = [sqrt(1 - z * z) for z in (s12, s23, s13)]
    e = np.exp(1j * dl)
    return np.array([
        [c12 * c13, s12 * c13, s13 * np.conj(e)],
        [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])

def tri_angles(V):
    """(alpha,beta,gamma) of the d-b unitarity triangle, degrees, abs values"""
    g = np.angle(-V[0, 0] * np.conj(V[0, 2]) / (V[1, 0] * np.conj(V[1, 2])))
    b = np.angle(-V[1, 0] * np.conj(V[1, 2]) / (V[2, 0] * np.conj(V[2, 2])))
    a = np.angle(-V[2, 0] * np.conj(V[2, 2]) / (V[0, 0] * np.conj(V[0, 2])))
    return degrees(abs(a)), degrees(abs(b)), degrees(abs(g))

def apex_bar(V):
    z = -V[0, 0] * np.conj(V[0, 2]) / (V[1, 0] * np.conj(V[1, 2]))
    return z.real, z.imag

def right_angle_residual(V):
    B = np.abs(V) ** 2
    return B[0, 0] * B[0, 2] + B[2, 0] * B[2, 2] - B[1, 0] * B[1, 2], B[1, 0] * B[1, 2]

# ------------------------------------------------------------------ Test C
hdr("C. Moduli fix the phase; CP violation is visible in CP-even moduli")
alpha_s = (1 / (4 * pi)) / sqrt(0.5934)
lam = sqrt(alpha_s / 2); Aa = sqrt(2 / 3)
r = 1 / sqrt(6)
s12, s23, s13 = lam, Aa * lam ** 2, Aa * lam ** 3 * r
dl = atan(sqrt(5))
Va = ckm_std(s12, s23, s13, dl)
print("alpha_s = %.5f  lambda = %.5f  |Vus|=%.6f |Vcb|=%.6f |Vub|=%.6f |Vtd|=%.6f" %
      (alpha_s, lam, abs(Va[0, 1]), abs(Va[1, 2]), abs(Va[0, 2]), abs(Va[2, 0])))
rb, eb = apex_bar(Va)
al, be, ga = tri_angles(Va)
print("exact barred apex: rho_bar=%.5f eta_bar=%.5f (repo note: 0.16264, 0.36304)" % (rb, eb))
print("exact angles: alpha=%.2f beta=%.2f gamma=%.2f (repo note: 90.69, 23.44, 65.87)" % (al, be, ga))
# C1: recover delta from four moduli
a12 = abs(Va[0, 1]); a23 = abs(Va[1, 2]); a13 = abs(Va[0, 2]); atd = abs(Va[2, 0])
c13 = sqrt(1 - a13 ** 2); S12 = a12 / c13; S23 = a23 / c13
C12, C23 = sqrt(1 - S12 ** 2), sqrt(1 - S23 ** 2)
cosd = (S12 ** 2 * S23 ** 2 + C12 ** 2 * C23 ** 2 * a13 ** 2 - atd ** 2) / (2 * S12 * S23 * C12 * C23 * a13)
d_rec = degrees(acos(cosd))
print("C1: delta recovered from |Vus|,|Vcb|,|Vub|,|Vtd| = %.9f deg  (input %.9f)" % (d_rec, degrees(dl)))
C1 = abs(d_rec - degrees(dl)) < 1e-6
# C2: real completions
td0 = abs(S12 * S23 - C12 * C23 * a13)
tdpi = abs(S12 * S23 + C12 * C23 * a13)
print("C2: |Vtd| atlas = %.6f ; real completion delta=0: %.6f (ratio %.2f) ; delta=pi: %.6f (ratio %.2f)" %
      (atd, td0, atd / td0, tdpi, atd / tdpi))
C2 = min(abs(atd / td0 - 1), abs(atd / tdpi - 1)) > 0.30
# data (PDG 2024 wolfenstein, barred)
lamD, AD, rD, eD = 0.22497, 0.839, 0.1581, 0.3548
zb = rD + 1j * eD
s13z = AD * lamD ** 3 * zb * sqrt(1 - AD ** 2 * lamD ** 4) / (sqrt(1 - lamD ** 2) * (1 - AD ** 2 * lamD ** 4 * zb))
Vd = ckm_std(lamD, AD * lamD ** 2, abs(s13z), np.angle(s13z))
print("PDG-2024 central: |Vub|=%.5f |Vtd|=%.5f delta=%.2f deg" %
      (abs(Vd[0, 2]), abs(Vd[2, 0]), degrees(np.angle(s13z))))
a12d, a23d, a13d, atdd = abs(Vd[0, 1]), abs(Vd[1, 2]), abs(Vd[0, 2]), abs(Vd[2, 0])
c13d = sqrt(1 - a13d ** 2); S12d = a12d / c13d; S23d = a23d / c13d
C12d, C23d = sqrt(1 - S12d ** 2), sqrt(1 - S23d ** 2)
td0d = abs(S12d * S23d - C12d * C23d * a13d); tdpid = abs(S12d * S23d + C12d * C23d * a13d)
print("   data |Vtd| = %.6f ; real completions: delta=0: %.6f, delta=pi: %.6f -> CP-odd phase is visible in |Vtd| (a CP-even modulus)" %
      (atdd, td0d, tdpid))
res_a, den_a = right_angle_residual(Va)
res_d, den_d = right_angle_residual(Vd)
print("C3: exact right-angle residual (B11B13+B31B33-B21B23)/(B21B23): atlas %.3e ; PDG-central %.3e" %
      (res_a / den_a, res_d / den_d))
print("   leading-order sum rule |Vub|^2+|Vtd|^2 vs |Vus Vcb|^2: atlas %.4e vs %.4e ; PDG %.4e vs %.4e" %
      (a13 ** 2 + atd ** 2, (a12 * a23) ** 2, a13d ** 2 + atdd ** 2, (a12d * a23d) ** 2))
print("   ratio |Vtd|^2/|Vub|^2: atlas %.3f (5 at leading order) ; PDG-central %.3f" % (atd ** 2 / a13 ** 2, atdd ** 2 / a13d ** 2))
print("TEST C:", "C1", "PASS" if C1 else "FAIL", "| C2", "PASS" if C2 else "FAIL")
OUT["C"] = dict(delta_recovered_deg=d_rec, Vtd_atlas=atd, Vtd_real_delta0=td0, Vtd_real_deltapi=tdpi,
                ratio_to_delta0=atd / td0, ratio_to_deltapi=atd / tdpi, atlas_alpha_bar=al, atlas_gamma_bar=ga,
                right_angle_rel_residual_atlas=res_a / den_a, right_angle_rel_residual_pdg=res_d / den_d,
                Vtd2_over_Vub2_atlas=atd ** 2 / a13 ** 2, Vtd2_over_Vub2_pdg=atdd ** 2 / a13d ** 2, C1=bool(C1), C2=bool(C2))

# ------------------------------------------------------------------ Test D
hdr("D. Data versus the arccos(1/sqrt k) family and the wall's 'cheapest test'")
N = 200000
rr = rng.normal(rD, 0.0092, N); ee = rng.normal(eD, 0.0072, N)
gam = np.degrees(np.arctan2(ee, rr))
g_fit, s_fit = gam.mean(), gam.std()
# alpha from the apex
alp = np.degrees(np.arccos(((-rr) * (1 - rr) + ee * ee) / np.sqrt((rr ** 2 + ee ** 2) * ((1 - rr) ** 2 + ee ** 2))))
a_fit, sa_fit = alp.mean(), alp.std()
g_lhcb, s_lhcb = 63.8, 3.6
print("fit-derived gamma = %.2f +- %.2f deg (rho,eta uncorrelated: approximation) ; LHCb direct 63.8 +3.5 -3.7" % (g_fit, s_fit))
print("fit-derived alpha = %.2f +- %.2f deg (right angle: %.1f sigma from 90)" % (a_fit, sa_fit, abs(a_fit - 90) / sa_fit))
print(" k   gamma_k   sig(fit)  sig(LHCb)")
rowsD = []
for k in range(2, 13):
    gk = degrees(acos(1 / sqrt(k)))
    rowsD.append((k, gk, abs(gk - g_fit) / s_fit, abs(gk - g_lhcb) / s_lhcb))
    print("%2d  %8.3f  %8.2f  %8.2f" % rowsD[-1])
g24 = degrees(acos(sqrt(1 / 3))); g33 = 45.0
print("wall alternatives: 2+4 -> %.3f deg (%.1f sig fit, %.1f sig LHCb); 3+3 -> 45 (%.1f sig fit, %.1f sig LHCb)" %
      (g24, abs(g24 - g_fit) / s_fit, abs(g24 - g_lhcb) / s_lhcb, abs(45 - g_fit) / s_fit, abs(45 - g_lhcb) / s_lhcb))
# alpha for alternatives with radius r^2 = 1/6 fixed
for name, w in (("1+5", 1 / 6), ("2+4", 1 / 3), ("3+3", 1 / 2)):
    rho_, eta_ = r * sqrt(w), r * sqrt(1 - w)
    v1 = np.array([-rho_, -eta_]); v2 = np.array([1 - rho_, -eta_])
    a_ = degrees(acos(v1 @ v2 / (np.linalg.norm(v1) * np.linalg.norm(v2))))
    print("   split %s with r^2=1/6 fixed: apex (%.4f,%.4f) alpha = %.2f deg (data %.2f +- %.2f)" % (name, rho_, eta_, a_, a_fit, sa_fit))
D_pass = (abs(g24 - g_fit) / s_fit > 3) and (abs(45 - g_fit) / s_fit > 3)
print("TEST D (wall's 'needs 1 deg to separate 2+4/3+3' is stale):", "PASS" if D_pass else "FAIL")
OUT["D"] = dict(gamma_fit=g_fit, gamma_fit_sigma=s_fit, alpha_fit=a_fit, alpha_fit_sigma=sa_fit,
                k_table=[dict(k=k, gamma=g, sigma_fit=a, sigma_lhcb=b) for k, g, a, b in rowsD],
                sig_2p4_fit=abs(g24 - g_fit) / s_fit, sig_3p3_fit=abs(45 - g_fit) / s_fit, pass_=bool(D_pass))

# ------------------------------------------------------------------ Test E
hdr("E. Texture route: hierarchical 4-zero Hermitian textures, ONE imaginary element vs generic phase")
def sample(N, mode):
    def sector():
        D = np.ones(N)
        C = 10 ** rng.uniform(-1.7, -0.6, N)
        B = 10 ** rng.uniform(-3.0, -1.2, N)
        A = 10 ** rng.uniform(-4.2, -2.2, N)
        return A, B, C, D
    Au, Bu, Cu, Du = sector(); Ad, Bd, Cd, Dd = sector()
    if mode == "up_imag":   phu, phd = np.full(N, pi / 2), np.zeros(N)
    elif mode == "down_imag": phu, phd = np.zeros(N), np.full(N, pi / 2)
    elif mode == "random":  phu, phd = rng.uniform(0, 2 * pi, N), np.zeros(N)
    elif mode == "real":    phu, phd = np.zeros(N), np.zeros(N)
    def mk(A, B, C, D, ph):
        M = np.zeros((N, 3, 3), complex)
        M[:, 0, 1] = A * np.exp(1j * ph); M[:, 1, 0] = A * np.exp(-1j * ph)
        M[:, 1, 1] = B; M[:, 1, 2] = C; M[:, 2, 1] = C; M[:, 2, 2] = D
        return M
    Mu, Md = mk(Au, Bu, Cu, Du, phu), mk(Ad, Bd, Cd, Dd, phd)
    def diag(M):
        w, U = np.linalg.eigh(M)
        idx = np.argsort(np.abs(w), axis=1)
        w = np.take_along_axis(w, idx, 1)
        U = np.take_along_axis(U, idx[:, None, :], 2)
        return np.abs(w), U
    wu, Uu = diag(Mu); wd, Ud = diag(Md)
    V = np.conj(np.transpose(Uu, (0, 2, 1))) @ Ud
    return wu, wd, V

def analyse(V):
    ab = np.abs(V)
    g = np.angle(-V[:, 0, 0] * np.conj(V[:, 0, 2]) / (V[:, 1, 0] * np.conj(V[:, 1, 2])))
    b = np.angle(-V[:, 1, 0] * np.conj(V[:, 1, 2]) / (V[:, 2, 0] * np.conj(V[:, 2, 2])))
    a = np.angle(-V[:, 2, 0] * np.conj(V[:, 2, 2]) / (V[:, 0, 0] * np.conj(V[:, 0, 2])))
    Ru = ab[:, 0, 0] * ab[:, 0, 2] / (ab[:, 1, 0] * ab[:, 1, 2])
    return np.degrees(np.abs(a)), np.degrees(np.abs(g)), Ru

resE = {}
Nn = 1_500_000
for mode in ("up_imag", "down_imag", "random", "real"):
    wu, wd, V = sample(Nn, mode)
    ab = np.abs(V)
    win = ((ab[:, 0, 1] > 0.15) & (ab[:, 0, 1] < 0.35) & (ab[:, 1, 2] > 0.02) & (ab[:, 1, 2] < 0.08)
           & (ab[:, 0, 2] > 0.001) & (ab[:, 0, 2] < 0.01)
           & (wu[:, 0] / wu[:, 1] < 0.1) & (wu[:, 1] / wu[:, 2] < 0.2)
           & (wd[:, 0] / wd[:, 1] < 0.3) & (wd[:, 1] / wd[:, 2] < 0.2))
    n_in = int(win.sum())
    a, g, Ru = analyse(V[win])
    if n_in == 0:
        print(mode, "no samples in window"); continue
    near = np.mean(np.abs(a - 90) < 5)
    cg = np.abs(np.cos(np.radians(g)) - Ru) / Ru
    resE[mode] = dict(n=n_in, frac_alpha_within5=float(near), median_abs_alpha_minus_90=float(np.median(np.abs(a - 90))),
                      median_rel_cosgamma_vs_Ru=float(np.median(cg)),
                      gamma_median=float(np.median(g)), gamma_p16_p84=[float(np.percentile(g, 16)), float(np.percentile(g, 84))])
    print("%-10s n_in_window=%6d  frac(|alpha-90|<5deg)=%.3f  median|alpha-90|=%.2f  median|cos g - R_u|/R_u=%.3f  gamma median %.1f [%.1f, %.1f]" %
          (mode, n_in, near, np.median(np.abs(a - 90)), np.median(cg), np.median(g), np.percentile(g, 16), np.percentile(g, 84)))
E_pass = ("up_imag" in resE and "random" in resE and resE["up_imag"]["median_abs_alpha_minus_90"] < 5
          and resE["up_imag"]["frac_alpha_within5"] >= 3 * max(resE["random"]["frac_alpha_within5"], 1e-9)
          and resE["up_imag"]["median_rel_cosgamma_vs_Ru"] < 0.10)
print("TEST E", "PASS" if E_pass else "FAIL")
OUT["E"] = dict(results=resE, pass_=bool(E_pass))

# ------------------------------------------------------------------ Test F
hdr("F. Born-triangle lemma: atlas apex = <e|u> e in the (u, v) frame, p = |<e|u>|^2 = 1/n")
ok = True
for n in (2, 3, 6, 7):
    p = 1 / n
    uu = np.ones(n) / sqrt(n); ee_ = np.zeros(n); ee_[0] = 1
    c = uu @ ee_
    v = ee_ - c * uu; v /= np.linalg.norm(v)
    ecoords = np.array([ee_ @ uu, ee_ @ v])                       # e in (u,v) coordinates
    apex = c * ecoords                                            # <e|u> e
    rho_, eta_ = apex
    v1 = -apex; v2 = np.array([1, 0]) - apex
    alpha_ = degrees(acos(v1 @ v2 / (np.linalg.norm(v1) * np.linalg.norm(v2))))
    gamma_ = degrees(atan2(eta_, rho_))
    good = (abs(rho_ - p) < 1e-12 and abs(eta_ - sqrt(p * (1 - p))) < 1e-12 and abs(alpha_ - 90) < 1e-9
            and abs(gamma_ - degrees(acos(sqrt(p)))) < 1e-9 and abs(np.hypot(rho_, eta_) - sqrt(p)) < 1e-12)
    ok &= good
    print("n=%d: apex=(%.6f,%.6f) alpha=%.6f gamma=%.6f r=cos(delta)=%.6f  %s" % (n, rho_, eta_, alpha_, gamma_, np.hypot(rho_, eta_), "ok" if good else "MISMATCH"))
# complex u with random phases: same weights
uc = np.exp(1j * rng.uniform(0, 2 * pi, 6)) / sqrt(6)
print("complex democratic vector: |<e|u>|^2 =", abs(uc[0]) ** 2)
print("TEST F", "PASS" if ok else "FAIL")
OUT["F"] = dict(pass_=bool(ok))

hdr("SUMMARY")
for k in "ABCDEF":
    v = OUT[k]
    print(k, v.get("pass_", (v.get("C1"), v.get("C2"))))
import json
with open(__file__.replace("t45_test.py", "t45_results.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=float)
