#!/usr/bin/env python3
"""CPTP propagation controls and descriptive Daya Bay hall-shape statistics.

No likelihood, p-value, exclusion, Npred use, or arbitrary-law fit is produced.
See FROZEN_PROTOCOL.md and NEUTRINO_CHANNEL_AND_INPUT_REPORT.md.
Run with one numerical thread. Outputs and downloaded input bytes stay outside repo.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np
import scipy
from scipy.linalg import expm

ROOT = Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
DEFAULT_INPUT = ROOT / "neutrino/inputs"
BASE_URL = "https://arxiv.org/src/2211.14988v1/anc/"
EXPECTED = {
    "DayaBay_IBDPromptSpectrum_EH1_3158days.txt": "4c4c9bcf782782bba349e64851f4aa36a777bfcb3655038fcc6155fb62b40170",
    "DayaBay_IBDPromptSpectrum_EH2_3158days.txt": "d5f7db430d5c102bfc2c33e14ab6f2e28717270b3c8bcb0cdc7ed75401ceaff7",
    "DayaBay_IBDPromptSpectrum_EH3_3158days.txt": "c1e015b6b41a8da5a30ac3df387482207104963f1de5bd0bcc0a61ab1ba9ad83",
    "DayaBay_BackgroundSpectrum_EH1_3158days.txt": "b0c7c5822b0d292bdfaf60d8e4557310c7ad15a0976f1065f97c01df38c6985c",
    "DayaBay_BackgroundSpectrum_EH2_3158days.txt": "9274860914a5c083103af0ddc0b263464b83188382877bf80b3da23bc0edf0c9",
    "DayaBay_BackgroundSpectrum_EH3_3158days.txt": "ddb2cb9b3d411140e3201546ca2966c4d61f47fff0fb9ee0fd6a8a703bd979f4",
    "DayaBay_DetectorModel_Etrue_to_Eprompt.txt": "92a2c1399d0d768eae59ed9aec965dee18942357a5dbedb6a01231b4571e23c8",
    "supplemental.tex": "2a9676a80334c98310f96f201690945efb63cd576ea020564949c1a4b7e6c124",
}


def check_stop() -> None:
    # This is a sub-second calculation; still honor the campaign stop markers.
    for name in ("STOP_REQUESTED", "USER_STOP_REQUESTED"):
        if (ROOT / name).exists():
            raise SystemExit(f"Stopped by {ROOT / name}")


def acquire_and_verify(folder: Path, download: bool) -> dict:
    folder.mkdir(parents=True, exist_ok=True)
    for name, expected in EXPECTED.items():
        path = folder / name
        if download and not path.exists():
            subprocess.run(["/usr/bin/curl", "--fail", "--location", "--silent",
                            "--show-error", "--max-time", "40", "--output",
                            str(path), BASE_URL + name], check=True)
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f"Input SHA256 differs: {name}: {actual}")
    return {name: {"url": BASE_URL + name, "sha256": digest}
            for name, digest in EXPECTED.items()}


def response_audit(folder: Path) -> dict:
    matrix = np.loadtxt(folder / "DayaBay_DetectorModel_Etrue_to_Eprompt.txt")
    assert matrix.shape == (240, 240)
    assert np.min(matrix) >= 0
    column_sums = matrix.sum(axis=0)
    row_sums = matrix.sum(axis=1)
    centers = (np.arange(240) + .5) * .05
    samples = []
    for j in (20, 30, 40, 60, 80, 100, 140, 180, 192):
        samples.append({"column": j, "nominal_energy_MeV": float(centers[j]),
                        "column_sum": float(column_sums[j]),
                        "conditional_mean_row_energy_MeV":
                        float(centers @ matrix[:, j] / column_sums[j])})
    return {
        "shape": list(matrix.shape), "total": float(matrix.sum()),
        "nonzero_columns": int(np.count_nonzero(column_sums)),
        "nonzero_rows": int(np.count_nonzero(row_sums)),
        "positive_column_sum_min": float(column_sums[column_sums > 0].min()),
        "column_sum_max": float(column_sums.max()),
        "row_sum_max": float(row_sums.max()),
        "zero_column_indices": np.flatnonzero(column_sums == 0).tolist(),
        "samples": samples,
        "interpretation": "Not column-stochastic in either orientation; joint-histogram interpretation is an inference, not established metadata. Not used in spectrum comparison.",
    }


def normalized_ratio_stats(far, near, obs_far, obs_near, window, low, high):
    """Exact central ratios; diagonal-observed-count proxy propagated analytically.

    The window normalization is correlated with each pooled sum. Gradients retain
    that dependence. The actual covariance is unavailable; this proxy is neither
    a lower bound nor claimed conservative.
    """
    fw, nw = far[window].sum(), near[window].sum()

    def ratio_and_gradient(mask):
        fs, ns = far[mask].sum(), near[mask].sum()
        ratio = fs * nw / (ns * fw)
        gf = ratio * (mask.astype(float) / fs - window.astype(float) / fw)
        gn = ratio * (window.astype(float) / nw - mask.astype(float) / ns)
        return ratio, gf, gn

    rl, gfl, gnl = ratio_and_gradient(low)
    rh, gfh, gnh = ratio_and_gradient(high)
    gd_f, gd_n = gfh - gfl, gnh - gnl
    proxy_error = np.sqrt(np.sum(gd_f**2 * obs_far + gd_n**2 * obs_near))
    bin_ratios = (far[window] / fw) / (near[window] / nw)
    q = (far[high].sum() / far[low].sum()) / (near[high].sum() / near[low].sum())
    # The ratio-of-ratios cancels the full-window normalization exactly.
    gqf = q * (high.astype(float) / far[high].sum() - low.astype(float) / far[low].sum())
    gqn = q * (low.astype(float) / near[low].sum() - high.astype(float) / near[high].sum())
    qerr = np.sqrt(np.sum(gqf**2 * obs_far + gqn**2 * obs_near))
    return {"signal_window_far": float(fw), "signal_window_near": float(nw),
            "ratio_low": float(rl), "ratio_high": float(rh),
            "high_minus_low": float(rh-rl), "diagonal_count_proxy_error": float(proxy_error),
            "bin_ratio_min": float(bin_ratios.min()), "bin_ratio_max": float(bin_ratios.max()),
            "bin_ratio_range": float(np.ptp(bin_ratios)),
            "ratio_of_ratios_Q": float(q), "Q_diagonal_count_proxy_error": float(qerr),
            "central_Q_min_symmetric_relative_transfer_modulation": float(abs(q-1)/(q+1)),
            "bin_ratios": bin_ratios.tolist()}


def shape_audit(folder: Path) -> dict:
    observed, backgrounds = [], []
    edges = None
    for hall in (1, 2, 3):
        # Npred columns are not even parsed.
        data = np.loadtxt(folder / f"DayaBay_IBDPromptSpectrum_EH{hall}_3158days.txt",
                          usecols=(0, 1, 2, 3, 4, 5))
        bkg = np.loadtxt(folder / f"DayaBay_BackgroundSpectrum_EH{hall}_3158days.txt")
        assert data.shape == (26, 6) and bkg.shape == (78, 9)
        bkg = bkg.reshape(3, 26, 9)
        if edges is None:
            edges = data[:, :2]
        assert np.array_equal(data[:, :2], edges)
        for period in range(3):
            assert np.array_equal(bkg[period, :, :2], edges)
        # Tabulated component rounding can give differences of a few hundredths.
        assert np.max(abs(bkg[:, :, 3] - bkg[:, :, 4:].sum(axis=2))) < .04
        observed.append(data[:, 3:6].T)
        backgrounds.append(bkg[:, :, 3])
    obs = np.asarray(observed)
    bkg = np.asarray(backgrounds)
    signal = obs - bkg
    assert np.all(signal > 0)
    window = (edges[:, 0] >= 2) & (edges[:, 1] <= 8)
    low = (edges[:, 0] >= 2) & (edges[:, 1] <= 4)
    high = (edges[:, 0] >= 6) & (edges[:, 1] <= 8)
    result = {
        "actual_window_MeV": [float(edges[window, 0].min()), float(edges[window, 1].max())],
        "actual_low_MeV": [float(edges[low, 0].min()), float(edges[low, 1].max())],
        "actual_high_MeV": [float(edges[high, 0].min()), float(edges[high, 1].max())],
        "whole_bins_window_low_high": [int(window.sum()), int(low.sum()), int(high.sum())],
        "all_candidate_count_sum": float(obs.sum()),
        "uncertainty_scope": "DIAGONAL OBSERVED-COUNT PROXY ONLY. Nominal background fixed. No correction covariance or nuisance uncertainties. No experimental significance or exclusion.",
        "periods": {},
    }
    for p, name in enumerate(("6AD", "8AD", "7AD")):
        comparisons = {}
        for label, f, n, vf, vn in (
            ("EH3_over_EH1", signal[2,p], signal[0,p], obs[2,p], obs[0,p]),
            ("EH3_over_EH2", signal[2,p], signal[1,p], obs[2,p], obs[1,p]),
            ("EH3_over_pooled_near", signal[2,p], signal[0,p]+signal[1,p], obs[2,p], obs[0,p]+obs[1,p]),
            ("EH2_over_EH1_control", signal[1,p], signal[0,p], obs[1,p], obs[0,p]),
        ):
            comparisons[label] = normalized_ratio_stats(f, n, vf, vn, window, low, high)
        result["periods"][name] = comparisons
    return result


def channel_controls() -> dict:
    h = np.array([-.7, .15, .9])
    vectors = np.array([[0., 0.], [.3, -.1], [-.2, .8]])
    rates = .5*np.sum((vectors[:,None,:]-vectors[None,:,:])**2, axis=2)
    gaps = h[:,None]-h[None,:]
    H = np.diag(h)
    jumps = [np.diag(vectors[:,r]) for r in range(vectors.shape[1])]
    gen = np.empty((9,9), complex)
    for a in range(3):
        for b in range(3):
            e = np.zeros((3,3),complex); e[a,b] = 1
            g = -1j*(H@e-e@H)
            for j in jumps:
                g += j@e@j - .5*(j@j@e + e@j@j)
            gen[:,3*a+b] = g.ravel()
    max_expm_error, max_comp_error, min_choi = 0., 0., 0.
    for length in (0., .1, .7, 2.):
        k = np.exp((-1j*gaps-rates)*length)
        matrix = expm(gen*length)
        max_expm_error = max(max_expm_error, float(np.max(abs(matrix-np.diag(k.ravel())))))
        choi = np.zeros((9,9), complex)
        for a in range(3):
            for b in range(3):
                e = np.zeros((3,3),complex); e[a,b] = 1
                choi += np.kron(e, (matrix@e.ravel()).reshape(3,3))/3
        assert np.max(abs(choi-choi.conj().T)) < 1e-14
        min_choi = min(min_choi,float(np.linalg.eigvalsh(choi).min()))
        assert abs(np.trace(choi)-1) < 1e-14
        k1 = np.exp((-1j*gaps-rates)*(.3*length))
        k2 = np.exp((-1j*gaps-rates)*(.7*length))
        max_comp_error = max(max_comp_error,float(np.max(abs(k-k1*k2))))
    # Direct Kraus calculation, independent of the survival expression.
    max_survival_error = 0.
    min_probability, max_probability = 1., 0.
    for amplitude in (0., .0851, .5, 1.):
        p = (1+np.sqrt(1-amplitude))/2
        ket = np.array([np.sqrt(p),np.sqrt(1-p)],complex)
        rho = np.outer(ket,ket.conj())
        for exponent in (-1,0,1):
            for energy in (1.8,4.,8.):
                for length in (0.,.5,1.65,10.):
                    omega = 1.6*(energy/4)**exponent
                    gamma = .12*(energy/4)**2
                    d = np.exp(-gamma*length)
                    u = np.diag(np.exp(-1j*np.array([omega/2,-omega/2])*length))
                    z = np.diag([1.,-1.])
                    out = (1+d)/2*(u@rho@u.conj().T)+(1-d)/2*(u@z@rho@z@u.conj().T)
                    prob = float(np.vdot(ket,out@ket).real)
                    formula = 1-amplitude/2*(1-d*np.cos(omega*length))
                    max_survival_error = max(max_survival_error,abs(prob-formula))
                    min_probability = min(min_probability,prob)
                    max_probability = max(max_probability,prob)
    # Nonnegative pairwise rates do not suffice in dimension three.
    invalid_rates = np.array([[0.,1.,9.],[1.,0.,1.],[9.,1.,0.]])
    bad_kernel = np.exp(-.1*invalid_rates)
    bad_eigenvalues = np.linalg.eigvalsh(bad_kernel)
    u = np.array([1.,-2.,1.])
    assert u@invalid_rates@u > 0 and bad_eigenvalues[0] < -.01
    # A baseline mixture is CPTP but generally not a semigroup in mean length.
    mix = lambda s: .5*np.exp(-.5j*s)+.5*np.exp(-1.5j*s)
    mixture_error = abs(mix(2)-mix(1)**2)
    # Bounded static random phase and renewed phase have identical one-time maps
    # at integer steps, but different echo response. Poisson-kernel quadrature.
    r, m = .8, 4
    theta = (np.arange(16384)+.5)*(2*np.pi/16384)-np.pi
    density = (1-r*r)/(1-2*r*np.cos(theta)+r*r)
    char_error = max(abs(np.mean(density*np.exp(-1j*n*theta))-r**n) for n in range(13))
    static_echo = np.mean(density*np.exp(-1j*(m-m)*theta))
    renewed_echo = np.mean(density*np.exp(-1j*m*theta))*np.mean(density*np.exp(1j*m*theta))
    assert max_expm_error < 1e-13 and max_comp_error < 1e-13 and min_choi > -1e-13
    assert max_survival_error < 1e-13 and -1e-13 <= min_probability <= max_probability <= 1+1e-13
    assert char_error < 1e-12 and abs(static_echo-1) < 1e-12 and abs(renewed_echo-r**(2*m)) < 1e-12
    return {"analytic_vs_explicit_Lindblad_expm_max_error": max_expm_error,
            "semigroup_max_error": max_comp_error, "minimum_sampled_normalized_Choi_eigenvalue": min_choi,
            "Kraus_vs_survival_max_error": max_survival_error,
            "sampled_survival_range": [min_probability,max_probability],
            "invalid_pairwise_rate_counterexample": {"rates": invalid_rates.tolist(),
                "zero_sum_vector_quadratic_form": float(u@invalid_rates@u),
                "kernel_eigenvalues_at_L_0p1": bad_eigenvalues.tolist()},
            "baseline_mixture_composition_failure": float(mixture_error),
            "bounded_phase_memory_nonidentifiability": {"r":r,"echo_half_steps":m,
                "Fourier_character_quadrature_error":float(char_error),
                "static_noise_echo_coherence":float(static_echo.real),
                "renewed_noise_echo_coherence":float(renewed_echo.real),
                "same_unintervened_coherence_at_8_steps":r**8}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=ROOT / "neutrino/results.json")
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    check_stop()
    manifest = acquire_and_verify(args.inputs, args.download)
    result = {"scope":"Conditional mathematics and descriptive shape only; no experimental exclusion.",
              "source_revision":"7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de",
              "environment":{"python":sys.version,"numpy":np.__version__,"scipy":scipy.__version__,"platform":platform.platform()},
              "input_identity":manifest,"channel_controls":channel_controls(),
              "response_audit":response_audit(args.inputs),"shape_audit":shape_audit(args.inputs)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print("CHANNEL CONTROLS: all assertions passed; mathematical proof is in the note.")
    a = result["response_audit"]
    print(f"RESPONSE: total={a['total']:.12f}; max column sum={a['column_sum_max']:.12f}; nonzero columns={a['nonzero_columns']}/240")
    print("SHAPE: actual low 2.05-3.80 MeV; high 6.05-7.30 MeV; normalization 2.05-7.30 MeV")
    print("DIAGONAL COUNT PROXY ERRORS ONLY; NO SIGNIFICANCE OR EXCLUSION")
    for period, comparisons in result["shape_audit"]["periods"].items():
        for name, s in comparisons.items():
            print(f"{period} {name}: high-low={100*s['high_minus_low']:.6f}% +/- {100*s['diagonal_count_proxy_error']:.6f}% proxy; Q={s['ratio_of_ratios_Q']:.8f} +/- {s['Q_diagonal_count_proxy_error']:.8f} proxy")
    print(f"OUTPUT: {args.output}")


if __name__ == "__main__":
    main()
