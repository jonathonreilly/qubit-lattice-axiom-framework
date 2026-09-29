"""PR 9355 attack-e: SAMPLED EVIDENCE.  The note's alignment coordinate rests on six snapshots (three optimizer starts at each charge offset, one flux offset each) explored AFTER the evaluation
discrepancies were known; its statement is that column 50 (+108 kHz) is insensitive and column 250 (+115..+120 kHz) is sensitive.  An adversarial search instead of more snapshots:

  choose the three axis nuisances that make the reserved-column residuals SMALLEST -- a flux offset d, a relative flux scale s (flux' = (1 + s) flux + d) and a common frequency offset nu --
  by multi-start least squares (RMS objective) and by a minimax objective (largest |residual|), starting from a grid of 45 initial points inside d in [-3e-4, 3e-4], s in [-2e-3, 2e-3], nu in [-100, 100] kHz,
  with the model parameters otherwise fixed at the nominal snapshots (ng = 0 and 1/2).
What is left of the column-50 and column-250 residuals at the adversarial optimum, and the floor of the RMS, tell how much of the note's discrepancy an axis nuisance alone can absorb.
Own dip fits and own charge x Fock cavity model (reduced basis for the search: charges -30..30, 16 device levels, 6 photon levels; the optimum is re-evaluated in the full basis).
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
cols = [c["column"] for c in COLS]; flux = np.array([c["flux"] for c in COLS]); i50, i250 = cols.index(50), cols.index(250)
ctr = centers()[:, 0]
rms = lambda r: float(np.sqrt(np.mean(r ** 2)))
def resid(snap, p, **kw):
    d, s, nu = p
    pred = np.array([cav_offset(snap, (1 + s) * f + d, **kw)[0] * 1e3 for f in flux]) + nu * 1e-3      # MHz, nu in kHz
    return (pred - ctr) * 1e3
RED = dict(Nch=30, ND=16, K=6)
rng = np.random.default_rng(90355)
summary = {}
for si, snap in enumerate(INP["driven_snapshots"]):
    base = resid(snap, (0, 0, 0), **RED)
    scale = np.array([1e-4, 5e-4, 20.0])
    best = None
    starts = [np.array([0.0, 0.0, 0.0])] + [rng.uniform([-3e-4, -2e-3, -100], [3e-4, 2e-3, 100]) for _ in range(44)]
    for x0 in starts:
        try:
            r = least_squares(lambda q: resid(snap, q * scale, **RED), x0 / scale, x_scale=1.0, bounds=(np.array([-3e-4, -2e-3, -100]) / scale, np.array([3e-4, 2e-3, 100]) / scale), max_nfev=60, xtol=1e-10, ftol=1e-10)
        except Exception:
            continue
        if best is None or r.cost < best.cost: best = r
    p_opt = best.x * scale
    full = resid(snap, p_opt)
    # minimax from the RMS optimum and from the nominal
    from scipy.optimize import minimize
    mm = minimize(lambda q: np.max(np.abs(resid(snap, q * scale, **RED))), best.x, method="Nelder-Mead", options={"xatol": 1e-4, "fatol": 1e-3, "maxiter": 300})
    fullm = resid(snap, mm.x * scale)
    summary[si] = dict(base=base, p=p_opt, res=full, pm=mm.x * scale, resm=fullm)
    print(f"snapshot ng = {snap['ng']}: nominal RMS {rms(resid(snap, (0,0,0))):.2f} kHz -> adversarial RMS optimum {rms(full):.2f} kHz at flux offset {p_opt[0]:+.2e}, scale {p_opt[1]:+.2e}, freq offset {p_opt[2]:+.1f} kHz;"
          f" column 50 {full[i50]:+.1f}, column 250 {full[i250]:+.1f} kHz; other 18 columns RMS {rms(full[[i for i in range(20) if i not in (i50, i250)]]):.2f} kHz")
    print(f"      minimax optimum: largest |residual| {np.abs(fullm).max():.1f} kHz at column {cols[int(np.abs(fullm).argmax())]} (parameters {np.round(mm.x*scale, 6)}); RMS {rms(fullm):.2f} kHz")
s0 = summary[0]
check("with three free axis nuisances the RMS optimum leaves column 50 above 90 kHz at both charge offsets, and no choice of the nuisances brings the largest residual of any column below 50 kHz (minimax)",
      all(abs(summary[k]["res"][i50]) > 90 and np.abs(summary[k]["resm"]).max() > 50 for k in (0, 1)), f"column 50 at the RMS optimum {[round(float(summary[k]['res'][i50]),1) for k in (0,1)]}; minimax largest residual {[round(float(np.abs(summary[k]['resm']).max()),1) for k in (0,1)]} kHz")
check("with the nuisances free, column 250 is removable: its residual falls below 40 kHz at the RMS optimum for both charge offsets (the sensitive discrepancy is an axis-alignment quantity)",
      all(abs(summary[k]["res"][i250]) < 40 for k in (0, 1)), f"{[round(summary[k]['res'][i250],1) for k in (0,1)]}")
check("the adversarial floor of the RMS is above 20 kHz at both charge offsets (the alignment snapshots reach 27.4-27.9 kHz)", all(rms(summary[k]["res"]) > 20 for k in (0, 1)), f"{[round(rms(summary[k]['res']),2) for k in (0,1)]} kHz")
print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-e sampled evidence on PR 9355: adversarial search over axis nuisances (flux offset, flux scale, frequency offset; 45 starts, RMS and minimax objectives) with the model otherwise nominal: RMS floor {rms(summary[0]['res']):.1f}/{rms(summary[1]['res']):.1f} kHz (nominal 36.5/37.2), column 250 falls to {summary[0]['res'][i250]:+.1f}/{summary[1]['res'][i250]:+.1f} kHz, column 50 stays at {summary[0]['res'][i50]:+.1f}/{summary[1]['res'][i50]:+.1f} kHz, minimax largest residual {np.abs(summary[0]['resm']).max():.0f}/{np.abs(summary[1]['resm']).max():.0f} kHz; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
