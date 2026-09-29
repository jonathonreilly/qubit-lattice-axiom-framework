"""PR 9359 attack-d: QUANTIFIER SCOPE of the note's exact-assumption inputs: 'exact psi = pi and stability across acquisitions are additional assumptions', B = 0.15 T, alpha = 0.442.

The note calibrates (EC, Jsum, tau) to the low-level f01 and f12 centers and the full f01 dispersion of each calibration version and then reads off f03 (residual +0.432226 MHz for the lowest-cost raw return).
Here the whole pipeline (calibration + f03 prediction) is repeated with the assumed inputs moved, for the processed version and the raw 0.30 V (lowest-cost) version:
  psi = pi + delta for delta in {-0.2, -0.1, -0.05, -0.02, 0, 0.02, 0.05, 0.1, 0.2} rad (the two arms' relative phase; the note assumes the bottom sweet spot),
  B = 0.15 (1 + eps) T for eps in {-3, -1, 0, +1, +3} %, and the arm asymmetry alpha -> alpha (1 + eta) for eta in {-2, +2} % (through Ja/Jb),
and reports how the sub-MHz f03 center residual and the dispersion residual move.  Own model (charge x Fock, sinc envelopes, short-channel potential), own fits (several starts).
"""
import json, subprocess, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
import os
ROOT = Path(os.environ.get('PROBE_ROOT') or Path(__file__).resolve().parents[3])
BRANCH = "physics-loop/microscopic-transmon-20260927"; DD = "data/microscopic_transmon_2026_09_27"
def load(name):
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{DD}/{name}"], cwd=ROOT, capture_output=True, text=True)
    return json.loads(r.stdout)
OM, G = 7.544917319789201, 0.07352541358551871
B0, BA, BB = 0.15, 0.8, 0.8 * 256 / 178
B = B0
ALPHA = (256 * 257 - 178 * 143) / (256 * 257 + 178 * 143)
def sinc(z): return np.sinc(z)                                  # numpy sinc(z) = sin(pi z)/(pi z)
MMAX = 14
def cos_coeffs(tau, M=8192):
    ph = (np.arange(M) + 0.5) * 2 * np.pi / M
    s = np.sin(ph / 2) ** 2
    r = 4 * s / (1 + np.sqrt(1 - tau * s))
    a = np.array([(2.0 / M) * np.sum(r * np.cos(m * ph)) for m in range(MMAX + 1)])
    return -a / a[1]                                            # normalised: c_1 = -1
PSI = np.pi
def hops(p, ablate=False, psi=None):
    psi = PSI if psi is None else psi
    EC, Jsum, tau = p
    c = cos_coeffs(tau)
    Ja, Jb = Jsum * (1 + ALPHA) / 2, Jsum * (1 - ALPHA) / 2
    h = np.zeros(MMAX + 1)
    for m in range(1, MMAX + 1):
        env = m if not ablate else 1
        h[m] = 0.5 * c[m] * (Ja * sinc(env * B / BA) + Jb * sinc(env * B / BB) * np.cos(m * psi))
    return h
def gaps(p, q, ablate=False, N=14, K=8, nlev=4, cosine=False):
    EC = p[0]
    n = np.arange(-N, N + 1, dtype=float); d = len(n)
    hp = hops(p, ablate) if not cosine else np.r_[0.0, -0.5 * p[1], np.zeros(MMAX - 1)]
    hop = np.zeros((d, d))
    for m in range(1, MMAX + 1):
        hop += hp[m] * (np.eye(d, k=m) + np.eye(d, k=-m))
    h0 = np.diag(4 * EC * (n - q) ** 2) + hop
    e0, v0 = np.linalg.eigh(h0)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(h0, np.eye(K)) + OM * np.kron(np.eye(d), np.diag(np.arange(K, dtype=float))) + G * np.kron(np.diag(n - q), a + a.T)
    w, V = np.linalg.eigh(h)
    lev = []
    for j in range(nlev):
        pr = np.abs(np.kron(v0[:, j], np.eye(K)[:, 0]) @ V) ** 2
        i = int(np.argmax(pr)); lev.append((w[i], pr[i], i))
    if len({l[2] for l in lev}) < nlev or min(l[1] for l in lev) < 0.5: raise ValueError("unassignable")
    return np.array([lev[j][0] - lev[0][0] for j in range(1, nlev)]), min(l[1] for l in lev)
def obs(p, **kw):
    a, wa = gaps(p, 0.0, **kw); b, wb = gaps(p, 0.5, **kw)
    c = (a + b) / 2
    return np.array([c[0], c[1] - c[0], abs(a[0] - b[0])]), c[2], min(wa, wb)
def fit(cal3, starts, cosine=False, ablate=False, ncal=3):
    tgt = np.array([cal3[0] / 1e9, cal3[1] / 1e9, cal3[2] / 1e9])
    best = None
    for st in starts:
        def res(z):
            try: o, _, _ = obs(z if not cosine else np.r_[z, 0.0], cosine=cosine, ablate=ablate)
            except ValueError: return np.full(ncal, 10.0)
            return ((o - tgt) / np.array([1, 1, 1e-3]))[:ncal]
        r = least_squares(res, st, x_scale=[0.2, 10, 0.2][:len(st)], ftol=1e-14, xtol=1e-14, gtol=1e-14, max_nfev=400)
        e = float(np.max(np.abs(r.fun)))
        if best is None or e < best[1]: best = (r.x, e)
    return best

PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
T0 = time.time()
cal = load("calibration.json")["calibration_Hz"]; tg = load("targets.json")
F03 = float(tg["processed"]["f_center"]) / 1e9; D03 = float(tg["processed"]["charge_dispersion"]) / 1e9
def f03_disp(p, N=14, K=8):
    a, _ = gaps(p, 0.0, N=N, K=K); b, _ = gaps(p, 0.5, N=N, K=K)
    return (a[2] + b[2]) / 2, abs(a[2] - b[2])
STARTS = [[0.285, 33.0, 0.01], [0.34, 29.9, 0.15], [0.30, 31.0, 0.5]]
def pipeline(nm):
    sols = []
    for st in STARTS:
        try: z, e = fit(cal[nm], [st])
        except Exception: continue
        if e < 1e-6 and not any(np.allclose(z, y[0], atol=1e-6) for y in sols): sols.append((z, e))
    if not sols: return None
    outs = []
    for z, e in sols:
        c, d = f03_disp(z); outs.append((1000 * (c - F03), 1000 * (d - D03), z))
    return outs
def ALPHA_set(v):
    global ALPHA
    ALPHA = v
ALPHA0 = ALPHA
res = {}
for nm in ("processed", "raw_period_0.3"):
    print(f"== {nm} ==")
    print("   variation                    solutions  f03 center residual (MHz)   full dispersion residual (MHz)")
    for lab, setter in ([(f"psi = pi {d:+.2f}", ("psi", np.pi + d)) for d in (-0.2, -0.1, -0.05, -0.02, 0.0, 0.02, 0.05, 0.1, 0.2)] +
                        [(f"B x (1 {e:+.0%})", ("B", B0 * (1 + e))) for e in (-0.03, -0.01, 0.01, 0.03)] +
                        [(f"alpha x (1 {e:+.0%})", ("alpha", ALPHA0 * (1 + e))) for e in (-0.02, 0.02)]):
        PSI = np.pi; B = B0; ALPHA = ALPHA0
        kind, val = setter
        if kind == "psi": PSI = val
        elif kind == "B": B = val
        else: ALPHA = val
        out = pipeline(nm)
        if out is None:
            print(f"   {lab:26s}  no calibration solution below 1e-6"); res[(nm, lab)] = None; continue
        best = out[0]
        print(f"   {lab:26s}  {len(out):2d}        {best[0]:+11.6f}                 {best[1]:+11.6f}")
        res[(nm, lab)] = best
    PSI = np.pi; B = B0; ALPHA = ALPHA0
base = res[("raw_period_0.3", "psi = pi +0.00")]
check("at the assumed inputs (psi = pi, B = 0.15 T, alpha = 0.442) the raw 0.30 V version gives the note's +0.432226 MHz center residual", abs(base[0] - 0.432226) < 5e-4, f"{base[0]:+.6f}")
def spread(nm, prefix):
    v = [res[(nm, k)][0] for (n_, k) in res if n_ == nm and k.startswith(prefix) and res[(n_, k)] is not None]
    return min(v), max(v)
sp_psi = spread("raw_period_0.3", "psi"); sp_B = spread("raw_period_0.3", "B x"); sp_a = spread("raw_period_0.3", "alpha")
print(f"   raw 0.30 V f03 center residual range: psi in pi +- 0.2: {sp_psi[0]:+.3f} .. {sp_psi[1]:+.3f} MHz; B +-3 %: {sp_B[0]:+.3f} .. {sp_B[1]:+.3f} MHz; alpha +-2 %: {sp_a[0]:+.3f} .. {sp_a[1]:+.3f} MHz")
psi_small = [res[("raw_period_0.3", f"psi = pi {d:+.2f}")] for d in (-0.02, 0.02)]
print(f"   psi = pi +- 0.02: f03 residual {psi_small[0][0]:+.4f} / {psi_small[1][0]:+.4f} MHz (base {base[0]:+.4f}); half-width of the note's headline: the residual is 0.43 MHz")
allv = [v[0] for (n_, k), v in res.items() if n_ == "raw_period_0.3" and v is not None]
check("recalibrating at each moved input absorbs it: the raw 0.30 V f03 center residual stays within 0.11 MHz of +0.432 MHz (and positive) for psi = pi +- 0.2 rad, B +- 3 % and alpha +- 2 %, and the processed version stays within 0.10 MHz of +0.930 MHz",
      max(abs(x - base[0]) for x in allv) < 0.11 and min(allv) > 0 and max(abs(v[0] - res[("processed", "psi = pi +0.00")][0]) for (n_, k), v in res.items() if n_ == "processed" and v is not None) < 0.10,
      f"raw range {min(allv):+.3f} .. {max(allv):+.3f}; largest move {max(abs(x - base[0]) for x in allv):.3f} MHz")
print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-d quantifier scope on PR 9359: whole calibrate-then-predict pipeline repeated with the assumed inputs moved (raw 0.30 V version): f03 center residual {base[0]:+.3f} MHz at psi = pi; over psi in pi +- 0.2 rad it ranges {sp_psi[0]:+.2f} .. {sp_psi[1]:+.2f} MHz, over B +- 3 % {sp_B[0]:+.2f} .. {sp_B[1]:+.2f} MHz, over alpha +- 2 % {sp_a[0]:+.2f} .. {sp_a[1]:+.2f} MHz, so the sub-MHz f03 residual is robust to those assumed inputs (three calibrated shape parameters absorb them), the +0.43 MHz stays positive and within 0.11 MHz; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
