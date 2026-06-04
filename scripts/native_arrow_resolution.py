#!/usr/bin/env python3
"""Conditional checks for the supplied heat-kernel Koide-arrow route.

This runner supports a bounded theorem only:

* sharpen(r) = 2 r^2 and thermalize(r) = sqrt(r/2) are inverse maps on
  the positive r-line.
* Their stability at r = 1/2 flips because the maps run the same
  one-dimensional flow in opposite directions.
* For the explicitly supplied heat-kernel/blocking path r(t)=tanh(t)^4,
  r=1/2 is a transit value, not an attractor.

It does not derive r(t)=tanh(t)^4 from the framework baseline, from the
single-clock theorem, or from a retained generation-sector beta theorem.
"""

from __future__ import annotations

import math

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{suffix}")
    return ok


r = sp.symbols("r", positive=True)
t = sp.symbols("t", positive=True)
a = sp.symbols("a", positive=True)
b = sp.symbols("b", real=True)


def iterate(func, seed: float, steps: int = 120) -> float:
    x = float(seed)
    for _ in range(steps):
        x = func(x)
        if not math.isfinite(x):
            return x
    return x


print("=" * 78)
print("Supplied heat-kernel Koide-arrow bounded route check")
print("Claim boundary: conditional on the displayed maps and r(t)=tanh(t)^4.")
print("No framework-native beta derivation is asserted by this runner.")
print("=" * 78)

# Koide light-cone algebra on the positive real C3 line.
spec = [a + 2 * b, a - b, a - b]
q_expr = sp.simplify(sum(s**2 for s in spec) / (sum(spec)) ** 2)
r_expr = (b / a) ** 2
q_line = sp.Rational(1, 3) + sp.Rational(2, 3) * r_expr
check(
    "Koide line Q = 1/3 + (2/3) r for the C3 circulant spectrum",
    sp.simplify(q_expr - q_line) == 0,
    f"Q={q_expr}",
)
q_half_solutions = sorted(
    {sp.simplify((bb / a) ** 2) for bb in sp.solve(sp.Eq(q_line, sp.Rational(2, 3)), b)}
)
check(
    "Q=2/3 corresponds to r=1/2 on this line",
    sp.Rational(1, 2) in q_half_solutions,
    f"r-solutions={q_half_solutions}",
)

# The two proposed one-step maps.
sharpen_map = 2 * r**2
thermalize_map = sp.sqrt(r / 2)
check("thermalize(sharpen(r)) = r on r>0", sp.simplify(sp.sqrt(sharpen_map / 2) - r) == 0)
check(
    "sharpen(thermalize(r)) = r on r>0",
    sp.simplify(2 * thermalize_map**2 - r) == 0,
)

r_free = sp.symbols("r_free", real=True)
fixed_sharpen = set(sp.solve(sp.Eq(2 * r_free**2, r_free), r_free))
fixed_thermalize = set(sp.solve(sp.Eq(r_free / 2, r_free**2), r_free))
check(
    "sharpen fixed points are {0, 1/2}",
    fixed_sharpen == {sp.Integer(0), sp.Rational(1, 2)},
    f"{sorted(fixed_sharpen, key=float)}",
)
check(
    "thermalize fixed points are {0, 1/2}",
    fixed_thermalize == {sp.Integer(0), sp.Rational(1, 2)},
    f"{sorted(fixed_thermalize, key=float)}",
)

sharpen_multiplier = sp.diff(sharpen_map, r).subs(r, sp.Rational(1, 2))
thermalize_multiplier = sp.diff(thermalize_map, r).subs(r, sp.Rational(1, 2))
check("sharpen multiplier at r=1/2 is 2", sharpen_multiplier == 2)
check("thermalize multiplier at r=1/2 is 1/2", thermalize_multiplier == sp.Rational(1, 2))
check(
    "multiplier product is 1, as expected for inverse branches",
    sp.simplify(sharpen_multiplier * thermalize_multiplier) == 1,
)

below = iterate(lambda x: 2 * x * x, 0.49)
above = iterate(lambda x: 2 * x * x, 0.51, steps=60)
therm_low = iterate(lambda x: math.sqrt(x / 2), 0.02)
therm_high = iterate(lambda x: math.sqrt(x / 2), 5.0)
check("sharpen seed below 1/2 moves toward 0", below < 1e-8, f"{below:.3e}")
check("sharpen seed above 1/2 moves upward", above > 1.0, f"{above:.3g}")
check(
    "thermalize positive seeds move toward 1/2",
    abs(therm_low - 0.5) < 1e-9 and abs(therm_high - 0.5) < 1e-9,
    f"{therm_low:.6f}, {therm_high:.6f}",
)

# Supplied heat-kernel path, not derived here.
r_of_t = sp.tanh(t) ** 4
beta_r = sp.simplify(sp.diff(r_of_t, t))
beta_expected = 4 * sp.tanh(t) ** 3 * (1 - sp.tanh(t) ** 2)
check("supplied path derivative is 4 tanh(t)^3 sech(t)^2", sp.simplify(beta_r - beta_expected) == 0)
grid_positive = all(
    4 * np.tanh(tt) ** 3 * (1 - np.tanh(tt) ** 2) > 0 for tt in np.linspace(0.05, 12.0, 400)
)
check("supplied path has beta_r > 0 for sampled finite t>0", grid_positive)
check("supplied path starts at r=0", sp.limit(r_of_t, t, 0) == 0)
check("supplied path tends to r=1", sp.limit(r_of_t, t, sp.oo) == 1)
t_half = sp.nsolve(sp.tanh(t) ** 4 - sp.Rational(1, 2), 1.2)
beta_half = float(beta_expected.subs(t, t_half))
check(
    "r=1/2 is a transit value of the supplied path",
    beta_half > 1e-3,
    f"t={float(t_half):.4f}, beta={beta_half:.4f}",
)

# Non-load-bearing consistency check: block dimensions are 1 and 2, so a
# dimension-weighted state is not the equal-power-per-block condition.
omega = np.exp(2j * np.pi / 3)
fourier = np.array(
    [[1, 1, 1], [1, omega, omega**2], [1, omega**2, omega**4]], dtype=complex
) / np.sqrt(3)
projector_singlet = fourier[:, [0]] @ fourier[:, [0]].conj().T
projector_doublet = np.eye(3) - projector_singlet
check(
    "C3 isotype block dimensions are 1 and 2",
    abs(np.trace(projector_singlet).real - 1) < 1e-9
    and abs(np.trace(projector_doublet).real - 2) < 1e-9,
)

print("=" * 78)
print("BOUNDED RESULT: under the supplied heat-kernel path, r=1/2 is not an")
print("attractor; under the thermalizing inverse branch it is an attractor.")
print("This runner does not prove which branch is framework-native.")
print("=" * 78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")

raise SystemExit(0 if FAIL == 0 else 1)
