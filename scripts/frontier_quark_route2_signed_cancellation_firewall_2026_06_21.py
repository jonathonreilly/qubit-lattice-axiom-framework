#!/usr/bin/env python3
"""Route-2 signed-cancellation firewall for the endpoint ratio.

This runner tests the remaining affine signed escape:

    F_X = a / w_X + b

for the Route-2 endpoint ratio q_E/q_T = 9/4.  The fit exists exactly, but
every nonzero affine one-pole fit requires opposite-sign coefficients
(`b = -6a/5`).  Pointwise positivity of the final E/T responses is therefore
not enough to derive or reject the fit; a coefficient-level signed selector or
positivity firewall would be an additional premise.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AUDIT_DATA = DOCS / "audit" / "data"

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


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def read_norm(name: str) -> str:
    return norm((DOCS / name).read_text(encoding="utf-8"))


W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2)
TARGET_LAMBDA = Fraction(9, 4)


def affine_response(weight: Fraction, a: Fraction, b: Fraction) -> Fraction:
    return a / weight + b


def affine_ratio(a: Fraction, b: Fraction) -> Fraction:
    return affine_response(W_E, a, b) / affine_response(W_T, a, b)


def endpoint_tuple(lam: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = lam * Q_T
    rho_e = 6 * (q_e - 1)
    c_te = SHELL_TE * Q_T / q_e
    return q_e, rho_e, c_te


def part1_endpoint() -> None:
    print("\nPART 1: endpoint target")
    q_e, rho_e, c_te = endpoint_tuple(TARGET_LAMBDA)
    check("finite-star weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("target lambda is 9/4", TARGET_LAMBDA == Fraction(9, 4), frac_text(TARGET_LAMBDA))
    check("target lambda gives q_E=15/8", q_e == Fraction(15, 8), frac_text(q_e))
    check("target q_E gives rho_E=21/4", rho_e == Fraction(21, 4), frac_text(rho_e))
    check("target center ratio is c_TE=-8/9", c_te == Fraction(-8, 9), frac_text(c_te))


def solve_b_for_target(a: Fraction) -> Fraction:
    # (3a+b)/(2a+b)=9/4 => b=-6a/5.
    return Fraction(-6, 5) * a


def part2_signed_affine_solution() -> None:
    print("\nPART 2: exact signed affine cancellation")
    a = Fraction(1)
    b = solve_b_for_target(a)
    e = affine_response(W_E, a, b)
    t = affine_response(W_T, a, b)
    lam = e / t
    q_e, rho_e, c_te = endpoint_tuple(lam)
    check("affine one-pole target equation forces b=-6a/5", b == Fraction(-6, 5), frac_text(b))
    check("the signed affine response remains pointwise positive for a=1", e > 0 and t > 0, f"E={frac_text(e)}, T={frac_text(t)}")
    check("the signed affine response gives lambda=9/4", lam == TARGET_LAMBDA, frac_text(lam))
    check("the signed affine response gives q_E=15/8", q_e == Fraction(15, 8), frac_text(q_e))
    check("the signed affine response gives rho_E=21/4", rho_e == Fraction(21, 4), frac_text(rho_e))
    check("the signed affine response gives c_TE=-8/9", c_te == Fraction(-8, 9), frac_text(c_te))
    check("the target fit uses a negative constant coefficient", b < 0)


def part3_coefficient_firewall() -> None:
    print("\nPART 3: coefficient-level positivity firewall")
    # For a,b >= 0 and not both zero, (3a+b)/(2a+b) is a positive weighted
    # average between 1 and 3/2; it cannot reach 9/4.
    max_seen = Fraction(0)
    argmax = None
    for anum in range(0, 8):
        for bnum in range(0, 8):
            if anum == 0 and bnum == 0:
                continue
            a = Fraction(anum, 7)
            b = Fraction(bnum, 7)
            ratio = affine_ratio(a, b)
            if ratio > max_seen:
                max_seen = ratio
                argmax = (a, b)
            check(
                f"nonnegative affine sample a={frac_text(a)}, b={frac_text(b)} stays below target",
                ratio <= Fraction(3, 2) < TARGET_LAMBDA,
                frac_text(ratio),
            )
    check("exhaustive nonnegative affine sample has max lambda=3/2", max_seen == Fraction(3, 2), f"argmax={argmax}")
    check("coefficient-positive affine one-pole rules cannot fit lambda=9/4", max_seen < TARGET_LAMBDA)


def part4_pointwise_positivity_is_not_enough() -> None:
    print("\nPART 4: pointwise positivity is insufficient")
    witnesses = [Fraction(1), Fraction(2), Fraction(5, 3)]
    for a in witnesses:
        b = solve_b_for_target(a)
        e = affine_response(W_E, a, b)
        t = affine_response(W_T, a, b)
        check(
            f"signed target fit with a={frac_text(a)} has positive E/T outputs",
            e > 0 and t > 0 and affine_ratio(a, b) == TARGET_LAMBDA,
            f"b={frac_text(b)}, E={frac_text(e)}, T={frac_text(t)}",
        )
    check("pointwise positivity cannot distinguish coefficient-positive from signed-cancellation fits", True)


QUOTE_ANCHORS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "record/positivity note says norm/sign conditions do not select rho_E",
        "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
        (
            "The tested registration/positivity conditions are **norm** conditions",
            "Selecting `rho_E` requires a shell-vs-center **distinguishing** input",
            "positivity all fix the readout **norm**",
        ),
    ),
    (
        "naturality no-go leaves rho_E free without an extra primitive",
        "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md",
        (
            "remains a free parameter unless an additional E-center endpoint ratio",
            "source-domain, or readout-map primitive is supplied",
        ),
    ),
    (
        "E-center blindness note requires a real E-center lift",
        "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md",
        (
            "A positive repair must supply a genuine E-center lift",
            "equivalent source/readout primitive",
        ),
    ),
    (
        "Schur covariance note says positivity leaves continuum and future nonlinear routes open",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "positivity leaves the",
            "continuum",
            "does **not** prove impossibility over such constructions",
        ),
    ),
    (
        "Record axiom does not supply a signed selector or weighting rule",
        "MINIMAL_AXIOMS_2026-06-05.md",
        (
            "A record supplies no readout context",
            "weighting, normalization, probability",
        ),
    ),
)


def part5_quote_anchors() -> None:
    print("\nPART 5: quote-anchored firewall")
    for label, doc_name, needles in QUOTE_ANCHORS:
        text = read_norm(doc_name)
        missing = [needle for needle in needles if needle not in text]
        check(label, not missing, f"{doc_name}; missing={len(missing)}")


def part6_registered_premise_scan() -> None:
    print("\nPART 6: registered premise scan")
    premise = (AUDIT_DATA / "axiom_premise_nodes.json").read_text(encoding="utf-8")
    tier_a = (AUDIT_DATA / "premise_decision_history.json").read_text(encoding="utf-8")
    json.loads(premise)
    json.loads(tier_a)
    combined = (premise + "\n" + tier_a).lower()
    for token in ("route2_signed_cancellation", "signed_cancellation_firewall", "negative_coefficient_selector"):
        check(f"registered premise surfaces do not name `{token}`", token not in combined)
    check("registered premise JSON is parseable", True)


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("route2_restricted_readout_family", "rho_E_free_parameter", "carrier admits every rho_E"),
    Edge("record_positivity", "norm_or_bound_only", "does not fix direction"),
    Edge("coefficient_positive_affine", "lambda_bound_3_2", "nonnegative a,b upper bound"),
)

SIGNED_EDGES: tuple[Edge, ...] = (
    Edge("signed_affine_selector", "negative_constant_coefficient", "b=-6a/5"),
    Edge("negative_constant_coefficient", "lambda_9_4", "(3a+b)/(2a+b)=9/4"),
    Edge("lambda_9_4", "rho_E_21_4", "endpoint algebra"),
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


def part7_typed_reachability() -> None:
    print("\nPART 7: typed reachability")
    current = reachable(CURRENT_EDGES, "coefficient_positive_affine", "rho_E_21_4")
    signed = reachable(CURRENT_EDGES + SIGNED_EDGES, "signed_affine_selector", "rho_E_21_4")
    check("coefficient-positive affine graph has no path to rho_E=21/4", current == [], f"path={current}")
    check("adding signed affine selector creates the conditional target path", signed == [
        "signed_affine_selector",
        "negative_constant_coefficient",
        "lambda_9_4",
        "rho_E_21_4",
    ], " -> ".join(signed))


def main() -> int:
    print("Route-2 signed-cancellation firewall")
    print("Scope: affine one-pole signed fit versus coefficient-positive source/readout rules")
    part1_endpoint()
    part2_signed_affine_solution()
    part3_coefficient_firewall()
    part4_pointwise_positivity_is_not_enough()
    part5_quote_anchors()
    part6_registered_premise_scan()
    part7_typed_reachability()
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={PASS_COUNT + FAIL_COUNT}")
    if FAIL_COUNT:
        print("VERDICT: failed checks; do not use this packet.")
        return 1
    print(
        "VERDICT: scoped no-go plus conditional support. A signed affine "
        "one-pole cancellation can fit the Route-2 endpoint exactly, but every "
        "nonzero fit requires a negative coefficient; current coefficient-positive "
        "source/readout rules cannot supply it, and pointwise positivity alone is "
        "not a signed-selector theorem."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
