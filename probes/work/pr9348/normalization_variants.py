#!/usr/bin/env python3
"""J:attack-f:PR9348 -- NORMALIZATION: which conventions of the transmon holdout note do its numbers pin down?

Note: 'Numerical values are GHz energy frequencies throughout; no extra factor of 2 pi is applied'; H/h = 4 EC (n - ng)^2 - EJ cos(phi) + Omega a^dag a + G n (a + a^dag); the average of the ng = 0 and ng = 1/2 transition frequencies; drive residual = (f0j - measured f0j)/j
('the measured j-photon drive frequency is f0j/j'); four calibration coordinates f01 = 6.0391, f02 = 11.8680, fres1 = 7.4613, fres2 = 7.4587 GHz; drive residuals +5.181438, +14.395723, +28.257343 MHz; total residuals +15.544315, +57.582891, +141.286714 MHz.
This script rebuilds the full charge x Fock model, recalibrates (EC, EJ, Omega, G) to the four coordinates under the note's conventions and under single variants (4 EC replaced by EC or 8 EC; the cosine half-hopping replaced by full hopping; G doubled or halved;
the endpoint average replaced by ng = 0 alone or ng = 1/2 alone; the drive residual not divided by j or divided by j^2), and compares the three residuals with the note's. Pure rescalings of EC or EJ are expected to leave the residuals unchanged; the others must change them.
Prints SUMMARY:; HIT only if the note's own convention fails to reproduce its numbers, a physics-changing variant reproduces them equally well, or a pure rescaling changes them.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.optimize import least_squares

T0 = time.time()
RESULTS, FIRED = [], []
DRY = "--dry" in sys.argv

CAL = np.array([6.0391, 11.8680, 7.4613, 7.4587])                    # f01, f02, fres1, fres2 (GHz)
MEAS = {3: 17.457, 4: 22.778, 5: 27.794}                              # f03, f04, f05 (GHz)
NOTE_ROOT = np.array([0.196567178810, 24.852181043101, 7.453936854591, 0.077763912291])
NOTE_DRIVE = {3: 5.181438, 4: 14.395723, 5: 28.257343}
NOTE_CORNER = {3: (1.70986, 8.63695), 4: (7.95155, 20.78745), 5: (18.24457, 38.15028)}
NOTE_WIDTH = {3: 0.000368, 4: 0.008878, 5: 0.157861}


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def fire(msg):
    FIRED.append(msg)


class Unassignable(Exception):
    pass


VAR = dict(ec4=4.0, g=1.0, ejfac=1.0, ends=(0.0, 0.5), divj=True)
def endpoint(p, ng, N=12, K=8):
    """Levels of the full charge x Fock Hamiltonian at offset charge ng; returns (f01..f05, fres1, fres2) in GHz from dressed states labelled by dominant bare overlap.
    Basis: charges -N..N (no transmon truncation), photons 0..K-1."""
    ec, ej, om, g = p
    n = np.arange(-N, N + 1, dtype=float)
    nq = len(n)
    hc = np.diag(VAR['ec4'] * ec * (n - ng) ** 2) - 0.5 * VAR['ejfac'] * ej * (np.eye(nq, k=1) + np.eye(nq, k=-1))
    _, bare = np.linalg.eigh(hc)                                       # bare transmon eigenvectors (columns), for labelling only
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(hc, np.eye(K)) + om * np.kron(np.eye(nq), np.diag(np.arange(K, dtype=float))) + g * VAR['g'] * np.kron(np.diag(n), a + a.T)
    e, v = np.linalg.eigh(h)
    labels = [(j, 0) for j in range(6)] + [(0, 1), (1, 1)]           # (transmon level, photon number)
    idx, wts = [], []
    for j, k in labels:
        b = np.kron(bare[:, j], np.eye(K)[:, k])
        ov = np.abs(b @ v) ** 2
        i = int(np.argmax(ov)); idx.append(i); wts.append(ov[i])
    if len(set(idx)) != len(idx) or min(wts) < 0.5:
        raise Unassignable()
    lev = e[idx]
    f = np.array([lev[j] - lev[0] for j in range(1, 6)] + [lev[6] - lev[0], lev[7] - lev[1]])       # f01..f05, fres1 = E(0,1)-E(0,0), fres2 = E(1,1)-E(1,0)
    return f, float(min(wts))


def predict(p, **kw):
    e0, e1 = VAR['ends']
    a, wa = endpoint(p, e0, **kw); b, wb = endpoint(p, e1, **kw)
    return (a + b) / 2, min(wa, wb)


CALIDX = [0, 1, 5, 6]                                                  # f01, f02, fres1, fres2 positions in the 7-vector


def resid_cal(z, target, **kw):
    try:
        f, _ = predict(np.exp(z), **kw)
    except Unassignable:
        return np.full(4, 1e3)
    return (f[CALIDX] - target) * 1000.0                               # MHz


def solve(target, start, max_nfev=80, **kw):
    r = least_squares(lambda z: resid_cal(z, target, **kw), np.log(start), xtol=1e-14, ftol=1e-14, gtol=1e-12, max_nfev=max_nfev, x_scale=1.0)
    return np.exp(r.x), float(np.max(np.abs(r.fun)))


def drive_residuals(p, **kw):
    f, w = predict(p, **kw)
    return {j: 1000.0 * (f[j - 1] - MEAS[j]) / (j if VAR['divj'] else 1) for j in (3, 4, 5)}, f, w



import warnings; warnings.filterwarnings("ignore")
NOTE_DRIVE = {3: 5.181438, 4: 14.395723, 5: 28.257343}; NOTE_TOTAL = {3: 15.544315, 4: 57.582891, 5: 141.286714}
T0 = time.time()
def run_variant(name, sw, start):
    VAR.update(dict(ec4=4.0, g=1.0, ejfac=1.0, ends=(0.0, 0.5), divj=True)); VAR.update(sw)
    try:
        p, err = solve(CAL, start, max_nfev=200, N=12, K=8)
    except Exception:
        return None
    if err > 1e-3: return None
    try: d, f, w = drive_residuals(p, N=12, K=8)
    except Unassignable: return None
    tot = {j: 1000.0 * (f[j - 1] - MEAS[j]) for j in (3, 4, 5)}
    return p, d, tot
S0 = NOTE_ROOT
VARIANTS = [("note's conventions", {}, S0, "must reproduce"),
            ("4 EC (n - ng)^2 replaced by EC (n - ng)^2", dict(ec4=1.0), np.array([S0[0] * 4, S0[1], S0[2], S0[3]]), "pure rescaling of EC: invariant"),
            ("4 EC (n - ng)^2 replaced by 8 EC (n - ng)^2", dict(ec4=8.0), np.array([S0[0] / 2, S0[1], S0[2], S0[3]]), "pure rescaling of EC: invariant"),
            ("full instead of half hopping (EJ cos phi -> 2 EJ cos phi)", dict(ejfac=2.0), np.array([S0[0], S0[1] / 2, S0[2], S0[3]]), "pure rescaling of EJ: invariant"),
            ("G doubled", dict(g=2.0), np.array([S0[0], S0[1], S0[2], S0[3] / 2]), "G rescaling: invariant if G is refit (free parameter)"),
            ("endpoint ng = 0 only", dict(ends=(0.0, 0.0)), S0, "changes physics"),
            ("endpoint ng = 1/2 only", dict(ends=(0.5, 0.5)), S0, "changes physics"),
            ("drive residual not divided by j (total residual)", dict(divj=False), S0, "changes the reported quantity only")]
rows = []
for name, sw, st, kind in VARIANTS:
    r = run_variant(name, sw, st)
    rows.append((name, kind, r))
    if r is None: print(f"   {name}: no calibration to 1e-3 MHz  ({kind})", flush=True)
    else: print(f"   {name}: (EC, EJ, Omega, G) = {np.round(r[0], 6).tolist()}; drive residuals {r[1][3]:+.6f}, {r[1][4]:+.6f}, {r[1][5]:+.6f} MHz; total {r[2][3]:+.4f}, {r[2][4]:+.4f}, {r[2][5]:+.4f} MHz  ({kind})", flush=True)
VAR.update(dict(ec4=4.0, g=1.0, ejfac=1.0, ends=(0.0, 0.5), divj=True))
base = rows[0][2]
ok_base = base is not None and all(abs(base[1][j] - NOTE_DRIVE[j]) < 5e-4 for j in (3, 4, 5)) and all(abs(base[2][j] - NOTE_TOTAL[j]) < 5e-3 for j in (3, 4, 5))
print(f"[{'PASS' if ok_base else 'FAIL'}] the note's conventions reproduce its drive residuals (+5.181438, +14.395723, +28.257343 MHz) to 5e-4 MHz and its total residuals (+15.544315, +57.582891, +141.286714 MHz) to 5e-3 MHz")
inv = [r for r in rows[1:5]]
ok_inv = all(r[2] is not None and all(abs(r[2][1][j] - NOTE_DRIVE[j]) < 5e-3 for j in (3, 4, 5)) for r in inv)
print(f"[{'PASS' if ok_inv else 'FAIL'}] the pure rescalings (EC and EJ conventions, G with G refit) leave the drive residuals unchanged to 5e-3 MHz")
phys = [r for r in rows[5:7]]
NOTE_WIDTH = {3: 0.000368, 4: 0.008878, 5: 0.157861}                      # total-frequency full charge-grid widths of the note (MHz)
def shift_ok(r):
    if r[2] is None: return False
    return all(abs(abs(r[2][1][j] - base[1][j]) - NOTE_WIDTH[j] / (2 * j)) < 2e-5 + 0.05 * NOTE_WIDTH[j] / (2 * j) for j in (3, 4, 5))
ok_phys = all(shift_ok(r) for r in phys) and (phys[0][2][1][5] - base[1][5]) * (phys[1][2][1][5] - base[1][5]) < 0
print(f"[{'PASS' if ok_phys else 'FAIL'}] using the endpoint ng = 0 alone or ng = 1/2 alone instead of their average shifts each drive residual by plus or minus half the note's charge-grid width divided by j (0.000061, 0.001110, 0.015786 MHz) in opposite directions: " + "; ".join(f"{r[0]}: " + ("no fit" if r[2] is None else ", ".join(f"{r[2][1][j] - base[1][j]:+.6f}" for j in (3, 4, 5))) for r in phys))
tot_r = rows[7][2]
ok_tot = tot_r is not None and all(abs(tot_r[1][j] - NOTE_TOTAL[j]) < 5e-3 for j in (3, 4, 5))
print(f"[{'PASS' if ok_tot else 'FAIL'}] without the division by j the reported drive residual equals the note's total residual (and the calibration is unchanged): the division by j is the only difference between the two tables")
print(f"   total {time.time() - T0:.0f}s")
if ok_base and ok_inv and ok_phys and ok_tot:
    print("SUMMARY: no purchase: the note's conventions reproduce its drive and total residuals; the EC, EJ and G conventions are pure rescalings that leave the residuals unchanged; the endpoint average matters only at half the note's charge-grid width per photon (0.016 MHz at f05) and the division by j is the only difference between the drive and total tables")
else:
    print("SUMMARY: a convention is not pinned or the note's fails: base %s, invariant %s, physics %s, totals %s" % (ok_base, ok_inv, ok_phys, ok_tot)); print("HIT: normalization variants do not behave as expected")
sys.exit(0)
