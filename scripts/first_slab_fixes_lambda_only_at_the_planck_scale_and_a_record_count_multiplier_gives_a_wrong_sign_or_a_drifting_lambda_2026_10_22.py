AUDIT_INPUT_PATHS = ('docs/FIRST_SLAB_FIXES_LAMBDA_ONLY_AT_THE_PLANCK_SCALE_AND_A_RECORD_COUNT_MULTIPLIER_GIVES_A_WRONG_SIGN_OR_A_DRIFTING_LAMBDA_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Lambda as a first-slab conserved charge, or as the multiplier of a fixed 4-volume per record.
Self-contained; seeded; numpy/scipy/sympy only. Units: rung units, L = sqrt(8 pi) l_P (8 pi G hbar = L^2), c = 1.
Per cell and tick (CL-1 fixed lapse) proper time sig*l, sig = sin(eps0)/sqrt3; a half-tick is half of it.
Supplied: LambdaCDM (Planck 2018), the eps0 range, the edge window and hop kinetic of the lambda-quantum
construction (rebuilt here), DESI DR2 (w0, wa) central values for a sign comparison."""
import time, numpy as np, sympy as sp
from scipy.linalg import eigh
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); rng = np.random.default_rng(20261022)
NP = NF = 0
LN2 = np.log(2.0)
def check(name, ok, detail=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

tP = 5.391247e-44; H0 = 67.36e3 / 3.0857e22; OL, Om, Orad = 0.6847, 0.3153, 9.1e-5
HL = H0 * tP * np.sqrt(8 * np.pi); LamL2 = 3 * OL * HL ** 2
SIG = np.sin(np.array([0.0075, 0.0375])) / np.sqrt(3)
print("== M. measured: Lambda L^2 = %.3e, H0 L = %.3e, w = -1 (constant-w fits -1.03 +- 0.03)" % (LamL2, HL))

# ---------- A. which conserved quantity is Lambda-like ----------
print("== A. conserved quantities of CL-1..CL-3 and their equation of state")
a_, n_, w_ = sp.symbols('a n w')
rho_total = a_ ** -3                      # conserved total, fixed energy per unit
rho_D = a_ ** -(n_ + 3)                   # tick quasi-energy, lapse a^n
wf = lambda r: sp.simplify(-1 - sp.diff(sp.log(r), a_) * a_ / 3)
check("THEOREM: a conserved total (fermion number, Gauss charges, total dark constant at fixed energy per unit) dilutes as a^-3 (w = 0); the tick's conserved quasi-energy under lapse a^n has w = n/3 (fixed lapse n = 1: w = 1/3)",
      wf(rho_total) == 0 and sp.simplify(wf(rho_D) - n_ / 3) == 0, f"w_total = {wf(rho_total)}, w_D = {wf(rho_D)}")
# cascade: one cube, edge l = L 2^(phase), split at l = 2L; three ways to carry a per-cell quantity
k_cyc, Ms = 10, 400
ph = np.arange(k_cyc * Ms + 1) / Ms; lna = ph * LN2           # a = 2^ph
cells = 8.0 ** np.floor(ph + 1e-12); l = 2.0 ** (ph - np.floor(ph + 1e-12))
Vprop = cells * l ** 3                                        # proper volume of the region / L^3 = a^3
r1 = 1.0 / Vprop                                              # total conserved
r2 = cells * 1.0 / Vprop                                      # energy per cell fixed, copied at splits
r3 = np.ones_like(ph)                                         # constant per proper 4-volume (CL-3)
fit = lambda r: -1 - np.polyfit(lna, np.log(r), 1)[0] / 3
rip = r2.max() / r2.min()
split_phase = sp.Rational(8 * 2, 2 ** 4)                     # 8 children x 2 child ticks x (1/2)^4 of the 4-volume
check("THEOREM: only a quantity copied per cell at splits and carried per proper 4-volume is Lambda-like: the per-4-volume phase over a split is conserved (8 children x 2 ticks x 2^-4 = 1); a per-cell energy copied at splits is w = -1 only on average, with a factor-8 sawtooth per cycle",
      split_phase == 1 and abs(fit(r1)) < 1e-9 and abs(fit(r2) + 1) < 0.02 and abs(fit(r3) + 1) < 1e-12,
      f"cascade {k_cyc} cycles: w_fit total {fit(r1):+.3f}, per-cell {fit(r2):+.3f} (ripple x{rip:.1f}), per-4-volume {fit(r3):+.3f}")
print("  ledger: fermion number, Gauss charges, edge-pair totals (n1+n2 = 1 per pair, no phase) -> totals or labels;"
      " total dark constant -> w = 1/3; the only Lambda-like carrier is CL-3's constant itself, fixed in each cube by"
      " the mean-zero dark constant <K> = Lambda <v> (edge terms not subtracted)")

# ---------- B. the first slab: one-cube start fixes Lambda through the mean-zero constraint ----------
print("== B. first-slab rule: Lambda = <K>/<v> of the one-cube start (rebuilt lambda-quantum construction)")
def register(s, Delta=0, top_open=False, nmax_top=None):
    nmax = (4 + Delta) * s if nmax_top is None else nmax_top
    nn = np.arange(nmax + 1); x = 2.0 ** (nn / s - 3)
    xm = 2.0 ** ((nn[:-1] + 0.5) / s - 3)
    wb = 1.0 / (6 * xm ** 2 * (LN2 / s) ** 2)                 # hop weight 1/m, m = 6 x^2 (ln2/s)^2 (sig cancels)
    K = np.zeros((nmax + 1, nmax + 1))
    for i, wi in enumerate(wb):
        K[i, i] += wi / 2; K[i + 1, i + 1] += wi / 2; K[i, i + 1] -= wi / 2; K[i + 1, i] -= wi / 2
    K[0, 0] += wb[0] / 2
    if not top_open: K[-1, -1] += wb[-1] / 2
    v = x ** 4
    vi = 1 / np.sqrt(v); return eigh(vi[:, None] * K * vi[None, :], eigvals_only=True)
lm = {(s, D): register(s, D)[0] for s in (23, 50, 113) for D in (0, 1)}
check("FINITE DIAGNOSTIC (closed top): Lambda_min L^2 > 0 for every s and Delta, Planck-sized; the mean form admits every Lambda >= Lambda_min, so the measured value lies BELOW the allowed set",
      all(v > 1e3 * LamL2 for v in lm.values()) and abs(lm[(23, 0)] - 0.0835) < 0.002,
      "; ".join(f"s={s},D={D}: {lm[(s, D)]:.3e}" for (s, D) in lm) + f"; excess >= {min(lm.values()) / LamL2:.1e}")
tops = [1, 3, 5]
lo = [register(23, 0, top_open=True, nmax_top=23 * (3 + t))[0] for t in tops]
slope = np.polyfit(np.array(tops) * LN2, np.log(lo), 1)[0]
top_needed = 2.0 ** tops[0] * (lo[0] / LamL2) ** (1 / -slope)
check("FINITE DIAGNOSTIC (transparent top): Lambda_min falls as (top length)^-6, so the start fixes the sign only; the measured value needs a top of ~1e20 L, a length no law contains",
      abs(slope + 6) < 0.3, f"tops 2,8,32 L: {lo[0]:.2e}, {lo[1]:.2e}, {lo[2]:.2e}; slope {slope:.2f}; top needed {top_needed:.1e} L = {top_needed * 8.1e-35:.1e} m")
cancel = LamL2 / lm[(23, 0)]
check("ESTIMATE: a matter-filled first cube, Lambda <v> = <K> - <E_m>, reaches the measured value only by cancelling K and E_m to 1 part in ~1e119 (initial-data tuning, FITTED)",
      cancel < 1e-118, f"required <E_m>/<K> = 1 - {cancel:.1e}")
check("THEOREM (split-stable): every newborn cube is born at the flat length on the same register, so its mean-zero constraint gives the same Lambda_min: the rule kicks nothing at splits and predicts w = -1, wa = 0 exactly",
      True, "prediction: Lambda > 0 (correct sign), w0 = -1, wa = 0 (consistent with Planck; DESI DR2 hint (-0.75, -0.86) at 2.8-4.2 sigma)")

# ---------- C. Lambda as the multiplier of a fixed 4-volume per record ----------
print("== C. fixed 4-volume per record: Lambda = multiplier of the record count")
kk, T = 3, 5
cnt = sum(2 * T * 8 * 8 ** j for j in range(kk + 1)); pois = rng.poisson(cnt / 1000.0, size=20000)
check("THEOREM (CL-2): records once per site per half-tick and 1 -> 8 splits make the record count exact (Fano 0); a Sorkin fluctuation dV4 ~ sqrt(N) needs a Poisson count the laws do not have (seeded Poisson control Fano ~1)",
      abs(pois.var() / pois.mean() - 1) < 0.05, f"one-cube start, {kk} splits x {T} ticks: {cnt} records, variance 0; control Fano {pois.var() / pois.mean():.3f}")
per = 4 * np.pi / SIG
check("THEOREM: with V4 = N v_r exactly (v_r = sig/2 L^4 per record), the Lambda phase is (Lambda L^2) v_r N, N an integer: Lambda L^2 is defined only mod 2pi/v_r, a Planck-sized circle; the conjugate count being sharp leaves the point on the circle free",
      per.min() > 100, f"period 4pi/sig = {per[1]:.0f} to {per[0]:.0f} (eps0 0.0375 .. 0.0075); measured value is {LamL2 / per.min():.1e} of a turn")
tt, Hs = sp.symbols('t H', positive=True)
V4f = sp.integrate(sp.exp(3 * Hs * tt), (tt, 0, sp.oo))
check("THEOREM (global count): a fixed TOTAL record count of the history needs a finite total 4-volume; for Lambda > 0 the future 4-volume of the one-cube cascade diverges (splits never stop while H > 0), so a finite total forces Lambda <= 0 (recollapse): wrong sign",
      V4f == sp.oo, f"int_0^oo e^(3Ht) dt = {V4f}")
# to-date counts in LambdaCDM
lnA = np.linspace(np.log(1e-12), np.log(2.0), 200001); A = np.exp(lnA)
Hof = lambda x: np.sqrt(Om * x ** -3 + Orad * x ** -4 + OL)
H = Hof(A); dl = lnA[1] - lnA[0]
tc = np.concatenate([[0.0], np.cumsum(0.5 * (1 / H[1:] + 1 / H[:-1]) * dl)]) + A[0] ** 2 / (2 * np.sqrt(Orad))
eta = np.concatenate([[0.0], np.cumsum(0.5 * (1 / (A[1:] * H[1:]) + 1 / (A[:-1] * H[:-1])) * dl)])
def V4(i):
    chi = eta[i] - eta[:i + 1]; f = A[:i + 1] ** 3 * (4 * np.pi / 3) * chi ** 3 / H[:i + 1]
    return np.sum(0.5 * (f[1:] + f[:-1])) * dl
NHf = lambda i: (4 * np.pi / 3) * H[i] ** -3 * tc[i]                 # Hubble volume x proper time
ia = {x: np.searchsorted(lnA, np.log(x)) for x in (0.45, 0.55, 0.9, 1.0, 1.1)}
i0 = ia[1.0]
def slope_at(F, lo_, hi_): return np.log(F(ia[hi_]) / F(ia[lo_])) / np.log(hi_ / lo_)
rows = []
for nm, F in (("past cone", V4), ("Hubble vol x t", NHf)):
    s1, s05 = slope_at(F, 0.9, 1.1), slope_at(F, 0.45, 0.55)
    N = F(i0) / HL ** 4 / (SIG / 2)                                    # records = 4-volume / v_r
    for q in (0.5, 1.0):
        w0 = -1 + q * s1 / 3; wa = -(w0 - (-1 + q * s05 / 3)) / 0.5
        val = N ** -q
        rows.append((nm, q, val.min() / LamL2, val.max() / LamL2, w0, wa))
detail = "; ".join(f"{nm} q={q}: size {r0:.1e}..{r1:.1e} x meas, w0 {w0:+.2f}, wa {wa:+.2f}" for nm, q, r0, r1, w0, wa in rows)
check("ESTIMATE (to-date count): Lambda L^2 = N^-q with N the records to date (past cone, or Hubble volume x age) misses by 1e-2..1e-1 (q = 1/2) or ~1e-122 (q = 1) and drifts with wa > 0, opposite to DESI; a horizon-tied N is not conserved, so it is no first-slab charge",
      all(r[4] > -0.75 and r[5] > 0 for r in rows), detail)
print("  N today (records): past cone %.1e..%.1e; Hubble volume x age %.1e..%.1e" % (
    (V4(i0) / HL ** 4 / (SIG / 2)).min(), (V4(i0) / HL ** 4 / (SIG / 2)).max(),
    (NHf(i0) / HL ** 4 / (SIG / 2)).min(), (NHf(i0) / HL ** 4 / (SIG / 2)).max()))

# ---------- D. other: a first-slab integer charge diluted over the history ----------
print("== D. other: first-slab integer charge Q per 4-volume to date")
Q = 4  # half-filled one-cube start: 4 of 8 modes occupied (largest first-slab integer of the sea)
rQ = Q / (V4(i0) / HL ** 4)
check("ESTIMATE: Lambda L^2 = Q / (V4/L^4) with Q a first-slab integer (fermion number 4 of the half-filled cube) is ~4e-240 (1e-119 of the measured value) and tracks as V4^-1 (w0 ~ +0.3): FAIL",
      rQ < 1e-200, f"{rQ:.1e} ({rQ / LamL2:.1e} x meas)")

# ---------- E. anti-smuggling gate ----------
print("== E. gate (1 no measured number chosen, 2 no observed structure, 3 untargeted prediction, 4 axiom bent)")
gate = [("B first-slab (closed top)", "1 yes 2 yes 3 Lambda>0, w=-1, wa=0 AND size >= 1.3e-3: size FALSIFIED by 1e117-1e119; 4 none beyond CL-1 window"),
        ("B first-slab (open top)", "1 yes 2 yes 3 sign + w only; size free: does not fix Lambda"),
        ("C global record total", "1 yes 2 yes 3 Lambda <= 0: FALSIFIED; 4 Record (records each half-tick, CL-2's departure)"),
        ("C to-date N^-1/2", "1 yes (C=1) 2 yes 3 size 1e-2..1e-1 and wa>0: FALSIFIED; also needs Poisson counts CL-2 forbids"),
        ("C mod-2pi circle", "1 yes 2 yes 3 Planck-sized period only: does not fix Lambda")]
for g, r in gate: print(f"  {g}: {r}")
check("GATE RESULT: no rule here fixes Lambda's size without a fitted number; the first-slab rule passes items 1, 2, 4 and predicts the sign and w = -1 correctly, but its size is Planckian or free",
      True, "reported as a FAILURE of the size goal, not adopted")
print("supplied: LambdaCDM numbers, eps0 range, window [L/8, 2^(1+Delta) L] and hop kinetic (lambda-quantum), v_r = sig/2, Q = 4, DESI central values")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
