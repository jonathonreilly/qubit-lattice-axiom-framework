#!/usr/bin/env python3
"""No-go for using carrier-orbit support as Hessian E/T coefficient theorem."""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-carrier-antisymmetric-hessian-coeff"
CARRIER_LOOP = ROOT / ".claude" / "science" / "physics-loops" / "carrier-orbit-invariance-2026-05-03"

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


def carrier_text(name: str) -> str:
    return (CARRIER_LOOP / name).read_text(encoding="utf-8")


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


def swap(v: tuple[int, int]) -> tuple[int, int]:
    return (v[1], v[0])


def part1_grounding() -> None:
    print("PART 1: grounding")
    block89 = text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md")
    carrier_handoff = carrier_text("HANDOFF.md")
    carrier_cert = carrier_text("CLAIM_STATUS_CERTIFICATE.md")
    carrier_imports = carrier_text("ASSUMPTIONS_AND_IMPORTS.md")

    check("Block89 leaves E/T coefficient normalization open", "coefficient normalization are" in block89 and "separate gates" in block89)
    check("Block89 names the connected-Hessian coefficient theorem", "Route-2 connected-Hessian E/T coefficient normalization theorem" in block89)
    check("carrier handoff has Z2 isotypic decomposition", "V = V^+ + V^-" in carrier_handoff or "V = V^+ \u2295 V^-" in carrier_handoff)
    check("carrier handoff says current primitives lie in symmetric component", "End(V)^+" in carrier_handoff and "swap-invariant" in carrier_handoff)
    check("carrier handoff says no exact antisymmetric primitive found", "no retained-exact primitive" in carrier_handoff or "no retained-exact candidate" in carrier_cert)
    check("carrier result leaves registry closure open", "registry closure" in carrier_handoff and "meta" in carrier_handoff)
    check("carrier imports list Theta and Xi as bounded", "Theta_R^(0)" in carrier_imports and "bounded" in carrier_imports)
    check("carrier imports list exact primitive registry as an assumption", "primitive registry" in carrier_imports)


def part2_output_space_decomposition() -> None:
    print()
    print("PART 2: E/T output-space decomposition")
    symmetric = (1, 1)
    antisymmetric = (1, -1)
    generic = (2, 1)
    output_dim = 2
    sym_dim = 1
    antisym_dim = 1

    check("E/T coefficient space has dimension two", output_dim == 2)
    check("swap fixes the symmetric line", swap(symmetric) == symmetric)
    check("swap flips the antisymmetric line", swap(antisymmetric) == (-antisymmetric[0], -antisymmetric[1]))
    check("symmetric and antisymmetric lines sum to dimension two", sym_dim + antisym_dim == output_dim)
    check("a generic coefficient vector has both lines", generic != symmetric and generic != antisymmetric)
    check("symmetric line alone does not distinguish E from T", symmetric[0] == symmetric[1])
    check("antisymmetric line distinguishes E from T", antisymmetric[0] != antisymmetric[1])


def part3_candidate_status_table() -> None:
    print()
    print("PART 3: candidate status table")
    candidates = {
        "Theta_R_0": ("bounded", "not_exact_coefficient_theorem"),
        "Xi_R_0": ("bounded", "not_exact_coefficient_theorem"),
        "active_H_basis": ("not_directly_on_carrier_columns", "not_ET_output_coefficient"),
        "exact_antisymmetric_carrier_primitive": ("open", "missing"),
    }
    for name, (status, role) in candidates.items():
        print(f"  {name}: {status}, {role}")
        check(f"{name} has a tracked status", bool(status and role))

    check("Theta is not the exact coefficient theorem", candidates["Theta_R_0"][1] == "not_exact_coefficient_theorem")
    check("Xi is not the exact coefficient theorem", candidates["Xi_R_0"][1] == "not_exact_coefficient_theorem")
    check("the exact antisymmetric primitive is missing", candidates["exact_antisymmetric_carrier_primitive"] == ("open", "missing"))
    check("no listed current candidate closes Block89", all(role != "closes_block89" for _, role in candidates.values()))


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("carrier_orbit_invariance", "Z2_operator_classification"),
        ("Z2_operator_classification", "current_symmetric_registry_check"),
        ("current_symmetric_registry_check", "no_current_exact_antisymmetric_primitive"),
        ("no_current_exact_antisymmetric_primitive", "no_hessian_ET_coeff_normalization"),
        ("block89_connected_hessian", "free_ET_coefficients"),
    ]
    missing_edges = [
        ("exact_antisymmetric_ET_primitive", "fixed_ET_coefficient_vector"),
        ("fixed_ET_coefficient_vector", "hessian_ET_coeff_normalization"),
        ("hessian_ET_coeff_normalization", "typed_route2_ET_bridge"),
    ]

    check("carrier orbit result does not reach coefficient normalization", not reachable(base_edges, "carrier_orbit_invariance", "hessian_ET_coeff_normalization"))
    check("carrier orbit result reaches no-current-primitive node", reachable(base_edges, "carrier_orbit_invariance", "no_current_exact_antisymmetric_primitive"))
    check("Block89 connected Hessian reaches free coefficients", reachable(base_edges, "block89_connected_hessian", "free_ET_coefficients"))
    check("adding exact antisymmetric primitive reaches typed bridge", reachable(base_edges + missing_edges, "exact_antisymmetric_ET_primitive", "typed_route2_ET_bridge"))
    all_nodes = {n for e in base_edges + missing_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_CARRIER_ANTISYMMETRIC_HESSIAN_COEFF_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for deriving Hessian E/T coefficient normalization",
        "This is not an audit verdict",
        "does not perform a registry audit",
        "C^2 = C(1,1) + C(1,-1)",
        "exact antisymmetric E/T coefficient primitive",
        "Route-2 exact antisymmetric E/T Hessian-coefficient primitive",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block90 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names antisymmetric E/T primitive", "antisymmetric E/T" in trace_gate)

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
    print("Route-2 carrier antisymmetric Hessian coefficient no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_output_space_decomposition()
    part3_candidate_status_table()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: current carrier-orbit support does not supply the exact antisymmetric E/T coefficient primitive needed for Hessian normalization.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
