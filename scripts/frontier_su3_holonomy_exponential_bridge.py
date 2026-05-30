#!/usr/bin/env python3
"""
Finite SU(3) Holonomy Exponential Bridge
=======================================

Purpose
-------
Check the algebraic bridge that the g_bare rigidity row needs:

  every finite SU(3) link holonomy U admits a traceless-Hermitian
  logarithm A_op in the fixed su(3) generator span, so

      U = exp(i a A_op) = exp(i a A^a T_a)

  for a > 0.  The bridge is existence plus fixed-basis coefficient
  reconstruction.  It does not derive a continuum gauge field, Wilson
  action, beta value, path integral measure, or a unique global log branch.

Self-contained: numpy only.
"""

from __future__ import annotations

import math

import numpy as np

np.set_printoptions(precision=10, linewidth=120, suppress=True)

TAU = 2.0 * math.pi
TOL = 2.0e-9
PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    msg = f"  [{tag}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)


def gellmann_generators() -> list[np.ndarray]:
    lam = [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3.0),
    ]
    return [x / 2.0 for x in lam]


def expm_hermitian(h: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(h)
    return (vecs * np.exp(1j * vals)) @ vecs.conj().T


def coeffs_to_algebra(coeffs: np.ndarray, basis: list[np.ndarray] | None = None) -> np.ndarray:
    if basis is None:
        basis = gellmann_generators()
    out = np.zeros((3, 3), dtype=complex)
    for c, t in zip(coeffs, basis):
        out += float(c) * t
    return out


def algebra_to_coeffs(h: np.ndarray, basis: list[np.ndarray] | None = None) -> np.ndarray:
    if basis is None:
        basis = gellmann_generators()
    return np.array([2.0 * np.trace(h @ t).real for t in basis])


def canonical_su3_log(u: np.ndarray, a: float = 1.0) -> np.ndarray:
    """Return one traceless-Hermitian logarithm H/a with exp(i a H)=U.

    The phase adjustment enforces su(3) trace zero.  It selects one discrete
    branch, not a unique global connection.
    """
    vals, vecs = np.linalg.eig(u)
    angles = np.angle(vals)
    order = np.argsort(angles)
    angles = angles[order]
    vecs = vecs[:, order]

    # det(U)=1 implies sum principal phases is an integer multiple of 2*pi.
    winding = int(np.rint(np.sum(angles) / TAU))
    if winding > 0:
        for _ in range(winding):
            angles[int(np.argmax(angles))] -= TAU
    elif winding < 0:
        for _ in range(-winding):
            angles[int(np.argmin(angles))] += TAU

    h = vecs @ np.diag(angles / a) @ np.linalg.inv(vecs)
    h = (h + h.conj().T) / 2.0
    h -= np.trace(h) / 3.0 * np.eye(3)
    return h


def su3_from_phases(phases: tuple[float, float, float]) -> np.ndarray:
    assert abs(sum(phases)) < 1.0e-12
    return np.diag(np.exp(1j * np.array(phases)))


def random_su3_from_coeffs(seed: int, scale: float) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    coeffs = rng.normal(size=8) * scale
    h = coeffs_to_algebra(coeffs)
    return expm_hermitian(h), h


def test_basis() -> None:
    print("\nSECTION 1: canonical su(3) basis")
    print("-" * 72)
    basis = gellmann_generators()
    gram = np.array([[np.trace(a @ b).real for b in basis] for a in basis])
    check("Gell-Mann basis is Hermitian and traceless", all(np.linalg.norm(t - t.conj().T) < TOL and abs(np.trace(t)) < TOL for t in basis))
    check("Tr(T_a T_b)=delta_ab/2", np.linalg.norm(gram - 0.5 * np.eye(8)) < TOL, f"max dev={np.max(np.abs(gram - 0.5 * np.eye(8))):.2e}")


def test_reconstruction_cases() -> None:
    print("\nSECTION 2: finite-link logarithm reconstruction")
    print("-" * 72)
    cases: list[tuple[str, np.ndarray, np.ndarray | None]] = [
        ("identity link", np.eye(3, dtype=complex), np.zeros((3, 3), dtype=complex)),
        ("generic diagonal link", su3_from_phases((0.71, -0.19, -0.52)), None),
        ("center-sector link", np.exp(2j * math.pi / 3.0) * np.eye(3, dtype=complex), None),
    ]
    for seed, scale in [(11, 0.18), (23, 0.55), (37, 1.10)]:
        u, h0 = random_su3_from_coeffs(seed, scale)
        cases.append((f"random exponential link seed={seed}", u, h0 if scale < 0.25 else None))

    basis = gellmann_generators()
    for label, u, h_expected in cases:
        h = canonical_su3_log(u)
        coeffs = algebra_to_coeffs(h, basis)
        h_coeff = coeffs_to_algebra(coeffs, basis)
        u_back = expm_hermitian(h)
        check(f"{label}: U is special unitary", np.linalg.norm(u.conj().T @ u - np.eye(3)) < TOL and abs(np.linalg.det(u) - 1.0) < TOL)
        check(f"{label}: log is Hermitian traceless", np.linalg.norm(h - h.conj().T) < TOL and abs(np.trace(h)) < TOL)
        check(f"{label}: log lies in fixed generator span", np.linalg.norm(h - h_coeff) < TOL, f"coeff_norm={np.linalg.norm(coeffs):.6f}")
        check(f"{label}: exp(i H) reconstructs U", np.linalg.norm(u - u_back) < 2.0e-8, f"err={np.linalg.norm(u-u_back):.2e}")
        if h_expected is not None:
            check(f"{label}: local branch recovers supplied generator", np.linalg.norm(h - h_expected) < 2.0e-8, f"err={np.linalg.norm(h-h_expected):.2e}")


def test_discrete_branch_not_scalar_freedom() -> None:
    print("\nSECTION 3: branch ambiguity is discrete, not a continuous scalar")
    print("-" * 72)
    h = np.diag([0.40, -0.10, -0.30]).astype(complex)
    coroot = np.diag([TAU, -TAU, 0.0]).astype(complex)
    u = expm_hermitian(h)
    u_shift = expm_hermitian(h + coroot)
    coeffs = algebra_to_coeffs(h)
    coeffs_shift = algebra_to_coeffs(h + coroot)

    ratios = []
    for a, b in zip(coeffs, coeffs_shift):
        if abs(a) > 1.0e-10:
            ratios.append(b / a)
    scalar_like = bool(ratios) and max(abs(r - ratios[0]) for r in ratios) < 1.0e-8

    check("integer coroot shift leaves the same SU(3) holonomy", np.linalg.norm(u - u_shift) < TOL, f"err={np.linalg.norm(u-u_shift):.2e}")
    check("branch shift preserves su(3), but changes coefficients discretely", abs(np.trace(h + coroot)) < TOL and np.linalg.norm(coeffs_shift - coeffs) > 1.0)
    check("branch shift is not a uniform scalar dilation of all generators", not scalar_like)


def main() -> int:
    print("=" * 72)
    print("FINITE SU(3) HOLONOMY EXPONENTIAL BRIDGE")
    print("=" * 72)
    print("Claim checked: every tested finite SU(3) link has a traceless-Hermitian")
    print("logarithm in the fixed canonical generator span, giving U=exp(i A^a T_a a).")
    print("Scope: algebraic finite-link bridge only; no continuum or action claim.")

    test_basis()
    test_reconstruction_cases()
    test_discrete_branch_not_scalar_freedom()

    print()
    print("=" * 72)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    if FAIL:
        return 1
    print("BRIDGE PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
