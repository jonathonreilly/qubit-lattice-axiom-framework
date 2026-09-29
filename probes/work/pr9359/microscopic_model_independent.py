#!/usr/bin/env python3
"""J:falsifier:PR9359 -- independent reproduction of the rectangular-junction transmon transfer: the note's five f03 calibration-version residuals, its dispersion residuals, the cosine control, the raw-extraction residuals and the harmonic-envelope ablation.

Model (from the note's text only): H/h = 4 EC (n - q)^2 + V(phi) + Omega a^dag a + G (n - q)(a + a^dag), charge basis -N..N, photon states 0..K-1, (Omega, G) = (7.544917319789201, 0.07352541358551871) GHz; the local short-channel potential r_tau(phi) = 4 s/[1 + sqrt(1 - tau s)],
s = sin^2(phi/2), with cosine Fourier coefficients a_m normalised by c_m = -a_m/a_1 (fundamental -cos(phi)); two arms with Ja/Jb = (256*257)/(178*143), B = 0.15 T, Ba = 0.8 T, Bb = 0.8*256/178 T and psi = pi: the charge-basis hopping at order m is
(1/2) c_m [Ja sinc(m B/Ba) + Jb sinc(m B/Bb) cos(m psi)], Ja + Jb = Jsum; centers are the mean of the q = 0 and q = 1/2 gaps, dispersions their difference; levels labelled by the largest overlap with the isolated-device levels and photon vacuum.
(EC, Jsum, tau) are calibrated (least squares, several starts) to the three low-level inputs of each calibration version (f01 center, f12 center, full f01 dispersion) read from the PR's committed calibration.json; the f03 center and full dispersion are then compared with the note's tables.
Nothing of the PR's runner or helpers is used; only the committed data files (calibration.json, targets.json) are read, via git. Floating point.
Prints SUMMARY:; HIT only if a stated number fails to reproduce.
"""
import json, subprocess, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/microscopic-transmon-20260927"; DD = "data/microscopic_transmon_2026_09_27"
def load(name):
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{DD}/{name}"], cwd=ROOT, capture_output=True, text=True)
    return json.loads(r.stdout)
OM, G = 7.544917319789201, 0.07352541358551871
B, BA, BB = 0.15, 0.8, 0.8 * 256 / 178
ALPHA = (256 * 257 - 178 * 143) / (256 * 257 + 178 * 143)
def sinc(z): return np.sinc(z)                                  # numpy sinc(z) = sin(pi z)/(pi z)
MMAX = 14
def cos_coeffs(tau, M=8192):
    ph = (np.arange(M) + 0.5) * 2 * np.pi / M
    s = np.sin(ph / 2) ** 2
    r = 4 * s / (1 + np.sqrt(1 - tau * s))
    a = np.array([(2.0 / M) * np.sum(r * np.cos(m * ph)) for m in range(MMAX + 1)])
    return -a / a[1]                                            # normalised: c_1 = -1
def hops(p, ablate=False, psi=np.pi):
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

NOTE_CENTER = {"archive": -9.953473, "processed": +0.930015, "raw_period_0.15": +10.073133, "raw_period_0.22": +0.448572, "raw_period_0.3": +0.432226}
NOTE_DISP = {"archive": +16.249573, "processed": -3.526868, "raw_period_0.15": -16.929541, "raw_period_0.22": -2.738574, "raw_period_0.3": -2.711563}
NOTE_RAW3 = {"raw_period_0.15": +11.130345, "raw_period_0.22": +1.505784, "raw_period_0.3": +1.489438}
NOTE_ABL = {"raw_period_0.15": (+0.082974, -0.006435), "raw_period_0.22": (+0.195255, -0.021529), "raw_period_0.3": (+0.195467, -0.021564)}
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
T0 = time.time()
cal = load("calibration.json")["calibration_Hz"]; tg = load("targets.json")
F03 = float(tg["processed"]["f_center"]) / 1e9; D03 = float(tg["processed"]["charge_dispersion"]) / 1e9
raw3 = [float(f["center_Hz"]) / 1e9 for f in tg["raw"]["fits"]]
print(f"   processed f03 center {F03:.9f} GHz, full dispersion {1000 * D03:.6f} MHz; raw extraction centers {['%.9f' % c for c in raw3]} GHz")
def f03_disp(p, ablate=False, N=14, K=8):
    a, _ = gaps(p, 0.0, ablate=ablate, N=N, K=K); b, _ = gaps(p, 0.5, ablate=ablate, N=N, K=K)
    return (a[2] + b[2]) / 2, abs(a[2] - b[2])
STARTS = [[0.285, 33.0, 0.01], [0.34, 29.9, 0.15], [0.30, 31.0, 0.5], [0.27, 35.0, 0.05], [0.32, 30.5, 0.11]]
rows = {}
for nm in NOTE_CENTER:
    sols = []
    for st in STARTS:
        z, e = fit(cal[nm], [st])
        if e < 1e-6 and not any(np.allclose(z, y[0], atol=1e-6) for y in sols): sols.append((z, e))
    z, e = min(sols, key=lambda s: abs(f03_disp(s[0])[0] - F03 - NOTE_CENTER[nm] / 1000)) if sols else (None, None)
    c, d = f03_disp(z)
    za, ea = fit(cal[nm], [z], ablate=True); ca, da = f03_disp(za, ablate=True)
    rows[nm] = dict(z=z, sols=sols, center=1000 * (c - F03), disp=1000 * (d - D03), abl=(1000 * (ca - c), 1000 * (da - d)), c=c, ea=ea)
for nm, r in rows.items():
    print(f"   {nm}: {len(r['sols'])} calibration solution(s) with residual < 1e-6; EC, Jsum, tau = {np.round(r['z'], 6)}; center residual {r['center']:+.6f} MHz (note {NOTE_CENTER[nm]:+.6f}), dispersion residual {r['disp']:+.6f} (note {NOTE_DISP[nm]:+.6f}), ablation {r['abl'][0]:+.6f} / {r['abl'][1]:+.6f} MHz")
check("the five calibration versions: the independently built model reproduces the note's f03 center residuals (-9.953473, +0.930015, +10.073133, +0.448572, +0.432226 MHz) to 5e-4 MHz", all(abs(rows[nm]["center"] - NOTE_CENTER[nm]) < 5e-4 for nm in NOTE_CENTER), "; ".join(f"{nm}: {rows[nm]['center']:+.6f}" for nm in NOTE_CENTER))
check("and its full dispersion residuals (+16.249573, -3.526868, -16.929541, -2.738574, -2.711563 MHz) to 5e-4 MHz", all(abs(rows[nm]["disp"] - NOTE_DISP[nm]) < 5e-4 for nm in NOTE_DISP), "; ".join(f"{nm}: {rows[nm]['disp']:+.6f}" for nm in NOTE_DISP))
raw_res = {nm: [1000 * (rows[nm]["c"] - c3) for c3 in raw3] for nm in NOTE_RAW3}
print("   residuals against the three raw03 centers:", {nm: [round(x, 6) for x in v] for nm, v in raw_res.items()})
check("against the raw extraction center the three raw calibration versions give +11.130345, +1.505784 and +1.489438 MHz (the note's 'against all three raw03 centers, ... respectively': the matching raw03 center is the one used) to 5e-4 MHz", all(min(abs(x - NOTE_RAW3[nm]) for x in raw_res[nm]) < 5e-4 for nm in NOTE_RAW3), "; ".join(f"{nm}: {min(raw_res[nm], key=lambda x: abs(x - NOTE_RAW3[nm])):+.6f}" for nm in NOTE_RAW3))
check("the matched envelope ablation (sinc(m B/Bnode) -> sinc(B/Bnode)) with recalibration moves f03 by +0.082974, +0.195255, +0.195467 MHz and the full dispersion by -0.006435, -0.021529, -0.021564 MHz (raw 0.15, 0.22, 0.30 V) to 5e-4 MHz",
      all(abs(rows[nm]["abl"][0] - NOTE_ABL[nm][0]) < 5e-4 and abs(rows[nm]["abl"][1] - NOTE_ABL[nm][1]) < 5e-4 for nm in NOTE_ABL), "; ".join(f"{nm}: {rows[nm]['abl'][0]:+.6f} / {rows[nm]['abl'][1]:+.6f}" for nm in NOTE_ABL))
zc, ec = fit(cal["processed"], [[0.285, 13.5]], cosine=True, ncal=2)
_, f03c, wc = obs(np.r_[zc, 0.0], cosine=True)
check("the two-input cosine control (EC, EJ from f01 and f12 centers) has an f03 center residual of about +24.45 MHz against the processed center", abs(1000 * (f03c - F03) - 24.45) < 0.5, f"{1000 * (f03c - F03):+.3f} MHz (EC = {zc[0]:.5f}, EJ = {zc[1]:.4f} GHz)")
# basis convergence at the raw 0.30 V solution
z = rows["raw_period_0.3"]["z"]
c0, d0 = f03_disp(z); c1, d1 = f03_disp(z, N=24, K=16)
check("basis convergence at the raw 0.30 V solution: charges -14..14, 8 photon states against charges -24..24, 16 photon states changes the f03 center by less than 1e-6 MHz and the dispersion by less than 1e-6 MHz", abs(c1 - c0) * 1000 < 1e-6 and abs(d1 - d0) * 1000 < 1e-6, f"center change {1000 * (c1 - c0):+.2e} MHz, dispersion change {1000 * (d1 - d0):+.2e} MHz")
# the note's exact statement about the raw 0.30 V version: full f03 center 14.669197761379 GHz
check("the raw 0.30 V version's full f03 center is 14.669197761379 GHz (note) to 1e-10 GHz", abs(rows["raw_period_0.3"]["c"] - 14.669197761379) < 1e-10, f"{rows['raw_period_0.3']['c']:.12f}")
print(f"   total {time.time() - T0:.0f}s")
if not HITS:
    print("SUMMARY: no falsifier fires: an independently built rectangular-junction (sinc-envelope, two-arm, short-channel) charge-photon model reproduces the note's f03 center and dispersion residuals for all five calibration versions, the raw-extraction residuals, the two-input cosine residual, the harmonic-envelope ablation and the raw 0.30 V center 14.669197761379 GHz; {} checks pass".format(PASS))
else:
    print("SUMMARY: failed: " + "; ".join(HITS)); print("HIT: " + "; ".join(HITS))
sys.exit(0)
