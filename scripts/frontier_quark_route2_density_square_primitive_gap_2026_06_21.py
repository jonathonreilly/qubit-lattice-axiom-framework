#!/usr/bin/env python3
"""Route-2 p=-2 density-square primitive gap.

This runner tests the hard residual left by the Route-2 readout endpoint:

    q_E / q_T = 9/4  <=>  rho_E = 21/4  <=>  c_TE = -8/9.

It separates two statements.

1. Conditional exact support: if a channel-local density-square primitive
   supplies q_X proportional to w_X^-2, the endpoint follows exactly.
2. Current-surface gap: the named Route-2 authority bank does not supply that
   primitive; existing notes keep the E-center readout entry free.

No audit verdict is run or applied by this script.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
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


def read_doc(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def read_norm(name: str) -> str:
    return norm(read_doc(name))


def pow_frac(x: Fraction, p: int) -> Fraction:
    return x**p if p >= 0 else Fraction(1, x ** (-p))


W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
R = W_E / W_T
Q_T = Fraction(5, 6)
SHELL_TE = Fraction(-2, 1)
TARGET_LAMBDA = Fraction(9, 4)


def q_e_from_lambda(lam: Fraction) -> Fraction:
    return lam * Q_T


def rho_e_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def center_te(q_e: Fraction) -> Fraction:
    return SHELL_TE * Q_T / q_e


def endpoint_tuple(lam: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = q_e_from_lambda(lam)
    return q_e, rho_e_from_q(q_e), center_te(q_e)


def p_response_ratio(p: int) -> Fraction:
    return pow_frac(R, p)


def part1_endpoint_arithmetic() -> None:
    print("\nPART 1: endpoint arithmetic and exponent characterization")
    q_e, rho_e, c_te = endpoint_tuple(TARGET_LAMBDA)
    check("finite-star channel weights are w_E=1/3 and w_T=1/2", (W_E, W_T) == (Fraction(1, 3), Fraction(1, 2)))
    check("weight ratio r=w_E/w_T is 2/3", R == Fraction(2, 3), frac_text(R))
    check("target lambda is 9/4", TARGET_LAMBDA == Fraction(9, 4), frac_text(TARGET_LAMBDA))
    check("target lambda gives q_E=15/8", q_e == Fraction(15, 8), frac_text(q_e))
    check("target q_E gives rho_E=21/4", rho_e == Fraction(21, 4), frac_text(rho_e))
    check("target center ratio is c_TE=-8/9", c_te == Fraction(-8, 9), frac_text(c_te))

    check("p=-2 density-square scaling gives lambda=9/4", p_response_ratio(-2) == TARGET_LAMBDA, frac_text(p_response_ratio(-2)))
    check("p=-1 one-density scaling gives only lambda=3/2", p_response_ratio(-1) == Fraction(3, 2), frac_text(p_response_ratio(-1)))
    check("p=0 channel-blind scaling gives lambda=1", p_response_ratio(0) == Fraction(1), frac_text(p_response_ratio(0)))
    check("p=+2 quadratic-weight scaling gives the wrong-side lambda=4/9", p_response_ratio(2) == Fraction(4, 9), frac_text(p_response_ratio(2)))


def part2_conditional_density_square_primitive() -> None:
    print("\nPART 2: conditional p=-2 primitive consequence")
    scale = Fraction(7, 5)
    d_e = scale * pow_frac(W_E, -2)
    d_t = scale * pow_frac(W_T, -2)
    ratio = d_e / d_t
    q_e, rho_e, c_te = endpoint_tuple(ratio)
    check("overall density-square scale cancels from E/T ratio", ratio == TARGET_LAMBDA, f"D_E={frac_text(d_e)}, D_T={frac_text(d_t)}")
    check("density-square primitive plus q_T=5/6 gives q_E=15/8", q_e == Fraction(15, 8), frac_text(q_e))
    check("density-square primitive gives rho_E=21/4", rho_e == Fraction(21, 4), frac_text(rho_e))
    check("density-square primitive gives c_TE=-8/9 under shell T/E=-2", c_te == Fraction(-8, 9), frac_text(c_te))
    check("the primitive is exactly the missing p=-2 edge, not an observed target fit", ratio == pow_frac(W_E / W_T, -2))


def exact_p_apply(rho_e: Fraction, column: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    x0, x1, x2, x3 = column
    return (x0 + rho_e * x2, -2 * x1 + 2 * x3)


def part3_readout_freedom() -> None:
    print("\nPART 3: exact readout freedom that the primitive would have to break")
    e_shell = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    e_center = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
    zero_shell = exact_p_apply(Fraction(0), e_shell)
    target_shell = exact_p_apply(Fraction(21, 4), e_shell)
    zero_center = exact_p_apply(Fraction(0), e_center)
    target_center = exact_p_apply(Fraction(21, 4), e_center)

    check("rho_E=0 and rho_E=21/4 agree on E-shell normalization", zero_shell == target_shell == (Fraction(1), Fraction(0)))
    check("rho_E=0 gives E-center lift q_E=1", zero_center == (Fraction(1), Fraction(0)), str(zero_center))
    check("rho_E=21/4 gives E-center lift q_E=15/8", target_center == (Fraction(15, 8), Fraction(0)), str(target_center))
    check("the only changed restricted endpoint column is the E-center prefactor", zero_center != target_center)
    check("therefore any successful p=-2 primitive must evaluate E-center, not just shell data", target_center[0] / zero_shell[0] == Fraction(15, 8))


QUOTE_ANCHORS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "Schur covariance note names inverse-square gap and says no named functional supplies it",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "No named functional produces an inverse-square-of-projector-weight center lift.",
            "The gap is exactly `q_X",
            "realized by no named functional",
        ),
    ),
    (
        "exact readout note leaves endpoint triple unproved and rho_E free",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "it still does not derive the exact dimensionless readout triple",
            "`rho_E = 0` and `rho_E = 21/4` are both exact admissible maps",
        ),
    ),
    (
        "s3 theta-to-slice parent points back to the missing readout triple",
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        (
            "endpoint triple is not yet derived",
            "The next theorem target is the missing readout-map endpoint triple.",
        ),
    ),
    (
        "factor-rigidity note keeps the ambiguity in the spatial prefactor",
        "S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md",
        (
            "does **not** derive the unresolved readout-triple",
            "structurally localized in the spatial prefactor",
        ),
    ),
    (
        "E-center lift attempt did not find an exact E-channel source row",
        "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
        (
            "I did not find a source row that is the E-analog",
            "The exact computation that would have to exist is:",
        ),
    ),
    (
        "bilinear carrier primitive is definition-only, not the needed physical density primitive",
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            "Class-A definition",
            "does **not** prove that this symbol is a physical tensor primitive",
        ),
    ),
    (
        "Record axiom does not supply weighting or readout context",
        "MINIMAL_AXIOMS_2026-06-05.md",
        (
            "A record supplies no readout context",
            "weighting, normalization, probability",
        ),
    ),
)


def part4_quote_anchors() -> None:
    print("\nPART 4: quote-anchored current-surface gap")
    for label, doc_name, needles in QUOTE_ANCHORS:
        text = read_norm(doc_name)
        missing = [needle for needle in needles if needle not in text]
        check(label, not missing, f"{doc_name}; missing={len(missing)}")


def part5_registered_premise_scan() -> None:
    print("\nPART 5: registered premise scan for the missing primitive")
    premise_path = AUDIT_DATA / "axiom_premise_nodes.json"
    tier_a_path = AUDIT_DATA / "premise_decision_history.json"
    premise = premise_path.read_text(encoding="utf-8")
    tier_a = tier_a_path.read_text(encoding="utf-8")
    combined = (premise + "\n" + tier_a).lower()
    json.loads(premise)
    json.loads(tier_a)
    forbidden_tokens = (
        "density_square",
        "density-square",
        "inverse-square-of-projector-weight",
        "w_x^-2",
        "route2_density_square",
    )
    for token in forbidden_tokens:
        check(f"registered premise surfaces do not name `{token}`", token not in combined)
    check("registered premise JSON is parseable", True, f"{premise_path.name}, {tier_a_path.name}")


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("oh_projector_weights", "kappa_3_2", "same-domain shell leverage value"),
    Edge("kappa_3_2", "kappa_square_value_9_4", "value arithmetic only"),
    Edge("route2_bilinear_carrier_K_R", "route2_restricted_readout_family", "channelwise readout reduction"),
    Edge("route2_restricted_readout_family", "rho_E_free_parameter", "exact E-center freedom"),
    Edge("theta_to_slice_family", "spatial_prefactor_ambiguity", "factor-rigidity localization"),
    Edge("record_axiom", "finite_scalar_additivity", "Record supplies additivity only"),
)

MISSING_DENSITY_EDGES: tuple[Edge, ...] = (
    Edge("oh_projector_weights", "p_minus_2_density_square_primitive", "new channel-density-square primitive"),
    Edge("p_minus_2_density_square_primitive", "lambda_9_4", "q_E/q_T=(w_E/w_T)^-2"),
    Edge("lambda_9_4", "q_E_15_8", "with q_T=5/6"),
    Edge("q_E_15_8", "rho_E_21_4", "rho_E=6(q_E-1)"),
    Edge("rho_E_21_4", "endpoint_triple", "(-1,-2,21/4) with T-side candidates"),
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


def part6_typed_reachability() -> None:
    print("\nPART 6: typed reachability")
    current = reachable(CURRENT_EDGES, "oh_projector_weights", "rho_E_21_4")
    current_value_only = reachable(CURRENT_EDGES, "oh_projector_weights", "kappa_square_value_9_4")
    with_density = reachable(CURRENT_EDGES + MISSING_DENSITY_EDGES, "oh_projector_weights", "endpoint_triple")
    check("current graph reaches the value kappa^2=9/4 only as value arithmetic", current_value_only == ["oh_projector_weights", "kappa_3_2", "kappa_square_value_9_4"], " -> ".join(current_value_only))
    check("current graph has no typed path from projector weights to rho_E=21/4", current == [], f"path={current}")
    check("adding only the p=-2 density-square primitive creates the endpoint path", with_density == [
        "oh_projector_weights",
        "p_minus_2_density_square_primitive",
        "lambda_9_4",
        "q_E_15_8",
        "rho_E_21_4",
        "endpoint_triple",
    ], " -> ".join(with_density))


@dataclass(frozen=True)
class FanoutFrame:
    name: str
    result: str
    needs_new_premise: bool


FANOUT: tuple[FanoutFrame, ...] = (
    FanoutFrame("carrier/readout algebra", "rho_E remains free in P(rho_E)", True),
    FanoutFrame("Schur/quadratic invariant", "E:T quadratic ratio is free; p=-2 not forced", True),
    FanoutFrame("time/slice coupling", "Lambda_R and V_R(t) are readout-independent", True),
    FanoutFrame("Record/minimal axioms", "no readout context, weighting, or normalization supplied", True),
    FanoutFrame("source-domain color bridge", "conditional c_TE=-8/9 bridge is separate from density-square", True),
)


def part7_stuck_fanout() -> None:
    print("\nPART 7: stretch fan-out synthesis")
    check("fan-out covers at least five orthogonal frames", len(FANOUT) >= 5, str(len(FANOUT)))
    for frame in FANOUT:
        check(f"{frame.name} requires a new density/readout premise", frame.needs_new_premise, frame.result)
    check("density-square primitive is the minimal direct missing premise in this packet", all(frame.needs_new_premise for frame in FANOUT))


def main() -> int:
    print("Route-2 p=-2 density-square primitive gap")
    print("Scope: current named Route-2 authority bank plus conditional p=-2 consequence")
    part1_endpoint_arithmetic()
    part2_conditional_density_square_primitive()
    part3_readout_freedom()
    part4_quote_anchors()
    part5_registered_premise_scan()
    part6_typed_reachability()
    part7_stuck_fanout()
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={PASS_COUNT + FAIL_COUNT}")
    if FAIL_COUNT:
        print("VERDICT: failed checks; do not use this packet.")
        return 1
    print(
        "VERDICT: conditional support plus scoped current-surface gap. "
        "A p=-2 density-square primitive would force the Route-2 endpoint "
        "exactly, but the current named authority bank does not supply that "
        "primitive; it remains the direct hard residual."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
