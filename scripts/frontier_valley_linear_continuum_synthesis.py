#!/usr/bin/env python3
"""Valley-linear continuum bridge runner.

Checks the self-contained bridge in VALLEY_LINEAR_CONTINUUM_SYNTHESIS_NOTE.md:

    S = L(1-f), f=s/r
      -> delta Phi(b) = -k s [asinh((L-x_m)/b) + asinh(x_m/b)]
      -> d(delta Phi)/db -> 2 k s / b

This runner certifies only the continuum straight-ray bridge. It does not
promote the finite lattice artifacts to a universal theorem.
"""

from __future__ import annotations

import sympy as sp


def check(label: str, condition: bool, detail: str) -> bool:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}: {detail}")
    return condition


def main() -> int:
    print("=" * 80)
    print("VALLEY-LINEAR CONTINUUM SYNTHESIS BRIDGE")
    print("=" * 80)
    print("Scope: symbolic straight-ray continuum bridge only.")
    print("Not scope: universal finite-lattice or architecture-independent theorem.")
    print()

    L, f, k, s, b, x0, x1 = sp.symbols("L f k s b x0 x1", positive=True)

    passes: list[bool] = []

    delta_s = sp.expand(L * (1 - f) - L)
    passes.append(check("valley-linear perturbation is -L*f", delta_s == -L * f, str(delta_s)))

    integral = sp.asinh(x1 / b) + sp.asinh(x0 / b)
    delta_phi = -k * s * integral
    derivative = sp.simplify(sp.diff(delta_phi, b))
    expected_derivative = k * s * (
        x1 / (b * sp.sqrt(x1**2 + b**2))
        + x0 / (b * sp.sqrt(x0**2 + b**2))
    )
    passes.append(
        check(
            "derivative of continuum phase",
            sp.simplify(derivative - expected_derivative) == 0,
            str(derivative),
        )
    )

    term_x0 = x0 / (b * sp.sqrt(x0**2 + b**2))
    term_x1 = x1 / (b * sp.sqrt(x1**2 + b**2))
    limit_x0 = sp.limit(b * term_x0, x0, sp.oo)
    limit_x1 = sp.limit(b * term_x1, x1, sp.oo)
    passes.append(check("left wide-ray term tends to 1/b", limit_x0 == 1, f"b*term -> {limit_x0}"))
    passes.append(check("right wide-ray term tends to 1/b", limit_x1 == 1, f"b*term -> {limit_x1}"))

    wide_limit = sp.simplify(k * s * (limit_x0 + limit_x1) / b)
    passes.append(check("wide-ray derivative tends to 2*k*s/b", wide_limit == 2 * k * s / b, str(wide_limit)))

    # Numeric sanity check away from the symbolic limit.
    numeric_ratio = sp.N(
        derivative.subs({k: 3, s: 5, b: 2, x0: 10**6, x1: 10**6})
        / ((2 * k * s / b).subs({k: 3, s: 5, b: 2}))
    )
    passes.append(check("large-finite ray ratio is near one", abs(float(numeric_ratio) - 1.0) < 1e-10, f"{numeric_ratio}"))

    n_pass = sum(1 for item in passes if item)
    n_total = len(passes)
    print()
    print(f"PASS={n_pass} FAIL={n_total - n_pass}")
    print("Result: continuum bridge yields a 1/b straight-ray deflection scale.")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
