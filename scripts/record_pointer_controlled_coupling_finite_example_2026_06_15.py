#!/usr/bin/env python3
"""Finite controlled-coupling record-formation example.

This is the narrow source split of the broader record-formation dynamics
packet. It proves only a concrete sufficiency example:

  H = g sigma_z(S) sum_k sigma_x(E_k)

commutes with the pointer observable Pi_S = sigma_z(S), forms redundant
single-fragment pointer records at t = pi/(4g), and preserves already written
records under a later local recording step.  It does not claim an equivalence
between all objective record formation and pointer non-demolition dynamics.
"""

from __future__ import annotations

import numpy as np


PASS = 0
FAIL = 0
TOL = 1e-10
EXPECTED_PASS = 18

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return cond


def kron_all(items: list[np.ndarray]) -> np.ndarray:
    out = items[0]
    for item in items[1:]:
        out = np.kron(out, item)
    return out


def op(single: np.ndarray, pos: int, n: int) -> np.ndarray:
    return kron_all([single if i == pos else I2 for i in range(n)])


def partial_trace(rho: np.ndarray, keep: list[int], n: int) -> np.ndarray:
    keep = sorted(keep)
    traced = [q for q in range(n) if q not in keep]
    tensor = rho.reshape([2] * (2 * n))
    offset = 0
    for q in traced:
        ax = q - offset
        tensor = np.trace(tensor, axis1=ax, axis2=ax + n - offset)
        offset += 1
    dim = 2 ** len(keep)
    return tensor.reshape(dim, dim)


def entropy_bits(rho: np.ndarray) -> float:
    vals = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    vals = vals[vals > 1e-12]
    return float(-np.sum(vals * np.log2(vals)))


def shannon_bits(probs: np.ndarray) -> float:
    p = np.asarray(probs, dtype=float)
    p = p[p > 1e-12]
    return float(-np.sum(p * np.log2(p)))


def unitary_from_h(H: np.ndarray, t: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(H)
    return (vecs * np.exp(-1j * vals * t)) @ vecs.conj().T


def controlled_h(n_env: int, g: float, active: list[int] | None = None) -> np.ndarray:
    n = n_env + 1
    active = list(range(1, n)) if active is None else active
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    z_s = op(SZ, 0, n)
    for k in active:
        H += g * (z_s @ op(SX, k, n))
    return H


def demolition_h(n_env: int, g: float, active: list[int] | None = None) -> np.ndarray:
    n = n_env + 1
    active = list(range(1, n)) if active is None else active
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    x_s = op(SX, 0, n)
    for k in active:
        H += g * (x_s @ op(SX, k, n))
    return H


def initial_state(n_env: int) -> np.ndarray:
    # Generic off-axis S state: nonzero pointer entropy and nonzero coherence.
    theta = 0.73
    phi = 0.41
    system = np.array(
        [np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)],
        dtype=complex,
    )
    return kron_all([system] + [KET0] * n_env)


def density(psi: np.ndarray) -> np.ndarray:
    return np.outer(psi, psi.conj())


def pointer_entropy(rho: np.ndarray, n: int) -> float:
    rho_s = partial_trace(rho, [0], n)
    return shannon_bits(np.real(np.diag(rho_s)))


def dephase_system(rho: np.ndarray, n: int) -> np.ndarray:
    q0 = op(P0, 0, n)
    q1 = op(P1, 0, n)
    return q0 @ rho @ q0 + q1 @ rho @ q1


def pointer_info(rho: np.ndarray, frag: list[int], n: int) -> float:
    rho_d = dephase_system(rho, n)
    rho_s = partial_trace(rho_d, [0], n)
    rho_f = partial_trace(rho_d, frag, n)
    rho_sf = partial_trace(rho_d, sorted([0] + frag), n)
    return entropy_bits(rho_s) + entropy_bits(rho_f) - entropy_bits(rho_sf)


def conditional_fragment_states(rho: np.ndarray, frag: list[int], n: int) -> tuple[np.ndarray, np.ndarray]:
    states = []
    for projector in (P0, P1):
        P = op(projector, 0, n)
        block = P @ rho @ P
        prob = np.trace(block).real
        states.append(partial_trace(block / prob, frag, n))
    return states[0], states[1]


def populations(rho: np.ndarray, n: int) -> np.ndarray:
    return np.real(np.diag(partial_trace(rho, [0], n)))


def main() -> int:
    n_env = 3
    n = n_env + 1
    g_values = [0.5, 1.0, 2.0]
    psi0 = initial_state(n_env)
    rho0 = density(psi0)
    H_record = pointer_entropy(rho0, n)
    Pi = op(SZ, 0, n)

    print("Finite controlled-coupling record-formation split")

    check(
        "F1 initial pointer entropy is nontrivial",
        0.05 < H_record < 0.99,
        detail=f"H(Pi_S)={H_record:.6f}",
    )
    check(
        "F2 no fragment initially carries pointer information",
        max(pointer_info(rho0, [k], n) for k in range(1, n)) < TOL,
    )

    for g in g_values:
        H = controlled_h(n_env, g)
        t = np.pi / (4 * g)
        U = unitary_from_h(H, t)
        rho = density(U @ psi0)
        comm_norm = np.linalg.norm(H @ Pi - Pi @ H)
        infos = [pointer_info(rho, [k], n) for k in range(1, n)]
        cond0, cond1 = conditional_fragment_states(rho, [1], n)
        overlap = abs(np.trace(cond0 @ cond1))
        check(
            f"F3 g={g:g}: controlled Hamiltonian commutes with pointer",
            comm_norm < TOL,
            detail=f"||[H,Pi_S]||={comm_norm:.2e}",
        )
        check(
            f"F4 g={g:g}: pointer populations are preserved",
            np.allclose(populations(rho, n), populations(rho0, n), atol=TOL),
        )
        check(
            f"F5 g={g:g}: every singleton fragment carries the full pointer record",
            all(abs(info - H_record) < 1e-8 for info in infos),
            detail=f"infos={[round(x, 6) for x in infos]}",
        )
        check(
            f"F6 g={g:g}: conditional fragment states are orthogonal",
            overlap < TOL,
            detail=f"Tr(rho_F|0 rho_F|1)={overlap:.2e}",
        )

    # Persistence: write E1, then write E2 later.  The E1 record is unchanged
    # because the later step acts only on S and E2 and still commutes with Pi_S.
    g = 1.0
    t = np.pi / (4 * g)
    U_e1 = unitary_from_h(controlled_h(n_env, g, active=[1]), t)
    rho_after_e1 = density(U_e1 @ psi0)
    info_e1_before = pointer_info(rho_after_e1, [1], n)
    U_e2 = unitary_from_h(controlled_h(n_env, g, active=[2]), t)
    rho_after_e2 = U_e2 @ rho_after_e1 @ U_e2.conj().T
    info_e1_after = pointer_info(rho_after_e2, [1], n)
    info_e2_after = pointer_info(rho_after_e2, [2], n)
    check(
        "F7 finished fragment persists under later local controlled recording",
        abs(info_e1_after - info_e1_before) < 1e-8 and abs(info_e1_after - H_record) < 1e-8,
        detail=f"E1 before={info_e1_before:.6f}, after={info_e1_after:.6f}",
    )
    check(
        "F8 later fragment also reaches the same pointer record",
        abs(info_e2_after - H_record) < 1e-8,
        detail=f"E2 after={info_e2_after:.6f}",
    )

    # Boundary control: a pointer-rotating handle is not the finite example.
    H_bad = demolition_h(n_env, 1.0)
    U_bad = unitary_from_h(H_bad, np.pi / 4)
    rho_bad = density(U_bad @ psi0)
    check(
        "F9 demolition control fails the pointer commutant condition",
        np.linalg.norm(H_bad @ Pi - Pi @ H_bad) > 1.0,
    )
    check(
        "F10 demolition control changes pointer populations",
        not np.allclose(populations(rho_bad, n), populations(rho0, n), atol=1e-3),
        detail=f"initial={np.round(populations(rho0, n), 6).tolist()}, final={np.round(populations(rho_bad, n), 6).tolist()}",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if PASS != EXPECTED_PASS:
        print(f"ERROR: expected {EXPECTED_PASS} PASS checks, got {PASS}.")
        return 1
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
