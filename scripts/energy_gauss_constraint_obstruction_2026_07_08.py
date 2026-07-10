#!/usr/bin/env python3
"""Check one adjacent-density obstruction for a commuting auxiliary ansatz.

For the declared two-species cell Hamiltonian density h_n, define
G_n = eta_n-eta_{n-1}-h_n and impose [eta_n,eta_m]=[eta_n,h_m]=0.  The runner
computes [h_0,h_1] and checks that it is nonzero at one declared parameter
point, while [h_0,h_2] vanishes by locality.  Under the displayed auxiliary
premise, [G_0,G_1]=[h_0,h_1].  No statement is made about other density
apportionings, noncommuting auxiliaries, enlarged constraints, or gauging in
general.
"""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys
import time

import numpy as np
import scipy.sparse as sp


sys.dont_write_bytecode = True

CELL_SITES = 2
DENSE_SITES = 8
CHECK_TOL = 1.0e-12
CLEAN_TOL = 1.0e-14


def import_classification_runner():
    path = Path(__file__).with_name("noether_source_current_classification_2026_07_08.py")
    spec = importlib.util.spec_from_file_location("noether_source_current_classification_2026_07_08", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load finite-basis operator runner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


eng = import_classification_runner()


def translate_op(operator, delta_sites: int):
    translated = {}
    for key, coefficient in operator.items():
        eng.op_add(translated, eng.translate_key(key, delta_sites), coefficient)
    return translated


def cell_energy(couplings, cell: int):
    return translate_op(eng.build_h_density(couplings), CELL_SITES * cell)


def site_charge(site: int):
    operator = {}
    eng.add_number(operator, eng.mode(site, "a"), 1.0)
    eng.add_number(operator, eng.mode(site, "b"), 1.0)
    return operator


def commutator(left, right):
    output = {}
    for left_key, left_coefficient in left.items():
        if abs(left_coefficient) <= CLEAN_TOL:
            continue
        for right_key, right_coefficient in right.items():
            if abs(right_coefficient) <= CLEAN_TOL:
                continue
            scale = left_coefficient * right_coefficient
            for key, coefficient in eng.commutator_key_items(left_key, right_key):
                eng.op_add(output, key, scale * coefficient)
    return output


def coefficient_norm(operator) -> float:
    return math.sqrt(sum(float(abs(coefficient) ** 2) for coefficient in operator.values()))


def sparse_max_abs(matrix: sp.spmatrix) -> float:
    coo = matrix.tocoo()
    return float(np.max(np.abs(coo.data))) if coo.nnz else 0.0


def dense_commutator_error(left, right, symbolic, cache) -> float:
    left_matrix = eng.operator_sparse(left, DENSE_SITES, cache)
    right_matrix = eng.operator_sparse(right, DENSE_SITES, cache)
    symbolic_matrix = eng.operator_sparse(symbolic, DENSE_SITES, cache)
    difference = left_matrix @ right_matrix - right_matrix @ left_matrix - symbolic_matrix
    difference.eliminate_zeros()
    return sparse_max_abs(difference)


def hilbert_schmidt_norm(operator, cache) -> float:
    matrix = eng.operator_sparse(operator, DENSE_SITES, cache).tocsr()
    return float(np.linalg.norm(matrix.data)) if matrix.nnz else 0.0


def commuting_auxiliary_identity_error() -> tuple[float, float]:
    """Independent finite-matrix check of [G0,G1]=[h0,h1]."""

    eye_aux = np.eye(3, dtype=np.complex128)
    eye_matter = np.eye(2, dtype=np.complex128)
    eta_minus = np.diag([-0.7, 0.2, 1.1]).astype(np.complex128)
    eta_zero = np.diag([0.4, -0.3, 0.9]).astype(np.complex128)
    eta_one = np.diag([1.2, 0.5, -0.6]).astype(np.complex128)
    h_zero = np.array([[0.3, 1.0 - 0.2j], [1.0 + 0.2j, -0.4]], dtype=np.complex128)
    h_one = np.array([[-0.1, 0.6 + 0.5j], [0.6 - 0.5j, 0.8]], dtype=np.complex128)

    g_zero = np.kron(eta_zero - eta_minus, eye_matter) - np.kron(eye_aux, h_zero)
    g_one = np.kron(eta_one - eta_zero, eye_matter) - np.kron(eye_aux, h_one)
    lhs = g_zero @ g_one - g_one @ g_zero
    matter_commutator = h_zero @ h_one - h_one @ h_zero
    rhs = np.kron(eye_aux, matter_commutator)
    return float(np.linalg.norm(lhs - rhs)), float(np.linalg.norm(rhs))


def main() -> int:
    started = time.time()
    cache = {}
    couplings = eng.Couplings(
        t_a=0.8,
        t_b=1.1,
        m_a=0.4,
        m_b=0.6,
        U=0.9,
        V_a=0.5,
        V_b=1.2,
        W_ab=0.7,
    )

    h0 = cell_energy(couplings, 0)
    h1 = cell_energy(couplings, 1)
    h2 = cell_energy(couplings, 2)
    adjacent = commutator(h0, h1)
    separated = commutator(h0, h2)
    adjacent_coefficient_norm = coefficient_norm(adjacent)
    adjacent_hs_norm = hilbert_schmidt_norm(adjacent, cache)
    dense_error = dense_commutator_error(h0, h1, adjacent, cache)

    charges = [site_charge(site) for site in range(6)]
    charge_abelian = all(not commutator(left, right) for left in charges for right in charges)
    adjacent_nonzero = adjacent_coefficient_norm > CHECK_TOL and adjacent_hs_norm > CHECK_TOL
    separated_zero = not separated
    dense_ok = dense_error <= CHECK_TOL
    auxiliary_identity_error, auxiliary_rhs_norm = commuting_auxiliary_identity_error()
    auxiliary_identity_ok = auxiliary_identity_error <= CHECK_TOL and auxiliary_rhs_norm > CHECK_TOL
    passed = charge_abelian and adjacent_nonzero and separated_zero and dense_ok and auxiliary_identity_ok

    coupling_text = ",".join(f"{name}={value:.8g}" for name, value in couplings.__dict__.items())
    print(f"SURFACE {coupling_text};density=declared-cell-h;auxiliary=commuting-with-self-and-matter")
    print(
        "OPERATORS "
        f"adjacent_coeff_l2={adjacent_coefficient_norm:.8e};"
        f"adjacent_hs8={adjacent_hs_norm:.8e};"
        f"separated_d2_zero={'Y' if separated_zero else 'N'};"
        f"dense_error={dense_error:.1e};"
        f"aux_identity_error={auxiliary_identity_error:.1e};"
        f"aux_rhs_norm={auxiliary_rhs_norm:.8e}"
    )
    print(
        "CHECKS "
        f"CHECK-01-charge-control={'ok' if charge_abelian else 'FAIL'};"
        f"CHECK-02-adjacent-nonzero={'ok' if adjacent_nonzero else 'FAIL'};"
        f"CHECK-03-separated-zero={'ok' if separated_zero else 'FAIL'};"
        f"CHECK-04-dense-crosscheck={'ok' if dense_ok else 'FAIL'};"
        f"CHECK-05-commuting-auxiliary-identity={'ok' if auxiliary_identity_ok else 'FAIL'}"
    )
    print(f"TOTAL {'PASS' if passed else 'MACHINERY-FAIL'} elapsed={time.time()-started:.2f}s")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
