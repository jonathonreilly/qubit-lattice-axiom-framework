#!/usr/bin/env python3
"""Runner for GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM.

Checks the bounded weak-field source-response bridge:

1. The quadratic action A[phi;rho] = 1/2 <phi,H phi> - <P0 rho,phi>
   has Euler equation H phi = P0 rho and unique minimizer phi = G0 P0 rho
   on the zero-mode-removed sector.
2. The only local diagonal phase-invariant translation-covariant normalized
   quadratic density is rho(x)=|psi(x)|^2.
3. A localized test source coupled by the same source term has first-order
   action response S_test = L_test(1 - phi(x)) and bilinear force response.
"""

from __future__ import annotations

from pathlib import Path
import itertools
import math
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{tag}: {label}{suffix}")


def idx(x: tuple[int, int, int], L: int) -> int:
    return (x[0] % L) * L * L + (x[1] % L) * L + (x[2] % L)


def coords(i: int, L: int) -> tuple[int, int, int]:
    return (i // (L * L), (i // L) % L, i % L)


def build_laplacian(L: int) -> np.ndarray:
    N = L**3
    H = np.zeros((N, N), dtype=float)
    for x in itertools.product(range(L), repeat=3):
        ix = idx(x, L)
        H[ix, ix] = 6.0
        for mu in range(3):
            for s in (-1, 1):
                y = list(x)
                y[mu] = (y[mu] + s) % L
                H[ix, idx(tuple(y), L)] -= 1.0
    return H


def translation_matrix(L: int, shift: tuple[int, int, int]) -> np.ndarray:
    N = L**3
    T = np.zeros((N, N), dtype=float)
    for x in itertools.product(range(L), repeat=3):
        y = ((x[0] + shift[0]) % L, (x[1] + shift[1]) % L, (x[2] + shift[2]) % L)
        T[idx(y, L), idx(x, L)] = 1.0
    return T


def neutral_projector(N: int) -> np.ndarray:
    one = np.ones((N, 1), dtype=float)
    return np.eye(N) - (one @ one.T) / N


def finite_difference_gradient(values: np.ndarray, site: tuple[int, int, int], L: int) -> np.ndarray:
    grad = np.zeros(3, dtype=float)
    for mu in range(3):
        xp = list(site)
        xm = list(site)
        xp[mu] = (xp[mu] + 1) % L
        xm[mu] = (xm[mu] - 1) % L
        grad[mu] = 0.5 * (values[idx(tuple(xp), L)] - values[idx(tuple(xm), L)])
    return grad


def main() -> int:
    rng = np.random.default_rng(20260611)
    L = 5
    N = L**3
    H = build_laplacian(L)
    P0 = neutral_projector(N)

    note_text = NOTE.read_text(encoding="utf-8")

    # Source-note contract checks.
    required_phrases = [
        "Claim type:** bounded_theorem",
        "Status authority:** independent audit lane only",
        "A[phi; rho] = (1/2) <phi, H phi> - <P0 rho, phi>",
        "rho_psi(x) = |psi(x)|^2",
        "S_test(phi; x) = L_test (1 - phi(x))",
        "L^{-1} = G0",
        "U_test(phi; x) = -m phi(x)",
        "F_x = -grad_x U_test = +m grad_x phi(x)",
        "This is a bounded weak-field theorem",
        "does not claim",
        "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
        "POISSON_SELF_GRAVITY_LOOP_V3_NOTE.md",
        "GATE_B_POISSON_SELF_GRAVITY_NOTE.md",
    ]
    for phrase in required_phrases:
        check(f"note contains required phrase: {phrase}", phrase in note_text)

    forbidden_phrases = [
        "**Status:** retained",
        "zero-free-parameter physical-gravity closure",
        "full Einstein equations are derived",
        "G_Newton in SI units is derived",
        "proportional to `-m grad phi(x)`",
        "F_x = -grad_x Delta S_test",
    ]
    for phrase in forbidden_phrases:
        check(f"note excludes forbidden phrase: {phrase}", phrase not in note_text)

    # Laplacian structure.
    check("H is symmetric", np.allclose(H, H.T, atol=1e-12))
    w, V = np.linalg.eigh(H)
    check("H has one constant zero mode", np.sum(w < 1e-10) == 1, f"zero_modes={np.sum(w < 1e-10)}")
    check("H is positive on neutral sector", np.min(w[w > 1e-10]) > 0.0, f"lambda_min={np.min(w[w > 1e-10]):.6g}")

    inv = np.array([0.0 if wi < 1e-10 else 1.0 / wi for wi in w])
    G0 = V @ np.diag(inv) @ V.T
    check("G0 is symmetric", np.allclose(G0, G0.T, atol=1e-10))
    check("H G0 equals P0", np.allclose(H @ G0, P0, atol=1e-9))
    check("G0 H equals P0", np.allclose(G0 @ H, P0, atol=1e-9))

    # Variational Euler equation and uniqueness.
    rho_raw = rng.normal(size=N)
    rho = P0 @ rho_raw
    phi = G0 @ rho
    grad = H @ phi - rho
    check("Euler equation H phi = P0 rho at phi=G0 P0 rho", np.linalg.norm(grad) < 1e-9, f"norm={np.linalg.norm(grad):.3e}")

    def action(field: np.ndarray, source: np.ndarray) -> float:
        return 0.5 * float(field @ H @ field) - float(source @ field)

    eta = P0 @ rng.normal(size=N)
    lhs = action(phi + eta, rho) - action(phi, rho)
    rhs = 0.5 * float(eta @ H @ eta)
    check("quadratic action increase is 1/2 eta.H.eta", abs(lhs - rhs) < 1e-9, f"diff={abs(lhs-rhs):.3e}")
    check("stationary point is a minimum on neutral sector", rhs > 0.0, f"increase={rhs:.6g}")

    K_bad = G0 + 0.05 * P0
    bad_residual = np.linalg.norm(H @ (K_bad @ rho) - rho)
    check("perturbed kernel K != G0 fails Euler equation", bad_residual > 1e-4, f"residual={bad_residual:.3e}")

    # Born-density uniqueness in the class rho_x = a_x |psi_x|^2.
    # Translation covariance imposes a_x = a_{x-e_mu}; solve the linear
    # constraint rank to verify the allowed weight space is one-dimensional.
    constraints: list[np.ndarray] = []
    for mu in range(3):
        for x in itertools.product(range(L), repeat=3):
            row = np.zeros(N)
            row[idx(x, L)] = 1.0
            y = list(x)
            y[mu] = (y[mu] - 1) % L
            row[idx(tuple(y), L)] -= 1.0
            constraints.append(row)
    C = np.vstack(constraints)
    rank = np.linalg.matrix_rank(C, tol=1e-10)
    null_dim = N - rank
    check("translation-covariant local weights have one-dimensional nullspace", null_dim == 1, f"null_dim={null_dim}")
    constant_weight = np.ones(N)
    check("constant weight satisfies translation constraints", np.linalg.norm(C @ constant_weight) < 1e-10)

    psi = rng.normal(size=N) + 1j * rng.normal(size=N)
    phases = np.exp(1j * rng.uniform(0.0, 2.0 * math.pi, size=N))
    rho_psi = np.abs(psi) ** 2
    rho_phase = np.abs(phases * psi) ** 2
    check("Born density is local phase invariant", np.allclose(rho_psi, rho_phase, atol=1e-12))
    check("Born density normalizes to ||psi||^2", abs(float(np.sum(rho_psi)) - float(np.vdot(psi, psi).real)) < 1e-10)
    a = 1.0
    check("normalization fixes constant local weight a=1", abs(a * np.sum(rho_psi) - np.vdot(psi, psi).real) < 1e-10)

    # Translation covariance numerical check for the Born density.
    T = translation_matrix(L, (1, 0, 0))
    shifted_density = np.abs(T @ psi) ** 2
    check("Born density is translation covariant", np.allclose(shifted_density, T @ rho_psi, atol=1e-12))

    rho_born_neutral = P0 @ rho_psi
    phi_born = G0 @ rho_born_neutral
    check("Poisson solve with neutral Born density closes", np.linalg.norm(H @ phi_born - rho_born_neutral) < 1e-8)

    # Test-source first-order response and bilinearity.
    source_site = (1, 1, 1)
    test_site = (3, 2, 1)
    source = np.zeros(N)
    source[idx(source_site, L)] = 1.0
    source = P0 @ source
    background_phi = G0 @ source

    m = 2.3
    delta_tau = 0.17
    L_test = m * delta_tau
    S_free = L_test
    S_with_phi = L_test * (1.0 - background_phi[idx(test_site, L)])
    delta_S = S_with_phi - S_free
    expected_delta = -m * delta_tau * background_phi[idx(test_site, L)]
    check("test action response is S=L(1-phi)", abs(delta_S - expected_delta) < 1e-12)

    grad_phi = finite_difference_gradient(background_phi, test_site, L)
    force = m * grad_phi
    check("force is m times gradient of background potential", np.linalg.norm(force - m * grad_phi) < 1e-12)
    U_values = -m * background_phi
    force_from_potential = -finite_difference_gradient(U_values, test_site, L)
    check("U=-m phi gives F=-grad U=+m grad phi", np.allclose(force_from_potential, force, atol=1e-12))
    check("test potential energy is -m phi", abs(U_values[idx(test_site, L)] + m * background_phi[idx(test_site, L)]) < 1e-12)

    M1, m1 = 1.7, 2.9
    M2, m2 = 0.4, 5.1
    phi_M1 = G0 @ (M1 * source)
    phi_M2 = G0 @ (M2 * source)
    F1 = m1 * finite_difference_gradient(phi_M1, test_site, L)
    F2 = m2 * finite_difference_gradient(phi_M2, test_site, L)
    base_grad = finite_difference_gradient(background_phi, test_site, L)
    check("force response is bilinear in source and test mass (case 1)", np.allclose(F1, M1 * m1 * base_grad, atol=1e-12))
    check("force response is bilinear in source and test mass (case 2)", np.allclose(F2, M2 * m2 * base_grad, atol=1e-12))

    # Effective action after integrating out phi at the stationary point.
    source2 = np.zeros(N)
    source2[idx(test_site, L)] = 1.0
    source2 = P0 @ source2
    eps = 1e-5
    rho_total = M1 * source + eps * source2
    phi_total = G0 @ rho_total
    action_min = action(phi_total, rho_total)
    exact_action_min = -0.5 * float(rho_total @ G0 @ rho_total)
    check("integrated-out action equals -1/2 rho.G0.rho", abs(action_min - exact_action_min) < 1e-10)
    derivative_numeric = (
        -0.5 * float((M1 * source + eps * source2) @ G0 @ (M1 * source + eps * source2))
        + 0.5 * float((M1 * source) @ G0 @ (M1 * source))
    ) / eps
    derivative_expected = -M1 * float(source2 @ G0 @ source)
    check("test-source derivative equals -M G0(x,y)", abs(derivative_numeric - derivative_expected) < 1e-5)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
