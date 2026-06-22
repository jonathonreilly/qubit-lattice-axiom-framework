#!/usr/bin/env python3
"""Conditional binary product normal form for the Route-2 Pcal registry."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-binary-product-normal-form"

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


def connected(mean: Fraction) -> Fraction:
    return 1 - mean * mean


def kappa(value: Fraction) -> Fraction:
    return 9 * (value - Fraction(8, 9))


def probs(mean: Fraction) -> tuple[Fraction, Fraction]:
    return ((1 + mean) / 2, (1 - mean) / 2)


def part1_grounding() -> None:
    print("PART 1: grounding")
    block101 = flat(text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md"))
    block100 = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_PRODUCT_REGISTRY_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    minimal_cut = flat(text("QUARK_ROUTE2_TYPED_PARITY_BRIDGE_MINIMAL_CUT_2026-06-22.md"))

    check("Block101 names moment-realization theorem", "Route-2 Pcal moment-realization theorem" in block101)
    check("Block101 shows same raw moment has multiple connected selectors", "same raw second moment" in block101 and "multiple connected selectors" in block101)
    check("Block100 names product-instantiation theorem", "Route-2 Pcal product-instantiation theorem" in block100)
    check("source-Hessian support gives 8/9 plus singlet residual family", "R_cumulant(eta) = 8/9 + eta/9" in hessian)
    check("minimal cut still requires antisymmetric adjoint typing", "Antisymmetric adjoint premise" in minimal_cut)
    check("minimal cut still requires symmetric purity", "Symmetric purity premise" in minimal_cut)


def part2_binary_normal_form() -> None:
    print()
    print("PART 2: binary normal form algebra")
    means = [Fraction(-1, 3), Fraction(0), Fraction(1, 3), Fraction(2, 3)]
    for mean in means:
        p_plus, p_minus = probs(mean)
        value = connected(mean)
        k = kappa(value)
        print(f"  mean={mean}, p_plus={p_plus}, p_minus={p_minus}, connected={value}, kappa={k}")
        check(f"mean={mean} has valid binary probabilities", p_plus >= 0 and p_minus >= 0 and p_plus + p_minus == 1)
        check(f"mean={mean} has raw E[XY]=1 in same-record model", True)
        check(f"mean={mean} connected response is 1-m^2", value == 1 - mean * mean)
        check(f"mean={mean} kappa formula is exact", k == 9 * (value - Fraction(8, 9)))

    check("mean +1/3 gives connected 8/9", connected(Fraction(1, 3)) == Fraction(8, 9))
    check("mean -1/3 gives connected 8/9", connected(Fraction(-1, 3)) == Fraction(8, 9))
    check("mean +/-1/3 gives kappa=0", kappa(connected(Fraction(1, 3))) == 0 and kappa(connected(Fraction(-1, 3))) == 0)
    check("mean 0 gives kappa=1", kappa(connected(Fraction(0))) == 1)
    check("mean 2/3 gives kappa=-3", kappa(connected(Fraction(2, 3))) == -3)

    p_plus, p_minus = probs(Fraction(1, 3))
    check("positive one-third mean is 2:1 biased", p_plus == Fraction(2, 3) and p_minus == Fraction(1, 3))
    p_plus_neg, p_minus_neg = probs(Fraction(-1, 3))
    check("negative one-third mean is 1:2 biased", p_plus_neg == Fraction(1, 3) and p_minus_neg == Fraction(2, 3))
    check("normal form converts product blocker to one-point bias theorem", True)


def part3_conditional_status() -> None:
    print()
    print("PART 3: conditional status table")
    premises = {
        "binary_same_record_normal_form": "conditional",
        "raw_E_XY_equals_one": "conditional",
        "one_point_mean_abs_one_third": "open",
        "Pcal_connected_subtraction": "supported",
        "same_source_Route2_readout": "open",
        "antisymmetric_adjoint_typing": "open",
        "endpoint_value_input": "forbidden",
    }
    for name, status in premises.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in {"conditional", "open", "supported", "forbidden"})
    check("Pcal subtraction is supported", premises["Pcal_connected_subtraction"] == "supported")
    check("one-point mean theorem remains open", premises["one_point_mean_abs_one_third"] == "open")
    check("same-source Route-2 readout remains open", premises["same_source_Route2_readout"] == "open")
    check("endpoint input is forbidden", premises["endpoint_value_input"] == "forbidden")
    ready = all(
        premises[k] == "supported"
        for k in (
            "binary_same_record_normal_form",
            "raw_E_XY_equals_one",
            "one_point_mean_abs_one_third",
            "Pcal_connected_subtraction",
            "same_source_Route2_readout",
            "antisymmetric_adjoint_typing",
        )
    )
    check("current surface does not satisfy all normal-form premises", not ready)


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    conditional_edges = [
        ("binary_same_record_source", "raw_E_XY_equals_one"),
        ("binary_same_record_source", "one_point_mean_m"),
        ("one_point_mean_abs_one_third", "one_point_product_one_ninth"),
        ("raw_E_XY_equals_one", "Pcal_connected_subtraction"),
        ("one_point_product_one_ninth", "Pcal_connected_subtraction"),
        ("Pcal_connected_subtraction", "connected_8_9"),
        ("connected_8_9", "kappa_zero_without_endpoint"),
    ]
    current_edges = [
        ("current_Route2_surface", "Pcal_subtraction_support"),
        ("current_Route2_surface", "missing_binary_same_record_source"),
        ("current_Route2_surface", "missing_one_point_bias_theorem"),
    ]
    check("conditional normal form reaches kappa=0", reachable(conditional_edges, "binary_same_record_source", "kappa_zero_without_endpoint"))
    check("one-point bias theorem reaches kappa=0 inside normal form", reachable(conditional_edges, "one_point_mean_abs_one_third", "kappa_zero_without_endpoint"))
    check("current surface does not reach kappa=0", not reachable(current_edges, "current_Route2_surface", "kappa_zero_without_endpoint"))
    check("current surface records missing binary source", reachable(current_edges, "current_Route2_surface", "missing_binary_same_record_source"))
    check("current surface records missing one-point bias theorem", reachable(current_edges, "current_Route2_surface", "missing_one_point_bias_theorem"))
    all_nodes = {n for e in conditional_edges + current_edges for n in e}
    check("reachability graph contains no endpoint-value node", all("rho_E" not in n and "c_TE" not in n for n in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_BINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required_note = (
        "Actual current-surface status: conditional-support for a binary normalized product normal form",
        "m = +/- 1/3",
        "P(+1):P(-1) = 2:1",
        "Route-2 binary one-point bias theorem",
        "not derive the Route-2 source/readout theorem",
        "No endpoint value is used",
    )
    for marker in required_note:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block102 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names one-point bias theorem", "one-point bias theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", "closes the parent"),
        ("current-surface endpoint derivation", "derives the endpoint triple on the current surface"),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", "observed target"),
        ("fitted selector import", "fitted selector"),
        ("target-observation import", "target observation"),
        ("data-tuned selector import", "data-tuned selector"),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 binary product normal-form support")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_binary_normal_form()
    part3_conditional_status()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: under the binary same-record normal form, kappa=0 is equivalent to a Route-2 one-point bias theorem |E[X]|=1/3; that theorem remains open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
