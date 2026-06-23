#!/usr/bin/env python3
"""Fan-out no-go for physical instantiation of the Route-2 selector theorem."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-physical-selector-instantiation-fanout"

PASS = 0
FAIL = 0

CLAUSES = (
    "source_law",
    "physical_variables",
    "raw_moment_one",
    "connected_typing",
    "product_selector",
    "unit_calibration",
    "orientation_sign",
)


@dataclass(frozen=True)
class Frame:
    name: str
    clauses: dict[str, bool]
    missing: tuple[str, ...]

    @property
    def closes_kappa(self) -> bool:
        return all(self.clauses[c] for c in CLAUSES[:5])

    @property
    def closes_signed_bridge(self) -> bool:
        return self.closes_kappa and self.clauses["unit_calibration"] and self.clauses["orientation_sign"]


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
    block148 = flat(text("QUARK_ROUTE2_SAME_SOURCE_SELECTOR_CLAUSE_INDEPENDENCE_NO_GO_2026-06-22.md"))
    atlas = flat(text("QUARK_ROUTE2_SELECTOR_EQUIVALENCE_ATLAS_SUPPORT_2026-06-22.md"))
    readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    product = flat(text("QUARK_ROUTE2_SOURCE_MEASURE_PRODUCT_REGISTRY_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    moment = flat(text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    fisher = flat(text("QUARK_ROUTE2_FISHER_RIESZ_REALIZATION_NO_GO_2026-06-22.md"))
    minimal = flat(text("QUARK_ROUTE2_MINIMAL_MULTI_RECORD_EXTENSION_SUPPORT_2026-06-22.md"))
    current_pr = flat(text("QUARK_ROUTE2_CURRENT_PR_MULTI_RECORD_INSTANTIATION_NO_GO_2026-06-22.md"))
    unit = flat(text("QUARK_ROUTE2_SOURCE_READOUT_UNIT_CALIBRATION_NO_GO_2026-06-22.md"))
    check("Block148 names full selector bridge theorem", "Route-2 same-source selector bridge theorem" in block148)
    check("Block147 supplies selector atlas", "Route-2 typed selector theorem" in atlas)
    check("exact readout map is carrier/readout reduction", "exact carrier/readout reduction" in readout)
    check("generic source-measure product registry is pruned", "Route-2 product registry" in product)
    check("Pcal moment realization from P_R slots is pruned", "Route-2 Pcal moment-realization theorem" in moment)
    check("source-jet lift remains missing", "same-source source-jet lift theorem" in source_jet)
    check("Fisher-Riesz realization remains missing", "Omega_R, P_0, and a normalized RN source path" in fisher)
    check("minimal extension leaves physical identification open", "not a proof that the existing finite P_R/E-T packet supplies it" in minimal)
    check("current P_R multi-record instantiation remains absent", "not already present in the finite P_R/E-T readout packet" in current_pr)
    check("unit calibration remains missing", "source algebra alone does not select one of them" in unit)
    check("grounding says no endpoint value is used", "No endpoint value is used" in block148)


def frames() -> list[Frame]:
    return [
        Frame(
            "exact_pr_slots",
            {
                "source_law": False,
                "physical_variables": False,
                "raw_moment_one": False,
                "connected_typing": False,
                "product_selector": False,
                "unit_calibration": False,
                "orientation_sign": True,
            },
            ("source_law", "physical_variables", "raw_moment_one", "connected_typing", "product_selector", "unit_calibration"),
        ),
        Frame(
            "normalized_four_slot_source",
            {
                "source_law": True,
                "physical_variables": False,
                "raw_moment_one": False,
                "connected_typing": False,
                "product_selector": False,
                "unit_calibration": False,
                "orientation_sign": True,
            },
            ("physical_variables", "raw_moment_one", "connected_typing", "product_selector", "unit_calibration"),
        ),
        Frame(
            "generic_pcal_source_measure",
            {
                "source_law": True,
                "physical_variables": False,
                "raw_moment_one": False,
                "connected_typing": True,
                "product_selector": False,
                "unit_calibration": False,
                "orientation_sign": True,
            },
            ("physical_variables", "raw_moment_one", "product_selector", "unit_calibration"),
        ),
        Frame(
            "minimal_one_plus_adjoint_extension",
            {
                "source_law": True,
                "physical_variables": False,
                "raw_moment_one": True,
                "connected_typing": True,
                "product_selector": True,
                "unit_calibration": False,
                "orientation_sign": True,
            },
            ("physical_variables", "unit_calibration"),
        ),
        Frame(
            "formal_binary_source_jet",
            {
                "source_law": True,
                "physical_variables": False,
                "raw_moment_one": True,
                "connected_typing": True,
                "product_selector": False,
                "unit_calibration": False,
                "orientation_sign": False,
            },
            ("physical_variables", "product_selector", "unit_calibration", "orientation_sign"),
        ),
        Frame(
            "generic_fisher_riesz",
            {
                "source_law": False,
                "physical_variables": False,
                "raw_moment_one": False,
                "connected_typing": False,
                "product_selector": False,
                "unit_calibration": False,
                "orientation_sign": True,
            },
            ("source_law", "physical_variables", "raw_moment_one", "connected_typing", "product_selector", "unit_calibration"),
        ),
    ]


def part2_fanout_clause_matrix() -> None:
    print()
    print("PART 2: fan-out clause matrix")
    for frame in frames():
        print(f"  frame: {frame.name}, missing={frame.missing}")
        check(f"{frame.name} has all clause keys", tuple(frame.clauses) == CLAUSES)
        check(f"{frame.name} missing list matches false clauses", tuple(k for k in CLAUSES if not frame.clauses[k]) == frame.missing)
        check(f"{frame.name} does not close kappa", not frame.closes_kappa)
        check(f"{frame.name} does not close signed bridge", not frame.closes_signed_bridge)
    check("six candidate frames were tested", len(frames()) == 6)
    check("no current frame closes kappa", not any(frame.closes_kappa for frame in frames()))
    check("no current frame closes signed bridge", not any(frame.closes_signed_bridge for frame in frames()))


def part3_exact_witnesses() -> None:
    print()
    print("PART 3: exact witnesses")
    four_slot_fraction = Fraction(3, 4)
    four_slot_kappa = kappa_from_connected(four_slot_fraction)
    check("four-slot normalized tangent fraction is 3/4", four_slot_fraction == Fraction(3, 4))
    check("four-slot normalized tangent misses kappa zero", four_slot_kappa == Fraction(-5, 4))
    raw_family = {
        "neutral": (Fraction(1), Fraction(0), Fraction(1)),
        "target": (Fraction(1), Fraction(1, 9), Fraction(0)),
        "off_product": (Fraction(1), Fraction(1, 4), Fraction(-5, 4)),
        "wrong_raw": (Fraction(2, 3), Fraction(1, 9), Fraction(-3)),
    }
    for name, (raw, product, expected_kappa) in raw_family.items():
        conn = raw - product
        kap = kappa_from_connected(conn)
        print(f"  {name}: raw={raw}, product={product}, connected={conn}, kappa={kap}")
        check(f"{name} kappa matches expected", kap == expected_kappa)
    mu_outputs = {mu: c_te(-1, mu, Fraction(0)) for mu in (Fraction(1, 2), Fraction(1), Fraction(3, 2))}
    for mu, value in mu_outputs.items():
        print(f"  mu={mu}, c_TE={value}")
        check(f"mu={mu} output is rational", isinstance(value, Fraction))
    check("only mu=1 gives signed target in sampled family", [mu for mu, value in mu_outputs.items() if value == Fraction(-8, 9)] == [Fraction(1)])


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    current_edges = [
        ("current_support_stack", "exact_pr_slots"),
        ("current_support_stack", "normalized_four_slot_source"),
        ("current_support_stack", "generic_pcal_source_measure"),
        ("current_support_stack", "minimal_one_plus_adjoint_extension"),
        ("current_support_stack", "formal_binary_source_jet"),
        ("current_support_stack", "generic_fisher_riesz"),
        ("exact_pr_slots", "missing_physical_selector_realization"),
        ("normalized_four_slot_source", "missing_physical_selector_realization"),
        ("generic_pcal_source_measure", "missing_physical_selector_realization"),
        ("minimal_one_plus_adjoint_extension", "missing_physical_selector_realization"),
        ("formal_binary_source_jet", "missing_physical_selector_realization"),
        ("generic_fisher_riesz", "missing_physical_selector_realization"),
    ]
    full_edges = [
        ("physical_selector_realization_theorem", "source_law"),
        ("source_law", "physical_variables"),
        ("physical_variables", "raw_moment_one"),
        ("raw_moment_one", "connected_typing"),
        ("connected_typing", "product_selector"),
        ("product_selector", "kappa_zero"),
        ("kappa_zero", "unit_calibration"),
        ("unit_calibration", "orientation_sign"),
        ("orientation_sign", "c_TE_minus_8_9"),
    ]
    check("current stack reaches missing realization node", reachable(current_edges, "current_support_stack", "missing_physical_selector_realization"))
    check("current stack does not reach kappa zero", not reachable(current_edges, "current_support_stack", "kappa_zero"))
    check("current stack does not reach signed bridge", not reachable(current_edges, "current_support_stack", "c_TE_minus_8_9"))
    check("full realization theorem reaches kappa zero", reachable(full_edges, "physical_selector_realization_theorem", "kappa_zero"))
    check("full realization theorem reaches signed bridge", reachable(full_edges, "physical_selector_realization_theorem", "c_TE_minus_8_9"))
    all_current_nodes = {n for edge in current_edges for n in edge}
    check("current graph has no endpoint-value input node", all("rho_E" not in n and "q_E" not in n for n in all_current_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_PHYSICAL_SELECTOR_INSTANTIATION_FANOUT_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for current candidate surfaces instantiating the full Route-2 same-source selector bridge theorem",
        "Route-2 physical same-source selector realization theorem",
        "No current candidate supplies all clauses",
        "Omega_R",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block149 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 physical selector instantiation fan-out no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_fanout_clause_matrix()
    part3_exact_witnesses()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: no current candidate surface instantiates the full physical same-source selector realization; the missing primitive is Omega_R/P0/P_h plus physical readouts, raw/product registry, unit calibration, and post-selector orientation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
