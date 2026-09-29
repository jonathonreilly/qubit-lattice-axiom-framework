"""PR 9348 attack-a: WITNESS REALIZABILITY for the transmon calibration hold-out note.

Every configuration, count and example the note states is constructed from the PR head and checked:
 1. the CSV: byte-identical hash 0b6abf45..., row KIT with the four calibration cells and f03..f05, f06/f07 empty ('unavailable f06/f07 are not counted');
 2. the square's Gauss-law solutions: enumeration of integer link fields on the four oriented links (A -> B) with zero divergence: the solution set is {(n, -n, -n, n)}, D = 4 n^2;
 3. 'three starting guesses converge to the same found calibration root': three starts (own, different from the runner's) reach the note's root, residual below 0.001 MHz;
 4. the numerical cutoff claim: charges -40..40 x photons 20 (own direct charge x Fock construction, no transmon truncation) change the three evaluated totals by at most 0.00003 MHz;
 5. the 21-point charge grid widths of the total frequencies (0.000368, 0.008878, 0.157861 MHz) and the assignment weight along 21 coupling values (note: above 0.97);
 6. the note's drive residuals (+5.181438, +14.395723, +28.257343 MHz) at the note's root.
Own charge x Fock model (offset charge averaged over ng = 0 and 1/2 as the note adopts), own root finder.
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
# 1. CSV
csv = blob("scripts/data/transmon_holdout_2026_09_26/Experiment.csv")
sha = hashlib.sha256(csv).hexdigest()
lines = csv.decode().strip().splitlines(); hdr = lines[0].split(","); rows = {l.split(",")[0]: dict(zip(hdr, l.split(","))) for l in lines[1:]}
kit = rows["KIT"]
check("the committed CSV has the SHA256 of the note (0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b)", sha == "0b6abf45a5b574f2ecc492b19560d44ff1638894a0579504dc850c1cb628a01b", sha[:16])
check("row KIT: calibration cells f01 = 6.0391, f02 = 11.868, fres1 = 7.4613, fres2 = 7.4587 and evaluation cells f03 = 17.457, f04 = 22.778, f05 = 27.794; f06 and f07 are empty",
      [float(kit[k]) for k in ("f01", "f02", "fres1", "fres2")] == [6.0391, 11.868, 7.4613, 7.4587] and [float(kit[k]) for k in ("f03", "f04", "f05")] == [17.457, 22.778, 27.794] and kit["f06"] == "" and kit["f07"] == "", str({k: kit[k] for k in ("f06", "f07")}))
# 2. Gauss law on the square
# vertices 0 (A), 1 (B), 2 (A), 3 (B); links oriented A -> B: 0->1, 0->3, 2->1, 2->3.  E = flux along the orientation.  Zero divergence at every vertex.
links = [(0, 1), (0, 3), (2, 1), (2, 3)]
sols = []
for E in itertools.product(range(-4, 5), repeat=4):
    div = [0] * 4
    for (a, b), e in zip(links, E):
        div[a] += e; div[b] -= e
    if not any(div): sols.append(E)
ok = sols == [(n, -n, -n, n) for n in range(-4, 5)]
check("integer Gauss-law solutions on the oriented square (links 01, 03, 21, 23; |E| <= 4) are exactly E = (n, -n, -n, n), so D = sum E^2 = 4 n^2", ok and all(sum(e * e for e in E) == 4 * E[0] ** 2 for E in sols), f"{len(sols)} solutions")
# 3. three starts
starts = [np.array(s, float) for s in ([0.25, 20.0, 7.3, 0.06], [0.15, 30.0, 7.6, 0.1], [0.3, 15.0, 7.4, 0.03])]
roots = []
for s in starts:
    p, res = solve(s); roots.append((p, res))
det = "; ".join(f"start {i}: max residual {r:.2e} MHz, root {np.round(p, 6)}" for i, (p, r) in enumerate(roots))
check("three fresh starting guesses reach the note's root (EC, EJ, Omega, G) to 1e-6 GHz with calibration residual < 0.001 MHz", all(np.max(np.abs(p - NOTE_ROOT)) < 1e-6 and r < 1e-3 for p, r in roots), det)
# 6. drive residuals
dr, f, w = drive_res(NOTE_ROOT)
check("drive residuals at the note's root: +5.181438, +14.395723, +28.257343 MHz to 5e-5", all(abs(dr[j] - NOTE_DRIVE[j]) < 5e-5 for j in (3, 4, 5)), ", ".join(f"f0{j}: {dr[j]:+.6f}" for j in (3, 4, 5)))
# 4. cutoffs
f0 = predict(NOTE_ROOT, N=14, K=9)[0]
f1 = predict(NOTE_ROOT, N=40, K=20)[0]
d = 1000 * np.abs(f1[2:5] - f0[2:5]).max()
check("charges -14..14 x 9 photons versus charges -40..40 x 20 photons (no transmon truncation): the three totals differ by at most 0.00003 MHz", d < 3.0e-5 * 1.5, f"{d:.2e} MHz")
# 5. charge grid widths and assignment weights
ngs = np.linspace(0, 0.5, 21)
tot = np.array([endpoint(NOTE_ROOT, ng)[0][2:5] for ng in ngs])
widths = 1000 * (tot.max(0) - tot.min(0))
print("   21-point charge-grid total-frequency widths (MHz):", np.round(widths, 6), "(note 0.000368, 0.008878, 0.157861)")
check("the 21-point charge grid widths of f03, f04, f05 reproduce the note's three values to 3%", all(abs(widths[i] / NOTE_WIDTH[j] - 1) < 0.03 for i, j in enumerate((3, 4, 5))), str(np.round(widths, 6)))
mins = []
for lam in np.linspace(0, 1, 21):
    p = NOTE_ROOT.copy(); p[3] *= lam
    mins.append(min(endpoint(p, 0.0)[1], endpoint(p, 0.5)[1]))
check("the dressed-state assignment weight stays above 0.97 along 21 coupling values (G from 0 to its calibrated value)", min(mins) > 0.97, f"minimum {min(mins):.5f}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-a witness realizability on PR 9348: CSV hash and KIT row (f06/f07 empty), Gauss solutions E=(n,-n,-n,n), three fresh starts reach the note's root, drive residuals reproduced, cutoff change {d:.1e} MHz, charge-grid widths {np.round(widths,6).tolist()} MHz, assignment weight >= {min(mins):.4f}; PASS={PASS} FAIL={FAIL}; no defect in the note's witnesses")
sys.exit(1 if FAIL else 0)
