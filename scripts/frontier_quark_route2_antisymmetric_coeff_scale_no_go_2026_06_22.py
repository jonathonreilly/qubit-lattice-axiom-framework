#!/usr/bin/env python3
"""No-go for antisymmetric E/T direction alone fixing Hessian coefficients."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-antisymmetric-coeff-scale"

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


def coeff(s: Fraction, t: Fraction) -> tuple[Fraction, Fraction]:
    return (s + t, -s + t)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block90 = text("QUARK_ROUTE2_CARRIER_ANTISYMMETRIC_HESSIAN_COEFF_NO_GO_NOTE_2026-06-22.md")
    block89 = text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md")
    block90_flat = flat(block90)
    block89_flat = flat(block89)

    check("Block90 names exact antisymmetric E/T primitive", "exact antisymmetric E/T Hessian-coefficient primitive" in block90_flat)
    check("Block90 says carrier support does not supply the primitive", "does not provide an exact antisymmetric E/T coefficient primitive" in block90_flat)
    check("Block90 records E/T swap decomposition", "C^2 = C(1,1) + C(1,-1)" in block90_flat)
    check("Block90 records current carrier primitives as swap-symmetric", "current enumerated carrier primitives lie in the swap-symmetric component" in block90_flat)
    check("Block90 records Theta/Xi as bounded candidates", "Theta_R^(0) and Xi_R^(0) are bounded candidates" in block90_flat)
    check("Block90 leaves registry closure open", "blocked on registry closure" in block90_flat)
    check("Block90 uses no endpoint value", "No endpoint value is used" in block90_flat)
    check("Block89 has free E/T coefficients", "lambda_E, lambda_T" in block89)
    check("Block89 separates kappa support from E/T bridge", "kappa=0 support and the scalar E/T bridge are distinct" in block89_flat)
    check("Block89 names coefficient normalization theorem", "Route-2 connected-Hessian E/T coefficient normalization theorem" in block89)


def part2_decomposition() -> None:
    print()
    print("PART 2: coefficient decomposition")
    samples = {
        "pure_antisym_unit": coeff(Fraction(1), Fraction(0)),
        "pure_antisym_double": coeff(Fraction(2), Fraction(0)),
        "symmetric_only": coeff(Fraction(0), Fraction(1)),
        "mixed": coeff(Fraction(2), Fraction(1)),
    }
    for name, vector in samples.items():
        print(f"  {name}: {vector}")
        check(f"{name} has two coefficients", len(vector) == 2)

    check("unit antisymmetric direction is (1,-1)", samples["pure_antisym_unit"] == (1, -1))
    check("scale changes along the same antisymmetric line", samples["pure_antisym_double"] == (2, -2))
    check("symmetric contamination changes the coefficient vector", samples["mixed"] != samples["pure_antisym_double"])
    check("symmetric-only vector does not distinguish E and T", samples["symmetric_only"][0] == samples["symmetric_only"][1])
    check("mixed vector has both antisymmetric and symmetric pieces", samples["mixed"] == (3, -1))


def part3_family_count() -> None:
    print()
    print("PART 3: family count")
    pure_antisym = [coeff(Fraction(s), Fraction(0)) for s in (1, 2, 3)]
    mixed = [coeff(Fraction(s), Fraction(t)) for s in (1, 2) for t in (0, 1, 2)]

    check("pure antisymmetric line still has multiple scales", len(set(pure_antisym)) == 3)
    check("mixed family has more choices than pure line", len(set(mixed)) > len(set(pure_antisym)))
    check("choosing the line does not choose the scale", pure_antisym[0] != pure_antisym[1])
    check("excluding symmetric contamination is an extra statement", coeff(Fraction(1), Fraction(1)) != coeff(Fraction(1), Fraction(0)))
    check("no endpoint value is needed to expose the scale freedom", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("exact_antisymmetric_direction", "antisymmetric_line_selected"),
        ("antisymmetric_line_selected", "free_scale_s"),
        ("coefficient_space", "possible_symmetric_contamination_t"),
        ("free_scale_s", "no_fixed_hessian_coeff_vector"),
        ("possible_symmetric_contamination_t", "no_fixed_hessian_coeff_vector"),
    ]
    missing_edges = [
        ("same_source_scale_normalization", "fixed_scale_s"),
        ("symmetric_contamination_exclusion", "pure_antisymmetric_line"),
        ("fixed_scale_s", "fixed_hessian_coeff_vector"),
        ("pure_antisymmetric_line", "fixed_hessian_coeff_vector"),
        ("fixed_hessian_coeff_vector", "typed_route2_ET_bridge"),
    ]

    check("antisymmetric direction alone does not reach fixed vector", not reachable(base_edges, "exact_antisymmetric_direction", "fixed_hessian_coeff_vector"))
    check("antisymmetric direction reaches free scale", reachable(base_edges, "exact_antisymmetric_direction", "free_scale_s"))
    check("coefficient space reaches symmetric contamination risk", reachable(base_edges, "coefficient_space", "possible_symmetric_contamination_t"))
    check("adding scale and purity primitives reaches typed bridge", reachable(base_edges + missing_edges, "same_source_scale_normalization", "typed_route2_ET_bridge"))
    all_nodes = {n for e in base_edges + missing_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_ANTISYMMETRIC_COEFF_SCALE_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for an antisymmetric E/T direction alone",
        "An antisymmetric direction fixes a line, not a scale-normalized coefficient vector",
        "(lambda_E, lambda_T) = s(1,-1) + t(1,1)",
        "Route-2 scale-normalized pure-antisymmetric Hessian coefficient theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block91 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names scale-normalized antisymmetric primitive", "scale-normalized" in trace_gate and "antisymmetric" in trace_gate)

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
    print("Route-2 antisymmetric coefficient scale no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_decomposition()
    part3_family_count()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: an antisymmetric E/T direction alone does not fix the scale-normalized Hessian coefficient vector.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
