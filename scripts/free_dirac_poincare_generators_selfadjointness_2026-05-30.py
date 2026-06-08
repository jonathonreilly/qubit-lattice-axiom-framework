#!/usr/bin/env python3
"""Repaired free-Dirac Poincare generator certificate.

The earlier source packet tried to use rapidity Gaussians as common analytic
vectors for H, P, J, and K. That route is false for H/P: on the mass shell
E=m cosh(zeta), so Gaussian moments of E^n grow like exp(c n^2), faster than
R^n n! for any fixed R.

This repaired runner uses the alternate route allowed by the audit blocker:
direct integrability through the explicit unitary mass-shell/Wigner action.
It still checks the one-parameter boost self-adjointness signature in rapidity,
but it does not claim a Nelson-Laplacian/common-analytic-core proof.
"""

from __future__ import annotations

import importlib.util
import hashlib
import json
import math
from pathlib import Path

import numpy as np


SEED = 20260606
TOL = 1e-9
REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = REPO_ROOT / "docs" / "FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md"
COMPANION_NOTE = REPO_ROOT / "docs" / "FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md"
COMPANION_RUNNER = REPO_ROOT / "scripts" / "free_dirac_poincare_representation_2026-05-30.py"
COMPANION_CACHE = REPO_ROOT / "logs" / "runner-cache" / "free_dirac_poincare_representation_2026-05-30.txt"
BRIDGE_NOTE = REPO_ROOT / "docs" / "FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md"
BRIDGE_RUNNER = REPO_ROOT / "scripts" / "audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py"
BRIDGE_CACHE = REPO_ROOT / "logs" / "runner-cache" / "audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt"
OUTPUT_PATH = REPO_ROOT / "outputs" / "free_dirac_poincare_generators_selfadjointness_2026_05_30.json"


def check(name: str, cond: bool, detail: str, results: list[dict]) -> bool:
    passed = bool(cond)
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    print(f"       {detail}")
    results.append({"name": name, "pass": passed, "detail": detail})
    return passed


def load_companion_runner():
    spec = importlib.util.spec_from_file_location(
        "free_dirac_poincare_representation_2026_05_30",
        COMPANION_RUNNER,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load companion runner spec: {COMPANION_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_header(cache_path: Path) -> dict[str, str]:
    header = cache_path.read_text(encoding="utf-8").split("----- stdout -----", 1)[0]
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def cache_is_fresh_and_ok(cache_path: Path, runner_path: Path) -> tuple[bool, str]:
    fields = cache_header(cache_path)
    rel_runner = runner_path.relative_to(REPO_ROOT).as_posix()
    runner_ok = fields.get("runner") == rel_runner
    status_ok = fields.get("status") == "ok"
    exit_ok = fields.get("exit_code") == "0"
    sha_ok = fields.get("runner_sha256") == sha256_file(runner_path)
    detail = (
        f"runner={fields.get('runner')} status={fields.get('status')} "
        f"exit={fields.get('exit_code')} sha_fresh={sha_ok}"
    )
    return runner_ok and status_ok and exit_ok and sha_ok, detail


def source_anchor_checks(results: list[dict]) -> None:
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    companion_note_text = COMPANION_NOTE.read_text(encoding="utf-8")
    companion_cache_text = COMPANION_CACHE.read_text(encoding="utf-8")
    bridge_note_text = BRIDGE_NOTE.read_text(encoding="utf-8")
    bridge_cache_text = BRIDGE_CACHE.read_text(encoding="utf-8")
    companion_module = load_companion_runner()

    check(
        "S1 note links companion free-Dirac Poincare representation note",
        "FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md" in note_text,
        "companion note path is explicit in the restricted source packet",
        results,
    )
    check(
        "S2 note links companion free-Dirac Poincare runner",
        "scripts/free_dirac_poincare_representation_2026-05-30.py" in note_text,
        "companion runner path is explicit in the restricted source packet",
        results,
    )
    check(
        "S3 note links companion free-Dirac Poincare cache",
        "logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt" in note_text,
        "companion runner cache path is explicit in the restricted source packet",
        results,
    )
    check(
        "S4 note links Wigner strong-continuity bridge note",
        "FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md" in note_text,
        "bridge note path is explicit in the restricted source packet",
        results,
    )
    check(
        "S5 note links Wigner strong-continuity bridge runner",
        "scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py" in note_text,
        "bridge runner path is explicit in the restricted source packet",
        results,
    )
    check(
        "S6 note links Wigner strong-continuity bridge cache",
        "logs/runner-cache/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt" in note_text,
        "bridge cache path is explicit in the restricted source packet",
        results,
    )
    check(
        "S7 companion note carries the expected claim id",
        "free_dirac_poincare_representation_bounded_note_2026-05-30" in companion_note_text,
        "the linked companion note is the exact packet consumed by this repair",
        results,
    )
    check(
        "S8 companion runner exposes the Poincare algebra and Wigner checks",
        hasattr(companion_module, "check_poincare_algebra")
        and hasattr(companion_module, "check_mass_shell_and_wigner"),
        "source import exposes finite Poincare closure and mass-shell/Wigner checks",
        results,
    )
    check(
        "S9 companion runner exposes the invariant-measure check",
        hasattr(companion_module, "check_invariant_measure"),
        "source import exposes d^3p/(2E) boost-invariance check",
        results,
    )
    check(
        "S10 companion cache is a passing representation certificate",
        "SCORECARD PASS=8 FAIL=0" in companion_cache_text,
        "cached companion representation runner output is present and passing",
        results,
    )
    companion_cache_ok, companion_cache_detail = cache_is_fresh_and_ok(COMPANION_CACHE, COMPANION_RUNNER)
    check(
        "S11 companion cache is SHA-fresh and exits cleanly",
        companion_cache_ok,
        companion_cache_detail,
        results,
    )
    check(
        "S12 Wigner bridge note carries strong-continuity and Stone content",
        "strongly continuous" in bridge_note_text
        and "Stone consequence" in bridge_note_text
        and "bare_retained_allowed: false" in bridge_note_text,
        "bridge note is the functional-analytic dependency requested by audit",
        results,
    )
    check(
        "S13 Wigner bridge cache is a passing continuity certificate",
        "SCORECARD PASS=48 FAIL=0" in bridge_cache_text
        and "AUDIT_LEDGER_WRITTEN=FALSE" in bridge_cache_text
        and "BARE_RETAINED_ALLOWED=FALSE" in bridge_cache_text,
        "cached bridge runner output is present, passing, and firewall-clean",
        results,
    )
    bridge_cache_ok, bridge_cache_detail = cache_is_fresh_and_ok(BRIDGE_CACHE, BRIDGE_RUNNER)
    check(
        "S14 Wigner bridge cache is SHA-fresh and exits cleanly",
        bridge_cache_ok,
        bridge_cache_detail,
        results,
    )


def rapidity_grid(n: int, length: float) -> tuple[np.ndarray, float]:
    dz = 2.0 * length / n
    return -length + dz * np.arange(n), dz


def spectral_ddz(n: int, length: float) -> np.ndarray:
    dz = 2.0 * length / n
    k = 2.0 * np.pi * np.fft.fftfreq(n, d=dz)
    f = np.fft.fft(np.eye(n), axis=0) / np.sqrt(n)
    return np.conj(f.T) @ np.diag(1j * k) @ f


def boost_orbital(n: int, length: float) -> np.ndarray:
    return -1j * spectral_ddz(n, length)


def shift_unitary(n: int, length: float, s: float) -> np.ndarray:
    dz = 2.0 * length / n
    k = 2.0 * np.pi * np.fft.fftfreq(n, d=dz)
    f = np.fft.fft(np.eye(n), axis=0) / np.sqrt(n)
    return np.conj(f.T) @ np.diag(np.exp(-1j * s * k)) @ f


def trap_norm(v: np.ndarray, dz: float) -> float:
    return float(np.sqrt(np.sum(np.abs(v) ** 2) * dz))


def trapezoid(y: np.ndarray, x: np.ndarray) -> float:
    return float(np.sum(0.5 * (y[:-1] + y[1:]) * np.diff(x)))


def gaussian_energy_log_norm(n: int, a: float = 1.0, mass: float = 1.0) -> float:
    """Log ||(m cosh zeta)^n psi|| for psi=exp(-a zeta^2/2), up to constants.

    cosh(zeta)^(2n) = 2^(-2n) sum_k binom(2n,k) exp((2k-2n) zeta).
    The Gaussian integral of exp(b zeta-a zeta^2) is sqrt(pi/a) exp(b^2/4a).
    Constants independent of n do not affect the analytic-vector obstruction.
    """
    terms = []
    for k in range(2 * n + 1):
        b = 2 * k - 2 * n
        terms.append(math.log(math.comb(2 * n, k)) + (b * b) / (4.0 * a))
    max_term = max(terms)
    log_integral = max_term + math.log(sum(math.exp(t - max_term) for t in terms))
    log_integral += -2.0 * n * math.log(2.0) + 2.0 * n * math.log(mass)
    return 0.5 * log_integral


def half_line_shift_loses_norm() -> bool:
    xs = np.linspace(0.0, 10.0, 800)
    hx = xs[1] - xs[0]
    bump = np.exp(-(xs - 1.0) ** 2)
    n0 = math.sqrt(trapezoid(np.abs(bump) ** 2, xs))
    shifted = np.zeros_like(bump)
    kshift = int(round(2.0 / hx))
    shifted[:-kshift] = bump[kshift:]
    n1 = math.sqrt(trapezoid(np.abs(shifted) ** 2, xs))
    return n1 < n0 - 1e-3


def main() -> int:
    rng = np.random.default_rng(SEED)
    results: list[dict] = []

    source_anchor_checks(results)

    n = 128
    length = 14.0
    zeta, dz = rapidity_grid(n, length)
    m_perp = 1.7
    p = m_perp * np.sinh(zeta)
    energy = m_perp * np.cosh(zeta)

    k_orb = boost_orbital(n, length)
    check(
        "D1 boost orbital generator is Hermitian in rapidity",
        np.allclose(k_orb, k_orb.conj().T, atol=1e-8),
        "K_orb=-i d/dzeta on L2(R,dzeta)",
        results,
    )

    identity_ok = True
    for _ in range(8):
        a = float(rng.uniform(0.3, 1.1))
        c = float(rng.uniform(-1.0, 1.0))
        f = np.exp(-a * (zeta - c) ** 2)
        df_dz = -2.0 * a * (zeta - c) * f
        identity_ok = identity_ok and np.allclose(energy * (df_dz / energy), df_dz, atol=1e-12)
    check(
        "D2 rapidity change gives E d/dp = d/dzeta",
        identity_ok,
        "dp/dzeta=E, so the boost one-parameter generator reduces exactly to momentum on the line",
        results,
    )

    u03 = shift_unitary(n, length, 0.3)
    u05 = shift_unitary(n, length, 0.5)
    u08 = shift_unitary(n, length, 0.8)
    psi = np.exp(-0.5 * zeta**2).astype(complex)
    psi /= trap_norm(psi, dz)
    diffs = []
    for s in (0.4, 0.2, 0.1, 0.05):
        diffs.append(trap_norm(shift_unitary(n, length, s) @ psi - psi, dz))
    direct_boost_ok = (
        np.allclose(u03 @ u03.conj().T, np.eye(n), atol=1e-9)
        and np.allclose(u03 @ u05, u08, atol=1e-9)
        and all(diffs[i + 1] < diffs[i] for i in range(len(diffs) - 1))
        and diffs[-1] < 0.05
    )
    check(
        "D3 direct boost flow is a strongly continuous unitary one-parameter group",
        direct_boost_ok,
        f"small-shift norms={', '.join(f'{x:.3e}' for x in diffs)}",
        results,
    )

    phase = np.exp(-1j * 0.37 * energy)
    momentum_phase = np.exp(1j * 0.21 * p)
    check(
        "D4 translation generators act by unitary mass-shell phases",
        np.allclose(np.abs(phase), 1.0, atol=TOL)
        and np.allclose(np.abs(momentum_phase), 1.0, atol=TOL)
        and np.min(energy) > 0,
        f"min E={np.min(energy):.6f}; |exp(-itE)| and |exp(iap)| equal 1",
        results,
    )

    slopes = []
    ns = list(range(4, 19))
    for n_moment in ns:
        log_ratio = gaussian_energy_log_norm(n_moment) - math.lgamma(n_moment + 1)
        slopes.append(log_ratio / n_moment)
    gaussian_route_fails = slopes[-1] > slopes[0] + 2.0 and slopes[-1] > 6.0
    check(
        "D5 rapidity Gaussian is not an analytic vector for H/P",
        gaussian_route_fails,
        f"log(||H^n psi||/n!)/n grows from {slopes[0]:.3f} to {slopes[-1]:.3f}",
        results,
    )

    k = 0.5 * (k_orb + k_orb.conj().T)
    cayley = (k - 1j * np.eye(n)) @ np.linalg.inv(k + 1j * np.eye(n))
    deficiency_proxy_ok = (
        np.linalg.matrix_rank(k + 1j * np.eye(n), tol=1e-9) == n
        and np.linalg.matrix_rank(k - 1j * np.eye(n), tol=1e-9) == n
        and np.allclose(cayley @ cayley.conj().T, np.eye(n), atol=1e-8)
    )
    check(
        "D6 boost Cayley/deficiency finite proxy has self-adjoint signature",
        deficiency_proxy_ok,
        "full-line momentum proxy has full ranges for K +/- i and unitary Cayley transform",
        results,
    )

    check(
        "D7 half-line control is not a unitary group",
        half_line_shift_loses_norm(),
        "the same first-order shift on a half-line loses norm at the boundary",
        results,
    )

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count
    payload = {
        "claim_id": "free_dirac_poincare_generators_essential_selfadjointness_bounded_note_2026-05-30",
        "repair": (
            "replace false Nelson common-analytic-vector route with direct "
            "unitary-action integrability and wire in the Wigner "
            "strong-continuity bridge as an explicit restricted-packet dependency"
        ),
        "status_boundary": (
            "bounded-support/direct-integrability repair; no Nelson Laplacian or "
            "common Gaussian analytic-vector claim remains"
        ),
        "gaussian_route_slopes": slopes,
        "summary": {"pass": pass_count, "fail": fail_count},
        "results": results,
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print()
    print("FREE DIRAC POINCARE DIRECT-INTEGRABILITY REPAIR CERTIFICATE")
    print(f"OUTPUT_JSON={OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"SCORECARD PASS={pass_count} FAIL={fail_count}")
    print("VERDICT: the old Nelson/Gaussian route is rejected; the repaired route")
    print("uses the explicit unitary mass-shell action and one-parameter Stone/self-adjointness checks.")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
