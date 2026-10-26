#!/usr/bin/env python3
"""Supplied finite weight and quadratic-form diagnostic, not a physical selector.

The old ledger census is preserved as historical source and is not executed.
Boolean readiness labels are stipulated classifications, not derived authority.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/POST_RECORD_SELECTOR_TANGENT_READOUT_WEIGHT_PROTOTYPE_2026-06-06.md",
    "docs/HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md",
)
PASS = 0
FAIL = 0


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read_rel(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    flat = " ".join(text.split())
    report(f"{path} exists", (ROOT / path).exists())
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text or needle in flat)


def normalize(weights: dict[str, Fraction]) -> dict[str, Fraction]:
    if any(value < 0 for value in weights.values()):
        raise ValueError("negative supplied weight")
    total = sum(weights.values(), Fraction(0))
    if total <= 0:
        raise ValueError("nonpositive supplied total")
    return {key: value / total for key, value in weights.items()}


def quadratic(metric: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]], vector: tuple[Fraction, Fraction]) -> Fraction:
    x, y = vector
    return metric[0][0] * x * x + (metric[0][1] + metric[1][0]) * x * y + metric[1][1] * y * y


def is_spd_2x2(metric: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> bool:
    return metric[0][1] == metric[1][0] and metric[0][0] > 0 and metric[0][0] * metric[1][1] - metric[0][1] * metric[1][0] > 0


def selector_authority(has_weight_certificate: bool, has_selector_rule: bool) -> str:
    if has_weight_certificate and has_selector_rule:
        return "conditional_selector_ready"
    return "blocked_missing_selector"


def certificate_checks() -> None:
    section("Supplied finite selector/tangent/readout arithmetic checks")
    weights = normalize({"endpoint_lo": Fraction(1), "endpoint_hi": Fraction(3)})
    report("finite supplied readout weights normalize", weights == {"endpoint_lo": Fraction(1, 4), "endpoint_hi": Fraction(3, 4)}, str(weights))
    metric = ((Fraction(3), Fraction(1)), (Fraction(1), Fraction(2)))
    report("supplied tangent metric is SPD", is_spd_2x2(metric), str(metric))
    report("quadratic tangent norm is exact", quadratic(metric, (Fraction(1), Fraction(1, 2))) == Fraction(9, 2))
    projection = normalize({"ground": Fraction(1), "excited": Fraction(15)})
    report("projection/readout weights normalize", projection == {"ground": Fraction(1, 16), "excited": Fraction(15, 16)}, str(projection))
    has_weight_certificate = bool(weights)
    has_selector_rule = False
    report(
        "supplied Boolean classification: weights alone select blocked label",
        selector_authority(has_weight_certificate, has_selector_rule) == "blocked_missing_selector",
    )
    report(
        "supplied Boolean classification: both flags select conditional label",
        selector_authority(has_weight_certificate, not has_selector_rule) == "conditional_selector_ready",
    )
    try:
        normalize({"bad": Fraction(-1)})
        negative_rejected = False
    except ValueError:
        negative_rejected = True
    report("negative supplied weights are rejected", negative_rejected)
    # The old determinant-only criterion accepted this nonsymmetric matrix.
    nonsymmetric = ((Fraction(1), Fraction(10)), (Fraction(0), Fraction(1)))
    witness = (Fraction(1), Fraction(-1))
    old_determinant_conditions = nonsymmetric[0][0] > 0 and (
        nonsymmetric[0][0] * nonsymmetric[1][1]
        - nonsymmetric[0][1] * nonsymmetric[1][0] > 0
    )
    report("nonsymmetric counterexample defeats determinant-only SPD test",
           old_determinant_conditions and quadratic(nonsymmetric, witness) == Fraction(-8),
           f"x^T M x={quadratic(nonsymmetric, witness)}")
    report("corrected SPD helper rejects nonsymmetric counterexample",
           not is_spd_2x2(nonsymmetric))



def source_anchor_checks() -> None:
    section("Documentary scope consistency, not proof")
    require_text(AUDIT_INPUT_PATHS[0], [
        "**Type:** open_gate", "supplied finite packet data",
        "not selector/tangent/readout authority",
        "symmetric real 2x2", "positive total",
        "historical 17-row census", "No current ledger census",
    ])
    require_text(AUDIT_INPUT_PATHS[1], [
        "stipulated quartic density law",
        "fixed positive D=4 density-coefficient readout",
        "does not identify the electroweak VEV",
        "No physical selector is ruled out",
    ])


def main() -> int:
    source_anchor_checks()
    certificate_checks()
    print("INFO: no current ledger census, physical selector, metric derivation or audit verdict is claimed.")
    print("INFO: supplied Boolean classification is not a physical readiness certificate.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
