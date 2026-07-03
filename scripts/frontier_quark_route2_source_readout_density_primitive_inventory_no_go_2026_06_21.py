#!/usr/bin/env python3
"""Route-2 source/readout density-primitive inventory no-go.

This runner asks a narrow question left by the Route-2 endpoint work:

    Does the current named source/readout authority bank supply a typed
    primitive equivalent to q_X ~ w_X^{-2}?

It does not audit or apply verdicts.  It verifies exact conditional arithmetic
if the primitive is supplied, then quote-checks that current main names the
same object as an open gap rather than as a derived primitive.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
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


def read_doc(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def frac_text(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def q_e_from_lambda(lam: Fraction, q_t: Fraction = Fraction(5, 6)) -> Fraction:
    return lam * q_t


def rho_from_q(q: Fraction) -> Fraction:
    return 6 * (q - 1)


def center_te(q_e: Fraction, q_t: Fraction = Fraction(5, 6), shell_te: Fraction = Fraction(-2)) -> Fraction:
    return shell_te * q_t / q_e


def exact_density_primitive_checks() -> None:
    print("\nPART 1: exact inverse-square density primitive consequences")
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    inv_density_factor = (1 / w_e) / (1 / w_t)
    lambda_needed = inv_density_factor**2
    q_t = Fraction(5, 6)
    q_e = q_e_from_lambda(lambda_needed, q_t)
    rho_e = rho_from_q(q_e)
    c_te = center_te(q_e, q_t)

    check("O_h projector weights are w_E=1/3 and w_T=1/2", (w_e, w_t) == (Fraction(1, 3), Fraction(1, 2)))
    check("one inverse-density factor is 3/2", inv_density_factor == Fraction(3, 2), frac_text(inv_density_factor))
    check("two inverse-density factors give lambda=9/4", lambda_needed == Fraction(9, 4), frac_text(lambda_needed))
    check("lambda=9/4 with q_T=5/6 gives q_E=15/8", q_e == Fraction(15, 8), frac_text(q_e))
    check("q_E=15/8 gives rho_E=21/4", rho_e == Fraction(21, 4), frac_text(rho_e))
    check("with shell T/E=-2 the center ratio is c_TE=-8/9", c_te == Fraction(-8, 9), frac_text(c_te))

    print("\nPART 2: exponent scan over channel weight powers")
    ratio = w_e / w_t
    rows: list[tuple[int, Fraction, Fraction, Fraction, Fraction]] = []
    for power in [-2, -1, 0, 1, 2]:
        if power < 0:
            lam = Fraction(1, ratio ** abs(power))
        else:
            lam = ratio**power
        q_e_p = q_e_from_lambda(lam)
        rho_p = rho_from_q(q_e_p)
        c_p = center_te(q_e_p)
        rows.append((power, lam, q_e_p, rho_p, c_p))
        print(
            "  p={:>2}: lambda={}, q_E={}, rho_E={}, c_TE={}".format(
                power, frac_text(lam), frac_text(q_e_p), frac_text(rho_p), frac_text(c_p)
            )
        )

    target_rows = [row for row in rows if row[1:] == (Fraction(9, 4), Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9))]
    check("among tested natural powers only p=-2 gives the endpoint target", target_rows == [rows[0]])
    one_power = next(row for row in rows if row[0] == -1)
    check(
        "one inverse-density power gives the wrong E lift",
        one_power[2:] == (Fraction(5, 4), Fraction(3, 2), Fraction(-4, 3)),
        f"q_E={frac_text(one_power[2])}, rho_E={frac_text(one_power[3])}, c_TE={frac_text(one_power[4])}",
    )


QUOTE_ANCHORS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "quadratic Schur note names inverse-square as the gap, not a derived primitive",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "No named functional produces an\n  inverse-square-of-projector-weight center lift.",
            "The gap is exactly `q_X",
            "realized by no named functional",
        ),
    ),
    (
        "E-center blindness note names the necessary new ingredient",
        "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md",
        (
            "A positive repair\nmust supply a genuine E-center lift, source-domain rule, or equivalent\nreadout primitive.",
            "Viable positive routes now have to include at least one of:",
        ),
    ),
    (
        "E-center lift attempt says the current source bank lacks the E row",
        "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
        (
            "requested source bank does not contain an exact E-channel row that computes",
            "`beta_E/alpha_E`. The named missing link is:",
            "current requested source",
            "bank does not supply that exact computation.",
        ),
    ),
    (
        "readout primitive bridge assessment leaves map selection open",
        "S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md",
        (
            "The one-hop authorities do not supply a theorem selecting `P_eta` as the\n  physical gate primitive.",
            "the named selection freedom is `rho_E`.",
        ),
    ),
    (
        "Rconn typed bridge note does not type F_adj as Route-2 readout",
        "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md",
        (
            "the Route-2 E-center lift is still a free map entry.",
            "`F_adj` is not typed as a Route-2",
            "center readout.",
        ),
    ),
    (
        "T-side attempt keeps the first two entries as row-selector data",
        "QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md",
        (
            "both the sign and\nmagnitude of `s_TE` are row-normalization data unless a further readout-row\nselector is supplied.",
            "the current cited carrier/time surface leaves\nthat row as the named open target.",
        ),
    ),
    (
        "theta-to-slice note localizes this block upstream of time transport",
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        (
            "The next theorem target is the missing readout-map endpoint triple.",
            "That\ntarget lives on the upstream readout-map row, not on this row.",
        ),
    ),
    (
        "bilinear primitive note does not identify K_R as physical primitive",
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            "A bridge theorem identifying the bilinear carrier `K_R(q)` with any",
            "physical tensor primitive in the GR-readout chain",
            "These are **real derivation gaps**, not dependency-citation issues.",
        ),
    ),
)


FORBIDDEN_DIRECT_CLOSURES: tuple[str, ...] = (
    "q_x ~ w_x^{-2} is derived",
    "q_x proportional to w_x^{-2} is derived",
    "d_x = a_x / w_x is derived",
    "d_x=a_x/w_x is derived",
    "source/readout channel-weight primitive is supplied",
    "source/readout density primitive is supplied",
    "inverse-square density primitive is supplied",
    "current source bank derives rho_e = 21/4",
    "current source bank derives beta_e/alpha_e = 21/4",
)


def quote_inventory_checks() -> None:
    print("\nPART 3: quote-anchored current-bank inventory")
    for label, doc_name, anchors in QUOTE_ANCHORS:
        text = read_doc(doc_name)
        missing = [anchor for anchor in anchors if anchor not in text]
        check(label, not missing, f"{doc_name}; missing={len(missing)}")

    print("\nPART 4: direct-closure phrase firewall")
    bank_text = "\n".join(read_doc(doc_name) for _, doc_name, _ in QUOTE_ANCHORS).lower()
    hits = [phrase for phrase in FORBIDDEN_DIRECT_CLOSURES if phrase in bank_text]
    check("no scanned authority states the inverse-square density primitive as supplied", not hits, f"hits={hits}")


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("oh_projector_weights", "kappa_3_2", "w_T/w_E = 3/2"),
    Edge("kappa_3_2", "kappa_square_value_9_4", "same-domain value kappa^2"),
    Edge("route2_restricted_readout_family", "route2_endpoint_algebra", "endpoint ratio formulas"),
    Edge("route2_t_side_candidates", "q_T_5_6_shell_TE_minus_2", "conditional T-side values"),
    Edge("route2_center_TE_minus_8_9", "q_E_15_8", "endpoint algebra"),
    Edge("q_E_15_8", "rho_E_21_4", "rho_E = 6(q_E-1)"),
    Edge("rconn_fadj_8_9", "positive_color_fraction_8_9", "color count, not typed Route-2 readout"),
)

MISSING_DENSITY_EDGES: tuple[Edge, ...] = (
    Edge("oh_projector_weights", "source_readout_inverse_square_density_primitive", "missing D_X ~ 1/w_X primitive"),
    Edge("source_readout_inverse_square_density_primitive", "lambda_9_4", "missing q_E/q_T = (w_E/w_T)^-2 bridge"),
    Edge("lambda_9_4", "q_E_15_8", "with q_T=5/6"),
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


def typed_graph_checks() -> None:
    print("\nPART 5: typed reachability")
    current_path = reachable(CURRENT_EDGES, "oh_projector_weights", "rho_E_21_4")
    with_missing = reachable(CURRENT_EDGES + MISSING_DENSITY_EDGES, "oh_projector_weights", "rho_E_21_4")
    count_path = reachable(CURRENT_EDGES, "rconn_fadj_8_9", "rho_E_21_4")

    check("current typed graph has no path from O_h weights to rho_E=21/4", current_path == [], f"path={current_path}")
    check("current typed graph has no path from F_adj count to rho_E=21/4", count_path == [], f"path={count_path}")
    check(
        "adjoining the explicit inverse-square density primitive creates the path",
        with_missing
        == [
            "oh_projector_weights",
            "source_readout_inverse_square_density_primitive",
            "lambda_9_4",
            "q_E_15_8",
            "rho_E_21_4",
        ],
        " -> ".join(with_missing),
    )
    check(
        "the only new path uses the explicitly missing density primitive",
        "source_readout_inverse_square_density_primitive" in with_missing,
    )


def main() -> int:
    print("Route-2 source/readout density-primitive inventory no-go")
    print("Scope: named current source/readout authority bank; future nonlinear primitives remain open")
    exact_density_primitive_checks()
    quote_inventory_checks()
    typed_graph_checks()
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={PASS_COUNT + FAIL_COUNT}")
    if FAIL_COUNT:
        print("VERDICT: failed checks; do not use this packet.")
        return 1
    print(
        "VERDICT: scoped no-go. The exact inverse-square density primitive would force "
        "rho_E=21/4, but the scanned current authority bank names it as a missing "
        "source/readout primitive rather than supplying it."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
