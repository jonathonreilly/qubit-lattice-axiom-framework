#!/usr/bin/env python3
"""J:falsifier:PR9348 -- calibrated transmon holdout: is the found calibration root the only one, and do the residuals survive independent code?

Target claims (PR #9348, note TRANSMON_CALIBRATION_HOLDOUT_BOUNDED_THEOREM_NOTE_2026-09-26): with H/h = 4 EC (n - ng)^2 - EJ cos(phi) + Omega a^dag a + G n (a + a^dag),
the ng = 0 / 1/2 endpoint mean, and the four calibration coordinates f01 = 6.0391, f02 = 11.8680, fres1 = 7.4613, fres2 = 7.4587 GHz, the calibration root is
EC = 0.196567178810, EJ = 24.852181043101, Omega = 7.453936854591, G = 0.077763912291 GHz, and the unused lines f03, f04, f05 (measured 17.457, 22.778, 27.794 GHz) have
drive residuals +5.181438, +14.395723, +28.257343 MHz; over sixteen calibration corners [1,2,1,1] MHz the drive residuals lie in +1.70986..+8.63695, +7.95155..+20.78745,
+18.24457..+38.15028 MHz; the charge grid widths are 0.000368, 0.008878, 0.157861 MHz; the calibration Jacobian condition number is about 7826.
The note states the root is a found root, not a proved unique one ("alternate roots remain unexhausted"). This script (1) builds the model itself in the full charge x Fock basis
(no transmon-subspace truncation; bare transmon eigenvectors only to label dressed states), (2) searches for calibration roots from random starts over a wide box (EC 0.02-3,
EJ 0.5-300, Omega 2-14, G 0.001-1.5 GHz, wider than the runner's fit box), (3) verifies every root found in a larger basis, (4) recomputes the residuals, the sixteen corner
refits, the charge-grid widths and the Jacobian condition, and (5) checks the operator identity H_square + 4 delta = 4 K n^2 - 4 delta cos(phi) as matrices (EC = K, EJ = 4 delta).
It does not read the PR's runner or helpers; only the four calibration numbers and three measured numbers quoted in the note are inputs. Floating point throughout.
Prints SUMMARY: and, only if a falsifier fires, HIT:.
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


def endpoint(p, ng, N=12, K=8):
    """Levels of the full charge x Fock Hamiltonian at offset charge ng; returns (f01..f05, fres1, fres2) in GHz from dressed states labelled by dominant bare overlap.
    Basis: charges -N..N (no transmon truncation), photons 0..K-1."""
    ec, ej, om, g = p
    n = np.arange(-N, N + 1, dtype=float)
    nq = len(n)
    hc = np.diag(4 * ec * (n - ng) ** 2) - 0.5 * ej * (np.eye(nq, k=1) + np.eye(nq, k=-1))
    _, bare = np.linalg.eigh(hc)                                       # bare transmon eigenvectors (columns), for labelling only
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    h = np.kron(hc, np.eye(K)) + om * np.kron(np.eye(nq), np.diag(np.arange(K, dtype=float))) + g * np.kron(np.diag(n), a + a.T)
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
    a, wa = endpoint(p, 0.0, **kw); b, wb = endpoint(p, 0.5, **kw)
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
    return {j: 1000.0 * (f[j - 1] - MEAS[j]) / j for j in (3, 4, 5)}, f, w


def run():
    # ---- 1. the note's root and residuals from the independently built model
    dres, f, w = drive_residuals(NOTE_ROOT)
    cal_err = float(np.max(np.abs((f[CALIDX] - CAL) * 1000.0)))
    check("(R1) with the note's four parameters, the independently built full charge x Fock model reproduces the four calibration coordinates to 1e-3 MHz and the three drive residuals to 1e-3 MHz",
          cal_err < 1e-3 and all(abs(dres[j] - NOTE_DRIVE[j]) < 1e-3 for j in (3, 4, 5)),
          f"calibration error {cal_err:.1e} MHz; drive residuals {dres[3]:+.6f}, {dres[4]:+.6f}, {dres[5]:+.6f} MHz (note +5.181438, +14.395723, +28.257343); min assignment weight {w:.3f}; {time.time() - T0:.0f} s")
    if not (cal_err < 1e-3 and all(abs(dres[j] - NOTE_DRIVE[j]) < 1e-3 for j in (3, 4, 5))):
        fire("independent model does not reproduce the note's calibration/residuals")
    dbig, fbig, wbig = drive_residuals(NOTE_ROOT, N=40, K=20)
    okb = all(abs(dbig[j] - NOTE_DRIVE[j]) < 1e-3 for j in (3, 4, 5)) and float(np.max(np.abs((fbig[CALIDX] - CAL) * 1000.0))) < 1e-3
    check("(R1b) beyond the note's basis (81 charges x 20 photons, 1620 dimensions, no transmon-subspace truncation) the same three drive residuals and the calibration coordinates hold to 1e-3 MHz", okb,
          f"drive residuals {dbig[3]:+.6f}, {dbig[4]:+.6f}, {dbig[5]:+.6f} MHz; min assignment weight {wbig:.3f}; {time.time() - T0:.0f} s")
    if not okb:
        fire("residuals change beyond the note's basis")
    # ---- 2. root search over a wide box
    rng = np.random.default_rng(20260929)
    lo, hi = np.log([0.02, 0.5, 2.0, 0.001]), np.log([3.0, 300.0, 14.0, 1.5])
    nstart = 24 if DRY else 1500
    roots, failed = [], 0
    for s in range(nstart):
        z0 = rng.uniform(lo, hi)
        try:
            p, err = solve(CAL, np.exp(z0), max_nfev=60, N=10, K=6)
        except Exception:
            failed += 1
            continue
        if err < 1e-3:
            roots.append(p)
    uniq = []
    for p in roots:
        if all(np.max(np.abs(np.log(p / q))) > 1e-4 for q in uniq):
            uniq.append(p)
    print(f"   {nstart} random starts over the wide box: {len(roots)} converged to a calibration root (max error < 1e-3 MHz in the search basis), {failed} failed, {len(uniq)} distinct", flush=True)
    # refine and verify each distinct root in the large basis
    info = []
    for p in uniq:
        try:
            pv, ev = solve(CAL, p, max_nfev=40, N=24, K=12)
            d, ff, ww = drive_residuals(pv, N=24, K=12)
        except Exception as ex:
            info.append((p, None, None, repr(ex))); continue
        info.append((pv, ev, d, ww))
    for pv, ev, d, ww in info:
        if d is None:
            print(f"   root (search basis) {np.round(pv, 6)}: verification failed ({ww})"); continue
        print(f"   root EC {pv[0]:.9f} EJ {pv[1]:.9f} Omega {pv[2]:.9f} G {pv[3]:.9f}: calibration error {ev:.1e} MHz, drive residuals {d[3]:+.5f}, {d[4]:+.5f}, {d[5]:+.5f} MHz, min assignment weight {ww:.3f}")
    good = [(pv, d) for pv, ev, d, ww in info if d is not None and ev < 1e-3]
    is_note = [np.max(np.abs(np.log(pv / NOTE_ROOT))) < 1e-6 for pv, _ in good]
    others = [(pv, d) for (pv, d), yes in zip(good, is_note) if not yes]
    check("(R2) the note's root is found by the search and reproduced to 1e-6 relative (larger basis: 49 charges x 12 photons)", any(is_note), f"{sum(is_note)} of {len(good)} verified roots coincide with the note's; {time.time() - T0:.0f} s")
    if not any(is_note):
        fire("the note's calibration root is not reproduced")
    small = [(pv, d) for pv, d in others if max(abs(d[j]) for j in (3, 4, 5)) < 2.0]
    check(f"(R3) no other calibration root predicts f03, f04, f05 to within 2 MHz drive (the paper's stated accuracy is about 1 MHz): {len(others)} other root(s) found in {nstart} starts over the wide box", not small,
          "; ".join(f"EC {pv[0]:.4f}, EJ {pv[1]:.3f}, Omega {pv[2]:.4f}, G {pv[3]:.4f} (EJ/EC {pv[1] / pv[0]:.1f}) -> drive residuals " + ", ".join(f"{d[j]:+.3f}" for j in (3, 4, 5)) for pv, d in others) or "no other root found")
    if small:
        fire("alternate calibration root(s) that fit f03-f05 within 2 MHz: " + "; ".join(f"({pv[0]:.4f}, {pv[1]:.3f}, {pv[2]:.4f}, {pv[3]:.4f}) -> " + ", ".join(f"{d[j]:+.3f}" for j in (3, 4, 5)) for pv, d in small))
    # ---- 3. the sixteen corners
    halfwidth = np.array([1, 2, 1, 1]) / 1000.0
    rows = []
    for signs in itertools.product((-1, 1), repeat=4):
        pv, ev = solve(CAL + halfwidth * np.array(signs), NOTE_ROOT, max_nfev=60, N=16, K=8)
        d, _, _ = drive_residuals(pv, N=16, K=8)
        rows.append((ev, d))
    lo_r = {j: min(d[j] for _, d in rows) for j in (3, 4, 5)}
    hi_r = {j: max(d[j] for _, d in rows) for j in (3, 4, 5)}
    okc = all(ev < 1e-3 for ev, _ in rows) and all(abs(lo_r[j] - NOTE_CORNER[j][0]) < 5e-4 and abs(hi_r[j] - NOTE_CORNER[j][1]) < 5e-4 for j in (3, 4, 5))
    check("(R4) the sixteen calibration corners [1,2,1,1] MHz refit from the note's root give the drive-residual ranges of the note to 5e-4 MHz", okc,
          "; ".join(f"f0{j}: {lo_r[j]:+.5f}..{hi_r[j]:+.5f} (note {NOTE_CORNER[j][0]:+.5f}..{NOTE_CORNER[j][1]:+.5f})" for j in (3, 4, 5)) + f"; {time.time() - T0:.0f} s")
    if not okc:
        fire("corner ranges differ from the note")
    # ---- 4. charge grid and Jacobian
    grid = np.array([endpoint(NOTE_ROOT, float(x), N=16, K=8)[0] for x in np.linspace(0, 0.5, 21)])
    wid = 1000.0 * np.ptp(grid, axis=0)
    okw = all(abs(wid[j - 1] - NOTE_WIDTH[j]) < 5e-5 + 0.02 * NOTE_WIDTH[j] for j in (3, 4, 5))
    check("(R5) the 21-point offset-charge grid at the note's root has total-frequency widths 0.000368, 0.008878, 0.157861 MHz (f03, f04, f05) to 2%", okw,
          f"{wid[2]:.6f}, {wid[3]:.6f}, {wid[4]:.6f} MHz")
    if not okw:
        fire("charge-grid widths differ from the note")
    step = 1e-5
    J = np.column_stack([(predict(NOTE_ROOT + np.eye(4)[i] * step, N=16, K=8)[0][CALIDX] - predict(NOTE_ROOT - np.eye(4)[i] * step, N=16, K=8)[0][CALIDX]) / (2 * step) for i in range(4)])
    cnd = float(np.linalg.cond(J))
    check("(R6) the calibration Jacobian (GHz per GHz, four coordinates against four parameters) has condition number 7826 to 2% (the note: about 7826)", abs(cnd - 7826) / 7826 < 0.02, f"{cnd:.0f}")
    if abs(cnd - 7826) / 7826 >= 0.02:
        fire("Jacobian condition number differs from the note")
    # ---- 5. the operator identity as matrices
    Nn = 30
    n = np.arange(-Nn, Nn + 1, dtype=float)
    K_, delta = 0.196567178810, 24.852181043101 / 4
    U = np.eye(len(n), k=-1)                                           # U|n> = |n + 1>
    Hsq = 4 * K_ * np.diag(n ** 2) - 2 * delta * (U + U.T) - 4 * delta * np.eye(len(n))
    Htm = 4 * K_ * np.diag(n ** 2) - 0.5 * (4 * delta) * (np.eye(len(n), k=1) + np.eye(len(n), k=-1))
    SS = 2 * np.eye(len(n)) + U + U.T
    d1 = float(np.abs(np.linalg.eigvalsh(Hsq) + 0 - (np.linalg.eigvalsh(Htm) - 4 * delta)).max())
    d2 = float(np.abs(Hsq - (4 * K_ * np.diag(n ** 2) - 2 * delta * SS)).max())
    check("(O) as matrices on the charge basis: H_square = 4 K n^2 - 2 delta (U + U^dag) - 4 delta I has the spectrum of 4 EC n^2 - EJ cos(phi) - 4 delta with EC = K, EJ = 4 delta, and equals 4 K n^2 - 2 delta S^dag S",
          d1 < 1e-9 and d2 < 1e-12, f"spectrum difference {d1:.1e}; S^dag S form {d2:.1e} (matrix identities, truncated charge basis)")
    if not (d1 < 1e-9 and d2 < 1e-12):
        fire("operator identity fails as a matrix identity")
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: PR #9348 claim is root-dependent or fails: " + "; ".join(FIRED))
        sys.exit(1)
    print(f"SUMMARY: no falsifier fired: the independently built full charge x Fock model reproduces the note's root, the three drive residuals, the sixteen corner ranges, the charge-grid widths and the Jacobian condition; "
          f"{nstart} random starts over EC 0.02-3, EJ 0.5-300, Omega 2-14, G 0.001-1.5 GHz found {len(uniq)} distinct calibration root(s): the note's and {len(others)} other(s), "
          + ("none of which predicts f03-f05 within 2 MHz" if others else "so the found root is the only one located"))


if __name__ == "__main__":
    run()
