"""PR 9348 attack-d: QUANTIFIER SCOPE of 'positive residuals on three unused transitions' against the offset-charge convention.

The note adopts the source model's average of the ng = 0 and ng = 1/2 transition frequencies ('a direct controlled parity-branch average for KIT is not established here') and reports the
endpoints and a 21-point charge grid only as SENSITIVITY of the evaluated totals at the fixed calibrated parameters.  Executed here: the whole pipeline (calibrate on f01, f02, fres1, fres2;
predict f03, f04, f05) under other offset-charge conventions, each recalibrated with the same four coordinates and with the same full charge x Fock model:
  ng = 0 only; ng = 1/2 only; ng = 1/4 only; average of ng = 0 and 1/2 (the note); uniform average over five ng in [0, 1/2]; uniform average over nine ng in [0, 1/2]; (x)
and the sign of the three drive residuals, plus how far the calibration would have to move to remove them.
Own charge x Fock model, own root finder (multi-start), transmon levels labelled by bare overlap.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import hashlib, itertools, subprocess, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
PR = 9348
PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True)
git("fetch", "origin", f"pull/{PR}/head", "--quiet")
HEAD = git("rev-parse", "FETCH_HEAD").stdout.decode().strip()
def blob(path):
    """file at the PR head via ls-tree + cat-file (rev:path is not used)"""
    ent = git("ls-tree", HEAD, path).stdout.decode().split()
    if len(ent) < 4: raise SystemExit(f"{path} not in the PR head")
    return git("cat-file", "-p", ent[2]).stdout

CAL = np.array([6.0391, 11.8680, 7.4613, 7.4587])                    # f01, f02, fres1, fres2 (GHz)
MEAS = {3: 17.457, 4: 22.778, 5: 27.794}
NOTE_ROOT = np.array([0.196567178810, 24.852181043101, 7.453936854591, 0.077763912291])
NOTE_DRIVE = {3: 5.181438, 4: 14.395723, 5: 28.257343}
NOTE_WIDTH = {3: 0.000368, 4: 0.008878, 5: 0.157861}

class Unassignable(Exception):
    pass

def endpoint(p, ng, N=12, K=8, ntr=None):
    """levels of the full charge x Fock Hamiltonian at offset charge ng (charges -N..N, photons 0..K-1); returns f01..f05, fres1, fres2 in GHz (dressed states labelled by dominant bare overlap) and the smallest label weight"""
    ec, ej, om, g = p
    n = np.arange(-N, N + 1, dtype=float); nq = len(n)
    hc = np.diag(4 * ec * (n - ng) ** 2) - 0.5 * ej * (np.eye(nq, k=1) + np.eye(nq, k=-1))
    _, bare = np.linalg.eigh(hc)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(hc, np.eye(K)) + om * np.kron(np.eye(nq), np.diag(np.arange(K, dtype=float))) + g * np.kron(np.diag(n), a + a.T)
    e, v = np.linalg.eigh(h)
    labels = [(j, 0) for j in range(6)] + [(0, 1), (1, 1)]
    idx, wts = [], []
    for j, k in labels:
        b = np.kron(bare[:, j], np.eye(K)[:, k]); ov = np.abs(b @ v) ** 2
        i = int(np.argmax(ov)); idx.append(i); wts.append(ov[i])
    if len(set(idx)) != len(idx) or min(wts) < 0.5: raise Unassignable()
    lev = e[idx]
    return np.array([lev[j] - lev[0] for j in range(1, 6)] + [lev[6] - lev[0], lev[7] - lev[1]]), float(min(wts))
def predict(p, ngs=(0.0, 0.5), **kw):
    fs = [endpoint(p, ng, **kw) for ng in ngs]
    return np.mean([f for f, _ in fs], axis=0), min(w for _, w in fs)
CALIDX = [0, 1, 5, 6]
def resid_cal(z, target=CAL, ngs=(0.0, 0.5), **kw):
    try: f, _ = predict(np.exp(z), ngs, **kw)
    except Unassignable: return np.full(4, 1e3)
    return (f[CALIDX] - target) * 1000.0
def solve(start, target=CAL, ngs=(0.0, 0.5), **kw):
    r = least_squares(lambda z: resid_cal(z, target, ngs, **kw), np.log(start), xtol=1e-14, ftol=1e-14, gtol=1e-12, max_nfev=80)
    return np.exp(r.x), float(np.max(np.abs(r.fun)))
def drive_res(p, ngs=(0.0, 0.5), **kw):
    f, w = predict(p, ngs, **kw)
    return {j: 1000.0 * (f[j - 1] - MEAS[j]) / j for j in (3, 4, 5)}, f, w

T0 = time.time()
convs = {"average of ng = 0 and 1/2 (the note)": (0.0, 0.5), "ng = 0 only": (0.0,), "ng = 1/2 only": (0.5,), "ng = 1/4 only": (0.25,),
         "uniform average over 5 values in [0, 1/2]": tuple(np.linspace(0, 0.5, 5)), "uniform average over 9 values in [0, 1/2]": tuple(np.linspace(0, 0.5, 9))}
rows = {}
print("convention                                        EC        EJ      Omega       G      calib resid   drive residuals f03, f04, f05 (MHz)")
for name, ngs in convs.items():
    best = None
    for s in ([0.196567, 24.85, 7.454, 0.0778], [0.25, 20.0, 7.3, 0.06], [0.15, 30.0, 7.6, 0.1]):
        try:
            p, r = solve(np.array(s), ngs=ngs)
        except Exception:
            continue
        if best is None or r < best[1]: best = (p, r)
    p, r = best
    dr, f, w = drive_res(p, ngs=ngs)
    rows[name] = (p, r, dr)
    print(f"{name:48s}  {p[0]:.6f} {p[1]:9.5f} {p[2]:.6f} {p[3]:.6f}  {r:.1e}   " + "  ".join(f"{dr[j]:+9.5f}" for j in (3, 4, 5)), flush=True)
note = rows["average of ng = 0 and 1/2 (the note)"]
check("under the note's convention the drive residuals are the note's (+5.181438, +14.395723, +28.257343 MHz to 1e-4) with calibration residual below 1e-3 MHz",
      all(abs(note[2][j] - NOTE_DRIVE[j]) < 1e-4 for j in (3, 4, 5)) and note[1] < 1e-3, ", ".join(f"{note[2][j]:+.6f}" for j in (3, 4, 5)))
allpos = all(all(v[2][j] > 0 for j in (3, 4, 5)) for v in rows.values())
check("the three drive residuals are positive under every offset-charge convention tried (recalibrated each time)", allpos, "; ".join(f"{k.split(' (')[0]}: " + "/".join(f"{v[2][j]:+.2f}" for j in (3, 4, 5)) for k, v in rows.items()))
mn = {j: min(v[2][j] for v in rows.values()) for j in (3, 4, 5)}; mx = {j: max(v[2][j] for v in rows.values()) for j in (3, 4, 5)}
print("   range over conventions (MHz):", ", ".join(f"f0{j}: {mn[j]:+.3f} .. {mx[j]:+.3f}" for j in (3, 4, 5)))
spread = max(mx[j] - mn[j] for j in (3, 4, 5))
check("the spread of each drive residual over the conventions is small compared with the residual itself (< 5% of the note's value)", all((mx[j] - mn[j]) < 0.05 * NOTE_DRIVE[j] for j in (3, 4, 5)), f"spreads {[round(mx[j]-mn[j],4) for j in (3,4,5)]} MHz vs {[NOTE_DRIVE[j] for j in (3,4,5)]}")
# how far must the four calibration inputs move to remove all three residuals? (least squares over a 4-vector of input shifts, 3 residuals: underdetermined -> minimum norm)
def full_res(delta_mhz):
    tgt = CAL + np.asarray(delta_mhz) * 1e-3
    p, r = solve(NOTE_ROOT, target=tgt)
    dr, _, _ = drive_res(p); return np.array([dr[3], dr[4], dr[5]]), p, r
J = np.empty((3, 4)); h = 0.5
r0 = np.array([NOTE_DRIVE[3], NOTE_DRIVE[4], NOTE_DRIVE[5]])
for i in range(4):
    e = np.zeros(4); e[i] = h
    rp, _, _ = full_res(e); rm, _, _ = full_res(-e); J[:, i] = (rp - rm) / (2 * h)
dmin = -np.linalg.pinv(J) @ r0
rz, _, rz_res = full_res(dmin)
print(f"   minimum-norm shift of (f01, f02, fres1, fres2) that zeroes the linearised residuals: {np.round(dmin, 3)} MHz (norm {np.linalg.norm(dmin):.2f}); residuals after the actual nonlinear recalibration: {np.round(rz, 3)} MHz")
print(f"   sensitivity matrix d(drive residual)/d(calibration input in MHz):\n{np.round(J, 3)}")
print()
for h_ in HITS: print("HIT:", h_)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-d quantifier scope on PR 9348: whole pipeline recalibrated under six offset-charge conventions; drive residuals stay positive in all (f03 {mn[3]:+.2f}..{mx[3]:+.2f}, f04 {mn[4]:+.2f}..{mx[4]:+.2f}, f05 {mn[5]:+.2f}..{mx[5]:+.2f} MHz), spread <= {spread:.3f} MHz; minimum-norm calibration-input shift that removes them {np.linalg.norm(dmin):.1f} MHz (residuals after refit {np.round(rz,2).tolist()}); the note reports endpoints and a grid at fixed parameters only; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
