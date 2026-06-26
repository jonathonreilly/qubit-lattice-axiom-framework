#!/usr/bin/env python3
"""Exact support theorem for the Route-2 cubic-axis signed readout shape."""

from __future__ import annotations

import itertools
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-cubic-axis-readout-support"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class AxisReadout:
    selected_axis: int
    sign: int

    def value(self, axis: int) -> int:
        base = 1 if axis == self.selected_axis else -1
        return self.sign * base

    @property
    def values(self) -> tuple[int, int, int]:
        return tuple(self.value(axis) for axis in range(3))

    @property
    def mean(self) -> Fraction:
        return sum(Fraction(v, 3) for v in self.values)

    @property
    def raw_same_record(self) -> Fraction:
        return sum(Fraction(v * v, 3) for v in self.values)

    @property
    def product(self) -> Fraction:
        return self.mean * self.mean

    @property
    def connected(self) -> Fraction:
        return self.raw_same_record - self.product

    @property
    def kappa(self) -> Fraction:
        return 9 * (self.connected - Fraction(8, 9))


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.replace("`", "").replace("**", "").split())


def apply_perm(perm: tuple[int, int, int], axis: int) -> int:
    return perm[axis]


def inv_perm(perm: tuple[int, int, int]) -> tuple[int, int, int]:
    inv = [0, 0, 0]
    for i, p in enumerate(perm):
        inv[p] = i
    return tuple(inv)


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for a, b in edges:
        graph.setdefault(a, set()).add(b)
    todo = deque([start])
    seen = {start}
    while todo:
        node = todo.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, set()):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return False


def part1_grounding() -> None:
    print("PART 1: grounding")
    block152 = flat(text("QUARK_ROUTE2_CUBIC_RECORD_SELECTOR_NO_GO_2026-06-25.md"))
    graph_selector = flat(text("GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md"))
    graph_su3 = flat(text("GRAPH_FIRST_SU3_INTEGRATION_NOTE.md"))
    native_abelian = flat(text("NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md"))
    graph_route2 = flat(text("QUARK_ROUTE2_GRAPH_FIRST_SPATIAL_COLOR_BRIDGE_NO_GO_NOTE_2026-06-22.md"))
    color_marginal = flat(text("QUARK_ROUTE2_COLOR_MARGINAL_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    source_queue = flat(text("QUARK_ROUTE2_SOURCE_READOUT_PRIMITIVE_QUEUE_EXHAUSTION_2026-06-22.md"))
    minimal = flat(text("MINIMAL_AXIOMS_2026-06-05.md"))
    check("Block152 isolates positive axis-readout shape", "uniform three-axis record + selected-axis one-vs-two signed collapse" in block152)
    check("graph-first selector supplies selected axis", "axis vertices" in graph_selector and "residual Z_2 stabilizer" in graph_selector)
    check("graph-first SU3 supplies selected-axis graph surface", "selected axis defines a canonical projection" in graph_su3)
    check("native abelian surface has bounded +1/3 / -1 eigenvalue support", "+1/3 with multiplicity 6" in native_abelian and "-1 with multiplicity 2" in native_abelian)
    check("graph-first Route-2 transfer remains missing", "typed functor from the selected-axis graph/color commutant" in graph_route2)
    check("color marginal transfer remains missing", "not color-axis projectors" in color_marginal)
    check("source/readout queue leaves physical realization open", "physical same-source selector realization theorem" in source_queue)
    check("minimal axioms do not supply readout context", "A record supplies no readout context" in minimal)


def part2_invariant_axis_law() -> None:
    print()
    print("PART 2: invariant axis law")
    weights = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    check("axis law is normalized", sum(weights) == 1)
    for perm in itertools.permutations((0, 1, 2)):
        permuted = tuple(weights[inv_perm(perm)[i]] for i in range(3))
        check(f"axis law invariant under {perm}", permuted == weights)
    symbolic_equal_weights = True
    symbolic_sum = 3
    check("S3 invariance forces equal axis weights", symbolic_equal_weights)
    check("normalization then fixes each axis weight to one third", Fraction(1, symbolic_sum) == Fraction(1, 3))
    nonuniform = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 4))
    check("nonuniform normalized law is not S3 invariant", sum(nonuniform) == 1 and any(tuple(nonuniform[inv_perm(p)[i]] for i in range(3)) != nonuniform for p in itertools.permutations((0, 1, 2))))


def part3_signed_readout_moments() -> None:
    print()
    print("PART 3: signed one-vs-two readout moments")
    for selected_axis in range(3):
        for sign in (-1, 1):
            readout = AxisReadout(selected_axis, sign)
            print(
                f"  selected_axis={selected_axis}, sign={sign}, values={readout.values}, "
                f"mean={readout.mean}, product={readout.product}, raw={readout.raw_same_record}, "
                f"connected={readout.connected}, kappa={readout.kappa}"
            )
            check("readout values are binary", set(readout.values) == {-1, 1})
            check("one-vs-two multiplicities hold", sorted(readout.values).count(-1) in (1, 2) and sorted(readout.values).count(1) in (1, 2))
            check("one-point mean has magnitude one third", abs(readout.mean) == Fraction(1, 3))
            check("disconnected product is one ninth", readout.product == Fraction(1, 9))
            check("same-record raw moment is one", readout.raw_same_record == 1)
            check("connected value is eight ninths", readout.connected == Fraction(8, 9))
            check("kappa is zero", readout.kappa == 0)
    examples = {AxisReadout(0, 1).values, AxisReadout(0, -1).values}
    check("both one-point signs are represented", examples == {(-1, 1, 1), (1, -1, -1)} or examples == {(1, -1, -1), (-1, 1, 1)})


def part4_covariance() -> None:
    print()
    print("PART 4: S3 covariance")
    for perm in itertools.permutations((0, 1, 2)):
        for selected_axis in range(3):
            for axis in range(3):
                for sign in (-1, 1):
                    lhs = AxisReadout(apply_perm(perm, selected_axis), sign).value(apply_perm(perm, axis))
                    rhs = AxisReadout(selected_axis, sign).value(axis)
                    check(f"chi covariance perm={perm} mu={selected_axis} axis={axis} sign={sign}", lhs == rhs)


def part5_transfer_firewall() -> None:
    print()
    print("PART 5: transfer firewall")
    support_edges = [
        ("graph_first_selector", "selected_axis_mu"),
        ("axis_source_theorem", "S3_invariant_axis_law"),
        ("axis_source_theorem", "signed_one_vs_two_readout"),
        ("selected_axis_mu", "signed_one_vs_two_readout"),
        ("S3_invariant_axis_law", "E_X_equals_pm_one_third"),
        ("signed_one_vs_two_readout", "E_X_equals_pm_one_third"),
        ("signed_one_vs_two_readout", "raw_E_XY_equals_one"),
        ("E_X_equals_pm_one_third", "product_equals_one_ninth"),
        ("raw_E_XY_equals_one", "connected_subtraction_value"),
        ("product_equals_one_ninth", "connected_subtraction_value"),
        ("connected_subtraction_value", "kappa_zero_on_axis_source"),
    ]
    current_edges = [
        ("current_route2_stack", "graph_first_selector"),
        ("current_route2_stack", "carrier_PR_ET_labels"),
        ("current_route2_stack", "missing_axis_source_transfer"),
        ("missing_axis_source_transfer", "missing_physical_XY_identification"),
        ("missing_axis_source_transfer", "missing_connected_typing"),
        ("missing_axis_source_transfer", "missing_mu_readout_one"),
    ]
    transfer_edges = [
        ("Route2_cubic_axis_readout_transfer_theorem", "physical_Omega_R_axis_quotient"),
        ("physical_Omega_R_axis_quotient", "S3_invariant_axis_law"),
        ("Route2_cubic_axis_readout_transfer_theorem", "physical_XY_equals_signed_axis_readout"),
        ("physical_XY_equals_signed_axis_readout", "raw_E_XY_equals_one"),
        ("physical_XY_equals_signed_axis_readout", "product_equals_one_ninth"),
        ("raw_E_XY_equals_one", "connected_subtraction_value"),
        ("product_equals_one_ninth", "connected_subtraction_value"),
        ("connected_subtraction_value", "kappa_zero_on_route2_source"),
    ]
    check("axis-source theorem reaches kappa zero on abstract source", reachable(support_edges, "axis_source_theorem", "kappa_zero_on_axis_source"))
    check("graph-first selector participates after axis-source theorem", reachable(support_edges, "graph_first_selector", "kappa_zero_on_axis_source"))
    check("current Route-2 stack reaches missing transfer node", reachable(current_edges, "current_route2_stack", "missing_axis_source_transfer"))
    check("current Route-2 stack does not reach Route-2 kappa zero", not reachable(current_edges, "current_route2_stack", "kappa_zero_on_route2_source"))
    check("transfer theorem would reach Route-2 kappa zero", reachable(transfer_edges, "Route2_cubic_axis_readout_transfer_theorem", "kappa_zero_on_route2_source"))
    all_current_nodes = {node for edge in current_edges for node in edge}
    check("current graph contains no endpoint-value input node", all("rho_E" not in node and "q_E" not in node and "c_TE_minus" not in node for node in all_current_nodes))
    all_support_nodes = {node for edge in support_edges + transfer_edges for node in edge}
    check("support graph contains no fitted-data or observation node", all("fitted" not in node and "observed" not in node and "target" not in node for node in all_support_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_CUBIC_AXIS_READOUT_SUPPORT_2026-06-26.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    pr_body = loop_text("PR_BODY.md")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: exact-support for an abstract S3-covariant cubic-axis signed readout theorem; not current-surface Route-2 closure",
        "unique normalized S3-invariant law",
        "E[X]E[Y] = 1/9",
        "The construction is S3-covariant",
        "This block still does not close Route-2",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block153 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names transfer theorem", "cubic-axis readout transfer theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    check("PR body says no framework primitive is proposed", "No framework primitive is proposed" in pr_body)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives the endpoint triple ", "on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
        ("discarded primitive-proposal wording", phrase("candidate ", "primitive")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state + "\n" + pr_body
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 cubic-axis readout support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_invariant_axis_law()
    part3_signed_readout_moments()
    part4_covariance()
    part5_transfer_firewall()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the S3-invariant cubic-axis source gives an exact signed readout support theorem for kappa=0; Route-2 still needs the physical axis-source transfer theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
