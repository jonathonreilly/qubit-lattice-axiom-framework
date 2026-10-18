"""HIER-3 R1: the g^2(M_cut) window for a colour strong scale at v/M_Pl, with
regressions against H1-referee and main numbers. Own code."""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scipy.optimize import brentq
import numpy as np
import rgcommon as rg

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

FOURPI = 4 * math.pi
# ---------------- regressions ----------------
print("== Regressions ==")
e_pure = 8 * math.pi ** 2 / (15 * 11 * rg.LN10)
e_nf8 = 8 * math.pi ** 2 / (15 * (11 - 16 / 3) * rg.LN10)
check("R(i) one-loop 15-decade edge, pure SU(3)", abs(e_pure - 0.208) < 5e-4, f"g2={e_pure:.4f}")
check("R(i) one-loop 15-decade edge, SU(3) N_f=8", abs(e_nf8 - 0.403) < 5e-4, f"g2={e_nf8:.4f}")
v_hier = 246.282818290129
need = 7 * math.log(rg.M_PL / v_hier) / (2 * math.pi)
runup = 1 / 0.118 + 7 / (2 * math.pi) * math.log(rg.M_PL / rg.M_Z)
check("R(ii) needed 1/alpha(M_Pl) for b0=7 pole at v", abs(need - 42.8) < 0.1, f"{need:.2f}")
check("R(ii) one-loop run-up of 0.118 to M_Pl", abs(runup - 52.4) < 0.1, f"{runup:.2f}")
aMZ = rg.piecewise_down(0.10330382, v_hier, [(172.69, 6), (rg.M_Z, 5)], loops=2)
check("R(iii) piecewise 2-loop alpha_s(v)->alpha_s(M_Z) = 0.118233", abs(aMZ - 0.118233) < 1e-5,
      f"{aMZ:.6f}")
# Lambda invariance along a 2-loop trajectory
a1, _ = rg.run_alpha(0.02, rg.M_PL, 1e6, 6, 2)
L0 = rg.Lambda(rg.M_PL, 0.02, 6, 2); L1 = rg.Lambda(1e6, a1, 6, 2)
check("R(iv) exact 2-loop Lambda RG-invariant", abs(L1 / L0 - 1) < 1e-8, f"rel={L1/L0-1:.2e}")
a4, _ = rg.run_alpha(0.02, rg.M_PL, 1e6, 6, 4)
L40 = rg.Lambda(rg.M_PL, 0.02, 6, 4); L41 = rg.Lambda(1e6, a4, 6, 4)
check("R(iv') 4-loop Lambda RG-invariant", abs(L41 / L40 - 1) < 1e-7, f"rel={L41/L40-1:.2e}")

# ---------------- strong scale functions ----------------
def strong_scale(alpha_c, Mcut, content, defn, kappa=1.0):
    """Return strong scale in GeV for coupling alpha_c (MSbar, at mu = Mcut)."""
    loops = {"L1": 1, "L2": 2, "L4": 4, "MU1": 2}[defn]
    if content == "A":
        nf_low = 0; segs = []
    elif content == "B":
        nf_low = 6; segs = []
    elif content == "C":
        nf_low = 6; segs = [(kappa * Mcut, 12)] if kappa < 1 else []
    a, mu = alpha_c, Mcut
    for mu_low, nf in segs:
        a, _ = rg.run_alpha(a, mu, mu_low, nf, max(loops, 1))
        if a is None: return float('nan')
        mu = mu_low
    if defn == "MU1":
        m = rg.mu_where_alpha(a, mu, nf_low, 2, 1.0)
        return m if m is not None else float('nan')
    return rg.Lambda(mu, a, nf_low, loops)

def edge(Mcut, content, defn, target_ratio_to_MPl, kappa=1.0):
    f = lambda la: math.log(strong_scale(math.exp(la), Mcut, content, defn, kappa) / rg.M_PL) \
        - math.log(target_ratio_to_MPl)
    la = brentq(f, math.log(3e-3), math.log(0.3), xtol=1e-13)
    return FOURPI * math.exp(la)  # g^2

TV = rg.V_OBS / rg.M_PL
print(f"\nTarget T_v: Lambda*/M_Pl = {TV:.4e}; window W_v = [2.0e-18, 2.0e-16]")
bs = [1, 2, 5, 19, 35]
print("\n== W_v window in g^2(M_cut), MSbar at mu = M_cut ==")
print("content b    defn  g2(edge 2e-16)  g2(centre)  g2(edge 2e-18)  rel.width  g2(HIER-1 1e-15 of M_cut)")
store = {}
for content, kap in [("A", 1.0), ("B", 1.0), ("C", 0.3), ("C", 0.1)]:
    for b in bs:
        Mcut = rg.M_PL / b
        for defn in ["L1", "L2", "L4", "MU1"]:
            hi = edge(Mcut, content, defn, 2.0e-16, kap)
            ce = edge(Mcut, content, defn, TV, kap)
            lo = edge(Mcut, content, defn, 2.0e-18, kap)
            h1 = edge(Mcut, content, defn, 1e-15 / b, kap)
            store[(content, kap, b, defn)] = (lo, ce, hi, h1)
            lab = content if content != "C" else f"C(k={kap})"
            print(f"{lab:8s} {b:3d}  {defn:4s}  {hi:12.4f}  {ce:10.4f}  {lo:12.4f}  {(hi-lo)/ce:8.3f}  {h1:10.4f}")
# X2' with kappa = 1 is identical to B by construction:
check("X2' with mirrors exactly at the cutoff = SM-like colour content",
      abs(edge(rg.M_PL, "C", "L2", TV, 1.0) - store[("B", 1.0, 1, "L2")][1]) < 1e-12)

# loop/definition spread at b=1
for content, kap in [("A", 1.0), ("B", 1.0), ("C", 0.1)]:
    vals = [store[(content, kap, 1, d)][1] for d in ["L2", "L4", "MU1"]]
    print(f"spread of centre g2 over (L2, L4, MU1), content {content} k={kap}: "
          f"{min(vals):.4f}..{max(vals):.4f} ({(max(vals)-min(vals))/np.mean(vals)*100:.1f} %)")

# global upper edge of W_v over everything (largest g2 still inside the window)
gmax = max(v[2] for v in store.values())
print(f"\nLargest g^2(M_cut) inside W_v over all contents, b, definitions: {gmax:.4f} "
      f"(alpha = {gmax/FOURPI:.5f})")

# ---------------- pure-gauge windows in lattice schemes ----------------
print("\n== Pure SU(3): W_v edges in other schemes (b = 1), 2-loop ==")
r_L = 28.809   # Lambda_MS / Lambda_L (comparator, Hasenfratz-Hasenfratz 1980)
r_HK = r_L / 1.819  # Lambda_MS / Lambda_HK, using PR #9702 Lambda_HK/Lambda_W = 1.819
for name, r in [("MSbar", 1.0), ("Wilson bare", r_L), ("heat kernel", r_HK)]:
    # Lambda_scheme = Lambda_MS / r ; the scheme coupling at mu = M_cut gives Lambda_scheme
    # with the same 2-loop universal formula; physical Lambda_MS = r * Lambda_scheme.
    out = []
    for tgt in [2.0e-16, TV, 2.0e-18]:
        f = lambda la: math.log(r * rg.Lambda(rg.M_PL, math.exp(la), 0, 2) / rg.M_PL) - math.log(tgt)
        out.append(FOURPI * math.exp(brentq(f, math.log(3e-3), math.log(0.3), xtol=1e-13)))
    print(f"  {name:12s}: g2 in [{out[2]:.4f}, {out[0]:.4f}], centre {out[1]:.4f}; beta = 6/g2 in "
          f"[{6/out[0]:.1f}, {6/out[2]:.1f}]")

# ---------------- T_QCD (secondary): observed QCD at the cutoff ----------------
print("\n== T_QCD (secondary comparator): coupling at M_cut reproducing Lambda^(5) ==")
mt = 172.69
aem, s2w = 1 / 127.95, 0.23122
g1_MZ = math.sqrt(FOURPI * (5 / 3) * aem / (1 - s2w)); g2_MZ = math.sqrt(FOURPI * aem / s2w)
# one-loop SM run of g1, g2 from MZ to mt (tiny) for the initial point
def run1(g, b, mu0, mu1):
    return 1 / math.sqrt(1 / g ** 2 - 2 * b / (16 * math.pi ** 2) * math.log(mu1 / mu0))
g1_mt = run1(g1_MZ, 41 / 10, rg.M_Z, mt); g2_mt = run1(g2_MZ, -19 / 6, rg.M_Z, mt)
yt_mt = 0.934
print(f"  supplied comparators: alpha_em^-1(MZ)=127.95, s2w=0.23122, y_t(m_t)=0.934, m_t=172.69")
for L5 in [2.1, 0.21, 0.021]:
    aMZ5 = rg.alpha_from_Lambda(rg.M_Z, L5, 5, 2)
    a_mt, _ = rg.run_alpha(aMZ5, rg.M_Z, mt, 5, 2)
    row = [f"Lambda5={L5:6.3f} GeV: alpha_s(MZ)={aMZ5:.4f}"]
    for b in [1, 35]:
        Mcut = rg.M_PL / b
        a_qcd, _ = rg.run_alpha(a_mt, mt, Mcut, 6, 2)
        y = rg.run_sm(np.array([g1_mt, g2_mt, math.sqrt(FOURPI * a_mt), yt_mt]), mt, Mcut)
        g3sm = y[2] ** 2
        # X2': mirrors at 0.1 Mcut
        y1 = rg.run_sm(np.array([g1_mt, g2_mt, math.sqrt(FOURPI * a_mt), yt_mt]), mt, 0.1 * Mcut)
        y2 = rg.run_sm(y1, 0.1 * Mcut, Mcut, extra_gens=3.0)
        row.append(f"b={b}: g2 QCD-only {FOURPI*a_qcd:.4f}, SM 2-loop {g3sm:.4f}, X2'(k=0.1) {y2[2]**2:.4f}")
    print("  " + " | ".join(row))
aMZ_obs = 0.1180
a_mt, _ = rg.run_alpha(aMZ_obs, rg.M_Z, mt, 5, 2)
y = rg.run_sm(np.array([g1_mt, g2_mt, math.sqrt(FOURPI * a_mt), yt_mt]), mt, rg.M_PL)
print(f"  observed alpha_s(MZ)=0.1180 -> SM 2-loop g3(M_Pl) = {y[2]:.4f} (g2 = {y[2]**2:.4f}, "
      f"1/alpha3 = {FOURPI/y[2]**2:.2f}); main HIGGS_MASS_RETENTION:685 quotes 0.489")
check("T_QCD regression: g3(M_Pl) close to main's 0.489", abs(y[2] - 0.489) < 0.01, f"{y[2]:.4f}")
L6obs = rg.Lambda(rg.M_PL, y[2] ** 2 / FOURPI, 6, 2)
print(f"  the observed colour coupling at M_Pl gives Lambda^(6)/M_Pl = {L6obs/rg.M_PL:.3e} "
      f"(T_v needs {TV:.3e}): {math.log10(TV/(L6obs/rg.M_PL)):.2f} decades too weak for T_v")

# EW sensitivity of the T_v centre (content B, b = 1): run SM 2-loop with observed EW couplings
# from M_Pl down to 1e4 GeV with g3 at the QCD-only centre, then QCD-only Lambda^(6)
ce = store[("B", 1.0, 1, "L2")][1]
yPl = rg.run_sm(np.array([g1_mt, g2_mt, math.sqrt(FOURPI * a_mt), yt_mt]), mt, rg.M_PL)
yPl[2] = math.sqrt(ce)
ylow = rg.run_sm(yPl, rg.M_PL, 1e4)
Lew = rg.Lambda(1e4, ylow[2] ** 2 / FOURPI, 6, 2)
print(f"  EW/top two-loop sensitivity at the T_v centre: Lambda^(6)/M_Pl = {Lew/rg.M_PL:.3e} vs "
      f"{TV:.3e} (shift {math.log10(Lew/rg.M_PL/TV):+.3f} decades)")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
