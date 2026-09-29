"""PR 9360 attack (pattern c, EXECUTED NUMBERS): every executed optimizer range, count and status the note names, against the committed fit records and the historical protocol text on the PR branch.

Note statements checked:
  * 'fits all 36,051 calibration population coordinates, with fixed initial |2>, no offset/rescaling, rates in [0,10] per microsecond, and three starts';
  * 'All three returns stop by ftol and remain above the requested gradient tolerance. All starts and their statuses are preserved. No active bounds occur.';
  * 'Rates are approximately [k10,k21,k20]=[0.07126916,0.11124121,0.00839770] per microsecond, with calibration population RMS 0.03151155. A local Jacobian condition near 4.97';
  * the sequential-only control: 'It also retains all three starts, all ftol terminations above gradient tolerance'; rates [0.07728135,0.11762925,0]; calibration RMS 0.03227173;
  * the requested gradient tolerance itself (from the historical calibration text: least_squares(..., bounds=(0,10), ftol=1e-10, xtol=1e-10, gtol=1e-10)).
Read from data/preparation_transfer_2026_09_27/{calibration_fits,sequential_control_fits}.json and historical_calibrate_and_freeze.txt at the PR head.
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

cf = loadjson("calibration_fits.json"); sf = loadjson("sequential_control_fits.json")
hist = gitshow(f"{D}/historical_calibrate_and_freeze.txt").decode()
m = re.search(r"least_squares\(residual,start,bounds=\((\d+),(\d+)\),max_nfev=(\d+),ftol=([0-9.e-]+),xtol=([0-9.e-]+),gtol=([0-9.e-]+)\)", hist)
lo, hi, nfev, ftol, xtol, gtol = (float(x) for x in m.groups())
check("the historical calibration call requests bounds (0, 10), ftol = xtol = gtol = 1e-10 (the 'requested gradient tolerance')", (lo, hi, ftol, xtol, gtol) == (0, 10, 1e-10, 1e-10, 1e-10), m.group(0)[:120])
fits = cf["fits"]
check("three starts are preserved ((0.05,0.1,0.05), (0.2,0.2,0.2), (1,0.1,1)) with statuses 'returned'", [f["start"] for f in fits] == [[0.05, 0.1, 0.05], [0.2, 0.2, 0.2], [1, 0.1, 1]] and all(f["status"] == "returned" for f in fits))
check("all three stop by ftol ('`ftol` termination condition is satisfied') and every gradient optimality (2.2e-4 .. 1.6e-3) is above the requested gtol = 1e-10 by more than six orders of magnitude", all("ftol" in f["message"] for f in fits) and all(f["optimality"] > 1e6 * gtol for f in fits), ", ".join(f"{f['optimality']:.2e}" for f in fits))
check("no active bounds (active_mask all zero) and the rates are inside (0, 10)", all(all(a == 0 for a in f["active_mask"]) for f in fits) and all(0 < r < 10 for f in fits for r in f["rates_per_us"]))
rates = np.array([f["rates_per_us"] for f in fits]); spread = np.abs(rates - rates.mean(0)).max(0)
check("the three returns agree to 1e-8 per microsecond and to the note's rates [0.07126916, 0.11124121, 0.00839770] to 5e-8", spread.max() < 1e-8 and np.max(np.abs(rates[0] - NOTE_RATES)) < 5e-8, f"spread {spread}")
N = 61 * 197 * 3
rms = [f["raw_population_rms"] for f in fits]
check("calibration population RMS 0.03151155 over 36,051 coordinates: sqrt(2 cost / N) from the recorded cost equals the recorded RMS", all(abs(np.sqrt(2 * f["cost"] / N) - f["raw_population_rms"]) < 1e-12 for f in fits) and abs(rms[0] - 0.03151155) < 5e-9, f"{rms[0]:.10f}")
sv = fits[0]["jacobian_singular_values"]
check("local Jacobian condition near 4.97: ratio of the recorded singular values 542.668 / 109.102", abs(sv[0] / sv[2] - 4.974) < 0.005, f"{sv[0]/sv[2]:.4f}")
seq = sf["fits"]
check("sequential-only control: three starts retained, all ftol terminations, optimality above 1e-10, no active bounds, rates [0.07728135, 0.11762925, 0], RMS 0.03227173",
      len(seq) == 3 and all("ftol" in f["message"] for f in seq) and all(f["optimality"] > 1e6 * gtol for f in seq) and all(all(a == 0 for a in f["active_mask"]) for f in seq)
      and abs(seq[0]["rates_per_us"][0] - 0.07728135) < 5e-8 and abs(seq[0]["rates_per_us"][1] - 0.11762925) < 5e-8 and seq[0]["rates_per_us"][2] == 0 and abs(seq[0]["raw_population_rms"] - 0.03227173) < 5e-9,
      f"optimality {[round(f['optimality'], 5) for f in seq]}, condition {seq[0]['jacobian_condition']:.3f}")
print(f"   outside-simplex fraction of the calibration estimates recorded in the fit file: {cf['outside_simplex_fraction']:.4f} (the note says such values are retained and does not print the fraction); reference population defect {cf['reference_population_max_defect']:.1e}")
check("the recorded outside-simplex fraction of the calibration estimates equals the own-readout value 0.3314", abs(cf["outside_simplex_fraction"] - 0.3314) < 5e-4, f"{cf['outside_simplex_fraction']:.4f}")
print()
for h in HITS: print("HIT:", h)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: pattern (c) executed numbers on PR 9360: the committed fit records match the note's optimizer statements (3 starts, all ftol, gradient optimality 2e-4..1.6e-3 vs requested gtol 1e-10, no active bounds, rates and RMS to the printed digits, Jacobian condition 4.974, sequential control likewise); the recorded outside-simplex fraction of the calibration estimates is 0.331 (retained, not printed in the note); PASS={PASS} FAIL={FAIL}; no defect")
sys.exit(1 if FAIL else 0)
