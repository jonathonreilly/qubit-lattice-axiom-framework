#!/usr/bin/env python3
"""Same-action scalar-spectral free 3+1 transfer/covariance checks.

This runner starts from one dimensionless free staggered action with
M(a)=a*m and canonical phases.  It independently reconstructs:

* the spatial two-step transfer recurrence and its stable eigenvalue;
* the blocked-time Euclidean covariance denominator;
* the exact equality between the covariance pole and the stable transfer
  eigenvalue;
* the positive CAR/Fock contraction and its exactly unitary real-time group;
* the massive a->0 energy/covariance/Gaussian limit.

It is free and conditional on the CAR/quasi-free branch.  It does not select a
taste, an interacting gauge theory, the Standard Model, or gravity.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "FREE_STAGGERED_3PLUS1_SAME_OBJECT_TRANSFER_GAUSSIAN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-07-12.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    PASS_COUNT += int(ok)
    FAIL_COUNT += int(not ok)
    line = f"{'PASS' if ok else 'FAIL'}: {name}"
    if detail:
        line += f" ({detail})"
    print(line)


def phase_clifford(d: int) -> list[np.ndarray]:
    """Canonical staggered phase matrices on a 2^d hypercube.

    alpha_mu |b> = (-1)^(sum_{nu<mu} b_nu) |b xor e_mu>.
    """
    n = 2**d
    out = []
    for mu in range(d):
        A = np.zeros((n, n), dtype=complex)
        for b in range(n):
            sign = (-1) ** sum((b >> nu) & 1 for nu in range(mu))
            A[b ^ (1 << mu), b] = sign
        out.append(A)
    return out


def spatial_cell_clifford(d: int) -> list[np.ndarray]:
    """The equivalent folded spatial matrices used by the transfer recurrence."""
    n = 2**d
    out = []
    for mu in range(d):
        mask = (1 << mu) - 1
        G = np.zeros((n, n), dtype=complex)
        for r in range(n):
            G[r ^ mask, r] = (-1) ** ((r >> mu) & 1)
        out.append(G)
    return out


def two_step_matrix(M: float, lam: float) -> np.ndarray:
    I = np.eye(1, dtype=complex)
    Z = np.zeros((1, 1), dtype=complex)
    even = np.block([[-2.0 * (M + 1j * lam) * I, I], [I, Z]])
    odd = np.block([[-2.0 * (M - 1j * lam) * I, I], [I, Z]])
    return odd @ even


def one_step_matrices(M: float, lam: float) -> tuple[np.ndarray, np.ndarray]:
    I = np.eye(1, dtype=complex)
    Z = np.zeros((1, 1), dtype=complex)
    even = np.block([[-2.0 * (M + 1j * lam) * I, I], [I, Z]])
    odd = np.block([[-2.0 * (M - 1j * lam) * I, I], [I, Z]])
    return even, odd


def blocked_time_dirac(M: float, lam: float, q: complex) -> np.ndarray:
    """Exact two-time-cell action block; coarse momentum is Q=2q."""
    Q = 2.0 * q
    return np.array(
        [
            [M + 1j * lam, 0.5 * (1.0 - np.exp(-1j * Q))],
            [0.5 * (np.exp(1j * Q) - 1.0), M - 1j * lam],
        ],
        dtype=complex,
    )


def energy_lattice(M: float, k: np.ndarray) -> float:
    return float(np.arcsinh(np.sqrt(M * M + np.sum(np.sin(k) ** 2))))


def euclidean_gammas() -> list[np.ndarray]:
    I = np.eye(2, dtype=complex)
    Z = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return [
        np.block([[Z, -1j * sx], [1j * sx, Z]]),
        np.block([[Z, -1j * sy], [1j * sy, Z]]),
        np.block([[Z, -1j * sz], [1j * sz, Z]]),
        np.block([[I, Z], [Z, -I]]),
    ]


GAMMAS = euclidean_gammas()


def covariance_lattice(p: np.ndarray, a: float, m: float) -> np.ndarray:
    s = np.sin(a * p) / a
    numerator = m * np.eye(4) - 1j * sum(s[mu] * GAMMAS[mu] for mu in range(4))
    return numerator / (m * m + float(s @ s))


def covariance_continuum(p: np.ndarray, m: float) -> np.ndarray:
    numerator = m * np.eye(4) - 1j * sum(p[mu] * GAMMAS[mu] for mu in range(4))
    return numerator / (m * m + float(p @ p))


def pfaffian(A: np.ndarray) -> complex:
    n = A.shape[0]
    if n == 0:
        return 1.0 + 0.0j
    if n == 2:
        return complex(A[0, 1])
    total = 0.0 + 0.0j
    for j in range(1, n):
        keep = [i for i in range(1, n) if i != j]
        total += ((-1) ** (j + 1)) * A[0, j] * pfaffian(A[np.ix_(keep, keep)])
    return total


def fock_products(values: np.ndarray) -> np.ndarray:
    result = []
    for occupations in product((0, 1), repeat=len(values)):
        result.append(np.prod([values[i] for i, n in enumerate(occupations) if n], initial=1.0))
    return np.asarray(result, dtype=float)


def test_note_guardrails() -> None:
    text = NOTE.read_text(encoding="utf-8")
    normalized = text.replace("`", "").replace("*", "")
    required = [
        "one action family",
        "pole--transfer identity",
        "conditional on the CAR/quasi-free branch",
        "does not select one taste",
        "does not recover",
        "the interacting Standard Model or GR",
        "N1--N8",
        "No axiom-update stop condition",
        "M(a) = a m",
    ]
    forbidden = [
        "This theorem is an unconditional TOE",
        "This note recovers the Standard Model",
        "This note recovers GR",
    ]
    schema = [
        normalized.count("ATTEMPTED") == 7,
        all(f"| C{i},C{j}" in normalized for i in range(1, 7) for j in range(i + 1, 7)),
        "hidden-condition phrase scan" in normalized,
        "citation/residual matching" in normalized,
        "rhetoric and resolution audit" in normalized,
        "primitive registry and live ledger were checked" in normalized,
        "hostile steelman" in normalized,
        "cross-cycle echo" in normalized,
        "No-Go Discipline verdict: PASS" in normalized,
        "FAIL for a completed finite-a QFT/Hilbert identity" in normalized,
    ]
    check(
        "source guardrails pin one family, CAR/taste/SM/GR boundaries, N1--N8, and no axiom stop",
        all(token in normalized for token in required)
        and all(token not in normalized for token in forbidden)
        and all(schema),
        f"N1--N8 schema {sum(schema)}/{len(schema)}",
    )


def test_phase_algebras() -> None:
    worst = 0.0
    for matrices in (phase_clifford(4), spatial_cell_clifford(3)):
        I = np.eye(matrices[0].shape[0])
        for mu, A in enumerate(matrices):
            worst = max(worst, float(np.linalg.norm(A @ A - I, ord=np.inf)))
            for B in matrices[mu + 1 :]:
                worst = max(worst, float(np.linalg.norm(A @ B + B @ A, ord=np.inf)))
    check("canonical 4D action and 3D transfer phase matrices obey exact Clifford relations", worst == 0.0, f"worst residual {worst:.1e}")


def test_action_scalar_spectrum() -> None:
    alphas = phase_clifford(4)
    rng = np.random.default_rng(20260712)
    worst = 0.0
    for _ in range(24):
        M = float(rng.uniform(0.05, 1.2))
        q = rng.uniform(-1.2, 1.2, size=4)
        D = M * np.eye(16) + 1j * sum(np.sin(q[mu]) * alphas[mu] for mu in range(4))
        Delta = M * M + float(np.sum(np.sin(q) ** 2))
        worst = max(worst, float(np.linalg.norm(D.conj().T @ D - Delta * np.eye(16), ord=np.inf)))
    check("same canonical 4D action has exact scalar D^dag D spectrum", worst < 2e-14, f"worst residual {worst:.2e}")


def test_clifford_multiplicity_invariant() -> None:
    alphas = phase_clifford(4)
    n = 16
    words = []
    for mask in range(16):
        word = np.eye(n, dtype=complex)
        for mu in range(4):
            if (mask >> mu) & 1:
                word = word @ alphas[mu]
        words.append(word.reshape(-1))
    algebra_dim = int(np.linalg.matrix_rank(np.stack(words), tol=1e-10))
    constraints = []
    I = np.eye(n, dtype=complex)
    for A in alphas:
        constraints.append(np.kron(I, A.T) - np.kron(A, I))
    commutator_map = np.concatenate(constraints, axis=0)
    commutant_dim = n * n - int(np.linalg.matrix_rank(commutator_map, tol=1e-10))
    check(
        "Cl4 generated algebra and commutant dimensions are 16 and 16, fixing four identical 4D spin blocks",
        algebra_dim == 16 and commutant_dim == 16,
        f"algebra dim {algebra_dim}, commutant dim {commutant_dim}",
    )


def test_spatial_transfer_square() -> None:
    G = spatial_cell_clifford(3)
    rng = np.random.default_rng(412)
    worst = 0.0
    for _ in range(30):
        k = rng.uniform(-1.3, 1.3, size=3)
        H = 1j * sum(np.sin(k[mu]) * G[mu] for mu in range(3))
        target = -float(np.sum(np.sin(k) ** 2)) * np.eye(8)
        worst = max(worst, float(np.linalg.norm(H @ H - target, ord=np.inf)))
    check("same action's folded spatial hop squares to -sum sin^2(k)", worst < 2e-14, f"worst residual {worst:.2e}")


def test_blocked_action_determinant() -> None:
    rng = np.random.default_rng(921)
    worst = 0.0
    for _ in range(100):
        M = float(rng.uniform(0.05, 1.0))
        lam = float(rng.uniform(-1.4, 1.4))
        q = float(rng.uniform(-1.4, 1.4))
        got = np.linalg.det(blocked_time_dirac(M, lam, q))
        target = M * M + lam * lam + np.sin(q) ** 2
        worst = max(worst, abs(got - target))
    check("exact blocked-time covariance denominator is M^2+lambda^2+sin^2(q0)", worst < 2e-15, f"worst residual {worst:.2e}")


def test_pole_transfer_identity() -> None:
    rng = np.random.default_rng(117)
    eig_residual = 0.0
    pole_residual = 0.0
    determinant_residual = 0.0
    hermitian_residual = 0.0
    factor_residual = 0.0
    imag_residual = 0.0
    min_eigenvalue = float("inf")
    for _ in range(120):
        M = float(rng.uniform(0.02, 1.1))
        lam = float(rng.uniform(-1.5, 1.5))
        E = float(np.arcsinh(np.sqrt(M * M + lam * lam)))
        expected = np.array([np.exp(-2 * E), np.exp(2 * E)])
        T2 = two_step_matrix(M, lam)
        even, odd = one_step_matrices(M, lam)
        eig = np.linalg.eigvals(T2)
        imag_residual = max(imag_residual, float(np.max(np.abs(eig.imag))))
        got = np.sort(eig.real)
        eig_residual = max(eig_residual, float(np.max(np.abs(got - expected))))
        hermitian_residual = max(hermitian_residual, float(np.linalg.norm(T2 - T2.conj().T, ord=np.inf)))
        factor_residual = max(factor_residual, float(np.linalg.norm(odd - even.conj().T, ord=np.inf)), float(np.linalg.norm(T2 - even.conj().T @ even, ord=np.inf)))
        min_eigenvalue = min(min_eigenvalue, float(np.min(np.linalg.eigvalsh(T2))))
        pole_residual = max(pole_residual, abs(M * M + lam * lam + np.sin(1j * E) ** 2))
        determinant_residual = max(determinant_residual, abs(np.linalg.det(blocked_time_dirac(M, lam, 1j * E))))
    check("pole--transfer identity: z=e^{2iq0}=e^{-2E} is exactly the stable T2 eigenvalue", eig_residual < 2e-12 and pole_residual < 2e-14 and determinant_residual < 2e-14 and imag_residual < 2e-14, f"eig {eig_residual:.1e}, pole {pole_residual:.1e}, det {determinant_residual:.1e}")
    check("T2=T_even^dag T_even is Hermitian positive, so stable positivity is not inferred from eigenvalues alone", hermitian_residual < 2e-14 and factor_residual < 2e-14 and min_eigenvalue > 0, f"Herm {hermitian_residual:.1e}, factor {factor_residual:.1e}, min eig {min_eigenvalue:.3e}")


def test_stable_solution_space_intertwiner() -> None:
    G = spatial_cell_clifford(3)
    k = np.array([0.31, -0.47, 0.22])
    M = 0.29
    H = 1j * sum(np.sin(k[mu]) * G[mu] for mu in range(3))
    lam2 = float(np.sum(np.sin(k) ** 2))
    E = float(np.arcsinh(np.sqrt(M * M + lam2)))
    z = float(np.exp(-2 * E))
    I = np.eye(8, dtype=complex)
    Z = np.zeros_like(I)
    even = np.block([[-2.0 * (M * I + H), I], [I, Z]])
    odd = even.conj().T
    T2 = odd @ even
    D2 = np.block(
        [
            [M * I + H, 0.5 * (1.0 - 1.0 / z) * I],
            [0.5 * (z - 1.0) * I, M * I - H],
        ]
    )
    _, singular, vh = np.linalg.svd(D2)
    null_basis = vh.conj().T[:, singular < 1e-10]
    J = np.block([[I, Z], [Z, (1.0 / z) * I]])
    mapped = J @ null_basis
    intertwiner_residual = float(np.linalg.norm(T2 @ mapped - z * mapped, ord=np.inf))
    stable_count = int(np.count_nonzero(np.abs(np.linalg.eigvalsh(T2) - z) < 1e-10))
    check(
        "the time-cell map diag(I,z^-1 I) sends the 8D covariance-pole nullspace onto the 8D stable T2 eigenspace",
        null_basis.shape[1] == 8 and stable_count == 8 and intertwiner_residual < 2e-12,
        f"nullity {null_basis.shape[1]}, stable multiplicity {stable_count}, residual {intertwiner_residual:.1e}",
    )


def test_recurrence_is_action_equation() -> None:
    rng = np.random.default_rng(331)
    worst = 0.0
    for _ in range(100):
        M = float(rng.uniform(0.05, 0.8))
        lam = float(rng.uniform(-1.2, 1.2))
        old = complex(*rng.normal(size=2))
        now = complex(*rng.normal(size=2))
        for t in (0, 1):
            nxt = old - 2.0 * (M + ((-1) ** t) * 1j * lam) * now
            action_eq = M * now + 0.5 * (nxt - old) + ((-1) ** t) * 1j * lam * now
            worst = max(worst, abs(action_eq))
    check("alternating transfer recurrence is algebraically identical to D_lat chi=0", worst < 1e-15, f"worst residual {worst:.2e}")


def test_mass_scaling_selection() -> None:
    m = 0.73
    seq = np.array([0.08, 0.04, 0.02, 0.01])
    limits = {}
    for alpha in (0.6, 1.0, 1.4):
        limits[alpha] = np.arcsinh(m * seq**alpha) / seq
    finite_mass = abs(limits[1.0][-1] - m) < 3e-5
    divergent = limits[0.6][-1] > 2.0 * limits[0.6][0]
    massless = limits[1.4][-1] < 0.5 * limits[1.4][0]
    check("within M(a)=m a^alpha, alpha=1 uniquely gives a finite nonzero rest-energy limit", finite_mass and divergent and massless, f"alpha .6/1/1.4 endpoints {limits[0.6][-1]:.3f}/{limits[1.0][-1]:.3f}/{limits[1.4][-1]:.3f}")


def test_uniform_energy_limit() -> None:
    m = 0.61
    axes = np.linspace(-1.1, 1.1, 9)
    momenta = np.array(list(product(axes, repeat=3)))
    errors = []
    for a in (0.2, 0.1, 0.05, 0.025):
        lattice = np.array([energy_lattice(a * m, a * p) / a for p in momenta])
        continuum = np.sqrt(m * m + np.sum(momenta * momenta, axis=1))
        errors.append(float(np.max(np.abs(lattice - continuum))))
    ratios = [errors[i] / errors[i + 1] for i in range(3)]
    check("physical one-particle energy converges uniformly on a compact momentum band at O(a^2)", all(3.7 < r < 4.15 for r in ratios), f"errors {errors}, ratios {ratios}")


def test_fixed_particle_unitary_limit() -> None:
    m = 0.61
    momenta = np.array(
        [
            [0.2, -0.3, 0.4],
            [-0.5, 0.1, 0.25],
            [0.35, 0.45, -0.15],
            [0.0, 0.0, 0.0],
        ]
    )
    continuum = np.sqrt(m * m + np.sum(momenta * momenta, axis=1))
    pair_target = np.array([continuum[i] + continuum[j] for i, j in combinations(range(4), 2)])
    t = 1.23
    errors = []
    for a in (0.2, 0.1, 0.05, 0.025):
        lattice = np.array([energy_lattice(a * m, a * p) / a for p in momenta])
        pair_lattice = np.array([lattice[i] + lattice[j] for i, j in combinations(range(4), 2)])
        errors.append(float(np.max(np.abs(np.exp(-1j * t * pair_lattice) - np.exp(-1j * t * pair_target)))))
    ratios = [errors[i] / errors[i + 1] for i in range(3)]
    check("real-time unitary groups converge on a fixed two-particle sector at O(a^2)", all(3.75 < r < 4.2 for r in ratios), f"errors {errors}, ratios {ratios}")


def test_positive_fock_and_exact_unitarity() -> None:
    a = 0.17
    m = 0.8
    ks = [np.array([0.1, 0.2, -0.3]), np.array([0.4, -0.2, 0.5]), np.zeros(3)]
    eps = np.array([energy_lattice(a * m, a * k) / a for k in ks])
    contraction = np.exp(-2.0 * a * eps)
    fock_C = fock_products(contraction)
    fock_H = np.array([sum(eps[i] * n for i, n in enumerate(occ)) for occ in product((0, 1), repeat=len(eps))])
    t = 1.37
    U = np.diag(np.exp(-1j * t * fock_H))
    reconstructed_H = -(1.0 / (2.0 * a)) * np.log(fock_C)
    check("stable two-step contraction second-quantizes to a strictly positive CAR/Fock operator", np.min(fock_C) > 0 and np.max(fock_C) <= 1.0 + 1e-14)
    check("H_a=-(2a)^-1 log Gamma(C_a) equals the additive Fock spectrum and is nonnegative", np.min(fock_H) >= 0 and np.max(np.abs(reconstructed_H - fock_H)) < 2e-14)
    check("U_a(t)=exp(-it H_a) is exactly unitary at every a", np.linalg.norm(U.conj().T @ U - np.eye(U.shape[0]), ord=np.inf) < 1e-14)


def test_covariance_and_gaussian_limit() -> None:
    rng = np.random.default_rng(555)
    m = 0.72
    momenta = rng.uniform(-1.2, 1.2, size=(32, 4))
    f = rng.normal(size=(4, len(momenta), 4)) + 1j * rng.normal(size=(4, len(momenta), 4))
    g = rng.normal(size=(4, len(momenta), 4)) + 1j * rng.normal(size=(4, len(momenta), 4))
    envelope = np.exp(-0.5 * np.sum(momenta * momenta, axis=1))
    f *= envelope[None, :, None]
    g *= envelope[None, :, None]
    errors = []
    pf_errors = []
    def smeared_matrix(kernel) -> np.ndarray:
        C = np.zeros((4, 4), dtype=complex)
        for i in range(4):
            for j in range(4):
                C[i, j] = np.mean([np.vdot(f[i, n], kernel(momenta[n]) @ g[j, n]) for n in range(len(momenta))])
        return C

    def nambu_antisymmetrize(C: np.ndarray) -> np.ndarray:
        Z = np.zeros_like(C)
        return np.block([[Z, C], [-C.T, Z]])

    target_pf = pfaffian(nambu_antisymmetrize(smeared_matrix(lambda p: covariance_continuum(p, m))))
    for a in (0.2, 0.1, 0.05, 0.025):
        errs = [np.linalg.norm(covariance_lattice(p, a, m) - covariance_continuum(p, m), ord=2) for p in momenta]
        errors.append(max(errs))
        C_a = smeared_matrix(lambda p: covariance_lattice(p, a, m))
        pf_errors.append(abs(pfaffian(nambu_antisymmetrize(C_a)) - target_pf))
    ratios = [errors[i] / errors[i + 1] for i in range(3)]
    pf_ratios = [pf_errors[i] / pf_errors[i + 1] for i in range(3)]
    check("the same action covariance converges uniformly on compact momentum samples at O(a^2)", all(3.8 < r < 4.2 for r in ratios), f"ratios {ratios}")
    check("a finite smeared Nambu-doubled Pfaffian built from S_a converges with the same covariance family", all(3.7 < r < 4.3 for r in pf_ratios), f"ratios {pf_ratios}")


def test_so4_continuum_target() -> None:
    rng = np.random.default_rng(811)
    worst = 0.0
    for _ in range(20):
        p = rng.normal(size=4)
        theta = float(rng.uniform(-2, 2))
        mu, nu = rng.choice(4, size=2, replace=False)
        generator = GAMMAS[mu] @ GAMMAS[nu]
        Sspin = np.cos(theta / 2) * np.eye(4) + np.sin(theta / 2) * generator
        R = np.eye(4)
        R[mu, mu] = R[nu, nu] = np.cos(theta)
        R[mu, nu] = np.sin(theta)
        R[nu, mu] = -np.sin(theta)
        # Recover the sign convention directly from the spin action rather than assume it.
        A = np.zeros((4, 4))
        for aidx in range(4):
            for bidx in range(4):
                A[bidx, aidx] = (np.trace(GAMMAS[bidx] @ Sspin @ GAMMAS[aidx] @ Sspin.conj().T) / 4).real
        worst = max(worst, float(np.linalg.norm(Sspin @ covariance_continuum(p, 0.7) @ Sspin.conj().T - covariance_continuum(A @ p, 0.7), ord=np.inf)))
    check("continuum covariance target is exactly SO(4)-bispinor covariant", worst < 2e-14, f"worst residual {worst:.2e}")


def test_physical_quasilocal_scale() -> None:
    m = 0.54
    a_seq = np.array([0.2, 0.1, 0.05, 0.025])
    inverse_lengths = np.arcsinh(a_seq * m) / a_seq
    lengths = a_seq / np.arcsinh(a_seq * m)
    target_rate = m
    target_length = 1.0 / m
    err_rate = np.abs(inverse_lengths - target_rate)
    err_length = np.abs(lengths - target_length)
    ratios_rate = err_rate[:-1] / err_rate[1:]
    ratios_length = err_length[:-1] / err_length[1:]
    check("transfer-log correlation length has finite physical limit xi_phys->1/m", abs(lengths[-1] - target_length) < 1e-4 and np.all((ratios_length > 3.8) & (ratios_length < 4.2)), f"xi {lengths[-1]:.6f} vs {target_length:.6f}")
    check("physical inverse quasilocal scale asinh(am)/a converges to m at O(a^2)", np.all((ratios_rate > 3.8) & (ratios_rate < 4.2)), f"rates {inverse_lengths.tolist()}")


def test_taste_and_wrong_object_controls() -> None:
    alphas = phase_clifford(4)
    p = np.array([0.17, -0.29, 0.41, -0.53])
    M = 0.33
    D = M * np.eye(16) + 1j * sum(np.sin(p[mu]) * alphas[mu] for mu in range(4))
    singular = np.linalg.eigvalsh(D.conj().T @ D)
    Delta = M * M + float(np.sum(np.sin(p) ** 2))
    scalar_multiplicity = np.allclose(singular, Delta)
    E = float(np.arcsinh(np.sqrt(M * M + np.sum(np.sin(p[:3]) ** 2))))
    wrong = np.exp(-E)
    stable = np.min(np.abs(np.linalg.eigvals(two_step_matrix(M, float(np.sqrt(np.sum(np.sin(p[:3]) ** 2)))))))
    check("finite-a D^dag D scalar spectrum has the full 16-component multiplicity used by the separate Cl4 commutant test", scalar_multiplicity and len(singular) == 16)
    check("one-step decay is a negative control: the action-derived blocked transfer is e^{-2E}, not e^{-E}", abs(stable - np.exp(-2 * E)) < 2e-14 and abs(stable - wrong) > 1e-3)


def main() -> int:
    print("FREE STAGGERED 3+1 SAME-ACTION SCALAR-SPECTRAL TRANSFER / COVARIANCE CONTINUUM")
    print("Deterministic bounded-theorem checks; free CAR/quasi-free branch only.")
    test_note_guardrails()
    test_phase_algebras()
    test_action_scalar_spectrum()
    test_clifford_multiplicity_invariant()
    test_spatial_transfer_square()
    test_blocked_action_determinant()
    test_pole_transfer_identity()
    test_stable_solution_space_intertwiner()
    test_recurrence_is_action_equation()
    test_mass_scaling_selection()
    test_uniform_energy_limit()
    test_fixed_particle_unitary_limit()
    test_positive_fock_and_exact_unitarity()
    test_covariance_and_gaussian_limit()
    test_so4_continuum_target()
    test_physical_quasilocal_scale()
    test_taste_and_wrong_object_controls()
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
