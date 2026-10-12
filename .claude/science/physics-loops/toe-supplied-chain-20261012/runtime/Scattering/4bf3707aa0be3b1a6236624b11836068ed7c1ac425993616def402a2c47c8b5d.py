#!/usr/bin/env python3
"""Independent finite witnesses. No finite suite claims the infinite theorem."""
import argparse
from itertools import combinations, permutations, product
import importlib.util
import json
from math import acos, factorial, pi, sqrt
from pathlib import Path
import sys
import numpy as np


def load(path):
    spec = importlib.util.spec_from_file_location("candidate_under_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def distance(left, right):
    return float(sqrt(sum(abs(left.get(k, 0)-right.get(k, 0))**2
                          for k in set(left) | set(right))))


def pauli_reference(packets):
    """Independent dense tensor product of the actual 2x2 lowering matrix."""
    size = len(packets[0])
    lower = np.array([[0, 0], [1, 0]], dtype=complex)
    matrices = []
    for site in range(size):
        operator = np.array([[1]], dtype=complex)
        for coordinate in reversed(range(size)):
            operator = np.kron(operator, lower if site == coordinate else np.eye(2))
        matrices.append(operator)
    vector = np.zeros(2**size, dtype=complex)
    vector[0] = 1
    for packet in reversed(packets):
        vector = sum(c*m for c, m in zip(packet, matrices)) @ vector
    return {i: value for i, value in enumerate(vector) if value != 0}


def determinant_reference(packets):
    n, size = packets.shape
    return {sum(1 << j for j in sites): np.linalg.det(packets[:, sites])
            for sites in combinations(range(size), n)}


def boson_reference(packets):
    """Ordinary bosonic occupation creators with sqrt(occupation+1)."""
    size = packets.shape[1]
    state = {(0,)*size: 1+0j}
    for packet in reversed(packets):
        new = {}
        for occupation, amplitude in state.items():
            for j, coefficient in enumerate(packet):
                target = list(occupation)
                target[j] += 1
                key = tuple(target)
                new[key] = new.get(key, 0j) + coefficient*sqrt(target[j])*amplitude
        state = new
    return sum(abs(value)**2 for value in state.values())


def energy_reference(k, g, J):
    return 2*np.hypot(g-J*np.cos(k), J*np.sin(k))


def bump(k, center, width):
    z = (k-center)/width
    result = np.zeros_like(z, dtype=float)
    inside = np.abs(z) < 1
    result[inside] = np.exp(-1/(1-z[inside]**2))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    C = load(args.candidate)
    rows = []
    def row(name, value, tolerance, **details):
        value = float(value)
        rows.append({"name": name, "error": value, "tolerance": tolerance,
                     "pass": bool(np.isfinite(value) and value <= tolerance), **details})

    rng = np.random.default_rng(7102026)
    for n in range(1, 5):
        packets = (rng.normal(size=(n, 6))+1j*rng.normal(size=(n, 6)))/3
        spin = C.spin_product(packets)
        row(f"literal_pauli_n{n}", distance(spin, pauli_reference(packets)), 2e-12,
            sites=6, particles=n, comparison="dense 2x2 Pauli tensor products")
        row(f"car_determinant_n{n}", distance(C.car_product(packets), determinant_reference(packets)), 2e-12,
            sites=6, particles=n, comparison="independent determinant minors")
    for n in range(1, 8):
        for direction in (1, -1):
            packets = np.zeros((n, 2*n), dtype=complex)
            for i in range(n):
                place = i if direction > 0 else n-1-i
                packets[i, 2*place:2*place+2] = [1+0.07j*(i+1), 0.4-0.13j*(i+1)]
            spin, car = C.spin_product(packets), C.car_product(packets)
            predicted = {key: C.cone_sign(n, direction)*value for key, value in car.items()}
            row(f"cone_identity_n{n}_t{direction:+d}", distance(spin, predicted), 2e-12,
                particles=n, exact_spatial_supports=True)
            ordering = tuple(range(n)) if direction > 0 else tuple(reversed(range(n)))
            inversions = sum(ordering[i] > ordering[j] for i in range(n) for j in range(i+1, n))
            row(f"incoming_phase_n{n}_t{direction:+d}", abs(C.cone_sign(n, direction)-(-1)**inversions), 0,
                reference_inversions=inversions)
    collision = np.array([[1+2j, 0], [0.3-0.1j, 0]])
    row("hardcore_same_site", distance(C.spin_product(collision), {}), 0,
        reason="actual S_minus squared is zero; disjoint cones alone cannot discriminate this mutation")

    for n in (2, 3, 4):
        points = 4
        packets = (rng.normal(size=(n, points))+1j*rng.normal(size=(n, points)))/2
        norms = [0., 0.]
        for tuple_indices in product(range(points), repeat=n):
            matrix = packets[:, tuple_indices]
            for antisymmetric in (False, True):
                value = C.wavefunction(matrix, antisymmetric)
                norms[int(antisymmetric)] += abs(value)**2 / points**n
        expected_bose = boson_reference(packets/sqrt(points))
        expected_fermi = float(np.linalg.det(packets @ packets.conj().T / points).real)
        row(f"symmetric_normalization_n{n}", abs(norms[0]-expected_bose), 3e-11,
            norm_squared=norms[0], reference_norm_squared=expected_bose,
            comparison="occupation-basis creation with sqrt(n+1)")
        row(f"antisymmetric_normalization_n{n}", abs(norms[1]-expected_fermi), 3e-11,
            norm_squared=norms[1], reference_norm_squared=expected_fermi,
            comparison="Gram determinant")

    g, J = 2.3, 0.7
    for speed in (0.55, 0.95, 1.25):
        discriminant = sqrt((4*g*g-speed*speed)*(4*J*J-speed*speed))
        momenta = np.array([acos((speed*speed+sign*discriminant)/(4*g*J)) for sign in (1, -1)])
        row(f"two_velocity_branches_{speed}", np.max(np.abs(C.velocity(momenta, g, J)-speed)), 2e-14,
            momenta=momenta.tolist(), speeds=C.velocity(momenta, g, J).tolist(), critical_momentum=acos(J/g))
        for j, k in enumerate(momenta):
            row(f"one_particle_branch_{speed}_{j}", abs(C.out_coordinate(0.4+0.9j, [k], g, J)-(0.4+0.9j)), 2e-14,
                momentum=float(k), branch=j)
    for k in (-2.7, -0.4, 0.2, 1.1, 2.6):
        step = 2e-5
        derivative = (energy_reference(k-2*step, g, J)-8*energy_reference(k-step, g, J)
                      +8*energy_reference(k+step, g, J)-energy_reference(k+2*step, g, J))/(12*step)
        row(f"velocity_derivative_{k}", abs(C.velocity(k, g, J)-derivative), 2e-10,
            comparison="five-point derivative of independent hypot energy")
    for n in (2, 3, 4):
        momenta = np.array([-0.7, 2.6, 0.8, -2.8][:n])
        # Reference velocity order uses an independent derivative, not candidate.velocity.
        h = 1e-6
        reference_speeds = (energy_reference(momenta+h, g, J)-energy_reference(momenta-h, g, J))/(2*h)
        order = np.argsort(reference_speeds)
        sorted_momenta = momenta[order]
        amplitudes = (1+0.2j*np.arange(1, n+1))*np.linspace(0.7, 1.2, n)
        diagonal = np.diag(amplitudes)
        maximum = 0.
        mapped_norm = 0.
        source_norm = 0.
        for perm in permutations(range(n)):
            matrix = diagonal[:, perm]
            symmetric = C.wavefunction(matrix, False)
            antisymmetric_reference = np.linalg.det(matrix)/sqrt(factorial(n))
            mapped = C.out_coordinate(symmetric, sorted_momenta[list(perm)], g, J)
            maximum = max(maximum, abs(mapped-antisymmetric_reference))
            mapped_norm += abs(mapped)**2
            source_norm += abs(symmetric)**2
        row(f"velocity_sorting_map_n{n}", maximum, 3e-13,
            momenta_in_velocity_order=sorted_momenta.tolist(), comparison="determinant and derivative ordering")
        row(f"velocity_map_norm_n{n}", abs(mapped_norm-source_norm), 3e-13,
            source_norm_squared=source_norm, target_norm_squared=mapped_norm)

    grid_size = 8192
    k = -pi+2*pi*np.arange(grid_size)/grid_size
    centers, width = (-0.82, 0.64), 0.24
    samples = [bump(k, center, width) for center in centers]
    normalizations = [sqrt(np.mean(abs(f)**2)) for f in samples]
    samples = [f/a for f, a in zip(samples, normalizations)]
    # Independent Gauss integration on each packet's actual support, not the FFT grid.
    nodes, weights = np.polynomial.legendre.leggauss(320)
    reference_nodes, reference_weights = [], []
    for center, normalization in zip(centers, normalizations):
        q = center+width*nodes
        reference_nodes.append(q)
        reference_weights.append(width*weights*bump(q, center, width)/(2*pi*normalization))
    for direction in (1, -1):
        sites = np.array([-37, -4, 0, 9, 41])
        time = direction*19.5
        for i in range(2):
            q = reference_nodes[i]
            reference = np.exp(1j*(np.outer(sites, q)-time*energy_reference(q, g, J))) @ reference_weights[i]
            value = C.packet_coefficients(samples[i], k, g, J, time, sites)
            row(f"fourier_gauss_packet{i}_t{direction:+d}", np.max(np.abs(value-reference)), 2e-11,
                sites=sites.tolist(), time=time, comparison="Gauss-Legendre oscillatory integral on packet support")
    for direction in (1, -1):
        for magnitude in (8, 16, 32, 64, 128):
            time = direction*magnitude
            radius = int(2*J*magnitude+190)
            sites = np.arange(-radius, radius+1)
            packets = [C.packet_coefficients(f, k, g, J, time, sites) for f in samples]
            sign = C.cone_sign(2, time)
            error = C.pair_error(*packets, sign)
            u, w = (abs(packet)**2 for packet in packets)
            if sign == 1:
                expected_squared = 4*np.sum(w*np.concatenate((np.cumsum(u[:0:-1])[::-1], [0])))
            else:
                expected_squared = 4*np.sum(u*np.concatenate((np.cumsum(w[:0:-1])[::-1], [0])))
            expected = sqrt(max(0., expected_squared))
            row(f"pair_error_identity_t{time:+d}", abs(error-expected), 2e-10,
                spin_car_vector_error=error, cumulative_reference=expected, sites=len(sites))
            norms = [float(np.sum(abs(packet)**2)) for packet in packets]
            row(f"packet_window_norm_t{time:+d}", max(abs(1-value) for value in norms), 2e-7,
                captured_norm_squared=norms, radius=radius)
            if magnitude == 128:
                row(f"separated_pair_limit_fixture_t{time:+d}", error, 0.01,
                    disclaimer="One finite-time fixture; the all-time and all-n theorem is analytic.")
    dense_k = -pi+2*pi*np.arange(2*grid_size)/(2*grid_size)
    sites = np.arange(-400, 401)
    for i, center in enumerate(centers):
        dense_f = bump(dense_k, center, width)/normalizations[i]
        coarse = C.packet_coefficients(samples[i], k, g, J, 128, sites)
        fine = C.packet_coefficients(dense_f, dense_k, g, J, 128, sites)
        row(f"fourier_grid_doubling_packet{i}", np.max(np.abs(fine-coarse)), 2e-11,
            grid_sizes=[grid_size, 2*grid_size], sites=len(sites))

    # Direct actual-character quadrature of a known Schwartz kernel.
    # Gaussian is deliberately only a Fourier-clock control, not the compact-support proof.
    nodes, weights = np.polynomial.legendre.leggauss(640)
    time_nodes, time_weights = 24*nodes, 24*weights
    center, spread = 4.1, 0.45
    energy_kernel = spread/sqrt(2*pi)*np.exp(-spread*spread*time_nodes*time_nodes/2-1j*center*time_nodes)
    spatial_kernel = {-1: 0.115+0.085j, 0: 1, 1: 0.115-0.085j}
    def transform(e, momentum):
        return np.exp(-(e-center)**2/(2*spread*spread))*(1+0.23*np.cos(momentum)-0.17*np.sin(momentum))
    for momentum in (-2.1, -0.7, 0.35, 1.8):
        energy = energy_reference(momentum, g, J)
        actual_character = sum(value*np.exp(-1j*x*momentum) for x, value in spatial_kernel.items())
        reference = np.dot(time_weights, energy_kernel*np.exp(1j*time_nodes*energy))*actual_character
        value = C.filter_vacuum(momentum, g, J, transform)
        row(f"filter_actual_character_{momentum}", abs(value-reference), 2e-12,
            reference_real=float(reference.real), reference_imag=float(reference.imag), candidate_real=float(np.real(value)),
            comparison="continuous time quadrature and literal integer spatial character")

    result = {"candidate": str(args.candidate.resolve()), "rows": rows,
              "passed": sum(r["pass"] for r in rows), "failed": sum(not r["pass"] for r in rows),
              "scope": "Finite different-method witnesses only. Infinity, density, AL, Arveson support and completeness are analytic obligations."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
    return 0 if result["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
