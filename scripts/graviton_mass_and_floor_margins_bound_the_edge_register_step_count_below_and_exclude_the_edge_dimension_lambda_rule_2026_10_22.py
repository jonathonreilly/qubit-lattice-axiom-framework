AUDIT_INPUT_PATHS = ('docs/GRAVITON_MASS_AND_FLOOR_MARGINS_BOUND_THE_EDGE_REGISTER_STEP_COUNT_BELOW_AND_EXCLUDE_THE_EDGE_DIMENSION_LAMBDA_RULE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""register-size-s: can the edge-register step count s (and Delta) be fixed WITHOUT Lambda,
and is 2^-(4+Delta)s then the measured Lambda?

CL-1 edge register: length = flat x 2^(n/s - 3), n = 0..(4+Delta)s, window [L/8, 2^(1+Delta) L],
children born at n = 3s (length = flat), split at log-mean 2 x flat (mean value 4s).
Inputs used (no Lambda): graviton-mass bound, hbar c/L, the floor 1/8, alpha_c of J0740+6620 and of
the causal maximum-mass star, the heating cap eps0 < 0.026, Delta >= 1 (>= 2 with the trapped-shift cure).
Self-contained: numpy/scipy only.  Seeded (rng only for a random-state control).
"""
import math
import time
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq
from scipy.special import pbdv

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0
rng = np.random.default_rng(20261022)


def check(tag, ok, msg, det=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] [{tag}] {msg} | {det}")


# ------------------------------------------------------------------ M. measured / supplied numbers
LAM = 7.151e-121                    # Lambda L^2, L = sqrt(8 pi) l_P (Planck 2018) -- used ONLY in part D
BITS = math.log2(1 / LAM)           # 398.9
MG = 1.3e-23                        # eV, LIGO graviton-mass bound
HBARC_L = {"B (L = rung)": 2.435e27, "A (L = site)": 2 * 2.435e27}   # eV; reading A halves L
D_WEAK, A_J0740, A_CAUS = 7 / 8, (0.45, 0.55), 0.240
EPS_HEAT = 0.026
print("== M. inputs (no Lambda until part D)")
print(f"   m_g L < {MG / HBARC_L['B (L = rung)']:.2e} (B), {MG / HBARC_L['A (L = site)']:.2e} (A); floor 1/8; "
      f"alpha_c J0740 {A_J0740}, causal max {A_CAUS}; eps0 < {EPS_HEAT}")

# ------------------------------------------------------------------ A. pinning by the value lattice
print("== A. pinning: integer register values give the long-wavelength edge field a mass")
M = 70
nn = np.arange(-M, M + 1, dtype=float)


def ground(t, f):
    w, v = eigh_tridiagonal(0.5 * (nn - f) ** 2, -t * np.ones(2 * M), select="i", select_range=(0, 0))
    return w[0], v[:, 0]


rows = []
for t in np.linspace(0.6, 3.2, 9):
    e0, v0 = ground(t, 0.0)
    e5, _ = ground(t, 0.5)
    sig2 = float(np.sum(v0 ** 2 * nn ** 2))
    kpin = (2 * math.pi) ** 2 * abs(e5 - e0) / 2       # k_pin = (2 pi)^2 A,  k = 1
    rows.append((sig2, kpin))
S2 = np.array([r[0] for r in rows]); KP = np.array([r[1] for r in rows])
# Mathieu bandwidth ~ q^(3/4) e^(-4 sqrt q), q ~ sigma^4: prefactor (sigma^2)^(3/2)
c_fit, lnP = np.polyfit(S2[S2 > 0.5], np.log(KP[S2 > 0.5]) - 1.5 * np.log(S2[S2 > 0.5]), 1)
c_fit = -c_fit
check("T", abs(c_fit - 16) / 16 < 0.05,
      "A1 a register with quadratic phase (k/2)(n-f)^2 on integer n: E0(f) = E - A cos 2 pi f, the theta-circle "
      "instanton (Mathieu q = 8t/k, sigma_n^2 = sqrt(t/2k)) gives k_pin/k ~ exp(-16 sigma_n^2); exact tridiagonal "
      "ground states reproduce the slope",
      f"fitted slope {c_fit:.2f} (WKB 16) over sigma_n = {math.sqrt(S2.min()):.2f}..{math.sqrt(S2.max()):.2f}")


def sig_pin(mL):
    # m a = sqrt(k_pin/k) = sqrt(P sigma^3 exp(-c sigma^2))
    g = lambda x: lnP + 1.5 * math.log(x) - c_fit * x - 2 * math.log(mL)
    return math.sqrt(brentq(g, 0.5, 100))


SIGP = {k: sig_pin(MG / v) for k, v in HBARC_L.items()}
SIGP16 = math.sqrt(-2 * math.log(MG / HBARC_L["B (L = rung)"]) / 16)
check("E", all(3.5 < x < 4.1 for x in SIGP.values()),
      "A2 ESTIMATE: the graviton-mass bound needs every register's zero-point spread sigma_n >= sigma_pin steps "
      "(block edges: mass per block length moves it by < 0.05)",
      "; ".join(f"{k}: {v:.2f}" for k, v in SIGP.items()) + f"; bare e^(-8 sigma^2): {SIGP16:.2f}; hop-recheck D3 quoted 3.79")
SIG_PIN = SIGP["B (L = rung)"]

# ------------------------------------------------------------------ B. wall margin
print("== B. a hard wall t spreads away: edge-local mass")


def nu_exact(t):
    # oscillator H = -1/2 d2 + y^2/2, wall at y = Y, |psi|^2 spread 1/sqrt2, t = sqrt2 Y; ground: D_nu(-t) = 0
    g = lambda lv: pbdv(math.exp(lv), -t)[0]
    return math.exp(brentq(g, -60, math.log(0.999)))


def nu_asym(t):
    return t * math.exp(-t * t / 2) / math.sqrt(2 * math.pi)


rat = [(t, nu_exact(t) / nu_asym(t)) for t in (3.0, 4.0, 5.0, 6.0)]
check("T", abs(rat[-1][1] - 1) < 0.05,
      "B1 ground-energy shift of a mode with a hard wall t zero-point spreads away: exact D_nu(-t) = 0 against "
      "nu = t e^(-t^2/2)/sqrt(2 pi) (ratio -> 1)", "; ".join(f"t {a:.0f}: {b:.3f}" for a, b in rat))


def t_wall(mL):
    # wall potential V(d) = hbar w nu(d/sigma); its curvature over the mode stiffness hbar w/(2 sigma^2) = 2 nu''(t)
    f = lambda t: 0.5 * (math.log(2 * (t ** 3 - 3 * t) / math.sqrt(2 * math.pi)) - t * t / 2) - math.log(mL)
    return brentq(f, 3, 60)


TW = {k: t_wall(MG / v) for k, v in HBARC_L.items()}
T_WALL = TW["B (L = rung)"]
check("E", all(20 < x < 24 for x in TW.values()),
      "B2 ESTIMATE: m a = sqrt(2 nu''(t)) below the graviton-mass bound needs every wall >= t_wall spreads away",
      "; ".join(f"{k}: {v:.1f}" for k, v in TW.items()) + "; edge-block B2 (Weiss/RPA, log register) 22.0")

# ------------------------------------------------------------------ C. the allowed (s, Delta) region
print("== C. the allowed (s, Delta) region from pinning + walls + floor (no Lambda)")
# absolute zero-point spread of a block edge = s1 L (edge-block B0, any b); step at length l = l ln2/s
#  pinning at the split (l = 2 b L, sparsest values of the cosmic cycle): s1 s/(2 b ln2) >= sigma_pin
#  floor margin (child at b L in weak fields, alpha_c b L in a core at the worst far phase): d b >= t s1
LN2 = math.log(2)


def s_min(d, s1):
    b = T_WALL * s1 / d
    return 2 * LN2 * SIG_PIN * b / s1, b


lines = []
same = True
for s1 in (0.2, 0.4):
    vals = [s_min(D_WEAK, s1), s_min(A_J0740[1] - 1 / 8, s1), s_min(A_J0740[0] - 1 / 8, s1), s_min(A_CAUS - 1 / 8, s1)]
    lines.append(f"s1 {s1}: " + ", ".join(f"b {b:.1f} s {s:.0f}" for s, b in vals))
    same &= abs(vals[0][0] - s_min(D_WEAK, 0.2)[0]) < 1e-9
check("T", same,
      "C1 THEOREM (given A2, B2): s >= 2 ln2 sigma_pin t_wall / d, with d the floor distance in flat units; the "
      "unknown spread normalisation s1 and the block size b_e cancel, so the bound is reading-independent "
      "(weak field d = 7/8; J0740 d = 0.55-1/8 .. 0.45-1/8; causal max-mass d = 0.115)", " ; ".join(lines))
S_W, S_J1, S_J0, S_C = (s_min(d, 0.2)[0] for d in (D_WEAK, A_J0740[1] - 1 / 8, A_J0740[0] - 1 / 8, A_CAUS - 1 / 8))
S_MOVE = 0.85 / math.sin(EPS_HEAT)
check("E", S_W > S_MOVE,
      "C2 the moving bound s >= 0.85/sin eps0 (>= 32.7 at the heating cap) is weaker than the pinning bound; "
      "the split trigger at mean value 4s and the 3s birth value are integer for every s (no constraint)",
      f"s_min: moving {S_MOVE:.1f}, weak field {S_W:.1f}, J0740 {S_J1:.0f}..{S_J0:.0f}, causal max-mass {S_C:.0f}")
dmarg = [math.log2(1 + d / 2) for d in (D_WEAK, A_J0740[0] - 1 / 8)]
check("T", max(dmarg) < 1,
      "C3 the top-wall margin (gap H5) Delta s >= t_wall sigma_n at the split reads Delta >= log2(1 + t s1/(2b)) = "
      "log2(1 + d/2) at the floor-limited b: s cancels again, and Delta >= 1 (post-crunch exterior) already "
      "satisfies it; Delta >= 2 with the trapped-shift cure", f"needed Delta: weak {dmarg[0]:.2f}, J0740 {dmarg[1]:.2f}")
strong = {D: S_W * 2 ** D for D in (1, 2, 3)}
check("E", True,
      "C4 ESTIMATE (strong-field variant): radially stretched exterior edges reach 2^(1+Delta) b L; keeping them "
      "unpinned there multiplies the bound by 2^Delta", ", ".join(f"Delta {k}: s >= {v:.0f}" for k, v in strong.items()))
budget = []
for s1 in (0.2, 0.4):
    coef = 2 * LN2 * SIG_PIN / s1
    budget.append(f"s1 {s1}: s = {coef:.1f} b_e, b_e >= {math.sqrt(12 * 5 * coef / 0.8):.0f}, s >= {coef * math.sqrt(12 * 5 * coef / 0.8):.0f}")
check("E", True,
      "C5 ESTIMATE: the register site budget 12(4+Delta)s/b_e^3 <= 0.8 per cell (block-hierarchy) is only an "
      "upper bound on s at given b_e, and b_e is free above, so no upper bound on s follows: s is NOT fixed, "
      "only bounded below", " ; ".join(budget) + " (Delta = 1)")
# dispersion smoothness beyond pinning
kL = 2 * math.pi / 3.0e6 * 8.1e-35 * 40
check("E", kL ** 2 < 1e-70,
      "C6 ESTIMATE: with dressed weights and sigma_n >= sigma_pin, the value lattice enters GW dispersion only "
      "through the pinning mass (A2) and lattice terms (k b_e L)^2; uniform dilations are exact whole shifts; "
      "collinear-shift deficits (sigma_n ln2/s)^2 = (s1/2b)^2 are s-independent: no further bound on s",
      f"(k b_e L)^2 at LIGO, b_e 40: {kL ** 2:.1e}")

# ------------------------------------------------------------------ D. the edge-dimension rule against the region
print("== D. Lambda L^2 = 2^-(4+Delta)s against the region (Lambda used here only)")
hit = {D: BITS / (4 + D) for D in range(0, 4)}
check("T", all(hit[D] < S_W for D in hit),
      "D1 the rule needs s = 398.9/(4+Delta) <= 80 for Delta >= 1, below the weak-field bound alone: the "
      "s ~ 57-100 hits are outside the allowed region", ", ".join(f"Delta {D}: s* {v:.1f}" for D, v in hit.items()))
pred = []
for D in (1, 2):
    for lab, s in (("weak", math.ceil(S_W)), ("J0740", math.ceil(S_J1))):
        lg = -(4 + D) * s * math.log10(2)
        pred.append(f"D{D} {lab} s {s}: <= 1e{lg:.0f} ({lg - math.log10(LAM):.0f} dec)")
check("E", True,
      "D2 PREDICTION at the smallest allowed s: Lambda L^2 <= 2^-(4+Delta)s_min, far below the measured value: a "
      "miss, not a prediction", " ; ".join(pred))
menu = {"1(octave)": 1, "3(floor-birth)": 3, "4": 4, "5(4+D,D=1)": 5, "6(D=2)": 6, "10(register)": 10, "60(block-site)": 60}
mrows = []
ok_menu = True
for name, c in menu.items():
    s = BITS / c
    tag = "J0740 ok" if s >= S_J0 else ("weak ok" if s >= S_W else "out")
    name = name.split(" ")[0]
    mrows.append(f"c={name}: s {s:.0f} {tag}")
ok_menu = abs(BITS / 3 / S_W - 1) < 0.1 and BITS / 3 < S_J1 and BITS >= S_J0 and BITS < S_C
check("E", ok_menu,
      "D3 LOOK-ELSEWHERE: other bit counts c per end; s is only bounded below, so any c <= 398.9/s_min fits at "
      "s = 398.9/c (chance 1); c = 3 lands at the weak-field bound (log coincidence: s_min ~ sqrt2 ln2 ln(1/m_g L)/d), "
      "excluded by J0740; c = 1 survives J0740, not the causal max-mass bound",
      " ; ".join(mrows) + f" ; 3 s_min(weak) = {3 * S_W:.0f}")

# ------------------------------------------------------------------ E. law-level justification of a 1/dimension phase
print("== E. is a phase per 4-volume = 1/(Fock dimension of an end) a law?")
N = 8
dim = 2 ** N
psi_u = np.ones(dim) / math.sqrt(dim)                     # uniform odds
cfg = int(rng.integers(dim))
p_cfg = abs(psi_u[cfg]) ** 2
psi_d = rng.normal(size=dim) + 1j * rng.normal(size=dim); psi_d /= np.linalg.norm(psi_d)
resp_vac = p_cfg - abs(psi_u[cfg]) ** 2
resp_dep = abs(psi_d[cfg]) ** 2 - p_cfg
binom_sum = sum(math.comb(N, k) for k in range(N + 1))
check("T", abs(p_cfg - 2.0 ** -N) < 1e-15 and resp_vac == 0 and abs(resp_dep) > 0 and binom_sum == dim,
      "E1 uniform odds give every end configuration weight 2^-N, but CL-3 responds only to departures from the "
      "vacuum of the same edges: a vacuum-share 2^-N cancels exactly (response 0 in the vacuum, nonzero only on "
      "departures), so the rule cannot arise as a response; the length reads n only (N+1 values, C(N,n) "
      "configurations each), so 1/(readable dimension) = 1/(N+1) ~ 1e-3",
      f"N {N}: weight {p_cfg:.3e}, vacuum response {resp_vac:.1e}, departure response {resp_dep:.2e}, sum C(N,n) = {binom_sum}")
check("E", True,
      "E2 normalisation ambiguity: per end (N bits), per register (2N), per block site (12N); per cell 4-volume or "
      "per block 4-volume (factor b_e^4); the CL text fixes none of these, so 'one end per cell 4-volume' is a choice",
      f"log2 b_e^4 at b_e 40: {4 * math.log2(40):.1f} bits of 398.9")
print("theorems: A1, B1, C1, C3, D1, E1; estimates: A2, B2, C2, C4-C6, D2, D3, E2")
print("supplied: m_g < 1.3e-23 eV, hbar c/L (readings A/B), floor 1/8, alpha_c (J0740, causal), eps0 < 0.026, "
      "Delta >= 1 (>= 2 cure), s1 (cancels), budget 0.8/cell; Lambda only in part D")
print(f"runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
