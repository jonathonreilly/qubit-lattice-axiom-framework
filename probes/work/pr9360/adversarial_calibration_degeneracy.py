"""PR 9360 attack-e: SAMPLED EVIDENCE.  The note's calibration rests on three optimizer starts ('close starts do not define an error bar', condition number 4.97) and its headline
transfer numbers (Ramsey 1.659 pp with the frozen rates; the k20 = 0 control 1.674 pp) are read as insensitive to the calibration.  An adversarial construction instead of more starts:

  1. global search: 400 random starts over [0, 10]^3 with the note's bounds (the note's three starts are the sampled evidence): every distinct local minimum of the calibration cost;
  2. hill-climb over the near-degenerate calibration set: maximise and minimise the Ramsey RMS, the echo (swap) RMS and the echo-no-swap RMS subject to calibration cost <= (1 + delta) x minimum
     for delta = 1e-4, 1e-3, 1e-2 (SLSQP with penalty restarts from the optimum and from 40 random feasible points);
  3. the linearised (Jacobian) 1-sigma spread of the three rates and of the Ramsey RMS, with noise variance taken at the calibration RMS and the 36,051 coordinates treated as independent
     (an optimistic error, as the note says) and with an effective sample of 1/100 of that (correlated reference noise).
Own barycentric readout and propagation from the packaged raw arrays.
"""
import io, subprocess, sys, time, json, re
from pathlib import Path
import numpy as np
from scipy.linalg import expm

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/preparation-transfer-20260927"
D = "data/preparation_transfer_2026_09_27"
PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

def gitshow(path):
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{path}"], cwd=ROOT, capture_output=True)
    if r.returncode != 0: raise SystemExit(f"cannot read {path}: {r.stderr.decode()[:200]}")
    return r.stdout
def load(name): return np.load(io.BytesIO(gitshow(f"{D}/{name}")), allow_pickle=False)
def loadjson(name): return json.loads(gitshow(f"{D}/{name}"))

def populations(z):
    """barycentric populations of every stored point in the frame of the final three reference points of each gate"""
    iq = z["raw_IQ"]; out = []
    for gate in iq:
        M = np.vstack([gate[-3:].T, np.ones(3)])
        out.append(np.linalg.solve(M, np.vstack([gate.T, np.ones(len(gate))])).T)
    return np.array(out)

def propagate(rates, t_us, init, swap=False):
    k10, k21, k20 = rates; lam = k21 + k20
    def step(t, u):
        F = (np.exp(-k10 * t) - np.exp(-lam * t)) / (lam - k10)
        u2 = u[..., 2] * np.exp(-lam * t)
        u1 = u[..., 1] * np.exp(-k10 * t) + k21 * u[..., 2] * F
        return np.stack([1 - u1 - u2, u1, u2], axis=-1)
    u0 = np.broadcast_to(np.asarray(init, float), (len(t_us), 3))
    if swap:
        h = step(t_us / 2, u0); return step(t_us / 2, h[..., [0, 2, 1]])
    return step(t_us, u0)

NOTE_RATES = np.array([0.07126916, 0.11124121, 0.00839770])
SEQ_RATES = np.array([0.07728135, 0.11762925, 0.0])
def lindblad_L(k10, k21, k20):
    """vectorised Lindblad generator (column-stacking vec) for H = 0 and jump operators sqrt(k_ij)|j><i|"""
    d = 3
    def ket(i): v = np.zeros((d, 1)); v[i] = 1; return v
    I = np.eye(d)
    Lv = np.zeros((d * d, d * d), complex)
    for (i, j, k) in ((1, 0, k10), (2, 1, k21), (2, 0, k20)):
        A = np.sqrt(k) * (ket(j) @ ket(i).T)
        AdA = A.T @ A
        Lv += np.kron(A.conj(), A) - 0.5 * np.kron(I, AdA) - 0.5 * np.kron(AdA.T, I)
    return Lv
from scipy.optimize import least_squares, minimize
np.seterr(all='ignore')

T0 = time.time()
zc, zr, ze = load("calibration_raw.npz"), load("ramsey_raw.npz"), load("echo_raw.npz")
P = {n: populations(z) for n, z in (("c", zc), ("r", zr), ("e", ze))}
def gen(z, n):
    m = z["genuine_mask"]; return z["times_s"][m] * 1e6, P[n][:, m, :]
tc, Pc = gen(zc, "c"); tr, Pr = gen(zr, "r"); te, Pe = gen(ze, "e")
def cal_res(k): return (propagate(np.clip(k, 0, 10), tc, [0, 0, 1])[None, :, :] - Pc).ravel()
def cost(k): r = cal_res(k); return float(r @ r)
def rms_t(rates, tt, PP, init, swap=False):
    pred = propagate(np.clip(rates, 0, 10), tt, init, swap)[:, 1:].sum(-1); obs = PP[..., 1:].sum(-1); d = pred[None, :] - obs
    return float(np.sqrt(np.mean(d ** 2))) * 100
ramsey = lambda k: rms_t(k, tr, Pr, [0, .5, .5]); echo_sw = lambda k: rms_t(k, te, Pe, [0, .5, .5], True); echo_ns = lambda k: rms_t(k, te, Pe, [0, .5, .5])

# ---- 1. global search
rng = np.random.default_rng(90360)
fits = []
for s in [np.array(x, float) for x in ([0.05, 0.1, 0.05], [0.2, 0.2, 0.2], [1, 0.1, 1])] + [rng.uniform(0, 10, 3) for _ in range(400)]:
    r = least_squares(cal_res, s, bounds=(0, 10), ftol=1e-15, xtol=1e-15, gtol=1e-14, max_nfev=300)
    fits.append((float(np.sum(r.fun ** 2)), r.x))
fits.sort(key=lambda f: f[0]); best_c, best_k = fits[0]
distinct = []
for c, x in fits:
    if all(np.max(np.abs(x - y[1])) > 1e-3 or abs(c - y[0]) / best_c > 1e-6 for y in distinct): distinct.append((c, x))
print("== 1. global search: 403 starts ==")
for c, x in distinct[:6]: print(f"   cost {c:.9f} (x{c/best_c:.6f}) at rates {np.round(x, 6)}")
check("all 403 starts end at the note's minimum (a single distinct minimum) with the note's rates to 5e-8", len(distinct) == 1 and np.max(np.abs(best_k - NOTE_RATES)) < 5e-8, f"{len(distinct)} distinct; best {np.round(best_k, 8)}")

# ---- 2. near-degenerate hill-climb
print("\n== 2. hill-climb over the near-degenerate calibration set (cost <= (1+delta) x minimum) ==")
def extremum(fun, delta, sign):
    """maximise sign*fun subject to cost <= (1+delta) best_c; starts at the optimum and 40 random feasible perturbations"""
    limit = best_c * (1 + delta)
    cons = [{"type": "ineq", "fun": lambda k: (limit - cost(k)) / best_c * 1e3}]
    best = None
    starts = [best_k] + [np.clip(best_k * (1 + rng.normal(0, 0.05 * (1 + 20 * delta) ** 0.5, 3)), 0, 10) for _ in range(40)]
    for x0 in starts:
        if cost(x0) > limit: continue
        r = minimize(lambda k: -sign * fun(k), x0, method="SLSQP", bounds=[(0, 10)] * 3, constraints=cons, options={"maxiter": 200, "ftol": 1e-12})
        if cost(r.x) <= limit * (1 + 1e-9) and (best is None or -r.fun * 1 > best[0]): best = (-r.fun, r.x)
    return best
tab = {}
print("   delta     quantity        min          max      (rates at max)")
for delta in (1e-4, 1e-3, 1e-2):
    for nm, fun in (("Ramsey", ramsey), ("echo swap", echo_sw), ("echo noswap", echo_ns)):
        hi = extremum(fun, delta, +1); lo = extremum(fun, delta, -1)
        tab[(delta, nm)] = (-lo[0] if lo else np.nan, hi[0] if hi else np.nan)
        print(f"   {delta:6.0e}  {nm:12s}  {tab[(delta, nm)][0]:8.4f}  {tab[(delta, nm)][1]:8.4f}   {np.round(hi[1], 4) if hi else None}")
r_opt = ramsey(best_k)
check("at delta = 1e-3 (cost within 0.1% of the minimum) the Ramsey RMS stays within 0.1 pp of the note's 1.659 pp",
      all(abs(v - r_opt) < 0.1 for v in tab[(1e-3, "Ramsey")]), f"range {tab[(1e-3, 'Ramsey')][0]:.4f}..{tab[(1e-3, 'Ramsey')][1]:.4f}")
print(f"   at delta = 1e-2 the Ramsey RMS ranges {tab[(1e-2, 'Ramsey')][0]:.3f}..{tab[(1e-2, 'Ramsey')][1]:.3f} pp; the k20 = 0 control (Ramsey 1.6735) lies "
      + ("INSIDE" if tab[(1e-2, 'Ramsey')][0] - 1e-3 <= 1.673540 <= tab[(1e-2, 'Ramsey')][1] + 1e-3 else "OUTSIDE") + " that range")
# ---- 3. linearised spread
r = least_squares(cal_res, best_k, bounds=(0, 10), ftol=1e-15, xtol=1e-15, gtol=1e-14)
J = r.jac; sig2 = np.mean(r.fun ** 2)
print("\n== 3. linearised (Jacobian) spread ==")
sp = {}
for lab, neff in (("36,051 independent coordinates", 36051), ("effective sample 1/100 (correlated reference noise)", 360.51)):
    cov = sig2 * np.linalg.inv(J.T @ J) * (36051 / neff)
    se = np.sqrt(np.diag(cov))
    # delta method for the Ramsey RMS
    h = 1e-6; g = np.array([(ramsey(best_k + h * np.eye(3)[i]) - ramsey(best_k - h * np.eye(3)[i])) / (2 * h) for i in range(3)])
    sr = float(np.sqrt(g @ cov @ g)); sp[lab] = (se, sr)
    print(f"   {lab}: rate se {np.round(se, 6)} (relative {np.round(se / best_k * 100, 3)} %); Ramsey RMS se {sr:.4f} pp")
print(f"   the note's Ramsey difference between the three-rate and k20 = 0 calibrations is 0.0142 pp; the linearised Ramsey-RMS uncertainty is {sp['36,051 independent coordinates'][1]:.4f} pp (independent-coordinate noise) or {sp['effective sample 1/100 (correlated reference noise)'][1]:.4f} pp (1/100 effective sample)")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-e sampled evidence on PR 9360: 403 starts -> {len(distinct)} distinct calibration minimum; hill-climb over cost <= (1+delta) x min: Ramsey RMS range {tab[(1e-3,'Ramsey')][0]:.3f}-{tab[(1e-3,'Ramsey')][1]:.3f} pp at delta 1e-3 and {tab[(1e-2,'Ramsey')][0]:.3f}-{tab[(1e-2,'Ramsey')][1]:.3f} at 1e-2 (note 1.659), echo swap {tab[(1e-2,'echo swap')][0]:.2f}-{tab[(1e-2,'echo swap')][1]:.2f} pp at 1e-2; linearised Ramsey-RMS se {sp['36,051 independent coordinates'][1]:.4f}/{sp['effective sample 1/100 (correlated reference noise)'][1]:.4f} pp; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
