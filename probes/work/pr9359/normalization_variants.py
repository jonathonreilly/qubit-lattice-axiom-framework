#!/usr/bin/env python3
"""J:attack-f:PR9359 -- NORMALIZATION: which conventions do the note's f03 numbers pin down? Factors of 2 and pi, the sinc definition, the sign and normalisation of the local harmonics, the arm phase and the charge-coupling factor.

The note says: 'Numerical values are cyclic GHz'; sinc(z) = sin(pi z)/(pi z); local coefficients normalised by minus twice the first coefficient (fundamental -cos(phi)); hopping c_|m| [Ja sinc(|m| B/Ba) + Jb sinc(|m| B/Bb) exp(i m psi)] with psi = pi;
H/h = 4 EC (n - q)^2 + V + Omega a^dag a + G (n - q)(a + a^dag). This script rebuilds the model and re-runs the raw 0.30 V calibration and the f03 comparison (center residual +0.432226 MHz, dispersion residual -2.711563 MHz against the processed record) under the note's conventions and under
single mis-normalised variants: sinc without pi, hopping without the factor 1/2 (equivalent to rescaling Jsum: expected invariant), the arm phase psi = 0, Ba and Bb swapped, a local potential of opposite sign (c_1 = +1), G doubled and halved, and 4 EC replaced by EC and by 8 EC (EC rescaling: expected invariant except through the G term).
For each variant the three low-level inputs are refit with several starts; a variant 'fails' if the fit does not reach a residual below 1e-6 or its f03 center residual differs from the note's by more than 0.05 MHz.
Prints SUMMARY:; HIT only if the note's own convention fails to reproduce its numbers or a variant that changes the physics reproduces them equally well (a convention the numbers do not pin).
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
VAR = dict(sinc='pi', hopfac=0.5, psi=np.pi, swap=False, g=1.0, cnorm=-1.0, ec4=4.0)
def sinc(z): return np.sinc(z) if VAR['sinc'] == 'pi' else (np.sin(z) / z if z != 0 else 1.0)
MMAX = 14
def cos_coeffs(tau, M=8192):
    ph = (np.arange(M) + 0.5) * 2 * np.pi / M
    s = np.sin(ph / 2) ** 2
    r = 4 * s / (1 + np.sqrt(1 - tau * s))
    a = np.array([(2.0 / M) * np.sum(r * np.cos(m * ph)) for m in range(MMAX + 1)])
    return VAR['cnorm'] * a / a[1]                              # normalised: c_1 = -1 (variant: +1)
def hops(p, ablate=False, psi=None):
    psi = VAR['psi'] if psi is None else psi
    EC, Jsum, tau = p
    c = cos_coeffs(tau)
    Ja, Jb = Jsum * (1 + ALPHA) / 2, Jsum * (1 - ALPHA) / 2
    h = np.zeros(MMAX + 1)
    for m in range(1, MMAX + 1):
        env = m if not ablate else 1
        ba, bb = (BB, BA) if VAR['swap'] else (BA, BB)
        h[m] = VAR['hopfac'] * c[m] * (Ja * sinc(env * B / ba) + Jb * sinc(env * B / bb) * np.cos(m * psi))
    return h
def gaps(p, q, ablate=False, N=14, K=8, nlev=4, cosine=False):
    EC = p[0]
    n = np.arange(-N, N + 1, dtype=float); d = len(n)
    hp = hops(p, ablate) if not cosine else np.r_[0.0, -0.5 * p[1], np.zeros(MMAX - 1)]
    hop = np.zeros((d, d))
    for m in range(1, MMAX + 1):
        hop += hp[m] * (np.eye(d, k=m) + np.eye(d, k=-m))
    h0 = np.diag(VAR['ec4'] * EC * (n - q) ** 2) + hop
    e0, v0 = np.linalg.eigh(h0)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(h0, np.eye(K)) + OM * np.kron(np.eye(d), np.diag(np.arange(K, dtype=float))) + G * VAR['g'] * np.kron(np.diag(n - q), a + a.T)
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

import warnings; warnings.filterwarnings("ignore")
T0 = time.time()
cal = load("calibration.json")["calibration_Hz"]; tg = load("targets.json")
F03 = float(tg["processed"]["f_center"]) / 1e9; D03 = float(tg["processed"]["charge_dispersion"]) / 1e9
NOTE_C, NOTE_D = +0.432226, -2.711563
def f03_disp(p, N=14, K=8):
    a, _ = gaps(p, 0.0, N=N, K=K); b, _ = gaps(p, 0.5, N=N, K=K)
    return (a[2] + b[2]) / 2, abs(a[2] - b[2])
VARIANTS = [("note's conventions", {}, "must reproduce"), ("sinc(z) = sin(z)/z (no pi)", dict(sinc="nopi"), "changes physics"), ("hopping without the factor 1/2", dict(hopfac=1.0), "rescales Jsum only: invariant"),
            ("arm phase psi = 0", dict(psi=0.0), "changes physics"), ("Ba and Bb swapped", dict(swap=True), "changes physics"), ("local potential with c_1 = +1", dict(cnorm=+1.0), "changes physics (odd harmonics flip)"),
            ("G doubled", dict(g=2.0), "changes physics"), ("G halved", dict(g=0.5), "changes physics"), ("EC term EC (n - q)^2 instead of 4 EC (n - q)^2", dict(ec4=1.0), "rescales EC; G term fixes the scale: nearly invariant"),
            ("EC term 8 EC (n - q)^2", dict(ec4=8.0), "rescales EC; nearly invariant")]
results = []
for name, sw, kind in VARIANTS:
    VAR.update(dict(sinc="pi", hopfac=0.5, psi=np.pi, swap=False, g=1.0, cnorm=-1.0, ec4=4.0)); VAR.update(sw)
    best = None
    starts = [[0.325, 30.6, 0.117], [0.3, 30.0, 0.3], [0.5, 25.0, 0.05], [0.2, 45.0, 0.6], [0.35, 60.0, 0.02]] if name != "hopping without the factor 1/2" else [[0.325, 15.3, 0.117], [0.3, 15.0, 0.3]]
    if sw.get("ec4"): starts = [[0.325 * 4 / sw["ec4"], 30.6, 0.117], [0.3, 30.0, 0.3]]
    for st in starts:
        try: z, e = fit(cal["raw_period_0.3"], [st])
        except Exception: continue
        if e < 1e-6 and 0.0 <= z[2] < 1.0 and z[0] > 0 and z[1] > 0:                    # physical transparency and positive energies only
            try: c, d = f03_disp(z)
            except ValueError: continue
            if best is None or e < best[3]: best = (z, 1000 * (c - F03), 1000 * (d - D03), e)
    results.append((name, kind, best))
    if best is None: print(f"   {name}: no calibration with a physical transparency 0 <= tau < 1 reached residual < 1e-6 ({kind})", flush=True)
    else: print(f"   {name}: calibrated (EC, Jsum, tau) = {np.round(best[0], 4).tolist()}; f03 center residual {best[1]:+.6f} MHz, dispersion residual {best[2]:+.6f} MHz  ({kind})", flush=True)
VAR.update(dict(sinc="pi", hopfac=0.5, psi=np.pi, swap=False, g=1.0, cnorm=-1.0, ec4=4.0))
base = results[0][2]
ok_base = base is not None and abs(base[1] - NOTE_C) < 5e-4 and abs(base[2] - NOTE_D) < 5e-4
print(f"[{'PASS' if ok_base else 'FAIL'}] the note's conventions reproduce its raw 0.30 V numbers (+0.432226 / -2.711563 MHz)")
phys = [(n, k, b) for n, k, b in results[1:] if k.startswith("changes physics")]
def differs(b): return b is None or abs(b[1] - NOTE_C) > 0.05 or abs(b[2] - NOTE_D) > 0.05
ok_phys = all(differs(b) for _, _, b in phys)
print(f"[{'PASS' if ok_phys else 'FAIL'}] every variant that changes the physics (sinc without pi, psi = 0, Ba/Bb swapped, c_1 = +1, G doubled or halved) either has no physical-transparency calibration or moves the f03 center by more than 0.05 MHz: {[(n, None if b is None else round(b[1], 3)) for n, _, b in phys]}")
inv = [(n, k, b) for n, k, b in results[1:] if not k.startswith("changes physics")]
print(f"   invariance variants: " + "; ".join(f"{n}: {'no fit' if b is None else '%+.6f MHz' % b[1]}" for n, _, b in inv))
ok_inv = all(b is not None and abs(b[1] - NOTE_C) < 0.5 for _, _, b in inv[:1])
print(f"[{'PASS' if ok_inv else 'FAIL'}] the hopping factor 1/2 is absorbed by Jsum (result unchanged to 0.5 MHz), as expected of a pure rescaling")
print(f"   total {time.time() - T0:.0f}s")
if ok_base and ok_phys and ok_inv:
    print("SUMMARY: no purchase: the note's conventions reproduce its numbers, and each single mis-normalisation that changes the physics (sinc without pi, arm phase 0, Ba and Bb swapped, opposite-sign local potential, G doubled or halved) either cannot calibrate or moves the f03 center residual by more than 0.05 MHz; the hopping factor 1/2 is a pure rescaling absorbed by Jsum")
else:
    print("SUMMARY: a convention is not pinned or the note's convention fails: " + str([r[0] for r in results if False])); print("HIT: normalization variants do not behave as expected: base ok = %s, physics variants all differ = %s, invariance ok = %s" % (ok_base, ok_phys, ok_inv))
sys.exit(0)
