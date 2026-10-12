"""Disjoint weighted-position Galerkin reference versus candidate ODE flow."""
import argparse
import hashlib
import importlib.util
import json
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import quad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("candidate_under_test", args.candidate)
    target = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(target)
    m, v, a = 0.91, 1.17, 0.37
    sigma = np.sqrt(m*m/4+v*v/a**2)
    g, J = sigma/2+m/4, sigma/2-m/4
    nq = 2048
    q = -np.pi/a + (2*np.pi/a)*np.arange(nq)/nq
    dq = 2*np.pi/(a*nq)
    initial = {-3: 0.23+0.17j, -1: -0.31+0.11j,
               0: 0.71-0.19j, 2: 0.24+0.38j}
    normalizer = np.sqrt(sum(abs(c)**2 for c in initial.values()))
    initial = {n: c/normalizer for n, c in initial.items()}

    def f(x):
        return np.sqrt(a/(2*np.pi))*sum(c*np.exp(-1j*a*n*x)
                                        for n, c in initial.items())

    # Independent source: positive eigenvalue of the actual 2x2 parent kernel.
    nfft = 8192
    k = 2*np.pi*np.arange(nfft)/nfft
    off = 2j*(g-J*np.exp(-1j*k))
    kernel = np.zeros((nfft, 2, 2), dtype=complex)
    kernel[:, 0, 1] = off
    kernel[:, 1, 0] = off.conj()
    band = np.linalg.eigvalsh(kernel)[:, 1]
    hopping = np.fft.fft(band)/nfft
    def parent_E(x):
        return 2*np.sqrt(g*g+J*J-2*g*J*np.cos(a*x))
    length, length_err = quad(lambda x: 1/parent_E(x), -np.pi/a, np.pi/a,
                             epsabs=1e-12, epsrel=1e-12, limit=100)
    times = [0.43, -0.43, 0.91, -0.91, length+0.23, -length-0.23]
    targets = {s: target.transport(q, s, a, m, v, f) for s in times}
    predicates = []
    def check(label, observed, limit):
        predicates.append({"label": label, "observed": float(observed),
                           "limit": limit, "ok": bool(observed <= limit)})
    rows = []
    final_B = None
    final_modes = None
    final_c0 = None
    final_eig = None
    for N in [24, 48, 80, 128]:
        modes = np.arange(-N, N+1)
        energy_matrix = hopping[(modes[:, None]-modes[None, :]) % nfft]
        # Literal weighted real-position kernel; no target differential operator.
        B = a*((modes[:, None]+modes[None, :]-1)/2)*energy_matrix
        hermitian_error = np.max(np.abs(B-B.conj().T))
        eig, vectors = np.linalg.eigh(B)
        c0 = np.array([initial.get(int(n), 0j) for n in modes])
        spectral0 = vectors.conj().T@c0
        basis = np.sqrt(a/(2*np.pi))*np.exp(-1j*a*q[:, None]*modes[None, :])
        for s in times:
            evolved = vectors@(np.exp(-1j*s*eig)*spectral0)
            reference = basis@evolved
            actual, F, info = targets[s]
            error = np.sqrt(dq*np.sum(abs(reference-actual)**2))
            norm2 = dq*np.sum(abs(actual)**2)
            rows.append({"mode_cutoff": N, "s": s,
                         "complex_wavefunction_error": float(error),
                         "transport_norm_squared": float(norm2),
                         "reference_norm_squared": float(dq*np.sum(abs(reference)**2)),
                         "matrix_hermiticity_error": float(hermitian_error),
                         "flow_lift_range": [float(F.min()), float(F.max())],
                         "ode": info,
                         "passes_fixed_final_error_target": bool(error <= 2e-9)})
            if N == 128:
                check(f"full_wavefunction_s_{s:.12g}", error, 2e-9)
                check(f"unitarity_s_{s:.12g}", abs(norm2-1), 2e-10)
        final_B, final_modes, final_c0 = B, modes, c0
        final_eig = (eig, vectors)
    eig, vectors = final_eig
    cycle_vector = vectors@(np.exp(-1j*length*eig)*(vectors.conj().T@final_c0))
    predicted_cycle = target.gauge_cycle_phase()*final_c0
    check("actual_matrix_versus_candidate_gauge_cycle",
          np.linalg.norm(cycle_vector-predicted_cycle), 2e-9)
    check("actual_matrix_minus_identity_holonomy",
          np.linalg.norm(cycle_vector+final_c0), 2e-9)
    # A candidate transformed eigenfunction must have the actual periodic trace.
    endpoints = np.array([-np.pi/a, np.pi/a])
    uend = np.array([-length/2, length/2])
    edge_E = parent_E(endpoints)
    traces = []
    for n in [-2, 0, 3]:
        wave = np.exp(-1j*a*endpoints/2)*np.exp(-1j*target.gauge_frequency(n, length)*uend)/np.sqrt(edge_E)
        mismatch = abs(wave[1]-wave[0])
        traces.append({"n": n, "endpoint_mismatch": float(mismatch)})
        check(f"periodic_domain_trace_n_{n}", mismatch, 2e-12)
    # Weighted matrix and literal derivative expectation pin the original sign.
    # This target uses its own origin coefficient; the source-weighted reference is fixed.
    Evals = parent_E(q)
    fvals = f(q)
    fprime = np.sqrt(a/(2*np.pi))*sum((-1j*a*n)*c*np.exp(-1j*a*n*q)
                                                   for n, c in initial.items())
    Ep = 4*g*J*a*np.sin(a*q)/Evals
    target_action = 1j*(Evals*fprime+Ep*fvals/2)+target.ORIGIN_COEFFICIENT*a*Evals*fvals
    basis = np.sqrt(a/(2*np.pi))*np.exp(-1j*a*q[:, None]*final_modes[None, :])
    position_action = basis@(final_B@final_c0)
    origin_action_error = np.sqrt(dq*np.sum(abs(target_action-position_action)**2))
    check("literal_weighted_origin_action", origin_action_error, 2e-9)
    result = {"method": "actual 2x2 kernel eigenband -> weighted real-position Fourier matrix -> Hermitian evolution; separately candidate ODE transport",
              "candidate": str(Path(args.candidate).resolve()),
              "candidate_sha256": hashlib.sha256(Path(args.candidate).read_bytes()).hexdigest(),
              "fixture": {"m": m, "v": v, "a": a, "g": g, "J": J, "nq": nq, "kernel_fft_points": nfft},
              "circle_length": length, "quad_reported_error": length_err,
              "rows": rows, "domain_traces": traces, "predicates": predicates,
              "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
              "limits": "Floating diagnostics, no interval bounds; common mathematical conventions with author; no domain theorem from PASS counts."}
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if all(x["ok"] for x in predicates) else 1


if __name__ == "__main__":
    raise SystemExit(main())

