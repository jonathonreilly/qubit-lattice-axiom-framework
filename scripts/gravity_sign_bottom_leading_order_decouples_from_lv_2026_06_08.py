"""Conditional order separation for gravity-sign LV corrections.

The runner verifies a narrow algebraic statement:

    omega^2(k) = c2 |k|^2 (1 + alpha A4(khat) |k|^2)

has strict k->0 leading sign sign(c2), for finite alpha. It does not derive
c2, its sign, the physical TT kernel, reflection-positivity transfer, leading
gravity isotropy, or an emergent dynamical metric.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def A4(kvec: np.ndarray) -> float:
    """Cubic anisotropy harmonic: sum k_i^4 / |k|^4 minus 3/5 in 3D."""
    k2 = float(np.dot(kvec, kvec))
    if k2 == 0.0:
        return 0.0
    return float(np.sum(kvec**4)) / (k2 * k2) - 3.0 / 5.0


def omega2(kvec: np.ndarray, c2: float, alpha: float) -> float:
    k2 = float(np.dot(kvec, kvec))
    return c2 * k2 * (1.0 + alpha * A4(kvec) * k2)


def source_guardrail() -> tuple[bool, str]:
    note = Path(
        "docs/GRAVITY_SIGN_BOTTOM_IS_LEADING_ORDER_DECOUPLES_FROM_LV_REAL_BOTTOM_IS_EMERGENT_METRIC_NARROW_THEOREM_NOTE_2026-06-08.md"
    )
    text = note.read_text(encoding="utf-8")
    required = [
        "The submitted PR claimed a broad bottom relocation",
        "That broad claim is **not landed**",
        "does not derive `c2`",
        "approved axioms and primitives do not supply",
        "conditional bounded theorem",
    ]
    missing = [marker for marker in required if marker not in text]
    return not missing, f"missing={missing}"


def main() -> int:
    print("Conditional order separation for gravity-sign LV corrections")
    print("=" * 72)

    c2 = 0.5
    alphas = [-50.0, -5.0, -1.0, 0.0, 1.0, 5.0, 50.0]
    direction = np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0)
    eps_values = np.array([1e-1, 1e-2, 1e-3, 1e-4])

    max_tiny_error = 0.0
    sign_ok = True
    for alpha in alphas:
        tiny = 1e-6 * direction
        tiny_coeff = omega2(tiny, c2, alpha) / float(np.dot(tiny, tiny))
        max_tiny_error = max(max_tiny_error, abs(tiny_coeff - c2))
        sign_ok = sign_ok and np.sign(tiny_coeff) == np.sign(c2)
    check(
        "B1 supplied leading coefficient controls the strict k->0 sign",
        sign_ok and max_tiny_error < 1e-9,
        f"tested alpha={alphas}; max tiny-k coefficient error={max_tiny_error:.3e}",
    )

    axis = np.array([1.0, 0.0, 0.0])
    alpha = 7.0
    ratios = []
    for eps in eps_values:
        kvec = eps * axis
        k2 = float(np.dot(kvec, kvec))
        relative = abs(alpha * A4(kvec) * k2)
        ratios.append(relative)
    scale_ok = ratios[1] < ratios[0] and ratios[2] < ratios[1] and ratios[3] < ratios[2]
    decade_ratios = [ratios[i] / ratios[i + 1] for i in range(len(ratios) - 1)]
    check(
        "B2 LV contribution is O(k^2) relative to the leading coefficient",
        scale_ok and all(90.0 < r < 110.0 for r in decade_ratios),
        "relative LV terms="
        + ", ".join(f"{r:.3e}" for r in ratios)
        + "; decade ratios="
        + ", ".join(f"{r:.1f}" for r in decade_ratios),
    )

    supplied_signs = []
    for supplied_c2 in (0.5, -0.5):
        tiny = 1e-6 * axis
        coeff = omega2(tiny, supplied_c2, 50.0) / float(np.dot(tiny, tiny))
        supplied_signs.append(float(np.sign(coeff)))
    check(
        "B3 result depends on the supplied c2 sign",
        supplied_signs == [1.0, -1.0],
        f"signs for supplied c2=+0.5,-0.5 are {supplied_signs}",
    )

    guard_ok, guard_detail = source_guardrail()
    check(
        "B4 source note demotes the broad wall-relocation claim",
        guard_ok,
        guard_detail,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("Boundary: conditional order-counting only. This runner does not prove G>0,")
    print("does not supply c2, and does not retire Lorentz/naturalness or dynamical-metric walls.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
