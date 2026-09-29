#!/usr/bin/env python3
"""J:attack-e:PR9359 -- SAMPLED EVIDENCE: the note's calibrations are local least-squares returns from a few starts ('All shape starts', 'shape start 0.01'); 'no global-optimum claim follows', but its f03 comparison is stated for the returned solution of each calibration version.

Three inputs (f01 center, f12 center, full f01 dispersion) fix three shape parameters (EC, Jsum, tau), so a different root of the same three equations would give a different f03 prediction. Instead of more hand-picked starts, this script searches for other roots adversarially:
for each of the five calibration versions, 300 uniformly random starts over EC in (0.08, 0.9), Jsum in (8, 80), tau in (0, 0.98) (own model of the rectangular-junction two-arm short-channel transmon built from the note's text), least squares to the three inputs, and a list of the
distinct converged solutions (residual below 1e-6 in the fit units) with their f03 residuals; plus a coarse grid scan of the residual norm over the whole box to see whether any other basin exists that random starts miss.
Prints SUMMARY:; HIT only if a second calibration root with a different f03 prediction exists.
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

import warnings; warnings.filterwarnings("ignore")
T0 = time.time()
cal = load("calibration.json")["calibration_Hz"]; F03 = float(load("targets.json")["processed"]["f_center"]) / 1e9
rng = np.random.default_rng(5)
allsols = {}
for nm in ("archive", "processed", "raw_period_0.15", "raw_period_0.22", "raw_period_0.3"):
    sols = []; ok = 0; nst = 300
    for i in range(nst):
        st = [rng.uniform(0.08, 0.9), rng.uniform(8, 80), rng.uniform(0.0, 0.98)]
        try: z, e = fit(cal[nm], [st])
        except Exception: continue
        if e < 1e-6 and z[0] > 0 and z[1] > 0 and 0 <= z[2] < 1:
            ok += 1
            if not any(np.allclose(z, y[0], rtol=1e-4, atol=1e-5) for y in sols):
                _, f03, w = obs(z); sols.append((z, 1000 * (f03 - F03), w))
    allsols[nm] = (ok, sols)
    print(f"   {nm}: {ok} of {nst} random starts converged; {len(sols)} distinct solution(s): " + "; ".join(f"EC, Jsum, tau = {np.round(z, 5).tolist()} -> f03 residual {r:+.4f} MHz" for z, r, w in sols) + f"  [{time.time() - T0:.0f}s]", flush=True)
ok_unique = all(len(allsols[nm][1]) == 1 for nm in allsols)
print("[%s] every calibration version has exactly one root of its three equations found by 300 random starts over the whole box (f03 prediction is not root-dependent)" % ("PASS" if ok_unique else "FAIL"))
# coarse grid: does the residual norm have any other zero-level basin?
ECg = np.linspace(0.08, 0.9, 18); Jg = np.linspace(8, 80, 19); Tg = np.linspace(0.0, 0.95, 12)
tgt = np.array([cal["raw_period_0.3"][0] / 1e9, cal["raw_period_0.3"][1] / 1e9, cal["raw_period_0.3"][2] / 1e9])
best = []
for ec in ECg:
    for j in Jg:
        for t in Tg:
            try: o, _, _ = obs([ec, j, t])
            except ValueError: continue
            best.append((float(np.linalg.norm((o - tgt) / np.array([1, 1, 1e-3]))), ec, j, t))
best.sort()
print(f"   coarse grid ({len(ECg) * len(Jg) * len(Tg)} points) residual norm (raw 0.30 V inputs): smallest {best[0][0]:.3f} at (EC, Jsum, tau) = ({best[0][1]:.3f}, {best[0][2]:.2f}, {best[0][3]:.2f}); count of grid points within 1.0 of a zero-level basin: {sum(1 for b in best if b[0] < 1.0)}")
print(f"   total {time.time() - T0:.0f}s")
if ok_unique:
    print("SUMMARY: no purchase: 300 random starts per calibration version over EC 0.08-0.9, Jsum 8-80, tau 0-0.98 find exactly one root of the three-input equations in each of the five versions, so the f03 comparison does not depend on which root a start converges to (unlike the two-input cosine model of the sibling holdout note, which has a second root)")
else:
    print("SUMMARY: a second calibration root exists: " + str({nm: len(v[1]) for nm, v in allsols.items()})); print("HIT: a second root with a different f03 prediction exists")
sys.exit(0)
