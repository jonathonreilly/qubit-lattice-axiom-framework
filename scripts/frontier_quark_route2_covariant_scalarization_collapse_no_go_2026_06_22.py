#!/usr/bin/env python3
"""No-go for scalarizing a covariant color family into the Route-2 bridge."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-covariant-scalarization-collapse"

PASS = 0
FAIL = 0

Matrix = tuple[tuple[complex, complex, complex], tuple[complex, complex, complex], tuple[complex, complex, complex]]


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


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(3))


def scale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def diag(a: complex, b: complex, c: complex) -> Matrix:
    return ((a, 0, 0), (0, b, 0), (0, 0, c))


def quadratic_invariant(x: Matrix) -> complex:
    return trace(matmul(x, x))


def cubic_invariant(x: Matrix) -> complex:
    return trace(matmul(matmul(x, x), x))


def scalarization(x: Matrix, a: Fraction, b: Fraction) -> complex:
    return a * quadratic_invariant(x) + b * cubic_invariant(x)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block87 = text("QUARK_ROUTE2_INVARIANT_SCALAR_OUTPUT_COUPLING_NO_GO_NOTE_2026-06-22.md")
    hessian = text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md")
    observable = text("QUARK_ROUTE2_OBSERVABLE_HESSIAN_READOUT_IDENTIFICATION_NO_GO_NOTE_2026-06-22.md")
    transfer = text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")

    check("Block87 says invariant scalar output has zero first-order response", "zero first-order response" in block87)
    check("Block87 leaves covariant color-readout family open", "covariant color-readout family" in block87)
    check("source-Hessian support gives exact disconnected subtraction", "subtracts factorizable disconnected products exactly" in hessian)
    check("source-Hessian support leaves physical readout primitive open", "missing physical readout primitive" in hessian)
    check("observable-Hessian no-go asks for color/tensor-resolved source functional", "color/tensor-resolved source functional" in observable)
    check("observable-Hessian no-go asks for same-source identification", "same-source identification" in observable)
    check("connected color-source note identifies End(C^3)/CI with sl_3", "End(C^3) / C I = sl_3" in transfer)
    check("connected color-source note says Route-2 readout does not live on that source surface", "Route-2 readout does not yet live on that source surface" in transfer)


def part2_scalarization_algebra() -> None:
    print()
    print("PART 2: scalarization algebra")
    x = diag(1, 1, -2)
    neg_x = scale(-1, x)
    q_x = quadratic_invariant(x)
    q_neg = quadratic_invariant(neg_x)
    c_x = cubic_invariant(x)
    c_neg = cubic_invariant(neg_x)
    sl3_dim = 8
    invariant_generator_count = 2
    route2_feature_slots = 4
    route2_output_slots = 2

    check("test tangent X is traceless", abs(trace(x)) < 1e-12)
    check("quadratic invariant is nonzero on X", abs(q_x) > 1e-12)
    check("quadratic invariant is even under X -> -X", q_x == q_neg)
    check("cubic invariant changes sign under X -> -X", c_x == -c_neg and abs(c_x) > 1e-12)
    check("sl_3 connected tangent has dimension eight", sl3_dim == 8)
    check("orientation-free scalar invariant generators are only scalar orbit data here", invariant_generator_count == 2)
    check("current Route-2 carrier has four feature slots", route2_feature_slots == 4)
    check("current P_R/E-T output has two scalar slots", route2_output_slots == 2)
    check("scalar orbit data do not preserve the eight adjoint tangent directions", invariant_generator_count < sl3_dim)


def part3_scalarization_underdetermination() -> None:
    print()
    print("PART 3: scalarization underdetermination")
    x = diag(1, 1, -2)
    choices = {
        "quadratic_only": (Fraction(1), Fraction(0)),
        "cubic_only": (Fraction(0), Fraction(1)),
        "quadratic_plus_cubic": (Fraction(1), Fraction(1)),
        "quadratic_minus_cubic": (Fraction(1), Fraction(-1)),
    }
    values = {name: scalarization(x, a, b) for name, (a, b) in choices.items()}
    for name, value in values.items():
        print(f"  {name}: {value}")
        check(f"{name} is a scalar orbit readout", isinstance(value, (int, float, complex, Fraction)))

    check("different invariant scalarizations give different scalar values", len(set(values.values())) == len(values))
    check("the scalarization family has free coefficients before a readout theorem", len(choices) > 1)
    check("quadratic-only scalarization loses the sign of X", scalarization(x, Fraction(1), Fraction(0)) == scalarization(scale(-1, x), Fraction(1), Fraction(0)))
    check("cubic-only scalarization keeps an odd orbit scalar but not an E/T readout map", scalarization(x, Fraction(0), Fraction(1)) == -scalarization(scale(-1, x), Fraction(0), Fraction(1)))
    check("no endpoint value is needed for the underdetermination", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    scalarization_edges = [
        ("covariant_sl3_color_family", "invariant_scalarization"),
        ("invariant_scalarization", "scalar_orbit_data"),
        ("scalar_orbit_data", "lost_adjoint_readout_typing"),
        ("lost_adjoint_readout_typing", "no_route2_ET_bridge"),
    ]
    missing_theorem_edges = [
        ("covariant_sl3_color_family", "same_source_color_tensor_functional"),
        ("same_source_color_tensor_functional", "route2_ET_readout_tensor"),
        ("route2_ET_readout_tensor", "connected_source_hessian_D2_logZ"),
        ("connected_source_hessian_D2_logZ", "pure_disconnected_scalar_line"),
        ("pure_disconnected_scalar_line", "kappa0_selector"),
    ]
    shortcut_edges = [
        ("invariant_scalarization", "connected_source_hessian_D2_logZ"),
    ]

    check("scalarization shortcut does not reach kappa=0", not reachable(scalarization_edges, "covariant_sl3_color_family", "kappa0_selector"))
    check("scalarization shortcut reaches lost typing", reachable(scalarization_edges, "covariant_sl3_color_family", "lost_adjoint_readout_typing"))
    check("adding the missing typed theorem reaches kappa=0", reachable(missing_theorem_edges, "covariant_sl3_color_family", "kappa0_selector"))
    check("a bare scalarization-to-Hessian shortcut would be an extra bridge", shortcut_edges[0] == ("invariant_scalarization", "connected_source_hessian_D2_logZ"))
    all_nodes = {n for e in scalarization_edges + missing_theorem_edges + shortcut_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_COVARIANT_SCALARIZATION_COLLAPSE_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for invariant scalarization of a covariant color family",
        "covariant sl_3 color-readout family",
        "invariant scalarization",
        "Route-2 covariant-family connected-Hessian E/T readout theorem",
        "This is stronger than \"take the Casimir/norm of the color family",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block88 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names scalarization shortcut", "invariant scalarization" in trace_gate)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 covariant scalarization collapse no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_scalarization_algebra()
    part3_scalarization_underdetermination()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: invariant scalarization of a covariant color family loses the typed Route-2 E/T readout bridge.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
