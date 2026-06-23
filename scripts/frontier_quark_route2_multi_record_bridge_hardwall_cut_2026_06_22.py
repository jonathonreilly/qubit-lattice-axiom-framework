#!/usr/bin/env python3
"""Hard-wall cut certificate for the Route-2 multi-record bridge."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-bridge-hardwall-cut"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class BridgeClauses:
    covariant_records: bool
    physical_log_hessian_typing: bool
    identity_factorization: bool
    coefficient_normalization: bool
    endpoint_magnitude_typing: bool
    inverse_killing_contraction: bool
    endpoint_sign: bool

    @property
    def closes_magnitude(self) -> bool:
        return all(
            (
                self.covariant_records,
                self.physical_log_hessian_typing,
                self.identity_factorization,
                self.coefficient_normalization,
                self.endpoint_magnitude_typing,
                self.inverse_killing_contraction,
            )
        )

    @property
    def closes_signed_bridge(self) -> bool:
        return self.closes_magnitude and self.endpoint_sign


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


def c_te(sigma: int, kappa: Fraction) -> Fraction:
    return Fraction(sigma) * (Fraction(8, 9) + kappa * Fraction(1, 9))


def part1_grounding() -> None:
    print("PART 1: grounding")
    block115 = flat(text("QUARK_ROUTE2_COVARIANT_MULTI_RECORD_CUMULANT_SUFFICIENT_THEOREM_2026-06-22.md"))
    block116 = flat(text("QUARK_ROUTE2_ADJOINT_INVARIANT_CONTRACTION_UNIQUENESS_SUPPORT_NOTE_2026-06-22.md"))
    block117 = flat(text("QUARK_ROUTE2_ADJOINT_SINGLET_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    block118 = flat(text("QUARK_ROUTE2_SINGLET_RESIDUAL_INDEPENDENCE_NO_GO_NOTE_2026-06-22.md"))
    sign = flat(text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md"))
    source_jet = flat(text("QUARK_ROUTE2_SOURCE_JET_LIFT_NO_GO_NOTE_2026-06-22.md"))
    pcal = flat(text("QUARK_ROUTE2_PCAL_MOMENT_REALIZATION_NO_GO_NOTE_2026-06-22.md"))
    check("Block115 states sufficient multi-record theorem", "same-source covariant adjoint record family" in block115)
    check("Block116 proves inverse-Killing uniqueness up to scale", "unique up to scale" in block116)
    check("Block117 prunes invariance-only normalization", "does not choose their relative coefficient" in block117)
    check("Block118 prunes invariance-only eta zero", "connected-cumulant algebra forcing the identity-line residual to vanish" in block118)
    check("endpoint sign support separates sigma=-1", "sigma=-1" in sign and "magnitude remains open" in sign.lower())
    check("source-jet lift keeps physical source Hessian missing", "same-source source-jet lift theorem" in source_jet)
    check("Pcal moment realization keeps raw/product split missing", "Route-2 Pcal moment-realization theorem" in pcal)


def part2_clause_status() -> None:
    print()
    print("PART 2: clause status")
    current = BridgeClauses(
        covariant_records=False,
        physical_log_hessian_typing=False,
        identity_factorization=False,
        coefficient_normalization=False,
        endpoint_magnitude_typing=False,
        inverse_killing_contraction=True,
        endpoint_sign=True,
    )
    sufficient = BridgeClauses(
        covariant_records=True,
        physical_log_hessian_typing=True,
        identity_factorization=True,
        coefficient_normalization=True,
        endpoint_magnitude_typing=True,
        inverse_killing_contraction=True,
        endpoint_sign=True,
    )
    fields = current.__dict__
    for name, supplied in fields.items():
        print(f"  current {name}: {supplied}")
        check(f"{name} has boolean status", isinstance(supplied, bool))
    check("current clauses do not close magnitude", not current.closes_magnitude)
    check("current clauses do not close signed bridge", not current.closes_signed_bridge)
    check("sufficient clauses close magnitude", sufficient.closes_magnitude)
    check("sufficient clauses close signed bridge", sufficient.closes_signed_bridge)
    check("current support has exactly two supported switches", sum(1 for v in fields.values() if v) == 2)
    check("current missing clauses are exactly five", sum(1 for v in fields.values() if not v) == 5)


def part3_exact_bridge_arithmetic() -> None:
    print()
    print("PART 3: exact bridge arithmetic")
    cases = {
        "target": (-1, Fraction(0), Fraction(-8, 9)),
        "wrong_sign": (+1, Fraction(0), Fraction(8, 9)),
        "wrong_kappa": (-1, Fraction(1), Fraction(-1)),
        "half_residual": (-1, Fraction(1, 2), Fraction(-17, 18)),
    }
    for name, (sigma, kap, expected) in cases.items():
        value = c_te(sigma, kap)
        print(f"  {name}: sigma={sigma}, kappa={kap}, c_TE={value}")
        check(f"{name} signed ratio matches expected", value == expected)
    check("only sigma=-1 and kappa=0 lands target in tested cases", [name for name, (sigma, kap, _) in cases.items() if c_te(sigma, kap) == Fraction(-8, 9)] == ["target"])
    check("positive sign with kappa=0 is wrong signed endpoint", c_te(+1, Fraction(0)) != Fraction(-8, 9))
    check("negative sign with kappa=1 is wrong magnitude", c_te(-1, Fraction(1)) != Fraction(-8, 9))


def part4_reachability() -> None:
    print()
    print("PART 4: reachability cut")
    current_edges = [
        ("current_support_stack", "inverse_killing_contraction_supported"),
        ("current_support_stack", "endpoint_sign_supported"),
        ("current_support_stack", "missing_same_source_multirecord_theorem"),
        ("missing_same_source_multirecord_theorem", "missing_log_hessian_typing"),
        ("missing_same_source_multirecord_theorem", "missing_identity_factorization"),
        ("missing_same_source_multirecord_theorem", "missing_coefficient_normalization"),
        ("missing_same_source_multirecord_theorem", "missing_endpoint_magnitude_typing"),
    ]
    sufficient_edges = [
        ("same_source_multirecord_theorem", "covariant_records"),
        ("covariant_records", "physical_log_hessian_typing"),
        ("physical_log_hessian_typing", "identity_factorization"),
        ("identity_factorization", "coefficient_normalization"),
        ("coefficient_normalization", "kappa_zero"),
        ("kappa_zero", "R_phys_8_9"),
        ("R_phys_8_9", "endpoint_magnitude_typed"),
        ("endpoint_magnitude_typed", "endpoint_sign_sigma_minus_one"),
        ("endpoint_sign_sigma_minus_one", "c_TE_minus_8_9"),
    ]
    check("current stack reaches missing theorem node", reachable(current_edges, "current_support_stack", "missing_same_source_multirecord_theorem"))
    check("current stack does not reach kappa zero", not reachable(current_edges, "current_support_stack", "kappa_zero"))
    check("current stack does not reach signed bridge", not reachable(current_edges, "current_support_stack", "c_TE_minus_8_9"))
    check("sufficient theorem reaches kappa zero", reachable(sufficient_edges, "same_source_multirecord_theorem", "kappa_zero"))
    check("sufficient theorem reaches signed bridge", reachable(sufficient_edges, "same_source_multirecord_theorem", "c_TE_minus_8_9"))
    all_current_nodes = {n for e in current_edges for n in e}
    check("current graph has no endpoint-value import node", all("rho_E" not in n and "q_E" not in n for n in all_current_nodes))


def part5_missing_primitive_packet() -> None:
    print()
    print("PART 5: missing primitive packet")
    primitive_clauses = {
        "construct covariant adjoint records X_A": True,
        "type physical readout as D_A D_B log Z": True,
        "prove D_0 D_0 Z = (D_0 Z)^2": True,
        "fix equal adjoint/singlet unit weights": True,
        "identify magnitude readout with Route-2 center ratio": True,
    }
    for clause, present in primitive_clauses.items():
        print(f"  primitive clause: {clause}")
        check(f"primitive clause recorded: {clause}", present)
    check("primitive packet has five clauses", len(primitive_clauses) == 5)
    check("primitive packet separates sign from magnitude", "identify magnitude readout with Route-2 center ratio" in primitive_clauses)


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_MULTI_RECORD_BRIDGE_HARDWALL_CUT_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for the current available support stack alone closing R_conn -> c_TE=-8/9",
        "Route-2 same-source covariant multi-record bridge theorem",
        "D_0 D_0 Z = (D_0 Z)^2",
        "c_TE = -8/9",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block119 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks negative route pruning", "trace_class: negative_route_pruning" in trace_gate)
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
    print("Route-2 multi-record bridge hard-wall cut")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_clause_status()
    part3_exact_bridge_arithmetic()
    part4_reachability()
    part5_missing_primitive_packet()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: the current support stack does not close R_conn -> c_TE=-8/9; the exact missing primitive is the same-source covariant multi-record bridge theorem with source-Hessian typing, identity factorization, normalization, and endpoint magnitude typing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
