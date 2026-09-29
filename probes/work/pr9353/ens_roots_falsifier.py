#!/usr/bin/env python3
"""J:falsifier:PR9353 -- ENS cavity holdout: independent recomputation of the calibration, the unused drive errors, the exact offset-convention identity, the parity maxima, and a scan for other calibration roots.

Target claims (PR #9353, note ENS_CAVITY_CALIBRATED_HOLDOUT_OPEN_GATE_NOTE_2026-09-27): with H/h = 4 EC (n - ng)^2 + V_tau(phi) + Omega a^dag a + G n (a + a^dag), V_tau = EJ1 w_tau/(-2 c_1), w_tau = 4 s/(1 + sqrt(1 - tau s)),
s = sin^2(phi/2), the ng = 0 / 1/2 endpoint mean, five calibration inputs f01 = 5.354767, f02 = 10.5356, fres1 = 7.76131, fres2 = 7.75608, fres3 = 7.75135 GHz, the calibrated point
EC = .1841990760792327, EJ1 = 21.829772186093592, Omega = 7.738912856323958, G = .18858878602560333, tau = .15464897201354028 gives drive errors (prediction - measurement) f03/3 .. f06/6 = -.218231, -.389980, -.951250, -2.323107 MHz
(cosine baseline, four inputs: +.796329, +2.898695, +6.238759, +11.008222), potential ratios +.0104917249 cos(2 phi), -.00022017684 cos(3 phi) in units of EJ1, cavity errors fres4..7 = -.019387, +.033543, -.546382, -.789351 MHz;
the exact identity H_phys(q) = 4EC(n-q)^2 + V + Omega a^dag a + G (n-q)(a + a^dag) has the gap spectrum of the old model at ng = (1 - delta) q, delta = G^2/(4 EC Omega); the parity-splitting maxima are .544477 (cosine) and 3.464585 MHz (Andreev);
"global uniqueness is not proved" (two of three starts hit their evaluation limits).
This script builds the model itself (own Fourier coefficients, own charge x Fock construction, own dressed-state labelling), refits the calibration, reproduces the numbers above, verifies the identity and the parity maxima with a
direct construction of H_phys(q) (no displacement), and scans the calibration for other roots by profiling tau: for each tau in a grid the other four parameters are refit to the five inputs, and the cost curve's zeros are the roots.
Floating point throughout. It reads none of the PR's runner or helpers; only numbers quoted in the note and the pinned CSV row of the note's own table are inputs. Prints SUMMARY: and, only if a claim fails, HIT:.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys
import time

import numpy as np
from scipy.optimize import least_squares

T0 = time.time()
RESULTS, FIRED = [], []
DRY = "--dry" in sys.argv

CAL = np.array([5.354767, 10.5356, 7.76131, 7.75608, 7.75135])            # f01, f02, fres1, fres2, fres3
MEAS_F = {3: 15.5289, 4: 20.3168, 5: 24.879, 6: 29.1888}                    # f03..f06 (GHz), the ENS row of the note's source table
MEAS_R = {4: 7.747, 5: 7.74276, 6: 7.73902, 7: 7.73385}                     # fres4..fres7
NOTE_P = np.array([0.1841990760792327, 21.829772186093592, 7.738912856323958, 0.18858878602560333, 0.15464897201354028])
NOTE_ANDREEV = {3: -0.218231, 4: -0.389980, 5: -0.951250, 6: -2.323107}
NOTE_COSINE = {3: +0.796329, 4: +2.898695, 5: +6.238759, 6: +11.008222}
NOTE_FRES = {4: -0.019387, 5: +0.033543, 6: -0.546382, 7: -0.789351}


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""), flush=True)


def fire(msg):
    FIRED.append(msg)


class Unassignable(Exception):
    pass


def coeffs(tau, grid=1 << 14):
    """Fourier coefficients c_m (m = 0..) of w_tau(phi) = 4 s/(1 + sqrt(1 - tau s)), s = sin^2(phi/2), normalised by -2 c_1 (so the cos(phi) coefficient of V/EJ1 is -1)."""
    phi = 2 * np.pi * np.arange(grid) / grid
    s = np.sin(phi / 2) ** 2
    w = 4 * s / (1 + np.sqrt(1 - tau * s))
    c = np.fft.rfft(w).real / grid
    return c[:80] / (-2 * c[1])


def h_charge(p, ng, N):
    ec, ej, om, g, tau = p
    n = np.arange(-N, N + 1, dtype=float)
    cm = coeffs(tau)
    idx = np.abs(np.subtract.outer(np.arange(2 * N + 1), np.arange(2 * N + 1)))
    return n, ej * cm[idx] + np.diag(4 * ec * (n - ng) ** 2)


def levels(p, ng, N=16, M=14, K=9, full=False):
    """Transitions f01..f06 (photon-0 dressed gaps) and fres1..fres7 (photon 0 -> 1 at fixed bare transmon level) from dressed states labelled by the dominant bare-product overlap.
    full = True keeps every charge state (no transmon-subspace truncation)."""
    ec, ej, om, g, tau = p
    n, h0 = h_charge(p, ng, N)
    e0, v0 = np.linalg.eigh(h0)
    a = np.diag(np.sqrt(np.arange(1, K)), 1)
    if full:
        h = np.kron(h0, np.eye(K)) + om * np.kron(np.eye(len(n)), np.diag(np.arange(K, dtype=float))) + g * np.kron(np.diag(n), a + a.T)
        w, V = np.linalg.eigh(h)
        bare = lambda j, k: np.kron(v0[:, j], np.eye(K)[:, k])
        proj = lambda j, k: np.abs(bare(j, k) @ V) ** 2
    else:
        e = e0[:M] - e0[0]; v = v0[:, :M]
        charge = v.T @ (n[:, None] * v)
        h = np.diag((om * np.arange(K)[:, None] + e[None, :]).ravel()) + g * np.kron(a + a.T, charge)
        w, V = np.linalg.eigh(h)
        proj = lambda j, k: np.abs(V[k * M + j, :]) ** 2
    targets = [(j, 0) for j in range(7)] + [(j, 1) for j in range(7)]
    ix, wt = [], []
    for j, k in targets:
        pr = proj(j, k); i = int(np.argmax(pr)); ix.append(i); wt.append(pr[i])
    if len(set(ix)) != len(ix) or min(wt) < 0.5:
        raise Unassignable()
    lev = {t: w[i] for t, i in zip(targets, ix)}
    f = [lev[j, 0] - lev[0, 0] for j in range(1, 7)] + [lev[j, 1] - lev[j, 0] for j in range(7)]
    return np.array(f), float(min(wt))


def predict(p, **kw):
    a, wa = levels(p, 0.0, **kw); b, wb = levels(p, 0.5, **kw)
    return (a + b) / 2, min(wa, wb)


CALIDX = [0, 1, 6, 7, 8]


def drive_errors(f):
    return {j: 1000 * (f[j - 1] - MEAS_F[j]) / j for j in (3, 4, 5, 6)}, {j: 1000 * (f[6 + j - 1] - MEAS_R[j]) for j in (4, 5, 6, 7)}


DIV = np.array([1, 2, 1, 1, 1.0])


def fit(target, start, ncal=5, cosine=False, bounds=None, max_nfev=200, **kw):
    n = 4 if cosine else 5

    def res(z):
        pp = np.r_[z, 0.0] if cosine else z
        try:
            f, _ = predict(pp, **kw)
        except Unassignable:
            return np.full(ncal, 10.0)
        return (f[CALIDX[:ncal]] - target[:ncal]) / DIV[:ncal]
    lo, hi = np.array([0.03, 1, 7, 0.001, 0.0])[:n], np.array([1, 100, 8.5, 1, 0.99])[:n]
    r = least_squares(res, np.asarray(start, float)[:n], bounds=(lo, hi), x_scale=np.array([0.2, 20, 8, 0.1, 0.2])[:n], ftol=1e-13, xtol=1e-13, gtol=1e-13, max_nfev=max_nfev)
    p = np.r_[r.x, 0.0] if cosine else r.x
    return p, float(np.max(np.abs(res(r.x)))), r


def run():
    # ---- E1: the note's calibrated point and the numbers derived from it
    f, w = predict(NOTE_P)
    cal_err = float(np.max(np.abs((f[CALIDX] - CAL) * 1e6)))            # kHz
    dr, fr = drive_errors(f)
    ok1 = cal_err < 1e-3 and all(abs(dr[j] - NOTE_ANDREEV[j]) < 2e-4 for j in dr) and all(abs(fr[j] - NOTE_FRES[j]) < 2e-3 for j in fr)
    check("(E1) at the note's five parameters the independently built model reproduces the five calibration inputs (to 1e-3 kHz), the four unused drive errors (to 0.2 kHz) and the four unused cavity errors (to 2 kHz)", ok1,
          f"calibration error {cal_err:.1e} kHz; drive errors " + ", ".join(f"{dr[j]:+.6f}" for j in dr) + "; fres4..7 errors " + ", ".join(f"{fr[j]:+.6f}" for j in fr) + f" MHz; min assignment weight {w:.3f}; {time.time() - T0:.0f} s")
    if not ok1:
        fire("the note's calibrated point does not reproduce its printed errors")
    # cosine baseline refit (four inputs)
    pc, ec_err, _ = fit(CAL, [0.18, 20, 7.75, 0.1], ncal=4, cosine=True)
    fc, _ = predict(pc)
    drc, _ = drive_errors(fc)
    okc = ec_err < 1e-7 and all(abs(drc[j] - NOTE_COSINE[j]) < 5e-4 for j in drc)
    check("(E2) the four-input cosine baseline refit (tau = 0) reproduces the note's unused drive errors +.796329, +2.898695, +6.238759, +11.008222 MHz (to 0.5 kHz)", okc,
          f"parameters {np.round(pc[:4], 8)}; calibration error {ec_err:.1e} GHz; drive errors " + ", ".join(f"{drc[j]:+.6f}" for j in drc))
    if not okc:
        fire("the cosine baseline does not reproduce the note's errors")
    # bigger basis
    fb, wb = predict(NOTE_P, N=24, M=20, K=14)
    dre, _ = drive_errors(fb)
    okb = all(abs(dre[j] - dr[j]) < 1e-3 for j in dr)
    fbf, wbf = predict(NOTE_P, N=20, K=14, full=True)
    drf, _ = drive_errors(fbf)
    okb &= all(abs(drf[j] - dr[j]) < 1e-3 for j in dr)
    check("(E3) beyond the note's basis (charges -24..24 with 20 transmon states and 14 photons; and the full 41-charge x 14-photon space with no transmon truncation) the drive errors move by less than 1 Hz per MHz-unit, i.e. < 1e-3 MHz", okb,
          f"larger reduced basis: " + ", ".join(f"{dre[j]:+.6f}" for j in dre) + "; full: " + ", ".join(f"{drf[j]:+.6f}" for j in drf) + f"; min assignment weights {wb:.3f}, {wbf:.3f}")
    if not okb:
        fire("drive errors change beyond the note's basis")
    # ---- E4: Fourier ratios
    cm = coeffs(NOTE_P[4])
    # V/EJ1 = sum_m a_m e^{i m phi} with a_m = c_m/(-2 c_1) (already normalised); the cos(m phi) coefficient is 2 a_m (m >= 1)
    c2, c3 = 2 * cm[2], 2 * cm[3]
    c1 = 2 * cm[1]
    okf = abs(c1 + 1.0) < 1e-12 and abs(c2 - 0.0104917249) < 5e-10 and abs(c3 + 0.00022017684) < 5e-10
    check("(E4) V_tau/EJ1 has cos(phi) coefficient -1 and, at the note's tau, +.0104917249 cos(2 phi) and -.00022017684 cos(3 phi) (own FFT, 16384 points)", okf, f"c1 = {c1:+.12f}, c2 = {c2:+.10f}, c3 = {c3:+.11f}")
    if not okf:
        fire("Fourier coefficients differ from the note's")
    # ---- E5: exact convention identity with a direct construction
    ec_, ej_, om_, g_, tau_ = NOTE_P
    delta = g_ ** 2 / (4 * ec_ * om_)

    def hphys_gaps(q, N=20, K=30, nlev=7):
        n, h0 = h_charge(NOTE_P, q, N)                                   # 4 EC (n - q)^2 + V
        a = np.diag(np.sqrt(np.arange(1, K)), 1)
        h = np.kron(h0, np.eye(K)) + om_ * np.kron(np.eye(len(n)), np.diag(np.arange(K, dtype=float))) + g_ * np.kron(np.diag(n - q), a + a.T)
        w = np.linalg.eigvalsh(h)[:nlev]
        return w - w[0]

    def old_gaps(ng, N=20, K=14, nlev=7):
        n, h0 = h_charge(NOTE_P, ng, N)
        a = np.diag(np.sqrt(np.arange(1, K)), 1)
        h = np.kron(h0, np.eye(K)) + om_ * np.kron(np.eye(len(n)), np.diag(np.arange(K, dtype=float))) + g_ * np.kron(np.diag(n), a + a.T)
        w = np.linalg.eigvalsh(h)[:nlev]
        return w - w[0]
    worst = 0.0
    for q in ((0.05, 0.13) if DRY else (0.05, 0.13, 0.25, 0.4)):
        worst = max(worst, float(np.abs(hphys_gaps(q) - old_gaps((1 - delta) * q)).max()))
    check("(E5) the lowest seven gaps of the directly constructed H_phys(q) = ... + G (n - q)(a + a^dag) equal those of the old model at ng = (1 - delta) q, delta = G^2/(4 EC Omega) (q = .05, .13, .25, .4; 30 photons vs 14)", worst < 1e-7,
          f"delta = {delta:.6f}; max difference {worst:.2e} GHz (finite Fock cutoffs are not exactly displacement invariant); {time.time() - T0:.0f} s")
    if worst >= 1e-7:
        fire("the offset-convention identity fails in the direct construction")
    # ---- E6: parity maxima from the direct physical-offset model
    def f06_phys(p, q, N=18, K=20):
        ec, ej, om, g, tau = p
        n, h0 = h_charge(p, q, N)
        e0, v0 = np.linalg.eigh(h0)
        a = np.diag(np.sqrt(np.arange(1, K)), 1)
        h = np.kron(h0, np.eye(K)) + om * np.kron(np.eye(len(n)), np.diag(np.arange(K, dtype=float))) + g * np.kron(np.diag(n - q), a + a.T)
        w, V = np.linalg.eigh(h)
        def lab(j, k):
            pr = np.abs(np.kron(v0[:, j], np.eye(K)[:, k]) @ V) ** 2
            i = int(np.argmax(pr)); return i, pr[i]
        i6, w6 = lab(6, 0); i0, w0 = lab(0, 0)
        if w6 < 0.5 or w0 < 0.5:
            raise Unassignable()
        return w[i6] - w[i0]

    def parity_max(p, nq):
        qs = np.linspace(0, 0.25, nq)
        vals = np.array([abs(f06_phys(p, q) - f06_phys(p, q + 0.5)) for q in qs])
        return qs, vals
    nq = 9 if DRY else 26
    qs, vals = parity_max(NOTE_P, nq)
    pc_full = pc
    qsc, valsc = parity_max(pc_full, nq)
    okp = abs(vals.max() * 1000 - 3.464585) < 5e-3 and abs(valsc.max() * 1000 - 0.544477) < 5e-3
    check("(E6) the parity-splitting maxima |f06(q) - f06(q + 1/2)| over q in [0, 1/4] from the direct H_phys(q) are 3.464585 MHz (Andreev) and .544477 MHz (cosine) to 5 kHz, and vanish at q = 1/4",
          okp and vals[-1] * 1000 < 1e-3 and valsc[-1] * 1000 < 1e-3,
          f"Andreev max {vals.max() * 1000:.6f} MHz at q = {qs[vals.argmax()]:.4f}; cosine max {valsc.max() * 1000:.6f} MHz at q = {qsc[valsc.argmax()]:.4f}; at q = 1/4: {vals[-1] * 1000:.2e}, {valsc[-1] * 1000:.2e} MHz; {time.time() - T0:.0f} s")
    if not (okp and vals[-1] * 1000 < 1e-3 and valsc[-1] * 1000 < 1e-3):
        fire("parity maxima differ from the note's")
    # ---- E7: scan for other calibration roots by profiling tau
    taus = np.linspace(0.0, 0.95, 20 if DRY else 96)
    prof = []
    start = np.array([0.18, 20.0, 7.75, 0.1])
    for tau in taus:
        best = None
        for st in (start, [0.15, 25.0, 7.74, 0.15], [0.3, 15.0, 7.8, 0.3]):
            def res4(z, tau=tau):
                try:
                    f, _ = predict(np.r_[z, tau], N=14, M=12, K=8)
                except Unassignable:
                    return np.full(5, 10.0)
                return (f[CALIDX] - CAL) / DIV
            try:
                r = least_squares(res4, st, bounds=([0.03, 1, 7, 0.001], [1, 100, 8.5, 1]), x_scale=[0.2, 20, 8, 0.1], ftol=1e-12, xtol=1e-12, gtol=1e-12, max_nfev=60)
            except Exception:
                continue
            c = float(np.max(np.abs(r.fun)))
            if best is None or c < best[0]:
                best = (c, r.x)
        prof.append((tau, best[0], best[1]))
    prof_c = np.array([p_[1] for p_ in prof])
    # roots: local minima of the profile with cost < 1e-6 GHz (1 kHz)
    roots = [(t, c, x) for i, (t, c, x) in enumerate(prof) if c < 1e-5 and (i == 0 or c <= prof[i - 1][1]) and (i == len(prof) - 1 or c <= prof[i + 1][1])]
    print("   profile (tau: max calibration residual in GHz) at every 8th grid point: " + "; ".join(f"{t:.3f}: {c:.1e}" for t, c, _ in prof[::8]), flush=True)
    near = [(t, c) for t, c, _ in prof if c < 1e-4]
    print(f"   {len(near)} of {len(prof)} grid points have residual below 1e-4 GHz (100 kHz): tau from {min(t for t, _ in near):.2f} to {max(t for t, _ in near):.2f}; the residual is below 1e-5 GHz only for tau in [{min(t for t, c, _ in prof if c < 1e-5):.2f}, {max(t for t, c, _ in prof if c < 1e-5):.2f}]", flush=True)
    # refine every candidate: free tau
    refined = []
    for t, c, x in roots:
        try:
            pr_, err_, rr = fit(CAL, np.r_[x, t], ncal=5, N=14, M=12, K=8, max_nfev=200)
            fr_, wr_ = predict(pr_)
            drr, _ = drive_errors(fr_)
            refined.append((pr_, err_, drr, wr_))
        except Exception as ex:
            print(f"   refinement failed at tau {t:.3f}: {ex}")
    uniq = []
    for pr_, err_, drr, wr_ in refined:
        if err_ < 1e-7 and all(np.max(np.abs(np.log(pr_[:4] / q[0][:4]))) > 1e-4 or abs(pr_[4] - q[0][4]) > 1e-4 for q in uniq):
            uniq.append((pr_, err_, drr, wr_))
    for pr_, err_, drr, wr_ in uniq:
        print(f"   exact root: EC {pr_[0]:.6f} EJ1 {pr_[1]:.6f} Omega {pr_[2]:.6f} G {pr_[3]:.6f} tau {pr_[4]:.6f}; calibration error {err_:.1e} GHz; drive errors " + ", ".join(f"{drr[j]:+.3f}" for j in drr) + f" MHz; min assignment weight {wr_:.3f}")
    others = [u for u in uniq if abs(u[0][4] - NOTE_P[4]) > 1e-3]
    small = [u for u in others if max(abs(u[2][j]) for j in u[2]) < 1.0]
    check(f"(E7) profiling tau over {len(taus)} values in [0, 0.95] (other four parameters refit to the five inputs): {len(uniq)} exact root(s) (calibration error < 1e-7 GHz) found, {len(others)} other than the note's; none other predicts all four unused drives to within 1 MHz",
          any(abs(u[0][4] - NOTE_P[4]) < 1e-3 for u in uniq) and not small,
          "; ".join(f"tau {u[0][4]:.4f}: " + ", ".join(f"{u[2][j]:+.2f}" for j in u[2]) for u in uniq) + f"; {time.time() - T0:.0f} s")
    if small:
        fire("another exact calibration root predicts the four unused drives within 1 MHz: " + "; ".join(f"tau {u[0][4]:.4f}" for u in small))
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: PR #9353 claim fails: " + "; ".join(FIRED))
        return 0
    print("SUMMARY: no falsifier fired: the independently built model reproduces the note's calibrated point, the unused drive and cavity errors, the cosine baseline, the Fourier ratios, the offset-convention identity (direct construction) and both parity maxima; "
          f"profiling tau found {len(uniq)} exact calibration root(s) ({len(others)} besides the note's)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
