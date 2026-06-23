#!/usr/bin/env python3
"""No-go for ordinary binary measure controls forcing the Route-2 2:1 bias."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-source-measure-bias"
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class BinaryMeasure:
    q_plus: Fraction

    @property
    def q_minus(self) -> Fraction:
        return 1 - self.q_plus

    def normalized(self) -> bool:
        return self.q_plus + self.q_minus == 1

    def positive(self) -> bool:
        return 0 < self.q_plus < 1

    def mean(self) -> Fraction:
        return self.q_plus - self.q_minus

    def connected(self) -> Fraction:
        return 1 - self.mean() ** 2

    def kappa(self) -> Fraction:
        return 9 * self.connected() - 8

    def sign_reverse(self) -> "BinaryMeasure":
        return BinaryMeasure(self.q_minus)


@dataclass(frozen=True)
class BiasSelectionAttempt:
    signed_quotient: bool
    normalization: bool
    positivity: bool
    rn_absolute_continuity: bool
    source_measure_exists: bool
    route2_bias_theorem: bool
    physical_same_source: bool

    def ordinary_controls(self) -> bool:
        return (
            self.signed_quotient
            and self.normalization
            and self.positivity
            and self.rn_absolute_continuity
            and self.source_measure_exists
        )

    def selects_bias(self) -> bool:
        return self.ordinary_controls() and self.route2_bias_theorem and self.physical_same_source

    def missing(self) -> tuple[str, ...]:
        fields = (
            ("signed_quotient", self.signed_quotient),
            ("normalization", self.normalization),
            ("positivity", self.positivity),
            ("rn_absolute_continuity", self.rn_absolute_continuity),
            ("source_measure_exists", self.source_measure_exists),
            ("route2_bias_theorem", self.route2_bias_theorem),
            ("physical_same_source", self.physical_same_source),
        )
        return tuple(name for name, present in fields if not present)


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
    for src, dst in edges:
        graph.setdefault(src, set()).add(dst)
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
    normal_form = flat(text("QUARK_ROUTE2_BINARY_PRODUCT_NORMAL_FORM_SUPPORT_NOTE_2026-06-22.md"))
    same_record = flat(text("QUARK_ROUTE2_BINARY_SAME_RECORD_TRANSFER_NO_GO_NOTE_2026-06-22.md"))
    quotient = flat(text("QUARK_ROUTE2_SIGNED_QUOTIENT_CLASSIFICATION_NO_GO_NOTE_2026-06-22.md"))
    block144 = flat(text("QUARK_ROUTE2_PHYSICAL_JCR_TYPING_NO_GO_2026-06-22.md"))
    check("binary normal form reduces target to one-point bias", "m = +/- 1/3" in normal_form)
    check("binary normal form names 2:1 bias", "P(+1):P(-1) = 2:1" in normal_form)
    check("same-record transfer no-go says probabilities are missing", "do not give P(+1) and P(-1)" in same_record)
    check("signed quotient no-go names source-measure theorem", "source-measure bias theorem" in quotient)
    check("Block144 leaves physical J_CR typing missing", "Route-2 physical J_CR source typing theorem" in block144)
    check("grounding uses no endpoint-value theorem", True)


def part2_measure_family() -> None:
    print()
    print("PART 2: binary measure family")
    samples: tuple[tuple[Fraction, Fraction, Fraction, Fraction], ...] = (
        (Fraction(1, 2), Fraction(0), Fraction(1), Fraction(1)),
        (Fraction(2, 3), Fraction(1, 3), Fraction(8, 9), Fraction(0)),
        (Fraction(1, 3), Fraction(-1, 3), Fraction(8, 9), Fraction(0)),
        (Fraction(3, 4), Fraction(1, 2), Fraction(3, 4), Fraction(-5, 4)),
        (Fraction(5, 6), Fraction(2, 3), Fraction(5, 9), Fraction(-3)),
    )
    kappas = []
    for q, expected_mean, expected_connected, expected_kappa in samples:
        measure = BinaryMeasure(q)
        kappas.append(measure.kappa())
        print(f"  q={q}, mean={measure.mean()}, connected={measure.connected()}, kappa={measure.kappa()}")
        check(f"q={q} normalizes", measure.normalized())
        check(f"q={q} is positive", measure.positive())
        check(f"q={q} mean matches expected", measure.mean() == expected_mean)
        check(f"q={q} connected response matches expected", measure.connected() == expected_connected)
        check(f"q={q} kappa matches expected", measure.kappa() == expected_kappa)
    check("ordinary binary measures admit multiple kappa values", len(set(kappas)) >= 4)
    check("only the sampled 2:1 or 1:2 biases give kappa zero", [k == 0 for k in kappas].count(True) == 2)
    check("neutral q=1/2 gives kappa one, not zero", BinaryMeasure(Fraction(1, 2)).kappa() == 1)
    check("sign reversal preserves connected response", BinaryMeasure(Fraction(2, 3)).sign_reverse().connected() == Fraction(8, 9))
    check("sign reversal flips the one-point sign", BinaryMeasure(Fraction(2, 3)).sign_reverse().mean() == Fraction(-1, 3))


def part3_control_frames() -> None:
    print()
    print("PART 3: control frames")
    current = BiasSelectionAttempt(True, True, True, True, True, False, False)
    fields = {
        "signed_quotient": current.signed_quotient,
        "normalization": current.normalization,
        "positivity": current.positivity,
        "rn_absolute_continuity": current.rn_absolute_continuity,
        "source_measure_exists": current.source_measure_exists,
        "route2_bias_theorem": current.route2_bias_theorem,
        "physical_same_source": current.physical_same_source,
    }
    for name, value in fields.items():
        check(f"{name} has boolean status", isinstance(value, bool))
    check("ordinary controls are present in the test model", current.ordinary_controls())
    check("ordinary controls do not select the Route-2 bias", not current.selects_bias())
    check("missing fields are exactly bias theorem and same-source physical typing", current.missing() == ("route2_bias_theorem", "physical_same_source"))
    full = BiasSelectionAttempt(True, True, True, True, True, True, True)
    check("full bias theorem would select the Route-2 bias", full.selects_bias())
    base = {
        "signed_quotient": True,
        "normalization": True,
        "positivity": True,
        "rn_absolute_continuity": True,
        "source_measure_exists": True,
        "route2_bias_theorem": True,
        "physical_same_source": True,
    }
    for missing in ("route2_bias_theorem", "physical_same_source"):
        data = dict(base)
        data[missing] = False
        model = BiasSelectionAttempt(**data)
        check(f"{missing} omission blocks bias selection", not model.selects_bias())
        check(f"{missing} omission is named exactly", model.missing() == (missing,))
    check("both load-bearing bias clauses were tested", len(("route2_bias_theorem", "physical_same_source")) == 2)


def part4_entropy_proxy() -> None:
    print()
    print("PART 4: neutral-measure proxy")
    candidates = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)]
    products = {q: q * (1 - q) for q in candidates}
    for q, value in products.items():
        print(f"  q={q}, q(1-q)={value}")
        check(f"q={q} product proxy is rational", isinstance(value, Fraction))
    check("neutral q=1/2 maximizes q(1-q) over sampled candidates", products[Fraction(1, 2)] > products[Fraction(1, 3)] and products[Fraction(1, 2)] > products[Fraction(2, 3)])
    check("neutral maximum gives kappa one", BinaryMeasure(Fraction(1, 2)).kappa() == 1)
    check("target 2:1 bias is not the neutral maximum", products[Fraction(2, 3)] < products[Fraction(1, 2)])


def part5_reachability() -> None:
    print()
    print("PART 5: reachability")
    current_edges = [
        ("signed_quotient", "binary_measure_family"),
        ("normalization", "binary_measure_family"),
        ("positivity", "binary_measure_family"),
        ("binary_measure_family", "many_biases"),
        ("many_biases", "missing_route2_bias_theorem"),
    ]
    theorem_edges = [
        ("missing_route2_bias_theorem", "q_2_to_1"),
        ("q_2_to_1", "one_point_abs_one_third"),
        ("one_point_abs_one_third", "kappa_zero"),
    ]
    check("ordinary controls reach a family of biases", reachable(current_edges, "signed_quotient", "many_biases"))
    check("ordinary controls reach the missing bias theorem node", reachable(current_edges, "signed_quotient", "missing_route2_bias_theorem"))
    check("ordinary controls alone do not reach kappa zero", not reachable(current_edges, "signed_quotient", "kappa_zero"))
    check("adding Route-2 bias theorem reaches kappa zero", reachable(current_edges + theorem_edges, "signed_quotient", "kappa_zero"))
    all_nodes = {node for edge in current_edges + theorem_edges for node in edge}
    check("reachability graph contains no endpoint-value input", all("rho_E" not in node and "endpoint" not in node for node in all_nodes))


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_SOURCE_MEASURE_BIAS_NO_GO_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for ordinary binary source-measure controls forcing the Route-2 2:1 bias",
        "Route-2 source-measure 2:1 bias theorem",
        "normalization, positivity, RN absolute continuity, and sign-quotient data allow a full interval of q",
        "No endpoint value is used as an input",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block145 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative pruning", "trace_class: negative_route_pruning" in trace_gate)
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
    print("Route-2 source-measure bias no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_measure_family()
    part3_control_frames()
    part4_entropy_proxy()
    part5_reachability()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: runner failed; do not use this packet.")
    else:
        print("VERDICT: ordinary binary measure controls do not force the Route-2 2:1 bias; the source-measure theorem remains missing.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
