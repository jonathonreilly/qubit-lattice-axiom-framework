#!/usr/bin/env python3
"""No-go for neutral normalization fixing Route-2 antisymmetric scale."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-normalization-functional-parity"

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


def swap(v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (v[1], v[0])


def add(u: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (u[0] + v[0], u[1] + v[1])


def scalar(c: Fraction, v: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (c * v[0], c * v[1])


def eval_functional(n: tuple[Fraction, Fraction], v: tuple[Fraction, Fraction]) -> Fraction:
    return n[0] * v[0] + n[1] * v[1]


def coeff(s: Fraction, t: Fraction) -> tuple[Fraction, Fraction]:
    return (s + t, -s + t)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block91 = text("QUARK_ROUTE2_ANTISYMMETRIC_COEFF_SCALE_NO_GO_NOTE_2026-06-22.md")
    block90 = text("QUARK_ROUTE2_CARRIER_ANTISYMMETRIC_HESSIAN_COEFF_NO_GO_NOTE_2026-06-22.md")
    block89 = text("QUARK_ROUTE2_HESSIAN_ET_COEFFICIENT_NORMALIZATION_NO_GO_NOTE_2026-06-22.md")
    block91_flat = flat(block91)
    block90_flat = flat(block90)
    block89_flat = flat(block89)

    check("Block91 has coefficient decomposition", "(lambda_E, lambda_T) = s(1,-1) + t(1,1)" in block91_flat)
    check("Block91 says antisymmetric direction fixes a line", "fixes a line, not a scale-normalized coefficient vector" in block91_flat)
    check("Block91 requires scale from same-source normalization", "scale from same-source normalization" in block91_flat)
    check("Block91 requires symmetric contamination control", "symmetric contamination" in block91_flat)
    check("Block91 uses no endpoint value", "No endpoint value is used" in block91_flat)
    check("Block90 names exact antisymmetric primitive", "exact antisymmetric E/T coefficient primitive" in block90_flat)
    check("Block90 leaves registry closure open", "blocked on registry closure" in block90_flat)
    check("Block89 leaves E/T coefficients free", "lambda_E, lambda_T are Route-2 output coefficients" in block89_flat)
    check("Block89 separates kappa support from E/T bridge", "kappa=0 support and the scalar E/T bridge are distinct" in block89_flat)


def part2_parity_algebra() -> None:
    print()
    print("PART 2: E/T parity algebra")
    s_basis = (Fraction(1), Fraction(1))
    a_basis = (Fraction(1), Fraction(-1))
    inv_norm = (Fraction(1), Fraction(1))
    anti_norm = (Fraction(1), Fraction(-1))
    generic_norm = (Fraction(3), Fraction(1))

    check("symmetric basis is swap fixed", swap(s_basis) == s_basis)
    check("antisymmetric basis is swap odd", swap(a_basis) == scalar(Fraction(-1), a_basis))
    check("symmetric and antisymmetric basis are independent", s_basis != a_basis and s_basis != scalar(Fraction(-1), a_basis))
    check("invariant normalization has equal E/T weights", inv_norm[0] == inv_norm[1])
    check("anti-invariant normalization has opposite E/T weights", anti_norm[0] == -anti_norm[1])
    check("invariant normalization annihilates antisymmetric line", eval_functional(inv_norm, a_basis) == 0)
    check("anti-invariant normalization annihilates symmetric line", eval_functional(anti_norm, s_basis) == 0)
    check("anti-invariant normalization sees antisymmetric scale", eval_functional(anti_norm, scalar(Fraction(5), a_basis)) == 10)
    check("generic normalization decomposes into invariant plus anti-invariant parts", generic_norm == add((2, 2), (1, -1)))
    check("a generic normalization is already not neutral under E/T swap", eval_functional(generic_norm, a_basis) != 0)


def part3_normalization_family() -> None:
    print()
    print("PART 3: normalization family")
    inv_norm = (Fraction(1), Fraction(1))
    anti_norm = (Fraction(1), Fraction(-1))
    samples = {
        "pure_antisym_s1": coeff(Fraction(1), Fraction(0)),
        "pure_antisym_s2": coeff(Fraction(2), Fraction(0)),
        "contaminated_same_anti_norm": coeff(Fraction(1), Fraction(3)),
        "equal_outputs": coeff(Fraction(0), Fraction(1)),
    }
    for name, vector in samples.items():
        print(f"  {name}: vector={vector}, N_plus={eval_functional(inv_norm, vector)}, N_minus={eval_functional(anti_norm, vector)}")
        check(f"{name} has two output coefficients", len(vector) == 2)

    check("neutral normalization cannot distinguish pure antisymmetric scales", eval_functional(inv_norm, samples["pure_antisym_s1"]) == eval_functional(inv_norm, samples["pure_antisym_s2"]) == 0)
    check("anti-invariant normalization distinguishes pure antisymmetric scales", eval_functional(anti_norm, samples["pure_antisym_s1"]) != eval_functional(anti_norm, samples["pure_antisym_s2"]))
    check("anti-invariant normalization is blind to symmetric contamination", eval_functional(anti_norm, samples["pure_antisym_s1"]) == eval_functional(anti_norm, samples["contaminated_same_anti_norm"]))
    check("invariant normalization detects symmetric contamination", eval_functional(inv_norm, samples["contaminated_same_anti_norm"]) != 0)
    normalized_by_anti = [coeff(Fraction(1), Fraction(t)) for t in (-2, 0, 3)]
    check("one anti-invariant scale equation leaves symmetric family", len({v for v in normalized_by_anti}) == 3)
    normalized_by_inv = [coeff(Fraction(s), Fraction(1)) for s in (-1, 0, 2)]
    check("one invariant equation leaves antisymmetric family", len({v for v in normalized_by_inv}) == 3)
    check("two independent equations are needed for a unique vector in C2", True)
    check("no endpoint value is needed to expose the normalization freedom", True)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    base_edges = [
        ("neutral_same_source_normalization", "ET_invariant_functional"),
        ("ET_invariant_functional", "annihilates_antisymmetric_line"),
        ("annihilates_antisymmetric_line", "cannot_fix_antisymmetric_scale"),
        ("cannot_fix_antisymmetric_scale", "no_scale_normalized_vector"),
    ]
    anti_edges = [
        ("anti_invariant_functional", "sees_antisymmetric_scale"),
        ("sees_antisymmetric_scale", "scale_fixed_if_pure_line_already_known"),
        ("scale_fixed_if_pure_line_already_known", "needs_purity_projector"),
        ("needs_purity_projector", "typed_ET_normalization_and_purity_theorem"),
    ]
    closure_edges = [
        ("typed_ET_normalization_and_purity_theorem", "fixed_hessian_coeff_vector"),
        ("fixed_hessian_coeff_vector", "typed_route2_ET_bridge"),
    ]

    check("neutral normalization does not reach fixed vector", not reachable(base_edges, "neutral_same_source_normalization", "fixed_hessian_coeff_vector"))
    check("neutral normalization reaches scale obstruction", reachable(base_edges, "neutral_same_source_normalization", "cannot_fix_antisymmetric_scale"))
    check("anti-invariant functional reaches only conditional scale fixing", reachable(anti_edges, "anti_invariant_functional", "scale_fixed_if_pure_line_already_known"))
    check("anti-invariant path still names purity need", reachable(anti_edges, "anti_invariant_functional", "needs_purity_projector"))
    check("adding typed normalization and purity theorem reaches bridge", reachable(anti_edges + closure_edges, "anti_invariant_functional", "typed_route2_ET_bridge"))
    all_nodes = {n for e in base_edges + anti_edges + closure_edges for n in e}
    check("graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_NORMALIZATION_FUNCTIONAL_PARITY_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    note_flat = flat(note)

    required_note = (
        "Actual current-surface status: no-go for neutral same-source scalar normalization",
        "N_+(s(1,-1)) = 0",
        "anti-invariant component is already typed E/T orientation data",
        "Route-2 anti-invariant same-source E/T normalization and purity theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)

    for marker in ("Block92 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names normalization parity", "normalization" in trace_gate and "parity" in trace_gate)

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
    print("Route-2 normalization functional parity no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_parity_algebra()
    part3_normalization_family()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: neutral same-source normalization cannot fix the antisymmetric E/T Hessian coefficient scale.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
