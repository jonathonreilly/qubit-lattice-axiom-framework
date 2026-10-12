#!/usr/bin/env python3
"""Author controls for a conditional proof; finite checks do not prove its domains.

Distinct controls use direct Kronecker matrices, stabilizer spectrum formulas,
and exact rational tail sums. Mutation options change computed objects while
leaving comparison criteria fixed, and the script must then exit nonzero.
No author/source helper or expected-result file is imported.
"""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/MICROSCOPIC_BOOST_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

import argparse
import datetime as dt
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.linalg import expm


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
TOL = 2e-10
ROWS = []


def norm(a):
    return float(np.linalg.norm(a, 2))


def comm(a, b):
    return a @ b - b @ a


def tensor(parts):
    a = np.ones((1, 1), dtype=complex)
    for part in parts:
        a = np.kron(a, part)
    return a


def at(pauli, site, size):
    return tensor([pauli if k == site else I for k in range(size)])


def check(name, passed, **data):
    row = {"name": name, "passed": bool(passed), **data}
    ROWS.append(row)
    print(json.dumps(row, sort_keys=True))


def qstr(a):
    return str(a.numerator) if a.denominator == 1 else f"{a.numerator}/{a.denominator}"


def seminorm(coefficients, nu):
    """Exact norm+tail norm for commuting, independent traceless onsite Paulis.

    Real radii: supremum at r tending to each support coordinate from below.
    Each term has norm |coefficient| and independent joint eigenvalues.
    """
    absolute = sorted((int(r), abs(a)) for r, a in coefficients if a)
    nrm = sum((a for _, a in absolute), F(0))
    tail = F(0)
    sup = F(0)
    for radius, a in reversed(absolute):
        tail += a
        sup = max(sup, (1 + radius) ** nu * tail)
    return nrm + sup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=["none", "drop_position", "reverse_clock",
                                               "drop_gns_right", "reverse_current"], default="none")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    def weighted_sum(terms, coords):
        weights = [1] * len(coords) if args.mutation == "drop_position" else coords
        return sum((w * h for w, h in zip(weights, terms)), np.zeros_like(terms[0]))

    def evolve(generator, observable, time):
        sign = -1 if args.mutation == "reverse_clock" else 1
        unitary = expm(1j * sign * time * generator)
        return unitary @ observable @ unitary.conj().T

    def gns_generator(generator):
        ident = np.eye(generator.shape[0], dtype=complex)
        left = np.kron(ident, generator)
        if args.mutation == "drop_gns_right":
            return left
        return left - np.kron(generator.T, ident)

    # A stationary, translation-invariant infinite-product state need not obey
    # boost infinitesimal invariance: the finite padded sums are exact on Y_0.
    onsite_z = [at(Z, k, 3) for k in range(3)]
    hminus, hzero = onsite_z[0] - onsite_z[1], onsite_z[1] - onsite_z[2]
    aa = at(Y, 1, 3)
    h = hminus + hzero
    b = weighted_sum([hminus, hzero], [-1, 0])
    dh = 1j * comm(h, aa)
    db = 1j * comm(b, aa)
    plus = np.array([1, 1], complex) / np.sqrt(2)
    vector = tensor([plus.reshape(2, 1)] * 3).reshape(-1)
    state_value = float(np.vdot(vector, db @ vector).real)
    check("telescoping_energy_is_zero_on_local_probe", norm(dh) == 0.0,
          residual=norm(dh), support_coordinates=[-1, 0, 1])
    check("telescoping_weighted_derivative_sign", norm(db - 2 * at(X, 1, 3)) == 0.0,
          residual=norm(db - 2 * at(X, 1, 3)))
    check("stationary_product_state_fails_boost_identity", abs(state_value - 2) < TOL,
          expected_from_Pauli_commutator=2, observed_expectation=state_value)

    # Independent stabilizer argument predicts the exact local norm. The
    # matrix is independently assembled as [sum_x x Z_x, product_x X_x].
    for radius in (1, 2, 3):
        coords = list(range(-radius, radius + 1))
        size = len(coords)
        terms = [at(Z, k, size) for k in range(size)]
        bb = weighted_sum(terms, coords)
        aa = tensor([X] * size)
        derivative = 1j * comm(bb, aa)
        eig = np.linalg.eigvalsh(derivative)
        observed = float(max(abs(eig)))
        stabilizer_norm = 2 * radius * (radius + 1)
        check(f"local_weighted_support_growth_L{radius}", abs(observed - stabilizer_norm) < TOL,
              observed_norm=observed, independent_joint_sign_norm=stabilizer_norm)
        if radius >= 2:
            check(f"omitting_position_is_not_a_valid_bound_L{radius}", observed > 2 * size + TOL,
                  observed_norm=observed, unweighted_mutant_bound=2 * size)
            check(f"omitting_support_count_is_not_a_valid_bound_L{radius}", observed > 2 * radius + TOL,
                  observed_norm=observed, one_site_mutant_bound=2 * radius)

    # A local norm approximation of zero whose derivative does not tend to zero.
    for position in (2, 4, 16, 64):
        a = X / position
        weight = 1 if args.mutation == "drop_position" else position
        derivative = 1j * comm(weight * Z, a)
        check(f"norm_approximation_is_not_graph_approximation_x{position}",
              abs(norm(derivative) - 2) < TOL and abs(norm(a) - 1 / position) < TOL,
              observable_norm=norm(a), derivative_norm=norm(derivative))

    # Exact finite dyadic graph tails and the displayed loss constant, d=1,R=0.
    # These finite sums are AL; no numerical extrapolation claims infinite decay.
    terms = [(2 ** m, F(1, 2 ** (7 * m))) for m in range(1, 19)]
    nu, q, d, kappa = 2, 5, 1, 1
    u = nu + d + kappa
    K = F(2 * 3 ** d)
    tail_constant = 3 * K * F(2 ** (q + 1), 2 ** (q - u) - 1)
    input_norm = seminorm(terms, q)
    derivative_terms = [(r, -2 * r * c) for r, c in terms]
    for level in (0, 1, 2, 4, 8, 12):
        remaining = [(r, c) for r, c in derivative_terms if r > 2 ** level]
        observed = seminorm(remaining, nu)
        bound = tail_constant * F(1, 2 ** (level * (q - u))) * input_norm
        check(f"dyadic_graph_tail_N{level}", observed <= bound,
              exact_tail_seminorm=qstr(observed), exact_B16_bound=qstr(bound),
              ratio=float(observed / bound))
    # B11 is checked with the same norm+tail definition, independently of B16.
    for level in (0, 2, 5):
        tail_terms = [(r, c) for r, c in terms if r > 2 ** level]
        observed = seminorm(tail_terms, nu)
        bound = 2 * F(1, (1 + 2 ** level) ** (q - nu)) * input_norm
        check(f"expectation_approximation_N{level}", observed <= bound,
              exact_tail_seminorm=qstr(observed), exact_B11_bound=qstr(bound))

    # Positive-clock evolution is independently known from the 2x2 Pauli formula.
    for position in (1, 3, 11):
        for time in (0.13, -0.27):
            computed = evolve(position * Z, X, time)
            explicit = np.cos(2 * position * time) * X - np.sin(2 * position * time) * Y
            check(f"onsite_positive_clock_x{position}_t{time}", norm(computed - explicit) < TOL,
                  matrix_exponential_vs_trigonometric_residual=norm(computed - explicit))
            check(f"onsite_tail_term_norm_preserved_x{position}_t{time}",
                  abs(norm(computed) - 1) < TOL and abs(np.trace(computed)) < TOL,
                  term_norm=norm(computed), trace_abs=float(abs(np.trace(computed))))

    # A separate finite noncommuting fixture. The two densities are translates
    # inside these three sites; this is a finite algebra control, not a proof
    # about a boundary-free thermodynamic boost or the physical model.
    h0 = at(Z, 0, 3) + 0.5 * at(X, 0, 3) @ at(X, 1, 3) + 0.25 * at(Y, 1, 3)
    h1 = at(Z, 1, 3) + 0.5 * at(X, 1, 3) @ at(X, 2, 3) + 0.25 * at(Y, 2, 3)
    densities, coords = [h0, h1], [0, 1]
    h = h0 + h1
    b = weighted_sum(densities, coords)
    pdensity = sum((0.5j * (coords[j] - coords[i]) * comm(densities[i], densities[j])
                    for i in range(2) for j in range(2)), np.zeros_like(h))
    if args.mutation == "reverse_current":
        pdensity = -pdensity
    check("finite_current_pair_sign", norm(1j * comm(h, b) - pdensity) < TOL,
          residual=norm(1j * comm(h, b) - pdensity), current_norm=norm(pdensity))

    dim = h.shape[0]
    eye = np.eye(dim, dtype=complex)
    hh, bb, pp = gns_generator(h), gns_generator(b), gns_generator(pdensity)
    omega = eye.reshape(-1, order="F") / np.sqrt(dim)
    check("canonical_GNS_boost_fixes_trace_vector", np.linalg.norm(bb @ omega) < TOL,
          vector_residual=float(np.linalg.norm(bb @ omega)))
    check("canonical_GNS_generators_are_Hermitian",
          max(norm(g - g.conj().T) for g in (hh, bb, pp)) < TOL,
          max_residual=max(norm(g - g.conj().T) for g in (hh, bb, pp)))
    check("canonical_GNS_current_commutator", norm(1j * comm(hh, bb) - pp) < TOL,
          full_Hilbert_matrix_residual=norm(1j * comm(hh, bb) - pp))

    basis = []
    max_local_action = 0.0
    max_state_derivative = 0.0
    for i in range(dim):
        for j in range(dim):
            a = np.zeros((dim, dim), complex)
            a[i, j] = 1
            basis.append(a)
            vec = a.reshape(-1, order="F") / np.sqrt(dim)
            local = comm(b, a).reshape(-1, order="F") / np.sqrt(dim)
            max_local_action = max(max_local_action, float(np.linalg.norm(bb @ vec - local)))
            max_state_derivative = max(max_state_derivative, float(abs(np.trace(1j * comm(b, a)) / dim)))
    check("GNS_local_action_on_complete_matrix_basis", max_local_action < TOL,
          basis_size=len(basis), max_vector_residual=max_local_action)
    check("trace_infinitesimal_invariance_on_complete_basis", max_state_derivative < TOL,
          basis_size=len(basis), max_state_derivative=max_state_derivative)

    for time in (0.19, -0.41):
        group = expm(1j * time * bb)
        groupstar = group.conj().T
        columns, algebra, curve, state = 0.0, 0.0, 0.0, 0.0
        for a in basis:
            evolved = evolve(b, a, time)
            vec = a.reshape(-1, order="F") / np.sqrt(dim)
            evolved_vec = evolved.reshape(-1, order="F") / np.sqrt(dim)
            columns = max(columns, float(np.linalg.norm(group @ vec - evolved_vec)))
            algebra = max(algebra, norm(group @ np.kron(eye, a) @ groupstar - np.kron(eye, evolved)))
            # Independently differentiate the computed curve, including its
            # actual clock sign, rather than substituting the expected equation.
            step = 1e-4
            finite_difference = (-evolve(b, a, time + 2 * step)
                                 + 8 * evolve(b, a, time + step)
                                 - 8 * evolve(b, a, time - step)
                                 + evolve(b, a, time - 2 * step)) / (12 * step)
            actual_derivative = finite_difference.reshape(-1, order="F") / np.sqrt(dim)
            curve = max(curve, float(np.linalg.norm(actual_derivative - 1j * bb @ evolved_vec)))
            state = max(state, float(abs(np.trace(evolved - a) / dim)))
        check(f"GNS_group_columns_t{time}", columns < TOL, basis_size=len(basis), max_residual=columns)
        check(f"GNS_full_algebra_implementation_t{time}", algebra < TOL,
              basis_size=len(basis), max_operator_residual=algebra)
        check(f"GNS_C1_Schrodinger_curve_t{time}", curve < TOL,
              basis_size=len(basis), max_derivative_residual=curve,
              differentiation="fourth-order centered finite difference", step=1e-4)
        check(f"trace_finite_time_invariance_t{time}", state < TOL,
              basis_size=len(basis), max_state_residual=state)

    raw = Path(__file__).read_bytes()
    result = {"utc": dt.datetime.now(dt.timezone.utc).isoformat(), "mutation": args.mutation,
              "source_sha256": hashlib.sha256(raw).hexdigest(),
              "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
              "matrix_tolerance": TOL, "rows": ROWS,
              "passed": sum(r["passed"] for r in ROWS), "failed": sum(not r["passed"] for r in ROWS),
              "scope": "Author finite controls only; no proof of infinite-volume domains or independent review."}
    # Publication suppresses the adjacent-result write only; all calculations and original JSON evidence are preserved.
    print(json.dumps({"total_passed": result["passed"], "total_failed": result["failed"], "mutation": args.mutation}))
    print('per_element: finite weighted commutator, current and orbit-derivative fixtures are checked; the analytic proof carries their generalization.')
    print('per_site: finite support and current signs are checked; no intended microscopic density/state is supplied by the controls.')
    print('per_mode: checked and not executed — no physical particle mode or positive-energy spectral realization is constructed.')
    print('per_block: finite GNS column, adjoint and C1-orbit fixtures are checked; their nondiscriminating rows remain visible.')
    print('lattice_wide: checked and not executed — infinite weighted-flow existence and domains use the conditional analytic argument and matched external theorem.')
    print("TOTAL: PASS=" + str(result["passed"]) + " FAIL=" + str(result["failed"]))
    print('SCOPE: Original finite controls only; documented mutation survivors and insensitive rows remain. Counts do not prove the analytic theorem or a physical model.')
    return 1 if result["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
