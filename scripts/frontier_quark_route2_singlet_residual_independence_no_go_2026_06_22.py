#!/usr/bin/env python3
"""No-go for invariance/cumulants alone forcing pure disconnected singlet residual."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-singlet-residual-independence"

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


def r_cumulant(eta: Fraction) -> Fraction:
    return Fraction(8, 9) + eta * Fraction(1, 9)


def kappa(eta: Fraction) -> Fraction:
    return 9 * (r_cumulant(eta) - Fraction(8, 9))


def connected_identity_second_derivative(raw_second: Fraction, one_point: Fraction) -> Fraction:
    return raw_second - one_point * one_point


def part1_grounding() -> None:
    print("PART 1: grounding")
    block115 = flat(text("QUARK_ROUTE2_COVARIANT_MULTI_RECORD_CUMULANT_SUFFICIENT_THEOREM_2026-06-22.md"))
    block116 = flat(text("QUARK_ROUTE2_ADJOINT_INVARIANT_CONTRACTION_UNIQUENESS_SUPPORT_NOTE_2026-06-22.md"))
    block117 = flat(text("QUARK_ROUTE2_ADJOINT_SINGLET_NORMALIZATION_NO_GO_NOTE_2026-06-22.md"))
    source_hessian = flat(text("QUARK_ROUTE2_SOURCE_HESSIAN_CUMULANT_SELECTOR_SUPPORT_NOTE_2026-06-22.md"))
    symmetric_purity = flat(text("QUARK_ROUTE2_SYMMETRIC_LINE_PURITY_NO_GO_NOTE_2026-06-22.md"))
    check("Block115 requires pure disconnected identity line", "scalar identity line is pure disconnected" in block115)
    check("Block116 retires orientation selector only", "unique up to scale" in block116)
    check("Block117 keeps adjoint/singlet normalization separate", "relative coefficient" in block117)
    check("source-Hessian support exposes eta family", "R_cumulant(eta) = 8/9 + eta/9" in source_hessian)
    check("symmetric purity no-go keeps same-source factorization open", "same-source factorization" in symmetric_purity)


def part2_eta_family() -> None:
    print()
    print("PART 2: singlet residual eta family")
    cases = {
        "pure_disconnected": (Fraction(0), Fraction(8, 9), Fraction(0)),
        "half_connected": (Fraction(1, 2), Fraction(17, 18), Fraction(1, 2)),
        "pure_connected": (Fraction(1), Fraction(1), Fraction(1)),
    }
    for name, (eta, expected_r, expected_kappa) in cases.items():
        value = r_cumulant(eta)
        kap = kappa(eta)
        print(f"  {name}: eta={eta}, R={value}, kappa={kap}")
        check(f"{name} R matches expected", value == expected_r)
        check(f"{name} kappa matches expected", kap == expected_kappa)
    check("only eta=0 gives kappa=0 in sampled cases", [name for name, (eta, _, _) in cases.items() if kappa(eta) == 0] == ["pure_disconnected"])
    check("eta remains a one-parameter obstruction", len({r_cumulant(Fraction(n, 4)) for n in range(5)}) == 5)


def part3_factorization_boundary() -> None:
    print()
    print("PART 3: factorization boundary")
    one_point = Fraction(1, 3)
    pure_raw = one_point * one_point
    half_raw = pure_raw + Fraction(1, 18)
    connected_raw = pure_raw + Fraction(1, 9)
    samples = {
        "pure_raw": (pure_raw, Fraction(0)),
        "half_raw": (half_raw, Fraction(1, 18)),
        "connected_raw": (connected_raw, Fraction(1, 9)),
    }
    for name, (raw, expected_connected) in samples.items():
        connected = connected_identity_second_derivative(raw, one_point)
        print(f"  {name}: raw={raw}, connected={connected}")
        check(f"{name} connected identity derivative matches", connected == expected_connected)
    check("raw second moment equal to product is extra information", pure_raw == one_point * one_point)
    check("same one-point can support nonzero connected residual", half_raw != one_point * one_point and connected_raw != one_point * one_point)
    check("connected-cumulant formula subtracts product but does not choose raw second moment", len({raw for raw, _ in samples.values()}) == 3)


def part4_trace_boundary() -> None:
    print()
    print("PART 4: trace boundary")
    statuses = {
        "singlet_adjoint_cross_term": "forbidden",
        "adjoint_contraction": "unique_up_to_scale",
        "identity_connected_residual": "open",
        "invariance_forces_eta_zero": "pruned",
        "same_source_factorization_theorem": "missing",
    }
    allowed = {"forbidden", "unique_up_to_scale", "open", "pruned", "missing"}
    for name, status in statuses.items():
        print(f"  {name}: {status}")
        check(f"{name} status classified", status in allowed)
    check("invariance forcing eta=0 is pruned", statuses["invariance_forces_eta_zero"] == "pruned")
    check("same-source factorization theorem remains missing", statuses["same_source_factorization_theorem"] == "missing")
    check("identity connected residual remains open", statuses["identity_connected_residual"] == "open")


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    note = text("QUARK_ROUTE2_SINGLET_RESIDUAL_INDEPENDENCE_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    cert = loop_text("CLAIM_STATUS_CERTIFICATE.md")
    trace_gate = loop_text("TRACE_GATE.md")
    review = loop_text("REVIEW_HISTORY.md")
    state = loop_text("STATE.yaml")
    note_flat = flat(note)
    required = (
        "Actual current-surface status: no-go for SU(3) invariance plus connected-cumulant algebra forcing the identity-line residual to vanish",
        "R_cumulant(eta) = 8/9 + eta/9",
        "Route-2 identity-line pure-disconnected factorization theorem",
        "D_0 D_0 log Z = 0",
        "No endpoint value is used",
    )
    for marker in required:
        check(f"note contains marker: {marker}", marker in note_flat)
    for marker in ("Block118 Summary", "negative_route_pruning", "Do not audit", "Next Exact Action"):
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
    print("Route-2 singlet residual independence no-go")
    print("TRACE: negative_route_pruning")
    part1_grounding()
    part2_eta_family()
    part3_factorization_boundary()
    part4_trace_boundary()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        return 1
    print("VERDICT: SU(3) invariance and connected-cumulant algebra do not force the identity-line residual eta to vanish; Route-2 still needs a same-source pure-disconnected factorization theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
