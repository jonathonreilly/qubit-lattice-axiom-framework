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
    for i, n in enumerate(nodes):
        if n < hi:
            ml, _mr = labels.edge_labels(n)
            rplus = 1.0 - labels.f(ml) / C
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
    if max_operator_error > 2e-11 or zero_mode_error > 2e-11:
        raise ArithmeticError(("ground-state rate identity", spin, max_operator_error,
                               zero_mode_error))
    if max_balance_error > 2e-12 or hermitian_error > 2e-12:
        raise ArithmeticError(("detailed balance or symmetry", spin,
                               max_balance_error, hermitian_error))
    return {
        "spin": spin,
        "dimension": len(nodes),
        "max_operator_identity_error": max_operator_error,
        "max_zero_mode_error": zero_mode_error,
        "max_detailed_balance_error": max_balance_error,
        "max_hermitian_error": hermitian_error,
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
    result = {
        "claim": "conditional exact ground-state reversible-rate transform",
        "source_revision": revision,
        "input_sha256": {str(path.relative_to(ROOT)): sha256(path) for path in INPUTS},
        "spins": [check_operator_identity(s) for s in SPINS],
        "degree_one_formal_ansatz": check_degree_one_cell_polynomial_obstruction(),
        "limitations": [
            "The finite checks corroborate an exact row-factorization proof; they do not prove an asymptotic result.",
            "No moving-index eigenphase, eigenfunction overlap, or t=1/4 readout limit is established.",
            "The supplied model and output are not derived from the framework axioms.",
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
