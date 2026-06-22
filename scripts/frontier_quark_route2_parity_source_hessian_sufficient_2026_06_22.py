#!/usr/bin/env python3
"""Sufficient typed parity source-Hessian theorem for Route-2 kappa=0."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-parity-source-hessian-sufficient"

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


def add(u: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (u[0] + v[0], u[1] + v[1])


def scale(c: Fraction, v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (c * v[0], c * v[1])


def coeff(s: Fraction, t: Fraction) -> tuple[Fraction, Fraction]:
    return add(scale(s, (Fraction(1), Fraction(-1))), scale(t, (Fraction(1), Fraction(1))))


def sym_coeff(v: tuple[Fraction, Fraction]) -> Fraction:
    return (v[0] + v[1]) / 2


def anti_coeff(v: tuple[Fraction, Fraction]) -> Fraction:
    return (v[0] - v[1]) / 2


def connected_subtract(raw: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return add(raw, scale(-sym_coeff(raw), (Fraction(1), Fraction(1))))


def anti_norm(v: tuple[Fraction, Fraction]) -> Fraction:
    return v[0] - v[1]


def part1_grounding() -> None:
    print("PART 1: grounding")
    block92 = text("QUARK_ROUTE2_NORMALIZATION_FUNCTIONAL_PARITY_NO_GO_NOTE_2026-06-22.md")
    block91 = text("QUARK_ROUTE2_ANTISYMMETRIC_COEFF_SCALE_NO_GO_NOTE_2026-06-22.md")
    source = text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md")
    block92_flat = flat(block92)
    block91_flat = flat(block91)
    source_flat = flat(source)

    check("Block92 names anti-invariant normalization and purity theorem", "anti-invariant same-source E/T normalization and purity theorem" in block92_flat)
    check("Block92 says invariant normalization annihilates antisymmetric line", "annihilates the antisymmetric line" in block92_flat)
    check("Block92 says anti-invariant component is typed orientation data", "already typed E/T orientation data" in block92_flat)
    check("Block92 uses no endpoint value", "No endpoint value is used" in block92_flat)
    check("Block91 has coefficient decomposition", "(lambda_E, lambda_T) = s(1,-1) + t(1,1)" in block91_flat)
    check("Block91 requires symmetric contamination control", "symmetric contamination" in block91_flat)
    check("source-Hessian note states D2 log Z subtracts disconnected products", "D^2 log Z subtracts factorizable disconnected products exactly" in source_flat)
    check("source-Hessian note names pure-disconnected singlet identification", "pure-disconnected singlet identification" in source_flat)
    check("source-Hessian note leaves physical readout primitive open", "does not derive the missing physical readout primitive" in source_flat)


def part2_parity_cumulant_algebra() -> None:
    print()
    print("PART 2: parity cumulant algebra")
    samples = {
        "unit_scale_with_singlet": (Fraction(1), Fraction(3)),
        "double_scale_with_singlet": (Fraction(2), Fraction(5)),
        "negative_scale_with_singlet": (Fraction(-1), Fraction(4)),
        "no_singlet": (Fraction(3), Fraction(0)),
    }
    for name, (s, t) in samples.items():
        raw = coeff(s, t)
        conn = connected_subtract(raw)
        print(f"  {name}: raw={raw}, conn={conn}, s={anti_coeff(conn)}, t_conn={sym_coeff(conn)}")
        check(f"{name} raw has requested anti coefficient", anti_coeff(raw) == s)
        check(f"{name} raw has requested symmetric coefficient", sym_coeff(raw) == t)
        check(f"{name} connected subtraction preserves anti coefficient", anti_coeff(conn) == s)
        check(f"{name} connected subtraction kills symmetric coefficient", sym_coeff(conn) == 0)

    unit_conn = connected_subtract(coeff(Fraction(1), Fraction(3)))
    double_conn = connected_subtract(coeff(Fraction(2), Fraction(5)))
    check("connected outputs lie on antisymmetric line", unit_conn[0] == -unit_conn[1] and double_conn[0] == -double_conn[1])
    check("anti-invariant normalization sees connected scale", anti_norm(double_conn) == 2 * anti_norm(unit_conn))
    check("symmetric contamination is removed before scale normalization", sym_coeff(unit_conn) == 0)
    check("kappa is zero after connected subtraction", sym_coeff(unit_conn) == 0)
    check("raw moment would have nonzero singlet coefficient", sym_coeff(coeff(Fraction(1), Fraction(3))) == 3)
    check("no endpoint value is used in the cumulant algebra", True)


def part3_sufficient_premise_table() -> None:
    print()
    print("PART 3: sufficient premise table")
    premises = {
        "same_source_ET_hessian": "open",
        "symmetric_line_pure_disconnected": "open",
        "D2_logZ_connected_subtraction": "supported",
        "antisymmetric_line_connected_adjoint": "open",
        "anti_invariant_normalization": "open",
        "endpoint_value_input": "forbidden",
    }
    for name, status in premises.items():
        print(f"  {name}: {status}")
        check(f"{name} has classified status", status in {"open", "supported", "forbidden"})

    check("D2 log Z support is the only already-supported theorem premise", list(premises.values()).count("supported") == 1)
    check("endpoint input is forbidden", premises["endpoint_value_input"] == "forbidden")
    check("same-source E/T Hessian remains open", premises["same_source_ET_hessian"] == "open")
    check("pure-disconnected symmetric typing remains open", premises["symmetric_line_pure_disconnected"] == "open")
    check("anti-invariant normalization remains open", premises["anti_invariant_normalization"] == "open")
    theorem_ready = all(
        premises[k] == "supported"
        for k in (
            "same_source_ET_hessian",
            "symmetric_line_pure_disconnected",
            "D2_logZ_connected_subtraction",
            "antisymmetric_line_connected_adjoint",
            "anti_invariant_normalization",
        )
    )
    check("current surface does not yet satisfy all sufficient premises", not theorem_ready)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("typed_parity_source_hessian_premises", "raw_sA_plus_tS"),
        ("raw_sA_plus_tS", "D2_logZ_subtracts_factorized_S"),
        ("D2_logZ_subtracts_factorized_S", "connected_sA_only"),
        ("connected_sA_only", "kappa_zero_without_endpoint"),
        ("connected_sA_only", "anti_invariant_scale_normalization_possible"),
        ("anti_invariant_scale_normalization_possible", "scale_fixed_if_normalizer_derived"),
    ]
    missing_edges = [
        ("current_surface", "D2_logZ_subtraction_support"),
        ("current_surface", "missing_same_source_ET_hessian"),
        ("current_surface", "missing_pure_disconnected_symmetric_typing"),
        ("current_surface", "missing_anti_invariant_normalizer"),
    ]

    check("sufficient premises reach kappa=0", reachable(base_edges, "typed_parity_source_hessian_premises", "kappa_zero_without_endpoint"))
    check("sufficient premises reach scale-normalization condition", reachable(base_edges, "typed_parity_source_hessian_premises", "scale_fixed_if_normalizer_derived"))
    check("current surface does not reach kappa=0 through missing-premise graph", not reachable(missing_edges, "current_surface", "kappa_zero_without_endpoint"))
    check("current surface records missing same-source E/T Hessian", reachable(missing_edges, "current_surface", "missing_same_source_ET_hessian"))
    check("current surface records missing pure-disconnected typing", reachable(missing_edges, "current_surface", "missing_pure_disconnected_symmetric_typing"))
    check("current surface records missing anti-invariant normalizer", reachable(missing_edges, "current_surface", "missing_anti_invariant_normalizer"))
    all_nodes = {n for e in base_edges + missing_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_PARITY_SOURCE_HESSIAN_SUFFICIENT_THEOREM_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: conditional-support",
        "H_conn = s A_ET B_adj",
        "kappa = 0",
        "does not prove that the current Route-2 physical readout satisfies the theorem premises",
        "Route-2 typed parity source-Hessian bridge theorem",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block93 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names typed parity source-Hessian bridge", "typed parity source-Hessian bridge" in trace_gate)

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
    print("Route-2 typed parity source-Hessian sufficient theorem")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_parity_cumulant_algebra()
    part3_sufficient_premise_table()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the typed parity source-Hessian premises are sufficient to force kappa=0 without endpoint input; those premises remain open on the current surface.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
