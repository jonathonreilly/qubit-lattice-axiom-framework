#!/usr/bin/env python3
"""Positive source-functional cone no-go for the Route-2 endpoint.

Scope:
  finite positive channel-local source/readout functionals whose net
  channel-weight exponents satisfy p >= -1.  This includes ordinary positive
  polynomial/tracial weight dependence (p >= 0) and at most one explicit
  inverse channel-volume power (p = -1).

It does not rule out:
  * a supplied density-square primitive with p = -2;
  * signed cancellations;
  * future nonlinear tensor observables outside this exponent-cone model.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def frac_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def pow_frac(x: Fraction, p: int) -> Fraction:
    return x**p if p >= 0 else Fraction(1, x ** (-p))


def read_doc(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
R = W_E / W_T
TARGET_LAMBDA = Fraction(9, 4)
Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2)


def q_e_from_lambda(lam: Fraction) -> Fraction:
    return lam * Q_T


def rho_e_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def center_te(q_e: Fraction) -> Fraction:
    return SHELL_TE * Q_T / q_e


def response_ratio(exponents: list[int], coeffs: list[int]) -> Fraction:
    num = sum(Fraction(c) * pow_frac(W_E, p) for p, c in zip(exponents, coeffs))
    den = sum(Fraction(c) * pow_frac(W_T, p) for p, c in zip(exponents, coeffs))
    if den == 0:
        raise ValueError("zero T-channel response")
    return num / den


def exponent_ratio(p: int) -> Fraction:
    return pow_frac(R, p)


def cone_bounds(exponents: list[int]) -> tuple[Fraction, Fraction]:
    vals = [exponent_ratio(p) for p in exponents]
    return min(vals), max(vals)


def endpoint_tuple(lam: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = q_e_from_lambda(lam)
    return q_e, rho_e_from_q(q_e), center_te(q_e)


def part1_target_arithmetic() -> None:
    print("\nPART 1: endpoint target arithmetic")
    q_e, rho_e, c_te = endpoint_tuple(TARGET_LAMBDA)
    check("projector weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("channel-weight ratio w_E/w_T is 2/3", R == Fraction(2, 3), frac_text(R))
    check("target lambda is 9/4", TARGET_LAMBDA == Fraction(9, 4), frac_text(TARGET_LAMBDA))
    check("target lambda gives q_E=15/8", q_e == Fraction(15, 8), frac_text(q_e))
    check("target q_E gives rho_E=21/4", rho_e == Fraction(21, 4), frac_text(rho_e))
    check("target center ratio is c_TE=-8/9", c_te == Fraction(-8, 9), frac_text(c_te))


def part2_cone_bounds() -> None:
    print("\nPART 2: exact positive-cone exponent bounds")
    no_inverse = list(range(0, 6))
    one_inverse = list(range(-1, 6))
    two_inverse = list(range(-2, 6))

    _, max_no_inverse = cone_bounds(no_inverse)
    _, max_one_inverse = cone_bounds(one_inverse)
    _, max_two_inverse = cone_bounds(two_inverse)

    check("positive polynomial cone p>=0 has lambda <= 1", max_no_inverse == Fraction(1), frac_text(max_no_inverse))
    check("positive cone with at most one inverse-volume power has lambda <= 3/2", max_one_inverse == Fraction(3, 2), frac_text(max_one_inverse))
    check("Route-2 endpoint target 9/4 is above the p>=-1 positive-cone bound", TARGET_LAMBDA > max_one_inverse)
    check("allowing p=-2 first reaches lambda=9/4", max_two_inverse == TARGET_LAMBDA, frac_text(max_two_inverse))
    check("the p=-2 endpoint tuple is exactly the target", endpoint_tuple(max_two_inverse) == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)))


def part3_exhaustive_positive_sums() -> None:
    print("\nPART 3: exhaustive finite positive sums")
    exps_one_inverse = list(range(-1, 5))
    exps_no_inverse = list(range(0, 5))
    max_seen_one = Fraction(-10)
    argmax_one: tuple[int, ...] | None = None
    max_seen_zero = Fraction(-10)
    argmax_zero: tuple[int, ...] | None = None

    for coeffs in product(range(4), repeat=len(exps_one_inverse)):
        if not any(coeffs):
            continue
        ratio = response_ratio(exps_one_inverse, list(coeffs))
        if ratio > max_seen_one:
            max_seen_one = ratio
            argmax_one = coeffs

    for coeffs in product(range(4), repeat=len(exps_no_inverse)):
        if not any(coeffs):
            continue
        ratio = response_ratio(exps_no_inverse, list(coeffs))
        if ratio > max_seen_zero:
            max_seen_zero = ratio
            argmax_zero = coeffs

    check("exhaustive p>=-1 nonnegative coefficient scan has max lambda=3/2", max_seen_one == Fraction(3, 2), f"coeffs={argmax_one}")
    check("exhaustive p>=0 nonnegative coefficient scan has max lambda=1", max_seen_zero == Fraction(1), f"coeffs={argmax_zero}")
    check("no p>=-1 nonnegative finite sum reaches 9/4", max_seen_one < TARGET_LAMBDA)

    # A mixed example shows the convex-average mechanism: adding any less
    # singular positive term pulls the ratio below the p=-1 extremum.
    mixed = response_ratio([-1, 0, 1], [1, 1, 1])
    check("mixed positive terms sit strictly below the one-inverse extremum", mixed < Fraction(3, 2), frac_text(mixed))


def part4_endpoint_bound_consequences() -> None:
    print("\nPART 4: endpoint consequences of the p>=-1 bound")
    lam_bound = Fraction(3, 2)
    q_e, rho_e, c_te = endpoint_tuple(lam_bound)
    check("p>=-1 gives q_E<=5/4", q_e == Fraction(5, 4), frac_text(q_e))
    check("p>=-1 gives rho_E<=3/2", rho_e == Fraction(3, 2), frac_text(rho_e))
    check("p>=-1 gives center-ratio no closer than c_TE=-4/3 at the upper endpoint", c_te == Fraction(-4, 3), frac_text(c_te))
    check("target rho_E=21/4 is outside the p>=-1 endpoint range", Fraction(21, 4) > rho_e)


def part5_escape_hatches() -> None:
    print("\nPART 5: explicit escape hatches left open")
    two_density = exponent_ratio(-2)
    q_e, rho_e, c_te = endpoint_tuple(two_density)
    check("two inverse-volume powers p=-2 give lambda=9/4", two_density == TARGET_LAMBDA)
    check("two inverse-volume powers give the full endpoint target", (q_e, rho_e, c_te) == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)))

    # Signed cancellation can fit the value without p=-2:
    # R_X = 1/w_X - 6/5 gives (3-6/5)/(2-6/5)=9/4.
    signed_e = Fraction(1, W_E) - Fraction(6, 5)
    signed_t = Fraction(1, W_T) - Fraction(6, 5)
    signed_ratio = signed_e / signed_t
    check("signed cancellation can fit 9/4 without p=-2, so this no-go is positive-cone scoped", signed_ratio == TARGET_LAMBDA, f"E={frac_text(signed_e)}, T={frac_text(signed_t)}")
    check("the signed escape uses a negative coefficient", Fraction(-6, 5) < 0)


QUOTE_ANCHORS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "quadratic Schur note leaves nonlinear observables open but names inverse-square gap",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "A future genuinely **nonlinear** (non-quadratic) tensor observable",
            "`q_X",
            "w_X",
            "one power",
            "No named functional produces an",
            "inverse-square-of-projector-weight center lift.",
        ),
    ),
    (
        "E-center blindness note requires an E-center or equivalent primitive",
        "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md",
        (
            "must supply a genuine E-center lift, source-domain rule, or equivalent",
            "readout primitive.",
        ),
    ),
    (
        "naturality no-go keeps rho_E free without added primitive",
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        (
            "remains a free parameter unless an additional E-center endpoint ratio,",
            "source-domain, or readout-map primitive is supplied.",
        ),
    ),
    (
        "sign-separation note says magnitude remains open",
        "QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md",
        (
            "The magnitude remains open: sign-only gives the whole",
            "interval `c_TE < 0`, not `c_TE = -8/9`.",
        ),
    ),
    (
        "Record/color route says count is not weight",
        "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md",
        (
            "Count is not weight.",
            "Record does not supply the missing readout context.",
        ),
    ),
)


def part6_quote_anchors() -> None:
    print("\nPART 6: quote-anchored scope checks")
    for label, doc_name, anchors in QUOTE_ANCHORS:
        text = read_doc(doc_name)
        missing = [anchor for anchor in anchors if anchor not in text]
        check(label, not missing, f"{doc_name}; missing={len(missing)}")


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("oh_projector_weights", "one_inverse_bound_3_2", "at most one inverse channel-volume power"),
    Edge("one_inverse_bound_3_2", "q_E_bound_5_4", "q_E <= (3/2)(5/6)"),
    Edge("q_E_bound_5_4", "rho_E_bound_3_2", "rho_E <= 6(5/4-1)"),
)

MISSING_EDGES: tuple[Edge, ...] = (
    Edge("oh_projector_weights", "two_inverse_density_square", "explicit p=-2 density-square primitive"),
    Edge("two_inverse_density_square", "lambda_9_4", "q_E/q_T = (w_E/w_T)^-2"),
    Edge("lambda_9_4", "q_E_15_8", "with q_T=5/6"),
    Edge("q_E_15_8", "rho_E_21_4", "rho_E=6(q_E-1)"),
)


def reachable(edges: tuple[Edge, ...], source: str, target: str) -> list[str]:
    graph: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        graph[edge.source].append(edge.target)
    queue: deque[tuple[str, list[str]]] = deque([(source, [source])])
    seen = {source}
    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return []


def part7_reachability() -> None:
    print("\nPART 7: typed reachability")
    current = reachable(CURRENT_EDGES, "oh_projector_weights", "rho_E_21_4")
    with_missing = reachable(CURRENT_EDGES + MISSING_EDGES, "oh_projector_weights", "rho_E_21_4")
    check("current p>=-1 cone has no path to rho_E=21/4", current == [], f"path={current}")
    check("adding explicit p=-2 density-square primitive creates the target path", with_missing == [
        "oh_projector_weights",
        "two_inverse_density_square",
        "lambda_9_4",
        "q_E_15_8",
        "rho_E_21_4",
    ], " -> ".join(with_missing))


def main() -> int:
    print("Route-2 positive source-functional cone no-go")
    print("Scope: finite positive channel-local functionals with net exponent p >= -1")
    part1_target_arithmetic()
    part2_cone_bounds()
    part3_exhaustive_positive_sums()
    part4_endpoint_bound_consequences()
    part5_escape_hatches()
    part6_quote_anchors()
    part7_reachability()
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={PASS_COUNT + FAIL_COUNT}")
    if FAIL_COUNT:
        print("VERDICT: failed checks; do not use this packet.")
        return 1
    print(
        "VERDICT: scoped no-go. Positive finite channel-local source/readout "
        "cones with at most one inverse channel-volume power cannot reach "
        "the Route-2 endpoint lambda=9/4; the remaining live escapes require "
        "an explicit p=-2 density-square primitive, signed cancellation, or a "
        "future nonlinear observable outside this class."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
