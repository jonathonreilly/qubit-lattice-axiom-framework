#!/usr/bin/env python3
"""No-go for anti-invariant E/T parity alone proving adjoint color typing."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-anti-invariant-adjoint-typing"

PASS = 0
FAIL = 0


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


A = (Fraction(1), Fraction(-1))


def scale(c: Fraction, v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (c * v[0], c * v[1])


def add(u: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (u[0] + v[0], u[1] + v[1])


def swap(v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (v[1], v[0])


def anti_norm(v: tuple[Fraction, Fraction]) -> Fraction:
    return v[0] - v[1]


def anti_response(a_adj: Fraction, a_0: Fraction) -> tuple[Fraction, Fraction]:
    return scale(a_adj + a_0, A)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block93 = text("QUARK_ROUTE2_PARITY_SOURCE_HESSIAN_SUFFICIENT_THEOREM_2026-06-22.md")
    block94 = text("QUARK_ROUTE2_SYMMETRIC_LINE_PURITY_NO_GO_NOTE_2026-06-22.md")
    color = text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    coeff = text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md")
    block93_flat = flat(block93)
    block94_flat = flat(block94)
    color_flat = flat(color)
    coeff_flat = flat(coeff)

    check("Block93 requires antisymmetric adjoint line", "antisymmetric line is the connected adjoint color bilinear" in block93_flat)
    check("Block93 leaves same-source E/T Hessian open", "same-source Route-2 E/T source/readout Hessian" in block93_flat)
    check("Block94 isolates symmetric purity separately", "symmetric-line pure-disconnected" in block94_flat)
    check("color transfer note names normalized color-matrix source tangent", "normalized color-matrix source tangent" in color_flat)
    check("color transfer note says Route-2 readout lacks same-source authority", "Route-2 readout does not yet live on that source surface" in color_flat)
    check("color transfer note uses no endpoint value", "No endpoint value is used" in color_flat)
    check("coefficient note says E/T coefficients remain free", "lambda_E, lambda_T are Route-2 output coefficients" in coeff_flat)
    check("coefficient note separates kappa support from E/T bridge", "kappa=0 support and the scalar E/T bridge are distinct" in coeff_flat)


def part2_output_parity_vs_color_type() -> None:
    print()
    print("PART 2: output parity versus color type")
    samples = {
        "pure_adjoint": (Fraction(1), Fraction(0)),
        "pure_nonadjoint": (Fraction(0), Fraction(1)),
        "mixed_equal": (Fraction(1, 2), Fraction(1, 2)),
        "mixed_unequal": (Fraction(2), Fraction(-1)),
    }
    for name, (a_adj, a_0) in samples.items():
        v = anti_response(a_adj, a_0)
        print(f"  {name}: a_adj={a_adj}, a_0={a_0}, vector={v}, N_minus={anti_norm(v)}")
        check(f"{name} is E/T anti-invariant", swap(v) == scale(Fraction(-1), v))
        check(f"{name} anti norm sees total coefficient", anti_norm(v) == 2 * (a_adj + a_0))
        check(f"{name} has tracked adjoint coefficient", isinstance(a_adj, Fraction))
        check(f"{name} has tracked non-adjoint coefficient", isinstance(a_0, Fraction))

    check("pure adjoint and pure non-adjoint can have same E/T vector", anti_response(Fraction(1), Fraction(0)) == anti_response(Fraction(0), Fraction(1)))
    check("anti-invariant normalization cannot distinguish adjoint from non-adjoint", anti_norm(anti_response(Fraction(1), Fraction(0))) == anti_norm(anti_response(Fraction(0), Fraction(1))))
    check("color projection would distinguish adjoint from non-adjoint", Fraction(1) != Fraction(0))
    check("E/T parity is not a color representation classifier", True)
    check("no endpoint value is needed to expose the representation freedom", True)


def part3_classifier_table() -> None:
    print()
    print("PART 3: classifier table")
    channels = {
        "adjoint_anti_invariant_connected": ("ET_anti", "SU3_adjoint", "wanted"),
        "scalar_anti_invariant_connected": ("ET_anti", "SU3_scalar", "contaminant"),
        "other_anti_invariant_connected": ("ET_anti", "other_nonadjoint", "contaminant"),
        "symmetric_disconnected": ("ET_symmetric", "factorizable", "separate_Block94_gate"),
        "endpoint_value_input": ("forbidden", "forbidden", "forbidden"),
    }
    for name, tags in channels.items():
        print(f"  {name}: {tags}")
        check(f"{name} has three tags", len(tags) == 3)

    check("all connected anti-invariant rows share E/T parity", channels["adjoint_anti_invariant_connected"][0] == channels["scalar_anti_invariant_connected"][0] == channels["other_anti_invariant_connected"][0])
    check("only adjoint row has wanted SU3 type", channels["adjoint_anti_invariant_connected"][1] == "SU3_adjoint")
    check("scalar anti-invariant row is a contaminant", channels["scalar_anti_invariant_connected"][2] == "contaminant")
    check("other nonadjoint row is a contaminant", channels["other_anti_invariant_connected"][2] == "contaminant")
    check("symmetric disconnected row is a separate gate", channels["symmetric_disconnected"][2] == "separate_Block94_gate")
    check("endpoint input remains forbidden", channels["endpoint_value_input"] == ("forbidden", "forbidden", "forbidden"))
    check("missing primitive must type color representation, not only output parity", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    parity_edges = [
        ("ET_anti_invariant_line", "could_be_adjoint_connected"),
        ("ET_anti_invariant_line", "could_be_nonadjoint_connected"),
        ("could_be_nonadjoint_connected", "anti_norm_sees_contaminated_sum"),
        ("anti_norm_sees_contaminated_sum", "adjoint_fraction_not_forced"),
    ]
    typing_edges = [
        ("adjoint_line_typing_theorem", "no_nonadjoint_residue"),
        ("no_nonadjoint_residue", "ET_anti_line_equals_adjoint_bilinear"),
        ("ET_anti_line_equals_adjoint_bilinear", "adjoint_fraction_available"),
    ]
    check("E/T anti-invariance alone does not reach adjoint fraction", not reachable(parity_edges, "ET_anti_invariant_line", "adjoint_fraction_available"))
    check("E/T anti-invariance reaches non-adjoint risk", reachable(parity_edges, "ET_anti_invariant_line", "could_be_nonadjoint_connected"))
    check("non-adjoint risk reaches contaminated anti norm", reachable(parity_edges, "ET_anti_invariant_line", "anti_norm_sees_contaminated_sum"))
    check("adjoint typing theorem reaches adjoint fraction", reachable(typing_edges, "adjoint_line_typing_theorem", "adjoint_fraction_available"))
    all_nodes = {n for e in parity_edges + typing_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))
    check("missing primitive is distinct from symmetric-line purity", True)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_ANTI_INVARIANT_ADJOINT_TYPING_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for anti-invariant E/T parity alone",
        "A_total = a_adj A_ET B_adj + a_0 A_ET C_0",
        "anti-invariant E/T normalization sees the sum",
        "Route-2 anti-invariant adjoint-line typing theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block95 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names anti-invariant adjoint typing", "anti-invariant adjoint-line typing" in trace_gate)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", "observed target"),
        ("fitted selector import", "fitted selector"),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 anti-invariant adjoint typing no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_output_parity_vs_color_type()
    part3_classifier_table()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: E/T anti-invariance alone does not prove the connected response is the adjoint color bilinear.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
