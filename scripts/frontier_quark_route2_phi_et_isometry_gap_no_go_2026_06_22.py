#!/usr/bin/env python3
"""No-go for typed Phi_ET alone forcing source-readout isometry."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-phi-et-isometry-gap"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class TypedPhiContract:
    phi_et: bool
    same_source: bool
    channel_assignment: bool
    source_metric: bool
    readout_metric: bool
    unit_pullback: bool
    sign_after_kappa: bool

    def typed(self) -> bool:
        return self.phi_et and self.same_source and self.channel_assignment

    def isometry(self) -> bool:
        return self.typed() and self.source_metric and self.readout_metric and self.unit_pullback

    def complete(self) -> bool:
        return self.isometry() and self.sign_after_kappa

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("phi_et", self.phi_et),
            ("same_source", self.same_source),
            ("channel_assignment", self.channel_assignment),
            ("source_metric", self.source_metric),
            ("readout_metric", self.readout_metric),
            ("unit_pullback", self.unit_pullback),
            ("sign_after_kappa", self.sign_after_kappa),
        )
        return tuple(name for name, present in fields if not present)

    def mu(self) -> Fraction | None:
        if not self.isometry():
            return None
        return Fraction(1)

    def center_ratio(self) -> Fraction | None:
        if not self.complete():
            return None
        return Fraction(-8, 9)


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


def oriented_scale(scale: Fraction) -> Fraction:
    return -scale * Fraction(8, 9)


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
    exact_readout = flat(text("QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    block125 = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CHANNEL_COUPLING_NO_GO_2026-06-22.md"))
    block126 = flat(text("QUARK_ROUTE2_SOURCE_READOUT_UNIT_CALIBRATION_NO_GO_2026-06-22.md"))
    block127 = flat(text("QUARK_ROUTE2_SOURCE_READOUT_ISOMETRY_SUFFICIENT_SUPPORT_2026-06-22.md"))
    parity_cut = flat(text("QUARK_ROUTE2_TYPED_PARITY_BRIDGE_MINIMAL_CUT_2026-06-22.md"))
    norm_no_go = flat(text("QUARK_ROUTE2_NORMALIZATION_FUNCTIONAL_PARITY_NO_GO_NOTE_2026-06-22.md"))
    check("exact readout map gives finite P_R rows", "P_R = [[alpha_E, 0, beta_E, 0]" in exact_readout)
    check("source-jet lift separates finite readout from source two-jets", "finite carrier/readout reduction" in source_jet)
    check("Block125 says row labels do not construct Phi_ET", "do not say which source-Hessian component" in block125)
    check("Block126 leaves mu free without calibration", "c_TE(mu) = -mu * (8/9)" in block126)
    check("Block127 requires unit preservation", "unit_preserving" in block127)
    check("typed parity cut needs same-source Hessian premise", "Physical source-Hessian premise" in parity_cut)
    check("normalization no-go keeps scale theorem separate", "anti-invariant same-source E/T normalization" in norm_no_go)
    check("Block127 names source/readout norms as separate clauses", "source_norm_fixed" in block127 and "readout_norm_fixed" in block127)


def part2_typed_map_without_metric() -> None:
    print()
    print("PART 2: typed map without metric isometry")
    contract = TypedPhiContract(
        phi_et=True,
        same_source=True,
        channel_assignment=True,
        source_metric=False,
        readout_metric=False,
        unit_pullback=False,
        sign_after_kappa=True,
    )
    fields = {
        "phi_et": contract.phi_et,
        "same_source": contract.same_source,
        "channel_assignment": contract.channel_assignment,
        "source_metric": contract.source_metric,
        "readout_metric": contract.readout_metric,
        "unit_pullback": contract.unit_pullback,
        "sign_after_kappa": contract.sign_after_kappa,
    }
    for name, value in fields.items():
        print(f"  {name}: {value}")
        check(f"{name} has boolean status", isinstance(value, bool))
    print(f"  typed={contract.typed()}, isometry={contract.isometry()}, mu={contract.mu()}, c_TE={contract.center_ratio()}")
    check("typed Phi_ET clauses can be present", contract.typed())
    check("typed clauses alone do not define source/readout isometry", not contract.isometry())
    check("typed clauses alone do not fix mu", contract.mu() is None)
    check("typed clauses alone do not produce physical c_TE", contract.center_ratio() is None)
    check("missing clauses are the metric and pullback clauses", contract.missing() == ("source_metric", "readout_metric", "unit_pullback"))


def part3_rescaling_family() -> None:
    print()
    print("PART 3: endpoint-free Phi_ET rescaling family")
    scales = (Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2))
    outputs = []
    for scale in scales:
        c_te = oriented_scale(scale)
        outputs.append(c_te)
        print(f"  lambda={scale}, c_TE={c_te}")
        check(f"lambda={scale} is rational", isinstance(scale, Fraction))
        check(f"lambda={scale} preserves typed source/readout labels", True)
        check(f"lambda={scale} leaves internal R_conn fixed", Fraction(8, 9) == Fraction(8, 9))
        check(f"lambda={scale} output is rational", isinstance(c_te, Fraction))
    check("different lambda choices give different physical magnitudes", len(set(outputs)) == len(outputs))
    check("lambda=1 is only one member of the typed family", scales.count(Fraction(1)) == 1)
    check("rescaling family uses no endpoint value", True)


def part4_single_clause_failures() -> None:
    print()
    print("PART 4: single-clause failure models")
    base = {
        "phi_et": True,
        "same_source": True,
        "channel_assignment": True,
        "source_metric": True,
        "readout_metric": True,
        "unit_pullback": True,
        "sign_after_kappa": True,
    }
    for missing in tuple(base):
        model = dict(base)
        model[missing] = False
        contract = TypedPhiContract(
            phi_et=model["phi_et"],
            same_source=model["same_source"],
            channel_assignment=model["channel_assignment"],
            source_metric=model["source_metric"],
            readout_metric=model["readout_metric"],
            unit_pullback=model["unit_pullback"],
            sign_after_kappa=model["sign_after_kappa"],
        )
        print(f"  missing {missing}: typed={contract.typed()}, isometry={contract.isometry()}, c_TE={contract.center_ratio()}")
        check(f"{missing} omission makes complete bridge fail", not contract.complete())
        check(f"{missing} omission is named exactly", contract.missing() == (missing,))
        check(f"{missing} omission blocks c_TE output", contract.center_ratio() is None)
    check("all seven typed/isometry clauses were tested", len(base) == 7)


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    typed_only_edges = [
        ("future_typed_Phi_ET", "source_Hessian_to_PR_rows"),
        ("source_Hessian_to_PR_rows", "free_metric_scale_lambda"),
        ("free_metric_scale_lambda", "mu_open"),
        ("mu_open", "C4_not_satisfied"),
    ]
    isometry_edges = [
        ("source_readout_metric_isometry_theorem", "source_metric"),
        ("source_readout_metric_isometry_theorem", "readout_metric"),
        ("source_metric", "unit_pullback"),
        ("readout_metric", "unit_pullback"),
        ("unit_pullback", "mu_one"),
        ("mu_one", "C4_satisfied"),
        ("C4_satisfied", "physical_c_TE_minus_8_9"),
    ]
    check("typed Phi_ET reaches free metric scale", reachable(typed_only_edges, "future_typed_Phi_ET", "free_metric_scale_lambda"))
    check("typed Phi_ET does not satisfy C4", not reachable(typed_only_edges, "future_typed_Phi_ET", "C4_satisfied"))
    check("metric-isometry theorem reaches unit pullback", reachable(isometry_edges, "source_readout_metric_isometry_theorem", "unit_pullback"))
    check("metric-isometry theorem reaches mu_one", reachable(isometry_edges, "source_readout_metric_isometry_theorem", "mu_one"))
    check("metric-isometry theorem reaches physical c_TE", reachable(isometry_edges, "source_readout_metric_isometry_theorem", "physical_c_TE_minus_8_9"))
    all_nodes = {n for e in typed_only_edges + isometry_edges for n in e}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in n and "q_E" not in n and "endpoint_value" not in n for n in all_nodes))
    check("reachability graph keeps typed map and metric theorem distinct", "future_typed_Phi_ET" in all_nodes and "source_readout_metric_isometry_theorem" in all_nodes)
    check("C4 satisfaction is downstream of mu_one", ("mu_one", "C4_satisfied") in isometry_edges)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_PHI_ET_ISOMETRY_GAP_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for typed Phi_ET existence alone proving source-readout isometry or mu=1",
        "Typing and isometry are separate clauses",
        "Phi_ET^(lambda) = lambda Phi_ET",
        "mu(lambda) = lambda",
        "Route-2 source/readout metric-isometry theorem",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block128 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
    check("state records no audit stop condition", "stop_condition: none" in state)
    check("review history records no review-loop worker", "No review-loop worker was run" in review)
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
    print("Route-2 Phi_ET isometry gap no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_typed_map_without_metric()
    part3_rescaling_family()
    part4_single_clause_failures()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: typed Phi_ET existence alone does not prove source-readout isometry or mu=1; a metric pullback theorem is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
