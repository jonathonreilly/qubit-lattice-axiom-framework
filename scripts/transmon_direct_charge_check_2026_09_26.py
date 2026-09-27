"""Direct charge x photon verification; all parameters and frequencies are GHz.

No transmon-subspace truncation enters the Hamiltonian. Bare transmon eigenvectors
are used only to assign dressed states. Outputs f01..f06,fres1,fres2, where
fres1 is conditional on physical transmon ground state.
"""
import numpy as np
from scipy.linalg import eigh
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import eigsh
from scipy.optimize import linear_sum_assignment


def independent_predict(parameters, charge_cutoff=20, photon_count=16):
    ec, ej, omega, g = np.asarray(parameters, dtype=float)
    if min(ec, ej, omega) <= 0 or charge_cutoff < 4 or photon_count < 2:
        raise ValueError('Positive energy scales and sufficient basis sizes required')
    labels = [(j, 0) for j in range(7)] + [(0, 1), (1, 1)]
    endpoint_frequencies, diagnostics = [], []
    for ng in (0., .5):
        n = np.arange(-charge_cutoff, charge_cutoff + 1, dtype=float)
        off = -.5 * ej * np.ones(len(n) - 1)
        hc = diags([off, 4 * ec * (n - ng)**2, off], [-1, 0, 1], format='csr')
        _, bare_vectors = eigh(hc.toarray())
        a = diags(np.sqrt(np.arange(1, photon_count)), 1,
                  shape=(photon_count, photon_count), format='csr')
        h = (kron(hc, eye(photon_count))
             + kron(eye(len(n)), diags(omega * np.arange(photon_count)))
             + g * kron(diags(n), a + a.T))
        # Increase spectral coverage until every target has a dominant (>1/2)
        # eigenstate; stop explicitly if unambiguous labeling is unavailable.
        count = min(40, h.shape[0] - 1)
        bare = np.column_stack([np.kron(bare_vectors[:, j], np.eye(photon_count)[:, r])
                                for j, r in labels])
        while True:
            energy, vectors = eigsh(h, k=count, which='SA', tol=1e-12,
                                   v0=np.random.default_rng(20260926).normal(size=h.shape[0]))
            order = np.argsort(energy)
            energy, vectors = energy[order], vectors[:, order]
            overlap = np.abs(bare.T @ vectors)**2
            indices = overlap.argmax(axis=1)
            weights = overlap[np.arange(len(labels)), indices]
            if np.min(weights) > .5:
                break
            if count == h.shape[0] - 1:
                raise ValueError('No dominant bare-state assignment; continuation needed')
            count = min(2 * count, h.shape[0] - 1)
        _, one_to_one = linear_sum_assignment(-overlap)
        if len(set(indices)) != len(labels) or not np.array_equal(indices, one_to_one):
            raise ValueError('Ambiguous dressed-state assignment')
        levels = energy[indices]
        freq = np.r_[levels[1:7] - levels[0], levels[7] - levels[0], levels[8] - levels[1]]
        residual = np.linalg.norm(h @ vectors[:, indices] - vectors[:, indices] * levels, axis=0)
        endpoint_frequencies.append(freq)
        diagnostics.append(dict(ng=ng, indices=indices.tolist(), bare_weights=weights.tolist(),
                                runner_up_weights=np.sort(overlap, axis=1)[:, -2].tolist(),
                                eigen_residual_max_GHz=float(max(residual)),
                                spectral_count=count, frequencies_GHz=freq.tolist()))
    return np.mean(endpoint_frequencies, axis=0), dict(
        charge_cutoff=charge_cutoff, photon_count=photon_count,
        labels=labels, endpoints=diagnostics,
        endpoint_difference_GHz=(endpoint_frequencies[1] - endpoint_frequencies[0]).tolist())
