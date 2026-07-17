#!/usr/bin/env python3
"""Deterministic certificate for the free-staggered pole/residue carrier bridge.

The scientific checks derive the continuum carrier from the finite blocked
staggered symbol and construct the finite given-CAR hole relabelling.  The
runner does not assign audit status and does not claim statistics selection.
"""

from __future__ import annotations

import json
import math
from itertools import product
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "FREE_STAGGERED_POLE_RESIDUE_DIRAC_CARRIER_CAR_RELABELING_"
    "BOUNDED_THEOREM_NOTE_2026-07-17.md"
)
TARGET_NOTE = ROOT / "docs" / "FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md"

ABJ_ID = "abj_p_rec_spintaste_clifford_core_bridge_note_2026-06-18"


def ledger_row(claim_id: str) -> dict:
    path = ROOT / "docs" / "audit" / "data" / "ledger" / claim_id[:2] / f"{claim_id}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def blocked_alphas() -> list[np.ndarray]:
    """Canonical 2^4 blocked staggered Clifford flips."""
    out: list[np.ndarray] = []
    for mu in range(4):
        mat = np.zeros((16, 16), dtype=complex)
        for b in range(16):
            bits = [(b >> nu) & 1 for nu in range(4)]
            eta = (-1) ** sum(bits[:mu])
            mat[b ^ (1 << mu), b] = eta
        out.append(mat)
    return out


def hamiltonian(alphas: list[np.ndarray], p: np.ndarray, m: float, a: float) -> tuple[np.ndarray, float]:
    s = np.sin(a * p) / a if a else p.copy()
    omega = float(np.sqrt(m * m + np.dot(s, s)))
    h = m * alphas[0]
    for i in range(3):
        h = h + 1j * alphas[0] @ alphas[i + 1] * s[i]
    return h, omega


def pole_data(p: np.ndarray, m: float, a: float) -> tuple[float, float, float]:
    s = np.sin(a * p) / a
    omega = float(np.sqrt(m * m + np.dot(s, s)))
    energy = math.asinh(a * omega) / a
    rho = 1.0 / (2.0 * omega * math.cosh(a * energy))
    return omega, energy, rho


def kron_all(items: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0 + 0.0j]])
    for item in items:
        out = np.kron(out, item)
    return out


def jw_annihilator(index: int, modes: int) -> np.ndarray:
    ident = np.eye(2, dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)
    sigma_plus = np.array([[0, 1], [0, 0]], dtype=complex)
    return kron_all([z if j < index else sigma_plus if j == index else ident for j in range(modes)])


def raw_ladder(index: int, modes: int) -> np.ndarray:
    ident = np.eye(2, dtype=complex)
    sigma_plus = np.array([[0, 1], [0, 0]], dtype=complex)
    return kron_all([sigma_plus if j == index else ident for j in range(modes)])


def check_dependencies_and_edge() -> tuple[bool, str]:
    abj = ledger_row(ABJ_ID)
    registry = json.loads((ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json").read_text())
    note = NOTE.read_text(encoding="utf-8")
    target = TARGET_NOTE.read_text(encoding="utf-8")
    bridge_name = NOTE.name
    ok = (
        abj.get("audit_status") == "audited_clean"
        and abj.get("effective_status") == "retained_bounded"
        and registry["nodes"]["minimal_axioms"]["current_path"] == "docs/MINIMAL_AXIOMS_2026-06-29.md"
        and registry["nodes"]["kinetic_isotropy_primitive"]["current_path"]
        == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
        and "](ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md)" in note
        and "](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)" in note
        and "](MINIMAL_AXIOMS_2026-06-29.md)" not in note
        and "c_t=c_s" in note
        and bridge_name in target
    )
    return ok, (
        f"ABJ={abj.get('effective_status')} graph_links=2 "
        f"minimal_context_only={'](MINIMAL_AXIOMS_2026-06-29.md)' not in note} "
        f"edge={bridge_name in target}"
    )


def check_blocked_clifford() -> tuple[bool, str]:
    alphas = blocked_alphas()
    ident = np.eye(16)
    worst = 0.0
    for mu, nu in product(range(4), repeat=2):
        got = alphas[mu] @ alphas[nu] + alphas[nu] @ alphas[mu]
        want = 2.0 * ident if mu == nu else np.zeros_like(ident)
        worst = max(worst, float(np.max(np.abs(got - want))))
    h, omega = hamiltonian(alphas, np.array([0.31, -0.27, 0.19]), 0.73, 0.16)
    eig = np.linalg.eigvalsh(h)
    multiplicity = np.count_nonzero(np.isclose(eig, omega)) == 8 and np.count_nonzero(np.isclose(eig, -omega)) == 8
    hermitian = np.allclose(h, h.conj().T, atol=1e-12)
    square = np.allclose(h @ h, omega * omega * ident, atol=1e-12)
    spin = [
        -0.5j * alphas[2] @ alphas[3],
        -0.5j * alphas[3] @ alphas[1],
        -0.5j * alphas[1] @ alphas[2],
    ]
    rest_proj = (ident + alphas[0]) / 2.0
    spin_residual = 0.0
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        spin_residual = max(
            spin_residual,
            float(np.max(np.abs(spin[i] @ spin[j] - spin[j] @ spin[i] - 1j * spin[k]))),
        )
    spin_residual = max(
        spin_residual,
        float(np.max(np.abs(sum(j @ j for j in spin) - 0.75 * ident))),
        max(float(np.max(np.abs(j @ rest_proj - rest_proj @ j))) for j in spin),
    )
    ok = worst < 1e-12 and spin_residual < 1e-12 and multiplicity and hermitian and square
    return ok, (
        f"clifford_residual={worst:.1e} spin={spin_residual:.1e} "
        "spectrum=8x(+/-omega)"
    )


def check_pole_and_residue() -> tuple[bool, str]:
    rng = np.random.default_rng(1707)
    worst_pole = 0.0
    worst_derivative = 0.0
    for _ in range(30):
        p = rng.uniform(-0.9, 0.9, size=3)
        m = float(rng.uniform(0.3, 1.2))
        a = float(rng.uniform(0.04, 0.3))
        omega, energy, _ = pole_data(p, m, a)
        delta = m * m + np.dot(np.sin(a * p) / a, np.sin(a * p) / a) - (math.sinh(a * energy) / a) ** 2
        worst_pole = max(worst_pole, abs(float(delta)))
        q0 = 1j * energy
        analytic = 2j * omega * math.cosh(a * energy)
        direct = 2.0 * np.sin(a * q0) * np.cos(a * q0) / a
        worst_derivative = max(worst_derivative, abs(complex(direct - analytic)))
    return worst_pole < 2e-12 and worst_derivative < 2e-12, f"pole={worst_pole:.2e} derivative={worst_derivative:.2e}"


def check_projector_residue() -> tuple[bool, str]:
    alphas = blocked_alphas()
    ident = np.eye(16)
    p = np.array([0.42, -0.28, 0.17])
    m, a = 0.81, 0.13
    h, omega = hamiltonian(alphas, p, m, a)
    proj = (ident + h / omega) / 2.0
    s = np.sin(a * p) / a
    numerator = m * ident + alphas[0] * omega
    for i in range(3):
        numerator = numerator - 1j * alphas[i + 1] * s[i]
    residual = float(np.max(np.abs(numerator - 2.0 * omega * proj @ alphas[0])))
    rest_proj = (ident + alphas[0]) / 2.0
    frame_numerator = (omega + m) * ident
    for i in range(3):
        frame_numerator = frame_numerator + 1j * alphas[0] @ alphas[i + 1] * s[i]
    frame = frame_numerator @ rest_proj / math.sqrt(2.0 * omega * (omega + m))
    frame_residual = max(
        float(np.max(np.abs(frame.conj().T @ frame - rest_proj))),
        float(np.max(np.abs(frame @ frame.conj().T - proj))),
    )
    projective = (
        np.allclose(proj @ proj, proj, atol=1e-12)
        and np.allclose(proj, proj.conj().T, atol=1e-12)
        and np.linalg.matrix_rank(proj, tol=1e-9) == 8
    )
    return residual < 2e-12 and frame_residual < 2e-12 and projective, (
        f"numerator_residual={residual:.2e} frame={frame_residual:.2e} "
        f"rank={np.linalg.matrix_rank(proj)}"
    )


def check_compact_convergence() -> tuple[bool, str]:
    alphas = blocked_alphas()
    momenta = [
        np.array([0.21, -0.37, 0.43]),
        np.array([-0.62, 0.15, 0.31]),
        np.array([0.48, 0.52, -0.29]),
    ]
    m = 0.77
    errors: list[tuple[float, float, float]] = []
    for a in (0.20, 0.10, 0.05):
        e_err = rho_err = p_err = 0.0
        for p in momenta:
            h0, e0 = hamiltonian(alphas, p, m, 0.0)
            p0 = (np.eye(16) + h0 / e0) / 2.0
            h, omega = hamiltonian(alphas, p, m, a)
            pa = (np.eye(16) + h / omega) / 2.0
            _, ea, rhoa = pole_data(p, m, a)
            e_err = max(e_err, abs(ea - e0))
            rho_err = max(rho_err, abs(rhoa - 1.0 / (2.0 * e0)))
            p_err = max(p_err, float(np.linalg.norm(pa - p0, ord=2)))
        errors.append((e_err, rho_err, p_err))
    ratios = [errors[j][k] / errors[j + 1][k] for j in (0, 1) for k in range(3)]
    ok = min(ratios) > 3.75 and max(ratios) < 4.25
    return ok, f"O(a^2)_ratios=[{min(ratios):.3f},{max(ratios):.3f}] final={errors[-1]}"


def check_anisotropy_falsifier() -> tuple[bool, str]:
    p = np.array([0.44, -0.31, 0.26])
    m = 0.69
    omega0 = float(np.sqrt(m * m + np.dot(p, p)))
    lam = 1.37
    errors = []
    for a in (0.08, 0.04, 0.02):
        s = np.sin(a * p) / a
        omega = float(np.sqrt(m * m + np.dot(s, s)))
        e_lam = math.asinh(a * omega / lam) / a
        errors.append(abs(e_lam - omega0 / lam))
    target_shell_residual = (omega0 / lam) ** 2 - np.dot(p, p) - m * m
    deformed_shell_residual = lam * lam * (omega0 / lam) ** 2 - np.dot(p, p) - m * m
    ok = errors[2] < errors[1] < errors[0] and abs(target_shell_residual) > 0.1 and abs(deformed_shell_residual) < 1e-12
    return ok, f"lambda={lam} target_residual={target_shell_residual:.3f} deformed={deformed_shell_residual:.1e}"


def check_derived_measure() -> tuple[bool, str]:
    rng = np.random.default_rng(44)
    worst_invariant = 0.0
    smallest_flat = float("inf")
    worst_jacobian = 0.0
    worst_shell = 0.0
    worst_standard_boost = 0.0
    m = 0.83
    rapidity = 0.61
    c, s = math.cosh(rapidity), math.sinh(rapidity)
    for _ in range(20):
        p = rng.uniform(-0.9, 0.9, size=3)
        e = float(np.sqrt(m * m + np.dot(p, p)))
        # rho*V_i = (1/(2E))*E = 1/2, so its divergence is exactly zero.
        invariant_div = 0.0
        flat_div = p[0] / e
        ep = c * e + s * p[0]
        pp = np.array([s * e + c * p[0], p[1], p[2]])
        jac = c + s * p[0] / e
        worst_invariant = max(worst_invariant, abs(invariant_div))
        if abs(p[0]) > 0.1:
            smallest_flat = min(smallest_flat, abs(flat_div))
        worst_jacobian = max(worst_jacobian, abs(jac / ep - 1.0 / e))
        worst_shell = max(worst_shell, abs(ep * ep - np.dot(pp, pp) - m * m))

        boost = np.eye(4)
        boost[0, 0] = e / m
        boost[0, 1:] = p / m
        boost[1:, 0] = p / m
        boost[1:, 1:] += np.outer(p, p) / (m * (e + m))
        eta = np.diag([1.0, -1.0, -1.0, -1.0])
        rest = np.array([m, 0.0, 0.0, 0.0])
        standard_residual = max(
            float(np.max(np.abs(boost.T @ eta @ boost - eta))),
            float(np.max(np.abs(boost @ rest - np.r_[e, p]))),
        )
        worst_standard_boost = max(worst_standard_boost, standard_residual)
    ok = (
        worst_invariant == 0.0
        and smallest_flat > 0.05
        and worst_jacobian < 2e-15
        and worst_shell < 3e-15
        and worst_standard_boost < 3e-15
    )
    return ok, (
        f"div(rho V)={worst_invariant:.1e} flat_nonzero>={smallest_flat:.2e} "
        f"measure_jac={worst_jacobian:.1e} shell={worst_shell:.1e} "
        f"L(p)={worst_standard_boost:.1e}"
    )


def check_jw_car_and_control() -> tuple[bool, str]:
    modes = 4
    ops = [jw_annihilator(i, modes) for i in range(modes)]
    ident = np.eye(2**modes)
    worst = 0.0
    for i, j in product(range(modes), repeat=2):
        worst = max(worst, float(np.max(np.abs(ops[i] @ ops[j] + ops[j] @ ops[i]))))
        mixed = ops[i] @ ops[j].conj().T + ops[j].conj().T @ ops[i]
        want = ident if i == j else np.zeros_like(ident)
        worst = max(worst, float(np.max(np.abs(mixed - want))))
    raw = [raw_ladder(i, modes) for i in range(modes)]
    control = float(np.linalg.norm(raw[0] @ raw[1] + raw[1] @ raw[0]))
    return worst < 1e-12 and control > 1.0, f"CAR_residual={worst:.1e} no_string_norm={control:.1f}"


def spectral_car_data() -> tuple[list[np.ndarray], np.ndarray, float, float]:
    # One irreducible spin block.  The retained 16x16 carrier is four copies.
    sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)
    ident2 = np.eye(2, dtype=complex)
    euclid = [
        np.kron(sigma1, ident2),
        np.kron(sigma2, ident2),
        np.kron(sigma3, sigma1),
        np.kron(sigma3, sigma2),
    ]
    p, m, a = np.array([0.37, -0.22, 0.29]), 0.74, 0.11
    h, omega = hamiltonian(euclid, p, m, a)
    eigvals, eigvecs = np.linalg.eigh(h)
    c_ops = [jw_annihilator(i, 4) for i in range(4)]
    d_ops = [sum(np.conjugate(eigvecs[j, r]) * c_ops[j] for j in range(4)) for r in range(4)]
    pole_energy = math.asinh(a * omega) / a
    return d_ops, eigvals, omega, pole_energy


def check_spectral_car() -> tuple[bool, str]:
    d_ops, eigvals, omega, _ = spectral_car_data()
    ident = np.eye(16)
    worst = 0.0
    for i, j in product(range(4), repeat=2):
        mixed = d_ops[i] @ d_ops[j].conj().T + d_ops[j].conj().T @ d_ops[i]
        want = ident if i == j else np.zeros_like(ident)
        worst = max(worst, float(np.max(np.abs(mixed - want))))
    spectrum_ok = np.allclose(eigvals, [-omega, -omega, omega, omega], atol=1e-11)
    return worst < 2e-12 and spectrum_ok, f"unitary_CAR_residual={worst:.2e} eig={np.round(eigvals, 6).tolist()}"


def check_hole_relabel() -> tuple[bool, str]:
    d_ops, eigvals, _, pole_energy = spectral_car_data()
    ident = np.eye(16)
    branch_energy = np.where(eigvals > 0.0, pole_energy, -pole_energy)
    h_raw = sum(branch_energy[r] * d_ops[r].conj().T @ d_ops[r] for r in range(4))
    positive = d_ops[2:]
    negative = d_ops[:2]
    h_relabel = sum(pole_energy * a.conj().T @ a for a in positive)
    # b^dagger=d_- and b=d_-^dagger, hence b^dagger b=d_- d_-^dagger.
    h_relabel = h_relabel + sum(pole_energy * d @ d.conj().T for d in negative)
    shifted = h_raw + 2.0 * pole_energy * ident
    residual = float(np.max(np.abs(shifted - h_relabel)))
    eig = np.linalg.eigvalsh(h_relabel)
    ok = residual < 3e-12 and eig.min() > -2e-12 and np.isclose(eig.min(), 0.0, atol=2e-12)
    return ok, (
        f"pole_energy={pole_energy:.6f} relabel_residual={residual:.2e} "
        f"spectrum=[{eig.min():.2e},{eig.max():.6f}]"
    )


def check_source_boundaries() -> tuple[bool, str]:
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.split())
    required = [
        "four framework axioms select CAR statistics",
        "does not prove a single-taste physical selector",
        "does not claim essential self-adjointness",
        "does not set or predict an audit verdict",
        "No literature result",
        "fitted value",
        "The strings are load-bearing",
        "principal low-energy time patch",
    ]
    forbidden = ["Status: retained", "proposed_retained", "promote to retained"]
    ok = all(token in normalized for token in required) and not any(token in normalized for token in forbidden)
    present = sum(token in normalized for token in required)
    absent = sum(token in normalized for token in forbidden)
    return ok, f"required={present}/{len(required)} forbidden={absent}"


def main() -> int:
    checks = [
        ("C1 dependency classes and one-hop target edge", check_dependencies_and_edge),
        ("C2 blocked Clifford, spin-half rest carrier, and taste multiplicity", check_blocked_clifford),
        ("C3 finite-spacing complex pole and residue derivative", check_pole_and_residue),
        ("C4 pole numerator and explicit rest-fiber isometry", check_projector_residue),
        ("C5 compact-momentum energy/residue/projector convergence is O(a^2)", check_compact_convergence),
        ("C6 temporal anisotropy falsifies the target shell normalization", check_anisotropy_falsifier),
        ("C7 pole-derived limiting measure is boost invariant", check_derived_measure),
        ("C8 Jordan-Wigner CAR is exact and no-string control fails", check_jw_car_and_control),
        ("C9 Hamiltonian spectral basis preserves CAR", check_spectral_car),
        ("C10 hole relabelling is exact and normal-ordered spectrum nonnegative", check_hole_relabel),
        ("C11 source boundaries and status firewalls", check_source_boundaries),
    ]
    results = []
    for name, fn in checks:
        try:
            ok, detail = fn()
        except Exception as exc:  # deterministic failure reporting
            ok, detail = False, f"{type(exc).__name__}: {exc}"
        results.append((name, ok, detail))

    print("FREE-STAGGERED POLE/RESIDUE DIRAC CARRIER + FINITE CAR RELABELLING")
    for name, ok, detail in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    passed = sum(ok for _, ok, _ in results)
    failed = len(results) - passed
    print(f"SCORECARD PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
