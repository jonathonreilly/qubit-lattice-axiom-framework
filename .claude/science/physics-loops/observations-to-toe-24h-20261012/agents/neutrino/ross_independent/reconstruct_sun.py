#!/usr/bin/env python3
"""Independent second-stage source port and declared synthetic response probes.

This is not certified MATLAB execution or a reanalysis of unavailable raw TDMS.
The source-derived contract is in FROZEN_RECONSTRUCTION.md. No code is imported
from the composition worker. A fixed-mass number is only a diagnostic.
"""
from __future__ import annotations

import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import csv
import hashlib
import json
from pathlib import Path
import platform
import time

import numpy as np
import scipy
from scipy.io import loadmat
from scipy.signal import cheby1, filtfilt, freqz, sosfiltfilt

CAMPAIGN = Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
INPUT = CAMPAIGN / "composition"
OUTPUT = CAMPAIGN / "neutrino/ross_independent"
PIN = "1e103b78b5c3f2d948a30da4f1e7301c6b6f83f5"
RUNS = [6891, 6893, 6895, 6896, 6897, 6900, 6903, 6904, 6905,
        6923, 6925, 6926, 6927, 6930, 6931, 6936, 6939, 6949,
        6950, 6954, 6955, 6956, 6958, 6962, 6964]
MASS = 38.72e-3 / 2
LEVER = 3.77e-2 / 2
CALIB = np.exp(1j * np.deg2rad(53.69)) / .9958
SID_DAY = 86164.0905
THERMAL = np.sqrt(4 * 1.38064852e-23 * 293 * 3.78e-5 * (2*np.pi*6.8567e-4)**2 / 1.13e5)
A_SUN = 6.67430e-11 * 1.9891e30 / (149.6e9)**2
INJECTION = 1e-15


def check_stop():
    for name in ("STOP_REQUESTED", "USER_STOP_REQUESTED"):
        if (CAMPAIGN / name).exists():
            raise SystemExit(f"Stopped: {name}")
    deadline = json.loads((CAMPAIGN / "DEADLINE.json").read_text())["deadline_epoch"]
    if time.time() >= deadline:
        raise SystemExit("Campaign deadline reached")


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for piece in iter(lambda: f.read(1 << 20), b""):
            h.update(piece)
    return h.hexdigest()


def verify_inputs():
    manifest = json.loads((INPUT / "eotwash/manifest.json").read_text())
    assert manifest["repo_head"] == PIN
    used = {f"Fits/run{r}Fits.mat" for r in RUNS}
    used.update(("Fits/NewWashAnalysis.m", "Basis Functions/sunVect.py", "Basis Functions/sunVectMin.out"))
    receipts = []
    for item in manifest["files"]:
        if item["path"] in used:
            p = INPUT / "eotwash" / item["path"]
            assert digest(p) == item["sha256"], p
            receipts.append({**item, "local_path": str(p)})
    assert len(receipts) == len(used)
    p = INPUT / "eotwash_NewWashMultiRunSun.m"
    h = digest(p)
    assert h == "e37298004871bb9849cd6c188bea060a29e00e1fa8595560ae0b6b4080a33fd3"
    receipts.append({"local_path": str(p), "sha256": h,
                     "url": f"https://raw.githubusercontent.com/EotWash/EP-Analysis-Sun/{PIN}/NewWashMultiRunSun.m"})
    return receipts


def linear_detrend(z):
    # MATLAB detrend(vector): subtract the fitted constant and index-linear term.
    j = np.arange(len(z), dtype=float)
    j -= np.mean(j)
    w = z - np.mean(z)
    return w - j * (np.dot(j, w) / np.dot(j, j))


def midpoint_percentile(v, p):
    # Exact midpoint plotting positions, independently implemented.
    v = np.sort(v)
    return np.interp(p / 100, (np.arange(len(v)) + .5) / len(v), v)


def percentile_mask(z):
    c0, c1 = [midpoint_percentile(z.real, p) for p in (5, 95)]
    s0, s1 = [midpoint_percentile(z.imag, p) for p in (5, 95)]
    return (z.real > c0) & (z.real < c1) & (z.imag > s0) & (z.imag < s1)


def load_runs():
    times, values, flips, ids, counts = [], [], [], [], []
    for f, run in enumerate(RUNS, 1):
        out = loadmat(INPUT / f"eotwash/Fits/run{run}Fits.mat")["out"]
        assert out.shape[0] == 4 and np.isfinite(out).all()
        good = out[3] / THERMAL < 3.77
        ts = np.mod(out[0, good], 31556926.) + (31556926. if f >= 10 else 0.)
        times.append(ts)
        values.append(out[1, good] + 1j*out[2, good])
        flip = 1 if f < 3 or 13 < f < 20 else -1
        flips.append(np.full(sum(good), flip))
        ids.append(np.full(sum(good), run))
        counts.append({"run": run, "archived_points": out.shape[1], "thermal_selected": int(sum(good))})
    return dict(time=np.concatenate(times), value=np.concatenate(values),
                flip=np.concatenate(flips), run=np.concatenate(ids), counts=counts)


def detrend_runs(values, run_ids):
    result = np.empty_like(values)
    for run in RUNS:
        k = run_ids == run
        result[k] = linear_detrend(values[k])
    return result


def sampling(times):
    return 1. / (times[4] - times[3])


def dst(t):
    # All comparisons use the same OLD time vector, as in a MATLAB RHS.
    return t - (t > 307.042)/24 - (t < 69.082)/24 - (t < 433.041)/24 - (t > 671.041)/24


def response_order(q):
    diagnostics = []
    for n in range(8, 0, -1):
        b, a = cheby1(n, .05, .8/q)
        _, h = freqz(b, a, worN=np.array([np.pi*.8/q]))
        error = abs(abs(h[0]) - 10**(-.05/20))
        diagnostics.append(dict(order=n, cutoff_error=float(error), dc_gain=float(sum(b)/sum(a))))
        if error <= 1e-6:
            return n, diagnostics
    raise ValueError("No stable order")


class Basis:
    def __init__(self, raw, q, mode):
        self.mode, self.q = mode, q
        self.metadata = {"mode": mode, "q": q, "certified_native_matlab": False}
        if mode == "raw_minute":
            filtered = raw
            order, start = None, 0
        else:
            if mode == "adaptive_ba_last":
                order, diagnostics = response_order(q)
                self.metadata["order_diagnostics"] = diagnostics
                b, a = cheby1(order, .05, .8/q)
                # Traditional MATLAB padding length, not scipy's default 3*(n+1).
                filtered = filtfilt(b, a, raw, axis=0, padlen=3*order)
            else:
                order = int(mode.split("_")[0][3:])
                sos = cheby1(order, .05, .8/q, output="sos")
                filtered = sosfiltfilt(sos, raw, axis=0, padlen=3*order)
            start = (len(raw)-1) % q if mode.endswith("last") else 0
            filtered = filtered[start::q]
        self.metadata.update(filter_order=order, first_source_index_zero_based=start,
                             decimated_points=len(filtered))
        self.time = dst(filtered[:, 0])
        self.x = filtered[:, 1] + 1j*filtered[:, 2]
        self.sort = np.argsort(self.time, kind="stable")
        self.sorted_time = self.time[self.sort]
        self.metadata["nonincreasing_time_steps"] = int(np.sum(np.diff(self.time) <= 0))
        self.metadata["time_range_days"] = [float(self.time[0]), float(self.time[-1])]

    def nearest(self, times_seconds):
        targets = np.asarray(times_seconds) / 86400
        p = np.searchsorted(self.sorted_time, targets)
        left = self.sort[np.maximum(p-1, 0)]
        right = self.sort[np.minimum(p, len(self.time)-1)]
        dl, dr = abs(self.time[left] - targets), abs(self.time[right] - targets)
        # MATLAB min returns the first original index on exact ties.
        choose_left = (dl < dr) | ((dl == dr) & (left < right))
        indices = np.where(choose_left, left, right)
        distances = abs(self.time[indices] - targets)
        return self.x[indices], distances, indices


def fit_blocks(times, corrected_torque, basis, sample_f):
    labels = np.floor((times-times[0]) / 86400 / 2).astype(int)
    minimum = np.floor(sample_f * SID_DAY) / 4
    final = int(np.floor(np.ceil((times[-1]-times[0])/86400)/2))
    rows = []
    last_shadow = MASS
    for block in range(final + 1):
        which = labels == block
        if sum(which) == 0 or sum(which) < minimum:
            continue
        x, residual, indices = basis.nearest(times[which])
        last_shadow = float(residual[-1])
        z = corrected_torque[which]
        y = z - np.mean(z)
        denominator = np.vdot(x, x).real
        a = np.vdot(x, np.conjugate(y)) / denominator
        if a == 0:
            continue
        centered_x = x - np.mean(x)
        centered_gain = np.vdot(x, centered_x).real / denominator
        residual_std = np.std(np.conj(a*x) - y, ddof=1)
        # A literal two-real-parameter design offers an independent algebra check.
        real_design = np.block([[x.real[:, None], -x.imag[:, None]],
                                [-x.imag[:, None], -x.real[:, None]]])
        real_target = np.r_[y.real, y.imag]
        pair = np.linalg.lstsq(real_design, real_target, rcond=None)[0]
        assert abs(a - (pair[0]+1j*pair[1])) < 1e-29
        # The exact synthetic probe tests the coefficient/conjugation convention.
        synthetic_z = LEVER*MASS*INJECTION*np.conj(x)
        synthetic_y = synthetic_z - np.mean(synthetic_z)
        recovered = np.vdot(x, np.conj(synthetic_y))/denominator/(LEVER*MASS*INJECTION)
        assert abs(recovered - centered_gain) < 2e-14
        assert -.000000000001 <= centered_gain <= 1.000000000001
        rows.append({"block": block, "n": int(sum(which)), "time_start_days": float(times[which][0]/86400),
                     "time_end_days": float(times[which][-1]/86400), "coefficient_real_Nm": float(a.real),
                     "coefficient_imag_Nm": float(a.imag), "residual_std_Nm": float(residual_std),
                     "centering_only_gain": float(centered_gain), "last_residual_days": float(residual[-1]),
                     "last_basis_index_zero_based": int(indices[-1])})
    return rows, last_shadow, minimum


def summarize(rows, shadow):
    real = np.array([x["coefficient_real_Nm"] for x in rows])
    imag = np.array([x["coefficient_imag_Nm"] for x in rows])
    mean = np.array([np.mean(real), np.mean(imag)])
    sem = np.array([np.std(real, ddof=1), np.std(imag, ddof=1)]) / np.sqrt(len(rows))
    return {"blocks": len(rows), "fitted_points": sum(x["n"] for x in rows),
            "coefficient_mean_Nm_re_im": mean.tolist(), "coefficient_sem_Nm_re_im": sem.tolist(),
            "shadow_m_time_residual_days": shadow,
            "literal_display_numerals_re_im": (mean/(LEVER*shadow)*1e15).tolist(),
            "literal_display_sem_numerals_re_im": (sem/(LEVER*shadow)*1e15).tolist(),
            "physical_mass_diagnostic_fm_s2_re_im": (mean/(LEVER*MASS)*1e15).tolist(),
            "physical_mass_diagnostic_sem_fm_s2_re_im": (sem/(LEVER*MASS)*1e15).tolist(),
            "centering_gain_mean": float(np.mean([x["centering_only_gain"] for x in rows])),
            "centering_gain_range": [min(x["centering_only_gain"] for x in rows), max(x["centering_only_gain"] for x in rows)]}


def evaluate(run_data, values, basis, frozen_mask=None):
    z = detrend_runs(values, run_data["run"])
    mask = percentile_mask(z) if frozen_mask is None else frozen_mask
    ts = run_data["time"][mask]
    sample_f = sampling(ts)
    rows, shadow, minimum = fit_blocks(ts, CALIB*run_data["flip"][mask]*z[mask], basis, sample_f)
    summary = summarize(rows, shadow)
    summary.update(selected_points=int(sum(mask)), sample_interval_seconds=float(1/sample_f),
                   minimum_block_samples=float(minimum), first_selected_time_seconds=float(ts[0]))
    return summary, rows, mask


def injection_probe(data, nominal, mask, basis, injection_basis):
    x, _, _ = injection_basis.nearest(data["time"])
    dz = LEVER*MASS*INJECTION*np.conj(x)/(CALIB*data["flip"])
    results = {}
    for selection in ("fixed", "dynamic"):
        for sign in (-1, 1):
            output, rows, resulting_mask = evaluate(data, data["value"] + sign*dz, basis,
                                                  mask if selection == "fixed" else None)
            # If selected points 4/5 changed, the literal script would recompute
            # the basis factor q: reject this branch rather than silently freeze it.
            assert output["sample_interval_seconds"] == nominal["sample_interval_seconds"]
            difference = np.array(output["physical_mass_diagnostic_fm_s2_re_im"]) - np.array(nominal["physical_mass_diagnostic_fm_s2_re_im"])
            literal_difference = np.array(output["literal_display_numerals_re_im"]) - np.array(nominal["literal_display_numerals_re_im"])
            results[f"{selection}_{sign:+d}"] = dict(response_re_im= (difference/sign).tolist(),
                    literal_display_response_numerals_re_im=(literal_difference/sign).tolist(),
                    changed_selection_entries=int(np.sum(resulting_mask != mask)),
                    selected_points=output["selected_points"], blocks=output["blocks"],
                    shadow_m_time_residual_days=output["shadow_m_time_residual_days"])
    fixed_gain = np.array(results["fixed_+1"]["response_re_im"])
    assert np.max(abs(fixed_gain-np.array(results["fixed_-1"]["response_re_im"]))) < 2e-12
    results["source"] = injection_basis.mode
    results["injected_acceleration_m_s2"] = INJECTION
    results["misfit_array_unchanged"] = True
    results["raw_first_stage_injection"] = False
    return results


def main():
    check_stop()
    started = time.time()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    receipts = verify_inputs()
    data = load_runs()
    z0 = detrend_runs(data["value"], data["run"])
    mask = percentile_mask(z0)
    sample_f = sampling(data["time"][mask])
    raw = np.loadtxt(INPUT / "eotwash/Basis Functions/sunVectMin.out")
    source_sample_f = 1/(raw[1, 0]-raw[0, 0])/86400
    q = int(np.floor(source_sample_f/sample_f))
    assert q == 72
    baseline_basis = Basis(raw, q, "adaptive_ba_last")
    nominal, rows, mask = evaluate(data, data["value"], baseline_basis)
    # Exhaustive min cross-check for the baseline's 2240 timestamps.
    _, _, fast_indices = baseline_basis.nearest(data["time"])
    slow_indices = np.array([np.argmin(abs(baseline_basis.time-t/86400)) for t in data["time"]])
    assert np.array_equal(fast_indices, slow_indices)
    with (OUTPUT / "baseline_blocks.csv").open("w") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    matched_injection = injection_probe(data, nominal, mask, baseline_basis, baseline_basis)
    raw_basis = Basis(raw, q, "raw_minute")
    raw_injection = injection_probe(data, nominal, mask, baseline_basis, raw_basis)
    variants = {}
    for mode in ("sos5_last", "sos5_first", "sos6_last", "sos8_last", "raw_minute"):
        check_stop()
        basis = raw_basis if mode == "raw_minute" else Basis(raw, q, mode)
        output, _, _ = evaluate(data, data["value"], basis, mask)
        output["basis"] = basis.metadata
        variants[mode] = output
    results = {"status": "independent source port; no native MATLAB equivalence certified; no corrected experimental result",
               "upstream_commit": PIN,
               "software": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
               "constants": {"mass_kg": MASS, "lever_m": LEVER, "thermal_amplitude_Nm": float(THERMAL),
                             "sun_acceleration_m_s2": A_SUN, "nominal_q": q},
               "run_counts": data["counts"], "input_receipts": receipts,
               "baseline_basis": baseline_basis.metadata, "baseline": nominal,
               "matched_template_injection": matched_injection, "raw_minute_template_injection": raw_injection,
               "numerical_controls": variants,
               "paper_summary_known_before_fit": {"mean_fm_s2": .66, "sem_fm_s2": .61},
               "elapsed_seconds": time.time()-started}
    (OUTPUT / "independent_results.json").write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({k: results[k] for k in ("status", "baseline_basis", "baseline", "matched_template_injection", "raw_minute_template_injection", "elapsed_seconds")}, indent=2))
    print("All algebra, nearest-index, fixed-selection linearity and hash checks passed.")


if __name__ == "__main__":
    main()
