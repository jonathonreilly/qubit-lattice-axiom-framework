#!/usr/bin/env python3
"""Finite author controls; no claim to prove the analytic scattering theorem.

No predecessor control code or output is imported. Exact free-word algebra,
exact lattice shell sums, and concrete matrix clock calculations are separate
routes to their finite targets. The author's proof and root lead were visible.
"""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/NONISOLATED_FOCK_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/NONISOLATED_MASS_SCATTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    ".claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import json
import numpy as np


def report(name, **data):
    print(json.dumps({"check": name, **data}, sort_keys=True))


def add(*terms):
    result = defaultdict(int)
    for term in terms:
        for word, value in term.items():
            result[word] += value
    return {word: value for word, value in result.items() if value}


def scale(poly, factor):
    return {word: factor * value for word, value in poly.items() if factor * value}


def mul(*polys):
    result = {(): 1}
    for poly in polys:
        nxt = defaultdict(int)
        for u, a in result.items():
            for v, b in poly.items():
                nxt[u + v] += a * b
        result = {word: value for word, value in nxt.items() if value}
    return result


def bracket(a, b):
    return add(mul(a, b), scale(mul(b, a), -1))


def free_word_control():
    cases = []
    a = {("a",): 1}
    for n in range(1, 10):
        xs = [{(f"x{j}",): 1} for j in range(n)]
        terminal = mul(*xs, a)
        singles, doubles = [], []
        for k in range(n):
            singles.append(mul(*(xs[j] for j in range(n) if j != k), bracket(a, xs[k])))
            for ell in range(k + 1, n):
                doubles.append(mul(*(xs[j] for j in range(ell) if j != k),
                                   bracket(bracket(a, xs[k]), xs[ell]), *xs[ell + 1:]))
        lhs = mul(a, *xs)
        rhs = add(terminal, *singles, *doubles)
        assert lhs == rhs
        no_double = add(terminal, *singles)
        mutation_rejected = n == 1 or lhs != no_double
        assert mutation_rejected
        if n >= 2:
            omit_one = add(rhs, scale(doubles[-1], -1))
            assert lhs != omit_one
        cases.append({"n": n, "single_terms": len(singles), "double_terms": len(doubles),
                      "right_spectators_per_double": max(0, n - 2),
                      "omit_all_doubles_rejected": n >= 2})
    report("full_noncommutative_gram_identity", status="pass", cases=cases,
           limit="Exact free-word identity before vacuum, clustering, or asymptotic replacement.")


def moment_half(k):
    # M_k=sum_{j>=0}j^k 2^-j. Shift the summation index to derive this recursion.
    values = [2]
    for power in range(1, k + 1):
        values.append(sum(comb(power, h) * values[h] for h in range(power)))
    return values[k]


def weighted_shell_tail(d, start):
    # sum_{r=start}^infty ((2r+1)^d-(2r-1)^d) 2^-(r-start).
    total = 0
    for odd in range(1, d + 1, 2):
        power = d - odd
        coefficient = 2 * comb(d, odd) * 2 ** power
        shifted_moment = sum(comb(power, h) * start ** (power - h) * moment_half(h)
                             for h in range(power + 1))
        total += coefficient * shifted_moment
    return total


def middle_sum(d, radius, capped=True):
    amplitude = (radius + 1) ** d
    if capped:
        cap_radius = 6 * radius + amplitude.bit_length() - 1
        start = cap_radius + 1
        return Fraction((2 * cap_radius + 1) ** d) + Fraction(
            amplitude * weighted_shell_tail(d, start), 2 ** (start - 6 * radius))
    start = 6 * radius + 1
    return amplitude * (Fraction((12 * radius + 1) ** d) +
                        Fraction(weighted_shell_tail(d, start), 2))


def lattice_count_control():
    # Actual set enumeration checks the support-distance inequality, independently
    # of the shell-polynomial route used for the infinite majorant sum.
    wrong_padding_witness = None
    geometric_cases = 0
    for radius in (1, 2, 3):
        for a, c, b in product(range(-2 * radius, 2 * radius + 1),
                               range(-2 * radius, 2 * radius + 1),
                               range(-10 * radius, 10 * radius + 1)):
            left = set(range(-radius, radius + 1)) | set(range(a - radius, a + radius + 1))
            right = set(range(b - radius, b + radius + 1)) | set(range(b + c - radius, b + c + radius + 1))
            distance = min(abs(x - y) for x in left for y in right)
            assert distance >= max(0, abs(b) - 6 * radius)
            if distance < max(0, abs(b) - 2 * radius) and wrong_padding_witness is None:
                wrong_padding_witness = dict(R=radius, a=a, b=b, c=c, distance=distance,
                                             false_lower_bound=max(0, abs(b) - 2 * radius))
            geometric_cases += 1
    assert wrong_padding_witness is not None
    rows = []
    for d in range(1, 5):
        for radius in (1, 2, 4, 8, 16, 32):
            exact = middle_sum(d, radius)
            # Independently sum 40 shells beyond the cap and add the exact
            # residual tail, checking the closed formula without truncation.
            amplitude = (radius + 1) ** d
            cutoff = 6 * radius + amplitude.bit_length() + 40
            finite = Fraction(1)
            for r in range(1, cutoff + 1):
                shell = (2 * r + 1) ** d - (2 * r - 1) ** d
                weight = min(Fraction(1), Fraction(amplitude, 2 ** max(0, r - 6 * radius)))
                finite += shell * weight
            residual = Fraction(amplitude * weighted_shell_tail(d, cutoff + 1),
                                2 ** (cutoff + 1 - 6 * radius))
            assert finite + residual == exact
            pair_counts = (4 * radius + 1) ** (2 * d)
            full = pair_counts * exact
            uncapped = pair_counts * middle_sum(d, radius, capped=False)
            assert uncapped > full
            rows.append({"d": d, "R": radius, "three_relative_sum_exact": str(full),
                         "sum_over_R_3d": float(full / radius ** (3 * d)),
                         "uncapped_over_capped": float(uncapped / full)})
    report("local_support_and_infinite_lattice_majorant", status="pass",
           geometric_cases=geometric_cases, wrong_padding_witness=wrong_padding_witness,
           rows=rows,
           limit="Exact exponential-2 lattice majorant and finite one-dimensional support checks; general clustering and all-R power bound are analytic NF14-NF19.")


def dagger(a):
    return a.conjugate().T


def comm(a, b):
    return a @ b - b @ a


def matrix_clock_control():
    identity = np.eye(2, dtype=complex)
    raising = np.array([[0, 0], [1, 0]], dtype=complex)
    n = dagger(raising) @ raising
    # Number projector on the excited state in the basis |0>,|1>.
    n = raising @ dagger(raising)
    s0, s1 = np.kron(raising, identity), np.kron(identity, raising)
    n0, n1 = np.kron(n, identity), np.kron(identity, n)
    hamiltonian = 3 * (n0 + n1) + 0.4 * (s0 @ dagger(s1) + s1 @ dagger(s0)) + 0.6 * n0 @ n1
    energies, eigenvectors = np.linalg.eigh(hamiltonian)
    omega = np.array([1, 0, 0, 0], dtype=complex)
    perpendicular = np.eye(4) - np.outer(omega, omega.conjugate())
    shift = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    seeds = [s0 + 0.3 * s0 @ s1, s1 + 0.7j * s0 @ s1, s0 + 0.2 * s1 + 0.5 * s0 @ s1]
    masses = [2.1, 1.7, 2.4]
    amplitudes = [np.array([1.0, 0.4 + 0.3j]), np.array([0.6 - 0.2j, 0.9]), np.array([0.7, -0.2 + 0.6j])]
    transfer_ranges = []
    for seed in seeds:
        matrix = dagger(eigenvectors) @ seed @ eigenvectors
        transfers = [float(energies[i] - energies[j]) for i in range(4) for j in range(4)
                     if abs(matrix[i, j]) > 1e-12]
        assert min(transfers) > 0
        transfer_ranges.append([min(transfers), max(transfers)])

    def evolved(seed, t):
        unitary = (eigenvectors * np.exp(1j * t * energies)) @ dagger(eigenvectors)
        return unitary @ seed @ dagger(unitary)

    def packet(which, t):
        p = np.array([0.0, np.pi])
        dispersion = np.sqrt(masses[which] ** 2 + 0.6 * p ** 2)
        coefficients = [np.sum(amplitudes[which] * np.exp(1j * p * x - 1j * t * dispersion)) / 2
                        for x in (0, 1)]
        return coefficients[0] * evolved(seeds[which], t) + coefficients[1] * evolved(shift @ seeds[which] @ shift, t)

    times = [np.array([0.2, 0.8, 1.7]), np.array([-0.4, 0.5, 1.4, 2.2]), np.array([-0.2, 0.7, 2.0])]
    weights = [np.array([0.2 + 0.1j, 0.5 - 0.15j, 0.3 + 0.05j]),
               np.array([0.1 - 0.05j, 0.25 + 0.1j, 0.4 - 0.02j, 0.25 - 0.03j]),
               np.array([0.25 + 0.03j, 0.35 - 0.08j, 0.4 + 0.05j])]
    arrays = [[packet(which, float(t)) for t in times[which]] for which in range(3)]
    averages = [sum(w * c for w, c in zip(weights[which], arrays[which])) for which in range(3)]
    assert all(abs(sum(w) - 1) < 1e-14 for w in weights)
    assert all(np.linalg.norm(dagger(a) @ omega) < 1e-14 for a in averages)
    a, b, y = averages
    residual = perpendicular @ dagger(a) @ b @ omega
    norm_squared = float(np.vdot(residual, residual).real)
    full_integral = 0j
    tied_integral = 0j
    for i, j, k, ell in product(range(len(arrays[0])), range(len(arrays[1])),
                               range(len(arrays[0])), range(len(arrays[1]))):
        coefficient = weights[0][i] * weights[1][j].conjugate() * weights[0][k].conjugate() * weights[1][ell]
        left = comm(dagger(arrays[1][j]), arrays[0][i])
        right = comm(dagger(arrays[0][k]), arrays[1][ell])
        full_integral += coefficient * np.vdot(omega, left @ perpendicular @ right @ omega)
        tied_right = comm(dagger(arrays[0][i]), arrays[1][j])
        tied_integral += coefficient * np.vdot(omega, left @ perpendicular @ tied_right @ omega)
    common = perpendicular @ dagger(packet(0, 1.0)) @ packet(1, 1.0) @ omega
    common_clock_value = float(np.vdot(common, common).real)
    without_projection = dagger(a) @ b @ omega
    without_projection_value = float(np.vdot(without_projection, without_projection).real)
    assert norm_squared > 1e-8
    assert abs(full_integral - norm_squared) < 1e-12
    assert abs(tied_integral - norm_squared) > 1e-5
    assert abs(common_clock_value - norm_squared) > 1e-5
    assert abs(without_projection_value - norm_squared) > 1e-5

    triple = np.zeros((4, 4), dtype=complex)
    for i, j, k in product(range(len(arrays[0])), range(len(arrays[1])), range(len(arrays[2]))):
        triple += weights[0][i].conjugate() * weights[1][j] * weights[2][k] * comm(comm(dagger(arrays[0][i]), arrays[1][j]), arrays[2][k])
    direct = comm(comm(dagger(a), b), y)
    jacobi = comm(dagger(a), comm(b, y)) - comm(b, comm(dagger(a), y))
    wrong_sign = comm(dagger(a), comm(b, y)) + comm(b, comm(dagger(a), y))
    assert np.linalg.norm(triple - direct) < 1e-12
    assert np.linalg.norm(jacobi - direct) < 1e-12
    assert np.linalg.norm(wrong_sign - direct) > 1e-5
    report("four_independent_clocks_and_connected_projection", status="pass",
           energies=energies.tolist(), transfer_ranges=transfer_ranges,
           target_norm_squared=norm_squared,
           quadruple_integral_real=float(full_integral.real), quadruple_integral_imag=float(full_integral.imag),
           tied_clock_mutation_error=float(abs(tied_integral - norm_squared)),
           common_clock_mutation_error=abs(common_clock_value - norm_squared),
           omitted_Pperp_mutation_error=abs(without_projection_value - norm_squared),
           triple_integral_error=float(np.linalg.norm(triple - direct)),
           jacobi_error=float(np.linalg.norm(jacobi - direct)),
           jacobi_sign_mutation_error=float(np.linalg.norm(wrong_sign - direct)),
           limit="Finite two-site positive-transfer model with discrete clock weights; checks exact identities, not asymptotic locality or nonisolated scattering.")

    # The same non-exact vacuum creators test the imported finite-energy padding.
    seed = seeds[0]
    translated_sum = seed @ dagger(seed) + shift @ seed @ dagger(seed) @ shift
    epsilon, upper = transfer_ranges[0]
    sb = np.linalg.norm(comm(dagger(seed), seed), 2) + np.linalg.norm(comm(dagger(seed), shift @ seed @ shift), 2)
    f2 = float(np.linalg.norm(amplitudes[0]) / np.sqrt(2))
    energy_cases = []

    def projection(ceiling):
        keep = (energies <= ceiling + 1e-12).astype(float)
        return (eigenvectors * keep) @ dagger(eigenvectors)

    def gamma(ceiling):
        p = projection(ceiling)
        return float(np.linalg.norm(p @ translated_sum @ p, 2))

    for cutoff in (0.0, 2.6, 3.4, 6.6):
        p = projection(cutoff)
        creator_bound = sum(abs(weights[0])) * f2 * np.sqrt(gamma(cutoff + upper))
        annihilator_bound = sum(abs(weights[0])) * f2 * np.sqrt(gamma(cutoff))
        creator_norm, annihilator_norm = np.linalg.norm(a @ p, 2), np.linalg.norm(dagger(a) @ p, 2)
        assert creator_norm <= creator_bound + 1e-11
        assert annihilator_norm <= annihilator_bound + 1e-11
        # Avoid flooring binary floating point at an exact endpoint.
        energy_count = int(np.floor(cutoff / epsilon + 1e-11))
        assert gamma(cutoff) <= energy_count * sb + 1e-11
        energy_cases.append({"ceiling": cutoff, "creator_norm": float(creator_norm),
                             "creator_bound": float(creator_bound), "annihilator_norm": float(annihilator_norm),
                             "annihilator_bound": float(annihilator_bound)})
    missing_padding_bound = sum(abs(weights[0])) * f2 * np.sqrt(gamma(0))
    assert np.linalg.norm(a @ omega) > missing_padding_bound + 1e-5
    report("finite_energy_bound_with_nonexact_vacuum_creators", status="pass", cases=energy_cases,
           omitted_padding_bound=float(missing_padding_bound), creator_on_vacuum=float(np.linalg.norm(a @ omega)),
           limit="Finite matrix support/Parseval control; the full mixed-word infinite-volume proof is the reviewed N15-N19 argument.")


def width_control():
    small, kappa = Fraction(1, 16), Fraction(1, 8)
    rows = []
    for d in range(1, 7):
        for exponent in [Fraction(1, 100), Fraction(1, 2), Fraction(1), Fraction(3), Fraction(100)]:
            reference = (1 + 1 / (1 + exponent)) / 2
            assert reference * (1 + exponent) > 1
            assert 0 < small < kappa < Fraction(1, 3)
            target_decay = d * (1 - 3 * kappa)
            target_order = 3
            delta = kappa - small
            locality_order = int((2 * d + target_order) / kappa) + 1
            tail_order = int((2 * d + target_order) / delta) + 1
            assert 2 * d - kappa * locality_order < -target_order
            assert 2 * d - delta * tail_order < -target_order
            assert target_decay > 0
            rows.append({"d": d, "regularity_a": str(exponent), "reference_nu": str(reference),
                         "small_width_direct_Cook_integrable": small * (1 + exponent) > 1,
                         "squared_contraction_decay": str(target_decay),
                         "locality_order_for_O_Tminus3": locality_order,
                         "tail_order_for_O_Tminus3": tail_order})
    assert 1 - 3 * Fraction(1, 3) == 0
    assert 1 - 3 * Fraction(1, 2) < 0
    report("width_and_all_tail_bookkeeping", status="pass", small_nu=str(small), kappa=str(kappa), cases=rows,
           limit="Exact rational sufficient-exponent accounting; neither finite arithmetic nor a failed bound establishes necessity.")


if __name__ == "__main__":
    report("environment", numpy_version=np.__version__)
    free_word_control()
    lattice_count_control()
    matrix_clock_control()
    width_control()
    report("completion", status="complete", independent_review=False,
           scope="Author finite algebra, support-counting and exponent controls only.")
    print('per_element: exact free-word and finite covariance identities are checked; the analytic contraction proof remains separate.')
    print('per_site: finite support geometry and exact rational lattice sums are checked; general exponent gates have documented survivors.')
    print('per_mode: finite four-clock and energy-window fixtures are checked; no nonisolated infinite-lattice particle model is constructed.')
    print('per_block: finite spectator and width bookkeeping is checked; one completed driver is not a predicate count or proof grade.')
    print('lattice_wide: checked and not executed — Fock isometry and density in the defined regular space use the conditional analytic proof.')
    print("TOTAL: PASS=1 FAIL=0")
    print('SCOPE: Original finite controls only; documented mutation survivors and insensitive rows remain. Counts do not prove the analytic theorem or a physical model. TOTAL counts one completed assertion-guarded driver.')
