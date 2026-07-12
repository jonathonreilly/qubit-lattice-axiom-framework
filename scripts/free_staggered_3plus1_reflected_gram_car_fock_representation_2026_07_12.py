#!/usr/bin/env python3
"""Exact free 3+1 staggered reflected-Gram / CAR-Fock representation.

For the infinite temporal lattice at fixed spacing and a finite even 3D
spatial torus, derive the reflected two-slice Berezin Gram from the same
blocked covariance used by the action-derived transfer.  Mode by mode the
Gram is rank one with nonzero eigenvalue 2 exp(-2E).  The induced partial
isometry W obeys K_n = 2 W^dag C^n W, and exterior powers turn the Gaussian
Wick determinants into CAR-Fock matrix elements of Gamma(C)^n.

Free U=1 and supplied CAR/Grassmann branch only.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md"

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


def energy_and_z(M: float, lam: float) -> tuple[float, float]:
    E = float(np.arcsinh(np.sqrt(M * M + lam * lam)))
    return E, float(np.exp(-2.0 * E))


def blocked_dirac(M: float, lam: float, z: complex) -> np.ndarray:
    return np.array(
        [
            [M + 1j * lam, 0.5 * (1.0 - 1.0 / z)],
            [0.5 * (z - 1.0), M - 1j * lam],
        ],
        dtype=complex,
    )


def two_step(M: float, lam: float) -> np.ndarray:
    even = np.array([[-2.0 * (M + 1j * lam), 1.0], [1.0, 0.0]], dtype=complex)
    return even.conj().T @ even


def covariance_residue_cell_step(M: float, lam: float) -> np.ndarray:
    """Residue giving G(cell separation +1) for the blocked covariance.

    With z=e^{iQ}, D(z)^-1 has the inside pole z_-=exp(-2E) and reciprocal
    outside pole z_+=1/z_-.  For cell separation one, the Fourier coefficient
    is the residue of D(z)^-1 itself at z_-.
    """
    _, z = energy_and_z(M, lam)
    d = z - 1.0 / z
    a = M + 1j * lam
    return np.array(
        [
            [-4.0 * z * np.conj(a), 2.0 * (z - 1.0)],
            [2.0 * z * (z - 1.0), -4.0 * z * a],
        ],
        dtype=complex,
    ) / d


def reflected_gram_from_residue(residue: np.ndarray) -> np.ndarray:
    """K_ab=<Theta chi_a chi_b>, a,b in {0,1}, theta(t)=-1-t.

    The residue is ordered by target (even,odd) and source (even,odd).  The
    reflected sources for a=(0,1) are (odd,even) in the previous cell.
    """
    return np.array(
        [
            [residue[0, 1], residue[1, 1]],
            [residue[0, 0], residue[1, 0]],
        ],
        dtype=complex,
    )


def reflected_gram(M: float, lam: float) -> np.ndarray:
    _, z = energy_and_z(M, lam)
    d = z - 1.0 / z
    return np.array(
        [
            [2.0 * (z - 1.0), -4.0 * z * (M + 1j * lam)],
            [-4.0 * z * (M - 1j * lam), 2.0 * z * (z - 1.0)],
        ],
        dtype=complex,
    ) / d


def open_chain_reflected_gram(M: float, lam: float, Nt: int, block_separation: int = 1) -> np.ndarray:
    tmin = -Nt
    Lt = 2 * Nt
    D = np.zeros((Lt, Lt), dtype=complex)
    for t in range(tmin, Nt):
        i = t - tmin
        D[i, i] = M + 1j * ((-1) ** t) * lam
        if t + 1 < Nt:
            D[i, t + 1 - tmin] += 0.5
        if t - 1 >= tmin:
            D[i, t - 1 - tmin] -= 0.5
    G = np.linalg.inv(D)
    K = np.zeros((2, 2), dtype=complex)
    target_shift = 2 * (block_separation - 1)
    for a, ta in enumerate((0, 1)):
        for b, tb in enumerate((0, 1)):
            K[a, b] = G[target_shift + tb - tmin, (-1 - ta) - tmin]
    return K


def coord_to_index(x: tuple[int, ...], L: int) -> int:
    idx = 0
    stride = 1
    for value in x:
        idx += value * stride
        stride *= L
    return idx


def index_to_coord(idx: int, d: int, L: int) -> tuple[int, ...]:
    out = []
    for _ in range(d):
        out.append(idx % L)
        idx //= L
    return tuple(out)


def spatial_hop_3d(L: int) -> np.ndarray:
    V = L**3
    H = np.zeros((V, V), dtype=complex)
    for site in range(V):
        x = list(index_to_coord(site, 3, L))
        for mu in range(3):
            eta = (-1) ** sum(x[:mu])
            xp = x.copy()
            xm = x.copy()
            xp[mu] = (xp[mu] + 1) % L
            xm[mu] = (xm[mu] - 1) % L
            H[site, coord_to_index(tuple(xp), L)] += 0.5 * eta
            H[site, coord_to_index(tuple(xm), L)] -= 0.5 * eta
    return H


def parity_involution_3d(L: int) -> np.ndarray:
    values = []
    for site in range(L**3):
        x = index_to_coord(site, 3, L)
        values.append((-1) ** sum(x))
    return np.diag(values).astype(complex)


def modal_representation(M: float, lambdas: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return K, C, W in mode-major block ordering with K=2 W^dag C W."""
    n = len(lambdas)
    K = np.zeros((2 * n, 2 * n), dtype=complex)
    W = np.zeros((n, 2 * n), dtype=complex)
    zvals = np.zeros(n, dtype=float)
    for j, lam in enumerate(lambdas):
        Kj = reflected_gram(M, float(lam))
        vals, vecs = np.linalg.eigh(Kj)
        w = vecs[:, np.argmax(vals)]
        _, z = energy_and_z(M, float(lam))
        K[2 * j : 2 * j + 2, 2 * j : 2 * j + 2] = Kj
        W[j, 2 * j : 2 * j + 2] = np.conj(w)
        zvals[j] = z
    return K, np.diag(zvals), W


def wedge_coordinates(vectors: np.ndarray, degree: int) -> tuple[list[tuple[int, ...]], np.ndarray]:
    """Coordinates of v1 wedge ... wedge vr; vectors has columns v_i."""
    basis = list(combinations(range(vectors.shape[0]), degree))
    coords = np.array([np.linalg.det(vectors[np.ix_(subset, range(degree))]) for subset in basis])
    return basis, coords


def exterior_diagonal(diagonal: np.ndarray, degree: int) -> np.ndarray:
    return np.array([np.prod(diagonal[list(subset)]) for subset in combinations(range(len(diagonal)), degree)])


def test_note_guardrails() -> None:
    raw = NOTE.read_text(encoding="utf-8").replace("`", "").replace("*", "")
    text = " ".join(raw.split())
    required = [
        "infinite temporal lattice",
        "finite even 3D spatial torus",
        "K_n = 2 W^dag C^n W",
        "conditional on the CAR/Grassmann branch",
        "does not select CAR",
        "does not recover the interacting Standard Model or GR",
        "No axiom-update stop condition",
        "No-Go Discipline verdict: PASS",
    ]
    schema = [
        text.count("ATTEMPTED") == 7,
        all(f"| C{i},C{j}" in text for i in range(1, 7) for j in range(i + 1, 7)),
        "hidden-condition phrase scan" in text,
        "citation/residual matching" in text,
        "rhetoric and resolution audit" in text,
        "primitive registry and live ledger were checked" in text,
        "hostile steelman" in text,
        "cross-cycle echo" in text,
    ]
    check("source scope and full N1--N8 schema are pinned", all(x in text for x in required) and all(schema), f"schema {sum(schema)}/{len(schema)}")


def test_poles_and_transfer() -> None:
    rng = np.random.default_rng(1201)
    det_res = 0.0
    eig_res = 0.0
    for _ in range(100):
        M = float(rng.uniform(0.03, 1.2))
        lam = float(rng.uniform(-1.5, 1.5))
        E, z = energy_and_z(M, lam)
        det_res = max(det_res, abs(np.linalg.det(blocked_dirac(M, lam, z))))
        eig = np.sort(np.linalg.eigvalsh(two_step(M, lam)))
        eig_res = max(eig_res, float(np.max(np.abs(eig - [z, 1.0 / z]))))
    check("blocked covariance inside pole and positive T2 stable eigenvalue are the same z=e^-2E", det_res < 2e-14 and eig_res < 2e-12, f"det {det_res:.1e}, eig {eig_res:.1e}")


def test_residue_formula() -> None:
    rng = np.random.default_rng(1202)
    worst = 0.0
    for _ in range(100):
        M = float(rng.uniform(0.03, 1.2))
        lam = float(rng.uniform(-1.5, 1.5))
        K1 = reflected_gram_from_residue(covariance_residue_cell_step(M, lam))
        K2 = reflected_gram(M, lam)
        worst = max(worst, float(np.linalg.norm(K1 - K2, ord=np.inf)))
    check("covariance residue with theta(t)=-1-t gives the closed reflected two-slice Gram", worst < 2e-14, f"worst residual {worst:.1e}")


def test_rank_one_projector() -> None:
    rng = np.random.default_rng(1203)
    herm = 0.0
    eig = 0.0
    proj = 0.0
    for _ in range(100):
        M = float(rng.uniform(0.01, 1.2))
        lam = float(rng.uniform(-1.5, 1.5))
        _, z = energy_and_z(M, lam)
        K = reflected_gram(M, lam)
        herm = max(herm, float(np.linalg.norm(K - K.conj().T, ord=np.inf)))
        eig = max(eig, float(np.max(np.abs(np.linalg.eigvalsh(K) - [0.0, 2.0 * z]))))
        P = K / (2.0 * z)
        proj = max(proj, float(np.linalg.norm(P @ P - P, ord=np.inf)))
    check("mode Gram is Hermitian PSD rank one with eigenvalues {0,2z}", herm < 2e-14 and eig < 2e-13, f"Herm {herm:.1e}, eig {eig:.1e}")
    check("K/(2z) is the exact orthogonal positive-time OS support projector", proj < 2e-13, f"projector residual {proj:.1e}")


def test_open_chain_limit() -> None:
    cases = [(0.5, 0.0), (0.5, 0.3), (0.5, -0.7), (0.8, 1.1)]
    worst32 = 0.0
    raw_hermitian = 0.0
    contraction = True
    for M, lam in cases:
        target = reflected_gram(M, lam)
        finite = [open_chain_reflected_gram(M, lam, Nt) for Nt in (8, 16, 32)]
        raw_hermitian = max(raw_hermitian, *(float(np.linalg.norm(item - item.conj().T, ord=np.inf)) for item in finite))
        errs = [float(np.linalg.norm(item - target, ord=np.inf)) for item in finite]
        contraction &= errs[2] < errs[1] < errs[0]
        worst32 = max(worst32, errs[-1])
    check("raw finite open-chain Grams are Hermitian and converge exponentially to the exact infinite-time Gram", raw_hermitian < 2e-13 and contraction and worst32 < 2e-12, f"raw Herm {raw_hermitian:.1e}, worst Nt=32 {worst32:.1e}")


def test_full_3d_modal_lift() -> None:
    H = spatial_hop_3d(4)
    anti = float(np.linalg.norm(H + H.conj().T, ord=np.inf))
    lambdas, U = np.linalg.eigh(-1j * H)
    K, C, W = modal_representation(0.37, lambdas)
    partial = float(np.linalg.norm(W @ W.conj().T - np.eye(len(lambdas)), ord=np.inf))
    representation = float(np.linalg.norm(K - 2.0 * W.conj().T @ C @ W, ord=np.inf))
    eig_match = float(np.max(np.abs(np.sort(np.linalg.eigvalsh(K)[np.linalg.eigvalsh(K) > 1e-10]) - np.sort(2.0 * np.diag(C)))))
    check("canonical finite 3D spatial hop is anti-Hermitian and unitarily mode-decomposable", anti < 1e-14 and np.linalg.norm(U.conj().T @ U - np.eye(len(lambdas))) < 1e-13, f"anti residual {anti:.1e}")
    check("full 3D reflected Gram obeys K=2 W^dag C W with W a coisometry", partial < 2e-13 and representation < 2e-13, f"WWdag {partial:.1e}, representation {representation:.1e}")
    check("full 3D positive Gram spectrum is exactly twice the stable transfer spectrum", eig_match < 2e-13, f"eigenvalue residual {eig_match:.1e}")

    # Position-basis conjugation: both independently transformed objects still agree.
    Ub = np.kron(U, np.eye(2))
    Kpos = Ub @ K @ Ub.conj().T
    Cpos = U @ C @ U.conj().T
    Wpos = U @ W @ Ub.conj().T
    pos_res = float(np.linalg.norm(Kpos - 2.0 * Wpos.conj().T @ Cpos @ Wpos, ord=np.inf))
    check("the representation equality survives the full position-basis transform with all cross-mode contractions", pos_res < 5e-13, f"position residual {pos_res:.1e}")


def test_basis_independent_operator_formula() -> None:
    L = 4
    M = 0.37
    H = spatial_hop_3d(L)
    n = H.shape[0]
    lambdas, U = np.linalg.eigh(-1j * H)
    r = np.sqrt(M * M + lambdas * lambdas)
    z = np.exp(-2.0 * np.arcsinh(r))
    Rinv = U @ np.diag(1.0 / r) @ U.conj().T
    Z = U @ np.diag(z) @ U.conj().T
    sqrtZ = U @ np.diag(np.sqrt(z)) @ U.conj().T
    invsqrt1pZ = U @ np.diag(1.0 / np.sqrt(1.0 + z)) @ U.conj().T
    B = (M * np.eye(n) + H) @ Rinv
    V = np.vstack([np.eye(n), sqrtZ @ B.conj().T]) @ invsqrt1pZ
    Upole = np.vstack([np.eye(n), sqrtZ @ B]) @ invsqrt1pZ
    Wstable = np.vstack([sqrtZ, B]) @ invsqrt1pZ
    Kclosed = 2.0 * V @ Z @ V.conj().T

    # Convert the independent mode-major construction to component-first position order.
    Kmode, _, _ = modal_representation(M, lambdas)
    perm = np.zeros((2 * n, 2 * n))
    for j in range(n):
        for s in range(2):
            perm[s * n + j, 2 * j + s] = 1.0
    U2 = np.block([[U, np.zeros_like(U)], [np.zeros_like(U), U]])
    Kindependent = U2 @ perm @ Kmode @ perm.T @ U2.conj().T

    I = np.eye(n, dtype=complex)
    Z0 = np.zeros_like(I)
    Teven = np.block([[-2.0 * (M * I + H), I], [I, Z0]])
    T2 = Teven.conj().T @ Teven
    J = np.block([[I, Z0], [Z0, np.linalg.inv(Z)]])
    Pi = parity_involution_3d(L)
    Pi2 = np.block([[Pi, Z0], [Z0, Pi]])
    Lmap = Wstable @ Pi @ V.conj().T

    formula_res = float(np.linalg.norm(Kclosed - Kindependent, ord=np.inf))
    isometry_res = max(
        float(np.linalg.norm(B.conj().T @ B - I, ord=np.inf)),
        float(np.linalg.norm(V.conj().T @ V - I, ord=np.inf)),
        float(np.linalg.norm(Upole.conj().T @ Upole - I, ord=np.inf)),
        float(np.linalg.norm(Wstable.conj().T @ Wstable - I, ord=np.inf)),
    )
    stable_res = float(np.linalg.norm(T2 @ Wstable - Wstable @ Z, ord=np.inf))
    polar_res = float(np.linalg.norm(J @ Upole - Wstable @ np.linalg.inv(sqrtZ), ord=np.inf))
    parity_res = max(
        float(np.linalg.norm(Pi @ H @ Pi + H, ord=np.inf)),
        float(np.linalg.norm(V - Pi2 @ Upole @ Pi, ord=np.inf)),
    )
    intertwine_res = float(np.linalg.norm(Lmap @ (Kclosed / 2.0) - T2 @ Lmap, ord=np.inf))

    check("basis-independent formula K=2 V Z V^dag matches the independent full 3D modal residue construction", formula_res < 2e-12, f"residual {formula_res:.1e}")
    check("pole, OS, and stable frames are exact isometries and T2 Wstable=Wstable Z", isometry_res < 2e-12 and stable_res < 2e-12, f"isometry {isometry_res:.1e}, stable {stable_res:.1e}")
    check("Block13 map has exact polar form J_Z Upole=Wstable Z^-1/2", polar_res < 5e-12, f"residual {polar_res:.1e}")
    check("canonical staggered parity flips H and conjugates the pole frame into the OS frame", parity_res < 3e-12, f"residual {parity_res:.1e}")
    check("partial unitary L=Wstable Pi V^dag intertwines K/2 with the positive transfer T2", intertwine_res < 5e-12, f"residual {intertwine_res:.1e}")


def test_os_quotient_factorization() -> None:
    lambdas = np.array([-1.1, -0.4, 0.0, 0.35, 0.9])
    K, C, W = modal_representation(0.43, lambdas)
    sqrtC = np.diag(np.sqrt(np.diag(C)))
    A = np.sqrt(2.0) * sqrtC @ W
    factor = float(np.linalg.norm(K - A.conj().T @ A, ord=np.inf))
    singular = np.linalg.svd(A, compute_uv=False)
    check("K=A^dag A gives the exact positive OS quotient map with rank equal to the spatial one-particle space", factor < 2e-13 and len(singular) == len(lambdas) and np.min(singular) > 0, f"factor {factor:.1e}, min singular {np.min(singular):.3e}")


def test_semigroup_grams() -> None:
    lambdas = np.array([-1.0, -0.3, 0.0, 0.45, 1.2])
    K, C, W = modal_representation(0.52, lambdas)
    worst = 0.0
    open_chain_worst = 0.0
    for n in range(1, 7):
        Kn = np.zeros_like(K)
        for j, lam in enumerate(lambdas):
            _, z = energy_and_z(0.52, float(lam))
            Kn[2 * j : 2 * j + 2, 2 * j : 2 * j + 2] = (z ** (n - 1)) * reflected_gram(0.52, float(lam))
        expected = 2.0 * W.conj().T @ np.linalg.matrix_power(C, n) @ W
        worst = max(worst, float(np.linalg.norm(Kn - expected, ord=np.inf)))
        if n <= 4:
            exact_mode = (energy_and_z(0.52, float(lambdas[1]))[1] ** (n - 1)) * reflected_gram(0.52, float(lambdas[1]))
            finite_mode = open_chain_reflected_gram(0.52, float(lambdas[1]), 48, n)
            open_chain_worst = max(open_chain_worst, float(np.linalg.norm(finite_mode - exact_mode, ord=np.inf)))
    check("all blocked-time reflected two-point Grams obey K_n=2 W^dag C^n W", worst < 3e-13 and open_chain_worst < 2e-12, f"operator {worst:.1e}, independent open-chain n=1..4 {open_chain_worst:.1e}")


def test_wick_to_fock_exterior_powers() -> None:
    rng = np.random.default_rng(1204)
    lambdas = np.array([-1.15, -0.63, -0.21, 0.18, 0.55, 1.05])
    K, C, W = modal_representation(0.48, lambdas)
    worst_pair = 0.0
    worst_det = 0.0
    worst_wedge = 0.0
    worst_os_pair = 0.0
    worst_multitime_wedge = 0.0
    sqrtC = np.diag(np.sqrt(np.diag(C)))
    A = np.sqrt(2.0) * sqrtC @ W
    for n in (1, 2, 4):
        Cn = np.linalg.matrix_power(C, n)
        Kn = 2.0 * W.conj().T @ Cn @ W
        for degree in (1, 2, 3):
            F = rng.normal(size=(2 * len(lambdas), degree)) + 1j * rng.normal(size=(2 * len(lambdas), degree))
            G = rng.normal(size=(2 * len(lambdas), degree)) + 1j * rng.normal(size=(2 * len(lambdas), degree))
            Phi = np.sqrt(2.0) * W @ F
            Psi = np.sqrt(2.0) * W @ G
            berezin_pairs = F.conj().T @ Kn @ G
            operator_pairs = Phi.conj().T @ Cn @ Psi
            worst_pair = max(worst_pair, float(np.linalg.norm(berezin_pairs - operator_pairs, ord=np.inf)))
            wick_det = np.linalg.det(berezin_pairs)
            operator_det = np.linalg.det(operator_pairs)
            worst_det = max(worst_det, abs(wick_det - operator_det))
            _, wedge_phi = wedge_coordinates(Phi, degree)
            _, wedge_psi = wedge_coordinates(Psi, degree)
            Cext = exterior_diagonal(np.diag(Cn), degree)
            wedge_value = np.vdot(wedge_phi, Cext * wedge_psi)
            worst_wedge = max(worst_wedge, abs(wick_det - wedge_value))
            # Canonical OS quotient factorization: K_n=A^dag Z^(n-1) A.
            os_pairs = F.conj().T @ A.conj().T @ np.linalg.matrix_power(C, n - 1) @ A @ G
            worst_os_pair = max(worst_os_pair, float(np.linalg.norm(berezin_pairs - os_pairs, ord=np.inf)))

            # Arbitrary positive block times r_i,s_j, not just two common-time clusters.
            r_times = np.arange(degree, dtype=int)
            s_times = np.arange(degree - 1, -1, -1, dtype=int)
            multi_pairs = np.zeros((degree, degree), dtype=complex)
            Xi = np.zeros((len(lambdas), degree), dtype=complex)
            Eta = np.zeros((len(lambdas), degree), dtype=complex)
            for i in range(degree):
                Xi[:, i] = np.linalg.matrix_power(C, int(r_times[i])) @ A @ F[:, i]
            for j in range(degree):
                Eta[:, j] = np.linalg.matrix_power(C, int(s_times[j])) @ A @ G[:, j]
            for i in range(degree):
                for j in range(degree):
                    Kij = 2.0 * W.conj().T @ np.linalg.matrix_power(C, int(r_times[i] + s_times[j] + 1)) @ W
                    multi_pairs[i, j] = np.vdot(F[:, i], Kij @ G[:, j])
            os_multi_pairs = Xi.conj().T @ Eta
            worst_os_pair = max(worst_os_pair, float(np.linalg.norm(multi_pairs - os_multi_pairs, ord=np.inf)))
            multi_det = np.linalg.det(multi_pairs)
            _, wedge_xi = wedge_coordinates(Xi, degree)
            _, wedge_eta = wedge_coordinates(Eta, degree)
            worst_multitime_wedge = max(worst_multitime_wedge, abs(multi_det - np.vdot(wedge_xi, wedge_eta)))
    check("one-particle Berezin pairings equal CAR transfer pairings for multiple block separations", worst_pair < 2e-12, f"worst pairing residual {worst_pair:.1e}")
    check("canonical OS quotient and boundary-insertion factorizations agree for common and arbitrary positive block times", worst_os_pair < 2e-12, f"worst residual {worst_os_pair:.1e}")
    check("all tested common-time and multitime Wick determinants equal CAR-Fock exterior inner products", worst_det < 2e-10 and worst_wedge < 2e-10 and worst_multitime_wedge < 2e-10, f"det {worst_det:.1e}, common wedge {worst_wedge:.1e}, multitime {worst_multitime_wedge:.1e}")


def test_null_direction_and_mutation_controls() -> None:
    M, lam = 0.5, 0.7
    _, z = energy_and_z(M, lam)
    K = reflected_gram(M, lam)
    vals, vecs = np.linalg.eigh(K)
    null = vecs[:, 0]
    physical = vecs[:, 1]
    null_norm = abs(np.vdot(null, K @ null))
    phys_norm = float(np.vdot(physical, K @ physical).real)
    wrong_z = float(np.exp(-energy_and_z(M, lam)[0]))
    mutation = abs(phys_norm - 2.0 * wrong_z)
    check("the orthogonal block-field combination is exactly OS-null while the physical combination has norm 2z", null_norm < 2e-14 and abs(phys_norm - 2.0 * z) < 2e-14, f"null {null_norm:.1e}, physical {phys_norm:.6f}")
    check("single-step decay e^-E fails the reflected-Gram normalization control", mutation > 1e-2, f"mutation residual {mutation:.3f}")


def main() -> int:
    print("FREE STAGGERED 3+1 REFLECTED GRAM / CAR-FOCK REPRESENTATION")
    print("Infinite temporal lattice, finite even 3D spatial torus, free supplied CAR/Grassmann branch.")
    test_note_guardrails()
    test_poles_and_transfer()
    test_residue_formula()
    test_rank_one_projector()
    test_open_chain_limit()
    test_full_3d_modal_lift()
    test_basis_independent_operator_formula()
    test_os_quotient_factorization()
    test_semigroup_grams()
    test_wick_to_fock_exterior_powers()
    test_null_direction_and_mutation_controls()
    print(f"SCORECARD: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
