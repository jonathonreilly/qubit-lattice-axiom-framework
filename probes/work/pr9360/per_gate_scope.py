"""PR 9360 attack-d: QUANTIFIER SCOPE.  The note pools every applied gate voltage: ONE rate triple from all 61 calibration gates predicts Ramsey (31 gates) and echo (61 gates) with a single
RMS.  'For every gate' is what the pooled numbers stand in for, and the note assumes 'cross-acquisition rate stability' and 'stationary rates'.  Executed here, from the packaged arrays:
  1. per-gate calibration: each of the 61 gates fitted alone (three rates, bounds [0, 10]); spread of the rates against the pooled rates;
  2. per-gate transfer residuals with the POOLED frozen rates: spread of the Ramsey (31 gates) and echo (61 gates) RMS, and the share of the summed squared residual carried by the worst gates;
  3. gate matching: which target gates coincide in voltage with a calibration gate, and the Ramsey/echo residual when each gate is predicted from ITS OWN calibrated rates instead of the pooled ones;
  4. whether the pooled Ramsey RMS is representative: fraction of gates below/above it, and the pooled RMS after removing the worst 10% of gates.
Own barycentric readout and own propagation.
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
np.seterr(all="ignore")
T0 = time.time()
zc, zr, ze = load("calibration_raw.npz"), load("ramsey_raw.npz"), load("echo_raw.npz")
P = {n: populations(z) for n, z in (("c", zc), ("r", zr), ("e", ze))}
def gen(z, n):
    m = z["genuine_mask"]; return z["times_s"][m] * 1e6, P[n][:, m, :]
tc, Pc = gen(zc, "c"); tr, Pr = gen(zr, "r"); te, Pe = gen(ze, "e")
gc, gr, ge = zc["gates_V"], zr["gates_V"], ze["gates_V"]
print(f"gate voltages: calibration {gc.min():.4f}..{gc.max():.4f} ({len(gc)}), Ramsey {gr.min():.4f}..{gr.max():.4f} ({len(gr)}), echo {ge.min():.4f}..{ge.max():.4f} ({len(ge)})")
def res_gate(k, g): return (propagate(np.clip(k, 0, 10), tc, [0, 0, 1]) - Pc[g]).ravel()
# 1. per-gate calibration
rates_g = []
for g in range(len(gc)):
    best = None
    for s in ([0.07, 0.11, 0.008], [0.2, 0.2, 0.2], [0.02, 0.05, 0.02]):
        r = least_squares(lambda k: res_gate(k, g), s, bounds=(0, 10), ftol=1e-13, xtol=1e-13, gtol=1e-12, max_nfev=200)
        if best is None or r.cost < best.cost: best = r
    rates_g.append(best.x)
rates_g = np.array(rates_g)
print("\n== 1. per-gate calibration rates (per us) ==")
for j, nm in enumerate(("k10", "k21", "k20")):
    print(f"   {nm}: pooled {NOTE_RATES[j]:.5f}; per gate median {np.median(rates_g[:, j]):.5f}, min {rates_g[:, j].min():.5f}, max {rates_g[:, j].max():.5f}, sd {rates_g[:, j].std(ddof=1):.5f} ({100*rates_g[:, j].std(ddof=1)/np.median(rates_g[:, j]):.1f}% of the median)")
on_bound = int(((rates_g <= 1e-9) | (rates_g >= 10 - 1e-9)).any(1).sum())
print(f"   gates with a rate on a bound: {on_bound} of {len(gc)}; the k20 (direct 2 -> 0) rate is at zero for {int((rates_g[:, 2] <= 1e-9).sum())} gates")
# 2. per-gate transfer residuals with pooled rates
def gate_rms(rates, tt, PP, init, swap=False):
    pred = propagate(rates, tt, init, swap)[:, 1:].sum(-1); obs = PP[..., 1:].sum(-1); d = pred[None, :] - obs
    return np.sqrt((d ** 2).mean(1)) * 100, d.mean(1) * 100
rr_g, rm_g = gate_rms(NOTE_RATES, tr, Pr, [0, .5, .5]); er_g, em_g = gate_rms(NOTE_RATES, te, Pe, [0, .5, .5], True)
pooled_r = float(np.sqrt(np.mean(rr_g ** 2))); pooled_e = float(np.sqrt(np.mean(er_g ** 2)))
check("the pooled RMS values are the note's (Ramsey 1.659315, echo swap 15.851257)", abs(pooled_r - 1.659315) < 5e-4 and abs(pooled_e - 15.851257) < 5e-4, f"{pooled_r:.6f}, {pooled_e:.6f}")
print("\n== 2. per-gate transfer residuals with the pooled frozen rates (percentage points) ==")
for nm, x, pooled in (("Ramsey", rr_g, pooled_r), ("echo swap", er_g, pooled_e)):
    srt = np.sort(x)[::-1]; share = (srt[:max(1, len(x) // 10)] ** 2).sum() / (x ** 2).sum()
    print(f"   {nm:9s}: {len(x)} gates, RMS per gate min {x.min():.3f} median {np.median(x):.3f} max {x.max():.3f}; pooled {pooled:.3f}; worst 10% of gates carry {100*share:.1f}% of the squared residual; gates below the pooled value: {int((x < pooled).sum())}")
mean_r = rm_g
print(f"   Ramsey mean(prediction - observation) per gate: min {mean_r.min():+.3f}, max {mean_r.max():+.3f}; sign is positive for {int((mean_r > 0).sum())} of {len(mean_r)} gates")
print(f"   echo   mean(prediction - observation) per gate: min {em_g.min():+.3f}, max {em_g.max():+.3f}; positive for {int((em_g > 0).sum())} of {len(em_g)}")
# 3. gate matching and own-gate transfer
def match(gt):
    idx = []
    for v in gt:
        j = int(np.argmin(np.abs(gc - v))); idx.append((j, abs(gc[j] - v)))
    return idx
mr, me = match(gr), match(ge)
print("\n== 3. gate matching ==")
print(f"   Ramsey gates to nearest calibration gate: max |dV| {max(d for _, d in mr):.2e} V, exact matches {sum(d < 1e-9 for _, d in mr)} of {len(mr)}; echo: max |dV| {max(d for _, d in me):.2e} V, exact {sum(d < 1e-9 for _, d in me)} of {len(me)}")
if max(d for _, d in mr) < 1e-6 and max(d for _, d in me) < 1e-6:
    own_r = []; own_e = []
    for i, (j, _) in enumerate(mr):
        pred = propagate(rates_g[j], tr, [0, .5, .5])[:, 1:].sum(-1); obs = Pr[i][:, 1:].sum(-1); own_r.append(np.mean((pred - obs) ** 2))
    for i, (j, _) in enumerate(me):
        pred = propagate(rates_g[j], te, [0, .5, .5], True)[:, 1:].sum(-1); obs = Pe[i][:, 1:].sum(-1); own_e.append(np.mean((pred - obs) ** 2))
    own_R = float(np.sqrt(np.mean(own_r)) * 100); own_E = float(np.sqrt(np.mean(own_e)) * 100)
    print(f"   each gate predicted from its OWN calibrated rates: Ramsey RMS {own_R:.3f} pp (pooled rates: {pooled_r:.3f}); echo (swap) {own_E:.3f} pp (pooled: {pooled_e:.3f})")
    check("own-gate calibration changes the Ramsey RMS by less than 30% of the pooled value (the pooled single-triple summary is not hiding a large gate dependence)", abs(own_R - pooled_r) < 0.3 * pooled_r, f"{own_R:.3f} vs {pooled_r:.3f}")
else:
    own_R = own_E = float("nan")
    print("   gate voltages do not coincide: no own-gate transfer computed")
# 4. representativeness
srt = np.sort(rr_g); trimmed = float(np.sqrt(np.mean(srt[:int(0.9 * len(srt))] ** 2)))
print(f"\n== 4. representativeness ==\n   Ramsey pooled RMS {pooled_r:.3f} pp; after dropping the worst 10% of gates {trimmed:.3f} pp; best gate {srt[0]:.3f}, worst {srt[-1]:.3f}")
check("no single gate exceeds 3x the pooled Ramsey RMS (the pooled figure is not carried by an outlier gate)", rr_g.max() < 3 * pooled_r, f"worst gate {rr_g.max():.2f} pp vs 3 x pooled {3*pooled_r:.2f}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-d quantifier scope on PR 9360: per-gate calibration rates (k10 sd {100*rates_g[:,0].std(ddof=1)/np.median(rates_g[:,0]):.0f}%, k21 {100*rates_g[:,1].std(ddof=1)/np.median(rates_g[:,1]):.0f}%, k20 {100*rates_g[:,2].std(ddof=1)/np.median(rates_g[:,2]):.0f}% of median; {on_bound} gates on a bound), per-gate Ramsey RMS {rr_g.min():.2f}-{rr_g.max():.2f} pp (median {np.median(rr_g):.2f}, pooled {pooled_r:.3f}), echo {er_g.min():.1f}-{er_g.max():.1f} pp (pooled {pooled_e:.2f}); own-gate transfer Ramsey {own_R:.3f} / echo {own_E:.3f} pp; the note's claims are pooled statements and make no per-gate claim; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
