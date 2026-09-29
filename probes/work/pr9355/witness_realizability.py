"""PR 9355 attack-a: WITNESS REALIZABILITY for the driven-SQUID resonator comparison note.

The note's evaluation objects exist and behave as stated, rebuilt from the packaged data with own code:
 1. structure: 20 reserved columns 10, 30, ..., 390 with 55-point signals each on one frequency axis (MHz offsets from 7.6918 GHz); 22 calibration columns 0, 20, ..., 400 plus 197, disjoint from the
    reserved ones; two nominal driven snapshots (ng = 0 and 1/2); six alignment snapshots (three starts at each ng); 
 2. own Lorentzian-plus-linear-background dip fit of every column (55 points) and the Gaussian repeat; every dip centre lies inside the measured axis, none on its edge;
 3. own ground-state cavity calculation (charge -40..40, 24 device levels, 7 photon levels; the coupled eigenstates with largest overlaps with the bare (ground, 0) and (ground, 1)): the label weights,
    the RMS residuals 36.453 / 37.235 kHz, column 50 (+108.149 / +108.519 kHz) and column 250 (+114.807 / +120.441 kHz);
 4. the six alignment snapshots' column 50 (+113.27..+113.62 kHz) and column 250 (+17.18..+28.98 kHz).
Residual = prediction minus measured centre; all in kHz.  Own model, own fits.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import json, re, subprocess, sys, time
from pathlib import Path
import numpy as np
from scipy.linalg import expm

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
PR = 9355
D = "data/driven_squid_resonator_2026_09_27"
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
    ent = git("ls-tree", HEAD, path).stdout.decode().split()
    if len(ent) < 4: raise SystemExit(f"{path} not in the PR head")
    return git("cat-file", "-p", ent[2]).stdout
INP = json.loads(blob(f"{D}/inputs.json")); MEAS = json.loads(blob(f"{D}/measurements.json"))

def device_h(EC, J, a_asym, f, EL, ng, N):
    n = np.arange(-N, N + 1, dtype=float); d = len(n)
    Jl, Jr = J * (1 + a_asym), J * (1 - a_asym)
    H = np.diag(4 * EC * (n - ng) ** 2).astype(complex)
    up1 = np.eye(d, k=-1); up2 = np.eye(d, k=-2)
    c1 = lambda ph: -(np.exp(1j * ph) * up1 + np.exp(-1j * ph) * up1.T) / 2
    c2 = lambda ph: (np.exp(1j * ph) * up2 + np.exp(-1j * ph) * up2.T) / 2
    H += Jl * c1(0.0) + Jr * c1(2 * np.pi * f)
    H += (Jl ** 2 * c2(0.0) + Jr ** 2 * c2(4 * np.pi * f)) / (4 * EL) * 1.0
    return H, np.diag(n)
from scipy.optimize import least_squares
XF = np.array(MEAS["frequency_offset_MHz"]); COLS = MEAS["columns"]
def fit_dip(y, shape):
    c0 = XF[int(np.argmin(y))]
    def model(p):
        b0, b1, A, c, w = p; u = (XF - c) / w
        dip = A / (1 + u ** 2) if shape == "lor" else A * np.exp(-0.5 * u ** 2)
        return b0 + b1 * (XF - XF.mean()) - dip
    r = least_squares(lambda p: model(p) - y, [np.median(y), 0.0, np.median(y) - y.min(), c0, 0.05], x_scale=[0.1, 0.1, 0.1, 0.02, 0.02], xtol=1e-14, ftol=1e-14, gtol=1e-14)
    return r.x
def centers():
    out = []
    for c in COLS:
        y = np.array(c["signal"]); out.append((fit_dip(y, "lor")[3], fit_dip(y, "gau")[3]))
    return np.array(out)                     # MHz, (lorentz, gauss)
def cav_offset(snap, flux, Nch=40, ND=24, K=7):
    EC, J, aa = snap["params"]; ng = snap["ng"]; G = snap["G_GHz"]; Om = snap["Omega_GHz"]; off = snap["offset_GHz"]
    Hd, nop = device_h(EC, J, aa, flux + snap.get("flux_offset", 0.0), INP["EL_GHz"], ng, Nch)
    ev, V = np.linalg.eigh(Hd)
    Ed = ev[:ND] - ev[0]; nd = V[:, :ND].conj().T @ nop @ V[:, :ND]
    a = np.diag(np.sqrt(np.arange(1, K)), 1); P = 1j * (a.T - a)
    H0 = np.kron(np.diag(Ed), np.eye(K)) + Om * np.kron(np.eye(ND), np.diag(np.arange(K, dtype=float))) + G * np.kron(nd, P)
    e, U = np.linalg.eigh(H0)
    def lab(d, k):
        b = np.zeros(ND * K); b[d * K + k] = 1; ov = np.abs(U.conj().T @ b) ** 2; i = int(np.argmax(ov)); return i, ov[i]
    i0, w0 = lab(0, 0); i1, w1 = lab(0, 1)
    return (e[i1] - e[i0]) - Om + off, min(w0, w1)
def residuals(snap, ctr, which=0, **kw):
    pred = []; wmin = 1.0
    for c in COLS:
        p, w = cav_offset(snap, c["flux"], **kw); pred.append(p * 1e3); wmin = min(wmin, w)
    return (np.array(pred) - ctr[:, which]) * 1e3, wmin      # kHz

T0 = time.time()
cols = [c["column"] for c in COLS]
check("20 reserved columns 10, 30, ..., 390 with 55-point signals on a 55-point axis (MHz offsets), calibration columns 0, 20, ..., 400 plus 197 (22 in all) disjoint from them",
      cols == list(range(10, 391, 20)) and all(len(c["signal"]) == 55 for c in COLS) and len(XF) == 55 and sorted(INP["calibration_columns"]) == sorted(list(range(0, 401, 20)) + [197]) and not set(cols) & set(INP["calibration_columns"]) and len(INP["calibration_columns"]) == 22,
      f"axis {XF.min():.2f}..{XF.max():.2f} MHz")
check("two nominal driven snapshots (ng = 0, 0.5) and six alignment snapshots (ng = 0 x3, 0.5 x3, start deltas 0, -1e-4, +1e-4)",
      [s["ng"] for s in INP["driven_snapshots"]] == [0, 0.5] and sorted((s["ng"], s["start_delta"]) for s in INP["alignment_snapshots"]) == [(0, -0.0001), (0, 0), (0, 0.0001), (0.5, -0.0001), (0.5, 0), (0.5, 0.0001)])
ctr = centers()
inside = all(XF.min() + 0.05 < ctr[i, j] < XF.max() - 0.05 for i in range(20) for j in (0, 1))
check("all 20 fitted dip centres (Lorentzian and Gaussian) lie well inside the measured axis (0.05 MHz margin)", inside, f"centres {ctr[:,0].min():.3f}..{ctr[:,0].max():.3f} MHz")
shift = 1e3 * np.abs(ctr[:, 0] - ctr[:, 1]).max()
check("changing the extraction shape moves the centres by at most 2.642 kHz (note): own value within 0.01 kHz", abs(shift - 2.642) < 0.01, f"{shift:.4f} kHz")
NOTE = {0: (36.453, 108.149, 114.807), 1: (37.235, 108.519, 120.441)}
res = {}
for si, snap in enumerate(INP["driven_snapshots"]):
    r, w = residuals(snap, ctr); res[si] = r
    rms = float(np.sqrt(np.mean(r ** 2))); c50 = r[cols.index(50)]; c250 = r[cols.index(250)]
    check(f"nominal snapshot ng = {snap['ng']}: RMS {NOTE[si][0]} kHz, column 50 {NOTE[si][1]:+.3f}, column 250 {NOTE[si][2]:+.3f} kHz reproduced to 5e-3 kHz; label weights >= {w:.4f} (unique labels)",
          abs(rms - NOTE[si][0]) < 5e-3 and abs(c50 - NOTE[si][1]) < 5e-3 and abs(c250 - NOTE[si][2]) < 5e-3 and w > 0.9, f"RMS {rms:.4f}, col50 {c50:+.4f}, col250 {c250:+.4f}")
a50, a250 = [], []
for snap in INP["alignment_snapshots"]:
    r, _ = residuals(snap, ctr); a50.append(r[cols.index(50)]); a250.append(r[cols.index(250)])
check("the six alignment snapshots give column 50 in +113.27..+113.62 kHz and column 250 in +17.18..+28.98 kHz (note, 'about'): own ranges within 0.05 kHz",
      abs(min(a50) - 113.27) < 0.05 and abs(max(a50) - 113.62) < 0.05 and abs(min(a250) - 17.18) < 0.05 and abs(max(a250) - 28.98) < 0.05, f"col50 {min(a50):+.3f}..{max(a50):+.3f}, col250 {min(a250):+.3f}..{max(a250):+.3f}")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-a witness realizability on PR 9355: structure (20 reserved + 22 calibration columns, 55-point signals, 2 nominal + 6 alignment snapshots) confirmed; own Lorentzian/Gaussian dip fits (max shape shift {shift:.3f} kHz) and own charge x Fock ground-state cavity model reproduce the nominal RMS {np.sqrt(np.mean(res[0]**2)):.3f}/{np.sqrt(np.mean(res[1]**2)):.3f} kHz, columns 50 and 250, and the six alignment ranges; PASS={PASS} FAIL={FAIL}; no defect in the note's witnesses")
sys.exit(1 if FAIL else 0)
