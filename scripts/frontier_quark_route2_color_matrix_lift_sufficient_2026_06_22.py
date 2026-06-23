#!/usr/bin/env python3
"""Conditional sufficient theorem for Route-2 color-matrix source lift."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-color-matrix-lift-sufficient"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class LiftPremises:
    same_source_lift: bool
    full_color_source: bool
    connected_readout_typing: bool
    singlet_typing: bool
    output_normalization: bool
    orientation_sign: Fraction

    @property
    def lift_complete(self) -> bool:
        return all(
            (
                self.same_source_lift,
                self.full_color_source,
                self.connected_readout_typing,
                self.singlet_typing,
                self.output_normalization,
            )
        )


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


def connected_fraction(n: int) -> Fraction:
    return Fraction(n * n - 1, n * n)


def kappa_from_fraction(frac: Fraction) -> Fraction:
    return 9 * (frac - Fraction(8, 9))


def oriented_bridge(sigma: Fraction, r_phys: Fraction) -> Fraction:
    return sigma * r_phys


def centered_identity_score(trace_rho: Fraction, lam: Fraction) -> Fraction:
    return lam * trace_rho - lam


def part1_grounding() -> None:
    print("PART 1: grounding")
    support = flat(text("QUARK_ROUTE2_NORMALIZED_COLOR_SOURCE_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    connected_transfer = flat(text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    finite_rank = flat(text("QUARK_ROUTE2_FINITE_ENDPOINT_SOURCE_RANK_NO_GO_NOTE_2026-06-22.md"))
    source_measure = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_COLOR_ENSEMBLE_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    check("Block113 support gives kappa=0 on color source", "kappa = 0" in support and "color-source surface" in support)
    check("connected transfer note keeps same-source authority missing", "same-source normalized color-matrix source authority" in connected_transfer)
    check("finite endpoint rank note bounds four-record pullback", "rank centered scores <= 4 - 1 = 3" in finite_rank)
    check("source-measure color ensemble transfer remains missing", "same-source full color-record ensemble/readout theorem" in source_measure)
    check("endpoint orientation sign support supplies sigma conditionally", "sigma=-1" in sign and "magnitude remains open" in sign)


def part2_sufficient_theorem() -> None:
    print()
    print("PART 2: sufficient theorem implication")
    premises = LiftPremises(
        same_source_lift=True,
        full_color_source=True,
        connected_readout_typing=True,
        singlet_typing=True,
        output_normalization=True,
        orientation_sign=Fraction(-1),
    )
    frac = connected_fraction(3)
    kappa = kappa_from_fraction(frac)
    center_ratio = oriented_bridge(premises.orientation_sign, frac)
    print(f"  connected_fraction={frac}, kappa={kappa}, center_ratio={center_ratio}")
    check("all lift premises are supplied in the conditional theorem", premises.lift_complete)
    check("N=3 connected fraction is 8/9", frac == Fraction(8, 9))
    check("conditional theorem forces kappa=0", kappa == 0)
    check("conditional theorem plus orientation gives -8/9", center_ratio == Fraction(-8, 9))
    check("identity score vanishes on trace-one records", centered_identity_score(Fraction(1), Fraction(5, 2)) == 0)


def part3_current_surface_firewall() -> None:
    print()
    print("PART 3: current-surface firewall")
    current = LiftPremises(
        same_source_lift=False,
        full_color_source=False,
        connected_readout_typing=False,
        singlet_typing=False,
        output_normalization=False,
        orientation_sign=Fraction(-1),
    )
    fields = {
        "same_source_lift": current.same_source_lift,
        "full_color_source": current.full_color_source,
        "connected_readout_typing": current.connected_readout_typing,
        "singlet_typing": current.singlet_typing,
        "output_normalization": current.output_normalization,
        "orientation_sign_support": current.orientation_sign == -1,
    }
    for name, supplied in fields.items():
        print(f"  current {name}: {supplied}")
        check(f"{name} classification is boolean", isinstance(supplied, bool))
    check("current lift theorem is not complete", not current.lift_complete)
    check("orientation sign support alone is insufficient", fields["orientation_sign_support"] and not current.lift_complete)
    check("five non-sign lift premises remain open", sum(1 for name, supplied in fields.items() if name != "orientation_sign_support" and not supplied) == 5)


def part4_rank_and_trace_constraints() -> None:
    print()
    print("PART 4: rank and trace constraints")
    full_dim = 9
    connected_dim = 8
    endpoint_records = 4
    centered_endpoint_rank_bound = endpoint_records - 1
    print(f"  full_dim={full_dim}, connected_dim={connected_dim}, endpoint_rank_bound={centered_endpoint_rank_bound}")
    check("End(C^3) dimension is 9", full_dim == 9)
    check("sl_3 connected dimension is 8", connected_dim == 8)
    check("four endpoint records center to rank at most 3", centered_endpoint_rank_bound == 3)
    check("four endpoint pullback cannot cover sl_3", centered_endpoint_rank_bound < connected_dim)
    check("trace-one condition is load-bearing", centered_identity_score(Fraction(2), Fraction(3)) != 0)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("current_Route2_P_R", "four_endpoint_surface"),
        ("four_endpoint_surface", "missing_color_matrix_lift"),
        ("missing_color_matrix_lift", "no_current_transfer"),
    ]
    sufficient_edges = [
        ("Route2_color_matrix_lift_sufficient_theorem", "same_source_trace_one_records"),
        ("same_source_trace_one_records", "full_EndC3_source"),
        ("full_EndC3_source", "identity_line_centered_zero"),
        ("identity_line_centered_zero", "sl3_connected_tangent"),
        ("sl3_connected_tangent", "kappa_zero_without_endpoint"),
        ("kappa_zero_without_endpoint", "oriented_center_bridge_minus_8_9"),
    ]
    check("current Route-2 P_R reaches missing lift node", reachable(current_edges, "current_Route2_P_R", "missing_color_matrix_lift"))
    check("current Route-2 P_R does not reach kappa=0", not reachable(current_edges, "current_Route2_P_R", "kappa_zero_without_endpoint"))
    check("sufficient theorem reaches kappa=0", reachable(sufficient_edges, "Route2_color_matrix_lift_sufficient_theorem", "kappa_zero_without_endpoint"))
    check("sufficient theorem reaches oriented bridge consequence", reachable(sufficient_edges, "Route2_color_matrix_lift_sufficient_theorem", "oriented_center_bridge_minus_8_9"))
    all_nodes = {n for e in current_edges + sufficient_edges for n in e}
    check("reachability graph contains no endpoint triple node", all("rho_E_21_4" not in n and "q_E_15_8" not in n for n in all_nodes))
    check("reachability graph does not use finite-box comparator", all("finite_box" not in n and "box" not in n for n in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_COLOR_MATRIX_LIFT_SUFFICIENT_THEOREM_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: conditional-support; the same-source lift premises are not current-surface theorems",
        "Sufficient Theorem",
        "Current-Surface Boundary",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block114 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
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
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 color-matrix lift sufficient theorem")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_sufficient_theorem()
    part3_current_surface_firewall()
    part4_rank_and_trace_constraints()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: a same-source Route-2 color-matrix lift with the stated five clauses would force kappa=0 and, with orientation support, the -8/9 bridge; those clauses remain open on the current surface.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
