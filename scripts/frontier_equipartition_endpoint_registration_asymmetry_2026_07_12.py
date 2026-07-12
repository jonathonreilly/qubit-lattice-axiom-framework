#!/usr/bin/env python3
"""Exact checks for the tied-section equipartition endpoint asymmetry.

This runner proves only finite algebra and trigonometric identities.  The
spectral-to-record identification and either branch convention are declared
modeling elements; running these checks does not adopt either element or set
an audit status.
"""

from __future__ import annotations

import sys

import sympy as sp


PASS = 0
FAIL = 0
CHECK = 0


def exact_zero(expr: sp.Expr) -> bool:
    """Return whether SymPy reduces an exact expression to zero."""

    reduced = sp.trigsimp(sp.expand_trig(expr), method="fu")
    return sp.simplify(reduced) == 0


def report(label: str, condition: bool, detail: str = "") -> None:
    """Print one numbered exact check and update the scorecard."""

    global PASS, FAIL, CHECK
    CHECK += 1
    if bool(condition):
        PASS += 1
        print(f"[{CHECK:02d}] [PASS] {label}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[{CHECK:02d}] [FAIL] {label}{suffix}")


def all_zero(expressions: list[sp.Expr]) -> bool:
    return all(exact_zero(expr) for expr in expressions)


def all_distinct(values: list[sp.Expr]) -> bool:
    return all(
        not exact_zero(values[i] - values[j])
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )


# Structural symbols.  The theorem assumes a > 0, rho = |b| >= 0, and
# r = rho**2/a**2.  No empirical values enter the runner.
a = sp.symbols("a", positive=True, real=True)
rho = sp.symbols("rho", nonnegative=True, real=True)
r = sp.symbols("r", nonnegative=True, real=True)
theta = sp.symbols("theta", real=True)
d = sp.symbols("d", nonnegative=True, real=True)
pi = sp.pi


def lam(k: int, angle: sp.Expr = theta, radius: sp.Expr = rho) -> sp.Expr:
    return a + 2 * radius * sp.cos(angle + 2 * pi * k / 3)


lams = [lam(k) for k in range(3)]


# 1--4: phase covariance, theta-free traces, and the conditional Q identity.
shifted = [lam(k, theta + 2 * pi / 3) for k in range(3)]
rotated = [lams[1], lams[2], lams[0]]
report(
    "theta -> theta + 2*pi/3 only permutes the tied spectrum",
    all_zero([shifted[k] - rotated[k] for k in range(3)]),
)

sum_lam = sp.trigsimp(sum(lams), method="fu")
report("sum_k lambda_k = 3*a is theta-free", exact_zero(sum_lam - 3 * a))

sum_lam_sq = sp.trigsimp(sum(value**2 for value in lams), method="fu")
report(
    "sum_k lambda_k**2 = 3*a**2 + 6*|b|**2 is theta-free",
    exact_zero(sum_lam_sq - (3 * a**2 + 6 * rho**2)),
)

q_signed = sp.simplify(sum_lam_sq / sum_lam**2)
q_in_r = sp.simplify(q_signed.subs(rho, a * sp.sqrt(r)))
report(
    "on sqrt(m)=lambda, Q=(1+2*r)/3",
    exact_zero(q_in_r - (1 + 2 * r) / 3),
)


# 5--13: exact reduced-sector minimum and complete general-r window.
# Reduce theta modulo 2*pi/3 and reflect so 0 <= d <= pi/3.  The three
# cosines are then the following set.  The displayed gaps are nonnegative on
# that interval, proving c_min is the minimum without numerical sampling.
c0 = sp.cos(d)
c_plus = sp.cos(2 * pi / 3 + d)
c_minus = sp.cos(2 * pi / 3 - d)
gap_0 = sp.Rational(3, 2) * sp.cos(d) + sp.sqrt(3) * sp.sin(d) / 2
gap_minus = sp.sqrt(3) * sp.sin(d)
report(
    "reduced-sector cosine gaps have manifest nonnegative forms",
    all_zero([c0 - c_plus - gap_0, c_minus - c_plus - gap_minus]),
)

c_envelope = -sp.cos(pi / 3 - d)
report(
    "min_k cos(theta+2*pi*k/3) = -cos(pi/3-delta)",
    exact_zero(c_plus - c_envelope),
)

lambda_min = sp.simplify(a + 2 * rho * c_envelope)
report(
    "the spectral minimum decreases monotonically across 0<=delta<=pi/3",
    exact_zero(sp.diff(lambda_min, d) + 2 * rho * sp.sin(pi / 3 - d)),
)

report(
    "the best and worst phase minima are a-|b| and a-2|b|",
    all_zero(
        [
            lambda_min.subs(d, 0) - (a - rho),
            lambda_min.subs(d, pi / 3) - (a - 2 * rho),
        ]
    ),
)

alpha = pi / 3 - sp.acos(a / (2 * rho))
report(
    "for |b|<a<2|b|, delta=alpha is the exact zero boundary",
    exact_zero(lambda_min.subs(d, alpha)),
)

report(
    "the intermediate half-width runs from pi/3 to 0",
    exact_zero(alpha.subs(a, 2 * rho) - pi / 3)
    and exact_zero(alpha.subs(a, rho)),
)

report(
    "the worst-phase zero is a=2|b| (the all-phase threshold)",
    exact_zero(lambda_min.subs(d, pi / 3) - (a - 2 * rho)),
)

report(
    "the best-phase zero is a=|b| (the open-window threshold)",
    exact_zero(lambda_min.subs(d, 0) - (a - rho))
    and exact_zero(lambda_min.subs(d, pi / 3) - (a - 2 * rho)),
    "The equivalence follows from the monotone envelope on 0<=delta<=pi/3.",
)

rho_zero_lams = [sp.simplify(value.subs(rho, 0)) for value in lams]
report(
    "r=0 is the all-positive but fully degenerate special case",
    all_zero([value - a for value in rho_zero_lams]),
)


# 14--19: the r=1/2 and r=1 endpoint comparison, including degeneracy.
alpha_r = pi / 3 - sp.acos(1 / (2 * sp.sqrt(r)))
report(
    "r=1/2 has exact half-width pi/12",
    exact_zero(alpha_r.subs(r, sp.Rational(1, 2)) - pi / 12),
)

rhalf_radius = a / sp.sqrt(2)
rhalf_boundary = [lam(k, pi / 12, rhalf_radius) for k in range(3)]
report(
    "the r=1/2 boundary has one exact zero and no negative eigenvalue",
    any(exact_zero(value) for value in rhalf_boundary)
    and all(bool(sp.simplify(value >= 0)) for value in rhalf_boundary),
)

pair_difference_product = (
    (lams[0] - lams[1])
    * (lams[0] - lams[2])
    * (lams[1] - lams[2])
)
disc_target = -6 * sp.sqrt(3) * rho**3 * sp.sin(3 * theta)
report(
    "the spectrum is distinct iff |b|>0 and sin(3*theta)!=0",
    exact_zero(pair_difference_product - disc_target),
)

rhalf_q = sp.simplify(q_in_r.subs(r, sp.Rational(1, 2)))
report("r=1/2 pins Q=2/3 on the positive branch", rhalf_q == sp.Rational(2, 3))

rone_radius = a
rone_center = [sp.trigsimp(lam(k, 0, rone_radius)) for k in range(3)]
report(
    "r=1 has only the zero-width phase set and spectrum (3*a,0,0)",
    exact_zero(alpha_r.subs(r, 1))
    and all_zero(
        [
            rone_center[0] - 3 * a,
            rone_center[1],
            rone_center[2],
        ]
    ),
)

rone_registered = [sp.expand(value**2) for value in rone_center]
report(
    "r=1 positive-branch registration is doublet-degenerate",
    exact_zero(rone_registered[1] - rone_registered[2])
    and exact_zero(rone_registered[1]),
)


# 20--23: sign-allowed branch at r=1.  Normalize a=1; scale cancels from Q.
def normalized_rone(angle: sp.Expr) -> list[sp.Expr]:
    return [sp.trigsimp(1 + 2 * sp.cos(angle + 2 * pi * k / 3)) for k in range(3)]


pi6_lam = normalized_rone(pi / 6)
pi6_expected = [1 + sp.sqrt(3), 1 - sp.sqrt(3), 1]
pi6_m = [sp.expand(value**2) for value in pi6_lam]
pi6_m_expected = [4 + 2 * sp.sqrt(3), 4 - 2 * sp.sqrt(3), 1]
report(
    "sign branch at theta=pi/6 gives the exact supervisor spectrum",
    all_zero([pi6_lam[k] - pi6_expected[k] for k in range(3)])
    and all_zero([pi6_m[k] - pi6_m_expected[k] for k in range(3)]),
)

pi6_abs_sum = sp.simplify(sum(sp.Abs(value) for value in pi6_lam))
pi6_q = sp.simplify(sum(pi6_m) / pi6_abs_sum**2)
report(
    "theta=pi/6 is non-degenerate and Q=9/(13+4*sqrt(3))",
    all_distinct(pi6_m)
    and exact_zero(pi6_abs_sum - (1 + 2 * sp.sqrt(3)))
    and exact_zero(pi6_q - 9 / (13 + 4 * sp.sqrt(3))),
)

pi12_lam = normalized_rone(pi / 12)
pi12_m = [sp.expand(value**2) for value in pi12_lam]
pi12_abs_sum = sp.simplify(sum(sp.Abs(value) for value in pi12_lam))
pi12_q = sp.simplify(sum(pi12_m) / pi12_abs_sum**2)
report(
    "theta=pi/12 is a second exact non-degenerate sign-branch point",
    bool(sp.simplify(pi12_lam[0] > 0))
    and bool(sp.simplify(pi12_lam[1] < 0))
    and bool(sp.simplify(pi12_lam[2] > 0))
    and all_distinct(pi12_m),
)

report(
    "the two non-degenerate sign-branch points have different exact Q",
    exact_zero(pi12_abs_sum - (1 + 2 * sp.sqrt(2)))
    and exact_zero(pi12_q - 9 / (9 + 4 * sp.sqrt(2)))
    and not exact_zero(pi12_q - pi6_q),
)


print("RESIDUAL (declared-open): sqrt(m_k)=lambda_k is this note's unadopted bridge element.")
print("RESIDUAL (declared-open): lambda_k>=0 is the positive-branch convention.")
print("RESIDUAL (declared-open): the three-distinct-value comparator is named, not thresholded.")
print("RESIDUAL (declared-open): the equipartition/dial law still selects neither endpoint.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
if FAIL == 0:
    print(
        "VERDICT: exact tied-section asymmetry verified conditionally: r=1 has no "
        "non-degenerate positive-branch registration, r=1/2 has an open one with "
        "Q=2/3, and the sign branch restores non-degeneracy at r=1 only by making "
        "Q phase-dependent. No premise is adopted and no audit status is set."
    )
else:
    print("VERDICT: verification failed; no theorem verdict is available.")

sys.exit(0 if FAIL == 0 else 1)
