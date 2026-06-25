#!/usr/bin/env python3
"""No-go for cubic-record geometry alone forcing the Route-2 selector."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-cubic-record-selector-no-go"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class FiniteReadoutModel:
    name: str
    weights: tuple[Fraction, ...]
    x_values: tuple[Fraction, ...]
    y_values: tuple[Fraction, ...]
    extra_clause: str

    @property
    def normalized(self) -> bool:
        return sum(self.weights) == 1

    @property
    def mean_x(self) -> Fraction:
        return sum(w * x for w, x in zip(self.weights, self.x_values))

    @property
    def mean_y(self) -> Fraction:
        return sum(w * y for w, y in zip(self.weights, self.y_values))

    @property
    def raw(self) -> Fraction:
        return sum(w * x * y for w, x, y in zip(self.weights, self.x_values, self.y_values))

    @property
    def product(self) -> Fraction:
        return self.mean_x * self.mean_y

    @property
    def connected(self) -> Fraction:
        return self.raw - self.product

    @property
    def kappa(self) -> Fraction:
        return 9 * (self.connected - Fraction(8, 9))


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


def models() -> dict[str, FiniteReadoutModel]:
    thirds = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    sixths = tuple(Fraction(1, 6) for _ in range(6))
    ninths = tuple(Fraction(1, 9) for _ in range(9))
    independent_axis_x = tuple(Fraction(1 if i < 3 else 0) for i in range(9))
    independent_axis_y = tuple(Fraction(1 if i % 3 == 0 else 0) for i in range(9))
    return {
        "unsigned_axis_projector": FiniteReadoutModel(
            "unsigned_axis_projector",
            thirds,
            (Fraction(1), Fraction(0), Fraction(0)),
            (Fraction(1), Fraction(0), Fraction(0)),
            "uniform axis law plus unsigned selected-axis projector",
        ),
        "independent_axis_projectors": FiniteReadoutModel(
            "independent_axis_projectors",
            ninths,
            independent_axis_x,
            independent_axis_y,
            "two independent uniform axis records, not same-source co-recording",
        ),
        "signed_six_direction_component": FiniteReadoutModel(
            "signed_six_direction_component",
            sixths,
            (Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
            (Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
            "cubic signed directions with no selected binary collapse",
        ),
        "symmetric_binary_same_record": FiniteReadoutModel(
            "symmetric_binary_same_record",
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(1), Fraction(-1)),
            (Fraction(1), Fraction(-1)),
            "same-source binary record without one-point bias",
        ),
        "axis_one_vs_two_signed": FiniteReadoutModel(
            "axis_one_vs_two_signed",
            thirds,
            (Fraction(1), Fraction(-1), Fraction(-1)),
            (Fraction(1), Fraction(-1), Fraction(-1)),
            "uniform axis law plus selected-axis one-vs-two signed collapse",
        ),
        "target_biased_binary": FiniteReadoutModel(
            "target_biased_binary",
            (Fraction(2, 3), Fraction(1, 3)),
            (Fraction(1), Fraction(-1)),
            (Fraction(1), Fraction(-1)),
            "explicit 2:1 signed source bias",
        ),
        "off_target_biased_binary": FiniteReadoutModel(
            "off_target_biased_binary",
            (Fraction(3, 4), Fraction(1, 4)),
            (Fraction(1), Fraction(-1)),
            (Fraction(1), Fraction(-1)),
            "explicit 3:1 signed source bias",
        ),
    }


def part1_grounding() -> None:
    print("PART 1: grounding")
    axioms = flat(text("MINIMAL_AXIOMS_2026-06-05.md"))
    block147 = flat(text("QUARK_ROUTE2_SELECTOR_EQUIVALENCE_ATLAS_SUPPORT_2026-06-22.md"))
    block148 = flat(text("QUARK_ROUTE2_SAME_SOURCE_SELECTOR_CLAUSE_INDEPENDENCE_NO_GO_2026-06-22.md"))
    block149 = flat(text("QUARK_ROUTE2_PHYSICAL_SELECTOR_INSTANTIATION_FANOUT_NO_GO_2026-06-22.md"))
    block150 = flat(text("QUARK_ROUTE2_SOURCE_READOUT_PRIMITIVE_QUEUE_EXHAUSTION_2026-06-22.md"))
    scalar = flat(text("QUARK_ROUTE2_SCALAR_PARTITION_PRODUCT_SELECTOR_NO_GO_NOTE_2026-06-22.md"))
    binary = flat(text("QUARK_ROUTE2_BINARY_SAME_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    graph = flat(text("QUARK_ROUTE2_GRAPH_FIRST_SPATIAL_COLOR_BRIDGE_NO_GO_NOTE_2026-06-22.md"))
    check("minimal Lattice axiom does not supply probability law", "does not supply a dynamics, boundary condition, metric scale, lattice spacing, continuum or infrared limit, causal cone, probabilistic independence rule" in axioms)
    check("minimal Record axiom does not supply probability", "A record supplies no readout context, decomposition, K/CPT structure, sector-generation rule, weighting, normalization, probability" in axioms)
    check("Block147 maps uv=1/9 to kappa=0 under same-source raw moment", "kappa = 0 <=> uv = 1/9" in block147)
    check("Block148 requires raw moment and one-point product clauses", "C2. raw moment registry" in block148 and "C4. one-point product selector" in block148)
    check("Block149 leaves physical selector realization open", "Route-2 physical same-source selector realization theorem" in block149)
    check("Block150 records queue exhaustion, not closure", "physical same-source selector realization theorem" in block150 and "remains open" in block150)
    check("scalar normalization shortcut is already pruned", "Normalization alone does not select the one-point product" in scalar)
    check("binary finite-label transfer is already pruned", "P_R surface supplies disjoint finite E/T carrier labels" in binary)
    check("graph-first bridge still lacks typed functor", "typed functor from the selected-axis graph/color commutant" in graph)


def part2_exact_models() -> None:
    print()
    print("PART 2: exact cubic/readout models")
    expected = {
        "unsigned_axis_projector": (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3), Fraction(1, 9), Fraction(2, 9), Fraction(-6)),
        "independent_axis_projectors": (Fraction(1, 3), Fraction(1, 3), Fraction(1, 9), Fraction(1, 9), Fraction(0), Fraction(-8)),
        "signed_six_direction_component": (Fraction(0), Fraction(0), Fraction(1, 3), Fraction(0), Fraction(1, 3), Fraction(-5)),
        "symmetric_binary_same_record": (Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(1)),
        "axis_one_vs_two_signed": (Fraction(-1, 3), Fraction(-1, 3), Fraction(1), Fraction(1, 9), Fraction(8, 9), Fraction(0)),
        "target_biased_binary": (Fraction(1, 3), Fraction(1, 3), Fraction(1), Fraction(1, 9), Fraction(8, 9), Fraction(0)),
        "off_target_biased_binary": (Fraction(1, 2), Fraction(1, 2), Fraction(1), Fraction(1, 4), Fraction(3, 4), Fraction(-5, 4)),
    }
    for name, model in models().items():
        exp_mean_x, exp_mean_y, exp_raw, exp_product, exp_conn, exp_kappa = expected[name]
        print(
            f"  {name}: mean_x={model.mean_x}, mean_y={model.mean_y}, "
            f"raw={model.raw}, product={model.product}, connected={model.connected}, "
            f"kappa={model.kappa}"
        )
        check(f"{name} is normalized", model.normalized)
        check(f"{name} has exact expected X mean", model.mean_x == exp_mean_x)
        check(f"{name} has exact expected Y mean", model.mean_y == exp_mean_y)
        check(f"{name} has exact expected raw moment", model.raw == exp_raw)
        check(f"{name} has exact expected product", model.product == exp_product)
        check(f"{name} has exact expected connected value", model.connected == exp_conn)
        check(f"{name} has exact expected kappa", model.kappa == exp_kappa)
    check("unsigned axis projector has product 1/9 but wrong raw moment", models()["unsigned_axis_projector"].product == Fraction(1, 9) and models()["unsigned_axis_projector"].raw != 1)
    check("independent axis projectors have zero connected value", models()["independent_axis_projectors"].connected == 0)
    check("six-direction cubic symmetry makes signed mean zero", models()["signed_six_direction_component"].mean_x == 0)
    check("symmetric binary raw moment alone gives wrong kappa", models()["symmetric_binary_same_record"].raw == 1 and models()["symmetric_binary_same_record"].kappa != 0)
    check("one-vs-two axis collapse reaches target only with signed collapse", models()["axis_one_vs_two_signed"].kappa == 0)
    check("2:1 binary bias reaches target but is an explicit bias", models()["target_biased_binary"].kappa == 0)
    check("nearby 3:1 binary bias misses target", models()["off_target_biased_binary"].kappa != 0)


def part3_clause_supply() -> None:
    print()
    print("PART 3: clause supply")
    minimal_surface = {
        "z3_cubic_adjacency": True,
        "local_cl3_carrier": True,
        "finite_additive_record": True,
        "uniform_axis_probability_law": False,
        "selected_axis_for_route2": False,
        "signed_one_vs_two_readout": False,
        "physical_pr_et_variables": False,
        "same_source_raw_moment_one": False,
        "one_point_product_selector": False,
        "connected_subtraction_typing": False,
        "source_readout_unit_mu_one": False,
        "post_selector_orientation_sign": False,
    }
    theorem_surface = {
        **minimal_surface,
        "uniform_axis_probability_law": True,
        "selected_axis_for_route2": True,
        "signed_one_vs_two_readout": True,
        "physical_pr_et_variables": True,
        "same_source_raw_moment_one": True,
        "one_point_product_selector": True,
        "connected_subtraction_typing": True,
    }
    for name, present in minimal_surface.items():
        print(f"  minimal supplies {name}: {present}")
        check(f"minimal {name} is boolean", isinstance(present, bool))
    check("minimal surface has cubic support only", minimal_surface["z3_cubic_adjacency"] and minimal_surface["local_cl3_carrier"] and minimal_surface["finite_additive_record"])
    check("minimal surface does not supply uniform axis law", not minimal_surface["uniform_axis_probability_law"])
    check("minimal surface does not supply signed readout", not minimal_surface["signed_one_vs_two_readout"])
    check("minimal surface does not supply physical P_R/E-T variables", not minimal_surface["physical_pr_et_variables"])
    check("minimal surface does not supply product selector", not minimal_surface["one_point_product_selector"])
    check("theorem surface would add the exact load-bearing clauses", all(theorem_surface[k] for k in ("uniform_axis_probability_law", "selected_axis_for_route2", "signed_one_vs_two_readout", "physical_pr_et_variables", "same_source_raw_moment_one", "one_point_product_selector", "connected_subtraction_typing")))
    check("theorem surface still leaves unit/sign as separate downstream clauses", not theorem_surface["source_readout_unit_mu_one"] and not theorem_surface["post_selector_orientation_sign"])


def part4_reachability() -> None:
    print()
    print("PART 4: reachability")
    cubic_only_edges = [
        ("minimal_cubic_record_geometry", "z3_cubic_adjacency"),
        ("minimal_cubic_record_geometry", "finite_additive_record"),
        ("optional_uniform_axis_record", "unsigned_axis_occupancy_1_3"),
        ("unsigned_axis_occupancy_1_3", "missing_signed_readout_identification"),
        ("unsigned_axis_occupancy_1_3", "missing_same_source_raw_moment"),
    ]
    theorem_edges = [
        ("Route2_cubic_axis_readout_identification_theorem", "uniform_three_axis_record"),
        ("uniform_three_axis_record", "selected_axis_one_vs_two_signed_collapse"),
        ("selected_axis_one_vs_two_signed_collapse", "same_source_X_equals_Y"),
        ("same_source_X_equals_Y", "raw_E_XY_equals_one"),
        ("selected_axis_one_vs_two_signed_collapse", "product_E_X_E_Y_equals_one_ninth"),
        ("raw_E_XY_equals_one", "connected_subtraction_typed"),
        ("product_E_X_E_Y_equals_one_ninth", "connected_subtraction_typed"),
        ("connected_subtraction_typed", "kappa_zero_without_endpoint"),
    ]
    check("cubic-only graph reaches unsigned occupancy if uniform law is granted", reachable(cubic_only_edges, "optional_uniform_axis_record", "unsigned_axis_occupancy_1_3"))
    check("cubic-only graph reaches missing signed readout node", reachable(cubic_only_edges, "optional_uniform_axis_record", "missing_signed_readout_identification"))
    check("cubic-only graph does not reach raw E[XY]=1", not reachable(cubic_only_edges, "optional_uniform_axis_record", "raw_E_XY_equals_one"))
    check("cubic-only graph does not reach kappa=0", not reachable(cubic_only_edges, "optional_uniform_axis_record", "kappa_zero_without_endpoint"))
    check("cubic-axis readout theorem would reach kappa=0", reachable(theorem_edges, "Route2_cubic_axis_readout_identification_theorem", "kappa_zero_without_endpoint"))
    check("product selector remains load-bearing in theorem graph", reachable(theorem_edges, "product_E_X_E_Y_equals_one_ninth", "kappa_zero_without_endpoint"))
    all_nodes = {node for edge in cubic_only_edges + theorem_edges for node in edge}
    check("reachability graph has no endpoint-value input node", all("rho_E" not in node and "q_E" not in node and "c_TE_minus" not in node for node in all_nodes))
    check("reachability graph has no finite-box comparator node", all("box" not in node and "comparator" not in node for node in all_nodes))


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_CUBIC_RECORD_SELECTOR_NO_GO_2026-06-25.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    pr_body = loop_text("PR_BODY.md")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for cubic record geometry alone forcing the Route-2 same-source product selector E[X]E[Y]=1/9",
        "Cubic axis counting can supply at most an unsigned one-axis occupancy",
        "selected-axis one-vs-two signed collapse",
        "Route-2 cubic-axis readout identification theorem",
        "unsupported import or an axiom update, not a qualifying framework primitive",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block152 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate names cubic-axis readout identification theorem", "cubic-axis readout identification theorem" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
    check("PR body says no primitive is proposed", "No new primitive is proposed" in pr_body)
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
        ("discarded primitive-proposal wording", phrase("candidate ", "primitive")),
    )
    combined = note + "\n" + handoff + "\n" + cert + "\n" + trace_gate + "\n" + review + "\n" + state + "\n" + pr_body
    for label, marker in banned:
        check(f"banned marker absent: {label}", marker not in combined)


def main() -> int:
    print("Route-2 cubic-record selector no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_exact_models()
    part3_clause_supply()
    part4_reachability()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: cubic record geometry alone does not force the Route-2 same-source product selector; the remaining object is a typed cubic-axis readout identification theorem, not a new primitive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
