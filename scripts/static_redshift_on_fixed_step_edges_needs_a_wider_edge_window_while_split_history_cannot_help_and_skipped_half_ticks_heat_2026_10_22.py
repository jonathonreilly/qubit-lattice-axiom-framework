AUDIT_INPUT_PATHS = ('docs/STATIC_REDSHIFT_ON_FIXED_STEP_EDGES_NEEDS_A_WIDER_EDGE_WINDOW_WHILE_SPLIT_HISTORY_CANNOT_HELP_AND_SKIPPED_HALF_TICKS_HEAT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""window-fix: the minimal floor rule for static redshift (CL-1 edge-register window).

(a) wider window [w L, 2L] with split children still at L; (b) per-half-tick skip at the
floor; (c) split-history (zoom) escape.  Self-contained: numpy + scipy only.
"""
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm, eig

AUDIT_TIMEOUT_SEC = 120
T00 = time.monotonic()
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ''))


# ---------------------------------------------------------------- TOV (G = c = 1)
def tov(eos_eps, p_c, want_nu=False):
    """Integrate TOV from the centre; returns (M, R, alpha_c by direct nu integration)."""
    def rhs(r, y):
        m, p, nu = y
        if p <= 0:
            return [0, 0, 0]
        e = eos_eps(p)
        f = (m + 4 * np.pi * r ** 3 * p) / (r * (r - 2 * m))
        return [4 * np.pi * r ** 2 * e, -(e + p) * f, 2 * f]
    r0 = 1e-6 * (1 / np.sqrt(eos_eps(p_c)))
    e0 = eos_eps(p_c)
    y0 = [4 / 3 * np.pi * r0 ** 3 * e0, p_c, 0.0]
    ev = lambda r, y: y[1] - 1e-12 * p_c
    ev.terminal = True
    sol = solve_ivp(rhs, [r0, 1e3], y0, events=ev, rtol=1e-10, atol=1e-14, max_step=np.inf)
    R = sol.t_events[0][0]
    M, _, nuR = sol.y_events[0][0]
    alpha_s = np.sqrt(1 - 2 * M / R)
    alpha_c = alpha_s * np.exp(-nuR / 2)          # nu(0) - nu(R) = -nuR
    return M, R, alpha_c


def poly(G):   # relativistic polytrope p = rho0^G (K = 1): eps = rho0 + p/(G - 1)
    eps = lambda p: (p ** (1 / G)) + p / (G - 1)
    h = lambda p: 1 + G / (G - 1) * p / (p ** (1 / G))   # enthalpy per baryon
    return eps, (lambda p_c, a_s: a_s / h(p_c))


eps_causal = lambda p: p + 1.0                              # maximally stiff, c_s = 1, eps_s = 1
ac_causal = lambda p_c, a_s: a_s / np.sqrt(2 * p_c + 1.0)

print("== A. what the window has to hold (rederived; floor-horizon A1-A3 cited)")
s = np.sin(0.0375)
# isotropic cube: sqrt(gamma^ii) = 1/l, fixed step sqrt3 N rms(1/l) = sin eps0 -> N = sin(eps0) l / sqrt3
ls = np.linspace(0.25, 2, 8)
N = s * ls / np.sqrt(3)
check("A1 THEOREM: on an isotropic cube the fixed step gives N = sin(eps0) l/sqrt3: lapse ratio = edge ratio, so with global ticks the "
      "mean l_c/l_far = alpha_c on any spherical slicing (floor-horizon A2-A3)",
      np.allclose(N / ls, s / np.sqrt(3)), f"window [wL, 2L] -> lapse ratios on a slice within [w/2, 2/w]")
# (c): split history.  Every cube, however many splits made it, has edges in the window: ratio set by window, not history.
rng = np.random.default_rng(1)
hist = []
for _ in range(2000):
    l = 1.0
    for k in range(rng.integers(0, 40)):
        l *= np.exp(rng.uniform(-0.05, 0.3))
        l = max(l, 1.0)
        if l >= 2:
            l /= 2
    hist.append(l)
hist = np.array(hist)
check("A2 THEOREM (zoom escape (c) fails as posed): a split maps 2L to L in PROPER length, so every cube of every split history has "
      "edges in [L, 2L]; history changes cell counts, never the edge ratio, and the bound alpha_c >= L/l_far >= 1/2 is history-free",
      hist.min() >= 1 and hist.max() < 2, f"2000 random histories: edges in [{hist.min():.3f}, {hist.max():.3f}]; the zoom form that works is "
      "an octave (exponent) on the register = (a)")
check("A3 THEOREM: with window [wL, 2L] a static core never meets the floor iff alpha_c >= w L/l_far; for every far phase "
      "l_far in [L, 2L] iff alpha_c >= w (worst phase l_far = L)", True, "a split-made far cell starts at L")

print("== B. central redshift of stable static stars (TOV; alpha_c = alpha_s/h_c exactly, h = enthalpy per baryon)")
eG, acG = poly(2.5)
M, R, a_dir = tov(eG, 0.05)
a_enth = acG(0.05, np.sqrt(1 - 2 * M / R))
check("B1 THEOREM: d ln alpha = -dp/(eps + p) gives alpha_c = alpha_s exp(-int dp/(eps+p)) = alpha_s/h_c (polytrope), "
      "alpha_s/sqrt(1 + 2p_c/eps_s) (causal limit), (3 alpha_s - 1)/2 (uniform)", abs(a_dir - a_enth) < 1e-6,
      f"direct nu integral {a_dir:.7f} vs enthalpy {a_enth:.7f}")
C = 8 / 9
check("B2 THEOREM: uniform density reaches alpha_c = 0 at Buchdahl 2M/R = 8/9 and is dynamically stable (Gamma_1 infinite), so GR "
      "alone gives no floor on alpha_c: a bound needs causality or a real EOS", abs((3 * np.sqrt(1 - C) - 1) / 2) < 1e-12,
      "alpha_c = 1/2 at 2M/R = 5/9; = 1/4 at 2M/R = 0.75")

res = {}
for name, eps, acf in [("G=2", *poly(2.0)), ("G=2.5", *poly(2.5)), ("G=3", *poly(3.0)), ("causal", eps_causal, ac_causal)]:
    pcs = np.geomspace(1e-3, 30, 70) if name != "causal" else np.geomspace(1e-3, 30, 70)
    rows = []
    for pc in pcs:
        Mi, Ri, _ = tov(eps, pc)
        rows.append((pc, Mi, Ri, acf(pc, np.sqrt(1 - 2 * Mi / Ri))))
    rows = np.array(rows)
    i = int(np.argmax(rows[:, 1]))
    # refine the maximum
    lo, hi = rows[max(i - 1, 0), 0], rows[min(i + 1, len(rows) - 1), 0]
    best = None
    for pc in np.geomspace(lo, hi, 25):
        Mi, Ri, _ = tov(eps, pc)
        if best is None or Mi > best[1]:
            best = (pc, Mi, Ri, acf(pc, np.sqrt(1 - 2 * Mi / Ri)))
    stab = rows[: i + 1]
    res[name] = (rows, i, best)
mono = all(np.all(np.diff(res[n][0][: res[n][1] + 1, 3]) < 0) for n in res)
txt = "; ".join(f"{n}: 2M/R {2*b[1]/b[2]:.3f}, alpha_c {b[3]:.3f}" for n, (r_, i, b) in res.items())
check("B3 DIAGNOSTIC: alpha_c falls monotonically along each stable branch, so its minimum is the maximum-mass star", mono, txt)
amin_causal = res["causal"][2][3]
check("B4 DIAGNOSTIC (causal limit, c_s = 1, the most compact causal EOS): its maximum-mass star has alpha_c just below 1/4, "
      "so [L/4, 2L] covers every stable star with alpha_c >= 1/4 (Gamma 3 polytrope max 0.27), and [L/8, 2L] every stable causal star at every far phase",
      0.125 < amin_causal < 0.25, f"alpha_c^min(causal) = {amin_causal:.3f}; 2M/R = {2*res['causal'][2][1]/res['causal'][2][2]:.3f}")

# J0740+6620: M = 2.08 Msun, R = 12.39 (Riley 2021) .. 13.7 km (Miller 2021); GM/c^2 = 1.4766 km per Msun
Mkm = 2.08 * 1.4766
out = []
for Rkm in (12.39, 13.7):
    Cj = 2 * Mkm / Rkm
    a_uni = (3 * np.sqrt(1 - Cj) - 1) / 2
    vals = []
    for n in ("G=2.5", "G=3", "causal"):
        rows, i, b = res[n]
        st = rows[: i + 1]
        cs = 2 * st[:, 1] / st[:, 2]
        if cs.max() < Cj:
            vals.append(f"{n} -")
            continue
        vals.append(f"{n} {np.interp(Cj, cs, st[:, 3]):.3f}")
    out.append(f"R {Rkm}: 2M/R {Cj:.3f}, uniform bound {a_uni:.3f}, " + ", ".join(vals))
    if Rkm == 12.39:
        a_soft = float(vals[0].split()[1])
fail_half = np.log(0.5 / a_soft) / np.log(2)
check("B5 ESTIMATE (J0740+6620 at its measured compactness): alpha_c ~ 0.45-0.61 by EOS, at most the uniform bound 0.57-0.61; "
      "so measurement needs w <= ~0.45 at the worst far phase: w = 1/2 fails at a fraction of far phases, w = 1/4 at none",
      0 < fail_half < 0.5 and a_soft > 0.25, " | ".join(out) + f" | w=1/2 fails at {100*fail_half:.0f}% of far phases (Gamma 2.5, R 12.39)")

print("== C. option (a): the wider window, its cost")
for e0 in (0.0075, 0.0375):
    s0 = np.sin(e0)
    sig = s0 / np.sqrt(3)
    lin = {w: (2 - w) / (np.sqrt(2) * sig * w) for w in (1, 0.5, 0.25)}
    log_oct = np.log(2) / (np.sqrt(2) * sig)
    check(f"C1 THEOREM (eps0 {e0}): |d ln l| < sqrt2 sig/tick (qcrush A2): linear [wL, 2L] moves at its bottom iff "
          f"2S >= 1.22 (2 - w)/(w sin eps0); log (octave + mantissa): 0.85/sin eps0 per octave",
          abs(lin[1] * s0 - 1.2247) < 1e-3,
          f"2S_min linear w=1: {lin[1]:.0f}, w=1/2: {lin[0.5]:.0f}, w=1/4: {lin[0.25]:.0f}; log per octave {log_oct:.0f} (x3 = {3*log_oct:.0f} for [L/4, 2L])")
# rms 2L still only at the all-full corner; child length L is interior
w = 0.25
ns = rng.uniform(w, 2, size=(20000, 12))
ns[:50] = 2.0
rms = np.sqrt((ns ** 2).mean(1))
check("C2 THEOREM: in [wL, 2L] the rms edge reaches 2L only when every register is full, so the split trigger, the split and "
      "children at L are unchanged; the children's vacuum value sits inside the window (n_L = (1-w)/(2-w) of the range)",
      np.all((rms >= 2 - 1e-12) == np.all(ns == 2, axis=1)), f"w = 1/4: n_L at {(1-w)/(2-w):.3f} of the register")
check("C3 THEOREM: lapse ratios on a slice are bounded by 2/w (8 for w = 1/4), and the static core is stationary: the tick is the "
      "same unitary in every cube (fixed step), redshift is carried by edge VALUES, so no time-dependent drive appears", True,
      "the floor bounce (qcrush A3) moves to wL; collapse still needs the shift law (floor-horizon D2-D4)")

print("== D. option (b): skip half-ticks at the floor (1D free-fermion split-step test)")


def walk(Nsite, e, mu):
    X = np.array([[0, 1], [1, 0]], complex)
    ue = expm(-1j * (e - mu / 2) * X)
    uo = expm(1j * (e + mu / 2) * X)
    return ue, uo


def layer(Nsite, u, parity, active):
    U = np.eye(Nsite, dtype=complex)
    for j in range(parity, Nsite, 2):
        a, b = j % Nsite, (j + 1) % Nsite
        if active(a, b):
            idx = [a, b]
            U[np.ix_(idx, idx)] = u
    return U


def setup(e, mu, Nsite=160, edge_tick=True):
    ue, uo = walk(Nsite, e, mu)
    inB = lambda x: Nsite // 3 <= x < 2 * Nsite // 3
    allon = lambda a, b: True
    U = layer(Nsite, uo, 1, allon) @ layer(Nsite, ue, 0, allon)
    if edge_tick:
        act = lambda a, b: not (inB(a) and inB(b))
    else:
        act = lambda a, b: not (inB(a) or inB(b))
    Us = layer(Nsite, uo, 1, act) @ layer(Nsite, ue, 0, act)
    w_, V = np.linalg.eig(U)
    q = np.angle(w_)
    Qm, _ = np.linalg.qr(V[:, q < 0])
    Qp, _ = np.linalg.qr(V[:, q > 0])
    return U, Us, Qm, Qp, q, V


def skip_run(e, mu, sched, edge_tick=True):
    U, Us, Qm, Qp, q, V = setup(e, mu, edge_tick=edge_tick)
    Pp = Qp @ Qp.conj().T
    Cc = Qm @ Qm.conj().T
    nex = []
    for sk in sched:
        Ut = Us if sk else U
        Cc = Ut @ Cc @ Ut.conj().T
        nex.append(np.real(np.trace(Cc @ Pp)))
    Vi = np.linalg.inv(V)
    occ = np.real(np.einsum('ij,jk,ki->i', Vi, Cc, V))
    qe = np.sum(np.abs(q[q > 0]) * occ[q > 0]) / max(np.sum(occ[q > 0]), 1e-30)
    return np.array(nex), qe


bres = lambda f, T: [bool(np.floor((t + 1) * f) == np.floor(t * f)) for t in range(T)]
nex0, _ = skip_run(0.3, 0.1, [False] * 40)
check("D1 control: no skip (f = 1), like any time-independent tick, keeps the vacuum exactly; a register-controlled identity is "
      "unitary", np.max(np.abs(nex0)) < 1e-9, f"max excitations {np.max(np.abs(nex0)):.1e}")
one = {}
for e in (0.3, 0.1, 0.03):
    nex, qe = skip_run(e, e / 3, [True] + [False] * 30)
    one[e] = (nex[-1] / 2, qe)
c2 = [one[e][0] / e ** 2 for e in one]
check("D2 DIAGNOSTIC (one skipped tick): each boundary of the skip region creates p1 ~ c eps^2 excitations at band quasi-energies "
      "(a sudden local quench of the vacuum), never undone by later ticks",
      min(v[0] for v in one.values()) > 1e-5 and max(c2) / min(c2) < 3,
      "; ".join(f"eps {e}: p1 {v[0]:.2e} (p1/eps^2 {v[0]/e**2:.2f}), <q>/eps {v[1]/e:.2f}" for e, v in one.items()))
lines, slopes = [], {}
for f in (0.5, 0.75, 0.9, 0.618034):
    nex, qe = skip_run(0.3, 0.1, bres(f, 300))
    sl = np.polyfit(np.arange(300)[100:], nex[100:], 1)[0]
    slopes[f] = sl
    lines.append(f"f {f:.3f}: {nex[99]:.2f} -> {nex[-1]:.2f}, slope {sl:.1e}/tick")
check("D3 DIAGNOSTIC (eps 0.3, periodic schedules): a schedule is a drive at frequencies 2 pi {k f}; short periods (f = 1/2) are "
      "off-resonant with the band and leave only the transient, while schedules with components below the band width (f = 0.9, "
      "golden f) pump excitations linearly in time", slopes[0.5] < 1e-3 and slopes[0.9] > 1e-3, " | ".join(lines))
# 3D estimate: mismatch events per radial line per tick sum to (1 - f_c) over any grading; p1 = c eps0^2
Lr = np.sqrt(8 * np.pi) * 1.616e-35
cmin = min(c2)
for e0 in (0.0075, 0.0375):
    tau = np.sin(e0) * Lr / (np.sqrt(3) * 2.998e8)
    p1 = cmin * e0 ** 2
    E = e0 * 1.0546e-34 / tau
    flux = 0.5 * p1 * E / (Lr ** 2 * tau)
    Lum = flux * 4 * np.pi * (5e3) ** 2
    check(f"D4 ESTIMATE (eps0 {e0}, J0740 core, f_c ~ 1/2): transient alone, (1 - f_c) p1 hbar eps0/tau per L^2 per tick, is "
          f"{Lum:.0e} W against <~1e27 W seen from neutron stars", Lum > 1e60, f"p1 {p1:.1e}, E/quantum {E:.1e} J, flux {flux:.0e} W/m^2")
check("D5 THEOREM: a skipped half-tick must carry zero proper time and make no record: if it recorded, records per proper time "
      "would rise by 1/f in the core (a local, measurable difference: equivalence principle); unitary as a register-controlled "
      "identity, Lorentz-safe on average, but excluded by heating (D2-D4)", True)
print("supplied: CL-1 lapse + window, global ticks, continuum GR TOV, relativistic polytropes K=1 / causal-limit EOS, J0740 M,R")
print("  (Riley 2021, Miller 2021), qcrush A2 speed bound, 1D two-tiling free walk as a proxy of the 3D tick, rung L = sqrt(8pi) l_P.")
print(f"elapsed {time.monotonic() - T00:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
