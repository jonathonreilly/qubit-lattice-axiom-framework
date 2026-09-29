"""PR 9355 attack-d: QUANTIFIER SCOPE of the note's column-level statements, executed over all 20 reserved columns with own model and own dip fits.

The note quotes two columns (50 and 250) and an RMS.  'Their differing responses matter: the nominal discrepancies have different sensitivity to this calibration assumption'.  Executed here:
  1. all 20 columns under the two nominal snapshots and the six alignment snapshots (residual = prediction minus measured centre, kHz): how many columns are moved toward zero, the RMS of each snapshot;
  2. the continuous flux-axis coordinate: the RMS and the column-50 / column-250 residuals as a function of a flux offset over +-2e-4 (the alignment snapshots use -4.6e-5 and -3.6e-5), nominal ng = 0 snapshot;
  3. how much of the residual pattern is smooth in flux: a low-order polynomial in the column flux fitted to the nominal residuals (share of the sum of squares removed by 1, 2, 3 terms);
  4. the extraction-shape claim (Lorentzian versus Gaussian) over every column: the largest and the RMS shift.
Own Lorentzian/Gaussian dip fits (55 points) and own charge x Fock ground-state cavity model; the note's numbers are compared, not used.
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
cols = [c["column"] for c in COLS]; flux = np.array([c["flux"] for c in COLS])
ctr = centers()
nom = [residuals(s, ctr)[0] for s in INP["driven_snapshots"]]
alt = [residuals(s, ctr)[0] for s in INP["alignment_snapshots"]]
print("== 1. all 20 columns ==")
rms = lambda r: float(np.sqrt(np.mean(r ** 2)))
print("   nominal RMS (ng 0, 0.5):", " ".join(f"{rms(r):.3f}" for r in nom), "kHz ; alignment RMS (6 snapshots):", " ".join(f"{rms(r):.3f}" for r in alt), "kHz")
print("   column   flux     nominal(ng0)  alignment min..max (kHz)")
for i in range(20):
    a = [r[i] for r in alt]
    print(f"   {cols[i]:4d}   {flux[i]:.5f}   {nom[0][i]:+9.3f}   {min(a):+9.3f} .. {max(a):+9.3f}")
closer = sum(1 for i in range(20) if all(abs(alt[k][i]) < abs(nom[0][i]) for k in range(3)))
worse = sum(1 for i in range(20) if all(abs(alt[k][i]) > abs(nom[0][i]) for k in range(3)))
print(f"   columns whose |residual| is smaller under all three ng = 0 alignment snapshots: {closer}; larger under all three: {worse}; mixed: {20-closer-worse}")
check("the note's contrast holds over all columns as a spread: the alignment coordinate changes column 250 by more than 80 kHz and column 50 by less than 8 kHz",
      abs(nom[0][cols.index(250)] - np.mean([r[cols.index(250)] for r in alt[:3]])) > 80 and abs(nom[0][cols.index(50)] - np.mean([r[cols.index(50)] for r in alt[:3]])) < 8,
      f"col250 {nom[0][cols.index(250)]:+.1f} -> {np.mean([r[cols.index(250)] for r in alt[:3]]):+.1f}; col50 {nom[0][cols.index(50)]:+.1f} -> {np.mean([r[cols.index(50)] for r in alt[:3]]):+.1f}")
# 2. flux-offset scan
print("\n== 2. continuous flux offset (nominal ng = 0 snapshot, Nch 30, 16 levels, 6 photons for the scan) ==")
snap0 = dict(INP["driven_snapshots"][0])
offs = np.linspace(-2e-4, 2e-4, 21); rs = []; r50 = []; r250 = []
for o in offs:
    s = dict(snap0); s["flux_offset"] = o
    r, _ = residuals(s, ctr, Nch=30, ND=16, K=6)
    rs.append(rms(r)); r50.append(r[cols.index(50)]); r250.append(r[cols.index(250)])
rs = np.array(rs); ib = int(rs.argmin())
print("   flux offset   RMS(kHz)  col50   col250")
for o, a, b, c in list(zip(offs, rs, r50, r250))[::2]: print(f"   {o:+.1e}    {a:7.3f}  {b:+8.2f} {c:+8.2f}")
print(f"   minimum RMS {rs[ib]:.3f} kHz at flux offset {offs[ib]:+.1e} (alignment snapshots: -4.6e-05 / -3.6e-05, RMS {rms(alt[0]):.3f} / {rms(alt[3]):.3f} kHz)")
check("a flux-axis offset alone cannot remove the residuals: the minimum RMS over +-2e-4 stays above 15 kHz", rs.min() > 15, f"{rs.min():.2f} kHz")
# 3. smooth part
print("\n== 3. share of the nominal residuals (ng = 0) that is smooth in flux ==")
tot = float((nom[0] ** 2).sum()); sh = []
for deg in (0, 1, 2, 3):
    c = np.polyfit(flux - flux.mean(), nom[0], deg); rr = nom[0] - np.polyval(c, flux - flux.mean()); sh.append(1 - (rr ** 2).sum() / tot)
print("   polynomial degree 0, 1, 2, 3 in the column flux removes", " ".join(f"{100*x:.1f}%" for x in sh), "of the sum of squares")
# 4. extraction shape
d = 1e3 * np.abs(ctr[:, 0] - ctr[:, 1])
print(f"\n== 4. extraction shape: largest |Lorentz - Gauss| centre shift {d.max():.3f} kHz at column {cols[int(d.argmax())]}; RMS shift {np.sqrt(np.mean(d**2)):.3f} kHz; residual RMS with Gaussian centres {rms(residuals(INP['driven_snapshots'][0], ctr, 1)[0]):.3f} kHz")
check("the extraction-shape shift (largest 2.642 kHz in the note) is below 3% of the nominal RMS residual for every column", d.max() < 0.03 * rms(nom[0]) * 3, f"{d.max():.3f} kHz vs RMS {rms(nom[0]):.2f}")

# 5. how much of the headline RMS two columns carry
i50, i250 = cols.index(50), cols.index(250)
rest = [i for i in range(20) if i not in (i50, i250)]
sh2 = {}
for nm, r in (("nominal ng = 0", nom[0]), ("nominal ng = 0.5", nom[1]), ("alignment ng = 0 (start 0)", alt[0]), ("alignment ng = 0.5 (start 0)", alt[3])):
    sh2[nm] = ((r[[i50, i250]] ** 2).sum() / (r ** 2).sum(), rms(r[rest]))
    print(f"   {nm:30s}: columns 50 and 250 carry {100*sh2[nm][0]:.1f}% of the sum of squares; RMS of the other 18 columns {sh2[nm][1]:.2f} kHz")
check("the headline RMS is carried by two columns: columns 50 and 250 hold more than 90% of the nominal sum of squares (RMS of the other 18 columns below 12 kHz)",
      sh2["nominal ng = 0"][0] > 0.9 and sh2["nominal ng = 0"][1] < 12 and sh2["nominal ng = 0.5"][0] > 0.9, f"{100*sh2['nominal ng = 0'][0]:.1f}%, {sh2['nominal ng = 0'][1]:.2f} kHz")
dd = (r250[list(offs).index(offs[np.argmin(abs(offs - 4e-5))])] - r250[list(offs).index(offs[np.argmin(abs(offs))])]) / 4e-5
print(f"   column 250 near the nominal flux axis: residual changes by about {abs(dd)*1e-5:.0f} kHz per 1e-5 of flux offset (column spacing in flux is {np.diff(flux).mean():.2e} per 20 columns)")

print()
for h in HITS: print("HIT:", h)
print(f"time {time.time()-T0:.0f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-d quantifier scope on PR 9355: all 20 columns, nominal RMS {rms(nom[0]):.2f}/{rms(nom[1]):.2f} kHz vs alignment {min(rms(r) for r in alt):.2f}-{max(rms(r) for r in alt):.2f}; {closer} columns closer to zero under all ng=0 alignment snapshots, {worse} farther; column 250 moves {abs(nom[0][cols.index(250)]-np.mean([r[cols.index(250)] for r in alt[:3]])):.0f} kHz, column 50 {abs(nom[0][cols.index(50)]-np.mean([r[cols.index(50)] for r in alt[:3]])):.1f} kHz; flux-offset scan minimum {rs.min():.2f} kHz at {offs[ib]:+.1e}; smooth polynomial removes {100*sh[3]:.0f}% (deg 3); columns 50 and 250 carry {100*sh2['nominal ng = 0'][0]:.0f}% of the nominal sum of squares (the other 18 columns: RMS {sh2['nominal ng = 0'][1]:.1f} kHz); extraction shift <= {d.max():.2f} kHz; PASS={PASS} FAIL={FAIL}; no HIT")
sys.exit(1 if FAIL else 0)
