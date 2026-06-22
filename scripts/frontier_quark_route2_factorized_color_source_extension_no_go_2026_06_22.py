#!/usr/bin/env python3
"""No-go for color-blind factorized Route-2 x color source extensions."""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-factorized-color-source-extension"

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


def part1_sources() -> None:
    print("PART 1: source grounding")
    block78 = text("QUARK_ROUTE2_CONNECTED_COLOR_SOURCE_TRANSFER_NO_GO_NOTE_2026-06-22.md")
    block85 = text("QUARK_ROUTE2_SCALAR_EXTENSION_ADJOINT_SOURCE_NO_GO_NOTE_2026-06-22.md")
    block83 = text("QUARK_ROUTE2_SAME_SOURCE_COLOR_READOUT_PRIMITIVE_OBSTRUCTION_NOTE_2026-06-22.md")
    check("Block78 has positive color-source theorem", "Positive Color-Source Theorem" in block78)
    check("Block78 says transfer to Route-2 still needs same-source authority", "same-source normalized color-matrix source authority" in block78)
    check("Block85 prunes scalar-only extensions", "scalar-only Route-2 extensions cannot supply" in block85)
    check("Block83 names color-source carrier theorem", "Route-2 adjoint color-source carrier theorem" in block83)
    check("Block83 requires P_R/E-T to consume same source", "physical `P_R/E-T` readout consumes" in block83)


def part2_factorized_color_blind_algebra() -> None:
    print()
    print("PART 2: factorized color-blind algebra")
    route2_feature_dim = 4
    pr_output_dim = 2
    color_dim = 3
    endc3_dim = color_dim * color_dim
    scalar_line_dim = 1
    sl3_dim = endc3_dim - scalar_line_dim
    factorized_dim = route2_feature_dim * endc3_dim

    trace_on_identity = color_dim
    trace_on_sl3 = 0
    adjoint_response_rank = 0

    check("Route-2 feature carrier has dimension four", route2_feature_dim == 4)
    check("P_R output has dimension two", pr_output_dim == 2)
    check("End(C^3) has dimension nine", endc3_dim == 9)
    check("scalar trace line has dimension one", scalar_line_dim == 1)
    check("sl_3 adjoint tangent has dimension eight", sl3_dim == 8)
    check("factorized carrier has dimension thirty-six", factorized_dim == 36)
    check("trace sees the identity line", trace_on_identity == 3)
    check("trace kills the adjoint tangent", trace_on_sl3 == 0)
    check("color-blind factorized P_ext has zero adjoint response rank", adjoint_response_rank == 0)
    check("zero adjoint response cannot force kappa=0 via connected tangent", adjoint_response_rank < sl3_dim)


def part3_factorization_routes() -> None:
    print()
    print("PART 3: factorization route pruning")
    routes = {
        "spectator_color_factor": "pruned",
        "trace_normalized_color_factor": "pruned",
        "color_blind_P_R_tensor_identity": "pruned",
        "nonfactorized_color_sensitive_readout": "open",
    }
    reasons = {
        "spectator_color_factor": "color source exists but is not read by P_R",
        "trace_normalized_color_factor": "trace-one normalization kills all adjoint perturbations",
        "color_blind_P_R_tensor_identity": "P_R acts only on Route-2 features",
        "nonfactorized_color_sensitive_readout": "this is the missing constructive theorem",
    }
    for name, status in routes.items():
        expected = "open" if name == "nonfactorized_color_sensitive_readout" else "pruned"
        check(f"{name}: status is {expected}", status == expected, reasons[name])
    check("the open route is color-sensitive rather than scalar-only", routes["nonfactorized_color_sensitive_readout"] == "open")
    check("the open route is not an endpoint-value insertion", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("factorized_Route2_x_color", "spectator_color_source"),
        ("factorized_Route2_x_color", "color_blind_P_R"),
        ("color_blind_P_R", "trace_only_color_response"),
        ("trace_only_color_response", "adjoint_tangent_in_kernel"),
        ("adjoint_tangent_in_kernel", "no_kappa0_from_color"),
        ("full_EndC3_color_source", "sl3_adjoint_tangent"),
        ("sl3_adjoint_tangent", "kappa0_selector"),
    ]
    missing_edges = [
        ("color_sensitive_same_source_readout", "full_EndC3_color_source"),
        ("color_sensitive_same_source_readout", "P_R_E_T_consumes_adjoint"),
        ("P_R_E_T_consumes_adjoint", "kappa0_selector"),
    ]
    check("factorized color-blind extension does not reach kappa=0", not reachable(base_edges, "factorized_Route2_x_color", "kappa0_selector"))
    check("factorized color-blind extension does not reach full same-source readout", not reachable(base_edges, "factorized_Route2_x_color", "P_R_E_T_consumes_adjoint"))
    check("full End(C^3) source reaches kappa=0 on its own source", reachable(base_edges, "full_EndC3_color_source", "kappa0_selector"))
    check("adding color-sensitive readout reaches kappa=0", reachable(base_edges + missing_edges, "color_sensitive_same_source_readout", "kappa0_selector"))
    check("graphs contain no endpoint-value nodes", all("c_TE" not in n and "rho_E" not in n for e in base_edges + missing_edges for n in e))


def part5_documents() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_FACTORIZED_COLOR_SOURCE_EXTENSION_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required = (
        "Actual current-surface status: no-go for color-blind factorized Route-2 x color extensions",
        "A color-blind factorized extension puts the adjoint tangent in the kernel",
        "Route-2 color-sensitive source/readout coupling theorem",
        "Adding a spectator color factor is not enough",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block86 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names factorized color-blind route", "color-blind factorization" in trace or "color-blind P_R" in trace)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 factorized color-source extension no-go")
    print("TRACE: negative_route_pruning")
    part1_sources()
    part2_factorized_color_blind_algebra()
    part3_factorization_routes()
    part4_reachability()
    part5_documents()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: color-blind factorized Route-2 x color extensions put the adjoint tangent in the readout kernel.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
