#!/usr/bin/env python3
"""Typed-edge cut certificate for the Route-2 source-domain E-center bridge.

This runner does not try to select rho_E. It certifies the graph-theoretic
shape of the remaining source-domain task:

* the current quote-derived typed inventory has no path from R_conn to the
  Route-2 E-center readout nodes;
* scalar-only or physical-selector-looking additions still fail unless a
  typed edge lands in the Route-2 readout domain;
* the successful one-edge discharge, or its two-edge scalarization/typecast
  split, is exactly a source-domain E-center rule.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_source_domain_bridge_no_go import (
    CURRENT_TYPED_EDGES,
    DERIVED_ADDITIONAL_EDGES,
    MISSING_BRIDGE,
    TypedEdge,
    reachable,
)


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
    path = DOCS / name
    check(f"{name} exists", path.exists(), str(path.relative_to(ROOT)))
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def q_e_from_center_ratio(c_te: Fraction) -> Fraction:
    return Fraction(-2, 1) * Fraction(5, 6) / c_te


def rho_e_from_q_e(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def rho_e_from_center_ratio(c_te: Fraction) -> Fraction:
    return rho_e_from_q_e(q_e_from_center_ratio(c_te))


def edge(source: str, target: str, label: str, role: str = "test") -> TypedEdge:
    return TypedEdge(source, target, label, "block22 test edge", role)


def reaches(edges: tuple[TypedEdge, ...], source: str, target: str) -> bool:
    ok, _path = reachable(edges, source, target)
    return ok


def path_labels(edges: tuple[TypedEdge, ...], source: str, target: str) -> str:
    ok, path = reachable(edges, source, target)
    if not ok:
        return "absent"
    return " -> ".join([source, *[item.target for item in path]])


@dataclass(frozen=True)
class WeakAddition:
    name: str
    edge: TypedEdge
    reason: str


def main() -> int:
    print("Route-2 source-domain typed-edge cut certificate")
    print("=" * 78)

    new_note = read_doc("QUARK_ROUTE2_SOURCE_DOMAIN_TYPED_EDGE_CUT_CERTIFICATE_NOTE_2026-06-21.md")
    source_note = read_doc("QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md")
    typed_bridge_note = read_doc("QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md")
    derivation_attempt = read_doc("QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md")
    readout_note = read_doc("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    naturality_note = read_doc("QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md")
    rconn_note = read_doc("RCONN_DERIVED_NOTE.md")
    kappa_note = read_doc("RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md")

    print()
    print("A. Source-surface anchors")
    print("-" * 78)
    check(
        "new note records the required cut sections",
        all(
            needle in new_note
            for needle in (
                "Minimal typed-edge cut",
                "Weak additions that still fail",
                "Two-edge scalarization split",
                "Equivalent discharge edges",
                "does not select the E-center readout entry",
                "source-domain E-center rule",
            )
        ),
    )
    check(
        "source-domain no-go exposes the same missing typed bridge",
        "R_conn = (N_c^2 - 1) / N_c^2\n    ?=> gamma_T(center) / gamma_E(center) = -R_conn"
        in source_note,
    )
    check(
        "typed-bridge bounded note keeps F_adj separate from Route-2 center readout",
        "This step needs an additional source-domain/readout rule" in typed_bridge_note
        and "F_adj` is not typed as a Route-2\ncenter readout" in typed_bridge_note,
    )
    check(
        "E-center derivation attempt names the exact typed target",
        "from a typed E-center source/readout structure" in derivation_attempt
        and "gamma_T(center)/gamma_E(center) = -8/9" in derivation_attempt,
    )
    check(
        "readout note carries endpoint algebra",
        "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6"
        in readout_note,
    )
    check(
        "naturality note states E-channel parameter remains free without extra primitive",
        "remains a free parameter unless an additional E-center endpoint ratio,\nsource-domain, or readout-map primitive is supplied"
        in naturality_note,
    )
    check(
        "Rconn note keeps exact support in the color domain",
        "The exact `8/9` support remains available as `F_adj`, not as a derived connected-trace observable."
        in flat(rconn_note),
    )
    check(
        "kappa note keeps physical selector separate",
        "physical weighting or observable-bridge rule" in " ".join(kappa_note.split()),
    )

    print()
    print("B. Exact conditional arithmetic")
    print("-" * 78)
    f = f_adj(3)
    check("F_adj at N_c=3 is 8/9", f == Fraction(8, 9), str(f))
    check("signed center bridge gives q_E=15/8", q_e_from_center_ratio(-f) == Fraction(15, 8), str(q_e_from_center_ratio(-f)))
    check("signed center bridge gives rho_E=21/4", rho_e_from_center_ratio(-f) == Fraction(21, 4), str(rho_e_from_center_ratio(-f)))
    check("positive F_adj has the wrong Route-2 sign", rho_e_from_center_ratio(f) == Fraction(-69, 4), str(rho_e_from_center_ratio(f)))
    check("q_E=15/8 gives rho_E=21/4", rho_e_from_q_e(Fraction(15, 8)) == Fraction(21, 4))

    print()
    print("C. Minimal typed-edge cut")
    print("-" * 78)
    base_edges = CURRENT_TYPED_EDGES + DERIVED_ADDITIONAL_EDGES
    source = "su3_R_conn_8_9"
    center = "route2_center_TE_minus_8_9"
    q_e = "route2_q_E_15_8"
    rho = "route2_rho_E_21_4"
    check("current quote-derived bank has no Rconn-to-center path", not reaches(base_edges, source, center), path_labels(base_edges, source, center))
    check("current quote-derived bank has no Rconn-to-q_E path", not reaches(base_edges, source, q_e), path_labels(base_edges, source, q_e))
    check("current quote-derived bank has no Rconn-to-rho_E path", not reaches(base_edges, source, rho), path_labels(base_edges, source, rho))
    check("MISSING_BRIDGE has the expected source node", MISSING_BRIDGE.source == source, MISSING_BRIDGE.source)
    check("MISSING_BRIDGE lands in the Route-2 center-ratio node", MISSING_BRIDGE.target == center, MISSING_BRIDGE.target)
    check(
        "adding the missing bridge reaches rho_E",
        reaches(base_edges + (MISSING_BRIDGE,), source, rho),
        path_labels(base_edges + (MISSING_BRIDGE,), source, rho),
    )
    check("current bank does not already contain the missing bridge", MISSING_BRIDGE not in base_edges)

    equivalent_discharge_edges = (
        edge(source, center, "direct typed center-ratio bridge", "typed_bridge"),
        edge(source, q_e, "direct typed E-center lift bridge", "typed_bridge"),
        edge(source, rho, "direct typed readout-entry bridge", "typed_bridge"),
    )
    for item in equivalent_discharge_edges:
        check(
            f"one-edge discharge via {item.target} reaches rho_E",
            reaches(base_edges + (item,), source, rho),
            path_labels(base_edges + (item,), source, rho),
        )
    check(
        "all one-edge discharges land in Route-2 readout nodes",
        {item.target for item in equivalent_discharge_edges} == {center, q_e, rho},
    )

    print()
    print("D. Weak additions that still fail")
    print("-" * 78)
    weak_additions = (
        WeakAddition(
            "positive scalar only",
            edge(source, "scalar_positive_8_9", "R_conn supplies +8/9 as an untyped scalar", "scalar"),
            "no Route-2 readout landing node",
        ),
        WeakAddition(
            "signed scalar only",
            edge(source, "scalar_signed_minus_8_9", "R_conn supplies -8/9 as an untyped scalar", "scalar"),
            "sign without typecast is still not c_TE",
        ),
        WeakAddition(
            "physical selector only",
            edge(source, "physical_connected_trace_selector", "R_conn supplies a physical connected trace selector", "physical"),
            "physical selector is not a Route-2 center ratio",
        ),
        WeakAddition(
            "T-side sign only",
            edge("route2_q_T_5_6_and_shell_TE_minus_2", "route2_negative_orientation", "T-side orientation sign", "orientation"),
            "orientation does not supply E-center magnitude",
        ),
        WeakAddition(
            "center slot only",
            edge("route2_endpoint_algebra", "route2_center_ratio_slot_open", "Route-2 has an open center-ratio slot", "slot"),
            "slot existence is not a value",
        ),
        WeakAddition(
            "wrong signed typed bridge",
            edge(source, "route2_center_TE_plus_8_9", "wrong Route-2 center ratio sign", "wrong_bridge"),
            "wrong sign computes a different E-center entry",
        ),
    )
    for weak in weak_additions:
        check(
            f"{weak.name} still has no Rconn-to-rho_E path",
            not reaches(base_edges + (weak.edge,), source, rho),
            weak.reason,
        )
    check("all weak additions fail alone", all(not reaches(base_edges + (weak.edge,), source, rho) for weak in weak_additions))

    print()
    print("E. Two-edge scalarization split")
    print("-" * 78)
    signed_scalar = edge(source, "scalar_signed_minus_8_9", "R_conn supplies -8/9 as a scalar", "scalar")
    typecast = edge("scalar_signed_minus_8_9", center, "typed source-domain identification of scalar with c_TE", "typecast")
    positive_scalar = edge(source, "scalar_positive_8_9", "R_conn supplies +8/9 as a scalar", "scalar")
    positive_typecast = edge("scalar_positive_8_9", "route2_center_TE_plus_8_9", "wrong signed typecast", "typecast")
    check("signed scalar without typecast fails", not reaches(base_edges + (signed_scalar,), source, rho))
    check("typecast without signed scalar fails", not reaches(base_edges + (typecast,), source, rho))
    check(
        "signed scalar plus typecast reaches rho_E",
        reaches(base_edges + (signed_scalar, typecast), source, rho),
        path_labels(base_edges + (signed_scalar, typecast), source, rho),
    )
    check("positive scalar plus wrong typecast fails target rho_E", not reaches(base_edges + (positive_scalar, positive_typecast), source, rho))
    check("two-edge split is equivalent to making a typed readout bridge explicit", typecast.target == MISSING_BRIDGE.target)

    print()
    print("F. Note inventories")
    print("-" * 78)
    for label in (
        "positive scalar only",
        "signed scalar only",
        "physical selector only",
        "T-side sign only",
        "center slot only",
        "wrong signed typed bridge",
    ):
        check(f"new note lists weak addition: {label}", label in new_note)
    for label in (
        "direct typed center-ratio bridge",
        "direct typed E-center lift bridge",
        "direct typed readout-entry bridge",
    ):
        check(f"new note lists discharge edge: {label}", label in new_note)

    print()
    print("Summary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: current source-domain work is blocked exactly at the typed Route-2 readout landing edge.")
        return 0
    print("VERDICT: typed-edge cut certificate failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
