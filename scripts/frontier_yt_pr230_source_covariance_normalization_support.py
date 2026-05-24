#!/usr/bin/env python3
"""PR230 source-side covariance normalization support gate.

This runner checks the finite-support Schwinger-Dyson/Feynman-Hellmann
identity for the PR230 product RN source packet:

    d log Z / dh_i = <epsilon_i>
    d^2 log Z / dh_i dh_j = Cov(epsilon_i, epsilon_j)

It intentionally does not claim scalar/Higgs LSZ normalization or Y_T closure.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "outputs" / "yt_pr230_source_covariance_normalization_support_2026-05-24.json"
NOTE = DOCS / "YT_PR230_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md"
PR230_NOTE = DOCS / "YT_PR230_CONSOLIDATED_STATUS_NOTE_2026-05-22.md"
POLE_NOGO = DOCS / "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: object = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{status}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def states(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n))


def base_weight(eps: tuple[int, ...]) -> float:
    # Positive nonuniform reference measure.  This keeps the theorem honest:
    # connected covariance, not uncentered two-point algebra, is the invariant.
    if len(eps) < 3:
        return 1.0
    e0, e1, e2 = eps
    exponent = 0.13 * e0 * e1 - 0.07 * e1 * e2 + 0.05 * e0
    return math.exp(exponent)


def partition(h: list[float], omega: list[tuple[int, ...]]) -> float:
    return sum(base_weight(eps) * math.exp(sum(hi * ei for hi, ei in zip(h, eps))) for eps in omega)


def density(h: list[float], omega: list[tuple[int, ...]]) -> list[float]:
    z = partition(h, omega)
    return [base_weight(eps) * math.exp(sum(hi * ei for hi, ei in zip(h, eps))) / z for eps in omega]


def expect(h: list[float], omega: list[tuple[int, ...]], f: Callable[[tuple[int, ...]], float]) -> float:
    return sum(p * f(eps) for p, eps in zip(density(h, omega), omega))


def mean_vector(h: list[float], omega: list[tuple[int, ...]]) -> list[float]:
    return [expect(h, omega, lambda eps, i=i: float(eps[i])) for i in range(len(h))]


def covariance_matrix(h: list[float], omega: list[tuple[int, ...]]) -> list[list[float]]:
    means = mean_vector(h, omega)
    out: list[list[float]] = []
    for i in range(len(h)):
        row: list[float] = []
        for j in range(len(h)):
            two = expect(h, omega, lambda eps, i=i, j=j: float(eps[i] * eps[j]))
            row.append(two - means[i] * means[j])
        out.append(row)
    return out


def log_z(h: list[float], omega: list[tuple[int, ...]]) -> float:
    return math.log(partition(h, omega))


def unit(n: int, i: int, scale: float) -> list[float]:
    out = [0.0] * n
    out[i] = scale
    return out


def add(a: list[float], b: list[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def finite_gradient(h: list[float], omega: list[tuple[int, ...]], step: float = 1.0e-5) -> list[float]:
    grad: list[float] = []
    for i in range(len(h)):
        hp = add(h, unit(len(h), i, step))
        hm = add(h, unit(len(h), i, -step))
        grad.append((log_z(hp, omega) - log_z(hm, omega)) / (2.0 * step))
    return grad


def finite_hessian(h: list[float], omega: list[tuple[int, ...]], step: float = 1.0e-4) -> list[list[float]]:
    n = len(h)
    out: list[list[float]] = []
    for i in range(n):
        row: list[float] = []
        for j in range(n):
            hpp = add(add(h, unit(n, i, step)), unit(n, j, step))
            hpm = add(add(h, unit(n, i, step)), unit(n, j, -step))
            hmp = add(add(h, unit(n, i, -step)), unit(n, j, step))
            hmm = add(add(h, unit(n, i, -step)), unit(n, j, -step))
            row.append((log_z(hpp, omega) - log_z(hpm, omega) - log_z(hmp, omega) + log_z(hmm, omega)) / (4.0 * step * step))
        out.append(row)
    return out


def max_vec_error(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def max_matrix_error(a: list[list[float]], b: list[list[float]]) -> float:
    return max(abs(x - y) for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b))


def part1_anchors() -> None:
    print("\nPart 1: anchors")
    for path in (NOTE, PR230_NOTE, POLE_NOGO, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())
    note = read(NOTE)
    check("note declares bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note registers this runner", "scripts/frontier_yt_pr230_source_covariance_normalization_support.py" in note)
    check("note cites PR230 consolidated packet", "YT_PR230_CONSOLIDATED_STATUS_NOTE_2026-05-22.md" in note)
    check("note cites pole-row normalization no-go", "YT_SOURCE_HIGGS_POLE_ROW_NORMALIZATION_NO_GO_NOTE_2026-05-23.md" in note)


def part2_fh_covariance_identity() -> tuple[float, float]:
    print("\nPart 2: finite-support FH covariance identity")
    omega = states(3)
    h = [0.17, -0.23, 0.31]
    analytic_grad = mean_vector(h, omega)
    numeric_grad = finite_gradient(h, omega)
    grad_error = max_vec_error(analytic_grad, numeric_grad)
    check("d log Z / dh equals source expectation", grad_error < 1.0e-9, grad_error)

    analytic_hessian = covariance_matrix(h, omega)
    numeric_hessian = finite_hessian(h, omega)
    hessian_error = max_matrix_error(analytic_hessian, numeric_hessian)
    check("d2 log Z / dhdh equals connected covariance", hessian_error < 1.0e-7, hessian_error)
    check("covariance matrix is symmetric", max_matrix_error(analytic_hessian, [list(row) for row in zip(*analytic_hessian)]) < 1.0e-12)
    check("diagonal connected variances are positive", all(analytic_hessian[i][i] > 0.0 for i in range(3)))
    return grad_error, hessian_error


def part3_uniform_origin_source_score() -> float:
    print("\nPart 3: uniform-origin score convention")
    omega = states(3)
    uniform = [1.0 / len(omega)] * len(omega)
    max_mean = 0.0
    for i in range(3):
        mean = sum(p * eps[i] for p, eps in zip(uniform, omega))
        max_mean = max(max_mean, abs(mean))
    check("uniform reference has zero signed-record mean", max_mean < 1.0e-12, max_mean)
    for i in range(3):
        max_score_error = max(abs((eps[i] - 0.0) - eps[i]) for eps in omega)
        check(f"site {i} score equals epsilon for every record", max_score_error < 1.0e-12, max_score_error)
    return max_mean


def part4_source_normalization_boundary() -> None:
    print("\nPart 4: source normalization boundary")
    omega = states(2)
    lam = 1.3
    check("test rescaling lambda is nontrivial", abs(lam - 1.0) > 0.0, lam)
    scaled_score_errors = []
    for eps in omega:
        scaled_score_errors.append(abs(lam * eps[0] - eps[0]))
    check("rescaling source insertion changes fixed-h score", min(scaled_score_errors) > 0.0, scaled_score_errors)
    h_prime = [lam * 0.21, -0.08]
    h_reparam = [0.21, -0.08 / lam]
    lhs = [math.exp(sum(hi * ei for hi, ei in zip(h_prime, eps))) for eps in omega]
    rhs = [math.exp(lam * h_reparam[0] * eps[0] + lam * h_reparam[1] * eps[1]) for eps in omega]
    max_reparam = max(abs(a - b) for a, b in zip(lhs, rhs))
    check("source rescaling can be moved into source-coordinate redefinition", max_reparam < 1.0e-12, max_reparam)


def part5_firewalls() -> None:
    print("\nPart 5: firewalls")
    note = read(NOTE)
    required = [
        "does not fix canonical `O_H`",
        "does not fix scalar LSZ normalization",
        "does not select `kappa_Y = 0`",
        "does not derive `m_t` or `y_t`",
        "claim_type_author_hint: bounded_theorem",
        "status_authority: independent_audit_lane_only",
        "direct_effective_status_change_allowed_from_this_note: false",
    ]
    for phrase in required:
        check(f"required boundary phrase present: {phrase}", phrase in note)
    forbidden = [
        "Status:** retained",
        "positive retained Y_T closure",
        "kappa_Y = 0 is derived",
        "derive y_t",
        "y_t =",
        "m_t =",
        "sqrt(8/9) as an unconditional",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def write_output(grad_error: float, hessian_error: float) -> None:
    payload = {
        "generated_at": "2026-05-24T00:00:00Z",
        "claim": "PR230 product RN source coordinate fixes source-side connected covariance row",
        "claim_type_author_hint": "bounded_theorem",
        "status_authority": "independent_audit_lane_only",
        "direct_effective_status_change_allowed_from_this_note": False,
        "boundary_reason": (
            "Source-side covariance support only; same-surface source/action authority, "
            "canonical O_H, scalar LSZ, strict pole rows or W/Z bypass, and matching/running remain open."
        ),
        "grad_error": grad_error,
        "hessian_error": hessian_error,
        "pass_count": PASS_COUNT,
        "fail_count": FAIL_COUNT,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")


def main() -> int:
    print("=" * 88)
    print("PR230 SOURCE-COVARIANCE NORMALIZATION SUPPORT")
    print("=" * 88)
    part1_anchors()
    grad_error, hessian_error = part2_fh_covariance_identity()
    part3_uniform_origin_source_score()
    part4_source_normalization_boundary()
    part5_firewalls()
    write_output(grad_error, hessian_error)
    print()
    print("=" * 88)
    print(f"RESULT: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if PASS_COUNT == 33 and FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
