"""PR 9360 attack-f: NORMALIZATION.  Factors of 2 in rates and delays, of sqrt(N), of ddof and of parametrisation in the note's numbers, recomputed from the packaged raw arrays.

 1. Lindblad jump-operator normalisation: collapse operators sqrt(k_ij)|j><i| give population rates k_ij (not k/2 or 2k): 3-level vectorised Lindblad vs the note's generator, and the factors 1/2, 2.
 2. RMS conventions: which definition reproduces the printed 1.659315 (Ramsey, three rates) and 0.03151155 (calibration): mean over all points (ddof 0) vs sample (ddof 1), per coordinate vs per (gate, delay) L2 norm.
 3. Jacobian condition number 4.97: in rate coordinates (per us or per s: the same) and in log-rate coordinates.
 4. Delay/rate scale: the echo residual under a common rate scale s (the 1/T versus 2/T convention the note mentions) and under a scale on the echo delay axis alone, with the Ramsey residual alongside and the model class's own floors.
Own barycentric readout and own propagation from the packaged arrays.
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
from scipy.optimize import least_squares

T0 = time.time()
zc, zr, ze = load("calibration_raw.npz"), load("ramsey_raw.npz"), load("echo_raw.npz")
P = {n: populations(z) for n, z in (("c", zc), ("r", zr), ("e", ze))}
def gen(z, n):
    m = z["genuine_mask"]; return z["times_s"][m] * 1e6, P[n][:, m, :]
tc, Pc = gen(zc, "c"); tr, Pr = gen(zr, "r"); te, Pe = gen(ze, "e")
def resid_t(rates, tt, PP, init, swap=False):
    pred = propagate(rates, tt, init, swap)[:, 1:].sum(-1); obs = PP[..., 1:].sum(-1); return pred[None, :] - obs
def rms_t(rates, tt, PP, init, swap=False, ddof=0):
    d = resid_t(rates, tt, PP, init, swap); return float(np.sqrt((d ** 2).sum() / (d.size - ddof))) * 100, float(d.mean()) * 100

# ---- 1. Lindblad normalisation
print("== 1. jump-operator normalisation ==")
t = 9.0
p_ref = propagate(NOTE_RATES, np.array([t]), [0, 0, 1])[0]
def pops_from(Lv, tt):
    rho0 = np.diag([0, 0, 1]).astype(complex)
    return np.real(np.diag(( expm(Lv * tt) @ rho0.reshape(-1, order="F")).reshape(3, 3, order="F")))
for fac, nm in ((1.0, "sqrt(k)"), (2.0, "sqrt(2k)"), (0.5, "sqrt(k/2)")):
    pp = pops_from(lindblad_L(*(NOTE_RATES * fac)), t)
    print(f"   jump operators {nm}: max |population - note's generator at rates k| = {np.max(np.abs(pp - p_ref)):.2e}")
pp1 = pops_from(lindblad_L(*NOTE_RATES), t)
check("collapse operators sqrt(k_ij)|j><i| reproduce the note's generator to 1e-12, and the factor-2 variants do not (differences >= 1e-2)",
      np.max(np.abs(pp1 - p_ref)) < 1e-12 and np.max(np.abs(pops_from(lindblad_L(*(2 * NOTE_RATES)), t) - p_ref)) > 1e-2 and np.max(np.abs(pops_from(lindblad_L(*(0.5 * NOTE_RATES)), t) - p_ref)) > 1e-2)

# ---- 2. RMS conventions
print("\n== 2. RMS conventions ==")
r0, m0 = rms_t(NOTE_RATES, tr, Pr, [0, .5, .5]); r1, _ = rms_t(NOTE_RATES, tr, Pr, [0, .5, .5], ddof=1)
print(f"   Ramsey, three rates: ddof 0 {r0:.6f} pp, ddof 1 {r1:.6f} pp; mean (prediction - observation) {m0:+.6f} pp; note 1.659315 / +0.274780")
check("the note's Ramsey RMS uses the mean over all 31 x 380 points (ddof 0): 1.659315 to 5e-6 pp, and the prediction-minus-observation sign of the mean", abs(r0 - 1.659315) < 5e-6 and abs(m0 - 0.274780) < 5e-6 and abs(r1 - 1.659315) > 3e-5, f"ddof0 {r0:.6f}, ddof1 {r1:.6f}")
res = propagate(NOTE_RATES, tc, [0, 0, 1])[None, :, :] - Pc
rc, rl2 = float(np.sqrt(np.mean(res ** 2))), float(np.sqrt(np.mean((res ** 2).sum(-1))))
print(f"   calibration: per coordinate {rc:.8f} (note 0.03151155); per (gate, delay) L2 norm {rl2:.8f}; ratio {rl2/rc:.4f} (sqrt 3 = 1.7321)")
check("the calibration RMS 0.03151155 is per coordinate over 36,051 values (not per (gate, delay) L2 norm)", abs(rc - 0.03151155) < 5e-8 and abs(rl2 / rc - np.sqrt(3)) < 1e-9, f"{rc:.8f}")

# ---- 3. Jacobian condition
print("\n== 3. Jacobian condition number ==")
def rescal(k): return (propagate(k, tc, [0, 0, 1])[None, :, :] - Pc).ravel()
def jac(f, x, h=1e-6):
    f0 = f(x); J = np.empty((f0.size, x.size))
    for i in range(x.size):
        xp = x.copy(); xm = x.copy(); dx = h * max(abs(x[i]), 1e-3); xp[i] += dx; xm[i] -= dx
        J[:, i] = (f(xp) - f(xm)) / (2 * dx)
    return J
sv = np.linalg.svd(jac(rescal, NOTE_RATES.copy()), compute_uv=False)
svl = np.linalg.svd(jac(lambda u: rescal(np.exp(u)), np.log(NOTE_RATES)), compute_uv=False)
print(f"   rate coordinates (per us): {sv[0]/sv[-1]:.3f} (note 4.97; per s gives the same by a common column scale); log-rate coordinates: {svl[0]/svl[-1]:.3f}")
check("the note's Jacobian condition 'near 4.97' is the condition number in the rates themselves; in log-rate coordinates it is different", abs(sv[0] / sv[-1] - 4.97) < 0.02 and abs(svl[0] / svl[-1] - 4.97) > 0.5, f"{sv[0]/sv[-1]:.3f} vs {svl[0]/svl[-1]:.3f}")

# ---- 4. delay / rate scale
print("\n== 4. common rate scale s and echo-delay-axis scale (RMS in percentage points) ==")
rows = []
print("      s   Ramsey  echo(swap)  echo(no swap)   echo(swap) with delay axis only x s")
for s in (0.5, 1.0, 1.5, 2.0, 3.0):
    a = rms_t(NOTE_RATES * s, tr, Pr, [0, .5, .5])[0]; b = rms_t(NOTE_RATES * s, te, Pe, [0, .5, .5], True)[0]; c = rms_t(NOTE_RATES * s, te, Pe, [0, .5, .5])[0]
    d = rms_t(NOTE_RATES, te * s, Pe, [0, .5, .5], True)[0]
    rows.append((s, a, b, c, d)); print(f"   {s:4.1f}  {a:7.3f}  {b:9.3f}  {c:12.3f}   {d:9.3f}")
def fit_echo(swap):
    best = None
    for s0 in ([0.07, 0.11, 0.008], [0.2, 0.2, 0.2], [1, 0.1, 1], [0.01, 0.01, 0.01]):
        r = least_squares(lambda k: resid_t(k, te, Pe, [0, .5, .5], swap).ravel(), s0, bounds=(0, 10), ftol=1e-14, xtol=1e-14, gtol=1e-13)
        if best is None or r.cost < best.cost: best = r
    return float(np.sqrt(2 * best.cost / (Pe.shape[0] * Pe.shape[1]))) * 100
fl = fit_echo(True)
sgrid = np.linspace(1.5, 2.5, 101)
ecs = np.array([rms_t(NOTE_RATES, te * s, Pe, [0, .5, .5], True)[0] for s in sgrid]); sbest = sgrid[ecs.argmin()]
print(f"   echo delay-axis scale minimising the frozen-rate swap residual: {sbest:.3f} -> {ecs.min():.3f} pp (floor of the model class fitted to the echo itself: {fl:.3f} pp)")
r_s1 = rows[1]; r_s2 = rows[3]
check("at the declared convention (s = 1) the numbers are the note's table: Ramsey 1.659, echo swap 15.851, no swap 13.387", abs(r_s1[1] - 1.659315) < 5e-4 and abs(r_s1[2] - 15.851257) < 5e-4 and abs(r_s1[3] - 13.387442) < 5e-4, f"{r_s1[1:4]}")
check("the factor-2 sensitivity: echo swap residual falls to about 2 pp at s = 2 (delay axis only or common rate scale), below the no-swap value, while the Ramsey residual under a COMMON rate scale of 2 rises to about 4.8 pp",
      r_s2[2] < 3 and r_s2[2] < r_s2[3] and 4.5 < r_s2[1] < 5.2 and abs(r_s2[4] - r_s2[2]) < 1e-9, f"s=2: Ramsey {r_s2[1]:.3f}, echo swap {r_s2[2]:.3f}, no swap {r_s2[3]:.3f}, echo-axis-only {r_s2[4]:.3f}")
print(f"NOTE: the note declares the total-delay convention and says no factor is taken from echo agreement; the frozen-rate echo residual is {r_s1[2]:.2f} pp at s=1 and {ecs.min():.2f} pp at an echo delay-axis scale {sbest:.2f} (model-class floor {fl:.2f} pp), with the swap model then preferred to no swap ({r_s2[2]:.2f} vs {r_s2[3]:.2f} pp): the echo mismatch is a single factor-2 convention in this data, which the note lists among unresolved 'clock/rate conventions'.")
print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-f normalization on PR 9360: jump operators sqrt(k)|j><i| = rates k (factor-2 variants differ), Ramsey RMS is ddof-0 mean over 31x380 points ({r0:.6f}), calibration RMS per coordinate {rc:.8f} (L2-per-point is sqrt3 larger), Jacobian condition {sv[0]/sv[-1]:.2f} in rate coordinates ({svl[0]/svl[-1]:.2f} in log-rates); echo swap residual {r_s1[2]:.2f} pp at the declared convention and {ecs.min():.2f} pp at echo delay-axis scale {sbest:.2f} (floor {fl:.2f}), Ramsey under common scale 2: {r_s2[1]:.2f} pp; the note names clock/rate conventions as unresolved and takes no factor from echo agreement; PASS={PASS} FAIL={FAIL}; no defect in the note's stated numbers")
sys.exit(1 if FAIL else 0)
