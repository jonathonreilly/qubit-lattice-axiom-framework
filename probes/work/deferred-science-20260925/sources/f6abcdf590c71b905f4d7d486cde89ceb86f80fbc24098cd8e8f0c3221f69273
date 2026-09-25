#!/usr/bin/env python3
"""Fresh POST controls. No campaign, author, or PRE builder imports.

These finite controls test algebra and counterexamples, not the spin limit.
"""
from pathlib import Path
import hashlib
import json
import math
import sys
import numpy as np

HERE = Path(__file__).resolve().parent


def projector(v):
    return np.outer(v, v.conj())


def trace_norm(x):
    return float(np.linalg.svd(x, compute_uv=False).sum())


def fisher(rho, h):
    vals, vecs = np.linalg.eigh((rho + rho.conj().T) / 2)
    assert vals.min() > -1e-12
    vals = np.maximum(vals, 0)
    h_eig = vecs.conj().T @ h @ vecs
    total = 0.0
    for i, v in enumerate(vals):
        for j, w in enumerate(vals):
            if v + w > 1e-14:
                total += 2 * (v - w) ** 2 / (v + w) * abs(h_eig[i, j]) ** 2
    return float(total)


def non_eigenvector_phase_witness():
    h = np.zeros((5, 5), complex)
    h[:2, :2] = [[-2, 1j], [-1j, 3]]
    h[2:4, 2:4] = [[100, 2], [2, 105]]
    h[4, 4] = 220
    a = np.array([1, 2j, 0, 0, 0], complex) / math.sqrt(5)
    b = np.array([0, 0, 3, 1 + 1j, 0], complex) / math.sqrt(11)
    assert np.linalg.norm(h @ a - np.vdot(a, h @ a) * a) > 0.1
    assert np.linalg.norm(h @ b - np.vdot(b, h @ b) * b) > 0.1
    ell, u, z = math.sqrt(.71), math.sqrt(.17), math.sqrt(.12)
    phi = ell * a + u * b + z * np.eye(5)[4]
    p = .013
    omega = p * projector(phi)
    witness = 1j * (np.outer(b, a.conj()) - np.outer(a, b.conj()))
    derivative = float(abs(np.trace(omega @ (1j * (h @ witness - witness @ h)))))
    expected_derivative = 2 * p * ell * u * abs(np.vdot(b, h @ b) - np.vdot(a, h @ a))
    v = float(np.trace(omega @ witness @ witness).real)
    assert abs(derivative - expected_derivative) < 1e-13
    assert abs(v - p * (ell**2 + u**2)) < 1e-14
    assert derivative**2 / v <= fisher(omega, h) + 1e-10
    energies = np.linalg.eigvalsh(h)
    centered_norm = (energies[-1] - energies[0]) / 2
    rows = []
    for noise, loss in [(2e-5, 0), (7e-4, 3e-4)]:
        sigma = (1 - loss) * ((1 - noise) * omega + noise * p * np.eye(5) / 5)
        eta = trace_norm(sigma - omega)
        bound = max(derivative - 2 * centered_norm * eta, 0)**2 / (v + eta)
        actual = fisher(sigma, h)
        assert actual >= bound - 1e-10
        rows.append({'noise': noise, 'loss': loss, 'selected_error': eta,
                     'selected_probability': float(np.trace(sigma).real),
                     'phase_witness_lower': bound, 'selected_fisher': actual})
    return {'non_eigenvector_derivative': derivative,
            'formula_derivative': float(expected_derivative),
            'phase_witness_lower': derivative**2 / v,
            'selected_fisher': fisher(omega, h), 'noisy_rows': rows}


def pair_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def pair_sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def frequency_support_controls():
    # Exact spectral labels a+b*sqrt(2): no common period is used.
    system_levels = [(0, 0), (1, 0), (0, 1), (5, 1)]
    resource_levels = [(0, 0), (1, 0), (4, 1)]
    system_energy = np.array([a + b * math.sqrt(2) for a, b in system_levels])
    resource_energy = np.array([a + b * math.sqrt(2) for a, b in resource_levels])
    basis = [(s, r, f) for s in range(4) for r in range(3) for f in range(2)]
    labels = [pair_add(system_levels[s], resource_levels[r]) for s, r, f in basis]
    rng = np.random.default_rng(240924083)
    unitary = np.zeros((24, 24), complex)
    for level in sorted(set(labels)):
        inds = [i for i, x in enumerate(labels) if x == level]
        raw = rng.normal(size=(len(inds), len(inds))) + 1j * rng.normal(size=(len(inds), len(inds)))
        block, _ = np.linalg.qr(raw)
        unitary[np.ix_(inds, inds)] = block
    assert np.linalg.norm(unitary.conj().T @ unitary - np.eye(24)) < 1e-13
    assert all(unitary[i, j] == 0 for i in range(24) for j in range(24) if labels[i] != labels[j])
    psi = np.array([1, 1j, 0, 0], complex) / math.sqrt(2)
    theta = np.array([1, 1, 0], complex) / math.sqrt(2)
    resource = .7 * projector(theta) + .3 * np.diag([0, 0, 1])
    rho = projector(psi)
    initial = np.kron(np.kron(rho, resource), np.diag([1, 0]))
    final = unitary @ initial @ unitary.conj().T
    selected = np.zeros((4, 4), complex)
    for i, (s, r, f) in enumerate(basis):
        for j, (ss, rr, ff) in enumerate(basis):
            if r == rr and f == ff == 1:
                selected[s, ss] += final[i, j]
    system_modes = {pair_sub(system_levels[i], system_levels[j])
                    for i in range(4) for j in range(4) if abs(rho[i, j]) > 1e-14}
    resource_modes = {pair_sub(resource_levels[i], resource_levels[j])
                      for i in range(3) for j in range(3) if abs(resource[i, j]) > 1e-14}
    total_modes = {pair_add(a, b) for a in system_modes for b in resource_modes}
    absent_entries = [abs(selected[i, j]) for i in range(4) for j in range(4)
                      if pair_sub(system_levels[i], system_levels[j]) not in total_modes]
    assert max(absent_entries) < 1e-13
    assert np.linalg.norm(selected[3, :3]) < 1e-13
    assert selected[3, 3].real > 1e-4  # High populations need no high-frequency coherence.
    a = np.array([math.sqrt(.6), 1j * math.sqrt(.4), 0, 0], complex)
    b = np.array([0, 0, 0, 1], complex)
    p, ell, u = .07, math.sqrt(.9), math.sqrt(.1)
    phi = ell * a + u * b
    omega = p * projector(phi)
    witness = np.outer(a, b.conj()) + np.outer(b, a.conj())
    expected_error_lower = 2 * p * ell * u
    assert abs(np.trace(selected @ witness)) < 1e-13
    assert abs(np.trace(omega @ witness).real - expected_error_lower) < 1e-14
    assert trace_norm(selected - omega) >= expected_error_lower - 1e-13
    pinched = p * (ell**2 * projector(a) + u**2 * projector(b))
    assert abs(trace_norm(pinched - omega) - expected_error_lower) < 1e-13
    bandwidth = max(abs(a + b * math.sqrt(2)) for a, b in resource_modes)
    assert bandwidth == 1
    # Counterexample to dropping initial system frequencies: identity passes rho through.
    assert abs(rho[0, 1]) > .49
    stationary_resource_modes = {(0, 0)}
    assert (1, 0) not in stationary_resource_modes and (1, 0) in system_modes
    # Bandwidth alone is not sufficient: gap sqrt(2) is absent from modes {0,+/-2}.
    large_but_wrong_modes = {(0, 0), (2, 0), (-2, 0)}
    assert 2 > math.sqrt(2) and (0, 1) not in large_but_wrong_modes
    return {'exact_energy_labels': 'a+b*sqrt(2)',
            'system_modes': sorted(system_modes), 'resource_modes': sorted(resource_modes),
            'input_modes': sorted(total_modes),
            'maximum_forbidden_output_entry': float(max(absent_entries)),
            'selected_high_population': float(selected[3, 3].real),
            'selected_error': trace_norm(selected - omega),
            'witness_error_lower': expected_error_lower,
            'pinched_target_error': trace_norm(pinched - omega),
            'resource_coherence_bandwidth': bandwidth,
            'resource_spectral_diameter': float(np.ptp(resource_energy)),
            'initial_input_frequency_omission_rejected': True,
            'bandwidth_sufficiency_rejected_by_missing_sqrt2_mode': True}


def restricted_swap_controls():
    # System states 0,1: initial low sector; 2,3,4: output low/high1/high2.
    # State 5 is an additional excluded sector. D={0,1,2,3}; both flags have H=0.
    # All conservation tests apply globally, including system D-perp.
    basis = [(s, fs, r, fr) for s in range(6) for fs in range(2)
             for r in range(4) for fr in range(2)]
    index = {x: i for i, x in enumerate(basis)}
    unitary = np.zeros((96, 96))
    for source, (s, fs, r, fr) in enumerate(basis):
        target = (r, fr, s, fs) if s < 4 else (s, fs, r, fr)
        unitary[index[target], source] = 1
    assert np.array_equal(unitary.T @ unitary, np.eye(96))
    rows = []
    alpha, delta, bcoef, rcoef, second_weight = .25, 1.5, 2, 4, 3
    for epsilon in [.25, .125, .0625]:
        gap = delta * epsilon**-4
        energies = np.array([-3, 1, -2, gap + 2 * epsilon**-2,
                             2 * gap - epsilon**-2, 7 * gap])
        ground = float(min(energies[:4]))
        resource_energies = np.repeat(energies[:4] - ground, 2)
        total_energy = np.array([energies[s] + energies[r] - ground for s, fs, r, fr in basis])
        conservation_residual = np.linalg.norm((total_energy[:, None] - total_energy[None, :]) * unitary)
        assert conservation_residual == 0
        q1, q2 = (rcoef / bcoef) * epsilon**2, second_weight * epsilon**4
        phi = np.array([0, 0, math.sqrt(1 - q1 - q2), math.sqrt(q1), math.sqrt(q2), 0], complex)
        truncated = phi.copy(); truncated[4] = 0
        truncated /= np.linalg.norm(truncated)
        p = alpha**2 * bcoef * epsilon**2
        success = np.zeros(8, complex)
        success[1::2] = truncated[:4]
        failure = np.eye(8)[0]
        resource = p * projector(success) + (1 - p) * projector(failure)
        psi = np.array([math.sqrt(.4), 1j * math.sqrt(.6), 0, 0, 0, 0])
        sf_initial = np.kron(projector(psi), np.diag([1, 0]))
        initial = np.kron(sf_initial, resource)
        final = unitary @ initial @ unitary.T
        accessible = np.einsum('arbr->ab', final.reshape(12, 8, 12, 8))
        embed = np.eye(12, 8)
        expected_accessible = embed @ resource @ embed.T
        assert trace_norm(accessible - expected_accessible) < 1e-13
        selected = accessible[1::2, 1::2]
        assert trace_norm(selected - p * projector(truncated)) < 1e-13
        error = trace_norm(selected - p * projector(phi))
        exact_error = 2 * p * math.sqrt(q2)
        assert abs(error - exact_error) < 1e-13
        h_resource = np.diag(resource_energies)
        qfi = fisher(resource, h_resource)
        mean = float(np.trace(resource @ h_resource).real)
        conditional_mean = float(np.vdot(truncated, energies * truncated).real)
        conditional_var = float(np.vdot(truncated, energies**2 * truncated).real) - conditional_mean**2
        assert abs(qfi - 4 * p * conditional_var) < 1e-9 * max(qfi, 1)
        assert abs(mean - p * (conditional_mean - ground)) < 1e-12
        variance = float(np.trace(resource @ h_resource @ h_resource).real) - mean**2
        coherence_indices = np.argwhere(abs(resource) > 1e-14)
        bandwidth = max(abs(resource_energies[i] - resource_energies[j]) for i, j in coherence_indices)
        diameter = float(np.ptp(resource_energies))
        assert abs(bandwidth - (energies[3] - energies[2])) < 1e-12
        # An input in D-perp stays there: this checks the advertised extension, not just one input.
        outside = np.kron(projector(np.eye(6)[4]), np.diag([1, 0]))
        outside_initial = np.kron(outside, resource)
        assert trace_norm(unitary @ outside_initial @ unitary.T - outside_initial) == 0
        row = {'epsilon': epsilon, 'selected_probability': float(np.trace(selected).real),
               'selected_error': error, 'projection_formula_error': exact_error,
               'error_over_epsilon_cubed': error / epsilon**3,
               'global_conservation_residual': float(conservation_residual),
               'apparatus_fisher': qfi, 'scaled_fisher': epsilon**4 * qfi,
               'target_scaled_fisher': 4 * alpha**2 * delta**2 * rcoef,
               'ground_relative_mean': mean, 'target_mean_limit': alpha**2 * delta * rcoef,
               'apparatus_variance': variance,
               'scaled_spectral_diameter': epsilon**4 * diameter,
               'scaled_coherence_bandwidth': epsilon**4 * bandwidth,
               'target_range_coefficient': delta}
        rows.append(row)
    assert abs(rows[-1]['scaled_fisher'] - rows[-1]['target_scaled_fisher']) < abs(rows[0]['scaled_fisher'] - rows[0]['target_scaled_fisher'])
    assert abs(rows[-1]['ground_relative_mean'] - rows[-1]['target_mean_limit']) < abs(rows[0]['ground_relative_mean'] - rows[0]['target_mean_limit'])
    return rows


def main():
    result = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python': sys.version, 'numpy': np.__version__,
              'phase_witness': non_eigenvector_phase_witness(),
              'frequency_support': frequency_support_controls(),
              'restricted_swap': restricted_swap_controls(),
              'scope': 'Independent finite algebra/implementation controls after source release; no author/campaign imports, no microscopic matrix reproduction or numerical proof of a uniform limit.'}
    (HERE / 'POST_OWN_CONTROL_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
