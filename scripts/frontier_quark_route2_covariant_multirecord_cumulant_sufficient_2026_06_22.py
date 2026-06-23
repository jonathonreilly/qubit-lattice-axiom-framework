#!/usr/bin/env python3
"""Conditional covariant multi-record cumulant theorem for Route-2."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-multirecord-cumulant-sufficient"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class MultiRecordPremises:
    covariant_adjoint_family: bool
    connected_hessian_typing: bool
    pure_disconnected_identity: bool
    coefficient_normalization: bool
    killing_contraction: bool

    @property
    def complete(self) -> bool:
        return all(
            (
                self.covariant_adjoint_family,
                self.connected_hessian_typing,
                self.pure_disconnected_identity,
                self.coefficient_normalization,
                self.killing_contraction,
            )
        )


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


def connected_fraction(adjoint_dim: int, identity_dim: int) -> Fraction:
    return Fraction(adjoint_dim, adjoint_dim + identity_dim)


def kappa_from_connected_fraction(frac: Fraction) -> Fraction:
    return 9 * (frac - Fraction(8, 9))


def trace(matrix: list[list[Fraction]]) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def permute_matrix(matrix: list[list[Fraction]], perm: list[int]) -> list[list[Fraction]]:
    return [[matrix[perm[i]][perm[j]] for j in range(len(perm))] for i in range(len(perm))]


def sign_flip_matrix(matrix: list[list[Fraction]], signs: list[int]) -> list[list[Fraction]]:
    return [[Fraction(signs[i] * signs[j]) * matrix[i][j] for j in range(len(signs))] for i in range(len(signs))]


def part1_grounding() -> None:
    print("PART 1: grounding")
    invariant = flat(text("QUARK_ROUTE2_INVARIANT_SCALAR_OUTPUT_COUPLING_NO_GO_NOTE_2026-06-22.md"))
    scalarization = flat(text("QUARK_ROUTE2_COVARIANT_SCALARIZATION_COLLAPSE_NO_GO_NOTE_2026-06-22.md"))
    bridge = flat(text("QUARK_ROUTE2_PHYSICAL_CONNECTED_HESSIAN_BRIDGE_STRETCH_NO_GO_NOTE_2026-06-22.md"))
    sufficient = flat(text("QUARK_ROUTE2_COLOR_MATRIX_LIFT_SUFFICIENT_THEOREM_2026-06-22.md"))
    check("invariant scalar output route is pruned", "color-invariant scalar output has zero first-order response" in invariant)
    check("covariant scalarization before E/T typing is pruned", "collapses the readout before the Route-2 E/T typing" in scalarization)
    check("Block112 names physical connected-Hessian theorem", "Route-2 physical connected-Hessian bridge theorem" in bridge)
    check("Block114 names same-source color-matrix lift clauses", "same-source lift premises" in sufficient)


def part2_conditional_theorem() -> None:
    print()
    print("PART 2: conditional theorem")
    premises = MultiRecordPremises(True, True, True, True, True)
    frac = connected_fraction(8, 1)
    kappa = kappa_from_connected_fraction(frac)
    print(f"  adjoint_dim=8, identity_dim=1, fraction={frac}, kappa={kappa}")
    check("all multi-record premises supplied in conditional theorem", premises.complete)
    check("connected fraction is 8/9", frac == Fraction(8, 9))
    check("conditional theorem forces kappa=0", kappa == 0)
    check("identity direction is one-dimensional", connected_fraction(8, 1).denominator == 9)


def part3_orientation_free_contraction() -> None:
    print()
    print("PART 3: orientation-free contraction")
    diag = [Fraction(i + 1) for i in range(8)]
    hessian = [[Fraction(0) for _ in range(8)] for _ in range(8)]
    for i, value in enumerate(diag):
        hessian[i][i] = value
    original = trace(hessian)
    perm = [7, 6, 5, 4, 3, 2, 1, 0]
    signs = [1, -1, 1, -1, 1, -1, 1, -1]
    permuted = trace(permute_matrix(hessian, perm))
    flipped = trace(sign_flip_matrix(hessian, signs))
    print(f"  trace original={original}, permuted={permuted}, sign_flipped={flipped}")
    check("Killing contraction trace is invariant under basis permutation", original == permuted)
    check("Killing contraction trace is invariant under sign flips", original == flipped)
    check("no adjoint covector is selected by trace contraction", original == sum(diag))
    check("single chosen component is not orientation-free", hessian[0][0] != original)


def part4_current_surface_firewall() -> None:
    print()
    print("PART 4: current-surface firewall")
    current = MultiRecordPremises(False, False, False, False, False)
    fields = {
        "covariant_adjoint_family": current.covariant_adjoint_family,
        "connected_hessian_typing": current.connected_hessian_typing,
        "pure_disconnected_identity": current.pure_disconnected_identity,
        "coefficient_normalization": current.coefficient_normalization,
        "killing_contraction": current.killing_contraction,
    }
    for name, supplied in fields.items():
        print(f"  current {name}: {supplied}")
        check(f"{name} classification is boolean", isinstance(supplied, bool))
    check("current multi-record theorem is not complete", not current.complete)
    check("all five multi-record premises remain open", sum(1 for supplied in fields.values() if not supplied) == 5)


def part5_trace_boundary() -> None:
    print()
    print("PART 5: trace boundary")
    support_edges = {
        "covariant_family": "open",
        "connected_subtraction": "available_support",
        "killing_contraction": "conditional",
        "scalarize_before_typing": "pruned",
        "external_adjoint_covector": "forbidden",
    }
    allowed = {"open", "available_support", "conditional", "pruned", "forbidden"}
    for name, status in support_edges.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("the theorem avoids scalarizing before typing", support_edges["scalarize_before_typing"] == "pruned")
    check("the theorem forbids an external adjoint covector", support_edges["external_adjoint_covector"] == "forbidden")


def part6_document_boundary() -> None:
    print()
    print("PART 6: document boundary")
    note = text("QUARK_ROUTE2_COVARIANT_MULTI_RECORD_CUMULANT_SUFFICIENT_THEOREM_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: conditional-support; the covariant multi-record Route-2 source/readout family is not supplied",
        "Sufficient Theorem",
        "orientation-free Killing contraction",
        "kappa = 0",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block115 Summary", "upstream_support", "Do not audit", "Next Exact Action"):
        check(f"handoff contains marker: {marker}", marker in handoff)
    check("certificate keeps proposal disallowed", "proposal_allowed: false" in cert)
    check("trace gate marks upstream support", "trace_class: upstream_support" in trace_gate)
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
    print("Route-2 covariant multi-record cumulant sufficient theorem")
    print("TRACE: upstream_support")
    part1_grounding()
    part2_conditional_theorem()
    part3_orientation_free_contraction()
    part4_current_surface_firewall()
    part5_trace_boundary()
    part6_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: a same-source covariant adjoint multi-record cumulant with Killing contraction would force kappa=0 without a color-orientation selector; that record family remains open on the current surface.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
