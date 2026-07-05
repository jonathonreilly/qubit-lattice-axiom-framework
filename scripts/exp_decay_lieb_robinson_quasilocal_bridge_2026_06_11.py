#!/usr/bin/env python3
"""Exponential-decay quasilocal Lieb-Robinson bridge runner.

Companion to
docs/EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md.

Deterministic finite-block checks:
  [C]  Hastings-Koma reproducing weight vs pure-exponential falsifier.
  [N]  H_log = -log(exp(-A/2) exp(-B) exp(-A/2)) Pauli support norm.
  [LR] Direct commutator <= displayed bound with computed constants.
  [F]  Falsifiers and finite-range consistency checks.

No fitted constants are used in the LR checks.
"""

from __future__ import annotations

import itertools
import math
import sys

import numpy as np

PASS = 0
FAIL = 0
SEED = 20260611


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"[{status}] [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def F_weight(r: int | float, mu: float, alpha: float) -> float:
    return math.exp(-mu * float(r)) / (1.0 + float(r)) ** alpha


def pure_weight(r: int | float, mu: float) -> float:
    return math.exp(-mu * float(r))


def l1_norm(point: tuple[int, ...]) -> int:
    return int(sum(abs(v) for v in point))


def s_alpha_box(dim: int, alpha: float, radius: int) -> float:
    if dim == 1:
        return sum((1 + abs(z)) ** (-alpha) for z in range(-radius, radius + 1))
    if dim == 2:
        total = 0.0
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):
                total += (1 + abs(x) + abs(y)) ** (-alpha)
        return total
    if dim == 3:
        total = 0.0
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):
                for z in range(-radius, radius + 1):
                    total += (1 + abs(x) + abs(y) + abs(z)) ** (-alpha)
        return total
    raise ValueError("dim must be 1, 2, or 3")


def convolution_ratio(dim: int, R: int, mu: float, alpha: float, box_pad: int, pure: bool) -> float:
    if dim == 1:
        total = 0.0
        for z in range(-box_pad, R + box_pad + 1):
            a = abs(z)
            b = abs(z - R)
            if pure:
                total += pure_weight(a, mu) * pure_weight(b, mu)
            else:
                total += F_weight(a, mu, alpha) * F_weight(b, mu, alpha)
        denom = pure_weight(R, mu) if pure else F_weight(R, mu, alpha)
        return total / denom
    if dim == 2:
        total = 0.0
        for zx in range(-box_pad, R + box_pad + 1):
            for zy in range(-box_pad, box_pad + 1):
                a = abs(zx) + abs(zy)
                b = abs(zx - R) + abs(zy)
                if pure:
                    total += pure_weight(a, mu) * pure_weight(b, mu)
                else:
                    total += F_weight(a, mu, alpha) * F_weight(b, mu, alpha)
        denom = pure_weight(R, mu) if pure else F_weight(R, mu, alpha)
        return total / denom
    if dim == 3:
        total = 0.0
        for zx in range(-box_pad, R + box_pad + 1):
            for zy in range(-box_pad, box_pad + 1):
                for zz in range(-box_pad, box_pad + 1):
                    a = abs(zx) + abs(zy) + abs(zz)
                    b = abs(zx - R) + abs(zy) + abs(zz)
                    if pure:
                        total += pure_weight(a, mu) * pure_weight(b, mu)
                    else:
                        total += F_weight(a, mu, alpha) * F_weight(b, mu, alpha)
        denom = pure_weight(R, mu) if pure else F_weight(R, mu, alpha)
        return total / denom
    raise ValueError("dim must be 1, 2, or 3")


I2 = np.eye(2, dtype=complex)
PX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
PY = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
PZ = np.diag([1.0, -1.0]).astype(complex)
PAULIS = (I2, PX, PY, PZ)


def kron_ops(ops: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0]], dtype=complex)
    for op in ops:
        out = np.kron(out, op)
    return out


def site_op(L: int, op: np.ndarray, site: int) -> np.ndarray:
    return kron_ops([op if k == site else I2 for k in range(L)])


def two_site_op(L: int, op_a: np.ndarray, a: int, op_b: np.ndarray, b: int) -> np.ndarray:
    return kron_ops([op_a if k == a else op_b if k == b else I2 for k in range(L)])


def pauli_string(indices: tuple[int, ...]) -> np.ndarray:
    return kron_ops([PAULIS[i] for i in indices])


def hermitian_expm(H: np.ndarray, scale: float) -> np.ndarray:
    Hh = 0.5 * (H + H.conj().T)
    vals, vecs = np.linalg.eigh(Hh)
    return vecs @ np.diag(np.exp(scale * vals)) @ vecs.conj().T


def positive_log_hamiltonian(T: np.ndarray) -> np.ndarray:
    Th = 0.5 * (T + T.conj().T)
    vals, vecs = np.linalg.eigh(Th)
    return -(vecs @ np.diag(np.log(vals)) @ vecs.conj().T)


def op_norm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, 2))


def comm(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def build_local_generators(L: int, scale: float = 0.05) -> tuple[np.ndarray, np.ndarray]:
    dim = 2**L
    A = np.zeros((dim, dim), dtype=complex)
    B = np.zeros((dim, dim), dtype=complex)
    for i in range(L - 1):
        A += scale * (0.90 * two_site_op(L, PX, i, PX, i + 1))
        A += scale * (0.35 * two_site_op(L, PZ, i, PY, i + 1))
        B += scale * (0.80 * two_site_op(L, PZ, i, PZ, i + 1))
        B += scale * (0.30 * two_site_op(L, PX, i, PY, i + 1))
    for i in range(L):
        A += scale * 0.22 * site_op(L, PZ, i)
        B += scale * 0.18 * site_op(L, PX, i)
    return 0.5 * (A + A.conj().T), 0.5 * (B + B.conj().T)


def decompose_by_support(H: np.ndarray, L: int, tol: float = 1e-12) -> dict[tuple[int, ...], np.ndarray]:
    dim = 2**L
    groups: dict[tuple[int, ...], np.ndarray] = {}
    for indices in itertools.product(range(4), repeat=L):
        if all(i == 0 for i in indices):
            continue
        P = pauli_string(indices)
        coeff = np.vdot(P, H) / dim
        if abs(coeff) <= tol:
            continue
        support = tuple(k for k, i in enumerate(indices) if i != 0)
        if support not in groups:
            groups[support] = np.zeros_like(H)
        groups[support] += coeff * P
    return groups


def support_norms(groups: dict[tuple[int, ...], np.ndarray]) -> dict[tuple[int, ...], float]:
    return {supp: op_norm(0.5 * (mat + mat.conj().T)) for supp, mat in groups.items()}


def support_diameter(supp: tuple[int, ...]) -> int:
    if len(supp) <= 1:
        return 0
    return max(supp) - min(supp)


def pair_kernel(norms: dict[tuple[int, ...], float], L: int) -> np.ndarray:
    K = np.zeros((L, L), dtype=float)
    for supp, norm in norms.items():
        for x in supp:
            for y in supp:
                K[x, y] += norm
    return K


def weighted_pair_norm(K: np.ndarray, mu: float, alpha: float) -> float:
    L = K.shape[0]
    worst = 0.0
    for x in range(L):
        for y in range(L):
            worst = max(worst, K[x, y] / F_weight(abs(x - y), mu, alpha))
    return worst


def c_alpha_1d(alpha: float, cutoff: int = 200_000) -> float:
    total = 1.0 + 2.0 * sum((1 + n) ** (-alpha) for n in range(1, cutoff + 1))
    return (2.0**alpha) * total


def evolve_from_eig(vals: np.ndarray, vecs: np.ndarray, A: np.ndarray, t: float) -> np.ndarray:
    U = vecs @ np.diag(np.exp(1j * t * vals)) @ vecs.conj().T
    return U @ A @ U.conj().T


def run_convolution_checks() -> tuple[bool, dict[int, list[float]]]:
    section("[C] reproducing inequality and pure-exponential falsifier")
    mu = 0.55
    distances = [4, 8, 12, 16, 20, 24]
    pure_ratios: dict[int, list[float]] = {}
    weighted_ok = True
    pure_ok = True
    details = []
    for dim, alpha, c_radius, box_pad in ((1, 3.0, 80, 40), (2, 4.0, 80, 40), (3, 5.0, 32, 18)):
        c_box = (2.0**alpha) * s_alpha_box(dim, alpha, c_radius)
        wr = [convolution_ratio(dim, R, mu, alpha, box_pad, pure=False) for R in distances]
        gr = [convolution_ratio(dim, R, mu, alpha, box_pad, pure=True) for R in distances]
        pure_ratios[dim] = gr
        weighted_ok = weighted_ok and max(wr) < c_box and max(wr) / min(wr) < 1.25
        pure_ok = pure_ok and gr[-1] > 3.5 * gr[0] and all(b > a for a, b in zip(gr, gr[1:]))
        details.append(
            f"Z^{dim}: max F-ratio={max(wr):.4f} < C_box={c_box:.4f}; "
            f"pure {gr[0]:.2f}->{gr[-1]:.2f}"
        )
    check("C", "F_{mu,alpha} has bounded reproducing ratios on finite Z^1/Z^2/Z^3 boxes",
          weighted_ok, "; ".join(details))
    check("C", "FALSIFIER: pure exponential reproducing ratio grows with distance",
          pure_ok, "geodesic contribution visible in all tested dimensions")
    return pure_ok, pure_ratios


def build_log_transfer_data() -> dict[str, object]:
    L = 6
    mu = 0.45
    alpha = 3.0
    A, B = build_local_generators(L)
    EA = hermitian_expm(A, -0.5)
    EB = hermitian_expm(B, -1.0)
    T = 0.5 * (EA @ EB @ EA + (EA @ EB @ EA).conj().T)
    eig_T = np.linalg.eigvalsh(T)
    H_log = positive_log_hamiltonian(T)
    H_log = 0.5 * (H_log + H_log.conj().T)
    groups = decompose_by_support(H_log, L)
    norms = support_norms(groups)
    K = pair_kernel(norms, L)
    J = weighted_pair_norm(K, mu, alpha)
    C = c_alpha_1d(alpha)
    return {
        "L": L,
        "mu": mu,
        "alpha": alpha,
        "A": A,
        "B": B,
        "T": T,
        "eig_T": eig_T,
        "H_log": H_log,
        "groups": groups,
        "norms": norms,
        "K": K,
        "J": J,
        "C": C,
    }


def run_norm_checks(data: dict[str, object]) -> None:
    section("[N] log-transfer interaction norm")
    L = int(data["L"])
    eig_T = data["eig_T"]  # type: ignore[assignment]
    H_log = data["H_log"]  # type: ignore[assignment]
    norms = data["norms"]  # type: ignore[assignment]
    J = float(data["J"])
    mu = float(data["mu"])
    alpha = float(data["alpha"])

    assert isinstance(eig_T, np.ndarray)
    assert isinstance(H_log, np.ndarray)
    assert isinstance(norms, dict)

    positivity_ok = float(np.min(eig_T)) > 0.0 and op_norm(H_log - H_log.conj().T) < 1e-12
    check("N", "strictly local positive T gives Hermitian H_log = -log T",
          positivity_ok,
          f"min eig(T)={float(np.min(eig_T)):.6f}, hermiticity defect={op_norm(H_log-H_log.conj().T):.1e}")

    by_diam: dict[int, float] = {}
    for supp, norm in norms.items():
        by_diam[support_diameter(supp)] = by_diam.get(support_diameter(supp), 0.0) + norm
    total = sum(norms.values())
    tail = sum(norm for supp, norm in norms.items() if support_diameter(supp) >= 4)
    tail_rel = tail / total
    norm_ok = math.isfinite(J) and J > 0.0 and tail_rel < 1e-4
    detail = (
        f"L={L}, mu={mu}, alpha={alpha}, supports={len(norms)}, "
        f"J_F={J:.6f}, diam weights={{{', '.join(f'{k}:{by_diam[k]:.3e}' for k in sorted(by_diam))}}}, "
        f"tail diam>=4 rel={tail_rel:.2e}"
    )
    check("N", "weighted interaction norm is finite and support-diameter tail is negligible",
          norm_ok, detail)


def run_lr_checks(data: dict[str, object]) -> None:
    section("[LR] displayed Lieb-Robinson inequality")
    L = int(data["L"])
    H = data["H_log"]  # type: ignore[assignment]
    J = float(data["J"])
    C = float(data["C"])
    mu = float(data["mu"])
    alpha = float(data["alpha"])
    assert isinstance(H, np.ndarray)
    vals, vecs = np.linalg.eigh(H)
    A0 = site_op(L, PX, 0)
    norm_a = op_norm(A0)
    worst_ratio = 0.0
    worst_point = None
    ok = True
    for t in (0.005, 0.01, 0.02, 0.05, 0.08):
        At = evolve_from_eig(vals, vecs, A0, t)
        for d in range(1, L):
            Bd = site_op(L, PZ, d)
            measured = op_norm(comm(At, Bd))
            bound = (
                (2.0 * norm_a * op_norm(Bd) / C)
                * (math.exp(2.0 * C * J * abs(t)) - 1.0)
                * F_weight(d, mu, alpha)
            )
            ratio = measured / bound if bound > 0 else float("inf")
            if ratio > worst_ratio:
                worst_ratio = ratio
                worst_point = (t, d, measured, bound)
            if measured > bound * (1.0 + 1e-10) + 1e-12:
                ok = False
    assert worst_point is not None
    t, d, measured, bound = worst_point
    check("LR", "matrix commutators obey the displayed bound with computed C_alpha and J_F",
          ok,
          f"worst ratio={worst_ratio:.4f} at t={t}, d={d}, true={measured:.3e}, bound={bound:.3e}")


def run_falsifier_checks(data: dict[str, object], pure_ok: bool) -> None:
    section("[F] falsifiers and finite-range consistency")
    check("F", "pure-exponential convolution growth is asserted as the note's falsifier",
          pure_ok, "same data as [C]")

    L = int(data["L"])
    mu = float(data["mu"])
    alpha = float(data["alpha"])
    C = float(data["C"])
    H = data["H_log"]  # type: ignore[assignment]
    K = data["K"]  # type: ignore[assignment]
    J = float(data["J"])
    A = data["A"]  # type: ignore[assignment]
    B = data["B"]  # type: ignore[assignment]
    assert isinstance(H, np.ndarray)
    assert isinstance(K, np.ndarray)
    assert isinstance(A, np.ndarray)
    assert isinstance(B, np.ndarray)

    H_fr = A + B
    norms_fr = support_norms(decompose_by_support(H_fr, L))
    max_diam = max(support_diameter(supp) for supp in norms_fr)
    K_fr = pair_kernel(norms_fr, L)
    J_fr = weighted_pair_norm(K_fr, mu, alpha)
    spatial_rate_ok = all(F_weight(r, mu, alpha) <= math.exp(-mu * r) for r in range(1, L))
    check("F", "finite-range special case is inside the new normed class",
          max_diam <= 1 and math.isfinite(J_fr) and J_fr > 0.0 and spatial_rate_ok,
          f"max diam={max_diam}, J_F(finite-range)={J_fr:.6f}, F(r)<=exp(-mu r) for r<=5")

    vals, vecs = np.linalg.eigh(H)
    A0 = site_op(L, PX, 0)
    found = None
    for t in (0.005, 0.01, 0.02, 0.05):
        At = evolve_from_eig(vals, vecs, A0, t)
        for d in range(1, L):
            Bd = site_op(L, PZ, d)
            measured = op_norm(comm(At, Bd))
            dropped_c_bound = (
                (2.0 * op_norm(A0) * op_norm(Bd) / C)
                * (math.exp(2.0 * J * abs(t)) - 1.0)
                * F_weight(d, mu, alpha)
            )
            if measured > dropped_c_bound * (1.0 + 1e-8) + 1e-12:
                found = (t, d, measured, dropped_c_bound)
                break
        if found is not None:
            break
    if found is None:
        check("F", "dropping C_alpha from velocity is load-bearing on this grid",
              False, "no true-commutator violation found")
    else:
        t, d, measured, dropped = found
        check("F", "dropping C_alpha from the velocity violates the true commutator bound",
              True,
              f"t={t}, d={d}, true={measured:.3e} > no-C bound={dropped:.3e}")

    path_ok = True
    worst2 = 0.0
    worst3 = 0.0
    M2 = K @ K
    M3 = M2 @ K
    for x in range(L):
        for y in range(L):
            r = abs(x - y)
            b2 = (J**2) * C * F_weight(r, mu, alpha)
            b3 = (J**3) * (C**2) * F_weight(r, mu, alpha)
            worst2 = max(worst2, M2[x, y] / b2 if b2 > 0 else 0.0)
            worst3 = max(worst3, M3[x, y] / b3 if b3 > 0 else 0.0)
            if M2[x, y] > b2 * (1.0 + 1e-12) or M3[x, y] > b3 * (1.0 + 1e-12):
                path_ok = False
    check("F", "k=2 and k=3 path-series terms obey the corrected C_alpha powers",
          path_ok, f"worst k=2 ratio={worst2:.4f}, worst k=3 ratio={worst3:.4f}")


def main() -> int:
    np.random.default_rng(SEED)
    print("EXP-DECAY LIEB-ROBINSON QUASILOCAL BRIDGE RUNNER")
    print(f"deterministic seed = {SEED}")
    print("DECLARED SCOPE: finite blocks; constants displayed; consumer must separately supply finite weighted log-transfer norm")
    pure_ok, _pure_ratios = run_convolution_checks()
    data = build_log_transfer_data()
    run_norm_checks(data)
    run_lr_checks(data)
    run_falsifier_checks(data, pure_ok)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
