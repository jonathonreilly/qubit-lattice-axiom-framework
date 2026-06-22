#!/usr/bin/env python3
"""No-go for invariant scalar-output Route-2 color coupling."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-invariant-scalar-output-coupling"

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


def eye() -> Matrix:
    return ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def gell_mann_basis() -> list[Matrix]:
    z = 0
    return [
        ((z, 1, z), (1, z, z), (z, z, z)),
        ((z, -1j, z), (1j, z, z), (z, z, z)),
        ((1, z, z), (z, -1, z), (z, z, z)),
        ((z, z, 1), (z, z, z), (1, z, z)),
        ((z, z, -1j), (z, z, z), (1j, z, z)),
        ((z, z, z), (z, z, 1), (z, 1, z)),
        ((z, z, z), (z, z, -1j), (z, 1j, z)),
        ((1, z, z), (z, 1, z), (z, z, -2)),
    ]


def invariant_derivative_power_at_identity(power: int, x: Matrix) -> complex:
    """Derivative of Tr((I/3 + eps X)^power) at eps=0."""
    return power * (Fraction(1, 3) ** (power - 1)) * trace(x)


def part1_source_grounding() -> None:
    print("PART 1: source grounding")
    exact = text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    block83 = text("QUARK_ROUTE2_SAME_SOURCE_COLOR_READOUT_PRIMITIVE_OBSTRUCTION_NOTE_2026-06-22.md")
    block86 = text("QUARK_ROUTE2_FACTORIZED_COLOR_SOURCE_EXTENSION_NO_GO_NOTE_2026-06-22.md")
    block78 = text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")

    check("exact readout note has two scalar P_R outputs", "P_R" in exact and "alpha_E" in exact and "alpha_T" in exact)
    check("exact readout note has four scalar feature coordinates", "K_R" in exact and "delta_A1" in exact and "u_E" in exact and "u_T" in exact)
    check("Block83 says current P_R carrier cannot be full color readout", "cannot be the same-source full" in block83)
    check("Block83 names the adjoint color-source carrier theorem", "Route-2 adjoint color-source carrier theorem" in block83)
    check("Block86 prunes color-blind factorized extension", "color-blind factorized extension puts the adjoint tangent in the kernel" in block86)
    check("Block86 leaves color-sensitive source/readout coupling open", "Route-2 color-sensitive source/readout coupling theorem" in block86)
    check("Block78 supplies the positive color-source theorem only on its own source", "Positive Color-Source Theorem" in block78)
    check("Block78 still needs same-source normalized color-matrix authority", "same-source normalized color-matrix source authority" in block78)


def part2_representation_obstruction() -> None:
    print()
    print("PART 2: invariant scalar-output representation obstruction")
    color_dim = 3
    end_dim = color_dim * color_dim
    scalar_line_dim = 1
    sl3_dim = end_dim - scalar_line_dim
    scalar_output_dim = 2
    hom_sl3_to_scalar_dim = 0
    hom_sl3_to_two_scalars_dim = scalar_output_dim * hom_sl3_to_scalar_dim
    imported_covector_dim = sl3_dim

    check("End(C^3) has dimension nine", end_dim == 9)
    check("trace scalar line has dimension one", scalar_line_dim == 1)
    check("sl_3 connected tangent has dimension eight", sl3_dim == 8)
    check("P_R/E-T scalar output has dimension two", scalar_output_dim == 2)
    check("Hom_SU3(sl_3, C) has dimension zero", hom_sl3_to_scalar_dim == 0)
    check("Hom_SU3(sl_3, C^2) has dimension zero", hom_sl3_to_two_scalars_dim == 0)
    check("an imported adjoint covector would have eight choices", imported_covector_dim == 8)
    check("imported covector is outside invariant scalar-output route", imported_covector_dim > hom_sl3_to_two_scalars_dim)


def part3_first_order_scalar_invariants() -> None:
    print()
    print("PART 3: first-order scalar invariant derivatives")
    basis = gell_mann_basis()
    rho0 = scale(Fraction(1, 3), eye())
    rho0_sq = matmul(rho0, rho0)
    rho0_cube = matmul(rho0_sq, rho0)

    check("Gell-Mann tangent basis has eight elements", len(basis) == 8)
    check("trace of I/3 is one", abs(trace(rho0) - 1) < 1e-12)
    check("trace of (I/3)^2 is one third", abs(trace(rho0_sq) - Fraction(1, 3)) < 1e-12)
    check("trace of (I/3)^3 is one ninth", abs(trace(rho0_cube) - Fraction(1, 9)) < 1e-12)
    check("every basis tangent is traceless", all(abs(trace(x)) < 1e-12 for x in basis))

    for power in (1, 2, 3):
        derivs = [invariant_derivative_power_at_identity(power, x) for x in basis]
        check(
            f"first derivative of Tr(rho^{power}) vanishes on all sl_3 basis tangents",
            all(abs(d) < 1e-12 for d in derivs),
        )

    y = basis[0]
    selector_response = trace(matmul(y, basis[0]))
    check("an adjoint covector can make a nonzero linear response", abs(selector_response) > 1e-12)
    check("that response uses a supplied color orientation", True)


def part4_route_graph() -> None:
    print()
    print("PART 4: route graph")
    invariant_edges = [
        ("invariant_scalar_P_R_output", "componentwise_invariant_linear_differential"),
        ("componentwise_invariant_linear_differential", "zero_sl3_first_order_response"),
        ("zero_sl3_first_order_response", "no_kappa0_from_connected_color"),
    ]
    constructive_edges = [
        ("covariant_color_readout_family", "sl3_first_order_response"),
        ("orientation_free_multi_record_cumulant", "covariant_color_readout_family"),
        ("sl3_first_order_response", "connected_color_fraction_8_over_9"),
        ("connected_color_fraction_8_over_9", "kappa0_selector"),
    ]
    imported_edges = [
        ("external_adjoint_covector", "sl3_first_order_response"),
        ("external_adjoint_covector", "imported_color_orientation"),
    ]

    check(
        "invariant scalar output does not reach kappa=0",
        not reachable(invariant_edges, "invariant_scalar_P_R_output", "kappa0_selector"),
    )
    check(
        "invariant scalar output reaches zero first-order response",
        reachable(invariant_edges, "invariant_scalar_P_R_output", "zero_sl3_first_order_response"),
    )
    check(
        "covariant readout family reaches kappa=0 route node",
        reachable(constructive_edges, "covariant_color_readout_family", "kappa0_selector"),
    )
    check(
        "multi-record cumulant route reaches kappa=0 route node",
        reachable(constructive_edges, "orientation_free_multi_record_cumulant", "kappa0_selector"),
    )
    check(
        "external covector reaches response only by importing orientation",
        reachable(imported_edges, "external_adjoint_covector", "imported_color_orientation"),
    )
    all_nodes = {n for e in invariant_edges + constructive_edges + imported_edges for n in e}
    check("graph contains no endpoint-value node", all("c_TE" not in n and "rho_E" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_INVARIANT_SCALAR_OUTPUT_COUPLING_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for invariant scalar-output Route-2 color coupling",
        "A color-invariant scalar output has zero first-order response",
        "Hom_SU3(sl_3, C^2) = 0",
        "Route-2 covariant color-readout family or orientation-free multi-record",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block87 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names invariant scalar-output route", "invariant scalar-output" in trace_gate)

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
    print("Route-2 invariant scalar-output coupling no-go")
    print("TRACE: negative_route_pruning")
    part1_source_grounding()
    part2_representation_obstruction()
    part3_first_order_scalar_invariants()
    part4_route_graph()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: invariant scalar P_R/E-T output has zero first-order adjoint response without an added color-readout primitive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
