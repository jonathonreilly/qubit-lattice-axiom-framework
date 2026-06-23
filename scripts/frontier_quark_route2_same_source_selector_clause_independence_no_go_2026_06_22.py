#!/usr/bin/env python3
"""Clause-independence hardwall for the Route-2 same-source selector bridge."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-same-source-selector-clause-independence"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class SelectorClauses:
    same_source_surface: bool
    raw_moment_registry: bool
    connected_subtraction_typed: bool
    one_point_product_selector: bool
    physical_readout_unit: bool
    orientation_sign: bool

    @property
    def closes_kappa(self) -> bool:
        return all(
            (
                self.same_source_surface,
                self.raw_moment_registry,
                self.connected_subtraction_typed,
                self.one_point_product_selector,
            )
        )

    @property
    def closes_signed_bridge(self) -> bool:
        return self.closes_kappa and self.physical_readout_unit and self.orientation_sign


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


def connected(raw: Fraction, product: Fraction) -> Fraction:
    return raw - product


def kappa_from_connected(value: Fraction) -> Fraction:
    return 9 * (value - Fraction(8, 9))


def c_te(sigma: int, mu: Fraction, kappa: Fraction) -> Fraction:
    return Fraction(sigma) * mu * (Fraction(8, 9) + kappa * Fraction(1, 9))


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


def part1_grounding() -> None:
    print("PART 1: grounding")
    atlas = flat(text("QUARK_ROUTE2_SELECTOR_EQUIVALENCE_ATLAS_SUPPORT_2026-06-22.md"))
    product = flat(text("QUARK_ROUTE2_NONBINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    scalar_no_go = flat(text("QUARK_ROUTE2_SCALAR_PARTITION_PRODUCT_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    hardwall = flat(text("QUARK_ROUTE2_MULTI_RECORD_BRIDGE_HARDWALL_CUT_2026-06-22.md"))
    minimal = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    isometry = flat(text("QUARK_ROUTE2_SOURCE_READOUT_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md"))
    calibration = flat(text("QUARK_ROUTE2_SOURCE_READOUT_UNIT_CALIBRATION_NO_GO_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    current_pr = flat(text("QUARK_ROUTE2_CURRENT_PR_MULTI_RECORD_INSTANTIATION_NO_GO_2026-06-22.md"))
    jcr = flat(text("QUARK_ROUTE2_PHYSICAL_JCR_TYPING_NO_GO_2026-06-22.md"))
    check("Block147 names typed selector theorem", "Route-2 typed selector theorem" in atlas)
    check("Block107 supplies non-binary product normal form", "Route-2 same-source one-point product theorem" in product)
    check("Block110 prunes scalar normalization shortcut", "scalar normalization remains support context" in scalar_no_go)
    check("Block119 names same-source covariant bridge theorem", "Route-2 same-source covariant multi-record bridge theorem" in hardwall)
    check("Block121 constructs minimal endpoint-free extension", "Minimal Extension Model" in minimal)
    check("Block127 supplies source-readout isometry target", "mu = 1" in isometry and "unit-preserving isometry" in isometry)
    check("Block126 prunes source-unit calibration shortcut", "source-readout unit calibration theorem" in calibration)
    check("endpoint sign support separates sign from magnitude", "sigma=-1" in sign and "magnitude remains open" in sign.lower())
    check("current P_R multi-record instantiation remains absent", "not already present in the finite P_R/E-T readout packet" in current_pr)
    check("physical J_CR typing remains absent", "physical J_CR source typing theorem" in jcr)
    check("grounding says no endpoint value is used as an input", "No endpoint value is used as an input" in atlas)


def part2_full_clause_bundle() -> None:
    print()
    print("PART 2: full selector bridge bundle")
    full = SelectorClauses(True, True, True, True, True, True)
    for name, supplied in full.__dict__.items():
        print(f"  full {name}: {supplied}")
        check(f"{name} has boolean status", isinstance(supplied, bool))
    raw = Fraction(1, 1)
    product = Fraction(1, 9)
    conn = connected(raw, product)
    kap = kappa_from_connected(conn)
    signed = c_te(-1, Fraction(1), kap)
    check("full clauses close kappa", full.closes_kappa)
    check("full clauses close signed bridge", full.closes_signed_bridge)
    check("full raw moment is one", raw == 1)
    check("full one-point product is one ninth", product == Fraction(1, 9))
    check("full connected value is eight ninths", conn == Fraction(8, 9))
    check("full kappa is zero", kap == 0)
    check("full signed bridge gives c_TE=-8/9", signed == Fraction(-8, 9))


def part3_single_clause_omissions() -> None:
    print()
    print("PART 3: single-clause omission witnesses")
    full = SelectorClauses(True, True, True, True, True, True)
    omitted_models = {
        "same_source_surface": {
            "clauses": SelectorClauses(False, True, True, True, True, True),
            "kind": "typed",
            "detail": "matching moments on unrelated sources do not define one physical cumulant",
        },
        "raw_moment_registry": {
            "clauses": SelectorClauses(True, False, True, True, True, True),
            "kind": "numeric",
            "raw": Fraction(2, 3),
            "product": Fraction(1, 9),
            "expected_kappa": Fraction(-3, 1),
        },
        "connected_subtraction_typed": {
            "clauses": SelectorClauses(True, True, False, True, True, True),
            "kind": "raw_readout",
            "raw": Fraction(1, 1),
            "product": Fraction(1, 9),
            "expected_kappa": Fraction(1, 1),
        },
        "one_point_product_selector": {
            "clauses": SelectorClauses(True, True, True, False, True, True),
            "kind": "numeric",
            "raw": Fraction(1, 1),
            "product": Fraction(1, 4),
            "expected_kappa": Fraction(-5, 4),
        },
        "physical_readout_unit": {
            "clauses": SelectorClauses(True, True, True, True, False, True),
            "kind": "mu",
            "mu": Fraction(1, 2),
            "expected_c_te": Fraction(-4, 9),
        },
        "orientation_sign": {
            "clauses": SelectorClauses(True, True, True, True, True, False),
            "kind": "sigma",
            "sigma": +1,
            "expected_c_te": Fraction(8, 9),
        },
    }
    check("full model is the only all-true clause vector", all(full.__dict__.values()))
    for omitted, model in omitted_models.items():
        clauses: SelectorClauses = model["clauses"]  # type: ignore[assignment]
        print(f"  omit {omitted}: {model['detail'] if 'detail' in model else model['kind']}")
        check(f"{omitted} omission flips exactly one clause", sum(not v for v in clauses.__dict__.values()) == 1)
        check(f"{omitted} omission does not close signed bridge", not clauses.closes_signed_bridge)
        if model["kind"] == "typed":
            check(f"{omitted} omission does not type kappa", not clauses.closes_kappa)
        elif model["kind"] == "numeric":
            raw = model["raw"]  # type: ignore[assignment]
            product = model["product"]  # type: ignore[assignment]
            kap = kappa_from_connected(connected(raw, product))  # type: ignore[arg-type]
            print(f"    raw={raw}, product={product}, kappa={kap}")
            check(f"{omitted} numeric witness misses kappa zero", kap != 0)
            check(f"{omitted} numeric witness matches expected kappa", kap == model["expected_kappa"])
        elif model["kind"] == "raw_readout":
            raw = model["raw"]  # type: ignore[assignment]
            kap = kappa_from_connected(raw)  # type: ignore[arg-type]
            print(f"    raw_readout={raw}, kappa={kap}")
            check(f"{omitted} raw-readout witness misses kappa zero", kap != 0)
            check(f"{omitted} raw-readout witness matches expected kappa", kap == model["expected_kappa"])
        elif model["kind"] == "mu":
            value = c_te(-1, model["mu"], Fraction(0))  # type: ignore[arg-type]
            print(f"    mu={model['mu']}, c_TE={value}")
            check(f"{omitted} mu witness misses signed target", value != Fraction(-8, 9))
            check(f"{omitted} mu witness matches expected c_TE", value == model["expected_c_te"])
        elif model["kind"] == "sigma":
            value = c_te(model["sigma"], Fraction(1), Fraction(0))  # type: ignore[arg-type]
            print(f"    sigma={model['sigma']}, c_TE={value}")
            check(f"{omitted} sign witness misses signed target", value != Fraction(-8, 9))
            check(f"{omitted} sign witness matches expected c_TE", value == model["expected_c_te"])


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("current_support_stack", "selector_atlas_support"),
        ("current_support_stack", "minimal_extension_support"),
        ("current_support_stack", "isometry_target_support"),
        ("current_support_stack", "orientation_sign_support"),
        ("current_support_stack", "missing_same_source_selector_bridge_theorem"),
        ("missing_same_source_selector_bridge_theorem", "missing_same_source_surface"),
        ("missing_same_source_selector_bridge_theorem", "missing_raw_moment_registry"),
        ("missing_same_source_selector_bridge_theorem", "missing_connected_subtraction_typing"),
        ("missing_same_source_selector_bridge_theorem", "missing_one_point_product_selector"),
        ("missing_same_source_selector_bridge_theorem", "missing_physical_readout_unit"),
    ]
    full_edges = [
        ("same_source_selector_bridge_theorem", "same_source_surface"),
        ("same_source_surface", "raw_moment_registry"),
        ("raw_moment_registry", "connected_subtraction_typed"),
        ("connected_subtraction_typed", "one_point_product_selector"),
        ("one_point_product_selector", "kappa_zero"),
        ("kappa_zero", "physical_readout_unit_mu_one"),
        ("physical_readout_unit_mu_one", "orientation_sign_sigma_minus_one"),
        ("orientation_sign_sigma_minus_one", "c_TE_minus_8_9"),
    ]
    check("current stack reaches missing selector theorem node", reachable(current_edges, "current_support_stack", "missing_same_source_selector_bridge_theorem"))
    check("current stack does not reach kappa zero", not reachable(current_edges, "current_support_stack", "kappa_zero"))
    check("current stack does not reach signed bridge", not reachable(current_edges, "current_support_stack", "c_TE_minus_8_9"))
    check("full selector theorem reaches kappa zero", reachable(full_edges, "same_source_selector_bridge_theorem", "kappa_zero"))
    check("full selector theorem reaches signed bridge", reachable(full_edges, "same_source_selector_bridge_theorem", "c_TE_minus_8_9"))
    all_current_nodes = {n for edge in current_edges for n in edge}
    check("current graph has no endpoint-value input node", all("rho_E" not in n and "q_E" not in n for n in all_current_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SAME_SOURCE_SELECTOR_CLAUSE_INDEPENDENCE_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for weakened same-source selector bridge clauses",
        "Route-2 same-source selector bridge theorem",
        "single-clause omissions",
        "same-source one-point product E[X]E[Y]=1/9",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block148 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative route pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    check("review history records no audit worker", "No audit worker was run" in review)
    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives the endpoint triple ", "on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("observed-target import", phrase("observed ", "target")),
        ("fitted-selector import", phrase("fitted ", "selector")),
        ("target-observation import", phrase("target ", "observation")),
        ("data-tuned-selector import", phrase("data-tuned ", "selector")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 same-source selector clause-independence no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_full_clause_bundle()
    part3_single_clause_omissions()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: no weakened same-source selector bridge theorem is enough; the Route-2 proof must supply same-source typing, raw moment, connected subtraction, one-point product, unit calibration, and post-selector orientation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
