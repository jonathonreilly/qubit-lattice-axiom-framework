#!/usr/bin/env python3
"""J:attack-b:PR9359 -- SAME TEST, BOTH SIDES: is the f03 transfer of the rectangular-junction (sinc-envelope, two-junction, transparency) model specific to that microscopic content?

Claim attacked (note MICROSCOPIC_TRANSMON_TRANSFER_OPEN_GATE_NOTE_2026-09-27, abstract and "Comparisons and matched mechanism control"): a uniform rectangular junction multiplies its m-th local Josephson harmonic by signed sinc(m B/Bnode); applied to a supplied
two-junction circuit (alpha = .442, B = .15 T, transparency tau) and calibrated to three low-level inputs (f01 center, f12 center, full f01 dispersion; EC, Jsum, tau), the full f03 center differs from the processed source center by
-9.953473 (archived), +0.930015 (processed), +10.073133 (raw start 0.15 V, not converged), +0.448572 (raw 0.22 V) and +0.432226 MHz (raw 0.30 V), against about +24.45 MHz for the cosine (two inputs); "improvement belongs to the complete conditional model
and extra low-level calibration, not solely to the spatial envelope" (the matched envelope ablation moves f03 by +0.083..+0.195 MHz).
Same test on both sides: give the cosine the SAME three inputs and one added parameter that carries none of the microscopic content, a free second harmonic r2 (V = -J(cos phi + r2 cos 2 phi), 3 parameters EC, J, r2), and apply the identical procedure
(physical-offset Hamiltonian 4 EC (n - q)^2 + V + Omega a^dag a + G (n - q)(a + a^dag), Omega = 7.544917319789201, G = 0.07352541358551871 GHz, q = 0 and 1/2 endpoint mean, dressed levels labelled by bare overlap; exact three-input calibration; f03 center against the processed
source center 14.668765535 GHz). Also a free third harmonic r3 and the two-input cosine as controls. Inputs are the PR's committed calibration.json and targets.json (read via git). The model is built here. Floating point. Prints SUMMARY: and, only if the
generic second harmonic matches or beats the microscopic model's residual pattern, HIT:.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/microscopic-transmon-20260927"
DD = "data/microscopic_transmon_2026_09_27"
T0 = time.time()
RESULTS, FIRED = [], []
OM, G = 7.544917319789201, 0.07352541358551871
NOTE = {"archive": -9.953473, "processed": +0.930015, "raw_period_0.15": +10.073133, "raw_period_0.22": +0.448572, "raw_period_0.3": +0.432226}


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def load(name):
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{DD}/{name}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"cannot read {name}: {r.stderr[:200]}")
    return json.loads(r.stdout)


def gaps(p, shape, q, N=12, K=8, nlev=4):
    EC, J, r = p
    n = np.arange(-N, N + 1, dtype=float); d = len(n)
    hop = -0.5 * J * (np.eye(d, k=1) + np.eye(d, k=-1))
    if shape == "h2":
        hop = hop - 0.5 * J * r * (np.eye(d, k=2) + np.eye(d, k=-2))
    if shape == "h3":
        hop = hop - 0.5 * J * r * (np.eye(d, k=3) + np.eye(d, k=-3))
    h0 = np.diag(4 * EC * (n - q) ** 2) + hop
    e0, v0 = np.linalg.eigh(h0)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(h0, np.eye(K)) + OM * np.kron(np.eye(d), np.diag(np.arange(K, dtype=float))) + G * np.kron(np.diag(n - q), a + a.T)
    w, V = np.linalg.eigh(h)
    lev = []
    for j in range(nlev):
        pr = np.abs(np.kron(v0[:, j], np.eye(K)[:, 0]) @ V) ** 2
        i = int(np.argmax(pr)); lev.append((w[i], pr[i], i))
    if len({l[2] for l in lev}) < nlev or min(l[1] for l in lev) < 0.5:
        raise ValueError("unassignable")
    return np.array([lev[j][0] - lev[0][0] for j in range(1, nlev)]), min(l[1] for l in lev)


def obs(p, shape):
    a, wa = gaps(p, shape, 0.0); b, wb = gaps(p, shape, 0.5)
    c = (a + b) / 2
    return np.array([c[0], c[1] - c[0], abs(a[0] - b[0])]), c[2], min(wa, wb)


def fit(cal3, shape, starts, ncal=3):
    tgt = np.array([cal3[0] / 1e9, cal3[1] / 1e9, cal3[2] / 1e9])
    best = None
    for st in starts:
        def res(z):
            try:
                o, _, _ = obs(z if len(z) == 3 else np.r_[z, 0.0], shape)
            except ValueError:
                return np.full(ncal, 10.0)
            return ((o - tgt) / np.array([1, 1, 1e-3]))[:ncal]
        r = least_squares(res, st, x_scale=[0.2, 10, 0.05][:len(st)], ftol=1e-14, xtol=1e-14, gtol=1e-14, max_nfev=300)
        e = float(np.max(np.abs(r.fun)))
        if best is None or e < best[1]:
            best = (r.x, e)
    return best


def run():
    cal = load("calibration.json")["calibration_Hz"]
    F03 = float(load("targets.json")["processed"]["f_center"]) / 1e9
    rows = {}
    for nm in NOTE:
        c = cal[nm]
        z2, e2 = fit(c, "h2", [[0.285, 13.5, 0.0], [0.3, 13, 0.02], [0.28, 14, -0.02]])
        z3, e3 = fit(c, "h3", [[0.285, 13.5, 0.0], [0.3, 13, 0.005], [0.28, 14, -0.005]])
        zc, ec = fit(c, "h2", [[0.285, 13.5]], ncal=2)
        _, f03_2, w2 = obs(z2, "h2"); _, f03_3, w3 = obs(z3, "h3"); _, f03_c, wc = obs(np.r_[zc, 0.0], "h2")
        rows[nm] = dict(h2=(z2, e2, 1000 * (f03_2 - F03), w2), h3=(z3, e3, 1000 * (f03_3 - F03), w3), cos=(zc, ec, 1000 * (f03_c - F03)))
    for nm, r in rows.items():
        print(f"   {nm}: note (microscopic) {NOTE[nm]:+.3f} MHz | generic cos + r2 (3 inputs, r2 = {r['h2'][0][2]:+.5f}): {r['h2'][2]:+.3f} | cos + r3: {r['h3'][2]:+.3f} | cosine (2 inputs): {r['cos'][2]:+.3f}  (calibration errors {r['h2'][1]:.0e}, {r['h3'][1]:.0e}, {r['cos'][1]:.0e})", flush=True)
    okcos = abs(rows["processed"]["cos"][2] - 24.45) < 0.5
    check("(B0) the two-input cosine reproduces the note's 'about +24.45 MHz' center residual (processed calibration)", okcos, f"{rows['processed']['cos'][2]:+.3f} MHz")
    conv = ["archive", "processed", "raw_period_0.22", "raw_period_0.3"]
    diffs = {nm: rows[nm]["h2"][2] - NOTE[nm] for nm in NOTE}
    closer = all(abs(rows[nm]["h2"][2]) <= abs(NOTE[nm]) for nm in conv if nm != "archive")
    same_pattern = all(abs(diffs[nm]) < 0.6 for nm in NOTE)
    check("(B1) same test both sides: a generic cosine + free second harmonic fitted to the same three inputs reproduces the note's f03 residuals in every calibration version to within 0.6 MHz, and is closer to the target in the three converged non-archived versions",
          same_pattern and closer, "; ".join(f"{nm}: {rows[nm]['h2'][2]:+.3f} vs {NOTE[nm]:+.3f}" for nm in NOTE))
    print(f"   [total {time.time() - T0:.0f} s]", flush=True)
    if same_pattern and closer:
        print("SUMMARY: SEPARATION IS NOT SPECIFIC TO THE MICROSCOPIC CONTENT: with the same three low-level inputs, a cosine plus ONE free second harmonic (r2 = " + f"{rows['raw_period_0.3']['h2'][0][2]:+.4f}" + " for the raw 0.30 V calibration; no sinc envelope, no two-junction geometry, no transparency) gives f03 center residuals "
              + ", ".join(f"{rows[nm]['h2'][2]:+.3f}" for nm in NOTE) + " MHz against the note's " + ", ".join(f"{NOTE[nm]:+.3f}" for nm in NOTE) + " MHz (archived, processed, raw 0.15, 0.22, 0.30 V), and is closer to the processed target than the microscopic model in the converged versions; the two-input cosine stays at about +24 MHz")
        print("HIT: PR #9359 the f03 'transfer' does not test the rectangular-junction (sinc-envelope) content: the improvement over the cosine comes from the third calibration input and any added harmonic, as the same test on the cosine with one free second harmonic shows; "
              + "; ".join(f"{nm}: generic {rows[nm]['h2'][2]:+.3f} vs microscopic {NOTE[nm]:+.3f}" for nm in NOTE))
        return 0
    print("SUMMARY: pattern has no purchase: a generic second harmonic does not reproduce the microscopic model's f03 residual pattern")
    return 0


if __name__ == "__main__":
    sys.exit(run())
