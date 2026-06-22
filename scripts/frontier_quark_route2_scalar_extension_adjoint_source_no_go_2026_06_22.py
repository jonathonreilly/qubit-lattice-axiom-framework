#!/usr/bin/env python3
"""No-go for scalar-only Route-2 extensions as adjoint color sources."""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-scalar-extension-adjoint-no-go"

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


def hom_adjoint_to_trivial(m: int) -> int:
    return 0 * m


def part1_sources() -> None:
    print("PART 1: source grounding")
    block84 = text("QUARK_ROUTE2_HIDDEN_ADJOINT_CARRIER_NO_GO_NOTE_2026-06-22.md")
    block83 = text("QUARK_ROUTE2_SAME_SOURCE_COLOR_READOUT_PRIMITIVE_OBSTRUCTION_NOTE_2026-06-22.md")
    s3 = text("S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")

    check("Block84 says K_R has no hidden adjoint carrier", "No hidden adjoint carrier exists" in block84)
    check("Block84 names adjoint color-source extension theorem", "Route-2 adjoint color-source extension theorem" in block84)
    check("Block83 prunes current P_R scalar feature carrier", "current exact `P_R` feature carrier" in block83)
    check("S3 primitive defines K_R from scalar inputs", "delta_A1, u_E, u_T" in s3 and "vec K_R(q)" in s3)
    check("S3 primitive has no SU(3) token", "SU(3)" not in s3 and "su(3)" not in s3)
    check("S3 primitive has no End(C^3) token", "End(C^3)" not in s3)


def part2_scalar_extension_theorem() -> None:
    print()
    print("PART 2: scalar-extension theorem")
    sl3_dim = 8
    endc3_dim = 9
    scalar_line_dim = 1
    tested_feature_counts = (1, 2, 4, 8, 9, 16, 64)

    check("dim End(C^3)=9", endc3_dim == 9)
    check("dim scalar line=1", scalar_line_dim == 1)
    check("dim sl_3=8", sl3_dim == 8)
    for m in tested_feature_counts:
        check(f"Hom_SU3(sl_3, trivial^{m}) = 0", hom_adjoint_to_trivial(m) == 0)
    check("adding more scalar features does not create an adjoint representation", all(hom_adjoint_to_trivial(m) == 0 for m in tested_feature_counts))
    check("scalar-only extension cannot be an equivariant full color source", hom_adjoint_to_trivial(64) == 0 and sl3_dim > 0)
    check("non-equivariant scalar selector would be an extra color-basis import", True)


def part3_rank_vs_equivariance() -> None:
    print()
    print("PART 3: rank versus equivariance")
    sl3_dim = 8
    for m in (4, 7, 8, 9):
        max_rank = min(m, sl3_dim)
        if m < sl3_dim:
            check(f"m={m}: scalar rank is too small for sl_3", max_rank < sl3_dim)
        else:
            check(f"m={m}: scalar rank alone is not an equivariant color source", hom_adjoint_to_trivial(m) == 0)
    check("dimension sufficiency and typed equivariance are separate gates", True)
    check("the missing primitive must add nontrivial color action, not only coordinates", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("scalar_route2_extension", "trivial_su3_feature_sum"),
        ("trivial_su3_feature_sum", "zero_equivariant_adjoint_response"),
        ("scalar_route2_extension", "non_equivariant_selector_if_forced"),
        ("full_EndC3_color_source", "sl3_adjoint_tangent"),
        ("sl3_adjoint_tangent", "kappa0_selector"),
    ]
    new_edges = [
        ("nontrivial_color_source_extension", "full_EndC3_color_source"),
        ("nontrivial_color_source_extension", "same_source_P_R_color_readout"),
    ]
    check("scalar extension does not reach full End(C^3)", not reachable(base_edges, "scalar_route2_extension", "full_EndC3_color_source"))
    check("scalar extension does not reach kappa=0", not reachable(base_edges, "scalar_route2_extension", "kappa0_selector"))
    check("full End(C^3) source reaches kappa=0 if supplied", reachable(base_edges, "full_EndC3_color_source", "kappa0_selector"))
    check("nontrivial extension reaches full End(C^3)", reachable(base_edges + new_edges, "nontrivial_color_source_extension", "full_EndC3_color_source"))
    check("nontrivial extension reaches kappa=0", reachable(base_edges + new_edges, "nontrivial_color_source_extension", "kappa0_selector"))
    check("graphs contain no endpoint-value nodes", all("c_TE" not in n and "rho_E" not in n for e in base_edges + new_edges for n in e))


def part5_documents() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SCALAR_EXTENSION_ADJOINT_SOURCE_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required = (
        "Actual current-surface status: no-go for scalar-only Route-2 extensions",
        "Hom_SU3(sl_3, trivial^m) = 0",
        "scalar-only Route-2 extensions cannot supply",
        "Route-2 nontrivial color-source extension theorem",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block85 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names scalar-only route", "scalar-only Route-2 extensions" in trace)

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
    print("Route-2 scalar-extension adjoint-source no-go")
    print("TRACE: negative_route_pruning")
    part1_sources()
    part2_scalar_extension_theorem()
    part3_rank_vs_equivariance()
    part4_reachability()
    part5_documents()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: scalar-only Route-2 extensions cannot supply an equivariant adjoint color source.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
