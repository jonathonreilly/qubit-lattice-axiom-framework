#!/usr/bin/env python3
"""Scope check for the UV gauge-to-Yukawa coefficient comparison row.

This runner is intentionally local to
docs/UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md. It avoids editing the
shared Ward runner, because that runner is load-bearing for other audited rows.

It checks only the repaired bounded surface:

* C_pert = 1/(2*N_c) from finite SU(3) Fierz algebra;
* the normalized singlet S_ab = delta_ab/sqrt(N_c);
* the rank-one projector Pi_1(ab;cd) = delta_ab delta_cd/N_c;
* the exact pair-space contraction Pi_1 H Pi_1 = (1/N_c) Pi_1;
* C_strong = 1/N_c^2 as the coefficient of delta_ab delta_cd, derived rather
  than hard-coded;
* the two coefficients differ;
* the Dirac scalar/pseudoscalar Fierz channels are nonzero and tensor vanishes;
* the Q_L singlet overlap is 1/sqrt(6);
* the source note excludes the old expansion-domain selector claim.

The pair ordering is (ab);(cd), and U^dag_cd means conjugate(U_dc).
"""

from __future__ import annotations

import math
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs/UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md"
N_c = 3
N_iso = 2
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def source_firewall() -> None:
    print("\n" + "=" * 78)
    print("PART 0: SOURCE NOTE SCOPE FIREWALL")
    print("=" * 78)
    note = NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "This repair removes the governing-coefficient selection claim",
        "This row does not select `C_pert` over `C_strong`",
        "This row does not prove perturbative convergence",
        "No new axiom is introduced",
        "bounded coefficient support/comparison note",
        "normalized-projector coefficient is",
        "coefficient of the unnormalized tensor",
    ]
    forbidden = [
        "the perturbative expansion is convergent",
        "the correct input to the main theorem",
        "The canonical surface selects the perturbative expansion",
        "governs the retained result",
    ]
    for phrase in required:
        check(f"source note carries repaired-scope phrase: {phrase}", phrase in note)
    for phrase in forbidden:
        check(f"source note excludes old selector phrase: {phrase}", phrase not in note)


def su3_generators() -> list[np.ndarray]:
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / math.sqrt(3)
    return [lam / 2.0 for lam in (l1, l2, l3, l4, l5, l6, l7, l8)]


def check_su3_fierz() -> sp.Rational:
    print("\n" + "=" * 78)
    print("PART 1: SU(3) FIERZ AND PERTURBATIVE COEFFICIENT")
    print("=" * 78)
    gens = su3_generators()
    norm_err = 0.0
    for a, ta in enumerate(gens):
        for b, tb in enumerate(gens):
            expected = 0.5 if a == b else 0.0
            norm_err = max(norm_err, abs(np.trace(ta @ tb).real - expected))
    check("Tr(T^A T^B) = 1/2 delta_AB", norm_err < 1e-14, f"max err={norm_err:.2e}")

    fierz_err = 0.0
    for a, b, c, d in product(range(N_c), repeat=4):
        lhs = sum(gen[a, b] * gen[c, d] for gen in gens).real
        rhs = 0.5 * (
            (1.0 if a == d else 0.0) * (1.0 if b == c else 0.0)
            - (1.0 / N_c) * (1.0 if a == b else 0.0) * (1.0 if c == d else 0.0)
        )
        fierz_err = max(fierz_err, abs(lhs - rhs))
    c_pert = sp.Rational(1, 2 * N_c)
    check("SU(3) Fierz identity holds entrywise", fierz_err < 1e-14, f"max err={fierz_err:.2e}")
    check("C_pert = 1/(2*N_c) = 1/6", c_pert == sp.Rational(1, 6))
    return c_pert


def random_sun_haar(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    phases = np.diag(r) / np.abs(np.diag(r))
    q = q @ np.diag(phases.conj())
    det_q = np.linalg.det(q)
    return q * (det_q.conj()) ** (1.0 / n)


def pair_operator(n: int, entry) -> sp.Matrix:
    """Flatten a rank-four tensor with pair ordering (ab);(cd)."""
    pairs = list(product(range(n), repeat=2))
    return sp.Matrix(n * n, n * n, lambda i, j: entry(*pairs[i], *pairs[j]))


def hs_inner(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    """Exact Hilbert-Schmidt inner product for equal-size pair operators."""
    return sp.simplify(
        sum(
            sp.conjugate(left[i, j]) * right[i, j]
            for i in range(left.rows)
            for j in range(left.cols)
        )
    )


def coefficient_along(basis: sp.Matrix, tensor: sp.Matrix) -> sp.Expr:
    return sp.simplify(hs_inner(basis, tensor) / hs_inner(basis, basis))


def check_strong_coupling(c_pert: sp.Rational) -> None:
    print("\n" + "=" * 78)
    print("PART 2: EXACT SINGLET PROJECTOR AND STRONG COEFFICIENT")
    print("=" * 78)

    n = N_c
    pairs = list(product(range(n), repeat=2))

    def delta(i: int, j: int) -> sp.Integer:
        return sp.Integer(i == j)

    def haar_entry(a: int, b: int, c: int, d: int) -> sp.Expr:
        return sp.Rational(1, n) * delta(a, d) * delta(b, c)

    singlet = sp.Matrix([delta(a, b) / sp.sqrt(n) for a, b in pairs])
    unnormalized_singlet = pair_operator(
        n, lambda a, b, c, d: delta(a, b) * delta(c, d)
    )
    projector = sp.simplify(singlet * singlet.H)
    expected_projector = unnormalized_singlet / n
    haar = pair_operator(n, haar_entry)

    singlet_norm = sp.simplify((singlet.H * singlet)[0])
    check("S_ab = delta_ab/sqrt(N_c) has unit norm", singlet_norm == 1)
    check("Pi_1 = S S^dag = delta_ab delta_cd/N_c entrywise", projector == expected_projector)
    check("Pi_1 is Hermitian", projector.H == projector)
    check("Pi_1 is idempotent", projector * projector == projector)
    check("Pi_1 has rank one", projector.rank() == 1)
    check("Tr(Pi_1) = 1", sp.trace(projector) == 1)
    check("||Pi_1||_HS^2 = 1", hs_inner(projector, projector) == 1)

    expected_eigenvector = singlet / n
    check("H S = (1/N_c) S", haar * singlet == expected_eigenvector)
    sandwich = sp.simplify(projector * haar * projector)
    check("Pi_1 H Pi_1 = (1/N_c) Pi_1", sandwich == projector / n)

    projector_coeff = coefficient_along(projector, haar)
    projected_component = sp.simplify(projector_coeff * projector)
    check(
        "normalized-projector coefficient is 1/N_c",
        projector_coeff == sp.Rational(1, n),
        f"alpha_1={projector_coeff}",
    )
    check(
        "singlet component reconstructs delta_ab delta_cd/N_c^2",
        projected_component == unnormalized_singlet / (n * n),
    )

    c_strong_direct = coefficient_along(unnormalized_singlet, haar)
    c_strong_reconstructed = coefficient_along(
        unnormalized_singlet, projected_component
    )
    check("<D,H>_HS = 1", hs_inner(unnormalized_singlet, haar) == 1)
    check(
        "||D||_HS^2 = N_c^2",
        hs_inner(unnormalized_singlet, unnormalized_singlet) == n * n,
    )
    check(
        "unnormalized-tensor coefficient is C_strong = 1/N_c^2",
        c_strong_direct == sp.Rational(1, n * n),
        f"C_strong={c_strong_direct}",
    )
    check(
        "direct and reconstructed C_strong agree",
        c_strong_reconstructed == c_strong_direct,
    )
    check(
        "C_strong times delta_ab delta_cd reconstructs the singlet component",
        c_strong_direct * unnormalized_singlet == projected_component,
    )
    check("N_c=3 gives C_strong = 1/9", c_strong_direct == sp.Rational(1, 9))

    # Conjugation/index convention: U^dag_cd = conjugate(U_dc).  Using
    # conjugate(U_cd) instead gives a different rank-four tensor.
    wrong_conjugation_order = pair_operator(
        n,
        lambda a, b, c, d: sp.Rational(1, n) * delta(a, c) * delta(b, d),
    )
    check(
        "U^dag_cd ordering is distinct from conjugate(U_cd) ordering",
        wrong_conjugation_order != haar,
    )

    # Hostile control 1: one of the two 1/sqrt(N_c) factors is omitted.
    half_normalized_projector = unnormalized_singlet / sp.sqrt(n)
    check(
        "HOSTILE: omitting one projector normalization factor breaks idempotence",
        half_normalized_projector * half_normalized_projector
        != half_normalized_projector,
    )
    check(
        "HOSTILE: one-factor projector has trace sqrt(N_c), not one",
        sp.trace(half_normalized_projector) == sp.sqrt(n),
    )

    # Hostile control 2: 1/N_c is the Pi_1 coefficient, not the D coefficient.
    confused_reconstruction = sp.simplify(projector_coeff * unnormalized_singlet)
    check(
        "HOSTILE: normalized-projector and unnormalized-tensor coefficients differ",
        projector_coeff != c_strong_direct,
    )
    check(
        "HOSTILE: using 1/N_c on delta_ab delta_cd is too large by N_c",
        confused_reconstruction != projected_component
        and confused_reconstruction == n * projected_component,
    )

    # Hostile control 3: exchanging b and d changes H into Pi_1 and changes
    # the projected channel coefficient from 1/N_c to 1.
    permuted_haar = pair_operator(
        n, lambda a, b, c, d: haar_entry(a, d, c, b)
    )
    permuted_projector_coeff = coefficient_along(projector, permuted_haar)
    permuted_unnormalized_coeff = coefficient_along(
        unnormalized_singlet, permuted_haar
    )
    check("HOSTILE: b<->d permutation changes H into Pi_1", permuted_haar == projector)
    check(
        "HOSTILE: permuted channel has normalized-projector coefficient 1",
        permuted_projector_coeff == 1 and permuted_projector_coeff != projector_coeff,
    )
    check(
        "HOSTILE: permuted channel has D coefficient 1/N_c, not 1/N_c^2",
        permuted_unnormalized_coeff == sp.Rational(1, n)
        and permuted_unnormalized_coeff != c_strong_direct,
    )

    print("\n  Numerical support for the starting Haar identity:")
    rng = np.random.default_rng(20260529)
    n_samples = 20_000
    sample = np.zeros((n, n, n, n), dtype=complex)
    for _ in range(n_samples):
        u = random_sun_haar(n, rng)
        # einsum label dc implements U^dag_cd = conjugate(U_dc).
        sample += np.einsum("ab,dc->abcd", u, u.conj()) / n_samples
    expected = np.zeros_like(sample)
    for a, b, c, d in product(range(n), repeat=4):
        expected[a, b, c, d] = (1.0 / n) if (a == d and b == c) else 0.0
    mc_err = float(np.max(np.abs(sample - expected)))
    check("Haar witness for integral dU U_ab U^dag_cd", mc_err < 0.02, f"max err={mc_err:.3f}")
    check(
        "C_pert and C_strong are distinct coefficients",
        c_pert != c_strong_direct,
        f"delta={float(abs(c_pert - c_strong_direct)):.4f}; selector out of scope",
    )


def check_dirac_fierz() -> None:
    print("\n" + "=" * 78)
    print("PART 3: DIRAC FIERZ CHANNEL SANITY")
    print("=" * 78)
    g0 = np.diag([1, 1, -1, -1]).astype(complex)
    g1 = np.zeros((4, 4), dtype=complex)
    g1[0, 3] = g1[1, 2] = 1
    g1[2, 1] = g1[3, 0] = -1
    g2 = np.zeros((4, 4), dtype=complex)
    g2[0, 3] = -1j
    g2[1, 2] = 1j
    g2[2, 1] = 1j
    g2[3, 0] = -1j
    g3 = np.zeros((4, 4), dtype=complex)
    g3[0, 2] = g3[3, 1] = 1
    g3[1, 3] = g3[2, 0] = -1
    i4 = np.eye(4, dtype=complex)
    g5 = 1j * g0 @ g1 @ g2 @ g3
    gammas = [g0, g1, g2, g3]
    metric = [1.0, -1.0, -1.0, -1.0]

    clifford_err = 0.0
    for mu in range(4):
        for nu in range(4):
            lhs = gammas[mu] @ gammas[nu] + gammas[nu] @ gammas[mu]
            rhs = 2 * metric[mu] * (1.0 if mu == nu else 0.0) * i4
            clifford_err = max(clifford_err, float(np.max(np.abs(lhs - rhs))))
    check("Clifford algebra holds for the gamma basis", clifford_err < 1e-14)

    tensor = np.zeros((4, 4, 4, 4), dtype=complex)
    for mu in range(4):
        tensor += metric[mu] * np.einsum("AB,CD->ABCD", gammas[mu], gammas[mu])

    def coeff(gamma: np.ndarray) -> float:
        val = 0.0 + 0.0j
        for a, b, c, d in product(range(4), repeat=4):
            val += gamma[d, a] * np.conj(gamma[b, c]) * tensor[a, b, c, d]
        return float(val.real / 16.0)

    c_s = coeff(i4)
    c_p = coeff(1j * g5)
    c_t = 0.0
    for mu in range(4):
        for nu in range(mu + 1, 4):
            sigma = (1j / 2.0) * (gammas[mu] @ gammas[nu] - gammas[nu] @ gammas[mu])
            c_t += metric[mu] * metric[nu] * coeff(sigma)
    check("scalar Fierz channel is nonzero with |c_S| = 1", abs(abs(c_s) - 1.0) < 1e-12)
    check("pseudoscalar Fierz channel is nonzero with |c_P| = 1", abs(abs(c_p) - 1.0) < 1e-12)
    check("tensor channel vanishes in the vector-vector Fierz", abs(c_t) < 1e-12, f"c_T={c_t:.2e}")


def check_h_unit_overlap() -> None:
    print("\n" + "=" * 78)
    print("PART 4: H_UNIT SINGLET OVERLAP")
    print("=" * 78)
    dim = N_c * N_iso
    singlet = np.eye(dim, dtype=complex) / math.sqrt(dim)
    norm = float(np.trace(singlet.conj().T @ singlet).real)
    overlaps = []
    for k in range(dim):
        basis = np.zeros((dim, dim), dtype=complex)
        basis[k, k] = 1.0
        overlaps.append(float(np.trace(basis.conj().T @ singlet).real))
    expected = 1.0 / math.sqrt(6.0)
    check("unit singlet has norm one", abs(norm - 1.0) < 1e-12)
    check("all six diagonal overlaps are 1/sqrt(6)", all(abs(v - expected) < 1e-12 for v in overlaps))


def main() -> int:
    source_firewall()
    c_pert = check_su3_fierz()
    check_strong_coupling(c_pert)
    check_dirac_fierz()
    check_h_unit_overlap()
    print("\n" + "=" * 78)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
