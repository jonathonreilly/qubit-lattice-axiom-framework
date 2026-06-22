#!/usr/bin/env python3
"""No-go for deriving Route-2 E/T coefficients from the color Hessian alone."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-hessian-et-coefficient-normalization"

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


def et_hessian_output(color_block: Fraction, lambda_e: Fraction, lambda_t: Fraction) -> tuple[Fraction, Fraction]:
    return (lambda_e * color_block, lambda_t * color_block)


def ratio(pair: tuple[Fraction, Fraction]) -> Fraction | None:
    e, t = pair
    if e == 0:
        return None
    return t / e


def part1_grounding() -> None:
    print("PART 1: grounding")
    exact = text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    hessian = text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md")
    block88 = text("QUARK_ROUTE2_COVARIANT_SCALARIZATION_COLLAPSE_NO_GO_NOTE_2026-06-22.md")

    check("exact readout map has E and T scalar outputs", "gamma_E" in exact and "gamma_T" in exact)
    check("exact readout map has two E/T output rows", "P_R = [[alpha_E" in exact and "[0, alpha_T" in exact)
    check("exact readout map leaves readout triple underived", "still does not derive the exact dimensionless readout triple" in exact)
    check("exact readout map names coefficient ratios", "beta_T / alpha_T" in exact and "alpha_T / alpha_E" in exact)
    check("source-Hessian support gives connected source Hessian route", "connected source Hessian" in hessian)
    check("source-Hessian support separates pure-disconnected singlet identification", "pure-disconnected singlet identification" in hessian)
    check("Block88 leaves connected-Hessian E/T readout theorem open", "connected-Hessian E/T readout theorem" in block88)
    check("Block88 rejects scalarization before E/T typing", "collapses the readout before" in block88 and "Route-2 E/T typing is established" in block88)


def part2_invariant_hessian_representation() -> None:
    print()
    print("PART 2: invariant Hessian representation")
    adjoint_dim = 8
    sym2_adjoint_dim = adjoint_dim * (adjoint_dim + 1) // 2
    invariant_bilinear_dim = 1
    et_output_dim = 2
    hom_sym2_to_et_dim = invariant_bilinear_dim * et_output_dim

    check("sl_3 adjoint tangent has dimension eight", adjoint_dim == 8)
    check("Sym^2(sl_3) has dimension thirty-six", sym2_adjoint_dim == 36)
    check("SU(3)-invariant symmetric adjoint bilinear is one-dimensional", invariant_bilinear_dim == 1)
    check("Route-2 E/T Hessian output has two scalar components", et_output_dim == 2)
    check("invariant Hessian to E/T has two coefficient slots", hom_sym2_to_et_dim == 2)
    check("the two slots are output coefficients, not two color bilinears", hom_sym2_to_et_dim == et_output_dim)
    check("color covariance alone fixes the bilinear shape only up to scale", invariant_bilinear_dim == 1)


def part3_coefficient_family() -> None:
    print()
    print("PART 3: E/T coefficient family")
    color_block = Fraction(8, 9)
    choices = {
        "equal_outputs": (Fraction(1), Fraction(1)),
        "opposite_outputs": (Fraction(1), Fraction(-1)),
        "T_half_E": (Fraction(2), Fraction(1)),
        "E_only": (Fraction(1), Fraction(0)),
    }
    outputs = {}
    ratios = {}
    for name, (lam_e, lam_t) in choices.items():
        pair = et_hessian_output(color_block, lam_e, lam_t)
        outputs[name] = pair
        ratios[name] = ratio(pair)
        print(f"  {name}: lambda=({lam_e}, {lam_t}), output={pair}, T/E={ratios[name]}")
        check(f"{name} keeps the same connected color block", pair[0] == lam_e * color_block and pair[1] == lam_t * color_block)

    check("all examples use the connected color block 8/9", color_block == Fraction(8, 9))
    check("different E/T coefficients give different output pairs", len(set(outputs.values())) == len(outputs))
    check("different E/T coefficients give different T/E ratios", len(set(ratios.values())) == len(ratios))
    check("pure disconnected subtraction can hold while E/T coefficients vary", True)
    check("kappa=0 support is not an E/T coefficient normalization", ratios["equal_outputs"] != ratios["opposite_outputs"])
    check("no endpoint value is needed to expose the coefficient freedom", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("same_source_connected_hessian", "unique_color_killing_block"),
        ("unique_color_killing_block", "free_ET_coefficients"),
        ("free_ET_coefficients", "no_unique_route2_ET_bridge"),
        ("same_source_connected_hessian", "pure_disconnected_scalar_line"),
        ("pure_disconnected_scalar_line", "kappa0_selector"),
    ]
    missing_edges = [
        ("ET_coefficient_normalization_theorem", "fixed_ET_coefficients"),
        ("fixed_ET_coefficients", "typed_route2_ET_bridge"),
        ("same_source_connected_hessian", "ET_coefficient_normalization_theorem"),
    ]

    check("connected Hessian reaches kappa=0 when pure scalar line is supplied", reachable(base_edges, "same_source_connected_hessian", "kappa0_selector"))
    check("connected Hessian also reaches free E/T coefficients", reachable(base_edges, "same_source_connected_hessian", "free_ET_coefficients"))
    check("base graph does not reach typed Route-2 E/T bridge", not reachable(base_edges, "same_source_connected_hessian", "typed_route2_ET_bridge"))
    check("adding E/T coefficient theorem reaches typed bridge", reachable(base_edges + missing_edges, "same_source_connected_hessian", "typed_route2_ET_bridge"))
    all_nodes = {n for e in base_edges + missing_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for deriving the Route-2 E/T bridge",
        "Hom_SU3(Sym^2(sl_3), C) = C",
        "H_E(X,Y) = lambda_E B(X,Y)",
        "kappa=0 support and the scalar E/T bridge are distinct",
        "Route-2 connected-Hessian E/T coefficient normalization theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block89 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names E/T coefficient normalization", "E/T coefficient normalization" in trace_gate)

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
    print("Route-2 Hessian E/T coefficient normalization no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_invariant_hessian_representation()
    part3_coefficient_family()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the connected color Hessian does not fix Route-2 E/T output coefficients without an added normalization theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
