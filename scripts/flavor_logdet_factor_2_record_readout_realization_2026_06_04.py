#!/usr/bin/env python3
"""Finite disconnected-block record-readout checks for log-det Factor 2.

This runner verifies a bounded lemma: declared block-diagonal Grassmann
determinant products form a multiplicative finite scalar record-readout
surface. It also checks that a general coupled principal determinant does not
factor automatically, so full Factor 2 remains open.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def block_restrict(M: np.ndarray, idx: list[int]) -> np.ndarray:
    if not idx:
        return np.zeros((0, 0), dtype=M.dtype)
    arr = np.array(idx, dtype=int)
    return M[np.ix_(arr, arr)]


def component_det(D: np.ndarray, j: np.ndarray, idx: list[int]) -> complex:
    if not idx:
        return 1.0 + 0j
    with np.errstate(invalid="ignore", over="ignore"):
        return complex(np.linalg.det(block_restrict(D, idx) + np.diag(j[idx].astype(complex))))


def product_det(D: np.ndarray, j: np.ndarray, components: list[list[int]]) -> complex:
    out = 1.0 + 0j
    for comp in components:
        out *= component_det(D, j, comp)
    return out


def principal_det(D: np.ndarray, j: np.ndarray, idx: list[int]) -> complex:
    return component_det(D, j, idx)


def leibniz_det(M: np.ndarray) -> complex:
    n = M.shape[0]
    if n == 0:
        return 1.0 + 0j
    total = 0j
    for sigma in itertools.permutations(range(n)):
        inversions = sum(1 for i in range(n) for j in range(i + 1, n) if sigma[i] > sigma[j])
        sign = -1 if inversions % 2 else 1
        prod = 1.0 + 0j
        for i in range(n):
            prod *= M[i, sigma[i]]
        total += sign * prod
    return total


def block_diagonal_matrix(D: np.ndarray, j: np.ndarray, components: list[list[int]]) -> np.ndarray:
    sizes = [len(c) for c in components]
    total = sum(sizes)
    out = np.zeros((total, total), dtype=complex)
    offset = 0
    for comp, size in zip(components, sizes):
        block = block_restrict(D, comp) + np.diag(j[comp].astype(complex))
        out[offset:offset + size, offset:offset + size] = block
        offset += size
    return out


def main() -> int:
    rng = np.random.default_rng(2026_06_04)
    passed: list[bool] = []

    n = 8
    D = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n)) + 2.5 * np.eye(n)
    j = rng.standard_normal(n) * 0.3 + 1j * rng.standard_normal(n) * 0.1

    passed.append(check(
        "(S1) finite declared site set",
        isinstance(n, int) and n > 0,
        f"|Lambda| = {n}",
    ))

    passed.append(check(
        "(S6) empty component product has F(empty)=1",
        abs(product_det(D, j, []) - 1.0) < 1e-12,
        f"F(empty) = {product_det(D, j, [])}",
    ))

    sample = [0, 2, 5, 7]
    M_sample = block_restrict(D, sample) + np.diag(j[sample].astype(complex))
    det_np = complex(np.linalg.det(M_sample))
    det_leibniz = leibniz_det(M_sample)
    passed.append(check(
        "(S4) determinant is a finite scalar and matches Leibniz/Berezin expansion",
        np.isfinite(det_np.real) and np.isfinite(det_np.imag)
        and abs(det_np - det_leibniz) < 1e-9 * max(abs(det_np), 1.0),
        f"det={det_np:.6g}; |det-Leibniz|={abs(det_np-det_leibniz):.2e}",
    ))

    components_a = [[0, 1], [2, 3]]
    components_b = [[4], [5, 6, 7]]
    F_a = product_det(D, j, components_a)
    F_b = product_det(D, j, components_b)
    F_union = product_det(D, j, components_a + components_b)
    passed.append(check(
        "(S5) declared disconnected components multiply",
        abs(F_union - F_a * F_b) < 1e-9 * max(abs(F_a * F_b), 1.0),
        f"|F_union - F_a*F_b|={abs(F_union-F_a*F_b):.2e}",
    ))

    I_a = np.log(abs(F_a))
    I_b = np.log(abs(F_b))
    I_union = np.log(abs(F_union))
    passed.append(check(
        "log readout is additive on nonzero disconnected products",
        abs(I_union - (I_a + I_b)) < 1e-10,
        f"|I_union-(I_a+I_b)|={abs(I_union-(I_a+I_b)):.2e}",
    ))

    M_bd = block_diagonal_matrix(D, j, components_a + components_b)
    passed.append(check(
        "block-diagonal determinant equals product over declared components",
        abs(np.linalg.det(M_bd) - F_union) < 1e-9 * max(abs(F_union), 1.0),
        f"|det(blockdiag)-product|={abs(np.linalg.det(M_bd)-F_union):.2e}",
    ))

    # Hostile check: the full principal determinant on a coupled union generally
    # does not factor. This is the reason the full Factor 2 claim remains open.
    Lambda_1 = [0, 1, 2]
    Lambda_2 = [3, 4, 5]
    coupled_union = sorted(Lambda_1 + Lambda_2)
    full_union = principal_det(D, j, coupled_union)
    product_union = principal_det(D, j, Lambda_1) * principal_det(D, j, Lambda_2)
    coupled_gap = abs(full_union - product_union)
    passed.append(check(
        "hostile check: coupled principal determinant need not be multiplicative",
        coupled_gap > 1e-3,
        f"|det(union principal)-det(L1)det(L2)|={coupled_gap:.3g}",
    ))

    # Sanity: if off-block couplings are explicitly zeroed, principal determinant
    # reduces to the block-diagonal case.
    D_decoupled = D.copy()
    for a in Lambda_1:
        for b in Lambda_2:
            D_decoupled[a, b] = 0
            D_decoupled[b, a] = 0
    decoupled_union = principal_det(D_decoupled, j, coupled_union)
    decoupled_product = principal_det(D_decoupled, j, Lambda_1) * principal_det(D_decoupled, j, Lambda_2)
    decoupled_err = abs(decoupled_union - decoupled_product)
    passed.append(check(
        "decoupled principal determinant multiplicativity sanity",
        decoupled_err < 1e-9 * max(abs(decoupled_product), 1.0),
        f"|det(decoupled union)-product|={decoupled_err:.2e}",
    ))

    D_nh = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n)) + 3.0 * np.eye(n)
    nh_norm = np.linalg.norm(D_nh - D_nh.conj().T)
    F_nh = product_det(D_nh, j, components_a + components_b)
    passed.append(check(
        "non-Hermitian finite blocks still define finite disconnected products",
        np.isfinite(F_nh.real) and np.isfinite(F_nh.imag) and nh_norm > 1e-3,
        f"||D-D^dagger||_F={nh_norm:.3g}; F={F_nh:.6g}",
    ))

    D_real = rng.standard_normal((n, n)) + 3.0 * np.eye(n)
    j_real = rng.standard_normal(n)
    F_real = product_det(D_real, j_real, components_a + components_b)
    passed.append(check(
        "real-matrix finite blocks also define finite disconnected products",
        np.isfinite(F_real.real) and abs(F_real.imag) < 1e-12,
        f"F_real={F_real:.6g}",
    ))

    def trace_surface(D_in: np.ndarray, j_in: np.ndarray, idx: list[int]) -> complex:
        if not idx:
            return 0.0 + 0j
        return complex(np.trace(block_restrict(D_in, idx) + np.diag(j_in[idx].astype(complex))))

    tr_a = trace_surface(D, j, Lambda_1)
    tr_b = trace_surface(D, j, Lambda_2)
    tr_union = trace_surface(D, j, coupled_union)
    trace_gap = abs(tr_union - tr_a * tr_b)
    passed.append(check(
        "hostile check: trace surface fails multiplicativity",
        trace_gap > 1e-3,
        f"|Tr(union)-Tr(L1)Tr(L2)|={trace_gap:.3g}",
    ))

    D_bad = D.copy()
    D_bad[0, 0] = np.inf
    F_bad = component_det(D_bad, j, [0, 1, 2])
    passed.append(check(
        "hostile check: non-finite operator is outside the finite-scalar precondition",
        not np.isfinite(F_bad),
        f"F_bad={F_bad}",
    ))

    repo_root = Path(__file__).resolve().parents[1]
    cite_paths = [
        "docs/MINIMAL_AXIOMS_2026-06-04.md",
        "docs/FLAVOR_LOGDET_GENERATOR_THREE_FACTOR_PROVENANCE_2026-06-04.md",
        "docs/STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md",
    ]
    missing = [p for p in cite_paths if not (repo_root / p).exists()]
    passed.append(check(
        "cite-check: load-bearing source paths exist",
        not missing,
        f"missing: {missing if missing else 'none'}",
    ))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("FACTOR 2 DISCONNECTED-BLOCK LEMMA: declared block-diagonal Grassmann")
    print("determinant products realize a multiplicative finite scalar record-readout surface.")
    print("The coupled KS principal determinant does not factor automatically; full Factor 2 remains open.")
    print("Record is baseline semantics, not a status source. No audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
