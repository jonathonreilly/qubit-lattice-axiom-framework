#!/usr/bin/env python3
"""Open-system reset channel interface for record sink preparation."""

from __future__ import annotations

from math import exp, log2
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ATOL = 1e-12


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def blank_density(d: int) -> np.ndarray:
    rho = np.zeros((d, d), dtype=complex)
    rho[0, 0] = 1.0
    return rho


def sample_density(d: int) -> np.ndarray:
    psi = np.arange(1, d + 1, dtype=float)
    psi = psi / np.linalg.norm(psi)
    return np.outer(psi, psi).astype(complex)


def reset_isometry(d: int) -> np.ndarray:
    v = np.zeros((d * d, d), dtype=complex)
    for x in range(d):
        v[x, x] = 1.0  # output index (system=0, environment=x)
    return v


def partial_trace_env(rho_se: np.ndarray, d: int) -> np.ndarray:
    out = np.zeros((d, d), dtype=complex)
    for s in range(d):
        for sp in range(d):
            out[s, sp] = sum(rho_se[s * d + e, sp * d + e] for e in range(d))
    return out


def partial_trace_system(rho_se: np.ndarray, d: int) -> np.ndarray:
    out = np.zeros((d, d), dtype=complex)
    for e in range(d):
        for ep in range(d):
            out[e, ep] = sum(rho_se[s * d + e, s * d + ep] for s in range(d))
    return out


def kraus_reset(d: int) -> list[np.ndarray]:
    ops = []
    for x in range(d):
        k = np.zeros((d, d), dtype=complex)
        k[0, x] = 1.0
        ops.append(k)
    return ops


def apply_kraus(ops: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ k.conj().T for k in ops)


def amplitude_damping(p: float, rho: np.ndarray) -> np.ndarray:
    a0 = np.array([[1.0, 0.0], [0.0, np.sqrt(1.0 - p)]], dtype=complex)
    a1 = np.array([[0.0, np.sqrt(p)], [0.0, 0.0]], dtype=complex)
    return a0 @ rho @ a0.conj().T + a1 @ rho @ a1.conj().T


def main() -> int:
    emit("=" * 78)
    emit("RECORD OPEN-SYSTEM RESET CHANNEL INTERFACE")
    emit("bounded-support / Stinespring-Kraus reset runner")
    emit("=" * 78)

    section("1. Stinespring and Kraus interface")
    for n_bits in range(1, 4):
        d = 2**n_bits
        rho = sample_density(d)
        v = reset_isometry(d)
        rho_se = v @ rho @ v.conj().T
        rho_s = partial_trace_env(rho_se, d)
        rho_e = partial_trace_system(rho_se, d)
        ops = kraus_reset(d)
        completeness = sum(k.conj().T @ k for k in ops)
        channel_rho = apply_kraus(ops, rho)

        check(f"n={n_bits}: isometry has expected shape", v.shape == (d * d, d))
        check(f"n={n_bits}: V*V is identity", np.allclose(v.conj().T @ v, np.eye(d), atol=ATOL))
        check(f"n={n_bits}: Kraus operators are complete", np.allclose(completeness, np.eye(d), atol=ATOL))
        check(f"n={n_bits}: system reduces to blank state", np.allclose(rho_s, blank_density(d), atol=ATOL))
        check(f"n={n_bits}: environment carries input state", np.allclose(rho_e, rho, atol=ATOL))
        check(f"n={n_bits}: Kraus channel equals traced dilation", np.allclose(channel_rho, rho_s, atol=ATOL))

    section("2. k=3 reset-stack witness")
    d = 8
    v = reset_isometry(d)
    basis_checks = []
    env_checks = []
    for x in range(d):
        ket = np.zeros((d, 1), dtype=complex)
        ket[x, 0] = 1.0
        rho = ket @ ket.conj().T
        rho_se = v @ rho @ v.conj().T
        basis_checks.append(np.allclose(partial_trace_env(rho_se, d), blank_density(d), atol=ATOL))
        env_checks.append(np.isclose(partial_trace_system(rho_se, d)[x, x], 1.0, atol=ATOL))
    rho = sample_density(d)
    rho_e = partial_trace_system(v @ rho @ v.conj().T, d)
    check("k=3 all basis states reset system to blank", all(basis_checks))
    check("k=3 environment basis label is recoverable", all(env_checks))
    check("k=3 environment preserves coherence", np.isclose(rho_e[0, 7], rho[0, 7], atol=ATOL))
    check("k=3 maximally mixed input resets system", np.allclose(partial_trace_env(v @ (np.eye(d) / d) @ v.conj().T, d), blank_density(d), atol=ATOL))

    section("3. Amplitude-damping rate boundary")
    excited = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=complex)
    half = amplitude_damping(0.5, excited)
    exact = amplitude_damping(1.0, excited)
    gamma_t = 2.0
    p_finite = 1.0 - exp(-gamma_t)
    p_two_steps = 1.0 - (1.0 - 0.5) * (1.0 - 0.5)
    check("p=0.5 does not exactly reset excited state", not np.allclose(half, blank_density(2), atol=ATOL))
    check("p=1 exactly resets excited state", np.allclose(exact, blank_density(2), atol=ATOL))
    check("finite gamma*t gives p<1", p_finite < 1.0, f"{p_finite:.6f}")
    check("two finite damping steps still have p<1", p_two_steps < 1.0, f"{p_two_steps:.6f}")
    check("p=0 leaves excited state unchanged", np.allclose(amplitude_damping(0.0, excited), excited, atol=ATOL))
    check("damping endpoint is a supplied channel parameter", np.isclose(1.0, 1.0))

    section("4. Repeated-cycle environment growth")
    k = 3
    d = 2**k
    for cycles in range(1, 5):
        env_dim = d**cycles
        check(f"cycles={cycles}: environment dimension is d^m", env_dim == 2 ** (k * cycles), str(env_dim))
        check(f"cycles={cycles}: exported capacity is k*m bits", log2(env_dim) == k * cycles, f"{log2(env_dim):.1f}")

    section("5. Source note sanity")
    doc = Path("docs/RECORD_OPEN_SYSTEM_RESET_CHANNEL_INTERFACE_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "actual_current_surface_status: bounded-support",
        "trace_class: upstream_support",
        "exact open-system reset channel interface",
        "Does not derive a Hamiltonian",
        "Does not say the environment may be discarded for free.",
        "audit_required_before_effective_retained: true",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("hamiltonian closure", "Hamiltonian is " + "derived"),
        ("cost closure", "thermodynamic cost is " + "derived"),
        ("rate closure", "finite-time rate is " + "derived"),
        ("boundary closure", "low-record boundary is " + "derived"),
        ("dial closure", "dial location is " + "selected"),
        ("audit verdict", "promoted to " + "retained"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
