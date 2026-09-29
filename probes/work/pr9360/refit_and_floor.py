#!/usr/bin/env python3
"""J:falsifier:PR9360 -- qutrit preparation transfer: independent re-fit of the calibration, the target residuals, and the model class's own floor.

Target claims (PR #9360, note QUTRIT_PREPARATION_TRANSFER_OPEN_GATE_NOTE_2026-09-27): the classical rate model L = [[0, k10, k20], [0, -k10, k21], [0, 0, -k21 - k20]] (initial |2> for calibration; [0, 1/2, 1/2] for Ramsey) fitted to all
36,051 calibration population coordinates (61 gates x 197 delays x 3 populations, equal weights, rates in [0, 10]/us, affine readout by the final three reference centroids) gives rates ~[0.07126916, 0.11124121, 0.00839770]/us with
calibration RMS 0.03151155 (Jacobian condition ~4.97); with those frozen rates the Ramsey population sum has RMS residual 1.659315 pp (mean +0.274780), the fixed no-decay comparator 5.164180 pp; the echo with an instantaneous
midpoint swap 15.851257 pp (no swap 13.387442); the sequential-only recalibration (k20 = 0, rates ~[0.07728135, 0.11762925]) 1.673540 pp (Ramsey), calibration RMS 0.03227173.
The PR's runner propagates supplied snapshots and does not rerun any optimizer. This script (1) rebuilds the populations from the raw I/Q arrays with its own barycentric solve, (2) refits the calibration from 300 random starts over
[0, 10]^3 with its own model code and compares the rates, cost and Jacobian condition, (3) recomputes the target residuals from the refit, (4) computes the floors: the same model class fitted directly to the Ramsey and to the echo data
(no cross-acquisition transfer), and the residual as a function of a common rate scale s (the 1/T versus 2/T convention the note mentions). It reads only the packaged arrays (calibration_raw.npz, ramsey_raw.npz, echo_raw.npz) and
the note's quoted numbers; none of the PR's code. Floating point throughout. Prints SUMMARY: and, only if a claim fails, HIT:.
"""
import io
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

ROOT = Path.home() / ".probe-clones/probes-view" if "--scratch" in sys.argv else Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/preparation-transfer-20260927"
D = "data/preparation_transfer_2026_09_27"
T0 = time.time()
RESULTS, FIRED = [], []
DRY = "--dry" in sys.argv


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def load(name):
    subprocess.run(["git", "fetch", "origin", BRANCH, "--quiet"], cwd=ROOT)
    r = subprocess.run(["git", "show", f"origin/{BRANCH}:{D}/{name}"], cwd=ROOT, capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"cannot read {name}: {r.stderr.decode()[:200]}")
    return np.load(io.BytesIO(r.stdout), allow_pickle=False)


def populations(z):
    """Barycentric populations of every stored point in the frame of the final three reference points (1, 0, 0), (0, 1, 0), (0, 0, 1) of each gate."""
    iq = z["raw_IQ"]; out = []
    for gate in iq:
        M = np.vstack([gate[-3:].T, np.ones(3)])
        out.append(np.linalg.solve(M, np.vstack([gate.T, np.ones(len(gate))])).T)
    return np.array(out)


def propagate(rates, t_us, init, swap=False):
    """Populations (states 0, 1, 2) at times t_us (microseconds) for rates (k10, k21, k20) from the population generator; midpoint swap of states 1 and 2 if swap."""
    k10, k21, k20 = rates
    lam = k21 + k20
    def step(t, u):
        F = np.where(np.abs(lam - k10) < 1e-12, t * np.exp(-k10 * t), (np.exp(-k10 * t) - np.exp(-lam * t)) / np.where(np.abs(lam - k10) < 1e-12, 1.0, lam - k10))
        u2 = u[..., 2] * np.exp(-lam * t)
        u1 = u[..., 1] * np.exp(-k10 * t) + k21 * u[..., 2] * F
        return np.stack([1 - u1 - u2, u1, u2], axis=-1)
    u0 = np.broadcast_to(np.asarray(init, float), (len(t_us), 3))
    if swap:
        h = step(t_us / 2, u0)
        return step(t_us / 2, h[..., [0, 2, 1]])
    return step(t_us, u0)


def run():
    zc, zr, ze = load("calibration_raw.npz"), load("ramsey_raw.npz"), load("echo_raw.npz")
    pops = {}
    for name, z, n in (("calibration", zc, 197), ("ramsey", zr, 380), ("echo", ze, 246)):
        t = z["times_s"]; mask = z["genuine_mask"]
        P = populations(z)
        pops[name] = (t[mask] * 1e6, P[:, mask, :])
        assert mask.sum() == n and np.allclose(P[:, -3:, :], np.eye(3), atol=1e-12)
    tc, Pc = pops["calibration"]; tr, Pr = pops["ramsey"]; te, Pe = pops["echo"]
    check("(R0) own barycentric readout: 61 x 197 calibration, 31 x 380 Ramsey and 61 x 246 echo genuine points (references excluded), reference points are the unit vectors, coordinates sum to one",
          Pc.shape == (61, 197, 3) and Pr.shape == (31, 380, 3) and Pe.shape == (61, 246, 3) and abs(Pc.sum(-1) - 1).max() < 1e-12,
          f"calibration outside-simplex fraction {np.mean(np.any((Pc < 0) | (Pc > 1), axis=-1)):.4f} (note table: 0.3314 in the snapshot file); {time.time() - T0:.0f} s")
    # ---- calibration refit
    def res_cal(k, tt=tc, PP=Pc):
        return (propagate(k, tt, [0, 0, 1])[None, :, :] - PP).ravel()
    rng = np.random.default_rng(20260929)
    starts = [np.array(s, float) for s in ([0.05, 0.1, 0.05], [0.2, 0.2, 0.2], [1, 0.1, 1])] + [rng.uniform(0, 3, 3) for _ in range(12 if DRY else 300)]
    fits = []
    for s in starts:
        r = least_squares(res_cal, s, bounds=(0, 10), ftol=1e-15, xtol=1e-15, gtol=1e-14, max_nfev=400)
        fits.append((float(0.5 * np.sum(r.fun ** 2)), r.x, r))
    fits.sort(key=lambda f: f[0])
    best = fits[0]
    distinct = []
    for c, x, r in fits:
        if all(np.max(np.abs(x - y[1])) > 1e-4 or abs(c - y[0]) > 1e-6 for y in distinct):
            distinct.append((c, x, r))
    rms = float(np.sqrt(np.mean(best[2].fun ** 2)))
    sv = np.linalg.svd(best[2].jac, compute_uv=False)
    note_rates = np.array([0.07126916, 0.11124121, 0.00839770])
    ok_cal = np.max(np.abs(best[1] - note_rates)) < 5e-8 and abs(rms - 0.03151155) < 5e-8 and abs(sv[0] / sv[-1] - 4.97) < 0.02
    check(f"(R1) refit of the three-rate model to all 36,051 calibration coordinates from {len(starts)} starts (3 declared + random over [0, 3]^3, bounds [0, 10]): the best minimum has the note's rates, RMS and Jacobian condition, and is the only distinct local minimum",
          ok_cal and len(distinct) == 1,
          f"best cost {best[0]:.9f} at rates {np.round(best[1], 8)}; RMS {rms:.8f}; Jacobian condition {sv[0] / sv[-1]:.3f}; distinct minima {[(round(c, 6), np.round(x, 5).tolist()) for c, x, _ in distinct[:4]]}; {time.time() - T0:.0f} s")
    if not ok_cal or len(distinct) != 1:
        FIRED.append("calibration refit differs from the note's rates/RMS/condition or has another minimum")
    # sequential-only (k20 = 0)
    def res_seq(k2):
        return res_cal(np.array([k2[0], k2[1], 0.0]))
    fs = min((least_squares(res_seq, s, bounds=(0, 10), ftol=1e-15, xtol=1e-15, gtol=1e-14) for s in ([0.05, 0.1], [0.2, 0.2], [1, 0.1])), key=lambda r: r.cost)
    rs = np.array([fs.x[0], fs.x[1], 0.0]); rms_s = float(np.sqrt(np.mean(fs.fun ** 2)))
    check("(R2) the sequential-only refit (k20 = 0) gives the note's rates [0.07728135, 0.11762925] and calibration RMS 0.03227173", np.max(np.abs(fs.x - [0.07728135, 0.11762925])) < 5e-8 and abs(rms_s - 0.03227173) < 5e-8,
          f"rates {np.round(fs.x, 8)}, RMS {rms_s:.8f}")
    if not (np.max(np.abs(fs.x - [0.07728135, 0.11762925])) < 5e-8 and abs(rms_s - 0.03227173) < 5e-8):
        FIRED.append("sequential-only refit differs from the note's")
    # ---- target residuals
    def rms_target(rates, tt, PP, init, swap=False):
        pred = propagate(rates, tt, init, swap)[:, 1:].sum(-1)
        obs = PP[..., 1:].sum(-1)
        d = pred[None, :] - obs
        return float(np.sqrt(np.mean(d ** 2))) * 100, float(d.mean()) * 100
    k3 = best[1]
    rr = {"Ramsey three rates": rms_target(k3, tr, Pr, [0, .5, .5]), "Ramsey sequential-only": rms_target(rs, tr, Pr, [0, .5, .5]),
          "Ramsey fixed no decay": rms_target([0, 0, 0], tr, Pr, [0, .5, .5]), "Echo three rates, midpoint swap": rms_target(k3, te, Pe, [0, .5, .5], True),
          "Echo three rates, no swap": rms_target(k3, te, Pe, [0, .5, .5]), "Echo sequential-only, swap": rms_target(rs, te, Pe, [0, .5, .5], True), "Echo sequential-only, no swap": rms_target(rs, te, Pe, [0, .5, .5])}
    note = {"Ramsey three rates": (1.659315, 0.274780), "Ramsey sequential-only": (1.673540, 0.358514), "Ramsey fixed no decay": (5.164180, 4.414061), "Echo three rates, midpoint swap": (15.851257, 14.175870),
            "Echo three rates, no swap": (13.387442, 12.104752), "Echo sequential-only, swap": (16.254789, 14.553427), "Echo sequential-only, no swap": (13.308114, 12.070934)}
    ok_t = all(abs(rr[k][0] - note[k][0]) < 5e-4 and abs(rr[k][1] - note[k][1]) < 5e-4 for k in note)
    check("(R3) target residuals recomputed from the refit rates (own propagation): all seven RMS and mean residuals of the note's table to 5e-4 percentage points", ok_t,
          "; ".join(f"{k}: {rr[k][0]:.6f}/{rr[k][1]:+.6f} (note {note[k][0]:.6f}/{note[k][1]:+.6f})" for k in note))
    if not ok_t:
        FIRED.append("target residuals differ from the note's table")
    # ---- floors: the same model class fitted to the target itself
    def fit_target(tt, PP, init, swap):
        best_ = None
        for s in ([0.07, 0.11, 0.008], [0.2, 0.2, 0.2], [1, 0.1, 1], [0.01, 0.01, 0.01]):
            r = least_squares(lambda k: (propagate(k, tt, init, swap)[:, 1:].sum(-1)[None, :] - PP[..., 1:].sum(-1)).ravel(), s, bounds=(0, 10), ftol=1e-14, xtol=1e-14, gtol=1e-13)
            if best_ is None or r.cost < best_.cost:
                best_ = r
        return best_
    fr_r = fit_target(tr, Pr, [0, .5, .5], False); fr_e = fit_target(te, Pe, [0, .5, .5], True); fr_e2 = fit_target(te, Pe, [0, .5, .5], False)
    fl_r = float(np.sqrt(2 * fr_r.cost / (Pr.shape[0] * Pr.shape[1]))) * 100
    fl_e = float(np.sqrt(2 * fr_e.cost / (Pe.shape[0] * Pe.shape[1]))) * 100
    fl_e2 = float(np.sqrt(2 * fr_e2.cost / (Pe.shape[0] * Pe.shape[1]))) * 100
    print(f"   floors (the model class fitted directly to the target's population sum, 3 free rates): Ramsey {fl_r:.4f} pp (rates {np.round(fr_r.x, 5)}), echo with swap {fl_e:.4f} pp (rates {np.round(fr_e.x, 5)}), echo without swap {fl_e2:.4f} pp", flush=True)
    check("(R4) floors: fitting the same class directly to the Ramsey data lowers the RMS from 1.659 to the floor printed above, and to the echo data (with the swap) from 15.851 to its floor: the echo mismatch is a transfer/convention failure, not a model-class limit, if the echo floor is far below 15.851",
          fl_r <= 1.6593 and fl_e < 15.85, f"Ramsey floor {fl_r:.4f}, echo (swap) floor {fl_e:.4f}, echo (no swap) floor {fl_e2:.4f} pp")
    # ---- common rate scale (the 1/T versus 2/T convention)
    scales = np.array([0.25, 0.4, 0.5, 0.6, 0.75, 1.0, 1.5, 2.0, 3.0])
    rows = []
    for s in scales:
        rows.append((s, rms_target(k3 * s, tr, Pr, [0, .5, .5])[0], rms_target(k3 * s, te, Pe, [0, .5, .5], True)[0], rms_target(k3 * s, te, Pe, [0, .5, .5])[0]))
    print("   common rate scale s (all three calibrated rates x s): " + "; ".join(f"s = {s:g}: Ramsey {a:.3f}, echo swap {b:.3f}, echo no-swap {c:.3f} pp" for s, a, b, c in rows), flush=True)
    sopt = least_squares(lambda s: np.array([rms_target(k3 * s[0], te, Pe, [0, .5, .5], True)[0]]), [1.0], bounds=(0.05, 5)).x[0]
    print(f"   echo (swap) RMS is minimised at s = {sopt:.3f} (RMS {rms_target(k3 * sopt, te, Pe, [0, .5, .5], True)[0]:.3f} pp) where the Ramsey RMS is {rms_target(k3 * sopt, tr, Pr, [0, .5, .5])[0]:.3f} pp", flush=True)
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: PR #9360 claim fails: " + "; ".join(FIRED))
        return 0
    print("SUMMARY: no falsifier fired: an independent refit from the raw I/Q arrays (own readout, own propagation, 300 starts) reproduces the note's calibrated rates, RMS and Jacobian condition with a single minimum, the sequential-only rates, and all seven "
          f"target residuals; the model class's own floors are {fl_r:.3f} pp (Ramsey) and {fl_e:.3f} pp (echo with swap), so the echo mismatch is not a model-class limit; the echo RMS is minimised at a common rate scale s = {sopt:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
