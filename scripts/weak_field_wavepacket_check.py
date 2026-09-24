"""Finite controls for a supplied compact-rotor weak-field packet limit.

This computes cubic incidence and harmonic spectra, and a complete one-loop
compact rotor. It is neither a many-body phase proof nor an independent audit.
No author/reviewer module or expected numerical output is imported.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/weak_field_wavepacket_check.py',)
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import itertools
import json
import math
import platform
import sys

import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal

HERE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": sha256(data).hexdigest()}


def modular_rank(matrix, prime=65521):
    a = np.array(matrix, dtype=np.int64) % prime
    nr, nc = a.shape
    rank = 0
    for col in range(nc):
        nz = np.flatnonzero(a[rank:, col])
        if not len(nz):
            continue
        pivot = rank + int(nz[0])
        a[[rank, pivot]] = a[[pivot, rank]]
        a[rank, col:] = a[rank, col:] * pow(int(a[rank, col]), -1, prime) % prime
        if rank+1 < nr:
            # Products and subtraction are < 2*prime^2, far below int64 limits.
            a[rank+1:, col:] = (a[rank+1:, col:] -
                                a[rank+1:, col, None] * a[rank, None, col:]) % prime
        rank += 1
        if rank == nr:
            break
    return rank


def cubic(side):
    sites = list(itertools.product(range(side), repeat=3))
    index = {x: i for i, x in enumerate(sites)}
    volume = len(sites)
    edges = 3*volume
    divergence = np.zeros((volume, edges), dtype=np.int64)
    curl = np.zeros((edges, edges), dtype=np.int64)

    def step(x, mu):
        y = list(x)
        y[mu] = (y[mu]+1) % side
        return tuple(y)

    def edge(x, mu):
        return 3*index[x]+mu

    face = 0
    for x in sites:
        for mu in range(3):
            divergence[index[x], edge(x, mu)] += 1
            divergence[index[step(x, mu)], edge(x, mu)] -= 1
        for mu, nu in itertools.combinations(range(3), 2):
            curl[face, edge(x, mu)] += 1
            curl[face, edge(step(x, mu), nu)] += 1
            curl[face, edge(step(x, nu), mu)] -= 1
            curl[face, edge(x, nu)] -= 1
            face += 1
    assert np.count_nonzero(curl @ divergence.T) == 0
    harmonic = np.tile(np.eye(3, dtype=np.int64), (volume, 1))
    assert np.count_nonzero(divergence @ harmonic) == 0
    assert np.count_nonzero(curl @ harmonic) == 0
    rb = modular_rank(divergence)
    rc = modular_rank(curl)
    assert rb == volume-1 and rc == 2*(volume-1)

    values, vectors = np.linalg.eigh((curl.T @ curl).astype(float))
    predicted = [0.0]*(volume+2)
    fourier_rows = []
    for n in sites:
        if n == (0, 0, 0):
            continue
        k = 2*np.pi*np.array(n)/side
        q = np.exp(1j*k)-1
        symbol = np.vdot(q, q).real*np.eye(3)-np.outer(q, q.conj())
        eig = np.linalg.eigvalsh(symbol)
        lam = float(4*np.sin(k/2) @ np.sin(k/2))
        assert np.max(np.abs(eig-[0, lam, lam])) < 1e-12
        predicted += [lam, lam]
        fourier_rows.append((n, lam))
    discrepancy = float(np.max(np.abs(values-np.sort(predicted))))
    assert discrepancy < 2e-12
    positive = values > 1e-8
    covariance = (vectors[:, positive] / (2*np.sqrt(values[positive]))) @ vectors[:, positive].T
    variance = np.einsum('ij,ij->i', curl @ covariance, curl)
    assert np.min(variance) > 0
    # Vacuum: ||(curl x)_p^4 psi|| = sqrt(105)*variance_p^2.
    # Potential remainder coefficient for c/a=1 is (g^2/24)*sum_p of these.
    quartic_bound = float(math.sqrt(105)*np.sum(variance**2)/24)
    return {"side": side, "volume": volume, "edge_count": edges,
            "boundary_of_boundary_exact_zero": True,
            "divergence_rank_mod_65521": rb, "curl_rank_mod_65521": rc,
            "zero_curl_dimension": int(np.count_nonzero(~positive)),
            "transverse_oscillators": int(np.count_nonzero(positive)),
            "full_spectrum_max_discrepancy": discrepancy,
            "smallest_positive_lambda": float(values[positive][0]),
            "plaquette_vacuum_variance_range": [float(min(variance)), float(max(variance))],
            "vacuum_potential_residual_bound_over_g2_at_c_over_a_one": quartic_bound,
            "scope": "Exact incidence/modular ranks plus floating harmonic spectral control; no compact many-body diagonalization."}


def rotor_case(g, cutoff_multiplier):
    cutoff = int(math.ceil(cutoff_multiplier/g))
    m = np.arange(-cutoff, cutoff+1, dtype=float)
    diagonal = 2*g*g*m*m + 1/(g*g)
    off = np.full(len(m)-1, -1/(2*g*g))
    eigenvalues, eigenvectors = eigh_tridiagonal(diagonal, off)
    ground = np.exp(-(g*m)**2).astype(complex)
    ground /= np.linalg.norm(ground)
    first = -2j*g*m*ground
    first /= np.linalg.norm(first)
    assert abs(np.vdot(ground, first)) < 1e-13

    def action(v):
        out = diagonal*v
        out[1:] += off*v[:-1]
        out[:-1] += off*v[1:]
        return out

    residuals = [float(np.linalg.norm(action(ground)-ground)),
                 float(np.linalg.norm(action(first)-3*first))]
    initial = (ground+first)/math.sqrt(2)
    coeff = eigenvectors.T @ initial
    times = []
    for duration in (.25, 1.0, 3.0):
        state = eigenvectors @ (np.exp(-1j*duration*eigenvalues)*coeff)
        reference = (np.exp(-1j*duration)*ground+np.exp(-3j*duration)*first)/math.sqrt(2)
        error = float(np.linalg.norm(state-reference))
        duhamel_bound = duration*sum(residuals)/math.sqrt(2)
        assert error <= duhamel_bound + 1e-10
        times.append({"time": duration, "state_norm_difference": error,
                      "norm_difference_over_g2": error/g**2,
                      "infidelity": float(max(0, 1-abs(np.vdot(reference, state))**2)),
                      "finite_matrix_duhamel_bound": duhamel_bound,
                      "state_norm_error": float(abs(np.linalg.norm(state)-1))})
    return {"g": g, "electric_cutoff": cutoff, "dimension": len(m),
            "lowest_four_energies": list(map(float, eigenvalues[:4])),
            "first_two_energy_shifts_over_g2": [float((eigenvalues[0]-1)/g**2),
                                                float((eigenvalues[1]-3)/g**2)],
            "harmonic_packet_residual_norms": residuals,
            "residuals_over_g2": [x/g**2 for x in residuals], "dynamics": times}


def continuum_dispersion():
    out = []
    # Fixed physical box length ell=2*pi, c=1: physical momenta are integer n.
    for n in ((1, 0, 0), (1, 2, 0), (1, 2, 3)):
        continuum = float(np.linalg.norm(n))
        for side in (12, 24, 48, 96, 192):
            a = 2*np.pi/side
            lattice = float(2/a*np.linalg.norm(np.sin(np.array(n)*a/2)))
            # |sin z-z| <= |z|^3/6 gives the norm/Lipschitz frequency bound.
            bound = float(a*a*np.linalg.norm(np.array(n, dtype=float)**3)/24)
            assert abs(lattice-continuum) <= bound + 1e-14
            out.append({"mode": list(n), "side": side, "a": a,
                        "lattice_frequency": lattice, "continuum_frequency": continuum,
                        "error": abs(lattice-continuum), "analytic_error_bound": bound})
    return out


def main():
    gs = (.4, .2, .1, .05)
    primary = [rotor_case(g, 7) for g in gs]
    larger = [rotor_case(g, 10) for g in gs]
    cutoff_comparison = []
    for a, b in zip(primary, larger):
        energy = max(abs(x-y) for x, y in zip(a['lowest_four_energies'], b['lowest_four_energies']))
        errors = max(abs(x['state_norm_difference']-y['state_norm_difference'])
                     for x, y in zip(a['dynamics'], b['dynamics']))
        assert energy < 2e-10 and errors < 2e-10
        cutoff_comparison.append({"g": a['g'], "largest_energy_change": energy,
                                  "largest_dynamical_error_change": errors})
    output = {"created_utc": datetime.now(timezone.utc).isoformat(),
              "script": identity(__file__),
              "runtime": {"python": sys.version, "numpy": np.__version__,
                          "scipy": scipy.__version__, "platform": platform.platform()},
              "cubic_cochains": [cubic(side) for side in (3, 4, 6)],
              "compact_single_loop": primary, "larger_cutoff": larger,
              "cutoff_comparison": cutoff_comparison,
              "limiting_single_loop_residuals_over_g2": [math.sqrt(105)/24, math.sqrt(945)/24],
              "continuum_dispersion": continuum_dispersion(),
              "status": "Author finite controls. Finite-box packet convergence is proved analytically in the companion note; no phase, native derivation or independent verification claimed."}
    data = json.dumps(output, indent=2)+'\n'
    (HERE/'WEAK_FIELD_WAVEPACKET_RESULTS.json').write_text(data)
    print(data, end='')


if __name__ == '__main__':
    main()
