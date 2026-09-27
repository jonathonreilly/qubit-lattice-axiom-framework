#!/usr/bin/env python3
"""Check the exact ground-state rate transform from physical hop enumeration.

This runner checks an algebraic identity under the supplied finite-spin model.
It does not estimate long-time propagation or the fixed-time electric scalar.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from pathlib import Path
import subprocess

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INPUTS = (
    ROOT / "scripts/core_derivation.py",
    ROOT / "scripts/postmark_electric_five_site_inter_fiber_phase_2026_09_24.py",
    ROOT / "docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
SPINS = (1, 2, 3, 5, 8, 12, 20, 32)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


physical = load_module(INPUTS[0], "physical_hop_model")
labels = load_module(INPUTS[1], "supplied_casimir_labels")


def direct_staggered_matrix(spin: int):
    """Rebuild N=J(-H2)J from the physical legal-hop enumeration."""
    lo, hi = -5 * spin, 5 * spin - 4
    nodes = tuple(range(lo, hi + 1))
    path = physical.walk_nodes(5 * spin)
    if any(n not in path for n in nodes):
        raise ArithmeticError(("missing finite-spin path node", spin))
    inverse = {path[n]: n for n in nodes}
    position = {n: i for i, n in enumerate(nodes)}
    size = len(nodes)
    M = np.zeros((size, size), dtype=np.float64)
    for n in nodes:
        i = position[n]
        h2_row = physical.finite_spin_h2(path[n], spin)
        for state, amplitude in h2_row.items():
            target = inverse.get(state)
            if target is not None:
                M[i, position[target]] = -float(amplitude)
    J = np.array([(-1.0) ** n for n in nodes])
    N = J[:, None] * M * J[None, :]
    return nodes, N


def positive_ground_profile(nodes, spin: int):
    """Use the exact A-row null recurrence, normalized in ordinary l2."""
    lo, hi = nodes[0], nodes[-1]
    C = spin * (spin + 1)
    h = np.ones(len(nodes), dtype=np.float64)
    zero = -lo

    def weight(m: int) -> float:
        return 1.0 - labels.f(m) / C

    for n in range(0, hi):
        ml, mr = labels.edge_labels(n)
        left, right = weight(ml), weight(mr)
        if left <= 0.0 or right <= 0.0:
            raise ArithmeticError(("nonpositive in-domain edge", spin, n, left, right))
        h[n + 1 - lo] = h[n - lo] * math.sqrt(left / right)
    for n in range(-1, lo - 1, -1):
        ml, mr = labels.edge_labels(n)
        left, right = weight(ml), weight(mr)
        if left <= 0.0 or right <= 0.0:
            raise ArithmeticError(("nonpositive in-domain edge", spin, n, left, right))
        h[n - lo] = h[n + 1 - lo] * math.sqrt(right / left)
    norm = float(np.linalg.norm(h))
    return h / norm


def check_operator_identity(spin: int) -> dict:
    nodes, N = direct_staggered_matrix(spin)
    lo, hi = nodes[0], nodes[-1]
    profile = positive_ground_profile(nodes, spin)
    rng = np.random.default_rng(20260926 + spin)
    f = rng.normal(size=len(nodes)) + 1j * rng.normal(size=len(nodes))
    direct = (N @ (profile * f)) / profile
    predicted = np.zeros(len(nodes), dtype=np.complex128)
    C = spin * (spin + 1)
    pi = profile * profile
    max_balance_error = 0.0
    rates_plus = np.zeros(len(nodes), dtype=np.float64)
    for i, n in enumerate(nodes):
        if n < hi:
            ml, _mr = labels.edge_labels(n)
            rplus = 1.0 - labels.f(ml) / C
            rates_plus[i] = rplus
            predicted[i] += rplus * (f[i] - f[i + 1])
            _next_left, next_right = labels.edge_labels(n)
            balance = pi[i] * rplus - pi[i + 1] * (1.0 - labels.f(next_right) / C)
            max_balance_error = max(max_balance_error, float(abs(balance)))
        if n > lo:
            _prev_left, prev_right = labels.edge_labels(n - 1)
            rminus = 1.0 - labels.f(prev_right) / C
            predicted[i] += rminus * (f[i] - f[i - 1])
    max_operator_error = float(np.max(np.abs(direct - predicted)))
    zero_mode_error = float(np.max(np.abs(N @ profile)))
    hermitian_error = float(np.max(np.abs(N - N.T)))
    eigenvalues, eigenvectors = np.linalg.eigh(N)
    max_transfer_relative_error = 0.0
    for mode_index, eigenvalue in enumerate(eigenvalues):
        mode = eigenvectors[:, mode_index] / profile
        scale = max(1.0, float(np.max(np.abs(mode))))
        previous_flux = 0.0
        for i in range(len(nodes) - 1):
            conductance = pi[i] * rates_plus[i]
            current_flux = previous_flux - eigenvalue * pi[i] * mode[i]
            next_value = mode[i] + current_flux / conductance
            max_transfer_relative_error = max(
                max_transfer_relative_error,
                float(abs(next_value - mode[i + 1]) / scale))
            previous_flux = current_flux
        endpoint_residual = abs(
            previous_flux - eigenvalue * pi[-1] * mode[-1]) / scale
        max_transfer_relative_error = max(
            max_transfer_relative_error, float(endpoint_residual))
    if max_operator_error > 2e-11 or zero_mode_error > 2e-11:
        raise ArithmeticError(("ground-state rate identity", spin, max_operator_error,
                               zero_mode_error))
    if max_balance_error > 2e-12 or hermitian_error > 2e-12:
        raise ArithmeticError(("detailed balance or symmetry", spin,
                               max_balance_error, hermitian_error))
    if max_transfer_relative_error > 2e-8:
        raise ArithmeticError(("determinant-one edge transfer", spin,
                               max_transfer_relative_error))
    return {
        "spin": spin,
        "dimension": len(nodes),
        "max_operator_identity_error": max_operator_error,
        "max_zero_mode_error": zero_mode_error,
        "max_detailed_balance_error": max_balance_error,
        "max_hermitian_error": hermitian_error,
        "max_edge_transfer_relative_error": max_transfer_relative_error,
        "minimum_normalized_ground_weight": float(np.min(pi)),
    }


def check_degree_one_cell_polynomial_obstruction() -> dict:
    """Reject only the simplest formal scalar-cell polynomial ansatz."""
    h, C, E = sp.symbols("h C E", real=True)
    c = sp.symbols("c0:5", real=True)
    left_offsets = (0, 1, 0, 1, 1)
    previous_right_offsets = (-1, 0, 0, 0, 1)
    F = [h + c[s] for s in range(5)]
    residuals = []
    for s in range(5):
        up_shift = 1 if s == 4 else 0
        down_shift = -1 if s == 0 else 0
        up = F[(s + 1) % 5].subs(h, h + up_shift)
        down = F[(s - 1) % 5].subs(h, h + down_shift)
        rplus = C - (h + left_offsets[s]) * (h + left_offsets[s] + 1)
        rminus = C - (h + previous_right_offsets[s]) * (h + previous_right_offsets[s] + 1)
        residuals.append(sp.Poly(sp.expand(rplus * (F[s] - up) +
                                           rminus * (F[s] - down) - E * F[s]), h))
    h2 = [p.coeff_monomial(h**2) for p in residuals]
    h1 = [p.coeff_monomial(h) for p in residuals]
    h2_solutions = sp.linsolve(h2, c)
    if not h2_solutions:
        raise ArithmeticError("unexpected failure in degree-one h^2 system")
    h2_tuple = next(iter(h2_solutions))
    h1_reduced = [sp.simplify(q.subs(dict(zip(c, h2_tuple)))) for q in h1]
    # The s=0 equation forces E=2/5; s=2 forces E=0.
    if sp.solve(h1_reduced[0], E) != [sp.Rational(2, 5)]:
        raise ArithmeticError(("unexpected residue-0 constraint", h1_reduced[0]))
    if sp.solve(h1_reduced[2], E) != [sp.Integer(0)]:
        raise ArithmeticError(("unexpected residue-2 constraint", h1_reduced[2]))
    return {
        "cell_offsets_after_h2": [str(sp.simplify(q - h2_tuple[0])) for q in h2_tuple],
        "residue_0_eigenvalue_constraint": "E=2/5",
        "residue_2_eigenvalue_constraint": "E=0",
        "result": "no global F_s(h)=h+c_s eigenfunction ansatz for the formal five-residue recurrence",
        "scope": "rejects only this degree-one scalar-cell polynomial ansatz; not a spectral no-go",
    }


def check_cell_gauge_subprincipal() -> dict:
    """Restore the edge ground-state gauge before reading the cell symbol."""
    u = sp.symbols("u", real=True)
    w = 1 - u**2
    eps = sp.symbols("eps", positive=True)
    h = u / eps
    casimir = (1 + eps) / eps**2

    def normalized_rate(a: int):
        return sp.cancel((casimir - (h + a) * (h + a + 1)) / casimir)

    def first_order(expression):
        return sp.simplify(sp.diff(expression, eps).subs(eps, 0))

    alpha = lambda a: sp.expand(u**2 - u * (2 * a + 1))
    ell = labels.ELL
    rho = labels.RHO
    previous_rho = labels.PREVIOUS_RHO

    def exact_rate_coefficient(a: int):
        return first_order(normalized_rate(a))

    def exact_edge_gauge_coefficient(s: int):
        edge_ratio = sp.cancel(normalized_rate(ell[s]) /
                               normalized_rate(rho[s]))
        # sqrt(1 + eps*d + O(eps^2)) has first coefficient d/2.
        return sp.simplify(first_order(edge_ratio) / 2)

    beta = [sp.Integer(0)]
    for s in range(4):
        beta.append(sp.simplify(beta[-1] +
                                exact_edge_gauge_coefficient(s)))

    internal_links = [
        sp.simplify(exact_rate_coefficient(ell[s]) +
                    w * (beta[s] - beta[s + 1]))
        for s in range(4)
    ]
    wrap_delta = exact_edge_gauge_coefficient(4)
    wrap_link = sp.simplify(exact_rate_coefficient(ell[4]) -
                             w * wrap_delta)
    links = internal_links + [wrap_link]
    expected_links = []
    diagonals = []
    for s in range(5):
        edge_product = sp.cancel(normalized_rate(ell[s]) *
                                 normalized_rate(rho[s]))
        # sqrt(edge_product) starts at w>0, so its first coefficient is
        # the product's first coefficient divided by 2w.
        expected_links.append(sp.simplify(
            first_order(edge_product) / (2 * w)))
        diagonal_rates = (normalized_rate(ell[s]) +
                          normalized_rate(previous_rho[s]))
        diagonals.append(first_order(diagonal_rates))
    if any(sp.simplify(a - b) != 0
           for a, b in zip(links, expected_links)):
        raise ArithmeticError(("ground-state gauge link correction", links,
                               expected_links))
    expected_diagonals = [
        sp.simplify(alpha(ell[s]) + alpha(previous_rho[s]))
        for s in range(5)
    ]
    if any(sp.simplify(a - b) != 0
           for a, b in zip(diagonals, expected_diagonals)):
        raise ArithmeticError(("ground-state gauge diagonal", diagonals,
                               expected_diagonals))
    return {
        "cell_ground_state_coefficients_beta": [str(sp.factor(x))
                                                 for x in beta],
        "gauge_corrected_link_coefficients": [str(sp.factor(x)) for x in links],
        "hermitian_link_coefficients": [str(sp.factor(x))
                                        for x in expected_links],
        "diagonal_coefficients": [str(sp.factor(x)) for x in diagonals],
        "identities_exact": True,
        "validity": "first-subprincipal expansion on compact interior subsets |u|<1",
        "scope": "restores local Hermitian coefficients; proves no global WKB transport, crossing match, or t=1/4 limit",
    }


def check_second_order_non_crossing_band(gamma_shift: float = 0.0) -> dict:
    """Check the local 1/S^2 band coefficient away from cell degeneracies."""
    ell = labels.ELL
    rho = labels.RHO
    previous_rho = labels.PREVIOUS_RHO
    u, k = 0.37, 0.41
    w = 1.0 - u * u
    theta = 5.0 * k
    alpha = lambda a: u * u - u * (2.0 * a + 1.0)
    gamma = lambda a: -(u - a) * (u - a - 1.0) + gamma_shift
    diag1 = np.array([alpha(ell[s]) + alpha(previous_rho[s])
                      for s in range(5)])
    link1 = np.array([(alpha(ell[s]) + alpha(rho[s])) / 2.0
                      for s in range(5)])
    diag2 = np.array([gamma(ell[s]) + gamma(previous_rho[s])
                      for s in range(5)])
    link2 = np.array([
        (gamma(ell[s]) + gamma(rho[s])) / 2.0 -
        (alpha(ell[s]) - alpha(rho[s]))**2 / (8.0 * w)
        for s in range(5)
    ])

    def make_cell(diagonal, links):
        matrix = np.zeros((5, 5), dtype=np.complex128)
        matrix[np.diag_indices(5)] = diagonal
        for s in range(4):
            matrix[s, s + 1] = matrix[s + 1, s] = -links[s]
        matrix[0, 4] = -links[4] * np.exp(-1j * theta)
        matrix[4, 0] = -links[4] * np.exp(1j * theta)
        return matrix

    H0 = make_cell(np.full(5, 2.0 * w), np.full(5, w))
    H1 = make_cell(diag1, link1)
    H2 = make_cell(diag2, link2)
    qs = k + 2.0 * np.pi * np.arange(5) / 5.0
    vectors = [
        np.exp(1j * q * np.arange(5)) / math.sqrt(5.0) for q in qs
    ]
    mus = 2.0 * w - 2.0 * w * np.cos(qs)
    v0 = vectors[0]
    nu1 = float(np.real(np.vdot(v0, H1 @ v0)))
    nu2 = float(np.real(np.vdot(v0, H2 @ v0)))
    mixing_terms = []
    for m in range(1, 5):
        coupling = np.vdot(vectors[m], H1 @ v0)
        term = float(abs(coupling)**2 / (mus[0] - mus[m]))
        mixing_terms.append(term)
        nu2 += term

    rows = []
    for spin in (80, 160, 320, 640, 1280):
        h = u * spin
        C = spin * (spin + 1.0)
        exact_diag = np.array([
            2.0 - ((h + ell[s]) * (h + ell[s] + 1.0) +
                   (h + previous_rho[s]) *
                   (h + previous_rho[s] + 1.0)) / C
            for s in range(5)
        ])
        exact_links = np.array([
            math.sqrt(
                (1.0 - (h + ell[s]) * (h + ell[s] + 1.0) / C) *
                (1.0 - (h + rho[s]) * (h + rho[s] + 1.0) / C))
            for s in range(5)
        ])
        exact = make_cell(exact_diag, exact_links)
        exact_values = np.linalg.eigvalsh(exact)
        prediction = mus[0] + nu1 / spin + nu2 / (spin * spin)
        exact_branch = float(exact_values[np.argmin(np.abs(exact_values -
                                                         prediction))])
        error = abs(exact_branch - prediction)
        rows.append({
            "S": spin,
            "h_over_S": u,
            "k": k,
            "selected_frozen_branch": exact_branch,
            "second_order_prediction": prediction,
            "absolute_error": error,
            "S_cubed_error": spin**3 * error,
        })
    ratios = [
        rows[i]["absolute_error"] / rows[i + 1]["absolute_error"]
        for i in range(len(rows) - 1)
        if rows[i + 1]["absolute_error"] > 0.0
    ]
    if min(ratios[-3:]) < 4.0 or max(ratios[-3:]) > 16.0:
        raise ArithmeticError(("second-order frozen-band convergence ratio",
                               ratios))
    return {
        "u": u,
        "k": k,
        "minimum_principal_band_gap": float(min(
            abs(mus[0] - mus[m]) for m in range(1, 5))),
        "nu1": nu1,
        "nu2": nu2,
        "second_order_band_mixing_terms": mixing_terms,
        "samples": rows,
        "successive_error_ratios": ratios,
        "scope": "one nondegenerate frozen-cell diagnostic; not a uniform WKB or global finite-spin phase estimate",
    }


def check_finite_spectrum_candidate() -> dict:
    """Retest the exact full-spectrum Gegenbauer candidate on finite sentinels."""
    rows = []
    for spin in SPINS:
        _nodes, matrix = direct_staggered_matrix(spin)
        exact = np.linalg.eigvalsh(matrix)
        dimension = len(exact)
        indices = np.arange(dimension, dtype=np.float64)
        candidate = indices * (indices + 5.0) / (25.0 * spin * (spin + 1.0))
        error = np.abs(exact - candidate)
        rows.append({
            "spin": spin,
            "dimension": dimension,
            "first_nonzero_error": float(error[1]),
            "largest_candidate_value": float(candidate[-1]),
            "largest_exact_eigenvalue": float(exact[-1]),
            "max_abs_error": float(np.max(error)),
            "max_error_index": int(np.argmax(error)),
        })
    if rows[-1]["max_abs_error"] < 0.1:
        raise ArithmeticError(("full-spectrum candidate was not rejected",
                               rows[-1]))
    return {
        "candidate": "lambda_j = j(j+5)/(25 S(S+1)), j=0,...,10S-4",
        "purpose": "finite diagnostic rejecting the full-spectrum extension of the fixed-index Gegenbauer eigenvalue formula",
        "rows": rows,
        "scope": "finite double-precision diagnostic only; fixed-index asymptotics remain valid and this rejects only exact full-spectrum identification",
    }


def check_mutation_rejections() -> dict:
    """Keep two narrow mutations that guard the exact rate and band formulas."""
    original_f = labels.f

    def mutated_f(m: int) -> int:
        return original_f(m) + (1 if m == 0 else 0)

    labels.f = mutated_f
    try:
        try:
            check_operator_identity(3)
        except ArithmeticError as error:
            casimir = {
                "mutation": "replace f(0) by f(0)+1 in the effective-Casimir evaluator",
                "gate_result": "rejected",
                "error": str(error),
            }
        else:
            raise ArithmeticError("effective-Casimir mutation escaped the identity gate")
    finally:
        labels.f = original_f

    try:
        check_second_order_non_crossing_band(gamma_shift=0.01)
    except ArithmeticError as error:
        second_order = {
            "mutation": "add 0.01 to every gamma_a coefficient in H2",
            "gate_result": "rejected",
            "error": str(error),
        }
    else:
        raise ArithmeticError("second-order gamma mutation escaped the convergence gate")
    return {
        "effective_casimir": casimir,
        "second_order_band": second_order,
    }


def check_periodic_rate_cell_transfer() -> dict:
    """Match a periodicized rate cell to its twisted Hermitian Bloch block.

    The periodic auxiliary operator is defined by freezing the *site* forward
    and backward rates. In particular, its wrap reverse rate is the backward
    rate at residue zero, PREVIOUS_RHO[0], not the reverse factor on the
    residue-four edge. That distinction is invisible at principal order but
    changes the first subprincipal phase.
    """
    ell, rho, previous = labels.ELL, labels.RHO, labels.PREVIOUS_RHO
    u0, k0 = 0.37, 0.41
    theta = 5.0 * k0
    spins = (80, 160, 320, 640, 1280)

    def rate(offset: int, spin: int) -> float:
        h = u0 * spin
        C = spin * (spin + 1.0)
        return 1.0 - (h + offset) * (h + offset + 1.0) / C

    rows = []
    maximum_transfer_spectral_residual = 0.0
    maximum_transfer_determinant_error = 0.0
    for spin in spins:
        p = np.array([rate(a, spin) for a in ell])
        q = np.array([rate(a, spin) for a in previous])
        q_next = np.roll(q, -1)
        if np.min(p) <= 0.0 or np.min(q) <= 0.0:
            raise ArithmeticError(("nonpositive frozen periodic rate", spin))

        # Detailed balance for the periodic site-rate array. The last update
        # uses q_0, the periodic wrap site's backward rate.
        pi = np.ones(6, dtype=np.float64)
        for s in range(5):
            pi[s + 1] = pi[s] * p[s] / q_next[s]
        gamma = math.sqrt(float(pi[5]))
        conductance = pi[:5] * p

        # Symmetrized periodic operator and its Bloch boundary phase.
        diagonal = p + q
        links = np.sqrt(p * q_next)
        z = np.exp(1j * theta)
        H = np.diag(diagonal.astype(np.complex128))
        for s in range(4):
            H[s, s + 1] = H[s + 1, s] = -links[s]
        H[0, 4] = -links[4] * np.exp(-1j * theta)
        H[4, 0] = -links[4] * np.exp(1j * theta)
        eigenvalues = np.linalg.eigvalsh(H)

        D = np.diag([1.0 / gamma, gamma])
        cell_residual = 0.0
        cell_determinant_error = 0.0
        for eigenvalue in eigenvalues:
            P = np.eye(2)
            for s in range(5):
                M = np.array([
                    [1.0 - eigenvalue / p[s], 1.0 / conductance[s]],
                    [-eigenvalue * pi[s], 1.0],
                ])
                cell_determinant_error = max(
                    cell_determinant_error, abs(float(np.linalg.det(M)) - 1.0))
                P = M @ P
            discriminant = float(np.trace(np.linalg.solve(P, D)))
            cell_residual = max(
                cell_residual,
                abs(discriminant - 2.0 * math.cos(theta)))
        maximum_transfer_spectral_residual = max(
            maximum_transfer_spectral_residual, cell_residual)
        maximum_transfer_determinant_error = max(
            maximum_transfer_determinant_error, cell_determinant_error)
        rows.append({
            "S": spin,
            "u": u0,
            "k": k0,
            "gamma_cell_drift": gamma,
            "five_periodic_block_eigenvalues": [float(x) for x in eigenvalues],
            "max_discriminant_residual_at_block_eigenvalues": cell_residual,
        })

    # Deliberately use the residue-four edge reverse factor at the wrap. The
    # periodic site operator rejects that off-by-one choice at finite S.
    mutation_spin = 320
    p = np.array([rate(a, mutation_spin) for a in ell])
    q = np.array([rate(a, mutation_spin) for a in previous])
    q_next = np.roll(q, -1)
    pi = np.ones(6, dtype=np.float64)
    for s in range(4):
        pi[s + 1] = pi[s] * p[s] / q_next[s]
    gamma_correct = math.sqrt(float(pi[4] * p[4] / q[0]))
    gamma_wrong = math.sqrt(float(pi[4] * p[4] / rate(rho[4], mutation_spin)))
    conductance = pi[:5] * p
    links = np.sqrt(p * q_next)
    diagonal = p + q
    z = np.exp(1j * theta)
    H = np.diag(diagonal.astype(np.complex128))
    for s in range(4):
        H[s, s + 1] = H[s + 1, s] = -links[s]
    H[0, 4] = -links[4] * np.exp(-1j * theta)
    H[4, 0] = -links[4] * np.exp(1j * theta)
    eigenvalues = np.linalg.eigvalsh(H)

    def max_residual_for_gamma(test_gamma: float) -> float:
        Dtest = np.diag([1.0 / test_gamma, test_gamma])
        residual = 0.0
        for eigenvalue in eigenvalues:
            P = np.eye(2)
            for s in range(5):
                M = np.array([
                    [1.0 - eigenvalue / p[s], 1.0 / conductance[s]],
                    [-eigenvalue * pi[s], 1.0],
                ])
                P = M @ P
            residual = max(
                residual,
                abs(float(np.trace(np.linalg.solve(P, Dtest))) -
                    2.0 * math.cos(theta)))
        return residual

    correct_wrap_residual = max_residual_for_gamma(gamma_correct)
    wrong_wrap_residual = max_residual_for_gamma(gamma_wrong)
    if maximum_transfer_spectral_residual > 2e-8:
        raise ArithmeticError(("periodic rate-cell transfer/Bloch mismatch",
                               maximum_transfer_spectral_residual))
    if maximum_transfer_determinant_error > 2e-10:
        raise ArithmeticError(("periodic edge transfer determinant",
                               maximum_transfer_determinant_error))
    if wrong_wrap_residual < 1e-3 or correct_wrap_residual > 2e-8:
        raise ArithmeticError(("wrap-rate mutation was not rejected",
                               correct_wrap_residual, wrong_wrap_residual))

    us, ks = sp.symbols("u k", real=True)
    alpha = lambda a: us**2 - us * (2 * a + 1)
    diagonal1 = [alpha(ell[s]) + alpha(previous[s]) for s in range(5)]
    local_links1 = [(alpha(ell[s]) + alpha(rho[s])) / 2
                    for s in range(5)]
    periodic_links1 = [
        (alpha(ell[s]) + alpha(previous[(s + 1) % 5])) / 2
        for s in range(5)
    ]
    nu1_local = sp.simplify(
        sum(diagonal1) / 5 -
        2 * sp.cos(ks) * sum(local_links1) / 5)
    nu1_periodic = sp.simplify(
        sum(diagonal1) / 5 -
        2 * sp.cos(ks) * sum(periodic_links1) / 5)
    nu1_published = (2 * us**2 * (1 - sp.cos(ks)) +
                     us * (18 * sp.cos(ks) - 16) / 5)
    if sp.simplify(nu1_local - nu1_published) != 0:
        raise ArithmeticError(("local first-order symbol identity", nu1_local))
    expected_periodic = sp.simplify(nu1_published -
                                    2 * us * sp.cos(ks) / 5)
    if sp.simplify(nu1_periodic - expected_periodic) != 0:
        raise ArithmeticError(("periodic first-order wrap correction",
                               nu1_periodic, expected_periodic))
    return {
        "auxiliary_cell": "periodicized site forward/backward rates; q_s uses PREVIOUS_RHO[s]",
        "state_boundary": "P y = z diag(Gamma^-1,Gamma) y, z=exp(i*5*k)",
        "exact_periodic_hermitian_block": "diag(p_s+q_s), links sqrt(p_s*q_(s+1 mod 5))",
        "max_transfer_spectral_residual": maximum_transfer_spectral_residual,
        "max_edge_transfer_determinant_error": maximum_transfer_determinant_error,
        "samples": rows,
        "first_order_existing_local_symbol": str(sp.factor(nu1_local)),
        "first_order_periodic_transfer_symbol": str(sp.factor(nu1_periodic)),
        "first_order_difference": "-2*u*cos(k)/5; caused by the wrap-link convention",
        "wrong_edge_wrap_mutation": {
            "S": mutation_spin,
            "correct_periodic_site_rate_residual": correct_wrap_residual,
            "using_residue_four_edge_reverse_rate_residual": wrong_wrap_residual,
            "rejected": True,
        },
        "scope": "exact Floquet equivalence for the explicitly periodicized auxiliary cell; the O(S^-1) symbol depends on wrap convention and proves no global varying-coefficient WKB or readout limit",
    }


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True,
        capture_output=True, text=True).stdout.strip()
    mutations = check_mutation_rejections()
    result = {
        "claim": "conditional exact ground-state reversible-rate transform",
        "source_revision": revision,
        "runner_sha256": sha256(Path(__file__).resolve()),
        "input_sha256": {str(path.relative_to(ROOT)): sha256(path) for path in INPUTS},
        "spins": [check_operator_identity(s) for s in SPINS],
        "degree_one_formal_ansatz": check_degree_one_cell_polynomial_obstruction(),
        "gauge_corrected_subprincipal": check_cell_gauge_subprincipal(),
        "second_order_non_crossing_band": check_second_order_non_crossing_band(),
        "periodic_rate_cell_transfer": check_periodic_rate_cell_transfer(),
        "finite_spectrum_candidate": check_finite_spectrum_candidate(),
        "mutation_rejections": mutations,
        "limitations": [
            "The finite checks corroborate an exact row-factorization proof; they do not prove an asymptotic result.",
            "The gauge expansion is uniform only on fixed compact interior subsets and does not supply crossing or endpoint transport.",
            "The second-order band check is at one fixed nondegenerate frozen cell and does not control the slowly varying global operator.",
            "The periodic rate-cell transfer is exactly matched to its explicitly periodicized auxiliary Hermitian block; its wrap convention differs from the existing local symbol at order 1/S.",
            "No moving-index eigenphase, eigenfunction overlap, or t=1/4 readout limit is established.",
            "The supplied model and output are not derived from the framework axioms.",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
