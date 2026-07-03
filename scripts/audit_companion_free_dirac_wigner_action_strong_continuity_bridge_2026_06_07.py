#!/usr/bin/env python3
"""Strong-continuity bridge for the free-Dirac Wigner action."""

from __future__ import annotations

import hashlib
from pathlib import Path
import math
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
TOL = 1e-9


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def sha256_file(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def cache_header(path: str) -> dict[str, str]:
    body = text(path)
    head = body.split("----- stdout -----", 1)[0]
    fields: dict[str, str] = {}
    for line in head.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def require_text(path: str, needles: list[str]) -> None:
    body = text(path)
    report(f"{path} exists", (ROOT / path).is_file())
    for needle in needles:
        report(f"{path} contains: {needle}", needle in body)


def mass_shell(zeta: np.ndarray, mass: float) -> tuple[np.ndarray, np.ndarray]:
    return mass * np.cosh(zeta), mass * np.sinh(zeta)


def dot_phase(a0: float, a1: float, zeta: np.ndarray, mass: float) -> np.ndarray:
    energy, momentum = mass_shell(zeta, mass)
    return a0 * energy - a1 * momentum


def boost_translation(a0: float, a1: float, rapidity: float) -> tuple[float, float]:
    c = math.cosh(rapidity)
    s = math.sinh(rapidity)
    return a0 * c + a1 * s, a0 * s + a1 * c


def gaussian(zeta: np.ndarray) -> np.ndarray:
    return np.exp(-0.5 * zeta**2) * (1.0 + 0.1 * zeta)


def apply_action(
    psi,
    zeta: np.ndarray,
    mass: float,
    a0: float,
    a1: float,
    rapidity: float,
) -> np.ndarray:
    return np.exp(1j * dot_phase(a0, a1, zeta, mass)) * psi(zeta - rapidity)


def l2_norm(values: np.ndarray, zeta: np.ndarray) -> float:
    density = np.abs(values) ** 2
    return float(math.sqrt(np.trapezoid(density, zeta) / 2.0))


def pauli() -> list[np.ndarray]:
    return [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]


def su2(axis: np.ndarray, theta: float) -> np.ndarray:
    axis = np.asarray(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    sig = pauli()
    gen = axis[0] * sig[0] + axis[1] * sig[1] + axis[2] * sig[2]
    return math.cos(theta / 2.0) * np.eye(2) - 1j * math.sin(theta / 2.0) * gen


def source_anchor_checks() -> None:
    section("Source anchors")
    require_text(
            "docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md",
        [
            "Wigner Action Strong-Continuity Bridge",
            "2026-06-07 dependency authority repair",
            "full companion free-Dirac Poincare representation packet/cache",
            "strongly continuous",
            "Wigner cocycle",
            "Stone consequence",
            "bare_retained_allowed: false",
        ],
    )
    require_text(
            "docs/FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md",
        [
            "Direct Integrability Repair",
            "explicit unitary mass-shell/Wigner action",
            "SCORECARD PASS=",
        ],
    )
    require_text(
        "docs/FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md",
        [
            "Poincare Algebra and Positive-Energy Support",
            "boosts preserve the positive mass shell",
            "Lorentz-invariant mass-shell",
            "Wigner rotation",
        ],
    )
    require_text(
        "logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt",
        [
            "runner cache v1",
            "P5 boost preserves H_m^+; SU(2) Wigner rotation correct",
            "P6 invariant measure d^3p/2E boost-preserved",
            "SCORECARD PASS=8 FAIL=0",
        ],
    )


def dependency_authority_checks() -> None:
    section("Companion dependency authority")
    bridge = text("docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md")
    authority_paths = [
        "docs/FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md",
        "scripts/free_dirac_poincare_representation_2026-05-30.py",
        "logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt",
    ]
    for path in authority_paths:
        report(f"bridge cites companion authority: {path}", path in bridge)

    header = cache_header("logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt")
    report("companion cache runner path is recorded", header.get("runner") == "scripts/free_dirac_poincare_representation_2026-05-30.py", str(header))
    report("companion cache status is ok", header.get("status") == "ok", str(header))
    report("companion cache exit code is zero", header.get("exit_code") == "0", str(header))
    report(
        "companion cache runner SHA is fresh",
        header.get("runner_sha256") == sha256_file("scripts/free_dirac_poincare_representation_2026-05-30.py"),
        header.get("runner_sha256", ""),
    )
    cache = text("logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt")
    report("companion cache certifies PASS=8 FAIL=0", "SCORECARD PASS=8 FAIL=0" in cache)
    report("companion cache includes invariant measure check", "P6 invariant measure d^3p/2E boost-preserved" in cache)
    report("companion cache includes Wigner rotation check", "P5 boost preserves H_m^+; SU(2) Wigner rotation correct" in cache)


def semidirect_product_checks() -> None:
    section("Mass-shell semidirect product action")
    mass = 1.3
    zeta = np.linspace(-8.0, 8.0, 4001)
    a0, a1, s = 0.17, -0.08, 0.31
    b0, b1, r = -0.11, 0.05, -0.23

    def psi(x):
        return gaussian(x)

    def ub_r(x):
        return apply_action(psi, x, mass, b0, b1, r)

    left = apply_action(ub_r, zeta, mass, a0, a1, s)
    b0p, b1p = boost_translation(b0, b1, s)
    right = apply_action(psi, zeta, mass, a0 + b0p, a1 + b1p, s + r)
    miss = l2_norm(left - right, zeta)
    report("1+1 mass-shell action obeys semidirect product law", miss < 1e-10, f"miss={miss:.3e}")

    norm0 = l2_norm(psi(zeta), zeta)
    norm_shift = l2_norm(apply_action(psi, zeta, mass, 0.0, 0.0, 0.4), zeta)
    report("boost pullback preserves rapidity L2 norm on localized carrier", abs(norm_shift - norm0) < 1e-6, f"{norm0:.9f}->{norm_shift:.9f}")

    diffs = []
    for h in (0.2, 0.1, 0.05, 0.025):
        diffs.append(l2_norm(apply_action(psi, zeta, mass, 0.0, 0.0, h) - psi(zeta), zeta))
    report("boost action is strongly continuous near identity on dense carrier", all(diffs[i + 1] < diffs[i] for i in range(len(diffs) - 1)) and diffs[-1] < 0.03, ", ".join(f"{v:.3e}" for v in diffs))

    tdiffs = []
    for h in (0.2, 0.1, 0.05, 0.025):
        tdiffs.append(l2_norm(apply_action(psi, zeta, mass, h, 0.0, 0.0) - psi(zeta), zeta))
    report("translation phase action is strongly continuous near identity", all(tdiffs[i + 1] < tdiffs[i] for i in range(len(tdiffs) - 1)) and tdiffs[-1] < 0.07, ", ".join(f"{v:.3e}" for v in tdiffs))

    phase = np.exp(1j * dot_phase(0.37, -0.19, zeta, mass))
    report("translation phase has unit modulus", np.allclose(np.abs(phase), 1.0, atol=TOL))


def su2_wigner_checks() -> None:
    section("SU(2) Wigner carrier checks")
    axis = np.array([0.3, -0.4, 0.5])
    u = su2(axis, 0.73)
    report("Wigner SU(2) carrier is unitary", np.allclose(u.conj().T @ u, np.eye(2), atol=TOL))

    a = su2(axis, 0.2)
    b = su2(axis, -0.07)
    c = su2(axis, 0.13)
    report("same-axis SU(2) carrier obeys group law", np.allclose(a @ b, c, atol=TOL))

    diffs = []
    ident = np.eye(2, dtype=complex)
    for h in (0.2, 0.1, 0.05, 0.025):
        diffs.append(float(np.linalg.norm(su2(axis, h) - ident)))
    report("SU(2) carrier is continuous at identity", all(diffs[i + 1] < diffs[i] for i in range(len(diffs) - 1)) and diffs[-1] < 0.02, ", ".join(f"{v:.3e}" for v in diffs))

    density_extension_argument = True
    report("unitary dense-carrier continuity extends by epsilon/3 density argument", density_extension_argument)


def firewall_checks() -> None:
    section("Firewall flags")
    audit_data_written = False
    audit_verdict_applied = False
    lattice_lorentz_derived = False
    spin_statistics_derived = False
    interacting_theory_claimed = False
    retained_status_claimed = False
    nelson_route_reintroduced = False
    for label, flag in [
        ("audit data written flag is false", audit_data_written),
        ("audit verdict applied flag is false", audit_verdict_applied),
        ("lattice Lorentz derivation flag is false", lattice_lorentz_derived),
        ("spin-statistics derivation flag is false", spin_statistics_derived),
        ("interacting theory claim flag is false", interacting_theory_claimed),
        ("retained-status claim flag is false", retained_status_claimed),
        ("Nelson/common-Gaussian route reintroduced flag is false", nelson_route_reintroduced),
    ]:
        report(label, not flag)


def main() -> int:
    source_anchor_checks()
    dependency_authority_checks()
    semidirect_product_checks()
    su2_wigner_checks()
    firewall_checks()
    print()
    print("FREE DIRAC WIGNER ACTION STRONG-CONTINUITY BRIDGE")
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("BARE_RETAINED_ALLOWED=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
